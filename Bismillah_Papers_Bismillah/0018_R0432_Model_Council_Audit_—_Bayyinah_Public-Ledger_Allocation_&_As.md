# Bismillah ir-Rahman ir-Rahim

# R0432 -- Model Council Audit — Bayyinah Public-Ledger Allocation & Asymmetric-Measure Audits v0.5, Round 6 (F-AA-R6)

**Chronological Index:** 18 of 995  
**Date:** 2024  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-AA-R6_claude_advisory.md  
**Source Format:** md  
**SHA-256:** `aa8ab75b5197692fa8759d28288cc6c1d7a33f3d523f2a08a07907fc875456cf`  

---

## R0432 · Model Council Audit — Bayyinah Public-Ledger Allocation & Asymmetric-Measure Audits v0.5, Round 6 (F-AA-R6)

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-AA-R6_claude_advisory.md
- source_format: md
- text_sha256: aa8ab75b5197692fa8759d28288cc6c1d7a33f3d523f2a08a07907fc875456cf

# Model Council Audit — Bayyinah Public-Ledger Allocation & Asymmetric-Measure Audits v0.5, Round 6 (F-AA-R6)

## Auditor identity and status

- **Model identity:** Claude Opus 4.8
- **Lineage:** Anthropic / Claude — **the producing lineage** of this artifact program.
- **Advisory status:** **QUARANTINED, ADVISORY-ONLY.** Excluded from the convergence-bearing verdict under Standing Rule 7 (producer-lineage cannot discharge the independence gate). **A Claude PASS remains advisory only and cannot affect the consecutive qualifying-PASS counter or convergence.**
- **Round / namespace:** F-AA-R6; findings use namespace `F-AA-R6`.
- **Council framing:** One of several frontier models independently auditing the same packet. This report is my independent angle; a synthesizer compares reports only after all members finish.

### Explicit no-prior-state attestation

I attest that I performed this audit as a **brand-new, memoryless, independent instance**. I did **not** use memory, personalization, saved state, prior audits, prior findings reports, or any other council member's work. I did **not** inspect model-council files or directories belonging to other members. I worked **only** in `/home/user/workspace/r6-claude-opus-4-8` and the submitted packet at `/home/user/workspace/uploaded_attachments/883b6ed7ec3d439c892de8b18ef0e846/new-audit-package.zip`, which I independently unzipped. Every figure below was recomputed in this session from the frozen snapshot and/or live New York State Open Data; nothing is carried from prior rounds. All quoted expected values were taken from the packet documents solely as targets to test against, not as substitutes for computation.

---

## Verdict

**ADVISORY PASS (advisory-only; non-convergence-bearing).**

- Severity tally: **0 CRITICAL, 0 HIGH, 1 MEDIUM, 1 INFO.**
- All seven protocol steps executed with real outputs (pasted below). Packet was **COMPLETE** (snapshot JSON, MANIFEST, and `reproduce_paper2.py` all present) — I did **not** return INCOMPLETE and did **not** reconstruct anything from Zenodo or the web.
- Every principal figure reproduces exactly under both the supplied script and my own independent code.
- One new **MEDIUM** defect found (companion header version-lag, F-AA-R6-01) — a recurrence of the propagation failure mode the program's own standing rule exists to prevent. Because a Claude round is advisory-only, this finding **does not** change the qualifying counter; it is offered as advisory input for the synthesizer and producer.
- **The single operational metric — the consecutive qualifying-PASS count — remains ZERO.** My advisory PASS cannot increment it. Convergence still requires two consecutive qualifying (0 CRITICAL / 0 HIGH, executed-reproduction, non-producer-lineage) passes on the then-current artifact.

> Because I am the producing lineage, even a clean result cannot be credited as convergence. My value here is executed evidence plus a fresh adversarial angle, not a pass credit.

---

## Per-step execution status

