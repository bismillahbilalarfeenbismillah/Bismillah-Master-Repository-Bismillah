# Bismillah ir-Rahman ir-Rahim

# R0384 -- shvvp_v0_8_route_gates.py — Executable route-level DESCRIPTIVE GATES for SHVVP v0.8-rc1.

**Chronological Index:** 753 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** shvvp_v0_8_route_gates.py  
**Source Format:** py  
**SHA-256:** `acd2e378229a9b1af6af69a8852e4614b87f5fbe325557cffe06c0606744008a`  

---

## R0384 · shvvp_v0_8_route_gates.py — Executable route-level DESCRIPTIVE GATES for SHVVP v0.8-rc1.

- section: V. BSSG & SHVVP Protocols
- source_file: shvvp_v0_8_route_gates.py
- source_format: py
- merged_variants: 2 (shvvp_v0_7_route_gates.py; shvvp_v0_8_route_gates.py.txt)
- text_sha256: acd2e378229a9b1af6af69a8852e4614b87f5fbe325557cffe06c0606744008a

"""Executable route-level DESCRIPTIVE GATES for SHVVP v0.8-rc1.

This revision absorbs the v0.7 carrying-audit findings F-P7-1 through F-P7-4.
It remains descriptive only: no p-value, null, confidence bound, significance,
false-discovery-rate procedure, generalization, or population-level novelty claim
is produced by the route path.

TRUST BOUNDARY
--------------
1. The three verification keys are frozen inside the canonical manifest. The public
   evaluator exposes no key-override parameter. Replacing any authority key requires
   rebuilding the manifest and therefore changes MANIFEST_SHA256.
2. Channel B is raw evidence and may only carry a commitment_id reference.
3. A SEALED commitment is signed by the frozen commitment authority and includes its
   unique commitment_id.
4. A REALIZED universe requires all of: (a) a commitment-authority-signed pre-run
   commitment; (b) an independent anchor-authority receipt over that pre-run digest;
   (c) individually signed, hash-chained append events from the frozen run logger; and
   (d) a commitment-authority-signed close receipt bound to the pre-run commitment.
   A completed caller-created list and close receipt are insufficient.
5. Commitment bundles are indexed by commitment_id. Unknown, duplicate-by-alias,
   cross-component, cross-version, cross-manifest, or mismatched identifiers reject
   before any share is computed.

The keys below are release public keys only. Their private halves are not included in
this module, the tests, or the packet. Positive test vectors are pre-signed fixtures.
"""
from __future__ import annotations

import hashlib
import json
import unicodedata
from dataclasses import dataclass
from numbers import Integral
from typing import Any, Mapping

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

PROTOCOL_VERSION = "0.8"
RELEASE_STAGE = "rc1"

DOMAIN_SEALED = "SHVVP-V0.8-SEALED-UNIVERSE"
DOMAIN_PRERUN = "SHVVP-V0.8-PRE-RUN-COMMITMENT"
DOMAIN_ANCHOR = "SHVVP-V0.8-PRE-RUN-ANCHOR"
DOMAIN_EVENT = "SHVVP-V0.8-RUN-APPEND-EVENT"
DOMAIN_RUNCLOSE = "SHVVP-V0.8-RUN-CLOSE"
DOMAIN_RUNGENESIS = "SHVVP-V0.8-RUN-GENESIS"

# Three independent public trust roots, frozen before evaluation. There is no
# runtime override. Changing any key changes the canonical manifest digest.
COMMITMENT_AUTHORITY_PUBKEY = "b603204916623ec030e6ba851a321dc67f6a00c7a28bee1d878d0a71a611c251"
RUN_LOGGER_PUBKEY = "8d8dab152398183082c0461ece15d06a58528c1e6df942c153d2cc024bba28a0"
PRERUN_ANCHOR_PUBKEY = "0ebc3b1e23207fd41eef3f519983c5eae76efdd9555d8ec142b7eba3b64e2a73"

# ---------------------------------------------------------------- vocabulary
ROUTE_CLAIM_LABELS = (
    "OUT OF SCOPE",           # ONLY via a validly predeclared exclusion (manifest)
    "INCOMPLETE",             # a COMMITTED component's raw-evidence record is absent
    "FAILED",                 # a zero-tolerance violation was recorded
    "NOT EVALUABLE",          # present but below the frozen minimum, or zero
    "NOT SUPPORTED",          # evaluable, observed pass share below the threshold
    "SUPPORTED-DESCRIPTIVE",  # every committed component present, evaluable, passing
)
WITHDRAWN_LABELS = ("SUPPORTED-INFERENTIAL", "DESCRIPTIVE-ONLY")

KIND_FIXED = "FIXED"
KIND_SEALED = "SEALED"
KIND_REALIZED = "REALIZED"
STATUS_COMMITTED = "COMMITTED"
STATUS_PREDECLARED_CONDITIONAL_OOS = "PREDECLARED_CONDITIONAL_OOS"


class RouteInputError(ValueError):
    """Raised when raw evidence, or a universe commitment, is structurally invalid,
    unbound, or unauthenticated. Nothing is returned, so an invalid, unbound or
    caller-asserted record cannot be laundered into support."""


class CommitmentError(RouteInputError):
    """Raised specifically when a Channel A universe commitment fails to
    authenticate against the trusted authority, its binding, or its run log."""


@dataclass(frozen=True)
class GateSpec:
    key: str
    route: str
    phase: str
    unit: str
    denominator_field: str
    numerator_field: str
    violation_field: str | None
    min_items: int
    threshold: float
    statement: str
    scope_limit: str

    @property
    def count_fields(self) -> tuple[str, ...]:
        f = [self.denominator_field, self.numerator_field]
        if self.violation_field:
            f.append(self.violation_field)
        return tuple(f)


@dataclass(frozen=True)
class ScopeEntry:
    key: str
    status: str
    kind: str
    universe_id: str
    universe_n: int | None       # committed cardinality for KIND_FIXED; else None
    authority: str


CLASS = "G"

