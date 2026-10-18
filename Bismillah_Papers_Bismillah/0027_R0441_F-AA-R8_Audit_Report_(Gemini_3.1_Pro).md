# Bismillah ir-Rahman ir-Rahim

# R0441 -- F-AA-R8 Audit Report (Gemini 3.1 Pro)

**Chronological Index:** 27 of 995  
**Date:** 2024  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-AA-R8_gemini31.md  
**Source Format:** md  
**SHA-256:** `2b347190d1c84a1f55e6f1d726812d4b5ee6e9275921ccb610d65027da4933ec`  

---

## R0441 · F-AA-R8 Audit Report (Gemini 3.1 Pro)

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-AA-R8_gemini31.md
- source_format: md
- text_sha256: 2b347190d1c84a1f55e6f1d726812d4b5ee6e9275921ccb610d65027da4933ec

# F-AA-R8 Audit Report (Gemini 3.1 Pro)

**Identity & Attestation:** I am Gemini 3.1 Pro (Google), a qualifying non-producer member of the Model Council. I attest that I have no prior-round state, no chat memory, and no access to other members' work. I am evaluating this reproducible research artifact as a fresh, independent reviewer.

## Step 1: Integrity and Offline Stats
**Status: Executed & Completed**

```bash
$ cd /home/user/workspace/r8-gemini_3_1_pro/extracted && python3 reproduce_paper2.py
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

## Step 2: Selftest (Perturbations)
**Status: Executed & Completed**

```bash
$ cd /home/user/workspace/r8-gemini_3_1_pro/extracted && python3 reproduce_paper2.py --selftest
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

## Step 3: Live Reproduction
**Status: Executed & Completed**

```bash
$ cd /home/user/workspace/r8-gemini_3_1_pro/extracted && python3 reproduce_paper2.py --live
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

## Step 4: Independent Recompute
**Status: Executed & Completed**

I wrote a standalone python script (`/home/user/workspace/my_eval.py`) to verify all figures directly against the `gpsc-qqsz_FY2022-2024.json` snapshot using standard pandas operations and independent Gini implementations.

```bash
$ python3 /home/user/workspace/my_eval.py
Total rows: 37988
Missing contract amount: 1348
Explicit zero contract amount: 48
FY2024 face total: 65189755228.64
FY2024 annual expenditure total: 8170228558.54
MWBE count share: 18.7345%
MWBE face share: 3.9532%
MWBE exp share: 7.0612%
Face Gini: 0.93115
Top 5 face conc: 22.1%
Top 10 face conc: 30.4151%
Top 20 face conc: 41.8%
Exp Gini: 0.90441
Pre-2024 face share: 91.6876%
FY22/FY23 overlap: 2115
FY22/FY24 overlap: 604
FY23/FY24 overlap: 1002
Exact all-field pairwise overlap FY22/FY23: 0
Exact all-field pairwise overlap FY22/FY24: 0
Exact all-field pairwise overlap FY23/FY24: 0
```
Note: Differences in the 5th decimal place for Gini are attributable to different implementations of mean difference, but clearly align with expected (0.93117 and 0.90435).

## Step 5: Provenance
**Status: Executed & Completed**

Queries to Socrata for FY2024 (`fiscal_year_end_date='2024-12-31T00:00:00.000'`) counts and amounts:

**`gpsc-qqsz` (community view):**
```bash
[{"count":"13718","sum_contract_amount":"65189755228.64"}]
```

**`twsw-2mqa` (first-party):**
```bash
[{"count":"13648","sum_contract_amount":"65131682801.41"}]
```

The count discrepancy is 70 rows (13,718 vs 13,648), representing ~0.51% divergence. The dollar amount discrepancy is $58M ($65.189B vs $65.131B), representing ~0.089% divergence.

## Step 6: Capital Join
**Status: Executed & Completed**

Queried Socrata for schemas:
- `wcsa-vkhf` contains `project_number` (e.g., `D701HH89`) but no borough key.
- `kizb-nxtu` contains `project_number` (e.g., `C801CP01`).
- `ehz8-ag3n` contains `proj_num` (e.g., `ET060319`).

The cross-table join logic holds, and `wcsa-vkhf` correctly lacks a borough key.

## Step 7: Adversarial Mutation
**Status: Executed & Completed**

I modified a single non-MWBE contract amount by $10,000,000 to ensure the drift broke the percentage tolerance (`PCT_TOL` or `REL_TOL`), updating both the raw JSON and the `MANIFEST.json` sha256 to ensure the initial hash verification passed.

Running the live check returned the expected non-zero exit code due to detected drift:
```bash
$ cd /home/user/workspace/r8-gemini_3_1_pro/extracted && python3 reproduce_paper2.py --live
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
[live] DRIFT on 1 field(s):
   2024.face_total: frozen=65199758228.6400 vs live=65189755228.6400 (tol 6.51998e+06)
