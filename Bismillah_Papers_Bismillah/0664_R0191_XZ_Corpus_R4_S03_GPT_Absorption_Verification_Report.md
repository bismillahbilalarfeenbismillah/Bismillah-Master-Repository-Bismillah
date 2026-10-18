# Bismillah ir-Rahman ir-Rahim

# R0191 -- XZ Corpus R4 S03 GPT Absorption Verification Report

**Chronological Index:** 664 of 995  
**Date:** Undated  
**Section:** IV. XZ Protocol  
**Source File:** XZ_CORPUS_R4_S03_GPT_REPORT (1).md  
**Source Format:** md  
**SHA-256:** `3417e150732e59d9c11d5f5dce142d06025ea993f2fc8486966780164e4e14db`  

---

## R0191 · XZ Corpus R4 S03 GPT Absorption Verification Report

- section: IV. XZ Protocol
- source_file: XZ_CORPUS_R4_S03_GPT_REPORT (1).md
- source_format: md
- text_sha256: 3417e150732e59d9c11d5f5dce142d06025ea993f2fc8486966780164e4e14db

# XZ Corpus R4 S03 GPT Absorption Verification Report

**Artifact:** *The XZ Structural Honesty Audit Corpus* v1.2
**Extractor:** `extract_corpus.py` v0.5
**Round:** R4 absorption verification
**Seat:** S03
**Model:** GPT-5.6 Sol (OpenAI)
**Role:** ADVERSARIAL ADVISORY (non-binding)
**Mode:** FRESH
**Verdict:** **HALT**

**Severity ledger:** **0 CRITICAL / 1 HIGH / 1 MEDIUM / 4 LOW**

---

## Executive verdict

# **HALT**

The R4 package closes the R3 HIGH findings that motivated this round:

- the abstract now partitions the corpus as **609 R1–R31 findings + 223 unnumbered findings = 832**;
- the primary-series Class A count is now correctly **102 in R7–R31**, distinct from **136 corpus-wide**;
- the stale R1–R6 version parenthetical is removed;
- the era table now describes the extractor's **round-first, version-fallback** classification and its observed version ranges.

The core CSV/JSON aggregate tables are internally consistent and the packet hashes verify.

However, extractor v0.5 introduces/retains a deposit-blocking data-integrity defect in the R3 description/locus repair. The validator can silently preserve the **next finding's locus** while backfilling the current finding's description. A minimal test against the shipped extractor reproduces the cross-finding shift deterministically. Current `findings.csv` contains sequences consistent with this failure. Because the defect silently corrupts structured finding-to-locus attribution in the primary corpus, I rate it **HIGH**.

Under the R4 brief, a new HIGH requires HALT.

---

# S0 — Packet integrity, scope, and method

## S0.1 Packet inventory

The R4 archive contains:

1. `AUDIT_BRIEF.txt`
2. `DISPATCH.txt`
3. `PACKET_SHA256SUMS.txt`
4. `XZ_CORPUS_R2_TRIAGE.md`
5. `XZ_STRUCTURAL_HONESTY_AUDIT_CORPUS.md`
6. `coverage.csv`
7. `extract_corpus.py`
8. `findings.csv`
9. `reports.csv`
10. `summary.json`

The manifest covers the eight non-dispatch/non-self files. I independently SHA-256 hashed all eight.

| File | Manifest prefix | Result |
|---|---:|---|
| `AUDIT_BRIEF.txt` | `95b9b72068d054cc` | MATCH |
| `XZ_CORPUS_R2_TRIAGE.md` | `3495ae4d389a5ae9` | MATCH |
| `XZ_STRUCTURAL_HONESTY_AUDIT_CORPUS.md` | `974b937ddc168c7d` | MATCH |
| `coverage.csv` | `b1d2e6dd45369a9` | MATCH |
| `extract_corpus.py` | `7fcba60522d61125` | MATCH |
| `findings.csv` | `26a096a8e6acf4d5` | MATCH |
| `reports.csv` | `8b2e27e53064ca44` | MATCH |
| `summary.json` | `fffc56792335b727` | MATCH |

**Packet integrity: PASS.**

## S0.2 Verification surface

I independently re-derived from the shipped bytes:

- report/finding/coverage row counts;
- unique finding IDs;
- family, era, severity, class, and verdict distributions;
- round and Class A partitions used by the abstract;
- empty round/version/description/locus counts;
- duplicate-ID population;
- coverage-to-reports one-to-one consistency;
- `summary.json` agreement with CSV aggregates;
- manual override and exclusion-set sizes;
- discovery negative-signal count;
- metadata regex-family counts;
- finding-pattern count and handler coverage;
- import-time side effects;
- description-validator behavior with a minimal synthetic probe;
- machine-specific path literals;
- extractor version/output documentation.

The source archive reports are not included in the R4 packet, so exact source-row spot checks cannot be independently performed from this packet alone. Where source semantics would be required, I distinguish static/reproducible extractor defects from source-dependent conclusions.

---

# S1 — R3 absorption verification

## S1.1 R4 brief repair matrix

| R3 repair obligation | R4 result | Disposition |
|---|---|---|
| 1. Remove false “185 pre-R7” abstract partition | Abstract uses 609 R1–R31 + 223 unnumbered | **CLOSED** |
| 2. Distinguish 102 R7–R31 Class A from 136 corpus-wide | Correct in abstract, §2.4, §5.1 | **CLOSED** |
| 3. Remove/correct R1–R6 version-range parenthetical | Removed | **CLOSED** |
| 4. Description validator backfills rather than destroys | Empty descriptions decreased, but validator can cross-assign neighboring locus | **FAILED — HIGH** |
| 5. Verdict-family attribution | 13 Anthropic / 7 OpenAI / 4 Zhipu / 1 Moonshot / 1 Perplexity | **CLOSED** |
| 6. Duplicate-ID text removes F-EARLY attribution | No F-EARLY collision claim remains | **CLOSED** |
| 7. Add extractor version to summary | `"extractor_version": "v0.5"` present | **CLOSED** |
| 8. Pattern note includes pattern 18 | Pattern 18 added, but note remains technically inaccurate | **PARTIAL — LOW** |
| 9. Negative signal count = 12 | 12 terms in code and paper | **CLOSED** |
| 10. §3.2: 3 seat header patterns; 5 outputs | Correct | **CLOSED** |
| 11. R36 mechanism: observable fact only | Correctly reduced to observable fact | **CLOSED** |
| 12. §5.1 mechanism explanation | Corrected and data-compatible | **CLOSED** |

**R3 HIGH absorption:** all prior HIGH quantitative/scope findings are closed.
**Overall absorption:** not complete because the extractor-field repair fails materially.

---

# S2 — Quantitative re-verification

## S2.1 Abstract partition

Re-derived from `findings.csv`:

- total findings: **832**
- findings with `round_number` R1–R31: **609**
- findings with empty `round_number`: **223**
- findings assigned R36: **0**

Therefore:

**609 + 223 = 832**

The R36 artifact exists at report level only; its report has zero extracted findings.

**Abstract partition: PASS.**

## S2.2 Class A partition

Re-derived:

- all Class A findings: **136**
- R7–R31 Class A findings: **102**
- R1–R6 Class A findings: **24**
- empty-round Class A findings: **10**

Therefore:

**102 + 24 + 10 = 136**

R7–R31 rounds with at least one extracted Class A finding:

**R7, R8, R12, R13, R14, R16, R17, R18, R19, R20, R21, R22, R23, R24, R25, R26, R27, R30, R31 = 19 rounds**

No extracted Class A tag occurs at:

**R9, R10, R11, R15, R28, R29 = 6 rounds**

The paper correctly marks the companion-paper claim for those six rounds as **ASSERTED, not COMPUTED** from the structured corpus.

**Class A claims: PASS.**

## S2.3 Aggregate-table verification

