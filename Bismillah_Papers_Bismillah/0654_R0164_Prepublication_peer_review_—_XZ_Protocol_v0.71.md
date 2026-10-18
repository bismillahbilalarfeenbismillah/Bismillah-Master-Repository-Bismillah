# Bismillah ir-Rahman ir-Rahim

# R0164 -- Prepublication peer review — XZ Protocol v0.71

**Chronological Index:** 654 of 995  
**Date:** Undated  
**Section:** IV. XZ Protocol  
**Source File:** PEER_REVIEW_GPT.md  
**Source Format:** md  
**SHA-256:** `ba8137f797871713b2263fa140b535ae98112b545f1e5790b4fde918bbbb22c7`  

---

## R0164 · Prepublication peer review — XZ Protocol v0.71

- section: IV. XZ Protocol
- source_file: PEER_REVIEW_GPT.md
- source_format: md
- text_sha256: ba8137f797871713b2263fa140b535ae98112b545f1e5790b4fde918bbbb22c7

# Prepublication peer review — XZ Protocol v0.71

**Recommendation: HALT / Major Revision. Do not publish or deposit v0.71 as “FROZEN” in its current form.**

I reviewed the canonical v0.71 source, the rendered 107-page PDF, executable package, build/test suite, R27/R28 reports, R28 cross-seat triage, methodology document, amendment/seal history, and supporting generators. I also executed the supplied build and tests.

This is an **independent technical/model-based peer review, not independent human peer review**. It therefore does not itself satisfy the manuscript's stated requirement for human peer review or its separate two-family carrying-seat requirement.

## Executive assessment

There is a substantial and potentially publishable methodological contribution here. The protocol has unusually strong practices around explicit UNKNOWN states, denominator discipline, preregistered decision rules, append-only amendment history, executable checks, adversarial testing, and explicit separation between protocol claims and later empirical claims.

The problem is that **the current v0.71 freeze decision is contradicted by the artifact itself**.

Mechanically, the package is healthy:

| Verification | Result |
|---|---|
| Canonical build | **PASS** |
| Explicit test suite | **186/186 PASS** |
| Packet SHA-256 verification | **PASS** |
| Amendment seals | **71/71 verify** |
| PDF | Readable; sampled critical sections correspond to source |
| PDF length | 107 pages |

Those facts establish reproducibility of the packaged state. They **do not establish semantic correctness of that state**. In fact, several publication-blocking semantic defects remain outside what the green build currently proves.

### Publication-blocking findings

1. **The document cannot consistently call itself FROZEN under its own governance rules. — CRITICAL**

   The contradiction is direct, not interpretive.

   `xz_protocol_v0_71.md:4–5` declares **“0.71, FROZEN”** and describes v0.71 as a FROZEN repair build. Yet `:18` says **“Current status: PENDING RE-CARRY on v0.71 bytes,”** and `:20` states **“FB-8 ... is OPEN.”**

   Section 25 is even more explicit. At `:760`, the manuscript says FROZEN status may be issued only when every freeze-blocker is satisfied **and** the Section 22 carry rule has been satisfied. But `:771` says FB-7b is **“PENDING RE-CARRY v0.71”**, and `:772` leaves FB-8 **OPEN**.

   Section 22 (`:701–702`) requires two executing non-producer seats from different vendor families and says that a carrying-seat **HALT blocks freeze**. Its special persistent-HALT exception explicitly says it **does not apply to Class A or Class B findings**.

   Yet the v0.71 entry itself records R28 as **4/4 HALT**, with Class A findings (`:1645–1647`).

   Finally, the canonical manuscript ends twice with:

   > `End of XZ Protocol v0.71 draft candidate.`

   at `:1685` and `:1689`.

   The manuscript is therefore simultaneously **FROZEN**, **PENDING RE-CARRY**, **FB-8 OPEN**, and a **draft candidate**.

   Under the protocol's own declared rules, the defensible current state is **DRAFT CANDIDATE / HALT**, not FROZEN.

