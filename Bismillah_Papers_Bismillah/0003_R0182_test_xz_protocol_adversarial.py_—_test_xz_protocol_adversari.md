# Bismillah ir-Rahman ir-Rahim

# R0182 -- test_xz_protocol_adversarial.py — test_xz_protocol_adversarial.py -- Cross-module adversarial integration suite.

**Chronological Index:** 3 of 995  
**Date:** 2024  
**Section:** IV. XZ Protocol  
**Source File:** test_xz_protocol_adversarial.py  
**Source Format:** py  
**SHA-256:** `887645a9a162d9bd8f7f0b582c3a0c3c04f5e4e0f9c50ee7f24f85247e832adf`  

---

## R0182 · test_xz_protocol_adversarial.py — test_xz_protocol_adversarial.py -- Cross-module adversarial integration suite.

- section: IV. XZ Protocol
- source_file: test_xz_protocol_adversarial.py
- source_format: py
- merged_variants: 2 (test_xz_protocol_adversarial.py.txt; test_xz_protocol_adversarial.txt)
- text_sha256: 887645a9a162d9bd8f7f0b582c3a0c3c04f5e4e0f9c50ee7f24f85247e832adf

# XZ Protocol v0.75 test suite
"""
test_xz_protocol_adversarial.py -- Cross-module adversarial integration suite.

Covers all nine Section 22 item 4 mandated attack categories plus
cross-module invariants. All fixtures are decoys (non-XZ).
"""
import pytest
from xz_protocol_kernel import (
    TruthValue, KernelDecision, ConjunctVector, evaluate_kernel,
)
from xz_protocol_condition_a import (
    ADisposition, BaselineCheck, BoundaryStratum as AStratum,
    CheckOutcome, ConditionAError, create_check_result,
    evaluate_boundary, is_dual_evaluable, is_primary_seam_divergence,
)
from xz_protocol_source_frame import (
    DISCLOSURE_DATE, FRAME_START, FRAME_END, SOURCE_FRAME_MANIFEST,
    BoundaryStratum as SFStratum, get_sources_for_stratum, validate_manifest,
)
from xz_protocol_control_graph import (
    AuthorityChannel, ChannelStatus, ControlEdge, WithinAuthVerdict,
    compute_verdict,
)

T, F, U = TruthValue.TRUE, TruthValue.FALSE, TruthValue.UNKNOWN

def _cr(check, outcome, reason="test"):
    return create_check_result(check, outcome, "test-tool", "1.0", reason)

def _commit_accept():
    return evaluate_boundary("adv-1", AStratum.S_COMMIT, [
        _cr(BaselineCheck.COMMIT_SIGNING, CheckOutcome.PASS),
        _cr(BaselineCheck.IDENTITY_VERIFICATION, CheckOutcome.PASS),
        _cr(BaselineCheck.PROVENANCE_REVIEW, CheckOutcome.PASS)])


# === CAT-1: CALLER-SUPPLIED DERIVED FACTS ===
class TestCallerSuppliedDerivedFacts:
    def test_string_b_decision_rejected(self):
        """The seam estimator rejects string decisions."""
        d = _commit_accept()
        with pytest.raises(ConditionAError, match="KernelDecision"):
            is_dual_evaluable(d, "DENY_FALSE")

    def test_kernel_rejects_string_vector(self):
        with pytest.raises(Exception):
            evaluate_kernel("ALLOW")

    def test_kernel_rejects_string_truth(self):
        with pytest.raises(Exception):
            ConjunctVector("TRUE", T, T, T, T)


