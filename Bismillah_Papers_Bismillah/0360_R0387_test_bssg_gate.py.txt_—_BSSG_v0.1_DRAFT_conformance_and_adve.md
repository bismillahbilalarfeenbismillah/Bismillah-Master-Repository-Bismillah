# Bismillah ir-Rahman ir-Rahim

# R0387 -- test_bssg_gate.py.txt — BSSG v0.1 DRAFT conformance and adversarial test suite.

**Chronological Index:** 360 of 995  
**Date:** 2026-07-25  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** test_bssg_gate.py.txt  
**Source Format:** txt  
**SHA-256:** `b9ad36116b7cc84d00bd6b874f0aa2e2e83a76eea138f0482f7114d22638b138`  

---

## R0387 · test_bssg_gate.py.txt — BSSG v0.1 DRAFT conformance and adversarial test suite.

- section: V. BSSG & SHVVP Protocols
- source_file: test_bssg_gate.py.txt
- source_format: txt
- merged_variants: 3 (test_bssg_gate.py)
- text_sha256: b9ad36116b7cc84d00bd6b874f0aa2e2e83a76eea138f0482f7114d22638b138

#!/usr/bin/env python3
"""
BSSG v0.1 DRAFT conformance and adversarial test suite.

Deterministic by construction: injected clock, injected token factory,
injected signature verifier, no randomness, no network, no wall-clock reads.

Two families of tests:

  1. KernelTruthTableTests: the exhaustive 3^5 = 243 kernel truth states.
     ALLOW occurs if and only if all five conjuncts are TRUE. FALSE dominates
     UNKNOWN in the reason classification, and UNKNOWN never satisfies.

  2. Adversarial and protocol tests: TOCTOU, replay, rollback, double-spend,
     forged and mismatched receipts, colluding but apparently healthy witness
     (an architectural limitation test, NOT an assurance test), stale clocks,
     authority widening on witness degradation, confused deputy, target
     aliasing and canonicalization, extra fields, malformed input, fail-closed
     recovery, descendant correction gaps, and terminal state transitions.

No test in this file asserts, implies, or measures effectiveness.
"""

from __future__ import annotations

import itertools
import json
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bssg_gate as G

try:  # optional
    import jsonschema

    HAVE_JSONSCHEMA = True
except Exception:  # pragma: no cover
    jsonschema = None
    HAVE_JSONSCHEMA = False

SCHEMA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "schemas")
SCHEMA_FILES = (
    "effect-request.schema.json",
    "authorization-receipt.schema.json",
    "witness-receipt.schema.json",
    "execution-receipt.schema.json",
    "correction-event.schema.json",
    "lineage-record.schema.json",
)


def load_schema(name):
    with open(os.path.join(SCHEMA_DIR, name), "r", encoding="utf-8") as handle:
        return json.load(handle)


# ---------------------------------------------------------------------------
# Deterministic fixtures
# ---------------------------------------------------------------------------

BASE_TIME = G.parse_rfc3339_utc("2026-07-25T12:00:00Z")
ADAPTER_DIGEST = G.digest_bytes(b"adapter-v1")
PARAMS_DIGEST = G.digest_bytes(b"params-v1")


def signature(status="valid", kid="k1"):
    return {
        "alg": "test-alg",
        "kid": kid,
        "envelope": "detached-json",
        "canonicalization": G.CANONICALIZATION_ID,
        "signature_b64": status,
        "verification_status": "verified_by_injected_verifier",
    }


def injected_verifier(kind, payload_bytes, sig):
    """
    Models signature verification. Returns True, False, or None (UNKNOWN).

    This callable establishes nothing about key custody, key distribution, or
    whether the signing key is genuinely outside the subject's authority.
    """
    del kind, payload_bytes
    value = sig.get("signature_b64")
    if value == "valid":
        return True
    if value == "invalid":
        return False
    return None


class Clock:
    def __init__(self, start=BASE_TIME):
        self.now = start

    def __call__(self):
        return self.now

    def advance(self, seconds):
        self.now += seconds


class Tokens:
    def __init__(self):
        self.counter = 0

    def __call__(self):
        self.counter += 1
        return "token-%08d" % self.counter


def policy_body():
    return {"policy_id": "pol-1", "revision": 3, "release_class": "internal"}


def contract_body(policy_digest, degraded_effects=None, degraded_targets=None):
    return {
        "contract_id": "ctr-1",
        "subject_id": "agent-1",
        "policy_digest": policy_digest,
        "not_after": "2026-12-31T00:00:00Z",
        "allowed_effects": ["READ", "WRITE"],
        "degraded_effects": ["READ"] if degraded_effects is None else degraded_effects,
        "allowed_target_scopes": ["https://db.example.internal/records/"],
        "degraded_target_scopes": ["https://db.example.internal/records/"]
        if degraded_targets is None
        else degraded_targets,
        "target_classes": ["datastore"],
        "effect_registry": {
            "READ": {"adapter_digest": ADAPTER_DIGEST},
            "WRITE": {"adapter_digest": ADAPTER_DIGEST},
        },
    }


def build_registries(**kwargs):
    policy = policy_body()
    policy_digest = G.digest(policy)
    contract = contract_body(policy_digest, **kwargs)
    contract_digest = G.digest(contract)
    return (
        {contract_digest: {"body": contract, "revoked": False}},
        {policy_digest: {"body": policy}},
        contract_digest,
        policy_digest,
    )


def witness_receipt(
    health="HEALTHY",
    epoch=7,
    sequence=11,
    subject="agent-1",
    within_auth="outside_subject_authority",
    admin="false-explicit",
    observed_at="2026-07-25T11:59:55Z",
    expires_at="2026-07-25T12:05:00Z",
    sig_status="valid",
    control_domain="witness-domain",
    subject_domain="subject-domain",
):
    if admin == "false-explicit":
        admin_value = False
    elif admin == "unknown":
        admin_value = "unknown"
    else:
        admin_value = True
    return {
        "record_type": "bssg.witness-receipt",
        "spec_version": G.SPEC_VERSION,
        "witness_id": "witness-1",
        "covered_subject": subject,
        "covered_subject_domain": subject_domain,
        "covered_effect_classes": ["datastore"],
        "independence_declaration": {
            "control_domain": control_domain,
            "subject_can_administer": admin_value,
            "basis": "operator-declared control graph review CGR-001",
        },
        "within_auth_assessment": {
            "value": within_auth,
            "method": "control-graph-review",
            "assessor": "operator-ops",
        },
        "epoch": epoch,
        "sequence": sequence,
        "checkpoint": {
            "origin": "bssg.witness.example",
            "tree_size": 42,
            "root_hash": G.digest_bytes(b"root-42"),
        },
        "health": health,
        "observed_at": observed_at,
        "expires_at": expires_at,
        "signature": signature(sig_status, kid="witness-key-1"),
    }


def time_authority(
    anchor="2026-07-25T12:00:00Z", skew=5, kind="external_signed_anchor", sig="valid"
):
    return {
        "authority_id": "time-anchor-1",
        "kind": kind,
        "anchor_time": anchor,
        "max_skew_seconds": skew,
        "signature": signature(sig, kid="time-key-1"),
    }


def evidence_bundle(receipt=None, epoch=5, authority=None):
    bundle = {
        "witness_receipt": witness_receipt() if receipt is None else receipt,
        "time_authority": time_authority() if authority is None else authority,
        "evidence_epoch": epoch,
    }
    return bundle


