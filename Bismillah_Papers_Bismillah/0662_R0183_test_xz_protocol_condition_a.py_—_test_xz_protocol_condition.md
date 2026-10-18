# Bismillah ir-Rahman ir-Rahim

# R0183 -- test_xz_protocol_condition_a.py — test_xz_protocol_condition_a.py -- Adversarial test suite for Condition A.

**Chronological Index:** 662 of 995  
**Date:** Undated  
**Section:** IV. XZ Protocol  
**Source File:** test_xz_protocol_condition_a.py  
**Source Format:** py  
**SHA-256:** `7bfa5a4636d86190a3793ff21e39343fc806b21f8510ad2769dc31b6d231067a`  

---

## R0183 · test_xz_protocol_condition_a.py — test_xz_protocol_condition_a.py -- Adversarial test suite for Condition A.

- section: IV. XZ Protocol
- source_file: test_xz_protocol_condition_a.py
- source_format: py
- merged_variants: 2 (test_xz_protocol_condition_a.py.txt; test_xz_protocol_condition_a.txt)
- text_sha256: 7bfa5a4636d86190a3793ff21e39343fc806b21f8510ad2769dc31b6d231067a

# XZ Protocol v0.75 test suite
"""
test_xz_protocol_condition_a.py -- Adversarial test suite for Condition A.

Tests the executable baseline disposition function against decoy boundaries
(non-XZ inputs). No XZ-specific data in this file.
"""
import pytest
from xz_protocol_kernel import KernelDecision
from xz_protocol_condition_a import (
    ADisposition, BaselineCheck, BaselineCheckResult, BoundaryStratum,
    CheckOutcome, ConditionAError, BoundaryDisposition, BASELINE_PROFILE,
    create_check_result, evaluate_boundary, is_dual_evaluable,
    is_primary_seam_divergence,
)


def _cr(check, outcome, reason="test"):
    return create_check_result(check, outcome, "test-tool", "1.0", reason)


# === DISPOSITION VOCABULARY ===

class TestDispositionVocabulary:
    def test_all_four_labels_exist(self):
        assert len(ADisposition) == 4

    def test_values(self):
        assert ADisposition.A_ACCEPT.value == "A-ACCEPT"
        assert ADisposition.A_REJECT.value == "A-REJECT"
        assert ADisposition.A_INDETERMINATE.value == "A-INDETERMINATE"
        assert ADisposition.A_NOT_APPLICABLE.value == "A-NOT-APPLICABLE"


# === BASELINE PROFILE ===

class TestBaselineProfile:
    def test_all_strata_have_profiles(self):
        for s in BoundaryStratum:
            assert s in BASELINE_PROFILE

    def test_all_profiles_nonempty(self):
        for s, checks in BASELINE_PROFILE.items():
            assert len(checks) > 0, f"{s} has empty profile"


# === ACCEPT (all mandatory pass) ===

class TestAccept:
    def test_commit_all_pass(self):
        results = [
            _cr(BaselineCheck.COMMIT_SIGNING, CheckOutcome.PASS),
            _cr(BaselineCheck.IDENTITY_VERIFICATION, CheckOutcome.PASS),
            _cr(BaselineCheck.PROVENANCE_REVIEW, CheckOutcome.PASS),
        ]
        d = evaluate_boundary("decoy-1", BoundaryStratum.S_COMMIT, results)
        assert d.disposition == ADisposition.A_ACCEPT
        assert not d.has_failure
        assert not d.has_indeterminate

    def test_release_all_pass(self):
        results = [
            _cr(BaselineCheck.SIGNATURE_VERIFICATION, CheckOutcome.PASS),
            _cr(BaselineCheck.SOURCE_TO_ARTIFACT_COMPARISON, CheckOutcome.PASS),
            _cr(BaselineCheck.IDENTITY_VERIFICATION, CheckOutcome.PASS),
            _cr(BaselineCheck.PROVENANCE_REVIEW, CheckOutcome.PASS),
            _cr(BaselineCheck.SLSA_PROVENANCE, CheckOutcome.PASS),
        ]
        d = evaluate_boundary("decoy-2", BoundaryStratum.S_RELEASE, results)
        assert d.disposition == ADisposition.A_ACCEPT


# === REJECT (at least one failure) ===

