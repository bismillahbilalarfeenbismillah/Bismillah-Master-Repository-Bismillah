# Bismillah ir-Rahman ir-Rahim

# R0374 -- shvvp_v0_8_4_phase_a_m3.txt — shvvp_v0_8_4_phase_a_m3.py -- Per-fact M3 vector, M3-FIRST, paired differences.

**Chronological Index:** 747 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** shvvp_v0_8_4_phase_a_m3.txt  
**Source Format:** txt  
**SHA-256:** `4a0b055e2f88db441775fc783e1b2ed9acda8e8c79eaf9e041cd384b8f84b268`  

---

## R0374 · shvvp_v0_8_4_phase_a_m3.txt — shvvp_v0_8_4_phase_a_m3.py -- Per-fact M3 vector, M3-FIRST, paired differences.

- section: V. BSSG & SHVVP Protocols
- source_file: shvvp_v0_8_4_phase_a_m3.txt
- source_format: txt
- merged_variants: 3 (xz_protocol_phase_a_m3.py; xz_protocol_phase_a_m3.py.txt; xz_protocol_phase_a_m3.txt)
- text_sha256: 4a0b055e2f88db441775fc783e1b2ed9acda8e8c79eaf9e041cd384b8f84b268

"""
shvvp_v0_8_4_phase_a_m3.py -- Per-fact M3 vector, M3-FIRST, paired differences.

SHVVP v0.8.4 Phase A Amendment, Section 1.

v0.8.4 repairs from v0.8.3 carrying audit (GPT Sol + Kimi K3):
  F-SOL-083-1: M3Vector is now FROZEN with observations as tuple.
  F-SOL-083-2: censor_status enum membership validated first.
  F-SOL-083-5: M3 endpoint declared SUBSTANTIVE change from parent.
  F-SOL-083-9/F-K3-083-6: bool rejected uniformly at all entry points.
  F-SOL-083-10/F-K3-083-10: raw exceptions wrapped in PhaseAInputError.
  F-K3-083-2: non-finite ratios excluded and counted (PA-Z13).
  F-K3-083-5: provenance docstrings aligned with accident-guard.
  F-K3-083-11: evidence_record_id must be non-empty str for OBSERVED;
               forbidden on non-discovery statuses.
  F-K3-083-14: dead branches removed.

SUBSTANTIVE ENDPOINT CHANGE (declared, not silent): The parent SHVVP
v0.8 defines M3 as ending at the "first correctly adjudicated
consequential fact." This implementation times to the first immutable
saved evidence record that identifies the fact. The distinction is
recorded as amendment entry PA-A12. No scalar-preservation claim
is made for inputs where adjudication time differs from evidence time.

The provenance token on PairedDifference is an ACCIDENT GUARD against
casual misuse. It is NOT a security boundary. dataclasses.replace()
and direct token import can bypass it. The BSSG raw-evidence discipline
is enforced at the protocol layer, not at this Python API layer.
"""

from __future__ import annotations

import math
import secrets
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


FROZEN_BUDGET_MINUTES: float = 480.0

_PROVENANCE_TOKEN: str = secrets.token_hex(16)


class CensorStatus(Enum):
    OBSERVED = "OBSERVED"
    RIGHT_CENSORED_BUDGET = "RIGHT_CENSORED_BUDGET"
    CENSORED_EARLY = "CENSORED_EARLY"


class M3FirstResult(Enum):
    NO_DISCOVERY = "NO_DISCOVERY"


class PhaseAInputError(Exception):
    pass


def _reject_bool(value, name: str) -> None:
    if isinstance(value, bool):
        raise PhaseAInputError(f"{name} must not be bool, got {value!r}")


def _validate_numeric(value, name: str) -> float:
    """Validate and coerce to float. Rejects bool, non-numeric, NaN, Inf, negative."""
    _reject_bool(value, name)
    try:
        fval = float(value)
    except (TypeError, ValueError, OverflowError) as e:
        raise PhaseAInputError(f"{name} must be numeric, got {type(value).__name__}: {e}") from e
    if math.isnan(fval):
        raise PhaseAInputError(f"{name} is NaN")
    if math.isinf(fval):
        raise PhaseAInputError(f"{name} is infinite")
    if fval < 0:
        raise PhaseAInputError(f"{name} is negative ({fval})")
    return fval


