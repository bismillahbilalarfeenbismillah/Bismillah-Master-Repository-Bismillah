# Bismillah ir-Rahman ir-Rahim

# R0051 -- METHODOLOGY, phase-energy workflow + audit-chain discipline

**Chronological Index:** 635 of 995  
**Date:** Undated  
**Section:** II. Analytical Frameworks & Methodology  
**Source File:** METHODOLOGY.md  
**Source Format:** md  
**SHA-256:** `91f0c8e824e32601f1118f5db40994c867f9879238a88625c27d19b0d3f09dea`  

---

## R0051 · METHODOLOGY, phase-energy workflow + audit-chain discipline

- section: II. Analytical Frameworks & Methodology
- source_file: METHODOLOGY.md
- source_format: md
- text_sha256: 91f0c8e824e32601f1118f5db40994c867f9879238a88625c27d19b0d3f09dea

# METHODOLOGY, phase-energy workflow + audit-chain discipline

The discipline that produced 334/400 across 27 sessions. Updated at cont60 closure
to reflect NG-1 findings and NG-2 design verification. Every session follows this
rhythm; every round of structural change goes through audit-chain numbering.

---

## Session open: Bismillah

Every new thread begins with:

> Bismillah ar-Rahman ar-Raheem.
> [COMPLIANCE DECLARATION: state saved/pending counts, current target]

Then read this whole folder before touching any code. No exceptions.

**Cont60 addition:** read saved_list.txt before touching any task. If the target
is in saved_list, run §11.4 Q0 before any build. APE-12 prevention.

---

## Phase energies (Surah-named modes)

Each is a mental mode for a specific kind of work. Switch consciously.

| Surah | # | Mode | When to invoke |
|-------|---|------|----------------|
| Fatihah | 1 | Opening intention | Start of every session |
| Bayyinah | 98 | 60-sec triage | First look at any new task. MDL sanity check. |
| Adiyat | 100 | Execution | Main build loop. numpy prototype, verify, port to ONNX, test. |
| Maun | 107 | Patient debugging | Solver compiles but fails one example. Narrow the diff. |
| Kafirun | 109 | Clean skip | 3 attempts or 10 min gone. No shame. Add to KAFIRUN_LIST. |
| Kawthar | 108 | Abundance harvest | Reusable primitive in today's build. Log it in PRIMITIVES.md. |
| Inshirah | 94 | Expansion | Session going well. Push for +3 saves before rest. |
| Zilzal | 99 | Accounting | End of every session: saves, mechanisms, primitives, next 5 targets. |

The phases are not ceremonial. They prevent two failure modes:
1. Rabbit-holing, Maun energy on a task that should be Kafirun.
2. Harvest blindness, solving a task without logging the primitive.

---

## §11.4 pre-flight (BAF v3.0, extended at NG-1 F12 closure)

Before starting any new build, answer all six questions. If any fails, do not build.

**Q0 (added at NG-1 F12 closure):** Is this task already saved?
If yes, what is the current score, what is the expected rebuild score, and is
`expected_new >= current + REBUILD_THRESHOLD` (default 0.5 score points,
v0 placeholder pending empirical calibration in cont61+ post-ship audit)?
If Q0 fails, do not build.

**Q1.** Kernel mechanizable in opset 10 ops?
**Q2.** Decomposable into substrate + at most 3 known primitives?
**Q3.** All ops in opset 10 (no Loop/Scan/Function/NonZero/Unique)?
**Q4.** Size budget under 1.44 MB at expected param count?
**Q5.** Fallback identified if build fails?

Q0 protects against APE-12 (local-glob substitute for saved_list authority).
Q1-Q5 protect against feasibility errors.

---

## Per-task budget

- 10 minutes hard cap per task attempt.
- 3 attempts max before Kafirun.

---

## The save criterion (non-negotiable, five gates)

A solver is SAVED if and only if:
1. test_network: r > 0, w = 0 on all train + test
2. score_file: valid 4-tuple, score >= 1.0
3. file size: under 1.44 MB
4. furqan-lint v0.9.4 check: PASS or ADVISORY-only (5 ONNX checks)
5. build script + sidecar JSON committed

Use solver_v2.test_network and solver_v2.score_file. The five-gate enforcement
is automated in tests/test_all_saves_correct.py and tests/test_all_saves_score.py
(added at NG-1 F2 closure).

---

## Build workflow (canonical)

