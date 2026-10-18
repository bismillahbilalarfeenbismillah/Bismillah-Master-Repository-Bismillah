# Bismillah ir-Rahman ir-Rahim

# R0554 -- APE_REGISTER, anti-pattern register for the NeuroGolf chain

**Chronological Index:** 819 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** APE_REGISTER.md  
**Source Format:** md  
**SHA-256:** `c44761e12c5da1c729fc94543e32f8d83af471b629d15d8008a4fcc535e03c2e`  

---

## R0554 · APE_REGISTER, anti-pattern register for the NeuroGolf chain

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: APE_REGISTER.md
- source_format: md
- text_sha256: c44761e12c5da1c729fc94543e32f8d83af471b629d15d8008a4fcc535e03c2e

# APE_REGISTER, anti-pattern register for the NeuroGolf chain

Live append register. Each session that surfaces a new APE lands the entry here
before session close, per the Zilzal-close discipline added at NG-1 F4 closure.

Each entry follows the BAF v4.0 §10 documentation discipline (added at NG-2 D11
closure): origin (cont session or document section), one-sentence empirical
example or reproducer pointer, prevention.

---

## APE-1: Equal on float in opset 10

**Origin:** pre-cont33 chain experience, documented in cont45 ONNX_GOTCHAS.md.

**Empirical example:** ONNX opset 10 Equal supports only integer types. Calling
Equal on float tensors fails registration or silently mis-compares.

**Prevention:** Use `M = 1 - Clip(Abs(v - k), 0, 1)` for integer-valued floats
(P-110), or cast to int64 before Equal. See ONNX_GOTCHAS in cont45 archive for
full op-availability table.

---

## APE-2: ArgMin/ArgMax not profiler-registered

**Origin:** pre-cont33 chain experience, documented in cont45 ONNX_GOTCHAS.md.

**Empirical example:** 20 saves with ArgMin/ArgMax cause score_file to return
None locally (NG-1 F2). Kaggle's profiler accepts these ops; the local profiler
does not.

**Prevention:** Use the argmax-without-ArgMax pattern in PRIMITIVES.md (P-140,
P-141). For saves that already use ArgMin/ArgMax, document under MARAD-10 and
treat the local score_file failure as a known false negative.

---

## APE-3: Sequential mutation in ONNX iterative loops

**Origin:** cont48-cont49 P-NEW17 shared-substrate CC propagation. Documented
in dossier §9.

**Empirical example:** When propagating CC labels iteratively, reading and
writing the same tensor in a loop body produces incorrect labels because the
update is not atomic across the iteration. Specifically, in iter k, all
direction reads must use the same iter_start tensor; the accumulator updates
separately. A naive in-place mutation produces a "race condition" where later
direction reads see partial updates from the same iteration.

**Prevention:** Each iteration explicitly preserves iter_start at the top of
the iteration and reads from it for ALL direction operations. The accumulator
is a separate tensor that updates after all reads complete.

---

## APE-4: Padded-cell collision with all-zero one-hot

**Origin:** cont48-cont49 P-NEW17. Documented in dossier §9.

**Empirical example:** Cells outside the actual ARC grid are encoded as all-zero
one-hot (no channel set). This is structurally indistinguishable from "channel 0
absent" without explicit handling, leading to incorrect bbox computations,
spurious "background" detection, and CC propagation across the padding boundary.

**Prevention:** Compute `in_grid_mask = ReduceSum(input, axis=channel)` to
distinguish padded cells (mask=0) from in-grid cells (mask=1). Multiply all
position-dependent computations by in_grid_mask before reduction.

---

## APE-5: Equal on float (opset 10), reaffirmed

**Origin:** cont55+ rediscovery during P-NEW17.5 development. Documented in
dossier §9.

**Empirical example:** Equal in opset 10 requires int64 inputs. Float comparison
silently fails or returns incorrect bool tensors. Specific instance: Equal on
size_count vs size_target where both were floats produced all-False.

**Prevention:** Cast both operands to int64 before Equal, OR use `(v >= k) AND
(v <= k)` decomposition via Less + Greater + arithmetic. The latter avoids the
int64 round-trip.

---

## APE-6: Premature SAVED claim before all five gates

**Origin:** cont50 quantization sweep. Documented in dossier §9.

**Empirical example:** A save was claimed SAVED after passing test_network only,
without verifying score_file or file size. The save subsequently failed
score_file silently (it was a quantization that broke profiler invariants),
producing a phantom save that took zero correctness errors but zero Kaggle score.

**Prevention:** Five-gate check is non-negotiable before any SAVED claim:
test_network, score_file, file size, furqan-lint, build-script-plus-sidecar.
Automated CI gate added at NG-1 F2 closure (test_all_saves_correct.py and
test_all_saves_score.py).

---

## APE-7: Inflated PARTIAL severity

