# Bismillah ir-Rahman ir-Rahim

# R0733 -- Phase 2 Ablation: Pre-Registration, Operational Runner, and Audit System Integration

**Chronological Index:** 90 of 995  
**Date:** 2025-04-05  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** phase2_ablation_preregistration.md  
**Source Format:** md  
**SHA-256:** `1660609e55d02d05e8958ba805af461b460440da75feece7e27a0af6fdef1f99`  

---

## R0733 · Phase 2 Ablation: Pre-Registration, Operational Runner, and Audit System Integration

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: phase2_ablation_preregistration.md
- source_format: md
- text_sha256: 1660609e55d02d05e8958ba805af461b460440da75feece7e27a0af6fdef1f99

# Phase 2 Ablation: Pre-Registration, Operational Runner, and Audit System Integration

**Document version:** v1.0
**Status:** READY FOR v1.0 AUDIT
**Author:** Bilal Syed Arfeen (BayyinahEnterprise)
**Methodology basis:** Bayyinah Audit Framework v4.0 (private operational edition); v3.0 published at Zenodo DOI 10.5281/zenodo.20017335 (CC-BY-NC-4.0)
**Phase 1 paper anchor:** "Structural Regularities in AI-Assisted Audit Chains: A Pilot Study in Predictive Finding Localization", §8 (Phase 2 Pre-Registration)
**Pre-registration target:** OSF (osf.io); finalize after v1.0 audit absorption cycle
**Date:** 2026-05-09

Bismillah ar-Rahman ar-Rahim. La hawla wa la quwwata illa billah.

---

## §0: Why this document exists

The Phase 1 pilot reported 10 of 10 dimension-level HITs across two retrospective predictions on the F22-F26 sub-chain (Hamming distance d = 0 against ground truth on both tests). The pilot's primary acknowledged limitation, surfaced in §6.5, §7.2, and §7.3 of the Phase 1 paper, is that the predictor was the same Claude Opus 4 instance that participated in audit-chain authoring. The pilot cannot, on its own evidence, distinguish chain-conditioning's contribution from general LLM priors that may operate independently of the audit-chain log.

Phase 2 is the cross-vendor ablation study designed to isolate that contribution. This document is the load-bearing protocol behind the Phase 1 paper's surface claim that "Phase 2 will run a cross-instance ablation that addresses same-instance contamination." Per the structural-honesty thesis the framework operationalises, the surface claim must match the substrate behaviour: a concrete, executable protocol that produces evidence usable for or against H1, including null and contradicting outcomes that are publishable on equal footing.

The document is sole-authored by Bilal Syed Arfeen and serves two purposes. First, it is a standalone research artefact suitable for upload to OSF as supporting material; reviewers should be able to verify every claim against published primary sources. Second, its sections are designed to map cleanly onto the OSF Preregistration template fields (see Appendix A), so the OSF form body can be populated by paraphrasing or quoting from this document rather than re-authoring from scratch.

---

## §A: OSF Pre-Registration Document body content

### A.1 Research question

Does conditioning a large language model on a structured audit-chain log of past findings (CSV, 18 columns) plus a small set of declared structural regularities (R1-R11 from Phase 1) measurably reduce the Hamming distance between the model's five-dimension prediction codeword and the ground-truth codeword for the next finding the project ships a fix for, compared to an unconditioned baseline that has access only to the repository skeleton?

### A.2 Hypotheses

Let d_A and d_B denote the Hamming distance (over the five-dimension prediction codeword P1 step, P2 error code, P3 substrate layer, P4 fix-size class, P5 root cause) between the predicted codeword and the ground-truth codeword for paired predictor configurations A (chain-conditioned, cross-vendor) and B (unconditioned, same vendor as A) on the same held-out finding F(N). Let d_A,r and d_B,r denote the same quantities computed only over the three discriminating dimensions {P1, P2, P3}, dropping P4 and P5 which are coarse-grained per Phase 1 §6.5. Let d_C denote the corresponding distance under Condition C (vendor control, optional).

**H1 primary.** Mean Hamming distance under Condition A is strictly less than under Condition B over all paired predictions. Formal: E[d_A] < E[d_B] across the held-out set.

**H1 weighted secondary.** The same inequality holds when restricted to the discriminating dimensions: E[d_A,r] < E[d_B,r].

**H1 tertiary, vendor control.** If Condition C is run, mean Hamming distance under Condition A and Condition C differ only by an effect attributable to model size or generation, not to chain conditioning. Operationally: |E[d_A] - E[d_C]| is small relative to E[d_B] - E[d_A], where "small" is pre-specified as a rank-biserial correlation of magnitude below 0.2.

**H0 null.** E[d_A] >= E[d_B]. The null subsumes both no-effect and reverse-effect outcomes; both are explicitly publishable as Outcome 2 and Outcome 3 respectively (§A.8).

### A.3 Predictor configurations

All three conditions use a fresh model instance with no shared conversation context with the audit-chain producer or with each other. Each condition receives a single prompt (templates in §D) and produces a single five-dimension prediction codeword, committed to a Git-tracked Markdown file before any ground-truth scoring document is read.

**Condition A (chain-conditioned, cross-vendor).** Vendor: not Anthropic. Candidate models verified against public API documentation as of 2026-05-09 (web-verified, see references):
- OpenAI GPT-5.5 (released 2026-04-23 in API; 1M token context window; standard Responses and Chat Completions APIs at $5/$30 per 1M tokens) -- primary candidate
- Google Gemini 2.5 Pro (Vertex AI; supports 1M+ token context; structured output, system instructions, function calling) -- secondary candidate
- OpenAI GPT-5.4 (released 2026-03-05 in API; 1M context) -- backup if GPT-5.5 unavailable

Condition A inputs: (i) the structured audit-chain log CSV for findings F(1) through F(N-1), (ii) the eleven regularities R1-R11 in propositional form (Appendix B of the Phase 1 paper, included verbatim), (iii) the Gate 11 Sigstore-CASM verifier pipeline schema (8 steps, included verbatim from `experiment_protocol.md`), (iv) the prediction prompt template (§D.1).

