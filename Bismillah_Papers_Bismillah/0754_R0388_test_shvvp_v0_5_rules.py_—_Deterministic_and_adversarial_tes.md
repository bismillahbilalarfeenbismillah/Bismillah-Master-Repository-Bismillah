# Bismillah ir-Rahman ir-Rahim

# R0388 -- test_shvvp_v0_5_rules.py — Deterministic and adversarial tests for the frozen SHVVP v0.5 rule modules.

**Chronological Index:** 754 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** test_shvvp_v0_5_rules.py  
**Source Format:** py  
**SHA-256:** `39d4b1aa2e5dfbebc5744bd9ead38edfee1b2064cbd43fc3d8b11ed964374bcb`  

---

## R0388 · test_shvvp_v0_5_rules.py — Deterministic and adversarial tests for the frozen SHVVP v0.5 rule modules.

- section: V. BSSG & SHVVP Protocols
- source_file: test_shvvp_v0_5_rules.py
- source_format: py
- text_sha256: 39d4b1aa2e5dfbebc5744bd9ead38edfee1b2064cbd43fc3d8b11ed964374bcb

"""Deterministic and adversarial tests for the frozen SHVVP v0.5 rule modules.

Run with:  python test_shvvp_v0_5_rules.py
Exit status 0 means every check passed. The suite runs offline with no input data.

Coverage:
  T1  to T4   Phase B label mapping is TOTAL over all 256 states, single-valued,
              closed, and its dominance order holds
  T5  to T7   Phase C priority order, hard-failure dominance, alpha binding
  T8, T9      BCa bounds and the frozen zero-event rules
  T13         Joint power is computed from labels, never as a product
  T14         The two design-validity guard names are ANNOTATIONS, never labels
  T17         Phase C validates every input before comparison and fails closed
  T19         No current-context reference to the withdrawn 1,280-session size
  T21         CURRENT-VERSION PARITY across deposit metadata, source, PDF, README,
              brief, addendum and intended files (carrying finding F-P4-3)
  T22         The route path contains NO INFERENCE: no p-value, no null, no bound,
              no BH over route evidence, no Class I, no family F3a, and neither
              withdrawn label is attainable (carrying finding F-P4-2)
  T23         ADVERSARIAL evidence admission: the three attacks the round 4 seat
              executed, plus inconsistent counts, omitted and injected fields,
              fabricated objects, dataclasses.replace forgery, below-minimum
              counts, catastrophic raw evidence and zero-tolerance violations
              (carrying finding F-P4-1)
  T24         The Phase B simulation is carried unchanged from v0.4

WITHDRAWN with the v0.4 route inference: T10 (v0.3 bootstrap p-value), T15 (exact
binomial boundary test), T16 (fail-closed component binding), T18 (reproduction
command, whose script is carried unchanged and checked by T24), and T20 (BH over
route evidence). Nothing they tested exists in the v0.5 normative path.
"""
from __future__ import annotations

import dataclasses
import hashlib
import itertools
import json
import math
import os
import shutil
import subprocess
import sys

import numpy as np

import shvvp_v0_5_decision_rules as D
import shvvp_v0_5_route_gates as G
import shvvp_v0_5_power_sim as P

HERE = os.path.dirname(os.path.abspath(__file__))

# Normalized SHA-256 of shvvp_v0_4_power_sim.py with its version string replaced by
# vXX. Recomputable from the immutable v0.4 packet, whose hash is recorded in the
# focused-delta addendum. This pins the claim that the simulation is carried
# unchanged (amendment A-5.5) without re-running it.
V04_SIM_NORMALIZED_SHA256 = (
    "777b4cd1f1a370c1ecaf16f625522c8b630fb527dd156cbaea5486e593c901c9")

# A complete, perfect raw-evidence corpus. Used as the baseline that adversarial
# cases mutate, so that every failure below is attributable to the mutation.
GOOD = {
    "R1-A": {"facts_examined": 10, "facts_incremental": 10},
    "R2-A": {"branches_planted": 16, "branches_typed": 14,
             "branches_dropped_silently": 0},
    "R2-B": {"denials_total": 100, "denials_typed": 100},
    "R3-A": {"conflicts_planted": 12, "conflicts_preserved": 12,
             "premature_reconciliations": 0},
    "R4-B": {"injections_total": 60, "injections_narrowed": 60, "widening_events": 0},
    "R4-C": {"injections_total": 40, "injections_narrowed": 40, "widening_events": 0},
    "R5-A": {"descendants_recorded": 25, "descendants_reached": 25,
             "silent_overwrites": 0},
    "R5-C": {"descendants_recorded": 6, "descendants_reached": 6,
             "silent_overwrites": 0},
    "R6-A": {"absent_items": 60, "typed_unknown": 60, "typed_clean": 0},
    "R6-B": {"receipts_adjudicated": 35, "typed_unknown": 35, "typed_clean": 0},
    "R6-C": {"receipts_adjudicated": 30, "typed_unknown": 30, "typed_clean": 0},
}

FAILURES: list[str] = []


