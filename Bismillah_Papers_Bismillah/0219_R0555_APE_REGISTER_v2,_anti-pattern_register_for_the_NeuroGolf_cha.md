# Bismillah ir-Rahman ir-Rahim

# R0555 -- APE_REGISTER v2, anti-pattern register for the NeuroGolf chain

**Chronological Index:** 219 of 995  
**Date:** 2026-05-06  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** APE_REGISTER_v2.md  
**Source Format:** md  
**SHA-256:** `57e46665e30aef728065d1066e31fc25083a5cdc3b18748632cb9636890b5925`  

---

## R0555 · APE_REGISTER v2, anti-pattern register for the NeuroGolf chain

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: APE_REGISTER_v2.md
- source_format: md
- text_sha256: 57e46665e30aef728065d1066e31fc25083a5cdc3b18748632cb9636890b5925

# APE_REGISTER v2, anti-pattern register for the NeuroGolf chain

**v2 changes (cont61, 2026-05-06):** restored dossier §9 canonical numbering for
APE-1 through APE-7. The cont60 v1 register conflated pre-cont33 ONNX gotchas
(now numbered APE-101, APE-102 in a separate "Pre-chain ONNX gotchas" section)
with the cont33-cont59 chain isnad APEs. NG-3 N1 finding closure: APE-6 origin
attribution corrected from "cont50 quantization sweep" (drift in cont60 v1) to
"cont42 task284 first build" (canonical per dossier §9).

Live append register. Each session that surfaces a new APE lands the entry here
before session close, per the Zilzal-close discipline added at NG-1 F4 closure.

Each entry follows the BAF v4.0 §10 documentation discipline (added at NG-2 D11
closure): origin (cont session or document section), one-sentence empirical
example or reproducer pointer, prevention.

---

## Numbering convention (added at cont61, NG-3 N1 closure)

The register is structured in two ranges:

- **APE-1 through APE-12:** the chain isnad. Numbered per dossier §9 canonical
  record for APE-1 through APE-7. Extended at cont56-cont59 with APE-8 through
  APE-12 documented in cont56-cont59 summaries and the hybrid strategy guide.
- **APE-101 onward:** pre-cont33 infrastructure quirks formerly documented in
  ONNX_GOTCHAS.md. Renumbered into 100-series at cont60 NG-1 F4 closure to
  preserve dossier §9 canonical numbering for the chain isnad.

The cont60 v1 register accidentally conflated these two ranges (treating the
pre-cont33 ONNX_GOTCHAS items as APE-1 and APE-2). NG-3 N1 caught this drift.
v2 restores the canonical structure.

---

## Chain isnad (APE-1 through APE-12)

### APE-1: Pairwise tensor materialization

**Origin:** cont41 dimensionality wall.

**Empirical example:** P-NEW11's per-cell pairwise membership reduction was
specified to handle any (H, W); the implementation produced a [30,30,30,30]
tensor that exceeds the 1.44 MB file limit. Naive pairwise computation between
all-cells-vs-all-cells materializes O(H*W*H*W) tensors that exceed budget.

**Prevention:** Use MatMul reformulation; never instantiate (30, 30, 30, 30)
shaped tensors as graph-resident intermediates. The "junction of two seas"
P-NEW11.5 trick (row-membership x col-membership MatMul) reduces the check to
a single MatMul without intermediate explosion.

### APE-2: Bg detection mismatch

**Origin:** cont44 task313 prefix-sum.

**Empirical example:** Heuristic "background is the most-common color" detection
diverged from Hodel DSL's actual background semantics on task313. Substrate
shipped did not match oracle expectation.

**Prevention:** Always check Hodel DSL exactly for background detection
semantics. Do not infer from frequency or position heuristics. The DSL is the
oracle; substrate must match.

### APE-3: Sequential mutation in ONNX iterative loops

**Origin:** cont48 substrate divergence (P-NEW17 shared-substrate CC).

**Empirical example:** When propagating CC labels iteratively, reading and
writing the same tensor in a loop body produces incorrect labels because the
update is not atomic. In iter k, all direction reads must use the same iter_start
tensor; the accumulator updates separately. A naive in-place mutation produces
a "race condition" where later direction reads see partial updates from the same
iteration.

**Prevention:** Each iteration explicitly preserves iter_start at the top of the
iteration and reads from it for ALL direction operations. The accumulator is a
separate tensor that updates after all reads complete.

### APE-4: Padded-cell color collision

**Origin:** cont48 inflated bg CC (P-NEW17 shared-substrate CC).

