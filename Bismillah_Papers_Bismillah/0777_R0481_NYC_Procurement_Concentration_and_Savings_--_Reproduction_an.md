# Bismillah ir-Rahman ir-Rahim

# R0481 -- NYC Procurement Concentration and Savings -- Reproduction and Audit Dataset (v1.0, converged)

**Chronological Index:** 777 of 995  
**Date:** Undated  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** README.md  
**Source Format:** md  
**SHA-256:** `7059c8587be7bf7b7d777c00cbccdbf2b22499d4489d54607aa9f800856efc79`  

---

## R0481 · NYC Procurement Concentration and Savings -- Reproduction and Audit Dataset (v1.0, converged)

- section: VI. Applied Audits & Public-Data Studies
- source_file: README.md
- source_format: md
- text_sha256: 7059c8587be7bf7b7d777c00cbccdbf2b22499d4489d54607aa9f800856efc79

# NYC Procurement Concentration and Savings -- Reproduction and Audit Dataset (v1.0, converged)

## Related deposits

- Paper: DOI 10.5281/zenodo.21447217
- Audit and provenance ledger and this dataset: DOI 10.5281/zenodo.21447219

The paper converged under Audit Framework v3.0, Standing Rule 7, after three cross-instance rounds (F-PC-R1 NON-PASS, then F-PC-R2 and F-PC-R3 qualifying passes; count TWO; rotation closed by a member new to the second pass). Convergence certifies structural honesty and reproducibility, not that the savings estimate is verified recoverable.

Reproduces the concentration figures (Table 2), the addressable-base and savings arithmetic (Table 3), and the MTA cross-check of the working paper *Procurement Concentration and Recoverable Competitive Savings in New York City Contracting*.

## Contents

- `reproduce_procurement.py` -- standard-library Python. Verifies the CSV hashes, recomputes Sole Source and Negotiated Acquisition concentration (vendor count, top-N shares, Gini) on the clean vendor rows, checks the savings arithmetic, and (with `--live`) re-pulls the MTA FY2024 cross-check figures from data.ny.gov.
- `data/sole_source_vendors_fy25.csv` -- FY25 Sole Source vendor aggregation (Rank 1..106 vendors, then a TOTAL row and three footnote rows).
- `data/negotiated_acquisition_vendors_fy25.csv` -- FY25 Negotiated Acquisition vendor aggregation (Rank 1..462 vendors, then TOTAL and footnote rows).
- `data/MANIFEST.json` -- SHA-256 of both CSVs; the script aborts on mismatch.
- `audit-reports/` -- the primary auditor reports and syntheses for all three rounds (F-PC-R1/R2/R3), organized by round, the source records behind the ledger's summaries.

## How to run

```
python3 reproduce_procurement.py            # verify hashes + reproduce concentration + savings
python3 reproduce_procurement.py --live     # additionally re-pull the MTA cross-check from data.ny.gov
python3 reproduce_procurement.py --selftest # perturb each checked value; confirm all detected
```

## Method (must match to reproduce)

Vendor rows are the CSV rows whose `Rank` is a positive integer; the `TOTAL` and footnote rows the CSVs also contain are excluded. Concentration is on the positive-amount vendor basis: aggregate to one total per vendor (the CSVs are already aggregated), sort descending, take top-N shares, and compute the Gini coefficient over the vendor totals. This is the identical convention independently reproduced across the nine audit rounds of the AllocationAsymmetry paper.

## Expected results

- Sole Source: 106 vendors, $1,597,506,644.98, top-1 82.5004%, top-5 90.5858%, top-10 94.0642%, top-20 97.2606%, Gini 0.95557. Top vendor NYCEDC $1,317,949,728.
- Negotiated Acquisition: 462 vendors, $3,865,895,209.67, top-1 24.0334%, top-5 36.9178%, top-10 46.2163%, top-20 55.3833%, Gini 0.81855. Top vendor HANYC $929,104,960.
- Savings bases (official Table 7): Core $5,658,002,459; Wide $6,984,040,398; NYCEDC-adjusted $4,340,052,731.
- MTA FY2024 cross-check (from converged AllocationAsymmetry, DOI 10.5281/zenodo.21445552; reproducible live): 13,718 records, 2,656 vendors, $65,189,755,228.64 face, top-10 30.4151%, Gini 0.93117.

## Reconciliation (resolved)

The Negotiated Acquisition positive-amount total is about 4.75% ($192.96M, 27 contracts) below the official Table 7 figure of $4,058,851,691. This has been reconciled directly against the Comptroller's Appendix 1 parent-contracts microdata (publicly reachable, though the host intermittently returns HTTP 403 to automated requests). The FY2025 Appendix 1 extract contains exactly 935 Negotiated rows and 115 Sole Source rows, every one positive and vendor-named (zero blank or null names), summing to the positive-basis totals. Nothing was dropped in aggregation. The gap is between Table 7's aggregate counts (962 Negotiated, 126 Sole Source) and the parent-contracts extract (935 and 115): 27 Negotiated contracts ($192.96M) and 11 Sole Source contracts ($1.64M) are in the summary but absent from the extract -- a coverage/scope difference between the summary and the export, not attribution loss. Negotiated concentration is computed on about 95.25% of the official subgroup base.

## Refusal boundary

This package measures concentration and reproduces arithmetic. It does not judge whether any award should have been competitively bid, whether any vendor relationship is improper, or whether any dollar figure is recoverable. The savings estimate is a conditional planning range under stated assumptions, gated on the pilot the paper proposes; it is not a verified recoverable amount.

---

# Bismillah ir-Rahman ir-Rahim