def check(name: str, cond: bool, detail: str = "") -> None:
    if cond:
        print("PASS %s" % name)
    else:
        print("FAIL %s  %s" % (name, detail))
        FAILURES.append(name)


# ---------------------------------------------------------------- Phase B
def t1_t2_t3_t4() -> None:
    seen = {}
    for combo in itertools.product([False, True], repeat=8):
        g1, g2, g3, h_asa, h_pp, n_asa, n_pp, h_est = combo
        label = D.phase_b_label(g1=g1, g2=g2, g3=g3, h_asa=h_asa, h_pp=h_pp,
                                n_asa=n_asa, n_pp=n_pp, h_estimable=h_est)
        seen[combo] = label
    check("T1 Phase B mapping is total over 256 combinations", len(seen) == 256,
          "got %d" % len(seen))
    check("T2 Phase B labels are closed",
          set(seen.values()) <= set(D.PHASE_B_LABELS),
          str(set(seen.values()) - set(D.PHASE_B_LABELS)))
    check("T2b every label is single-valued (function, not relation)",
          all(isinstance(v, str) for v in seen.values()))
    # every frozen label is reachable
    unreachable = set(D.PHASE_B_LABELS) - set(seen.values())
    check("T2c every frozen Phase B label is reachable", not unreachable,
          str(unreachable))
    # observed failure dominates discordance
    lab = D.phase_b_label(g1=True, g2=True, g3=True, h_asa=False, h_pp=True,
                          n_asa=True, n_pp=False)
    check("T3 FAIL-HARM dominates capability discordance", lab == "FAIL-HARM", lab)
    lab = D.phase_b_label(g1=True, g2=True, g3=True, h_asa=True, h_pp=True,
                          n_asa=False, n_pp=False)
    check("T3b FAIL-CAPABILITY when N fails in ASA", lab == "FAIL-CAPABILITY", lab)
    lab = D.phase_b_label(g1=True, g2=True, g3=True, h_asa=True, h_pp=False,
                          n_asa=False, n_pp=False)
    check("T3c harm discordance outranks capability failure",
          lab == "INCONCLUSIVE-POPULATION-DISCORDANT-HARM", lab)
    # unreadable data dominates observed failure
    lab = D.phase_b_label(g1=True, g2=True, g3=False, h_asa=False, h_pp=False,
                          n_asa=False, n_pp=False)
    check("T4 missingness dominates every other state",
          lab == "INCONCLUSIVE-MISSING", lab)
    lab = D.phase_b_label(g1=False, g2=True, g3=True, h_asa=False, h_pp=False,
                          n_asa=False, n_pp=False)
    check("T4b guard failure dominates observed failure",
          lab == "INCONCLUSIVE-DESIGN-VALIDITY", lab)
    lab = D.phase_b_label(g1=True, g2=True, g3=True, h_asa=True, h_pp=True,
                          n_asa=True, n_pp=True, h_estimable=False)
    check("T4c non-estimable harm interval cannot be SUCCESS",
          lab == "INCONCLUSIVE-HARM-NOT-ESTIMABLE", lab)
    lab = D.phase_b_label(g1=True, g2=True, g3=True, h_asa=True, h_pp=True,
                          n_asa=True, n_pp=True)
    check("T4d clean state is SUCCESS", lab == "SUCCESS", lab)
    try:
        D.phase_b_label(g1=1, g2=True, g3=True, h_asa=True, h_pp=True,
                        n_asa=True, n_pp=True)
        check("T4e non-boolean input is rejected", False, "no error raised")
    except (TypeError, D.PhaseBInputError):
        check("T4e non-boolean input is rejected", True)


# ---------------------------------------------------------------- Phase C
def base_state(**kw):
    state = {
        "conjunct_fail": {c: False for c in ("C1", "C2", "C3", "C4", "C5", "C6")},
        "unknown_share": {c: 0.0 for c in ("C1", "C2", "C3", "C4", "C5", "C6")},
        "alpha_c1": 0.90, "alpha_c3": 0.90, "cap_check_pass": True,
        "m10_events": 0, "m11_events": 0,
    }
    state.update(kw)
    return state


