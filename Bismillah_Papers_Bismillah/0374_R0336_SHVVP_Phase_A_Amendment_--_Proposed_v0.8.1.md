# Bismillah ir-Rahman ir-Rahim

# R0336 -- SHVVP Phase A Amendment -- Proposed v0.8.1

**Chronological Index:** 374 of 995  
**Date:** 2026-07-30  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** shvvp_phase_a_amendment_v0_8_1.txt  
**Source Format:** txt  
**SHA-256:** `ea75b7465d3c6396e78ec08a4fef3e38ec0603b5e68d8e5669318f0dcc6e59a8`  

---

## R0336 · SHVVP Phase A Amendment -- Proposed v0.8.1

- section: V. BSSG & SHVVP Protocols
- source_file: shvvp_phase_a_amendment_v0_8_1.txt
- source_format: txt
- text_sha256: ea75b7465d3c6396e78ec08a4fef3e38ec0603b5e68d8e5669318f0dcc6e59a8

# SHVVP Phase A Amendment -- Proposed v0.8.1

**Author of record:** Bilal Syed Arfeen (BayyinahEnterprise)
**Date:** 2026-07-30
**Status:** PROPOSED AMENDMENT -- NOT FROZEN, NOT CARRIED, NOT DEPOSITED
**Amends:** SHVVP v0.8 ([doi:10.5281/zenodo.21583202](https://doi.org/10.5281/zenodo.21583202)), Sections 5.2 and 5.3 only
**Triggered by:** XZ Protocol freeze-blockers FB-1 and FB-2, identified by the GPT 5.6 Sol advisory seat (F-SOL-1, F-SOL-2) and confirmed by Claude Fable 5 and the model-council synthesis
**Scope:** Phase A metrics and interval algorithms ONLY. No Phase B or Phase C rule is touched. No estimand attribute, decision threshold, margin, corpus size, anchor fact, scope statement, or safety boundary is altered.

---

## 0. The defect

### 0.1 FB-1: M3 and T2 are not the same computable quantity

The deposited SHVVP v0.8 Section 5.2 defines:

> **M3** -- Time to first consequential fact. Wall-clock minutes from corpus access to first correctly adjudicated consequential fact, per condition.

This is one scalar per condition.

Section 5.3 then defines:

> **T2** -- On the shared fact set only: median M3(A) minus M3(B) at least 30 minutes AND at least 20 percent relative AND a 95 percent bootstrap interval excluding 0.

T2 operates "on the shared fact set" and takes a "median" -- which presupposes a per-fact vector of paired discovery-time observations. A median of two scalars is undefined over a shared set. Two competent executors can lawfully compute different T2 results from the same bytes, because the deposited definition does not uniquely determine the observation.

### 0.2 FB-2: Phase A interval algorithms are under-specified

T2, T3, T4, T5, and T7 require "95 percent bootstrap interval" or "95 percent interval lower bound," but Phase A does not freeze:

- the resampling unit (fact, item, team pair, or something else);
- the paired or unpaired structure;
- the number of bootstrap draws;
- the deterministic seed;
- the interval construction method (BCa, percentile, or other);
- the tie handling rule for discovery times;
- the empty-shared-set rule;
- the zero-burden denominator rule (M7(A) = 0);
- the all-agreement reliability degeneracy (alpha undefined);
- the handling of failed bootstrap resamples.

Phase B has a fully frozen BCa algorithm (A-1, A-2, A-3, Z-1 through Z-4 in Section 6.5.1). Phase A has no equivalent specification. The Phase B algorithms cannot be silently imported because they are keyed to Phase B's resampling unit (task-by-variant cell) and Phase B's population model; Phase A has no resampling unit and no population model, and the frozen inferential-honesty clause states that Phase A "has no power target because it has no replicable unit of randomisation."

---

## 1. Resolution of FB-1: M3 redefinition (SUBSTANTIVE)

### 1.1 M3 becomes a per-fact observation

**Old definition (v0.8).** M3 = wall-clock minutes from corpus access to first correctly adjudicated consequential fact, per condition.

**New definition (v0.8.1).** M3 is a per-fact observation vector. For each correctly adjudicated consequential fact f in the sealed reference-standard ledger and each condition c:

> M3(f, c) = wall-clock minutes from corpus access to the first immutable saved evidence record that identifies f, under condition c.

If condition c does not identify f at all, M3(f, c) is RIGHT-CENSORED at the fixed wall-clock budget. If condition c's session is terminated before the budget expires, the termination time is used and the observation carries a CENSORED-EARLY flag. Discovery is defined as the first immutable saved evidence record that identifies the fact, not a later narrative claim; pauses, tool failures, and adjudication time are recorded separately but do not interrupt the clock.

### 1.2 M3-FIRST: the named scalar summary

The time-to-first quantity that v0.8 called M3 is preserved as a named summary:

> M3-FIRST(c) = min over all consequential facts f of M3(f, c), for condition c.

M3-FIRST is reported alongside the per-fact vector but is not a primary metric. It is not renumbered; it is a derived quantity from M3. The v0.8 label "M3" in any existing text is understood as M3-FIRST for backward compatibility with pre-amendment prose. No pre-v0.8.1 text is silently edited.

### 1.3 T2 restated over the per-fact vector

**Old T2 (v0.8).** On the shared fact set only: median M3(A) minus M3(B) at least 30 minutes AND at least 20 percent relative AND a 95 percent bootstrap interval excluding 0.

**New T2 (v0.8.1).** On the shared fact set S (facts found by both conditions and correctly adjudicated as consequential under both conditions):

For each f in S, define the paired difference:

> Delta-M3(f) = M3(f, A) minus M3(f, B).

T2 is satisfied if and only if ALL THREE of the following hold:

1. The median of {Delta-M3(f) : f in S} is at least 30 minutes (absolute gate);
2. The median of {Delta-M3(f) / M3(f, A) : f in S, M3(f, A) > 0} is at least 0.20 (relative gate; facts with M3(f, A) = 0 are excluded from the relative gate's median and their count is reported);
3. The 95 percent BCa bootstrap interval for the median of {Delta-M3(f) : f in S}, computed by the Phase A interval algorithm of Section 2, excludes zero.

If S is empty (no shared facts), T2 is NOT-EVALUABLE. This is a registered edge state, not a silent omission (see Section 3, rule PA-Z1).

### 1.4 What this changes

A2 evaluates T2 AND T3 on the shared set, but only if IDC > 0. If IDC = 0, A1 fires and A2's domain is never entered. If IDC > 0 but S is empty (B found unique facts but shares none with A), then T2 and T3 are both NOT-EVALUABLE, and A2 cannot fire; the inherited priority order (NOT-EVALUABLE dominates) applies. This edge state is new and is frozen here as amendment record item PA-1.4.

No other metric, threshold, clause, or label changes. M4 is already per-fact by definition and requires no amendment. T3 operates on "mean M4(B) minus M4(A)" over the shared facts, which is well-defined given the per-fact M4 rubric.

---

## 2. Resolution of FB-2: Phase A interval algorithm (SUBSTANTIVE)

### 2.1 Status of Phase A intervals

Phase A intervals are **finite-corpus stability summaries**. They are not population confidence intervals, because Phase A has no population model and no replicable unit of randomisation. They characterize the sensitivity of the registered point statistics to the composition of the shared fact set or corpus item set. This is stated explicitly and governs interpretation: no Phase A interval may be reported with language implying a population inference, a hypothesis test, or a sampling distribution.

### 2.2 Frozen algorithm PA-1 (resampling)

**Resampling unit.** The unit varies by threshold:

| Threshold | Resampling unit | Population |
|---|---|---|
| T2 | The shared fact | S (shared consequential facts) |
| T3 | The shared fact | S |
| T4 | The declared-generated artifact | The 200-item legitimate-difference corpus |
| T5 | The team pair | NOT BOOTSTRAPPED (see PA-Z3) |
| T7 (M6 interval) | The discrimination-set item | The 240-item discrimination set |

**Paired structure.** T2 and T3 resample paired observations (one pair per shared fact: A score and B score). T4 resamples paired observations (one pair per artifact: A flag and B flag). T7 resamples paired per-item classification outcomes. The pairing is preserved across all resampled sets within a single bootstrap replicate.

**Number of draws.** 10,000 bootstrap replicates for any reported analysis, consistent with the Phase B rule.

**Deterministic seed.** A single seed is drawn uniformly at random and published in the protocol's sealed commitment before any data are opened. The seed, the pseudorandom number generator (NumPy default_rng with SeedSequence), and the draw order are frozen so that any executor reproducing the analysis from the same data and seed obtains identical intervals.

### 2.3 Frozen algorithm PA-2 (BCa bounds)

The BCa construction follows the Phase B algorithm A-2, adapted to Phase A's resampling units:

For a statistic theta computed on the full sample and bootstrap replicates theta-star(1) through theta-star(B):

1. **Bias correction z0:** the standard normal quantile of the proportion of replicates strictly below theta.
2. **Acceleration a:** computed from a leave-one-unit-out jackknife of the same statistic, using the standard third-moment formula.
3. **Reported bounds:** the bootstrap percentiles at the BCa-adjusted levels for a two-sided 95 percent interval.

No smoothing, no variance stabilisation, and no continuity correction of any kind is applied to any statistic. This is the same prohibition as Phase B, extended to Phase A by this amendment.

### 2.4 Frozen algorithm PA-3 (statistics)

| Threshold | Point statistic | Bootstrap target |
|---|---|---|
| T2 (absolute) | Median of {Delta-M3(f) : f in S} | BCa interval for this median |
| T2 (relative) | Median of {Delta-M3(f) / M3(f, A) : f in S, M3(f, A) > 0} | BCa interval for this median |
| T3 | Mean of {M4(f, B) minus M4(f, A) : f in S} | BCa interval for this mean |
| T4 | M5(B) minus M5(A), each computed as items flagged / 200 | BCa interval for this difference |
| T7 | M6(B) = mean of sensitivity and specificity on the 240-item set | BCa interval for M6(B) |

### 2.5 Tie handling

If two or more facts share the same discovery time under one condition, they are recorded with the same M3 value. Ties in Delta-M3 are preserved in the median computation (standard definition: median of an even-count set is the average of the two middle values). Ties do not trigger special handling beyond standard sort-order determinism (secondary sort by fact identifier, ascending).

### 2.6 Censored observations

A right-censored M3 observation (condition c did not identify fact f within the budget) enters the paired difference as Delta-M3(f) = M3(f, A) minus BUDGET. Because censoring at a large value makes Delta-M3 more positive (favoring B) when A identified the fact but B did not, this is the conservative direction for T2: it makes the median harder to achieve, not easier. The reverse (B found f, A did not) produces a large negative Delta-M3, which is also conservative -- it makes the median harder to satisfy. The censoring direction is therefore fail-safe for both arms and requires no correction.

If A did not find fact f at all, f is not in S (A's fact set does not include f), so it does not enter the shared-set computation. The same holds for B. Censoring applies only when both conditions found the fact but one's saved-evidence timestamp is at the budget limit.

---

## 3. Frozen zero-event and degeneracy rules for Phase A

These are predeclared before data and are the only permitted handling. They parallel the Phase B rules Z-1 through Z-4.

| Rule | Condition | Frozen handling |
|---|---|---|
| PA-Z1 | S is empty (no shared consequential facts) | T2 and T3 are NOT-EVALUABLE. A2 cannot fire. M3 and M4 are still computed per-condition on each condition's own fact set and reported descriptively. |
| PA-Z2 | S contains exactly one fact | The median of one observation is that observation. The BCa jackknife acceleration is undefined (zero denominator in the third-moment formula). The interval for T2 reverts to the plain percentile bootstrap interval, and the reversion is counted and reported. T3's mean of one observation is that observation; same BCa fallback applies. |
| PA-Z3 | M7(A) = 0 (zero baseline reviewer-hours) | T5 is NOT-EVALUABLE. The ratio M7(B)/M7(A) is undefined. A4 cannot fire. Both M7 values are reported. |
| PA-Z4 | Alpha is undefined (fewer than two ratable items for M12, or all pairs identical) | INDETERMINATE-ADJUDICATION under the existing v0.8 rule. This is not zero and not satisfactory. The frozen handling is the same as v0.8 Section 5.3: alpha below 0.67 yields INDETERMINATE-ADJUDICATION; undefined alpha receives the same label. |
| PA-Z5 | More than 5 percent of bootstrap replicates produce a degenerate jackknife (zero third-moment denominator) | The BCa acceleration is set to zero for the affected replicates (reducing BCa to BC -- bias-corrected only). The count of affected replicates is reported. If more than 20 percent of replicates are affected, the interval for that statistic reverts to the plain percentile interval, the reversion is counted, and the report discloses the instability. |
| PA-Z6 | A bootstrap resample draws the same fact |S| times (all-identical resample) | The statistic for that resample is the observed value of the unique fact. The resample is not discarded. |
| PA-Z7 | The legitimate-difference corpus has zero items flagged by both conditions | T4 is evaluated on the zero difference. M5(B) minus M5(A) = 0, and the interval is computed normally. T4 does not fire unless the interval lower bound is above +0.05. |
| PA-Z8 | M6(B) cannot be computed (zero items in a classification cell, producing undefined sensitivity or specificity) | M6(B) is NOT-EVALUABLE. T7 is NOT-EVALUABLE. A6 evaluates T8 alone: if M11 is at least 1, A6 fires through T8. |

---

## 4. Executable artifacts required by this amendment

This amendment is not FROZEN until the following exist as canonical bytes shipped with the deposit:

1. **shvvp_v0_8_1_phase_a_intervals.py** -- implementing PA-1, PA-2, PA-3 and the statistics of Section 2.4, with the deterministic seed interface.
2. **shvvp_v0_8_1_phase_a_m3.py** -- implementing the per-fact M3 vector, M3-FIRST, the paired difference, the censoring rule, and the tie-handling rule.
3. **test_shvvp_v0_8_1_phase_a.py** -- adversarial test suite covering:
   - Every PA-Z rule (PA-Z1 through PA-Z8), with at least one fixture per rule demonstrating the edge state and verifying the frozen handling;
   - The T2 computation on a hand-constructed shared set of 5 facts with known discovery times, verifying the median, relative gate, and interval against a reference computation;
   - The T3 computation on the same 5-fact set with known M4 scores;
   - The BCa-to-percentile fallback (PA-Z2, PA-Z5) on a 1-fact and a degenerate-jackknife fixture;
   - A censoring fixture where one condition's fact is censored at the budget, verifying the conservative direction;
   - A seed-reproducibility test: two runs with the same seed and data produce identical intervals;
   - A caller-supplied-statistic rejection test: a submitted pre-computed median or interval is rejected structurally, and only raw M3 vectors are accepted;
   - An input-validation test: non-numeric, negative, NaN, and infinity M3 values are rejected with PhasaAInputError, not silently coerced.

Text and code are the same rule written twice. A divergence between them is a defect in this amendment and must be raised as a finding, consistent with the v0.8 rule of Section 0.

---

## 5. What this amendment does NOT change

Explicitly recorded, because the append-only discipline requires it:

- No estimand attribute of any phase.
- No Phase B or Phase C rule, threshold, interval algorithm, corpus size, or label.
- No Phase A decision clause (A1-A6) or its Boolean structure. A2's domain and firing conditions are unchanged; the amendment makes A2 uniquely executable, not differently structured.
- No metric other than M3 (which is enriched from a scalar to a vector with a named scalar summary; the summary's value on any input is identical to the old M3's value).
- No threshold other than T2 (which is restated to be computable on the new M3 vector; the direction and magnitude of the gates are unchanged).
- No reliability threshold, no adjudication rule, no missing-data rule (except the new PA-Z rules, which fill a previously undefined space), no scope statement, no safety boundary, no anchor fact.
- No carrying-audit result. v0.8's carrying record is unaltered. This amendment requires its own two-family non-producer carrying audit before it can be deposited as FROZEN.

---

## 6. Carrying and deposit plan

This amendment follows the carrying rule inherited from v0.8:

1. The amendment text, the three executable artifacts, and the test suite are shipped as a candidate package.
2. Two non-producer carrying seats of different vendor families execute the canonical bytes, verify the test suite, recompute identity values, and attack the interval computation, the edge-state handling, and the BCa fallback paths.
3. Same-vendor seats count once. Producer-family review is advisory.
4. A HALT from either carrying seat blocks deposit and requires a new version.
5. Upon convergent non-HALT verdicts, the amendment is deposited as SHVVP v0.8.1, citing the parent v0.8 DOI and carrying the append-only amendment record.

The XZ Protocol's FREEZE-BLOCKER fields FB-1 and FB-2 are filled by referencing the deposited v0.8.1 DOI and the test-suite digest.

---

## 7. Amendment record entry (append-only)

**v0.8.1 (proposed, 2026-07-30): Phase A executability amendment.**

- **PA-A1 (from XZ Protocol FB-1 / GPT F-SOL-1).** ACCEPTED IN FULL. M3 is redefined as a per-fact discovery-time vector. M3-FIRST is the named scalar summary preserving the v0.8 scalar quantity. T2 is restated over the per-fact paired differences. The shared-set empty case is frozen as PA-Z1.
- **PA-A2 (from XZ Protocol FB-2 / GPT F-SOL-2).** ACCEPTED IN FULL. Phase A interval algorithms are frozen as PA-1 (resampling), PA-2 (BCa bounds), PA-3 (statistics), with eight degeneracy rules PA-Z1 through PA-Z8 covering every identified edge state. Phase A intervals are explicitly declared finite-corpus stability summaries, not population inferences, consistent with the frozen inferential-honesty clause of v0.8 Section 5.4.
- **PA-A3 (new; consequential edge state).** RECORDED. The empty-shared-set state (S = {}, PA-Z1) creates a new A2 edge: IDC > 0 but T2 and T3 are NOT-EVALUABLE, so A2 cannot fire. This is frozen as the intended behavior -- A2's domain requires shared facts, and its absence is a data limitation, not a design gap.
- **PA-A4 (scope of this amendment).** RECORDED. No Phase B or Phase C rule, no estimand, no decision-clause structure, no anchor fact, and no carrying record is altered. The amendment enriches one metric (M3) and specifies previously unspecified algorithms. It changes the computable content of T2 -- making it uniquely executable where it was previously ambiguous -- which is a SUBSTANTIVE change requiring a new version under the v0.8 Section 12 rule.

**Status:** PROPOSED. Not frozen, not carried, not deposited. Requires executable artifacts (Section 4) and two-family non-producer carrying audit (Section 6) before FROZEN status.

---

*Provenance.* Drafted by Bilal Syed Arfeen (BayyinahEnterprise) under the direction and analytical support of frontier language models as drafting instruments. This amendment has NOT undergone independent human peer review. It makes no effectiveness claim about BSSG, SHV, or any component of the Structural Honesty program.

*End of proposed SHVVP Phase A Amendment v0.8.1.*

---

# Bismillah ir-Rahman ir-Rahim
