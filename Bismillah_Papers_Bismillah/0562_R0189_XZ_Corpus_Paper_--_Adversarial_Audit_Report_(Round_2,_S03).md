# Bismillah ir-Rahman ir-Rahim

# R0189 -- XZ Corpus Paper -- Adversarial Audit Report (Round 2, S03)

**Chronological Index:** 562 of 995  
**Date:** 2026-08-18  
**Section:** IV. XZ Protocol  
**Source File:** XZ_CORPUS_R2_S03_GPT_REPORT.md  
**Source Format:** md  
**SHA-256:** `7351882d2f452932593ee9ec75ef4dd98e03a8c041f208811167bca549f4135b`  

---

## R0189 · XZ Corpus Paper -- Adversarial Audit Report (Round 2, S03)

- section: IV. XZ Protocol
- source_file: XZ_CORPUS_R2_S03_GPT_REPORT.md
- source_format: md
- text_sha256: 7351882d2f452932593ee9ec75ef4dd98e03a8c041f208811167bca549f4135b

# XZ Corpus Paper -- Adversarial Audit Report (Round 2, S03)

**Artifact:** *The XZ Structural Honesty Audit Corpus: 818 Findings from 31 Rounds of Multi-Model Verification*
**Seat:** S03
**Model:** GPT-5.6 Sol (OpenAI)
**Role:** ADVERSARIAL ADVISORY -- non-binding
**Dispatch mode:** FRESH; this audit restricts evidentiary reliance to the bytes in the R2 packet
**Namespace:** F-XC2
**Date:** 2026-08-18

> **Verdict: HALT-AND-RETURN-TO-PRODUCER**
>
> **Severity ledger: 0 CRITICAL / 6 HIGH / 9 MEDIUM / 2 LOW**
>
> The R1 same-instance audit correctly found several stale values, but it missed multiple independent defects in the paper's quantitative framing and in the extractor itself. Most importantly, the shipped extractor compiles 18 finding patterns but never executes the handling branch for pattern 18 because the `pat_idx == 16` branch is duplicated; index 17 is unhandled and matches are silently discarded. The paper is not deposit-ready.

---

## S0: Identity, mode, execution surface

Audit execution used direct byte access to the supplied R2 packet, Python 3 execution/import of `extract_corpus.py`, independent CSV/JSON counting, regex/code inspection, and SHA-256 verification of the packet manifest. No raw 800 MB source-report archive was present, so source-to-row substrate verification remains outside this audit exactly as the brief states.

The following shipped artifacts were directly inspected or executed:

- `XZ_STRUCTURAL_HONESTY_AUDIT_CORPUS.md`
- `extract_corpus.py`
- `findings.csv`
- `reports.csv`
- `coverage.csv`
- `summary.json`
- `XZ_CORPUS_AUDIT_REPORT_R1.md`
- `PACKET_SHA256SUMS.txt`

`PACKET_SHA256SUMS.txt` was independently recomputed for all eight files it lists; every listed digest matches the shipped byte stream.

---

## S1: Quantitative claim verification (Axis 1)

### S1.1 Core claims

| Claim | Paper | Shipped-data result | Status |
|---|---:|---:|---|
| Seat reports | 199 | 199 rows in `reports.csv`; 199 distinct SHA-256 hashes | **TRUE** |
| Findings | 818 | 818 rows in `findings.csv` | **TRUE** |
| Unique finding IDs | 796 | 796 distinct non-empty IDs | **TRUE**, but see F-XC2-11 |
| Class A findings | 136 | 136 | **TRUE** |
| Class A rounds R7--R31 | 19 of 25 | 19 rounds | **TRUE** |
| Missing extracted Class A rounds | R9--R11, R15, R28--R29 | Exactly those 6 | **TRUE** |
| CRITICAL | 62 | 62 | **TRUE** |
| HIGH | 360 | 360 | **TRUE** |
| MEDIUM | 228 | 228 | **TRUE** |
| LOW | 127 | 127 | **TRUE** |
| INFORMATIONAL | 41 | 41 | **TRUE** |
| HALT reports | 147 | 147 | **TRUE** |
| CONDITIONAL PASS | 22 | 22 | **TRUE** |
| PASS | 4 | 4 | **TRUE** |
| Verdict not extracted | 26 | 26 | **TRUE** |
| Verdict coverage | 87% (173/199) | 173/199 = 86.93% | **TRUE (rounded)** |
| Manual verdict overrides | 62 | 52 dictionary entries | **FALSE** |
| Exclusion rules | 6 | 6 set entries | **TRUE** |
| Finding regex patterns | 18 | 18 compiled regex objects | **NUMERICALLY TRUE**, operationally false for pattern 18; see F-XC2-06 |
| Unclassified findings | 615 | 611 | **FALSE** |
| Locus extraction | 79% | 665/818 = 81.30% | **FALSE** |
| Protocol versions | 64 | 64 distinct non-empty `reports.csv` version strings | **TRUE as a count**, but the paper's span/framing is inconsistent; see F-XC2-07 |
| Carrying-family reports | 28 | Zhipu 23 + Moonshot 5 = 28 (14.07%) | **TRUE** |

