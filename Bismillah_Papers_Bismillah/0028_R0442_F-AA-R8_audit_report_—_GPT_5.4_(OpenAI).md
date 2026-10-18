# Bismillah ir-Rahman ir-Rahim

# R0442 -- F-AA-R8 audit report — GPT 5.4 (OpenAI)

**Chronological Index:** 28 of 995  
**Date:** 2024  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-AA-R8_gpt54.md  
**Source Format:** md  
**SHA-256:** `06d14986853e3a8fe7e5c9b114018bdf03f060bd5f01adb394fe6db6659ba0e5`  

---

## R0442 · F-AA-R8 audit report — GPT 5.4 (OpenAI)

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-AA-R8_gpt54.md
- source_format: md
- text_sha256: 06d14986853e3a8fe7e5c9b114018bdf03f060bd5f01adb394fe6db6659ba0e5

# F-AA-R8 audit report — GPT 5.4 (OpenAI)

## Attestation

I attest that I began this task with no prior-round state, no chat memory, and no access to other members’ work. I am GPT 5.4 (OpenAI), a qualifying non-producer council member; Claude/Anthropic is the producing lineage and is advisory-only here. I am also a rotation member relative to round 6.

## Scope and artifact used

I used only `/home/user/workspace/r8-gpt_5_4/` as instructed. The package file was present as `/home/user/workspace/r8-gpt_5_4/pkg.zip`, alongside the extracted reproduction directory, the reader note, and the audit companion.

## Per-leg execution status

1. Supplied offline reproduction: COMPLETE
2. Supplied self-test: COMPLETE
3. Supplied live comparison: COMPLETE
4. Independent recompute with my own code: COMPLETE
5. Provenance check against `gpsc-qqsz` and `twsw-2mqa`: COMPLETE
6. Capital join check across `wcsa-vkhf`, `kizb-nxtu`, and `ehz8-ag3n`: COMPLETE
7. Adversarial snapshot mutation with manifest re-hash and comparator drift check: COMPLETE

## Step 1 — supplied offline reproduction

Command run:

```bash
cd /home/user/workspace/r8-gpt_5_4/extracted && python3 reproduce_paper2.py
```

Raw output:

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

Result: matched the expected snapshot-integrity and headline statistics.

## Step 2 — supplied self-test

Command run:

```bash
cd /home/user/workspace/r8-gpt_5_4/extracted && python3 reproduce_paper2.py --selftest
```

Raw output:

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
```

Result: self-test detected all 45 perturbations plus schema perturbation.

## Step 3 — supplied live comparison

Command run:

```bash
cd /home/user/workspace/r8-gpt_5_4/extracted && python3 reproduce_paper2.py --live
```

Raw output:

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

EXIT_CODE=0
```

Result: live comparator exited 0 and reported no drift.

## Steps 4–7 — independent checks, provenance, capital join, and adversarial mutation

