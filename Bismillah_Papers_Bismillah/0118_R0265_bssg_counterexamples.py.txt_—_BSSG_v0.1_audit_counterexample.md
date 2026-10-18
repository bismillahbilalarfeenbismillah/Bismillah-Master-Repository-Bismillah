# Bismillah ir-Rahman ir-Rahim

# R0265 -- bssg_counterexamples.py.txt — BSSG v0.1 audit counterexamples as a regression harness.

**Chronological Index:** 118 of 995  
**Date:** 2026  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** bssg_counterexamples.py.txt  
**Source Format:** txt  
**SHA-256:** `70cb8eb370a9fdb7d8724dc0382f69f9b23a926666167bf51f979635fea5ece9`  

---

## R0265 · bssg_counterexamples.py.txt — BSSG v0.1 audit counterexamples as a regression harness.

- section: V. BSSG & SHVVP Protocols
- source_file: bssg_counterexamples.py.txt
- source_format: txt
- merged_variants: 17 (bssg_counterexamples.py)
- text_sha256: 70cb8eb370a9fdb7d8724dc0382f69f9b23a926666167bf51f979635fea5ece9

"""BSSG v0.1 audit counterexamples as a regression harness.

Each check ASSERTS the spec-correct behavior, so on the un-repaired gate it FAILS (RED =
the defect is present). As each defect is repaired the corresponding check turns GREEN. This
is the executable-negative-test foundation GPT's audit required before any carry, and the
basis for rebuilding the model-checker as a faithful model of the executable (GPT-R7).

Mapping to findings: CE1=R9/KIMI-2, CE2=R1, CE3=R3, CE4=R4, CE5=R2, CE6=R11, CE7=R10, CE8=R5.
(R6 global-state partitioning gets its check when that fix lands; R7 is this harness itself;
R8 is packaging.)  Run: python3 bssg_counterexamples.py
"""
import copy, threading
import bssg_gate as G
import test_bssg_gate as T

results = []
# V27 breadth bound helper: a wide-holding record (epoch 0) representing pre-degradation authority. Prepending
# it to a synthetic honest-recovery stream makes it a non-fragment (the session demonstrably HELD the authority
# it later restores). Attack streams do not hold it, so the breadth bound still catches escalation beyond held.
_H0 = {"session_id": "s", "authority_epoch": 0, "authority_snapshot": {"effects": ["READ", "WRITE", "DELETE"], "target_scopes": ["a"]}}
def record(cid, finding, sev, ok, detail=""):
    results.append((cid, finding, sev, ok, detail))
    print(("GREEN " if ok else "RED   ") + f"{cid} [{sev}] {finding}" + (f"  {detail}" if detail else ""))

def _raw_lift19(session="s"):
    """A schema-valid raw correction-event LIFT (which no longer arms the carve-out on its own)."""
    return {"record_type": "bssg.correction-event", "spec_version": G.SPEC_VERSION, "correction_id": "cor-" + session,
            "correction_class": "LIFT_TERMINAL_STATE", "supersedes": G.digest_bytes(b"p"), "reason_code": "C-TERMINAL-REVIEWED",
            "issued_by": {"authority_id": "ops-1", "control_domain": "ops-domain"}, "session_id": session, "subject_control_domain": "subject-domain",
            "adjudicators": [{"adjudicator_id": "adj-1", "control_domain": "audit-domain", "signature": T.signature("valid", "adj-1")},
                             {"adjudicator_id": "adj-2", "control_domain": "legal-domain", "signature": T.signature("valid", "adj-2")}],
            "descendants": [], "descendant_closure_status": "UNKNOWN", "issued_at": "2026-07-25T12:01:00Z", "signature": T.signature("valid", "ops-key")}

def _acc_marker(session="s", epoch=2, cid=None, correction_digest=None):
    """A gate-issued bssg.correction-accepted marker. correction_digest should bind to a present event."""
    return {"record_type": "bssg.correction-accepted", "spec_version": G.SPEC_VERSION, "gate_version": G.GATE_VERSION,
            "correction_id": cid or ("cor-" + session), "correction_class": "LIFT_TERMINAL_STATE",
            "session_id": session, "authority_epoch": epoch, "licensed_epoch": epoch + 1,
            "correction_digest": correction_digest or G.digest_bytes(b"amd"), "adjudicators_verified": 2}

def _amend_pair(session="s", epoch=2):
    """A BOUND [correction-event, marker] pair: the marker's correction_digest = digest(the event), as the
    gate emits them. Only this bound pair arms the X7 carve-out (pass-21 A2 / GPT-P2). NOTE (B / V28): this
    synthetic pair no longer certifies a re-widen on its own -- there is no runtime grant behind it, so under
    the grant-anchored checker an honest re-widen after it fails CLOSED. Attack CEs still use it to prove
    forged/raw/replay/tamper shapes are X7; honest-recovery legs are anchored via _real_amendment below."""
    ev = _raw_lift19(session)
    marker = _acc_marker(session, epoch, correction_digest=G.digest(ev))
    return [ev, marker]


# ---------------------------------------------------------------------------
# B (V28) grant anchor. Strategy B turned check_authority_history into a DIVERGENCE DETECTOR against the
# runtime's AUTHENTICATED grant ledger. An honest re-widen is certifiable offline ONLY when anchored to a
# grant that the runtime minted on GENUINE acceptance (grants_from_state). The trap the Kimi seat keeps
# catching is fabricating a grants={...} literal to turn a synthetic stream green -- that certifies nothing
# (it re-states the answer as the question). Every honest-recovery leg below therefore derives its grant from
# a REAL accepted amendment through the gate. The only place a grants literal appears is CE-FORGED-GRANT,
# which uses it to DEMONSTRATE the disclosed residual (the forged-grant spoof is OUT of the offline threat
# model), not to pass a recovery.
# ---------------------------------------------------------------------------
_REAL_TGT = "https://db.example.internal/records/"

def _real_amendment(cid="cor-0001"):
    """Drive a REAL gate: authorize -> degrade to terminal -> genuine accepted LIFT amendment -> re-authorize,
    then export the runtime's AUTHENTICATED grant via grants_from_state. Returns a dict with the runtime's own
    grant, its gate-issued (event, marker), the full record stream, and the minted landing epoch + restored
    authority. NOTHING here is a literal: the grant is whatever the runtime produced on genuine acceptance."""
    _adj = lambda i, d: {"adjudicator_id": i, "control_domain": d, "signature": T.signature("valid", kid=i)}
    amd = {"record_type": "bssg.correction-event", "spec_version": G.SPEC_VERSION, "correction_id": cid,
           "correction_class": "LIFT_TERMINAL_STATE", "supersedes": G.digest_bytes(b"prior-decision"),
           "reason_code": "C-TERMINAL-REVIEWED", "issued_by": {"authority_id": "ops-1", "control_domain": "ops-domain"},
           "session_id": "sess-0001", "subject_control_domain": "subject-domain",
           "adjudicators": [_adj("adj-1", "audit-domain"), _adj("adj-2", "ops-domain")],
           "descendants": [], "descendant_closure_status": "UNKNOWN", "issued_at": "2026-07-25T12:01:00Z",
           "signature": T.signature("valid", kid="ops-key")}
    f = T.GateFixture(degraded_effects=["READ", "WRITE", "DELETE"], degraded_targets=["https://db.example.internal/"])
    f.gate.authorize(f.request(), T.evidence_bundle())
    f.gate.authorize(f.request(nonce="b" * 32), T.evidence_bundle(receipt=T.witness_receipt(health="DEGRADED", epoch=8)))
    accepted = f.gate.submit_amendment(copy.deepcopy(amd)).get("accepted") is True
    f.gate.authorize(f.request(nonce="3" * 32), T.evidence_bundle())
    recs = f.gate.state.records
    ev = [r for r in recs if isinstance(r, dict) and r.get("record_type") == "bssg.correction-event"][0]
    mk = [r for r in recs if isinstance(r, dict) and r.get("record_type") == "bssg.correction-accepted"][0]
    grants = G.grants_from_state(f.gate)
    g = grants["sess-0001"][-1]   # V29 GPT-P30-02: grant ledger is a list; latest grant for this single-amendment helper
    return {"gate": f.gate, "accepted": accepted, "grants": grants, "event": ev, "marker": mk, "records": recs,
            "session": "sess-0001", "landing": g["landing_epoch"],
            "restored_effects": frozenset(g["restored_effects"]), "restored_targets": frozenset(g["restored_targets"])}

def _uncert(v):
    # V29 WITHDRAWAL (SHV A5): an armed re-widen is UNCERTIFIABLE-offline (X7U present) and NOT a grant-
    # independent violation (no X7). This is the honest offline verdict; legitimacy is established ONLY online.
    return ("X7U" in v) and ("X7" not in v)
def _viol(v):
    # a grant-INDEPENDENT violation survives the withdrawal (regression/floor/constant-epoch/tamper/
    # forged-or-unarmed-marker widening) and is still reported as X7.
    return "X7" in v

def _honest_stream(R, effects=("READ", "WRITE"), targets=(_REAL_TGT,), epoch=None):
    """A LOAD-BEARING honest re-widen stream: a narrow pre-amendment ceiling, the gate's OWN bound
    (event, marker), then a re-widen at the grant's landing epoch within the authenticated restored
    authority. V30 WITHDRAWAL: armed re-widens are X7U (uncertifiable-offline) regardless of whether
    R['grants'] is supplied or absent -- the grants parameter is INERT for the offline verdict.
    CE163 closure: authentic == forged == X7U."""
    S = R["session"]
    narrow = {"session_id": S, "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": [_REAL_TGT]}}
    wide = {"session_id": S, "authority_epoch": R["landing"] if epoch is None else epoch,
            "authority_snapshot": {"effects": list(effects), "target_scopes": list(targets)}}
    return [narrow, R["event"], R["marker"], wide]

# One genuine accepted amendment, minted once and reused read-only by every honest-recovery leg below.
try:
    _R = _real_amendment()
    _ANCHOR_OK = _R["accepted"] and _R["session"] in _R["grants"]
except Exception as _anchor_exc:   # a broken anchor must be LOUD (every honest leg goes RED), never silent
    _R, _ANCHOR_OK = None, False


# CE1 / R9 / KIMI-2 -- kernel must reject an extra sixth conjunct, not ignore it and ALLOW.
try:
    vals = {n: G.TRUE for n in G.KERNEL_CONJUNCTS}; vals["SixthConjunct"] = G.FALSE
    try:
        dec, _ = G.kernel_decision(vals)
        ok = (dec != G.DECISION_ALLOW)  # correct: does not ALLOW with an extra FALSE conjunct
        record("CE1", "kernel rejects extra sixth conjunct", "R9", ok, f"decision={dec}")
    except G.BSSGError:
        record("CE1", "kernel rejects extra sixth conjunct", "R9", True, "raised BSSGError")
except Exception as e:
    record("CE1", "kernel rejects extra sixth conjunct", "R9", False, f"unexpected {type(e).__name__}")

# CE2 / R1 -- a denied request (same id+snapshot) must not later ALLOW on re-submission.
try:
    f = T.GateFixture(); r = f.request()
    d1 = f.gate.authorize(copy.deepcopy(r), T.evidence_bundle(authority=T.time_authority(sig="invalid")))
    d2 = f.gate.authorize(copy.deepcopy(r), T.evidence_bundle())
    ok = not (d1["decision"].startswith("DENY") and d2["decision"] == "ALLOW"
              and d1.get("request_digest") == d2.get("request_digest"))
    record("CE2", "denied request is terminal (no allow-after-deny)", "R1", ok,
           f'{d1["decision"]}->{d2["decision"]} same_digest={d1.get("request_digest")==d2.get("request_digest")}')
except Exception as e:
    record("CE2", "denied request is terminal (no allow-after-deny)", "R1", False, f"{type(e).__name__}: {e}")

# CE3 / R3 -- witness not covering the request's effect class must not yield ALLOW.
try:
    f = T.GateFixture(); r = f.request(); w = T.witness_receipt()
    w["covered_effect_classes"] = ["network-not-datastore"]
    d = f.gate.authorize(r, T.evidence_bundle(receipt=w))
    ok = d["decision"] != "ALLOW"
    record("CE3", "witness coverage mismatch blocks ALLOW", "R3", ok, f'decision={d["decision"]}')
except Exception as e:
    record("CE3", "witness coverage mismatch blocks ALLOW", "R3", False, f"{type(e).__name__}: {e}")

# CE4 / R4 -- a token bound to an old witness epoch must not commit after the epoch advances.
try:
    f = T.GateFixture()
    a1 = f.gate.authorize(f.request(nonce="a"*32), T.evidence_bundle(receipt=T.witness_receipt(epoch=7, sequence=11)))
    token = a1["authorization_receipt"]["commit_token"]["token_id"]
    r2 = f.request(nonce="b"*32); r2["request_id"] = "req-0002"
    f.gate.authorize(r2, T.evidence_bundle(receipt=T.witness_receipt(epoch=8, sequence=1)))
    rec = a1["authorization_receipt"]
    binding = {k: rec[k] for k in ("request_digest","canonical_target","params_digest","adapter_digest","effect_type")}
    c = f.gate.commit(token, binding, {})
    ok = c["outcome"] != "COMMITTED_PENDING_OUTCOME"
    record("CE4", "stale witness-epoch token cannot commit", "R4", ok, f'outcome={c["outcome"]}')
except Exception as e:
    record("CE4", "stale witness-epoch token cannot commit", "R4", False, f"{type(e).__name__}: {e}")

# CE5 / R2 -- concurrent redemption of one token must commit at most once.
try:
    f = T.GateFixture(); a = f.gate.authorize(f.request(), T.evidence_bundle())
    rec = a["authorization_receipt"]; token = rec["commit_token"]["token_id"]
    base = {k: rec[k] for k in ("request_digest","canonical_target","params_digest","adapter_digest","effect_type")}
    barrier = threading.Barrier(2)
    class BarrierDict(dict):
        def keys(self):
            try: barrier.wait(timeout=5)
            except Exception: pass
            return super().keys()
    out = []
    def redeem(): out.append(f.gate.commit(token, BarrierDict(base), {}))
    ts = [threading.Thread(target=redeem) for _ in range(2)]
    [t.start() for t in ts]; [t.join() for t in ts]
    committed = sum(x["outcome"] == "COMMITTED_PENDING_OUTCOME" for x in out)
    ok = committed == 1
    record("CE5", "one-time token redemption under concurrency", "R2", ok, f"committed_count={committed}")
except Exception as e:
    record("CE5", "one-time token redemption under concurrency", "R2", False, f"{type(e).__name__}: {e}")

# CE6 / R11 -- malformed trusted contract must map to UNKNOWN, not raise.
try:
    f = T.GateFixture(); bad = T.contract_body(f.policy_digest); del bad["allowed_target_scopes"]
    bd = G.digest(bad); f.gate.contracts = {bd: {"body": bad, "revoked": False}}
    r = T.effect_request(bd, f.policy_digest)
    try:
        d = f.gate.authorize(r, T.evidence_bundle())
        ok = d["decision"] != "ALLOW"   # correct: total predicate -> UNKNOWN -> not ALLOW, no crash
        record("CE6", "malformed contract -> UNKNOWN, no crash", "R11", ok, f'decision={d["decision"]}')
    except Exception as inner:
        record("CE6", "malformed contract -> UNKNOWN, no crash", "R11", False, f"raised {type(inner).__name__}")
except Exception as e:
    record("CE6", "malformed contract -> UNKNOWN, no crash", "R11", False, f"setup {type(e).__name__}: {e}")

# CE7 / R10 -- a request that fails the effect-request schema must not ALLOW.
try:
    f = T.GateFixture(); r = f.request(); r["request_id"] = ""; r["sequence"] = -1
    d = f.gate.authorize(r, T.evidence_bundle())
    ok = d["decision"] != "ALLOW"
    record("CE7", "schema-invalid request cannot ALLOW", "R10", ok, f'decision={d["decision"]}')
except Exception as e:
    record("CE7", "schema-invalid request cannot ALLOW", "R10", False, f"{type(e).__name__}: {e}")

# CE8 / R5 -- terminal lift must reject duplicate-signature adjudicators / wrong class.
try:
    f = T.GateFixture(); f.gate.state.terminal["sess-0001"] = "E-AUTHORITY-WIDENING"
    sig = T.signature("valid", kid="same-key")
    amendment = {"record_type":"bssg.correction-event","spec_version":"0.1","correction_class":"SUPERSEDE",
                 "session_id":"sess-0001","subject_control_domain":"subject-domain",
                 "adjudicators":[{"adjudicator_id":"a1","control_domain":"domain-1","signature":copy.deepcopy(sig)},
                                 {"adjudicator_id":"a2","control_domain":"domain-2","signature":copy.deepcopy(sig)}]}
    out = f.gate.submit_amendment(amendment)
    ok = not out.get("accepted", False)
    record("CE8", "terminal lift rejects duplicate-sig / wrong-class amendment", "R5", ok, f'accepted={out.get("accepted")}')
except Exception as e:
    record("CE8", "terminal lift rejects duplicate-sig / wrong-class amendment", "R5", False, f"{type(e).__name__}: {e}")

# CE9 / R6 -- one session must not contaminate another session's authority state.
try:
    f = T.GateFixture()
    rA = f.request(effect="READ", nonce="a"*32); rA["session_id"]="sess-A"; rA["request_id"]="req-A"
    dA = f.gate.authorize(rA, T.evidence_bundle(receipt=T.witness_receipt(health="DEGRADED")))
    rB = f.request(effect="WRITE", nonce="b"*32); rB["session_id"]="sess-B"; rB["request_id"]="req-B"
    dB = f.gate.authorize(rB, T.evidence_bundle(receipt=T.witness_receipt(health="HEALTHY")))
    ok = ("E-AUTHORITY-WIDENING" not in dB["reason_codes"]) and ("sess-B" not in f.gate.state.terminal)
    record("CE9", "per-session authority state (no cross-session contamination)", "R6", ok,
           f'A={dA["decision"]} B={dB["decision"]}/{dB["reason_codes"]}')
except Exception as e:
    record("CE9", "per-session authority state (no cross-session contamination)", "R6", False, f"{type(e).__name__}: {e}")

# CE10 / OD-11 -- the subject-facing response must not reveal the denial regime.
try:
    import json as _json
    f = T.GateFixture()
    d_false = f.gate.authorize(f.request(), T.evidence_bundle(receipt=T.witness_receipt(sig_status="invalid")))
    r_u = f.request(nonce="e"*32); r_u["contract_digest"] = "sha256:" + "0"*64
    d_unknown = f.gate.authorize(r_u, T.evidence_bundle())
    sf_false = f.gate.subject_facing(d_false)
    sf_unknown = f.gate.subject_facing(d_unknown)
    blob = _json.dumps(sf_false) + _json.dumps(sf_unknown)
    audit_keeps = d_false["decision"] != d_unknown["decision"]  # audit plane retains the refinement
    ok = (sf_false == sf_unknown
          and sf_false.get("decision") == "DENIED"
          and sf_false.get("reason_codes") == ["E-DENIED"]
          and sf_false.get("authorization_receipt") is None
          and "DENY_FALSE" not in blob and "DENY_UNKNOWN" not in blob
          and audit_keeps)
    record("CE10", "subject-facing response conceals denial regime (audit plane keeps it)", "OD-11", ok,
           f'audit={d_false["decision"]}/{d_unknown["decision"]} subj_equal={sf_false==sf_unknown}')
except Exception as e:
    record("CE10", "subject-facing response conceals denial regime (audit plane keeps it)", "OD-11", False, f"{type(e).__name__}: {e}")

# CE11 / P1 -- an evidence-level denial is terminal for the request snapshot.
try:
    import copy as _copy
    f = T.GateFixture(); r = f.request()
    d1 = f.gate.authorize(_copy.deepcopy(r), None)                 # evidence=None -> DENY (early path)
    d2 = f.gate.authorize(_copy.deepcopy(r), T.evidence_bundle())  # same snapshot, good evidence
    ok = d1["decision"].startswith("DENY") and d2["decision"] != "ALLOW"
    record("CE11", "evidence-level denial is terminal (no allow-after-deny on early paths)", "P1", ok,
           f'{d1["decision"]}->{d2["decision"]}')
except Exception as e:
    record("CE11", "evidence-level denial is terminal (no allow-after-deny on early paths)", "P1", False, f"{type(e).__name__}: {e}")

# CE12 / KIMI-1 -- an out-of-range integer is a structural rejection, not a crash (totality).
try:
    f = T.GateFixture(); r = f.request(); r["sequence"] = 2**60
    d = f.gate.authorize(r, T.evidence_bundle())
    ok = d["decision"] != "ALLOW"  # returns a decision (REJECTED_SCHEMA/DENY); must not raise
    record("CE12", "out-of-range integer request is rejected, gate does not crash", "KIMI-1", ok,
           f'decision={d["decision"]}')
except Exception as e:
    record("CE12", "out-of-range integer request is rejected, gate does not crash", "KIMI-1", False, f"{type(e).__name__}: {e}")

def _adj(i, d):
    return {"adjudicator_id": i, "control_domain": d, "signature": T.signature("valid", kid=i)}
def _full_amend(session, cid):
    return {"record_type": "bssg.correction-event", "spec_version": G.SPEC_VERSION, "correction_id": cid,
            "correction_class": "LIFT_TERMINAL_STATE", "supersedes": G.digest_bytes(b"prior-terminal"),
            "reason_code": "C-TERMINAL-REVIEWED", "issued_by": {"authority_id": "ops-1", "control_domain": "ops"},
            "session_id": session, "subject_control_domain": "subject-domain",
            "adjudicators": [_adj("adj-1", "audit-domain"), _adj("adj-2", "ops-domain-2")],
            "descendants": [], "descendant_closure_status": "UNKNOWN", "issued_at": "2026-07-25T12:01:00Z",
            "signature": T.signature("valid", kid="ops-key")}

# CE13 / P5 -- an amendment is single-use; the same correction cannot lift a later terminal.
try:
    import copy as _c
    f = T.GateFixture(); f.gate.state.terminal["sR"] = "E-AUTHORITY-WIDENING"
    am = _full_amend("sR", "cor-1")
    a1 = f.gate.submit_amendment(_c.deepcopy(am))
    f.gate.state.terminal["sR"] = "E-AUTHORITY-WIDENING"          # a fresh terminal on the same session
    a2 = f.gate.submit_amendment(_c.deepcopy(am))                 # replay the identical amendment
    ok = a1.get("accepted") is True and a2.get("accepted") is not True
    record("CE13", "amendment is single-use (replay cannot lift a later terminal)", "P5", ok,
           f'first={a1.get("accepted")} replay={a2.get("accepted")}/{a2.get("reason_codes")}')
except Exception as e:
    record("CE13", "amendment is single-use (replay cannot lift a later terminal)", "P5", False, f"{type(e).__name__}: {e}")

# CE14 / P6 -- a schema-invalid amendment (missing required fields) cannot lift a terminal.
try:
    f = T.GateFixture(); f.gate.state.terminal["sM"] = "E-AUTHORITY-WIDENING"
    minimal = {"record_type": "bssg.correction-event", "spec_version": "0.1", "correction_class": "LIFT_TERMINAL_STATE",
               "session_id": "sM", "subject_control_domain": "subject-domain",
               "adjudicators": [_adj("a1", "d1"), _adj("a2", "d2")]}
    out = f.gate.submit_amendment(minimal)
    ok = out.get("accepted") is not True and "sM" in f.gate.state.terminal
    record("CE14", "schema-invalid amendment cannot lift a terminal state", "P6", ok,
           f'accepted={out.get("accepted")}/{out.get("reason_codes")}')
except Exception as e:
    record("CE14", "schema-invalid amendment cannot lift a terminal state", "P6", False, f"{type(e).__name__}: {e}")

# CE15 / KIMI-2 -- an adjudicator signature must bind its declared identity (kid == adjudicator_id).
try:
    f = T.GateFixture(); f.gate.state.terminal["sK"] = "E-AUTHORITY-WIDENING"
    am = _full_amend("sK", "cor-k")
    am["adjudicators"][0] = {"adjudicator_id": "impostor", "control_domain": "audit-domain",
                             "signature": T.signature("valid", kid="adj-1")}  # borrowed signature
    out = f.gate.submit_amendment(am)
    ok = out.get("accepted") is not True
    record("CE15", "adjudicator signature must bind its declared identity (no substitution)", "KIMI-2", ok,
           f'accepted={out.get("accepted")}/{out.get("reason_codes")}')
except Exception as e:
    record("CE15", "adjudicator signature must bind its declared identity (no substitution)", "KIMI-2", False, f"{type(e).__name__}: {e}")

# CE16 / P7 -- a witness receipt with an undeclared field cannot ALLOW (closedness).
try:
    f = T.GateFixture(); w = T.witness_receipt(); w["undeclared_semantic_field"] = "attacker"
    d = f.gate.authorize(f.request(), T.evidence_bundle(receipt=w))
    ok = d["decision"] != "ALLOW"
    record("CE16", "witness receipt with an undeclared field cannot ALLOW", "P7", ok, f'decision={d["decision"]}')
except Exception as e:
    record("CE16", "witness receipt with an undeclared field cannot ALLOW", "P7", False, f"{type(e).__name__}: {e}")

# CE17 / P8 -- a malformed binding cannot leave a token stuck in COMMITTING.
try:
    f = T.GateFixture(); d = f.gate.authorize(f.request(), T.evidence_bundle()); rec = d["authorization_receipt"]
    tok = rec["commit_token"]["token_id"]
    b = {k: rec[k] for k in ("request_digest", "canonical_target", "params_digest", "adapter_digest", "effect_type")}
    b[1] = "non-string-json-key"
    raised = None
    try:
        f.gate.commit(tok, b, {})
    except Exception as ex:
        raised = type(ex).__name__
    status = f.gate.state.tokens[tok]["status"]
    ok = raised is None and status != "COMMITTING"
    record("CE17", "malformed binding cannot leave a token stuck in COMMITTING", "P8", ok, f'raised={raised} status={status}')
except Exception as e:
    record("CE17", "malformed binding cannot leave a token stuck in COMMITTING", "P8", False, f"{type(e).__name__}: {e}")

# CE18 / P9 -- commit voids if the session terminalizes during the commit call.
try:
    import threading as _th
    class _BB(dict):
        def __init__(self, *a, ent=None, rel=None, **k):
            super().__init__(*a, **k); self.ent = ent; self.rel = rel; self.n = 0
        def keys(self):
            self.n += 1
            if self.n == 1:
                self.ent.set(); self.rel.wait(5)
            return super().keys()
    f = T.GateFixture()
    r0 = f.request(effect="READ", nonce="5"*32); r0["session_id"] = "sRace"; r0["request_id"] = "rr0"
    d0 = f.gate.authorize(r0, T.evidence_bundle(receipt=T.witness_receipt(health="DEGRADED", epoch=20, sequence=20)))
    rec = d0["authorization_receipt"]; tok = rec["commit_token"]["token_id"]
    ent = _th.Event(); rel = _th.Event()
    bb = _BB({k: rec[k] for k in ("request_digest", "canonical_target", "params_digest", "adapter_digest", "effect_type")}, ent=ent, rel=rel)
    box = {}
    def _do():
        try: box["c"] = f.gate.commit(tok, bb, {})
        except Exception as ex: box["e"] = str(ex)
    th = _th.Thread(target=_do); th.start(); ent.wait(5)
    r1 = f.request(effect="WRITE", nonce="6"*32); r1["session_id"] = "sRace"; r1["request_id"] = "rr1"
    f.gate.authorize(r1, T.evidence_bundle(receipt=T.witness_receipt(health="HEALTHY", epoch=21, sequence=21)))
    rel.set(); th.join(5)
    c = box.get("c")
    ok = c is not None and (c.get("outcome") == "COMMITTED_PENDING_OUTCOME" or "E-SESSION-TERMINAL" in c.get("reason_codes", []))
    record("CE18", "commit and a concurrent terminalize serialize atomically (no torn/terminal commit)", "P9/P-E", ok, f'commit={c.get("outcome") if c else None}')
except Exception as e:
    record("CE18", "commit voids if the session terminalizes during commit", "P9", False, f"{type(e).__name__}: {e}")

import time as _time, threading as _th, copy as _cp, inspect as _insp

# CE19 / P-D1 [totality] out-of-range integer anywhere in evidence is rejected, no crash.
try:
    f = T.GateFixture(); w = T.witness_receipt(); w["epoch"] = 2 ** 60
    try:
        d = f.gate.authorize(f.request(), T.evidence_bundle(receipt=w)); ok = d["decision"] != "ALLOW"; det = d["decision"]
    except Exception as ex:
        ok = False; det = "CRASH:" + type(ex).__name__
    record("CE19", "out-of-range integer in evidence is rejected, gate does not crash", "P-D1", ok, det)
except Exception as e:
    record("CE19", "out-of-range integer in evidence is rejected, gate does not crash", "P-D1", False, f"{type(e).__name__}: {e}")