### S1.2 Model-family table

Actual `reports.csv` normalized-family counts are:

| Family | Actual reports |
|---|---:|
| Anthropic | 86 |
| OpenAI | 62 |
| Zhipu | 23 |
| Google | 21 |
| Moonshot | 5 |
| Perplexity | 1 |
| UNKNOWN | 1 |

The paper's table is stale in four cells: Anthropic 88 -> 86; OpenAI 64 -> 62; Google 15 -> 21; Other/Unknown 4 -> 2. Zhipu 23 and Moonshot 5 are correct.

### S1.3 Era distribution

The paper states five eras totaling 199 reports: 71 / 42 / 20 / 34 / 32. The shipped `reports.csv` `era` field and `summary.json` instead contain:

| Shipped era label | Count |
|---|---:|
| pre-R7 | 71 |
| seat-lineage | 43 |
| convergence | 24 |
| mid-program | 11 |
| CI-era | 16 |
| mature | 32 |
| blank | 2 |

This is not a rounding issue. The paper describes a five-era partition that does not match the extractor's six-label classification logic or its output.

### S1.4 Round-count nuance

`findings.csv` contains finding rows tagged only to R1--R31 (plus 214 rows with no round number). `reports.csv` and `coverage.csv`, however, contain a report tagged `R36` (`XZ_v27_SEAT_G_ADVISORY.md`, version v0.27). Thus the distinct non-zero `reports.csv` round numbers are 32 values: 1--31 plus 36. Section 5.7 acknowledges that R36 is a version-number parsing artifact, but the `round_number` field is not normalized accordingly and the schema still says `1--31`.

---

## S2: Internal consistency (Axis 2)

Several internal contradictions survive R1:

1. The abstract says the 818 findings come from XZ Protocol versions “v0.37 through v0.74,” while Section 2.2 explicitly includes the pre-R7 corpus. The shipped data contain **137 finding rows with numeric version suffixes below 37** and **214 findings with no round number**. The abstract's scope sentence therefore does not describe all 818 rows.
2. The paper repeatedly says “four vendor/model families,” yet its own Section 2.3 table treats Anthropic, OpenAI, Zhipu, Google, and Moonshot as distinct families, and the shipped data additionally contain Perplexity and UNKNOWN. “Moonshot/Zhipu” is not one vendor family.
3. Section 2.1 says the corpus contains “three structured outputs,” while Section 3.2 correctly says the extractor outputs three CSV files **and a JSON summary**, and Section 7 lists `summary.json` as part of the corpus.
4. Section 4 defines `round_number` as 1--31, but Section 5.7 admits an R36 artifact that remains present in `reports.csv` and `coverage.csv`.
5. Section 4 calls `finding_id` a “Unique identifier,” yet 818 rows contain only 796 distinct IDs. The duplicates are not merely byte-identical repeated observations: 5 duplicate IDs disagree on severity, 4 on class, 6 on version, and 4 on round number.

---

## S3: Construction procedure (Axis 3)

### S3.1 Constant counts

Direct import of the shipped extractor produced:

```text
len(FINDING_PATTERNS) = 18
len(MANUAL_VERDICTS) = 52
len(EXCLUDE_FILES) = 6
```

Thus the paper is correct on 18 compiled finding regexes and 6 exclusions, but false on 62 manual overrides.

### S3.2 Pattern-order and handler audit

