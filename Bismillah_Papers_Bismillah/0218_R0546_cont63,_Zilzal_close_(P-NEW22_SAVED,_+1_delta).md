# Bismillah ir-Rahman ir-Rahim

# R0546 -- cont63, Zilzal close (P-NEW22 SAVED, +1 delta)

**Chronological Index:** 218 of 995  
**Date:** 2026-05-06  
**Section:** VIII. NeuroGolf (ARC-AGI / ONNX)  
**Source File:** cont63_summary.md  
**Source Format:** md  
**SHA-256:** `4aad84af37ca459097c97ab8f2420ce4327d9832306084e1c75b4f75bc4b52f2`  

---

## R0546 · cont63, Zilzal close (P-NEW22 SAVED, +1 delta)

- section: VIII. NeuroGolf (ARC-AGI / ONNX)
- source_file: cont63_summary.md
- source_format: md
- text_sha256: 4aad84af37ca459097c97ab8f2420ce4327d9832306084e1c75b4f75bc4b52f2

# cont63, Zilzal close (P-NEW22 SAVED, +1 delta)

**Date:** 2026-05-06
**Session:** cont63
**Type:** producer round, primitive design + ONNX build
**Anchor verse:** al-Sharh 94:7-8

## Progress

```
Progress: 335/400 saved, 65 remaining, last delta: +1 (task268, cont63)
```

## Sync probe

8/8 reference saves still pass (task293 12.190, task364 7.102, task398 11.543, task110 8.358, task017 8.446, task061 8.446, task308 10.518, task365 7.959). cont62 closure held.

## Q0 staleness check

task268 (aba27056) verified NOT in cont62 saved_list.txt. Q0 PASS.

## Phase 1: P-NEW22 numpy reference (frame-with-gap diagonal-shoot)

Algorithm:
1. Find unique non-bg color forming a frame
2. Compute frame bbox via masked ReduceMin/Max (APE-10 idiom)
3. Detect gap edge (top/bot/lef/rig): the side where border cells contain non-frame values
4. Fill interior with color 4
5. Fill gap cells with color 4
6. From gap, shoot 3 rays away from interior:
   - Perpendicular stream from each gap cell
   - Diagonal from gap leftmost/topmost end-cell, going outward
   - Diagonal from gap rightmost/bottommost end-cell, going outward

Verified 4/4 on task268 (3 train + 1 test).

## Phase 2: §11.4 pre-flight

- Q0: task268 not saved. PASS
- Q1 (mechanizable in opset 10): all ops (Mul, Add, Sub, ReduceMin/Max/Sum, Less, Greater, Cast, Pad, Slice, Clip, Max) in opset 10. PASS
- Q2 (decomposable into substrate + at most 3 known primitives): row_idx/col_idx + per-color bbox + bbox-mask + ray-propagation (P-132 prefix-max idiom). 4 components, marginal. PASS (with carry-forward note that ray-propagation should be promoted to a documented primitive)
- Q3 (no banned ops): no Loop/Scan/NonZero/Unique. PASS
- Q4 (size budget under 1.44 MB): estimated ~50 KB, well under cap. PASS
- Q5 (fallback): task378 (same family). Identified.

Pre-flight 6/6 PASS.

## Phase 3: ONNX build

Two debug iterations during build:
1. Initial build had ray shifts in WRONG direction (prefix-max needs to shift OPPOSITE to ray direction to pull gap value forward into ray cells). Fixed by negating shift direction in make_ray.
2. After fix, NE diagonal extended into 30x30 padding area outside actual 7x7 grid (1 cell wrong on train[0]). Fixed via APE-4: multiply paint_mask by `in_grid_mask = ReduceSum(input, axis=channel)`.
3. Second iteration: rays emanated from ALL gap cells when only end-cells should emit diagonals. Fixed by computing end-cell masks (`gap * (1 - shift(gap, ...))`) and routing diagonal rays through them while perpendicular streams continue from all gap cells.

