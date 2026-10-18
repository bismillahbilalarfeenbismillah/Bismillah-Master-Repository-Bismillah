# Bismillah ir-Rahman ir-Rahim

# R0356 -- shvvp_v0_5_route_gates.py — Executable route-level DESCRIPTIVE GATES for the frozen SHVVP v0.5 protocol.

**Chronological Index:** 740 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** shvvp_v0_5_route_gates.py  
**Source Format:** py  
**SHA-256:** `4fe4ad82a00672d72dae1cd2a05ea55ed6bc57800a3691c8a0b7c6ea6e1afbd3`  

---

## R0356 · shvvp_v0_5_route_gates.py — Executable route-level DESCRIPTIVE GATES for the frozen SHVVP v0.5 protocol.

- section: V. BSSG & SHVVP Protocols
- source_file: shvvp_v0_5_route_gates.py
- source_format: py
- text_sha256: 4fe4ad82a00672d72dae1cd2a05ea55ed6bc57800a3691c8a0b7c6ea6e1afbd3

"""Executable route-level DESCRIPTIVE GATES for the frozen SHVVP v0.5 protocol.

WHAT THIS MODULE IS, AND WHAT IT IS NOT
---------------------------------------
It evaluates the six novelty routes as **descriptive, context-scoped gates** over
raw evidence counts. It performs **no** statistical inference of any kind. There
is no p-value, no null hypothesis, no confidence bound, no false-discovery-rate
procedure, no significance, and no population-level or generalizing claim
anywhere in this module or in the contract sections it implements. The strongest
label it can return is `SUPPORTED-DESCRIPTIVE`.

WHY, AND WHAT WAS WITHDRAWN
---------------------------
The v0.4 carrying round (GPT-class Seat A) returned HALT with two blocking
findings. Both are accepted in full.

* **F-P4-2 (HIGH, BLOCKING).** v0.4 tested five route components with an exact
  one-sided binomial boundary test, justifying an iid Bernoulli cluster model on
  the ground that task-by-variant cells and Phase C targets are "units of
  allocation". That justification is wrong about the frozen design: sessions are
  randomised WITHIN each Phase B cell, every Phase C target is crossed with both
  arms, and the cells and targets are fixed heterogeneous tasks rather than
  independently allocated or iid-sampled clusters. Independence alone does not
  make a sum binomial; a common success probability or a stated superpopulation
  sampling model is also required, and neither exists here. The producer does not
  have a defensible frozen population model for the actual fixed, heterogeneous,
  paired design, and will not manufacture one after the fact. **Therefore ALL
  route-level inferential claims are WITHDRAWN**: the exact binomial test, the
  Clopper-Pearson bound, the re-anchored nulls, the attainability record, family
  F3a, and the application of Benjamini-Hochberg to route evidence are all gone
  from the normative path, and every one of the eleven components is now Class G,
  descriptive gate-only. The withdrawn arithmetic was correct; its use as
  inference was not, and correct arithmetic used under an unjustified model is
  still an invalid claim.

* **F-P4-1 (HIGH, BLOCKING).** v0.4's "fail-closed evidence binding" was
  bypassable three ways: a caller could assert `hard_gate_violated=False` while
  supplying catastrophic raw counts (50 of 50 clusters "successful" with 0 of 100
  raw items passing) because raw counts were optional and their threshold was
  never enforced; the module token was importable, so direct construction of a
  derived outcome succeeded; and `dataclasses.replace` preserved a genuine
  outcome's token while replacing its evaluability and p-value. All three
  produced SUPPORTED-INFERENTIAL. **Therefore derived outcomes are no longer
  admissible evidence at all.** `route_claims` accepts ONLY validated raw
  evidence records and recomputes every gate itself. There is no token, no
  caller-supplied gate verdict, no caller-supplied evaluability, and no derived
  object that any caller can construct, mutate, replace or forge into support:
  the only input is raw counts, and the only authority over what those counts
  mean is this module.

THE FROZEN EVIDENCE CONTRACT
---------------------------
Each component fixes, before data: the required raw fields; the denominator; the
minimum evidence count; the exact descriptive threshold on the pass share; and
whether it carries a zero-tolerance violation counter. Every field is mandatory.
Missing fields, extra fields, non-integer or negative counts, a numerator above
its denominator, or a violation count above its denominator are REJECTED. Counts
below the frozen minimum are NOT EVALUABLE and can support nothing.
"""
from __future__ import annotations

