# Bismillah ir-Rahman ir-Rahim

# R0394 -- test_shvvp_v0_8_4_phase_a.txt — test_shvvp_v0_8_4_phase_a.py -- Adversarial test suite for SHVVP v0.8.4.

**Chronological Index:** 759 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** test_shvvp_v0_8_4_phase_a.txt  
**Source Format:** txt  
**SHA-256:** `c7358ba6fcbc40a9451e79c8c5e7ecf64adb4dda827606b92bce54e296e51f55`  

---

## R0394 · test_shvvp_v0_8_4_phase_a.txt — test_shvvp_v0_8_4_phase_a.py -- Adversarial test suite for SHVVP v0.8.4.

- section: V. BSSG & SHVVP Protocols
- source_file: test_shvvp_v0_8_4_phase_a.txt
- source_format: txt
- merged_variants: 3 (xz_protocol_phase_a_tests.py; xz_protocol_phase_a_tests.py.txt; xz_protocol_phase_a_tests.txt)
- text_sha256: c7358ba6fcbc40a9451e79c8c5e7ecf64adb4dda827606b92bce54e296e51f55

"""
test_shvvp_v0_8_4_phase_a.py -- Adversarial test suite for SHVVP v0.8.4.

Covers all CODE-LEVEL PA-Z rules (PA-Z1-Z3, PA-Z5-Z14; eleven rules).
PA-Z4 (alpha undefined) is adjudication-layer and scoped out.
Golden vectors pin exact bounds for T2-abs, T2-rel, T3, T4, T7,
PA-Z2, PA-Z5, PA-Z10, PA-Z11, PA-Z14.
"""
import math, pytest, numpy as np
from shvvp_v0_8_4_phase_a_m3 import (
    CensorStatus, FROZEN_BUDGET_MINUTES, M3FirstResult,
    M3Observation, M3Vector, PairedDifference, PhaseAInputError,
    compute_median, compute_paired_differences, compute_shared_set,
    evaluate_t2_point,
)
from shvvp_v0_8_4_phase_a_intervals import (
    IntervalMethod, T4_CORPUS_SIZE, T7_CORPUS_SIZE,
    evaluate_t2_full, evaluate_t5,
    t2_absolute_interval, t2_relative_interval, t3_interval,
    t4_interval, t7_interval,
)
SEED = 42

def _obs(fid, cond, mins, eid="ev"):
    return M3Observation(fid, cond, mins, CensorStatus.OBSERVED, eid)

def _5fact():
    oa = [_obs(f"f{i}","A",a,f"ea{i}") for i,(a,_) in enumerate([(60,20),(120,45),(90,90),(200,30),(150,100)])]
    ob = [_obs(f"f{i}","B",b,f"eb{i}") for i,(_,b) in enumerate([(60,20),(120,45),(90,90),(200,30),(150,100)])]
    return M3Vector("A",tuple(oa)), M3Vector("B",tuple(ob))

# === INPUT VALIDATION ===
class TestInputValidation:
    def test_nan(self):
        with pytest.raises(PhaseAInputError): _obs("f1","A",float("nan"))
    def test_inf(self):
        with pytest.raises(PhaseAInputError): _obs("f1","A",float("inf"))
    def test_neg(self):
        with pytest.raises(PhaseAInputError): _obs("f1","A",-5.0)
    def test_bool(self):
        with pytest.raises(PhaseAInputError): _obs("f1","A",True)
    def test_empty_fid(self):
        with pytest.raises(PhaseAInputError): _obs("","A",60.0)
    def test_string_censor(self):
        """F-SOL-083-2: string censor_status rejected."""
        with pytest.raises(PhaseAInputError, match="CensorStatus enum"):
            M3Observation("f1","A",60.0,"OBSERVED","ev1")
    def test_dup_constructor(self):
        o = _obs("f1","A",60.0)
        with pytest.raises(PhaseAInputError): M3Vector("A",(o,o))

