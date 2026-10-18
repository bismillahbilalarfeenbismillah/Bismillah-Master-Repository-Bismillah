# Bismillah ir-Rahman ir-Rahim

# R0396 -- test_shvvp_v0_8_rules.py.txt — Adversarial suite for the SHVVP v0.8 route gate (producer-authored).

**Chronological Index:** 132 of 995  
**Date:** 2026  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** test_shvvp_v0_8_rules.py.txt  
**Source Format:** txt  
**SHA-256:** `fd0d38fd1762e2f243c0135bcf54b679e3f5c1f1e69150c2db5d14f4ebdaeee5`  

---

## R0396 · test_shvvp_v0_8_rules.py.txt — Adversarial suite for the SHVVP v0.8 route gate (producer-authored).

- section: V. BSSG & SHVVP Protocols
- source_file: test_shvvp_v0_8_rules.py.txt
- source_format: txt
- text_sha256: fd0d38fd1762e2f243c0135bcf54b679e3f5c1f1e69150c2db5d14f4ebdaeee5

"""Adversarial suite for the SHVVP v0.8 route gate (producer-authored).

Verification is against the THREE FROZEN trust roots using shipped pre-signed vectors;
there is no key override to pass, so these tests exercise the real trust root rather
than a per-call substitute (the trap the producer's own v0.7 suite fell into). An
ephemeral attacker key is generated only to prove that anything NOT signed by a frozen
authority is rejected. No secret is read or shipped.

Run: python3 test_shvvp_v0_8_rules.py  ->  non-zero exit on any failure.
"""
from __future__ import annotations

import copy
import hashlib
import inspect
import json
import os

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

import shvvp_v0_8_route_gates as G

HERE = os.path.dirname(os.path.abspath(__file__))
V = json.load(open(os.path.join(HERE, "shvvp_v0_8_signed_test_vectors.json")))
COMM = V["commitments"]
LOGS = V["run_logs"]
ATK = Ed25519PrivateKey.generate()
COUNT = 0
FAIL: list[str] = []


def check(name, cond, detail=""):
    global COUNT
    COUNT += 1
    print(("PASS  " if cond else "FAIL  ") + name + (("  [%s]" % detail)
                                                     if detail and not cond else ""))
    if not cond:
        FAIL.append(name)


def raises(fn, exc=G.RouteInputError):
    try:
        fn()
        return False
    except exc:
        return True


def cid_for(key):
    for cid, c in COMM.items():
        comp = c.get("commitment", {}).get("component") or \
            c.get("pre_run", {}).get("component")
        if comp == key:
            return cid


def raw(key, d, n, viol=0, cid=None, recon=None):
    e = G.MANIFEST_BY_KEY[key]
    s = G.BY_KEY[key]
    r = {s.denominator_field: d, s.numerator_field: n,
         "manifest_sha256": G.MANIFEST_SHA256, "universe_id": e.universe_id}
    if s.violation_field:
        r[s.violation_field] = viol
    if e.kind in (G.KIND_SEALED, G.KIND_REALIZED):
        r["commitment_id"] = cid or cid_for(key)
    if recon is not None:
        r["reconciliation"] = recon
    return r


def good():
    full = {**V["sealed_n"], **V["realized_n"]}
    ev = {"R2-A": raw("R2-A", 16, 16), "R4-C": raw("R4-C", 216, 216),
          "R6-A": raw("R6-A", 60, 60), "R3-A": raw("R3-A", 12, 12)}
    for k, n in full.items():
        ev[k] = raw(k, n, n)
    return ev


def claims(ev, comm=None, logs=None):
    return G.route_claims(ev, comm if comm is not None else COMM,
                          logs if logs is not None else LOGS)


