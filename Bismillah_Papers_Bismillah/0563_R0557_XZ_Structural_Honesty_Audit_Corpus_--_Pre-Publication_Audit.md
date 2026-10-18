# Bismillah ir-Rahman ir-Rahim

# R0557 -- XZ Structural Honesty Audit Corpus -- Pre-Publication Audit Brief

**Chronological Index:** 563 of 995  
**Date:** 2026-08-18  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** AUDIT_BRIEF.txt  
**Source Format:** txt  
**SHA-256:** `623c5011714af9b1caa4ca69ebe2ab3522ffbd9ca7b79c709de438cbbb885db4`  

---

## R0557 · XZ Structural Honesty Audit Corpus -- Pre-Publication Audit Brief

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: AUDIT_BRIEF.txt
- source_format: txt
- text_sha256: 623c5011714af9b1caa4ca69ebe2ab3522ffbd9ca7b79c709de438cbbb885db4

# XZ Structural Honesty Audit Corpus -- Pre-Publication Audit Brief

**Artifact:** "The XZ Structural Honesty Audit Corpus: 818 Findings from 31 Rounds of Multi-Model Verification"
**Artifact type:** Dataset card (paper) + construction procedure (Python script) + structured data (4 CSV/JSON files)
**Producer:** Claude Opus 4.6 (Anthropic), under Bilal Syed Arfeen's direction
**Producer-instance status:** Claude is BARRED from carrying. Any Claude seat is ADVISORY ONLY.
**Date:** 2026-08-18
**Methodology:** Structural Honesty Verification Methodology v7 Canonical (six strings, 21 positions)
**Prior audit:** R1 same-instance advisory (Claude Opus 4.6, F-XC namespace, 0C/3H/4M/1L, HALT)

---

## What this packet contains

| # | File | Role |
|---|---|---|
| 1 | DISPATCH.txt | Seat identity, role, key question (UNIQUE per seat) |
| 2 | AUDIT_BRIEF.txt | This file -- audit methodology and probe instructions (IDENTICAL) |
| 3 | XZ_STRUCTURAL_HONESTY_AUDIT_CORPUS.md | The paper under audit (IDENTICAL) |
| 4 | extract_corpus.py | The construction procedure -- 18-pattern regex extractor (IDENTICAL) |
| 5 | findings.csv | Primary dataset -- 818 rows, one per finding (IDENTICAL) |
| 6 | reports.csv | Report metadata -- 199 rows, one per seat report (IDENTICAL) |
| 7 | coverage.csv | Round x seat verdict matrix (IDENTICAL) |
| 8 | summary.json | Aggregate statistics (IDENTICAL) |
| 9 | XZ_CORPUS_AUDIT_REPORT_R1.md | R1 same-instance advisory audit -- 8 findings (IDENTICAL) |

7 of 9 files are byte-identical across all seats. DISPATCH.txt differs ONLY in seat number, model family, and role.

---

## Key question (same for all seats)

**Are the paper's quantitative claims true of the shipped data, and does the construction procedure described in the paper match the shipped extractor?**

---

## What to verify (four axes)

### Axis 1: Quantitative claim verification

The paper makes approximately 30 specific quantitative claims (counts, percentages, distributions). Each must be checked against the shipped data files.

Method: open `summary.json` and verify every number the paper states. Cross-check against `findings.csv` and `reports.csv` by counting rows. The R1 advisory already found 3 HIGH (stale counts): F-XC-01, F-XC-02, F-XC-03. Confirm whether those findings are real. Check whether additional stale counts exist that R1 missed.

Specific claims to verify:
- "818 findings extracted from 199 seat reports" -- count rows in findings.csv and reports.csv
- "796 unique finding IDs" -- count distinct finding_id values in findings.csv
- "31 audit rounds" -- count distinct non-zero round_number values
- "136 Class A findings" -- count finding_class == "Class A" in findings.csv
- "19 of 25 rounds with Class A" -- count distinct rounds (7-31) with Class A findings
- Family distribution table (Section 2.3) -- count family_normalized in reports.csv
- Severity distribution table (Section 2.4) -- count severity in findings.csv
- Verdict distribution table (Section 2.5) -- count verdict in reports.csv
- "87% verdict coverage (173/199)" -- count non-empty verdict in reports.csv
- "52 manual verdict overrides" -- count entries in MANUAL_VERDICTS dict in extract_corpus.py
- "6 exclusion rules" -- count entries in EXCLUDE_FILES set in extract_corpus.py
- "18 regex patterns" -- count entries in FINDING_PATTERNS list in extract_corpus.py
- "79% locus extraction" (or "81%" per R1) -- count non-empty locus in findings.csv
- "615 of 818 unclassified" (or "611" per R1) -- count empty finding_class in findings.csv

