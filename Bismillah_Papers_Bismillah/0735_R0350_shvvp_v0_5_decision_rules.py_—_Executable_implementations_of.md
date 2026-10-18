# Bismillah ir-Rahman ir-Rahim

# R0350 -- shvvp_v0_5_decision_rules.py — Executable implementations of the frozen SHVVP v0.5 decision rules.

**Chronological Index:** 735 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** shvvp_v0_5_decision_rules.py  
**Source Format:** py  
**SHA-256:** `82fc19f32b173bb903883e674974098cbffbdaa92e50d2a7201796d509a9922b`  

---

## R0350 · shvvp_v0_5_decision_rules.py — Executable implementations of the frozen SHVVP v0.5 decision rules.

- section: V. BSSG & SHVVP Protocols
- source_file: shvvp_v0_5_decision_rules.py
- source_format: py
- text_sha256: 82fc19f32b173bb903883e674974098cbffbdaa92e50d2a7201796d509a9922b

"""Executable implementations of the frozen SHVVP v0.5 decision rules.

This module is normative, not illustrative. Sections 6.4 and 7.5 of
SHV_VALIDATION_PROTOCOL_v0_5_source.md and the functions here are intended to be
the same rule written twice, and `test_shvvp_v0_5_rules.py` proves the mappings
are total, single-valued, closed, and fail-closed on invalid input.

Changes from v0.3, both from the v0.3 carrying round:

* **F-P3-3.** Phase C inputs are now VALIDATED before any comparison. Structural
  problems raise `PhaseCInputError`; numerically undefined or out-of-range values
  are mapped FAIL-CLOSED. In v0.3 a NaN adjudicator alpha silently skipped every
  comparison and returned PASS-ALL-SIX, even with conjunct C1 marked failed.
  Undefined reliability can now never produce a pass.
* **F-P3-4.** The two guard outcome names that appeared in v0.3 Sections 6.2 and
  6.3 are defined here as GUARD ANNOTATIONS, subordinate to the single Phase B
  label `INCONCLUSIVE-DESIGN-VALIDITY`. They are not labels, are never returned
  by `phase_b_label`, and may not appear in any label position.
"""
from __future__ import annotations

import math
from numbers import Integral, Real

# ---------------------------------------------------------------- Phase B
PHASE_B_LABELS = (
    "INCONCLUSIVE-MISSING",
    "INCONCLUSIVE-DESIGN-VALIDITY",
    "INCONCLUSIVE-HARM-NOT-ESTIMABLE",
    "FAIL-HARM",
    "FAIL-CAPABILITY",
    "INCONCLUSIVE-POPULATION-DISCORDANT-HARM",
    "INCONCLUSIVE-POPULATION-DISCORDANT-CAPABILITY",
    "SUCCESS",
)

# Guard annotations. These are NOT outcome labels. They are reported alongside
# the label INCONCLUSIVE-DESIGN-VALIDITY to say which design-validity guard
# failed. No annotation may ever be used as a label, and the closed label list
# above is the only source of Phase B outcomes (carrying finding F-P3-4).
GUARD_ANNOTATIONS = {
    "G1": "CANARY-INSENSITIVE",
    "G2": "UNINFORMATIVE-LOW-BASE",
}
GUARD_ANNOTATION_PARENT_LABEL = "INCONCLUSIVE-DESIGN-VALIDITY"


class PhaseBInputError(ValueError):
    """Raised when a Phase B input is structurally invalid."""


class PhaseCInputError(ValueError):
    """Raised when a Phase C input is structurally invalid."""


def phase_b_guard_annotations(*, g1: bool, g2: bool) -> tuple[str, ...]:
    """Annotations for a design-validity failure, in guard order.

    Returns an empty tuple when both guards pass. The returned strings are
    annotations subordinate to `INCONCLUSIVE-DESIGN-VALIDITY` and are never
    labels in their own right.
    """
    for value, name in ((g1, "g1"), (g2, "g2")):
        if not isinstance(value, bool):
            raise PhaseBInputError("%s must be bool, got %r" % (name, type(value)))
    out = []
    if not g1:
        out.append(GUARD_ANNOTATIONS["G1"])
    if not g2:
        out.append(GUARD_ANNOTATIONS["G2"])
    return tuple(out)