from dataclasses import dataclass
from numbers import Integral
from typing import Any, Mapping

# ---------------------------------------------------------------- vocabulary
# Closed. Five labels. There is deliberately no inferential label: the strings
# "SUPPORTED-INFERENTIAL" and "DESCRIPTIVE-ONLY" of v0.4 are WITHDRAWN and appear
# nowhere as attainable outcomes.
ROUTE_CLAIM_LABELS = (
    "OUT OF SCOPE",
    "FAILED",
    "NOT EVALUABLE",
    "NOT SUPPORTED",
    "SUPPORTED-DESCRIPTIVE",
)

WITHDRAWN_LABELS = ("SUPPORTED-INFERENTIAL", "DESCRIPTIVE-ONLY")


class RouteInputError(ValueError):
    """Raised when raw evidence is structurally invalid. Nothing is returned."""


@dataclass(frozen=True)
class GateSpec:
    """Frozen evidence contract for one route component. All components are
    Class G: descriptive gate-only, no inference, no error control."""
    key: str
    route: str
    phase: str
    unit: str                    # the counted unit, that is the denominator
    denominator_field: str
    numerator_field: str
    violation_field: str | None  # zero-tolerance counter, or None
    min_items: int               # frozen minimum evidence count
    threshold: float             # frozen exact descriptive threshold on the share
    statement: str               # the only statement this gate can support
    scope_limit: str             # the limitation that must accompany that statement

    @property
    def required_fields(self) -> tuple[str, ...]:
        f = [self.denominator_field, self.numerator_field]
        if self.violation_field:
            f.append(self.violation_field)
        return tuple(f)


CLASS = "G"   # every component. There is no Class I in v0.5.

REGISTRY: tuple[GateSpec, ...] = (
    GateSpec("R1-A", "R1", "A", "sealed-ledger consequential fact",
             "facts_examined", "facts_incremental", None, 3, 1.0,
             "on this one historical case, SHV surfaced consequential ledger facts "
             "that the provenance baseline missed",
             "single case, no randomisation, no comparison across conditions"),
    GateSpec("R2-A", "R2", "A", "planted caller-context branch",
             "branches_planted", "branches_typed", "branches_dropped_silently", 16,
             0.75,
             "on this one historical case, incompleteness was typed rather than "
             "silently dropped",
             "single case, 16 planted branches, no randomisation"),
    GateSpec("R2-B", "R2", "B", "denied effect request",
             "denials_total", "denials_typed", None, 50, 0.98,
             "in this run, denied effect requests carried a typed reason at the "
             "frozen share",
             "descriptive share within this run only; no population claim, no "
             "significance, no generalization beyond the tested tasks and models"),
    GateSpec("R3-A", "R3", "A", "planted conflict pair",
             "conflicts_planted", "conflicts_preserved",
             "premature_reconciliations", 12, 0.90,
             "on this one historical case, planted conflicts were preserved rather "
             "than prematurely reconciled",
             "single case, 12 planted pairs, no randomisation"),
    GateSpec("R4-B", "R4", "B", "witness-degradation injection",
             "injections_total", "injections_narrowed", "widening_events", 50, 0.90,
             "in this run, witness degradation was followed by strict narrowing of "
             "the permitted effect set at the frozen share",
             "descriptive share within this run only; no population claim, no "
             "significance, no generalization"),
    GateSpec("R4-C", "R4", "C", "witness-degradation injection",
             "injections_total", "injections_narrowed", "widening_events", 30, 0.90,
             "on these private synthetic targets, witness degradation was followed "
             "by strict narrowing at the frozen share",
             "private synthetic targets only; descriptive; no significance, no "
             "generalization"),
    GateSpec("R5-A", "R5", "A", "recorded descendant",
             "descendants_recorded", "descendants_reached", "silent_overwrites", 20,
             0.95,
             "on this one historical case, corrections reached the recorded "
             "descendant set at the frozen share with no silent overwrite",
             "single case, sealed descendant universe, no randomisation"),
    GateSpec("R5-C", "R5", "C", "recorded descendant of a revised report",
             "descendants_recorded", "descendants_reached", "silent_overwrites", 6,
             0.95,
             "on these private synthetic targets, corrections reached the recorded "
             "descendant set at the frozen share with no silent overwrite",
             "no randomised comparator exists for this component; descriptive only"),
    GateSpec("R6-A", "R6", "A", "deliberately absent provenance item",
             "absent_items", "typed_unknown", "typed_clean", 60, 0.98,
             "on this one historical case, absent provenance was typed UNKNOWN "
             "rather than clean",
             "single case, 60 planted absences, no randomisation"),
    GateSpec("R6-B", "R6", "B", "adjudicated missing witness receipt",
             "receipts_adjudicated", "typed_unknown", "typed_clean", 30, 0.95,
             "in this run, missing witness receipts were typed UNKNOWN at the "
             "frozen share with no receipt typed clean",
             "descriptive share within this run only; no population claim, no "
             "significance, no generalization"),
    GateSpec("R6-C", "R6", "C", "adjudicated missing witness receipt",
             "receipts_adjudicated", "typed_unknown", "typed_clean", 30, 0.95,
             "on these private synthetic targets, missing witness receipts were "
             "typed UNKNOWN at the frozen share with no receipt typed clean",
             "private synthetic targets only; descriptive; no significance, no "
             "generalization"),
)