**Condition B (unconditioned, same vendor and model as A).** Same vendor and model identifier as Condition A. Inputs: (i) the repository skeleton -- public file paths, exported function signatures, top-level test names, and release version history of furqan-lint -- with no audit history, no findings, no regularities, no pipeline schema. (ii) The prediction prompt template (§D.2). The model is asked: "What is the next finding this project will ship a fix for?" with the same five-dimension output schema.

**Condition C (vendor control, optional).** Vendor: same as A. Model: a different size or generation from A's model (e.g., if A uses GPT-5.5, then C uses GPT-5.4 or GPT-5.5-mini). Inputs: identical to Condition A. Purpose: separate model-size/generation effects within a single vendor from chain-conditioning effects across vendors.

### A.4 Ablation control: Condition C rationale

Condition C is optional but recommended. It addresses the residual confound that Condition B's underperformance against Condition A could be attributed to model size or generation rather than to the absence of chain conditioning, if Conditions A and B happened to use models of meaningfully different capability. Running Condition C with the same inputs as Condition A but a different intra-vendor model size isolates intra-vendor capability variance from chain-conditioning effects. If E[d_A] approximately equals E[d_C] and both are less than E[d_B], the chain-conditioning interpretation strengthens. If E[d_C] approaches E[d_A] only when given the chain log, but E[d_C] under Condition B inputs approaches E[d_B], the chain-conditioning interpretation is consistent across model scales.

Condition C's optionality reflects budget and timeline realism. It is preferred but not required; the registered report will report whether C was run and present results stratified accordingly.

### A.5 Sample size

Pre-registered minimum N = 10 paired predictions. Pre-registered preferred N = 20.

**Source priority (forward-looking preferred):**
1. Audit findings F27 onward as the audit chain produces them in the natural course of the project. Each future finding becomes a paired prediction the moment it surfaces in an audit round.
2. Backward-normalisation fallback: pre-round-28 audit memos from sibling repositories (Bayyinah-Integrity-Scanner, Furqan-language) transcribed to the 18-column schema. The corpus accounting document (`corpus_accounting.md`) estimates 50-80 transcribable findings from the existing 43-round corpus.

**Mixed-source handling.** If N is reached using a mix of forward-looking and backward-normalised findings, the registered report stratifies analyses by source type (forward vs. backward) and reports both pooled and stratified results. A pre-specified subgroup analysis tests whether the H1 effect is consistent across sources.

**Stopping rule.** Data collection stops when (a) N >= 20 has been reached and analysis is locked, or (b) N >= 10 has been reached and at least 12 calendar months have passed since the OSF timestamp, whichever comes first. Stopping at 10 invokes a sensitivity analysis acknowledging reduced power in the registered report.

### A.6 Statistical analysis plan

**Per-prediction scoring.** For each paired prediction (Condition A, Condition B, optionally Condition C) on held-out finding F(N), compute the five-bit Hamming distance d in {0, 1, 2, 3, 4, 5} between the predicted codeword and the ground-truth codeword extracted from the audit document for F(N). Scoring follows Phase 1's Section 5.2 dimensions (P1-P5) and Section 8.2 rules (first-named candidate counts; mechanism presence for P5, not exclusion of alternatives).

**Primary test.** One-sided paired Wilcoxon signed-rank test on (d_A, d_B) pairs, alternative `less` (testing E[d_A] < E[d_B]), alpha = 0.05. Computed via R `exactRankTests::wilcox.exact(d_A, d_B, paired=TRUE, alternative="less", exact=TRUE)`. The exact form is preferred over the normal approximation for N <= 20 (per Wilcoxon 1945 and the `exactRankTests` Shift-Algorithm documentation). Effect size: rank-biserial correlation r_rb = 1 - (2 * U) / (n * (n + 1)) where U is the smaller of the signed-rank sums.

**Secondary test (per-dimension).** Five paired McNemar's tests (one per dimension P1-P5), each comparing HIT/MISS outcomes for Condition A vs Condition B. For each dimension d in {P1, P2, P3, P4, P5}, count discordant pairs b (A HIT, B MISS) and c (A MISS, B HIT) over the held-out set. Because expected discordant counts are small (b + c likely < 25 for N = 10-20), use the **exact binomial form**: `binom.test(b, b + c, p = 0.5, alternative = "greater")` (per r-statistics.co and Fagerland et al. 2013). Family-wise alpha = 0.05 controlled across the 5 tests via Holm-Bonferroni step-down: order p-values smallest to largest, compare p_(1) to alpha/5, p_(2) to alpha/4, p_(3) to alpha/3, p_(4) to alpha/2, p_(5) to alpha (Holm 1979).

**Restricted-dimensions sensitivity.** Repeat the primary Wilcoxon on (d_A,r, d_B,r) pairs computed over {P1, P2, P3} only. If the H1 result holds on the restricted dimensions, the conclusion is robust to the coarse-grain critique of P4 and P5 surfaced in Phase 1 §6.5 and §7.4.

**Vendor-control comparison (if Condition C run).** Two-sided paired Wilcoxon signed-rank on (d_A, d_C) pairs, alpha = 0.05. The pre-specified expectation is non-significance; significance indicates intra-vendor model-size/generation effects that should be reported as a moderator.

**Multiple comparison correction.** The four-test family (primary Wilcoxon, restricted Wilcoxon, McNemar Holm-Bonferroni family, vendor-control Wilcoxon) is treated as one primary plus three pre-specified secondaries; the primary is not corrected, the McNemar family is internally corrected, and the restricted and vendor-control Wilcoxons are reported with un-corrected p-values plus the Holm-Bonferroni-adjusted family alpha as a footnote.

**Reproducibility.** Single R Quarto document (`phase2_analysis.qmd`) with locked package versions (R >= 4.4; `stats` base; `exactRankTests` >= 0.8-37; `arules` >= 1.7-9; `binom.test` is base R `stats`). Fixed `set.seed(20260509)` before any randomised step. Raw prediction CSVs and scoring CSVs committed under `data/`. The Quarto renders to PDF and HTML; both committed.

**Pre-registered exclusion criteria E1-E5.**

