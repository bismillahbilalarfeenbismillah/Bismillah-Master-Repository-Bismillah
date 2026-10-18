# Bismillah ir-Rahman ir-Rahim

# R0199 -- xz_protocol_condition_a.py — xz_protocol_condition_a.py -- Executable Condition A disposition function.

**Chronological Index:** 667 of 995  
**Date:** Undated  
**Section:** IV. XZ Protocol  
**Source File:** xz_protocol_condition_a.py  
**Source Format:** py  
**SHA-256:** `dc2cbd9feb46ff15fb72215e0cfc7432fbb4ae6603a61bb30b18d9f4b905badc`  

---

## R0199 · xz_protocol_condition_a.py — xz_protocol_condition_a.py -- Executable Condition A disposition function.

- section: IV. XZ Protocol
- source_file: xz_protocol_condition_a.py
- source_format: py
- merged_variants: 2 (xz_protocol_condition_a.py.txt; xz_protocol_condition_a.txt)
- text_sha256: dc2cbd9feb46ff15fb72215e0cfc7432fbb4ae6603a61bb30b18d9f4b905badc

"""
xz_protocol_condition_a.py -- Executable Condition A disposition function.

XZ Protocol v0.75, Section 6.1, FREEZE-BLOCKER FB-3.

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

---

# Bismillah ir-Rahman ir-Rahim
