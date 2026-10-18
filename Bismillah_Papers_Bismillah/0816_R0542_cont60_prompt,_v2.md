# Bismillah ir-Rahman ir-Rahim

# R0542 -- cont60 prompt, v2

**Chronological Index:** 816 of 995  
**Date:** Undated  
**Section:** VIII. NeuroGolf (ARC-AGI / ONNX)  
**Source File:** cont60_prompt_v2.md  
**Source Format:** md  
**SHA-256:** `7715d98095e36c700455e7ff4741c7fc83150514785f5334bba183209fcedf0e`  

---

## R0542 · cont60 prompt, v2

- section: VIII. NeuroGolf (ARC-AGI / ONNX)
- source_file: cont60_prompt_v2.md
- source_format: md
- text_sha256: 7715d98095e36c700455e7ff4741c7fc83150514785f5334bba183209fcedf0e

# cont60 prompt, v2

**Status:** post-NG-2 closure of v1 findings. Pending Q1 and Q2 principal resolution before execution.
**Round disclosure:** cont60 (NG-1 closure execution). NOT a producer round. Original P-NEW21 perpendicular-bar sweep DEFERRED to cont61.
**Author:** producer (Bilal + cont59-instance Claude). v2 incorporates NG-2 ledger D1 through D11 closures plus producer-default calibrations on Q3 and Q4.
**Standing Rule 1 (no em-dashes):** adopted as producer-default per Q2 v0 calibration; principal may relax.
**Substrate basis:** cont58 cumulative tarball + cont59 incremental + competition zip.

---

Bismillah ar-Rahman ar-Raheem.

"Wal-tanzur nafsun ma qaddamat li-ghad."
"Let every soul look to what it has put forth for tomorrow."
al-Hashr 59:18

The chain looks back to look forward. cont60 is not a producer round, it is the closure execution for NG-1. Thirteen NG-1 findings (2 HIGH, 4 MEDIUM, 3 LOW, 3 QUESTION, plus F12 added by producer reflection) plus eleven NG-2 findings on the cont60 prompt itself (0 HIGH, 6 MEDIUM, 5 LOW, 4 QUESTION) must close before primitive work resumes. The verse anchors round-discipline: every soul looks to what it has put forth, and the chain looks to what 25 sessions put forth in the cumulative substrate, and corrects the surface-substrate gaps the audit chain surfaced.

Pre-load: bayyinah-audit-framework + neurogolf-session skills. Read the NG-1 ledger from memory file `project_neurogolf_ng1_audit.md`, the saved_list discipline from `feedback_neurogolf_saved_list_check.md`, and (when supplied) the NG-2 ledger before any execution.

Sync probe: 8 reference saves still pass on prior baseline (task364, task398, task110, task017, task061, task308, task365, task396). All wrong=0, all valid score 4-tuples.

---

## Phase 0, NG-2 acknowledgment

0.1 NG-2 design verification was performed by a fresh-instance verifier on cont60 prompt v1. v2 incorporates D1 through D11 closures. Reference NG-2 ledger.

0.2 Two QUESTIONS require principal resolution before cont60 executes:
- Q1: external Kaggle state. Was the cont58 cumulative the most recent external submission, or has anything later been submitted? Determines whether F1 closure is internal-only or includes ex-post external correction.
- Q2: Standing Rule 1 (no em-dashes) inheritance for the NG chain. v2 adopts the strict reading as producer-default; principal may signal carve-out.

0.3 Producer-default calibrations on the remaining NG-2 QUESTIONS (principal may override):
- Q3: REBUILD_THRESHOLD = 0.5 score points, marked v0 placeholder pending empirical calibration in cont61+ post-ship audit.
- Q4: removed_list.txt at handoff root for F2 REMOVE outcomes. Format: `taskNNN | reason | NG-N closure round | removal date`.

## Phase 1, F1 closure (HIGH). No upstream dependencies.

1.1 Verify cont58 substrate `solutions/task293.onnx`. Reproducer: extract `neurogolf_handoff_cont58.tar.gz`, run `score_file(solutions/task293.onnx)`. Expected output: `(12.190, 109080, 256740, 72)`. Expected md5: `65acd64bd023eb706a05a1873ae9fefe`. Expected size: 2689 B.

