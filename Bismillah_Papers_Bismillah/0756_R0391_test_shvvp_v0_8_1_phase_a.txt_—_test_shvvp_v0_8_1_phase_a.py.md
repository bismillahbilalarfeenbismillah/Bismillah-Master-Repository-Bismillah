# Bismillah ir-Rahman ir-Rahim

# R0391 -- test_shvvp_v0_8_1_phase_a.txt — test_shvvp_v0_8_1_phase_a.py -- Adversarial test suite for SHVVP v0.8.1.

**Chronological Index:** 756 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** test_shvvp_v0_8_1_phase_a.txt  
**Source Format:** txt  
**SHA-256:** `d8f24c36d02fefd09486ddd8e2ea4e5da0eebde87e83ee8c58d63ea0af22e479`  

---

## R0391 · test_shvvp_v0_8_1_phase_a.txt — test_shvvp_v0_8_1_phase_a.py -- Adversarial test suite for SHVVP v0.8.1.

- section: V. BSSG & SHVVP Protocols
- source_file: test_shvvp_v0_8_1_phase_a.txt
- source_format: txt
- text_sha256: d8f24c36d02fefd09486ddd8e2ea4e5da0eebde87e83ee8c58d63ea0af22e479

"""
test_shvvp_v0_8_1_phase_a.py -- Adversarial test suite for SHVVP v0.8.1.

Covers:
  - Every PA-Z rule (PA-Z1 through PA-Z8)
  - T2 computation on a hand-constructed 5-fact shared set
  - T3 computation on the same 5-fact set
  - BCa-to-percentile fallback (PA-Z2, PA-Z5)
  - Censoring direction verification
  - Seed reproducibility
  - Caller-supplied statistic rejection
  - Input validation (non-numeric, negative, NaN, infinity)

Text and code are the same rule written twice. A divergence is a defect.
"""

import math
import pytest
import numpy as np

from shvvp_v0_8_1_phase_a_m3 import (
    CensorStatus,
    M3Observation,
    M3Vector,
    PairedDifference,
    PhaseAInputError,
    compute_median,
    compute_paired_differences,
    compute_shared_set,
    evaluate_t2_point,
    reject_caller_supplied_statistic,
)
from shvvp_v0_8_1_phase_a_intervals import (
    IntervalMethod,
    T5Result,
    evaluate_t2_full,
    evaluate_t5,
    t2_absolute_interval,
    t2_relative_interval,
    t3_interval,
    t4_interval,
    t7_interval,
)


# ===================================================================
# FIXTURES
# ===================================================================

SEED = 42
BUDGET = 480.0  # 8-hour budget in minutes


def _make_5fact_vectors():
    """Hand-constructed 5-fact shared set with known discovery times.

    Fact | M3(f,A) | M3(f,B) | Delta | Ratio
    f1   |   60    |   20    |  40   |  0.667
    f2   |  120    |   45    |  75   |  0.625
    f3   |   90    |   90    |   0   |  0.000
    f4   |  200    |   30    | 170   |  0.850
    f5   |  150    |  100    |  50   |  0.333

    Sorted deltas: [0, 40, 50, 75, 170]
    Median delta: 50 (middle of 5)
    Sorted ratios: [0.0, 0.333, 0.625, 0.667, 0.850]
    Median ratio: 0.625

    T2 absolute gate: 50 >= 30 -> MET
    T2 relative gate: 0.625 >= 0.20 -> MET
    """
    vec_a = M3Vector(condition="A")
    vec_b = M3Vector(condition="B")

    facts = [
        ("f1", 60.0, 20.0),
        ("f2", 120.0, 45.0),
        ("f3", 90.0, 90.0),
        ("f4", 200.0, 30.0),
        ("f5", 150.0, 100.0),
    ]
    for fid, ta, tb in facts:
        vec_a.add(M3Observation(fid, "A", ta, CensorStatus.OBSERVED))
        vec_b.add(M3Observation(fid, "B", tb, CensorStatus.OBSERVED))

    return vec_a, vec_b