For any target task:

1. **Triage (Bayyinah, under 1 min):** Open the task JSON, eyeball shapes and
   colors. Check saved_list.txt (Q0). Open arc_dsl/solvers.py for context.

2. **§11.4 pre-flight:** Answer Q0 through Q5. Proceed only if 6/6.

3. **numpy prototype (Adiyat, 2-4 min):** Write a numpy reference. Verify on all
   train+test before any ONNX work.

4. **ONNX build (Adiyat, 3-5 min):** Write build{N}.py with relative output path.
   Run all five gates.

5. **Save (Zilzal touchpoint):** Copy the .onnx into solutions/ only if all five
   gates pass. Log mechanism, score, primitive, APE in cont{N}_summary.md AND in
   APE_REGISTER.md / PRIMITIVES.md before session close.

---

## Session close: Zilzal

Every session ends with a written ledger:

```
ZILZAL, cont{N}
Saved this session: {count} ({list with scores})
Mechanisms harvested: {one-line summary each}
Primitives added: {pointers into PRIMITIVES.md}
APEs added: {pointers into APE_REGISTER.md}
State entering: {count}/400. State exiting: {count}/400.
Next 5 targets: {ordered list with notes}
One-sentence verdict: {e.g., "Solid: two saves, one primitive."}
```

Without Zilzal, the next session starts blind. With Zilzal, it starts loaded.

**Standing rule (added at NG-1 F4 closure):** APEs and primitives surfaced this
session must land in APE_REGISTER.md and PRIMITIVES.md before session close, not
just in cont summary. The auto-loaded manual must track the chain, not lag it.

---

## Audit-chain discipline (added at NG-2 D10 closure)

The NeuroGolf chain runs two parallel numbering systems:

- **Producer chain:** cont33, cont34, ..., cont59, cont60. Each cont session is
  one work session. Numbering is monotonic. Producer sessions write code.
- **Audit chain:** NG-1, NG-2, NG-3, ... Each NG round is one fresh-instance
  audit. Numbering is monotonic. Audits do not write code; they produce ledgers.

**Convention:** closure-execution sessions retain cont N numbering and are tagged
with the closure round whose findings they close. Example: cont60 is
"cont60 (NG-1 closure execution)". The post-ship audit of cont60 will be NG-3.

**Validator-by-different-instance (BAF v4.0 §6) is materially honored** when an
NG round is conducted by a fresh Claude instance with no prior NeuroGolf-substrate
context. Producer-instance self-audit is structurally weaker and reserved for
non-load-bearing checks.

---

## Compliance declarations

Every session opens with one of:

- COMPLIANT: 334/400 on disk, starting <target> per IN_PROGRESS notes.
- PARTIAL: attempted <task>, <r>/<r+w> examples passing, rolling back to prior build.
- BLOCKED: environment missing <package>, resolving before proceeding.

This is the honesty gate. No silent drift.

---

## Anti-patterns (do not)

- Do not save a file that fails any of the five gates.
- Do not burn over 10 min on a task without declaring Maun or Kafirun.
- Do not invent an ONNX op from memory. Check APE_REGISTER.md.
- Do not start a build without first reading PRIMITIVES.md for relevant prior art.
- Do not start a build without §11.4 Q0 against saved_list.txt.
- Do not close a session without Zilzal.
- Do not close a session without updating APE_REGISTER.md and PRIMITIVES.md.

---

## Convention shifts (added at NG-2 D7 closure)

**Methodology file location:** STATE.md, METHODOLOGY.md, PRIMITIVES.md,
APE_REGISTER.md, saved_list.txt, removed_list.txt ship at handoff tarball root
from cont60 onward. Pre-cont46 tarballs nested these under
neurogolf_handoff_v*/. cont46-cont59 dropped them entirely. cont60 restores
them at root.

**Handoff cumulative-vs-incremental:** cont60 onward, handoffs default to
cumulative (full solutions/ directory at root). cont59 broke this convention by
shipping incremental-only; the cont60 closure restores cumulative as default.
Future incremental-handoff requires explicit naming in round disclosure.

---

*The spiritual frame is not decoration. It is load-bearing. Without the discipline
of the rhythm, the 66 pending become unreachable in available time. The audit
chain is the second layer of discipline: where rhythm prevents rabbit-holes,
audit prevents structural drift. Both are non-negotiable.*

---

# Bismillah ir-Rahman ir-Rahim