# ---------------------------------------------------------------- positive
def t_positive():
    out = claims(good())
    check("P1 full authentic corpus is all SUPPORTED-DESCRIPTIVE",
          set(v["claim"] for v in out["routes"].values()) == {"SUPPORTED-DESCRIPTIVE"},
          str({k: v["claim"] for k, v in out["routes"].items()}))
    check("P2 result reports all three frozen authorities",
          out["authorities"] == {"commitment_authority_pubkey": G.COMMITMENT_AUTHORITY_PUBKEY,
                                  "run_logger_pubkey": G.RUN_LOGGER_PUBKEY,
                                  "prerun_anchor_pubkey": G.PRERUN_ANCHOR_PUBKEY})
    check("P3 no inference produced", out["inference"].startswith("NONE"))
    check("P4 shipped vectors bind this manifest and these keys",
          V["manifest_sha256"] == G.MANIFEST_SHA256
          and V["public_keys"]["commitment"] == G.COMMITMENT_AUTHORITY_PUBKEY)
    ev = good()
    ev["R5-A"] = raw("R5-A", 24, 24, recon={"universe_n": 25, "excluded":
                     [{"count": 1, "reason": "one descendant not yet corrected"}]})
    check("P5 authentic reconciled 24-of-25 (0.96>=0.95) still SUPPORTED",
          claims(ev)["routes"]["R5"]["claim"] == "SUPPORTED-DESCRIPTIVE")


# ----------------------------------------------- F-P7-1 no caller trust root
def t_fp71():
    sig = inspect.signature(G.route_claims)
    check("A1 route_claims exposes no trust-root parameter",
          list(sig.parameters) == ["raw_evidence", "commitments", "run_logs"])
    check("A2 passing a trusted_pubkey raises TypeError",
          raises(lambda: G.route_claims(good(), COMM, LOGS, trusted_pubkey="00" * 32),
                 TypeError))
    check("A3 trust roots absent from any override path (not in code interface)",
          "trusted_pubkey" not in inspect.getsource(G.route_claims))
    canon = G._manifest_canonical()
    check("A4 manifest binds all three authority keys",
          all(k in canon for k in (G.COMMITMENT_AUTHORITY_PUBKEY, G.RUN_LOGGER_PUBKEY,
                                   G.PRERUN_ANCHOR_PUBKEY)))
    # attacker signs a favorable sealed subset (20) with its own key + own anchor
    key = "R5-A"
    e = G.MANIFEST_BY_KEY[key]
    c = {"kind": G.KIND_SEALED, "commitment_id": "atk", "protocol_version": G.PROTOCOL_VERSION,
         "manifest_sha256": G.MANIFEST_SHA256, "component": key, "universe_id": e.universe_id,
         "sealed_universe_n": 20, "sealed_universe_inventory_hash": "a" * 64,
         "authority": "attacker", "commitment_sequence": 1, "committed_at": "2026-07-26T10:00:00Z"}
    c["signature"] = ATK.sign(G.sealed_commitment_payload(c)).hex()
    cd = hashlib.sha256(G.sealed_commitment_payload(c)).hexdigest()
    a = {"anchor_id": "atk-a", "commitment_id": "atk", "sealed_commitment_sha256": cd,
         "manifest_sha256": G.MANIFEST_SHA256, "anchor_sequence": 1,
         "anchored_at": "2026-07-26T10:05:00Z", "authority": "attacker"}
    a["signature"] = ATK.sign(G.sealed_anchor_payload(a)).hex()
    bundle = {"kind": G.KIND_SEALED, "commitment_id": "atk", "commitment": c, "anchor": a}
    check("A5 attacker-signed sealed subset (own commitment+own anchor) rejected",
          raises(lambda: claims({key: raw(key, 20, 20, cid="atk")}, {"atk": bundle}, LOGS)))
    check("A6 attacker public key is absent from the manifest",
          ATK.public_key().public_bytes_raw().hex() not in canon)


