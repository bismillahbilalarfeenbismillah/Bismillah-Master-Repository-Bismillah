# Bismillah ir-Rahman ir-Rahim

# R0371 -- shvvp_v0_8_3_phase_a_m3.txt — shvvp_v0_8_3_phase_a_m3.py -- Per-fact M3 vector, M3-FIRST, paired differences.

**Chronological Index:** 745 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** shvvp_v0_8_3_phase_a_m3.txt  
**Source Format:** txt  
**SHA-256:** `cd36ea1a4d95ca149387bf58317c02e1149f41fb358e77bc8cc1d60d3b91d6eb`  

---

## R0371 · shvvp_v0_8_3_phase_a_m3.txt — shvvp_v0_8_3_phase_a_m3.py -- Per-fact M3 vector, M3-FIRST, paired differences.

- section: V. BSSG & SHVVP Protocols
- source_file: shvvp_v0_8_3_phase_a_m3.txt
- source_format: txt
- merged_variants: 1 (shvvp_v0_8_2_phase_a_m3.txt)
- text_sha256: cd36ea1a4d95ca149387bf58317c02e1149f41fb358e77bc8cc1d60d3b91d6eb

"""
shvvp_v0_8_3_phase_a_m3.py -- Per-fact M3 vector, M3-FIRST, paired differences.

SHVVP v0.8.3 Phase A Amendment, Section 1.

v0.8.3 repairs from v0.8.2 carrying audit (GPT Sol + Kimi K3):
  F-SOL-082-1/F-K3-N1: Provenance downgraded to accident-guard.
  F-SOL-082-2/F-K3-N5: OBSERVED <= FROZEN_BUDGET_MINUTES enforced.
  F-SOL-082-8/F-K3-N4: PA-Z9 evaluable=False in both APIs.
  F-K3-N14: M3Vector validates on construction.
  F-K3-N16: Docstring corrected (censoring analysis withdrawn, not re-derived).
  F-K3-N17: bool rejected as numeric input.

The provenance token on PairedDifference is an ACCIDENT GUARD against
casual misuse. It is not a security boundary -- dataclasses.replace()
and direct token import can bypass it. The BSSG raw-evidence discipline
is enforced at the protocol layer (adjudicators verify raw evidence
references), not at this Python API layer.

Text and code are the same rule written twice. A divergence is a defect.
"""

from __future__ import annotations

import math
import secrets
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


# ---------------------------------------------------------------------------
# Frozen constants
# ---------------------------------------------------------------------------

FROZEN_BUDGET_MINUTES: float = 480.0
"""The fixed wall-clock budget in minutes. Frozen by this amendment.
Any executor using a different value computes a different estimand."""

_PROVENANCE_TOKEN: str = secrets.token_hex(16)
"""Module-private provenance token. PairedDifference objects created
outside compute_paired_differences() cannot carry this token and are
rejected by the interval pipeline."""


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

class CensorStatus(Enum):
    OBSERVED = "OBSERVED"
    RIGHT_CENSORED_BUDGET = "RIGHT_CENSORED_BUDGET"
    CENSORED_EARLY = "CENSORED_EARLY"


class M3FirstResult(Enum):
    """Typed result for M3-FIRST when no observed discovery exists."""
    NO_DISCOVERY = "NO_DISCOVERY"


# ---------------------------------------------------------------------------
# Errors
# ---------------------------------------------------------------------------

class PhaseAInputError(Exception):
    """Raised for structurally invalid Phase A inputs."""
    pass


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def _validate_m3_value(value: float, fact_id: str, condition: str) -> None:
    """Reject bool, non-numeric, negative, NaN, and infinity M3 values."""
    if isinstance(value, bool):
        raise PhaseAInputError(
            f"M3 value must be numeric (not bool), got {value!r} "
            f"for fact {fact_id}, condition {condition}"
        )
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


def normalize_fact_id(raw: str) -> str:
    """Frozen fact-ID normalization: strip whitespace, case-sensitive.
    (F-K3-A9: normalization must be frozen; we choose case-sensitive
    with whitespace stripping as the minimal canonical form.)"""
    if not isinstance(raw, str) or not raw.strip():
        raise PhaseAInputError(f"Fact ID must be a non-empty string, got {raw!r}")
    return raw.strip()


