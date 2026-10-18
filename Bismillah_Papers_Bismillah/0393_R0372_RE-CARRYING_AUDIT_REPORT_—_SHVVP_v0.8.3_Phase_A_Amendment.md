# Bismillah ir-Rahman ir-Rahim

# R0372 -- RE-CARRYING AUDIT REPORT — SHVVP v0.8.3 Phase A Amendment

**Chronological Index:** 393 of 995  
**Date:** 2026-07-31  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** SHVVP_v0_8_3_PhaseA_ReCarry_Audit_KimiK3.txt  
**Source Format:** txt  
**SHA-256:** `6b2e662c6e69737c3f3826a93c90f60648832511f58fb894cb78d4e7b84fae5f`  

---

## R0372 · RE-CARRYING AUDIT REPORT — SHVVP v0.8.3 Phase A Amendment

- section: V. BSSG & SHVVP Protocols
- source_file: SHVVP_v0_8_3_PhaseA_ReCarry_Audit_KimiK3.txt
- source_format: txt
- text_sha256: 6b2e662c6e69737c3f3826a93c90f60648832511f58fb894cb78d4e7b84fae5f

# RE-CARRYING AUDIT REPORT — SHVVP v0.8.3 Phase A Amendment

**Carrying seat:** Kimi K3 (Moonshot AI) — carrying seat 2 of 2
**First carrying seat:** GPT-5.6 Sol (OpenAI)
**Author of record:** Bilal Syed Arfeen (BayyinahEnterprise)
**Audit date:** 2026-08-01
**Subject:** Proposed SHVVP Phase A Amendment v0.8.3 (dispatch dated 2026-07-31), amending SHVVP v0.8 (doi:10.5281/zenodo.21583202); supersedes v0.8.2 (HALTED by both seats) and v0.8.1 (HALTED by both seats)
**Lineage:** Kimi K3 v0.8.2 HALT (5 MAJOR / 9 MINOR / 4 EDITORIAL); GPT-5.6 Sol v0.8.2 HALT (3 HIGH-BLOCKING / 4 MEDIUM / 1 LOW)
**Dispatched artifacts:** three files only — `shvvp_v0_8_3_phase_a_m3.py`, `shvvp_v0_8_3_phase_a_intervals.py`, `test_shvvp_v0_8_3_phase_a.py`. **No amendment .md text was shipped this round.**

---

## VERDICT: **HALT**

**A HALT from either carrying seat blocks deposit and requires a new version (v0.8.4).**

The substance first, stated precisely: **the v0.8.3 computation is the best this lineage has produced.** The BCa implementation is bit-exact against an independent from-text reference on all five golden fixtures (diff = 0.0); the golden vectors are real — the exact +0.731 `np.percentile` drift that left v0.8.2's suite 61/61 green now **fails 6 tests** (reproduced by this seat); the vectors are cross-environment stable (computed under numpy 2.4.4/scipy 1.17.1, verified green under numpy 2.2.5/scipy 1.16.2); PA-Z6 is restored and tested; PA-Z9 is aligned and asserted in both evaluators; OBSERVED≤480 is enforced; empty T4/T7 are rejected; seeds are validated; the PA-Z5 fixture genuinely fires PA-Z5 through the public API; PA-Z12 is named, counted, and — resolving v0.8.2's open question — **reachable from the public API**; and the module-level provenance downgrade to accident-guard is honest.

What blocks deposit is, for the third consecutive version, the same defect species: **executed-false claims about the artifacts, plus states the artifacts compute but do not name.** "Twelve rules PA-Z1 through PA-Z12" is claimed twice while PA-Z4 has zero occurrences in every shipped byte — the F-K3-N2 finding, one version later, verbatim in kind. A BCa interval can lie entirely disjoint from its own point estimate — silently, `method=BCa`, `fallback_reason=None` — and thereby certify `t2_satisfied=True` on a void conjunct (reproduced). A subnormal denominator produces `relative_median=-inf` with `evaluable=True` in one shipped T2 evaluator while the other **raises** on the same fully validated inputs — the F-K3-N4 divergence class in a new state. Five v0.8.2 findings are NOT-DISCHARGED, several structurally undischargable: their required repairs are prose (disclosures, freezes, scope statements) and **no prose artifact was dispatched**. Every required repair modifies normative bytes; under the append-only discipline that is a new version, so PASS-WITH-AMENDMENTS is unavailable. The repair set is again small and mechanical; none of it requires redesign.