| Step | Description | Status |
|---|---|---|
| 0 | Packet completeness check + independent unzip | **PASS** (complete) |
| 1 | `python3 reproduce_paper2.py` (offline) | **PASS** |
| 2 | `python3 reproduce_paper2.py --selftest` | **PASS** |
| 3 | `python3 reproduce_paper2.py --live` | **PASS** (network available; exit 0; no drift) |
| 4 | Own independent recomputation (no supplied functions) | **PASS** |
| 5 | Provenance reconciliation (`gpsc-qqsz` vs `twsw-2mqa`) | **PASS** |
| 6 | Capital join (`wcsa-vkhf` → `kizb-nxtu` / `ehz8-ag3n`) | **PASS** |
| 7 | Adversarial mutation + comparator | **PASS** (drift flagged, exit 2) |

Environment: Python 3.14.3. Snapshot SHA-256 `9aefc01789854e79fa07d19484bc14be7a899ec7856b8c79fd4994629fdf0f09` (matches manifest).

---

## Packet completeness (gate)

Independent unzip produced the reader note, the audit companion, and a nested `Bayyinah_AllocationAsymmetry_ReproPackage.zip`, which further contained exactly the mandated trio:

```
repro/reproduce_paper2.py
repro/snapshot/gpsc-qqsz_FY2022-2024.json
repro/snapshot/MANIFEST.json
```

The reproduction package is **present in this R6 packet** (unlike R5, where its absence caused F-AA-R5-C-01). Proceeding with a real reproduction rather than an INCOMPLETE return.

---

## Step 1 — `python3 reproduce_paper2.py` (offline, unedited output)

```
=== PYTHON VERSION ===
Python 3.14.3
=== STEP 1: python3 reproduce_paper2.py ===
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

**Confirmed:** hash-OK and field-inventory-OK; FY totals; vintage MWBE count/face/expenditure shares (both measures); both-measure process composition; concentration and Gini (face 0.931, expenditure 0.904); pre-2024 share 91.7%; missing/zero counts (FY2024: 1,348/48). **Step 1 PASS.**

---

## Step 2 — `--selftest` (unedited output)

```
=== STEP 2: --selftest ===
[integrity] hash OK, field inventory OK (22 fields), 37988 rows
... (report block identical to Step 1) ...
[selftest] perturbing each statistic to confirm the comparator detects it...
[selftest] PASS: comparator detected all 45 deliberate perturbations
EXIT_CODE=0
```

Reconciliation of the "45" count (I verified this independently rather than trusting the label):

```
numeric stat count = 44
plus schema => total perturbations = 45
```

**Confirmed:** the comparator detects **all 44 numeric statistics plus the schema perturbation = 45 total**, i.e. "all 45 stats plus schema" is satisfied as 44 stats + schema. Exit 0. **Step 2 PASS.**

---

## Step 3 — `--live` (unedited output)

Network reachability pre-check: `HTTP 200 in 0.19s` against `https://data.ny.gov/resource/gpsc-qqsz.json`. Network is available, so this step is eligible to PASS (per protocol, I would have marked it INCOMPLETE and never PASS if the network were unavailable).

```
=== STEP 3: --live ===
[integrity] hash OK, field inventory OK (22 fields), 37988 rows
... (report block identical to Step 1) ...
[live] pulling all three years and comparing EVERY statistic + schema + row count...
[live] no drift on any published statistic, schema, or row count
EXIT_CODE=0
```

**Confirmed:** live re-pull of all three years; **no drift**; **exit 0**. **Step 3 PASS.**

---

## Step 4 — Own independent code (NOT the supplied functions)

I wrote `claude_independent_recompute.py` from scratch: own JSON parse, own aggregation, **two independent Gini formulas** (ordered-cumulative and mean-absolute-difference) cross-checked against each other, own fingerprint overlap logic, and an explicit guard proving I do **not** use a three-way intersection or an identity-subset. It imports nothing from `reproduce_paper2.py`.

Unedited output:

```
[claude] snapshot sha256      = 9aefc01789854e79fa07d19484bc14be7a899ec7856b8c79fd4994629fdf0f09
[claude] manifest sha256      = 9aefc01789854e79fa07d19484bc14be7a899ec7856b8c79fd4994629fdf0f09
[claude] hash match           = True
[claude] TOTAL ROWS           = 37988   (expect 37,988)
[claude] FY2024 record count  = 13718  (expect 13,718)
[claude] FY2024 face total    = $65,189,755,228.64  ($65.1898B; expect ~$65.19B)
[claude] FY2024 AE total      = $8,170,228,558.54  ($8.1702B; expect ~$8.17B)
[claude] FY2024 missing face  = 1348  (expect 1,348)
[claude] FY2024 zero face     = 48  (expect 48)
[claude] MWBE count           = 2570
[claude] MWBE count %         = 18.7345%  (expect 18.73%)
[claude] MWBE face %          = 3.9532%  (expect 3.95%)
[claude] MWBE AE %            = 7.0612%  (expect 7.06%)
[claude] distinct positive-face vendors = 2656  (expect 2,656)
[claude] FY2024 top-5  face conc = 22.1434%
[claude] FY2024 top-10 face conc = 30.4151%  (expect 30.42%)
[claude] FY2024 top-20 face conc = 41.7769%
[claude] FACE Gini (formula A) = 0.93117  (expect ~0.931)
[claude] FACE Gini (formula B) = 0.93117  (cross-check)
[claude] AE   Gini (formula A) = 0.90435  (expect ~0.904)
[claude] AE   Gini (formula B) = 0.90435  (cross-check)
[claude] total non-computed fields = 22
[claude] fingerprint fields used   = 18  (expect 18)
[claude] excluded fields           = ['amount_expended_for_fiscal_year', 'amount_expended_to_date', 'current_or_outstanding_balance', 'fiscal_year_end_date']
[claude] 18-field overlap FY22-FY23 = 2115  (expect 2,115)
[claude] 18-field overlap FY22-FY24 = 604  (expect 604)
[claude] 18-field overlap FY23-FY24 = 1002  (expect 1,002)
[claude] all-field pairwise overlap TOTAL = 0  (expect 0)
[claude]   all-field FY22-FY23 = 0
[claude]   all-field FY22-FY24 = 0
[claude]   all-field FY23-FY24 = 0
[claude] (guard) 18-field THREE-WAY intersection = 265  (NOT the reported metric)
[claude] pre-2024 award face share = 91.6876%  (expect ~91.7%)
```

**Confirmed independently:**

| Quantity | Required | My independent value | Match |
|---|---|---|---|
| Total rows | 37,988 | 37,988 | ✓ |
| FY2024 face | $65.19B | $65,189,755,228.64 | ✓ |
| FY2024 annual expenditure | $8.17B | $8,170,228,558.54 | ✓ |
| FY2024 MWBE count % | 18.73 | 18.7345 | ✓ |
| FY2024 MWBE face % | 3.95 | 3.9532 | ✓ |
| FY2024 MWBE expenditure % | 7.06 | 7.0612 | ✓ |
| FY2024 top-10 face conc | 30.42 | 30.4151 | ✓ |
| Vendor Gini (face) | ~0.931 | 0.93117 (both formulas) | ✓ |
| Vendor Gini (annual expenditure) | ~0.904 | 0.90435 (both formulas) | ✓ |
| 18-field pairwise overlaps | 2,115 / 604 / 1,002 | 2,115 / 604 / 1,002 | ✓ |
| All-field pairwise overlap | 0 | 0 | ✓ |

**Method fidelity notes (my angle):**
- **Gini method** exactly per fixed spec: `contract_amount` aggregated to one positive total per distinct `vendor_name`, null/zero/negative dropped, Gini computed over positive vendor totals. Two independent formulas agree to 5 decimals (0.93117), which rules out a formula-artifact and reproduces the FY2024 face Gini ~0.931 and the annual-expenditure Gini ~0.904. There are 2,656 distinct positive-face vendors and no negative amounts.
- **Fingerprint method** exactly per fixed spec: **three pairwise** overlaps (FY22-FY23, FY22-FY24, FY23-FY24) on **18 fields** (all non-computed fields except `fiscal_year_end_date`, `amount_expended_for_fiscal_year`, `amount_expended_to_date`, `current_or_outstanding_balance`). I explicitly did **not** use a three-way intersection or an identity subset. As a guard I additionally computed the three-way 18-field intersection (**265**) and the 5-field identity-subset variant to demonstrate they are *different* metrics; the R5 note that Gemini's divergent triplet came from mixing three-way/pairwise and a different denominator is consistent with what I observe (the correct pairwise-18 method uniquely yields 2,115/604/1,002).

