# Bismillah ir-Rahman ir-Rahim

# R0373 -- shvvp_v0_8_4_phase_a_intervals.txt — shvvp_v0_8_4_phase_a_intervals.py -- Phase A BCa bootstrap intervals.

**Chronological Index:** 746 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** shvvp_v0_8_4_phase_a_intervals.txt  
**Source Format:** txt  
**SHA-256:** `82eb117656a5954b8f31ab8e650ab820551f141fd6481952089547e883532b7c`  

---

## R0373 · shvvp_v0_8_4_phase_a_intervals.txt — shvvp_v0_8_4_phase_a_intervals.py -- Phase A BCa bootstrap intervals.

- section: V. BSSG & SHVVP Protocols
- source_file: shvvp_v0_8_4_phase_a_intervals.txt
- source_format: txt
- merged_variants: 2 (xz_protocol_phase_a_intervals.py; xz_protocol_phase_a_intervals.py.txt)
- text_sha256: 82eb117656a5954b8f31ab8e650ab820551f141fd6481952089547e883532b7c

"""
shvvp_v0_8_4_phase_a_intervals.py -- Phase A BCa bootstrap intervals.

SHVVP v0.8.4 Phase A Amendment, Section 2.

THE CODE IS THE SOLE NORMATIVE DEFINITION of the interval computation.
Golden-vector receipts in the test suite pin exact numerical outputs.

Code-level degeneracy rules: PA-Z1 through PA-Z3, PA-Z5 through PA-Z14
(eleven rules). PA-Z4 (alpha undefined / INDETERMINATE-ADJUDICATION) is
an adjudication-layer rule outside these modules; it is scoped out of
the code and tested at the adjudication layer.

BCa numerical guards (documented, not silent):
  _bca_q denom within 1e-15 of zero -> returns level 0.5
    (n_bca_denom_guard incremented)
  Adjusted percentile levels clamped to [0.5/n_valid, 1-0.5/n_valid]
    (n_bca_level_clamp incremented)

PA-Z14 (new in v0.8.4): BCa interval excludes its own point estimate
  -> declared percentile reversion.

Intervals are FINITE-CORPUS STABILITY SUMMARIES, not population CIs.

Provenance token is an ACCIDENT GUARD (see m3 module docstring).

Pinned golden-vector environment: numpy 2.4.4, scipy 1.17.1.
Percentile method: numpy default ('linear').
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from enum import Enum
from typing import Optional

import numpy as np
from scipy import stats as scipy_stats

from shvvp_v0_8_4_phase_a_m3 import (
    PhaseAInputError, PairedDifference, compute_median, _reject_bool,
)

N_BOOTSTRAP = 10_000
CONFIDENCE_LEVEL = 0.95
T4_CORPUS_SIZE = 200
T7_CORPUS_SIZE = 240


class IntervalMethod(Enum):
    BCA = "BCa"
    PERCENTILE = "PERCENTILE_FALLBACK"


def _validate_seed(seed: int) -> None:
    _reject_bool(seed, "Seed")
    if not isinstance(seed, int):
        raise PhaseAInputError(f"Seed must be int, got {type(seed).__name__}")
    if seed < 0:
        raise PhaseAInputError(f"Seed must be non-negative, got {seed}")


@dataclass(frozen=True)
class BootstrapResult:
    point_estimate: float
    lower: float
    upper: float
    method: IntervalMethod
    n_resamples: int
    n_valid_resamples: int
    n_nan_resamples: int          # PA-Z11
    n_degenerate_resample: int    # PA-Z6: single-index resamples, kept
    n_loo_nan_substitutions: int  # PA-Z12
    n_bca_denom_guard: int        # documented guard
    n_bca_level_clamp: int        # documented guard
    fallback_reason: Optional[str]
    caller_seed: int              # the seed the caller passed
    internal_seed: int            # the offset-adjusted seed used
    excludes_zero: bool
    point_in_interval: bool       # PA-Z14 check

    @property
    def is_fallback(self) -> bool:
        return self.method == IntervalMethod.PERCENTILE


def _make_result(*, point, lower, upper, method, n_resamples, n_valid,
                 n_nan, n_degen, n_loo_nan, n_denom_guard, n_level_clamp,
                 reason, caller_seed, internal_seed) -> BootstrapResult:
    excludes = (lower > 0.0) or (upper < 0.0)
    p_in = (lower <= point <= upper)
    # PA-Z14: if BCa and point not in interval, revert to percentile
    if method == IntervalMethod.BCA and not p_in:
        # This is a named state, not silent
        method = IntervalMethod.PERCENTILE
        reason = (f"PA-Z14: BCa interval [{lower},{upper}] excludes "
                  f"point estimate {point}; declared percentile reversion")
        # Recalculate with the _stored_ bootstrap replicates? No -- we
        # flag and report. The interval bounds remain as computed but the
        # method is marked PERCENTILE and excludes_zero is re-evaluated
        # conservatively as False (the BCa correction is unreliable).
        excludes = False
        p_in = False
    return BootstrapResult(
        point_estimate=point, lower=lower, upper=upper, method=method,
        n_resamples=n_resamples, n_valid_resamples=n_valid,
        n_nan_resamples=n_nan, n_degenerate_resample=n_degen,
        n_loo_nan_substitutions=n_loo_nan,
        n_bca_denom_guard=n_denom_guard, n_bca_level_clamp=n_level_clamp,
        fallback_reason=reason, caller_seed=caller_seed,
        internal_seed=internal_seed, excludes_zero=excludes,
        point_in_interval=p_in)


def _bca_interval(data, stat_func, caller_seed, internal_seed,
                  n_boot=N_BOOTSTRAP, alpha=1.0-CONFIDENCE_LEVEL,
                  multidim=False):
    _validate_seed(caller_seed)
    n = len(data)
    if n == 0:
        raise PhaseAInputError("Cannot bootstrap empty data")

    theta = float(stat_func(data))
    if not math.isfinite(theta):
        raise PhaseAInputError(f"Statistic on full data is {theta}")

    common = dict(n_nan=0, n_degen=0, n_loo_nan=0, n_denom_guard=0,
                  n_level_clamp=0, caller_seed=caller_seed,
                  internal_seed=internal_seed)

    if n == 1:
        return _make_result(point=theta, lower=theta, upper=theta,
                            method=IntervalMethod.PERCENTILE,
                            n_resamples=0, n_valid=0,
                            reason="PA-Z2: single observation", **common)

    rng = np.random.default_rng(np.random.SeedSequence(internal_seed))

    theta_star_raw = np.empty(n_boot)
    n_degen = 0
    for b in range(n_boot):
        idx = rng.choice(n, size=n, replace=True)
        sample = data[idx, :] if multidim else data[idx]
        theta_star_raw[b] = stat_func(sample)
        if len(set(idx)) == 1:
            n_degen += 1  # PA-Z6

    nan_mask = np.isnan(theta_star_raw)
    n_nan = int(nan_mask.sum())
    theta_star = theta_star_raw[~nan_mask]
    n_valid = len(theta_star)
    common.update(n_nan=n_nan, n_degen=n_degen)

    if n_valid < 2:
        return _make_result(point=theta, lower=theta, upper=theta,
                            method=IntervalMethod.PERCENTILE,
                            n_resamples=n_boot, n_valid=n_valid,
                            reason=f"PA-Z11: {n_valid} valid ({n_nan} NaN)",
                            **common)

    prop_below = float(np.mean(theta_star < theta))
    method = IntervalMethod.BCA
    reason = None
    n_denom_guard = 0
    n_level_clamp = 0

    if prop_below == 0.0 or prop_below == 1.0:
        reason = f"PA-Z10: z0 undefined (prop_below={prop_below})"
        method = IntervalMethod.PERCENTILE

    if method == IntervalMethod.BCA:
        z0 = float(scipy_stats.norm.ppf(prop_below))

        jk = np.empty(n)
        n_loo_nan = 0
        for i in range(n):
            loo = np.delete(data, i, axis=0) if multidim else np.delete(data, i)
            jv = stat_func(loo)
            if math.isnan(jv):
                jk[i] = theta  # PA-Z12
                n_loo_nan += 1
            else:
                jk[i] = jv
        common['n_loo_nan'] = n_loo_nan

        jm = float(np.mean(jk))
        diffs = jm - jk
        sum_sq = float(np.sum(diffs**2))

        if sum_sq == 0.0:
            reason = f"PA-Z5: sum_sq=0 (n={n})"
            method = IntervalMethod.PERCENTILE
        else:
            a = float(np.sum(diffs**3)) / (6.0 * sum_sq**1.5)

    if method == IntervalMethod.BCA:
        z_lo = float(scipy_stats.norm.ppf(alpha / 2.0))
        z_hi = float(scipy_stats.norm.ppf(1.0 - alpha / 2.0))

        def _bca_q(z_alpha):
            nonlocal n_denom_guard
            num = z0 + z_alpha
            denom = 1.0 - a * num
            if abs(denom) < 1e-15:
                n_denom_guard += 1
                return 0.5
            return float(scipy_stats.norm.cdf(z0 + num / denom))

        p_lo, p_hi = _bca_q(z_lo), _bca_q(z_hi)
        lo_before, hi_before = p_lo, p_hi
        p_lo = max(0.5/n_valid, min(p_lo, 1.0-0.5/n_valid))
        p_hi = max(0.5/n_valid, min(p_hi, 1.0-0.5/n_valid))
        if p_lo != lo_before or p_hi != hi_before:
            n_level_clamp += 1

        lower = float(np.percentile(theta_star, p_lo*100))
        upper = float(np.percentile(theta_star, p_hi*100))
    else:
        lower = float(np.percentile(theta_star, (alpha/2.0)*100))
        upper = float(np.percentile(theta_star, (1.0-alpha/2.0)*100))

    common.update(n_denom_guard=n_denom_guard, n_level_clamp=n_level_clamp)
    return _make_result(point=theta, lower=lower, upper=upper, method=method,
                        n_resamples=n_boot, n_valid=n_valid, reason=reason,
                        **common)


# === T2 ===

def t2_absolute_interval(pds, seed):
    _validate_seed(seed)
    if not pds: return None
    for pd in pds: pd.verify_provenance()
    d = np.array([pd.delta for pd in pds], dtype=np.float64)
    return _bca_interval(d, lambda x: float(np.median(x)), seed, seed)

def t2_relative_interval(pds, seed):
    _validate_seed(seed)
    ratios = []
    for pd in pds:
        pd.verify_provenance()
        if pd.m3_a != 0:
            r = pd.delta / pd.m3_a
            if math.isfinite(r):
                ratios.append(r)
    if not ratios: return None
    d = np.array(ratios, dtype=np.float64)
    return _bca_interval(d, lambda x: float(np.median(x)), seed, seed+1)


# === T3 ===

def t3_interval(m4_diffs, seed):
    _validate_seed(seed)
    if not m4_diffs: return None
    for i, v in enumerate(m4_diffs):
        _reject_bool(v, f"M4 diff[{i}]")
        try:
            fv = float(v)
        except (TypeError, ValueError, OverflowError) as e:
            raise PhaseAInputError(f"M4 diff[{i}] invalid: {e}") from e
        if not math.isfinite(fv):
            raise PhaseAInputError(f"M4 diff[{i}] is {fv}")
    d = np.array(m4_diffs, dtype=np.float64)
    return _bca_interval(d, lambda x: float(np.mean(x)), seed, seed+2)


# === T4 ===

def _validate_binary_int(val, name):
    _reject_bool(val, name)
    if type(val) is not int:
        raise PhaseAInputError(f"{name} must be int, got {type(val).__name__}")
    if val not in (0, 1):
        raise PhaseAInputError(f"{name} must be 0 or 1, got {val}")

def t4_interval(flag_pairs, seed):
    """Exactly 200 items. PA-Z7: union-empty is natural zero-diff."""
    _validate_seed(seed)
    if len(flag_pairs) != T4_CORPUS_SIZE:
        raise PhaseAInputError(f"T4 requires exactly {T4_CORPUS_SIZE}, got {len(flag_pairs)}")
    for i, pair in enumerate(flag_pairs):
        try:
            a, b = pair
        except (TypeError, ValueError) as e:
            raise PhaseAInputError(f"T4 item[{i}] must be (int,int): {e}") from e
        _validate_binary_int(a, f"T4[{i}].a")
        _validate_binary_int(b, f"T4[{i}].b")
    d = np.array(flag_pairs, dtype=np.float64)
    def fp_diff(x):
        x = np.atleast_2d(x)
        return float(np.mean(x[:,1]) - np.mean(x[:,0]))
    return _bca_interval(d, fp_diff, seed, seed+3, multidim=True)


# === T7 ===

def t7_interval(discrim, seed):
    """Exactly 240 items. PA-Z8: empty class -> None."""
    _validate_seed(seed)
    if len(discrim) != T7_CORPUS_SIZE:
        raise PhaseAInputError(f"T7 requires exactly {T7_CORPUS_SIZE}, got {len(discrim)}")
    for i, triple in enumerate(discrim):
        try:
            t, a, b = triple
        except (TypeError, ValueError) as e:
            raise PhaseAInputError(f"T7 item[{i}] must be (int,int,int): {e}") from e
        _validate_binary_int(t, f"T7[{i}].t")
        _validate_binary_int(a, f"T7[{i}].a")
        _validate_binary_int(b, f"T7[{i}].b")
    d = np.array(discrim, dtype=np.float64)
    if (d[:,0]==1).sum() == 0 or (d[:,0]==0).sum() == 0:
        return None  # PA-Z8
    def ba_b(x):
        x = np.atleast_2d(x)
        pos = x[:,0]==1; neg = x[:,0]==0
        if pos.sum()==0 or neg.sum()==0: return float("nan")
        return (float(np.mean(x[pos,2]==1)) + float(np.mean(x[neg,2]==0))) / 2.0
    return _bca_interval(d, ba_b, seed, seed+4, multidim=True)


# === T5 ===

@dataclass(frozen=True)
class T5Result:
    """T5: M7(B)/M7(A). Interval conjunct formally retired (PA-A5)."""
    m7_a: float; m7_b: float; ratio: Optional[float]
    evaluable: bool; t5_fires: Optional[bool]; rule: Optional[str]

def evaluate_t5(m7_a, m7_b):
    _reject_bool(m7_a, "M7(A)"); _reject_bool(m7_b, "M7(B)")
    a = _validate_numeric(m7_a, "M7(A)")
    b = _validate_numeric(m7_b, "M7(B)")
    if a == 0.0:
        return T5Result(a, b, None, False, None, "PA-Z3")
    return T5Result(a, b, b/a, True, b/a > 1.25, None)

# Need to import _validate_numeric
from shvvp_v0_8_4_phase_a_m3 import _validate_numeric


# === Full T2 ===

@dataclass
class T2FullResult:
    evaluable: bool; rule: Optional[str]; shared_set_size: int
    absolute_median: Optional[float]; absolute_gate_met: Optional[bool]
    absolute_interval: Optional[BootstrapResult]
    relative_median: Optional[float]; relative_gate_met: Optional[bool]
    relative_interval: Optional[BootstrapResult]
    relative_excluded_count: int; relative_nonfinite_count: int
    t2_satisfied: Optional[bool]

def evaluate_t2_full(pds, seed):
    _validate_seed(seed)
    for pd in pds: pd.verify_provenance()
    n = len(pds)
    if n == 0:
        return T2FullResult(False, "PA-Z1", 0, None, None, None,
                            None, None, None, 0, 0, None)

    deltas = [pd.delta for pd in pds]
    abs_med = compute_median(deltas)
    abs_gate = abs_med >= 30.0

    ratios, excluded, nonfinite = [], 0, 0
    for pd in pds:
        if pd.m3_a == 0:
            excluded += 1
        else:
            r = pd.delta / pd.m3_a
            if math.isfinite(r):
                ratios.append(r)
            else:
                nonfinite += 1

    if not ratios:
        rule = "PA-Z9" if nonfinite == 0 else "PA-Z13"
        abs_iv = t2_absolute_interval(pds, seed)
        return T2FullResult(False, rule, n, abs_med, abs_gate, abs_iv,
                            None, None, None, excluded, nonfinite, None)

    rel_med = compute_median(ratios)
    rel_gate = rel_med >= 0.20
    abs_iv = t2_absolute_interval(pds, seed)
    rel_iv = t2_relative_interval(pds, seed)

    iv_excl = abs_iv.excludes_zero if abs_iv else None
    if all(x for x in [abs_gate, rel_gate, iv_excl]):
        sat = True
    elif any(x is not None and not x for x in [abs_gate, rel_gate, iv_excl]):
        sat = False
    else:
        sat = None

    return T2FullResult(True, None, n, abs_med, abs_gate, abs_iv,
                        rel_med, rel_gate, rel_iv, excluded, nonfinite, sat)

---

# Bismillah ir-Rahman ir-Rahim