Carry is limited to the checks executed. It is not peer review.

---

## 1. Mechanical gates (PASSED)

| Gate | Result |
|---|---|
| SHA-256 manifest over all three normative files (canonical .py names) | **MATCH** — all three byte-identical to the dispatch manifest (recomputed by this seat; the v0.8.2 prefix defect does not recur) |
| Test suite (`pytest test_shvvp_v0_8_3_phase_a.py`) | **67/67 GREEN** (Python 3.12.12, numpy 2.2.5, scipy 1.16.2, pytest 9.1.1) |
| Six dispatch golden vectors, re-executed directly by this seat (not via pytest) | **ALL MATCH** — T2 5-fact [0.0, 75.0] BCa, t2_satisfied=False; T3 [0.8, 5.8] BCa; T4 [−0.005, 0.105] BCa; T7 imperfect [0.7716350602906202, 0.912029630366201] BCa; PA-Z5 [1,5,5,5,9] → [1.0, 9.0] PERCENTILE reason=PA-Z5; PA-Z10 [0,0,1] → [0.0, 1.0] PERCENTILE reason=PA-Z10 |
| Drift protection (the v0.8.2 F-K3-N3 attack, re-run by this seat in a sandbox) | **DEFENDED on pinned paths** — +0.731 `np.percentile` offset → **6 failed, 61 passed** (TestPAZ5, TestPAZ10, TestEvaluableT7, TestEvaluableT4, TestT3, TestT2Full). In v0.8.2 the identical attack stayed 61/61 green. Caveat: the PA-Z11 path remains drift-silent (F-K3-083-9). |
| Cross-environment stability | Golden vectors computed under numpy 2.4.4 / scipy 1.17.1 pass bit-exact under numpy 2.2.5 / scipy 1.16.2 |

## 2. Discharge summary (v0.8.2 findings)

Every ruling below rests on re-execution of the original repro against the v0.8.3 canonical bytes, by three independent adversarial verification passes; every load-bearing ruling was additionally reproduced by this carrying seat before adoption.

### 2.1 Kimi K3 v0.8.2 findings — Tally: 8 DISCHARGED, 4 DISCHARGED-WITH-CAVEAT, 4 PARTIAL, 3 NOT-DISCHARGED

