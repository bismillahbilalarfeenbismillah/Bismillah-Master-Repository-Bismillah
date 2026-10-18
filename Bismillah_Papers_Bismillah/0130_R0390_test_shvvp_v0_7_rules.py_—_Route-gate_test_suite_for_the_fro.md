# Bismillah ir-Rahman ir-Rahim

# R0390 -- test_shvvp_v0_7_rules.py — Route-gate test suite for the frozen SHVVP v0.7 protocol.

**Chronological Index:** 130 of 995  
**Date:** 2026  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** test_shvvp_v0_7_rules.py  
**Source Format:** py  
**SHA-256:** `307354bda38b533083626d6884b69e67c160598d40a80507eb8e2ea690255999`  

---

## R0390 · test_shvvp_v0_7_rules.py — Route-gate test suite for the frozen SHVVP v0.7 protocol.

- section: V. BSSG & SHVVP Protocols
- source_file: test_shvvp_v0_7_rules.py
- source_format: py
- text_sha256: 307354bda38b533083626d6884b69e67c160598d40a80507eb8e2ea690255999

"""Route-gate test suite for the frozen SHVVP v0.7 protocol.

The v0.6 suite's fatal flaw (finding F-P6-1) was that its `bound()` helper defaulted
the sealed or realized cardinality to the submitted denominator and fabricated the
hash, so the tests ASSUMED the property under test and 62 green checks proved nothing
about a self-declared universe. This suite fixes that at the root: the AUTHORITATIVE
universe commitments (Channel A) and the untrusted raw evidence (Channel B) are built
by SEPARATE helpers, the committed cardinalities are deliberately set DIFFERENT from
the favorable subset an attacker would submit, and the evidence helper has no ability
to sign or alter a commitment. The ephemeral custodian key is generated at test time,
so no secret ships.

Run: `python3 test_shvvp_v0_7_rules.py` -> exits non-zero if any check fails.
"""
from __future__ import annotations

import copy
import os

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

import shvvp_v0_7_route_gates as G

HERE = os.path.dirname(os.path.abspath(__file__))
FAILURES: list[str] = []
COUNT = 0

# The custodian's key. PRIVATE half exists only inside this test process and is
# never written anywhere; PUBLIC half is passed to the gate as the operator's
# trusted verification key. The attacker key below is a DIFFERENT keypair with no
# authority.
_CUSTODIAN = Ed25519PrivateKey.generate()
CUSTODIAN_PUB = _CUSTODIAN.public_key().public_bytes_raw().hex()
_ATTACKER = Ed25519PrivateKey.generate()

# Authoritative committed universes, fixed here as the pre-results commitment. These
# are deliberately LARGER than the favorable subset the self-seal attack submits.
SEALED_N = {"R1-A": 8, "R5-A": 25, "R5-C": 9}
REALIZED_N = {"R2-B": 100, "R4-B": 60, "R6-B": 40, "R6-C": 35}


def check(name: str, cond: bool, detail: str = "") -> None:
    global COUNT
    COUNT += 1
    if cond:
        print("PASS  %s" % name)
    else:
        print("FAIL  %s%s" % (name, ("  [%s]" % detail) if detail else ""))
        FAILURES.append(name)


def _raises(fn) -> bool:
    try:
        fn()
        return False
    except G.RouteInputError:
        return True


# ---- Channel A: authoritative commitment fixtures, signed by the custodian ----
def sealed_commitment(key, n, signer=_CUSTODIAN, **override):
    entry = G.MANIFEST_BY_KEY[key]
    c = {
        "protocol_version": G.PROTOCOL_VERSION,
        "manifest_sha256": G.MANIFEST_SHA256,
        "component": key,
        "universe_id": entry.universe_id,
        "sealed_universe_n": n,
        "sealed_universe_inventory_hash": "a" * 64,
        "authority": "test custodian",
        "commitment_sequence": 1,
        "committed_at": "2026-07-25T00:00:00Z",
    }
    c.update(override)
    c["signature"] = signer.sign(G.sealed_commitment_payload(c)).hex()
    return c