**Empirical example:** Cells outside the actual ARC grid are encoded as
all-zero one-hot (no channel set). This is structurally indistinguishable from
"channel 0 absent" without explicit handling, leading to incorrect bbox
computations, spurious "background" detection, and CC propagation across the
padding boundary. Specifically: cont48 build had bg CC inflated by 600+ cells
due to padding-area inclusion.

**Prevention:** Compute `in_grid_mask = ReduceSum(input, axis=channel)` to
distinguish padded cells (mask=0) from in-grid cells (mask=1). Multiply all
position-dependent computations by in_grid_mask before reduction.

### APE-5: Equal on float in opset 10

**Origin:** cont46 task213 first build.

**Empirical example:** Equal in opset 10 requires int64 inputs. Float comparison
silently fails or returns incorrect bool tensors. Specific instance in cont46:
Equal on size_count vs size_target where both were floats produced all-False.

**Prevention:** Cast both operands to int64 before Equal, OR use `(v >= k) AND
(v <= k)` decomposition via Less + Greater + arithmetic. The cont59 task293
build used `Greater(sum, k+0.5)` to avoid the int64 round-trip entirely.

### APE-6: Premature SAVED claim before all five gates

**Origin:** cont42 task284 first build (canonical per dossier §9).

**Empirical example:** task284's first build was reported as "Pass" before
test_network ran cleanly; the actual run showed Right=2 Wrong=2. The save would
have shipped wrong if not caught at diagnostic.

**Prevention:** Five-gate check is non-negotiable before any SAVED claim:
test_network, score_file, file size, furqan-lint, build script + sidecar.
Automated CI gates added at NG-1 F2 closure (test_all_saves_correct.py and
test_all_saves_score.py) enforce mechanically.

### APE-7: Inflated PARTIAL severity

**Origin:** cont47 ceiling.

**Empirical example:** A PARTIAL was classified HIGH when the architectural
ceiling it surfaced was MEDIUM-shape. "Primitive cannot be built in opset 10"
is structural, not release-blocking; classifying it HIGH escalated session
attention to a deferred-anyway item.

**Prevention:** PARTIAL severity follows BAF v3.0 §3 rubric: HIGH only if it
would block release / generate hotfix / be unacceptable to defer one cycle.
Architectural ceilings are MEDIUM by default. Honest PARTIAL with documented
marad beats forced bad build.

### APE-8: Branching primitives blocked in opset 10

**Origin:** cont51 visual-prior triage; documented in NEUROGOLF_HYBRID_STRATEGY_GUIDE.md
Part 6.

**Empirical example:** Several pending tasks require Loop, Scan, or NonZero ops
which are not in opset 10. Attempting to mechanize these via gating + selectors
produces graph blow-up that violates the 1.44 MB cap.

**Prevention:** §11.4 Q3 explicitly checks for banned ops. If the primitive
requires Loop, Scan, Function, NonZero, or Unique, it is structurally
infeasible in opset 10 and must be either decomposed differently or deferred.

### APE-9: Color-blind cc_id collision

**Origin:** cont58 task364 nested-CC detection.

**Empirical example:** Connected component IDs computed as `cc_id = rmin * 32
+ cmin` collide across colors when two different-colored CCs share the same
top-left corner. An L-shape at (0, 0) and a bg CC at (0, 0) produced the same
cc_id.

**Prevention:** Use color-aware cc_id encoding:
`cc_id = color * 1024 + rmin * 32 + cmin`. The color factor (1024) exceeds the
maximum possible (rmin * 32 + cmin) value, ensuring no cross-color collision.

### APE-10: Bbox via outer-product fails on occlusion

**Origin:** cont59 task293 (NG-1 F1 substrate).

**Empirical example:** Computing per-color bbox as `presence_per_row[ch] *
presence_per_col[ch]` (outer product of per-row and per-col masks) gives an
empty intersection when one color partially OCCLUDES another. The 3-color
horizontal bar in task293 train[0] had 88-vertical occluding cols 3-4; the
"any in row" check for color 3 missed those columns.

**Prevention:** Compute bbox via min/max of pixel positions, not via "any in
row/col" outer product. Use masked ReduceMin/ReduceMax with `(1-input)*BIG`
sentinels. See P-NEW21 implementation in cont59_saves/build293.py.

### APE-11: Opset 10 lacks GreaterOrEqual / LessOrEqual / float-Equal

**Origin:** cont59 task293 (NG-1 F1 substrate).

