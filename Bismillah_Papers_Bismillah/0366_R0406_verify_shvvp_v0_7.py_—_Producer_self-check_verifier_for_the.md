# Bismillah ir-Rahman ir-Rahim

# R0406 -- verify_shvvp_v0_7.py — Producer self-check verifier for the SHVVP v0.7 release.

**Chronological Index:** 366 of 995  
**Date:** 2026-07-26  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** verify_shvvp_v0_7.py  
**Source Format:** py  
**SHA-256:** `daef89a58073ac02342d348a47dccfa3a17c0f4a6961762e8c2ae0e02ebc3a7a`  

---

## R0406 · verify_shvvp_v0_7.py — Producer self-check verifier for the SHVVP v0.7 release.

- section: V. BSSG & SHVVP Protocols
- source_file: verify_shvvp_v0_7.py
- source_format: py
- text_sha256: daef89a58073ac02342d348a47dccfa3a17c0f4a6961762e8c2ae0e02ebc3a7a

"""Producer self-check verifier for the SHVVP v0.7 release.

Producer self-check only, not an audit and not an attestation. It re-proves the
F-P6-1 closure by running the self-sealing attack INLINE against the gate with an
ephemeral custodian key, independently of the test file, so a mistaken fixture in
the suite cannot make this pass. It replaces the v0.6 five-phrase stale-reference
scan (which gave false confidence, finding F-P6-2) with a STRUCTURED current-status
parity check over a single canonical release-metadata object.

Run: `python3 verify_shvvp_v0_7.py [--v05-release DIR]` -> exits non-zero on any gate
failure and writes verify_shvvp_v0_7_receipt.json.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "SHV_VALIDATION_PROTOCOL_v0_7_source.md")
PDF = os.path.join(HERE, "SHVVP_v0_7_flagship.pdf")
TESTS = os.path.join(HERE, "test_shvvp_v0_7_rules.py")

RELEASE_META = {"version": "0.7", "freeze_date": "2026-07-26", "flagship_pages": None}

RESULTS: list[tuple[str, bool, str]] = []


def gate(name, cond, detail=""):
    RESULTS.append((name, bool(cond), detail))
    print("%-6s %s%s" % ("PASS" if cond else "FAIL", name,
                         ("  [%s]" % detail) if detail and not cond else ""))


def sha256(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--v05-release", default=None)
    args = ap.parse_args()
    sys.path.insert(0, HERE)
    import shvvp_v0_7_route_gates as G

    # G1 -- manifest digest reproducible and binds the authority + protocol version.
    canon = G._manifest_canonical()
    gate("G1 manifest digest reproducible and binds authority+version",
         G.MANIFEST_SHA256 == hashlib.sha256(canon.encode()).hexdigest()
         and G.COMMITMENT_AUTHORITY_PUBKEY in canon and G.PROTOCOL_VERSION in canon,
         G.MANIFEST_SHA256)

    # G2 -- 11 components, R4-C committed to 216, one predeclared exclusion.
    gate("G2 manifest covers 11 components, R4-C=216, one predeclared OOS",
         set(G.MANIFEST_BY_KEY) == set(G.BY_KEY) and len(G.BY_KEY) == 11
         and G.MANIFEST_BY_KEY["R4-C"].universe_n == 216
         and [e.key for e in G.SCOPE_MANIFEST
              if e.status == G.STATUS_PREDECLARED_CONDITIONAL_OOS] == ["R3-A"])

    # G3 -- F-P6-1 closed INLINE with an ephemeral custodian key (self-contained).
    cust = Ed25519PrivateKey.generate()
    pub = cust.public_key().public_bytes_raw().hex()
    atk = Ed25519PrivateKey.generate()

    def sealed(key, n, signer=cust, **ovr):
        e = G.MANIFEST_BY_KEY[key]
        c = {"protocol_version": G.PROTOCOL_VERSION, "manifest_sha256": G.MANIFEST_SHA256,
             "component": key, "universe_id": e.universe_id, "sealed_universe_n": n,
             "sealed_universe_inventory_hash": "a" * 64, "authority": "v",
             "commitment_sequence": 1, "committed_at": "2026-07-26T00:00:00Z"}
        c.update(ovr)
        c["signature"] = signer.sign(G.sealed_commitment_payload(c)).hex()
        return c

    def raw(key, d, num, viol=None):
        e = G.MANIFEST_BY_KEY[key]; s = G.BY_KEY[key]
        r = {s.denominator_field: d, s.numerator_field: num,
             "manifest_sha256": G.MANIFEST_SHA256, "universe_id": e.universe_id}
        if s.violation_field:
            r[s.violation_field] = 0 if viol is None else viol
        if e.kind in (G.KIND_SEALED, G.KIND_REALIZED):
            r["commitment_id"] = key + "-c"
        return r

    def raises(fn):
        try:
            fn(); return False
        except G.RouteInputError:
            return True

    # authoritative R5-A universe is 25; a favorable 20/20 subset must be rejected,
    # a forged commitment (attacker key) declaring 20 must be rejected, a missing
    # commitment must be rejected, a smuggled authority field must be rejected, and
    # the full authentic 25/25 must pass.
    comm = {"R5-A": sealed("R5-A", 25)}
    a_subset = raises(lambda: G.evaluate_gate(
        "R5-A", raw("R5-A", 20, 20), comm["R5-A"], None, pub))
    a_forge = raises(lambda: G.evaluate_gate(
        "R5-A", raw("R5-A", 20, 20), sealed("R5-A", 20, signer=atk), None, pub))
    a_missing = raises(lambda: G.evaluate_gate("R5-A", raw("R5-A", 20, 20),
                                               None, None, pub))
    a_smuggle = raises(lambda: G.evaluate_gate(
        "R5-A", {**raw("R5-A", 25, 25), "sealed_universe_n": 20}, comm["R5-A"],
        None, pub))
    authentic = G.evaluate_gate("R5-A", raw("R5-A", 25, 25), comm["R5-A"], None, pub)
    gate("G3 F-P6-1 self-seal closed inline (subset/forge/missing/smuggle rejected, "
         "authentic passes)",
         a_subset and a_forge and a_missing and a_smuggle and authentic.gate_pass,
         "subset=%s forge=%s missing=%s smuggle=%s authentic=%s"
         % (a_subset, a_forge, a_missing, a_smuggle, authentic.gate_pass))

    # G4 -- the v0.7 test suite passes.
    proc = subprocess.run([sys.executable, TESTS], capture_output=True, text=True)
    gate("G4 test_shvvp_v0_7_rules.py exits clean", proc.returncode == 0,
         proc.stdout.strip().splitlines()[-1] if proc.stdout else "no output")

    # G5 -- STRUCTURED current-status parity (replaces the v0.6 phrase scanner).
    src = open(SRC, encoding="utf-8").read()
    v = RELEASE_META["version"]
    checks = {
        "header title vN": ("(SHVVP) v%s" % v) in src,
        "byline version N": ("Version %s, freeze date %s"
                             % (v, RELEASE_META["freeze_date"])) in src,
        "status version N": ("FROZEN preregistration, version %s." % v) in src,
        "ending vN": ("End of frozen contract v%s." % v) in src,
        "self-carries-no-verdict": ("v%s itself carries no verdict" % v) in src,
    }
    # forbidden: any superseded version asserted as the CURRENT document/status.
    forbidden_patterns = [
        r"End of frozen contract v0\.[1-6]\b",
        r"exactly one component class in v0\.[1-6]\b",
        r"OUT OF SCOPE for v0\.[1-6]\b",
        r"Nothing here is a verdict on v0\.[1-6]\b",
        r"\|\s*5\s*\|\s*v0\.5\s*\|\s*Pending",
        r"version %s\b" % re.escape("0.6"),  # 'version 0.6' as a current-status claim
    ]
    hits = []
    for pat in forbidden_patterns:
        for m in re.finditer(pat, src):
            w = src[max(0, m.start() - 60):m.start()]
            # allow inside amendment/appendix prose that quotes the fix or history
            if not re.search(r"A-7\.|finding-to-change|round 6|round 5|HALTED|"
                             r"unmodified|historical|Supersedes|superseded", w):
                hits.append(m.group(0))
    gate("G5 structured current-status parity holds",
         all(checks.values()) and not hits,
         "failing: %s hits: %s"
         % ([k for k, ok in checks.items() if not ok], hits))

    # G6 -- no em-dash; six-label list; Section 8.1b present.
    gate("G6 no em-dash, six labels incl INCOMPLETE, Section 8.1b present",
         "\u2014" not in src and "\u2013" not in src
         and "These six are exhaustive and closed" in src
         and "### 8.1b Frozen universe-commitment channels" in src)

    # G7 -- flagship present, page count consistent, no all-black page.
    pages, black, pdf_ok = 0, [], os.path.exists(PDF)
    if pdf_ok:
        try:
            import fitz
            doc = fitz.open(PDF)
            pages = doc.page_count
            RELEASE_META["flagship_pages"] = pages
            for i, p in enumerate(doc):
                px = p.get_pixmap(dpi=60, colorspace=fitz.csGRAY)
                if sum(1 for b in px.samples if b < 40) / len(px.samples) > 0.5:
                    black.append(i + 1)
        except Exception as exc:
            pdf_ok = False
            print("  (pdf inspection unavailable: %s)" % exc)
    gate("G7 flagship PDF present and free of all-black pages",
         pdf_ok and not black, "pages=%d black=%s" % (pages, black))

    # G8 -- modules carried unchanged from v0.5 are byte-identical.
    carried = ("shvvp_v0_5_decision_rules.py", "shvvp_v0_5_power_sim.py",
               "test_shvvp_v0_5_rules.py", "power_sim_receipt.json")
    if args.v05_release:
        mism = [n for n in carried
                if not (os.path.exists(os.path.join(HERE, n))
                        and os.path.exists(os.path.join(args.v05_release, n))
                        and sha256(os.path.join(HERE, n))
                        == sha256(os.path.join(args.v05_release, n)))]
        gate("G8 carried-unchanged modules byte-identical to v0.5", not mism,
             "mismatched: %s" % mism)
    else:
        present = [n for n in carried if os.path.exists(os.path.join(HERE, n))]
        gate("G8 carried-unchanged modules present (pass --v05-release to diff)",
             len(present) == len(carried))

    receipt = {
        "artifact": "SHVVP v0.7 release", "manifest_sha256": G.MANIFEST_SHA256,
        "commitment_authority_pubkey": G.COMMITMENT_AUTHORITY_PUBKEY,
        "flagship_pdf_sha256": sha256(PDF) if os.path.exists(PDF) else None,
        "flagship_pages": pages,
        "gates": [{"name": n, "pass": ok, "detail": d} for n, ok, d in RESULTS],
        "all_pass": all(ok for _, ok, _ in RESULTS),
        "note": "producer self-check only; a fresh two-family carrying audit that "
                "executes the gate is required before deposit",
    }
    open(os.path.join(HERE, "verify_shvvp_v0_7_receipt.json"), "w").write(
        json.dumps(receipt, indent=2))
    failed = [n for n, ok, _ in RESULTS if not ok]
    print("\n%d gates, %d failed" % (len(RESULTS), len(failed)))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

---

# Bismillah ir-Rahman ir-Rahim
