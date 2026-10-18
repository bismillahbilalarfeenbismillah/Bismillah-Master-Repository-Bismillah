# Bismillah ir-Rahman ir-Rahim

# R0462 -- Audit Report: Procurement Concentration and Recoverable Competitive Savings in New York City Contracting (v0.3)

**Chronological Index:** 82 of 995  
**Date:** 2025  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-PC-R1_gemini31.md  
**Source Format:** md  
**SHA-256:** `427d0bd3a815c760ecc281057b8bf5696790b3022313739fe90ec6dfa5fdc853`  

---

## R0462 · Audit Report: Procurement Concentration and Recoverable Competitive Savings in New York City Contracting (v0.3)

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-PC-R1_gemini31.md
- source_format: md
- text_sha256: 427d0bd3a815c760ecc281057b8bf5696790b3022313739fe90ec6dfa5fdc853

# Audit Report: Procurement Concentration and Recoverable Competitive Savings in New York City Contracting (v0.3)

**Identity & Lineage:** Gemini 3.1 Pro (Google). Lineage: Google.
**Attestation:** I am an INDEPENDENT, FRESH, MEMORYLESS audit instance on a Model Council. I have NO chat history, NO memory, NO saved skills, NO prior-conversation context, NO carryover from any earlier Bayyinah round, and NO access to any other council member's work.
**Execution Status:** Executed (All 5 mandatory steps completed successfully).
**Verdict:** PASS (Qualifying member)
**Consecutive Qualifying-PASS Count Outcome:** ONE (First step toward convergence).

## 1. Reproduction Outputs

### Step 1: Baseline Reproduction Script
```
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

### Step 2: Selftest Mode
```
[integrity] sole_source  OK
[integrity] negotiated   OK
[selftest] perturbing each checked value...
[selftest] perturbed 14 values; missed 0
```

### Step 3: Live MTA Data Reproduction
```
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

### Step 4: Independent Clean Recompute
```
=== CLEAN INDEPENDENT RECOMPUTE ===

Columns in /home/user/workspace/council/gemini/data/sole_source_vendors_fy25.csv:
['Rank', 'Vendor', 'Lead Agency', 'Contracts', 'Total Value ($)', 'Cumulative % of Subgroup Total', 'Sample Contract Purpose']
Using Rank column: Rank, Amount column: Total Value ($)
File: sole_source_vendors_fy25.csv
Vendors: 106
Total: $1,597,506,644.98
Top-1: 82.5004%
Top-5: 90.5858%
Top-10: 94.0642%
Top-20: 97.2606%
Gini: 0.95557
Top vendor: NEW YORK CITY ECONOMIC DEVELOPMENT CORPORATION - $1,317,949,728.00

Columns in /home/user/workspace/council/gemini/data/negotiated_acquisition_vendors_fy25.csv:
['Rank', 'Vendor', 'Lead Agency', 'Contracts', 'Total Value ($)', 'Cumulative % of Subgroup Total', 'Sample Contract Purpose']
Using Rank column: Rank, Amount column: Total Value ($)
File: negotiated_acquisition_vendors_fy25.csv
Vendors: 462
Total: $3,865,895,209.67
Top-1: 24.0334%
Top-5: 36.9178%
Top-10: 46.2163%
Top-20: 55.3833%
Gini: 0.81855
Top vendor: HANYC FOUNDATION INC - $929,104,960.00

=== SAVINGS BASES RECOMPUTE ===
Core Base (Sole + Negotiated): $5,658,002,459
Wide Base (Core + Emergency): $6,984,040,398
NYCEDC-adjusted Base (Core - NYCEDC): $4,340,052,731
```

### Step 5: Adversarial Trap Recompute
```
=== ADVERSARIAL TRAP RECOMPUTE (INCLUDING TOTALS AND FOOTNOTES) ===
File: sole_source_vendors_fy25.csv
Vendors: 110
Total: $3,195,013,289.96
Top-1: 50.0000%
Top-5: 94.7295%
Top-10: 96.7606%
Gini: 0.96496
Top value in array: $1,597,506,644.98

File: negotiated_acquisition_vendors_fy25.csv
Vendors: 466
Total: $7,731,790,419.35
Top-1: 50.0000%
Top-5: 67.2173%
Top-10: 72.3878%
Gini: 0.90684
Top value in array: $3,865,895,209.68
```