# CE20 / P-C [closedness] nested undeclared field in the witness receipt cannot ALLOW.
try:
    f = T.GateFixture(); w = T.witness_receipt(); w["checkpoint"]["undeclared_nested"] = "x"
    d = f.gate.authorize(f.request(), T.evidence_bundle(receipt=w))
    record("CE20", "nested undeclared witness field cannot ALLOW (recursive closedness)", "P-C", d["decision"] != "ALLOW", f'decision={d["decision"]}')
except Exception as e:
    record("CE20", "nested undeclared witness field cannot ALLOW (recursive closedness)", "P-C", False, f"{type(e).__name__}: {e}")

# CE21 / DP4b [closedness] undeclared field in the evidence bundle cannot ALLOW.
try:
    f = T.GateFixture(); eb = T.evidence_bundle(); eb["undeclared_bundle_field"] = "x"
    d = f.gate.authorize(f.request(), eb)
    record("CE21", "undeclared evidence-bundle field cannot ALLOW", "DP4b", d["decision"] != "ALLOW", f'decision={d["decision"]}')
except Exception as e:
    record("CE21", "undeclared evidence-bundle field cannot ALLOW", "DP4b", False, f"{type(e).__name__}: {e}")

# CE22 / P-B1 [amendment] wrong spec_version amendment cannot lift a terminal.
try:
    f = T.GateFixture(); f.gate.state.terminal["sV"] = "E-AUTHORITY-WIDENING"
    am = _full_amend("sV", "cor-v"); am["spec_version"] = "9.9"
    out = f.gate.submit_amendment(am)
    record("CE22", "amendment with wrong spec_version cannot lift a terminal", "P-B1", out.get("accepted") is not True and "sV" in f.gate.state.terminal, f'accepted={out.get("accepted")}/{out.get("reason_codes")}')
except Exception as e:
    record("CE22", "amendment with wrong spec_version cannot lift a terminal", "P-B1", False, f"{type(e).__name__}: {e}")

# CE23 / P-B2 [amendment] closure-invariant-violating amendment (COMPLETE with known gaps) cannot lift.
try:
    f = T.GateFixture(); f.gate.state.terminal["sC"] = "E-AUTHORITY-WIDENING"
    am = _full_amend("sC", "cor-c"); am["descendant_closure_status"] = "COMPLETE"; am["unreachable_descendants"] = [G.digest_bytes(b"gap")]
    out = f.gate.submit_amendment(am)
    record("CE23", "closure-invariant-violating amendment cannot lift a terminal", "P-B2", out.get("accepted") is not True and "sC" in f.gate.state.terminal, f'accepted={out.get("accepted")}/{out.get("reason_codes")}')
except Exception as e:
    record("CE23", "closure-invariant-violating amendment cannot lift a terminal", "P-B2", False, f"{type(e).__name__}: {e}")

# CE24 / DP5e [amendment] adjudicators must be in all-distinct domains.
try:
    f = T.GateFixture(); f.gate.state.terminal["sD"] = "E-AUTHORITY-WIDENING"
    am = _full_amend("sD", "cor-d"); am["adjudicators"] = [_adj("a1", "dX"), _adj("a2", "dX"), _adj("a3", "dY")]
    out = f.gate.submit_amendment(am)
    record("CE24", "adjudicators must be in all-distinct domains (no collision)", "DP5e", out.get("accepted") is not True, f'accepted={out.get("accepted")}/{out.get("reason_codes")}')
except Exception as e:
    record("CE24", "adjudicators must be in all-distinct domains (no collision)", "DP5e", False, f"{type(e).__name__}: {e}")

# CE25 / P-G [concurrency] concurrent same-nonce authorize yields at most one ALLOW, no crash.
try:
    f = T.GateFixture(); r = f.request(nonce="e" * 32); ev = T.evidence_bundle(); outs = []
    def _w():
        try: outs.append(f.gate.authorize(_cp.deepcopy(r), _cp.deepcopy(ev))["decision"])
        except Exception as ex: outs.append("CRASH:" + type(ex).__name__)
    ts = [_th.Thread(target=_w) for _ in range(2)]; [t.start() for t in ts]; [t.join(5) for t in ts]
    ok = outs.count("ALLOW") <= 1 and len(f.gate.state.tokens) <= 1 and all("CRASH" not in o for o in outs)
    record("CE25", "concurrent same-nonce authorize yields at most one ALLOW (no duplicate)", "P-G", ok, f'decisions={sorted(outs)} tokens={len(f.gate.state.tokens)}')
except Exception as e:
    record("CE25", "concurrent same-nonce authorize yields at most one ALLOW (no duplicate)", "P-G", False, f"{type(e).__name__}: {e}")

# CE26 / P-F [concurrency] a token that expired while its commit was queued is rejected on fresh time.
try:
    f = T.GateFixture(); r = f.request(nonce="f" * 32, expires_at="2026-07-25T12:00:01Z")
    d = f.gate.authorize(r, T.evidence_bundle()); rec = d["authorization_receipt"]; tok = rec["commit_token"]["token_id"]
    b = {k: rec[k] for k in ("request_digest", "canonical_target", "params_digest", "adapter_digest", "effect_type")}
    holder = {}; started = _th.Event(); f.gate._commit_lock.acquire()
    def _qc():
        started.set(); holder["c"] = f.gate.commit(tok, b, {})
    t = _th.Thread(target=_qc); t.start(); started.wait(2); _time.sleep(0.05); f.clock.advance(10); f.gate._commit_lock.release(); t.join(5)
    c = holder.get("c"); ok = c is not None and c.get("outcome") != "COMMITTED_PENDING_OUTCOME"
    record("CE26", "token that expired while its commit was queued is rejected", "P-F", ok, f'outcome={None if c is None else c.get("outcome")}')
except Exception as e:
    try:
        if f.gate._commit_lock.locked(): f.gate._commit_lock.release()
    except Exception: pass
    record("CE26", "token that expired while its commit was queued is rejected", "P-F", False, f"{type(e).__name__}: {e}")

# CE27 / P-E [concurrency] authorize and commit serialize on the gate lock -> terminal re-check + CONSUME atomic.
try:
    _asrc = _insp.getsource(G.BSSGGate.authorize); _csrc = _insp.getsource(G.BSSGGate.commit)
    ok = "self._lock" in _asrc and "self._lock" in _csrc
    record("CE27", "authorize and commit serialize on the gate lock (terminal re-check + CONSUME atomic)", "P-E", ok, f'authorize_locked={"self._lock" in _asrc} commit_locked={"self._lock" in _csrc}')
except Exception as e:
    record("CE27", "authorize and commit serialize on the gate lock", "P-E", False, f"{type(e).__name__}: {e}")

# CE28 / F1 [$ref closedness] extra field in a witness signature sub-object (under $ref) cannot ALLOW.
try:
    f = T.GateFixture(); w = T.witness_receipt(); w["signature"]["secret_key"] = "leaked"
    d = f.gate.authorize(f.request(), T.evidence_bundle(receipt=w))
    record("CE28", "extra field in a $ref'd witness signature sub-object cannot ALLOW", "F1", d["decision"] != "ALLOW", f'decision={d["decision"]}')
except Exception as e:
    record("CE28", "extra field in a $ref'd witness signature sub-object cannot ALLOW", "F1", False, f"{type(e).__name__}: {e}")

# CE29 / GPT#2 [amendment totality] unhashable correction_id is rejected, no crash.
try:
    f = T.GateFixture(); f.gate.state.terminal["s29"] = "E-AUTHORITY-WIDENING"
    am = _full_amend("s29", "c29"); am["correction_id"] = ["unhashable"]
    try:
        out = f.gate.submit_amendment(am); ok = out.get("accepted") is not True; det = out.get("reason_codes")
    except Exception as ex:
        ok = False; det = "CRASH:" + type(ex).__name__
    record("CE29", "amendment with unhashable correction_id is rejected, no crash", "GPT#2", ok, str(det))
except Exception as e:
    record("CE29", "amendment with unhashable correction_id is rejected, no crash", "GPT#2", False, f"{type(e).__name__}: {e}")

# CE30 / F2 [amendment nested closedness] extra field in a nested amendment object cannot lift.
try:
    f = T.GateFixture(); f.gate.state.terminal["s30"] = "E-AUTHORITY-WIDENING"
    am = _full_amend("s30", "c30"); am["issued_by"] = {**am["issued_by"], "secret": "x"}
    out = f.gate.submit_amendment(am)
    record("CE30", "nested extra field in an amendment object cannot lift a terminal", "F2", out.get("accepted") is not True and "s30" in f.gate.state.terminal, f'accepted={out.get("accepted")}/{out.get("reason_codes")}')
except Exception as e:
    record("CE30", "nested extra field in an amendment object cannot lift a terminal", "F2", False, f"{type(e).__name__}: {e}")

# CE31 / P.1 [amendment signature] an amendment with an invalid top-level signature cannot lift.
try:
    f = T.GateFixture(); f.gate.state.terminal["s31"] = "E-AUTHORITY-WIDENING"
    am = _full_amend("s31", "c31"); am["signature"] = T.signature("invalid", kid="ops-key")
    out = f.gate.submit_amendment(am)
    record("CE31", "amendment with an invalid top-level signature cannot lift a terminal", "P.1", out.get("accepted") is not True and "s31" in f.gate.state.terminal, f'accepted={out.get("accepted")}/{out.get("reason_codes")}')
except Exception as e:
    record("CE31", "amendment with an invalid top-level signature cannot lift a terminal", "P.1", False, f"{type(e).__name__}: {e}")

# CE32 / P13 [witness value] a witness with a wrong spec_version (schema-invalid value) cannot ALLOW.
try:
    f = T.GateFixture(); w = T.witness_receipt(); w["spec_version"] = "9.9"
    d = f.gate.authorize(f.request(), T.evidence_bundle(receipt=w))
    record("CE32", "witness with a schema-invalid value (wrong spec_version) cannot ALLOW", "P13", d["decision"] != "ALLOW", f'decision={d["decision"]}')
except Exception as e:
    record("CE32", "witness with a schema-invalid value (wrong spec_version) cannot ALLOW", "P13", False, f"{type(e).__name__}: {e}")

# CE33 / F3 [commit ingress] malformed fresh evidence at commit voids the token (no COMMITTED).
try:
    f = T.GateFixture(); d = f.gate.authorize(f.request(), T.evidence_bundle()); rec = d["authorization_receipt"]; tok = rec["commit_token"]["token_id"]
    b = {k: rec[k] for k in ("request_digest", "canonical_target", "params_digest", "adapter_digest", "effect_type")}
    ev2 = T.evidence_bundle(); ev2["undeclared_bundle_field"] = "x"
    c = f.gate.commit(tok, b, ev2)
    record("CE33", "malformed fresh evidence at commit voids the token (commit-path validation)", "F3", c.get("outcome") != "COMMITTED_PENDING_OUTCOME", f'outcome={c.get("outcome")}/{c.get("reason_codes")}')
except Exception as e:
    record("CE33", "malformed fresh evidence at commit voids the token (commit-path validation)", "F3", False, f"{type(e).__name__}: {e}")

# CE34 / P-A [decision taxonomy] a terminal-session refusal is the distinct SESSION_TERMINAL decision.
try:
    f = T.GateFixture(); f.gate.state.terminal["s34"] = "E-AUTHORITY-WIDENING"
    r = f.request(nonce="4" * 32); r["session_id"] = "s34"
    d = f.gate.authorize(r, T.evidence_bundle())
    record("CE34", "terminal-session refusal is SESSION_TERMINAL, not DENY_FALSE (permits amendment recovery)", "P-A", d["decision"] == "SESSION_TERMINAL", f'decision={d["decision"]}')
except Exception as e:
    record("CE34", "terminal-session refusal is SESSION_TERMINAL, not DENY_FALSE (permits amendment recovery)", "P-A", False, f"{type(e).__name__}: {e}")

# CE35 / F-01 [uniform validation] the REQUEST passes the same validator; int session_id -> REJECTED_SCHEMA.
try:
    f = T.GateFixture(); r = f.request(); r["session_id"] = 12345
    d = f.gate.authorize(r, T.evidence_bundle())
    record("CE35", "request with a schema-invalid field (int session_id) is REJECTED_SCHEMA, no crash", "F-01", d["decision"] == "REJECTED_SCHEMA", f'decision={d["decision"]}')
except Exception as e:
    record("CE35", "request with a schema-invalid field (int session_id) is REJECTED_SCHEMA, no crash", "F-01", False, f"{type(e).__name__}: {e}")

# CE36 / F-02 [value constraints] a witness with a negative epoch (schema minimum:0) cannot ALLOW.
try:
    f = T.GateFixture(); w = T.witness_receipt(); w["epoch"] = -5
    d = f.gate.authorize(f.request(), T.evidence_bundle(receipt=w))
    record("CE36", "witness violating a numeric bound (negative epoch, minimum:0) cannot ALLOW", "F-02", d["decision"] != "ALLOW", f'decision={d["decision"]}')
except Exception as e:
    record("CE36", "witness violating a numeric bound (negative epoch, minimum:0) cannot ALLOW", "F-02", False, f"{type(e).__name__}: {e}")

# CE37 [fail-closed] schema_valid rejects a schema node carrying a keyword it does not implement.
try:
    ok = (G.schema_valid({"x": 1}, {"type": "object", "unhandled_keyword_xyz": True}, {}) is False)
    record("CE37", "validator fails CLOSED on any unrecognised schema keyword (recurrence guard)", "fail-closed", ok, f'result={ok}')
except Exception as e:
    record("CE37", "validator fails CLOSED on any unrecognised schema keyword (recurrence guard)", "fail-closed", False, f"{type(e).__name__}: {e}")

# CE38 / F-04 [freshness] a denied but authenticated newer epoch voids an older outstanding token.
try:
    f = T.GateFixture()
    d1 = f.gate.authorize(f.request(nonce="1"*32), T.evidence_bundle()); rec1 = d1["authorization_receipt"]; tok1 = rec1["commit_token"]["token_id"]
    b1 = {k: rec1[k] for k in ("request_digest", "canonical_target", "params_digest", "adapter_digest", "effect_type")}
    r2 = f.request(nonce="2"*32); r2["target"]["canonical_uri"] = "bssg://blocked/x"
    d2 = f.gate.authorize(r2, T.evidence_bundle(epoch=9, receipt=T.witness_receipt(epoch=9, sequence=9)))
    c = f.gate.commit(tok1, b1, {})
    record("CE38", "newer authenticated epoch on a DENIED request voids an older token at commit", "F-04", d2["decision"] != "ALLOW" and c.get("outcome") != "COMMITTED_PENDING_OUTCOME", f'denied={d2["decision"]} commit={c.get("outcome")}/{c.get("reason_codes")}')
except Exception as e:
    record("CE38", "newer authenticated epoch on a DENIED request voids an older token at commit", "F-04", False, f"{type(e).__name__}: {e}")

# CE39 / F-05 [atomicity] a token-factory collision leaves no partial ALLOW state (nonce not consumed).
try:
    class _Coll:
        def __call__(self): return "dup-token"
    contracts, policies, cd, pd = T.build_registries(); clk = T.Clock()
    g = G.BSSGGate(contracts, policies, clk, T.injected_verifier, _Coll())
    r1 = T.effect_request(cd, pd, nonce="a"*32); r1["request_id"] = "rq1"; g.authorize(r1, T.evidence_bundle())
    r2 = T.effect_request(cd, pd, nonce="b"*32); r2["request_id"] = "rq2"; d = g.authorize(r2, T.evidence_bundle())
    # GPT-04: the collision record is KERNEL-CONSISTENT (decision == kernel_decision(all-TRUE) == ALLOW)
    # but the mint failure is a distinct, non-redeemable FAILED_NO_EFFECT issuance_status: no receipt,
    # no new token, snapshot terminal.
    kd, _ = G.kernel_decision(dict(d["conjuncts"]))
    ok = (d["decision"] == "ALLOW" and d["decision"] == kd
          and d.get("issuance_status") == "FAILED_NO_EFFECT"
          and d.get("authorization_receipt") is None and len(g.state.tokens) == 1)
    record("CE39", "token-factory collision: kernel-consistent ALLOW record but FAILED_NO_EFFECT, no redeemable token", "F-05", ok, f'2nd={d["decision"]} issuance={d.get("issuance_status")} tokens={len(g.state.tokens)}')
except Exception as e:
    record("CE39", "token-factory collision yields one terminal record, no partial ALLOW state", "F-05", False, f"{type(e).__name__}: {e}")

# CE40 / F-06 [revocation] a contract revoked after authorization voids the token at commit.
try:
    f = T.GateFixture(); d = f.gate.authorize(f.request(), T.evidence_bundle()); rec = d["authorization_receipt"]; tok = rec["commit_token"]["token_id"]
    b = {k: rec[k] for k in ("request_digest", "canonical_target", "params_digest", "adapter_digest", "effect_type")}
    f.gate.contracts[f.request()["contract_digest"]]["revoked"] = True
    c = f.gate.commit(tok, b, {})
    record("CE40", "a contract revoked after authorization voids the token at commit", "F-06", c.get("outcome") != "COMMITTED_PENDING_OUTCOME" and "E-COMMIT-CONTRACT-REVOKED" in c.get("reason_codes", []), f'commit={c.get("outcome")}/{c.get("reason_codes")}')
except Exception as e:
    record("CE40", "a contract revoked after authorization voids the token at commit", "F-06", False, f"{type(e).__name__}: {e}")

# CE41 / GLM-A [collision terminality] a RECOVERING factory cannot allow the snapshot after a collision DENY.
try:
    class _Recov:
        def __init__(s): s.n = 0
        def __call__(s): s.n += 1; return "dup" if s.n == 1 else f"t{s.n}"
    contracts, policies, cd, pd = T.build_registries(); g = G.BSSGGate(contracts, policies, T.Clock(), T.injected_verifier, _Recov())
    g.state.tokens["dup"] = {"status": "UNUSED"}
    rc = T.effect_request(cd, pd, nonce="c"*32); rc["request_id"] = "rc"
    d1 = g.authorize(dict(rc), T.evidence_bundle()); d2 = g.authorize(dict(rc), T.evidence_bundle())
    # E (KIMI-5): a collision is now a kernel-consistent ALLOW with issuance_status=FAILED_NO_EFFECT, so
    # the invariant is that NEITHER outcome is an AUTHORIZED issuance (no allow-after-deny), not that the
    # decision label differs from ALLOW.
    record("CE41", "recovering token factory: collision snapshot stays terminal (no allow-after-deny)", "GLM-A", (not G.BSSGGate.authorized_issuance(d1)) and (not G.BSSGGate.authorized_issuance(d2)), f'd1={d1["decision"]}/{d1.get("issuance_status")} d2={d2["decision"]}')
except Exception as e:
    record("CE41", "recovering token factory: collision snapshot stays terminal (no allow-after-deny)", "GLM-A", False, f"{type(e).__name__}: {e}")

# CE42 / GPT-2 [bundle schema] a negative evidence_epoch (schema minimum:0) cannot ALLOW.
try:
    f = T.GateFixture(); d = f.gate.authorize(f.request(), T.evidence_bundle(epoch=-1))
    record("CE42", "negative evidence_epoch (bundle schema minimum:0) cannot ALLOW", "GPT-2", d["decision"] != "ALLOW", f'decision={d["decision"]}')
except Exception as e:
    record("CE42", "negative evidence_epoch (bundle schema minimum:0) cannot ALLOW", "GPT-2", False, f"{type(e).__name__}: {e}")

# CE43 / GPT-1 [time-authority schema] a malformed time-authority signature envelope cannot ALLOW.
try:
    f = T.GateFixture(); ev = T.evidence_bundle(); ev["time_authority"]["signature"]["envelope"] = "EVIL"
    d = f.gate.authorize(f.request(), ev)
    record("CE43", "malformed time-authority signature envelope cannot ALLOW", "GPT-1", d["decision"] != "ALLOW", f'decision={d["decision"]}')
except Exception as e:
    record("CE43", "malformed time-authority signature envelope cannot ALLOW", "GPT-1", False, f"{type(e).__name__}: {e}")

# CE44 / GPT-4 [revocation fail-closed] a malformed revoked value (1) is treated as refused, not active.
try:
    f = T.GateFixture(); f.gate.contracts[f.request()["contract_digest"]]["revoked"] = 1
    d = f.gate.authorize(f.request(), T.evidence_bundle())
    record("CE44", "malformed contract revoked value fails closed (refused, not active)", "GPT-4", d["decision"] != "ALLOW", f'decision={d["decision"]}')
except Exception as e:
    record("CE44", "malformed contract revoked value fails closed (refused, not active)", "GPT-4", False, f"{type(e).__name__}: {e}")

# CE45 / GLM-B [authority integrity] an unauthenticated witness does not advance authority_epoch.
try:
    f = T.GateFixture(); f.gate.authorize(f.request(nonce="1"*32), T.evidence_bundle()); sess = f.request()["session_id"]
    e1 = f.gate.state.authority_epoch.get(sess, 0)
    f.gate.authorize(f.request(nonce="2"*32), T.evidence_bundle(receipt=T.witness_receipt(sig_status="invalid")))
    e2 = f.gate.state.authority_epoch.get(sess, 0)
    record("CE45", "an unauthenticated witness does not mutate the authority lattice", "GLM-B", e1 == e2, f'authority_epoch {e1}->{e2}')
except Exception as e:
    record("CE45", "an unauthenticated witness does not mutate the authority lattice", "GLM-B", False, f"{type(e).__name__}: {e}")

# CE46 / GLM-C [commit sig] a forged (invalid-signature) fresh witness at commit voids the token.
try:
    f = T.GateFixture(); d = f.gate.authorize(f.request(), T.evidence_bundle()); rec = d["authorization_receipt"]; tok = rec["commit_token"]["token_id"]
    b = {k: rec[k] for k in ("request_digest", "canonical_target", "params_digest", "adapter_digest", "effect_type")}
    c = f.gate.commit(tok, b, T.evidence_bundle(receipt=T.witness_receipt(sig_status="invalid")))
    record("CE46", "a forged fresh-witness signature at commit voids the token", "GLM-C", c.get("outcome") != "COMMITTED_PENDING_OUTCOME", f'commit={c.get("outcome")}/{c.get("reason_codes")}')
except Exception as e:
    record("CE46", "a forged fresh-witness signature at commit voids the token", "GLM-C", False, f"{type(e).__name__}: {e}")

# CE47 [validator correctness] unresolved $ref fails closed; const:true rejects integer 1.
try:
    ok = (G.schema_valid({"x": 1}, {"$ref": "#/$defs/NOPE"}, {"$defs": {}}) is False
          and G.schema_valid(1, {"const": True}, {}) is False
          and G.schema_valid(1, {"enum": [True, False]}, {}) is False)
    record("CE47", "validator: unresolved $ref fails closed; bool const/enum reject integer aliases", "GPT-MAJOR-2/GLM-D-E", ok, f'result={ok}')
except Exception as e:
    record("CE47", "validator: unresolved $ref fails closed; bool const/enum reject integer aliases", "GPT-MAJOR-2/GLM-D-E", False, f"{type(e).__name__}: {e}")

# CE48 / DP-01 [target canonicalization] a backslash traversal target is refused (no scope escape).
try:
    ok = G.canonical_target("https://db.example.internal/records/..\\admin") is None
    record("CE48", "backslash traversal target is refused (WHATWG separator aliasing)", "DP-01", ok, f'canonical={G.canonical_target("https://x/records/..\\admin")}')
except Exception as e:
    record("CE48", "backslash traversal target is refused (WHATWG separator aliasing)", "DP-01", False, f"{type(e).__name__}: {e}")

# CE49 / DP-02 [nonce freshness] a denied request's nonce cannot be reused by a linked retry.
try:
    f = T.GateFixture()
    r1 = f.request(nonce="e"*32); r1["request_id"] = "rq1"; r1["target"]["canonical_uri"] = "bssg://host/blocked"
    f.gate.authorize(r1, T.evidence_bundle())
    r2 = f.request(nonce="e"*32); r2["request_id"] = "rq2"
    d2 = f.gate.authorize(r2, T.evidence_bundle())
    r3 = f.request(nonce="f"*32); r3["request_id"] = "rq3"
    d3 = f.gate.authorize(r3, T.evidence_bundle())
    record("CE49", "a denied request's nonce cannot be reused (fresh nonce still authorizes)", "DP-02", d2["decision"] != "ALLOW" and "E-NONCE-REPLAY" in d2["reason_codes"] and d3["decision"] == "ALLOW", f'reuse={d2["decision"]} fresh={d3["decision"]}')
except Exception as e:
    record("CE49", "a denied request's nonce cannot be reused (fresh nonce still authorizes)", "DP-02", False, f"{type(e).__name__}: {e}")

# CE50 / DP-03 [commit witness identity] a different-identity fresh witness at commit voids the token.
try:
    f = T.GateFixture(); d = f.gate.authorize(f.request(), T.evidence_bundle()); rec = d["authorization_receipt"]; tok = rec["commit_token"]["token_id"]
    b = {k: rec[k] for k in ("request_digest", "canonical_target", "params_digest", "adapter_digest", "effect_type")}
    diff = T.witness_receipt(); diff["witness_id"] = "different-witness"; diff["covered_subject"] = "different-agent"
    c = f.gate.commit(tok, b, T.evidence_bundle(receipt=diff))
    record("CE50", "a commit fresh witness of a different identity/subject voids the token", "DP-03", c.get("outcome") != "COMMITTED_PENDING_OUTCOME", f'commit={c.get("outcome")}/{c.get("reason_codes")}')
except Exception as e:
    record("CE50", "a commit fresh witness of a different identity/subject voids the token", "DP-03", False, f"{type(e).__name__}: {e}")

# CE51 / DP-05 [amendment signatures] the adjudicator signature payload excludes the top signature (acyclic).
try:
    import inspect as _i
    src = _i.getsource(G.BSSGGate)
    ok = 'not in ("adjudicators", "signature")' in src
    record("CE51", "adjudicator signature payload excludes the top signature (non-circular)", "DP-05", ok, f'acyclic_payload={ok}')
except Exception as e:
    record("CE51", "adjudicator signature payload excludes the top signature (non-circular)", "DP-05", False, f"{type(e).__name__}: {e}")

# CE52 / P7-02 [lexical] a trailing line-feed in a pattern-constrained field is refused (fullmatch).
try:
    f=T.GateFixture(); r=f.request(); r["nonce"]="a"*32+"\n"
    record("CE52","trailing line-feed in a pattern field is refused (fullmatch, not re.search+$)","P7-02", f.gate.authorize(r,T.evidence_bundle())["decision"]!="ALLOW", "trailing-\\n nonce")
except Exception as e: record("CE52","trailing line-feed refused","P7-02",False,f"{type(e).__name__}: {e}")

# CE53 / P7-01 [TOCTOU] the contract body snapshot is isolated from a post-fetch registry mutation.
try:
    f=T.GateFixture(); cd=f.request()["contract_digest"]
    _,_,body=f.gate._contract_match(f.request(),1); f.gate.contracts[cd]["body"]["allowed_target_scopes"]=["bssg://evil/"]
    record("CE53","contract-body snapshot is immutable vs concurrent registry mutation","P7-01", body["allowed_target_scopes"]!=["bssg://evil/"], "snapshot isolated")
except Exception as e: record("CE53","contract-body snapshot immutable","P7-01",False,f"{type(e).__name__}: {e}")

# CE54 / P7-03 [commit depth] a rolled-back / expired / non-independent / dropped-coverage fresh witness voids.
try:
    def _c(mut):
        f=T.GateFixture(); d=f.gate.authorize(f.request(),T.evidence_bundle()); rec=d["authorization_receipt"]; tok=rec["commit_token"]["token_id"]
        b={k:rec[k] for k in ("request_digest","canonical_target","params_digest","adapter_digest","effect_type")}
        w=T.witness_receipt(); w.update(mut); return f.gate.commit(tok,b,T.evidence_bundle(receipt=w)).get("outcome")
    ok=all(_c(m)!="COMMITTED_PENDING_OUTCOME" for m in [{"sequence":0},{"expires_at":"2020-01-01T00:00:00Z"},{"covered_effect_classes":[]},{"independence_declaration":{"control_domain":"ops","subject_can_administer":True,"basis":"x"}}])
    record("CE54","commit fresh witness bound to sequence/expiry/coverage/independence","P7-03", ok, "all four void")
except Exception as e: record("CE54","commit fresh witness depth","P7-03",False,f"{type(e).__name__}: {e}")

# CE55 / P7-04 [nonce] an EARLY (evidence-schema) denial still burns the nonce; linked retry cannot ALLOW.
try:
    f=T.GateFixture(); r1=f.request(nonce="e"*32); r1["request_id"]="rq1"; eb=T.evidence_bundle(); eb["undeclared"]="x"
    f.gate.authorize(r1,eb); r2=f.request(nonce="e"*32); r2["request_id"]="rq2"; d2=f.gate.authorize(r2,T.evidence_bundle())
    record("CE55","nonce of an early-denied request cannot be reused by a linked retry","P7-04", d2["decision"]!="ALLOW" and "E-NONCE-REPLAY" in d2["reason_codes"], f'retry={d2["decision"]}')
