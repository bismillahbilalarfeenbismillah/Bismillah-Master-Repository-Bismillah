# Bismillah ir-Rahman ir-Rahim

# R0338 -- SHVVP Phase A Amendment -- v0.8.4

**Chronological Index:** 390 of 995  
**Date:** 2026-07-31  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** shvvp_phase_a_amendment_v0_8_4.txt  
**Source Format:** txt  
**SHA-256:** `492f288f8cd522b9491cf4b7491f245b21de4bea1e4716d30d6f89530c8ff1ac`  

---

## R0338 · SHVVP Phase A Amendment -- v0.8.4

- section: V. BSSG & SHVVP Protocols
- source_file: shvvp_phase_a_amendment_v0_8_4.txt
- source_format: txt
- text_sha256: 492f288f8cd522b9491cf4b7491f245b21de4bea1e4716d30d6f89530c8ff1ac

# SHVVP Phase A Amendment -- v0.8.4

**Author of record:** Bilal Syed Arfeen (BayyinahEnterprise)
**Date:** 2026-07-31
**Status:** PROPOSED AMENDMENT -- NOT FROZEN, NOT CARRIED, NOT DEPOSITED
**Amends:** SHVVP v0.8 (doi:10.5281/zenodo.21583202), Sections 5.2, 5.3, and edge-state behavior of Section 5.4
**Supersedes:** v0.8.3 (HALTED), v0.8.2 (HALTED), v0.8.1 (HALTED)

## 0. Scope

This amendment touches Sections 5.2 (M3), 5.3 (T2, T5), and edge-state behavior of the Section 5.4 decision table. The code is the sole normative definition of the interval computation; this text describes the algorithm.

### 0.1 What changed from v0.8.3