**Step 4 PASS.**

---

## Step 5 — Provenance reconciliation (live SoQL, unedited)

**Query A — `gpsc-qqsz` FY2024 count + face sum:**
```
URL: https://data.ny.gov/resource/gpsc-qqsz.json?$select=count(1) as cnt,sum(contract_amount) as face&$where=fiscal_year_end_date='2024-12-31T00:00:00.000'
[{"cnt":"13718","face":"65189755228.64"}]
```

**Query B — first-party `twsw-2mqa` FY2024 count + face sum:**
```
URL: https://data.ny.gov/resource/twsw-2mqa.json?$select=count(1) as cnt,sum(contract_amount) as face&$where=fiscal_year_end_date='2024-12-31T00:00:00.000'
[{"cnt":"13648","face":"65131682801.41"}]
```

**Divergence computation (unedited):**
```
Face-value divergence = 0.0891%   (artifact states ~0.089%)
Record-count divergence = 0.5103%  (70 records; artifact states ~0.51%)
VERDICT: face ~0.089%  -> CONFIRMED
VERDICT: count ~0.51%  -> CONFIRMED
```

**Confirmed:** `gpsc-qqsz` = 13,718 / $65,189,755,228.64 (expected 13,718 / $65.19B); `twsw-2mqa` = 13,648 / $65,131,682,801.41 (expected 13,648 / $65.13B). The artifact separately states a **~0.089%** face divergence and a **~0.51%** (70-record) count divergence rather than collapsing both under a single sub-0.1% label — the exact correction absorbed as **F-AA-R5-C-03**. **Step 5 PASS.**

---

## Step 6 — Capital join (live, unedited)

Schema evidence:
- `wcsa-vkhf` fields include `project_number`, `latitude`, `longitude`, `georeference`, `location_indicator` — **no borough/county/boro key.**
- `kizb-nxtu` uses `project_number`.
- `ehz8-ag3n` uses `proj_num` (the column-name divergence recorded as F-AA-2).

Batch join output:
```
[claude] wcsa-vkhf project_number batch size = 120
[claude] kizb-nxtu: 120/120 batch project_numbers matched (distinct matched=120)
[claude] ehz8-ag3n: 120/120 batch project_numbers matched (distinct matched=120)
[claude] wcsa-vkhf non-computed fields: ['agency_name', 'capital_plan', 'category_description', 'element_description', 'georeference', 'latitude', 'location', 'location_indicator', 'longitude', 'plan_series', 'project_description', 'project_number', 'project_number_sequence']
[claude] wcsa-vkhf borough-like fields = []  (expect NONE)
[claude] worked example project D501CB08: kizb-nxtu rows found = 5
[claude]   sample allocation: total_allocation=48845 desc=Deck and Structural Rehabilitation - Cross Bay Bri
```

**Confirmed:** batching 120 distinct `wcsa-vkhf` `project_number` values yields **120/120** matches against `kizb-nxtu.project_number` and **120/120** against `ehz8-ag3n.proj_num`; `wcsa-vkhf` carries **no borough key**; a worked example (`D501CB08`) resolves to a real `kizb-nxtu` allocation ($48,845, Cross Bay Bridge deck rehabilitation). This corroborates Section 3's claim that borough attribution requires a project-number join followed by a coordinate-to-boundary spatial join (deferred GIS step). **Step 6 PASS.**

---

## Step 7 — Adversarial mutation (unedited)

I copied the snapshot **in memory** (original file never modified), altered **one non-MWBE** FY2024 `contract_amount` (+$5B), and ran the artifact's own comparator (`compare`) against the frozen baseline.

