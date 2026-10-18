# Bismillah ir-Rahman ir-Rahim

# R0347 -- SHVVP Amendment and Adjudication Record

**Chronological Index:** 338 of 995  
**Date:** 2026-07-24  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** SHVVP_v0_5_AMENDMENT_AND_ADJUDICATION_RECORD.md  
**Source Format:** md  
**SHA-256:** `b377ef0efe9de2d1a693d0ece6bc9e7bbadca6f131be8361a6d9958a4f2190fd`  

---

## R0347 · SHVVP Amendment and Adjudication Record

- section: V. BSSG & SHVVP Protocols
- source_file: SHVVP_v0_5_AMENDMENT_AND_ADJUDICATION_RECORD.md
- source_format: md
- text_sha256: b377ef0efe9de2d1a693d0ece6bc9e7bbadca6f131be8361a6d9958a4f2190fd

# SHVVP Amendment and Adjudication Record

**Append-only record for the Structural Honesty Validation Protocol (SHVVP).** This file is the standalone companion to Section 13 of the frozen contract. It records every version, every finding filed against every version, and the disposition of each finding, including REJECTED findings and including a carrying PASS that did not carry. Entries are appended, never edited or deleted. Where this file and the frozen contract differ in wording, the frozen contract governs the conduct of the study and this file governs the audit history.

**Standing.** Prepared by the producer and editor of v0.5, who are ADVISORY and NON-CARRYING. Nothing in this file constitutes a carrying verdict on v0.5.

---

## 1. Version register

| Version | Freeze date | Status | Deposited? | Carrying audit outcome |
|---|---|---|---|---|
| v0.1 | 2026-07-24 | **HALTED**, superseded, retained as historical record | NO, never deposited as a binding preregistration | DIVERGENT: GPT-class HALT (six findings), Gemini-class PASS-WITH-AMENDMENTS (three findings) |
| v0.2 | 2026-07-24 | **HALTED**, superseded, retained as historical record | NO, never deposited as a binding preregistration | DIVERGENT: GPT-class **HALT** (four HIGH and BLOCKING findings), Gemini-class **PASS** (zero findings) |
| v0.3 | 2026-07-24 | **HALTED**, superseded, retained as historical record | NO, never deposited as a binding preregistration | DIVERGENT: GPT-class **HALT** (six findings, five HIGH and BLOCKING, one MEDIUM), Gemini-class **PASS** (zero findings) |
| v0.4 | 2026-07-24 | **HALTED**, superseded, retained as historical record | NO, never deposited as a binding preregistration | **HALT** from the GPT-class carrying seat (three findings, two HIGH and BLOCKING); no Gemini-class verdict returned at the v0.5 freeze. A HALT from either carrying seat blocks deposit outright |
| v0.5 | 2026-07-24 | FROZEN, NOT DEPOSITED, NOT BINDING | NO | NONE YET. A fresh carrying audit by one GPT-class and one Gemini-class non-producer seat is required before deposit |

**None of v0.1, v0.2, v0.3 and v0.4 is deposit-ready, and none may ever be described as deposit-ready or binding.** All four ship unmodified in this release for lineage, together with all seven carrying-seat reports and the v0.4 producer completion report.

---

## 2. Round 1 (v0.1): findings and dispositions, preserved

The full round 1 register is preserved in the v0.2 amendment record, which is itself preserved in Section 13 of the v0.3 contract. In summary: GPT F-PP-1 through F-PP-6 were accepted (F-PP-6 as a precision fix); Gemini F-PP-1's concern was accepted while its proposed variance-derived margin formula was REJECTED IN PART on EMA grounds; Gemini F-PP-2 was merged into GPT F-PP-2 at the higher severity; Gemini F-PP-3 was REJECTED on the Anthropic primary record; and the chair's method-paper DOI note was RESOLVED. Both round 1 rejections were independently adjudicated as CORRECT by both round 2 seats.

---

## 3. Round 2 (v0.2): findings and dispositions

Four findings were filed by the GPT-class seat. The Gemini-class seat filed none and returned PASS.

