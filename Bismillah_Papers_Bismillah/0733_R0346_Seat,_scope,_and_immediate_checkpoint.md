# Bismillah ir-Rahman ir-Rahim

# R0346 -- Seat, scope, and immediate checkpoint

**Chronological Index:** 733 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** SHVVP_v0_4_SEAT_A_GPT_DELTA_VERDICT.md  
**Source Format:** md  
**SHA-256:** `a93747bb02e507e12d4acc43b216dec4383893536bae59355b787999029902e3`  

---

## R0346 · Seat, scope, and immediate checkpoint

- section: V. BSSG & SHVVP Protocols
- source_file: SHVVP_v0_4_SEAT_A_GPT_DELTA_VERDICT.md
- source_format: md
- text_sha256: a93747bb02e507e12d4acc43b216dec4383893536bae59355b787999029902e3

# HALT

## Seat, scope, and immediate checkpoint

**Seat A — GPT-class / OpenAI-family, independent non-producer carrying seat.**

Focused-delta status of the six F-P3 remedies:

| Remedy | Status | Execution result |
|---|---|---|
| F-P3-1 exact boundary test | **PARTIALLY ABSORBED** | Exact tails, Clopper-Pearson inversion, zero case, and nominal type-I bounds passed independently; the new inferential model still lacks a valid frozen iid-cluster basis (F-P4-2). |
| F-P3-2 fail-closed evidence binding | **NOT ABSORBED** | Three independent injection paths produced `SUPPORTED-INFERENTIAL`, including catastrophic raw evidence and forged outcomes (F-P4-1). |
| F-P3-3 Phase C invalid inputs | **ABSORBED** | NaN, infinities, None, out-of-range values, malformed types and counts fail closed; mechanical failure still dominates. |
| F-P3-4 label closure | **ABSORBED** | The 256-state map is closed; guard terms are annotations subordinate to L2. |
| F-P3-5 stale 1,280 size | **ABSORBED** | Section 11 freezes 1,440; every current-source 1,280 occurrence is historical or a ladder row. |
| F-P3-6 reproduction defaults | **IMPLEMENTATION ABSORBED; FULL-RUN ATTESTATION INCOMPLETE** | Defaults are correct; standalone calibration completed at 9 repetitions and exactly matched the receipt; the no-extra-argument full run exactly reproduced Stages 1–2 and entered Stage 3 before being stopped at the immediate-checkpoint instruction. |

At least one blocker exists. Deposit is blocked and v0.5 is required.

## Findings

### F-P4-1

- **ID:** F-P4-1
- **SEVERITY:** HIGH, BLOCKING
- **Locus (by contract section):** Sections 8.2–8.4; `ComponentOutcome`; `evaluate_component`; `route_claims`; amendment A-4.2
- **Substance:** The claimed fail-closed evidence binding is bypassable in three independently executed ways. First, `evaluate_component` still accepts the caller-supplied `hard_gate_violated` Boolean and does not compute the frozen descriptive hard gate from raw counts. I passed R2-B 50/50 successful clusters but 0/100 successful raw items, asserted `hard_gate_violated=False`, and received `SUPPORTED-INFERENTIAL` although the frozen pooled-share gate is 0.98. Raw counts are optional and their threshold is never enforced. Second, direct `ComponentOutcome` construction succeeds when the module’s accessible `_TOKEN` is supplied. Third, `dataclasses.replace` preserves the token of a genuine below-threshold outcome while replacing `evaluable`, `p_value`, and related fields. Both forged three-cluster objects were accepted by `route_claims` and yielded `SUPPORTED-INFERENTIAL` against a minimum of 50. The shipped T16c tests only construction without `_TOKEN` and therefore proves less than its name claims.
- **Disposition:** **HALT.** Compute every hard/descriptive gate from required raw evidence inside the normative evaluator; make raw evidence mandatory where a gate depends on it; remove caller-supplied gate conclusions. Do not rely on an importable object token as evidence provenance. Recompute admissibility from immutable raw fields inside `route_claims`, or use a closed serialization/validation boundary that cannot trust mutable/replaceable derived fields.
- **Cross-reference:** Focused addendum §3.1 item 2; regression F-P3-2; independent output `shvvp_v0_4_seat_a_independent_delta_checks.json`. **Unanticipated by producer; lead adjudication required.**

### F-P4-2