def effect_request(
    contract_digest,
    policy_digest,
    effect="WRITE",
    nonce="a" * 32,
    declared="https://db.example.internal/records/row-1",
    canonical=None,
    issued_at="2026-07-25T11:59:58Z",
    expires_at="2026-07-25T12:04:00Z",
    subject="agent-1",
    target_class="datastore",
    adapter=None,
):
    canonical_uri = (
        G.canonical_target(declared) if canonical is None else canonical
    )
    return {
        "record_type": "bssg.effect-request",
        "spec_version": G.SPEC_VERSION,
        "request_id": "req-0001",
        "subject_id": subject,
        "session_id": "sess-0001",
        "contract_digest": contract_digest,
        "policy_digest": policy_digest,
        "effect_type": effect,
        "target": {
            "declared_uri": declared,
            "canonical_uri": canonical_uri,
            "target_class": target_class,
        },
        "params_digest": PARAMS_DIGEST,
        "adapter_digest": ADAPTER_DIGEST if adapter is None else adapter,
        "nonce": nonce,
        "sequence": 1,
        "issued_at": issued_at,
        "expires_at": expires_at,
    }


class GateFixture:
    def __init__(self, **kwargs):
        (
            self.contracts,
            self.policies,
            self.contract_digest,
            self.policy_digest,
        ) = build_registries(**kwargs)
        self.clock = Clock()
        self.tokens = Tokens()
        self.gate = G.BSSGGate(
            contract_registry=self.contracts,
            policy_registry=self.policies,
            clock=self.clock,
            signature_verifier=injected_verifier,
            token_factory=self.tokens,
            max_clock_skew_seconds=5,
            evidence_max_age_seconds=300,
            profile="BSSG-M",
        )

    def request(self, **kwargs):
        return effect_request(self.contract_digest, self.policy_digest, **kwargs)


# ---------------------------------------------------------------------------
# 1. Exhaustive kernel truth table: 3^5 = 243 states
# ---------------------------------------------------------------------------


class KernelTruthTableTests(unittest.TestCase):
    """Generated below: one test method per truth state."""


def _make_kernel_test(assignment):
    values = dict(zip(G.KERNEL_CONJUNCTS, assignment))

    def test(self):
        decision, reasons = G.kernel_decision(values)
        all_true = all(v == G.TRUE for v in assignment)
        any_false = any(v == G.FALSE for v in assignment)
        any_unknown = any(v == G.UNKNOWN for v in assignment)
        if all_true:
            self.assertEqual(decision, G.DECISION_ALLOW)
            self.assertEqual(reasons, [])
        else:
            self.assertNotEqual(decision, G.DECISION_ALLOW)
            self.assertTrue(reasons)
        if any_false:
            self.assertEqual(decision, G.DECISION_DENY_FALSE)
        elif any_unknown:
            self.assertEqual(decision, G.DECISION_DENY_UNKNOWN)
        # UNKNOWN is never satisfied: no assignment containing UNKNOWN allows.
        if any_unknown:
            self.assertNotEqual(decision, G.DECISION_ALLOW)

    return test


_ALLOW_COUNT = 0
for _index, _assignment in enumerate(
    itertools.product(G.TRUTH_VALUES, repeat=len(G.KERNEL_CONJUNCTS))
):
    _name = "test_kernel_%03d_%s" % (
        _index,
        "_".join(v[0] for v in _assignment),
    )
    setattr(KernelTruthTableTests, _name, _make_kernel_test(_assignment))
    if all(v == G.TRUE for v in _assignment):
        _ALLOW_COUNT += 1


class KernelTableShapeTests(unittest.TestCase):
    def test_exactly_243_states_enumerated(self):
        generated = [n for n in dir(KernelTruthTableTests) if n.startswith("test_kernel_")]
        self.assertEqual(len(generated), 243)

    def test_exactly_one_allowing_state(self):
        self.assertEqual(_ALLOW_COUNT, 1)

    def test_kernel_rejects_non_three_valued_input(self):
        values = {name: G.TRUE for name in G.KERNEL_CONJUNCTS}
        values["ContractMatch"] = True  # a Boolean, not a truth value
        with self.assertRaises(G.BSSGError):
            G.kernel_decision(values)

    def test_kernel_rejects_sixth_conjunct_absence_of_required(self):
        values = {name: G.TRUE for name in G.KERNEL_CONJUNCTS}
        del values["EvidenceCurrent"]
        with self.assertRaises(G.BSSGError):
            G.kernel_decision(values)


# ---------------------------------------------------------------------------
# 2. Adversarial and protocol tests
# ---------------------------------------------------------------------------


class HappyPathTests(unittest.TestCase):
    def setUp(self):
        self.fx = GateFixture()

    def test_allow_and_commit(self):
        request = self.fx.request()
        decision = self.fx.gate.authorize(request, evidence_bundle())
        self.assertEqual(decision["decision"], G.DECISION_ALLOW, decision["reason_codes"])
        receipt = decision["authorization_receipt"]
        binding = {
            "request_digest": receipt["request_digest"],
            "canonical_target": receipt["canonical_target"],
            "params_digest": receipt["params_digest"],
            "adapter_digest": receipt["adapter_digest"],
            "effect_type": receipt["effect_type"],
        }
        execution = self.fx.gate.commit(
            receipt["commit_token"]["token_id"], binding, evidence_bundle()
        )
        self.assertEqual(execution["outcome"], "COMMITTED_PENDING_OUTCOME")
        self.assertEqual(execution["revalidation"]["result"], "PASS")

    def test_cross_record_invariants_hold(self):
        request = self.fx.request()
        witness = witness_receipt()
        decision = self.fx.gate.authorize(
            request, evidence_bundle(receipt=witness)
        )
        receipt = decision["authorization_receipt"]
        binding = {
            "request_digest": receipt["request_digest"],
            "canonical_target": receipt["canonical_target"],
            "params_digest": receipt["params_digest"],
            "adapter_digest": receipt["adapter_digest"],
            "effect_type": receipt["effect_type"],
        }
        execution = self.fx.gate.commit(
            receipt["commit_token"]["token_id"], binding, evidence_bundle()
        )
        violations = G.check_cross_record_invariants(
            request, receipt, witness, execution
        )
        self.assertEqual(violations, [])

    def test_cross_record_invariant_detects_target_substitution(self):
        request = self.fx.request()
        witness = witness_receipt()
        decision = self.fx.gate.authorize(request, evidence_bundle(receipt=witness))
        receipt = decision["authorization_receipt"]
        binding = {
            "request_digest": receipt["request_digest"],
            "canonical_target": receipt["canonical_target"],
            "params_digest": receipt["params_digest"],
            "adapter_digest": receipt["adapter_digest"],
            "effect_type": receipt["effect_type"],
        }
        execution = self.fx.gate.commit(
            receipt["commit_token"]["token_id"], binding, evidence_bundle()
        )
        tampered = dict(execution)
        tampered["executed_target_canonical"] = "https://db.example.internal/records/row-9"
        violations = G.check_cross_record_invariants(
            request, receipt, witness, tampered
        )
        self.assertIn("X3c", violations)

    def test_determinism_of_digests(self):
        request = self.fx.request()
        self.assertEqual(G.digest(request), G.digest(json.loads(json.dumps(request))))


