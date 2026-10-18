# Bismillah ir-Rahman ir-Rahim

# R0428 -- F-AA-R5 Closing-Round Audit — Bayyinah Public-Ledger Allocation and Asymmetric-Measure Audits v0.4

**Chronological Index:** 290 of 995  
**Date:** 2026-07-19  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-AA-R5_claude_advisory.md  
**Source Format:** md  
**SHA-256:** `7dde4d18c5c314050a9d2eb11b385c028bd8e7fa745a36bceed47de85ee6e845`  

---

## R0428 · F-AA-R5 Closing-Round Audit — Bayyinah Public-Ledger Allocation and Asymmetric-Measure Audits v0.4

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-AA-R5_claude_advisory.md
- source_format: md
- text_sha256: 7dde4d18c5c314050a9d2eb11b385c028bd8e7fa745a36bceed47de85ee6e845

# F-AA-R5 Closing-Round Audit — Bayyinah Public-Ledger Allocation and Asymmetric-Measure Audits v0.4

**Auditor model identity:** Claude Opus 4.8
**Provider lineage:** Anthropic / Claude — **the producing lineage of this artifact.**
**Qualifying status:** **NON-QUALIFYING, QUARANTINED, ADVISORY-ONLY.** Under Standing Rule 7 a producer-lineage round cannot discharge the independence gate and **cannot count toward convergence**, regardless of technical outcome. This report is advisory input to the model council only.

## No-prior-state attestation

This assessment was produced by a **clean, independent instance** with **no prior findings, no memory, no personalization, and no residual state** carried into it. I did **not** read any other model-council report file, any prior F-AA-R1..R4 auditor output, or any producer scratch notes. My inputs were exactly the two supplied artifacts (`Bayyinah_AllocationAsymmetry_v0.4.md`, `Bayyinah_AllocationAsymmetry_AuditCompanion.md`), the original zip inventory, live first-party New York State Open Data endpoints, and public web/Zenodo lookups. All numbers reported below are **executed evidence** from live queries and my own independent code — not the expected numbers stated in the objective. Where an objective-stated number matched, I say so only after independent execution reproduced it.

---

## VERDICT

**INCOMPLETE (findings-bearing).** Steps 4, 5, and 6 were fully executed against live first-party data and PASS on their own terms with zero material discrepancies. Steps 1, 2, 3, and the supplied-comparator leg of Step 7 are **INCOMPLETE**: the reproduction package they require (`reproduce_paper2.py`, `MANIFEST.json`, `snapshot/gpsc-qqsz_FY2022-2024.json`) **was not supplied and is not recoverable** from any authoritative link. Per the mandatory execution protocol I do **not** infer their outputs and do **not** award PASS to any step that requires the frozen snapshot's own integrity chain.

Because a technical PASS requires **complete documented execution of steps 1–7 with zero CRITICAL/HIGH**, and execution of the package-dependent steps is impossible with the material provided, **only INCOMPLETE is available**. This is **missing-material incompleteness**, not an artifact defect — a distinction I preserve throughout. **No convergence is claimed or implied**; even had execution been complete, this is a producer-lineage round and is non-qualifying.

Severity tally of findings I raise: **0 CRITICAL, 0 HIGH, 2 MEDIUM, 3 LOW, 2 INFO.** None of the MEDIUM/LOW findings is a data-substrate error; all reported figures that could be independently recomputed reproduce exactly.

---

## EXECUTION MATRIX

