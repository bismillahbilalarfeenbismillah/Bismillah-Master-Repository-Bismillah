# Bismillah ir-Rahman ir-Rahim

# R0195 -- XZ Empirical R4 — S03 GPT-5.6 Sol Final Audit Report

**Chronological Index:** 568 of 995  
**Date:** 2026-08-19  
**Section:** IV. XZ Protocol  
**Source File:** XZ_EMPIRICAL_R4_S03_GPT_REPORT.md  
**Source Format:** md  
**SHA-256:** `a98bf98580e1188e160ec2d1684539b0d55d7d4fe18332040b3fc9502ef8dfb2`  

---

## R0195 · XZ Empirical R4 — S03 GPT-5.6 Sol Final Audit Report

- section: IV. XZ Protocol
- source_file: XZ_EMPIRICAL_R4_S03_GPT_REPORT.md
- source_format: md
- text_sha256: a98bf98580e1188e160ec2d1684539b0d55d7d4fe18332040b3fc9502ef8dfb2

# XZ Empirical R4 — S03 GPT-5.6 Sol Final Audit Report

**Artifact audited:** *Empirical Results from 31 Rounds of Multi-Model Structural Honesty Audit* v1.3
**Packet:** `XZ_EMPIRICAL_R4_DISPATCH_S03_GPT.zip`
**Seat:** S03
**Model:** GPT-5.6 Sol
**Role:** ADVERSARIAL ADVISORY
**Mode:** FRESH
**Audit date:** 2026-08-19
**Prior S03 verdict:** R3 HALT — 3 HIGH, 3 MEDIUM, 1 LOW

# VERDICT: HALT

Version 1.3 successfully absorbs most of the explicitly requested R3 surface repairs. In particular:

- R28 no longer falsely imports the R29 `"Class A -- String N, Position M"` wording.
- R10 is now consistently identified as `REPORT-METADATA`.
- `classify_migration.py` now ships.
- the unsupported phrase `"per-report depth"` is gone.
- the `Other/unclassified` table description now matches the classifier's basic behavior.
- all principal corpus counts and migration layer totals still regenerate.

The publication gate nevertheless remains **HALT** because two substantive HIGH-level evidentiary defects from R3 remain unresolved:

1. the headline **25/25 Class A recurrence** still depends on one externally asserted round, R15, for which the packet supplies no direct witness and the cited Heartbeat deposit is still pending; and
2. the **102-row migration analysis remains restricted to extractor-tagged Class A rows even though the same corpus contains 53 additional rows with empty class fields whose descriptions explicitly identify them as Class A**. A conservative sensitivity run over those additional rows materially changes every published layer count.

A new reproducibility defect also appears in the R4 repair: the shipped classifier does **not** exactly regenerate the shipped migration CSV. The layer assignments are identical, but 21 `coding_rationale` cells differ, making the paper's statement that the CSV was “produced by `classify_migration.py`” false as packaged.

---

## 1. Packet integrity

All eight files listed in `PACKET_SHA256SUMS.txt` match their declared SHA-256 digests:

- `AUDIT_BRIEF.txt`
- `XZ_EMPIRICAL.md`
- `findings.csv`
- `reports.csv`
- `summary.json`
- `recurrence_witness.csv`
- `migration_classification.csv`
- `classify_migration.py`

No packet-integrity failure was found.

---

## 2. Machine-rederived baseline

Direct reconstruction from `findings.csv` and `reports.csv` gives:

| Quantity | Re-derived |
|---|---:|
| Total report rows | 199 |
| Total finding rows | 832 |
| R7–R31 report rows | 68 |
| R7–R31 finding rows | 428 |
| Full-corpus rows with `finding_class == Class A` | 136 |
| R7–R31 rows with `finding_class == Class A` | 102 |
| R7–R31 rounds with tagged Class A | 19 |
| R7–R31 rounds without tagged Class A | R9, R10, R11, R15, R28, R29 |
| R7–R31 report-count range | 1–9 per round |
| Median reports per R7–R31 round | 3 |
| R7–R31 family reports | OpenAI 30; Anthropic 24; Google 11; Moonshot 3; Zhipu 0 |
| R7–R31 verdicts | HALT 63; CONDITIONAL PASS 3; PASS 1; missing 1 |
| R7–R31 severities | CRITICAL 15; HIGH 224; MEDIUM 104; LOW 67; INFORMATIONAL 13; missing 5 |
| Findings with no class tag | 625/832 = 75.1% |
| Findings with no extracted round | 223/832 = 26.8% |
| Findings with empty description | 40/832 = 4.8% |

The paper's published arithmetic for these quantities is consistent with the supplied structured files.

---

