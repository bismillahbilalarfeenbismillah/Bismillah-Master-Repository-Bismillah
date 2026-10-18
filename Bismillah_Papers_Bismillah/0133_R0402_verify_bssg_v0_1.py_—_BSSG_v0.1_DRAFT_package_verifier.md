# Bismillah ir-Rahman ir-Rahim

# R0402 -- verify_bssg_v0_1.py — BSSG v0.1 DRAFT package verifier.

**Chronological Index:** 133 of 995  
**Date:** 2026  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** verify_bssg_v0_1.py  
**Source Format:** py  
**SHA-256:** `d16bbe7cbf506e7bdf0d3c0b0954aa309250ff0cffbbaecfceb2559ae5b50ef3`  

---

## R0402 · verify_bssg_v0_1.py — BSSG v0.1 DRAFT package verifier.

- section: V. BSSG & SHVVP Protocols
- source_file: verify_bssg_v0_1.py
- source_format: py
- merged_variants: 15 (verify_bssg_v0_1.py; verify_bssg_v0_1.py.txt)
- text_sha256: d16bbe7cbf506e7bdf0d3c0b0954aa309250ff0cffbbaecfceb2559ae5b50ef3

#!/usr/bin/env python3
"""
BSSG v0.1 DRAFT package verifier.

Runs twelve gates over the package directory it lives in:

  G1  file parity and required-file presence
  G2  JSON Schema 2020-12 validity and closure discipline for the six schemas
  G3  test suite execution
  G4  citation URL extraction sanity (every cited URL must appear in the
      specification's reference list; no invented hosts)
  G5  prohibited effectiveness-language scan
  G6  normative-term scan (BCP 14 boilerplate and uppercase usage)
  G7  dash scan (no em dash or en dash characters in source files)
  G8  version and status parity
  G9  SHA-256 manifest check against SHA256SUMS
  G10 unresolved open-decision report
  G11 X4/X7/X8 mechanical-checker exercise (negative + positive vectors, real
      gate-record binding, and tamper-detection against vacuity)
  G12 claim-substrate consistency (load-bearing REPAIR_STATUS claims re-verified
      against runtime behavior; every cited counterexample id must exist)

Exit status is 0 when no gate FAILS. WARN does not fail the package: an
unresolved design decision is an honest state, an inconsistent package is not.

This verifier makes no claim about the effectiveness, security, or correctness
of anything it verifies. It checks package self-consistency only.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys

# V27 breadth-bound: a wide-holding record (epoch 0) = the pre-degradation authority a realistic honest
# recovery restores to. Prepending it to a synthetic honest re-widen makes the stream a non-fragment.
_HELD = {"session_id": "s", "authority_epoch": 0, "authority_snapshot": {"effects": ["READ", "WRITE", "DELETE"], "target_scopes": ["a"]}}

HERE = os.path.dirname(os.path.abspath(__file__))
SPEC = "BSSG_v0_1_CANONICAL_SPEC_DRAFT.pplx.md"
SCHEMA_DIR = os.path.join(HERE, "schemas")

REQUIRED_FILES = [
    SPEC,
    "BSSG_v0_1_MODEL_COUNCIL_SYNTHESIS.pplx.md",
    "BSSG_v0_1_DECISION_REGISTER.md",
    "README.md",
    "REQUIREMENTS_TRACEABILITY.md",
    "ATTACK_AND_FALSIFIER_REGISTER.md",
    "OPEN_DECISIONS.md",
    "bssg_gate.py",
    "test_bssg_gate.py",
    "verify_bssg_v0_1.py",
]

REQUIRED_SCHEMAS = [
    "effect-request.schema.json",
    "authorization-receipt.schema.json",
    "witness-receipt.schema.json",
    "execution-receipt.schema.json",
    "correction-event.schema.json",
    "lineage-record.schema.json",
]

# Phrases that may not appear outside the registry. Lines carrying the marker
# token below are skipped by the scanner, including these very lines.
PROHIBITED_PATTERNS = [
    r"prevents harm",  # prohibited-phrase-registry
    r"makes agents safe",  # prohibited-phrase-registry
    r"reduces unauthorized effects",  # prohibited-phrase-registry
    r"outperform",  # prohibited-phrase-registry
    r"proven secure",  # prohibited-phrase-registry
    r"guarantees safety",  # prohibited-phrase-registry
    r"is validated",  # prohibited-phrase-registry
    r"prevents equivocation",  # prohibited-phrase-registry
    r"preserves capability(?! under evidence)",  # prohibition #8: BARE form only (conditional allowed)
    r"guarantees security",  # prohibited-phrase-registry
    r"guarantees correctness",  # prohibited-phrase-registry
    r"guarantees safe",  # prohibited-phrase-registry (broadened beyond 'guarantees safety')
    r"\bis safe\b",  # prohibited-phrase-registry (unqualified affirmative safety claim; negated disclaimers reworded)
    r"tolerates witness failure",  # prohibited-phrase-registry
    r"state of the art",  # prohibited-phrase-registry
    r"industry leading",  # prohibited-phrase-registry
    r"battle tested",  # prohibited-phrase-registry
    r"production ready",  # prohibited-phrase-registry
]
SKIP_MARKER = "prohibited-phrase-registry"
# Audit / producer meta-documents legitimately NAME the prohibited phrases while recording
# findings; the Section 1.3 prohibition targets BSSG documents, README, and the deposit
# abstract, not the audit trail. G5 exempts these from the effectiveness-language scan.
AUDIT_META = (
    "DECISION_REGISTER", "MODEL_COUNCIL_SYNTHESIS", "PRODUCER", "ATTACK_AND_FALSIFIER",
    "REQUIREMENTS_TRACEABILITY", "OPEN_DECISIONS", "REPAIR_STATUS",
    "bssg_counterexamples", "bssg_model_check", "verify_bssg",
)

NORMATIVE_TERMS = [
    "MUST NOT",
    "MUST",
    "SHALL NOT",
    "SHALL",
    "SHOULD NOT",
    "SHOULD",
    "REQUIRED",
    "RECOMMENDED",
    "MAY",
    "OPTIONAL",
]

DASHES = {
    "\u2013": "en dash",
    "\u2014": "em dash",
    "\u2012": "figure dash",
    "\u2015": "horizontal bar",
    "\u2212": "minus sign",
}

MD_LINK_RE = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+)\)")
BARE_URL_RE = re.compile(r"(?<![(\w])(https?://[^\s`\"'<>)\]]+)")

results = []


def record(gate, status, message):
    results.append((gate, status, message))
    print("%-5s %-6s %s" % (gate, status, message))


# Dispatch/transport wrappers are not packet content; the verifier ignores them so it
# runs cleanly whether or not an audit brief or reconstruction helper travels alongside.
DISPATCH_ARTIFACTS = ("AUDIT_BRIEF", "reconstruct.py", "PRODUCER_KEPT")

def source_files():
    out = []
    for root, dirs, files in os.walk(HERE):
        dirs[:] = [d for d in dirs if d not in ("__pycache__", ".git")]
        for name in files:
            if not name.endswith((".md", ".py", ".json")):
                continue
            if name.startswith("schema__") or any(a in name for a in DISPATCH_ARTIFACTS):
                continue
            out.append(os.path.join(root, name))
    return sorted(out)


def read(path):
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


# ---------------------------------------------------------------------------
# G1 file parity
# ---------------------------------------------------------------------------


def gate_g1():
    missing = [f for f in REQUIRED_FILES if not os.path.isfile(os.path.join(HERE, f))]
    for schema in REQUIRED_SCHEMAS:
        if not os.path.isfile(os.path.join(SCHEMA_DIR, schema)):
            missing.append("schemas/" + schema)
    if missing:
        record("G1", "FAIL", "missing required files: %s" % ", ".join(missing))
        return
    present = sorted(os.listdir(SCHEMA_DIR))
    extra = [f for f in present if f not in REQUIRED_SCHEMAS]
    if extra:
        record("G1", "FAIL", "unexpected files in schemas/: %s" % ", ".join(extra))
        return
    record(
        "G1",
        "PASS",
        "all %d required files and exactly %d schemas present"
        % (len(REQUIRED_FILES), len(REQUIRED_SCHEMAS)),
    )


# ---------------------------------------------------------------------------
# G2 schema validity
# ---------------------------------------------------------------------------


def gate_g2():
    try:
        import jsonschema
    except Exception:
        record("G2", "WARN", "jsonschema not installed; structural check only")
        jsonschema = None
    problems = []
    for name in REQUIRED_SCHEMAS:
        path = os.path.join(SCHEMA_DIR, name)
        try:
            schema = json.loads(read(path))
        except Exception as exc:
            problems.append("%s: not parseable (%s)" % (name, exc))
            continue
        if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            problems.append("%s: $schema is not the 2020-12 dialect" % name)
        schema_id = schema.get("$id", "")
        if not schema_id.startswith("urn:bssg:schema:0.1:"):
            problems.append("%s: $id is not a urn:bssg:schema:0.1 identifier" % name)
        if schema.get("additionalProperties") is not False:
            problems.append("%s: root object is not closed" % name)
        if "DRAFT" not in json.dumps(schema):
            problems.append("%s: no DRAFT status marker in the description" % name)
        if jsonschema is not None:
            try:
                jsonschema.Draft202012Validator.check_schema(schema)
            except Exception as exc:
                problems.append("%s: invalid schema (%s)" % (name, exc))
    # the frozen kernel must not gain a sixth conjunct
    auth = json.loads(read(os.path.join(SCHEMA_DIR, "authorization-receipt.schema.json")))
    conjuncts = auth["$defs"]["conjuncts"]["properties"]
    expected = {
        "ContractMatch",
        "EffectTypeValid",
        "TargetAllowed",
        "WitnessHealthy",
        "EvidenceCurrent",
    }
    if set(conjuncts) != expected:
        problems.append("authorization-receipt: conjunct set is not the frozen five")
    if problems:
        record("G2", "FAIL", "; ".join(problems))
    else:
        record("G2", "PASS", "six schemas valid, closed, DRAFT-marked, five conjuncts")


# ---------------------------------------------------------------------------
# G3 tests
# ---------------------------------------------------------------------------


def gate_g3():
    proc = subprocess.run(
        [sys.executable, "-m", "unittest", "test_bssg_gate", "-v"],
        cwd=HERE,
        capture_output=True,
        text=True,
    )
    output = proc.stdout + proc.stderr
    match = re.search(r"Ran (\d+) tests", output)
    count = int(match.group(1)) if match else -1
    kernel = len(set(re.findall(r"test_kernel_\d{3}_[TFU_]+", output)))
    if proc.returncode != 0:
        tail = output.strip().splitlines()[-15:]
        record("G3", "FAIL", "tests failed (%d run): %s" % (count, " | ".join(tail)))
        return
    if kernel < 243:
        record("G3", "FAIL", "kernel truth states enumerated: %d, expected 243" % kernel)
        return
    record("G3", "PASS", "%d tests passed, including %d kernel truth states" % (count, kernel))
    return count


# ---------------------------------------------------------------------------
# G4 citation sanity
# ---------------------------------------------------------------------------


def gate_g4():
    spec_text = read(os.path.join(HERE, SPEC))
    refs_section = spec_text.split("## 32. References", 1)
    if len(refs_section) != 2:
        record("G4", "FAIL", "specification has no reference section")
        return
    allow = set(BARE_URL_RE.findall(refs_section[1]))
    allow.add("https://json-schema.org/draft/2020-12/schema")
    if not allow:
        record("G4", "FAIL", "reference section contains no URLs")
        return
    problems = []
    total = 0
    for path in source_files():
        if not path.endswith(".md"):
            continue
        text = read(path)
        if path.endswith(SPEC):
            text = text.split("## 32. References", 1)[0]
        urls = set(MD_LINK_RE.findall(text)) | set(BARE_URL_RE.findall(text))
        for url in urls:
            total += 1
            clean = url.rstrip(".,;:")
            if clean not in allow:
                problems.append("%s cites unlisted URL %s" % (os.path.basename(path), clean))
    bad_shape = [u for u in allow if " " in u or u.count("://") != 1]
    if bad_shape:
        problems.append("malformed reference URLs: %s" % bad_shape)
    if problems:
        record("G4", "FAIL", "; ".join(sorted(set(problems))[:10]))
    else:
        record(
            "G4",
            "PASS",
            "%d citation occurrences, all resolvable to the %d listed references"
            % (total, len(allow)),
        )


# ---------------------------------------------------------------------------
# G5 prohibited language
# ---------------------------------------------------------------------------


def gate_g5():
    hits = []
    for path in source_files():
        if any(m in os.path.basename(path) for m in AUDIT_META):
            continue  # meta-docs discuss the prohibited terms; they do not assert them
        for number, line in enumerate(read(path).splitlines(), 1):
            if SKIP_MARKER in line.lower():
                continue
            if "PROHIBITED-PHRASE-REGISTRY" in line:
                continue
            lowered = line.lower()
            for pattern in PROHIBITED_PATTERNS:
                if re.search(pattern, lowered):
                    hits.append("%s:%d %s" % (os.path.basename(path), number, pattern))
    if hits:
        record("G5", "FAIL", "prohibited effectiveness language: %s" % "; ".join(hits[:10]))
    else:
        record("G5", "PASS", "no prohibited effectiveness language outside the registry")


# ---------------------------------------------------------------------------
# G6 normative terms
# ---------------------------------------------------------------------------


def gate_g6():
    spec_text = read(os.path.join(HERE, SPEC))
    problems = []
    if "RFC 2119" not in spec_text or "RFC 8174" not in spec_text:
        problems.append("BCP 14 boilerplate does not cite both RFC 2119 and RFC 8174")
    if "when, and only when, they appear in all capitals" not in spec_text:
        problems.append("BCP 14 capitalization clause missing")
    counts = {}
    for term in NORMATIVE_TERMS:
        counts[term] = len(re.findall(r"\b%s\b" % term, spec_text))
    for term in ("MUST", "MUST NOT", "SHALL", "SHOULD", "MAY"):
        if counts[term] == 0:
            problems.append("normative term %s never used" % term)
    ambiguous = re.findall(r"\b(Must|Shall|Should|May not)\b\s+(?:be|not|have)", spec_text)
    _counts = ("BCP 14 boilerplate present; MUST=%d MUST NOT=%d SHALL=%d SHOULD=%d MAY=%d"
               % (counts["MUST"], counts["MUST NOT"], counts["SHALL"], counts["SHOULD"], counts["MAY"]))
    if problems:
        record("G6", "FAIL", "; ".join(problems))
    elif ambiguous:
        record("G6", "WARN", "mixed-case normative-looking terms: %s; %s" % (set(ambiguous), _counts))
    else:
        record("G6", "PASS", _counts)


# ---------------------------------------------------------------------------
# G7 dashes
# ---------------------------------------------------------------------------


def gate_g7():
    hits = []
    for path in source_files():
        text = read(path)
        for char, label in DASHES.items():
            if char in text:
                index = text.index(char)
                hits.append("%s contains %s at offset %d" % (os.path.basename(path), label, index))
    if hits:
        record("G7", "FAIL", "; ".join(hits[:10]))
    else:
        record("G7", "PASS", "no em dash, en dash, or related characters in source files")


# ---------------------------------------------------------------------------
# G8 version and status parity
# ---------------------------------------------------------------------------


def gate_g8():
    problems = []
    gate_src = read(os.path.join(HERE, "bssg_gate.py"))
    if 'SPEC_VERSION = "0.1"' not in gate_src:
        problems.append("bssg_gate.py SPEC_VERSION is not 0.1")
    for name in REQUIRED_SCHEMAS:
        schema = json.loads(read(os.path.join(SCHEMA_DIR, name)))
        blob = json.dumps(schema)
        if '"const": "0.1"' not in blob and "urn:bssg:schema:0.1:" not in blob:
            problems.append("%s does not pin spec version 0.1" % name)
    for name in REQUIRED_FILES:
        if not name.endswith(".md"):
            continue
        text = read(os.path.join(HERE, name))
        if "DRAFT" not in text:
            problems.append("%s does not carry a DRAFT marker" % name)
        if "NOT CARRIED" not in text:
            problems.append("%s does not carry a NOT CARRIED marker" % name)
    spec_text = read(os.path.join(HERE, SPEC))
    for phrase in (
        "NOT PUBLICATION-READY",
        "Bilal Syed Arfeen",
        "HALT-WITH-FINDINGS",
        "CONDITIONAL APPROVAL",
    ):
        if phrase not in spec_text:
            problems.append("specification is missing required phrase: %s" % phrase)
    if "council approved" in spec_text.lower() or "approved by the council" in spec_text.lower():
        problems.append("specification claims council approval")
    if problems:
        record("G8", "FAIL", "; ".join(problems))
    else:
        record("G8", "PASS", "version 0.1 parity and DRAFT / NOT CARRIED status intact")


# ---------------------------------------------------------------------------
# G9 manifest
# ---------------------------------------------------------------------------


def gate_g9():
    manifest_path = os.path.join(HERE, "SHA256SUMS")
    if not os.path.isfile(manifest_path):
        record("G9", "WARN", "SHA256SUMS absent; run before packaging")
        return
    problems = []
    listed = set()
    for line in read(manifest_path).splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(None, 1)
        if len(parts) != 2:
            problems.append("malformed manifest line: %s" % line)
            continue
        expected, name = parts[0], parts[1].lstrip("*").strip()
        listed.add(name)
        path = os.path.join(HERE, name)
        if not os.path.isfile(path):
            problems.append("manifest lists missing file %s" % name)
            continue
        with open(path, "rb") as handle:
            actual = hashlib.sha256(handle.read()).hexdigest()
        if actual != expected:
            problems.append("digest mismatch for %s" % name)
    on_disk = set()
    for path in source_files():
        on_disk.add(os.path.relpath(path, HERE))
    unlisted = sorted(on_disk - listed)
    if unlisted:
        problems.append("files present but not in the manifest: %s" % ", ".join(unlisted))
    if problems:
        record("G9", "FAIL", "; ".join(problems[:10]))
    else:
        record("G9", "PASS", "SHA256SUMS verified for %d files" % len(listed))


# ---------------------------------------------------------------------------
# G10 open decisions
# ---------------------------------------------------------------------------


def gate_g10():
    text = read(os.path.join(HERE, "OPEN_DECISIONS.md"))
    ods = sorted(set(re.findall(r"\bOD-(\d+)\b", text)), key=int)
    register = read(os.path.join(HERE, "BSSG_v0_1_DECISION_REGISTER.md"))
    blocking = "STILL BLOCKING" in register
    message = "%d open design decisions (%s)" % (
        len(ods),
        ", ".join("OD-" + o for o in ods),
    )
    if blocking:
        message += "; decision register records STILL BLOCKING findings"
    record("G10", "WARN", message)

def gate_g11():
    """G11: the X4/X7/X8 mechanical checkers detect their negative vectors, pass their positive vectors,
    AND bind the REAL gate record stream -- including tamper-detection so the gate catches an
    UNDER-flagging / vacuous checker (K18-11), not only an over-flagging one."""
    import bssg_gate as _BG
    import test_bssg_gate as _T11
    import copy as _cp
    _kc = list(_BG.KERNEL_CONJUNCTS)
    _x8_clean = _BG.check_allow_receipt({"decision": "ALLOW", "conjuncts": {k: "TRUE" for k in _kc}, "reason_codes": []})
    _x8_forged = _BG.check_allow_receipt({"decision": "ALLOW", "conjuncts": {**{k: "TRUE" for k in _kc}, "EvidenceCurrent": "UNKNOWN"}, "reason_codes": ["E-FORGED-X8"]})
    _x8_absent = _BG.check_allow_receipt({"decision": "ALLOW", "conjuncts": {k: "TRUE" for k in _kc}})
    _x7_bad = _BG.check_authority_history([{"session_id": "s", "authority_epoch": 2, "authority_snapshot": {"effects": ["READ"], "target_scopes": []}}, {"session_id": "s", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": []}}])
    _x7_same_epoch = _BG.check_authority_history([{"session_id": "s", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}, {"session_id": "s", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}])
    _x4_bad = _BG.check_single_redemption([{"commit_token_id": "t1", "outcome": "COMMITTED_PENDING_OUTCOME"}, {"commit_token_id": "t1", "outcome": "COMMITTED_PENDING_OUTCOME"}])
    _x4_dbl_succeeded = _BG.check_single_redemption([{"commit_token_id": "t1", "outcome": "SUCCEEDED"}, {"commit_token_id": "t1", "outcome": "SUCCEEDED"}])
    _x4_settle_chain = _BG.check_single_redemption([{"commit_token_id": "t1", "outcome": "COMMITTED_PENDING_OUTCOME"}, {"commit_token_id": "t1", "outcome": "SUCCEEDED"}])
    _x4_fail_then_success = _BG.check_single_redemption([{"commit_token_id": "t1", "outcome": "COMMITTED_PENDING_OUTCOME"}, {"commit_token_id": "t1", "outcome": "FAILED_NO_EFFECT"}, {"commit_token_id": "t1", "outcome": "SUCCEEDED"}])

    # -- REAL record stream: authorize + commit (+ double-spend) + a DEGRADED narrowing.
    _f = _T11.GateFixture()
    _a1 = _f.gate.authorize(_f.request(nonce="1" * 32), _T11.evidence_bundle())
    _rc = _a1["authorization_receipt"]
    _b = {k: _rc[k] for k in ("request_digest", "canonical_target", "params_digest", "adapter_digest", "effect_type")}
    _f.gate.commit(_rc["commit_token"]["token_id"], _b, {})
    _f.gate.commit(_rc["commit_token"]["token_id"], _b, {})  # double-spend -> FAILED_NO_EFFECT
    _f.gate.authorize(_f.request(nonce="2" * 32), _T11.evidence_bundle(receipt=_T11.witness_receipt(health="DEGRADED", epoch=9)))
    _real = _f.gate.state.records
    _execs = [r for r in _real if r.get("record_type") == "bssg.execution-receipt"]

    _x7_real = _BG.check_authority_history(_real)                 # conformant real stream -> []
    _x4_real = _BG.check_single_redemption(_execs)                # one redemption + a failed retry -> []

    # -- V29 (Strategy B): a real AUTHENTICATED grant, driven inline, so the amend POSITIVE control is anchored
    # (a marker-licensed re-widen is clean ONLY with the grant; the identical stream is X7 unanchored).
    _adjg = lambda i, d: {"adjudicator_id": i, "control_domain": d, "signature": _T11.signature("valid", kid=i)}
    _amd = {"record_type": "bssg.correction-event", "spec_version": _BG.SPEC_VERSION, "correction_id": "cor-g11r",
            "correction_class": "LIFT_TERMINAL_STATE", "supersedes": _BG.digest_bytes(b"prior-decision"),
            "reason_code": "C-TERMINAL-REVIEWED", "issued_by": {"authority_id": "ops-1", "control_domain": "ops-domain"},
            "session_id": "sess-0001", "subject_control_domain": "subject-domain",
            "adjudicators": [_adjg("adj-1", "audit-domain"), _adjg("adj-2", "ops-domain")],
            "descendants": [], "descendant_closure_status": "UNKNOWN", "issued_at": "2026-07-25T12:01:00Z",
            "signature": _T11.signature("valid", kid="ops-key")}
    _gf = _T11.GateFixture(degraded_effects=["READ", "WRITE", "DELETE"], degraded_targets=["https://db.example.internal/"])
    _gf.gate.authorize(_gf.request(), _T11.evidence_bundle())
    _gf.gate.authorize(_gf.request(nonce="b" * 32), _T11.evidence_bundle(receipt=_T11.witness_receipt(health="DEGRADED", epoch=8)))
    _gf.gate.submit_amendment(_cp.deepcopy(_amd))
    _gf.gate.authorize(_gf.request(nonce="3" * 32), _T11.evidence_bundle())
    _grecs = _gf.gate.state.records
    _gev = [r for r in _grecs if isinstance(r, dict) and r.get("record_type") == "bssg.correction-event"][0]
    _gmk = [r for r in _grecs if isinstance(r, dict) and r.get("record_type") == "bssg.correction-accepted"][0]
    _ggrants = _BG.grants_from_state(_gf.gate)
    _gland = _ggrants["sess-0001"]["landing_epoch"]
    _TGTR = "https://db.example.internal/records/"
    _amend_honest = [{"session_id": "sess-0001", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": [_TGTR]}},
                     _gev, _gmk, {"session_id": "sess-0001", "authority_epoch": _gland, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": [_TGTR]}}]
    _x7_amend_anchored = _BG.check_authority_history(_amend_honest, grants=_ggrants)   # anchored -> []
    _x7_amend_unanchored = _BG.check_authority_history(_amend_honest)                  # no grant -> X7

    # -- X5 / X6 lineage-family binding (V29): G11 previously exercised only X4/X7/X8, leaving the descendant-
    # closure (X5) and lineage-completeness (X6) checkers unbound by the verifier. Bind each on a negative
    # vector (detected), a positive vector (clean), and a TOTALITY vector (a non-dict input fails closed to a
    # list, never raises -- the K-round non-total defect).
    _x5_neg = _BG.check_correction_closure({"descendant_closure_status": "COMPLETE", "descendants": None, "unreachable_descendants": ["d1"]})  # COMPLETE w/ gaps -> X5
    _x5_badstatus = _BG.check_correction_closure({"descendant_closure_status": "NONSENSE"})                                                    # bad status -> X5b
    _x5_pos = _BG.check_correction_closure({"descendant_closure_status": "COMPLETE", "descendants": []})                                       # well-formed -> []
    _x6_neg = _BG.check_lineage_completeness({"completeness": "COMPLETE", "declared_gaps": ["g1"], "nodes": []})                               # COMPLETE w/ declared gaps -> X6
    _x6_dangling = _BG.check_lineage_completeness({"completeness": "COMPLETE", "declared_gaps": [], "nodes": [{"node_id": "a", "parents": ["missing"]}]})  # dangling parent -> X6c
    _x6_pos = _BG.check_lineage_completeness({"completeness": "PARTIAL", "declared_gaps": ["g1"], "nodes": [{"node_id": "a", "parents": []}]})              # PARTIAL w/ gaps -> []
    def _is_total(_fn, _inputs):
        for _h in _inputs:
            try:
                if not isinstance(_fn(_h), list):
                    return False
            except Exception:
                return False   # a checker that RAISES on hostile input is non-total (fails closed to a list is required)
        return True
    _x5_total = _is_total(_BG.check_correction_closure, (None, 42, "s", [1]))    # totality: never raises
    _x6_total = _is_total(_BG.check_lineage_completeness, (None, 42, "s", [1]))

    # -- TAMPER-DETECTION: a deliberately corrupted copy of the real stream MUST be flagged, proving the
    # checkers are not vacuous on the real record shape.
    _tamp_x7 = _cp.deepcopy(_real)
    for _r in _tamp_x7:
        if _r.get("record_type") == "bssg.decision" and isinstance(_r.get("authority_snapshot"), dict):
            _r["authority_snapshot"]["effects"] = list(set(_r["authority_snapshot"].get("effects", [])) | {"DELETE", "ADMIN"})
            _r["authority_epoch"] = 0  # epoch regression on a real record
    _x7_tamper = _BG.check_authority_history(_tamp_x7)            # MUST be flagged
    _tid = _execs[0]["commit_token_id"] if _execs else "t"
    _x4_tamper = _BG.check_single_redemption([{"commit_token_id": _tid, "outcome": "COMMITTED_PENDING_OUTCOME"},
                                              {"commit_token_id": _tid, "outcome": "COMMITTED_PENDING_OUTCOME"}])

    # health-only bump + accepted-amendment carve-out (valid LIFT) + forged-amendment rejection.
    _x7_healthonly = _BG.check_authority_history([{"session_id": "s", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}, {"session_id": "s", "authority_epoch": 2, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}])
    _raw_lift = {"record_type": "bssg.correction-event", "spec_version": _BG.SPEC_VERSION, "correction_id": "cor-g11",
                 "correction_class": "LIFT_TERMINAL_STATE", "supersedes": _BG.digest_bytes(b"p"), "reason_code": "C-TERMINAL-REVIEWED",
                 "issued_by": {"authority_id": "ops-1", "control_domain": "ops-domain"}, "session_id": "s", "subject_control_domain": "subject-domain",
                 "adjudicators": [{"adjudicator_id": "adj-1", "control_domain": "audit-domain", "signature": _T11.signature("valid", "adj-1")},
                                  {"adjudicator_id": "adj-2", "control_domain": "legal-domain", "signature": _T11.signature("valid", "adj-2")}],
                 "descendants": [], "descendant_closure_status": "UNKNOWN", "issued_at": "2026-07-25T12:01:00Z", "signature": _T11.signature("valid", "ops-key")}
    _marker = {"record_type": "bssg.correction-accepted", "spec_version": _BG.SPEC_VERSION, "gate_version": _BG.GATE_VERSION,
               "correction_id": "cor-g11", "correction_class": "LIFT_TERMINAL_STATE", "session_id": "s",
               "authority_epoch": 2, "licensed_epoch": 3, "correction_digest": _BG.digest(_raw_lift), "adjudicators_verified": 2}
    # a marker BOUND to a present accepted-LIFT event licenses the re-widening AT ITS DECLARED licensed epoch
    # (marker+1, the honest landing); the raw event alone and a bare forged event do NOT (A2 / GPT-P19-01).
    _x7_amend = _BG.check_authority_history([_HELD, {"session_id": "s", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}, _raw_lift, _marker, {"session_id": "s", "authority_epoch": 3, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}])
    _x7_raw_amend = _BG.check_authority_history([{"session_id": "s", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}, _raw_lift, {"session_id": "s", "authority_epoch": 2, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}])
    _x7_forged_amend = _BG.check_authority_history([{"session_id": "s", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}, {"record_type": "bssg.correction-event", "session_id": "s"}, {"session_id": "s", "authority_epoch": 2, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}])

    _x_ok = (not _x8_clean and "X8" in _x8_forged and "X8" in _x8_absent
             and "X7" in _x7_bad and "X7" in _x7_same_epoch
             and "X4" in _x4_bad and "X4" in _x4_dbl_succeeded and not _x4_settle_chain
             and "X4" in _x4_fail_then_success
             and not _x7_real and not _x4_real
             and "X7" in _x7_tamper and "X4" in _x4_tamper                 # vacuity guard
             and not _x7_healthonly
             and not _x7_amend_anchored and "X7" in _x7_amend_unanchored   # B: valid marker clean ONLY when anchored to the grant
             and "X7" in _x7_raw_amend and "X7" in _x7_forged_amend        # A2: only the marker arms
             and "X5" in _x5_neg and "X5b" in _x5_badstatus and not _x5_pos    # X5 descendant-closure bound
             and "X6" in _x6_neg and "X6c" in _x6_dangling and not _x6_pos     # X6 lineage-completeness bound
             and _x5_total and _x6_total)                                  # X5/X6 totality: non-dict fails closed, never raises
    record("G11", "PASS" if _x_ok else "FAIL",
           "X4/X5/X6/X7/X8 detect negatives, pass positives, bind + tamper-check real gate records; X5/X6 total" if _x_ok else "X-invariant checker gap")


def gate_g12():
    """G12 (claim-substrate consistency, registry-driven -- pass-21). Retires the 'performed repair' shape
    AND its own pass-20 recursion (GPT-P4 / GLM-01 / K20-G1: the pass-20 G12 hardcoded four probes and let
    an unprobed false claim ship green). The fix inverts the default: a CLAIMS REGISTRY is the single
    source of truth for load-bearing retirement claims, and coverage is VERIFIED, not asserted --
      1. every registered claim's probe MUST pass;
      2. every registered claim MUST be tagged `{claim:ID}` in REPAIR_STATUS (no orphan probe);
      3. every `{claim:ID}` tag in REPAIR_STATUS MUST be a registered id (no unregistered load-bearing
         claim ships without a probe -- this is the coverage-completeness that pass-20 lacked);
      4. every `CE<N>` cited in REPAIR_STATUS (any digit count) MUST exist in the corpus; and
      5. numeric corpus claims (counterexample count) MUST match the actual corpus.
    HONEST SCOPE (corrected from pass-20): G12 verifies REGISTERED load-bearing claims and does NOT claim
    to verify arbitrary prose -- so a load-bearing claim MUST be registered and tagged, and an untagged
    prose sentence is out of scope by construction, not silently blessed."""
    import bssg_gate as _BG
    import test_bssg_gate as _T
    import re
    import copy as _copy
    failures = []

    # V29 (Strategy B): the verifier's OWN independent runtime-grant anchor. Built here from _T.GateFixture --
    # NOT imported from the corpus under test -- so the verifier and the corpus arrive at the same anchoring
    # independently. Drives a genuine amendment (authorize -> degrade-to-terminal -> accepted LIFT -> re-auth)
    # and exports the AUTHENTICATED grant via grants_from_state. Every migrated X7/marker probe's positive
    # control is anchored to THIS grant, and each also asserts the same honest stream fails closed (X7) with no
    # grant supplied -- so a fail-open regression (B reverted to trust stream-derived authority) fails the probe.
    _REAL_TGT_V = "https://db.example.internal/records/"
    def _real_grant_v(cid="cor-v29"):
        _adj = lambda i, d: {"adjudicator_id": i, "control_domain": d, "signature": _T.signature("valid", kid=i)}
        amd = {"record_type": "bssg.correction-event", "spec_version": _BG.SPEC_VERSION, "correction_id": cid,
               "correction_class": "LIFT_TERMINAL_STATE", "supersedes": _BG.digest_bytes(b"prior-decision"),
               "reason_code": "C-TERMINAL-REVIEWED", "issued_by": {"authority_id": "ops-1", "control_domain": "ops-domain"},
               "session_id": "sess-0001", "subject_control_domain": "subject-domain",
               "adjudicators": [_adj("adj-1", "audit-domain"), _adj("adj-2", "ops-domain")],
               "descendants": [], "descendant_closure_status": "UNKNOWN", "issued_at": "2026-07-25T12:01:00Z",
               "signature": _T.signature("valid", kid="ops-key")}
        f = _T.GateFixture(degraded_effects=["READ", "WRITE", "DELETE"], degraded_targets=["https://db.example.internal/"])
        f.gate.authorize(f.request(), _T.evidence_bundle())
        f.gate.authorize(f.request(nonce="b" * 32), _T.evidence_bundle(receipt=_T.witness_receipt(health="DEGRADED", epoch=8)))
        accepted = f.gate.submit_amendment(_copy.deepcopy(amd)).get("accepted") is True
        f.gate.authorize(f.request(nonce="3" * 32), _T.evidence_bundle())
        recs = f.gate.state.records
        ev = [r for r in recs if isinstance(r, dict) and r.get("record_type") == "bssg.correction-event"][0]
        mk = [r for r in recs if isinstance(r, dict) and r.get("record_type") == "bssg.correction-accepted"][0]
        grants = _BG.grants_from_state(f.gate)
        g = grants["sess-0001"]
        return {"grants": grants, "event": ev, "marker": mk, "session": "sess-0001", "landing": g["landing_epoch"],
                "accepted": accepted}
    try:
        _RG = _real_grant_v()
        _RG_OK = _RG["accepted"] and _RG["session"] in _RG["grants"]
    except Exception:
        _RG, _RG_OK = None, False
    def _anchored_honest(effects=("READ", "WRITE"), targets=(_REAL_TGT_V,), epoch=None):
        S = _RG["session"]
        narrow = {"session_id": S, "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": [_REAL_TGT_V]}}
        wide = {"session_id": S, "authority_epoch": _RG["landing"] if epoch is None else epoch,
                "authority_snapshot": {"effects": list(effects), "target_scopes": list(targets)}}
        return [narrow, _RG["event"], _RG["marker"], wide]
    # positive control shared by the migrated probes: anchored -> clean, unanchored -> X7 (fail closed).
    def _anchor_clean_and_failclosed():
        return (_RG_OK
                and _BG.check_authority_history(_anchored_honest(), grants=_RG["grants"]) == []
                and "X7" in _BG.check_authority_history(_anchored_honest()))

    def _clock_strict():
        # K26-VF-1: BEHAVIORAL, not source-grep. (1) _read_clock rejects every non-int/out-of-range clock
        # value with _ClockFault. (2) the REAL authorize path fails closed (never ALLOW) under a non-int
        # clock -- exercising the actual clock-reading site rather than substring-matching the source. A gate
        # that coerces the clock (int(self.clock())) fails (1), so the mutation axis below catches a downgrade.
        for bad in ["1", 1.5, True, -1, 2 ** 60]:
            g = _BG.BSSGGate(*_T.build_registries()[:2], (lambda b=bad: b), _T.injected_verifier, lambda: "tok-1")
            try:
                g._read_clock(); return False
            except _BG._ClockFault:
                pass
        for bad in [1.5, "1", True]:
            g = _BG.BSSGGate(*_T.build_registries()[:2], (lambda b=bad: b), _T.injected_verifier, lambda: "tok-1")
            try:
                d = g.authorize(_T.GateFixture().request(), _T.evidence_bundle())
            except Exception:
                return False   # an entrypoint that raises instead of failing closed is not strict
            if d.get("decision") == _BG.DECISION_ALLOW:
                return False   # a non-int clock must never yield ALLOW
        return True

    def _x4_failclosed():
        # a double redemption whose token id is an unhashable JSON value is still flagged (not skipped).
        return "X4" in _BG.check_single_redemption([{"commit_token_id": ["x"], "outcome": "SUCCEEDED"},
                                                    {"commit_token_id": ["x"], "outcome": "SUCCEEDED"}])

    def _type_strict():
        return "X7" in _BG.check_authority_history([{"session_id": "s", "authority_epoch": True, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]},
                                                     "authorization_receipt": {"session_id": "s", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}}])

    def _unhashable_total():
        r = _BG.check_authority_history([{"session_id": "s", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ", ["n"]], "target_scopes": ["a"]}},
                                         {"session_id": "s", "authority_epoch": 2, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}])
        return isinstance(r, list)

    def _a4_omission():
        # a settlement receipt that OMITS revalidation.authority_epoch fails closed (X7).
        return "X7" in _BG.check_authority_history([{"record_type": "bssg.execution-receipt", "outcome": "SUCCEEDED",
                                                     "authorization_receipt_digest": "sha256:" + "0" * 64, "revalidation": {"result": "PASS"}}])

    def _a2_marker_bound():
        # GPT-P21-03: registry presence is not coverage. This probe enumerates EVERY negative binding
        # dimension (unbound digest, cross-session, mismatched correction-id, duplicate/replayed marker,
        # future-event retrobind) -- all must return X7 -- and confirms the one correctly-ordered, bound,
        # single-use chain stays clean. Coverage: {digest, session-identity, correction-identity,
        # replay/consumption, stream-order}.
        def ev(session, cid="c"):
            return {"record_type": "bssg.correction-event", "spec_version": _BG.SPEC_VERSION, "correction_id": cid,
                    "correction_class": "LIFT_TERMINAL_STATE", "supersedes": _BG.digest_bytes(b"p"), "reason_code": "C-TERMINAL-REVIEWED",
                    "issued_by": {"authority_id": "o", "control_domain": "ops"}, "session_id": session, "subject_control_domain": "subj",
                    "adjudicators": [{"adjudicator_id": "a1", "control_domain": "audit", "signature": _T.signature("valid", "a1")},
                                     {"adjudicator_id": "a2", "control_domain": "legal", "signature": _T.signature("valid", "a2")}],
                    "descendants": [], "descendant_closure_status": "UNKNOWN", "issued_at": "2026-07-25T12:01:00Z", "signature": _T.signature("valid", "o")}
        def mk(session, e, ep=2):
            return {"record_type": "bssg.correction-accepted", "spec_version": _BG.SPEC_VERSION, "gate_version": _BG.GATE_VERSION,
                    "correction_id": e["correction_id"], "correction_class": "LIFT_TERMINAL_STATE", "session_id": session,
                    "authority_epoch": ep, "licensed_epoch": ep + 1, "correction_digest": _BG.digest(e), "adjudicators_verified": 2}
        b = lambda s, ep: {"session_id": s, "authority_epoch": ep, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}
        w = lambda s, ep: {"session_id": s, "authority_epoch": ep, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}
        eA = ev("A"); eS = ev("s"); mS = mk("s", eS)
        neg = [
            [b("B", 1), eA, mk("B", eA), w("B", 2)],                                   # cross-session
            [b("s", 1), eS, dict(mk("s", eS), correction_id="other"), w("s", 2)],      # mismatched correction-id
            [b("s", 1), dict(mS, correction_digest="sha256:" + "0" * 64), w("s", 2)],  # unbound digest
            [b("s", 1), mk("s", eS), w("s", 2), eS],                                   # future-event retrobind
            [b("s", 1), eS, mS, w("s", 3), b("s", 4), mS, w("s", 5)],                  # duplicate-marker replay (2nd not re-licensed)
        ]
        for stream in neg:
            if "X7" not in _BG.check_authority_history(stream):
                return False
        return _anchor_clean_and_failclosed()       # sole legit chain: anchored -> clean, unanchored -> X7 (fail closed under B)

    def _interval_commit():
        f = _T.GateFixture(); a = f.gate.authorize(f.request(nonce="c" * 32), _T.evidence_bundle())
        rc = a["authorization_receipt"]; b = {k: rc[k] for k in ("request_digest", "canonical_target", "params_digest", "adapter_digest", "effect_type")}
        fresh = _T.witness_receipt(); fresh["observed_at"] = "2026-07-25T12:00:04Z"; fresh["expires_at"] = "2026-07-25T12:00:02Z"
        out = f.gate.commit(rc["commit_token"]["token_id"], b, {"witness_receipt": fresh})
        return "E-COMMIT-WITNESS-LEASE-INVERTED" in out.get("reason_codes", [])

    def _x4_float():
        # K21-A2: two DISTINCT NaN token ids (a multi-shard merge) must not launder a double redemption.
        return "X4" in _BG.check_single_redemption([{"commit_token_id": float("nan"), "outcome": "SUCCEEDED"},
                                                    {"commit_token_id": float("nan"), "outcome": "SUCCEEDED"}])

    def _x4_outcome_type():
        # K25-A2: an unhashable list/dict outcome must not crash X4; it fails closed as malformed.
        try:
            return "X4" in _BG.check_single_redemption([{"commit_token_id": "t", "outcome": ["SUCCEEDED"]}])
        except Exception:
            return False

    def _x7_epoch_type():
        # K25-A3: a PRESENT but wrong-typed authority_epoch (float) fails closed, not silently skipped.
        return "X7" in _BG.check_authority_history([
            {"session_id": "s", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}},
            {"session_id": "s", "authority_epoch": 2.0, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}])

    def _x4_numeric_keyspace():
        # K25-A1: int 1 and float 1.0 are one token -- a double redemption across them is caught.
        return "X4" in _BG.check_single_redemption([{"commit_token_id": 1, "outcome": "SUCCEEDED"},
                                                    {"commit_token_id": 1.0, "outcome": "SUCCEEDED"}])

    def _strict_materialization():
        # P23-04 (behavioral, non-vacuous): the strict materializer round-trips EXACT structures and fails
        # closed to the sentinel on any subclass / hostile accessor, WITHOUT dispatching the accessor. AND
        # (V23-GPT-04) the actual boundary SITES -- both checkers and the projection predicates -- must use
        # it, so a two-view hostile dict cannot project a forged AUTHORIZED via subject_facing.
        exact = _BG._strict_copy({"a": [1, "x", {"b": True}], "c": None})
        class HL(list):
            def __iter__(self): raise AssertionError("hostile __iter__ must never run")
        class HD(dict):
            def items(self): raise AssertionError("hostile items must never run")
        class FlipD(dict):
            def __init__(self, a, b):
                super().__init__(a); self._v = [a, b]; self._n = 0
            def items(self):
                v = self._v[self._n % 2]; self._n += 1; return v.items()
            def get(self, k, d=None):
                v = self._v[self._n % 2]; self._n += 1; return v.get(k, d)
        good = {"decision": "ALLOW", "issuance_status": "ISSUED"}; bad = {"decision": "DENY_FALSE"}
        # V23-GPT-04: a GENUINELY authorized record wrapped in a plain dict subclass must be REJECTED at the
        # projection sites (strict materialization refuses the subclass). Under lenient json materialization
        # the subclass would round-trip to an authorized plain dict and project AUTHORIZED -- so this probe
        # fails if strict materialization is removed from subject_facing or authorized_issuance.
        _f = _T.GateFixture(); _allow = _f.gate.authorize(_f.request(), _T.evidence_bundle())
        class _Sub(dict): pass
        return (exact == {"a": [1, "x", {"b": True}], "c": None}
                and _BG._strict_copy(HL([1, 2])) is _BG._UNCOPYABLE_INPUT
                and _BG._strict_copy(HD({"x": 1})) is _BG._UNCOPYABLE_INPUT
                and _BG.check_single_redemption(HL([{"commit_token_id": "t", "outcome": "SUCCEEDED"}])) == ["X4"]
                and _BG.BSSGGate.authorized_issuance(_allow) is True                      # genuine authorized
                and _BG.BSSGGate.authorized_issuance(_Sub(_allow)) is False               # site: authorized_issuance
                and _f.gate.authorized_issuance_bound(_Sub(_allow)) is False              # site: authorized_issuance_bound (A9)
                and _BG.BSSGGate.subject_facing(_Sub(_allow)).get("decision") == "DENIED")  # site: subject_facing

    def _top_signature():
        # V23-GPT-03/05: under `verify`, a correction-event whose TOP-LEVEL signature does not verify does
        # NOT arm the carve-out, even if its adjudicator signatures verify. The payload matches runtime.
        ev = {"record_type": "bssg.correction-event", "spec_version": _BG.SPEC_VERSION, "correction_id": "c",
              "correction_class": "LIFT_TERMINAL_STATE", "supersedes": _BG.digest_bytes(b"p"), "reason_code": "C-TERMINAL-REVIEWED",
              "issued_by": {"authority_id": "o", "control_domain": "ops"}, "session_id": "s", "subject_control_domain": "subj",
              "adjudicators": [{"adjudicator_id": "a1", "control_domain": "audit", "signature": _T.signature("valid", "a1")},
                               {"adjudicator_id": "a2", "control_domain": "legal", "signature": _T.signature("valid", "a2")}],
              "descendants": [], "descendant_closure_status": "UNKNOWN", "issued_at": "2026-07-25T12:01:00Z",
              "signature": _T.signature("valid", "corr")}
        mk = {"record_type": "bssg.correction-accepted", "spec_version": _BG.SPEC_VERSION, "gate_version": _BG.GATE_VERSION,
              "correction_id": "c", "correction_class": "LIFT_TERMINAL_STATE", "session_id": "s", "authority_epoch": 2, "licensed_epoch": 3,
              "correction_digest": _BG.digest(ev), "adjudicators_verified": 2}
        b1 = {"session_id": "s", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}
        w2 = {"session_id": "s", "authority_epoch": 3, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}
        v_reject_top = lambda role, payload, s: role == "adjudicator"   # accepts adjudicator, rejects top
        v_all = lambda role, payload, s: True
        # A8 (K25-A8): assert the offline top-signature PAYLOAD equals the runtime submit_amendment payload,
        # not merely that a rejecting verifier fails to arm. Capture the bytes the verifier is handed.
        seen = {}
        def v_capture(role, payload, s):
            if role == "correction":
                seen["top"] = payload
            return True
        _BG.check_authority_history([b1, ev, mk, w2], verify=v_capture)
        runtime_payload = _BG.canonical_bytes({k: vv for k, vv in ev.items() if k != "signature"})
        return ("X7" in _BG.check_authority_history([b1, ev, mk, w2], verify=v_reject_top)
                and _RG_OK
                and _BG.check_authority_history(_anchored_honest(), grants=_RG["grants"], verify=v_all) == []   # accepting verify + grant -> clean
                and "X7" in _BG.check_authority_history(_anchored_honest(), verify=v_all)                       # accepting verify but NO grant -> X7 (fail closed)
                and seen.get("top") == runtime_payload)

    def _marker_floor():
        # P23-02: a marker's declared epoch is INSTALLED as a floor; a later record below it is X7.
        def ev(cid="c"):
            return {"record_type": "bssg.correction-event", "spec_version": _BG.SPEC_VERSION, "correction_id": cid,
                    "correction_class": "LIFT_TERMINAL_STATE", "supersedes": _BG.digest_bytes(b"p"), "reason_code": "C-TERMINAL-REVIEWED",
                    "issued_by": {"authority_id": "o", "control_domain": "ops"}, "session_id": "s", "subject_control_domain": "subj",
                    "adjudicators": [{"adjudicator_id": "a1", "control_domain": "audit", "signature": _T.signature("valid", "a1")},
                                     {"adjudicator_id": "a2", "control_domain": "legal", "signature": _T.signature("valid", "a2")}],
                    "descendants": [], "descendant_closure_status": "UNKNOWN", "issued_at": "2026-07-25T12:01:00Z", "signature": _T.signature("valid", "o")}
        e = ev()
        b5 = {"session_id": "s", "authority_epoch": 5, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}
        m999 = {"record_type": "bssg.correction-accepted", "spec_version": _BG.SPEC_VERSION, "gate_version": _BG.GATE_VERSION,
                "correction_id": "c", "correction_class": "LIFT_TERMINAL_STATE", "session_id": "s", "authority_epoch": 999,
                "correction_digest": _BG.digest(e), "adjudicators_verified": 2}
        null6 = {"session_id": "s", "authority_epoch": 6, "authority_snapshot": None}
        w999 = {"session_id": "s", "authority_epoch": 999, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}
        return "X7" in _BG.check_authority_history([b5, e, m999, null6, w999])

    def _x4_subclass():
        # GLM-01: a str-subclass token id with a hostile __hash__/__eq__ cannot bypass X4 de-duplication.
        class _E(str):
            _c = [0]
            def __hash__(self): _E._c[0] += 1; return _E._c[0]
            def __eq__(self, o): return False
        return "X4" in _BG.check_single_redemption([{"commit_token_id": _E("t"), "outcome": "SUCCEEDED"},
                                                    {"commit_token_id": _E("t"), "outcome": "SUCCEEDED"}])

    def _x7_subclass():
        # GLM-02: a str-subclass session_id cannot split one session and hide a widening.
        class _E(str):
            _c = [0]
            def __hash__(self): _E._c[0] += 1; return _E._c[0]
            def __eq__(self, o): return False
        return "X7" in _BG.check_authority_history([{"session_id": _E("s"), "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}},
                                                    {"session_id": _E("s"), "authority_epoch": 2, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}])

    def _marker_epoch():
        # GPT-B: a marker's own authority_epoch is tamper-checked (a bogus epoch below the preceding record,
        # or one whose licensed widening lands at a different epoch, is X7).
        def ev(cid="c"):
            return {"record_type": "bssg.correction-event", "spec_version": _BG.SPEC_VERSION, "correction_id": cid,
                    "correction_class": "LIFT_TERMINAL_STATE", "supersedes": _BG.digest_bytes(b"p"), "reason_code": "C-TERMINAL-REVIEWED",
                    "issued_by": {"authority_id": "o", "control_domain": "ops"}, "session_id": "s", "subject_control_domain": "subj",
                    "adjudicators": [{"adjudicator_id": "a1", "control_domain": "audit", "signature": _T.signature("valid", "a1")},
                                     {"adjudicator_id": "a2", "control_domain": "legal", "signature": _T.signature("valid", "a2")}],
                    "descendants": [], "descendant_closure_status": "UNKNOWN", "issued_at": "2026-07-25T12:01:00Z", "signature": _T.signature("valid", "o")}
        def mk(e, ep):
            return {"record_type": "bssg.correction-accepted", "spec_version": _BG.SPEC_VERSION, "gate_version": _BG.GATE_VERSION,
                    "correction_id": e["correction_id"], "correction_class": "LIFT_TERMINAL_STATE", "session_id": "s",
                    "authority_epoch": ep, "licensed_epoch": ep + 1, "correction_digest": _BG.digest(e), "adjudicators_verified": 2}
        e = ev()
        b5 = {"session_id": "s", "authority_epoch": 5, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}
        w6 = {"session_id": "s", "authority_epoch": 6, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}
        w7 = {"session_id": "s", "authority_epoch": 7, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}
        return ("X7" in _BG.check_authority_history([b5, e, mk(e, 0), w6])           # epoch below preceding
                and "X7" in _BG.check_authority_history([b5, e, mk(e, 999), w6])     # inflated epoch
                and _anchor_clean_and_failclosed())        # legit widening lands at the grant landing (marker+1): anchored clean / unanchored X7

    def _x7_licensed_epoch():
        # V26 X7-2 (BLOCKER): the license LANDING epoch is DERIVED (marker_epoch+1), NOT trusted from the
        # marker's licensed_epoch field. This probe FAILS against the pass-27 behavior (which read the field
        # directly): a TAMPERED licensed_epoch=50 + forged WIDE@50 must be X7 (V23-GPT-02), and a tampered
        # licensed_epoch=marker_epoch + forged@marker must be X7 (the K26-X7-1 fail-open shape). Only a marker
        # whose licensed_epoch == authority_epoch+1 arms, and only at that derived epoch.
        def ev(cid="c"):
            return {"record_type": "bssg.correction-event", "spec_version": _BG.SPEC_VERSION, "correction_id": cid,
                    "correction_class": "LIFT_TERMINAL_STATE", "supersedes": _BG.digest_bytes(b"p"), "reason_code": "C-TERMINAL-REVIEWED",
                    "issued_by": {"authority_id": "o", "control_domain": "ops"}, "session_id": "s", "subject_control_domain": "subj",
                    "adjudicators": [{"adjudicator_id": "a1", "control_domain": "audit", "signature": _T.signature("valid", "a1")},
                                     {"adjudicator_id": "a2", "control_domain": "legal", "signature": _T.signature("valid", "a2")}],
                    "descendants": [], "descendant_closure_status": "UNKNOWN", "issued_at": "2026-07-25T12:01:00Z", "signature": _T.signature("valid", "o")}
        e = ev()
        def mk(le):
            return {"record_type": "bssg.correction-accepted", "spec_version": _BG.SPEC_VERSION, "gate_version": _BG.GATE_VERSION,
                    "correction_id": "c", "correction_class": "LIFT_TERMINAL_STATE", "session_id": "s", "authority_epoch": 3,
                    "licensed_epoch": le, "correction_digest": _BG.digest(e), "adjudicators_verified": 2}
        b1 = {"session_id": "s", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}
        b2 = {"session_id": "s", "authority_epoch": 2, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}
        forged3 = {"session_id": "s", "authority_epoch": 3, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}
        honest4 = {"session_id": "s", "authority_epoch": 4, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}
        far50 = {"session_id": "s", "authority_epoch": 50, "authority_snapshot": {"effects": ["READ", "WRITE", "DELETE"], "target_scopes": ["*"]}}
        # V27 (BLOCKER): the landing is bound to the checker's OWN tracked epoch and to demonstrably-held
        # authority, NOT to any marker-carried field. These sub-assertions FAIL against the pass-28 behavior
        # (derive marker_epoch+1 from the unsigned marker): a DUAL-FIELD tamper moving authority_epoch and
        # licensed_epoch together, and a WALK-UP that advances the epoch via a narrowing then re-widens beyond
        # held authority, must both be X7.
        def mkep(ep, le):
            m = dict(mk(le)); m["authority_epoch"] = ep; return m
        dual = mkep(49, 50)                                                    # both fields moved together
        wide50 = {"session_id": "s", "authority_epoch": 50, "authority_snapshot": {"effects": ["READ", "WRITE", "DELETE"], "target_scopes": ["*"]}}
        narrow48 = {"session_id": "s", "authority_epoch": 48, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}
        walkup_mk = mkep(49, 50)
        return ("X7" in _BG.check_authority_history([b1, b2, e, mk(4), forged3])          # forged @marker epoch -> X7
                and _anchor_clean_and_failclosed()        # honest landing @grant epoch -> anchored clean / unanchored X7
                and "X7" in _BG.check_authority_history([b1, b2, e, mk(50), far50])       # tampered le=50 + WIDE@50 -> X7
                and "X7" in _BG.check_authority_history([b1, b2, e, mk(3), forged3])      # tampered le=marker + WIDE@marker -> X7
                and "X7" in _BG.check_authority_history([b1, e, dual, wide50])            # V27 dual-field relocation -> X7
                and "X7" in _BG.check_authority_history([b1, e, dual, wide50], verify=lambda *a: True)  # survives verify
                and "X7" in _BG.check_authority_history([b1, e, narrow48, walkup_mk, wide50]))  # V27 walk-up escalation -> X7

    def _x7_breadth_bound():
        # V27 (BLOCKER): a licensed re-widen may only restore authority the session DEMONSTRABLY HELD; an
        # escalation beyond the held envelope is X7 even under a well-formed license. FAILS against any build
        # that licenses an unbounded re-widen.
        def ev(cid="c"):
            return {"record_type": "bssg.correction-event", "spec_version": _BG.SPEC_VERSION, "correction_id": cid,
                    "correction_class": "LIFT_TERMINAL_STATE", "supersedes": _BG.digest_bytes(b"p"), "reason_code": "C-TERMINAL-REVIEWED",
                    "issued_by": {"authority_id": "o", "control_domain": "ops"}, "session_id": "s", "subject_control_domain": "subj",
                    "adjudicators": [{"adjudicator_id": "a1", "control_domain": "audit", "signature": _T.signature("valid", "a1")},
                                     {"adjudicator_id": "a2", "control_domain": "legal", "signature": _T.signature("valid", "a2")}],
                    "descendants": [], "descendant_closure_status": "UNKNOWN", "issued_at": "2026-07-25T12:01:00Z", "signature": _T.signature("valid", "o")}
        e = ev()
        mk = {"record_type": "bssg.correction-accepted", "spec_version": _BG.SPEC_VERSION, "gate_version": _BG.GATE_VERSION,
              "correction_id": "c", "correction_class": "LIFT_TERMINAL_STATE", "session_id": "s", "authority_epoch": 2,
              "licensed_epoch": 3, "correction_digest": _BG.digest(e), "adjudicators_verified": 2}
        # V29 (Strategy B): the breadth bound is the AUTHENTICATED restored authority (the grant's restored
        # set), NOT any stream-derived "held" envelope. Within the restored set is clean ONLY when anchored;
        # beyond it (a wider effect or a wider target) is X7 EVEN WITH the grant; unanchored is X7 always.
        return (_RG_OK
                and _BG.check_authority_history(_anchored_honest(), grants=_RG["grants"]) == []                                              # within restored -> anchored clean
                and "X7" in _BG.check_authority_history(_anchored_honest())                                                                 # within restored but UNANCHORED -> X7
                and "X7" in _BG.check_authority_history(_anchored_honest(effects=("READ", "WRITE", "DELETE")), grants=_RG["grants"])         # beyond restored EFFECT -> X7 even anchored
                and "X7" in _BG.check_authority_history(_anchored_honest(targets=("https://db.example.internal/",)), grants=_RG["grants"]))  # beyond restored TARGET -> X7 even anchored

    def _abort_clock_independent():
        # V27-GPT (BLOCKER): the abort recovers a clock-INDEPENDENT determinate FALSE (an out-of-contract
        # effect) even when the FIRST clock read raises. FAILS against pass-28 (which gated all recovery on a
        # valid stashed clock).
        f = _T.GateFixture(); f.gate.authorize(f.request(nonce="1" * 32), _T.evidence_bundle())
        f.gate.clock = lambda: (_ for _ in ()).throw(RuntimeError("first clock read unavailable"))
        d = f.gate.authorize(f.request(nonce="2" * 32, effect="ADMIN"), _T.evidence_bundle())
        return d["decision"] == _BG.DECISION_DENY_FALSE and d.get("conjuncts", {}).get("EffectTypeValid") == _BG.FALSE

    def _kernel_false_dom():
        # V26 kernel BLOCKER (GPT P3 + Kimi K27-K-1): FALSE-domination in the abort path must (i) hold for a
        # determinate FALSE on ANY evidence-independent conjunct -- not only EvidenceCurrent -- and (ii)
        # re-derive expiry from the STASHED first clock read, never a fresh read that could itself fail. This
        # probe FAILS against pass-27: an out-of-contract effect with a raising witness was DENY_UNKNOWN
        # (EffectTypeValid masked), and an expired request whose abort-path re-read failed was DENY_UNKNOWN.
        f = _T.GateFixture(); f.gate.authorize(f.request(nonce="1" * 32), _T.evidence_bundle())
        f.gate._witness_healthy = lambda *a, **k: (_ for _ in ()).throw(RuntimeError("fault"))
        d_eff = f.gate.authorize(f.request(nonce="2" * 32, effect="ADMIN"), _T.evidence_bundle())
        g = _T.GateFixture(); g.gate.authorize(g.request(nonce="1" * 32), _T.evidence_bundle()); g.clock.advance(10 ** 9)
        g.gate._witness_healthy = lambda *a, **k: (_ for _ in ()).throw(RuntimeError("fault"))
        _og = g.gate._read_clock; _st = {"n": 0}
        def _flaky():
            _st["n"] += 1
            if _st["n"] >= 2:
                raise RuntimeError("clock fault on re-read")
            return _og()
        g.gate._read_clock = _flaky
        d_exp = g.gate.authorize(g.request(nonce="2" * 32), _T.evidence_bundle())
        h = _T.GateFixture(); h.gate.authorize(h.request(nonce="1" * 32), _T.evidence_bundle())
        h.gate._witness_healthy = lambda *a, **k: (_ for _ in ()).throw(RuntimeError("fault"))
        d_unk = h.gate.authorize(h.request(nonce="2" * 32), _T.evidence_bundle())
        return (d_eff["decision"] == _BG.DECISION_DENY_FALSE and d_eff.get("conjuncts", {}).get("EffectTypeValid") == _BG.FALSE
                and d_exp["decision"] == _BG.DECISION_DENY_FALSE and d_exp.get("conjuncts", {}).get("EvidenceCurrent") == _BG.FALSE
                and d_unk["decision"] == _BG.DECISION_DENY_UNKNOWN)

    def _grant_anchor():
        # V29 (Strategy B, core): the AUTHENTICATED grant is the SOLE source of PERMISSION to re-widen. Its
        # unique, non-redundant contribution is exactly this: an honest within-ceiling re-widen anchored to the
        # grant is CLEAN, and the identical stream with NO grant fails closed (X7). That anchor-presence pair is
        # the real tripwire -- reverting B to trust stream-derived authority flips the unanchored leg to clean
        # and FAILS this probe. The three divergence legs below assert the divergence PROPERTY holds (wrong
        # correction-digest, wrong landing-epoch, both X7); note (empirically verified, and recorded for the
        # seats) that each divergence is ALSO caught by defense-in-depth -- marker-arming for the digest, the
        # general re-widen tracking for the epoch, and an independent contract-ceiling check for breadth (the
        # grant's restored set EQUALS the full contract ceiling by construction, so the grant breadth conjunct
        # is redundant with that ceiling check). So these legs are NOT single-conjunct isolations of the grant
        # binding; they confirm the property is enforced, redundantly. Breadth divergence -> CLAIM-X7-BREADTH.
        if not _RG_OK:
            return False
        base = _anchored_honest()
        gr = _RG["grants"]
        wrong_digest = _copy.deepcopy(base); wrong_digest[2]["correction_digest"] = "sha256:" + "0" * 64
        wrong_epoch = _copy.deepcopy(base); wrong_epoch[3]["authority_epoch"] = _RG["landing"] + 1
        return (_BG.check_authority_history(base, grants=gr) == []                   # anchored within ceiling -> clean (grant = permission)
                and "X7" in _BG.check_authority_history(base)                        # SAME stream, no grant -> X7 (the load-bearing anchor pair)
                and "X7" in _BG.check_authority_history(wrong_digest, grants=gr)     # wrong correction-digest -> X7 (property; also marker-arming)
                and "X7" in _BG.check_authority_history(wrong_epoch, grants=gr))     # wrong landing-epoch -> X7 (property; also re-widen tracking)

    def _unanchored_failclosed():
        # V29 (Strategy B): with no usable grant the checker NEVER trusts stream-derived authority -- every
        # marker-licensed re-widen fails closed (X7). Covered: (a) no grants= at all; (b) an EMPTY grant ledger;
        # (c) a grant for a DIFFERENT session (no entry for this one). Closes the V28 PROBE-1 shape (a runtime
        # rejection mints no grant, so a claimed re-widen has nothing to anchor to).
        if not _RG_OK:
            return False
        h = _anchored_honest()
        return ("X7" in _BG.check_authority_history(h)                                             # (a) no grants
                and "X7" in _BG.check_authority_history(h, grants={})                              # (b) empty ledger
                and "X7" in _BG.check_authority_history(h, grants={"other-session": _RG["grants"][_RG["session"]]}))  # (c) wrong session

    def _abort_witness_clockindep():
        # V28 GLM-01 / Kimi-A1/A2 (BLOCKER): the kernel abort must recover WitnessHealthy's OWN determinate
        # FALSE even when the FIRST clock read raises -- the witness FALSE is clock-independent and must not be
        # masked to DENY_UNKNOWN by a clock fault. Distinct from CLAIM-KERNEL-FALSE-DOM (which raises the
        # witness and checks OTHER conjuncts): here WitnessHealthy itself is determinately FALSE (inverted lease)
        # while the first clock read is unavailable. Empirically grounded on real bytes.
        f = _T.GateFixture(); f.gate.authorize(f.request(nonce="1" * 32), _T.evidence_bundle())
        f.gate.clock = lambda: (_ for _ in ()).throw(RuntimeError("first clock read unavailable"))
        inv = _T.witness_receipt(); inv["observed_at"] = "2026-07-25T12:00:04Z"; inv["expires_at"] = "2026-07-25T12:00:02Z"
        d = f.gate.authorize(f.request(nonce="2" * 32), _T.evidence_bundle(receipt=inv))
        return d["decision"] == _BG.DECISION_DENY_FALSE and d.get("conjuncts", {}).get("WitnessHealthy") == _BG.FALSE

    def _x7_adj_kid():
        # V26-GPT (P2): offline X7 mirrors the runtime adjudicator kid binding -- an adjudicator signature
        # whose kid != adjudicator_id does not arm a marker even under a verify callable that accepts every
        # signature. FAILS against pass-27 (which omitted the offline kid check).
        e = {"record_type": "bssg.correction-event", "spec_version": _BG.SPEC_VERSION, "correction_id": "c",
             "correction_class": "LIFT_TERMINAL_STATE", "supersedes": _BG.digest_bytes(b"p"), "reason_code": "C-TERMINAL-REVIEWED",
             "issued_by": {"authority_id": "o", "control_domain": "ops"}, "session_id": "s", "subject_control_domain": "subj",
             "adjudicators": [{"adjudicator_id": "a1", "control_domain": "audit", "signature": {"kid": "WRONG", "alg": "x"}},
                              {"adjudicator_id": "a2", "control_domain": "legal", "signature": {"kid": "a2", "alg": "x"}}],
             "descendants": [], "descendant_closure_status": "UNKNOWN", "issued_at": "2026-07-25T12:01:00Z", "signature": {"kid": "corr", "alg": "x"}}
        mk = {"record_type": "bssg.correction-accepted", "spec_version": _BG.SPEC_VERSION, "gate_version": _BG.GATE_VERSION,
              "correction_id": "c", "correction_class": "LIFT_TERMINAL_STATE", "session_id": "s", "authority_epoch": 2,
              "licensed_epoch": 3, "correction_digest": _BG.digest(e), "adjudicators_verified": 2}
        b1 = {"session_id": "s", "authority_epoch": 1, "authority_snapshot": {"effects": ["READ"], "target_scopes": ["a"]}}
        w3 = {"session_id": "s", "authority_epoch": 3, "authority_snapshot": {"effects": ["READ", "WRITE"], "target_scopes": ["a"]}}
        return "X7" in _BG.check_authority_history([b1, e, mk, w3], verify=lambda *a: True)

    def _x7_reserved_wrongtype():
        # V26-GPT (P5): a PRESENT wrong-typed authority field on a reserved record-type is X7, caught BEFORE
        # the reserved-type continue branch. FAILS against pass-27 (which skipped it under the receipt branch).
        er = {"record_type": "bssg.execution-receipt", "session_id": 1.0, "authority_epoch": 2.0, "revalidation": {"result": "FAIL"}}
        return "X7" in _BG.check_authority_history([er])

    def _issuance_bound_atomic():
        # V26-GPT (P4) + V27-GPT (MAJOR): authorized_issuance_bound SNAPSHOTS the token entry atomically under
        # the commit lock, so no concurrent consume can flip status mid-check. A token consumed during the
        # clock read, and a token consumed via the real commit path before the call, both yield False. FAILS
        # against pass-27 (stale UNUSED window) and pass-28 (live-by-reference entry, no lock).
        f = _T.GateFixture()
        d = f.gate.authorize(f.request(nonce="1" * 32), _T.evidence_bundle())
        rc = d["authorization_receipt"]; tok = rc["commit_token"]["token_id"]
        rec = {"record_type": "bssg.decision", "authorization_receipt": rc, "session_id": rc.get("session_id")}
        _o = f.gate._read_clock
        def _racing():
            f.gate.state.tokens[tok]["status"] = "CONSUMED"
            return _o()
        f.gate._read_clock = _racing
        consumed_during_clock = f.gate.authorized_issuance_bound(rec) is False
        f.gate._read_clock = _o
        # a token consumed via the real commit path (which takes the commit lock and swaps UNUSED->CONSUMED) is
        # observed CONSUMED by the snapshot -> False; an unused token is True.
        g = _T.GateFixture()
        d2 = g.gate.authorize(g.request(nonce="2" * 32), _T.evidence_bundle())
        rc2 = d2["authorization_receipt"]; tok2 = rc2["commit_token"]["token_id"]
        unused_true = g.gate.authorized_issuance_bound(d2) is True
        g.gate.state.tokens[tok2]["status"] = "CONSUMED"
        consumed_true_is_false = g.gate.authorized_issuance_bound(d2) is False
        # Kimi-A5 (lock tripwire -- retires the vacuous-sequential-probe shape Kimi-A4 flagged): the commit
        # lock is LOAD-BEARING, not decorative. Instrument _commit_lock so a token consume fires AT lock-entry
        # -- in the exact window (after the clock read, before the entry snapshot) the lock serializes. WITH the
        # lock, AIB observes CONSUMED -> False AND the lock was taken; if `with self._commit_lock` is removed,
        # the hook never fires, the snapshot reads a stale UNUSED, and AIB returns True -- so this sub-assertion
        # FAILS against a lock-removed gate (verified by in-place reversion: lock present -> (False, fired=1);
        # lock removed -> (True, fired=0)).
        h = _T.GateFixture()
        dh = h.gate.authorize(h.request(nonce="3" * 32), _T.evidence_bundle())
        rch = dh["authorization_receipt"]; tokh = rch["commit_token"]["token_id"]
        _real_lock = h.gate._commit_lock; _fired = {"n": 0}
        class _InstrLock:
            def __enter__(_s):
                _fired["n"] += 1
                h.gate.state.tokens[tokh]["status"] = "CONSUMED"   # a consume serialized BY the lock, at entry
                return _real_lock.__enter__()
            def __exit__(_s, *a):
                return _real_lock.__exit__(*a)
        h.gate._commit_lock = _InstrLock()
        try:
            lock_serialized = h.gate.authorized_issuance_bound(dh) is False and _fired["n"] >= 1
        finally:
            h.gate._commit_lock = _real_lock
        return consumed_during_clock and unused_true and consumed_true_is_false and lock_serialized

    # THE REGISTRY: (claim id, human description, probe). Adding a load-bearing retirement claim REQUIRES
    # adding an entry here AND a {claim:ID} tag in REPAIR_STATUS, or G12 fails.
    CLAIMS = [
        ("CLAIM-X7-LICENSED-EPOCH", "X7 landing is bound to the checker's tracked epoch, not marker fields; dual-field + walk-up relocation are X7", _x7_licensed_epoch),
        ("CLAIM-X7-BREADTH", "a licensed re-widen may only restore demonstrably-held authority; escalation beyond the held envelope is X7", _x7_breadth_bound),
        ("CLAIM-ABORT-CLOCKINDEP", "the abort recovers a clock-independent determinate FALSE even when the first clock read raises", _abort_clock_independent),
        ("CLAIM-KERNEL-FALSE-DOM", "kernel FALSE-domination in the abort holds for any evidence-independent conjunct via the stashed clock read", _kernel_false_dom),
        ("CLAIM-GRANT-ANCHOR", "an honest re-widen is certified ONLY when anchored to the authenticated runtime grant; the same stream is X7 unanchored", _grant_anchor),
        ("CLAIM-UNANCHORED-FAILCLOSED", "with no usable grant every marker-licensed re-widen fails closed (X7); the checker never trusts stream-derived authority", _unanchored_failclosed),
        ("CLAIM-ABORT-WITNESS-CLOCKINDEP", "the abort recovers WitnessHealthy's own determinate FALSE (inverted lease) even when the first clock read raises", _abort_witness_clockindep),
        ("CLAIM-X7-ADJ-KID", "offline X7 enforces adjudicator signature kid==adjudicator_id, mirroring the runtime", _x7_adj_kid),
        ("CLAIM-X7-RESERVED-TYPE", "a wrong-typed authority field on a reserved record-type is X7 before the reserved continue branch", _x7_reserved_wrongtype),
        ("CLAIM-ISSUANCE-BOUND-ATOMIC", "authorized_issuance_bound is a point-in-time linearization under the load-bearing commit lock: the entry is snapshotted atomically so a lock-serialized consume is observed not raced past; True is not durable past the call (runtime effect authorization is enforced at commit)", _issuance_bound_atomic),
        ("CLAIM-CLOCK", "strict clock reader on every path, no coercion", _clock_strict),
        ("CLAIM-X4-FAILCLOSED", "X4 flags a double redemption with unhashable token ids", _x4_failclosed),
        ("CLAIM-X4-FLOAT", "X4 flags a double redemption with distinct NaN float token ids", _x4_float),
        ("CLAIM-X4-NUMERIC", "X4 treats int 1 and float 1.0 as one token id", _x4_numeric_keyspace),
        ("CLAIM-X4-OUTCOME-TYPE", "X4 fails closed (no crash) on an unhashable outcome", _x4_outcome_type),
        ("CLAIM-X7-EPOCH-TYPE", "X7 fails closed on a present but wrong-typed authority_epoch", _x7_epoch_type),
        ("CLAIM-X4-SUBCLASS", "X4 materializes input; a hostile str-subclass token id cannot bypass it", _x4_subclass),
        ("CLAIM-X7-SUBCLASS", "X7 materializes input; a hostile str-subclass session_id cannot split a session", _x7_subclass),
        ("CLAIM-MARKER-EPOCH", "a marker's own authority_epoch is tamper-checked for monotonicity + consumption", _marker_epoch),
        ("CLAIM-TYPESTRICT", "bool authority_epoch does not alias int in X7 divergence", _type_strict),
        ("CLAIM-UNHASHABLE", "X7 does not raise on an unhashable nested-list element", _unhashable_total),
        ("CLAIM-A4-OMISSION", "a settlement receipt omitting its authority epoch fails closed", _a4_omission),
        ("CLAIM-A2-MARKER", "X7 carve-out arms only from an identity-bound, single-use, in-order marker", _a2_marker_bound),
        ("CLAIM-INTERVAL-COMMIT", "inverted lease refused at commit-time fresh-witness revalidation", _interval_commit),
        ("CLAIM-STRICT-MATERIALIZE", "boundaries reject subclasses/hostile accessors incl. projection sites", _strict_materialization),
        ("CLAIM-MARKER-FLOOR", "a marker installs an epoch floor; a later regression below it is X7", _marker_floor),
        ("CLAIM-TOP-SIGNATURE", "under verify, a bad top-level correction signature does not arm the carve-out", _top_signature),
    ]
    registered = set()
    for cid, desc, fn in CLAIMS:
        registered.add(cid)
        try:
            if not fn():
                failures.append("%s probe FAILED (%s)" % (cid, desc))
        except Exception as _e:
            failures.append("%s probe raised %s" % (cid, type(_e).__name__))

    # PROBE-LIVENESS META-GATE (P23-04 / K25-A11): a probe that still PASSES when the invariant it targets
    # is sabotaged is vacuous. Axis 1: sabotage the two checkers to no-ops. Axis 2 (mutation, V24): make the
    # strict materializer LENIENT (json round-trip) -- a subclass then survives, so any probe genuinely
    # depending on strict materialization at its sites must FAIL. This retires the probe-coverage-gap class
    # (a probe that stays green when a materialization site is downgraded is not covering that site).
    _VIOLATION_PROBES = {"CLAIM-X4-FAILCLOSED", "CLAIM-X4-FLOAT", "CLAIM-X4-SUBCLASS", "CLAIM-X7-SUBCLASS",
                         "CLAIM-X4-NUMERIC", "CLAIM-X4-OUTCOME-TYPE", "CLAIM-X7-EPOCH-TYPE",
                         "CLAIM-MARKER-EPOCH", "CLAIM-MARKER-FLOOR", "CLAIM-TYPESTRICT", "CLAIM-UNHASHABLE",
                         "CLAIM-A4-OMISSION", "CLAIM-A2-MARKER", "CLAIM-STRICT-MATERIALIZE", "CLAIM-TOP-SIGNATURE",
                         "CLAIM-X7-LICENSED-EPOCH", "CLAIM-X7-ADJ-KID", "CLAIM-X7-RESERVED-TYPE", "CLAIM-X7-BREADTH",
                         "CLAIM-GRANT-ANCHOR", "CLAIM-UNANCHORED-FAILCLOSED"}
    _real_ah, _real_sr = _BG.check_authority_history, _BG.check_single_redemption
    try:
        _BG.check_authority_history = lambda *a, **k: []
        _BG.check_single_redemption = lambda *a, **k: []
        for cid, desc, fn in CLAIMS:
            try:
                still_passes = bool(fn())
            except Exception:
                still_passes = False
            # CLAIM-UNHASHABLE is a totality probe (asserts a list is returned), legitimately survives no-op.
            if still_passes and cid in (_VIOLATION_PROBES - {"CLAIM-UNHASHABLE"}):
                failures.append("VACUOUS-PROBE: %s passes against a no-op checker" % cid)
    finally:
        _BG.check_authority_history, _BG.check_single_redemption = _real_ah, _real_sr
    # Axis 2: mutation of the strict materializer -> the site-coverage probe must fail.
    _real_strict = _BG._strict_copy
    try:
        _BG._strict_copy = _BG._safe_copy   # downgrade to lenient json round-trip
        for cid, desc, fn in CLAIMS:
            if cid != "CLAIM-STRICT-MATERIALIZE":
                continue
            try:
                still_passes = bool(fn())
            except Exception:
                still_passes = False
            if still_passes:
                failures.append("MUTATION-SURVIVED: %s green with lenient materialization (site not covered)" % cid)
    finally:
        _BG._strict_copy = _real_strict
    # Axis 3 (K26-VF-1): mutation of the strict clock reader -> a coercing _read_clock (int(self.clock()))
    # must make the behavioral CLAIM-CLOCK probe FAIL. A probe that stays green when the clock is downgraded
    # to coercion is not behaviorally covering the clock -- the exact source-grep false-green Kimi surfaced.
    _real_read_clock = _BG.BSSGGate._read_clock
    try:
        def _coercing_read_clock(self):
            _v = self.clock()
            try:
                return int(_v)
            except Exception:
                return 0
        _BG.BSSGGate._read_clock = _coercing_read_clock
        for cid, desc, fn in CLAIMS:
            if cid != "CLAIM-CLOCK":
                continue
            try:
                still_passes = bool(fn())
            except Exception:
                still_passes = False
            if still_passes:
                failures.append("MUTATION-SURVIVED: CLAIM-CLOCK green with a coercing clock reader (probe is not behavioral)")
    finally:
        _BG.BSSGGate._read_clock = _real_read_clock


    try:
        status = open(os.path.join(HERE, "REPAIR_STATUS.md")).read()
        ce_src = open(os.path.join(HERE, "bssg_counterexamples.py")).read()
        # A12 (K25-A12) + V29 (Kimi positional-extraction fix): the CURRENT claim surface is the section with
        # the HIGHEST pass NUMBER, selected semantically -- NOT "whatever heading is physically first". A section
        # appended at the bottom, or a reordered file, can no longer mis-select a stale section as current. The
        # current section runs from the newest heading to the next heading in FILE ORDER after it (or EOF).
        _heads = [(int(m.group(1)), m.start()) for m in re.finditer(r"# BSSG v0\.1 -- Repair Status \(pass-(\d+)", status)]
        if _heads:
            _newest_n = max(n for n, _ in _heads)
            _newest_start = min(pos for n, pos in _heads if n == _newest_n)   # defensive: dup pass numbers -> first
            _later = [pos for _, pos in _heads if pos > _newest_start]
            current = status[_newest_start:(min(_later) if _later else len(status))]
        else:
            current = status
        tagged = set(re.findall(r"\{claim:([A-Z0-9-]+)\}", current))
        # (2) orphan probe: a registered claim with no tag in REPAIR_STATUS.
        for cid in registered - tagged:
            failures.append("REGISTERED-BUT-UNTAGGED: " + cid)
        # (3) coverage completeness: a tagged load-bearing claim with no registered probe.
        for cid in tagged - registered:
            failures.append("TAGGED-BUT-UNREGISTERED (no probe): " + cid)
        # (4) cited CE ids (any digit count) must exist.
        cited = set(re.findall(r"CE(\d+)", current))
        defined = set(re.findall(r'record\("CE(\d+)"', ce_src))
        for c in sorted(cited - defined):
            failures.append("CITED-CE-MISSING: CE" + c)
        # only the newest pass section is the CURRENT claim surface (older sections are historical record).
        # (5) numeric corpus claim: the CANONICAL "claims <N> counterexamples" statement must match.
        actual_ce = len(defined)
        for n in re.findall(r"claims (\d+) counterexamples", current):
            if int(n) != actual_ce:
                failures.append("NUMERIC-CE-CLAIM %s != actual %d" % (n, actual_ce))
        # (6) ROOT FIX (GPT-P21-03 / K21-A1/A3/A9 -- the false-prose-claim shape). Any load-bearing
        # REMEDY or COMPLETENESS assertion in the CURRENT pass section must be anchored: on a line that
        # carries a {claim:ID} tag (mechanically probed) OR an explicit (UNVERIFIED) marker. DECLARED
        # PARTIAL (GLM-04): this is a blocklist heuristic and cannot catch every phrasing of an overclaim;
        # it is a tripwire that raises the cost of the most common completeness/remedy assertions, not a
        # guarantee. The positive discipline (a load-bearing claim must be a registered {claim:ID}) is the
        # real control; this scan is a secondary net.
        ASSERT_RE = re.compile(r"(closes it|does not reach|class-complete|retires the whole class|"
                               r"covers every|is complete across|guarantees|fully retired|"
                               r"cannot recur|eliminates the|solves the whole|handles all|closes the gap)",
                               re.IGNORECASE)
        for ln in current.splitlines():
            if ASSERT_RE.search(ln) and "{claim:" not in ln and "(UNVERIFIED)" not in ln:
                failures.append("UNANCHORED-LOAD-BEARING-CLAIM: " + ln.strip()[:70])
    except Exception as _e:
        failures.append("registry/citation check raised %s" % type(_e).__name__)

    record("G12", "PASS" if not failures else "FAIL",
           "every registered load-bearing claim (%d) has a passing probe and a REPAIR_STATUS tag; cited CEs exist"
           % len(registered) if not failures else "claim-substrate mismatch: " + " | ".join(failures))


def gate_g13():
    # V27-Kimi (K28-VF-1): the verifier must EXECUTE the counterexample corpus, not merely count record("CE…")
    # definitions in the source (G12). A copy with a RED counterexample previously still verified 0 FAIL because
    # nothing here ran the corpus.
    # V28-Kimi (Kimi-A6): the verifier must not TRUST the corpus's self-reported "N/M GREEN" summary line. This
    # gate now INDEPENDENTLY counts the per-CE result lines it actually observes (each record() prints exactly
    # one "GREEN <cid> …" or "RED   <cid> …"), derives the verdict from those observed lines, and cross-checks
    # the self-reported summary against the independent count -- a corpus whose summary lied about its totals (or
    # truncated mid-run while printing a hardcoded/miscomputed summary) FAILS on the mismatch, not silently.
    proc = subprocess.run([sys.executable, "bssg_counterexamples.py"], cwd=HERE, capture_output=True, text=True)
    output = proc.stdout + proc.stderr
    if proc.returncode != 0:
        record("G13", "FAIL", "counterexample corpus did not execute cleanly (exit %d)" % proc.returncode)
        return
    # INDEPENDENT count: per-CE lines anchored to line-start (detail text cannot spoof these).
    green_lines = re.findall(r"^GREEN\s+(CE\d+)\b", output, re.MULTILINE)
    red_lines = re.findall(r"^RED\s+(CE\d+)\b", output, re.MULTILINE)
    green_obs, red_obs = len(green_lines), len(red_lines)
    ids = green_lines + red_lines
    uniq = set(ids)
    if red_obs != 0:
        record("G13", "FAIL", "counterexample corpus emitted %d RED CE line(s) (independent count); open defects present" % red_obs)
        return
    if green_obs == 0:
        record("G13", "FAIL", "counterexample corpus emitted no GREEN CE lines (independent count); corpus did not run")
        return
    if len(uniq) != len(ids):
        record("G13", "FAIL", "counterexample corpus emitted a duplicate CE id (independent count): %d lines, %d unique" % (len(ids), len(uniq)))
        return
    # CROSS-CHECK the self-reported summary against the independent observation (do not trust it as the source).
    m = re.search(r"(\d+)/(\d+) GREEN\s+\((\d+) RED", output)
    if m is None:
        record("G13", "FAIL", "counterexample corpus produced no GREEN/RED summary line")
        return
    rep_green, rep_total, rep_red = int(m.group(1)), int(m.group(2)), int(m.group(3))
    if (rep_green, rep_total, rep_red) != (green_obs, green_obs, 0):
        record("G13", "FAIL", "corpus self-report %d/%d GREEN (%d RED) disagrees with independent count %d/%d GREEN (0 RED)"
               % (rep_green, rep_total, rep_red, green_obs, green_obs))
        return
    record("G13", "PASS", "counterexample corpus EXECUTED: %d/%d GREEN, 0 RED (independently counted; self-report matches)" % (green_obs, green_obs))
    return green_obs


def main():
    print("BSSG v0.1 DRAFT package verifier")
    print("Package directory: %s" % HERE)
    print("-" * 72)
    # F-GPT-P10-05: the verifier is TOTAL -- any gate that raises (e.g. a missing manifest-bound file)
    # records FAIL and the run proceeds to the summary rather than escaping mid-way.
    for _g in (gate_g1, gate_g2, gate_g3, gate_g4, gate_g5, gate_g6,
               gate_g7, gate_g8, gate_g9, gate_g10, gate_g11, gate_g12, gate_g13):
        try:
            _g()
        except Exception as _e:
            record(_g.__name__.replace("gate_g", "G").upper(), "FAIL",
                   "gate raised %s on non-total input (e.g. a missing manifest-bound file)"
                   % type(_e).__name__)
    print("-" * 72)
    fails = [r for r in results if r[1] == "FAIL"]
    warns = [r for r in results if r[1] == "WARN"]
    print(
        "SUMMARY: %d gates, %d PASS, %d WARN, %d FAIL"
        % (len(results), len(results) - len(warns) - len(fails), len(warns), len(fails))
    )
    if fails:
        print("PACKAGE STATUS: INCONSISTENT (draft retained, do not package)")
        return 1
    print("PACKAGE STATUS: SELF-CONSISTENT DRAFT (not carried, not publication ready)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

---

# Bismillah ir-Rahman ir-Rahim
