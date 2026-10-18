# Bismillah ir-Rahman ir-Rahim

# R0367 -- CARRYING AUDIT REPORT — SHVVP v0.8.1 Phase A Amendment

**Chronological Index:** 375 of 995  
**Date:** 2026-07-30  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** SHVVP_v0_8_1_PhaseA_Carrying_Audit_KimiK3.txt  
**Source Format:** txt  
**SHA-256:** `569591aad5249ad9d98b2399197924941b802fb977251bbe5ee577ffafed684f`  

---

## R0367 · CARRYING AUDIT REPORT — SHVVP v0.8.1 Phase A Amendment

- section: V. BSSG & SHVVP Protocols
- source_file: SHVVP_v0_8_1_PhaseA_Carrying_Audit_KimiK3.txt
- source_format: txt
- text_sha256: 569591aad5249ad9d98b2399197924941b802fb977251bbe5ee577ffafed684f

# CARRYING AUDIT REPORT — SHVVP v0.8.1 Phase A Amendment

**Carrying seat:** Kimi K3 (Moonshot AI) — carrying seat 2 of 2
**First carrying seat:** GPT-5.6 Sol (OpenAI)
**Author of record:** Bilal Syed Arfeen (BayyinahEnterprise)
**Audit date:** 2026-07-31
**Subject:** Proposed SHVVP Phase A Amendment v0.8.1 (2026-07-30), amending SHVVP v0.8 (doi:10.5281/zenodo.21583202)
**Producer seat:** Claude Opus 4.6 (Anthropic) — advisory, non-carrying

---

## VERDICT: **HALT**

**A HALT from either carrying seat blocks deposit outright and requires a new version (v0.8.2).**

This carry executed the canonical bytes, verified the shipped identity manifest, ran the full adversarial test suite, and attacked the amendment along every dimension named in the dispatch (M3/T2 computability, interval-algorithm uniqueness, PA-Z exhaustiveness, censoring, BCa fallback, A2 interaction, inferential honesty, and the §5 no-change ledger). The mechanical gates pass cleanly; the substantive attack does not. Three independent BLOCKER findings and fourteen MAJOR findings stand, each reproduced by execution against the shipped canonical bytes.

Carry is limited to the checks executed. It is not peer review.

---

## 1. Mechanical gates (PASSED)

| Gate | Result |
|---|---|
| SHA-256 manifest recomputed over all four normative files in canonical (.md/.py) form | **MATCH** — all four hashes identical to the shipped manifest |
| Test suite execution (`pytest test_shvvp_v0_8_1_phase_a.py`) | **44/44 GREEN** (8.91s, Python 3.12.12, numpy 2.2.5, scipy 1.16.2) |

Note for the record: the 44/44 GREEN result is materially weaker than it appears. The suite never exercises the T7 interval on any evaluable input (F-K3-B1), never exercises the T4 jackknife on non-degenerate data (F-K3-B2), and lacks the PA-Z5 and PA-Z7 fixtures that amendment §4 makes a freeze precondition (F-K3-B10). The suite is green because it does not look where the defects are.

## 2. Headline defects (summary)

1. **FB-1 is reproduced, not resolved.** The amendment contradicts itself on whether a never-found fact enters the shared set S (§1.1 + §2.6 para 1 say yes, censored at budget; §1.3 + §2.6 paras 2–3 say no). The code silently implements the first reading. Executed on identical bytes, the two lawful readings produce **opposite T2 verdicts** — the exact defect the amendment exists to repair (F-K3-A1).
2. **The T7 interval crashes on every evaluable input** (`IndexError` from a 2-D jackknife flattening bug). The shipped canonical code cannot compute one of the five frozen intervals at all (F-K3-B1).
3. **The T4 interval's acceleration is silently fabricated** from single flag bits on every valid input — same root cause, masked by `np.atleast_2d` — and reported as a clean BCa result with no fallback disclosure (F-K3-B2).
4. **The §5 no-change ledger is falsified.** T5's "95 percent interval lower bound above 1.00" conjunct is silently dropped (code fires T5 on the ratio alone); the header "Amends … Sections 5.2 and 5.3 only" is contradicted by the amendment's own §5.4 decision-table freezes (F-K3-C1, F-K3-C4).
5. **FB-2's explicitly enumerated "handling of failed bootstrap resamples" remains unfrozen**, and NaN-emitting resamples silently poison intervals (F-K3-B5). Executor uniqueness fails empirically: same data + same seed → different intervals under two lawful readings of the text (F-K3-B8).

---

## 3. Findings register (six-element format)

