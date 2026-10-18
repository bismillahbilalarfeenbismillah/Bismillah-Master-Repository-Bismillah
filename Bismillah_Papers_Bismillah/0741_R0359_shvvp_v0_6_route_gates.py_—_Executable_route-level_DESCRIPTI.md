# Bismillah ir-Rahman ir-Rahim

# R0359 -- shvvp_v0_6_route_gates.py — Executable route-level DESCRIPTIVE GATES for the frozen SHVVP v0.6 protocol.

**Chronological Index:** 741 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** shvvp_v0_6_route_gates.py  
**Source Format:** py  
**SHA-256:** `60cbb22e49f8fc2d011c4c024b615039337e6411dfe2568dd8ed086b18e5cbea`  

---

## R0359 · shvvp_v0_6_route_gates.py — Executable route-level DESCRIPTIVE GATES for the frozen SHVVP v0.6 protocol.

- section: V. BSSG & SHVVP Protocols
- source_file: shvvp_v0_6_route_gates.py
- source_format: py
- text_sha256: 60cbb22e49f8fc2d011c4c024b615039337e6411dfe2568dd8ed086b18e5cbea

"""Executable route-level DESCRIPTIVE GATES for the frozen SHVVP v0.6 protocol.

WHAT THIS MODULE IS, AND WHAT IT IS NOT
---------------------------------------
It evaluates the six novelty routes as **descriptive, context-scoped gates** over
raw evidence counts, bound to a **frozen pre-results scope manifest** and to the
committed evidence universe of each component. It performs **no** statistical
inference of any kind. There is no p-value, no null hypothesis, no confidence
bound, no false-discovery-rate procedure, no significance, and no population-level
or generalizing claim anywhere in this module or in the contract sections it
implements. The strongest label it can return is `SUPPORTED-DESCRIPTIVE`.

WHY v0.6 EXISTS, AND WHAT WAS CLOSED
-----------------------------------
The v0.5 carrying round was DIVERGENT: the GPT-class Seat A returned HALT with one
blocking finding, independently corroborated against source and code. Both the
finding and its prescribed disposition are accepted in full.

* **F-P5-1 (HIGH, BLOCKING). Caller-selectable evidence universe and post-result
  omission.** v0.5's route gate validated the syntax and local adequacy of the
  records it received but never established that those records EXHAUST the evidence
  universe the protocol freezes, and it had no pre-results map of which components
  are in scope. Three attacks succeeded against the v0.5 gate:

    (a) A favorable subset satisfied a fixed-denominator route. Section 7.2 fixes
        Phase C witness degradation at **216 sessions** (source line "that is 216
        sessions"), yet the v0.5 gate accepted an R4-C record of `30/30` because it
        checked `total < spec.min_items`, a MINIMUM, not equality to or
        reconciliation with the committed 216-injection universe. 186 committed
        sessions, and any failures among them, could be silently absent.
    (b) A sealed descendant universe was reduced to a favorable sample. Sections
        5.1/M9 and 7.4/C6 define denominators over SEALED descendant universes; the
        v0.5 gate accepted R5-A `20/20` and R5-C `6/6` without requiring the counts
        to match a frozen sealed cardinality, manifest, or digest.
    (c) An observed failure was weakened by omitting its component. A complete R2
        submission with R2-B `0/100` correctly returned NOT SUPPORTED; deleting the
        R2-B record flipped the same route to OUT OF SCOPE. The v0.5 gate could not
        distinguish a component PREDECLARED out of scope from an unfavorable
        component DELETED after observation, and shipped test T23k treated the
        omission as expected, making it a contract-level gap rather than a slip.

  **The disposition, implemented here in full:**

    1. A **pre-results scope manifest** (`SCOPE_MANIFEST`) fixes, before any data,
       every committed route component, its status, and any permitted predeclared
       exclusion. Its canonical digest is `MANIFEST_SHA256`.
    2. Every evidence record is **bound** to that manifest (`manifest_sha256`) and
       to a **sealed evidence-universe identifier** (`universe_id`), plus a
       cardinality or reproducible commitment appropriate to its denominator kind.
    3. Where the protocol FIXES a denominator, the gate requires **exact equality
       or explicit reconciliation** -- including the 216 Phase C injections.
    4. **Complete accounting** is required for sealed descendant universes: the
       denominator must equal the sealed cardinality (or reconcile the difference),
       never a favorable minimum sample.
    5. Three states are DISTINGUISHED, not collapsed:
         - a validly predeclared exclusion               -> `OUT OF SCOPE`
         - a committed component whose record is absent   -> `INCOMPLETE`
         - an observed threshold failure                  -> `NOT SUPPORTED`
    6. An unfavorable committed component can no longer be converted to
       `OUT OF SCOPE` by omission: its absence is `INCOMPLETE`.
    7. Adversarial regression tests reproduce all three attacks and assert the
       corrected outcomes (`test_shvvp_v0_6_rules.py`).

WHAT v0.5 ALREADY CLOSED, CARRIED FORWARD UNCHANGED
---------------------------------------------------
All route-level inference remains WITHDRAWN (v0.4 finding F-P4-2): no binomial
test, no Clopper-Pearson bound, no re-anchored null, no family F3a, no
Benjamini-Hochberg over route evidence; every component is Class G, descriptive
gate only. Derived outcomes remain inadmissible (v0.4 finding F-P4-1): the only
input is raw counts plus scope-binding fields, and the only authority over what
the counts mean is this module. v0.6 adds universe binding to that fail-closed
core; it removes none of it.

THE FROZEN EVIDENCE CONTRACT
---------------------------
Each component fixes, before data: its manifest status; its committed-universe
kind (FIXED cardinality, SEALED cardinality, or REALIZED-and-run-log-committed);
the required raw fields; the denominator; the minimum evidence count; the exact
descriptive threshold on the pass share; and whether it carries a zero-tolerance
violation counter. Every mandatory field must be present and bound. Missing
fields, extra fields, non-integer or negative counts, a numerator above its
denominator, a violation count above its denominator, a wrong or missing manifest
binding, a wrong or missing universe identifier, or a denominator that neither
equals its committed universe nor carries a valid reconciliation, are all
REJECTED. Counts below the frozen minimum are NOT EVALUABLE and can support
nothing.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from numbers import Integral
from typing import Any, Mapping

# ---------------------------------------------------------------- vocabulary
# Closed. Six labels. `INCOMPLETE` is new in v0.6 and is the state of a route with
# a COMMITTED component whose raw-evidence record is absent: it is non-supporting
# and is NOT `OUT OF SCOPE`. The strings "SUPPORTED-INFERENTIAL" and
# "DESCRIPTIVE-ONLY" of v0.4 remain WITHDRAWN and appear nowhere as attainable
# outcomes.
ROUTE_CLAIM_LABELS = (
    "OUT OF SCOPE",           # ONLY via a validly predeclared exclusion (manifest)
    "INCOMPLETE",             # NEW in v0.6: a COMMITTED component's record is absent
    "FAILED",                 # a zero-tolerance violation was recorded
    "NOT EVALUABLE",          # present but below the frozen minimum, or zero
    "NOT SUPPORTED",          # evaluable, observed pass share below the threshold
    "SUPPORTED-DESCRIPTIVE",  # every committed component present, evaluable, passing
)

WITHDRAWN_LABELS = ("SUPPORTED-INFERENTIAL", "DESCRIPTIVE-ONLY")

# Committed-universe kinds. Fixes, before data, how the denominator is committed.
KIND_FIXED = "FIXED"        # cardinality fixed numerically in the contract
KIND_SEALED = "SEALED"      # cardinality fixed by an external seal (not in the doc)
KIND_REALIZED = "REALIZED"  # count not knowable before the run; run-log committed

# Manifest statuses.
STATUS_COMMITTED = "COMMITTED"
STATUS_PREDECLARED_CONDITIONAL_OOS = "PREDECLARED_CONDITIONAL_OOS"


class RouteInputError(ValueError):
    """Raised when raw evidence is structurally invalid or unbound. Nothing is
    returned, so an invalid or unbound record cannot be laundered into support."""


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
    def count_fields(self) -> tuple[str, ...]:
        f = [self.denominator_field, self.numerator_field]
        if self.violation_field:
            f.append(self.violation_field)
        return tuple(f)


@dataclass(frozen=True)
class ScopeEntry:
    """Frozen, pre-results scope commitment for one component. Fixed before any
    outcome is inspected; its digest is committed as `MANIFEST_SHA256`."""
    key: str
    status: str                  # STATUS_COMMITTED | STATUS_PREDECLARED_CONDITIONAL_OOS
    kind: str                    # KIND_FIXED | KIND_SEALED | KIND_REALIZED
    universe_id: str             # stable identifier for this sealed evidence universe
    universe_n: int | None       # committed cardinality for KIND_FIXED; else None
    authority: str               # the contract locus that authorizes this status/kind


CLASS = "G"   # every component. There is no Class I in v0.5 or v0.6.

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
             "injections_total", "injections_narrowed", "widening_events", 216, 0.90,
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

# --------------------------------------------------------- frozen scope manifest
# Pre-results scope commitment (F-P5-1 disposition item 1). Fixed BEFORE any
# outcome is inspected. Every committed component MUST be present in a submission
# or the route is INCOMPLETE (disposition items 5, 6). The single legitimate
# predeclared exclusion is R3: its ConflictLedger instrumentation is UNKNOWN in the
# frozen document (Section 0.1 item 2), so R3 is OUT OF SCOPE for v0.6 unless an
# R3-A record is supplied, per Section 8 ("A route without committed instrumentation
# is declared OUT OF SCOPE"). No other component may reach OUT OF SCOPE.
#
# Committed-universe kinds:
#   FIXED    -- cardinality is fixed numerically in the contract; the denominator
#               must equal universe_n or carry an explicit reconciliation.
#   SEALED   -- cardinality is fixed by an external seal recorded before results
#               (Section 5.1); the document does not contain the number, so the
#               record carries the sealed cardinality and its hash, and the
#               denominator must equal that sealed cardinality or reconcile it.
#   REALIZED -- the count is not knowable before the run (Section 0.1 amendment
#               A-3.7); the record carries the pre-committed run-log hash and its
#               realized total, and the denominator must equal that realized total.
SCOPE_MANIFEST: tuple[ScopeEntry, ...] = (
    ScopeEntry("R1-A", STATUS_COMMITTED, KIND_SEALED, "u.r1a.sealed-ledger", None,
               "Section 5.1 sealed ground-truth ledger; cardinality N_D fixed by "
               "the custodian seal before the Phase-A run"),
    ScopeEntry("R2-A", STATUS_COMMITTED, KIND_FIXED, "u.r2a.planted-branches", 16,
               "Section 8.2 R2-A: 16 planted caller-context branches"),
    ScopeEntry("R2-B", STATUS_COMMITTED, KIND_REALIZED, "u.r2b.denials-run", None,
               "Section 0.1 A-3.7: realized denied-effect-request count, run-log "
               "committed"),
    ScopeEntry("R3-A", STATUS_PREDECLARED_CONDITIONAL_OOS, KIND_FIXED,
               "u.r3a.planted-conflicts", 12,
               "Section 0.1 item 2 and Section 8: R3 ConflictLedger instrumentation "
               "is UNKNOWN; OUT OF SCOPE unless an R3-A record is supplied"),
    ScopeEntry("R4-B", STATUS_COMMITTED, KIND_REALIZED, "u.r4b.phaseb-injections",
               None,
               "Section 0.1 A-3.7: realized Phase-B witness-degradation injection "
               "count, run-log committed"),
    ScopeEntry("R4-C", STATUS_COMMITTED, KIND_FIXED, "u.r4c.phasec-injections", 216,
               "Section 7.2: witness-degradation injection in a randomly selected "
               "half of C-BSSG sessions, that is 216 sessions"),
    ScopeEntry("R5-A", STATUS_COMMITTED, KIND_SEALED, "u.r5a.descendant-universe",
               None,
               "Sections 5.1/M9: correction reach over the sealed descendant "
               "universe; cardinality sealed before results"),
    ScopeEntry("R5-C", STATUS_COMMITTED, KIND_SEALED, "u.r5c.revised-descendants",
               None,
               "Sections 7.4/C6: sealed descendant universe for the 6 revised "
               "seeded reports; cardinality sealed before results"),
    ScopeEntry("R6-A", STATUS_COMMITTED, KIND_FIXED, "u.r6a.planted-absences", 60,
               "Section 8.2 R6-A: 60 deliberately absent provenance items"),
    ScopeEntry("R6-B", STATUS_COMMITTED, KIND_REALIZED, "u.r6b.receipts-run", None,
               "Section 0.1 A-3.7: realized adjudicated-missing-receipt count, "
               "run-log committed"),
    ScopeEntry("R6-C", STATUS_COMMITTED, KIND_REALIZED, "u.r6c.receipts-synth", None,
               "Section 0.1 A-3.7: realized adjudicated-missing-receipt count on "
               "private synthetic targets, run-log committed"),
)

MANIFEST_BY_KEY = {e.key: e for e in SCOPE_MANIFEST}
assert set(MANIFEST_BY_KEY) == set(BY_KEY), "manifest and registry must cover the "\
    "same components"


def _manifest_canonical() -> str:
    """Canonical, order-stable serialization of the frozen scope manifest. The
    digest of this string is the pre-results commitment every record binds to."""
    rows = [
        {"key": e.key, "status": e.status, "kind": e.kind,
         "universe_id": e.universe_id, "universe_n": e.universe_n}
        for e in SCOPE_MANIFEST
    ]
    return json.dumps(rows, sort_keys=True, separators=(",", ":"))


MANIFEST_SHA256 = hashlib.sha256(_manifest_canonical().encode("utf-8")).hexdigest()

# Binding fields required on every raw-evidence record, and the kind-specific
# fields required by each committed-universe kind. `reconciliation` is permitted on
# any record and mandatory only when the denominator differs from the committed
# universe cardinality.
_BIND_COMMON = ("manifest_sha256", "universe_id")
_BIND_BY_KIND = {
    KIND_FIXED: (),
    KIND_SEALED: ("sealed_universe_n", "sealed_universe_hash"),
    KIND_REALIZED: ("run_log_hash", "realized_total"),
}
_OPTIONAL_FIELDS = ("reconciliation",)


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


def _str_field(record: Mapping[str, Any], name: str, key: str) -> str:
    if name not in record:
        raise RouteInputError("%s: required binding field %r is missing" % (key, name))
    value = record[name]
    if not isinstance(value, str) or not value.strip():
        raise RouteInputError("%s: binding field %r must be a non-empty string"
                              % (key, name))
    return value


def _required_fields(entry: ScopeEntry, spec: GateSpec) -> tuple[str, ...]:
    return spec.count_fields + _BIND_COMMON + _BIND_BY_KIND[entry.kind]


def _check_binding(key: str, entry: ScopeEntry, record: Mapping[str, Any],
                   total: int) -> tuple[int, int, list[str]]:
    """Verify the manifest and universe binding, and enforce equality or explicit
    reconciliation against the committed universe cardinality. Returns the committed
    universe cardinality, the EFFECTIVE denominator to score over, and binding
    notes, or raises. For a reconciled shortfall the effective denominator is the
    full committed universe, so a favorable subset can never inflate the share."""
    notes: list[str] = []

    manifest_hash = _str_field(record, "manifest_sha256", key)
    if manifest_hash != MANIFEST_SHA256:
        raise RouteInputError(
            "%s: manifest_sha256 %r does not match the frozen scope manifest %r"
            % (key, manifest_hash, MANIFEST_SHA256))
    universe_id = _str_field(record, "universe_id", key)
    if universe_id != entry.universe_id:
        raise RouteInputError(
            "%s: universe_id %r does not match the committed universe %r"
            % (key, universe_id, entry.universe_id))

    if entry.kind == KIND_FIXED:
        universe_n = int(entry.universe_n)  # type: ignore[arg-type]
        notes.append("committed universe: FIXED cardinality %d (%s)"
                     % (universe_n, entry.authority))
    elif entry.kind == KIND_SEALED:
        universe_n = _int_field(record, "sealed_universe_n", key)
        _str_field(record, "sealed_universe_hash", key)
        notes.append("committed universe: SEALED cardinality %d, hash bound (%s)"
                     % (universe_n, entry.authority))
    else:  # KIND_REALIZED
        universe_n = _int_field(record, "realized_total", key)
        _str_field(record, "run_log_hash", key)
        notes.append("committed universe: REALIZED total %d, run-log bound (%s)"
                     % (universe_n, entry.authority))

    effective_total = _enforce_completeness(key, entry, record, total, universe_n,
                                             notes)
    return universe_n, effective_total, notes


def _enforce_completeness(key: str, entry: ScopeEntry, record: Mapping[str, Any],
                          total: int, universe_n: int, notes: list[str]) -> int:
    """The denominator must equal the committed universe cardinality, or a valid
    reconciliation must account for the difference (F-P5-1 disposition items 3, 4).
    A favorable subset with no reconciliation is REJECTED. When a shortfall is
    reconciled, the EFFECTIVE denominator is the full committed universe and the
    shortfall is scored as non-passing (fail-closed, Section 7.4: an absent or
    unverifiable item is counted against the architecture, never as clean), so a
    reconciliation can only lower a share, never inflate one."""
    if total == universe_n:
        notes.append("denominator %d equals the committed universe %d: complete"
                     % (total, universe_n))
        return total
    if total > universe_n:
        raise RouteInputError(
            "%s: denominator %d exceeds the committed universe %d; the evidence "
            "universe cannot be enlarged after commitment"
            % (key, total, universe_n))
    # total < universe_n : a shortfall must be reconciled explicitly.
    recon = record.get("reconciliation")
    if recon is None:
        raise RouteInputError(
            "%s: denominator %d is below the committed universe %d and no "
            "reconciliation was supplied; a favorable subset is not admissible "
            "evidence for a fixed universe" % (key, total, universe_n))
    if not isinstance(recon, Mapping):
        raise RouteInputError("%s: reconciliation must be a mapping" % key)
    stated_n = recon.get("universe_n")
    if not isinstance(stated_n, Integral) or isinstance(stated_n, bool) \
            or int(stated_n) != universe_n:
        raise RouteInputError(
            "%s: reconciliation universe_n must equal the committed universe %d"
            % (key, universe_n))
    excluded = recon.get("excluded")
    if not isinstance(excluded, (list, tuple)) or not excluded:
        raise RouteInputError(
            "%s: reconciliation must list the excluded items with reasons" % key)
    accounted = 0
    for i, item in enumerate(excluded):
        if not isinstance(item, Mapping):
            raise RouteInputError("%s: reconciliation item %d must be a mapping"
                                  % (key, i))
        cnt = item.get("count")
        reason = item.get("reason")
        if not isinstance(cnt, Integral) or isinstance(cnt, bool) or int(cnt) <= 0:
            raise RouteInputError(
                "%s: reconciliation item %d needs a positive integer count"
                % (key, i))
        if not isinstance(reason, str) or not reason.strip():
            raise RouteInputError(
                "%s: reconciliation item %d needs a non-empty reason" % (key, i))
        accounted += int(cnt)
    if accounted != universe_n - total:
        raise RouteInputError(
            "%s: reconciliation accounts for %d excluded items but the committed "
            "universe %d exceeds the denominator %d by %d"
            % (key, accounted, universe_n, total, universe_n - total))
    notes.append("denominator %d reconciled against committed universe %d: %d "
                 "excluded items accounted with reasons and scored as non-passing "
                 "over the full universe" % (total, universe_n, accounted))
    return universe_n


@dataclass(frozen=True)
class GateResult:
    """Result of evaluating ONE component from raw evidence.

    This object is a REPORT, never evidence. `route_claims` never accepts one:
    it recomputes from raw evidence itself, so mutating, replacing or forging a
    GateResult cannot change any route label (carrying finding F-P4-1)."""
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
    universe_n: int
    reasons: tuple[str, ...]
    statement: str
    scope_limit: str
    inference: str = ("NONE. Descriptive gate only: no p-value, no null, no "
                      "confidence bound, no significance, no generalization")


def evaluate_gate(key: str, evidence: Mapping[str, Any]) -> GateResult:
    """Evaluate one component from MANDATORY RAW EVIDENCE bound to the frozen scope
    manifest. Fail-closed.

    The caller supplies raw counts plus the scope-binding fields, and nothing else.
    There is no `gate_pass`, `hard_gate_violated`, `evaluable` or p-value parameter:
    every conclusion below is computed here from the counts. Beyond the v0.5 checks,
    v0.6 REJECTS: a wrong or missing `manifest_sha256`; a wrong or missing
    `universe_id`; a denominator that neither equals its committed universe nor
    carries a valid reconciliation; and, for a sealed or realized universe, a
    missing sealed cardinality/hash or run-log commitment. Nothing is returned in
    those cases, so an unbound or subset record cannot be laundered into a report.

    FAIL-CLOSED, returning a NOT EVALUABLE result that cannot support anything:
    a denominator of zero, or a denominator below the component's frozen minimum.

    The gate PASSES only if the component is evaluable, the pass share is at or
    above the frozen threshold, and the zero-tolerance violation count, where the
    component has one, is exactly zero."""
    if not isinstance(key, str) or key not in BY_KEY:
        raise RouteInputError("unknown component key %r" % (key,))
    spec = BY_KEY[key]
    entry = MANIFEST_BY_KEY[key]
    if not isinstance(evidence, Mapping):
        raise RouteInputError("%s: raw evidence must be a mapping, got %r"
                              % (key, type(evidence).__name__))

    required = _required_fields(entry, spec)
    allowed = set(required) | set(_OPTIONAL_FIELDS)
    extra = sorted(set(evidence) - allowed)
    if extra:
        raise RouteInputError("%s: unexpected raw field(s) %s; the frozen record is "
                              "exactly %s plus the optional %s"
                              % (key, extra, list(required), list(_OPTIONAL_FIELDS)))

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

    # Manifest and universe binding, and completeness against the committed
    # universe. This raises before any share is computed if the record is unbound
    # or represents a favorable subset without reconciliation. `total_eff` is the
    # denominator scored: the submitted total under exact equality, or the full
    # committed universe under a reconciled shortfall.
    universe_n, total_eff, bind_notes = _check_binding(key, entry, evidence, total)

    reasons: list[str] = list(bind_notes)
    hard = bool(spec.violation_field and violations > 0)
    if hard:
        reasons.append("%d zero-tolerance violation(s) recorded in %s: the route "
                       "FAILS regardless of any share"
                       % (violations, spec.violation_field))

    if total_eff == 0:
        reasons.append("no evidence recorded: NOT EVALUABLE")
        return GateResult(key, spec.route, spec.phase, CLASS, 0, passed, violations,
                          None, spec.min_items, spec.threshold, False, False, hard,
                          universe_n, tuple(reasons), spec.statement, spec.scope_limit)
    if total_eff < spec.min_items:
        reasons.append("%s = %d is below the frozen minimum evidence count %d: NOT "
                       "EVALUABLE" % (spec.denominator_field, total_eff,
                                      spec.min_items))
        return GateResult(key, spec.route, spec.phase, CLASS, total_eff, passed,
                          violations, passed / total_eff, spec.min_items,
                          spec.threshold, False, False, hard, universe_n,
                          tuple(reasons), spec.statement, spec.scope_limit)

    share = passed / total_eff
    meets = share >= spec.threshold
    reasons.append("descriptive share %d/%d = %.6f against the frozen threshold "
                   "%.2f: %s" % (passed, total_eff, share, spec.threshold,
                                 "MET" if meets else "NOT MET"))
    return GateResult(key, spec.route, spec.phase, CLASS, total_eff, passed,
                      violations, share, spec.min_items, spec.threshold, True,
                      bool(meets and not hard), hard, universe_n, tuple(reasons),
                      spec.statement, spec.scope_limit)


# ---------------------------------------------------------------- route claims
def route_claims(raw_evidence: Mapping[str, Any]) -> dict:
    """Map RAW EVIDENCE to one frozen descriptive label per route, driven by the
    frozen scope manifest. Fail-closed.

    The ONLY admissible input is a mapping from component key to a raw-evidence
    record. `route_claims` calls `evaluate_gate` itself, so no caller-computed
    conclusion enters the decision, and it iterates the MANIFEST rather than the
    submission, so a committed component cannot be silenced by omission.

    Per route, over its manifest components:
      - A `PREDECLARED_CONDITIONAL_OOS` component (R3-A) whose record is absent is a
        validly predeclared exclusion; if every component of a route is excluded
        this way, the route is OUT OF SCOPE. This is the ONLY path to OUT OF SCOPE.
      - A `COMMITTED` component whose record is absent makes the route INCOMPLETE.
        It is NEVER OUT OF SCOPE (F-P5-1 items 5, 6): an unfavorable component
        cannot be converted to OUT OF SCOPE by deleting it.

    Priority over the route's in-scope committed components, in this order:
      1  any records a zero-tolerance violation            -> FAILED
      2  any is present but below its frozen minimum        -> NOT EVALUABLE
      3  any is evaluable but below its threshold           -> NOT SUPPORTED
      4  any committed component's record is absent          -> INCOMPLETE
      5  every committed component is present and passes     -> SUPPORTED-DESCRIPTIVE

    Observed failures (1-3) dominate INCOMPLETE (4) so that a failure actually seen
    is reported as a failure, not masked as missing evidence. Clause 5 is
    CONJUNCTION ONLY across phases: a route with components in more than one phase
    is supported only if EVERY committed component passes. No p-value combination
    method exists to prohibit, because no p-value exists.

    `SUPPORTED-DESCRIPTIVE` licenses only each component's frozen statement with its
    frozen scope limitation in the same sentence. It is not significance, not
    inferential support, not a population claim, and not evidence of novelty beyond
    the case or run in which it was observed."""
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
        # Partition the route's manifest components. A committed component is in
        # scope whether or not its record was supplied; a predeclared-conditional
        # component (R3-A) is in scope only when its record IS supplied.
        committed_keys = [k for k in keys
                          if MANIFEST_BY_KEY[k].status == STATUS_COMMITTED]
        conditional_keys = [k for k in keys
                            if MANIFEST_BY_KEY[k].status
                            == STATUS_PREDECLARED_CONDITIONAL_OOS]

        present = [k for k in keys if k in results]
        in_scope = committed_keys + [k for k in conditional_keys if k in results]
        missing_committed = [k for k in committed_keys if k not in results]
        excluded_predeclared = [k for k in conditional_keys if k not in results]

        if not in_scope:
            routes[route] = {
                "claim": "OUT OF SCOPE",
                "reason": "every component of this route is a validly predeclared "
                          "exclusion and no evidence was supplied: %s"
                          % ", ".join("%s (%s)" % (k, MANIFEST_BY_KEY[k].authority)
                                      for k in excluded_predeclared),
                "components": keys, "ceiling": "SUPPORTED-DESCRIPTIVE",
                "predeclared_out_of_scope": excluded_predeclared,
            }
            continue

        members = [results[k] for k in present]
        violated = [m.key for m in members if m.hard_gate_violated]
        not_eval = [m.key for m in members if not m.evaluable]
        failed = [m.key for m in members if m.evaluable and not m.gate_pass]

        if violated:
            claim = "FAILED"
            reason = "zero-tolerance violation recorded in %s" % ", ".join(violated)
        elif not_eval:
            claim = "NOT EVALUABLE"
            reason = ("evidence below the frozen minimum, or zero, for %s"
                      % ", ".join(not_eval))
        elif failed:
            claim = "NOT SUPPORTED"
            reason = "descriptive threshold not met by %s" % ", ".join(failed)
        elif missing_committed:
            claim = "INCOMPLETE"
            reason = ("committed evidence is absent for %s; a committed component "
                      "cannot be treated as out of scope by omission"
                      % ", ".join(missing_committed))
        else:
            claim = "SUPPORTED-DESCRIPTIVE"
            reason = ("every committed component of this route is present, "
                      "evaluable and meets its frozen descriptive threshold, by "
                      "conjunction")

        routes[route] = {
            "claim": claim, "reason": reason, "components": keys,
            "ceiling": "SUPPORTED-DESCRIPTIVE",
            "predeclared_out_of_scope": excluded_predeclared,
            "missing_committed": missing_committed,
            "statements": [m.statement for m in members] if claim
            == "SUPPORTED-DESCRIPTIVE" else [],
            "scope_limits": [m.scope_limit for m in members],
        }
    return {
        "manifest_sha256": MANIFEST_SHA256,
        "routes": routes,
        "components": {k: {"denominator": r.denominator, "numerator": r.numerator,
                           "violations": r.violations, "share": r.share,
                           "universe_n": r.universe_n, "evaluable": r.evaluable,
                           "gate_pass": r.gate_pass,
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
             "unit": g.unit, "required_fields": list(_required_fields(
                 MANIFEST_BY_KEY[g.key], g)),
             "denominator": g.denominator_field, "numerator": g.numerator_field,
             "zero_tolerance": g.violation_field or "none",
             "min_items": g.min_items, "threshold": g.threshold,
             "statement": g.statement, "scope_limit": g.scope_limit}
            for g in REGISTRY]


def scope_manifest_table() -> list[dict]:
    """The frozen scope manifest as plain rows, for the contract and verifier."""
    return [{"component": e.key, "status": e.status, "kind": e.kind,
             "universe_id": e.universe_id, "universe_n": e.universe_n,
             "authority": e.authority} for e in SCOPE_MANIFEST]


if __name__ == "__main__":
    print("SHVVP v0.6 route gates: DESCRIPTIVE ONLY. No inference of any kind.")
    print("Frozen scope manifest sha256: %s" % MANIFEST_SHA256)
    print("Withdrawn since v0.5: %s, family F3a, exact binomial route p-values, "
          "Clopper-Pearson route bounds, Benjamini-Hochberg over route evidence."
          % ", ".join(WITHDRAWN_LABELS))
    for row in scope_manifest_table():
        print("  %-5s %-26s %-8s universe_n=%s"
              % (row["component"], row["status"], row["kind"],
                 row["universe_n"]))

---

# Bismillah ir-Rahman ir-Rahim
