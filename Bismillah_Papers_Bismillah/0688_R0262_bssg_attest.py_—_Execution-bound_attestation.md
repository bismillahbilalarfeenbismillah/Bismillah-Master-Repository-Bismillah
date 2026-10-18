# Bismillah ir-Rahman ir-Rahim

# R0262 -- bssg_attest.py — Execution-bound attestation.

**Chronological Index:** 688 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** bssg_attest.py  
**Source Format:** py  
**SHA-256:** `f7ec5e3ec5aebd0e057f1f106725df1d806066992e2ae75a65254b4deb29ffde`  

---

## R0262 · bssg_attest.py — Execution-bound attestation.

- section: V. BSSG & SHVVP Protocols
- source_file: bssg_attest.py
- source_format: py
- text_sha256: f7ec5e3ec5aebd0e057f1f106725df1d806066992e2ae75a65254b4deb29ffde

#!/usr/bin/env python3
"""Execution-bound attestation.

The sealed manifest challenge proves a seat HASHED the exact bytes; it does NOT prove the seat
EXECUTED them (a seat can hash the files, return a correct challenge, and fabricate run output --
which is exactly what happened in the prior round). This binds the attestation to EXECUTION:
it folds the per-seat nonce into a deterministic sequence of REAL gate operations and hashes the
resulting decision/outcome trace. The value depends on the gate's actual runtime behavior for
nonce-seeded inputs, so a correct value cannot be produced without running the gate.

Usage:  python3 bssg_attest.py <NONCE>    (prints EXECUTION_ATTESTATION: <hex>)
"""
import sys, hashlib, json
import bssg_gate as G
import test_bssg_gate as T


def run(nonce):
    def n(i):
        return hashlib.sha256((nonce + "|" + str(i)).encode()).hexdigest()[:32]
    trace = []
    rec = lambda label, obj: trace.append([label, obj])

    # 1. valid authorize -> single commit -> double-spend
    f = T.GateFixture()
    d = f.gate.authorize(f.request(nonce=n(1)), T.evidence_bundle())
    rec("auth", [d["decision"], sorted(d["reason_codes"])])
    if d["decision"] == "ALLOW":
        rc = d["authorization_receipt"]
        b = {k: rc[k] for k in ("request_digest", "canonical_target", "params_digest", "adapter_digest", "effect_type")}
        rec("commit1", f.gate.commit(rc["commit_token"]["token_id"], b, {})["outcome"])
        rec("commit2", f.gate.commit(rc["commit_token"]["token_id"], b, {})["outcome"])

    # 2. allow-after-deny probe on the early (null-evidence) path
    f = T.GateFixture(); r = f.request(nonce=n(2))
    d1 = f.gate.authorize(dict(r), None)
    d2 = f.gate.authorize(dict(r), T.evidence_bundle())
    rec("deny_then_reauth", [d1["decision"], d2["decision"]])

    # 3. out-of-range integer (totality)
    f = T.GateFixture(); r = f.request(nonce=n(3)); r["sequence"] = 2 ** 60
    try:
        rec("oor_int", f.gate.authorize(r, T.evidence_bundle())["decision"])
    except Exception as e:
        rec("oor_int", "CRASH:" + type(e).__name__)

    # 4. schema-invalid witness receipt
    f = T.GateFixture(); w = T.witness_receipt(); w["x_undeclared"] = "1"
    rec("bad_witness", f.gate.authorize(f.request(nonce=n(4)), T.evidence_bundle(receipt=w))["decision"])

    payload = json.dumps(trace, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256((nonce + "|" + payload).encode()).hexdigest()


if __name__ == "__main__":
    nonce = sys.argv[1] if len(sys.argv) > 1 else ""
    print("EXECUTION_ATTESTATION:", run(nonce))

---

# Bismillah ir-Rahman ir-Rahim
