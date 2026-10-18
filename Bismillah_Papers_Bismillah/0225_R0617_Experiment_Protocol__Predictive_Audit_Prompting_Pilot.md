# Bismillah ir-Rahman ir-Rahim

# R0617 -- Experiment Protocol: Predictive Audit Prompting Pilot

**Chronological Index:** 225 of 995  
**Date:** 2026-05-08  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** experiment_protocol.md  
**Source Format:** md  
**SHA-256:** `c0d9d8dfb39050fece6266d345812e4fc23f5641415dbb5dd61b1c0628584583`  

---

## R0617 · Experiment Protocol: Predictive Audit Prompting Pilot

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: experiment_protocol.md
- source_format: md
- text_sha256: c0d9d8dfb39050fece6266d345812e4fc23f5641415dbb5dd61b1c0628584583

# Experiment Protocol: Predictive Audit Prompting Pilot

**Pre-registered before predictions were committed.**
**Date:** 2026-05-08
**Author:** Bilal Syed Arfeen, BayyinahEnterprise

---

## 1. Objective

Determine whether structural regularities in the audit-chain log
(F22-F26) enable prediction of future findings on five dimensions.

## 2. Sub-Chain Selection

The F22-F26 chain from the Gate 11 Sigstore-CASM verifier pipeline
(furqan-lint v0.11.2 through v0.11.6) was selected because:

1. It is a single failure-mode sequence (unambiguous causal chain).
2. All findings have complete six-element documentation.
3. The 8-step pipeline provides a natural categorical target.

## 3. Scoring Dimensions

Five dimensions, scored independently per test:

| Dim | Name | Type | HIT Criterion |
|---|---|---|---|
| P1 | Failing step | Categorical (8 classes) | Predicted step matches actual step |
| P2 | Error code | Open categorical | Predicted code matches actual code (first-named candidate counts) |
| P3 | Substrate layer | Open categorical | Predicted layer matches actual layer (first-named candidate counts) |
| P4 | Fix-size class | Ordinal (4 classes: one_word, few_lines, ~30_lines, 100+) | Predicted class matches actual class |
| P5 | Root cause | Free text | Predicted mechanism appears in ground-truth description |

## 4. Threshold

A test is **TIGHT** if >= 3 of 5 dimensions score HIT.
A test is **LOOSE** if < 3 of 5 dimensions score HIT.

This threshold was set before any predictions were made.

## 5. Predict-Then-Reveal Procedure

For each test:

1. The predictor receives the structured log for F22 through
   F(N-1) only. The ground-truth document for F(N) is not read.
2. The predictor commits predictions on all five dimensions in
   a markdown document. The document is saved before proceeding.
3. The ground-truth scoring document for F(N) is read.
4. Each dimension is scored as HIT or MISS by comparing the
   committed prediction against ground truth.
5. The aggregate is computed and compared to the TIGHT threshold.

## 6. Tests

**Test 1:** Predict F25 from F22-F24 (3 findings as input).
**Test 2:** Predict F26 from F22-F25 (4 findings as input,
including F25's revealed ground truth from Test 1).

## 7. Predictor Disclosure

The predictor is a Claude instance (Anthropic Claude Opus 4)
that participated in the audit chain from which the findings
are drawn. The predictor's context includes audit memos from
rounds 28-33. This shared context is a known limitation.

The Phase 2 ablation study (separate protocol) will use a
different LLM instance from a different vendor with no shared
context.

## 8. Scoring Rules

- When the prediction names multiple candidates (e.g., "CASM-V-032
  or CASM-V-035"), the first-named candidate is scored. If the
  first-named candidate matches, the dimension scores HIT.
- P4's four-class granularity (25% random baseline) is noted
  as a limitation in the paper.
- P5 is scored on whether the predicted mechanism appears in the
  ground-truth description, not on whether alternatives are
  excluded. This is noted as generous scoring in the paper.

## 9. Pre-Registration Statement

This protocol was established before predictions were committed
for Test 1. The TIGHT threshold (>= 3/5 HIT) and the five
scoring dimensions were fixed before any ground-truth documents
were read for scoring purposes.

The Phase 2 registered report will be pre-registered on OSF
with the expanded corpus and ablation design.

---

# Bismillah ir-Rahman ir-Rahim
