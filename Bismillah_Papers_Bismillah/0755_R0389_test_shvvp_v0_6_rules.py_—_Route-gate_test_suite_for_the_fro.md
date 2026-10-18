# Bismillah ir-Rahman ir-Rahim

# R0389 -- test_shvvp_v0_6_rules.py — Route-gate test suite for the frozen SHVVP v0.6 protocol.

**Chronological Index:** 755 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** test_shvvp_v0_6_rules.py  
**Source Format:** py  
**SHA-256:** `71137f09be15901d26ea9749bb9684acb50900b6173f7ed57916d9e479bbaf20`  

---

## R0389 · test_shvvp_v0_6_rules.py — Route-gate test suite for the frozen SHVVP v0.6 protocol.

- section: V. BSSG & SHVVP Protocols
- source_file: test_shvvp_v0_6_rules.py
- source_format: py
- text_sha256: 71137f09be15901d26ea9749bb9684acb50900b6173f7ed57916d9e479bbaf20

"""Route-gate test suite for the frozen SHVVP v0.6 protocol.

Scope. v0.6 changes exactly one executable module relative to v0.5, the route
gate, to close the blocking finding F-P5-1 (caller-selectable evidence universe
and post-result omission). This suite therefore focuses on the route gate: it
carries forward the v0.5 no-inference and raw-evidence-only tests, adapted to the
v0.6 scope-binding record schema, and ADDS named adversarial regression tests that
reproduce each of the three F-P5-1 attacks and assert the corrected outcome. The
decision-rules, power-simulation and verifier suites are unchanged from v0.5 and
are carried in the release packet as lineage.

Run: `python3 test_shvvp_v0_6_rules.py` -> exits non-zero if any check fails.
"""
from __future__ import annotations

import ast
import dataclasses
import os

import shvvp_v0_6_route_gates as G

HERE = os.path.dirname(os.path.abspath(__file__))
FAILURES: list[str] = []
COUNT = 0


def check(name: str, cond: bool, detail: str = "") -> None:
    global COUNT
    COUNT += 1
    if cond:
        print("PASS  %s" % name)
    else:
        print("FAIL  %s%s" % (name, ("  [%s]" % detail) if detail else ""))
        FAILURES.append(name)


# --------------------------------------------------------------- record binding
def bound(key: str, **counts) -> dict:
    """Build a v0.6-valid raw-evidence record: the frozen counts plus the manifest
    and committed-universe binding. For a sealed or realized universe the committed
    cardinality defaults to the submitted denominator (a complete submission);
    tests that probe subsets pass an explicit `sealed_universe_n` / `realized_total`
    or a `reconciliation`."""
    entry = G.MANIFEST_BY_KEY[key]
    spec = G.BY_KEY[key]
    rec = dict(counts)
    rec.setdefault("manifest_sha256", G.MANIFEST_SHA256)
    rec.setdefault("universe_id", entry.universe_id)
    denom = counts.get(spec.denominator_field)
    if entry.kind == G.KIND_SEALED:
        if "sealed_universe_n" not in rec:
            rec["sealed_universe_n"] = denom
        rec.setdefault("sealed_universe_hash", "sealed:%s:committed" % key)
    elif entry.kind == G.KIND_REALIZED:
        if "realized_total" not in rec:
            rec["realized_total"] = denom
        rec.setdefault("run_log_hash", "runlog:%s:committed" % key)
    return rec


# The canonical perfect corpus, every record bound and complete against its
# committed universe. Note R4-C is now the full 216-injection universe (was a
# 40-item subset under v0.5), and every record carries its manifest binding.
GOOD = {
    "R1-A": bound("R1-A", facts_examined=10, facts_incremental=10),
    "R2-A": bound("R2-A", branches_planted=16, branches_typed=14,
                  branches_dropped_silently=0),
    "R2-B": bound("R2-B", denials_total=100, denials_typed=100),
    "R3-A": bound("R3-A", conflicts_planted=12, conflicts_preserved=12,
                  premature_reconciliations=0),
    "R4-B": bound("R4-B", injections_total=60, injections_narrowed=60,
                  widening_events=0),
    "R4-C": bound("R4-C", injections_total=216, injections_narrowed=216,
                  widening_events=0),
    "R5-A": bound("R5-A", descendants_recorded=25, descendants_reached=25,
                  silent_overwrites=0),
    "R5-C": bound("R5-C", descendants_recorded=6, descendants_reached=6,
                  silent_overwrites=0),
    "R6-A": bound("R6-A", absent_items=60, typed_unknown=60, typed_clean=0),
    "R6-B": bound("R6-B", receipts_adjudicated=35, typed_unknown=35, typed_clean=0),
    "R6-C": bound("R6-C", receipts_adjudicated=30, typed_unknown=30, typed_clean=0),
}