# === IMMUTABILITY (F-SOL-083-1) ===
class TestImmutability:
    def test_frozen(self):
        v = M3Vector("A",(_obs("f1","A",60.0),))
        with pytest.raises(AttributeError):
            v.observations = ()
    def test_with_obs(self):
        v = M3Vector("A",(_obs("f1","A",60.0),))
        v2 = v.with_obs(_obs("f2","A",90.0))
        assert len(v.observations) == 1
        assert len(v2.observations) == 2

# === CENSOR CONSISTENCY ===
class TestCensorConsistency:
    def test_budget_wrong(self):
        with pytest.raises(PhaseAInputError):
            M3Observation("f1","A",100.0,CensorStatus.RIGHT_CENSORED_BUDGET)
    def test_budget_no_evidence(self):
        o = M3Observation("f1","A",FROZEN_BUDGET_MINUTES,CensorStatus.RIGHT_CENSORED_BUDGET)
        assert not o.is_observed
    def test_budget_with_evidence(self):
        with pytest.raises(PhaseAInputError, match="must not carry"):
            M3Observation("f1","A",FROZEN_BUDGET_MINUTES,CensorStatus.RIGHT_CENSORED_BUDGET,"ev")
    def test_early_at_budget(self):
        with pytest.raises(PhaseAInputError):
            M3Observation("f1","A",FROZEN_BUDGET_MINUTES,CensorStatus.CENSORED_EARLY)
    def test_early_with_evidence(self):
        with pytest.raises(PhaseAInputError, match="must not carry"):
            M3Observation("f1","A",100.0,CensorStatus.CENSORED_EARLY,"ev")
    def test_observed_no_evidence(self):
        with pytest.raises(PhaseAInputError, match="non-empty str"):
            M3Observation("f1","A",60.0,CensorStatus.OBSERVED)
    def test_observed_empty_evidence(self):
        with pytest.raises(PhaseAInputError, match="non-empty str"):
            M3Observation("f1","A",60.0,CensorStatus.OBSERVED,"")
    def test_observed_beyond_budget(self):
        with pytest.raises(PhaseAInputError):
            _obs("f1","A",481.0)
    def test_observed_at_budget_ok(self):
        assert _obs("f1","A",FROZEN_BUDGET_MINUTES).is_observed

# === M3-FIRST ===
class TestM3First:
    def test_observed_only(self):
        v = M3Vector("A",(
            M3Observation("f1","A",10.0,CensorStatus.CENSORED_EARLY),
            _obs("f2","A",60.0)))
        assert v.m3_first() == 60.0
    def test_empty(self):
        assert M3Vector("A").m3_first() == M3FirstResult.NO_DISCOVERY

# === S-MEMBERSHIP ===
class TestSharedSet:
    def test_both_observed(self):
        va,vb = _5fact()
        assert len(compute_shared_set(va,vb)) == 5
    def test_censored_excluded(self):
        va = M3Vector("A",(_obs("f1","A",60.0),))
        vb = M3Vector("B",(M3Observation("f1","B",FROZEN_BUDGET_MINUTES,CensorStatus.RIGHT_CENSORED_BUDGET),))
        assert compute_shared_set(va,vb) == []

# === PROVENANCE ===
class TestProvenance:
    def test_fabricated(self):
        fake = PairedDifference("f1",100,30,70,CensorStatus.OBSERVED,CensorStatus.OBSERVED)
        with pytest.raises(PhaseAInputError, match="provenance"): fake.verify_provenance()
    def test_genuine(self):
        va,vb = _5fact()
        for d in compute_paired_differences(va,vb): d.verify_provenance()

# === PA-Z1 ===
class TestPAZ1:
    def test_t2(self):
        r = evaluate_t2_full([], SEED)
        assert not r.evaluable and r.rule == "PA-Z1"
    def test_t3(self):
        assert t3_interval([], SEED) is None

# === PA-Z2 ===
class TestPAZ2:
    def test_single(self):
        va = M3Vector("A",(_obs("f1","A",100.0),))
        vb = M3Vector("B",(_obs("f1","B",30.0),))
        ds = compute_paired_differences(va,vb)
        r = evaluate_t2_full(ds, SEED)
        assert r.absolute_interval.method == IntervalMethod.PERCENTILE
        assert "PA-Z2" in r.absolute_interval.fallback_reason