2. **The R28 cross-seat triage incorporated into the frozen record is materially misbound. — CRITICAL**

   I compared the individual R28 reports against `R28_CROSS_SEAT_TRIAGE.md` and then against the v0.71 amendment entry at `:1649–1666`.

   R28 contains **37 actual findings**: 9 from S01, 8 from S02, 2 from S03, and 18 from S04.

   The published triage accounts for only **35 unique finding IDs**. Two actual R28 findings disappear from the synthesis:

   **`F-S02-70-02`**, a HIGH Class-A C-suffix extraction defect, and **`F-S04-70-05`**, a HIGH Class-A contradictory-disposition defect.

   The text claims **“NOTED (19 items)”** at `:1666`, but only **17 IDs are actually enumerated**.

   More seriously, several convergence groups bind the *wrong IDs* to the claimed substance. For example, Group 1 says the C-suffix convergence consists partly of `F-S01-70-05` and `F-S02-70-06`. The individual reports show that the actual C-suffix findings are **`F-S01-70-02` and `F-S02-70-02`**. `F-S01-70-05` concerns overbroad declaration-context matching; `F-S02-70-06` concerns a contradictory hardcoded gate summary.

   Likewise, Group 3 binds `F-S02-70-07` to hardcoded zero summaries, whereas that report's `F-S02-70-07` is the **tagging-completeness** finding; its hardcoded-summary finding is `F-S02-70-06`.

   Group 4 binds `F-S04-70-04` to register reproduction failure, although `F-S04-70-04` is actually the **NOTED 21-versus-20 count defect**.

   This is particularly damaging because v0.71 labels these synthesis statements `[COMPUTED: ...]`. The canonical amendment record therefore contains a **finding-ID/proposition transposition error of exactly the kind the protocol is designed to prevent**.

3. **Several R28 defects remain live in the actual v0.71 tooling. v0.71 is not a substantive R28 repair. — CRITICAL**

   I tested the current v0.71 bytes rather than relying on the prose claims.

   The C-suffix defect remains. `extract_findings.py:26` allows `S\d{2}C?` in the generic `FINDING_ID_RE`, but all five operative `DECLARATION_PATTERNS` at lines 33–41 still use `S\d{2}` without `C?`. A synthetic legitimate C-suffix declaration is still dropped by the extractor.

   The register generator also remains unreproducible from the shipped index. Running it on the supplied R27 index raises a `ValueError` concerning the mixed-severity group without an adjudication receipt.

   `xz_protocol_register_gen.py:22` still defines:

   `{"HIGH", "MEDIUM", "LOW", "INFORMATIONAL"}`

   and therefore still omits **CRITICAL**, despite the v0.71 front matter claiming the CRITICAL-remap problem has been removed.

   Gate [13] in `build.py:748–792` still has a fail-open absence branch: when reports are missing it prints a disclosure but never calls `check(False, ...)`.

   Its final summary at `build.py:788–789` still literally prints:

   `0 missing, 0 phantom, 0 severity mismatches`

   rather than deriving those displayed values.

   `xz_protocol_boundaries.json` also still declares `"version": "0.62"`.

   These are not merely historical R28 findings. They remain properties of the **current v0.71 bytes**.

4. **The canonical v0.71 body itself contains readily falsifiable current-byte claims. — HIGH**

   Section 25 says at `:767` that FB-4 is backed by **“22 source-frame tests.”** The actual suite has **29** source-frame tests.

   At `:768`, it says FB-5 has **“30 control-graph tests.”** The actual suite has **18**.

   The full executed distribution is 29 Condition-A, 29 source-frame, 18 control-graph, 14 kernel, 27 adversarial, and 69 Phase-A tests = **186 total**.

   The total is correct; the component claims are not.

   At `:22`, v0.71 additionally states that the defect trajectory contains **“seventy-one amendment entries, v0.1 through v0.70.”** A sequence v0.1 through v0.70 supplies 70 version entries, not 71. Seventy-one requires inclusion of v0.71.

   The status line at `:5` also remains stale: it describes Bearer 4 at **R27** and a 21/21 recurrence even though the same document records the R28 result as 22/22.

   These are exactly the sort of finite, byte-level claims that the manuscript argues should not survive into a frozen instrument.