class InputDisciplineTests(unittest.TestCase):
    def setUp(self):
        self.fx = GateFixture()

    def assertDenied(self, decision, code):
        self.assertNotEqual(decision["decision"], G.DECISION_ALLOW)
        self.assertIn(code, decision["reason_codes"])

    def test_caller_supplied_derived_boolean_in_request(self):
        request = self.fx.request()
        request["witness_healthy"] = True
        decision = self.fx.gate.authorize(request, evidence_bundle())
        self.assertDenied(decision, "E-CALLER-SUPPLIED-DERIVED-FIELD")

    def test_caller_supplied_derived_boolean_in_evidence(self):
        evidence = evidence_bundle()
        evidence["evidence_current"] = True
        decision = self.fx.gate.authorize(self.fx.request(), evidence)
        self.assertDenied(decision, "E-CALLER-SUPPLIED-DERIVED-FIELD")

    def test_caller_supplied_conjuncts_block(self):
        request = self.fx.request()
        request["conjuncts"] = {n: "TRUE" for n in G.KERNEL_CONJUNCTS}
        decision = self.fx.gate.authorize(request, evidence_bundle())
        self.assertDenied(decision, "E-CALLER-SUPPLIED-DERIVED-FIELD")

    def test_extra_field_rejected(self):
        request = self.fx.request()
        request["priority"] = "high"
        decision = self.fx.gate.authorize(request, evidence_bundle())
        self.assertDenied(decision, "E-EXTRA-FIELD")

    def test_missing_field_rejected(self):
        request = self.fx.request()
        del request["params_digest"]
        decision = self.fx.gate.authorize(request, evidence_bundle())
        self.assertDenied(decision, "E-MISSING-FIELD")

    def test_malformed_timestamp_rejected(self):
        request = self.fx.request(issued_at="2026-07-25 11:59:58")
        decision = self.fx.gate.authorize(request, evidence_bundle())
        self.assertDenied(decision, "E-MALFORMED-TIMESTAMP")

    def test_malformed_timestamp_with_offset_rejected(self):
        request = self.fx.request(issued_at="2026-07-25T06:59:58-05:00")
        decision = self.fx.gate.authorize(request, evidence_bundle())
        self.assertDenied(decision, "E-MALFORMED-TIMESTAMP")

    def test_malformed_nonce_rejected(self):
        request = self.fx.request(nonce="not-a-nonce")
        decision = self.fx.gate.authorize(request, evidence_bundle())
        self.assertDenied(decision, "E-MALFORMED-NONCE")

    def test_non_dict_request_rejected(self):
        decision = self.fx.gate.authorize("not-a-request", evidence_bundle())
        self.assertDenied(decision, "E-MALFORMED-REQUEST")

    def test_non_dict_evidence_rejected(self):
        decision = self.fx.gate.authorize(self.fx.request(), ["evidence"])
        self.assertDenied(decision, "E-MALFORMED-EVIDENCE")

    def test_float_values_are_refused_by_canonicalization(self):
        with self.assertRaises(G.BSSGError):
            G.canonical_bytes({"value": 1.5})

    def test_oversized_integer_refused(self):
        with self.assertRaises(G.BSSGError):
            G.canonical_bytes({"value": 2 ** 60})


class ReplayRollbackTests(unittest.TestCase):
    def setUp(self):
        self.fx = GateFixture()

    def test_nonce_replay_denied_false(self):
        first = self.fx.gate.authorize(self.fx.request(), evidence_bundle())
        self.assertEqual(first["decision"], G.DECISION_ALLOW)
        second = self.fx.gate.authorize(self.fx.request(), evidence_bundle())
        self.assertEqual(second["decision"], G.DECISION_DENY_FALSE)
        self.assertIn("E-NONCE-REPLAY", second["reason_codes"])

    def test_evidence_epoch_rollback_denied(self):
        self.fx.gate.authorize(self.fx.request(), evidence_bundle(epoch=9))
        decision = self.fx.gate.authorize(
            self.fx.request(nonce="b" * 32), evidence_bundle(epoch=4)
        )
        self.assertEqual(decision["decision"], G.DECISION_DENY_FALSE)
        self.assertIn("E-EVIDENCE-EPOCH-ROLLBACK", decision["reason_codes"])

    def test_witness_epoch_rollback_denied(self):
        self.fx.gate.authorize(
            self.fx.request(), evidence_bundle(receipt=witness_receipt(epoch=9))
        )
        decision = self.fx.gate.authorize(
            self.fx.request(nonce="b" * 32),
            evidence_bundle(receipt=witness_receipt(epoch=3)),
        )
        self.assertEqual(decision["decision"], G.DECISION_DENY_FALSE)
        self.assertIn("E-WITNESS-EPOCH-ROLLBACK", decision["reason_codes"])

    def test_witness_sequence_rollback_denied(self):
        self.fx.gate.authorize(
            self.fx.request(),
            evidence_bundle(receipt=witness_receipt(epoch=9, sequence=20)),
        )
        decision = self.fx.gate.authorize(
            self.fx.request(nonce="b" * 32),
            evidence_bundle(receipt=witness_receipt(epoch=9, sequence=2)),
        )
        self.assertEqual(decision["decision"], G.DECISION_DENY_FALSE)
        self.assertIn("E-WITNESS-SEQUENCE-ROLLBACK", decision["reason_codes"])

    def test_stale_evidence_denied(self):
        request = self.fx.request(
            issued_at="2026-07-25T11:00:00Z", expires_at="2026-07-25T13:00:00Z"
        )
        decision = self.fx.gate.authorize(request, evidence_bundle())
        self.assertEqual(decision["decision"], G.DECISION_DENY_FALSE)
        self.assertIn("E-EVIDENCE-STALE", decision["reason_codes"])

    def test_expired_request_denied(self):
        request = self.fx.request(
            issued_at="2026-07-25T11:59:00Z", expires_at="2026-07-25T11:59:30Z"
        )
        decision = self.fx.gate.authorize(request, evidence_bundle())
        self.assertEqual(decision["decision"], G.DECISION_DENY_FALSE)
        self.assertIn("E-REQUEST-EXPIRED", decision["reason_codes"])


