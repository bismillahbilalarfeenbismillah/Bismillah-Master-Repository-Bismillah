# Bismillah ir-Rahman ir-Rahim

# R0267 -- bssg_model_check.py.txt — BSSG -- OPERATIONAL model-checker (R7 rebuild).

**Chronological Index:** 119 of 995  
**Date:** 2026  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** bssg_model_check.py.txt  
**Source Format:** txt  
**SHA-256:** `47b7da6f19035da063d494aea50c8f240994e16b75e6c32eb0487a2deb86260f`  

---

## R0267 · bssg_model_check.py.txt — BSSG -- OPERATIONAL model-checker (R7 rebuild).

- section: V. BSSG & SHVVP Protocols
- source_file: bssg_model_check.py.txt
- source_format: txt
- merged_variants: 7 (bssg_model_check.py)
- text_sha256: 47b7da6f19035da063d494aea50c8f240994e16b75e6c32eb0487a2deb86260f

"""BSSG -- OPERATIONAL model-checker (R7 rebuild).

The prior model-checker proved properties of a hand-copied transition graph; GPT's audit
showed the executable violated one of them (allow-after-deny), so an abstract-graph proof
does not bind the implementation. This version establishes a REFINEMENT RELATION: it drives
the REAL gate through positive and adversarial traces and checks that (a) every observed
operation lands in a state the Section-14 model permits, and (b) the model's safety
invariants hold on actual executions. It also keeps the two sound abstract checks (kernel
truth table, antitone degradation) and removes the dead strictness code from finding KIMI-1
(strictness is a gate behavior, checked operationally in OP-STRICT).

On the un-repaired gate the operational checks FAIL (they are the audit counterexamples as
model invariants); on the repaired gate they PASS. Run: python3 bssg_model_check.py
"""
import os, sys, copy
from itertools import product, chain, combinations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import bssg_gate as G
import test_bssg_gate as T

fail = []
def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("  " + detail) if detail else ""))
    if not ok:
        fail.append(name)

def subsets(s):
    s = list(s)
    return [frozenset(c) for c in chain.from_iterable(combinations(s, r) for r in range(len(s)+1))]

# ===========================================================================
# ABSTRACT CHECK 1 -- kernel truth table, re-derived from the gate's own code.
# ===========================================================================
TV = G.TRUTH_VALUES; conj = list(G.KERNEL_CONJUNCTS); n = 0; ok = True
for combo in product(TV, repeat=5):
    dec, _ = G.kernel_decision(dict(zip(conj, combo)))
    any_false = any(v == G.FALSE for v in combo); any_unknown = any(v == G.UNKNOWN for v in combo)
    exp = G.DECISION_DENY_FALSE if any_false else (G.DECISION_DENY_UNKNOWN if any_unknown else G.DECISION_ALLOW)
    if dec != exp or ((dec == G.DECISION_ALLOW) != all(v == G.TRUE for v in combo)):
        ok = False; break
    n += 1
check("A1 kernel truth table: gate matches spec rule on all 3^5 states + ALLOW iff all TRUE", ok and n == 243, "states=%d" % n)

# ===========================================================================
# ABSTRACT CHECK 2 -- degradation antitone (subset) over the finite lattice.
# (KIMI-1 fix: the dead 'strict_ok' branch is gone; strictness is checked in OP-STRICT.)
# ===========================================================================
U_eff = ["READ", "WRITE", "DELETE"]; U_tgt = ["a", "b", "c"]; healths = ["HEALTHY", "DEGRADED", "FAILED", "UNKNOWN"]
anti = True; contracts = 0
for he in subsets(U_eff):
    for ht in subsets(U_tgt):
        for de in subsets(he):
            for dt in subsets(ht):
                c = {"allowed_effects": list(he), "allowed_target_scopes": list(ht),
                     "degraded_effects": list(de), "degraded_target_scopes": list(dt)}
                ceil = {h: G.ceiling_for_health(c, h) for h in healths}; contracts += 1
                for h1 in healths:
                    for h2 in healths:
                        if G.HEALTH_ORDER[h1] <= G.HEALTH_ORDER[h2] and not (ceil[h1] <= ceil[h2]):
                            anti = False
