# Bismillah ir-Rahman ir-Rahim

# R0548 -- F2 triage, the 20 score_file failures

**Chronological Index:** 818 of 995  
**Date:** Undated  
**Section:** VIII. NeuroGolf (ARC-AGI / ONNX)  
**Source File:** f2_triage.md  
**Source Format:** md  
**SHA-256:** `782f124cc7d9977fcbaa744c469a9dc8db8368bde599b1846ce71972d17f3d2a`  

---

## R0548 · F2 triage, the 20 score_file failures

- section: VIII. NeuroGolf (ARC-AGI / ONNX)
- source_file: f2_triage.md
- source_format: md
- text_sha256: 782f124cc7d9977fcbaa744c469a9dc8db8368bde599b1846ce71972d17f3d2a

# F2 triage, the 20 score_file failures

NG-1 F2 closure. Per-task disposition for every save in cumulative `solutions/`
that returns None from `solver_v2.score_file`.

## Root cause (uniform across all 20)

Every failing save uses ArgMin and/or ArgMax. Per ONNX_GOTCHAS.md (pre-cont33
register): ArgMin / ArgMax are NOT registered in the onnx_tool profiler, so
local score_file returns None. Kaggle's profiler accepts these ops, so the
saves are structurally valid Kaggle submissions and should NOT be removed.

This was previously documented in ONNX_GOTCHAS.md but was never escalated to
a MARAD entry, which is why F2 was a silent surface. Cont60 closure escalates
to MARAD-10.

## Per-task disposition

All 20 are classified as (b) DOCUMENT, retained in `solutions/`, registered
under MARAD-10.

Pre-cont33 inheritance vs chain-introduced split: all 20 are pre-cont33
inheritance saves (none originate from cont33-cont59 sessions; verified by
their absence from any cont*_saves/ directory).

| Task    | Size (B) | Ops flagged | Disposition |
|---------|----------|-------------|-------------|
| task014 | 39641    | ArgMin                | DOCUMENT under MARAD-10 |
| task019 | 4851     | ArgMax, ArgMin        | DOCUMENT under MARAD-10 |
| task034 | 39663    | ArgMin                | DOCUMENT under MARAD-10 |
| task036 | 39916    | ArgMax, ArgMin        | DOCUMENT under MARAD-10 |
| task049 | 39915    | ArgMax, ArgMin        | DOCUMENT under MARAD-10 |
| task051 | 3444     | ArgMax, ArgMin        | DOCUMENT under MARAD-10 |
| task064 | 4868     | ArgMax, ArgMin        | DOCUMENT under MARAD-10 |
| task088 | 4727     | ArgMax, ArgMin        | DOCUMENT under MARAD-10 |
| task111 | 69355    | ArgMax, ArgMin        | DOCUMENT under MARAD-10 |
| task134 | 5276     | ArgMax, ArgMin        | DOCUMENT under MARAD-10 |
| task137 | 3431     | ArgMin                | DOCUMENT under MARAD-10 |
| task151 | 8517     | ArgMin                | DOCUMENT under MARAD-10 |
| task193 | 2054     | ArgMin                | DOCUMENT under MARAD-10 |
| task254 | 2419     | ArgMax, ArgMin        | DOCUMENT under MARAD-10 |
| task281 | 4218     | ArgMax, ArgMin        | DOCUMENT under MARAD-10 |
| task290 | 45013    | ArgMax, ArgMin        | DOCUMENT under MARAD-10 |
| task295 | 1840     | ArgMin                | DOCUMENT under MARAD-10 |
| task296 | 2449     | ArgMin                | DOCUMENT under MARAD-10 |
| task343 | 15872    | ArgMax, ArgMin        | DOCUMENT under MARAD-10 |
| task388 | 3476     | ArgMax, ArgMin        | DOCUMENT under MARAD-10 |

## MARAD-10 entry (new)

**Severity:** MEDIUM
**Origin:** NG-1 F2 closure, cont60
**Description:** 20 cumulative saves use ArgMin and/or ArgMax operations. The
local solver_v2.score_file function relies on onnx_tool.profile, which has no
profiler registered for ArgMin/ArgMax and returns valid_profile=False. The
saves are structurally valid Kaggle submissions (ArgMin/ArgMax are standard
opset 10 ops); the failure is local-only.

**Reproducer:** `python3 -c "import sys; sys.path.insert(0,'.'); from solver_v2 import score_file; print(score_file('solutions/task014.onnx'))"` returns None.

**Impact:** zero on Kaggle scoring. The local score_file gate is a false
negative for these saves. They pass test_network with Wrong=0 and would
score correctly on Kaggle.

**Minimal fix:** none required. The saves ship as-is.

**Long-term remediation (optional, deferred to post-cont60):** rebuild each
of these saves using the argmax-without-ArgMax pattern in PRIMITIVES.md
(P-140, P-141). This would unify local and Kaggle profilers but is high-effort
for low value (the saves are already shipping correctly).

## CI gate handling (test_all_saves_score.py)

The gate must ACCEPT these 20 as known-MARAD-10 cases. Implementation: skip
the assertion for any save in the MARAD-10 allowlist, OR run a softer assert
that the save uses ArgMin/ArgMax if score_file returns None. The latter is
preferred because it self-documents: any NEW score_file failure that does NOT
use ArgMin/ArgMax is a real bug.

See `tests/test_all_saves_score.py` for the implementation.

## Closure verification

Post-F2 expectations:
- `solutions/` count: 334 (no removals)
- saved_list.txt count: 334
- removed_list.txt: empty (no removals)
- pytest tests/test_all_saves_score.py: passes (with MARAD-10 carve-out)
- pytest tests/test_all_saves_correct.py: passes (all 334 already at Wrong=0)

---

# Bismillah ir-Rahman ir-Rahim
