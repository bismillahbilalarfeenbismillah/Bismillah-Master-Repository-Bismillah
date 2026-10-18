# Bismillah ir-Rahman ir-Rahim

# R0443 -- F-AA-R8 Independent Audit Report — GPT 5.5 (OpenAI)

**Chronological Index:** 29 of 995  
**Date:** 2024  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-AA-R8_gpt55.md  
**Source Format:** md  
**SHA-256:** `6968a87b626d54bbbb127a724ebf70bc6af46b30056bfea734a30394646098da`  

---

## R0443 · F-AA-R8 Independent Audit Report — GPT 5.5 (OpenAI)

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-AA-R8_gpt55.md
- source_format: md
- text_sha256: 6968a87b626d54bbbb127a724ebf70bc6af46b30056bfea734a30394646098da

# F-AA-R8 Independent Audit Report — GPT 5.5 (OpenAI)

## Attestation and identity

I attest that I am acting as an independent, fresh, memoryless council member for this audit. I have no prior-round state, no chat memory, and no access to other members' work. My identity for this council is **GPT 5.5 (OpenAI)**, a qualifying non-producer member. Claude/Anthropic is the producing lineage and is quarantined advisory-only; I am non-Claude, so my verdict counts toward convergence if otherwise qualifying.

I used only the isolated copy under `/home/user/workspace/r8-gpt_5_5/`. I did not read any other `r8-*` directories.

## Artifact/package presence

The isolated workspace contains the reader note, companion, reproduction script, extracted snapshot/manifest, and `pkg.zip`. The attached reproduction package requirement is satisfied for this audit packet.

## Per-leg execution status

| Leg | Required action | Status |
|---|---|---|
| 1 | Offline integrity + stats: `python3 reproduce_paper2.py` | COMPLETE, exit 0 |
| 2 | Self-test: `python3 reproduce_paper2.py --selftest` | COMPLETE, exit 0, all 45 perturbations detected |
| 3 | Live comparator: `python3 reproduce_paper2.py --live` | COMPLETE, exit 0, no drift |
| 4 | Independent recompute with my own code | COMPLETE; all expected figures reproduced |
| 5 | Provenance `gpsc-qqsz` vs `twsw-2mqa` FY2024 | COMPLETE; separated face/count divergences confirmed |
| 6 | Capital join `wcsa-vkhf` to `kizb-nxtu`/`ehz8-ag3n`; no borough key | COMPLETE; batch resolved in both datasets; no borough-like field in `wcsa-vkhf` |
| 7 | Adversarial mutation with rehashed manifest and comparator drift | COMPLETE; hash passed and `--live` returned exit 2 with DRIFT |

## Step 1 raw output — offline integrity + stats

Command: `cd /home/user/workspace/r8-gpt_5_5/extracted && python3 reproduce_paper2.py`

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
EXIT_CODE=0

```

## Step 2 raw output — self-test

Command: `cd /home/user/workspace/r8-gpt_5_5/extracted && python3 reproduce_paper2.py --selftest`

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
EXIT_CODE=0

```

## Step 3 raw output — live comparator

Command: `cd /home/user/workspace/r8-gpt_5_5/extracted && python3 reproduce_paper2.py --live`

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

## Steps 4–7 raw output — independent recompute, provenance, capital join, adversarial mutation

Independent code saved at `/home/user/workspace/r8-gpt_5_5/independent_audit.py`; output saved at `/home/user/workspace/r8-gpt_5_5/independent_audit_output.txt`.

