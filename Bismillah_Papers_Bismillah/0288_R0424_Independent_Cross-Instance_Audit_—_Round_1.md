# Bismillah ir-Rahman ir-Rahim

# R0424 -- Independent Cross-Instance Audit — Round 1

**Chronological Index:** 288 of 995  
**Date:** 2026-07-19  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-AA-R1_gpt_report.md  
**Source Format:** md  
**SHA-256:** `72f36e7207b4ff425f2e56b18f71128f0dd824559a8da3f41b0b42efaa93a0fd`  

---

## R0424 · Independent Cross-Instance Audit — Round 1

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-AA-R1_gpt_report.md
- source_format: md
- text_sha256: 72f36e7207b4ff425f2e56b18f71128f0dd824559a8da3f41b0b42efaa93a0fd

# Independent Cross-Instance Audit — Round 1

**Artifact:** *Bayyinah: Public-Ledger Allocation and Asymmetric-Measure Audits* (v0.1 corrected)
**Audit date:** 2026-07-19
**Auditor:** OpenAI GPT-5.6 Thinking
**Producing lineage stated by artifact:** Bilal Syed Arfeen / BayyinahEnterprise, with Claude (Anthropic) analytical assistance
**Round status:** **NON-PASS**
**Severity count:** **0 CRITICAL / 3 HIGH / 3 MEDIUM / 3 LOW / 0 INFO**

## 1. Independence attestation

I am an OpenAI model instance, not the Claude/Anthropic model lineage credited in the drafting of the note, and I had no role in producing the submitted artifact or reproduction package. The brief's cross-lineage independence condition therefore holds. The package does not provide the complete private rubric needed for me to certify a separate “Tier 1 auditor” designation; this report attests independence and competence of the work performed, not a framework label whose qualification rules were not supplied.

## 2. Verdict

**Round 1 does not pass.** The pass criterion is zero CRITICAL and zero HIGH findings. This round returns three HIGH findings, so it cannot count toward the two-round convergence gate.

**Direct answer to the requested controlling question:** **Yes. The note claims several things its data does not support in their current wording.** The exact arithmetic on `contract_amount` is reproducible, but:

1. it is presented as FY2024 spending/allocation even though `contract_amount` is the full value of a contract, including multi-year contracts awarded long before FY2024;
2. the 3.95% prime-vendor contract-value share is presented as the operative dollar substrate for New York MWBE utilization goals, although the governing framework concerns annual procurement, direct and indirect participation, contract-specific eligibility, and waivers; and
3. a competitive-process “pass” is declared without testing the MTA's operative procurement guidelines, waiver conditions, exception documentation, or coding accuracy.

These are surface-versus-substrate divergences, not arithmetic discrepancies.

## 3. Audit coverage and execution limits

Completed:

- inspected the brief, note, companion, snapshot, manifest, and reproduction script;
- verified the snapshot hash and row count;
- ran the supplied script offline;
- independently recomputed every Section 4 headline statistic from the frozen rows without importing the supplied calculation functions;
- recomputed the same measures using `amount_expended_for_fiscal_year`;
- tested award-year composition, conservative cross-year repeat fingerprints, missing/zero amounts, vendor aggregation, negative values, and Gini implementation;
- checked official field definitions, the governing procurement statute, MWBE goal structure, data-source provenance, PARIS reporting mechanics, and the capital-data schemas.

Not completed in this environment:

- the supplied `--live` request failed at DNS resolution, so a fresh live aggregate was not obtained through the script;
- the live row-level `project_number` join among the capital tables was not re-executed. The dataset schemas support the corrected claim, but functional join confirmation remains carried from the companion's EV-2 rather than independently reproduced here.

These uncompleted legs do not change the non-pass: the HIGH findings arise from the frozen rows, official field definitions, and governing legal structure. They must nevertheless be rerun in the corrected resubmission round.

## 4. Reproduction results

### 4.1 Package integrity

- Snapshot rows: **37,988**, matching the manifest.
- Snapshot SHA-256: **`9aefc01789854e79fa07d19484bc14be7a899ec7856b8c79fd4994629fdf0f09`**, matching the manifest.
- The snapshot bytes are canonical compact JSON under the manifest's stated convention.
- The supplied script reproduces its stated output exactly.

### 4.2 Exact reproduction on the selected `contract_amount` measure

