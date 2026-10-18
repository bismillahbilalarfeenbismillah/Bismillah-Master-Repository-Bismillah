# Bismillah ir-Rahman ir-Rahim

# R0470 -- Report for Audit F-PC-R3

**Chronological Index:** 771 of 995  
**Date:** Undated  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-PC-R3_gemini31.md  
**Source Format:** md  
**SHA-256:** `7489d8c27ba682ca78f832087d395640a118559363732d0406f2b960e3181e70`  

---

## R0470 · Report for Audit F-PC-R3

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-PC-R3_gemini31.md
- source_format: md
- text_sha256: 7489d8c27ba682ca78f832087d395640a118559363732d0406f2b960e3181e70

# Report for Audit F-PC-R3

## Execution Status
**Status: SUCCESS**
All six mandatory protocol steps executed successfully using bash commands in the isolated workspace environment. The outputs were verified against expected figures.
- Step 1: `python3 reproduce_procurement.py` ran successfully. Output verifies hashes, concentration stats, savings bases, and MTA constants exactly as expected. Exit code 0.
- Step 2: `python3 reproduce_procurement.py --selftest` ran successfully. Perturbed 14 values, missed 0.
- Step 3: `python3 reproduce_procurement.py --live` ran successfully. Confirmed 13,718 records, 2,656 vendors, $65.19B, top10 30.4151%, Gini 0.93117.
- Step 4: `independent_recompute.py` built from scratch and executed. Confirmed concentration, five savings bases, and $194.6M basis effect exactly as expected.
- Step 5: `adversarial_trap.py` built and executed, reproducing the exact expected behavior when TOTAL/footnotes are included (roughly 2x inflation, top-1 drops to exactly 50%).
- Step 6: `appendix_reconcile.py` built and executed against `appendix1.xlsx` FY2025. Confirmed exact counts/sums for Sole Source Contracts (115 rows / $1,597,506,644.98 / 106 vendors) and Negotiated Acquisition Contracts (935 rows / $3,865,895,209.68 / 462 vendors). All positive, 0 blanks. Supported v0.5's coverage-difference mechanism exactly.

## Identity and Attestations
I am Gemini 3.1 Pro (Google). I am a QUALIFYING member (non-Claude, non-producer lineage).
I operated as a fresh, memoryless instance. No chat history, no memory, and structural isolation were maintained.
I WAS part of the Round-2 qualifying pair (GPT 5.5 + Gemini 3.1 Pro), so I am NOT new relative to that pair.

## Fix Verification
- F-PC-R2-001 (Conclusion floor wording): FIXED. The conclusion clearly separates the NYCEDC-only floor ($434M) and the intermediary-screened sensitivity ($341M to $682M).
- F-PC-R2-009 (Tool note): FIXED. `reproduce_procurement.py` note explains the 4.75% / $192.96M coverage difference vs Appendix-1 and no longer contains "open reconciliation item".
- F-PC-R2-006 (One-cent artifact): FIXED. The tool note was checked and the logic confirms rounding tolerance inside the tool.

## Audit Checks
- House style: The paper uses double-hyphens `--`, consistent "BayyinahEnterprise" brand, and mentions the MTA reproduction across "nine rounds".
- Internal consistency: Transliteration is consistent (`AllocationAsymmetry` without spaces, `at-Ta'līm`). Version `v0.5` is uniformly used except for `v0.4` where historically appropriate in the audit notice. Figures are consistent across abstract, body, and conclusion.
- Savings framing: Conditional pilot-gated framing is meticulously maintained throughout (abstract, section 5.0, conclusion).
- Tier 3 violations: None. The paper properly avoids asserting culpability, explicitly refuses to judge whether awards should have been competed, and treats the savings strictly conditionally.

## Findings
None. Zero CRITICAL, zero HIGH, zero MEDIUM, zero LOW, zero INFO. The v0.5 artifact is extremely rigorous, accurate, and internally consistent based on the provided brief and my execution.

## Verdict
**PASS**
With zero CRITICAL/HIGH findings and successful execution of all steps.

Since I am not a new rotated member, I note that convergence under Standing Rule 7 is MET on the v0.5 artifact assuming a valid qualifying pair completes execution, though my own presence does not introduce the desired rotation from F-PC-R2.## Outputs

**Step 1:**
```
[integrity] sole_source  OK
[integrity] negotiated   OK

Concentration (Table 2), clean vendor rows:
  sole_source  vendors=106 total=$1597506644.98 top1=82.5004% top5=90.5858% top10=94.0642% gini=0.95557  [OK]
  negotiated   vendors=462 total=$3865895209.67 top1=24.0334% top5=36.9178% top10=46.2163% gini=0.81855  [OK]

Addressable base and savings (Table 3), official Table 7 basis:
  savings base Core (official)  $5,658,002,459  @10%=$565,800,246  @20%=$1,131,600,492  [OK]
  savings base Wide (official)  $6,984,040,398  @10%=$698,404,040  @20%=$1,396,808,080  [OK]
  savings base NYCEDC-adj (official) $4,340,052,731  @10%=$434,005,273  @20%=$868,010,546  [OK]
  savings base NYCEDC-adj (positive) $4,145,452,127  @10%=$414,545,213  @20%=$829,090,425  [OK]
  savings base Intermediary-screened $3,410,947,771  @10%=$341,094,777  @20%=$682,189,554  [OK]

MTA constants carried from converged AllocationAsymmetry (DOI 10.5281/zenodo.21445552):
  FY2024: 13718 records, 2656 vendors, $65189755228.64 face, top10 30.4151%, Gini 0.93117

[note] Concentration is measured on the positive-amount vendor basis; the savings model uses the official Table 7 base. The Negotiated positive basis is about 4.75% ($192.96M) below official -- a Table-7-vs-Appendix-1 coverage difference (27 contracts absent from the parent-contracts extract), reconciled directly against Appendix 1. This tool measures; it does not judge whether any award should have been competed (refused).

All checks reproduced exactly. Exit 0.
```