```text
=== MANIFEST HASH CHECK ===
computed_sha256 9aefc01789854e79fa07d19484bc14be7a899ec7856b8c79fd4994629fdf0f09
manifest_sha256 9aefc01789854e79fa07d19484bc14be7a899ec7856b8c79fd4994629fdf0f09
sha256_match True
manifest_field_count 22 actual_field_count 22 fields_match True

=== INDEPENDENT OFFLINE RECOMPUTE ===
total_rows 37988
fy2022_rows 12156
fy2023_rows 12114
fy2024_rows 13718
fy2024_face_total 65189755228.64
fy2024_annual_expenditure_total 8170228558.54
fy2024_mwbe_count_share_pct 18.7345
fy2024_mwbe_face_share_pct 3.9532
fy2024_mwbe_annual_exp_share_pct 7.0612
face_concentration_top5_pct 22.1434
face_concentration_top10_pct 30.4151
face_concentration_top20_pct 41.7769
face_vendor_positive_count 2656
face_vendor_gini 0.93117
annual_exp_vendor_positive_count 2518
annual_exp_vendor_gini 0.90435
pre_2024_award_share_of_fy2024_face_pct 91.6876
missing_contract_amount_fy2024 1348
explicit_zero_contract_amount_fy2024 48
fingerprint_18_fields_count 18
overlap_18field_FY2022_FY2023 2115
overlap_18field_FY2022_FY2024 604
overlap_18field_FY2023_FY2024 1002
exact_all_22field_overlap_FY2022_FY2023 0
exact_all_22field_overlap_FY2022_FY2024 0
exact_all_22field_overlap_FY2023_FY2024 0

=== PROVENANCE SOCRATA FY2024 ===
gpsc-qqsz count 13718 face_sum 65189755228.64
twsw-2mqa count 13648 face_sum 65131682801.41
count_divergence_gpsc_minus_twsw 70 pct_of_gpsc 0.5103
face_divergence_gpsc_minus_twsw 58072427.23 pct_of_gpsc 0.0891

=== CAPITAL JOIN CHECK ===
wcsa_vkhf_field_count 16
wcsa_vkhf_borough_like_fields []
wcsa_vkhf_has_project_number True
wcsa_vkhf_has_borough_key False
wcsa_vkhf_project_number_batch ['D501CB08', 'D501TN85', 'D502BW89', 'D502HH80', 'D502TB64', 'D502TN50', 'D502VN80', 'D601BB28', 'D601BW07', 'D601BW14', 'D601BW84', 'D601BW97']
kizb_nxtu_matches_by_project_number [{'project_number': 'D501CB08', 'matches': '6'}, {'project_number': 'D501TN85', 'matches': '6'}, {'project_number': 'D502BW89', 'matches': '6'}, {'project_number': 'D502HH80', 'matches': '6'}, {'project_number': 'D502TB64', 'matches': '6'}, {'project_number': 'D502TN50', 'matches': '6'}, {'project_number': 'D502VN80', 'matches': '6'}, {'project_number': 'D601BB28', 'matches': '1'}, {'project_number': 'D601BW07', 'matches': '1'}, {'project_number': 'D601BW14', 'matches': '1'}, {'project_number': 'D601BW84', 'matches': '1'}, {'project_number': 'D601BW97', 'matches': '1'}]
ehz8_ag3n_matches_by_proj_num [{'proj_num': 'D501CB08', 'matches': '22'}, {'proj_num': 'D501TN85', 'matches': '22'}, {'proj_num': 'D502BW89', 'matches': '22'}, {'proj_num': 'D502HH80', 'matches': '22'}, {'proj_num': 'D502TB64', 'matches': '22'}, {'proj_num': 'D502TN50', 'matches': '22'}, {'proj_num': 'D502VN80', 'matches': '22'}, {'proj_num': 'D601BB28', 'matches': '24'}, {'proj_num': 'D601BW07', 'matches': '24'}, {'proj_num': 'D601BW14', 'matches': '24'}, {'proj_num': 'D601BW84', 'matches': '24'}, {'proj_num': 'D601BW97', 'matches': '24'}]
kizb_nxtu_resolved_count 12 of 12
ehz8_ag3n_resolved_count 12 of 12

=== ADVERSARIAL MUTATED-SNAPSHOT CHECK ===
adversarial_dir /home/user/workspace/r8-gpt_5_5/adversarial_mutation
mutated_row_index 24278
old_contract_amount 4500000.00
new_contract_amount 127956789.01
rehash_sha256 c7c1a68692a02b84d5a5cf1ba3b9f272e19808180e11add1058296c954ee9708
adversarial_exit_code 2
--- adversarial stdout ---
[integrity] hash OK, field inventory OK (22 fields), 37988 rows

[4.2] MWBE count vs dollar share (both estimands), by vintage:
  FY2022: count 16.4%  face 3.27% (x5.0)  exp 4.25% (x3.9)  [face $54.7B exp $6.8B miss 712 zero 0]
  FY2023: count 18.6%  face 3.51% (x5.3)  exp 6.27% (x3.0)  [face $63.6B exp $6.7B miss 1049 zero 111]
  FY2024: count 18.7%  face 3.95% (x4.7)  exp 7.06% (x2.7)  [face $65.3B exp $8.2B miss 1348 zero 48]
[4.1] FY2024 process (face | exp):
  Authority Contract - Competitive Bid     face 92.23%  exp 89.65%
  Authority Contract - Non-Competitive B   face  7.77%  exp  4.73%
  Purchased Under State Contract           face  0.00%  exp  3.24%
  Non Contract Procurement/Purchase Orde   face  0.00%  exp  2.38%
[4.3] face conc  top5 22.1% top10 30.4% top20 41.7% gini 0.931 (vendors 2656)
[4.3] exp  conc  top5 16.9% top10 26.2% top20 37.6% gini 0.904
[4.0] pre-2024-award face share 91.7% (stock, not FY2024 flow)

[live] pulling all three years and comparing EVERY statistic + schema + row count...
[live] DRIFT on 3 field(s):
   2024.face_total: frozen=65313212017.6500 vs live=65189755228.6400 (tol 6.53132e+06)
   conc_face.top10: frozen=30.3576 vs live=30.4151 (tol 0.05)
   conc_face.top20: frozen=41.6979 vs live=41.7769 (tol 0.05)
--- adversarial stderr ---


```

