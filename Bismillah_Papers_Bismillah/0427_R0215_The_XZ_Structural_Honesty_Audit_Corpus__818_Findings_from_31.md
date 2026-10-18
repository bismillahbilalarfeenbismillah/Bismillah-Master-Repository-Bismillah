# Bismillah ir-Rahman ir-Rahim

# R0215 -- The XZ Structural Honesty Audit Corpus: 818 Findings from 31 Rounds of Multi-Model Verification

**Chronological Index:** 427 of 995  
**Date:** 2026-08  
**Section:** IV. XZ Protocol  
**Source File:** XZ_STRUCTURAL_HONESTY_AUDIT_CORPUS.md  
**Source Format:** md  
**SHA-256:** `25dc2508e839d60c51ee9e86c6b3979c12537a379a38bbcc69ec6d498f3beb55`  

---

## R0215 · The XZ Structural Honesty Audit Corpus: 818 Findings from 31 Rounds of Multi-Model Verification

- section: IV. XZ Protocol
- source_file: XZ_STRUCTURAL_HONESTY_AUDIT_CORPUS.md
- source_format: md
- text_sha256: 25dc2508e839d60c51ee9e86c6b3979c12537a379a38bbcc69ec6d498f3beb55

# The XZ Structural Honesty Audit Corpus: 818 Findings from 31 Rounds of Multi-Model Verification

Bilal Syed Arfeen

2026-08-18

Prepared with Claude Opus 4.6 (Anthropic) as analytical and drafting instrument under the author's direction and final authority. This paper makes no effectiveness claim about any component of the Structural Honesty program.

Bismillah ar-Rahman ar-Rahim

---

## Abstract

This paper describes the construction, schema, and content of the XZ Structural Honesty Audit Corpus, a structured dataset of 818 findings extracted from 199 seat reports across 31 audit rounds of the XZ Protocol (v0.37 through v0.74), produced by independent AI systems from four vendor families (Anthropic, OpenAI, Google, Moonshot/Zhipu). The corpus is the evidentiary substrate for the empirical claims in the companion synthesis paper "The Heartbeat of a Live System" and provides the first publicly available multi-model, multi-round audit dataset for a software verification instrument. The primary series -- 25 consecutive rounds with Class A (byte-false claim) defects present -- is recoverable from the structured data, with 136 Class A findings extracted across 19 of 25 rounds and the remaining 6 rounds documented as present in the verdict record but not individually classified in the extracted finding headers. The construction procedure (an 18-pattern regex extractor with 62 manual verdict overrides) ships with the corpus as a reproducible pipeline.

---

## 1. Motivation

The XZ Protocol audit program produced a 25-round empirical series whose central finding -- a software verification instrument cannot verify that it has no remaining byte-false claims about its own verification properties -- rests on primary evidence: the seat reports produced by independent AI auditors. The Heartbeat paper synthesizes this evidence into narrative. The corpus structures it into data.

No comparable dataset exists. Multi-model adversarial auditing of software artifacts is a new practice, and the audit reports have until now been scattered across chat sessions, dispatch packets, and handoff archives in heterogeneous formats spanning 75 protocol versions and four model families. The corpus makes this evidence queryable, reproducible, and independently verifiable.

The corpus publishes under the program's Gate 1 (safety) and Gate 2 (moat) discipline. Gate 1 is satisfied by construction: findings concern the protocol text's claims about its own verification properties, not the XZ Utils backdoor. No payload, activation recipe, or reconstruction detail appears anywhere in the corpus. Gate 2 is satisfied: the corpus is OPEN under the publication posture's Tier 1.

---

## 2. Composition

### 2.1 Scale

The corpus contains three structured outputs derived from 199 deduplicated seat reports:

- **reports.csv** -- 199 rows, one per unique seat report. Fields: filename, sha256, round, version, seat ID, model family, normalized family, role, mode, verdict, severity counts, Class A count, finding count, era classification.
- **findings.csv** -- 818 rows (796 unique finding IDs), one per extracted finding. Fields: finding ID, severity, finding class, tier, description, locus, round, version, seat ID, model family, normalized family, source report.
- **coverage.csv** -- round x version x seat x family verdict matrix.

### 2.2 Temporal span

The corpus covers 31 audit rounds (R1 through R31) and 64 protocol versions (v0.1 through v0.74), produced between August 1 and August 17, 2026. The rounds fall into five eras:

- **Pre-R7** (v0.1--v0.36): 71 reports. The carrying and advisory rounds before the Class A recurrence series began. Format heterogeneity is highest in this era.
- **Seat-lineage** (R1--R6, v0.37--v0.39): 42 reports. Cross-domain analytical frameworks (GAN convergence, Fractal/Hurst, Structural Revelation, Cobweb, Meta-audit) deployed across named seat lineages.
- **Convergence** (R7--R8, v0.40--v0.49): 20 reports. Multi-seat convergence rounds with the first standardized dispatch architecture.
- **CI era** (R9--R20, v0.50--v0.61): 34 reports. CI automation (v0.2 through v0.3.2), GPT-5.6 Sol enters as carrying seat, Kimi K3 as carrying seat.
- **Mature** (R21--R31, v0.62--v0.74): 32 reports. Standardized S0--S10 report structure, canonical six-suite pytest, four-family rotation.

### 2.3 Model family distribution

| Family | Reports | Role |
|---|---|---|
| Anthropic (Claude Opus 4.6 / 5) | 88 | Producer-family, advisory only, zero carry weight |
| OpenAI (GPT-5.6 Sol) | 64 | Advisory (self-disqualified from carry at v0.6), adversarial record |
| Zhipu (GLM-5.2) | 23 | Carrying seat (one of two carrying families) |
| Google (Gemini 3.1 Pro) | 15 | Advisory |
| Moonshot (Kimi K3) | 5 | Carrying seat (one of two carrying families) |
| Other/Unknown | 4 | Perplexity (1), unclassified (3) |

The carrying pool (Kimi K3 + GLM-5.2) is underrepresented in the extracted corpus relative to its governance weight because Kimi reports were often delivered as agent-output zip files whose internal markdown did not match the standard finding-header patterns, and GLM-5.2 reports frequently used minimal-format prose without structured finding headers.

### 2.4 Finding distribution

| Severity | Count | Pct |
|---|---|---|
| CRITICAL | 62 | 7.6% |
| HIGH | 360 | 44.0% |
| MEDIUM | 228 | 27.9% |
| LOW | 127 | 15.5% |
| INFORMATIONAL | 41 | 5.0% |

