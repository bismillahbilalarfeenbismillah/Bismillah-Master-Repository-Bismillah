# Bismillah ir-Rahman ir-Rahim

# R0366 -- shvvp_v0_8_1_phase_a_m3.txt — shvvp_v0_8_1_phase_a_m3.py -- Per-fact M3 vector, M3-FIRST, and paired differences.

**Chronological Index:** 743 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** shvvp_v0_8_1_phase_a_m3.txt  
**Source Format:** txt  
**SHA-256:** `a2751e221f13698ebb3ff0a6594ee0cfbaba7c6e2a7ae3903d95d9d5e74a5925`  

---

## R0366 · shvvp_v0_8_1_phase_a_m3.txt — shvvp_v0_8_1_phase_a_m3.py -- Per-fact M3 vector, M3-FIRST, and paired differences.

- section: V. BSSG & SHVVP Protocols
- source_file: shvvp_v0_8_1_phase_a_m3.txt
- source_format: txt
- text_sha256: a2751e221f13698ebb3ff0a6594ee0cfbaba7c6e2a7ae3903d95d9d5e74a5925

"""
shvvp_v0_8_1_phase_a_m3.py -- Per-fact M3 vector, M3-FIRST, and paired differences.

SHVVP v0.8.1 Phase A Amendment, Section 1.

Rules implemented:
  - M3(f, c) = wall-clock minutes from corpus access to first immutable saved
    evidence record identifying f under condition c.
  - Right-censored at BUDGET if c did not identify f.
  - CENSORED-EARLY flag if session terminated before budget.
  - M3-FIRST(c) = min over all consequential facts f of M3(f, c).
  - Delta-M3(f) = M3(f, A) - M3(f, B) for shared facts.
  - Tie handling: secondary sort by fact_id ascending.

Text and code are the same rule written twice. A divergence is a defect.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class CensorStatus(Enum):
    OBSERVED = "OBSERVED"
    RIGHT_CENSORED_BUDGET = "RIGHT_CENSORED_BUDGET"
    CENSORED_EARLY = "CENSORED_EARLY"


class PhaseAInputError(Exception):
    """Raised for structurally invalid M3 inputs."""
    pass


@dataclass(frozen=True)
class M3Observation:
    """One M3 observation: discovery time for fact f under condition c."""
    fact_id: str
    condition: str  # "A" or "B"
    minutes: float
    censor_status: CensorStatus
    evidence_record_id: Optional[str] = None

    def __post_init__(self):
        _validate_m3_value(self.minutes, self.fact_id, self.condition)
        if self.condition not in ("A", "B"):
            raise PhaseAInputError(
                f"Condition must be 'A' or 'B', got '{self.condition}' "
                f"for fact {self.fact_id}"
            )


def _validate_m3_value(value: float, fact_id: str, condition: str) -> None:
    """Reject non-numeric, negative, NaN, and infinity M3 values."""
    if not isinstance(value, (int, float)):
        raise PhaseAInputError(
            f"M3 value must be numeric, got {type(value).__name__} "
            f"for fact {fact_id}, condition {condition}"
        )
    if math.isnan(value):
        raise PhaseAInputError(
            f"M3 value is NaN for fact {fact_id}, condition {condition}"
        )
    if math.isinf(value):
        raise PhaseAInputError(
            f"M3 value is infinite for fact {fact_id}, condition {condition}"
        )
    if value < 0:
        raise PhaseAInputError(
            f"M3 value is negative ({value}) for fact {fact_id}, "
            f"condition {condition}"
        )


@dataclass
class M3Vector:
    """The per-fact M3 observation vector for one condition."""
    condition: str
    observations: list[M3Observation] = field(default_factory=list)

    def add(self, obs: M3Observation) -> None:
        if obs.condition != self.condition:
            raise PhaseAInputError(
                f"Observation condition '{obs.condition}' does not match "
                f"vector condition '{self.condition}'"
            )
        # Check for duplicate fact_id
        existing_ids = {o.fact_id for o in self.observations}
        if obs.fact_id in existing_ids:
            raise PhaseAInputError(
                f"Duplicate fact_id '{obs.fact_id}' in condition "
                f"'{self.condition}' vector"
            )
        self.observations.append(obs)

    @property
    def fact_ids(self) -> set[str]:
        return {o.fact_id for o in self.observations}

    def get(self, fact_id: str) -> Optional[M3Observation]:
        for o in self.observations:
            if o.fact_id == fact_id:
                return o
        return None

    def m3_first(self) -> Optional[float]:
        """M3-FIRST(c) = min over all facts of M3(f, c).

        Returns None if no observations exist.
        Considers only OBSERVED values; if all are censored,
        returns the minimum censored value (which is the budget).
        """
        if not self.observations:
            return None
        return min(o.minutes for o in self.observations)


def compute_shared_set(
    vec_a: M3Vector, vec_b: M3Vector
) -> list[str]:
    """Return the shared fact set S: facts found by both conditions,
    sorted by fact_id ascending (deterministic tie-breaking)."""
    shared = vec_a.fact_ids & vec_b.fact_ids
    return sorted(shared)


@dataclass(frozen=True)
class PairedDifference:
    """Delta-M3(f) = M3(f, A) - M3(f, B) for one shared fact."""
    fact_id: str
    m3_a: float
    m3_b: float
    delta: float
    censor_a: CensorStatus
    censor_b: CensorStatus


def compute_paired_differences(
    vec_a: M3Vector, vec_b: M3Vector
) -> list[PairedDifference]:
    """Compute Delta-M3 for all shared facts.

    Returns list sorted by fact_id ascending (deterministic order).
    Raises PhaseAInputError if vec_a.condition != 'A' or vec_b.condition != 'B'.
    """
    if vec_a.condition != "A":
        raise PhaseAInputError(
            f"First vector must be condition 'A', got '{vec_a.condition}'"
        )
    if vec_b.condition != "B":
        raise PhaseAInputError(
            f"Second vector must be condition 'B', got '{vec_b.condition}'"
        )

    shared = compute_shared_set(vec_a, vec_b)
    results = []
    for fid in shared:
        obs_a = vec_a.get(fid)
        obs_b = vec_b.get(fid)
        assert obs_a is not None and obs_b is not None
        delta = obs_a.minutes - obs_b.minutes
        results.append(PairedDifference(
            fact_id=fid,
            m3_a=obs_a.minutes,
            m3_b=obs_b.minutes,
            delta=delta,
            censor_a=obs_a.censor_status,
            censor_b=obs_b.censor_status,
        ))
    return results


def compute_median(values: list[float]) -> float:
    """Standard median. Even count: average of two middle values.
    Ties preserved. Secondary sort not needed here (values are numeric).

    Raises PhaseAInputError if values is empty.
    """
    if not values:
        raise PhaseAInputError("Cannot compute median of empty list")
    s = sorted(values)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    else:
        return (s[mid - 1] + s[mid]) / 2.0


def evaluate_t2_point(
    paired_diffs: list[PairedDifference],
) -> dict:
    """Evaluate T2 point statistics (no intervals -- those are in the
    interval module).

    Returns a dict with:
      - shared_set_size: int
      - evaluable: bool (False if S is empty -- PA-Z1)
      - absolute_median: float or None
      - absolute_gate_met: bool or None (>= 30 minutes)
      - relative_ratios: list[float] (excluding M3(f,A)=0 facts)
      - relative_excluded_count: int (facts with M3(f,A)=0)
      - relative_median: float or None
      - relative_gate_met: bool or None (>= 0.20)

    The interval gate (BCa excluding 0) is evaluated by the interval module.
    """
    n = len(paired_diffs)

    if n == 0:
        # PA-Z1: S is empty
        return {
            "shared_set_size": 0,
            "evaluable": False,
            "rule": "PA-Z1",
            "absolute_median": None,
            "absolute_gate_met": None,
            "relative_ratios": [],
            "relative_excluded_count": 0,
            "relative_median": None,
            "relative_gate_met": None,
        }

    deltas = [pd.delta for pd in paired_diffs]
    abs_median = compute_median(deltas)
    abs_gate = abs_median >= 30.0

    # Relative gate: Delta-M3(f) / M3(f, A) for facts where M3(f, A) > 0
    relative_ratios = []
    excluded = 0
    for pd in paired_diffs:
        if pd.m3_a > 0:
            relative_ratios.append(pd.delta / pd.m3_a)
        else:
            excluded += 1

    rel_median = None
    rel_gate = None
    if relative_ratios:
        rel_median = compute_median(relative_ratios)
        rel_gate = rel_median >= 0.20
    else:
        # All M3(f, A) = 0 -- relative gate is NOT-EVALUABLE
        rel_gate = None

    return {
        "shared_set_size": n,
        "evaluable": True,
        "rule": None,
        "absolute_median": abs_median,
        "absolute_gate_met": abs_gate,
        "relative_ratios": relative_ratios,
        "relative_excluded_count": excluded,
        "relative_median": rel_median,
        "relative_gate_met": rel_gate,
    }


def reject_caller_supplied_statistic(**kwargs) -> None:
    """Structural rejection of pre-computed statistics.

    Any attempt to pass a pre-computed median, interval, delta,
    or T2 result is rejected. Only raw M3 vectors are accepted.
    This implements the BSSG raw-evidence discipline for Phase A.
    """
    forbidden_keys = {
        "median", "interval", "t2_result", "precomputed_delta",
        "precomputed_statistic", "caller_median", "caller_interval",
        "derived_decision", "derived_verdict",
    }
    for key in kwargs:
        if key.lower() in forbidden_keys:
            raise PhaseAInputError(
                f"Caller-supplied derived statistic rejected: '{key}'. "
                f"Only raw M3 observation vectors are admissible."
            )

---

# Bismillah ir-Rahman ir-Rahim
