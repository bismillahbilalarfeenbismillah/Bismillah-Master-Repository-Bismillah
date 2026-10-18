# Bismillah ir-Rahman ir-Rahim

# R0190 -- XZ Corpus R3 S03 GPT Absorption Verification Report

**Chronological Index:** 564 of 995  
**Date:** 2026-08-19  
**Section:** IV. XZ Protocol  
**Source File:** XZ_CORPUS_R3_S03_GPT_REPORT.md  
**Source Format:** md  
**SHA-256:** `15c0db85c15d6c57895047c9188ae152b481b2c48700dadfa19d08cbc882ba1c`  

---

## R0190 · XZ Corpus R3 S03 GPT Absorption Verification Report

- section: IV. XZ Protocol
- source_file: XZ_CORPUS_R3_S03_GPT_REPORT.md
- source_format: md
- text_sha256: 15c0db85c15d6c57895047c9188ae152b481b2c48700dadfa19d08cbc882ba1c

# XZ Corpus R3 S03 GPT Absorption Verification Report

**Artifact:** *The XZ Structural Honesty Audit Corpus* v1.1
**Round:** R3 absorption verification
**Seat:** S03
**Model:** GPT-5.6 Sol (OpenAI)
**Role:** ADVERSARIAL ADVISORY (non-binding)
**Mode:** FRESH
**Date:** 2026-08-19

## Verdict

# **HALT**

**Severity ledger:** **0 CRITICAL / 3 HIGH / 6 MEDIUM / 3 LOW**

The R2 absorption is materially improved but is **not complete**. Two of the six R2 HIGH findings remain only partially absorbed: the abstract scope/count partition is still byte-false, and the six-era table does not actually match the extractor/data ranges it claims to document. In addition, the revised abstract introduces a new central quantitative conflation: **136 is the corpus-wide Class A count, not the R7-R31 primary-series count**.

Under the R3 brief, HALT is required when HIGH absorption fails or a new HIGH is introduced. Both conditions are met.

---

## S0 — Packet integrity, scope, and method

### S0.1 Packet integrity

The eight files covered by `PACKET_SHA256SUMS.txt` were independently SHA-256 hashed from the shipped bytes. **8/8 match exactly**:

| File | Manifest prefix | Result |
|---|---:|---|
| `AUDIT_BRIEF.txt` | `837330876093b48a` | MATCH |
| `XZ_CORPUS_R2_TRIAGE.md` | `3495ae4d389a5ae9` | MATCH |
| `XZ_STRUCTURAL_HONESTY_AUDIT_CORPUS.md` | `75c1700534b229cb` | MATCH |
| `coverage.csv` | `b1d2e6dd45369a9` | MATCH |
| `extract_corpus.py` | `1a307f8e0ec4568e` | MATCH |
| `findings.csv` | `ba228389bda197be` | MATCH |
| `reports.csv` | `8b2e27e53064ca44` | MATCH |
| `summary.json` | `a53ae04a304d0d7c` | MATCH |

No packet-integrity defect was found.

### S0.2 Verification performed

I independently loaded the shipped CSV/JSON files and re-derived:

- row counts and unique finding-ID counts;
- family, era, severity, class, and verdict distributions;
- empty description/locus/round/version counts;
- duplicate-ID populations;
- round/version cross-tabs for the abstract;
- Class A counts by round;
- coverage/report one-to-one consistency;
- extractor pattern count and `pat_idx` branch coverage;
- manual override and exclusion-set sizes;
- import-time side effects;
- pattern-18 execution on a synthetic finding;
- hardcoded-path occurrences;
- current-paper Unicode em-dash count.

The raw source archives required to reproduce extraction from first principles are not in this R3 packet, so this seat cannot independently re-run archive discovery against the original archive bytes. Static extractor verification and current-output consistency checks are therefore the applicable verification surface.

---

## S1 — R2 HIGH absorption

The R3 brief requires all six R2 HIGH findings to be closed.