## 3. R3 absorption matrix

| R3 finding | R4 status | Assessment |
|---|---|---|
| **F-XE-R3-01 — R15 makes 25/25 conditional** | **OPEN — HIGH** | R15 remains `ASSERTED`, with no in-packet witness and a pending external deposit. The paper still states 25/25 categorically. |
| **F-XE-R3-02 — migration population excludes description-level Class A evidence** | **OPEN — HIGH** | The classifier still selects only rows where `finding_class == "Class A"`. The 53 explicit description-level Class A rows with empty class fields remain excluded. No sensitivity analysis is reported. |
| **F-XE-R3-03 — migration classifier/reproducibility** | **PARTIAL** | The script now ships and reproduces all layer assignments and aggregates, but it does not exactly reproduce the shipped CSV, still lacks a stable source-row key, and has undocumented score ties. |
| **F-XE-R3-04 — R10/R28 recurrence metadata** | **CLOSED** | R10 now says `REPORT-METADATA`; R28 no longer uses the R29 string-position wording. |
| **F-XE-R3-05 — “per-report depth”** | **CLOSED as requested** | The phrase is removed. A weaker interpretation issue remains in §2.2; see F-XE-R4-05. |
| **F-XE-R3-06 — pending external methods/protocol evidence** | **OPEN — MEDIUM** | The manuscript still says corpus/procedure are “deposited separately” while References 10–12 remain “deposit pending.” |
| **F-XE-R3-07 — Other/unclassified description** | **CLOSED** | The table now correctly says “No layer-specific keyword match, opaque locus, or empty locus.” |

---

# 4. Binding R4 findings

## F-XE-R4-01 — HIGH — The headline 25/25 recurrence remains conditional on unverified R15 evidence

`recurrence_witness.csv` now cleanly documents 25 round rows:

- 19 `COMPUTED`
- 3 `DESCRIPTION-LEVEL`
- 2 `REPORT-METADATA`
- 1 `ASSERTED`

The sole `ASSERTED` row is R15:

> `No in-packet evidence; ASSERTED from Heartbeat paper`

The manuscript likewise says:

> “R15: No in-packet evidence.”

Reference 12 is still:

> `Heartbeat paper: (deposit pending)`

This is transparent, but transparency does not make the external assertion independently verifiable. The strongest packet-supported statement is therefore:

> **24 of 25 rounds have direct in-packet evidence; R15 is externally asserted. Conditional on the R15 source, the sequence is 25/25.**

Instead, the abstract, §3.1, and conclusion continue to state categorically that every R7–R31 round contained Class A.

The Laplace value `26/27 = 0.963` is arithmetically correct only **conditional on accepting R15 as the 25th success**.

### Required repair

Either:

1. ship or stably cite the exact R15 source witness, including a report/finding locator and evidence establishing byte-false/Class A status; or
2. change the primary result everywhere to a conditional formulation, e.g. “24/25 directly evidenced in this packet; 25/25 conditional on the external R15 classification.”

Until then, the paper's central empirical result exceeds the independently auditable packet.

---

## F-XE-R4-02 — HIGH — The migration analysis still uses an incomplete Class A population

The shipped script selects migration rows only when:

```python
row['finding_class'] == 'Class A'
```

That produces the published 102-row migration dataset.

However, the same R7–R31 `findings.csv` contains **53 additional rows** satisfying both of the following conservative conditions:

- `finding_class` is empty; and
- the description explicitly begins with a Class A label, including forms such as `Class A`, `/ Class A`, or `-- Class A`.

These include explicit Class A rows in R9, R11, R14, R20–R22, R24–R25, and R29–R31.

This remains an evidentiary asymmetry:

- description-level Class A evidence is accepted for the **primary recurrence result**;
- the same form of evidence is excluded from the **secondary migration result**.

### Sensitivity result

Applying the shipped layer-classification rule to the 53 omitted explicit Class A rows yields:

| Layer | Published 102-row count | Additional explicit-Class-A rows | Conservative 155-row sensitivity total |
|---|---:|---:|---:|
| Code/CI | 41 | 13 | 54 |
| Cross-layer consistency | 23 | 4 | 27 |
| Other/unclassified | 21 | 27 | 48 |
| Methodology/dispatch | 11 | 6 | 17 |
| Provenance/amendment | 6 | 3 | 9 |

This sensitivity run is deliberately conservative. It does **not** claim that 155 is the final true Class A count. It establishes something narrower and decisive: **102 is not the complete observable Class A population under the paper's own willingness to accept explicit description-level Class A evidence.**

The additional rows also expand the observed-round coverage of several layers. The qualitative conclusion that defects occur across all five layers survives, but the quantitative migration trajectory changes materially.

