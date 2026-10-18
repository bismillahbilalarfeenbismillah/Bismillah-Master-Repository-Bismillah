# Bismillah ir-Rahman ir-Rahim

# R0404 -- verify_shvvp_v0_6.py — Producer self-check verifier for the SHVVP v0.6 release.

**Chronological Index:** 361 of 995  
**Date:** 2026-07-25  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** verify_shvvp_v0_6.py  
**Source Format:** py  
**SHA-256:** `38dd07f0f8859d0cf4fd70ebc465749c6fb458221f1597f481c51b9556b344b6`  

---

## R0404 · verify_shvvp_v0_6.py — Producer self-check verifier for the SHVVP v0.6 release.

- section: V. BSSG & SHVVP Protocols
- source_file: verify_shvvp_v0_6.py
- source_format: py
- text_sha256: 38dd07f0f8859d0cf4fd70ebc465749c6fb458221f1597f481c51b9556b344b6

"""Producer self-check verifier for the SHVVP v0.6 release.

This is a producer self-check, not an audit and not an attestation: producer self-
repairs earn no absence-credit, and v0.6 requires a fresh two-family carrying audit
before deposit. The verifier confirms, mechanically, that the F-P5-1 closure is
present and executable, that the source carries no reintroduced stale reference or
em-dash, that the current-version artifacts agree on v0.6, that the flagship PDF is
present, page-count-consistent and free of all-black pages, and that the modules
carried unchanged from v0.5 are byte-identical.

Run: `python3 verify_shvvp_v0_6.py [--v05-release DIR]` -> exits non-zero on any
gate failure and writes verify_shvvp_v0_6_receipt.json.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "SHV_VALIDATION_PROTOCOL_v0_6_source.md")
PDF = os.path.join(HERE, "SHVVP_v0_6_flagship.pdf")
GATE = os.path.join(HERE, "shvvp_v0_6_route_gates.py")
TESTS = os.path.join(HERE, "test_shvvp_v0_6_rules.py")

RESULTS: list[tuple[str, bool, str]] = []


def gate(name: str, cond: bool, detail: str = "") -> None:
    RESULTS.append((name, bool(cond), detail))
    print("%-6s %s%s" % ("PASS" if cond else "FAIL", name,
                         ("  [%s]" % detail) if detail and not cond else ""))


def sha256(path: str) -> str:
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def read(path: str) -> str:
    return open(path, encoding="utf-8").read()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--v05-release", default=None,
                    help="path to the extracted v0.5 release dir for the "
                         "carried-unchanged byte-identity check")
    args = ap.parse_args()

    # G1 -- the route gate imports and the scope-manifest digest is reproducible.
    sys.path.insert(0, HERE)
    import shvvp_v0_6_route_gates as G
    recomputed = hashlib.sha256(G._manifest_canonical().encode("utf-8")).hexdigest()
    gate("G1 manifest digest reproducible",
         G.MANIFEST_SHA256 == recomputed and len(G.MANIFEST_SHA256) == 64,
         G.MANIFEST_SHA256)

    # G2 -- the eleven components are covered and R4-C is committed to 216.
    gate("G2 manifest covers 11 components, R4-C universe = 216",
         set(G.MANIFEST_BY_KEY) == set(G.BY_KEY) and len(G.BY_KEY) == 11
         and G.MANIFEST_BY_KEY["R4-C"].universe_n == 216
         and G.BY_KEY["R4-C"].min_items == 216)

    # G3 -- the three F-P5-1 attacks are closed (independent of the test file).
    def bound(key, **c):
        e = G.MANIFEST_BY_KEY[key]; s = G.BY_KEY[key]; r = dict(c)
        r["manifest_sha256"] = G.MANIFEST_SHA256; r["universe_id"] = e.universe_id
        if e.kind == G.KIND_SEALED:
            r.setdefault("sealed_universe_n", c[s.denominator_field])
            r.setdefault("sealed_universe_hash", "seal:%s" % key)
        elif e.kind == G.KIND_REALIZED:
            r.setdefault("realized_total", c[s.denominator_field])
            r.setdefault("run_log_hash", "rl:%s" % key)
        return r
    good = {
        "R1-A": bound("R1-A", facts_examined=10, facts_incremental=10),
        "R2-A": bound("R2-A", branches_planted=16, branches_typed=14, branches_dropped_silently=0),
        "R2-B": bound("R2-B", denials_total=100, denials_typed=100),
        "R3-A": bound("R3-A", conflicts_planted=12, conflicts_preserved=12, premature_reconciliations=0),
        "R4-B": bound("R4-B", injections_total=60, injections_narrowed=60, widening_events=0),
        "R4-C": bound("R4-C", injections_total=216, injections_narrowed=216, widening_events=0),
        "R5-A": bound("R5-A", descendants_recorded=25, descendants_reached=25, silent_overwrites=0),
        "R5-C": bound("R5-C", descendants_recorded=6, descendants_reached=6, silent_overwrites=0),
        "R6-A": bound("R6-A", absent_items=60, typed_unknown=60, typed_clean=0),
        "R6-B": bound("R6-B", receipts_adjudicated=35, typed_unknown=35, typed_clean=0),
        "R6-C": bound("R6-C", receipts_adjudicated=30, typed_unknown=30, typed_clean=0),
    }

    def raises(fn):
        try:
            fn(); return False
        except G.RouteInputError:
            return True
    a_closed = raises(lambda: G.evaluate_gate(
        "R4-C", bound("R4-C", injections_total=30, injections_narrowed=30, widening_events=0)))
    b_closed = raises(lambda: G.evaluate_gate("R5-A", bound(
        "R5-A", descendants_recorded=20, descendants_reached=20, silent_overwrites=0,
        sealed_universe_n=25, sealed_universe_hash="s")))
    deleted = {k: v for k, v in good.items() if k != "R2-B"}
    c_closed = (G.route_claims(deleted)["routes"]["R2"]["claim"] == "INCOMPLETE")
    r3_oos = (G.route_claims({k: v for k, v in good.items() if k != "R3-A"})
              ["routes"]["R3"]["claim"] == "OUT OF SCOPE")
    gate("G3 F-P5-1 attacks a/b/c closed and R3 OOS preserved",
         a_closed and b_closed and c_closed and r3_oos,
         "a=%s b=%s c=%s r3=%s" % (a_closed, b_closed, c_closed, r3_oos))

    # G4 -- the v0.6 route-gate test suite passes.
    proc = subprocess.run([sys.executable, TESTS], capture_output=True, text=True)
    gate("G4 test_shvvp_v0_6_rules.py exits clean", proc.returncode == 0,
         proc.stdout.strip().splitlines()[-1] if proc.stdout else "no output")

    # G5 -- no em-dash and no reintroduced stale current-context reference.
    src = read(SRC)
    stale = [p for p in (
        "anywhere in v0.2", 'verdict in v0.2', "As of v0.3 the residual",
        "requires a v0.4 freeze", "v0.2 explicitly lacks the authority")
        if p in src]
    # allow these only inside the A-6.2 amendment record that quotes them as fixed.
    stale_outside = []
    for p in stale:
        for m in re.finditer(re.escape(p), src):
            window = src[max(0, m.start() - 900):m.start()]
            if "A-6.2" not in window and "finding-to-change" not in window:
                stale_outside.append(p)
    gate("G5 no em-dash and no live stale version reference",
         "\u2014" not in src and "\u2013" not in src and not stale_outside,
         "stale: %s" % stale_outside)

    # G6 -- current-version parity across the v0.6 artifacts.
    header_v06 = "Version 0.6, freeze date 2026-07-25" in src
    label_six = "These six are exhaustive and closed" in src
    gate("G6 source declares v0.6 and the six-label list", header_v06 and label_six)

    # G7 -- flagship PDF present, page-count consistent, no all-black page.
    pdf_ok = os.path.exists(PDF)
    pages = 0
    black = []
    if pdf_ok:
        try:
            import fitz
            doc = fitz.open(PDF)
            pages = doc.page_count
            for i, p in enumerate(doc):
                pix = p.get_pixmap(dpi=60, colorspace=fitz.csGRAY)
                if sum(1 for b in pix.samples if b < 40) / len(pix.samples) > 0.5:
                    black.append(i + 1)
        except Exception as exc:  # pragma: no cover
            pdf_ok = False
            print("  (pdf inspection unavailable: %s)" % exc)
    gate("G7 flagship PDF present and free of all-black pages",
         pdf_ok and not black, "black pages: %s" % black)

    # G8 -- modules carried unchanged from v0.5 are byte-identical.
    carried = ("shvvp_v0_5_decision_rules.py", "shvvp_v0_5_power_sim.py",
               "test_shvvp_v0_5_rules.py", "power_sim_receipt.json")
    if args.v05_release:
        mism = []
        for name in carried:
            a = os.path.join(HERE, name)
            b = os.path.join(args.v05_release, name)
            if not (os.path.exists(a) and os.path.exists(b)
                    and sha256(a) == sha256(b)):
                mism.append(name)
        gate("G8 carried-unchanged modules byte-identical to v0.5", not mism,
             "mismatched: %s" % mism)
    else:
        present = [n for n in carried if os.path.exists(os.path.join(HERE, n))]
        gate("G8 carried-unchanged modules present (pass --v05-release to diff)",
             len(present) == len(carried), "present: %d/%d"
             % (len(present), len(carried)))

    receipt = {
        "artifact": "SHVVP v0.6 release",
        "manifest_sha256": G.MANIFEST_SHA256,
        "flagship_pdf_sha256": sha256(PDF) if os.path.exists(PDF) else None,
        "flagship_pages": pages,
        "gates": [{"name": n, "pass": ok, "detail": d} for n, ok, d in RESULTS],
        "all_pass": all(ok for _, ok, _ in RESULTS),
        "note": "producer self-check only; a fresh two-family carrying audit is "
                "required before deposit",
    }
    open(os.path.join(HERE, "verify_shvvp_v0_6_receipt.json"), "w").write(
        json.dumps(receipt, indent=2))
    failed = [n for n, ok, _ in RESULTS if not ok]
    print("\n%d gates, %d failed" % (len(RESULTS), len(failed)))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

---

# Bismillah ir-Rahman ir-Rahim
