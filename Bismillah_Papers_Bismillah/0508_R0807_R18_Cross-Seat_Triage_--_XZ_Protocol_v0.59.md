# Bismillah ir-Rahman ir-Rahim

# R0807 -- R18 Cross-Seat Triage -- XZ Protocol v0.59

**Chronological Index:** 508 of 995  
**Date:** 2026-08-11  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** R18_TRIAGE.txt  
**Source Format:** txt  
**SHA-256:** `8ec45cc71d1f18e3c7b565062a89960347ce341beccf847afa77905874a19f0e`  

---

## R0807 · R18 Cross-Seat Triage -- XZ Protocol v0.59

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: R18_TRIAGE.txt
- source_format: txt
- text_sha256: 8ec45cc71d1f18e3c7b565062a89960347ce341beccf847afa77905874a19f0e

# R18 Cross-Seat Triage -- XZ Protocol v0.59
# Round: 18 (10 seats: 5 fresh + 5 continuous)
# All 10 seats: HALT (4 carrying binding HALT, 6 advisory HALT)
# Class A recurrence: R7-R18 (12/12), H = 1.0
# Laplace P(Class A at R19) = 13/14 = 0.929

## What CI v0.2.2 got right (verified across 10 seats)

- CI-1R: byte-exact register reproduction at all seats (unanimous PASS)
- CI-4: ASSERTED fraction 3.8-5.0% by tag count (all PASS under tag basis)
- Disposition fail-closed: unknown tokens rejected at all executing seats
- Finding ID validation: malformed and duplicate IDs rejected within groups
- Header seat word computed from index; correction cursor computed from prior_correction_end
- Terminal line tagged [COMPUTED: generate_terminal_line], unique, final
- Section 22.2/22.3 bounds advanced to v0.57 (correct for v0.58 carried entries)
- Narrative convergence counts verified individually against index
- All 186 tests GREEN; 19/19 PACKET_SHA256SUMS OK; 59/59 ENTRY seals verified
- Full executable packet shipped and verified for the first time
- R17 Defects 4 (narrative counts), 7 (terminal tag), 8 (disposition), 9 (hardcoded literals), 10 (ID validation): all DISCHARGED on bytes

## Convergent defect groups

### Surface 1: findings[] semantically inert (spec-impl gap persists)
Convergence: 9/10 seats. Unanimous across all models and modes.
- S01F: F-S01-59-03 (HIGH) -- findings_by_id never used; M2/M3 prove inertness
- S02F: F-S02-59-01 (HIGH) -- deleting entire findings[] leaves output unchanged
- S02C: F-S02-59-01 (HIGH) -- same with 7 sabotage probes proving disconnection
- S03F: Gemini severity provenance (HIGH) -- static trace confirms no derivation logic
- S03C: F-S03-59-01 (HIGH) -- same via continuous re-verification
- S04F: F-S04-59-02 (HIGH) -- M2/M3 confirm; adjudication_receipt in docstring only
- S05F: F-S05-59-01 (HIGH) -- 6 inert mutations documented
- S05C: same substance, receipt removal inert, valid-severity mutation inert
Triage severity: HIGH. R17 Defect 2 persists one layer down: findings[] is now parsed but remains semantically inert for output. The generator builds findings_by_id and never reads it. The front-matter Status and generator docstring falsely claim derivation and receipt enforcement.
Root cause: CI v0.2.2 implemented token validation only. The relational logic (source-severity derivation, adjudication receipt requirement, cross-reference enforcement) was specified in the docstring but not coded. The R17 triage's repair item required "derive group severity from source records with mandatory adjudication receipt on divergence" -- only the token validation half landed.

