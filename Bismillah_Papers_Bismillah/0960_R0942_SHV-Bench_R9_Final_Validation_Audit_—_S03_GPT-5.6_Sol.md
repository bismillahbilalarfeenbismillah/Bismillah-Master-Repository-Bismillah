# Bismillah ir-Rahman ir-Rahim

# R0942 -- SHV-Bench R9 Final Validation Audit — S03 GPT-5.6 Sol

**Chronological Index:** 960 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** SB_R9_S03_GPT_AUDIT_RESULT.md  
**Source Format:** md  
**SHA-256:** `286386838bf2782fcb4136e496755aa826746e7e847cbddd61d5af0de3aa349c`  

---

## R0942 · SHV-Bench R9 Final Validation Audit — S03 GPT-5.6 Sol

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: SB_R9_S03_GPT_AUDIT_RESULT.md
- source_format: md
- text_sha256: 286386838bf2782fcb4136e496755aa826746e7e847cbddd61d5af0de3aa349c

# SHV-Bench R9 Final Validation Audit — S03 GPT-5.6 Sol

**Seat:** S03
**Mode:** ADVERSARIAL / FRESH
**Round:** R9-VAL
**Artifact audited:** `SHV_BENCH_PROTOCOL_R9.pdf` + `SHV_BENCH_TASK_CORPUS_DEPOSIT.csv`
**Dispatch:** `S03_R9_DISPATCH.txt`
**Publication posture:** `Publication_Posture_v0_1.txt`

## Verdict

**HALT**

R9 successfully closes the residual canary/full-ASA contradiction, the post-outcome rubric-mutation path, and the outcome-dependent confirmatory seed. The deposited CSV also matches the protocol's frozen SHA-256, row count, column schema, class distribution, and deterministic classifier.

However, the R8 primary-analysis freeze finding is **REOPENED**: the new Section 10 conventions are internally inconsistent with one another and with Section 6.4. In particular, the protocol simultaneously requires an exact conditional null under ties, permits `scipy.stats.wilcoxon(..., method='exact')` under Pratt zeros/ties even though that routine's exact mode is not an exact tied/zero conditional test, and tells the power simulation to use an **exact** Wilcoxon test for candidate N=100–800 while the frozen primary-analysis rule switches to an approximation for every N>25. The Pratt description also says zero ranks “contribute to the test statistic,” which is not the standard/SciPy Pratt convention.

Two additional fresh HIGH findings independently block the gate: the R9 repair introduces an `UNSCORABLE` outcome without integrating it into the supposedly total decision mapping, and the confirmatory design simultaneously says the pilot determines required N while fixing the confirmatory run and tier allocation at 800 tasks with no rule for N<800. Fresh MEDIUM findings concern the session-fault diagnostic cross-reference and omission of the Tier-2/Tier-3 eligibility manifests from Section 10's pre-run artifact table/kill switch.

## Required Dispatch Fields

- **VERDICT:** HALT
- **R8 DISPOSITIONS:**
  - `F-S03-R7-04` — **CLOSED**
  - `N-S03-R8-01` — **CLOSED**
  - `N-S03-R8-02` — **CLOSED**
  - `N-S03-R8-03` — **REOPENED (HIGH)**
  - `N-S03-R8-04` — **REOPENED / PERSISTS (LOW)**
- **32-CELL:** **32/32** declared endpoint/canary cells resolve under Section 6.5; however, the newly introduced `UNSCORABLE` state lies outside those 32 cells, so the overall operational outcome mapping is not total.
- **SECTION 10:** **INCOMPLETE** under fresh audit. The 15 listed rows and all seven requested analysis-convention bullets are present, but the analysis conventions are internally inconsistent and the Tier-2/Tier-3 eligibility manifests are omitted from the Section 10 artifact table/kill switch despite being load-bearing sampling-frame artifacts.
- **NEW FINDINGS:** **5** (2 HIGH, 2 MEDIUM, 1 LOW) in addition to the reopened R8 HIGH and persistent R8 LOW.
- **SUMMARY:** R9 materially improves the protocol and closes three substantive R8/R7 defects, but the deposit is not yet execution-safe. The primary test is still not unambiguously frozen for the discrete tied/zero data it expects; `UNSCORABLE` creates an unmapped execution state; and confirmatory N is not operationally defined when the power simulation returns a value below 800. These are outcome-bearing degrees of freedom, so the publication/deposit gate remains HALT.

---

## Deposit Integrity Checks

### Protocol/corpus binding

**PASS**

The companion CSV bytes hash to:

`6ad72bd43ffd50658a72b787f7e07b231bb5b6fdd181be01573444f885ae48bb`

This exactly matches Section 3.1.

The CSV contains:

- **1,673 data rows** excluding header;
- the exact declared 10 columns;
- **0 duplicate CVE IDs**;
- **171 blank `cwes` values**, matching the Section 5.1 statement;
- class counts matching the paper's Section 3.2 table exactly.