class TestReject:
    def test_one_failure(self):
        results = [
            _cr(BaselineCheck.COMMIT_SIGNING, CheckOutcome.FAIL, "bad sig"),
            _cr(BaselineCheck.IDENTITY_VERIFICATION, CheckOutcome.PASS),
            _cr(BaselineCheck.PROVENANCE_REVIEW, CheckOutcome.PASS),
        ]
        d = evaluate_boundary("decoy-3", BoundaryStratum.S_COMMIT, results)
        assert d.disposition == ADisposition.A_REJECT
        assert d.has_failure

    def test_failure_dominates_indeterminate(self):
        """A-REJECT > A-INDETERMINATE (parallels FALSE > UNKNOWN)."""
        results = [
            _cr(BaselineCheck.COMMIT_SIGNING, CheckOutcome.FAIL, "bad sig"),
            _cr(BaselineCheck.IDENTITY_VERIFICATION, CheckOutcome.AMBIGUOUS, "unclear"),
            # PROVENANCE_REVIEW absent -> INDETERMINATE
        ]
        d = evaluate_boundary("decoy-4", BoundaryStratum.S_COMMIT, results)
        assert d.disposition == ADisposition.A_REJECT
        assert d.has_failure and d.has_indeterminate


# === INDETERMINATE (no failure, but mandatory absent/ambiguous) ===

class TestIndeterminate:
    def test_missing_mandatory(self):
        results = [
            _cr(BaselineCheck.COMMIT_SIGNING, CheckOutcome.PASS),
            _cr(BaselineCheck.IDENTITY_VERIFICATION, CheckOutcome.PASS),
            # PROVENANCE_REVIEW absent
        ]
        d = evaluate_boundary("decoy-5", BoundaryStratum.S_COMMIT, results)
        assert d.disposition == ADisposition.A_INDETERMINATE
        assert d.has_indeterminate
        assert BaselineCheck.PROVENANCE_REVIEW in d.mandatory_absent

    def test_ambiguous_check(self):
        results = [
            _cr(BaselineCheck.COMMIT_SIGNING, CheckOutcome.PASS),
            _cr(BaselineCheck.IDENTITY_VERIFICATION, CheckOutcome.AMBIGUOUS, "shared account"),
            _cr(BaselineCheck.PROVENANCE_REVIEW, CheckOutcome.PASS),
        ]
        d = evaluate_boundary("decoy-6", BoundaryStratum.S_COMMIT, results)
        assert d.disposition == ADisposition.A_INDETERMINATE

    def test_unverifiable_check(self):
        results = [
            _cr(BaselineCheck.COMMIT_SIGNING, CheckOutcome.UNVERIFIABLE, "key expired"),
            _cr(BaselineCheck.IDENTITY_VERIFICATION, CheckOutcome.PASS),
            _cr(BaselineCheck.PROVENANCE_REVIEW, CheckOutcome.PASS),
        ]
        d = evaluate_boundary("decoy-7", BoundaryStratum.S_COMMIT, results)
        assert d.disposition == ADisposition.A_INDETERMINATE

    def test_stale_check(self):
        results = [
            _cr(BaselineCheck.SOURCE_TO_ARTIFACT_COMPARISON, CheckOutcome.PASS),
            _cr(BaselineCheck.REPRODUCIBLE_BUILD, CheckOutcome.STALE, "recipe outdated"),
            _cr(BaselineCheck.STATIC_ANALYSIS, CheckOutcome.PASS),
            _cr(BaselineCheck.MALWARE_SCAN, CheckOutcome.PASS),
        ]
        d = evaluate_boundary("decoy-8", BoundaryStratum.S_BUILD, results)
        assert d.disposition == ADisposition.A_INDETERMINATE


# === NOT-APPLICABLE ===

class TestNotApplicable:
    def test_all_strata_have_checks(self):
        """All six strata have mandatory checks, so A-NOT-APPLICABLE
        only fires if a stratum were added with no profile."""
        # Verify current profile is complete
        for s in BoundaryStratum:
            assert len(BASELINE_PROFILE[s]) > 0


# === DUAL-EVALUABILITY ===

