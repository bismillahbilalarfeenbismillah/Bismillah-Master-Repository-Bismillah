# Bismillah ir-Rahman ir-Rahim

# R0574 -- BEGIN FILE: xz_protocol_kernel.py | SIZE: 4515 bytes | SHA256: 4109f59f12ac9b4e7d7058a93f9ccc75b9393b3b82f5479cad3a4a62f533ed0c

**Chronological Index:** 62 of 995  
**Date:** 2024-03-29  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** code_modules.txt  
**Source Format:** txt  
**SHA-256:** `6945009b22606f968eec5051d02894050cd4dba0e5a2bc039a2201892dbf0447`  

---

## R0574 · BEGIN FILE: xz_protocol_kernel.py | SIZE: 4515 bytes | SHA256: 4109f59f12ac9b4e7d7058a93f9ccc75b9393b3b82f5479cad3a4a62f533ed0c

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: code_modules.txt
- source_format: txt
- text_sha256: 6945009b22606f968eec5051d02894050cd4dba0e5a2bc039a2201892dbf0447

===== BEGIN FILE: xz_protocol_kernel.py | SIZE: 4515 bytes | SHA256: 4109f59f12ac9b4e7d7058a93f9ccc75b9393b3b82f5479cad3a4a62f533ed0c =====
"""
# Version: XZ Protocol v0.48
xz_protocol_kernel.py -- BSSG five-conjunct kernel for the XZ Protocol.

Extracted from the carried BSSG v0.1 pass-37 reference gate
(doi:10.5281/zenodo.21713180). The kernel equation:

  Allow(r) iff ContractMatch AND EffectTypeValid AND TargetAllowed
               AND WitnessHealthy AND EvidenceCurrent

Three-valued: TRUE, FALSE, UNKNOWN.
  - UNKNOWN never satisfies.
  - FALSE dominates UNKNOWN order-independently.
  - DENY_FALSE and DENY_UNKNOWN are always distinct.

This module is the sole normative kernel for the XZ Protocol.
"""

from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class TruthValue(Enum):
    TRUE = "TRUE"
    FALSE = "FALSE"
    UNKNOWN = "UNKNOWN"


class KernelDecision(Enum):
    ALLOW = "ALLOW"
    DENY_FALSE = "DENY_FALSE"
    DENY_UNKNOWN = "DENY_UNKNOWN"


CONJUNCT_NAMES = (
    "ContractMatch", "EffectTypeValid", "TargetAllowed",
    "WitnessHealthy", "EvidenceCurrent",
)


class KernelError(Exception):
    pass


@dataclass(frozen=True)
class ConjunctVector:
    """The five conjunct values for one boundary evaluation."""
    contract_match: TruthValue
    effect_type_valid: TruthValue
    target_allowed: TruthValue
    witness_healthy: TruthValue
    evidence_current: TruthValue

    def __post_init__(self):
        for name in CONJUNCT_NAMES:
            attr = name[0].lower() + name[1:]  # camelCase to snake
            # Use the frozen field names directly
        for val in self.as_dict().values():
            if not isinstance(val, TruthValue):
                raise KernelError(f"All conjuncts must be TruthValue, got {type(val).__name__}")

    def as_dict(self) -> dict[str, TruthValue]:
        return {
            "ContractMatch": self.contract_match,
            "EffectTypeValid": self.effect_type_valid,
            "TargetAllowed": self.target_allowed,
            "WitnessHealthy": self.witness_healthy,
            "EvidenceCurrent": self.evidence_current,
        }


@dataclass(frozen=True)
class KernelResult:
    """Result of kernel evaluation."""
    decision: KernelDecision
    vector: ConjunctVector
    false_conjuncts: tuple[str, ...]
    unknown_conjuncts: tuple[str, ...]
    reason_codes: tuple[str, ...]


def evaluate_kernel(vector: ConjunctVector) -> KernelResult:
    """Evaluate the frozen five-conjunct kernel.

    FALSE dominates UNKNOWN. UNKNOWN never satisfies.
    No sixth conjunct. No caller-supplied decision.
    """
    if type(vector) is not ConjunctVector:  # exact type, not isinstance -- blocks descriptor laundering (F-K3-03)
        raise KernelError(f"Input must be ConjunctVector, got {type(vector).__name__}")

    # Read frozen fields via object.__getattribute__ to defeat subclass
    # __getattribute__ overrides (H-1 hardened). This is the code-plane
    # boundary; the protocol-layer boundary is adjudicator verification.
    _get = object.__getattribute__
    field_values = (
        ("ContractMatch", _get(vector, "contract_match")),
        ("EffectTypeValid", _get(vector, "effect_type_valid")),
        ("TargetAllowed", _get(vector, "target_allowed")),
        ("WitnessHealthy", _get(vector, "witness_healthy")),
        ("EvidenceCurrent", _get(vector, "evidence_current")),
    )
    for name, val in field_values:
        if not isinstance(val, TruthValue):
            raise KernelError(f"Conjunct {name} is {type(val).__name__}, not TruthValue")
    falses = tuple(n for n, v in field_values if v == TruthValue.FALSE)
    unknowns = tuple(n for n, v in field_values if v == TruthValue.UNKNOWN)

    if falses:
        decision = KernelDecision.DENY_FALSE
        codes = tuple(f"E-FALSE-{n.upper()}" for n in falses)
    elif unknowns:
        decision = KernelDecision.DENY_UNKNOWN
        codes = tuple(f"E-UNKNOWN-{n.upper()}" for n in unknowns)
    else:
        decision = KernelDecision.ALLOW
        codes = ()

    return KernelResult(
        decision=decision, vector=vector,
        false_conjuncts=falses, unknown_conjuncts=unknowns,
        reason_codes=codes)


def generate_exhaustive_vectors():
    """Generate all 3^5 = 243 possible conjunct vectors."""
    vectors = []
    for cm in TruthValue:
        for ev in TruthValue:
            for ta in TruthValue:
                for wh in TruthValue:
                    for ec in TruthValue:
                        vectors.append(ConjunctVector(cm, ev, ta, wh, ec))
    assert len(vectors) == 243
    return vectors

===== END FILE: xz_protocol_kernel.py =====