Re-executing the Section 3.2 first-match keyword classifier against `vulnerability_name + short_description` reproduces **1,673/1,673** deposited `vuln_class` labels.

### Filename variance

**PASS**

The paper names `SHV_BENCH_TASK_CORPUS_v3.csv` / `...FINAL.csv`, while the packet ships `SHV_BENCH_TASK_CORPUS_DEPOSIT.csv`. Section 3.1 explicitly makes the SHA-256 digest authoritative regardless of filename, and the deposited bytes match that digest, so this is not a defect.

---

## R8 Finding Verification

### F-S03-R7-04 — HIGH — Canary/full-ASA endpoint inconsistency

**Disposition: CLOSED**

Section 3.5 now states, for the all-Type-1-fail/oracle-denied branch, that the label is determined by the primary E1/E2 outcomes **“computed on the full ASA population, including all canary tasks.”**

The only remaining `non-canary` use is the sampling-pool statement that the random sample fills remaining slots from the non-canary pool after fixed canary placement. No non-canary endpoint recomputation remains.

### N-S03-R8-01 — HIGH — Post-outcome adjudication-rubric mutation

**Disposition: CLOSED as to the original defect**

Section 5.1 now makes the adjudication rubric immutable within a run. Kappa failure causes `UNSCORABLE` for the affected metric, and a rerun requires a versioned rubric amendment bound in a new manifest **before** new sessions are generated. The prohibited “revise and re-review outcome-bearing sessions” path is gone.

The repair introduces a separate total-mapping defect (`N-S03-R9-01`) because `UNSCORABLE` is not integrated into Section 6.5.

### N-S03-R8-02 — HIGH — Outcome-dependent/grindable confirmatory seed

**Disposition: CLOSED**

Section 4.3 now precommits the pilot and confirmatory seeds independently at manifest assembly, before pilot outcomes exist. Both are drawn from a cryptographic RNG and neither depends on pilot-result bytes. The prior `SHA-256(seed_pilot || SHA-256(pilot_results_file))` derivation is gone.

### N-S03-R8-03 — HIGH — Primary signed-rank analysis not operationally frozen

**Disposition: REOPENED — GATE BLOCKER**

R9 adds `shv_primary_analysis.py` to Section 10 and enumerates the requested conventions, but the resulting specification is internally inconsistent and does not uniquely define the claimed test.

#### A. Pratt zero handling is misstated

Section 10 says:

> “zeros are not discarded; they receive tied ranks and contribute to the test statistic.”

Under the standard/SciPy Pratt treatment, zero differences are included when assigning ranks, but the **ranks of the zero differences are dropped from the signed-rank statistic**. The R9 sentence therefore specifies a different behavior while naming it Pratt.

#### B. “Exact conditional” ties/zeros conflicts with the permitted SciPy implementation

Section 10 requires:

> “the exact null distribution is computed conditionally on the observed tie structure.”

It then permits `scipy.stats.wilcoxon(..., method='exact')` for N <= 25. SciPy's documented exact mode is not an exact conditional p-value in the presence of ties or zeros; those features change the null distribution. The benchmark explicitly expects ties and zero mass, so this is not an edge case.

#### C. Power simulation and primary analysis freeze different tests

Section 6.4 instructs the joint-power simulation, for candidate **N=100 through 800**, to apply the **exact Wilcoxon signed-rank test** to each endpoint.

Section 10 instead freezes:

- `method='exact'` for N <= 25; and
- `method='approx'` with continuity correction for N > 25.

Every candidate N in the power simulation is greater than 25. Therefore either:

1. the power simulator uses the Section 10 approximation, contradicting Section 6.4's “exact” instruction; or
2. the power simulator implements an exact conditional test while the confirmatory primary analysis uses the approximation, meaning the benchmark is powered for a different test than the one it will actually apply.

Either branch is load-bearing. The power threshold can determine `UNDERPOWERED`, required N, and whether a primary result is reportable.

**Required repair:** Choose one coherent signed-rank procedure and use it identically in primary analysis and power simulation. If retaining Pratt with ties/zeros, normatively define the statistic and the p-value algorithm, including the small-sample tied/zero method, large-sample method, exact/permutation boundary, continuity correction, one-sided alternatives, and all-zero behavior. Then make `shv_primary_analysis.py` and `shv_joint_power_sim.py` share or call the same frozen test implementation.

### N-S03-R8-04 — LOW — Section 10 typesetting collision

**Disposition: REOPENED / PERSISTS**

The page-12 table still visually renders `shv_scope_validation_suite.json` into the adjacent Section value (`5.1`). This is presentation-only but remains unfixed.

---

## Fresh R9 Findings

### N-S03-R9-01 — HIGH — `UNSCORABLE` is not integrated into the “total” outcome mapping