### Surface 2: Correction-letter namespace collision (novel R18 defect)
Convergence: 6/10 seats. Both Kimi seats + both GPT-5.6 Sol CONT + S05 fresh + S02 continuous.
- S01F: F-S01-59-04 (HIGH) -- body (cc)/(cd)/(ce)/(cf) vs register (cc)/(cd)/(ce)
- S02C: F-S02-59-02 (HIGH) -- same with F-CI-3R fired
- S04F: F-S04-59-01 (HIGH) -- correction-letter namespace collision, metastasis boundary
- S05F: F-S05-59-02 (HIGH) -- generator advances once per group not once per correction
- S05C: same, with correction-reference cross-check against body ledger
Triage severity: HIGH. This is a novel R18 defect introduced by the R17 Defect 9 repair (hardcoded cursor -> computed cursor). Group 1 consumes two corrections (cc)+(cd) in the body, but the generator increments correction_idx once per group. Register items (4) and (5) therefore cite letters that map to different repairs in the body. Internal to item (1), the adjudication says "(cc)/(cd)" while the disposition says "(cc)" only. F-CI-3R fires: a Class A inside a [COMPUTED: generate_register] claim.
Root cause: One-letter-per-group assumption in the generator. No build gate checks letter-to-body-repair fidelity. The repaired surface (computed cursor) metastasized: a hardcoded wrong value became a computed wrong value.

### Surface 3: Section 22.2/22.3 version-token staleness (6th recurrence)
Convergence: 2/10 seats (S01F, Gemini fresh). S04F explicitly marks it DISCHARGED (bounds at v0.57 = correct for v0.58 carried entries).
- S01F: F-S01-59-01 (HIGH) -- "v0.1 through v0.57" and "v0.38-v0.57" in a v0.59 doc whose carried entries run to v0.58. Sixth consecutive round of this class (R13-R18).
- Gemini: version-token staleness (HIGH) -- same substance
Triage assessment: DISPUTED. The v0.59 document has 59 entries, v0.1-v0.59. Carried entries are v0.1-v0.58 (the v0.59 entry is the current entry, not yet carried). Section 22.2 says "v0.1 through v0.57" -- stale by one. S01F is correct that this is byte-false. S04F discharged it because the bounds advanced to the R17 repair target; but the repair target was for a v0.58 document, and this is v0.59. The rule should be VERSION-1 (entry count minus one), and the v0.59 document's carried entries end at v0.58, not v0.57.
Producer assessment: S01F is right. The repair applied the R17 triage's literal target ("advance to v0.57") instead of the semantic rule ("advance to current minus one"). Needs to advance to v0.58 and be gated.

### Surface 4: Secondary membership CLOSED but not implemented
Convergence: DISPUTED. 5/10 seats call it Class A; 2/10 call it discharged via explicit scope-out.
- S02F: F-S02-59-02 (HIGH) -- scalar convergence_group only, CLOSED label overstates
- S02C: discharged via explicit scope-out but lossy membership "remains absent"
- S04F: explicitly DISCHARGED -- R17 triage allowed "implement or explicitly scope out"
- S05F: F-S05-59-03 (HIGH) -- CLOSED label with no closure mechanism
- S05C: same substance
- Gemini: secondary membership schema gap (HIGH)
Triage assessment: The R17 triage's own Defect 3 repair said "implement or explicitly scope out." AUDIT_CONTEXT explicitly scopes it out. The register says "CLOSED via CI v0.2.2 architecture repair" -- this disposition label overstates the actual repair (scope-out, not architecture implementation). S02 continuous accepted the explicit scope-out as adequate. S01F and S04F accepted it. S02F fresh, S05F/C, and Gemini call it Class A because the register label says CLOSED-via-repair when nothing was implemented.
Producer assessment: The disposition label should be "SCOPED OUT" or "CLOSED via explicit scope-out, canonical-group rule retained." The current "CLOSED via CI v0.2.2 architecture repair" is technically false since no code implements multi-membership. Fix the label, not the mechanism.

### Surface 5: Gate count documentation (262 vs 261 vs 222)
Convergence: 5/10 seats. MEDIUM at all.
- S01F: F-S01-59-05 (MEDIUM), S02F: F-S02-59-05 (MEDIUM), S02C: F-S02-59-03 (MEDIUM)
- S04F: F-S04-59-03 (MEDIUM), S05F: F-S05-59-04 (MEDIUM)
Triage severity: MEDIUM. Fourth consecutive round. AUDIT_CONTEXT says 262; executed build emits 261 PASS lines; CI_METHODOLOGY still says 222; front-matter claims "Gate count documentation reconciled."