| Quantity | Independent result | Note result | Status |
|---|---:|---:|---|
| FY2024 records | 13,718 | 13,718 | Match |
| Sum of `contract_amount` | $65,189,755,228.64 | $65.19B | Match |
| Positive-amount records | 12,322 | 12,322 | Match |
| Excluded missing/zero records | 1,396 (10.176%) | about 1,400 / roughly 10% | Rounded match |
| Competitive `contract_amount` share | 92.2197% | 92.2% | Match |
| MWBE count share | 18.7345% | 18.7% | Match |
| MWBE `contract_amount` share | 3.9532% | 3.95% | Match |
| Count/contract-value ratio | 4.7391x | 4.7x | Match |
| Top 5 / 10 / 20 shares | 22.143% / 30.415% / 41.777% | 22.1% / 30.4% / 41.8% | Match |
| Distinct vendor strings | 2,656 | 2,656 | Match |
| Gini | 0.9311677 | 0.931 | Match |

No negative `contract_amount` records were present. Basic case/whitespace vendor normalization does not materially alter the concentration result.

### 4.3 Measure-semantic recomputations

The official dataset defines `contract_amount` as the **total value of the contract**, while `amount_expended_for_fiscal_year` is the amount expended under the contract during that fiscal year.

On the same FY2024 rows:

- annual expenditures total **$8,170,228,558.54**, not $65.19B;
- prime-MWBE annual expenditures are **$576,915,678.94**, or **7.0612%**;
- the MWBE count-to-annual-expenditure ratio is **2.653x**, not 4.739x;
- competitive annual expenditures are **89.6533%**;
- state-contract and non-contract-purchase-order categories, which contribute no `contract_amount` in this extract, contribute **5.6175%** of annual expenditures combined.

The prime-MWBE annual-expenditure shares are **4.2468% (FY2022), 6.2714% (FY2023), and 7.0612% (FY2024)**. A count-versus-dollar asymmetry remains, but its magnitude and three-year trajectory are materially different.

### 4.4 Stock/flow and repeated-reporting diagnostics

Within the FY2024 report:

- **91.6876%** of the summed `contract_amount` belongs to records whose award date precedes 2024;
- only **8.3124%** belongs to records with a 2024 award date;
- award years extend back to **1984**;
- an exact full-field fingerprint finds **2,056 FY2024 rows (14.99%)**, carrying **$7.643B (11.72%)**, also present in the FY2022 or FY2023 snapshot. This is a conservative lower bound because the extract lacks a stable transaction identifier and field edits can hide repeats.

Thus $65.19B is not a clean annual flow of FY2024 awards or expenditures. It is the stock of total contract values reported in the FY2024 annual procurement file.

## 5. Findings

### F-AA-R1-01 — HIGH

**Identifier:** F-AA-R1-01
**Severity:** HIGH
**Locus:** Abstract; Sections 4 introductory paragraph, 4.1, 4.2, 4.3, 6, and 8; phrases including “FY2024 contract dollars,” “dollar volume in FY2024,” “largest awards,” and the three-year persistence interpretation.
**Substance — surface versus substrate:** The surface presents the $65.19B sum and its derived shares as FY2024 procurement spending/allocation. The substrate field is `contract_amount`, officially defined as the contract's total value, and 91.69% of the FY2024 sum comes from contracts awarded before 2024. Repeated multi-year contracts also recur across annual report vintages. The statistic is reproducible, but its annual-flow interpretation is not.
**Disposition:** **REQUIRES CORRECTION.** Choose and name the estimand. For annual spending, use `amount_expended_for_fiscal_year`. For awards made during 2024, filter on `award_date` and address missing dates. If retaining `contract_amount`, call it the total face value of contracts appearing in the FY2024 report, remove annual-spending/allocation language, and substantially narrow the persistence claim. Recompute all process, MWBE, concentration, and Gini figures on the chosen estimand. Add multi-year carryover and repeat-reporting limitations.
**Cross-reference:** Official MTA dataset data dictionary; ABO procurement-data limitations; independent recomputation §§4.3–4.4; F-AA-R1-02 and F-AA-R1-03.

### F-AA-R1-02 — HIGH

**Identifier:** F-AA-R1-02
**Severity:** HIGH
**Locus:** Abstract; Sections 2, 4.2, 4.4, and 6; especially the statements that 3.95% is “the relevant substrate,” “fewer than four cents on the dollar,” and that the count figure is the “short measure.”
**Substance — surface versus substrate:** The surface treats the `vendor_is_a_mwbe` share of total prime-contract face value as the operative measure against New York MWBE utilization goals. The governing substrate is more qualified: goals concern annual procurement and direct and indirect participation; contract-specific goals depend on available subcontract opportunities and disparity-study categories; participation may be credited through primes, subcontractors, and joint ventures; and waivers/exemptions matter. The dataset's binary prime-vendor flag cannot establish goal attainment or the full utilization denominator. On the closer annual-expenditure field, the prime-MWBE share is 7.06%, not 3.95%, but even 7.06% remains incomplete because indirect participation and goal-eligible spend are absent.
**Disposition:** **REQUIRES CORRECTION.** Recast 18.7% versus 3.95% as a descriptive prime-vendor count-versus-total-contract-value statistic, not the operative New York goal measure. To test declared-goal correspondence, obtain contract-specific or agency utilization data including annual eligible expenditures, certified prime and subcontract participation, industry/category goals, exemptions, and waivers. Until then, remove “honest measure,” “short measure,” “operative substrate,” and any implied goal-compliance inference. Add prime-only, eligibility, subcontracting, and waiver limitations.
**Cross-reference:** New York Executive Law §313 and related Article 15-A reporting provisions; independent recomputation §4.3; F-AA-R1-01.