### Direct extractor inconsistency

The corpus also contains contradictory class extraction in the opposite direction:

- `F-S05-55-05` has structured `finding_class = Class A`, so it is included in the 102-row migration set, but its description is `-- Class B`.
- `F-S05-55-01` and `F-S05-55-02` have descriptions `-- Class A`, but their structured class fields are empty and they are excluded.

There is also at least one row with `finding_class = Class B` whose description explicitly begins `Class A`.

These are exactly the kinds of inconsistencies that require a reconciled class-selection rule before migration can be presented as a population-level result.

### Required repair

Choose one of two publication-safe approaches:

1. **Reconcile the Class A universe.** Repair/re-run extraction, resolve explicit field/description conflicts, and regenerate migration over the reconciled set; or
2. **Narrow the claim explicitly.** Rename the analysis throughout as the migration of the **102 extractor-tagged Class A rows**, disclose the 53 explicit description-level rows that are excluded, and include a sensitivity table demonstrating how the layer distribution changes when they are added.

Without one of these repairs, the secondary result remains publication-blocking.

---

## F-XE-R4-03 — MEDIUM — The shipped classifier does not exactly produce the shipped migration CSV

R4 correctly adds `classify_migration.py`, and executing it against the shipped `findings.csv` reproduces:

- all 102 selected rows;
- every `migration_layer` assignment;
- the published layer counts `41 / 23 / 21 / 11 / 6`;
- every non-rationale output field.

But it does **not** reproduce the shipped CSV exactly.

For **21 rows**, the shipped CSV contains:

> `No layer-specific terms matched`

whereas the current script emits:

> `No layer-specific keyword match`

Thus the manuscript statement that `migration_classification.csv` is:

> “produced by `classify_migration.py`”

is false for the bytes and semantic cell values actually shipped.

This does not alter the layer table, so it is not independently a HIGH result defect, but it defeats exact artifact provenance.

### Additional reproducibility residuals

- `migration_classification.csv` has **102 rows but only 97 unique `finding_id` values**.
- Five finding IDs are duplicated across ten R19 rows.
- The script does not output `report_file` or a stable corpus-row ID.
- Seven classified rows have ties for the highest layer score. Python dictionary insertion order implicitly resolves those ties, but the paper does not state this tie-breaking rule.

### Required repair

- regenerate `migration_classification.csv` from the exact shipped script, or change the script so that it produces the currently shipped CSV;
- add a stable source-row identifier, preferably `report_file` plus `finding_id` or an explicit corpus row ID;
- document tie handling.

---

## F-XE-R4-04 — MEDIUM — Methods/deposit claims remain internally inconsistent

Section 2.3 says:

> “The corpus, its construction procedure, and its dataset card are deposited separately.”

But the references still say:

- `XZ Corpus: (deposit pending)`
- `XZ Protocol v0.75: (deposit pending)`
- `Heartbeat paper: (deposit pending)`

The R4 packet also does not ship `extract_corpus.py`, despite the paper's specific claim that v0.6 applies 18 regex patterns.

Similarly, §4.4 makes substantive claims about XZ Protocol v0.75 while that source remains pending in the references.

These claims may be correct, but the current package does not support the stronger wording “deposited separately.”

### Required repair

Either provide stable deposits/DOIs or change the prose to say that the supporting corpus/protocol/Heartbeat materials are **pending deposit** and are not independently reconstructible from this paper packet.

---

## F-XE-R4-05 — MEDIUM — The finding-rate interpretation remains unsupported and contains a textual artifact

Section 2.2 now says:

> “the carrying families.* lower rates represent genuinely independent verification.”

Two problems remain:

1. `.*` is an apparent regex/editing artifact that should not appear in publication prose.
2. The extracted finding-rate numbers do not establish that a lower findings-per-report rate “represents” independence. Independence follows, if at all, from governance, vendor separation, and execution conditions, not from the numerical rate.

There is also only one observed carrying family in R7–R31: Moonshot has 3 reports; Zhipu has 0. So plural language about the carrying families' observed rates is imprecise.

### Required repair

Keep the numerical statement descriptive:

> “Moonshot produced 3 R7–R31 reports at 1.3 extracted findings per report; Zhipu produced none in this window.”

Then discuss independence separately as a governance property, not as an inference from the rate.

---

## F-XE-R4-06 — LOW — The migration method prose does not disclose score-tie behavior

Seven of the 102 migration rows have equal maximum scores across two or more candidate layers.

Examples include ties between:

- Code/CI and Provenance/amendment;
- Code/CI and Methodology/dispatch;
- Cross-layer consistency and Methodology/dispatch;
- Provenance/amendment and Methodology/dispatch.