- **E1.** Predictor produces a refusal, off-task output, or syntactically malformed codeword that persists across two re-executions with identical inputs. Excluded prediction is reported in the registered report as a failure mode but does not enter the analysis.
- **E2.** Audit document for F(N) does not provide ground truth on at least 4 of 5 dimensions. The held-out finding is dropped from the paired set; replacement is not attempted post-hoc.
- **E3.** Finding F(N) surfaces via a path outside the predictor's training data window (e.g., a CVE disclosed before the predictor's known cutoff that explicitly mentions the substrate symbol). Surface as ADVISORY-tier deviation in the registered report; finding is included in the primary analysis but flagged.
- **E4.** OSF timestamp of the pre-registration does not precede the predictor's commit timestamp for any prediction on F(N). The prediction is excluded.
- **E5.** The audit-reveal commit (the round closure marking F(N) as visible to the project lead) was made publicly before the prediction commit for F(N). The prediction is excluded.

### A.7 Pre-registration timing

Two timestamp guarantees support the pre-registration's load-bearing claim that predictions were not made after ground truth was visible:

1. **OSF timestamp anchor.** This document and the prediction prompt templates (§D) are uploaded to OSF and frozen via the OSF registration process. OSF assigns a DOI of the form `10.17605/OSF.IO/<8-char-id>` (per doi.org/10.17605 prefix and help.osf.io documentation). The DOI's registration timestamp is the immutable anchor.
2. **Git enforcement.** A pre-commit hook in the Phase 2 prediction repository rejects commits to `predictions/` whose author timestamp predates the OSF DOI registration timestamp. Each prediction commit's hash is included in the registered report's appendix. The Git history is forced read-only after analysis lock.

If either anchor is broken (commit timestamp predates OSF, or OSF registration is amended without the audit-trail field set), exclusion criterion E4 fires.

### A.8 Pre-registered publishable outcomes

All three outcomes are pre-registered as publishable. The registered-report submission commits to publishing whichever outcome obtains, with full statistical reporting and a discussion section appropriate to the obtained outcome.

**Outcome 1 (H1 supported).** Primary Wilcoxon p < 0.05 with rank-biserial correlation magnitude > 0.3, AND restricted Wilcoxon p < 0.05. McNemar family-wise significance on at least one dimension. Interpretation: chain-conditioning contributes to prediction accuracy beyond what an unconditioned LLM provides on the same task. The registered report discusses which dimensions drive the effect (per the per-dimension McNemar results) and what regularities (R1-R11) appear load-bearing.

**Outcome 2 (H1 not supported, null).** Primary Wilcoxon p >= 0.05, OR primary p < 0.05 but restricted Wilcoxon p >= 0.05. Interpretation: the Phase 1 pilot's 10/10 HIT result is plausibly attributable to general LLM priors and is not isolated evidence for chain-conditioning's contribution. The registered report discusses which alternative explanations (training-data leakage, dimension coarseness, sample size) are best supported by the per-dimension and stratified analyses, and revises the Phase 1 paper's claims via an erratum or amendment.

**Outcome 3 (H1 contradicted).** Primary Wilcoxon p < 0.05 in the **opposite** direction, i.e., E[d_B] < E[d_A] significantly. Interpretation: the structured audit-chain log encodes systematic noise that degrades prediction relative to the unconditioned baseline. The registered report investigates the source of the noise (overfitting to chain-specific failure modes, regularities that fail to generalise, prompt-template artefacts), retracts the Phase 1 paper's predictive-utility framing, and pivots the contribution to "what audit chains do not encode."

The structural-honesty discipline that motivated this study requires Outcome 2 and Outcome 3 be reported with the same prominence, completeness, and submission target as Outcome 1. The registered report's title and abstract are pre-drafted in three versions, one per outcome, in this document's supplementary materials and committed to the OSF project before data collection completes.

---

## §B: Operational Runner

This section is the concrete procedure for executing Phase 2 once OSF pre-registration is complete.

### B.1 Trigger conditions

The runner executes when **all** of the following hold:

1. OSF pre-registration is timestamped and the DOI is recorded in `osf_doi.txt` under the Phase 2 repository root.
2. A new audit finding F(N) for N >= 27 has been documented under the Bayyinah Audit Framework, with closure-shape A (fully closed, ground truth available), and the finding's audit memo has been committed to the audit chain repository.
3. The forward-looking source (or backward-normalisation if invoked) yields the next-in-line held-out finding.
4. No HALT condition (§B.8) is currently raised.

The runner does NOT execute opportunistically on every audit round; it executes when held-out findings accumulate or on a calendar cadence (monthly batch processing).

### B.2 Pre-execution checklist

Before each prediction round, verify:

- **PE-1.** Vendor API access is current; model identifier matches the pre-registered candidate list; no model deprecation or capability change has been announced since OSF timestamp. Document the model version in the prediction's metadata field.
- **PE-2.** Substrate-symbol verification per G14.7-F7/F8/F9: the pipeline schema, regularities text, and prediction prompt template are byte-identical to the OSF-anchored versions. SHA-256 hashes of all four input artefacts logged.
- **PE-3.** No accidental leak: the prediction operator (the human running the runner) confirms in writing that they have not read the F(N) audit memo or any commit message that names F(N)'s substrate symbols.
- **PE-4.** Git pre-commit hook is installed and tested (rejects commits with author-timestamp < OSF DOI timestamp).
- **PE-5.** OSF timestamp is at least 1 hour earlier than the planned prediction commit (buffer for clock skew).

If any pre-execution check fails, raise HALT and surface a finding (§B.8).

### B.3 Condition A execution

1. Open a fresh model session with the pre-registered Condition A vendor and model.
2. Submit the §D.1 prompt template, with placeholders filled from: (i) the audit-chain log CSV trimmed to F(1) through F(N-1), (ii) the regularities R1-R11 verbatim, (iii) the pipeline schema.
3. Receive the model's response. Parse into the five-dimension codeword. If the response is malformed, retry once with identical inputs; if still malformed, invoke E1.
4. Commit the codeword to `predictions/A/F<N>.md` with the timestamp, model identifier, full prompt hash, full response, and parsed codeword.
5. Tag the commit with `phase2-A-F<N>`.
6. Blinding: the operator does not view the F(N) audit memo until all conditions for F(N) have been committed.

### B.4 Condition B execution