# ---------------------------------------------------------------- no inference
def t22_no_inference_anywhere() -> None:
    """T22 the route path contains no inference of any kind (carried, F-P4-2)."""
    check("T22a the closed route label list has exactly six descriptive labels",
          len(G.ROUTE_CLAIM_LABELS) == 6
          and set(G.ROUTE_CLAIM_LABELS) == {"OUT OF SCOPE", "INCOMPLETE", "FAILED",
                                            "NOT EVALUABLE", "NOT SUPPORTED",
                                            "SUPPORTED-DESCRIPTIVE"},
          str(G.ROUTE_CLAIM_LABELS))
    for stray in ("SUPPORTED-INFERENTIAL", "DESCRIPTIVE-ONLY"):
        check("T22b %s is not an attainable label" % stray,
              stray not in G.ROUTE_CLAIM_LABELS and stray in G.WITHDRAWN_LABELS)
    forbidden = ("binom", "clopper", "pearson", "pvalue", "p_value", "bh_",
                 "fdr", "pi0", "significance", "attainab", "confint")
    tree = ast.parse(open(os.path.join(HERE, "shvvp_v0_6_route_gates.py"),
                          encoding="utf-8").read())
    names: set[str] = set()
    for node in ast.walk(tree):
        for attr in ("name", "id", "attr", "arg"):
            v = getattr(node, attr, None)
            if isinstance(v, str):
                names.add(v.lower())
        if isinstance(node, ast.keyword) and node.arg:
            names.add(node.arg.lower())
    hits = sorted({f for f in forbidden for n in names if f in n})
    check("T22c no identifier in the normative module is inferential machinery",
          not hits, str(hits))
    check("T22d every registry component is Class G", G.CLASS == "G"
          and all(hasattr(g, "threshold") and not hasattr(g, "pi0")
                  for g in G.REGISTRY))
    check("T22e there is no Class I and no family F3a",
          not hasattr(G, "F3A_MEMBERS") and not hasattr(G, "F3A")
          and len(G.FAMILY_F3_GATE_ONLY) == 11)
    out = G.route_claims(GOOD)
    check("T22f route output declares that no inference is performed",
          out["inference"].startswith("NONE")
          and all(v["ceiling"] == "SUPPORTED-DESCRIPTIVE"
                  for v in out["routes"].values()))
    check("T22g the strongest attainable label over a perfect corpus is descriptive",
          set(v["claim"] for v in out["routes"].values())
          == {"SUPPORTED-DESCRIPTIVE"},
          str({k: v["claim"] for k, v in out["routes"].items()}))