===== BEGIN FILE: xz_protocol_condition_a.py | SIZE: 13822 bytes | SHA256: ec458b1f32e8d26ec66a1ba9f0a0edaddbf9dc7501ccd88065b51fad9b8e850b =====
"""
xz_protocol_condition_a.py -- Executable Condition A disposition function.

XZ Protocol v0.48, Section 6.1, FREEZE-BLOCKER FB-3.

This module implements the conventional baseline disposition for the
XZ Protocol's retrospective structural decision replay. It maps
tool-output vectors to the four-label vocabulary:

  A-ACCEPT: every mandatory check passes, none missing or unverifiable
  A-REJECT: at least one mandatory check returns verified contradiction
  A-INDETERMINATE: no check fails, but a mandatory check is absent/ambiguous
  A-NOT-APPLICABLE: the baseline profile defines no rule for this stratum

Dominance: A-REJECT > A-INDETERMINATE (parallels BSSG FALSE > UNKNOWN).

Fairness rules (frozen, from Section 6.1):
  1. Every ambiguity resolved in Condition A's favor, logged.
  2. Condition A never required to produce BSSG-shaped record types.
  3. Tool documentation governs fail-closed behavior.
  4. Tuning on decoys only; no tuning on XZ outputs.
  5. Piloted on non-case decoys before XZ packets opened.
  6. Fairness attestation signed; breach fires falsifier XZ-S11.

The _provenance field on BaselineCheckResult is a DOCUMENTATION MARKER only. It is NOT enforced by evaluate_boundary() and does NOT prevent direct construction. The protocol-layer discipline (raw evidence only, no derived objects) is enforced at the BSSG layer, not at this Python API layer. This is a disclosed limitation, not a hidden bypass
(same discipline as the Phase A scoring module).

Author of record: Bilal Syed Arfeen
"""

from __future__ import annotations

import secrets
from dataclasses import dataclass
from enum import Enum
from typing import Optional


# ---------------------------------------------------------------------------
# Disposition vocabulary (frozen semantics)
# ---------------------------------------------------------------------------

class ADisposition(Enum):
    """The four-label Condition A boundary disposition."""
    A_ACCEPT = "A-ACCEPT"
    A_REJECT = "A-REJECT"
    A_INDETERMINATE = "A-INDETERMINATE"
    A_NOT_APPLICABLE = "A-NOT-APPLICABLE"


class CheckOutcome(Enum):
    """Individual baseline check result."""
    PASS = "PASS"
    FAIL = "FAIL"
    ABSENT = "ABSENT"
    UNVERIFIABLE = "UNVERIFIABLE"
    STALE = "STALE"
    AMBIGUOUS = "AMBIGUOUS"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class ConditionAError(Exception):
    """Raised for invalid evaluator inputs."""
    pass


# ---------------------------------------------------------------------------
# Boundary strata (frozen at v0.1)
# ---------------------------------------------------------------------------

class BoundaryStratum(Enum):
    S_COMMIT = "S-COMMIT"
    S_RELEASE = "S-RELEASE"
    S_BUILD = "S-BUILD"
    S_DISTRIBUTION = "S-DISTRIBUTION"
    S_INSTALLATION = "S-INSTALLATION"
    S_RUNTIME_AUTH = "S-RUNTIME-AUTH"


# ---------------------------------------------------------------------------
# Baseline check categories
# ---------------------------------------------------------------------------

class BaselineCheck(Enum):
    """Conventional baseline checks available to Condition A."""
    # Provenance and identity
    SIGNATURE_VERIFICATION = "signature-verification"
    IDENTITY_VERIFICATION = "identity-verification"
    PROVENANCE_REVIEW = "provenance-review"

    # Source integrity
    SOURCE_TO_ARTIFACT_COMPARISON = "source-to-artifact-comparison"
    REPRODUCIBLE_BUILD = "reproducible-build"
    COMMIT_SIGNING = "commit-signing"

    # Attestation
    SLSA_PROVENANCE = "slsa-provenance"
    IN_TOTO_ATTESTATION = "in-toto-attestation"
    STEP_ATTESTATION = "step-attestation"

    # Scanning
    STATIC_ANALYSIS = "static-analysis"
    MALWARE_SCAN = "malware-scan"
    DEPENDENCY_SCAN = "dependency-scan"

    # Distribution
    PACKAGE_SIGNATURE = "package-signature"
    REPOSITORY_POLICY = "repository-policy"
    DISTRIBUTION_CHANNEL_INTEGRITY = "distribution-channel-integrity"

    # Runtime
    SERVICE_AUTHENTICATION_CHECK = "service-authentication-check"
    LIBRARY_LOAD_VERIFICATION = "library-load-verification"


# ---------------------------------------------------------------------------
# Baseline profile: which checks are MANDATORY per stratum
# ---------------------------------------------------------------------------

BASELINE_PROFILE: dict[BoundaryStratum, set[BaselineCheck]] = {
    BoundaryStratum.S_COMMIT: {
        BaselineCheck.COMMIT_SIGNING,
        BaselineCheck.IDENTITY_VERIFICATION,
        BaselineCheck.PROVENANCE_REVIEW,
    },
    BoundaryStratum.S_RELEASE: {
        BaselineCheck.SIGNATURE_VERIFICATION,
        BaselineCheck.SOURCE_TO_ARTIFACT_COMPARISON,
        BaselineCheck.IDENTITY_VERIFICATION,
        BaselineCheck.PROVENANCE_REVIEW,
        BaselineCheck.SLSA_PROVENANCE,
    },
    BoundaryStratum.S_BUILD: {
        BaselineCheck.SOURCE_TO_ARTIFACT_COMPARISON,
        BaselineCheck.REPRODUCIBLE_BUILD,
        BaselineCheck.STATIC_ANALYSIS,
        BaselineCheck.MALWARE_SCAN,
        BaselineCheck.STEP_ATTESTATION,
    },
    BoundaryStratum.S_DISTRIBUTION: {
        BaselineCheck.PACKAGE_SIGNATURE,
        BaselineCheck.REPOSITORY_POLICY,
        BaselineCheck.DISTRIBUTION_CHANNEL_INTEGRITY,
        BaselineCheck.DEPENDENCY_SCAN,
    },
    BoundaryStratum.S_INSTALLATION: {
        BaselineCheck.PACKAGE_SIGNATURE,
        BaselineCheck.MALWARE_SCAN,
    },
    BoundaryStratum.S_RUNTIME_AUTH: {
        BaselineCheck.SERVICE_AUTHENTICATION_CHECK,
        BaselineCheck.LIBRARY_LOAD_VERIFICATION,
    },
}


