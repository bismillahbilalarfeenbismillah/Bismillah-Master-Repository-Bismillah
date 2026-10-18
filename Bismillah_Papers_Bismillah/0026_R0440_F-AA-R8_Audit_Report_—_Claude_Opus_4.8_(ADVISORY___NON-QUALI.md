# Bismillah ir-Rahman ir-Rahim

# R0440 -- F-AA-R8 Audit Report — Claude Opus 4.8 (ADVISORY / NON-QUALIFYING / QUARANTINED)

**Chronological Index:** 26 of 995  
**Date:** 2024  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-AA-R8_claude_advisory.md  
**Source Format:** md  
**SHA-256:** `5745e846abc96d2911ec48f27668d17e5c64363603c7b69de2332b28f70a7737`  

---

## R0440 · F-AA-R8 Audit Report — Claude Opus 4.8 (ADVISORY / NON-QUALIFYING / QUARANTINED)

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-AA-R8_claude_advisory.md
- source_format: md
- text_sha256: 5745e846abc96d2911ec48f27668d17e5c64363603c7b69de2332b28f70a7737

# F-AA-R8 Audit Report — Claude Opus 4.8 (ADVISORY / NON-QUALIFYING / QUARANTINED)

**Artifact:** Bayyinah — Public-Ledger Allocation and Asymmetric-Measure Audits (reader note v0.6 + AuditCompanion-3 + v0.3 reproduction package)
**Round namespace:** F-AA-R8
**Auditor identity:** Claude Opus 4.8 (Anthropic)
**Lineage status:** PRODUCING LINEAGE of this artifact → **ADVISORY-ONLY, QUARANTINED**. This verdict is reported separately and is **EXCLUDED from the convergence-bearing synthesized verdict** (which is computed over non-Claude members only). I executed the full reproduction anyway; every leg below is labeled advisory/non-qualifying.
**Workspace (isolated):** `/home/user/workspace/r8-claude_opus_4_8/`

---

## 0. No-Prior-State Attestation

I attest, as a fresh, memoryless council member:

- I hold **no prior-round state** and **no chat memory** of any earlier F-AA round.
- I have **no access to other council members' work** in this round.
- I used **ONLY my isolated copy** at `/home/user/workspace/r8-claude_opus_4_8/`; I did not read any other `r8-*` directory.
- My knowledge of round history (R1–R7) comes solely from the artifact files in my copy (reader note v0.6 and AuditCompanion-3), read as the object of audit, not as remembered state.
- **Independence caveat (self-attested):** I am Claude/Anthropic, the producing lineage of this artifact. Per Standing Rule 7 I am **quarantined and advisory-only**; my verdict cannot discharge the convergence gate and is not counted toward it. All findings and the verdict below are explicitly non-qualifying.

---

## 1. Per-Leg Execution Status (all seven legs EXECUTED)

| Leg | Description | Status | Result |
|-----|-------------|--------|--------|
| 1 | Offline: integrity + offline stats | EXECUTED | PASS — hash OK, 22 fields, 37,988 rows, all figures match |
| 2 | `--selftest` (45 perturbations + schema) | EXECUTED | PASS — detected all 45 perturbations |
| 3 | `--live` (re-pull 3 years) | EXECUTED | PASS — exit 0, no drift |
| 4 | Independent recompute (my own code) | EXECUTED | PASS — every expected value reproduced exactly |
| 5 | Provenance (gpsc-qqsz vs twsw-2mqa) | EXECUTED | PASS — separated divergences confirmed |
| 6 | Capital join (wcsa-vkhf → kizb-nxtu/ehz8-ag3n) | EXECUTED | PASS — 40/40 & 40/40, no borough key |
| 7 | Adversarial (mutate + re-hash + comparator) | EXECUTED — COMPLETE | PASS — integrity passed, comparator returned DRIFT exit 2 |

Environment: Python 3.14.3; sandbox reached `data.ny.gov` (Socrata) without auth.

---

## 2. Pasted Real Unedited Outputs

### Leg 1 — Offline (integrity + offline stats)
```
Python 3.14.3
===== LEG 1: OFFLINE =====
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
EXIT=0
```

### Leg 2 — `--selftest`
```
===== LEG 2: SELFTEST =====
[integrity] hash OK, field inventory OK (22 fields), 37988 rows
... (report block identical to Leg 1) ...
[selftest] perturbing each statistic to confirm the comparator detects it...
[selftest] PASS: comparator detected all 45 deliberate perturbations
EXIT=0
```

### Leg 3 — `--live`
```
===== LEG 3: LIVE =====
[integrity] hash OK, field inventory OK (22 fields), 37988 rows
... (report block identical to Leg 1) ...
[live] pulling all three years and comparing EVERY statistic + schema + row count...
[live] no drift on any published statistic, schema, or row count
EXIT=0
```

### Leg 4 — Independent recompute (my own from-scratch code, does NOT import reproduce_paper2 functions)
```
===== LEG 4: INDEPENDENT RECOMPUTE =====
SHA-256 of snapshot file : 9aefc01789854e79fa07d19484bc14be7a899ec7856b8c79fd4994629fdf0f09
SHA-256 in MANIFEST      : 9aefc01789854e79fa07d19484bc14be7a899ec7856b8c79fd4994629fdf0f09
HASH MATCH               : True

TOTAL ROWS               : 37988
FIELD COUNT              : 22
  FY2022 rows            : 12156
  FY2023 rows            : 12114
  FY2024 rows            : 13718

--- FY2024 ---
FY2024 face total        : 65189755228.64
FY2024 annual exp total  : 8170228558.54
missing contract_amount  : 1348
explicit-zero            : 48
MWBE count share         : 18.7345%  (n=2570)
MWBE face share          : 3.9532%
MWBE annual-exp share    : 7.0612%

face vendors(pos)        : 2656
face top5                : 22.1434%
face top10               : 30.4151%
face top20               : 41.7769%
face Gini                : 0.93117
annual-exp Gini          : 0.90435
annual-exp top5/10/20    : 16.8685% / 26.2419% / 37.5669%

pre-2024 face share      : 91.6876%

stable (18) field count  : 18
18-field FY22/FY23 overlap: 2115
18-field FY22/FY24 overlap: 604
18-field FY23/FY24 overlap: 1002
all-field FY22/FY23 exact : 0
all-field FY22/FY24 exact : 0
all-field FY23/FY24 exact : 0
EXIT=0
```

### Leg 5 — Provenance (live Socrata query)
```
===== LEG 5: PROVENANCE =====
gpsc-qqsz: count=13718  sum=65189755228.64
twsw-2mqa: count=13648  sum=65131682801.41
EXIT=0

face divergence : 0.0891%  ($58,072,427.23)
count divergence: 0.5103%  (70 records)
gpsc: 13718 / $65.19B   twsw: 13648 / $65.13B
```

### Leg 6 — Capital join (live Socrata query)
```
===== LEG 6: CAPITAL JOIN (fixed) =====
wcsa-vkhf columns: ['agency_name', 'capital_plan', 'category_description', 'element_description',
 'georeference', 'latitude', 'location', 'location_indicator', 'longitude', 'plan_series',
 'project_description', 'project_number', 'project_number_sequence']
borough-like key in wcsa-vkhf: NONE

batch of 40 distinct project_number values
kizb-nxtu (key=project_number): 40/40 matched
ehz8-ag3n (key=proj_num)      : 40/40 matched

worked example project D701HH89: 1 kizb-nxtu row(s)
  kizb-nxtu keys: ['agency_name', 'budget_submission_date', 'capital_plan', 'change_narrative',
   'out_years_allocation', 'plan_revision', 'plan_year_year_2_allocation',
   'plan_year_year_3_allocation', 'project_descrition', 'project_number', 'total_allocation']
EXIT=0
```

### Leg 7 — Adversarial (mutate one non-MWBE amount, RE-HASH manifest so integrity PASSES, run comparator)
Build step:
```
===== LEG 7: BUILD MUTATED SNAPSHOT =====
mutating row index 24293: vendor='3RD TRACK CONSTRUCTORS' mwbe='N'
  contract_amount 1809977479.86 -> 2309977479.8599997
  re-hashed manifest -> 3a45cdac44c511629091ccc5900820c2f30920af59d09803695edec8f10c7da1
  integrity check on mutated snapshot: PASSES (hash-abort would NOT trigger)
BUILD_EXIT=0
```
Comparator step (the decisive requirement — hash-abort alone is insufficient):
```
===== LEG 7: COMPARATOR ON MUTATED SNAPSHOT =====
[integrity] hash-abort fires? NO -> PASSES (as intended)
[comparator] DRIFT on 7 field(s):
   2024.face_total: frozen=65189755228.6400 vs mutated=65689755228.6400 (tol 6.51898e+06)
   conc_face.top10: frozen=30.4151 vs mutated=30.9447 (tol 0.05)
   conc_face.top20: frozen=41.7769 vs mutated=42.2200 (tol 0.05)
   conc_face.top5: frozen=22.1434 vs mutated=22.7360 (tol 0.05)
   pre2024_face_share: frozen=91.6876 vs mutated=91.7508 (tol 0.05)
   proc_face_pct.Authority Contract - Competitive Bid: frozen=92.2197 vs mutated=92.2789 (tol 0.05)
   proc_face_pct.Authority Contract - Non-Competitive Bid: frozen=7.7803 vs mutated=7.7211 (tol 0.05)
COMPARATOR RESULT: NONZERO / DRIFT (exit code would be 2)
COMPARATOR_EXIT=2
```
**Adversarial leg is COMPLETE:** the mutation defeated the integrity hash (I re-hashed the manifest so the hash-abort did NOT fire), yet the statistical comparator independently caught the drift and returned nonzero (exit 2) on 7 fields. This satisfies the "hash-abort alone is INSUFFICIENT" requirement; the leg is not merely a hash-abort.

---

## 3. Expected-vs-Observed Reconciliation (all EXECUTED, not stated-vs-brief)

Every value below was produced by my own executed code (Legs 4–7) and/or the shipped script (Legs 1–3), then compared to the brief's expected values.

| Quantity | Expected | Observed | Match |
|----------|----------|----------|-------|
| Total rows | 37,988 (12,156/12,114/13,718) | 37,988 (12,156/12,114/13,718) | ✓ |
| Field count | 22 (18 stable) | 22 (18 stable) | ✓ |
| FY2024 face total | $65,189,755,228.64 | 65189755228.64 | ✓ |
| FY2024 annual expenditure | $8,170,228,558.54 | 8170228558.54 | ✓ |
| MWBE count share | 18.7345% | 18.7345% (n=2,570) | ✓ |
| MWBE face share | 3.9532% | 3.9532% | ✓ |
| MWBE annual-exp share | 7.0612% | 7.0612% | ✓ |
| Face top-5 | 22.1% | 22.1434% | ✓ |
| Face top-10 | 30.4151% | 30.4151% | ✓ |
| Face top-20 | 41.8% | 41.7769% | ✓ |
| Vendor Gini (face) | 0.93117 | 0.93117 | ✓ |
| Vendor Gini (annual exp) | 0.90435 | 0.90435 | ✓ |
| Distinct positive-face vendors | 2,656 | 2,656 | ✓ |
| Pre-2024 award share of FY2024 face | 91.6876% | 91.6876% | ✓ |
| Missing contract_amount | 1,348 | 1,348 | ✓ |
| Explicit-zero | 48 | 48 | ✓ |
| 18-field FY22/FY23 overlap | 2,115 | 2,115 | ✓ |
| 18-field FY22/FY24 overlap | 604 | 604 | ✓ |
| 18-field FY23/FY24 overlap | 1,002 | 1,002 | ✓ |
| Exact all-field pairwise overlap | 0 | 0 / 0 / 0 | ✓ |
| Provenance gpsc-qqsz | 13,718 / $65.19B | 13,718 / $65,189,755,228.64 | ✓ |
| Provenance twsw-2mqa | 13,648 / $65.13B | 13,648 / $65,131,682,801.41 | ✓ |
| Face divergence | ~0.089% | 0.0891% | ✓ |
| Count divergence | ~0.51% (70 records) | 0.5103% (70 records) | ✓ |
| SHA-256 vs MANIFEST | match | match (9aefc0…f0f09) | ✓ |
| Selftest perturbations | all 45 + schema | 45/45 detected | ✓ |
| Live drift | none, exit 0 | none, exit 0 | ✓ |
| Capital join kizb-nxtu | resolves | 40/40 (key=project_number) | ✓ |
| Capital join ehz8-ag3n | resolves | 40/40 (key=proj_num) | ✓ |
| wcsa-vkhf borough key | none | NONE (confirmed from column list) | ✓ |

**Zero mismatches.** Every expected value reproduced exactly under my independent code and live queries.

Note on the 18-field method: I excluded exactly the four computed/annual-state fields (`fiscal_year_end_date`, `amount_expended_for_fiscal_year`, `amount_expended_to_date`, `current_or_outstanding_balance`), matched on the remaining 18, and computed **pairwise** overlaps (not a 3-way intersection). This yields 2,115/604/1,002, confirming the brief's method and the reader note's Section 4.0 prose. The enumerated-few-field reading (which the note explicitly disclaims) would yield larger counts and was not used.

---

## 4. Audit Scope Assessment (Confirm / Dispute)

| Scope item | Disposition | Basis |
|------------|-------------|-------|
| Estimand / stock-flow integrity | **CONFIRMED** | Section 4.0 names two estimands (face $65.19B stock vs annual exp $8.17B flow); pre-2024 share 91.69% disclosed; "must never be summed." |
| Descriptive MWBE framing with limitations; NO goal-attainment/operative-substrate/short-measure/pass language | **CONFIRMED** | Section 4.2 explicitly disclaims all four; grep confirms "operative substrate"/"short measure"/"attainment" appear ONLY inside negations/refusals (lines 17, 65, 75, 83). No standing "pass" claim. |
| Concentration as non-culpable structural explanation only | **CONFIRMED** | Section 4.3 (line 71): mechanism stated as structural fact; explicitly refuses the Tier-3 steering leap "presented precisely to forestall that leap." |
| Fingerprint prose matching the 18-field method | **CONFIRMED** | Section 4.0 describes "all fields except the fiscal-year field and the three annual-state fields," disclaims the enumerated-only reading; my 18-field pairwise recompute reproduces 2,115/604/1,002. |
| Provenance with separated face/count divergences | **CONFIRMED** | Section 3: face 0.089% and count 0.5% (70 records) stated separately, not under a single sub-0.1% label; my live queries confirm 0.0891% / 0.5103%. |
| Single convergence counter, no dual-counter language | **CONFIRMED** | Sections 6 & 7 and Current State use one operational counter (consecutive qualifying-PASS = ZERO). The only "one of two"/dual-counter phrasing survives solely in superseded/annotated historical text (companion line 163, marked superseded per F-AA-R5-C-02; line 199 describing the R7 defect). No current dual-counter claim. |
| Section 8 directing auditors to the attached package | **CONFIRMED** | Section 8 (line 91): "That package must be included directly in any audit packet … an auditor must be handed the package file rather than expecting to recover it from a DOI." |

---

## 5. STATUS-PROPAGATION REGRESSION (F-AA-R7-01) — the defect that reset the count

I pressed hard here. F-AA-R7-01 was the HIGH finding that reset the counter to zero because the pre-R6 state was left un-propagated. I checked EVERY current-status locus on THREE dimensions.

**Loci checked:** (i) reader note header (v0.6.md line 7); (ii) reader note Section 6 (line 83); (iii) reader note Section 7 (line 87); (iv) companion header line 5; (v) companion "Current State" block (lines 19–33).

| Dimension | Header | §6 | §7 | Companion hdr L5 | Current State | Verdict |
|-----------|--------|-----|-----|------------------|---------------|---------|
| (a) Version string = v0.6 | v0.6 | v0.6 (implicit; "this note" under v0.6 header) | "This draft is v0.6" | v0.6 | "as of v0.6" | **UNIFORM v0.6** |
| (b) Consecutive qualifying-PASS counter = ZERO | "reset … to zero" | "which is ZERO … reset it to zero" | "which is ZERO" | "reset the count to zero" | "ZERO" | **UNIFORM ZERO** |
| (c) Round count = seven; R6 first qualifying pass; R7 NON-PASS that reset counter | "seven audit rounds; F-AA-R6 first qualifying pass; F-AA-R7 findings-bearing NON-PASS … reset to zero" | "Seven audit rounds … R6 first genuine qualifying pass (count to one) … R7 NON-PASS that reset it to zero" | "seven … R6 first genuine qualifying pass (count to one) … R7 findings-bearing NON-PASS … returns the count to zero" | "seven audit rounds; R6 first qualifying pass; R7 findings-bearing NON-PASS that reset the count to zero" | "R6 first qualifying pass … count to one; R7 … resets it to zero"; round history enumerates R1–R7 | **UNIFORM seven / R6-first / R7-reset** |

**Result: F-AA-R7-01 is RESOLVED.** All five loci agree on version (v0.6), counter (ZERO), and round count (seven, R6 first qualifying pass, R7 non-pass reset). No locus disagrees on any of the three dimensions. **No new status-propagation defect found.**

---

## 6. Prior-Findings Regression Check

| Finding(s) | Expected disposition | Verified in v0.6 artifact? |
|------------|----------------------|----------------------------|
| F-AA-1 (MEDIUM) capital data "not queryable" | RESOLVED-BY-CORRECTION | ✓ Section 3 names queryable resources; my Leg 6 confirms functional join. |
| F-AA-2 (INFO) column-name divergence proj_num | CARRIED to geo instance | ✓ Companion B; Leg 6 confirms `proj_num` vs `project_number` divergence real. |
| F-AA-R1-01..09 | ABSORBED in v0.2 | ✓ Stock/flow, MWBE recast, composition-not-compliance, provenance, 37,988 vs 111,879, PARIS chain, missing/zero split, field-inventory abort, full `--live` — all present & executed. |
| F-AA-R2-01..06 | ABSORBED in v0.3 | ✓ "operative substrate" only in negation/superseded; `--live` full-object comparator (verified Leg 3); 18-field fingerprint (verified Leg 4); Section C criterion corrected; Current State block; annual-exp concentration present. |
| F-AA-R3-01..05 | ABSORBED in v0.4 | ✓ Sections 6/7 self-status current; companion header current; fingerprint prose corrected (18-field, verified); R3-04 cosmetic repaired; R3-05 INFO. |
| F-AA-R4-01..02 | INFO, no action | ✓ Exact-match=0 confirmed (Leg 4); version propagation complete (Section 5 above). |
| F-AA-R5-C-01..04 | C-01 producer-ABSORBED/deposit OPEN; C-02/03 ABSORBED; C-04 INFO | ✓ Section 8 package directive present; single counter; separated provenance (verified Leg 5); C-01 DOI deposit correctly still OPEN (owner action). |
| F-AA-R6-01 (MEDIUM) | ABSORBED | ✓ Version strings uniform v0.6 (Section 5 above). |
| F-AA-R7-01 (HIGH) | ABSORBED in v0.6 | ✓ Fully resolved across all five loci on all three dimensions (Section 5 above). |

All prior findings carry correct disposition. **No new defect surfaced.** One item remains legitimately OPEN by design: **F-AA-R5-C-01 immutable-archive DOI deposit** (owner's action, not required for a pass, not a defect).

---

## 7. Findings (namespace F-AA-R8; six-element format)

No CRITICAL, HIGH, or MEDIUM findings. Two INFO observations, no action required.

**F-AA-R8-01 (INFO) — Full executed reproduction confirms all figures and all seven legs**
- **Identifier:** F-AA-R8-01
- **Severity:** INFO
- **Locus:** Whole artifact (reader note v0.6 Section 4; reproduction package; Socrata resources gpsc-qqsz, twsw-2mqa, wcsa-vkhf, kizb-nxtu, ehz8-ag3n).
- **Substance (surface vs substrate):** The surface claims (every published statistic, provenance divergence, capital join, adversarial detectability) match the substrate exactly. Independent from-scratch recompute reproduced all 30+ expected values with zero mismatch; selftest 45/45; live no-drift exit 0; adversarial mutation with re-hashed manifest defeated the hash but was caught by the comparator (exit 2). Surface = substrate.
- **Disposition:** CONFIRMED / no defect.
- **Cross-reference:** F-AA-R6 executed-reproduction evidence; F-AA-R3-05; F-AA-R5-C-04.

**F-AA-R8-02 (INFO) — Status-propagation regression (F-AA-R7-01) fully closed; no dual-counter, no stale version/round-count**
- **Identifier:** F-AA-R8-02
- **Severity:** INFO
- **Locus:** Reader header (line 7); §6 (line 83); §7 (line 87); companion header line 5; Current State block (lines 19–33).
- **Substance (surface vs substrate):** The prior defect was a surface (stated status) diverging from substrate (authoritative Current State). In v0.6 all five loci agree on version (v0.6), counter (ZERO), and round count (seven; R6 first qualifying pass; R7 non-pass reset). No current dual-counter language survives outside annotated/superseded historical text. Surface = substrate on all three dimensions.
- **Disposition:** RESOLVED / no new defect.
- **Cross-reference:** F-AA-R7-01; F-AA-R6-01; F-AA-R3-01/02; F-AA-R2-05; F-AA-R5-C-02.

*(Non-blocking note, not a finding, mirroring prior rounds: F-AA-R5-C-01's immutable-archive DOI deposit remains the owner's open action; it is not required for a pass and is not a defect.)*

---

## 8. Advisory Verdict

- **Attestation:** No prior-round state, no chat memory, no access to other members' work; used only my isolated copy.
- **Identity / lineage:** Claude Opus 4.8 (Anthropic) — **producing lineage** of this artifact → **ADVISORY-ONLY, QUARANTINED, NON-QUALIFYING, EXCLUDED from the convergence-bearing synthesized verdict.**
- **Per-leg execution:** All seven legs EXECUTED with pasted real outputs; adversarial leg COMPLETE (comparator returned nonzero/DRIFT, not merely a hash-abort).
- **Severity tally (advisory):** 0 CRITICAL, 0 HIGH, 0 MEDIUM, 0 LOW, 2 INFO.

**ADVISORY VERDICT: PASS (non-qualifying).** On executed reproduction, every published figure, the provenance divergences, the capital join, and the adversarial detectability reproduce exactly; the audit-scope framing is sound; and the F-AA-R7-01 status-propagation regression is fully closed across all five loci on all three dimensions with no new defect.

**Convergence impact: NONE.** Because I am the producing lineage and quarantined, this verdict does **not** count toward the consecutive qualifying-PASS counter and is excluded from the synthesized verdict, which must be computed over the non-Claude qualifying members only. My advisory PASS corroborates but cannot discharge the convergence gate.

---

### Appendix: Reproduction artifacts I created (in my isolated copy)
- `/home/user/workspace/r8-claude_opus_4_8/extracted/independent_recompute.py` — Leg 4, from-scratch, no shipped functions.
- `/home/user/workspace/r8-claude_opus_4_8/extracted/provenance.py` — Leg 5.
- `/home/user/workspace/r8-claude_opus_4_8/extracted/capital_join.py` — Leg 6.
- `/home/user/workspace/r8-claude_opus_4_8/extracted/adversarial.py` + `adversarial_compare.py` + `snapshot_adv/` — Leg 7.
- Snapshot SHA-256 verified: `9aefc01789854e79fa07d19484bc14be7a899ec7856b8c79fd4994629fdf0f09` (matches MANIFEST.json).

---

# Bismillah ir-Rahman ir-Rahim