# ---------------------------------------------------------- raw evidence only
def t23_raw_evidence_only() -> None:
    """T23 adversarial evidence admission, carried from v0.5 (F-P4-1), on the v0.6
    binding schema."""
    # a catastrophic but well-bound record cannot support a route.
    catastrophic = dict(GOOD)
    catastrophic["R2-B"] = bound("R2-B", denials_total=100, denials_typed=0)
    claim = G.route_claims(catastrophic)["routes"]["R2"]["claim"]
    check("T23a 0 of 100 passing raw items cannot support a route",
          claim == "NOT SUPPORTED", claim)

    # an injected decision field is rejected as an unexpected field.
    for flag in ("evaluable", "gate_pass", "p_value", "share", "_token",
                 "hard_gate_violated", "clusters_total"):
        rec = bound("R2-B", denials_total=100, denials_typed=100)
        rec[flag] = True
        try:
            G.evaluate_gate("R2-B", rec)
            check("T23b injected field %r is rejected" % flag, False)
        except G.RouteInputError:
            check("T23b injected field %r is rejected" % flag, True)

    # a fabricated derived object is rejected as evidence.
    fabricated = G.GateResult(
        key="R2-B", route="R2", phase="B", cls="G", denominator=100, numerator=100,
        violations=0, share=1.0, min_items=50, threshold=0.98, evaluable=True,
        gate_pass=True, hard_gate_violated=False, universe_n=100, reasons=("forged",),
        statement="forged", scope_limit="forged")
    try:
        G.route_claims({**GOOD, "R2-B": fabricated})
        check("T23c a fabricated derived object is rejected as evidence", False)
    except G.RouteInputError:
        check("T23c a fabricated derived object is rejected as evidence", True)

    # dataclasses.replace on a genuine below-minimum report is rejected.
    genuine = G.evaluate_gate("R2-B", bound("R2-B", denials_total=3, denials_typed=3))
    check("T23d a genuine below-minimum report is not evaluable",
          genuine.evaluable is False and genuine.gate_pass is False)
    replaced = dataclasses.replace(genuine, evaluable=True, gate_pass=True,
                                   denominator=100, numerator=100, share=1.0)
    try:
        G.route_claims({**GOOD, "R2-B": replaced})
        check("T23e a dataclasses.replace forgery is rejected as evidence", False)
    except G.RouteInputError:
        check("T23e a dataclasses.replace forgery is rejected as evidence", True)
    check("T23f no token mechanism exists to forge",
          not any(hasattr(G, n) for n in ("_TOKEN", "TOKEN")))

    # minimum evidence counts enforced at n-1, n, n+1 (realized components, where a
    # subset below the committed universe is not itself the point).
    ok, detail = True, []
    for key in ("R2-B", "R4-B", "R6-B", "R6-C"):
        g = G.BY_KEY[key]
        for delta in (-1, 0, 1):
            n = g.min_items + delta
            rec = bound(key, **{g.denominator_field: n, g.numerator_field: n,
                                **({g.violation_field: 0} if g.violation_field
                                   else {})})
            r = G.evaluate_gate(key, rec)
            want = delta >= 0
            if r.evaluable is not want or r.gate_pass is not want:
                ok = False
                detail.append("%s n=%d" % (key, n))
    check("T23g realized minimum evidence counts enforced at n-1, n and n+1", ok,
          ",".join(detail))

    # malformed or inconsistent records are rejected.
    bad = [
        ("R2-B", bound("R2-B", denials_total=10, denials_typed=11)),
        ("R6-B", bound("R6-B", receipts_adjudicated=5, typed_unknown=5,
                       typed_clean=9)),
        ("R2-B", bound("R2-B", denials_total=100, denials_typed=100.0)),
        ("R2-B", {**bound("R2-B", denials_total=100, denials_typed=100),
                  "denials_total": True}),
        ("R2-B", {k: v for k, v in bound("R2-B", denials_total=100,
                                         denials_typed=100).items()
                  if k != "denials_typed"}),
        ("NOPE", {"denials_total": 100, "denials_typed": 100}),
    ]
    raised = sum(1 for key, rec in bad
                 if _raises(lambda: G.evaluate_gate(key, rec)))
    check("T23h all %d malformed or inconsistent records are rejected" % len(bad),
          raised == len(bad), "%d of %d" % (raised, len(bad)))

    # route_claims level rejections.
    for mutate, name in (
            (lambda d: {**d, "R9-Z": {"a": 1}}, "an unknown component key"),
            (lambda d: {**d, "R2-B": "SUPPORTED"}, "a string in place of evidence"),
            (lambda d: {**d, "R2-B": [100, 100]}, "a list in place of evidence"),
            (lambda d: "everything passed", "a non-mapping input")):
        check("T23i route_claims rejects %s" % name,
              _raises(lambda: G.route_claims(mutate(dict(GOOD)))))

    # zero-tolerance violations dominate a passing share.
    for key, field in (("R6-B", "typed_clean"), ("R4-B", "widening_events"),
                       ("R5-A", "silent_overwrites"),
                       ("R2-A", "branches_dropped_silently")):
        g = G.BY_KEY[key]
        n = g.min_items + 10 if G.MANIFEST_BY_KEY[key].kind != G.KIND_FIXED \
            else G.MANIFEST_BY_KEY[key].universe_n
        rec = bound(key, **{g.denominator_field: n, g.numerator_field: n, field: 1})
        r = G.evaluate_gate(key, rec)
        claim = G.route_claims({**GOOD, key: rec})["routes"][g.route]["claim"]
        check("T23j a violation in %s.%s FAILS the route despite a perfect share"
              % (key, field), r.hard_gate_violated and claim == "FAILED",
              "%s / %s" % (r.hard_gate_violated, claim))

    # conjunction only: one failing component blocks its whole route.
    part = dict(GOOD)
    part["R6-C"] = bound("R6-C", receipts_adjudicated=30, typed_unknown=28,
                         typed_clean=0)
    claims = G.route_claims(part)["routes"]
    check("T23k conjunction: one component below threshold blocks the route",
          claims["R6"]["claim"] == "NOT SUPPORTED", claims["R6"]["claim"])
    check("T23l other routes are unaffected by that failure",
          claims["R2"]["claim"] == "SUPPORTED-DESCRIPTIVE")

    # exact threshold boundary behaviour (realized component, denominator == 100).
    boundary = dict(GOOD)
    boundary["R2-B"] = bound("R2-B", denials_total=100, denials_typed=98)
    check("T23m a share exactly at the frozen threshold is supported",
          G.route_claims(boundary)["routes"]["R2"]["claim"]
          == "SUPPORTED-DESCRIPTIVE")
    boundary["R2-B"] = bound("R2-B", denials_total=100, denials_typed=97)
    check("T23n a share one item below the frozen threshold is not supported",
          G.route_claims(boundary)["routes"]["R2"]["claim"] == "NOT SUPPORTED")
    zero = dict(GOOD)
    zero["R2-B"] = bound("R2-B", denials_total=0, denials_typed=0)
    check("T23o zero evidence is NOT EVALUABLE, never a pass",
          G.route_claims(zero)["routes"]["R2"]["claim"] == "NOT EVALUABLE")