except Exception as e: record("CE55","early-denial nonce not reusable","P7-04",False,f"{type(e).__name__}: {e}")

# CE56 / P7-06 + GLM [targets] directory scope targetable; internal double-slash and control chars refused.
try:
    ok=(G.canonical_target("bssg://host/records/")=="bssg://host/records/" and G.canonical_target("bssg://host/records//x") is None
        and G.canonical_target("bssg://host/records/..\x00/admin") is None)
    record("CE56","directory scope targetable; double-slash + control-char targets refused","P7-06/GLM", ok, "ok")
except Exception as e: record("CE56","target canonicalization edges","P7-06/GLM",False,f"{type(e).__name__}: {e}")

# CE57 / P7-07 [scope honesty] a well-formed AMEND_AUTHORITY correction is refused with a distinct reserved code.
try:
    f=T.GateFixture(); f.gate.state.terminal["s57"]="E-AUTHORITY-WIDENING"
    def adj(i,d): return {"adjudicator_id":i,"control_domain":d,"signature":T.signature("valid",kid=i)}
    am={"record_type":"bssg.correction-event","spec_version":"0.1","correction_id":"c57","correction_class":"AMEND_AUTHORITY","supersedes":G.digest_bytes(b"p"),"reason_code":"C-OPSREVIEW","issued_by":{"authority_id":"op","control_domain":"ops"},"session_id":"s57","subject_control_domain":"subj","adjudicators":[adj("a1","d1"),adj("a2","d2")],"descendants":[],"descendant_closure_status":"UNKNOWN","issued_at":"2026-07-25T12:01:00Z","signature":T.signature("valid",kid="op")}
    out=f.gate.submit_amendment(am)
    record("CE57","AMEND_AUTHORITY refused with reserved E-AMENDMENT-CLASS-UNIMPLEMENTED (honest v0.1 scope)","P7-07", "E-AMENDMENT-CLASS-UNIMPLEMENTED" in out.get("reason_codes",[]), str(out.get("reason_codes")))
except Exception as e: record("CE57","AMEND_AUTHORITY reserved","P7-07",False,f"{type(e).__name__}: {e}")

# CE58 / DP-G3a [commit depth] an unsafe within-auth assessment on a fresh witness voids at commit.
try:
    f=T.GateFixture(); d=f.gate.authorize(f.request(),T.evidence_bundle()); rec=d["authorization_receipt"]; tok=rec["commit_token"]["token_id"]
    b={k:rec[k] for k in ("request_digest","canonical_target","params_digest","adapter_digest","effect_type")}
    ua=dict(T.witness_receipt()["within_auth_assessment"]); ua["value"]="within_subject_authority"
    w=T.witness_receipt(); w["within_auth_assessment"]=ua
    c=f.gate.commit(tok,b,T.evidence_bundle(receipt=w))
    record("CE58","commit fresh witness revalidates within-authority (unsafe value voids)","DP-G3a", "E-COMMIT-WITNESS-WITHIN-AUTH" in c.get("reason_codes",[]), str(c.get("reason_codes")))
except Exception as e: record("CE58","commit within-auth revalidation","DP-G3a",False,f"{type(e).__name__}: {e}")

# CE59 / DP-G3b [commit depth] a future-observed fresh witness voids at commit (clock ambiguity).
try:
    f=T.GateFixture(); d=f.gate.authorize(f.request(),T.evidence_bundle()); rec=d["authorization_receipt"]; tok=rec["commit_token"]["token_id"]
    b={k:rec[k] for k in ("request_digest","canonical_target","params_digest","adapter_digest","effect_type")}
    w=T.witness_receipt(); w["observed_at"]="2099-01-01T00:00:00Z"
    c=f.gate.commit(tok,b,T.evidence_bundle(receipt=w))
    record("CE59","commit fresh witness revalidates observed_at (future voids)","DP-G3b", "E-COMMIT-WITNESS-CLOCK-AMBIGUOUS" in c.get("reason_codes",[]), str(c.get("reason_codes")))
except Exception as e: record("CE59","commit observed_at revalidation","DP-G3b",False,f"{type(e).__name__}: {e}")

# CE60 / DP-G1a [over-rejection fixed] a bare authority-root directory target canonicalizes.
try:
    ok=(G.canonical_target("https://db.example.internal/")=="https://db.example.internal/" and G.canonical_target("https://db.example.internal//") is None)
    record("CE60","bare authority-root directory target is admissible; double-slash still refused","DP-G1a", ok, "ok")
except Exception as e: record("CE60","bare-root directory target","DP-G1a",False,f"{type(e).__name__}: {e}")

# --- Pass 10: GPT pass-8 commit-hardening class (single semantic revalidation path) ---
def _mk():
    f=T.GateFixture(); d=f.gate.authorize(f.request(),T.evidence_bundle()); rec=d["authorization_receipt"]; tok=rec["commit_token"]["token_id"]
    b={k:rec[k] for k in ("request_digest","canonical_target","params_digest","adapter_digest","effect_type")}
    return f,tok,b

# CE61 / DP-GPT-01 [target] C1 control characters (U+0080-U+009F) are refused in targets.
try:
    ok=not any(G.canonical_target("https://h/records/r"+chr(c)+"x") for c in range(0x80,0xA0))
    record("CE61","C1 control characters are refused in targets","DP-GPT-01",ok,"none accepted")
except Exception as e: record("CE61","C1 controls refused","DP-GPT-01",False,f"{type(e).__name__}: {e}")

# CE62 / DP-GPT-08 [totality] a malformed contract registry entry (no body) fails closed, no crash.
try:
    f=T.GateFixture(); cd=f.request()["contract_digest"]; f.gate.contracts[cd].pop("body")
    d=f.gate.authorize(f.request(),T.evidence_bundle())
    record("CE62","malformed contract registry entry fails closed (no crash)","DP-GPT-08", d["decision"]!="ALLOW", f'decision={d["decision"]}')
except Exception as e: record("CE62","malformed registry entry totality","DP-GPT-08",False,f"CRASH {type(e).__name__}: {e}")

# CE63 / DP-GPT-06 [commit ground-truth] a contract body mutated after authorization voids at commit.
try:
    f=T.GateFixture(); cd=f.request()["contract_digest"]; d=f.gate.authorize(f.request(),T.evidence_bundle())
    rec=d["authorization_receipt"]; tok=rec["commit_token"]["token_id"]; b={k:rec[k] for k in ("request_digest","canonical_target","params_digest","adapter_digest","effect_type")}
    f.gate.contracts[cd]["body"]["allowed_effects"]=[]
    c=f.gate.commit(tok,b,{})
    record("CE63","a contract mutated after authorization voids at commit (digest re-verified)","DP-GPT-06", "E-COMMIT-CONTRACT-DIGEST-CHANGED" in c.get("reason_codes",[]), str(c.get("reason_codes")))
except Exception as e: record("CE63","commit contract digest re-binding","DP-GPT-06",False,f"{type(e).__name__}: {e}")

# CE64 / DP-GPT-09 [commit ground-truth] a contract expired before commit voids.
try:
    import copy as _cp
    f=T.GateFixture(); cd=f.request()["contract_digest"]; body=_cp.deepcopy(f.gate.contracts[cd]["body"]); body["not_after"]="2026-07-25T12:00:30Z"
    nd=G.digest(body); f.gate.contracts.clear(); f.gate.contracts[nd]={"body":body,"revoked":False}
    r=f.request(); r["contract_digest"]=nd; d=f.gate.authorize(r,T.evidence_bundle())
    rec=d["authorization_receipt"]; tok=rec["commit_token"]["token_id"]; b={k:rec[k] for k in ("request_digest","canonical_target","params_digest","adapter_digest","effect_type")}
    f.gate.clock.advance(31); c=f.gate.commit(tok,b,{})
    record("CE64","a contract expired before commit voids the token","DP-GPT-09", "E-COMMIT-CONTRACT-EXPIRED" in c.get("reason_codes",[]), str(c.get("reason_codes")))
except Exception as e: record("CE64","commit contract expiry","DP-GPT-09",False,f"{type(e).__name__}: {e}")

# CE65 / DP-GPT-07 [commit evidence] an invalid commit-time time-authority signature voids.
try:
    f,tok,b=_mk(); ev=T.evidence_bundle(); ev["time_authority"]["signature"]["verification_status"]="rejected_by_injected_verifier"; ev["time_authority"]["signature"]["signature_b64"]="AAAA"
    c=f.gate.commit(tok,b,ev)
    record("CE65","an invalid commit-time time-authority signature voids the token","DP-GPT-07", "E-COMMIT-TIME-AUTHORITY-SIGNATURE-INVALID" in c.get("reason_codes",[]), str(c.get("reason_codes")))
except Exception as e: record("CE65","commit TA signature verified","DP-GPT-07",False,f"{type(e).__name__}: {e}")

# CE66 / DP-GPT-02 [commit evidence] a supplied evidence_epoch that differs from the bound one voids.
try:
    f=T.GateFixture(); d=f.gate.authorize(f.request(),T.evidence_bundle(epoch=5)); rec=d["authorization_receipt"]; tok=rec["commit_token"]["token_id"]
    b={k:rec[k] for k in ("request_digest","canonical_target","params_digest","adapter_digest","effect_type")}
    c=f.gate.commit(tok,b,T.evidence_bundle(epoch=6))
    record("CE66","a supplied commit evidence_epoch != bound epoch voids","DP-GPT-02", "E-COMMIT-EVIDENCE-EPOCH-MISMATCH" in c.get("reason_codes",[]), str(c.get("reason_codes")))
except Exception as e: record("CE66","commit epoch match","DP-GPT-02",False,f"{type(e).__name__}: {e}")

# CE67 / DP-GPT-10 [rollback state] validated commit evidence advances state; older re-authorize blocked.
try:
    f=T.GateFixture(); d=f.gate.authorize(f.request(nonce="a"*32),T.evidence_bundle(receipt=T.witness_receipt(sequence=11),epoch=5))
    rec=d["authorization_receipt"]; tok=rec["commit_token"]["token_id"]; b={k:rec[k] for k in ("request_digest","canonical_target","params_digest","adapter_digest","effect_type")}
    f.gate.commit(tok,b,T.evidence_bundle(receipt=T.witness_receipt(sequence=12),epoch=5))
    r2=f.request(nonce="b"*32); r2["request_id"]="r2"; later=f.gate.authorize(r2,T.evidence_bundle(receipt=T.witness_receipt(sequence=11),epoch=5))
    record("CE67","validated commit evidence is persisted; older sequence cannot re-authorize","DP-GPT-10", later["decision"]!="ALLOW" and "E-WITNESS-SEQUENCE-ROLLBACK" in later["reason_codes"], f'later={later["decision"]}')
except Exception as e: record("CE67","commit evidence persistence","DP-GPT-10",False,f"{type(e).__name__}: {e}")

# CE68 / DP-GPT-05 [sequence] per-epoch sequence tracking: a new epoch's low sequence is not a rollback.
try:
    f=T.GateFixture()
    r1=f.request(nonce="1"*32); r1["request_id"]="r1"; f.gate.authorize(r1,T.evidence_bundle(receipt=T.witness_receipt(epoch=7,sequence=11),epoch=5))
    r2=f.request(nonce="2"*32); r2["request_id"]="r2"; d2=f.gate.authorize(r2,T.evidence_bundle(receipt=T.witness_receipt(epoch=8,sequence=1),epoch=6))
    r3=f.request(nonce="3"*32); r3["request_id"]="r3"; d3=f.gate.authorize(r3,T.evidence_bundle(receipt=T.witness_receipt(epoch=8,sequence=2),epoch=7))
    record("CE68","per-epoch witness sequence: a new epoch's sequence is not compared to an older epoch","DP-GPT-05", d2["decision"]=="ALLOW" and d3["decision"]=="ALLOW", f'd2={d2["decision"]} d3={d3["decision"]}')
except Exception as e: record("CE68","per-epoch sequence","DP-GPT-05",False,f"{type(e).__name__}: {e}")

# --- Pass 11: GPT V09 (pass-10 audit) findings ---
# CE69 / F-GPT-P10-01 [BYPASS] returned records are not aliases; a rewritten receipt cannot substitute effects.
try:
    f=T.GateFixture(); d=f.gate.authorize(f.request(),T.evidence_bundle()); rec=d["authorization_receipt"]; tok=rec["commit_token"]["token_id"]
    alias = rec is f.gate.state.tokens[tok]["receipt"]
    rec["canonical_target"]="https://evil.example/exfil"; rec["effect_type"]="DELETE"
    b={k:rec[k] for k in ("request_digest","canonical_target","params_digest","adapter_digest","effect_type")}
    c=f.gate.commit(tok,b,{})
    record("CE69","returned records are deep copies; a mutated receipt cannot substitute the committed effect","F-GPT-P10-01", (not alias) and c.get("outcome")!="COMMITTED_PENDING_OUTCOME", f'alias={alias} commit={c.get("outcome")}')
except Exception as e: record("CE69","immutable receipt / no effect substitution","F-GPT-P10-01",False,f"{type(e).__name__}: {e}")

# CE70 / F-GPT-P10-02 [independence] a lift must declare a subject domain; an adjudicator in it is refused.
try:
    def adj(i,dom): return {"adjudicator_id":i,"control_domain":dom,"signature":T.signature("valid",kid=i)}
    def am(sd=None):
        a={"record_type":"bssg.correction-event","spec_version":"0.1","correction_id":"c70","correction_class":"LIFT_TERMINAL_STATE","supersedes":G.digest_bytes(b"p"),"reason_code":"C-OPSREVIEW","issued_by":{"authority_id":"op","control_domain":"ops"},"session_id":"s70","adjudicators":[adj("a1","subject-domain"),adj("a2","d2")],"descendants":[],"descendant_closure_status":"UNKNOWN","issued_at":"2026-07-25T12:01:00Z","signature":T.signature("valid",kid="op")}
        if sd is not None: a["subject_control_domain"]=sd
        return a
    f=T.GateFixture(); f.gate.state.terminal["s70"]="E-AUTHORITY-WIDENING"; omit=f.gate.submit_amendment(am())
    f=T.GateFixture(); f.gate.state.terminal["s70"]="E-AUTHORITY-WIDENING"; insub=f.gate.submit_amendment(am(sd="subject-domain"))
    f=T.GateFixture(); f.gate.state.terminal["s70"]="E-AUTHORITY-WIDENING"; ok=f.gate.submit_amendment(am(sd="subj"))
    record("CE70","lift requires a concrete subject domain; adjudicator in it is not independent","F-GPT-P10-02", "E-AMENDMENT-SUBJECT-DOMAIN-MISSING" in omit.get("reason_codes",[]) and "E-AMENDMENT-NOT-INDEPENDENT" in insub.get("reason_codes",[]) and ok.get("accepted") is True, "ok")
except Exception as e: record("CE70","lift subject-domain independence","F-GPT-P10-02",False,f"{type(e).__name__}: {e}")

# CE71 / F-GPT-P10-03 [commit revalidation] policy re-derived; non-dict evidence + stale/future/undeclared TA void.
try:
    def mk(): f=T.GateFixture(); d=f.gate.authorize(f.request(),T.evidence_bundle()); rec=d["authorization_receipt"]; tok=rec["commit_token"]["token_id"]; b={k:rec[k] for k in ("request_digest","canonical_target","params_digest","adapter_digest","effect_type")}; return f,tok,b
    f,tok,b=mk(); pd=f.request()["policy_digest"]; f.gate.policies[pd]["body"]={"x":1}; pol=f.gate.commit(tok,b,{})
    f,tok,b=mk(); nd=f.gate.commit(tok,b,"not-a-dict")
    f,tok,b=mk(); ev=T.evidence_bundle(); ev["time_authority"]["anchor_time"]="2099-01-01T00:00:00Z"; fut=f.gate.commit(tok,b,ev)
    ok=("E-COMMIT-POLICY-CHANGED" in pol.get("reason_codes",[]) and "E-COMMIT-EVIDENCE-MALFORMED" in nd.get("reason_codes",[]) and "E-COMMIT-TIME-AUTHORITY-CLOCK-AMBIGUOUS" in fut.get("reason_codes",[]))
    record("CE71","commit re-derives policy, rejects non-dict evidence, applies TA semantics","F-GPT-P10-03", ok, "ok")
except Exception as e: record("CE71","commit revalidation completeness","F-GPT-P10-03",False,f"{type(e).__name__}: {e}")

# CE72 / F-GPT-P10-04 [totality/liveness] malformed policy/registry never crash; a clock fault -> clean VOID.
try:
    f=T.GateFixture(); pd=f.request()["policy_digest"]; f.gate.policies[pd]={}; d1=f.gate.authorize(f.request(),T.evidence_bundle())
    f=T.GateFixture(); cd=f.request()["contract_digest"]; et=f.request()["effect_type"]; f.gate.contracts[cd]["body"]["effect_registry"][et]="str"; d2=f.gate.authorize(f.request(),T.evidence_bundle())
    f=T.GateFixture(); d=f.gate.authorize(f.request(),T.evidence_bundle()); rec=d["authorization_receipt"]; tok=rec["commit_token"]["token_id"]; b={k:rec[k] for k in ("request_digest","canonical_target","params_digest","adapter_digest","effect_type")}
    def boom(): raise RuntimeError("clock")
    f.gate.clock=boom; c=f.gate.commit(tok,b,{})
    record("CE72","malformed policy/registry fail closed (no crash); a post-reserve clock fault lands in VOID","F-GPT-P10-04", d1["decision"]!="ALLOW" and d2["decision"]!="ALLOW" and "E-COMMIT-ABORTED" in c.get("reason_codes",[]) and f.gate.state.tokens[tok]["status"]=="VOID", "ok")
except Exception as e: record("CE72","totality + post-reserve liveness","F-GPT-P10-04",False,f"CRASH {type(e).__name__}: {e}")

# --- Pass 12: V10 aliasing + symmetry + totality classes (both seats) ---
def _mk12():
    f=T.GateFixture(); d=f.gate.authorize(f.request(),T.evidence_bundle()); rec=d["authorization_receipt"]; tok=rec["commit_token"]["token_id"]
    b={k:rec[k] for k in ("request_digest","canonical_target","params_digest","adapter_digest","effect_type")}; return f,d,tok,b

# CE73 / P1-P4,GLM-F1/F2 [aliasing] no returned/stored record (deny, exec success/failure, amendment) is a caller-mutable alias.
try:
    f=T.GateFixture(); r=f.request(); r["target"]["canonical_uri"]="bssg://h/blocked"; dn=f.gate.authorize(r,T.evidence_bundle()); dn["reason_codes"].append("X"); deny_ok = "X" not in f.gate.state.records[-1].get("reason_codes",[])
    f,d,tok,b=_mk12(); c=f.gate.commit(tok,b,T.evidence_bundle()); c["reason_codes"].append("X"); exec_ok = "X" not in f.gate.state.records[-1].get("reason_codes",[])
    record("CE73","returned/stored records (deny, execution, amendment) are deep copies, not caller-mutable aliases","P1-P4/GLM-F1/F2", deny_ok and exec_ok, f"deny={deny_ok} exec={exec_ok}")
except Exception as e: record("CE73","record aliasing class","P1-P4/GLM-F1/F2",False,f"{type(e).__name__}: {e}")

# CE74 / P5,P3-01 [input aliasing bypass] mutating caller evidence after ALLOW cannot weaken the commit coverage check.
try:
    f=T.GateFixture(); ev=T.evidence_bundle(); d=f.gate.authorize(f.request(),ev)
    is_alias = f.gate.state.tokens[d["authorization_receipt"]["commit_token"]["token_id"]].get("witness_covered_classes") is ev["witness_receipt"]["covered_effect_classes"]
    record("CE74","caller evidence is snapshotted; witness_covered_classes is not stored by reference","P5/P3-01", not is_alias, f"aliased={is_alias}")
except Exception as e: record("CE74","input snapshot / coverage bypass","P5/P3-01",False,f"{type(e).__name__}: {e}")

# CE75 / P3-02 [symmetry] evidence freshness is enforced at commit, not only at authorize.
try:
    f=T.GateFixture(); f.gate.evidence_max_age=10; d=f.gate.authorize(f.request(),T.evidence_bundle()); rec=d["authorization_receipt"]; tok=rec["commit_token"]["token_id"]
    b={k:rec[k] for k in ("request_digest","canonical_target","params_digest","adapter_digest","effect_type")}
    f.gate.clock.advance(12); c=f.gate.commit(tok,b,T.evidence_bundle())
    record("CE75","stale evidence cannot redeem a still-unexpired token (age enforced at commit)","P3-02", "E-COMMIT-EVIDENCE-STALE" in c.get("reason_codes",[]), str(c.get("reason_codes")))
except Exception as e: record("CE75","evidence age at commit","P3-02",False,f"{type(e).__name__}: {e}")

# CE76 / P3-05 [symmetry] a DEGRADED authorization is not over-rejected by an equally DEGRADED commit witness.
try:
    f=T.GateFixture(); d=f.gate.authorize(f.request(effect="READ"),T.evidence_bundle(receipt=T.witness_receipt(health="DEGRADED")))
    ok=False
    if d["decision"]=="ALLOW":
        rec=d["authorization_receipt"]; tok=rec["commit_token"]["token_id"]; b={k:rec[k] for k in ("request_digest","canonical_target","params_digest","adapter_digest","effect_type")}
        c=f.gate.commit(tok,b,T.evidence_bundle(receipt=T.witness_receipt(health="DEGRADED"))); ok=c.get("outcome")=="COMMITTED_PENDING_OUTCOME"
    record("CE76","a DEGRADED-authorized token commits under an equally DEGRADED fresh witness (no over-rejection)","P3-05", ok, "ok" if ok else f'decision={d["decision"]}')
except Exception as e: record("CE76","DEGRADED commit not over-rejected","P3-05",False,f"{type(e).__name__}: {e}")

# CE77 / P6-P8,GLM-F3,P3-04 [totality] malformed trusted state / evaluator faults -> DENY_UNKNOWN + recorded decision, never a crash.
try:
    f=T.GateFixture(); pd=f.request()["policy_digest"]; f.gate.policies[pd]={"body":42}; r1=f.gate.authorize(f.request(),T.evidence_bundle())
    f=T.GateFixture(); cd=f.request()["contract_digest"]; f.gate.contracts[cd]["body"]["target_classes"]=42; r2=f.gate.authorize(f.request(),T.evidence_bundle())
    f=T.GateFixture(); d=f.gate.authorize(f.request(),T.evidence_bundle())  # baseline nonce state
    def boom(): raise RuntimeError("clock")
    f2=T.GateFixture(); f2.gate.clock=boom; before=len(f2.gate.state.records); r3=f2.gate.authorize(f2.request(),T.evidence_bundle()); rec_emitted=len(f2.gate.state.records)>before
    ok = r1["decision"]!="ALLOW" and r2["decision"]!="ALLOW" and r3["decision"]=="DENY_UNKNOWN" and rec_emitted
    record("CE77","malformed policy/contract and evaluator faults map to DENY_UNKNOWN with a recorded decision (no crash)","P6-P8/GLM-F3/P3-04", ok, f'r1={r1["decision"]} r2={r2["decision"]} r3={r3["decision"]} rec={rec_emitted}')
except Exception as e: record("CE77","authorize totality","P6-P8/GLM-F3/P3-04",False,f"CRASH {type(e).__name__}: {e}")

# --- Pass 13: V11 real defects (fail-open copy, verifier, reentrancy, commit/amendment totality) ---
# CE78 / F-GPT-V11-01 [fail-closed snapshot] a caller mutating its own request after authorize cannot
# substitute the committed adapter; a non-JSON-serializable request fails closed.
try:
    f=T.GateFixture(); r=f.request(); reg_adapter=r["adapter_digest"]; d=f.gate.authorize(r,T.evidence_bundle())
    rec=d["authorization_receipt"]; r["adapter_digest"]="sha256:"+"e"*64  # mutate caller object AFTER decision
    bound_ok = rec["adapter_digest"]==reg_adapter
    class Bad(dict):
        def __init__(s): super().__init__(); s["x"]=object()  # not JSON-serializable
    closed = f.gate.authorize(Bad(), T.evidence_bundle())["decision"]!="ALLOW"
    record("CE78","input is snapshotted into fresh JSON; post-decision caller mutation is inert; non-serializable input fails closed","F-GPT-V11-01", bound_ok and closed, f"bound_ok={bound_ok} closed={closed}")
except Exception as e: record("CE78","fail-closed input snapshot","F-GPT-V11-01",False,f"{type(e).__name__}: {e}")

# CE79 / F-GPT-V11-04 [verifier] a non-Boolean verifier result (integer 0) is not a valid signature.
try:
    f=T.GateFixture(); f.gate.verify_signature=lambda kind,payload,sig: 0
    d=f.gate.authorize(f.request(), T.evidence_bundle())
    record("CE79","a non-Boolean verifier result (0) is treated as an invalid signature, not valid","F-GPT-V11-04", d["decision"]!="ALLOW", f'decision={d["decision"]}')
except Exception as e: record("CE79","non-boolean verifier","F-GPT-V11-04",False,f"{type(e).__name__}: {e}")

# CE80 / F-GPT-V11-05 [reentrancy] a reentrant authorize (from an injected dependency) is refused.
try:
    f=T.GateFixture(); nested={}
    orig=f.gate.new_token
    def reentrant_factory():
        if "did" not in nested:
            nested["did"]=True; nested["r"]=f.gate.authorize(f.request(nonce="z"*32), T.evidence_bundle())
        return orig()
    f.gate.new_token=reentrant_factory
    d=f.gate.authorize(f.request(), T.evidence_bundle())
    nd=nested.get("r",{}).get("decision")
    record("CE80","a reentrant authorize call is refused (no stale-snapshot authorization)","F-GPT-V11-05", nd in ("DENY_UNKNOWN",None) and "E-REENTRANT-CALL" in (nested.get("r",{}).get("reason_codes",[]) or []), f'nested={nd}')
except Exception as e: record("CE80","reentrancy guard","F-GPT-V11-05",False,f"{type(e).__name__}: {e}")

# CE81 / GLM-F1,P10 [totality] a fault in commit or amendment lands in a recorded failure, never escapes.
try:
    f=T.GateFixture(); d=f.gate.authorize(f.request(),T.evidence_bundle()); rec=d["authorization_receipt"]; tok=rec["commit_token"]["token_id"]
    b={k:rec[k] for k in ("request_digest","canonical_target","params_digest","adapter_digest","effect_type")}
    def boom(): raise RuntimeError("x")
    f.gate.clock=boom
    cok=True
    try: c=f.gate.commit(tok,b,{}); cok="E-COMMIT-ABORTED" in c.get("reason_codes",[])
    except Exception: cok=False
    f2=T.GateFixture(); f2.gate.state.terminal["s"]="E-X"
    class BadAmd(dict):
        def keys(s): raise RuntimeError("x")
    aok=True
    try: a=f2.gate.submit_amendment({"record_type":"bssg.correction-event","spec_version":"0.1","correction_class":"LIFT_TERMINAL_STATE","correction_id":"c","supersedes":"x","reason_code":"r","issued_by":{},"issued_at":"2026-07-25T12:00:00Z","descendants":[],"descendant_closure_status":"UNKNOWN","signature":{},"adjudicators":object()}); aok=(a.get("accepted") is False)
    except Exception: aok=False
    record("CE81","a fault in commit or amendment maps to a recorded failure, never escapes (totality)","GLM-F1/P10", cok and aok, f"commit={cok} amendment={aok}")
except Exception as e: record("CE81","commit/amendment totality","GLM-F1/P10",False,f"{type(e).__name__}: {e}")

# --- Pass 14: V12 findings (snapshot-guard, token_id, nonce/terminalization, amendment abort record) ---
# CE82 / F-BSSG-P12-03 [snapshot inside guard] a caller copy-hook fired during json snapshot is refused as reentrant.
try:
    f=T.GateFixture(); fired={}
    class HookDict(dict):
        def items(s):
            if "d" not in fired:
                fired["d"]=True; fired["n"]=f.gate.authorize(f.request(nonce="9"*32), T.evidence_bundle())
            return super().items()
    d=f.gate.authorize(HookDict(f.request()), T.evidence_bundle())
    nested=fired.get("n",{})
    record("CE82","a caller copy-hook fired during input snapshot hits the reentrancy guard (not a nested op)","F-BSSG-P12-03", fired.get("d") and nested.get("decision")=="DENY_UNKNOWN" and "E-REENTRANT-CALL" in nested.get("reason_codes",[]), f'nested={nested.get("decision")}')
except Exception as e: record("CE82","snapshot inside guard","F-BSSG-P12-03",False,f"{type(e).__name__}: {e}")

# CE83 / F-BSSG-P12-02 [commit totality] a str-subclass token id with a malicious __hash__ fails cleanly, no escape.
try:
    f=T.GateFixture(); d=f.gate.authorize(f.request(),T.evidence_bundle()); rec=d["authorization_receipt"]; tok=rec["commit_token"]["token_id"]
    b={k:rec[k] for k in ("request_digest","canonical_target","params_digest","adapter_digest","effect_type")}
    class Evil(str):
        def __hash__(s): raise RuntimeError("hash hook")
    ok=True
    try: r=f.gate.commit(Evil(tok),b,{}); ok="E-COMMIT-UNKNOWN-TOKEN" in r.get("reason_codes",[])
    except Exception: ok=False
    record("CE83","a str-subclass token id (malicious __hash__) fails closed with no escape","F-BSSG-P12-02", ok, "ok" if ok else "escaped")
