# Bismillah ir-Rahman ir-Rahim

# R0279 -- python3 test_bssg_gate.py

**Chronological Index:** 698 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** BSSG_v0_1_PASS3_GPT_COMMAND_TRANSCRIPT.txt  
**Source Format:** txt  
**SHA-256:** `24c57d7df8ded335578a5cd627b3405ae1f81e782e659fa95a4aa163c76eeedd`  

---

## R0279 · python3 test_bssg_gate.py

- section: V. BSSG & SHVVP Protocols
- source_file: BSSG_v0_1_PASS3_GPT_COMMAND_TRANSCRIPT.txt
- source_format: txt
- merged_variants: 1 (glm_pass8_raw_outputs (1).txt)
- text_sha256: 24c57d7df8ded335578a5cd627b3405ae1f81e782e659fa95a4aa163c76eeedd

=== python3 test_bssg_gate.py ===
...................................................................................................................................................................................................................................................................................................................................................
----------------------------------------------------------------------
Ran 339 tests in 0.122s

OK

=== python3 bssg_counterexamples.py ===
GREEN CE1 [R9] kernel rejects extra sixth conjunct  raised BSSGError
GREEN CE2 [R1] denied request is terminal (no allow-after-deny)  DENY_FALSE->DENY_FALSE same_digest=True
GREEN CE3 [R3] witness coverage mismatch blocks ALLOW  decision=DENY_FALSE
GREEN CE4 [R4] stale witness-epoch token cannot commit  outcome=FAILED_NO_EFFECT
GREEN CE5 [R2] one-time token redemption under concurrency  committed_count=1
GREEN CE6 [R11] malformed contract -> UNKNOWN, no crash  decision=DENY_UNKNOWN
GREEN CE7 [R10] schema-invalid request cannot ALLOW  decision=REJECTED_SCHEMA
GREEN CE8 [R5] terminal lift rejects duplicate-sig / wrong-class amendment  accepted=False
GREEN CE9 [R6] per-session authority state (no cross-session contamination)  A=ALLOW B=ALLOW/[]
GREEN CE10 [OD-11] subject-facing response conceals denial regime (audit plane keeps it)  audit=DENY_FALSE/DENY_UNKNOWN subj_equal=True
GREEN CE11 [P1] evidence-level denial is terminal (no allow-after-deny on early paths)  DENY_UNKNOWN->DENY_FALSE
GREEN CE12 [KIMI-1] out-of-range integer request is rejected, gate does not crash  decision=REJECTED_SCHEMA
GREEN CE13 [P5] amendment is single-use (replay cannot lift a later terminal)  first=True replay=False/['E-AMENDMENT-REPLAY']
GREEN CE14 [P6] schema-invalid amendment cannot lift a terminal state  accepted=False/['E-AMENDMENT-SCHEMA-INVALID']
GREEN CE15 [KIMI-2] adjudicator signature must bind its declared identity (no substitution)  accepted=False/['E-AMENDMENT-KID-MISMATCH']
GREEN CE16 [P7] witness receipt with an undeclared field cannot ALLOW  decision=DENY_FALSE
GREEN CE17 [P8] malformed binding cannot leave a token stuck in COMMITTING  raised=None status=VOID
GREEN CE18 [P9/P-E] commit and a concurrent terminalize serialize atomically (no torn/terminal commit)  commit=COMMITTED_PENDING_OUTCOME
GREEN CE19 [P-D1] out-of-range integer in evidence is rejected, gate does not crash  DENY_UNKNOWN
GREEN CE20 [P-C] nested undeclared witness field cannot ALLOW (recursive closedness)  decision=DENY_FALSE
GREEN CE21 [DP4b] undeclared evidence-bundle field cannot ALLOW  decision=DENY_UNKNOWN
GREEN CE22 [P-B1] amendment with wrong spec_version cannot lift a terminal  accepted=False/['E-AMENDMENT-SCHEMA-INVALID']
GREEN CE23 [P-B2] closure-invariant-violating amendment cannot lift a terminal  accepted=False/['E-AMENDMENT-CLOSURE-INVALID']
GREEN CE24 [DP5e] adjudicators must be in all-distinct domains (no collision)  accepted=False/['E-AMENDMENT-DOMAIN-COLLISION']
GREEN CE25 [P-G] concurrent same-nonce authorize yields at most one ALLOW (no duplicate)  decisions=['ALLOW', 'DENY_FALSE'] tokens=1
GREEN CE26 [P-F] token that expired while its commit was queued is rejected  outcome=FAILED_NO_EFFECT
GREEN CE27 [P-E] authorize and commit serialize on the gate lock (terminal re-check + CONSUME atomic)  authorize_locked=True commit_locked=True
GREEN CE28 [F1] extra field in a $ref'd witness signature sub-object cannot ALLOW  decision=DENY_FALSE
GREEN CE29 [GPT#2] amendment with unhashable correction_id is rejected, no crash  ['E-AMENDMENT-SCHEMA-INVALID']
GREEN CE30 [F2] nested extra field in an amendment object cannot lift a terminal  accepted=False/['E-AMENDMENT-SCHEMA-INVALID']
GREEN CE31 [P.1] amendment with an invalid top-level signature cannot lift a terminal  accepted=False/['E-AMENDMENT-BAD-SIGNATURE']
GREEN CE32 [P13] witness with a schema-invalid value (wrong spec_version) cannot ALLOW  decision=DENY_FALSE
GREEN CE33 [F3] malformed fresh evidence at commit voids the token (commit-path validation)  outcome=FAILED_NO_EFFECT/['E-COMMIT-EVIDENCE-SCHEMA-INVALID']
GREEN CE34 [P-A] terminal-session refusal is SESSION_TERMINAL, not DENY_FALSE (permits amendment recovery)  decision=SESSION_TERMINAL
GREEN CE35 [F-01] request with a schema-invalid field (int session_id) is REJECTED_SCHEMA, no crash  decision=REJECTED_SCHEMA
GREEN CE36 [F-02] witness violating a numeric bound (negative epoch, minimum:0) cannot ALLOW  decision=DENY_FALSE
GREEN CE37 [fail-closed] validator fails CLOSED on any unrecognised schema keyword (recurrence guard)  result=True
GREEN CE38 [F-04] newer authenticated epoch on a DENIED request voids an older token at commit  denied=DENY_FALSE commit=FAILED_NO_EFFECT/['E-COMMIT-EVIDENCE-EPOCH-CHANGED']
GREEN CE39 [F-05] token-factory collision yields one terminal record, no redeemable token minted  2nd=DENY_FALSE tokens=1
GREEN CE40 [F-06] a contract revoked after authorization voids the token at commit  commit=FAILED_NO_EFFECT/['E-COMMIT-CONTRACT-REVOKED']
GREEN CE41 [GLM-A] recovering token factory: collision snapshot stays terminal (no allow-after-deny)  d1=DENY_FALSE d2=DENY_FALSE
GREEN CE42 [GPT-2] negative evidence_epoch (bundle schema minimum:0) cannot ALLOW  decision=DENY_UNKNOWN
GREEN CE43 [GPT-1] malformed time-authority signature envelope cannot ALLOW  decision=DENY_UNKNOWN
GREEN CE44 [GPT-4] malformed contract revoked value fails closed (refused, not active)  decision=DENY_FALSE
GREEN CE45 [GLM-B] an unauthenticated witness does not mutate the authority lattice  authority_epoch 1->1
GREEN CE46 [GLM-C] a forged fresh-witness signature at commit voids the token  commit=FAILED_NO_EFFECT/['E-COMMIT-WITNESS-SIGNATURE-INVALID']
GREEN CE47 [GPT-MAJOR-2/GLM-D-E] validator: unresolved $ref fails closed; bool const/enum reject integer aliases  result=True
GREEN CE48 [DP-01] backslash traversal target is refused (WHATWG separator aliasing)  canonical=None
GREEN CE49 [DP-02] a denied request's nonce cannot be reused (fresh nonce still authorizes)  reuse=DENY_FALSE fresh=ALLOW
GREEN CE50 [DP-03] a commit fresh witness of a different identity/subject voids the token  commit=FAILED_NO_EFFECT/['E-COMMIT-WITNESS-IDENTITY-MISMATCH']
GREEN CE51 [DP-05] adjudicator signature payload excludes the top signature (non-circular)  acyclic_payload=True
GREEN CE52 [P7-02] trailing line-feed in a pattern field is refused (fullmatch, not re.search+$)  trailing-\n nonce
GREEN CE53 [P7-01] contract-body snapshot is immutable vs concurrent registry mutation  snapshot isolated
GREEN CE54 [P7-03] commit fresh witness bound to sequence/expiry/coverage/independence  all four void
GREEN CE55 [P7-04] nonce of an early-denied request cannot be reused by a linked retry  retry=DENY_FALSE
GREEN CE56 [P7-06/GLM] directory scope targetable; double-slash + control-char targets refused  ok
GREEN CE57 [P7-07] AMEND_AUTHORITY refused with reserved E-AMENDMENT-CLASS-UNIMPLEMENTED (honest v0.1 scope)  ['E-AMENDMENT-CLASS-UNIMPLEMENTED']

57/57 GREEN  (0 RED = open defects)

=== python3 bssg_model_check.py ===
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

MODEL CHECK: PASS -- kernel(243) + antitone(729) + operational refinement on the executable

=== python3 verify_bssg_v0_1.py ===
BSSG v0.1 DRAFT package verifier
Package directory: /mnt/data/bssg_v0_1_pass3_audit_pkg
------------------------------------------------------------------------
G1    PASS   all 10 required files and exactly 6 schemas present
G2    PASS   six schemas valid, closed, DRAFT-marked, five conjuncts
G3    PASS   339 tests passed, including 243 kernel truth states
G4    PASS   73 citation occurrences, all resolvable to the 34 listed references
G5    PASS   no prohibited effectiveness language outside the registry
G6    PASS   BCP 14 boilerplate present; MUST=87 MUST NOT=30 SHALL=13 SHOULD=10 MAY=5
G7    PASS   no em dash, en dash, or related characters in source files
G8    PASS   version 0.1 parity and DRAFT / NOT CARRIED status intact
G9    PASS   SHA256SUMS verified for 20 files
G10   WARN   12 open design decisions (OD-1, OD-2, OD-3, OD-4, OD-5, OD-6, OD-7, OD-8, OD-9, OD-10, OD-11, OD-12); decision register records STILL BLOCKING findings
------------------------------------------------------------------------
SUMMARY: 10 gates, 9 PASS, 1 WARN, 0 FAIL
PACKAGE STATUS: SELF-CONSISTENT DRAFT (not carried, not publication ready)

=== python3 bssg_attest.py BSSG-V08-AUDIT-GPT-caa8b05b4ecf8f48 ===
EXECUTION_ATTESTATION: accd2ed9142c9619f6add0a76a9243b05b713bcadff0b74d7466968b1360d9fe

=== dispatch-defined manifest recomputation ===
MANIFEST: 151cb3855f2f39ea80581d20371a8d52921eb28c96687553fa06c73a2a5b1196
CHALLENGE: 498de390625988d61406623dd7ddac5b9ecd8b6ab4c74cf65a513722d3a66b1f

---

# Bismillah ir-Rahman ir-Rahim
