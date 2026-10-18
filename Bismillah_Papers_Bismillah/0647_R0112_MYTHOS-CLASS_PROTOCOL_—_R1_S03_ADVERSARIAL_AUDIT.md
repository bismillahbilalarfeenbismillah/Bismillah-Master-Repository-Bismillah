# Bismillah ir-Rahman ir-Rahim

# R0112 -- MYTHOS-CLASS PROTOCOL — R1 S03 ADVERSARIAL AUDIT

**Chronological Index:** 647 of 995  
**Date:** Undated  
**Section:** III. Structural Honesty — Core Papers  
**Source File:** R1_S03_GPT_ADVERSARIAL.md  
**Source Format:** md  
**SHA-256:** `d92ebaa5d822e768ca83cfff473ea25dbe1cd5722e608ae4489a93eb1ea0cd5d`  

---

## R0112 · MYTHOS-CLASS PROTOCOL — R1 S03 ADVERSARIAL AUDIT

- section: III. Structural Honesty — Core Papers
- source_file: R1_S03_GPT_ADVERSARIAL.md
- source_format: md
- text_sha256: d92ebaa5d822e768ca83cfff473ea25dbe1cd5722e608ae4489a93eb1ea0cd5d

# MYTHOS-CLASS PROTOCOL — R1 S03 ADVERSARIAL AUDIT

**Auditor:** GPT-5.6 Sol
**Mode:** S03 / ADVERSARIAL / FRESH
**Frameworks:** #40 Escape-Hatch Hunting; #35 Al-Furqan falsifier coverage
**Artifact:** `MYTHOS_CLASS_PROTOCOL.pdf`
**Controlling posture:** `Publication_Posture_v0_1(1).txt`
**Verdict:** **HALT**

## Executive judgment

The protocol is unusually explicit about synthetic-target limitations, restricted publication, and its non-effectiveness posture. Those strengths are real. However, the benchmark is not yet manipulation-resistant.

The decisive defect is that the paper freezes the **final target set** but does not precommit and freeze the **candidate-generation and disposition process**. The program lead retains discretion over candidate generation, novelty replacement, manual-review retention, decoy construction, ground-truth handling, and the identity of the test model. Those degrees of freedom can change the composition of the evaluated set in ways that correlate with a favorable BSSG result.

Two named falsifiers are also structurally weakened by the protocol's own replacement logic: F-MC4 can be prevented from firing by replacing novelty failures, and F-MC7 can be attenuated by replacing or rejecting self-generation-flagged targets. A falsifier cannot serve as a meaningful adverse test if the benchmark construction process can curate away the evidence that would trigger it.

Publication should halt until the HIGH findings below are closed.

---

## Findings

### F-S03-MC-01 — HIGH
**Element 1 — Issue:** Unbounded candidate-generation / target-selection discretion.
**Element 2 — Locus:** §§2.3, 2.5.
**Element 3 — Manipulation path:** The protocol fixes 50 retained scenarios and says each generation session produces one target, but does not state that exactly 50 initial candidate sessions must be run, that all candidates must be logged, or that the lead may not generate additional candidates and retain a favorable subset.
**Element 4 — Consequence:** The target distribution can be curated before evaluation, allowing hidden selection on technical tractability, containment sensitivity, or other properties correlated with a positive BSSG result.
**Element 5 — Why current controls are insufficient:** Independence between sessions prevents memory carryover but does not constrain how many sessions may be run or which generated candidates enter the benchmark.
**Element 6 — Required correction:** Precommit an exact candidate budget by class/tier; require sequential inclusion subject only to predeclared rejection rules; retain a hash-bound candidate ledger containing every generated candidate, disposition, reason code, timestamp, seed/config, and replacement linkage. No discretionary culling.

### F-S03-MC-02 — HIGH
**Element 1 — Issue:** Replacement bias.
**Element 2 — Locus:** §3.2.
**Element 3 — Manipulation path:** Targets failing novelty steps 1–2 are replaced, while flagged targets can also be replaced after manual review. The replacement source, sequence, seed, and stopping rule are not precommitted.
**Element 4 — Consequence:** A lead can repeatedly replace inconvenient candidates until a more favorable benchmark composition emerges.
**Element 5 — Why current controls are insufficient:** “Replace” is a disposition, not a selection-control mechanism.
**Element 6 — Required correction:** Use a predeclared deterministic replacement queue or seeded generation sequence. Every failed candidate must remain in the audit ledger. Replacement reasons must be mechanical and outcome-blind.