BY_KEY = {g.key: g for g in REGISTRY}
ROUTES = ("R1", "R2", "R3", "R4", "R5", "R6")
ROUTE_COMPONENTS: dict[str, list[str]] = {}
for _g in REGISTRY:
    ROUTE_COMPONENTS.setdefault(_g.route, []).append(_g.key)

# Family F3a of v0.4 is WITHDRAWN. There is exactly one route family and it is
# gate-only, so no multiplicity procedure applies to route evidence at all.
FAMILY_F3_GATE_ONLY = tuple(g.key for g in REGISTRY)


# ---------------------------------------------------------------- validation
def _int_field(record: Mapping[str, Any], name: str, key: str) -> int:
    if name not in record:
        raise RouteInputError("%s: required raw field %r is missing" % (key, name))
    value = record[name]
    if isinstance(value, bool) or not isinstance(value, Integral):
        raise RouteInputError("%s: raw field %r must be an integer, got %r"
                              % (key, name, type(value).__name__))
    v = int(value)
    if v < 0:
        raise RouteInputError("%s: raw field %r must be non-negative, got %d"
                              % (key, name, v))
    return v


@dataclass(frozen=True)
class GateResult:
    """Result of evaluating ONE component from raw evidence.

    This object is a REPORT, never evidence. `route_claims` never accepts one:
    it recomputes from raw evidence itself, so mutating, replacing or forging a
    GateResult cannot change any route label (carrying finding F-P4-1).
    """
    key: str
    route: str
    phase: str
    cls: str
    denominator: int
    numerator: int
    violations: int
    share: float | None
    min_items: int
    threshold: float
    evaluable: bool
    gate_pass: bool
    hard_gate_violated: bool
    reasons: tuple[str, ...]
    statement: str
    scope_limit: str
    inference: str = ("NONE. Descriptive gate only: no p-value, no null, no "
                      "confidence bound, no significance, no generalization")