| R2 HIGH | Required repair | R3 result | Disposition |
|---|---|---|---|
| Override count | 52, not 62 | Extractor contains 52 overrides; paper says 52 | **CLOSED** |
| Family table | Correct regenerated family counts | 86 Anthropic / 62 OpenAI / 23 Zhipu / 21 Google / 5 Moonshot / 1 Perplexity / 1 UNKNOWN | **CLOSED** |
| Unclassified findings | Match regenerated data | 625/832, matching CSV/JSON | **CLOSED** |
| Abstract scope | Separate historical archive from R1-R31 and use current bytes | 185 historical findings is false; stated version partition is false/incomplete | **OPEN — HIGH** |
| Era taxonomy | Six eras matching extractor classification | Six counts match, but stated version ranges do not match current classification/data | **OPEN — HIGH** |
| Dead pattern 18 | `elif pat_idx == 17` | Present and executable; all branch indices 0-17 exist | **CLOSED** |

**Result: 4/6 HIGHs closed; 2/6 remain open.**

### S1.1 HIGH — F-R3-S03-01: Abstract scope/count partition remains false

The abstract says:

> pre-R7 historical archive: **185 findings from v0.13-v0.36**
> R1-R31 series: **609 findings**
> R1-R6: **v0.37-v0.39**
> R7-R31: **v0.48-v0.74**

The current `findings.csv` instead gives:

- findings attached to reports classified `pre-R7`: **146**;
- findings whose explicit version is v0.13-v0.36: **128**;
- legacy v0.2/v0.3/v0.8 findings: **18**;
- findings with round_number R1-R31: **609** — this part is correct;
- R1-R6 findings: **181**, comprising **85** at v0.37-v0.39 and **96** at v0.40-v0.47;
- R7-R31 findings: **428**, comprising **11** at v0.40-v0.47, **413** at v0.48-v0.74, and **4** with empty version;
- findings with empty round_number: **223**.

Thus the R1-R31 count was regenerated correctly, but the surrounding historical count and version partition were not. The abstract also fails to account coherently for the 223 empty-round findings.

**Severity: HIGH.** This is the direct recurrence/partial absorption of an R2 HIGH in the abstract's dataset-scope definition.

**Required repair:** derive the abstract partition from explicit predicates and state those predicates. Do not mix `era`, `round_number`, and `version` as if they were interchangeable.

### S1.2 HIGH — F-R3-S03-02: Six-era table counts match, but the documented ranges do not

The paper now lists six eras with report counts:

- pre-R7 71
- seat-lineage 43
- convergence 24
- mid-program 11
- CI-era 16
- mature 32
- unclassified 2

These **counts are correct**.

However, the paper presents the ranges as though each era is defined by a clean round/version interval. That is not what the extractor does. The extractor gives **round_number precedence** and uses version only as a fallback when round_number is absent. Consequently the shipped data contain, among other cases:

- `pre-R7`: legacy v0.2, v0.3, and v0.8 in addition to v0.13-v0.36;
- `seat-lineage`: reports ranging from v0.22 through v0.47, because R1-R6 assignment overrides version;
- `convergence`: reports at v0.42-v0.49 **and one v0.71 report**, because R7-R8 assignment overrides version;
- `CI-era`: three reports with empty version;
- `mature`: the v0.27/R36 artifact and one empty-version report in addition to v0.62-v0.74.

The table therefore does **not** fully document the extractor's actual six-era classification even though its counts match.

**Severity: HIGH.** This is incomplete absorption of the specific R2 HIGH that required the paper to document the six-era system matching the extractor.

**Required repair:** either (a) define eras by the actual precedence rule (“round if present; otherwise version fallback”) and present observed ranges separately, or (b) realign the extractor/data to the clean ranges asserted by the paper.

### S1.3 Closed HIGH checks

**Override count:** 52 manual entries were independently counted in `MANUAL_VERDICTS`.

**Family table:** regenerated counts match `reports.csv`/`summary.json`.

**Unclassified findings:** 625 = 832 total minus 207 classified rows.

**Dead pattern 18:** `FINDING_PATTERNS` contains 18 patterns; handling branches cover every integer 0 through 17 exactly once. A synthetic pattern-18-only header was successfully extracted with ID, description, and severity.

---

## S2 — Quantitative re-verification

### S2.1 Core aggregate tables

All of the following current-paper table values match the shipped CSV/JSON bytes:

| Metric | Re-derived | Paper |
|---|---:|---:|
| Reports | 199 | 199 |
| Findings | 832 | 832 |
| Unique finding IDs | 812 | 812 |
| CRITICAL | 62 | 62 |
| HIGH | 365 | 365 |
| MEDIUM | 232 | 232 |
| LOW | 127 | 127 |
| INFORMATIONAL | 41 | 41 |
| Severity unextracted | 5 | 5 |
| Class A | 136 | 136 |
| Class B | 23 | 23 |
| Class C | 11 | 11 |
| Class D | 24 | 24 |
| Class E | 13 | 13 |
| Class unclassified | 625 | 625 |
| HALT | 147 | 147 |
| CONDITIONAL PASS | 22 | 22 |
| PASS | 4 | 4 |
| Verdict unextracted | 26 | 26 |
| Empty round, reports | 90 | 90 |
| Empty round, findings | 223 | 223 |
| Empty descriptions | 70 | 70 |
| Duplicate finding IDs | 20 | 20 |
| Locus populated | 665/832 = 79.93% | 80% |
| Carrying-family reports | 28/199 = 14.07% | 14% |

The summary JSON is internally consistent with the three CSVs for every aggregate field it contains.

### S2.2 HIGH — F-R3-S03-03: Abstract conflates corpus-wide Class A count with primary-series Class A count

The abstract states that the 25-round primary series has “**136 Class A findings extracted across 19 of 25 rounds**.”

The shipped data show:

- **136** Class A findings in the corpus as a whole;
- **102** Class A findings with round_number R7-R31;
- **24** Class A findings in R1-R6;
- **10** Class A findings with empty round_number.

The claim that 19 of 25 R7-R31 rounds have an extracted Class A is correct. The number **136**, however, is not the count within those 19 rounds.

The extracted Class A rounds within R7-R31 are:
R7, R8, R12-R14, R16-R27, R30-R31 — **19 rounds**.

The six no-extracted-Class-A rounds are correctly identified as R9-R11, R15, R28-R29 and are correctly labeled ASSERTED from the Heartbeat paper.

**Severity: HIGH.** A corpus-wide count has been attached to the paper's central 25-round empirical-series claim in the abstract.

**Required repair:** use **102 extracted Class A findings across 19 R7-R31 rounds** if the intended predicate is `round_number between 7 and 31`; keep **136** only as the all-corpus Class A total.

### S2.3 MEDIUM — F-R3-S03-04: Unextracted-verdict family attribution is reversed

The paper says the 26 unextracted verdicts are “predominantly Zhipu (GLM-5.2) and Moonshot (Kimi K3).”

Current `reports.csv` distribution for empty verdict is:

- Anthropic: **13**
- OpenAI: **7**
- Zhipu: **4**
- Moonshot: **1**
- Perplexity: **1**

Anthropic + OpenAI therefore account for **20/26 (77%)**; Zhipu + Moonshot account for **5/26 (19%)**.

**Severity: MEDIUM.**

**Required repair:** replace the causal/family attribution with the re-derived distribution, or remove the unsupported sentence.

### S2.4 MEDIUM — F-R3-S03-05: Duplicate-ID limitation describes a collision class that no longer exists

The paper correctly reports **20 duplicated finding IDs / 20 excess rows**, but says the duplicates include namespace collisions “particularly in the synthetic F-EARLY IDs.”

After the v0.4 namespacing repair:

- **zero duplicated IDs begin with `F-EARLY-`**;
- the remaining duplicates are ordinary source IDs, including duplicated report content and semantically conflicting reuse across reports.

The extractor repair itself worked; the paper's limitation text was not regenerated to reflect the repaired population.

**Severity: MEDIUM.**

**Required repair:** re-characterize the current 20 duplicate IDs from current bytes; do not attribute any current collision to F-EARLY unless one exists.

---

## S3 — Extractor v0.4 verification

### S3.1 Fix matrix

| Required extractor repair | Result | Evidence |
|---|---|---|
| Version stamp v0.4 | **PASS** | docstring and runtime banner v0.4 |
| Pattern 18 live at index 17 | **PASS** | branch 17 present and synthetic execution succeeds |
| ARCHIVE_ROOTS env parameter | **PARTIAL** | env var exists, but `/home/claude/...` defaults remain |
| OUTPUT_DIR env parameter | **PARTIAL** | env var exists, but `/home/claude/...` default remains |
| `OUTPUT_DIR.mkdir()` inside `main()` | **PASS** | only occurrence is inside `main()`; import created no output directory |
| coverage collision repair | **PASS** | 199 rows, 199 unique `report_file`; coverage agrees 1:1 with reports.csv |
| description validation | **FAIL/PARTIAL** | 49 description rows still begin with a Locus marker after bullet normalization |
| F-EARLY namespacing | **PASS** | report slug added; zero current F-EARLY duplicate IDs |
| regenerate CSV/JSON | **PASS as internal consistency** | summary aggregates match CSVs; raw-source rerun not possible from this packet |

