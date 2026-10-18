# Bismillah ir-Rahman ir-Rahim

# R0431 -- F-AA-R5 Model Council Closing-Round Audit

**Chronological Index:** 17 of 995  
**Date:** 2024  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-AA-R5_synthesis.md  
**Source Format:** md  
**SHA-256:** `ee4bdc1e3960962683b184860e03c52acd9c21c8ed30e19ce9833749f68cf79e`  

---

## R0431 · F-AA-R5 Model Council Closing-Round Audit

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-AA-R5_synthesis.md
- source_format: md
- text_sha256: ee4bdc1e3960962683b184860e03c52acd9c21c8ed30e19ce9833749f68cf79e

# F-AA-R5 Model Council Closing-Round Audit

Council members: GPT 5.5, Gemini 3.1 Pro, and Claude Opus 4.8. GPT 5.5 and Gemini 3.1 Pro are qualifying; Claude Opus 4.8 is producer-lineage, quarantined, advisory-only, and excluded from convergence.

## Where Models Agree

| Finding | GPT 5.5 | Gemini 3.1 Pro | Claude Opus 4.8 | Evidence |
|---|---:|---:|---:|---|
| The mandatory reproduction package was absent, so the offline, self-test, supplied live-comparator, and supplied adversarial-comparator requirements could not be completed. | ✓ | ✓ | ✓ | The public artifact links checked by the members did not expose the named package; the cited Zenodo records contain unrelated companion works ([Zenodo 21436484](https://zenodo.org/api/records/21436484), [Zenodo 19894724](https://zenodo.org/api/records/19894724), [Zenodo 20069654](https://zenodo.org/api/records/20069654)). |
| No member may return PASS under the brief’s mandatory-execution rule. | ✓ | ✓ | ✓ | All three returned INCOMPLETE or findings-bearing NON-PASS because Steps 1–3 could not be executed. |
| Independent live pulls reproduce 37,988 rows and the principal FY2024 totals and MWBE shares. | ✓ | ✓ | ✓ | FY2024 live aggregation returns 13,718 rows, $65,189,755,228.64 face value, and $8,170,228,558.54 annual expenditure ([New York Open Data aggregate](https://data.ny.gov/resource/gpsc-qqsz.json?%24select=count(*)+as+row_count,+sum(contract_amount)+as+face_total,+sum(amount_expended_for_fiscal_year)+as+exp_total&fiscal_year_end_date=2024-12-31T00%3A00%3A00.000)). |
| The first-party and community views are close in face-value dollars but not identical. | ✓ | ✓ | ✓ | The first-party view returns 13,648 rows and $65,131,682,801.41 face value ([MTA first-party aggregate](https://data.ny.gov/resource/twsw-2mqa.json?%24select=count(*)+as+row_count,+sum(contract_amount)+as+face_total,+sum(amount_expended_for_fiscal_year)+as+exp_total&fiscal_year_end_date=2024-12-31T00%3A00%3A00.000)). |
| The capital-table join is feasible and `wcsa-vkhf` has no borough field. | ✓ | ✓ | ✓ | Portal metadata exposes project and coordinate/location fields but no borough field ([wcsa-vkhf metadata](https://data.ny.gov/api/views/wcsa-vkhf)); joins resolve through `project_number` and `proj_num` in the two capital resources ([kizb-nxtu](https://data.ny.gov/resource/kizb-nxtu.json), [ehz8-ag3n](https://data.ny.gov/resource/ehz8-ag3n.json)). |
| The substantive stock/flow, prime-vendor, concentration, and no-compliance-inference framing is materially sound. | ✓ | ✓ | ✓ | The live FY2024 data support the named stock and flow estimands and the descriptive MWBE shares ([FY2024 community-view rows](https://data.ny.gov/resource/gpsc-qqsz.json?%24limit=50000&%24order=:id&fiscal_year_end_date=2024-12-31T00:00:00.000)). |

## Where Models Disagree

| Topic | GPT 5.5 | Gemini 3.1 Pro | Claude Opus 4.8 | Why They Differ |
|---|---|---|---|---|
| FY2024 face-value Gini | 0.931167744 using positive aggregated vendor face values | 0.937 using an incompletely documented variant | 0.931 using positive aggregated vendor face values | Gemini used a different or insufficiently specified denominator/filter; GPT and Claude implemented the artifact’s stated positive-face-vendor basis. |
| 18-field overlap fingerprint | 2,115 / 604 / 1,002; exact all-field overlap 0 | Reported 2,115 / 1,003 plus a separate 265 three-way overlap, not the requested pairwise triplet | 2,115 / 604 / 1,002; exact all-field overlap 0 | Gemini’s report mixed pairwise and three-way intersections and did not present the requested 2022/2024 value. GPT and Claude excluded exactly the fiscal-year field and three annual-state fields. |
| Severity of the missing package | HIGH artifact/reproduction defect | HIGH missing-material defect | LOW artifact defect, with INCOMPLETE treated separately as an execution status | The models weighted audit-package availability differently. All agree it blocks PASS regardless of severity label. |
| Convergence-status wording | HIGH contradiction between “one of two” and “ZERO” | No separate finding | MEDIUM phrasing tension | GPT reads the adjacent counts as directly incompatible; Claude treats them as two differently qualified counters that are still too easy to misread. |
| “Under 0.1 percent” wording | LOW because it is true for face dollars but not counts | Accepted the phrase without qualification | MEDIUM because the sentence reports both count and sum | GPT and Claude calculated the count gap as about 0.510% and the face-value gap as about 0.0891%; Gemini applied the bound only to the dollar reconciliation without flagging the sentence-level ambiguity. |

## Unique Discoveries

| Model | Unique Finding | Why It Matters |
|---|---|---|
| Claude Opus 4.8 | The portal declares 23 columns while live row payloads expose 22 keys because a null-only field is omitted; the 18-field fingerprint still follows from 22 row-present keys minus four excluded fields. | The missing manifest prevents verification of whether its inventory is based on declared metadata or the row-union schema. |
| GPT 5.5 | Classified the package absence and the dual convergence counters as separate HIGH findings. | This is the strictest reading of the brief and independently prevents a zero-HIGH qualifying outcome. |
| Gemini 3.1 Pro | Surfaced an alternate Gini and overlap calculation. | The divergence is useful as a reproducibility warning, but the reported method does not match the artifact’s specified basis and should not displace the correctly reproduced values. |

## Comprehensive Analysis

The council ran as three clean, independent subagent instances with no prior findings, memory, personalization, or access to one another’s reports. GPT 5.5 and Gemini 3.1 Pro are the only qualifying members. Claude Opus 4.8 belongs to the Anthropic/Claude producing lineage and is therefore quarantined as advisory-only under Standing Rule 7.

The high-confidence result is that F-AA-R5 does not pass. The delivered archive contained the two narrative artifacts but not `reproduce_paper2.py`, `MANIFEST.json`, or the frozen `gpsc-qqsz_FY2022-2024.json` snapshot. All three members attempted recovery through the links present in the artifacts and found that the cited Zenodo records hosted other works, not the required package ([Zenodo 21436484](https://zenodo.org/api/records/21436484), [Zenodo 19894724](https://zenodo.org/api/records/19894724), [Zenodo 20069654](https://zenodo.org/api/records/20069654)). Consequently, none could execute the required offline hash and field-inventory check, the 45-statistic-plus-schema self-test, the supplied `--live` comparator, or the supplied comparator’s adversarial behavior. The brief expressly forbids PASS when qualifying members have not documented execution of all seven steps.

The missing package should not obscure the substantial live evidence. GPT 5.5 and Claude Opus 4.8 independently pulled 12,156 FY2022 rows, 12,114 FY2023 rows, and 13,718 FY2024 rows, totaling 37,988. Their FY2024 calculations matched $65,189,755,228.64 in face value, $8,170,228,558.54 in annual expenditure, and MWBE shares of 18.7345% by count, 3.9532% by face value, and 7.0612% by annual expenditure ([FY2024 community-view aggregate](https://data.ny.gov/resource/gpsc-qqsz.json?%24select=count(*)+as+row_count,+sum(contract_amount)+as+face_total,+sum(amount_expended_for_fiscal_year)+as+exp_total&fiscal_year_end_date=2024-12-31T00%3A00%3A00.000)). They also reproduced the 30.4151% top-10 face concentration, 0.93117 positive-face-vendor Gini, 91.6876% pre-2024 face share, 1,348 missing amounts, 48 explicit zero amounts, pairwise 18-field overlaps of 2,115 / 604 / 1,002, and zero exact all-field overlap. Those results support the substantive estimand, stock/flow, descriptive prime-vendor, structural-concentration, and vintage-overlap claims.

Gemini 3.1 Pro’s independent execution supports the main totals but is weaker on the two most method-sensitive statistics. Its 0.937 Gini and mixed 2,115 / 1,003 / 265 overlap output do not implement the specified positive-face-vendor and pairwise 18-field procedures transparently. The discrepancy should therefore be recorded as a member-level methodological divergence, not treated as live-data drift. GPT 5.5’s complete code and Claude Opus 4.8’s independent matching result provide the stronger interpretation.

The live provenance reconciliation also exposes a wording defect. The community view returns 13,718 FY2024 rows and $65.1898B face value, while the first-party MTA view returns 13,648 rows and $65.1317B ([community aggregate](https://data.ny.gov/resource/gpsc-qqsz.json?%24select=count(*)+as+row_count,+sum(contract_amount)+as+face_total&fiscal_year_end_date=2024-12-31T00%3A00%3A00.000), [first-party aggregate](https://data.ny.gov/resource/twsw-2mqa.json?%24select=count(*)+as+row_count,+sum(contract_amount)+as+face_total&fiscal_year_end_date=2024-12-31T00%3A00%3A00.000)). The face-value divergence is about 0.0891%, but the record-count divergence is about 0.510%. The phrase “a divergence under 0.1 percent” should be narrowed explicitly to face-value dollars.

The artifacts also present “one of two on the letter” beside “ZERO toward convergence.” Even if these are intended as different counters, the juxtaposition is unstable and can launder the weaker consistency-only R4 result into a convergence claim. After this findings-bearing, execution-incomplete R5, the practical consecutive qualifying PASS count is zero because R5 did not pass and the streak is broken.

The recommended disposition is a findings-bearing NON-PASS / INCOMPLETE for F-AA-R5. Deposit the exact frozen snapshot, manifest, and script under an authoritative immutable URL or DOI; include that package in the next audit packet; clarify the dollar-only 0.1% statement; and collapse the convergence language to one operational counter. Then rerun a fresh non-Claude qualifying council with mandatory execution of all seven steps.

## Member Identities, Lineages, and Verdicts

| Council member | Lineage | Qualifying? | Independent verdict | Critical | High | Execution status |
|---|---|---:|---|---:|---:|---|
| GPT 5.5 | OpenAI | Yes | Findings-bearing NON-PASS | 0 | 2 | Steps 1–3 incomplete; Step 7 partial; Steps 4–6 executed |
| Gemini 3.1 Pro | Google | Yes | INCOMPLETE / NON-PASS | 0 | 1 | Steps 1–3 incomplete; independent Steps 4–7 attempted |
| Claude Opus 4.8 | Anthropic/Claude producing lineage | No, advisory-only | INCOMPLETE, findings-bearing | 0 | 0 | Steps 1–3 incomplete; supplied-comparator leg of Step 7 incomplete; Steps 4–6 executed |

## Synthesized Qualifying-Member Verdict

The qualifying set is GPT 5.5 and Gemini 3.1 Pro. Both independently declined PASS, both documented missing mandatory execution substrate, and both reported at least one HIGH finding. The synthesized qualifying-member verdict is **FINDINGS-BEARING NON-PASS / INCOMPLETE**.

This round is not the second consecutive passing round and is not the first independent executed reproduction of the frozen v0.4 package. Convergence under Audit Framework v3.0 Standing Rule 7 is **not met**. Because F-AA-R5 is non-passing, the consecutive qualifying PASS streak is now **zero**.

## Synthesized Findings

### F-AA-R5-C-01

1. **Identifier:** F-AA-R5-C-01
2. **Severity:** HIGH
3. **Locus:** Reproduction package and the data-availability/reproduction claims.
4. **Substance:** The surface states that a frozen snapshot, manifest, and reproducer accompany the published artifact; the supplied substrate contains none of them and exposes no recoverable authoritative package link.
5. **Disposition:** OPEN. Deposit and supply the exact package before resubmission.
6. **Cross-reference:** Mandatory Steps 1–3 and supplied-comparator portion of Step 7; unanimous council finding.

### F-AA-R5-C-02

1. **Identifier:** F-AA-R5-C-02
2. **Severity:** HIGH
3. **Locus:** Companion Current State and reader convergence language.
4. **Substance:** The surface simultaneously records “one of two on the letter” and “ZERO toward convergence”; the operational substrate after this non-passing R5 supports only zero consecutive qualifying passes.
5. **Disposition:** OPEN. Replace dual counters with one governing convergence counter and explanatory history.
6. **Cross-reference:** GPT 5.5 F-AA-R5-02; Claude Opus 4.8 F-AA-R5-02.

### F-AA-R5-C-03

1. **Identifier:** F-AA-R5-C-03
2. **Severity:** MEDIUM
3. **Locus:** Reader provenance comparison of `gpsc-qqsz` and `twsw-2mqa`.
4. **Substance:** The surface attaches “under 0.1 percent” to a sentence reporting count and face sum; the live substrate supports about 0.0891% for face value but about 0.510% for row count.
5. **Disposition:** OPEN. State “face-value divergence under 0.1 percent; record counts differ by about 0.5 percent.”
6. **Cross-reference:** GPT 5.5 F-AA-R5-03; Claude Opus 4.8 F-AA-R5-01; live aggregate queries.

### F-AA-R5-C-04

1. **Identifier:** F-AA-R5-C-04
2. **Severity:** INFO
3. **Locus:** Numerical claims independently recomputable from live data.
4. **Substance:** Surface and substrate coincide for the principal totals, MWBE shares, stock/flow distinction, concentration under the stated basis, pre-2024 share, missing/zero split, and 18-field pairwise fingerprint.
5. **Disposition:** CLOSED / NOTED. Preserve the current substantive framing.
6. **Cross-reference:** GPT 5.5 and Claude Opus 4.8 independent recomputations; Gemini 3.1 Pro confirmation of principal totals.

---

# Bismillah ir-Rahman ir-Rahim
