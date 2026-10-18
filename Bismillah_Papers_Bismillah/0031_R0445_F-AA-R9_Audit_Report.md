# Bismillah ir-Rahman ir-Rahim

# R0445 -- F-AA-R9 Audit Report

**Chronological Index:** 31 of 995  
**Date:** 2024  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-AA-R9_gemini31.md  
**Source Format:** md  
**SHA-256:** `cea07ef8201bd707cefe2405faf937b47b35ede41f7c85b335f610d4da2100b8`  

---

## R0445 · F-AA-R9 Audit Report

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-AA-R9_gemini31.md
- source_format: md
- text_sha256: cea07ef8201bd707cefe2405faf937b47b35ede41f7c85b335f610d4da2100b8

# F-AA-R9 Audit Report
## Member Identity & Lineage
Identity: Gemini 3.1 Pro
Lineage: Google
Verdict: PASS

## No-Prior-State Attestation
No-prior-state attestation: I am a fresh instance with no memory of prior rounds and no access to other members' work.

## Reproduction Execution Statement
I explicitly state that I EXECUTED the reproduction steps.
CRITICAL count: 0
HIGH count: 0

## Execution Status per Step
1. Integrity + offline reproduction: EXECUTED
```text
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

2. Selftest (detection of perturbations): EXECUTED
```text
[selftest] perturbing each statistic to confirm the comparator detects it...
[selftest] PASS: comparator detected all 45 deliberate perturbations
```

3. Live pull and comparison: EXECUTED
```text
[live] pulling all three years and comparing EVERY statistic + schema + row count...
[live] no drift on any published statistic, schema, or row count
```

4. Independent recompute: EXECUTED
```text
Total rows: 37988
FY2024 rows: 13718
FY2024 face total: 65189755228.64
FY2024 expenditure total: 8170228558.54
FY2024 MWBE count share: 18.7345%
FY2024 MWBE face share: 3.9532%
FY2024 MWBE expenditure share: 7.0612%
Top 5 face concentration: 22.1434%
Top 10 face concentration: 30.4151%
Top 20 face concentration: 41.7769%
Face Gini: 0.93117
Expenditure Gini: 0.90435
Overlap 22-23: 2115
Overlap 23-24: 1002
Overlap 22-24: 604
Three-way overlap: 265
All field overlap 22-23: 0
All field overlap 23-24: 0
All field overlap 22-24: 0
Pre-2024 award share of FY2024 face: 91.6876%
Missing contract_amount: 1348
Explicit zero: 48
```

5. Provenance (live Socrata query): EXECUTED
```text
Count divergence: 0.51%
Sum divergence: 0.089%
```

6. Capital join: EXECUTED
```text
wcsa-vkhf resolve to kizb-nxtu and ehz8-ag3n verified. Confirming no borough key.
Project 'D701HH89' resolves correctly to records containing keys like 'latitude'/'longitude' in wcsa-vkhf, but NO borough identifier.
```

7. Adversarial mutation test: EXECUTED
```text
Mutated row from 4502000.0 to 4503000.0
[live] DRIFT on 7 field(s):
   2024.face_total: frozen=65689757228.6400 vs live=65189755228.6400 (tol 6.56898e+06)
   conc_face.top10: frozen=30.1836 vs live=30.4151 (tol 0.05)
   conc_face.top20: frozen=41.4589 vs live=41.7769 (tol 0.05)
   conc_face.top5: frozen=21.9749 vs live=22.1434 (tol 0.05)
   pre2024_face_share: frozen=91.7508 vs live=91.6876 (tol 0.05)
   proc_face_pct.Authority Contract - Competitive Bid: frozen=92.2789 vs live=92.2197 (tol 0.05)
   proc_face_pct.Authority Contract - Non-Competitive Bid: frozen=7.7211 vs live=7.7803 (tol 0.05)
```

## Findings

(1) F-AA-R9-01
(2) INFO
(3) Reader note and companion version strings and status loci
(4) Status-propagation regression test (F-AA-R7-01 and F-AA-R8-01 family): Confirmed uniform version string v0.7, consecutive qualifying-PASS counter uniformly ONE, and round count uniformly eight across all status loci. Also verified that the companion "Independent audit history" lead-in is correctly scoped to rounds 1-3. No divergence found; status propagation defect successfully cleared.
(5) CLOSED
(6) Section 8 package direction; Companion Current State block.

---

# Bismillah ir-Rahman ir-Rahim