| Step | Requirement | Status | Basis |
|---|---|---|---|
| 1 | `reproduce_paper2.py` integrity + offline (hash-OK, field inventory, FY totals, MWBE shares, composition, concentration/Gini, pre-2024, missing/zero) | **INCOMPLETE** | Script and frozen snapshot not supplied; unrecoverable. Underlying *figures* independently reproduced in Step 4, but the script's own hash-verification/offline-determinism cannot be executed. |
| 2 | `--selftest` perturbs all 45 statistics + schema | **INCOMPLETE** | Supplied script unavailable; cannot verify the 45-statistic comparator exists or fires as documented. |
| 3 | `--live` re-pull three years, no drift, exit 0 | **INCOMPLETE (script)** / live data independently PASS | Supplied comparator unavailable. I independently re-pulled all three years live (Step 4) with no drift vs the paper's stated figures. |
| 4 | Independent recompute, wholly independent code | **PASS (executed)** | Own code, live pull; every recomputable figure matches. |
| 5 | Live `gpsc-qqsz` vs first-party `twsw-2mqa` FY2024 count/sum, <0.1% divergence | **PASS (executed, with one precision caveat)** | Live queries; face divergence 0.089% (<0.1%); count divergence 0.510% (>0.1%). |
| 6 | Capital join `wcsa-vkhf` → `kizb-nxtu` / `ehz8-ag3n` (`proj_num`); no borough key | **PASS (executed)** | Live batch join 120/120 both tables; no borough key confirmed. |
| 7 | Adversarial perturbation flagged by comparator | **PARTIAL** | My **independent** comparator flags the drift and produces no false positive. The **supplied** `reproduce_paper2.py --live` comparator could not be run (INCOMPLETE). |

---

## RAW EXECUTED OUTPUTS AND CODE