check("A2 degradation antitone over the full finite lattice (health down => ceiling subset)", anti, "contracts=%d" % contracts)

# ===========================================================================
# OPERATIONAL REFINEMENT -- drive the REAL gate; observed transitions must be
# permitted by Section 14, and the safety invariants must hold on real traces.
# ===========================================================================
PERMITTED = {
    "RECEIVED": {"REJECTED_SCHEMA", "EVALUATING"},
    "EVALUATING": {"DENIED_FALSE", "DENIED_UNKNOWN", "AUTHORIZED_UNUSED", "SESSION_TERMINAL"},
    "AUTHORIZED_UNUSED": {"COMMITTED_PENDING_OUTCOME", "FAILED_NO_EFFECT"},
    "SESSION_TERMINAL": {"EVALUATING"},
}
TERMINAL_REASONS = {"E-SESSION-TERMINAL", "E-REQUEST-DENIED-TERMINAL", "E-AUTHORITY-WIDENING", "E-NONSTRICT-NARROWING"}
def st_auth(d):
    r = d.get("reason_codes", [])
    # F (F-BSSG-P17-GPT-05 / KIMI-6): the model projection uses the SAME positive-issuance predicate as
    # the product path, so a collision / issuance-failure record (decision=ALLOW, issuance_status=
    # FAILED_NO_EFFECT) is NOT modeled as authorized.
    if G.BSSGGate.authorized_issuance(d): return "AUTHORIZED_UNUSED"
    if d.get("issuance_status") == "FAILED_NO_EFFECT": return "DENIED_UNKNOWN"  # authorizable but no effect
    if any(x in TERMINAL_REASONS for x in r): return "SESSION_TERMINAL"
    if d["decision"] == "DENY_FALSE": return "DENIED_FALSE"
    if d["decision"] == "DENY_UNKNOWN": return "DENIED_UNKNOWN"
    if str(d["decision"]).startswith("CRASH"): return "CRASH"
    return "REJECTED_SCHEMA"
def st_commit(c):
    return "COMMITTED_PENDING_OUTCOME" if c["outcome"] == "COMMITTED_PENDING_OUTCOME" else "FAILED_NO_EFFECT"

observed = []  # (from_state, to_state) collected across every scenario
def auth(f, r, ev):
    try:
        d = f.gate.authorize(r, ev)
    except Exception as e:  # totality: a decision function must never raise
        d = {"decision": "CRASH:" + type(e).__name__, "reason_codes": [], "conjuncts": {}}
    to = st_auth(d)
    observed.append(("RECEIVED" if to == "REJECTED_SCHEMA" else "EVALUATING", to))
    return d
def commit(f, tok, binding, ev):
    c = f.gate.commit(tok, binding, ev); observed.append(("AUTHORIZED_UNUSED", st_commit(c))); return c
def binding_of(rec):
    return {k: rec[k] for k in ("request_digest", "canonical_target", "params_digest", "adapter_digest", "effect_type")}

# OP-POS: a valid request authorizes and its token commits once (the happy path exists).
f = T.GateFixture(); d = auth(f, f.request(), T.evidence_bundle())
pos_auth = d["decision"] == "ALLOW"
tok = d["authorization_receipt"]["commit_token"]["token_id"] if pos_auth else None
c1 = commit(f, tok, binding_of(d["authorization_receipt"]), {}) if pos_auth else None
check("OP-POS valid authorize -> AUTHORIZED_UNUSED and a single commit -> COMMITTED",
      bool(pos_auth and c1 and c1["outcome"] == "COMMITTED_PENDING_OUTCOME"))

