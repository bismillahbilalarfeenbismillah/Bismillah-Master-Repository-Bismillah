# Bismillah ir-Rahman ir-Rahim

# R0368 -- RE-CARRYING AUDIT REPORT — SHVVP v0.8.2 Phase A Amendment

**Chronological Index:** 391 of 995  
**Date:** 2026-07-31  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** SHVVP_v0_8_2_PhaseA_ReCarry_Audit_KimiK3.txt  
**Source Format:** txt  
**SHA-256:** `d72ecdb18902780023f76225316400ae08d0db3981f340f25c1f3a7bc7b8e5c1`  

---

## R0368 · RE-CARRYING AUDIT REPORT — SHVVP v0.8.2 Phase A Amendment

- section: V. BSSG & SHVVP Protocols
- source_file: SHVVP_v0_8_2_PhaseA_ReCarry_Audit_KimiK3.txt
- source_format: txt
- text_sha256: d72ecdb18902780023f76225316400ae08d0db3981f340f25c1f3a7bc7b8e5c1

# RE-CARRYING AUDIT REPORT — SHVVP v0.8.2 Phase A Amendment

**Carrying seat:** Kimi K3 (Moonshot AI) — carrying seat 2 of 2
**First carrying seat:** GPT-5.6 Sol (OpenAI)
**Author of record:** Bilal Syed Arfeen (BayyinahEnterprise)
**Audit date:** 2026-07-31
**Subject:** Proposed SHVVP Phase A Amendment v0.8.2 (2026-07-31), amending SHVVP v0.8 (doi:10.5281/zenodo.21583202); supersedes v0.8.1 (HALTED by both seats, never deposited)
**Lineage:** Kimi K3 v0.8.1 HALT (3 BLOCKER / 14 MAJOR / 5 MINOR / 2 EDITORIAL); GPT-5.6 Sol v0.8.1 HALT (7 findings)

---

## VERDICT: **HALT** — narrow, near-the-line

**A HALT from either carrying seat blocks deposit and requires a new version (v0.8.3).**

This must be stated precisely, because the substance of v0.8.2 is good: **the FB-1 and FB-2 computability defects are genuinely resolved.** All three v0.8.1 BLOCKER classes are verifiably repaired in execution — the S-membership contradiction is closed under a single observed-shared rule (my own v0.8.1 divergence fixture now yields |S|=6 and a single lawful reading), the 2-D jackknife produces **bit-exact agreement with an independent from-text BCa reference** on both T4 and T7, z0-undefined and NaN-resample states are declared, counted, and named, T5's interval retirement is honestly recorded as SUBSTANTIVE (PA-A5), and the vacuous-A2 path to NOT-FALSIFIED is barred by an explicit guard (§1.5).

What blocks deposit is not the computation — it is that **the normative text once again makes executed-false claims about its own artifacts**, the same defect species that halted v0.8.1: a provenance guarantee that is bypassable in one line with the verdict flipped end-to-end; a degeneracy rule (PA-Z6) silently deleted while the text twice claims "eleven rules PA-Z1 through PA-Z11" and claims complete fixture coverage; golden-vector and drift-protection claims for which no golden vectors exist; a wrong SHA-256 prefix in the very identity table carrying seats are instructed to recompute; and two shipped T2 evaluators that disagree on PA-Z9 evaluability. Under the amendment's own rule — "a divergence between them is a defect" (§0.2) — and under the append-only discipline, every required repair modifies normative bytes (text, tests, or the identity table), which forces new hashes and a new version. PASS-WITH-AMENDMENTS is therefore unavailable: the amendments are themselves normative changes. The repair set is small and mechanical; none of it requires redesign. If executed honestly, v0.8.3 should carry quickly.

Carry is limited to the checks executed. It is not peer review.

---

## 1. Mechanical gates (PASSED)

| Gate | Result |
|---|---|
| SHA-256 manifest over all four normative files in canonical form | **MATCH** — all four identical to the dispatch manifest |
| Test suite (`pytest test_shvvp_v0_8_2_phase_a.py`) | **61/61 GREEN** (Python 3.12.12, numpy 2.2.5, scipy 1.16.2) |
| Amendment §6 identity table | **DEFECT** — intervals module recorded as `07338303...`; actual digest is `0733830d36...` (verified by re-hashing both shipped copies). See F-K3-N15. |

## 2. Discharge summary (v0.8.1 findings)

