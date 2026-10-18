# Bismillah ir-Rahman ir-Rahim

# R0433 -- Model Council Audit Report: Bayyinah Allocation & Asymmetric-Measure Audits v0.5 (Round 6)

**Chronological Index:** 19 of 995  
**Date:** 2024  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-AA-R6_gemini31.md  
**Source Format:** md  
**SHA-256:** `9e902bade34962c0922edd66c983b1db95451389a20c36fa10b984eeda42b4bd`  

---

## R0433 · Model Council Audit Report: Bayyinah Allocation & Asymmetric-Measure Audits v0.5 (Round 6)

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-AA-R6_gemini31.md
- source_format: md
- text_sha256: 9e902bade34962c0922edd66c983b1db95451389a20c36fa10b984eeda42b4bd

# Model Council Audit Report: Bayyinah Allocation & Asymmetric-Measure Audits v0.5 (Round 6)

## Identity & State Attestation
*   **Model Identity:** Gemini 3.1 Pro
*   **Lineage:** Google
*   **Status:** QUALIFYING non-Claude member
*   **State Attestation:** EXPLICIT NO-PRIOR-STATE ATTESTATION. I have operated as a brand-new, memoryless, independent council auditor with no memory, personalization, saved state, prior audits, or prior findings reports used. No other member's work or model-council files were inspected. All tasks were executed independently within `/home/user/workspace/r6-gemini-3-1-pro`.
*   **Verdict:** **PASS**. Executed successfully with zero CRITICAL and zero HIGH findings. Note: This council round can only become the first of two consecutive qualifying passes; the current counter is ZERO before this round.

## Packet Inventory
*   `Bayyinah_AllocationAsymmetry_v0.5.md` (Reader-facing note)
*   `Bayyinah_AllocationAsymmetry_AuditCompanion.md` (Companion document)
*   `Bayyinah_AllocationAsymmetry_ReproPackage.zip` (Contains snapshot json, MANIFEST.json, and reproduce_paper2.py)

## Execution Protocol

### Step 1: `python3 reproduce_paper2.py`
```bash
[integrity] hash OK, field inventory OK (22 fields), 37988 rows

[4.2] MWBE count vs dollar share (both estimands), by vintage:
  FY2022: count 16.4%  face 3.27% (x5.0)  exp 4.25% (x3.9)  [face $54.7B exp $6.8B miss 712 zero 0]
  FY2023: count 18.6%  face 3.51% (x5.3)  exp 6.27% (x3.0)  [face $63.6B exp $6.7B miss 1049 zero 111]
  FY2024: count 18.7%  face 3.95% (x4.7)  exp 7.06% (x2.7)  [face $65.2B exp $8.2B miss 1348 zero 48]
[4.1] FY2024 process (face | exp):
  Authority Contract - Competitive Bid     face 92.22%  exp 89.65%
  Authority Contract - Non-Competitive B   face  7.78%  exp  4.73%
  Purchased Under State Contract           face  0.00%  exp  3.24%
  Non Contract Procurement/Purchase Orde   face  0.00%  exp  2.38%
[4.3] face conc  top5 22.1% top10 30.4% top20 41.8% gini 0.931 (vendors 2656)
[4.3] exp  conc  top5 16.9% top10 26.2% top20 37.6% gini 0.904
[4.0] pre-2024-award face share 91.7% (stock, not FY2024 flow)
```

### Step 2: `python3 reproduce_paper2.py --selftest`
Exit Code: `0`
```bash
[integrity] hash OK, field inventory OK (22 fields), 37988 rows

[4.2] MWBE count vs dollar share (both estimands), by vintage:
  FY2022: count 16.4%  face 3.27% (x5.0)  exp 4.25% (x3.9)  [face $54.7B exp $6.8B miss 712 zero 0]
  FY2023: count 18.6%  face 3.51% (x5.3)  exp 6.27% (x3.0)  [face $63.6B exp $6.7B miss 1049 zero 111]
  FY2024: count 18.7%  face 3.95% (x4.7)  exp 7.06% (x2.7)  [face $65.2B exp $8.2B miss 1348 zero 48]
[4.1] FY2024 process (face | exp):
  Authority Contract - Competitive Bid     face 92.22%  exp 89.65%
  Authority Contract - Non-Competitive B   face  7.78%  exp  4.73%
  Purchased Under State Contract           face  0.00%  exp  3.24%
  Non Contract Procurement/Purchase Orde   face  0.00%  exp  2.38%
[4.3] face conc  top5 22.1% top10 30.4% top20 41.8% gini 0.931 (vendors 2656)
[4.3] exp  conc  top5 16.9% top10 26.2% top20 37.6% gini 0.904
[4.0] pre-2024-award face share 91.7% (stock, not FY2024 flow)

[selftest] perturbing each statistic to confirm the comparator detects it...
[selftest] PASS: comparator detected all 45 deliberate perturbations
```

