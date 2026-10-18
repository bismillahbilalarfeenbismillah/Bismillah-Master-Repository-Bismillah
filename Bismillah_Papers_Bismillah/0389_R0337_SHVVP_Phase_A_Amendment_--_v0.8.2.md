# Bismillah ir-Rahman ir-Rahim

# R0337 -- SHVVP Phase A Amendment -- v0.8.2

**Chronological Index:** 389 of 995  
**Date:** 2026-07-31  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** shvvp_phase_a_amendment_v0_8_2.txt  
**Source Format:** txt  
**SHA-256:** `e6a9837fbbe4185690f616bec47d234e4dfa0a61f334a490d5d57b8eccddf2b1`  

---

## R0337 · SHVVP Phase A Amendment -- v0.8.2

- section: V. BSSG & SHVVP Protocols
- source_file: shvvp_phase_a_amendment_v0_8_2.txt
- source_format: txt
- text_sha256: e6a9837fbbe4185690f616bec47d234e4dfa0a61f334a490d5d57b8eccddf2b1

# SHVVP Phase A Amendment -- v0.8.2

**Author of record:** Bilal Syed Arfeen (BayyinahEnterprise)
**Date:** 2026-07-31
**Status:** PROPOSED AMENDMENT -- NOT FROZEN, NOT CARRIED, NOT DEPOSITED
**Amends:** SHVVP v0.8 ([doi:10.5281/zenodo.21583202](https://doi.org/10.5281/zenodo.21583202)), Sections 5.2, 5.3, and edge-state behavior of the Section 5.4 decision table
**Supersedes:** v0.8.1 (HALTED; never deposited)
**Triggered by:** XZ Protocol freeze-blockers FB-1 and FB-2
**v0.8.1 carrying audit:** GPT 5.6 Sol HALT (7 findings); Kimi K3 HALT (3 BLOCKER, 14 MAJOR, 5 MINOR, 2 EDITORIAL). All findings accepted in full. Both seat reports ship unmodified with this release.

---

## 0. History and scope

### 0.1 What happened to v0.8.1

v0.8.1 was dispatched to two carrying seats (GPT 5.6 Sol, Kimi K3) on 2026-07-31. Both returned HALT. The seats converged on five structural defects: (1) self-contradictory S-membership rule reproducing the FB-1 computability defect; (2) 2-D jackknife crash on T7 and fabricated acceleration on T4; (3) T5 interval conjunct silently dropped while claiming no threshold changed; (4) PA-Z5 dead code with z0-undefined silently clamped; (5) Phase A NOT-EVALUABLE priority invoked but not inherited. Additional findings included unfrozen BUDGET, caller-supplied-statistic bypass, NaN-poisoned resamples, unenforced cardinalities, M3-FIRST returning censored non-discoveries, and a test suite that did not exercise the paths where defects lived.

v0.8.1 is HALTED, was NEVER DEPOSITED, and is not binding. It is retained for lineage and shipped unmodified.

### 0.2 What v0.8.2 changes

This amendment touches Sections 5.2 (M3 definition), 5.3 (T2 and T5 definitions), and edge-state behavior of the Section 5.4 decision table. Specifically:

1. M3 is enriched from a scalar to a per-fact discovery-time vector (FB-1).
2. T2 is restated over the per-fact paired differences (FB-1).
3. T5's interval conjunct is formally retired (PA-A5; substantive, declared).
4. Phase A interval algorithms are frozen as PA-1, PA-2, PA-3 with eleven degeneracy rules PA-Z1 through PA-Z11 (FB-2).
5. A Phase A construction-evaluability gate is added to the 5.4 decision table, preventing NOT-FALSIFIED when A2's shared-set domain was vacuous.

The code is the sole normative definition of the interval computation. The amendment text describes the algorithm; the shipped code implements it. A divergence between them is a defect.

### 0.3 What v0.8.2 does NOT change

- No estimand attribute of any phase.
- No Phase B or Phase C rule, threshold, interval algorithm, corpus size, label, or anchor fact.
- No Phase A decision clause (A1-A6) or its Boolean structure -- the clauses fire on the same conditions; the amendment makes them uniquely executable and adds an evaluability guard.
- No metric other than M3 (enriched from scalar to vector with a named scalar summary).
- No threshold other than T2 (restated to be computable on the new M3 vector) and T5 (interval conjunct formally retired -- see PA-A5).
- No reliability threshold, no adjudication rule, no scope statement, no safety boundary, no anchor fact.

The T5 change is SUBSTANTIVE under SHVVP v0.8 Section 12 and is declared as such in amendment entry PA-A5. It is not a silent deletion.

---

## 1. Resolution of FB-1: M3, T2, and S-membership

### 1.1 M3 is a per-fact observation vector

**Old M3 (v0.8).** Wall-clock minutes from corpus access to first correctly adjudicated consequential fact, per condition. One scalar.

**New M3 (v0.8.2).** For each correctly adjudicated consequential fact f in the sealed reference-standard ledger and each condition c:

> M3(f, c) = wall-clock minutes from first packet access to the first immutable saved evidence record that identifies f, under condition c.

Censor-status rules:

- **OBSERVED:** condition c identified f. The `minutes` field is the discovery time. An `evidence_record_id` is required.
- **RIGHT_CENSORED_BUDGET:** condition c did NOT identify f within the budget. The `minutes` field MUST equal FROZEN_BUDGET_MINUTES (480.0 minutes, frozen by this amendment). No evidence record exists.
- **CENSORED_EARLY:** the session terminated before the budget expired. The `minutes` field is the termination time and MUST be strictly less than FROZEN_BUDGET_MINUTES. The fact was NOT identified.

### 1.2 M3-FIRST: observed-only scalar summary

> M3-FIRST(c) = min over OBSERVED discoveries of M3(f, c).

If no OBSERVED facts exist, M3-FIRST returns the typed result NO_DISCOVERY. Censored observations (RIGHT_CENSORED_BUDGET, CENSORED_EARLY) are excluded from M3-FIRST.

This preserves the v0.8 scalar quantity for non-censored inputs. The identity is qualified: on vectors containing only censored entries, old M3 was undefined; new M3-FIRST returns NO_DISCOVERY rather than a budget value.

### 1.3 S is the observed-shared set

The shared fact set S consists of facts OBSERVED by both conditions:

> S = {f : f is OBSERVED in vec_A AND f is OBSERVED in vec_B}

A fact that one condition did not identify (RIGHT_CENSORED_BUDGET or CENSORED_EARLY) is NOT in S. This resolves the v0.8.1 contradiction (F-K3-A1) by choosing one rule and implementing it consistently: `compute_shared_set` intersects `observed_fact_ids`, not `all_fact_ids`. A fact found by neither condition cannot enter S. A fact found by one but not the other cannot enter S.

Because only OBSERVED facts enter S, censored observations never enter the T2 paired differences. The censoring-direction analysis of v0.8.1 Section 2.6 is withdrawn; it was wrong in both sign statements (F-K3-A2) and unnecessary under the observed-shared rule.

### 1.4 T2 restated

On S only, for each f in S define:

> Delta-M3(f) = M3(f, A) - M3(f, B).

Both M3 values are OBSERVED (by S-membership). T2 is satisfied if and only if ALL THREE hold:

1. The median of {Delta-M3(f) : f in S} is at least 30 minutes.
2. The median of {Delta-M3(f) / M3(f, A) : f in S, M3(f, A) > 0} is at least 0.20. Facts with M3(f, A) = 0 are excluded from this relative median and their count is reported. If all M3(f, A) = 0, the relative gate is NOT-EVALUABLE (PA-Z9).
3. The 95 percent BCa bootstrap interval for the median of {Delta-M3(f) : f in S}, computed by the Phase A interval algorithm of Section 2, excludes zero. The interval gate is computed on the absolute median only; the relative interval is reported but not gated. This disambiguation is a substantive decision recorded here.

If S is empty, T2 is NOT-EVALUABLE (PA-Z1).

### 1.5 Edge state: IDC > 0, S empty

If Condition B finds unique facts (IDC > 0) but shares none with A (S = {}), then T2 and T3 are both NOT-EVALUABLE, and A2 cannot fire. Under v0.8's formula, this could produce NOT-FALSIFIED on a shared-set comparison that never happened. v0.8.2 adds an explicit construction-evaluability guard: NOT-FALSIFIED requires that every clause whose domain was entered produced a determinate result. If A2's domain was entered (IDC > 0) but A2 could not evaluate (S empty), the Phase A result is NOT-EVALUABLE, not NOT-FALSIFIED. This guard is a new edge-state rule for the Section 5.4 decision table and is recorded as amendment entry PA-A3.

### 1.6 Fact-ID normalization

Fact identifiers are normalized by stripping whitespace, case-sensitive. "F1" and "f1" are distinct. The normalization is frozen by this amendment.

---

## 2. Resolution of FB-2: Phase A interval algorithms

### 2.1 Status of Phase A intervals

Phase A intervals are **finite-corpus stability summaries**. They are not population confidence intervals. No hypothesis test, no p-value, and no population inference attaches to any Phase A interval. This is consistent with the v0.8 Section 5.4 inferential-honesty clause.

### 2.2 The code is the sole normative definition

The shipped Python modules (`shvvp_v0_8_2_phase_a_m3.py`, `shvvp_v0_8_2_phase_a_intervals.py`) are the sole normative definition of the interval computation. The text in this section describes the algorithm; a text-only reimplementer must match the golden-vector outputs in the test suite. Where text and code could be read as differing, the code governs and the difference is a defect in this text, not a license to choose.

### 2.3 PA-1: resampling

| Threshold | Resampling unit | Population | Paired |
|---|---|---|---|
| T2 | The shared fact | S | Yes |
| T3 | The shared fact | S | Yes |
| T4 | The declared-generated artifact | 200 items (enforced) | Yes |
| T5 | NOT BOOTSTRAPPED (PA-A5) | -- | -- |
| T7 | The discrimination-set item | 240 items (enforced) | Yes (multidim) |

Number of draws: 10,000. Seed: passed as an integer; the code derives an internal seed via `np.random.default_rng(SeedSequence(seed))`. Per-threshold seed offsets: T2-abs = seed, T2-rel = seed+1, T3 = seed+2, T4 = seed+3, T7 = seed+4. These offsets exist only in code and are normative.

### 2.4 PA-2: BCa bounds

For a statistic theta on the full sample and bootstrap replicates theta-star:

1. **Bias correction z0:** standard normal quantile of the proportion of replicates strictly below theta. If prop_below is 0 or 1, z0 is undefined -- PA-Z10 fires.
2. **Acceleration a:** leave-one-unit-out jackknife, standard third-moment formula. For multidim data, jackknife uses `np.delete(data, i, axis=0)`. If sum_sq = 0, acceleration is undefined -- PA-Z5 fires.
3. **Bounds:** bootstrap percentiles at BCa-adjusted levels for a two-sided 95 percent interval.

No smoothing, no variance stabilisation, no continuity correction.

### 2.5 PA-3: statistics

| Threshold | Point statistic | Bootstrap target |
|---|---|---|
| T2 (absolute) | Median of Delta-M3 | BCa interval for median |
| T2 (relative) | Median of Delta-M3/M3(f,A) | Reported, not gated |
| T3 | Mean of M4(B)-M4(A) | BCa interval for mean |
| T4 | M5(B)-M5(A), /200 (enforced) | BCa interval for difference |
| T7 | M6(B) = balanced accuracy | BCa interval for M6(B) |

### 2.6 Cardinality enforcement

T4 requires exactly 200 items with binary (0/1) flags. T7 requires exactly 240 items with binary (0/1) labels. T3 rejects NaN and Inf. M3 rejects NaN, Inf, and negative values. Wrong cardinality or invalid values raise PhaseAInputError before any computation.

---

## 3. Degeneracy rules PA-Z1 through PA-Z11

| Rule | Condition | Handling |
|---|---|---|
| PA-Z1 | S is empty | T2 and T3 are NOT-EVALUABLE. A2 cannot fire. Section 1.5 guard applies. |
| PA-Z2 | |S| = 1 (or n=1 for any threshold) | Percentile reversion. No bootstrap run. Zero-width interval; point estimate only. Reported and counted. |
| PA-Z3 | M7(A) = 0 | T5 NOT-EVALUABLE. Ratio undefined. A4 cannot fire. |
| PA-Z4 | Alpha undefined (fewer than 2 ratable items, or all pairs identical) | INDETERMINATE-ADJUDICATION under v0.8 Section 5.3. |
| PA-Z5 | sum_sq = 0 with n > 1 (jackknife acceleration undefined) | Percentile reversion. Counted and reported. Fallback reason cites PA-Z5. |
| PA-Z7 | T4 union-empty: no items flagged by either condition | M5(B)-M5(A) = 0. Interval computed normally. T4 fires only if point > +0.05 AND interval LB > 0. |
| PA-Z8 | M6(B) not computable: zero items in a classification cell | T7 NOT-EVALUABLE. A6 evaluates T8 alone. |
| PA-Z9 | All M3(f,A) = 0 in S | T2 relative gate NOT-EVALUABLE. T2 overall NOT-EVALUABLE. |
| PA-Z10 | z0 undefined: prop_below = 0 or 1 | Percentile reversion. Counted and reported. No silent clamp. |
| PA-Z11 | NaN bootstrap resamples | Counted, discarded. Intervals computed on valid resamples. n_nan_resamples reported. If fewer than 2 valid resamples remain, zero-width interval returned. |

PA-Z5 is a structural guard. For mean and median statistics, if all jackknife values are identical (sum_sq = 0), all bootstrap replicates are also identical (prop_below = 0), so PA-Z10 fires first. PA-Z5 guards against edge cases where floating-point rounding produces sum_sq = 0 after z0 has been validly computed for other statistics.

---

## 4. T5 interval conjunct: formally retired (PA-A5)

v0.8 T5: "M7(B)/M7(A) greater than 1.25 AND 95 percent interval lower bound above 1.00."

v0.8.2 T5: "M7(B)/M7(A) greater than 1.25." The interval conjunct is retired.

**Justification (declared, not silent).** Phase A has no T5 resampling unit. The two team pairs are never pooled (v0.8 Section 5.4 inferential-honesty clause). A bootstrap over two team pairs is a bootstrap over n=2, which produces a degenerate interval that does not meaningfully constrain the ratio. The inherited inferential-honesty clause precludes treating team pairs as independent observations of a population parameter. Retiring the interval conjunct is more honest than computing a vacuous interval and calling it a gate.

This is a SUBSTANTIVE change to T5 under v0.8 Section 12 and changes A4's firing threshold (T5 fires strictly more often without the interval conjunct). It is recorded as amendment entry PA-A5 and in the scope statement of Section 0.2.

---

## 5. Caller-supplied statistic rejection

PairedDifference objects carry a module-private provenance token generated at import. Only `compute_paired_differences()` can produce valid instances. Every evaluation path (`evaluate_t2_point`, `evaluate_t2_full`, `t2_absolute_interval`, `t2_relative_interval`) calls `verify_provenance()` on each input. Hand-fabricated PairedDifference objects are rejected with PhaseAInputError before any statistic is computed.

This implements the BSSG raw-evidence discipline: the evaluator accepts raw M3 vectors and recomputes everything. A caller cannot inject a pre-computed median, interval, delta, or verdict.

---

## 6. Executable artifacts

| File | SHA-256 | Role |
|---|---|---|
| `shvvp_v0_8_2_phase_a_m3.py` | `34f08307...` | M3 vector, S-membership, paired differences, provenance |
| `shvvp_v0_8_2_phase_a_intervals.py` | `07338303...` | PA-1/PA-2/PA-3, PA-Z1 through PA-Z11, T2/T3/T4/T5/T7 |
| `test_shvvp_v0_8_2_phase_a.py` | `367b475e...` | 61-test adversarial suite |

The test suite covers: every PA-Z rule (PA-Z1 through PA-Z11), evaluable T4 with 200 items, evaluable T7 with 240 items, z0-undefined (PA-Z10), NaN resamples (PA-Z11), all-zero relative gate (PA-Z9), provenance rejection of fabricated deltas, M3-FIRST observed-only with NO_DISCOVERY, S-membership observed-only with censored exclusion, censor-status consistency (budget value, early < budget, observed requires evidence_record_id), fact-ID normalization, cardinality enforcement, NaN/Inf rejection for T3, seed reproducibility, frozen budget value, and the 5-fact reference computation.

---

## 7. Amendment record (append-only)

**v0.8.2 (2026-07-31): Phase A executability amendment, corrected after two-family carrying HALT of v0.8.1.**

- **PA-A1 (from FB-1 / F-SOL-1 / F-K3-A1).** ACCEPTED IN FULL. M3 redefined as a per-fact discovery-time vector. S-membership rule resolved: observed-shared-only. Censored non-discoveries excluded from S structurally. v0.8.1's contradictory censoring-direction analysis withdrawn.
- **PA-A2 (from FB-2 / F-SOL-2 / F-K3-B1/B2/B3/B4/B5).** ACCEPTED IN FULL. Phase A interval algorithms frozen as PA-1, PA-2, PA-3 with eleven degeneracy rules PA-Z1 through PA-Z11. 2-D jackknife fixed (axis=0). z0-undefined declared as PA-Z10 percentile reversion. NaN resamples declared as PA-Z11. PA-Z5 rewritten over sum_sq = 0 (computable quantity).
- **PA-A3 (new edge state).** The empty-S state (IDC > 0, S = {}) adds a construction-evaluability guard to the Section 5.4 decision table: NOT-FALSIFIED is barred when A2's domain was entered vacuously. This is an edge-state rule, not a clause change.
- **PA-A4 (scope).** This amendment touches Sections 5.2 (M3), 5.3 (T2, T5), and edge-state behavior of Section 5.4. The header and this entry say so explicitly, correcting v0.8.1's inaccurate "5.2 and 5.3 only" (F-K3-C4).
- **PA-A5 (T5 interval conjunct retired).** SUBSTANTIVE. T5's "95 percent interval lower bound above 1.00" conjunct is removed. Justification: Phase A has no T5 resampling unit; two team pairs are never pooled; a bootstrap over n=2 is degenerate. This changes A4's firing threshold and is declared as a substantive change under Section 12, not a silent deletion. v0.8.1 made this change silently while claiming no threshold changed (F-K3-C1, F-SOL-081-1); v0.8.2 records it.
- **PA-A6 (M3-FIRST observed-only).** M3-FIRST returns NO_DISCOVERY for all-censored or empty vectors. The backward-compatibility claim is qualified to non-censored inputs (F-K3-A3/C5).
- **PA-A7 (cardinalities enforced).** T4: exactly 200 items, binary flags. T7: exactly 240 items, binary labels. T3: NaN/Inf rejected. M3: NaN/Inf/negative rejected. Censor-status consistency enforced (F-K3-B7, F-SOL-081-6).
- **PA-A8 (caller rejection structural).** Provenance token on PairedDifference. Pipeline entry validation. Fabricated deltas rejected (F-K3-A6).
- **PA-A9 (BUDGET frozen).** FROZEN_BUDGET_MINUTES = 480.0 (F-K3-A5).
- **PA-A10 (code is sole normative definition).** Per-threshold seed offsets, percentile interpolation, and interval computation exist only in code. Text describes; code governs (F-K3-B8).
- **PA-A11 (v0.8.1 status).** v0.8.1 is HALTED, was never deposited, and is not binding. Both carrying-seat reports (GPT 5.6 Sol, Kimi K3) ship unmodified. All findings from both seats are accepted in full; none is downgraded.

**Status:** PROPOSED. Not frozen, not carried, not deposited. Requires two-family non-producer carrying audit before FROZEN status.

---

## 8. Carrying and deposit plan

1. Ship the amendment text, three executable artifacts, and both v0.8.1 carrying-seat reports as a candidate package.
2. Two non-producer carrying seats of different vendor families execute the canonical bytes, verify the test suite, recompute SHA-256 identity, and attack every repair claim against the v0.8.1 findings.
3. Same-vendor seats count once. Producer-family review is advisory.
4. A HALT from either carrying seat blocks deposit and requires a new version.
5. Upon convergent non-HALT verdicts, the amendment is deposited as SHVVP v0.8.2.
6. The XZ Protocol's FREEZE-BLOCKER fields FB-1 and FB-2 are filled by referencing the deposited v0.8.2 DOI and test-suite digest.

---

*Provenance.* Authored by Bilal Syed Arfeen (BayyinahEnterprise); prepared with frontier language models as analytical and drafting instruments under the author's direction and final authority. This document has NOT undergone independent human peer review. v0.8.1 carrying-seat reports from GPT 5.6 Sol and Kimi K3 ship unmodified. This document makes no effectiveness claim about BSSG, SHV, or any component of the Structural Honesty program.

*End of proposed SHVVP Phase A Amendment v0.8.2.*

---

# Bismillah ir-Rahman ir-Rahim