Full matrix verified by re-execution of every original repro against the v0.8.2 canonical bytes.

**Tally: 26 DISCHARGED (2 with caveats), 8 PARTIAL, 2 NOT-DISCHARGED.**

| v0.8.1 finding | Ruling | Note |
|---|---|---|
| F-K3-A1 S-membership contradiction | **DISCHARGED** | Observed-shared-only; two-readings test closed; \|S\|=6 vs 13 |
| F-K3-A2 censoring signs | PARTIAL | Analysis withdrawn in text; m3 docstring says "re-derived" (F-K3-N16) |
| F-K3-A3 M3-FIRST censored | **DISCHARGED** | Observed-only + typed NO_DISCOVERY; identity qualified |
| F-K3-A4 all-zero relative gate | PARTIAL | PA-Z9 registered, but the two evaluators disagree on `evaluable` (F-K3-N4) |
| F-K3-A5 BUDGET | **DISCHARGED** | FROZEN_BUDGET_MINUTES = 480.0, enforced |
| F-K3-A6 caller bypass | PARTIAL | Raw fabrication rejected; replace()/token-import bypass live (F-K3-N1) |
| F-K3-A7 relative-interval gating | **DISCHARGED** | "Reported but not gated" explicit; recorded as substantive decision |
| F-K3-A8 code-only numerical choices | **DISCHARGED** | Seed chain and offsets documented (§2.3); code declared sole normative |
| F-K3-A9 fact-ID normalization | **DISCHARGED** | Frozen (§1.6); case-sensitivity and stripping executed |
| F-K3-A10 t=0 / boundary | PARTIAL | t=0 frozen; OBSERVED>budget still accepted (F-K3-N5) |
| F-K3-B1 T7 crash | **DISCHARGED** | 240-item mixed-class runs; bit-exact vs independent reference |
| F-K3-B2 T4 fabricated acceleration | **DISCHARGED** | a = −0.0047 (was fabricated 0.1326); bit-exact vs reference |
| F-K3-B3 PA-Z5 unimplementable | **DISCHARGED** | Rewritten over sum_sq=0; reachable; cited in fallback_reason |
| F-K3-B4 silent z0 clamp | **DISCHARGED** | PA-Z10 declared percentile reversion; clamp removed |
| F-K3-B5 NaN resamples | **DISCHARGED** | PA-Z11 counted/discarded/reported; exhaustion path declared |
| F-K3-B6 denom==0 guard | **DISCHARGED** | Widened threshold; unreachable in 600-case search |
| F-K3-B7 cardinalities | **DISCHARGED** | 200/240 enforced; binary enforced (199/201/239/241 rejected) |
| F-K3-B8 executor uniqueness | PARTIAL | Sole-normative-code declaration made; golden vectors absent (F-K3-N3) |
| F-K3-B9 unnamed states | **NOT-DISCHARGED** | Regression: PA-Z6 vanished; false count/coverage claims (F-K3-N2) |
| F-K3-B10 fixture gaps | PARTIAL | Real fixtures added for Z5/Z7/Z9/Z10/Z11/evaluable T4/T7; TestPAZ4 still a proxy; no acceleration/bound assertions (F-K3-N10) |
| F-K3-B11 typo | **DISCHARGED** | |
| F-K3-C1 T5 silent drop | **DISCHARGED** | Declared SUBSTANTIVE with justification (§4, PA-A5) |
| F-K3-C2 vacuous A2 | **DISCHARGED** (caveat) | §1.5 guard bars NOT-FALSIFIED; no executable evaluator (F-K3-N11) |
| F-K3-C3 PA-Z7 | PARTIAL | Trigger corrected to union-empty; firing rules in no artifact (F-K3-N11) |
| F-K3-C4 scope header | **DISCHARGED** | "5.2, 5.3, and edge-state behavior of the Section 5.4 decision table" |
| F-K3-C5 identity overclaim | **DISCHARGED** | Qualified to non-censored inputs |
| F-K3-C6 n=1 vacuous gate | PARTIAL | Consequence still undisclosed (F-K3-N6) |
| F-K3-C7/C8 typo, citations | **DISCHARGED** | T5 quote verbatim; 0.67 threshold accurate |
| F-SOL-081-1..6 | DISCHARGED (5 caveated as above) | T5 declaration, jackknife, estimand, PA-Z5/z0, label rule, domains |
| F-SOL-081-7 environment lock / golden receipts | **NOT-DISCHARGED** | No pins, no lock, no golden vectors; claims false (F-K3-N3) |