I wrote and ran my own independent verifier at `/home/user/workspace/r8-gpt_5_4/independent_checks.py`. It did not import or call the supplied script’s functions. It recomputed the requested metrics from the frozen JSON; queried live Socrata aggregates from [gpsc-qqsz](https://data.ny.gov/resource/gpsc-qqsz.json) and [twsw-2mqa](https://data.ny.gov/resource/twsw-2mqa.json); checked a batch of project-number joins against [wcsa-vkhf](https://data.ny.gov/resource/wcsa-vkhf.json), [kizb-nxtu](https://data.ny.gov/resource/kizb-nxtu.json), and [ehz8-ag3n](https://data.ny.gov/resource/ehz8-ag3n.json); and performed the required adversarial manifest-rehash mutation test.

Command run:

```bash
python3 /home/user/workspace/r8-gpt_5_4/independent_checks.py
```

Raw output:

```text
[independent] manifest_sha_match True
[independent] field_inventory_match True
[independent] total_rows 37988
[independent] rows 2022-12-31T00:00:00.000 12156
[independent] rows 2023-12-31T00:00:00.000 12114
[independent] rows 2024-12-31T00:00:00.000 13718
[independent] fy2024_face_total 65189755228.64
[independent] fy2024_ae_total 8170228558.54
[independent] fy2024_mwbe_count_pct 18.7345
[independent] fy2024_mwbe_face_pct 3.9532
[independent] fy2024_mwbe_ae_pct 7.0612
[independent] fy2024_missing_contract_amount 1348
[independent] fy2024_zero_contract_amount 48
[independent] pre2024_face_share_pct 91.6876
[independent] face_vendor_count 2656
[independent] face_top5_pct 22.1434
[independent] face_top10_pct 30.4151
[independent] face_top20_pct 41.7769
[independent] face_gini 0.93117
[independent] ae_top10_pct 26.2419
[independent] ae_gini 0.90435
[independent] overlap_fields18_count 18
[independent] overlap18_22_23 2115
[independent] overlap18_22_24 604
[independent] overlap18_23_24 1002
[independent] overlap22_22_23 0
[independent] overlap22_22_24 0
[independent] overlap22_23_24 0
[provenance] gpsc-qqsz_count 13718
[provenance] gpsc-qqsz_sum_contract_amount 65189755228.64
[provenance] twsw-2mqa_count 13648
[provenance] twsw-2mqa_sum_contract_amount 65131682801.41
[provenance] face_divergence_pct_vs_gpsc 0.089082
[provenance] count_divergence_pct_vs_gpsc 0.510278
[capital] wcsa_sample_project_numbers ['D501CB08', 'D501TN85', 'D502BW89', 'D502HH80', 'D502TB64']
[capital] wcsa_noncomputed_field_count 13
[capital] wcsa_borough_like_fields []
[capital] project D501CB08 kizb_matches 5 ehz8_matches 5
[capital] project D501CB08 kizb_keys ['agency_name', 'budget_submission_date', 'capital_plan', 'plan_revision', 'plan_year_year_2_allocation', 'project_descrition', 'project_number', 'total_allocation']
[capital] project D501CB08 ehz8_keys ['ada_flag', 'agency_code', 'agency_name', 'capital_plan', 'category', 'category_description', 'current_budget', 'current_completion_mm', 'current_completion_yyyy', 'current_start_mm']
[capital] project D501TN85 kizb_matches 5 ehz8_matches 5
[capital] project D501TN85 kizb_keys ['agency_name', 'budget_submission_date', 'capital_plan', 'plan_revision', 'plan_year_year_1_allocation', 'plan_year_year_2_allocation', 'project_descrition', 'project_number', 'total_allocation']
[capital] project D501TN85 ehz8_keys ['ada_flag', 'agency_code', 'agency_name', 'capital_plan', 'category', 'category_description', 'current_budget', 'current_completion_mm', 'current_completion_yyyy', 'current_start_mm']
[capital] project D502BW89 kizb_matches 5 ehz8_matches 5
[capital] project D502BW89 kizb_keys ['agency_name', 'budget_submission_date', 'capital_plan', 'plan_revision', 'plan_year_year_4_allocation', 'project_descrition', 'project_number', 'total_allocation']
[capital] project D502BW89 ehz8_keys ['ada_flag', 'agency_code', 'agency_name', 'capital_plan', 'category', 'category_description', 'current_budget', 'current_completion_mm', 'current_completion_yyyy', 'current_start_mm']
[capital] project D502HH80 kizb_matches 5 ehz8_matches 5
[capital] project D502HH80 kizb_keys ['agency_name', 'budget_submission_date', 'capital_plan', 'change_narrative', 'plan_revision', 'plan_year_year_1_allocation', 'plan_year_year_2_allocation', 'project_descrition', 'project_number', 'total_allocation']
[capital] project D502HH80 ehz8_keys ['ada_flag', 'agency_code', 'agency_name', 'capital_plan', 'category', 'category_description', 'current_budget', 'current_completion_mm', 'current_completion_yyyy', 'current_start_mm']
[capital] project D502TB64 kizb_matches 5 ehz8_matches 5
[capital] project D502TB64 kizb_keys ['agency_name', 'budget_submission_date', 'capital_plan', 'plan_revision', 'plan_year_year_1_allocation', 'project_descrition', 'project_number', 'total_allocation']
[capital] project D502TB64 ehz8_keys ['ada_flag', 'agency_code', 'agency_name', 'capital_plan', 'category', 'category_description', 'current_budget', 'current_completion_mm', 'current_completion_yyyy', 'current_start_mm']
[adversarial] mutated_row_index 1
[adversarial] mutated_vendor 11 ENVIROGROUP LLC
[adversarial] mutated_fy 2022-12-31T00:00:00.000
[adversarial] original_contract_amount 1189080.00
[adversarial] new_contract_amount 101189080.99
[adversarial] live_compare_exit_code 2
[adversarial] begin_output
[integrity] hash OK, field inventory OK (22 fields), 37988 rows

[4.2] MWBE count vs dollar share (both estimands), by vintage:
  FY2022: count 16.4%  face 3.27% (x5.0)  exp 4.25% (x3.9)  [face $54.8B exp $6.8B miss 712 zero 0]
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
   2022.face_total: frozen=54798007775.6800 vs live=54698007774.6900 (tol 5.4798e+06)
[adversarial] end_output
```

Independent recompute matched the expected values, including 37,988 total rows; FY2024 totals of $65,189,755,228.64 face and $8,170,228,558.54 annual expenditure; MWBE shares of 18.7345 percent count, 3.9532 percent face, and 7.0612 percent annual expenditure; top-10 face concentration of 30.4151 percent; Ginis of 0.93117 face and 0.90435 annual expenditure; 18-field overlaps of 2,115, 604, and 1,002; exact all-field pairwise overlaps of 0; pre-2024 face share of 91.6876 percent; and missing/zero face amounts of 1,348 and 48.

The provenance aggregates from [gpsc-qqsz](https://data.ny.gov/resource/gpsc-qqsz.json?$select=count(*),sum(contract_amount)&$where=fiscal_year_end_date='2024-12-31T00:00:00.000') and [twsw-2mqa](https://data.ny.gov/resource/twsw-2mqa.json?$select=count(*),sum(contract_amount)&$where=fiscal_year_end_date='2024-12-31T00:00:00.000') were separated correctly as face divergence and count divergence, at about 0.089082 percent and 0.510278 percent respectively.

The capital check confirmed that sampled `wcsa-vkhf` project numbers resolved against both [kizb-nxtu](https://data.ny.gov/resource/kizb-nxtu.json) using `project_number` and [ehz8-ag3n](https://data.ny.gov/resource/ehz8-ag3n.json) using `proj_num`, and that the sampled non-computed `wcsa-vkhf` field list exposed no borough-like key.

The adversarial leg was complete in the required sense: after mutating one non-MWBE `contract_amount`, re-hashing the manifest so integrity still passed, and re-running the comparator, the result was `DRIFT` with exit code 2 rather than a hash abort.

## Reader-note and companion regression review

I reviewed the reader note and companion directly.

### Current-status propagation regression F-AA-R7-01

The specified loci were mutually consistent on all three required dimensions:

- Reader-note header: `Working draft v0.6`, `seven audit rounds`, and `F-AA-R7 ... reset the consecutive qualifying-PASS count to zero`.
- Reader-note Section 6: `The single operational metric is the consecutive qualifying-PASS count, which is ZERO` and the seven-round sequence ending with `F-AA-R7 ... reset it to zero`.
- Reader-note Section 7: `This draft is v0.6`, `seven independent cross-instance audit rounds`, `F-AA-R6 ... first genuine qualifying pass`, `F-AA-R7 ... findings-bearing NON-PASS`, and `The single operational metric is the consecutive qualifying-PASS count, which is ZERO`.
- Companion header line 5: `Mirrors note state v0.6 (seven audit rounds; F-AA-R6 was the first qualifying pass, but the closing round F-AA-R7 was a findings-bearing NON-PASS that reset the count to zero)`.
- Companion `Current State` block: `as of v0.6` and `Consecutive qualifying-PASS count ... ZERO ... F-AA-R6 ... one; F-AA-R7 ... resets it to zero`, with the seven-round history spelled out.

I found no surviving version/counter/round-count inconsistency in those current-status loci.

### Scope and framing regression checks

I found the requested descriptive framing intact.

- The MWBE discussion stayed descriptive and explicitly refused goal-attainment, operative-substrate, short-measure, and compliance-pass language in the live prose of Sections 4.2, 4.4, 6, and 7.
- Concentration was framed as a structural explanation only, with an explicit refusal to infer steering, discrimination, favoritism, or fraud.
- The fingerprint prose in Section 4.0 matched the 18-field method: exclude exactly `fiscal_year_end_date`, `amount_expended_for_fiscal_year`, `amount_expended_to_date`, and `current_or_outstanding_balance`, and do not substitute a three-way intersection.
- Provenance language separated face divergence from count divergence.
- The artifact used a single operational convergence counter, not dual-counter language.
- Section 8 directed auditors to the attached reproduction package and explained why the package must travel with the audit packet.

### Prior-finding disposition regression check

I found no evident regression of the cited prior findings set. The artifact’s live content reflects the previously required corrections on estimand naming, stock-versus-flow integrity, MWBE descriptive limitation, non-compliance framing for process composition, provenance wording, package handling, fingerprint method, and single-counter status language.

## Findings (namespace F-AA-R8)

No CRITICAL, HIGH, MEDIUM, LOW, or INFO findings identified.

## Verdict

QUALIFYING PASS.

Basis:

- Executed reproduction is documented above with pasted raw outputs for offline, self-test, live, independent recompute, provenance, capital join, and adversarial drift detection.
- I identified zero CRITICAL findings and zero HIGH findings.
- The required package was present in the workspace.
- The adversarial leg satisfied the round-7 regression requirement by producing comparator nonzero drift after manifest re-hash.

## Saved artifacts

- Full report: `/home/user/workspace/model-council-gpt_5_4.md`
- Offline reproduction transcript: `/home/user/workspace/r8-gpt_5_4/offline_reproduction_output.txt`
- Self-test transcript: `/home/user/workspace/r8-gpt_5_4/selftest_output.txt`
- Live comparison transcript: `/home/user/workspace/r8-gpt_5_4/live_output.txt`
- Independent verifier: `/home/user/workspace/r8-gpt_5_4/independent_checks.py`
- Independent-check transcript: `/home/user/workspace/r8-gpt_5_4/independent_checks_output.txt`

---

# Bismillah ir-Rahman ir-Rahim
