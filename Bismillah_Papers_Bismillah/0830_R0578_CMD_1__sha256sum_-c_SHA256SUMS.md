# Bismillah ir-Rahman ir-Rahim

# R0578 -- CMD 1: sha256sum -c SHA256SUMS

**Chronological Index:** 830 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** COMMAND_OUTPUTS.txt  
**Source Format:** txt  
**SHA-256:** `e88a6eaed3318bdeba046721019d93a993ee6ca1a093b1d0dd79753c37b89aa8`  

---

## R0578 · CMD 1: sha256sum -c SHA256SUMS

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: COMMAND_OUTPUTS.txt
- source_format: txt
- text_sha256: e88a6eaed3318bdeba046721019d93a993ee6ca1a093b1d0dd79753c37b89aa8

=== CMD 1: sha256sum -c SHA256SUMS ===
sha256sum: ATTACK_AND_FALSIFIER_REGISTER.md: No such file or directory
ATTACK_AND_FALSIFIER_REGISTER.md: FAILED open or read
BSSG_v0_1_CANONICAL_SPEC_DRAFT.pplx.md: OK
sha256sum: BSSG_v0_1_DECISION_REGISTER.md: No such file or directory
BSSG_v0_1_DECISION_REGISTER.md: FAILED open or read
sha256sum: BSSG_v0_1_MODEL_COUNCIL_SYNTHESIS.pplx.md: No such file or directory
BSSG_v0_1_MODEL_COUNCIL_SYNTHESIS.pplx.md: FAILED open or read
sha256sum: OPEN_DECISIONS.md: No such file or directory
OPEN_DECISIONS.md: FAILED open or read
sha256sum: README.md: No such file or directory
README.md: FAILED open or read
REPAIR_STATUS.md: OK
sha256sum: REQUIREMENTS_TRACEABILITY.md: No such file or directory
REQUIREMENTS_TRACEABILITY.md: FAILED open or read
bssg_attest.py: OK
bssg_counterexamples.py: OK
bssg_gate.py: OK
bssg_model_check.py: OK
schemas/authorization-receipt.schema.json: OK
schemas/correction-event.schema.json: OK
schemas/effect-request.schema.json: OK
schemas/execution-receipt.schema.json: OK
schemas/lineage-record.schema.json: OK
schemas/witness-receipt.schema.json: OK
test_bssg_gate.py: OK
verify_bssg_v0_1.py: OK
sha256sum: WARNING: 6 listed files could not be read

=== CMD 2: python3 test_bssg_gate.py (tail) ===
......................................................................................................................................................................................................................................................................................................................ssssssss...........................
----------------------------------------------------------------------
Ran 345 tests in 0.065s

OK (skipped=8)

=== CMD 3: python3 bssg_counterexamples.py (tail) ===
GREEN CE174 [AUDIT-V33-01] AUDIT-V33-01 commit pre-reserve BaseException totality: a hostile BaseException-raising binding fails closed (VOID + failure record), does not escape the public API  escaped=False closed=True token_status=VOID

174/174 GREEN  (0 RED = open defects)

=== CMD 4: python3 bssg_model_check.py (tail) ===
PASS BOUNDED-AUTH-INTRO: over all schedules (len<=4, 7-op alphabet) no ALLOW authorizes an effect or target outside the established healthy ceiling (Axiom-3/R_may closure)  schedules=2800 allows=1603

MODEL CHECK: PASS -- kernel(243) + antitone(729) + bounded-auth-intro(2800 schedules) + operational refinement on the executable

=== CMD 5: python3 verify_bssg_v0_1.py ===
BSSG v0.1 DRAFT package verifier
Package directory: /home/user/workspace/bssg_review
------------------------------------------------------------------------
G1    FAIL   missing required files: BSSG_v0_1_MODEL_COUNCIL_SYNTHESIS.pplx.md, BSSG_v0_1_DECISION_REGISTER.md, README.md, REQUIREMENTS_TRACEABILITY.md, ATTACK_AND_FALSIFIER_REGISTER.md, OPEN_DECISIONS.md
G2    WARN   jsonschema not installed; structural check only
G2    PASS   six schemas valid, closed, DRAFT-marked, five conjuncts
G3    PASS   345 tests passed, including 243 kernel truth states
G4    PASS   28 citation occurrences, all resolvable to the 34 listed references
G5    FAIL   prohibited effectiveness language: bayyinah_cross-vendor-rotation.md:151 outperform
G6    PASS   BCP 14 boilerplate present; MUST=88 MUST NOT=30 SHALL=13 SHOULD=10 MAY=5
G7    FAIL   bayyinah_em-dash-policy.md contains en dash at offset 2099; bayyinah_em-dash-policy.md contains em dash at offset 2037; bayyinah_em-dash-policy.md contains horizontal bar at offset 2168
G8    FAIL   gate raised FileNotFoundError on non-total input (e.g. a missing manifest-bound file)
G9    FAIL   manifest lists missing file ATTACK_AND_FALSIFIER_REGISTER.md; manifest lists missing file BSSG_v0_1_DECISION_REGISTER.md; manifest lists missing file BSSG_v0_1_MODEL_COUNCIL_SYNTHESIS.pplx.md; manifest lists missing file OPEN_DECISIONS.md; manifest lists missing file README.md; manifest lists missing file REQUIREMENTS_TRACEABILITY.md; files present but not in the manifest: COUNCIL_BRIEF.md, methodology/METHODOLOGY_INDEX.md, methodology/PMD_v1_2_BAF_v3_0.md, methodology/bayyinah_audit-modes.md, methodology/bayyinah_brand-canonical.md, methodology/bayyinah_cross-vendor-rotation.md, methodology/bayyinah_em-dash-policy.md, methodology/bayyinah_findings-format.md, methodology/bayyinah_methodology-foundations.md, methodology/bayyinah_severity-rubric.md, methodology/bayyinah_substrate-of-record.md
G10   FAIL   gate raised FileNotFoundError on non-total input (e.g. a missing manifest-bound file)
G11   PASS   X4/X5/X6/X7/X8 detect negatives, pass positives, bind + tamper-check real gate records; X5/X6 total
G12   PASS   every registered load-bearing claim (27) has a passing probe and a REPAIR_STATUS tag; cited CEs exist
G13   PASS   counterexample corpus EXECUTED: 174/174 GREEN, 0 RED (independently counted; self-report matches)
------------------------------------------------------------------------
SUMMARY: 14 gates, 7 PASS, 1 WARN, 6 FAIL
PACKAGE STATUS: INCONSISTENT (draft retained, do not package)

=== EXTRA: python3 bssg_gate.py ===
BSSG reference gate 0.1.0-draft, spec version 0.1
DRAFT / NOT CARRIED. No effectiveness claim is made by this software.

---

# Bismillah ir-Rahman ir-Rahim