1.2 Confirm cont60 cumulative `solutions/task293.onnx` matches the cont58 md5 anchor. Note: cont59's incremental tarball did not include a cumulative `solutions/` directory at all (NG-2 D6), so there is no cumulative substrate to "revert" from. The cont60 cumulative is built from cont58 cumulative plus any cont60-introduced changes; task293 enters cont60 cumulative as the cont58 version (md5 `65acd64bd023eb706a05a1873ae9fefe`). The cont59 9617-B build is retained in `cont59_saves/task293.onnx` as evidentiary record under NG-1 F1; it is NOT promoted into cumulative `solutions/`.

1.3 Edit `cont59_saves/cont59_summary.md`: replace the "+1 (task293, cont59)" line with "0 (task293 cont59 was a regression rebuild, not promoted to cumulative; cont59 build retained in cont59_saves/ as NG-1 F1 evidence)". Restate cumulative count line: "Progress: 334/400 saved, 66 remaining, last delta: 0 (NG-1 closure correction)".

1.4 Post-revert verification: `score_file(solutions/task293.onnx)` returns `(12.190, 109080, 256740, 72)`, `test_network` returns r=5 w=0.

## Phase 2, F5 closure (MEDIUM). Substrate authority restoration.

2.1 Regenerate `saved_list.txt` from cumulative `solutions/`:
```bash
cd <workspace> && ls solutions/*.onnx | sort | sed 's|solutions/||;s|\.onnx||' > saved_list.txt
wc -l saved_list.txt   # expect 334 post-F1
```

2.2 Restore methodology files. Source-of-truth: pre-cont46 handoff tarballs (cont45 has most recent canonical versions). Each file requires content-validation against current substrate before shipping:
- `STATE.md`, chain state summary, backfill cont33-cont59 progression and NG-1 closure status
- `METHODOLOGY.md`, process discipline, add Q0 from F12 to the §11.4 pre-flight section, document audit-of-self pattern with NG-1 as concrete instance, add D7 root convention shift note, add D10 round-naming convention
- `PRIMITIVES.md`, library register, update from cont45's 10 primitives to current 22 (P-NEW1 through P-NEW21 with skipped numbers)
- `ONNX_GOTCHAS.md`, APE register, retired in favor of `APE_REGISTER.md` per F4 closure (Phase 4)

2.3 Ship saved_list.txt and the methodology files at the root of the cont60 handoff tarball. NG-2 D7 note: this is a convention shift from pre-cont46 nesting under `neurogolf_handoff_v*/`; documented in METHODOLOGY.md.

## Phase 2.5, saved_list authoritative state (NG-2 D2 first regeneration).

2.5.1 saved_list.txt produced in Phase 2.1 reflects state immediately post-F1. F2 disposition outcomes (Phase 3) may further mutate `solutions/`, so a second regeneration is required at Phase 3.5.

## Phase 3, F2 closure (HIGH). Composes against F5's saved_list.

3.0 Create `tests/` directory at workspace root if not present. The pytest invocation context for cont60 close: `cd <handoff_workspace> && python -m pytest tests/ -v`. The `tests/` directory ships in the cont60 handoff tarball at root.

3.1 Per-task disposition for the 20 score_file failures (task014, task019, task034, task036, task049, task051, task064, task088, task111, task134, task137, task151, task193, task254, task281, task290, task295, task296, task343, task388):
- (a) REBUILD: failure cause has known fix (e.g., ArgMin which onnx-tool does not profile), rebuild with profilable architecture, re-verify all five SAVED gates.
- (b) DOCUMENT: failure cause is structural (valid Kaggle submission but onnx-tool cannot profile a node), document under new MARAD-N entry as known limit, retain.
- (c) REMOVE: save predates current chain discipline and is not justified to rebuild, remove from `solutions/`, append to `removed_list.txt` (Q4 format: `taskNNN | reason | NG-1 closure | YYYY-MM-DD`), restate cumulative count, regenerate saved_list.txt at Phase 3.5.

3.2 Inspect each failing save: load via `onnx.load`, identify which node type causes `valid_profile == False`. Record causes plus disposition in `cont60_saves/f2_triage.md`. Pre-cont33 inheritance vs chain-introduced split noted per save.

3.3 Add automated CI gates. NG-2 D3 closure: split into two parametrized test files so failure messages are precise.