| Class | Count | Meaning |
|---|---|---|
| Class A | 136 | Byte-false claim in sealed or shipped text |
| Class B | 23 | Concealed defect (gate exists, doesn't cover) |
| Class C | 11 | Disclosed standing boundary |
| Class D | 24 | Gate limitation |
| Class E | 13 | Methodology or governance observation |
| Unclassified | 615 | No class tag in finding header (mostly pre-R13 and non-Opus reports) |

### 2.5 Verdict distribution

| Verdict | Count |
|---|---|
| HALT | 147 |
| CONDITIONAL PASS | 22 |
| PASS | 4 |
| Not extracted | 26 |

Verdict coverage is 87% (173/199). The 26 unextracted verdicts are predominantly Zhipu (GLM-5.2) and Moonshot (Kimi K3) reports in minimal or non-standard formats.

---

## 3. Collection process

### 3.1 Primary sources

The corpus was assembled from three archive files containing the complete audit dispatch and result history of the XZ Protocol program:

- Archive 1: 328 files (383 MB) -- dispatch packets and reports, R1--R31.
- Archive 2: 1,159 files (85 MB) -- dispatch prompts, seat reports, methodology documents.
- Archive 3: 595 files (344 MB) -- dispatch packets, Kimi agent outputs, seat reports.
- Supplementary: two handoff zips (v0.53, v0.54) containing the R12 report not present in the main archives.

Total raw material: 2,082 files. After deduplication by content hash and exclusion of non-report files (dispatch prompts, methodology documents, framework PDFs, OS metadata), 199 unique seat reports remained.

### 3.2 Extraction procedure

The construction procedure is a single Python script (`extract_corpus.py`, shipped with the corpus) that:

1. Walks all archive roots and discovers `.md` files passing the `is_seat_report` heuristic (positive signals: REPORT, AUDIT, VERDICT, RESULT, ADVISORY in filename; negative signals: DISPATCH_PROMPT, METHODOLOGY, DISCIPLINE, HANDOFF; content fallback: verdict pattern in first 3000 characters).
2. Deduplicates by SHA-256 content hash (handles the `(1)` / `(2)` copy variants in the archives).
3. Excludes 6 files identified by manual triage as non-reports (methodology documents, command logs).
4. Extracts report-level metadata (round, version, seat, model family, role, mode, verdict) from structured headers using 8 regex patterns with fallback to filename parsing.
5. Applies 62 manual verdict overrides for reports where the verdict is embedded in prose paragraphs rather than structured headers.
6. Extracts per-finding data using 18 regex patterns covering every observed finding-header format across the program's history, from the early numbered format (`### 1. Critical -`) through the mature six-element format (`### F-S04-74-01 [CRITICAL] [Class A] --`).
7. Extracts locus from `**Locus:**` fields, `**Severity:**` lines, and inline `Locus:` annotations.
8. Extracts finding class from headers, body text, and `**Severity:**` lines, accepting only single letters A--E.
9. Outputs three CSV files and a JSON summary.

The 18 finding-header patterns, in priority order:

1. Mature bracket: `### F-ID [SEVERITY] [Class X] -- description`
2. Mid-era class-first: `### F-ID [Class X] SEVERITY -- description`
3. Cross-domain tier: `### F-ID [SEVERITY] [Tier N] -- description`
4. Kimi bare-class: `### F-ID [SEVERITY] -- Class X -- description`
5. Bracket severity: `### F-ID [SEVERITY] -- description`
6. GPT slash-class: `### F-ID — SEVERITY / Class X`
7. GPT paren-class: `### F-ID — SEVERITY (Class X): description`
8. Em-dash severity: `### F-ID — SEVERITY — description`
9. GLM inline: `### N.N F-ID — description — **SEVERITY**`
10. Convergence: `### F-ID -- SEVERITY description`
11. Numbered early: `### N. Severity - description`
12. Bold finding: `**F-ID** [SEVERITY] -- description`
13. R8 numbered-bold: `N. **F-ID — Class X:** description`
14. R16 pipe-bold: `**F-ID | SEVERITY (Class X) | description**`
15. R17 pipe-hash: `### F-ID | SEVERITY (Class X) | Locus | description`
16. R12 class-after-dash: `### F-ID -- CLASS X (description)`
17. Bare header: `### F-ID` (severity on next line)
18. Bare description catch-all: `### F-ID — description` (severity from body)

### 3.3 What is not in the corpus

The corpus does not contain:

- The protocol text itself (published separately as XZ Protocol v0.75 FROZEN).
- The executable code (build.py, test suites, gates) -- these are part of the protocol deposit.
- The dispatch packets (AUDIT_CONTEXT.txt, DISPATCH.txt, EXECUTABLE_PACKET.txt) -- these are program infrastructure.
- The triage records (R1--R31 cross-seat triages) -- these are governance documents, not primary evidence.
- The CI outputs (pytest results, build.py gate logs) -- these are embedded in the seat reports and extractable from the finding descriptions, but not separately structured.
- Any XZ Utils payload, activation, or reconstruction content -- the protocol's Section 0.2 bars this, and the corpus inherits the prohibition.

---

## 4. Annotation schema

Each finding carries the following fields:

| Field | Type | Description |
|---|---|---|
| finding_id | string | Unique identifier in the program's namespace (e.g. F-S04-74-01) |
| severity | enum | CRITICAL, HIGH, MEDIUM, LOW, INFORMATIONAL |
| finding_class | enum | Class A (byte-false), Class B (concealed), Class C (disclosed), Class D (gate limit), Class E (governance) |
| tier | enum | Tier 1 (byte-reproducible), Tier 2 (tool-derived), Tier 3 (seat-produced) |
| description | string | First-line description from the finding header |
| locus | string | Where in the artifact the finding lives (file, line, section) |
| round_number | int | Audit round (1--31) |
| version | string | Protocol version under audit (v0.37--v0.74) |
| seat_id | string | Seat identifier (S01--S12, C01--C08, etc.) |
| model_family | string | Model name as reported |
| family_normalized | string | Vendor family (Anthropic, OpenAI, Google, Moonshot, Zhipu) |
| report_file | string | Source report filename |

The finding ID namespace encodes provenance: `F-{seat/namespace}-{version}-{sequence}`. The namespace prefix identifies the seat and often the analytical framework (e.g. F-OP = Opus producer-family, F-S02 = Seat 2 standardized, F-GPT37FH = GPT Fractal/Hurst on v0.37, F-CONV1 = Convergence Round 1).

---

## 5. Known limitations

1. **Class A extraction coverage.** The Heartbeat paper documents 25 consecutive rounds (R7--R31) with Class A present. The corpus extracts Class A findings from 19 of those 25 rounds. The 6 rounds without extracted Class A (R9--R11, R15, R28--R29) have Class A documented in the round verdict or triage record but not individually tagged in the finding headers the extractor parses. The Class A presence at every round is independently verifiable from the verdict record (all 25 rounds returned HALT with Class A cited as the basis).

2. **Unclassified findings.** 615 of 818 findings (75%) carry no class tag. The A--E classification was introduced at R7 and applied consistently only from R13 onward by Opus-family seats. GPT, Gemini, Kimi, and GLM reports frequently omit the class tag or embed it in prose rather than headers.

3. **Carrying-seat underrepresentation.** The two carrying families (Kimi K3, GLM-5.2) account for only 28 reports (14%) despite holding binding governance authority. Their reports use formats the extractor handles less completely (Kimi agent zip outputs, GLM minimal prose).

4. **Verdict coverage.** 26 of 199 reports (13%) have no extracted verdict. These are predominantly early-era Zhipu and Moonshot reports.

5. **Locus extraction.** 79% of findings have a locus field. The remaining 21% embed locus information in the finding body in non-standard formats.

6. **No disposition chains.** The corpus does not yet track finding lifecycles across rounds (raised at Rn, dispositioned at Rn+1, recurred at Rn+k). The cross-references are present in the finding descriptions and could be extracted in a future version.

7. **Round 36.** One report is tagged R36 (v0.36, pre-R7 era). This is a version-number artifact, not a genuine 36th audit round; the report audited v0.36 which predates the R1--R31 round-numbering system.

---

## 6. Uses

### 6.1 Intended uses

- **Reproducing the Heartbeat paper's empirical claims.** Every quantitative claim in the synthesis paper (25-round Class A series, H=1.0, defect migration trajectory, severity distribution, framework productivity) can be checked against the structured data.
- **Studying multi-model verification dynamics.** The corpus provides the first dataset for analyzing how different AI model families produce different findings on the same artifact under the same methodology.
- **Studying defect migration.** The round-over-round structure allows tracking how defect classes migrate upward through verification layers as lower layers are secured.
- **Methodology research.** The 18-pattern extractor documents the format evolution of AI-generated audit reports across 31 rounds and 4 families, which is itself a finding about standardization in multi-model workflows.

### 6.2 Out of scope

- **Training data for code generation or vulnerability detection.** The corpus contains no code, no vulnerabilities, and no XZ Utils technical content.
- **Evaluating AI model capabilities.** The corpus was not designed as a benchmark and the seat reports were produced under heterogeneous conditions (different dispatch formats, different execution environments, different context lengths).

---

## 7. Distribution

The corpus publishes as a Zenodo deposit under CC-BY-4.0, consistent with the program's publication posture (Tier 1, fully open). The deposit contains:

- `findings.csv` -- the primary dataset
- `reports.csv` -- report-level metadata
- `coverage.csv` -- round x seat verdict matrix
- `summary.json` -- aggregate statistics
- `extract_corpus.py` -- the construction procedure (reproducible pipeline)
- This paper (dataset card)

The raw seat reports are not included in the corpus deposit. They are available in the XZ Protocol's own deposit archive and in the program's handoff records.

Program chain DOIs: AX-SH5 Flagship 10.5281/zenodo.21500700; SHUDP 10.5281/zenodo.21522932; SHVVP 10.5281/zenodo.21583202; BSSG 10.5281/zenodo.21713180; BAF 10.5281/zenodo.20017335; PMD 10.5281/zenodo.21462879; SHV Method 10.5281/zenodo.21449063.

---

## 8. Maintenance

The corpus is a snapshot of the audit record as of v0.75 FROZEN (2026-08-17). If the protocol receives further audit rounds, a new version of the corpus will be produced by re-running the extractor on the expanded archive. The extractor is versioned (v0.3) and the version is recorded in the output metadata.

---

## Appendix A: Construction verification

The extractor's correctness can be verified by:

1. Re-running `extract_corpus.py` on the same archives and comparing the output hashes.
2. Spot-checking any finding row against its source report (the `report_file` field identifies the source).
3. Checking the 62 manual verdict overrides against the cited prose passages (each override's basis is documented in the extraction log).

The extractor does not modify any source file. It reads, parses, and outputs. The source reports are the evidence; the CSV files are a structured view.

---

Bilal Syed Arfeen
Bayyinah Structural Honesty Validation Program -- August 2026

"Indeed, We sent down the reminder, and indeed, We will be its preserver." (Qur'an 15:9)

---

# Bismillah ir-Rahman ir-Rahim