# ---------------------------------------------------------------------------
# Provenance
# ---------------------------------------------------------------------------

_CHECK_TOKEN = secrets.token_hex(16)


# ---------------------------------------------------------------------------
# Check result
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class BaselineCheckResult:
    """Result of one baseline check on one boundary.

    Provenance token is an accident guard (not a security boundary).
    """
    check: BaselineCheck
    outcome: CheckOutcome
    tool_name: str
    tool_version: str
    reason: str
    evidence_ref: Optional[str] = None
    ambiguity_resolution: Optional[str] = None  # logged per fairness rule 1
    _provenance: str = ""

    def __post_init__(self):
        if not isinstance(self.check, BaselineCheck):
            raise ConditionAError(
                f"check must be BaselineCheck, got {type(self.check).__name__}")
        if not isinstance(self.outcome, CheckOutcome):
            raise ConditionAError(
                f"outcome must be CheckOutcome, got {type(self.outcome).__name__}")
        if not isinstance(self.tool_name, str) or not self.tool_name.strip():
            raise ConditionAError("tool_name must be a non-empty string")
        if not isinstance(self.tool_version, str) or not self.tool_version.strip():
            raise ConditionAError("tool_version must be a non-empty string")
        if not isinstance(self.reason, str) or not self.reason.strip():
            raise ConditionAError("reason must be a non-empty string")


def create_check_result(
    check: BaselineCheck,
    outcome: CheckOutcome,
    tool_name: str,
    tool_version: str,
    reason: str,
    evidence_ref: Optional[str] = None,
    ambiguity_resolution: Optional[str] = None,
) -> BaselineCheckResult:
    """Create a provenance-bearing check result."""
    return BaselineCheckResult(
        check=check, outcome=outcome,
        tool_name=tool_name, tool_version=tool_version,
        reason=reason, evidence_ref=evidence_ref,
        ambiguity_resolution=ambiguity_resolution,
        _provenance=_CHECK_TOKEN,
    )


# ---------------------------------------------------------------------------
# Disposition evaluator
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class BoundaryDisposition:
    """Condition A disposition for one boundary."""
    boundary_id: str
    stratum: BoundaryStratum
    disposition: ADisposition
    check_results: tuple[BaselineCheckResult, ...]
    mandatory_checks: frozenset[BaselineCheck]
    mandatory_present: frozenset[BaselineCheck]
    mandatory_absent: frozenset[BaselineCheck]
    has_failure: bool
    has_indeterminate: bool
    reason: str


def evaluate_boundary(
    boundary_id: str,
    stratum: BoundaryStratum,
    check_results: list[BaselineCheckResult],
) -> BoundaryDisposition:
    """Evaluate Condition A disposition for a single boundary.

    Implements the dominance rule: A-REJECT > A-INDETERMINATE.
    Implements A-NOT-APPLICABLE for strata with no mandatory checks.
    """
    if not isinstance(stratum, BoundaryStratum):
        raise ConditionAError(
            f"stratum must be BoundaryStratum, got {type(stratum).__name__}")
    if not isinstance(boundary_id, str) or not boundary_id.strip():
        raise ConditionAError("boundary_id must be a non-empty string")

    mandatory = BASELINE_PROFILE.get(stratum, set())

    if not mandatory:
        return BoundaryDisposition(
            boundary_id=boundary_id, stratum=stratum,
            disposition=ADisposition.A_NOT_APPLICABLE,
            check_results=tuple(check_results),
            mandatory_checks=frozenset(mandatory),
            mandatory_present=frozenset(),
            mandatory_absent=frozenset(),
            has_failure=False, has_indeterminate=False,
            reason="No mandatory checks defined for this stratum",
        )

    # Materialize check_results to prevent generator consumption (M-6)
    check_results = list(check_results)

    # Map check results by check type
    results_by_check: dict[BaselineCheck, BaselineCheckResult] = {}
    for cr in check_results:
        if cr.check in results_by_check:
            raise ConditionAError(
                f"Duplicate check {cr.check.value} for boundary {boundary_id}")
        results_by_check[cr.check] = cr

    mandatory_present = frozenset(mandatory & results_by_check.keys())
    mandatory_absent = frozenset(mandatory - results_by_check.keys())

    # Evaluate each mandatory check
    has_failure = False
    has_indeterminate = False
    failure_reasons = []
    indeterminate_reasons = []

    for chk in sorted(mandatory, key=lambda c: c.value):
        if chk not in results_by_check:
            has_indeterminate = True
            indeterminate_reasons.append(f"{chk.value}: ABSENT (no result submitted)")
            continue

        cr = results_by_check[chk]
        if cr.outcome == CheckOutcome.FAIL:
            has_failure = True
            failure_reasons.append(f"{chk.value}: FAIL ({cr.reason})")
        elif cr.outcome in (CheckOutcome.ABSENT, CheckOutcome.UNVERIFIABLE,
                            CheckOutcome.STALE, CheckOutcome.AMBIGUOUS):
            has_indeterminate = True
            indeterminate_reasons.append(
                f"{chk.value}: {cr.outcome.value} ({cr.reason})")
        elif cr.outcome == CheckOutcome.PASS:
            pass  # contributes to ACCEPT
        elif cr.outcome == CheckOutcome.NOT_APPLICABLE:
            # A mandatory check returning NOT_APPLICABLE means the check
            # exists but cannot apply -- this is INDETERMINATE, not ACCEPT.
            # (F-SOL-XZ-3: NOT_APPLICABLE on mandatory must not produce A-ACCEPT)
            has_indeterminate = True
            indeterminate_reasons.append(
                f"{chk.value}: NOT_APPLICABLE on mandatory check ({cr.reason})")

    # Dominance: REJECT > INDETERMINATE (parallels FALSE > UNKNOWN)
    if has_failure:
        disposition = ADisposition.A_REJECT
        reason = "; ".join(failure_reasons)
    elif has_indeterminate:
        disposition = ADisposition.A_INDETERMINATE
        reason = "; ".join(indeterminate_reasons)
    else:
        disposition = ADisposition.A_ACCEPT
        reason = "All mandatory checks pass"

    return BoundaryDisposition(
        boundary_id=boundary_id, stratum=stratum,
        disposition=disposition,
        check_results=tuple(check_results),
        mandatory_checks=frozenset(mandatory),
        mandatory_present=mandatory_present,
        mandatory_absent=mandatory_absent,
        has_failure=has_failure,
        has_indeterminate=has_indeterminate,
        reason=reason,
    )