# ---------------------------------- DIVERGENCE 1: sealed independent anchor
def t_sealed_anchor():
    key = "R5-A"
    cid = cid_for(key)
    # (1) valid commitment, but strip the anchor -> field-set mismatch, rejected
    no_anchor = {"kind": G.KIND_SEALED, "commitment_id": cid,
                 "commitment": COMM[cid]["commitment"]}
    check("S1 sealed bundle with no independent anchor is rejected",
          raises(lambda: claims({key: raw(key, 25, 25, cid=cid)}, {**COMM, cid: no_anchor}, LOGS)))
    # (2) genuine commitment, anchor re-signed by attacker key -> rejected
    t = copy.deepcopy(COMM[cid])
    t["anchor"]["signature"] = ATK.sign(G.sealed_anchor_payload(t["anchor"])).hex()
    check("S2 sealed anchor signed by a non-anchor key is rejected (lone authority "
          "cannot self-declare a sealed universe)",
          raises(lambda: claims({key: raw(key, 25, 25, cid=cid)}, {**COMM, cid: t}, LOGS)))
    # (3) anchor binds the wrong sealed-commitment digest -> rejected
    t2 = copy.deepcopy(COMM[cid])
    t2["anchor"]["sealed_commitment_sha256"] = "f" * 64
    t2["anchor"]["signature"] = None  # will fail sig anyway; also digest mismatch
    check("S3 sealed anchor over a wrong commitment digest is rejected",
          raises(lambda: claims({key: raw(key, 25, 25, cid=cid)}, {**COMM, cid: t2}, LOGS)))
    # (4) tamper the sealed cardinality after signing -> commitment sig breaks
    t3 = copy.deepcopy(COMM[cid])
    t3["commitment"]["sealed_universe_n"] = 20
    check("S4 tampering sealed_universe_n after signing breaks the commitment signature",
          raises(lambda: claims({key: raw(key, 20, 20, cid=cid)}, {**COMM, cid: t3}, LOGS)))
    # (5) genuine full sealed universe still authenticates and passes
    check("S5 the genuine anchored sealed universe still authenticates and passes",
          claims({key: raw(key, 25, 25, cid=cid)})["routes"]["R5"]["claim"] in
          ("SUPPORTED-DESCRIPTIVE", "INCOMPLETE"))  # R5 also needs R5-C; INCOMPLETE ok here


# ------------------------------------------- F-P7-2 realized append history
def t_fp72():
    key = "R2-B"
    cid = cid_for(key)
    total = COMM[cid]["close"]["realized_total"]
    # (1) attacker re-signs the independent anchor -> rejected
    t = copy.deepcopy(COMM[cid])
    t["anchor"]["signature"] = ATK.sign(G.pre_run_anchor_payload(t["anchor"])).hex()
    check("B1 realized independent anchor signed by a non-anchor key is rejected",
          raises(lambda: claims({key: raw(key, total, total, cid=cid)}, {**COMM, cid: t}, LOGS)))
    # (2) truncate the append log
    tl = dict(LOGS)
    tl[cid] = LOGS[cid][:-1]
    check("B2 truncated append history is rejected",
          raises(lambda: claims({key: raw(key, total, total, cid=cid)}, COMM, tl)))
    # (3) reorder
    ro = list(LOGS[cid])
    ro[0], ro[1] = ro[1], ro[0]
    tl2 = dict(LOGS)
    tl2[cid] = ro
    check("B3 reordered append history is rejected",
          raises(lambda: claims({key: raw(key, total, total, cid=cid)}, COMM, tl2)))
    # (4) modify an event payload after signing -> event sig / chain breaks
    md = copy.deepcopy(LOGS[cid])
    md[3]["event"] = {"idx": 4, "qualifying": False, "tampered": True}
    tl3 = dict(LOGS)
    tl3[cid] = md
    check("B4 an event modified after signing is rejected",
          raises(lambda: claims({key: raw(key, total, total, cid=cid)}, COMM, tl3)))
    # (5) attacker forges a whole post-hoc realized bundle with own keys
    e = G.MANIFEST_BY_KEY[key]
    run_id = "posthoc"
    pre = {"commitment_id": "atkR", "protocol_version": G.PROTOCOL_VERSION,
           "manifest_sha256": G.MANIFEST_SHA256, "component": key,
           "universe_id": e.universe_id, "run_id": run_id,
           "event_schema_sha256": "a" * 64, "inclusion_rule_sha256": "b" * 64,
           "logger_pubkey": G.RUN_LOGGER_PUBKEY, "authority": "attacker",
           "commitment_sequence": 1, "committed_at": "2026-07-26T10:00:00Z"}
    pre["genesis_hash"] = G.expected_run_genesis(pre)
    pre["signature"] = ATK.sign(G.pre_run_commitment_payload(pre)).hex()
    check("B5 a post-hoc realized bundle signed by a non-authority is rejected",
          raises(lambda: G.verify_realized_commitment(
              key, e, {"kind": G.KIND_REALIZED, "commitment_id": "atkR", "pre_run": pre,
                       "anchor": {}, "close": {}}, [], "atkR")))
    # (6) genuine realized still authenticates
    check("B6 the genuine anchored realized universe authenticates",
          claims({key: raw(key, total, total, cid=cid), "R2-A": raw("R2-A", 16, 16)}
                 )["routes"]["R2"]["claim"] == "SUPPORTED-DESCRIPTIVE")


