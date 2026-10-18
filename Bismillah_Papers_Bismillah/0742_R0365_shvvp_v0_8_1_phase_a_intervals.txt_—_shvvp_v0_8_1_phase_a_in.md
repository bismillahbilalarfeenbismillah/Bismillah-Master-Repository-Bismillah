# Bismillah ir-Rahman ir-Rahim

# R0365 -- shvvp_v0_8_1_phase_a_intervals.txt — shvvp_v0_8_1_phase_a_intervals.py -- Phase A BCa bootstrap intervals.

**Chronological Index:** 742 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** shvvp_v0_8_1_phase_a_intervals.txt  
**Source Format:** txt  
**SHA-256:** `af1a3f0b1b4a7f91229cd259881f9dea68f0b37482acc21b8330a33440410417`  

---

## R0365 · shvvp_v0_8_1_phase_a_intervals.txt — shvvp_v0_8_1_phase_a_intervals.py -- Phase A BCa bootstrap intervals.

- section: V. BSSG & SHVVP Protocols
- source_file: shvvp_v0_8_1_phase_a_intervals.txt
- source_format: txt
- text_sha256: af1a3f0b1b4a7f91229cd259881f9dea68f0b37482acc21b8330a33440410417

"""
shvvp_v0_8_1_phase_a_intervals.py -- Phase A BCa bootstrap intervals.

SHVVP v0.8.1 Phase A Amendment, Section 2.

Implements:
  PA-1 (resampling), PA-2 (BCa bounds), PA-3 (statistics).
  Degeneracy rules PA-Z1 through PA-Z8.

All intervals are FINITE-CORPUS STABILITY SUMMARIES, not population
confidence intervals. No population model is assumed. No hypothesis
test is performed. No p-value is computed.

Text and code are the same rule written twice. A divergence is a defect.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from enum import Enum
from typing import Callable, Optional

import numpy as np
from scipy import stats as scipy_stats

from shvvp_v0_8_1_phase_a_m3 import (
    PhaseAInputError,
    PairedDifference,
    compute_median,
)


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

N_BOOTSTRAP = 10_000
CONFIDENCE_LEVEL = 0.95
# BCa fallback thresholds
BCA_DEGENERATE_JACKKNIFE_WARN = 0.05   # >5% degenerate -> warn
BCA_DEGENERATE_JACKKNIFE_FALLBACK = 0.20  # >20% -> plain percentile


class IntervalMethod(Enum):
    BCA = "BCa"
    PERCENTILE = "PERCENTILE_FALLBACK"


@dataclass(frozen=True)
class BootstrapResult:
    """Result of a Phase A bootstrap interval computation."""
    point_estimate: float
    lower: float
    upper: float
    method: IntervalMethod
    n_resamples: int
    n_degenerate_jackknife: int
    n_degenerate_resample: int  # PA-Z6: all-identical resamples
    fallback_reason: Optional[str]
    seed: int
    excludes_zero: bool  # convenience: lower > 0 or upper < 0

    @property
    def is_fallback(self) -> bool:
        return self.method == IntervalMethod.PERCENTILE


# ---------------------------------------------------------------------------
# Core BCa implementation (PA-2)
# ---------------------------------------------------------------------------

def _bca_interval(
    data: np.ndarray,
    stat_func: Callable[[np.ndarray], float],
    rng: np.random.Generator,
    n_boot: int = N_BOOTSTRAP,
    alpha: float = 1.0 - CONFIDENCE_LEVEL,
) -> BootstrapResult:
    """Compute BCa bootstrap interval for a statistic.

    PA-2: bias correction z0, acceleration a from leave-one-out jackknife,
    BCa-adjusted percentile levels for two-sided interval.

    No smoothing, no variance stabilisation, no continuity correction.
    """
    n = len(data)
    if n == 0:
        raise PhaseAInputError("Cannot bootstrap empty data")

    theta = stat_func(data)
    seed_value = int(rng.integers(0, 2**31))

    # Bootstrap replicates
    boot_rng = np.random.default_rng(np.random.SeedSequence(seed_value))
    theta_star = np.empty(n_boot)
    n_degenerate_resample = 0
    for b in range(n_boot):
        indices = boot_rng.choice(n, size=n, replace=True)
        sample = data[indices]
        theta_star[b] = stat_func(sample)
        # PA-Z6: all-identical resample -> stat is the unique value
        if len(set(indices)) == 1:
            n_degenerate_resample += 1

    # Bias correction z0 (PA-2 step 1)
    prop_below = np.mean(theta_star < theta)
    if prop_below == 0.0:
        z0 = scipy_stats.norm.ppf(1.0 / (2.0 * n_boot))
    elif prop_below == 1.0:
        z0 = scipy_stats.norm.ppf(1.0 - 1.0 / (2.0 * n_boot))
    else:
        z0 = scipy_stats.norm.ppf(prop_below)

    # Acceleration a from leave-one-out jackknife (PA-2 step 2)
    jackknife_values = np.empty(n)
    n_degenerate_jackknife = 0
    for i in range(n):
        loo = np.delete(data, i)
        if len(loo) == 0:
            # PA-Z2: single observation -> jackknife undefined
            n_degenerate_jackknife += 1
            jackknife_values[i] = theta
        else:
            jackknife_values[i] = stat_func(loo)

    jack_mean = np.mean(jackknife_values)
    diffs = jack_mean - jackknife_values
    sum_sq = np.sum(diffs ** 2)
    sum_cu = np.sum(diffs ** 3)

    fallback_reason = None
    method = IntervalMethod.BCA

    # Check for degenerate jackknife
    degen_frac = n_degenerate_jackknife / n if n > 0 else 0.0

    if sum_sq == 0.0 or n == 1:
        # PA-Z2 / PA-Z5: jackknife is degenerate
        if n == 1:
            fallback_reason = "PA-Z2: single observation, jackknife undefined"
        else:
            fallback_reason = (
                f"Jackknife sum of squares is zero "
                f"({n_degenerate_jackknife}/{n} degenerate)"
            )
        method = IntervalMethod.PERCENTILE
    elif degen_frac > BCA_DEGENERATE_JACKKNIFE_FALLBACK:
        # PA-Z5: >20% degenerate -> plain percentile
        fallback_reason = (
            f"PA-Z5: {n_degenerate_jackknife}/{n} "
            f"({degen_frac:.1%}) degenerate jackknife values, "
            f"exceeds 20% threshold"
        )
        method = IntervalMethod.PERCENTILE
    elif degen_frac > BCA_DEGENERATE_JACKKNIFE_WARN:
        # PA-Z5: >5% but <=20% -> BCa with a=0 (BC only)
        a = 0.0
        fallback_reason = (
            f"PA-Z5: {n_degenerate_jackknife}/{n} "
            f"({degen_frac:.1%}) degenerate, acceleration set to 0"
        )
    else:
        # Normal BCa
        a = sum_cu / (6.0 * (sum_sq ** 1.5))

    if method == IntervalMethod.BCA:
        # BCa-adjusted percentile levels (PA-2 step 3)
        z_alpha_low = scipy_stats.norm.ppf(alpha / 2.0)
        z_alpha_high = scipy_stats.norm.ppf(1.0 - alpha / 2.0)

        # Adjusted levels
        def _bca_quantile(z_alpha_x):
            num = z0 + z_alpha_x
            denom = 1.0 - a * num
            if denom == 0.0:
                return 0.5  # degenerate
            adjusted_z = z0 + num / denom
            return scipy_stats.norm.cdf(adjusted_z)

        p_low = _bca_quantile(z_alpha_low)
        p_high = _bca_quantile(z_alpha_high)

        # Clamp to valid percentile range
        p_low = max(0.5 / n_boot, min(p_low, 1.0 - 0.5 / n_boot))
        p_high = max(0.5 / n_boot, min(p_high, 1.0 - 0.5 / n_boot))

        sorted_boot = np.sort(theta_star)
        lower = float(np.percentile(theta_star, p_low * 100))
        upper = float(np.percentile(theta_star, p_high * 100))
    else:
        # Plain percentile fallback
        lower = float(np.percentile(theta_star, (alpha / 2.0) * 100))
        upper = float(np.percentile(theta_star, (1.0 - alpha / 2.0) * 100))

    excludes_zero = (lower > 0.0) or (upper < 0.0)

    return BootstrapResult(
        point_estimate=theta,
        lower=lower,
        upper=upper,
        method=method,
        n_resamples=n_boot,
        n_degenerate_jackknife=n_degenerate_jackknife,
        n_degenerate_resample=n_degenerate_resample,
        fallback_reason=fallback_reason,
        seed=seed_value,
        excludes_zero=excludes_zero,
    )


# ---------------------------------------------------------------------------
# T2 interval (Section 2.4)
# ---------------------------------------------------------------------------

def t2_absolute_interval(
    paired_diffs: list[PairedDifference],
    seed: int,
) -> Optional[BootstrapResult]:
    """BCa interval for the median of Delta-M3 on the shared fact set.

    Returns None if S is empty (PA-Z1 -- caller should check first).
    """
    if not paired_diffs:
        return None  # PA-Z1

    deltas = np.array([pd.delta for pd in paired_diffs], dtype=np.float64)
    rng = np.random.default_rng(np.random.SeedSequence(seed))

    def median_stat(x):
        return float(np.median(x))

    return _bca_interval(deltas, median_stat, rng)


def t2_relative_interval(
    paired_diffs: list[PairedDifference],
    seed: int,
) -> Optional[BootstrapResult]:
    """BCa interval for the median of Delta-M3(f)/M3(f,A) on the
    shared set, excluding facts where M3(f,A) = 0.

    Returns None if no ratios exist (all M3(f,A) = 0 or S empty).
    """
    ratios = []
    for pd in paired_diffs:
        if pd.m3_a > 0:
            ratios.append(pd.delta / pd.m3_a)
    if not ratios:
        return None

    data = np.array(ratios, dtype=np.float64)
    rng = np.random.default_rng(np.random.SeedSequence(seed + 1))

    def median_stat(x):
        return float(np.median(x))

    return _bca_interval(data, median_stat, rng)


# ---------------------------------------------------------------------------
# T3 interval (Section 2.4)
# ---------------------------------------------------------------------------

def t3_interval(
    m4_diffs: list[float],
    seed: int,
) -> Optional[BootstrapResult]:
    """BCa interval for the mean of M4(B) - M4(A) on the shared set.

    m4_diffs: list of per-fact M4(f,B) - M4(f,A) differences.
    Returns None if empty (PA-Z1 applies to T3 as well).
    """
    if not m4_diffs:
        return None

    data = np.array(m4_diffs, dtype=np.float64)
    rng = np.random.default_rng(np.random.SeedSequence(seed + 2))

    def mean_stat(x):
        return float(np.mean(x))

    return _bca_interval(data, mean_stat, rng)


# ---------------------------------------------------------------------------
# T4 interval (Section 2.4)
# ---------------------------------------------------------------------------

def t4_interval(
    flag_pairs: list[tuple[int, int]],
    seed: int,
) -> Optional[BootstrapResult]:
    """BCa interval for M5(B) - M5(A).

    flag_pairs: list of (a_flagged, b_flagged) per artifact,
                where 1 = flagged, 0 = not flagged.
    Denominator: 200 declared-generated artifacts.

    Returns None if no artifacts.
    """
    if not flag_pairs:
        return None

    data = np.array(flag_pairs, dtype=np.float64)
    n_items = len(flag_pairs)
    rng = np.random.default_rng(np.random.SeedSequence(seed + 3))

    def fp_diff_stat(x):
        # x is (n, 2): column 0 = A flags, column 1 = B flags
        x = np.atleast_2d(x)
        rate_a = np.mean(x[:, 0])
        rate_b = np.mean(x[:, 1])
        return float(rate_b - rate_a)

    return _bca_interval(data, fp_diff_stat, rng)


# ---------------------------------------------------------------------------
# T7 interval (Section 2.4)
# ---------------------------------------------------------------------------

def t7_interval(
    discrim_pairs: list[tuple[int, int, int]],
    seed: int,
) -> Optional[BootstrapResult]:
    """BCa interval for M6(B) = balanced accuracy of B on discrimination set.

    discrim_pairs: list of (true_label, a_prediction, b_prediction)
                   where labels are 0 or 1.

    Returns None if M6(B) is not computable (PA-Z8).
    """
    if not discrim_pairs:
        return None

    data = np.array(discrim_pairs, dtype=np.float64)
    rng = np.random.default_rng(np.random.SeedSequence(seed + 4))

    def balanced_acc_b(x):
        true = x[:, 0]
        pred_b = x[:, 2]
        pos_mask = true == 1
        neg_mask = true == 0
        if pos_mask.sum() == 0 or neg_mask.sum() == 0:
            return float("nan")  # PA-Z8
        sensitivity = np.mean(pred_b[pos_mask] == 1)
        specificity = np.mean(pred_b[neg_mask] == 0)
        return float((sensitivity + specificity) / 2.0)

    # Check PA-Z8 on full data
    true_full = data[:, 0]
    if (true_full == 1).sum() == 0 or (true_full == 0).sum() == 0:
        return None  # PA-Z8: M6(B) not computable

    return _bca_interval(data, balanced_acc_b, rng)


# ---------------------------------------------------------------------------
# T5: NOT BOOTSTRAPPED (PA-Z3)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class T5Result:
    """T5 is a scalar ratio, not bootstrapped.

    M7(B)/M7(A). Two team pairs report separately; never pooled.
    PA-Z3: if M7(A) = 0, T5 is NOT-EVALUABLE.
    """
    m7_a: float
    m7_b: float
    ratio: Optional[float]
    evaluable: bool
    t5_fires: Optional[bool]  # ratio > 1.25
    rule: Optional[str]


def evaluate_t5(m7_a: float, m7_b: float) -> T5Result:
    """Evaluate T5 for one team pair."""
    if m7_a < 0 or m7_b < 0:
        raise PhaseAInputError(
            f"M7 values must be non-negative, got A={m7_a}, B={m7_b}"
        )
    if math.isnan(m7_a) or math.isnan(m7_b):
        raise PhaseAInputError("M7 values must not be NaN")

    if m7_a == 0.0:
        return T5Result(
            m7_a=m7_a, m7_b=m7_b, ratio=None,
            evaluable=False, t5_fires=None, rule="PA-Z3",
        )

    ratio = m7_b / m7_a
    return T5Result(
        m7_a=m7_a, m7_b=m7_b, ratio=ratio,
        evaluable=True,
        t5_fires=ratio > 1.25,
        rule=None,
    )


# ---------------------------------------------------------------------------
# Full T2 evaluation (point + interval)
# ---------------------------------------------------------------------------

@dataclass
class T2FullResult:
    """Complete T2 evaluation: point statistics and interval."""
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
    t2_satisfied: Optional[bool]  # all three sub-gates


def evaluate_t2_full(
    paired_diffs: list[PairedDifference],
    seed: int,
) -> T2FullResult:
    """Full T2 evaluation with point statistics and BCa intervals."""
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

    # Point statistics
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

    rel_median = compute_median(ratios) if ratios else None
    rel_gate = (rel_median >= 0.20) if rel_median is not None else None

    # Intervals
    abs_interval = t2_absolute_interval(paired_diffs, seed)
    rel_interval = t2_relative_interval(paired_diffs, seed)

    # T2 satisfied iff all three hold
    interval_excludes = (
        abs_interval.excludes_zero if abs_interval else None
    )
    if abs_gate and rel_gate and interval_excludes:
        t2_sat = True
    elif abs_gate is None or rel_gate is None or interval_excludes is None:
        t2_sat = None
    else:
        t2_sat = False

    return T2FullResult(
        evaluable=True, rule=None, shared_set_size=n,
        absolute_median=abs_median, absolute_gate_met=abs_gate,
        absolute_interval=abs_interval,
        relative_median=rel_median, relative_gate_met=rel_gate,
        relative_interval=rel_interval,
        relative_excluded_count=excluded,
        t2_satisfied=t2_sat,
    )

---

# Bismillah ir-Rahman ir-Rahim
