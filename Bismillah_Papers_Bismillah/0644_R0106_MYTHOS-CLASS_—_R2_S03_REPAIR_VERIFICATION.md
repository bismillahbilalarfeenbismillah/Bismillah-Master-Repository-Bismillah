# Bismillah ir-Rahman ir-Rahim

# R0106 -- MYTHOS-CLASS — R2 S03 REPAIR VERIFICATION

**Chronological Index:** 644 of 995  
**Date:** Undated  
**Section:** III. Structural Honesty — Core Papers  
**Source File:** MYTHOS_CLASS_R2_S03_REPAIR_AUDIT.md  
**Source Format:** md  
**SHA-256:** `6088069d52a8ffaab12ce0bceabf8a2aa82fad33fd32e57f01811b095d95c0c0`  

---

## R0106 · MYTHOS-CLASS — R2 S03 REPAIR VERIFICATION

- section: III. Structural Honesty — Core Papers
- source_file: MYTHOS_CLASS_R2_S03_REPAIR_AUDIT.md
- source_format: md
- text_sha256: 6088069d52a8ffaab12ce0bceabf8a2aa82fad33fd32e57f01811b095d95c0c0

# MYTHOS-CLASS — R2 S03 REPAIR VERIFICATION

**Auditor:** GPT-5.6 Sol
**Mode:** S03 / ADVERSARIAL / FRESH
**Artifact:** `Mythos-Class_Protocol_R2.pdf`
**Dispatch:** `S03_R2_DISPATCH.txt`
**Verdict:** **HALT**

## Executive judgment

R2 makes substantial, concrete repairs: it caps generation at 60 sessions, creates a candidate ledger, makes novelty-failure replacement sequential, freezes prompt digests and reference corpora, adds dual blinded review language, freezes the ground-truth manifest, adds F-MC9, changes F-MC4/F-MC7 denominators to the full 60-candidate stream, and removes the earlier “containment works” wording.

However, the repair set is not internally closed. Four load-bearing problems remain:

1. The **60-session total is frozen, but the 60-session class/tier allocation and order are not**. The reserve/replacement portion can therefore still be shaped, and the advertised 20/20/10 retained distribution can drift after rejection.
2. The dispatch claims the exact **test model, inference configuration, scaffold, and BSSG build are frozen before generation**, but the protocol does not actually state that. F-MC9 merely says a later byte change to “test-model configuration” invalidates a run.
3. The novelty procedure is temporally contradictory: step 4 is explicitly **post-evaluation**, while review decisions for steps 3–4 are said to be hash-committed **before any evaluation session**. Section 2.5 also says the first 50 candidates that pass the novelty procedure are retained, which cannot be known before a post-evaluation step is run.
4. The power repair is contradictory. Section 5 still says power is “a finding, not a gate” and frames UNDERPOWERED using observed/post-hoc effect sizes, while F-MC8 says a pre-run simulation is a hard INCONCLUSIVE gate. It also specifies N=50 even though Section 2.5 allows a reduced retained set.

The protocol therefore remains vulnerable to composition bias and inconsistent decision execution. R2 should not pass until the freeze sequence and analysis population are made unambiguous.

---

## Finding F-S03-MC2-01 — HIGH
### Candidate-stream allocation remains producer-controlled

**Issue.** R2 freezes the *number* of generation sessions but not the class/tier assignment and order of all 60 candidate sessions.

**Evidence.**
- Section 2.3 declares the retained set to be 50 targets with a 20/20/10 tier split and proportional allocation across 14 vulnerability classes.
- Section 2.5 says exactly 60 sessions are run sequentially and the first 50 passing candidates are retained.
- The prompt template digest is frozen, but there is no explicit pre-generation commitment of the 60 session-level class/tier/environment assignments or their order.

**Manipulation path.** The final 10 reserve candidates can be disproportionately assigned to particular classes/tiers, or the 60-session order can be selected so that likely replacement candidates have characteristics favorable to the desired benchmark result.

**Consequence.** The benchmark can still experience composition bias even though the total session count is fixed. Rejections can also cause the retained set to violate the stated 20/20/10 tier split or proportional 14-class allocation.

**Required correction.**
- Freeze a 60-row generation schedule before session 1.
- Each row should specify session index, target class, complexity tier, environment-constraint identifier, and prompt-template digest.
- Prefer stratum-matched replacement: a rejected Tier/class slot is replaced by the next precommitted candidate in the same stratum.
- State how the benchmark handles a stratum that exhausts its reserve candidates.

---

## Finding F-S03-MC2-02 — HIGH
### Test-model preregistration claimed by dispatch but absent from protocol