## 2. Findings Table

| Identifier | Severity | Locus | Substance | Disposition | Cross-Reference |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F-PC-R1-001 | INFO | Section 4.4 | Negotiated Acquisition reconciliation magnitude. The 4.75% / $192.96M gap cannot logically be zeroes or negatives. The paper's conclusion—positive-value contracts missing a distinct vendor name—is logically sound. I attempted to fetch Appendix 1 at https://comptroller.nyc.gov/wp-content/uploads/2025/10/Appendix-1-Parent-Contracts.xlsx but received an HTTP error (Server Error/Unavailable). The paper adequately discloses the gap and correctly states the Gini computation represents ~95.25% of the base. | Acknowledged. Author hypothesis holds. | See Step 4 outputs & Section 4.4 |
| F-PC-R1-002 | MEDIUM | Table 3, Section 5.0 | Mixed-basis in the "NYCEDC-adjusted" row. The calculation subtracts a positive-basis vendor total ($1.317B) from the official Table 7 Core ($5.658B) rather than subtracting it from the positive-basis Core ($5.463B) or subtracting the official NYCEDC Table 7 amount from the official Core. | Flagged for correction. As noted by the paper, this is an immaterial ~$2M error but should be harmonized for mathematical consistency. | See Step 4 outputs & Section 5.0 |
| F-PC-R1-003 | LOW | Table 1, 2, 3 | Internal Consistency/House Style. Figures are consistent across abstract, body, and tables. Version v0.3 is uniform. Em/en-dashes are excluded (using standard hyphens or double hyphens). The MTA reproduction is accurately described as "nine rounds" of audit. "BayyinahEnterprise" branding is present. | Compliant. No further action needed. | General text review |

## 3. Assessment of "Two Points to Press Hardest"

**1. Negotiated Acquisition Reconciliation ($192.96M Gap)**
The logical deduction holds: adding $192.96M to reach the official total requires missing positive values. Zeroes don't add up to $192 million, and removing negatives would inflate the positive sum past the official total, not leave it 4.75% short. A lack of distinct vendor attribution is the most likely remaining explanation for missing positive contract records in a vendor-aggregated dataset. I attempted to pull the Appendix 1 dataset from the comptroller's site but received a server error, matching the paper's noted inaccessibility. The paper thoroughly discloses this gap and its impact on the base percentage (~95.25%).

**2. Conditional Framing of Savings Estimate**
I have reviewed Section 5.0, the abstract, the conclusion, and the recommendations with an adversarial lens. The paper strictly maintains its conditional framing. Sentences repeatedly anchor the numbers as "a conditional planning range," stating that the estimate "is not a verified recoverable amount" and is "gated on a pilot (Section 7) that tests whether the underlying spend has viable alternative vendors, the assumption the whole estimate rests on." Nowhere does the paper assert the savings are verified facts or definitively "lost money" being stolen.

Regarding the application of a single-bid-elimination delta to the entire addressable base: the paper bounds this by presenting a "core" and "wide" range, and then further bound it with an "adjusted core" that removes the largest non-competitive vehicle (NYCEDC). Applying literature rates across a massive macro-base is standard exploratory policy analysis, provided the assumptions and exclusions (e.g., gov-to-gov, small purchases, jails/design-build) are clear, which they are here. The paper is measuring, not accusing.

## 4. Tier 3 Boundaries
The paper successfully avoids Tier 3 violations. It explicitly states that "Group 2 is not inherently improper" and that concentration via NYCEDC or HANYC "is driven by one or two single-purpose intermediary vehicles... that function structurally more like the already-excluded Government-to-Government category than like private-market vendor capture." No vendor or agency is accused of impropriety.

---

# Bismillah ir-Rahman ir-Rahim