### Step 3: `python3 reproduce_paper2.py --live`
Exit Code: `0`
```bash
[integrity] hash OK, field inventory OK (22 fields), 37988 rows

[4.2] MWBE count vs dollar share (both estimands), by vintage:
  FY2022: count 16.4%  face 3.27% (x5.0)  exp 4.25% (x3.9)  [face $54.7B exp $6.8B miss 712 zero 0]
  FY2023: count 18.6%  face 3.51% (x5.3)  exp 6.27% (x3.0)  [face $63.6B exp $6.7B miss 1049 zero 111]
  FY2024: count 18.7%  face 3.95% (x4.7)  exp 7.06% (x2.7)  [face $65.2B exp $8.2B miss 1348 zero 48]
[4.1] FY2024 process (face | exp):
  Authority Contract - Competitive Bid     face 92.22%  exp 89.65%
  Authority Contract - Non-Competitive B   face  7.78%  exp  4.73%
  Purchased Under State Contract           face  0.00%  exp  3.24%
  Non Contract Procurement/Purchase Orde   face  0.00%  exp  2.38%
[4.3] face conc  top5 22.1% top10 30.4% top20 41.8% gini 0.931 (vendors 2656)
[4.3] exp  conc  top5 16.9% top10 26.2% top20 37.6% gini 0.904
[4.0] pre-2024-award face share 91.7% (stock, not FY2024 flow)

[live] pulling all three years and comparing EVERY statistic + schema + row count...
[live] no drift on any published statistic, schema, or row count
```

### Step 4: Independent Compute (`indep_compute_v2.py`)
Code implemented strictly using base Python functions, fully without imports of supplied logic, enforcing positive-total Gini calculation correctly and producing overlapping counts directly.