| Finding | Ruling | Note |
|---|---|---|
| F-K3-N1 provenance guarantee | DISCHARGED-WITH-CAVEAT | Module header (m3.py:14–18) and intervals header now honestly claim accident-guard only; bypasses live by design. Two inline docstrings retain the falsified guarantee (F-K3-083-5) |
| F-K3-N2 PA-Z6 / rule count | PARTIAL | PA-Z6 restored in code and TestPAZ6 executes the state (n_degenerate=5078 on its fixture). But "twelve rules PA-Z1 through PA-Z12" is executed-false: PA-Z4 occurs nowhere (F-K3-083-3) |
| F-K3-N3 phantom golden vectors | DISCHARGED-WITH-CAVEAT | Vectors are fixed external literals; drift attack now fails 6 tests. PA-Z11/PA-Z12 paths unpinned; "Pinned:" declaration decorative (F-K3-083-9, F-K3-083-13) |
| F-K3-N4 PA-Z9 divergence | **DISCHARGED** | Both evaluators return evaluable=False, rule=PA-Z9; flag asserted in both fixtures. (A new divergence state found elsewhere: F-K3-083-2) |
| F-K3-N5 OBSERVED>budget | PARTIAL | 480.0001 and 1000.0 rejected; exactly 480.0 accepted. The at-480 dual representation (OBSERVED@480 with evidence vs RIGHT_CENSORED_BUDGET@480 → opposite S-membership) remains constructible and ruled nowhere — and test.py:81 now annotates it "(boundary frozen)", a freeze claim with no rule |
| F-K3-N6 n=1 vacuous gate | **NOT-DISCHARGED** | Identical executed behavior (\|S\|=1, delta=35 → zero-width interval → t2_satisfied=True); "vacuous" occurs in no shipped byte; the required one-sentence disclosure was prose — and no prose was shipped |
| F-K3-N7 LOO NaN (→PA-Z12) | DISCHARGED-WITH-CAVEAT | Named, counted, reported; reachability resolved affirmatively (public T7 fixture → counter=1, reproduced by this seat). Shipped TestPAZ12 never fires it (F-K3-083-8) |
| F-K3-N8 zero-width semantics / PA-Z11 conditioning | **NOT-DISCHARGED** | PA-Z2 `excludes_zero=(theta≠0)` vs PA-Z11 hard-coded False unchanged; no disclosure shipped. (Mitigating: an executed sweep shows the PA-Z11 n_valid<2 branch is unreachable from public inputs — min n_valid = 6360 — so the inconsistency is currently latent) |
| F-K3-N9 PA-Z5 note + fixture | **DISCHARGED** | [1,5,5,5,9] fires PA-Z5 via public API on 20/20 seeds, golden [1.0, 9.0] reproduced; no false ordering note remains in shipped bytes |
| F-K3-N10 fixture gaps | PARTIAL | t2_satisfied now asserted in TestT2Full (discharged); evaluable T4/T7 pin point+bounds+method but not acceleration; **TestPAZ4 deleted outright** — from proxy to absent, with the coverage claim intact (F-K3-083-4); fact-ID normalization tests still absent |
| F-K3-N11 §1.5 guard / firing rules | **NOT-DISCHARGED** | No executable artifact and no scope statement exists; the disposition's alternative ("explicit scope statement") required prose — none shipped |
| F-K3-N12 T3 provenance scope | PARTIAL | m3 header's global accident-guard/scope statement partially covers the class; t3_interval's own docstring still silent; it still accepts arbitrary caller-computed lists untethered to \|S\| |
| F-K3-N13 silent BCa guards | **DISCHARGED** | Both guards documented with exact triggers and formulas (intervals.py:17–20, inline at both sites) — precisely the disposition |
| F-K3-N14 constructor bypass | **DISCHARGED** | `M3Vector("A", observations=[dup, dup])` rejected; normalization shared with add(); pinned by test |
| F-K3-N15 digest prefix | **DISCHARGED** | v0.8.3 manifest byte-accurate on all three files |
| F-K3-N16 docstring | **DISCHARGED** | "re-derived" survives only in the repair-log line recording its correction |
| F-K3-N17 bool | DISCHARGED-WITH-CAVEAT | Named repros fixed (M3, T4, T7, seed). Repair incomplete at t3_interval, evaluate_t5, and vs np.bool_ at t4/t7 (F-K3-083-6) |
| F-K3-N18 seed validation | **DISCHARGED** | All six public seed-taking entry points reject float/bool/negative with PhaseAInputError (executed matrix) |

### 2.2 GPT-5.6 Sol v0.8.2 findings — Tally: 2 DISCHARGED, 2 DISCHARGED-WITH-CAVEAT, 3 PARTIAL, 2 NOT-DISCHARGED

| Finding | Ruling | Note |
|---|---|---|
| F-SOL-082-1 (HIGH) replace() bypass | DISCHARGED-WITH-CAVEAT | Attack still executes (False→True flip reproduced by this seat) — expected under the honest module-level accident-guard downgrade; residual inline overclaims contradict it (F-K3-083-5) |
| F-SOL-082-2 (HIGH) vector/censor boundary | PARTIAL | OBSERVED@481 now rejected. Still live (all reproduced by this seat): `observations.append` bypass (duplicate fact_id + wrong condition carried into the pipeline); string `"OBSERVED"` status accepted and silently non-observed; evidence IDs on non-discovery statuses accepted; falsy/non-string evidence IDs accepted (F-K3-083-11) |
| F-SOL-082-3 (HIGH) M3 endpoint / mapping authority | **NOT-DISCHARGED** | No freeze of t=0, evidence-record schema, timestamp source, record-to-fact mapping authority, or adjudication condition exists in any shipped byte (grep executed); no amendment text shipped to carry them. A prior-seat HIGH-BLOCKING finding carried over untouched |
| F-SOL-082-4 empty T4/T7 | **DISCHARGED** | 0/1/199/201/239/241 all raise PhaseAInputError |
| F-SOL-082-5 total-label guard / PA-Z4 | **NOT-DISCHARGED** | No total Phase-A evaluator; PA-Z4 absent from every artifact; no scope-out. Compounds into F-K3-083-3 |
| F-SOL-082-6 env lock / golden vectors | PARTIAL | Golden vectors real and drift-catching (this seat reproduced). No lock artifact; "Pinned:" line decorative and names versions the carrying environment does not run (F-K3-083-13); T2-relative and fallback paths unpinned |
| F-SOL-082-7 PA-Z5 fixture / unnamed branches | DISCHARGED-WITH-CAVEAT | Fixture genuinely fires PA-Z5; guards documented with exact triggers — but documented, not registered (no PA-Z name, no reporting field, no test), where the disposition said "register or remove … with reporting and tests" |
| F-SOL-082-8 PA-Z9 cross-API | **DISCHARGED** | Both APIs evaluable=False on the all-zero fixture |