# ---------------------------------------------------------------------------
# M3 Observation
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class M3Observation:
    """One M3 observation: discovery time for fact f under condition c.

    Censor-status rules (frozen):
      OBSERVED: condition c identified fact f; minutes is the discovery time.
      RIGHT_CENSORED_BUDGET: condition c did NOT identify fact f within the
        budget; minutes MUST equal FROZEN_BUDGET_MINUTES.
      CENSORED_EARLY: session terminated before budget; minutes is the
        termination time; the fact was NOT identified.
    """
    fact_id: str
    condition: str  # "A" or "B"
    minutes: float
    censor_status: CensorStatus
    evidence_record_id: Optional[str] = None

    def __post_init__(self):
        normalize_fact_id(self.fact_id)  # validates non-empty
        _validate_m3_value(self.minutes, self.fact_id, self.condition)
        if self.condition not in ("A", "B"):
            raise PhaseAInputError(
                f"Condition must be 'A' or 'B', got '{self.condition}' "
                f"for fact {self.fact_id}"
            )
        # Censor-status consistency (F-K3-A3, F-K3-A10)
        if self.censor_status == CensorStatus.RIGHT_CENSORED_BUDGET:
            if self.minutes != FROZEN_BUDGET_MINUTES:
                raise PhaseAInputError(
                    f"RIGHT_CENSORED_BUDGET requires minutes == "
                    f"{FROZEN_BUDGET_MINUTES}, got {self.minutes} "
                    f"for fact {self.fact_id}, condition {self.condition}"
                )
        if self.censor_status == CensorStatus.CENSORED_EARLY:
            if self.minutes >= FROZEN_BUDGET_MINUTES:
                raise PhaseAInputError(
                    f"CENSORED_EARLY requires minutes < "
                    f"{FROZEN_BUDGET_MINUTES}, got {self.minutes} "
                    f"for fact {self.fact_id}, condition {self.condition}"
                )
        if self.censor_status == CensorStatus.OBSERVED:
            if self.evidence_record_id is None:
                raise PhaseAInputError(
                    f"OBSERVED requires evidence_record_id, got None "
                    f"for fact {self.fact_id}, condition {self.condition}"
                )
            if self.minutes > FROZEN_BUDGET_MINUTES:
                raise PhaseAInputError(
                    f"OBSERVED requires minutes <= {FROZEN_BUDGET_MINUTES}, "
                    f"got {self.minutes} for fact {self.fact_id}, "
                    f"condition {self.condition}"
                )

    @property
    def is_observed(self) -> bool:
        """True iff the condition actually identified this fact."""
        return self.censor_status == CensorStatus.OBSERVED


# ---------------------------------------------------------------------------
# M3 Vector
# ---------------------------------------------------------------------------

@dataclass
class M3Vector:
    """The per-fact M3 observation vector for one condition."""
    condition: str
    observations: list[M3Observation] = field(default_factory=list)

    def __post_init__(self):
        """Validate no duplicate fact_ids on construction (F-K3-N14)."""
        seen = set()
        for obs in self.observations:
            if obs.condition != self.condition:
                raise PhaseAInputError(
                    f"Observation condition '{obs.condition}' does not match "
                    f"vector condition '{self.condition}'"
                )
            nid = normalize_fact_id(obs.fact_id)
            if nid in seen:
                raise PhaseAInputError(
                    f"Duplicate fact_id '{obs.fact_id}' in condition "
                    f"'{self.condition}' vector (via constructor)"
                )
            seen.add(nid)

    def add(self, obs: M3Observation) -> None:
        if obs.condition != self.condition:
            raise PhaseAInputError(
                f"Observation condition '{obs.condition}' does not match "
                f"vector condition '{self.condition}'"
            )
        nid = normalize_fact_id(obs.fact_id)
        existing_ids = {normalize_fact_id(o.fact_id) for o in self.observations}
        if nid in existing_ids:
            raise PhaseAInputError(
                f"Duplicate fact_id '{obs.fact_id}' in condition "
                f"'{self.condition}' vector"
            )
        self.observations.append(obs)

    @property
    def observed_fact_ids(self) -> set[str]:
        """Fact IDs where the condition OBSERVED (actually identified)."""
        return {normalize_fact_id(o.fact_id)
                for o in self.observations if o.is_observed}

    @property
    def all_fact_ids(self) -> set[str]:
        return {normalize_fact_id(o.fact_id) for o in self.observations}

    def get(self, fact_id: str) -> Optional[M3Observation]:
        nid = normalize_fact_id(fact_id)
        for o in self.observations:
            if normalize_fact_id(o.fact_id) == nid:
                return o
        return None

    def m3_first(self) -> float | M3FirstResult:
        """M3-FIRST(c) = min observed discovery time.

        Returns M3FirstResult.NO_DISCOVERY if no OBSERVED facts exist.
        Censored observations (non-discoveries) are excluded.
        (F-K3-A3: M3-FIRST is observed-only.)
        """
        observed = [o.minutes for o in self.observations if o.is_observed]
        if not observed:
            return M3FirstResult.NO_DISCOVERY
        return min(observed)