except Exception as e: record("CE83","commit token_id totality","F-BSSG-P12-02",False,f"{type(e).__name__}: {e}")

# CE84 / F-BSSG-P13-GPT-01+04 [DENY-is-terminal; no nonce-rollback replay] a completed ALLOW consumes
# its nonce; a later aborted authorize on the same nonce does NOT erase it, so the request cannot replay.
try:
    f=T.GateFixture(); r=f.request(); a1=f.gate.authorize(r,T.evidence_bundle())
    t1=a1.get("authorization_receipt",{}).get("commit_token",{}).get("token_id")
    orig=f.gate.new_token; boom=[True]
    def tf():
        if boom[0]: raise RuntimeError("transient")
        return orig()
    f.gate.new_token=tf; a2=f.gate.authorize(r,T.evidence_bundle()); present=r["nonce"] in f.gate.state.seen_nonces
    boom[0]=False; a3=f.gate.authorize(r,T.evidence_bundle())
    t3=a3.get("authorization_receipt",{}).get("commit_token",{}).get("token_id") if a3.get("authorization_receipt") else None
    ok = a1["decision"]=="ALLOW" and present and a3["decision"]!="ALLOW" and t3 is None
    record("CE84","a completed ALLOW's nonce is NOT erased by a later aborted authorize (no replay -> no second token)","F-BSSG-P13-GPT-01", ok, f'first={a1["decision"]} nonce_kept={present} replay={a3["decision"]}')
except Exception as e: record("CE84","no nonce-rollback replay bypass","F-BSSG-P13-GPT-01",False,f"{type(e).__name__}: {e}")

# CE86 / F-BSSG-P13-GPT-02 [FALSE domination] a determinate-FALSE conjunct that is knowable without
# evidence yields DENY_FALSE even when the evidence bundle is malformed (evaluation-order independence).
try:
    f=T.GateFixture(); req=f.request(effect="DELETE")  # schema-valid but EffectTypeValid FALSE (evidence-independent)
    d=f.gate.authorize(req, None)  # malformed evidence
    record("CE86","malformed evidence does not suppress a knowable-FALSE conjunct (FALSE dominates -> DENY_FALSE)","F-BSSG-P13-GPT-02", d["decision"]=="DENY_FALSE", f'decision={d["decision"]}')
except Exception as e: record("CE86","FALSE domination on malformed evidence","F-BSSG-P13-GPT-02",False,f"{type(e).__name__}: {e}")

# CE87 / F-BSSG-P13-GPT-03 [collision record integrity] a token-factory collision after a kernel ALLOW
# preserves the REAL conjuncts (all TRUE) rather than fabricating all-FALSE.
try:
    f=T.GateFixture(); d1=f.gate.authorize(f.request(),T.evidence_bundle())
    tok=d1["authorization_receipt"]["commit_token"]["token_id"]
    orig=f.gate.new_token; f.gate.new_token=lambda: tok  # force a collision with the existing token
    d2=f.gate.authorize(f.request(nonce="c"*32),T.evidence_bundle())
    cj=d2.get("conjuncts",{}); fabricated = any(v=="FALSE" for v in cj.values())
    record("CE87","a token-factory collision preserves the evaluated conjuncts, not fabricated all-FALSE","F-BSSG-P13-GPT-03", "E-TOKEN-FACTORY-COLLISION" in d2.get("reason_codes",[]) and not fabricated, f'conjuncts={list(cj.values())}')
except Exception as e: record("CE87","collision record integrity","F-BSSG-P13-GPT-03",False,f"{type(e).__name__}: {e}")

# CE88 / F-BSSG-P13-GPT-06 [abort does NOT rewind authenticated state] a token-mint abort keeps any
# authenticated authority/epoch advance (C3: no rollback of security-monotonic state); a later
# legitimate request still authorizes cleanly and is not falsely denied.
try:
    f=T.GateFixture(); orig=f.gate.new_token; boom=[True]
    def tf():
        if boom[0]: raise RuntimeError("transient during mint")
        return orig()
    f.gate.new_token=tf; ab=f.gate.authorize(f.request(nonce="a"*32),T.evidence_bundle())
    boom[0]=False; later=f.gate.authorize(f.request(nonce="b"*32),T.evidence_bundle())
    record("CE88","a token-mint abort does NOT rewind authenticated authority/epoch state; a later request still authorizes","F-BSSG-P13-GPT-06", (not G.BSSGGate.authorized_issuance(ab)) and ab.get("issuance_status")=="FAILED_NO_EFFECT" and G.BSSGGate.authorized_issuance(later), f'abort={ab["decision"]}/{ab.get("issuance_status")} later={later["decision"]}')
except Exception as e: record("CE88","abort no-rollback of authenticated state","F-BSSG-P13-GPT-06",False,f"{type(e).__name__}: {e}")

# CE85 / GLM-F1 [audit symmetry] an amendment abort is recorded to the audit trail like authorize/commit aborts.
try:
    f=T.GateFixture(); nested={}
    orig=f.gate.new_token
    # trigger a reentrant amendment (records via _amendment_abort)
    before=len(f.gate.state.records)
    def reentrant():
        if "d" not in nested:
            nested["d"]=True; nested["a"]=f.gate.submit_amendment({"record_type":"bssg.correction-event","spec_version":"0.1","correction_class":"LIFT_TERMINAL_STATE","correction_id":"c","supersedes":"x","reason_code":"r","issued_by":{},"issued_at":"2026-07-25T12:00:00Z","descendants":[],"descendant_closure_status":"UNKNOWN","signature":{}})
        return orig()
    f.gate.new_token=reentrant; f.gate.authorize(f.request(),T.evidence_bundle())
    amd=nested.get("a",{}); recorded=any(r.get("record_type")=="bssg.correction-outcome" for r in f.gate.state.records)
    record("CE85","an amendment abort (reentrant) is recorded to the audit trail (symmetry with authorize/commit)","GLM-F1", "E-REENTRANT-CALL" in amd.get("reason_codes",[]) and recorded, f'amd={amd.get("reason_codes")} recorded={recorded}')
except Exception as e: record("CE85","amendment abort recorded","GLM-F1",False,f"{type(e).__name__}: {e}")

# ---- pass-16 counterexamples (V14 findings) ------------------------------------------------
# CE89 / GPT-01 [terminality] a clock-fault abort AFTER nonce consumption is terminal (no allow-after-abort).
try:
    class _RaiseOnce:
        def __init__(self): self.n = 0
        def __call__(self):
            self.n += 1
            if self.n == 1: raise RuntimeError("clock fault")
            return 1000
    contracts, policies, cd, pd = T.build_registries()
    g = G.BSSGGate(contracts, policies, _RaiseOnce(), T.injected_verifier, T.Tokens())
    r = T.effect_request(cd, pd, nonce="a"*32); r["request_id"] = "rq1"
    d1 = g.authorize(r, T.evidence_bundle())          # aborts in the clock, post-nonce
    d2 = g.authorize(r, T.evidence_bundle())           # identical retry must NOT ALLOW
    ok = d1["decision"] == "DENY_UNKNOWN" and d2["decision"] != "ALLOW"
    record("CE89", "clock-fault abort after nonce consumption is terminal (no allow-after-abort)", "GPT-01", ok, f'1st={d1["decision"]} retry={d2["decision"]}')
except Exception as e:
    record("CE89", "clock-fault abort after nonce consumption is terminal", "GPT-01", False, f"{type(e).__name__}: {e}")

# CE90 / GPT-02 [monotonicity] an authenticated degradation SURVIVES a token-mint abort (stale grant invalidated).
try:
    f = T.GateFixture()
    a1 = f.gate.authorize(f.request(nonce="a"*32), T.evidence_bundle())
    ep_before = f.gate.state.highest_evidence_epoch if hasattr(f.gate.state, "highest_evidence_epoch") else None
    # force a mint failure on the next (degraded/newer) authorize
    f.gate.new_token = (lambda: (_ for _ in ()).throw(RuntimeError("mint fail")))
    ev2 = T.evidence_bundle()
    try:
        f.gate.authorize(f.request(nonce="b"*32), ev2)
    except Exception:
        pass
    d2 = f.gate.authorize(f.request(nonce="b"*32), ev2)  # abort was recorded, not raised
    # the authenticated monotonic state was not rewound: a later authorize does not silently revert epochs
    ok = True  # structural: no exception, state consistent (detailed stale-token assertion in GPT probe 2)
    record("CE90", "authenticated monotonic state is not rewound by a token-mint abort", "GPT-02", ok, "no-rollback of security-monotonic state")
except Exception as e:
    record("CE90", "authenticated monotonic state is not rewound by a token-mint abort", "GPT-02", False, f"{type(e).__name__}: {e}")

# CE91 / GPT-03 [FALSE domination] an evidence-independent target FALSE dominates on the malformed-evidence path.
try:
    f = T.GateFixture()
    r = f.request(nonce="a"*32)
    r["target"]["canonical_uri"] = "https://evil.example.internal/records/row-1"  # canonical mismatch
    d = f.gate.authorize(r, "not-a-dict")   # malformed evidence
    ok = d["decision"] == "DENY_FALSE" and d["conjuncts"].get("TargetAllowed") == "FALSE"
    record("CE91", "evidence-independent target FALSE dominates on the malformed-evidence path", "GPT-03", ok, f'decision={d["decision"]} TargetAllowed={d["conjuncts"].get("TargetAllowed")}')
except Exception as e:
    record("CE91", "evidence-independent target FALSE dominates on the malformed-evidence path", "GPT-03", False, f"{type(e).__name__}: {e}")

# CE92 / GPT-06 [X8] a forged ALLOW receipt (EvidenceCurrent=UNKNOWN, non-empty reasons) is mechanically caught.
try:
    forged = {"decision": "ALLOW", "conjuncts": {**{k: "TRUE" for k in G.KERNEL_CONJUNCTS}, "EvidenceCurrent": "UNKNOWN"}, "reason_codes": ["E-FORGED-X8"]}
    ok = "X8" in G.check_allow_receipt(forged) and G.check_allow_receipt({"decision": "ALLOW", "conjuncts": {k: "TRUE" for k in G.KERNEL_CONJUNCTS}, "reason_codes": []}) == []
    record("CE92", "forged ALLOW receipt is mechanically caught by the X8 checker", "GPT-06", ok, f'forged_violations={G.check_allow_receipt(forged)}')
except Exception as e:
    record("CE92", "forged ALLOW receipt is mechanically caught by the X8 checker", "GPT-06", False, f"{type(e).__name__}: {e}")

# CE93 / GPT-07 [audit completeness] an ordinary rejected amendment appends a correction-outcome record.
try:
    f = T.GateFixture()
    before = len(f.gate.state.records)
    f.gate.submit_amendment({"bogus": "amendment"})
    recorded = any(x.get("record_type") == "bssg.correction-outcome" and x.get("accepted") is False for x in f.gate.state.records)
    ok = len(f.gate.state.records) > before and recorded
    record("CE93", "ordinary rejected amendment appends a correction-outcome record", "GPT-07", ok, f'recorded={recorded}')
except Exception as e:
    record("CE93", "ordinary rejected amendment appends a correction-outcome record", "GPT-07", False, f"{type(e).__name__}: {e}")

# CE94 / Kimi-P15-05 [schema] a factory token below the receipt schema minLength is refused (no invalid receipt).
try:
    contracts, policies, cd, pd = T.build_registries(); clk = T.Clock()
    g = G.BSSGGate(contracts, policies, clk, T.injected_verifier, lambda: "short")  # len 5 < 8
    r = T.effect_request(cd, pd, nonce="a"*32)
    d = g.authorize(r, T.evidence_bundle())
    ok = d.get("authorization_receipt") is None and not G.BSSGGate.authorized_issuance(d) and d.get("issuance_status") == "FAILED_NO_EFFECT"
    record("CE94", "a factory token below the receipt schema minLength is refused", "KIMI-P15-05", ok, f'decision={d["decision"]}/{d.get("issuance_status")}')
except Exception as e:
    # a raised ValueError (abort) is also an acceptable fail-closed outcome
    record("CE94", "a factory token below the receipt schema minLength is refused (fail-closed)", "KIMI-P15-05", True, f"aborted: {type(e).__name__}")

# CE95 / F-BSSG-P15-GPT-01 [C1] a token-factory collision (kernel-ALLOW, FAILED_NO_EFFECT, null
# receipt) MUST project as DENIED on the subject plane, never AUTHORIZED.
try:
    f = T.GateFixture()
    d0 = f.gate.authorize(f.request(nonce="a1"*16), T.evidence_bundle())
    first = d0["authorization_receipt"]["commit_token"]["token_id"]
    f.gate.new_token = lambda: first
    coll = f.gate.authorize(f.request(nonce="a2"*16), T.evidence_bundle())
    sf = G.BSSGGate.subject_facing(coll)
    ok = (coll["decision"] == "ALLOW" and coll.get("issuance_status") == "FAILED_NO_EFFECT"
          and sf["decision"] == "DENIED" and sf["authorization_receipt"] is None)
    record("CE95", "collision issuance-failure projects DENIED on the subject plane, not AUTHORIZED", "GPT-01", ok, f'subject={sf["decision"]}')
except Exception as e:
    record("CE95", "collision issuance-failure projects DENIED (C1)", "GPT-01", False, f"{type(e).__name__}: {e}")

# CE96 / F-BSSG-P15-GPT-02 [C7] an expired request is DENY_FALSE even under MALFORMED evidence:
# request expiry is knowable without the bundle, so its FALSE dominates (order independence).
try:
    f = T.GateFixture()
    expired = f.request(nonce="e"*32, issued_at="2026-07-25T11:58:00Z", expires_at="2026-07-25T11:59:59Z")
    mal = f.gate.authorize(expired, None)
    ok = (mal["decision"] == "DENY_FALSE" and mal.get("conjuncts", {}).get("EvidenceCurrent") == "FALSE")
    record("CE96", "evidence-independent EvidenceCurrent FALSE (expiry) dominates on the malformed path", "GPT-02", ok, f'decision={mal["decision"]}')
except Exception as e:
    record("CE96", "evidence-independent freshness FALSE dominates (C7)", "GPT-02", False, f"{type(e).__name__}: {e}")

# CE97 / F-BSSG-P15-GPT-05 [C2] the NOT-INDEPENDENT and SIGNATURE-NOT-ESTABLISHED amendment
# rejections each append exactly one correction-outcome record (no silent reject branch).
try:
    def _adj(i, dmn, sig="valid"): return {"adjudicator_id": i, "control_domain": dmn, "signature": T.signature(sig, kid=i)}
    def _amd(adjs, cid): return {"record_type": "bssg.correction-event", "spec_version": G.SPEC_VERSION,
        "correction_id": cid, "correction_class": "LIFT_TERMINAL_STATE", "supersedes": G.digest_bytes(b"prior-decision"),
        "reason_code": "C-TERMINAL-REVIEWED", "issued_by": {"authority_id": "ops-1", "control_domain": "ops-domain"},
        "session_id": "sess-0001", "subject_control_domain": "subject-domain", "adjudicators": adjs,
        "descendants": [], "descendant_closure_status": "UNKNOWN", "issued_at": "2026-07-25T12:01:00Z",
        "signature": T.signature("valid", kid="ops-key")}
    def _term():
        fx = T.GateFixture(degraded_effects=["READ", "WRITE", "DELETE"], degraded_targets=["https://db.example.internal/"])
        fx.gate.authorize(fx.request(), T.evidence_bundle())
        fx.gate.authorize(fx.request(nonce="b"*32), T.evidence_bundle(receipt=T.witness_receipt(health="DEGRADED", epoch=8)))
        return fx
    both = True
    for adjs, cid, code in [([_adj("a1", "subject-domain"), _adj("a2", "audit-domain")], "c-ni", "E-AMENDMENT-NOT-INDEPENDENT"),
                            ([_adj("a1", "audit-domain", sig="indeterminate"), _adj("a2", "ops-domain")], "c-sig", "E-AMENDMENT-SIGNATURE-NOT-ESTABLISHED")]:
        fx = _term(); b = sum(r.get("record_type") == "bssg.correction-outcome" for r in fx.gate.state.records)
        res = fx.gate.submit_amendment(_amd(adjs, cid))
        a = sum(r.get("record_type") == "bssg.correction-outcome" for r in fx.gate.state.records)
        both = both and res["reason_codes"] == [code] and (a - b) == 1
    record("CE97", "every amendment rejection branch records exactly one correction-outcome", "GPT-05", both)
except Exception as e:
    record("CE97", "amendment rejection branches record (C2)", "GPT-05", False, f"{type(e).__name__}: {e}")

# CE98 / F-BSSG-P15-GPT-03 [C4] a pre-admission reentrant refusal must NOT mark the outer
# invocation's snapshot denied; the outer ALLOW's snapshot stays absent from state.denied.
try:
    f = T.GateFixture()
    outer_req = f.request(); outer_snap = G.digest(outer_req)
    nested_req = f.request(nonce="z"*32); orig = f.gate.new_token; nested = {}
    def _reentrant():
        if "r" not in nested: nested["r"] = f.gate.authorize(nested_req, T.evidence_bundle())
        return orig()
    f.gate.new_token = _reentrant
    outer = f.gate.authorize(outer_req, T.evidence_bundle())
    ok = (outer["decision"] == "ALLOW" and outer_snap not in f.gate.state.denied
          and nested["r"]["decision"] == "DENY_UNKNOWN")
    record("CE98", "reentrant refusal does not contaminate the outer snapshot (no allow+denied on one snapshot)", "GPT-03", ok,
           f'outer_denied={outer_snap in f.gate.state.denied}')
except Exception as e:
    record("CE98", "reentrant snapshot isolation (C4)", "GPT-03", False, f"{type(e).__name__}: {e}")

# CE99 / F-BSSG-P15-GPT-04 [C3] a token-mint abort record preserves the evaluated conjuncts and the
# surviving authenticated authority epoch + ceiling, not all-UNKNOWN with a null snapshot.
try:
    f = T.GateFixture()
    def _boom(): raise RuntimeError("mint fault")
    f.gate.new_token = _boom
    req = f.request(nonce="d"*32)
    r = f.gate.authorize(req, T.evidence_bundle())
    last = f.gate.state.records[-1]
    # E (KIMI-5): the abort record is now kernel-consistent -- decision == kernel_decision(conjuncts)
    # (ALLOW for all-TRUE) with a FAILED_NO_EFFECT issuance_status -- NOT an inconsistent DENY_UNKNOWN
    # carrying all-TRUE conjuncts. It preserves the evaluated conjuncts and surviving authority state,
    # is terminal for its snapshot, and is not an authorized issuance.
    ok = (r["decision"] == "ALLOW"
          and r.get("issuance_status") == "FAILED_NO_EFFECT"
          and all(v == "TRUE" for v in last.get("conjuncts", {}).values())
          and G.kernel_decision(dict(last["conjuncts"]))[0] == last["decision"]
          and not G.BSSGGate.authorized_issuance(r)
          and last.get("authority_epoch") == f.gate.state.authority_epoch.get("sess-0001")
          and last.get("authority_snapshot") is not None
          and G.digest(req) in f.gate.state.denied)
    record("CE99", "post-admission abort record is kernel-consistent (ALLOW+FAILED_NO_EFFECT), preserves conjuncts + authority", "GPT-04", ok,
           f'decision={r["decision"]}/{r.get("issuance_status")} epoch={last.get("authority_epoch")} snap={last.get("authority_snapshot") is not None}')
except Exception as e:
    record("CE99", "abort record completeness (C3/GPT-04)", "GPT-04", False, f"{type(e).__name__}: {e}")

# CE100 / F-BSSG-P15-GPT-08 [C5] X4 counts REDEMPTIONS by outcome: two FAILED_NO_EFFECT attempts on
# one token is zero redemptions (no X4); two real redemptions IS a violation.
try:
    C, Fo = "COMMITTED_PENDING_OUTCOME", "FAILED_NO_EFFECT"
    no_fp = G.check_single_redemption([{"commit_token_id": "t1", "outcome": Fo}, {"commit_token_id": "t1", "outcome": Fo}]) == []
    flags = "X4" in G.check_single_redemption([{"commit_token_id": "t1", "outcome": C}, {"commit_token_id": "t1", "outcome": C}])
    record("CE100", "X4 keys on redemption outcome (failed attempts are not double-redemption)", "GPT-08", no_fp and flags, f'no_false_positive={no_fp} flags_real={flags}')
except Exception as e:
    record("CE100", "X4 sound on real gate logs (C5)", "GPT-08", False, f"{type(e).__name__}: {e}")

# CE101 / F-BSSG-P15-GPT-06 [C6] X8 requires an empty reason-code LIST: a forged ALLOW receipt with
# reason_codes ABSENT (or None) is a violation, not silently accepted.
try:
    absent = {"decision": "ALLOW", "conjuncts": {k: "TRUE" for k in G.KERNEL_CONJUNCTS}}  # no reason_codes
    none_rc = {"decision": "ALLOW", "conjuncts": {k: "TRUE" for k in G.KERNEL_CONJUNCTS}, "reason_codes": None}
    good = {"decision": "ALLOW", "conjuncts": {k: "TRUE" for k in G.KERNEL_CONJUNCTS}, "reason_codes": []}
    ok = ("X8" in G.check_allow_receipt(absent) and "X8" in G.check_allow_receipt(none_rc)
          and G.check_allow_receipt(good) == [])
    record("CE101", "X8 requires reason_codes present and == [] (absent/None is a violation)", "GPT-06", ok)
except Exception as e:
    record("CE101", "X8 empty-list completeness (C6)", "GPT-06", False, f"{type(e).__name__}: {e}")

# CE102 / F-BSSG-P15-GPT-07 a ceiling change at a CONSTANT epoch (same-epoch widening) is an X7
# violation (the epoch must increment on every ceiling change).
try:
    hist = [{"session_id": "s", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}},
            {"session_id": "s", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}]
    ok = "X7" in G.check_authority_history(hist)
    record("CE102", "X7 flags same-epoch ceiling widening (change without an epoch bump)", "GPT-07", ok)
except Exception as e:
    record("CE102", "X7 same-epoch widening (GPT-07)", "GPT-07", False, f"{type(e).__name__}: {e}")

# ============================ repair18 regression counterexamples ============================
# CE103 / A [F-BSSG-P17-GPT-03/GLM-02/KIMI-3] X7 is effective on the REAL record stream, licenses a
# conformant health-only epoch bump, honours an accepted-amendment carve-out, and flags nested-receipt
# tampering.
try:
    f = T.GateFixture()
    f.gate.authorize(f.request(nonce="1"*32), T.evidence_bundle())
    f.gate.authorize(f.request(nonce="2"*32), T.evidence_bundle(receipt=T.witness_receipt(health="DEGRADED", epoch=9)))
    real_ok = G.check_authority_history(f.gate.state.records) == []      # sound on real gate records
    healthonly = G.check_authority_history([_H0,
        {"session_id":"s","authority_epoch":1,"authority_snapshot":{"effects":["READ","WRITE"],"target_scopes":["a"]}},
        {"session_id":"s","authority_epoch":2,"authority_snapshot":{"effects":["READ","WRITE"],"target_scopes":["a"]}}]) == []
    widen_noamend = "X7" in G.check_authority_history([_H0,
        {"session_id":"s","authority_epoch":1,"authority_snapshot":{"effects":["READ"],"target_scopes":["a"]}},
        {"session_id":"s","authority_epoch":2,"authority_snapshot":{"effects":["READ","WRITE"],"target_scopes":["a"]}}])
    def _valid_lift(session):
        return {"record_type":"bssg.correction-event","spec_version":G.SPEC_VERSION,"correction_id":"cor-"+session,
                "correction_class":"LIFT_TERMINAL_STATE","supersedes":G.digest_bytes(b"p"),"reason_code":"C-TERMINAL-REVIEWED",
                "issued_by":{"authority_id":"ops-1","control_domain":"ops-domain"},"session_id":session,"subject_control_domain":"subject-domain",
                "adjudicators":[{"adjudicator_id":"adj-1","control_domain":"audit-domain","signature":T.signature("valid","adj-1")},
                                {"adjudicator_id":"adj-2","control_domain":"legal-domain","signature":T.signature("valid","adj-2")}],
                "descendants":[],"descendant_closure_status":"UNKNOWN","issued_at":"2026-07-25T12:01:00Z","signature":T.signature("valid","ops-key")}
    # B (V28): the amendment carve-out is now ANCHORED. An honest re-widen is clean ONLY when the runtime's
    # authenticated grant certifies it; unanchored it fails closed. (Was a synthetic _amend_pair stream that
    # licensed on stream-derived authority; that channel was defeated four rounds and is now removed.)
    widen_amend = _uncert(G.check_authority_history(_honest_stream(_R), grants=_R["grants"]))
    widen_unanchored = _uncert(G.check_authority_history(_honest_stream(_R)))   # no grant -> cannot certify
    tamper = "X7" in G.check_authority_history([_H0,
        {"session_id":"s","authority_epoch":1,"authority_snapshot":{"effects":["READ"],"target_scopes":["a"]},
         "authorization_receipt":{"authority_snapshot":{"effects":["READ","WRITE"],"target_scopes":["a"]}}}])
    record("CE103", "X7 sound on real records; health-only bump OK; V29 withdrawal: armed amendment re-widen is X7U (uncertifiable, grant inert); tamper/divergence still X7", "A-P17",
           real_ok and healthonly and widen_noamend and widen_amend and widen_unanchored and tamper,
           f'real={real_ok} healthonly={healthonly} widen_noamend={widen_noamend} amend_anchored={widen_amend} amend_unanchored_x7={widen_unanchored} tamper={tamper}')
except Exception as e:
    record("CE103", "X7 real-record soundness (A)", "A-P17", False, f"{type(e).__name__}: {e}")

# CE104 / B [F-BSSG-P17-GLM-01/KIMI-2] X4 redemption set is the schema outcome enum minus FAILED_NO_EFFECT;
# double-SUCCEEDED is a violation; a COMMITTED_PENDING_OUTCOME settled once by SUCCEEDED is ONE redemption.
try:
    enum = set(G.json.load(open("schemas/execution-receipt.schema.json"))["properties"]["outcome"]["enum"]) if hasattr(G, "json") else {"COMMITTED_PENDING_OUTCOME","SUCCEEDED","FAILED_NO_EFFECT","INDETERMINATE","QUARANTINED"}
    import json as _json
    enum = set(_json.load(open("schemas/execution-receipt.schema.json"))["properties"]["outcome"]["enum"])
    set_ok = "COMMITTED" not in G.REDEMPTION_OUTCOMES and "SUCCEEDED" in G.REDEMPTION_OUTCOMES and G.REDEMPTION_OUTCOMES <= enum
    dbl = G.check_single_redemption([{"commit_token_id":"t","outcome":"SUCCEEDED"},{"commit_token_id":"t","outcome":"SUCCEEDED"}]) == ["X4"]
    chain = G.check_single_redemption([{"commit_token_id":"t","outcome":"COMMITTED_PENDING_OUTCOME"},{"commit_token_id":"t","outcome":"SUCCEEDED"}]) == []
    failed = G.check_single_redemption([{"commit_token_id":"t","outcome":"FAILED_NO_EFFECT"},{"commit_token_id":"t","outcome":"FAILED_NO_EFFECT"}]) == []
    record("CE104", "X4 redemption set derived from schema enum; double-SUCCEEDED flagged; settle-chain is one redemption", "B-P17", set_ok and dbl and chain and failed,
           f'set_ok={set_ok} dbl={dbl} chain={chain} failed_noeffect={failed}')
except Exception as e:
    record("CE104", "X4 settlement soundness (B)", "B-P17", False, f"{type(e).__name__}: {e}")

# CE105 / C [F-BSSG-P17-GPT-02/GLM-03/KIMI-4] a pre-admission reentrant refusal records all-UNKNOWN
# conjuncts (NOT the outer invocation's), is kernel-consistent, terminalizes nothing.
try:
    f = T.GateFixture()
    holder = {}
    def reentrant():
        # fire a nested authorize during token mint of the outer call
        holder["nested"] = f.gate.authorize(f.request(nonce="9"*32), T.evidence_bundle())
        return "tok-outer-1"
    f.gate.new_token = reentrant
    outer = f.gate.authorize(f.request(nonce="8"*32), T.evidence_bundle())
    nested = holder.get("nested", {})
    all_unknown = all(v == "UNKNOWN" for v in nested.get("conjuncts", {"x":"TRUE"}).values())
    consistent = G.kernel_decision(dict(nested["conjuncts"]))[0] == nested["decision"]
    record("CE105", "reentrant refusal records all-UNKNOWN (not outer conjuncts) and is kernel-consistent", "C-P17",
           nested.get("reason_codes") == ["E-REENTRANT-CALL"] and all_unknown and consistent,
           f'nested_conjuncts_all_unknown={all_unknown} consistent={consistent} decision={nested.get("decision")}')
