# Bismillah ir-Rahman ir-Rahim

# R0539 -- verify_seat_evidence.py — Independently reproduce ALL seat evidence against the shipped gate AND the shipped

**Chronological Index:** 134 of 995  
**Date:** 2026  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** verify_seat_evidence.py  
**Source Format:** py  
**SHA-256:** `f1469b18e7c06c1e4e312efca256929036bfdea56fd4127da70b98e3f30a60fd`  

---

## R0539 · verify_seat_evidence.py — Independently reproduce ALL seat evidence against the shipped gate AND the shipped

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: verify_seat_evidence.py
- source_format: py
- text_sha256: f1469b18e7c06c1e4e312efca256929036bfdea56fd4127da70b98e3f30a60fd

"""Independently reproduce ALL seat evidence against the shipped gate AND the shipped
raw seat reports. Run from the release root: python3 seat_evidence/verify_seat_evidence.py
For each carrying seat this (1) reproduces, from the real gate, the six fresh-forgery
exception strings and both challenge hashes, and (2) PARSES the raw seat report files and
requires every reproduced value to appear there verbatim -- so a divergence between the
shipped report and the code is detected, not assumed. Needs the cryptography package.
Exit 0 only if all six strings and both challenges reproduce AND match the reports."""
import copy, hashlib, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT); os.chdir(ROOT)
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
import shvvp_v0_8_route_gates as G
V = json.load(open("shvvp_v0_8_signed_test_vectors.json")); COMM = V["commitments"]
ATK = Ed25519PrivateKey.generate()
def cid_for(k):
    for c, b in COMM.items():
        if (b.get("commitment", {}).get("component") or b.get("pre_run", {}).get("component")) == k:
            return c
def emsg(fn):
    try: fn(); return "NO ERROR"
    except G.RouteInputError as x: return "%s: %s" % (type(x).__name__, x)
def raw(cid, k, n=25):
    e = G.MANIFEST_BY_KEY[k]
    return {"descendants_recorded": n, "descendants_reached": n, "silent_overwrites": 0,
            "manifest_sha256": G.MANIFEST_SHA256, "universe_id": e.universe_id, "commitment_id": cid}

# ---- reproduce all six Kimi forgery strings from the real gate ----
skey = "R5-A"; scid = cid_for(skey); se = G.MANIFEST_BY_KEY[skey]
repro = {}
# 6.1 attacker-signed sealed subset (own commitment + own anchor)
c = {"kind": G.KIND_SEALED, "commitment_id": "x", "protocol_version": G.PROTOCOL_VERSION,
     "manifest_sha256": G.MANIFEST_SHA256, "component": skey, "universe_id": se.universe_id,
     "sealed_universe_n": 20, "sealed_universe_inventory_hash": "a"*64, "authority": "x",
     "commitment_sequence": 1, "committed_at": "2026-07-26T10:00:00Z"}
c["signature"] = ATK.sign(G.sealed_commitment_payload(c)).hex()
cdg = hashlib.sha256(G.sealed_commitment_payload(c)).hexdigest()
a = {"anchor_id": "x", "commitment_id": "x", "sealed_commitment_sha256": cdg,
     "manifest_sha256": G.MANIFEST_SHA256, "anchor_sequence": 1,
     "anchored_at": "2026-07-26T10:05:00Z", "authority": "x"}
a["signature"] = ATK.sign(G.sealed_anchor_payload(a)).hex()
repro["sealed_subset"] = emsg(lambda: G.route_claims({skey: raw("x", skey, 20)},
    {"x": {"kind": G.KIND_SEALED, "commitment_id": "x", "commitment": c, "anchor": a}}, {}))
# 6.2 post-outcome realized bundle (R2-B, attacker-signed pre_run)
rkey = "R2-B"; re_ = G.MANIFEST_BY_KEY[rkey]; run_id = "posthoc"
pre = {"commitment_id": "atkR", "protocol_version": G.PROTOCOL_VERSION,
       "manifest_sha256": G.MANIFEST_SHA256, "component": rkey, "universe_id": re_.universe_id,
       "run_id": run_id, "event_schema_sha256": "a"*64, "inclusion_rule_sha256": "b"*64,
       "logger_pubkey": G.RUN_LOGGER_PUBKEY, "authority": "attacker",
       "commitment_sequence": 1, "committed_at": "2026-07-26T10:00:00Z"}
pre["genesis_hash"] = G.expected_run_genesis(pre); pre["signature"] = ATK.sign(G.pre_run_commitment_payload(pre)).hex()
repro["realized_posthoc"] = emsg(lambda: G.verify_realized_commitment(
    rkey, re_, {"kind": G.KIND_REALIZED, "commitment_id": "atkR", "pre_run": pre, "anchor": {}, "close": {}}, [], "atkR"))
# 6.3 sealed-anchor family
na = {"kind": G.KIND_SEALED, "commitment_id": scid, "commitment": COMM[scid]["commitment"]}
repro["noanchor"] = emsg(lambda: G.route_claims({skey: raw(scid, skey)}, {**COMM, scid: na}, {}))
for name, mut in [("atkanchor", lambda x: x),
                  ("wrongdig", lambda x: x.__setitem__("sealed_commitment_sha256", "f"*64) or x),
                  ("predate", lambda x: x.__setitem__("anchored_at", "2026-07-26T09:00:00Z") or x)]:
    t = copy.deepcopy(COMM[scid]); mut(t["anchor"])
    t["anchor"]["signature"] = ATK.sign(G.sealed_anchor_payload(t["anchor"])).hex()
    repro[name] = emsg(lambda: G.route_claims({skey: raw(scid, skey)}, {**COMM, scid: t}, {}))

# ---- parse the shipped raw seat reports ----
kimi_txt = open(os.path.join(HERE, "SEAT_kimi_moonshot_vendor_direct.md")).read()
qwen_txt = open(os.path.join(HERE, "SEAT_qwen_alibaba_local_native.md")).read()
report_errs = set(re.findall(r"CommitmentError: [^\n]+", kimi_txt))
def challenge(nonce): return hashlib.sha256((G.MANIFEST_SHA256 + nonce).encode()).hexdigest()
def parsed_challenge(txt):
    m = re.search(r"Challenge response:\s*([0-9a-f]{64})", txt); return m.group(1) if m else None
def parsed_nonce(txt):
    m = re.search(r"nonce[^:]*:\s*(SHVVP-[A-Za-z0-9-]+)", txt); return m.group(1) if m else None

ok = True
print("=== six forgery strings: reproduced-from-code must appear verbatim in Kimi report ===")
for name, s in repro.items():
    inrep = s in report_errs
    ok = ok and inrep
    print("  %-16s %s  %s" % (name, "MATCH " if inrep else "MISSING", s))
print("  (reproduced %d/6; report lists %d CommitmentError lines)" % (len(repro), len(report_errs)))
print("=== challenge hashes: report value must equal code-reproduced value ===")
for who, txt in [("Kimi", kimi_txt), ("Qwen", qwen_txt)]:
    n = parsed_nonce(txt); rep = parsed_challenge(txt); comp = challenge(n) if n else None
    good = (n is not None and rep is not None and rep == comp)
    ok = ok and good
    print("  %-4s nonce=%s report=%s recomputed=%s %s" % (who, n, (rep or "?")[:12], (comp or "?")[:12], "MATCH" if good else "MISMATCH"))
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)

---

# Bismillah ir-Rahman ir-Rahim