def normalize_fact_id(raw: str) -> str:
    """Frozen: strip ASCII whitespace, case-sensitive."""
    if not isinstance(raw, str) or not raw.strip():
        raise PhaseAInputError(f"Fact ID must be a non-empty string, got {raw!r}")
    return raw.strip()


@dataclass(frozen=True)
class M3Observation:
    """One M3 observation: discovery time for fact f under condition c."""
    fact_id: str
    condition: str
    minutes: float
    censor_status: CensorStatus
    evidence_record_id: Optional[str] = None

    def __post_init__(self):
        # Enum membership FIRST (F-SOL-083-2)
        if not isinstance(self.censor_status, CensorStatus):
            raise PhaseAInputError(
                f"censor_status must be a CensorStatus enum member, "
                f"got {type(self.censor_status).__name__}: {self.censor_status!r}"
            )
        normalize_fact_id(self.fact_id)
        _validate_numeric(self.minutes, f"M3({self.fact_id},{self.condition})")
        if self.condition not in ("A", "B"):
            raise PhaseAInputError(f"Condition must be 'A' or 'B', got '{self.condition}'")

        if self.censor_status == CensorStatus.RIGHT_CENSORED_BUDGET:
            if self.minutes != FROZEN_BUDGET_MINUTES:
                raise PhaseAInputError(
                    f"RIGHT_CENSORED_BUDGET requires minutes == {FROZEN_BUDGET_MINUTES}, "
                    f"got {self.minutes}")
            if self.evidence_record_id is not None:
                raise PhaseAInputError(
                    f"RIGHT_CENSORED_BUDGET must not carry evidence_record_id")
        elif self.censor_status == CensorStatus.CENSORED_EARLY:
            if self.minutes >= FROZEN_BUDGET_MINUTES:
                raise PhaseAInputError(
                    f"CENSORED_EARLY requires minutes < {FROZEN_BUDGET_MINUTES}, "
                    f"got {self.minutes}")
            if self.evidence_record_id is not None:
                raise PhaseAInputError(
                    f"CENSORED_EARLY must not carry evidence_record_id")
        elif self.censor_status == CensorStatus.OBSERVED:
            if not isinstance(self.evidence_record_id, str) or not self.evidence_record_id.strip():
                raise PhaseAInputError(
                    f"OBSERVED requires a non-empty str evidence_record_id, "
                    f"got {self.evidence_record_id!r}")
            if self.minutes > FROZEN_BUDGET_MINUTES:
                raise PhaseAInputError(
                    f"OBSERVED requires minutes <= {FROZEN_BUDGET_MINUTES}, "
                    f"got {self.minutes}")

    @property
    def is_observed(self) -> bool:
        return self.censor_status == CensorStatus.OBSERVED


@dataclass(frozen=True)
class M3Vector:
    """Immutable per-fact M3 vector for one condition.

    observations is a tuple (immutable). No mutation after construction.
    (F-SOL-083-1: closes the mutable-list bypass permanently.)
    """
    condition: str
    observations: tuple[M3Observation, ...] = ()

    def __post_init__(self):
        if not isinstance(self.observations, tuple):
            try:
                object.__setattr__(self, 'observations', tuple(self.observations))
            except TypeError as e:
                raise PhaseAInputError(f"observations must be iterable: {e}") from e
        seen = set()
        for obs in self.observations:
            if not isinstance(obs, M3Observation):
                raise PhaseAInputError(
                    f"Each observation must be M3Observation, got {type(obs).__name__}")
            if obs.condition != self.condition:
                raise PhaseAInputError(
                    f"Observation condition '{obs.condition}' != vector '{self.condition}'")
            nid = normalize_fact_id(obs.fact_id)
            if nid in seen:
                raise PhaseAInputError(
                    f"Duplicate fact_id '{obs.fact_id}' in condition '{self.condition}'")
            seen.add(nid)

    def with_obs(self, obs: M3Observation) -> 'M3Vector':
        """Return a NEW vector with obs appended. Original unchanged."""
        return M3Vector(self.condition, self.observations + (obs,))

    @property
    def observed_fact_ids(self) -> set[str]:
        return {normalize_fact_id(o.fact_id) for o in self.observations if o.is_observed}

    def get(self, fact_id: str) -> Optional[M3Observation]:
        nid = normalize_fact_id(fact_id)
        for o in self.observations:
            if normalize_fact_id(o.fact_id) == nid:
                return o
        return None

    def m3_first(self) -> float | M3FirstResult:
        """Observed-only scalar summary."""
        observed = [o.minutes for o in self.observations if o.is_observed]
        return min(observed) if observed else M3FirstResult.NO_DISCOVERY