# ---------------------------------------------- F-P5-1 adversarial regressions
def tp51a_fixed_denominator_subset() -> None:
    """F-P5-1 attack (a): a favorable subset satisfies a fixed-denominator route.
    Section 7.2 fixes Phase C at 216 injections; v0.5 accepted R4-C 30/30. v0.6
    requires equality or an explicit, fail-closed reconciliation."""
    # the exact v0.5-accepted submission is now rejected outright.
    subset = bound("R4-C", injections_total=30, injections_narrowed=30,
                   widening_events=0)
    check("TP51a-1 R4-C 30/30 subset of the 216 universe is rejected at the gate",
          _raises(lambda: G.evaluate_gate("R4-C", subset)))
    check("TP51a-2 the same subset is rejected inside route_claims",
          _raises(lambda: G.route_claims({**GOOD, "R4-C": subset})))
    # a reconciliation cannot inflate: the 186 shortfall is scored as non-passing.
    recon = {"universe_n": 216,
             "excluded": [{"count": 186, "reason": "not run in this pass"}]}
    r = G.evaluate_gate("R4-C", bound("R4-C", injections_total=30,
                                      injections_narrowed=30, widening_events=0,
                                      reconciliation=recon))
    check("TP51a-3 a reconciled 30/30 is scored over the full 216 and does not pass",
          r.denominator == 216 and r.numerator == 30 and abs(r.share - 30 / 216)
          < 1e-9 and r.gate_pass is False, "%d/%d share=%.4f pass=%s"
          % (r.numerator, r.denominator, r.share, r.gate_pass))
    # a reconciliation whose arithmetic does not close is rejected.
    bad_recon = {"universe_n": 216,
                 "excluded": [{"count": 10, "reason": "short"}]}
    check("TP51a-4 a reconciliation that does not account for the full shortfall is "
          "rejected",
          _raises(lambda: G.evaluate_gate("R4-C", bound(
              "R4-C", injections_total=30, injections_narrowed=30,
              widening_events=0, reconciliation=bad_recon))))
    # the full committed universe passes.
    full = bound("R4-C", injections_total=216, injections_narrowed=216,
                 widening_events=0)
    check("TP51a-5 the full 216-injection universe is admissible and supports R4-C",
          G.route_claims({**GOOD, "R4-C": full})["routes"]["R4"]["claim"]
          == "SUPPORTED-DESCRIPTIVE")
    # a denominator ABOVE the committed universe is rejected (no enlargement).
    check("TP51a-6 a denominator above the committed 216 universe is rejected",
          _raises(lambda: G.evaluate_gate("R4-C", bound(
              "R4-C", injections_total=217, injections_narrowed=217,
              widening_events=0))))


