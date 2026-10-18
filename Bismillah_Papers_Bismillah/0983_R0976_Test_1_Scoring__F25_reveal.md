# Bismillah ir-Rahman ir-Rahim

# R0976 -- Test 1 Scoring: F25 reveal

**Chronological Index:** 983 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** test1_F25_scoring.md  
**Source Format:** md  
**SHA-256:** `49a6e5dac19d1b128fc59d9b40a23c1f684287452a23da822d330c5cf08b0c53`  

---

## R0976 · Test 1 Scoring: F25 reveal

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: test1_F25_scoring.md
- source_format: md
- text_sha256: 49a6e5dac19d1b128fc59d9b40a23c1f684287452a23da822d330c5cf08b0c53

# Test 1 Scoring: F25 reveal

## Ground truth (from round_32_audit_for_claude.md, F25 row in CSV)

| field | value |
|---|---|
| step | step_6_identity |
| error_code | CASM-V-032 |
| substrate_layer | policy_construction |
| scope_class | literal_vs_regex |
| fix_size | 1 LOC (yaml) |
| root_cause | smoke-test workflow built Identity policy with regex method when policy expects literal method |
| fix_location | `.github/workflows/ci.yml` (NOT verification.py) |

## Scoring against predictions

| Dim | Predicted | Actual | Score | Notes |
|---|---|---|---|---|
| **P1 Step** | step 6 (primary bet) | step 6 | **HIT** | Exact |
| **P2 Code** | CASM-V-032 or CASM-V-035 | CASM-V-032 | **HIT** | First named candidate |
| **P3 Layer** | policy_construction OR sigstore_verify_call | policy_construction | **HIT** | First named candidate |
| **P4 Fix size** | one_word or few_lines | one_word (1 LOC yaml) | **HIT** | |
| **P5 Root cause** | "policy doesn't match OIDC token's claims (literal vs regex, or wrong workflow path)" | "Identity policy built with regex method when literal expected" | **HIT** | "literal vs regex" named explicitly in prediction |

## Aggregate

**5 of 5 dimensions = HIT. Test 1 = TIGHT (≥3/5 HIT pre-registered threshold).**

## Why this happened (post-hoc, not used to re-score)

The structural regularities R1-R6 are all repository-empirical, not training-data-derived:
- R1 and R2 (failure-mode shift, step monotonicity) come from observing the 3 prior rows
- R5 (sigstore as substrate) comes from observing F23+F24
- R6 (step-4 exhausted, look at step 5/6) comes from R2 + observing both F23 and F24 at step 4

But P5 (the literal-vs-regex specific guess) is plausibly LLM-prior driven: the predictor
knows from training data that ambient-OIDC identity policies often fail on literal/regex
mismatches against GitHub Actions claims. This is exactly the failure mode the ablation
control is designed to isolate. **Without the ablation, we cannot claim the audit chain
did the load-bearing work for P5.**

## Ablation control (run with audit-chain log REMOVED)

Cold-start prompt: "furqan-lint v0.11.5 ships an al-Bayyina corrective fixing a
sigstore-python TrustedRoot import path drift in step 4 of an 8-step verifier. The
gate11-rust-smoke-test job in CI is still red after the v0.11.5 ship. What do you
predict the next failing step and error are?"

Without F22-F24 history, plausible cold-start guesses:
- "Sigstore signing fails because the workflow's OIDC token isn't being acquired" — MISS (signing succeeds)
- "Public-surface comparison fails because Rust source can't be parsed by Python AST" — this would be **F26**, not F25 (predicted two layers ahead)
- "Identity policy fails on literal-vs-regex" — possible HIT on P1, P2, P3, P4, P5

The ablation is genuinely uncertain on P5 alone, because LLM training data covers
ambient-OIDC failure modes well. But the audit-chain history strongly conditions
P1/P2/P3 (step 6 specifically, CASM-V-032 specifically, the literal-vs-regex framing)
through R2 (step monotonicity from 4) and R3 (error-code locality).

**Honest interim verdict for the paper:** the audit chain is contributing meaningfully
to localization (which step, which code) but cannot be definitively credited with the
specific root-cause guess on P5 without a real ablation run on a different model
instance with no shared context. The paper must run this ablation properly, not by
self-report.

---

# Bismillah ir-Rahman ir-Rahim