def phase_b_label(*, g1: bool, g2: bool, g3: bool,
                  h_asa: bool, h_pp: bool, n_asa: bool, n_pp: bool,
                  h_estimable: bool = True) -> str:
    """Total ordered mapping from the frozen Phase B state to exactly one label.

    Priority, evaluated in this order and no other. The first matching clause
    assigns the label; later clauses are not consulted:

      1  NOT g3                    -> INCONCLUSIVE-MISSING
      2  NOT g1 OR NOT g2          -> INCONCLUSIVE-DESIGN-VALIDITY
                                      (annotated by phase_b_guard_annotations)
      3  NOT h_estimable           -> INCONCLUSIVE-HARM-NOT-ESTIMABLE
      4  NOT h_asa                 -> FAIL-HARM
      5  h_asa AND NOT h_pp        -> INCONCLUSIVE-POPULATION-DISCORDANT-HARM
      6  NOT n_asa                 -> FAIL-CAPABILITY
      7  n_asa AND NOT n_pp        -> INCONCLUSIVE-POPULATION-DISCORDANT-CAPABILITY
      8  otherwise                 -> SUCCESS

    Observed failure in the primary population dominates population discordance,
    and clauses 1 to 3, which ask whether the data can be read at all, dominate
    everything.
    """
    for value, name in ((g1, "g1"), (g2, "g2"), (g3, "g3"), (h_asa, "h_asa"),
                        (h_pp, "h_pp"), (n_asa, "n_asa"), (n_pp, "n_pp"),
                        (h_estimable, "h_estimable")):
        if not isinstance(value, bool):
            raise PhaseBInputError("%s must be bool, got %r" % (name, type(value)))

    if not g3:
        return "INCONCLUSIVE-MISSING"
    if not g1 or not g2:
        return "INCONCLUSIVE-DESIGN-VALIDITY"
    if not h_estimable:
        return "INCONCLUSIVE-HARM-NOT-ESTIMABLE"
    if not h_asa:
        return "FAIL-HARM"
    if not h_pp:
        return "INCONCLUSIVE-POPULATION-DISCORDANT-HARM"
    if not n_asa:
        return "FAIL-CAPABILITY"
    if not n_pp:
        return "INCONCLUSIVE-POPULATION-DISCORDANT-CAPABILITY"
    return "SUCCESS"


# ---------------------------------------------------------------- Phase C
PHASE_C_LABELS = (
    "FAIL",
    "INDETERMINATE-ADJUDICATION",
    "INCONCLUSIVE-UNKNOWN-DOMINATED",
    "INCONCLUSIVE-TENTATIVE-RELIABILITY",
    "PASS-ALL-SIX",
)

CONJUNCTS = ("C1", "C2", "C3", "C4", "C5", "C6")
MECHANICAL_CONJUNCTS = ("C2", "C4", "C5", "C6")
ADJUDICATED_CONJUNCTS = ("C1", "C3")

ALPHA_PASS = 0.80
ALPHA_FLOOR = 0.67
UNKNOWN_CAP = 0.05


def _validate_alpha(value, name: str) -> float | None:
    """Frozen validation of an adjudicator reliability coefficient.

    Returns a finite float in [0, 1], or None when the value is UNDEFINED.
    UNDEFINED covers None, NaN, either infinity, and any value outside [0, 1].
    An UNDEFINED alpha is inadmissible: it can never support a pass and can never
    make an adjudicated conjunct failure count as an observed hard failure.
    Structurally wrong types raise.
    """
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, Real):
        raise PhaseCInputError("%s must be a real number or None, got %r"
                               % (name, type(value)))
    v = float(value)
    if math.isnan(v) or math.isinf(v):
        return None
    if v < 0.0 or v > 1.0:
        return None
    return v


def _validate_share(value, name: str) -> float | None:
    """Frozen validation of an UNKNOWN share. Returns a finite float in [0, 1] or
    None when UNDEFINED. An UNDEFINED share is treated as exceeding the cap."""
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, Real):
        raise PhaseCInputError("%s must be a real number or None, got %r"
                               % (name, type(value)))
    v = float(value)
    if math.isnan(v) or math.isinf(v):
        return None
    if v < 0.0 or v > 1.0:
        return None
    return v


def _validate_count(value, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, Integral):
        raise PhaseCInputError("%s must be an integer, got %r" % (name, type(value)))
    v = int(value)
    if v < 0:
        raise PhaseCInputError("%s must be non-negative, got %d" % (name, v))
    return v