def tp51b_sealed_universe_subset() -> None:
    """F-P5-1 attack (b): a sealed descendant universe is reduced to a favorable
    sample. v0.5 accepted R5-A 20/20 and R5-C 6/6 with no cardinality binding."""
    # a submission of 20 against a sealed universe of 25, without reconciliation.
    subset = bound("R5-A", descendants_recorded=20, descendants_reached=20,
                   silent_overwrites=0, sealed_universe_n=25,
                   sealed_universe_hash="seal-25")
    check("TP51b-1 an R5-A 20-of-25 sealed subset is rejected without reconciliation",
          _raises(lambda: G.evaluate_gate("R5-A", subset)))
    # a sealed record with no sealed cardinality/hash binding is rejected.
    unbound_seal = {k: v for k, v in bound(
        "R5-A", descendants_recorded=20, descendants_reached=20,
        silent_overwrites=0).items() if k != "sealed_universe_hash"}
    check("TP51b-2 a sealed record missing its sealed_universe_hash is rejected",
          _raises(lambda: G.evaluate_gate("R5-A", unbound_seal)))
    # the full sealed universe is admissible and supports the route.
    check("TP51b-3 the full sealed descendant universe supports R5",
          G.route_claims(GOOD)["routes"]["R5"]["claim"]
          == "SUPPORTED-DESCRIPTIVE")
    # a reconciled sealed shortfall is scored over the sealed cardinality.
    recon = {"universe_n": 25,
             "excluded": [{"count": 5, "reason": "descendant not yet corrected"}]}
    r = G.evaluate_gate("R5-A", bound(
        "R5-A", descendants_recorded=20, descendants_reached=20, silent_overwrites=0,
        sealed_universe_n=25, sealed_universe_hash="seal-25", reconciliation=recon))
    check("TP51b-4 a reconciled sealed shortfall is scored over the sealed universe",
          r.denominator == 25 and abs(r.share - 20 / 25) < 1e-9
          and r.gate_pass is False, "%d/%d pass=%s"
          % (r.numerator, r.denominator, r.gate_pass))


def tp51c_omission_is_not_out_of_scope() -> None:
    """F-P5-1 attack (c): an unfavorable committed component is deleted to convert
    NOT SUPPORTED into OUT OF SCOPE. v0.5 shipped test T23k blessing this."""
    # present unfavorable -> NOT SUPPORTED.
    present_bad = dict(GOOD)
    present_bad["R2-B"] = bound("R2-B", denials_total=100, denials_typed=0)
    check("TP51c-1 R2 with R2-B 0/100 present is NOT SUPPORTED",
          G.route_claims(present_bad)["routes"]["R2"]["claim"] == "NOT SUPPORTED")
    # delete the unfavorable committed component -> INCOMPLETE, never OUT OF SCOPE.
    deleted = {k: v for k, v in GOOD.items() if k != "R2-B"}
    r2 = G.route_claims(deleted)["routes"]["R2"]
    check("TP51c-2 deleting the committed R2-B yields INCOMPLETE, not OUT OF SCOPE",
          r2["claim"] == "INCOMPLETE" and "R2-B" in r2["missing_committed"],
          r2["claim"])
    check("TP51c-3 the v0.5 omission escape (absence -> OUT OF SCOPE) is closed",
          G.route_claims(deleted)["routes"]["R2"]["claim"] != "OUT OF SCOPE")
    # a present OBSERVED failure is reported as such even if another committed
    # component is also missing: an observed failure is not masked as INCOMPLETE.
    both = {k: v for k, v in GOOD.items() if k != "R2-B"}
    both["R2-A"] = bound("R2-A", branches_planted=16, branches_typed=16,
                         branches_dropped_silently=3)
    check("TP51c-4 an observed FAILED dominates a co-occurring missing component",
          G.route_claims(both)["routes"]["R2"]["claim"] == "FAILED")
    # the ONE legitimate predeclared exclusion (R3, no instrumentation) is distinct.
    no_r3 = {k: v for k, v in GOOD.items() if k != "R3-A"}
    check("TP51c-5 R3 with no instrumentation record is validly OUT OF SCOPE",
          G.route_claims(no_r3)["routes"]["R3"]["claim"] == "OUT OF SCOPE")
    check("TP51c-6 R3 with an instrumentation record is evaluated, not excused",
          G.route_claims(GOOD)["routes"]["R3"]["claim"] == "SUPPORTED-DESCRIPTIVE")
    # deleting a committed component from a MULTI-phase route is INCOMPLETE too.
    del_r4c = {k: v for k, v in GOOD.items() if k != "R4-C"}
    check("TP51c-7 deleting committed R4-C yields INCOMPLETE for R4, not OUT OF SCOPE",
          G.route_claims(del_r4c)["routes"]["R4"]["claim"] == "INCOMPLETE")


