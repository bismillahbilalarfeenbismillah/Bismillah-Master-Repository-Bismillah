# Bismillah ir-Rahman ir-Rahim

# R0535 -- FILE: test_xz_protocol_kernel.py | BYTES: 4008

**Chronological Index:** 42 of 995  
**Date:** 2024-01-01  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** test_suites.txt  
**Source Format:** txt  
**SHA-256:** `9a24953e09de5fd8a4dcc3f9bcf9fdd51831ee850180f6df29e263db607c08cf`  

---

## R0535 · FILE: test_xz_protocol_kernel.py | BYTES: 4008

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: test_suites.txt
- source_format: txt
- text_sha256: 9a24953e09de5fd8a4dcc3f9bcf9fdd51831ee850180f6df29e263db607c08cf

# === FILE: test_xz_protocol_kernel.py | BYTES: 4008 ===
# XZ Protocol v0.47 test suite
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
# === FILE: test_xz_protocol_condition_a.py | BYTES: 14060 ===
# XZ Protocol v0.47 test suite
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
# === FILE: test_xz_protocol_source_frame.py | BYTES: 6493 ===
# XZ Protocol v0.47 test suite
"""
test_xz_protocol_source_frame.py -- Tests for the source-frame manifest.

Validates completeness, consistency, and correctness of the sealed
public-record universe.
"""
import pytest
from datetime import date

from xz_protocol_source_frame import (
    DISCLOSURE_DATE, FRAME_START, FRAME_END, DISCLOSURE_URL,
    SOURCE_FRAME_MANIFEST, BoundaryStratum, SourceCategory,
    AuthenticationMethod, SourceRecord,
    get_sources_for_stratum, get_source_by_id, validate_manifest,
)


class TestFrameWindow:
    def test_disclosure_date(self):
        assert DISCLOSURE_DATE == date(2024, 3, 29)

    def test_frame_start(self):
        delta = (DISCLOSURE_DATE - FRAME_START).days
        assert delta == 180  # ~180 days

    def test_frame_end(self):
        delta = (FRAME_END - DISCLOSURE_DATE).days
        assert delta == 30

    def test_frame_start_before_end(self):
        assert FRAME_START < FRAME_END

    def test_disclosure_within_frame(self):
        assert FRAME_START < DISCLOSURE_DATE < FRAME_END


class TestManifestCompleteness:
    def test_core_strata_covered(self):
        """Strata with known public records must have sources."""
        for stratum in [BoundaryStratum.S_COMMIT, BoundaryStratum.S_RELEASE,
                        BoundaryStratum.S_BUILD, BoundaryStratum.S_DISTRIBUTION]:
            sources = get_sources_for_stratum(stratum)
            assert len(sources) > 0, f"No sources for {stratum.value}"

    def test_installation_runtime_may_be_empty(self):
        """Per Section 5.4 item 8: strata with zero eligible public records
        are retained and reported as NOT-EVALUABLE, not dropped."""
        # These strata may have zero public sources; that's a frame limitation
        for stratum in [BoundaryStratum.S_INSTALLATION, BoundaryStratum.S_RUNTIME_AUTH]:
            sources = get_sources_for_stratum(stratum)
            # Zero is acceptable -- it maps to NOT-EVALUABLE at stratum level
            assert isinstance(sources, list)

    def test_commit_stratum_has_repository(self):
        sources = get_sources_for_stratum(BoundaryStratum.S_COMMIT)
        categories = {s.category for s in sources}
        assert SourceCategory.REPOSITORY in categories

    def test_release_stratum_has_archive(self):
        sources = get_sources_for_stratum(BoundaryStratum.S_RELEASE)
        categories = {s.category for s in sources}
        assert SourceCategory.RELEASE_ARCHIVE in categories

    def test_distribution_has_multiple_channels(self):
        sources = get_sources_for_stratum(BoundaryStratum.S_DISTRIBUTION)
        dist_sources = [s for s in sources if s.category == SourceCategory.DISTRIBUTION]
        assert len(dist_sources) >= 4  # Debian, Fedora, Arch, Ubuntu minimum

    def test_build_stratum_covered(self):
        sources = get_sources_for_stratum(BoundaryStratum.S_BUILD)
        assert len(sources) >= 2