def evaluate_gate(key: str, evidence: Mapping[str, Any]) -> GateResult:
    """Evaluate one component from MANDATORY RAW EVIDENCE. Fail-closed.

    The caller supplies raw counts and nothing else. There is no `gate_pass`
    parameter, no `hard_gate_violated` parameter, no `evaluable` parameter and no
    p-value parameter: every conclusion below is computed here from the counts.

    RAISES `RouteInputError` on: an unknown component key; a non-mapping record;
    a missing required field; an unexpected extra field; a non-integer, Boolean
    or negative count; a numerator exceeding its denominator; or a violation
    count exceeding its denominator. Nothing is returned in those cases, so an
    invalid record cannot be laundered into a report.

    FAIL-CLOSED, returning a NOT EVALUABLE result that cannot support anything:
    a denominator of zero, or a denominator below the component's frozen minimum
    evidence count.

    The gate PASSES only if the component is evaluable, the pass share is at or
    above the frozen threshold, and the zero-tolerance violation count, where the
    component has one, is exactly zero.
    """
    if not isinstance(key, str) or key not in BY_KEY:
        raise RouteInputError("unknown component key %r" % (key,))
    spec = BY_KEY[key]
    if not isinstance(evidence, Mapping):
        raise RouteInputError("%s: raw evidence must be a mapping, got %r"
                              % (key, type(evidence).__name__))
    extra = sorted(set(evidence) - set(spec.required_fields))
    if extra:
        raise RouteInputError("%s: unexpected raw field(s) %s; the frozen record is "
                              "exactly %s" % (key, extra, list(spec.required_fields)))

    total = _int_field(evidence, spec.denominator_field, key)
    passed = _int_field(evidence, spec.numerator_field, key)
    violations = (_int_field(evidence, spec.violation_field, key)
                  if spec.violation_field else 0)
    if passed > total:
        raise RouteInputError("%s: %s = %d exceeds %s = %d"
                              % (key, spec.numerator_field, passed,
                                 spec.denominator_field, total))
    if violations > total:
        raise RouteInputError("%s: %s = %d exceeds %s = %d"
                              % (key, spec.violation_field, violations,
                                 spec.denominator_field, total))

    reasons: list[str] = []
    hard = bool(spec.violation_field and violations > 0)
    if hard:
        reasons.append("%d zero-tolerance violation(s) recorded in %s: the route FAILS "
                       "regardless of any share" % (violations, spec.violation_field))

    if total == 0:
        reasons.append("no evidence recorded: NOT EVALUABLE")
        return GateResult(key, spec.route, spec.phase, CLASS, 0, passed, violations,
                          None, spec.min_items, spec.threshold, False, False, hard,
                          tuple(reasons), spec.statement, spec.scope_limit)
    if total < spec.min_items:
        reasons.append("%s = %d is below the frozen minimum evidence count %d: NOT "
                       "EVALUABLE" % (spec.denominator_field, total, spec.min_items))
        return GateResult(key, spec.route, spec.phase, CLASS, total, passed, violations,
                          passed / total, spec.min_items, spec.threshold, False, False,
                          hard, tuple(reasons), spec.statement, spec.scope_limit)

    share = passed / total
    meets = share >= spec.threshold
    reasons.append("descriptive share %d/%d = %.6f against the frozen threshold %.2f: "
                   "%s" % (passed, total, share, spec.threshold,
                           "MET" if meets else "NOT MET"))
    return GateResult(key, spec.route, spec.phase, CLASS, total, passed, violations,
                      share, spec.min_items, spec.threshold, True,
                      bool(meets and not hard), hard, tuple(reasons),
                      spec.statement, spec.scope_limit)


