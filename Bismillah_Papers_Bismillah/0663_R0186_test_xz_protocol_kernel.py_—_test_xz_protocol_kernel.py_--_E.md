# Bismillah ir-Rahman ir-Rahim

# R0186 -- test_xz_protocol_kernel.py — test_xz_protocol_kernel.py -- Exhaustive 3^5=243 kernel tests + adversarial.

**Chronological Index:** 663 of 995  
**Date:** Undated  
**Section:** IV. XZ Protocol  
**Source File:** test_xz_protocol_kernel.py  
**Source Format:** py  
**SHA-256:** `d3b557985bc571b535d021792cb0cd772446ecdeb317177b5305229cfaafb228`  

---

## R0186 · test_xz_protocol_kernel.py — test_xz_protocol_kernel.py -- Exhaustive 3^5=243 kernel tests + adversarial.

- section: IV. XZ Protocol
- source_file: test_xz_protocol_kernel.py
- source_format: py
- merged_variants: 2 (test_xz_protocol_kernel.py.txt; test_xz_protocol_kernel.txt)
- text_sha256: d3b557985bc571b535d021792cb0cd772446ecdeb317177b5305229cfaafb228

# XZ Protocol v0.75 test suite
"""
test_xz_protocol_kernel.py -- Exhaustive 3^5=243 kernel tests + adversarial.
"""
import pytest
from xz_protocol_kernel import (
    TruthValue, KernelDecision, KernelError,
    ConjunctVector, KernelResult, CONJUNCT_NAMES,
    evaluate_kernel, generate_exhaustive_vectors,
)

T, F, U = TruthValue.TRUE, TruthValue.FALSE, TruthValue.UNKNOWN

class TestExhaustive243:
    def test_count(self):
        assert len(generate_exhaustive_vectors()) == 243

    def test_all_true_allows(self):
        r = evaluate_kernel(ConjunctVector(T,T,T,T,T))
        assert r.decision == KernelDecision.ALLOW
        assert r.false_conjuncts == () and r.unknown_conjuncts == ()

    def test_any_false_denies_false(self):
        for i in range(5):
            vals = [T]*5; vals[i] = F
            r = evaluate_kernel(ConjunctVector(*vals))
            assert r.decision == KernelDecision.DENY_FALSE

    def test_false_dominates_unknown(self):
        r = evaluate_kernel(ConjunctVector(F,U,T,T,T))
        assert r.decision == KernelDecision.DENY_FALSE

    def test_any_unknown_no_false_denies_unknown(self):
        for i in range(5):
            vals = [T]*5; vals[i] = U
            r = evaluate_kernel(ConjunctVector(*vals))
            assert r.decision == KernelDecision.DENY_UNKNOWN

    def test_all_false(self):
        r = evaluate_kernel(ConjunctVector(F,F,F,F,F))
        assert r.decision == KernelDecision.DENY_FALSE
        assert len(r.false_conjuncts) == 5

    def test_all_unknown(self):
        r = evaluate_kernel(ConjunctVector(U,U,U,U,U))
        assert r.decision == KernelDecision.DENY_UNKNOWN
        assert len(r.unknown_conjuncts) == 5

    def test_exhaustive_decision_correctness(self):
        """Every one of 243 vectors produces the correct decision."""
        for v in generate_exhaustive_vectors():
            r = evaluate_kernel(v)
            vals = list(v.as_dict().values())
            has_false = any(x == F for x in vals)
            has_unknown = any(x == U for x in vals)
            if has_false:
                assert r.decision == KernelDecision.DENY_FALSE, f"Expected DENY_FALSE for {v}"
            elif has_unknown:
                assert r.decision == KernelDecision.DENY_UNKNOWN, f"Expected DENY_UNKNOWN for {v}"
            else:
                assert r.decision == KernelDecision.ALLOW, f"Expected ALLOW for {v}"

    def test_exhaustive_reason_codes(self):
        for v in generate_exhaustive_vectors():
            r = evaluate_kernel(v)
            if r.decision == KernelDecision.DENY_FALSE:
                assert len(r.false_conjuncts) > 0
                assert all("E-FALSE-" in c for c in r.reason_codes)
            elif r.decision == KernelDecision.DENY_UNKNOWN:
                assert len(r.false_conjuncts) == 0
                assert len(r.unknown_conjuncts) > 0
            else:
                assert r.reason_codes == ()

class TestDenyClassDistinct:
    """DENY_FALSE and DENY_UNKNOWN are NEVER collapsed (CR-3, XZ-S9)."""
    def test_never_equal(self):
        assert KernelDecision.DENY_FALSE != KernelDecision.DENY_UNKNOWN

    def test_false_dominates_in_all_mixed(self):
        """If both FALSE and UNKNOWN present, decision is DENY_FALSE."""
        r = evaluate_kernel(ConjunctVector(F,U,F,U,T))
        assert r.decision == KernelDecision.DENY_FALSE

class TestInputValidation:
    def test_string_rejected(self):
        with pytest.raises(KernelError):
            evaluate_kernel("ALLOW")

    def test_string_truth_rejected(self):
        with pytest.raises(KernelError):
            ConjunctVector("TRUE",T,T,T,T)

class TestNoCallerSuppliedDecision:
    """The kernel takes a vector, not a decision. No bypass."""
    def test_result_is_computed(self):
        r = evaluate_kernel(ConjunctVector(T,F,T,T,T))
        assert r.decision == KernelDecision.DENY_FALSE
        assert "EffectTypeValid" in r.false_conjuncts

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

---

# Bismillah ir-Rahman ir-Rahim