**Source Code:**
```python
import json
import math

def compute_gini(values):
    # compute Gini coefficient exact method requested
    values = sorted(values)
    n = len(values)
    if n == 0: return 0
    cumulative_sum = [0] * n
    cumulative_sum[0] = values[0]
    for i in range(1, n):
        cumulative_sum[i] = cumulative_sum[i-1] + values[i]

    sum_cumsum = sum(cumulative_sum)
    gini = (n + 1 - 2 * sum_cumsum / cumulative_sum[-1]) / n
    return gini

def num(val):
    if val is None or val == "":
        return 0.0
    try:
        return float(val)
    except:
        return 0.0

def main():
    with open('snapshot/gpsc-qqsz_FY2022-2024.json', 'r') as f:
        data = json.load(f)

    print(f"Total rows: {len(data)}")

    fy24_data = [r for r in data if r.get('fiscal_year_end_date', '').startswith('2024-')]

    total_face_24 = sum(num(r.get('contract_amount')) for r in fy24_data)
    total_exp_24 = sum(num(r.get('amount_expended_for_fiscal_year')) for r in fy24_data)

    print(f"FY2024 face: ${total_face_24 / 1e9:.2f}B")
    print(f"FY2024 annual expenditure: ${total_exp_24 / 1e9:.2f}B")

    # MWBE status
    mwbe_count = sum(1 for r in fy24_data if str(r.get('vendor_is_a_mwbe')).upper() == 'Y')
    mwbe_face = sum(num(r.get('contract_amount')) for r in fy24_data if str(r.get('vendor_is_a_mwbe')).upper() == 'Y')
    mwbe_exp = sum(num(r.get('amount_expended_for_fiscal_year')) for r in fy24_data if str(r.get('vendor_is_a_mwbe')).upper() == 'Y')

    mwbe_count_pct = (mwbe_count / len(fy24_data)) * 100 if len(fy24_data) > 0 else 0
    mwbe_face_pct = (mwbe_face / total_face_24) * 100 if total_face_24 > 0 else 0
    mwbe_exp_pct = (mwbe_exp / total_exp_24) * 100 if total_exp_24 > 0 else 0

    print(f"FY2024 MWBE count/face/expenditure: {mwbe_count_pct:.2f}/{mwbe_face_pct:.2f}/{mwbe_exp_pct:.2f}%")

    # Top 10 Face Concentration
    vendor_face = {}
    vendor_exp = {}

    for r in fy24_data:
        v_name = r.get('vendor_name', 'UNKNOWN')
        if v_name not in vendor_face:
            vendor_face[v_name] = 0.0
        if v_name not in vendor_exp:
            vendor_exp[v_name] = 0.0

        c_amt = num(r.get('contract_amount'))
        e_amt = num(r.get('amount_expended_for_fiscal_year'))

        vendor_face[v_name] += c_amt
        vendor_exp[v_name] += e_amt

    positive_face_vendors = {k: v for k, v in vendor_face.items() if v > 0}
    positive_exp_vendors = {k: v for k, v in vendor_exp.items() if v > 0}

    sorted_face_vendors = sorted(positive_face_vendors.values(), reverse=True)
    top_10_face = sum(sorted_face_vendors[:10])
    top_10_face_pct = (top_10_face / sum(sorted_face_vendors)) * 100 if sum(sorted_face_vendors) > 0 else 0

    print(f"FY2024 top-10 face concentration: {top_10_face_pct:.2f}%")

    # Gini coefficients
    face_gini = compute_gini(list(positive_face_vendors.values()))
    exp_gini = compute_gini(list(positive_exp_vendors.values()))

    print(f"Vendor Gini face: {face_gini:.3f}")
    print(f"Vendor Gini exp: {exp_gini:.3f}")

    # Vintage Fingerprint
    fy22_data = [r for r in data if r.get('fiscal_year_end_date', '').startswith('2022-')]
    fy23_data = [r for r in data if r.get('fiscal_year_end_date', '').startswith('2023-')]

    all_keys = set()
    for r in data:
        all_keys.update([k for k in r.keys() if not k.startswith(':')])

    exclude_18 = {'fiscal_year_end_date', 'amount_expended_for_fiscal_year', 'amount_expended_to_date', 'current_or_outstanding_balance'}
    fields_18 = sorted(list(all_keys - exclude_18))

    def get_tuple_18(r):
        return tuple(str(r.get(k, '')) for k in fields_18)

    def get_tuple_all(r):
        return tuple(str(r.get(k, '')) for k in sorted(list(all_keys)))

    set22_18 = set(get_tuple_18(r) for r in fy22_data)
    set23_18 = set(get_tuple_18(r) for r in fy23_data)
    set24_18 = set(get_tuple_18(r) for r in fy24_data)

    print(f"Overlap FY22-FY23 (18 fields): {len(set22_18.intersection(set23_18))}")
    print(f"Overlap FY22-FY24 (18 fields): {len(set22_18.intersection(set24_18))}")
    print(f"Overlap FY23-FY24 (18 fields): {len(set23_18.intersection(set24_18))}")

    set22_all = set(get_tuple_all(r) for r in fy22_data)
    set23_all = set(get_tuple_all(r) for r in fy23_data)
    set24_all = set(get_tuple_all(r) for r in fy24_data)

    print(f"All field overlap FY22-FY23: {len(set22_all.intersection(set23_all))}")
    print(f"All field overlap FY22-FY24: {len(set22_all.intersection(set24_all))}")
    print(f"All field overlap FY23-FY24: {len(set23_all.intersection(set24_all))}")
    print(f"All field overlap FY22-FY23-FY24: {len(set22_all.intersection(set23_all).intersection(set24_all))}")

if __name__ == '__main__':
    main()
```
**Output:**
```bash
Total rows: 37988
FY2024 face: $65.19B
FY2024 annual expenditure: $8.17B
FY2024 MWBE count/face/expenditure: 18.73/3.95/7.06%
FY2024 top-10 face concentration: 30.42%
Vendor Gini face: 0.931
Vendor Gini exp: 0.904
Overlap FY22-FY23 (18 fields): 2115
Overlap FY22-FY24 (18 fields): 604
Overlap FY23-FY24 (18 fields): 1002
All field overlap FY22-FY23: 0
All field overlap FY22-FY24: 0
All field overlap FY23-FY24: 0
All field overlap FY22-FY23-FY24: 0
```