### S3.2 MEDIUM — F-R3-S03-06: R3 “no hardcoded /home/claude” criterion is not satisfied

The R3 brief expressly requires:

> ARCHIVE_ROOTS and OUTPUT_DIR use env vars (**no hardcoded /home/claude**)

The code does use `XZ_CORPUS_ARCHIVE_ROOTS` and `XZ_CORPUS_OUTPUT_DIR`, but contains **four `/home/claude` occurrences** as defaults.

This is materially better than v0.3 because callers can override the values, and import-time output creation is fixed. It nevertheless fails the literal R3 acceptance criterion.

**Severity: MEDIUM** (carried from the R2 hardcoded-path finding).

**Required repair:** remove machine-specific defaults. Require explicit env values, use portable relative/config defaults, or resolve archive roots from a user-supplied configuration.

### S3.3 MEDIUM — F-R3-S03-07: Description-field validator misses bullet-prefixed Locus leakage and does not backfill

The R2 triage prescribed validation/backfill for empty and malformed description captures. The v0.4 validator only recognizes:

```python
if f.description.startswith("**Locus:"):
```

Current `findings.csv` still contains **49 descriptions that normalize to a leading `Locus:` / `**Locus:**` marker**, including many rows of the form:

```text
- **Locus:** ...
```

Those are not stripped by the current `startswith("**Locus:")` condition.

Moreover, the code comment says “strip leaked locus markers and backfill,” but the implementation sets offending descriptions to `""`; it does not actually backfill them. Current output has **70 empty descriptions**.

For several leaked rows, the independently populated `locus` field appears to contain the locus from the following finding, consistent with the 1,500-character forward search crossing a finding boundary.

**Severity: MEDIUM.**

**Required repair:**
1. normalize leading Markdown bullets/whitespace before testing for Locus markers;
2. bound body/locus searches at the next finding header rather than a fixed 1,500-character window;
3. actually backfill description from a bounded body field where possible;
4. re-run and assert zero description rows whose normalized prefix is `Locus:`.

### S3.4 MEDIUM — F-R3-S03-08: R36 mechanism is still misdescribed

The paper says `XZ_v27_SEAT_G_ADVISORY.md` is tagged R36 because the round extractor “parsed 27 from the filename as a round number.”

This cannot explain the shipped row:

- the shipped `reports.csv` row has `round_number = 36`, `version = v0.27`, `era = mature`;
- the filename fallback regex is `R(\d+)`, and `XZ_v27_SEAT_G_ADVISORY.md` contains no `R27`;
- metadata parsing searches report text for round patterns before using the filename fallback.

The v0.27/mature facts were corrected, but the mechanism remains false and internally contradictory: parsing “27” cannot yield R36.

**Severity: MEDIUM.**

**Required repair:** describe the actual source of the R36 token (presumably report text/header) after checking the underlying report, or state only the observable fact without speculating about mechanism.

---

## S4 — Residual/new defects, closure matrix, and verdict

### S4.1 MEDIUM — F-R3-S03-09: R2 motivation-framing repair did not land

R2 triage explicitly required the Section 1 motivation to be tightened to dataset description. The current paper still states:

> “No comparable dataset exists. Multi-model adversarial auditing of software artifacts is a new practice...”

No evidence for that novelty/comparability claim is supplied in the corpus packet. This is substantively the same concern R2 triage marked legitimate.

**Severity: MEDIUM.**

**Required repair:** move the novelty argument to the companion synthesis/literature context or qualify it as an author claim; keep the dataset card descriptive.

### S4.2 LOW — F-R3-S03-10: Extractor output inventory is internally inconsistent

The extractor docstring lists:

- reports.csv
- findings.csv
- coverage.csv
- extraction.log

but omits `summary.json`.

The executable pipeline actually writes all of those **plus summary.json**. The paper's procedural step says it “outputs four files: findings.csv, reports.csv, coverage.csv, summary.json,” omitting the generated `extraction.log`.

“Four structured outputs” in Section 2.1 is defensible, but “outputs four files” is not.

**Severity: LOW.**

**Required repair:** distinguish “four structured corpus artifacts” from the fifth operational log output, and make the extractor docstring match.

