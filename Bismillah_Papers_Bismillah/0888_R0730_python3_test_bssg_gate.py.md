# Bismillah ir-Rahman ir-Rahim

# R0730 -- python3 test_bssg_gate.py

**Chronological Index:** 888 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** pass32_all_outputs.txt  
**Source Format:** txt  
**SHA-256:** `3ef722e4c19c934c79e30088bbf0af7b9897a72ffebb100061742f6e1bfc67b6`  

---

## R0730 · python3 test_bssg_gate.py

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: pass32_all_outputs.txt
- source_format: txt
- text_sha256: 3ef722e4c19c934c79e30088bbf0af7b9897a72ffebb100061742f6e1bfc67b6

===== python3 test_bssg_gate.py =====
.........................................................................................................................................................................................................................................................................................................................................................
----------------------------------------------------------------------
Ran 345 tests in 0.157s

OK
[exit=0]

===== python3 bssg_counterexamples.py =====
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
GREEN CE39 [F-05] token-factory collision: kernel-consistent ALLOW record but FAILED_NO_EFFECT, no redeemable token  2nd=ALLOW issuance=FAILED_NO_EFFECT tokens=1
GREEN CE40 [F-06] a contract revoked after authorization voids the token at commit  commit=FAILED_NO_EFFECT/['E-COMMIT-CONTRACT-REVOKED']
GREEN CE41 [GLM-A] recovering token factory: collision snapshot stays terminal (no allow-after-deny)  d1=ALLOW/FAILED_NO_EFFECT d2=DENY_FALSE
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
GREEN CE58 [DP-G3a] commit fresh witness revalidates within-authority (unsafe value voids)  ['E-COMMIT-WITNESS-WITHIN-AUTH']
GREEN CE59 [DP-G3b] commit fresh witness revalidates observed_at (future voids)  ['E-COMMIT-WITNESS-CLOCK-AMBIGUOUS']
GREEN CE60 [DP-G1a] bare authority-root directory target is admissible; double-slash still refused  ok
GREEN CE61 [DP-GPT-01] C1 control characters are refused in targets  none accepted
GREEN CE62 [DP-GPT-08] malformed contract registry entry fails closed (no crash)  decision=DENY_UNKNOWN
GREEN CE63 [DP-GPT-06] a contract mutated after authorization voids at commit (digest re-verified)  ['E-COMMIT-CONTRACT-DIGEST-CHANGED']
GREEN CE64 [DP-GPT-09] a contract expired before commit voids the token  ['E-COMMIT-CONTRACT-EXPIRED']
GREEN CE65 [DP-GPT-07] an invalid commit-time time-authority signature voids the token  ['E-COMMIT-TIME-AUTHORITY-SIGNATURE-INVALID']
GREEN CE66 [DP-GPT-02] a supplied commit evidence_epoch != bound epoch voids  ['E-COMMIT-EVIDENCE-EPOCH-MISMATCH']
GREEN CE67 [DP-GPT-10] validated commit evidence is persisted; older sequence cannot re-authorize  later=DENY_FALSE
GREEN CE68 [DP-GPT-05] per-epoch witness sequence: a new epoch's sequence is not compared to an older epoch  d2=ALLOW d3=ALLOW
GREEN CE69 [F-GPT-P10-01] returned records are deep copies; a mutated receipt cannot substitute the committed effect  alias=False commit=FAILED_NO_EFFECT
GREEN CE70 [F-GPT-P10-02] lift requires a concrete subject domain; adjudicator in it is not independent  ok
GREEN CE71 [F-GPT-P10-03] commit re-derives policy, rejects non-dict evidence, applies TA semantics  ok
GREEN CE72 [F-GPT-P10-04] malformed policy/registry fail closed (no crash); a post-reserve clock fault lands in VOID  ok
GREEN CE73 [P1-P4/GLM-F1/F2] returned/stored records (deny, execution, amendment) are deep copies, not caller-mutable aliases  deny=True exec=True
GREEN CE74 [P5/P3-01] caller evidence is snapshotted; witness_covered_classes is not stored by reference  aliased=False
GREEN CE75 [P3-02] stale evidence cannot redeem a still-unexpired token (age enforced at commit)  ['E-COMMIT-EVIDENCE-STALE']
GREEN CE76 [P3-05] a DEGRADED-authorized token commits under an equally DEGRADED fresh witness (no over-rejection)  ok
GREEN CE77 [P6-P8/GLM-F3/P3-04] malformed policy/contract and evaluator faults map to DENY_UNKNOWN with a recorded decision (no crash)  r1=DENY_UNKNOWN r2=DENY_FALSE r3=DENY_UNKNOWN rec=True
GREEN CE78 [F-GPT-V11-01] input is snapshotted into fresh JSON; post-decision caller mutation is inert; non-serializable input fails closed  bound_ok=True closed=True
GREEN CE79 [F-GPT-V11-04] a non-Boolean verifier result (0) is treated as an invalid signature, not valid  decision=DENY_FALSE
GREEN CE80 [F-GPT-V11-05] a reentrant authorize call is refused (no stale-snapshot authorization)  nested=DENY_UNKNOWN
GREEN CE81 [GLM-F1/P10] a fault in commit or amendment maps to a recorded failure, never escapes (totality)  commit=True amendment=True
GREEN CE82 [F-BSSG-P12-03] a caller copy-hook fired during input snapshot hits the reentrancy guard (not a nested op)  nested=DENY_UNKNOWN
GREEN CE83 [F-BSSG-P12-02] a str-subclass token id (malicious __hash__) fails closed with no escape  ok
GREEN CE84 [F-BSSG-P13-GPT-01] a completed ALLOW's nonce is NOT erased by a later aborted authorize (no replay -> no second token)  first=ALLOW nonce_kept=True replay=DENY_FALSE
GREEN CE86 [F-BSSG-P13-GPT-02] malformed evidence does not suppress a knowable-FALSE conjunct (FALSE dominates -> DENY_FALSE)  decision=DENY_FALSE
GREEN CE87 [F-BSSG-P13-GPT-03] a token-factory collision preserves the evaluated conjuncts, not fabricated all-FALSE  conjuncts=['TRUE', 'TRUE', 'TRUE', 'TRUE', 'TRUE']
GREEN CE88 [F-BSSG-P13-GPT-06] a token-mint abort does NOT rewind authenticated authority/epoch state; a later request still authorizes  abort=ALLOW/FAILED_NO_EFFECT later=ALLOW
GREEN CE85 [GLM-F1] an amendment abort (reentrant) is recorded to the audit trail (symmetry with authorize/commit)  amd=['E-REENTRANT-CALL'] recorded=True
GREEN CE89 [GPT-01] clock-fault abort after nonce consumption is terminal (no allow-after-abort)  1st=DENY_UNKNOWN retry=DENY_FALSE
GREEN CE90 [GPT-02] authenticated monotonic state is not rewound by a token-mint abort  no-rollback of security-monotonic state
GREEN CE91 [GPT-03] evidence-independent target FALSE dominates on the malformed-evidence path  decision=DENY_FALSE TargetAllowed=FALSE
GREEN CE92 [GPT-06] forged ALLOW receipt is mechanically caught by the X8 checker  forged_violations=['X8', 'X8']
GREEN CE93 [GPT-07] ordinary rejected amendment appends a correction-outcome record  recorded=True
GREEN CE94 [KIMI-P15-05] a factory token below the receipt schema minLength is refused  decision=ALLOW/FAILED_NO_EFFECT
GREEN CE95 [GPT-01] collision issuance-failure projects DENIED on the subject plane, not AUTHORIZED  subject=DENIED
GREEN CE96 [GPT-02] evidence-independent EvidenceCurrent FALSE (expiry) dominates on the malformed path  decision=DENY_FALSE
GREEN CE97 [GPT-05] every amendment rejection branch records exactly one correction-outcome
GREEN CE98 [GPT-03] reentrant refusal does not contaminate the outer snapshot (no allow+denied on one snapshot)  outer_denied=False
GREEN CE99 [GPT-04] post-admission abort record is kernel-consistent (ALLOW+FAILED_NO_EFFECT), preserves conjuncts + authority  decision=ALLOW/FAILED_NO_EFFECT epoch=1 snap=True
GREEN CE100 [GPT-08] X4 keys on redemption outcome (failed attempts are not double-redemption)  no_false_positive=True flags_real=True
GREEN CE101 [GPT-06] X8 requires reason_codes present and == [] (absent/None is a violation)
GREEN CE102 [GPT-07] X7 flags same-epoch ceiling widening (change without an epoch bump)
GREEN CE103 [A-P17] X7 sound on real records; health-only bump OK; V29 withdrawal: armed amendment re-widen is X7U (uncertifiable, grant inert); tamper/divergence still X7  real=True healthonly=True widen_noamend=True amend_anchored=True amend_unanchored_x7=True tamper=True
GREEN CE104 [B-P17] X4 redemption set derived from schema enum; double-SUCCEEDED flagged; settle-chain is one redemption  set_ok=True dbl=True chain=True failed_noeffect=True
GREEN CE105 [C-P17] reentrant refusal records all-UNKNOWN (not outer conjuncts) and is kernel-consistent  nested_conjuncts_all_unknown=True consistent=True decision=DENY_UNKNOWN
GREEN CE106 [D-P17] authorized_issuance provenance-consistent + total; forgeries fail closed; genuine projects; bound binds  min=False nocj=False false=False real=True unbound_rejected=True
GREEN CE107 [E-P17] post-admission mint abort is a kernel-consistent issuance-failure record (E)  decision=ALLOW/FAILED_NO_EFFECT kernel_evaluated=True
GREEN CE108 [F-P17] model projection predicate: an issuance-failure ALLOW is not authorized (not modeled AUTHORIZED_UNUSED)  authorized=False
GREEN CE109 [G-P17] expired request under a schema-valid-but-indeterminate bundle is DENY_FALSE (evidence-independent expiry)  decision=DENY_FALSE
GREEN CE110 [H-P17] clock-unavailable failure receipt is schema-valid (null commit_time + E-CLOCK-UNAVAILABLE)  schema_valid=True commit_time=None
GREEN CE111 [ATTEST-P18] execution attestation is not forgeable by a constant trace; varies by nonce; deterministic  forged_matches=False varies=True
GREEN CE112 [D1-P18] authorized_issuance is total (fails closed, never raises on malformed input)  all_false=True
GREEN CE113 [D2-P18] record<->receipt binding: a provenance-transplanted receipt is not authorized  genuine=True splice_static=False splice_bound=False
GREEN CE114 [D3-P18] expired UNUSED token is not bound-authorized (unexpired now enforced)  before=True after=False
GREEN CE115 [A1-P18] V29 withdrawal: an armed re-widen is X7U with or without the grant (survives a snapshot-less deny); a no-amendment widening control is still X7  anchored=True unanchored_x7=True control_x7=True
GREEN CE116 [A2-P19] V29 withdrawal: a gate-issued marker re-widen is X7U (grant inert); a forged/raw marker does NOT arm -> its widening is a grant-independent X7  forged=['X7'] anchored=True unanchored_x7=True raw=['X7']
GREEN CE117 [A3-P18] X7 full-triple divergence (session/epoch/snapshot) is flagged  result=['X7', 'X7', 'X7']
GREEN CE118 [B1-P18] X4 flags PENDING->FAILED_NO_EFFECT->SUCCEEDED (two contradictory terminals); a single settlement is clean  chain=['X4'] single=[]
GREEN CE119 [B2-P18] REDEMPTION_OUTCOMES derived from schema enum; out-of-enum outcome flagged (not silently skipped)  derived=True lowercase_flagged=True
GREEN CE120 [INTERVAL-P18] inverted request interval (issued_at > expires_at) is DENY_FALSE, never ALLOW  decision=DENY_FALSE
GREEN CE121 [INTERVAL-P18] inverted witness lease (observed_at > expires_at) yields WitnessHealthy=FALSE, not ALLOW  decision=DENY_FALSE wh=FALSE
GREEN CE122 [K18-12-P18] X7/X4 are total: malformed records are skipped/flagged, never raised on  x7=['X7'] x4=[]
GREEN CE124 [CLOCK-P19] strict clock reader: string/float/bool/negative fail closed on every path (authorize + success commit)  commit_time=None '1784980800'->DENY_UNKNOWN 1784980800.75->DENY_UNKNOWN True->DENY_UNKNOWN -999->DENY_UNKNOWN None->DENY_UNKNOWN
GREEN CE125 [A3-P19] X7 divergence is type-strict: bool epoch does not alias int; non-dict snapshot is flagged  bool_epoch=['X7'] nondict_snapshot=['X7']
GREEN CE126 [A4-P19] X4/A4: unresolved or mismatched execution-receipt epoch binding fails closed (X7)  unresolved=['X7']
GREEN CE127 [INTERVAL-P19] commit-time fresh-witness inverted lease (observed_at > expires_at) is refused, not PASS  outcome=FAILED_NO_EFFECT reasons=['E-COMMIT-WITNESS-LEASE-INVERTED']
GREEN CE128 [A2-P19] V29 withdrawal: a gate-issued marker re-widen is X7U (anchored==unanchored); a raw/forged marker does NOT arm -> grant-independent X7  anchored=['X7U'] unanchored=['X7U'] raw=['X7'] forged=['X7']
GREEN CE129 [K18-12-P19] X7 fails closed (no crash) on an unhashable nested-list element  result=['X7']
GREEN CE123 [F-P18] pre-admission reentrant refusal is kernel_evaluated=False with all-UNKNOWN conjuncts  kernel_evaluated=False reasons=['E-REENTRANT-CALL']
GREEN CE130 [X4-P20] X4 flags a double redemption with an unhashable token id (fail closed, not skipped)  double=['X4'] single=[]
GREEN CE131 [A4-P20] settlement execution receipt omitting authority_epoch fails closed (A4 omission)  omitted=['X7']
GREEN CE132 [A2-P20] V29 withdrawal: a bound gate marker re-widen is X7U (grant inert); an UNBOUND marker does NOT arm -> grant-independent X7  bound=['X7U'] bound_unanchored=['X7U'] unbound=['X7']
GREEN CE133 [CLOCK-P20] strict clock reader rejects an out-of-range upper-bound clock value  raised_ClockFault=True
GREEN CE134 [X4-P21] X4 flags a distinct-NaN double redemption (no float laundering across a merge)  double=['X4'] single=[]
GREEN CE135 [A2-P21] X7 marker binding is identity-complete: A's event cannot license B's widening  cross_session=['X7']
GREEN CE136 [A2-P21] X7 consumes a correction once: a replayed (consumed) marker does not re-arm -> grant-independent X7; the single armed re-widen is X7U (grant inert)  replay=['X7U', 'X7', 'X7'] legit=['X7U'] legit_unanchored=['X7U']
GREEN CE137 [A2-P21] X7 marker cannot retro-bind to an event appearing later in the stream  future_event=['X7']
GREEN CE138 [X4-P22] X4 materializes input: a hostile str-subclass token id cannot launder a double redemption  subclass_double=['X4']
GREEN CE139 [X7-P22] X7 materializes input: a hostile str-subclass session_id cannot hide a widening  subclass_widen=['X7']
GREEN CE140 [A2-P22] marker authority_epoch tamper-checked (bogus low/inflated -> grant-independent X7); the honest armed re-widen is X7U (grant inert)  low=['X7', 'X7U'] hi=['X7', 'X7U'] legit=['X7U'] legit_unanchored=['X7U']
GREEN CE141 [X4-P23] X4 strict materialization: a hostile flipping __iter__ list cannot erase a double redemption  benign_first=['X4'] hostile_first=['X4']
GREEN CE142 [DP-P23] subject_facing/authorized_issuance fail closed on a two-view hostile dict subclass  subject_facing=DENIED authorized_issuance=False
GREEN CE143 [A2-P23] marker installs an epoch floor (a regression below it is a grant-independent X7); the honest armed re-widen is X7U (grant inert)  attack=['X7', 'X7U'] legit=['X7U'] legit_unanchored=['X7U']
GREEN CE144 [X4-P24] X4 strict-materializes first: a tuple/non-list outer sequence fails closed; None is clean  tuple=['X4'] none=[]
GREEN CE145 [A2-P24] V29 withdrawal: the landing is NOT certified offline -- a relocated armed re-widen is X7U (grant inert), enforced online  over=['X7U'] legit=['X7U'] legit_unanchored=['X7U']
GREEN CE146 [A2-P24] under verify, a bad top-level correction signature does NOT arm -> grant-independent X7; the armed verified re-widen is X7U (grant inert)  reject_top=['X7'] all_ok=['X7U'] all_ok_unanchored=['X7U']
GREEN CE147 [DP-P24] projection sites (subject_facing/authorized_issuance) use strict materialization  subject_facing=DENIED authorized_issuance=False
GREEN CE148 [X4-P25] X4 fails closed (no crash) on an unhashable list/dict outcome  list=['X4'] dict=['X4']
GREEN CE149 [X7-P25] X7 fails closed on a present but wrong-typed (float) authority_epoch  float_epoch=['X7']
GREEN CE150 [X4-P25] X4 numeric keyspace: int 1 and float 1.0 are one token (double redemption caught)  numeric_double=['X4']
GREEN CE151 [DP-P25] authorized_issuance_bound uses strict materialization (rejects an authorized subclass)  bound_subclass=False
GREEN CE152 [X7-P26] CONFORMANCE: a real gate re-widen is X7U (anchored==unanchored, grant inert); marker licensed_epoch==authority_epoch+1; a forged WIDE @marker-epoch is X7U (relocation online-only)  real_anchored=True real_unanchored_x7=True plus1=True(le=3,me=2) honest_clean=True forged_caught=True
GREEN CE153 [X7-P26] V29 withdrawal: a forged WIDE @marker-epoch and the honest armed re-widen are both X7U (relocation/landing not certified offline)  forged_at_marker=True honest_anchored=True honest_unanchored=True
GREEN CE154 [K-P26] kernel FALSE-domination survives an exception: expired+raising request is DENY_FALSE, not DENY_UNKNOWN  expired_false=True fresh_unknown=True dec=DENY_FALSE
GREEN CE155 [X7-P27] V29 withdrawal: a relocated armed re-widen (far/marker-epoch) is X7U; the honest armed re-widen is X7U (grant inert)  far=True reopen=True honest=True honest_unanchored=True forged=True
GREEN CE156 [K-P27] kernel abort preserves FALSE-domination for every evidence-independent conjunct, via the stashed clock read  effecttype_false=True expired_via_stashed=True indeterminate_unknown=True
GREEN CE157 [X7-P28] V29 withdrawal: the landing is NOT certified offline -- dual-field + walk-up relocations are X7U; the honest armed re-widen is X7U (grant inert)  dual=True dual_verify=True walkup=True honest=True honest_unanchored=True
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