# ---------------------------------------------------------------------------
# Shared set: OBSERVED-SHARED-ONLY (F-K3-A1 resolution)
# ---------------------------------------------------------------------------

def compute_shared_set(vec_a: M3Vector, vec_b: M3Vector) -> list[str]:
    """Return the shared fact set S: facts OBSERVED by both conditions.

    A fact that one condition did not identify (censored) is NOT in S.
    This is the single coherent rule resolving F-K3-A1.
    Sorted by normalized fact_id ascending (deterministic).
    """
    shared = vec_a.observed_fact_ids & vec_b.observed_fact_ids
    return sorted(shared)


# ---------------------------------------------------------------------------
# Paired differences with provenance token (F-K3-A6)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class PairedDifference:
    """Delta-M3(f) = M3(f, A) - M3(f, B) for one shared fact.

    Can only be created by compute_paired_differences() -- the
    _provenance field carries a module-private token that the interval
    pipeline verifies. Hand-fabricated instances are rejected.
    """
    fact_id: str
    m3_a: float
    m3_b: float
    delta: float
    censor_a: CensorStatus
    censor_b: CensorStatus
    _provenance: str = ""

    def verify_provenance(self) -> None:
        """Raise if this was not created by compute_paired_differences()."""
        if self._provenance != _PROVENANCE_TOKEN:
            raise PhaseAInputError(
                f"PairedDifference for fact '{self.fact_id}' has invalid "
                f"provenance. Only compute_paired_differences() may create "
                f"these objects. Caller-supplied derived facts are rejected."
            )


def compute_paired_differences(
    vec_a: M3Vector, vec_b: M3Vector
) -> list[PairedDifference]:
    """Compute Delta-M3 for all shared facts (observed by both).

    Both observations MUST be OBSERVED (by S-membership rule).
    Returns list sorted by normalized fact_id ascending.
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
        assert obs_a.is_observed and obs_b.is_observed  # by S-membership
        delta = obs_a.minutes - obs_b.minutes
        results.append(PairedDifference(
            fact_id=fid,
            m3_a=obs_a.minutes,
            m3_b=obs_b.minutes,
            delta=delta,
            censor_a=obs_a.censor_status,
            censor_b=obs_b.censor_status,
            _provenance=_PROVENANCE_TOKEN,
        ))
    return results


# ---------------------------------------------------------------------------
# Median
# ---------------------------------------------------------------------------

def compute_median(values: list[float]) -> float:
    """Standard median. Even count: average of two middle values.
    Raises PhaseAInputError if values is empty."""
    if not values:
        raise PhaseAInputError("Cannot compute median of empty list")
    s = sorted(values)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2.0


# ---------------------------------------------------------------------------
# T2 point statistics
# ---------------------------------------------------------------------------

def evaluate_t2_point(
    paired_diffs: list[PairedDifference],
) -> dict:
    """Evaluate T2 point statistics (intervals computed separately).

    PA-Z1: S empty -> NOT-EVALUABLE.
    PA-Z9: All M3(f,A)=0 -> relative gate NOT-EVALUABLE (F-K3-A4).
    """
    # Verify provenance on every input (F-K3-A6)
    for pd in paired_diffs:
        pd.verify_provenance()

    n = len(paired_diffs)

    if n == 0:
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

    relative_ratios = []
    excluded = 0
    for pd in paired_diffs:
        if pd.m3_a > 0:
            relative_ratios.append(pd.delta / pd.m3_a)
        else:
            excluded += 1

    if not relative_ratios:
        # PA-Z9: all M3(f,A) = 0 -> relative gate NOT-EVALUABLE
        return {
            "shared_set_size": n,
            "evaluable": False,
            "rule": "PA-Z9",
            "absolute_median": abs_median,
            "absolute_gate_met": abs_gate,
            "relative_ratios": [],
            "relative_excluded_count": excluded,
            "relative_median": None,
            "relative_gate_met": None,
        }

    rel_median = compute_median(relative_ratios)
    rel_gate = rel_median >= 0.20

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

---

# Bismillah ir-Rahman ir-Rahim
