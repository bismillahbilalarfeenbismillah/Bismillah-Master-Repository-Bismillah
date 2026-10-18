# Bismillah ir-Rahman ir-Rahim

# R0479 -- Companion Dataset: NYC DOE Fair Student Funding (FSF) FY2023 Five-School Recompute

**Chronological Index:** 286 of 995  
**Date:** 2026-07-18  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** README.md  
**Source Format:** md  
**SHA-256:** `184440f90d7f146b12fe499710143de3c50e9a11fe7bc90d804d70ed03fc802f`  

---

## R0479 · Companion Dataset: NYC DOE Fair Student Funding (FSF) FY2023 Five-School Recompute

- section: VI. Applied Audits & Public-Data Studies
- source_file: README.md
- source_format: md
- text_sha256: 184440f90d7f146b12fe499710143de3c50e9a11fe7bc90d804d70ed03fc802f

# Companion Dataset: NYC DOE Fair Student Funding (FSF) FY2023 Five-School Recompute

Companion dataset to: Bilal Syed Arfeen (BayyinahEnterprise), *Bayyinah at-Taʿlīm: Structural Honesty Verification for Educational Fairness Systems, from Primary Schooling to Graduate Research*, Draft Application Note v1.0 (currently v1.0-rc6), Section 4.4.6 and Findings F-ED-10, F-ED-13, F-ED-14. This dataset exists to discharge two open action items: Finding F-ED-11 (archiving the underlying five-school extract and mastersheet rows so the FY2023 FSF recompute is independently reproducible by a second party rather than single-instance) and Finding F-ED-13's Next Audit Cycle note (b) (archiving the category-level Detail Report data so the full formula-reconstruction walkthrough, not just the top-level line items, is independently reproducible).

## What this dataset is

Six files: four small CSV files (5 rows, or one row per subcategory per sample school), two Python recompute scripts, and one supporting reference table:

1. **`five_school_fsf_fy2023_detail_report_extract.csv`** — the disclosed walkthrough components of each school's Total FY2023 Fair Student Funding allocation, as reported by the NYC DOE Fair Student Funding Public App's FSF Detail Report for each school, obtained via direct browser interaction (the app is rendered through ASP.NET WebForms postbacks and is not retrievable via a plain HTTP request). Columns: prior-year (FY2022) register, system base rate per pupil, teacher-salary change, register-change adjustment, the fixed $225,000 foundation amount, and three collective-bargaining/state-aid adjustment terms, plus the DOE's own reported Total FY2023 FSF Allocation for cross-check.
2. **`five_school_comptroller_mastersheet_rows.csv`** — the exact rows for the same five schools extracted from the [NYC Comptroller's FY2023/FY2024 School Budget Allocations Mastersheet](https://comptroller.nyc.gov/wp-content/uploads/2023/09/School-Budget-Allocations-Mastersheet-8-29-2023.xlsx) (downloaded 2026-07-19; "Reference" sheet), covering Enrollment/FSF/Register Relief/All Other/Total for FY2023 Initial, FY2023 Final, and FY2024 Initial (plus Hold Harmless where applicable).
3. **`five_school_fsf_fy2023_category_level_register_detail.csv`** — new, added to discharge F-ED-13's Next Audit Cycle note (b). The category-level Weighted Register Formula breakdown (Grade Weight; Academic Intervention/Poverty; English Language Learner/ELL; Special Education Services; Portfolio, with every published subcategory) for all five schools, in long/tidy format: one row per (school, category group, subcategory), with register count, dollar amount, and a `value_source` column tagging each row `reported` (read directly off the rendered Detail Report) or `inferred_zero` (subcategory not itemized in the browsing pass; zero inferred because the category-group subtotal is fully accounted for by the reported nonzero lines, consistent with the source narrative's explicit "all in X" / "= 0" language for the remaining lines). Includes a per-school `TOTAL` row (weighted register and amount) as directly reported by the app, for cross-check against file (1).
4. **`fsf_recompute.py`** — the exact computation used to reconstruct each school's Total FY2023 FSF Allocation from column (1) and compare it against column (2)'s Initial and Final figures. Running it reproduces the paper's reported $2-$18 (rounding) match to the DOE's own published total and the exact match to the mastersheet's "FY2023 Initial" column.
5. **`fsf_category_level_recompute.py`** — new. Cross-checks file (3) two ways: (a) the category-level sub-lines sum to the reported per-school TOTAL row (within $0-$2, rounding in the DOE's own published sub-line dollars); (b) the F-ED-13 mechanistic walkthrough reconstruction — (FY2022 register x FY2022 base rate) + teacher-salary-change + register-change adjustment + foundation + collective-bargaining terms — lands within $2-$18 of the DOE's own reported grand total for all five schools, and the teacher-salary-change term matches the F-ED-14 identity (fy22_register x (FY2023 rate - FY2022 rate)) to under $1 for all five schools.
6. **`fsf_fy2023_weights_percapitas.xlsx`** — supporting reference: the FY2023 "Fair Student Funding Per Capitas" (SAM 1.1f) weight and per-capita dollar table, downloaded from [NYC Public Schools' FY2023 FSF SAM page](https://www.nycenet.edu/offices/finance_schools/budget/DSBPO/allocationmemo/fy22_23/fy23_docs/fy2023_Weights.xlsx), included because it is the formula parameter table referenced throughout the recompute methodology, even though it is not itself school-specific.

## Sample schools

| DBN | School name | District |
|---|---|---|
| 28Q160 | P.S. 160 Walter Francis Bishop | 28 (Queens) |
| 10X085 | P.S. 085 Great Expectations | 10 (Bronx) |
| 30Q258 | Energy Tech High School | 30 (Queens) |
| 14K488 | Brooklyn Preparatory High School | 14 (Brooklyn) |
| 30Q148 | P.S. 148 Queens | 30 (Queens) |

Sample selection: convenience sample of five schools with FY2023 FSF Detail Reports retrievable through the DOE Public App during data collection; not randomly drawn, not representative of the roughly 1,500 FSF-funded schools citywide. Any generalization beyond these five schools is explicitly out of scope, per the paper's own F-ED-10/F-ED-11 disclosures.

## Provenance and extraction method

- **FSF Detail Report figures** (files 1 and 3): NYC DOE Fair Student Funding Public App, [`OverviewReports.aspx`](https://www.nycenet.edu/publicapps/Offices/FSF/OverviewReports.aspx) / [`FSFDetail.aspx`](https://www.nycenet.edu/publicapps/Offices/FSF/FSFDetail.aspx), FY2023 report vintage, extracted via browser automation on 2026-07-18/19. This app returns `robots.txt`-disallowed to unauthenticated automated HTTP requests; a real browser session executing the page's JavaScript postbacks is required, which is why this dataset is being archived rather than relying on future readers re-running the same extraction. Navigation path for file (3): fiscal-year dropdown set to "2022-2023" (=FY2023), school name typed into the autocomplete search box (the raw DBN, e.g. "28Q160", returns no matches; the search requires the school name), GO triggers an ASP.NET `__doPostBack` to `Report.aspx?type=d&year=2023&schoolcode=<CODE>`, and "Expand All & Collapse" reveals every category subcategory row.
- **Comptroller mastersheet rows** (file 2): [NYC Comptroller, "School Budget Allocations Mastersheet," September 2023](https://comptroller.nyc.gov/wp-content/uploads/2023/09/School-Budget-Allocations-Mastersheet-8-29-2023.xlsx). As of this dataset's creation, automated (non-browser) requests to this URL are intermittently blocked by an Incapsula/Imperva bot-detection challenge; the file was obtained via a successful direct download and the five rows above extracted from its "Reference" sheet.
- **Weight/per-capita table** (file 6): [NYC Public Schools, FY2023 FSF Per Capitas, SAM 1.1f](https://www.nycenet.edu/offices/finance_schools/budget/DSBPO/allocationmemo/fy22_23/fy23_docs/fy2023_Weights.xlsx), and cross-checked against the identical table in the [FY2023 FSF Guide](https://www.nycenet.edu/offices/finance_schools/budget/DSBPO/allocationmemo/fy22_23/fy23_docs/FY2023_FSF_Guide.pdf), Chapter 4.1.3.
- **DOE FSF Working Group Meeting 3 base-weight deck**, cited by the parent paper for F-ED-14 (the $4,223.00 FY2022 / $4,197.19 FY2023 base rates): [infohub.nyced.org](https://infohub.nyced.org/docs/default-source/default-document-library/fsf-working-group_meeting-3.pdf). Not archived as a file in this package (it is a stable DOE-hosted PDF, not paywalled or robots-disallowed), but the exact URL is recorded here for reproducibility.

## Note on the category-level file's `value_source` column

File (3)'s `reported` rows were read directly off the rendered Detail Report during the browsing session. Its `inferred_zero` rows were not individually screen-read; they are subcategories the source narrative described as "all in X" or explicitly "= 0" for the remaining lines, and which the reported category-group subtotal (also archived, and cross-checked in `fsf_category_level_recompute.py`) is fully accounted for without them. This distinction is disclosed rather than presented as uniformly screen-verified, consistent with this paper's own citation-provenance discipline (F-ED-11).

## Known limitation carried over from the paper

This recompute is Tier 2 (Structural), not Tier 1 (byte-deterministic), by the paper's own Section 3 definition: reproducing the DOE's published total requires disclosing which report vintage (Initial versus Final) is being matched, a disclosed parameter choice rather than a parameter-free operation. It is a five-school demonstration, not a system-wide audit, and should not be read as validating FSF formula fidelity across all FSF-funded schools. See the paper's F-ED-10 and F-ED-11 for the full disclosure.

## How to reproduce

```
python3 fsf_recompute.py
python3 fsf_category_level_recompute.py
```

`fsf_recompute.py` prints, for each school: the recomputed total from the walkthrough components, the DOE's own reported total, the difference (should be $2-$18, rounding only), and the comparison against the Comptroller mastersheet's Initial and Final FSF columns.

`fsf_category_level_recompute.py` prints, for each school: the category-line sum versus the reported category-level TOTAL (should be $0-$2), the mechanistic walkthrough reconstruction from category-level inputs versus the DOE's own reported grand total (should be $2-$18), and the teacher-salary-change identity check underlying F-ED-14 (should be under $1).

## License

The underlying figures are public records published by the NYC Department of Education and the NYC Comptroller's Office and are not subject to copyright as U.S. government/municipal works. This compilation (selection, extraction, and computation script) is released under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) — reuse is permitted with attribution to this dataset and to the parent paper.

## Citation

Arfeen, Bilal Syed (2026). *Companion Dataset: NYC DOE Fair Student Funding (FSF) FY2023 Five-School Recompute*, companion to *Bayyinah at-Taʿlīm* v1.0 (rc6 revision, category-level data added). BayyinahEnterprise.

## Related work

Companion papers by the same author/lineage (Zenodo DOIs): Bayyinah at-Tartīb (10.5281/zenodo.20070782); Al-Mutaffifīn (10.5281/zenodo.19894724); Structural Honesty Verification: A New Frontier (10.5281/zenodo.20131072); Bayyinah al-Munāsabāt (10.5281/zenodo.20069654); Cross-Text Computational Linguistics (10.5281/zenodo.19961267).

---

# Bismillah ir-Rahman ir-Rahim
