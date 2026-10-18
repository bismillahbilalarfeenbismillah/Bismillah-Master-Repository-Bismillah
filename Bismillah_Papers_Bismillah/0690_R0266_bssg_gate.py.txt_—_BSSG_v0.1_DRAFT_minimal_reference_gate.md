# Bismillah ir-Rahman ir-Rahim

# R0266 -- bssg_gate.py.txt — BSSG v0.1 DRAFT minimal reference gate.

**Chronological Index:** 690 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** bssg_gate.py.txt  
**Source Format:** txt  
**SHA-256:** `46938c59018384ff584c54d2fc9fc61425207a782f1dae8ff24afef3f04273f7`  

---

## R0266 · bssg_gate.py.txt — BSSG v0.1 DRAFT minimal reference gate.

- section: V. BSSG & SHVVP Protocols
- source_file: bssg_gate.py.txt
- source_format: txt
- merged_variants: 18 (bssg_gate.py)
- text_sha256: 46938c59018384ff584c54d2fc9fc61425207a782f1dae8ff24afef3f04273f7

#!/usr/bin/env python3
"""
BSSG v0.1 DRAFT minimal reference gate.

Status: DRAFT / NOT CARRIED / NOT PUBLICATION-READY.

Scope and honesty statement (read before using anything here):

  * This module is an ARCHITECTURAL reference. It implements the decision
    semantics and the atomic commit protocol described in
    BSSG_v0_1_CANONICAL_SPEC_DRAFT.pplx.md. It makes NO claim that any
    deployment using it achieves safety, security, harm-reduction, or effectiveness.
  * Signature verification is MODELLED through an injected verifier callable.
    This module does not implement, establish, or audit key custody, key
    distribution, revocation infrastructure, or hardware roots of trust.
    A verifier that returns True does not establish that a key is genuinely
    outside the acting system's authority.
  * This module does not and cannot establish complete mediation. Complete
    mediation is a deployment property (see AX-CM in the spec). Everything
    this code enforces is conditional on the assumption that every
    consequential effect is actually routed through it.
  * Evidence independence is an ASSUMPTION plus a declared WithinAuth
    assessment carried in the witness receipt. It is not derivable from a
    valid signature and this code does not derive it.

Dependencies: Python standard library. jsonschema is used if importable
(for optional structural validation); the gate's own field discipline does
not depend on it.

Author of record: Bilal Syed Arfeen (BayyinahEnterprise).
AI producer: Claude (Anthropic) acting as producer agent in Perplexity Computer.
License recommendation for this file: Apache-2.0 (no LICENSE file is shipped
in this first-draft packet, so no grant is made here).
"""

from __future__ import annotations

import hashlib
import copy
import json
import os
import re
import threading
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple

SPEC_VERSION = "0.1"
GATE_VERSION = "0.1.0-draft"
CANONICALIZATION_ID = "BSSG-CANON-1"

# ---------------------------------------------------------------------------
# Three-valued logic
# ---------------------------------------------------------------------------

TRUE = "TRUE"
FALSE = "FALSE"
UNKNOWN = "UNKNOWN"
TRUTH_VALUES = (TRUE, FALSE, UNKNOWN)

KERNEL_CONJUNCTS = (
    "ContractMatch",
    "EffectTypeValid",
    "TargetAllowed",
    "WitnessHealthy",
    "EvidenceCurrent",
)

# V27-GLM-01 / Kimi-A1/A2: WitnessHealthy reason codes that are DETERMINATELY false WITHOUT reading the
# clock (they compare receipt-internal fields, signatures, identity, and monotonic sequence -- not `now`).
# The abort may recover WitnessHealthy=FALSE only for these; the clock-DEPENDENT witness FALSEs
# (LEASE-EXPIRED, CLOCK-AMBIGUOUS) must stay UNKNOWN under a first-clock fault, never manufactured.
_CLOCK_INDEP_WITNESS_FALSE = frozenset({
    "E-WITNESS-SCHEMA-INVALID", "E-CALLER-SUPPLIED-DERIVED-FIELD", "E-WITNESS-SIGNATURE-INVALID",
    "E-WITNESS-SUBJECT-MISMATCH", "E-WITNESS-EPOCH-ROLLBACK", "E-WITNESS-SEQUENCE-ROLLBACK",
    "E-WITNESS-LEASE-INVERTED", "E-WITNESS-FAILED",
})
# V29 K30-A4: the subset recoverable under a first-clock fault (NO trustworthy clock). E-WITNESS-FAILED is a
# health ASSERTION whose trust requires the receipt to be temporally CURRENT -- a far-future observed_at would
# be clock-ambiguous UNKNOWN under a real clock, so crediting health=FAILED without a clock FABRICATES a FALSE
# the honest (stashed-clock) path reports as UNKNOWN. The rest are PURELY receipt-internal (structural,
# identity, monotonic sequence, receipt-internal lease inversion, signature) and are FALSE regardless of when
# the receipt was observed, so they remain recoverable clock-free.
_RECEIPT_INTERNAL_WITNESS_FALSE = _CLOCK_INDEP_WITNESS_FALSE - frozenset({"E-WITNESS-FAILED"})

DECISION_ALLOW = "ALLOW"
DECISION_DENY_FALSE = "DENY_FALSE"
DECISION_DENY_UNKNOWN = "DENY_UNKNOWN"
DECISION_REJECTED_SCHEMA = "REJECTED_SCHEMA"
DECISION_SESSION_TERMINAL = "SESSION_TERMINAL"

# Field names that a caller MUST NOT supply. These are derived facts. A caller
# that supplies them is trying to hand the gate its own conclusion.
PROHIBITED_DERIVED_FIELDS = frozenset(
    {
        "allow",
        "allowed",
        "decision",
        "authorized",
        "authorization",
        "contract_match",
        "contractmatch",
        "effect_type_valid",
        "effecttypevalid",
        "target_allowed",
        "targetallowed",
        "witness_healthy",
        "witnesshealthy",
        "evidence_current",
        "evidencecurrent",
        "within_auth",
        "withinauth",
        "evidence_independent",
        "trusted",
        "verified",
        "signature_valid",
        "is_valid",
        "conjuncts",
        "commit_token",
        "authority_epoch_override",
        "override",
    }
)

DIGEST_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
NONCE_RE = re.compile(r"^[0-9a-f]{32}$")
IDENTIFIER_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$")
RFC3339_RE = re.compile(
    r"^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})Z$"
)


class BSSGError(Exception):
    """Raised only for programming errors in the caller of this module."""


class TerminalFailure(Exception):
    """Raised when the gate enters a terminal state for a session."""


# ---------------------------------------------------------------------------
# Canonicalization and digests
# ---------------------------------------------------------------------------

MAX_SAFE_INT = 2 ** 53 - 1


_SCHEMA_CACHE: Dict[str, Any] = {}
def _load_schema(name: str) -> Any:
    """Load schemas/<name>.schema.json next to this module (cached). None if unavailable."""
    if name in _SCHEMA_CACHE:
        return _SCHEMA_CACHE[name]
    schema = None
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "schemas", name + ".schema.json"), encoding="utf-8") as fh:
            schema = json.load(fh)
    except Exception:
        schema = None
    _SCHEMA_CACHE[name] = schema
    return schema


SIGNATURE_FIELDS = {"alg", "kid", "envelope", "canonicalization", "signature_b64",
                    "cose_sign1_b64", "verification_status"}

# Every untrusted record gets a schema. The witness/request/amendment have file schemas; the evidence
# bundle and time authority are given equivalent inline schemas so they pass the SAME validator
# (closedness, evidence_epoch bounds, signature envelope/canonicalization) -- no key-set shortcuts.
_SIGNATURE_SCHEMA = {
    "type": "object", "additionalProperties": False,
    "required": ["alg", "kid", "envelope", "canonicalization"],
    "properties": {
        "alg": {"type": "string"}, "kid": {"type": "string"},
        "envelope": {"enum": ["detached-json", "COSE_Sign1", "COSE_Sign"]},
        "canonicalization": {"const": "BSSG-CANON-1"},
        "signature_b64": {"type": "string"}, "cose_sign1_b64": {"type": "string"},
        "verification_status": {"enum": ["verified_by_injected_verifier",
            "rejected_by_injected_verifier", "unknown", "not_performed_by_reference_gate"]},
    },
}
_TIME_AUTHORITY_SCHEMA = {
    "type": "object", "additionalProperties": False,
    "required": ["kind", "anchor_time", "signature"],
    "properties": {
        "kind": {"type": "string"},
        "max_skew_seconds": {"type": "integer", "minimum": 0},
        "anchor_time": {"type": "string"},
        "authority_id": {"type": "string"},
        "signature": {"$ref": "#/$defs/signature"},
    },
    "$defs": {"signature": _SIGNATURE_SCHEMA},
}
_EVIDENCE_BUNDLE_SCHEMA = {
    "type": "object", "additionalProperties": False,
    "properties": {
        "witness_receipt": {"type": "object"},
        "time_authority": {"type": "object"},
        "evidence_epoch": {"type": "integer", "minimum": 0, "maximum": 9007199254740991},
    },
}


_UNRESOLVED_REF = {"$__unresolved_ref__": True}


_UNCOPYABLE_INPUT = ("__bssg_uncopyable_input__",)


class _ClockFault(Exception):
    """Raised by _read_clock when the deployment clock returns anything other than a built-in
    non-negative int. Kept internal; every call site converts it to that site's fail-closed outcome."""


def _strict_json(x: Any) -> Any:
    """Recursively rebuild x using EXACT built-in types only. A subclass of dict/list/str/int/float, a
    tuple, or any custom object is REJECTED (raises), so no hostile __iter__ / items() / __hash__ /
    __eq__ accessor is ever dispatched -- pass-24 P23-01/GLM-01/02/GPT-P21-04. Only exact dict (with
    exact-str keys), exact list, and the exact JSON scalars survive; everything else fails closed."""
    t = type(x)
    if x is None or t is bool or t is int or t is float or t is str:
        return x
    if t is dict:
        out = {}
        for k, v in list(x.items()):   # exact dict.items() is the builtin; safe to call
            if type(k) is not str:
                raise ValueError("non-str key")
            out[k] = _strict_json(v)
        return out
    if t is list:
        return [_strict_json(v) for v in list(x)]   # exact list.__iter__ is the builtin; safe
    raise ValueError("non-exact type: %r" % (t,))


def _strict_copy(x: Any) -> Any:
    """Strict exact-type materialization for HOSTILE-INPUT BOUNDARIES (the two invariant checkers and the
    three projection predicates). FAIL CLOSED: input not built entirely from exact dict/list/str/int/
    float/bool/None -- a dict/list subclass, a hostile accessor, a custom object -- becomes the sentinel.
    Refuses the subclass BEFORE any accessor runs (P23-01), so a hostile __iter__/items()/__hash__ never
    dispatches. Distinct from _safe_copy, which stays lenient for INTERNAL snapshotting (commit/storage)
    where the gate's own already-plain records and legitimate copy-hook timing must be preserved."""
    try:
        return _strict_json(x)
    except Exception:
        return _UNCOPYABLE_INPUT


def _safe_copy(x: Any) -> Any:
    """Snapshot caller-owned input at the API boundary into FRESH built-in JSON objects, so no dict/list
    subclass, custom __deepcopy__ hook, or post-decision mutation can affect evaluation or a stored
    record. FAIL CLOSED (V11-01): an input that will not round-trip into plain JSON becomes a sentinel
    that every structural check rejects -- never the caller's original object. (Lenient json round-trip:
    used for internal snapshotting; the hostile-input boundaries use _strict_copy -- P23-01.)"""
    try:
        return json.loads(json.dumps(x))
    except Exception:
        return _UNCOPYABLE_INPUT


def _resolve_ref(schema: Any, root: Any) -> Any:
    seen = 0
    while isinstance(schema, dict) and "$ref" in schema and seen < 16:
        node = root
        for part in schema["$ref"].lstrip("#/").split("/"):
            if isinstance(node, dict) and part in node:
                node = node[part]
            else:
                return _UNRESOLVED_REF  # fail closed: reference target does not exist
        if not isinstance(node, dict):
            return _UNRESOLVED_REF
        schema = node; seen += 1
    if isinstance(schema, dict) and "$ref" in schema:
        return _UNRESOLVED_REF  # depth overflow / cycle
    return schema


# JSON-Schema keywords the six normative schemas actually use, enumerated from the schemas.
# ENFORCED constraints + IGNORABLE annotations. schema_valid FAILS CLOSED on any keyword outside
# these sets, so an incomplete validator can never silently produce a false ALLOW.
_SCHEMA_ENFORCE = {"type", "properties", "required", "additionalProperties", "items", "$ref",
                   "const", "enum", "minimum", "maximum", "minLength", "maxLength", "pattern",
                   "minItems", "maxItems", "oneOf"}
_SCHEMA_IGNORE = {"$defs", "$id", "$schema", "$comment", "description", "title", "default",
                  "examples", "deprecated", "readOnly"}


def _type_ok(obj: Any, t: Any) -> bool:
    for tt in (t if isinstance(t, list) else [t]):
        if tt == "string" and isinstance(obj, str):
            return True
        if tt == "integer" and isinstance(obj, int) and not isinstance(obj, bool):
            return True
        if tt == "number" and isinstance(obj, (int, float)) and not isinstance(obj, bool):
            return True
        if tt == "boolean" and isinstance(obj, bool):
            return True
        if tt == "array" and isinstance(obj, list):
            return True
        if tt == "object" and isinstance(obj, dict):
            return True
        if tt == "null" and obj is None:
            return True
    return False


def _json_eq(a: Any, b: Any) -> bool:
    """JSON-instance equality: a boolean is a distinct type from a number, so 1 != true, 0 != false."""
    if isinstance(a, bool) != isinstance(b, bool):
        return False
    return a == b


def schema_valid(obj: Any, schema: Any, root: Any) -> bool:
    """Validate obj against a (possibly $ref) schema at EVERY level: closedness, required, const,
    enum, oneOf, type, and the value constraints minimum/maximum/minLength/maxLength/pattern/
    minItems/maxItems. FAILS CLOSED on any schema keyword outside the enforce/ignore vocabulary --
    an unrecognised construct rejects rather than silently passing."""
    schema = _resolve_ref(schema, root)
    if schema is _UNRESOLVED_REF:
        return False  # fail closed on an unresolved $ref
    if not isinstance(schema, dict):
        return True
    for k in schema:  # fail closed on any keyword we do not fully implement
        if k not in _SCHEMA_ENFORCE and k not in _SCHEMA_IGNORE:
            return False
    if "const" in schema and not _json_eq(obj, schema["const"]):
        return False
    if "enum" in schema and not any(_json_eq(obj, e) for e in schema["enum"]):
        return False
    if "oneOf" in schema and sum(1 for sub in schema["oneOf"] if schema_valid(obj, sub, root)) != 1:
        return False
    t = schema.get("type")
    if t is not None and not _type_ok(obj, t):
        return False
    if isinstance(obj, str):
        if "minLength" in schema and len(obj) < schema["minLength"]:
            return False
        if "maxLength" in schema and len(obj) > schema["maxLength"]:
            return False
        if "pattern" in schema and re.fullmatch(schema["pattern"], obj) is None:
            return False
    if isinstance(obj, (int, float)) and not isinstance(obj, bool):
        if "minimum" in schema and obj < schema["minimum"]:
            return False
        if "maximum" in schema and obj > schema["maximum"]:
            return False
    if isinstance(obj, list):
        if "minItems" in schema and len(obj) < schema["minItems"]:
            return False
        if "maxItems" in schema and len(obj) > schema["maxItems"]:
            return False
        it = schema.get("items")
        if it is not None and not all(schema_valid(x, it, root) for x in obj):
            return False
    if isinstance(obj, dict):
        props = schema.get("properties", {})
        if schema.get("additionalProperties") is False and (set(obj) - set(props)):
            return False
        for r in schema.get("required", []):
            if r not in obj:
                return False
        for k, v in obj.items():
            if k in props and not schema_valid(v, props[k], root):
                return False
    return True


def validate_record(record: Any, schema_name: str) -> bool:
    """Uniform ingress check applied at EVERY path: totality (canonicalizable) + $ref-aware
    recursive schema validity. A record that cannot be canonicalized or violates its schema fails."""
    try:
        canonical_bytes(record)
    except Exception:
        return False
    schema = _load_schema(schema_name)
    if schema is None:
        return False  # fail closed: a record we cannot validate is not admitted
    return schema_valid(record, schema, schema)


def schema_closed(obj: Any, schema: Any) -> bool:
    """Recursively verify obj introduces no field outside a closed (additionalProperties:false)
    schema, at EVERY object level. Closedness only -- types/refs are validated elsewhere."""
    if not isinstance(schema, dict):
        return True
    props = schema.get("properties")
    if isinstance(obj, dict) and isinstance(props, dict):
        if schema.get("additionalProperties") is False and (set(obj.keys()) - set(props.keys())):
            return False
        for k, v in obj.items():
            if k in props and not schema_closed(v, props[k]):
                return False
        return True
    if isinstance(obj, list) and isinstance(schema.get("items"), dict):
        return all(schema_closed(x, schema["items"]) for x in obj)
    return True