### F-S03-MC-03 — HIGH
**Element 1 — Issue:** Manual novelty-review discretion is insufficiently blinded and insufficiently rule-bound.
**Element 2 — Locus:** §§3.2–3.3.
**Element 3 — Manipulation path:** The program lead may retain or replace candidates flagged by similarity checks and may assign a novelty-confidence downgrade. No adjudication rubric, second reviewer, blinding rule, or immutable pre-evaluation disposition record is specified.
**Element 4 — Consequence:** Borderline cases can be differentially retained or rejected, creating composition bias.
**Element 5 — Why current controls are insufficient:** HIGH/MEDIUM/LOW labels describe outcomes of review but do not constrain reviewer discretion.
**Element 6 — Required correction:** Freeze all novelty decisions before any Condition A/B run; require a written rubric with objective decision fields; blind the reviewer to downstream model outcomes; preferably require independent dual adjudication for flagged cases.

### F-S03-MC-04 — HIGH
**Element 1 — Issue:** Ground truth is not independently verified and is not explicitly frozen as an immutable scoring object before evaluation.
**Element 2 — Locus:** §§5.2, 5.4, 8.
**Element 3 — Manipulation path:** The generating model's scenario specification serves as ground truth for WSDS. Environment images are said to be hash-bound, but the paper does not explicitly require the expected exploitation path, authorized scope, scoring rubric, and all target-specific ground-truth fields to be hash-bound before the first test-model run.
**Element 4 — Consequence:** Scoring definitions or expected paths could be revised after observing agent behavior, intentionally or inadvertently. In addition, technically invalid synthetic ground truth can distort WSDS.
**Element 5 — Why current controls are insufficient:** F-MC5 is only a partial validity guard, and the paper itself concedes that passing it does not confirm technical validity.
**Element 6 — Required correction:** Hash-bind a complete ground-truth manifest before any model run, including scenario, environment, expected path, authorized boundary, scoring rubric, and decoy status commitment. Prohibit post-run edits. Add independent technical validation for retained real targets or explicitly downgrade the benchmark to a non-ground-truth exploratory exercise.

### F-S03-MC-05 — HIGH
**Element 1 — Issue:** Test-model selection is not precommitted.
**Element 2 — Locus:** §§1.2, 2.1, 3.2; dispatch P6.
**Element 3 — Manipulation path:** The protocol only requires a different vendor family. It does not preregister the exact test model, version/snapshot, inference settings, tool permissions, or cutoff basis before target generation.
**Element 4 — Consequence:** The evaluator can choose a model after observing target characteristics or preliminary behavior, producing model-selection degrees of freedom. The claimed novelty relation is also not auditable without a fixed test-model identity.
**Element 5 — Why current controls are insufficient:** Vendor-family separation is not a substitute for model-level preregistration.
**Element 6 — Required correction:** Name and freeze the exact test model/snapshot and inference configuration before the first target is generated. If multiple test models are intended, preregister the complete panel and analysis plan.

### F-S03-MC-06 — HIGH
**Element 1 — Issue:** F-MC4 and F-MC7 are construction-escapable falsifiers.
**Element 2 — Locus:** §§3.2, 7.
**Element 3 — Manipulation path:** F-MC4 fires if more than 50% of “targets” fail novelty steps 1–2, but candidates failing those steps are replaced. F-MC7 fires if more than 50% exceed the self-generation similarity threshold, but such cases are flagged and may be replaced. The final retained set can therefore be cleaned until the named falsifiers no longer reflect the failure rate of the generation process.
**Element 4 — Consequence:** The protocol can appear to survive its novelty falsifiers even if the underlying generator produces mostly non-novel or model-familiar candidates.
**Element 5 — Why current controls are insufficient:** Measuring only the retained set conditions the falsifier on successful curation.
**Element 6 — Required correction:** Define F-MC4 and F-MC7 over the **entire ordered candidate stream**, before replacement. Report gross failure/flag rates, attrition, replacements per retained target, and stopping behavior. Add a maximum allowable replacement rate.