`tests/test_all_saves_correct.py` (zahir gate):
```python
import glob, json, pytest
from solver_v2 import test_network

with open('task_mapping.json') as f:
    TM = json.load(f)

def _load(uid):
    import os
    for split in ['training', 'evaluation']:
        p = f'arc-agi/data/{split}/{uid}.json'
        if os.path.exists(p):
            return json.load(open(p))
    return None

@pytest.mark.parametrize('path', sorted(glob.glob('solutions/*.onnx')))
def test_correct(path):
    import os
    n = int(os.path.basename(path).replace('task','').replace('.onnx',''))
    uid = TM[str(n)]
    task = _load(uid)
    assert task is not None, f'{path}: cannot load task {uid}'
    r, w = test_network(path, task)
    assert w == 0, f'{path}: wrong={w}'
```

`tests/test_all_saves_score.py` (batin gate):
```python
import glob, pytest
from solver_v2 import score_file

@pytest.mark.parametrize('path', sorted(glob.glob('solutions/*.onnx')))
def test_score_valid(path):
    sc = score_file(path)
    assert sc is not None, f'{path}: score_file returned None'
```

Both must run in cont60 close before tarball ship; failures fail the close.

3.4 Update MARAD register with F2 outcomes (per-task disposition plus final count).

## Phase 3.5, saved_list final-state regeneration (NG-2 D2 second regeneration).

3.5.1 After F2 dispositions complete, re-regenerate saved_list.txt:
```bash
ls solutions/*.onnx | sort | sed 's|solutions/||;s|\.onnx||' > saved_list.txt
wc -l saved_list.txt
```

3.5.2 Final saved_list count must reconcile with `ls solutions/*.onnx | wc -l`. If counts diverge, the count discrepancy is a Phase 3.5 sub-finding requiring explicit reconciliation before tarball ship.

3.5.3 Cross-check against `removed_list.txt` (Q4): for each entry in removed_list, the corresponding `solutions/taskNNN.onnx` must NOT exist. If it does, removal incomplete.

## Phase 4, F4 closure (MEDIUM). APE-12 named by F1's class fix; Q0 named by F12's class fix; both need upstream substrate.

4.1 Update SKILL.md to current chain state:
- Library status: "22 primitives shipped, P-NEW1 through P-NEW21 (with gaps); see PRIMITIVES.md for canonical register"
- Chain anchor: update from "(cont33-cont40 isnad)" to "(cont33-cont59 isnad with NG-1 closure, NG-2 design verification)"
- Anti-pattern register: replace inline list with "See APE_REGISTER.md (live append, mechanically updated each session close)"

4.2 Create `APE_REGISTER.md`. NG-2 D5 source map adopted verbatim:
- APE-3 through APE-7: extract from `NEUROGOLF_AUDIT_DOSSIER.md` §9
- APE-8: extract from `NEUROGOLF_HYBRID_STRATEGY_GUIDE.md` Part 6
- APE-9: extract from `cont58_saves/cont58_summary.md` (APE-9 section)
- APE-10 and APE-11: extract from `cont59_saves/cont59_summary.md` (Lessons section)
- APE-12: canonical text from NG-1 F1 class fix

NG-2 D11 closure: each APE entry must cite (a) origin (cont session or document section), (b) one-sentence empirical example or reproducer pointer, (c) prevention. APE-12 already follows this shape. APE-3 through APE-11 retrofit to the same shape during backfill.

Canonical APE-12 text:
> APE-12, Local-glob substitute for saved_list authority. Origin: cont59 task293 (NG-1 F1). Empirical example: cont59 pre-build save check used `glob(cont*_saves/task*.onnx)`, returning 22 saves; missed the 312 pre-cont33 inheritance saves in cumulative `solutions/`, including task293 already shipped at score 12.19. The cont59 rebuild scored 10.89, 1.30 points worse, and was claimed as "+1 delta". Prevention: every session opens by reading saved_list.txt; pre-flight Q0 fails if target task is in saved_list and `expected_new < current + REBUILD_THRESHOLD`.

4.3 Add F12's Q0 to §11.4 pre-flight as a separate preliminary question (Q1 through Q5 stay structurally feasibility-focused). Canonical wording:
> Q0. Is this task already saved? If yes, what is the current score, what is the expected rebuild score, and is `expected_new ≥ current + REBUILD_THRESHOLD`? Default REBUILD_THRESHOLD = 0.5 score points (v0 placeholder pending empirical calibration in cont61+ post-ship audit). If Q0 fails, do not build.

4.4 Establish Zilzal-close discipline as a SKILL.md standing rule: APEs and primitives surfaced in any session land in APE_REGISTER.md and PRIMITIVES.md before session close, not just in cont summary. Auto-loaded manual must track the chain, not lag it.