## Reproduction conclusions

The supplied script validates the SHA-256 and 22-field manifest, computes 37,988 rows across FY2022/FY2023/FY2024, detects all 45 deliberate perturbations in self-test, and finds no live drift.

My independent recompute matches the expected values: 37,988 total rows; FY row counts 12,156 / 12,114 / 13,718; FY2024 face value $65,189,755,228.64; FY2024 annual expenditure $8,170,228,558.54; MWBE prime shares 18.7345% count / 3.9532% face / 7.0612% annual expenditure; top-5/top-10/top-20 face concentration 22.1434% / 30.4151% / 41.7769%; face Gini 0.93117; annual-expenditure Gini 0.90435; pre-2024 award share 91.6876%; missing/zero `contract_amount` 1,348 / 48; 18-field overlaps 2,115 / 604 / 1,002; exact all-22-field pairwise overlaps all 0.

The provenance check confirms `gpsc-qqsz` FY2024 at 13,718 records and $65,189,755,228.64 face value versus `twsw-2mqa` at 13,648 records and $65,131,682,801.41 face value, a 70-record / 0.5103% count divergence and $58,072,427.23 / 0.0891% face-value divergence.

The capital join check resolved 12 sampled `wcsa-vkhf.project_number` values against `kizb-nxtu.project_number` and `ehz8-ag3n.proj_num`, and `wcsa-vkhf` metadata contained no borough-like field.

The adversarial test mutated a non-MWBE FY2024 `contract_amount`, rewrote the snapshot, rehashed the manifest so the integrity check passed, and then `--live` returned exit code 2 with DRIFT on three fields; this satisfies the comparator-drift requirement rather than stopping at hash abort.

## Scope/regression review

### Estimand and stock-flow integrity

The reader note names `contract_amount` as contract face-value stock and `amount_expended_for_fiscal_year` as annual-flow expenditure; it explicitly says these are not interchangeable and that the $65.19B face total is not FY2024 spending.