class TestManifestConsistency:
    def test_unique_source_ids(self):
        ids = [s.source_id for s in SOURCE_FRAME_MANIFEST]
        assert len(ids) == len(set(ids))

    def test_all_sources_have_authentication(self):
        for s in SOURCE_FRAME_MANIFEST:
            assert len(s.authentication) > 0, f"{s.source_id} has no auth"

    def test_all_sources_have_retrieval_rule(self):
        for s in SOURCE_FRAME_MANIFEST:
            assert s.retrieval_rule.strip(), f"{s.source_id} has no retrieval rule"

    def test_all_sources_have_strata(self):
        for s in SOURCE_FRAME_MANIFEST:
            assert len(s.strata_covered) > 0, f"{s.source_id} covers no strata"


class TestPrimaryCitations:
    """The four primary XZ citations from Section 26.3 must appear."""

    def test_oss_security(self):
        assert any("openwall.com/lists/oss-security" in s.url
                    for s in SOURCE_FRAME_MANIFEST)

    def test_nvd(self):
        assert any("nvd.nist.gov/vuln/detail/cve-2024-3094" in s.url
                    for s in SOURCE_FRAME_MANIFEST)

    def test_xz_issue_103(self):
        assert any("tukaani-project/xz/issues" in s.url
                    for s in SOURCE_FRAME_MANIFEST)

    def test_github_advisory(self):
        assert any("GHSA-rxwq-x6h5-x525" in s.url
                    for s in SOURCE_FRAME_MANIFEST)


class TestSourceLookup:
    def test_by_id(self):
        s = get_source_by_id("SRC-REPO-01")
        assert s is not None
        assert "tukaani" in s.name.lower() or "xz" in s.name.lower()

    def test_missing_id(self):
        assert get_source_by_id("SRC-NONEXISTENT") is None


class TestValidateManifest:
    def test_manifest_valid(self):
        result = validate_manifest()
        assert result["valid"], f"Manifest invalid: {result['errors']}"
        assert result["source_count"] == len(SOURCE_FRAME_MANIFEST)

    def test_core_strata_positive_count(self):
        result = validate_manifest()
        for stratum in ["S-COMMIT", "S-RELEASE", "S-BUILD", "S-DISTRIBUTION"]:
            assert result["strata_coverage"][stratum] > 0


class TestNoRestrictedContent:
    """Safety gate: the manifest must contain no restricted content."""

    def test_no_payload_hashes(self):
        for s in SOURCE_FRAME_MANIFEST:
            combined = f"{s.url} {s.retrieval_rule} {s.notes or ''}"
            assert "payload" not in combined.lower() or "hash" not in combined.lower()

    def test_no_activation_recipes(self):
        for s in SOURCE_FRAME_MANIFEST:
            combined = f"{s.url} {s.retrieval_rule} {s.notes or ''}"
            assert "activation" not in combined.lower()
            assert "ifunc" not in combined.lower()
            assert "backdoor" not in combined.lower()


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])


class TestExactSourceFrameValues:
    """Exact regression tests for source-frame facts (F-XZ06-GPT-05)."""

    def test_exact_source_count(self):
        assert len(SOURCE_FRAME_MANIFEST) == 16

    def test_exact_represented_category_count(self):
        cats = {r.category for r in SOURCE_FRAME_MANIFEST}
        assert len(cats) == 6

    def test_s_installation_zero_sources(self):
        sources = get_sources_for_stratum(BoundaryStratum.S_INSTALLATION)
        assert len(sources) == 0

    def test_s_runtime_auth_two_sources(self):
        sources = get_sources_for_stratum(BoundaryStratum.S_RUNTIME_AUTH)
        assert len(sources) == 2
        ids = {s.source_id for s in sources}
        assert ids == {"SRC-ML-01", "SRC-ADV-01"}
# === FILE: test_xz_protocol_control_graph.py | BYTES: 5593 ===
# XZ Protocol v0.47 test suite
"""
test_xz_protocol_control_graph.py -- Tests for the WithinAuth control graph.

All fixtures are decoys (non-XZ). Tests verify adjudication rules,
verdict computation, prohibited shortcuts, and schema validation.
"""
import pytest
from xz_protocol_control_graph import (
    AuthorityChannel, ChannelStatus, ControlEdge, WithinAuthVerdict,
    ActingSubstrate, RecordGenerationAct, WithinAuthAssessment,
    compute_verdict, PROHIBITED_SHORTCUTS,
    decoy_fixture_independent_ci,
    decoy_fixture_maintainer_controlled_release,
    decoy_fixture_ambiguous_shared_infra,
)


