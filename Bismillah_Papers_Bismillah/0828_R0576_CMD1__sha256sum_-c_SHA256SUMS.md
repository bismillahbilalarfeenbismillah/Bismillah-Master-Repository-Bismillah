# Bismillah ir-Rahman ir-Rahim

# R0576 -- CMD1: sha256sum -c SHA256SUMS

**Chronological Index:** 828 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** COMMAND_OUTPUTS (2).txt  
**Source Format:** txt  
**SHA-256:** `60b6228a5fb7659a09a3759d277cb507049d5426dd6736e8fe2c30afba2cbdc4`  

---

## R0576 · CMD1: sha256sum -c SHA256SUMS

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: COMMAND_OUTPUTS (2).txt
- source_format: txt
- text_sha256: 60b6228a5fb7659a09a3759d277cb507049d5426dd6736e8fe2c30afba2cbdc4

=== CMD1: sha256sum -c SHA256SUMS ===
ATTACK_AND_FALSIFIER_REGISTER.md: OK
BSSG_v0_1_CANONICAL_SPEC_DRAFT.pplx.md: OK
BSSG_v0_1_DECISION_REGISTER.md: OK
BSSG_v0_1_MODEL_COUNCIL_SYNTHESIS.pplx.md: OK
OPEN_DECISIONS.md: OK
README.md: OK
REPAIR_STATUS.md: OK
REQUIREMENTS_TRACEABILITY.md: OK
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

=== CMD2: python3 test_bssg_gate.py ===
......................................................................................................................................................................................................................................................................................................................ssssssss...........................
----------------------------------------------------------------------
Ran 345 tests in 0.065s

OK (skipped=8)

=== CMD3: python3 bssg_counterexamples.py ===
GREEN CE158 [X7-P28] V29 withdrawal: breadth is NOT certified offline -- within-ceiling and beyond-ceiling armed re-widens are both X7U; the breadth bound is enforced online (BOUNDED-AUTH-INTRO)  within_clean=True within_unanchored_x7=True beyond_eff_x7=True beyond_tgt_x7=True
GREEN CE159 [K-P28] kernel abort recovers a clock-independent determinate FALSE even when the first clock read raises  effecttype_false_on_clockfault=True valid_stays_unknown=True
GREEN CE160 [B-PROBE1-P30] PROBE-1: a runtime-REJECTED amendment mints no grant (runtime truth); the claimed armed re-widen is X7U offline (grant inert; the rejection is enforced online)  rejected_no_grant=True claimed_rewiden_x7=True
GREEN CE161 [B-PROBE2-P30] PROBE-2 (V29 withdrawal): an armed beyond-ceiling re-widen is X7U offline, but a forged beyond-ceiling wide SEED is a grant-independent target-widening -> X7 (it cannot ride along: it contaminates the stream to X7); a within-ceiling seed is inert (armed re-widen stays X7U); a lone seed (no re-widen) is clean  seed_beyond_x7=True noseed_beyond_x7=True within_clean=True wide_seed_contaminates=True within_seed_inert=True lone_wide_seed_clean=True
GREEN CE162 [B-A3-P30] Kimi-A3: the gate's OWN honest degraded-first recovery is NOT a violation -- it is X7U (uncertifiable, not a false positive), identical with or without the grant  recovery_clean_anchored=True unanchored_x7=True
GREEN CE163 [B-RESIDUAL-P30] RESIDUAL CLOSED (V29 withdrawal): an authentic and a fabricated grant now yield the IDENTICAL X7U -- there is no positive certification left to spoof; the forged-grant residual is eliminated at the root  authentic=['X7U'] forged=['X7U'] identical_uncertifiable=True
GREEN CE164 [GPT-P30-01] GPT-P30-01 EFFECT BYPASS CLOSED: a widening rejected before a genuine lift cannot launder through it (runtime DENY_FALSE; ceiling+grant carry no DELETE; checker honest)  rewiden_denied=True ceiling_no_delete=True grant_no_delete=True checker_honest=True
GREEN CE165 [GPT-P30-02] GPT-P30-02 multi-cycle: a conformant two-amendment history is X7U offline (each cycle uncertifiable, grant inert); the per-session ledger remains a runtime diagnostic  two_amendment_clean=True ledger_size=2
GREEN CE166 [GPT-P30-03/K30-A4] GPT-P30-03 + K30-A4 abort soundness both ways: recovers a determinate witness FALSE on a raising verifier (not masked); never fabricates one clock-free (not manufactured)  mask_recovered_false=True no_clockfree_fabrication=True
GREEN CE167 [GPT-P30-05] GPT-P30-05 BaseException totality/liveness: a dependency-originated non-Exception BaseException fails closed at AIB/commit/amendment (no COMMITTING strand, outcome recorded, no escape); KeyboardInterrupt/SystemExit still propagate with rollback  aib_closed=True commit_closed_no_strand=True amend_recorded=True ki_propagates_voided=True
GREEN CE168 [GPT-P30-04] GPT-P30-04: authorized_issuance_bound reads the clock INSIDE the commit lock (precise point-in-time linearization -- a token expiring while the predicate waits for the lock is observed expired, not certified on stale pre-lock time)  clock_read_under_lock=True baseline_true=True
GREEN CE169 [GLM-F1] GLM-F1/K32-01 DEGRADED-vector ceiling-poison CLOSED: a DENIED degraded C2 DELETE does not poison contract_ceiling; post-lift re-establish for DELETE is DENY_FALSE  ceiling_no_delete=True exploit_denied=True
GREEN CE173 [K33-01] K33-01 ALLOWed-degraded ceiling-poison CLOSED: an ALLOWed degraded C2 READ does not broaden contract_ceiling; post-lift DELETE is DENIED  allowed=True no_delete_leak=True cc_unchanged=True delete_denied=True
GREEN CE170 [GPT-P32-01] GPT-P32-01 same-epoch over-withdrawal CLOSED: unarmed same-epoch ceiling CHANGE is X7; armed same-epoch ceiling CHANGE is X7 (grant-independent); armed same-epoch EQUAL is X7U  unarmed_changed_x7=True armed_changed_x7=True armed_equal_x7u=True
GREEN CE171 [K32-03] K32-03 malformed snapshot CLOSED: armed + string/int snapshot is X7 (type-tamper); armed + absent snapshot is skipped (clean)  str_x7=True int_x7=True absent_clean=True
GREEN CE172 [K32-04] K32-04 marker metadata CLOSED: well-formed marker arms X7U; missing licensed_epoch fails marker validation -> widening is unlicensed X7  good_x7u=True no_le_x7=True
GREEN CE174 [AUDIT-V33-01] AUDIT-V33-01 commit pre-reserve BaseException totality: a hostile BaseException-raising binding fails closed (VOID + failure record), does not escape the public API  escaped=False closed=True token_status=VOID
GREEN CE175 [F-GS-1] F-GS-1 mint-fault ceiling-poison CLOSED: a FAILED_NO_EFFECT first-establish writes empty contract_ceiling; post-lift DELETE is DENIED; session never successfully held DELETE  mint_failed=True no_delete=True cc_empty=True delete_denied=True