**Step 2:**
```
[integrity] sole_source  OK
[integrity] negotiated   OK
[selftest] perturbing each checked value...
[selftest] perturbed 14 values; missed 0
```

**Step 3:**
```
[integrity] sole_source  OK
[integrity] negotiated   OK

Concentration (Table 2), clean vendor rows:
  sole_source  vendors=106 total=$1597506644.98 top1=82.5004% top5=90.5858% top10=94.0642% gini=0.95557  [OK]
  negotiated   vendors=462 total=$3865895209.67 top1=24.0334% top5=36.9178% top10=46.2163% gini=0.81855  [OK]

Addressable base and savings (Table 3), official Table 7 basis:
  savings base Core (official)  $5,658,002,459  @10%=$565,800,246  @20%=$1,131,600,492  [OK]
  savings base Wide (official)  $6,984,040,398  @10%=$698,404,040  @20%=$1,396,808,080  [OK]
  savings base NYCEDC-adj (official) $4,340,052,731  @10%=$434,005,273  @20%=$868,010,546  [OK]
  savings base NYCEDC-adj (positive) $4,145,452,127  @10%=$414,545,213  @20%=$829,090,425  [OK]
  savings base Intermediary-screened $3,410,947,771  @10%=$341,094,777  @20%=$682,189,554  [OK]

MTA FY2024 cross-check (live re-pull from data.ny.gov):
  MTA FY2024 live: records=13718 vendors=2656 face=$65189755228.64 top10=30.4151% gini=0.93117  [OK]

MTA constants carried from converged AllocationAsymmetry (DOI 10.5281/zenodo.21445552):
  FY2024: 13718 records, 2656 vendors, $65189755228.64 face, top10 30.4151%, Gini 0.93117

[note] Concentration is measured on the positive-amount vendor basis; the savings model uses the official Table 7 base. The Negotiated positive basis is about 4.75% ($192.96M) below official -- a Table-7-vs-Appendix-1 coverage difference (27 contracts absent from the parent-contracts extract), reconciled directly against Appendix 1. This tool measures; it does not judge whether any award should have been competed (refused).

All checks reproduced exactly. Exit 0.
```

**Step 4:**
```
Sole Source: vendors=106 total=1597506644.98 top1=82.5004% top5=90.5858% top10=94.0642% top20=97.2606% gini=0.95557 top_vendor=NEW YORK CITY ECONOMIC DEVELOPMENT CORPORATION top_amt=1317949728.00
Negotiated: vendors=462 total=3865895209.67 top1=24.0334% top5=36.9178% top10=46.2163% top20=55.3833% gini=0.81855 top_vendor=HANYC FOUNDATION INC top_amt=929104960.00

Core (off): 5658002459 (10% 565800246, 20% 1131600492)
Wide (off): 6984040398 (10% 698404040, 20% 1396808080)
NYCEDC-adj (off): 4340052731 (10% 434005273, 20% 868010546)
NYCEDC-adj (pos): 4145452126.65 (10% 414545213, 20% 829090425)
Intermediary (off): 3410947771 (10% 341094777, 20% 682189554)

Basis Effect: 194600604.35
10% Effect: 19460060.44
20% Effect: 38920120.87
SS Diff: 1644123.02
NA Diff: 192956481.33
Total Diff (SS+NA): 194600604.35
```

**Step 5:**
```
TRAP Sole Source: vendors=110 total=3195013289.96 top1=50.0000% top5=94.7295% top10=96.7606% top_vendor=nan top_amt=1597506644.98
TRAP Negotiated: vendors=466 total=7731790419.35 top1=50.0000% top5=67.2173% top10=72.3878% top_vendor=nan top_amt=3865895209.68
```

**Step 6:**
```
Columns: ['Contract_Group', 'Subgroup', 'Doc_CD', 'Doc_Dept_CD', 'Doc_ID', 'Agreement_ID_or_PIN', 'Doc_Dept_Short_Name', 'Vend_Cust_CD', 'Vendor_Legal_Name', '_1099_Classification', 'OCA_Number', 'Contract_Purpose', 'Doc_Created_On_Date', 'Original_Registration_Date', 'Contract_Registered_Amount', 'Revised_Max_Amount', 'Contract_Start_Date', 'Revised_Start_Date', 'Registration_Delta', 'Retroactivity_Category', 'Contract_End_Date', 'Revised_End_Date', 'Award_Method_Code', 'Award_Method_Description', 'Contract_Type_Code', 'Contract_Type_Description', 'Contract_Class_Code', 'Contract_Class_Description', 'Contract_Category_Code', 'Contract_Category_Description', 'Award_Level', 'Industry', 'Replaces_Award_Doc_Code', 'Replaces_Award_Department_Code', 'Replaces_Award_Number', 'MWBE_Gendered', 'Agency_Type', 'FY']
FY25 rows: 12786

Sole Source in Appendix 1:
Rows: 115
Total Amount: 1597506644.98
Vendors (positive amount): 106
Blank Vendor Names: 0
Negative/Zero Amounts: 0

Negotiated Acquisition in Appendix 1:
Rows: 935
Total Amount: 3865895209.68
Vendors (positive amount): 462
Blank Vendor Names: 0
Negative/Zero Amounts: 0
```

---

# Bismillah ir-Rahman ir-Rahim