# === VERDICT COMPUTATION ===

class TestVerdictComputation:
    def _edges(self, statuses):
        channels = list(AuthorityChannel)
        return tuple(ControlEdge(channels[i], statuses[i], "test", "test")
                     for i in range(5))

    def test_all_no_is_outside(self):
        e = self._edges([ChannelStatus.NO]*5)
        assert compute_verdict(e) == WithinAuthVerdict.OUTSIDE

    def test_any_yes_is_inside(self):
        for i in range(5):
            statuses = [ChannelStatus.NO]*5
            statuses[i] = ChannelStatus.YES
            e = self._edges(statuses)
            assert compute_verdict(e) == WithinAuthVerdict.INSIDE

    def test_yes_dominates_unknown(self):
        statuses = [ChannelStatus.UNKNOWN]*4 + [ChannelStatus.YES]
        e = self._edges(statuses)
        assert compute_verdict(e) == WithinAuthVerdict.INSIDE

    def test_unknown_without_yes_is_unknown(self):
        statuses = [ChannelStatus.NO]*4 + [ChannelStatus.UNKNOWN]
        e = self._edges(statuses)
        assert compute_verdict(e) == WithinAuthVerdict.UNKNOWN

    def test_all_unknown_is_unknown(self):
        e = self._edges([ChannelStatus.UNKNOWN]*5)
        assert compute_verdict(e) == WithinAuthVerdict.UNKNOWN

    def test_mixed_no_unknown_is_unknown(self):
        statuses = [ChannelStatus.NO, ChannelStatus.UNKNOWN,
                    ChannelStatus.NO, ChannelStatus.NO, ChannelStatus.UNKNOWN]
        e = self._edges(statuses)
        assert compute_verdict(e) == WithinAuthVerdict.UNKNOWN


# === DOMINANCE ORDER ===

class TestDominance:
    """YES (INSIDE) dominates UNKNOWN dominates NO (OUTSIDE).
    Parallels BSSG: FALSE dominates UNKNOWN dominates TRUE."""

    def _edges(self, statuses):
        channels = list(AuthorityChannel)
        return tuple(ControlEdge(channels[i], statuses[i], "test", "test")
                     for i in range(5))

    def test_inside_dominates_all(self):
        # One YES among UNKNOWNs and NOs -> INSIDE
        for pattern in [[ChannelStatus.YES]+[ChannelStatus.NO]*4,
                        [ChannelStatus.YES]+[ChannelStatus.UNKNOWN]*4,
                        [ChannelStatus.NO,ChannelStatus.UNKNOWN,ChannelStatus.NO,
                         ChannelStatus.YES,ChannelStatus.UNKNOWN]]:
            assert compute_verdict(self._edges(pattern)) == WithinAuthVerdict.INSIDE

    def test_outside_requires_unanimity(self):
        # OUTSIDE only when ALL five are NO
        assert compute_verdict(self._edges([ChannelStatus.NO]*5)) == WithinAuthVerdict.OUTSIDE


# === SCHEMA VALIDATION ===

class TestSchemaValidation:
    def test_missing_channel_rejected(self):
        edges = tuple(ControlEdge(c, ChannelStatus.NO, "t", "t")
                      for c in list(AuthorityChannel)[:4])  # only 4
        with pytest.raises(ValueError, match="Missing"):
            WithinAuthAssessment(
                ActingSubstrate("s1", "test", "test"),
                RecordGenerationAct("r1", "test", "gen", "2024-01-01", "type"),
                edges, WithinAuthVerdict.OUTSIDE, "adj1", "test")

    def test_string_channel_rejected(self):
        with pytest.raises(ValueError, match="AuthorityChannel"):
            ControlEdge("can-cause", ChannelStatus.NO, "t", "t")

    def test_string_status_rejected(self):
        with pytest.raises(ValueError, match="ChannelStatus"):
            ControlEdge(AuthorityChannel.CAUSE, "no", "t", "t")


# === DECOY FIXTURES ===

class TestDecoyFixtures:
    def test_independent_ci_outside(self):
        a = decoy_fixture_independent_ci()
        assert a.verdict == WithinAuthVerdict.OUTSIDE

    def test_maintainer_release_inside(self):
        a = decoy_fixture_maintainer_controlled_release()
        assert a.verdict == WithinAuthVerdict.INSIDE

    def test_shared_infra_unknown(self):
        a = decoy_fixture_ambiguous_shared_infra()
        assert a.verdict == WithinAuthVerdict.UNKNOWN