# OP-R1: a denied snapshot must not later ALLOW; a FRESH request still evaluates (liveness).
f = T.GateFixture(); r = f.request()
d1 = auth(f, copy.deepcopy(r), T.evidence_bundle(authority=T.time_authority(sig="invalid")))
d2 = auth(f, copy.deepcopy(r), T.evidence_bundle())                      # same snapshot
d3 = auth(f, f.request(nonce="c"*32), T.evidence_bundle())               # fresh, different snapshot
check("OP-R1 no allow-after-deny for a snapshot, and a fresh request still authorizes",
      d1["decision"].startswith("DENY") and d2["decision"] != "ALLOW" and d3["decision"] == "ALLOW")

# OP-R2: one-time redemption -- a second commit of the same token fails.
f = T.GateFixture(); d = auth(f, f.request(), T.evidence_bundle()); rec = d["authorization_receipt"]; tok = rec["commit_token"]["token_id"]
first = commit(f, tok, binding_of(rec), {}); second = commit(f, tok, binding_of(rec), {})
check("OP-R2 single-use redemption: first COMMITTED, second FAILED_NO_EFFECT",
      first["outcome"] == "COMMITTED_PENDING_OUTCOME" and second["outcome"] != "COMMITTED_PENDING_OUTCOME")

# OP-R6: cross-session isolation, and same-session widening still terminalizes (both directions).
f = T.GateFixture()
rA = f.request(effect="READ", nonce="a"*32); rA["session_id"] = "sA"; rA["request_id"] = "req-A"
auth(f, rA, T.evidence_bundle(receipt=T.witness_receipt(health="DEGRADED")))
rB = f.request(effect="WRITE", nonce="b"*32); rB["session_id"] = "sB"; rB["request_id"] = "req-B"
dB = auth(f, rB, T.evidence_bundle(receipt=T.witness_receipt(health="HEALTHY")))
rA2 = f.request(effect="WRITE", nonce="d"*32); rA2["session_id"] = "sA"; rA2["request_id"] = "req-A2"
dA2 = auth(f, rA2, T.evidence_bundle(receipt=T.witness_receipt(health="HEALTHY")))
check("OP-R6 sessions isolated (B unaffected by A) AND same-session widening is terminal",
      "E-AUTHORITY-WIDENING" not in dB["reason_codes"] and "sB" not in f.gate.state.terminal
      and "E-AUTHORITY-WIDENING" in dA2["reason_codes"])

# OP-STRICT: a strict health drop with no actual narrowing must terminalize (E-NONSTRICT-NARROWING).
f2 = T.GateFixture(degraded_effects=["READ", "WRITE"], degraded_targets=["https://db.example.internal/records/"])
auth(f2, f2.request(effect="WRITE", nonce="a"*32), T.evidence_bundle(receipt=T.witness_receipt(health="HEALTHY")))
dS = auth(f2, f2.request(effect="WRITE", nonce="b"*32), T.evidence_bundle(receipt=T.witness_receipt(health="DEGRADED", epoch=8)))
check("OP-STRICT strict health drop without strict narrowing is terminal (E-NONSTRICT-NARROWING)",
      "E-NONSTRICT-NARROWING" in dS["reason_codes"])

# OP-R5: terminal recovery -- a valid independent amendment lifts; bad ones do not.
def amendment(session, adjs, cclass="LIFT_TERMINAL_STATE"):
    return {"record_type": "bssg.correction-event", "spec_version": G.SPEC_VERSION,
            "correction_id": "cor-" + session, "correction_class": cclass,
            "supersedes": G.digest_bytes(b"prior-terminal"), "reason_code": "C-TERMINAL-REVIEWED",
            "issued_by": {"authority_id": "ops-1", "control_domain": "ops"},
            "session_id": session, "subject_control_domain": "subject-domain", "adjudicators": adjs,
            "descendants": [], "descendant_closure_status": "UNKNOWN",
            "issued_at": "2026-07-25T12:01:00Z", "signature": T.signature("valid", kid="ops-key")}
def adj(ident, domain):
    return {"adjudicator_id": ident, "control_domain": domain, "signature": T.signature("valid", kid=ident)}
