# Bismillah ir-Rahman ir-Rahim

# R0332 -- Seat evidence -- Kimi (Moonshot AI), vendor-direct execution

**Chronological Index:** 69 of 995  
**Date:** 2024-12-11  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** SEAT_kimi_moonshot_vendor_direct.md  
**Source Format:** md  
**SHA-256:** `b6cf0a6c750feb7656442dd85656597bb66df937d3514e934689c49db2e0d5ea`  

---

## R0332 · Seat evidence -- Kimi (Moonshot AI), vendor-direct execution

- section: V. BSSG & SHVVP Protocols
- source_file: SEAT_kimi_moonshot_vendor_direct.md
- source_format: md
- text_sha256: b6cf0a6c750feb7656442dd85656597bb66df937d3514e934689c49db2e0d5ea

# Seat evidence -- Kimi (Moonshot AI), vendor-direct execution

Immutable record of the carrying seat's raw report, shipped so the carry is
independently auditable from the packet rather than from the producer's summary.

## Seat identity (self-reported by the seat)
- Model: Kimi (Moonshot AI)
- Vendor family: Moonshot AI
- Site/endpoint: kimi.moonshot.cn, under operator login
- Harness: Python 3.11.11 (/opt/conda/bin/python3), Linux-5.15.0-131-generic-x86_64, glibc 2.31
- Per-seat nonce (from the sealed dispatch): SHVVP-RECONFIRM-kimi-e7adeccb7dc1c3f3
- Challenge response: 8742263b6e481ac0b45a5f26d17a67df964a42ed89c70f3f5af9cd7a350fccc3
- Verdict: PASS, no F-P8 findings.

## Raw report as returned by the seat (verbatim)
Interpreter: 3.11.11 (main, Dec 11 2024, 16:28:39) [GCC 11.2.0]; /opt/conda/bin/python3;
Linux-5.15.0-131-generic-x86_64-with-glibc2.31.

File SHA-256 (seat-computed):
- shvvp_v0_8_route_gates.py:           f73af0142380462b0e465382cd3f387c0a46be1c71d3f41a97c59c495304e0f6
- shvvp_v0_8_signed_test_vectors.json: cb9434176554c12a46820a146c7af214efeb2f26f30f02616aede317f3814926
- test_shvvp_v0_8_rules.py:            a2a83722515b13acdd83f118c2b4f5f06678bcc9521d6d526a7509dacc80f6c6

Manifest digest (seat-computed): f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c
Suite: 35 checks, 0 failures (full P/A/S/B/C/D battery, all PASS).

Fresh-key forgery exceptions (seat-reported, verbatim):
- attacker-signed SEALED subset (own commitment + own anchor):
  CommitmentError: sealed bundle for R5-A commitment: signature does not verify against the frozen trust root
- post-outcome REALIZED bundle:
  CommitmentError: realized bundle for R2-B pre_run: signature does not verify against the frozen trust root
- sealed, no anchor:
  CommitmentError: sealed bundle for R5-A: field set mismatch (extra=[] missing=['anchor'])
- sealed, attacker-signed anchor:
  CommitmentError: sealed bundle for R5-A anchor: signature does not verify against the frozen trust root
- sealed, anchor over wrong commitment digest:
  CommitmentError: sealed bundle for R5-A: anchor does not bind the verified sealed commitment
- sealed, anchor predating the commitment:
  CommitmentError: sealed bundle for R5-A: anchor predates the sealed commitment

## Producer independent verification of this seat report
The producer regenerated the same six forgeries with fresh attacker keys against the
shipped gate and obtained byte-identical exception strings to those the seat reported
(see verify_seat_evidence.py in this directory; run it to reproduce). These strings are
specific to the gate's internal control flow for these exact crafted inputs and cannot be
produced without executing the real module.

## What this evidence establishes, and its limits (per F-R8-PUB-1)
- ESTABLISHES: code was executed (the challenge hash requires a live SHA-256), and the
  executed code was THIS gate (the six verbatim exception strings match the shipped gate's
  control flow for these inputs), against files whose seat-computed SHA-256 match the
  shipped bytes.
- DOES NOT cryptographically establish, from this artifact alone: the served model
  weights, or that the endpoint is exclusively Moonshot's. Model/family identity here rests
  on the operator-controlled vendor-direct endpoint (the operator ran this on
  kimi.moonshot.cn under their own login), which is a strong but attestation-level, not
  substrate-level, guarantee. This limit is stated plainly rather than overclaimed.

---

# Bismillah ir-Rahman ir-Rahim