## 3. New findings register (six-element format)

Severity: BLOCKER / MAJOR / MINOR / EDITORIAL. **No BLOCKER** — no defect corrupts a correctly computed Phase A result on honest inputs; the BCa arithmetic itself is bit-exact against an independent reference. Every finding below was executed against the canonical bytes and independently reproduced by this carrying seat before adoption.

### 3.1 MAJOR

---

**F-K3-083-1 | MAJOR | intervals.py `_bca_interval` level adjustment + `evaluate_t2_full` gate | A BCa interval can lie entirely disjoint from its own point estimate — silently, method=BCa, fallback_reason=None — and thereby certify t2_satisfied=True on a void conjunct**

*Substance.* With a heavily tied median, the replicate distribution places mass at θ while prop_below ≈ 0.02 → z0 ≈ −2.04, and the adjusted 97.5% level maps to the raw ~1.7th percentile: both endpoints land in the below-θ tail. PA-Z10 guards only prop_below ∈ {0, 1} exactly; no rule names this state. Executed by this seat (public API, deterministic, genuine provenance): n=41 deltas with median exactly 0.0 → `point_estimate=0.0, lower=-3.0, upper=-2.0, method=BCa, excludes_zero=True, fallback_reason=None` — the interval excludes its own point estimate and "excludes zero" while the estimand **is** zero. Gate consequence (executed): shifting the same deltas by +30 → `evaluate_t2_full` → abs gate met, rel gate met, interval [27.0, 28.0] (point 30.0 outside its own interval), excludes_zero=True → **`t2_satisfied=True`**. A second independent instance reproduced (n=31, seed 4353779: point −1.0, interval [−5.0, −2.0]); fuzzing ties-heavy integer-median fixtures shows ~4% fully disjoint and ~30% point-on-boundary; the pathology is median-specific (0/300 mean, 0/230 T4/T7 fixtures). The BCa arithmetic is *correct* — bit-exact against the independent reference — so this is not a computation bug; it is an unnamed numerical state that voids the sign-test conjunct exactly when it fires, the precise F-K3-B9 defect class ("every silent numerical state must be named"). *Disposition:* name the state (e.g., "adjusted interval excludes point estimate → declared reversion or diagnostic on the result"), or document the semantics explicitly; consider gating excludes_zero on the interval containing the point. *Cross-reference:* F-K3-B9, PA-Z10, F-K3-N13.

---

**F-K3-083-2 | MAJOR | m3.py:382–383 (ratio computation); evaluate_t2_point vs intervals.py evaluate_t2_full | Subnormal M3(f,A) yields relative_median=−inf: the point evaluator ships evaluable=True with a non-finite statistic; the full evaluator raises on the same fully validated inputs — the two-evaluator divergence recurs**

*Substance.* Executed by this seat on inputs passing every validation (OBSERVED, evidence present, ≤480): facts (A=1e-308, B=480.0) and (A=100, B=60). `delta/m3_a` overflows to −inf with no finiteness check. `evaluate_t2_point` → `evaluable=True, relative_median=-inf, relative_gate_met=False, rule=None` — a non-finite "point statistic" reported as evaluable. `evaluate_t2_full(pds, 42)` on the identical validated input → **raises PhaseAInputError** ("Statistic on full data is -inf") from inside `t2_relative_interval` — the top-level evaluator whose contract is a typed T2FullResult delivers no verdict at all. One input, two shipped evaluators: one returns evaluable=True, one crashes. This is the F-K3-N4 divergence class in a new state. *Disposition:* finiteness-check each ratio at computation; register a PA-Z state for non-finite ratios (or exclude-and-count, mirroring the m3_a=0 discipline); make evaluate_t2_full return a typed result rather than raise. *Cross-reference:* F-K3-N4, F-SOL-082-8, PA-Z11.