### F-AA-R1-03 — HIGH

**Identifier:** F-AA-R1-03
**Severity:** HIGH
**Locus:** Sections 2, 4.1, and 4.4; the declared rule “contracts are competitively bid unless an exception is documented” and the conclusion that the process rule receives a “pass.”
**Substance — surface versus substrate:** The surface claims correspondence between a declared procurement rule and operative behavior. The substrate shows only the authority-supplied `award_process` category and value composition. New York Public Authorities Law §2879 requires each authority to adopt its own procurement guidelines, including competitive-selection provisions and circumstances for waiving competition. The note does not identify the operative MTA guideline, test whether each noncompetitive award fits a permitted exception, verify required documentation/approval, or validate the authority's coding. A high competitive share does not prove compliance with the declared rule and no universal pass threshold is established.
**Disposition:** **REQUIRES CORRECTION.** Report the competitive/noncompetitive composition as a descriptive Tier-2 statistic only. Withhold “pass,” “substrate matches surface,” and rule-compliance language unless the MTA's operative guidelines, thresholds, exception categories, waiver records, and approval/documentation requirements are elicited and tested transaction-by-transaction or through a defensible sample.
**Cross-reference:** New York Public Authorities Law §2879; official `award_process` data dictionary; F-AA-R1-01.

### F-AA-R1-04 — MEDIUM

**Identifier:** F-AA-R1-04
**Severity:** MEDIUM
**Locus:** Sections 3, 7, and 8; companion Verification Status; audit brief description of `gpsc-qqsz` as “the primary source itself.”
**Substance — surface versus substrate:** The surface identifies `gpsc-qqsz` as the primary MTA source. The portal identifies it as a community-created view based on the statewide authority procurement dataset and warns that New York State did not review or approve modifications. A first-party MTA-attributed dataset, `twsw-2mqa`, is separately published and more recently updated. The community view may accurately reflect official submitted data, but provenance is overstated.
**Disposition:** **REQUIRES CORRECTION.** Freeze and reproduce from the official MTA-attributed dataset or the official ABO statewide dataset filtered to MTA, then compare with `gpsc-qqsz`. Describe `gpsc-qqsz` accurately as a derived community view if retained. Record the source dataset ID, metadata version, query, retrieval time, and any row/schema divergence.
**Cross-reference:** Official Open Data metadata for `gpsc-qqsz`, `twsw-2mqa`, and the state-authority procurement dataset.

### F-AA-R1-05 — MEDIUM

**Identifier:** F-AA-R1-05
**Severity:** MEDIUM
**Locus:** Section 3, sentence stating that the report contains 111,879 contract records across fiscal years ending 2022 through 2024.
**Substance — surface versus substrate:** The surface states 111,879 records for the three-year interval. The frozen three-year substrate and manifest contain 37,988 records: 12,156 in FY2022, 12,114 in FY2023, and 13,718 in FY2024. The larger number appears to describe a broader historical view, not the stated three years.
**Disposition:** **REQUIRES CORRECTION.** Replace with 37,988 for the frozen FY2022–FY2024 extract, or state the broader date range and source for 111,879. Ensure all scope counts refer to the same dataset/version.
**Cross-reference:** Snapshot manifest; independent recomputation §4.1.

### F-AA-R1-06 — MEDIUM

**Identifier:** F-AA-R1-06
**Severity:** MEDIUM
**Locus:** Section 3 and Section 5; claim that state law requires public authorities to publish procurement reports to a common schema on the state open-data portal.
**Substance — surface versus substrate:** The surface attributes the entire standardized portal-publication mechanism directly to statute. The legal substrate requires annual authority reporting; PARIS supplies the common electronic reporting/template mechanism, and ABO in collaboration with Open Data NY publishes compiled data. The resulting common schema is real, but the legal/operational chain is compressed into an overstatement.
**Disposition:** **REQUIRES CORRECTION.** State that Public Authorities Law requires annual reporting; authorities submit through PARIS using standardized reporting structures; ABO/Open Data NY publishes compiled datasets. Avoid saying the statute itself directly mandates portal publication in the precise schema unless a specific provision establishes that mechanism.
**Cross-reference:** Public Authorities Law §2800; ABO public-authority data methodology; PARIS documentation.