1. Open a fresh model session with the same vendor and model identifier as Condition A's commit (read from `predictions/A/F<N>.md` metadata).
2. Submit the §D.2 prompt template. Inputs: repository skeleton (file tree, exported function signatures, test names, release version history), and the five-dimension output schema. No audit history, no regularities, no pipeline schema.
3. Receive, parse, retry on malformed (then invoke E1 if still malformed).
4. Commit to `predictions/B/F<N>.md` with the same metadata fields.
5. Tag with `phase2-B-F<N>`.

### B.5 Condition C execution (if running)

1. Open a fresh model session with the same vendor as A but a different intra-vendor model size or generation.
2. Submit the §D.3 prompt template. Inputs: identical to Condition A.
3. Receive, parse, retry, commit to `predictions/C/F<N>.md`.
4. Tag with `phase2-C-F<N>`.

### B.6 Reveal and scoring procedure

1. After all conditions for F(N) are committed and tagged, the operator opens the F(N) audit memo and extracts the ground-truth codeword.
2. The ground-truth codeword is committed to `ground_truth/F<N>.md` with the audit-memo commit hash referenced.
3. For each condition, score per Phase 1 Section 5.2 rules. Compute Hamming distance d (5-bit) and d_r (3-bit restricted to {P1, P2, P3}).
4. Append the row (finding_id, condition, d, d_r, per-dimension HITs) to `scoring/results.csv`.
5. Tag the scoring commit with `phase2-scored-F<N>`.

The operator must not edit any prediction file after viewing the audit memo; the Git history enforces this and the audit log is committed as evidence.

### B.7 Aggregation and analysis

1. After data collection stop (per §A.5 stopping rule), freeze `scoring/results.csv`.
2. Render `phase2_analysis.qmd` to produce `phase2_analysis.pdf` and `.html`.
3. The Quarto document executes the primary, secondary, restricted, and vendor-control tests per §A.6.
4. The rendered analysis is committed and tagged `phase2-analysis-locked`.
5. The registered report is drafted using the locked analysis. Pre-drafted abstracts (one per outcome) are selected; the matching abstract is finalised.

### B.8 HALT criteria

The runner halts and surfaces a finding if:

- **HALT-1.** Vendor API for the pre-registered model is unavailable or has changed capability (e.g., context window reduced) such that pre-registered prompt templates exceed limits. Resolution: amend pre-registration with a deviation notice on OSF, downgrade to the backup model in §A.3, document.
- **HALT-2.** A held-out finding's ground-truth document violates E2 (less than 4 of 5 dimensions documented). Drop the finding and continue.
- **HALT-3.** Substrate-symbol mismatch between the OSF-anchored prompt template and the runner's stored copy (SHA-256 mismatch on PE-2). Resolution: re-fetch from OSF or its mirror; do not predict from the desynchronised template.
- **HALT-4.** Git pre-commit hook rejects a prediction commit. Resolution: investigate clock-skew or OSF-timestamp issues; do not bypass the hook.
- **HALT-5.** Cross-chain crossover (§C.3): an S-chain (security) finding surfaces during a G-chain prediction round and the operator cannot reliably maintain blinding. Resolution: defer prediction until the S-chain corrective ship completes.

Each HALT raises a six-element finding into the project's audit chain (severity per the framework rubric) and updates the OSF deviation log.

---

## §C: Audit System Integration

This section specifies the contract between Phase 2's prediction runner and the existing audit-chain infrastructure.

### C.1 Non-interference contract with G-chain corrective rhythm

Phase 2 prediction execution must not delay, modify, or otherwise interfere with the G-chain (Gate 11 furqan-lint corrective ship sequence) or its successors. The runner executes asynchronously: predictions are committed before reveal, and reveals occur only after the corrective ship for F(N) has closed under the audit framework's normal protocol. If a corrective ship is in progress when a prediction is due, the prediction is deferred until ship-close; the deferral and its duration are logged.

The G-chain is the audit chain's primary product; Phase 2 is a measurement instrument attached to the chain, not a participant in it.

### C.2 Round numbering reconciliation

The Phase 1 paper documents two parallel numbering systems: Counter A (global, framework-mandated, rounds 1-37) and Counter B (phase-scoped to Gate 11, rounds 28-33, mapping to global rounds approximately 38-43). Phase 2 uses **Counter A as the canonical anchor** for all forward-looking findings (F27 onward = global round 44 onward). When a finding's documentation references Counter B, the runner resolves to Counter A via the mapping table in `corpus_accounting.md`. Backward-normalised findings are tagged with both counters in the prediction metadata.

The 18-column schema (Appendix C) carries `global_round` and `phase_round` columns precisely to keep this reconciliation explicit.

### C.3 Cross-chain crossover handling

The audit chain has two active sub-chains: G-chain (Gate 11, furqan-lint static-analyzer audit) and S-chain (security hardening, scope per `bayyinah_security_hardening_plan.md`). When findings surface in S-chain that are structurally relevant to a G-chain prediction round in flight, the operator must declare the crossover in the prediction metadata field `crossover_disclosure` and either (a) defer the G-chain prediction until S-chain closure, or (b) execute the prediction with explicit acknowledgement of contamination risk and flag the prediction for sensitivity analysis.

Predictions flagged for crossover sensitivity are analysed both in-pool and out-of-pool in the registered report.

### C.4 Out-of-scope items

Phase 2 explicitly does NOT do any of the following:

- Phase 2 does not modify the Phase 1 paper. Revisions to the Phase 1 paper (in response to Phase 2 outcomes 2 or 3) proceed via a separate erratum or amendment cycle after Phase 2 results lock.
- Phase 2 does not execute regularity-mining on the corpus. Algorithmic mining via `arules` is Phase 3 (cross-project validation across all three repositories) and is documented in §F.
- Phase 2 does not change the Bayyinah Audit Framework's six-element findings format, severity rubric, or closure-shape taxonomy.
- Phase 2 does not introduce new regularities. R1-R11 from Phase 1 are the operative set; if new regularities surface in the held-out predictions, they are documented but not added to the predictor's input mid-study (would invalidate pre-registration).
- Phase 2 does not change the Phase 1 paper's authorship, byline, or affiliation strings.

---

## §D: Prompt templates

These templates are byte-frozen at OSF-anchor time. Any deviation invokes HALT-3.