The paper's numbered pattern descriptions broadly correspond to the 18 compiled regex objects in priority order. However, the extraction dispatcher contains a concrete indexing defect:

- Pattern index 16 (`FINDING_PATTERNS[16]`) is handled by `elif pat_idx == 16` as the bare F-ID header.
- The next branch is **again** `elif pat_idx == 16`, but its comment and code are intended for the bare-description catch-all.
- The bare-description regex is actually `FINDING_PATTERNS[17]`.
- Therefore `pat_idx == 17` has no handler. Its `Finding` object never receives `finding_id`, and the final guard `if f.finding_id ...` drops it.

The extractor is consequently **not functionally an 18-pattern extractor** even though the list length is 18. Source archives are absent, so this audit cannot quantify how many source findings are lost through this branch, but the code defect is byte-observable and deterministic.

### S3.3 Locus description mismatch

Section 3.2 says the script extracts locus from `**Locus:**` fields, `**Severity:**` lines, and inline `Locus:` annotations. The code does not extract locus from `**Severity:**` lines. Its locus regexes target only `**Locus:**` and inline `Locus:` forms. `**Severity:**` is used to populate severity for bare-header/class-after-dash patterns. R1's explanation for the improved locus rate likewise incorrectly attributed locus extraction to `**Severity:**` lines.

### S3.4 `is_seat_report` precedence

The paper describes both positive filename signals and negative signals. The actual function returns `True` immediately on a positive signal **before checking any negative signals**. Consequently a filename containing both a positive token (for example `AUDIT`) and a negative token (for example `DISPATCH_PROMPT`) is accepted. No current row in `reports.csv` contains both token classes, so this is a latent construction-procedure defect rather than a demonstrated current-row contamination.

### S3.5 Extractor version stamp

The script docstring says `XZ Protocol Audit Corpus Extractor v0.1`, while the paper states the shipped extractor is v0.3. The paper itself carries no artifact version number. This confirms R1's versioning finding.

---

## S4: R1 finding verification (Axis 4)

| R1 finding | R2 disposition | Independent result |
|---|---|---|
| F-XC-01: 62 overrides vs 52 | **SUSTAINED** | `MANUAL_VERDICTS` has 52 entries. |
| F-XC-02: family table stale | **SUSTAINED, UNDER-SPECIFIED** | Four table cells are wrong; R1's prose failed to state the Google 15 -> 21 mismatch explicitly, although its proposed corrected table included 21. |
| F-XC-03: 615 unclassified vs 611 | **SUSTAINED** | Exactly 611 empty class fields. |
| F-XC-04: locus 79% vs 81% | **SUSTAINED ON VALUE; R1 CAUSAL EXPLANATION REJECTED** | 665/818 = 81.30%. The code does not extract locus from `**Severity:**` lines, contrary to R1's explanation. |
| F-XC-05: no SHA-256 manifest | **NOT SUSTAINED AS FRAMED IN R2** | The current packet includes `PACKET_SHA256SUMS.txt`; all eight listed digests validate. Section 7 still omits the manifest from the deposit inventory, so a minor documentation issue remains. |
| F-XC-06: six-round Class A assertion not shown by shipped structured data | **SUSTAINED** | Absence of extracted Class A in exactly six rounds is verified; the stronger claim that those six verdict texts cite Class A cannot be independently checked from this packet because raw reports/triage text are absent. |
| F-XC-07: no coherent version stamp | **SUSTAINED** | Paper has no version; script says v0.1 while paper says v0.3. |
| F-XC-08: eight U+2014 characters | **SUSTAINED, LOW** | Exactly 8 U+2014 characters occur, all in pattern examples. |

R1's statement that all quantitative claims were true except its four stale-value findings is itself not sustained. It missed the era-distribution mismatch, abstract scope mismatch, and family-count framing inconsistency, among other defects below.

---

## S5: Spot-checks

### Spot-check 1: five deterministic random finding rows

A fixed seed (`20260818`) selected five rows from `findings.csv`:

1. `F-S05-46-09` -- R5, v0.46, Anthropic, MEDIUM, Class A. ID/provenance fields are structurally plausible; no source report is available for semantic verification.
2. `F-OP32C899-03` -- v0.32, Anthropic, HIGH. The description field is malformed (`advisory, non-carrying. **HALT basis.**] --`), indicating header capture leakage.
3. `F-S04-64-09` -- R23, v0.64, Anthropic, MEDIUM. Structurally plausible.
4. `F-S02-51-04` -- R10, v0.51, Anthropic, HIGH. Structurally plausible.
5. `F-V42-02` -- R1, v0.42, Google, LOW, Class D. Its `description` begins with a `**Locus:**` line rather than a finding description, another extraction-quality anomaly.

Corpus-wide, **34 descriptions are empty**, **79 begin with a `**Locus:**` marker**, and 3 contain the malformed `HALT basis` capture observed above.

### Spot-check 2: R12 edge case

`F-S01-53-01` exists exactly as required:

- `round_number = 12`
- `version = v0.53`
- `finding_class = Class A`
- `severity = HIGH`
- source report `R12_OPUS5_ADVISORY_v0_53.md`

**PASS.**

### Spot-check 3: Class A coverage gap

Distinct R7--R31 rounds with extracted Class A are:

`7, 8, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 30, 31`

Exactly six rounds lack extracted Class A: **R9, R10, R11, R15, R28, R29**. This portion of the paper is correct.

### Additional anomaly probes

- Empty `finding_id`: **0**
- Finding rows with round number >31: **0**
- Report rows with round number >31: **1** (`R36`, disclosed as an artifact)
- Unexpected normalized families in reports relative to the paper's Section 4 enum: **Perplexity (1), UNKNOWN (1)**
- Duplicate finding IDs: **22 IDs / 44 rows**, creating 22 row-excess observations over 796 unique IDs

---

## S6: Novel findings (R1 misses)

### F-XC2-05 -- HIGH -- Era distribution and era schema do not match shipped output

- **ID:** F-XC2-05
- **Severity:** HIGH
- **Locus:** Paper Section 2.2; `summary.json` `reports_by_era`; `reports.csv` `era`; `extract_corpus.py` era classifier
- **Substance:** The paper gives a five-era 71/42/20/34/32 distribution. The shipped extractor/output use six non-empty era labels plus blanks: 71/43/24/11/16/32/2. The paper therefore does not describe the dataset's own era field.
- **Disposition:** Choose one canonical era taxonomy, update the classifier and regenerate outputs, then regenerate Section 2.2 from the output rather than hand-entering counts.
- **Cross-reference:** R1 missed this despite claiming all remaining quantitative claims were verified.

### F-XC2-06 -- HIGH -- Pattern 18 is compiled but functionally dead

- **ID:** F-XC2-06
- **Severity:** HIGH
- **Locus:** `extract_corpus.py`, `extract_findings`, duplicated `elif pat_idx == 16` branches following `FINDING_PATTERNS[16]` and `[17]`
- **Substance:** The 18th regex exists at index 17, but no `pat_idx == 17` handler exists. Any source header matched only by pattern 18 fails to receive a finding ID and is dropped by the final deduplication guard. This is a concrete completeness defect in the shipped construction procedure.
- **Disposition:** Change the second duplicated branch to `elif pat_idx == 17`, re-run extraction on the raw archive, regenerate all CSV/JSON outputs and every paper count, then re-audit.
- **Cross-reference:** Paper Abstract/Section 3.2 “18-pattern extractor” completeness claim.

### F-XC2-07 -- HIGH -- Abstract scope does not describe the 818 shipped finding rows

- **ID:** F-XC2-07
- **Severity:** HIGH
- **Locus:** Abstract; Section 2.2; `findings.csv`
- **Substance:** The abstract says the 818 findings are from XZ Protocol v0.37--v0.74 across 31 rounds. The corpus includes 137 findings whose numeric version suffix is below 37 and 214 findings with no extracted round number. Section 2.2 itself describes pre-R7 material. The headline scope sentence is therefore byte-false/internally inconsistent.
- **Disposition:** Rewrite the abstract to distinguish the full historical corpus from the 31-round R1--R31 series, and report how many rows belong to each scope.
- **Cross-reference:** Section 2.2 temporal span; Section 5 limitations.

### F-XC2-08 -- MEDIUM -- “Four vendor families” framing is false/internally inconsistent