def run_close(key, total, signer=_CUSTODIAN, run_id=None, **override):
    entry = G.MANIFEST_BY_KEY[key]
    run_id = run_id or ("run-%s" % key)
    events = [{"sequence": i, "event_type": "qualifying", "idx": i}
              for i in range(1, total + 1)]
    final = G.run_log_chain(run_id, events, G.MANIFEST_SHA256)
    receipt = {
        "protocol_version": G.PROTOCOL_VERSION,
        "manifest_sha256": G.MANIFEST_SHA256,
        "component": key,
        "universe_id": entry.universe_id,
        "run_id": run_id,
        "realized_total": total,
        "first_sequence": 1,
        "last_sequence": total,
        "final_chain_hash": final,
        "authority": "test custodian",
        "committed_at": "2026-07-25T00:00:00Z",
    }
    receipt.update(override)
    receipt["signature"] = signer.sign(G.run_close_payload(receipt)).hex()
    return receipt, events


def commitments_and_logs():
    comm = {}
    logs = {}
    for k, n in SEALED_N.items():
        comm[k] = sealed_commitment(k, n)
    for k, n in REALIZED_N.items():
        r, ev = run_close(k, n)
        comm[k] = r
        logs[k] = ev
    return comm, logs


# ---- Channel B: untrusted raw evidence. Cannot define or alter a universe. ----
def raw(key, denom, num, viol=None, recon=None):
    entry = G.MANIFEST_BY_KEY[key]
    spec = G.BY_KEY[key]
    r = {spec.denominator_field: denom, spec.numerator_field: num,
         "manifest_sha256": G.MANIFEST_SHA256, "universe_id": entry.universe_id}
    if spec.violation_field:
        r[spec.violation_field] = 0 if viol is None else viol
    if entry.kind in (G.KIND_SEALED, G.KIND_REALIZED):
        r["commitment_id"] = "%s-commit-001" % key
    if recon is not None:
        r["reconciliation"] = recon
    return r


def good_evidence():
    # every denominator equals its committed universe (full submission)
    return {
        "R1-A": raw("R1-A", 8, 8),
        "R2-A": raw("R2-A", 16, 16, viol=0),
        "R2-B": raw("R2-B", 100, 100),
        "R3-A": raw("R3-A", 12, 12, viol=0),
        "R4-B": raw("R4-B", 60, 60, viol=0),
        "R4-C": raw("R4-C", 216, 216, viol=0),
        "R5-A": raw("R5-A", 25, 25, viol=0),
        "R5-C": raw("R5-C", 9, 9, viol=0),
        "R6-A": raw("R6-A", 60, 60, viol=0),
        "R6-B": raw("R6-B", 40, 40, viol=0),
        "R6-C": raw("R6-C", 35, 35, viol=0),
    }


def claims(evidence, comm=None, logs=None, pub=None):
    if comm is None or logs is None:
        comm, logs = commitments_and_logs()
    return G.route_claims(evidence, commitments=comm, run_logs=logs,
                          trusted_pubkey=pub or CUSTODIAN_PUB)


# ---------------------------------------------------------------- positive path
def t_positive() -> None:
    out = claims(good_evidence())
    check("P1 a full, authentically committed corpus is all SUPPORTED-DESCRIPTIVE",
          set(v["claim"] for v in out["routes"].values()) == {"SUPPORTED-DESCRIPTIVE"},
          str({k: v["claim"] for k, v in out["routes"].items()}))
    check("P2 six closed descriptive labels including INCOMPLETE",
          len(G.ROUTE_CLAIM_LABELS) == 6 and "INCOMPLETE" in G.ROUTE_CLAIM_LABELS
          and set(G.ROUTE_CLAIM_LABELS) == {"OUT OF SCOPE", "INCOMPLETE", "FAILED",
                                            "NOT EVALUABLE", "NOT SUPPORTED",
                                            "SUPPORTED-DESCRIPTIVE"})
    check("P3 no inference is produced", out["inference"].startswith("NONE"))
    check("P4 route output records the trusted authority",
          out["commitment_authority_pubkey"] == CUSTODIAN_PUB
          and out["protocol_version"] == "0.7")
    # an authentic reconciled shortfall that still clears the threshold is supported
    comm, logs = commitments_and_logs()
    ev = good_evidence()
    ev["R5-A"] = raw("R5-A", 24, 24, viol=0,
                     recon={"universe_n": 25, "excluded": [{"count": 1,
                            "reason": "one descendant not yet corrected"}]})
    r5 = claims(ev, comm, logs)["routes"]["R5"]["claim"]
    check("P5 an authentic reconciled 24-of-25 (0.96 >= 0.95) is still SUPPORTED",
          r5 == "SUPPORTED-DESCRIPTIVE", r5)