## 3. New findings register (six-element format)

Severity: BLOCKER / MAJOR / MINOR / EDITORIAL. **No new BLOCKER** — no defect corrupts a correctly computed Phase A result on honest inputs. All findings were executed against the canonical bytes; each was independently reproduced by the carrying seat or by both verification passes.

### 3.1 MAJOR

---

**F-K3-N1 | MAJOR | m3.py lines 38, 234–257; amendment §5, PA-A8 | Provenance guarantee falsified — fabricated deltas flip the T2 verdict end-to-end**
*Substance.* §5 states "Only `compute_paired_differences()` can produce valid instances… Hand-fabricated PairedDifference objects are rejected." Executed: (i) `dataclasses.replace(real_pd, delta=40.0)` — the idiomatic copy API for frozen dataclasses — carries `_provenance` over; a fixture with legitimate deltas [10,12,8] gives `t2_satisfied=False`, the forged copy gives `t2_satisfied=True`; (ii) `_PROVENANCE_TOKEN` is a readable module attribute and `_provenance` is a declared init parameter — direct fabrication with the imported token is accepted; (iii) pickle round-trips carry the token. `secrets.token_hex` provides uniqueness, not secrecy; against an in-process caller there is no coherent boundary, so the token's honest function is accident-prevention. The defect is the *claim*: PA-A8 declares the caller-injection class structurally closed when it is not. *Disposition:* downgrade §5/PA-A8 to an accident-guard claim, or fuse compute-and-evaluate so deltas never cross a trust boundary. *Cross-reference:* F-K3-A6; BSSG raw-evidence discipline.

---

**F-K3-N2 | MAJOR | Amendment §0.2 item 4, §3 table, §6, §7 PA-A2; intervals.py lines 131–140 | PA-Z6 silently deleted; "eleven rules" and full-coverage claims false; unnamed-state regression**
*Substance.* §3's table lists ten rules (Z1–Z5, Z7–Z11); PA-Z6 (all-identical resample, "not discarded") has zero occurrences in text, code comments, or tests (grep executed). Yet §0.2 and PA-A2 twice claim "eleven degeneracy rules PA-Z1 through PA-Z11," and §6 claims the suite covers "every PA-Z rule (PA-Z1 through PA-Z11)" — no TestPAZ6 exists or can exist. The code still detects and counts exactly that state (`n_degenerate_resample`) with no rule naming it: a regression of the precise F-K3-B9 defect class, in the version whose docstring claims "All unnamed states registered." *Disposition:* restore the PA-Z6 row (or renumber and record the renumbering), correct both count claims and the §6 coverage ledger, add the fixture. *Cross-reference:* F-K3-B9, F-K3-B10.

---

**F-K3-N3 | MAJOR | intervals.py docstring lines 30–33; amendment §2.2; whole test file | Phantom golden vectors; no environment lock; F-SOL-081-7 NOT discharged**
*Substance.* §2.2 instructs a text-only reimplementer to "match the golden-vector outputs in the test suite"; the docstring claims "Version changes that alter bit-level PRNG streams or percentile interpolation will fail the golden-vector tests." Full-file read + grep: **no golden vectors exist** — the suite pins point estimates only; TestSeedReproducibility checks the code against itself. Executed proof of consequence: sandboxing the suite with a +0.731 drift in `np.percentile` moves every interval bound ([0.0, 75.0] → [0.731, 75.731]) and the suite **stays 61/61 green**. A dependency upgrade alters every shipped interval silently — exactly what the docstring declares impossible. No version pin or lock artifact exists. *Disposition:* ship golden-vector receipts (fixed inputs → fixed bounds, including each fallback path) and pin numpy/scipy, or delete both claims. *Cross-reference:* F-K3-B8, F-SOL-081-7, F-K3-A8.

---