- **ID:** F-XC2-08
- **Severity:** MEDIUM
- **Locus:** Abstract; Sections 1 and 6.1; Section 2.3 table; `reports.csv`
- **Substance:** The paper repeatedly says four families and combines “Moonshot/Zhipu,” despite Moonshot and Zhipu being separate normalized vendor families in the same table/data. The shipped reports contain five core named vendor families plus Perplexity and UNKNOWN.
- **Disposition:** State the exact normalization taxonomy and distinguish core rotation families, carrying families, and incidental/unknown families without collapsing vendors.
- **Cross-reference:** F-XC2-02 family-table count correction.

### F-XC2-09 -- MEDIUM -- Locus extraction procedure is misdescribed

- **ID:** F-XC2-09
- **Severity:** MEDIUM
- **Locus:** Paper Section 3.2 item 7; `extract_corpus.py` locus and severity regexes
- **Substance:** The paper says locus is extracted from `**Severity:**` lines. The code never derives locus from a severity line; it derives severity from them. This is a direct procedure-description mismatch.
- **Disposition:** Correct Section 3.2 and R1's causal narrative; if another locus path was intended, implement and test it before regenerating the corpus.
- **Cross-reference:** R1 F-XC-04 rationale.

### F-XC2-10 -- MEDIUM -- `round_number` schema contradicts shipped R36 artifact

- **ID:** F-XC2-10
- **Severity:** MEDIUM
- **Locus:** Paper Section 4 (`round_number` 1--31), Section 5.7; `reports.csv`; `coverage.csv`
- **Substance:** `reports.csv` and `coverage.csv` contain round 36 even though the schema bounds the field to 1--31. The paper discloses the parsing artifact but leaves the invalid value in the structured field, making simple distinct-round counting return 32.
- **Disposition:** Normalize that report to a null/non-round field or add an explicit `round_parse_artifact` field; regenerate `summary.json` so `rounds_covered` does not present 36 as an audit round.
- **Cross-reference:** Title/Abstract “31 rounds.”

### F-XC2-11 -- MEDIUM -- Duplicate finding IDs are semantically conflicting

- **ID:** F-XC2-11
- **Severity:** MEDIUM
- **Locus:** Paper Sections 2.1 and 4; `findings.csv`
- **Substance:** 818 rows contain 796 IDs, leaving 22 duplicate-ID row excess. Among the 22 duplicated IDs, 5 disagree on severity, 4 on class, 6 on version, and 4 on round number. Examples include `F-S05-60-05` (MEDIUM/Class B vs HIGH/Class A) and `F-S04-66-01` (R25/v0.66 vs R26/v0.67). Calling `finding_id` a unique identifier is therefore false at the row schema level, and aggregate analyses can double-count/cross-label the same identifier.
- **Disposition:** Define the row key explicitly (`report_file + finding_id` if observations are intended), distinguish repeated findings from ID collisions, and add collision diagnostics to the extractor/summary.
- **Cross-reference:** Paper's explicit “796 unique finding IDs” count.

### F-XC2-12 -- MEDIUM -- Description field does not reliably contain a finding description

- **ID:** F-XC2-12
- **Severity:** MEDIUM
- **Locus:** Paper Section 4 `description` schema; `findings.csv`
- **Substance:** 34 rows have empty descriptions; 79 descriptions begin with a `**Locus:**` marker; 3 contain malformed `HALT basis` header leakage. A deterministic five-row spot-check hit two such malformed/structurally wrong descriptions.
- **Disposition:** Add post-extraction validation for empty/field-marker descriptions, backfill from the finding body where the header carries no description, and regenerate affected rows.
- **Cross-reference:** Spot-check 1.

### F-XC2-15 -- MEDIUM -- Negative `is_seat_report` signals are not authoritative

- **ID:** F-XC2-15
- **Severity:** MEDIUM
- **Locus:** Paper Section 3.2 item 1; `extract_corpus.py:is_seat_report`
- **Substance:** The function checks positive filename tokens first and returns `True` before evaluating negative tokens. Therefore a filename containing both classes bypasses the negative filter. The shipped output currently has no report filename with both signal classes, so no present contamination is proven, but the implementation does not match the paper's stated heuristic semantics.
- **Disposition:** Evaluate negative exclusions before positive inclusions or document the precedence explicitly; add a regression test with a filename such as `AUDIT_DISPATCH_PROMPT.md`.
- **Cross-reference:** Construction-procedure accuracy axis.