# ----------------------------------------------- F-P7-3 commitment_id
def t_fp73():
    key = "R5-A"
    check("C1 unknown commitment_id is rejected",
          raises(lambda: claims({key: raw(key, 25, 25, cid="no-such-id")})))
    # cross-component: use R5-C's commitment for R5-A
    other = cid_for("R5-C")
    check("C2 a commitment resolved for another component is rejected",
          raises(lambda: claims({key: raw(key, 25, 25, cid=other)},
                                {**COMM, other: COMM[other]}, LOGS)))
    check("C3 a smuggled authority field in the raw record is rejected",
          raises(lambda: claims({key: {**raw(key, 25, 25, cid=cid_for(key)),
                                       "sealed_universe_n": 20}})))
    check("C4 a smuggled signature field in the raw record is rejected",
          raises(lambda: claims({key: {**raw(key, 25, 25, cid=cid_for(key)),
                                       "signature": "x"}})))


# -------------------------------------------------- carried v0.7 closures
def t_carried():
    ev = good()
    ev["R4-C"] = raw("R4-C", 30, 30)
    check("D1 R4-C 30 of fixed 216 with no reconciliation is rejected",
          raises(lambda: claims(ev)))
    ev["R4-C"] = raw("R4-C", 30, 30, recon={"universe_n": 216, "excluded":
                     [{"count": 186, "reason": "not run"}]})
    comp = claims(ev)["components"]["R4-C"]
    check("D2 reconciled R4-C 30/216 scores over 216 and does not pass",
          comp["denominator"] == 216 and comp["numerator"] == 30 and not comp["gate_pass"])
    ev = good()
    del ev["R2-B"]
    r2 = claims(ev)["routes"]["R2"]
    check("D3 deleting committed R2-B yields INCOMPLETE, not OUT OF SCOPE",
          r2["claim"] == "INCOMPLETE" and "R2-B" in r2["missing_committed"])
    ev = good()
    del ev["R3-A"]
    check("D4 R3-A absent is validly OUT OF SCOPE",
          claims(ev)["routes"]["R3"]["claim"] == "OUT OF SCOPE")
    ev = good()
    ev["R5-A"] = raw("R5-A", 25, 25, viol=1)
    check("D5 a silent_overwrite violation FAILS R5 despite a perfect share",
          claims(ev)["routes"]["R5"]["claim"] == "FAILED")
    ev = good()
    ev["R6-A"] = {**raw("R6-A", 60, 60), "manifest_sha256": "0" * 64}
    check("D6 a raw record bound to the wrong manifest digest is rejected",
          raises(lambda: claims(ev)))
    check("D7 manifest digest reproducible",
          G.MANIFEST_SHA256 == hashlib.sha256(G._manifest_canonical().encode()).hexdigest())
    check("D8 unknown component key rejected",
          raises(lambda: claims({**good(), "R9-Z": {"a": 1}})))
    check("D9 a fabricated GateResult is rejected as evidence",
          raises(lambda: claims({**good(), "R2-A": G.GateResult(
              "R2-A", "R2", "A", "G", 16, 16, 0, 1.0, 16, 0.75, True, True, False, 16,
              (), "x", "x")})))


def main():
    t_positive()
    t_fp71()
    t_sealed_anchor()
    t_fp72()
    t_fp73()
    t_carried()
    print("\n%d checks, %d failures" % (COUNT, len(FAIL)))
    for n in FAIL:
        print("  FAILED:", n)
    raise SystemExit(1 if FAIL else 0)


if __name__ == "__main__":
    main()

---

# Bismillah ir-Rahman ir-Rahim