```
[claude] target vendor (non-MWBE) = 22ND CENTURY TECHNOLOGIES, INC
[claude] mwbe flag = 'N'  (confirm non-MWBE)
[claude] mutated contract_amount: 4,500,000.00 -> 5,004,500,000.00

[claude] comparator mismatches flagged = 8
   2024.face_total: frozen=65189755228.6400 vs mutated_copy=70189755228.6400 (tol 6.51898e+06)
   2024.mwbe_face_pct: frozen=3.9532 vs mutated_copy=3.6716 (tol 0.05)
   conc_face.top10: frozen=30.4151 vs mutated_copy=34.1517 (tol 0.05)
   conc_face.top20: frozen=41.7769 vs mutated_copy=45.0740 (tol 0.05)
   conc_face.top5: frozen=22.1434 vs mutated_copy=25.2377 (tol 0.05)
   pre2024_face_share: frozen=91.6876 vs mutated_copy=92.2797 (tol 0.05)
   proc_face_pct.Authority Contract - Competitive Bid: frozen=92.2197 vs mutated_copy=92.7739 (tol 0.05)
   proc_face_pct.Authority Contract - Non-Competitive Bid: frozen=7.7803 vs mutated_copy=7.2261 (tol 0.05)

[claude] ADVERSARIAL EXIT CODE = 2  (expect nonzero == drift flagged)
EXIT_CODE=2
```

Original snapshot integrity after the test:
```
hash still matches manifest: True
```

**Confirmed:** a single-cell non-MWBE mutation triggers the comparator to flag **8 downstream statistics** and return **nonzero exit code 2**. Note that even though the mutated vendor is non-MWBE, the MWBE face **percentage** correctly moves (denominator effect), which is the desired sensitivity. The original snapshot hash is unchanged. **Step 7 PASS.**

---

## Scope audit (executed outputs against required scope)

- **Estimand and stock/flow integrity.** Face is a **stock** ($65.19B, $8.17B annual flow named separately); **91.69%** pre-2024 confirmed (my value 91.6876%); vintages are treated as overlapping repeated observations and never summed. The abstract's ratios (4.7 face, 2.7 expenditure) reconcile to my computed 4.74 / 2.65. **Consistent.**
- **MWBE framing.** Descriptive prime-vendor with full limitations (indirect/subcontract, eligible-spend denominator, contract-specific goals, waivers). A term scan confirms "operative substrate", "short measure", "honest measure", "four cents", and "pass" survive **only inside explicit negations/withdrawals** — no live goal-attainment/operative-substrate/short-measure/pass claim. **Consistent.**
- **Concentration.** Presented as the sole **non-culpable structural** explanation for the count-vs-dollar asymmetry; the Tier-3 steering inference is explicitly refused. **Consistent.**
- **Fingerprint prose.** Section 4.0 states the exact **18-field** method (all fields except the fiscal-year and three annual-state fields), names identity fields only as examples, and explicitly flags that the enumerated-only reading is not the method used. My independent run reproduces 2,115/604/1,002 **only** under the 18-field method. **Consistent (F-AA-R3-03 holds).**
- **Provenance split (F-AA-R5-C-03).** Face ~0.089% and count ~0.51% (70 records) stated separately. **Consistent.**
- **Single ZERO convergence counter (F-AA-R5-C-02).** Reader Sections 6/7 carry only the single ZERO counter; the "one of two on the letter" phrase appears in the companion **only** in the withdrawal, the bracketed-superseded R4 conclusion, and the F-AA-R5-C-02 finding text. **No live dual-counter language.** **Consistent.**
- **Section 8 package statement (F-AA-R5-C-01).** Accurately states the package must be handed directly, its DOI is pending, and cited Zenodo DOIs are related works — and the package **is** present in this packet. Producer-side of C-01 discharged; DOI deposit remains the owner's OPEN action. **Consistent.**
- **Cross-artifact v0.5 consistency.** Reader header/abstract/Sections 6-7 and companion Current State all reflect v0.5. **Companion header is NOT fully consistent** — see F-AA-R6-01 below.

---

## Regression check of prior findings