175/175 GREEN  (0 RED = open defects)

=== CMD4: python3 bssg_model_check.py ===
PASS A1 kernel truth table: gate matches spec rule on all 3^5 states + ALLOW iff all TRUE  states=243
PASS A2 degradation antitone over the full finite lattice (health down => ceiling subset)  contracts=729
PASS OP-POS valid authorize -> AUTHORIZED_UNUSED and a single commit -> COMMITTED
PASS OP-R1 no allow-after-deny for a snapshot, and a fresh request still authorizes
PASS OP-R2 single-use redemption: first COMMITTED, second FAILED_NO_EFFECT
PASS OP-R6 sessions isolated (B unaffected by A) AND same-session widening is terminal
PASS OP-STRICT strict health drop without strict narrowing is terminal (E-NONSTRICT-NARROWING)
PASS OP-R5 valid amendment recovers (SESSION_TERMINAL->EVALUATING); bad-domain / dup-sig / wrong-class rejected
PASS OP-ABSORB request in a terminal session is refused (E-SESSION-TERMINAL)
PASS OP-OD11 subject-facing conceals DENY_FALSE vs DENY_UNKNOWN (audit plane retains it)
PASS OP-REJECT structural admission failure is a distinct REJECTED_SCHEMA state
PASS OP-DENY-PATHS every deny path is terminal for its snapshot (no allow-after-deny on ANY path)  paths=3
PASS REFINE every observed executable transition is permitted by Section 14  observed=22 illegal=0
PASS REFINE no DENIED_*->AUTHORIZED_UNUSED edge ever occurred on the executable
PASS REFINE every kernel-evaluated record satisfies decision == kernel_decision(conjuncts); protocol records (replay, reentrant) exempt and load-bearing  records=7 inconsistent=0 collision=FAILED_NO_EFFECT mint_abort=FAILED_NO_EFFECT replay_exempt=True reentrant_false=True
PASS BOUNDED-AUTH-INTRO: over all schedules (len<=4, 10-op alphabet) no ALLOW authorizes an effect or target outside the established healthy ceiling (Axiom-3/R_may closure)  schedules=11110 allows=7200

MODEL CHECK: PASS -- kernel(243) + antitone(729) + bounded-auth-intro(11110 schedules) + operational refinement on the executable

=== CMD5: python3 verify_bssg_v0_1.py ===
BSSG v0.1 DRAFT package verifier
Package directory: /home/user/workspace/bssg_round2/packet
------------------------------------------------------------------------
G1    PASS   all 10 required files and exactly 6 schemas present
G2    WARN   jsonschema not installed; structural check only
G2    PASS   six schemas valid, closed, DRAFT-marked, five conjuncts
G3    PASS   345 tests passed, including 243 kernel truth states
G4    PASS   73 citation occurrences, all resolvable to the 34 listed references
G5    PASS   no prohibited effectiveness language outside the registry
G6    PASS   BCP 14 boilerplate present; MUST=88 MUST NOT=30 SHALL=13 SHOULD=10 MAY=5
G7    PASS   no em dash, en dash, or related characters in source files
G8    PASS   version 0.1 parity and DRAFT / NOT CARRIED status intact
G9    PASS   SHA256SUMS verified for 20 files
G10   WARN   12 open design decisions (OD-1, OD-2, OD-3, OD-4, OD-5, OD-6, OD-7, OD-8, OD-9, OD-10, OD-11, OD-12); decision register records STILL BLOCKING findings
G11   PASS   X4/X5/X6/X7/X8 detect negatives, pass positives, bind + tamper-check real gate records; X5/X6 total
G12   PASS   every registered load-bearing claim (27) has a passing probe and a REPAIR_STATUS tag; cited CEs exist
G13   PASS   counterexample corpus EXECUTED: 175/175 GREEN, 0 RED (independently counted; self-report matches)
------------------------------------------------------------------------
SUMMARY: 14 gates, 12 PASS, 2 WARN, 0 FAIL
PACKAGE STATUS: SELF-CONSISTENT DRAFT (not carried, not publication ready)

=== EXTRA: python3 bssg_gate.py banner ===
BSSG reference gate 0.1.0-draft, spec version 0.1
DRAFT / NOT CARRIED. No effectiveness claim is made by this software.

---

# Bismillah ir-Rahman ir-Rahim
