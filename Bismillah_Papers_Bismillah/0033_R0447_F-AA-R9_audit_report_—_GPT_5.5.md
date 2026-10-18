# Bismillah ir-Rahman ir-Rahim

# R0447 -- F-AA-R9 audit report — GPT 5.5

**Chronological Index:** 33 of 995  
**Date:** 2024  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-AA-R9_gpt55.md  
**Source Format:** md  
**SHA-256:** `a3e0e6cc0549f062a351db9306ed5645c3573f92831ab991abf6a65773711776`  

---

## R0447 · F-AA-R9 audit report — GPT 5.5

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-AA-R9_gpt55.md
- source_format: md
- text_sha256: a3e0e6cc0549f062a351db9306ed5645c3573f92831ab991abf6a65773711776

# F-AA-R9 audit report — GPT 5.5

## Identity, lineage, qualification, verdict

- Member identity: GPT 5.5.
- Lineage: OpenAI lineage.
- Producer lineage exclusion: Claude/Anthropic is the producing lineage and is excluded from the verdict; I am non-Claude.
- No-prior-state attestation: I am a fresh instance with no memory of prior rounds and no access to other members' work.
- Reproduction executed: YES — all seven mandatory protocol steps were executed against `/home/user/workspace/audit-r9/member-gpt55/` and live Socrata resources.
- Verdict: **PASS**.
- CRITICAL findings: **0**.
- HIGH findings: **0**.

## Scope/regression conclusions

- The supplied package was present at `/home/user/workspace/audit-r9/member-gpt55/`, contained `reproduce_paper2.py`, `snapshot/MANIFEST.json`, and `snapshot/gpsc-qqsz_FY2022-2024.json`, and the script validated hash/field inventory.
- The reproduction outputs and my independent code confirmed the expected principal values: 37,988 total rows; FY2024 rows 13,718; FY2024 face total $65,189,755,228.64; FY2024 annual expenditure total $8,170,228,558.54; MWBE shares 18.7345% count, 3.9532% face, and 7.0612% annual expenditure; top-10 face concentration 30.4151%; Gini 0.93117 face and 0.90435 annual expenditure; pairwise stable 18-field overlaps 2,115 / 604 / 1,002; exact all-field pairwise overlaps 0.
- Status-propagation regression checks were clean: reader header, reader Sections 6 and 7, companion header line 5, and companion Current State are consistent on v0.7, eight rounds, and consecutive qualifying-PASS count ONE, with F-AA-R6 and F-AA-R8 recorded as qualifying passes and F-AA-R7 recorded as the NON-PASS reset.
- The companion Current State lead-in explicitly scopes “Independent audit history” to rounds 1–3 and points to the counter bullet for the full eight-round sequence.
- Prior-finding regression check: current text preserves stock/flow integrity; descriptive MWBE prime-vendor framing with limitations; no current goal-attainment, operative-substrate, short-measure, or compliance-pass claim; concentration is used as non-culpable structural explanation; fingerprint prose matches the 18-field method; provenance separates face/count divergence; Section 8 package direction is present. I found no new CRITICAL or HIGH defect.

## Step 1 — `python3 reproduce_paper2.py`

Status: EXECUTED.

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
EXIT:0
```

## Step 2 — `python3 reproduce_paper2.py --selftest`

Status: EXECUTED.

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

[selftest] perturbing each statistic to confirm the comparator detects it...
[selftest] PASS: comparator detected all 45 deliberate perturbations
EXIT:0
```

## Step 3 — `python3 reproduce_paper2.py --live`

Status: EXECUTED.

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

