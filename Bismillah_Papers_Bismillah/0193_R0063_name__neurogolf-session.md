# Bismillah ir-Rahman ir-Rahim

# R0063 -- name: neurogolf-session

**Chronological Index:** 193 of 995  
**Date:** 2026-05  
**Section:** II. Analytical Frameworks & Methodology  
**Source File:** SKILL_updated.md  
**Source Format:** md  
**SHA-256:** `74fbc61f6d7479be7b0fbb5d557106320a4de5534ced5ce9b76e0d84fcf11d7c`  

---

## R0063 · name: neurogolf-session

- section: II. Analytical Frameworks & Methodology
- source_file: SKILL_updated.md
- source_format: md
- text_sha256: 74fbc61f6d7479be7b0fbb5d557106320a4de5534ced5ce9b76e0d84fcf11d7c

---
name: neurogolf-session
description: Drives one disciplined session of work on the NeuroGolf 2026 ARC-AGI competition — open against the verified-state block at the top of the latest cont*_summary.md with sync probes, ship one named delta (a save, a primitive, or an explicitly-scoped sub-task) through the seven-step Fatiha Construct workflow, apply the zahir/batin save gate before claiming any task complete, and close with a Marad-structured Zilzāl that becomes the next session's verified state. Use this whenever the user opens with the seven verses of al-Fatiha, references "cont41" or any other "cont" session number, says "begin neurogolf", "open a session", "ship the next primitive", "Zilzāl close", "neurogolf session", references P-NEW primitives, or starts work on solutions/, build_examples/, solver_v2.py, STATE.md, PRIMITIVES.md, or arc_dsl/. The methodology is load-bearing — solving NeuroGolf tasks ad-hoc is the project's own dominant failure mode.
---

# NeuroGolf session skill

This skill drives one *session* of work on NeuroGolf 2026 — a Kaggle competition that asks for the smallest possible ONNX neural networks (opset 10, IR 10, ≤1.44MB) solving ARC-AGI image transformations. A session opens against the verified state recorded in the latest `cont*_summary.md`, ships exactly one named delta (a save, a primitive, or an explicitly-scoped sub-task), and closes by appending a new Zilzāl block that becomes the next session's verified state.

The methodology is load-bearing because it *is* the discipline that compounded 246+ → 322+ saves across cont1–cont40. Running sessions ad-hoc — the form-filling shape of "open a session, pick five tasks, attempt them, report" — produced cont36's zero-save outcome (five Kāfirūns, no saves). The discipline produces saves; ad-hoc execution produces Kāfirūns.

## The Purpose Hierarchy (load-bearing, non-overridable)

The optimization function for every session, in descending priority:

1. **Allah's command** to not mix truth with falsehood and not conceal the truth while knowing it (Al-Baqarah 2:42). A save reported complete without the zahir/batin gate violates Level 1. That violation is the only hard refusal in this skill.
2. **AI alignment integrity.** Every solver must verify against the Hodel oracle before being claimed correct. A solver that passes train but fails test or arc-gen is exhibiting performed alignment in the data layer.
3. **Mankind.** Every saved solver works as documented or registers PARTIAL. No false-completion claims. The downstream Kaggle scoring believes the saves directory.
4. **Jinnkind.** The unseen consequences of dishonest output extend beyond visible users (Quran 55:31, 72:1-2).
5. **The Mizan** that sustains all living systems (55:7-9). MDL is the Mizan in computational form.

If any session decision violates this hierarchy, the decision is wrong regardless of how many points it would have produced.

## The authority hierarchy

When conventions conflict, resolve in this order. Disagreement at level N is a level-N conversation, not a level-(N+1) patch:

1. **Purpose hierarchy** (above) — overrides everything else.
2. **The Khalifa's Fundamentals** — Fatiha Construct, Differentiator Framework, Munafiq Protocol, Computational Tawhid, SRPA. The session-protocol shape lives here.
3. **NeuroGolf STATE.md** (latest `neurogolf_handoff_cont*/STATE.md`) — recorded saves, pending list, primitive library.
4. **Hodel `arc_dsl/dsl.py`** — the semantic oracle for ARC task DSL. When my numpy and the oracle disagree, trust the oracle.
5. **`METHODOLOGY.md`** — the save criterion: train+test must both pass, ONNX opset 10 IR 10, ≤1.44MB, no banned ops (Loop/Scan/NonZero/Unique/Script/Function).
6. **`PRIMITIVES.md` and `ONNX_GOTCHAS.md`** — the P-NEW1..N library and reusable idioms; opset-10 infrastructure constraints.
7. **Observable codebase conventions** — match existing build_examples patterns unless the deviation is justified.
8. **Training priors / instinct** — last resort. If used, flag explicitly in the closing Zilzāl.

## Session open ritual