# ---------------------------------------------------------------------------
# Dual-evaluability check
# ---------------------------------------------------------------------------

def is_dual_evaluable(
    a_disposition: BoundaryDisposition,
    b_decision: 'KernelDecision',
) -> bool:
    """A boundary is dual-evaluable when both conditions produced a
    determinate disposition and the boundary is not A-NOT-APPLICABLE.

    b_decision: a KernelDecision enum value (ALLOW, DENY_FALSE, DENY_UNKNOWN).
    String inputs are rejected -- no caller-supplied derived decisions.
    """
    from xz_protocol_kernel import KernelDecision
    if not isinstance(b_decision, KernelDecision):
        raise ConditionAError(
            f"b_decision must be KernelDecision, got {type(b_decision).__name__}. "
            f"Caller-supplied string decisions are rejected.")
    if a_disposition.disposition == ADisposition.A_NOT_APPLICABLE:
        return False
    return True


def is_primary_seam_divergence(
    a_disposition: BoundaryDisposition,
    b_decision: 'KernelDecision',
) -> bool:
    """Primary seam divergence (CR-3): A-ACCEPT and DENY_FALSE only.
    DENY_UNKNOWN is never primary. String decisions rejected."""
    from xz_protocol_kernel import KernelDecision
    if not is_dual_evaluable(a_disposition, b_decision):
        return False
    return (a_disposition.disposition == ADisposition.A_ACCEPT
            and b_decision == KernelDecision.DENY_FALSE)

===== END FILE: xz_protocol_condition_a.py =====