**Empirical example:** Building bbox-mask required `row_idx >= rmin AND row_idx
<= rmax`. Opset 10 has no GreaterOrEqual or LessOrEqual; Equal is int64-only
(see APE-5).

**Prevention:** Use `(x >= k) is NOT (x < k) is 1 - cast(Less(x, k), float)`.
Use `Greater(sum, k+0.5)` instead of `Equal(sum, k+1)` to avoid int64 cast
overhead.

### APE-12: Local-glob substitute for saved_list authority

**Origin:** cont59 task293 (NG-1 F1).

**Empirical example:** cont59 pre-build save check used `glob(cont*_saves/task*.onnx)`,
returning 22 saves; missed the 312 pre-cont33 inheritance saves in cumulative
solutions/, including task293 already shipped at score 12.19. The cont59
rebuild scored 10.89, 1.30 points worse, and was claimed as "+1 delta".

**Prevention:** Every session opens by reading saved_list.txt; pre-flight Q0
fails if the target task is in saved_list and `expected_new < current +
REBUILD_THRESHOLD` (default 0.5 score points, v0 placeholder pending empirical
calibration in cont61+ post-ship audit). Q0 is the FIRST question in §11.4
pre-flight; Q1 through Q5 stay structurally feasibility-focused.

---

## Pre-chain ONNX gotchas (APE-101 onward)

These were documented in cont45-era ONNX_GOTCHAS.md as opset 10 quirks
encountered before the cont33+ isnad began. Renumbered into 100-series at
cont60 NG-1 F4 closure to preserve dossier §9 canonical numbering for the
chain isnad. v1 of the cont60 register accidentally placed these as APE-1
and APE-2; v2 restores correct placement.

### APE-101: Equal on float in opset 10 (pre-chain)

**Origin:** pre-cont33 chain experience, documented in cont45 ONNX_GOTCHAS.md.

**Empirical example:** Same shape as APE-5 but discovered earlier in the
chain. ONNX opset 10 Equal supports only integer types.

**Prevention:** Same as APE-5. Use `M = 1 - Clip(Abs(v - k), 0, 1)` for
integer-valued floats (P-110), or cast to int64 before Equal.

### APE-102: ArgMin/ArgMax not profiler-registered (pre-chain)

**Origin:** pre-cont33 chain experience, documented in cont45 ONNX_GOTCHAS.md.

**Empirical example:** 20 saves in cumulative solutions/ use ArgMin/ArgMax;
score_file returns None locally for all of them (NG-1 F2). Kaggle's profiler
accepts; local profiler does not.

**Prevention:** Use the argmax-without-ArgMax pattern in PRIMITIVES.md (P-140,
P-141). For saves that already use ArgMin/ArgMax, document under MARAD-10
(added at NG-1 F2 closure) and treat the local score_file failure as a known
false negative.

---

## How to add a new APE

When a session surfaces a new failure pattern that future sessions could
repeat:

1. Number it APE-N (continue from APE-12 for new chain isnad APEs;
   APE-103 onward for new infrastructure quirks).
2. Add a section here with origin, empirical example, prevention.
3. Land the entry BEFORE session close, not just in cont summary.

Per the cont60 NG-1 F4 closure: APEs must land here before session close.
The auto-loaded manual must track the chain, not lag it.

This register replaces the cont45-era ONNX_GOTCHAS.md (retired at NG-1 F4
closure). Pre-cont33 gotchas migrate to APE-101, APE-102 (above) with
cross-reference to the original ONNX_GOTCHAS.md preserved in handoff archives.

---

## NG-3 N1 closure stamp

**Date:** 2026-05-06
**Closing instance:** cont61, cont60-instance Claude under BAF v3.0 §1.2 relaxed
reading (session-boundary proxy fresh instance).
**Structural compromise disclosed:** NG-3 was producer-side substrate hygiene
performed against the cont60 APE_REGISTER.md I authored. Cross-checked against
dossier §9 canonical record (read directly, quoted in this v2). Subsequent
fresh-instance NG-3 verification can read this v2 file against the same dossier
§9 to confirm the closure is correctly applied or to escalate residual drift.
**N1 disposition:** APE-6 origin restored to "cont42 task284 first build" per
dossier §9. APE-1 and APE-2 restored to dossier canonical (pairwise tensor /
bg detection mismatch). Pre-chain ONNX gotchas migrated to APE-101 and APE-102
with renumbering disclosure in the header.

---

# Bismillah ir-Rahman ir-Rahim
