# Bismillah ir-Rahman ir-Rahim

# R0323 -- PT Verdict - SHVVP v0.8.2 Phase A Amendment

**Chronological Index:** 388 of 995  
**Date:** 2026-07-31  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** PT_verdict_GPT_5_6_Sol_SHVVP_v0_8_2.txt  
**Source Format:** txt  
**SHA-256:** `991e30e9c865e47f1c4cb743ac2d483504216745c5f9005a6cf8d5a555436497`  

---

## R0323 · PT Verdict - SHVVP v0.8.2 Phase A Amendment

- section: V. BSSG & SHVVP Protocols
- source_file: PT_verdict_GPT_5_6_Sol_SHVVP_v0_8_2.txt
- source_format: txt
- text_sha256: 991e30e9c865e47f1c4cb743ac2d483504216745c5f9005a6cf8d5a555436497

# PT Verdict - SHVVP v0.8.2 Phase A Amendment

**Seat:** GPT-5.6 Sol, carrying seat 1 of 2
**Dispatch:** `SHVVP v0.8.2 Phase A Amendment -- Re-Carry Dispatch`
**Author of record:** Bilal Syed Arfeen (BayyinahEnterprise)
**Producer seat:** Claude Opus 4.6, advisory and non-carrying
**Audit date:** 2026-07-31
**Verdict:** **HALT**

## 1. Carrying conclusion

SHVVP v0.8.2 is **not deposit-ready**.

The candidate clears its mechanical gate and repairs several v0.8.1 failures:

- all four normative SHA-256 values match the dispatch;
- the shipped suite reports **61/61 GREEN**;
- a valid 200-item T4 input and a valid 240-item mixed-class T7 input both execute;
- the multidimensional jackknife now deletes rows with `axis=0`;
- T5's interval conjunct is openly retired as substantive amendment PA-A5;
- S is now observed-shared-only, M3-FIRST excludes censored entries, z0-undefined is routed to PA-Z10, and T3 rejects NaN/Inf.

Those repairs do not close the carrying gate. The independent attack reproduced **three HIGH-BLOCKING defects**, including a direct caller-supplied-statistic bypass that changes T2 from false to true while retaining the supposedly private provenance token. It also found four MEDIUM defects and one LOW divergence. The package therefore remains non-carriable under its own rule that any carrying-seat HALT blocks deposit and requires a new version.

## 2. Mechanical execution receipt

### 2.1 Normative identity

All four digests match exactly:

```text
shvvp_phase_a_amendment_v0_8_2.md
8de7827766360a5acb0194aa48a1ca2ea10ae019884d3b9c21dd19f46bcd1a31

shvvp_v0_8_2_phase_a_m3.py
34f083072c30b70b97e6e5b7be356fb7e0107e562ccf37a25c07ee29d368350d

shvvp_v0_8_2_phase_a_intervals.py
0733830d36a3cacc654bccc594b1f41ef0809c6f7150d2ec28f2121ec6451299

test_shvvp_v0_8_2_phase_a.py
367b475e8a6807b4ccbcfc0f93352c1d72afb780805a8e85075dd54d5de7df48
```

### 2.2 Shipped tests

Execution environment:

```text
Python 3.13.5
NumPy 2.3.5
SciPy 1.17.0
pytest 9.0.2
```

Suite result:

```text
.............................................................            [100%]
61 passed
```

### 2.3 Required valid T4 and T7 attacks

The v0.8.1 two-dimensional crash and flattened-jackknife defect are repaired on the dispatched examples:

```text
T4, n=200:
point = 0.05
interval = [-0.0049999999999999906, 0.10499999999999998]
method = BCa
internal seed = 45

T7, n=240, 40 positive and 200 negative, B perfect:
point = 1.0
interval = [1.0, 1.0]
method = PERCENTILE_FALLBACK (PA-Z10)
internal seed = 46
```

## 3. v0.8.1 finding-discharge matrix