All data retrieved without authentication from the New York State Open Data portal ([data.ny.gov](https://data.ny.gov/resource/gpsc-qqsz)).

### Package-recovery attempt (Steps 1–3 precondition)

Original zip inventory (`fresh-instance-audit-packet.zip`) contains **only the two markdown files**:

```
Archive:  fresh-instance-audit-packet.zip
  34508  2026-07-19 18:44   Bayyinah_AllocationAsymmetry_AuditCompanion.md
  22586  2026-07-19 18:44   Bayyinah_AllocationAsymmetry_v0.4.md
  2 files
```

The artifacts reference `reproduce_paper2.py`, `MANIFEST.json`, and `snapshot/gpsc-qqsz_FY2022-2024.json` (companion §A) but contain **no URL, DOI, or repository link** to them. The paper's own DOI is `[to be assigned on deposit]` (unminted). The three cited Zenodo records ([21436484](https://zenodo.org/records/21436484), [19894724](https://zenodo.org/records/19894724), [20069654](https://zenodo.org/records/20069654)) are the *governing/companion* papers (educational-fairness, financial-governance, and the al-Munāsabāt falsification study), not this procurement note, and do not carry the reproduction package. Web search for `reproduce_paper2.py` / `gpsc-qqsz` snapshot returned no matching artifact. **Conclusion: the reproduction package is unrecoverable.** Steps 1, 2, 3 are INCOMPLETE for missing material.

### Step 4 — Independent recompute (wholly independent code, live pull)

Code: `/home/user/workspace/independent_recompute_R5.py` (own urllib pull, own Gini/top-k/fingerprint; no supplied functions used). Unedited output:

```
FY2022: fetched 12156 rows
FY2023: fetched 12114 rows
FY2024: fetched 13718 rows
TOTAL ROWS: 37988

=== FY2022 ===
  n=12156 face_sum=54698007774.69 exp_sum=6837685984.96
  missing_contract_amount=712 explicit_zero=0
  MWBE count=1996 (16.42%)  face_share=3.27%  exp_share=4.25%

=== FY2023 ===
  n=12114 face_sum=63569204049.36 exp_sum=6681146956.30
  missing_contract_amount=1049 explicit_zero=111
  MWBE count=2251 (18.58%)  face_share=3.51%  exp_share=6.27%

=== FY2024 ===
  n=13718 face_sum=65189755228.64 exp_sum=8170228558.54
  missing_contract_amount=1348 explicit_zero=48
  MWBE count=2570 (18.73%)  face_share=3.95%  exp_share=7.06%
  -- process composition by FACE --
     'Authority Contract - Competitive Bid': $60,117,800,205 = 92.22%  (n=10876, 79.3%)
     'Authority Contract - Non-Competitive Bid': $5,071,955,024 = 7.78%  (n=1494, 10.9%)
  -- process composition by EXPENDITURE --
     'Authority Contract - Competitive Bid': 89.65%
     'Authority Contract - Non-Competitive Bid': 4.73%
     'Purchased Under State Contract': 3.24%
     'Non Contract Procurement/Purchase Order': 2.38%
  distinct vendor strings (all names) = 2907
  FACE top5=22.1% top10=30.4% top20=41.8% Gini=0.931
  EXP  top5=16.9% top10=26.2% top20=37.6% Gini=0.904
  negative face amounts = 0
  largest face vendors:
     KAWASAKI RAIL CAR INC: $6,460,041,130
     NEW FLYER OF AMERICA INC: $2,561,472,333
     HALMAR-RAILWORKS A JV: $1,878,276,491
     3RD TRACK CONSTRUCTORS: $1,809,977,480
     TUTOR PERINI CORP: $1,725,475,795
  pre-2024 face share = 91.7%  (2024+ = 8.3%)
  award-year range: 1984-2025

Stable-field fingerprint (18 present-in-rows fields, excluding fiscal_year + 3 annual-state fields):
  STABLE overlap 2022/2023 = 2115
  STABLE overlap 2022/2024 = 604
  STABLE overlap 2023/2024 = 1002
  EXACT all-field overlap 2022/2023 = 0
  EXACT all-field overlap 2022/2024 = 0
  EXACT all-field overlap 2023/2024 = 0
```

**Comparison to the objective's expected numbers (all matched by executed evidence):**

| Quantity | Expected (objective) | Executed | Match |
|---|---|---|---|
| Total rows | 37,988 | 37,988 | ✓ |
| FY2024 face | ~$65.19B | $65,189,755,228.64 | ✓ |
| FY2024 expenditure | $8.17B | $8,170,228,558.54 | ✓ |
| MWBE FY2024 count / face / exp | 18.7 / 3.95 / 7.06% | 18.73 / 3.95 / 7.06% | ✓ |
| FY2024 face top-10 / Gini | 30.4% / 0.931 | 30.4% / 0.931 | ✓ |
| 18-field vintage overlaps | 2,115 / 604 / 1,002 | 2,115 / 604 / 1,002 | ✓ |
| Exact all-field match | 0 | 0 / 0 / 0 | ✓ |

### Field-count and vendor-count verification (drill-down)

```
distinct vendor_name (all rows):                 2907
distinct vendor_name where contract_amount >0:   2656   <- paper's concentration basis
vendors with positive aggregated face:           2656
union of keys present across FY2024 rows:         22   (metadata declares 23; 'procurements' is null-only, dropped from row payloads)
stable field count (22 present-in-rows minus 4 excluded): 18
  -> 18-field STABLE overlap 2022/2023 = 2115
  -> 18-field STABLE overlap 2022/2024 = 604
  -> 18-field STABLE overlap 2023/2024 = 1002
enumerated 7-identity-field overlap:              3674 / 690 / 1892  (matches companion F-AA-R3-03 warning)
```

The paper's "2,656 distinct vendor strings" is vendors with positive aggregated face value (the Gini basis) — correct. The "18-field" method is accurate **at the row level**: rows carry 22 keys, minus the four fiscal-year/annual-state fields = 18. The enumerated 7-field reading reproduces the exact 3,674/690/1,892 the companion warns is *not* the method — corroborating the F-AA-R3-03 fix.

### Step 5 — Provenance and cross-dataset reconciliation (live)

```
gpsc-qqsz:  provenance = "community"  base = ehig-g5x3  attribution = Authorities Budget Office
twsw-2mqa:  provenance = "official"   attribution = Metropolitan Transportation Authority

gpsc-qqsz FY2024:  n=13718  face=$65,189,755,228.64  exp=$8,170,228,558.54
twsw-2mqa FY2024:  n=13648  face=$65,131,682,801.41

count divergence: 0.510%  (70 records)
face  divergence: 0.0891%  ($58,072,427)
```

Portal metadata independently confirms `gpsc-qqsz` is a **community** view and `twsw-2mqa` is the **official** first-party MTA dataset — matching the note's Section 3 provenance description exactly. First-party MWBE FY2024: 2,566 records / $2.577B face (3.96%) / $576.8M exp (7.05%) — consistent with the community-view shares within rounding.

### Step 6 — Capital join (live batch)

Code: `/home/user/workspace/capital_join_R5.py`. Unedited output:

```
wcsa-vkhf distinct project_number: 2609
wcsa-vkhf borough/county fields: NONE
kizb-nxtu distinct project_number: 4766
ehz8-ag3n distinct proj_num: 2512

Batch of 120 wcsa-vkhf project_numbers:
  matched in kizb-nxtu (project_number): 120/120
  matched in ehz8-ag3n (proj_num):       120/120

Full wcsa-vkhf set (2609):
  matched in kizb-nxtu: 2608 (100.0%)
  matched in ehz8-ag3n: 1455 (55.8%)

Worked example project_number D501CB08: kizb-nxtu total_allocation = 62963
```

Confirms: (a) `wcsa-vkhf` carries **no borough key** (only latitude/longitude/location), (b) the `project_number` join to `kizb-nxtu` and the `proj_num` join to `ehz8-ag3n` are **functional** (120/120 both), and (c) the column-name divergence (`project_number` vs `proj_num`, companion F-AA-2) is real and handled. Worked example `D501CB08` (the same key EV-2 cited) resolves to a real `$62,963` allocation.

### Step 7 — Adversarial perturbation (independent comparator)

```
Perturbed FY2024 row 8: contract_amount 4500000.00 -> 5500000.0 (vendor_is_a_mwbe=N)
  DRIFT DETECTED FY2024 face: baseline=65189755228.64 new=65190755228.64 delta=1000000.0
COMPARATOR VERDICT: DRIFT FLAGGED (exit nonzero)
Unchanged copy comparator: no drift (correct)
```

Altering one **non-MWBE** `contract_amount` by $1,000,000 in a snapshot copy is detected exactly (face total moves +$1,000,000); an unaltered copy produces no false positive. **Caveat:** this is *my* comparator. The claim that the **supplied** `reproduce_paper2.py --live` fires `exit 2` on this perturbation (companion F-AA-R3 leg) **could not be executed** and remains unverified — INCOMPLETE.

---

## SCOPE ASSESSMENT (judged against executed outputs)

- **Estimand and stock/flow integrity — CONFIRMED.** `contract_amount` is a stock (face value); FY2024 = $65.19B. `amount_expended_for_fiscal_year` is the annual flow = $8.17B. Award years span **1984–2025**; **91.7%** of summed face is pre-2024 (executed). The two estimands are named and never conflated. The three vintages overlap (2,115/604/1,002) and the note correctly states they are **never summed**. All confirmed by independent execution.
- **MWBE framing — CONFIRMED as descriptive prime-vendor statistics.** The note reports count 18.7% vs face 3.95% vs expenditure 7.06% as a descriptive count-versus-dollar asymmetry, with explicit disclaimers: no goal-attainment claim, no "operative substrate"/"short measure" language as a current claim, no compliance inference. Executed shares match exactly. The limitations (prime-only flag; no indirect participation, eligible-spend denominator, contract-specific goals, or waivers under Executive Law Article 15-A) are correctly stated.
- **Concentration as non-culpable structural explanation — CONFIRMED.** Face Gini 0.931 (top-10 30.4%) and expenditure Gini 0.904 (top-10 26.2%) reproduce exactly. The note uses concentration only as a *structural* mechanism for the asymmetry and explicitly refuses the Tier-3 steering/intent inference.
- **Fingerprint prose — CONFIRMED accurate.** The 18-field method (all fields except fiscal-year + three annual-state fields) reproduces 2,115/604/1,002; the enumerated-field reading yields 3,674/690/1,892 and is correctly flagged as *not* the method (F-AA-R3-03 fix landed).
- **Provenance accuracy — CONFIRMED.** Portal metadata: `gpsc-qqsz` = community view (base `ehig-g5x3`); `twsw-2mqa` = official MTA. Divergence disclosed. See Finding F-AA-R5-01 on the "under 0.1%" precision.
- **Cross-artifact v0.4 consistency — SUBSTANTIALLY CONFIRMED, one residual (F-AA-R5-02).** Reader header/abstract/Sections 6–7 and companion header/Current State uniformly state v0.4 and a zero-consecutive-pass evidentiary reality. The recurring version-propagation defect (F-AA-R2-05, F-AA-R3-01/02) appears resolved. One internal tension remains between the "one of two on the letter" phrasing and the "consecutive count = ZERO" phrasing (see F-AA-R5-02).

---

## REGRESSION ASSESSMENT (prior 20+ findings)

I regression-checked every prior finding that is independently checkable from live data. **No regression detected.**

| Prior finding | Substance | R5 executed check | Status |
|---|---|---|---|
| F-AA-1 (MED) | Capital data queryable, lacks borough key | `kizb-nxtu`/`ehz8-ag3n` queryable; `wcsa-vkhf` no borough key | Holds ✓ |
| F-AA-2 (INFO) | `proj_num` vs `project_number` name divergence | Confirmed; join works with correct keys | Holds ✓ |
| F-AA-R1-01 (HIGH) | Stock vs flow; 91.7% pre-2024 | 91.7% pre-2024, range 1984–2025 | Holds ✓ |
| F-AA-R1-02 (HIGH) | Prime-vendor flag, not goal substrate; exp 7.06% | 18.73/3.95/7.06 reproduced; framing descriptive | Holds ✓ |
| F-AA-R1-03 (HIGH) | Composition ≠ compliance | Composition reported descriptively only | Holds ✓ |
| F-AA-R1-04 (MED) | `gpsc-qqsz` community; `twsw-2mqa` differs | community/official metadata + 0.089% face divergence | Holds ✓ (see F-AA-R5-01) |
| F-AA-R1-05 (MED) | 37,988 three-year, not 111,879 | 12,156+12,114+13,718 = 37,988 | Holds ✓ |
| F-AA-R1-07 (LOW) | Missing (1,348) vs zero (48) split | 1,348 missing / 48 zero (FY2024) | Holds ✓ |
| F-AA-R1-08 (LOW) | Field inventory incl. `vendor_province_region` | Field present in schema; 22 row-keys/23 declared reconciled | Holds ✓ |
| F-AA-R2-03 (MED) | Exact all-field match = 0 | 0/0/0 confirmed | Holds ✓ |
| F-AA-R2-06 (LOW) | Both-measure concentration | Exp Gini 0.904, top-5 16.9% | Holds ✓ |
| F-AA-R3-03 (MED) | 18-field method vs enumerated reading | 2,115/604/1,002 (18-field); 3,674/690/1,892 (enum) | Holds ✓ |
| F-AA-R4-01 (INFO) | Exact all-field = 0 | Confirmed | Holds ✓ |

**F-AA-R1-08 nuance (new observation):** the portal *declares* 23 columns but rows carry only **22 keys** (`procurements` is null-only and dropped by Socrata from row payloads). This does not break the field-inventory abort logic in principle, but a manifest built from the *declared* schema (23) versus the *row-union* schema (22) would disagree — a subtlety the missing `MANIFEST.json` prevents me from verifying directly (see F-AA-R5-03).

---

## FINDINGS (namespace F-AA-R5; six elements each)

**F-AA-R5-01 — MEDIUM — Provenance divergence precision (reader Section 3 / companion §A)**
- *Identifier:* F-AA-R5-01
- *Severity:* MEDIUM
- *Locus:* Reader Section 3, "Provenance, stated precisely"; companion §A.
- *Substance (surface vs substrate):* The **surface** claim states the `gpsc-qqsz`↔`twsw-2mqa` gap is "a divergence under 0.1 percent." The executed **substrate** shows this is true only for the **dollar face value** (0.0891%); the **record-count** divergence is **0.510%** (70 records: 13,718 vs 13,648) — over five times the stated bound. The single "under 0.1 percent" phrase, attached to a sentence that reports both count and sum, understates the count-level divergence.
- *Disposition:* OPEN — recommend rewording to "a face-value divergence under 0.1 percent (record counts differ by ~0.5 percent)." Non-blocking; does not affect qualitative findings.
- *Cross-reference:* F-AA-R1-04; Step 5 executed output.

**F-AA-R5-02 — MEDIUM — Convergence-count phrasing tension (reader Sections 6–7 / companion Current State)**
- *Identifier:* F-AA-R5-02
- *Severity:* MEDIUM
- *Locus:* Reader Sections 6, 7; companion Current State bullets ("Consecutive-passing-round count: one of two on the letter" vs "toward convergence: ZERO").
- *Substance (surface vs substrate):* The **surface** presents two co-existing counts — "one of two on the letter of the criterion" (crediting F-AA-R4) and "ZERO … the count has never left zero." The **substrate** (the evidentiary reality the artifact itself argues) is that no round has been simultaneously independent and a genuine reproduction, so the honest count toward *convergence* is zero. Holding both a "one of two" and a "ZERO" figure in adjacent bullets invites a reader to cite the more favorable one out of context. The artifact's own governing logic favors ZERO.
- *Disposition:* OPEN — recommend collapsing to a single stated count (ZERO toward convergence) with the "letter of the criterion" note demoted to explanatory prose. Non-blocking.
- *Cross-reference:* F-AA-R3-01; companion lines 27–28.

**F-AA-R5-03 — LOW — Declared-schema vs row-union field-count (companion §A manifest description)**
- *Identifier:* F-AA-R5-03
- *Severity:* LOW
- *Locus:* Companion §A (frozen snapshot / MANIFEST field-list description); reader Section 8.
- *Substance (surface vs substrate):* The **surface** describes a manifest "field list" validated against rows. The live **substrate** shows the portal declares **23** columns while row payloads carry **22** keys (`procurements` is null-only and dropped per row). Because the `MANIFEST.json` is not supplied, I cannot confirm whether it lists 22 or 23 fields, and thus cannot confirm the "validated equal to the actual field set" claim (F-AA-R1-08 remedy) holds for this exact snapshot.
- *Disposition:* OPEN-UNVERIFIABLE (missing material). The 18-field fingerprint reproduces correctly regardless, so this is a documentation-completeness gap, not a demonstrated error.
- *Cross-reference:* F-AA-R1-08; field-count drill-down output.

**F-AA-R5-04 — LOW — Missing reproduction package with no authoritative link (whole artifact)**
- *Identifier:* F-AA-R5-04
- *Severity:* LOW (as an *artifact* defect; the *audit-material* gap is separately the cause of INCOMPLETE)
- *Locus:* Reader Section 8 "Data Availability and Reproduction"; companion §A.
- *Substance (surface vs substrate):* The **surface** repeatedly asserts a reproducible package (script + hash + manifest + snapshot) "accompany the published version." The **substrate** available to an auditor is that the package is absent from the delivered zip, the paper DOI is unminted, and no URL/repository is given — so a second party cannot in fact obtain the exact frozen rows the falsifiability criteria (companion §C) reference. The figures *are* reproducible from the live endpoint (I did so), but the *frozen, hash-pinned* reproduction the artifact centers on is not currently distributable.
- *Disposition:* OPEN — recommend depositing the package to a DOI and citing it inline before any convergence claim. This is missing-material, distinct from a computed-figure defect.
- *Cross-reference:* Steps 1–3 INCOMPLETE; package-recovery attempt.

**F-AA-R5-05 — LOW — Supplied-comparator adversarial claim unverifiable (companion F-AA-R3 leg)**
- *Identifier:* F-AA-R5-05
- *Severity:* LOW
- *Locus:* Companion F-AA-R3 appendix ("adversarially perturbed a non-MWBE statistic and confirmed `--live` flags it (exit 2)").
- *Substance (surface vs substrate):* The **surface** asserts the supplied `--live` comparator exits 2 on a perturbed non-MWBE amount. My **substrate** test confirms the *arithmetic* is detectable (an independent comparator flags a $1M perturbation and yields no false positive), but the *specific supplied comparator's* behavior (that it perturbs and detects all 45 statistics + schema, and exits 2) cannot be executed because the script is absent.
- *Disposition:* OPEN-UNVERIFIABLE (missing material). The detectability of the drift is confirmed; the supplied tool's conformance is not.
- *Cross-reference:* Step 7; F-AA-R5-04.

**F-AA-R5-06 — INFO — All independently recomputable figures reproduce exactly**
- *Identifier:* F-AA-R5-06
- *Severity:* INFO
- *Locus:* Reader Section 4 (all subsections).
- *Substance (surface vs substrate):* Surface and substrate **coincide**: totals (37,988; $65.19B; $8.17B), MWBE tri-vintage shares, ratios (4.7/2.7; 5.0/5.3/4.7; 3.9/3.0/2.7), composition (92.22% face competitive), concentration (top-5/10/20 = 22.1/30.4/41.8%; Gini 0.931; exp Gini 0.904), pre-2024 91.7%, missing/zero 1,348/48, fingerprint 2,115/604/1,002, exact-match 0, largest vendors (Kawasaki $6.46B, New Flyer $2.56B) — all reproduced from live data. No data-level discrepancy surfaced.
- *Disposition:* NOTED, no action.
- *Cross-reference:* Step 4; F-AA-R4 producer re-verification.

**F-AA-R5-07 — INFO — Producer-lineage non-qualification (whole round)**
- *Identifier:* F-AA-R5-07
- *Severity:* INFO
- *Locus:* This round.
- *Substance (surface vs substrate):* Surface: a competent execution that reproduces the figures. Substrate: the auditor is Anthropic/Claude — the producing lineage — so the round is non-qualifying under Standing Rule 7 and adds independence-of-*execution* evidence but **no independence-of-*lineage*** evidence. It cannot be one of the two consecutive passing rounds.
- *Disposition:* NOTED. Convergence must not be declared on this round.
- *Cross-reference:* F-AA-R3 (prior producer-lineage round); companion Current State.

---

## MISSING-MATERIAL vs ARTIFACT-DEFECT SUMMARY

- **Missing-material incompleteness** (cause of the INCOMPLETE verdict, *not* artifact defects): absence of `reproduce_paper2.py`, `MANIFEST.json`, and `snapshot/gpsc-qqsz_FY2022-2024.json`, with no authoritative recovery link. This blocks Steps 1, 2, 3 and the supplied-comparator leg of Step 7.
- **Artifact defects** (independent of missing material): F-AA-R5-01 (count-divergence precision), F-AA-R5-02 (convergence-count phrasing tension). Both MEDIUM, non-blocking, no CRITICAL/HIGH.
- **Documentation-completeness gaps** tied to missing material: F-AA-R5-03, F-AA-R5-04, F-AA-R5-05 (LOW/unverifiable).

## CONVERGENCE STATEMENT

**No convergence is claimed.** This is a producer-lineage, non-qualifying advisory round. Even setting lineage aside, execution of the package-dependent steps is incomplete, so a technical PASS is unavailable and the verdict is INCOMPLETE (findings-bearing). The consecutive-passing-round count toward convergence remains **zero** on the artifact's own governing logic; the closing gate still requires a **genuinely independent (non-OpenAI, non-Claude, non-Gemini-consistency-only) round that actually reproduces the figures from a distributable frozen package**.

---

### Sources (live first-party endpoints and public records used)

- MTA Procurement Report (All), community view `gpsc-qqsz`: https://data.ny.gov/resource/gpsc-qqsz.json and metadata https://data.ny.gov/api/views/gpsc-qqsz.json (provenance "community", base `ehig-g5x3`, attribution Authorities Budget Office).
- MTA Procurements: Beginning 2018, first-party `twsw-2mqa`: https://data.ny.gov/resource/twsw-2mqa.json (provenance "official", attribution Metropolitan Transportation Authority).
- Capital tables: `wcsa-vkhf` https://data.ny.gov/resource/wcsa-vkhf.json (locations, no borough key), `kizb-nxtu` https://data.ny.gov/resource/kizb-nxtu.json (`project_number`, allocations), `ehz8-ag3n` https://data.ny.gov/resource/ehz8-ag3n.json (`proj_num`).
- Governing/companion Zenodo records (not the reproduction package): https://zenodo.org/records/21436484, https://zenodo.org/records/19894724, https://zenodo.org/records/20069654.
- Portal dataset landing page: https://data.ny.gov/Transparency/MTA-Procurement-Report-All-/gpsc-qqsz

*Executed-code artifacts saved in workspace: `independent_recompute_R5.py`, `investigate_R5.py`, `capital_join_R5.py`, `live_snapshot_R5.json`.*

---

# Bismillah ir-Rahman ir-Rahim