### Descriptive MWBE framing

The current reader note frames MWBE results as descriptive prime-vendor count-versus-dollar statistics only. It states the data do not measure goal attainment, do not include indirect/subcontract participation, eligible-spend denominators, contract-specific goals, waivers, or exemptions, and do not support goal-compliance inferences.

### Concentration framing

The current reader note uses vendor concentration as a non-culpable structural explanation for why count and dollar shares diverge, and expressly refuses conclusions about steering, discrimination, favoritism, fraud, or absence of those things.

### Fingerprint prose

The fingerprint prose matches the 18-field method: exclude exactly `fiscal_year_end_date`, `amount_expended_for_fiscal_year`, `amount_expended_to_date`, and `current_or_outstanding_balance`; do not use a five-field identity shortcut; do not substitute a three-way intersection.

### Provenance

The reader note separates `gpsc-qqsz` from first-party `twsw-2mqa` and separately reports the face-value divergence (about 0.089%) and count divergence (about 0.5%).

### Convergence counter

The current reader note header, Section 6, Section 7, companion header line 5, and companion Current State line 31 all use a single operational counter: consecutive qualifying-PASS count ZERO. Historical dual-counter language is annotated as superseded in the companion.

### Section 8 / attached package

Reader note Section 8 directs auditors to the attached reproduction package and states that its DOI is pending, so auditors must be handed the package file directly rather than relying on related-work DOIs.

### Prior findings disposition

F-AA-1 is resolved by correction; F-AA-2 is carried as non-error for the future geographic instance. F-AA-R1-01 through R1-09 are absorbed. F-AA-R2-01 through R2-06 are absorbed. F-AA-R3-01 through R3-04 are absorbed and R3-05 is noted. F-AA-R4-01 and R4-02 are INFO. F-AA-R5-C-01 is producer-absorbed with owner deposit action still open; F-AA-R5-C-02 and C-03 are absorbed; C-04 is noted. F-AA-R6-01 is absorbed. F-AA-R7-01 is absorbed. I found one new R8 finding below.

## Findings

### F-AA-R8-01

1. **Identifier:** F-AA-R8-01.
2. **Severity:** MEDIUM.
3. **Locus:** `Bayyinah_AllocationAsymmetry_AuditCompanion-3.md`, Current State block, line 24.
4. **Substance as surface-vs-substrate divergence:** The surface text in the authoritative Current State block says, “Independent audit history: three independent cross-instance rounds attempted, all NON-PASS,” while the substrate of the same current artifact is seven audit rounds: R1–R3 NON-PASS, R4 non-reproducing consistency-only PASS not credited, R5 findings-bearing NON-PASS, R6 qualifying PASS, and R7 findings-bearing NON-PASS resetting the counter. The same Current State block later states the correct seven-round history and zero counter, so this does not create a convergence-credit contradiction, but it is a stale round-count/status sentence inside an authoritative status locus.
5. **Disposition:** NEW; requires a wording correction such as “First three rounds” or replacement with a fully current one-sentence seven-round summary. Non-blocking for PASS because the defect is local, the correct seven-round state and ZERO counter are present in the same block and all other required status loci, and it does not claim convergence or alter the operational counter.
6. **Cross-reference:** Regression family F-AA-R2-05, F-AA-R3-01/02, F-AA-R5-C-02, F-AA-R6-01, F-AA-R7-01; required R8 status-propagation check.

## Verdict

**Qualifying PASS with one MEDIUM finding.**

Rationale: I executed all seven mandatory reproduction/audit legs and pasted real outputs above. The reproduction package is present. There are zero CRITICAL findings and zero HIGH findings. The one new finding is MEDIUM and concerns a stale local status phrase in the companion Current State block, not the data, script, estimands, provenance, attached package, single operational counter, or convergence outcome.

---

# Bismillah ir-Rahman ir-Rahim
