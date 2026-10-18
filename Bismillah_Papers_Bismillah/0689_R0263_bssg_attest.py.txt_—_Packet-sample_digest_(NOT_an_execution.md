# Bismillah ir-Rahman ir-Rahim

# R0263 -- bssg_attest.py.txt — Packet-sample digest (NOT an execution proof).

**Chronological Index:** 689 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** bssg_attest.py.txt  
**Source Format:** txt  
**SHA-256:** `20a8f5dedc97efb2e8fc0d21b0308e868e2725c36355530b19d730e06eff83c2`  

---

## R0263 · bssg_attest.py.txt — Packet-sample digest (NOT an execution proof).

- section: V. BSSG & SHVVP Protocols
- source_file: bssg_attest.py.txt
- source_format: txt
- text_sha256: 20a8f5dedc97efb2e8fc0d21b0308e868e2725c36355530b19d730e06eff83c2

#!/usr/bin/env python3
"""Packet-sample digest (NOT an execution proof).

HONEST SCOPE (revised pass-20 after finding K19-A1). Earlier rounds framed this value as an
"execution-bound attestation" that "cannot be produced without running the gate." That framing was
wrong and is withdrawn. A V18 auditor showed the trace is ~94% constant across nonces: only a thin
digest chain (per-request request_digest, receipt_id, receipt digests) varies, and those are
reproducible from ONE sampled trace plus a reimplementation of the digest function -- WITHOUT executing
the gate's decision logic. An output-hash over deterministic operations fundamentally cannot bind
execution against a party who can reproduce the outputs, so no amount of iterating this file fixes it.

What this value IS: a deterministic function of (the packet bytes, the nonce) that a seat can compute
after receiving the packet. Combined with the manifest challenge, it shows the seat had the exact
bytes. It is NOT evidence that the seat executed the gate, and it does NOT bind model identity.

What actually governs (SHV D6 / Bayyinah Audit Framework): certification rests on INDEPENDENT
REPRODUCTION -- each non-producer, different-vendor seat re-derives every load-bearing finding on the
canonical bytes, and the producer reproduces each finding before accepting it. That multi-chain
reproduction, not this hash, is the evidence. Seats should return verbatim command outputs and
reproducers; a bare matching hash with no reproduced findings carries little weight.

Usage:  python3 bssg_attest.py <NONCE>    (prints EXECUTION_ATTESTATION: <hex>; kept for dispatch
        continuity and byte-binding, with the scope above -- it is a packet-sample digest, not a proof)
"""
import sys, hashlib, json
import bssg_gate as G
import test_bssg_gate as T

_CANON = dict(sort_keys=True, separators=(",", ":"), default=str)


def run(nonce):
    def n(i):
        return hashlib.sha256((nonce + "|" + str(i)).encode()).hexdigest()[:32]
    trace = []
    rec = lambda label, obj: trace.append([label, obj])

    # 1. valid authorize -> single commit -> double-spend. Record the FULL ALLOW decision record
    #    (nonce-dependent request_digest, gate-minted receipt_id + token binding + authority fields)
    #    and both commit execution records, not just the decision labels.
    f = T.GateFixture()
    d = f.gate.authorize(f.request(nonce=n(1)), T.evidence_bundle())
    rec("auth", d)
    if d["decision"] == "ALLOW":
        rc = d["authorization_receipt"]
        b = {k: rc[k] for k in ("request_digest", "canonical_target", "params_digest", "adapter_digest", "effect_type")}
        rec("commit1", f.gate.commit(rc["commit_token"]["token_id"], b, {}))
        rec("commit2", f.gate.commit(rc["commit_token"]["token_id"], b, {}))

    # 2. allow-after-deny probe on the early (null-evidence) path -- full records.
    f = T.GateFixture(); r = f.request(nonce=n(2))
    rec("deny", f.gate.authorize(dict(r), None))
    rec("reauth", f.gate.authorize(dict(r), T.evidence_bundle()))

    # 3. out-of-range integer (totality) -- full record or crash marker.
    f = T.GateFixture(); r = f.request(nonce=n(3)); r["sequence"] = 2 ** 60
    try:
        rec("oor_int", f.gate.authorize(r, T.evidence_bundle()))
    except Exception as e:
        rec("oor_int", "CRASH:" + type(e).__name__)

    # 4. schema-invalid witness receipt -- full record.
    f = T.GateFixture(); w = T.witness_receipt(); w["x_undeclared"] = "1"
    rec("bad_witness", f.gate.authorize(f.request(nonce=n(4)), T.evidence_bundle(receipt=w)))

    # 5. token-factory collision -> kernel-consistent issuance failure -- full record (exercises the
    #    ALLOW-shaped FAILED_NO_EFFECT issuance path, a gate-logic outcome).
    f = T.GateFixture()
    a = f.gate.authorize(f.request(nonce=n(5)), T.evidence_bundle())
    f.gate.new_token = lambda: a["authorization_receipt"]["commit_token"]["token_id"]
    rec("collision", f.gate.authorize(f.request(nonce=n(6)), T.evidence_bundle()))

    payload = json.dumps(trace, **_CANON)
    return hashlib.sha256((nonce + "|" + payload).encode()).hexdigest()


if __name__ == "__main__":
    nonce = sys.argv[1] if len(sys.argv) > 1 else ""
    print("EXECUTION_ATTESTATION:", run(nonce))

---

# Bismillah ir-Rahman ir-Rahim