f = T.GateFixture(); f.gate.state.terminal["sX"] = "E-AUTHORITY-WIDENING"
bad = f.gate.submit_amendment(amendment("sX", [adj("a1", "d1"), adj("a2", "d1")]))
dup = f.gate.submit_amendment(amendment("sX", [{"adjudicator_id":"a1","control_domain":"d1","signature":T.signature("valid",kid="same")},
                                               {"adjudicator_id":"a2","control_domain":"d2","signature":T.signature("valid",kid="same")}]))
wrongclass = f.gate.submit_amendment(amendment("sX", [adj("a1", "d1"), adj("a2", "d2")], cclass="SUPERSEDE"))
good = f.gate.submit_amendment(amendment("sX", [adj("a1", "d1"), adj("a2", "d2")]))
if good.get("accepted"):
    observed.append(("SESSION_TERMINAL", "EVALUATING"))
check("OP-R5 valid amendment recovers (SESSION_TERMINAL->EVALUATING); bad-domain / dup-sig / wrong-class rejected",
      good.get("accepted") is True and not bad.get("accepted") and not dup.get("accepted")
      and not wrongclass.get("accepted") and "sX" not in f.gate.state.terminal)

# OP-ABSORB: a request in an already-terminal session is refused (terminal is absorbing).
f = T.GateFixture(); f.gate.state.terminal["sT"] = "E-AUTHORITY-WIDENING"
rt = f.request(); rt["session_id"] = "sT"
dt = auth(f, rt, T.evidence_bundle())
check("OP-ABSORB request in a terminal session is refused (E-SESSION-TERMINAL)",
      "E-SESSION-TERMINAL" in dt["reason_codes"])

# OP-OD11: the subject-facing response conceals the denial regime (audit plane keeps it).
f = T.GateFixture()
dF = f.gate.authorize(f.request(), T.evidence_bundle(receipt=T.witness_receipt(sig_status="invalid")))
ru = f.request(nonce="e"*32); ru["contract_digest"] = "sha256:" + "0"*64
dU = f.gate.authorize(ru, T.evidence_bundle())
sfF = f.gate.subject_facing(dF); sfU = f.gate.subject_facing(dU)
check("OP-OD11 subject-facing conceals DENY_FALSE vs DENY_UNKNOWN (audit plane retains it)",
      sfF == sfU and sfF.get("decision") == "DENIED" and dF["decision"] != dU["decision"])

# OP-REJECT: a structurally invalid request is a distinct REJECTED_SCHEMA state (spec S14.1),
# never conflated with a kernel-level DENY_UNKNOWN.
f = T.GateFixture(); rbad = f.request(); rbad["sequence"] = 2**60
drej = auth(f, rbad, T.evidence_bundle())
check("OP-REJECT structural admission failure is a distinct REJECTED_SCHEMA state",
      drej["decision"] == "REJECTED_SCHEMA" and st_auth(drej) == "REJECTED_SCHEMA")

# OP-DENY-PATHS: on EVERY denial path the identical request re-submitted must not ALLOW. The
# prior checker failed to exercise this -- P1 was an allow-after-deny on an early path it never
# drove -- so driving each path is what makes the no-DENY->ALLOW refinement non-vacuous.
import copy as _copy
_paths = []
f = T.GateFixture(); r = f.request()                                   # (a) null evidence
_paths.append((auth(f, _copy.deepcopy(r), None), auth(f, _copy.deepcopy(r), T.evidence_bundle())))
f = T.GateFixture(); r = f.request(); r["contract_digest"] = "sha256:" + "0"*64   # (b) unknown contract
_paths.append((auth(f, _copy.deepcopy(r), T.evidence_bundle()), auth(f, _copy.deepcopy(r), T.evidence_bundle())))
f = T.GateFixture(); r = f.request()                                   # (c) invalid witness signature
_bad = T.evidence_bundle(receipt=T.witness_receipt(sig_status="invalid"))
_paths.append((auth(f, _copy.deepcopy(r), _bad), auth(f, _copy.deepcopy(r), T.evidence_bundle())))
check("OP-DENY-PATHS every deny path is terminal for its snapshot (no allow-after-deny on ANY path)",
      all(a["decision"] != "ALLOW" and b["decision"] != "ALLOW" for a, b in _paths), "paths=%d" % len(_paths))

