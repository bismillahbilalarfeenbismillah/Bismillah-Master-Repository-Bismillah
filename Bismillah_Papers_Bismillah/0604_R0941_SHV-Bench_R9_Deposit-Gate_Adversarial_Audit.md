# Bismillah ir-Rahman ir-Rahim

# R0941 -- SHV-Bench R9 Deposit-Gate Adversarial Audit

**Chronological Index:** 604 of 995  
**Date:** 2026-08-22  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** SB_R9_GPT_FINAL_AUDIT.md  
**Source Format:** md  
**SHA-256:** `8a2123293cf11c77ba1663bc00ed9b6c268f78a10416ef1728e1678b84c4b5b3`  

---

## R0941 · SHV-Bench R9 Deposit-Gate Adversarial Audit

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: SB_R9_GPT_FINAL_AUDIT.md
- source_format: md
- text_sha256: 8a2123293cf11c77ba1663bc00ed9b6c268f78a10416ef1728e1678b84c4b5b3

# SHV-Bench R9 Deposit-Gate Adversarial Audit

**Auditor:** S03 / GPT-5.6 Sol
**Mode:** ADVERSARIAL / FRESH
**Packet:** `SB_R9_GPT_FINAL.zip`
**Date:** 2026-08-22

## Required Verdict Block

- **VERDICT:** **HALT**
- **R8 DISPOSITIONS:**
  - `F-S03-R7-04` — **CLOSED**
  - `N-S03-R8-01` — **CLOSED**
  - `N-S03-R8-02` — **CLOSED**
  - `N-S03-R8-03` — **CLOSED AS TO PRESENCE OF THE FROZEN-ANALYSIS OBLIGATION; R9 INFERENTIAL DEFECT FOUND SEPARATELY**
  - `N-S03-R8-04` — **REOPENED (LOW; typesetting only)**
- **32-CELL:** **32/32**
- **SECTION 10:** **INCOMPLETE**
- **EFFECTIVENESS VERBS:** **0** (`prevents`, `mitigates`, `ensures`, `guarantees`)
- **NEW FINDINGS:** **4** — 3 HIGH, 1 MEDIUM
- **BLIND SPOT:** This audit verifies the deposited protocol/corpus bytes and internal specification, but cannot verify the future pre-run manifest or companion artifacts because those bytes are expressly not part of this deposit.
- **SUMMARY:** R9 successfully repairs the R8 endpoint-language, post-outcome-rubric, seed-grinding, and analysis-artifact-presence issues, and the 32-cell decision mapping is total. The corpus also matches the protocol's bound SHA-256 and stated 1,673-row/classification facts. Deposit should nevertheless halt because Section 10 omits the Tier 2/3 eligibility manifest required by Sections 3.3 and 4.3; the frozen Wilcoxon implementation rules are internally inconsistent and do not specify the claimed exact handling of ties/zeros; and the protocol leaves the confirmatory tier allocation undefined when the pilot-derived required N is below 800. The BH subgroup rule is also stated as an individual threshold rather than the standard step-up rule. The page-12 table collision persists but is non-content-bearing.

---

## 1. Artifact Integrity and Corpus Checks

The packet contains:

1. `SHV_BENCH_PROTOCOL_R9.pdf` — 15 pages.
2. `SHV_BENCH_TASK_CORPUS_DEPOSIT.csv` — 1,673 data rows.
3. `S03_R9_FINAL_DISPATCH.txt`.
4. `Publication_Posture_v0_1.txt`.

### Corpus binding

Protocol Section 3.1 binds the corpus to:

`6ad72bd43ffd50658a72b787f7e07b231bb5b6fdd181be01573444f885ae48bb`

The deposited CSV hashes to exactly:

`6ad72bd43ffd50658a72b787f7e07b231bb5b6fdd181be01573444f885ae48bb`

**Result: PASS.** The filename differs from the prose aliases, but the protocol explicitly makes the digest authoritative regardless of filename.

### Corpus structure

- Rows: **1,673**
- Unique CVE IDs: **1,673**
- Duplicate CVE IDs: **0**
- Columns: **10**, matching Section 3.1
- Blank `cwes` entries: **171**, matching Section 5.1
- Reimplementation of the ordered keyword classifier in Section 3.2 against all 1,673 rows: **0 classification mismatches**
- Class counts reproduce the paper's table exactly.

**Result: PASS.**

---

## 2. R8 Finding Verification

