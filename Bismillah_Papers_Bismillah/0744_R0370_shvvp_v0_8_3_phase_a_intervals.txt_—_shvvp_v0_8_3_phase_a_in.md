# Bismillah ir-Rahman ir-Rahim

# R0370 -- shvvp_v0_8_3_phase_a_intervals.txt — shvvp_v0_8_3_phase_a_intervals.py -- Phase A BCa bootstrap intervals.

**Chronological Index:** 744 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** shvvp_v0_8_3_phase_a_intervals.txt  
**Source Format:** txt  
**SHA-256:** `358366c932d76a6add6eef425241ab94d23f886712e6bdb79c5595c9bb2bf880`  

---

## R0370 · shvvp_v0_8_3_phase_a_intervals.txt — shvvp_v0_8_3_phase_a_intervals.py -- Phase A BCa bootstrap intervals.

- section: V. BSSG & SHVVP Protocols
- source_file: shvvp_v0_8_3_phase_a_intervals.txt
- source_format: txt
- merged_variants: 1 (shvvp_v0_8_2_phase_a_intervals.txt)
- text_sha256: 358366c932d76a6add6eef425241ab94d23f886712e6bdb79c5595c9bb2bf880

"""
shvvp_v0_8_3_phase_a_intervals.py -- Phase A BCa bootstrap intervals.

SHVVP v0.8.3 Phase A Amendment, Section 2.

THE CODE IS THE SOLE NORMATIVE DEFINITION of the interval computation.
Golden-vector receipts in the test suite pin exact numerical outputs
for every statistic and fallback path under the pinned dependency
versions below. A dependency upgrade that changes PRNG streams or
percentile interpolation will fail the golden-vector tests.

Pinned: Python 3.12.x, numpy 2.4.x, scipy 1.17.x.
Percentile interpolation: numpy default ('linear').

Degeneracy rules: PA-Z1 through PA-Z12 (twelve rules).

BCa numerical guards (documented, not silent):
  - _bca_q denom within 1e-15 of zero -> returns level 0.5 (latent guard)
  - Adjusted percentile levels clamped to [0.5/n_valid, 1-0.5/n_valid]
    to avoid out-of-range percentile queries (boundary guard)

Intervals are FINITE-CORPUS STABILITY SUMMARIES, not population
confidence intervals.

The provenance token on PairedDifference is an ACCIDENT GUARD,
not a security boundary (see m3 module docstring).
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from enum import Enum
from typing import Optional

import numpy as np
from scipy import stats as scipy_stats

from shvvp_v0_8_3_phase_a_m3 import (
    PhaseAInputError,
    PairedDifference,
    compute_median,
)


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

N_BOOTSTRAP = 10_000
CONFIDENCE_LEVEL = 0.95
T4_CORPUS_SIZE = 200
T7_CORPUS_SIZE = 240


class IntervalMethod(Enum):
    BCA = "BCa"
    PERCENTILE = "PERCENTILE_FALLBACK"


def _validate_seed(seed: int) -> None:
    """Validate seed is a non-negative integer (F-K3-N18)."""
    if isinstance(seed, bool):
        raise PhaseAInputError(f"Seed must be int, got bool")
    if not isinstance(seed, int):
        raise PhaseAInputError(f"Seed must be int, got {type(seed).__name__}")
    if seed < 0:
        raise PhaseAInputError(f"Seed must be non-negative, got {seed}")


@dataclass(frozen=True)
class BootstrapResult:
    """Result of a Phase A bootstrap interval computation."""
    point_estimate: float
    lower: float
    upper: float
    method: IntervalMethod
    n_resamples: int
    n_valid_resamples: int  # after NaN discard
    n_nan_resamples: int   # PA-Z11
    n_degenerate_resample: int  # PA-Z6: all-identical resamples, kept
    n_loo_nan_substitutions: int  # PA-Z12: LOO NaN -> theta substitutions
    fallback_reason: Optional[str]
    seed: int
    excludes_zero: bool

    @property
    def is_fallback(self) -> bool:
        return self.method == IntervalMethod.PERCENTILE


# ---------------------------------------------------------------------------
# Core BCa (PA-2), with all fallback paths declared and named
# ---------------------------------------------------------------------------

def _bca_interval(
    data: np.ndarray,
    stat_func,
    seed: int,
    n_boot: int = N_BOOTSTRAP,
    alpha: float = 1.0 - CONFIDENCE_LEVEL,
    multidim: bool = False,
) -> BootstrapResult:
    """BCa bootstrap interval.

    multidim: if True, data is 2-D and jackknife/resampling operate
    on rows (axis=0). If False, data is 1-D.

    Degeneracy cascade:
      n=1 -> PA-Z2 (before bootstrap)
      NaN resamples -> PA-Z11 (counted, discarded)
      prop_below in {0,1} -> PA-Z10 (percentile reversion)
      sum_sq == 0 -> PA-Z5 (percentile reversion)
      All-identical resample -> PA-Z6 (kept, counted)
      LOO NaN -> PA-Z12 (substituted with theta, counted)
      BCa denom near zero -> documented boundary guard
      Adjusted levels clamped -> documented boundary guard
    """
    _validate_seed(seed)
    n = len(data)
    if n == 0:
        raise PhaseAInputError("Cannot bootstrap empty data")

    theta = float(stat_func(data))
    if math.isnan(theta) or math.isinf(theta):
        raise PhaseAInputError(
            f"Statistic on full data is {theta}; non-finite input rejected"
        )

    # PA-Z2: n=1 -> percentile fallback immediately
    if n == 1:
        return BootstrapResult(
            point_estimate=theta, lower=theta, upper=theta,
            method=IntervalMethod.PERCENTILE,
            n_resamples=0, n_valid_resamples=0,
            n_nan_resamples=0, n_degenerate_resample=0,
            n_loo_nan_substitutions=0,
            fallback_reason="PA-Z2: single observation; "
                           "declared percentile reversion",
            seed=seed, excludes_zero=(theta != 0.0),
        )

    rng = np.random.default_rng(np.random.SeedSequence(seed))

    # Bootstrap replicates
    theta_star_raw = np.empty(n_boot)
    n_degenerate = 0  # PA-Z6: all-identical resamples, kept
    for b in range(n_boot):
        indices = rng.choice(n, size=n, replace=True)
        if multidim:
            sample = data[indices, :]
        else:
            sample = data[indices]
        theta_star_raw[b] = stat_func(sample)
        if len(set(indices)) == 1:
            n_degenerate += 1  # PA-Z6: counted, not discarded

    # PA-Z11: NaN resamples counted, discarded, reported
    nan_mask = np.isnan(theta_star_raw)
    n_nan = int(nan_mask.sum())
    theta_star = theta_star_raw[~nan_mask]
    n_valid = len(theta_star)

    if n_valid < 2:
        return BootstrapResult(
            point_estimate=theta, lower=theta, upper=theta,
            method=IntervalMethod.PERCENTILE,
            n_resamples=n_boot, n_valid_resamples=n_valid,
            n_nan_resamples=n_nan, n_degenerate_resample=n_degenerate,
            n_loo_nan_substitutions=0,
            fallback_reason=f"PA-Z11: only {n_valid} valid resamples "
                           f"({n_nan} NaN discarded)",
            seed=seed, excludes_zero=False,
        )

    # Bias correction z0 (PA-2 step 1)
    prop_below = float(np.mean(theta_star < theta))

    fallback_reason = None
    method = IntervalMethod.BCA
    n_loo_nan = 0  # PA-Z12 counter

    # PA-Z10: z0-undefined
    if prop_below == 0.0 or prop_below == 1.0:
        fallback_reason = (
            f"PA-Z10: z0 undefined (prop_below={prop_below}); "
            f"declared percentile reversion"
        )
        method = IntervalMethod.PERCENTILE

    if method == IntervalMethod.BCA:
        z0 = float(scipy_stats.norm.ppf(prop_below))

        # Jackknife acceleration (PA-2 step 2)
        jackknife_values = np.empty(n)
        for i in range(n):
            if multidim:
                loo = np.delete(data, i, axis=0)
            else:
                loo = np.delete(data, i)
            if len(loo) == 0:
                jackknife_values[i] = theta
                n_loo_nan += 1  # PA-Z12
            else:
                jv = stat_func(loo)
                if math.isnan(jv):
                    jackknife_values[i] = theta  # PA-Z12: LOO NaN -> theta
                    n_loo_nan += 1
                else:
                    jackknife_values[i] = jv

        jack_mean = float(np.mean(jackknife_values))
        diffs = jack_mean - jackknife_values
        sum_sq = float(np.sum(diffs ** 2))
        sum_cu = float(np.sum(diffs ** 3))

        # PA-Z5: acceleration undefined when sum_sq == 0
        if sum_sq == 0.0:
            if n == 1:
                fallback_reason = (
                    "PA-Z2: single observation; jackknife undefined; "
                    "declared percentile reversion"
                )
            else:
                fallback_reason = (
                    f"PA-Z5: jackknife sum of squares is zero (n={n}); "
                    f"acceleration undefined; declared percentile reversion"
                )
            method = IntervalMethod.PERCENTILE
        else:
            a = sum_cu / (6.0 * (sum_sq ** 1.5))

    if method == IntervalMethod.BCA:
        # BCa-adjusted percentile levels (PA-2 step 3)
        z_lo = float(scipy_stats.norm.ppf(alpha / 2.0))
        z_hi = float(scipy_stats.norm.ppf(1.0 - alpha / 2.0))

        def _bca_q(z_alpha):
            num = z0 + z_alpha
            denom = 1.0 - a * num
            # Documented boundary guard: near-zero denom -> level 0.5
            if abs(denom) < 1e-15:
                return 0.5
            adjusted_z = z0 + num / denom
            return float(scipy_stats.norm.cdf(adjusted_z))

        p_low = _bca_q(z_lo)
        p_high = _bca_q(z_hi)
        # Documented boundary guard: clamp to valid percentile range
        p_low = max(0.5 / n_valid, min(p_low, 1.0 - 0.5 / n_valid))
        p_high = max(0.5 / n_valid, min(p_high, 1.0 - 0.5 / n_valid))

        lower = float(np.percentile(theta_star, p_low * 100))
        upper = float(np.percentile(theta_star, p_high * 100))
    else:
        # Plain percentile fallback
        lower = float(np.percentile(theta_star, (alpha / 2.0) * 100))
        upper = float(np.percentile(theta_star, (1.0 - alpha / 2.0) * 100))

    excludes_zero = (lower > 0.0) or (upper < 0.0)

    return BootstrapResult(
        point_estimate=theta, lower=lower, upper=upper,
        method=method,
        n_resamples=n_boot, n_valid_resamples=n_valid,
        n_nan_resamples=n_nan, n_degenerate_resample=n_degenerate,
        n_loo_nan_substitutions=n_loo_nan,
        fallback_reason=fallback_reason,
        seed=seed, excludes_zero=excludes_zero,
    )

# ---------------------------------------------------------------------------
# T2 intervals
# ---------------------------------------------------------------------------

def t2_absolute_interval(
    paired_diffs: list[PairedDifference],
    seed: int,
) -> Optional[BootstrapResult]:
    """BCa interval for median of Delta-M3 on the shared set.
    Returns None if S is empty (PA-Z1)."""
    _validate_seed(seed)
    if not paired_diffs:
        return None
    for pd in paired_diffs:
        pd.verify_provenance()
    deltas = np.array([pd.delta for pd in paired_diffs], dtype=np.float64)

    def median_stat(x):
        return float(np.median(x))

    return _bca_interval(deltas, median_stat, seed)


def t2_relative_interval(
    paired_diffs: list[PairedDifference],
    seed: int,
) -> Optional[BootstrapResult]:
    """BCa interval for median of Delta-M3(f)/M3(f,A), excluding M3(f,A)=0.
    Returns None if no ratios exist (PA-Z9)."""
    _validate_seed(seed)
    ratios = []
    for pd in paired_diffs:
        pd.verify_provenance()
        if pd.m3_a > 0:
            ratios.append(pd.delta / pd.m3_a)
    if not ratios:
        return None
    data = np.array(ratios, dtype=np.float64)

    def median_stat(x):
        return float(np.median(x))

    return _bca_interval(data, median_stat, seed + 1)


# ---------------------------------------------------------------------------
# T3 interval
# ---------------------------------------------------------------------------

def t3_interval(
    m4_diffs: list[float],
    seed: int,
) -> Optional[BootstrapResult]:
    """BCa interval for mean of M4(B)-M4(A) on shared set.
    Returns None if empty. Rejects NaN/Inf (F-SOL-081-6)."""
    _validate_seed(seed)
    if not m4_diffs:
        return None
    for i, v in enumerate(m4_diffs):
        if not isinstance(v, (int, float)) or math.isnan(v) or math.isinf(v):
            raise PhaseAInputError(
                f"M4 difference at index {i} is {v!r}; "
                f"non-finite values rejected"
            )
    data = np.array(m4_diffs, dtype=np.float64)

    def mean_stat(x):
        return float(np.mean(x))

    return _bca_interval(data, mean_stat, seed + 2)


# ---------------------------------------------------------------------------
# T4 interval -- exactly 200 items (F-K3-B7)
# ---------------------------------------------------------------------------

def t4_interval(
    flag_pairs: list[tuple[int, int]],
    seed: int,
) -> Optional[BootstrapResult]:
    """BCa interval for M5(B) - M5(A).
    flag_pairs: (a_flagged, b_flagged) per artifact, 0 or 1.
    MUST be exactly 200 items (F-K3-B7). Empty = wrong cardinality."""
    _validate_seed(seed)
    if len(flag_pairs) != T4_CORPUS_SIZE:
        raise PhaseAInputError(
            f"T4 requires exactly {T4_CORPUS_SIZE} artifacts, "
            f"got {len(flag_pairs)}"
        )
    for i, (a, b) in enumerate(flag_pairs):
        if isinstance(a, bool) or isinstance(b, bool):
            raise PhaseAInputError(
                f"T4 flags must be int 0 or 1 (not bool) at index {i}"
            )
        if a not in (0, 1) or b not in (0, 1):
            raise PhaseAInputError(
                f"T4 flags must be 0 or 1 at index {i}, got ({a}, {b})"
            )

    data = np.array(flag_pairs, dtype=np.float64)

    def fp_diff_stat(x):
        x = np.atleast_2d(x)
        return float(np.mean(x[:, 1]) - np.mean(x[:, 0]))

    return _bca_interval(data, fp_diff_stat, seed + 3, multidim=True)


# ---------------------------------------------------------------------------
# T7 interval -- exactly 240 items (F-K3-B7)
# ---------------------------------------------------------------------------

def t7_interval(
    discrim_triples: list[tuple[int, int, int]],
    seed: int,
) -> Optional[BootstrapResult]:
    """BCa interval for M6(B) = balanced accuracy of B.
    discrim_triples: (true_label, a_pred, b_pred), all 0 or 1.
    MUST be exactly 240 items. Empty = wrong cardinality. Returns None if PA-Z8."""
    _validate_seed(seed)
    if len(discrim_triples) != T7_CORPUS_SIZE:
        raise PhaseAInputError(
            f"T7 requires exactly {T7_CORPUS_SIZE} items, "
            f"got {len(discrim_triples)}"
        )
    for i, (t, a, b) in enumerate(discrim_triples):
        if isinstance(t, bool) or isinstance(a, bool) or isinstance(b, bool):
            raise PhaseAInputError(
                f"T7 labels must be int 0 or 1 (not bool) at index {i}"
            )
        if t not in (0, 1) or a not in (0, 1) or b not in (0, 1):
            raise PhaseAInputError(
                f"T7 labels must be 0 or 1 at index {i}, got ({t}, {a}, {b})"
            )

    data = np.array(discrim_triples, dtype=np.float64)

    # PA-Z8 check on full data
    true_full = data[:, 0]
    n_pos = int((true_full == 1).sum())
    n_neg = int((true_full == 0).sum())
    if n_pos == 0 or n_neg == 0:
        return None

    def balanced_acc_b(x):
        x = np.atleast_2d(x)
        true = x[:, 0]
        pred_b = x[:, 2]
        pos_mask = true == 1
        neg_mask = true == 0
        if pos_mask.sum() == 0 or neg_mask.sum() == 0:
            return float("nan")  # will be caught by PA-Z11
        sensitivity = float(np.mean(pred_b[pos_mask] == 1))
        specificity = float(np.mean(pred_b[neg_mask] == 0))
        return (sensitivity + specificity) / 2.0

    return _bca_interval(data, balanced_acc_b, seed + 4, multidim=True)


# ---------------------------------------------------------------------------
# T5: NOT BOOTSTRAPPED -- interval conjunct formally retired (F-K3-C1)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class T5Result:
    """T5 evaluation. The interval conjunct is formally retired by
    amendment PA-A5: Phase A has no T5 resampling unit (two team pairs,
    never pooled; the inferential-honesty clause gives no population
    model). This is a DECLARED SUBSTANTIVE CHANGE to T5, recorded in
    the amendment record -- not a silent deletion.

    PA-Z3: if M7(A) = 0, T5 is NOT-EVALUABLE.
    """
    m7_a: float
    m7_b: float
    ratio: Optional[float]
    evaluable: bool
    t5_fires: Optional[bool]
    rule: Optional[str]


def evaluate_t5(m7_a: float, m7_b: float) -> T5Result:
    """Evaluate T5 for one team pair. Point ratio only (PA-A5)."""
    if not isinstance(m7_a, (int, float)) or not isinstance(m7_b, (int, float)):
        raise PhaseAInputError(f"M7 values must be numeric")
    if math.isnan(m7_a) or math.isnan(m7_b):
        raise PhaseAInputError("M7 values must not be NaN")
    if math.isinf(m7_a) or math.isinf(m7_b):
        raise PhaseAInputError("M7 values must not be infinite")
    if m7_a < 0 or m7_b < 0:
        raise PhaseAInputError(
            f"M7 values must be non-negative, got A={m7_a}, B={m7_b}"
        )
    if m7_a == 0.0:
        return T5Result(
            m7_a=m7_a, m7_b=m7_b, ratio=None,
            evaluable=False, t5_fires=None, rule="PA-Z3",
        )
    ratio = m7_b / m7_a
    return T5Result(
        m7_a=m7_a, m7_b=m7_b, ratio=ratio,
        evaluable=True, t5_fires=ratio > 1.25, rule=None,
    )


# ---------------------------------------------------------------------------
# Full T2 evaluation
# ---------------------------------------------------------------------------

@dataclass
class T2FullResult:
    evaluable: bool
    rule: Optional[str]
    shared_set_size: int
    absolute_median: Optional[float]
    absolute_gate_met: Optional[bool]
    absolute_interval: Optional[BootstrapResult]
    relative_median: Optional[float]
    relative_gate_met: Optional[bool]
    relative_interval: Optional[BootstrapResult]
    relative_excluded_count: int
    t2_satisfied: Optional[bool]


def evaluate_t2_full(
    paired_diffs: list[PairedDifference],
    seed: int,
) -> T2FullResult:
    """Full T2 evaluation with provenance verification."""
    for pd in paired_diffs:
        pd.verify_provenance()

    n = len(paired_diffs)
    if n == 0:
        return T2FullResult(
            evaluable=False, rule="PA-Z1", shared_set_size=0,
            absolute_median=None, absolute_gate_met=None,
            absolute_interval=None,
            relative_median=None, relative_gate_met=None,
            relative_interval=None,
            relative_excluded_count=0, t2_satisfied=None,
        )

    deltas = [pd.delta for pd in paired_diffs]
    abs_median = compute_median(deltas)
    abs_gate = abs_median >= 30.0

    ratios = []
    excluded = 0
    for pd in paired_diffs:
        if pd.m3_a > 0:
            ratios.append(pd.delta / pd.m3_a)
        else:
            excluded += 1

    if not ratios:
        # PA-Z9: all-zero relative gate
        return T2FullResult(
            evaluable=False, rule="PA-Z9", shared_set_size=n,
            absolute_median=abs_median, absolute_gate_met=abs_gate,
            absolute_interval=t2_absolute_interval(paired_diffs, seed),
            relative_median=None, relative_gate_met=None,
            relative_interval=None,
            relative_excluded_count=excluded, t2_satisfied=None,
        )

    rel_median = compute_median(ratios)
    rel_gate = rel_median >= 0.20

    abs_interval = t2_absolute_interval(paired_diffs, seed)
    rel_interval = t2_relative_interval(paired_diffs, seed)

    interval_excludes = abs_interval.excludes_zero if abs_interval else None

    if all(x is not None and x for x in [abs_gate, rel_gate, interval_excludes]):
        t2_sat = True
    elif any(x is not None and not x for x in [abs_gate, rel_gate, interval_excludes]):
        t2_sat = False
    else:
        t2_sat = None

    return T2FullResult(
        evaluable=True, rule=None, shared_set_size=n,
        absolute_median=abs_median, absolute_gate_met=abs_gate,
        absolute_interval=abs_interval,
        relative_median=rel_median, relative_gate_met=rel_gate,
        relative_interval=rel_interval,
        relative_excluded_count=excluded, t2_satisfied=t2_sat,
    )

---

# Bismillah ir-Rahman ir-Rahim