| Finding | Disposition audited | Status now |
|---|---|---|
| F-AA-1 (capital data queryable; missing borough key) | RESOLVED-BY-CORRECTION | Holds; join re-confirmed 120/120 (Step 6) |
| F-AA-2 (`proj_num` vs `project_number` divergence) | CARRIED | Holds; confirmed live |
| F-AA-R1-01 (stock/flow) | ABSORBED | Holds; 91.69% pre-2024 reproduced |
| F-AA-R1-02 (MWBE descriptive) | ABSORBED | Holds; no live overreach term |
| F-AA-R1-03 (composition ≠ compliance) | ABSORBED | Holds |
| F-AA-R1-04 (community view divergence) | ABSORBED | Holds; reconciled live (Step 5) |
| F-AA-R1-05 (37,988 not 111,879) | ABSORBED | Holds |
| F-AA-R1-06 (reporting-chain wording) | ABSORBED | Holds |
| F-AA-R1-07 (missing vs zero split 1,348/48) | ABSORBED | Holds; reproduced |
| F-AA-R1-08 (field-inventory abort) | ABSORBED | Holds; 22-field inventory validated |
| F-AA-R1-09 (live compares all stats) | ABSORBED | Holds; Step 3 exit 0 |
| F-AA-R2-01 (companion "operative substrate" removed) | ABSORBED | Holds (only in negation/history) |
| F-AA-R2-02 (`--live`/`--selftest` complete) | ABSORBED | Holds; 45 perturbations detected |
| F-AA-R2-03 (fingerprint zero all-field) | ABSORBED | Holds; all-field overlap = 0 |
| F-AA-R2-04 (falsifiability criterion) | ABSORBED | Holds |
| F-AA-R2-05 (Current State block) | ABSORBED | Holds |
| F-AA-R2-06 (both-measure concentration) | ABSORBED | Holds; expenditure Gini 0.904 reproduced |
| F-AA-R3-01 (version propagation, reader) | ABSORBED | Reader holds; **companion header regressed → F-AA-R6-01** |
| F-AA-R3-02 (companion header v-label) | ABSORBED | **Partial regression → F-AA-R6-01** |
| F-AA-R3-03 (18-field fingerprint prose) | ABSORBED | Holds |
| F-AA-R3-04 (sentence-boundary cosmetic) | ABSORBED | Holds |
| F-AA-R3-05 (INFO clean) | NOTED | Holds |
| F-AA-R4-01 / -02 (INFO) | NOTED | Holds |
| F-AA-R5-C-01 (package present + Section 8) | ABSORBED (deposit OPEN) | Producer-side holds; package present; DOI still OPEN |
| F-AA-R5-C-02 (single ZERO counter) | ABSORBED | Holds |
| F-AA-R5-C-03 (split divergences) | ABSORBED | Holds; reconfirmed live |
| F-AA-R5-C-04 (INFO) | NOTED | Holds |

No prior absorbed finding has substantively regressed **except** the version-propagation family (F-AA-R3-01/-02), which recurs at the companion header — reported as a new finding below.

---

## Findings (namespace F-AA-R6; six-element format)

### F-AA-R6-01 — MEDIUM — Companion header references a stale reader-note version (v0.4), recurring the propagation defect the standing rule forbids

- **Identifier:** F-AA-R6-01
- **Severity:** **MEDIUM**
- **Locus:** `Bayyinah_AllocationAsymmetry_AuditCompanion.md`, header **line 3**: *"Companion to: … (the reader-facing note, v0.4)."*
- **Substance (surface vs substrate):** The **surface** of the companion header states the reader-facing note is **v0.4**. The **substrate** is that the reader note is unambiguously **v0.5** (its line 7 reads *"Working draft v0.5"*), and the companion's own line 5 ("Mirrors note state v0.5") and its authoritative Current State block ("as of v0.5", "v0.5 reader note") both say v0.5. Thus the *same header* cites two different reader-note versions (v0.4 on line 3, v0.5 on line 5) — an internal contradiction. This is the **exact failure mode** the program's own standing rule (widened at F-AA-R3-01) was written to prevent: on any version bump, *every* self-referential version statement — reader header, abstract, limitations, provenance, **companion header**, companion Current State — must be updated in the same edit, and the version is "not considered bumped until all are consistent." This is now the **fourth** occurrence of the version-propagation-lag family (after F-AA-R2-05, F-AA-R3-01, F-AA-R3-02) and a partial regression of F-AA-R3-02, which specifically fixed the companion header to point at the then-current version. Evidence: `grep` of the companion header shows line 3 = v0.4 while line 5 and the Current State block = v0.5.
- **Disposition:** **OPEN (new; advisory).** Recommended remedy: change companion header line 3 to "the reader-facing note, v0.5" so the header is internally consistent and satisfies the standing rule. As my round is advisory-only, this finding does not by itself set the qualifying verdict, but a qualifying auditor encountering the same contradiction could reasonably rate it HIGH on the standing-rule-recurrence grounds the producer itself used for F-AA-R3-01; I rate it MEDIUM to match the severity the identical prior header-lag defect (F-AA-R3-02) received.
- **Cross-reference:** F-AA-R2-05, F-AA-R3-01, F-AA-R3-02 (same propagation family); companion Current State block; reader note line 7.