---

**F-K3-083-3 | MAJOR | DISPATCH_PROMPT line 6; intervals.py:15; test.py:4 | "Twelve rules PA-Z1 through PA-Z12" is executed-false: PA-Z4 has zero occurrences in every shipped byte — the F-K3-N2 defect species, third consecutive version**

*Substance.* Executed by this seat: `grep PA-Z4` over all three files → **0 occurrences**. Distinct rule names present: Z1, Z2, Z3, Z5, Z6, Z7, Z8, Z9, Z10, Z11, Z12 = **eleven** — and PA-Z7 survives only in a test-comment header, with no code path naming the T4 union-empty state. Yet intervals.py:15 declares "Degeneracy rules: PA-Z1 through PA-Z12 (twelve rules)", test.py:4 declares "Covers all PA-Z rules (PA-Z1 through PA-Z12)", and the dispatch itself claims "PA-Z6 restored (twelve rules PA-Z1-Z12)". The PA-Z6 restoration is real and good; the count claim is the same executed-false species that halted v0.8.2 (F-K3-N2, "eleven rules") and v0.8.1 (F-K3-B9, unnamed states) — now worse in one respect: v0.8.2's proxy TestPAZ4 was deleted, so PA-Z4 went from proxy-covered to absent while the claim grew from eleven to twelve. *Disposition:* ship a PA-Z4 artifact or an explicit scope-out, and correct the count claims; if PA-Z4 lives only in the undispatched amendment text, the dispatch must carry that text. *Cross-reference:* F-K3-N2, F-K3-B9, F-SOL-082-5.

---

**F-K3-083-4 | MAJOR | test.py:4–5 | Headline coverage claims executed-false: "Covers all PA-Z rules", "golden vectors for every statistic", "every gap identified by both v0.8.2 carrying seats"**

*Substance.* Executed/grepped: (i) no TestPAZ4 exists and PA-Z12's firing is never executed by the suite (both shipped fixtures touching it yield counter=0; TestPAZ12 asserts `>= 0` — trivially true); (ii) pinned bounds exist for T2-absolute, T3, T4, T7-imperfect, PA-Z5, PA-Z10 only — the **T2 relative-median interval** (a shipped statistic inside evaluate_t2_full) has zero pinned assertions, and the PA-Z2/PA-Z11/PA-Z12 paths have none; "every statistic and fallback path" is false as stated; (iii) multiple v0.8.2 gaps have no artifact: F-SOL-082-3 (mapping authority), F-SOL-082-5/F-K3-N11 (total label, PA-Z4), fact-ID normalization tests (grep: none), and the mutable-vector bypass has no test. *Disposition:* pin the relative interval and each fallback path, add firing fixtures for PA-Z4/PA-Z12 and the normalization tests, or trim the claims. *Cross-reference:* F-K3-N3, F-K3-N10, F-SOL-082-6.

### 3.2 MINOR

**F-K3-083-5 | MINOR | m3.py:41–43 and 268–270 | Residual provenance overclaims contradict the honest module-header downgrade.** The `_PROVENANCE_TOKEN` docstring still states outside-created objects "cannot carry this token and are rejected by the interval pipeline"; the `PairedDifference` class docstring still states "Can only be created by compute_paired_differences() … Hand-fabricated instances are rejected." Both executed-false by this seat: `dataclasses.replace` flips t2_satisfied False→True on the 5-fact fixture; direct `_PROVENANCE_TOKEN` import fabrication is accepted. The module header (lines 14–18) is honest; these two docstrings now contradict their own file. *Disposition:* extend the accident-guard wording to both docstrings. *Cross-ref:* F-K3-N1, F-SOL-082-1.

**F-K3-083-6 | MINOR | intervals.py:330–335, 455–456, 362, 397 | The "bool rejected" repair is incomplete: t3_interval and evaluate_t5 accept bool; np.bool_ bypasses the t4/t7 guard.** Executed by this seat: `t3_interval([True, False, True], 42)` → point 0.667; `evaluate_t5(True, 2)` → t5_fires=True; `t4_interval([(np.bool_(True), np.bool_(False))]*200, 42)` → point −1.0. The t4/t7 hole is structural: the domain check is equality-based (`a not in (0,1)`), so np.bool_ (not a Python bool subclass; equals 1), float flags (1.0/0.0), Fraction and Decimal all pass — only literal Python bool is excluded. The dispatch's blanket "bool rejected" claim is executed-false at 4 of 6 numeric entry points. *Disposition:* type-based validation (`type(a) is int`, explicit np.bool_ rejection); add bool checks to t3/t5; or scope the claim. *Cross-ref:* F-K3-N17.