### F-AA-R1-07 — LOW

**Identifier:** F-AA-R1-07
**Severity:** LOW
**Locus:** Sections 4 introductory paragraph, 4.4, and 6; “carry no dollar amount” / “no dollar amount” wording.
**Substance — surface versus substrate:** The surface merges missing and zero values. The substrate contains 1,348 missing `contract_amount` values and 48 explicit zeros, totaling 1,396 excluded records. Those conditions are analytically distinct.
**Disposition:** **REQUIRES CORRECTION.** Report missing and explicit-zero counts separately, explain why each is excluded, and bound sensitivity where feasible.
**Cross-reference:** Independent recomputation §4.2.

### F-AA-R1-08 — LOW

**Identifier:** F-AA-R1-08
**Severity:** LOW
**Locus:** `snapshot/MANIFEST.json`, field inventory.
**Substance — surface versus substrate:** The manifest lists 21 fields, while the snapshot contains 22. `vendor_province_region` is present in the rows but omitted from the manifest field list. The hash remains valid, so this is a metadata completeness defect rather than integrity failure.
**Disposition:** **REQUIRES CORRECTION.** Regenerate the manifest's field inventory programmatically from the frozen rows and add a validation that the listed set equals the actual set.
**Cross-reference:** Snapshot and manifest integrity check.

### F-AA-R1-09 — LOW

**Identifier:** F-AA-R1-09
**Severity:** LOW
**Locus:** Audit brief Materials item 4; companion Verification Status; `reproduce_paper2.py --live`.
**Substance — surface versus substrate:** The surface says `--live` checks drift against the current endpoint in connection with reproduction of every Section 4 figure. The script's live mode checks only FY2024 row count and summed `contract_amount`; it does not recompute or compare process shares, MWBE shares, prior-year persistence, vendor concentration, Gini, missingness composition, or source schema. Offseting or subgroup drift could therefore go undetected.
**Disposition:** **REQUIRES CORRECTION.** Make live mode run the complete calculation pipeline for all three years and compare every emitted statistic, source schema, and row/hash summary against the frozen baseline, with explicit tolerances and nonzero exit status on drift.
**Cross-reference:** Reproduction script; audit brief numerical-reproduction scope.

## 6. Checklist outcomes without findings

- **Arithmetic reproducibility:** PASS on the frozen snapshot for the selected `contract_amount` estimand.
- **Tier-3 leakage:** No accusation of intent, steering, discrimination, favoritism, or fraud was found. The explicit refusals are clear.
- **Concentration mechanism framing:** The non-culpable structural explanation is appropriately framed as a mechanism rather than an accusation. Its numerical basis must be recomputed on the corrected estimand.
- **Corrected capital-infrastructure claim F-AA-1:** Schema-level review supports that `kizb-nxtu` and `ehz8-ag3n` are tabular capital datasets and that project locations are separate, making a project-key join followed by spatial attribution necessary. No new contradiction was found. A fresh functional row-level join remains pending.
- **Portability scope:** The note properly says cross-jurisdiction portability is designed but not demonstrated.
- **Religious vocabulary/evidence separation:** The note explicitly treats the vocabulary as inspiration rather than empirical evidence; no finding.

## 7. Minimum correction package before re-audit

1. Select and define the dollar estimand: annual expenditure, new-award face value, or reported-contract stock.
2. Recompute all Section 4 figures consistently on that estimand and revise annual/persistence language.
3. Reframe the MWBE statistic as prime-vendor descriptive data unless full direct/indirect, eligible-spend, goal, waiver, and exemption data are added.
4. Remove the competitive-process “pass,” or execute a real declared-rule test against MTA guidelines and exceptions.
5. Rebase provenance on an official MTA/ABO source and reconcile the community view.
6. Correct the three-year record count, reporting-law phrasing, missing/zero split, manifest field list, and live-drift test.
7. Rerun the full live endpoint comparison and functional capital-location join.
8. Append these findings and dispositions to the companion ledger without silently replacing the superseded text.

## 8. Round disposition

**NON-PASS — revise and restart the two-consecutive-round count after absorption.**

The note retains a potentially publishable descriptive result: prime-MWBE vendors account for a substantially larger share of reported contract records than of either total reported contract face value or annual expenditures, and vendor contract values are highly concentrated. The present version does not yet establish the stronger declared-versus-operative conclusions it attaches to those numbers.

---

# Bismillah ir-Rahman ir-Rahim