### F-AA-R6-02 — INFO — All principal figures, methods, and mandatory legs independently reproduced; no data-level or framing defect found

- **Identifier:** F-AA-R6-02
- **Severity:** **INFO**
- **Locus:** Reader note Sections 4.0–4.4, 6, 7, 8; companion Verification Status and Current State; reproduction package.
- **Substance (surface vs substrate):** Surface claims and substrate agree throughout the quantitative core. Independently (own code, live queries): total rows 37,988; FY2024 face $65,189,755,228.64 and annual expenditure $8,170,228,558.54; MWBE 18.7345 / 3.9532 / 7.0612%; top-10 face 30.4151%; face Gini 0.93117 (two formulas) and annual-expenditure Gini 0.90435; pre-2024 face share 91.6876%; missing/zero 1,348/48; 18-field pairwise overlaps 2,115/604/1,002; all-field overlap 0. `--selftest` detects all 45 perturbations; `--live` shows no drift (exit 0); the adversarial mutation is flagged (exit 2); the capital join resolves 120/120 through `project_number`/`proj_num` with `wcsa-vkhf` carrying no borough key; the two provenance datasets reconcile with correctly split divergences. MWBE framing is descriptive prime-vendor with limitations; concentration is a non-culpable structural explanation; no live overreach term survives.
- **Disposition:** **NOTED.** No action. Reproduction integrity is sound.
- **Cross-reference:** Steps 1–7 above; F-AA-R3-05, F-AA-R4-01/02, F-AA-R5-C-04 (prior clean-reproduction notes).

---

## Advisory closing statement

I executed all seven protocol steps with real, unedited outputs, plus independent recomputation and an independent adversarial angle. Every principal figure reproduces exactly; the method disciplines (named estimands, stock/flow, descriptive MWBE, non-culpable structural concentration, 18-field pairwise fingerprint, split provenance divergences, single ZERO convergence counter) are all upheld in the reader note. I found **one MEDIUM defect** — a stale reader-note version label in the companion header (F-AA-R6-01), a fourth recurrence of the version-propagation-lag family — and no data-level defect.

**My advisory verdict is PASS with one MEDIUM advisory finding, but this is ADVISORY-ONLY and cannot affect convergence.** As the producing lineage, I cannot discharge the independence gate. The single operational metric — the consecutive qualifying-PASS count — remains **ZERO**, and both required qualifying passes remain to be earned by non-producer families on the then-current artifact.

---

## Evidence artifacts (this session, in `/home/user/workspace/r6-claude-opus-4-8/`)

- `repro/reproduce_paper2.py`, `repro/snapshot/gpsc-qqsz_FY2022-2024.json`, `repro/snapshot/MANIFEST.json` (unzipped packet)
- `claude_independent_recompute.py` (Step 4, my own code)
- `capital_join.py` (Step 6)
- `adversarial_test.py` (Step 7)

## Web / live-data sources (URLs)

- `gpsc-qqsz` community view: https://data.ny.gov/resource/gpsc-qqsz.json
- `twsw-2mqa` first-party MTA dataset: https://data.ny.gov/resource/twsw-2mqa.json
- `wcsa-vkhf` capital locations: https://data.ny.gov/resource/wcsa-vkhf.json
- `kizb-nxtu` capital allocations: https://data.ny.gov/resource/kizb-nxtu.json
- `ehz8-ag3n` capital budget: https://data.ny.gov/resource/ehz8-ag3n.json

---

# Bismillah ir-Rahman ir-Rahim
