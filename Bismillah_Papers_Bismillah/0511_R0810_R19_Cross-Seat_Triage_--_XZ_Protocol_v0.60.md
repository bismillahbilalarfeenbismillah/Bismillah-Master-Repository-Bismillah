# Bismillah ir-Rahman ir-Rahim

# R0810 -- R19 Cross-Seat Triage -- XZ Protocol v0.60

**Chronological Index:** 511 of 995  
**Date:** 2026-08-11  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** R19_TRIAGE.txt  
**Source Format:** txt  
**SHA-256:** `9c55cb86e0aba5c04485ef448da1b9901260de0387d3031ffec0dc215ccc8a9f`  

---

## R0810 · R19 Cross-Seat Triage -- XZ Protocol v0.60

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: R19_TRIAGE.txt
- source_format: txt
- text_sha256: 9c55cb86e0aba5c04485ef448da1b9901260de0387d3031ffec0dc215ccc8a9f

# R19 Cross-Seat Triage -- XZ Protocol v0.60
# Round: 19 (10 seats: 5 fresh + 5 continuous)
# All 10 seats: HALT (4 carrying binding HALT, 6 advisory HALT)
# Class A recurrence: R7-R19 (13/13), H = 1.0
# Laplace P(Class A at R20) = 14/15 = 0.933

## What CI v0.3 got right (verified across 10 seats)

- CI-1R: byte-exact register reproduction, unanimous PASS (all 10 seats)
- Baseline green: build.py PASS, 186/186 pytest, 19/19 PACKET_SHA256SUMS at all executing seats
- HISTORY seal chain: 60/60 ENTRY seals + FULL_SECTION_27 + PRIOR_HISTORY verified
- PRIOR_HISTORY cross-anchored to held v0.59 HISTORY.sha256 (S01C, S04C -- first round with held-byte anchor)
- Correction-letter allocation from explicit refs: no namespace collision (R18 Defect 2 DISCHARGED)
- Disposition vocabulary: SCOPED_OUT in generator code verified functional
- Validation fail-closed: invalid severities, malformed IDs, duplicates, missing finding records all rejected
- Referenced-finding existence validated: removing a group finding_id from findings[] fails generation
- Section 22.2/22.3 values at v0.59 (correct VERSION-1 for 60 entries)
- Terminal line tagged, boundary list correct, ASSERTED fraction 4.5-5.6% (all PASS)
- R18 Defects 2 (correction cursor), 4 (secondary membership label), 5 (R16 receipt) DISCHARGED

## Convergent defect groups

### Surface 1: Source severity still not load-bearing (M2/M3 remain inert)
Convergence: UNANIMOUS -- all 10 seats.
- S01F: 3 findings covering M2 (105/105 inert), M3 (receipt enforcement vacuous on shipped index)
- S01C: F-S01C-60-01 (HIGH) -- 4 Class A findings; M2 and M3 inert
- S02F: F-S02-60-01F (HIGH) -- M2a/M2b/M3 all produce byte-identical register
- S02C: F-S02-60-01 (HIGH) -- same, with 7 mutation probes
- S03F: (not separately cited but noted CI v0.3 mechanisms intact at majority depth)
- S03C: (severity provenance finding from R17 still tracked)
- S04F: (M2a ACCEPT, M2b RAISE, M3 receipt enforcement vacuous)
- S04C: F-S04-60-03 (MEDIUM) -- M2 shape still silent when receipt present
- S05F: F-S05-60-01 (HIGH) -- 6 inert mutations; stale receipt accepted after flip
- S05C: F-S05-60-01 (HIGH) -- same with 14 continuity mutations

Triage severity: HIGH. The generator computes a majority but still emits group["triage_severity"] unconditionally. Source severity is a conditional validation input, not a load-bearing rendered value. A valid source-severity mutation can be invisible if a receipt (of any content) exists. Receipt content is not validated against the distribution it claims to adjudicate.
Root cause: CI v0.3 checks majority divergence and receipt presence/non-emptiness, but never binds the receipt to the computed distribution. The spec says "severity derivation from source records with mandatory adjudication receipt on divergence" -- the implementation only gates presence, not fidelity.

### Surface 2: Correction (ch) never landed (SCOPED_OUT not set in index)
Convergence: 7/10 seats (S01F, S01C, S02F, S02C, S03C, S04C, S05F).
- S01F: finding covering group 4 disposition still CLOSED
- S02F: F-S02-60-02F (HIGH) -- DIFF-VERIFIED statement false on bytes
- S02C: same substance
- S03C: F-S03-60-01 (HIGH) -- generator emits CLOSED not SCOPED OUT
- S04C: F-S04-60-01 (HIGH) -- correction (ch) never landed; Status claim false
- S05F: F-S05-60-03 (HIGH) -- index group 4 disposition still CLOSED
- S05C: discharged as scope-out in v0.60 narrative, but index not updated

Triage severity: HIGH. The body repair ledger says correction (ch) changed group 4 disposition to "SCOPED OUT" and marks it [DIFF-VERIFIED]. The shipped r18_findings_index.json group 4 has disposition: "CLOSED". The register emits "CLOSED via append-only correction (ch)". The producer forgot to actually set the field in the index.