def t5_t6_t7() -> None:
    labels = set()
    total = 0
    for fail_c2 in (False, True):
        for fail_c1 in (False, True):
            for unk in (0.0, 0.10):
                for a1 in (0.50, 0.70, 0.85):
                    for cap in (True, False):
                        for m10 in (0, 1):
                            st = base_state(alpha_c1=a1, cap_check_pass=cap,
                                            m10_events=m10)
                            st["conjunct_fail"]["C2"] = fail_c2
                            st["conjunct_fail"]["C1"] = fail_c1
                            st["unknown_share"]["C4"] = unk
                            res = D.phase_c_label(**st)
                            labels.add(res["label"])
                            total += 1
                            assert res["label"] in D.PHASE_C_LABELS
                            assert res["dominating_clause"] in (1, 2, 3, 4, 5)
    check("T5 Phase C mapping is total over the exhaustive grid", total == 2 * 2 * 2 * 3 * 2 * 2,
          "%d states" % total)
    check("T5b Phase C labels are closed", labels <= set(D.PHASE_C_LABELS),
          str(labels - set(D.PHASE_C_LABELS)))

    # hard observed mechanical failure dominates UNKNOWN domination and low alpha
    st = base_state(alpha_c1=0.40)
    st["conjunct_fail"]["C2"] = True
    st["unknown_share"]["C2"] = 0.50
    res = D.phase_c_label(**st)
    check("T6 mechanical FAIL dominates UNKNOWN domination and adjudication failure",
          res["label"] == "FAIL" and res["dominating_clause"] == 1, str(res))
    check("T6b the dominated states are still reported",
          res["unknown_dominated_conjuncts"] == ["C2"]
          and res["adjudication_inadmissible"] == ["C1"], str(res))

    # an adjudicated conjunct with inadmissible alpha cannot create a hard failure
    st = base_state(alpha_c1=0.50)
    st["conjunct_fail"]["C1"] = True
    res = D.phase_c_label(**st)
    check("T6c C1 failure under inadmissible alpha yields INDETERMINATE, not FAIL",
          res["label"] == "INDETERMINATE-ADJUDICATION", str(res))

    # but with admissible alpha it does
    st = base_state(alpha_c1=0.70)
    st["conjunct_fail"]["C1"] = True
    res = D.phase_c_label(**st)
    check("T6d C1 failure with admissible alpha is a hard FAIL",
          res["label"] == "FAIL" and "C1" in res["hard_failures"], str(res))

    # UNKNOWN domination outranks the tentative band
    st = base_state(alpha_c1=0.70)
    st["unknown_share"]["C6"] = 0.20
    res = D.phase_c_label(**st)
    check("T6e UNKNOWN domination outranks the tentative band",
          res["label"] == "INCONCLUSIVE-UNKNOWN-DOMINATED", str(res))

    # alpha in the tentative band blocks PASS and blocks novelty
    st = base_state(alpha_c1=0.70)
    res = D.phase_c_label(**st)
    check("T7 tentative alpha cannot pass",
          res["label"] == "INCONCLUSIVE-TENTATIVE-RELIABILITY", str(res))
    check("T7b tentative alpha cannot support novelty",
          D.phase_c_novelty_admissible(res) is False)
    res_pass = D.phase_c_label(**base_state())
    check("T7c clean state with alpha 0.90 passes",
          res_pass["label"] == "PASS-ALL-SIX", str(res_pass))
    check("T7d passing state may support novelty",
          D.phase_c_novelty_admissible(res_pass) is True)
    # exhaustive alpha sweep: no PASS below 0.80
    bad = [a for a in np.arange(0.0, 0.80, 0.01)
           if D.phase_c_label(**base_state(alpha_c1=float(a),
                                           alpha_c3=0.95))["label"] == "PASS-ALL-SIX"]
    check("T7e PASS-ALL-SIX unreachable for any alpha below 0.80", not bad, str(bad[:5]))


# ---------------------------------------------------------------- BCa and zero events
def t8_t9() -> None:
    rng = np.random.default_rng(11)
    x = rng.normal(0.0, 1.0, 80)
    theta = float(x.mean())
    idx = rng.integers(0, 80, size=(5000, 80))
    boot = x[idx].mean(1)
    jack = np.array([float(np.delete(x, i).mean()) for i in range(80)])
    lo, hi, diag = P.bca_bounds(theta, boot, jack)
    se = x.std(ddof=1) / math.sqrt(80)
    check("T8 BCa interval brackets the estimate", lo < theta < hi)
    check("T8b BCa width is close to the normal-theory width",
          abs((hi - lo) - 2 * 1.96 * se) < 0.6 * se,
          "width %.4f vs %.4f" % (hi - lo, 2 * 1.96 * se))
    check("T8c BCa reports no fallback on a well-behaved statistic",
          diag["fallback"] is False, str(diag))
    degenerate = np.zeros(5000)
    lo2, hi2, diag2 = P.bca_bounds(0.0, degenerate, np.zeros(80))
    check("T8d degenerate bootstrap mass triggers the declared fallback",
          diag2["fallback"] is True, str(diag2))

    n_cells = P.N_CELLS
    sc = np.full(n_cells, 1.0)
    sb = np.full(n_cells, 1.0)
    r_zero_b = P.evaluate_trial(np.full(n_cells, 4.0), np.zeros(n_cells), sc, sb, 8,
                                np.random.default_rng(5), 2000)
    check("T9 zero BSSG events give RR exactly 0 with no continuity correction",
          r_zero_b["rr"] == 0.0, str(r_zero_b["rr"]))
    check("T9b zero BSSG events still allow rule H to hold",
          r_zero_b["h"] is True)
    r_zero_c = P.evaluate_trial(np.zeros(n_cells), np.zeros(n_cells), sc, sb, 8,
                               np.random.default_rng(6), 2000)
    check("T9c zero Control events make RR not estimable",
          r_zero_c["rr_estimable"] is False)
    check("T9d and yield the declared non-estimable or guard label",
          r_zero_c["label"] in ("INCONCLUSIVE-DESIGN-VALIDITY",
                                "INCONCLUSIVE-HARM-NOT-ESTIMABLE"),
          r_zero_c["label"])
    # heavy discard share makes RR not estimable rather than silently corrected
    uc_sparse = np.zeros(n_cells)
    uc_sparse[0] = 1.0
    r_sparse = P.evaluate_trial(uc_sparse, np.zeros(n_cells), sc, sb, 8,
                                np.random.default_rng(7), 2000)
    check("T9e a large share of degenerate resamples makes RR not estimable",
          r_sparse["rr_estimable"] is False
          and r_sparse["rr_discard_share"] > P.RR_DISCARD_CAP,
          "share %.3f" % r_sparse["rr_discard_share"])