===== BEGIN FILE: xz_protocol_source_frame.py | SIZE: 15398 bytes | SHA256: 4e1377500f3ba8d164820604ab3d429e802bfceb96cf0dcd782a846eb182b6be =====
"""
xz_protocol_source_frame.py -- Source-frame manifest for the XZ Protocol.

XZ Protocol v0.48, Section 5.1, FREEZE-BLOCKER FB-4.

This module defines the closed, enumerable list of public-record sources
that constitute the universe from which effect boundaries are enumerated.
No source outside this manifest may enter the primary enumeration. A
source discovered after the seal is appended as a deviation and cannot
enter the primary denominator.

Frame window:
  Start: 2023-10-01 (180 days before disclosure)
  End:   2024-04-28 (30 days after disclosure)
  Disclosure: 2024-03-29 (Andres Freund, oss-security)

This manifest is OPEN (Tier 1). It contains no restricted content,
no payload detail, no activation recipe, and no compromised binary.

Author of record: Bilal Syed Arfeen
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Optional


# ---------------------------------------------------------------------------
# Frame window (frozen)
# ---------------------------------------------------------------------------

DISCLOSURE_DATE = date(2024, 3, 29)
FRAME_START = date(2023, 10, 1)   # 180 days before disclosure
FRAME_END = date(2024, 4, 28)     # 30 days after disclosure
DISCLOSURE_URL = "https://www.openwall.com/lists/oss-security/2024/03/29/4"


# ---------------------------------------------------------------------------
# Source categories
# ---------------------------------------------------------------------------

class SourceCategory(Enum):
    REPOSITORY = "repository"
    RELEASE_ARCHIVE = "release-archive"
    DISTRIBUTION = "distribution"
    MAILING_LIST = "mailing-list"
    ADVISORY = "advisory"
    BUILD_INFRASTRUCTURE = "build-infrastructure"
    TRANSPARENCY_LOG = "transparency-log"


class AuthenticationMethod(Enum):
    """How to verify the source is authentic and unmodified."""
    GIT_HASH = "git-commit-hash"
    GPG_SIGNATURE = "gpg-signature"
    TLS_CERTIFICATE = "tls-certificate"
    ARCHIVE_CHECKSUM = "archive-checksum"
    DISTRIBUTION_SIGNATURE = "distribution-package-signature"
    INSTITUTIONAL_AUTHORITY = "institutional-authority"
    CONTENT_HASH = "content-hash-at-retrieval"


# ---------------------------------------------------------------------------
# Stratum coverage
# ---------------------------------------------------------------------------

class BoundaryStratum(Enum):
    S_COMMIT = "S-COMMIT"
    S_RELEASE = "S-RELEASE"
    S_BUILD = "S-BUILD"
    S_DISTRIBUTION = "S-DISTRIBUTION"
    S_INSTALLATION = "S-INSTALLATION"
    S_RUNTIME_AUTH = "S-RUNTIME-AUTH"


# ---------------------------------------------------------------------------
# Source record
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class SourceRecord:
    """One entry in the source-frame manifest."""
    source_id: str
    name: str
    category: SourceCategory
    url: str
    authentication: tuple[AuthenticationMethod, ...]
    strata_covered: frozenset[BoundaryStratum]
    retrieval_rule: str
    notes: Optional[str] = None


# ---------------------------------------------------------------------------
# THE MANIFEST (frozen, enumerable, closed)
# ---------------------------------------------------------------------------

SOURCE_FRAME_MANIFEST: tuple[SourceRecord, ...] = (

    # === REPOSITORIES ===

    SourceRecord(
        source_id="SRC-REPO-01",
        name="tukaani-project/xz (GitHub)",
        category=SourceCategory.REPOSITORY,
        url="https://github.com/tukaani-project/xz",
        authentication=(AuthenticationMethod.GIT_HASH, AuthenticationMethod.TLS_CERTIFICATE),
        strata_covered=frozenset({BoundaryStratum.S_COMMIT, BoundaryStratum.S_RELEASE}),
        retrieval_rule="git clone with full history; enumerate commits in frame window by author date; "
                       "record commit hash, author, committer, date, changed paths, and parent hashes",
    ),

    SourceRecord(
        source_id="SRC-REPO-02",
        name="tukaani-project/xz issue tracker (GitHub Issues)",
        category=SourceCategory.REPOSITORY,
        url="https://github.com/tukaani-project/xz/issues",
        authentication=(AuthenticationMethod.TLS_CERTIFICATE,),
        strata_covered=frozenset({BoundaryStratum.S_COMMIT, BoundaryStratum.S_RELEASE}),
        retrieval_rule="GitHub API: list issues and comments in frame window; "
                       "record issue number, author, timestamps, and body hashes",
        notes="Issue 103 is a primary XZ citation",
    ),

    # === RELEASE ARCHIVES ===

    SourceRecord(
        source_id="SRC-REL-01",
        name="xz.tukaani.org releases",
        category=SourceCategory.RELEASE_ARCHIVE,
        url="https://xz.tukaani.org/xz-utils/",
        authentication=(AuthenticationMethod.GPG_SIGNATURE, AuthenticationMethod.ARCHIVE_CHECKSUM),
        strata_covered=frozenset({BoundaryStratum.S_RELEASE}),
        retrieval_rule="Download all release tarballs and .sig files in frame window; "
                       "record filename, size, SHA-256, GPG verification result, "
                       "and signing key fingerprint",
    ),

    SourceRecord(
        source_id="SRC-REL-02",
        name="GitHub Releases (tukaani-project/xz)",
        category=SourceCategory.RELEASE_ARCHIVE,
        url="https://github.com/tukaani-project/xz/releases",
        authentication=(AuthenticationMethod.TLS_CERTIFICATE,),
        strata_covered=frozenset({BoundaryStratum.S_RELEASE}),
        retrieval_rule="GitHub API: list releases in frame window; "
                       "record tag, date, asset URLs, asset checksums",
    ),

    # === DISTRIBUTION CHANNELS ===

    SourceRecord(
        source_id="SRC-DIST-01",
        name="Debian package tracker (xz-utils)",
        category=SourceCategory.DISTRIBUTION,
        url="https://tracker.debian.org/pkg/xz-utils",
        authentication=(AuthenticationMethod.DISTRIBUTION_SIGNATURE,),
        strata_covered=frozenset({BoundaryStratum.S_DISTRIBUTION, BoundaryStratum.S_BUILD}),
        retrieval_rule="Query snapshot.debian.org for all xz-utils versions in frame window; "
                       "record version, upload date, suite, architecture, maintainer, "
                       "source package hash, build log URL",
    ),

    SourceRecord(
        source_id="SRC-DIST-02",
        name="Fedora Koji / Bodhi (xz)",
        category=SourceCategory.DISTRIBUTION,
        url="https://koji.fedoraproject.org/koji/packageinfo?packageID=xz",
        authentication=(AuthenticationMethod.DISTRIBUTION_SIGNATURE,),
        strata_covered=frozenset({BoundaryStratum.S_DISTRIBUTION, BoundaryStratum.S_BUILD}),
        retrieval_rule="Koji API: list builds for xz in frame window; "
                       "Bodhi API: list updates; record build ID, version, "
                       "task ID, completion date, update status",
    ),

    SourceRecord(
        source_id="SRC-DIST-03",
        name="Arch Linux packages (xz)",
        category=SourceCategory.DISTRIBUTION,
        url="https://archlinux.org/packages/core/x86_64/xz/",
        authentication=(AuthenticationMethod.DISTRIBUTION_SIGNATURE,),
        strata_covered=frozenset({BoundaryStratum.S_DISTRIBUTION}),
        retrieval_rule="Arch Linux Archive: list xz package versions in frame window; "
                       "record version, packager, build date, signature",
    ),

    SourceRecord(
        source_id="SRC-DIST-04",
        name="Ubuntu Launchpad (xz-utils)",
        category=SourceCategory.DISTRIBUTION,
        url="https://launchpad.net/ubuntu/+source/xz-utils",
        authentication=(AuthenticationMethod.DISTRIBUTION_SIGNATURE,),
        strata_covered=frozenset({BoundaryStratum.S_DISTRIBUTION, BoundaryStratum.S_BUILD}),
        retrieval_rule="Launchpad API: list published versions in frame window; "
                       "record version, series, pocket, date published, build URLs",
    ),

    SourceRecord(
        source_id="SRC-DIST-05",
        name="Alpine Linux packages (xz)",
        category=SourceCategory.DISTRIBUTION,
        url="https://pkgs.alpinelinux.org/packages?name=xz",
        authentication=(AuthenticationMethod.DISTRIBUTION_SIGNATURE,),
        strata_covered=frozenset({BoundaryStratum.S_DISTRIBUTION}),
        retrieval_rule="Alpine package index: list xz versions in frame window; "
                       "record version, branch, maintainer, build date",
    ),

    SourceRecord(
        source_id="SRC-DIST-06",
        name="Homebrew formulae (xz)",
        category=SourceCategory.DISTRIBUTION,
        url="https://formulae.brew.sh/formula/xz",
        authentication=(AuthenticationMethod.GIT_HASH, AuthenticationMethod.TLS_CERTIFICATE),
        strata_covered=frozenset({BoundaryStratum.S_DISTRIBUTION}),
        retrieval_rule="Homebrew/homebrew-core git history: list formula changes for xz "
                       "in frame window; record commit hash, version, bottle URLs",
    ),

    # === MAILING LISTS ===

    SourceRecord(
        source_id="SRC-ML-01",
        name="oss-security mailing list",
        category=SourceCategory.MAILING_LIST,
        url="https://www.openwall.com/lists/oss-security/",
        authentication=(AuthenticationMethod.TLS_CERTIFICATE, AuthenticationMethod.CONTENT_HASH),
        strata_covered=frozenset({BoundaryStratum.S_RELEASE, BoundaryStratum.S_RUNTIME_AUTH}),
        retrieval_rule="Retrieve all posts mentioning 'xz' or 'CVE-2024-3094' in frame window; "
                       "record message-id, date, author, subject, body hash",
        notes="Contains the primary disclosure (2024-03-29)",
    ),

    SourceRecord(
        source_id="SRC-ML-02",
        name="Distribution security announcement lists",
        category=SourceCategory.MAILING_LIST,
        url="(multiple; see retrieval rule)",
        authentication=(AuthenticationMethod.GPG_SIGNATURE, AuthenticationMethod.TLS_CERTIFICATE),
        strata_covered=frozenset({BoundaryStratum.S_DISTRIBUTION}),
        retrieval_rule="Retrieve security announcements for xz-utils/CVE-2024-3094 from: "
                       "debian-security-announce, fedora-package-announce, "
                       "arch-security, ubuntu-security-announce. "
                       "Record message-id, date, DSA/advisory ID, affected versions, fixed versions",
    ),

    # === ADVISORIES ===

    SourceRecord(
        source_id="SRC-ADV-01",
        name="NVD CVE-2024-3094",
        category=SourceCategory.ADVISORY,
        url="https://nvd.nist.gov/vuln/detail/cve-2024-3094",
        authentication=(AuthenticationMethod.INSTITUTIONAL_AUTHORITY,
                        AuthenticationMethod.TLS_CERTIFICATE),
        strata_covered=frozenset({BoundaryStratum.S_RELEASE, BoundaryStratum.S_RUNTIME_AUTH}),
        retrieval_rule="NVD API: retrieve full CVE record; "
                       "record published date, modified dates, CVSS, CWE, references, "
                       "affected version ranges",
        notes="Primary XZ citation",
    ),

    SourceRecord(
        source_id="SRC-ADV-02",
        name="GitHub Advisory GHSA-rxwq-x6h5-x525",
        category=SourceCategory.ADVISORY,
        url="https://github.com/advisories/GHSA-rxwq-x6h5-x525",
        authentication=(AuthenticationMethod.INSTITUTIONAL_AUTHORITY,
                        AuthenticationMethod.TLS_CERTIFICATE),
        strata_covered=frozenset({BoundaryStratum.S_RELEASE, BoundaryStratum.S_DISTRIBUTION}),
        retrieval_rule="GitHub Advisory API: retrieve full advisory; "
                       "record published date, severity, affected packages and versions, "
                       "references",
        notes="Primary XZ citation",
    ),

    # === BUILD INFRASTRUCTURE ===

    SourceRecord(
        source_id="SRC-BUILD-01",
        name="Debian snapshot.debian.org build logs",
        category=SourceCategory.BUILD_INFRASTRUCTURE,
        url="https://snapshot.debian.org/",
        authentication=(AuthenticationMethod.INSTITUTIONAL_AUTHORITY,
                        AuthenticationMethod.TLS_CERTIFICATE),
        strata_covered=frozenset({BoundaryStratum.S_BUILD}),
        retrieval_rule="Retrieve build logs for xz-utils source package versions "
                       "in frame window; record builder, build date, build dependencies, "
                       "configure flags, build result hash",
    ),

    SourceRecord(
        source_id="SRC-BUILD-02",
        name="Reproducible Builds project (xz-utils results)",
        category=SourceCategory.BUILD_INFRASTRUCTURE,
        url="https://reproducible-builds.org/",
        authentication=(AuthenticationMethod.TLS_CERTIFICATE,),
        strata_covered=frozenset({BoundaryStratum.S_BUILD}),
        retrieval_rule="Query reproducibility status for xz-utils versions in frame window; "
                       "record version, reproducibility verdict, diffoscope output URL if available",
        notes="Covers Debian reproducible-builds infrastructure",
    ),
)


# ---------------------------------------------------------------------------
# Manifest operations
# ---------------------------------------------------------------------------

def get_sources_for_stratum(stratum: BoundaryStratum) -> list[SourceRecord]:
    """Return all sources covering the given stratum."""
    return [s for s in SOURCE_FRAME_MANIFEST if stratum in s.strata_covered]


def get_source_by_id(source_id: str) -> Optional[SourceRecord]:
    """Look up a source by its ID."""
    for s in SOURCE_FRAME_MANIFEST:
        if s.source_id == source_id:
            return s
    return None


def validate_manifest() -> dict:
    """Validate manifest completeness and internal consistency."""
    errors = []

    # Core strata must have at least one source; installation/runtime may be empty
    core_strata = {BoundaryStratum.S_COMMIT, BoundaryStratum.S_RELEASE,
                   BoundaryStratum.S_BUILD, BoundaryStratum.S_DISTRIBUTION}
    for stratum in BoundaryStratum:
        sources = get_sources_for_stratum(stratum)
        if stratum in core_strata and not sources:
            errors.append(f"No sources cover core stratum {stratum.value}")

    # Source IDs must be unique
    ids = [s.source_id for s in SOURCE_FRAME_MANIFEST]
    if len(ids) != len(set(ids)):
        errors.append("Duplicate source IDs found")

    # All four primary XZ citations must appear
    primary_urls = {
        DISCLOSURE_URL,
        "https://nvd.nist.gov/vuln/detail/cve-2024-3094",
        "https://github.com/tukaani-project/xz/issues",
        "https://github.com/advisories/GHSA-rxwq-x6h5-x525",
    }
    manifest_urls = {s.url for s in SOURCE_FRAME_MANIFEST}
    # Check that primary citations are covered (exact or prefix match)
    for purl in primary_urls:
        if not any(purl in murl or murl in purl for murl in manifest_urls):
            errors.append(f"Primary citation not covered: {purl}")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "source_count": len(SOURCE_FRAME_MANIFEST),
        "strata_coverage": {
            s.value: len(get_sources_for_stratum(s))
            for s in BoundaryStratum
        },
        "frame_start": str(FRAME_START),
        "frame_end": str(FRAME_END),
        "disclosure_date": str(DISCLOSURE_DATE),
    }

===== END FILE: xz_protocol_source_frame.py =====

===== BEGIN FILE: xz_protocol_control_graph.py | SIZE: 14763 bytes | SHA256: 3eb7cc44ab5e88215bd1c7f3c293f999c6a2ee92dd373489b3a2a27cd193689c =====
"""
xz_protocol_control_graph.py -- WithinAuth control-graph standard.

