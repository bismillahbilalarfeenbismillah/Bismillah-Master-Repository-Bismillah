# Bismillah ir-Rahman ir-Rahim

# R0343 -- Seat and carrying status

**Chronological Index:** 122 of 995  
**Date:** 2026  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** SHVVP_v0_3_SEAT_A_GPT_VERDICT.md  
**Source Format:** md  
**SHA-256:** `6008e18c9785ecbbd8d5c6898d63338092be79ce9742fcd440c3fe8c76a150cf`  

---

## R0343 · Seat and carrying status

- section: V. BSSG & SHVVP Protocols
- source_file: SHVVP_v0_3_SEAT_A_GPT_VERDICT.md
- source_format: md
- text_sha256: 6008e18c9785ecbbd8d5c6898d63338092be79ce9742fcd440c3fe8c76a150cf

# HALT

## Seat and carrying status

**Seat A — GPT-class / OpenAI-family, independent non-producer carrying seat.**

This is one carrying verdict. It does not carry the artifact by itself. Convergence requires agreement by both non-producer seats from different vendor families. Because this verdict is **HALT**, deposit is blocked and v0.4 is required under the dispatch rule.

## Executive determination

The packet passed custody, lineage, rendering, anchor, arithmetic, Phase B finite-state enumeration, BH step-up, shipped-test, and simulation-reproduction checks. It nevertheless fails the core executability standard:

1. the frozen null-centred route bootstrap can report \(p=1/10001\) for 50/50 successes against \(H_0:\pi\le0.98\), although the exact boundary probability is \(0.98^{50}=0.36417\);
2. route evaluability thresholds are recorded but not enforced by the normative claim code;
3. `phase_c_label` returns `PASS-ALL-SIX` when adjudicator alpha is undefined (`NaN`), even when C1 is marked failed;
4. Sections 6.2 and 6.3 create two outcome names absent from the supposedly closed eight-label mapping;
5. Section 11 still freezes a 1,280-session deliverable although Sections 6.8 and 13 freeze 1,440;
6. the documented reproduction command uses defaults different from the frozen receipt.

These are substantive defects in a preregistration whose principal claim is that no motivated analyst can reinterpret or manufacture an inferential outcome after unblinding.

## Findings

### F-P3-1

- **ID:** F-P3-1
- **SEVERITY:** HIGH, BLOCKING
- **Locus (by contract section):** Sections 8.2–8.4; `bootstrap_p_one_sided`; amendment A-3.3
- **Substance:** The null-centred nonparametric cluster bootstrap is severely anti-conservative at an attainable boundary. With 50 one-item clusters all equal to 1 for R2-B, the shipped code returns \(p=0.00009999\) against \(H_0:\pi\le0.98\). Under the least-favourable Bernoulli null, the probability of 50/50 successes is \(0.98^{50}=0.36417\). Likewise, R6-B/C at its minimum 30 items returns \(0.00009999\) for 30/30 although \(0.95^{30}=0.21464\). Degenerate empirical resamples contain no null variance; translation does not restore it. BH can therefore certify an inferential route where a valid boundary test plainly would not.
- **Disposition:** **HALT.** Replace the p-value rule with a valid predeclared clustered test whose size is calibrated at the high-proportion boundary, then rerun route tests and carrying audit.
- **Cross-reference:** Axis 1.7; regression F-P2-3; independent output `shvvp_v0_3_seat_a_independent_checks.json`. **Unanticipated by producer; lead adjudication required.**

### F-P3-2

- **ID:** F-P3-2
- **SEVERITY:** HIGH, BLOCKING
- **Locus (by contract section):** Sections 6.8 and 8.2–8.4; `bootstrap_p_one_sided`; `route_claims`
- **Substance:** The normative code does not enforce the component-specific minimum evaluable counts. `bootstrap_p_one_sided` reports `evaluable=True` for any positive item count; `route_claims` trusts a caller-supplied Boolean and never checks `n_items` against the registry threshold. An analyst can therefore enter a below-threshold R2-B, R4-B/C, or R6-B/C p-value into F3a and obtain `SUPPORTED-INFERENTIAL`.
- **Disposition:** **HALT.** Bind component key, observed count, registry threshold, p-value generation, BH membership, and route claim in one fail-closed executable path.
- **Cross-reference:** Axis 1.7 and 1.9; regression F-P2-3. **Unanticipated by producer; lead adjudication required.**

### F-P3-3

