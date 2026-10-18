# Bismillah ir-Rahman ir-Rahim

# R0621 -- FALSIFIER RUN 1: CE169 under MUTATED (reverted) gate

**Chronological Index:** 842 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** falsifier_output.txt  
**Source Format:** txt  
**SHA-256:** `376784ce5548a253d50d32cba15f1fd216ff76f3b03c6bbca8176b4d0e08a4e2`  

---

## R0621 · FALSIFIER RUN 1: CE169 under MUTATED (reverted) gate

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: falsifier_output.txt
- source_format: txt
- text_sha256: 376784ce5548a253d50d32cba15f1fd216ff76f3b03c6bbca8176b4d0e08a4e2

########## FALSIFIER RUN 1: CE169 under MUTATED (reverted) gate ##########
$ python3 bssg_counterexamples.py   # CE169 line + summary
GREEN CE169 [GLM-F1] GLM-F1/K32-01 cross-contract ceiling-poison CLOSED: a DENIED degraded C2 DELETE does not poison contract_ceiling; post-lift re-establish for DELETE is DENY_FALSE  ceiling_no_delete=True exploit_denied=True
172/172 GREEN  (0 RED = open defects)

########## FALSIFIER RUN 2: model check under MUTATED (reverted) gate ##########
$ python3 bssg_model_check.py
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
FAIL BOUNDED-AUTH-INTRO: over all schedules (len<=4, 5-op alphabet) no ALLOW authorizes an effect or target outside the established healthy ceiling (Axiom-3/R_may closure)  schedules=553 allows=228 VIOLATION sched=(('A', 'C2', 'DELETE', 'DEGRADED'), ('A', 'C1', 'READ', 'HEALTHY'), ('L',), ('A', 'C2', 'DELETE', 'HEALTHY')) eff=DELETE

MODEL CHECK: FAIL -- 1: BOUNDED-AUTH-INTRO: over all schedules (len<=4, 5-op alphabet) no ALLOW authorizes an effect or target outside the established healthy ceiling (Axiom-3/R_may closure)
EXIT=1

---

# Bismillah ir-Rahman ir-Rahim