| Prior finding | Re-carry result | Determination |
|---|---|---|
| F-SOL-081-1, T5 interval silently dropped | **DISCHARGED** | PA-A5 states the deletion, its substantive status, and the A4 consequence explicitly. |
| F-SOL-081-2, two-dimensional jackknife | **DISCHARGED on the targeted defect** | `axis=0` is present; valid T4/T7 executions complete. |
| F-SOL-081-3, censoring/S/M3-FIRST contradiction | **PARTIALLY DISCHARGED** | Observed-shared S and observed-only M3-FIRST are repaired, but the M3 object boundary, budget boundary, and old-M3 identity remain defective. See F-SOL-082-2 and F-SOL-082-3. |
| F-SOL-081-4, PA-Z5 and undefined z0 | **PARTIALLY DISCHARGED** | PA-Z5 is keyed to `sum_sq == 0`; z0 clamp is removed and PA-Z10 added. The claimed PA-Z5 test does not exercise PA-Z5, and unnamed numerical branches remain. See F-SOL-082-7. |
| F-SOL-081-5, nonexistent Phase-A NOT-EVALUABLE priority | **TEXTUALLY DISCHARGED, NOT EXECUTABLY VERIFIED** | Section 1.5 now assigns NOT-EVALUABLE to the vacuous-A2 edge. No shipped total Phase-A evaluator or operative fixture applies that guard. See F-SOL-082-5. |
| F-SOL-081-6, cardinalities and NaN | **PARTIALLY DISCHARGED** | Nonempty wrong-size T4/T7 inputs are rejected and T3 rejects NaN/Inf, but empty T4/T7 corpora bypass cardinality enforcement. See F-SOL-082-4. |
| F-SOL-081-7, execution environment | **NOT DISCHARGED IN SUBSTANCE** | The code is declared normative, but dependency versions are not frozen and the alleged golden interval vectors do not exist. See F-SOL-082-6. |

## 4. Findings

### F-SOL-082-1

**Severity:** HIGH - BLOCKING
**Locus:** Amendment Sections 5 and 7 PA-A8; `shvvp_v0_8_2_phase_a_m3.py` lines 38-41 and 234-257; `evaluate_t2_full`.
**Substance:** The provenance token does not prevent caller-supplied derived facts. `PairedDifference` is a public frozen dataclass. Python's standard `dataclasses.replace` copies its `_provenance` field unchanged. Starting from one genuine paired difference with `delta = 0`, the attack replaced `m3_a`, `m3_b`, and `delta` with attacker values. `verify_provenance()` accepted the replacement, and the canonical evaluator changed `t2_satisfied` from `False` to `True`:

```text
genuine: m3_a=10, m3_b=10, delta=0    -> T2 False
replaced: m3_a=100, m3_b=0, delta=100 -> T2 True
```

The module-level `_PROVENANCE_TOKEN` is also directly accessible to an importer, but `dataclasses.replace` is sufficient to falsify the repair without reading that variable. The implementation therefore recreates the same class of derived-state bypass that the cited BSSG discipline forbids and that PA-A8 claims to close.

**Disposition:** REJECT. Do not expose a token-bearing derived record as an accepted evaluator input. Make the public evaluator accept only the authoritative source objects and construct paired differences internally, or use an actually opaque capability boundary. In every case, revalidate `delta == m3_a - m3_b`, both statuses are OBSERVED, all fields are finite, and each value is tied to the source observations at evaluation time.

### F-SOL-082-2

**Severity:** HIGH - BLOCKING
**Locus:** Amendment Sections 1.1, 1.3, 5 and PA-A8; `M3Observation.__post_init__`; public `M3Vector.observations`; `M3Vector.add`; `compute_paired_differences`.
**Substance:** The supposed raw-input boundary is independently bypassable before `PairedDifference` exists. `M3Vector.observations` is a public mutable list. Appending directly bypasses the condition-match and duplicate-ID checks in `add()`. The attack inserted a condition-B observation into an A vector, then produced a valid-token paired difference and `T2 True`.

The observation constructor also admits states contrary to the amendment's declared censor rules:

```text
censor_status="OBSERVED" with no evidence record    -> accepted, treated as not observed
RIGHT_CENSORED_BUDGET with an evidence_record_id     -> accepted
OBSERVED at 481 minutes with budget frozen at 480    -> accepted
OBSERVED exactly at 480 and RIGHT_CENSORED at 480    -> both representable
```

The first case silently converts an intended observation into a non-observation because enum membership is never validated. The latter cases leave the evidence/no-evidence and budget-boundary semantics open. These records change S-membership and therefore T2.

**Disposition:** REJECT. Close the vector representation; validate the vector on every evaluation path rather than relying on `add()`. Require `censor_status` to be a `CensorStatus` member, forbid evidence IDs on non-discoveries, validate evidence-ID type and non-emptiness, freeze and enforce the OBSERVED-at-budget boundary, and reject observations outside the session budget. Prefer an immutable vector constructed from validated records.

### F-SOL-082-3