def compute_shared_set(vec_a: M3Vector, vec_b: M3Vector) -> list[str]:
    """S = facts OBSERVED by both conditions. Sorted ascending."""
    return sorted(vec_a.observed_fact_ids & vec_b.observed_fact_ids)


@dataclass(frozen=True)
class PairedDifference:
    """Delta-M3(f) = M3(f,A) - M3(f,B) for one shared fact.

    The _provenance field is an ACCIDENT GUARD (not a security boundary).
    dataclasses.replace() and direct token import can bypass it.
    See module docstring.
    """
    fact_id: str
    m3_a: float
    m3_b: float
    delta: float
    censor_a: CensorStatus
    censor_b: CensorStatus
    _provenance: str = ""

    def verify_provenance(self) -> None:
        if self._provenance != _PROVENANCE_TOKEN:
            raise PhaseAInputError(
                f"PairedDifference '{self.fact_id}' has invalid provenance. "
                f"This is an accident guard, not a security boundary.")


def compute_paired_differences(
    vec_a: M3Vector, vec_b: M3Vector
) -> list[PairedDifference]:
    if vec_a.condition != "A":
        raise PhaseAInputError(f"First vector must be 'A', got '{vec_a.condition}'")
    if vec_b.condition != "B":
        raise PhaseAInputError(f"Second vector must be 'B', got '{vec_b.condition}'")
    shared = compute_shared_set(vec_a, vec_b)
    results = []
    for fid in shared:
        oa, ob = vec_a.get(fid), vec_b.get(fid)
        assert oa and ob and oa.is_observed and ob.is_observed
        delta = oa.minutes - ob.minutes
        results.append(PairedDifference(
            fid, oa.minutes, ob.minutes, delta,
            oa.censor_status, ob.censor_status, _PROVENANCE_TOKEN))
    return results


def compute_median(values: list[float]) -> float:
    """Standard median. Rejects bool."""
    if not values:
        raise PhaseAInputError("Cannot compute median of empty list")
    for v in values:
        _reject_bool(v, "median input")
    s = sorted(values)
    n = len(s)
    mid = n // 2
    return s[mid] if n % 2 == 1 else (s[mid-1] + s[mid]) / 2.0


def evaluate_t2_point(paired_diffs: list[PairedDifference]) -> dict:
    """T2 point statistics. PA-Z1/PA-Z9/PA-Z13."""
    for pd in paired_diffs:
        pd.verify_provenance()
    n = len(paired_diffs)
    if n == 0:
        return {"shared_set_size": 0, "evaluable": False, "rule": "PA-Z1",
                "absolute_median": None, "absolute_gate_met": None,
                "relative_ratios": [], "relative_excluded_count": 0,
                "relative_nonfinite_count": 0,
                "relative_median": None, "relative_gate_met": None}

    deltas = [pd.delta for pd in paired_diffs]
    abs_median = compute_median(deltas)
    abs_gate = abs_median >= 30.0

    ratios, excluded, nonfinite = [], 0, 0
    for pd in paired_diffs:
        if pd.m3_a == 0:
            excluded += 1
        else:
            r = pd.delta / pd.m3_a
            if math.isfinite(r):
                ratios.append(r)
            else:
                nonfinite += 1  # PA-Z13

    if not ratios:
        rule = "PA-Z9" if excluded == n else "PA-Z13"
        return {"shared_set_size": n, "evaluable": False, "rule": rule,
                "absolute_median": abs_median, "absolute_gate_met": abs_gate,
                "relative_ratios": [], "relative_excluded_count": excluded,
                "relative_nonfinite_count": nonfinite,
                "relative_median": None, "relative_gate_met": None}

    rel_median = compute_median(ratios)
    return {"shared_set_size": n, "evaluable": True, "rule": None,
            "absolute_median": abs_median, "absolute_gate_met": abs_gate,
            "relative_ratios": ratios, "relative_excluded_count": excluded,
            "relative_nonfinite_count": nonfinite,
            "relative_median": rel_median, "relative_gate_met": rel_median >= 0.20}

---

# Bismillah ir-Rahman ir-Rahim