class TestDualEvaluable:
    def test_accept_deny_false(self):
        results = [
            _cr(BaselineCheck.COMMIT_SIGNING, CheckOutcome.PASS),
            _cr(BaselineCheck.IDENTITY_VERIFICATION, CheckOutcome.PASS),
            _cr(BaselineCheck.PROVENANCE_REVIEW, CheckOutcome.PASS),
        ]
        d = evaluate_boundary("decoy-9", BoundaryStratum.S_COMMIT, results)
        assert is_dual_evaluable(d, KernelDecision.DENY_FALSE)
        assert is_primary_seam_divergence(d, KernelDecision.DENY_FALSE)

    def test_accept_allow_no_divergence(self):
        results = [
            _cr(BaselineCheck.COMMIT_SIGNING, CheckOutcome.PASS),
            _cr(BaselineCheck.IDENTITY_VERIFICATION, CheckOutcome.PASS),
            _cr(BaselineCheck.PROVENANCE_REVIEW, CheckOutcome.PASS),
        ]
        d = evaluate_boundary("decoy-10", BoundaryStratum.S_COMMIT, results)
        assert is_dual_evaluable(d, KernelDecision.ALLOW)
        assert not is_primary_seam_divergence(d, KernelDecision.ALLOW)

    def test_accept_deny_unknown_not_primary(self):
        """DENY_UNKNOWN is never primary seam divergence (CR-3)."""
        results = [
            _cr(BaselineCheck.COMMIT_SIGNING, CheckOutcome.PASS),
            _cr(BaselineCheck.IDENTITY_VERIFICATION, CheckOutcome.PASS),
            _cr(BaselineCheck.PROVENANCE_REVIEW, CheckOutcome.PASS),
        ]
        d = evaluate_boundary("decoy-11", BoundaryStratum.S_COMMIT, results)
        assert is_dual_evaluable(d, KernelDecision.DENY_UNKNOWN)
        assert not is_primary_seam_divergence(d, KernelDecision.DENY_UNKNOWN)


# === INPUT VALIDATION ===

class TestValidation:
    def test_string_stratum_rejected(self):
        with pytest.raises(ConditionAError, match="BoundaryStratum"):
            evaluate_boundary("b1", "S-COMMIT", [])

    def test_empty_boundary_id(self):
        with pytest.raises(ConditionAError, match="non-empty"):
            evaluate_boundary("", BoundaryStratum.S_COMMIT, [])

    def test_string_check_rejected(self):
        with pytest.raises(ConditionAError, match="BaselineCheck"):
            BaselineCheckResult("commit-signing", CheckOutcome.PASS,
                                "tool", "1.0", "reason")

    def test_string_outcome_rejected(self):
        with pytest.raises(ConditionAError, match="CheckOutcome"):
            BaselineCheckResult(BaselineCheck.COMMIT_SIGNING, "PASS",
                                "tool", "1.0", "reason")

    def test_duplicate_check_rejected(self):
        results = [
            _cr(BaselineCheck.COMMIT_SIGNING, CheckOutcome.PASS),
            _cr(BaselineCheck.COMMIT_SIGNING, CheckOutcome.FAIL, "dup"),
        ]
        with pytest.raises(ConditionAError, match="Duplicate"):
            evaluate_boundary("b2", BoundaryStratum.S_COMMIT, results)

    def test_invalid_b_decision(self):
        d = evaluate_boundary("b3", BoundaryStratum.S_COMMIT, [
            _cr(BaselineCheck.COMMIT_SIGNING, CheckOutcome.PASS),
            _cr(BaselineCheck.IDENTITY_VERIFICATION, CheckOutcome.PASS),
            _cr(BaselineCheck.PROVENANCE_REVIEW, CheckOutcome.PASS),
        ])
        with pytest.raises(ConditionAError):
            is_dual_evaluable(d, "INVALID_STRING")


# === SUPPLY-CHAIN DECOY SCENARIOS ===


    def test_not_applicable_on_mandatory_is_indeterminate(self):
        """F-SOL-XZ-3: NOT_APPLICABLE on mandatory -> A-INDETERMINATE."""
        results = [
            _cr(BaselineCheck.COMMIT_SIGNING, CheckOutcome.NOT_APPLICABLE, "na"),
            _cr(BaselineCheck.IDENTITY_VERIFICATION, CheckOutcome.PASS),
            _cr(BaselineCheck.PROVENANCE_REVIEW, CheckOutcome.PASS),
        ]
        d = evaluate_boundary("decoy-na", BoundaryStratum.S_COMMIT, results)
        assert d.disposition == ADisposition.A_INDETERMINATE

    def test_string_b_decision_rejected(self):
        """No caller-supplied string decisions (B-1 fix)."""
        results = [
            _cr(BaselineCheck.COMMIT_SIGNING, CheckOutcome.PASS),
            _cr(BaselineCheck.IDENTITY_VERIFICATION, CheckOutcome.PASS),
            _cr(BaselineCheck.PROVENANCE_REVIEW, CheckOutcome.PASS),
        ]
        d = evaluate_boundary("decoy-str", BoundaryStratum.S_COMMIT, results)
        with pytest.raises(ConditionAError, match="KernelDecision"):
            is_dual_evaluable(d, "DENY_FALSE")

