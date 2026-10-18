# Bismillah ir-Rahman ir-Rahim

# R0187 -- test_xz_protocol_source_frame.py — test_xz_protocol_source_frame.py -- Tests for the source-frame manifest.

**Chronological Index:** 5 of 995  
**Date:** 2024  
**Section:** IV. XZ Protocol  
**Source File:** test_xz_protocol_source_frame.py  
**Source Format:** py  
**SHA-256:** `03f80f3c5252374b34402f7473b5c3162c0756beb0af8979296276968ce81ee6`  

---

## R0187 · test_xz_protocol_source_frame.py — test_xz_protocol_source_frame.py -- Tests for the source-frame manifest.

- section: IV. XZ Protocol
- source_file: test_xz_protocol_source_frame.py
- source_format: py
- merged_variants: 2 (test_xz_protocol_source_frame.py.txt; test_xz_protocol_source_frame.txt)
- text_sha256: 03f80f3c5252374b34402f7473b5c3162c0756beb0af8979296276968ce81ee6

# XZ Protocol v0.75 test suite
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

---

# Bismillah ir-Rahman ir-Rahim