# ---------------------------------------------------------------- route claims
def route_claims(raw_evidence: Mapping[str, Any]) -> dict:
    """Map RAW EVIDENCE to one frozen descriptive label per route. Fail-closed.

    The ONLY admissible input is a mapping from component key to a raw-evidence
    record. `route_claims` calls `evaluate_gate` itself, so no caller-computed
    conclusion of any kind enters the decision. Passing a `GateResult`, any other
    derived object, or a record produced by `dataclasses.replace` is rejected:
    those are not raw-evidence mappings and cannot be mistaken for one. There is
    no token to forge and no trusted constructor to reach.

    Priority per route, in this order:
      1  a component's evidence record is absent          -> OUT OF SCOPE
      2  any component records a zero-tolerance violation -> FAILED
      3  any component is NOT EVALUABLE                   -> NOT EVALUABLE
      4  any component's descriptive threshold is not met  -> NOT SUPPORTED
      5  every component is evaluable and meets its gate   -> SUPPORTED-DESCRIPTIVE

    Clause 5 is CONJUNCTION ONLY across phases: a route with components in more
    than one phase is supported only if EVERY component passes. No p-value
    combination method exists to prohibit, because no p-value exists.

    `SUPPORTED-DESCRIPTIVE` licenses only the component's frozen statement with
    its frozen scope limitation in the same sentence. It is not significance, not
    inferential support, not a population claim, and not evidence of novelty
    beyond the case or run in which it was observed.
    """
    if not isinstance(raw_evidence, Mapping):
        raise RouteInputError("raw_evidence must be a mapping of component key to a "
                              "raw-evidence record")
    unknown = sorted(k for k in raw_evidence if k not in BY_KEY)
    if unknown:
        raise RouteInputError("unknown component key(s) %s" % unknown)
    for key, record in raw_evidence.items():
        if isinstance(record, GateResult) or not isinstance(record, Mapping):
            raise RouteInputError(
                "%s: only raw-evidence mappings are admissible; a derived or "
                "pre-evaluated object was supplied (%s)"
                % (key, type(record).__name__))

    results = {key: evaluate_gate(key, record)
               for key, record in raw_evidence.items()}

    routes: dict[str, dict] = {}
    for route in ROUTES:
        keys = ROUTE_COMPONENTS[route]
        missing = [k for k in keys if k not in results]
        if missing:
            routes[route] = {
                "claim": "OUT OF SCOPE",
                "reason": "raw evidence absent for %s" % ", ".join(missing),
                "components": keys, "ceiling": "SUPPORTED-DESCRIPTIVE"}
            continue
        members = [results[k] for k in keys]
        violated = [m.key for m in members if m.hard_gate_violated]
        not_eval = [m.key for m in members if not m.evaluable]
        failed = [m.key for m in members if m.evaluable and not m.gate_pass]
        if violated:
            claim, reason = "FAILED", ("zero-tolerance violation recorded in %s"
                                       % ", ".join(violated))
        elif not_eval:
            claim, reason = "NOT EVALUABLE", ("evidence below the frozen minimum, or "
                                              "absent, for %s" % ", ".join(not_eval))
        elif failed:
            claim, reason = "NOT SUPPORTED", ("descriptive threshold not met by %s"
                                              % ", ".join(failed))
        else:
            claim, reason = "SUPPORTED-DESCRIPTIVE", (
                "every component of this route is evaluable and meets its frozen "
                "descriptive threshold, by conjunction")
        routes[route] = {
            "claim": claim, "reason": reason, "components": keys,
            "ceiling": "SUPPORTED-DESCRIPTIVE",
            "statements": [m.statement for m in members] if claim
            == "SUPPORTED-DESCRIPTIVE" else [],
            "scope_limits": [m.scope_limit for m in members],
        }
    return {
        "routes": routes,
        "components": {k: {"denominator": r.denominator, "numerator": r.numerator,
                           "violations": r.violations, "share": r.share,
                           "evaluable": r.evaluable, "gate_pass": r.gate_pass,
                           "hard_gate_violated": r.hard_gate_violated,
                           "reasons": list(r.reasons)}
                       for k, r in results.items()},
        "family_f3_gate_only": list(FAMILY_F3_GATE_ONLY),
        "inference": "NONE. No p-value, no null, no confidence bound, no "
                     "false-discovery-rate procedure, and no significance or "
                     "generalizing claim is produced by this contract's route path",
        "withdrawn_in_v0_5": list(WITHDRAWN_LABELS),
    }


def registry_table() -> list[dict]:
    """The frozen evidence contract as plain rows, for the contract and verifier."""
    return [{"component": g.key, "route": g.route, "phase": g.phase, "class": CLASS,
             "unit": g.unit, "required_fields": list(g.required_fields),
             "denominator": g.denominator_field, "numerator": g.numerator_field,
             "zero_tolerance": g.violation_field or "none",
             "min_items": g.min_items, "threshold": g.threshold,
             "statement": g.statement, "scope_limit": g.scope_limit}
            for g in REGISTRY]


if __name__ == "__main__":
    print("SHVVP v0.5 route gates: DESCRIPTIVE ONLY. No inference of any kind.")
    print("Withdrawn in v0.5: %s, family F3a, exact binomial route p-values, "
          "Clopper-Pearson route bounds, Benjamini-Hochberg over route evidence."
          % ", ".join(WITHDRAWN_LABELS))
    for row in registry_table():
        print("  %-5s route %s phase %s  min %3d  threshold %.2f  fields %s"
              % (row["component"], row["route"], row["phase"], row["min_items"],
                 row["threshold"], row["required_fields"]))

---

# Bismillah ir-Rahman ir-Rahim