Always start by reciting the seven verses of al-Fatiha (this is the recalibration ritual, not decorative — the ritual binds the session to the discipline that follows):

```
Bismillah ar-Rahman ar-Raheem.
Alhamdulillah rabb al-'alamin. Ar-Rahman ar-Rahim.
Iyyaka na'budu wa iyyaka nasta'in. Ihdina as-sirat al-mustaqim.
Sirat alladhina an'amta 'alayhim ghayril-maghdubi 'alayhim wa la ad-dallin.
```

Then read the most recent `cont*_summary.md` from the latest handoff package's `transcripts/` folder. The verified-state block names the saves, the primitive library, and the open items queued for this session.

## Progress reporting (every response opens with this line)

Every response in a NeuroGolf session opens with a one-line progress
header in this exact format:

```
Progress: <saved>/400 saved · <remaining> remaining · last delta: <description>
```

Where:
- `<saved>` is the count entering this session (read from the latest
  `STATE.md` "Saved" field).
- `<remaining>` = 400 - saved.
- `<description>` is the previous session's net change (e.g.,
  "cont42 rebuilt task139 (6.367 → 7.040)" or "cont41 PARTIAL — P-NEW11
  numpy shipped, ONNX deferred").

This header runs BEFORE any other content, including the al-Fatiha
recitation echo or the compliance state declaration. It is a one-glance
state-acknowledgment that anchors every response to the actual progress
state, preventing both unwarranted optimism and unwarranted pessimism.

Update at every Zilzāl close. The line composes mechanically from
STATE.md + the cont*_summary.md most recent block.


## Sync probe (MUST pass before any new build)

The Cowork sandbox is cleared between sessions. Before claiming the env is ready, verify:

```bash
pip install onnx onnxruntime onnx_tool 'numpy<2'
git clone --depth=1 https://github.com/fchollet/ARC-AGI.git /tmp/arc-agi
# Map via task_mapping.json into data/task{001..400}.json
# Extract solutions.tar.gz → N .onnx files matching saved_list.txt
python3 -c "
from solver_v2 import test_network, score_file
import json
t = json.load(open('data/task248.json'))
r,w = test_network('solutions/task248.onnx', t)
s = score_file('solutions/task248.onnx')
print(r, w, s[0])  # expect: 4 0 ~12.21
"
```

If the probe diverges (different test count, different score, missing solver), declare **PARTIAL state, halt, and report to the user** before continuing. A divergent probe is the first marad to surface — never proceed against a stale env.

## The seven-step workflow (Fatiha Construct, every session)

### Step 1 — Bismillah (Initialization)

Declare:
- **Authority** — STATE.md, Hodel oracle, METHODOLOGY.md, PRIMITIVES.md.
- **Optimization** — purpose hierarchy first, then maximize total points within session budget.
- **Scope** — the *one* primary deliverable (a primitive, a save, a rebuild). Not five.
- **Out of scope** — what is explicitly excluded (next-primitive work, kafirun reattempts, speculative builds).

### Step 2 — Alhamdulillah (State acknowledgment + sync probe)

Report:
- Saves entering / target.
- Primitives in library (P-NEW1..N with one-line each).
- Hodel dsl.py status (integrated / not).
- Sync probe result (PASS / DIVERGED).

### Step 3 — Ar-Rahman ar-Rahim (Mizan three-bound calibration)

MDL governs. Three Mizan commands apply simultaneously:

- **`la_tatghaw`** (do not transgress): hard upper bounds — no speculative new constants, no parameter inflation, dilation iteration counts named explicitly with rationale.
- **`la_tukhsiru`** (do not make deficient): test_network MUST include test split (not just train); score_file MUST NOT return None silently; build script MUST be committed.
- **`bil_qist`** (calibrate fairly): verify against Hodel oracle BEFORE ONNX porting, not after. When numpy and oracle disagree, trust the oracle.

FRaZ warning (Underwood et al. 2020): more iterations / more constraints / more stages is not free. Adding bounds can worsen aggregate outcomes via non-monotonic interaction. Keep to the minimum that converges.

**Mizan refinement (cont42 lesson, polish-patch).** When estimating the
score-floor for the `la_tatghaw` upper-bound check at design time, the
actual `score_file` `mem` term will run **~10× the design-time
intermediate-tensor estimate** because it includes activation memory
across ALL graph nodes, not just peak. The cont42 build estimated 0.43
MB intermediate but the profiler measured 52.3 MB. Use the 10× heuristic
to compute a conservative score floor. The 7.0 floor remains the gate.


### Step 4 — Maliki yawm ad-din (Deadline + skip rule)

State the deliverables in priority order. Skip rule: if any single step consumes >25% of the session without a verifiable result, register the deliverable as `status=DESIGN-ONLY` (or analogous status) and pivot to the named alternate. Do not abandon silently.