### D.1 Condition A prompt template (chain-conditioned, cross-vendor)

```
SYSTEM: You are a software-defect predictor. You will receive a structured audit-chain log, a list of declared structural regularities, and a verifier pipeline schema. Your task is to predict the next finding in the chain on five dimensions. Output strictly in the schema given. Do not invent dimensions, do not omit dimensions.

USER: Below are findings F(1) through F(N-1) from the Gate 11 Sigstore-CASM verifier pipeline of the furqan-lint static analyzer. The chain follows a single failure-mode sequence through an 8-step pipeline. Eleven structural regularities (R1-R11) have been extracted from the chain by manual inspection.

[STRUCTURED AUDIT-CHAIN LOG, CSV, 18 columns, rows F(1) through F(N-1)]

[REGULARITIES R1-R11, propositional form, verbatim from Phase 1 paper Appendix B]

[PIPELINE SCHEMA, 8 steps, verbatim from experiment_protocol.md]

Predict the next finding F(N) on five dimensions:
- P1 (failing step): one of {step_1_init, step_2-3_dispatch, step_4_install, step_4_import, step_5_bytes, step_6_identity, step_7_signature, step_8_surface}
- P2 (error code): one of CASM-V-NNN format, or a Python exception class name (e.g., SyntaxError, KeyError)
- P3 (substrate layer): a snake_case label naming the layer (e.g., verifier_dispatch, policy_construction, extractor_dispatch)
- P4 (fix-size class): one of {one_word, few_lines, ~30_lines, 100+}
- P5 (root cause): one sentence describing the mechanism

Output as a single JSON object with keys P1, P2, P3, P4, P5. If you would name multiple candidates for any dimension, name only the first; the first-named candidate is what will be scored.
```

### D.2 Condition B prompt template (unconditioned, same vendor as A)

```
SYSTEM: You are a software-defect predictor. You will receive a repository skeleton -- file paths, function signatures, test names, release versions. Your task is to predict the next bug this project will ship a fix for, on five dimensions. Output strictly in the schema given. Do not invent dimensions, do not omit dimensions.

USER: The project is furqan-lint, a static analyzer published on PyPI. Below is the repository skeleton.

[FILE TREE, top 3 levels]

[EXPORTED FUNCTION SIGNATURES from public modules]

[TOP-LEVEL TEST NAMES from tests/]

[RELEASE VERSION HISTORY, last 20 versions, with release dates only]

Predict the next bug the project will ship a fix for, on five dimensions:
- P1 (failing step): one of {step_1_init, step_2-3_dispatch, step_4_install, step_4_import, step_5_bytes, step_6_identity, step_7_signature, step_8_surface} -- if you do not recognise this taxonomy, predict "unknown"
- P2 (error code): one of CASM-V-NNN format, or a Python exception class name
- P3 (substrate layer): a snake_case label naming the layer
- P4 (fix-size class): one of {one_word, few_lines, ~30_lines, 100+}
- P5 (root cause): one sentence describing the mechanism

Output as a single JSON object with keys P1, P2, P3, P4, P5. If you would name multiple candidates, name only the first.
```

### D.3 Condition C prompt template (vendor control, optional)

Identical to Condition A's prompt template (D.1). Only the model identifier changes.

---

## §E: Acceptance criteria

This document is OSF-ready when all of the following are true:

1. Each section §A through §G is filled with substantive content (not stubs).
2. Every empirical claim about a statistical method, R package, or OSF mechanism is cited to a verified primary or authoritative source listed in Appendix B.
3. The 18-column dataset schema in Appendix C matches `audit_chain_log_F22_F26.csv` byte-for-byte (column names and order).
4. The five-dimension codeword definition matches Phase 1 Section 5.2 byte-for-byte.
5. Prompt templates §D.1, D.2, D.3 are concrete enough that an independent operator could run them without re-asking the project lead for clarification.
6. The three pre-registered outcomes §A.8 are mutually exhaustive and the decision rules between them are unambiguous.
7. Exclusion criteria E1-E5 are concrete and verifiable (each has a binary check that an operator can perform).
8. HALT criteria §B.8 each have a documented resolution path.
9. Findings surfaced during authoring (Appendix D, if any) are absorbed or explicitly deferred with a recommended-shape entry.
10. Authorship, affiliation, and DOI fields are filled and the byline reads "Bilal Syed Arfeen, BayyinahEnterprise" without trailing co-authorship.

The v1.0 audit cycle (typically by a different LLM instance or human reviewer than the author) verifies each acceptance criterion. Failures generate findings; v1.1 absorbs the audit and the document is re-checked.

---

## §F: Successor work

**Phase 3: Cross-project validation.** Apply the same ablation design to the two sibling repositories (Bayyinah-Integrity-Scanner, Furqan-language compiler). The regularities R1-R11 were extracted from a single sub-chain in furqan-lint; Phase 3 tests whether they transfer. Phase 3 also runs algorithmic association-rule mining on the full normalised corpus via R `arules` (CRAN, package version >= 1.7-9, last updated 2026-03-29) to discover regularities that manual inspection missed.

**Counter A normalisation.** The pre-round-28 audit memos must be transcribed to the 18-column schema before backward-normalisation can supply the Phase 2 sample. Estimated effort: 2-3 hours per round across approximately 27 rounds (rounds 1-22 across three sibling repositories under Framework v1-v3, plus rounds 23-27 in furqan-lint under v3). Time estimate, with the project's 75% buffer applied: 95 to 142 hours of dedicated transcription work. This is not on the critical path for Phase 2 if the forward-looking source supplies N >= 10 within the stopping window.

**Registered-report submission timing.** Target venues, in order of preference, have registered-report tracks at:
1. ACM Transactions on Software Engineering and Methodology (TOSEM)
2. IEEE Transactions on Software Engineering (TSE)
3. ICSE / FSE registered-report tracks (annual deadlines)

The OSF pre-registration anchor is submitted to the chosen venue's registered-report track at Stage 1 (in-principle acceptance); analysis lock and Stage 2 submission follow data collection completion. Wall-clock estimate from OSF timestamp to Stage 2 submission, with 75% buffer: 14-21 months for forward-looking N = 20; 9-13 months for forward-looking N = 10 with backward fallback.