XZ Protocol v0.48, Section 7.4, FREEZE-BLOCKER FB-5.

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

===== END FILE: xz_protocol_control_graph.py =====

===== BEGIN FILE: xz_protocol_phase_a_m3.py | SIZE: 11567 bytes | SHA256: bee318ac05d3098de3c2c0fcb6204452ffcb956b0661855304ccd3f80690eb65 =====
"""
xz_protocol_phase_a_m3.py -- Per-fact M3 vector, M3-FIRST, paired differences.

XZ Protocol v0.48 Phase A Amendment, Section 1.

v0.8.4 repairs from v0.8.3 carrying audit (GPT Sol + Kimi K3):
  F-SOL-083-1: M3Vector is now FROZEN with observations as tuple.
  F-SOL-083-2: censor_status enum membership validated first.
  F-SOL-083-5: M3 endpoint declared SUBSTANTIVE change from parent.
  F-SOL-083-9/F-K3-083-6: bool rejected uniformly at all entry points.
  F-SOL-083-10/F-K3-083-10: raw exceptions wrapped in PhaseAInputError.
  F-K3-083-2: non-finite ratios excluded and counted (PA-Z13).
  F-K3-083-5: provenance docstrings aligned with accident-guard.
  F-K3-083-11: evidence_record_id must be non-empty str for OBSERVED;
               forbidden on non-discovery statuses.
  F-K3-083-14: dead branches removed.

SUBSTANTIVE ENDPOINT CHANGE (declared, not silent): The parent SHVVP
v0.8 defines M3 as ending at the "first correctly adjudicated
consequential fact." This implementation times to the first immutable
saved evidence record that identifies the fact. The distinction is
recorded in Section 13.3.5 and the v0.2 amendment entry. No scalar-preservation claim
is made for inputs where adjudication time differs from evidence time.

The provenance token on PairedDifference is an ACCIDENT GUARD against
casual misuse. It is NOT a security boundary. dataclasses.replace()
and direct token import can bypass it. The BSSG raw-evidence discipline
is enforced at the protocol layer, not at this Python API layer.
"""