### Surface 3: VERSION-1 gate claimed but absent from build.py
Convergence: 7/10 seats (S01F, S01C, S02F, S02C, S03F, S04C, S05F).
- S01F: M8 proof -- stale bounds + resealed sums still pass build
- S02C: F-S02-60-03 (HIGH) -- stale bounds with consistent sums pass build
- S03F: F-S03-60-01 (HIGH) -- no VERSION-1 gate in build.py
- S04C: F-S04-60-02 (HIGH) -- executed sabotage: reverted bounds still pass build
- S05F: F-S05-60-04 (HIGH) -- no Section 22 token check in build.py

Triage severity: HIGH. The register adjudication says "CI v0.3 gates both bounds to VERSION-1" and the Status line claims the bounds are gated. No such gate exists in build.py. S04C's executed sabotage (reverting to v0.57 with resealed sums) proves BUILD PASSED on stale bounds.

### Surface 4: Dangling convergence_group values in findings[]
Convergence: 5/10 seats (S01F, S01C, S02F, S02C, S05F).
- S01F: S1-P8 predicted and confirmed; mutation to group 99 inert
- S02F: F-S02-60-03F or cited as cross-layer validation failure
- S02C: 7 dangling records (groups 9-12); mutation to 999 accepted
- S05F: F-S05-60-02 (HIGH) -- 7 dangling records; convergence_group mutation inert
- S05C: same substance from continuity

Triage severity: HIGH. The register claims validation boundary extension covers cross-layer references (group 8 CLOSED via CI v0.3). The shipped index contains findings[] records referencing convergence_groups 9-12 that don't exist. The generator never validates findings[].convergence_group against declared groups.

### Surface 5: Finding ID F/C suffixes not in source reports (CI-8 fidelity)
Convergence: 4/10 seats (S02F, S02C, S04C, S05C).
- S02F: F-S02-60-03F (HIGH) -- 19/35 index finding IDs absent from R18_REPORTS
- S02C: same, 19/35 absent
- S04C: F-S04-60-05 (MEDIUM) -- undocumented F/C suffix mapping
- S05C: (cited as CI-8 finding)

Triage severity: HIGH (per S02F binding), MEDIUM at S04C. The index appends F/C mode suffixes to source finding IDs. R18_REPORTS use the base IDs (F-S02-59-01, not F-S02-59-01F). No normalization receipt or source_finding_id field maps the renamed IDs back. CI-8 requires every index finding_id to exist in its seat report.

### Surface 6: Gate count documentation (recurring)
Convergence: 6/10 seats.
- AUDIT_CONTEXT says 258; executed build emits 257 PASS: lines; CI_METHODOLOGY says 222
Triage severity: MEDIUM.

### Surface 7: Body-repair ledger not generated from correction_refs
Convergence: 3/10 seats (S02C, S05F, S05C).
- S05F: F-S05-60-05 (HIGH) -- register claims "body-repair ledger generated from same refs" but no body-ledger generation exists
- S02C: register-to-body coupling not gated; (cg)->(zz) mutation passes build
Triage severity: MEDIUM. The register adjudication prose is tagged [COMPUTED] but is verbatim-copied from hand-authored index fields. No build gate cross-checks register correction refs against the body ledger.

## Minimum repair set for v0.61

1. **Make source-severity distribution load-bearing**: hash or emit the exact distribution into the receipt; validate receipt content against computed distribution; make every valid source-severity mutation alter output or fail. THIS IS THE CENTRAL REPAIR.
2. **Land correction (ch)**: set r18_findings_index.json group 4 disposition to "SCOPED_OUT" with scope_note. One-line fix.
3. **Add VERSION-1 gate to build.py**: derive expected prior version from VERSION; assert Section 22.2 and 22.3 tokens match; add mutation tests.
4. **Validate findings[].convergence_group**: reject dangling values; use null for ungrouped/noted findings.
5. **Preserve literal source finding IDs**: add source_finding_id field or define normalization mapping.
6. **Derive gate count from build.py runtime output**: inject into dispatch documents.
7. **Narrow COMPUTED tag scope**: tag only fields truly derived by code; or generate body-repair ledger from correction_refs.

## Recurrence analysis

R7-R19: 13/13, H = 1.0. The defect surface continues to narrow and migrate:

R7-R15: Register/body prose/narrative (formatting, counts, staleness)
R16-R18: Spec-impl gap in CI architecture (findings[] inert, cursor collision)
R19: Severity derivation incomplete + unlanded correction + missing gate + dangling references

The CI v0.3 mechanism repairs ARE landing (correction cursor fixed, fail-closed validation real, referenced-finding existence enforced, PRIOR_HISTORY cross-anchored). The Class A surface moved off the computed register and onto the hand-maintained surfaces around it: the body-repair ledger that claims corrections landed when they didn't, the front-matter Status that claims gates exist when they don't, and the generator's majority-only severity check that doesn't match the dispatched M2/M3 contract.

S04C's analysis is the sharpest: "The Class A defects are not in the mechanism; they are in the hand-written claims about the mechanism and about corrections that did not land. The metastasis boundary moved off the computed surface back onto tagged hand prose."

---
*R19 cross-seat triage produced by Claude Opus 4.6 (producer), 2026-08-11.*
*Bismillah.*

---

# Bismillah ir-Rahman ir-Rahim