class TestDecoyScenarios:
    def test_clean_release_with_reproducible_build(self):
        """Decoy: a legitimate release with full conventional checks."""
        results = [
            _cr(BaselineCheck.SIGNATURE_VERIFICATION, CheckOutcome.PASS, "GPG sig valid"),
            _cr(BaselineCheck.SOURCE_TO_ARTIFACT_COMPARISON, CheckOutcome.PASS, "tarball matches tag"),
            _cr(BaselineCheck.IDENTITY_VERIFICATION, CheckOutcome.PASS, "known maintainer"),
            _cr(BaselineCheck.PROVENANCE_REVIEW, CheckOutcome.PASS, "clean commit history"),
            _cr(BaselineCheck.SLSA_PROVENANCE, CheckOutcome.PASS, "SLSA L2 verified"),
        ]
        d = evaluate_boundary("decoy-clean-release", BoundaryStratum.S_RELEASE, results)
        assert d.disposition == ADisposition.A_ACCEPT

    def test_tampered_tarball_detected(self):
        """Decoy: source-to-artifact mismatch caught by conventional tools."""
        results = [
            _cr(BaselineCheck.SIGNATURE_VERIFICATION, CheckOutcome.PASS, "sig valid"),
            _cr(BaselineCheck.SOURCE_TO_ARTIFACT_COMPARISON, CheckOutcome.FAIL,
                 "tarball contains files not in tagged source"),
            _cr(BaselineCheck.IDENTITY_VERIFICATION, CheckOutcome.PASS),
            _cr(BaselineCheck.PROVENANCE_REVIEW, CheckOutcome.PASS),
            _cr(BaselineCheck.SLSA_PROVENANCE, CheckOutcome.PASS, "SLSA ok"),
        ]
        d = evaluate_boundary("decoy-tampered", BoundaryStratum.S_RELEASE, results)
        assert d.disposition == ADisposition.A_REJECT

    def test_missing_signature_indeterminate(self):
        """Decoy: release exists but GPG signature is absent."""
        results = [
            _cr(BaselineCheck.SIGNATURE_VERIFICATION, CheckOutcome.ABSENT, "no GPG sig found"),
            _cr(BaselineCheck.SOURCE_TO_ARTIFACT_COMPARISON, CheckOutcome.PASS),
            _cr(BaselineCheck.IDENTITY_VERIFICATION, CheckOutcome.PASS),
            _cr(BaselineCheck.PROVENANCE_REVIEW, CheckOutcome.PASS),
            _cr(BaselineCheck.SLSA_PROVENANCE, CheckOutcome.PASS, "SLSA ok"),
        ]
        d = evaluate_boundary("decoy-no-sig", BoundaryStratum.S_RELEASE, results)
        assert d.disposition == ADisposition.A_INDETERMINATE

    def test_build_with_obfuscated_input(self):
        """Decoy: build input contains binary blob, static analysis flags it."""
        results = [
            _cr(BaselineCheck.SOURCE_TO_ARTIFACT_COMPARISON, CheckOutcome.PASS),
            _cr(BaselineCheck.REPRODUCIBLE_BUILD, CheckOutcome.FAIL,
                 "build not reproducible; output differs from reference"),
            _cr(BaselineCheck.STATIC_ANALYSIS, CheckOutcome.FAIL,
                 "suspicious binary blob in test fixtures"),
            _cr(BaselineCheck.MALWARE_SCAN, CheckOutcome.PASS),
            _cr(BaselineCheck.STEP_ATTESTATION, CheckOutcome.PASS, "steps attested"),
        ]
        d = evaluate_boundary("decoy-obfuscated", BoundaryStratum.S_BUILD, results)
        assert d.disposition == ADisposition.A_REJECT
        assert d.has_failure

    def test_distribution_missing_checks(self):
        """Decoy: package admitted to repo with no dependency scan."""
        results = [
            _cr(BaselineCheck.PACKAGE_SIGNATURE, CheckOutcome.PASS),
            _cr(BaselineCheck.REPOSITORY_POLICY, CheckOutcome.PASS),
            _cr(BaselineCheck.DISTRIBUTION_CHANNEL_INTEGRITY, CheckOutcome.PASS),
            # DEPENDENCY_SCAN absent
        ]
        d = evaluate_boundary("decoy-no-depscan", BoundaryStratum.S_DISTRIBUTION, results)
        assert d.disposition == ADisposition.A_INDETERMINATE
        assert BaselineCheck.DEPENDENCY_SCAN in d.mandatory_absent


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

---

# Bismillah ir-Rahman ir-Rahim
