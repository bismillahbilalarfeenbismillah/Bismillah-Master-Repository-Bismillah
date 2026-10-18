# Bismillah ir-Rahman ir-Rahim

# R0478 -- Bayyinah al-Mizan -- Reproduction Package (v0.1)

**Chronological Index:** 776 of 995  
**Date:** Undated  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** README.md  
**Source Format:** md  
**SHA-256:** `a4946efa6fc4cd8c2f11984128363b2ce58d1d57e9ccb45894b280f1744d6eda`  

---

## R0478 · Bayyinah al-Mizan -- Reproduction Package (v0.1)

- section: VI. Applied Audits & Public-Data Studies
- source_file: README.md
- source_format: md
- text_sha256: a4946efa6fc4cd8c2f11984128363b2ce58d1d57e9ccb45894b280f1744d6eda

# Bayyinah al-Mizan -- Reproduction Package (v0.1)

Structural Honesty Verification of the U.S. federal improper-payment MEASUREMENT.

This package does NOT re-detect improper payments (that needs protected claims data). It
verifies the coverage, reconciliation, and completeness integrity of the government's own
published estimate on PaymentAccuracy.gov, against the substrate of federal spending and the
government's own PIIA-compliance determinations. It measures; it does not accuse.

## Contents
- `reproduce_mizan.py` -- default verifies the frozen seed snapshot (government-wide rates +
  HHS integrity facts + SHA-256 hashes); `--live` re-pulls all 40 agencies x 5 years of
  `/agency/{CODE}/{YEAR}.html` and extracts program/agency series + PIIA compliance; `--selftest`
  perturbs each of the 17 checked values (5 gov rates + 9 rollup + 3 HHS) and confirms detection.
- `snapshot/` -- frozen raw captures (government-wide numbers page + HHS FY2024 page).
- `data/mizan_seed_snapshot.json` -- parsed seed values + hashes + sitemap map (1,679 pages).

## Run
    python3 reproduce_mizan.py            # snapshot verify (offline, byte-deterministic)
    python3 reproduce_mizan.py --selftest # perturbation detection
    python3 reproduce_mizan.py --live     # full re-pull from PaymentAccuracy.gov

## Sources (all public)
PaymentAccuracy.gov (substrate); GAO improper-payment reports + agency financial reports
(reconciliation targets); OMB Circular A-123 Appendix C (declared methodology); USAspending
(outlay denominator for coverage).

## Status
v0.1 pre-audit. Not yet through Standing Rule 7 review. No figure is converged or policy-ready.

---

# Bismillah ir-Rahman ir-Rahim
