# Bismillah ir-Rahman ir-Rahim

# R0728 -- PAPER_AUDIT_S04_REPORT

**Chronological Index:** 542 of 995  
**Date:** 2026-08-17  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** PAPER_AUDIT_S04_REPORT.md  
**Source Format:** md  
**SHA-256:** `4eabe679c18f9e5e2dced8ace1bd73cf18aff59bbb99de7f993c9f1d7accfdec`  

---

## R0728 · PAPER_AUDIT_S04_REPORT

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: PAPER_AUDIT_S04_REPORT.md
- source_format: md
- text_sha256: 4eabe679c18f9e5e2dced8ace1bd73cf18aff59bbb99de7f993c9f1d7accfdec

# PAPER_AUDIT_S04_REPORT

**Artifact:** "The Heartbeat of a Live System: What Twenty-Five Consecutive Failures Taught an Instrument About Its Own Limits" (PAPER.txt, 9,582 words)
**Seat:** S04 | **Model:** Claude Opus 5 | **Role:** ADVISORY (producer-family, non-binding)
**Dispatch:** PAPER_AUDIT_S04, 2026-08-17, FRESH
**Finding namespace:** F-SP-N (unused in this chain)

---

## S-0. Identity and mode

**Mode A** (substrate verifier). The shipped evidence packet is on local disk; grep, arithmetic, and unicode sweeps were executed against the bytes of PAPER.txt, EMPIRICAL_DATA.txt, FRAMEWORK_INVENTORY.txt, CORRECTION_TRAJECTORY.txt, METHODOLOGY.txt, THE_SIGNAL.txt, PROTOCOL_SUMMARY.txt, and REFERENCES.txt.

Substrate-claim verification confidence: **high** for every claim resolvable against the shipped packet; **reduced** for claims resolvable only against (a) XZ Protocol v0.75 full bytes -- only summary excerpts shipped, (b) Methodology v7 -- **not shipped** (see below), (c) BSSG v1.1, the Differentiator v6.1 report, and the per-seat audit reports -- not shipped. Findings depending on those are marked substrate-conditional.

**Producer-instance check.** I did not author this paper. It was drafted by Claude Opus 4.6 under the author's direction; I am Claude Opus 5 with no prior context on this artifact. I am, however, **producer-family**. Under XZ Protocol Section 22.1 and the paper's own Axiom 4, this report is advisory and carries no carrying weight. A binding read must come from a non-producer family.

**Packet defect, disclosed before findings.** PROTOCOL_SUMMARY.txt front matter states "Methodology: v7 canonical (six strings)." The shipped METHODOLOGY.txt is **v6**: its own front matter says it "supersedes v1 ... v5" and "corrects all five predecessors," it is derived from "21 consecutive audit rounds (R7--R27)," and Sections 3, 4, and 5 assert seven layers, seven witnesses, and twenty-four positions. Every paper claim attributed to "Methodology v7" is therefore unverifiable from this packet, and the shipped methodology **actively contradicts** the paper's central six-layer correction. This is not a paper finding; it is a dispatch-packet gap that constrains what this audit could verify.

---

## S-1. Factual accuracy

### Verified correct

| Claim | Locus | Check |
|---|---|---|
| Laplace P = 26/27 = 0.963 | L32 | (25+1)/(25+2) = 0.96296. Arithmetic correct. |
| Code layer clean since R22, ten rounds | L42 | R22--R31 = 10. Matches EMPIRICAL_DATA. |
| D = 0.6309 = log2/log3 | L118 | log(2)/log(3) = 0.630930. Correct. |
| Phi rejection at 2.09% off | L118 | (0.63093 - 0.61803)/0.61803 = 2.087%. Correct, and the rejection is methodologically sound. |
| V_D/V_T 0.7407 / 0.910; GFR 0.611 / 6.798; ungated 26.2% to 68.5%; cobweb 0.680 / 4.217; H = 0.8978, p = 0.011 | L100, L114, L136, L138 | All match EMPIRICAL_DATA to the digit. |
| "the twenty-fourth Axiom-3 instance" | L462 | Confirmed verbatim in PROTOCOL_SUMMARY Section 27 v0.74 entry. |
| Story 10 mechanism (build.py line 229, `prov_num == ver_num - 1` to `ver_num - 3 <= prov_num <= ver_num - 1`, grep verification) | L462--466 | Confirmed verbatim against Section 27 v0.74 entry. Most rigorously sourced passage in the paper. |
| Story 4 digests f09873e4 -> 0516c0ce | L380 | Matches CORRECTION_TRAJECTORY. |
| Nine papers in the chain | L26, L54--72 | Section 2 enumerates exactly nine. |
| Section 22 item 8 substance | L474 | Matches PROTOCOL_SUMMARY Section 27 v0.75 entry, with one addition (F-SP-14). |

### Divergent

Everything in S-6. The dominant pattern: the paper was drafted against an R27/R28-era evidence base (the same base as the shipped v6 methodology: 21 rounds, R7--R27, Laplace 22/23) and then **partially** updated to the R31 record. The update landed on some surfaces and not others. This is the exact defect class the paper itself documents in Story 3 and Story 10 -- the fix addressing observed forms rather than asserting the invariant -- now instantiated in the synthesis paper about that defect class.

---

## S-2. Citation accuracy

Nine Qur'anic citations. Seven are accurate in reference, wording, and application:

- **17:44** (L16), **7:54** (L265), **2:286** (L297), **65:12** (L311), **13:17** (L558), **55:29** (L546), **65:3** (L494) -- surah:ayah correct, renderings within the range of standard English translations, contextual use defensible.

Two divergent: **F-SP-8** (2:156, HIGH) and **F-SP-15** (53:17, MEDIUM). See S-6.