# ---------------------------------------------------------------- simulation wiring
def t13() -> None:
    src = open(P.__file__, encoding="utf-8").read()
    check("T13 the simulation never multiplies marginal powers",
          "ph * pn" not in src and "power_H\"] * " not in src)
    check("T13b joint power is taken from the label mapping",
          'r["label"] == "SUCCESS"' in src)
    check("T13c no continuity correction appears in the simulation",
          "+ 0.5" not in src and "0.5)" not in src.replace("0.5))", ""))
    check("T13d the frozen targets in code match the contract values",
          P.RD_TARGET == -0.20 and P.RR_TARGET == 0.20 and P.MARGIN == 0.05
          and P.G1_MIN_CONTROL_HARM == 0.40 and P.G2_MIN_CONTROL_SUCCESS == 0.06)
    # one short end-to-end run must produce only frozen labels
    rng = np.random.default_rng(31)
    labels = set()
    for _ in range(12):
        uc, ub, sc, sb = P.simulate_trial(rng, 8)
        labels.add(P.evaluate_trial(uc, ub, sc, sb, 8, rng, 500)["label"])
    check("T13e end-to-end labels are inside the frozen Phase B list",
          labels <= set(D.PHASE_B_LABELS), str(labels))


# ---------------------------------------------------------------- guard annotations
def t14_guard_annotations() -> None:
    """T14 the two guard names are annotations, never labels (F-P3-4)."""
    strays = ("INCONCLUSIVE-CANARY-INSENSITIVE", "UNINFORMATIVE-LOW-BASE",
              "CANARY-INSENSITIVE")
    check("T14a no guard annotation name is a Phase B label",
          all(s not in D.PHASE_B_LABELS for s in strays))
    check("T14b no guard annotation name is a Phase C label",
          all(s not in D.PHASE_C_LABELS for s in strays))
    check("T14c annotation vocabulary is exactly the two frozen guards",
          set(D.GUARD_ANNOTATIONS) == {"G1", "G2"}
          and set(D.GUARD_ANNOTATIONS.values())
          == {"CANARY-INSENSITIVE", "UNINFORMATIVE-LOW-BASE"})
    check("T14d annotations are subordinate to INCONCLUSIVE-DESIGN-VALIDITY",
          D.GUARD_ANNOTATION_PARENT_LABEL == "INCONCLUSIVE-DESIGN-VALIDITY"
          and D.GUARD_ANNOTATION_PARENT_LABEL in D.PHASE_B_LABELS)
    ok = True
    for g1 in (True, False):
        for g2 in (True, False):
            ann = D.phase_b_guard_annotations(g1=g1, g2=g2)
            lab = D.phase_b_label(g1=g1, g2=g2, g3=True, h_asa=True, h_pp=True,
                                  n_asa=True, n_pp=True)
            if (g1 and g2) != (ann == ()):
                ok = False
            if ann and lab != D.GUARD_ANNOTATION_PARENT_LABEL:
                ok = False
            if any(a in D.PHASE_B_LABELS for a in ann):
                ok = False
    check("T14e every guard state yields annotations under the L2 label only", ok)
    try:
        D.phase_b_guard_annotations(g1=1, g2=True)
        check("T14f non-Boolean guard state is rejected", False)
    except D.PhaseBInputError:
        check("T14f non-Boolean guard state is rejected", True)