[live] pulling all three years and comparing EVERY statistic + schema + row count...
[live] no drift on any published statistic, schema, or row count
EXIT:0
```

## Step 4 — Independent recompute with my own code

Status: EXECUTED.

Code saved at `/home/user/workspace/audit-r9/independent_recompute_gpt55.py`. The code does not import or call `reproduce_paper2.py`.

```text
independent script: no import/use of reproduce_paper2.py
snapshot sha256 9aefc01789854e79fa07d19484bc14be7a899ec7856b8c79fd4994629fdf0f09
manifest sha256 9aefc01789854e79fa07d19484bc14be7a899ec7856b8c79fd4994629fdf0f09
total_rows 37988
FY2022_rows 12156
FY2023_rows 12114
FY2024_rows 13718
FY2024_face_total 65189755228.64
FY2024_annual_expenditure_total 8170228558.54
FY2024_missing_contract_amount 1348
FY2024_explicit_zero_contract_amount 48
FY2024_MWBE_count_pct 18.7345
FY2024_MWBE_face_pct 3.9532
FY2024_MWBE_annual_expenditure_pct 7.0612
FY2024_face_vendor_positive_count 2656
FY2024_face_top10_concentration_pct 30.4151
FY2024_face_gini 0.93117
FY2024_ae_vendor_positive_count 2518
FY2024_ae_top10_concentration_pct 26.2419
FY2024_ae_gini 0.90435
FY2024_pre2024_award_face_share_pct 91.6876
fingerprint_field_count 18
fingerprint_fields authority_name|award_date|award_process|begin_date|contract_amount|end_date|number_of_bids_or_proposals_received|number_of_mwbe_proposals|procurement_description|solicited_mwbe|type_of_procurement|vendor_city|vendor_country|vendor_is_a_mwbe|vendor_name|vendor_postal_code|vendor_province_region|vendor_state
18field_pairwise_overlap_FY2022_FY2023 2115
18field_pairwise_overlap_FY2022_FY2024 604
18field_pairwise_overlap_FY2023_FY2024 1002
exact_allfield_pairwise_overlap_FY2022_FY2023 0
exact_allfield_pairwise_overlap_FY2022_FY2024 0
exact_allfield_pairwise_overlap_FY2023_FY2024 0
identity_only_subset_used NO
three_way_intersection_reported_as_published_statistic NO
```

## Step 5 — Provenance live Socrata query: `gpsc-qqsz` vs `twsw-2mqa`

Status: EXECUTED.

```text
gpsc-qqsz_url https://data.ny.gov/resource/gpsc-qqsz.json?%24select=count%28%2A%29+as+count%2C+sum%28contract_amount%29+as+face_sum&%24where=fiscal_year_end_date%3D%272024-12-31T00%3A00%3A00.000%27
gpsc-qqsz_count 13718
gpsc-qqsz_face_sum 65189755228.64
twsw-2mqa_url https://data.ny.gov/resource/twsw-2mqa.json?%24select=count%28%2A%29+as+count%2C+sum%28contract_amount%29+as+face_sum&%24where=fiscal_year_end_date%3D%272024-12-31T00%3A00%3A00.000%27
twsw-2mqa_count 13648
twsw-2mqa_face_sum 65131682801.41
count_difference_gpsc_minus_twsw 70
face_difference_gpsc_minus_twsw 58072427.23
count_divergence_pct_vs_gpsc 0.5103
face_divergence_pct_vs_gpsc 0.0891
```

## Step 6 — Capital join: `wcsa-vkhf` project numbers against `kizb-nxtu` and `ehz8-ag3n`

Status: EXECUTED.

```text
SCHEMA BOROUGH/PROJECT FIELD CHECK
wcsa-vkhf project-like= ['project_number', 'project_number_sequence', 'project_description'] borough-like= []
kizb-nxtu project-like= ['project_number', 'project_descrition'] borough-like= []
ehz8-ag3n project-like= ['proj_num', 'project', 'mega_project', 'proj_description'] borough-like= []
sample_project_numbers ['D501CB08', 'D501TN85', 'D502BW89', 'D502HH80', 'D502TB64', 'D502TN50', 'D502VN80', 'D601BB28', 'D601BW07', 'D601BW14', 'D601BW84', 'D601BW97', 'D601CB09', 'D601HH07', 'D601HH81', 'D601HH89', 'D601MP06', 'D601MP16', 'D601MPXB', 'D601QM18']
PROJECT JOIN COUNTS
D501CB08 kizb-nxtu.project_number_count 6 ehz8-ag3n.proj_num_count 22
D501TN85 kizb-nxtu.project_number_count 6 ehz8-ag3n.proj_num_count 22
D502BW89 kizb-nxtu.project_number_count 6 ehz8-ag3n.proj_num_count 22
D502HH80 kizb-nxtu.project_number_count 6 ehz8-ag3n.proj_num_count 22
D502TB64 kizb-nxtu.project_number_count 6 ehz8-ag3n.proj_num_count 22
D502TN50 kizb-nxtu.project_number_count 6 ehz8-ag3n.proj_num_count 22
D502VN80 kizb-nxtu.project_number_count 6 ehz8-ag3n.proj_num_count 22
D601BB28 kizb-nxtu.project_number_count 1 ehz8-ag3n.proj_num_count 24
D601BW07 kizb-nxtu.project_number_count 1 ehz8-ag3n.proj_num_count 24
D601BW14 kizb-nxtu.project_number_count 1 ehz8-ag3n.proj_num_count 24
D601BW84 kizb-nxtu.project_number_count 1 ehz8-ag3n.proj_num_count 24
D601BW97 kizb-nxtu.project_number_count 1 ehz8-ag3n.proj_num_count 24
D601CB09 kizb-nxtu.project_number_count 1 ehz8-ag3n.proj_num_count 24
D601HH07 kizb-nxtu.project_number_count 1 ehz8-ag3n.proj_num_count 24
D601HH81 kizb-nxtu.project_number_count 1 ehz8-ag3n.proj_num_count 24
D601HH89 kizb-nxtu.project_number_count 1 ehz8-ag3n.proj_num_count 24
D601MP06 kizb-nxtu.project_number_count 1 ehz8-ag3n.proj_num_count 24
D601MP16 kizb-nxtu.project_number_count 1 ehz8-ag3n.proj_num_count 24
D601MPXB kizb-nxtu.project_number_count 1 ehz8-ag3n.proj_num_count 24
D601QM18 kizb-nxtu.project_number_count 1 ehz8-ag3n.proj_num_count 24
coverage 20 kizb_hits 20 ehz8_hits 20
example_join_project D501CB08
kizb_sample_keys ['agency_name', 'budget_submission_date', 'capital_plan', 'plan_revision', 'plan_year_year_2_allocation', 'project_descrition', 'project_number', 'total_allocation']
ehz8_sample_keys ['ada_flag', 'agency_code', 'agency_name', 'capital_plan', 'category', 'category_description', 'current_budget', 'current_completion_mm', 'current_completion_yyyy', 'current_start_mm', 'current_start_yyyy', 'element', 'element_description', 'lastest_approved_budget_vs_current_budget', 'latest_approved_budget', 'loaddate', 'location_indicator', 'milestone_construction_completion_mm', 'milestone_construction_completion_yyyy', 'milestone_construction_start_mm', 'milestone_construction_start_yyyy', 'milestone_design_completion_mm', 'milestone_design_completion_yyyy', 'milestone_design_start_mm', 'milestone_design_start_yyyy', 'needs_code', 'original_budget', 'original_budget_vs_current_budget', 'original_completion_mm', 'original_completion_yyyy', 'original_start_mm', 'original_start_yyyy', 'percentage_complete', 'phase', 'plan_rev_display_keys', 'plan_rev_keys', 'proj_description', 'proj_num', 'project', 'resiliency_flag', 'scope_change', 'scope_objective']
```

## Step 7 — Adversarial mutation test

Status: EXECUTED.

Mutation setup: copied the isolated package to `/home/user/workspace/audit-r9/member-gpt55-mutation-test`, mutated one FY2024 non-MWBE positive `contract_amount`, rewrote the snapshot, and updated the manifest hash so integrity would pass before comparator execution.

```text
mutated_index 24278
vendor_is_a_mwbe N
vendor_name 22ND CENTURY TECHNOLOGIES, INC
old_contract_amount 4500000.0
new_contract_amount 1004500000.00
updated_manifest_sha256 3062c5a946cb3888cf4478286003bbe581b9f1d4b2e6d859915ddf60494164fd
[integrity] hash OK, field inventory OK (22 fields), 37988 rows