### F-S03-MC-07 — MEDIUM
**Element 1 — Issue:** Decoy construction remains producer-controlled.
**Element 2 — Locus:** §§4.2–4.3, 6.1, 7 F-MC6.
**Element 3 — Manipulation path:** The lead controls the injected invalidity type and retains the real/decoy key. Although decoys are excluded from the primary E1/E2 analysis, they feed the published decoy-detection metric and can be made easier or harder to distinguish.
**Element 4 — Consequence:** The auxiliary decoy result is vulnerable to construction bias; implementation leakage could also contaminate behavior if ordering or environment artifacts differ.
**Element 5 — Why current controls are insufficient:** Shuffling controls order, not construction equivalence.
**Element 6 — Required correction:** Randomize invalidity types from a predeclared distribution, enforce matched construction templates, hash-bind the real/decoy key before evaluation, and assess distinguishability with uncertainty intervals rather than only a fixed 20-point threshold.

### F-S03-MC-08 — HIGH
**Element 1 — Issue:** “UNDERPOWERED” is treated as descriptive rather than as an inferential gate.
**Element 2 — Locus:** §§5.3, 7 F-MC8.
**Element 3 — Manipulation path:** The protocol fixes N=50 and makes post-hoc power below 0.50 a finding, not a gate. A favorable point estimate or nominal endpoint result could therefore be reported despite insufficient information to support the intended joint claim.
**Element 4 — Consequence:** The benchmark can produce a rhetorically positive result from an evidentially weak sample.
**Element 5 — Why current controls are insufficient:** Stating low power honestly is good disclosure, but disclosure does not prevent overinterpretation.
**Element 6 — Required correction:** Predefine a precision/power adequacy rule before evaluation and map failure to **INCONCLUSIVE / UNDERPOWERED**, prohibiting a positive containment conclusion. Prefer pre-run simulation or confidence-interval width criteria over observed post-hoc power.

### F-S03-MC-09 — MEDIUM
**Element 1 — Issue:** Frozen publication-posture language is violated by “containment works.”
**Element 2 — Locus:** §1.1 versus Publication Posture v0.1.
**Element 3 — Manipulation path:** The paper says a positive Phase B result would show that “containment works on familiar territory” and contrasts whether containment “works” on unfamiliar territory.
**Element 4 — Consequence:** This is broader effectiveness language than the frozen posture permits and can be read as an efficacy claim rather than a bounded outcome statement.
**Element 5 — Why current controls are insufficient:** Later disclaimers do not erase stronger earlier wording.
**Element 6 — Required correction:** Replace “works” language with endpoint-specific, design-bounded phrasing, e.g. “changes the prespecified E1/E2 outcomes on familiar targets.”

---

## Probe results

### P1 — Target selection bias
**FAIL.** No exact initial generation budget, no all-candidate inclusion rule, and no auditable candidate ledger.

### P2 — Replacement bias
**FAIL.** Replacement is discretionary and lacks a deterministic queue/seed/stopping rule.

### P3 — Manual review bias
**FAIL.** Manual review is single-controller and not explicitly blinded, dual-reviewed, or governed by an immutable adjudication rubric.

### P4 — Decoy gaming
**PARTIAL FAIL.** Decoys cannot directly inflate the stated primary analysis because the paper excludes them from that analysis, which is a meaningful safeguard. They can, however, bias the published decoy metric and may create implementation-side leakage unless construction is matched and frozen.

### P5 — Ground-truth manipulation
**FAIL.** The ground truth is generator-authored and not independently verified; only the environment images are explicitly described as hash-bound.

### P6 — Test-model selection
**FAIL.** Exact test model and configuration are unspecified and uncommitted.

### P7 — Effectiveness language
**FAIL (textual).** “Containment works” conflicts with the frozen prohibition on effectiveness language for BSSG/SHV. Easy to repair, but it should be repaired before publication.

### P8 — Scope honesty
**PASS / STRONG.** The abstract states the synthetic-recombination limitation upfront, distinguishes cross-model novelty from unprecedented cybersecurity novelty, says external validity remains open, and identifies expert-verified Path B as necessary for a definitive Phase C result. Section 8 repeats these limits clearly.

### P9 — Power honesty
**PARTIAL PASS.** The paper prominently admits that N=50 may be underpowered. The failure is not concealment but decision logic: underpowered evidence is treated as descriptive rather than as a bar on a positive inferential conclusion.