# NOTE ON STATE SCOPE: COMMITTING/VOID/EXPIRED/CONSUMED are internal token statuses, not
# decision-record outputs; the observable commit outcomes are COMMITTED_PENDING_OUTCOME and
# FAILED_NO_EFFECT. INDETERMINATE (unknown remote outcome) and QUARANTINED (artifact plane)
# are outside the reference gate's commit path and are declared OUT OF MODEL here.

# REFINEMENT: every transition observed on the real gate is a permitted Section-14 transition.
bad_edges = [(a, b) for (a, b) in observed if b not in PERMITTED.get(a, set())]
check("REFINE every observed executable transition is permitted by Section 14",
      not bad_edges, "observed=%d illegal=%d" % (len(observed), len(bad_edges)))
check("REFINE no DENIED_*->AUTHORIZED_UNUSED edge ever occurred on the executable",
      not any(a in ("DENIED_FALSE", "DENIED_UNKNOWN") and b == "AUTHORIZED_UNUSED" for (a, b) in observed))


def _check_record_kernel_consistency(gate):
    """GPT-04 + F (GPT-05/KIMI-5/6): on every KERNEL-EVALUATED decision record, assert
    recorded_decision == kernel_decision(recorded_conjuncts). Records are classified at emission by the
    explicit `kernel_evaluated` flag: kernel ALLOW/DENY, issuance failures (collision/mint), and aborts
    are kernel-evaluated (and must be consistent); protocol/admission denials (nonce replay, session
    terminal, structural reject, reentrant refusal) are kernel_evaluated=False and exempt -- their
    decision is a protocol classification, not a kernel one, so the universal claim is honestly scoped."""
    from bssg_gate import kernel_decision
    bad = []
    for rec in gate.state.records:
        if rec.get("record_type") != "bssg.decision":
            continue
        if rec.get("kernel_evaluated") is not True:
            continue
        cj = rec.get("conjuncts")
        if not isinstance(cj, dict):
            bad.append((rec.get("decision"), "NON-DICT-CONJUNCTS", cj)); continue
        expected, _ = kernel_decision(dict(cj))
        if expected != rec.get("decision"):
            bad.append((rec.get("decision"), expected, cj))
    return bad

# F: drive collision, mint-abort, nonce-replay, and reentrant-refusal traces, then assert kernel
# consistency over EVERY kernel-evaluated record across all of them (not only the collision fixture).
import test_bssg_gate as _KT
_kf = _KT.GateFixture()
_ka1 = _kf.gate.authorize(_kf.request(nonce="a" * 32), _KT.evidence_bundle())
_ktok = _ka1["authorization_receipt"]["commit_token"]["token_id"]
_kf.gate.new_token = lambda: _ktok
_kd2 = _kf.gate.authorize(_kf.request(nonce="b" * 32), _KT.evidence_bundle())        # collision
def _mint_boom():
    raise RuntimeError("mint fault")
