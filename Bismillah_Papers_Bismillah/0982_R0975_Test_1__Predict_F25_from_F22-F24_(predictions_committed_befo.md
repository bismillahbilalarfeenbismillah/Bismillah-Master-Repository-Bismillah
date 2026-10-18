# Bismillah ir-Rahman ir-Rahim

# R0975 -- Test 1: Predict F25 from F22-F24 (predictions committed before reveal)

**Chronological Index:** 982 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** test1_F25_predictions.md  
**Source Format:** md  
**SHA-256:** `5f66f0043e41bc7356d0bf3798915dbb64b2e6c29285e73f7d6bd17b509f114d`  

---

## R0975 · Test 1: Predict F25 from F22-F24 (predictions committed before reveal)

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: test1_F25_predictions.md
- source_format: md
- text_sha256: 5f66f0043e41bc7356d0bf3798915dbb64b2e6c29285e73f7d6bd17b509f114d

# Test 1: Predict F25 from F22-F24 (predictions committed before reveal)

## Input visible to predictor (F22-F24 only)

| F | step | code | layer | scope | fix |
|---|---|---|---|---|---|
| F22 | 2-3 dispatch | CASM-V-001 | verifier_dispatch | whitelist_alignment | 21 LOC python |
| F23 | 4 install | CASM-V-021 | ci_install_matrix | extras_gap | 1 LOC yaml |
| F24 | 4 import | CASM-V-021 | sigstore_api_drift | api_path_drift | 3 LOC python |

## Structural regularities observed (R1-R6)

**R1 (Failure-mode shift).** Each fix unblocks the next step. F22 fix
unblocked step 4; F23 fix unblocked the import within step 4; F24 fix
will unblock whatever comes after step 4.

**R2 (Step monotonicity).** Steps visited: 2-3, 4, 4. Non-decreasing.
The next finding will be at step 4 or later.

**R3 (Error-code locality).** F23 and F24 share CASM-V-021 (both at
step 4). If the next finding is at a different step, expect a different
error code.

**R4 (Fix-size bimodality).** Fixes so far: 21 LOC (medium), 1 LOC
(small), 3 LOC (small). Two size classes.

**R5 (Sigstore as substrate).** F22 and F24 involve sigstore-specific
semantics. The dependency is a persistent finding source.

**R6 (Step exhaustion).** Two consecutive findings at step 4 (F23, F24).
Double-occupancy suggests step 4's finding surface is exhausted. The
next finding should be at step 5 or later.

## Predictions (committed)

| Dimension | Prediction | Confidence |
|---|---|---|
| **P1 Step** | **step 6** (primary bet). Step 5 is bytes-IO serialization, less likely to fail on this fixture. Step 6 (identity/policy verification) is the next substantive logic step. | HIGH |
| **P2 Error code** | **CASM-V-032 or CASM-V-035**. New step implies new error-code prefix per R3. CASM-V-03x is the identity-verification range. | MEDIUM |
| **P3 Substrate layer** | **policy_construction OR sigstore_verify_call**. Per R5, sigstore semantics are a persistent source. The identity policy layer is the step-6 substrate. | MEDIUM |
| **P4 Fix-size class** | **one_word or few_lines**. Per R4 bimodality, the next fix is either small (1-3 LOC) or medium (20-30 LOC). The corrective-ship pattern favors small. | MEDIUM |
| **P5 Root cause** | **"policy doesn't match OIDC token's claims (literal vs regex, or wrong workflow path)"**. Ambient-OIDC identity policies commonly fail on literal/regex mismatches against GitHub Actions claims. The step-6 identity check compares the policy's expected identity against the OIDC token's actual claims. | MEDIUM |

## Ablation note

P5's literal-vs-regex prediction is plausibly derivable from LLM
training data on OIDC failure modes without the audit chain. P1's
step-6 localization is chain-derived (R2 + R6). The ablation control
must separate these contributions.

---

# Bismillah ir-Rahman ir-Rahim