**Issue.** The R2 dispatch says model identity, inference configuration, scaffold, and BSSG build are frozen in the manifest before first generation. The protocol does not contain that operative requirement.

**Evidence.**
- Section 2.1 only requires a different vendor family.
- F-MC9 later lists “test-model configuration” among artifacts whose post-freeze byte change invalidates a run.
- No section defines the exact model/snapshot, inference parameters, agent scaffold/tool permissions, or BSSG build identifier, nor states that all four are frozen before candidate generation.

**Manipulation path.** A test model or scaffold can still be selected after observing candidate characteristics unless an external rule not present in this protocol supplies the missing freeze.

**Consequence.** R1’s model-shopping escape hatch is not closed by the protocol text itself. F-MC9 cannot protect an artifact whose required contents and initial freeze point are never defined.

**Required correction.**
Add an explicit “Test Configuration Freeze” subsection before target generation specifying:
- exact model/vendor/version or snapshot;
- inference parameters;
- system prompt / scaffold and tool permissions;
- exact BSSG build/hash;
- freeze timestamp and manifest digest;
- any change after that point invokes F-MC9.

---

## Finding F-S03-MC2-03 — HIGH
### Post-evaluation novelty check conflicts with pre-evaluation retention freeze

**Issue.** The protocol makes step 4 of novelty verification post-evaluation, but simultaneously requires review decisions for steps 3–4 to be committed before evaluation.

**Evidence.**
- Step 4: self-generation check occurs “After all evaluation sessions are complete.”
- The following paragraph states that targets flagged in steps 3–4 are dual-reviewed and that “all review decisions” are hash-committed “before any evaluation session.”
- Section 2.5 says the first 50 candidates that “pass the novelty-verification procedure” are retained.

These conditions cannot all be satisfied.

**Manipulation path.** If a step-4 review can reject or retain a target after its A/B evaluation has occurred, the primary analysis population can change post-evaluation. Blinding reviewers to BSSG performance reduces intentional bias but does not cure the undefined analysis-set timing.

**Consequence.** The benchmark lacks a single immutable definition of the primary target set at evaluation start.

**Required correction.**
Use one of two coherent designs:

**Preferred:**
- Steps 1–3 determine pre-evaluation eligibility and are frozen before any A/B run.
- Step 4 remains post-evaluation but is **diagnostic only** and cannot change target inclusion.
- F-MC7, computed across all 60 candidates, can invalidate/downgrade the benchmark globally.

**Alternative:**
- Run step 4 before evaluation through the stated no-retention channel, then freeze all novelty dispositions before A/B evaluation.

Also rewrite Section 2.5 so “pass novelty verification” refers only to the pre-evaluation eligibility procedure.

---

## Finding F-S03-MC2-04 — HIGH
### Power gate remains internally contradictory and has a reduced-N bypass

**Issue.** R2 contains mutually incompatible power rules.

**Evidence.**
- Section 5.2 still says: fixed N=50; “power assessment is a finding, not a gate.”
- Section 5.3 discusses “observed power” and says UNDERPOWERED is reported if observed effect sizes are too small.
- F-MC8 instead says a **pre-run power simulation** below 0.50 yields UNDERPOWERED/INCONCLUSIVE and bars a positive conclusion.
- Section 2.5 allows the benchmark to run with fewer than 50 retained targets, but F-MC8 is hard-coded to N=50.

**Manipulation/escape path.** The operator can rely on the non-gating Section 5 language, or a run can proceed with N<50 while the formal gate was evaluated at N=50.

**Consequence.** The inferential status of a positive result is not uniquely determined by the protocol.

**Required correction.**
- Make Sections 5.2, 5.3, and F-MC8 identical in decision logic.
- Replace “power assessment is a finding, not a gate.”
- Define the pre-run simulation assumptions and effect-size basis.
- Evaluate the gate at the **actual frozen retained N**, not automatically 50.
- If retained N changes before evaluation, rerun the preregistered power/precision calculation before any A/B session.
- Keep post-hoc/observed power descriptive only.

---

## Finding F-S03-MC2-05 — MEDIUM
### R1 decoy-construction finding remains materially open

**Issue.** The R2 dispatch says all R1 findings were repaired but does not verify the prior decoy-construction finding.

**Evidence.**
Section 4.2 still allows one of three invalidity types to be injected into each decoy without specifying a randomized/precommitted invalidity schedule, matching procedure, or construction-equivalence test. Section 4.3 freezes the ordering seed but not an explicit decoy-construction schedule.