| Finding | Seat | Severity as filed | Adjudication | Absorbed at | Amendment entry |
|---|---|---|---|---|---|
| F-P2-1 | GPT-class (Seat A) | HIGH, BLOCKING | **ACCEPTED IN FULL** | Contract Sections 6.5, 6.5.1 and 6.8; the v0.2 simulation is WITHDRAWN and replaced by `shvvp_v0_5_power_sim.py` | A-3.1 |
| F-P2-2 | GPT-class | HIGH, BLOCKING | **ACCEPTED IN FULL** | Contract Sections 6.4 and 6.6; `phase_b_label` in `shvvp_v0_5_decision_rules.py` | A-3.2 |
| F-P2-3 | GPT-class | HIGH, BLOCKING | **ACCEPTED IN FULL** | Contract Sections 8.1 to 8.4 and the family table in 6.8; `shvvp_v0_5_route_inference.py` | A-3.3 |
| F-P2-4 | GPT-class | HIGH, BLOCKING | **ACCEPTED IN FULL** | Contract Sections 7.4 and 7.5; `phase_c_label` | A-3.4 |
| PASS with zero findings | Gemini-class (Seat B) | Not a finding | **PRESERVED IN FULL, NOT OVERWRITTEN** | Contract Section 0.3 divergence adjudication | A-3.5 |

### 3.1 Detail: F-P2-1, the simulation did not implement the frozen rule

The seat established three separate mismatches between the frozen text and the shipped v0.2 script: plain percentile bounds where the contract froze BCa; an undeclared 0.5 continuity correction on the risk ratio; and joint power computed as the product of two independently simulated marginal powers rather than as the probability of the conjunction. All three are accepted. The replacement script implements genuine two-sided 95 percent BCa cluster-bootstrap intervals for RD, RR and DeltaS on a shared resampled cell set, applies no continuity correction anywhere, predeclares zero-event and degeneracy handling as frozen rules Z-1 through Z-4, simulates E1 and E2 session outcomes jointly through a Gaussian copula with a frozen within-session correlation of 0.30, and estimates joint power as the share of replicates receiving the SUCCESS label from the Section 6.4 mapping.

**Consequence: the frozen confirmatory design grew from 1,280 to 1,440 sessions.**

| Design | Sessions | Joint power under the correctly implemented rule | 95 percent Monte Carlo interval | Meets the frozen selection rule? |
|---|---|---|---|---|
| 8 repetitions (the v0.2 size) | 1,280 | 0.800 | [0.785, 0.814] | NO, the lower bound is below 0.80 |
| **9 repetitions (the v0.3 size)** | **1,440** | **0.871** | **[0.859, 0.883]** | **YES, and it is the smallest such design** |
| 10 repetitions | 1,600 | 0.911 | [0.901, 0.921] | Yes, but larger than necessary |

The frozen selection rule is now explicit and was applied mechanically: the smallest ladder design whose confirmation-stage joint power has a 95 percent Monte Carlo lower bound at or above 0.80. Boundary calibration at the frozen design gives a realized one-sided error of 0.0247 for rule N at a true difference of exactly the margin and 0.0127 for rule H at its joint boundary, against a nominal 0.025, so the frozen bootstrap-t switch is not triggered by the design simulation.

### 3.2 Detail: F-P2-2, the Phase B label set was not closed

v0.2 declared five labels and then created a sixth in a later subsection, leaving the same data readable two ways. The remedy is one total ordered mapping over eight labels, with rules H and N evaluated in both ASA and PP, with population discordance defined exactly and given its own two labels, and with a new label for the state in which the frozen zero-event rules make the harm interval not estimable. The reverse discordance pattern, failure in ASA with success in PP, is declared to be an observed failure rather than an inconclusive state, because that is the pattern a motivated analyst would prefer to call inconclusive. The mapping is executable and its totality is proved by enumeration over all 256 input combinations.

### 3.3 Detail: F-P2-3, Benjamini-Hochberg was invoked without any test

v0.2 attached BH at q = 0.05 to all six routes while freezing no null, statistic, unit, clustering, sidedness or p-value construction. The remedy does not manufacture tests where none is admissible. Phase A is a single-case construct validation whose own inferential honesty clause forbids across-condition testing, and two Phase C components have no randomised comparator. Those six components are reclassified as Class G gates that support descriptive claims only, and **BH is declared not to apply to them**. The five components that are genuine one-sample proportions on randomised, clustered sessions become Class I, each with a frozen null, a frozen statistic, a frozen null-centred cluster-bootstrap p-value, a frozen evaluability threshold, and a hard gate that fails the route regardless of any p-value. Family F3 is split into F3a and F3b accordingly, and cross-phase combination is by conjunction only, with every p-value combination method prohibited.

### 3.4 Detail: F-P2-4, Phase C had no priority order