# ------------------------------------------------- F-P6-1 sealed-universe attacks
def t_fp61_sealed() -> None:
    comm, logs = commitments_and_logs()
    # (1) the exact v0.6 self-seal: submit favorable 20, declare 20 the universe.
    # With no forged commitment, the authoritative R5-A commitment says 25, so a
    # bare 20/20 subset is rejected as an unreconciled shortfall.
    ev = good_evidence(); ev["R5-A"] = raw("R5-A", 20, 20, viol=0)
    check("A1 R5-A 20 of authoritatively committed 25, no reconciliation, rejected",
          _raises(lambda: claims(ev, comm, logs)))
    # (2) attacker forges a commitment declaring 20, signs with the WRONG key.
    forged = sealed_commitment("R5-A", 20, signer=_ATTACKER)
    c2 = dict(comm); c2["R5-A"] = forged
    check("A2 a commitment declaring 20 signed by a non-authority key is rejected",
          _raises(lambda: claims(ev, c2, logs)))
    # (3) same, but with a well-formed random 64-hex inventory hash.
    forged3 = sealed_commitment("R5-A", 20, signer=_ATTACKER,
                                sealed_universe_inventory_hash="b" * 64)
    c3 = dict(comm); c3["R5-A"] = forged3
    check("A3 a well-formed forged hash signed by a non-authority is rejected",
          _raises(lambda: claims(ev, c3, logs)))
    # (4) tamper a genuine commitment's cardinality after signing.
    t4 = copy.deepcopy(comm["R5-A"]); t4["sealed_universe_n"] = 20
    c4 = dict(comm); c4["R5-A"] = t4
    check("A4 mutating sealed_universe_n after signing breaks the signature",
          _raises(lambda: claims(ev, c4, logs)))
    # (5) tamper the inventory digest after signing.
    t5 = copy.deepcopy(comm["R5-A"]); t5["sealed_universe_inventory_hash"] = "c" * 64
    c5 = dict(comm); c5["R5-A"] = t5
    check("A5 mutating the inventory digest after signing breaks the signature",
          _raises(lambda: claims(good_evidence(), c5, logs)))
    # (6) cross-component replay: a valid R5-C seal presented for R5-A.
    c6 = dict(comm); c6["R5-A"] = comm["R5-C"]
    check("A6 a valid R5-C commitment replayed against R5-A is rejected",
          _raises(lambda: claims(good_evidence(), c6, logs)))
    # (7) cross-manifest replay: commitment bound to a different manifest digest.
    replay = sealed_commitment("R5-A", 25,
                               manifest_sha256="0" * 64)
    c7 = dict(comm); c7["R5-A"] = replay
    check("A7 a commitment bound to another manifest digest is rejected",
          _raises(lambda: claims(good_evidence(), c7, logs)))
    # (8) cross-version replay.
    replay8 = sealed_commitment("R5-A", 25, protocol_version="0.6")
    c8 = dict(comm); c8["R5-A"] = replay8
    check("A8 a commitment bound to another protocol version is rejected",
          _raises(lambda: claims(good_evidence(), c8, logs)))
    # (9) altered signature bytes.
    t9 = copy.deepcopy(comm["R5-A"])
    t9["signature"] = ("f" + t9["signature"][1:]) if t9["signature"][0] != "f" \
        else ("0" + t9["signature"][1:])
    c9 = dict(comm); c9["R5-A"] = t9
    check("A9 an altered signature is rejected",
          _raises(lambda: claims(good_evidence(), c9, logs)))
    # (10) operator verifies against the FROZEN DEFAULT key (no trusted_pubkey
    # override), while the commitments are signed by the ephemeral custodian key ->
    # no authority match, rejected. (The frozen reference key differs from the
    # test custodian key.)
    check("A10 verifying custodian-signed commitments against the frozen default "
          "authority key is rejected",
          _raises(lambda: G.route_claims(good_evidence(), commitments=comm,
                                         run_logs=logs)))
    # (11) no commitment at all for a sealed component.
    c11 = dict(comm); del c11["R5-A"]
    check("A11 a sealed component with no Channel A commitment is rejected",
          _raises(lambda: claims(good_evidence(), c11, logs)))
    # (12) authority field smuggled into the raw record.
    ev12 = good_evidence()
    ev12["R5-A"] = {**raw("R5-A", 25, 25, viol=0), "sealed_universe_n": 20}
    check("A12 a sealed_universe_n smuggled into the raw record is rejected",
          _raises(lambda: claims(ev12, comm, logs)))