class ClockAndFreshnessTests(unittest.TestCase):
    def setUp(self):
        self.fx = GateFixture()

    def test_baseexception_clock_fails_closed_not_escape(self):
        # V29 (7th-round finding): the authorize fail-closed boundary catches BaseException, not only
        # Exception, so a misbehaving/hostile injected clock that raises a NON-Exception BaseException fails
        # CLOSED to a determinate abort rather than escaping the gate uncaught. Reverting the boundary to
        # `except Exception` makes this test fail (the BaseException propagates out of authorize).
        class _EvilBase(BaseException):
            pass
        self.fx.gate.authorize(self.fx.request(nonce="1" * 32), evidence_bundle())
        self.fx.gate.clock = lambda: (_ for _ in ()).throw(_EvilBase("hostile clock"))
        decision = self.fx.gate.authorize(self.fx.request(nonce="2" * 32), evidence_bundle())
        self.assertIn(decision["decision"], (G.DECISION_DENY_UNKNOWN, G.DECISION_DENY_FALSE))
        self.assertNotEqual(decision["decision"], G.DECISION_ALLOW)

    def test_keyboardinterrupt_and_systemexit_are_not_swallowed(self):
        # the fail-closed boundary must NOT swallow process-control signals into a DENY; they propagate.
        for _sig in (KeyboardInterrupt, SystemExit):
            fx = GateFixture()
            fx.gate.authorize(fx.request(nonce="1" * 32), evidence_bundle())
            fx.gate.clock = lambda _s=_sig: (_ for _ in ()).throw(_s())
            with self.assertRaises(_sig):
                fx.gate.authorize(fx.request(nonce="2" * 32), evidence_bundle())

    def test_baseexception_during_abort_recovery_fails_closed(self):
        # V29 (one-level-deeper completion of the boundary fix): a BaseException raised by an injected
        # dependency DURING abort recovery (e.g. the witness evaluator or the structural contract read) must
        # ALSO fail closed, not escape. Reverting any recovery-region catch to `except Exception` re-opens the
        # escape and makes this test error.
        class _EvilBase(BaseException):
            pass
        for _attr in ("_witness_healthy", "_contract_structural"):
            fx = GateFixture()
            fx.gate.authorize(fx.request(nonce="1" * 32), evidence_bundle())
            fx.gate.clock = lambda: (_ for _ in ()).throw(RuntimeError("first-clock fault"))  # force the abort
            setattr(fx.gate, _attr, lambda *a, **k: (_ for _ in ()).throw(_EvilBase("hostile during recovery")))
            decision = fx.gate.authorize(fx.request(nonce="2" * 32), evidence_bundle())
            self.assertNotEqual(decision["decision"], G.DECISION_ALLOW)
            self.assertIn(decision["decision"], (G.DECISION_DENY_UNKNOWN, G.DECISION_DENY_FALSE))

    def test_missing_time_authority_yields_unknown(self):
        evidence = evidence_bundle()
        del evidence["time_authority"]
        decision = self.fx.gate.authorize(self.fx.request(), evidence)
        self.assertEqual(decision["decision"], G.DECISION_DENY_UNKNOWN)
        self.assertIn("E-TIME-AUTHORITY-ABSENT", decision["reason_codes"])

    def test_undeclared_time_authority_kind_yields_unknown(self):
        evidence = evidence_bundle(authority=time_authority(kind="local_clock"))
        decision = self.fx.gate.authorize(self.fx.request(), evidence)
        self.assertEqual(decision["decision"], G.DECISION_DENY_UNKNOWN)
        self.assertIn("E-TIME-AUTHORITY-UNDECLARED", decision["reason_codes"])

    def test_stale_clock_beyond_declared_skew_yields_unknown(self):
        evidence = evidence_bundle(
            authority=time_authority(anchor="2026-07-25T11:50:00Z", skew=5)
        )
        decision = self.fx.gate.authorize(self.fx.request(), evidence)
        self.assertEqual(decision["decision"], G.DECISION_DENY_UNKNOWN)
        self.assertIn("E-CLOCK-AMBIGUOUS", decision["reason_codes"])

    def test_unverifiable_time_anchor_signature_yields_unknown(self):
        evidence = evidence_bundle(authority=time_authority(sig="indeterminate"))
        decision = self.fx.gate.authorize(self.fx.request(), evidence)
        self.assertEqual(decision["decision"], G.DECISION_DENY_UNKNOWN)
        self.assertIn("E-TIME-ANCHOR-SIGNATURE-UNKNOWN", decision["reason_codes"])

    def test_invalid_time_anchor_signature_denies_false(self):
        evidence = evidence_bundle(authority=time_authority(sig="invalid"))
        decision = self.fx.gate.authorize(self.fx.request(), evidence)
        self.assertEqual(decision["decision"], G.DECISION_DENY_FALSE)
        self.assertIn("E-TIME-ANCHOR-SIGNATURE-INVALID", decision["reason_codes"])

    def test_backward_clock_jump_does_not_revive_expired_request(self):
        request = self.fx.request(
            issued_at="2026-07-25T11:59:58Z", expires_at="2026-07-25T12:00:30Z"
        )
        self.fx.clock.advance(600)
        evidence = evidence_bundle(
            authority=time_authority(anchor="2026-07-25T12:10:00Z")
        )
        decision = self.fx.gate.authorize(request, evidence)
        self.assertEqual(decision["decision"], G.DECISION_DENY_FALSE)
        self.assertIn("E-REQUEST-EXPIRED", decision["reason_codes"])


class WitnessTests(unittest.TestCase):
    def setUp(self):
        self.fx = GateFixture()

    def test_absent_witness_is_unknown_not_healthy(self):
        evidence = evidence_bundle()
        del evidence["witness_receipt"]
        decision = self.fx.gate.authorize(self.fx.request(), evidence)
        self.assertEqual(decision["conjuncts"]["WitnessHealthy"], G.UNKNOWN)
        self.assertIn("E-WITNESS-ABSENT", decision["reason_codes"])
        # Silence is not health. The ceiling collapses to empty, so the
        # overall decision is DENY_FALSE by way of the ceiling check while the
        # WitnessHealthy conjunct itself remains UNKNOWN.
        self.assertNotEqual(decision["decision"], G.DECISION_ALLOW)
        self.assertEqual(decision["decision"], G.DECISION_DENY_FALSE)
        self.assertIn("E-EFFECT-ABOVE-CEILING", decision["reason_codes"])

    def test_forged_witness_signature_denies_false(self):
        evidence = evidence_bundle(receipt=witness_receipt(sig_status="invalid"))
        decision = self.fx.gate.authorize(self.fx.request(), evidence)
        self.assertEqual(decision["conjuncts"]["WitnessHealthy"], G.FALSE)
        self.assertIn("E-WITNESS-SIGNATURE-INVALID", decision["reason_codes"])

    def test_unverifiable_witness_signature_is_unknown(self):
        evidence = evidence_bundle(receipt=witness_receipt(sig_status="indeterminate"))
        decision = self.fx.gate.authorize(self.fx.request(), evidence)
        self.assertEqual(decision["conjuncts"]["WitnessHealthy"], G.UNKNOWN)

    def test_witness_control_ambiguity_is_unknown(self):
        evidence = evidence_bundle(receipt=witness_receipt(admin="unknown"))
        decision = self.fx.gate.authorize(self.fx.request(), evidence)
        self.assertEqual(decision["conjuncts"]["WitnessHealthy"], G.UNKNOWN)
        self.assertIn("E-WITNESS-CONTROL-AMBIGUOUS", decision["reason_codes"])

    def test_subject_administrable_witness_is_unknown(self):
        evidence = evidence_bundle(receipt=witness_receipt(admin="true"))
        decision = self.fx.gate.authorize(self.fx.request(), evidence)
        self.assertEqual(decision["conjuncts"]["WitnessHealthy"], G.UNKNOWN)

    def test_same_control_domain_is_unknown(self):
        evidence = evidence_bundle(
            receipt=witness_receipt(control_domain="subject-domain")
        )
        decision = self.fx.gate.authorize(self.fx.request(), evidence)
        self.assertEqual(decision["conjuncts"]["WitnessHealthy"], G.UNKNOWN)

    def test_within_auth_unknown_is_unknown(self):
        evidence = evidence_bundle(receipt=witness_receipt(within_auth="unknown"))
        decision = self.fx.gate.authorize(self.fx.request(), evidence)
        self.assertEqual(decision["conjuncts"]["WitnessHealthy"], G.UNKNOWN)
        self.assertIn("E-WITHINAUTH-NOT-ESTABLISHED", decision["reason_codes"])

    def test_within_subject_authority_is_unknown(self):
        evidence = evidence_bundle(
            receipt=witness_receipt(within_auth="within_subject_authority")
        )
        decision = self.fx.gate.authorize(self.fx.request(), evidence)
        self.assertEqual(decision["conjuncts"]["WitnessHealthy"], G.UNKNOWN)

    def test_failed_witness_denies_false(self):
        evidence = evidence_bundle(receipt=witness_receipt(health="FAILED"))
        decision = self.fx.gate.authorize(self.fx.request(), evidence)
        self.assertEqual(decision["conjuncts"]["WitnessHealthy"], G.FALSE)

    def test_unknown_health_is_unknown(self):
        evidence = evidence_bundle(receipt=witness_receipt(health="UNKNOWN"))
        decision = self.fx.gate.authorize(self.fx.request(), evidence)
        self.assertEqual(decision["conjuncts"]["WitnessHealthy"], G.UNKNOWN)

    def test_expired_witness_lease_denies_false(self):
        evidence = evidence_bundle(
            receipt=witness_receipt(expires_at="2026-07-25T11:59:59Z")
        )
        decision = self.fx.gate.authorize(self.fx.request(), evidence)
        self.assertEqual(decision["conjuncts"]["WitnessHealthy"], G.FALSE)
        self.assertIn("E-WITNESS-LEASE-EXPIRED", decision["reason_codes"])

    def test_witness_covering_other_subject_denies_false(self):
        evidence = evidence_bundle(receipt=witness_receipt(subject="agent-2"))
        decision = self.fx.gate.authorize(self.fx.request(), evidence)
        self.assertEqual(decision["conjuncts"]["WitnessHealthy"], G.FALSE)
        self.assertIn("E-WITNESS-SUBJECT-MISMATCH", decision["reason_codes"])

    def test_colluding_but_apparently_healthy_witness_is_out_of_model(self):
        """
        ARCHITECTURAL LIMITATION TEST, NOT AN ASSURANCE TEST.

        A witness that is fully controlled by, or colluding with, the subject
        but that emits a structurally perfect HEALTHY receipt with an explicit
        'subject_can_administer: false' declaration is INDISTINGUISHABLE at the
        gate from an honest witness. The gate ALLOWS. This test asserts that it
        allows, so that any future version claiming to detect this case must
        delete or rewrite this test, which is a visible act.

        WitnessHealthy does not imply witness honesty. Evidence independence is
        an assumption plus a declared assessment, not a derivation.
        """
        colluding = witness_receipt()
        colluding["independence_declaration"]["basis"] = (
            "declared by the colluding operator; false in fact, unverifiable here"
        )
        decision = self.fx.gate.authorize(
            self.fx.request(), evidence_bundle(receipt=colluding)
        )
        self.assertEqual(decision["decision"], G.DECISION_ALLOW)
        self.assertEqual(decision["conjuncts"]["WitnessHealthy"], G.TRUE)
        # And the gate exposes no field that could have detected it:
        self.assertNotIn("witness_honest", json.dumps(decision))
        self.assertNotIn("collusion_detected", json.dumps(decision))


