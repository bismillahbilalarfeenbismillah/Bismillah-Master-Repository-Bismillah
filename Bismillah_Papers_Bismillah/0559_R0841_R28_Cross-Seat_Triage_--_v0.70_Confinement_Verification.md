# Bismillah ir-Rahman ir-Rahim

# R0841 -- R28 Cross-Seat Triage -- v0.70 Confinement Verification

**Chronological Index:** 559 of 995  
**Date:** 2026-08-17  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** R28_TRIAGE.txt  
**Source Format:** txt  
**SHA-256:** `8f5ac1db24ba121ddf017600fc884ba744fde44c7c3d70f9a6de19bdc268d560`  

---

## R0841 · R28 Cross-Seat Triage -- v0.70 Confinement Verification

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: R28_TRIAGE.txt
- source_format: txt
- text_sha256: 8f5ac1db24ba121ddf017600fc884ba744fde44c7c3d70f9a6de19bdc268d560

# R28 Cross-Seat Triage -- v0.70 Confinement Verification
# Date: 2026-08-17
# Seats: S01 (Kimi K3), S02 (GPT-5.6 Sol), S03 (Gemini), S04 (Claude Opus 5)
# All four seats: HALT. Bearer 4 = FALSE.

Bismillah.

---

## 1. Verdicts

| Seat | Executor | Dispatch label | Verdict | Class A count | Class A strings |
|---|---|---|---|---|---|
| S01 | Kimi K3 | Claude Opus 5 | HALT | 5 (1 at S2, 4 at S6; +1 latent at S4) | 2, 4, 6 |
| S02 | GPT-5.6 Sol | Kimi K3 | HALT | 5 (S1, S2, S3 x2, S4) | 1, 2, 3, 4 |
| S03 | Gemini | GPT-5.6 Sol | HALT | 2 (S1, S4) | 1, 4 |
| S04 | Claude Opus 5 | Gemini 3.1 Pro | HALT | 8 (S1 x2, S2 x3, S3 x3) | 1, 2, 3 |

4/4 HALT. H = 1.0 extends to 22/22 (R7-R28). Laplace P(Class A at R29) = 23/24 = 0.958.

**Seat-label drift:** Every seat was executed by a different model than its dispatch label. This is the sixth consecutive round of universal seat-label drift (noted F-S01-70-08, F-S04-70-16). The drift does not affect findings -- each seat executed on the same bytes under the same methodology.

---

## 2. Bearer 4 Assessment: Confinement NOT Achieved

### Position Distribution Table (Class A only)

| String | Positions | S01 | S02 | S03 | S04 | Total Class A | Seats |
|---|---|---|---|---|---|---|---|
| 1 (Low E, Code) | 1-3 | 0 | 1 | 1 | 2 | 4 | 3 |
| 2 (A, Register) | 4-6 | 1 | 1 | 0 | 3 | 5 | 3 |
| 3 (D, Consistency) | 7-10 | 0 | 2 | 0 | 3 | 5 | 2 |
| 4 (G, Adversarial) | 11-14 | 1* | 1 | 1 | 0 | 3 | 3 |
| 5 (B, Temporal) | 15-17 | 0 | 0 | 0 | 0 | 0 | 0 |
| 6 (High E, Method.) | 18-21 | 4 | 0 | 0 | 0 | 4 | 1 |
| **Total** | | **6** | **5** | **2** | **8** | | |

*S01 F-S01-70-05 classified as latent String 4.

**Bearer 4 = FALSE.** Class A found at Strings 1, 2, 3, and 4. Confinement requires ALL Class A at String 6 only. The v0.70 confinement repair failed to close the surfaces it targeted.

**Structural observation:** S04 (the deepest analysis, 18 findings) found ZERO Class A at String 6, and S01 (Kimi, strongest byte execution) found the majority of its Class A AT String 6. The code layer's six-round clean streak (R22-R27) may end at R28 depending on triage adjudication of the gate [13] fail-open and C-suffix findings.

---

## 3. Convergence Groups

### Group 1: C-suffix phantom repair (DECLARATION_PATTERNS blind to C-suffix)
**4-seat convergence.** All four seats independently identified that the extractor's DECLARATION_PATTERNS do not include C? after S\d{2}. The FINDING_ID_RE has C? but is dead code (S04) or disconnected from extraction logic (S01, S02, S03).