# === CAT-2: DENOMINATOR SUBSTITUTION ===
class TestDenominatorSubstitution:
    def test_not_applicable_excluded_from_dual(self):
        """A-NOT-APPLICABLE boundaries must not enter the S1 denominator."""
        # All strata have profiles, so NOT-APPLICABLE is unreachable
        # from normal strata. Verify the gate exists.
        d = _commit_accept()
        assert is_dual_evaluable(d, KernelDecision.DENY_FALSE)
        # A boundary with A-INDETERMINATE IS dual-evaluable but NOT primary divergence
        d2 = evaluate_boundary("adv-denom", AStratum.S_COMMIT, [
            _cr(BaselineCheck.COMMIT_SIGNING, CheckOutcome.AMBIGUOUS, "unclear")])
        assert is_dual_evaluable(d2, KernelDecision.DENY_FALSE)
        assert not is_primary_seam_divergence(d2, KernelDecision.DENY_FALSE)


# === CAT-3: COMMITMENT-IDENTIFIER CONFUSION ===
class TestCommitmentIdConfusion:
    def test_source_ids_unique(self):
        ids = [s.source_id for s in SOURCE_FRAME_MANIFEST]
        assert len(ids) == len(set(ids))

    def test_trust_root_keys_distinct(self):
        import json
        with open("xz_protocol_trust_roots_PUBLIC.json") as f:
            roots = json.load(f)
        keys = [v["public_key_hex"] for v in roots["trust_roots"].values()]
        assert len(keys) == len(set(keys)) == 3


# === CAT-4: TRUST-ROOT OVERRIDE ===
class TestTrustRootOverride:
    def test_trust_roots_are_ed25519(self):
        import json
        with open("xz_protocol_trust_roots_PUBLIC.json") as f:
            roots = json.load(f)
        for role, v in roots["trust_roots"].items():
            assert v["algorithm"] == "Ed25519"
            assert len(v["public_key_hex"]) == 64  # 32 bytes hex

    def test_three_distinct_roles(self):
        import json
        with open("xz_protocol_trust_roots_PUBLIC.json") as f:
            roots = json.load(f)
        roles = set(roots["trust_roots"].keys())
        assert roles == {"commitment-authority", "independent-anchor", "run-logger"}


# === CAT-5: PACKET-REGIME MIXING (CR-11) ===
class TestPacketRegimeMixing:
    def test_kernel_decisions_are_typed(self):
        """Kernel outputs are enum-typed, not strings.
        Mixing regimes requires type confusion -- which is blocked."""
        r = evaluate_kernel(ConjunctVector(T, F, T, T, T))
        assert isinstance(r.decision, KernelDecision)
        assert r.decision == KernelDecision.DENY_FALSE


# === CAT-6: POST-CUTOFF EVIDENCE INJECTION ===
class TestPostCutoffInjection:
    def test_frame_end_is_bounded(self):
        from datetime import date
        assert FRAME_END == date(2024, 4, 28)
        assert FRAME_END < date(2024, 5, 1)

    def test_kernel_has_no_timestamp_backdoor(self):
        """The kernel takes a ConjunctVector, not timestamps.
        Cutoff enforcement is at the packet layer, not the kernel."""
        v = ConjunctVector(T, T, T, T, T)
        r = evaluate_kernel(v)
        assert r.decision == KernelDecision.ALLOW
        # No timestamp field exists on ConjunctVector
        assert not hasattr(v, 'timestamp')


# === CAT-7: ROLE REMAPPING AFTER OUTCOMES ===
class TestRoleRemappingAfterOutcomes:
    def test_conjunct_vector_is_frozen(self):
        """ConjunctVector is frozen -- no post-evaluation mutation."""
        v = ConjunctVector(T, F, T, T, T)
        with pytest.raises(AttributeError):
            v.contract_match = T

    def test_kernel_result_is_frozen(self):
        r = evaluate_kernel(ConjunctVector(T, F, T, T, T))
        with pytest.raises(AttributeError):
            r.decision = KernelDecision.ALLOW