- **ID:** F-P3-3
- **SEVERITY:** HIGH, BLOCKING
- **Locus (by contract section):** Sections 7.4–7.5; `phase_c_label`; amendment A-3.4
- **Substance:** Phase C totality was tested only on a finite hand-chosen grid of ordinary floats. For `alpha_c1=NaN`, clean other inputs return `PASS-ALL-SIX`; even `C1=True` still returns `PASS-ALL-SIX`. Comparisons against `NaN` are false, so the inadmissible adjudication and hard-failure branches are skipped. Undefined alpha is a possible adjudication result and has no frozen fail-closed handling.
- **Disposition:** **HALT.** Define handling for undefined/non-finite alpha and all invalid metric values; reject or map them fail-closed before label evaluation; independently enumerate the expanded domain.
- **Cross-reference:** Axis 1.8; regression F-P2-4; independent output `shvvp_v0_3_seat_a_independent_checks.json`. **Unanticipated by producer; lead adjudication required.**

### F-P3-4

- **ID:** F-P3-4
- **SEVERITY:** HIGH, BLOCKING
- **Locus (by contract section):** Sections 6.2–6.4
- **Substance:** Section 6.4 declares eight labels exhaustive and prohibits any other label, but Section 6.2 says G1 failure is “recorded as `INCONCLUSIVE-CANARY-INSENSITIVE`” and Section 6.3 says G2 failure is “recorded as `UNINFORMATIVE-LOW-BASE`.” Neither appears in the eight-label list or code, which instead returns `INCONCLUSIVE-DESIGN-VALIDITY`. A hostile reader can treat these as outcome labels or annotations.
- **Disposition:** **HALT.** Remove the stray names or define them unambiguously as non-label guard annotations subordinate to L2.
- **Cross-reference:** Axis 1.1 and 1.9; regression F-P2-2. **Unanticipated by producer; lead adjudication required.**

### F-P3-5

- **ID:** F-P3-5
- **SEVERITY:** HIGH, BLOCKING
- **Locus (by contract section):** Sections 6.8, 11 and 13
- **Substance:** Section 6.8 and A-3.1 freeze 1,440 sessions, but the frozen deliverables in Section 11 still specify a “1,280-session confirmatory run.” This is a direct contradiction in a frozen numeric design commitment.
- **Disposition:** **HALT.** Change Section 11 to 1,440 in a new frozen version and audit every downstream rendering and metadata reference.
- **Cross-reference:** Axis 3.2 and Axis 4.5; regression F-P2-1. **Unanticipated by producer; lead adjudication required.**

### F-P3-6

- **ID:** F-P3-6
- **SEVERITY:** MEDIUM
- **Locus (by contract section):** Section 6.8; README §3; `shvvp_v0_3_power_sim.py`
- **Substance:** README says `python shvvp_v0_3_power_sim.py --stage all --json power_sim_receipt.json` reproduces the frozen receipt, but defaults are 400/2,000/2,000/600 simulations rather than the receipt’s 500/3,000/3,000/1,000. Standalone `--stage calib` and `--stage sens` also silently use 8 repetitions, not the frozen 9, with no calibration/sensitivity repetition CLI option.
- **Disposition:** Required amendment in v0.4: make frozen counts the defaults or publish the complete command; expose/fix the frozen-design repetition argument and test standalone stages.
- **Cross-reference:** Axis 1.3–1.6; mandatory simulation reproduction. **Unanticipated by producer; lead adjudication required.**

## Four-axis analysis

### Axis 1 — Executability of every decision rule

**Phase B mapping.** I independently enumerated all \(2^8=256\) Boolean inputs and compared the shipped function with an independently written ordered oracle. There were zero mismatches; all eight labels were reachable and no code output fell outside the tuple. Missingness, design validity, non-estimability, ASA failure, discordance, and success priorities were implemented as stated. The prose closure fails separately under F-P3-4.

**Population evaluation.** H and N are defined for ASA and PP. Forward discordance maps to L5/L7; reverse discordance correctly remains observed ASA failure. `h_estimable` represents the stated disjunction across either population, although that disjunction must be computed by the caller.

**Intervals and zero events.** I read and executed `bca_bounds`, `evaluate_trial`, and the self-test. Bias correction uses the proportion strictly below the estimate; acceleration uses leave-one-cell-out jackknife values; cells are resampled within variant; one shared index set feeds RD, RR and DeltaS; no continuity correction appears. Z-1 through Z-4 and fallback counters are present. The self-test returned `selftest OK`.

**Joint estimation and correlation.** Trial outcomes are generated jointly through the declared Gaussian copula; SUCCESS is counted per replicate and powers are never multiplied. Completed sensitivity reruns at rho 0, 0.30 and 0.60 matched the receipt exactly and showed stable joint-power estimates 0.868, 0.874 and 0.870.