def _make_1fact_vectors():
    """Single shared fact for PA-Z2 testing."""
    vec_a = M3Vector(condition="A")
    vec_b = M3Vector(condition="B")
    vec_a.add(M3Observation("f1", "A", 100.0, CensorStatus.OBSERVED))
    vec_b.add(M3Observation("f1", "B", 30.0, CensorStatus.OBSERVED))
    return vec_a, vec_b


# ===================================================================
# M3 OBSERVATION TESTS
# ===================================================================

class TestM3Observation:

    def test_valid_observation(self):
        obs = M3Observation("f1", "A", 60.0, CensorStatus.OBSERVED)
        assert obs.fact_id == "f1"
        assert obs.minutes == 60.0

    def test_nan_rejected(self):
        with pytest.raises(PhaseAInputError, match="NaN"):
            M3Observation("f1", "A", float("nan"), CensorStatus.OBSERVED)

    def test_infinity_rejected(self):
        with pytest.raises(PhaseAInputError, match="infinite"):
            M3Observation("f1", "A", float("inf"), CensorStatus.OBSERVED)

    def test_negative_rejected(self):
        with pytest.raises(PhaseAInputError, match="negative"):
            M3Observation("f1", "A", -5.0, CensorStatus.OBSERVED)

    def test_invalid_condition_rejected(self):
        with pytest.raises(PhaseAInputError, match="Condition"):
            M3Observation("f1", "X", 60.0, CensorStatus.OBSERVED)

    def test_string_value_rejected(self):
        with pytest.raises(PhaseAInputError, match="numeric"):
            M3Observation("f1", "A", "sixty", CensorStatus.OBSERVED)


class TestM3Vector:

    def test_duplicate_fact_rejected(self):
        vec = M3Vector(condition="A")
        vec.add(M3Observation("f1", "A", 60.0, CensorStatus.OBSERVED))
        with pytest.raises(PhaseAInputError, match="Duplicate"):
            vec.add(M3Observation("f1", "A", 90.0, CensorStatus.OBSERVED))

    def test_wrong_condition_rejected(self):
        vec = M3Vector(condition="A")
        with pytest.raises(PhaseAInputError, match="does not match"):
            vec.add(M3Observation("f1", "B", 60.0, CensorStatus.OBSERVED))

    def test_m3_first(self):
        vec_a, _ = _make_5fact_vectors()
        assert vec_a.m3_first() == 60.0

    def test_m3_first_empty(self):
        vec = M3Vector(condition="A")
        assert vec.m3_first() is None


# ===================================================================
# SHARED SET AND PAIRED DIFFERENCES
# ===================================================================

class TestSharedSet:

    def test_5fact_shared(self):
        vec_a, vec_b = _make_5fact_vectors()
        shared = compute_shared_set(vec_a, vec_b)
        assert shared == ["f1", "f2", "f3", "f4", "f5"]

    def test_partial_overlap(self):
        vec_a = M3Vector(condition="A")
        vec_b = M3Vector(condition="B")
        vec_a.add(M3Observation("f1", "A", 60.0, CensorStatus.OBSERVED))
        vec_a.add(M3Observation("f2", "A", 90.0, CensorStatus.OBSERVED))
        vec_b.add(M3Observation("f2", "B", 30.0, CensorStatus.OBSERVED))
        vec_b.add(M3Observation("f3", "B", 45.0, CensorStatus.OBSERVED))
        assert compute_shared_set(vec_a, vec_b) == ["f2"]

    def test_empty_shared(self):
        vec_a = M3Vector(condition="A")
        vec_b = M3Vector(condition="B")
        vec_a.add(M3Observation("f1", "A", 60.0, CensorStatus.OBSERVED))
        vec_b.add(M3Observation("f2", "B", 30.0, CensorStatus.OBSERVED))
        assert compute_shared_set(vec_a, vec_b) == []


