# Bismillah ir-Rahman ir-Rahim

# R0846 -- Structural Regularities in AI-Assisted Audit Chains: A Pilot Study in Predictive Finding Localization

**Chronological Index:** 199 of 995  
**Date:** 2026-05  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** README.md  
**Source Format:** md  
**SHA-256:** `8c4379d28b58ea481c0c403d8cea606efdeb388cadd4c1e3a8fc3465894c8b82`  

---

## R0846 · Structural Regularities in AI-Assisted Audit Chains: A Pilot Study in Predictive Finding Localization

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: README.md
- source_format: md
- text_sha256: 8c4379d28b58ea481c0c403d8cea606efdeb388cadd4c1e3a8fc3465894c8b82

# Structural Regularities in AI-Assisted Audit Chains: A Pilot Study in Predictive Finding Localization

**Author:** Bilal Syed Arfeen, BayyinahEnterprise
**Date:** May 2026
**License:** CC BY-NC 4.0

## Summary

This bundle contains the paper, dataset, experiment protocol,
committed predictions, and scoring documents for a pilot study
on predictive finding localization in AI-assisted audit chains.

The pilot extracts eleven structural regularities (R1-R11) from
a five-finding chain (F22-F26) in the furqan-lint Sigstore-CASM
verifier pipeline. A retrospective prediction experiment achieved
10/10 hits across five dimensions on two held-out findings, with
caveats about predictor contamination, scoring granularity, and
the absence of a cross-instance ablation.

## Files

| File | Description |
|---|---|
| `paper.md` | Full paper (markdown, submission-ready) |
| `audit_chain_log_F22_F26.csv` | Structured dataset (5 rows, 18 columns) |
| `experiment_protocol.md` | Pre-registered scoring rules and procedure |
| `test1_F25_predictions.md` | Committed predictions for F25 from F22-F24 |
| `test1_F25_scoring.md` | Ground-truth scoring for Test 1 (5/5 HIT) |
| `test2_F26_predictions.md` | Committed predictions for F26 from F22-F25 |
| `test2_F26_scoring.md` | Ground-truth scoring for Test 2 (5/5 HIT) |
| `corpus_accounting.md` | Counter reconciliation and finding inventory |
| `LICENSE` | CC BY-NC 4.0 |

## Reproducing the Experiment

1. Read `experiment_protocol.md` for the scoring rules.
2. Read `audit_chain_log_F22_F26.csv` rows F22-F24.
3. Without reading `test1_F25_scoring.md`, attempt your own
   predictions for F25 on the five dimensions (step, error code,
   substrate layer, fix-size class, root cause).
4. Compare your predictions against the ground truth in
   `test1_F25_scoring.md`.
5. Repeat for F26 using F22-F25 as input.
6. Score using the TIGHT threshold (>= 3/5 HIT).

## Related Work

- Bayyinah Audit Framework v3.0: DOI 10.5281/zenodo.20017335
- Application Brief: DOI 10.5281/zenodo.20031395
- furqan-lint: https://pypi.org/project/furqan-lint/
- Source: https://github.com/BayyinahEnterprise

## Contact

bayyinahenterprises@tuta.com

---

# Bismillah ir-Rahman ir-Rahim
