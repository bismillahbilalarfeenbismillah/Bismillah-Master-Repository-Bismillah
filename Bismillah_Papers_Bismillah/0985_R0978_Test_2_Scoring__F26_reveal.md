# Bismillah ir-Rahman ir-Rahim

# R0978 -- Test 2 Scoring: F26 reveal

**Chronological Index:** 985 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** test2_F26_scoring.md  
**Source Format:** md  
**SHA-256:** `ca5a8623a1076efa95574feb4e3f79b7e57d790e227878dd7d4a6213cfecbcab`  

---

## R0978 · Test 2 Scoring: F26 reveal

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: test2_F26_scoring.md
- source_format: md
- text_sha256: ca5a8623a1076efa95574feb4e3f79b7e57d790e227878dd7d4a6213cfecbcab

# Test 2 Scoring: F26 reveal

## Ground truth (from round_33_audit_for_claude.md, F26 row in CSV)

| field | value |
|---|---|
| step | step_8_surface |
| error_code | unhandled SyntaxError (CASM-V-XXX pending assignment in v0.11.7) |
| substrate_layer | extractor_dispatch |
| scope_class | wrong_language_dispatch |
| fix_size | ~30 LOC (dispatch table addition) |
| root_cause | extract_public_surface dispatches all files to Python ast.parse with no extension routing |
| fix_location | `surface_extraction.py` (Python substrate, NOT yaml workflow) |

## Scoring against predictions

| Dim | Predicted | Actual | Score | Notes |
|---|---|---|---|---|
| **P1 Step** | step 8 (primary bet, "step 7 or 8") | step 8 | **HIT** | Exact, primary bet |
| **P2 Code** | "unhandled SyntaxError from Python's ast.parse" | unhandled SyntaxError from ast.parse | **HIT** | Exact mechanism named |
| **P3 Layer** | extractor_dispatch | extractor_dispatch | **HIT** | Exact term |
| **P4 Fix size** | ~30 LOC dispatch table addition | ~30 LOC dispatch table addition | **HIT** | Exact size class and shape |
| **P5 Root cause** | "dispatches all files to Python ast.parse without routing by extension; rust source raises SyntaxError" | "extract_public_surface dispatches all files to Python ast.parse with no extension routing" | **HIT** | Verbatim-level match |

## Aggregate

**5 of 5 dimensions = HIT. Test 2 = TIGHT (≥3/5 HIT pre-registered threshold).**

## Combined results across both tests

| | P1 | P2 | P3 | P4 | P5 | Verdict |
|---|---|---|---|---|---|---|
| Test 1 (predict F25 from F22-F24) | HIT | HIT | HIT | HIT | HIT | TIGHT |
| Test 2 (predict F26 from F22-F25) | HIT | HIT | HIT | HIT | HIT | TIGHT |
| **Overall** | **2/2** | **2/2** | **2/2** | **2/2** | **2/2** | **10/10 HIT** |

## Honest interpretation

10/10 is suspiciously good for a real experiment. The honest reading is:

1. **The predictor is the same instance that has access to the audit-chain memos
   themselves**, which describe these findings. Even though the predictions were
   committed before the scoring memos were re-read for ground truth, this run cannot
   prove "audit-chain history alone, fed to a clean LLM, predicts the next finding."
   It can only prove "audit-chain structure has predictive regularities." That is a
   weaker but still publishable claim.

2. **The 5-dimension scoring is generous on P4 and P5.** Fix-size class (one_word,
   few_lines, ~30_lines) has only 4 buckets; coarse predictions easily HIT. Root-cause
   one-liners in this experiment are scored on whether the named mechanism appears in
   the prediction, not whether the prediction also rules out alternatives.

3. **A real Phase 1 paper experiment requires:**
   - A different LLM instance (different model, different vendor) with NO context from
     the audit memos themselves, fed only the structured CSV.
   - The ablation control (same LLM, no audit-chain history, just repo skeleton).
   - At least 10 findings, ideally 20+, for any frequentist claim.
   - Pre-registration on OSF or similar before scoring.

4. **What this DOES validate:** the audit-chain has structural regularities (R1-R11)
   that are genuinely extractable. Failure-mode shift, step monotonicity, cross-language
   seam recurrence, and error-code locality are real properties of THIS corpus. A
   future predictor — human or machine — equipped with these regularities is plausibly
   more accurate than one without them.

5. **What this DOES NOT validate:** that the audit-chain log alone (without LLM training
   on Sigstore + AST patterns) suffices. The ablation question is open.

## Pre-registered verdict

**The 90-minute experiment validates premise on the smallest possible corpus, with
caveats.** The premise being "audit-chain history contains extractable regularities
that materialize in subsequent findings." It does NOT yet validate the stronger claim
that "an LLM-as-predictor conditioned on this chain meaningfully outperforms an
unconditioned LLM," which requires the cross-instance ablation from the Phase 1 paper
protocol.

## Recommendation to project lead

Treat this as a **pilot**. Document it honestly in the Phase 1 paper as the pilot that
generated the structural regularities R1-R11, NOT as the experiment itself. The actual
experiment must be run on a different instance with proper controls, and ideally on a
larger corpus once the structured log is published on Zenodo and other audit chains
(Bayyinah's, your Furqan-lint history pre-F22) are normalized into the same schema.

The pilot's value is that it forces R1-R11 onto paper, which is the actual seed for a
Phase 1 method section.

---

# Bismillah ir-Rahman ir-Rahim