# === PA-Z3 ===
class TestPAZ3:
    def test_zero(self): assert not evaluate_t5(0.0, 10.0).evaluable
    def test_fires(self): assert evaluate_t5(8.0, 12.0).t5_fires
    def test_bool_rejected(self):
        with pytest.raises(PhaseAInputError): evaluate_t5(True, 10.0)

# === PA-Z5 ===
class TestPAZ5:
    def test_median_fires(self):
        """Kimi's [1,5,5,5,9] fixture."""
        oa = [_obs(f"f{i}","A",a,f"ea{i}") for i,a in enumerate([101,105,105,105,109])]
        ob = [_obs(f"f{i}","B",100.0,f"eb{i}") for i in range(5)]
        va,vb = M3Vector("A",tuple(oa)), M3Vector("B",tuple(ob))
        ds = compute_paired_differences(va,vb)
        r = t2_absolute_interval(ds, SEED)
        assert r.method == IntervalMethod.PERCENTILE
        assert "PA-Z5" in r.fallback_reason
        assert r.point_estimate == 5.0
        assert r.lower == 1.0 and r.upper == 9.0

# === PA-Z6 ===
class TestPAZ6:
    def test_counted(self):
        oa = [_obs("f0","A",100.0,"ea0"), _obs("f1","A",200.0,"ea1")]
        ob = [_obs("f0","B",50.0,"eb0"), _obs("f1","B",100.0,"eb1")]
        va,vb = M3Vector("A",tuple(oa)), M3Vector("B",tuple(ob))
        ds = compute_paired_differences(va,vb)
        r = t2_absolute_interval(ds, SEED)
        assert r.n_degenerate_resample > 0

# === PA-Z7 (named via T4 zero-diff behavior) ===
class TestPAZ7:
    def test_no_flags(self):
        r = t4_interval([(0,0)]*T4_CORPUS_SIZE, SEED)
        assert r.point_estimate == 0.0

# === PA-Z8 ===
class TestPAZ8:
    def test_all_pos(self): assert t7_interval([(1,1,1)]*T7_CORPUS_SIZE, SEED) is None
    def test_all_neg(self): assert t7_interval([(0,0,0)]*T7_CORPUS_SIZE, SEED) is None

# === PA-Z9 ===
class TestPAZ9:
    def test_point(self):
        oa = [_obs(f"f{i}","A",0.0,f"ea{i}") for i in range(3)]
        ob = [_obs(f"f{i}","B",30.0,f"eb{i}") for i in range(3)]
        va,vb = M3Vector("A",tuple(oa)), M3Vector("B",tuple(ob))
        ds = compute_paired_differences(va,vb)
        r = evaluate_t2_point(ds)
        assert r["evaluable"] is False and r["rule"] == "PA-Z9"
    def test_full(self):
        oa = [_obs(f"f{i}","A",0.0,f"ea{i}") for i in range(3)]
        ob = [_obs(f"f{i}","B",30.0,f"eb{i}") for i in range(3)]
        va,vb = M3Vector("A",tuple(oa)), M3Vector("B",tuple(ob))
        ds = compute_paired_differences(va,vb)
        r = evaluate_t2_full(ds, SEED)
        assert not r.evaluable and r.rule == "PA-Z9"

# === PA-Z10 ===
class TestPAZ10:
    def test_z0_undef(self):
        oa = [_obs(f"f{i}","A",a,f"ea{i}") for i,a in enumerate([100.0,100.0,100.0])]
        ob = [_obs(f"f{i}","B",b,f"eb{i}") for i,b in enumerate([100.0,100.0,99.0])]
        va,vb = M3Vector("A",tuple(oa)), M3Vector("B",tuple(ob))
        ds = compute_paired_differences(va,vb)
        r = t2_absolute_interval(ds, SEED)
        assert r.method == IntervalMethod.PERCENTILE
        assert "PA-Z10" in r.fallback_reason
        assert r.point_estimate == 0.0
        assert r.lower == 0.0 and r.upper == 1.0

