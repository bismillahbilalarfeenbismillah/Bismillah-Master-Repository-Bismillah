# Bismillah ir-Rahman ir-Rahim

# R0611 -- NEUROGOLF AUDIT DOSSIER, refresh post cont60 (NG-1 closure execution)

**Chronological Index:** 206 of 995  
**Date:** 2026-05-04  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** DOSSIER_REFRESH.md  
**Source Format:** md  
**SHA-256:** `4ded6046f8edfa9276ef747d7c21ead5c709a5786a6e13ac19f346caeafcacd8`  

---

## R0611 · NEUROGOLF AUDIT DOSSIER, refresh post cont60 (NG-1 closure execution)

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: DOSSIER_REFRESH.md
- source_format: md
- text_sha256: 4ded6046f8edfa9276ef747d7c21ead5c709a5786a6e13ac19f346caeafcacd8

# NEUROGOLF AUDIT DOSSIER, refresh post cont60 (NG-1 closure execution)

This file is the cont60 refresh delta. The original NEUROGOLF_AUDIT_DOSSIER.md
is anchored at cont49 (May 4, 2026) and 325 saves. Per NG-2 D6 closure
recommendation, cont60 ships this delta document; the principal may merge into
the canonical dossier post-cont60 or pin the original as "AS OF cont49 snapshot."

---

## Refresh anchor

**Date:** May 5, 2026
**Saved:** 334 / 400 (post NG-1 F1 correction; pre any cont61+ delta)
**Pending:** 66
**Compliance state:** COMPLIANT (NG-1 closure execution complete, NG-2 design
verified before execution)

## NG-1 closure summary

Thirteen findings (2 HIGH, 4 MEDIUM, 3 LOW, 3 QUESTION, plus F12 added by
producer reflection) were closed in cont60. Plus eleven NG-2 design findings
on the cont60 prompt itself (0 HIGH, 6 MEDIUM, 5 LOW, 4 QUESTION) closed
pre-execution. See `cont60_summary.md` for per-finding closure status.

Highlight: F1 (HIGH, task293 silent rebuild claimed as +1 delta) closed by
restoring cont58 cumulative anchor (md5 65acd64bd023eb706a05a1873ae9fefe,
score 12.19). Cumulative count restated 335 -> 334.

## NG-2 design verification reference

NG-2 was a fresh-instance audit on the cont60 prompt v1 before execution.
Validator-by-different-instance (BAF v4.0 §6) materially honored.

## Library register

22 primitives shipped, P-NEW1 through P-NEW21 (with gaps). See `PRIMITIVES.md`
at handoff root for canonical register. Recent additions documented in
APE_REGISTER.md include:
- P-NEW17.5 / 17.7 / 17.8: shared-substrate CC variants
- P-NEW20: periodic-fill primitive (3-task family)
- P-NEW21: bbox-intersect-swap primitive (cont59, NG-1 F1 substrate)

## Anti-pattern register

APE-3 through APE-12 documented in `APE_REGISTER.md` at handoff root. Each
entry follows BAF v4.0 §10 documentation discipline (origin, empirical
example, prevention). APE-12 specifically prevents the F1 failure mode via
§11.4 Q0 pre-flight check against saved_list.txt.

## F4 escalation rule disclosure

If cont60 closes without F5 landing, F4 escalates HIGH at cont61 META check.
This is a deterministic rule, not a re-derived calibration.

**As of cont60 close:** F5 landed (saved_list.txt + STATE.md + METHODOLOGY.md
+ PRIMITIVES.md + APE_REGISTER.md ship at handoff root). F4 stays MEDIUM.

## Round-naming convention (NG-2 D10)

The NeuroGolf chain runs two parallel numbering systems:
- **Producer chain:** cont33, cont34, ..., cont59, cont60. Each is one work
  session; producer sessions write code.
- **Audit chain:** NG-1, NG-2, NG-3, ... Each is one fresh-instance audit;
  audits produce ledgers.

Closure-execution sessions retain cont N numbering and are tagged with the
closure round. Example: cont60 is "cont60 (NG-1 closure execution)". The
post-ship audit of cont60 will be NG-3.

## MARAD register additions (cont60)

**MARAD-10 (MEDIUM):** 20 cumulative saves use ArgMin/ArgMax which onnx_tool
cannot profile. Local score_file returns None for these but the saves are
valid Kaggle submissions. No fix required; documented in `cont60_saves/f2_triage.md`.

## CI gates added (cont60)

`tests/test_all_saves_correct.py` (zahir gate): every save must pass
test_network with Wrong=0.

`tests/test_all_saves_score.py` (batin gate): every save must return valid
score 4-tuple, except MARAD-10 allowlist (skip). New score_file None outside
allowlist fails the test.

Both gates run as part of the cont60 close before tarball ship.

## Convention shifts in effect from cont60

- **Methodology files at handoff root** (NG-2 D7): STATE.md, METHODOLOGY.md,
  PRIMITIVES.md, APE_REGISTER.md, saved_list.txt, removed_list.txt all ship
  at handoff tarball root. Pre-cont46 nested under neurogolf_handoff_v*/;
  cont46-cont59 dropped them; cont60 restores at root.
- **Cumulative handoffs by default** (NG-2 D6): handoff tarballs include
  full cumulative `solutions/` directory unless explicit incremental-handoff
  named in round disclosure. cont59 broke this; cont60 restores.
- **Standing Rule 1 inheritance** (NG-2 Q2): NG chain documentation does not
  use em-dashes (producer-default; principal may relax).

## Pending priorities for cont61

1. P-NEW21 perpendicular-bar sweep across pending tasks (carry-forward from cont59).
2. task070 (32597951), task020 (11852cab), task118 (50846271) inspection from
   cont59 sweep.
3. cont61 is also NG-3 (post-ship audit on cont60 NG-1 closure rollout).

## Post-cont60 dossier disposition (NG-2 D6)

Producer recommendation: refresh the canonical NEUROGOLF_AUDIT_DOSSIER.md by
merging this delta. Alternative: pin the original as "AS OF cont49 snapshot"
with a banner. Principal call.

---

# Bismillah ir-Rahman ir-Rahim
