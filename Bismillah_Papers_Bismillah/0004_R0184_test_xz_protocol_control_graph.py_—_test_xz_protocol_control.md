# Bismillah ir-Rahman ir-Rahim

# R0184 -- test_xz_protocol_control_graph.py — test_xz_protocol_control_graph.py -- Tests for the WithinAuth control graph.

**Chronological Index:** 4 of 995  
**Date:** 2024-01-01  
**Section:** IV. XZ Protocol  
**Source File:** test_xz_protocol_control_graph.py  
**Source Format:** py  
**SHA-256:** `45ced8d2e20fffd3aef964937e0d0a5da2d6b0908dfaa26b176b701dfaa67687`  

---

## R0184 · test_xz_protocol_control_graph.py — test_xz_protocol_control_graph.py -- Tests for the WithinAuth control graph.

- section: IV. XZ Protocol
- source_file: test_xz_protocol_control_graph.py
- source_format: py
- merged_variants: 2 (test_xz_protocol_control_graph.py.txt; test_xz_protocol_control_graph.txt)
- text_sha256: 45ced8d2e20fffd3aef964937e0d0a5da2d6b0908dfaa26b176b701dfaa67687

# XZ Protocol v0.75 test suite
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

---

# Bismillah ir-Rahman ir-Rahim
