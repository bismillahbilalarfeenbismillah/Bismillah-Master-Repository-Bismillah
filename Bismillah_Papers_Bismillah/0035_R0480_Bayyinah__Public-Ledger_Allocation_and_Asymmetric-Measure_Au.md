# Bismillah ir-Rahman ir-Rahim

# R0480 -- Bayyinah: Public-Ledger Allocation and Asymmetric-Measure Audits -- Reproduction and Audit Dataset (v1.0)

**Chronological Index:** 35 of 995  
**Date:** 2024  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** README.md  
**Source Format:** md  
**SHA-256:** `2bb1d161a3f4ba05bd3758efa535ae631a95736bfa94796c416de4611ce00dd3`  

---

## R0480 · Bayyinah: Public-Ledger Allocation and Asymmetric-Measure Audits -- Reproduction and Audit Dataset (v1.0)

- section: VI. Applied Audits & Public-Data Studies
- source_file: README.md
- source_format: md
- text_sha256: 2bb1d161a3f4ba05bd3758efa535ae631a95736bfa94796c416de4611ce00dd3

# Bayyinah: Public-Ledger Allocation and Asymmetric-Measure Audits -- Reproduction and Audit Dataset (v1.0)

This dataset accompanies the canonical v1.0 release and lets any party reproduce every figure in the paper and inspect the full nine-round cross-instance audit trail.

## Related deposits

- Reader note (paper): DOI 10.5281/zenodo.21445552
- Audit and provenance ledger: DOI 10.5281/zenodo.21445556
- This dataset is deposited alongside the ledger (DOI 10.5281/zenodo.21445556).

## Contents

- `reproduce_paper2.py` -- verifies the snapshot hash and recomputes every published statistic on both estimands for all three fiscal years. Supports `--live` (re-pull from the New York State open-data portal and compare) and `--selftest` (perturb each statistic and confirm the comparator detects it).
- `snapshot/gpsc-qqsz_FY2022-2024.json` -- the frozen three-year extract (37,988 records: FY2022 12,156; FY2023 12,114; FY2024 13,718) that every figure is computed from.
- `snapshot/MANIFEST.json` -- the SHA-256 of the snapshot and the 22-field row-present inventory. The script aborts if the snapshot does not match this hash.
- `audit-reports/` -- the raw primary auditor outputs for all nine rounds (F-AA-R1 through F-AA-R9), organized by round, including each Model Council member report and each synthesis. These are the source records behind the ledger's summaries.

## How to reproduce

Requires Python 3 (standard library only).

```
python3 reproduce_paper2.py            # offline: verify hash, recompute all figures from the frozen snapshot
python3 reproduce_paper2.py --selftest # confirm the comparator detects all deliberate perturbations
python3 reproduce_paper2.py --live     # re-pull all three years from data.ny.gov and compare to the snapshot
```

The offline run needs no network. The `--live` run queries the community view `gpsc-qqsz` on `data.ny.gov`; the frozen snapshot and its hash, not the live endpoint, are what the reproduction rests on, so results are stable even if the live portal later changes.

## Expected top-line values (FY2024, community view gpsc-qqsz)

- Total rows across the three vintages: 37,988
- Face-value total (`contract_amount`): $65,189,755,228.64
- Annual-expenditure total (`amount_expended_for_fiscal_year`): $8,170,228,558.54
- MWBE prime-vendor shares: 18.7345% by count, 3.9532% by face value, 7.0612% by annual expenditure
- Face concentration: top-10 30.4151%; vendor Gini (positive-face basis) 0.93117 (face), 0.90435 (annual expenditure)
- Pre-2024 award share of FY2024 face value: 91.6876%
- Missing `contract_amount`: 1,348; explicit-zero: 48
- Vintage-overlap fingerprint (18-field method, pairwise): 2,115 / 604 / 1,002; exact all-field overlap: 0
- Provenance: gpsc-qqsz 13,718 rows / $65.19B vs first-party twsw-2mqa 13,648 rows / $65.13B (face divergence about 0.089%, record-count divergence about 0.51%)

## Audit trail summary

The artifact converged after nine independent cross-instance audit rounds under BayyinahEnterprise Audit Framework v3.0, Standing Rule 7 (two consecutive qualifying passes by non-producer auditors, executed reproduction, zero critical and zero high). Rounds 1-3 were NON-PASS (interpretive overreach, then producer status-propagation defects); round 4 was a consistency-only pass not credited; round 5 was NON-PASS (package absent from the packet); round 6 was the first qualifying executed-reproduction pass; round 7 was NON-PASS on a producer status-propagation defect that reset the count; rounds 8 and 9 were two consecutive qualifying passes (three qualifying members each: GPT 5.5, GPT 5.4, Gemini 3.1 Pro; the Claude producing-lineage member quarantined). Convergence caveats are recorded honestly in the ledger Current State: the two decisive passes shared the same three-member set (independence between them rests on fresh instances, not disjoint membership), and they audited materially-identical substance. The `audit-reports/` folder contains the primary records so the ledger's account can be checked against source.

---

# Bismillah ir-Rahman ir-Rahim