v0.2 listed four labels with no rule for a conjunct failing while UNKNOWN also exceeded its cap or while adjudicator reliability failed, and did not bind alpha into the pass expression. The remedy is a total priority order over five labels in which a HARD OBSERVED FAILURE dominates both inconclusive states, adjudication failure dominates UNKNOWN domination, and UNKNOWN domination dominates the new tentative reliability band. A failure of an adjudicated conjunct whose own alpha is below 0.67 is expressly not a hard failure, because an inadmissible adjudication cannot establish an observation. PASS-ALL-SIX is reachable only through the last clause and therefore structurally requires minimum alpha at or above 0.80; the 0.67 to below 0.80 band yields INCONCLUSIVE-TENTATIVE-RELIABILITY and can never support a pass or a novelty claim.

### 3.5 Detail: A-3.5, the Gemini-class PASS

The Gemini-class seat returned PASS with zero findings and is recorded as filed. It is not reinterpreted as an error, and its report ships unmodified. That seat verified chain of custody, both anchors, all arithmetic identities, scope honesty, the mechanical checks and the visual render, and reached the same conclusions as the GPT-class seat on every one of them. It also recorded its own limits: it did not write or modify code to verify the power simulation, relying on the shipped receipt, and it did not re-derive the design size. Those are exactly the questions on which the other seat found four gaps. Under the frozen carrying rule, convergence requires both non-producer families to agree; a PASS from one family neither carries nor cures the other family's HALT. v0.2 is HALTED because the seats diverged, not because either seat is disregarded.

---

## 4. v0.3 amendment entries

The authoritative text of entries A-3.1 through A-3.9 is Section 13 of `SHV_VALIDATION_PROTOCOL_v0_5_source.md`. Enumerated here for cross-reference completeness.

| Entry | Origin | Disposition | Substantive? |
|---|---|---|---|
| A-3.1 | GPT F-P2-1 | ACCEPTED IN FULL. Simulation replaced; design grew to 1,440 sessions | YES, blocking |
| A-3.2 | GPT F-P2-2 | ACCEPTED IN FULL. One total ordered mapping over eight labels | YES, blocking |
| A-3.3 | GPT F-P2-3 | ACCEPTED IN FULL. Route inference frozen; F3 split into F3a and F3b | YES, blocking |
| A-3.4 | GPT F-P2-4 | ACCEPTED IN FULL. Phase C total priority order; alpha bound into the pass | YES, blocking |
| A-3.5 | Gemini-class PASS | PRESERVED, NOT OVERWRITTEN | Governance record |
| A-3.6 | Producer, in response to the pattern of both rounds | RECORDED. Executable-rule commitment: every ambiguous rule ships as code with tests | YES |
| A-3.7 | Producer | AMENDED. New residual UNKNOWN for route evaluability counts; calibration UNKNOWN narrowed | YES, minor |
| A-3.8 | Producer | ADDED. Methodological citations for BCa and cluster resampling | YES, citation |
| A-3.9 | Governance | RECORDED. v0.1 and v0.2 HALTED, never deposited, not binding; v0.3 uncarried | Governance record |

---

## 4b. Round 3 (v0.3): findings and dispositions

Six findings were filed by the GPT-class seat, five HIGH and BLOCKING and one MEDIUM. The Gemini-class seat filed none and returned PASS. **The producer reproduced all six against the shipped v0.3 code before adjudicating, and none was factually in error.** No finding was downgraded because the other seat passed the artifact.

| Finding | Seat | Severity as filed | Adjudication | Absorbed at | Amendment entry |
|---|---|---|---|---|---|
| F-P3-1, the frozen route p-value is severely anti-conservative on degenerate clusters: 0.00009999 returned where the exact boundary probability is 0.36417, and again where it is 0.21464 | GPT-class (Seat A) | HIGH, BLOCKING | **ACCEPTED IN FULL. The construction is WITHDRAWN, not patched** | Contract Sections 8.0, 8.2, 8.3, 8.5; `shvvp_v0_5_route_inference.py`; v0.3 test T10 withdrawn with it | A-4.1 |
| F-P3-2, registry minimum evaluable counts unenforced and caller-injectable evaluability and p-values | GPT-class | HIGH, BLOCKING | **ACCEPTED IN FULL** | Contract Sections 6.8, 8.3, 8.4; `evaluate_component` | A-4.2 |
| F-P3-3, a NaN adjudicator alpha returned PASS-ALL-SIX with conjunct C1 failed | GPT-class | HIGH, BLOCKING | **ACCEPTED IN FULL** | Contract Section 7.5; `phase_c_label` | A-4.3 |
| F-P3-4, two stray outcome names outside the closed eight-label Phase B list | GPT-class | HIGH, BLOCKING | **ACCEPTED IN FULL** | Contract Sections 6.2, 6.3, 6.4; `GUARD_ANNOTATIONS` | A-4.4 |
| F-P3-5, Section 11 still froze the withdrawn 1,280-session confirmatory run | GPT-class | HIGH, BLOCKING | **ACCEPTED IN FULL** | Contract Section 11; `shvvp_v0_5_regression_scan.py`; verifier gate G13 | A-4.5 |
| F-P3-6, the documented reproduction command did not reproduce the receipt, and standalone stages silently used 8 repetitions | GPT-class | MEDIUM | **ACCEPTED IN FULL** | Contract Section 6.8; `shvvp_v0_5_power_sim.py` | A-4.6 |
| PASS, zero findings | Gemini-class (Seat B) | Not a finding | **PRESERVED IN FULL, NOT OVERWRITTEN** | Contract Section 0.3; `SHVVP_v0_3_SEAT_B_GEMINI_VERDICT.md` shipped unmodified | A-4.7 |