def tp51d_manifest_binding() -> None:
    """F-P5-1 disposition items 1-2: every record is bound to the frozen pre-results
    scope manifest and to its committed universe identifier."""
    check("TP51d-1 the scope manifest digest is stable and reproducible",
          isinstance(G.MANIFEST_SHA256, str) and len(G.MANIFEST_SHA256) == 64
          and G.MANIFEST_SHA256
          == __import__("hashlib").sha256(
              G._manifest_canonical().encode("utf-8")).hexdigest())
    check("TP51d-2 the manifest and registry cover the same eleven components",
          set(G.MANIFEST_BY_KEY) == set(G.BY_KEY) and len(G.MANIFEST_BY_KEY) == 11)
    check("TP51d-3 exactly one component is predeclared conditionally out of scope",
          [e.key for e in G.SCOPE_MANIFEST
           if e.status == G.STATUS_PREDECLARED_CONDITIONAL_OOS] == ["R3-A"])
    # a wrong manifest hash is rejected.
    wrong_m = bound("R2-B", denials_total=100, denials_typed=100)
    wrong_m["manifest_sha256"] = "0" * 64
    check("TP51d-4 a record bound to the wrong manifest digest is rejected",
          _raises(lambda: G.evaluate_gate("R2-B", wrong_m)))
    # a missing manifest hash is rejected.
    no_m = {k: v for k, v in bound("R2-B", denials_total=100,
                                   denials_typed=100).items()
            if k != "manifest_sha256"}
    check("TP51d-5 a record with no manifest binding is rejected",
          _raises(lambda: G.evaluate_gate("R2-B", no_m)))
    # a wrong universe identifier is rejected.
    wrong_u = bound("R2-B", denials_total=100, denials_typed=100)
    wrong_u["universe_id"] = "u.someone-elses-universe"
    check("TP51d-6 a record bound to the wrong universe identifier is rejected",
          _raises(lambda: G.evaluate_gate("R2-B", wrong_u)))
    # the R4-C committed cardinality is 216 in both the manifest and the registry.
    check("TP51d-7 R4-C committed universe is 216 (was a 30-item floor in v0.5)",
          G.MANIFEST_BY_KEY["R4-C"].universe_n == 216
          and G.BY_KEY["R4-C"].min_items == 216)


def tp51e_realized_run_log_binding() -> None:
    """F-P5-1 disposition item 2 for realized universes: a count not knowable before
    the run (Section 0.1 A-3.7) is bound to a pre-committed run log and its realized
    total, and the denominator must equal that total."""
    # a realized record with no run-log binding is rejected.
    no_runlog = {k: v for k, v in bound("R2-B", denials_total=100,
                                        denials_typed=100).items()
                 if k != "run_log_hash"}
    check("TP51e-1 a realized record missing its run_log_hash is rejected",
          _raises(lambda: G.evaluate_gate("R2-B", no_runlog)))
    # a realized_total that disagrees with the denominator is rejected.
    mismatch = bound("R2-B", denials_total=100, denials_typed=100)
    mismatch["realized_total"] = 120
    check("TP51e-2 a realized_total above the denominator (undeclared shortfall) is "
          "rejected", _raises(lambda: G.evaluate_gate("R2-B", mismatch)))
    # a matched realized submission is admissible.
    r = G.evaluate_gate("R2-B", bound("R2-B", denials_total=100, denials_typed=100))
    check("TP51e-3 a run-log-bound realized submission is admissible",
          r.evaluable and r.gate_pass and r.universe_n == 100)


def _raises(fn) -> bool:
    try:
        fn()
        return False
    except G.RouteInputError:
        return True


def main() -> None:
    t22_no_inference_anywhere()
    t23_raw_evidence_only()
    tp51a_fixed_denominator_subset()
    tp51b_sealed_universe_subset()
    tp51c_omission_is_not_out_of_scope()
    tp51d_manifest_binding()
    tp51e_realized_run_log_binding()
    print("\n%d checks, %d failures" % (COUNT, len(FAILURES)))
    if FAILURES:
        for name in FAILURES:
            print("  FAILED: %s" % name)
    raise SystemExit(1 if FAILURES else 0)


if __name__ == "__main__":
    main()

---

# Bismillah ir-Rahman ir-Rahim