from __future__ import annotations

import math
import secrets
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


FROZEN_BUDGET_MINUTES: float = 480.0

_PROVENANCE_TOKEN: str = secrets.token_hex(16)


class CensorStatus(Enum):
    OBSERVED = "OBSERVED"
    RIGHT_CENSORED_BUDGET = "RIGHT_CENSORED_BUDGET"
    CENSORED_EARLY = "CENSORED_EARLY"


class M3FirstResult(Enum):
    NO_DISCOVERY = "NO_DISCOVERY"


class PhaseAInputError(Exception):
    pass


def _reject_bool(value, name: str) -> None:
    if isinstance(value, bool):
        raise PhaseAInputError(f"{name} must not be bool, got {value!r}")
    try:
        import numpy as np
        if isinstance(value, np.bool_):
            raise PhaseAInputError(f"{name} must not be numpy.bool_, got {value!r}")
    except ImportError:
        pass


def _validate_numeric(value, name: str) -> float:
    """Validate and coerce to float. Rejects bool, non-numeric, NaN, Inf, negative."""
    _reject_bool(value, name)
    try:
        fval = float(value)
    except (TypeError, ValueError, OverflowError) as e:
        raise PhaseAInputError(f"{name} must be numeric, got {type(value).__name__}: {e}") from e
    if math.isnan(fval):
        raise PhaseAInputError(f"{name} is NaN")
    if math.isinf(fval):
        raise PhaseAInputError(f"{name} is infinite")
    if fval < 0:
        raise PhaseAInputError(f"{name} is negative ({fval})")
    return fval


def normalize_fact_id(raw: str) -> str:
    """Frozen: strip ASCII whitespace, case-sensitive."""
    if not isinstance(raw, str) or not raw.strip():
        raise PhaseAInputError(f"Fact ID must be a non-empty string, got {raw!r}")
    return raw.strip()


@dataclass(frozen=True)
class M3Observation:
    """One M3 observation: discovery time for fact f under condition c."""
    fact_id: str
    condition: str
    minutes: float
    censor_status: CensorStatus
    evidence_record_id: Optional[str] = None

    def __post_init__(self):
        # Enum membership FIRST (F-SOL-083-2)
        if not isinstance(self.censor_status, CensorStatus):
            raise PhaseAInputError(
                f"censor_status must be a CensorStatus enum member, "
                f"got {type(self.censor_status).__name__}: {self.censor_status!r}"
            )
        normalize_fact_id(self.fact_id)
        _validate_numeric(self.minutes, f"M3({self.fact_id},{self.condition})")
        if self.condition not in ("A", "B"):
            raise PhaseAInputError(f"Condition must be 'A' or 'B', got '{self.condition}'")

        if self.censor_status == CensorStatus.RIGHT_CENSORED_BUDGET:
            if self.minutes != FROZEN_BUDGET_MINUTES:
                raise PhaseAInputError(
                    f"RIGHT_CENSORED_BUDGET requires minutes == {FROZEN_BUDGET_MINUTES}, "
                    f"got {self.minutes}")
            if self.evidence_record_id is not None:
                raise PhaseAInputError(
                    f"RIGHT_CENSORED_BUDGET must not carry evidence_record_id")
        elif self.censor_status == CensorStatus.CENSORED_EARLY:
            if self.minutes >= FROZEN_BUDGET_MINUTES:
                raise PhaseAInputError(
                    f"CENSORED_EARLY requires minutes < {FROZEN_BUDGET_MINUTES}, "
                    f"got {self.minutes}")
            if self.evidence_record_id is not None:
                raise PhaseAInputError(
                    f"CENSORED_EARLY must not carry evidence_record_id")
        elif self.censor_status == CensorStatus.OBSERVED:
            if not isinstance(self.evidence_record_id, str) or not self.evidence_record_id.strip():
                raise PhaseAInputError(
                    f"OBSERVED requires a non-empty str evidence_record_id, "
                    f"got {self.evidence_record_id!r}")
            if self.minutes > FROZEN_BUDGET_MINUTES:
                raise PhaseAInputError(
                    f"OBSERVED requires minutes <= {FROZEN_BUDGET_MINUTES}, "
                    f"got {self.minutes}")

    @property
    def is_observed(self) -> bool:
        return self.censor_status == CensorStatus.OBSERVED


