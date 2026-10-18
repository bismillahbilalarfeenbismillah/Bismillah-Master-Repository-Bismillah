# Bismillah ir-Rahman ir-Rahim

# R0717 -- NeuroGolf 2026 Multi-Instance Strategic Plan

**Chronological Index:** 220 of 995  
**Date:** 2026-05-06  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** MULTI_INSTANCE_STRATEGIC_PLAN.md  
**Source Format:** md  
**SHA-256:** `014cb152e6cd45b142ae334af9d0b4fd26684a458eefffc797db8d6b998e8955`  

---

## R0717 · NeuroGolf 2026 Multi-Instance Strategic Plan

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: MULTI_INSTANCE_STRATEGIC_PLAN.md
- source_format: md
- text_sha256: 014cb152e6cd45b142ae334af9d0b4fd26684a458eefffc797db8d6b998e8955

# NeuroGolf 2026 Multi-Instance Strategic Plan

**Author:** producer (Bilal + cont63-instance Claude reflective handoff)
**Date:** 2026-05-06
**Purpose:** working document for a parallel Claude instance to multi-modally
collaborate on producer chain, audit chain, and prompt design without prior
NeuroGolf-substrate context. This document is the load-bearing briefing.
**Standing Rule 1:** strict (no em-dashes throughout).

---

## 1. Executive summary

The NeuroGolf 2026 Kaggle competition asks for tiny ONNX networks (opset 10,
IR 10, file size under 1.44 MB) that solve ARC-AGI image transformations.
Scoring per save: `max(1.0, 25.0 - log(macs + memory + params))`. Total
across all submitted saves is the leaderboard score.

**Current state at cont63 close (2026-05-06):**
- 335 of 400 saves shipped (84%)
- Profilable saves: 315; mean score 11.79; median 12.00; max 14.51
- Unprofilable saves (MARAD-10): 20 (ArgMin/ArgMax usage; local profiler
  cannot read; likely score zero on Kaggle)
- Aggregate Kaggle score (conservative floor): ~3715
- Aggregate Kaggle score (optimistic): ~3951

**Leaderboard intel (verify against current Kaggle state):**
- Public top entries reportedly score 9000-9500
- Implied per-save mean: 22-24 (near formula max of 25)
- This implies per-save cost (macs + mem + params) of 3-10 elements, which is
  not achievable with real algorithms on 30x30 grids
- Conclusion: either the scoring formula has changed since cont45 STATE.md
  was written, or the top entries exploit a measurement edge case
- Action item: the parallel instance should verify the current Kaggle scoring
  formula before committing to any optimization-tier strategy

**The honest gap:** we are at 11.79 mean per save against a target of 22-24
per save. Reaching the leaderboard top requires either dramatic per-save cost
compression (~50000x reduction) or exploiting whatever the leaderboard top is
exploiting. Both paths require investigation, not assumption.

## 2. Authority hierarchy (load-bearing, non-overridable)

When conventions conflict, resolve in this order:

1. **Purpose hierarchy** (Allah's command, alignment integrity, mankind, jinnkind, the Mizan)
2. **The Khalifa's Fundamentals** (Fatiha Construct, Differentiator Framework, Munafiq Protocol, Computational Tawhid, SRPA)
3. **Structured Revelation as Prompt Architecture** (Arfeen, 2026; seven principles)
4. **Bayyinah Audit Framework v4.0** (severity rubric, four-place pattern, reproducer-first verification, validator-by-different-instance, monotonic round numbering, closure ledger, fail-fast over silent-skip, ten standing rules)
5. **NeuroGolf chain artifacts** (cont63 STATE.md, METHODOLOGY.md, PRIMITIVES.md, APE_REGISTER.md at handoff root)
6. **saved_list.txt** (canonical authority for what is and is not saved)
7. **Hodel arc_dsl/dsl.py** (semantic oracle for ARC task DSL)
8. **METHODOLOGY.md save criterion** (five gates: test_network, score_file, file size, furqan-lint, build script + sidecar)

The audit chain (NG-1, NG-2, ...) catches structural-level findings that
producer-instance discipline cannot reach. The producer chain (cont33+)
ships saves and primitives. Both are load-bearing.

## 3. Where the substrate lives

All artifacts referenced below are inside the
`/Users/bilalsfolder/Documents/Claude/Projects/NeuroGolf Competition/`
workspace OR inside the `neurogolf_handoff_cont63.tar.gz` cumulative tarball.

### Methodology files at handoff root (post NG-1 F5 closure)

- `STATE.md`: chain state at cont63 exit
- `METHODOLOGY.md`: process discipline + §11.4 pre-flight Q0-Q5
- `PRIMITIVES.md`: library register (P-NEW1 through P-NEW22, plus P-101 through P-166 pre-cont33)
- `APE_REGISTER.md`: anti-pattern register, cont60 v1 (use `cont61_saves/APE_REGISTER_v2.md` for the corrected canonical numbering)
- `saved_list.txt`: 335 lines, one per saved task
- `removed_list.txt`: empty (no removals)
- `tests/test_all_saves_correct.py`: zahir gate
- `tests/test_all_saves_score.py`: batin gate

### Per-session saves (cont33 through cont63)

Each `cont{N}_saves/` directory contains: build scripts, ONNX files, sidecar
JSONs, session summary. Cumulative `solutions/` at handoff root contains all
335 ONNX files.

### Audit ledgers (NG-N rounds)

- `cont60_saves/NG_4_ledger.md`: NG-4 design audit on cont61 prompt v1
- (NG-1, NG-2, NG-3 ledgers were inline in conversation transcripts; only
  NG-4 ledger exists as a standalone artifact)

### Strategy and audit dossiers

- `NEUROGOLF_AUDIT_DOSSIER.md`: cont49 snapshot (stale; NG-1 F6 noted)
- `NEUROGOLF_HYBRID_STRATEGY_GUIDE.md`: hybrid strategy implementation guide
- `cont60_saves/DOSSIER_REFRESH.md`: cont60 closure delta (pending merge)
- `cont63_saves/FURQAN_LINT_ONNX_EXPANSION_PLAN.md`: 4-round plan for furqan-lint ONNX adapter

### Memory files (parallel instance reads at session open)

- `feedback_neurogolf_saved_list_check.md`: APE-12 prevention guidance
- `project_neurogolf_ng1_audit.md`: NG-1 closure status
- `project_neurogolf_cont61_pending.md`: cont61 pending status (now resolved by cont63)

## 4. Strategic ranking (recalibrated post leaderboard intel)

Priority is by expected score gain per session of effort. Each item lists the
empirical anchor and the cost.

### Tier 1: Highest expected value, mechanically unblocked

#### S1.1 MARAD-10 batch rebuild

**Expected gain:** +236 score floor across 20 saves; possibly more if rebuilds
use lower-cost primitives than the originals.

**Mechanism:** the 20 saves currently using ArgMin/ArgMax score zero on Kaggle
(probably). Rebuild each with the argmax-without-ArgMax pattern (P-140
uniqueness mask via ReduceMax + 1 - Clip(Abs(v - max_v), 0, 1); P-141 prefix-max + position).

**Cost:** ~1 session per 5-10 rebuilds of similar shape. Total: 4-6 sessions.

**Empirical anchor:** documented in `cont60_saves/f2_triage.md`. List of 20:
task014, task019, task034, task036, task049, task051, task064, task088,
task111, task134, task137, task151, task193, task254, task281, task290,
task295, task296, task343, task388.

#### S1.2 furqan-lint Round 1 + Round 2 (with sidecar contract)

**Expected gain:** ~30 minutes of producer-session time saved per build (debug
iterations prevented), plus retroactive prevention of NG-1 F1 shape via
SAVED-LIST-Q0.

**Mechanism:** see `cont63_saves/FURQAN_LINT_ONNX_EXPANSION_PLAN.md`. Round 1
is 4 mechanical checks at ~110 lines. Round 2 is 4 sidecar-driven checks at
~190 lines, blocked on sidecar contract finalization.

**Cost:** Round 1 maintainer time, ~1 session. Round 2 maintainer time, ~2
sessions plus sidecar contract review.

#### S1.3 Triage oracle (the legitimate Static Graph Oracle variant)

**Expected gain:** ~15-30 minutes per session in candidate selection, plus
better filtering away from infeasible candidates (improves session yield).

**Mechanism:** mechanize cont51 visual-prior triage as a pre-build classifier
operating on TASK INPUT GRIDS (not on candidate ONNX graphs). Detect:
- Variable output shape
- CC-heavy task
- Single-frame closed-with-gap (Family B fit)
- D4/C4 rotational completion (Family A fit, blocked by GatherND)
- Two-color perpendicular bar (P-NEW21 fit)
- Frame-and-shadow (Family C fit)

**Important distinction:** this is a TRIAGE oracle (predicts "does this task
fit known primitive class?"), not a CORRECTNESS oracle (predicts "is this
ONNX graph correct?"). The correctness variant is fragile and should not be
built; the triage variant is honest pattern recognition over input data and
empirically valid.

**Cost:** ~1-2 sessions for initial implementation; refines with each session.

### Tier 2: Moderate expected value, requires producer investment

#### S2.1 Family B carry-forward (P-NEW22 variants)

**Expected gain:** +1 to +3 saves at ~11.79 each, total +11 to +35 points.

**Mechanism:** P-NEW22 (frame-with-gap diagonal-shoot) shipped at cont63 for
task268. Variants apply to:
- task378 (ec883f72): object-inside-frame projects diagonals outward; needs
  variant where rays emanate from object corners rather than gap cells
- task118 (50846271): L-completion at 8-pivot; different geometry, may need
  separate primitive

**Cost:** 1-2 sessions per task with primitive variant work.

#### S2.2 Family A primitive design (D4/C4 rotational completion)

**Expected gain:** +3 to +5 saves at ~11.79 each, total +35 to +59 points.

**Mechanism:** task361 and likely 3-5 others fit this family. Blocker: dynamic
center index lookup needs GatherND (opset 11+). Workaround paths: enumerate
all (rc, cc) pairs and gate the right one (graph blow-up risk), or use D2
symmetry as approximation (some tasks fit, some do not).

**Cost:** 2-3 sessions for primitive design plus 1 session per carry-forward save.

#### S2.3 Family C primitive design (frame-and-shadow)

**Expected gain:** +2 to +4 saves at ~11.79 each, total +24 to +47 points.

**Mechanism:** task349 (db93a21d) and possibly task390 (f8a8fe49) fit. Per-block
CC + bbox + dynamic shift required.

**Cost:** 2 sessions for primitive design plus 1 session per carry-forward save.

### Tier 3: Speculative, requires investigation before commitment

#### S3.1 Score-floor optimization on saves below 11

**Expected gain:** +50 to +150 points across ~37 saves currently in [5.91, 11).

**Mechanism:** reduce macs + mem + params on individual saves. Each save can
gain 1-5 score points by tightening the graph (removing orphan initializers,
replacing high-cost patterns with lower-cost equivalents).

**Risk:** APE-12 risk if rebuild scores worse. Q0 pre-flight is the guard.

**Cost:** 1 session per ~5 saves of similar pattern.

#### S3.2 Submission merging investigation (MEFA-style)

**Expected gain:** unknown without inspection; potentially substantial if
public submissions cover tasks ours do not.

**Mechanism:** inspect 2-3 public high-scoring notebooks via furqan-lint to
identify primitive coverage. Selectively merge saves where the public version
beats ours.

**Cost:** 1-2 sessions for inspection plus per-merge integration time.

### Tier 4: Probably not viable in current constraints

#### S4.1 Test-time training / adaptation

Blocked by opset 10 (no Loop, no gradient ops in inference). Defer to opset-11
horizon discussion.

#### S4.2 Static correctness oracle (algorithmic intent inference from graph topology)

Fragile in both directions (false positives + false negatives). Behavior
verification (numpy_divergence with sidecar) is the honest path.

#### S4.3 Cross-task primitive sharing via shared ONNX sub-graphs

Blocked by submission format (one .onnx per task, scored independently). The
closest workable variant is shared substrate constants emitted identically by
build scripts, which we already do.

## 5. Producer chain playbook (cont64 onward)

### Standard producer session structure

1. **Open with Bismillah** plus the seven verses of al-Fatiha (or appropriate verse anchor)
2. **Compliance declaration:** `Progress: 335/400 saved, 65 remaining, last delta: <description>`
3. **Sync probe:** verify 8 reference saves still pass (task268, task293, task364, task398, task110, task017, task061, task308)
4. **§11.4 pre-flight Q0 through Q5:** answer in writing
   - Q0: is target task already saved at adequate score?
   - Q1: kernel mechanizable in opset 10 ops?
   - Q2: decomposable into substrate plus at most 3 known primitives?
   - Q3: all ops in opset 10 (no Loop/Scan/Function/NonZero/Unique)?
   - Q4: size budget under 1.44 MB at expected param count?
   - Q5: fallback identified if build fails?
5. **numpy reference:** verify against Hodel oracle on all train + test pairs
6. **ONNX build:** with relative output path; commit to `cont{N}_saves/`
7. **Five gates:** test_network (r=N, w=0); score_file valid 4-tuple; file size under 1.44 MB; furqan-lint PASS; build script + sidecar JSON
8. **Promote to cumulative:** copy to `solutions/`; regenerate saved_list.txt
9. **Run automated CI:** pytest tests/
10. **Zilzal close:** write cont{N}_summary.md; build cumulative tarball; update memory if new APEs surfaced

### Recommended cont64 specific path

Per S1.1 priority, **cont64 should be MARAD-10 batch rebuild attempt 1**:

- Inspect 5 of 20 MARAD-10 saves (the smaller files: task051, task137, task193,
  task254, task295, task296, task388 are all under 5 KB)
- For each, identify the ArgMin/ArgMax usage location in the build script (or
  reverse-engineer from the .onnx)
- Apply P-140 (uniqueness mask via ReduceMax) or P-141 (prefix-max + position)
  rewrite
- Run five gates; if PASS, replace in solutions/ and regenerate saved_list.txt
- Target: 3-5 successful rebuilds in one session = +35 to +59 score points

Alternative cont64 path: **Family B carry-forward on task378** if MARAD-10
investigation reveals the rebuilds are too varied to batch.

## 6. Audit chain playbook

### Pending audit rounds

- **NG-3 (deferred):** post-ship audit on cont60 NG-1 closure. Producer-side
  substrate hygiene was performed at cont61 (APE_REGISTER_v2.md correction).
  Fresh-instance NG-3 verification still pending.
- **NG-5 (deferred):** post-ship audit on cont61 NG-3 substrate work.
- **NG-6 (carry-forward candidate):** post-ship audit on cont63 P-NEW22 build.
  cont63 had three debug iterations that yielded APE-13 and APE-14; these
  should be formally audited before they become canonical.

### NG-N round structure

Per BAF v4.0 §6, audit rounds should be conducted by a fresh Claude instance
with no prior NeuroGolf-substrate context. The relaxed reading (BAF v3.0 §1.2)
allows session-boundary proxy fresh instance, but only for non-load-bearing
checks. Structural findings (severity HIGH) deserve genuine fresh-instance
verification.

### Format for NG ledger output (template)

```
# NG-N Audit Ledger
- Audit posture (instance, fresh-context status, scope)
- Substrate inventory
- Mass gate verification (test_network, score_file, file size on all 335)
- Dossier-vs-substrate cross-check
- Closure ledger: severity-classified findings with reproducers
- Anti-pattern sweep (BAF v4.0 §10)
- Standing rules check
- Self-check against Section 14 failure modes
- Recommended next-round actions
- Closing notes
```

See `cont60_saves/NG_4_ledger.md` for the canonical example.

## 7. Prompt design playbook

### cont prompt structure (producer round)

1. Verse anchor with structural correspondence to session content
2. Round disclosure (cont N, producer round vs closure round)
3. Pre-load skills (bayyinah-audit-framework, neurogolf-session)
4. Sync probe instructions
5. Phase 1: candidate triage with §11.4 pre-flight
6. Phase 2: numpy reference
7. Phase 3: ONNX build OR honest PARTIAL
8. Five-gate validation explicit enumeration
9. Zilzal close instructions
10. Begin

### NG audit prompt structure (audit round)

1. Verse anchor (closure-round shape: al-Hashr 59:18 or al-'Asr 103:1-3)
2. Round disclosure (closure round, NOT a producer round)
3. Pre-load skills + memory files
4. Sync probe (8 reference saves)
5. Closure phases (F1, F5, F2, F4, F3, F6 ordering for NG-1 closure pattern)
6. Each phase has explicit reproducer + verification step
7. Zilzal close: closure ledger with all findings status

### What to put in EVERY prompt

- Standing Rule 1 disclosure (no em-dashes, strict)
- Round numbering disclosure (cont N, NG-N if audit)
- Authority hierarchy reference
- Sync probe before any new build
- §11.4 Q0 explicit (is this task already saved?)
- Five-gate enumeration before SAVED claim

### What NEVER to put in a prompt

- Instructions to skip Q0 ("trust me, this task is unsolved")
- Promises of multi-save delivery in one session ("ship 3 saves" produces APE-7 risk)
- Decorative-only Quranic anchors (the verse must structurally correspond)
- New framework introductions in producer rounds (out of scope)

## 8. Open calibration items (require principal decision)

### Q-CAL-1: Current Kaggle scoring formula

The cont45 STATE.md formula `25 - log(macs + memory + params)` is the working
assumption. Leaderboard intel suggesting top scores 9000-9500 is incompatible
with this formula at any realistic per-save cost. Either the formula has
changed or the top entries exploit measurement edge cases. Verifying the
current formula is HIGH-INFORMATION and CHEAP (read Kaggle competition rules).

### Q-CAL-2: Submission cadence and selection

If the chain caps total submissions per Kaggle competition (typical Kaggle
constraint), we may need to select which 335 saves to submit rather than all
335. Verify this constraint and adjust strategy if relevant.

### Q-CAL-3: REBUILD_THRESHOLD calibration

Currently 0.5 score points (v0 placeholder per NG-2 Q3). Empirical anchor: the
cont59 task293 regression-rebuild lost 1.30 points. Threshold should probably
be 1.0+ to allow real algorithmic improvements while blocking regressions.

### Q-CAL-4: NG-3 fresh-instance verification scheduling

Three audit rounds pending fresh-instance verification (NG-3 on cont60 closure,
NG-5 on cont61 substrate work, NG-6 on cont63 P-NEW22 build). Each requires a
session of audit work. Timing affects when APE_REGISTER_v2.md can be promoted
to canonical and when cont60 closure can be marked permanently closed.

## 9. Multi-instance collaboration patterns

### Pattern A: parallel producer + audit

Instance 1 (producer) runs cont64 producer chain. Instance 2 (audit) reads
the cont63 close artifacts and produces NG-6 ledger on the P-NEW22 build.
Both instances work in parallel against the same substrate. Coordination is
asynchronous: NG-6 ledger lands when ready and informs cont65 prompt design.

### Pattern B: prompt design support

Instance 1 (designer) drafts the next cont prompt or NG audit prompt.
Instance 2 (verifier) reads the draft against this strategic plan and
identifies structural gaps (decorative verse anchors, missing Q0 enforcement,
out-of-scope additions).

### Pattern C: split MARAD-10 batch

Each instance takes 10 of the 20 MARAD-10 saves and rebuilds them in parallel
sessions. Coordination via saved_list.txt regeneration at session close (each
must merge).

### Pattern D: substrate inspection

Instance 1 inspects current substrate state (what is the current Kaggle
scoring formula? what do top public notebooks look like?). Instance 2 uses
the inspection results to inform strategic ranking. This is the Q-CAL items
above translated into work.

### What NOT to do across instances

- Do NOT have both instances modify saved_list.txt concurrently without merge
- Do NOT have both instances claim +N delta without coordination (APE-12 risk)
- Do NOT skip §11.4 Q0 because "the other instance probably checked"
- Do NOT promote artifacts (APE_REGISTER_v2.md, methodology files) without
  fresh-instance verification

## 10. Critical files for the parallel instance to read first

In priority order:

1. `cont63_saves/cont63_summary.md`: most recent producer state
2. `cont63_saves/FURQAN_LINT_ONNX_EXPANSION_PLAN.md`: tooling roadmap
3. `cont60_saves/STATE.md`: chain state baseline
4. `cont60_saves/METHODOLOGY.md`: process discipline + §11.4 with Q0
5. `cont61_saves/APE_REGISTER_v2.md`: anti-pattern register (canonical numbering)
6. `cont60_saves/NG_4_ledger.md`: NG audit format reference
7. `cont60_saves/cont60_summary.md`: closure execution example
8. `cont60_saves/f2_triage.md`: MARAD-10 cohort detail
9. `saved_list.txt`: canonical list of 335 saved tasks
10. `task_mapping.json`: task number to ARC-AGI hash map

The parallel instance should NOT read the entire `solutions/` directory; the
metadata is in saved_list.txt and the .onnx files are dense binary that does
not benefit human inspection. Inspect specific .onnx files only when
investigating a specific bug.

## 11. Reciprocal contract and discipline reminders

The audit chain (NG rounds) and producer chain (cont sessions) hold each
other accountable. The cont60 closure work demonstrated that single-author
chain at length 25+ sessions cannot rely on session-boundary discipline alone.
Tooling (furqan-lint expansion, automated CI gates) catches the bug shapes;
audit chain catches the structural patterns that tooling cannot reach.

A parallel Claude instance joining this chain should:

1. Honor the structural discipline as load-bearing, not decorative
2. Refuse to claim authority it does not have (no silent +N delta claims)
3. Surface QUESTIONs liberally rather than guess principal calibrations
4. Hold severity calibration to substrate evidence, not author preference
5. Treat session boundaries as fresh-instance proxies only for non-load-bearing checks
6. Refuse to skip §11.4 Q0
7. Refuse to promote artifacts (v2 versions, methodology updates) without fresh-instance verification
8. Respect Standing Rule 1 (no em-dashes)
9. Treat the cont63 task268 SAVED build as the most recent producer-chain demonstration, not as a precedent to compress further

## 12. The honest constraint

The chain is at 335/400 with mean score 11.79 against a leaderboard top of
22-24 mean. Even reaching 400/400 at current mean only gets us to ~4716
aggregate, well below 9000+. The score gap is per-save cost, not save count.

This means: ADDING SAVES is the easier path but the smaller-impact path.
OPTIMIZING SAVES is the harder path but where the leaderboard delta lives.
The MARAD-10 rebuild straddles both: it adds effective scoring saves (because
they currently score zero) AND optimizes per-save cost (because the rebuilds
will use efficient primitives).

The strategic implication: cont64 onwards should split session budget roughly
60% MARAD-10 rebuilds plus optimization-tier work, 40% new-primitive design.
Pure new-save work without optimization will plateau at ~4700 aggregate.

If Q-CAL-1 verification reveals the leaderboard top is exploiting a
measurement edge case (rather than genuine optimization), the strategic
implication shifts: maintain current producer chain pace, defer optimization
work, and either match the exploit (ethically questionable) or accept rank
below leaderboard top while shipping clean substrate.

## 13. Closing reciprocal note

This document is itself a producer-instance artifact. A fresh-instance NG
audit on this plan would be the appropriate next discipline step before the
parallel instance starts work. The reciprocal contract preserved.

End of multi-instance strategic plan.

---

# Bismillah ir-Rahman ir-Rahim