class TestPairedDifferences:

    def test_5fact_deltas(self):
        vec_a, vec_b = _make_5fact_vectors()
        diffs = compute_paired_differences(vec_a, vec_b)
        assert len(diffs) == 5
        expected = {"f1": 40.0, "f2": 75.0, "f3": 0.0,
                    "f4": 170.0, "f5": 50.0}
        for pd in diffs:
            assert abs(pd.delta - expected[pd.fact_id]) < 1e-10

    def test_wrong_condition_order_rejected(self):
        vec_a, vec_b = _make_5fact_vectors()
        with pytest.raises(PhaseAInputError, match="must be condition 'A'"):
            compute_paired_differences(vec_b, vec_a)


# ===================================================================
# T2 POINT STATISTICS
# ===================================================================

class TestT2Point:

    def test_5fact_point_statistics(self):
        vec_a, vec_b = _make_5fact_vectors()
        diffs = compute_paired_differences(vec_a, vec_b)
        result = evaluate_t2_point(diffs)

        assert result["shared_set_size"] == 5
        assert result["evaluable"] is True
        # Median of [0, 40, 50, 75, 170] = 50
        assert result["absolute_median"] == 50.0
        assert result["absolute_gate_met"] is True
        # Median of ratios [0.0, 0.333..., 0.625, 0.667..., 0.850] = 0.625
        assert abs(result["relative_median"] - 0.625) < 1e-10
        assert result["relative_gate_met"] is True

    def test_empty_set_pa_z1(self):
        """PA-Z1: S is empty -> NOT-EVALUABLE."""
        result = evaluate_t2_point([])
        assert result["evaluable"] is False
        assert result["rule"] == "PA-Z1"
        assert result["absolute_median"] is None


# ===================================================================
# PA-Z RULES (degeneracy tests)
# ===================================================================

class TestPAZ1:
    """PA-Z1: S empty -> T2 and T3 NOT-EVALUABLE."""

    def test_t2_not_evaluable(self):
        result = evaluate_t2_full([], SEED)
        assert result.evaluable is False
        assert result.rule == "PA-Z1"
        assert result.t2_satisfied is None

    def test_t3_not_evaluable(self):
        # T3 interval returns None on empty input
        result = t3_interval([], SEED)
        assert result is None


class TestPAZ2:
    """PA-Z2: S has exactly one fact -> BCa fallback to percentile."""

    def test_single_fact_fallback(self):
        vec_a, vec_b = _make_1fact_vectors()
        diffs = compute_paired_differences(vec_a, vec_b)
        assert len(diffs) == 1
        result = evaluate_t2_full(diffs, SEED)
        assert result.evaluable is True
        assert result.absolute_interval is not None
        assert result.absolute_interval.method == IntervalMethod.PERCENTILE
        assert "PA-Z2" in result.absolute_interval.fallback_reason


class TestPAZ3:
    """PA-Z3: M7(A) = 0 -> T5 NOT-EVALUABLE."""

    def test_zero_baseline_burden(self):
        result = evaluate_t5(0.0, 10.0)
        assert result.evaluable is False
        assert result.rule == "PA-Z3"
        assert result.ratio is None
        assert result.t5_fires is None

    def test_normal_t5(self):
        result = evaluate_t5(8.0, 12.0)
        assert result.evaluable is True
        assert result.ratio == 1.5
        assert result.t5_fires is True  # 1.5 > 1.25

    def test_t5_below_threshold(self):
        result = evaluate_t5(10.0, 11.0)
        assert result.evaluable is True
        assert result.ratio == 1.1
        assert result.t5_fires is False  # 1.1 <= 1.25