### Step 5: Provenance Reconciliation (curl)
**Querying Community View (`gpsc-qqsz`):**
```bash
curl -s "https://data.ny.gov/resource/gpsc-qqsz.json?\$where=fiscal_year_end_date='2024-12-31T00:00:00.000'&\$select=count(*),sum(contract_amount)"
```
**Raw Result:**
```json
[{"count":"13718","sum_contract_amount":"65189755228.64"}]
```

**Querying First-Party View (`twsw-2mqa`):**
```bash
curl -s "https://data.ny.gov/resource/twsw-2mqa.json?\$where=fiscal_year_end_date='2024-12-31T00:00:00.000'&\$select=count(*),sum(contract_amount)"
```
**Raw Result:**
```json
[{"count":"13648","sum_contract_amount":"65131682801.41"}]
```

**Verification:**
* Count: $13,718$ (Community) vs $13,648$ (First-party)
  * Difference: $70$. Divides as $(70 / 13648) \times 100 \approx 0.512\%$ (matches stated ~0.51% divergence)
* Face: $\$65,189,755,228.64$ (Community) vs $\$65,131,682,801.41$ (First-party)
  * Difference: $\$58,072,427.23$. Divides as $(58072427.23 / 65131682801.41) \times 100 \approx 0.089\%$ (matches stated ~0.089% divergence)

### Step 6: Capital Join Test
**Source Code (`capital_join_fix.py`):**
```python
import pandas as pd
import requests

def fetch_data(url):
    response = requests.get(url)
    return pd.DataFrame(response.json())

def main():
    print("Fetching wcsa-vkhf...")
    wcsa_url = "https://data.ny.gov/resource/wcsa-vkhf.json?$limit=50000"
    wcsa = fetch_data(wcsa_url)

    # Get distinct project numbers from wcsa-vkhf
    wcsa_projects = set(wcsa['project_number'].dropna())
    print(f"Distinct wcsa-vkhf project numbers: {len(wcsa_projects)}")

    print("Fetching kizb-nxtu...")
    kizb_url = "https://data.ny.gov/resource/kizb-nxtu.json?$limit=50000"
    kizb = fetch_data(kizb_url)
    kizb_projects = set(kizb['project_number'].dropna())

    print("Fetching ehz8-ag3n...")
    ehz8_url = "https://data.ny.gov/resource/ehz8-ag3n.json?$limit=50000"
    ehz8 = fetch_data(ehz8_url)
    ehz8_projects = set(ehz8['proj_num'].dropna())

    # Join on project number
    kizb_matches = wcsa_projects.intersection(kizb_projects)
    ehz8_matches = wcsa_projects.intersection(ehz8_projects)

    print(f"kizb-nxtu distinct matched project numbers: {len(kizb_matches)}")
    print(f"ehz8-ag3n distinct matched project numbers: {len(ehz8_matches)}")

    # Check for borough key
    borough_keys = ['borough', 'boro', 'borough_code', 'boro_code']
    found_keys = [col for col in borough_keys if col in wcsa.columns]
    print(f"Borough keys in wcsa-vkhf: {found_keys}")
    if not found_keys:
        print("Confirmed: wcsa-vkhf has no borough key.")

if __name__ == "__main__":
    main()
```
**Output:**
```bash
Fetching wcsa-vkhf...
Distinct wcsa-vkhf project numbers: 2609
Fetching kizb-nxtu...
Fetching ehz8-ag3n...
kizb-nxtu distinct matched project numbers: 2608
ehz8-ag3n distinct matched project numbers: 2288
Borough keys in wcsa-vkhf: []
Confirmed: wcsa-vkhf has no borough key.
```