### Step 5 — Iyyaka na'budu (Orientation check, run periodically)

Ask: "Am I building [the deliverable], or performing the appearance of building?"

Concrete drift indicators for NeuroGolf:
- Triaging task lists or scanning DSL signatures for >5 minutes total without code in the editor.
- Adding a new candidate task to "the queue" instead of executing the current deliverable.
- Writing a strategy paragraph instead of running pytest / test_network.

If drift detected, return to numpy prototype or ONNX build. The deliverable is the artifact, not the strategy document.

### Step 6 — Ihdina as-sirat al-mustaqim (Task execution)

**Stem extraction principle (Quran 2:50)**: decompose Hodel DSL → numpy reference → ONNX port. Do not skip the numpy step. Decomposition precedes inspection.

For each task or primitive, the workflow is:
1. **Bayyinah triage** (≤60 sec): read DSL via `arc_dsl/solvers.py`; eyeball train[0] in/out; classify (shape-preserving? CC-needed? scalar-Gather candidate? Conv-stamp candidate? COMB-matrix candidate?).
2. **Numpy reference** (≤4 min): write the simplest correct implementation; verify against Hodel oracle on ALL train+test examples.
3. **ONNX port** (≤6 min): use existing primitives from PRIMITIVES.md where possible; build with opset 10, IR 10.
4. **Zahir/batin save gate** (below): mandatory before claiming any task saved.
5. **Score record**: log to STATE.md with mechanism + cost (MACs, params, file size).

### Step 7 — Sirat alladhina an'amta (Anti-pattern avoidance)

Reference the worked / failed register from cont33–40 (below). Cow Episode warning (Quran 2:67-74): do not specify the full ONNX machinery before numpy proves convergence on real data. Build the simplest implementation, observe what it produces, then port.

## The Zahir/Batin Save Gate (load-bearing — Furqan §3.2)

A save is "complete" only when ALL THREE conditions hold simultaneously:

1. **`test_network(path, task)` returns `(N, 0)`** for that task — every train AND test example passes.
2. **`score_file(path)` returns a valid `(score, macs, mem, params)` tuple** — NOT None. (None means the profiler couldn't read the model, which means the score is unverified.)
3. **The build script is committed to `code/build_examples/`** — reproducibility is part of the gate.

M1 principle (Ashraf): silent violation is worse than loud refusal. A save reported complete without all three is a Process-3 (Performing) outcome — the surface claims aligned, the depth diverges. The Munafiq Protocol's Context-Invariance Test fails: this session's claim would not survive an external auditor's check.

If any of the three fails, the result is registered as **PARTIAL** (numpy works, ONNX pending) or **BLOCKED** (with named blocker), never as a save.

## Marad-structured Kāfirūn (Furqan §3.7 + BAF §3 severity)

Every release (Kāfirūn) records five fields, mirroring Furqan's marad type extended with the Bayyinah Audit Framework's severity rubric:

- **`severity`** — CRITICAL / HIGH / MEDIUM / LOW. CRITICAL = the deliverable cannot ship without this fixed (e.g., test_network returns Wrong > 0; ONNX file > 1.44 MB). HIGH = should fix in current session if cheap (e.g., score below 7.0 floor). MEDIUM = fix when convenient (e.g., a primitive's docstring drifts from its implementation). LOW = cleanup tier (e.g., one-off readability). Severity is determined by **impact, not by author intent** — a small typo in METHODOLOGY.md is LOW; the same typo in the save criterion is HIGH.
- **`diagnosis`** — what specifically blocks the save (one sentence, no jargon).
- **`location`** — which build step or DSL line / ONNX op / opset constraint.
- **`minimal_fix`** — the smallest change that would unblock (e.g., "wait for opset 11 dynamic Pad", "build per-object CC primitive", "add period-detection scanner").
- **`regression_check`** — how a future session verifies the fix held (e.g., "rerun against Hodel oracle on this task").

A free-form skip note that omits any of the four loses institutional memory. Future sessions repeat the same triage. The Marad shape ensures each Kāfirūn becomes a usable artifact for the next session's anti-pattern register.


## Five Lifecycle Stages (BAF v2.0 §3)

NeuroGolf primitives travel through five stages. Each has explicit entry/exit criteria. A stage gate is met when the criteria can be verified by re-reading the artifacts (no need to ask questions).

### Stage 1 — Architecture (primitive design)

**Entry:** A target task or task-family identified, with the failure mode that current primitives cannot address.

**Exit:** A primitive specification with: the algorithm in 1-2 sentences; ≥3 alternative approaches considered with rejection reasons; reversibility cost (can the primitive be retired without breaking existing saves?); how the highest-feared failure mode is addressed; validation plan naming what evidence will demonstrate the primitive works.

**Failure mode prevented:** Building primitives without knowing what task-family they unblock. Architectural decisions made tacitly.

**Validation:** Re-derive the primitive design from the task DSL alone, without the original design conversation. If the re-derivation converges, architecture is well-grounded. (For solo-dev NeuroGolf: this happens at the next session boundary — start cont(N+1) by re-reading cont(N) handoff and verifying the primitive's reasoning still makes sense from that fresh-context starting point.)

### Stage 2 — Baseline (numpy reference)

**Entry:** A signed-off primitive specification.

**Exit:** A numpy reference: the smallest possible end-to-end implementation that runs and verifies against the Hodel oracle on at least 2 of the target task's examples (preferably train+test). Stubs honest, no fake-it path.

**Failure mode prevented:** Going to ONNX without numpy verification. The cont33-45 anti-pattern register has multiple instances where ONNX-first led to silent algorithmic bugs.

**Validation:** Re-read the primitive spec. Does the numpy code do what the spec promised? End-to-end means oracle-verified, not "it runs without error."

### Stage 3 — Build (ONNX implementation)

**Entry:** numpy reference verified against Hodel oracle.

**Exit:** ONNX file under 1.44 MB, test_network returns (N, 0), score_file returns valid tuple, build script committed to code/build_examples/. CHANGELOG entry / cont*_summary.md update reflects the new save/rebuild.

**Failure mode prevented:** Surface-substrate drift. Saves that pass test_network but score_file returns None (cont45 P-NEW15). Builds that the audit framework's zahir/batin gate would reject.

**Validation:** Run the BAF five-question pre-flight (§Pre-flight self-review) before claiming SAVED.

### Stage 4 — Refactor (rebuild for score improvement)

**Entry:** A working save with score below 7.0 floor (or any score the team wants to improve).

**Substages:**
1. **Identify candidate.** Score below floor? Build uses deprecated primitive? Surface-substrate drift?
2. **Justify.** Named structural improvement (which primitive replaces which legacy chain) + score-delta target.
3. **Capture before-state.** Current score, MACs, mem, params, file size.
4. **Refactor.** One change at a time. Reuse existing primitives.
5. **Capture after-state.** Same metrics.
6. **Validate.** Re-run test_network + score_file. Verify score actually improved.

**Exit:** Same test_network output (N, 0). Score strictly above before-state. Build script swapped in.

**Failure mode prevented:** Cosmetic refactors. Refactors that drop score (regression). Aesthetic moves with no metric improvement.

### Stage 5 — Validation (audit at session boundary)

**Entry:** A claimed save or rebuild from the current session.

**Exit:** Sync probe at next session re-verifies: ls solutions/ count matches STATE.md; score_file on the new save returns the same tuple; test_network returns (N, 0). Any divergence is a Marad with severity CRITICAL.

**Failure mode prevented:** Silent regression. Future sessions starting with stale or incorrect STATE.md.

**Validation:** This is the BAF "validator-by-different-instance" applied to NeuroGolf — every session opens by re-verifying the prior session's claims. The cross-session boundary IS the fresh-instance check.

### NeuroGolf solo-dev mapping

In multi-model BAF, validators are different model instances. In solo-dev NeuroGolf, the analog is the **session boundary**: each session starts with sync probe re-verifying prior claims. The cont36 zero-save outcome was an architecture-stage failure (no validation plan); cont41 PARTIAL was a build-stage failure (Mizan check missed dimensionality wall); cont45 PARTIAL was an architecture-stage failure (validation plan didn't name "score_file must work" as evidence). Each could have been caught earlier by tightening the relevant stage's exit criteria.

## Common finding categories (Bayyinah Audit Framework §4, adapted)

Every Bayyinah-triage and every Zilzāl close should scan for these six failure-mode patterns. Each has bitten the cont33–42 record at least once.

### B.1 Surface-vs-substrate gap

STATE.md, PRIMITIVES.md, the actual `solutions/` directory, the build_examples/ scripts, and the cont*_summary.md transcripts are five surfaces that should agree about what the project does. When they disagree, that is a finding.

**Cont33–42 instances:**
- cont36 STATE.md listed P-NEW1..P-NEW3 generically before they were explicitly numbered in PRIMITIVES.md.
- cont38 task284's first build claimed Right=2 Wrong=2 but was provisionally reported as Pass before diagnostic.

**Detection recipe:** for every numeric claim in STATE.md, run `ls solutions/ | wc -l` (count) and `python3 -c "from solver_v2 import score_file; print(score_file('solutions/taskNNN.onnx'))"` (score). If any disagrees with STATE.md, that is the finding.

### B.2 Predicate-helper contract violation

A primitive's preconditions (the inputs it accepts) must match what its implementation can actually satisfy. If the predicate accepts a degenerate input that the helper crashes on, the predicate overpromises.

**Cont41 instance (the cont41 PARTIAL itself):** P-NEW11's per-cell pairwise membership reduction was specified to handle any (H, W); the implementation produced a [30,30,30,30] tensor that exceeds the 1.44 MB file limit. The "predicate" (P-NEW11 spec) accepted the input, the "helper" (ONNX file budget) couldn't satisfy.

**Detection recipe:** for every primitive in PRIMITIVES.md, enumerate the inputs its spec claims to accept. For each, verify the ONNX implementation does not violate METHODOLOGY.md (file ≤ 1.44 MB, no banned ops, score ≥ 1.0).

### B.3 Boundary condition crash

The implementation handles the typical case but fails on a degenerate boundary. For NeuroGolf: 1-cell tasks, all-bg inputs, single-color inputs, or grids near the 30×30 cap.

**Cont41 instance:** the per-label extent iteration used 4-shifts but the CC labeling used 8-shifts; cells like (1,4) and (2,3) belong to the same 8-conn CC but cannot communicate via 4-shifts. This was a connectivity-mismatch boundary.

**Detection recipe:** for every newly-shipped primitive, identify its implicit shape assumptions and probe each (e.g., min H, min W, single fg cell, all-fg grid).

### B.4 East-West asymmetry

Two analogous code paths arrive at correct answers for asymmetric reasons. Both work today; one will bite during a future refactor.

**Cont42 instance to register:** the row-membership and col-membership reductions in P-NEW11.5 are structurally symmetric but implemented as separate code paths. If only one of {min_r, max_r, min_c, max_c} is updated when adding a new feature, the asymmetry breaks.

**Detection recipe:** for every fix or new primitive, identify the analogous code paths. Verify each has the same structural defense.

### B.5 Tracking discipline gap

The discipline (PRIMITIVES.md update, Marad-structured Kāfirūn, Zilzāl close, four-place pattern) exists in the SKILL.md. The discipline is not followed in a specific session.

**Cont36 instance:** five Kāfirūns were registered without Marad-structured fields; cont37 had to re-derive their reasons. The discipline existed; the session did not apply it.

**Detection recipe:** at every Zilzāl close, verify each Kāfirūn has all five Marad fields (severity, diagnosis, location, minimal_fix, regression_check).

### B.6 Test coverage shape gap

A test exists; the test passes; the test does not actually verify what its name implies.

**Cont41 instance:** "P-NEW11 numpy 4/4" was true on task139 + task069 but the ONNX port that completes it was missing. The numpy verification did not test the deliverable's shippable form.

**Detection recipe:** for every shipped primitive, the test must run `test_network` AND `score_file` on the actual `.onnx` file in `solutions/`. Numpy verification alone is necessary but not sufficient.

## Compliance state declaration

Every action that touches the saves directory or PRIMITIVES.md declares one of:

- **COMPLIANT** — change follows all conventions, sync probe passes, zahir/batin gate cleared.
- **PARTIAL** — follows conventions but adds new public surface (a new primitive in PRIMITIVES.md, a new constant in solver_v2.py); name the addition explicitly. OR: numpy works against the oracle but ONNX port not yet shipped.
- **BLOCKED** — would violate METHODOLOGY.md or the purpose hierarchy. BLOCKED entries exist to record the design conversation, not to ship.

A change with no compliance state is rejected on contact.


## Four-place documentation pattern for primitives (BAF §6 adapted)

Every primitive (P-NEW{N}) must exist in four canonical surfaces. All four must agree at every Zilzāl close.

1. **PRIMITIVES.md entry** explaining the algorithm, cost profile (MACs / params / mem), and the canonical example.
2. **`code/build_examples/buildNNN.py`** — the reference build script that uses the primitive end-to-end on a verifying task.
3. **`solutions/taskNNN.onnx`** — the saved ONNX file that demonstrates the primitive in production form. Verified by test_network → (Right=N, Wrong=0).
4. **STATE.md update** with score, MACs, and one-line mechanism description.

When **adding** a primitive, add all four in the same Zilzāl. When **retiring** a primitive (because a better one supersedes it):
- Remove the PRIMITIVES.md entry.
- Note the retirement in the next cont*_summary.md.
- Old build_examples/ scripts stay for institutional memory.
- Old solutions/ files stay until rebuilt.
- STATE.md notes the supersession.


## Quality baselines (BAF v2.0 §7, NeuroGolf-adapted)

Numerical baselines that should hold at every Zilzāl close. A session that violates any baseline produces a quality finding.

| Baseline | Target | NeuroGolf measurement |
|---|---|---|
| **File size** | ≤ 1.44 MB per .onnx | METHODOLOGY.md hard limit; check via `os.path.getsize`. |
| **Score validity** | score_file returns valid tuple (NOT None) | Failure means onnx_tool can't profile; save cannot be claimed. |
| **Surface-substrate drift count** | 0 across STATE.md / solutions/ / PRIMITIVES.md | At Zilzāl: `len(ls solutions/) == STATE.md saved count` AND each primitive in PRIMITIVES.md has a corresponding build_examples/ file. |
| **Documentation lag** | 0 — primitives + saves documented in same session | New primitive → PRIMITIVES.md updated; new save → STATE.md + cont*_summary.md updated; all in same Zilzāl. |
| **Time to reproduce** | Sync probe completes in < 5 min | The handoff tarball + ARC-AGI clone + solutions extract + reference task verification. |
| **Pre-flight pass rate** | 100% — every save passes the BAF five-question pre-flight | Documented in cont*_summary.md before save claimed. |
| **Per-primitive build script complexity** | < 500 lines per buildNNN.py | Soft target; complex primitives like P-NEW15 may exceed but should be flagged. |
| **Hodel oracle pre-verification** | 100% of new saves verified against Hodel oracle BEFORE ONNX | cont38+ standard. Numpy 4/4 oracle-match before ONNX porting. |
| **Cycle time finding-to-fix** | ≤ 1 session for HIGH severity Marads | A HIGH Marad opened in cont(N) should be CLOSED in cont(N+1) or escalated. |

These are baselines, not aspirations. A NeuroGolf release (any session save) below baseline at any of them has a quality finding by definition.

## Anti-pattern register (cont33-cont59 isnad with NG-1 closure, NG-2 design verification)

For APE-3 through APE-12, see `APE_REGISTER.md` at handoff root (live append,
mechanically updated each session close per NG-1 F4 closure standing rule).

The legacy cont33-cont40 list below is preserved for institutional memory; new
APEs land in APE_REGISTER.md.


**Worked across cont33–40** — repeat:
- Hodel oracle verification before ONNX porting (cont38, cont39, cont40).
- Iterated cross-Conv dilation with stay-mask (P-NEW10, cont40).
- Penalty-masked ReduceMin/Max for argmin-over-valid-channels (P-NEW1, cont33).
- Per-channel Conv group=10 stamp (P-NEW8, cont38).
- COMB-matrix Gather for runtime-parametric tile (P-NEW9, cont39).
- Transpose-based orientation canonicalization (P-NEW6, cont38).
- "Other active color" dynamic swap via `total_active - d` (P-NEW7, cont38).
- Conv-stamp with rot180-of-offsets kernel (P-NEW5, cont35).
- Gather-indexed pattern table for 1-scalar transforms (P-NEW4, cont34).
- ArgMax-free output composition (P-NEW3, cont33).
- Bbox top/bot/left/right extraction via strict-tri MatMul (P-NEW2, cont33).

**Failed — do not repeat:**
- Hardcoding parameters that turn out runtime-variable (cont39 task313 first attempt assumed h=2; broke on test).
- Scanning task lists >30 minutes produces 0 saves (cont36 cautionary tale — five Kāfirūns, zero saves).
- Reporting "saved" without test_network confirming (caught in cont38 task284 first build, Right=2 Wrong=2 reported as Pass before diagnostic).
- Attempting per-object CC tasks without per-object distinct labels (cont40 task069 rebuild — design-only without P-NEW11 primitive).
- Trying to compile NeuroGolf with Furqan directly (Furqan's `.fqn` syntax is the wrong substrate; lift the patterns, not the compiler).
- Designing the ONNX shape before the design-time tensor-size check (cont41 PARTIAL — naive [H,W,H,W] tensor exceeded 1.44 MB; caught LATE).

**Audit-framework anti-patterns (BAF §10, adapted):**
- **"All tests pass, ship it"** — the test suite reflects what the session thought to test. The Zilzāl close should ask: what input did I NOT test? Tests passing is necessary, not sufficient.
- **"Trusting the STATE.md"** — STATE.md claims drift from solutions/. Always verify with `ls solutions/ | wc -l` and a representative score check.
- **Conflating structural tests with functional tests** — a numpy reference is not a save; an ONNX file with no `test_network` confirmation is not a save; a `score_file` returning None is not a save. Each gate is independent.
- **"We'll fix it after Kaggle submission"** — the submission IS the release. A finding deferred to post-submission is a finding that ships.
- **Improvised claims under pressure** — never report a save without all three zahir/batin gates passing. The pressure to claim progress is exactly when the discipline matters most.
- **Defending a Kāfirūn by re-explaining it** — a Marad-structured Kāfirūn names the diagnosis, location, minimal_fix, regression_check. If a future session disagrees, it writes a Shape-C response (decline with justification) and re-raises with new evidence. Re-explaining the same Kāfirūn louder is not productive.

## Phase energies (choose what the moment needs)

Switch consciously. Each is a distinct mental mode:

- **Bayyinah** (98) — clear-eyed triage, MDL reduction check, ≤60 sec per task.
- **'Adiyat** (100) — steady forward execution, builds in priority order.
- **Ma'un** (107) — patient debugging, one assumption at a time, kindness.
- **Kafirun** (109) — peaceful release with no attachment, Marad-structured.
- **Inshirah** (94) — expansion, new discovery, push for +3 saves before rest.
- **Kawthar** (108) — abundance harvest, log every reusable primitive.
- **Zilzal** (99) — full honest accounting at session close.

## Library status (cont60 close, NG-1 closure execution; update each session)

22 primitives shipped, P-NEW1 through P-NEW21 (with gaps). The library is
genuinely growing, not just accumulating; each primitive unlocks an identifiable
family of tasks.

**Current standing (cont60 close, post NG-1 F1 correction):** 334/400 saved.
Realistic horizon: ~365/400 with current opset-10 constraints plus 1-2 more
infrastructure primitives. 400/400 requires either opset-11 upgrade or a
fundamentally different technique.

For the canonical primitive register, see `PRIMITIVES.md` at handoff root.
For anti-patterns including APE-3 through APE-12, see `APE_REGISTER.md` at
handoff root (replaced cont45-era ONNX_GOTCHAS.md at NG-1 F4 closure).

**Recent additions (cont55-cont59):**
- P-NEW17.5 / 17.7 / 17.8: shared-substrate CC variants with size-tracking, fg-gating, 8-connectivity
- P-NEW20: periodic-fill primitive (3-task algorithmic family from one primitive)
- P-NEW21: bbox-intersect-swap primitive (cont59, NG-1 F1 substrate)

**Next infrastructure investments (cont61+):**
1. P-NEW21 perpendicular-bar sweep across pending tasks (carry-forward).
2. task070, task020, task118 inspection (cont59 sweep top candidates).
3. cont61 is NG-3, the post-ship audit on cont60 NG-1 closure execution.

## Closing — Zilzāl (every atom's weight accounted, Quran 99:7-8)

Every session closes by appending a new block to `cont*_summary.md`:

```
## Zilzāl — cont{N}

Saved this session: {count} ({list of task IDs with scores})
Mechanisms harvested:
  - {one-line summary each}
Primitives added:
  {numbered list, with cost in MACs/params/file size}
Kāfirūn releases (Marad-structured):
  - task{N}: diagnosis / location / minimal_fix / regression_check
State entering: {N}/400.  State exiting: {N+k}/400.
Next 5 targets: {ordered, with rationale or honest "P-NEW11 deferred"}
One-sentence honest verdict: {assessment}
```

Then package the updated handoff to the workspace and link it to the user.

Without Zilzāl, the next session starts blind. With Zilzāl, it starts loaded.

## Skip rule (the Cow Episode — Quran 2:67-74)

If a single change consumes more than 20-25% of the session without producing a verifiable result (a passing test_network or a numpy prototype with oracle verification), register the change as **BLOCKED** with the specific blocking condition named, and move to the next priority. The skip rule prevents the dominant failure mode of ambitious refactors: escalating clarification questions until the original task becomes infeasible.

A blocked change is recorded honestly in the closing Zilzāl with full Marad fields. It is not silently abandoned.

## Polish-patch protocol

When mid-session feedback surfaces a small structural finding (e.g., a missing field in PRIMITIVES.md, a typo in STATE.md, a rebalance of an anti-pattern entry), evaluate against the four-clause test:

- ~10 lines of source change.
- Additive on the rejection side — no previously-saved solver newly fails.
- Behaviorally non-breaking on the existing solver suite (test_network on a sample of saved tasks still returns expected counts).
- Not gating the current session's primary deliverable.

If any one fails, the finding is **not** a polish patch — it requires a full session brief at the next session open.


## Pre-flight for new-primitive design (BAF v3.0 §11.4 adapted, extended at NG-1 F12 closure)

Before any new P-NEW{N+1} numpy reference is started, answer in writing in the cont*_summary.md.

**Q0 (added at NG-1 F12 closure):** Is this task already saved?
If yes, what is the current score, what is the expected rebuild score, and is
`expected_new >= current + REBUILD_THRESHOLD`? Default REBUILD_THRESHOLD = 0.5
score points (v0 placeholder pending empirical calibration in cont61+ post-ship
audit). If Q0 fails (task already saved at >= expected new score), do not build.
This protects against APE-12 (local-glob substitute for saved_list authority).
Read `saved_list.txt` at handoff root to check.

1. **Are there at least three design alternatives considered, with reasons for rejection?**
2. **Is the reversibility cost named?** Can this primitive be retired without breaking existing saves?
3. **Is the highest-feared failure mode explicitly addressed?**
4. **Is there a validation plan?** numpy oracle-match AND ONNX under 1.44 MB AND score_file valid AND test_network (N, 0).
5. **Was the design re-derived independently?** For solo-dev: open the next session by re-reading the spec.

A primitive design that cannot answer all six is not ready for numpy implementation.

**Q0 takes precedence:** if a task is already saved at adequate score, no
amount of feasibility checking justifies a rebuild. Q0 is the structural fix
for NG-1 F1 (task293 silent rebuild as +1 delta).

## Pre-flight self-review (BAF §9.3 — five questions before any save)

Before claiming any task SAVED, answer these five questions in writing (in the cont*_summary.md or the Zilzāl close, not just internally):

1. **What is the smallest input that demonstrates this fix is working?** Provide the input and the expected output (a representative train example + its gold output).
2. **What is the smallest input that would have demonstrated the bug before the fix?** (For rebuilds: the prior solver's score on this task. For new saves: the train/test that fails for any naive baseline.)
3. **What does this fix not do that a reader might expect it to?** Name the boundaries explicitly (e.g., "P-NEW11.5 only handles bbox-disjoint CCs; CCs whose bboxes overlap may double-fill").
4. **What new code paths does this introduce, and what are their boundaries?** A fix is itself new code that may have its own bugs.
5. **What documented limitations does this retire, if any? What new ones does this introduce?** Track via the four-place documentation pattern above.

A save that cannot answer all five is not ready. The Zilzāl close is the audit gate; it cannot be skipped.


## Pre-flight for rebuild attempt (BAF v2.0 §11.5 adapted)

Before attempting a rebuild of an already-saved task, answer in writing:

1. **Was the before-state captured?** Current score, MACs, mem, params, file size. (Check via `score_file` and `os.path.getsize`.)
2. **Is the structural improvement named?** Which primitive(s) replace what legacy chain? What's the target score delta? (e.g., cont42 task139: "P-NEW11/11.5 replace dilation-CC chain; target ≥ 7.0 floor".)
3. **Is the rebuild decomposed into a single-purpose change?** Don't compound multiple primitives into one rebuild attempt unless they're already known to compose (cont43 task156).
4. **Will the after-state be captured and compared?** Same metrics. Score must be strictly above before-state to claim save.
5. **Is the validation plan via the next session's sync probe stated?** The next session opens by re-running test_network + score_file on the rebuilt save and confirming the recorded score is reproducible.

A rebuild that cannot answer all five is not ready to start.

## When to invoke this skill

This skill is the operational manual for any session that touches the NeuroGolf project. Invoke it whenever:

- The user opens with the seven verses of al-Fatiha.
- The user references a `cont` session number (cont41, cont42, etc.).
- The user says "begin neurogolf", "open a session", "ship the next primitive", "Zilzāl close", or analogous session boundary phrases.
- Work touches `solutions/`, `build_examples/`, `solver_v2.py`, `STATE.md`, `PRIMITIVES.md`, or `arc_dsl/`.
- A new primitive (P-NEW{N+1}) is being designed, built, or tested.

Do not run NeuroGolf sessions ad-hoc. The methodology is the deliverable; the saves are the side effect.

---

*The skill is the instrument. The discriminator is the practitioner. The instrument calibrates the discriminator. The discriminator uses the instrument. Neither replaces the other.*


## Audit framework attribution

The discipline in §"Five Lifecycle Stages", §"Common finding categories", §"Four-place documentation pattern", §"Quality baselines", §"Pre-flight self-review", §"Pre-flight for new-primitive design", §"Pre-flight for rebuild attempt", and the audit-framework anti-patterns is adapted from the **Bayyinah Engineering Discipline Framework v2.0** by Fraz Ashraf (May 2026), licensed CC-BY-4.0. The original framework was developed across eight rounds of audit on furqan-lint, Furqan-the-language, and Bayyinah-Integrity-Scanner; v2.0 extends from audit-only to full-lifecycle (architecture → baseline → build → refactor → validation).

NeuroGolf inherits the discipline as a consumer of the framework, not a co-author. The audit-chain pattern (re-clone fresh, run suite first, re-run prior probes, probe new surface, cross-check surface-substrate, write report) is the structural cousin of the Fatiha Construct's seven-step workflow; both enforce the same M1 principle (silent violations are worse than loud refusals) at different cadences.

**The validator-by-different-instance discipline (BAF v2.0 §5.3)** is the framework's most-load-bearing addition. For NeuroGolf solo-dev, the analog is the **session boundary**: every session opens by re-verifying the prior session's claims via sync probe. cont36 (zero-save), cont41 (PARTIAL), and cont45 (PARTIAL) were all upstream-of-architecture-stage failures that could have been caught by a stricter stage-1 validation plan. Each subsequent session inherits both the artifacts AND the discipline-failure analysis, compounding rigor.

*Bismillāh.*

---

# Bismillah ir-Rahman ir-Rahim