**Origin:** cont47 architectural-ceiling deferral. Documented in dossier §9.

**Empirical example:** A PARTIAL was classified HIGH when it was actually
MEDIUM-shape: "primitive cannot be built in opset 10" is a structural blocker
for that primitive but does not block the chain. Classifying it HIGH would
have escalated session attention to a deferred-anyway item.

**Prevention:** PARTIAL severity classification follows BAF v3.0 §3 rubric:
HIGH only if it would block release / generate hotfix / be unacceptable to
defer one cycle. Architectural ceilings are MEDIUM by default.

---

## APE-8: Branching primitives blocked in opset 10

**Origin:** cont51 visual-prior triage. Documented in NEUROGOLF_HYBRID_STRATEGY_GUIDE.md
Part 6.

**Empirical example:** Several pending tasks require Loop, Scan, or NonZero ops
which are not in opset 10. Attempting to mechanize these via gating + selectors
produces graph blow-up that violates the 1.44 MB cap.

**Prevention:** §11.4 Q3 explicitly checks for banned ops (Loop, Scan, Function,
NonZero, Unique). If the primitive requires any of them, it is structurally
infeasible in opset 10 and must be either decomposed differently or moved to
the deferred list.

---

## APE-9: Color-blind cc_id collision

**Origin:** cont58 task364 nested-CC detection. Documented in cont58_summary.md.

**Empirical example:** Connected component IDs computed as `cc_id = rmin * 32
+ cmin` collide across colors when two different-colored CCs share the same
top-left corner. Specifically, an L-shape at (0, 0) and a bg CC at (0, 0)
produced the same cc_id.

**Prevention:** Use color-aware cc_id encoding: `cc_id = color * 1024 + rmin
* 32 + cmin`. The color factor (1024) exceeds the maximum possible (rmin * 32
+ cmin) value, ensuring no cross-color collision.

---

## APE-10: Bbox via "any in row times any in col" outer-product fails on occlusion

**Origin:** cont59 task293 (NG-1 F1 substrate). Documented in cont59_summary.md
Lessons section.

**Empirical example:** Computing per-color bbox as `presence_per_row[ch] *
presence_per_col[ch]` (outer product of per-row and per-col masks) gives an
empty intersection when one color partially OCCLUDES another. The 3-color
horizontal bar in task293 train[0] had 88-vertical occluding cols 3-4; the
"any in row" check for color 3 missed those columns (color 3 absent there),
collapsing the bbox.

**Prevention:** Compute bbox via min/max of pixel positions, not via "any in
row/col" outer product. Use masked ReduceMin/ReduceMax with `(1-input)*BIG`
sentinels. See P-NEW21 implementation in cont59_saves/build293.py.

---

## APE-11: Opset 10 lacks GreaterOrEqual/LessOrEqual/float-Equal

**Origin:** cont59 task293 (NG-1 F1 substrate). Documented in cont59_summary.md
Lessons section.

**Empirical example:** Building bbox-mask required `row_idx >= rmin AND row_idx
<= rmax`. Opset 10 has no GreaterOrEqual or LessOrEqual; Equal is int64-only.

**Prevention:** Use `(x >= k) is NOT (x < k) is 1 - cast(Less(x, k), float)`.
Use `Greater(sum, k+0.5)` instead of `Equal(sum, k+1)` to avoid int64 cast
overhead (combines with APE-5 workaround).

---

## APE-12: Local-glob substitute for saved_list authority

**Origin:** cont59 task293 (NG-1 F1). Canonical text from NG-1 closure ledger.

**Empirical example:** cont59 pre-build save check used `glob(cont*_saves/task*.onnx)`,
returning 22 saves; missed the 312 pre-cont33 inheritance saves in cumulative
solutions/, including task293 already shipped at score 12.19. The cont59 rebuild
scored 10.89, 1.30 points worse, and was claimed as "+1 delta".

**Prevention:** Every session opens by reading saved_list.txt; pre-flight Q0
fails if the target task is in saved_list and `expected_new < current +
REBUILD_THRESHOLD` (default 0.5 score points, v0 placeholder pending empirical
calibration in cont61+ post-ship audit). Q0 is the FIRST question in §11.4
pre-flight; Q1 through Q5 stay structurally feasibility-focused.

---

## How to add a new APE

When a session surfaces a new failure pattern that future sessions could
repeat:

1. Number it APE-N (continue from APE-12).
2. Add a section here with origin, empirical example, prevention.
3. Land the entry BEFORE session close, not just in cont summary.

Per the cont60 NG-1 F4 closure: APEs must land here before session close.
The auto-loaded manual must track the chain, not lag it.

This register replaces the cont45-era ONNX_GOTCHAS.md (retired at NG-1 F4
closure). Pre-cont33 op-quirks information is in cont45 archive for reference.

---

# Bismillah ir-Rahman ir-Rahim
