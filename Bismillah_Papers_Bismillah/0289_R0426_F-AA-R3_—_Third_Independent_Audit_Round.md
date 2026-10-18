# Bismillah ir-Rahman ir-Rahim

# R0426 -- F-AA-R3 — Third Independent Audit Round

**Chronological Index:** 289 of 995  
**Date:** 2026-07-19  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-AA-R3_claude_report.md  
**Source Format:** md  
**SHA-256:** `4608796e7ef222102dd716abdd0b128d56c0873357dc94f24dbafec4d7a50d91`  

---

## R0426 · F-AA-R3 — Third Independent Audit Round

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-AA-R3_claude_report.md
- source_format: md
- text_sha256: 4608796e7ef222102dd716abdd0b128d56c0873357dc94f24dbafec4d7a50d91

# F-AA-R3 — Third Independent Audit Round
## Bayyinah: Public-Ledger Allocation and Asymmetric-Measure Audits (v0.3)

**Auditor namespace:** F-AA-R3
**Audited artifact:** reader note `Bayyinah_AllocationAsymmetry_v0.3.md`; audit companion `Bayyinah_AllocationAsymmetry_AuditCompanion.md`; reproduction package v0.3 (frozen snapshot 37,988 rows, `MANIFEST.json`, `reproduce_paper2.py`).
**Date:** 2026-07-19.

---

## Independence attestation (read first)

I am **Claude (Anthropic)**. The producing lineage of this artifact is also Claude/Anthropic — the reader note is co-authored "with collaborative analytical assistance from Claude (Anthropic)." Under the brief's binding independence requirement, the auditor must be a **non-OpenAI lineage outside the Claude/Anthropic producing lineage** (e.g., Gemini) or a qualified human reviewer. **I do not satisfy the different-family requirement.** I share the producing lineage, so this round is, from an independence standpoint, the most conflicted of the three (more so than a third OpenAI-family stopgap round).

**Fresh context:** this was run in a clean session. I did not begin from the F-AA-R1/F-AA-R2 findings as a checklist. I read the companion's prior-round appendices only as historical context, then re-derived every statistic independently from the frozen snapshot and the live `data.ny.gov` endpoint. The fifteen prior findings were treated as a regression target to re-verify, not as settled.

**Consequence:** Even if this round had returned zero CRITICAL / zero HIGH, it would **not count toward convergence** because it fails the different-family requirement. A Claude-family round cannot discharge the gate the brief sets. The substantive technical work below is nevertheless valid and, notably, completes the two mandatory legs no prior auditor could finish.

---

## Verdict: NON-PASS

**0 CRITICAL, 1 HIGH, 2 MEDIUM, 1 LOW, 1 INFO.**

Under the convergence criterion (Audit Framework v3.0, Standing Rule 7), a HIGH-bearing round does not pass and resets the two-consecutive-passing-round count to zero. **The count remains zero.** This round is NON-PASS on substance (the HIGH finding), independent of the independence failure. It is not the first of the two consecutive passing rounds required; the artifact still requires two clean, properly-independent passing rounds.

**Does the complete artifact still claim anything its data, cited legal structure, or own implementation does not support?** The data, legal-framing, and implementation claims now hold: every Section-4 figure reproduces from the frozen snapshot and from a live pull; the reproduction script does what it documents (`--live` compares every published statistic, schema, and row count; `--selftest` perturbs and detects all 45 statistics plus schema); the cross-table capital join is functional; the community-view provenance and its divergence from the first-party dataset are accurately disclosed. The interpretive overreaches of v0.1 (face-value-as-annual-spending, MWBE-goal-attainment, competitive-composition-as-compliance-"pass") are all properly withdrawn. **However, the artifact still makes unsupported provenance/status claims about its own version and audit history** — the reader note's Section 7 self-describes as v0.2 and references only the first audit round, contradicting its own v0.3 header and the companion's authoritative Current State block (F-AA-R3-01).

---

## Mandatory legs — both completed this round

For the first time in the three-round history, both mandatory legs executed successfully:

