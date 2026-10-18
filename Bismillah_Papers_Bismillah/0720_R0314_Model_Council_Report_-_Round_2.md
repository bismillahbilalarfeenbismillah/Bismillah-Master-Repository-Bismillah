# Bismillah ir-Rahman ir-Rahim

# R0314 -- Model Council Report - Round 2

**Chronological Index:** 720 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** model-council-gemini_3_1_pro-r2.md  
**Source Format:** md  
**SHA-256:** `509f3fb2149260d8a954ca94f8d10c2b5d12a093de3bab5355db1e9ae7b1d46a`  

---

## R0314 · Model Council Report - Round 2

- section: V. BSSG & SHVVP Protocols
- source_file: model-council-gemini_3_1_pro-r2.md
- source_format: md
- text_sha256: 509f3fb2149260d8a954ca94f8d10c2b5d12a093de3bab5355db1e9ae7b1d46a

# Model Council Report - Round 2

**Model:** Gemini 3.1 Pro

## 1. Command Outputs (Verbatim/Counts Preserved)

**Command:** `sha256sum -c SHA256SUMS`
```text
ATTACK_AND_FALSIFIER_REGISTER.md: OK
BSSG_v0_1_CANONICAL_SPEC_DRAFT.pplx.md: OK
BSSG_v0_1_DECISION_REGISTER.md: OK
BSSG_v0_1_MODEL_COUNCIL_SYNTHESIS.pplx.md: OK
OPEN_DECISIONS.md: OK
README.md: OK
REPAIR_STATUS.md: OK
REQUIREMENTS_TRACEABILITY.md: OK
bssg_attest.py: OK
bssg_counterexamples.py: OK
bssg_gate.py: OK
bssg_model_check.py: OK
schemas/authorization-receipt.schema.json: OK
schemas/correction-event.schema.json: OK
schemas/effect-request.schema.json: OK
schemas/execution-receipt.schema.json: OK
schemas/lineage-record.schema.json: OK
schemas/witness-receipt.schema.json: OK
test_bssg_gate.py: OK
verify_bssg_v0_1.py: OK
```

**Command:** `python3 test_bssg_gate.py`
```text
Ran 345 tests in 0.065s
OK (skipped=8)
```

**Command:** `python3 bssg_counterexamples.py`
```text
175/175 GREEN  (0 RED = open defects)
```

**Command:** `python3 bssg_model_check.py`
```text
MODEL CHECK: PASS -- kernel(243) + antitone(729) + bounded-auth-intro(11110 schedules) + operational refinement on the executable
```

**Command:** `python3 verify_bssg_v0_1.py`
```text
SUMMARY: 14 gates, 12 PASS, 2 WARN, 0 FAIL
PACKAGE STATUS: SELF-CONSISTENT DRAFT (not carried, not publication ready)
BSSG reference gate 0.1.0-draft, spec version 0.1
DRAFT / NOT CARRIED. No effectiveness claim is made by this software.
```

**Command:** `python3 bssg_gate.py`
```text
BSSG reference gate 0.1.0-draft, spec version 0.1
DRAFT / NOT CARRIED. No effectiveness claim is made by this software.
```

## 2. Independent A-05 Probe

**Verdict:** REPRODUCED

**Methodology:** I wrote an independent probe (`my_a05_probe.py`) that uses a monkey-patched `token_factory` to inject a simulated exception precisely into the `ceiling_for_health` call at the post-mint `contract_ceiling` write branch. The probe demonstrates that:
1. `R1` (HEALTHY READ) succeeds, but the exception causes `contract_ceiling` for the session to remain absent.
2. `R2` (DEGRADED READ) and `R3` (HEALTHY DELETE) are executed. `R3` terminalizes the session (`DENY_FALSE` via `E-AUTHORITY-WIDENING`).
3. An amendment lifts the terminal state.
4. `R4` (HEALTHY DELETE) requests an effect the session never held. Because `contract_ceiling` was absent during the lift, the restored grant is empty. The `_apply_narrowing` widening guard (`_held is None`) is bypassed, and the effect is ALLOWED and successfully committed.

**Probe JSON Output:**
```json
{
  "R1": "ALLOW",
  "contract_ceiling_absent": true,
  "R2": "ALLOW",
  "R3": "DENY_FALSE",
  "LIFT": true,
  "R4": "ALLOW",
  "COMMIT": "COMMITTED_PENDING_OUTCOME",
  "VERDICT": "REPRODUCED"
}
```

## 3. Adjudication of A-06 (Retroactive Edit Signature)

**Verdict:** REPRODUCED

**Methodology:** I manually inspected `REPAIR_STATUS.md` around line 66 (the pass-34 sealed block). The text literally reads:
`**Battery state (repair34 resealed):** 345 tests OK -- 173/173 CE GREEN ...`
followed immediately on line 70 by:
`This document claims 175 counterexamples.`

This is a blatant integrity violation. A hash-sealed block reporting 173 passing counterexamples cannot simultaneously claim 175 counterexamples. The presence of the 175 count within the pass-34 historical section constitutes a retroactive edit signature. This violates PMD v1.2 audit continuity rules.

## 4. Code-Spec Consistency Check

**Verdict:** MISMATCH DETECTED

**Analysis:** Spec Section 22.2 explicitly declares: *"An armed forward re-widen licensed by an accepted amendment is UNCERTIFIABLE offline (X7U) -- the runtime grant is caller-supplied (WithinAuth of its supplier) and cannot discharge the license under evidence-independence (SHV Axiom 5)"*.

However, the shipped `bssg_gate.py` behavior at ~L1830 specifically captures and caches the full `contract_ceiling` in the gate's internal state. Upon a terminal lift, `submit_amendment` uses this internal gate state (`_rc = self.state.contract_ceiling.get(session)`) to derive the restored `amendment_grants`.

**The Mismatch:** The code generates the runtime grant directly from its own internal enforcement-point cache, directly contradicting the specification's load-bearing claim that the grant is caller-supplied and therefore offline-uncertifiable.

## 5. NEW Defect (34th Instance)

**Vulnerability Class:** Authority Widening Bypass via Degraded-First Establishment
**Severity:** CRITICAL

**Description:**
The gate correctly defers the `contract_ceiling` write to the post-mint phase, but restricts it strictly via the condition `health == "HEALTHY"` (L1830). If a session's first successful authorization is made with `DEGRADED` health, the `contract_ceiling` write is skipped and remains permanently absent for that session.

If this session later terminalizes (e.g., via a legitimate `HEALTHY` request attempting a widening), and is lifted by a valid amendment, `submit_amendment` reads the absent `contract_ceiling` and generates an empty restored grant. The subsequent request to re-establish authority will hit `_apply_narrowing`, observe `_held is None`, and completely bypass the `E-AUTHORITY-WIDENING` check. The session will cleanly establish the full `HEALTHY` ceiling, allowing it to commit effects (e.g., `DELETE`) it had never legitimately held prior to the terminal state.

**Reachability:** Native. This is the exact same architectural bypass as A-05 and F-GS-1, but triggered entirely through protocol-valid `DEGRADED` inputs without requiring any exceptions or mint faults.

## 6. Final Verdict

**Verdict:** HALT

Because the gate fails to securely isolate `contract_ceiling` initialization (A-05 and the new 34th instance bypass), and because A-06 proves the integrity of the pass-34 ledger was compromised, the two-consecutive-clean-rounds premise required by PMD §0.4 cannot be met.

---

# Bismillah ir-Rahman ir-Rahim