class AuthorityTests(unittest.TestCase):
    def test_degradation_narrows_and_blocks_widened_effect(self):
        fx = GateFixture()
        allow = fx.gate.authorize(fx.request(), evidence_bundle())
        self.assertEqual(allow["decision"], G.DECISION_ALLOW)
        degraded = fx.gate.authorize(
            fx.request(nonce="b" * 32),
            evidence_bundle(receipt=witness_receipt(health="DEGRADED", epoch=8)),
        )
        self.assertEqual(degraded["decision"], G.DECISION_DENY_FALSE)
        self.assertIn("E-EFFECT-ABOVE-CEILING", degraded["reason_codes"])

    def test_degraded_ceiling_still_permits_narrowed_effect(self):
        fx = GateFixture()
        decision = fx.gate.authorize(
            fx.request(effect="READ"),
            evidence_bundle(receipt=witness_receipt(health="DEGRADED")),
        )
        self.assertEqual(decision["decision"], G.DECISION_ALLOW, decision["reason_codes"])

    def test_authority_widening_on_degradation_is_terminal(self):
        fx = GateFixture(
            degraded_effects=["READ", "WRITE", "DELETE"],
            degraded_targets=["https://db.example.internal/"],
        )
        fx.gate.authorize(fx.request(), evidence_bundle())
        widened = fx.gate.authorize(
            fx.request(nonce="b" * 32),
            evidence_bundle(receipt=witness_receipt(health="DEGRADED", epoch=8)),
        )
        self.assertIn("E-AUTHORITY-WIDENING", widened["reason_codes"])
        self.assertIn("sess-0001", fx.gate.state.terminal)

    def test_nonstrict_narrowing_on_degradation_is_terminal(self):
        fx = GateFixture(
            degraded_effects=["READ", "WRITE"],
            degraded_targets=["https://db.example.internal/records/"],
        )
        fx.gate.authorize(fx.request(), evidence_bundle())
        flat = fx.gate.authorize(
            fx.request(nonce="b" * 32),
            evidence_bundle(receipt=witness_receipt(health="DEGRADED", epoch=8)),
        )
        self.assertIn("E-NONSTRICT-NARROWING", flat["reason_codes"])

    def test_authority_epoch_is_monotone(self):
        fx = GateFixture()
        epochs = []
        fx.gate.authorize(fx.request(), evidence_bundle())
        epochs.append(fx.gate.state.authority_epoch["sess-0001"])
        fx.gate.authorize(
            fx.request(nonce="b" * 32, effect="READ"),
            evidence_bundle(receipt=witness_receipt(health="DEGRADED", epoch=8)),
        )
        epochs.append(fx.gate.state.authority_epoch["sess-0001"])
        self.assertEqual(epochs, sorted(epochs))
        self.assertLess(epochs[0], epochs[1])

    def test_authority_lattice_ordering(self):
        small = G.Authority(["READ"], ["https://a/"])
        large = G.Authority(["READ", "WRITE"], ["https://a/"])
        self.assertTrue(small <= large)
        self.assertTrue(small < large)
        self.assertFalse(large <= small)


class TargetTests(unittest.TestCase):
    def setUp(self):
        self.fx = GateFixture()

    def test_target_outside_contract_denied_false(self):
        request = self.fx.request(declared="https://other.example.internal/records/x")
        decision = self.fx.gate.authorize(request, evidence_bundle())
        self.assertEqual(decision["conjuncts"]["TargetAllowed"], G.FALSE)
        self.assertIn("E-TARGET-OUT-OF-CONTRACT", decision["reason_codes"])

    def test_traversal_alias_is_unknown(self):
        request = self.fx.request(
            declared="https://db.example.internal/records/../secrets/x",
            canonical="https://db.example.internal/records/row-1",
        )
        decision = self.fx.gate.authorize(request, evidence_bundle())
        self.assertEqual(decision["conjuncts"]["TargetAllowed"], G.UNKNOWN)
        self.assertIn("E-TARGET-NOT-CANONICALIZABLE", decision["reason_codes"])

    def test_percent_encoded_alias_is_unknown(self):
        request = self.fx.request(
            declared="https://db.example.internal/records%2f..%2fsecrets",
            canonical="https://db.example.internal/records/row-1",
        )
        decision = self.fx.gate.authorize(request, evidence_bundle())
        self.assertEqual(decision["conjuncts"]["TargetAllowed"], G.UNKNOWN)

    def test_wildcard_target_is_unknown_not_tautology(self):
        request = self.fx.request(declared="https://db.example.internal/records/*")
        decision = self.fx.gate.authorize(request, evidence_bundle())
        self.assertEqual(decision["conjuncts"]["TargetAllowed"], G.UNKNOWN)

    def test_declared_canonical_mismatch_denied_false(self):
        request = self.fx.request(
            declared="https://DB.example.internal/records/row-1",
            canonical="https://db.example.internal/records/row-9",
        )
        decision = self.fx.gate.authorize(request, evidence_bundle())
        self.assertEqual(decision["conjuncts"]["TargetAllowed"], G.FALSE)
        self.assertIn("E-TARGET-CANONICAL-MISMATCH", decision["reason_codes"])

    def test_case_folding_of_authority_is_canonical(self):
        self.assertEqual(
            G.canonical_target("HTTPS://DB.Example.Internal/records/row-1"),
            "https://db.example.internal/records/row-1",
        )

    def test_target_class_not_allowed_denied_false(self):
        request = self.fx.request(target_class="filesystem")
        decision = self.fx.gate.authorize(request, evidence_bundle())
        self.assertEqual(decision["conjuncts"]["TargetAllowed"], G.FALSE)