**Severity:** HIGH - BLOCKING
**Locus:** Parent SHVVP v0.8 Section 5.2 M3; amendment Sections 0.3, 1.1, 1.2 and PA-A6; M3 observation schema.
**Substance:** The amendment's scalar-preservation claim remains false, and the evidence-record-to-fact mapping remains an executor judgment. Parent M3 ends at the **first correctly adjudicated consequential fact**. v0.8.2 ends each fact's clock at the **first immutable saved evidence record that identifies f**. If a record is saved at minute 10 and the fact is correctly adjudicated at minute 60, v0.8.2 M3-FIRST returns 10 while parent M3 is 60. This failure exists on a fully observed, non-censored input, exactly where Section 1.2 claims preservation.

No normative field or algorithm identifies who maps an evidence record to ledger fact `f`, whether that mapping requires correct adjudication, how sealed-ledger membership is verified, or how the "first packet access" timestamp is established. The code accepts caller-supplied fact IDs, minutes, and evidence IDs without a ledger, evidence record, timestamp, or adjudication object. Thus FB-1 is not uniquely resolved at the measurement boundary, and the accepted v0.8.1 A10 repair is not implemented.

**Disposition:** REJECT. Freeze the authoritative t=0 event, evidence-record schema, immutable timestamp source, record-to-ledger-fact mapping authority, correct-adjudication condition, and budget-edge classification. Either preserve parent M3 by timing through correct adjudication or explicitly declare and justify a substantive endpoint change without claiming scalar identity.

### F-SOL-082-4

**Severity:** MEDIUM - MUST AMEND BEFORE RE-CARRY
**Locus:** Amendment Sections 2.6 and PA-A7; `t4_interval` lines 329-335; `t7_interval` lines 362-368.
**Substance:** Exact corpus cardinality is not enforced for the empty case. Both functions return `None` before checking the required size:

```text
t4_interval([], seed) -> None
t7_interval([], seed) -> None
```

The amendment says T4 requires exactly 200, T7 exactly 240, and wrong cardinality raises `PhaseAInputError` before computation. Empty is a wrong cardinality and, for A3/A6, a load-bearing missing-corpus state. Returning an untyped `None` can be mistaken for local non-firing or a declared PA-Z state.

**Disposition:** Move exact-size validation before emptiness handling and return a typed construction state only where the amendment explicitly defines one. Add fixtures for 0, 1, required-size-minus-one, and required-size-plus-one.

### F-SOL-082-5

**Severity:** MEDIUM - MUST AMEND BEFORE RE-CARRY
**Locus:** Amendment Section 1.5, PA-Z1, PA-Z4, PA-Z8 and Section 6 coverage claim; shipped Python modules and tests.
**Substance:** The vacuous-A2 guard is now stated clearly in prose, but no shipped evaluator computes the Phase-A total label or applies A1-A6, M12, denominator completeness, and the new construction-evaluability priority together. The suite tests `evaluate_t2_full([])` only; it never constructs `IDC > 0, S = {}` and verifies a final `NOT-EVALUABLE` label rather than `NOT-FALSIFIED`.

PA-Z4 is likewise not implemented or tested. `TestPAZ4` calls `evaluate_t5(NaN, 10)` and acknowledges that alpha-undefined is outside the code. This does not test fewer-than-two ratable items, all-identical pairs, the 0.67 boundary, or the required `INDETERMINATE-ADJUDICATION` outcome. The statement that the suite covers every PA-Z rule is therefore false.

**Disposition:** Add a canonical Phase-A decision evaluator or an equally precise executable reference fixture for the total label mapping. Directly test the empty-S/IDC-positive edge and implement/test PA-Z4 with actual adjudication inputs.

### F-SOL-082-6

**Severity:** MEDIUM - MUST AMEND BEFORE RE-CARRY
**Locus:** Amendment Sections 2.2, 2.3 and PA-A10; interval-module header lines 30-33; test suite seed-reproducibility test.
**Substance:** Declaring the Python source "sole normative" does not freeze the executable environment it imports. The package contains no dependency lock and states only unversioned `numpy` and `scipy`. It relies on NumPy PRNG streams, NumPy percentile defaults, and SciPy normal CDF/quantile behavior.

The claimed golden interval vectors do not exist. The only exact lower/upper assertions compare two executions of the same installed code to each other. No test pins a dispatched numeric lower or upper bound for T2, T3, T4, or T7. Consequently a dependency change can alter interval bytes while the stated golden-vector gate has nothing to compare against.

