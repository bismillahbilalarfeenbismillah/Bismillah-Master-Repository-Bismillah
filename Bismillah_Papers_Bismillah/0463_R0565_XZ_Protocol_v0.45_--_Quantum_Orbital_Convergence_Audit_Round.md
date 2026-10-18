# Bismillah ir-Rahman ir-Rahim

# R0565 -- XZ Protocol v0.45 -- Quantum Orbital Convergence Audit Round 4

**Chronological Index:** 463 of 995  
**Date:** 2026-08-07  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** AUDIT_PROMPT_v45_COMMON.md.txt  
**Source Format:** txt  
**SHA-256:** `e153699e3797f3db0748e559785e64d3577ecba06855eaecda161ae9283a60e1`  

---

## R0565 · XZ Protocol v0.45 -- Quantum Orbital Convergence Audit Round 4

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: AUDIT_PROMPT_v45_COMMON.md.txt
- source_format: txt
- text_sha256: e153699e3797f3db0748e559785e64d3577ecba06855eaecda161ae9283a60e1

# XZ Protocol v0.45 -- Quantum Orbital Convergence Audit Round 4
## Common Audit Prompt (all seats)

**Dispatch date:** 2026-08-07
**Artifact under audit:** XZ Protocol v0.45 DRAFT CANDIDATE
**Packet digest:** PACKET_SHA256SUMS = `2366a4ce5e4b5396caed37d083456658623896ee7ed5f4603dfcd7ff4a5e84be`
**Protocol text digest:** `34f014b829d1da5be85aa13d1b06669c2b8bcd8a85a65163169e89293aadb20f` (283,284 bytes, 1,205 lines)
**Packet members:** 16 (listed in PACKET_SHA256SUMS) + PACKET_SHA256SUMS itself = 17 shipped files

---

## Context

The XZ Protocol is a preregistered structural decision replay of the XZ Utils supply-chain compromise (CVE-2024-3094). It is part of the Structural Honesty Validation program (AX-SH5 -> SHUDP -> SHVVP -> BSSG -> XZ Protocol). The protocol ships as a sealed packet: one Markdown document, 12 Python files (6 code modules + 6 test suites), one JSON trust-roots manifest, one build verifier, one history digest, and one SHA256 checksum manifest.

**Convergence trajectory across three prior rounds:**

| Round | Version | Seats | Architecture | Result |
|---|---|---|---|---|
| R1 | v0.42 | 4 (A/B/C/D) | Recovery build | 3 HALT / 1 CONDITIONAL PASS |
| R2 | v0.43 | 8 (S1-S8) | 4-seat repair | 8 HALT / 0 non-HALT |
| R3 | v0.44 | 12 (S1-S12) | 8-seat repair | 10 HALT / 2 CONDITIONAL PASS |
| **R4** | **v0.45** | **This round** | **12-seat repair** | **?** |

All 9 v0.44 repairs were verified TRUE on bytes by every executing seat in Round 3 -- the first fully-landed repair round. The two CONDITIONAL PASSes came from Gemini (Seats 7 and 11). All three carrying seats (Kimi K3: Seats 2, 6, 10) HALTed binding. The convergent findings from Round 3 narrowed exclusively to Axiom-3 governance narration errors in the v0.44 amendment entry's own prose (wrong counts, stale ranges, miscited finding IDs).

**v0.45 addresses 5 convergent findings from the 12-seat v0.44 round:**

1. **EXTERNAL count: 2 -> 1** (6-seat convergence, correction (aq)). The single [EXTERNAL: ...] tag names two source categories; the tag count is 1 per the [9c] parser.
2. **Section 22.2 coverage v0.42 -> v0.44** (4-seat convergence, correction (ar) + body repair [a]). derive_prior_history() terminates at current_ver - 1.
3. **Register item(5) F-S8-43-03 -> F-S8-43-04** (3-seat convergence, correction (as)). The FB-7b finding is F-S8-43-04, not F-S8-43-03.
4. **Correction (ap) byte-false claim** (2-seat convergence, correction (at)). v0.43 had PA-A5 at 13.3.5 and PA-A12 at 13.3.3 (reversed, not identical as stated).
5. **v0.43 Class B F-S2-10 undispositioned -> DISCLOSED** (2-seat convergence, correction (au)). A-side seam disclosed as standing boundary.

Additional body repairs: [b] front-matter status updated, [c] Section 22.3 carry lineage to v0.38-v0.45, [d] FB-7b PENDING RE-CARRY to v0.45 bytes.