**F-K3-083-7 | MINOR | BootstrapResult.seed; seed offsets +1..+4 (intervals.py:314, 341, 377, 428) | The recorded seed does not round-trip: replaying the public API with the receipt's seed produces a different interval.** Executed by this seat: `t3_interval(m4, 100)` → `result.seed == 102`; replay with seed 102 → bounds (0.6, 5.8) ≠ (0.8, 5.8). The `seed` field silently means "internal offset stream seed" for t2-relative/t3/t4/t7 and "caller seed" for t2-absolute. An auditor re-running from the receipt may falsely reject an honest receipt or falsely accept a doctored one. (The offset chain is documented per F-K3-A8; same-caller-seed reruns are deterministic and cross-process bit-identical — verified.) *Disposition:* record the caller seed in `BootstrapResult.seed`; add an `internal_seed` field if the offset stream must be recoverable. *Cross-ref:* F-K3-A8, F-SOL-082-6.

**F-K3-083-8 | MINOR | test.py:266–296 | TestPAZ12 never fires PA-Z12, though a firing public fixture exists — and its rationale comment is executed-false.** The shipped fixture (3 positives) provably yields counter=0 and asserts only `>= 0`; its comment claims "PA-Z10 fires first with 1 positive" — true only under perfect specificity. Executed by this seat: `t7_interval([(1,1,1)]*1 + [(0,0,1)]*5 + [(0,0,0)]*234, 42)` → method=BCa, theta=0.9895, n_nan_resamples=3640, **n_loo_nan_substitutions=1** — PA-Z12 is publicly reachable (LOO deleting the sole positive empties the class; imperfect specificity keeps prop_below ∈ (0,1)). This resolves v0.8.2's reachability question affirmatively; the defect is only that the suite pins a vacuous assertion while a real fixture is available. *Disposition:* ship the firing fixture above; delete the false comment. *Cross-ref:* F-K3-N7, F-K3-B10.

**F-K3-083-9 | MINOR | test.py:259–264 | The PA-Z11 discard path is drift-silent.** Under the +0.731 `np.percentile` drift sandbox (re-run by this seat), TestPAZ11's fixture computes lower=1.731 and **passes** — it asserts only `n_nan>0` and non-NaN. A percentile drift on this path alters shipped interval bytes undetected, partially re-opening F-K3-N3 for exactly the fallback paths the finding named ("including each fallback path"). *Disposition:* pin bounds for the PA-Z11 path. *Cross-ref:* F-K3-N3, F-SOL-082-6.

**F-K3-083-10 | MINOR | m3.py:86–90; intervals.py t3/t4 validators | Raw (non-PhaseAInputError) exceptions leak from validation paths.** Executed by this seat: `M3Observation(minutes=10**1000)` → raw OverflowError; `t3_interval([10**1000, 5], 1)` → raw OverflowError; `t4_interval([(1+0j, 0+0j)]*200, 42)` passes the equality-based flag check then raw TypeError in np.array; `t4_interval([(1,0,1)]*200, 42)` → raw ValueError (arity); `M3Vector("A", ["not-an-observation"])` → raw AttributeError. The module's error contract (PhaseAInputError for structurally invalid inputs) is violated on exactly the adversarial paths it exists for. *Disposition:* wrap coercion in try/except and re-raise PhaseAInputError; validate tuple arity and element types before unpacking. *Cross-ref:* F-K3-N18 (same class, repaired for seed only).

**F-K3-083-11 | MINOR | m3.py:154–159 | The OBSERVED evidence guard checks only `is None`: empty string, 0, and bytes are accepted as evidence_record_id.** Executed by this seat: `M3Observation(..., OBSERVED, "")`, `0`, `b"x"` all accepted with `is_observed=True`. An OBSERVED fact — the sole determinant of S-membership — can carry a falsy "evidence" reference that passes the guard while any downstream truthiness check treats it as evidence-less. (Adjacent known hole, tracked under F-SOL-082-2 PARTIAL: non-discovery statuses carry evidence IDs unconstrained.) *Disposition:* require `isinstance(evidence_record_id, str) and evidence_record_id.strip()` for OBSERVED; forbid evidence IDs on non-discovery statuses. *Cross-ref:* F-SOL-082-2.