**Disposition:** Ship a lock or hermetic environment specification, state the percentile method explicitly, and add immutable expected point/bound outputs for every statistic and fallback path. A same-process repeatability test is not an independent golden vector.

### F-SOL-082-7

**Severity:** MEDIUM - MUST AMEND BEFORE RE-CARRY
**Locus:** Amendment Sections 2.4, 3 and 6; `_bca_interval` lines 219-228; `TestPAZ5` and `TestPAZ4`.
**Substance:** The claim that all degeneracy states are named and exercised is not true. `TestPAZ5` never causes PA-Z5; it deliberately uses all-identical data and asserts PA-Z10, then treats the existence of the unexecuted branch as coverage. The code also retains two unregistered numerical policies:

1. when a BCa denominator is within `1e-15` of zero, `_bca_q` silently returns percentile level `0.5`;
2. adjusted percentile levels are silently clamped to `[0.5/n_valid, 1 - 0.5/n_valid]` even though the text says no continuity correction and does not name this clamp.

These choices can affect load-bearing interval bounds, but neither produces a PA-Z rule or fallback reason.

**Disposition:** Either remove the unnamed branches or register them with exact triggers, methods, reporting, and tests. Provide a fixture that actually reaches PA-Z5, or prove it unreachable for every public statistic and remove it from the claimed covered rule set.

### F-SOL-082-8

**Severity:** LOW
**Locus:** `evaluate_t2_point` lines 357-369 versus `evaluate_t2_full` lines 495-504.
**Substance:** On PA-Z9, `evaluate_t2_point` reports `evaluable=True` while `evaluate_t2_full` reports `evaluable=False`. Both carry the same rule name. This is an internal API contradiction for the all-zero relative denominator state.

**Disposition:** Use one typed evaluability meaning in both APIs and add a cross-API consistency test.

## 5. Answers to the dispatch questions

**F-SOL-081-1: Is T5's interval deletion now declared as PA-A5?** Yes. This targeted finding is discharged.

**F-SOL-081-2: Does `axis=0` fix the T7 crash and T4 fabrication?** Yes for the targeted defect. Both required valid inputs execute, and row deletion is explicit.

**F-SOL-081-3: Is S observed-shared-only, are censored facts excluded, and is the old censoring-direction analysis withdrawn?** Yes at the intended-path level. The repair is undermined by malformed-status and mutable-vector admissions that can still alter S.

**F-SOL-081-4: Is PA-Z5 over `sum_sq == 0`, z0-undefined PA-Z10, and the z0 clamp removed?** Yes in source. PA-Z5 is not actually exercised, and separate unnamed BCa clamps remain.

**F-SOL-081-5: Does Section 1.5 prevent NOT-FALSIFIED on vacuous A2?** The prose now says so unambiguously. The shipped artifacts do not execute or test the final label, so the repair is not operationally demonstrated.

**F-SOL-081-6: Are T4=200, T7=240, and T3 NaN handling enforced?** Nonempty wrong sizes are rejected and T3 NaN/Inf is rejected. Empty T4/T7 inputs bypass the size check.

**F-SOL-081-7: Is code declared the sole normative definition?** Yes as a declaration. No as a complete reproducibility repair: imported dependency versions and exact golden interval outputs remain unfrozen.

## 6. Required next-version repair set

A re-carryable successor should, at minimum:

1. remove the public token-bearing `PairedDifference` evaluator boundary and close the `dataclasses.replace` bypass;
2. make M3 vectors immutable and fully revalidated at pipeline entry;
3. freeze the old/new M3 endpoint relation, adjudication timing, record-to-fact authority, ledger membership, t=0, and budget boundary;
4. reject empty T4/T7 corpora as wrong cardinality;
5. implement and test the total Phase-A label guard and PA-Z4;
6. ship a dependency lock and actual numeric golden vectors;
7. register or remove every silent BCa numerical branch; and
8. reconcile PA-Z9 evaluability across APIs.

## 7. Final carrying statement

**HALT.** The v0.8.2 bytes authentically pass their shipped 61-test suite and repair the v0.8.1 multidimensional jackknife. They do not establish the claimed raw-evidence boundary: a standard-library replacement operation preserves the provenance token and changes T2 from false to true, while the M3 vector itself remains mutable and admits contradictory censor states. The measurement endpoint and execution environment also remain underfrozen. Under the candidate's own carrying rule, no v0.8.2 deposit should be made from these bytes; a corrected successor requires a new version, new hashes, and a fresh two-family carrying run.

---

# Bismillah ir-Rahman ir-Rahim