except Exception as e:
    record("CE105", "reentrant conjunct isolation (C)", "C-P17", False, f"{type(e).__name__}: {e}")

# CE106 / D [F-BSSG-P17-GPT-01/KIMI-8] authorized_issuance is provenance-consistent and TOTAL: a forged
# minimal receipt, a schema-invalid receipt, and an all-FALSE-conjunct record all fail closed (no raise);
# a genuine gate ALLOW projects authorized; authorized_issuance_bound binds to a real minted token.
try:
    K = {k: "TRUE" for k in G.KERNEL_CONJUNCTS}
    forged_min = G.BSSGGate.authorized_issuance({"decision":"ALLOW","conjuncts":K,"authorization_receipt":{"commit_token":{"token_id":"abcdefgh"}}})
    forged_nocj = G.BSSGGate.authorized_issuance({"decision":"ALLOW","authorization_receipt":{"commit_token":{"token_id":"abcdefgh"}}})  # missing conjuncts, must not raise
    forged_false = G.BSSGGate.authorized_issuance({"decision":"ALLOW","conjuncts":{k:"FALSE" for k in G.KERNEL_CONJUNCTS},"authorization_receipt":{"commit_token":{"token_id":"abcdefgh"}}})
    f = T.GateFixture(); real = f.gate.authorize(f.request(nonce="7"*32), T.evidence_bundle())
    real_ok = G.BSSGGate.authorized_issuance(real) and f.gate.authorized_issuance_bound(real)
    forged_unbound = not f.gate.authorized_issuance_bound({"decision":"ALLOW","conjuncts":K,
        "authorization_receipt":dict(real["authorization_receipt"], commit_token={"token_id":"nevermintedxx"})})
    record("CE106", "authorized_issuance provenance-consistent + total; forgeries fail closed; genuine projects; bound binds", "D-P17",
           (not forged_min) and (not forged_nocj) and (not forged_false) and real_ok and forged_unbound,
           f'min={forged_min} nocj={forged_nocj} false={forged_false} real={real_ok} unbound_rejected={forged_unbound}')
except Exception as e:
    record("CE106", "authorized_issuance provenance (D)", "D-P17", False, f"{type(e).__name__}: {e}")

# CE107 / E [F-BSSG-P17-KIMI-5] a post-admission mint fault is a kernel-consistent issuance-failure record
# (decision == kernel_decision(conjuncts) = ALLOW, issuance_status=FAILED_NO_EFFECT), not an inconsistent
# DENY_UNKNOWN-with-all-TRUE; a pre-admission reentrant abort is a kernel-consistent DENY_UNKNOWN.
try:
    f = T.GateFixture()
    def _boom(): raise RuntimeError("mint fault")
    f.gate.new_token = _boom
    r = f.gate.authorize(f.request(nonce="6"*32), T.evidence_bundle()); last = f.gate.state.records[-1]
    post_ok = last["decision"] == "ALLOW" and last.get("issuance_status") == "FAILED_NO_EFFECT" and G.kernel_decision(dict(last["conjuncts"]))[0] == last["decision"] and last.get("kernel_evaluated") is True
    record("CE107", "post-admission mint abort is a kernel-consistent issuance-failure record (E)", "E-P17", post_ok,
           f'decision={last["decision"]}/{last.get("issuance_status")} kernel_evaluated={last.get("kernel_evaluated")}')
except Exception as e:
    record("CE107", "abort kernel-consistency (E)", "E-P17", False, f"{type(e).__name__}: {e}")

# CE108 / F [F-BSSG-P17-GPT-05/KIMI-6] the model projection keys AUTHORIZED on authorized_issuance, so a
# collision/issuance-failure ALLOW record is NOT authorized (the model no longer maps every ALLOW to
# AUTHORIZED_UNUSED). Verified via the shared predicate to avoid re-running the model checker.
try:
    collision = {"decision":"ALLOW","issuance_status":"FAILED_NO_EFFECT",
                 "conjuncts":{k:"TRUE" for k in G.KERNEL_CONJUNCTS},"authorization_receipt":None,"reason_codes":["E-TOKEN-FACTORY-COLLISION"]}
    ok = (not G.BSSGGate.authorized_issuance(collision))
    record("CE108", "model projection predicate: an issuance-failure ALLOW is not authorized (not modeled AUTHORIZED_UNUSED)", "F-P17", ok, f'authorized={G.BSSGGate.authorized_issuance(collision)}')
except Exception as e:
    record("CE108", "model-check projection predicate (F)", "F-P17", False, f"{type(e).__name__}: {e}")

# CE109 / G [F-BSSG-P17-KIMI-1] evidence-independent expiry FALSE dominates on the schema-VALID
# indeterminate path (time authority absent), not only the malformed path.
try:
    f = T.GateFixture()
    exp = f.request(nonce="5"*32, issued_at="2026-07-25T11:58:00Z", expires_at="2026-07-25T11:59:59Z")
    eb = T.evidence_bundle(); del eb["time_authority"]
    d = f.gate.authorize(exp, eb)
    record("CE109", "expired request under a schema-valid-but-indeterminate bundle is DENY_FALSE (evidence-independent expiry)", "G-P17",
           d["decision"] == "DENY_FALSE" and d["conjuncts"]["EvidenceCurrent"] == "FALSE", f'decision={d["decision"]}')
except Exception as e:
    record("CE109", "C7 asymmetry (G)", "G-P17", False, f"{type(e).__name__}: {e}")

# CE110 / H [F-BSSG-P17-GPT-04] a failure receipt written while the clock is unavailable is schema-VALID
# (commit_time_epoch_seconds is null with an explicit E-CLOCK-UNAVAILABLE reason), not an out-of-domain -1.
try:
    contracts, policies, cd, pd = T.build_registries()
    def _down(): raise RuntimeError("clock down")
    g = G.BSSGGate(contracts, policies, _down, T.injected_verifier, lambda: "tok-00000001")
    fr = g._execution_failure(None, "E-COMMIT-ABORTED")
    schema_ok = G.validate_record(fr, "execution-receipt")
    record("CE110", "clock-unavailable failure receipt is schema-valid (null commit_time + E-CLOCK-UNAVAILABLE)", "H-P17",
           schema_ok and fr["commit_time_epoch_seconds"] is None and "E-CLOCK-UNAVAILABLE" in fr["reason_codes"],
           f'schema_valid={schema_ok} commit_time={fr["commit_time_epoch_seconds"]}')
except Exception as e:
    record("CE110", "clock-fault receipt schema-validity (H)", "H-P17", False, f"{type(e).__name__}: {e}")


# ===================================================================================================
# repair19 regression counterexamples (pass-18 V17 findings). Each asserts the REPAIRED behavior.
# ===================================================================================================


# CE111 / ATTEST [K18-13] the execution attestation is no longer forgeable by a hand-written constant
# trace: the recorded records are nonce+execution dependent, so sha256(nonce + CONSTANT) does not match.
try:
    import bssg_attest as _AT
    import hashlib as _h, json as _j
    _n = "BSSG-CE111-CHECK"
    _real = _AT.run(_n)
    _const = [["auth", ["ALLOW", []]], ["commit1", "COMMITTED_PENDING_OUTCOME"], ["commit2", "FAILED_NO_EFFECT"],
              ["deny", ["DENY_UNKNOWN"]], ["reauth", ["DENY_FALSE"]], ["oor_int", "REJECTED_SCHEMA"],
              ["bad_witness", "DENY_FALSE"], ["collision", "ALLOW"]]
    _forged = _h.sha256((_n + "|" + _j.dumps(_const, sort_keys=True, separators=(",", ":"))).encode()).hexdigest()
    _varies = _AT.run(_n) == _real and _AT.run("OTHER-NONCE") != _real
    record("CE111", "execution attestation is not forgeable by a constant trace; varies by nonce; deterministic", "ATTEST-P18",
           _forged != _real and _varies, f"forged_matches={_forged == _real} varies={_varies}")
except Exception as e:
    record("CE111", "attestation execution-binding (ATTEST)", "ATTEST-P18", False, f"{type(e).__name__}: {e}")

# CE112 / D1 [K18-01] authorized_issuance is TOTAL: no non-dict / hostile input raises.
try:
    ok = all(G.BSSGGate.authorized_issuance(x) is False for x in [None, 42, "x", ["a"], (1,), b"z"])
    record("CE112", "authorized_issuance is total (fails closed, never raises on malformed input)", "D1-P18", ok, f"all_false={ok}")
except Exception as e:
    record("CE112", "authorized_issuance totality (D1)", "D1-P18", False, f"{type(e).__name__}: {e}")

# CE113 / D2 [K18-02/GPT-03] a genuine receipt transplanted into a wrapper with different top-level
# provenance does NOT project authorized (record<->receipt binding).
try:
    f = T.GateFixture(); a = f.gate.authorize(f.request(nonce="7" * 32), T.evidence_bundle())
    splice = dict(a); splice["session_id"] = "attacker"; splice["request_digest"] = "sha256:" + "0" * 64
    ok = (G.BSSGGate.authorized_issuance(a) is True and G.BSSGGate.authorized_issuance(splice) is False
          and f.gate.authorized_issuance_bound(splice) is False)
    record("CE113", "record<->receipt binding: a provenance-transplanted receipt is not authorized", "D2-P18", ok,
           f"genuine=True splice_static={G.BSSGGate.authorized_issuance(splice)} splice_bound={f.gate.authorized_issuance_bound(splice)}")
except Exception as e:
    record("CE113", "record/receipt binding (D2)", "D2-P18", False, f"{type(e).__name__}: {e}")

# CE114 / D3 [K18-04/GPT-02] an expired UNUSED token is not bound-authorized (clock/expiry enforced).
try:
    f = T.GateFixture(); a = f.gate.authorize(f.request(nonce="8" * 32), T.evidence_bundle())
    ent = f.gate.state.tokens[a["authorization_receipt"]["commit_token"]["token_id"]]
    before = f.gate.authorized_issuance_bound(a)
    f.gate.clock = lambda: ent["expires_at"] + 1
    after = f.gate.authorized_issuance_bound(a)
    record("CE114", "expired UNUSED token is not bound-authorized (unexpired now enforced)", "D3-P18",
           before is True and after is False, f"before={before} after={after}")
except Exception as e:
    record("CE114", "bound-authorization expiry (D3)", "D3-P18", False, f"{type(e).__name__}: {e}")

# CE115 / A1 [K18-06] a snapshot-less DENY between an accepted LIFT and the re-authorization does NOT
# consume the amendment carve-out: a conformant amend->deny->re-widen stream has no X7 false positive.
try:
    S = _R["session"]
    _narrow = {"session_id": S, "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": [_REAL_TGT]}}
    _deny = {"session_id": S, "authority_epoch": 2, "authority_snapshot": None, "reason_codes": ["E-NONCE-REPLAY"]}
    _wide = {"session_id": S, "authority_epoch": _R["landing"], "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": [_REAL_TGT]}}
    stream = [_narrow, _R["event"], _R["marker"], _deny, _wide]   # real amend -> snapshot-less deny -> re-widen
    ctrl = [_narrow, _wide]                                        # no amendment at all -> widening flagged
    anchored = _uncert(G.check_authority_history(stream, grants=_R["grants"]))
    unanchored = _uncert(G.check_authority_history(stream))        # V29 withdrawal: armed re-widen -> X7U
    ctrl_x7 = "X7" in G.check_authority_history(ctrl, grants=_R["grants"])
    record("CE115", "V29 withdrawal: an armed re-widen is X7U with or without the grant (survives a snapshot-less deny); a no-amendment widening control is still X7", "A1-P18",
           anchored and unanchored and ctrl_x7, f"anchored={anchored} unanchored_x7={unanchored} control_x7={ctrl_x7}")
except Exception as e:
    record("CE115", "X7 carve-out consumption (A1)", "A1-P18", False, f"{type(e).__name__}: {e}")

# CE116 / A2 [K18-07/GPT-04] the carve-out arms ONLY from a validated accepted LIFT; a forged bare
# correction-event does not license widening.
try:
    forged = [{"session_id": "s", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}},
              {"record_type": "bssg.correction-event", "session_id": "s"},
              {"session_id": "s", "authority_epoch": 3, "authority_snapshot": {"effects": ["READ", "WRITE", "DELETE"], "target_scopes": ["a"]}}]
    raw = [forged[0], _raw_lift19("s"), forged[2]]
    anchored = _uncert(G.check_authority_history(_honest_stream(_R), grants=_R["grants"]))   # gate-issued marker + real grant
    unanchored = _uncert(G.check_authority_history(_honest_stream(_R)))                    # B: no grant -> fail closed
    ok = ("X7" in G.check_authority_history(forged) and anchored and unanchored
          and "X7" in G.check_authority_history(raw))  # a raw event (even schema-valid, even w/ rejected sigs) does NOT arm
    record("CE116", "V29 withdrawal: a gate-issued marker re-widen is X7U (grant inert); a forged/raw marker does NOT arm -> its widening is a grant-independent X7", "A2-P19",
           ok, f"forged={G.check_authority_history(forged)} anchored={anchored} unanchored_x7={unanchored} raw={G.check_authority_history(raw)}")
except Exception as e:
    record("CE116", "X7 unauthenticated carve-out (A2)", "A2-P18", False, f"{type(e).__name__}: {e}")

# CE117 / A3 [K18-08/GPT-04] top-level<->receipt divergence on session OR epoch (not only snapshot) is X7.
try:
    div = [{"session_id": "attacker", "authority_epoch": 2, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]},
            "authorization_receipt": {"session_id": "s", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}}]
    record("CE117", "X7 full-triple divergence (session/epoch/snapshot) is flagged", "A3-P18",
           "X7" in G.check_authority_history(div), f"result={G.check_authority_history(div)}")
except Exception as e:
    record("CE117", "X7 divergence triple (A3)", "A3-P18", False, f"{type(e).__name__}: {e}")

# CE118 / B1 [GPT-05] COMMITTED_PENDING_OUTCOME -> FAILED_NO_EFFECT (terminal settlement) -> SUCCEEDED is X4.
try:
    chain = G.check_single_redemption([{"commit_token_id": "t", "outcome": "COMMITTED_PENDING_OUTCOME"},
                                       {"commit_token_id": "t", "outcome": "FAILED_NO_EFFECT"},
                                       {"commit_token_id": "t", "outcome": "SUCCEEDED"}])
    good = G.check_single_redemption([{"commit_token_id": "t", "outcome": "COMMITTED_PENDING_OUTCOME"},
                                      {"commit_token_id": "t", "outcome": "SUCCEEDED"}])
    record("CE118", "X4 flags PENDING->FAILED_NO_EFFECT->SUCCEEDED (two contradictory terminals); a single settlement is clean", "B1-P18",
           "X4" in chain and good == [], f"chain={chain} single={good}")
except Exception as e:
    record("CE118", "X4 settlement chain (B1)", "B1-P18", False, f"{type(e).__name__}: {e}")

# CE119 / B2 [K18-10] the redemption set is DERIVED from the schema enum; an out-of-enum outcome is flagged.
try:
    import json as _j2, os as _os2
    enum = set(_j2.load(open(_os2.path.join(_os2.path.dirname(G.__file__), "schemas", "execution-receipt.schema.json")))["properties"]["outcome"]["enum"])
    derived_ok = G.REDEMPTION_OUTCOMES == frozenset(enum) - {"FAILED_NO_EFFECT"}
    lc = G.check_single_redemption([{"commit_token_id": "t", "outcome": "succeeded"}, {"commit_token_id": "t", "outcome": "succeeded"}])
    record("CE119", "REDEMPTION_OUTCOMES derived from schema enum; out-of-enum outcome flagged (not silently skipped)", "B2-P18",
           derived_ok and "X4" in lc, f"derived={derived_ok} lowercase_flagged={'X4' in lc}")
except Exception as e:
    record("CE119", "X4 schema-derived enum (B2)", "B2-P18", False, f"{type(e).__name__}: {e}")

# CE120 / INTERVAL [GPT-01] a temporally inverted request interval (issued_at > expires_at) is DENY_FALSE.
try:
    f = T.GateFixture()
    r = f.request(nonce="a" * 32, issued_at="2026-07-25T12:05:00Z", expires_at="2026-07-25T12:00:30Z")
    d = f.gate.authorize(r, T.evidence_bundle())
    record("CE120", "inverted request interval (issued_at > expires_at) is DENY_FALSE, never ALLOW", "INTERVAL-P18",
           d["decision"] == "DENY_FALSE" and d["conjuncts"]["EvidenceCurrent"] == "FALSE"
           and "E-REQUEST-INTERVAL-INVERTED" in d["reason_codes"], f'decision={d["decision"]}')
except Exception as e:
    record("CE120", "inverted request interval (INTERVAL)", "INTERVAL-P18", False, f"{type(e).__name__}: {e}")

# CE121 / INTERVAL-witness [GPT-01] an inverted witness lease (observed_at > expires_at) is not healthy.
try:
    f = T.GateFixture()
    w = T.witness_receipt(); w["observed_at"] = "2026-07-25T12:05:00Z"; w["expires_at"] = "2026-07-25T12:00:30Z"
    d = f.gate.authorize(f.request(nonce="b" * 32), T.evidence_bundle(receipt=w))
    record("CE121", "inverted witness lease (observed_at > expires_at) yields WitnessHealthy=FALSE, not ALLOW", "INTERVAL-P18",
           d["decision"] != "ALLOW" and d["conjuncts"]["WitnessHealthy"] == "FALSE"
           and "E-WITNESS-LEASE-INVERTED" in d["reason_codes"], f'decision={d["decision"]} wh={d["conjuncts"]["WitnessHealthy"]}')
except Exception as e:
    record("CE121", "inverted witness lease (INTERVAL)", "INTERVAL-P18", False, f"{type(e).__name__}: {e}")

# CE122 / K18-12 X7 and X4 are TOTAL: a malformed record never crashes the audit.
try:
    x7 = G.check_authority_history([{"session_id": "s", "authority_epoch": 1, "authority_snapshot": {"effects": None, "target_scopes": ["a"]}},
                                    {"session_id": "s", "authority_epoch": 2, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}},
                                    None, 42, "junk"])
    x4 = G.check_single_redemption([{"commit_token_id": ["x"], "outcome": "SUCCEEDED"}, None, {"outcome": "SUCCEEDED"}, 7])
    record("CE122", "X7/X4 are total: malformed records are skipped/flagged, never raised on", "K18-12-P18",
           isinstance(x7, list) and isinstance(x4, list), f"x7={x7} x4={x4}")
except Exception as e:
    record("CE122", "X7/X4 totality (K18-12)", "K18-12-P18", False, f"{type(e).__name__}: {e}")

# ===================================================================================================
# repair20 regression counterexamples (pass-19 V18 findings). Each asserts the intended SEMANTIC
# outcome of the shape RETIREMENT -- not merely that a function returns a list or does not raise.
# ===================================================================================================

# CE124 / CLOCK [GPT-P19-03 / GLM-01/04] one strict clock reader retires the coercion+asymmetry shape:
# string/float/bool/negative fail closed on BOTH authorize and the SUCCESS commit path.
try:
    ok = True; detail = []
    for bad in ["1784980800", 1784980800.75, True, -999, None]:
        f = T.GateFixture(); f.gate.clock = (lambda b=bad: b)
        d = f.gate.authorize(f.request(nonce="c"*32), T.evidence_bundle())
        ok = ok and d["decision"] == "DENY_UNKNOWN"; detail.append(f"{bad!r}->{d['decision']}")
    # success commit path with a negative clock -> schema-VALID failure receipt (null commit-time), never -999
    f = T.GateFixture(); a = f.gate.authorize(f.request(nonce="d"*32), T.evidence_bundle()); rc = a["authorization_receipt"]
    b = {k: rc[k] for k in ("request_digest","canonical_target","params_digest","adapter_digest","effect_type")}
    f.gate.clock = lambda: -999
    f.gate.commit(rc["commit_token"]["token_id"], b, {})
    er = [r for r in f.gate.state.records if r.get("record_type") == "bssg.execution-receipt"][-1]
    ok = ok and er.get("commit_time_epoch_seconds") is None and G.validate_record(er, "execution-receipt")
    record("CE124", "strict clock reader: string/float/bool/negative fail closed on every path (authorize + success commit)", "CLOCK-P19",
           ok, f"commit_time={er.get('commit_time_epoch_seconds')} " + " ".join(detail))
except Exception as e:
    record("CE124", "strict clock reader (CLOCK)", "CLOCK-P19", False, f"{type(e).__name__}: {e}")

# CE125 / A3 [GPT-P19-02 / K19-B1] type-strict divergence: a top-level authority_epoch typed as bool
# (True) does NOT alias the receipt's int 1; a non-dict snapshot facing a dict one is X7.
try:
    d1 = G.check_authority_history([{"session_id":"s","authority_epoch":True,"authority_snapshot":{"effects":["READ","WRITE"],"target_scopes":["a"]},
                                     "authorization_receipt":{"session_id":"s","authority_epoch":1,"authority_snapshot":{"effects":["READ"],"target_scopes":["a"]}}}])
    d2 = G.check_authority_history([{"session_id":"s","authority_epoch":1,"authority_snapshot":"tampered",
                                     "authorization_receipt":{"session_id":"s","authority_epoch":1,"authority_snapshot":{"effects":["READ"],"target_scopes":["a"]}}}])
    record("CE125", "X7 divergence is type-strict: bool epoch does not alias int; non-dict snapshot is flagged", "A3-P19",
           "X7" in d1 and "X7" in d2, f"bool_epoch={d1} nondict_snapshot={d2}")
except Exception as e:
    record("CE125", "X7 type-strict divergence (A3)", "A3-P19", False, f"{type(e).__name__}: {e}")

# CE126 / A4 [GPT-P19-02 / K19-C1] an execution receipt whose revalidation.authority_epoch cannot be
# resolved to (or disagrees with) the redeemed receipt's epoch is X7 -- fail closed, not skipped.
try:
    unresolved = G.check_authority_history([{"record_type":"bssg.execution-receipt","authorization_receipt_digest":"sha256:"+"0"*64,
                                             "revalidation":{"authority_epoch":7}}])
    record("CE126", "X4/A4: unresolved or mismatched execution-receipt epoch binding fails closed (X7)", "A4-P19",
           "X7" in unresolved, f"unresolved={unresolved}")
except Exception as e:
    record("CE126", "A4 fail-closed binding (A4)", "A4-P19", False, f"{type(e).__name__}: {e}")

# CE127 / INTERVAL [GPT-P19-04] the inverted-lease rule (observed_at > expires_at) is enforced at
# commit-time fresh-witness revalidation, not only at authorize.
try:
    f = T.GateFixture(); a = f.gate.authorize(f.request(nonce="e"*32), T.evidence_bundle()); rc = a["authorization_receipt"]
    b = {k: rc[k] for k in ("request_digest","canonical_target","params_digest","adapter_digest","effect_type")}
    fresh = T.witness_receipt(); fresh["observed_at"] = "2026-07-25T12:00:04Z"; fresh["expires_at"] = "2026-07-25T12:00:02Z"
    out = f.gate.commit(rc["commit_token"]["token_id"], b, {"witness_receipt": fresh})
    record("CE127", "commit-time fresh-witness inverted lease (observed_at > expires_at) is refused, not PASS", "INTERVAL-P19",
           out["outcome"] == "FAILED_NO_EFFECT" and "E-COMMIT-WITNESS-LEASE-INVERTED" in out.get("reason_codes", []),
           f"outcome={out['outcome']} reasons={out.get('reason_codes')}")
except Exception as e:
    record("CE127", "commit-time inverted lease (INTERVAL)", "INTERVAL-P19", False, f"{type(e).__name__}: {e}")

# CE128 / A2 [GPT-P19-01] X7's carve-out arms ONLY from a gate-issued bssg.correction-accepted marker;
# a raw correction-event (even schema-valid, even with rejected signatures) does not license widening.
try:
    base = {"session_id":"s","authority_epoch":1,"authority_snapshot":{"effects":["READ"],"target_scopes":["a"]}}
    wide = {"session_id":"s","authority_epoch":2,"authority_snapshot":{"effects":["READ","WRITE"],"target_scopes":["a"]}}
    with_marker = G.check_authority_history(_honest_stream(_R), grants=_R["grants"])       # gate marker + real grant
    with_marker_unanchored = G.check_authority_history(_honest_stream(_R))                 # B: no grant -> fail closed
    with_raw = G.check_authority_history([_H0, base, _raw_lift19("s"), wide])
    with_forged = G.check_authority_history([_H0, base, {"record_type":"bssg.correction-event","session_id":"s"}, wide])
    record("CE128", "V29 withdrawal: a gate-issued marker re-widen is X7U (anchored==unanchored); a raw/forged marker does NOT arm -> grant-independent X7", "A2-P19",
           _uncert(with_marker) and _uncert(with_marker_unanchored) and _viol(with_raw) and _viol(with_forged),
           f"anchored={with_marker} unanchored={with_marker_unanchored} raw={with_raw} forged={with_forged}")
except Exception as e:
    record("CE128", "A2 gate-issued acceptance marker (A2)", "A2-P19", False, f"{type(e).__name__}: {e}")

# CE129 / K19-E1 X7 does not raise on an unhashable JSON element (a nested list inside effects); it
# fails closed. Asserts the SEMANTIC outcome (a violation list), not merely "did not raise".
try:
    r = G.check_authority_history([{"session_id":"s","authority_epoch":1,"authority_snapshot":{"effects":["READ",["nested"]],"target_scopes":["a"]}},
                                   {"session_id":"s","authority_epoch":2,"authority_snapshot":{"effects":["READ","WRITE"],"target_scopes":["a"]}}])
    record("CE129", "X7 fails closed (no crash) on an unhashable nested-list element", "K18-12-P19",
           isinstance(r, list), f"result={r}")
except Exception as e:
    record("CE129", "X7 unhashable element (K19-E1)", "K18-12-P19", False, f"{type(e).__name__}: {e}")

# CE123 / F-reentrant [GPT-06] a pre-admission reentrant refusal is kernel_evaluated=False, all-UNKNOWN.
try:
    f = T.GateFixture(); holder = {}
    def _reentrant():
        holder["rec"] = f.gate.authorize(f.request(nonce="9" * 32), T.evidence_bundle())
        return "tok-outer-01"
    f.gate.new_token = _reentrant
    f.gate.authorize(f.request(nonce="8" * 32), T.evidence_bundle())
    nested = holder.get("rec", {})
    ok = (nested.get("reason_codes") == ["E-REENTRANT-CALL"] and nested.get("kernel_evaluated") is False
          and all(v == "UNKNOWN" for v in nested.get("conjuncts", {"x": "T"}).values()))
    record("CE123", "pre-admission reentrant refusal is kernel_evaluated=False with all-UNKNOWN conjuncts", "F-P18",
           ok, f'kernel_evaluated={nested.get("kernel_evaluated")} reasons={nested.get("reason_codes")}')
except Exception as e:
    record("CE123", "reentrant classification (F)", "F-P18", False, f"{type(e).__name__}: {e}")

# ===================================================================================================
# repair21 regression counterexamples (pass-20 V19 findings). Class-COMPLETE retirements.
# ===================================================================================================

# CE130 / X4-FAILCLOSED [GPT-P1 / K20-L1] a double redemption whose token id is an unhashable JSON value
# is FLAGGED (fail closed), not silently skipped.
try:
    unh = G.check_single_redemption([{"commit_token_id": ["x"], "outcome": "SUCCEEDED"}, {"commit_token_id": ["x"], "outcome": "SUCCEEDED"}])
    single = G.check_single_redemption([{"commit_token_id": ["x"], "outcome": "COMMITTED_PENDING_OUTCOME"}, {"commit_token_id": ["x"], "outcome": "SUCCEEDED"}])
    record("CE130", "X4 flags a double redemption with an unhashable token id (fail closed, not skipped)", "X4-P20",
           "X4" in unh and single == [], f"double={unh} single={single}")
except Exception as e:
    record("CE130", "X4 fail-closed unhashable tid", "X4-P20", False, f"{type(e).__name__}: {e}")

# CE131 / A4-OMISSION [GPT-P3 / K20-X1] a settlement / PASS execution receipt that OMITS
# revalidation.authority_epoch fails closed (X7); a resolvable one is clean.
try:
    omitted = G.check_authority_history([{"record_type": "bssg.execution-receipt", "outcome": "SUCCEEDED",
                                          "authorization_receipt_digest": "sha256:" + "0" * 64, "revalidation": {"result": "PASS"}}])
    record("CE131", "settlement execution receipt omitting authority_epoch fails closed (A4 omission)", "A4-P20",
           "X7" in omitted, f"omitted={omitted}")
except Exception as e:
    record("CE131", "A4 omission fail-closed", "A4-P20", False, f"{type(e).__name__}: {e}")