1. M3Vector is frozen (immutable tuple). Mutation bypass closed permanently.
2. censor_status enum membership validated first. String bypass closed.
3. evidence_record_id: non-empty str required for OBSERVED; forbidden on non-discoveries.
4. M3 endpoint declared SUBSTANTIVE change from parent (PA-A12).
5. PA-Z4 scoped out of code (adjudication-layer). Count corrected to eleven code-level rules.
6. PA-Z13 added: non-finite ratios excluded and counted.
7. PA-Z14 added: BCa interval excluding its own point estimate -> percentile reversion.
8. Bool rejected uniformly at all numeric entry points.
9. Shape validation for T4/T7 tuples. Raw exceptions wrapped in PhaseAInputError.
10. caller_seed recorded on BootstrapResult; internal_seed separated.
11. BCa guard counters (n_bca_denom_guard, n_bca_level_clamp) on BootstrapResult.
12. PA-Z12 firing fixture shipped (Kimi's T7 fixture).
13. Golden vectors pinned for T2-abs, T3, T4, T7, PA-Z5, PA-Z10.
14. Provenance docstrings aligned with accident-guard.

## 1. M3 definition (Section 5.2)

M3 is a per-fact discovery-time vector. M3-FIRST is the observed-only scalar summary. S is the observed-shared set. See code module docstring for the SUBSTANTIVE ENDPOINT CHANGE (PA-A12).

M3Vector is a frozen dataclass with observations as a tuple. No mutation after construction. The with_obs() method returns a new vector. This closes the F-SOL-083-1 bypass permanently.

M3Observation validates censor_status as a CensorStatus enum member before any other check. String values (e.g. "OBSERVED") are rejected with PhaseAInputError. Evidence IDs are forbidden on RIGHT_CENSORED_BUDGET and CENSORED_EARLY; required as non-empty str on OBSERVED. OBSERVED minutes must be <= FROZEN_BUDGET_MINUTES (480.0).

### 1.1 At-480 boundary rule (disclosure)

At exactly 480.0 minutes, OBSERVED (with evidence) and RIGHT_CENSORED_BUDGET are both valid but carry opposite S-membership. The caller's enum choice governs. This is a disclosed boundary, not a bug.

### 1.2 n=1 vacuous gate (disclosure)

With |S|=1, PA-Z2 produces a zero-width interval. If the single delta is nonzero, excludes_zero is True and T2 can be satisfied on a single observation. This is a disclosed consequence of the point-interval semantics, not a bug. It is conservative: a single observation cannot drive a strong conclusion.

## 2. Interval algorithms (Section 5.3)

### 2.1 Code-level degeneracy rules

Eleven code-level rules: PA-Z1 through PA-Z3, PA-Z5 through PA-Z14.

PA-Z4 (alpha undefined / INDETERMINATE-ADJUDICATION) is an adjudication-layer rule outside these modules. It is tested at the adjudication layer.

| Rule | Condition | Handling |
|---|---|---|
| PA-Z1 | S empty | T2/T3 NOT-EVALUABLE |
| PA-Z2 | n=1 | Percentile reversion, zero-width |
| PA-Z3 | M7(A)=0 | T5 NOT-EVALUABLE |
| PA-Z5 | sum_sq=0, z0 valid | Percentile reversion |
| PA-Z6 | Single-index resample | Kept, counted (n_degenerate_resample) |
| PA-Z7 | T4 union-empty | M5 diff = 0, interval computed normally |
| PA-Z8 | T7 empty class | T7 returns None |
| PA-Z9 | All M3(f,A)=0 | Relative gate NOT-EVALUABLE |
| PA-Z10 | z0 undefined (prop_below in {0,1}) | Percentile reversion |
| PA-Z11 | NaN resamples | Counted, discarded (n_nan_resamples) |
| PA-Z12 | LOO NaN substitution | theta substituted, counted (n_loo_nan_substitutions) |
| PA-Z13 | Non-finite ratio (Delta/M3(f,A) overflows) | Excluded, counted (relative_nonfinite_count) |
| PA-Z14 | BCa interval excludes point estimate | Percentile reversion, excludes_zero=False |

### 2.2 BCa numerical guards (documented)

Two guards exist in the BCa computation. Both are documented and counted:
- _bca_q denominator within 1e-15 of zero: returns level 0.5 (n_bca_denom_guard)
- Adjusted percentile levels clamped to [0.5/n_valid, 1-0.5/n_valid] (n_bca_level_clamp)

### 2.3 PA-Z11 conditional-resampling (disclosure)

When NaN resamples are discarded, the reported interval is over the non-NaN resamples only. This is conditional on non-degeneracy. The conditioning is a consequence of the discard discipline.

### 2.4 PA-Z2/PA-Z11 zero-width semantics (disclosure)

PA-Z2 (n=1) sets excludes_zero = (theta != 0). PA-Z11 exhaustion (n_valid < 2) sets excludes_zero = False. The geometric situations are similar but the inferential meanings differ: PA-Z2 has a point estimate and no uncertainty; PA-Z11 has uncertainty but insufficient valid resamples to bound it. The difference is intentional.

## 3. T5 interval conjunct (PA-A5)

T5's "95 percent interval lower bound above 1.00" conjunct is retired. This is SUBSTANTIVE (see v0.8.2 amendment entry PA-A5).

## 4. Construction-evaluability guard (Section 5.4 edge state)

NOT-FALSIFIED requires that every clause whose domain was entered produced a determinate result. If A2's domain was entered (IDC > 0) but A2 could not evaluate (S empty), the Phase A result is NOT-EVALUABLE, not NOT-FALSIFIED. This is a prose rule tested at the adjudication layer alongside PA-Z4.

## 5. Provenance discipline

The provenance token on PairedDifference is an ACCIDENT GUARD against casual misuse. It is not a security boundary. dataclasses.replace() and direct token import can bypass it. The BSSG raw-evidence discipline is enforced at the protocol layer (adjudicators verify raw evidence references), not at this Python API layer. The T3 interface accepts caller-computed M4 differences without provenance; this is disclosed and accepted.

## 6. Normative artifacts

| File | SHA-256 | Role |
|---|---|---|
| shvvp_phase_a_amendment_v0_8_4.md | (this file) | Amendment text |
| shvvp_v0_8_4_phase_a_m3.py | fd1bd996... | M3 vector, S-membership, paired differences |
| shvvp_v0_8_4_phase_a_intervals.py | ff3a3801... | Intervals, PA-Z1-Z3/Z5-Z14, T2/T3/T4/T5/T7 |
| test_shvvp_v0_8_4_phase_a.py | b646429c... | 68-test adversarial suite |

Golden-vector environment: Python 3.12.3, numpy 2.4.4, scipy 1.17.1.

## 7. Amendment record (append-only)

PA-A1 through PA-A11: carried from v0.8.2/v0.8.3 (unchanged).

- **PA-A12 (v0.8.4): M3 endpoint SUBSTANTIVE change declared.** The parent v0.8 M3 ends at "first correctly adjudicated consequential fact." This implementation times to the first immutable saved evidence record that identifies the fact. The distinction is declared as a substantive endpoint change. No scalar-preservation claim is made for inputs where adjudication time differs from evidence time.
- **PA-A13 (v0.8.4): M3Vector frozen.** M3Vector is a frozen dataclass with observations as tuple. The mutation bypass (F-SOL-083-1) is closed permanently.
- **PA-A14 (v0.8.4): censor_status validation.** Enum membership is the first check. The string bypass (F-SOL-083-2) is closed permanently.
- **PA-A15 (v0.8.4): PA-Z4 scoped out.** PA-Z4 is an adjudication-layer rule. The code implements eleven code-level rules (PA-Z1-Z3, Z5-Z14). The "twelve rules" claims in v0.8.2/v0.8.3 are corrected.
- **PA-A16 (v0.8.4): PA-Z13 added.** Non-finite ratios from subnormal M3(f,A) are excluded and counted. The two-evaluator divergence on -inf ratios (F-K3-083-2) is resolved.
- **PA-A17 (v0.8.4): PA-Z14 added.** BCa interval excluding its own point estimate triggers percentile reversion. The unnamed numerical state (F-K3-083-1) is named.
- **PA-A18 (v0.8.4): Evidence-ID discipline.** Non-empty str required for OBSERVED; forbidden on non-discoveries. The falsy-evidence bypass (F-K3-083-11) is closed.

**Status:** PROPOSED. Not frozen, not carried, not deposited.

*Provenance.* Authored by Bilal Syed Arfeen (BayyinahEnterprise); prepared with frontier language models as drafting instruments. Not independently peer reviewed. No effectiveness claim about BSSG.

*End of proposed SHVVP Phase A Amendment v0.8.4.*

---

# Bismillah ir-Rahman ir-Rahim