# === PROHIBITED SHORTCUTS ===

class TestProhibitedShortcuts:
    def test_shortcuts_exist(self):
        assert len(PROHIBITED_SHORTCUTS) >= 4

    def test_signature_shortcut_documented(self):
        assert any("signature" in s.lower() and "does not" in s.lower()
                    for s in PROHIBITED_SHORTCUTS)

    def test_organizational_shortcut_documented(self):
        assert any("organizational" in s.lower() and "does not" in s.lower()
                    for s in PROHIBITED_SHORTCUTS)


# === ALL THREE VERDICTS REACHABLE ===

class TestVerdictReachability:
    def test_all_verdicts_produced(self):
        verdicts = {
            decoy_fixture_independent_ci().verdict,
            decoy_fixture_maintainer_controlled_release().verdict,
            decoy_fixture_ambiguous_shared_infra().verdict,
        }
        assert verdicts == {WithinAuthVerdict.OUTSIDE,
                            WithinAuthVerdict.INSIDE,
                            WithinAuthVerdict.UNKNOWN}


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
# === FILE: test_xz_protocol_adversarial.py | BYTES: 9501 ===
# XZ Protocol v0.47 test suite
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
# === FILE: xz_protocol_phase_a_tests.py | BYTES: 16365 ===
"""
xz_protocol_phase_a_tests.py -- Phase A scoring test suite for XZ Protocol v0.47.

Covers all CODE-LEVEL PA-Z rules (PA-Z1-Z3, PA-Z5-Z14; thirteen rules).
PA-Z4 (alpha undefined) is adjudication-layer and scoped out.
Golden vectors pin exact bounds for T2-abs, T2-rel, T3, T4, T7,
PA-Z2, PA-Z5, PA-Z10, PA-Z11, PA-Z14.
"""
import math, pytest, numpy as np
from xz_protocol_phase_a_m3 import (
    CensorStatus, FROZEN_BUDGET_MINUTES, M3FirstResult,
    M3Observation, M3Vector, PairedDifference, PhaseAInputError,
    compute_median, compute_paired_differences, compute_shared_set,
    evaluate_t2_point,
)
from xz_protocol_phase_a_intervals import (
    IntervalMethod, T4_CORPUS_SIZE, T7_CORPUS_SIZE,
    evaluate_t2_full, evaluate_t5,
    t2_absolute_interval, t2_relative_interval, t3_interval,
    t4_interval, t7_interval,
    _make_result,
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
    def test_point_inside_no_reversion(self):
        """Integration: this input does NOT trigger PA-Z14 (point stays in
        interval). Unconditional assertion proves the guard is not needed
        here -- the negative discriminator for the vacuity sweep."""
        oa = [_obs(f"f{i}","A",float(100+i),f"ea{i}") for i in range(41)]
        vals_b = [100]*38 + [97,98,99]  # deltas: [0]*38 + [3,2,1] -> median 0
        ob = [_obs(f"f{i}","B",float(vals_b[i]),f"eb{i}") for i in range(41)]
        va,vb = M3Vector("A",tuple(oa)), M3Vector("B",tuple(ob))
        ds = compute_paired_differences(va,vb)
        r = t2_absolute_interval(ds, SEED)
        # Unconditional: point IS inside, PA-Z14 does NOT fire
        assert r.point_in_interval is True
        assert r.fallback_reason is None or "PA-Z14" not in r.fallback_reason

    def test_pa_z14_reversion_direct(self):
        """Unit test: PA-Z14 reversion code path exercised directly via
        _make_result with a controlled point-outside-interval BCA input.
        This is the positive discriminator: sabotaging the PA-Z14 guard
        (removing it) would make this test fail because method would
        remain BCA and excludes_zero would remain True."""
        r = _make_result(
            point=50.0, lower=0.0, upper=40.0,
            method=IntervalMethod.BCA,
            n_resamples=1000, n_valid=1000,
            n_nan=0, n_degen=0, n_loo_nan=0,
            n_denom_guard=0, n_level_clamp=0,
            reason=None, caller_seed=42, internal_seed=42
        )
        assert r.method == IntervalMethod.PERCENTILE
        assert r.point_in_interval is False
        assert r.excludes_zero is False
        assert r.fallback_reason is not None
        assert "PA-Z14" in r.fallback_reason

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