_kf.gate.new_token = _mint_boom
_kd3 = _kf.gate.authorize(_kf.request(nonce="c" * 32), _KT.evidence_bundle())        # mint abort (issuance failure)
_rf = _KT.GateFixture()
_r_a = _rf.request(nonce="e" * 32); _r_a["request_id"] = "rid-A"
_r_b = _rf.request(nonce="e" * 32); _r_b["request_id"] = "rid-B"   # same nonce, distinct snapshot
_rf.gate.authorize(_r_a, _KT.evidence_bundle())                     # consumes the nonce
_rf.gate.authorize(_r_b, _KT.evidence_bundle())                     # E-NONCE-REPLAY: DENY_FALSE, all-UNKNOWN
# the replay record is kernel_evaluated=False and INCONSISTENT (DENY_FALSE vs kernel(all-UNKNOWN)=
# DENY_UNKNOWN); it MUST be exempted, which makes the scoping load-bearing rather than vacuous.
_rep = _rf.gate.state.records[-1]
_replay_exempt_inconsistent = (
    _rep.get("kernel_evaluated") is False
    and "E-NONCE-REPLAY" in _rep.get("reason_codes", [])
    and G.kernel_decision(dict(_rep["conjuncts"]))[0] != _rep["decision"])
# F/GPT-06 (pass-18): drive an ACTUAL reentrant refusal (a token factory that re-enters authorize during
# mint of the outer call) and assert the pre-admission refusal is classified kernel_evaluated=False with
# all-UNKNOWN conjuncts -- so code, classification, and this trace agree.
_ef = _KT.GateFixture()
_nested_holder = {}
def _reentrant_factory():
    _nested_holder["rec"] = _ef.gate.authorize(_ef.request(nonce="9" * 32), _KT.evidence_bundle())
    return "tok-outer-01"
_ef.gate.new_token = _reentrant_factory
_ef.gate.authorize(_ef.request(nonce="8" * 32), _KT.evidence_bundle())
_nested = _nested_holder.get("rec", {})
_reentrant_ok = (
    _nested.get("reason_codes") == ["E-REENTRANT-CALL"]
    and _nested.get("kernel_evaluated") is False
    and all(v == "UNKNOWN" for v in _nested.get("conjuncts", {"x": "TRUE"}).values()))
_kbad = (_check_record_kernel_consistency(_kf.gate)
         + _check_record_kernel_consistency(_rf.gate)
         + _check_record_kernel_consistency(_ef.gate))
_issuance_ok = _kd2.get("issuance_status") == "FAILED_NO_EFFECT" and _kd3.get("issuance_status") == "FAILED_NO_EFFECT"
check("REFINE every kernel-evaluated record satisfies decision == kernel_decision(conjuncts); protocol records (replay, reentrant) exempt and load-bearing",
      not _kbad and _issuance_ok and _replay_exempt_inconsistent and _reentrant_ok,
      "records=%d inconsistent=%d collision=%s mint_abort=%s replay_exempt=%s reentrant_false=%s" % (
          len(_kf.gate.state.records) + len(_rf.gate.state.records) + len(_ef.gate.state.records), len(_kbad),
          _kd2.get("issuance_status"), _kd3.get("issuance_status"), _replay_exempt_inconsistent, _reentrant_ok))

# ===========================================================================
# BOUNDED AUTHORITY-INTRODUCTION MODEL CHECK (V29 -- Axiom 3 / R_may closure).
# The CE corpus enumerates hand-picked schedules (R_declared); GPT-P30-01 lived
# in the schedule NO ONE enumerated (R_may). This check drives the REAL gate over
# EVERY schedule of bounded length from a small op alphabet and asserts the
# structural invariant the effect bypass violated: after a fixed healthy
# establishment under contract C1 ({READ,WRITE}), no ALLOW on ANY schedule may
# authorize an effect OUTSIDE that established ceiling -- no authorize/reject/lift
# sequence can introduce authority (DELETE) the session never legitimately held.
# GRANTED is fixed independently of the gate's contract_ceiling internals, so the
# check actually TESTS them rather than restating them. A locally-green but
# structurally-unjustified "fix" fails HERE, over all schedules, not five rounds
# later at a seat. On the poisoned gate it FAILS; on the repaired gate it PASSES.
# ===========================================================================
def _reg_c2(fx):
    b = T.contract_body(fx.policy_digest)
    b["allowed_effects"] = ["READ", "WRITE", "DELETE"]
    b["effect_registry"]["DELETE"] = {"adapter_digest": T.ADAPTER_DIGEST}
    b["degraded_effects"] = ["READ"]
    d = G.digest(b); fx.gate.contracts[d] = {"body": copy.deepcopy(b), "revoked": False}
    return d
