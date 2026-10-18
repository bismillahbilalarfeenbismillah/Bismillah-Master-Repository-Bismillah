# Bismillah ir-Rahman ir-Rahim

# R0200 -- xz_protocol_control_graph.py — xz_protocol_control_graph.py -- WithinAuth control-graph standard.

**Chronological Index:** 6 of 995  
**Date:** 2024  
**Section:** IV. XZ Protocol  
**Source File:** xz_protocol_control_graph.py  
**Source Format:** py  
**SHA-256:** `35b14f752e705cacfa81694ccd20b031610d4e9d56900636c5c0487d4c32552e`  

---

## R0200 · xz_protocol_control_graph.py — xz_protocol_control_graph.py -- WithinAuth control-graph standard.

- section: IV. XZ Protocol
- source_file: xz_protocol_control_graph.py
- source_format: py
- merged_variants: 2 (xz_protocol_control_graph.py.txt; xz_protocol_control_graph.txt)
- text_sha256: 35b14f752e705cacfa81694ccd20b031610d4e9d56900636c5c0487d4c32552e

"""
xz_protocol_control_graph.py -- WithinAuth control-graph standard.

XZ Protocol v0.75, Section 7.4, FREEZE-BLOCKER FB-5.

This module provides the frozen schema and adjudication rules for
evaluating whether a record-generation act is within the acting
substrate's authority (WithinAuth) per SHUDP v0.5 Axiom 5.

WithinAuth(x, S) holds exactly when S can cause, modify, suppress,
reconfigure, or credential x without an independently detectable
violation. Five authority channels are evaluated; any one TRUE
makes WithinAuth TRUE.

The control graph is declared per stratum before scoring.
Two adjudicators apply it independently; reliability is measured
before consensus.

Author of record: Bilal Syed Arfeen
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional


# ---------------------------------------------------------------------------
# WithinAuth verdict vocabulary (from Section 7.4)
# ---------------------------------------------------------------------------

class WithinAuthVerdict(Enum):
    OUTSIDE = "OUTSIDE_SUBJECT_AUTHORITY"
    INSIDE = "INSIDE_SUBJECT_AUTHORITY"
    UNKNOWN = "UNKNOWN"


# ---------------------------------------------------------------------------
# Authority channels (the five ways S can control a generation act)
# ---------------------------------------------------------------------------

class AuthorityChannel(Enum):
    """Five channels through which S might control generation act x."""
    CAUSE = "can-cause"
    MODIFY = "can-modify"
    SUPPRESS = "can-suppress"
    RECONFIGURE = "can-reconfigure"
    CREDENTIAL = "can-credential"


class ChannelStatus(Enum):
    """Per-channel assessment."""
    YES = "yes"         # S can exercise this channel
    NO = "no"           # S cannot, with supporting evidence
    UNKNOWN = "unknown" # cannot determine


# ---------------------------------------------------------------------------
# Substrate and record-generation act
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class ActingSubstrate:
    """The entity whose authority is being tested."""
    substrate_id: str
    description: str
    authority_basis: str  # what gives S its authority (e.g. "commit access")


@dataclass(frozen=True)
class RecordGenerationAct:
    """The act whose independence is being tested."""
    record_id: str
    description: str
    generator: str         # who/what generated the record
    generation_time: str   # when (ISO timestamp or bounded interval)
    record_type: str       # e.g. "git-commit-hash", "gpg-signature", "build-log"


# ---------------------------------------------------------------------------
# Control-graph edge (one channel assessment)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class ControlEdge:
    """Assessment of one authority channel for one (substrate, act) pair."""
    channel: AuthorityChannel
    status: ChannelStatus
    evidence: str          # what supports this assessment
    reasoning: str         # why

    def __post_init__(self):
        if not isinstance(self.channel, AuthorityChannel):
            raise ValueError(f"channel must be AuthorityChannel, got {type(self.channel).__name__}")
        if not isinstance(self.status, ChannelStatus):
            raise ValueError(f"status must be ChannelStatus, got {type(self.status).__name__}")


# ---------------------------------------------------------------------------
# WithinAuth assessment (the full evaluation for one pair)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class WithinAuthAssessment:
    """Complete WithinAuth evaluation. Verdict MUST equal compute_verdict(edges)."""
    """Complete WithinAuth evaluation for (substrate S, generation act x)."""
    substrate: ActingSubstrate
    act: RecordGenerationAct
    edges: tuple[ControlEdge, ...]
    verdict: WithinAuthVerdict
    adjudicator_id: str
    reasoning_summary: str

    def __post_init__(self):
        # Must have exactly five edges (one per channel)
        channels_present = {e.channel for e in self.edges}
        if channels_present != set(AuthorityChannel):
            missing = set(AuthorityChannel) - channels_present
            raise ValueError(f"Missing authority channels: {missing}")
        if len(self.edges) != 5:
            raise ValueError(f"Expected 5 edges, got {len(self.edges)}")
        # H-2: verdict MUST equal compute_verdict(edges)
        expected = compute_verdict(self.edges)
        if self.verdict != expected:
            raise ValueError(
                f"Verdict {self.verdict} does not match computed "
                f"{expected} from edges")


# ---------------------------------------------------------------------------
# Adjudication rules (frozen)
# ---------------------------------------------------------------------------

def compute_verdict(edges: tuple[ControlEdge, ...]) -> WithinAuthVerdict:
    # M-3: validate exactly 5 edges, no duplicates
    if not isinstance(edges, (tuple, list)) or len(edges) != 5:
        raise ValueError(f"Expected exactly 5 edges, got {len(edges) if hasattr(edges, '__len__') else type(edges).__name__}")
    channels_seen = set()
    for e in edges:
        if not isinstance(e, ControlEdge):
            raise ValueError(f"Each edge must be ControlEdge, got {type(e).__name__}")
        if e.channel in channels_seen:
            raise ValueError(f"Duplicate channel: {e.channel}")
        channels_seen.add(e.channel)
    if channels_seen != set(AuthorityChannel):
        raise ValueError(f"Missing channels: {set(AuthorityChannel) - channels_seen}")

    """Compute WithinAuth verdict from channel assessments.

    Rules (from Section 7.4 and SHUDP v0.5):
      - ANY channel YES -> INSIDE (WithinAuth holds)
      - ALL channels NO -> OUTSIDE (WithinAuth does not hold)
      - Otherwise -> UNKNOWN

    Additional frozen rules:
      - A signature alone does NOT establish OUTSIDE
      - Organizational distinctness alone does NOT establish OUTSIDE
        without the control graph
      - Witness records reconstructed only from subject-emitted logs
        are NOT independent evidence
      - Caller-supplied evidence is WithinAuth of the supplier
    """
    statuses = {e.channel: e.status for e in edges}

    # Any YES -> INSIDE (S can control this act through at least one channel)
    if any(s == ChannelStatus.YES for s in statuses.values()):
        return WithinAuthVerdict.INSIDE

    # All NO -> OUTSIDE (S cannot control this act through any channel)
    if all(s == ChannelStatus.NO for s in statuses.values()):
        return WithinAuthVerdict.OUTSIDE

    # Otherwise -> UNKNOWN
    return WithinAuthVerdict.UNKNOWN


# ---------------------------------------------------------------------------
# Prohibited shortcuts (frozen rules from Section 7.4)
# ---------------------------------------------------------------------------

PROHIBITED_SHORTCUTS = [
    "A GPG signature by a different key does NOT establish OUTSIDE; "
    "the control graph must show the signing key is outside S's authority.",

    "Organizational distinctness (different company, different team) does NOT "
    "establish OUTSIDE without showing that S cannot cause, modify, suppress, "
    "reconfigure, or credential the generation act.",

    "Witness records reconstructed solely from subject-emitted logs "
    "(e.g. the subject's own audit trail) are NOT independent evidence.",

    "Caller-supplied evidence is WithinAuth of the supplier; "
    "it discharges nothing about the supplier's own authority.",

    "A hosted CI/CD pipeline whose configuration is controlled by the "
    "repository owner is INSIDE for the repository owner substrate.",
]


# ---------------------------------------------------------------------------
# Decoy fixtures (non-XZ; for adjudicator calibration)
# ---------------------------------------------------------------------------

def decoy_fixture_independent_ci() -> WithinAuthAssessment:
    """Decoy: an independent CI service signs a build attestation.

    Substrate: repository maintainer (has commit access)
    Act: CI service generates a signed build attestation

    Expected: OUTSIDE -- the CI signing key and build environment
    are administered by a separate organization, and the maintainer
    cannot modify, suppress, or credential the attestation without
    a detectable violation of the CI service's integrity.
    """
    substrate = ActingSubstrate(
        "decoy-maintainer-01",
        "Repository maintainer with commit access",
        "Git commit signing key + push access")

    act = RecordGenerationAct(
        "decoy-ci-attestation-01",
        "Signed build attestation from independent CI",
        "ci-service.example.com",
        "2024-01-15T10:00:00Z",
        "signed-build-attestation")

    edges = (
        ControlEdge(AuthorityChannel.CAUSE, ChannelStatus.NO,
                     "CI triggers on push but builds in isolated environment",
                     "Maintainer can trigger a build but cannot control the attestation content"),
        ControlEdge(AuthorityChannel.MODIFY, ChannelStatus.NO,
                     "Attestation is signed by CI's key, not maintainer's",
                     "Maintainer has no access to CI's signing key"),
        ControlEdge(AuthorityChannel.SUPPRESS, ChannelStatus.NO,
                     "Attestations are published to a transparency log",
                     "Suppression would leave a detectable gap in the log"),
        ControlEdge(AuthorityChannel.RECONFIGURE, ChannelStatus.NO,
                     "CI configuration is admin-only at the CI service",
                     "Maintainer cannot change build/signing config"),
        ControlEdge(AuthorityChannel.CREDENTIAL, ChannelStatus.NO,
                     "CI credentials are rotated by the CI service",
                     "Maintainer cannot issue or rotate CI signing credentials"),
    )

    verdict = compute_verdict(edges)
    assert verdict == WithinAuthVerdict.OUTSIDE

    return WithinAuthAssessment(
        substrate, act, edges, verdict,
        "decoy-adjudicator", "All five channels NO; CI is independently administered")


def decoy_fixture_maintainer_controlled_release() -> WithinAuthAssessment:
    """Decoy: maintainer creates and signs a release tarball.

    Substrate: repository maintainer
    Act: maintainer generates a signed release tarball

    Expected: INSIDE -- the maintainer directly causes, controls content,
    and credentials the release. The release is WithinAuth of the maintainer.
    """
    substrate = ActingSubstrate(
        "decoy-maintainer-02",
        "Repository maintainer with release authority",
        "Git tag signing key + release upload access")

    act = RecordGenerationAct(
        "decoy-release-01",
        "Signed release tarball generated by maintainer",
        "maintainer@example.com",
        "2024-02-01T14:00:00Z",
        "gpg-signed-tarball")

    edges = (
        ControlEdge(AuthorityChannel.CAUSE, ChannelStatus.YES,
                     "Maintainer initiates and performs the release",
                     "Direct causal authority over the release act"),
        ControlEdge(AuthorityChannel.MODIFY, ChannelStatus.YES,
                     "Maintainer controls tarball content before signing",
                     "Can include or exclude any file"),
        ControlEdge(AuthorityChannel.SUPPRESS, ChannelStatus.YES,
                     "Maintainer can delete or replace releases",
                     "Has upload/delete access to the release archive"),
        ControlEdge(AuthorityChannel.RECONFIGURE, ChannelStatus.YES,
                     "Maintainer controls build scripts and release process",
                     "Can change what the release includes"),
        ControlEdge(AuthorityChannel.CREDENTIAL, ChannelStatus.YES,
                     "Maintainer holds the signing key",
                     "Signs with own GPG key"),
    )

    verdict = compute_verdict(edges)
    assert verdict == WithinAuthVerdict.INSIDE

    return WithinAuthAssessment(
        substrate, act, edges, verdict,
        "decoy-adjudicator", "All five channels YES; maintainer controls the release")


def decoy_fixture_ambiguous_shared_infra() -> WithinAuthAssessment:
    """Decoy: a distribution build service uses shared infrastructure.

    Substrate: upstream maintainer
    Act: distribution build service creates a binary package

    Expected: UNKNOWN -- the build service is organizationally distinct
    but pulls source from the maintainer's repository, and the build
    configuration may be influenced by upstream-provided scripts.
    """
    substrate = ActingSubstrate(
        "decoy-maintainer-03",
        "Upstream project maintainer",
        "Commit access to upstream repository")

    act = RecordGenerationAct(
        "decoy-distro-build-01",
        "Binary package built by distribution build service",
        "buildd.debian.org",
        "2024-01-20T08:00:00Z",
        "distribution-binary-package")

    edges = (
        ControlEdge(AuthorityChannel.CAUSE, ChannelStatus.NO,
                     "Distribution maintainer triggers builds, not upstream",
                     "Upstream cannot directly invoke the build service"),
        ControlEdge(AuthorityChannel.MODIFY, ChannelStatus.UNKNOWN,
                     "Build uses upstream-provided configure/make scripts",
                     "Upstream controls build scripts that run in the build environment; "
                     "whether this constitutes modify authority depends on sandboxing"),
        ControlEdge(AuthorityChannel.SUPPRESS, ChannelStatus.NO,
                     "Distribution controls package publication",
                     "Upstream cannot suppress a built package"),
        ControlEdge(AuthorityChannel.RECONFIGURE, ChannelStatus.UNKNOWN,
                     "Build rules may incorporate upstream-provided autoconf output",
                     "Upstream's configure.ac influences the build environment setup"),
        ControlEdge(AuthorityChannel.CREDENTIAL, ChannelStatus.NO,
                     "Distribution signs packages with its own keys",
                     "Upstream has no access to distribution signing keys"),
    )

    verdict = compute_verdict(edges)
    assert verdict == WithinAuthVerdict.UNKNOWN

    return WithinAuthAssessment(
        substrate, act, edges, verdict,
        "decoy-adjudicator",
        "MODIFY and RECONFIGURE are UNKNOWN due to shared build scripts; "
        "the remaining channels are NO but cannot override UNKNOWN")

---

# Bismillah ir-Rahman ir-Rahim