| Finding | R9 verification | Disposition |
|---|---|---|
| `F-S03-R7-04` endpoint language | The only `non-canary` occurrence is the Section 3.5 sampling-pool statement. Primary E1/E2 are explicitly computed on the full ASA population including canaries, with no non-canary recomputation. | **CLOSED** |
| `N-S03-R8-01` post-outcome rubric mutation | Section 5.1 now states that kappa failure yields `UNSCORABLE`; any rerun requires a versioned rubric amendment hash-bound before new sessions; no revision against outcome-bearing sessions is permitted. | **CLOSED** |
| `N-S03-R8-02` grindable confirmatory seed | Section 4.3 commits both pilot and confirmatory seeds at manifest assembly from a cryptographic RNG, before pilot execution, with no outcome dependence and no alternate-seed trials. | **CLOSED** |
| `N-S03-R8-03` primary analysis code unfrozen | Section 10 now contains `shv_primary_analysis.py` as row 15 and enumerates seven implementation conventions. The requested structural repair is present. A separate R9 HIGH finding below concerns contradictions within those conventions. | **CLOSED** |
| `N-S03-R8-04` p.12 typesetting collision | The rendered PDF still merges `shv_scope_validation_suite.json` with the adjacent `5.1` cell (`...json5.1`). Content remains recoverable. | **REOPENED — LOW** |

---

## 3. Dispatch Probes

### P1 — Scope honesty

**PASS.** No material scope drift found. The protocol repeatedly distinguishes a design/preregistration contribution from an empirical effectiveness result, acknowledges that corpus composition was inspected during design, and frames the freeze as before outcome-bearing runs rather than before all evidence.

### P3 — Effectiveness verbs

Case-insensitive whole-word scan of the PDF text for the prohibited posture verbs:

- `prevents`: 0
- `mitigates`: 0
- `ensures`: 0
- `guarantees`: 0

**Count: 0. PASS.**

### P4 — 32-cell decision mapping

Applying Section 6.5 precedence to all combinations of:

- E1: reject / fail
- E2: reject / fail
- Type-1: all-pass / partial-fail / all-fail-oracle-confirms / all-fail-oracle-denies
- Type-2: clean / breach

resolves **32/32** cells to exactly one label (assuming the separate run-level `UNDERPOWERED` condition is false; if true, precedence rule 2 supersedes endpoint labels).

Resolved-label counts across the 32 cells:

- `RUN-INVALID`: 8
- `NEGATIVE-CONTAINMENT`: 12
- `NEGATIVE-CAPABILITY`: 6
- `POSITIVE-WITH-CANARY-CAVEAT`: 4
- `POSITIVE-WITH-CONTAINMENT-BREACH`: 1
- `POSITIVE`: 1

**Result: 32/32. PASS.**

### P5 — Section 10 completeness

The Section 10 table contains **15 rows** and the requested seven-convention analysis block. However, it is **not complete against the paper's own manifest-binding references**.

Sections 3.3 and 4.3 require the Tier 2/Tier 3 **eligibility manifest** (the list of eligible CVE IDs per tier) to be frozen and SHA-256-bound in the benchmark manifest before a run. No eligibility-manifest artifact appears in Section 10's pre-run obligation table.

Because F-SB12 invalidates a run only when an artifact **in the table** is absent from the benchmark manifest, the omitted eligibility manifest is not covered by the stated kill switch even though it determines the confirmatory sampling frame.

**Result: INCOMPLETE.**

---

## 4. New Findings

### N-S03-R9-01 — HIGH — Required eligibility manifest omitted from Section 10 / F-SB12 coverage

**Evidence:** Section 3.3 states that the Tier 2/Tier 3 eligibility manifest is frozen with a SHA-256 digest in the benchmark manifest. Section 4.3 explicitly samples Tier 2 and Tier 3 from those eligibility manifests. Section 10 lists 15 required companion artifacts but does not list the eligibility manifest(s).

**Why this is load-bearing:** Eligibility determines which KEV entries can enter Tier 2/Tier 3. If those bytes are not an explicit pre-run obligation, the sampling frame can change while the run still satisfies the literal F-SB12 table test. This defeats the intended byte-level freeze for a primary design component.

**Minimum repair:** Add the Tier 2/Tier 3 eligibility manifest artifact(s) to Section 10 with SHA-256 binding, and make F-SB12 apply to every manifest-bound companion artifact referenced anywhere in the protocol, not only artifacts appearing in the table.

### N-S03-R9-02 — HIGH — Frozen Wilcoxon implementation is internally inconsistent

Section 10 freezes three statements that do not form one coherent executable rule:

1. `Zero paired differences` are assigned the **Pratt convention**, but the text says zeros "contribute to the test statistic." Under the standard Pratt convention, zeros participate in ranking but their zero ranks are not added to the signed-rank statistic; they affect the ranks/variance of nonzero observations.
2. `Tied absolute ranks` require an **exact null distribution conditional on the observed tie structure**.
3. `Exact p-values` permit `scipy.stats.wilcoxon(..., method='exact')` for `N <= 25`. SciPy's documented exact method is not an exact tie/zero-conditional calculation when ties or zeros are present; the protocol explicitly expects ties and zeros.

A further contradiction appears in Section 6.4: candidate N ranges from 100 to 800 and each Monte Carlo draw is instructed to use the **exact Wilcoxon signed-rank test**, while Section 10 requires the approximate method for all `N > 25`.

**Why this is load-bearing:** These rules govern the co-primary inferential engine and the sample-size/power calculation. Different reasonable implementations can produce different p-values, required N, and ultimately different gate outcomes.

**Minimum repair:** Specify one executable algorithm for zeros/ties and p-values; either provide a true conditional permutation/exact method for the supported small-N cases or explicitly use the asymptotic/permutation method appropriate to ties/zeros. Make Section 6.4 call the same method as the final primary analysis for each candidate N. Correct the Pratt description.

### N-S03-R9-03 — HIGH — Confirmatory N is pilot-dependent, but tier allocation is frozen only for N=800

Section 4.3 says the pilot may inform the **confirmatory sample size** through Section 6.4, and Section 6.4 chooses the smallest candidate `N` from 100 to 800 satisfying joint power. Yet Section 4.3 also presents the confirmatory run as **800 tasks** and freezes a tier allocation of `250/250/200/100`, which sums only to 800.

No deterministic rule specifies Tier 1/2/3/4 allocations when the required N is 100, 150, ..., 750. Nor does the protocol state that the run always uses all 800 regardless of the computed required N.

**Why this is load-bearing:** Tier composition affects endpoint distributions and subgroup structure. Leaving allocation unresolved until after pilot data creates outcome-bearing discretion precisely where the paper claims the confirmatory design is frozen.

**Minimum repair:** Choose one of two designs and state it unambiguously: (a) always run N=800 and treat Section 6.4 only as a prospective sufficiency diagnostic, or (b) use pilot-derived N and predeclare an exact deterministic tier-allocation/truncation algorithm for every candidate N, including canary placement and the Tier-4 shortfall rule.

### N-S03-R9-04 — MEDIUM — BH subgroup procedure is stated as an individual threshold, not the BH step-up rule

Section 10 states: `p_(k) is rejected if p_(k) <= k*q/8`. Standard Benjamini-Hochberg is a step-up procedure: identify the largest qualifying `k`, then reject all hypotheses with ranks `1..k`. Applying the displayed inequality independently to each ordered p-value is not equivalent in all cases and can create non-prefix rejection sets.

**Impact:** This affects the eight subgroup analyses, not the two co-primary pooled gate decisions, so severity is MEDIUM rather than HIGH.

**Minimum repair:** State the largest-k step-up rule explicitly and freeze that implementation in `shv_primary_analysis.py`.

---

## 5. Non-blocking Presentation Finding

### N-S03-R8-04 — LOW — p.12 Section 10 table collision persists

The first half of the Section 10 table visually renders `shv_scope_validation_suite.json` into the adjacent Section cell, producing `...json5.1`. The meaning is recoverable from context and extraction, so this is not content-bearing, but the R8 low-severity finding is not closed.

**Minimum repair:** Widen the artifact column or wrap the filename before final deposit rendering.

---

## 6. Deposit-Gate Decision

**HALT.** The R9 packet cannot receive a deposit PASS while HIGH findings remain. The smallest repair set is:

1. Add the Tier 2/Tier 3 eligibility manifest(s) to Section 10 and expand F-SB12 to all protocol-referenced manifest-bound artifacts.
2. Replace the contradictory Wilcoxon/Pratt/exact-tie rules with one executable, statistically coherent algorithm and use it consistently in power simulation and final analysis.
3. Freeze a deterministic confirmatory tier-allocation rule for every pilot-derived N, or declare that confirmatory N is always 800.
4. Correct the BH step-up wording.
5. Fix the p.12 table collision before publication-quality rendering.

After those repairs, the specific R8 HIGH findings need not be reopened unless their corresponding text changes again.

---

# Bismillah ir-Rahman ir-Rahim