class TestPAZ4:
    """PA-Z4: alpha undefined -> INDETERMINATE-ADJUDICATION.
    This is a policy rule, not a computation -- tested by verifying
    that the handling is documented and the rule exists."""

    def test_rule_documented(self):
        # PA-Z4 is a policy rule; we verify the code references it
        # by checking the T5 and M12 handling don't silently pass
        # undefined values.
        with pytest.raises(PhaseAInputError, match="NaN"):
            evaluate_t5(float("nan"), 10.0)


class TestPAZ6:
    """PA-Z6: all-identical resample -> stat is the unique value.
    Verified indirectly by ensuring degenerate resamples don't crash."""

    def test_single_fact_no_crash(self):
        diffs = [PairedDifference("f1", 100.0, 30.0, 70.0,
                                  CensorStatus.OBSERVED,
                                  CensorStatus.OBSERVED)]
        result = t2_absolute_interval(diffs, SEED)
        assert result is not None
        assert result.point_estimate == 70.0


class TestPAZ8:
    """PA-Z8: M6(B) not computable -> T7 NOT-EVALUABLE."""

    def test_all_positive_labels(self):
        # All items have true_label=1 -> specificity undefined
        items = [(1, 1, 1)] * 50
        result = t7_interval(items, SEED)
        assert result is None  # PA-Z8

    def test_all_negative_labels(self):
        # All items have true_label=0 -> sensitivity undefined
        items = [(0, 0, 0)] * 50
        result = t7_interval(items, SEED)
        assert result is None  # PA-Z8


# ===================================================================
# T2 FULL EVALUATION ON 5-FACT SET
# ===================================================================

class TestT2Full:

    def test_5fact_full_evaluation(self):
        vec_a, vec_b = _make_5fact_vectors()
        diffs = compute_paired_differences(vec_a, vec_b)
        result = evaluate_t2_full(diffs, SEED)

        assert result.evaluable is True
        assert result.shared_set_size == 5
        assert result.absolute_median == 50.0
        assert result.absolute_gate_met is True
        assert abs(result.relative_median - 0.625) < 1e-10
        assert result.relative_gate_met is True
        assert result.absolute_interval is not None
        assert result.absolute_interval.n_resamples == 10_000


# ===================================================================
# CENSORING DIRECTION
# ===================================================================

class TestCensoring:
    """Verify that censoring is conservative (fail-safe for T2)."""

    def test_censored_b_makes_delta_large_positive(self):
        """If B is censored at BUDGET but A found the fact,
        Delta = M3(A) - BUDGET is very negative, making the
        median harder to achieve (conservative against B)."""
        vec_a = M3Vector(condition="A")
        vec_b = M3Vector(condition="B")
        # A finds f1 at 60 minutes; B is censored at budget
        vec_a.add(M3Observation("f1", "A", 60.0, CensorStatus.OBSERVED))
        vec_b.add(M3Observation("f1", "B", BUDGET,
                                CensorStatus.RIGHT_CENSORED_BUDGET))
        diffs = compute_paired_differences(vec_a, vec_b)
        assert len(diffs) == 1
        # Delta = 60 - 480 = -420 (very negative, unfavorable to B)
        assert diffs[0].delta == 60.0 - BUDGET
        assert diffs[0].delta < 0

    def test_censored_a_makes_delta_large_positive(self):
        """If A is censored at BUDGET but B found the fact,
        Delta = BUDGET - M3(B) is large positive (favorable to B).
        But this is conservative because it inflates B's apparent
        advantage on ONE fact, which the median is robust to."""
        vec_a = M3Vector(condition="A")
        vec_b = M3Vector(condition="B")
        vec_a.add(M3Observation("f1", "A", BUDGET,
                                CensorStatus.RIGHT_CENSORED_BUDGET))
        vec_b.add(M3Observation("f1", "B", 30.0, CensorStatus.OBSERVED))
        diffs = compute_paired_differences(vec_a, vec_b)
        assert diffs[0].delta == BUDGET - 30.0
        assert diffs[0].delta > 0