**Erratum / amendment cycle.** If Phase 2 produces Outcome 2 or Outcome 3, the Phase 1 paper requires either an erratum (Outcome 2: claims softened, Phase 2 result cited) or a retraction-and-republication cycle (Outcome 3: predictive-utility framing withdrawn, contribution re-scoped to "what audit chains do not encode"). Both cycles are scoped under separate documents authored after Phase 2 lock.

---

## §G: Discipline this document follows

This document follows the Bayyinah Audit Framework v3 / v4 conventions:

- **Substrate-verification at authoring time** (G14.7-F7/F8/F9). Every statistical method named (Wilcoxon signed-rank, McNemar's exact, Holm-Bonferroni, rank-biserial correlation), every R package named (`stats`, `exactRankTests`, `arules`), every OSF mechanism named (DOI prefix `10.17605/OSF.IO/`, Preregistration template, deviation log) was verified against a primary or authoritative source via web search before inclusion. Citations in Appendix B.
- **Six-element findings format** when surfacing gaps (Appendix D).
- **75% time-estimate buffer** on every wall-clock estimate offered (Phase 3 transcription: 95-142h; Stage 2 submission: 14-21 months / 9-13 months).
- **Severity uppercase** (CRITICAL, HIGH, MEDIUM, LOW, ADVISORY) for any finding reference.
- **No em-dashes**; double-hyphens (`--`) where prose calls for the dash function.
- **Bullets only when content is genuinely enumerable.** Where prose carries a single coherent argument, prose is preferred.
- **Sole authorship.** Bilal Syed Arfeen, BayyinahEnterprise. No co-author trailers. The document is authored with assistance from a research-methodology auditor (Perplexity Computer); the auditor's role is verification and drafting, not authorship.
- **Religious anchor.** The opening invocation (Bismillah ar-Rahman ar-Rahim, La hawla wa la quwwata illa billah) and the closing Quranic anchor are project convention; they do not modify the document's standing as a peer-reviewable scientific protocol.

---

## Appendix A: OSF field-by-field mapping

The OSF Preregistration template (the standard, comprehensive template documented at help.osf.io and cos.io as of 2026-05-09) presents its content in sections that vary slightly by template version. The mapping below targets the **OSF Preregistration** template (DOI 10.17605/OSF.IO/WEKMB) and is the canonical mapping for this document. If the OSF UI presents differently-named sub-sections at upload time, the operator paraphrases this document's content into the OSF fields and notes any field-name deviation in the OSF deviation log.

| OSF Section / Field | Source in this document |
|---|---|
| Title | Title block of this document |
| Authors / Contributors | Title block (Bilal Syed Arfeen, BayyinahEnterprise) |
| Description / Abstract | §0 Why this document exists |
| Hypotheses | §A.2 Hypotheses |
| Study Design / Design Plan | §A.3 Predictor configurations; §A.4 Ablation control |
| Sampling Plan | §A.5 Sample size |
| Variables (Manipulated) | §A.3 (input artefacts to each condition) |
| Variables (Measured) | §A.6 per-prediction scoring (five-dimension codeword, Hamming distance) |
| Indices (Combined / Computed) | §A.6 d, d_r, rank-biserial correlation, odds ratios |
| Statistical Models | §A.6 Wilcoxon signed-rank, McNemar's exact, Holm-Bonferroni |
| Inference Criteria | §A.6 alpha = 0.05, family-wise correction; §A.8 Outcomes |
| Data Exclusion | §A.6 Exclusion criteria E1-E5 |
| Missing Data | §A.5 Mixed-source handling; §A.6 (E2 covers missing dimensions) |
| Exploratory Analysis (separate) | §B.7 stratification by source; §C.3 crossover-flagged predictions |
| Other / Notes | §B Operational Runner; §C Audit System Integration |
| Files attached | This document, audit_chain_log CSV, prompt templates §D verbatim |

The OSF help documentation distinguishes "confirmatory" pre-registered analyses from "exploratory" post-hoc analyses; everything in §A.6 is confirmatory, and the stratification analyses in §B.7 are pre-specified secondaries (still confirmatory). Any analysis not specified in this document before OSF timestamp is exploratory and flagged as such in the registered report.

OSF DOI assignment: confirmed as `10.17605/OSF.IO/<8-char-id>` per [doi.org/10.17605](https://doi.org/10.17605) and the example DOIs published in the OSF help articles (e.g., `10.17605/OSF.IO/WEKMB` for the OSF Preregistration template itself, [help.osf.io/article/330](https://help.osf.io/article/330-welcome-to-registrations)).

---

## Appendix B: References

Verified citations as of 2026-05-09. Each entry includes a DOI, URL, or other primary identifier permitting independent verification.

**Statistical methods.**

- Wilcoxon, F. (1945). Individual comparisons by ranking methods. *Biometrics Bulletin*, 1(6), 80-83. DOI: 10.2307/3001968. Canonical reference for the signed-rank test as a paired non-parametric test for ordinal or non-normal continuous data ([Wikipedia](https://en.wikipedia.org/wiki/Wilcoxon_signed-rank_test)).
- McNemar, Q. (1947). Note on the sampling error of the difference between correlated proportions or percentages. *Psychometrika*, 12(2), 153-157. DOI: 10.1007/BF02295996. Canonical reference for the paired-binary test ([Wikipedia](https://en.wikipedia.org/wiki/McNemar%27s_test)).
- Fagerland, M. W., Lydersen, S., & Laake, P. (2013). The McNemar test for binary matched-pairs data: mid-p and asymptotic are better than exact conditional. *BMC Medical Research Methodology*, 13(1), 91. DOI: 10.1186/1471-2288-13-91 ([PMC article](https://pmc.ncbi.nlm.nih.gov/articles/PMC3716987/)). Recommends mid-p / asymptotic over exact conditional in many practical regimes; this document uses exact binomial via `binom.test` per r-statistics.co's recommendation when discordant pairs b + c < 25, which the simulations in Fagerland et al. confirm is acceptable in the small-N regime.
- Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics*, 6(2), 65-70. JSTOR 4615733. Canonical reference for the step-down family-wise error correction ([Wikipedia](https://en.wikipedia.org/wiki/Holm%E2%80%93Bonferroni_method)).
- Hamming, R. W. (1950). Error detecting and error correcting codes. *Bell System Technical Journal*, 29(2), 147-160. DOI: 10.1002/j.1538-7305.1950.tb00463.x. Canonical reference for Hamming distance.
- Kerby, D. S. (2014). The simple difference formula: An approach to teaching nonparametric correlation. *Comprehensive Psychology*, 3(1). Canonical accessible reference for rank-biserial correlation as effect size for Wilcoxon signed-rank.

**OSF and pre-registration practice.**

- Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). The preregistration revolution. *Proceedings of the National Academy of Sciences*, 115(11), 2600-2606. DOI: 10.1073/pnas.1708274114. Canonical reference for OSF preregistration practice and the rationale for publishing null and contradicting outcomes.
- Center for Open Science. *Welcome to Registrations & Preregistrations* (help.osf.io article 330). Authoritative current documentation of OSF templates and DOI assignment ([help.osf.io](https://help.osf.io/article/330-welcome-to-registrations)).
- Center for Open Science blog. *Choosing the Right Preregistration Template: A Guide for Researchers* ([cos.io](https://www.cos.io/blog/choosing-preregistration-template-guide-for-researchers)). Confirms OSF Preregistration is the standard comprehensive template for studies without a discipline-specific match.
- DOI Foundation. *DOI Name 10.17605 Values* ([doi.org/10.17605](https://doi.org/10.17605)). Confirms OSF as the registrant under the 10.17605 prefix.

**R packages and software.**

- R Core Team (2025). R: A Language and Environment for Statistical Computing. Base R `stats` package supplies `wilcox.test`, `mcnemar.test`, and `binom.test`.
- Hothorn, T., & Hornik, K. *exactRankTests: Exact Distributions for Rank and Permutation Tests* (CRAN). Provides `wilcox.exact` for exact paired Wilcoxon p-values via Streitberg-Roehmel Shift-Algorithm ([CRAN PDF](https://cran.r-project.org/web/packages/exactRankTests/exactRankTests.pdf), [rdrr.io reference](https://rdrr.io/cran/exactRankTests/man/wilcox.exact.html)).
- Hahsler, M. *arules: Mining Association Rules and Frequent Itemsets* (CRAN, last updated 2026-03-29). DOI: 10.32614/CRAN.package.arules. Provides Apriori and Eclat for transaction-data mining ([CRAN page](https://cran.r-project.org/package=arules)).
- Fay, M. P. *exact2x2: Exact Tests and Confidence Intervals for 2x2 Tables* (CRAN). Provides exact McNemar's via `binom.exact` for matched-pair tables ([CRAN vignette](https://cran.r-project.org/web/packages/exact2x2/vignettes/exactMcNemar.pdf)).

**LLM vendor and model verification (as of 2026-05-09).**

- OpenAI. *Introducing GPT-5.5* (2026-04-23, updated 2026-04-24). 1M token context window; available in Responses and Chat Completions APIs at $5/$30 per 1M input/output tokens ([openai.com](https://openai.com/index/introducing-gpt-5-5/)).
- OpenAI. *Introducing GPT-5.4* (2026-03-05). 1M token context, native computer-use ([openai.com](https://openai.com/index/introducing-gpt-5-4/)).
- Google Cloud. *Gemini 2.5 Pro* documentation. 1M+ token context, structured output, function calling, system instructions on Vertex AI ([Vertex AI docs](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-pro), [Gemini long-context docs](https://ai.google.dev/gemini-api/docs/long-context)).
- Meta. *The Llama 4 herd* (2025-04-05). Llama 4 Scout supports up to 10M token context; pre-trained at 256K ([ai.meta.com](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)).

**Phase 1 paper and dataset.**

- Arfeen, B. S. (2026). Bayyinah Audit Framework v3.0. Zenodo. DOI: 10.5281/zenodo.20017335. CC-BY-NC-4.0.
- Arfeen, B. S. (2026). Bayyinah Audit Framework Application Brief v1.0. Zenodo. DOI: 10.5281/zenodo.20031395.
- Arfeen, B. S. (2026). Structural Regularities in AI-Assisted Audit Chains: A Pilot Study in Predictive Finding Localization. Phase 1 paper, deposited at Zenodo (DOI assigned at deposit time).
- Predictive Audit Prompting Pilot dataset bundle: `audit_chain_log_F22_F26.csv` plus protocol, predictions, and scoring documents (this document's supplementary data).

---

## Appendix C: Dataset schema

The audit-chain log CSV uses an 18-column schema. All columns are string-typed in the CSV; type semantics are documented below. The schema matches `audit_chain_log_F22_F26.csv` from the Phase 1 supplementary bundle byte-for-byte in column names and order.

| # | Column | Type | Value range / format | Example (F26) |
|---|---|---|---|---|
| 1 | finding_id | string | F<integer>, monotonic in counter B | F26 |
| 2 | counter | enum | A or B | B |
| 3 | global_round | integer | 1-37 historical; 38+ forward-looking | 42 |
| 4 | phase_round | integer | counter-B-scoped; 28-33 for Gate 11 | 33 |
| 5 | timestamp | date | ISO 8601 YYYY-MM-DD | 2026-05-08 |
| 6 | repository | enum | furqan-lint / Bayyinah-Integrity-Scanner / Furqan-language | furqan-lint |
| 7 | version | string | semver | 0.11.6 |
| 8 | step | string | step_<num>_<short_label>; <num> in {1, 2-3, 4, 5, 6, 7, 8} | step_8_surface |
| 9 | error_code | string | CASM-V-NNN or Python exception class name | SyntaxError |
| 10 | substrate_layer | string | snake_case label naming the failing pipeline layer | extractor_dispatch |
| 11 | scope_class | string | snake_case scope description | wrong_language_dispatch |
| 12 | severity | enum (uppercase) | CRITICAL / HIGH / MEDIUM / LOW / ADVISORY | LOW |
| 13 | fix_size_loc | integer | lines-of-code count, may be approximate (`~30`) | 30 |
| 14 | fix_size_class | enum | one_word / few_lines / ~30_lines / 100+ | ~30_lines |
| 15 | fix_location | string | filename | surface_extraction.py |
| 16 | root_cause | string | one-sentence mechanism description | extract_public_surface dispatches all files to Python ast.parse with no extension routing |
| 17 | closure_shape | enum | A (fully closed) / B (partial) / C (deferred) / D (escalated) | A |
| 18 | regularities | string | comma-separated list of regularity IDs (R1-R11) covering this finding | R1,R2,R7,R9,R11 |

Additional notes:

- `step` values combine the step number and a short layer label; the canonical eight steps are step_1_init, step_2-3_dispatch, step_4_install, step_4_import, step_5_bytes, step_6_identity, step_7_signature, step_8_surface. (Step 2-3 is a fused step in the Gate 11 pipeline.)
- `severity` for the F22-F26 sub-chain is uniformly LOW because none of the findings shipped to end-users; HIGH severity in the Phase 1 paper's discussion refers to the audit-internal HIGH classification used by the Counter B framework rubric, while severity in this CSV is the public-impact severity used by Counter A.
- `fix_size_loc` is parsed as the integer suffix when prefixed with `~` (approximate); analysis treats `~N` and `N` identically for the fix_size_class derivation.
- Empty `regularities` for early findings (rounds 1-22) is permissible during corpus normalisation; the field is filled by manual inspection during Counter A normalisation (§F).

---

## Appendix D: Findings surfaced during authoring

**Finding ID:** PHASE2-PROMPT-F1
**Severity:** ADVISORY
**Title:** OSF Preregistration template section labels in this prompt do not match help.osf.io's canonical template structure.
**Substrate:** The authoring prompt asserts that OSF has "eight steps: Metadata, Overview, Research Design, Sampling, Variables, Analysis Plan, Other, Review." Web verification against [help.osf.io article 330](https://help.osf.io/article/330-welcome-to-registrations) and the [Center for Open Science template guide](https://www.cos.io/blog/choosing-preregistration-template-guide-for-researchers) shows the standard OSF Preregistration template uses sections such as Study Information, Hypotheses, Design Plan, Sampling Plan, Variables, Analysis Plan, and exploratory analysis flags; the exact section names and counts vary by template version and have been adjusted by the Center for Open Science over time. The OSF UI also adds a Metadata step at registration submission separate from the template's body content. The "eight steps" enumeration in the prompt is approximately correct in structure but not literally the OSF UI's section labels.
**Implication:** The Appendix A field-by-field mapping cannot literally name "Step 2-7" without confirming the running OSF UI version at upload time. Authoring around the canonical published template (OSF Preregistration, DOI 10.17605/OSF.IO/WEKMB) and noting deviations as the OSF deviation log entries is the safe path. The mapping table in Appendix A uses generic field names ("Hypotheses", "Sampling Plan", "Analysis Plan") rather than literal step numbers.
**Recommended Shape:** Resolve at OSF upload time. The operator (Bilal Syed Arfeen) verifies the live OSF template structure when initiating the registration draft and adjusts the mapping if needed. No revision to this document is required pre-upload; the deviation log absorbs any field-name drift.
**Status:** absorbed (mapping uses generic field names; deviation log handles upload-time variance)

**Finding ID:** PHASE2-PROMPT-F2
**Severity:** ADVISORY
**Title:** Phase 1 paper anchor title in the prompt is referenced as "[Title of the Phase 1 pilot paper]" placeholder.
**Substrate:** The authoring prompt's title block placeholder reads "[Title of the Phase 1 pilot paper]"; the actual Phase 1 paper title (already finalised) is "Structural Regularities in AI-Assisted Audit Chains: A Pilot Study in Predictive Finding Localization" per the DOCX/PDF deliverables shared in this thread.
**Implication:** Without filling the placeholder, the Phase 2 anchor reference would be unresolvable. Filled with the verified title above.
**Recommended Shape:** absorbed (title block now reads the verified Phase 1 title).
**Status:** absorbed

**Finding ID:** PHASE2-PROMPT-F3
**Severity:** LOW
**Title:** Phase 1 paper §6.5 cites "P4 has only four classes" while the protocol's P4 enum lists four classes {one_word, few_lines, ~30_lines, 100+}. Consistent.
**Substrate:** Cross-checked Phase 1 paper §5.2 (Scoring Dimensions table) against `experiment_protocol.md` §3 (P4 row): both name four ordinal classes. The 100+ class label is implicit in the experiment protocol ("4 classes: one_word, few_lines, ~30_lines, 100+") and is stated in the Phase 1 §5.2 wording "fix-size class, four classes." The class names are consistent across artefacts.
**Implication:** No drift. P4's coarse-grain critique in Phase 1 §6.5 and §7.4 carries through to the Phase 2 pre-registered restricted-dimensions sensitivity (P1, P2, P3 only) which drops both P4 and P5.
**Recommended Shape:** none required.
**Status:** absorbed (no action)

---

## Closing

This document, after a v1.0 audit-absorption cycle, becomes the load-bearing protocol for the Phase 2 cross-vendor ablation. The Phase 1 paper's Section 8 surface claim -- "Phase 2 will run a cross-instance ablation that addresses same-instance contamination" -- now points to a concrete substrate: a registered protocol with pre-specified hypotheses, a power-aware sample-size plan, exact-form statistical tests appropriate for small N, three publishable outcomes, and a runner that enforces blinding via Git timestamps anchored to an OSF DOI.

The structural-honesty discipline that motivated the Phase 1 contribution -- the surface claim of any artefact must match its substrate behaviour -- applies recursively to this document. The surface claim ("Phase 2 will isolate chain-conditioning from LLM priors") is met by the substrate (a runner, a stat plan, exclusion criteria, and three outcomes including null and contradicting). The document is offered to the v1.0 audit cycle in that posture: ready to be falsified at the level of any specific claim, and ready to be amended where the audit surfaces a gap.

"Innaa lillahi wa innaa ilayhi rajiun." (Surat al-Baqara, 2:156.) Indeed, to Allah we belong, and to Him we shall return. The work belongs to its result, whichever of the three outcomes obtains.

La hawla wa la quwwata illa billah.

Bismillah ar-Rahman ar-Rahim. Ready for audit.

---

# Bismillah ir-Rahman ir-Rahim