---

## S7: Verdict and severity ledger

### Full finding ledger

#### F-XC2-01 -- HIGH -- Manual verdict override count is byte-false
- **Locus:** Abstract; Section 3.2 item 5; Appendix A item 3
- **Substance:** Paper says 62; shipped dictionary contains 52.
- **Disposition:** Replace 62 with 52 everywhere, or regenerate after any extractor correction.
- **Cross-reference:** R1 F-XC-01 (sustained).

#### F-XC2-02 -- HIGH -- Model-family table has four stale cells
- **Locus:** Section 2.3
- **Substance:** Correct counts are Anthropic 86, OpenAI 62, Zhipu 23, Google 21, Moonshot 5, Perplexity 1, UNKNOWN 1. Paper has Anthropic 88, OpenAI 64, Google 15, Other/Unknown 4.
- **Disposition:** Generate the table directly from `reports.csv`.
- **Cross-reference:** R1 F-XC-02 (sustained and clarified).

#### F-XC2-03 -- HIGH -- Unclassified finding count is stale
- **Locus:** Section 2.4; Section 5.2
- **Substance:** Paper says 615; shipped data contain 611 unclassified rows. 611/818 = 74.69%, which rounds to 75%.
- **Disposition:** Replace 615 with 611 everywhere.
- **Cross-reference:** R1 F-XC-03 (sustained).

#### F-XC2-04 -- MEDIUM -- Locus extraction percentage is stale
- **Locus:** Section 5.5
- **Substance:** 665/818 rows have non-empty locus = 81.30%, not 79%.
- **Disposition:** Replace 79%/21% with 81%/19% (or 81.3%/18.7%).
- **Cross-reference:** R1 F-XC-04 (value sustained; rationale corrected by F-XC2-09).

#### F-XC2-05 -- HIGH -- Era distribution and era schema do not match shipped output
- **Locus:** Section 2.2; `summary.json`; `reports.csv`; extractor era classifier
- **Substance:** Paper's five-era 71/42/20/34/32 partition does not match shipped 71/43/24/11/16/32 plus 2 blank.
- **Disposition:** Canonicalize taxonomy, regenerate output and prose.
- **Cross-reference:** Novel R2 finding.

#### F-XC2-06 -- HIGH -- Pattern 18 is compiled but functionally dead
- **Locus:** `extract_corpus.py:extract_findings`
- **Substance:** Duplicate `elif pat_idx == 16` leaves index 17 unhandled; pattern-18-only matches are dropped.
- **Disposition:** Fix branch to index 17 and regenerate all outputs/counts from source archives.
- **Cross-reference:** Novel R2 finding; blocks deposit.

#### F-XC2-07 -- HIGH -- Abstract scope is false for the full 818-row corpus
- **Locus:** Abstract; Section 2.2; `findings.csv`
- **Substance:** 137 finding rows carry versions below v0.37 and 214 have no round number, despite abstract framing all 818 as v0.37--v0.74 across 31 rounds.
- **Disposition:** Split full historical corpus scope from R1--R31 series scope.
- **Cross-reference:** Novel R2 finding.

#### F-XC2-08 -- MEDIUM -- Vendor-family count/framing is internally inconsistent
- **Locus:** Abstract; Sections 1, 2.3, 6.1
- **Substance:** “Four families” conflicts with separate Moonshot and Zhipu categories and the shipped Perplexity/UNKNOWN rows.
- **Disposition:** Define taxonomy explicitly and use it consistently.
- **Cross-reference:** F-XC2-02.

#### F-XC2-09 -- MEDIUM -- Locus extraction mechanism is misdescribed
- **Locus:** Section 3.2 item 7; extractor regexes
- **Substance:** `**Severity:**` lines are used for severity, not locus.
- **Disposition:** Correct prose or implementation.
- **Cross-reference:** R1 F-XC-04 rationale.

#### F-XC2-10 -- MEDIUM -- R36 violates the declared round-number schema
- **Locus:** Section 4; Section 5.7; `reports.csv`; `coverage.csv`; `summary.json`
- **Substance:** Distinct non-zero report rounds = 32 because R36 remains encoded as a round.
- **Disposition:** Normalize the artifact and regenerate round summaries.
- **Cross-reference:** Headline 31-round claim.