# ---------------------------------------------- F-P6-1 realized-universe attacks
def t_fp61_realized() -> None:
    comm, logs = commitments_and_logs()
    ev = good_evidence()
    # (1) realized run-log bound; wrong (attacker) signing key.
    r_forge, ev_log = run_close("R2-B", 100, signer=_ATTACKER)
    c1 = dict(comm); c1["R2-B"] = r_forge
    l1 = dict(logs); l1["R2-B"] = ev_log
    check("B1 a run-close receipt signed by a non-authority key is rejected",
          _raises(lambda: claims(ev, c1, l1)))
    # (2) truncate the log after favorable events but keep the receipt total=100.
    l2 = dict(logs); l2["R2-B"] = logs["R2-B"][:80]
    check("B2 a run log truncated below the signed realized_total is rejected",
          _raises(lambda: claims(ev, comm, l2)))
    # (3) reorder the log.
    reordered = list(logs["R2-B"]); reordered[0], reordered[1] = reordered[1], reordered[0]
    l3 = dict(logs); l3["R2-B"] = reordered
    check("B3 a reordered run log is rejected",
          _raises(lambda: claims(ev, comm, l3)))
    # (4) duplicate a sequence number.
    dup = list(logs["R2-B"]); dup[50] = dict(dup[49])
    l4 = dict(logs); l4["R2-B"] = dup
    check("B4 a run log with a duplicated sequence is rejected",
          _raises(lambda: claims(ev, comm, l4)))
    # (5) caller realized_total below the verified log count.
    r5, ev5 = run_close("R2-B", 100)
    r5b = copy.deepcopy(r5); r5b["realized_total"] = 50  # unsigned tamper
    c5 = dict(comm); c5["R2-B"] = r5b
    l5 = dict(logs); l5["R2-B"] = ev5
    check("B5 a realized_total mutated below the log count is rejected",
          _raises(lambda: claims(ev, c5, l5)))
    # (6) modify an event after the signed close receipt.
    modified = copy.deepcopy(logs["R2-B"]); modified[10]["event_type"] = "tampered"
    l6 = dict(logs); l6["R2-B"] = modified
    check("B6 a log modified after its signed close receipt is rejected "
          "(chain mismatch)", _raises(lambda: claims(ev, comm, l6)))
    # (7) no run log supplied for a realized component.
    l7 = dict(logs); del l7["R2-B"]
    check("B7 a realized component with no run log is rejected",
          _raises(lambda: claims(ev, comm, l7)))
    # (8) a favorable realized subset (80 of committed 100), no reconciliation.
    ev8 = good_evidence(); ev8["R2-B"] = raw("R2-B", 80, 80)
    check("B8 an 80-of-100 realized subset with no reconciliation is rejected",
          _raises(lambda: claims(ev8, comm, logs)))
    # (9) run_log_hash smuggled into the raw record.
    ev9 = good_evidence(); ev9["R2-B"] = {**raw("R2-B", 100, 100), "run_log_hash": "x"}
    check("B9 a run_log_hash smuggled into the raw record is rejected",
          _raises(lambda: claims(ev9, comm, logs)))