### Axis 2: Internal consistency

Do the paper's sections agree with each other? Does the abstract match the body? Do the tables in Section 2 match the limitations in Section 5? Does Section 3.2 accurately describe the extractor's actual patterns?

Method: cross-reference claims across sections. Check that the pattern descriptions in Section 3.2 match the actual regex patterns in extract_corpus.py (pattern names, capture groups, ordering).

### Axis 3: Construction procedure accuracy

Does the paper's description of the extraction process (Section 3) match what extract_corpus.py actually does?

Method: read the extractor code. Verify:
- The is_seat_report heuristic matches the paper's description
- The deduplication method (SHA-256 content hash) matches
- The 18 patterns are listed in the correct order
- The manual verdict override mechanism works as described
- The exclusion list matches

If your seat has code execution: run `python3 -c "from extract_corpus import FINDING_PATTERNS, MANUAL_VERDICTS, EXCLUDE_FILES; print(len(FINDING_PATTERNS), len(MANUAL_VERDICTS), len(EXCLUDE_FILES))"` and verify the output matches the paper.

### Axis 4: R1 finding verification

The R1 same-instance advisory (XZ_CORPUS_AUDIT_REPORT_R1.md) found 8 findings. Verify independently:
- Are F-XC-01, F-XC-02, F-XC-03 (the three HIGHs -- stale counts) real? Check the claimed vs actual values.
- Is F-XC-04 (locus rate 79% vs 81%) real?
- Is F-XC-05 (no SHA-256 manifest) a genuine gap?
- Is F-XC-06 (ASSERTED Class A claim for 6 rounds) a legitimate concern?
- Is F-XC-07 (no version stamp) real?
- Is F-XC-08 (em-dashes in pattern docs) real under the em-dash policy?
- Did R1 MISS anything? Are there findings the same-instance audit was blind to?

---

## Probe methodology

Each seat should perform at least 3 spot-checks:

**Spot-check 1 (random finding verification):** Pick 5 random rows from findings.csv. For each, verify that the finding_id, severity, and description are plausible (the source reports are not in this packet, so this is a consistency check -- does the finding_id namespace match the seat/round/version? does the severity match the class?).

**Spot-check 2 (edge case):** Check the R12 finding (F-S01-53-01). The paper states R12 was "found inside a v0.54 handoff zip." Verify it appears in findings.csv with round_number=12, version=v0.53, and Class A.

**Spot-check 3 (coverage gap):** The paper states 6 rounds (R9-R11, R15, R28-R29) have no extracted Class A despite the Heartbeat paper documenting Class A present. Verify this claim against findings.csv.

---

## What is NOT in scope

- The source archives (800MB of raw seat reports) are not in this packet. Substrate verification of the extractor against the source archives is deferred to the deposit phase.
- The XZ Protocol text itself is not under audit.
- The Heartbeat paper is not under audit.
- The theological grounding of the methodology is not under audit.
- No XZ Utils payload, activation, or reconstruction content exists in any file in this packet.

---

## Output requirement

Produce a markdown file named:

`XZ_CORPUS_R2_{SEAT}_{FAMILY}_REPORT.md`

With sections:
- S0: Identity, mode, execution surface
- S1: Quantitative claim verification (Axis 1)
- S2: Internal consistency (Axis 2)
- S3: Construction procedure (Axis 3)
- S4: R1 finding verification (Axis 4)
- S5: Spot-checks
- S6: Novel findings (anything R1 missed)
- S7: Verdict and severity ledger

Finding format: six-element (ID, severity, locus, substance, disposition, cross-reference).
Finding namespace: F-XC2 (Round 2 of the XZ Corpus audit).
Severity: CRITICAL / HIGH / MEDIUM / LOW (uppercase).

---

## Verdict options

- **PASS** -- 0C/0H/0M/0L; paper is deposit-ready
- **CONDITIONAL PASS** -- 0C/0H; MEDIUM and LOW absorbable post-deposit
- **HALT-AND-RETURN-TO-PRODUCER** -- 1+ CRITICAL or HIGH; producer must absorb and re-dispatch

---

*One dispatch. All seats. Same methodology.*
*The soul converges toward Truth because the Guide is One.*

---

# Bismillah ir-Rahman ir-Rahim