# V34 F-GS-2 FIX: C2W registers a broader healthy target scope ({records/, admin/}) while
# retaining degraded={records/} only. This makes the target-scope predicate non-vacuous:
# the model check now drives schedules where a broader target could be introduced via a
# HEALTHY C2W request whose target scope exceeds the established C1 ceiling.
_ADMIN_TARGET = "https://admin.example.internal/"
def _reg_c2w(fx):
    b = T.contract_body(fx.policy_digest)
    b["allowed_effects"] = ["READ", "WRITE"]
    b["effect_registry"] = {"READ": {"adapter_digest": T.ADAPTER_DIGEST}, "WRITE": {"adapter_digest": T.ADAPTER_DIGEST}}
    b["degraded_effects"] = ["READ"]
    b["allowed_target_scopes"] = ["https://db.example.internal/records/", _ADMIN_TARGET]
    b["degraded_target_scopes"] = ["https://db.example.internal/records/"]
    d = G.digest(b); fx.gate.contracts[d] = {"body": copy.deepcopy(b), "revoked": False}
    return d
def _amd_ab(session, cid):
    a = lambda i, dm: {"adjudicator_id": i, "control_domain": dm, "signature": T.signature("valid", kid=i)}
    return {"record_type": "bssg.correction-event", "spec_version": G.SPEC_VERSION, "correction_id": cid,
            "correction_class": "LIFT_TERMINAL_STATE", "supersedes": G.digest_bytes(b"prior"),
            "reason_code": "C-TERMINAL-REVIEWED", "issued_by": {"authority_id": "ops-1", "control_domain": "ops-domain"},
            "session_id": session, "subject_control_domain": "subject-domain",
            "adjudicators": [a("adj-1", "audit-domain"), a("adj-2", "ops-domain")],
            "descendants": [], "descendant_closure_status": "UNKNOWN", "issued_at": "2026-07-25T12:01:00Z",
            "signature": T.signature("valid", kid="ops-key")}
_GRANTED = frozenset({"READ", "WRITE"})   # C1 healthy ceiling = the authority legitimately established
_GRANTED_TARGETS = frozenset({"https://db.example.internal/records/"})  # V30 K32-02: track target scopes too
# V34 F-GS-2 FIX: alphabet expanded with C2W target-bearing ops (HEALTHY READ with admin target,
# DEGRADED READ with records target) and mint-fault op (F-GS-1 vector). The prior alphabet claimed
# target-scope coverage but _reg_c2 only mutated effects, never targets -- the target predicate was
# vacuously exercised. C2W registers {records/, admin/} healthy, {records/} degraded.
# Mint-fault ("M") injects a token-creation failure to cover the F-GS-1 ceiling-poison vector.
_OPS = [("A", "C1", "READ", "HEALTHY"), ("A", "C1", "WRITE", "DEGRADED"),
        ("A", "C2", "DELETE", "HEALTHY"), ("A", "C2", "DELETE", "DEGRADED"),
        ("A", "C2", "READ", "DEGRADED"),   # K33-01: the allowed-degraded poison vector
        ("A", "C2", "READ", "HEALTHY"),     # K33-01: broader-contract healthy read
        ("A", "C2W", "READ", "HEALTHY"),    # F-GS-2: broader-target healthy read
        ("A", "C2W", "READ", "DEGRADED"),   # F-GS-2: degraded read under broader-target contract
        ("M",),                              # F-GS-1: mint-fault (HEALTHY C2 READ with injected fault)
        ("L",)]