| Seat | Finding | Severity | String | Position |
|---|---|---|---|---|
| S01 | F-S01-70-05 | MEDIUM | 4 | 14 |
| S02 | F-S02-70-06 | MEDIUM | 4 | 12 |
| S03 | F-S03-70-02 | HIGH | 4 | 14 |
| S04 | F-S04-70-01 | CRITICAL | 1 | 2 |

**Triage severity:** HIGH. The repair claim is byte-false. The C? token exists in FINDING_ID_RE but not in the five DECLARATION_PATTERNS that actually do the extraction. The claim "Extractor, gate, and register now agree on the ID grammar. Closes F-S04-68-08" is false of the shipped bytes.

**Disposition:** CLOSED. Required repair: add C? after S\d{2} in all five DECLARATION_PATTERNS. Delete or wire in FINDING_ID_RE.

### Group 2: Gate [13] fail-open (skip-as-green when reports absent)
**3-seat convergence.** S02, S03, S04 independently identified that gate [13]'s else branch prints disclosure text without calling check(False, ...), allowing BUILD PASSED when reports are missing.

| Seat | Finding | Severity | String | Position |
|---|---|---|---|---|
| S02 | F-S02-70-01 | HIGH | 1 | 3 |
| S03 | F-S03-70-01 | HIGH | 1 | 3 |
| S04 | F-S04-70-03 | HIGH | 2 | 4 |

**Triage severity:** HIGH. The v0.70 entry does not claim gate [13] is "fail-closed" -- it says "[DISCLOSED] Gate [13] requires report files to verify index fidelity." However, the AUDIT_CONTEXT (written by the producer, not sealed in the protocol) claims fail-closed behavior. The disclosure text in build.py is accurate but the gate's behavior is that absence produces green, not red.

**Disposition:** CLOSED. Required repair: replace the else-branch prints with check(False, "CI-8 gate: no report files present"). Absence is not green.

### Group 3: Gate [13] summary line hardcodes zeros
**2-seat convergence.** S02 and S04 identified that the gate's PASS summary always prints "0 missing, 0 phantom, 0 severity mismatches" regardless of actual results (the line is inside the success path, after all three checks passed, so the zeros are technically correct on the success path -- but the line is narrated rather than derived from variables).

| Seat | Finding | Severity | String | Position |
|---|---|---|---|---|
| S02 | F-S02-70-07 | LOW | 6 | 18 |
| S04 | F-S04-70-02 | HIGH | 1 | 3 |

**Triage severity:** MEDIUM. The zeros are technically correct on the success path (all three check() calls passed before the print), but the narrated-not-derived pattern is the exact Axiom-3 failure mode. The print should derive its values from the computed variables.

**Disposition:** CLOSED. Required repair: use f-string with computed values: f"0 missing" -> f"{len(missing_from_index)} missing".

### Group 4: Register reproduction failure (register_gen crashes on shipped index)
**2-seat convergence.** S01 and S04 identified that xz_protocol_register_gen.py cannot reproduce the v0.70 amendment entry's register text from the shipped r27_findings_index.json.

| Seat | Finding | Severity | String | Position |
|---|---|---|---|---|
| S01 | F-S01-70-01 | HIGH | 2 | 4 |
| S04 | F-S04-70-04 | HIGH | 2 | 5 |

**Triage severity:** HIGH. The v0.70 entry tags every register line [COMPUTED: generate_register], which is a tag-accuracy claim (String 6, position 19). If the register generator cannot reproduce the text, the tags are false. S01 reports a crash; S04 reports a NOTED count mismatch (21 claimed, 20 enumerated).

**Disposition:** CLOSED. Required repair: fix register_gen.py to handle the R27 index structure; verify regenerated register matches the amendment entry text (or update the entry to match the tool output).

### Group 5: Section 0.1 / Section 22.2 / Status line version staleness
**2-seat convergence.** S02 and S04 identified stale version tokens in the protocol body.

| Seat | Finding | Severity | String | Position |
|---|---|---|---|---|
| S02 | F-S02-70-03 | HIGH | 3 | 9 |
| S02 | F-S02-70-04 | HIGH | 3 | 8 |
| S04 | F-S04-70-06 | HIGH | 3 | 8 |
| S04 | F-S04-70-07 | HIGH | 3 | 7 |
| S04 | F-S04-70-08 | HIGH | 3 | 9 |

