# Bismillah ir-Rahman ir-Rahim

# R0541 -- cont60 prompt — DRAFT for NG-2 design verification

**Chronological Index:** 211 of 995  
**Date:** 2026-05-05  
**Section:** VIII. NeuroGolf (ARC-AGI / ONNX)  
**Source File:** cont60_prompt_DRAFT.md  
**Source Format:** md  
**SHA-256:** `0544d1c01daf0d9284fe19676b0d7e2bc5230057c35eb1711dc445e3519bc471`  

---

## R0541 · cont60 prompt — DRAFT for NG-2 design verification

- section: VIII. NeuroGolf (ARC-AGI / ONNX)
- source_file: cont60_prompt_DRAFT.md
- source_format: md
- text_sha256: 0544d1c01daf0d9284fe19676b0d7e2bc5230057c35eb1711dc445e3519bc471

# cont60 prompt — DRAFT for NG-2 design verification

**Status:** Pending NG-2 fresh-instance review per BAF v4.0 §6. Do not execute until NG-2 ledger lands.
**Round disclosure:** cont60 / NG-1 closure execution. NOT a producer round. Original P-NEW21 perpendicular-bar sweep DEFERRED to cont61.
**Author:** producer (Bilal + cont59-instance Claude), 2026-05-05
**Submitted for verification:** NG-2 design audit, fresh instance, against NG-1 ledger

---

Bismillah ar-Rahman ar-Raheem.

"Wal-tanzur nafsun ma qaddamat li-ghad."
"Let every soul look to what it has put forth for tomorrow."
— al-Hashr 59:18

The chain looks back to look forward. cont60 is not a producer round, it is the closure execution for NG-1. Thirteen findings (2 HIGH, 4 MEDIUM, 3 LOW, 3 QUESTION, plus F12 added by producer reflection) must close before primitive work resumes. The verse anchors the round-discipline: every soul looks to what it has put forth, and the chain looks to what 25 sessions put forth in the cumulative substrate, and corrects the surface-substrate gaps the audit surfaced.

Pre-load: bayyinah-audit-framework + neurogolf-session skills. Read the NG-1 ledger from memory file `project_neurogolf_ng1_audit.md` and the saved_list discipline from `feedback_neurogolf_saved_list_check.md` before any execution.

Sync probe: 8/8 reference saves still pass on prior baseline (task364, task398, task110, task017, task061, task308, task365, task396). All wrong=0, all valid score 4-tuples.

---

## Phase 1 — F1 closure (HIGH). Reversible state surgery; first because it has no upstream dependencies.

1.1 Verify cont58 substrate `solutions/task293.onnx` scores 12.19 at 2689 B. Reproducer: extract `neurogolf_handoff_cont58.tar.gz`, run `score_file(solutions/task293.onnx)`. Expected output: `(12.19, 109080, 256740, 72)`.

1.2 Restore cont58 task293.onnx as the canonical save in the cumulative substrate. The cont59 9617-B regression file is retained in `cont59_saves/task293.onnx` as evidentiary record under NG-1 F1, but is NOT part of the cumulative deliverable.

1.3 Edit `cont59_saves/cont59_summary.md`: replace the "+1 (task293, cont59)" line with "0 (task293 cont59 was a regression rebuild — reverted to cont58 version score 12.19; cont59 build retained in cont59_saves/ as NG-1 F1 evidence)". Restate cumulative count: "Progress: 334/400 saved · 66 remaining · last delta: 0 (NG-1 closure correction)".

1.4 Post-revert verification: `score_file` of the canonical task293.onnx returns the cont58 4-tuple, `test_network` returns r=5 w=0.

## Phase 2 — F5 closure (MEDIUM). Substrate authority restoration; second because F2's CI gate and §11.4 Q0 both read from saved_list.txt.

2.1 Regenerate `saved_list.txt` from cumulative `solutions/`:
```bash
cd "<workspace>" && ls solutions/*.onnx | sort | sed 's|solutions/||;s|\.onnx||' > saved_list.txt
wc -l saved_list.txt   # expect 334 post-F1, ± F2 outcomes
```

