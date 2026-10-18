# Bismillah ir-Rahman ir-Rahim

# R0329 -- BSSG gate -- repair status (repair pass 14: V12 audit; API-surface totality + spec/code reconciliation)

**Chronological Index:** 727 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** REPAIR_STATUS.md  
**Source Format:** md  
**SHA-256:** `f7f15a2c25bb4204a50366f47687f8c6c82adc09c6976aa0c633e6eab13ba518`  

---

## R0329 · BSSG gate -- repair status (repair pass 14: V12 audit; API-surface totality + spec/code reconciliation)

- section: V. BSSG & SHVVP Protocols
- source_file: REPAIR_STATUS.md
- source_format: md
- text_sha256: f7f15a2c25bb4204a50366f47687f8c6c82adc09c6976aa0c633e6eab13ba518

# BSSG gate -- repair status (repair pass 14: V12 audit; API-surface totality + spec/code reconciliation)

The V12 round: a confirmed GLM-5.2 seat returned 2 MAJOR (no blocker) and GPT-5.6 returned HALT (3
BLOCKER, 1 MAJOR). Both executed; attestations matched V12. Crucially, GPT respected the pass-13 threat
boundary -- every finding is a DIRECT API call, not gate.state mutation -- and found real holes INSIDE
the API surface. Both seats CONVERGED on the most important one: a spec/code contradiction the producer
introduced in pass 13. All findings reproduced on canonical bytes; all are fixed.

## Fixed this pass (85/85 counterexamples; 339 tests; model-check PASS; verifier green post-regen)
- SPEC/CODE RECONCILIATION [F-BSSG-P12-01 BLOCKER / GLM-F2 MAJOR]: pass 13 documented that an aborted
  authorize does not consume the nonce and that DENY_UNKNOWN is non-terminal -- but the code consumed
  the nonce before evaluation and terminalized every non-ALLOW snapshot. FIXED to match the (correct)
  documented semantics: an aborted authorize now ROLLS BACK its nonce (a transient-fault retry of the
  identical request is a fresh evaluation, not a replay); and ONLY a determinate DENY_FALSE terminalizes
  the snapshot -- no DENY_UNKNOWN path (main eval or malformed-evidence) terminalizes, so a later
  distinct request may still ALLOW once evidence arrives. Spec 6.3 refined to state both nonce rules
  precisely.
- INPUT SNAPSHOT INSIDE THE GUARD [F-BSSG-P12-03 BLOCKER]: _safe_copy ran BEFORE the lock/reentrancy
  guard, so json.dumps invoking a dict-subclass items() hook could run a nested gate op unguarded. The
  snapshot now happens INSIDE the lock, after the guard is set; a hook fired during snapshotting is
  refused as E-REENTRANT-CALL.
- COMMIT token_id TOTALITY [F-BSSG-P12-02 BLOCKER]: commit snapshotted execution_binding and evidence
  but not token_id; a str subclass with a malicious __hash__ escaped through the lookup (and the abort
  repeated the unsafe lookup). commit now requires type(token_id) is str BEFORE any lookup, and the
  abort path never performs an unsafe lookup. This was a direct-API totality gap (in model), now closed.
- AMENDMENT ABORT RECORDED [GLM-F1 MAJOR]: the submit_amendment abort returned without recording; it now
  appends a bssg.correction-outcome to the audit trail, symmetric with authorize and commit aborts.
- README ACCURACY [F-BSSG-P12-04 MAJOR]: stale cached numbers corrected (SHOULD 9 -> 10; "16 files" ->
  20) to match the sealed verifier and SHA256SUMS.

## Standing / governance
Both V12 seats VALID (GLM confirmed GLM-5.2), converging on the spec/code contradiction -- which was the
producer's own pass-13 error (documenting a semantics the code did not implement). The lesson: a boundary
written into the spec must be verified against the code. GPT worked strictly inside the API surface,
confirming the pass-13 scoping held. DRAFT / NOT CARRIED.

---

# Bismillah ir-Rahman ir-Rahim