- **Full live comparison (all three years).** `reproduce_paper2.py --live` re-pulled FY2022, FY2023, FY2024 from `data.ny.gov/resource/gpsc-qqsz.json` and compared every published statistic, the field inventory, and row counts against the frozen baseline. Result: **no drift**, exit 0. (Rounds 1 and 2 both hit DNS failures and did not complete this leg.)
- **Row-level capital-table join.** Functionally executed. `wcsa-vkhf` (locations) confirmed to carry **no borough key** — only `latitude`/`longitude`/`georeference`/`location_indicator`. A batch of 120 location `project_number` values matched **120/120** in `kizb-nxtu` (key `project_number`) and **120/120** in `ehz8-ag3n` (key `proj_num`, the name divergence recorded as F-AA-2). Worked example: `D701HH89` (Henry Hudson Bridge rehab) joins to a `kizb-nxtu` allocation ($92,827) and to `ehz8-ag3n` budgets ($100.4M current). This independently confirms the Section 3 capital-join claim and the deferral of the by-geography analysis.
- **Provenance reconciliation.** Live `gpsc-qqsz` FY2024 = 13,718 rows / $65.19B; first-party `twsw-2mqa` FY2024 = 13,648 rows / $65.13B (divergence <0.1%, disclosed in the note). FY2022 (12,156/$54.70B) and FY2023 (12,114/$63.57B) are **identical** across both datasets. Three-year count = 37,988, confirmed.
- **Adversarial perturbation.** A $1B tamper of one FY2024 `contract_amount` (a non-MWBE statistic) was flagged by `--live` (drift on 7 fields including `2024.face_total`, concentration, process shares, pre-2024 share; exit 2). The hash-integrity layer aborts ("snapshot hash mismatch") on any snapshot-byte tampering. The comparator flags all 35 non-MWBE numeric perturbations and all 45 statistics + schema in `--selftest`.

---

## Findings (six-element format)

### F-AA-R3-01 — HIGH
**Locus:** Reader note, Section 7 (line 87); corroborating staleness in Section 6 (line 83).
**Substance (surface vs substrate):** Section 7 states, in present tense and unannotated: *"This draft is v0.2, produced by absorbing a first independent cross-instance audit round (namespace F-AA-R1)… a fresh independent round on this v0.2 is required."* This self-description is false for a v0.3 artifact. It contradicts (a) the note's own header (line 7: *"Working draft v0.3 (second independent-audit absorption…)"*), and (b) the companion's authoritative Current State block (v0.3; two NON-PASS rounds F-AA-R1 and F-AA-R2 absorbed). Section 6 (line 83) likewise references only the *"first audit round."* The v0.3 / R2 absorption was propagated into the header and the companion's Current State block but **not into the reader note's own provenance and limitations sections**. Surface (stated convergence state: v0.2, one round absorbed) diverges from substrate (actual: v0.3, two rounds absorbed, count zero).
**Disposition:** Update Section 7 (and Section 6) to v0.3, reference both F-AA-R1 and F-AA-R2, and state the consecutive-pass count remains zero pending the next fresh, properly-independent round.
**Cross-reference:** Companion Current State block (lines 19–27); brief status-coherence checklist; this is the exact recurring failure mode the brief identifies — a correction applied in one part of the artifact not propagated to the others. More severe than the round-2 F-AA-R2-05 (which was companion status ambiguity); here the primary reader-facing note self-identifies as the wrong version with the wrong absorbed-round state.

### F-AA-R3-02 — MEDIUM
**Locus:** Companion header, lines 3 and 5.
**Substance (surface vs substrate):** Line 3 reads *"Companion to: … (the reader-facing note, v0.1)"* and line 5 reads *"Mirrors note state v0.2 (first independent-audit absorption; the round was a NON-PASS)."* These are present-tense status labels that are stale (the note is v0.3; second absorption; two NON-PASS rounds) and are **not annotated as superseded**, directly contradicting the companion's own authoritative Current State block (lines 19–27) two paragraphs below. This is a residual of the round-2 F-AA-R2-05 fix: the Current State block and in-place supersession annotations were added to Sections A–D, but the header lines were left un-annotated. Surface (header: v0.1/v0.2, first absorption) diverges from substrate (Current State block: v0.3, second absorption).
**Disposition:** Annotate lines 3 and 5 as superseded per Section 14.5, or update them to v0.3.
**Cross-reference:** F-AA-R2-05; brief status-coherence checklist ("stale present-tense status labels are marked superseded").