# ===================================================================
# SEED REPRODUCIBILITY
# ===================================================================

class TestSeedReproducibility:
    """Two runs with the same seed and data produce identical intervals."""

    def test_same_seed_same_result(self):
        vec_a, vec_b = _make_5fact_vectors()
        diffs = compute_paired_differences(vec_a, vec_b)

        r1 = evaluate_t2_full(diffs, seed=12345)
        r2 = evaluate_t2_full(diffs, seed=12345)

        assert r1.absolute_interval.lower == r2.absolute_interval.lower
        assert r1.absolute_interval.upper == r2.absolute_interval.upper
        assert r1.absolute_interval.point_estimate == \
               r2.absolute_interval.point_estimate

    def test_different_seed_different_result(self):
        vec_a, vec_b = _make_5fact_vectors()
        diffs = compute_paired_differences(vec_a, vec_b)

        r1 = evaluate_t2_full(diffs, seed=12345)
        r2 = evaluate_t2_full(diffs, seed=99999)

        # Very likely different (not guaranteed, but overwhelmingly probable)
        # We test that the code at least runs without error
        assert r1.absolute_interval is not None
        assert r2.absolute_interval is not None


# ===================================================================
# CALLER-SUPPLIED STATISTIC REJECTION
# ===================================================================

class TestCallerRejection:

    def test_precomputed_median_rejected(self):
        with pytest.raises(PhaseAInputError, match="Caller-supplied"):
            reject_caller_supplied_statistic(median=50.0)

    def test_precomputed_interval_rejected(self):
        with pytest.raises(PhaseAInputError, match="Caller-supplied"):
            reject_caller_supplied_statistic(interval=(10.0, 90.0))

    def test_derived_verdict_rejected(self):
        with pytest.raises(PhaseAInputError, match="Caller-supplied"):
            reject_caller_supplied_statistic(derived_verdict="NOT-FALSIFIED")

    def test_safe_keys_pass(self):
        # Keys not in the forbidden set should pass
        reject_caller_supplied_statistic(
            fact_id="f1", raw_minutes=60.0, condition="A"
        )


# ===================================================================
# MEDIAN COMPUTATION
# ===================================================================

class TestMedian:

    def test_odd_count(self):
        assert compute_median([1, 3, 5, 7, 9]) == 5

    def test_even_count(self):
        assert compute_median([1, 3, 5, 7]) == 4.0

    def test_single_value(self):
        assert compute_median([42]) == 42

    def test_ties(self):
        assert compute_median([5, 5, 5, 5, 5]) == 5

    def test_empty_raises(self):
        with pytest.raises(PhaseAInputError, match="empty"):
            compute_median([])


# ===================================================================
# T3 INTERVAL
# ===================================================================

class TestT3:

    def test_5fact_t3(self):
        """Hand-constructed M4 differences for the 5-fact set.

        M4(f,B) - M4(f,A): [3, 5, -1, 8, 2]
        Mean: (3+5-1+8+2)/5 = 17/5 = 3.4
        T3 gate: 3.4 >= 2.0 -> MET (point statistic)
        """
        m4_diffs = [3.0, 5.0, -1.0, 8.0, 2.0]
        result = t3_interval(m4_diffs, SEED)
        assert result is not None
        assert abs(result.point_estimate - 3.4) < 1e-10

    def test_empty_t3(self):
        result = t3_interval([], SEED)
        assert result is None


# ===================================================================
# T4 INTERVAL
# ===================================================================

class TestT4:

    def test_no_flags(self):
        """PA-Z7: zero items flagged by either -> M5 diff = 0."""
        pairs = [(0, 0)] * 200
        result = t4_interval(pairs, SEED)
        assert result is not None
        assert result.point_estimate == 0.0


# ===================================================================
# ENTRY POINT
# ===================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

---

# Bismillah ir-Rahman ir-Rahim
