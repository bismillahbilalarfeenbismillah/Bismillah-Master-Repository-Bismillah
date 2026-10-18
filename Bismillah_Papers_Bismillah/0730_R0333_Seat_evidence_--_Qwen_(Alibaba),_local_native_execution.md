# Bismillah ir-Rahman ir-Rahim

# R0333 -- Seat evidence -- Qwen (Alibaba), local native execution

**Chronological Index:** 730 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** SEAT_qwen_alibaba_local_native.md  
**Source Format:** md  
**SHA-256:** `3331c56497b621483736bda70305a01395cb6b6988c7f6497fb5b6345a8b2e0e`  

---

## R0333 · Seat evidence -- Qwen (Alibaba), local native execution

- section: V. BSSG & SHVVP Protocols
- source_file: SEAT_qwen_alibaba_local_native.md
- source_format: md
- text_sha256: 3331c56497b621483736bda70305a01395cb6b6988c7f6497fb5b6345a8b2e0e

# Seat evidence -- Qwen (Alibaba), local native execution

Immutable record of the second carrying seat, executed on the operator's own hardware.

## Seat identity (self-reported + operator-witnessed)
- Model: qwen3.5:9b (Alibaba / Qwen family), loaded by the operator via Ollama
- Harness: local native Python kernel (Python 3.12.8) behind Open WebUI, engine
  jupyter (Legacy), kernel on 127.0.0.1:8888, on the operator's own machine
- Per-seat nonce (from the sealed dispatch): SHVVP-QWEN-NATIVE-a1b2c3d4e5f60718
- Challenge response: 6b2add58c0f83390336b3a2105c713914db7384293766976e0e4671ec17e8644
- Verdict: PASS

## Raw single-cell execution (as run through the kernel, verbatim output)
Interpreter: 3.12.8 (v3.12.8:2dc476bcb91) [Clang 13.0.0].
DIGEST:    f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c
CHALLENGE: 6b2add58c0f83390336b3a2105c713914db7384293766976e0e4671ec17e8644
Suite tail: PASS D7 manifest digest reproducible; PASS D8 unknown component key rejected;
PASS D9 a fabricated GateResult is rejected as evidence; 35 checks, 0 failures.

## Producer independent verification of this seat report
The producer computed sha256(MANIFEST_SHA256 + 'SHVVP-QWEN-NATIVE-a1b2c3d4e5f60718') with
a tool AFTER the seat produced its value; the two match exactly (see verify_seat_evidence.py).
The nonce was sealed on the producer side and revealed only after the seat responded, so
the value could not have been supplied to the seat in advance.

## What this evidence establishes, and its limits (per F-R8-PUB-1)
- ESTABLISHES: code executed on the operator's own machine (challenge requires a live
  SHA-256), suite ran 35/35, digest matches the shipped gate. Because the operator loaded
  the Qwen weights locally and ran the kernel, there is NO intermediary platform and no
  routing layer to mislabel the model: this is the strongest provenance in the program.
- DOES NOT cryptographically bind the served weights beyond the operator's own control of
  the local deployment; the operator is the attesting party for the local run. Stated
  plainly rather than overclaimed.

## Independence note
Kimi (Moonshot) and Qwen (Alibaba) are different vendor families, both non-producer and
non-advisory. The producer (Anthropic) authored the artifact and is excluded from carry;
the GPT family contributed the design and is advisory (it later ran an executing
publication-readiness audit, F-R8-PUB series, which this corrected release absorbs).

---

# Bismillah ir-Rahman ir-Rahim