class ContractAndEffectTests(unittest.TestCase):
    def setUp(self):
        self.fx = GateFixture()

    def test_confused_deputy_subject_mismatch(self):
        request = self.fx.request(subject="agent-2")
        decision = self.fx.gate.authorize(request, evidence_bundle())
        self.assertEqual(decision["conjuncts"]["ContractMatch"], G.FALSE)
        self.assertIn("E-CONTRACT-SUBJECT-MISMATCH", decision["reason_codes"])

    def test_unknown_contract_is_unknown(self):
        request = self.fx.request()
        request["contract_digest"] = G.digest_bytes(b"no-such-contract")
        decision = self.fx.gate.authorize(request, evidence_bundle())
        self.assertEqual(decision["conjuncts"]["ContractMatch"], G.UNKNOWN)

    def test_tampered_contract_body_detected(self):
        digest_key = self.fx.contract_digest
        self.fx.contracts[digest_key]["body"]["allowed_effects"].append("DELETE")
        decision = self.fx.gate.authorize(self.fx.request(), evidence_bundle())
        self.assertEqual(decision["conjuncts"]["ContractMatch"], G.FALSE)
        self.assertIn("E-CONTRACT-DIGEST-MISMATCH", decision["reason_codes"])

    def test_revoked_contract_denied(self):
        self.fx.contracts[self.fx.contract_digest]["revoked"] = True
        decision = self.fx.gate.authorize(self.fx.request(), evidence_bundle())
        self.assertEqual(decision["conjuncts"]["ContractMatch"], G.FALSE)

    def test_unregistered_effect_denied_false(self):
        request = self.fx.request(effect="DELETE")
        decision = self.fx.gate.authorize(request, evidence_bundle())
        self.assertEqual(decision["conjuncts"]["EffectTypeValid"], G.FALSE)
        self.assertIn("E-EFFECT-NOT-REGISTERED", decision["reason_codes"])

    def test_adapter_digest_mismatch_denied_false(self):
        request = self.fx.request(adapter=G.digest_bytes(b"other-adapter"))
        decision = self.fx.gate.authorize(request, evidence_bundle())
        self.assertEqual(decision["conjuncts"]["EffectTypeValid"], G.FALSE)
        self.assertIn("E-ADAPTER-DIGEST-MISMATCH", decision["reason_codes"])


class CommitProtocolTests(unittest.TestCase):
    def setUp(self):
        self.fx = GateFixture()
        self.decision = self.fx.gate.authorize(self.fx.request(), evidence_bundle())
        self.receipt = self.decision["authorization_receipt"]
        self.binding = {
            "request_digest": self.receipt["request_digest"],
            "canonical_target": self.receipt["canonical_target"],
            "params_digest": self.receipt["params_digest"],
            "adapter_digest": self.receipt["adapter_digest"],
            "effect_type": self.receipt["effect_type"],
        }
        self.token = self.receipt["commit_token"]["token_id"]

    def test_double_spend_rejected(self):
        first = self.fx.gate.commit(self.token, self.binding, evidence_bundle())
        self.assertEqual(first["revalidation"]["result"], "PASS")
        second = self.fx.gate.commit(self.token, self.binding, evidence_bundle())
        self.assertEqual(second["outcome"], "FAILED_NO_EFFECT")
        self.assertIn("E-COMMIT-DOUBLE-SPEND", second["reason_codes"])

    def test_unknown_token_rejected(self):
        result = self.fx.gate.commit("token-99999999", self.binding, evidence_bundle())
        self.assertIn("E-COMMIT-UNKNOWN-TOKEN", result["reason_codes"])

    def test_expired_token_rejected(self):
        self.fx.clock.advance(100000)
        result = self.fx.gate.commit(self.token, self.binding, evidence_bundle())
        self.assertIn("E-COMMIT-TOKEN-EXPIRED", result["reason_codes"])

    def test_binding_mismatch_rejected(self):
        binding = dict(self.binding)
        binding["params_digest"] = G.digest_bytes(b"substituted-params")
        result = self.fx.gate.commit(self.token, binding, evidence_bundle())
        self.assertIn("E-COMMIT-BINDING-MISMATCH", result["reason_codes"])

    def test_binding_field_set_must_be_exact(self):
        binding = dict(self.binding)
        binding["extra"] = "x"
        result = self.fx.gate.commit(self.token, binding, evidence_bundle())
        self.assertIn("E-COMMIT-BINDING-FIELDS", result["reason_codes"])

    def test_derived_field_in_binding_rejected(self):
        binding = dict(self.binding)
        binding["authorized"] = True
        result = self.fx.gate.commit(self.token, binding, evidence_bundle())
        self.assertIn("E-CALLER-SUPPLIED-DERIVED-FIELD", result["reason_codes"])

    def test_toctou_authority_epoch_change_blocks_commit(self):
        self.fx.gate.authorize(
            self.fx.request(nonce="b" * 32, effect="READ"),
            evidence_bundle(receipt=witness_receipt(health="DEGRADED", epoch=8)),
        )
        result = self.fx.gate.commit(self.token, self.binding, evidence_bundle())
        self.assertIn("E-COMMIT-AUTHORITY-EPOCH-CHANGED", result["reason_codes"])

    def test_toctou_evidence_epoch_change_blocks_commit(self):
        self.fx.gate.authorize(
            self.fx.request(nonce="c" * 32), evidence_bundle(epoch=99)
        )
        result = self.fx.gate.commit(self.token, self.binding, evidence_bundle())
        self.assertIn("E-COMMIT-EVIDENCE-EPOCH-CHANGED", result["reason_codes"])

    def test_commit_time_witness_degradation_blocks_commit(self):
        result = self.fx.gate.commit(
            self.token,
            self.binding,
            evidence_bundle(receipt=witness_receipt(health="DEGRADED")),
        )
        self.assertIn("E-COMMIT-WITNESS-HEALTH-REGRESSED", result["reason_codes"])

    def test_commit_time_witness_epoch_change_blocks_commit(self):
        result = self.fx.gate.commit(
            self.token,
            self.binding,
            evidence_bundle(receipt=witness_receipt(epoch=8)),
        )
        self.assertIn("E-COMMIT-WITNESS-EPOCH-CHANGED", result["reason_codes"])

    def test_voided_token_cannot_be_reused_after_failed_commit(self):
        binding = dict(self.binding)
        binding["params_digest"] = G.digest_bytes(b"substituted-params")
        self.fx.gate.commit(self.token, binding, evidence_bundle())
        again = self.fx.gate.commit(self.token, self.binding, evidence_bundle())
        self.assertIn("E-COMMIT-DOUBLE-SPEND", again["reason_codes"])


class TerminalStateAndRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.fx = GateFixture(
            degraded_effects=["READ", "WRITE", "DELETE"],
            degraded_targets=["https://db.example.internal/"],
        )
        self.fx.gate.authorize(self.fx.request(), evidence_bundle())
        self.fx.gate.authorize(
            self.fx.request(nonce="b" * 32),
            evidence_bundle(receipt=witness_receipt(health="DEGRADED", epoch=8)),
        )
        self.assertIn("sess-0001", self.fx.gate.state.terminal)

    def amendment(self, adjudicators):
        return {
            "record_type": "bssg.correction-event",
            "spec_version": G.SPEC_VERSION,
            "correction_id": "cor-0001",
            "correction_class": "LIFT_TERMINAL_STATE",
            "supersedes": G.digest_bytes(b"prior-decision"),
            "reason_code": "C-TERMINAL-REVIEWED",
            "issued_by": {"authority_id": "ops-1", "control_domain": "ops-domain"},
            "session_id": "sess-0001",
            "subject_control_domain": "subject-domain",
            "adjudicators": adjudicators,
            "descendants": [],
            "descendant_closure_status": "UNKNOWN",
            "issued_at": "2026-07-25T12:01:00Z",
            "signature": signature("valid", kid="ops-key"),
        }

    def adjudicator(self, ident, domain, sig="valid"):
        return {
            "adjudicator_id": ident,
            "control_domain": domain,
            "signature": signature(sig, kid=ident),
        }

    def test_terminal_session_denies_all_further_requests(self):
        decision = self.fx.gate.authorize(
            self.fx.request(nonce="c" * 32), evidence_bundle()
        )
        # A terminal-session refusal is the distinct SESSION_TERMINAL state (spec S14.2), not a
        # merits DENY_FALSE -- so that SESSION_TERMINAL -> AUTHORIZED via amendment is permitted
        # while DENIED_* -> AUTHORIZED stays forbidden (P-A).
        self.assertEqual(decision["decision"], G.DECISION_SESSION_TERMINAL)
        self.assertIn("E-SESSION-TERMINAL", decision["reason_codes"])

    def test_single_adjudicator_amendment_rejected(self):
        result = self.fx.gate.submit_amendment(
            self.amendment([self.adjudicator("adj-1", "audit-domain")])
        )
        self.assertFalse(result["accepted"])
        # Insufficient adjudicators is rejected either by the schema (minItems:2, fires first) or by
        # the explicit quorum check -- both are correct.
        self.assertTrue(
            {"E-AMENDMENT-SCHEMA-INVALID", "E-AMENDMENT-QUORUM"} & set(result["reason_codes"])
        )

    def test_subject_domain_adjudicator_rejected(self):
        result = self.fx.gate.submit_amendment(
            self.amendment(
                [
                    self.adjudicator("adj-1", "subject-domain"),
                    self.adjudicator("adj-2", "audit-domain"),
                ]
            )
        )
        self.assertFalse(result["accepted"])
        self.assertIn("E-AMENDMENT-NOT-INDEPENDENT", result["reason_codes"])

    def test_same_domain_adjudicators_rejected(self):
        result = self.fx.gate.submit_amendment(
            self.amendment(
                [
                    self.adjudicator("adj-1", "audit-domain"),
                    self.adjudicator("adj-2", "audit-domain"),
                ]
            )
        )
        self.assertFalse(result["accepted"])
        self.assertIn("E-AMENDMENT-DOMAIN-COLLISION", result["reason_codes"])

    def test_unverifiable_adjudicator_signature_rejected(self):
        result = self.fx.gate.submit_amendment(
            self.amendment(
                [
                    self.adjudicator("adj-1", "audit-domain", sig="indeterminate"),
                    self.adjudicator("adj-2", "ops-domain"),
                ]
            )
        )
        self.assertFalse(result["accepted"])
        self.assertIn(
            "E-AMENDMENT-SIGNATURE-NOT-ESTABLISHED", result["reason_codes"]
        )

    def test_independent_amendment_lifts_terminal_state(self):
        result = self.fx.gate.submit_amendment(
            self.amendment(
                [
                    self.adjudicator("adj-1", "audit-domain"),
                    self.adjudicator("adj-2", "ops-domain"),
                ]
            )
        )
        self.assertTrue(result["accepted"])
        decision = self.fx.gate.authorize(
            self.fx.request(nonce="d" * 32), evidence_bundle()
        )
        self.assertEqual(decision["decision"], G.DECISION_ALLOW, decision["reason_codes"])

    def test_commit_after_terminal_state_fails(self):
        fx = GateFixture()
        decision = fx.gate.authorize(fx.request(), evidence_bundle())
        token = decision["authorization_receipt"]["commit_token"]["token_id"]
        fx.gate.state.terminal["sess-0001"] = "E-MANUAL-HALT"
        binding = {
            "request_digest": decision["authorization_receipt"]["request_digest"],
            "canonical_target": decision["authorization_receipt"]["canonical_target"],
            "params_digest": decision["authorization_receipt"]["params_digest"],
            "adapter_digest": decision["authorization_receipt"]["adapter_digest"],
            "effect_type": decision["authorization_receipt"]["effect_type"],
        }
        result = fx.gate.commit(token, binding, evidence_bundle())
        self.assertIn("E-SESSION-TERMINAL", result["reason_codes"])


class CorrectionAndLineageTests(unittest.TestCase):
    def base_correction(self, **overrides):
        correction = {
            "record_type": "bssg.correction-event",
            "spec_version": G.SPEC_VERSION,
            "correction_id": "cor-0002",
            "correction_class": "SUPERSEDE",
            "supersedes": G.digest_bytes(b"record-a"),
            "reason_code": "C-BAD-INPUT",
            "issued_by": {"authority_id": "ops-1", "control_domain": "ops-domain"},
            "descendants": [G.digest_bytes(b"record-b")],
            "descendant_closure_status": "COMPLETE",
            "issued_at": "2026-07-25T12:02:00Z",
            "signature": signature("valid", kid="ops-key"),
        }
        correction.update(overrides)
        return correction

    def test_complete_closure_with_unreachable_descendants_is_a_violation(self):
        correction = self.base_correction(
            unreachable_descendants=[G.digest_bytes(b"record-c")]
        )
        self.assertIn("X5", G.check_correction_closure(correction))

    def test_partial_closure_with_gaps_is_consistent(self):
        correction = self.base_correction(
            descendant_closure_status="PARTIAL",
            unreachable_descendants=[G.digest_bytes(b"record-c")],
        )
        self.assertEqual(G.check_correction_closure(correction), [])

    def test_unknown_closure_is_a_first_class_value(self):
        correction = self.base_correction(descendant_closure_status="UNKNOWN")
        self.assertEqual(G.check_correction_closure(correction), [])

    def test_invalid_closure_value_flagged(self):
        correction = self.base_correction(descendant_closure_status="MOSTLY")
        self.assertIn("X5b", G.check_correction_closure(correction))

    def test_lineage_complete_with_declared_gaps_is_a_violation(self):
        lineage = {
            "record_type": "bssg.lineage-record",
            "completeness": "COMPLETE",
            "declared_gaps": [
                {"gap_kind": "unmediated-channel", "description": "raw socket path"}
            ],
            "nodes": [
                {
                    "node_id": "n1",
                    "node_type": "effect-request",
                    "digest": G.digest_bytes(b"n1"),
                    "parents": [],
                }
            ],
        }
        self.assertIn("X6", G.check_lineage_completeness(lineage))

    def test_lineage_dangling_parent_flagged_when_claiming_complete(self):
        lineage = {
            "completeness": "COMPLETE",
            "declared_gaps": [],
            "nodes": [
                {
                    "node_id": "n2",
                    "node_type": "execution-receipt",
                    "digest": G.digest_bytes(b"n2"),
                    "parents": ["n-missing"],
                }
            ],
        }
        self.assertIn("X6c", G.check_lineage_completeness(lineage))