2.2 Restore methodology files. Source-of-truth: pre-cont46 handoff tarballs (cont45 has most recent canonical versions). Each file requires content-validation against current substrate before shipping:
- `STATE.md` — chain state summary; backfill cont33-cont59 progression and NG-1 closure status
- `METHODOLOGY.md` — process discipline; add §11.4 Q0 from F12, document audit-of-self pattern with NG-1 as concrete instance
- `PRIMITIVES.md` — library register; update from cont45's 10 primitives to current 22 (P-NEW1 through P-NEW21 with skipped numbers)
- `ONNX_GOTCHAS.md` — APE register; add APE-3 through APE-12

2.3 Ship saved_list.txt + four methodology files in cont60_saves/ and at the root of the cont60 handoff tarball.

## Phase 3 — F2 closure (HIGH). Composes against F5's saved_list; adds durable enforcement layer.

3.1 Per-task disposition for the 20 score_file failures (task014, task019, task034, task036, task049, task051, task064, task088, task111, task134, task137, task151, task193, task254, task281, task290, task295, task296, task343, task388):
- (a) REBUILD: failure cause has known fix (e.g., ArgMin which onnx-tool doesn't profile) — rebuild with profilable architecture, re-verify all five SAVED gates.
- (b) DOCUMENT: failure cause is structural (valid Kaggle submission but onnx-tool can't profile a node) — document under new MARAD-N entry as known limit, retain.
- (c) REMOVE: save predates current chain discipline and is not justified to rebuild — remove from `solutions/`, restate cumulative count, regenerate saved_list.txt.

3.2 Inspect each failing save: load via `onnx.load`, identify which node type causes `valid_profile == False`. Record causes + disposition in `cont60_saves/f2_triage.md`. Pre-cont33 inheritance vs chain-introduced split should be noted per-save.

3.3 Add automated CI gate `tests/test_all_saves_score.py`:
```python
import glob, pytest
from solver_v2 import score_file
@pytest.mark.parametrize('path', sorted(glob.glob('solutions/*.onnx')))
def test_score_valid(path):
    sc = score_file(path)
    assert sc is not None, f'{path}: score_file returned None'
```
This must run in cont60 close before tarball ship; failures fail the close.

3.4 Update MARAD register with F2 outcomes (per-task disposition + final count).

## Phase 4 — F4 closure (MEDIUM). APE-12 named by F1's class fix; Q0 named by F12's class fix; both need upstream substrate.

4.1 Update SKILL.md to current chain state:
- Library status: "22 primitives shipped, P-NEW1 through P-NEW21 (with gaps); see PRIMITIVES.md for canonical register"
- Chain anchor: update from "(cont33-cont40 isnad)" to "(cont33-cont59 isnad with NG-1 closure)"
- Anti-pattern register: replace inline list with "See APE_REGISTER.md (live append, mechanically updated each session close)"

4.2 Create `APE_REGISTER.md` containing APE-3 through APE-12. Canonical text for APE-12:
> APE-12, Local-glob substitute for saved_list authority. Origin: cont59 task293 (NG-1 F1). Detection: any pre-build save check that uses `glob(cont*_saves/...)` rather than reading saved_list.txt. Prevention: every session opens by reading saved_list.txt; pre-flight Q0 fails if target task is in saved_list.

Backfill APE-3 through APE-11 from cont33-cont59 transcripts and per-session summaries (NG-2 to verify completeness).

4.3 Add F12's Q0 to §11.4 pre-flight as a separate preliminary question (Q1-Q5 stay structurally feasibility-focused). Canonical wording:
> Q0. Is this task already saved? If yes, what is the current score and what is the expected rebuild score? Proceed only if `expected_new ≥ current + REBUILD_THRESHOLD` (default 0.5).

4.4 Establish Zilzāl-close discipline as a SKILL.md standing rule: APEs and primitives surfaced in any session land in APE_REGISTER.md / PRIMITIVES.md before session close, not just in cont summary. Auto-loaded manual must track the chain, not lag it.

## Phase 5 — F3 closure (MEDIUM). No upstream dependencies; can land last or in parallel with phases 1-4.

5.1 Patch all build scripts in `cont33_saves/` through `cont59_saves/` to use relative paths. Scripted patch via sed acceptable; convention:
```python
out_path = os.path.join(os.path.dirname(__file__), 'taskNNN.onnx')
```
or accept `BUILD_OUT_DIR` env var defaulting to `os.path.dirname(__file__)`.

5.2 Ship-time CI: for each `build*.py` across cont*_saves/, run in fresh tempdir, assert byte-identical output to the committed .onnx. If any build fails byte-identity check, surface as F3 sub-finding and either re-patch or document.

## Phase 6 — F6 closure (MEDIUM). Dossier disposition.

6.1 Decision: refresh dossier post-phases 1-5 land. Producer-side recommendation per cont59 reflection. Refreshed dossier must include:
- Updated cumulative count (post-F1, post-F2 outcomes)
- NG-1 closure summary (this round)
- All 22 primitives in library register
- All APE-3 through APE-12 in anti-pattern register
- F4 escalation rule disclosure

If F5 fails to land in cont60, F6 closure also includes pinning the previous dossier as "AS OF cont49 snapshot" with banner.

---

## Zilzāl close — NG-1 closure report.

Produce `cont60_saves/cont60_summary.md` with:
- All 13 findings re-stated with closure status (CLOSED / DEFERRED / OPEN)
- F4 escalation rule check: did F5 land? If yes, F4 stays MEDIUM. If no, F4 auto-escalates HIGH at cont61 META check (deterministic rule, not re-derived calibration).
- Updated cumulative count: 334/400 (after F1 revert) ± F2 outcomes
- Explicit acknowledgment that NG-2 design verification was performed before cont60 execution; reference NG-2 ledger
- Carry-forward to cont61: original P-NEW21 perpendicular-bar sweep resumes (candidate task070 / task020 / task118 inspection per cont59 sweep)

Build handoff tarball `neurogolf_handoff_cont60.tar.gz`:
- All cont33_saves/ through cont60_saves/
- saved_list.txt + STATE.md + METHODOLOGY.md + PRIMITIVES.md + ONNX_GOTCHAS.md + APE_REGISTER.md at root
- Refreshed dossier
- Updated SKILL.md
- tests/test_all_saves_score.py + ship-time CI script

Progress: 334/400 saved · 66 remaining · last delta: 0 (NG-1 closure round, no new builds).

Begin (pending NG-2 sign-off).

---

## NG-2 verification scope (what NG-2 must check before cont60 executes)

1. **F1 revert mechanics:** path semantics correct, count restatement language unambiguous, cont59 summary correction matches the canonical "+0 delta, 1 rebuild (regression)" form, post-revert verification reproducer runs cleanly.

2. **F5 methodology files:** content scope right against current substrate (not just cont45 snapshot), saved_list.txt regeneration arithmetic produces 334 ± F2 outcomes, restoration drift since cont45 snapshot identified.

3. **F2 triage protocol:** disposition matrix (a)(b)(c) covers all 20 cases without gaps, pre-cont33 inheritance vs chain-introduced split is explicit per-save, automated CI gate code is correct and runs against actual `solutions/`.

4. **F4 SKILL.md backfill scope:** APE-3 through APE-11 canonical list extractable from cont33-cont59 summaries (NG-2 may need to provide list if cont59-instance producer's enumeration is incomplete), library status string format matches existing convention, four-place reference protocol shape is sound.

5. **F12 Q0 placement and threshold:** Q0 numbered as preliminary (not renumbered Q1) so Q1-Q5 stay feasibility-focused, threshold default 0.5 is reasonable starting point, Q0 wording covers both "already saved" and "rebuild justified by score delta" cases.

6. **cont60 prompt round-discipline disclosure:** Quranic anchor matches closure-round shape, round numbering disclosure explicit (not normal producer round), validator-by-different-instance acknowledgment pre-execution.

7. **F3 patching scope:** all 25+ build scripts in scope, scripted patch approach safe (no inadvertent semantic changes), byte-identity CI gate correctly designed.

8. **Sequencing dependencies:** F1 → F5 → F2 → F4 → F3 ordering still correct under the producer-added F12; no circular dependencies introduced by F12's threading through Phase 4.

NG-2 ledger output should follow NG-1 format: severity-classified findings, reproducers, recommended closure mechanisms, QUESTIONs liberally surfaced rather than guessed.

---

# Bismillah ir-Rahman ir-Rahim