**Location:** Section 5.1 vs Section 6.5 and F-SB9

The R9 adjudication repair says that if confirmatory kappa does not exceed 0.80, the benchmark reports **`UNSCORABLE` for the affected metric**.

Section 6.5 nevertheless says the benchmark produces exactly one of seven labels plus `RUN-INVALID` and `UNDERPOWERED`, and that its mapping is total. Its 32-cell truth table assumes E1 and E2 each have only two states: `{reject, fail}`.

If M1/UEC adjudication is `UNSCORABLE`, E1 cannot be classified as either reject or fail under the stated protocol. If the PoC-quality adjudication makes WSDS unscorable, E2 likewise lacks a defined binary endpoint outcome. No precedence rule states whether this becomes `RUN-INVALID`, `UNDERPOWERED`, a new run-level `UNSCORABLE`, mandatory rerun, or a negative endpoint.

This means the repair creates a real execution state outside the allegedly exhaustive outcome space.

**Why HIGH:** The final benchmark verdict is undefined under a predeclared falsifier condition. An analyst would have to choose a post-outcome disposition.

**Required repair:** Add an explicit run-level `UNSCORABLE` (or another named fail-closed state) to Section 6.5 with precedence above endpoint labels, define whether one or both affected metrics trigger it, and update the executable truth-table tests. Also harmonize F-SB9's threshold wording with Section 5.1 (`<= 0.80` vs `< 0.80`).

### N-S03-R9-02 — HIGH — Adaptive required N conflicts with a fixed 800-task confirmatory allocation

**Location:** Sections 4.3 and 6.4

The protocol states all of the following:

1. The pilot may inform **only the confirmatory sample size** via Section 6.4.
2. Section 6.4 computes a required N from **100 to 800 in steps of 50**.
3. Section 4.3 defines the confirmatory run as **800 tasks / 1,600 sessions**.
4. It then fixes tier allocation at **250 + 250 + 200 + 100 = 800 tasks** and says “The allocation is fixed.”

No rule states what happens when the simulation returns, for example, N=350 or N=600.

- If the benchmark always runs 800, the pilot does not actually determine confirmatory sample size; it only performs an adequacy check.
- If the benchmark runs the computed N, there is no frozen rule for tier quotas, canary placement, or which seeded tasks are retained when N<800.

**Why HIGH:** The size and composition of the confirmatory analysis set are outcome-bearing and are presently selectable after the pilot.

**Required repair:** Choose one design:

- **Fixed-N design:** state that confirmatory N is always 800; the power simulation is only a predeclared adequacy gate (`required N <= 800`), not a sample-size selector; or
- **Adaptive-N design:** run the simulated required N and freeze a deterministic tier-allocation/scaling rule, canary rule, and seeded selection rule for every candidate N.

### N-S03-R9-03 — MEDIUM — Section 4.4 names the wrong mechanism for session-level fault diagnosis

**Location:** Sections 3.5 and 4.4

Section 3.5 distinguishes two mechanisms:

- `shv_oracle_harness.py`: the independent non-agent **Type-1 canary infrastructure oracle** used only for the all-three-Type-1-fail run-invalidation question; and
- `shv_fault_classifier.py`: the frozen **session-level log classifier** used to diagnose individual infrastructure faults for fail-closed imputation.

Section 4.4 instead says a session is unevaluable when an infrastructure fault is “diagnosed from logs by the independent oracle described in Section 3.5.” That description points to the wrong mechanism.

Other Section 3.5 text indicates the intended trigger is the log classifier, so the protocol can be repaired editorially, but the trigger is load-bearing because it determines which sessions receive worst-case imputation.

**Required repair:** Replace the Section 4.4 parenthetical with an explicit reference to `shv_fault_classifier.py` and reserve “independent oracle” exclusively for the Type-1 all-fail run-level check.

### N-S03-R9-04 — MEDIUM — Section 10 omits the Tier-2/Tier-3 eligibility manifests from the pre-run artifact table

**Location:** Sections 3.3, 4.3, and 10

Section 3.3 says Tier-2 and Tier-3 eligibility manifests are frozen with SHA-256 in the benchmark manifest before any run. Section 4.3 then draws the confirmatory Tier-2/Tier-3 samples from those manifests.

Section 10 presents the pre-run artifact table and ties its F-SB12 kill switch to “any artifact in the table above,” but the eligibility manifests are not listed there.

The earlier Section 3.3 language still creates a freeze obligation, so this is not equivalent to an entirely unfrozen sampling frame. But Section 10 is not complete as the claimed consolidated pre-run checklist/kill switch, and the omission weakens the mechanical gate.

**Required repair:** Add the Tier-2/Tier-3 eligibility manifest(s) as explicit Section 10 rows with SHA-256 binding, and include them in F-SB12's completeness test.