| Metric | Re-derived | Paper | Result |
|---|---:|---:|---|
| Reports | 199 | 199 | PASS |
| Findings | 832 | 832 | PASS |
| Unique finding IDs | 812 | 812 | PASS |
| CRITICAL | 62 | 62 | PASS |
| HIGH | 365 | 365 | PASS |
| MEDIUM | 232 | 232 | PASS |
| LOW | 127 | 127 | PASS |
| INFORMATIONAL | 41 | 41 | PASS |
| Severity unextracted | 5 | 5 | PASS |
| Class A | 136 | 136 | PASS |
| Class B | 23 | 23 | PASS |
| Class C | 11 | 11 | PASS |
| Class D | 24 | 24 | PASS |
| Class E | 13 | 13 | PASS |
| Class unclassified | 625 | 625 | PASS |
| HALT | 147 | 147 | PASS |
| CONDITIONAL PASS | 22 | 22 | PASS |
| PASS verdict | 4 | 4 | PASS |
| Verdict unextracted | 26 | 26 | PASS |
| Empty-round reports | 90 | 90 | PASS |
| Empty-round findings | 223 | 223 | PASS |
| Empty-version reports | 6 | 6 | PASS |
| Empty-version findings | 4 | 4 | PASS |
| Empty descriptions | 34 | 34 | PASS |
| Populated locus | 681/832 = 81.85% | 82% | PASS |
| Duplicate IDs | 20 | 20 | PASS |
| Carrying-family reports (Zhipu + Moonshot) | 28/199 = 14.07% | 14% | PASS |

The family, era, severity, class, and verdict objects in `summary.json` agree with the CSVs.

## S2.4 Family counts

`reports.csv`:

- Anthropic: **86**
- OpenAI: **62**
- Zhipu: **23**
- Google: **21**
- Moonshot: **5**
- Perplexity: **1**
- UNKNOWN: **1**

Total: **199**.

The 26 missing verdicts are exactly:

- Anthropic: **13**
- OpenAI: **7**
- Zhipu: **4**
- Moonshot: **1**
- Perplexity: **1**

**Verdict-family R3 repair: PASS.**

## S2.5 Era counts and observed versions

Re-derived report counts:

- pre-R7: **71**
- seat-lineage: **43**
- convergence: **24**
- mid-program: **11**
- CI-era: **16**
- mature: **32**
- unclassified: **2**

The paper now correctly states the classifier precedence: use round number when available, then version fallback.

Observed parsed versions are compatible with the table:

- pre-R7: v0.13–v0.36 plus legacy v0.2/v0.3/v0.8
- seat-lineage: v0.22–v0.47
- convergence: v0.42–v0.49 plus v0.71
- mid-program: v0.50–v0.55
- CI-era: v0.56–v0.61, with some empty versions
- mature: v0.27 and v0.62–v0.74, with one empty version

**Era R3 repair: PASS.**

## S2.6 Duplicate-ID population

Current data contain exactly **20 IDs appearing twice**, yielding **812 unique IDs across 832 rows**.

No duplicated ID begins with `F-EARLY-`; the v0.4/v0.5 per-report namespacing repair is holding.

At the current structured-data level, the duplicates divide into:

- **5 IDs** whose core finding fields are the same across two report rows;
- **15 IDs** with differing core finding fields, consistent with namespace reuse/collision across reports.

The revised limitation text is materially accurate.

**Duplicate-ID R3 repair: PASS.**

---

# S3 — Extractor v0.5 verification

## S3.1 Mechanical checks

| Check | Result |
|---|---|
| Top extractor title says v0.5 | PASS |
| Runtime banner says v0.5 | PASS |
| `summary.json` contains extractor version v0.5 | PASS |
| Finding patterns | 18 |
| Finding handler branches | indices 0–17 exactly once |
| Manual verdict overrides | 52 |
| Manual exclusion entries | 6 |
| Negative discovery signals | 12 |
| Seat header patterns | 3 |
| Seat filename patterns | 5 |
| `OUTPUT_DIR.mkdir()` inside `main()` | PASS |
| Import creates output directory | NO |
| Coverage rows | 199 |
| Unique `report_file` in coverage | 199 |
| Coverage rows agree one-to-one with reports.csv | PASS |

## S3.2 HIGH — F-R4-S03-01: v0.5 validator can assign a neighboring finding's locus

**Locus:** `extract_corpus.py`, generic locus scan and description validation/backfill.

The current extraction sequence first searches up to **1,500 characters after the regex match** for a Locus marker:

```python
pos = m.end()
body_chunk = text[pos:pos+1500]
...
lm = locus_pat.search(body_chunk)
if lm:
    f.locus = ...
```