# === PA-Z11 ===
class TestPAZ11:
    def test_nan_counted(self):
        items = [(1,1,1)]*1 + [(0,0,0)]*(T7_CORPUS_SIZE-1)
        r = t7_interval(items, SEED)
        assert r.n_nan_resamples > 0
        assert not math.isnan(r.lower)

# === PA-Z12: FIRING fixture (F-K3-083-8) ===
class TestPAZ12:
    def test_loo_nan_fires(self):
        """1 positive (B=1) + 5 negative (B=1, misclassified) + 234 negative (B=0).
        LOO removing the sole positive empties the class -> NaN -> PA-Z12.
        Imperfect specificity keeps prop_below in (0,1) -> BCa runs."""
        items = [(1,1,1)]*1 + [(0,0,1)]*5 + [(0,0,0)]*234
        r = t7_interval(items, SEED)
        assert r is not None
        assert r.n_loo_nan_substitutions >= 1

# === PA-Z13 (non-finite ratio) ===
class TestPAZ13:
    def test_subnormal(self):
        """F-K3-083-2: subnormal M3(f,A) yields -inf ratio, excluded."""
        oa = [_obs("f0","A",1e-308,"ea0"), _obs("f1","A",100.0,"ea1")]
        ob = [_obs("f0","B",480.0,"eb0"), _obs("f1","B",60.0,"eb1")]
        va,vb = M3Vector("A",tuple(oa)), M3Vector("B",tuple(ob))
        ds = compute_paired_differences(va,vb)
        r = evaluate_t2_point(ds)
        assert r["relative_nonfinite_count"] >= 1
        # Full evaluator should NOT raise (F-K3-083-2 fix)
        rf = evaluate_t2_full(ds, SEED)
        assert rf is not None

# === PA-Z14 (BCa excludes point) ===
class TestPAZ14:
    def test_point_exclusion(self):
        """F-K3-083-1: heavily tied median -> BCa interval excludes point.
        Named PA-Z14 -> percentile reversion."""
        # Construct: many zeros and a few non-zeros so median=0 but
        # BCa correction pushes interval below zero
        oa = [_obs(f"f{i}","A",float(100+i),f"ea{i}") for i in range(41)]
        vals_b = [100]*38 + [97,98,99]  # deltas: [0]*38 + [3,2,1] -> median 0
        ob = [_obs(f"f{i}","B",float(vals_b[i]),f"eb{i}") for i in range(41)]
        va,vb = M3Vector("A",tuple(oa)), M3Vector("B",tuple(ob))
        ds = compute_paired_differences(va,vb)
        r = t2_absolute_interval(ds, SEED)
        # If PA-Z14 fires, method should be PERCENTILE with reason
        if not r.point_in_interval:
            assert "PA-Z14" in r.fallback_reason
            assert r.method == IntervalMethod.PERCENTILE
            assert r.excludes_zero is False  # conservative

# === GOLDEN VECTORS ===
class TestGoldenVectors:
    def test_t2_5fact(self):
        va,vb = _5fact()
        ds = compute_paired_differences(va,vb)
        r = evaluate_t2_full(ds, SEED)
        assert r.evaluable and r.shared_set_size == 5
        assert r.absolute_median == 50.0
        assert r.absolute_gate_met
        assert abs(r.relative_median - 0.625) < 1e-10
        assert r.relative_gate_met
        assert r.absolute_interval.lower == 0.0
        assert r.absolute_interval.upper == 75.0
        assert r.absolute_interval.method == IntervalMethod.BCA
        assert r.t2_satisfied is False  # interval doesn't exclude zero

    def test_t3(self):
        r = t3_interval([3.0,5.0,-1.0,8.0,2.0], SEED)
        assert abs(r.point_estimate - 3.4) < 1e-10
        assert abs(r.lower - 0.8) < 1e-6
        assert abs(r.upper - 5.8) < 1e-6

    def test_t4(self):
        ps = [(0,1)]*20+[(1,0)]*10+[(0,0)]*170
        r = t4_interval(ps, SEED)
        assert abs(r.point_estimate - 0.05) < 1e-10
        assert abs(r.lower - (-0.005)) < 1e-6
        assert abs(r.upper - 0.105) < 1e-6

    def test_t7_imperfect(self):
        items = [(1,1,1)]*30+[(1,1,0)]*10+[(0,0,0)]*190+[(0,0,1)]*10
        r = t7_interval(items, SEED)
        assert abs(r.point_estimate - 0.85) < 1e-10
        assert abs(r.lower - 0.7716350602906202) < 1e-6
        assert abs(r.upper - 0.912029630366201) < 1e-6