@unittest.skipUnless(HAVE_JSONSCHEMA, "jsonschema not installed")
class SchemaTests(unittest.TestCase):
    def setUp(self):
        self.schemas = {name: load_schema(name) for name in SCHEMA_FILES}

    def test_all_schemas_are_valid_2020_12_schemas(self):
        for name, schema in self.schemas.items():
            with self.subTest(schema=name):
                self.assertEqual(
                    schema["$schema"], "https://json-schema.org/draft/2020-12/schema"
                )
                jsonschema.Draft202012Validator.check_schema(schema)

    def test_effect_request_validates(self):
        fx = GateFixture()
        jsonschema.validate(
            fx.request(), self.schemas["effect-request.schema.json"]
        )

    def test_effect_request_rejects_extra_field(self):
        fx = GateFixture()
        request = fx.request()
        request["witness_healthy"] = True
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.validate(request, self.schemas["effect-request.schema.json"])

    def test_witness_receipt_validates(self):
        jsonschema.validate(
            witness_receipt(), self.schemas["witness-receipt.schema.json"]
        )

    def test_authorization_and_execution_receipts_validate(self):
        fx = GateFixture()
        decision = fx.gate.authorize(fx.request(), evidence_bundle())
        receipt = decision["authorization_receipt"]
        jsonschema.validate(
            receipt, self.schemas["authorization-receipt.schema.json"]
        )
        binding = {
            "request_digest": receipt["request_digest"],
            "canonical_target": receipt["canonical_target"],
            "params_digest": receipt["params_digest"],
            "adapter_digest": receipt["adapter_digest"],
            "effect_type": receipt["effect_type"],
        }
        execution = fx.gate.commit(
            receipt["commit_token"]["token_id"], binding, evidence_bundle()
        )
        jsonschema.validate(execution, self.schemas["execution-receipt.schema.json"])

    def test_failed_execution_receipt_validates(self):
        fx = GateFixture()
        failure = fx.gate.commit("token-00000000", {}, evidence_bundle())
        jsonschema.validate(failure, self.schemas["execution-receipt.schema.json"])

    def test_correction_event_validates(self):
        correction = {
            "record_type": "bssg.correction-event",
            "spec_version": G.SPEC_VERSION,
            "correction_id": "cor-0003",
            "correction_class": "AMEND_AUTHORITY",
            "supersedes": G.digest_bytes(b"record-a"),
            "reason_code": "C-AUTHORITY-AMENDED",
            "issued_by": {"authority_id": "ops-1", "control_domain": "ops-domain"},
            "adjudicators": [
                {
                    "adjudicator_id": "adj-1",
                    "control_domain": "audit-domain",
                    "signature": signature("valid", kid="adj-1"),
                },
                {
                    "adjudicator_id": "adj-2",
                    "control_domain": "ops-domain",
                    "signature": signature("valid", kid="adj-2"),
                },
            ],
            "descendants": [],
            "descendant_closure_status": "UNKNOWN",
            "issued_at": "2026-07-25T12:03:00Z",
            "signature": signature("valid", kid="ops-key"),
        }
        jsonschema.validate(correction, self.schemas["correction-event.schema.json"])

    def test_lineage_record_validates(self):
        lineage = {
            "record_type": "bssg.lineage-record",
            "spec_version": G.SPEC_VERSION,
            "lineage_id": "lin-0001",
            "subject_id": "agent-1",
            "session_id": "sess-0001",
            "nodes": [
                {
                    "node_id": "n1",
                    "node_type": "effect-request",
                    "digest": G.digest_bytes(b"n1"),
                    "parents": [],
                }
            ],
            "head_digest": G.digest_bytes(b"n1"),
            "chain_alg": "sha256-parent-chain",
            "completeness": "PARTIAL",
            "declared_gaps": [
                {
                    "gap_kind": "unmediated-channel",
                    "description": "operator console not mediated in this deployment",
                }
            ],
            "mediation_boundary_ref": "boundary-inventory-2026-07-25",
            "issued_at": "2026-07-25T12:04:00Z",
            "signature": signature("valid", kid="ops-key"),
        }
        jsonschema.validate(lineage, self.schemas["lineage-record.schema.json"])


class CrossRecordXInvariantTests(unittest.TestCase):
    """GPT-06: positive + negative vectors for the X4/X7/X8 mechanical checkers, so the package's
    X1-X8 mechanical-coverage claim is honest."""

    def test_x8_allow_receipt_positive_and_negative(self):
        clean = {"decision": "ALLOW",
                 "conjuncts": {k: "TRUE" for k in G.KERNEL_CONJUNCTS},
                 "reason_codes": []}
        self.assertEqual(G.check_allow_receipt(clean), [])
        forged_conjunct = {"decision": "ALLOW",
                           "conjuncts": {**{k: "TRUE" for k in G.KERNEL_CONJUNCTS},
                                         "EvidenceCurrent": "UNKNOWN"},
                           "reason_codes": []}
        self.assertIn("X8", G.check_allow_receipt(forged_conjunct))
        forged_reason = {"decision": "ALLOW",
                         "conjuncts": {k: "TRUE" for k in G.KERNEL_CONJUNCTS},
                         "reason_codes": ["E-FORGED-X8"]}
        self.assertIn("X8", G.check_allow_receipt(forged_reason))

    def test_x7_authority_history_positive_and_negative(self):
        proper = [{"session_id": "s", "authority_epoch": 1,
                   "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}},
                  {"session_id": "s", "authority_epoch": 2,
                   "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}]
        self.assertEqual(G.check_authority_history(proper), [])
        regression = [{"session_id": "s", "authority_epoch": 2, "authority_snapshot": {"effects": ["READ"], "target_scopes": []}},
                      {"session_id": "s", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": []}}]
        self.assertIn("X7", G.check_authority_history(regression))
        widening = [{"session_id": "s", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}},
                    {"session_id": "s", "authority_epoch": 2, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}]
        self.assertIn("X7", G.check_authority_history(widening))

    def test_x4_single_redemption_positive_and_negative(self):
        C = "COMMITTED_PENDING_OUTCOME"
        F = "FAILED_NO_EFFECT"
        # distinct redeemed tokens: no violation
        self.assertEqual(G.check_single_redemption(
            [{"commit_token_id": "t1", "outcome": C}, {"commit_token_id": "t2", "outcome": C}]), [])
        # a single redemption: no violation
        self.assertEqual(G.check_single_redemption([{"commit_token_id": "t1", "outcome": C}]), [])
        # C5: the same token REDEEMED twice IS a violation
        self.assertIn("X4", G.check_single_redemption(
            [{"commit_token_id": "t1", "outcome": C}, {"commit_token_id": "t1", "outcome": C}]))
        # C5 (the former false positive): two FAILED_NO_EFFECT attempts on one token is ZERO
        # redemptions and MUST NOT flag X4 -- this is the reference gate's own legitimate log.
        self.assertEqual(G.check_single_redemption(
            [{"commit_token_id": "t1", "outcome": F}, {"commit_token_id": "t1", "outcome": F}]), [])
        # a failed attempt followed by a real redemption is a single redemption: no violation
        self.assertEqual(G.check_single_redemption(
            [{"commit_token_id": "t1", "outcome": F}, {"commit_token_id": "t1", "outcome": C}]), [])

if __name__ == "__main__":
    unittest.main(verbosity=1)

---

# Bismillah ir-Rahman ir-Rahim