@dataclass(frozen=True)
class M3Vector:
    """Immutable per-fact M3 vector for one condition.

    observations is a tuple (immutable). No mutation after construction.
    (F-SOL-083-1: closes the mutable-list bypass permanently.)
    """
    condition: str
    observations: tuple[M3Observation, ...] = ()

    def __post_init__(self):
        if not isinstance(self.observations, tuple):
            try:
                object.__setattr__(self, 'observations', tuple(self.observations))
            except TypeError as e:
                raise PhaseAInputError(f"observations must be iterable: {e}") from e
        seen = set()
        for obs in self.observations:
            if not isinstance(obs, M3Observation):
                raise PhaseAInputError(
                    f"Each observation must be M3Observation, got {type(obs).__name__}")
            if obs.condition != self.condition:
                raise PhaseAInputError(
                    f"Observation condition '{obs.condition}' != vector '{self.condition}'")
            nid = normalize_fact_id(obs.fact_id)
            if nid in seen:
                raise PhaseAInputError(
                    f"Duplicate fact_id '{obs.fact_id}' in condition '{self.condition}'")
            seen.add(nid)

    def with_obs(self, obs: M3Observation) -> 'M3Vector':
        """Return a NEW vector with obs appended. Original unchanged."""
        return M3Vector(self.condition, self.observations + (obs,))

    @property
    def observed_fact_ids(self) -> set[str]:
        return {normalize_fact_id(o.fact_id) for o in self.observations if o.is_observed}

    def get(self, fact_id: str) -> Optional[M3Observation]:
        nid = normalize_fact_id(fact_id)
        for o in self.observations:
            if normalize_fact_id(o.fact_id) == nid:
                return o
        return None

    def m3_first(self) -> float | M3FirstResult:
        """Observed-only scalar summary."""
        observed = [o.minutes for o in self.observations if o.is_observed]
        return min(observed) if observed else M3FirstResult.NO_DISCOVERY


def compute_shared_set(vec_a: M3Vector, vec_b: M3Vector) -> list[str]:
    """S = facts OBSERVED by both conditions. Sorted ascending."""
    return sorted(vec_a.observed_fact_ids & vec_b.observed_fact_ids)


@dataclass(frozen=True)
class PairedDifference:
    """Delta-M3(f) = M3(f,A) - M3(f,B) for one shared fact.

    The _provenance field is an ACCIDENT GUARD (not a security boundary).
    dataclasses.replace() and direct token import can bypass it.
    See module docstring.
    """
    fact_id: str
    m3_a: float
    m3_b: float
    delta: float
    censor_a: CensorStatus
    censor_b: CensorStatus
    _provenance: str = ""

    def verify_provenance(self) -> None:
        if self._provenance != _PROVENANCE_TOKEN:
            raise PhaseAInputError(
                f"PairedDifference '{self.fact_id}' has invalid provenance. "
                f"This is an accident guard, not a security boundary.")


def compute_paired_differences(
    vec_a: M3Vector, vec_b: M3Vector
) -> list[PairedDifference]:
    if vec_a.condition != "A":
        raise PhaseAInputError(f"First vector must be 'A', got '{vec_a.condition}'")
    if vec_b.condition != "B":
        raise PhaseAInputError(f"Second vector must be 'B', got '{vec_b.condition}'")
    shared = compute_shared_set(vec_a, vec_b)
    results = []
    for fid in shared:
        oa, ob = vec_a.get(fid), vec_b.get(fid)
        assert oa and ob and oa.is_observed and ob.is_observed
        delta = oa.minutes - ob.minutes
        results.append(PairedDifference(
            fid, oa.minutes, ob.minutes, delta,
            oa.censor_status, ob.censor_status, _PROVENANCE_TOKEN))
    return results


def compute_median(values: list[float]) -> float:
    """Standard median. Rejects bool."""
    if not values:
        raise PhaseAInputError("Cannot compute median of empty list")
    for v in values:
        _reject_bool(v, "median input")
    s = sorted(values)
    n = len(s)
    mid = n // 2
    return s[mid] if n % 2 == 1 else (s[mid-1] + s[mid]) / 2.0


def evaluate_t2_point(paired_diffs: list[PairedDifference]) -> dict:
    """T2 point statistics. PA-Z1/PA-Z9/PA-Z13."""
    for pd in paired_diffs:
        pd.verify_provenance()
    n = len(paired_diffs)
    if n == 0:
        return {"shared_set_size": 0, "evaluable": False, "rule": "PA-Z1",
                "absolute_median": None, "absolute_gate_met": None,
                "relative_ratios": [], "relative_excluded_count": 0,
                "relative_nonfinite_count": 0,
                "relative_median": None, "relative_gate_met": None}

    deltas = [pd.delta for pd in paired_diffs]
    abs_median = compute_median(deltas)
    abs_gate = abs_median >= 30.0

    ratios, excluded, nonfinite = [], 0, 0
    for pd in paired_diffs:
        if pd.m3_a == 0:
            excluded += 1
        else:
            r = pd.delta / pd.m3_a
            if math.isfinite(r):
                ratios.append(r)
            else:
                nonfinite += 1  # PA-Z13

    if not ratios:
        rule = "PA-Z9" if excluded == n else "PA-Z13"
        return {"shared_set_size": n, "evaluable": False, "rule": rule,
                "absolute_median": abs_median, "absolute_gate_met": abs_gate,
                "relative_ratios": [], "relative_excluded_count": excluded,
                "relative_nonfinite_count": nonfinite,
                "relative_median": None, "relative_gate_met": None}

    rel_median = compute_median(ratios)
    return {"shared_set_size": n, "evaluable": True, "rule": None,
            "absolute_median": abs_median, "absolute_gate_met": abs_gate,
            "relative_ratios": ratios, "relative_excluded_count": excluded,
            "relative_nonfinite_count": nonfinite,
            "relative_median": rel_median, "relative_gate_met": rel_median >= 0.20}

===== END FILE: xz_protocol_phase_a_m3.py =====

===== BEGIN FILE: xz_protocol_phase_a_intervals.py | SIZE: 14309 bytes | SHA256: 900a095e887140c199f9b8e7ec6f4c86953f9f5b87f8520af52722bd53a7d9a0 =====
"""
xz_protocol_phase_a_intervals.py -- Phase A BCa bootstrap intervals.

XZ Protocol v0.48 Phase A Amendment, Section 2.

THE CODE IS THE SOLE NORMATIVE DEFINITION of the interval computation.
Golden-vector receipts in the test suite pin exact numerical outputs.

Code-level degeneracy rules: PA-Z1 through PA-Z3, PA-Z5 through PA-Z14
(thirteen rules). PA-Z4 (alpha undefined / INDETERMINATE-ADJUDICATION) is
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

from xz_protocol_phase_a_m3 import (
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
    # H-3: zero-resample intervals cannot meaningfully exclude zero
    if n_resamples == 0:
        excludes = False
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
    """T5: M7(B)/M7(A). Interval conjunct formally retired (Section 13.3.3, v0.2 entry)."""
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
from xz_protocol_phase_a_m3 import _validate_numeric


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

===== END FILE: xz_protocol_phase_a_intervals.py =====

---

# Bismillah ir-Rahman ir-Rahim
