# Bismillah ir-Rahman ir-Rahim

# R0567 -- XZ Protocol v0.47 -- Convergence Round 6

**Chronological Index:** 824 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** AUDIT_PROMPT_v47_COMMON.md.txt  
**Source Format:** txt  
**SHA-256:** `31a70780eac3eb652cf72f1fc636b7bd248b09e52ddcf44e70c77e48825003ed`  

---

## R0567 · XZ Protocol v0.47 -- Convergence Round 6

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: AUDIT_PROMPT_v47_COMMON.md.txt
- source_format: txt
- merged_variants: 1 (DISPATCH_S02.md.txt)
- text_sha256: 31a70780eac3eb652cf72f1fc636b7bd248b09e52ddcf44e70c77e48825003ed

# XZ Protocol v0.47 -- Convergence Round 6
## Common Audit Prompt

**Artifact:** XZ Protocol v0.47 DRAFT CANDIDATE
**Packet digest:** PACKET_SHA256SUMS = `0c5f7264...` (verify from shipped bytes)
**Protocol text:** 294,529 bytes, 1,223 lines, 17 shipped files

**Convergence trajectory:**

| Round | Version | Seats | Result |
|---|---|---|---|
| R1 | v0.42 | 4 | 3H / 1CP |
| R2 | v0.43 | 8 | 8H / 0 |
| R3 | v0.44 | 12 | 10H / 2CP |
| R4 | v0.45 | 4 | 4H / 0 |
| R5 | v0.46 | 8 | 7H / 1CP (first carrying non-HALT since v0.31) |
| **R6** | **v0.47** | **4** | **?** |

v0.47 addresses convergent R5 findings: build.py docstring corrected + [2d] self-version gate added (3-seat); trust-roots timestamp disposition corrected via (ay) (3-seat); R4 seat count qualified with independence status (2-seat); FB-7b rationale updated to full carrying-HALT trajectory (2-seat). 10-item register, 7 body repairs [a]-[g], 1 correction (ay), standing boundaries 27 to 29.

## Your task

1. `sha256sum -c PACKET_SHA256SUMS` (rc=0, 16/16). `python3 build.py` (BUILD PASSED).
2. Verify correction (ay) and body repairs [a]-[g] against bytes.
3. Verify standing properties (code partition, tests, seals, stamps, boundaries 29, EXTERNAL 1, register 10).
4. Probe every O-CLAIM in the v0.47 entry against bytes. The recurrent class is narrating from memory.
5. Issue verdict: HALT (Class A exists) / CONDITIONAL PASS (no Class A) / PASS (no findings).

Carrying seats: HALT is binding. Six-element findings format. No em-dash characters.

---

# Bismillah ir-Rahman ir-Rahim