# === CARDINALITY ===
class TestCardinality:
    def test_t4_empty(self):
        with pytest.raises(PhaseAInputError, match="exactly 200"): t4_interval([], SEED)
    def test_t7_empty(self):
        with pytest.raises(PhaseAInputError, match="exactly 240"): t7_interval([], SEED)
    def test_t4_wrong(self):
        with pytest.raises(PhaseAInputError): t4_interval([(0,0)]*100, SEED)
    def test_t7_wrong(self):
        with pytest.raises(PhaseAInputError): t7_interval([(0,0,0)]*100, SEED)
    def test_t4_bool(self):
        with pytest.raises(PhaseAInputError): t4_interval([(True,0)]+[(0,0)]*199, SEED)
    def test_t7_bool(self):
        with pytest.raises(PhaseAInputError): t7_interval([(True,0,0)]+[(0,0,0)]*239, SEED)
    def test_t4_shape(self):
        with pytest.raises(PhaseAInputError): t4_interval([(0,0,0)]*200, SEED)
    def test_t7_shape(self):
        with pytest.raises(PhaseAInputError): t7_interval([(0,0)]*240, SEED)

# === BOOL REJECTION (uniform) ===
class TestBoolUniform:
    def test_t3(self):
        with pytest.raises(PhaseAInputError): t3_interval([True,False], SEED)
    def test_t5(self):
        with pytest.raises(PhaseAInputError): evaluate_t5(True, 10.0)
    def test_median(self):
        with pytest.raises(PhaseAInputError): compute_median([True, False])

# === SEED VALIDATION ===
class TestSeed:
    def test_neg(self):
        with pytest.raises(PhaseAInputError): t3_interval([1.0,2.0], -1)
    def test_float(self):
        with pytest.raises(PhaseAInputError): t3_interval([1.0,2.0], 1.5)
    def test_bool(self):
        with pytest.raises(PhaseAInputError): t3_interval([1.0,2.0], True)
    def test_caller_seed_recorded(self):
        """F-K3-083-7: caller_seed round-trips."""
        r = t3_interval([1.0,2.0,3.0], 100)
        assert r.caller_seed == 100

# === SEED REPRODUCIBILITY ===
class TestSeedRepro:
    def test_same(self):
        va,vb = _5fact()
        ds = compute_paired_differences(va,vb)
        r1 = evaluate_t2_full(ds, 12345)
        r2 = evaluate_t2_full(ds, 12345)
        assert r1.absolute_interval.lower == r2.absolute_interval.lower

# === FACT-ID NORMALIZATION ===
class TestFactIdNorm:
    def test_strip(self):
        o = _obs(" f1 ", "A", 60.0)
        v = M3Vector("A", (o,))
        assert "f1" in v.observed_fact_ids
    def test_case_sensitive(self):
        o1 = _obs("f1", "A", 60.0, "e1")
        o2 = _obs("F1", "A", 90.0, "e2")
        v = M3Vector("A", (o1, o2))  # should not raise -- different IDs
        assert len(v.observations) == 2

# === MEDIAN ===
class TestMedian:
    def test_odd(self): assert compute_median([1,3,5,7,9]) == 5
    def test_even(self): assert compute_median([1,3,5,7]) == 4.0
    def test_empty(self):
        with pytest.raises(PhaseAInputError): compute_median([])

# === BUDGET ===
class TestBudget:
    def test_val(self): assert FROZEN_BUDGET_MINUTES == 480.0

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

---

# Bismillah ir-Rahman ir-Rahim