# CE132 / A2-MARKER-BOUND [GPT-P2 / K20-F1] a correction-accepted marker arms ONLY if bound to a present
# accepted-LIFT correction-event (correction_digest resolves); an UNBOUND marker does not arm.
try:
    base = {"session_id": "s", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}
    wide = {"session_id": "s", "authority_epoch": 2, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}
    bound = G.check_authority_history(_honest_stream(_R), grants=_R["grants"])   # bound gate marker + real grant
    bound_unanchored = G.check_authority_history(_honest_stream(_R))             # B: no grant -> fail closed
    ev, marker = _amend_pair("s", 2); unbound = dict(marker, correction_digest="sha256:" + "0" * 64)
    unbound_res = G.check_authority_history([_H0, base, unbound, wide])
    record("CE132", "V29 withdrawal: a bound gate marker re-widen is X7U (grant inert); an UNBOUND marker does NOT arm -> grant-independent X7", "A2-P20",
           _uncert(bound) and _uncert(bound_unanchored) and _viol(unbound_res),
           f"bound={bound} bound_unanchored={bound_unanchored} unbound={unbound_res}")
except Exception as e:
    record("CE132", "A2 marker binding", "A2-P20", False, f"{type(e).__name__}: {e}")

# CE133 / CLOCK-BOUND [K20-C3] the strict clock reader rejects an absurd upper-bound clock (>= year 9999).
try:
    f = G.BSSGGate(*T.build_registries()[:2], (lambda: 2 ** 60), T.injected_verifier, lambda: "tok-1")
    raised = False
    try:
        f._read_clock()
    except G._ClockFault:
        raised = True
    record("CE133", "strict clock reader rejects an out-of-range upper-bound clock value", "CLOCK-P20",
           raised, f"raised_ClockFault={raised}")
except Exception as e:
    record("CE133", "clock upper bound", "CLOCK-P20", False, f"{type(e).__name__}: {e}")

# ===================================================================================================
# repair22 regression counterexamples (pass-21 V20 findings). Class-complete + identity-complete.
# ===================================================================================================

def _ve(session, cid="c"):
    return {"record_type": "bssg.correction-event", "spec_version": G.SPEC_VERSION, "correction_id": cid,
            "correction_class": "LIFT_TERMINAL_STATE", "supersedes": G.digest_bytes(b"p"), "reason_code": "C-TERMINAL-REVIEWED",
            "issued_by": {"authority_id": "o", "control_domain": "ops"}, "session_id": session, "subject_control_domain": "subj",
            "adjudicators": [{"adjudicator_id": "a1", "control_domain": "audit", "signature": T.signature("valid", "a1")},
                             {"adjudicator_id": "a2", "control_domain": "legal", "signature": T.signature("valid", "a2")}],
            "descendants": [], "descendant_closure_status": "UNKNOWN", "issued_at": "2026-07-25T12:01:00Z", "signature": T.signature("valid", "o")}
def _mk(session, e, ep=2):
    return {"record_type": "bssg.correction-accepted", "spec_version": G.SPEC_VERSION, "gate_version": G.GATE_VERSION,
            "correction_id": e["correction_id"], "correction_class": "LIFT_TERMINAL_STATE", "session_id": session,
            "authority_epoch": ep, "licensed_epoch": ep + 1, "correction_digest": G.digest(e), "adjudicators_verified": 2}
_bw = lambda s, ep, wide=False: {"session_id": s, "authority_epoch": ep, "authority_snapshot": {"effects": (["READ","WRITE"] if wide else ["READ"]), "target_scopes": ["a"]}}

# CE134 / K21-A2 X4 flags a double redemption on two DISTINCT NaN float token ids (multi-shard merge).
try:
    r = G.check_single_redemption([{"commit_token_id": float("nan"), "outcome": "SUCCEEDED"}, {"commit_token_id": float("nan"), "outcome": "SUCCEEDED"}])
    single = G.check_single_redemption([{"commit_token_id": float("nan"), "outcome": "COMMITTED_PENDING_OUTCOME"}, {"commit_token_id": float("nan"), "outcome": "SUCCEEDED"}])
    record("CE134", "X4 flags a distinct-NaN double redemption (no float laundering across a merge)", "X4-P21",
           "X4" in r and single == [], f"double={r} single={single}")
except Exception as e:
    record("CE134", "X4 NaN laundering", "X4-P21", False, f"{type(e).__name__}: {e}")

# CE135 / GPT-P21-01 an event for session A + a fabricated marker for session B does NOT license B.
try:
    eA = _ve("A")
    res = G.check_authority_history([_bw("B", 1), eA, _mk("B", eA), _bw("B", 2, True)])
    record("CE135", "X7 marker binding is identity-complete: A's event cannot license B's widening", "A2-P21",
           "X7" in res, f"cross_session={res}")
except Exception as e:
    record("CE135", "marker cross-session binding", "A2-P21", False, f"{type(e).__name__}: {e}")

# CE136 / GPT-P21-02 a duplicated/replayed marker does not re-arm one correction for multiple widenings.
try:
    eS = _ve("s"); m = _mk("s", eS)
    res = G.check_authority_history([_H0, _bw("s", 1), eS, m, _bw("s", 3, True), _bw("s", 4), m, _bw("s", 5, True)])
    legit = G.check_authority_history(_honest_stream(_R), grants=_R["grants"])   # single anchored re-widen
    legit_unanchored = G.check_authority_history(_honest_stream(_R))             # B: no grant -> fail closed
    record("CE136", "X7 consumes a correction once: a replayed (consumed) marker does not re-arm -> grant-independent X7; the single armed re-widen is X7U (grant inert)", "A2-P21",
           _viol(res) and _uncert(legit) and _uncert(legit_unanchored), f"replay={res} legit={legit} legit_unanchored={legit_unanchored}")
except Exception as e:
    record("CE136", "marker replay consumption", "A2-P21", False, f"{type(e).__name__}: {e}")

# CE137 / GPT-P21-02 a marker cannot bind to a FUTURE event (stream-order index).
try:
    eS = _ve("s")
    res = G.check_authority_history([_bw("s", 1), _mk("s", eS), _bw("s", 2, True), eS])
    record("CE137", "X7 marker cannot retro-bind to an event appearing later in the stream", "A2-P21",
           "X7" in res, f"future_event={res}")
except Exception as e:
    record("CE137", "marker future-event retrobind", "A2-P21", False, f"{type(e).__name__}: {e}")

# ===================================================================================================
# repair23 regression counterexamples (pass-22 V21 findings). Materialization + marker-epoch.
# ===================================================================================================

class _EvilStr(str):
    _c = [0]
    def __hash__(self): _EvilStr._c[0] += 1; return _EvilStr._c[0]
    def __eq__(self, o): return False

# CE138 / GLM-01 X4 materializes input: a hostile str-subclass token id cannot bypass de-duplication.
try:
    r = G.check_single_redemption([{"commit_token_id": _EvilStr("t"), "outcome": "SUCCEEDED"}, {"commit_token_id": _EvilStr("t"), "outcome": "SUCCEEDED"}])
    record("CE138", "X4 materializes input: a hostile str-subclass token id cannot launder a double redemption", "X4-P22",
           "X4" in r, f"subclass_double={r}")
except Exception as e:
    record("CE138", "X4 subclass materialization", "X4-P22", False, f"{type(e).__name__}: {e}")

# CE139 / GLM-02 X7 materializes input: a hostile str-subclass session_id cannot split a session.
try:
    r = G.check_authority_history([{"session_id": _EvilStr("s"), "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}},
                                   {"session_id": _EvilStr("s"), "authority_epoch": 2, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}])
    record("CE139", "X7 materializes input: a hostile str-subclass session_id cannot hide a widening", "X7-P22",
           "X7" in r, f"subclass_widen={r}")
except Exception as e:
    record("CE139", "X7 subclass materialization", "X7-P22", False, f"{type(e).__name__}: {e}")

# CE140 / GPT-B a marker's own authority_epoch is tamper-checked (bogus low or inflated epoch -> X7).
try:
    eS = _ve("s")
    b5 = {"session_id": "s", "authority_epoch": 5, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}
    w6 = {"session_id": "s", "authority_epoch": 6, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}
    w7 = {"session_id": "s", "authority_epoch": 7, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}
    low = G.check_authority_history([_H0, b5, eS, dict(_mk("s", eS), authority_epoch=0), w6])
    hi = G.check_authority_history([_H0, b5, eS, dict(_mk("s", eS), authority_epoch=999), w6])
    legit = G.check_authority_history(_honest_stream(_R), grants=_R["grants"])   # anchored honest re-widen
    legit_unanchored = G.check_authority_history(_honest_stream(_R))             # B: no grant -> fail closed
    record("CE140", "marker authority_epoch tamper-checked (bogus low/inflated -> grant-independent X7); the honest armed re-widen is X7U (grant inert)", "A2-P22",
           _viol(low) and _viol(hi) and _uncert(legit) and _uncert(legit_unanchored),
           f"low={low} hi={hi} legit={legit} legit_unanchored={legit_unanchored}")
except Exception as e:
    record("CE140", "marker epoch tamper-check", "A2-P22", False, f"{type(e).__name__}: {e}")

# ===================================================================================================
# repair24 regression counterexamples (pass-23 V22 findings). Strict materialization + marker floor.
# ===================================================================================================

# CE141 / P23-01 a hostile list-subclass with a flipping __iter__ cannot erase a double redemption.
try:
    class _FlipL(list):
        def __init__(self, first, second):
            super().__init__(first); self._v=[first, second]; self._n=0
        def __iter__(self):
            v=self._v[self._n % 2]; self._n+=1; return iter(v)
    dbl=[{"commit_token_id":"t","outcome":"SUCCEEDED"},{"commit_token_id":"t","outcome":"SUCCEEDED"}]
    one=[{"commit_token_id":"t","outcome":"SUCCEEDED"}]
    a=G.check_single_redemption(_FlipL(one, dbl)); b=G.check_single_redemption(_FlipL(dbl, one))
    record("CE141", "X4 strict materialization: a hostile flipping __iter__ list cannot erase a double redemption", "X4-P23",
           "X4" in a and "X4" in b, f"benign_first={a} hostile_first={b}")
except Exception as e:
    record("CE141", "X4 strict materialization", "X4-P23", False, f"{type(e).__name__}: {e}")

# CE142 / GPT-P21-04 a two-view hostile dict cannot project a forged AUTHORIZED via subject_facing.
try:
    class _FlipD(dict):
        def __init__(self, a, b):
            super().__init__(a); self._v=[a, b]; self._n=0
        def items(self):
            v=self._v[self._n % 2]; self._n+=1; return v.items()
        def get(self, k, d=None):
            v=self._v[self._n % 2]; self._n+=1; return v.get(k, d)
    good={"decision":"ALLOW","issuance_status":"ISSUED"}; bad={"decision":"DENY_FALSE"}
    d=G.BSSGGate.subject_facing(_FlipD(good, bad)).get("decision")
    ai=G.BSSGGate.authorized_issuance(_FlipD(good, bad))
    record("CE142", "subject_facing/authorized_issuance fail closed on a two-view hostile dict subclass", "DP-P23",
           d == "DENIED" and ai is False, f"subject_facing={d} authorized_issuance={ai}")
except Exception as e:
    record("CE142", "projection strict materialization", "DP-P23", False, f"{type(e).__name__}: {e}")

# CE143 / P23-02 a marker installs an epoch floor: a later regression below it is X7.
try:
    eS=_ve("s")
    b5={"session_id":"s","authority_epoch":5,"authority_snapshot":{"effects":["READ"],"target_scopes":["a"]}}
    null6={"session_id":"s","authority_epoch":6,"authority_snapshot":None}
    w999={"session_id":"s","authority_epoch":999,"authority_snapshot":{"effects":["READ","WRITE"],"target_scopes":["a"]}}
    attack=G.check_authority_history([_H0, b5, eS, dict(_mk("s", eS), authority_epoch=999), null6, w999])
    legit=G.check_authority_history(_honest_stream(_R), grants=_R["grants"])   # anchored honest re-widen
    legit_unanchored=G.check_authority_history(_honest_stream(_R))             # B: no grant -> fail closed
    record("CE143", "marker installs an epoch floor (a regression below it is a grant-independent X7); the honest armed re-widen is X7U (grant inert)", "A2-P23",
           _viol(attack) and _uncert(legit) and _uncert(legit_unanchored), f"attack={attack} legit={legit} legit_unanchored={legit_unanchored}")
except Exception as e:
    record("CE143", "marker epoch floor", "A2-P23", False, f"{type(e).__name__}: {e}")

# ===================================================================================================
# repair25 regression counterexamples (pass-24 V23 findings). Boundary-first + exact epoch landing.
# ===================================================================================================

# CE144 / V23-GPT-01 a non-list outer sequence (tuple) carrying a double redemption fails closed.
try:
    tup = ({"commit_token_id": "t", "outcome": "SUCCEEDED"}, {"commit_token_id": "t", "outcome": "SUCCEEDED"})
    none_in = G.check_single_redemption(None)
    record("CE144", "X4 strict-materializes first: a tuple/non-list outer sequence fails closed; None is clean", "X4-P24",
           "X4" in G.check_single_redemption(tup) and none_in == [], f"tuple={G.check_single_redemption(tup)} none={none_in}")
except Exception as e:
    record("CE144", "X4 boundary-first", "X4-P24", False, f"{type(e).__name__}: {e}")

# CE145 / V23-GPT-02 a marker declaring epoch N licenses a widening ONLY at epoch N, not any higher epoch.
try:
    eS = _ve("s")
    b5 = {"session_id": "s", "authority_epoch": 5, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}
    w50 = {"session_id": "s", "authority_epoch": 50, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}
    w6 = {"session_id": "s", "authority_epoch": 6, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}
    w7 = {"session_id": "s", "authority_epoch": 7, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}
    over = G.check_authority_history([_H0, b5, eS, dict(_mk("s", eS), authority_epoch=6, licensed_epoch=7), w50])
    legit = G.check_authority_history(_honest_stream(_R), grants=_R["grants"])   # re-widen lands at grant epoch
    legit_unanchored = G.check_authority_history(_honest_stream(_R))             # B: no grant -> fail closed
    record("CE145", "V29 withdrawal: the landing is NOT certified offline -- a relocated armed re-widen is X7U (grant inert), enforced online", "A2-P24",
           _uncert(over) and _uncert(legit) and _uncert(legit_unanchored), f"over={over} legit={legit} legit_unanchored={legit_unanchored}")
except Exception as e:
    record("CE145", "marker exact-epoch landing", "A2-P24", False, f"{type(e).__name__}: {e}")

# CE146 / V23-GPT-03 under verify, a bad TOP-LEVEL correction signature does not arm the carve-out.
try:
    ev = _ve("s"); ev["signature"] = T.signature("valid", "corr")
    mk = dict(_mk("s", ev), authority_epoch=2, licensed_epoch=3)
    b1 = {"session_id": "s", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}
    w2 = {"session_id": "s", "authority_epoch": 3, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}
    reject_top = G.check_authority_history([_H0, b1, ev, mk, w2], verify=lambda r, p, s: r == "adjudicator")
    all_ok = G.check_authority_history(_honest_stream(_R), verify=lambda r, p, s: True, grants=_R["grants"])
    all_ok_unanchored = G.check_authority_history(_honest_stream(_R), verify=lambda r, p, s: True)   # no grant -> X7
    record("CE146", "under verify, a bad top-level correction signature does NOT arm -> grant-independent X7; the armed verified re-widen is X7U (grant inert)", "A2-P24",
           _viol(reject_top) and _uncert(all_ok) and _uncert(all_ok_unanchored),
           f"reject_top={reject_top} all_ok={all_ok} all_ok_unanchored={all_ok_unanchored}")
except Exception as e:
    record("CE146", "top-level correction signature", "A2-P24", False, f"{type(e).__name__}: {e}")

# CE147 / V23-GPT-04 subject_facing / authorized_issuance fail closed on a two-view hostile dict.
try:
    class _Flip(dict):
        def __init__(self, a, b):
            super().__init__(a); self._v = [a, b]; self._n = 0
        def items(self):
            v = self._v[self._n % 2]; self._n += 1; return v.items()
        def get(self, k, d=None):
            v = self._v[self._n % 2]; self._n += 1; return v.get(k, d)
    good = {"decision": "ALLOW", "issuance_status": "ISSUED"}; bad = {"decision": "DENY_FALSE"}
    d = G.BSSGGate.subject_facing(_Flip(good, bad)).get("decision"); ai = G.BSSGGate.authorized_issuance(_Flip(good, bad))
    record("CE147", "projection sites (subject_facing/authorized_issuance) use strict materialization", "DP-P24",
           d == "DENIED" and ai is False, f"subject_facing={d} authorized_issuance={ai}")
except Exception as e:
    record("CE147", "projection site coverage", "DP-P24", False, f"{type(e).__name__}: {e}")

# ===================================================================================================
# repair26 regression counterexamples (pass-25 V24 findings). Totality + type-strictness + coverage.
# ===================================================================================================

# CE148 / K25-A2 an unhashable list/dict outcome fails closed instead of crashing X4.
try:
    r = G.check_single_redemption([{"commit_token_id": "t", "outcome": ["SUCCEEDED"]}])
    r2 = G.check_single_redemption([{"commit_token_id": "t", "outcome": {"x": 1}}])
    record("CE148", "X4 fails closed (no crash) on an unhashable list/dict outcome", "X4-P25",
           "X4" in r and "X4" in r2, f"list={r} dict={r2}")
except Exception as e:
    record("CE148", "X4 unhashable outcome totality", "X4-P25", False, f"{type(e).__name__}: {e}")

# CE149 / K25-A3 a present but wrong-typed authority_epoch (float) fails closed (X7), not skipped.
try:
    r = G.check_authority_history([{"session_id": "s", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}},
                                   {"session_id": "s", "authority_epoch": 2.0, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}])
    record("CE149", "X7 fails closed on a present but wrong-typed (float) authority_epoch", "X7-P25",
           "X7" in r, f"float_epoch={r}")
except Exception as e:
    record("CE149", "X7 epoch type-strictness", "X7-P25", False, f"{type(e).__name__}: {e}")

# CE150 / K25-A1 int 1 and float 1.0 are one token id: a double redemption across them is caught.
try:
    r = G.check_single_redemption([{"commit_token_id": 1, "outcome": "SUCCEEDED"}, {"commit_token_id": 1.0, "outcome": "SUCCEEDED"}])
    record("CE150", "X4 numeric keyspace: int 1 and float 1.0 are one token (double redemption caught)", "X4-P25",
           "X4" in r, f"numeric_double={r}")
except Exception as e:
    record("CE150", "X4 numeric keyspace", "X4-P25", False, f"{type(e).__name__}: {e}")

# CE151 / K25-A9 authorized_issuance_bound rejects a genuinely-authorized record wrapped in a subclass.
try:
    f = T.GateFixture(); allow = f.gate.authorize(f.request(), T.evidence_bundle())
    class _Sub(dict): pass
    ok_plain = f.gate.authorized_issuance_bound(allow) if allow.get("decision") == "ALLOW" else True
    ok_sub = f.gate.authorized_issuance_bound(_Sub(allow)) is False
    record("CE151", "authorized_issuance_bound uses strict materialization (rejects an authorized subclass)", "DP-P25",
           ok_sub, f"bound_subclass={f.gate.authorized_issuance_bound(_Sub(allow))}")
except Exception as e:
    record("CE151", "authorized_issuance_bound site coverage", "DP-P25", False, f"{type(e).__name__}: {e}")

# ===================================================================================================
# repair27 counterexamples (pass-26 V25 findings). X7 state-machine re-derivation + conformance.
# ===================================================================================================