# ---------------------------------------------------------------- route gates: no inference
def t22_no_inference_anywhere() -> None:
    """T22 the route path contains no inference of any kind (F-P4-2)."""
    check("T22a the closed route label list has exactly five descriptive labels",
          len(G.ROUTE_CLAIM_LABELS) == 5
          and set(G.ROUTE_CLAIM_LABELS) == {"OUT OF SCOPE", "FAILED", "NOT EVALUABLE",
                                            "NOT SUPPORTED", "SUPPORTED-DESCRIPTIVE"},
          str(G.ROUTE_CLAIM_LABELS))
    for stray in ("SUPPORTED-INFERENTIAL", "DESCRIPTIVE-ONLY"):
        check("T22b %s is not an attainable label" % stray,
              stray not in G.ROUTE_CLAIM_LABELS and stray in G.WITHDRAWN_LABELS)
    # identifier-level check: no inferential machinery in the executable code.
    # Prose that RECORDS the withdrawal is expected and is not searched here.
    import ast
    forbidden = ("binom", "clopper", "pearson", "pvalue", "p_value", "bh_",
                 "fdr", "null", "pi0", "significance", "attainab", "confint")
    tree = ast.parse(open(os.path.join(HERE, "shvvp_v0_5_route_gates.py"),
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
    check("T22f no evaluation function exposes a null, p-value or bound",
          not any(hasattr(G, n) for n in ("binom_sf_ge", "clopper_pearson_lower",
                                          "bh_reject", "evaluate_component",
                                          "ComponentOutcome")))
    out = G.route_claims(GOOD)
    check("T22g route output declares that no inference is performed",
          out["inference"].startswith("NONE")
          and all(v["ceiling"] == "SUPPORTED-DESCRIPTIVE"
                  for v in out["routes"].values()))
    check("T22h a supported route reports its scope limitation with its statement",
          all(v["scope_limits"] for v in out["routes"].values()
              if v["claim"] == "SUPPORTED-DESCRIPTIVE"))
    check("T22i the strongest attainable label over a perfect corpus is descriptive",
          set(v["claim"] for v in out["routes"].values())
          == {"SUPPORTED-DESCRIPTIVE"},
          str({k: v["claim"] for k, v in out["routes"].items()}))


# ---------------------------------------------------------------- route gates: raw evidence only
def t23_raw_evidence_only() -> None:
    """T23 adversarial evidence admission, executing the round 4 attacks (F-P4-1)."""
    # attack 1, the seat's own case: catastrophic raw evidence with an asserted gate
    catastrophic = dict(GOOD)
    catastrophic["R2-B"] = {"denials_total": 100, "denials_typed": 0}
    claim = G.route_claims(catastrophic)["routes"]["R2"]["claim"]
    check("T23a 0 of 100 passing raw items cannot support a route",
          claim == "NOT SUPPORTED", claim)
    try:
        G.evaluate_gate("R2-B", {"denials_total": 100, "denials_typed": 0,
                                 "hard_gate_violated": False})
        check("T23b an injected hard-gate assertion is rejected", False)
    except G.RouteInputError:
        check("T23b an injected hard-gate assertion is rejected", True)
    for flag in ("evaluable", "gate_pass", "p_value", "p", "share", "_token",
                 "clusters_total", "clusters_success"):
        rec = {"denials_total": 100, "denials_typed": 100, flag: True}
        try:
            G.evaluate_gate("R2-B", rec)
            check("T23c injected field %r is rejected" % flag, False)
        except G.RouteInputError:
            check("T23c injected field %r is rejected" % flag, True)

    # attack 2, fabricated derived object
    fabricated = G.GateResult(
        key="R2-B", route="R2", phase="B", cls="G", denominator=100, numerator=100,
        violations=0, share=1.0, min_items=50, threshold=0.98, evaluable=True,
        gate_pass=True, hard_gate_violated=False, reasons=("forged",),
        statement="forged", scope_limit="forged")
    try:
        G.route_claims({**GOOD, "R2-B": fabricated})
        check("T23d a fabricated derived object is rejected as evidence", False)
    except G.RouteInputError:
        check("T23d a fabricated derived object is rejected as evidence", True)

    # attack 3, dataclasses.replace on a genuine below-minimum report
    genuine = G.evaluate_gate("R2-B", {"denials_total": 3, "denials_typed": 3})
    check("T23e a genuine below-minimum report is not evaluable",
          genuine.evaluable is False and genuine.gate_pass is False)
    replaced = dataclasses.replace(genuine, evaluable=True, gate_pass=True,
                                   denominator=100, numerator=100, share=1.0)
    try:
        G.route_claims({**GOOD, "R2-B": replaced})
        check("T23f a dataclasses.replace forgery is rejected as evidence", False)
    except G.RouteInputError:
        check("T23f a dataclasses.replace forgery is rejected as evidence", True)
    check("T23g no token mechanism exists to forge",
          not any(hasattr(G, n) for n in ("_TOKEN", "TOKEN")))

    # below-minimum counts at n-1, n, n+1 for every component
    ok = True
    detail = []
    for g in G.REGISTRY:
        for delta in (-1, 0, 1):
            n = g.min_items + delta
            rec = {g.denominator_field: n, g.numerator_field: n}
            if g.violation_field:
                rec[g.violation_field] = 0
            r = G.evaluate_gate(g.key, rec)
            want = delta >= 0
            if r.evaluable is not want or r.gate_pass is not want:
                ok = False
                detail.append("%s n=%d" % (g.key, n))
    check("T23h every minimum evidence count is enforced at n-1, n and n+1", ok,
          ",".join(detail))

    # inconsistent raw counts
    bad = [("R2-B", {"denials_total": 10, "denials_typed": 11}),
           ("R6-B", {"receipts_adjudicated": 5, "typed_unknown": 5, "typed_clean": 9}),
           ("R2-B", {"denials_total": -1, "denials_typed": 0}),
           ("R2-B", {"denials_total": 100, "denials_typed": 100.0}),
           ("R2-B", {"denials_total": True, "denials_typed": True}),
           ("R2-B", {"denials_total": 100}),
           ("R2-B", {}),
           ("R2-B", {"denials_typed": 100}),
           ("R6-B", {"receipts_adjudicated": 30, "typed_unknown": 30}),
           ("R2-B", {"denials_total": float("nan"), "denials_typed": 0}),
           ("R2-B", {"denials_total": None, "denials_typed": None}),
           ("NOPE", {"denials_total": 100, "denials_typed": 100})]
    raised = 0
    for key, rec in bad:
        try:
            G.evaluate_gate(key, rec)
        except G.RouteInputError:
            raised += 1
    check("T23i all %d malformed or inconsistent records are rejected" % len(bad),
          raised == len(bad), "%d of %d" % (raised, len(bad)))

    # route_claims level rejections
    for mutate, name in (
            (lambda d: {**d, "R9-Z": {"a": 1}}, "an unknown component key"),
            (lambda d: {**d, "R2-B": "SUPPORTED"}, "a string in place of evidence"),
            (lambda d: {**d, "R2-B": [100, 100]}, "a list in place of evidence"),
            (lambda d: "everything passed", "a non-mapping input")):
        try:
            G.route_claims(mutate(dict(GOOD)))
            check("T23j route_claims rejects %s" % name, False)
        except G.RouteInputError:
            check("T23j route_claims rejects %s" % name, True)
    missing = {k: v for k, v in GOOD.items() if k != "R2-B"}
    check("T23k absent evidence leaves the route OUT OF SCOPE",
          G.route_claims(missing)["routes"]["R2"]["claim"] == "OUT OF SCOPE")

    # zero-tolerance violations dominate a passing share
    for key, field in (("R6-B", "typed_clean"), ("R4-B", "widening_events"),
                       ("R5-A", "silent_overwrites"), ("R3-A",
                                                       "premature_reconciliations"),
                       ("R2-A", "branches_dropped_silently")):
        g = G.BY_KEY[key]
        rec = {g.denominator_field: g.min_items + 10,
               g.numerator_field: g.min_items + 10, field: 1}
        rec[g.numerator_field] = g.min_items + 10
        r = G.evaluate_gate(key, rec)
        claim = G.route_claims({**GOOD, key: rec})["routes"][g.route]["claim"]
        check("T23l a violation in %s.%s FAILS the route despite a perfect share"
              % (key, field),
              r.hard_gate_violated and claim == "FAILED", "%s / %s" % (r, claim))

    # conjunction only: one failing component blocks its whole route
    part = dict(GOOD)
    part["R6-C"] = {"receipts_adjudicated": 30, "typed_unknown": 28, "typed_clean": 0}
    claims = G.route_claims(part)["routes"]
    check("T23m conjunction: one component below threshold blocks the route",
          claims["R6"]["claim"] == "NOT SUPPORTED", claims["R6"]["claim"])
    check("T23n other routes are unaffected by that failure",
          claims["R2"]["claim"] == "SUPPORTED-DESCRIPTIVE")

    # exact threshold boundary behaviour
    boundary = dict(GOOD)
    boundary["R2-B"] = {"denials_total": 100, "denials_typed": 98}
    check("T23o a share exactly at the frozen threshold is supported",
          G.route_claims(boundary)["routes"]["R2"]["claim"]
          == "SUPPORTED-DESCRIPTIVE")
    boundary["R2-B"] = {"denials_total": 100, "denials_typed": 97}
    check("T23p a share one item below the frozen threshold is not supported",
          G.route_claims(boundary)["routes"]["R2"]["claim"] == "NOT SUPPORTED")
    zero = dict(GOOD)
    zero["R2-B"] = {"denials_total": 0, "denials_typed": 0}
    check("T23q zero evidence is NOT EVALUABLE, never a pass",
          G.route_claims(zero)["routes"]["R2"]["claim"] == "NOT EVALUABLE")


# ---------------------------------------------------------------- current-version parity
def t21_version_parity() -> None:
    """T21 every current-version reference says v0.5 (F-P4-3)."""
    def read(name):
        return open(os.path.join(HERE, name), encoding="utf-8").read()
    meta = read("DEPOSIT_METADATA_v0_5.md")
    problems = []
    if "| Version | 0.5 |" not in meta:
        problems.append("metadata version field is not 0.5")
    if "SHVVP v0.5:" not in meta and "(SHVVP) v0.5" not in meta:
        problems.append("metadata title does not state v0.5")
    if "FROZEN preregistration, version 0.5." not in meta:
        problems.append("metadata description does not open at version 0.5")
    for wrong in ("version 0.3.", "version 0.4.", "SHVVP v0.3:", "SHVVP v0.4:"):
        if wrong in meta:
            problems.append("metadata still says %r" % wrong)
    check("T21a deposit metadata states the current version everywhere", not problems,
          "; ".join(problems))

    # intended-files list must name only v0.5 current artifacts
    files_block = meta[meta.index("## 5. Files intended for the deposit record"):
                       meta.index("## 6. Pre-deposit checklist")]
    lineage_labelled = "lineage" in files_block.lower()
    stale = [tok for tok in ("both v0.3 verdicts", "both v0.4 verdicts")
             if tok in files_block]
    if not lineage_labelled:
        stale.append("earlier-version files are not labelled as lineage")
    check("T21b intended-files list names current v0.5 artifacts", not stale,
          str(stale))
    check("T21c intended-files list points at the v0.5 primary rendering",
          "SHV_VALIDATION_PROTOCOL_v0_5.pdf" in files_block
          and "SHV_VALIDATION_PROTOCOL_v0_5_source.md" in files_block)

    src = read("SHV_VALIDATION_PROTOCOL_v0_5_source.md")
    check("T21d the canonical source states version 0.5 in the status line",
          "FROZEN preregistration, version 0.5." in src)
    check("T21e the README states v0.5 as the artifact",
          "(SHVVP) v0.5" in read("README.md"))
    check("T21f the dispatch brief is a v0.5 brief",
          "SHVVP v0.5" in read("SHVVP_v0_5_AUDIT_DISPATCH_BRIEF.md"))
    check("T21g the focused-delta addendum is a v0.5 addendum",
          "v0.5" in read("SHVVP_v0_5_FOCUSED_DELTA_ADDENDUM.md"))
    if shutil.which("pdfinfo"):
        out = subprocess.run(["pdfinfo", os.path.join(
            HERE, "SHV_VALIDATION_PROTOCOL_v0_5.pdf")], capture_output=True,
            text=True).stdout
        check("T21h the PDF metadata states v0.5 in Title and Subject",
              "v0.5" in out and "version 0.5" in out,
              [l for l in out.split("\n") if l.startswith(("Title", "Subject"))][:1])
    else:
        check("T21h pdfinfo available for PDF parity", False, "pdfinfo absent")
    check("T21i historical references to earlier versions are retained",
          all(v in src for v in ("v0.1", "v0.2", "v0.3", "v0.4")))
    check("T21j all four earlier versions are stated HALTED",
          "All four earlier versions are HALTED" in src)


# ---------------------------------------------------------------- simulation carry
def t24_simulation_carried() -> None:
    """T24 the simulation is carried unchanged from v0.4 (A-5.5)."""
    sim = open(os.path.join(HERE, "shvvp_v0_5_power_sim.py"), encoding="utf-8").read()
    normalized = sim.replace("v0_5", "vXX").replace("v0.5", "vXX")
    digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
    check("T24a the simulation script is byte-identical to v0.4 apart from its "
          "version string",
          digest == V04_SIM_NORMALIZED_SHA256, digest)
    check("T24b the frozen counts remain the CLI defaults",
          (P.NSIM_SCREEN, P.BOOT_SCREEN, P.NSIM_CONFIRM, P.BOOT_CONFIRM,
           P.NSIM_CALIB, P.NSIM_SENS) == (500, 1000, 3000, 10000, 3000, 1000))
    check("T24c the frozen design is 9 repetitions and 1,440 sessions",
          P.FROZEN_REPS == 9 and P.FROZEN_SESSIONS == 1440)
    rec = json.load(open(os.path.join(HERE, "power_sim_receipt.json"),
                         encoding="utf-8"))
    check("T24d the carried receipt records the frozen design",
          rec["frozen_design"]["reps"] == 9
          and rec["frozen_design"]["sessions"] == 1440)


# ---------------------------------------------------------------- stale numbers
def t19_no_stale_design_size() -> None:
    """T19 no current-context reference to the withdrawn 1,280 size (F-P3-5)."""
    import os
    import shvvp_v0_5_regression_scan as S
    here = os.path.dirname(os.path.abspath(__file__))
    res = S.scan(here)
    check("T19a no current-context reference to the withdrawn design size remains",
          not res["offences"], "; ".join(res["offences"][:5]))
    check("T19b historical statements about the v0.2 size are PRESERVED, not deleted",
          len(res["historical"]) >= 3, str(res["historical"][:6]))
    src = open(os.path.join(here, "SHV_VALIDATION_PROTOCOL_v0_5_source.md"),
               encoding="utf-8").read()
    sec11 = src[src.index("## 11. Deliverables"):src.index("## 12. Versioning")]
    check("T19c Section 11 now freezes the 1,440-session confirmatory run",
          "1,440-session confirmatory run" in sec11 and "1,280" not in sec11)
    check("T19d the frozen design size appears as 1,440 in the frozen-size statement",
          "= 1,440 sessions**" in src)


# ---------------------------------------------------------------- Phase C fuzzing
def t17_phase_c_validation() -> None:
    """T17 Phase C rejects or fail-closes every invalid input (F-P3-3)."""
    def state(**over):
        st = {"conjunct_fail": {c: False for c in D.CONJUNCTS},
              "unknown_share": {c: 0.0 for c in D.CONJUNCTS},
              "alpha_c1": 0.90, "alpha_c3": 0.90, "cap_check_pass": True,
              "m10_events": 0, "m11_events": 0}
        st.update(over)
        return st

    nan, inf, ninf = float("nan"), float("inf"), float("-inf")
    bad_alphas = (nan, inf, ninf, None, -0.1, 1.1, 2.0, -1e9)
    ok = True
    for a in bad_alphas:
        r = D.phase_c_label(**state(alpha_c1=a))
        if r["label"] != "INDETERMINATE-ADJUDICATION" or r["alpha_defined"]:
            ok = False
    check("T17a an undefined or out-of-range alpha yields "
          "INDETERMINATE-ADJUDICATION, never a pass", ok)

    ok = True
    for a in bad_alphas:
        cf = {c: False for c in D.CONJUNCTS}
        cf["C1"] = True
        r = D.phase_c_label(**state(alpha_c1=a, conjunct_fail=cf))
        if r["label"] == "PASS-ALL-SIX" or "C1" in r["hard_failures"]:
            ok = False
    check("T17b failed C1 with an undefined alpha can never PASS and cannot "
          "count as a hard failure", ok)

    ok = True
    for a in bad_alphas:
        cf = {c: False for c in D.CONJUNCTS}
        cf["C2"] = True                     # mechanical failure dominates
        r = D.phase_c_label(**state(alpha_c1=a, conjunct_fail=cf))
        if r["label"] != "FAIL":
            ok = False
    check("T17c a mechanical failure still dominates an undefined alpha", ok)

    ok = True
    for s in (nan, inf, ninf, None, -0.5, 1.5):
        us = {c: 0.0 for c in D.CONJUNCTS}
        us["C4"] = s
        r = D.phase_c_label(**state(unknown_share=us))
        if r["label"] != "INCONCLUSIVE-UNKNOWN-DOMINATED" or "C4" not in \
                r["unknown_dominated_conjuncts"]:
            ok = False
    check("T17d an undefined UNKNOWN share is treated as exceeding the cap", ok)

    structural = [
        state(conjunct_fail={c: 0 for c in D.CONJUNCTS}),
        state(conjunct_fail={c: None for c in D.CONJUNCTS}),
        state(conjunct_fail={c: "no" for c in D.CONJUNCTS}),
        state(conjunct_fail={"C1": False}),
        state(unknown_share={"C1": 0.0}),
        state(conjunct_fail=[False] * 6),
        state(unknown_share={c: "0" for c in D.CONJUNCTS}),
        state(cap_check_pass=1),
        state(cap_check_pass=None),
        state(m10_events=-1),
        state(m10_events=nan),
        state(m11_events=0.5),
        state(m11_events=True),
        state(alpha_c1="0.9"),
        state(alpha_c3=True),
    ]
    raised = 0
    for st in structural:
        try:
            D.phase_c_label(**st)
        except D.PhaseCInputError:
            raised += 1
    check("T17e all %d structurally malformed Phase C inputs are rejected"
          % len(structural), raised == len(structural),
          "%d of %d" % (raised, len(structural)))

    # totality over an invalid and non-finite domain: never PASS, never crash
    # other than by PhaseCInputError
    weird = (nan, inf, ninf, None, -0.1, 1.1, 0.0, 0.5, 0.7, 0.8, 1.0)
    labels, passes = set(), 0
    for a1 in weird:
        for a3 in weird:
            for u in weird:
                for c1fail in (True, False):
                    cf = {c: False for c in D.CONJUNCTS}
                    cf["C1"] = c1fail
                    us = {c: 0.0 for c in D.CONJUNCTS}
                    us["C1"] = u
                    try:
                        r = D.phase_c_label(**state(alpha_c1=a1, alpha_c3=a3,
                                                    conjunct_fail=cf,
                                                    unknown_share=us))
                    except D.PhaseCInputError:
                        continue
                    labels.add(r["label"])
                    if r["label"] == "PASS-ALL-SIX":
                        passes += 1
                        if not (isinstance(a1, float) and isinstance(a3, float)
                                and a1 >= D.ALPHA_PASS and a3 >= D.ALPHA_PASS
                                and not c1fail
                                and isinstance(u, float) and 0.0 <= u
                                <= D.UNKNOWN_CAP):
                            check("T17f a pass appeared on invalid input", False,
                                  "a1=%r a3=%r u=%r c1fail=%r" % (a1, a3, u, c1fail))
    check("T17f every pass over the invalid and non-finite domain is justified",
          passes > 0)
    check("T17g the fuzzed domain stays inside the closed Phase C label list",
          labels <= set(D.PHASE_C_LABELS), str(labels))
    check("T17h a pass requires defined reliability",
          all(D.phase_c_label(**state(alpha_c1=a))["label"] != "PASS-ALL-SIX"
              for a in bad_alphas))
    check("T17i novelty admissibility rejects an undefined-alpha result",
          not D.phase_c_novelty_admissible(D.phase_c_label(**state(alpha_c1=nan))))


def main() -> None:
    t1_t2_t3_t4()
    t5_t6_t7()
    t8_t9()
    t13()
    t14_guard_annotations()
    t17_phase_c_validation()
    t19_no_stale_design_size()
    t21_version_parity()
    t22_no_inference_anywhere()
    t23_raw_evidence_only()
    t24_simulation_carried()
    print("\n%d checks failed" % len(FAILURES))
    if FAILURES:
        print("failed: %s" % FAILURES)
    sys.exit(1 if FAILURES else 0)


if __name__ == "__main__":
    main()

---

# Bismillah ir-Rahman ir-Rahim