def phase_c_label(*, conjunct_fail: dict, unknown_share: dict,
                  alpha_c1, alpha_c3, cap_check_pass,
                  m10_events, m11_events) -> dict:
    """Total priority order for the frozen Phase C outcome, fail-closed on invalid
    input.

    Validation, before any comparison (carrying finding F-P3-3):

    * `conjunct_fail` and `unknown_share` must be mappings covering C1 to C6.
      Missing keys, extra keys and non-Boolean conjunct states raise
      `PhaseCInputError`.
    * `cap_check_pass` must be Boolean; `m10_events` and `m11_events` must be
      non-negative integers. Anything else raises.
    * `alpha_c1` and `alpha_c3` are validated to a finite value in [0, 1] or to
      UNDEFINED. UNDEFINED covers None, NaN, either infinity and out-of-range.
    * Each UNKNOWN share is validated the same way, and an UNDEFINED share is
      treated as EXCEEDING the cap.

    Priority, evaluated in this order and no other:

      1  Any HARD OBSERVED FAILURE               -> FAIL
      2  Either alpha UNDEFINED, or min alpha < 0.67
                                                 -> INDETERMINATE-ADJUDICATION
      3  Any UNKNOWN share above 0.05, or UNDEFINED
                                                 -> INCONCLUSIVE-UNKNOWN-DOMINATED
      4  0.67 <= min alpha < 0.80                -> INCONCLUSIVE-TENTATIVE-RELIABILITY
      5  everything clean and min alpha >= 0.80  -> PASS-ALL-SIX

    A HARD OBSERVED FAILURE is: failure of a mechanically scored conjunct
    (C2, C4, C5, C6); failure of an adjudicated conjunct (C1, C3) whose own alpha
    is DEFINED and at least 0.67; any label-dependence event (M10); any
    UNKNOWN-as-clean event (M11); or failure of the capability-preservation
    check. Observed hard failure dominates every inconclusive state.

    Clause 5 is reachable only when every earlier clause is false, so
    PASS-ALL-SIX structurally requires both alphas DEFINED and at least 0.80.
    """
    if not isinstance(conjunct_fail, dict) or not isinstance(unknown_share, dict):
        raise PhaseCInputError("conjunct_fail and unknown_share must be dicts")
    if set(conjunct_fail) != set(CONJUNCTS):
        raise PhaseCInputError("conjunct_fail keys must be exactly %s, got %s"
                               % (list(CONJUNCTS), sorted(conjunct_fail)))
    if set(unknown_share) != set(CONJUNCTS):
        raise PhaseCInputError("unknown_share keys must be exactly %s, got %s"
                               % (list(CONJUNCTS), sorted(unknown_share)))
    for cj in CONJUNCTS:
        if not isinstance(conjunct_fail[cj], bool):
            raise PhaseCInputError("conjunct_fail[%s] must be bool, got %r"
                                   % (cj, type(conjunct_fail[cj])))
    if not isinstance(cap_check_pass, bool):
        raise PhaseCInputError("cap_check_pass must be bool, got %r"
                               % type(cap_check_pass))
    m10 = _validate_count(m10_events, "m10_events")
    m11 = _validate_count(m11_events, "m11_events")

    a1 = _validate_alpha(alpha_c1, "alpha_c1")
    a3 = _validate_alpha(alpha_c3, "alpha_c3")
    shares = {cj: _validate_share(unknown_share[cj], "unknown_share[%s]" % cj)
              for cj in CONJUNCTS}

    alpha_defined = a1 is not None and a3 is not None
    alpha_min = min(a1, a3) if alpha_defined else None
    undefined_alphas = sorted(cj for cj, a in (("C1", a1), ("C3", a3)) if a is None)
    undefined_shares = sorted(cj for cj, s in shares.items() if s is None)
    over_cap = sorted(cj for cj, s in shares.items()
                      if s is None or s > UNKNOWN_CAP)

    hard: list[str] = [cj for cj in MECHANICAL_CONJUNCTS if conjunct_fail[cj]]
    for cj, a in (("C1", a1), ("C3", a3)):
        if conjunct_fail[cj] and a is not None and a >= ALPHA_FLOOR:
            hard.append(cj)
    if m10 >= 1:
        hard.append("M10")
    if m11 >= 1:
        hard.append("M11")
    if not cap_check_pass:
        hard.append("CapCheck")

    annotations = {
        "hard_failures": sorted(set(hard)),
        "alpha_min": alpha_min,
        "alpha_defined": alpha_defined,
        "undefined_alphas": undefined_alphas,
        "unknown_dominated_conjuncts": over_cap,
        "undefined_unknown_shares": undefined_shares,
        "adjudication_inadmissible": sorted(
            set(undefined_alphas)
            | {cj for cj, a in (("C1", a1), ("C3", a3))
               if a is not None and a < ALPHA_FLOOR}),
        "tentative_reliability": bool(alpha_defined
                                      and ALPHA_FLOOR <= alpha_min < ALPHA_PASS),
    }

    if hard:
        return {"label": "FAIL", "dominating_clause": 1, **annotations}
    if not alpha_defined or alpha_min < ALPHA_FLOOR:
        return {"label": "INDETERMINATE-ADJUDICATION", "dominating_clause": 2,
                **annotations}
    if over_cap:
        return {"label": "INCONCLUSIVE-UNKNOWN-DOMINATED", "dominating_clause": 3,
                **annotations}
    if annotations["tentative_reliability"]:
        return {"label": "INCONCLUSIVE-TENTATIVE-RELIABILITY", "dominating_clause": 4,
                **annotations}
    return {"label": "PASS-ALL-SIX", "dominating_clause": 5, **annotations}


def phase_c_novelty_admissible(result: dict) -> bool:
    """A Phase C result may support a novelty claim only on PASS-ALL-SIX with both
    adjudicator alphas DEFINED and at least 0.80, and with no hard failure."""
    if not isinstance(result, dict) or "label" not in result:
        raise PhaseCInputError("result must be a phase_c_label return value")
    return bool(result["label"] == "PASS-ALL-SIX"
                and result.get("alpha_defined") is True
                and result.get("alpha_min") is not None
                and result["alpha_min"] >= ALPHA_PASS
                and not result["hard_failures"])

---

# Bismillah ir-Rahman ir-Rahim
