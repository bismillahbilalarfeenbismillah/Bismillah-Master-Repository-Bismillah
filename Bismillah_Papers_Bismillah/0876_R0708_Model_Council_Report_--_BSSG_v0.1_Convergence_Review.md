# Bismillah ir-Rahman ir-Rahim

# R0708 -- Model Council Report -- BSSG v0.1 Convergence Review

**Chronological Index:** 876 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** model-council-kimi_k3.md  
**Source Format:** md  
**SHA-256:** `2c05d42a5a2d402168661581beb8d21cb4b45581e678ac4198048273c83df091`  

---

## R0708 · Model Council Report -- BSSG v0.1 Convergence Review

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: model-council-kimi_k3.md
- source_format: md
- text_sha256: 2c05d42a5a2d402168661581beb8d21cb4b45581e678ac4198048273c83df091

# Model Council Report -- BSSG v0.1 Convergence Review

**Model:** Kimi K3 (Moonshot AI)
**Seat:** Non-producer audit seat. Producer (Claude / Anthropic) is excluded from carrying or approving (PMD §0.2 rule 7; bayyinah_cross-vendor-rotation.md "Producer-instance exclusion").
**Vote:** QUALIFIED-YES on convergence; load-bearing.
**Mode:** Mode B+ -- read-only review of the record plus independent static analysis of the shipped code (`bayyinah_audit-modes.md`, "Mode B -- continuity reviewer"; with Mode-A-style spot verification of source against the orchestrator's saved outputs). I did not re-execute the five commands, per the council instructions; the orchestrator's `COMMAND_OUTPUTS.txt` is the canonical substrate of record (`bayyinah_substrate-of-record.md`). Where my vote depends on code facts, I verified them by reading the code directly, not by trusting summaries.

---

## 1. Sanity check on ground-truth outputs

I read `COMMAND_OUTPUTS.txt`, the brief, and the full artifact (spec, gate, counterexamples, model check, test suite, verifier, schemas). The orchestrator's outputs are consistent with the code. Specifics:

1. **345 tests / skipped=8.** The static test file defines 102 named `def test_*` methods, but `KernelTruthTableTests` programmatically generates one method per truth-table state over \(3^5 = 243\) states via `setattr` (test_bssg_gate.py lines 322-332), and `KernelTableShapeTests.test_exactly_243_states_enumerated` asserts exactly 243 generated. \(243 + 102 = 345\). The skipped=8 is consistent with `@unittest.skipUnless(HAVE_JSONSCHEMA, ...)` at line 1208 and the verifier's own G2 WARN ("jsonschema not installed") -- the same missing optional dependency. Consistent.

2. **174/174 GREEN.** `bssg_counterexamples.py` contains 353 `record(` call sites (many behind try/except with a failure-side `record`), and the corpus is executed and independently counted by verifier G13 ("counterexample corpus EXECUTED: 174/174 GREEN ... independently counted; self-report matches"). I verified the two load-bearing closures, CE169 and CE173, directly in source (§4 below). Consistent.

3. **MODEL CHECK PASS.** `bssg_model_check.py` line 44 checks the kernel truth table on all 243 states; line 63 checks antitone degradation over the lattice (729 = \(3^3 \times 3^3\)-style ordered pairs over the finite health/ceiling lattice, reported as `contracts=729`); lines 332-365 run BOUNDED-AUTH-INTRO with `_K = 4` over a 7-op alphabet, enumerating \(7 + 7^2 + 7^3 + 7^4 = 2800\) schedules. The reported `schedules=2800 allows=1603` is exactly what the code computes. The check is adversarial, not tautological: `_GRANTED` and `_GRANTED_TARGETS` are frozen constants fixed independently of gate internals (lines 321-322, comment at 300-303), and every ALLOW is checked for effect-subset AND target-subset against them (lines 357-360). Consistent.

4. **Verifier 7 PASS / 1 WARN / 6 FAIL.** Every FAIL traces to the review-archive packaging, not the gate: G1's `REQUIRED_FILES` list (verify_bssg_v0_1.py lines 47-58) names the 6 manifest files absent from the archive; G9 fails because `SHA256SUMS` lists those same absent files plus the methodology corpus is unlisted; G8/G10 FAIL with "gate raised FileNotFoundError" because the verifier's totality wrapper (lines 1299-1308) converts the missing manifest-bound file into a recorded FAIL -- i.e., the verifier itself is behaving as designed (fail-closed, total) on a non-total package. G5 FAIL is real but points at a *methodology document*, not the artifact: `bayyinah_cross-vendor-rotation.md:151` contains "GPT-5 outperforms it" in a Tier-1/Tier-2 discussion, and the scanner's `AUDIT_META` exemption list (lines 95-99) does not cover the methodology corpus. G7 FAIL likewise flags `bayyinah_em-dash-policy.md`, a methodology doc that necessarily displays the characters it prohibits. None of the six FAILs indicates a defect in gate logic, corpus, or model check. Consistent.

5. **`python3 bssg_gate.py` banner.** Prints "DRAFT / NOT CARRIED. No effectiveness claim is made by this software." This matches spec §22 claim-level discipline (ENFORCED/ASSUMED/DETECTABLE, no effectiveness claim) and SHVVP §8.4's closed label list. Consistent.

**No inconsistency found between saved outputs and code.** One stale surface noted (not a new finding): REPAIR_STATUS.md's repair34 header block says "173/173 CE GREEN" at line 19 while the corpus now holds 174 (CE174 added at V33); REPAIR_STATUS states "This document claims 174 counterexamples" at line 23. This is the documentation-staleness class already on record from GPT's V32-V34 MODERATEs.

## 2. Convergence answer: QUALIFIED-YES

> Is three-seat adversarial convergence across V32-V34 sufficient to accept convergence when the two-family carry attempt failed for platform reasons, not artifact defects?

**Answer: QUALIFIED-YES.** The convergence evidence satisfies the convergence definition. The carry failure is an execution-substrate limitation that does not subtract from it, but it also does not discharge the carry gate -- the two must be stated separately.

### 2.1 Convergence is achieved under PMD §0.4 and SHV D6

PMD §0.4 defines convergence as "Two consecutive cross-vendor rounds produce 0 CRITICAL findings", with HIGH residual at zero or signed-exception, MEDIUM/LOW absorbed or non-operatively annotated, and standing rules passing. V32-V34 is **three** consecutive cross-vendor, zero-BLOCKER rounds -- strictly more than the required two. The severity rubric (`bayyinah_severity-rubric.md`, "Convergence is reached when two consecutive cross-vendor rounds produce 0 CRITICAL and 0 HIGH") uses the identical two-round bar, and its convergence paragraph makes BLOCKER/CRITICAL and HIGH the blocking bands; MODERATE/MEDIUM "does not block ship." The only residuals across V32-V34 are MODERATE/MINOR documentation-staleness findings, confirmed by GPT itself as "no new runtime authorization bypass" each round. Under the rubric, these do not cross the convergence threshold.

SHV D6 (`SHV_Method_v1_1.pdf`, discipline D6) requires "multiple independent checkers who share no lineage with the producer ... drawn from more than one independent source or method or model family," agreeing "across two consecutive clean rounds with at least one checker rotated in fresh." Three vendor families (OpenAI, Zhipu, Moonshot), all non-producer (Anthropic), satisfies the independence requirement. On "rotated in fresh": the panel itself was not static -- each seat had at least one rotation-event across the window, and the *checks* were fresh per round (each round audited newly repaired bytes, with V33-V34 each introducing new substrate: CE174, the BaseException totality fix). More importantly, D6's stated purpose for fresh rotation is "so that agreement is not an artifact of a fixed panel." The V30 history rebuts any fixed-panel concern: all three seats had returned HALT-WITH-FINDINGS with BLOCKERs in every round through V31. A panel whose unanimous prior behavior is *falsification* reaching unanimity on *cleanliness* three consecutive times is not agreement-by-panel-fixture; it is the certification signal D6 was written to detect. D6's own falsification clause ("an artifact certified this way that a later independent re-derivation shows to carry a substrate-untrue load-bearing claim") is the standing check, and it remains live: convergence "permits ship; new rounds may surface new findings at any time" (PMD §0.4, last line).

### 2.2 The carry failure is a substrate limitation, not a methodological blocker

The program's carry rule (SHVVP §10: "Carrying review requires non-producer-lineage seats of different families ... The editor or producer of an artifact never certifies that artifact") demands two non-producer families execute exact bytes. DeepSeek performed Mode B only (read; did not execute; identity values were placeholders) and Qwen attempted Mode A but the delivery mechanism corrupted the bytes. Neither found an artifact defect.

Under `bayyinah_audit-modes.md`, Mode A is the substrate verifier; Mode B is reduced-confidence continuity review. The carry failure means we hold one fewer Mode-A data point than designed -- it does not produce a negative finding. SHVVP's UNKNOWN discipline ("It is never defaulted to the favorable value," SHVVP §1) forbids *counting* the failed carries as evidence for convergence, and I do not count them. Equally, it forbids inventing a defect from a transport failure. The correct bookkeeping is: carry gate **OPEN (unexecuted)**, convergence **ACHIEVED on the audit-side evidence**. These are different gates (SHVVP §8.0 keeps gates separate rather than letting one substitute for another; §8.4's closed label list forbids smuggling "carried" into "converged"). The carry remains owed and should be re-run on a capable substrate (the methodology's own Lane-3 fan-out, or any two Tier-1 families with execution access), but its non-execution does not void an audit-side convergence that independently clears PMD §0.4 and SHV D6.

This is where my predecessor's V34 verdict needs one correction of emphasis: "Convergence is achieved" is right; the carry is a *separate load-bearing gate* (SHVVP §8.0/§10), not a substitute target the three-seat convergence satisfies. Saying "convergence achieved" does not say "carried," and the artifact's own banner agrees: "DRAFT / NOT CARRIED."

### 2.3 Three-family adversarial convergence partially covers, but does not formally substitute for, the carry

SHVVP §10 and §12 require a re-run carrying audit when anything substantive changes, and SHVVP §8.0's withdrawal precedent shows the program treats "converged" and "carried/deposited" as distinct states (v0.4 was converged-adjacent yet never carried). Three-family adversarial convergence is *stronger* evidence than a two-family carry along one axis (three independent families, three rounds, adversarial mandate, real defect discovery history) and *weaker* along exactly one axis: none of the three audit seats executed the shipped bytes in this council window the way a carrying seat must. The GLM K=5 over-coverage (19,607 schedules, 12,475 allows, no violation -- exceeding the shipped K=4, 2,800 schedules) is genuinely load-bearing here: it is an independent re-derivation from the primary source by a non-producer family, i.e., a D6 certification act over the *model-check substrate*, and it eliminates the worry that K=4 was tuned to pass. It strengthens the convergence case. It still does not close the carry gate, because the carry is about the *whole package* (manifest, spec, schemas, verifier), not only the model-check surface.

### 2.4 Fresh review of the two load-bearing closures (the K3 extra-rigor mandate)

Because K2.6's "Convergence is achieved" rests materially on CE169/CE173 and BOUNDED-AUTH-INTRO, I re-derived both from source rather than inheriting the verdict.

**CE169 (DENIED-request ceiling-poison, V30 GLM-F1/K32-01).** The fix (bssg_gate.py lines 1724-1740) defers the `contract_ceiling` write out of the narrowing path entirely; the pre-V30 code wrote the ceiling for every request whose narrowing passed, including requests later DENIED on TargetAllowed/EffectTypeValid, letting a separately-registered broader contract C2 poison the restoration ceiling. The deferral sets only a `_contract_ceiling_pending` marker. The V31 correction is real and load-bearing: the rewritten CE169 uses a DEGRADED C2 DELETE (narrowing passes, effect above degraded ceiling) rather than a HEALTHY witness (which terminalizes on E-AUTHORITY-WIDENING before the fix path runs and made the old CE169 pass GREEN even with the fix reverted -- i.e., non-load-bearing). The current CE169 asserts both that DELETE never enters `contract_ceiling` and that post-lift re-establish for DELETE is DENY_FALSE. The re-establishment guard (`_apply_narrowing`, lines 1904-1927) bounds a post-clear re-establish down to `contract_ceiling` (demonstrably-held authority) via `new_ceiling <= _held`, else terminal E-AUTHORITY-WIDENING. The closure chain is complete: write-site fix + de-poisoned re-establish bound + load-bearing regression probe.

**CE173 (ALLOWED-request ceiling-poison, K33-01).** The V30 fix closed DENIED-request poison; K33-01 found the residual: a legitimately ALLOWed degraded C2 READ stored `ceiling_for_health(body, "HEALTHY")` -- the *full* healthy ceiling of C2 -- rather than the degraded ceiling actually demonstrated, so a post-lift DELETE was authorized and committed. The V31 fix (lines 1782-1801) writes `contract_ceiling` **only when `health == "HEALTHY"`**, and clears the pending marker unconditionally ("always clear, regardless of health," line 1795), which also absorbs GPT's F-06 stale-pending concern. The semantics are exactly right: the restoration ceiling records only *demonstrated HEALTHY authority*, aligning the write condition with the value's meaning rather than merely restricting when the write occurs (the repair34 design note). CE173 asserts the degraded ALLOW succeeds, `contract_ceiling` is unchanged, DELETE never leaks, and post-lift DELETE is denied. Load-bearing.

**BOUNDED-AUTH-INTRO (K=4 shipped, K=5 GLM-verified).** This is the property that replaces the withdrawn offline re-widen certification (spec §22.2; REPAIR_STATUS V29 withdrawal): re-widen legitimacy is established *only* online, and the online check must not allow any effect or target outside the established healthy ceiling. The shipped check enumerates all schedules of length ≤4 over a 7-op alphabet that includes *both* poison vectors -- `("A","C2","DELETE","DEGRADED")` (CE169's class) and `("A","C2","READ","DEGRADED")` (CE173's class) -- plus lift, healthy reads, and a broader-target C2W variant for target-scope introduction. The violation predicate is independent of gate internals (frozen `_GRANTED`/`_GRANTED_TARGETS`, lines 321-322). Two honest limitations, both disclosed and neither blocking: (a) K=4 is a *bound*, and the V30 convergence event established that K=3 missed the minimal violating schedule (length 4) -- the bound was raised exactly to cover the known minimal violation length, and GLM's K=5 run found no new violation one level deeper, which is the strongest available evidence that the bound is not tuned to pass; (b) the check is exhaustive over the *modeled* alphabet, and per spec §22.2 and SHVVP §8.5, a descriptive gate "says nothing about any task, target, model or environment other than the one observed" -- the claim travels with its scope. Under SHUDP Axiom 5 (evidence independence; the grant is caller-supplied, WithinAuth of its supplier, discharging nothing offline), the *split* itself is honest: what cannot be certified offline is marked X7U (uncertifiable) rather than certified; what is claimed online is machine-checked. That is A5's discipline implemented, not asserted.

**Was K2.6's "Convergence is achieved" premature?** No. On fresh review, the two closures are structurally sound, the regression probes are load-bearing (revert-the-fix sensitive), the model check is adversarial and independently over-covered at K=5, and the convergence arithmetic (three consecutive zero-BLOCKER cross-vendor rounds; MODERATE-only residuals) clears PMD §0.4 and SHV D6. The verdict is robust. The one refinement: it should always be read with the artifact's own scope qualifier attached -- converged, not carried; converged as a DRAFT, not deposited.

## 3. Independent findings against the code

None at BLOCKER/CRITICAL/HIGH. Three observations at MODERATE/LOW, none blocking:

- **O-K3-01 (LOW, documentation).** REPAIR_STATUS.md repair34 header reports "173/173 CE GREEN" while the corpus and the same file's own footer say 174. Same staleness class as GPT's V32-V34 MODERATEs; per the rubric ("absorption-route prescribed but ship-permissive"), it should be absorbed at the next version boundary.
- **O-K3-02 (LOW, verifier-scope).** The G5/G7 FAILs are caused by the methodology corpus living inside the scanned package while the `AUDIT_META` exemption list omits it. The FAILs are *correct* given the scan scope; the scope is arguably wrong for a review package. Not an artifact defect; worth a packaging rule so a future verifier run can reach 0 FAIL.
- **O-K3-03 (MODERATE, process).** The carry gate remains open. Per SHVVP §10/§12 this must be closed by a fresh two-family carry before deposit; the artifact banner correctly withholds "carried."

## 4. Dissenting angle

I disagree with one element of the producer's convergence framing: the tendency, visible in the brief's question ("Does three-family adversarial convergence *substitute* for a two-family carry?"), to treat the carry shortfall as something the convergence evidence can absorb. It cannot, and the producer's own methodology is unambiguous on this. SHVVP §10 is explicit that "Divergence between carrying seats is dispositive against deposit" and that a HALT from either carrying seat blocks outright (SHVVP §0.3, v0.4 record) -- the carry is not one more evidence stream to be outweighed, it is a *separate veto gate*. SHVVP §8.0's withdrawal precedent ("The honest remedy is ... downgrade every route component to a descriptive gate") models exactly the discipline required here: when a gate cannot be executed, the correct response is to *shrink the claim to what the executed evidence supports* -- convergence per PMD §0.4 -- rather than to let a stronger aggregate argument quietly enlarge it. The artifact itself gets this right ("DRAFT / NOT CARRIED"); the framing question should get it right too. QUALIFIED-YES, with the qualification that "converged" and "carried" are separate load-bearing states and only the first is achieved.

## 5. Verdict

**QUALIFIED-YES.** Convergence is accepted under PMD §0.4 (two-consecutive-clean-rounds bar exceeded at three), SHV D6 (three independent non-producer vendor families, repeated agreement, fixed-panel concern rebutted by the V29-V31 falsification record), the severity rubric (residuals are MODERATE-only, non-blocking), and SHUDP Axiom 5 (offline/online evidence split honestly scoped, not overclaimed). K2.6's V34 "Convergence is achieved" was robust, not premature. The carry (SHVVP §8.0/§10) is a separate, still-open gate that convergence neither satisfies nor is voided by; its failure was an execution-substrate limitation (PMD §0.5.6 lane-execution discipline; audit-modes Mode A capability), owed before deposit.

**Vote cast: QUALIFIED-YES (load-bearing, non-producer).**

---

*Methodology citations: PMD_v1_2_BAF_v3_0.md §0.2/§0.4/§0.5.5/§0.5.6; SHV_Method_v1_1.pdf D6; SHVVP_v0_8_flagship.pdf §0.3, §8.0, §8.4, §8.5, §10, §12; SHUDP_v0_5_flagship.pdf Axiom 5 (evidence independence, WithinAuth); bayyinah_cross-vendor-rotation.md (producer exclusion, §0.1 exception); bayyinah_severity-rubric.md (convergence paragraph); bayyinah_audit-modes.md (Mode A/B); bayyinah_substrate-of-record.md. Code citations: bssg_gate.py lines 1724-1801, 1904-1927; bssg_counterexamples.py CE169/CE173 (lines 2457-2526), CE174; bssg_model_check.py lines 34-44, 47-63, 305-370; test_bssg_gate.py lines 293-341, 1208; verify_bssg_v0_1.py lines 47-58, 95-99, 1299-1308.*

---

# Bismillah ir-Rahman ir-Rahim