**F-K3-N4 | MAJOR | m3.py `evaluate_t2_point` line 361 vs intervals.py `evaluate_t2_full` line 498; amendment §3 PA-Z9 | The two shipped T2 evaluators disagree on PA-Z9 evaluability**
*Substance.* Executed on the same all-zero-M3(f,A) fixture: `evaluate_t2_point` → `evaluable=True, rule="PA-Z9"`; `evaluate_t2_full` → `evaluable=False, rule="PA-Z9", t2_satisfied=None`; the text legislates "T2 overall NOT-EVALUABLE." Two normative evaluators reporting opposite evaluability for one named state is a §0.2 divergence. (Not verdict-exploitable: under PA-Z9 the absolute gate cannot pass.) The suite masks it — TestPAZ9 never asserts `evaluable`. *Disposition:* align `evaluate_t2_point` to `evaluable=False`; assert the flag in both paths' fixtures. *Cross-reference:* F-K3-A4.

---

**F-K3-N5 | MAJOR | m3.py `M3Observation.__post_init__` lines 124–152; amendment §1.1 | OBSERVED beyond budget accepted; the 480-minute boundary rule remains unfrozen**
*Substance.* Executed: OBSERVED with minutes = 480.0001 and minutes = 1000.0 both accepted — a "discovery" after session expiry, semantically impossible under the protocol, with no rule for whether it counts. At exactly 480.0, OBSERVED (with evidence id) and RIGHT_CENSORED_BUDGET are two constructible representations of the same minute with opposite S-membership, distinguished only by the caller's enum choice. The evidence-record→fact mapping authority also remains frozen nowhere. *Disposition:* enforce OBSERVED ⇒ minutes ≤ FROZEN_BUDGET_MINUTES; freeze the at-480 assignment rule and the mapping authority. *Cross-reference:* F-K3-A10, F-K3-A5.

### 3.2 MINOR

**F-K3-N6 | MINOR | Amendment §3 PA-Z2; intervals.py line 124 | n=1 vacuous-pass consequence undisclosed.** Executed: |S|=1, delta=35 → zero-width interval, `excludes_zero=(theta≠0)=True` → **T2 satisfied on a single observation**. PA-Z2 discloses "zero-width interval" but never that gate 3 thereby lapses to "point ≠ 0." *Disposition:* one sentence in PA-Z2's row, or bar T2-satisfied at |S|=1. *Cross-ref:* F-K3-C6.

**F-K3-N7 | MINOR | intervals.py lines 187–189 | LOO NaN silently replaced with theta — reachable, unnamed, unreported.** Executed via public `t7_interval` (1 positive among 240): removing the single positive makes the LOO statistic NaN; line 189 substitutes theta and the result is presented as clean BCa with `fallback_reason=None`. Inconsistent with PA-Z11's count/discard/report discipline for the same phenomenon one stage earlier. *Disposition:* name it and report a count. *Cross-ref:* PA-Z11, F-K3-B9.

**F-K3-N8 | MINOR | intervals.py lines 142–158 vs 115–125 | Zero-width gate semantics inconsistent; PA-Z11 conditioning undisclosed.** PA-Z2 (n=1) sets `excludes_zero=(theta≠0)`; PA-Z11 (n_valid<2) hard-codes `excludes_zero=False` — identical geometry, opposite gate verdicts. And with 36.4% of resamples discarded (executed), the reported interval is over resamples conditional on non-degeneracy — a consequence the table does not spell out. *Disposition:* unify zero-width semantics; expand PA-Z11 disclosure. *Cross-ref:* PA-Z2, PA-Z11.

**F-K3-N9 | MINOR | Amendment §3 post-table note; TestPAZ5 docstring | The PA-Z5 ordering rationale is mathematically false for the median — and TestPAZ5 never fires PA-Z5.** §3 claims that for mean and median, sum_sq=0 implies prop_below=0 so "PA-Z10 fires first." Executed counterexample through the public API with genuine provenance: deltas [1,5,5,5,9] → all LOO medians identical (sum_sq=0) yet bootstrap medians vary (prop_below=0.057, z0 valid) → PA-Z5 fires, reproduced 20/20 seeds. True for the mean, false for the median. Positively: PA-Z5 is live, correctly named public code — but its shipped fixture fires PA-Z10 instead. *Disposition:* correct the note and docstring; add the public-API fixture. *Cross-ref:* F-K3-B3.