### F-AA-R3-03 — MEDIUM
**Locus:** Reader note, Section 4.0 (line 51).
**Substance (surface vs substrate):** The note reports pairwise vintage overlaps of 2,115 / 604 / 1,002 and describes the method as matching on *"stable contract-identity fields (vendor, procurement description, award process, award and term dates, and contract face value, excluding the fiscal-year and annual-state fields)."* Independent recompute: an exact all-field match yields **0** shared records across all three vintage pairs (confirmed — the fiscal-year and annual-state fields differ by construction). The published 2,115 / 604 / 1,002 reproduce **only** when matching on all 18 non-computed fields excluding the four fiscal-year/annual-state fields (`fiscal_year_end_date`, `amount_expended_for_fiscal_year`, `amount_expended_to_date`, `current_or_outstanding_balance`). They do **not** reproduce under the seven-field "contract-identity" enumeration the prose foregrounds — that set yields 3,674 / 690 / 1,892. The companion (F-AA-R2-03) frames the method as "excluding fiscal-year and expenditure/balance fields" (the 18-field reading, which reproduces), but the reader note's prose over-narrows it to seven fields. A second party following the reader note's enumerated field set would not reproduce the published numbers. Surface (prose method: 7 fields) diverges from substrate (computed method: 18 fields). The qualitative conclusion (vintages overlap, must not be summed) is unaffected.
**Disposition:** Align the reader note's prose with the companion's stated method — either describe the fingerprint as "all fields except the fiscal-year and annual-state fields" (the 18-field set that reproduces), or recompute and publish the seven-field overlaps (3,674 / 690 / 1,892).
**Cross-reference:** F-AA-R2-03; brief fingerprint checklist; companion Section A reproduction record. Note: the brief's literal fingerprint criterion ("overlaps appear only after excluding fiscal-year and annual-state fields") is satisfied under the 18-field reading; the defect is method-description reproducibility, not a failed fingerprint fix.

### F-AA-R3-04 — LOW
**Locus:** Reader note line 65; companion lines 27, 40, 91, 118.
**Substance (surface vs substrate):** The brief asks to confirm the phrase "operative substrate" (and "short measure," "honest measure") appears nowhere in the reader note or companion. The **operative-substrate reading is properly withdrawn as a current claim** everywhere — Section A's corroboration is corrected in place per F-AA-R2-01, and reader-note Section 4.2 explicitly disclaims it. However, the literal strings survive in: a reader-note negation (*"does not call the dollar share the 'operative substrate'"*), the companion's superseded-phrases list (line 27), a corrected-historical annotation (line 40), and the append-only findings ledger (lines 91, 118). Under Section 14.5, preserving superseded text with annotations is the prescribed method, so these appearances are methodology-compliant; they nonetheless technically conflict with the brief's literal "appears nowhere" instruction. F-AA-R2-01 (the round-2 HIGH) is substantively resolved. (Minor: companion line 40 has a sentence-boundary artifact from the in-place correction — *"…descriptive prime-vendor statistic only. and that a shared…"* — a drafting cosmetic, not a substantive defect.)
**Disposition:** No action required unless the brief's literal criterion is enforced; if so, reword the negation/ledger/superseded-list occurrences to avoid the quoted phrase.
**Cross-reference:** F-AA-R2-01; brief MWBE-framing checklist.