[4.2] MWBE count vs dollar share (both estimands), by vintage:
  FY2022: count 16.4%  face 3.27% (x5.0)  exp 4.25% (x3.9)  [face $54.7B exp $6.8B miss 712 zero 0]
  FY2023: count 18.6%  face 3.51% (x5.3)  exp 6.27% (x3.0)  [face $63.6B exp $6.7B miss 1049 zero 111]
  FY2024: count 18.7%  face 3.89% (x4.8)  exp 7.06% (x2.7)  [face $66.2B exp $8.2B miss 1348 zero 48]
[4.1] FY2024 process (face | exp):
  Authority Contract - Competitive Bid     face 92.34%  exp 89.65%
  Authority Contract - Non-Competitive B   face  7.66%  exp  4.73%
  Purchased Under State Contract           face  0.00%  exp  3.24%
  Non Contract Procurement/Purchase Orde   face  0.00%  exp  2.38%
[4.3] face conc  top5 21.8% top10 30.2% top20 41.8% gini 0.932 (vendors 2656)
[4.3] exp  conc  top5 16.9% top10 26.2% top20 37.6% gini 0.904
[4.0] pre-2024-award face share 91.8% (stock, not FY2024 flow)

[live] pulling all three years and comparing EVERY statistic + schema + row count...
[live] DRIFT on 7 field(s):
   2024.face_total: frozen=66189755228.6400 vs live=65189755228.6400 (tol 6.61898e+06)
   2024.mwbe_face_pct: frozen=3.8934 vs live=3.9532 (tol 0.05)
   conc_face.top10: frozen=30.1724 vs live=30.4151 (tol 0.05)
   conc_face.top5: frozen=21.8089 vs live=22.1434 (tol 0.05)
   pre2024_face_share: frozen=91.8132 vs live=91.6876 (tol 0.05)
   proc_face_pct.Authority Contract - Competitive Bid: frozen=92.3373 vs live=92.2197 (tol 0.05)
   proc_face_pct.Authority Contract - Non-Competitive Bid: frozen=7.6627 vs live=7.7803 (tol 0.05)