Severity scale: BLOCKER (defeats the amendment's purpose; deposit must not proceed) / MAJOR (must be fixed and re-frozen before carrying) / MINOR (must be fixed; does not alone block) / EDITORIAL.

### 3.1 BLOCKER findings

---

**F-K3-A1 | BLOCKER | Amendment §1.1 (line 57), §1.3 (line 71), §2.6 (lines 145–147) vs `compute_shared_set` (m3.py lines 120–126) | Censoring contradiction — decision-changing, FB-1 reproduced**

*Substance.* Four normative statements conflict. §1.1: "If condition c **does not identify f at all**, M3(f,c) is RIGHT-CENSORED at the fixed wall-clock budget," with the vector domain "each … fact f in the sealed reference-standard ledger" (line 53) — unfound facts get censored entries in the vector. §1.3: S = "facts **found by both** conditions." §2.6 para 1: "A right-censored M3 observation (condition c **did not identify fact f within the budget**) **enters the paired difference**." §2.6 paras 2–3: "If A did not find fact f **at all**, f is **not in S** … Censoring applies **only when both conditions found the fact**." The code picks the §1.1/§2.6-para-1 reading silently: `compute_shared_set` intersects raw `fact_ids` with no censor-status filter, and `TestCensoring` hard-codes a never-found fact entering S. **Executed proof of divergence from identical bytes** (6 facts found by both, deltas +180…+205; 7 facts found by A only): text-reading executor → |S|=6, median 192.5, T2 satisfied = **True**; §1.1-literal executor (full-ledger vectors, as the code accepts) → |S|=13, median −380.0, T2 satisfied = **False**. A fact found by *neither* condition also entered S in code (delta = BUDGET − BUDGET = 0). This is the FB-1 defect — "two competent executors can lawfully compute different T2 results from the same bytes" (amendment line 26) — reproduced verbatim against v0.8.1.
*Disposition.* Pick one reading; rewrite §1.1's vector domain and §2.6 to match; make `compute_shared_set` enforce the chosen reading structurally; if censored-not-found facts are admitted to S, re-derive the conservatism claim (see F-K3-A2) and restate §1.3's "found by both."
*Cross-reference.* FB-1; v0.8 §5.3 T2; TestCensoring; F-K3-A2, F-K3-A5.

---

**F-K3-B1 | BLOCKER | intervals.py line 119 (`np.delete(data, i)`) + line 341 | T7 interval crashes on every evaluable input**

*Substance.* `_bca_interval`'s jackknife uses `np.delete(data, i)` with no `axis=` on 2-D data, which flattens to 1-D; `t7_interval`'s statistic then does `x[:, 0]` → `IndexError: too many indices for array`. Executed (independently by two seats of this audit): `t7_interval([(1,1,1)]*40 + [(0,0,0)]*200, seed=123)` — a well-formed 240-item discrimination set mirroring the frozen corpus — raises. The only t7 paths the test suite exercises are the PA-Z8 early-returns, so 44/44 GREEN ships with PA-3's T7 row unexecutable. Phase A cannot produce T7's interval; A6 ("T7 OR T8") is not executable as frozen.
*Disposition.* Fix the jackknife to delete rows (`np.delete(data, i, axis=0)`); add an evaluable-T7 fixture to the suite; re-freeze.
*Cross-reference.* FB-2; PA-1 (T7 resampling unit), PA-2 step 2, PA-3 T7 row, PA-Z8; F-K3-B10.

---

**F-K3-B2 | BLOCKER | intervals.py line 119 (root) manifesting at line 311 (`np.atleast_2d`) | T4 jackknife silently computed on garbage — fabricated acceleration reported as clean BCa**

*Substance.* Same flattening root cause as F-K3-B1, but `t4_interval`'s statistic wraps the flattened (2n−1,)-vector in `np.atleast_2d`, masking the crash. The "leave-one-out" statistic degenerates to the difference of two flag *bits*. Executed: `[(0,1)]*100 + [(1,0)]*60 + [(0,0)]*40` → point estimate correct (0.20) but jackknife values ∈ {−1, 0, 1}, yielding a fabricated acceleration a = 0.1326 and a BCa interval [0.100, 0.175] reported as `method=BCa, fallback_reason=None`. On other inputs (executed: 180×(0,0), 10×(1,0), 6×(0,1), 4×(1,1)) the corrupted jackknife yields sum_sq ≈ 0 and a spurious PERCENTILE fallback "0/200 degenerate." Every valid T4 input receives either a wrong acceleration with zero disclosure or a spurious fallback. Silent numerical corruption is worse than a crash: it produces authoritative-looking wrong intervals.
*Disposition.* Fix the 2-D jackknife; add non-degenerate T4 fixtures asserting both the acceleration path and correct bounds against a reference computation; re-freeze.
*Cross-reference.* FB-2; PA-2 step 2, PA-3 T4; amendment §4 ("text and code are the same rule written twice"); F-K3-B1.

### 3.2 MAJOR findings

---

**F-K3-C1 | MAJOR | Amendment §2.2 PA-1 table (line 108), §3 PA-Z3 (line 159), §5 bullet 5 (line 196), §7; v0.8 §5.3 T5; `evaluate_t5` (intervals.py lines 378–399); test file lines 268–278 | T5's interval conjunct silently dropped**

*Substance.* v0.8 T5 = "M7(B)/M7(A) greater than 1.25 **AND 95 percent interval lower bound above 1.00**." The amendment declares T5 "NOT BOOTSTRAPPED (see PA-Z3)" with no alternative construction and no PA-3 row; the code fires T5 on the ratio alone (`t5_fires = ratio > 1.25`); the tests codify the weakened gate. Dropping the conjunct changes T5's firing conditions (it fires strictly more often), disclosed nowhere: §5 states flatly "No threshold other than T2 … is changed" — affirmatively false — and §7's amendment record has no T5 entry, violating v0.8 §12 ("alters … a numeric threshold … a decision rule or its Boolean structure" = SUBSTANTIVE; "never a silent edit"). A defensible justification exists (v0.8's own inferential-honesty clause gives T5 no resampling unit; team pairs are never pooled) but the amendment never makes it. Justification-without-disclosure does not satisfy append-only discipline.
*Disposition.* Restore the T5 interval gate with a frozen construction, or record the change in §5 and §7 with explicit justification.
*Cross-reference.* F-K3-C4; v0.8 §5.3 T5, §12; XZ draft line 446.

---

**F-K3-C2 | MAJOR | Amendment §1.4 (line 87), §7 PA-A3 (line 222); v0.8 §5.4 | The "inherited priority order (NOT-EVALUABLE dominates)" does not exist in v0.8 — and the vacuous-A2 path yields NOT-FALSIFIED**

*Substance.* Exhaustive search of the parent instrument: no Phase A evaluability priority order exists ("NOT-EVALUABLE" appears only in Phase C §7.5 and route provisions). The inheritance claim is false. Tracing the frozen edge (IDC > 0, S empty): A1 false; A2 cannot fire; if A3–A6 are silent and M12 ≥ 0.80, then by v0.8's own formula — NOT-FALSIFIED(A) = (NOT FALSIFIED(A)) AND (M12 ≥ 0.80) AND (denominators complete), which contains **no evaluability conjunct** — Phase A yields **NOT-FALSIFIED on a shared-set comparison that never happened** (reproduced in execution). PA-A3 freezes the edge as "intended behavior … a data limitation, not a design gap" while leaving the favorable-label path intact: the NOT-EVALUABLE state is silently absorbed into a pass.
*Disposition.* Add an explicit Phase A edge-state label rule (e.g., NOT-FALSIFIED barred when A2's domain was entered vacuously) with an amendment-record entry; delete the false inheritance claim.
*Cross-reference.* F-K3-A1, F-K3-C4; v0.8 §5.4.

---

**F-K3-A2 | MAJOR | Amendment §2.6 para 1 (line 145); test file lines 351–365 | Both signs in the conservatism argument are inverted; "fail-safe for both arms" is false as coded**

*Substance.* Executed: A found / B not found → delta = 60 − 480 = **−420 (negative)**; the amendment says this "makes Delta-M3 **more positive**." B found / A not found → delta = 480 − 30 = **+450 (positive)**; the amendment says "large **negative**." Both sign statements in line 145 are wrong. The test name `test_censored_b_makes_delta_large_positive` asserts `delta < 0` — name contradicts body. Substantively, under the code's S-membership reading, A-censored/B-found facts *inflate* the median toward T2-satisfied (executed: 3 shared facts at +40 plus 4 B-only facts → median rises 40 → 430, gate met). The censoring direction is therefore **not** fail-safe for both arms under the code's reading.
*Disposition.* Correct the signs and re-argue conservatism after F-K3-A1's S-membership question is resolved; rename the test.
*Cross-reference.* FB-1; F-K3-A1; TestCensoring.

---

**F-K3-B3 | MAJOR | Amendment PA-Z5 (line 161) vs intervals.py lines 116–165 | PA-Z5 is unimplementable as written; the code implements a different, partly dead rule**

*Substance.* (a) PA-Z5 keys on "bootstrap **replicates** produc[ing] a degenerate jackknife," but the algorithm computes *one* jackknife on the full data — replicates have no jackknives; the conditioned quantity does not exist (the 5% rule was mis-ported from Phase B Z-2, where it keys on resample composition, a quantity that does exist). (b) The code's reinterpretation (`degen_frac = n_degenerate_jackknife / n`) is nonzero only when n = 1, which the earlier PA-Z2 branch already captures — the >5%→BC-only and >20%→percentile graduated branches are **unreachable on 100% of inputs** (static proof + dynamic confirmation). (c) The genuinely occurring state — zero third-moment denominator with n > 1 — goes straight to percentile, bypassing the BC-only tier, with a fallback_reason citing **no PA-Z rule** (executed: all-identical n=10 → PERCENTILE, "Jackknife sum of squares is zero (0/10 degenerate)"; [1,1,1,2] with median stat → same branch).
*Disposition.* Rewrite PA-Z5 in terms of a computable quantity; name and graduate the sum_sq == 0 branch per the rule, or amend the rule to match intended behavior; cite the rule in fallback_reason.
*Cross-reference.* FB-2; PA-Z2; v0.8 §6.5.1 Z-2; F-K3-B10.

---

**F-K3-B4 | MAJOR | intervals.py lines 107–113; amendment §3 | Silent z0 clamp where the parallel Phase B rule mandates a declared, counted fallback**

*Substance.* Executed: `t2_absolute_interval` on deltas [0,0,5] (theta = 0 = minimum ⇒ no replicate strictly below) gives prop_below == 0.0; the code silently substitutes z0 = norm.ppf(1/20000) ≈ −3.89 and reports `method=BCa, fallback_reason=None`. v0.8 §6.5.1 Z-3 covers precisely this state with percentile reversion that is "counted … reported … a **declared fallback, not a silent one**." Amendment §3 claims the PA-Z rules "parallel the Phase B rules Z-1 through Z-4," yet the table has no Z-3 analogue and the code does the opposite. The clamp is also arguably a continuity-type adjustment against §2.3's prohibition.
*Disposition.* Add a PA-Z rule for the z0-undefined state (declared percentile reversion, counted and reported) or freeze the clamp explicitly with mandatory reporting.
*Cross-reference.* FB-2; PA-2 step 1; v0.8 Z-3; F-K3-B9.

---

**F-K3-B5 | MAJOR | intervals.py lines 345–346, 107, 189–190; amendment §3 | Failed-resample hole: FB-2's explicitly listed item remains unfrozen; NaN resamples silently poison intervals**

*Substance.* Executed exact replication of the t7 bootstrap loop (1 positive among 20 items): **3,580/10,000 replicates (35.8%) are NaN**. Consequences: prop_below corrupted (NaN comparisons count as not-below); `np.percentile` → lower = upper = NaN; `excludes_zero` = False; `n_degenerate_resample` = 0. NaN resamples are **not counted, not discarded, not reported**; PA-Z8 covers only the full-data case. FB-2 listed "handling of failed bootstrap resamples" as an unfrozen item — the PA-Z table does not close it. (In t7 proper, F-K3-B1's crash fires first; the engine hole is real for any NaN-emitting statistic.)
*Disposition.* Freeze a failed-resample rule (count/discard/revert — any declared handling) with mandatory reporting.
*Cross-reference.* FB-2 ("handling of failed bootstrap resamples"); PA-Z6, PA-Z8; v0.8 Z-2 (which counts degenerate resamples).

---

**F-K3-B8 | MAJOR | Amendment §2.2 (line 115) vs intervals.py lines 92, 228/253/278/307/338, 189–190 | Executor uniqueness fails: same data + same seed → different intervals under two lawful readings**

*Substance.* The text freezes "the seed, the PRNG (NumPy default_rng with SeedSequence), and the draw order" but does **not** freeze: (i) the internal derivation `seed_value = int(rng.integers(0, 2**31))` (an extra consumed draw; `BootstrapResult.seed` records the *derived* seed, not the published one); (ii) per-threshold offsets (T2-abs seed, T2-rel seed+1, T3 seed+2, T4 seed+3, T7 seed+4) — code-only; (iii) `np.percentile` interpolation (default 'linear'); (iv) the NumPy version (bit streams not stable across releases). Executed: a text-faithful executor feeding the published seed directly into `default_rng(SeedSequence(seed))` computes the 5-fact T3 interval upper bound **6.000** vs the shipped code's **5.800** — same data, same seed, same frozen PRNG, both lawful readings.
*Disposition.* Freeze the derivation chain, offsets, interpolation, and pinned versions in the text; or declare the code the sole normative definition of the interval computation and say so explicitly.
*Cross-reference.* FB-2 core; PA-1; amendment §4 reproducibility requirement.

---

**F-K3-A5 | MAJOR | Amendment lines 57/145; test file line 51 | The wall-clock BUDGET has no frozen value anywhere normative**

*Substance.* No numeric budget appears in the amendment, the code, or v0.8 §5.2–5.4 (v0.8 "budget" hits are Phase B/C token budgets). `BUDGET = 480.0` exists only as a test fixture. Under the code's censoring reading, BUDGET enters Delta-M3 directly; two executors with different budgets compute different deltas and can flip the median gate.
*Disposition.* Freeze the budget value in the amendment text (or bind it to an already-frozen v0.8 quantity by citation).
*Cross-reference.* FB-1; §2.6; F-K3-A1.

---

**F-K3-A6 | MAJOR | m3.py lines 261–278; intervals.py line 422 | Caller-supplied-statistic rejection is incomplete, unwired, and bypassable**

*Substance.* (a) Smuggled keys accepted (executed): `t2_satisfied`, `p50`, `ci95`, `delta_m3_median`, `verdict`, `"Median "` (trailing space defeats exact-match). (b) `reject_caller_supplied_statistic` is **never called** by any evaluation path. (c) Decisive bypass, executed: `evaluate_t2_full` accepts hand-fabricated `PairedDifference` objects (a public frozen dataclass) directly — 5 fabricated deltas of +499 returned `t2_satisfied = True` with no raw M3 vector anywhere. The docstring claim "Only raw M3 vectors are accepted" is unenforced. The BSSG raw-evidence discipline the amendment invokes is not structurally in force.
*Disposition.* Enforce provenance structurally (private constructor or provenance token issued by `compute_paired_differences`); invoke validation at pipeline entry rather than by blocklist.
*Cross-reference.* Amendment §4 item 3; TestCallerRejection.

---

**F-K3-A3 | MAJOR | m3.py `m3_first` lines 108–117; amendment §5 (line 195), §1.1 (line 57) | M3-FIRST docstring/code divergence; §5 identity-with-old-M3 claim falsified**

*Substance.* Executed (two independent repros): vector {f1 OBSERVED 45.0, f2 CENSORED_EARLY 10.0} → `m3_first()` returns **10.0** — a censored-early termination time reported as time-to-first-fact — while the docstring claims "Considers only OBSERVED values." The identity claim (§5: "the summary's value on any input is identical to the old M3's value") fails on three grounds: (a) all-censored-early vector → M3-FIRST = termination time though *no fact was found* (old M3 undefined); (b) nothing found within budget → M3-FIRST = BUDGET vs old M3 undefined; (c) old M3 timed to the first *correctly adjudicated* fact while new M3 stops at the saved *evidence record* with adjudication time excluded — old ≥ new whenever adjudication is non-instantaneous. No cross-fact session-consistency check exists (an OBSERVED-at-45 after a 10-minute termination is accepted).
*Disposition.* Fix code or docstring (a text/code divergence "is a defect" under §4); retract or qualify the identity sentence to non-censored inputs.
*Cross-reference.* FB-1; v0.8 §5.2 M3; F-K3-C5.

---

**F-K3-A4 | MAJOR | m3.py lines 239–246; intervals.py lines 452–468; amendment §3 | All-zero relative gate is an unregistered NOT-EVALUABLE state**

*Substance.* M3(f,A) = 0.0 passes validation (only < 0 rejected; executed). With S non-empty but all M3(f,A) = 0: `evaluable=True, rule=None, relative_gate_met=None, t2_satisfied=None` — a third truth value with no PA-Z rule, no label, and no registration, against §1.3's two-valued "satisfied if and only if ALL THREE hold." A fact with M3(f,A)=0 and M3(f,B)=300 (B infinitely relatively slower) is silently excluded from the relative gate.
*Disposition.* Add a PA-Z rule for the all-excluded state; wire `rule` to it; state the label consequence for A2.
*Cross-reference.* FB-1; PA-Z1; §1.4; F-K3-C2.

---

**F-K3-B7 | MAJOR | intervals.py lines 306–316 vs amendment §2.4 and v0.8 §5.2 M5 | T4 denominator divergence: code divides by actual count, text freezes /200**

*Substance.* Text (amendment and v0.8): M5 = "items flagged, divided by **200** declared-generated artifacts" — fixed denominator. Code: `rate = np.mean(x[:, j])` over `len(flag_pairs)`. Executed: 150 of 200 artifacts adjudicated, 30 B-flags → code reports 0.20; the frozen definition gives 0.15; no warning that 50 artifacts are missing. The string "200" occurs only in a docstring. v0.8's NOT-FALSIFIED clause ("every denominator complete or UNKNOWN-scored") requires shortfalls to be surfaced, not silently re-denominated.
*Disposition.* Fix code to the /200 denominator with a completeness check, or amend the text; either way a §4 text-code divergence as shipped.
*Cross-reference.* FB-2; PA-3 T4; v0.8 §5.2 M5, §5.4; TestT4.

---

**F-K3-C3 | MAJOR | Amendment §3 PA-Z7 (line 163); v0.8 §5.3 T4; test file lines 491–496 | PA-Z7: trigger ≠ consequence; misquotes T4's frozen structure; fixture implements a different trigger**

*Substance.* (i) "Zero items flagged by both" does not imply "M5(B) − M5(A) = 0" — disjoint flag sets give zero overlap with nonzero difference (executed: 30 A-only + 10 B-only flags, empty intersection → difference −0.10, interval (−0.185, −0.05)). (ii) v0.8 T4 = "*point* greater than +0.05 AND *interval lower bound* above 0"; PA-Z7 says "T4 does not fire unless the interval lower bound is above **+0.05**" — moving +0.05 from point estimate to interval bound, a restatement of a frozen threshold the amendment claims not to touch (inert on the zero-flag state, false as a necessary condition in general). (iii) The shipped fixture implements a *different* trigger ("zero items flagged by **either**", all-(0,0) pairs) than the amendment's "both" — a §4 text/test divergence. Additionally, T4's firing rule (point > +0.05 AND LB > 0) exists in no code artifact; only the interval is implemented (likewise T3 and T7 firing rules).
*Disposition.* Rewrite PA-Z7 with a correct trigger (union-empty) or correct consequence; restore T4's structure verbatim; reconcile the fixture; implement or explicitly scope out the firing rules.
*Cross-reference.* F-K3-C1 (same restatement pattern); v0.8 §5.3 T4; F-K3-B9.

---

**F-K3-C4 | MAJOR | Amendment header (line 6), §5 bullet 3 (line 194), §7 PA-A3, §3 PA-Z1/PA-Z8 | "Amends Sections 5.2 and 5.3 only" is inaccurate**

*Substance.* PA-A3 "creates a **new A2 edge** … frozen as the intended behavior" — A2 lives in §5.4's frozen decision table. PA-Z1 legislates "A2 cannot fire." PA-Z8 legislates "A6 evaluates T8 alone" — new behavior for §5.4's "T7 OR T8." §2.1 glosses §5.4's frozen inferential-honesty clause. §5's unqualified "No Phase A decision clause (A1–A6) or its Boolean structure [changes]" cannot stand alongside PA-A3's own "new." The scope statement and the no-change ledger mutually reinforce an understatement of the amendment's footprint.
*Disposition.* Correct the header scope (at minimum "5.2, 5.3, and edge-state behavior of the 5.4 decision table") or restructure the freezes into an explicitly scoped section.
*Cross-reference.* F-K3-C1, F-K3-C2.

---

**F-K3-B10 | MAJOR | test file lines 281–291, 491–496; amendment §4 | Test suite does not satisfy the amendment's own freeze preconditions**

*Substance.* Amendment §4 requires ≥ 1 fixture per PA-Z rule PA-Z1..PA-Z8 and explicitly "the BCa-to-percentile fallback (PA-Z2, PA-Z5) on a 1-fact AND a degenerate-jackknife fixture." Confirmed by grep and execution: **no PA-Z5 fixture exists** (the string appears only in the module docstring, which *claims* the coverage); **no TestPAZ7 class exists**; TestPAZ4 tests the wrong rule entirely (it exercises M7 NaN input validation, unrelated to alpha-undefined); TestPAZ6 asserts non-crashing only, never the resample count; and no test calls `t7_interval` on evaluable data — which is why F-K3-B1 ships green.
*Disposition.* Fixtures for PA-Z4 (real), PA-Z5, PA-Z7, evaluable-T7, non-degenerate-T4, and the z0-undefined state are mandatory before the amendment's own §4 freeze gate is met.
*Cross-reference.* Amendment §4; F-K3-B1, F-K3-B2, F-K3-B3, F-K3-B4.

---

**F-K3-A8 | MAJOR | intervals.py lines 92, 108–111, 116–165, 253/278/306/338; amendment lines 115, 127, 161 | Code-only freezing of load-bearing numerical choices (consolidated)**

*Substance.* Beyond F-K3-B8's seed chain: the z0 clamp (F-K3-B4), the n=2 jackknife (sum_cu identically 0 → a ≡ 0 silently), and the per-threshold seed offsets all exist only in code. A text-only reimplementer cannot reproduce the intervals. The amendment's own §4 reproducibility test ("two runs with the same seed and data produce identical intervals") tests only the shipped code against itself — it cannot detect text-code executor divergence.
*Disposition.* Fold into the F-K3-B8 disposition; extend the reproducibility requirement to a text-faithful independent reimplementation check.
*Cross-reference.* FB-2; F-K3-B3, F-K3-B4, F-K3-B8.

**F-K3-A10 | MAJOR | Amendment §1.1 (lines 53–57) | "Identifies f," the t=0 event, and the budget-boundary enum remain executor-judgment degrees of freedom**

*Substance.* Discovery is redefined as "the first immutable saved evidence record that **identifies f**," but the amendment never freezes who/what maps an evidence record to ledger fact f, nor whether that mapping requires successful adjudication of c's own claim (if yes, adjudication latency re-enters the clock the amendment tried to remove; if no, an unsupported record counts as discovery — either way the §5 identity claim breaks differently). "Wall-clock minutes from corpus access" never defines the t=0 event. §2.6 para 3's "timestamp at the budget limit" case is indistinguishable in the data model from never-found (both are minutes = BUDGET; only the enum differs, and the enum's assignment rule at the boundary is unfrozen).
*Disposition.* Freeze the evidence-record→fact mapping authority, the t=0 event, and the OBSERVED-at-budget vs RIGHT_CENSORED boundary rule.
*Cross-reference.* FB-1; v0.8 §5.2; F-K3-A1, F-K3-A5.

### 3.3 MINOR findings

---

**F-K3-A7 | MINOR | Amendment §1.3 (line 81) vs §2.4 (line 134); intervals.py lines 456–468 | Interval-gate pinning is a silent substantive choice; §2.4 invites a phantom fourth gate.** Text and code agree (absolute-median interval only is load-bearing; relative interval computed but never gated — confirmed in `evaluate_t2_full`). But v0.8's phrase "at least 20 percent relative AND a 95 percent bootstrap interval excluding 0" does not uniquely attach the interval to the absolute statistic; the amendment chose absolute-only without flagging the choice or recording it, and §2.4's table still lists the relative interval as a bootstrap target an executor could read as a fourth gate. *Disposition:* state explicitly that the relative interval is reported-but-not-gated; record the disambiguation as a substantive decision. *Cross-ref:* FB-1, FB-2; v0.8 §5.3 T2.

**F-K3-C5 | MINOR | Amendment §1.2 (line 65), §5 bullet 4 | M3-FIRST identity claim overstrong.** Covered substantively in F-K3-A3; the universal quantifier ("on any input") fails on censoring edges even where code and docstring agree (all-censored vector → M3-FIRST = BUDGET, old M3 undefined). *Disposition:* qualify the claim to non-censored inputs. *Cross-ref:* F-K3-A3; §2.6.

**F-K3-C6 | MINOR | Amendment §2.1, §3 PA-Z2; v0.8 §5.4, §5.3 | Inferential-honesty consistency passes, with one new vacuous edge.** §2.1's "finite-corpus stability summaries" declaration is consonant with v0.8's frozen clause, and the amendment adds no new interval-keyed gate — the structural tension (interval exclusion used as a decision gate while declaring intervals non-inferential) is inherited unchanged. New wrinkle: PA-Z2's |S|=1 percentile fallback yields a zero-width interval that "excludes zero" whenever the single delta ≠ 0, making T2 gate 3 vacuously passable on a one-fact shared set. *Disposition:* disclose the n=1 vacuity in PA-Z2. *Cross-ref:* v0.8 §5.4 frozen clause.

**F-K3-A9 | MINOR | m3.py line 125; amendment §2.5 | Fact-ID normalization unfrozen; §2.5's secondary sort is vacuous.** `compute_shared_set` intersects raw case-sensitive strings ("F1" ≠ "f1"); identifier normalization is frozen nowhere. The "secondary sort by fact identifier" affects only list order; medians are order-invariant — the rule is load-bearing nowhere. *Disposition:* freeze identifier normalization; delete or justify the decorative sort rule. *Cross-ref:* FB-1; §2.5.

**F-K3-B6 | MINOR | intervals.py lines 173–179 | `_bca_quantile` denom == 0 → returns 0.5 silently.** Undeclared in-formula fallback; adversarial search (4,000-dataset grid + 300 random datasets) found no reachable input, but no guard ensures p_low ≤ p_high. *Disposition:* document, delete, or guard. *Cross-ref:* PA-2 step 3.

**F-K3-B9 | MINOR | intervals.py lines 138–146, 452–468 | Residual PA-Z exhaustiveness gaps.** (a) sum_sq == 0 with n > 1 → unnamed code-only branch, fallback_reason cites no PA-Z rule; (b) seed input unvalidated (seed = −1 silently accepted; seed = 1.5 raises raw TypeError, not PhaseAInputError); (c) confirmed OK: PA-Z6 counting matches "not discarded" (5,005/10,000 all-identical resamples at n=2, kept); T3 single-observation correctly reports PA-Z2. *Disposition:* register the unnamed states; validate seed input. *Cross-ref:* PA-Z1..PA-Z8; F-K3-B3, F-K3-B4.

### 3.4 EDITORIAL findings

**F-K3-C7 / F-K3-B11 | EDITORIAL | Amendment §4 (line 182) | "PhasaAInputError" typo** (code: `PhaseAInputError`) — a nominal text-code divergence sitting in the normative artifact-requirements section. *Disposition:* fix at redraft.

**F-K3-C8 | EDITORIAL (verified accurate) | Amendment §4, §3, §1.4 | Citation spot-checks that PASSED.** (a) "the v0.8 rule of Section 0" — accurate (v0.8 §0 contains the text-and-code rule). (b) "parallel the Phase B rules Z-1 through Z-4" — Z-1..Z-4 exist as cited; the parallel is approximate (see F-K3-B3). (c) PA-Z4's alpha < 0.67 → INDETERMINATE-ADJUDICATION — verbatim-accurate against v0.8 §5.3. (d) M4/T3 well-definedness — verified: v0.8 M4 is per-fact averaged over the shared set; `t3_interval`'s resampling unit matches PA-1/PA-3. (e) T5 strict-inequality boundary correct. (f) PA-A4's concession that the T2 change is SUBSTANTIVE under §12 — honest and accurate (in contrast to T5). *Disposition:* none.

---

## 4. Answers to the dispatch's attack questions

| Dispatch question | Answer |
|---|---|
| Does the per-fact M3 vector uniquely resolve the computability defect? Is T2 computable without analyst interpretation? | **No.** The right shape, but self-contradictory at the exact targeted point; two lawful readings executed on identical bytes give opposite T2 verdicts (F-K3-A1). Compounded by F-K3-A2, A4, A5, A6, A10. |
| Do PA-1/PA-2/PA-3 produce unique results? | **No.** Same data + seed → different intervals under two lawful text readings (F-K3-B8); T7 unexecutable and T4 corrupted in the shipped code (F-K3-B1, B2). |
| Are resampling units, BCa construction, and PA-Z1–Z8 exhaustive? | Resampling units: genuinely frozen (pillar stands). BCa construction: broken for 2-D units. PA-Z rules: neither exhaustive nor implementable as written (F-K3-B3, B4, B5, B9, A4). |
| Does the censoring rule preserve the conservative direction for both arms? | **No** — both sign statements are inverted, and under the code's reading the A-censored arm inflates the median toward firing (F-K3-A2). |
| Is the BCa→percentile fallback correctly triggered and counted? | **No** — PA-Z5's graduated tiers are unreachable dead code; real degeneracies route to unnamed paths; the z0-undefined state is silently clamped against the declared-fallback principle (F-K3-B3, B4). |
| Does PA-Z1 interact correctly with the A2 clause domain? | **No** — the invoked inheritance does not exist; the vacuous-A2 path yields NOT-FALSIFIED with the shared-set comparison never performed (F-K3-C2). |
| Is the §2.1 declaration consistent with v0.8 §5.4's inferential-honesty clause? | **Yes** (F-K3-C6), with one new vacuous n=1 edge to disclose. |
| Does the amendment change anything it claims not to change? | **Yes** — T5's interval conjunct (F-K3-C1), §5.4 decision-table edge behavior (F-K3-C4), T4's frozen structure restated in PA-Z7 (F-K3-C3), M3-FIRST identity (F-K3-A3/C5). |
| Is there an edge state the PA-Z rules miss? | **Several**: failed/NaN resamples (B5), z0-undefined (B4), all-excluded relative gate (A4), sum_sq=0 with n>1 unnamed (B9), n=2 silent a≡0 (A8). |

## 5. Required actions before re-carrying (v0.8.2)

1. Resolve the S-membership contradiction (F-K3-A1) in text *and* code; re-derive the censoring conservatism argument with correct signs (F-K3-A2); freeze BUDGET (F-K3-A5).
2. Repair the 2-D jackknife (F-K3-B1, B2) and add evaluable-path fixtures for T4 and T7.
3. Rewrite PA-Z5 in terms of a computable quantity; add declared, counted rules for z0-undefined and failed/NaN resamples (F-K3-B3, B4, B5); register the all-excluded relative-gate state (F-K3-A4).
4. Freeze the seed-derivation chain, per-threshold offsets, percentile interpolation, and pinned library versions in the text — or declare the code solely normative for intervals and say so (F-K3-B8, A8).
5. Correct the §5 no-change ledger and header scope; record the T5 change (or restore the interval gate), the §5.4 edge freezes, and the T2 interval-gate disambiguation in the amendment record (F-K3-C1, C3, C4, A7).
6. Add an explicit Phase A edge-state label rule for vacuous A2 (F-K3-C2).
7. Complete the §4 fixture suite: PA-Z4 (real), PA-Z5, PA-Z7, evaluable-T7, non-degenerate-T4, z0-undefined, fabricated-delta rejection (F-K3-B10, A6).
8. Enforce raw-evidence provenance structurally (F-K3-A6); fix M3-FIRST (F-K3-A3); freeze fact-ID normalization and the t=0/identifies-f mapping authority (F-K3-A9, A10).

## 6. Provenance and carrying-rule statement

This audit was executed by Kimi K3 (Moonshot AI) as carrying seat 2 of 2, with three parallel adversarial verification passes whose every load-bearing claim was independently reproduced by the carrying seat against the canonical bytes before adoption into this register. All executed evidence is derived from the shipped files whose SHA-256 values match the dispatch manifest. Same-vendor seats count once; producer-family review is advisory; carry is limited to the checks executed and is not peer review. Under the carrying rule inherited from SHVVP v0.8 §12, this HALT blocks deposit of v0.8.1 and requires a new version.

**Carrying verdict: HALT.**

*End of carrying audit report — Kimi K3 seat, 2026-07-31.*

---

# Bismillah ir-Rahman ir-Rahim