### F-AA-R3-05 — INFO
**Locus:** Whole artifact (reproduction package + live endpoints).
**Substance:** Both mandatory legs completed for the first time; all figures reproduce. `--live` across all three years: no drift (exit 0). Row-level capital join functional (120/120 in both `kizb-nxtu` and `ehz8-ag3n`; `proj_num` divergence confirmed; no borough key in `wcsa-vkhf`). Provenance reconciled (`gpsc-qqsz` vs `twsw-2mqa`, divergence <0.1%, disclosed; 37,988 confirmed). Adversarial perturbation of a non-MWBE statistic flagged by `--live` (exit 2); hash layer aborts on tampering; `--selftest` detects all 45 perturbations + schema. No negative `contract_amount` values (note's "no negative amounts" holds). Top-5 vendors match the note (Kawasaki Rail Car $6.46B, New Flyer $2.56B, construction JVs >$1.5B). No annual-flow/allocation language survives on the face-value stock; vintages are never summed in the script. MWBE framing (18.7/3.95/7.06 as descriptive prime-vendor statistics with prime-only/indirect/eligible-spend/waiver limitations) is consistent across reader note, companion, and script. The withdrawn "pass" / "substrate matches surface" does not survive as a current claim or as a falsifiability criterion.
**Disposition:** Informational; no defect.
**Cross-reference:** F-AA-R2-02 (script `--live` overclaim — fully resolved), F-AA-R1-09, F-AA-1/F-AA-2 (capital infrastructure — confirmed).

---

## Regression re-verification of prior findings

All fifteen prior findings (F-AA-1, F-AA-2, F-AA-R1-01…09, F-AA-R2-01…06) were re-derived independently. Status as of v0.3:

- **F-AA-1, F-AA-2** (capital infrastructure / column-name divergence): confirmed — `kizb-nxtu` and `ehz8-ag3n` are queryable and carry allocation dollars; `wcsa-vkhf` lacks a borough key; `ehz8-ag3n` keys on `proj_num`. Resolved/carried correctly.
- **F-AA-R1-01** (stock vs flow): resolved — two named estimands, stock/flow disclosure, repeat-reporting caveat, vintages not summed.
- **F-AA-R1-02 / F-AA-R2-01** (MWBE operative-substrate framing): substantively resolved as a current claim; literal-string residue logged as F-AA-R3-04 (LOW).
- **F-AA-R1-03 / F-AA-R2-04** (competitive "pass" / falsifiability criterion): resolved — no "pass" or compliance conclusion survives; Section C fourth criterion corrected.
- **F-AA-R1-04** (community-view provenance): resolved and independently re-verified this round.
- **F-AA-R1-05** (37,988 vs 111,879): resolved; 37,988 confirmed.
- **F-AA-R1-06** (common-schema legal chain): resolved.
- **F-AA-R1-07** (missing/zero split): resolved; 1,348 missing / 48 explicit-zero confirmed.
- **F-AA-R1-08** (field inventory): resolved; hash + 22-field inventory validated.
- **F-AA-R1-09 / F-AA-R2-02** (script `--live` coverage): fully resolved and adversarially verified this round.
- **F-AA-R2-03** (fingerprint): numerically resolved (2115/604/1002 reproduce under the 18-field reading; exact all-field = 0), but prose over-narrows the field set — logged as F-AA-R3-03 (MEDIUM).
- **F-AA-R2-05** (companion status coherence): partially resolved — Current State block added and Sections A–D annotated, but companion header lines 3/5 left un-annotated — logged as F-AA-R3-02 (MEDIUM).
- **F-AA-R2-06** (both-measures concentration): resolved — annual-expenditure concentration (16.9/26.2/37.6, Gini 0.904) added and reproduced.

---

## Bottom line

The artifact's **data, legal framing, and implementation are sound and now fully reproduced, including the two legs no prior auditor completed.** The NON-PASS turns on **provenance/status propagation**: the reader note's own Section 7 still calls itself v0.2 and references only the first audit round — the precise recurring failure mode this program exists to catch, committed again by the producer against its own artifact. Combined with the independence failure (Claude/Anthropic = producing lineage), this round cannot advance convergence. The artifact requires one further properly-independent (different-family, fresh-context) round that, together with a subsequent independent passing round, achieves the two consecutive passes needed — and that next round must also verify the F-AA-R3-01/02/03 defects are resolved.

---

# Bismillah ir-Rahman ir-Rahim