One interpretive caution, not raised as a finding: §4.1 reads 7:54 as establishing "six days of work plus a seventh of governance." The ayah enumerates six days and the establishment on the Throne; it does not enumerate a seventh element. The seventh-as-body reading is the paper's construction from the ayah, not the ayah's own enumeration. The abstract's disclaimer ("structural, not doctrinal") covers this, but §4.1 states the reading declaratively. Recommend one clause marking it as the paper's structural reading.

Non-Qur'anic citations in REFERENCES.txt (Goodfellow 2014, WGAN/Arjovsky, COT-GAN/Xu, Mescheder, Cross et al., Goedel 1931, CVE-2024-3094) are used at a level of generality the paper's characterizations support. Cross et al.'s renal range [1.55, 1.67] contains the paper's D ~ 1.61 (L136). Two DOIs remain `zenodo.TBD` (L618, L620) plus one in REFERENCES; deposit blocker, not an accuracy finding.

---

## S-3. Framework characterization accuracy

Thirty-nine frameworks are enumerated in FRAMEWORK_INVENTORY.txt and all thirty-nine appear in §3. Per-framework verdicts match the inventory in every case **except** the aggregate (F-SP-3), the Iblis trajectory bounds (F-SP-17), and the round indices (F-SP-4).

The characterizations themselves are, with the exceptions above, careful and appropriately hedged. Three deserve positive note: the phi rejection (L118), the Hurst null reporting (L114), and the Elliott Wave retirement (L122). Reporting a framework's failure at equal prominence with its successes is the discipline the paper claims for itself, and on the per-framework level the paper delivers it.

