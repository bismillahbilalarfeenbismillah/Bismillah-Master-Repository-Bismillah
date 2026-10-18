# Bismillah ir-Rahman ir-Rahim

# R0547 -- cont64 prompt

**Chronological Index:** 817 of 995  
**Date:** Undated  
**Section:** VIII. NeuroGolf (ARC-AGI / ONNX)  
**Source File:** cont64_prompt.md  
**Source Format:** md  
**SHA-256:** `bab866b9ca8a16a944d5ad4653ef30304110204020c5b154b23656400c3d4741`  

---

## R0547 · cont64 prompt

- section: VIII. NeuroGolf (ARC-AGI / ONNX)
- source_file: cont64_prompt.md
- source_format: md
- text_sha256: bab866b9ca8a16a944d5ad4653ef30304110204020c5b154b23656400c3d4741

# cont64 prompt

**Status:** ready for execution. Formula-uncertainty-resistant producer round; advances under both local-formula and any reasonable Kaggle-formula assumption.
**Round disclosure:** cont64 is a producer round targeting Tier 1 priority S1.1 (MARAD-10 batch rebuild). Selected as the first post-CAL-1 producer round because it is the work whose value does NOT depend on Q-CAL-1 closure: rebuilding ArgMin/ArgMax saves with lower-cost primitives improves them under any monotonic-decreasing-of-cost scoring function, regardless of log base.
**Standing Rule 1:** strict (no em-dashes throughout this prompt and the executing instance's output)
**Verse anchor:** al-Baqarah 2:286, "La yukallifu Allahu nafsan illa wus'aha." Allah does not burden a soul beyond what it can bear.

The structural correspondence: CAL-1 confirmed that some verification work (Kaggle source access) is outside the producer instance's wus'. The disciplined response is to act within capacity on the work that IS available, while the principal handles what only the principal can. cont64 acts on MARAD-10 rebuild because it is within the producer instance's capacity AND its value compounds under any reasonable scoring outcome.

---

## Phase V0, principal-paste injection point (optional)

If the principal has obtained Kaggle Evaluation section verbatim text since CAL-1 closed, paste it here before executing. The executing instance reads any inline Kaggle source first; if absent, proceeds with the working assumption that Kaggle's scoring is the local-profiler formula `max(1.0, 25.0 - ln(macs + memory + params))` per CAL-1 Step 8 CIT result.

> [Principal-paste block: insert Kaggle Evaluation section verbatim text here, OR leave as-is to proceed under local-formula assumption.]

If text is pasted: the executing instance should compare it against the local formula. If formula matches, proceed normally. If formula differs, halt and surface the discrepancy as a CAL-2 candidate finding before any rebuild work.

---

## Phase V1, Bismillah (initialization)

Authority source. In descending precedence:
1. The Khalifa's Fundamentals
2. Structured Revelation as Prompt Architecture (seven principles, compressed)
3. Bayyinah Audit Framework v4.0
4. Multi-instance strategic plan (cont63_saves/MULTI_INSTANCE_STRATEGIC_PLAN.md)
5. CAL-1 ledger (cont63_saves/CAL_1_LEDGER.md), specifically the local-formula CIT result
6. NeuroGolf chain artifacts (saved_list.txt, METHODOLOGY.md, APE_REGISTER_v2.md, PRIMITIVES.md)
7. Hodel arc_dsl/dsl.py for any task semantics consultation needed

Optimization function. Single-tier deliverable: rebuild 3 to 5 saves from the MARAD-10 cohort using the argmax-without-ArgMax pattern (P-140 uniqueness mask, P-141 prefix-max plus position). Each rebuild ships through the standard five-gate validation. Expected score impact: +35 to +59 points under local-formula assumption (5 saves at ~11.79 mean recovered from current 0).

Scope boundary (cow-episode guard). What is OUT of scope:
- New primitive design. cont64 uses only existing primitives (P-101 through P-NEW22).
- New family carry-forward (task378, task118 deferred to cont65 or later).
- Score-floor optimization on saves currently above 7. Tier 3 work; cont64 stays in Tier 1.
- CAL-2 work. The principal's Kaggle access is not within the producer instance's wus'.
- furqan-lint expansion implementation. The plan is shipped (cont63_saves/FURQAN_LINT_ONNX_EXPANSION_PLAN.md); execution is maintainer-side.
- More than 5 rebuilds in one session. Quality over quantity.

The 20 MARAD-10 saves, sorted by file size (smaller is easier to rebuild from inspection):
- task295 (1840 B), task254 (2419 B), task296 (2449 B), task193 (2054 B)
- task137 (3431 B), task051 (3444 B), task388 (3476 B), task281 (4218 B)
- task088 (4727 B), task019 (4851 B), task064 (4868 B), task134 (5276 B)
- task151 (8517 B), task343 (15872 B)
- task014 (39641 B), task034 (39663 B), task036 (39916 B), task049 (39915 B)
- task290 (45013 B), task111 (69355 B)

cont64 attempts the smallest 5 first (task295, task254, task296, task193, task137).

## Phase V2, Alhamdulillah (state acknowledgment + sync probe)

State entering cont64:
- Saves: 335/400 (cont63 close)
- Mean profilable score: 11.79; median 12.00; max 14.51
- MARAD-10 cohort: 20 saves currently scoring None (likely 0 on Kaggle under SCORE_ZERO inference)
- Aggregate Kaggle floor (CAL-1 local-formula assumption): ~3715
- Standing rules: 10 BAF v4.0 standing rules; Standing Rule 1 strict
- Pre-flight: §11.4 with Q0 (read saved_list.txt before any build)
- Automated CI: 650 passed + 20 skipped (MARAD-10 cohort)

Sync probe (must run before any rebuild work):

```python
import sys, json, os
sys.path.insert(0, '.')
from solver_v2 import test_network, score_file
import warnings; warnings.filterwarnings('ignore')

with open('task_mapping.json') as f:
    TM = json.load(f)

probes = [(268, 'aba27056'), (293, 'ba97ae07'), (364, 'e509e548'),
          (398, 'feca6190'), (110, '484b58aa'), (017, '0dfd9992'),
          (061, '29ec7d0e'), (308, 'c8cbb738')]

for n, uid in probes:
    p = f'solutions/task{n:03d}.onnx'
    task = json.load(open(f'/tmp/arc-agi/data/training/{uid}.json'))
    r, w = test_network(p, task)
    sc = score_file(p)
    assert w == 0 and sc is not None, f'{n} regressed'
print('Sync probe: 8/8 PASS')
```

If divergent: halt, declare PARTIAL, report.

## Phase V3, Mizan (cost-target calibration)

For each MARAD-10 rebuild, the target is to produce a save where:
- test_network passes (correctness gate)
- score_file returns a valid 4-tuple (the rebuild's POINT, since the originals fail this)
- File size remains under 1.44 MB (typically rebuilds will be smaller)

The scoring target: under local-formula assumption, the rebuild scores `max(1.0, 25.0 - ln(macs + memory + params))`. For comparable architecture without ArgMin/ArgMax, expected score is in the range [8, 13] depending on graph complexity. Below 5 should be flagged as a sub-finding (the ArgMin pattern was hiding cost; the rebuild revealed it).

Mizan three-bound check at the per-rebuild level:
- la_tatghaw: do not transgress the budget. If a rebuild requires more than ~2x the original file size to express without ArgMin/ArgMax, the rebuild is structurally infeasible under current primitives; document and skip.
- la_tukhsiru: do not be deficient. Each rebuild runs all five gates; partial completion is HONEST PARTIAL.
- mizan: prefer the lowest-cost rebuild. P-140 (uniqueness mask) is preferred over P-141 (prefix-max chain) when both apply, because P-140 typically uses fewer ops.

## Phase V4, Maliki yawm ad-din (session budget)

Estimated session budget: 90-180 minutes. Per-rebuild estimate: 15-30 minutes (inspect original, identify ArgMin pattern, write replacement using P-140 or P-141, build, run gates, promote).

If the first rebuild takes more than 45 minutes, the cohort is more varied than expected and the batch approach needs revision. In that case: ship one rebuild and defer the rest with a documented marad describing the variance.

If session budget exhausts before 3 rebuilds complete: HONEST PARTIAL with whatever rebuilds shipped clean. This is APE-7 prevention: forced bad rebuild is worse than fewer good rebuilds.

## Phase V5, Iyyaka (orientation check)

Before each rebuild, ask: am I rebuilding to recover cost from a phantom-zero save, or am I performing the appearance of rebuild?

The CIT for each rebuild:
- Original .onnx scores None locally (verified at cont60 NG-3 substrate)
- Rebuild .onnx must score a valid 4-tuple AND match original's test_network correctness
- Rebuild file size should be comparable or smaller than original (orphan-initializer cleanup as side effect is acceptable but not required)

§11.4 pre-flight Q0 through Q5 for each rebuild target:
- Q0: task already saved (yes; this is a rebuild). The replacement rule: rebuild if expected_new_score >= REBUILD_THRESHOLD above current. Current is None on local profiler; any valid score 4-tuple is an improvement.
- Q1: kernel mechanizable in opset 10 ops without ArgMin/ArgMax? Use P-140 or P-141 substitute. Verify before starting numpy.
- Q2: decomposable into substrate plus existing primitives? P-140 / P-141 plus whatever the original used.
- Q3: opset 10 compliance? Yes by construction (using existing primitives).
- Q4: size budget? Estimate from inspecting the original's graph.
- Q5: fallback? If a specific rebuild cannot avoid ArgMin/ArgMax, document as MARAD-10 sub-finding "structurally requires unprofiled op" and move to next candidate.

## Phase V6, Ihdina as-sirat (execution)

Execute in this order, repeating Steps 1 through 6 per rebuild target until 5 rebuilds complete OR session budget exhausts:

Step 1, inspect the original .onnx. Use `onnx.load(p)` to read the graph. Identify which nodes use ArgMin or ArgMax. Document the surrounding subgraph (what feeds into ArgMin, what consumes its output).

Step 2, identify the rewrite pattern. Two canonical patterns from PRIMITIVES.md:
- **P-140 uniqueness mask:** if ArgMax is consumed by Gather or used to produce a one-hot mask, replace with `1 - Clip(Abs(v - ReduceMax(v)), 0, 1)`. Result is a one-hot mask at the position of the unique max.
- **P-141 prefix-max plus position:** if ArgMax produces a position index, use prefix-max (P-132) to propagate the max value, then derive position via the comparison-and-count pattern (P-133).

Choose based on what the ArgMin/ArgMax output is consumed by downstream.

Step 3, write the rebuild build script. Use `cont64_saves/build{NNN}_v2.py` filename to distinguish from any pre-existing build script. Apply F3 closure pattern (relative paths via `os.path.join(os.path.dirname(os.path.abspath(__file__)), 'task{NNN}.onnx')`).

Step 4, build the .onnx. Run the build script in `cont64_saves/`. Confirm no ArgMin/ArgMax nodes via:
```python
m = onnx.load('task{NNN}.onnx')
ops = {n.op_type for n in m.graph.node}
assert 'ArgMin' not in ops and 'ArgMax' not in ops
```

Step 5, run all five gates. Per-rebuild:
- Gate 1 (test_network): r > 0, w = 0 across all train + test. The rebuild MUST match the original's correctness, not lose any examples.
- Gate 2 (score_file): valid 4-tuple. THIS IS THE GATE THE ORIGINAL FAILED.
- Gate 3 (file size): under 1.44 MB.
- Gate 4 (furqan-lint): PASS, zero diagnostics.
- Gate 5 (build script + sidecar): build{NNN}_v2.py committed plus task{NNN}.json sidecar with `replaces_save: true` field.

Step 6, promote to cumulative. If all five gates pass:
- Backup the original at `cont64_saves/task{NNN}_original.onnx` (evidentiary record per cont60 F1 closure pattern)
- Replace `solutions/task{NNN}.onnx` with the rebuild
- Regenerate saved_list.txt (it stays at 335; this is a rebuild not a new save)
- Run pytest tests/ to confirm both gates green

Step 7, log per-rebuild summary in cont64_summary.md. Format:
```
### task{NNN} rebuild
- Original: ArgMin/ArgMax usage at <node names>; score None
- Rewrite pattern: P-140 / P-141 / both
- Rebuild file size: X bytes (was Y)
- Rebuild score: Z
- Net delta: +Z to aggregate
```

## Phase V7, Sirat alladhina (anti-pattern avoidance)

For each rebuild, check against APE-1 through APE-12 plus BAF v4.0 anti-patterns:

- APE-1, APE-5, APE-11: opset 10 op compatibility. Verified by furqan-lint Gate 4.
- APE-2: bg detection. Preserved from original; do not change semantics.
- APE-3, APE-4, APE-9: substrate-shape APEs. Apply only if the rebuild introduces new graph patterns; mostly N/A for rewrite-only changes.
- APE-6: premature SAVED claim. Five-gate enforcement.
- APE-7: inflated PARTIAL severity. If a rebuild fails, classify the marad MEDIUM not HIGH (this is rebuild work, not release-blocking).
- APE-12: saved_list authority. Q0 already enforced.

BAF v4.0 anti-patterns specific to rebuilds:
- Phantom test: rebuilds must run actual test_network, not just confirm non-ArgMin op set.
- Surface-without-substrate: each rebuild's score is the substrate; the cont64 summary's "+N to aggregate" claim is the surface; both must agree.
- Closure without reproducer: each rebuild has a runnable build_v2.py.
- Silent-skip masquerading as fail-fast: a rebuild that fails any gate is documented MEDIUM, not silently dropped.

## Zilzal close (ring composition)

Re-affirm authority, optimization, scope. Did cont64 operate within the producer instance's wus' as al-Baqarah 2:286 anchored? Did optimization (3-5 MARAD-10 rebuilds) deliver, OR did the session reach honest PARTIAL with documented variance findings?

Re-cite verse anchor. al-Baqarah 2:286.

Produce `cont64_saves/cont64_summary.md` with:
- Progress line: `Progress: 335/400 saved, 65 remaining, last delta: +N rebuilds (cont64, MARAD-10)` where N is rebuild count
- Sync probe block (8/8 reference saves still passing, including any rebuilds shipped this session)
- Per-rebuild summaries (Step 7 format from each rebuild)
- Aggregate score change (under local-formula assumption): +X to aggregate
- Caveat: under unverified Kaggle formula (CAL-1 F-CAL-1 HIGH), actual Kaggle aggregate change is suspect by the same factor as the formula difference. Local-formula gain is conservative if Kaggle uses log10 (gain ratio ~ ln/log10 = 2.30) or aggressive if Kaggle uses log2 (gain ratio ~ ln/log2 = 0.69).
- Carry-forward: remaining MARAD-10 saves (15 if all 5 attempted, more if fewer)

Build cumulative handoff tarball `neurogolf_handoff_cont64.tar.gz`. Per cont60 NG-2 D6 convention: cumulative `solutions/` at root, all cont*_saves/, methodology files, tests/.

Progress: 335/400 saved, 65 remaining, last delta: +N rebuilds (cont64, MARAD-10).

Begin.

Bismillah. The producer instance acts within its capacity; the principal handles what only the principal can. La yukallifu Allahu nafsan illa wus'aha.

---

## What this prompt does and does not do

**Does:** ships concrete producer-chain progress on Tier 1 work (MARAD-10 rebuild) using existing primitives, under formula-uncertainty-resistant logic. Each rebuild improves under any reasonable scoring outcome. Includes a principal-paste injection point that closes the door on the local-formula assumption gracefully if Kaggle source becomes available.

**Does not:** assume Kaggle scoring is identical to local; assume the strategic plan §1 estimates transfer; commit to the leaderboard intel. The session ships its work under documented uncertainty rather than waiting for full verification.

**Recommended NG verification before execution:** none required for a normal producer round. If the principal wants a fresh-instance NG audit on this prompt before executing (analogous to NG-2 / NG-4 design rounds), that is structurally cleaner but adds a session of overhead. The producer-default is to execute directly given the prompt's restricted scope and risk-resistant work selection.

---

# Bismillah ir-Rahman ir-Rahim