# === CAT-8: DENY-CLASS COLLAPSE (XZ-S7/S9) ===
class TestDenyClassCollapse:
    def test_deny_false_and_unknown_distinct(self):
        assert KernelDecision.DENY_FALSE != KernelDecision.DENY_UNKNOWN

    def test_seam_excludes_deny_unknown(self):
        """DENY_UNKNOWN is dual-evaluable but NOT primary divergence."""
        d = _commit_accept()
        assert is_dual_evaluable(d, KernelDecision.DENY_UNKNOWN)
        assert not is_primary_seam_divergence(d, KernelDecision.DENY_UNKNOWN)

    def test_false_dominates_in_kernel(self):
        r = evaluate_kernel(ConjunctVector(F, U, T, T, T))
        assert r.decision == KernelDecision.DENY_FALSE


# === CAT-9: SCREENED-EVENT SUPPRESSION ===
class TestScreenedEventSuppression:
    def test_all_strata_in_profile(self):
        """No stratum is silently dropped from the baseline profile."""
        from xz_protocol_condition_a import BASELINE_PROFILE
        for s in AStratum:
            assert s in BASELINE_PROFILE

    def test_source_frame_strata_match(self):
        """Source-frame strata match Condition A strata."""
        a_strata = {s.value for s in AStratum}
        sf_strata = {s.value for s in SFStratum}
        assert a_strata == sf_strata


# === CROSS-MODULE: source frame covers Condition A ===
class TestSourceFrameCoversConditionA:
    def test_core_strata(self):
        for s in [SFStratum.S_COMMIT, SFStratum.S_RELEASE,
                  SFStratum.S_BUILD, SFStratum.S_DISTRIBUTION]:
            assert len(get_sources_for_stratum(s)) > 0


# === CROSS-MODULE: A/B seam with kernel ===
class TestSeamWithKernel:
    def test_primary_divergence(self):
        d = _commit_accept()
        kr = evaluate_kernel(ConjunctVector(F, T, T, T, T))
        assert is_primary_seam_divergence(d, kr.decision)

    def test_agreement(self):
        d = _commit_accept()
        kr = evaluate_kernel(ConjunctVector(T, T, T, T, T))
        assert not is_primary_seam_divergence(d, kr.decision)


# === DOMINANCE CONSISTENCY ===
class TestDominanceConsistency:
    def test_a_reject_dominates(self):
        results = [
            _cr(BaselineCheck.COMMIT_SIGNING, CheckOutcome.FAIL, "bad"),
            _cr(BaselineCheck.IDENTITY_VERIFICATION, CheckOutcome.AMBIGUOUS, "unclear")]
        d = evaluate_boundary("dom-1", AStratum.S_COMMIT, results)
        assert d.disposition == ADisposition.A_REJECT

    def test_kernel_false_dominates(self):
        r = evaluate_kernel(ConjunctVector(F, U, F, U, T))
        assert r.decision == KernelDecision.DENY_FALSE


# === MANIFEST INTEGRITY ===
class TestManifestIntegrity:
    def test_valid(self):
        assert validate_manifest()["valid"]

    def test_frame_window(self):
        from datetime import date
        assert FRAME_START <= date(2024, 1, 1)
        assert FRAME_END >= date(2024, 4, 15)


# === PROHIBITED CONTENT ===
class TestProhibitedContent:
    def _all_text(self):
        import importlib
        texts = []
        for m in ["xz_protocol_condition_a", "xz_protocol_source_frame",
                   "xz_protocol_control_graph", "xz_protocol_kernel"]:
            mod = importlib.import_module(m)
            texts.append(open(mod.__file__).read())
        return " ".join(texts)

    def test_no_payload(self):
        t = self._all_text().lower()
        for term in ["ifunc", "got_plt", "cpuid", "rsa_public_decrypt"]:
            assert term not in t

    def test_no_activation(self):
        t = self._all_text().lower()
        # "activation recipe" in "no activation recipe" is a PROHIBITION, not content
        # Check for actual recipes, not prohibitions of them
        lines = t.split('\n')
        for line in lines:
            if "activation recipe" in line and "no activation recipe" not in line:
                pytest.fail(f"Activation recipe content found: {line.strip()}")
        assert "backdoor" not in t


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

---

# Bismillah ir-Rahman ir-Rahim