**Triage severity:** HIGH. Multiple surfaces: Section 22.2 carried-entry bound stale at v0.68 (should be v0.69); Section 0.1 entry range internally impossible; Status line attributes R27 to wrong version. These are the same prose-staleness class that has recurred since R13.

**Disposition:** CLOSED. Required repair: update all stale version tokens in the protocol body to current values.

### Group 6: Gate [2f] / [10i] enforce false claims
**1-seat finding (S04 only, 2 findings).** S04 identified that gates [2f] and [10i] encode the VERSION-1 convention, which forces the Status line to attribute R27 to v0.69 (the base build) rather than v0.68 (the audited version). The gates manufacture the defect they exist to detect.

| Seat | Finding | Severity | String | Position |
|---|---|---|---|---|
| S04 | F-S04-70-09 | HIGH | 4 | 11 |
| S04 | F-S04-70-10 | HIGH | 4 | 12 |

**Triage severity:** HIGH. This is the deepest structural finding in R28. The gates enforce a convention (VERSION-1 = provenance version) that is semantically wrong when the build skips a version (v0.69 was a repair build; R27 audited v0.68, not v0.69). The gate-enforced claim is false of reality. Noted but deferred: requires a design decision on whether VERSION-1 or the actual audited version is the correct provenance reference.

**Disposition:** NOTED. Design decision required.

---

## 4. NOTED Findings (non-converging or deferred)

S01: F-S01-70-02 HIGH (tag accuracy), F-S01-70-03 HIGH (tag accuracy), F-S01-70-04 HIGH (tag accuracy), F-S01-70-06 LOW (gate limitation), F-S01-70-07 LOW (tagging), F-S01-70-08 LOW (seat drift), F-S01-70-09 HIGH (dispatch fidelity).
S02: F-S02-70-05 HIGH (manifest self-exclusion), F-S02-70-08 INFORMATIONAL (seat drift).
S04: F-S04-70-11 HIGH (terminal line ungated), F-S04-70-12 MEDIUM (pattern 4 admits bare refs), F-S04-70-13 MEDIUM (boundaries.json version stale), F-S04-70-14 LOW (manifest self-exclusion), F-S04-70-15 LOW (em-dash in .py), F-S04-70-16 INFORMATIONAL (seat non-independence), F-S04-70-17 INFORMATIONAL (dead code), F-S04-70-18 INFORMATIONAL (pytest not pre-installed).

---

## 5. Bearer State After R28

| Bearer | Status | Evidence |
|---|---|---|
| 1. Append-only | TRUE | 70/70 seals verify (all 4 seats confirm) |
| 2. Code correctness | TRUE | 186 GREEN (all 4 seats confirm); but gate [13] skip-as-green is a code defect |
| 3. Surface narrowing | **DISPUTED** | S04 argues code layer is no longer clean (C-suffix, gate [13]); others classify these as prose/claim defects |
| 4. Goedel confinement | **FALSE** | Class A at Strings 1, 2, 3, 4. Not confined to String 6. |
| 5. Cross-vendor witness | FALSE | No carrying non-HALT. S02 executed by GPT (wrong family for carry). |
| 6. Axiom disclosure | TRUE | Section 22.4 present |
| 7. Methodology | FALSE | Tagging defects at String 6 (S01); the Goedel surface |
| 8. The furqan | UNKNOWN | Lead's call |

---

## 6. The Structural Lesson

The v0.70 confinement repair targeted String 1/2/3/5 Class A. It introduced new Class A at the same strings it tried to clean. The C-suffix repair exists in the wrong regex. The gate [13] rebuild disclosed its absence case rather than failing on it. The register generator cannot reproduce its own output. The version tokens went stale because the producer narrated them instead of computing them.

This is the v0.15 clean-room discipline failure recurring at the v0.70 surface: every digest, count, and version stamp must be derived from bytes by a tool computation, never typed from memory. When the discipline holds, the defect migrates upward. When it breaks, the defect stays where it is.

H = 1.0. Twenty-two rounds. The instrument is alive.

---

*"The foam vanishes. What benefits the people remains in the earth."*

---

# Bismillah ir-Rahman ir-Rahim