168/168 GREEN  (0 RED = open defects)
[exit=0]

===== python3 bssg_model_check.py =====
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
PASS BOUNDED-AUTH-INTRO: over ALL schedules (len<=3, 5-op alphabet) no ALLOW authorizes an effect outside the established healthy ceiling (Axiom-3/R_may closure of GPT-P30-01)  schedules=155 allows=48

MODEL CHECK: PASS -- kernel(243) + antitone(729) + bounded-auth-intro(155 schedules) + operational refinement on the executable
[exit=0]

===== python3 verify_bssg_v0_1.py =====
BSSG v0.1 DRAFT package verifier
Package directory: /mnt/data/bssg_pass32_audit_work/bssg_v0_1_pass32_audit_gpt
------------------------------------------------------------------------
G1    PASS   all 10 required files and exactly 6 schemas present
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
G13   PASS   counterexample corpus EXECUTED: 168/168 GREEN, 0 RED (independently counted; self-report matches)
------------------------------------------------------------------------
SUMMARY: 13 gates, 12 PASS, 1 WARN, 0 FAIL
PACKAGE STATUS: SELF-CONSISTENT DRAFT (not carried, not publication ready)
[exit=0]

===== python3 bssg_gate.py =====
BSSG reference gate 0.1.0-draft, spec version 0.1
DRAFT / NOT CARRIED. No effectiveness claim is made by this software.
[exit=0]

===== sha256sum -c SHA256SUMS =====
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
[exit=0]

===== python3 bssg_attest.py BSSG-V30-AUDIT-GPT-34c29290a93557cc =====
EXECUTION_ATTESTATION: e3349f1c411b2df43c438004cd8325d481ab479e59034fe61eee91c76fcb8966
[exit=0]

---

# Bismillah ir-Rahman ir-Rahim
