# Bismillah ir-Rahman ir-Rahim

# R0566 -- XZ Protocol v0.46 -- Quantum Orbital Convergence Audit Round 5

**Chronological Index:** 464 of 995  
**Date:** 2026-08-07  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** AUDIT_PROMPT_v46_COMMON.md.txt  
**Source Format:** txt  
**SHA-256:** `2d460a2fa0721f4840a13ffb6d24db06d09c1ddaa7da3c00237714ce2c8b22dc`  

---

## R0566 · XZ Protocol v0.46 -- Quantum Orbital Convergence Audit Round 5

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: AUDIT_PROMPT_v46_COMMON.md.txt
- source_format: txt
- text_sha256: 2d460a2fa0721f4840a13ffb6d24db06d09c1ddaa7da3c00237714ce2c8b22dc

# XZ Protocol v0.46 -- Quantum Orbital Convergence Audit Round 5
## Common Audit Prompt (all seats)

**Dispatch date:** 2026-08-07
**Artifact under audit:** XZ Protocol v0.46 DRAFT CANDIDATE
**Packet digest:** PACKET_SHA256SUMS = `0c5f7264f77db9054b03627c37d45d9153df9e195c97f1981a4d1a78d4a8a431`
**Protocol text digest:** `c4e78d67830e81f29cf9a9073cf4c3e41708aff1ffc4faf10bff472340b49dcf` (288,839 bytes, 1,214 lines)
**Packet members:** 16 (listed in PACKET_SHA256SUMS) + PACKET_SHA256SUMS itself = 17 shipped files

---

## Context

The XZ Protocol is a preregistered structural decision replay of the XZ Utils supply-chain compromise (CVE-2024-3094). It ships as a sealed packet: one Markdown document, 12 Python files (6 code modules + 6 test suites), one JSON trust-roots manifest, one build verifier, one history digest, and one SHA256 checksum manifest.

**Convergence trajectory across four prior rounds:**

| Round | Version | Seats | Result |
|---|---|---|---|
| R1 | v0.42 | 4 | 3 HALT / 1 CONDITIONAL PASS |
| R2 | v0.43 | 8 | 8 HALT / 0 non-HALT |
| R3 | v0.44 | 12 | 10 HALT / 2 CONDITIONAL PASS |
| R4 | v0.45 | 4 | 4 HALT / 0 non-HALT |
| **R5** | **v0.46** | **This round** | **?** |

All 5 v0.45 repairs were verified TRUE on bytes by every R4 seat -- the second consecutive fully-landed repair round. All four R4 seats HALTed (carrying seat Kimi K3 HALTed binding). Two convergent Class A Axiom-3 narration errors drove the HALT: (a) "initial non-HALTs across three rounds" was false against the sealed v0.43 entry (4-seat convergence); (b) the verdict tally 10+2=12 was irreconcilable with the Seat-3 exclusion reducing available verdicts to 11 (3-seat convergence).

**v0.46 addresses the R4 findings with 3 corrections and 5 body repairs:**

1. **(av)** "Initial non-HALTs" claim corrected -- 4-seat convergence.
2. **(aw)** Verdict tally reconciled: 12 deployed, 11 executing, 9 HALT / 2 CONDITIONAL PASS. Front-matter corrected. 3-seat convergence.
3. **(ax)** Malformed F-S644-07 corrected to F-S6-44-07 -- 2-seat convergence.
4. **Body [a-e]:** front-matter status, Section 22.2 coverage to v0.45, Section 22.3 carry lineage to v0.38-v0.46, FB-7b PENDING RE-CARRY to v0.46, standing boundaries 25 to 27 (added F-V44-01 prohibited-content 4-module limitation and [9d] synonym/bare-cardinal evasion).

**10-item register** dispositioning all R4 findings. 5 single-seat findings NOTED (not repaired).

---

## Your audit task

You are an independent auditor executing a seat in a multi-model convergence audit.

### 1. Verify packet integrity

Run `sha256sum -c PACKET_SHA256SUMS` (rc=0, 16/16). Run `python3 build.py` (must print `BUILD PASSED: all checks GREEN`). If either fails, HALT immediately.

### 2. Verify all 3 declared v0.46 corrections against bytes

For each correction (av, aw, ax), verify the claim is TRUE on the shipped bytes. State what you ran and what you found.

### 3. Verify body repairs [a]-[e]

Confirm each body repair landed: front-matter status, Section 22.2 range = "v0.1 through v0.45", Section 22.3 lineage = "v0.38-v0.46", FB-7b = "PENDING RE-CARRY v0.46", standing boundaries = 27.

### 4. Verify standing properties

- Code partition: 6 CODE_MODULES + 6 TEST_SUITES
- Test count: 186 passed
- PRIOR_HISTORY chain value
- v0.46 stamps on all 12 code files + trust roots
- Seal chain integrity (46 entries + FULL_SECTION_27)
- Standing boundaries: 27 declared
- EXTERNAL count: 1
- Register: 10 declared items
- Append-only: v0.1-v0.45 entries byte-identical to v0.45 shipped bytes

### 5. Probe the v0.46 entry for new Axiom-3 errors

The dominant failure mode across five rounds: the producer narrates counts, IDs, and ranges from memory. Every O-CLAIM in the v0.46 entry must be verified against bytes. Specifically check:
- Seat count, family count, shell count
- Verdict tally and convergence counts
- Finding IDs in the register (all 10 items)
- Correction letters and their claimed substances
- Standing boundary count and completeness
- The register count itself (10 declared vs parsed)

### 6. Issue verdict

- **HALT** -- Class A finding(s) exist.
- **CONDITIONAL PASS** -- no Class A. Class C/D/E may exist.
- **PASS** -- no findings.

Carrying seats (Kimi K3): HALT is binding.
Advisory seats (Opus 5 / Claude): HALT is advisory.
Adversarial seats (Gemini, GPT): findings carry full weight.

Use the six-element findings format (ID, severity, locus, substance, disposition, cross-reference).

### 7. Classification

| Class | Meaning | HALT? |
|---|---|---|
| A | Byte-false O-CLAIM or structural defect | Yes |
| B | Unverifiable O-CLAIM | Yes (unless DISCLOSED) |
| C | Gate limitation | No |
| D | Disclosed boundary | No |
| E | Informational | No |

---

## What NOT to do

- Do not accept the producer's narrative at face value.
- Do not count prior-round findings as your own.
- Do not soft-pedal to avoid a HALT.
- Do not use em-dash characters. Use `--` (double hyphen).

## Governance

- **FB-7b:** PENDING RE-CARRY on v0.46 bytes.
- **FB-8:** OPEN. Exit: two non-producer carrying seats from different families return non-HALT.
- **Producer:** Claude (Anthropic) -- advisory, non-carrying, non-binding.

---

# Bismillah ir-Rahman ir-Rahim