```

Repeat run capturing comparator exit code:

```text
[integrity] hash OK, field inventory OK (22 fields), 37988 rows

[4.2] MWBE count vs dollar share (both estimands), by vintage:
  FY2022: count 16.4%  face 3.27% (x5.0)  exp 4.25% (x3.9)  [face $54.7B exp $6.8B miss 712 zero 0]
  FY2023: count 18.6%  face 3.51% (x5.3)  exp 6.27% (x3.0)  [face $63.6B exp $6.7B miss 1049 zero 111]
  FY2024: count 18.7%  face 3.89% (x4.8)  exp 7.06% (x2.7)  [face $66.2B exp $8.2B miss 1348 zero 48]
[4.1] FY2024 process (face | exp):
  Authority Contract - Competitive Bid     face 92.34%  exp 89.65%
  Authority Contract - Non-Competitive B   face  7.66%  exp  4.73%
  Purchased Under State Contract           face  0.00%  exp  3.24%
  Non Contract Procurement/Purchase Orde   face  0.00%  exp  2.38%
[4.3] face conc  top5 21.8% top10 30.2% top20 41.8% gini 0.932 (vendors 2656)
[4.3] exp  conc  top5 16.9% top10 26.2% top20 37.6% gini 0.904
[4.0] pre-2024-award face share 91.8% (stock, not FY2024 flow)

[live] pulling all three years and comparing EVERY statistic + schema + row count...
[live] DRIFT on 7 field(s):
   2024.face_total: frozen=66189755228.6400 vs live=65189755228.6400 (tol 6.61898e+06)
   2024.mwbe_face_pct: frozen=3.8934 vs live=3.9532 (tol 0.05)
   conc_face.top10: frozen=30.1724 vs live=30.4151 (tol 0.05)
   conc_face.top5: frozen=21.8089 vs live=22.1434 (tol 0.05)
   pre2024_face_share: frozen=91.8132 vs live=91.6876 (tol 0.05)
   proc_face_pct.Authority Contract - Competitive Bid: frozen=92.3373 vs live=92.2197 (tol 0.05)
   proc_face_pct.Authority Contract - Non-Competitive Bid: frozen=7.6627 vs live=7.7803 (tol 0.05)
EXIT:2
```

## Findings list

No findings.

- CRITICAL count: 0.
- HIGH count: 0.
- MEDIUM count: 0.
- LOW count: 0.
- INFO count: 0.

## Final verdict

**PASS** — all seven mandatory steps were executed, the attached package reproduced successfully, live/provenance/capital checks completed, the adversarial rehashed mutation returned comparator DRIFT with exit 2, and I found zero CRITICAL and zero HIGH findings.

---

# Bismillah ir-Rahman ir-Rahim