REGISTRY: tuple[GateSpec, ...] = (
    GateSpec("R1-A", "R1", "A", "sealed-ledger consequential fact",
             "facts_examined", "facts_incremental", None, 3, 1.0,
             "on this one historical case, SHV surfaced consequential ledger facts "
             "that the provenance baseline missed",
             "single case, no randomisation, no comparison across conditions"),
    GateSpec("R2-A", "R2", "A", "planted caller-context branch",
             "branches_planted", "branches_typed", "branches_dropped_silently", 16,
             0.75,
             "on this one historical case, incompleteness was typed rather than "
             "silently dropped",
             "single case, 16 planted branches, no randomisation"),
    GateSpec("R2-B", "R2", "B", "denied effect request",
             "denials_total", "denials_typed", None, 50, 0.98,
             "in this run, denied effect requests carried a typed reason at the "
             "frozen share",
             "descriptive share within this run only; no population claim, no "
             "significance, no generalization beyond the tested tasks and models"),
    GateSpec("R3-A", "R3", "A", "planted conflict pair",
             "conflicts_planted", "conflicts_preserved",
             "premature_reconciliations", 12, 0.90,
             "on this one historical case, planted conflicts were preserved rather "
             "than prematurely reconciled",
             "single case, 12 planted pairs, no randomisation"),
    GateSpec("R4-B", "R4", "B", "witness-degradation injection",
             "injections_total", "injections_narrowed", "widening_events", 50, 0.90,
             "in this run, witness degradation was followed by strict narrowing of "
             "the permitted effect set at the frozen share",
             "descriptive share within this run only; no population claim, no "
             "significance, no generalization"),
    GateSpec("R4-C", "R4", "C", "witness-degradation injection",
             "injections_total", "injections_narrowed", "widening_events", 216, 0.90,
             "on these private synthetic targets, witness degradation was followed "
             "by strict narrowing at the frozen share",
             "private synthetic targets only; descriptive; no significance, no "
             "generalization"),
    GateSpec("R5-A", "R5", "A", "recorded descendant",
             "descendants_recorded", "descendants_reached", "silent_overwrites", 20,
             0.95,
             "on this one historical case, corrections reached the recorded "
             "descendant set at the frozen share with no silent overwrite",
             "single case, sealed descendant universe, no randomisation"),
    GateSpec("R5-C", "R5", "C", "recorded descendant of a revised report",
             "descendants_recorded", "descendants_reached", "silent_overwrites", 6,
             0.95,
             "on these private synthetic targets, corrections reached the recorded "
             "descendant set at the frozen share with no silent overwrite",
             "no randomised comparator exists for this component; descriptive only"),
    GateSpec("R6-A", "R6", "A", "deliberately absent provenance item",
             "absent_items", "typed_unknown", "typed_clean", 60, 0.98,
             "on this one historical case, absent provenance was typed UNKNOWN "
             "rather than clean",
             "single case, 60 planted absences, no randomisation"),
    GateSpec("R6-B", "R6", "B", "adjudicated missing witness receipt",
             "receipts_adjudicated", "typed_unknown", "typed_clean", 30, 0.95,
             "in this run, missing witness receipts were typed UNKNOWN at the "
             "frozen share with no receipt typed clean",
             "descriptive share within this run only; no population claim, no "
             "significance, no generalization"),
    GateSpec("R6-C", "R6", "C", "adjudicated missing witness receipt",
             "receipts_adjudicated", "typed_unknown", "typed_clean", 30, 0.95,
             "on these private synthetic targets, missing witness receipts were "
             "typed UNKNOWN at the frozen share with no receipt typed clean",
             "private synthetic targets only; descriptive; no significance, no "
             "generalization"),
)

BY_KEY = {g.key: g for g in REGISTRY}
ROUTES = ("R1", "R2", "R3", "R4", "R5", "R6")
ROUTE_COMPONENTS: dict[str, list[str]] = {}
for _g in REGISTRY:
    ROUTE_COMPONENTS.setdefault(_g.route, []).append(_g.key)
FAMILY_F3_GATE_ONLY = tuple(g.key for g in REGISTRY)

# --------------------------------------------------------- frozen scope manifest
SCOPE_MANIFEST: tuple[ScopeEntry, ...] = (
    ScopeEntry("R1-A", STATUS_COMMITTED, KIND_SEALED, "u.r1a.sealed-ledger", None,
               "Section 5.1 sealed ground-truth ledger; cardinality fixed by the "
               "custodian seal and authenticated through Channel A"),
    ScopeEntry("R2-A", STATUS_COMMITTED, KIND_FIXED, "u.r2a.planted-branches", 16,
               "Section 8.2 R2-A: 16 planted caller-context branches"),
    ScopeEntry("R2-B", STATUS_COMMITTED, KIND_REALIZED, "u.r2b.denials-run", None,
               "Section 0.1 A-3.7: realized denied-effect-request count, run-log "
               "committed and authenticated through Channel A"),
    ScopeEntry("R3-A", STATUS_PREDECLARED_CONDITIONAL_OOS, KIND_FIXED,
               "u.r3a.planted-conflicts", 12,
               "Section 0.1 item 2 and Section 8: R3 ConflictLedger instrumentation "
               "is UNKNOWN; OUT OF SCOPE unless an R3-A record is supplied"),
    ScopeEntry("R4-B", STATUS_COMMITTED, KIND_REALIZED, "u.r4b.phaseb-injections",
               None,
               "Section 0.1 A-3.7: realized Phase-B witness-degradation injection "
               "count, run-log committed and authenticated through Channel A"),
    ScopeEntry("R4-C", STATUS_COMMITTED, KIND_FIXED, "u.r4c.phasec-injections", 216,
               "Section 7.2: witness-degradation injection in a randomly selected "
               "half of C-BSSG sessions, that is 216 sessions"),
    ScopeEntry("R5-A", STATUS_COMMITTED, KIND_SEALED, "u.r5a.descendant-universe",
               None,
               "Sections 5.1/M9: correction reach over the sealed descendant "
               "universe; cardinality sealed before results, Channel A"),
    ScopeEntry("R5-C", STATUS_COMMITTED, KIND_SEALED, "u.r5c.revised-descendants",
               None,
               "Sections 7.4/C6: sealed descendant universe for the revised seeded "
               "reports; cardinality sealed before results, Channel A"),
    ScopeEntry("R6-A", STATUS_COMMITTED, KIND_FIXED, "u.r6a.planted-absences", 60,
               "Section 8.2 R6-A: 60 deliberately absent provenance items"),
    ScopeEntry("R6-B", STATUS_COMMITTED, KIND_REALIZED, "u.r6b.receipts-run", None,
               "Section 0.1 A-3.7: realized adjudicated-missing-receipt count, "
               "run-log committed and authenticated through Channel A"),
    ScopeEntry("R6-C", STATUS_COMMITTED, KIND_REALIZED, "u.r6c.receipts-synth", None,
               "Section 0.1 A-3.7: realized adjudicated-missing-receipt count on "
               "private synthetic targets, run-log committed, Channel A"),
)