### Step 7: Adversarial Alteration Test (`adversarial_v2.py`)
Code implemented simulating an alteration in a deep copy of the raw snapshot data ($10M injected on a single non-MWBE vendor) to ensure the variance triggers the comparison module.

**Source Code:**
```python
import json, sys
import reproduce_paper2

with open('snapshot/gpsc-qqsz_FY2022-2024.json', 'r') as f:
    orig_data = json.load(f)

mod_data = json.loads(json.dumps(orig_data))

altered = False
for row in mod_data:
    if row.get('vendor_is_a_mwbe') != 'Y' and row.get('contract_amount') is not None:
        try:
            val = float(row['contract_amount'])
            if val > 0:
                row['contract_amount'] = str(val + 10000000.0)
                print(f"Altered vendor {row.get('vendor_name')} contract_amount from {val} to {val + 10000000.0}")
                altered = True
                break
        except:
            pass

if not altered:
    print("Could not alter data")

s_orig = reproduce_paper2.stats(orig_data)
s_mod = reproduce_paper2.stats(mod_data)

drift = reproduce_paper2.compare(s_orig, s_mod, "original", "modified")
if drift:
    print("Drift detected:")
    for m in drift:
        print("  " + m)
    sys.exit(1)
else:
    print("No drift detected.")
    sys.exit(0)
```
**Output & Exit Code:**
```bash
Altered vendor 11 ENVIROGROUP LLC contract_amount from 1189080.0 to 11189080.0
Drift detected:
  2022.face_total: original=54698007774.6900 vs modified=54708007774.6900 (tol 5.4698e+06)
```
Exit code: `1`

## Findings
*   **Identifier:** F-AA-R6-01
*   **Severity:** MEDIUM
*   **Locus:** `Bayyinah_AllocationAsymmetry_AuditCompanion.md` Header (Line 3)
*   **Substance (Surface vs. Substrate):** The companion document's header explicitly states "Companion to: *Bayyinah: Public-Ledger Allocation and Asymmetric-Measure Audits* (the reader-facing note, v0.4)." Meanwhile, the Current State block correctly cites "Artifact state: v0.5 reader note," and the reader note itself states "Working draft v0.5." This is a surface-level divergence indicative of a failure to propagate artifact version numbers completely across documents. It does not affect the core data substrate or statistical validity of the paper.
*   **Disposition:** Needs correction to ensure consistency across the artifact, updating the string from `v0.4` to `v0.5` in the opening companion text.
*   **Cross-reference:** F-AA-R5-C-04 (Version propagation update)

## Regression Scope Review
- **Estimand & Stock/Flow Integrity:** Validated. Stock estimates confirmed pre-2024 award face share at 91.7%, strictly preserving difference against flow. No vintage aggregation faults found.
- **MWBE Limitations:** The limitations are properly framed and do not cross into invalid operational claims (e.g. goal-attainment proxying).
- **Concentration Explanations:** Only non-culpable, structural insights derived from valid Gini calculations (Vendor Gini face 0.931, vendor Gini expenditure 0.904).
- **Fingerprint Method:** Exact execution matching the 18-field definition (ignoring fiscal_year_end_date, amount_expended_for_fiscal_year, amount_expended_to_date, current_or_outstanding_balance). Zero all-field overlap validated.
- **Provenance Discrepancies:** Fully separated to match F-AA-R5-C-03 (Split face/count). First-party exact mismatch percentages perfectly correspond.
- **Zero Counter:** Confirmed one single zero-convergence counter in the file, with no dual-language statements. F-AA-R5-C-02 successfully regressed.
- **Section 8 Consistency:** Passed. F-AA-R5-C-01 correctly states section configurations.
- **Artifact Version Consistency:** Partially passed. Artifacts align between abstracts, current state, and sections, BUT a new defect was discovered on the Companion document header (Line 3, stating v0.4 vs Current State stating v0.5). Sourced as F-AA-R6-01.

---

# Bismillah ir-Rahman ir-Rahim