The script resolves ties implicitly by the insertion order of the `scores` dictionary because it uses:

```python
max(scores, key=scores.get)
```

The manuscript says only that “the highest-scoring layer is assigned,” which is incomplete when multiple layers share the maximum.

The shipped code makes the result executable, so this is not a major result failure, but the method should state the deterministic tie rule.

---

# 5. Requested R4 verification axes

## Axis 1 — R28 witness correction

**PASS.**

The R28 witness no longer says `"Class A -- String N, Position M"`. It now describes byte-false content such as phantom repair/fail-open behavior and identifies the evidence as description-level plus external assertion.

## Axis 2 — R10 evidence type

**PASS.**

Both the paper and `recurrence_witness.csv` now classify R10 as `REPORT-METADATA`. The cited R10 row in `reports.csv` has `class_a_count = 4`.

R11 is likewise now consistently represented as report-metadata evidence with `class_a_count = 3`.

## Axis 3 — migration script ships and is referenced

**PARTIAL PASS.**

`classify_migration.py` ships and is cited in §3.2. It reproduces every migration-layer assignment and table aggregate.

It does **not** exactly reproduce the shipped CSV because 21 rationale cells differ, and the script still analyzes only extractor-tagged Class A rows.

## Axis 4 — all numbers still match

**PASS for the stated 102-row subset and main corpus arithmetic.**

The principal corpus counts, severity table, verdict table, family counts, seat-report range, recurrence tagged counts, and migration layer totals all re-derive.

**Not a PASS for population completeness.** The quantitative migration table is valid only for the extractor-tagged 102-row subset.

## Axis 5 — no “per-report depth”

**PASS.**

The phrase is gone. The residual rate/independence interpretation is separately identified in F-XE-R4-05.

---

# 6. What v1.3 now establishes robustly

The packet supports the following claims without material arithmetic dispute:

1. The structured corpus contains 199 report rows and 832 finding rows.
2. R7–R31 contains 68 report rows and 428 finding rows.
3. Exactly 102 R7–R31 rows have the structured extractor field `finding_class = Class A`.
4. Those 102 tagged rows occur across 19 rounds.
5. Five additional non-tagged rounds have direct description-level or report-metadata evidence of Class A/byte-false substance.
6. R15 is explicitly external/ASSERTED rather than computed from the packet.
7. The shipped classifier reproduces the 102-row **layer assignments** and their published `41/23/21/11/6` aggregate.
8. The 102-row tagged subset exhibits recurrence across all five published migration layers.
9. The severity, verdict, family, and report-count tables are reproducible.
10. The paper now treats the Gödel comparison as an analogy rather than a theorem or proof of structural inevitability.

The strongest defensible primary-result wording remains:

> **Direct in-packet evidence supports Class A/byte-false recurrence in 24 of 25 rounds R7–R31. R15 is externally asserted; conditional on that external classification, the sequence is 25/25.**

The strongest defensible secondary-result wording is:

> **Among the 102 R7–R31 findings tagged `Class A` by the structured extractor, the shipped keyword classifier assigns findings across all five locus layers and shows late recurrence in previously observed layers. This tagged-subset analysis excludes additional explicit description-level Class A rows and therefore should not be presented as a complete Class A migration population without reconciliation or sensitivity analysis.**

---

# 7. Publication gate

## HALT conditions

The publication gate remains closed on two HIGH findings:

1. **F-XE-R4-01:** provide a direct/stable R15 witness or make the 25/25 result explicitly conditional everywhere.
2. **F-XE-R4-02:** reconcile the migration Class A population or explicitly scope the result to the 102 extractor-tagged rows and publish the omitted-row sensitivity analysis.

## Required non-blocking repairs

- Synchronize `classify_migration.py` and `migration_classification.csv`.
- Add a stable source-row key and state tie-breaking.
- Correct the pending-deposit language.
- Remove the `.*` artifact and decouple rate from independence interpretation.

---

# FINAL JUDGMENT: HALT

R4 is materially stronger than R3 and closes the requested R28, R10, “per-report depth,” and `Other/unclassified` repairs. The migration algorithm is now executable and its **layer assignments** reproduce.

The remaining blockers are not cosmetic. They concern the evidentiary basis of the paper's two headline results:

- the primary 25/25 recurrence still contains one unverified external success; and
- the secondary migration analysis still characterizes only the extractor-tagged subset while excluding dozens of explicit Class A descriptions accepted as valid evidence elsewhere in the same paper.

The manuscript is close to an auditable form, but the current v1.3 packet does not yet support an unconditional PASS.

---

# Bismillah ir-Rahman ir-Rahim