Later, if the captured description itself is a leaked Locus marker, the validator extracts the current finding's locus **only if `f.locus` is empty**:

```python
if locus_content and not f.locus:
    f.locus = locus_content[:200]
```

That condition is unsafe when the initial 1,500-character scan has already crossed into the next finding and populated `f.locus` from that neighboring finding.

The backfill is also unbounded by the next finding header:

```python
body_lines = text[pos:pos+1000].split('\n')
```

### Minimal reproduction against the shipped v0.5 extractor

Input:

```text
### F-A — - **Locus:** LOCUS A
Substance A is a sufficiently long substantive description for finding A.
### F-B — - **Locus:** LOCUS B
Substance B is a sufficiently long substantive description for finding B.
```

Actual v0.5 extraction:

```text
F-A:
  description = "Substance A is a sufficiently long substantive description for finding A."
  locus       = "LOCUS B"

F-B:
  description = "Substance B is a sufficiently long substantive description for finding B."
  locus       = "LOCUS B"
```

`F-A` silently acquires **F-B's locus**.

This directly contradicts the paper's §3.2 statement that the validator “moves locus content to the locus field.”

### Current-data manifestations consistent with the bug

The regenerated CSV contains chains such as:

- `F-OP43GAN-02`: description `FB-8 row, line 759.`; locus `Correction (ab), line 1172.`
- `F-OP43GAN-03`: description begins `(ab) reads: ...`; locus begins `xz_protocol_trust_roots_PUBLIC.json ...`
- `F-OP43GAN-04`: description ``manifest_digest_note`.``; locus `Section 0.1 ...`

and:

- `F-OP44GAN-01`: description `output in the same run.`; locus `v0.44 entry, append-only correction (am).`
- `F-OP44GAN-02`: description begins `(am) closes ...`; locus begins `v0.44 entry, body repair item (8) ...`

These sequences are consistent with the one-step shift reproduced by the code probe. Exact source-level correction of individual rows requires the source reports, which are not in the R4 packet.

The v0.5 repair did improve superficial metrics:

- empty descriptions fell to **34**;
- no current description has a normalized leading `Locus:` marker.

But those improvements do not establish field correctness. A validator that replaces visible leakage with silent neighboring-locus assignment is a data-integrity regression.

**Severity: HIGH.**

**Required repair:**

1. Bound every per-finding body/locus search at the **next finding-header boundary**.
2. When the captured description is itself a Locus marker, treat that marker as authoritative for the current finding rather than preserving a later scan result.
3. Backfill only from the bounded current-finding body.
4. Add unit tests with consecutive pattern-18/bare-description findings proving that finding A can never acquire finding B's locus.
5. Re-run the corpus and spot-check affected report sequences against source bytes.

## S3.3 Additional description-quality residue

Current `findings.csv` still has **six non-empty descriptions that are severity metadata rather than descriptions**, e.g.:

- `Severity:** HIGH`
- `Severity:** CRITICAL`
- `Severity:** MEDIUM`

These are not counted among the 34 empty descriptions, but they still violate the schema's “First-line description” semantics.

I treat this as supporting evidence for F-R4-S03-01 rather than a separate finding.

## S3.4 MEDIUM — F-R4-S03-02: machine-specific `/home/claude` defaults remain

**Locus:** `extract_corpus.py` configuration block.

The extractor supports:

- `XZ_CORPUS_ARCHIVE_ROOTS`
- `XZ_CORPUS_OUTPUT_DIR`

but still hardcodes four `/home/claude/...` path occurrences as defaults.

Thus a caller who runs the shipped script without producer-specific environment variables inherits private-machine paths. This was an R3 S03 residual and remains unchanged in v0.5.

**Severity: MEDIUM.**

**Required repair:** eliminate producer-machine defaults; require explicit paths or use portable/config-relative defaults.

---

# S4 — Documentation/regression findings and final disposition

## S4.1 LOW — F-R4-S03-03: extractor contains contradictory version stamps

The extractor begins:

```text
XZ Protocol Audit Corpus Extractor v0.5
```

but immediately states:

```text
Versioned: v0.4 (post-R2 three-seat triage absorption).
```

The runtime banner and `summary.json` correctly say v0.5, so this is not a data-count defect, but the shipped construction procedure is internally contradictory.

**Severity: LOW.**

**Required repair:** update the stale docstring line to v0.5/R4 absorption language.

## S4.2 LOW — F-R4-S03-04: pattern-note repair is still technically false

Paper §3.2 now says:

> Patterns 6–9, 13, and 18 match Unicode U+2014 em-dashes; patterns 1–5 and 10–12 match literal `--`.

Pattern 18 is now correctly included, satisfying the narrow R4 repair request. But the second half is false against the regex bytes:

- patterns **1–5** use `[-\u2013\u2014]+` and therefore also accept U+2013/U+2014;
- pattern **11** accepts `-`, `:`, U+2013, or U+2014;
- pattern **12** uses `[-\u2013\u2014]+`;
- only paper pattern **10** in that 10–12 group is constrained to literal `--`.

Synthetic regex probes against the shipped pattern list confirm that paper patterns 1–5, 11, and 12 accept an em dash.

**Severity: LOW.**

**Required repair:** describe the regex classes literally, or remove the parenthetical.

## S4.3 LOW — F-R4-S03-05: output inventory remains inconsistent at the extractor/deposit boundary

The paper now correctly says the script produces:

- four data files;
- plus `extraction.log`.

However:

1. the extractor's own top docstring still lists `reports.csv`, `findings.csv`, `coverage.csv`, and `extraction.log` while omitting `summary.json`;
2. §2.1 says the corpus contains a fifth operational `extraction.log`;
3. §7's deposit inventory does not list `extraction.log`;
4. the R4 packet itself does not ship `extraction.log`.

This is a documentation/inventory inconsistency, not a quantitative data defect.

**Severity: LOW.**

**Required repair:** decide whether `extraction.log` is part of the deposit. If yes, list and ship it; if no, state that it is a generated local operational artifact and make the extractor docstring list all generated outputs accurately.

## S4.4 LOW — F-R4-S03-06: abstract family scope drops the incidental qualifier

The abstract says the 199 reports were produced by systems from **five vendor families**: Anthropic, OpenAI, Google, Moonshot, and Zhipu.

The current family table contains those five core families **plus Perplexity (1) and UNKNOWN (1)**. v1.1 explicitly qualified these as incidental entries; v1.2 removes that qualifier from the abstract.

Because §2.3 discloses the complete distribution, this is a small abstract-scope imprecision rather than a hidden count error.

**Severity: LOW.**

**Required repair:** say “five core vendor families, plus one Perplexity report and one unclassified report,” or equivalent.

---

# R3 S03 continuity closure matrix

For completeness, the prior S03 findings now stand as follows:

| Prior S03 issue | R4 status |
|---|---|
| Abstract scope/count partition | **CLOSED** |
| Era taxonomy/ranges | **CLOSED** |
| 136 vs 102 Class A conflation | **CLOSED** |
| Missing-verdict family attribution | **CLOSED** |
| Duplicate-ID F-EARLY explanation | **CLOSED** |
| Hardcoded producer-machine defaults | **OPEN — MEDIUM** |
| Description/locus validator | **FAILED / REGRESSED — HIGH** |
| R36 speculative mechanism | **CLOSED** |
| Unsupported novelty framing | **CLOSED** |
| Output inventory | **PARTIAL — LOW** |
| Extractor version in summary metadata | **CLOSED** |
| Empty version counts | **CLOSED** |

---

# Final assessment

R4 is the strongest package in the sequence so far on **paper-to-table quantitative honesty**. The central R3 HIGH claims have been repaired correctly, and the shipped aggregates are internally coherent.

The remaining blocker is now narrower but more structural: the attempted v0.5 description cleanup can silently turn visible parsing defects into **wrong finding-to-locus mappings**. Because locus is a primary annotation field used to connect a finding to the artifact region it concerns, cross-finding assignment is not acceptable in a deposit represented as independently verifiable structured evidence.

The correct next repair is not another prose-only absorption. The extractor must introduce a real **per-finding boundary**, re-run the data, and verify the affected rows against source reports.

# **FINAL VERDICT: HALT**

**0 CRITICAL / 1 HIGH / 1 MEDIUM / 4 LOW**

---

# Bismillah ir-Rahman ir-Rahim