**Design selection and boundary calibration.** Recomputed Monte Carlo estimates, standard errors and Wald intervals from receipt counts had no discrepancy. Among authoritative Stage 2 rows, 8 repetitions has lower bound 0.7853, 9 has 0.8590 and 10 has 0.9012; the rule selects 9 repetitions/1,440 sessions. Staging uses Stage 1 to choose the bracket, so “smallest” is conditional on that screen rather than Stage 2 evaluation of the full ladder, but the screened lower designs were plainly below target. Boundary-calibration reruns at 9 repetitions matched 0.0247 for N and 0.0127 for H; the declared \(>0.030\) switch is not triggered on those simulated point estimates. F-P3-5 still makes the frozen size internally inconsistent.

**Route inference.** The eleven-component registry and F3a/F3b membership match the tables; Class G treatment is generally honest; cross-phase combination is conjunction-only; no Fisher path exists in code. My independent BH implementation matched `bh_reject` in 203 cases, including NaNs and empty families. Route inference nonetheless fails for the invalid boundary p-values and unenforced evaluability thresholds in F-P3-1 and F-P3-2.

**Phase C.** For finite, ordinary inputs, mechanical and admissible adjudicated failures dominate inconclusive states; alpha below 0.67 produces indeterminate adjudication; UNKNOWN dominates tentative reliability; PASS requires alpha at least 0.80. Undefined alpha defeats that order and can manufacture PASS under F-P3-3.

**Text versus code.** F-P3-4 and F-P3-6 are direct divergences. F-P3-2 is a missing executable binding. The code constants otherwise match the central thresholds and families.

### Axis 2 — Empirical anchors and citations