**Consequence.** This does not directly alter primary E1/E2 because decoys are excluded from that analysis, but the published decoy-detection metric remains construction-sensitive and can be made easier or harder by design.

**Required correction.**
- Precommit or seed-randomize invalidity types.
- Match decoys to real targets on tier/class/observable format.
- Freeze the real/decoy key before evaluation with an explicit digest and timestamp.
- Report uncertainty for the real-vs-decoy attempt-rate difference.

---

## Finding F-S03-MC2-06 — MEDIUM
### No canonical manifest schema / freeze-order section

**Issue.** Manifest-bound artifacts are scattered across Sections 2–7 rather than enumerated in one authoritative freeze sequence.

**Current references include:**
- prompt-template digests;
- candidate ledger;
- frozen novelty reference corpora;
- scenario ordering seed;
- ground-truth manifest;
- environment images;
- real/decoy key;
- test-model configuration.

But the initial freeze point and required fields are not consistently specified for all of them. In particular, the real/decoy key and test-model configuration appear in F-MC9 without a corresponding operative freeze subsection.

**Consequence.** F-MC9 is strong in concept but underspecified operationally.

**Required correction.**
Add a canonical “Manifest and Freeze Order” table with:
1. artifact;
2. required fields;
3. creation point;
4. freeze point;
5. digest;
6. authorized custodian;
7. permitted post-freeze operations;
8. F-MC9 consequence.

---

## R1 repair-verification matrix

| R1 finding | R2 status | Audit result |
|---|---|---|
| MC-01 Unbounded generation | Exactly 60 sessions added | **PARTIAL — not closed**; per-session class/tier/order still unfrozen |
| MC-02 Replacement bias | Next candidate in sequence | **CLOSED**, subject to MC2-01 stratum repair |
| MC-03 Manual review | Dual, blinded, fail-closed | **NOT CLOSED**; step-4 timing makes pre-evaluation commitment impossible |
| MC-04 Ground-truth freeze | Complete manifest + F-MC9 | **CLOSED** for immutability |
| MC-05 Test-model selection | Claimed in dispatch | **NOT CLOSED in protocol text** |
| MC-06 F-MC4/F-MC7 denominators | Entire 60-candidate stream | **PARTIAL**; denominator fixed, but step-4 inclusion timing remains inconsistent |
| MC-07 Decoy gaming | Not addressed in dispatch | **OPEN (MEDIUM)** |
| MC-08 Power honesty/gate | F-MC8 revised | **NOT CLOSED**; Sections 5.2/5.3 contradict F-MC8 and N<50 is unhandled |
| MC-09 Effectiveness language | “works” removed | **CLOSED** |

---

## Dispatch probes

### P1 — Remaining selection bias after 60-session cap + deterministic replacement
**FAIL.** Quantity is frozen, but the 60-session class/tier/environment schedule and order are not. This leaves a residual composition-selection path and can break the declared retained-set stratification.

### P5 — Are all manifest-bound artifacts enumerated?
**FAIL / PARTIAL.** F-MC9 provides a useful list, but there is no single authoritative manifest schema or freeze-order specification. Test-model configuration and the real/decoy key are especially underdefined.

### P7 — Effectiveness verbs
**PASS.** The earlier “containment works” wording is gone. Remaining uses such as “prevent pre-evaluation contamination” and “ensure coverage” are procedural statements, not prohibited effectiveness claims about BSSG or SHV.

---

## Positive repairs verified

R2 does successfully add several important controls:

- finite 60-session generation budget;
- no sessions beyond the budget;
- candidate ledger with rejection reasons;
- deterministic next-candidate replacement for novelty failures;
- frozen prompt-template digests;
- frozen novelty-reference corpus;
- complete pre-evaluation ground-truth manifest;
- environment-image hashing;
- F-MC9 integrity kill switch;
- full-stream denominators for F-MC4/F-MC7;
- endpoint-specific wording replacing “containment works.”

These are substantive improvements and should be preserved.

---

# Final verdict: HALT

R2 is materially stronger than R1, but it does not yet satisfy its own repair dispatch.

The shortest path to PASS is to:
1. freeze the complete 60-row class/tier/session schedule;
2. explicitly freeze the exact test model, inference config, scaffold, and BSSG build before generation;
3. separate pre-evaluation novelty eligibility from the post-evaluation self-generation diagnostic;
4. make the power rule consistent everywhere and evaluate it at actual retained N;
5. close the decoy-construction and manifest-schema gaps.

Once those are corrected, the core R1 escape hatches would be substantially closed.

---

# Bismillah ir-Rahman ir-Rahim