_K = 4  # retained at 4 with expanded 10-op alphabet
_bmc_sched = 0; _bmc_allows = 0; _bmc_violation = None
for _len in range(1, _K + 1):
    for _sched in product(_OPS, repeat=_len):
        fx = T.GateFixture(); c2 = _reg_c2(fx); c2w = _reg_c2w(fx)
        _ep = 7; _seq = 11; _nz = 0; _lift = 0
        _est = fx.gate.authorize(fx.request(effect="WRITE", nonce=("%032x" % _nz)),
                                 T.evidence_bundle(receipt=T.witness_receipt(epoch=_ep, sequence=_seq), epoch=5))
        _nz += 1; _ep += 1; _seq += 1; _bmc_sched += 1
        if _est.get("decision") != "ALLOW":
            continue
        for _op in _sched:
            if _op[0] == "L":
                fx.gate.submit_amendment(_amd_ab("sess-0001", "cor-%d" % _lift)); _lift += 1; continue
            if _op[0] == "M":
                # Mint-fault: inject a token-creation failure for a HEALTHY C2 READ
                _saved_mint = fx.gate.new_token
                fx.gate.new_token = lambda: (_ for _ in ()).throw(RuntimeError("probe-mint-fault"))
                try:
                    _req = T.effect_request(c2, fx.policy_digest, effect="READ", nonce=("%032x" % _nz))
                    fx.gate.authorize(_req, T.evidence_bundle(receipt=T.witness_receipt(health="HEALTHY", epoch=_ep, sequence=_seq), epoch=5))
                except Exception:
                    pass
                fx.gate.new_token = _saved_mint
                _nz += 1; _ep += 1; _seq += 1
                continue
            _, _which, _eff, _h = _op
            if _which == "C2W":
                _req = T.effect_request(c2w, fx.policy_digest, effect=_eff, nonce=("%032x" % _nz))
                if _h == "HEALTHY":
                    _req["target"] = {"declared": _ADMIN_TARGET + "panel", "canonical": _ADMIN_TARGET + "panel", "target_class": "admin-scope"}
            elif _which == "C2":
                _req = T.effect_request(c2, fx.policy_digest, effect=_eff, nonce=("%032x" % _nz))
            else:
                _req = fx.request(effect=_eff, nonce=("%032x" % _nz))
            try:
                _d = fx.gate.authorize(_req, T.evidence_bundle(receipt=T.witness_receipt(health=_h, epoch=_ep, sequence=_seq), epoch=5))
            except Exception as _e:
                _d = {"decision": "CRASH:" + type(_e).__name__}
            _nz += 1; _ep += 1; _seq += 1
            if _d.get("decision") == "ALLOW":
                _bmc_allows += 1
                # V30 K32-02 FIX: check BOTH effect and target-scope introduction
                _auth_snap = _d.get("authority_snapshot")
                _allowed_effs = frozenset(_auth_snap.get("effects", [])) if isinstance(_auth_snap, dict) else frozenset()
                _allowed_tgts = frozenset(_auth_snap.get("target_scopes", [])) if isinstance(_auth_snap, dict) else frozenset()
                if _eff not in _GRANTED or not _allowed_effs.issubset(_GRANTED) or not _allowed_tgts.issubset(_GRANTED_TARGETS):
                    _bmc_violation = (_sched, _eff); break
        if _bmc_violation: break
    if _bmc_violation: break
check("BOUNDED-AUTH-INTRO: over all schedules (len<=%d, %d-op alphabet) no ALLOW authorizes an effect or target outside the established healthy ceiling (Axiom-3/R_may closure)" % (_K, len(_OPS)),
      _bmc_violation is None, "schedules=%d allows=%d%s" % (_bmc_sched, _bmc_allows, "" if _bmc_violation is None else " VIOLATION sched=%r eff=%s" % _bmc_violation))

print()
if fail:
    print("MODEL CHECK: FAIL -- %d: %s" % (len(fail), ", ".join(fail))); sys.exit(1)
print("MODEL CHECK: PASS -- kernel(243) + antitone(%d) + bounded-auth-intro(%d schedules) + operational refinement on the executable" % (contracts, _bmc_sched))
sys.exit(0)

---

# Bismillah ir-Rahman ir-Rahim
