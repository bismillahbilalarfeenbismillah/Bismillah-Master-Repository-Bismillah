# Bismillah ir-Rahman ir-Rahim

# R0203 -- xz_protocol_kernel.py — # Version: XZ Protocol v0.75

**Chronological Index:** 669 of 995  
**Date:** Undated  
**Section:** IV. XZ Protocol  
**Source File:** xz_protocol_kernel.py  
**Source Format:** py  
**SHA-256:** `41c8a887786a1b94a67b81a53da54943f72a36ebf104d0eca751a900207c094f`  

---

## R0203 · xz_protocol_kernel.py — # Version: XZ Protocol v0.75

- section: IV. XZ Protocol
- source_file: xz_protocol_kernel.py
- source_format: py
- merged_variants: 2 (xz_protocol_kernel.py.txt; xz_protocol_kernel.txt)
- text_sha256: 41c8a887786a1b94a67b81a53da54943f72a36ebf104d0eca751a900207c094f

"""
# Version: XZ Protocol v0.75
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

---

# Bismillah ir-Rahman ir-Rahim