- **ID:** F-P4-2
- **SEVERITY:** HIGH, BLOCKING
- **Locus (by contract section):** Sections 6.1, 7.2, 8.1–8.3 and 8.5; `binom_sf_ge`; amendment A-4.1
- **Substance:** The arithmetic exact-binomial implementation is correct, but the contract’s justification for using a binomial model is not. Section 8 says task-by-variant cells and Phase C targets are independent “units of allocation” and therefore iid Bernoulli draws with one probability \(\pi\). The frozen design instead randomizes sessions within each Phase B cell and crosses every Phase C target with both arms; the cells/targets themselves are fixed heterogeneous tasks, not independently treatment-allocated or sampled iid clusters. The design simulation explicitly models cell heterogeneity. Independence alone does not make a sum binomial; a common success probability or a valid superpopulation/sampling model is also required. The shipped type-I checks simulate only iid `Bin(n, pi0)` draws and therefore cannot validate the actual fixed heterogeneous design.
- **Disposition:** **HALT.** Freeze the population/generalization target and a test valid for the actual fixed, heterogeneous paired design, or downgrade these components to descriptive gates. If a superpopulation binomial model is intended, state and justify the sampling mechanism and homogeneity/exchangeability assumptions rather than deriving them from session randomization.
- **Cross-reference:** Focused addendum §3.1 item 1; regression F-P3-1 and F-P2-3. **Unanticipated by producer; lead adjudication required.**

### F-P4-3

- **ID:** F-P4-3
- **SEVERITY:** MEDIUM
- **Locus (by contract section):** Deposit metadata §§1, 3 and 5; scope-honesty regression
- **Substance:** The v0.4 deposit metadata title calls the artifact “SHVVP v0.3,” and its deposit description begins “FROZEN preregistration, version 0.3.” Its intended-files list also says “once they exist, both v0.3 verdicts,” although those verdicts already ship and the future files are the v0.4 verdicts. Depositing this block would misidentify the frozen version.
- **Disposition:** Correct all three metadata references in v0.5 and add a current-version parity test covering title, description, version field, intended files, source, and PDF.
- **Cross-reference:** Axis 3 and Axis 4; packet scope-honesty check. **Unanticipated by producer; lead adjudication required.**

## Four-axis focused analysis

### Axis 1 — Executability and validity

I independently reproduced the prior statistical counterexamples: 50/50 against 0.98 returned \(0.36416968008711675\), and 30/30 against 0.95 returned \(0.21463876394293727\), matching an independent full summation and SciPy. The shipped Clopper-Pearson lower bounds matched independent Beta-quantile references to floating-point precision; \(x=0\) returned p=1 and bound 0. Exact rejection probabilities at the registry minima were 0.03379, 0.04803, 0.04418, and 0.04803, all at or below 0.05.

Every Class I minimum behaved correctly at \(n-1,n,n+1\). BH still matched the independently verified step-up implementation carried from v0.3. The re-anchored nulls are declared rather than hidden, but attainability is not a substantive justification and the iid binomial model is not established for the actual allocation (F-P4-2).

I independently enumerated all 256 Phase B Boolean states: zero oracle mismatches, exactly eight reachable labels, and no annotation in a label tuple. Phase C invalid-input fuzzing passed: undefined C1 alpha with failed C1 was `INDETERMINATE-ADJUDICATION` with no hard C1 failure; mechanical C2 failure with NaN alpha was `FAIL`.

The decisive failure is evidence admission. Public-API raw evidence, direct token construction, and `dataclasses.replace` all defeated the claimed binding (F-P4-1).

### Axis 2 — Changed citations and carried anchors