**CVE-2026-4747.** The live [Anthropic primary](https://www.anthropic.com/research/mythos-preview) explicitly names “FreeBSD’s NFS server” in the sentence about full root access, unauthenticated users, and a 20-gadget ROP chain split over multiple packets. The same FreeBSD account says the chain was over 1,000 bytes and split into six sequential RPC requests. The contract attributes the unauthenticated-root claim to Anthropic rather than adopting it as uncontested fact. The [FreeBSD advisory](https://www.freebsd.org/security/advisories/FreeBSD-SA-26:08.rpcsec_gss.asc) says both that exploitation “does not require the client to authenticate itself first” and that kernel RCE is possible by “an authenticated user”; `UNKNOWN-CONTESTED` is appropriate. The contract does not use the CVE as a discovery-novelty label.

**Round 1 Gemini rejection.** I agree with rejection of F-PP-3. The [Anthropic primary](https://www.anthropic.com/research/mythos-preview) assigns the 20-gadget chain to FreeBSD. Its OpenBSD SACK case is a null-pointer crash described as denial of service, not a ROP chain.

**AISI “The Last Ones.”** The live [AISI primary](https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities) supports 3/10 full completions, average 22/32 steps, next-best 16, and a 100M-token budget. It also states that the ranges lack active defenders/defensive tooling and impose no penalty for alert-triggering actions. The contract’s caveat is faithful.

**Identifiers and methods.** [Zenodo 21450932](https://doi.org/10.5281/zenodo.21450932) resolves to verification method v1.1; [Zenodo 21449063](https://doi.org/10.5281/zenodo.21449063) resolves to v1.0. [Zenodo 21539074](https://doi.org/10.5281/zenodo.21539074) resolves to the A5 evidence-independence paper; the contract correctly keeps A5 UNDER TEST. Sources 31–33 are real and germane: [DiCiccio and Efron](https://projecteuclid.org/journals/statistical-science/volume-11/issue-3/Bootstrap-confidence-intervals/10.1214/ss/1032280214.pdf) defines bias-corrected and accelerated intervals; [Efron and Tibshirani](https://projecteuclid.org/journals/statistical-science/volume-1/issue-1/Bootstrap-Methods-for-Standard-Errors-Confidence-Intervals-and-Other-Measures/10.1214/ss/1177013815.full) is the cited bootstrap-method review; and the [cluster-bootstrap paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC5965657/) instructs sampling clusters with replacement and retaining all observations in selected clusters.

**Fabrication check.** I extracted all 34 unique contract URLs and requested each live. Twenty-nine returned HTTP 200 directly; five publisher endpoints returned access-control 403 to command-line requests, but their documents were independently identifiable, including the [Benjamini–Hochberg article](https://academic.oup.com/jrsssb/article/57/1/289/7035855). I found no fabricated URL or mismatched anchor. This resolution check does not convert the contract’s expressly `UNKNOWN-PENDING-DEPOSIT` XZ/CVE-Bench repository URLs into asserted citations.

### Axis 3 — Internal consistency and completeness

The seven-item residual UNKNOWN list covers the named unresolved quantities, but undefined reliability statistics are not handled as an input state (F-P3-3). Arithmetic identities hold: Phase B 40×2×9×2 = 1,440, 80 cells and 720 per arm; ceiling 40×2×12×2 = 1,920; Phase C 48×3×3×2 = 864, 432 per arm and 9 C-BSSG sessions per target; 36+12=48; overlays 24/6/18; Phase A denominators 200/240/16/12/60 are present. Section 11’s 1,280 figure contradicts these commitments (F-P3-5).

The BSSG authorization rule remains five-conjunct and fail-closed; monotonicity narrows authority. Each phase states a falsifier and safety boundary; the Phase C live-target boundary remains non-amendable. Sections 12–13 and the separate adjudication record preserve accepted and rejected findings and the non-carrying Gemini PASS. The three normative modules are not fully complete because of F-P3-1 through F-P3-3.

### Axis 4 — Scope honesty

The canonical source says no corpus, pilot, confirmatory session, Phase C target, result, or empirical validation exists. Simulation values are identified as synthetic operating characteristics under assumptions. v0.1 and v0.2 are consistently HALTED, never deposited and nonbinding; v0.3 has no verdict at freeze and needs two-family convergence. The round 2 Gemini PASS is preserved byte-for-byte and not downgraded. Growth from 1,280 to 1,440 is disclosed in Sections 6.8 and 13, but Section 11 accidentally retains the old future deliverable (F-P3-5).

## Mandatory regression tables

### Round 2

| Prior item | Status | Exact v0.3 locus | Grade / explanation |
|---|---|---|---|
| F-P2-1 | **ABSORBED**, with new internal-size defect | §§6.5, 6.5.1, 6.8; `shvvp_v0_3_power_sim.py`; A-3.1 | Core BCa, zero-event, joint simulation, SUCCESS-share power, seeds and receipt are implemented and independently reproduced. Section 11’s 1,280 conflicts with the selected 1,440: F-P3-5 HIGH/BLOCKING. |
| F-P2-2 | **PARTIALLY ABSORBED** | §§6.2–6.6; `phase_b_label`; A-3.2 | Code mapping is total/closed over 256 Boolean states and populations are bound, but §§6.2–6.3 introduce two names outside the closed list: F-P3-4 HIGH/BLOCKING. |
| F-P2-3 | **NOT ABSORBED** | §§6.8, 8.1–8.4; `shvvp_v0_3_route_inference.py`; A-3.3 | Registry/BH/conjunction exist, but the p-value is invalid at attainable high-null boundaries and thresholds are not enforced: F-P3-1/F-P3-2 HIGH/BLOCKING. |
| F-P2-4 | **PARTIALLY ABSORBED** | §§7.4–7.5; `phase_c_label`; A-3.4 | Priority works on the tested finite grid, but undefined alpha can yield PASS, even with failed C1: F-P3-3 HIGH/BLOCKING. |
| Gemini-class PASS | **ABSORBED** | §0.3; A-3.5; shipped verdict | Preserved unmodified, not reinterpreted, and its limits recorded. |

### Round 1

| Prior item | Status | Exact v0.3 locus | Grade / explanation |
|---|---|---|---|
| GPT F-PP-1 and F-PP-2 | **ABSORBED** | §§5.2–5.4, 6.1–6.4 | Numeric targets, metrics, thresholds and reliability gate remain fixed; new defects are separately recorded. |
| GPT F-PP-3 | **ABSORBED** | §§7.1–7.5 | Corpus, allocation, conjunct scoring and thresholds remain specified. |
| GPT F-PP-4 | **ABSORBED** for instrumentation/scope; later inference defective | §8.2 | Eleven component rows commit data units, gates and out-of-scope handling; F-P3-1/F-P3-2 concern the new inference layer. |
| GPT F-PP-5 | **ABSORBED** | §§0.1, 6.9 | UNKNOWN discipline and exploratory-only pilot limits remain explicit. |
| GPT F-PP-6 and Gemini F-PP-3 | **ABSORBED** | §§2.2–2.3 | Attribution, dual FreeBSD descriptions, contested authentication and rejection record match the primary. |
| Gemini F-PP-1 | **ABSORBED** | §6.3; A-2.8 | Margin is substantive and fixed; variance-derived formula remains rejected. I agree with that rejection. |
| Chair DOI note | **ABSORBED** | §14 source 3; A-2.9 | v1.1 and earlier v1.0 identifiers resolve as stated. |

## Independent adjudication

I agree that all four round 2 findings were correctly accepted in full; each identified a genuine executability defect. I do **not** agree that all were fully absorbed in v0.3: F-P2-3 remains unabsorbed, while F-P2-2 and F-P2-4 are only partial.

I agree with both round 1 rejections/dispositions relevant here: the proposed variance-derived margin remedy was correctly rejected while its concern was absorbed, and Gemini F-PP-3 was correctly rejected because the Anthropic primary assigns the 20-gadget statement to FreeBSD, not OpenBSD.

## Chain of custody and lineage

- Recomputed archive SHA-256: `482f0faf4b55f998340e3be17073e3ede75885fa6e4a452dad4ec321114ace51` — exact expected match.
- Inspected 34 ZIP entries before extraction: no absolute path, `..` traversal, symlink, or non-regular member.
- Fresh-extracted to `/home/user/workspace/shvvp_v0_3_seat_a_fresh_extract/SHVVP_v0_3_REAUDIT_DISPATCH_PACKET`.
- Ran `sha256sum -c SHA256SUMS`: all 33 listed members matched; manifest excludes itself; no unlisted or missing member.
- Independently recomputed hashes for every extracted member, including the manifest. All eight historical lineage receipts match the brief.
- I modified no packet member. All audit scripts, logs, rendered pages, and rerun receipts were written outside the packet directory.

## Code executed versus trusted

**Executed by this seat:**

- shipped `test_shvvp_v0_3_rules.py`: 54 PASS, 0 failed;
- shipped simulation self-test: `selftest OK`;
- independent 256-state Phase B oracle comparison;
- independent BH step-up comparison over 203 cases;
- independent boundary p-value counterexamples;
- independent Phase C undefined-alpha counterexamples;
- complete Stage 1, Stage 2, Stage 3 and Stage 4 reruns at 500/3,000/3,000/1,000 simulations and 1,000/10,000 bootstrap counts; all stage payloads matched the shipped receipt exactly apart from runtime seconds;
- receipt Monte Carlo arithmetic and frozen selection;
- `qpdf --check`, metadata, font embedding, 30-page render, pixel-level monochrome check, hyperlink-annotation check, source mechanics, member hashes, URL resolution and live anchor fetches;
- producer verifier only for orientation; it returned 15 PASS, but I did not rely on it.

The first single-process full simulation attempt reached all four stages but exceeded the sandbox time limit before writing JSON. I therefore reran each stage to completion; because standalone calibration/sensitivity silently use 8 repetitions, I invoked the shipped stage functions from a separate seat-owned wrapper at the frozen 9 repetitions. The resulting four stage payloads matched exactly.

**Trusted:** cryptographic implementations supplied by the operating environment; PDF rendering libraries for mechanical inspection; publisher/primary pages for the cited factual records. I did not trust producer receipts, verifier conclusions, tests, or adjudication assertions without separate checks.

## PDF and secondary mechanics

`qpdf --check` found no syntax or stream errors. Metadata matches title/version/author and records both halted predecessors. All six fonts are embedded/subset. Thirty rendered pages contained zero non-gray pixels; 128 link annotations cover all 34 unique source URLs. Visual inspection of all-page contact sheet and detailed Section 6.4, figure, and route/deliverable pages found no clipping, overlap, or missing glyphs. The route table is dense but legible. Canonical source is ASCII-only, has zero U+2013/U+2014/U+2015, no doubled words, no placeholders, and the required final `BayyinahEnterprise` spelling.

## Limits — checks not performed

- I did not rebuild the PDF, DOCX, HTML, chart, source, manifest, or packet, because rebuilding would alter the artifact.
- I did not execute `finalize_packet_v0_3.py`, `inject_sim_values_v0_3.py`, or the PDF/chart builders.
- I did not conduct a human peer review of the scientific thesis, validate SHV or BSSG, or inspect nonexistent empirical data.
- I did not prove universal statistical validity of every secondary method. I did test the primary interval implementation, route p-value at decisive boundary cases, BH, Monte Carlo arithmetic, and declared calibration.
- I checked every cited URL for resolution and checked anchor/method claims against live primaries, but I did not reproduce every external paper’s underlying study.

## Final carrying statement

**HALT.** This Seat A verdict is carrying but insufficient alone for convergence. The blocking findings require a new frozen v0.4, append-only adjudication, new hashes, and a fresh two-family carrying audit. Producer, editor, chair, verifier, or this single family cannot substitute for the second independent carrying seat.

---

# Bismillah ir-Rahman ir-Rahim