**Round 3 divergence, adjudicated.** Both seats verified custody, anchors, arithmetic, the 256-state Phase B enumeration, the BH step-up and scope honesty, and agreed. They diverged on whether the shipped inferential machinery was VALID as distinct from executable. The GPT-class seat executed the frozen p-value on an all-successful cluster set and found it anti-conservative by more than three orders of magnitude at the decision boundary; the Gemini-class seat validated the design from the deterministic receipt and did not construct that case. Divergence blocks deposit regardless of which seat is more nearly right. **A finding that a shipped test is invalid outranks a finding that a rule is ambiguous, because an invalid test produces a number that looks like evidence.**

**Substantive judgement recorded for audit.** Absorbing F-P3-1 required changing the estimand scale from an item share to a cluster-level all-required-events probability, which made the v0.3 nulls unusable as stated: 0.98 cannot be rejected by a perfect result at any feasible cluster count. The nulls were therefore re-anchored (R2-B 0.90, R4-B and R4-C 0.80, R6-B and R6-C 0.85) under a new attainability requirement, and the former near-perfect thresholds were retained as hard and descriptive gates carrying no inferential support. This is the most contestable judgement in v0.4 and is flagged as such to the carrying seats rather than presented as routine.

---

## 4c. v0.4 amendment entries

Entries A-4.1 through A-4.11 are recorded verbatim in Section 13 of the frozen contract and are not duplicated here in full. In summary: A-4.1 withdraws the bootstrap p-value and freezes the exact binomial boundary test with a Clopper-Pearson bound and re-anchored attainable nulls; A-4.2 binds all component evidence into one fail-closed function; A-4.3 adds Phase C input validation with fail-closed mapping; A-4.4 converts the two stray names into a closed guard annotation vocabulary; A-4.5 fixes Section 11 and adds a contextual regression scan; A-4.6 makes the documented reproduction command actually reproduce the receipt; A-4.7 preserves the Gemini-class PASS unmodified; A-4.8 records the general fail-closed commitment; A-4.9 adds two methodological citations; A-4.10 records that v0.1 through v0.3 are HALTED and never deposited; A-4.11 records that no estimand, threshold, margin, interval algorithm, corpus size or anchor fact changed in this version, evidenced by a receipt payload identical to v0.3's.

---

## 4d. Round 4 (v0.4): findings and dispositions

Round 4 was a focused-delta re-audit. The GPT-class carrying seat returned **HALT** with three findings. No Gemini-class verdict had been returned at the time of this freeze; under the frozen carrying rule a HALT from either carrying seat blocks deposit outright, so v0.4 is HALTED regardless. **The producer accepts all three findings in full and reproduced the decisive behaviour before adjudicating.**

| Finding | Seat | Severity as filed | Adjudication | Absorbed at | Amendment entry |
|---|---|---|---|---|---|
| F-P4-1, the fail-closed evidence binding was bypassable three ways: caller-asserted hard-gate state with catastrophic raw counts, direct construction with the importable token, and `dataclasses.replace` on a genuine below-minimum object | GPT-class (Seat A) | HIGH, BLOCKING | **ACCEPTED IN FULL** | Contract Sections 8.2, 8.3, 8.6; `shvvp_v0_5_route_gates.py`, which admits raw evidence only | A-5.2 |
| F-P4-2, the exact binomial route inference assumed an iid cluster model that the fixed heterogeneous paired design does not support | GPT-class | HIGH, BLOCKING | **ACCEPTED IN FULL. ALL ROUTE-LEVEL INFERENCE WITHDRAWN** | Contract Sections 0.2, 6.8, 8.0 to 8.6; every component reclassified Class G descriptive | A-5.1 |
| F-P4-3, deposit metadata misidentified the frozen version in its title, description opening and intended-files list | GPT-class | MEDIUM | **ACCEPTED** | `DEPOSIT_METADATA_v0_5.md`; verifier gate G19; current-version parity tests | A-5.3 |