#### F-XC2-11 -- MEDIUM -- Duplicate IDs have conflicting semantics
- **Locus:** Sections 2.1 and 4; `findings.csv`
- **Substance:** 22 duplicated IDs include severity/class/version/round conflicts.
- **Disposition:** Define composite row key and collision policy; regenerate collision diagnostics.
- **Cross-reference:** 818 rows / 796 IDs claim.

#### F-XC2-12 -- MEDIUM -- Description-field extraction quality violates schema expectation
- **Locus:** Section 4; `findings.csv`
- **Substance:** 34 empty, 79 locus-marker descriptions, 3 malformed HALT-basis captures.
- **Disposition:** Add validation/backfill and regenerate affected rows.
- **Cross-reference:** Spot-check 1.

#### F-XC2-13 -- MEDIUM -- Six-round Class A verdict-basis claim is not independently verifiable from shipped structured data
- **Locus:** Abstract; Section 5.1
- **Substance:** The 19/25 extracted-Class-A result and six missing rounds are verified. The stronger claim that all six missing rounds have Class A cited in their verdict record cannot be verified from this packet; `reports.csv` stores only verdict labels and the source verdict prose/triage records are not included.
- **Disposition:** Mark the statement as externally asserted with a precise source, or include machine-verifiable evidence for the six round verdict bases.
- **Cross-reference:** R1 F-XC-06 (sustained).

#### F-XC2-14 -- MEDIUM -- Artifact/extractor version stamps conflict
- **Locus:** Paper header; Section 8; `extract_corpus.py` docstring
- **Substance:** Paper says extractor v0.3, script says v0.1, and paper itself has no version stamp.
- **Disposition:** Version both paper and extractor consistently before redispatch.
- **Cross-reference:** R1 F-XC-07 (sustained).

#### F-XC2-15 -- MEDIUM -- `is_seat_report` positive precedence defeats negative signals
- **Locus:** Section 3.2 item 1; `extract_corpus.py:is_seat_report`
- **Substance:** Positive filename tokens return `True` before negative tokens are tested.
- **Disposition:** Reverse precedence or document it and add tests.
- **Cross-reference:** Novel R2 construction finding.

#### F-XC2-16 -- LOW -- Structured-output count is internally inconsistent
- **Locus:** Section 2.1 vs Sections 3.2 and 7
- **Substance:** Section 2.1 says “three structured outputs,” while the corpus includes three CSVs plus `summary.json`.
- **Disposition:** Say “four structured outputs” or “three CSV outputs plus one JSON summary.”
- **Cross-reference:** Internal-consistency axis.

#### F-XC2-17 -- LOW -- Eight U+2014 characters remain in pattern documentation
- **Locus:** Section 3.2 pattern examples
- **Substance:** Exactly eight em-dashes remain, all within code-adjacent pattern examples.
- **Disposition:** Replace with escaped `\u2014` if the standing policy applies to quoted regex examples, or document the exception.
- **Cross-reference:** R1 F-XC-08 (sustained).

### R1 F-XC-05 disposition (no new numbered finding)

R1's “no SHA-256 manifest” claim is **not sustained as framed against the current R2 packet**. `PACKET_SHA256SUMS.txt` exists and all eight listed hashes verify. The remaining issue is merely that Section 7 does not list the manifest among deposit contents. This does not contribute a MEDIUM/HIGH to the R2 ledger.

### Final disposition

**HALT-AND-RETURN-TO-PRODUCER.** Before another carrying/pre-publication audit, the producer should at minimum:

1. Fix the pattern-18 dispatcher defect and re-run extraction on the source archives.
2. Regenerate all aggregate counts from the corrected outputs rather than patching prose values manually.
3. Canonicalize the era taxonomy and family taxonomy.
4. Resolve/declare duplicate finding-ID semantics and validate description-field quality.
5. Correct abstract scope, round-number normalization, locus-procedure description, and version stamps.
6. Re-dispatch the regenerated paper + script + CSV/JSON outputs with an updated hash manifest.

The present packet contains multiple HIGH defects in both quantitative narration and construction logic. Deposit should not proceed on these bytes.

*End of XZ Corpus R2 S03 adversarial audit report.*

---

# Bismillah ir-Rahman ir-Rahim
