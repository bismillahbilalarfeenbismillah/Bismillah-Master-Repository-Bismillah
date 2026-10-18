# Bismillah ir-Rahman ir-Rahim

# R0413 -- Bayyinah al-Mizan -- Citation Ledger v1.0 (standalone)

**Chronological Index:** 10 of 995  
**Date:** 2024  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** Bayyinah_al-Mizan_CitationLedger_v1.0.md  
**Source Format:** md  
**SHA-256:** `95587925f2ecaafda5d95ecdf1ef76d3b52823f08171e1846d34d77fa59486ca`  

---

## R0413 · Bayyinah al-Mizan -- Citation Ledger v1.0 (standalone)

- section: VI. Applied Audits & Public-Data Studies
- source_file: Bayyinah_al-Mizan_CitationLedger_v1.0.md
- source_format: md
- text_sha256: 95587925f2ecaafda5d95ecdf1ef76d3b52823f08171e1846d34d77fa59486ca

# Bayyinah al-Mizan -- Citation Ledger v1.0 (standalone)

Claim-by-claim citation ledger for *Bayyinah al-Mizan: An Audit of the Audit* (v1.0). One row per distinct load-bearing claim, with its tier, reported value, and primary source. This is the standalone ledger artifact whose absence was finding F-MZ-R2-001; it supersedes the earlier v0.1 ledger and matches v0.5's inline citations (Federal News Network and civicintelligence.news removed; CRS moved to the official endpoint; direct GAO-26-108694 added for the FY2025-cycle wording). Snapshot hashes are byte-verified and match an independent Perplexity capture and the reproduction package MANIFEST.

| # | Section | Tier | Claim | Value | Source | URL |
|---|---|---|---|---|---|---|
| 1 | Governance | -- | Framework / Tier discipline import | Al-Mutaffifin | Zenodo | https://doi.org/10.5281/zenodo.19894724 |
| 2 | Governance | -- | Companion, formula-fidelity | at-Ta'lim | Zenodo | https://doi.org/10.5281/zenodo.21436484 |
| 3 | Governance | -- | Companion, provenance-integrity | al-Amana | Zenodo | https://doi.org/10.5281/zenodo.21446613 |
| 4 | Governance | -- | al-Amana ledger (converged) | -- | Zenodo | https://doi.org/10.5281/zenodo.21446618 |
| 5 | Governance | -- | Companion, MTA procurement | AllocationAsymmetry | Zenodo | https://doi.org/10.5281/zenodo.21445552 |
| 6 | 1 | T1 | FY2024 improper payments | $162B / 16 agencies / 68 programs | GAO-25-108172 (matches paper Section 1; GAO-25-107753 is the equivalent FY2024 report) | https://files.gao.gov/reports/GAO-25-108172/index.html |
| 7 | 1 | T1 | FY2025 improper payments | $186B / 15 agencies / 64 programs | GAO-26-108694 | https://www.gao.gov/products/gao-26-108694 |
| 8 | 1 | T1 | Cumulative to FY2024 cycle | ~$2.8T | GAO-25-108172 | https://files.gao.gov/reports/GAO-25-108172/index.html |
| 9 | 1 | T1 | Cumulative to FY2025 cycle | ~$3.0T | GAO-26-108694 | https://www.gao.gov/products/gao-26-108694 |
| 10 | 1/4.5 | T2 | CRS synthesis | ~half noncompliant; 77% in 5 areas | CRS R48296 | https://crsreports.congress.gov/product/pdf/R/R48296 |
| 11 | 4.1 | T1 | Government-wide rate series | improper 7.05/4.44/4.40/3.66/3.83% | PaymentAccuracy.gov The Numbers | https://paymentaccuracy.gov/the-numbers/ |
| 12 | 4.2 | T1 | FY2025 rollup coverage | 83 / 15 / $4,473.7B | PaymentAccuracy.gov Agencies+Programs | https://paymentaccuracy.gov/agencies-and-programs |
| 13 | 4.2 | T1 | Reconciliation gap | implied $171.7B vs $186B = $14.3B / 7.7% | computed, reproduce_mizan.py | (package) |
| 14 | 4.2 | T1 | Total FY2025 outlays | ~$7,010B | Treasury FY2025 Combined Statement | https://fiscal.treasury.gov/system/files/files/reports-statements/combined-statement/cs2025/2025-cs-final.pdf |
| 15 | 4.2 | T2 | Net interest (CBO basis, used) | ~$1,028B | CBO MBR FY2025 | https://www.cbo.gov/system/files/2025-11/61307-MBR-FY25-final.pdf |
| 16 | 4.2 | T2 | Coverage ratio, both bases | 74.79% (CBO) / 74.07% (Treasury) | computed | (package) |
| 17 | 4.3 | T1 | FY2024 top-5 concentration | $121B / 75% | GAO-25-108172 | https://files.gao.gov/reports/GAO-25-108172/index.html |
| 18 | 4.3 | T1 | FY2025 top-5 concentration | $136B / 73% | Treasury FY2025 Independent Auditor's Report | https://fiscal.treasury.gov/system/files/2026-03/gao-audit-report-2025.pdf |
| 19 | 4.3 | T1 | HHS share of implied total | $97.4B / 56.7% | computed, reproduce_mizan.py | (package) |
| 20 | 4.4 | T1 | HHS PIIA non-compliance | non-compliant, 3 years, 195 programs | PaymentAccuracy.gov HHS FY2024 | https://paymentaccuracy.gov/agency/HHS/2024.html |
| 21 | 4.5 | T1 | CFO Act agencies noncompliant FY2024 | 12 of 24 (5 + 7) | Treasury FY2025 Independent Auditor's Report | https://fiscal.treasury.gov/system/files/2026-03/gao-audit-report-2025.pdf |
| 22 | 5.1 | T2 | Reporting-universe counts | FY2024 16/68; FY2025 15/64 | GAO-25-108172 / Treasury FY2025 audit | https://files.gao.gov/reports/GAO-25-108172/index.html |
| 23 | 5.4 | T2 | FY2025 overpayments share | ~$153B / 82% | GAO-26-108694 | https://www.gao.gov/products/gao-26-108694 |
| 24 | 8 | T1 | Snapshot integrity (SHA-256) | numbers 36ea0949; agencies-and-programs 474a3b51; HHS 47ddd449 | reproduce_mizan.py MANIFEST | (package) |
| 25 | 4.3 | T2 | SBA/TANF/HUD programs did not report a required estimate in a recent year | GAO written testimony | https://oversight.house.gov/wp-content/uploads/2026/01/Thomas-GAO-Written-Testimony.pdf |

Notes: URLs behind WAF gating (CBO MBR, some GAO product pages) return HTTP 403 to automated fetch but resolve in a browser; values are confirmable via alternate fetch paths. Rows 13, 16, 19, 24 are computed by the reproduction package from the frozen snapshot, not cited to an external page.

---

# Bismillah ir-Rahman ir-Rahim