### Additional findings (lower severity, selected)

- **COMPUTED tag overclaim** (S01F F-S01-59-06, MEDIUM): register adjudication prose is verbatim-copied from hand-authored index fields but tagged COMPUTED. Sabotage token lands inside a COMPUTED-tagged line.
- **Validation boundary gap** (S04F F-S04-59-04, MEDIUM; S05F partial): noted dispositions, findings[] IDs, uniqueness, and cross-layer references all unvalidated. findings[] records F-S01-58-06/07, F-S04-58-05 reference convergence_groups 12/13/14 but only 1-11 exist -- dangling references.
- **CI-4 metric ambiguity** (S02C F-S02-59-04, MEDIUM): character-basis ASSERTED fraction 17.44% exceeds 15% while tag-count basis passes.
- **R16 group 6 receipt still wrong** (S01F F-S01-59-02, HIGH): the (cf) correction claims 2 MEDIUM + 1 LOW but the shipped findings[] shows 3 MEDIUM + 1 LOW. S02 omitted. The correction propagated the R17 triage's own miscount.
- **CI_METHODOLOGY schema gap** (S04F F-S04-59-06, LOW): no normative v0.2.2 schema published.

## Minimum repair set for v0.60

1. **Implement actual severity derivation from findings[]**: cross-reference every group finding_id to findings_by_id; compute source-severity distribution; require adjudication_receipt when group severity diverges; fail generation on missing/inconsistent records. Add M2/M3-class mutation tests.
2. **Fix correction-letter allocation**: store explicit correction_refs[] per group in the index; emit the correct letter(s) per group; add a build gate that cross-checks register correction references against the body-repair ledger.
3. **Advance Section 22.2 to "v0.1 through v0.58" and 22.3 to "v0.38-v0.58"**: implement the VERSION-1 rule (current_version - 1) and gate both bounds.
4. **Fix secondary membership disposition label**: change "CLOSED via CI v0.2.2 architecture repair" to "SCOPED OUT: canonical-group rule retained, multi-membership not implemented" or equivalent truthful label.
5. **Fix R16 group 6 receipt**: correct from "2 MEDIUM + 1 LOW" to "3 MEDIUM + 1 LOW" (S02 is MEDIUM in the findings[]).
6. **Reconcile gate counts**: derive from build.py output, not hand-maintained prose.
7. **Extend validation boundary**: validate noted dispositions, findings[] IDs, cross-layer references; reject dangling convergence_group values.
8. **Publish normative CI v0.2.2 schema**: supersede the v0.2.1 appendix.
9. **Split COMPUTED tag scope**: code-derived fields vs verbatim-copied adjudication prose.
10. **Define CI-4 metric formally**: specify numerator, denominator, and unit.

## Recurrence analysis

R7-R18: 12/12, H = 1.0 (persistent). Defect surface migration continues:

R7-R12: Register surface (phantom entries, counts, literals)
R13-R15: Body prose + register (title, status, severity)
R16: Narrative + body + spec-impl gap (CI v0.2 surfaces)
R17: Body + spec-impl gap + narrative ambiguity (CI v0.2.1 surfaces)
R18: Spec-impl gap + correction-letter collision + 22.x recurrence (CI v0.2.2 surfaces)

Pattern: each repair round's new infrastructure (findings[], computed cursor, COMPUTED tags) becomes the next round's Class A surface. The CI architecture is converging -- the defect count is shrinking and the surfaces are becoming more specific -- but the architecture's own spec-impl gap has persisted for 3 consecutive rounds (R16-R18) through three CI versions (v0.2, v0.2.1, v0.2.2). The correction-letter collision is a metastasis of the R17 hardcoded-literal repair. The 22.x recurrence is now 6 rounds old (R13-R18).

The executable packet shipped for the first time at R18 and worked: all 4 executing seats (S01F, S04F, S02F/C) ran build.py, pytest, sha256sum, and seal verification as EXECUTED. This is a structural improvement even though it didn't prevent Class A.

---
*R18 cross-seat triage produced by Claude Opus 4.6 (producer), 2026-08-11.*
*Bismillah.*

---

# Bismillah ir-Rahman ir-Rahim