5. **The proposed “Gödel confinement” does not justify overriding these failures. — MAJOR THEORETICAL ISSUE**

   The epistemic intuition is reasonable: no finite test suite should be treated as proving the total absence of all defects in itself.

   But the manuscript advances a much stronger statement. At `:1679`, it claims Bearers 4, 5, and 7 are “structurally coupled,” that resolving any requires resolving all three, and that this would require the instrument to verify its own completeness, “which the Goedel sentence forbids.”

   That conclusion has not been formally established.

   The manuscript supplies no formal theory, effective axiomatization, consistency assumptions, arithmetization, undecidable proposition, reduction, or theorem demonstrating that Gödel's incompleteness theorem applies to these particular software/governance predicates.

   More importantly, the three predicates are not obviously Gödel-coupled at all. Bearer 4's empirical confinement criterion can be tested over the findings of a specified audit. Bearer 5 is an **external witness condition**: two eligible parties either return non-HALT or they do not. Bearer 7's current-entry tagging completeness is a finite syntactic property that can be checked by an external parser.

   None of those requires proving that the protocol is universally complete or free of all possible errors.

   The manuscript should therefore retain the **epistemic limitation**—roughly, “our verifier cannot establish the universal absence of defects beyond its specified checks”—but withdraw the claim that the current unresolved finite defects are **formally irreducible by Gödel's theorem** unless a genuine formal result is supplied.

   Disclosure of a defect is not equivalent to proof that the defect is logically unavoidable.

6. **The Hurst-exponent claim should be removed. — MAJOR STATISTICAL ISSUE**

   The methodology states that 21 consecutive Class-A-positive rounds produce **H = 1.0**, interpreted as “maximally persistent autocorrelation”; v0.71 extends this to 22/22.

   For a constant binary sequence of all ones, ordinary variance is zero. Standard autocorrelation and classical rescaled-range/Hurst calculations are therefore degenerate or undefined, rather than providing a meaningful empirical estimate of \(H=1\).

   The manuscript itself already contains the relevant prior finding at `:1323`:

   > `H=1.0 re-asserted on undefined R/S statistic (constant series 0/0).`

   Yet the same statistic is reintroduced in v0.71.

   This is a particularly clear case where the amendment history already documents the correction that the current manuscript needs.

   The **23/24 Laplace probability** also needs qualification. It corresponds to a simple rule-of-succession/Beta-Bernoulli calculation after 22 successes, but interpreting it as a predictive probability assumes a form of exchangeability that is implausible here: every audit round changes the artifact, tooling, repair strategy, and sometimes witness configuration. These are adaptive interventions, not repeated draws from an unchanged Bernoulli process.

   The scientifically defensible quantity is simply the observed recurrence: **Class-A findings occurred in 22/22 specified audit rounds**. That is interesting enough without giving it an unsupported Hurst exponent or calibrated predictive probability.

7. **The methodology's own provenance-tag rule fails in the freeze entry. — HIGH**

   `methodology_v7_canonical.md:301` says:

   **“Every sentence in the amendment entry carries exactly one provenance tag.”**

   It permits `[COMPUTED]`, `[TESTED]`, `[WITNESSED]`, and `[DISCLOSED]`, and at `:310` requires **zero untagged sentences**.

   The v0.71 entry does not meet this rule. It uses unsupported forms including `[ASSERTED]` and `[ENUMERATED]`; numerous sentences are untagged; and some terminal tags appear to cover several preceding sentences rather than exactly one.

   The build's current tag gate is substantially weaker than the methodology's stated criterion. Consequently, the green build does not establish Bearer 7.

   The manuscript itself labels Bearer 7 **FALSE** at `xz_protocol_v0_71.md:1675`. That is an accurate diagnosis—but a FALSE mandatory bearer cannot simply become a frozen “structural residual” without first changing the governing rule in a transparent prospective amendment.

8. **Independent witness provenance is not sufficiently authenticated for the evidentiary weight assigned to it. — HIGH**

   The four R28 reports can be inspected as files, and their technical findings can be reproduced. But the package does not cryptographically establish that each report originated unmodified from the named model/vendor/session.

   Indeed, the triage itself admits that **all four dispatch labels differed from the actual executors**. S02's dispatch identifies Kimi while the report says GPT-5.6 Sol executed it; the protocol separately says GPT is ineligible for carrying-seat credit.

   The frozen packet's checksum manifest anchors the R28 S01 report, but it does not similarly anchor all four R28 reports as immutable third-party-origin artifacts. The review package contains them, but packaging by the producer is not third-party provenance.

   This does not invalidate their technical observations. It does mean terms such as “independent,” “cross-vendor,” and “unmodified report” should be framed as **recorded process claims**, not cryptographically authenticated facts, unless external receipts or signatures are supplied.

## Scientific design review beyond the freeze defects

Even after those byte-level problems are repaired, I would require methodological revisions before journal publication.