# ------------------------------------------- carried v0.6 closures (still hold)
def t_carried() -> None:
    comm, logs = commitments_and_logs()
    # FIXED subset (R4-C 30 of 216) still rejected; reconciliation cannot inflate.
    ev = good_evidence(); ev["R4-C"] = raw("R4-C", 30, 30, viol=0)
    check("C1 R4-C 30 of fixed 216, no reconciliation, still rejected",
          _raises(lambda: claims(ev, comm, logs)))
    ev["R4-C"] = raw("R4-C", 30, 30, viol=0,
                     recon={"universe_n": 216, "excluded": [{"count": 186,
                            "reason": "not run"}]})
    r4 = claims(ev, comm, logs)
    comp = r4["components"]["R4-C"]
    check("C2 a reconciled R4-C 30/216 scores 30/216 and does not pass",
          comp["denominator"] == 216 and comp["numerator"] == 30
          and not comp["gate_pass"])
    # omission of a committed component -> INCOMPLETE, never OUT OF SCOPE.
    ev = good_evidence(); del ev["R2-B"]
    r2 = claims(ev, comm, logs)["routes"]["R2"]
    check("C3 deleting committed R2-B yields INCOMPLETE, not OUT OF SCOPE",
          r2["claim"] == "INCOMPLETE" and "R2-B" in r2["missing_committed"])
    # present unfavorable -> NOT SUPPORTED (observed failure not masked).
    ev = good_evidence(); ev["R2-B"] = raw("R2-B", 100, 0)
    check("C4 R2-B 0/100 present is NOT SUPPORTED",
          claims(ev, comm, logs)["routes"]["R2"]["claim"] == "NOT SUPPORTED")
    # R3 predeclared exclusion preserved.
    ev = good_evidence(); del ev["R3-A"]
    check("C5 R3-A absent is validly OUT OF SCOPE",
          claims(ev, comm, logs)["routes"]["R3"]["claim"] == "OUT OF SCOPE")
    check("C6 R3-A present is evaluated, not excused",
          claims(good_evidence(), comm, logs)["routes"]["R3"]["claim"]
          == "SUPPORTED-DESCRIPTIVE")
    # zero-tolerance violation dominates a perfect share.
    ev = good_evidence(); ev["R5-A"] = raw("R5-A", 25, 25, viol=1)
    check("C7 a silent_overwrite violation FAILS R5 despite a perfect share",
          claims(ev, comm, logs)["routes"]["R5"]["claim"] == "FAILED")
    # manifest binding: wrong manifest digest on the raw record.
    ev = good_evidence(); ev["R6-A"] = {**raw("R6-A", 60, 60, viol=0),
                                        "manifest_sha256": "0" * 64}
    check("C8 a raw record bound to the wrong manifest digest is rejected",
          _raises(lambda: claims(ev, comm, logs)))
    # manifest digest is reproducible and binds the authority key.
    import hashlib
    check("C9 manifest digest reproducible and binds the authority + version",
          G.MANIFEST_SHA256 == hashlib.sha256(
              G._manifest_canonical().encode()).hexdigest()
          and G.COMMITMENT_AUTHORITY_PUBKEY in G._manifest_canonical()
          and G.PROTOCOL_VERSION in G._manifest_canonical())
    # derived-object and unknown-key rejections carried from v0.4/v0.5.
    check("C10 a fabricated GateResult is rejected as evidence",
          _raises(lambda: claims({**good_evidence(), "R2-B": G.GateResult(
              key="R2-B", route="R2", phase="B", cls="G", denominator=100,
              numerator=100, violations=0, share=1.0, min_items=50, threshold=0.98,
              evaluable=True, gate_pass=True, hard_gate_violated=False,
              universe_n=100, reasons=(), statement="x", scope_limit="x")}, comm,
              logs)))
    check("C11 an unknown component key is rejected",
          _raises(lambda: claims({**good_evidence(), "R9-Z": {"a": 1}}, comm, logs)))


def main() -> None:
    t_positive()
    t_fp61_sealed()
    t_fp61_realized()
    t_carried()
    print("\n%d checks, %d failures" % (COUNT, len(FAILURES)))
    if FAILURES:
        for n in FAILURES:
            print("  FAILED: %s" % n)
    raise SystemExit(1 if FAILURES else 0)


if __name__ == "__main__":
    main()

---

# Bismillah ir-Rahman ir-Rahim