**F-K3-N10 | MINOR | Test file lines 306–375, 489–532; amendment §6 | Fixture independence gaps persist.** TestPAZ4 remains a proxy (exercises T5 NaN rejection; no alpha-undefined artifact exists); the evaluable T4/T7 fixtures assert point estimates and non-NaN only — zero pinned acceleration or bound values, short of F-SOL-081-2's required "independently verify point estimates, acceleration, bounds"; TestT2Full never asserts `t2_satisfied` (at the shipped seed the 5-fact reference verdict is actually False, unchecked); §6 claims a fact-ID-normalization test that does not exist (grep executed). *Disposition:* add reference-valued assertions and the missing fixtures, or trim §6. *Cross-ref:* F-K3-B10, F-SOL-081-2.

**F-K3-N11 | MINOR | Amendment §1.5, §3 PA-Z7; code (absent) | The §1.5 guard and the T3/T4/T7 firing rules have no executable artifact and no test.** The headline new construction-evaluability guard exists only as prose; likewise PA-Z7 quotes T4's firing rule correctly but no evaluator implements "point > +0.05 AND interval LB > 0" (nor T3's or T7's clause logic). Neither is scoped out. *Disposition:* ship an executable guard/firing evaluator with fixtures, or add an explicit scope statement. *Cross-ref:* F-K3-C2, F-K3-C3.

**F-K3-N12 | MINOR | intervals.py lines 296–315; amendment §5 | The provenance discipline covers only T2.** `t3_interval` accepts any caller-supplied list of caller-computed M4 differences — any length, no tie to |S|, no provenance — the same derived-fact injection class PA-A8 claims to exclude. §5's "the evaluator accepts raw M3 vectors and recomputes everything" is true only for T2. *Disposition:* state the scope honestly or extend raw-input recompute to T3. *Cross-ref:* F-K3-N1.

**F-K3-N13 | MINOR | intervals.py lines 222–228 | Silent numerical guards not in §2.4.** `abs(denom) < 1e-15 → return 0.5` is a silent clamp of the BCa correction — the same *class* of silent-clamp defect v0.8.1 was halted over — and the p_low/p_high clamping to [0.5/n_valid, 1−0.5/n_valid] is absent from the text. Latent (no public-API input reaches it in adversarial search), but unregistered. *Disposition:* register or delete; document the clamping. *Cross-ref:* F-K3-B4.

**F-K3-N14 | MINOR | m3.py lines 164–183 | `M3Vector` constructor bypasses `add()` validation.** Executed: `M3Vector("A", observations=[dup, dup])` accepts duplicate fact_ids; `get()` silently returns the first. The frozen duplicate-rejection rule holds only on the `add()` path. *Disposition:* validate in `__post_init__`. *Cross-ref:* §2.6 spirit.

### 3.3 EDITORIAL

**F-K3-N15 | EDITORIAL (verified by the carrying seat) | Amendment §6 table, line 196 | Wrong SHA-256 prefix for the intervals module.** Recorded `07338303...`; actual `0733830d36...` — re-hashed on both shipped copies. §8 step 2 instructs carrying seats to "recompute SHA-256 identity"; a prefix-checking seat HALTs on a transcription error. The same row repeats the "PA-Z1 through PA-Z11" miscount. *Disposition:* correct the digest. *Cross-ref:* F-K3-N2.

**F-K3-N16 | EDITORIAL | m3.py docstring line 8 vs amendment §1.3 | Incompatible characterizations of F-K3-A2's disposition.** Docstring: "Censoring signs corrected; conservatism re-derived." Text: the analysis "is withdrawn … and unnecessary." Both cannot be true. *Disposition:* fix the docstring. *Cross-ref:* F-K3-A2.

**F-K3-N17 | EDITORIAL | m3.py line 74; intervals.py lines 337, 370 | bool accepted as numeric input.** Executed: `minutes=True` accepted as an M3 value; `t4_interval([(True, False)]*200)` accepted (point −1.0). *Disposition:* reject `isinstance(v, bool)`. *Cross-ref:* §2.6.

**F-K3-N18 | EDITORIAL | intervals.py `_bca_interval` seed parameter | Seed input unvalidated.** Executed: seed=1.5 raises a raw `TypeError`, not PhaseAInputError; seed=−1 silently accepted. *Disposition:* validate at pipeline entry. *Cross-ref:* F-K3-B9.

## 4. Why HALT and not PASS-WITH-AMENDMENTS

Three reasons, stated for the record:

1. **The undischarged carry-over findings are carry-gating by the other seat's own standard.** F-SOL-081-7 (environment lock + golden receipts) was ruled "MUST AMEND BEFORE RE-CARRY" and is not discharged; F-K3-B9 (unnamed states) is not discharged — it *regressed* (PA-Z6 deleted, state still live in code, unnamed).
2. **Every required repair modifies normative bytes.** Correcting the rule count, restoring PA-Z6, adding golden vectors, fixing §5's claim, aligning the PA-Z9 flag, bounding OBSERVED, correcting the §6 digest — each changes the amendment text, the test suite, or the identity table. Under the append-only discipline, amended normative bytes are a new version with new hashes and a fresh carry; "PASS-WITH-AMENDMENTS" cannot attach to edits of the very artifacts being carried.
3. **The amendment's own acceptance rule compels it.** §0.2: "A divergence between them is a defect." Five MAJOR and fourteen lesser divergences between what the text claims and what the bytes do stand executed. A carrying seat that passed this package would be applying a weaker standard to v0.8.2 than both seats applied to v0.8.1.

## 5. Required repair set for v0.8.3 (all small, none structural)

1. §5/PA-A8: downgrade the provenance claim to accident-guard, or fuse compute-and-evaluate (F-K3-N1); state T3's scope honestly (F-K3-N12).
2. Restore PA-Z6 (or renumber with a recorded note); correct "eleven rules" ×2 and the §6 coverage ledger; add TestPAZ6 (F-K3-N2).
3. Ship golden-vector receipts for every statistic and fallback path; pin numpy/scipy versions; or delete the golden-vector/pinning claims (F-K3-N3).
4. Align `evaluate_t2_point` to `evaluable=False` under PA-Z9; assert the flag in fixtures (F-K3-N4).
5. Enforce OBSERVED ≤ FROZEN_BUDGET_MINUTES; freeze the at-480 rule (F-K3-N5).
6. One-sentence disclosures: PA-Z2 vacuous gate at n=1 (N6); PA-Z11 conditional-resampling consequence + unified zero-width semantics (N8); PA-Z5 median counterexample note (N9); name the LOO-NaN substitution (N7); register or delete the silent numerical guards (N13).
7. Fixtures: public-API PA-Z5 firing fixture; pinned acceleration/bound assertions for evaluable T4/T7; `t2_satisfied` assertion in TestT2Full; fact-ID normalization tests; a real PA-Z4 artifact or an explicit scope-out (N9, N10).
8. Executable artifact (or explicit scope-out) for the §1.5 guard and T3/T4/T7 firing rules (N11).
9. Editorials: §6 digest (N15), m3 docstring line (N16), bool rejection (N17), seed validation (N18), `M3Vector.__post_init__` validation (N14).

## 6. Acknowledged repairs (for the record)

The following are verified correct in execution and should be carried into v0.8.3 unchanged: the observed-shared S rule and single-reading T2 computation; the axis=0 2-D jackknife (bit-exact against an independent from-text BCa reference on T4 and T7); PA-Z10 declared z0 fallback (no clamp remains); PA-Z11 NaN count/discard/report; the PA-A5 T5 retirement with its declared justification; the §1.5 vacuous-A2 guard (as a rule — it needs an executable artifact, N11); FROZEN_BUDGET_MINUTES with censor-status invariant enforcement; cardinality and binary-domain enforcement; fact-ID normalization (as a rule — it needs tests, N10); the corrected scope header; the qualified M3-FIRST identity; and the honest amendment-record practice of PA-A1..PA-A11 in every place where the record describes the *text's* changes. The residual defect pattern is confined to the meta-layer: claims about the artifacts, not the artifacts' computations.

## 7. Provenance and carrying-rule statement

This re-carry was executed by Kimi K3 (Moonshot AI) as carrying seat 2 of 2. Mechanical gates were executed directly by the seat; the discharge matrix and fresh attack were executed by two independent adversarial verification passes, and every load-bearing claim in this register was reproduced by the carrying seat against the canonical bytes before adoption (including the headline discharges D1–D7, the provenance bypass, and the §6 digest error). Same-vendor seats count once; producer-family review is advisory; carry is limited to the checks executed and is not peer review. Under the carrying rule inherited from SHVVP v0.8 §12, this HALT blocks deposit of v0.8.2 and requires a new version.

**Carrying verdict: HALT — with the explicit assessment that FB-1 and FB-2 are substantively resolved and the remaining repair set is mechanical.**

*End of re-carrying audit report — Kimi K3 seat, 2026-07-31.*

---

# Bismillah ir-Rahman ir-Rahim
