# Bismillah ir-Rahman ir-Rahim

# R0463 -- Model Council Audit Report: GPT 5.4

**Chronological Index:** 83 of 995  
**Date:** 2025  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-PC-R1_gpt54.md  
**Source Format:** md  
**SHA-256:** `13f06e9ebc774af86b8fc9b82d54b7317c7ad9fd3a0cd5cc6e94526aa90a50d9`  

---

## R0463 · Model Council Audit Report: GPT 5.4

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-PC-R1_gpt54.md
- source_format: md
- text_sha256: 13f06e9ebc774af86b8fc9b82d54b7317c7ad9fd3a0cd5cc6e94526aa90a50d9

# Model Council Audit Report: GPT 5.4

## Identity and attestation

- **Model:** GPT 5.4
- **Lineage:** OpenAI
- **Qualifying status:** Qualifying member for Round 1 (non-Claude, non-producer lineage).
- **No-history/no-memory attestation:** "I am an INDEPENDENT, FRESH, MEMORYLESS audit instance on a Model Council. I have NO chat history, NO memory, NO saved skills, NO prior-conversation context, NO carryover from any earlier Bayyinah round, and NO access to any other council member's work."

## Execution status

**Executed.** I read the attached brief and paper in the workspace and executed all five mandatory steps against the attached package ([audit brief](file:///home/user/workspace/council/gpt54/brief.md)), ([paper v0.3](file:///home/user/workspace/council/gpt54/paper_v0.3.md)), ([reproduction script](file:///home/user/workspace/council/gpt54/reproduce_procurement.py)).

## Mandatory execution outputs

### Step 1: `python3 reproduce_procurement.py`

```text
[integrity] sole_source  OK
[integrity] negotiated   OK

Concentration (Table 2), clean vendor rows:
  sole_source  vendors=106 total=$1597506644.98 top1=82.5004% top5=90.5858% top10=94.0642% gini=0.95557  [OK]
  negotiated   vendors=462 total=$3865895209.67 top1=24.0334% top5=36.9178% top10=46.2163% gini=0.81855  [OK]

Addressable base and savings (Table 3), official Table 7 basis:
  savings base Core             $5,658,002,459  @10%=$565,800,246  @20%=$1,131,600,492  [OK]
  savings base Wide             $6,984,040,398  @10%=$698,404,040  @20%=$1,396,808,080  [OK]
  savings base NYCEDC-adjusted  $4,340,052,731  @10%=$434,005,273  @20%=$868,010,546  [OK]

MTA constants carried from converged AllocationAsymmetry (DOI 10.5281/zenodo.21445552):
  FY2024: 13718 records, 2656 vendors, $65189755228.64 face, top10 30.4151%, Gini 0.93117

[note] Concentration is measured on the positive-amount vendor basis; the savings model uses the official Table 7 base. The Negotiated positive basis is about 4.75% ($192.96M) below official (open reconciliation item). This tool measures; it does not judge whether any award should have been competed (refused).

All checks reproduced exactly. Exit 0.
```

### Step 2: `python3 reproduce_procurement.py --selftest`

```text
[integrity] sole_source  OK
[integrity] negotiated   OK
[selftest] perturbing each checked value...
[selftest] perturbed 14 values; missed 0
```

### Step 3: `python3 reproduce_procurement.py --live`

```text
[integrity] sole_source  OK
[integrity] negotiated   OK

Concentration (Table 2), clean vendor rows:
  sole_source  vendors=106 total=$1597506644.98 top1=82.5004% top5=90.5858% top10=94.0642% gini=0.95557  [OK]
  negotiated   vendors=462 total=$3865895209.67 top1=24.0334% top5=36.9178% top10=46.2163% gini=0.81855  [OK]

Addressable base and savings (Table 3), official Table 7 basis:
  savings base Core             $5,658,002,459  @10%=$565,800,246  @20%=$1,131,600,492  [OK]
  savings base Wide             $6,984,040,398  @10%=$698,404,040  @20%=$1,396,808,080  [OK]
  savings base NYCEDC-adjusted  $4,340,052,731  @10%=$434,005,273  @20%=$868,010,546  [OK]

MTA FY2024 cross-check (live re-pull from data.ny.gov):
  MTA FY2024 live: records=13718 vendors=2656 face=$65189755228.64 top10=30.4151% gini=0.93117  [OK]

MTA constants carried from converged AllocationAsymmetry (DOI 10.5281/zenodo.21445552):
  FY2024: 13718 records, 2656 vendors, $65189755228.64 face, top10 30.4151%, Gini 0.93117

[note] Concentration is measured on the positive-amount vendor basis; the savings model uses the official Table 7 base. The Negotiated positive basis is about 4.75% ($192.96M) below official (open reconciliation item). This tool measures; it does not judge whether any award should have been competed (refused).

All checks reproduced exactly. Exit 0.
```

### Step 4: independent recompute with separate code

```text
sole_source vendors=106 total=1597506644.98 top1=82.5004 top5=90.5858 top10=94.0642 top20=97.2606 gini=0.95557
negotiated vendors=462 total=3865895209.67 top1=24.0334 top5=36.9178 top10=46.2163 top20=55.3833 gini=0.81855
savings_core 5658002459 10pct 565800246 20pct 1131600492
savings_wide 6984040398 10pct 698404040 20pct 1396808080
savings_nycedc_adjusted 4340052731 10pct 434005273 20pct 868010546
```

### Step 5: adversarial trap check including the trailing rows

```text
sole_source rows_with_amount=107 total=3195013289.96 top1=50.0000
tail_labels ['TOTAL', 'Source', 'Official report total', 'URL']
negotiated rows_with_amount=463 total=7731790419.35 top1=50.0000
tail_labels ['TOTAL', 'Source', 'Official report total', 'URL']
```

## Assessment

Tier 1 reproduction passed on the attached package: both CSV hashes matched, both subgroup concentration outputs matched, the three savings bases matched, the self-test caught all 14 perturbations, the live MTA pull matched 13,718 records / 2,656 vendors / $65,189,755,228.64 / Gini 0.93117, and the adversarial trap produced the expected near-doubling with top-1 exactly 50% when the trailing rows were wrongly included ([reproduction script](file:///home/user/workspace/council/gpt54/reproduce_procurement.py)), ([independent recompute](file:///home/user/workspace/council/gpt54/independent_recompute.py)), ([MTA open data](https://data.ny.gov/it/it/Transparency/MTA-Procurement-Report-All-/gpsc-qqsz)).

The official FY25 Table 7 figures are Sole Source 126 / $1,599,150,768, Negotiated Acquisition 962 / $4,058,851,691, and Emergency 106 / $1,326,037,939 ([FY25 Annual Summary Contracts Report](https://comptroller.nyc.gov/wp-content/uploads/2025/10/FY25-AnnualSummaryContractsReport.pdf)).

The cited Comptroller Appendix 1 workbook was directly accessible during this audit at the published URL, and the accessible workbook itself contains 935 FY25 Negotiated Acquisition rows totaling $3,865,895,209.68 and 115 FY25 Sole Source rows totaling $1,597,506,644.98, so the observed gaps versus Table 7 are absent from the accessible Appendix 1 file itself rather than arising from blank, zero, or negative rows inside that file ([Appendix 1 workbook](https://comptroller.nyc.gov/wp-content/uploads/2025/10/Appendix-1-Parent-Contracts.xlsx)), ([workbook reconciliation script](file:///home/user/workspace/council/gpt54/workbook_reconciliation.py)).

That means the paper is correct that zero or blank amounts cannot explain the $192.96M Negotiated gap and that dropped negatives cannot explain it either, but the most defensible explanation from the evidence now in hand is broader than the paper states: the accessible Appendix 1 export is incomplete relative to Table 7 for Negotiated Acquisition, with 27 contracts and $192,956,481.32 missing from the accessible workbook, and the specific mechanism of "positive-value contracts unattributable to a distinct vendor name" remains plausible but unverified ([paper v0.3](file:///home/user/workspace/council/gpt54/paper_v0.3.md)), ([Appendix 1 workbook](https://comptroller.nyc.gov/wp-content/uploads/2025/10/Appendix-1-Parent-Contracts.xlsx)), ([FY25 Annual Summary Contracts Report](https://comptroller.nyc.gov/wp-content/uploads/2025/10/FY25-AnnualSummaryContractsReport.pdf)).

The paper does adequately disclose that Negotiated concentration is computed on about 95.25% of the official subgroup base, both in Section 4.4 and in the Section 5.0 note on mixed bases ([paper v0.3](file:///home/user/workspace/council/gpt54/paper_v0.3.md)).

Under adversarial reading, I did not find a sentence that flatly says the City is already losing, or will definitely save, the headline amount as an established fact; the abstract, Section 5.0, Section 7, and the conclusion repeatedly re-state that the figure is a conditional planning range gated on a pilot ([paper v0.3](file:///home/user/workspace/council/gpt54/paper_v0.3.md)).

I also did not find a sentence accusing any specific award or vendor of impropriety; the paper stays within structural interpretation more than accusation, even when it edges close to policy advocacy ([paper v0.3](file:///home/user/workspace/council/gpt54/paper_v0.3.md)).

House-style and internal-consistency checks passed on the requested points: I found no em-dash or en-dash characters, the paper uses the brand "BayyinahEnterprise," it describes the MTA reproduction as nine rounds, and I did not find an internal versioning conflict with v0.3 ([paper v0.3](file:///home/user/workspace/council/gpt54/paper_v0.3.md)).

## Findings table

| Identifier | Severity | Locus | Substance as surface-vs-substrate divergence | Disposition | Cross-reference |
|---|---|---|---|---|---|
| F-PC-R1-001 | HIGH | Section 5.0 note on bases; Table 3 adjusted row | **Surface:** the note says the NYCEDC-adjusted row "mixes the two bases by about $2M -- immaterial." **Substrate:** official adjusted core is $4,340,052,731, while a fully positive-basis adjusted core is $4,145,452,126.65, a gap of $194,600,604.35; that shifts the 10% and 20% sensitivities by about $19.46M and $38.92M, so the note understates the basis effect by roughly two orders of magnitude ([paper v0.3](file:///home/user/workspace/council/gpt54/paper_v0.3.md)), ([adjusted-base check](file:///home/user/workspace/council/gpt54/independent_recompute.py)). | Revise the note and either present both adjusted rows explicitly or keep a single basis throughout Section 5 and Table 3. | Section 5.0, line 136; Table 3. |
| F-PC-R1-002 | MEDIUM | Section 4.4 explanation of the $192.96M Negotiated gap; Section 3.1 data-source note | **Surface:** the paper says exact reconciliation requires Appendix 1 access that was blocked by HTTP 403 and identifies unattributable positive-value contracts as the likely mechanism. **Substrate:** the cited Appendix 1 workbook was directly reachable during this audit and the accessible file itself already falls short of Table 7 by 27 contracts and $192,956,481.32 for Negotiated Acquisition, with no blank, zero, or negative rows inside the accessible FY25 negotiated subset; the evidence therefore supports an Appendix 1 versus Table 7 divergence or upstream omission more directly than a vendor-name omission inside the accessible workbook ([paper v0.3](file:///home/user/workspace/council/gpt54/paper_v0.3.md)), ([Appendix 1 workbook](https://comptroller.nyc.gov/wp-content/uploads/2025/10/Appendix-1-Parent-Contracts.xlsx)), ([FY25 Annual Summary Contracts Report](https://comptroller.nyc.gov/wp-content/uploads/2025/10/FY25-AnnualSummaryContractsReport.pdf)). | Update Section 4.4 to reflect current accessibility, state that the gap is absent from the accessible Appendix 1 workbook itself, and downgrade the specific mechanism from likely to unverified. | Sections 3.1 and 4.4; Reference list Appendix 1 entry. |
| F-PC-R1-003 | MEDIUM | Abstract; Sections 4.5, 5.0, 9; Table 3 | **Surface:** the paper keeps the savings number linguistically conditional. **Substrate:** the model still applies literature price deltas across the entire official core and wide bases before establishing what share of those dollars has a real alternative-vendor counterfactual, even though the paper's own concentration analysis shows that large visible portions are designated-intermediary or quasi-governmental spend; the result is a planning range that is methodologically over-broad even if not rhetorically over-asserted ([paper v0.3](file:///home/user/workspace/council/gpt54/paper_v0.3.md)). | Bound the addressable share before applying the 10% to 20% rates, or move the full-base arithmetic to a secondary sensitivity and headline only vendor-screened or pilot-conditioned estimates. | Abstract; Sections 4.5, 5.0, 9; Table 3. |

## Verdict

**NON-PASS.** The package was executed successfully and the mandatory reproduction steps all ran, but the audit still contains one HIGH finding on the Section 5.0 basis note and two MEDIUM findings on the Negotiated-gap explanation and the breadth of the savings extrapolation ([audit brief](file:///home/user/workspace/council/gpt54/brief.md)), ([paper v0.3](file:///home/user/workspace/council/gpt54/paper_v0.3.md)).

Because this qualifying member found a HIGH issue, this audit does **not** satisfy the brief's zero-CRITICAL/zero-HIGH requirement for a qualifying PASS, so the convergence-bearing consecutive qualifying-PASS count remains **ZERO** ([audit brief](file:///home/user/workspace/council/gpt54/brief.md)).

---

# Bismillah ir-Rahman ir-Rahim