def canonical_bytes(obj: Any) -> bytes:
    """
    BSSG-CANON-1: deterministic JSON serialization used for all digests.

    Rules: object keys sorted by Unicode code point, no insignificant
    whitespace, UTF-8 output, no NaN or Infinity, integers restricted to the
    I-JSON safe range. This is an RFC 8785 style scheme; it is NOT an RFC 8785
    implementation and MUST NOT be described as one. Interoperability with
    RFC 8785 is an OPEN DECISION (see OPEN_DECISIONS.md, OD-1).
    """
    _reject_unsafe_numbers(obj)
    return json.dumps(
        obj,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")


def _reject_unsafe_numbers(obj: Any) -> None:
    if isinstance(obj, bool):
        return
    if isinstance(obj, int):
        if abs(obj) > MAX_SAFE_INT:
            raise BSSGError("integer outside I-JSON safe range")
        return
    if isinstance(obj, float):
        raise BSSGError("floating point values are not permitted in BSSG records")
    if isinstance(obj, dict):
        for key, value in obj.items():
            if not isinstance(key, str):
                raise BSSGError("non-string object key")
            _reject_unsafe_numbers(value)
        return
    if isinstance(obj, list):
        for value in obj:
            _reject_unsafe_numbers(value)


def digest(obj: Any) -> str:
    return "sha256:" + hashlib.sha256(canonical_bytes(obj)).hexdigest()


def digest_bytes(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


# ---------------------------------------------------------------------------
# Time handling
# ---------------------------------------------------------------------------

_DAYS_BEFORE_MONTH = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)


def parse_rfc3339_utc(value: Any) -> Optional[int]:
    """
    Strict RFC 3339 UTC parser returning POSIX seconds, or None if the value is
    malformed. None means UNKNOWN, never 'now' and never zero.
    """
    if not isinstance(value, str):
        return None
    match = RFC3339_RE.match(value)
    if match is None:
        return None
    year, month, day, hour, minute, second = (int(g) for g in match.groups())
    if not (1 <= month <= 12):
        return None
    if not (0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59):
        return None
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if _is_leap(year):
        days_in_month[1] = 29
    if not (1 <= day <= days_in_month[month - 1]):
        return None
    days = _days_from_civil(year, month, day)
    return days * 86400 + hour * 3600 + minute * 60 + second


def _is_leap(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def _days_from_civil(year: int, month: int, day: int) -> int:
    days = 0
    if year >= 1970:
        for y in range(1970, year):
            days += 366 if _is_leap(y) else 365
    else:
        for y in range(year, 1970):
            days -= 366 if _is_leap(y) else 365
    days += _DAYS_BEFORE_MONTH[month - 1]
    if month > 2 and _is_leap(year):
        days += 1
    return days + (day - 1)


# ---------------------------------------------------------------------------
# Kernel decision function (frozen five-conjunct equation)
# ---------------------------------------------------------------------------


def kernel_decision(values: Dict[str, str]) -> Tuple[str, List[str]]:
    """
    The frozen kernel, evaluated over already-recomputed conjunct values.

        Allow(r) iff ContractMatch(r) and EffectTypeValid(r)
                     and TargetAllowed(r) and WitnessHealthy
                     and EvidenceCurrent

    UNKNOWN is never treated as satisfied. There is no sixth conjunct.
    Commit-time revalidation is a protocol obligation outside this equation.

    Precedence rule: if any conjunct is FALSE the decision is DENY_FALSE;
    otherwise if any conjunct is UNKNOWN the decision is DENY_UNKNOWN. The
    distinction is preserved because collapsing it destroys the attack versus
    outage signal.
    """
    missing = [name for name in KERNEL_CONJUNCTS if name not in values]
    if missing:
        raise BSSGError("kernel evaluated with missing conjuncts: %r" % (missing,))
    extra = [name for name in values if name not in KERNEL_CONJUNCTS]
    if extra:
        raise BSSGError("kernel evaluated with extra conjuncts: %r" % (extra,))
    bad = [n for n, v in values.items() if v not in TRUTH_VALUES]
    if bad:
        raise BSSGError("kernel evaluated with non-three-valued inputs: %r" % (bad,))
    falses = [n for n in KERNEL_CONJUNCTS if values[n] == FALSE]
    unknowns = [n for n in KERNEL_CONJUNCTS if values[n] == UNKNOWN]
    if falses:
        return DECISION_DENY_FALSE, ["E-FALSE-" + n.upper() for n in falses]
    if unknowns:
        return DECISION_DENY_UNKNOWN, ["E-UNKNOWN-" + n.upper() for n in unknowns]
    return DECISION_ALLOW, []


# ---------------------------------------------------------------------------
# Authority lattice
# ---------------------------------------------------------------------------

HEALTH_ORDER = {"FAILED": 0, "UNKNOWN": 0, "DEGRADED": 1, "HEALTHY": 2}


class Authority:
    """A capability ceiling: a set of effect types and a set of target scopes."""

    __slots__ = ("effects", "targets")

    def __init__(self, effects: Iterable[str], targets: Iterable[str]) -> None:
        self.effects = frozenset(effects)
        self.targets = frozenset(targets)

    def __le__(self, other: "Authority") -> bool:
        return self.effects <= other.effects and self.targets <= other.targets

    def __lt__(self, other: "Authority") -> bool:
        return self <= other and (self.effects, self.targets) != (
            other.effects,
            other.targets,
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Authority):
            return NotImplemented
        return self.effects == other.effects and self.targets == other.targets

    def __hash__(self) -> int:
        return hash((self.effects, self.targets))

    def is_empty(self) -> bool:
        return not self.effects or not self.targets

    def as_json(self) -> Dict[str, List[str]]:
        return {
            "effects": sorted(self.effects),
            "target_scopes": sorted(self.targets),
        }

    def __repr__(self) -> str:  # pragma: no cover - debugging aid
        return "Authority(effects=%r, targets=%r)" % (
            sorted(self.effects),
            sorted(self.targets),
        )


def ceiling_for_health(contract: Dict[str, Any], health: str) -> Authority:
    """
    Authority ceiling as a function of witness health. Degradation MUST narrow.
    The ceiling function is part of the contract, not of the code, so that a
    deployment cannot claim conformance with a vacuous ceiling.
    """
    if health == "HEALTHY":
        return Authority(contract["allowed_effects"], contract["allowed_target_scopes"])
    if health == "DEGRADED":
        return Authority(
            contract.get("degraded_effects", []),
            contract.get("degraded_target_scopes", []),
        )
    return Authority([], [])


# ---------------------------------------------------------------------------
# Target canonicalization
# ---------------------------------------------------------------------------

_TARGET_RE = re.compile(r"^(?P<scheme>[a-z][a-z0-9+.-]*)://(?P<rest>[^\s]*)$")


def canonical_target(raw: Any) -> Optional[str]:
    """
    Canonicalize a target URI. Returns None when the target is ambiguous, which
    the caller MUST map to UNKNOWN rather than to a permissive default.

    Refusals: wildcards, relative traversal, percent-encoded separators,
    uppercase scheme or authority mismatch after folding, empty path segments,
    non-string input, embedded credentials, and anything not matching the
    restricted grammar.
    """
    if not isinstance(raw, str) or not raw or len(raw) > 2048:
        return None
    if any(ch.isspace() for ch in raw):
        return None
    if any(ord(ch) < 0x20 or 0x7f <= ord(ch) <= 0x9f for ch in raw):
        # control characters (NUL etc.) can smuggle past segment/traversal refusals; reject them
        return None
    if "*" in raw or "?" in raw or "#" in raw:
        return None
    if "@" in raw:
        return None
    if "\\" in raw:
        # a backslash is a path separator under WHATWG URL parsing; keeping it raw would let a
        # target escape its authorized scope (records/..\admin -> /admin). Refuse it.
        return None
    lowered_scheme = raw.split("://", 1)[0].lower() if "://" in raw else None
    if lowered_scheme is None:
        return None
    normalized = lowered_scheme + "://" + raw.split("://", 1)[1]
    match = _TARGET_RE.match(normalized)
    if match is None:
        return None
    rest = match.group("rest")
    if "%" in rest:
        # percent-encoding is an aliasing surface; declared canonical form only
        return None
    parts = rest.split("/")
    authority = parts[0].lower()
    if not authority:
        return None
    segments = parts[1:]
    trailing_slash = len(segments) >= 1 and segments[-1] == ""
    if trailing_slash:
        segments = segments[:-1]
    out_segments: List[str] = []
    for segment in segments:
        if segment == "" or segment == "." or segment == "..":
            return None
        out_segments.append(segment)
    canonical = match.group("scheme") + "://" + authority
    if out_segments:
        canonical += "/" + "/".join(out_segments)
    if trailing_slash:
        canonical += "/"
    return canonical


def target_within_scope(canonical: str, scopes: Iterable[str]) -> bool:
    for scope in scopes:
        if canonical == scope:
            return True
        if scope.endswith("/") and canonical.startswith(scope):
            return True
    return False


# ---------------------------------------------------------------------------
# Structural checks
# ---------------------------------------------------------------------------

REQUEST_REQUIRED_FIELDS = (
    "record_type",
    "spec_version",
    "request_id",
    "subject_id",
    "session_id",
    "contract_digest",
    "policy_digest",
    "effect_type",
    "target",
    "params_digest",
    "adapter_digest",
    "nonce",
    "sequence",
    "issued_at",
    "expires_at",
)

TARGET_REQUIRED_FIELDS = ("declared_uri", "canonical_uri", "target_class")


def find_prohibited_fields(obj: Any, path: str = "$") -> List[str]:
    found: List[str] = []
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(key, str) and key.lower() in PROHIBITED_DERIVED_FIELDS:
                found.append(path + "." + key)
            found.extend(find_prohibited_fields(value, path + "." + str(key)))
    elif isinstance(obj, list):
        for index, value in enumerate(obj):
            found.extend(find_prohibited_fields(value, "%s[%d]" % (path, index)))
    return found


def structural_check_request(request: Any) -> List[str]:
    """Return a list of reason codes. Empty list means structurally admissible."""
    errors: List[str] = []
    if not isinstance(request, dict):
        return ["E-MALFORMED-REQUEST"]
    prohibited = find_prohibited_fields(request)
    if prohibited:
        errors.append("E-CALLER-SUPPLIED-DERIVED-FIELD")
    missing = [f for f in REQUEST_REQUIRED_FIELDS if f not in request]
    if missing:
        errors.append("E-MISSING-FIELD")
    extra = [k for k in request if k not in REQUEST_REQUIRED_FIELDS]
    if extra:
        errors.append("E-EXTRA-FIELD")
    if request.get("record_type") != "bssg.effect-request":
        errors.append("E-WRONG-RECORD-TYPE")
    if request.get("spec_version") != SPEC_VERSION:
        errors.append("E-SPEC-VERSION")
    for field in ("contract_digest", "policy_digest", "params_digest", "adapter_digest"):
        if not DIGEST_RE.match(str(request.get(field, ""))):
            errors.append("E-MALFORMED-DIGEST")
            break
    if not NONCE_RE.match(str(request.get("nonce", ""))):
        errors.append("E-MALFORMED-NONCE")
    if not IDENTIFIER_RE.match(str(request.get("request_id", ""))):
        errors.append("E-MALFORMED-REQUEST-ID")
    _seq = request.get("sequence")
    if not isinstance(_seq, int) or isinstance(_seq, bool) or _seq < 0:
        errors.append("E-MALFORMED-SEQUENCE")
    for field in ("issued_at", "expires_at"):
        if parse_rfc3339_utc(request.get(field)) is None:
            errors.append("E-MALFORMED-TIMESTAMP")
            break
    target = request.get("target")
    if not isinstance(target, dict):
        errors.append("E-MALFORMED-TARGET")
    else:
        if sorted(target.keys()) != sorted(TARGET_REQUIRED_FIELDS):
            errors.append("E-MALFORMED-TARGET")
    # Totality: a request that cannot be canonicalized (e.g. an integer outside the
    # I-JSON safe range) is rejected here, never carried into digest() downstream.
    try:
        canonical_bytes(request)
    except Exception:
        errors.append("E-NONCANONICAL-REQUEST")
    return sorted(set(errors))


# ---------------------------------------------------------------------------
# The gate
# ---------------------------------------------------------------------------


class GateState:
    def __init__(self) -> None:
        self.authority_epoch: Dict[str, int] = {}
        self.ceiling: Dict[str, Optional[Authority]] = {}
        self.last_health: Dict[str, Optional[str]] = {}
        self.highest_evidence_epoch: Dict[str, int] = {}
        self.highest_witness_epoch: Dict[str, int] = {}
        self.highest_witness_sequence: Dict[str, int] = {}
        self.seen_nonces: set = set()
        self.tokens: Dict[str, Dict[str, Any]] = {}
        self.denied: Dict[str, List[str]] = {}
        self.consumed_corrections: set = set()
        self.terminal: Dict[str, str] = {}
        # B (V28 redesign): the AUTHENTICATED grant ledger. Written ONLY when the runtime genuinely ACCEPTS a
        # LIFT amendment (terminal state confirmed, quorum + domain + non-replay verified). It records the
        # landing epoch and the exact authority the runtime restored (the session's pre-terminal ceiling).
        # V29 WITHDRAWAL (SHUDP Axiom 5): the grant is a caller-supplied input (WithinAuth of its supplier)
        # and cannot discharge a re-widen license offline. The offline checker now reports armed re-widens as
        # X7U (uncertifiable-offline) regardless of whether a grant is present. The grant remains for RUNTIME
        # diagnostics and future online verification; it is INERT for the offline verdict. A forged marker
        # produces no grant entry; under the withdrawal this is moot since no grant changes the offline verdict.
        self.amendment_grants: Dict[str, List[Dict[str, Any]]] = {}   # V29 GPT-P30-02: per-session grant LEDGER
        # B: the session's full (undegraded) contract ceiling, recorded at each authorize, used as the
        # authenticated restore target when an amendment is accepted.
        self.contract_ceiling: Dict[str, Any] = {}
        self.records: List[Dict[str, Any]] = []


class BSSGGate:
    """
    Minimal reference gate.

    Enforced here (claim level: 'enforced by reference gate'):
      - raw-evidence recomputation of all five conjuncts;
      - refusal of caller-supplied derived booleans;
      - UNKNOWN is never satisfied;
      - authority epoch monotonicity and monotone narrowing on degradation;
      - binding of the authorization to request digest, contract digest,
        policy digest, witness-receipt digest, evidence epoch, nonce, expiry;
      - one-time commit tokens with compare-and-swap redemption;
      - commit-time revalidation of epochs and bindings;
      - rejection of replay, rollback, stale evidence, unknown or extra fields,
        malformed timestamps, clock ambiguity beyond declared skew,
        witness-control ambiguity, mismatched digests, target or effect
        widening, and recovery from a terminal state without an independent
        amendment.

    NOT established here: complete mediation, key custody, witness honesty,
    evidence independence as fact, or any effectiveness property.
    """

    def __init__(
        self,
        contract_registry: Dict[str, Dict[str, Any]],
        policy_registry: Dict[str, Dict[str, Any]],
        clock: Callable[[], int],
        signature_verifier: Callable[[str, bytes, Dict[str, Any]], Optional[bool]],
        token_factory: Callable[[], str],
        max_clock_skew_seconds: int = 5,
        evidence_max_age_seconds: int = 300,
        profile: str = "BSSG-M",
    ) -> None:
        self.contracts = contract_registry
        self.policies = policy_registry
        self.clock = clock
        self.verify_signature = signature_verifier
        self.new_token = token_factory
        self._commit_lock = threading.Lock()
        self._lock = threading.RLock()
        self._in_txn = False   # V11-05: reentrancy guard (a nested call from an injected dependency)
        self.max_skew = int(max_clock_skew_seconds)
        self.evidence_max_age = int(evidence_max_age_seconds)
        self.profile = profile
        self.state = GateState()

    # -- helpers ---------------------------------------------------------

    def _authority_fields(self, session: Optional[str]) -> Dict[str, Any]:
        """A (F-BSSG-P17-GPT-03 / GLM-02 / KIMI-3): one canonical authority-history shape on EVERY
        decision record. session_id and authority_snapshot are emitted top-level (not only nested in
        an authorization receipt), so X7 and any offline auditor can read a uniform shape from the
        actual record stream rather than only from synthetic dicts."""
        ceiling = self.state.ceiling.get(session) if isinstance(session, str) else None
        return {
            "session_id": session if isinstance(session, str) else None,
            "authority_epoch": self.state.authority_epoch.get(session, 0) if isinstance(session, str) else 0,
            "authority_snapshot": ceiling.as_json() if ceiling is not None else None,
        }

    def _deny(
        self,
        request: Any,
        conjuncts: Dict[str, str],
        reasons: List[str],
        decision: Optional[str] = None,
        kernel_evaluated: bool = False,
    ) -> Dict[str, Any]:
        if decision is None:
            decision, kernel_reasons = kernel_decision(conjuncts)
            reasons = sorted(set(reasons) | set(kernel_reasons))
        session = (request.get("session_id") if isinstance(request, dict)
                   and isinstance(request.get("session_id"), str) else None)
        record = {
            "record_type": "bssg.decision",
            "spec_version": SPEC_VERSION,
            "gate_version": GATE_VERSION,
            "decision": decision,
            "conjuncts": dict(conjuncts),
            "reason_codes": sorted(set(reasons)),
            "kernel_evaluated": kernel_evaluated,
            "request_digest": self._safe_request_digest(request),
            "authorization_receipt": None,
        }
        record.update(self._authority_fields(session))
        self.state.records.append(copy.deepcopy(record))
        return copy.deepcopy(record)

    def _issuance_failure(
        self, request: Any, conjuncts: Dict[str, str], snapshot: str, reason: str
    ) -> Dict[str, Any]:
        """GPT-04 + E (KIMI-5): post-kernel issuance failure (token-factory collision OR mint fault).
        The recorded decision is the true kernel classification (so recorded_decision ==
        kernel_decision(conjuncts) -- kernel_evaluated=True), the mint failure is a distinct
        FAILED_NO_EFFECT issuance_status with no authorization_receipt, and the snapshot is terminal.
        The surviving authenticated authority epoch and ceiling are recorded (they are NOT rolled back).

        V34 F-GS-1 FIX: a FAILED_NO_EFFECT issuance must not leave the session in a state where
        post-lift re-establishment can grant broader authority than was SUCCESSFULLY demonstrated.
        If contract_ceiling has no entry for this session (first-establish mint fault), write an
        EMPTY Authority -- so _apply_narrowing's _held check will terminalize any re-establishment
        attempt that exceeds nothing. This is the fail-closed default: a session that never
        successfully held any authority cannot re-establish with any authority after a lift."""
        kdecision, _ = kernel_decision(conjuncts)
        session = (request.get("session_id") if isinstance(request, dict)
                   and isinstance(request.get("session_id"), str) else None)
        # F-GS-1: ensure contract_ceiling has an entry (even if empty) so the _held check fires.
        if session is not None and session not in self.state.contract_ceiling:
            self.state.contract_ceiling[session] = Authority([], [])
        record = {
            "record_type": "bssg.decision",
            "spec_version": SPEC_VERSION,
            "gate_version": GATE_VERSION,
            "decision": kdecision,
            "conjuncts": dict(conjuncts),
            "reason_codes": [reason],
            "kernel_evaluated": True,
            "issuance_status": "FAILED_NO_EFFECT",
            "issuance_reason": reason,
            "request_digest": self._safe_request_digest(request),
            "authorization_receipt": None,
        }
        record.update(self._authority_fields(session))
        self.state.denied[snapshot] = [reason]
        self.state.records.append(copy.deepcopy(record))
        return copy.deepcopy(record)

    def _safe_request_digest(self, request: Any) -> Optional[str]:
        try:
            return digest(request)
        except Exception:
            return None

    @staticmethod
    def authorized_issuance(record: Dict[str, Any]) -> bool:
        """Authorization is a POSITIVE property of a completed, provenance-consistent issuance, never an
        inference from the kernel classification alone.

        D (pass-18 K18-01/02/03, GPT-01/02/03): this predicate is TOTAL and materializes its input.
        - Totality: a non-dict or otherwise malformed/hostile input FAILS CLOSED and never raises.
        - Materialization: the record is snapshotted into plain JSON (_safe_copy) before any check, so a
          dict/list subclass with lying accessors or divergent storage cannot make the validated view
          differ from the projected data.
        - Record<->receipt binding: the surrounding record's provenance fields (request_digest,
          session_id, authority_epoch, authority_snapshot, conjuncts) MUST equal the receipt's; a
          genuine receipt transplanted into a wrapper with different top-level provenance does NOT
          project authorized.
        A post-kernel issuance failure (collision / mint fault) is a kernel-consistent ALLOW with
        issuance_status=FAILED_NO_EFFECT and a null receipt; it MUST NOT project authorized on any path.
        Note (scope): a from-scratch, schema-valid receipt whose commit token was never minted still
        satisfies this RECORD-INTERNAL predicate; provenance to real gate state is checked only by the
        instance method authorized_issuance_bound(). Do not apply the static predicate to records of
        unknown provenance."""
        try:
            if not isinstance(record, dict):
                return False
            rec = _strict_copy(record)
            if not isinstance(rec, dict):
                return False
            return BSSGGate._authorized_issuance_snap(rec)
        except Exception:
            return False

    @staticmethod
    def _authorized_issuance_snap(rec: Dict[str, Any]) -> bool:
        """The record-internal authorization predicate over an ALREADY-MATERIALIZED plain snapshot
        (GPT-P21-04). Callers materialize the hostile input EXACTLY ONCE at the projection boundary and
        pass the same snapshot here AND to any binding / response construction, so a dict subclass with
        non-deterministic accessors cannot present one view to the predicate and a different view to the
        token binding or the subject response."""
        try:
            if not isinstance(rec, dict):
                return False
            if rec.get("decision") != DECISION_ALLOW:
                return False
            status = rec.get("issuance_status")
            if status is not None and status != "ISSUED":
                return False

            def _kernel_allows(conj: Any) -> bool:
                if not isinstance(conj, dict) or set(conj.keys()) != set(KERNEL_CONJUNCTS):
                    return False
                try:
                    return kernel_decision(dict(conj))[0] == DECISION_ALLOW
                except Exception:
                    return False

            if not _kernel_allows(rec.get("conjuncts")):
                return False
            receipt = rec.get("authorization_receipt")
            if not isinstance(receipt, dict):
                return False
            if receipt.get("decision") != DECISION_ALLOW:
                return False
            if not validate_record(receipt, "authorization-receipt"):
                return False
            if check_allow_receipt(receipt):
                return False
            if not _kernel_allows(receipt.get("conjuncts")):
                return False
            # D2 (GPT-03 / K18-02): the record must be bound to the receipt on every duplicated field.
            for field in ("request_digest", "session_id", "authority_epoch", "authority_snapshot", "conjuncts"):
                if rec.get(field) != receipt.get(field):
                    return False
            token = receipt.get("commit_token")
            if not isinstance(token, dict):
                return False
            token_id = token.get("token_id")
            return isinstance(token_id, str) and 8 <= len(token_id) <= 128
        except Exception:
            return False

    def authorized_issuance_bound(self, record: Dict[str, Any]) -> bool:
        """D (strongest form): the record-internal check PLUS provenance binding to this gate's state --
        the receipt digest matches a minted token entry that EXISTS, is UNUSED, and is UNEXPIRED at the
        current gate clock. TOTAL: any fault (bad clock, malformed state) fails closed. Runtime effect
        authorization is still ultimately enforced at commit (which independently revalidates and refuses
        unminted / consumed / expired / session-terminal tokens).

        PRECISION (V29, Kimi-A4/GPT-03): this is a POINT-IN-TIME linearization, not a durable guarantee. True
        means the entry was UNUSED/unexpired/non-terminal AT the instant of the locked snapshot; a commit that
        lands AFTER this call returns may still consume the token. The commit lock makes the snapshot atomic
        against a CONCURRENT consume (observed CONSUMED, never raced past) -- it does not freeze the token."""
        try:
            snap = _strict_copy(record)
            if not isinstance(snap, dict) or not BSSGGate._authorized_issuance_snap(snap):
                return False
            receipt = snap.get("authorization_receipt")  # SAME snapshot the predicate validated (GPT-P21-04)
            token_id = receipt.get("commit_token", {}).get("token_id")
            # GPT-P30-04 (MAJOR precision): read the clock INSIDE the commit lock, at the SAME linearization
            # point as the entry snapshot, so the unexpired check is evaluated at the instant of the locked
            # snapshot -- NOT a stale pre-lock time. A token that expires while this predicate is waiting for the
            # lock is then correctly observed expired, making the docstring's "at the instant of the locked
            # snapshot" claim true. (V27-GPT: the lock also makes the entry snapshot atomic against a racing
            # commit's UNUSED->CONSUMED compare-and-swap, so a consumed token is observed CONSUMED here.) A
            # single in-lock read of both time and entry closes the check-to-use window (V26-GPT P4).
            with self._commit_lock:
                try:
                    now = self._read_clock()
                except (KeyboardInterrupt, SystemExit):
                    raise
                except BaseException:
                    return False   # GPT-P30-05: a dependency-originated BaseException from the clock fails closed
                _live = self.state.tokens.get(token_id)
                entry = _strict_copy(_live) if isinstance(_live, dict) else None
            if not isinstance(entry, dict):
                return False
            if entry.get("status") != "UNUSED":
                return False
            if entry.get("receipt_digest") != digest(receipt):
                return False
            exp = entry.get("expires_at")
            if not isinstance(exp, int) or now > exp:
                return False
            return entry.get("session_id") not in self.state.terminal
        except (KeyboardInterrupt, SystemExit):
            raise
        except BaseException:
            return False   # GPT-P30-05: any dependency-originated throwable fails the predicate closed

    @staticmethod
    def subject_facing(record: Dict[str, Any]) -> Dict[str, Any]:
        """OD-11 plane split: the ONLY response a subject may receive.

        It reveals authorization but never the denial regime. DENY_FALSE (an attack signal)
        and DENY_UNKNOWN (an outage signal) and every specific reason code collapse to one
        constant DENIED. The rich record -- decision refinement, per-conjunct values, reason
        codes -- stays on the audit plane (self.state.records), where the statistic and the
        operator live.

        This normalizes response CONTENT only. A conformant deployment MUST also normalize
        response size, timing, retries, queueing, log-flush, transport-close behavior, and
        capability lifetime (the covert-channel inventory); those are deployment obligations
        outside the reference gate and are declared, not enforced here.
        """
        snap = _strict_copy(record)
        if isinstance(snap, dict) and BSSGGate._authorized_issuance_snap(snap):
            return {
                "decision": "AUTHORIZED",
                "authorization_receipt": snap.get("authorization_receipt"),  # SAME validated snapshot
                "reason_codes": [],
            }
        # Everything else -- DENY_FALSE, DENY_UNKNOWN, REJECTED_SCHEMA, SESSION_TERMINAL, and a
        # kernel-ALLOW record whose issuance FAILED_NO_EFFECT -- collapses to the constant DENIED.
        return {"decision": "DENIED", "authorization_receipt": None, "reason_codes": ["E-DENIED"]}

    @staticmethod
    def _unknown_all() -> Dict[str, str]:
        return {name: UNKNOWN for name in KERNEL_CONJUNCTS}

    # -- conjuncts -------------------------------------------------------

    def _contract_structural(
        self, request: Dict[str, Any]
    ) -> Tuple[str, List[str], Optional[Dict[str, Any]]]:
        """Clock-INDEPENDENT contract validation: digest, subject, revocation, policy binding, expiry-field
        presence, capability presence. Returns (value, reasons, cbody). Expiry (the ONLY clock-dependent
        judgement) is deferred to _contract_match. The abort uses this to recover a determinate STRUCTURAL
        FALSE, or to extract the contract body, without a clock and without manufacturing a time-dependent
        expiry FALSE (V27-GPT-04)."""
        contract = self.contracts.get(request["contract_digest"])
        if contract is None:
            return UNKNOWN, ["E-CONTRACT-UNKNOWN"], None
        if not isinstance(contract, dict) or not isinstance(contract.get("body"), dict):
            return UNKNOWN, ["E-CONTRACT-MALFORMED"], None
        body = copy.deepcopy(contract["body"])
        if digest(body) != request["contract_digest"]:
            return FALSE, ["E-CONTRACT-DIGEST-MISMATCH"], None
        if body.get("subject_id") != request["subject_id"]:
            return FALSE, ["E-CONTRACT-SUBJECT-MISMATCH"], None
        if contract.get("revoked") is not False:
            return FALSE, ["E-CONTRACT-REVOKED"], None
        policy = self.policies.get(request["policy_digest"])
        if policy is None:
            return UNKNOWN, ["E-POLICY-UNKNOWN"], None
        if not isinstance(policy, dict) or not isinstance(policy.get("body"), dict):
            return UNKNOWN, ["E-POLICY-MALFORMED"], None
        if digest(policy["body"]) != request["policy_digest"]:
            return FALSE, ["E-POLICY-DIGEST-MISMATCH"], None
        if body.get("policy_digest") != request["policy_digest"]:
            return FALSE, ["E-CONTRACT-POLICY-BINDING-MISMATCH"], None
        if parse_rfc3339_utc(body.get("not_after")) is None:
            return UNKNOWN, ["E-CONTRACT-NO-EXPIRY"], None
        if any(cap not in body for cap in ("allowed_effects", "allowed_target_scopes")):
            return UNKNOWN, ["E-CONTRACT-MALFORMED"], None
        return TRUE, [], body

    def _contract_match(
        self, request: Dict[str, Any], now: int
    ) -> Tuple[str, List[str], Optional[Dict[str, Any]]]:
        sv, sr, body = self._contract_structural(request)
        if sv != TRUE:
            return sv, sr, body
        not_after = parse_rfc3339_utc(body.get("not_after"))
        if now > not_after:
            return FALSE, ["E-CONTRACT-EXPIRED"], None
        return TRUE, [], body


    def _effect_type_valid(
        self, request: Dict[str, Any], contract_body: Optional[Dict[str, Any]]
    ) -> Tuple[str, List[str]]:
        if contract_body is None:
            return UNKNOWN, ["E-EFFECT-NO-CONTRACT"]
        registry = contract_body.get("effect_registry")
        if not isinstance(registry, dict) or not registry:
            return UNKNOWN, ["E-EFFECT-REGISTRY-ABSENT"]
        for _cf in ("allowed_effects", "allowed_target_scopes", "target_classes",
                    "degraded_effects", "degraded_target_scopes"):
            if _cf in contract_body and not isinstance(contract_body[_cf], list):
                return UNKNOWN, ["E-CONTRACT-CAPABILITY-MALFORMED"]
        effect_type = request["effect_type"]
        entry = registry.get(effect_type)
        if entry is None:
            return FALSE, ["E-EFFECT-NOT-REGISTERED"]
        if not isinstance(entry, dict):
            return UNKNOWN, ["E-EFFECT-REGISTRY-MALFORMED"]
        expected_adapter = entry.get("adapter_digest")
        if not DIGEST_RE.match(str(expected_adapter or "")):
            return UNKNOWN, ["E-ADAPTER-DIGEST-ABSENT"]
        if expected_adapter != request["adapter_digest"]:
            return FALSE, ["E-ADAPTER-DIGEST-MISMATCH"]
        if effect_type not in contract_body.get("allowed_effects", []):
            return FALSE, ["E-EFFECT-NOT-ALLOWED"]
        return TRUE, []

    def _target_independent(
        self, request: Dict[str, Any], contract_body: Optional[Dict[str, Any]]
    ) -> Tuple[str, List[str]]:
        """GPT-03: the evidence-INDEPENDENT part of TargetAllowed -- canonical match, target class, and
        contract scope. It needs no ceiling, so it is evaluable even when evidence is malformed. Returns
        FALSE on any determinate violation; UNKNOWN if not yet determinable (no context / not
        canonicalizable) or if the independent checks pass but the ceiling check is still pending."""
        if contract_body is None:
            return UNKNOWN, ["E-TARGET-NO-CONTEXT"]
        target = request["target"]
        canonical = canonical_target(target.get("declared_uri"))
        if canonical is None:
            return UNKNOWN, ["E-TARGET-NOT-CANONICALIZABLE"]
        if target.get("canonical_uri") != canonical:
            return FALSE, ["E-TARGET-CANONICAL-MISMATCH"]
        if target.get("target_class") not in contract_body.get("target_classes", []):
            return FALSE, ["E-TARGET-CLASS-NOT-ALLOWED"]
        if not target_within_scope(canonical, contract_body["allowed_target_scopes"]):
            return FALSE, ["E-TARGET-OUT-OF-CONTRACT"]
        return UNKNOWN, []

    def _evidence_independent(
        self, request: Dict[str, Any], now: int
    ) -> Tuple[str, List[str]]:
        """C7 (F-BSSG-P15-GPT-02 / KIMI-3): the evidence-INDEPENDENT part of EvidenceCurrent -- request
        expiry and staleness. These are knowable from the admitted request timestamps and the gate's
        own clock alone, needing NO evidence bundle, so a determinate FALSE here MUST dominate even on
        the malformed-evidence path (symmetry with _target_independent). The evidence-DEPENDENT part
        (time-authority skew, epoch rollback, from-the-future within skew) stays UNKNOWN when the
        bundle is malformed. Returns FALSE on a determinate violation, UNKNOWN otherwise."""
        issued_at = parse_rfc3339_utc(request.get("issued_at"))
        expires_at = parse_rfc3339_utc(request.get("expires_at"))
        if issued_at is None or expires_at is None:
            return UNKNOWN, ["E-REQUEST-TIMESTAMP-MALFORMED"]
        # GPT-01 (pass-18): a temporally INVERTED interval (issued after it expires) is logically
        # impossible and knowable from the request alone -- a determinate FALSE that dominates on every
        # path, so it can never yield an ALLOW with an all-TRUE EvidenceCurrent.
        if issued_at > expires_at:
            return FALSE, ["E-REQUEST-INTERVAL-INVERTED"]
        if now > expires_at:
            return FALSE, ["E-REQUEST-EXPIRED"]
        if now - issued_at > self.evidence_max_age:
            return FALSE, ["E-EVIDENCE-STALE"]
        return UNKNOWN, []

    def _target_allowed(
        self,
        request: Dict[str, Any],
        contract_body: Optional[Dict[str, Any]],
        ceiling: Optional[Authority],
    ) -> Tuple[str, List[str]]:
        indep_value, indep_reasons = self._target_independent(request, contract_body)
        if indep_value == FALSE:
            return FALSE, indep_reasons
        if contract_body is None or ceiling is None:
            return UNKNOWN, ["E-TARGET-NO-CONTEXT"]
        canonical = canonical_target(request["target"].get("declared_uri"))
        if canonical is None:
            return UNKNOWN, ["E-TARGET-NOT-CANONICALIZABLE"]
        if request["effect_type"] not in ceiling.effects:
            return FALSE, ["E-EFFECT-ABOVE-CEILING"]
        if not target_within_scope(canonical, ceiling.targets):
            return FALSE, ["E-TARGET-ABOVE-CEILING"]
        return TRUE, []

    def _witness_healthy(
        self, request: Dict[str, Any], evidence: Dict[str, Any], now: int,
        clock_free: bool = False,
    ) -> Tuple[str, List[str], Optional[str], Optional[Dict[str, Any]]]:
        receipt = evidence.get("witness_receipt")
        if not isinstance(receipt, dict):
            return UNKNOWN, ["E-WITNESS-ABSENT"], None, None
        if find_prohibited_fields(receipt):
            return FALSE, ["E-CALLER-SUPPLIED-DERIVED-FIELD"], None, None
        if receipt.get("record_type") != "bssg.witness-receipt":
            return UNKNOWN, ["E-WITNESS-WRONG-RECORD-TYPE"], None, None
        _wschema = _load_schema("witness-receipt")
        if _wschema is None or not schema_valid(receipt, _wschema, _wschema):
            # Fail closed: a witness that cannot be validated -- schema missing, or schema-invalid at
            # ANY depth ($ref-resolved) -- is not healthy.
            return FALSE, ["E-WITNESS-SCHEMA-INVALID"], None, None
        signature = receipt.get("signature")
        if not clock_free:
            if not isinstance(signature, dict):
                return UNKNOWN, ["E-WITNESS-NO-SIGNATURE"], None, None
            payload = {k: v for k, v in receipt.items() if k != "signature"}
            verdict = self.verify_signature("witness", canonical_bytes(payload), signature)
            if verdict is None:
                return UNKNOWN, ["E-WITNESS-SIGNATURE-UNKNOWN"], None, None
            if verdict is not True:
                # V11-04: any non-Boolean verifier result (e.g. integer 0) is NOT a valid signature.
                return FALSE, ["E-WITNESS-SIGNATURE-INVALID"], None, None
        else:
            # V29 GPT-P30-03 (abort must not MASK a determinate FALSE): in clock-free abort recovery, attempt
            # signature verification but do NOT let a RAISING or absent/unknown verifier abort the whole
            # evaluation -- that masked determinate NON-signature FALSEs (subject mismatch, rollback, lease
            # inversion, health=FAILED) to UNKNOWN when the injected witness verifier raised. A determinate
            # signature-INVALID is still recovered; a raising/None/absent verifier simply falls through to the
            # receipt-internal determinate checks below (signature validity stays unasserted, never fabricated).
            if isinstance(signature, dict):
                try:
                    payload = {k: v for k, v in receipt.items() if k != "signature"}
                    _vd = self.verify_signature("witness", canonical_bytes(payload), signature)
                    if _vd is not True and _vd is not None:
                        return FALSE, ["E-WITNESS-SIGNATURE-INVALID"], None, None
                except (KeyboardInterrupt, SystemExit):
                    raise
                except BaseException:
                    pass
        declaration = receipt.get("independence_declaration")
        if not isinstance(declaration, dict):
            return UNKNOWN, ["E-WITNESS-CONTROL-AMBIGUOUS"], None, None
        if declaration.get("subject_can_administer") is not False:
            # 'unknown' or True both fail; only an explicit False is admissible
            return UNKNOWN, ["E-WITNESS-CONTROL-AMBIGUOUS"], None, None
        if declaration.get("control_domain") == receipt.get("covered_subject_domain"):
            return UNKNOWN, ["E-WITNESS-CONTROL-AMBIGUOUS"], None, None
        if receipt.get("covered_subject") != request["subject_id"]:
            return FALSE, ["E-WITNESS-SUBJECT-MISMATCH"], None, None
        witness_id = receipt.get("witness_id")
        if not isinstance(witness_id, str) or not witness_id:
            return UNKNOWN, ["E-WITNESS-ID-ABSENT"], None, None
        epoch = receipt.get("epoch")
        sequence = receipt.get("sequence")
        if not isinstance(epoch, int) or isinstance(epoch, bool):
            return UNKNOWN, ["E-WITNESS-EPOCH-MALFORMED"], None, None
        if not isinstance(sequence, int) or isinstance(sequence, bool):
            return UNKNOWN, ["E-WITNESS-SEQUENCE-MALFORMED"], None, None
        prior_epoch = self.state.highest_witness_epoch.get(witness_id, -1)
        if epoch < prior_epoch:
            return FALSE, ["E-WITNESS-EPOCH-ROLLBACK"], None, None
        prior_sequence = self.state.highest_witness_sequence.get((witness_id, epoch), -1)
        if sequence < prior_sequence:
            return FALSE, ["E-WITNESS-SEQUENCE-ROLLBACK"], None, None
        observed_at = parse_rfc3339_utc(receipt.get("observed_at"))
        expires_at = parse_rfc3339_utc(receipt.get("expires_at"))
        if observed_at is None or expires_at is None:
            return UNKNOWN, ["E-WITNESS-TIMESTAMP-MALFORMED"], None, None
        # GPT-01 (pass-18): a witness lease observed AFTER it expires is a temporally inverted, invalid
        # lease -- a determinate FALSE, not a healthy witness. (Receipt-internal: observed_at vs expires_at,
        # no external clock -- so it is recoverable in clock_free abort recovery.)
        if observed_at > expires_at:
            return FALSE, ["E-WITNESS-LEASE-INVERTED"], None, None
        if not clock_free:
            # V29 K30-A4: the two clock-RELATIVE checks (skew, lease-expired) compare against `now`. In
            # clock_free abort recovery there is no trustworthy clock, so they are SKIPPED entirely rather than
            # evaluated against an attacker-influenceable sentinel (pass-30 used the receipt's OWN observed_at
            # as the sentinel, which let a far-future observed_at + health=FAILED neutralise skew and FABRICATE
            # a determinate FALSE where the honest verdict is clock-ambiguous UNKNOWN). LEASE-EXPIRED and
            # CLOCK-AMBIGUOUS stay UNKNOWN under a clock fault, never manufactured.
            if observed_at > now + self.max_skew:
                return UNKNOWN, ["E-WITNESS-CLOCK-AMBIGUOUS"], None, None
            if now > expires_at:
                return FALSE, ["E-WITNESS-LEASE-EXPIRED"], None, None
        health = receipt.get("health")
        if health not in HEALTH_ORDER:
            return UNKNOWN, ["E-WITNESS-HEALTH-MALFORMED"], None, None
        if health == "UNKNOWN":
            return UNKNOWN, ["E-WITNESS-HEALTH-UNKNOWN"], health, receipt
        if health == "FAILED":
            return FALSE, ["E-WITNESS-FAILED"], health, receipt
        assessment = receipt.get("within_auth_assessment")
        if not isinstance(assessment, dict) or assessment.get("value") not in (
            "outside_subject_authority",
            "within_subject_authority",
            "unknown",
        ):
            return UNKNOWN, ["E-WITHINAUTH-MALFORMED"], health, receipt
        if assessment.get("value") != "outside_subject_authority":
            # WithinAuth is an assessment, not a derivation from the signature.
            return UNKNOWN, ["E-WITHINAUTH-NOT-ESTABLISHED"], health, receipt
        required_class = request.get("target", {}).get("target_class")
        covered = receipt.get("covered_effect_classes")
        if not isinstance(covered, list):
            return UNKNOWN, ["E-WITNESS-COVERAGE-UNKNOWN"], health, receipt
        if required_class not in covered:
            return FALSE, ["E-WITNESS-COVERAGE-MISMATCH"], health, receipt
        return TRUE, [], health, receipt

    def _evidence_current(
        self, request: Dict[str, Any], evidence: Dict[str, Any], now: int
    ) -> Tuple[str, List[str], Optional[int]]:
        # G (F-BSSG-P17-KIMI-1): request expiry and staleness are knowable from the request timestamps
        # and the gate clock WITHOUT any evidence, so a determinate FALSE dominates on EVERY path --
        # including a schema-valid-but-indeterminate bundle (e.g. time authority absent), not only the
        # malformed path. Without this, an expired request with a valid-but-time-authority-absent bundle
        # was DENY_UNKNOWN while the same request with valid evidence was DENY_FALSE (order dependence).
        ind_value, ind_reasons = self._evidence_independent(request, now)
        if ind_value == FALSE:
            return FALSE, ind_reasons, None
        authority = evidence.get("time_authority")
        if not isinstance(authority, dict):
            return UNKNOWN, ["E-TIME-AUTHORITY-ABSENT"], None
        if authority.get("kind") not in (
            "external_signed_anchor",
            "trusted_timestamp",
            "epoch_id",
        ):
            return UNKNOWN, ["E-TIME-AUTHORITY-UNDECLARED"], None
        declared_skew = authority.get("max_skew_seconds")
        if not isinstance(declared_skew, int) or isinstance(declared_skew, bool):
            return UNKNOWN, ["E-TIME-SKEW-UNDECLARED"], None
        anchor_time = parse_rfc3339_utc(authority.get("anchor_time"))
        if anchor_time is None:
            return UNKNOWN, ["E-TIME-ANCHOR-MALFORMED"], None
        signature = authority.get("signature")
        if not isinstance(signature, dict):
            return UNKNOWN, ["E-TIME-ANCHOR-UNSIGNED"], None
        payload = {k: v for k, v in authority.items() if k != "signature"}
        verdict = self.verify_signature("time", canonical_bytes(payload), signature)
        if verdict is None:
            return UNKNOWN, ["E-TIME-ANCHOR-SIGNATURE-UNKNOWN"], None
        if verdict is not True:
            # V11-04: any non-Boolean verifier result (e.g. integer 0) is NOT a valid signature.
            return FALSE, ["E-TIME-ANCHOR-SIGNATURE-INVALID"], None
        if abs(anchor_time - now) > declared_skew:
            return UNKNOWN, ["E-CLOCK-AMBIGUOUS"], None
        epoch = evidence.get("evidence_epoch")
        if not isinstance(epoch, int) or isinstance(epoch, bool):
            return UNKNOWN, ["E-EVIDENCE-EPOCH-MALFORMED"], None
        if epoch < self.state.highest_evidence_epoch.get(request["session_id"], -1):
            return FALSE, ["E-EVIDENCE-EPOCH-ROLLBACK"], None
        issued_at = parse_rfc3339_utc(request["issued_at"])
        expires_at = parse_rfc3339_utc(request["expires_at"])
        if issued_at is None or expires_at is None:
            return UNKNOWN, ["E-REQUEST-TIMESTAMP-MALFORMED"], None
        if issued_at > now + declared_skew:
            return UNKNOWN, ["E-REQUEST-FROM-THE-FUTURE"], None
        if now > expires_at:
            return FALSE, ["E-REQUEST-EXPIRED"], None
        if now - issued_at > self.evidence_max_age:
            return FALSE, ["E-EVIDENCE-STALE"], None
        return TRUE, [], epoch

    # -- public API ------------------------------------------------------

    def _read_clock(self) -> int:
        """Single strict clock reader (retires the pass-19 clock coercion/asymmetry shape: GPT-P19-03,
        GLM-01/04). The deployment clock MUST return a built-in non-negative int. A bool (int subclass),
        float, string, negative value, other int subclass, or a raising clock is a uniform _ClockFault,
        so NO path -- authorize, commit, authorized_issuance_bound, or _execution_failure -- can silently
        coerce a bad value into a decision or a commit time. Callers convert the fault to their own
        fail-closed outcome (DENY_UNKNOWN / E-COMMIT-ABORTED / False / null commit-time)."""
        v = self.clock()
        if type(v) is not int or v < 0 or v > 253402300799:  # reject negative and beyond year 9999
            raise _ClockFault("clock returned %r" % (v,))
        return v

    def authorize(self, request: Any, evidence: Any) -> Dict[str, Any]:
        # Concurrency (class fix): serialize every state transition through one gate lock, so
        # nonce dedup, commit, and amendment are atomic. Distributed atomicity is a deployment
        # obligation (BSSG-H); the reference gate demonstrates the invariant under serialization.
        with self._lock:
            if self._in_txn:  # V11-05: refuse a reentrant call (stale-snapshot authorization)
                # C4: a pre-admission reentrant refusal terminalizes NOTHING (snapshot=None); it must
                # not read the outer invocation's _cur_snapshot and mark that outer snapshot denied.
                return self._authorize_abort(None, "E-REENTRANT-CALL", snapshot=None, conjuncts=None)
            self._in_txn = True
            self._cur_snapshot = None
            self._cur_conjuncts = None
            self._cur_now = None
            # V32 GPT-AUDIT-34-03 / GLM-P34-04: clear stale pending from any prior invocation.
            # Defense-in-depth: the ALLOW path re-sets this at L1733 before consuming, so a stale
            # value from a prior DENY is overwritten before it could matter -- but clearing here
            # removes the reliance on that non-local invariant.
            self._contract_ceiling_pending = None
            try:
                # P12-03: snapshot INSIDE the guard, so a caller copy-hook fired by json.dumps hits the
                # reentrancy guard rather than executing a nested operation before it exists.
                request = _safe_copy(request)
                evidence = _safe_copy(evidence)
                return self._authorize_locked(request, evidence)
            except (KeyboardInterrupt, SystemExit):
                # process-control signals are NEVER swallowed into a DENY -- they propagate.
                raise
            except BaseException:
                # V29 (7th-round finding): the fail-closed boundary catches BaseException, not only Exception,
                # so a misbehaving/hostile injected clock (or any dependency) that raises a non-Exception
                # BaseException on a clock read fails CLOSED to a determinate abort rather than escaping the
                # gate uncaught. KeyboardInterrupt/SystemExit are re-raised above and are out of this scope.
                # GPT-02: do NOT rewind authority/epoch state -- an authenticated monotonic advance or
                # narrowing already established is a security fact that must survive a later token-mint
                # failure and continue to invalidate older grants. Only issuance is incomplete, and it
                # committed nothing. C4: terminalize THIS invocation's own snapshot, passed explicitly.
                # V25/V26 FALSE-domination (order-independent). _cur_conjuncts is the LIVE partial evaluation,
                # so any conjunct already computed FALSE before the raise (e.g. EffectTypeValid on an
                # out-of-contract effect) is preserved. V26-Kimi (K27-K-1): the pass-27 abort only recovered
                # EvidenceCurrent -- a determinate FALSE on ANY evidence-INDEPENDENT conjunct that had not yet
                # been reached was masked to DENY_UNKNOWN. We therefore re-evaluate every evidence-independent
                # conjunct in isolation (ContractMatch, EffectTypeValid, TargetAllowed's independent FALSEs,
                # and evidence-currency/expiry) and record any FALSE. V26-GPT (P3): expiry is re-derived from
                # the STASHED first clock read (_cur_now), never a fresh _read_clock() that could itself fail
                # and re-mask an already-proven expiry. Conjuncts that genuinely depend on the raised component
                # (a witness fault leaves WitnessHealthy / health-derived TargetAllowed indeterminate) stay
                # UNKNOWN -- that is correct, not a mask.
                # V27 (GPT-02 / GLM-01 / Kimi-A1/A2 / GPT-04): the abort recovers determinate evidence-
                # INDEPENDENT FALSEs, but ONLY from immutable per-invocation context -- the captured contract
                # body (_cur_cbody), the request, and the immutable evidence bundle -- NEVER by re-reading a
                # registry a failing evaluator could have mutated, and NEVER with a synthetic clock that would
                # manufacture a time-dependent FALSE. Clock-DEPENDENT judgements (contract/witness expiry,
                # evidence currency) stay UNKNOWN unless a real STASHED clock read is available.
                _ab_conj = getattr(self, "_cur_conjuncts", None)
                _ab_conj = dict(_ab_conj) if isinstance(_ab_conj, dict) else {name: UNKNOWN for name in KERNEL_CONJUNCTS}
                _ab_now = getattr(self, "_cur_now", None)
                _now_ok = isinstance(_ab_now, int) and not isinstance(_ab_now, bool)
                _ev = getattr(self, "_cur_evidence", None)
                if isinstance(request, dict):
                    # Immutable contract body. Prefer the capture taken before any evaluator ran. If absent
                    # (a fault BEFORE ContractMatch, e.g. a first-clock fault), no evaluator has run, so the
                    # registry is unmutated and a clock-INDEPENDENT structural read is sound; use it only to
                    # obtain the body and any STRUCTURAL ContractMatch FALSE (never expiry).
                    _cb = getattr(self, "_cur_cbody", None)
                    if _cb is None and _ab_conj.get("ContractMatch") != FALSE:
                        try:
                            _sv, _sr, _sbody = self._contract_structural(request)
                            _cb = _sbody
                            if _sv == FALSE:
                                _ab_conj["ContractMatch"] = FALSE
                        except (KeyboardInterrupt, SystemExit):
                            raise
                        except BaseException:
                            pass   # best-effort structural read; a fault leaves ContractMatch UNKNOWN (fail closed)
                    # EffectTypeValid + TargetAllowed's evidence-independent FALSE, from the immutable body.
                    if isinstance(_cb, dict):
                        for _name, _fn in (
                            ("EffectTypeValid", lambda: self._effect_type_valid(request, _cb)[0]),
                            ("TargetAllowed", lambda: self._target_independent(request, _cb)[0]),
                        ):
                            if _ab_conj.get(_name) != FALSE:
                                try:
                                    if _fn() == FALSE:
                                        _ab_conj[_name] = FALSE
                                except (KeyboardInterrupt, SystemExit):
                                    raise
                                except BaseException:
                                    pass
                    # WitnessHealthy clock-INDEPENDENT determinate FALSE, from the immutable evidence bundle,
                    # evaluated in clock_free mode: no external/attacker clock sentinel (K30-A4) and a raising
                    # or absent witness verifier no longer masks a determinate NON-signature FALSE (GPT-P30-03).
                    # A FALSE is recorded only when its reason is genuinely clock- AND verifier-independent.
                    if _ab_conj.get("WitnessHealthy") != FALSE and isinstance(_ev, dict):
                        try:
                            _wv, _wr, _, _ = self._witness_healthy(request, _ev, 0, clock_free=True)
                            if _wv == FALSE and any(rc in _RECEIPT_INTERNAL_WITNESS_FALSE for rc in _wr):
                                _ab_conj["WitnessHealthy"] = FALSE
                        except (KeyboardInterrupt, SystemExit):
                            raise
                        except BaseException:
                            pass
                    # EvidenceCurrent (expiry): recovered ONLY with a proven stashed clock.
                    if _now_ok and _ab_conj.get("EvidenceCurrent") != FALSE:
                        try:
                            if self._evidence_independent(request, _ab_now)[0] == FALSE:
                                _ab_conj["EvidenceCurrent"] = FALSE
                        except (KeyboardInterrupt, SystemExit):
                            raise
                        except BaseException:
                            pass
                return self._authorize_abort(
                    request if isinstance(request, dict) else None,
                    snapshot=getattr(self, "_cur_snapshot", None),
                    conjuncts=_ab_conj)
            finally:
                self._in_txn = False
                # C4: clear ambient per-invocation context so no completed call's snapshot lingers to be
                # read by a later abort. The except handler above has already consumed it.
                self._cur_snapshot = None
                self._cur_conjuncts = None
                self._cur_cbody = None
                self._cur_evidence = None
                self._cur_now = None

    # GLM-06: the _snapshot_txn_state / _restore_txn_state rollback helpers were removed in repair17.
    # They were unreachable after the GPT-02 (V14) repair established that an authenticated,
    # security-monotonic authority/epoch advance MUST survive a later token-mint abort (rolling it
    # back could revive an older, wider grant). No abort path restores authority/epoch state.

    def _authorize_abort(self, request: Any, reason: str = "E-AUTHORIZE-ABORTED",
                         snapshot: Optional[str] = None,
                         conjuncts: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """Totality: an evaluator/factory exception (or a reentrant call) becomes a recorded, TERMINAL
        decision. The abort does NOT roll back the nonce -- rolling it back could erase a nonce consumed
        by an earlier COMPLETED authorization, letting the identical request replay and mint a second
        token. A well-formed submission consumes its nonce; a transient fault is retried as a fresh
        request (fresh nonce), a distinct snapshot.

        C4 (GPT-03/GLM-04): both the snapshot AND the conjuncts are passed EXPLICITLY per invocation and
        are NEVER read from instance-wide ambient attributes. A pre-admission reentrant refusal passes
        snapshot=None and conjuncts=None: it admitted no request, evaluated nothing, and consumed no
        nonce, so it terminalizes NOTHING and records all-UNKNOWN conjuncts.

        E (KIMI-5): every abort record is kernel-consistent (decision == kernel_decision(conjuncts),
        kernel_evaluated=True). A POST-admission abort (conjuncts known -- e.g. all TRUE at the mint
        point) is an issuance failure: decision = kernel_decision(conjuncts) with a FAILED_NO_EFFECT
        issuance_status and the surviving authority state preserved. A PRE-admission abort (conjuncts
        None) records all-UNKNOWN, whose kernel_decision is DENY_UNKNOWN -- also consistent."""
        try:
            _rd = digest(request) if isinstance(request, dict) else None
        except Exception:
            _rd = None
        session = (request.get("session_id") if isinstance(request, dict)
                   and isinstance(request.get("session_id"), str) else None)
        cj = dict(conjuncts) if conjuncts is not None else {n: UNKNOWN for n in KERNEL_CONJUNCTS}
        kdecision, _ = kernel_decision(cj)
        post_admission = conjuncts is not None
        rec = {
            "record_type": "bssg.decision",
            "spec_version": SPEC_VERSION,
            "gate_version": GATE_VERSION,
            "decision": kdecision,
            "conjuncts": cj,
            "reason_codes": [reason],
            # F/GPT-06 (pass-18): a PRE-admission abort (reentrant refusal / pre-conjunct fault) evaluated
            # no conjuncts -- it is a protocol/admission refusal, classified kernel_evaluated=False (and
            # exempt from the kernel-equality claim, though all-UNKNOWN -> DENY_UNKNOWN is consistent
            # anyway). A POST-admission abort IS a kernel-consistent issuance failure -> True.
            "kernel_evaluated": bool(post_admission),
            "request_digest": _rd,
            "authorization_receipt": None,
        }
        if post_admission:
            # an authorizable request whose issuance could not complete: mark it like a collision.
            rec["issuance_status"] = "FAILED_NO_EFFECT"
            rec["issuance_reason"] = reason
        rec.update(self._authority_fields(session))
        # terminal for ITS OWN snapshot only (nonce already consumed); a reentrant refusal (snapshot=None)
        # terminalizes nothing.
        if snapshot is not None:
            self.state.denied[snapshot] = [reason]
        self.state.records.append(copy.deepcopy(rec))
        return copy.deepcopy(rec)

    def _authorize_locked(self, request: Any, evidence: Any) -> Dict[str, Any]:
        """
        Recompute all five conjuncts from raw evidence and, on ALLOW, issue an
        authorization receipt carrying a one-time commit token.

        The caller's own beliefs are never inputs. Any derived field supplied
        by the caller is a hard structural rejection.
        """
        # GPT-01: no fallible evaluator (the clock) runs before structural admission + nonce
        # consumption, so a post-admission abort always has a consumed nonce and a snapshot to
        # terminalize. _cur_snapshot carries that context into the abort handler.
        conjuncts = self._unknown_all()
        self._cur_conjuncts = conjuncts   # V26-Kimi (K27-K-1): live reference, so any conjunct computed
        #                                   FALSE before a later raise is visible to the abort path.
        self._cur_snapshot = None
        self._cur_cbody = None            # V27-GPT-02: immutable contract-body capture for the abort
        self._cur_evidence = None

        # Step 1 (spec S12): structural admission, total. Runs before anything that
        # canonicalizes the request, so a non-canonicalizable request cannot crash the gate.
        structural = structural_check_request(request)
        if structural:
            # Spec S12/S14.1: structural admission failure is a distinct terminal state,
            # not a kernel-level DENY_UNKNOWN.
            return self._deny(request, conjuncts, structural, decision=DECISION_REJECTED_SCHEMA)
        if not validate_record(request, "effect-request"):
            # The request itself passes the SAME uniform, fail-closed validator as every other record.
            return self._deny(request, conjuncts, ["E-REQUEST-SCHEMA-INVALID"], decision=DECISION_REJECTED_SCHEMA)

        # The request is now canonicalizable; its snapshot digest can be taken once.
        snapshot = digest(request)
        self._cur_snapshot = snapshot  # GPT-01: a post-admission abort terminalizes this snapshot

        session = request["session_id"]
        if session in self.state.terminal:
            return self._deny(
                request,
                {name: FALSE for name in KERNEL_CONJUNCTS},
                ["E-SESSION-TERMINAL", self.state.terminal[session]],
                decision=DECISION_SESSION_TERMINAL,
            )

        if snapshot in self.state.denied:
            return self._deny(
                request,
                {name: FALSE for name in KERNEL_CONJUNCTS},
                ["E-REQUEST-DENIED-TERMINAL"],
            )

        # P7-04/DP-02: consume the nonce for every well-formed, non-terminal submission BEFORE the
        # evidence-dependent denials, so a request denied on an early evidence path still burns its
        # nonce and a linked retry cannot reuse it. SESSION_TERMINAL (above) deliberately does NOT
        # consume, preserving post-amendment recovery of the same request.
        if request["nonce"] in self.state.seen_nonces:
            return self._deny(request, conjuncts, ["E-NONCE-REPLAY"], decision=DECISION_DENY_FALSE)
        self.state.seen_nonces.add(request["nonce"])

        # V27-GLM-01/Kimi-A1: capture the immutable evidence bundle BEFORE the fallible clock read, so a
        # first-clock fault (which aborts before ContractMatch) can still recover a clock-INDEPENDENT witness
        # FALSE from the receipt.
        self._cur_evidence = evidence
        # GPT-01: the clock (a fallible evaluator) is read only now, AFTER the nonce is consumed and the
        # snapshot recorded, so a transient clock fault aborts to a TERMINAL DENY_UNKNOWN, not a
        # replayable pre-admission no-op.
        now = self._read_clock()  # strict; _ClockFault -> outer abort -> DENY_UNKNOWN
        self._cur_now = now        # V26-GPT (P3): the abort path reuses THIS proven read, never a fresh one

        # GPT-02 (FALSE domination / order independence): evidence-independent conjuncts are evaluated
        # even when evidence is malformed, so a determinate FALSE there yields DENY_FALSE rather than a
        # suppressed DENY_UNKNOWN. The evidence-dependent conjuncts remain UNKNOWN.
        def _evidence_indeterminate(malf_reason):
            cmv, cmr, cbody = self._contract_match(request, now)
            conjuncts["ContractMatch"] = cmv
            etv, etr = self._effect_type_valid(request, cbody)
            conjuncts["EffectTypeValid"] = etv
            tav, tar = self._target_independent(request, cbody)  # GPT-03: evidence-independent target FALSEs
            conjuncts["TargetAllowed"] = tav
            ecv, ecr = self._evidence_independent(request, now)  # GPT-02: evidence-independent freshness FALSEs
            conjuncts["EvidenceCurrent"] = ecv
            dec, kr = kernel_decision(conjuncts)
            rs = [malf_reason] + [r for r in (cmr + etr + tar + ecr + kr) if r and r not in {malf_reason}]
            self.state.denied[snapshot] = list(rs)
            return self._deny(request, conjuncts, rs, decision=dec)

        # Step 4 (evidence): denials here depend on evidence, so they are terminal for this
        # Every deny -- DENY_FALSE and DENY_UNKNOWN alike -- is terminal for its (request, nonce)
        # snapshot (the nonce is already consumed; a fresh request is a distinct snapshot that
        # re-evaluates). FALSE domination is preserved even here (see _evidence_indeterminate).
        if not isinstance(evidence, dict):
            return _evidence_indeterminate("E-MALFORMED-EVIDENCE")
        # Totality (class fix): reject evidence that cannot be canonicalized -- an integer outside
        # the I-JSON safe range ANYWHERE in the bundle (witness, epoch, time authority) -- before
        # any digest or comparison touches it.
        try:
            canonical_bytes(evidence)
        except Exception:
            return _evidence_indeterminate("E-NONCANONICAL-EVIDENCE")
        if find_prohibited_fields(evidence):
            return _evidence_indeterminate("E-CALLER-SUPPLIED-DERIVED-FIELD")
        # Every untrusted record through the SAME complete validator: bundle closedness + evidence_epoch
        # bounds, and the time authority incl. its signature envelope/canonicalization.
        if not schema_valid(evidence, _EVIDENCE_BUNDLE_SCHEMA, _EVIDENCE_BUNDLE_SCHEMA):
            return _evidence_indeterminate("E-EVIDENCE-SCHEMA-INVALID")
        _ta = evidence.get("time_authority")
        if isinstance(_ta, dict) and not schema_valid(_ta, _TIME_AUTHORITY_SCHEMA, _TIME_AUTHORITY_SCHEMA):
            return _evidence_indeterminate("E-EVIDENCE-SCHEMA-INVALID")

        reasons: List[str] = []

        cm_value, cm_reasons, contract_body = self._contract_match(request, now)
        conjuncts["ContractMatch"] = cm_value
        reasons += cm_reasons
        # V27-GPT-02: capture the validated contract body as IMMUTABLE per-invocation context, so the abort
        # recovers evidence-independent FALSEs from THIS snapshot -- never by re-reading self.contracts, which
        # a later failing evaluator could mutate before raising. The evidence bundle is already immutable.
        self._cur_cbody = copy.deepcopy(contract_body) if isinstance(contract_body, dict) else None

        et_value, et_reasons = self._effect_type_valid(request, contract_body)
        conjuncts["EffectTypeValid"] = et_value
        reasons += et_reasons

        wh_value, wh_reasons, health, witness_receipt = self._witness_healthy(
            request, evidence, now
        )
        conjuncts["WitnessHealthy"] = wh_value
        reasons += wh_reasons

        # Authority ceiling is recomputed from observed health, then checked
        # for monotone narrowing. Widening without an amendment is terminal.
        ceiling: Optional[Authority] = None
        if contract_body is not None:
            effective_health = health if health in HEALTH_ORDER else "UNKNOWN"
            ceiling = ceiling_for_health(contract_body, effective_health)
            if health is not None:
                # GLM-B: only an AUTHENTICATED witness (an invalid signature yields health=None) may
                # PERSIST authority narrowing / advance the epoch. The empty ceiling from an absent or
                # unauthenticated witness still governs THIS decision (E-EFFECT-ABOVE-CEILING), but
                # must not mutate the session's authority lattice.
                narrowing_error = self._apply_narrowing(session, effective_health, ceiling)
                if narrowing_error is not None:
                    return self._deny(
                        request,
                        {name: FALSE for name in KERNEL_CONJUNCTS},
                        [narrowing_error],
                    )
                # V30 GLM-F1/K32-01 FIX (cross-contract ceiling-poison effect bypass): contract_ceiling
                # recording is DEFERRED to the ALLOW path (see below, after `decision != DECISION_ALLOW`
                # returns). The pre-V30 site (here, after _apply_narrowing) ran for EVERY request whose
                # narrowing passed, including requests that were subsequently DENIED on TargetAllowed or
                # EffectTypeValid. A second, separately-registered contract C2 with a strictly larger
                # effect set could poison contract_ceiling with effects the session never held, via a
                # DENIED degraded request whose narrowing was correct but whose effect was above ceiling.
                # After terminalization + lift, re-establishment trusted the poisoned ceiling, and the
                # previously-rejected effect committed end-to-end -- a runtime effect bypass. The fix:
                # record contract_ceiling ONLY when the decision is ALLOW, so only authority the session
                # DEMONSTRABLY holds (as evidenced by a successful authorization) enters the ceiling.
                # The _contract_ceiling_pending flag carries the contract_body to the ALLOW path.
                try:
                    if isinstance(request.get("session_id"), str):
                        self._contract_ceiling_pending = (request["session_id"], contract_body)
                except Exception:
                    reasons.append("E-CEILING-RECORD-FAILED")

        ta_value, ta_reasons = self._target_allowed(request, contract_body, ceiling)
        conjuncts["TargetAllowed"] = ta_value
        reasons += ta_reasons

        ec_value, ec_reasons, evidence_epoch = self._evidence_current(
            request, evidence, now
        )
        conjuncts["EvidenceCurrent"] = ec_value
        reasons += ec_reasons

        decision, kernel_reasons = kernel_decision(conjuncts)
        reasons += kernel_reasons
        # C3/GPT-04: stash the fully evaluated conjuncts so that a later post-admission abort (e.g. a
        # token-factory exception during minting) records the REAL evaluated facts, not all-UNKNOWN.
        self._cur_conjuncts = dict(conjuncts)

        # F-04 freshness: once witness and evidence are authenticated and current, advance the
        # monotonic highest-seen epochs REGARDLESS of the final decision, so an outstanding token
        # bound to an older epoch becomes stale even when THIS request is denied for another reason.
        if (conjuncts.get("WitnessHealthy") == TRUE and conjuncts.get("EvidenceCurrent") == TRUE
                and witness_receipt is not None and evidence_epoch is not None):
            _fwid = witness_receipt["witness_id"]
            self.state.highest_evidence_epoch[session] = max(
                self.state.highest_evidence_epoch.get(session, -1), evidence_epoch)
            self.state.highest_witness_epoch[_fwid] = max(
                self.state.highest_witness_epoch.get(_fwid, -1), witness_receipt["epoch"])
            self.state.highest_witness_sequence[(_fwid, witness_receipt["epoch"])] = max(
                self.state.highest_witness_sequence.get((_fwid, witness_receipt["epoch"]), -1),
                witness_receipt["sequence"])

        if decision != DECISION_ALLOW:
            # P13-GPT-04: every deny (DENY_FALSE or DENY_UNKNOWN) is terminal for its (request+nonce)
            # snapshot. A transient fault is retried as a fresh request; the fresh nonce yields a distinct
            # snapshot that re-evaluates cleanly. This IS a kernel decision (kernel_evaluated=True).
            self.state.denied[snapshot] = list(reasons)
            return self._deny(request, conjuncts, reasons, decision=decision, kernel_evaluated=True)

        # ALLOW path. Commit state that must not be reusable.
        assert witness_receipt is not None and evidence_epoch is not None
        assert ceiling is not None
        # V31 K33-01 FIX (ALLOWed-degraded ceiling poison -- the 32nd instance): contract_ceiling
        # must record only HEALTHY-demonstrated authority. The V30 fix (ALLOW-only write) closed the
        # DENIED-request vector but not the ALLOWED-request vector: a legitimate degraded C2 READ
        # was ALLOWed (READ is in C2's degraded ceiling), yet the write stored ceiling_for_health(
        # contract_body, "HEALTHY") = {DELETE,READ,WRITE} -- the full HEALTHY ceiling of C2, not the
        # degraded ceiling the session actually demonstrated. After a lift, DELETE was authorized and
        # committed. Fix: write contract_ceiling ONLY when health == "HEALTHY". A degraded ALLOW
        # THE CLASS FIX (V34 council -- closes the 34-instance pattern structurally).
        #
        # Root cause across instances 30-34: contract_ceiling could be ABSENT after a successful
        # authorization, and _apply_narrowing's _held check (`if _held is not None`) treated absence
        # as "never touched = establishment free." Each fix narrowed WHEN the ceiling write executes
        # (pre-decision -> ALLOW-only -> HEALTHY-only -> post-mint-only) but every narrowing left a
        # new path where absence persisted: denied requests (V30), degraded ALLOWs (V31), mint faults
        # (V34 F-GS-1), ceiling-write exceptions (A-05), degraded-first sessions (34th instance).
        #
        # The structural fix: ensure contract_ceiling has an entry for this session AT THE TOP OF THE
        # ALLOW PATH, before any conditional (health check, mint, ceiling-write). An empty Authority
        # means "the session has been through an ALLOW decision but has not yet demonstrated any
        # HEALTHY authority." The _held check will fire on ANY post-lift re-establishment, bounding
        # it to at most what was previously demonstrated under HEALTHY (empty = nothing demonstrated
        # = no re-establishment wider than nothing).
        #
        # The HEALTHY-successful write below UPGRADES the entry to demonstrated authority. Degraded
        # ALLOWs, mint faults, and ceiling-write exceptions leave the empty (or prior) entry in place.
        # This closes the class: _held is NEVER None after an ALLOW, regardless of path.
        _cc_pending = getattr(self, "_contract_ceiling_pending", None)
        self._contract_ceiling_pending = None  # always clear, regardless of health
        # CLASS FIX: initialize contract_ceiling for this session if absent. Only first-establish
        # ALLOWs trigger this (subsequent ALLOWs already have an entry from the first).
        _cc_session = (request.get("session_id") if isinstance(request, dict)
                       and isinstance(request.get("session_id"), str) else None)
        if _cc_session is not None and _cc_session not in self.state.contract_ceiling:
            self.state.contract_ceiling[_cc_session] = Authority([], [])
        witness_id = witness_receipt["witness_id"]
        # F-05 + E: generate and collision-check the token BEFORE any ALLOW-side mutation or record.
        # Any mint fault (factory exception OR malformed/out-of-bounds token) is a POST-kernel issuance
        # failure, routed through _issuance_failure so the record stays kernel-consistent (decision ==
        # kernel_decision(conjuncts) = ALLOW, issuance_status=FAILED_NO_EFFECT) rather than an
        # inconsistent DENY_UNKNOWN-with-all-TRUE-conjuncts record (KIMI-5).
        try:
            token_id = self.new_token()
        except Exception:
            return self._issuance_failure(request, conjuncts, snapshot, "E-TOKEN-MINT-FAULT")
        if (not isinstance(token_id, str) or not (8 <= len(token_id) <= 128)
                or find_prohibited_fields({"t": token_id})):  # Kimi-P15-05: match the receipt schema bounds
            return self._issuance_failure(request, conjuncts, snapshot, "E-TOKEN-MINT-INVALID")
        if token_id in self.state.tokens:
            return self._issuance_failure(request, conjuncts, snapshot, "E-TOKEN-FACTORY-COLLISION")
        # Token successfully created. UPGRADE contract_ceiling to demonstrated HEALTHY authority.
        # This only fires for HEALTHY ALLOWs with successful issuance -- the class fix above ensures
        # the entry EXISTS regardless; this upgrades it to the demonstrated ceiling.
        if _cc_pending is not None and health == "HEALTHY":
            _cc_sess, _cc_body = _cc_pending
            try:
                self.state.contract_ceiling[_cc_sess] = ceiling_for_health(_cc_body, "HEALTHY")
            except Exception:
                reasons.append("E-CEILING-RECORD-FAILED")
        request_digest = digest(request)
        expires_at = min(
            parse_rfc3339_utc(request["expires_at"]) or now,
            parse_rfc3339_utc(witness_receipt["expires_at"]) or now,
        )
        receipt = {
            "record_type": "bssg.authorization-receipt",
            "spec_version": SPEC_VERSION,
            "receipt_id": digest_bytes(
                (token_id + "|" + request_digest).encode("utf-8")
            ),
            "request_digest": request_digest,
            "request_id": request["request_id"],
            "subject_id": request["subject_id"],
            "session_id": session,
            "contract_digest": request["contract_digest"],
            "policy_digest": request["policy_digest"],
            "witness_receipt_digest": digest(witness_receipt),
            "evidence_epoch": evidence_epoch,
            "witness_epoch": witness_receipt["epoch"],
            "authority_epoch": self.state.authority_epoch.get(session, 0),
            "authority_snapshot": ceiling.as_json(),
            "decision": DECISION_ALLOW,
            "conjuncts": dict(conjuncts),
            "reason_codes": [],
            "nonce": request["nonce"],
            "effect_type": request["effect_type"],
            "canonical_target": request["target"]["canonical_uri"],
            "params_digest": request["params_digest"],
            "adapter_digest": request["adapter_digest"],
            "commit_token": {
                "token_id": token_id,
                "one_time": True,
                "expires_at_epoch_seconds": expires_at,
            },
            "issued_at_epoch_seconds": now,
            "signature": {
                "alg": "unsigned-reference",
                "kid": "reference-gate",
                "envelope": "detached-json",
                "canonicalization": CANONICALIZATION_ID,
                "verification_status": "not_performed_by_reference_gate",
            },
        }
        record = {
            "record_type": "bssg.decision",
            "spec_version": SPEC_VERSION,
            "gate_version": GATE_VERSION,
            "decision": DECISION_ALLOW,
            "conjuncts": dict(conjuncts),
            "reason_codes": [],
            "kernel_evaluated": True,
            "session_id": session,
            "authority_epoch": self.state.authority_epoch.get(session, 0),
            "authority_snapshot": ceiling.as_json(),
            "request_digest": request_digest,
            "authorization_receipt": receipt,
        }
        self.state.records.append(copy.deepcopy(record))
        self.state.tokens[token_id] = {
            "status": "UNUSED",
            "receipt": copy.deepcopy(receipt),
            # F-GPT-P10-01: an immutable, caller-UNREACHABLE binding snapshot. Commit checks execution
            # bindings against THIS, never against a returned/mutable receipt object.
            "binding": {k: receipt[k] for k in (
                "request_digest", "canonical_target", "params_digest",
                "adapter_digest", "effect_type")},
            "receipt_digest": digest(receipt),
            "policy_digest": request["policy_digest"],
            "session_id": session,
            "authority_epoch": self.state.authority_epoch.get(session, 0),
            "evidence_epoch": evidence_epoch,
            "witness_epoch": witness_receipt["epoch"],
            "witness_sequence": witness_receipt["sequence"],
            "witness_covered_classes": witness_receipt.get("covered_effect_classes", []),
            "witness_id": witness_id,
            "contract_digest": request["contract_digest"],
            "authorized_health": witness_receipt.get("health"),
            "evidence_deadline": (parse_rfc3339_utc(request["issued_at"]) or now) + self.evidence_max_age,
            "expires_at": expires_at,
        }
        return copy.deepcopy(record)

    def _apply_narrowing(
        self, session: str, health: str, new_ceiling: Authority
    ) -> Optional[str]:
        previous = self.state.ceiling.get(session)
        previous_health = self.state.last_health.get(session)
        if previous is None:
            # V29 GPT-P30-01 (RUNTIME side of the grant-poison bypass): when RE-establishing authority from a
            # cleared ceiling (a terminal-lift amendment sets ceiling=None), the fresh ceiling must not exceed the
            # authority the session DEMONSTRABLY, LEGITIMATELY held -- its de-poisoned contract_ceiling. Without
            # this, a widening REJECTED before the lift (never entered contract_ceiling) re-establishes FRESH on
            # this no-widening-check branch, laundering the rejected authority into a clean ALLOW that then
            # commits. Binding it here (rather than restoring ceiling in the amendment) preserves the epoch
            # progression, so an honest degraded-first recovery still lands at the grant's landing epoch and audits
            # clean anchored. The FIRST-ever authorize has no contract_ceiling yet (it is recorded only AFTER
            # _apply_narrowing returns), so _held is None and establishment is free as before; only a post-clear
            # re-establish is bounded, and only DOWN to demonstrably-held authority.
            _held = self.state.contract_ceiling.get(session)
            if _held is not None and not (new_ceiling <= _held):
                self.state.terminal[session] = "E-AUTHORITY-WIDENING"
                return "E-AUTHORITY-WIDENING"
            self.state.ceiling[session] = new_ceiling
            self.state.last_health[session] = health
            self.state.authority_epoch[session] = self.state.authority_epoch.get(session, 0) + 1
            return None
        if not new_ceiling <= previous:
            self.state.terminal[session] = "E-AUTHORITY-WIDENING"
            return "E-AUTHORITY-WIDENING"
        if (
            previous_health is not None
            and HEALTH_ORDER[health] < HEALTH_ORDER[previous_health]
            and not previous.is_empty()
            and not (new_ceiling < previous)
        ):
            self.state.terminal[session] = "E-NONSTRICT-NARROWING"
            return "E-NONSTRICT-NARROWING"
        if new_ceiling != previous or health != previous_health:
            self.state.authority_epoch[session] = self.state.authority_epoch.get(session, 0) + 1
        self.state.ceiling[session] = new_ceiling
        self.state.last_health[session] = health
        return None

    def commit(
        self, token_id: Any, execution_binding: Any, evidence: Any
    ) -> Dict[str, Any]:
        with self._lock:
            if self._in_txn:
                return self._commit_abort(None, "E-REENTRANT-CALL")
            self._in_txn = True
            try:
                # P12-02: reject a non-plain-str token id BEFORE any dict lookup (a str subclass could
                # run a malicious __hash__). P12-03: snapshot inside the guard.
                if type(token_id) is not str:
                    return self._commit_abort(None, "E-COMMIT-UNKNOWN-TOKEN")
                execution_binding = _safe_copy(execution_binding)
                evidence = _safe_copy(evidence)
                return self._commit_locked(token_id, execution_binding, evidence)
            except (KeyboardInterrupt, SystemExit):
                raise
            except BaseException:
                # V33 AUDIT-V33-01 (same class as V29 GPT-P30-05/CE167): the commit pre-reserve
                # boundary must catch BaseException, not only Exception. A hostile caller-owned
                # dict subclass (e.g. execution_binding.items() raises BaseException) must fail
                # closed to _commit_abort, not escape the public API leaving the token UNUSED
                # with no failure record. KI/SE propagate above; everything else fails closed.
                return self._commit_abort(token_id if type(token_id) is str else None)
            finally:
                self._in_txn = False

    def _commit_abort(self, token_id: Any, reason: str = "E-COMMIT-ABORTED") -> Dict[str, Any]:
        """Totality: any pre/post-reserve fault in commit lands the token in VOID with a failure record."""
        entry = self.state.tokens.get(token_id) if type(token_id) is str else None
        if isinstance(entry, dict):
            entry["status"] = "VOID"
        return self._execution_failure(entry if isinstance(entry, dict) else None, reason)

    def _commit_locked(
        self, token_id: Any, execution_binding: Any, evidence: Any
    ) -> Dict[str, Any]:
        """
        Atomic commit protocol. This is a protocol obligation around the frozen
        kernel; it is NOT a sixth conjunct and the kernel equation is unchanged.

        Steps: token lookup, compare-and-swap UNUSED -> CONSUMED, expiry check,
        epoch revalidation against the current gate state, and binding
        revalidation against the authorized digests.
        """
        if not isinstance(token_id, str) or token_id not in self.state.tokens:
            return self._execution_failure(None, "E-COMMIT-UNKNOWN-TOKEN")
        entry = self.state.tokens[token_id]
        with self._commit_lock:
            if entry["status"] != "UNUSED":
                return self._execution_failure(entry, "E-COMMIT-DOUBLE-SPEND")
            entry["status"] = "COMMITTING"
        # Read the clock AFTER reserving, so a token that expired while this commit was queued is
        # rejected on fresh time rather than the stale pre-queue value (P-F).
        try:
            now = self._read_clock()
            return self._commit_after_reserve(
                token_id, entry, execution_binding, evidence, now
            )
        except BaseException as _exc:
            # GPT-P30-05 (MAJOR liveness/totality): ANY post-reserve throwable -- an ordinary Exception OR a
            # dependency-originated non-Exception BaseException raised by the injected clock/verifier -- must
            # roll the COMMITTING reservation back so no token is stranded. KeyboardInterrupt/SystemExit still
            # propagate, but ONLY after the rollback (the liveness invariant is restored unconditionally).
            entry["status"] = "VOID"
            if isinstance(_exc, (KeyboardInterrupt, SystemExit)):
                raise
            return self._execution_failure(entry, "E-COMMIT-ABORTED")

    def _commit_after_reserve(
        self, token_id, entry, execution_binding, evidence, now
    ):
        session = entry["session_id"]
        if session in self.state.terminal:
            entry["status"] = "VOID"
            return self._execution_failure(entry, "E-SESSION-TERMINAL")
        if not isinstance(execution_binding, dict) or find_prohibited_fields(
            execution_binding
        ):
            entry["status"] = "VOID"
            return self._execution_failure(entry, "E-CALLER-SUPPLIED-DERIVED-FIELD")
        if now > entry["expires_at"]:
            entry["status"] = "EXPIRED"
            return self._execution_failure(entry, "E-COMMIT-TOKEN-EXPIRED")
        # P3-02: the evidence freshness bound is enforced at commit too, not only at authorize -- a
        # still-unexpired token whose evidence has gone stale cannot redeem.
        if now > entry.get("evidence_deadline", now):
            entry["status"] = "VOID"
            return self._execution_failure(entry, "E-COMMIT-EVIDENCE-STALE")

        receipt = entry["receipt"]
        # Commit-time revalidation of epochs.
        if self.state.authority_epoch.get(session, 0) != entry["authority_epoch"]:
            entry["status"] = "VOID"
            return self._execution_failure(entry, "E-COMMIT-AUTHORITY-EPOCH-CHANGED")
        if self.state.highest_evidence_epoch.get(session, -1) != entry["evidence_epoch"]:
            entry["status"] = "VOID"
            return self._execution_failure(entry, "E-COMMIT-EVIDENCE-EPOCH-CHANGED")

        _twid = entry.get("witness_id")
        if _twid is not None and self.state.highest_witness_epoch.get(
            _twid, entry["witness_epoch"]
        ) > entry["witness_epoch"]:
            entry["status"] = "VOID"
            return self._execution_failure(entry, "E-COMMIT-WITNESS-EPOCH-STALE")

        # F-06: a contract revoked after authorization must void the outstanding token.
        _cd = entry.get("contract_digest")
        _contract = self.contracts.get(_cd) if isinstance(_cd, str) else None
        if (_contract is None or not isinstance(_contract, dict)
                or not isinstance(_contract.get("body"), dict)
                or _contract.get("revoked") is not False):
            entry["status"] = "VOID"
            return self._execution_failure(entry, "E-COMMIT-CONTRACT-REVOKED")
        # DP-GPT-06: re-verify the bound contract body still matches its digest against GROUND TRUTH.
        # A mutation under the same registry key invalidates the authorization -- the caller cannot
        # supply a substitute; the gate re-derives from the registry.
        if digest(_contract["body"]) != _cd:
            entry["status"] = "VOID"
            return self._execution_failure(entry, "E-COMMIT-CONTRACT-DIGEST-CHANGED")
        # DP-GPT-09: the bound contract must not have expired between authorization and effect.
        _na = parse_rfc3339_utc(_contract["body"].get("not_after"))
        if _na is None or now > _na:
            entry["status"] = "VOID"
            return self._execution_failure(entry, "E-COMMIT-CONTRACT-EXPIRED")
        # F-GPT-P10-03 #1 / GLM F-1: the bound POLICY is an authorization-bound fact too; re-derive it
        # against ground truth (existence + body digest), symmetric with the contract re-derivation.
        _pd = entry.get("policy_digest")
        _policy = self.policies.get(_pd) if isinstance(_pd, str) else None
        if (_policy is None or not isinstance(_policy, dict)
                or not isinstance(_policy.get("body"), dict) or digest(_policy["body"]) != _pd):
            entry["status"] = "VOID"
            return self._execution_failure(entry, "E-COMMIT-POLICY-CHANGED")

        # Commit-time evidence gets the SAME ingress validation as authorize-time evidence.
        if not isinstance(evidence, dict):
            # F-GPT-P10-03 #3: supplied commit evidence must be a closed bundle ({} = none). A non-dict
            # (None, str, int, list, bool) is malformed and fails closed rather than skipping validation.
            entry["status"] = "VOID"
            return self._execution_failure(entry, "E-COMMIT-EVIDENCE-MALFORMED")
        if isinstance(evidence, dict):
            try:
                canonical_bytes(evidence)
            except Exception:
                entry["status"] = "VOID"
                return self._execution_failure(entry, "E-COMMIT-EVIDENCE-NONCANONICAL")
            if find_prohibited_fields(evidence):
                entry["status"] = "VOID"
                return self._execution_failure(entry, "E-COMMIT-EVIDENCE-DERIVED-FIELD")
            if not schema_valid(evidence, _EVIDENCE_BUNDLE_SCHEMA, _EVIDENCE_BUNDLE_SCHEMA):
                entry["status"] = "VOID"
                return self._execution_failure(entry, "E-COMMIT-EVIDENCE-SCHEMA-INVALID")
            _cta = evidence.get("time_authority")
            if isinstance(_cta, dict) and not schema_valid(_cta, _TIME_AUTHORITY_SCHEMA, _TIME_AUTHORITY_SCHEMA):
                entry["status"] = "VOID"
                return self._execution_failure(entry, "E-COMMIT-EVIDENCE-SCHEMA-INVALID")
            if isinstance(_cta, dict):
                # DP-GPT-07: a supplied commit-time time authority must carry a VALID signature, held to
                # the same bar authorization applies -- schema validity alone is not sufficient.
                _ta_payload = {k: v for k, v in _cta.items() if k != "signature"}
                if self.verify_signature("time", canonical_bytes(_ta_payload), _cta.get("signature")) is not True:
                    entry["status"] = "VOID"
                    return self._execution_failure(entry, "E-COMMIT-TIME-AUTHORITY-SIGNATURE-INVALID")
                if _cta.get("kind") not in ("external_signed_anchor", "trusted_timestamp", "epoch_id"):
                    entry["status"] = "VOID"
                    return self._execution_failure(entry, "E-COMMIT-TIME-AUTHORITY-UNDECLARED")
                _cskew = _cta.get("max_skew_seconds"); _canchor = parse_rfc3339_utc(_cta.get("anchor_time"))
                if (not isinstance(_cskew, int) or isinstance(_cskew, bool)
                        or _canchor is None or abs(_canchor - now) > _cskew):
                    entry["status"] = "VOID"
                    return self._execution_failure(entry, "E-COMMIT-TIME-AUTHORITY-CLOCK-AMBIGUOUS")
            _cw = evidence.get("witness_receipt")
            if isinstance(_cw, dict) and not validate_record(_cw, "witness-receipt"):
                entry["status"] = "VOID"
                return self._execution_failure(entry, "E-COMMIT-WITNESS-SCHEMA-INVALID")
            # DP-GPT-02: a supplied commit-evidence epoch must MATCH the authorization-bound epoch. The
            # caller cannot substitute a different epoch (higher or lower) at redemption.
            _cee = evidence.get("evidence_epoch")
            if _cee is not None and _cee != entry["evidence_epoch"]:
                entry["status"] = "VOID"
                return self._execution_failure(entry, "E-COMMIT-EVIDENCE-EPOCH-MISMATCH")
        # Optional fresh witness assertion at commit time.
        if isinstance(evidence, dict) and "witness_receipt" in evidence:
            fresh = evidence["witness_receipt"]
            if not isinstance(fresh, dict):
                entry["status"] = "VOID"
                return self._execution_failure(entry, "E-COMMIT-WITNESS-MALFORMED")
            if HEALTH_ORDER.get(fresh.get("health"), 0) < HEALTH_ORDER.get(entry.get("authorized_health"), 2):
                # health may CONFIRM or IMPROVE relative to authorization, never regress below it
                entry["status"] = "VOID"
                return self._execution_failure(entry, "E-COMMIT-WITNESS-HEALTH-REGRESSED")
            _fresh_payload = {k: v for k, v in fresh.items() if k != "signature"}
            if self.verify_signature("witness", canonical_bytes(_fresh_payload), fresh.get("signature")) is not True:
                entry["status"] = "VOID"
                return self._execution_failure(entry, "E-COMMIT-WITNESS-SIGNATURE-INVALID")
            fresh_epoch = fresh.get("epoch")
            if not isinstance(fresh_epoch, int) or isinstance(fresh_epoch, bool):
                entry["status"] = "VOID"
                return self._execution_failure(entry, "E-COMMIT-WITNESS-MALFORMED")
            if fresh_epoch != entry["witness_epoch"]:
                entry["status"] = "VOID"
                return self._execution_failure(entry, "E-COMMIT-WITNESS-EPOCH-CHANGED")
            if fresh.get("witness_id") != entry.get("witness_id"):
                entry["status"] = "VOID"
                return self._execution_failure(entry, "E-COMMIT-WITNESS-IDENTITY-MISMATCH")
            if fresh.get("covered_subject") != entry["receipt"].get("subject_id"):
                entry["status"] = "VOID"
                return self._execution_failure(entry, "E-COMMIT-WITNESS-SUBJECT-MISMATCH")
            _decl = fresh.get("independence_declaration")
            if (not isinstance(_decl, dict) or _decl.get("subject_can_administer") is not False
                    or _decl.get("control_domain") == fresh.get("covered_subject_domain")):
                entry["status"] = "VOID"
                return self._execution_failure(entry, "E-COMMIT-WITNESS-NOT-INDEPENDENT")
            _fresh_seq = fresh.get("sequence")
            if (not isinstance(_fresh_seq, int) or isinstance(_fresh_seq, bool)
                    or _fresh_seq < entry.get("witness_sequence", -1)):
                entry["status"] = "VOID"
                return self._execution_failure(entry, "E-COMMIT-WITNESS-SEQUENCE-ROLLBACK")
            _fresh_exp = parse_rfc3339_utc(fresh.get("expires_at"))
            if _fresh_exp is None or now > _fresh_exp:
                entry["status"] = "VOID"
                return self._execution_failure(entry, "E-COMMIT-WITNESS-EXPIRED")
            if not set(entry.get("witness_covered_classes", [])) <= set(fresh.get("covered_effect_classes") or []):
                entry["status"] = "VOID"
                return self._execution_failure(entry, "E-COMMIT-WITNESS-COVERAGE-GAP")
            # DP-G3a: the commit-time fresh witness must carry the SAME within-authority assessment the
            # authorization path requires -- an outside-subject-authority control predicate.
            _assess = fresh.get("within_auth_assessment")
            if not isinstance(_assess, dict) or _assess.get("value") != "outside_subject_authority":
                entry["status"] = "VOID"
                return self._execution_failure(entry, "E-COMMIT-WITNESS-WITHIN-AUTH")
            # DP-G3b: the fresh witness must not be observed in the future beyond skew (clock ambiguity),
            # the same bound authorization enforces.
            _obs = parse_rfc3339_utc(fresh.get("observed_at"))
            if _obs is None or _obs > now + self.max_skew:
                entry["status"] = "VOID"
                return self._execution_failure(entry, "E-COMMIT-WITNESS-CLOCK-AMBIGUOUS")
            # INTERVAL parity (GPT-P19-04): the commit-time fresh witness gets the SAME inverted-lease
            # rule as the authorize-time witness -- observed_at MUST NOT be after expires_at. Without
            # this, a schema-valid fresh witness with an inverted lease could revalidate PASS at commit.
            if _fresh_exp is not None and _obs > _fresh_exp:
                entry["status"] = "VOID"
                return self._execution_failure(entry, "E-COMMIT-WITNESS-LEASE-INVERTED")

        # Binding revalidation.
        required = (
            "request_digest",
            "canonical_target",
            "params_digest",
            "adapter_digest",
            "effect_type",
        )
        if sorted(execution_binding.keys()) != sorted(required):
            entry["status"] = "VOID"
            return self._execution_failure(entry, "E-COMMIT-BINDING-FIELDS")
        _bind = entry.get("binding") or {}
        for field in required:
            if execution_binding[field] != _bind.get(field):
                entry["status"] = "VOID"
                return self._execution_failure(entry, "E-COMMIT-BINDING-MISMATCH")

        # P9: re-check session terminality as the last gate before consumption, so a
        # terminalization that raced in during revalidation still voids this commit. The
        # tiny residual window before CONSUMED requires a shared authorize/commit
        # transaction -- a BSSG-H deployment obligation.
        if session in self.state.terminal:
            entry["status"] = "VOID"
            return self._execution_failure(entry, "E-SESSION-TERMINAL")
        if isinstance(evidence, dict) and isinstance(evidence.get("witness_receipt"), dict):
            # DP-GPT-10: fold the (already fully re-validated) fresh witness into the monotonic state so
            # a later request cannot re-authorize with an older epoch/sequence than one just committed.
            _fw = evidence["witness_receipt"]; _fwid2 = _fw.get("witness_id")
            if isinstance(_fwid2, str):
                self.state.highest_witness_epoch[_fwid2] = max(
                    self.state.highest_witness_epoch.get(_fwid2, -1), _fw["epoch"])
                self.state.highest_witness_sequence[(_fwid2, _fw["epoch"])] = max(
                    self.state.highest_witness_sequence.get((_fwid2, _fw["epoch"]), -1), _fw["sequence"])
        entry["status"] = "CONSUMED"
        execution = {
            "record_type": "bssg.execution-receipt",
            "spec_version": SPEC_VERSION,
            "execution_id": digest_bytes(("exec|" + token_id).encode("utf-8")),
            "commit_token_id": token_id,
            "authorization_receipt_digest": digest(receipt),
            "request_digest": receipt["request_digest"],
            "executed_target_canonical": receipt["canonical_target"],
            "executed_params_digest": receipt["params_digest"],
            "adapter_digest": receipt["adapter_digest"],
            "outcome": "COMMITTED_PENDING_OUTCOME",
            "commit_time_epoch_seconds": now,
            "revalidation": {
                "authority_epoch": self.state.authority_epoch.get(session, 0),
                "evidence_epoch": self.state.highest_evidence_epoch.get(session, -1),
                "witness_epoch": entry["witness_epoch"],
                "result": "PASS",
            },
            "reason_codes": [],
            "signature": {
                "alg": "unsigned-reference",
                "kid": "reference-gate",
                "envelope": "detached-json",
                "canonicalization": CANONICALIZATION_ID,
                "verification_status": "not_performed_by_reference_gate",
            },
        }
        self.state.records.append(copy.deepcopy(execution))
        return copy.deepcopy(execution)

    def _execution_failure(
        self, entry: Optional[Dict[str, Any]], reason: str
    ) -> Dict[str, Any]:
        # Totality/liveness (F-GPT-P10-04): the failure-record path must never itself escape -- a
        # broken clock or a malformed receipt must not turn a VOID into an uncaught exception.
        # H (pass-17) + K18-14 (pass-18): a clock that RAISES *or* returns a bad value (non-int or
        # negative) is treated as unavailable -- commit time is null with an explicit E-CLOCK-UNAVAILABLE
        # reason, never an out-of-domain or negative sentinel that would violate the schema minimum:0.
        _clock_reasons: List[str] = []
        try:
            _ct = self._read_clock()
        except (KeyboardInterrupt, SystemExit):
            raise
        except BaseException:
            # GPT-P30-05: the failure-record path must never itself escape -- a dependency-originated
            # non-Exception BaseException from the clock is treated as clock-unavailable, like any other fault.
            _ct = None
            _clock_reasons = ["E-CLOCK-UNAVAILABLE"]
        _rcpt = entry.get("receipt") if isinstance(entry, dict) else None
        _rcpt = _rcpt if isinstance(_rcpt, dict) else None
        _tok = None
        if _rcpt is not None and isinstance(_rcpt.get("commit_token"), dict):
            _tok = _rcpt["commit_token"].get("token_id")
        record = {
            "record_type": "bssg.execution-receipt",
            "spec_version": SPEC_VERSION,
            "execution_id": None,
            "commit_token_id": _tok,
            "authorization_receipt_digest": None if _rcpt is None else digest(_rcpt),
            "request_digest": None if _rcpt is None else _rcpt.get("request_digest"),
            "executed_target_canonical": None,
            "executed_params_digest": None,
            "adapter_digest": None,
            "outcome": "FAILED_NO_EFFECT",
            "commit_time_epoch_seconds": _ct,
            "revalidation": {"result": "FAIL"},
            "reason_codes": [reason] + _clock_reasons,
            "signature": {
                "alg": "unsigned-reference",
                "kid": "reference-gate",
                "envelope": "detached-json",
                "canonicalization": CANONICALIZATION_ID,
                "verification_status": "not_performed_by_reference_gate",
            },
        }
        self.state.records.append(copy.deepcopy(record))
        return copy.deepcopy(record)

    # -- recovery --------------------------------------------------------

    def submit_amendment(self, amendment: Any) -> Dict[str, Any]:
        with self._lock:
            if self._in_txn:
                return self._amendment_abort("E-REENTRANT-CALL")
            self._in_txn = True
            try:
                amendment = _safe_copy(amendment)
                return self._submit_amendment_locked(amendment)
            except (KeyboardInterrupt, SystemExit):
                raise
            except BaseException:
                # GPT-P30-05: a dependency-originated non-Exception BaseException (injected verifier/clock)
                # must fail closed with a recorded correction-outcome, not escape leaving no record.
                return self._amendment_abort("E-AMENDMENT-ABORTED")
            finally:
                self._in_txn = False

    def _amendment_reject(self, reason: str) -> Dict[str, Any]:
        """GPT-07: an ORDINARY amendment rejection is recorded to the audit trail, so a failed attempt to
        lift a terminal state is never invisible in state.records (symmetry with the amendment abort)."""
        self.state.records.append(copy.deepcopy({
            "record_type": "bssg.correction-outcome",
            "spec_version": SPEC_VERSION,
            "accepted": False,
            "reason_codes": [reason],
        }))
        return {"accepted": False, "reason_codes": [reason]}

    def _amendment_abort(self, reason: str) -> Dict[str, Any]:
        """GLM-F1: an amendment abort is RECORDED to the audit trail, symmetric with authorize/commit."""
        rec = {
            "record_type": "bssg.correction-outcome",
            "spec_version": SPEC_VERSION,
            "accepted": False,
            "reason_codes": [reason],
        }
        self.state.records.append(copy.deepcopy(rec))
        return {"accepted": False, "reason_codes": [reason]}

    def _submit_amendment_locked(self, amendment: Any) -> Dict[str, Any]:
        """
        Recovery from a terminal state requires an independent amendment: at
        least two adjudicators in control domains distinct from each other and
        from the subject, each with a signature the injected verifier accepts.

        This code checks the STRUCTURE of independence. It does not and cannot
        establish that the declared control domains are actually independent.
        """
        if not isinstance(amendment, dict) or find_prohibited_fields(amendment):
            return self._amendment_reject("E-AMENDMENT-MALFORMED")
        if amendment.get("record_type") != "bssg.correction-event":
            return self._amendment_reject("E-AMENDMENT-WRONG-TYPE")
        if not validate_record(amendment, "correction-event"):
            return self._amendment_reject("E-AMENDMENT-SCHEMA-INVALID")
        _topsig = amendment.get("signature")
        if not isinstance(_topsig, dict) or self.verify_signature(
            "correction", canonical_bytes({k: v for k, v in amendment.items() if k != "signature"}), _topsig
        ) is not True:
            return self._amendment_reject("E-AMENDMENT-BAD-SIGNATURE")
        _required = {
            "record_type", "spec_version", "correction_id", "correction_class", "supersedes",
            "reason_code", "issued_by", "issued_at", "descendants", "descendant_closure_status",
            "signature",
        }
        _allowed = _required | {
            "session_id", "subject_control_domain", "adjudicators",
            "unreachable_descendants", "effective_from", "notes",
        }
        if (_required - set(amendment.keys())) or (set(amendment.keys()) - _allowed):
            return self._amendment_reject("E-AMENDMENT-SCHEMA-INVALID")
        if amendment.get("spec_version") != SPEC_VERSION:
            return self._amendment_reject("E-AMENDMENT-SCHEMA-INVALID")
        if amendment.get("descendant_closure_status") not in ("COMPLETE", "PARTIAL", "UNKNOWN"):
            return self._amendment_reject("E-AMENDMENT-SCHEMA-INVALID")
        if check_correction_closure(amendment):
            return self._amendment_reject("E-AMENDMENT-CLOSURE-INVALID")
        _cclass = amendment.get("correction_class")
        if _cclass == "AMEND_AUTHORITY":
            # v0.1 scope: AMEND_AUTHORITY (authority re-widening) is a RESERVED correction class, not
            # implemented by this reference gate. It is refused with a distinct, honest code rather
            # than a schema error, and the spec (R-1) marks it reserved for a future version.
            return self._amendment_reject("E-AMENDMENT-CLASS-UNIMPLEMENTED")
        if _cclass != "LIFT_TERMINAL_STATE":
            return self._amendment_reject("E-AMENDMENT-WRONG-CLASS")
        session = amendment.get("session_id")
        if session not in self.state.terminal:
            return self._amendment_reject("E-AMENDMENT-NO-TERMINAL-STATE")
        correction_id = amendment.get("correction_id")
        if correction_id in self.state.consumed_corrections:
            return self._amendment_reject("E-AMENDMENT-REPLAY")
        adjudicators = amendment.get("adjudicators")
        if not isinstance(adjudicators, list) or len(adjudicators) < 2:
            return self._amendment_reject("E-AMENDMENT-QUORUM")
        domains = set()
        kids = set()
        subject_domain = amendment.get("subject_control_domain")
        # F-GPT-P10-02: the subject-domain exclusion is the load-bearing recovery-independence datum. A
        # lift MUST declare a concrete subject_control_domain; absent/None/empty makes the adjudicator
        # independence comparison vacuous (an adjudicator in the subject's own domain would pass).
        if not isinstance(subject_domain, str) or not subject_domain:
            return self._amendment_reject("E-AMENDMENT-SUBJECT-DOMAIN-MISSING")
        for adjudicator in adjudicators:
            if not isinstance(adjudicator, dict):
                return self._amendment_reject("E-AMENDMENT-MALFORMED")
            domain = adjudicator.get("control_domain")
            if not isinstance(domain, str) or not domain:
                return self._amendment_reject("E-AMENDMENT-DOMAIN")
            if domain == subject_domain:
                # C2 (F-BSSG-P15-GPT-05 / GLM-03 / KIMI-1): EVERY rejection routes through
                # _amendment_reject so exactly one correction-outcome is recorded per submission.
                return self._amendment_reject("E-AMENDMENT-NOT-INDEPENDENT")
            signature = adjudicator.get("signature")
            if not isinstance(signature, dict):
                return self._amendment_reject("E-AMENDMENT-UNSIGNED")
            if signature.get("kid") != adjudicator.get("adjudicator_id"):
                return self._amendment_reject("E-AMENDMENT-KID-MISMATCH")
            payload = {k: v for k, v in amendment.items()
                       if k not in ("adjudicators", "signature")}
            payload["adjudicators"] = [
                {"adjudicator_id": a.get("adjudicator_id"), "control_domain": a.get("control_domain")}
                for a in adjudicators
            ]
            verdict = self.verify_signature(
                "adjudicator", canonical_bytes(payload), signature
            )
            if verdict is not True:
                # C2: route through _amendment_reject (see NOT-INDEPENDENT above).
                return self._amendment_reject("E-AMENDMENT-SIGNATURE-NOT-ESTABLISHED")
            domains.add(domain)
            kids.add(signature.get("kid"))
        if len(domains) < len(adjudicators):
            return self._amendment_reject("E-AMENDMENT-DOMAIN-COLLISION")
        if len(kids) < len(adjudicators):
            return self._amendment_reject("E-AMENDMENT-SIGNATURE-COLLISION")
        del self.state.terminal[session]
        self.state.consumed_corrections.add(correction_id)
        self.state.ceiling[session] = None
        self.state.last_health[session] = None
        self.state.authority_epoch[session] = self.state.authority_epoch.get(session, 0) + 1
        # B (V28): write the AUTHENTICATED grant. This line is reached ONLY after the terminal-state check,
        # quorum, domain-independence, and non-replay all passed -- i.e. the runtime genuinely accepted this
        # LIFT. The grant binds the landing epoch and the authenticated restore target (the session's full
        # contract ceiling). V29 WITHDRAWAL: the grant is INERT for the offline verdict (the checker reports
        # armed re-widens as X7U regardless of grant presence). The grant is retained for runtime diagnostics
        # and future online verification. A forged marker (or a runtime-rejected amendment) still produces no
        # grant entry, though under the withdrawal this is moot since no grant changes the offline verdict.
        _rc = self.state.contract_ceiling.get(session)
        # V29 GPT-P30-02 (multi-cycle grant retention): APPEND to a per-session grant LEDGER rather than
        # overwriting the single latest grant. A conformant history with TWO+ accepted amendments produces one
        # grant per landing; the offline checker must authenticate EACH re-widen against ITS amendment's grant.
        # Overwriting kept only the last grant, so a legitimate second-amendment history falsely audited the
        # first (now grant-less) re-widen as X7 -- an over-strict whole-log conformance soundness failure.
        self.state.amendment_grants.setdefault(session, []).append({
            "correction_digest": digest(amendment),
            "landing_epoch": self.state.authority_epoch.get(session, 0) + 1,
            "restored_effects": frozenset(_rc.effects) if _rc is not None else frozenset(),
            "restored_targets": frozenset(_rc.targets) if _rc is not None else frozenset(),
        })
        self.state.records.append(copy.deepcopy(amendment))
        # A2 (GPT-P19-01): emit a GATE-ISSUED acceptance marker that records the VERIFIED result (this
        # code path ran only after every signature/quorum/independence check passed). X7's carve-out arms
        # from THIS marker, never from re-deriving acceptance from a correction-event's shape -- so a
        # schema-valid event with rejected/forged signatures can no longer license a widening.
        new_epoch = self.state.authority_epoch.get(session, 0)
        self.state.records.append({
            "record_type": "bssg.correction-accepted",
            "spec_version": SPEC_VERSION,
            "gate_version": GATE_VERSION,
            "correction_id": correction_id,
            "correction_class": "LIFT_TERMINAL_STATE",
            "session_id": session,
            "authority_epoch": new_epoch,
            # K26-X7-1: the ceiling is now None, so the NEXT authorize takes the previous-is-None branch and
            # bumps the epoch AGAIN -- the honest re-widen therefore lands at new_epoch + 1. The marker
            # records that LANDING epoch so the offline checker licenses the real recovery record (and not a
            # forged record at new_epoch, which the runtime never emits). The gate owns the bump logic, so it
            # declares where the license fires rather than the checker re-deriving the arithmetic.
            "licensed_epoch": new_epoch + 1,
            "correction_digest": digest(amendment),
            "adjudicators_verified": len(adjudicators),
        })
        return {
            "accepted": True,
            "reason_codes": [],
            "authority_epoch": new_epoch,
        }


# ---------------------------------------------------------------------------
# Cross-record invariant checks (used by tests and by the verifier)
# ---------------------------------------------------------------------------


def check_cross_record_invariants(
    request: Dict[str, Any],
    authorization: Dict[str, Any],
    witness_receipt: Dict[str, Any],
    execution: Optional[Dict[str, Any]] = None,
) -> List[str]:
    """Return violated invariant identifiers (empty list means all held)."""
    violations: List[str] = []
    if authorization.get("request_digest") != digest(request):
        violations.append("X1")
    if authorization.get("witness_receipt_digest") != digest(witness_receipt):
        violations.append("X2")
    if witness_receipt.get("covered_subject") != request.get("subject_id"):
        violations.append("X2b")
    if execution is not None:
        if execution.get("authorization_receipt_digest") != digest(authorization):
            violations.append("X3")
        if execution.get("request_digest") != authorization.get("request_digest"):
            violations.append("X3b")
        if execution.get("executed_target_canonical") != authorization.get(
            "canonical_target"
        ):
            violations.append("X3c")
        if execution.get("executed_params_digest") != authorization.get(
            "params_digest"
        ):
            violations.append("X3d")
        if execution.get("commit_token_id") != authorization.get("commit_token", {}).get(
            "token_id"
        ):
            violations.append("X4")
    # GPT-06: apply the X8 receipt-shape checker to the authorization itself, so a forged ALLOW receipt
    # (e.g. EvidenceCurrent=UNKNOWN, or a non-empty reason list) is caught by the cross-record invariant
    # rather than only by the standalone checker.
    violations.extend(check_allow_receipt(authorization))
    return violations


def check_correction_closure(correction: Dict[str, Any]) -> List[str]:
    """X5: a correction may not report COMPLETE descendant closure it lacks."""
    violations: List[str] = []
    if not isinstance(correction, dict):
        return ["X5"]                      # non-total guard: a non-dict correction fails closed, never raises
    declared = correction.get("descendant_closure_status")
    descendants = correction.get("descendants")
    known_gaps = correction.get("unreachable_descendants")
    if declared == "COMPLETE":
        if not isinstance(descendants, list):
            violations.append("X5")
        if known_gaps:
            violations.append("X5")
    if declared not in ("COMPLETE", "PARTIAL", "UNKNOWN"):
        violations.append("X5b")
    return violations


def check_allow_receipt(receipt: Dict[str, Any]) -> List[str]:
    """X8: an ALLOW authorization receipt MUST carry exactly the five conjunct keys, each TRUE, and an
    empty reason-code list. A forged receipt (EvidenceCurrent=UNKNOWN, a missing/extra conjunct, or a
    non-empty reason list) is a violation."""
    violations: List[str] = []
    if not isinstance(receipt, dict) or receipt.get("decision") != DECISION_ALLOW:
        return violations
    conjuncts = receipt.get("conjuncts")
    if not isinstance(conjuncts, dict) or set(conjuncts.keys()) != set(KERNEL_CONJUNCTS):
        violations.append("X8")
    elif any(conjuncts.get(k) != TRUE for k in KERNEL_CONJUNCTS):
        violations.append("X8")
    # C6 (F-BSSG-P15-GPT-06 / KIMI): the required shape is an empty reason-code LIST, not merely a
    # falsy value. A forged receipt with reason_codes missing, None, 0, "", or {} previously passed
    # the truthiness test; require the key present, a list, and == [].
    rc = receipt.get("reason_codes")
    if not isinstance(rc, list) or rc:
        violations.append("X8")
    return violations


def _json_scalar_eq(a: Any, b: Any) -> bool:
    """Type-strict JSON scalar equality (retires the pass-19 type-confusion shape: GPT-P19-02 / K19-B1).
    Python's `==` treats True == 1 and 1.0 == 1, so a tampered top-level authority field typed as a bool
    could alias a genuine int and evade the X7 divergence check. Two JSON scalars are equal only when
    they share the SAME builtin type and compare equal."""
    if type(a) is bool or type(b) is bool:
        return type(a) is type(b) and a == b
    return type(a) is type(b) and a == b


def _safe_strset(x: Any):
    """Return a set of the list's string elements, or None if the list is missing or contains a
    non-string element (unhashable nested list/dict, number, bool, ...) -- retires the pass-19
    unhashable-JSON-element crash shape (K19-E1). None makes the caller fail closed rather than raise
    TypeError inside an offline audit. Effects and target scopes are string enums by schema."""
    if not isinstance(x, list):
        return None
    if not all(isinstance(e, str) for e in x):
        return None
    return set(x)


def _auth_subset(a: Dict[str, Any], b: Dict[str, Any]) -> bool:
    if not isinstance(a, dict) or not isinstance(b, dict):
        return False
    ae, at = _safe_strset(a.get("effects")), _safe_strset(a.get("target_scopes"))
    be, bt = _safe_strset(b.get("effects")), _safe_strset(b.get("target_scopes"))
    if any(s is None for s in (ae, at, be, bt)):
        return False
    return ae <= be and at <= bt


def _auth_equal(a: Dict[str, Any], b: Dict[str, Any]) -> bool:
    if not isinstance(a, dict) or not isinstance(b, dict):
        return False
    ae, at = _safe_strset(a.get("effects")), _safe_strset(a.get("target_scopes"))
    be, bt = _safe_strset(b.get("effects")), _safe_strset(b.get("target_scopes"))
    if any(s is None for s in (ae, at, be, bt)):
        return False
    return ae == be and at == bt


def _auth_nonempty(a: Dict[str, Any]) -> bool:
    return bool(a.get("effects")) or bool(a.get("target_scopes"))


def _lift_shape_ok(ev: Dict[str, Any]) -> bool:
    """The bound correction-event must have accepted-LIFT SHAPE: schema-valid, correct class, a declared
    subject domain, and a >=2-adjudicator quorum with distinct control domains excluding the subject."""
    try:
        if not isinstance(ev, dict) or ev.get("record_type") != "bssg.correction-event":
            return False
        if ev.get("correction_class") != "LIFT_TERMINAL_STATE" or not validate_record(ev, "correction-event"):
            return False
        subj = ev.get("subject_control_domain")
        if not isinstance(subj, str) or not subj:
            return False
        adj = ev.get("adjudicators")
        if not isinstance(adj, list) or len(adj) < 2:
            return False
        domains = set()
        for a in adj:
            if not isinstance(a, dict):
                return False
            d = a.get("control_domain")
            if not isinstance(d, str) or not d or d == subj:
                return False
            domains.add(d)
        return len(domains) == len(adj)
    except Exception:
        return False


def _marker_bound(marker: Dict[str, Any], events: Dict[str, Any], verify=None) -> bool:
    """A2 (GPT-P2 / K20-F1 / GPT-P21-01): a marker arms the carve-out ONLY IF its correction_digest resolves
    to a correction-event PRESENT earlier in the same stream whose recomputed digest matches, which has
    accepted-LIFT shape, AND whose session_id / correction_id / correction_class match the marker
    type-strictly (so an event for session A cannot license a widening in session B via a fabricated marker).
    If a `verify` callable is supplied, each adjudicator signature on the bound event MUST verify; without
    it the binding is structural and offline audit cannot cryptographically establish acceptance (stated
    boundary). A bare, unbound, or cross-identity marker no longer arms."""
    try:
        cd = marker.get("correction_digest")
        ev = events.get(cd)
        if not isinstance(ev, dict) or digest(ev) != cd or not _lift_shape_ok(ev):
            return False
        # identity binding (GPT-P21-01): the marker must name the SAME session, correction, and class.
        if not _json_scalar_eq(marker.get("session_id"), ev.get("session_id")):
            return False
        if not _json_scalar_eq(marker.get("correction_id"), ev.get("correction_id")):
            return False
        if not _json_scalar_eq(marker.get("correction_class"), ev.get("correction_class")):
            return False
        if verify is not None:
            # P23-03 / V23-GPT-03: verify the event's TOP-LEVEL correction signature over the SAME payload
            # the runtime submit_amendment path uses -- canonical_bytes of every field EXCEPT "signature"
            # (including the full adjudicators). Using a different payload rejected runtime-valid events and
            # accepted runtime-rejected ones. The adjudicator signatures are then verified over the reduced
            # identity payload as before.
            top_payload = {k: v for k, v in ev.items() if k != "signature"}
            if verify("correction", canonical_bytes(top_payload), ev.get("signature")) is not True:
                return False
            adj_payload = {k: v for k, v in ev.items() if k not in ("adjudicators", "signature")}
            adj_payload["adjudicators"] = [{"adjudicator_id": a.get("adjudicator_id"),
                                            "control_domain": a.get("control_domain")} for a in ev["adjudicators"]]
            for a in ev["adjudicators"]:
                # V26-GPT (P2): mirror the runtime submit_amendment binding -- each adjudicator's signature
                # kid MUST equal its adjudicator_id. Without this, an offline marker bound to an event whose
                # adjudicator signatures are cross-attributed (valid signature, wrong kid) armed offline while
                # the runtime rejects it E-AMENDMENT-KID-MISMATCH.
                _sig = a.get("signature")
                if not isinstance(_sig, dict) or not _json_scalar_eq(_sig.get("kid"), a.get("adjudicator_id")):
                    return False
                if verify("adjudicator", canonical_bytes(adj_payload), a.get("signature")) is not True:
                    return False
        return True
    except Exception:
        return False


def _is_acceptance_marker(rec: Dict[str, Any]) -> bool:
    """Structural validity of a gate-issued bssg.correction-accepted MARKER. Arming ALSO requires the
    marker be bound to a present accepted-LIFT correction-event (see _marker_bound); a well-formed marker
    alone no longer arms the carve-out.
    V30 K32-04 FIX: validates licensed_epoch, spec_version, and gate_version. A marker with missing or
    wrong-typed metadata is not structurally valid and must not arm the X7U branch."""
    try:
        if not isinstance(rec, dict) or rec.get("record_type") != "bssg.correction-accepted":
            return False
        if rec.get("correction_class") != "LIFT_TERMINAL_STATE":
            return False
        if not isinstance(rec.get("session_id"), str) or not rec.get("session_id"):
            return False
        ep = rec.get("authority_epoch")
        if not isinstance(ep, int) or isinstance(ep, bool):
            return False
        if not isinstance(rec.get("correction_digest"), str):
            return False
        # K32-04: validate licensed_epoch (integer, non-bool), spec_version (string), gate_version (string)
        le = rec.get("licensed_epoch")
        if not isinstance(le, int) or isinstance(le, bool):
            return False
        if not isinstance(rec.get("spec_version"), str) or not rec.get("spec_version"):
            return False
        if not isinstance(rec.get("gate_version"), str) or not rec.get("gate_version"):
            return False
        av = rec.get("adjudicators_verified")
        return isinstance(av, int) and not isinstance(av, bool) and av >= 2
    except Exception:
        return False


def _authority_view(rec: Dict[str, Any]) -> Tuple[Optional[str], Optional[int], Optional[Dict[str, Any]]]:
    """A: read the canonical authority triple from a REAL record (top-level, falling back to the nested
    authorization receipt for externally-produced records)."""
    if not isinstance(rec, dict):
        return None, None, None
    sess = rec.get("session_id")
    ep = rec.get("authority_epoch")
    snap = rec.get("authority_snapshot")
    receipt = rec.get("authorization_receipt")
    if isinstance(receipt, dict):
        if not isinstance(sess, str):
            sess = receipt.get("session_id")
        if not isinstance(ep, int) or isinstance(ep, bool):
            ep = receipt.get("authority_epoch")
        if not isinstance(snap, dict):
            snap = receipt.get("authority_snapshot")
    return sess, ep, snap


def grants_from_state(gate) -> Dict[str, Dict[str, Any]]:
    """B (V28): export the runtime's AUTHENTICATED amendment grant ledger. Under the V29 withdrawal (SHV
    Axiom 5 evidence-independence), this grant is INERT for the offline verdict -- the offline checker reports
    armed re-widens as X7U (uncertifiable-offline) regardless of whether a grant is present, absent, or forged.
    The grant is retained for runtime diagnostics, future online verification, and signature compatibility.
    Callers may still pass it as check_authority_history(records, grants=grants_from_state(gate)); the checker
    ignores it for the offline verdict but preserves the API shape for forward compatibility."""
    out: Dict[str, List[Dict[str, Any]]] = {}
    try:
        for sess, gl in dict(getattr(gate.state, "amendment_grants", {})).items():
            # V29 GPT-P30-02: a session's grants are a LEDGER (one per accepted amendment). Export the full
            # list so the checker can authenticate each re-widen against ITS landing amendment's grant. A legacy
            # single-dict value is normalized to a one-element list.
            _gl = gl if isinstance(gl, list) else ([gl] if isinstance(gl, dict) else [])
            out[sess] = [{
                "correction_digest": g.get("correction_digest"),
                "landing_epoch": g.get("landing_epoch"),
                "restored_effects": frozenset(g.get("restored_effects") or ()),
                "restored_targets": frozenset(g.get("restored_targets") or ()),
            } for g in _gl if isinstance(g, dict)]
    except Exception:
        return {}
    return out


def check_authority_history(records: List[Dict[str, Any]], verify=None, grants=None) -> List[str]:
    """X7 (authority monotonicity on the REAL record stream). TOTAL: a malformed record never crashes
    the check; it is skipped or flagged, never raised on (K18-12). Optional `verify` is an adjudicator
    signature-verification callable; when supplied, an amendment marker arms only if the bound
    correction-event's signatures verify (GPT-P2). Within each session:
      - authority_epoch is monotone non-decreasing (regression is X7);
      - at a CONSTANT epoch the ceiling MUST NOT change (change without an epoch bump is X7);
      - at a strictly HIGHER epoch the ceiling MUST NOT WIDEN (equal or narrower is fine), UNLESS an
        accepted-LIFT amendment intervened, which licenses ONE re-widening consumed only by the next
        record carrying a ceiling snapshot (A1);
      - the carve-out arms ONLY from a gate-issued correction-accepted MARKER that is BOUND to a present
        accepted-LIFT correction-event (A2/GPT-P2); a bare or unbound marker does not arm;
      - top-level and nested-receipt authority triples must agree type-strictly (A3); a settlement
        execution receipt must carry a resolvable revalidation.authority_epoch (A4/GPT-P3)."""
    violations: List[str] = []
    last: Dict[str, Any] = {}
    amendment_reset: set = set()
    receipt_epoch: Dict[str, Any] = {}  # authorization_receipt_digest -> authority_epoch (A4)
    if records is None:
        return violations   # truly absent input -> no records, no violation
    # V23-GPT-01: strict-materialize FIRST -- do not run a lenient isinstance(list) pre-guard, or a non-list
    # outer sequence (a tuple, a generator-backed object) with visible violations slips past before the
    # boundary. Any input that is not an exact list of exact JSON values fails closed here.
    records = _strict_copy(records)
    if records is _UNCOPYABLE_INPUT or not isinstance(records, list):
        return ["X7"]   # P23-01: a non-exact / hostile input fails closed, never returns clean
    # GPT-P21-02: index correction-events IN STREAM ORDER as they are encountered (not a whole-stream
    # pre-pass), so a marker can only bind to an event that already appeared before it -- a future event
    # can no longer retroactively excuse an earlier widening. `consumed_corrections` tracks digests that
    # have already armed the carve-out, so a duplicate/replayed marker cannot re-arm one correction to
    # license multiple widenings.
    correction_events: Dict[str, Any] = {}
    consumed_corrections: set = set()

    epoch_floor: Dict[str, Any] = {}       # session -> minimum epoch subsequent records may carry (P23-02)
    # V30 K32-05: marker_cd tracks the correction_digest each session's marker claims, used for
    # marker consumption bookkeeping (pop on X7U). The grants parameter is INERT for the offline
    # verdict (V29 withdrawal); marker_cd is retained for marker-consumption tracking only.
    marker_cd: Dict[str, Any] = {}
    for rec in records:
        if not isinstance(rec, dict):
            continue
        rtype = rec.get("record_type")

        # V26-GPT (P5): a PRESENT but wrong-typed authority_epoch (float/str/bool) or session_id (non-str) is
        # tampering on ANY record and fails closed HERE, before the record-type-specific `continue` branches.
        # Previously this check lived only in the generic snapshot path, so an execution-receipt (or any
        # reserved-type record) carrying a float epoch/session laundered past it. A truly ABSENT field (None)
        # is not flagged; the type-specific handlers below still run for well-typed reserved records.
        _pe, _ps = rec.get("authority_epoch"), rec.get("session_id")
        if (_pe is not None and (not isinstance(_pe, int) or isinstance(_pe, bool))) or (_ps is not None and not isinstance(_ps, str)):
            violations.append("X7")
            continue

        if rtype == "bssg.correction-event":
            try:
                correction_events[digest(rec)] = rec   # observed at this position; later markers may bind
            except Exception:
                pass
            continue
        if rtype == "bssg.correction-accepted":
            # A2 (GPT-P2 / GPT-P21-01/02): a marker arms only if well-formed, bound to an EARLIER
            # accepted-LIFT event with matching identity, and its correction has not already been consumed.
            cd = rec.get("correction_digest")
            m_sess = rec.get("session_id")
            m_ep = rec.get("authority_epoch")
            if (_is_acceptance_marker(rec) and cd not in consumed_corrections
                    and _marker_bound(rec, correction_events, verify)):
                # V26-GPT/GLM/Kimi X7-2 (BLOCKER): the license LANDING epoch is DERIVED, never trusted from
                # the marker. Pass-27 read it straight from rec["licensed_epoch"], but that field is
                # UNAUTHENTICATED offline -- a stream-tampered marker declaring licensed_epoch=50 licensed a
                # widening at epoch 50 (defeating V23-GPT-02), and declaring licensed_epoch=marker_epoch
                # re-opened the K26-X7-1 fail-open. The honest landing is deterministically marker_epoch+1
                # (the runtime's post-amendment re-bump). The checker DERIVES that and ARMS only for a marker
                # whose declared licensed_epoch is PRESENT and EQUALS marker_epoch+1; any other value (or a
                # non-int marker epoch) does not arm, so the subsequent widening is caught as X7. The field is
                # thus a tamper-CHECK, not a free dial: it cannot move the license.
                # V27-GPT/GLM/Kimi X7 (BLOCKER): the marker's authority_epoch is ALSO unauthenticated. Pass-28
                # bound licensed_epoch to marker_epoch+1, but an attacker who controls the offline stream moves
                # BOTH fields together (ep=49, le=50), relocating the landing to any epoch. The landing is now
                # bound to the checker's OWN tracked state, not the marker's self-declared epoch: the amendment
                # bumps the session by exactly one, so the marker's authority_epoch MUST equal the session's
                # last established (non-marker) epoch + 1. A marker whose epoch is inflated above that does not
                # arm. (Walking the established epoch up via prior narrowings is then caught by the breadth
                # bound on the licensed re-widen below -- a re-widen can only restore authority the session
                # demonstrably held.)
                # B (V28 redesign): the marker's self-declared epoch/licensed_epoch are UNAUTHENTICATED and
                # have been defeated four rounds running (field read -> derived -> dual-field -> walk-up). The
                # checker no longer trusts ANY marker-carried authority. The marker only SIGNALS that the
                # session claims an accepted amendment; the AUTHORITATIVE landing epoch and restored authority
                # come from the runtime's authenticated grant ledger (`grants`), matched by correction_digest
                # at the re-widen below. Without a grant, a claimed re-widen cannot be certified offline.
                amendment_reset.add(m_sess)
                consumed_corrections.add(cd)
                marker_cd[m_sess] = cd

            # GPT-B (pass-23): the marker's OWN authority_epoch is tamper-checked like any record. It must
            # be non-decreasing vs the session's last epoch (a marker epoch below the preceding record is a
            # regression -> X7), and it records the epoch at which the licensed re-widening MUST occur, so an
            # inflated marker epoch (e.g. 999) whose following widening lands at a different epoch is caught.
            if isinstance(m_sess, str) and isinstance(m_ep, int) and not isinstance(m_ep, bool):
                if m_sess in last and m_ep < last[m_sess][0]:
                    violations.append("X7")
                # P23-02: INSTALL the marker's declared epoch as a session floor. Checking it against the
                # preceding record is not enough -- the epoch must also constrain SUBSEQUENT records, or a
                # marker can declare epoch 999, a later record can regress to epoch 6, and the widening at
                # 999 still reports clean. Any subsequent record below the floor is now X7.
                epoch_floor[m_sess] = max(epoch_floor.get(m_sess, m_ep), m_ep)
            continue

        if rtype == "bssg.execution-receipt":
            # A4 (GPT-P19-02 / K19-C1): bind the commit's asserted epoch to the receipt it redeems, and
            # FAIL CLOSED -- a present revalidation.authority_epoch whose receipt digest does not resolve,
            # or resolves to a different epoch, is X7 (an unresolved binding is not silently skipped).
            try:
                reval = rec.get("revalidation")
                claimed = reval.get("authority_epoch") if isinstance(reval, dict) else None
                dig = rec.get("authorization_receipt_digest")
                outcome = rec.get("outcome")
                result = reval.get("result") if isinstance(reval, dict) else None
                # GPT-P3 / K20-X1: a SETTLEMENT / PASS execution receipt MUST carry a resolvable
                # revalidation.authority_epoch. Omitting it no longer evades the binding check: a
                # consuming outcome or a PASS revalidation with a missing epoch is X7 (fail closed).
                is_settlement = (outcome in REDEMPTION_OUTCOMES) or (result == "PASS")
                if is_settlement and claimed is None:
                    violations.append("X7")  # settlement receipt omitted its authority-epoch proof
                elif claimed is not None:
                    if dig in receipt_epoch:
                        if not _json_scalar_eq(receipt_epoch[dig], claimed):
                            violations.append("X7")
                    else:
                        violations.append("X7")  # unresolved epoch binding -> fail closed
            except Exception:
                violations.append("X7")
            continue

        # A3 (GPT-P19-02 / K19-B1): if both the top-level and the nested receipt carry authority data, the
        # FULL triple must agree under TYPE-STRICT equality; a divergence on session, epoch, or snapshot --
        # including a wrong-type value (True aliasing 1), a null counterpart, or a non-dict snapshot facing
        # a dict one -- is tampering of one copy and is X7.
        _rcpt = rec.get("authorization_receipt")
        if isinstance(_rcpt, dict):
            for fld in ("session_id", "authority_epoch"):
                top, nested = rec.get(fld), _rcpt.get(fld)
                if top is None and nested is None:
                    continue
                if not _json_scalar_eq(top, nested):
                    violations.append("X7")
            top, nested = rec.get("authority_snapshot"), _rcpt.get("authority_snapshot")
            if not (top is None and nested is None):
                if not (isinstance(top, dict) and isinstance(nested, dict) and _auth_equal(top, nested)):
                    violations.append("X7")

        sess, ep, snap = _authority_view(rec)
        # A4: remember the epoch bound to this record's receipt digest (for later execution receipts).
        if isinstance(_rcpt, dict) and isinstance(ep, int) and not isinstance(ep, bool):
            try:
                receipt_epoch[digest(_rcpt)] = ep
            except Exception:
                pass

        # A3 (K25-A3): a PRESENT but wrong-typed authority field (float/str/bool epoch, non-str session)
        # is tampering and fails closed -- it must not be silently skipped, or a regression/widening carried
        # on a float epoch launders. A truly ABSENT field (value None) is skipped as before.
        ep_bad = ep is not None and (not isinstance(ep, int) or isinstance(ep, bool))
        sess_bad = sess is not None and not isinstance(sess, str)
        if ep_bad or sess_bad:
            violations.append("X7")
            continue
        if not isinstance(sess, str) or not isinstance(ep, int) or isinstance(ep, bool):
            continue
        # P23-02: a record below the floor a prior marker installed is an epoch regression -> X7.
        if sess in epoch_floor and ep < epoch_floor[sess]:
            violations.append("X7")
        if sess in last:
            prev_ep, prev_snap = last[sess]
            # V23-GPT-02 + V28 B + V30 WITHDRAWAL: the armed re-widen branch. Under the V29 withdrawal
            # (SHUDP Axiom 5), armed forward re-widens are X7U (uncertifiable-offline). The grants parameter
            # is INERT; no positive certification path exists. Grant-independent violations (epoch regression,
            # constant-epoch ceiling change, type-tamper, unlicensed widening) remain X7 and are evaluated
            # BEFORE the X7U branch so they cannot be swallowed by it.
            # V30 GPT-P32-01 FIX (same-epoch over-withdrawal): same-epoch ceiling change is a
            # grant-INDEPENDENT violation (spec §20.4: "at a CONSTANT epoch the ceiling MUST NOT change").
            # It must remain X7 even when the session is armed. The pre-V30 guard `ep >= prev_ep` swallowed
            # same-epoch cases into X7U before the constant-epoch comparison could fire. Fix: evaluate
            # same-epoch equality and ep < prev_ep FIRST, before the armed-forward check.
            #
            # V30 K32-03 FIX (malformed snapshot -> clean): a non-dict or absent authority_snapshot in
            # ANY record is a grant-independent type-tamper -> X7. The pre-V30 `isinstance(snap, dict)` guard
            # silently skipped these records, letting them audit clean. Fix: check snapshot typing first.
            if snap is not None and not isinstance(snap, dict):
                # K32-03: a PRESENT but non-dict authority_snapshot (string, int, list, bool) is
                # grant-independent type-tamper -> X7. An ABSENT snapshot (None or key missing) means
                # the record does not carry authority and is skipped for widening analysis (e.g. a
                # snapshot-less deny between an amendment and a re-widen is structurally neutral).
                violations.append("X7")
            elif not isinstance(snap, dict):
                pass  # absent snapshot -- skip this record for widening analysis
            elif ep < prev_ep:
                violations.append("X7")
            elif ep == prev_ep:
                # GPT-P32-01: constant-epoch ceiling change is X7 regardless of armed status.
                # A same-epoch EQUAL snapshot after an armed marker is consumed as X7U (the re-widen
                # that is being tracked may still be pending at the next record).
                if isinstance(prev_snap, dict) and not _auth_equal(snap, prev_snap):
                    violations.append("X7")  # ceiling change without an epoch bump -- grant-independent
                elif sess in amendment_reset:
                    # Armed, same epoch, snapshot unchanged (or no prev snapshot to compare) -- consume
                    # the marker as X7U. This preserves the honest-recovery path where the re-widen
                    # snapshot can equal a prior snapshot.
                    amendment_reset.discard(sess)
                    marker_cd.pop(sess, None)
                    violations.append("X7U")
            elif (sess in amendment_reset and ep > prev_ep):
                # Armed, strictly forward epoch: the ONLY X7U case.
                # V29 WITHDRAWAL (SHUDP Axiom 5 evidence-independence + SHVVP §0.3 withdrawal precedent):
                # the offline checker no longer CERTIFIES a licensed re-widen as clean. The runtime grant
                # is a CALLER-SUPPLIED input -- WithinAuth of whoever supplies it -- so it is not an
                # independent witness and cannot discharge the license offline. Per A5's no-default rule
                # the honest verdict for an armed FORWARD re-widen is NOT-EVALUABLE offline: reported
                # UNCERTIFIABLE (X7U). Legitimacy is established ONLY online, by the runtime whose
                # authority-INTRODUCTION invariant is proven over bounded schedules (bssg_model_check
                # BOUNDED-AUTH-INTRO). Grant-INDEPENDENT divergences -- epoch regression, constant-epoch
                # ceiling change, type-tamper -- still fail closed as X7 in the branches above. The
                # `grants` parameter is retained for signature compatibility but no longer affects the
                # offline verdict.
                amendment_reset.discard(sess)
                marker_cd.pop(sess, None)
                violations.append("X7U")
            elif ep > prev_ep and isinstance(prev_snap, dict):
                if not _auth_subset(snap, prev_snap):
                    violations.append("X7")  # widening at a higher epoch without a matching amendment
        carry = snap if isinstance(snap, dict) else last.get(sess, (0, None))[1]
        last[sess] = (ep, carry)
    return violations


def _load_outcome_enum() -> frozenset:
    """B2 (K18-10 / GPT-05): the execution-receipt outcome enum is the single source of truth for X4
    redemption roles; it is READ from the schema at import rather than hand-listed, so the set cannot
    silently drift from the schema on a future revision. Fail-safe: if the schema cannot be read, fall
    back to the known v0.1 enum (and REDEMPTION_OUTCOMES is asserted non-empty below)."""
    try:
        import os as _os
        p = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "schemas", "execution-receipt.schema.json")
        enum = json.load(open(p))["properties"]["outcome"]["enum"]
        if isinstance(enum, list) and enum:
            return frozenset(enum)
    except Exception:
        pass
    return frozenset({"COMMITTED_PENDING_OUTCOME", "SUCCEEDED", "FAILED_NO_EFFECT", "INDETERMINATE", "QUARANTINED"})


OUTCOME_ENUM = _load_outcome_enum()
REDEMPTION_PENDING = "COMMITTED_PENDING_OUTCOME"
NON_CONSUMING_OUTCOMES = frozenset({"FAILED_NO_EFFECT"})
# A redemption is any schema outcome that CONSUMED the token (the enum minus the non-consuming ones),
# DERIVED from the schema so it tracks future additions. COMMITTED_PENDING_OUTCOME is the pending
# redemption; the remaining consuming outcomes are its settlements.
REDEMPTION_OUTCOMES = OUTCOME_ENUM - NON_CONSUMING_OUTCOMES
REDEMPTION_SETTLED = REDEMPTION_OUTCOMES - frozenset({REDEMPTION_PENDING})
assert REDEMPTION_OUTCOMES, "REDEMPTION_OUTCOMES derived from the schema enum must be non-empty"


def check_single_redemption(executions: List[Dict[str, Any]]) -> List[str]:
    """X4 (redeemed at most once). TOTAL: a malformed record never crashes the check (K18-12). A
    redemption is a CONSUMING outcome (the schema enum minus FAILED_NO_EFFECT), DERIVED from the schema.
    Per-token state machine (spec 368: COMMITTED_PENDING_OUTCOME -> {SUCCEEDED|FAILED_NO_EFFECT|
    INDETERMINATE|QUARANTINED}, all terminal):
      - COMMITTED_PENDING_OUTCOME: None -> PENDING; a second commit on a PENDING/SETTLED token is X4.
      - a settlement (SUCCEEDED/INDETERMINATE/QUARANTINED): None -> SETTLED (direct settlement, one
        redemption); PENDING -> SETTLED (settles it, same redemption); SETTLED -> X4 (second settlement).
      - FAILED_NO_EFFECT: standalone (None) consumes nothing; AFTER a PENDING it is the TERMINAL
        settlement of the already-consumed token -> SETTLED, so a later SUCCEEDED on that token is X4
        (B1/GPT-05: the two contradictory terminal outcomes are caught); on a SETTLED token it is X4.
      - an outcome outside the schema enum is a malformed redemption log -> X4 (B2/K18-10: e.g. a
        lowercase 'succeeded' is no longer silently skipped)."""
    violations: List[str] = []
    state: Dict[str, str] = {}  # token_id -> "PENDING" | "SETTLED"
    if executions is None:
        return violations   # truly absent input -> no executions, no violation
    # V23-GPT-01: strict-materialize FIRST (no lenient isinstance pre-guard), so a tuple / non-list outer
    # sequence carrying a double redemption fails closed instead of returning clean.
    executions = _strict_copy(executions)
    if executions is _UNCOPYABLE_INPUT or not isinstance(executions, list):
        return ["X4"]   # P23-01: a non-exact / hostile input fails closed, never returns clean
    for ex in executions:
        if not isinstance(ex, dict):
            continue
        tid = ex.get("commit_token_id")
        outcome = ex.get("outcome")
        if tid is None or outcome is None:
            continue
        # GPT-P1 / K20-L1 / K21-A2: FAIL CLOSED, not skip. The token id is canonicalized to a stable
        # hashable key so a double redemption is caught even when the id is unhashable (list/dict) OR a
        # float. ONLY str and int keep their raw identity; a FLOAT (NaN/inf are distinct objects that never
        # collide as dict keys) and every non-scalar go through json.dumps, so two NaN ids map to the same
        # "NaN" key and a double redemption on a NaN token id is caught instead of laundered across a
        # multi-shard merge. (The type-confusion class DOES reach X4 via floats -- pass-21's note was wrong.)
        try:
            if isinstance(tid, bool):
                tid = json.dumps(tid)
            elif isinstance(tid, float) and tid.is_integer():
                tid = int(tid)                          # A1 (K25-A1): 1.0 collides with int 1, one keyspace
            elif not isinstance(tid, (str, int)):
                tid = json.dumps(tid, sort_keys=True)
        except Exception:
            tid = repr(tid)
        # A2 (K25-A2): the outcome must be a str to be a schema-enum member. A list/dict/other outcome is
        # unhashable and would raise on `outcome in OUTCOME_ENUM`; guard the TYPE first and fail closed
        # (malformed redemption log) instead of crashing.
        if not isinstance(outcome, str):
            violations.append("X4")
            continue
        if outcome not in OUTCOME_ENUM:
            violations.append("X4")   # outcome outside the schema enum -- malformed redemption log
            continue
        st = state.get(tid)
        if outcome == REDEMPTION_PENDING:
            if st is not None:            # a second commit on an already-spent token
                violations.append("X4")
            else:
                state[tid] = "PENDING"
        elif outcome in NON_CONSUMING_OUTCOMES:
            if st == "PENDING":
                state[tid] = "SETTLED"    # terminal settlement of the pending redemption
            elif st == "SETTLED":
                violations.append("X4")   # an outcome after a terminal settlement is contradictory
            # st is None: a standalone failed attempt consumes nothing
        else:  # a consuming settlement outcome
            if st == "SETTLED":
                violations.append("X4")   # a second settlement is a second redemption
            else:
                state[tid] = "SETTLED"    # None or PENDING -> settled (one redemption)
    return violations


def check_lineage_completeness(lineage: Dict[str, Any]) -> List[str]:
    """X6: declared gaps forbid a COMPLETE completeness claim."""
    violations: List[str] = []
    if not isinstance(lineage, dict):
        return ["X6"]                      # non-total guard: a non-dict lineage fails closed, never raises
    gaps = lineage.get("declared_gaps")
    if lineage.get("completeness") == "COMPLETE" and gaps:
        violations.append("X6")
    node_ids = {n.get("node_id") for n in lineage.get("nodes", []) if isinstance(n, dict)}
    for node in lineage.get("nodes", []):
        if not isinstance(node, dict):
            violations.append("X6b")
            continue
        for parent in node.get("parents", []):
            if parent not in node_ids and lineage.get("completeness") == "COMPLETE":
                violations.append("X6c")
    return violations


if __name__ == "__main__":  # pragma: no cover
    print("BSSG reference gate %s, spec version %s" % (GATE_VERSION, SPEC_VERSION))
    print("DRAFT / NOT CARRIED. No effectiveness claim is made by this software.")

---

# Bismillah ir-Rahman ir-Rahim