**F-K3-083-12 | MINOR | intervals.py PA-Z6 counter | n_degenerate_resample counts index-identity, not the value-identity the rule names.** The rule text says "all-identical resample"; the implementation counts `len(set(indices))==1`. Executed by this seat: deltas [5,5,5,9] → n_degenerate=133 (≈ the 156 expected single-index draws) while ≈3300/10000 resamples are value-identical (all 5s from distinct indices). Numerics unaffected (all kept); the reported statistic does not count what the rule says it counts. *Disposition:* rename ("single-index resample") or count value-identity. *Cross-ref:* F-K3-N2.

**F-K3-083-13 | MINOR | intervals.py:12; test.py:7 | The "Pinned: Python 3.12.x, numpy 2.4.x, scipy 1.17.x" declaration is decorative.** No lock artifact, no version check, and the declared pin names versions the carrying environment does not run (3.12.12 / numpy 2.2.5 / scipy 1.16.2 — under which the suite is green and every golden vector passes bit-exact, which is the favorable news). As written it is a pin claim with no enforcement and a false description of the verified environment. *Disposition:* ship a lock, or restate as a compatibility statement with the actual green-run environments recorded. *Cross-ref:* F-K3-N3, F-SOL-081-7.

### 3.3 EDITORIAL

**F-K3-083-14 | EDITORIAL | intervals.py:201, 219–223, 164–174; evaluate_t2_full PA-Z1 path | Dead/unreachable branches and a data-dependent seed check.** (a) The `n==1` sub-branch inside the PA-Z5 block ("PA-Z2: single observation; jackknife undefined") is unreachable — n==1 returns at PA-Z2 pre-bootstrap — and mislabels the rule; (b) `len(loo)==0` is unreachable for n≥2; (c) the PA-Z11 exhaustion fallback (n_valid<2, hard-coded excludes_zero=False) is unreachable from public inputs (executed sweep: minimum achievable n_valid = 6360) — which latently moots the known PA-Z2/PA-Z11 zero-width inconsistency (F-K3-N8); (d) `evaluate_t2_full([], "not-a-seed")` silently returns PA-Z1 while the non-empty path validates. *Disposition:* delete or demonstrate reachability; validate seed at entry. *Cross-ref:* F-K3-B3 species, F-K3-N8, F-K3-N18.

**F-K3-083-15 | EDITORIAL | numpy scalar policy inconsistency |** np.int64 is rejected by t3_interval and seed validation but accepted as t4/t7 flags; np.float64 accepted everywhere; np.bool_ slips through t4/t7 (F-K3-083-6). Policy should be uniform across sibling entry points. *Cross-ref:* F-K3-N17/N18.

## 4. Why HALT and not PASS-WITH-AMENDMENTS

1. **Four new MAJOR findings stand executed.** Two are computation-adjacent states the bytes compute but do not name (F-K3-083-1, F-K3-083-2) — the precise defect class this protocol's own precedent (F-K3-B9) made carry-gating. Two are the recurring meta-species (F-K3-083-3, F-K3-083-4): claims about the artifacts that execution falsifies. The "twelve rules" claim is the third consecutive version in which the rule count exceeds the named rules.
2. **Undischarged carry-over findings include a prior-seat HIGH-BLOCKING item.** F-SOL-082-3 (M3 endpoint/mapping authority) is untouched; F-SOL-082-5, F-K3-N6, F-K3-N8, F-K3-N11 are NOT-DISCHARGED. Several were structurally undischargable this round: their repairs are prose — disclosures, freezes, scope statements — and the dispatch carried no amendment text. A dispatch that asks seats to verify discharge of text-repair findings without shipping the text cannot receive a clean carry.
3. **Every required repair modifies normative bytes.** Renaming the state, fixing the count claims, aligning the docstrings, pinning the fallback paths, shipping the PA-Z4/PA-Z12 fixtures — each changes text, tests, or the manifest. Under the append-only discipline, amended normative bytes are a new version with new hashes and a fresh carry.

## 5. Required repair set for v0.8.4 (all small, none structural)