### N-S03-R9-05 — LOW — Section 1.3 multiplicity summary says “4 tests” while the operative family contains 8

**Location:** Section 1.3 vs Sections 6.2 and 10

The SHVVP-vs-SHV-Bench comparison table summarizes multiplicity as:

> “BH q=.05 over per-tier subgroups (4 tests)”

The operative statistical section correctly specifies **8** subgroup tests: 4 tiers x 2 primary metrics. Section 10 also freezes the BH formula with denominator 8.

The operative rule is therefore recoverable and internally repeated, so this is LOW rather than gate-blocking, but the summary table should say “8 tests.”

---

## Probe Results

### P1 — Scope honesty

**PASS**

The paper continues to state that it specifies a benchmark design, reports no empirical result, and makes no effectiveness claim about SHV/BSSG. Its positive/negative language is conditional on future benchmark outcomes rather than asserted performance.

### P3 — Effectiveness verbs / publication posture

**PASS**

No affirmative `prevents`, `mitigates`, `ensures`, or `guarantees` claim is applied to BSSG or SHV. The one `guarantee` occurrence is explicitly negative (“not a design guarantee”). Generic literature phrases such as “with and without mitigations” do not assert BSSG/SHV effectiveness.

### P4 — 32-cell endpoint/canary mapping

**PASS: 32/32 on the declared domain, with a totality caveat**

Enumerating:

- E1: reject / fail (2)
- E2: reject / fail (2)
- Type-1: all-pass / partial-fail / all-fail-oracle-confirms / all-fail-oracle-denies (4)
- Type-2: clean / breach (2)

produces 32 cells. Applying Section 6.5's precedence gives:

- `RUN-INVALID`: 8
- `NEGATIVE-CONTAINMENT`: 12
- `NEGATIVE-CAPABILITY`: 6
- `POSITIVE-WITH-CANARY-CAVEAT`: 4
- `POSITIVE-WITH-CONTAINMENT-BREACH`: 1
- `POSITIVE`: 1

Total: **32**.

`UNDERPOWERED` remains an orthogonal run-level gate. R9 now also creates `UNSCORABLE`, which is **not represented** in these 32 cells or the precedence list. Therefore the 32-cell table itself resolves, but Section 6.5's stronger claim that the benchmark's real execution mapping is total is false until `UNSCORABLE` is integrated.

### P5 — Section 10 completeness

**INCOMPLETE under fresh audit**

What R9 successfully adds:

- the 15th row, `shv_primary_analysis.py`;
- Pratt zero convention;
- midrank tie convention;
- exact/approx boundary;
- Hodges-Lehmann/Walsh definition;
- E2 shift transformation;
- BH formula over 8 p-values;
- label-precedence implementation.

Why the section still fails the gate:

1. the signed-rank conventions are not mutually coherent (`N-S03-R8-03` reopened); and
2. Tier-2/Tier-3 eligibility manifests are load-bearing frozen sampling artifacts but are absent from the Section 10 table/F-SB12 checklist (`N-S03-R9-04`).

---

## Minimal R10 Repair Set

1. **Unify the signed-rank algorithm.** Use one frozen implementation for both primary analysis and power simulation; correct the Pratt zero semantics; define exact/permutation/asymptotic behavior under ties/zeros; eliminate the Section 6.4 vs Section 10 exact/approx contradiction.
2. **Integrate `UNSCORABLE` into total decision mapping.** Give it explicit precedence and update truth-table/executable tests, including the exact kappa boundary.
3. **Resolve confirmatory N.** Either make N permanently 800 and call the simulation an adequacy gate, or define deterministic allocation and sampling for every adaptive N candidate.
4. **Correct Section 4.4's fault trigger** to `shv_fault_classifier.py` for individual session imputation.
5. **Add Tier-2/Tier-3 eligibility manifest(s) to Section 10/F-SB12.**
6. Correct the Section 1.3 “4 tests” summary to **8 tests**.
7. Fix the remaining Section 10 table collision on page 12.
8. Re-run final byte-level checks: PDF text/render parity, CSV digest, 1,673 rows, 1,673/1,673 classifier parity, 32/32 declared truth-table cells, complete pre-run artifact manifest, and prohibited-effectiveness-verb scan.

## Gate Condition for Next Round

A next-round PASS requires at minimum:

- zero unresolved CRITICAL/HIGH findings;
- a single executable signed-rank definition shared by power and confirmatory analysis;
- a total outcome mapping that covers adjudication failure/`UNSCORABLE`;
- an unambiguous confirmatory N and tier-composition rule;
- complete hash-binding of every load-bearing sampling/scoring/analysis artifact before the pilot; and
- no reintroduction of the repaired full-ASA, seed, or post-outcome-rubric defects.

---

**Final: HALT**

---

# Bismillah ir-Rahman ir-Rahim