**Round 4 adjudication, recorded plainly.** The seat's regression table recorded F-P3-3, F-P3-4 and F-P3-5 as ABSORBED, F-P3-6 as implementation-absorbed with the full-run attestation stopped at a checkpoint after a blocker was established, F-P3-1 as PARTIALLY ABSORBED, and F-P3-2 as NOT ABSORBED. Both remaining defects are cured in v0.5 by removal rather than by replacement: route inference is withdrawn (A-5.1) and derived evidence is inadmissible (A-5.2).

**Producer reproduction before adjudication.**

| Finding | Reproduction against shipped v0.4 code | Result |
|---|---|---|
| F-P4-1 attack 1 | R2-B with 50 of 50 clusters, 0 of 100 raw items, `hard_gate_violated=False` | Returned SUPPORTED-INFERENTIAL. **CONFIRMED** |
| F-P4-1 attack 2 | Direct `ComponentOutcome` construction supplying the importable `_TOKEN` | Succeeded. **CONFIRMED** |
| F-P4-1 attack 3 | `dataclasses.replace` on a genuine three-cluster outcome, replacing `evaluable` and `p_value` | Accepted by `route_claims`, returned SUPPORTED-INFERENTIAL against a minimum of 50. **CONFIRMED** |
| F-P4-2 | Design review against Sections 6.1 and 7.2: sessions randomised within fixed heterogeneous cells; Phase C targets crossed with both arms; Section 6.8 simulates cell heterogeneity | No iid single-probability model is justified. **CONFIRMED** |
| F-P4-3 | v0.4 deposit metadata title, description opening and intended-files list | All three misidentified the version. **CONFIRMED** |

**The pattern, recorded rather than smoothed.** Three consecutive rounds produced a producer-built route-level inferential mechanism that a carrying seat falsified: a null-centred bootstrap that collapsed on degenerate clusters (F-P3-1), an evidence binding a caller could bypass (F-P3-2, recurring as F-P4-1), and a binomial model the frozen design does not justify (F-P4-2). That is evidence that this producer's route-level inferential ambition exceeded what the design supports. Withdrawal is the conclusion that follows.

---

## 4e. v0.5 amendment entries

Entries A-5.1 through A-5.6 are recorded verbatim in Section 13 of the frozen contract and are not duplicated in full here. In summary: A-5.1 withdraws all route-level inference and reclassifies every component as a descriptive gate; A-5.2 makes mandatory raw evidence the sole admissible input and recomputes every gate internally; A-5.3 corrects the deposit metadata and adds current-version parity checks; A-5.4 records the round 4 regression status; A-5.5 records that nothing else changed and that neither the simulation nor the anchor research was re-run; A-5.6 records that v0.1 through v0.4 are HALTED and never deposited, and that v0.5 carries no verdict.

---

## 5. Items carried forward as UNKNOWN into v0.5

The authoritative list is Section 0.1 of the frozen contract: the XZ ledger cardinality; whether the R3 ConflictLedger will be built; the Phase-B nuisance variance components; the realized calibration of the BCa rule under final harness parameters; the model families that will occupy the agent role; **new in v0.3**, the realized counts of denials, injections and adjudicated items that determine which Class I route components are EVALUABLE and therefore the size of family F3a; and the XZ and CVE-Bench source URLs, marked UNKNOWN-PENDING-DEPOSIT.

---

## 6. Next required action

Dispatch `SHVVP_v0_5_AUDIT_DISPATCH_BRIEF.md`, together with `SHVVP_v0_5_FOCUSED_DELTA_ADDENDUM.md`, to one GPT-class and one Gemini-class non-producer carrying seat. Producer and editor remain ADVISORY. On convergence, deposit; on divergence or any HALT, produce v0.6 with a further append-only entry and append both verdicts to the audit ledger verbatim. No deposit may occur on producer, editor or chair attestation alone, and no deposit may occur on a single family's PASS.

---

# Bismillah ir-Rahman ir-Rahim