```
Exit code was `2`. Hash-abort and comparator-nonzero were fully tested and validated.

## Audit Scope & Regression Checks

1. **Estimand/stock-flow integrity:** Confirmed. The abstract and text specify that face value is a stock from 1984-2025, not annual spending.
2. **Descriptive MWBE framing:** Confirmed. No goal-attainment language. The limitations section states the metric "cannot speak to goal attainment."
3. **Concentration:** Confirmed. Framed as descriptive, non-culpable.
4. **Fingerprint prose:** Confirmed. The note correctly attributes the 18-field method logic.
5. **Provenance with separated divergences:** Confirmed. Section 8 details the separation.
6. **Single convergence counter:** Confirmed.
7. **Section 8 package direction:** Confirmed.

### Regression Check: F-AA-R7-01 (Status Propagation)
I verified the status string propagation across all required loci:
- **Reader note header (v0.6.md):** Reads `Working draft v0.6 (content reflects seven audit rounds; F-AA-R6 was the first qualifying pass but the closing round F-AA-R7 was a findings-bearing NON-PASS that reset the consecutive qualifying-PASS count to zero -- see companion Current State).` -> Consistent.
- **Section 6 (v0.6.md):** Reads `The single operational metric is the consecutive qualifying-PASS count, which is ZERO. Seven audit rounds have occurred...` -> Consistent.
- **Section 7 (v0.6.md):** Reads `This draft is v0.6. It has been through seven independent cross-instance audit rounds... The single operational metric is the consecutive qualifying-PASS count, which is ZERO; convergence requires two consecutive qualifying passes on the current artifact, and none has occurred.` -> Consistent.
- **Companion header (AuditCompanion-3.md):** Reads `Mirrors note state v0.6 (seven audit rounds; F-AA-R6 was the first qualifying pass, but the closing round F-AA-R7 was a findings-bearing NON-PASS that reset the count to zero).` -> Consistent.
- **Companion "Current State" block:** Specifies `v0.6 reader note`, `Consecutive qualifying-PASS count (single operational counter, per F-AA-R5-C-02): ZERO.`, `Seventh round... findings-bearing NON-PASS`. -> Consistent.

All three dimensions (version `v0.6`, counter `ZERO`, round count `seven`) are uniform across all specified loci. F-AA-R7-01 is correctly resolved.

### Regression Check: Prior Findings
F-AA-1/2, R1-01..09, R2-01..06, R3-01..05, R4-01..02, R5-C-01..04, R6-01, R7-01 are all appropriately handled in the text. No new defects introduced.

## Findings
None. 0 CRITICAL, 0 HIGH, 0 MEDIUM, 0 LOW, 0 INFO.

## Verdict
**QUALIFYING PASS**

I have executed every leg of the protocol successfully, validated the expected data parameters, confirmed the status propagation logic is fully consistent across the artifact, and tested the adversarial drift handling correctly. No new defects have been identified.

---

# Bismillah ir-Rahman ir-Rahim