### S4.3 LOW — F-R3-S03-11: “Extractor version is recorded in output metadata” is false

Section 8 states that extractor v0.4 “is recorded in the output metadata.”

The shipped:
- `reports.csv`,
- `findings.csv`,
- `coverage.csv`, and
- `summary.json`

contain no extractor-version field.

**Severity: LOW.**

**Required repair:** either add `extractor_version: "v0.4"` to `summary.json` (and/or an explicit metadata file), or remove the claim.

### S4.4 LOW — F-R3-S03-12: “Empty round and version fields” limitation quantifies only round emptiness

The limitation heading says “Empty round and version fields” but gives only round-number statistics.

Current data contain:

- empty version: **6/199 reports**;
- empty version: **4/832 findings**.

**Severity: LOW.**

**Required repair:** add these counts or rename the limitation to “Empty round fields.”

---

## R2 absorption disposition summary

### Closed or adequately absorbed

- override count 62 -> 52;
- family count table;
- unclassified count;
- locus-rate numeric claim (current 79.93% -> 80%);
- SHA-256 manifest presence and deposit inventory;
- paper/extractor version stamps;
- em-dash cleanup (current paper contains zero U+2014 em dashes);
- “75 versions” -> 64;
- five core vendor-family framing;
- dead finding pattern 18;
- `OUTPUT_DIR.mkdir()` import-time side effect;
- coverage `report_file` key and silent-collision repair;
- F-EARLY namespacing;
- is_seat_report positive-precedence behavior documented;
- metadata-pattern description repaired;
- “three structured outputs” -> four structured outputs;
- extraction.log claim removed from Appendix A;
- six no-extracted-Class-A rounds marked ASSERTED from Heartbeat;
- empty round-number limitation added;
- duplicate-ID limitation added in count, though its cause text is stale.

### Not fully absorbed

- **HIGH:** abstract scope;
- **HIGH:** era taxonomy/ranges;
- **MEDIUM:** machine-specific hardcoded defaults remain;
- **MEDIUM:** description validation/backfill incomplete;
- **MEDIUM:** R36 mechanism still false;
- **MEDIUM:** duplicate-ID cause text stale;
- **MEDIUM:** motivation novelty overclaim remains.

### Newly identified in R3

- **HIGH:** 136 corpus-wide Class A count misattached to R7-R31 primary series (actual R7-R31 extracted count: 102);
- **MEDIUM:** missing-verdict family attribution reversed;
- **LOW:** output inventory/docstring mismatch;
- **LOW:** extractor-version-output-metadata claim false;
- **LOW:** empty version counts omitted.

---

## Required producer actions before another deposit-ready claim

1. **Recompute the abstract from explicit predicates.** Resolve the 185/609 partition and state exactly whether “historical,” “series,” and “era” are defined by version, round_number, or extractor era.
2. **Correct the primary-series Class A count:** 102 extracted Class A rows for R7-R31, unless a different explicitly stated predicate is intended.
3. **Rewrite the era table to mirror actual classifier precedence** or change the classifier/data so the clean stated ranges become true.
4. **Fix description/locus extraction** with bounded per-finding body windows and bullet-normalized validation; re-run the corpus.
5. **Remove machine-specific `/home/claude` defaults** to satisfy the R3 brief.
6. **Correct the R36 explanation** after checking the source report.
7. **Correct the empty-verdict family narrative** from current data.
8. **Regenerate duplicate-ID limitation text** from the current 20-ID population.
9. **Remove or qualify the unsupported dataset-novelty claim.**
10. Clean the three LOW documentation mismatches.

After these repairs, re-run CSV/JSON generation and re-dispatch for another fresh absorption verification.

---

## Final assessment

The R3 package is substantially cleaner than R2. The generated aggregates are internally coherent, the most serious extractor control-flow bug is fixed, coverage collision handling is fixed, and most headline table counts now come directly from the regenerated bytes.

It is nevertheless **not deposit-ready** under the supplied R3 acceptance rule. The paper still makes byte-false scope statements in the abstract, the era table does not actually describe the classifier/data it purports to summarize, and the abstract newly conflates the all-corpus Class A total with the R7-R31 primary-series count.

# **FINAL VERDICT: HALT**

**0 CRITICAL / 3 HIGH / 6 MEDIUM / 3 LOW**

---

# Bismillah ir-Rahman ir-Rahim