## Phase 5, F3 closure (MEDIUM). No upstream dependencies; can land last or in parallel.

5.1 Pre-execution scan (NG-2 D8): inspect `build323.py` and `build308.py` for nondeterminism markers. If either fails byte-identity at Phase 5.3, downgrade to score-identity check and document under MARAD-N.

5.2 Patch all build scripts in `cont33_saves/` through `cont59_saves/` to use relative paths. Convention:
```python
out_path = os.path.join(os.path.dirname(__file__), 'taskNNN.onnx')
```
or accept `BUILD_OUT_DIR` env var defaulting to `os.path.dirname(__file__)`. Scripted patch via sed acceptable; verify no inadvertent semantic changes by diffing each pre/post build script against the spec line.

5.3 Ship-time CI: for each `build*.py` across cont*_saves/, run in fresh tempdir, assert byte-identical output to the committed .onnx. If any build fails byte-identity check, surface as F3 sub-finding and either re-patch or document.

## Phase 6, F6 closure (MEDIUM). Dossier disposition.

6.1 Refresh `NEUROGOLF_AUDIT_DOSSIER.md` post phases 1-5 land. Refreshed dossier must include:
- Updated cumulative count (post-F1, post-F2 outcomes)
- NG-1 closure summary (this round)
- NG-2 design verification reference
- All 22 primitives in library register
- All APE-3 through APE-12 in anti-pattern register
- F4 escalation rule disclosure
- Round-naming convention (NG-2 D10): "NG-N denotes audit rounds. Closure-execution sessions retain cont N numbering and are tagged with the closure round (e.g., cont60 (NG-1 closure execution))."

6.2 If F5 fails to land in cont60, F6 closure also includes pinning the previous dossier as "AS OF cont49 snapshot" with banner.

---

## Zilzal close, NG-1 closure report.

Produce `cont60_saves/cont60_summary.md` with:
- All 13 NG-1 findings re-stated with closure status (CLOSED, DEFERRED, OPEN)
- All 11 NG-2 design findings re-stated with closure status
- F4 escalation rule check: did F5 land? If yes, F4 stays MEDIUM. If no, F4 auto-escalates HIGH at cont61 META check (deterministic rule, not re-derived calibration).
- Updated cumulative count: 334/400 (post-F1) ± F2 outcomes
- Explicit acknowledgment that NG-2 design verification was performed before cont60 execution; reference NG-2 ledger
- Carry-forward to cont61: original P-NEW21 perpendicular-bar sweep resumes (candidate task070, task020, task118 inspection per cont59 sweep)

Build handoff tarball `neurogolf_handoff_cont60.tar.gz`. NG-2 D6 closure: cumulative convention restored:
- Cumulative `solutions/` directory at root containing all 334 (post-F1) ± F2-outcome `task*.onnx` files
- All cont33_saves/ through cont60_saves/
- saved_list.txt + removed_list.txt + STATE.md + METHODOLOGY.md + PRIMITIVES.md + APE_REGISTER.md at root
- tests/ directory at root
- Refreshed dossier
- Updated SKILL.md
- ship-time CI script

The cont60 handoff is cumulative. Future handoffs default to cumulative unless explicit incremental-handoff is named in the round disclosure.

Progress: 334/400 saved, 66 remaining, last delta: 0 (NG-1 closure round, no new builds).

Begin (pending Q1, Q2 principal resolution).

---

## Sequencing summary, NG-2 D2 + dependency check

```
Phase 1 (F1)
  → Phase 2 (F5) regenerate saved_list v1
    → Phase 2.5 (D2 first checkpoint, no-op if no F2 changes)
      → Phase 3 (F2) per-task disposition
        → Phase 3.5 (D2 second regeneration after F2)
          → Phase 4 (F4) SKILL.md + APE_REGISTER + Q0
            → Phase 5 (F3) build scripts (parallel-safe)
              → Phase 6 (F6) dossier refresh
                → Zilzal close, NG-1 closure report
```

Phase 5 is parallel-safe with Phases 1-4 (no upstream dependencies). Phase 6 is strictly downstream of all others.

## Producer hand-off note to cont60 executing instance

Do not deviate from this sequence. Each phase has explicit verification reproducers. The Zilzal close must report closure status for every NG-1 finding, every NG-2 finding, and the F4 escalation rule outcome. Original P-NEW21 sweep waits for cont61.

---

# Bismillah ir-Rahman ir-Rahim