MANIFEST_BY_KEY = {e.key: e for e in SCOPE_MANIFEST}
assert set(MANIFEST_BY_KEY) == set(BY_KEY), "manifest and registry must cover the "\
    "same components"


def _manifest_canonical() -> str:
    """Canonical manifest including all fixed trust roots and signed-object domains."""
    rows = [
        {"key": e.key, "status": e.status, "kind": e.kind,
         "universe_id": e.universe_id, "universe_n": e.universe_n}
        for e in SCOPE_MANIFEST
    ]
    envelope = {
        "protocol_version": PROTOCOL_VERSION,
        "release_stage": RELEASE_STAGE,
        "authorities": {
            "commitment_authority_pubkey": COMMITMENT_AUTHORITY_PUBKEY,
            "run_logger_pubkey": RUN_LOGGER_PUBKEY,
            "prerun_anchor_pubkey": PRERUN_ANCHOR_PUBKEY,
        },
        "domains": [DOMAIN_SEALED, DOMAIN_PRERUN, DOMAIN_ANCHOR, DOMAIN_EVENT,
                    DOMAIN_RUNCLOSE, DOMAIN_RUNGENESIS],
        "components": rows,
    }
    return json.dumps(envelope, sort_keys=True, separators=(",", ":"))


MANIFEST_SHA256 = hashlib.sha256(_manifest_canonical().encode("utf-8")).hexdigest()

_BIND_COMMON = ("manifest_sha256", "universe_id")
_BIND_BY_KIND = {
    KIND_FIXED: (),
    KIND_SEALED: ("commitment_id",),
    KIND_REALIZED: ("commitment_id",),
}
_OPTIONAL_FIELDS = ("reconciliation",)
_FORBIDDEN_IN_RAW = (
    "sealed_universe_n", "sealed_universe_hash", "realized_total", "run_log_hash",
    "signature", "sealed_universe_inventory_hash", "final_chain_hash",
    "pre_run", "anchor", "close", "pre_run_commitment", "anchor_receipt",
    "close_receipt", "logger_pubkey", "authority_pubkey", "event_signature",
)


def _canonical_bytes(obj: Any) -> bytes:
    """UTF-8, NFC, sorted keys, no whitespace, no floats."""
    def norm(x: Any) -> Any:
        if isinstance(x, str):
            return unicodedata.normalize("NFC", x)
        if isinstance(x, bool) or isinstance(x, Integral):
            return int(x)
        if isinstance(x, float):
            raise CommitmentError("floating-point values are not canonicalizable")
        if isinstance(x, Mapping):
            return {norm(k): norm(v) for k, v in x.items()}
        if isinstance(x, (list, tuple)):
            return [norm(v) for v in x]
        if x is None:
            return None
        raise CommitmentError("uncanonicalizable value %r" % type(x).__name__)
    return json.dumps(norm(obj), sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False).encode("utf-8")


def _req(fields: Mapping[str, Any], name: str) -> Any:
    if name not in fields:
        raise CommitmentError("commitment payload missing field %r" % name)
    return fields[name]


def _exact_keys(fields: Mapping[str, Any], expected: set[str], what: str) -> None:
    extra = sorted(set(fields) - expected)
    missing = sorted(expected - set(fields))
    if extra or missing:
        raise CommitmentError("%s: exact signed schema mismatch; missing=%s extra=%s"
                              % (what, missing, extra))


def _positive_int(value: Any, label: str, what: str, allow_zero: bool = False) -> int:
    if not isinstance(value, Integral) or isinstance(value, bool):
        raise CommitmentError("%s: %s must be an integer" % (what, label))
    value = int(value)
    if value < (0 if allow_zero else 1):
        raise CommitmentError("%s: %s must be %s" %
                              (what, label, "non-negative" if allow_zero else "positive"))
    return value