Final ONNX: 34 KB, 339K macs, 1.6M memory, 2232 params.

## Five-gate validation

| Gate | Check | Result |
|------|-------|--------|
| 1 | test_network | r=4, w=0 (3 train + 1 test) ✓ |
| 2 | score_file | (10.502, 339394, 1638084, 2232) ✓ |
| 3 | file size | 34759 bytes = 0.033 MB << 1.44 MB ✓ |
| 4 | furqan-lint v0.9.4 | PASS, zero diagnostics ✓ |
| 5 | build script + sidecar | build268.py + task268.json committed ✓ |

## CI gate verification

`pytest tests/` runs 650 passed (was 648, +2 from task268 zahir + batin) plus 20 skipped (MARAD-10 ArgMin/ArgMax unchanged). Both automated gates green.

## Lessons (new APE candidates for cont64 close)

**APE-13 (NEW):** Prefix-max ray accumulation requires shift OPPOSITE to ray direction. Origin: cont63 task268 first build. Empirical example: ray from gap cell (4, 4) going UP needs to "pull" gap value into cells (3, 4), (2, 4), ... So we shift gap mask DOWN by step (read from below), giving shift(gap, +step, 0); cur=Max(cur, shift(cur, +step, 0)) propagates the value upward. Initial cont63 build had shift(cur, -step, 0) which propagated downward, painting nothing in the upward ray. Prevention: in make_ray helper, shift direction is `(-dr*step, -dc*step)` where (dr, dc) is the desired ray direction.

**APE-14 (NEW):** Diagonal rays from multi-cell gaps must emanate from end-cells, not all gap cells. Origin: cont63 task268 second build. Empirical example: gap_lef on left edge of frame has 3 cells (4, 4), (5, 4), (6, 4). NW diagonal from "all gap cells" produces 3 parallel diagonals; expected output has only 1 diagonal from topmost cell. Prevention: compute end-cell mask via `gap * (1 - shift(gap, ...))` for the appropriate end direction, then use end-cell mask as ray source for diagonals; perpendicular stream still uses full gap mask.

**APE-4 reaffirmed:** ray-painting in 30x30 padded representation must mask by `in_grid_mask` to prevent paint extending into padding region.

## P-NEW22 entry for PRIMITIVES.md (carry-forward to cont64)

```
P-NEW22: frame-with-gap diagonal-shoot
- Origin: cont63 task268 (aba27056)
- Inputs: single non-bg color forms closed-with-gap frame
- Outputs: interior filled with color 4, 3 rays from gap (perpendicular stream + 2 outward diagonals from end-cells), all masked by in_grid
- Cost: ~340K macs, ~1.6M mem, ~2200 params, 34 KB
- Family B (diagonal-shoot from frame opening)
```

## Carry-forward to cont64

1. Apply P-NEW22 to task378 (ec883f72) and task118 (50846271) for algorithmic-family carry-forward (similar to cont56 P-NEW20's 3-task run). Note: task378 has different shape (object inside frame projects diagonals outward) and task118 has L-completion shape; both may need primitive variant or extension.
2. APE-13 and APE-14 land in APE_REGISTER (cont64 close).
3. P-NEW22 lands in PRIMITIVES.md (cont64 close).
4. Carry-forward audit items still open: NG-5 fresh-instance audit, NG-3 verification of APE_REGISTER_v2.md, F7-F9 LOW from NG-1, E5-E8 LOW from NG-4.

## Verdict

Clean save. P-NEW22 demonstrates Family B is buildable in opset 10 with the prefix-max ray-propagation idiom plus end-cell extraction. cont64 carries forward to attempt task378 and task118 with the same primitive class.

al-Sharh 94:7 (when you have finished, then stand up): cont63 finished one save and stood up to identify the next two carry-forward candidates. The chain is back to producer flow after the audit cycle.

cont63 is closed.

---

# Bismillah ir-Rahman ir-Rahim