---

## Your audit task

You are an independent auditor executing a seat in a multi-model, multi-vendor convergence audit. Your task:

### 1. Verify packet integrity

Run `sha256sum -c PACKET_SHA256SUMS` (must return rc=0, 16/16). Run `python3 build.py` (must print `BUILD PASSED: all checks GREEN`). If either fails, HALT immediately and report the failure.

### 2. Verify all 5 declared v0.45 repairs against the shipped bytes

For each repair, verify the claim is TRUE on the shipped bytes using tool-driven checks (grep, sha256sum, python3, wc). State what you ran and what you found.

### 3. Verify standing properties

- Code file count: 6 CODE_MODULES + 6 TEST_SUITES in build.py
- Test count: 186 passed from the canonical test command
- PRIOR_HISTORY chain value: verify against HISTORY.sha256
- v0.45 stamps on all 12 code files + trust roots
- Seal chain: the v0.45 entry seal and FULL_SECTION_27 seal
- Standing boundaries count: 25 declared
- EXTERNAL count: 1 (verify with the [9c] parser or manual inspection)
- Section 22.2 coverage range matches derive_prior_history() scope

### 4. Execute your analytical framework

Apply your seat-specific analytical framework (see your seat cover note) to probe the artifact beyond the declared repairs. Look for:
- Axiom-3 violations: any O-CLAIM (narrated count, ID, range, state) in the v0.45 entry that is byte-false
- Gate coverage: any property asserted but not gated by build.py
- Cross-reference accuracy: every finding ID, correction ID, and convergence count cited in the v0.45 entry
- Standing boundary completeness: any new boundary condition not on the list of 25
- Append-only integrity: v0.1-v0.44 entries byte-identical to v0.44 shipped bytes

### 5. Issue your verdict

Use the standard vocabulary:
- **HALT** -- Class A finding(s) exist on the shipped bytes. The freeze is blocked.
- **CONDITIONAL PASS** -- no Class A findings. Class C/D/E conditions may exist.
- **PASS** -- no findings of any class.

Carrying seats (Kimi K3): your HALT is binding and blocks the freeze per FB-7b.
Advisory seats (Opus 5 / Claude): your HALT is advisory, non-binding, non-carrying.
Adversarial seats (Gemini, GPT): self-disqualified from carrying; findings carry full weight.

### 6. Format your report

Use the six-element findings format:
- **Finding ID** (e.g., F-S01-45-01 for Seat 1 finding 1 on v0.45)
- **Severity** (CRITICAL / HIGH / MEDIUM / LOW / INFORMATIONAL)
- **Locus** (exact file, section, line, or byte range)
- **Substance** (what is wrong and why; cite the bytes)
- **Disposition** (Class A through E per Section 22)
- **Cross-reference** (prior-round finding IDs if this is a recurrence)

---

## Classification taxonomy

| Class | Meaning | HALT? |
|---|---|---|
| A | Byte-false O-CLAIM or structural defect requiring repair | Yes |
| B | Claimed-false or unverifiable O-CLAIM whose truth cannot be established from shipped bytes | Yes (unless DISCLOSED) |
| C | Gate limitation -- property exists but gate does not enforce it | No |
| D | Disclosed boundary -- known limitation already on the standing-boundaries list | No |
| E | Informational observation or methodology note | No |

---

## What NOT to do

- Do not accept the producer's narrative at face value. Verify every claim against the bytes.
- Do not count findings from prior rounds as your own. Only findings you independently verify on the v0.45 shipped bytes belong in your report.
- Do not soft-pedal to avoid a HALT. If a Class A finding exists, HALT. The purpose of the audit is truth, not convergence.
- Do not use `--` (em-dash character) in your report. Use `--` (double hyphen) for em-dash effect.

---

## Governance notes

- **FB-7b status:** PENDING RE-CARRY on v0.45 bytes. Exit condition: non-HALT from carrying seats on repaired bytes.
- **FB-8 status:** OPEN. Exit condition: two non-producer carrying seats from different families return non-HALT on bytes where every prose claim in the current entry is verified.
- **Producer:** Claude (Anthropic) -- advisory only, non-carrying, non-binding.
- **The v0.44 round's 3rd Pauli violation is disclosed:** Opus 5 Seats 1/5/9 were deployed from the same continuous context. This round corrects it: the Opus 5 fresh seat is dispatched to a genuinely new conversation.

---

# Bismillah ir-Rahman ir-Rahim