The empirical anchors and identifiers are **CARRIED ON ROUND 3 CONVERGENCE** under the recomputed immutable v0.3 source/PDF and both v0.3 verdict hashes; I did not repeat anchor web research. The changed methodological locus was checked: [NIST Technical Note 2119](https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.2119.pdf) explicitly defines Clopper-Pearson intervals by inversion of exact binomial tests and describes their conservatism. [Brown, Cai and DasGupta](https://projecteuclid.org/journals/statistical-science/volume-16/issue-2/Interval-Estimation-for-a-Binomial-Proportion/10.1214/ss/1009213286.short) is the cited real binomial-interval paper. These citations support the arithmetic method but do not cure the design/model problem in F-P4-2.

### Axis 3 — Internal consistency and completeness

The independent stale-size review passed: Section 11 says 1,440, while all remaining 1,280 references in the canonical source are historical adjudication statements or simulation-ladder rows. The shipped contextual scan returned zero offences, 47 historical references, and 15 ladder/data rows.

Text/code constants, five Class I and six Class G members, thresholds, minima, exact tails, labels, and Phase C validation are concordant. The claim that hard-gate state and outcome provenance are bound is not concordant with executable behavior (F-P4-1). Deposit metadata contains three current-version errors (F-P4-3).

Round 1 and round 2 substantive requirements remain **CARRIED ON ROUND 3 CONVERGENCE** where unchanged and passed the regression suite. The changed route inference does not fully preserve F-P2-3 because its evidence admission and inferential model remain defective.

### Axis 4 — Scope honesty and rendering

The canonical source and README correctly state that v0.1–v0.3 are HALTED, never deposited and nonbinding; v0.4 claims no verdict or empirical result; simulations are described as synthetic operating characteristics. Deposit metadata misidentifies v0.4 as v0.3 (F-P4-3).

`qpdf --check` passed. The PDF has 36 pages, correct v0.4 title/author/subject metadata, six embedded subset fonts, and no syntax errors. All 36 pages were rendered and visually inspected, including the dense route table, Phase B tables and figure. Pixel analysis found zero non-gray pixels. All 36 unique source URLs appeared in PDF link annotations; no extra PDF URL was found. No clipping, overlap, or missing glyph was observed. Source mechanical checks found no non-ASCII character, prohibited dash, doubled word, placeholder, or brand error.

## Required regression status

### Round 3

| Item | Status | Locus / result |
|---|---|---|
| F-P3-1 | **PARTIALLY ABSORBED** | Exact arithmetic is correct; inferential design basis fails F-P4-2. |
| F-P3-2 | **NOT ABSORBED** | Three injection paths succeeded; F-P4-1. |
| F-P3-3 | **ABSORBED** | §7.5 and `phase_c_label`; invalid/non-finite domain fails closed. |
| F-P3-4 | **ABSORBED** | §§6.2–6.4 and `GUARD_ANNOTATIONS`; 256-state closure passed. |
| F-P3-5 | **ABSORBED** | §11 and independent contextual review; 1,440 current size only. |
| F-P3-6 | **IMPLEMENTATION ABSORBED; FULL-RUN ATTESTATION INCOMPLETE** | Defaults and standalone 9-repetition calibration passed; full default run was stopped after exact Stage 1–2 reproduction upon the immediate-checkpoint instruction. |
| Gemini-class v0.3 PASS | **ABSORBED** | Hash matched; preserved unmodified and not reinterpreted. |

### Rounds 1 and 2

| Item | Status | Locus / result |
|---|---|---|
| F-P2-1 | **ABSORBED / CARRIED** | §§6.5, 6.5.1, 6.8 unchanged on v0.3 hash; self-test and completed Stage 1–2 default run matched. |
| F-P2-2 | **ABSORBED** | §§6.4, 6.6; independent 256-state enumeration passed. |
| F-P2-3 | **NOT FULLY ABSORBED** | Registry split and conjunction remain, but F-P4-1 and F-P4-2 block valid executable inference. |
| F-P2-4 | **ABSORBED** | §§7.4–7.5; finite and invalid-input priority checks passed. |
| F-PP-1–F-PP-6, Gemini F-PP-1/F-PP-3, chair DOI note | **CARRIED ON ROUND 3 CONVERGENCE** | Unchanged loci and immutable v0.3 hashes matched. |

I continue to agree that all four round 2 findings and all six round 3 findings were correctly accepted. The round 1 rejection of the proposed variance-derived margin and the rejection of the OpenBSD/FreeBSD anchor conflation remain carried from my prior independent adjudication.

## Custody

- Archive SHA-256 recomputed as `299a64a2ae8af2fc4b3666098350c149cc988d712b7d8cb1e6eb3079d6fef964`, exact match.
- Pre-extraction inspection found 39 regular entries, no absolute path, traversal, or symlink.
- Fresh extraction was used.
- `sha256sum -c SHA256SUMS` returned OK for all 38 listed members; the manifest excludes itself; no unlisted or missing file.
- All v0.1–v0.3 lineage hashes, including my v0.3 verdict hash `c82178d91d834844baeb794d84b39de4dbd571010769f43813d9d694a99ca96e`, matched.
- I modified no packet member. Seat-owned scripts, logs, renders and outputs were written outside the packet.

## Code executed versus trusted

Executed: the 95-check shipped suite (0 failures), simulation self-test, route module, regression scan, producer verifier for orientation only, independent exact-tail and Clopper-Pearson references, exact type-I calculations, every registry minimum at \(n-1,n,n+1\), 256-state Phase B oracle, Phase C invalid-input cases, three evidence-injection attacks, PDF/mechanical checks, standalone default calibration, and the default full simulation through completed Stages 1–2.

I did not trust the producer verifier, tests, receipt, token mechanism, or adjudication claims. The producer verifier reported PASS because its fabrication test omitted the accessible token and did not try `dataclasses.replace` or inconsistent raw evidence.

## Limits

- Per the focused addendum, unchanged empirical anchors and unchanged round 1–2 loci were carried on exact v0.3 hashes rather than re-researched.
- The default full simulation and standalone sensitivity run were stopped at the immediate checkpoint after a blocker was established. Stage 1 and Stage 2 had reproduced the receipt exactly; standalone calibration completed and matched exactly at 9 repetitions.
- I did not rebuild any packet artifact or inspect nonexistent empirical data.
- I do not attest to universal safety or universal statistical correctness.

## Carrying statement

**HALT.** This is one carrying verdict and cannot carry alone. Convergence requires both non-producer seats from different vendor families. F-P4-1 and F-P4-2 block deposit; v0.5 and a fresh carrying audit are required.

---

# Bismillah ir-Rahman ir-Rahim