The manuscript is called a **preregistration**, but the focal XZ event is historical and already known. The later scoring exercise can certainly be prospectively frozen, and executor blinding can reduce some bias, but the overall research design was devised with knowledge of the case and its outcome. The authors therefore cannot obtain the strongest form of prospective-preregistration protection against hypothesis/design construction after outcome knowledge. I recommend describing this explicitly as a **retrospective case-study protocol with prospectively frozen replay rules**, or similar, and discussing author-level hindsight contamination separately from evaluator blinding.

The Condition A/B comparison also needs sharper causal language. Condition B appears to contain everything available to Condition A plus additional SHV/BSSG structure. That design may estimate the incremental yield of the augmented workflow under the chosen conditions, but it is not a capability-matched experiment. Differences could reflect extra information, time, procedural attention, or tooling rather than the specific structural theory. The protocol's current restrictions on causal/effectiveness claims are a strong safeguard and should remain.

The conventional-practice baseline also needs external validation. Because the same research program defines both the proposed method and much of the comparator, there is a risk—whether intentional or not—of constructing an underpowered conventional baseline. Independent supply-chain/security practitioners should validate the baseline workflow before execution.

The paper's literature context is currently too inward-looking for a journal methods article. It needs substantive engagement with established work on software supply-chain security, reproducible builds and provenance, registered reports/preregistration for retrospective datasets, inter-rater reliability, dependency-aware qualitative coding, formal verification, and the actual mathematical literature relevant to incompleteness/self-reference. The manuscript's internal reference canon can remain, but it cannot substitute for engagement with the external field.

The theological architecture is not itself a scientific defect. The methodology explicitly says the correspondences are parallels rather than proofs. For publication in a technical venue, however, the manuscript should more visibly separate the theological/narrative nomenclature from the normative computational propositions so that readers can determine exactly which claims depend on executable definitions and which constitute interpretive framing.

## What is strong enough to preserve

Several aspects should survive revision essentially intact. The separation of `DENY_UNKNOWN` from `DENY_FALSE` is methodologically valuable. The refusal to infer favorable facts when evidence is absent is strong. The prespecified eligibility strata, denominator rules, dependency clustering, anti-pseudoreplication rules, and prohibition on generalization beyond the single case are all defensible.

The package also demonstrates an unusual level of executable transparency. I could reproduce the 186-test green state, checksum verification, and amendment-seal verification directly. The limitations section is substantially more candid than is typical for methodological manuscripts, especially regarding the single-case design, constructed comparator, pretraining contamination, governance issues, and sample-collapse risk.

Most importantly, **R28 actually demonstrates that the adversarial-review architecture is useful**: four audits found defects that a green build did not detect. That is a compelling result. The publication would be stronger if it embraced that result rather than trying to reinterpret the remaining defects as proof that the protocol has reached a Gödelian terminal state.

## Required revision before publication

The minimum defensible path is to revert the current state from **FROZEN** to **DRAFT CANDIDATE**, rebuild the R28 triage directly from all 37 finding declarations, correct the finding-ID transpositions and missing findings, repair the still-live extractor/register/gate defects, regenerate the current amendment entry from reproducible tools, correct the Section 25 component test counts and all version/range claims, and enforce the methodology's actual sentence-level provenance rules.

After those repairs, the protocol should undergo the carry process it already specifies: **two eligible non-producer, different-family executions on the exact successor bytes, with no disqualifying HALT**. FB-8 then needs to satisfy its explicit exit condition rather than being declared an accepted residual.

Separately, the paper should replace the \(H=1.0\) analysis with straightforward recurrence reporting, characterize the 23/24 value—if retained—as a heuristic Bayesian calculation rather than a calibrated forecast, substantially narrow the Gödel claim, strengthen the external literature review, and explicitly characterize the retrospective nature of the XZ study design.

## Editorial verdict

**Current decision: HALT / reject in present form, with encouragement to resubmit after major revision.**

I would **not** recommend publication, archival deposit, or citation of **v0.71 as a frozen preregistration**.

I **would** encourage revision rather than abandonment. The underlying protocol contains serious, interesting work. But its strongest publication claim—namely that the verification process has legitimately reached a terminal FROZEN state despite Bearers 4, 5, and 7 being FALSE—is not supported by either its own rules or the current bytes.

The most consequential observation from this review is almost the inverse of the current conclusion: **the R28 process did what a rigorous audit process is supposed to do. It caught substantive errors that a 186/186 green build did not catch. Those errors should now be corrected, not converted into a theorem of irreducibility.**

---

# Bismillah ir-Rahman ir-Rahim