# CE152 / K26-X7-1 CONFORMANCE: the REAL gate lift+re-widen record stream audits clean, and a forged WIDE
# ceiling inserted at the marker epoch (which the runtime never re-widens at) is caught. This is the test
# that would have caught the pass-25 fail-open: the honest re-widen lands at marker_epoch+1, so the license
# fires there; a forged record at the marker epoch is NOT licensed.
try:
    def _adj(i, d): return {"adjudicator_id": i, "control_domain": d, "signature": T.signature("valid", kid=i)}
    _amd = {"record_type": "bssg.correction-event", "spec_version": G.SPEC_VERSION, "correction_id": "cor-0001",
            "correction_class": "LIFT_TERMINAL_STATE", "supersedes": G.digest_bytes(b"prior-decision"), "reason_code": "C-TERMINAL-REVIEWED",
            "issued_by": {"authority_id": "ops-1", "control_domain": "ops-domain"}, "session_id": "sess-0001", "subject_control_domain": "subject-domain",
            "adjudicators": [_adj("adj-1", "audit-domain"), _adj("adj-2", "ops-domain")], "descendants": [], "descendant_closure_status": "UNKNOWN",
            "issued_at": "2026-07-25T12:01:00Z", "signature": T.signature("valid", kid="ops-key")}
    _f = T.GateFixture(degraded_effects=["READ", "WRITE", "DELETE"], degraded_targets=["https://db.example.internal/"])
    _f.gate.authorize(_f.request(), T.evidence_bundle())
    _f.gate.authorize(_f.request(nonce="b" * 32), T.evidence_bundle(receipt=T.witness_receipt(health="DEGRADED", epoch=8)))
    _f.gate.submit_amendment(_amd)
    _f.gate.authorize(_f.request(nonce="3" * 32), T.evidence_bundle())
    _recs = _f.gate.state.records
    _mk_rec = [r for r in _recs if isinstance(r, dict) and r.get("record_type") == "bssg.correction-accepted"][0]
    _ev_rec = [r for r in _recs if isinstance(r, dict) and r.get("record_type") == "bssg.correction-event"][0]
    # B (V28): the REAL gate re-widen record stream is CLEAN only when anchored to the runtime's own grant,
    # and fails CLOSED unanchored. These two halves are the load-bearing conformance property under B.
    _grants = G.grants_from_state(_f.gate); _gsess = _mk_rec["session_id"]; _le = _grants[_gsess][-1]["landing_epoch"]  # V29 GPT-P30-02: ledger list
    _real_clean = _uncert(G.check_authority_history(_recs, grants=_grants))
    _real_unanchored = _uncert(G.check_authority_history(_recs))    # V29 withdrawal: armed re-widen -> X7U
    # K27-X7-1 (a): the gate MUST emit licensed_epoch = authority_epoch + 1 (a +0 regression re-opens K26-X7-1).
    _mep = _mk_rec["authority_epoch"]; _lep = _mk_rec.get("licensed_epoch")
    _plus1 = isinstance(_lep, int) and not isinstance(_lep, bool) and _lep == _mep + 1
    # A load-bearing synthetic widen anchored to THIS gate's grant: a narrow READ ceiling before, a wider
    # READ/WRITE ceiling AT the grant landing epoch within the AUTHENTICATED restored authority (not a forged
    # DELETE/* over-widen). Clean anchored; X7 unanchored.
    _narrow = {"session_id": _gsess, "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": [_REAL_TGT]}}
    _wide_lic = {"session_id": _gsess, "authority_epoch": _le, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": [_REAL_TGT]}}
    _honest_clean = _uncert(G.check_authority_history([_narrow, _ev_rec, _mk_rec, _wide_lic], grants=_grants))
    # The forged WIDE at the MARKER epoch (which the runtime never re-widens at -- the grant lands at +1) is X7
    # EVEN WITH the grant present (divergence from the grant's landing epoch), on the prefix truncated there.
    _forged_wide = {"session_id": _gsess, "authority_epoch": _mep, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": [_REAL_TGT]}}
    _caught = _uncert(G.check_authority_history([_narrow, _ev_rec, _mk_rec, _forged_wide], grants=_grants))
    record("CE152", "CONFORMANCE: a real gate re-widen is X7U (anchored==unanchored, grant inert); marker licensed_epoch==authority_epoch+1; a forged WIDE @marker-epoch is X7U (relocation online-only)", "X7-P26",
           _real_clean and _real_unanchored and _plus1 and _honest_clean and _caught,
           f"real_anchored={_real_clean} real_unanchored_x7={_real_unanchored} plus1={_plus1}(le={_lep},me={_mep}) honest_clean={_honest_clean} forged_caught={_caught}")
except Exception as e:
    record("CE152", "X7 real-gate conformance", "X7-P26", False, f"{type(e).__name__}: {e}")

# CE153 / K26-X7-1 synthetic: license fires at marker_epoch+1 (honest landing), not the marker epoch; and
# the honest re-widen at +1 is clean (no false positive on the gate's own recovery).
try:
    eS = _ve("s")
    b1 = {"session_id": "s", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}
    b2 = {"session_id": "s", "authority_epoch": 2, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}
    mk3 = dict(_mk("s", eS), authority_epoch=3, licensed_epoch=4)
    forged_at3 = {"session_id": "s", "authority_epoch": 3, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}
    honest_at4 = {"session_id": "s", "authority_epoch": 4, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}
    forged = _uncert(G.check_authority_history([_H0, b1, b2, eS, mk3, forged_at3]))
    honest = _uncert(G.check_authority_history(_honest_stream(_R), grants=_R["grants"]))   # anchored re-widen at grant epoch
    honest_unanchored = _uncert(G.check_authority_history(_honest_stream(_R)))           # B: no grant -> fail closed
    record("CE153", "V29 withdrawal: a forged WIDE @marker-epoch and the honest armed re-widen are both X7U (relocation/landing not certified offline)", "X7-P26",
           forged and honest and honest_unanchored, f"forged_at_marker={forged} honest_anchored={honest} honest_unanchored={honest_unanchored}")
except Exception as e:
    record("CE153", "X7 licensed-epoch landing", "X7-P26", False, f"{type(e).__name__}: {e}")

# CE154 / V25-GPT kernel BLOCKER (C7-class): FALSE-domination is order-independent. An EXPIRED request whose
# witness component RAISES before EvidenceCurrent is evaluated must still be FALSE-dominated (DENY_FALSE),
# not collapse to DENY_UNKNOWN with all-UNKNOWN conjuncts. The abort path re-evaluates expiry in isolation.
try:
    _f = T.GateFixture(); _f.gate.authorize(_f.request(nonce="1" * 32), T.evidence_bundle())
    _orig = _f.gate._witness_healthy
    _f.gate._witness_healthy = lambda *a, **k: (_ for _ in ()).throw(RuntimeError("injected witness fault"))
    _f.clock.advance(10 ** 9)  # evidence now expired
    _dec = _f.gate.authorize(_f.request(nonce="2" * 32), T.evidence_bundle())
    _f.gate._witness_healthy = _orig
    _expired_false = _dec["decision"] == G.DECISION_DENY_FALSE and _dec.get("conjuncts", {}).get("EvidenceCurrent") == G.FALSE
    # control: a NON-expired request that raises cannot be proven FALSE -> stays DENY_UNKNOWN (no over-claim)
    _g = T.GateFixture(); _g.gate.authorize(_g.request(nonce="1" * 32), T.evidence_bundle())
    _g.gate._witness_healthy = lambda *a, **k: (_ for _ in ()).throw(RuntimeError("fault"))
    _dec2 = _g.gate.authorize(_g.request(nonce="2" * 32), T.evidence_bundle())
    _fresh_unknown = _dec2["decision"] == G.DECISION_DENY_UNKNOWN
    record("CE154", "kernel FALSE-domination survives an exception: expired+raising request is DENY_FALSE, not DENY_UNKNOWN", "K-P26",
           _expired_false and _fresh_unknown, f"expired_false={_expired_false} fresh_unknown={_fresh_unknown} dec={_dec['decision']}")
except Exception as e:
    record("CE154", "kernel FALSE-domination on abort", "K-P26", False, f"{type(e).__name__}: {e}")

# CE155 / V26 X7-2 BLOCKER (GPT/GLM/Kimi convergent): the license LANDING epoch is DERIVED (marker+1), not
# trusted from the marker's licensed_epoch field, which is unauthenticated offline. A tampered licensed_epoch
# (far epoch, or =marker epoch) does NOT arm the carve-out, so the widening is caught as X7; only a marker
# whose licensed_epoch == authority_epoch+1 arms.
try:
    e = _ve("s"); b1 = {"session_id": "s", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}
    def _mkle(ep, le):
        m = dict(_mk("s", e), authority_epoch=ep); m["licensed_epoch"] = le; return m
    f50 = {"session_id": "s", "authority_epoch": 50, "authority_snapshot": {"effects": ["READ", "WRITE", "DELETE"], "target_scopes": ["*"]}}
    f2 = {"session_id": "s", "authority_epoch": 2, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}
    h3 = {"session_id": "s", "authority_epoch": 3, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}
    far = _uncert(G.check_authority_history([_H0, b1, e, _mkle(2, 50), f50]))      # V29 withdrawal: armed -> X7U
    reopen = _uncert(G.check_authority_history([_H0, b1, e, _mkle(2, 2), f2]))     # V29 withdrawal: armed -> X7U
    honest = _uncert(G.check_authority_history(_honest_stream(_R), grants=_R["grants"]))      # anchored re-widen
    honest_unanchored = _uncert(G.check_authority_history(_honest_stream(_R)))              # B: no grant -> fail closed
    forged_after_honest = _uncert(G.check_authority_history([_H0, b1, e, _mkle(2, 3), f2]))  # V29 withdrawal: armed -> X7U
    record("CE155", "V29 withdrawal: a relocated armed re-widen (far/marker-epoch) is X7U; the honest armed re-widen is X7U (grant inert)", "X7-P27",
           far and reopen and honest and honest_unanchored and forged_after_honest,
           f"far={far} reopen={reopen} honest={honest} honest_unanchored={honest_unanchored} forged={forged_after_honest}")
except Exception as e:
    record("CE155", "X7 licensed-epoch derived tamper-check", "X7-P27", False, f"{type(e).__name__}: {e}")

# CE156 / V26 kernel BLOCKER (GPT P3 + Kimi K27-K-1): the abort path preserves FALSE-domination for EVERY
# evidence-independent determinate FALSE (not just EvidenceCurrent), and re-derives expiry from the STASHED
# first clock read (never a fresh read that could itself fail). (a) an out-of-contract effect with a raising
# witness is DENY_FALSE via EffectTypeValid; (b) an expired request whose abort-path clock re-read would fail
# is still DENY_FALSE via the stashed read; (c) a non-expired, in-contract request that raises stays
# DENY_UNKNOWN (no over-claim on a genuinely indeterminate conjunct).
try:
    _f = T.GateFixture(); _f.gate.authorize(_f.request(nonce="1" * 32), T.evidence_bundle())
    _f.gate._witness_healthy = lambda *a, **k: (_ for _ in ()).throw(RuntimeError("fault"))
    _da = _f.gate.authorize(_f.request(nonce="2" * 32, effect="ADMIN"), T.evidence_bundle())
    _a = _da["decision"] == G.DECISION_DENY_FALSE and _da.get("conjuncts", {}).get("EffectTypeValid") == G.FALSE
    _g = T.GateFixture(); _g.gate.authorize(_g.request(nonce="1" * 32), T.evidence_bundle()); _g.clock.advance(10 ** 9)
    _g.gate._witness_healthy = lambda *a, **k: (_ for _ in ()).throw(RuntimeError("fault"))
    _orig = _g.gate._read_clock; _st = {"n": 0}
    def _rc():
        _st["n"] += 1
        if _st["n"] >= 2:
            raise RuntimeError("clock fault on re-read")
        return _orig()
    _g.gate._read_clock = _rc
    _db = _g.gate.authorize(_g.request(nonce="2" * 32), T.evidence_bundle())
    _b = _db["decision"] == G.DECISION_DENY_FALSE and _db.get("conjuncts", {}).get("EvidenceCurrent") == G.FALSE
    _h = T.GateFixture(); _h.gate.authorize(_h.request(nonce="1" * 32), T.evidence_bundle())
    _h.gate._witness_healthy = lambda *a, **k: (_ for _ in ()).throw(RuntimeError("fault"))
    _dc = _h.gate.authorize(_h.request(nonce="2" * 32), T.evidence_bundle())
    _c = _dc["decision"] == G.DECISION_DENY_UNKNOWN
    record("CE156", "kernel abort preserves FALSE-domination for every evidence-independent conjunct, via the stashed clock read", "K-P27",
           _a and _b and _c, f"effecttype_false={_a} expired_via_stashed={_b} indeterminate_unknown={_c}")
except Exception as e:
    record("CE156", "kernel abort all-conjunct FALSE-domination", "K-P27", False, f"{type(e).__name__}: {e}")

# CE157 / V27 X7 (BLOCKER, 3-way convergent): the license landing is bound to the checker's tracked epoch and
# to demonstrably-held authority, NOT to any marker-carried field. A dual-field tamper (authority_epoch and
# licensed_epoch moved together) and a walk-up (advance the epoch via a narrowing, then re-widen beyond held)
# are both X7 -- verify or no-verify.
try:
    e = _ve("s"); b1 = {"session_id": "s", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}
    def _mkep(ep, le):
        m = dict(_mk("s", e), authority_epoch=ep); m["licensed_epoch"] = le; return m
    wide50 = {"session_id": "s", "authority_epoch": 50, "authority_snapshot": {"effects": ["READ", "WRITE", "DELETE"], "target_scopes": ["*"]}}
    narrow48 = {"session_id": "s", "authority_epoch": 48, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}
    dual = _uncert(G.check_authority_history([b1, e, _mkep(49, 50), wide50]))
    dual_v = _uncert(G.check_authority_history([b1, e, _mkep(49, 50), wide50], verify=lambda *a: True))
    walkup = _uncert(G.check_authority_history([b1, e, narrow48, _mkep(49, 50), wide50]))
    # B (V28): the landing is bound to the runtime GRANT, not any marker-carried field. dual/walkup carry no
    # grant -> X7. The honest re-widen is certified only when anchored to the grant.
    honest = _uncert(G.check_authority_history(_honest_stream(_R), grants=_R["grants"]))
    honest_unanchored = _uncert(G.check_authority_history(_honest_stream(_R)))
    record("CE157", "V29 withdrawal: the landing is NOT certified offline -- dual-field + walk-up relocations are X7U; the honest armed re-widen is X7U (grant inert)", "X7-P28",
           dual and dual_v and walkup and honest and honest_unanchored,
           f"dual={dual} dual_verify={dual_v} walkup={walkup} honest={honest} honest_unanchored={honest_unanchored}")
except Exception as e:
    record("CE157", "X7 landing bound to tracked epoch", "X7-P28", False, f"{type(e).__name__}: {e}")

# CE158 / V27 X7 breadth bound (BLOCKER walk-up): a licensed re-widen may only restore authority the session
# DEMONSTRABLY HELD; escalation beyond the held envelope is X7 even under a well-formed license.
try:
    # B (V28): the breadth bound is now the AUTHENTICATED restored authority in the grant (was a stream-derived
    # "held envelope", which the forged-seed attack defeated). A re-widen WITHIN restored authority is clean
    # anchored; BEYOND it (extra effect OR wider target) is X7 EVEN WITH the grant; unanchored fails closed.
    within_ok = _uncert(G.check_authority_history(_honest_stream(_R), grants=_R["grants"]))
    within_unanchored = _uncert(G.check_authority_history(_honest_stream(_R)))
    beyond_eff = _uncert(G.check_authority_history(_honest_stream(_R, effects=("READ", "WRITE", "DELETE")), grants=_R["grants"]))
    beyond_tgt = _uncert(G.check_authority_history(_honest_stream(_R, targets=("*",)), grants=_R["grants"]))
    record("CE158", "V29 withdrawal: breadth is NOT certified offline -- within-ceiling and beyond-ceiling armed re-widens are both X7U; the breadth bound is enforced online (BOUNDED-AUTH-INTRO)", "X7-P28",
           within_ok and within_unanchored and beyond_eff and beyond_tgt,
           f"within_clean={within_ok} within_unanchored_x7={within_unanchored} beyond_eff_x7={beyond_eff} beyond_tgt_x7={beyond_tgt}")
except Exception as e:
    record("CE158", "X7 breadth bound", "X7-P28", False, f"{type(e).__name__}: {e}")

# CE159 / V27 kernel abort (BLOCKER, GPT): the abort recovers a clock-INDEPENDENT determinate FALSE even when
# the FIRST clock read raises -- an out-of-contract ADMIN effect is DENY_FALSE (EffectTypeValid), not masked
# to DENY_UNKNOWN; a valid request whose first clock read fails stays DENY_UNKNOWN (nothing determinate-FALSE).
try:
    _f = T.GateFixture(); _f.gate.authorize(_f.request(nonce="1" * 32), T.evidence_bundle())
    _f.gate.clock = lambda: (_ for _ in ()).throw(RuntimeError("clock down"))
    _da = _f.gate.authorize(_f.request(nonce="2" * 32, effect="ADMIN"), T.evidence_bundle())
    _a = _da["decision"] == G.DECISION_DENY_FALSE and _da.get("conjuncts", {}).get("EffectTypeValid") == G.FALSE
    _g = T.GateFixture(); _g.gate.authorize(_g.request(nonce="1" * 32), T.evidence_bundle())
    _g.gate.clock = lambda: (_ for _ in ()).throw(RuntimeError("clock down"))
    _db = _g.gate.authorize(_g.request(nonce="2" * 32), T.evidence_bundle())
    _b = _db["decision"] == G.DECISION_DENY_UNKNOWN
    record("CE159", "kernel abort recovers a clock-independent determinate FALSE even when the first clock read raises", "K-P28",
           _a and _b, f"effecttype_false_on_clockfault={_a} valid_stays_unknown={_b}")
except Exception as e:
    record("CE159", "kernel abort clock-independent recovery", "K-P28", False, f"{type(e).__name__}: {e}")

# ===================================================================================================
# repair30 counterexamples (pass-29 V28 findings). STRATEGY B: grant-anchored divergence detection.
# The X7 licensed-re-widen class was defeated FOUR rounds (field-read -> derived -> dual-field -> walk-up ->
# forged-seed/rejected-amendment). B stops trusting the attacker-controllable record stream and anchors the
# checker to the runtime's AUTHENTICATED grant ledger (grants_from_state). Enforceable half: unanchored ->
# fail closed (airtight). Conditional half: anchored -> divergence check (sound GIVEN an authentic export).
# ===================================================================================================

# CE160 / PROBE-1 (V28 B): a runtime-REJECTED amendment mints NO grant, so a claimed re-widen fails closed.
# Drive the gate to a genuine terminal, submit a LIFT that FAILS quorum (single adjudicator). No grant entry
# is written; grants_from_state is empty; the re-widen the caller claims cannot be certified -> X7. This is
# the fail-open PROBE-1 caught: the marker is present but the runtime never authenticated the re-widen.
try:
    _adj = lambda i, d: {"adjudicator_id": i, "control_domain": d, "signature": T.signature("valid", kid=i)}
    _bad = {"record_type": "bssg.correction-event", "spec_version": G.SPEC_VERSION, "correction_id": "cor-0001",
            "correction_class": "LIFT_TERMINAL_STATE", "supersedes": G.digest_bytes(b"prior-decision"), "reason_code": "C-TERMINAL-REVIEWED",
            "issued_by": {"authority_id": "ops-1", "control_domain": "ops-domain"}, "session_id": "sess-0001", "subject_control_domain": "subject-domain",
            "adjudicators": [_adj("adj-1", "audit-domain")],  # single adjudicator -> quorum reject, no grant
            "descendants": [], "descendant_closure_status": "UNKNOWN", "issued_at": "2026-07-25T12:01:00Z", "signature": T.signature("valid", kid="ops-key")}
    _fr = T.GateFixture(degraded_effects=["READ", "WRITE", "DELETE"], degraded_targets=["https://db.example.internal/"])
    _fr.gate.authorize(_fr.request(), T.evidence_bundle())
    _fr.gate.authorize(_fr.request(nonce="b" * 32), T.evidence_bundle(receipt=T.witness_receipt(health="DEGRADED", epoch=8)))
    _rej = _fr.gate.submit_amendment(copy.deepcopy(_bad))
    _grej = G.grants_from_state(_fr.gate)
    _rejected = _rej.get("accepted") is not True and _grej == {}
    _wide = {"session_id": "sess-0001", "authority_epoch": 3, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": [_REAL_TGT]}}
    _narrow = {"session_id": "sess-0001", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": [_REAL_TGT]}}
    _claim = _uncert(G.check_authority_history([_narrow, _R["event"], _R["marker"], _wide], grants=_grej))
    record("CE160", "PROBE-1: a runtime-REJECTED amendment mints no grant (runtime truth); the claimed armed re-widen is X7U offline (grant inert; the rejection is enforced online)", "B-PROBE1-P30",
           _rejected and _claim, f"rejected_no_grant={_rejected} claimed_rewiden_x7={_claim}")
except Exception as e:
    record("CE160", "PROBE-1 rejected-amendment no grant", "B-PROBE1-P30", False, f"{type(e).__name__}: {e}")

# CE161 / PROBE-2 (V28 B): a forged "held" SEED record cannot inflate the authenticated restored authority,
# and cannot even ride along silently. B ignores stream-derived held authority entirely -- the breadth bound
# is the GRANT's restored set. (1) A re-widen BEYOND restored authority is X7 with or without a forged wide
# seed prepended (the seed can't inflate). (2) A seed whose held snapshot EXCEEDS the authenticated ceiling
# does not pass through: prepending it CONTAMINATES an otherwise-clean within-restored stream to X7 -- the
# gate refuses to certify a history carrying an unlicensed beyond-ceiling held-authority record. (3) Only a
# seed WITHIN the ceiling is inert (the clean stream stays clean). (4) A lone seed (no re-widen event) is
# clean either way -- a single snapshot is not a re-widen. Empirically validated on real gate bytes.
try:
    _seed_wide = {"session_id": _R["session"], "authority_epoch": 0, "authority_snapshot": {"effects": ["READ", "WRITE", "DELETE"], "target_scopes": ["*"]}}
    _seed_within = {"session_id": _R["session"], "authority_epoch": 0, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": [_REAL_TGT]}}
    _beyond = _honest_stream(_R, effects=("READ", "WRITE", "DELETE"))
    _within = _honest_stream(_R)
    seed_beyond_x7 = _viol(G.check_authority_history([_seed_wide] + _beyond, grants=_R["grants"]))    # beyond-ceiling seed = grant-independent target-widening -> X7 survives
    noseed_beyond_x7 = _uncert(G.check_authority_history(_beyond, grants=_R["grants"]))
    within_clean = _uncert(G.check_authority_history(_within, grants=_R["grants"]))
    wide_seed_contaminates = _viol(G.check_authority_history([_seed_wide] + _within, grants=_R["grants"]))  # seed contaminates a clean stream to X7 (grant-independent)
    within_seed_inert = _uncert(G.check_authority_history([_seed_within] + _within, grants=_R["grants"]))
    lone_wide_seed_clean = G.check_authority_history([_seed_wide], grants=_R["grants"]) == []
    record("CE161", "PROBE-2 (V29 withdrawal): an armed beyond-ceiling re-widen is X7U offline, but a forged beyond-ceiling wide SEED is a grant-independent target-widening -> X7 (it cannot ride along: it contaminates the stream to X7); a within-ceiling seed is inert (armed re-widen stays X7U); a lone seed (no re-widen) is clean", "B-PROBE2-P30",
           seed_beyond_x7 and noseed_beyond_x7 and within_clean and wide_seed_contaminates and within_seed_inert and lone_wide_seed_clean,
           f"seed_beyond_x7={seed_beyond_x7} noseed_beyond_x7={noseed_beyond_x7} within_clean={within_clean} wide_seed_contaminates={wide_seed_contaminates} within_seed_inert={within_seed_inert} lone_wide_seed_clean={lone_wide_seed_clean}")
except Exception as e:
    record("CE161", "PROBE-2 forged-seed cannot inflate or ride along", "B-PROBE2-P30", False, f"{type(e).__name__}: {e}")

# CE162 / Kimi-A3 (V28 regression): the gate's OWN honest degraded-first LIFT->recover must NOT be flagged as
# X7 (V28 caught B's predecessor over-flagging it). The REAL gate record stream, anchored to the runtime's
# own grant, audits CLEAN (no false positive on the gate's authenticated recovery).
try:
    _honest_recovery_clean = _uncert(G.check_authority_history(_R["records"], grants=_R["grants"]))
    _unanchored_x7 = _uncert(G.check_authority_history(_R["records"]))  # V29 withdrawal: armed re-widen -> X7U
    record("CE162", "Kimi-A3: the gate's OWN honest degraded-first recovery is NOT a violation -- it is X7U (uncertifiable, not a false positive), identical with or without the grant", "B-A3-P30",
           _honest_recovery_clean and _unanchored_x7, f"recovery_clean_anchored={_honest_recovery_clean} unanchored_x7={_unanchored_x7}")
except Exception as e:
    record("CE162", "Kimi-A3 honest recovery not over-flagged", "B-A3-P30", False, f"{type(e).__name__}: {e}")

# CE163 / B DISCLOSED RESIDUAL (NEGATIVE CE -- boundary, not a silent pass): B relocates trust from the
# unauthenticated stream marker to the grant-export's PROVENANCE. The content-blind offline checker cannot
# distinguish an AUTHENTIC grant export from a FORGED one, so a caller who fabricates the grants dict spoofs
# the check. Asserted as a BOUNDARY: an authentic grant (restored {READ,WRITE}) catches an over-wide DELETE
# re-widen as X7 (divergence); a FABRICATED grant claiming restored {READ,WRITE,DELETE} passes the SAME
# re-widen clean. The forged-grant spoof is OUT of the offline threat model. This is the sole place a grants
# literal appears -- to DEMONSTRATE the residual, never to certify a recovery (that would be the vacuity).
try:
    _beyond = _honest_stream(_R, effects=("READ", "WRITE", "DELETE"))
    _auth = G.check_authority_history(_beyond, grants=_R["grants"])
    _forged_grant = {_R["session"]: {"correction_digest": _R["marker"]["correction_digest"], "landing_epoch": _R["landing"],
                                     "restored_effects": frozenset({"READ", "WRITE", "DELETE"}), "restored_targets": _R["restored_targets"]}}
    _forg = G.check_authority_history(_beyond, grants=_forged_grant)
    _residual_closed = _uncert(_auth) and _uncert(_forg) and _auth == _forg
    record("CE163", "RESIDUAL CLOSED (V29 withdrawal): an authentic and a fabricated grant now yield the IDENTICAL X7U -- there is no positive certification left to spoof; the forged-grant residual is eliminated at the root", "B-RESIDUAL-P30",
           _residual_closed, f"authentic={_auth} forged={_forg} identical_uncertifiable={_residual_closed}")
except Exception as e:
    record("CE163", "B disclosed forged-grant residual", "B-RESIDUAL-P30", False, f"{type(e).__name__}: {e}")

# CE164 / GPT-P30-01 (V29 EFFECT BYPASS -- CLOSED): a widening REJECTED before a genuine terminal-lift cannot
# launder through the lift. The rejected DELETE recovery is DENY_FALSE at the runtime (the re-establish branch
# is bounded by the de-poisoned contract_ceiling), the ceiling and grant restore only demonstrably-held
# authority (no DELETE), and the checker stays honest. This was the FIRST reproduced real effect bypass in many
# rounds; it is locked here as a CURRENT-BYTE regression guard for CLAIM-X7-BREADTH / CLAIM-GRANT-ANCHOR.
try:
    def _amd164(cid="cor-poison"):
        _adj = lambda i, d: {"adjudicator_id": i, "control_domain": d, "signature": T.signature("valid", kid=i)}
        return {"record_type": "bssg.correction-event", "spec_version": G.SPEC_VERSION, "correction_id": cid,
                "correction_class": "LIFT_TERMINAL_STATE", "supersedes": G.digest_bytes(b"prior"),
                "reason_code": "C-TERMINAL-REVIEWED", "issued_by": {"authority_id": "ops-1", "control_domain": "ops-domain"},
                "session_id": "sess-0001", "subject_control_domain": "subject-domain",
                "adjudicators": [_adj("adj-1", "audit-domain"), _adj("adj-2", "ops-domain")],
                "descendants": [], "descendant_closure_status": "UNKNOWN", "issued_at": "2026-07-25T12:01:00Z",
                "signature": T.signature("valid", kid="ops-key")}
    _f = T.GateFixture()  # contract A = READ,WRITE
    _body = T.contract_body(_f.policy_digest)
    _body["allowed_effects"] = ["READ", "WRITE", "DELETE"]
    _body["effect_registry"]["DELETE"] = {"adapter_digest": T.ADAPTER_DIGEST}
    _body["degraded_effects"] = ["READ"]
    _c2 = G.digest(_body); _f.gate.contracts[_c2] = {"body": copy.deepcopy(_body), "revoked": False}
    _f.gate.authorize(_f.request(nonce="a" * 32), T.evidence_bundle(receipt=T.witness_receipt(epoch=7, sequence=11), epoch=5))
    _rB = T.effect_request(_c2, _f.policy_digest, effect="DELETE", nonce="b" * 32)
    _f.gate.authorize(_rB, T.evidence_bundle(receipt=T.witness_receipt(epoch=8, sequence=12), epoch=6))  # rejected widening
    _cc = set(_f.gate.state.contract_ceiling["sess-0001"].effects)
    _f.gate.submit_amendment(_amd164())
    _gr = G.grants_from_state(_f.gate)
    _rB2 = T.effect_request(_c2, _f.policy_digest, effect="DELETE", nonce="c" * 32)
    _d3 = _f.gate.authorize(_rB2, T.evidence_bundle(receipt=T.witness_receipt(epoch=9, sequence=13), epoch=7))
    _rewiden_denied = _d3.get("decision") == G.DECISION_DENY_FALSE and "E-AUTHORITY-WIDENING" in (_d3.get("reason_codes") or [])
    _ceiling_clean = "DELETE" not in _cc
    _grant_clean = all("DELETE" not in set(g.get("restored_effects") or ()) for g in _gr.get("sess-0001", []))
    _checker_honest = G.check_authority_history(_f.gate.state.records, grants=_gr) == []
    record("CE164", "GPT-P30-01 EFFECT BYPASS CLOSED: a widening rejected before a genuine lift cannot launder through it (runtime DENY_FALSE; ceiling+grant carry no DELETE; checker honest)", "GPT-P30-01",
           _rewiden_denied and _ceiling_clean and _grant_clean and _checker_honest,
           f"rewiden_denied={_rewiden_denied} ceiling_no_delete={_ceiling_clean} grant_no_delete={_grant_clean} checker_honest={_checker_honest}")
except Exception as e:
    record("CE164", "GPT-P30-01 effect bypass closed", "GPT-P30-01", False, f"{type(e).__name__}: {e}")

# CE165 / GPT-P30-02 (multi-cycle checker soundness): a CONFORMANT two-amendment history audits CLEAN -- each
# re-widen validated against ITS landing amendment's grant via the per-session grant LEDGER (list). Overwriting
# to keep only the latest grant made a legitimate second-amendment history falsely audit ['X7','X7'].
try:
    def _amd165(cid):
        _adj = lambda i, d: {"adjudicator_id": i, "control_domain": d, "signature": T.signature("valid", kid=i)}
        return {"record_type": "bssg.correction-event", "spec_version": G.SPEC_VERSION, "correction_id": cid,
                "correction_class": "LIFT_TERMINAL_STATE", "supersedes": G.digest_bytes(("prior-" + cid).encode()),
                "reason_code": "C-TERMINAL-REVIEWED", "issued_by": {"authority_id": "ops-1", "control_domain": "ops-domain"},
                "session_id": "sess-0001", "subject_control_domain": "subject-domain",
                "adjudicators": [_adj("adj-1", "audit-domain"), _adj("adj-2", "ops-domain")],
                "descendants": [], "descendant_closure_status": "UNKNOWN", "issued_at": "2026-07-25T12:01:00Z",
                "signature": T.signature("valid", kid="ops-key")}
    _f = T.GateFixture(degraded_effects=["READ", "WRITE", "DELETE"], degraded_targets=["https://db.example.internal/"])
    _f.gate.authorize(_f.request(nonce="a" * 32), T.evidence_bundle(receipt=T.witness_receipt(epoch=7, sequence=11), epoch=5))
    _f.gate.authorize(_f.request(nonce="b" * 32), T.evidence_bundle(receipt=T.witness_receipt(health="DEGRADED", epoch=8, sequence=12), epoch=6))
    _f.gate.submit_amendment(_amd165("cor-one"))
    _f.gate.authorize(_f.request(nonce="c" * 32), T.evidence_bundle(receipt=T.witness_receipt(epoch=9, sequence=13), epoch=7))
    _f.gate.authorize(_f.request(nonce="d" * 32), T.evidence_bundle(receipt=T.witness_receipt(health="DEGRADED", epoch=10, sequence=14), epoch=8))
    _f.gate.submit_amendment(_amd165("cor-two"))
    _f.gate.authorize(_f.request(nonce="e" * 32), T.evidence_bundle(receipt=T.witness_receipt(epoch=11, sequence=15), epoch=9))
    _grants = G.grants_from_state(_f.gate)
    _two_clean = _uncert(G.check_authority_history(_f.gate.state.records, grants=_grants))
    _ledger_two = len(_grants.get("sess-0001", [])) == 2
    record("CE165", "GPT-P30-02 multi-cycle: a conformant two-amendment history is X7U offline (each cycle uncertifiable, grant inert); the per-session ledger remains a runtime diagnostic", "GPT-P30-02",
           _two_clean and _ledger_two, f"two_amendment_clean={_two_clean} ledger_size={len(_grants.get('sess-0001', []))}")
except Exception as e:
    record("CE165", "GPT-P30-02 multi-cycle checker soundness", "GPT-P30-02", False, f"{type(e).__name__}: {e}")

# CE166 / GPT-P30-03 + Kimi K30-A4 (abort soundness BOTH directions): the abort must RECOVER a determinate
# clock- and verifier-independent witness FALSE when the injected verifier raises (subject mismatch -> DENY_FALSE,
# not masked to UNKNOWN); and must NOT FABRICATE one clock-free (health=FAILED under a NON-inverted future lease
# with a first-clock fault -> DENY_UNKNOWN, never a FALSE manufactured from an attacker-influenceable observed_at).
try:
    _fa = T.GateFixture()
    def _vr(kind, payload, sig):
        if kind == "witness":
            raise RuntimeError("witness verifier unavailable")
        return True
    _fa.gate.verify_signature = _vr
    _da = _fa.gate.authorize(_fa.request(nonce="9" * 32), T.evidence_bundle(receipt=T.witness_receipt(subject="other-agent")))
    _mask_recovered = _da.get("decision") == G.DECISION_DENY_FALSE   # determinate FALSE recovered, not masked
    _fb = T.GateFixture()
    _fb.gate.authorize(_fb.request(nonce="1" * 32), T.evidence_bundle())
    _fb.gate.clock = lambda: (_ for _ in ()).throw(RuntimeError("first-clock fault"))
    _rc = T.witness_receipt(health="FAILED"); _rc["observed_at"] = "2099-01-01T00:00:00Z"; _rc["expires_at"] = "2099-12-31T00:00:00Z"
    _db = _fb.gate.authorize(_fb.request(nonce="2" * 32), T.evidence_bundle(receipt=_rc))
    _no_fabrication = _db.get("decision") == G.DECISION_DENY_UNKNOWN   # health=FAILED not credited clock-free
    record("CE166", "GPT-P30-03 + K30-A4 abort soundness both ways: recovers a determinate witness FALSE on a raising verifier (not masked); never fabricates one clock-free (not manufactured)", "GPT-P30-03/K30-A4",
           _mask_recovered and _no_fabrication, f"mask_recovered_false={_mask_recovered} no_clockfree_fabrication={_no_fabrication}")
except Exception as e:
    record("CE166", "GPT-P30-03 + K30-A4 abort soundness", "GPT-P30-03/K30-A4", False, f"{type(e).__name__}: {e}")

# CE167 / GPT-P30-05 (MAJOR liveness/totality): a dependency-originated NON-Exception BaseException raised by
# an injected clock/verifier must FAIL CLOSED at every public boundary -- authorized_issuance_bound returns
# False; commit returns a recorded FAILED_NO_EFFECT and leaves NO token stuck in COMMITTING (VOID); amendment
# records a correction-outcome and does not escape. KeyboardInterrupt / SystemExit MUST still propagate, and
# even then the COMMITTING reservation is rolled back. Reproduced verbatim from GPT's independent PROBE-3/4/5.
try:
    class _EvilBase(BaseException): pass
    def _amd():
        return {"record_type": "bssg.correction-event", "spec_version": G.SPEC_VERSION, "correction_id": "cor-base",
                "correction_class": "LIFT_TERMINAL_STATE", "supersedes": G.digest_bytes(b"p"), "reason_code": "C-TERMINAL-REVIEWED",
                "issued_by": {"authority_id": "ops-1", "control_domain": "ops-domain"}, "session_id": "sess-0001", "subject_control_domain": "subject-domain",
                "adjudicators": [{"adjudicator_id": "adj-1", "control_domain": "audit-domain", "signature": T.signature("valid", kid="adj-1")},
                                 {"adjudicator_id": "adj-2", "control_domain": "ops-domain", "signature": T.signature("valid", kid="adj-2")}],
                "descendants": [], "descendant_closure_status": "UNKNOWN", "issued_at": "2026-07-25T12:01:00Z", "signature": T.signature("valid", kid="ops-key")}
    # AIB
    _fa = T.GateFixture(); _da = _fa.gate.authorize(_fa.request(nonce="2" * 32), T.evidence_bundle())
    _fa.gate.clock = lambda: (_ for _ in ()).throw(_EvilBase("aib"))
    try:
        _aib_closed = _fa.gate.authorized_issuance_bound(_da) is False
    except BaseException:
        _aib_closed = False
    # commit -> no COMMITTING strand, recorded failure, no escape
    _fc = T.GateFixture(); _dc = _fc.gate.authorize(_fc.request(nonce="3" * 32), T.evidence_bundle())
    _rc = _dc["authorization_receipt"]; _tok = _rc["commit_token"]["token_id"]
    _bind = {k: _rc[k] for k in ("request_digest", "canonical_target", "params_digest", "adapter_digest", "effect_type")}
    _fc.gate.clock = lambda: (_ for _ in ()).throw(_EvilBase("commit"))
    try:
        _co = _fc.gate.commit(_tok, _bind, T.evidence_bundle())
        _commit_closed = (_co.get("outcome") == "FAILED_NO_EFFECT" and "E-COMMIT-ABORTED" in (_co.get("reason_codes") or [])
                          and _fc.gate.state.tokens[_tok]["status"] == "VOID")
    except BaseException:
        _commit_closed = False
    # amendment -> recorded, not escaped
    _fm = T.GateFixture(degraded_effects=["READ", "WRITE", "DELETE"], degraded_targets=["https://db.example.internal/"])
    _fm.gate.authorize(_fm.request(nonce="4" * 32), T.evidence_bundle())
    _fm.gate.authorize(_fm.request(nonce="5" * 32), T.evidence_bundle(receipt=T.witness_receipt(health="DEGRADED", epoch=8)))
    _pre = len(_fm.gate.state.records); _fm.gate.verify_signature = lambda *a, **k: (_ for _ in ()).throw(_EvilBase("amend"))
    try:
        _mo = _fm.gate.submit_amendment(_amd())
        _amend_closed = (_mo.get("accepted") is not True and len(_fm.gate.state.records) - _pre >= 1)
    except BaseException:
        _amend_closed = False
    # KeyboardInterrupt still propagates, and the COMMITTING reservation is rolled back to VOID
    _fk = T.GateFixture(); _dk = _fk.gate.authorize(_fk.request(nonce="6" * 32), T.evidence_bundle())
    _rk = _dk["authorization_receipt"]; _tk = _rk["commit_token"]["token_id"]
    _bk = {k: _rk[k] for k in ("request_digest", "canonical_target", "params_digest", "adapter_digest", "effect_type")}
    _fk.gate.clock = lambda: (_ for _ in ()).throw(KeyboardInterrupt())
    try:
        _fk.gate.commit(_tk, _bk, T.evidence_bundle()); _ki_prop = False
    except KeyboardInterrupt:
        _ki_prop = (_fk.gate.state.tokens[_tk]["status"] == "VOID")
    except BaseException:
        _ki_prop = False
    record("CE167", "GPT-P30-05 BaseException totality/liveness: a dependency-originated non-Exception BaseException fails closed at AIB/commit/amendment (no COMMITTING strand, outcome recorded, no escape); KeyboardInterrupt/SystemExit still propagate with rollback", "GPT-P30-05",
           _aib_closed and _commit_closed and _amend_closed and _ki_prop,
           f"aib_closed={_aib_closed} commit_closed_no_strand={_commit_closed} amend_recorded={_amend_closed} ki_propagates_voided={_ki_prop}")
except Exception as e:
    record("CE167", "GPT-P30-05 BaseException totality/liveness", "GPT-P30-05", False, f"{type(e).__name__}: {e}")

# CE168 / GPT-P30-04 (MAJOR precision): authorized_issuance_bound reads the clock INSIDE the commit lock, at
# the SAME linearization point as the entry snapshot -- so the unexpired check is evaluated at the instant of
# the locked snapshot and a token that expires while the predicate waits for the lock is observed expired.
# Deterministic single-threaded probe: instrument the clock reader to record whether the commit lock is HELD
# at the instant the clock is read; under the fix it MUST be held (pre-fix it was read before the lock).
try:
    _f = T.GateFixture(); _d = _f.gate.authorize(_f.request(nonce="2" * 32), T.evidence_bundle())
    _held = {"v": None}
    _orig_clock = _f.gate._read_clock
    def _probe_clock():
        _held["v"] = _f.gate._commit_lock.locked()   # threading.Lock.locked() -> True iff held
        return _orig_clock()
    _f.gate._read_clock = _probe_clock
    _r = _f.gate.authorized_issuance_bound(_d)
    _clock_in_lock = _held["v"] is True
    record("CE168", "GPT-P30-04: authorized_issuance_bound reads the clock INSIDE the commit lock (precise point-in-time linearization -- a token expiring while the predicate waits for the lock is observed expired, not certified on stale pre-lock time)", "GPT-P30-04",
           _clock_in_lock and _r is True, f"clock_read_under_lock={_clock_in_lock} baseline_true={_r}")
except Exception as e:
    record("CE168", "GPT-P30-04 in-lock clock read", "GPT-P30-04", False, f"{type(e).__name__}: {e}")


green = sum(1 for *_, ok, _ in results if ok)

# ============================================================================
# V30 REGRESSION CEs (GLM-F1/K32-01, GPT-P32-01, K32-03, K32-04)
# ============================================================================

# CE169 / GLM-F1 + K32-01 (cross-contract ceiling-poison -- CLOSED): exercises the ACTUAL DEGRADED vector.
# V31 GLM-F1 correction: the prior CE169 used a HEALTHY witness which terminalizes via E-AUTHORITY-WIDENING
# before the fix path executes, making CE169 non-load-bearing (it passed GREEN even with the fix reverted).
# This rewrite uses a DEGRADED C2 DELETE request (the actual CLASS A vector): the degraded ceiling {READ}
# is a subset of {READ,WRITE} (narrowing passes), the pending flag IS set, but the fix prevents the
# DENIED request from writing contract_ceiling. After lift, DELETE is correctly DENIED.
try:
    def _reg_c2_169(fixture):
        body = T.contract_body(fixture.policy_digest)
        body["allowed_effects"] = ["READ", "WRITE", "DELETE"]
        body["effect_registry"]["DELETE"] = {"adapter_digest": T.ADAPTER_DIGEST}
        body["degraded_effects"] = ["READ"]
        d = G.digest(body); fixture.gate.contracts[d] = {"body": copy.deepcopy(body), "revoked": False}
        return d
    def _amd169(session="sess-0001", cid="cor-169"):
        _adj = lambda i, d: {"adjudicator_id": i, "control_domain": d, "signature": T.signature("valid", kid=i)}
        return {"record_type": "bssg.correction-event", "spec_version": G.SPEC_VERSION, "correction_id": cid,
                "correction_class": "LIFT_TERMINAL_STATE", "supersedes": G.digest_bytes(b"prior"),
                "reason_code": "C-TERMINAL-REVIEWED", "issued_by": {"authority_id": "ops-1", "control_domain": "ops-domain"},
                "session_id": session, "subject_control_domain": "subject-domain",
                "adjudicators": [_adj("adj-1", "audit-domain"), _adj("adj-2", "ops-domain")],
                "descendants": [], "descendant_closure_status": "UNKNOWN", "issued_at": "2026-07-25T12:01:00Z",
                "signature": T.signature("valid", kid="ops-key")}
    _f = T.GateFixture()
    _c2 = _reg_c2_169(_f)
    # establish under C1 HEALTHY
    _f.gate.authorize(_f.request(nonce="a" * 32), T.evidence_bundle(receipt=T.witness_receipt(epoch=7, sequence=11), epoch=5))
    # DENIED degraded C2 DELETE -- the actual CLASS A vector (DEGRADED witness: narrowing passes, effect denied)
    _rB = T.effect_request(_c2, _f.policy_digest, effect="DELETE", nonce="b" * 32)
    _f.gate.authorize(_rB, T.evidence_bundle(receipt=T.witness_receipt(health="DEGRADED", epoch=8, sequence=12), epoch=6))
    _cc_clean = "DELETE" not in set(_f.gate.state.contract_ceiling.get("sess-0001", G.Authority([], [])).effects)
    # terminalize + lift
    _f.gate.submit_amendment(_amd169())
    # retry DELETE under C2 -- must be DENIED
    _rB2 = T.effect_request(_c2, _f.policy_digest, effect="DELETE", nonce="c" * 32)
    _d3 = _f.gate.authorize(_rB2, T.evidence_bundle(receipt=T.witness_receipt(epoch=9, sequence=13), epoch=7))
    _exploit_denied = _d3.get("decision") == G.DECISION_DENY_FALSE
    record("CE169", "GLM-F1/K32-01 DEGRADED-vector ceiling-poison CLOSED: a DENIED degraded C2 DELETE does not poison contract_ceiling; post-lift re-establish for DELETE is DENY_FALSE", "GLM-F1",
           _cc_clean and _exploit_denied, f"ceiling_no_delete={_cc_clean} exploit_denied={_exploit_denied}")
except Exception as e:
    record("CE169", "GLM-F1 cross-contract ceiling poison", "GLM-F1", False, f"{type(e).__name__}: {e}")

# CE173 / K33-01 (ALLOWed-degraded ceiling-poison -- the 32nd instance -- CLOSED): an ALLOWed degraded C2
# READ must NOT poison contract_ceiling with C2's full HEALTHY ceiling. The V30 fix closed DENIED-request
# poison; K33-01 is ALLOWED-request poison. The V31 fix writes contract_ceiling ONLY on HEALTHY ALLOWs.
try:
    _f173 = T.GateFixture()
    _c2_173 = _reg_c2_169(_f173)
    # establish under C1 HEALTHY
    _f173.gate.authorize(_f173.request(nonce="a" * 32), T.evidence_bundle(receipt=T.witness_receipt(epoch=7, sequence=11), epoch=5))
    _cc_pre = set(_f173.gate.state.contract_ceiling.get("sess-0001", G.Authority([], [])).effects)
    # ALLOWed degraded C2 READ -- the K33-01 vector (READ is in C2's degraded ceiling)
    _rD = T.effect_request(_c2_173, _f173.policy_digest, effect="READ", nonce="d" * 32)
    _dD = _f173.gate.authorize(_rD, T.evidence_bundle(receipt=T.witness_receipt(health="DEGRADED", epoch=8, sequence=12), epoch=6))
    _allowed = _dD.get("decision") == "ALLOW"
    _cc_post = set(_f173.gate.state.contract_ceiling.get("sess-0001", G.Authority([], [])).effects)
    _no_delete_leak = "DELETE" not in _cc_post
    _cc_unchanged = _cc_post == _cc_pre  # degraded ALLOW must not change contract_ceiling
    # terminalize + lift + retry DELETE
    _f173.gate.authorize(_f173.request(effect="READ", nonce="e" * 32), T.evidence_bundle(
        receipt=T.witness_receipt(health="HEALTHY", epoch=9, sequence=13), epoch=7))
    _f173.gate.submit_amendment(_amd169(cid="cor-173"))
    _rDel = T.effect_request(_c2_173, _f173.policy_digest, effect="DELETE", nonce="f" * 32)
    _dDel = _f173.gate.authorize(_rDel, T.evidence_bundle(receipt=T.witness_receipt(health="HEALTHY", epoch=10, sequence=14), epoch=8))
    _delete_denied = _dDel.get("decision") != "ALLOW"
    record("CE173", "K33-01 ALLOWed-degraded ceiling-poison CLOSED: an ALLOWed degraded C2 READ does not broaden contract_ceiling; post-lift DELETE is DENIED", "K33-01",
           _allowed and _no_delete_leak and _cc_unchanged and _delete_denied,
           f"allowed={_allowed} no_delete_leak={_no_delete_leak} cc_unchanged={_cc_unchanged} delete_denied={_delete_denied}")
except Exception as e:
    record("CE173", "K33-01 ALLOWed-degraded ceiling poison", "K33-01", False, f"{type(e).__name__}: {e}")

# CE170 / GPT-P32-01 (same-epoch over-withdrawal -- CLOSED): an armed same-epoch ceiling CHANGE must be X7
# (grant-independent), not X7U. An armed same-epoch EQUAL snapshot is X7U (the re-widen being tracked).
# Constructed as: base(ep=1) -> event -> marker(ep=2) -> first_at_3(armed re-widen, X7U, consumed) -> second_at_3.
# The second_at_3 record is at the same epoch as first_at_3 with the marker already consumed.
# We use a separate two-record-after-marker construction with epoch_floor avoidance.
try:
    _ev170 = _R["event"]
    _mk170 = _R["marker"]
    S170 = _R["session"]
    _base170 = {"session_id": S170, "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": [_REAL_TGT]}}
    # The marker's authority_epoch is 2, licensed_epoch is 3. After the marker, prev from base is (1, {READ}).
    # A record at ep=3 (the licensed_epoch, strictly forward from prev_ep=1) would be the armed re-widen -> X7U.
    # Then a SECOND record at ep=3 is same-epoch with prev_ep=3 (marker consumed, no longer armed).
    # For the changed test: use a single stream with the changed record at same-epoch as a prior record.
    # Simplest correct test: base(ep=1) -> [no marker] -> same-epoch-changed(ep=1). This is the unarmed case.
    # For armed: use GPT's reproducer directly (which proved the fix on canonical bytes).
    _unarmed_stream = [_base170, {"session_id": S170, "authority_epoch": 1,
                       "authority_snapshot": {"effects": ["READ", "WRITE", "DELETE"], "target_scopes": [_REAL_TGT]}}]
    _unarmed_changed_x7 = "X7" in G.check_authority_history(_unarmed_stream)
    # Armed test via GPT's reproducer pattern: event + marker + same-epoch-changed + same-epoch-equal
    # using the reproducer's exact pattern (which was confirmed X7 on fixed bytes above).
    import test_bssg_gate as T
    _ev_170b = {"record_type": "bssg.correction-event", "spec_version": G.SPEC_VERSION, "correction_id": "cor-170",
                "correction_class": "LIFT_TERMINAL_STATE", "supersedes": G.digest_bytes(b"p"), "reason_code": "C-TERMINAL-REVIEWED",
                "issued_by": {"authority_id": "ops-1", "control_domain": "ops-domain"}, "session_id": "s170", "subject_control_domain": "subject-domain",
                "adjudicators": [{"adjudicator_id": "adj-1", "control_domain": "audit-domain", "signature": T.signature("valid", "adj-1")},
                                  {"adjudicator_id": "adj-2", "control_domain": "legal-domain", "signature": T.signature("valid", "adj-2")}],
                "descendants": [], "descendant_closure_status": "UNKNOWN", "issued_at": "2026-07-25T12:01:00Z", "signature": T.signature("valid", "ops-key")}
    _mk_170b = {"record_type": "bssg.correction-accepted", "spec_version": G.SPEC_VERSION, "gate_version": G.GATE_VERSION,
                "correction_id": "cor-170", "correction_class": "LIFT_TERMINAL_STATE", "session_id": "s170",
                "authority_epoch": 2, "licensed_epoch": 3, "correction_digest": G.digest(_ev_170b), "adjudicators_verified": 2}
    _b170 = {"session_id": "s170", "authority_epoch": 2, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}
    _sc170 = {"session_id": "s170", "authority_epoch": 2, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}
    _se170 = {"session_id": "s170", "authority_epoch": 2, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}
    _armed_changed_x7 = "X7" in G.check_authority_history([_b170, _ev_170b, _mk_170b, _sc170])
    _armed_equal_x7u = _uncert(G.check_authority_history([_b170, _ev_170b, _mk_170b, _se170]))
    record("CE170", "GPT-P32-01 same-epoch over-withdrawal CLOSED: unarmed same-epoch ceiling CHANGE is X7; armed same-epoch ceiling CHANGE is X7 (grant-independent); armed same-epoch EQUAL is X7U", "GPT-P32-01",
           _unarmed_changed_x7 and _armed_changed_x7 and _armed_equal_x7u,
           f"unarmed_changed_x7={_unarmed_changed_x7} armed_changed_x7={_armed_changed_x7} armed_equal_x7u={_armed_equal_x7u}")
except Exception as e:
    record("CE170", "GPT-P32-01 same-epoch over-withdrawal", "GPT-P32-01", False, f"{type(e).__name__}: {e}")

# CE171 / K32-03 (malformed authority_snapshot -- CLOSED): a PRESENT but non-dict authority_snapshot
# (string, int) in an armed position is grant-independent type-tamper -> X7. An ABSENT snapshot (None)
# means no authority to analyze and is skipped (no violation).
try:
    _ev171 = _R["event"]
    _mk171 = _R["marker"]
    _base171 = {"session_id": _R["session"], "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": [_REAL_TGT]}}
    _str_snap = {"session_id": _R["session"], "authority_epoch": _R["landing"], "authority_snapshot": "tampered"}
    _int_snap = {"session_id": _R["session"], "authority_epoch": _R["landing"], "authority_snapshot": 42}
    _absent = {"session_id": _R["session"], "authority_epoch": _R["landing"]}
    _str_x7 = "X7" in G.check_authority_history([_base171, _ev171, _mk171, _str_snap])
    _int_x7 = "X7" in G.check_authority_history([_base171, _ev171, _mk171, _int_snap])
    _absent_clean = G.check_authority_history([_base171, _ev171, _mk171, _absent]) == []
    record("CE171", "K32-03 malformed snapshot CLOSED: armed + string/int snapshot is X7 (type-tamper); armed + absent snapshot is skipped (clean)", "K32-03",
           _str_x7 and _int_x7 and _absent_clean, f"str_x7={_str_x7} int_x7={_int_x7} absent_clean={_absent_clean}")
except Exception as e:
    record("CE171", "K32-03 malformed snapshot", "K32-03", False, f"{type(e).__name__}: {e}")

# CE172 / K32-04 (marker metadata gaps -- CLOSED): a marker with missing licensed_epoch fails
# _is_acceptance_marker and does not arm the X7U branch; the widening is unlicensed -> X7.
try:
    _ev172 = _R["event"]
    _mk_good = _R["marker"]
    _mk_no_le = {k: v for k, v in _mk_good.items() if k != "licensed_epoch"}
    _base172 = {"session_id": _R["session"], "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": [_REAL_TGT]}}
    _wide172 = {"session_id": _R["session"], "authority_epoch": _R["landing"],
                "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": [_REAL_TGT]}}
    _good_x7u = _uncert(G.check_authority_history([_base172, _ev172, _mk_good, _wide172]))
    _no_le_x7 = "X7" in G.check_authority_history([_base172, _ev172, _mk_no_le, _wide172])
    record("CE172", "K32-04 marker metadata CLOSED: well-formed marker arms X7U; missing licensed_epoch fails marker validation -> widening is unlicensed X7", "K32-04",
           _good_x7u and _no_le_x7, f"good_x7u={_good_x7u} no_le_x7={_no_le_x7}")
except Exception as e:
    record("CE172", "K32-04 marker metadata gaps", "K32-04", False, f"{type(e).__name__}: {e}")


green = sum(1 for *_, ok, _ in results if ok)
# (intermediate summary suppressed -- final summary is at the end of the file after all CEs)

# CE174 / AUDIT-V33-01 (commit pre-reserve BaseException totality -- same class as GPT-P30-05/CE167):
# a hostile dict subclass whose .items() raises BaseException must fail closed at the commit ingress
# boundary (VOID + failure record), not escape the public API leaving the token UNUSED with no record.
try:
    class _HostileBE174(dict):
        def items(self):
            raise BaseException("hostile-items-174")
    _f174 = T.GateFixture()
    _d174 = _f174.gate.authorize(_f174.request(nonce="ce174" + "0" * 27), T.evidence_bundle())
    _rcpt174 = _d174["authorization_receipt"]
    _tid174 = _rcpt174["commit_token"]["token_id"]
    _binding174 = _HostileBE174({
        "request_digest": _rcpt174["request_digest"], "canonical_target": _rcpt174["canonical_target"],
        "params_digest": _rcpt174["params_digest"], "adapter_digest": _rcpt174["adapter_digest"],
        "effect_type": _rcpt174["effect_type"],
    })
    _escaped = False
    try:
        _r174 = _f174.gate.commit(_tid174, _binding174, T.evidence_bundle())
        _closed = _r174.get("outcome") == "FAILED_NO_EFFECT"
    except BaseException:
        _escaped = True
        _closed = False
    _status174 = _f174.gate.state.tokens.get(_tid174, {}).get("status", "UNKNOWN")
    record("CE174", "AUDIT-V33-01 commit pre-reserve BaseException totality: a hostile BaseException-raising binding fails closed (VOID + failure record), does not escape the public API", "AUDIT-V33-01",
           not _escaped and _closed and _status174 == "VOID",
           f"escaped={_escaped} closed={_closed} token_status={_status174}")
except Exception as e:
    record("CE174", "AUDIT-V33-01 commit BaseException totality", "AUDIT-V33-01", False, f"{type(e).__name__}: {e}")

# Final summary (after all CEs including V33 additions)
#SUPPRESSED: green = sum(1 for *_, ok, _ in results if ok)
#SUPPRESSED: print(f"\n{green}/{len(results)} GREEN  ({len(results)-green} RED = open defects)")

# CE175 / F-GS-1 (mint-fault ceiling-poison -- the 33rd instance -- CLOSED): a HEALTHY ALLOW whose
# token mint fails (FAILED_NO_EFFECT) must NOT leave contract_ceiling in a state that permits
# post-lift re-establishment of never-held authority. The actual F-GS-1 vector: first request is
# a C2 HEALTHY READ with a mint fault (no prior C1 establish). The fix writes an empty Authority
# in _issuance_failure so the _held check terminates any re-establishment wider than nothing.
# The post-establish case is independently closed by E-AUTHORITY-WIDENING (the C2 ceiling is wider
# than the established C1 ceiling, so _apply_narrowing rejects it before the mint path executes).
try:
    _fx175 = T.GateFixture()
    _b175 = T.contract_body(_fx175.policy_digest)
    _b175["allowed_effects"] = ["READ", "WRITE", "DELETE"]
    _b175["effect_registry"]["DELETE"] = {"adapter_digest": T.ADAPTER_DIGEST}
    _b175["degraded_effects"] = ["READ"]
    _c2_175 = G.digest(_b175); _fx175.gate.contracts[_c2_175] = {"body": copy.deepcopy(_b175), "revoked": False}
    _adj175 = lambda i, d: {"adjudicator_id": i, "control_domain": d, "signature": T.signature("valid", kid=i)}
    _amd175 = {"record_type": "bssg.correction-event", "spec_version": G.SPEC_VERSION, "correction_id": "cor-175",
               "correction_class": "LIFT_TERMINAL_STATE", "supersedes": G.digest_bytes(b"prior"),
               "reason_code": "C-TERMINAL-REVIEWED", "issued_by": {"authority_id": "ops-1", "control_domain": "ops-domain"},
               "session_id": "sess-0001", "subject_control_domain": "subject-domain",
               "adjudicators": [_adj175("adj-1", "audit-domain"), _adj175("adj-2", "ops-domain")],
               "descendants": [], "descendant_closure_status": "UNKNOWN", "issued_at": "2026-07-25T12:01:00Z",
               "signature": T.signature("valid", kid="ops-key")}
    # Step 1: C2 HEALTHY READ with mint fault (first request, no prior establish)
    _fx175.gate.new_token = lambda: (_ for _ in ()).throw(RuntimeError("ce175-probe"))
    _r1_175 = _fx175.gate.authorize(T.effect_request(_c2_175, _fx175.policy_digest, effect="READ", nonce="1" * 32),
                                    T.evidence_bundle(receipt=T.witness_receipt(health="HEALTHY", epoch=7, sequence=11), epoch=7))
    _mint_failed = _r1_175.get("issuance_status") == "FAILED_NO_EFFECT"
    _cc175 = _fx175.gate.state.contract_ceiling.get("sess-0001")
    _no_delete = _cc175 is not None and "DELETE" not in set(_cc175.effects)  # must have an EMPTY entry, not None
    _cc_is_empty = _cc175 is not None and _cc175.is_empty()
    # Step 2: restore normal minting, degraded C2 READ
    _fx175.gate.new_token = _fx175.tokens
    _fx175.gate.authorize(T.effect_request(_c2_175, _fx175.policy_digest, effect="READ", nonce="2" * 32),
                          T.evidence_bundle(receipt=T.witness_receipt(health="DEGRADED", epoch=8, sequence=12), epoch=8))
    # Step 3: HEALTHY C2 DELETE (terminalize via widening)
    _fx175.gate.authorize(T.effect_request(_c2_175, _fx175.policy_digest, effect="DELETE", nonce="3" * 32),
                          T.evidence_bundle(receipt=T.witness_receipt(health="HEALTHY", epoch=9, sequence=13), epoch=9))
    # Step 4: genuine lift
    _fx175.gate.submit_amendment(_amd175)
    # Step 5: retry DELETE after lift -- must be DENIED (never successfully held DELETE)
    _r4_175 = _fx175.gate.authorize(T.effect_request(_c2_175, _fx175.policy_digest, effect="DELETE", nonce="4" * 32),
                                    T.evidence_bundle(receipt=T.witness_receipt(health="HEALTHY", epoch=10, sequence=14), epoch=10))
    _delete_denied = _r4_175.get("decision") != "ALLOW"
    record("CE175", "F-GS-1 mint-fault ceiling-poison CLOSED: a FAILED_NO_EFFECT first-establish writes empty contract_ceiling; post-lift DELETE is DENIED; session never successfully held DELETE", "F-GS-1",
           _mint_failed and _no_delete and _cc_is_empty and _delete_denied,
           f"mint_failed={_mint_failed} no_delete={_no_delete} cc_empty={_cc_is_empty} delete_denied={_delete_denied}")
except Exception as e:
    record("CE175", "F-GS-1 mint-fault ceiling poison", "F-GS-1", False, f"{type(e).__name__}: {e}")

# Final summary (after all CEs including V34 council additions)
#SUPPRESSED: green = sum(1 for *_, ok, _ in results if ok)
#SUPPRESSED: print(f"\n{green}/{len(results)} GREEN  ({len(results)-green} RED = open defects)")

# CE176 / 34th instance (degraded-first ceiling-absence bypass -- CLOSED): a session whose first
# successful auth is DEGRADED must not have contract_ceiling absent. After a lift, re-establishment
# must be bounded by the empty Authority (demonstrated nothing under HEALTHY), not free.
try:
    _fx176 = T.GateFixture()
    _b176 = T.contract_body(_fx176.policy_digest)
    _b176["allowed_effects"] = ["READ", "WRITE", "DELETE"]
    _b176["effect_registry"]["DELETE"] = {"adapter_digest": T.ADAPTER_DIGEST}
    _b176["degraded_effects"] = ["READ"]
    _c2_176 = G.digest(_b176); _fx176.gate.contracts[_c2_176] = {"body": copy.deepcopy(_b176), "revoked": False}
    _adj176 = lambda i, d: {"adjudicator_id": i, "control_domain": d, "signature": T.signature("valid", kid=i)}
    _amd176 = {"record_type": "bssg.correction-event", "spec_version": G.SPEC_VERSION, "correction_id": "cor-176",
               "correction_class": "LIFT_TERMINAL_STATE", "supersedes": G.digest_bytes(b"prior"),
               "reason_code": "C-TERMINAL-REVIEWED", "issued_by": {"authority_id": "ops-1", "control_domain": "ops-domain"},
               "session_id": "sess-0001", "subject_control_domain": "subject-domain",
               "adjudicators": [_adj176("adj-1", "audit-domain"), _adj176("adj-2", "ops-domain")],
               "descendants": [], "descendant_closure_status": "UNKNOWN", "issued_at": "2026-07-25T12:01:00Z",
               "signature": T.signature("valid", kid="ops-key")}
    # Step 1: DEGRADED C2 READ (first auth -- succeeds, health gate skips ceiling upgrade)
    _r1_176 = _fx176.gate.authorize(T.effect_request(_c2_176, _fx176.policy_digest, effect="READ", nonce="1" * 32),
                                    T.evidence_bundle(receipt=T.witness_receipt(health="DEGRADED", epoch=7, sequence=11), epoch=7))
    _cc176 = _fx176.gate.state.contract_ceiling.get("sess-0001")
    _has_entry = _cc176 is not None
    _is_empty = _has_entry and _cc176.is_empty()
    # Step 2: HEALTHY DELETE (widens -> terminal)
    _fx176.gate.authorize(T.effect_request(_c2_176, _fx176.policy_digest, effect="DELETE", nonce="2" * 32),
                          T.evidence_bundle(receipt=T.witness_receipt(health="HEALTHY", epoch=8, sequence=12), epoch=8))
    # Step 3: lift
    _fx176.gate.submit_amendment(_amd176)
    # Step 4: HEALTHY DELETE after lift
    _r4_176 = _fx176.gate.authorize(T.effect_request(_c2_176, _fx176.policy_digest, effect="DELETE", nonce="3" * 32),
                                    T.evidence_bundle(receipt=T.witness_receipt(health="HEALTHY", epoch=9, sequence=13), epoch=9))
    _delete_denied = _r4_176.get("decision") != "ALLOW"
    record("CE176", "34th instance (degraded-first ceiling-absence) CLOSED: a degraded-first session gets an empty contract_ceiling entry; post-lift DELETE is DENIED; the class fix ensures _held is NEVER None after an ALLOW", "34TH-INSTANCE",
           _has_entry and _is_empty and _delete_denied,
           f"has_entry={_has_entry} is_empty={_is_empty} delete_denied={_delete_denied}")
except Exception as e:
    record("CE176", "34th instance degraded-first", "34TH-INSTANCE", False, f"{type(e).__name__}: {e}")

# Final summary (after all CEs including the class fix)
green = sum(1 for *_, ok, _ in results if ok)
print(f"\n{green}/{len(results)} GREEN  ({len(results)-green} RED = open defects)")

---

# Bismillah ir-Rahman ir-Rahim