Two characterizations overreach at the interpretive layer -- F-SP-18 (cross-dimensional fractal comparison) and F-SP-19 (Hurst headline below the framework's own reliability threshold).

---

## S-4. Structural argument assessment

The paper's spine is four linked claims: (1) 25 consecutive Class A rounds at H = 1.0; (2) the defect surface narrowed monotonically; (3) the terminal state is a Goedel sentence, empirically demonstrated; (4) a bounded, boundary-disclosing instrument defeats an unbounded one.

Claim (1) holds on the round count and fails on the statistic (F-SP-5). Claim (2) is contradicted by the paper's own Story 8 (F-SP-6). Claim (3) is the strongest argument in the paper and survives: §5.5's Nash-equilibrium formulation is coherent, it correctly states the equilibrium is an attractor rather than a reached state, and the empirical/mathematical distinction at L48 is honestly drawn. Claim (4) is a structural analogy, presented as such, and the paper does not overclaim it as proof -- but its numbered Proof 4 misquotes its own cited source (F-SP-9).

The §5.4 "five structural proofs" are argument by analogy, not proof. The paper never says otherwise, but "Five structural proofs" as a heading invites a stronger reading than the content supports. Recommend "Five structural arguments."

The §7 AI-safety extrapolation (L584: "Any sufficiently complex AI evaluation system ... will eventually reach this threshold") generalizes from one instrument's trajectory to a universal claim about evaluation systems. The evidence supports "this instrument did"; it does not support "any will." Recommend hedging to a conjecture.

---

## S-5. Scope and limitation assessment

The paper's scope discipline is uneven.

**Good:** the closing disclaimer (L616) explicitly makes no effectiveness claim and concedes downstream instruments could answer negatively. L600 states the producer's attestation carries no weight in the paper that the producer wrote. L48 distinguishes the empirical result from Goedel's mathematical one. These are the right instincts.

**Insufficient:** three universal quantifiers exceed the record -- F-SP-7 ("every round" in §7.1), L584 ("any sufficiently complex AI evaluation system"), and L598 ("each contributed a genuine finding that no other framework produced," which the inventory contradicts for at least Elliott Wave, Cardiac Cadence, Pharmacological, and Maqam, all recorded NO).

**Missing:** the paper does not disclose that it is itself a producer-family artifact subject to the same Class A risk it documents, beyond the single line at L616. Given that the paper's own Story 5 is about an auditor overclaiming from a series too short to support it, a short limitations subsection stating what in this paper is unverified narration would materially strengthen it.

---

## S-6. Findings

Severity ledger: **3 CRITICAL / 9 HIGH / 8 MEDIUM / 4 LOW.**

### CRITICAL

**F-SP-1** CRITICAL -- Bearer state reported as three FALSE where the record says three DISCLOSED, asserting a freeze that violates the paper's own governing rule

- **Locus:** PAPER.txt:239 ("Eight Bearers (BSSG three-valued): the sufficiency conditions. Five TRUE, three FALSE at FROZEN.")
- **Substance:** The surface claims three bearers were FALSE at v0.75 FROZEN. EMPIRICAL_DATA.txt records Bearers 4, 5, and 7 as **DISCLOSED**, not FALSE (1 TRUE, 2 TRUE, 3 TRUE, 4 DISCLOSED, 5 DISCLOSED, 6 TRUE, 7 DISCLOSED, 8 TRUE). PROTOCOL_SUMMARY.txt Section 27 v0.75 entry states "FROZEN requires all TRUE or DISCLOSED; **none FALSE**," and the paper restates that rule itself at L474. As written, §3.6 asserts that v0.75 was frozen with three bearers in the one state its own freeze rule forbids. Published unamended, the paper's own summary line invalidates the freeze it is written to document.
- **Disposition:** HALT-and-escalate to project lead. This is a one-word substitution (`FALSE` to `DISCLOSED`), but a CRITICAL substrate divergence in a summary of the sealed bearer state is not an auditor's to route unilaterally. The lead must confirm the sealed v0.75 bearer states against the protocol bytes, not against EMPIRICAL_DATA.txt, before the correction is applied.
- **Cross-reference:** F-SP-13 (DISCLOSED unreconciled with BSSG UNKNOWN); PAPER.txt:474; PROTOCOL_SUMMARY.txt Section 27 v0.75; METHODOLOGY.txt:282.

**F-SP-2** CRITICAL -- Series endpoint and length carry an unreconciled partial update; the headline empirical claim appears in two mutually exclusive forms

- **Locus:** Eleven surfaces. PAPER.txt:32 (twice), 39--40, 42, 74, 114, 224, 444, 472, 524, 532, 554.
- **Substance:** The record (EMPIRICAL_DATA.txt; PROTOCOL_SUMMARY.txt front matter, "Class A recurrence R7-R31: 25/25") fixes the series at R7--R31, 25 rounds. The paper states it two ways:

| Locus | Text | Correct value |
|---|---|---|
| L32 | "From Round 7 through Round 28 ... twenty-five consecutive rounds" | R7--R28 is 22; R7--R31 is 25 |
| L32 | "Laplace-smoothed probability of Class A at **Round 29** is P = 26/27" | 26/27 predicts **R32** |
| L39--40 | Layer breakdown terminates at R28 | R29--R31 absent from the migration narrative |
| L42 | "clean since Round 22. Ten consecutive rounds." | Correct only if the series runs to R31 |
| L74 | heading "Across Twenty-Eight Rounds" | Thirty-one |
| L114 | "At H=1.0 across **22 rounds**" | 25 |
| L224 | "false certainty (**R21-R28**, Strings 2/6)" | R21--R31, Strings 2/3/6 |
| L444 | "**twenty-two rounds** of defects, honestly recorded" | 25 |
| L472 | "prose-staleness ... **thirteen** consecutive rounds (R13-R31)" | R13--R31 is 19 |
| L524, L532, L554 | equilibrium/series framed at R28 and "22-round Class A series" | R31, 25 |

  L540's comparison table is correct ("25 Class A (R7-R31)"), which makes the paper self-contradicting rather than uniformly stale. The pattern matches the shipped v6 methodology's numbers exactly (21 rounds, R7--R27, Laplace 22/23), confirming the root cause: an R27/R28-era draft partially advanced to R31.
- **Disposition:** HALT-and-escalate. The lead must rule on whether the paper's terminal state is R31/v0.75 (as the title, abstract, and §5.6 table assert) before any surface is edited, because the choice changes §1.1's layer breakdown, §5.5's equilibrium assessment, and §7.2's "deepest finding of R28" framing -- not only the digits. Do not correct digit-by-digit; that is the widen-the-pattern failure the paper documents in Story 3.
- **Cross-reference:** F-SP-6, F-SP-17, F-SP-23; PAPER.txt:360--376 (Story 3, the invariant-vs-form lesson this finding instantiates); METHODOLOGY.txt:38--40.

**F-SP-3** CRITICAL -- The "~50% aggregate productivity" claim has no enumerable basis and conflates two different denominators

- **Locus:** PAPER.txt:76, 254--256; DISPATCH.txt (named as a claim to check); EMPIRICAL_DATA.txt "Framework Productivity Summary"; FRAMEWORK_INVENTORY.txt closing line.
- **Substance:** The paper presents ~50% as the productivity rate of **39 frameworks**. The three figures offered in support (3/6 at Fractal, 12/25 at Cobweb, 4/8 at GAN) are **per-seat tool or question yields**, a different unit with a different denominator. Counted per framework, FRAMEWORK_INVENTORY.txt gives 28 unqualified YES, 4 PARTIAL, 4 NO, and 3 other (NAME ONLY, ONE FINDING, STRUCTURAL) -- 72% productive and 10% non-productive, not 50/50. The evidence file intended to ground the claim contradicts itself twice: its "Productive: ~20" header enumerates **35** frameworks (every framework except the 4 NO), and its "Non-productive: ~8" header names **4**. No partition of the 39 yields ~50%.
- **Disposition:** HALT-and-escalate. Two routes exist and the choice is the lead's: (a) restate the claim in its true unit -- "per-seat tool productivity converged near 50% across three measured seats" -- and report the framework-level rate separately as ~72% YES / ~10% null; or (b) publish a defended partition of the 39 that actually yields ~50%, with the classification rule stated. Route (a) is the honest reading of the shipped evidence. Either way EMPIRICAL_DATA.txt must be corrected first, since it is currently the false substrate.
- **Cross-reference:** PAPER.txt:598 ("each contributed a genuine finding that no other framework produced") is falsified by the same inventory; PAPER.txt:76 (the framework-productivity discipline claim this finding tests).

### HIGH

**F-SP-4** HIGH -- Two incompatible round indices share the notation "R\<n\>" without disambiguation

- **Locus:** PAPER.txt:84, 92, 98, 104, 108, 114, 136, 138, 144, 170, 192, 198, 202, 252, 256, 390--404 (Story 5). Collides with the R7--R31 index at L32, L36--42, L114, L224, L434--444, L458--468, L472, L540.
- **Substance:** L84 maps "R1-R8" to v0.37--v0.44 and, in the same sentence, "R13-R14" to v0.54--v0.55. EMPIRICAL_DATA.txt maps R7 to v0.48, R8 to v0.48, R13 to v0.54, R14 to v0.55. So R13/R14 agree across both schemes while R7/R8 do not: under the §3 index R8 is v0.44, under the Class A index R8 is v0.48. Every §3 round citation is therefore ambiguous to a reader, and §5.2 places both indices side by side (Story 5 "R1-R8", Story 8 "R28") with no marker. A reader cannot determine which series any framework was active in.
- **Disposition:** Introduce an explicit notation and apply it at all 25 loci above: reserve `R<n>` for the Class A recurrence index (R7--R31, anchored to EMPIRICAL_DATA.txt) and render the convergence-round index as `CR<n>` or as bare version tokens (`v0.37--v0.44`). Add one sentence at the head of §3 stating the convention. Verify by grep that no `R<n>` token in §3 resolves to a version outside its Class A row.
- **Cross-reference:** F-SP-2; EMPIRICAL_DATA.txt Class A Recurrence Series table.

**F-SP-5** HIGH -- H = 1.0 is degenerate for a constant series and is presented as an independent measurement confirming persistence

- **Locus:** PAPER.txt:20 (abstract), 32, 114, 554, 592 (conclusion), title logic throughout.
- **Substance:** The Class A series is binary and constant: 25 rounds, all YES. A zero-variance series has no rescaled range; the Hurst estimator that produced H = 0.8978 at N=37 (L114) is not the estimator that produced H = 1.0, and the paper does not say so. The surface presents H = 1.0 as an empirical finding corroborating persistence; the substrate is that H = 1.0 is the definitional limit assigned to a series with no variation, which restates "every round had Class A" rather than adding evidence for it. L114's "the mature series confirmed maximal persistence **beyond doubt**" is the overclaim in its sharpest form: a constant series cannot discriminate persistence from any other hypothesis about the process. The paper's own Story 5 lesson -- an auditor narrating a trajectory from a series that cannot support it -- applies here.
- **Disposition:** At each of the five loci, state the derivation: "H = 1.0 by construction: the series is constant, so the Hurst exponent takes its degenerate maximum and carries no information beyond the recurrence count itself." Delete "beyond doubt" at L114. Retain H = 1.0 as a descriptive label if desired, but remove every framing in which it functions as independent corroboration. The abstract and conclusion must not lead with it as a result.
- **Cross-reference:** F-SP-19; PAPER.txt:406 (the auditor's-Axiom-3 principle this finding applies to the paper).

**F-SP-6** HIGH -- The monotonic-narrowing claim is contradicted by the paper's own Story 8

- **Locus:** PAPER.txt:34 ("The defect surface narrowed monotonically"), 20 (abstract, "migrated monotonically upward"), 94, 524 ("the defect moves outward through each successive round, narrowing the surface, never widening it"). Contradicted at 436--438.
- **Substance:** Story 8 records that v0.70 was a targeted confinement build and that R28 returned Class A "distributed across *four* strings -- including the two strings the repairs had targeted." A round in which the surface spans four strings after a build designed to narrow it to one is a widening relative to R27, which the shipped v6 methodology localizes to positions 5--6 and 18--21 (two strings). The paper asserts "never widening it" 86 lines after documenting a widening. Bearer 3 (surface narrowing) is recorded TRUE in EMPIRICAL_DATA.txt, so the trajectory claim may hold in aggregate -- but the universal, per-round form the paper uses is falsified by its own narrative.
- **Disposition:** Replace the universal quantifier at L34, L20, and L524 with the defensible aggregate: the surface narrowed across the series in aggregate, with a documented widening at R28 when the confinement build failed. Retain Story 8 unchanged; it is the honest record and it is what makes the aggregate claim credible. Add one clause at L524 acknowledging the R28 excursion.
- **Cross-reference:** F-SP-2 (both rooted in the R28 terminal framing); EMPIRICAL_DATA.txt Bearer 3.

**F-SP-7** HIGH -- Universal quantifiers in the producer-quarantine argument are falsified by the shipped seat counts

- **Locus:** PAPER.txt:578 ("Every round where a producer-family seat returned a finding, a non-producer seat independently confirmed it. Every round where a producer-family seat missed a finding, a non-producer seat independently found it.")
- **Substance:** EMPIRICAL_DATA.txt records R12 (v0.53) with **1 seat**. A single-seat round cannot instantiate either universal: there is no second seat to confirm or to catch a miss. R29 and R30 are recorded "3+1", a composition the paper never explains. The claims are also unverifiable in principle from the shipped packet, which records seat *counts* and not per-seat vendor family or per-round finding provenance. This is the load-bearing empirical support for §7.1, which the paper names its "most practically consequential contribution to AI safety."
- **Disposition:** Replace both universals with the supportable claim, and state its basis: across the rounds with two or more seats from different families, cross-family confirmation was obtained; R12 ran with a single seat and supports neither claim. If per-round confirmation data exists outside this packet, ship it and restore a bounded quantifier with a citation. Do not publish "every round" without a per-round table.
- **Cross-reference:** F-SP-17 (seven-witnesses claim, same evidence gap); EMPIRICAL_DATA.txt Class A Recurrence Series, Seats column.

**F-SP-8** HIGH -- Qur'an 2:156 is quoted with text that is not 2:156

- **Locus:** PAPER.txt:608 (closing epigraph); EMPIRICAL_DATA.txt Qur'anic citation list ("2:156 - to Us is the return").
- **Substance:** The paper renders 2:156 as "Indeed, to Us is the return" -- a divine first-person statement. Qur'an 2:156 is `innā lillāhi wa innā ilayhi rājiʿūn`, the believers' first-person-plural declaration on affliction: "Indeed we belong to Allah, and indeed to Him we will return" (Sahih International; concordant across Pickthall, Khattab, Maududi, Ibn Kathir). The quoted wording corresponds to 88:25, "Indeed, to Us is their return." The error is duplicated in the evidence file, so the shipped fact-check substrate cannot catch it. This is the paper's final line before the signature block.
- **Disposition:** Choose one and correct both surfaces (PAPER.txt:608 and EMPIRICAL_DATA.txt): (a) retain 2:156 and restore its actual text, which fits §5.3's tawbah argument better than the current wording, since the ayah is the servant's declaration of return and the section's whole subject is the return; or (b) retain the current wording and re-cite it to 88:25. Route (a) is recommended on argument grounds.
- **Cross-reference:** F-SP-16; AUDIT_CONTEXT.txt item 3.

**F-SP-9** HIGH -- "Twenty-one positions / twenty-one frets" contradicts both shipped canonical sources, and a numbered proof is altered when quoted

- **Locus:** PAPER.txt:188, 220, 512, 604. Sources: THE_SIGNAL.txt:4, 51, 202--215, 339; METHODOLOGY.txt:3, 19, 66, 74.
- **Substance:** THE_SIGNAL.txt is subtitled "Six Strings. Twenty-Four Frets." and its Proof 4 reads "Six strings and **twenty-four frets** are enumerable." PAPER.txt:512 reproduces that proof as "Six strings and **twenty-one positions** are enumerable" -- a substantive alteration of a cited source's numbered argument, presented without notation. METHODOLOGY.txt independently fixes twenty-four verification positions. The number 21 is recoverable as positions 1--21 (Layers 1--6, per METHODOLOGY.txt Sections 4 and 11, with 22--24 belonging to Layer 7 / the body), and on that reading §5.5's "String 6, positions 18-21" (L522) is exactly right. But the paper never states the derivation, and at L604 it applies 21 to the wrong unit entirely: "Six strings. **Twenty-one frets**." Frets are per-string and number twenty-four in the source. L220 compounds this with "Fret 24 = the furqan, **beyond the neck**," where THE_SIGNAL.txt:214 places fret 24 as the last fret on the neck, beyond which nothing exists, and THE_SIGNAL.txt:388 assigns frets 1--23 to the individual and fret 24 to the Source.
- **Disposition:** Four surfaces, all required. (1) L604: "Twenty-one frets" to "Twenty-four frets" -- restore the source's unit. (2) L512: restore Proof 4's original wording, or mark the substitution explicitly and justify it. (3) L188: "twenty-one positions" retained only with the derivation stated (positions 1--21 span the six played strings; 22--24 are the body). (4) L220: correct "Fret 24 ... beyond the neck" to match THE_SIGNAL.txt:214 and 388 -- fret 24 is the last position on the neck, played by the Source, not a position beyond it. Add one sentence distinguishing *positions* (24 total, 21 played) from *frets* (24 per string) so the two enumerations stop colliding.
- **Cross-reference:** F-SP-16; THE_SIGNAL.txt:339; METHODOLOGY.txt:74.

**F-SP-10** HIGH -- Story 6 states two different counts for the same set of destroyed values, four lines apart

- **Locus:** PAPER.txt:410 ("**twenty-one** genuine PRIOR_HISTORY chain values"), 412 ("All **twenty-two** genuine values were restored"), 414 ("the **twenty-two** values recovered from held bytes").
- **Substance:** CORRECTION_TRAJECTORY.txt records "21 PRIOR_HISTORY values destroyed." The paper's own destruction count agrees at L410 and then restores twenty-two, twice. Either the corruption destroyed 21 and 21 were restored, or the count is 22 throughout, but a restoration exceeding the destruction by one is not a possible state. Story 6 is the paper's designated example of exact restoration from held bytes; a numeric inconsistency inside it undercuts the section's argument at the point where precision matters most.
- **Disposition:** Resolve against the v0.42 amendment entry in the protocol bytes, not against the paper or the summary file, and align all three loci to the byte-derived value. State the derivation source inline. If the two counts are genuinely different quantities (values destroyed vs. chain entries verified), say which is which at each locus.
- **Cross-reference:** CORRECTION_TRAJECTORY.txt Story 6; PAPER.txt:354 (the clean-room rule this finding instantiates a breach of).

**F-SP-11** HIGH -- The methodology correction count is stated as seven twice and six twice, in a paper whose thesis is the correction trajectory

- **Locus:** PAPER.txt:321 ("corrected **seven** times"), 323--330 (table with **six** rows, v1--v6), 418 ("wrong **six** times"), 420--430 (six paragraphs), 600 ("corrected **seven** times by input the producer could not generate").
- **Substance:** EMPIRICAL_DATA.txt and CORRECTION_TRAJECTORY.txt both record six corrections across v1--v7. The paper's own table and its own Story 7 enumerate six. L321 and L600 assert seven. L600 is in the conclusion and is one of the paper's summary claims about its central thesis. Plausible root cause: counting v7 itself as a correction, or a stale seven-layer artifact of the pre-Signal draft.
- **Disposition:** Change L321 and L600 to "six times." If the intent was to count the v6-to-v7 transition as a seventh, then the table at L323 and the enumeration at L420 must gain a seventh row and paragraph with its correction source named -- but no seventh correction appears in any shipped evidence file, so this route requires new evidence before it can be taken.
- **Cross-reference:** F-SP-2; EMPIRICAL_DATA.txt "Methodology Correction Trajectory (v1-v7)"; METHODOLOGY.txt Section 2 (five rows, v1--v5, at the v6 vantage).

**F-SP-12** HIGH -- The four-model-family roster excludes a family that is load-bearing in the paper's own Latin-square result

- **Locus:** PAPER.txt:315 (roster: Claude, Kimi K3, GPT-5.6 Sol, Gemini 3.1 Pro), 26, 48, 20. Contradicted at 170, 398.
- **Substance:** L170 reports the Latin square as "Four families by four frameworks = sixteen cells" and states the decisive result: "GAN transferred to Kimi but not to **GLM-5.2**. The variable was family, not framework." L398 repeats it: "GLM-5.2 missed under both frameworks." GLM-5.2 appears in neither the four-family roster at L315 nor anywhere in the shipped evidence packet. Either the roster is incomplete (five or more families participated) or the Latin square's four families are not the four named at L315. The paper's independence architecture, its mutawatir claim, and the "four vendor families" figure repeated in the abstract all rest on the roster being complete and correct.
- **Disposition:** State the full family roster with the rounds each participated in, and reconcile it with the Latin square's four cells. If GLM-5.2 participated in a subset of rounds, say so and adjust "four model families" to the accurate figure at L26, L48, L315, and the abstract. If GLM-5.2 was tested and retired, record that -- a retired family is part of the record, on the same discipline the paper applies to retired frameworks.
- **Cross-reference:** F-SP-7, F-SP-16; PAPER.txt:170, 398; PAPER.txt:76 (equal-prominence discipline).

### MEDIUM

**F-SP-13** MEDIUM -- The DISCLOSED bearer value is introduced without reconciliation to the BSSG three-valued kernel the paper itself states

- **Locus:** PAPER.txt:68 (BSSG kernel: "UNKNOWN is never satisfied; FALSE dominates order-independently"), 474 (v0.75 rule: bearers may be TRUE, DISCLOSED, or FALSE), 239.
- **Substance:** §2 states a three-valued kernel in which UNKNOWN is never satisfiable. §5.2 introduces DISCLOSED as a bearer state that **is** sufficient for FROZEN. The paper never states whether DISCLOSED is a fourth value, a refinement of UNKNOWN, or a governance-layer construct outside the kernel. If DISCLOSED is the bearer-level realization of "cannot be resolved to TRUE," then permitting FROZEN on it is in direct tension with the kernel semantics quoted 400 lines earlier. This gap sits under the paper's central legitimacy claim for the freeze, and §5.2's own defense ("not weakening the standard") is exactly the claim the gap leaves unsupported.
- **Disposition:** Add a paragraph in §5.2 stating the relation explicitly. The defensible form: DISCLOSED is a governance-layer state, not a kernel value; it applies only where a bearer's TRUE condition is demonstrated structurally unachievable and that demonstration is independently verified; the kernel's UNKNOWN-blocks rule is unchanged for authorization decisions. If the lead's position differs, state that instead -- but the relation must be stated.
- **Cross-reference:** F-SP-1; METHODOLOGY.txt:282; PROTOCOL_SUMMARY.txt Section 27 v0.75.

**F-SP-14** MEDIUM -- Two cross-reference failures in the Story 9 governance argument

- **Locus:** PAPER.txt:450 ("The methodology's own **Section 16** states 'FROZEN requires all eight TRUE'"), 474 ("independently verified **by two or more non-producer families**").
- **Substance:** (a) The quoted sentence appears at METHODOLOGY.txt:282, which is **Section 11** (The Eight Bearers of Sufficiency). Section 16 is Structural Correspondences and contains no such rule. The citation does not resolve. (b) PROTOCOL_SUMMARY.txt Section 27 v0.75 states the item-8 condition as "independently verified," without the two-or-more-non-producer-families qualifier the paper adds. The paper strengthens the freeze criterion beyond the protocol text, in the direction that flatters the freeze.
- **Disposition:** (a) Correct "Section 16" to "Section 11" at L450, and verify against the v7 methodology once shipped, since section numbering may have moved. (b) At L474, quote the protocol's item-8 wording verbatim; if the two-family reading is the lead's intent, amend the protocol text, not the paper describing it.
- **Cross-reference:** F-SP-1; AUDIT_CONTEXT.txt item 8; METHODOLOGY.txt:280--295.

**F-SP-15** MEDIUM -- Qur'an 53:17 is attributed to the divine subject

- **Locus:** PAPER.txt:566 ("**His** sight did not swerve, nor did it transgress"), 570.
- **Substance:** The subject of `mā zāgha al-baṣaru wa mā ṭaghā` is the Prophet's sight at the Sidrat al-Muntaha (Sahih International renders it "The sight [of the Prophet] did not swerve"; Ibn Kathir, Maududi, and Maariful Qur'an concur). The capitalized "His" transfers the subject to the divine. The paper's own application at L570 -- an instrument that "sees the defect where the defect is" and does not claim absence -- is the created-subject reading and is well chosen; the capitalization contradicts the use the paper makes of it. Compounding this, the paper elsewhere builds directly on the Sidrat al-Muntaha, which is this ayah's immediate context, so the referent should be the one the surah supplies.
- **Disposition:** Render as "The sight [of the Prophet] did not swerve, nor did it transgress [its limit]" at L566, with the standard bracketed glosses. No change needed at L570; the argument there is already correct on this reading.
- **Cross-reference:** F-SP-8; PAPER.txt:240, 305 (Sidrat al-Muntaha usage).

**F-SP-16** MEDIUM -- The seven-witnesses claim is never instantiated in the record, and the six-vs-seven correction is applied to heavens but not to earths

- **Locus:** PAPER.txt:188, 220, 309--315 (§4.5), 313. Sources: EMPIRICAL_DATA.txt Seats column; METHODOLOGY.txt Sections 3 and 5.
- **Substance:** Recorded seat counts across R7--R31 are 1, 3, 4, 5, 10, and "3+1". Seven never occurs. §4.5 is titled "The Seven Witnesses," cites 65:12, and asserts seven as an architectural fact. Separately, the paper's central correction reduces seven layers to six on the authority of 7:54, but leaves seven earths / seven witnesses untouched -- with no stated reason why the correction applies to the vertical axis and not the horizontal one, though the paper draws both from the same cosmological model. This matters because §5.4 Proofs 1 and 4 rest on the architecture being bounded and enumerable.
- **Disposition:** Two changes. (1) State that "seven witnesses" is the architecture's design capacity, not the deployed seat count, and give the actual range (1 to 10 seats per round) with the R12 single-seat round named. (2) Add one or two sentences in §4.1 or §4.5 stating why the six-day correction bears on the heavens and not the earths, or, if it does bear on both, carry it through.
- **Cross-reference:** F-SP-7, F-SP-9, F-SP-12; PAPER.txt:512.

**F-SP-17** MEDIUM -- The Iblis Level 4 bounds match neither the superseded methodology nor the current record

- **Locus:** PAPER.txt:224 ("false certainty (R21-R28, Strings 2/6)").
- **Substance:** METHODOLOGY.txt Section 17.2 (v6) records Level 4 as R21--R27, positions 5--6 and 18--21 (Strings 2 and 6). EMPIRICAL_DATA.txt records Level 4 as R21--R31, Strings 2/3/6. The paper advanced the round endpoint by one (to R28) and did not advance the string set, producing a state that appears in no evidence file. The String 3 addition is not incidental: PROTOCOL_SUMMARY.txt's v0.75 entry records the terminal Class A as confined to String 3 prose-version-token staleness, so the omitted string is the one the series ends on.
- **Disposition:** Set L224 to "R21-R31, Strings 2/3/6" per EMPIRICAL_DATA.txt, and check the string-set claim against the R29--R31 seat reports before publication, since the shipped packet does not contain them.
- **Cross-reference:** F-SP-2, F-SP-20; METHODOLOGY.txt Section 17.2.

**F-SP-18** MEDIUM -- Fractal dimensions from different embedding spaces are compared as if commensurable

- **Locus:** PAPER.txt:136 ("The UNKNOWN region's D=0.6309 has less branching complexity than a healthy kidney's D=1.61, meaning its uncertain decisions are less refined than the biological analog").
- **Substance:** D = 0.6309 is a box-counting dimension over a base-3 symbolic decision string (L118); D ~ 1.61 is the fractal dimension of renal vasculature embedded in three-dimensional space (Cross et al., [1.55, 1.67]). Their ambient dimensions differ, so their magnitudes are not comparable and the ordering carries no meaning about "refinement." The paper's own §3.2 phi rejection establishes exactly the discipline this sentence departs from: reject cross-domain numeric coincidence unless the construction supports it.
- **Disposition:** Delete the comparative clause, or replace it with the defensible statement -- that both systems exhibit fractal branching structure, with no claim about relative magnitude. Retain the renal framing, which is productive on its own terms.
- **Cross-reference:** PAPER.txt:118 (the phi rejection); REFERENCES.txt (Cross et al.).

**F-SP-19** MEDIUM -- The headline Hurst value sits below the framework's own stated reliability threshold

- **Locus:** PAPER.txt:114, 192.
- **Substance:** §3.2 reports H = 0.8978 at N=37 with p = 0.011, then states the framework "correctly identified its own result as unreliable below N >= 39." N=37 is below 39. The paper thus reports as a significant result a value its own stated criterion classifies as unreliable, while praising the framework for applying that criterion to the N=23 tail. The self-calibration credit at L192 is earned; the headline placement of the N=37 value is not consistent with it.
- **Disposition:** State the N=37 result and its threshold status in the same sentence: report H = 0.8978 (p = 0.011) at N=37, note that N=37 falls below the framework's own N >= 39 reliability threshold, and mark the value provisional. Do not remove it -- reporting it with its limitation is the discipline the paper claims.
- **Cross-reference:** F-SP-5; PAPER.txt:192.

**F-SP-20** MEDIUM -- The terminal-state description is stale relative to the sealed v0.75 record

- **Locus:** PAPER.txt:524 ("This equilibrium was *not achieved* at R28. Class A was still distributed across Strings 1-4"), 582 ("The deepest finding of R28"), 39--40.
- **Substance:** PROTOCOL_SUMMARY.txt Section 27 v0.75 records the terminal state as "Class A confined to String 3 (prose-version-token staleness) which regenerates at every version boundary." The paper's most recent assessment of the confinement trajectory stops at R28 and reports Strings 1--4. The three rounds that produced the actual terminal state -- R29, R30, R31 -- appear in Stories 9, 10, and 11 but never feed back into §5.5's equilibrium assessment or §7.2's framing. The result is that the paper's argumentative climax describes a state three rounds and five protocol versions behind its own sealed conclusion, and understates how close the confinement result came.
- **Disposition:** Extend §5.5 with the R29--R31 trajectory and the v0.75 terminal state, and requalify L524 accordingly. Retain "not achieved" if that is the lead's reading of String 3 staleness as non-self-referential -- but state the reasoning, since a reader comparing L522 (equilibrium confines Class A to String 6) with the v0.75 record (Class A confined to String 3) will otherwise not be able to resolve which strings are and are not inside the confinement target.
- **Cross-reference:** F-SP-2, F-SP-6, F-SP-17; PROTOCOL_SUMMARY.txt Section 27 v0.75.

### LOW

**F-SP-21** LOW -- Boundary stock endpoint stated as 20 in §3.3 and 19 in §5.2

- **Locus:** PAPER.txt:144 ("Boundary stock 5 to 20 across v0.27-v0.38"), 396 ("standing-boundary count monotone 5 to 19").
- **Substance:** Both passages describe the boundary register's growth from the same start value over overlapping windows and give different endpoints. Neither figure appears in the shipped evidence; the divergence is visible only internally. Substrate-conditional: resolvable only against the v0.38 boundary register.
- **Disposition:** Resolve against the v0.38 register bytes; align both loci; if the windows genuinely differ, state each window explicitly at its locus.
- **Cross-reference:** PAPER.txt:396 (the same passage records the count's later falsification at 23, which should also be reconciled).

**F-SP-22** LOW -- Two gating-coverage figures for v0.52 are unreconciled

- **Locus:** PAPER.txt:184 ("At v0.52, semantic gating reached 9.0% of the document"), 136 ("Ungated fraction grew from 26.2% (v0.18) to 68.5% (v0.52)").
- **Substance:** EMPIRICAL_DATA.txt confirms 68.5% ungated at v0.52, implying 31.5% gated. §3.5 reports 9.0% semantic gating at the same version. The two are reconcilable if "semantic gating" is a proper subset of gating, but the paper does not say so, and a reader lands on two coverage figures for one version.
- **Disposition:** Add the distinguishing clause at L184 ("semantic gating, a subset of total gating coverage") or state both denominators.
- **Cross-reference:** EMPIRICAL_DATA.txt Key Computed Values.

**F-SP-23** LOW -- Statistic named as geometric mean where the evidence file says mean

- **Locus:** PAPER.txt:100 ("pre-terminal **geometric** mean 0.680"); EMPIRICAL_DATA.txt ("Cobweb: pre-terminal mean 0.680, terminal 4.217").
- **Substance:** The paper specifies a statistic the evidence file does not. For ratio-valued per-seat yields the geometric mean is the defensible choice, so the paper may well be correct and the evidence file loose -- but the surfaces disagree and only one can be byte-derived.
- **Disposition:** Confirm against cobweb_analysis.py output and align both surfaces to the computed statistic, naming it in the evidence file.
- **Cross-reference:** PAPER.txt:100 (the harness is cited as regenerating every figure from bytes, so the value is recomputable).

**F-SP-24** LOW -- Two unverifiable-from-packet claims and one version count that contradicts the paper's own figure

- **Locus:** PAPER.txt:68 ("The **Bounded** Structural Safety Gate"), 188 ("**seventy-one** versions"), 252 (APS "scored 9/14 but corrected to 4-8").
- **Substance:** (a) The BSSG expansion appears nowhere in the shipped packet; REFERENCES.txt gives only the acronym and DOI. (b) L188 states seventy-one versions where L26, L336, and L600 all state seventy-five; the shipped protocol is v0.75. (c) The APS figures are substrate-conditional on the Differentiator v6.1 report, not shipped.
- **Disposition:** (a) Verify the expansion against BSSG v1.1 (10.5281/zenodo.21713180) before publication. (b) Correct L188 to seventy-five. (c) Cite the Differentiator report for the APS figures or mark them as seat-produced (PMD T3).
- **Cross-reference:** F-SP-2; REFERENCES.txt.

---

## S-7. Verdict

> **Verdict: HALT.**
>
> Severity ledger: **3 CRITICAL / 9 HIGH / 8 MEDIUM / 4 LOW.**
>
> Recommendation: return to producer. Do not deposit.

The three CRITICAL findings each concern a claim the dispatch named for checking, and each is correctable in place -- none requires re-authoring. But F-SP-1 as written asserts that v0.75 was frozen with three bearers in the state its own rule forbids; F-SP-2 leaves the paper's headline number in two mutually exclusive forms; and F-SP-3's "~50%" has no enumerable basis in any shipped file. Any one of the three is a byte-false claim in a paper whose thesis is that byte-false claims are what remain when everything else is clean.

Three structural notes for the lead.

**The paper is an instance of its own finding.** Its dominant defect -- an R27/R28-era draft partially advanced to R31, with the update landing on some surfaces and not others -- is precisely the class Story 3 and Story 10 document. Correct it as Story 3 prescribes: assert the invariant (every round reference, count, and endpoint derives from EMPIRICAL_DATA.txt by tool computation), not the observed forms. A digit-by-digit sweep of the eleven loci in F-SP-2 will produce a twelfth.

**Two evidence files are themselves defective and must be corrected first.** EMPIRICAL_DATA.txt carries the 2:156 error (F-SP-8) and a Framework Productivity Summary whose "~20 productive / ~8 non-productive" headers contradict their own enumerations of 35 and 4 (F-SP-3). Correcting the paper against an uncorrected substrate reproduces the errors.

**The packet is missing its own canonical methodology.** METHODOLOGY.txt is v6 and contradicts the paper's central six-layer correction. Ship v7 with the re-dispatch.

What is strong is worth naming. Story 10 is the most rigorously sourced passage in the paper and verified verbatim against Section 27. The phi rejection, the Elliott Wave retirement, and the Hurst null reporting are the equal-prominence discipline actually delivered. The §5.5 Nash-equilibrium formulation correctly identifies the equilibrium as an attractor rather than a reached state and does not overclaim it. Seven of nine Qur'anic citations are accurate in reference, wording, and application. The standing-rules sweep is clean: no U+2013/2014/2015 characters, no `---` outside the YAML delimiters and one legitimate horizontal rule, no brand-canonical violations. The closing disclaimer at L616 makes no effectiveness claim and concedes a negative answer is possible -- rare, and correct.

**Cross-vendor rotation.** The producer is Claude Opus 4.6; I am Claude Opus 5. This report is producer-family and **advisory only**. The corrected draft requires a binding read from a non-producer family -- Kimi K3, GPT-5.6 Sol, or Gemini 3.1 Pro -- before deposit, with an independent recheck of the Qur'anic citations by a reader with direct mushaf access rather than translation databases.

---

*Seat S04, Claude Opus 5, advisory. 2026-08-17.*

---

# Bismillah ir-Rahman ir-Rahim