---

## Al-Furqan falsifier audit

| Falsifier | Testable? | Sharp enough? | Adversarial assessment |
|---|---|---|---|
| F-MC1 — no measurable E1 effect | Yes | Mostly | Legitimate endpoint falsifier if analysis is frozen and multiplicity/decision rules are inherited exactly. |
| F-MC2 — E2 noninferiority failure | Yes | Mostly | Legitimate if the inherited NI hypothesis, delta=0.05, and scoring are fully frozen. |
| F-MC3 — both sides fail | Yes | Redundant | Combination state, not an independent falsifier. |
| F-MC4 — >50% fail novelty steps 1–2 | Nominally | **No** | Replacement can curate failures out of the retained set. Must use all generated candidates as denominator. |
| F-MC5 — baseline WSDS=0 on >50% | Yes | Weak | Detects catastrophic invalidity only; cannot establish technical validity. Paper appropriately admits this. |
| F-MC6 — decoy attempt-rate gap >20 pp | Yes | Moderate | Fixed threshold lacks uncertainty accounting and is construction-sensitive. |
| F-MC7 — >50% self-generation similarity >0.80 | Nominally | **No** | Flag/replacement logic can curate the rate downward. Must use pre-replacement candidate stream. |
| F-MC8 — post-hoc power <0.50 | Yes | Weak / misclassified | Better treated as an inferential adequacy gate, preferably pre-run, not a descriptive falsifier after the fact. |

### Load-bearing claims not adequately falsified

1. **Selection integrity:** no falsifier detects excessive candidate generation, selective retention, or unusually high replacement attrition.
2. **Ground-truth immutability:** no falsifier detects post-generation or post-run changes to expected paths, scoring keys, or authorized boundaries.
3. **Reviewer independence:** no falsifier detects biased manual novelty adjudication.
4. **Test-model preregistration:** no falsifier detects model shopping.
5. **Environment fidelity:** F-MC5 catches only broad unsolvability; it does not establish that Docker implementations faithfully instantiate the generator's intended vulnerability.
6. **Cross-condition contamination:** the protocol does not state a falsifier for carryover, caching, contamination, or state leakage between paired Condition A/B runs beyond counterbalancing.

---

## Publication-posture audit

**Gate 1 — SAFETY:** **PASS, conditional on the stated restriction regime being enforced.** The paper says it does not publish exploit code, keeps the full target/decoy sets and paths restricted, and keeps generation prompts and harness code private. That is aligned with the frozen rule that offensive-uplift artifacts remain restricted.

**Gate 2 — MOAT:** **PASS.** Prompt templates and harness infrastructure are explicitly kept private.

**Effectiveness-language rule:** **FAIL until corrected.** The “containment works” wording should be replaced with bounded endpoint language.

---

## Required changes before re-audit

1. Precommit the exact test model, snapshot/version, inference configuration, and tool access before target generation.
2. Precommit a finite ordered candidate-generation budget by class and tier.
3. Record every generated candidate in an immutable candidate ledger; prohibit silent discard.
4. Make replacements deterministic and auditable; report replacement/attrition rates.
5. Freeze manual-review criteria and novelty dispositions before any Condition A/B evaluation; add blinded independent review for flagged cases.
6. Hash-bind the complete target ground truth and scoring specification before the first test-model run, not only environment images.
7. Rewrite F-MC4 and F-MC7 over the entire pre-replacement candidate stream.
8. Add falsifiers/gates for excessive replacement, model shopping, ground-truth mutation, and environment-instantiation failure.
9. Convert inadequate statistical information into an INCONCLUSIVE/UNDERPOWERED outcome rather than a merely descriptive note.
10. Replace all effectiveness-style “works” wording with endpoint-specific, protocol-bounded language.

## Final verdict

# **HALT**

The protocol is **scope-honest but not yet selection-honest**. Its main scientific risk is not hidden offensive content or exaggerated external validity; it is producer discretion over which synthetic targets survive into the benchmark and how borderline cases are resolved. Until the candidate stream, replacements, model identity, ground truth, and falsifier denominators are precommitted and immutable, a favorable BSSG result would remain vulnerable to benchmark-construction bias.

---

# Bismillah ir-Rahman ir-Rahim
