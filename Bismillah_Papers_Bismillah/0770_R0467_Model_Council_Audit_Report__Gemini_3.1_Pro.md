# Bismillah ir-Rahman ir-Rahim

# R0467 -- Model Council Audit Report: Gemini 3.1 Pro

**Chronological Index:** 770 of 995  
**Date:** Undated  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-PC-R2_gemini31.md  
**Source Format:** md  
**SHA-256:** `6bd8058235e9b69150a8b7610a73805eb26cce400164817992d187aaecf05f7d`  

---

## R0467 · Model Council Audit Report: Gemini 3.1 Pro

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-PC-R2_gemini31.md
- source_format: md
- text_sha256: 6bd8058235e9b69150a8b7610a73805eb26cce400164817992d187aaecf05f7d

# Model Council Audit Report: Gemini 3.1 Pro

## A. Identity and Attestation
I am a fresh, memoryless, isolated instance of Gemini 3.1 Pro (Google lineage). I am a non-producer lineage, qualifying member whose verdict bears on convergence. I attest verbatim that I have NO chat history, NO memory, NO saved skills, NO prior-conversation context, and NO access to any other member's work. I have judged only what is in the brief and the attached package, reached purely from the data and executed code in my isolated working directory `/home/user/workspace/council/gemini31pro/`.

## B. Execution Status & Outputs
I have successfully executed the required reproduction steps, including writing my own independent verification scripts.

### Step 1: Exact reproduction
`python3 reproduce_procurement.py`
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

[note] Concentration is measured on the positive-amount vendor basis; the savings model uses the official Table 7 base. The Negotiated positive basis is about 4.75% ($192.96M) below official (open reconciliation item). This tool measures; it does not judge whether any award should have been competed (refused).

All checks reproduced exactly. Exit 0.
```

### Step 2: Selftest
`python3 reproduce_procurement.py --selftest`
```
[integrity] sole_source  OK
[integrity] negotiated   OK
[selftest] perturbing each checked value...
[selftest] perturbed 14 values; missed 0
```

### Step 3: Live MTA re-pull
`python3 reproduce_procurement.py --live`
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

[note] Concentration is measured on the positive-amount vendor basis; the savings model uses the official Table 7 base. The Negotiated positive basis is about 4.75% ($192.96M) below official (open reconciliation item). This tool measures; it does not judge whether any award should have been competed (refused).

All checks reproduced exactly. Exit 0.
```

### Steps 4 & 5: Independent recompute & Adversarial trap
Independent computation (my own python script):
```
--- Sole Source ---
Vendors: 106
Total: $1597506644.98
Top 1: 82.5004%
Top 5: 90.5858%
Top 10: 94.0642%
Top 20: 97.2606%
Gini: 0.95557
Top Vendor: NEW YORK CITY ECONOMIC DEVELOPMENT CORPORATION ($1317949728.00)

--- Negotiated Acquisition ---
Vendors: 462
Total: $3865895209.67
Top 1: 24.0334%
Top 5: 36.9178%
Top 10: 46.2163%
Top 20: 55.3833%
Gini: 0.81855
Top Vendor: HANYC FOUNDATION INC ($929104960.00)

--- Savings Bases ---
Core (official): $5658002459
Wide (official): $6984040398
NYCEDC-adj (official): $4340052731
NYCEDC-adj (positive): $4145452127
Intermediary-screened: $3410947771

--- F-PC-R1-001 Recompute ---
Difference (off - pos): $194600604.35
10% diff: $19460060.44
20% diff: $38920120.87

--- Adversarial Trap (Total Rows included) ---

Sole Source (Adversarial):
Total: $3195013289.96
Top 1: 50.0000%

Negotiated Acquisition (Adversarial):
Total: $7731790419.35
Top 1: 50.0000%
```
The adversarial trap works exactly as described: including the totals exactly doubles the sums and makes Top-1 a uniform 50.0000%. The paper correctly excludes them.

### Step 6: Appendix 1 reconciliation (Independent)
Output from fetching the file and parsing it:
```
Negotiated Acquisition:
  Rows: 935
  Total Amount: $3865895209.68
  Distinct Vendors: 462
  Blank Vendor Names: 0
  All positive: True
Sole Source:
  Rows: 115
  Total Amount: $1597506644.98
  Distinct Vendors: 106
  Blank Vendor Names: 0
  All positive: True
```
This confirms 935 rows for NA (vs 962 in Table 7 summary = 27 contract gap) and 115 rows for SS (vs 126 in Table 7 = 11 contract gap), with identical positive sums. The mechanism stated in v0.4 is supported.

## C. Findings

- **Identifier:** F-PC-R2-001
- **Severity:** INFO
- **Locus:** F-PC-R1-001 (Section 5.0 basis note and Table 3)
- **Substance (surface vs substrate):** The paper (v0.4) now correctly states the cross-basis effect of $194.6M (official $4,340,052,731 minus positive $4,145,452,127), and the 10%/20% floor deltas of $19.46M and $38.92M. My independent recomputation mathematically verifies these numbers. Table 3 explicitly shows the adjusted row on both bases. No sentences were found understating this effect.
- **Disposition:** Fix verified.
- **Cross-reference:** Brief F-PC-R1-001.

- **Identifier:** F-PC-R2-002
- **Severity:** INFO
- **Locus:** F-PC-R1-002 (Appendix 1 Reconciliation and Accessibility)
- **Substance (surface vs substrate):** The paper no longer claims Appendix 1 is HTTP-403 access-blocked or that the gap is "unattributable vendor names." It successfully explains the coverage-difference mechanism between Table 7 (summary counts) and the Appendix 1 export. My independent retrieval of Appendix 1 matches the 935 / 115 rows and the exact sums.
- **Disposition:** Fix verified.
- **Cross-reference:** Brief F-PC-R1-002.

- **Identifier:** F-PC-R2-003
- **Severity:** INFO
- **Locus:** F-PC-R1-003, 004, 005 (Savings breadth, abstract vs body, labels)
- **Substance (surface vs substrate):** Table 3 correctly labels Core/Wide as upper bounds and includes the intermediary-screened base ($3.41B). The abstract cleanly limits the headline bounds to "$500 million to $1.4 billion" with the $434M sensitivity floor, matching the body. The title reads "Potentially Recoverable" and Table 3 reads "Estimated Conditional Savings." The conditional boundaries are maintained throughout the text and do not leak into asserting recoverability as an unconditional fact. By adding the intermediary-screened row explicitly, the framing appropriately bounds the estimate compared to earlier drafts.
- **Disposition:** Fixes verified.
- **Cross-reference:** Brief F-PC-R1-003, F-PC-R1-004, F-PC-R1-005.

## D. Verdict

**PASS**.

I found zero CRITICAL and zero HIGH defects. The reproduction steps were fully and exactly executed, both via the provided script and via independent arithmetic computation and data pulls. The consecutive qualifying-PASS count moves from ZERO to ONE.

---

# Bismillah ir-Rahman ir-Rahim