def _nonempty(value: Any, label: str, what: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise CommitmentError("%s: %s must be a non-empty string" % (what, label))
    return value


def _digest(value: Any, label: str, what: str) -> str:
    s = _nonempty(value, label, what)
    try:
        b = bytes.fromhex(s)
    except ValueError:
        raise CommitmentError("%s: %s must be hexadecimal" % (what, label))
    if len(b) != 32:
        raise CommitmentError("%s: %s must encode exactly 32 bytes" % (what, label))
    return s.lower()


def _timestamp(value: Any, label: str, what: str):
    from datetime import datetime, timezone
    s = _nonempty(value, label, what)
    if not s.endswith("Z"):
        raise CommitmentError("%s: %s must be an RFC3339 UTC timestamp ending Z"
                              % (what, label))
    try:
        dt = datetime.fromisoformat(s[:-1] + "+00:00")
    except ValueError:
        raise CommitmentError("%s: %s is not a valid RFC3339 timestamp" % (what, label))
    if dt.tzinfo != timezone.utc:
        raise CommitmentError("%s: %s must be UTC" % (what, label))
    return dt


def _pubkey(hexkey: str, label: str) -> Ed25519PublicKey:
    try:
        raw = bytes.fromhex(hexkey)
        if len(raw) != 32:
            raise ValueError("must encode 32 bytes")
        return Ed25519PublicKey.from_public_bytes(raw)
    except Exception as exc:
        raise CommitmentError("frozen %s is not a valid Ed25519 key: %s" % (label, exc))


def _verify_sig(pub_hex: str, signature_hex: Any, payload: bytes, what: str) -> None:
    if not isinstance(signature_hex, str) or not signature_hex.strip():
        raise CommitmentError("%s: signature must be a non-empty hex string" % what)
    try:
        sig = bytes.fromhex(signature_hex)
        _pubkey(pub_hex, what).verify(sig, payload)
    except (InvalidSignature, ValueError):
        raise CommitmentError("%s: signature does not verify against its frozen authority"
                              % what)


def sealed_commitment_payload(fields: Mapping[str, Any]) -> bytes:
    body = {
        "domain": DOMAIN_SEALED,
        "commitment_id": _req(fields, "commitment_id"),
        "protocol_version": _req(fields, "protocol_version"),
        "manifest_sha256": _req(fields, "manifest_sha256"),
        "component": _req(fields, "component"),
        "universe_id": _req(fields, "universe_id"),
        "sealed_universe_n": _req(fields, "sealed_universe_n"),
        "sealed_universe_inventory_hash": _req(fields, "sealed_universe_inventory_hash"),
        "authority": _req(fields, "authority"),
        "commitment_sequence": _req(fields, "commitment_sequence"),
        "committed_at": _req(fields, "committed_at"),
    }
    return _canonical_bytes(body)


def pre_run_commitment_payload(fields: Mapping[str, Any]) -> bytes:
    body = {
        "domain": DOMAIN_PRERUN,
        "commitment_id": _req(fields, "commitment_id"),
        "protocol_version": _req(fields, "protocol_version"),
        "manifest_sha256": _req(fields, "manifest_sha256"),
        "component": _req(fields, "component"),
        "universe_id": _req(fields, "universe_id"),
        "run_id": _req(fields, "run_id"),
        "event_schema_sha256": _req(fields, "event_schema_sha256"),
        "inclusion_rule_sha256": _req(fields, "inclusion_rule_sha256"),
        "genesis_hash": _req(fields, "genesis_hash"),
        "logger_pubkey": _req(fields, "logger_pubkey"),
        "authority": _req(fields, "authority"),
        "commitment_sequence": _req(fields, "commitment_sequence"),
        "committed_at": _req(fields, "committed_at"),
    }
    return _canonical_bytes(body)


def pre_run_digest(fields: Mapping[str, Any]) -> str:
    return hashlib.sha256(pre_run_commitment_payload(fields)).hexdigest()


def pre_run_anchor_payload(fields: Mapping[str, Any]) -> bytes:
    body = {
        "domain": DOMAIN_ANCHOR,
        "anchor_id": _req(fields, "anchor_id"),
        "commitment_id": _req(fields, "commitment_id"),
        "pre_run_commitment_sha256": _req(fields, "pre_run_commitment_sha256"),
        "manifest_sha256": _req(fields, "manifest_sha256"),
        "anchor_sequence": _req(fields, "anchor_sequence"),
        "anchored_at": _req(fields, "anchored_at"),
        "authority": _req(fields, "authority"),
    }
    return _canonical_bytes(body)


def run_event_payload(fields: Mapping[str, Any]) -> bytes:
    body = {
        "domain": DOMAIN_EVENT,
        "commitment_id": _req(fields, "commitment_id"),
        "pre_run_commitment_sha256": _req(fields, "pre_run_commitment_sha256"),
        "protocol_version": _req(fields, "protocol_version"),
        "manifest_sha256": _req(fields, "manifest_sha256"),
        "component": _req(fields, "component"),
        "universe_id": _req(fields, "universe_id"),
        "run_id": _req(fields, "run_id"),
        "sequence": _req(fields, "sequence"),
        "previous_chain_hash": _req(fields, "previous_chain_hash"),
        "observed_at": _req(fields, "observed_at"),
        "event": _req(fields, "event"),
    }
    return _canonical_bytes(body)


def run_close_payload(fields: Mapping[str, Any]) -> bytes:
    body = {
        "domain": DOMAIN_RUNCLOSE,
        "close_id": _req(fields, "close_id"),
        "commitment_id": _req(fields, "commitment_id"),
        "pre_run_commitment_sha256": _req(fields, "pre_run_commitment_sha256"),
        "protocol_version": _req(fields, "protocol_version"),
        "manifest_sha256": _req(fields, "manifest_sha256"),
        "component": _req(fields, "component"),
        "universe_id": _req(fields, "universe_id"),
        "run_id": _req(fields, "run_id"),
        "realized_total": _req(fields, "realized_total"),
        "first_sequence": _req(fields, "first_sequence"),
        "last_sequence": _req(fields, "last_sequence"),
        "final_chain_hash": _req(fields, "final_chain_hash"),
        "authority": _req(fields, "authority"),
        "closed_at": _req(fields, "closed_at"),
    }
    return _canonical_bytes(body)


def expected_run_genesis(pre_run: Mapping[str, Any]) -> str:
    body = {
        "domain": DOMAIN_RUNGENESIS,
        "commitment_id": _req(pre_run, "commitment_id"),
        "protocol_version": _req(pre_run, "protocol_version"),
        "manifest_sha256": _req(pre_run, "manifest_sha256"),
        "component": _req(pre_run, "component"),
        "universe_id": _req(pre_run, "universe_id"),
        "run_id": _req(pre_run, "run_id"),
        "event_schema_sha256": _req(pre_run, "event_schema_sha256"),
        "inclusion_rule_sha256": _req(pre_run, "inclusion_rule_sha256"),
        "logger_pubkey": _req(pre_run, "logger_pubkey"),
    }
    return hashlib.sha256(_canonical_bytes(body)).hexdigest()


def _verify_binding(obj: Mapping[str, Any], key: str, entry: ScopeEntry,
                    what: str) -> None:
    if obj.get("protocol_version") != PROTOCOL_VERSION:
        raise CommitmentError("%s: protocol_version is not %s (cross-version replay)"
                              % (what, PROTOCOL_VERSION))
    if obj.get("manifest_sha256") != MANIFEST_SHA256:
        raise CommitmentError("%s: binds a different manifest (cross-manifest replay)"
                              % what)
    if obj.get("component") != key:
        raise CommitmentError("%s: component %r does not match %r (cross-component replay)"
                              % (what, obj.get("component"), key))
    if obj.get("universe_id") != entry.universe_id:
        raise CommitmentError("%s: universe_id %r does not match %r"
                              % (what, obj.get("universe_id"), entry.universe_id))


def verify_sealed_commitment(key: str, entry: ScopeEntry,
                             commitment: Mapping[str, Any], expected_id: str) -> int:
    what = "sealed commitment for %s" % key
    if not isinstance(commitment, Mapping):
        raise CommitmentError("%s: commitment must be a mapping" % what)
    expected = {"kind", "commitment_id", "protocol_version", "manifest_sha256",
                "component", "universe_id", "sealed_universe_n",
                "sealed_universe_inventory_hash", "authority",
                "commitment_sequence", "committed_at", "signature"}
    _exact_keys(commitment, expected, what)
    if commitment.get("kind") != KIND_SEALED:
        raise CommitmentError("%s: kind must be SEALED" % what)
    cid = _nonempty(commitment.get("commitment_id"), "commitment_id", what)
    if cid != expected_id:
        raise CommitmentError("%s: signed commitment_id %r does not match raw reference %r"
                              % (what, cid, expected_id))
    _verify_binding(commitment, key, entry, what)
    n = _positive_int(commitment.get("sealed_universe_n"), "sealed_universe_n",
                      what, allow_zero=True)
    _digest(commitment.get("sealed_universe_inventory_hash"),
            "sealed_universe_inventory_hash", what)
    _positive_int(commitment.get("commitment_sequence"), "commitment_sequence", what)
    _timestamp(commitment.get("committed_at"), "committed_at", what)
    _verify_sig(COMMITMENT_AUTHORITY_PUBKEY, commitment.get("signature"),
                sealed_commitment_payload(commitment), what)
    return n


def verify_realized_commitment(key: str, entry: ScopeEntry,
                               bundle: Mapping[str, Any], run_log: Any,
                               expected_id: str) -> int:
    what = "realized commitment bundle for %s" % key
    if not isinstance(bundle, Mapping):
        raise CommitmentError("%s: bundle must be a mapping" % what)
    _exact_keys(bundle, {"kind", "commitment_id", "pre_run", "anchor", "close"}, what)
    if bundle.get("kind") != KIND_REALIZED:
        raise CommitmentError("%s: kind must be REALIZED" % what)
    if bundle.get("commitment_id") != expected_id:
        raise CommitmentError("%s: bundle commitment_id does not match raw reference"
                              % what)
    pre = bundle.get("pre_run"); anchor = bundle.get("anchor"); close = bundle.get("close")
    if not all(isinstance(x, Mapping) for x in (pre, anchor, close)):
        raise CommitmentError("%s: pre_run, anchor and close mappings are all required"
                              % what)

    pre_expected = {"commitment_id", "protocol_version", "manifest_sha256",
                    "component", "universe_id", "run_id", "event_schema_sha256",
                    "inclusion_rule_sha256", "genesis_hash", "logger_pubkey",
                    "authority", "commitment_sequence", "committed_at", "signature"}
    _exact_keys(pre, pre_expected, what + " pre_run")
    if pre.get("commitment_id") != expected_id:
        raise CommitmentError("%s: pre-run commitment_id mismatch" % what)
    _verify_binding(pre, key, entry, what + " pre_run")
    _digest(pre.get("event_schema_sha256"), "event_schema_sha256", what)
    _digest(pre.get("inclusion_rule_sha256"), "inclusion_rule_sha256", what)
    _digest(pre.get("genesis_hash"), "genesis_hash", what)
    if pre.get("logger_pubkey") != RUN_LOGGER_PUBKEY:
        raise CommitmentError("%s: pre-run logger_pubkey is not the manifest-bound key"
                              % what)
    if pre.get("genesis_hash") != expected_run_genesis(pre):
        raise CommitmentError("%s: genesis_hash is not the deterministic pre-run genesis"
                              % what)
    _positive_int(pre.get("commitment_sequence"), "commitment_sequence", what)
    committed_at = _timestamp(pre.get("committed_at"), "committed_at", what)
    _verify_sig(COMMITMENT_AUTHORITY_PUBKEY, pre.get("signature"),
                pre_run_commitment_payload(pre), what + " pre_run")
    pre_digest = pre_run_digest(pre)

    anchor_expected = {"anchor_id", "commitment_id", "pre_run_commitment_sha256",
                       "manifest_sha256", "anchor_sequence", "anchored_at",
                       "authority", "signature"}
    _exact_keys(anchor, anchor_expected, what + " anchor")
    if anchor.get("commitment_id") != expected_id:
        raise CommitmentError("%s: anchor commitment_id mismatch" % what)
    if anchor.get("manifest_sha256") != MANIFEST_SHA256:
        raise CommitmentError("%s: anchor binds a different manifest" % what)
    if anchor.get("pre_run_commitment_sha256") != pre_digest:
        raise CommitmentError("%s: anchor does not bind the verified pre-run commitment"
                              % what)
    _digest(anchor.get("pre_run_commitment_sha256"),
            "pre_run_commitment_sha256", what)
    _positive_int(anchor.get("anchor_sequence"), "anchor_sequence", what)
    anchored_at = _timestamp(anchor.get("anchored_at"), "anchored_at", what)
    if anchored_at < committed_at:
        raise CommitmentError("%s: anchor predates the pre-run commitment" % what)
    _verify_sig(PRERUN_ANCHOR_PUBKEY, anchor.get("signature"),
                pre_run_anchor_payload(anchor), what + " anchor")

    close_expected = {"close_id", "commitment_id", "pre_run_commitment_sha256",
                      "protocol_version", "manifest_sha256", "component",
                      "universe_id", "run_id", "realized_total", "first_sequence",
                      "last_sequence", "final_chain_hash", "authority", "closed_at",
                      "signature"}
    _exact_keys(close, close_expected, what + " close")
    if close.get("commitment_id") != expected_id:
        raise CommitmentError("%s: close commitment_id mismatch" % what)
    _verify_binding(close, key, entry, what + " close")
    if close.get("pre_run_commitment_sha256") != pre_digest:
        raise CommitmentError("%s: close does not bind the verified pre-run commitment"
                              % what)
    if close.get("run_id") != pre.get("run_id"):
        raise CommitmentError("%s: close run_id does not match pre-run run_id" % what)
    closed_at = _timestamp(close.get("closed_at"), "closed_at", what)
    if closed_at < anchored_at:
        raise CommitmentError("%s: close predates the independent pre-run anchor" % what)
    _verify_sig(COMMITMENT_AUTHORITY_PUBKEY, close.get("signature"),
                run_close_payload(close), what + " close")

    if not isinstance(run_log, (list, tuple)):
        raise CommitmentError("%s: ordered individually signed append events required"
                              % what)
    total = _positive_int(close.get("realized_total"), "realized_total", what,
                          allow_zero=True)
    first = _positive_int(close.get("first_sequence"), "first_sequence", what,
                          allow_zero=True)
    last = _positive_int(close.get("last_sequence"), "last_sequence", what,
                         allow_zero=True)
    if total == 0:
        if run_log or first != 0 or last != 0:
            raise CommitmentError("%s: zero-event close must use first=last=0 and empty log"
                                  % what)
    else:
        if first != 1 or last != total or len(run_log) != total:
            raise CommitmentError("%s: close range/count disagrees with append history"
                                  % what)

    chain = pre.get("genesis_hash")
    previous_time = anchored_at
    event_expected = {"commitment_id", "pre_run_commitment_sha256",
                      "protocol_version", "manifest_sha256", "component",
                      "universe_id", "run_id", "sequence", "previous_chain_hash",
                      "observed_at", "event", "signature"}
    for idx, ev in enumerate(run_log, start=1):
        if not isinstance(ev, Mapping):
            raise CommitmentError("%s: append event %d is not a mapping" % (what, idx))
        _exact_keys(ev, event_expected, "%s append event %d" % (what, idx))
        _verify_binding(ev, key, entry, "%s append event %d" % (what, idx))
        if ev.get("commitment_id") != expected_id:
            raise CommitmentError("%s: event %d commitment_id mismatch" % (what, idx))
        if ev.get("pre_run_commitment_sha256") != pre_digest:
            raise CommitmentError("%s: event %d does not bind the pre-run commitment"
                                  % (what, idx))
        if ev.get("run_id") != pre.get("run_id"):
            raise CommitmentError("%s: event %d run_id mismatch" % (what, idx))
        if _positive_int(ev.get("sequence"), "sequence", what) != idx:
            raise CommitmentError("%s: append-event sequence is not contiguous from 1"
                                  % what)
        if ev.get("previous_chain_hash") != chain:
            raise CommitmentError("%s: event %d previous_chain_hash mismatch"
                                  % (what, idx))
        observed = _timestamp(ev.get("observed_at"), "observed_at", what)
        if observed < previous_time or observed > closed_at:
            raise CommitmentError("%s: event %d timestamp is outside anchored run order"
                                  % (what, idx))
        previous_time = observed
        if not isinstance(ev.get("event"), Mapping):
            raise CommitmentError("%s: event %d payload must be a mapping" % (what, idx))
        _verify_sig(RUN_LOGGER_PUBKEY, ev.get("signature"), run_event_payload(ev),
                    "%s append event %d" % (what, idx))
        chain = hashlib.sha256(_canonical_bytes(ev)).hexdigest()

    if chain != close.get("final_chain_hash"):
        raise CommitmentError("%s: final append chain does not match signed close"
                              % what)
    return total


# ---------------------------------------------------------------- validation

def _int_field(record: Mapping[str, Any], name: str, key: str) -> int:
    if name not in record:
        raise RouteInputError("%s: required raw field %r is missing" % (key, name))
    value = record[name]
    if isinstance(value, bool) or not isinstance(value, Integral):
        raise RouteInputError("%s: raw field %r must be an integer, got %r"
                              % (key, name, type(value).__name__))
    v = int(value)
    if v < 0:
        raise RouteInputError("%s: raw field %r must be non-negative, got %d"
                              % (key, name, v))
    return v


def _str_field(record: Mapping[str, Any], name: str, key: str) -> str:
    if name not in record:
        raise RouteInputError("%s: required binding field %r is missing" % (key, name))
    value = record[name]
    if not isinstance(value, str) or not value.strip():
        raise RouteInputError("%s: binding field %r must be a non-empty string"
                              % (key, name))
    return value


def _required_fields(entry: ScopeEntry, spec: GateSpec) -> tuple[str, ...]:
    return spec.count_fields + _BIND_COMMON + _BIND_BY_KIND[entry.kind]


def _check_binding(key: str, entry: ScopeEntry, record: Mapping[str, Any],
                   total: int, universe_n: int) -> tuple[int, int, list[str]]:
    """Verify the manifest and universe binding on the raw record, then enforce
    equality or reconciliation against the AUTHORITATIVE `universe_n` already
    obtained from the manifest (FIXED) or a verified Channel A commitment
    (SEALED, REALIZED). The raw record can no longer define the cardinality."""
    notes: list[str] = []
    manifest_hash = _str_field(record, "manifest_sha256", key)
    if manifest_hash != MANIFEST_SHA256:
        raise RouteInputError(
            "%s: manifest_sha256 %r does not match the frozen scope manifest %r"
            % (key, manifest_hash, MANIFEST_SHA256))
    universe_id = _str_field(record, "universe_id", key)
    if universe_id != entry.universe_id:
        raise RouteInputError(
            "%s: universe_id %r does not match the committed universe %r"
            % (key, universe_id, entry.universe_id))
    if entry.kind == KIND_FIXED:
        notes.append("committed universe: FIXED cardinality %d (%s)"
                     % (universe_n, entry.authority))
    elif entry.kind == KIND_SEALED:
        notes.append("committed universe: SEALED cardinality %d from an authenticated "
                     "Channel A commitment (%s)" % (universe_n, entry.authority))
    else:
        notes.append("committed universe: REALIZED total %d from an authenticated "
                     "run-close receipt (%s)" % (universe_n, entry.authority))
    effective_total = _enforce_completeness(key, entry, record, total, universe_n,
                                             notes)
    return universe_n, effective_total, notes


def _enforce_completeness(key: str, entry: ScopeEntry, record: Mapping[str, Any],
                          total: int, universe_n: int, notes: list[str]) -> int:
    """Denominator must equal the authoritative committed universe, or a valid
    reconciliation accounts for the shortfall, scored fail-closed over the FULL
    universe (Section 7.4). Carried forward unchanged from v0.6."""
    if total == universe_n:
        notes.append("denominator %d equals the committed universe %d: complete"
                     % (total, universe_n))
        return total
    if total > universe_n:
        raise RouteInputError(
            "%s: denominator %d exceeds the committed universe %d; the evidence "
            "universe cannot be enlarged after commitment"
            % (key, total, universe_n))
    recon = record.get("reconciliation")
    if recon is None:
        raise RouteInputError(
            "%s: denominator %d is below the committed universe %d and no "
            "reconciliation was supplied; a favorable subset is not admissible "
            "evidence" % (key, total, universe_n))
    if not isinstance(recon, Mapping):
        raise RouteInputError("%s: reconciliation must be a mapping" % key)
    stated_n = recon.get("universe_n")
    if not isinstance(stated_n, Integral) or isinstance(stated_n, bool) \
            or int(stated_n) != universe_n:
        raise RouteInputError(
            "%s: reconciliation universe_n must equal the committed universe %d"
            % (key, universe_n))
    excluded = recon.get("excluded")
    if not isinstance(excluded, (list, tuple)) or not excluded:
        raise RouteInputError(
            "%s: reconciliation must list the excluded items with reasons" % key)
    accounted = 0
    for i, item in enumerate(excluded):
        if not isinstance(item, Mapping):
            raise RouteInputError("%s: reconciliation item %d must be a mapping"
                                  % (key, i))
        cnt = item.get("count")
        reason = item.get("reason")
        if not isinstance(cnt, Integral) or isinstance(cnt, bool) or int(cnt) <= 0:
            raise RouteInputError(
                "%s: reconciliation item %d needs a positive integer count"
                % (key, i))
        if not isinstance(reason, str) or not reason.strip():
            raise RouteInputError(
                "%s: reconciliation item %d needs a non-empty reason" % (key, i))
        accounted += int(cnt)
    if accounted != universe_n - total:
        raise RouteInputError(
            "%s: reconciliation accounts for %d excluded items but the committed "
            "universe %d exceeds the denominator %d by %d"
            % (key, accounted, universe_n, total, universe_n - total))
    notes.append("denominator %d reconciled against committed universe %d: %d "
                 "excluded items scored as non-passing over the full universe"
                 % (total, universe_n, accounted))
    return universe_n


@dataclass(frozen=True)
class GateResult:
    key: str
    route: str
    phase: str
    cls: str
    denominator: int
    numerator: int
    violations: int
    share: float | None
    min_items: int
    threshold: float
    evaluable: bool
    gate_pass: bool
    hard_gate_violated: bool
    universe_n: int
    reasons: tuple[str, ...]
    statement: str
    scope_limit: str
    inference: str = ("NONE. Descriptive gate only: no p-value, no null, no "
                      "confidence bound, no significance, no generalization")


def _authoritative_universe_n(key: str, entry: ScopeEntry,
                              commitment: Mapping[str, Any] | None,
                              run_log: Any, commitment_id: str | None) -> int:
    if entry.kind == KIND_FIXED:
        return int(entry.universe_n)  # type: ignore[arg-type]
    if commitment_id is None:
        raise CommitmentError("%s: raw record has no commitment_id" % key)
    if commitment is None:
        raise CommitmentError("%s: commitment_id %r does not resolve in Channel A"
                              % (key, commitment_id))
    if entry.kind == KIND_SEALED:
        return verify_sealed_commitment(key, entry, commitment, commitment_id)
    return verify_realized_commitment(key, entry, commitment, run_log, commitment_id)


def evaluate_gate(key: str, evidence: Mapping[str, Any],
                  commitment: Mapping[str, Any] | None = None,
                  run_log: Any = None) -> GateResult:
    """Evaluate one raw component. All trust roots come only from the manifest."""
    if not isinstance(key, str) or key not in BY_KEY:
        raise RouteInputError("unknown component key %r" % (key,))
    spec = BY_KEY[key]
    entry = MANIFEST_BY_KEY[key]
    if not isinstance(evidence, Mapping):
        raise RouteInputError("%s: raw evidence must be a mapping, got %r"
                              % (key, type(evidence).__name__))
    smuggled = sorted(f for f in _FORBIDDEN_IN_RAW if f in evidence)
    if smuggled:
        raise RouteInputError("%s: authority field(s) %s are forbidden in Channel B"
                              % (key, smuggled))
    required = _required_fields(entry, spec)
    allowed = set(required) | set(_OPTIONAL_FIELDS)
    extra = sorted(set(evidence) - allowed)
    if extra:
        raise RouteInputError("%s: unexpected raw field(s) %s; expected exactly %s "
                              "plus optional %s"
                              % (key, extra, list(required), list(_OPTIONAL_FIELDS)))

    total = _int_field(evidence, spec.denominator_field, key)
    passed = _int_field(evidence, spec.numerator_field, key)
    violations = (_int_field(evidence, spec.violation_field, key)
                  if spec.violation_field else 0)
    if passed > total:
        raise RouteInputError("%s: numerator exceeds denominator" % key)
    if violations > total:
        raise RouteInputError("%s: violation count exceeds denominator" % key)

    commitment_id = None
    if entry.kind in (KIND_SEALED, KIND_REALIZED):
        commitment_id = _str_field(evidence, "commitment_id", key)
    universe_n = _authoritative_universe_n(key, entry, commitment, run_log,
                                           commitment_id)
    _u, total_eff, bind_notes = _check_binding(key, entry, evidence, total, universe_n)

    reasons: list[str] = list(bind_notes)
    hard = bool(spec.violation_field and violations > 0)
    if hard:
        reasons.append("%d zero-tolerance violation(s) recorded in %s: route FAILS"
                       % (violations, spec.violation_field))
    if total_eff == 0:
        reasons.append("no evidence recorded: NOT EVALUABLE")
        return GateResult(key, spec.route, spec.phase, CLASS, 0, passed, violations,
                          None, spec.min_items, spec.threshold, False, False, hard,
                          universe_n, tuple(reasons), spec.statement, spec.scope_limit)
    if total_eff < spec.min_items:
        reasons.append("%s = %d is below frozen minimum %d: NOT EVALUABLE"
                       % (spec.denominator_field, total_eff, spec.min_items))
        return GateResult(key, spec.route, spec.phase, CLASS, total_eff, passed,
                          violations, passed / total_eff, spec.min_items,
                          spec.threshold, False, False, hard, universe_n,
                          tuple(reasons), spec.statement, spec.scope_limit)
    share = passed / total_eff
    meets = share >= spec.threshold
    reasons.append("descriptive share %d/%d = %.6f against threshold %.2f: %s"
                   % (passed, total_eff, share, spec.threshold,
                      "MET" if meets else "NOT MET"))
    return GateResult(key, spec.route, spec.phase, CLASS, total_eff, passed,
                      violations, share, spec.min_items, spec.threshold, True,
                      bool(meets and not hard), hard, universe_n, tuple(reasons),
                      spec.statement, spec.scope_limit)


# ---------------------------------------------------------------- route claims

def route_claims(raw_evidence: Mapping[str, Any],
                 commitments: Mapping[str, Any] | None = None,
                 run_logs: Mapping[str, Any] | None = None) -> dict:
    """Map Channel-B raw evidence to one descriptive label per route.

    Channel-A commitments and run logs are indexed by the exact commitment_id named
    in the raw record. The evaluator has no authority-key parameter.
    """
    if not isinstance(raw_evidence, Mapping):
        raise RouteInputError("raw_evidence must be a mapping")
    commitments = commitments or {}
    run_logs = run_logs or {}
    if not isinstance(commitments, Mapping) or not isinstance(run_logs, Mapping):
        raise RouteInputError("commitments and run_logs must be mappings")
    unknown = sorted(k for k in raw_evidence if k not in BY_KEY)
    if unknown:
        raise RouteInputError("unknown component key(s) %s" % unknown)
    for key, record in raw_evidence.items():
        if isinstance(record, GateResult) or not isinstance(record, Mapping):
            raise RouteInputError("%s: only raw-evidence mappings are admissible"
                                  % key)

    results = {}
    resolved_ids = {}
    for key, record in raw_evidence.items():
        entry = MANIFEST_BY_KEY[key]
        cid = record.get("commitment_id") if entry.kind in (KIND_SEALED, KIND_REALIZED) else None
        commitment = commitments.get(cid) if cid is not None else None
        run_log = run_logs.get(cid) if cid is not None else None
        results[key] = evaluate_gate(key, record, commitment, run_log)
        if cid is not None:
            resolved_ids[key] = cid

    routes: dict[str, dict] = {}
    for route in ROUTES:
        keys = ROUTE_COMPONENTS[route]
        committed_keys = [k for k in keys
                          if MANIFEST_BY_KEY[k].status == STATUS_COMMITTED]
        conditional_keys = [k for k in keys
                            if MANIFEST_BY_KEY[k].status
                            == STATUS_PREDECLARED_CONDITIONAL_OOS]
        present = [k for k in keys if k in results]
        in_scope = committed_keys + [k for k in conditional_keys if k in results]
        missing_committed = [k for k in committed_keys if k not in results]
        excluded_predeclared = [k for k in conditional_keys if k not in results]
        if not in_scope:
            routes[route] = {
                "claim": "OUT OF SCOPE",
                "reason": "every component is a validly predeclared exclusion",
                "components": keys, "ceiling": "SUPPORTED-DESCRIPTIVE",
                "predeclared_out_of_scope": excluded_predeclared,
            }
            continue
        members = [results[k] for k in present]
        violated = [m.key for m in members if m.hard_gate_violated]
        not_eval = [m.key for m in members if not m.evaluable]
        failed = [m.key for m in members if m.evaluable and not m.gate_pass]
        if violated:
            claim, reason = "FAILED", "zero-tolerance violation in %s" % ", ".join(violated)
        elif not_eval:
            claim, reason = "NOT EVALUABLE", "below minimum or zero for %s" % ", ".join(not_eval)
        elif failed:
            claim, reason = "NOT SUPPORTED", "threshold not met by %s" % ", ".join(failed)
        elif missing_committed:
            claim, reason = "INCOMPLETE", "committed evidence absent for %s" % ", ".join(missing_committed)
        else:
            claim, reason = "SUPPORTED-DESCRIPTIVE", "every committed component is present, evaluable and passing"
        routes[route] = {
            "claim": claim, "reason": reason, "components": keys,
            "ceiling": "SUPPORTED-DESCRIPTIVE",
            "predeclared_out_of_scope": excluded_predeclared,
            "missing_committed": missing_committed,
            "statements": [m.statement for m in members] if claim == "SUPPORTED-DESCRIPTIVE" else [],
            "scope_limits": [m.scope_limit for m in members],
        }
    return {
        "manifest_sha256": MANIFEST_SHA256,
        "protocol_version": PROTOCOL_VERSION,
        "release_stage": RELEASE_STAGE,
        "authorities": {
            "commitment_authority_pubkey": COMMITMENT_AUTHORITY_PUBKEY,
            "run_logger_pubkey": RUN_LOGGER_PUBKEY,
            "prerun_anchor_pubkey": PRERUN_ANCHOR_PUBKEY,
        },
        "resolved_commitment_ids": resolved_ids,
        "routes": routes,
        "components": {k: {"denominator": r.denominator, "numerator": r.numerator,
                           "violations": r.violations, "share": r.share,
                           "universe_n": r.universe_n, "evaluable": r.evaluable,
                           "gate_pass": r.gate_pass,
                           "hard_gate_violated": r.hard_gate_violated,
                           "reasons": list(r.reasons)} for k, r in results.items()},
        "family_f3_gate_only": list(FAMILY_F3_GATE_ONLY),
        "inference": "NONE. No p-value, null, confidence bound, FDR, significance, or generalization",
        "withdrawn_since_v0_5": list(WITHDRAWN_LABELS),
    }


def registry_table() -> list[dict]:
    return [{"component": g.key, "route": g.route, "phase": g.phase, "class": CLASS,
             "unit": g.unit, "required_fields": list(_required_fields(
                 MANIFEST_BY_KEY[g.key], g)),
             "denominator": g.denominator_field, "numerator": g.numerator_field,
             "zero_tolerance": g.violation_field or "none",
             "min_items": g.min_items, "threshold": g.threshold,
             "statement": g.statement, "scope_limit": g.scope_limit}
            for g in REGISTRY]


def scope_manifest_table() -> list[dict]:
    return [{"component": e.key, "status": e.status, "kind": e.kind,
             "universe_id": e.universe_id, "universe_n": e.universe_n,
             "authority": e.authority} for e in SCOPE_MANIFEST]


if __name__ == "__main__":
    print("SHVVP v0.8-rc1 route gates: DESCRIPTIVE ONLY. No inference of any kind.")
    print("Frozen scope manifest sha256: %s" % MANIFEST_SHA256)
    print("Frozen commitment authority: %s" % COMMITMENT_AUTHORITY_PUBKEY)
    print("Frozen run logger: %s" % RUN_LOGGER_PUBKEY)
    print("Frozen pre-run anchor: %s" % PRERUN_ANCHOR_PUBKEY)
    print("Sealed/realized universes are authenticated through Channel A only.")
    for row in scope_manifest_table():
        print("  %-5s %-26s %-8s universe_n=%s"
              % (row["component"], row["status"], row["kind"], row["universe_n"]))

---

# Bismillah ir-Rahman ir-Rahim