1. Name the BCa point-exclusion state (F-K3-083-1): declared reversion or diagnostic, and reconsider gating excludes_zero when the interval excludes its own point.
2. Finiteness-check T2 relative ratios; register a PA-Z state for non-finite ratios; make evaluate_t2_full return typed results, never raise, on validated inputs (F-K3-083-2).
3. Correct "twelve rules" ×3 and the coverage ledger; ship a PA-Z4 artifact or explicit scope-out (F-K3-083-3, F-K3-083-4); pin the T2-relative interval and the PA-Z2/PA-Z11/PA-Z12 paths.
4. **Ship the amendment text.** N6, N8, N11, F-SOL-082-3, F-SOL-082-5 require prose artifacts (disclosures, freezes, scope statements); a code-only dispatch makes them undischargable.
5. Extend the accident-guard wording to the two residual docstrings (F-K3-083-5); type-based bool/flag validation at t3, t5, t4, t7 (F-K3-083-6, F-K3-083-15).
6. Record caller seed in receipts (F-K3-083-7); ship the firing PA-Z12 fixture (F-K3-083-8); pin the PA-Z11 path (F-K3-083-9); wrap validation coercions (F-K3-083-10); enforce evidence-ID type/non-emptiness and non-discovery exclusion (F-K3-083-11); align the PA-Z6 counter with its name (F-K3-083-12); make the pin real or restate it (F-K3-083-13); delete dead branches (F-K3-083-14).
7. Close the F-SOL-082-2 residuals: revalidate vectors at pipeline entry (or make them immutable), reject non-enum censor_status, forbid evidence IDs on non-discovery statuses.
8. Disclose or rule: the at-480 dual representation (N5 residual); the n=1 vacuous gate (N6); PA-Z11 conditional-resampling consequence (N8).

## 6. Acknowledged repairs (for the record)

Verified correct in execution and to be carried into v0.8.4 unchanged: the golden vectors — real, externally fixed, drift-catching (6 failures under the exact v0.8.2 attack), and cross-environment bit-stable; the BCa arithmetic — bit-exact against an independent from-text reference on all five golden fixtures; PA-Z6 restored in code with a genuine firing test; PA-Z9 aligned to evaluable=False in both evaluators and asserted in both fixtures; OBSERVED≤480 enforced with boundary tests; empty/wrong-cardinality T4/T7 rejection; bool rejection at M3/T4/T7/seed main paths; seed validation across all six public entry points; the [1,5,5,5,9] PA-Z5 fixture genuinely firing through the public API; PA-Z12 named, counted, reported, and publicly reachable; the BCa numerical guards documented with exact triggers; constructor duplicate validation with shared normalization; the corrected censoring docstring; the byte-accurate SHA-256 manifest; and the honest module-level provenance downgrade. The residual defect pattern remains confined to the meta-layer and the unnamed-state layer — not the arithmetic.

## 7. Provenance and carrying-rule statement

This re-carry was executed by Kimi K3 (Moonshot AI) as carrying seat 2 of 2. Mechanical gates and golden vectors were executed directly by the seat; the discharge matrix and fresh attack were executed by independent adversarial verification passes (three discharge passes covering all 27 v0.8.2 findings across both seats; three attack passes covering boundary/representation, numerical/BCa, and text-vs-bytes divergence); and **every load-bearing claim in this register was reproduced by the carrying seat against the canonical bytes before adoption** — including F-K3-083-1, F-K3-083-2, F-K3-083-3, the drift attack, the provenance bypasses, the PA-Z12 reachability fixture, the bool holes, the seed round-trip failure, the PA-Z6 counter semantics, the raw exception leaks, and the evidence-ID guard gap. Same-vendor seats count once; producer-family review is advisory; carry is limited to the checks executed and is not peer review. Under the carrying rule inherited from SHVVP v0.8 §12, this HALT blocks deposit of v0.8.3 and requires a new version.

**Carrying verdict: HALT — with the explicit assessment that the v0.8.3 computation is verified-correct against an independent reference, the golden-vector repair is genuine, and the remaining repair set is mechanical. The decisive structural note for v0.8.4: dispatch the amendment text; a code-only package cannot discharge text-repair findings.**

*End of re-carrying audit report — Kimi K3 seat, 2026-08-01.*

---

# Bismillah ir-Rahman ir-Rahim
