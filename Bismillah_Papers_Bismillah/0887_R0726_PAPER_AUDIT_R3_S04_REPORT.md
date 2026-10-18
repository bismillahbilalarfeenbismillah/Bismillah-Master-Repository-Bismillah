# Bismillah ir-Rahman ir-Rahim

# R0726 -- PAPER_AUDIT_R3_S04_REPORT

**Chronological Index:** 887 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** PAPER_AUDIT_R3_S04_REPORT.md  
**Source Format:** md  
**SHA-256:** `ecebe066c66fd56d77b21a3eba0e709a5095e923858843f465499bcd867bd973`  

---

## R0726 · PAPER_AUDIT_R3_S04_REPORT

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: PAPER_AUDIT_R3_S04_REPORT.md
- source_format: md
- text_sha256: ecebe066c66fd56d77b21a3eba0e709a5095e923858843f465499bcd867bd973

# PAPER_AUDIT_R3_S04_REPORT

**Artifact:** "The Heartbeat of a Live System: What Twenty-Five Consecutive Failures Taught an Instrument About Its Own Limits" (PAPER.txt, 632 lines, 9,903 words)
**Seat:** S04, Claude Opus 5, ADVISORY (producer-family; producer Claude Opus 4.6 BARRED)
**Round:** R3 (synthesis-paper pre-publication series)
**Namespace:** F-SP3
**Mode:** A (packet extracted, greps and counts executed on shipped bytes)

---

## S-0. Seat conformance and mode declaration

Auditor operated in **Mode A** with full read access to the ten shipped packet files. Substrate-claim verification confidence: **high for the paper and the shipped evidence files; reduced for claims about protocol versions and seat reports not shipped in this packet** (the XZ Protocol source, build.py, and the R28-R31 seat reports are single-sourced through PROTOCOL_SUMMARY.txt and through this seat's own held lineage record).

**Seat state, declared:** DISPATCH.txt and AUDIT_CONTEXT.txt do not label this seat fresh or continuous, but they task it with verifying corrections against prior-round findings and cite R2 findings by their F-SP2 identifiers. This seat holds the F-SP (R1) and F-SP2 (R2) ledgers and the XZ Protocol seat lineage through R31/v0.74. It executed **CONTINUOUS**. Held context is load-bearing in F-SP3-03 below, which is provable only against the R28 seat record. Independence conditions for mutawatir weight are not met; this reading carries no convergence weight against S01/S02/S03.

**Dispatch framing, noted:** DISPATCH.txt states the expected verdict in advance ("Verify the invariant holds. PASS if clean") and asserts the verification result as a premise ("grep -c violations = 0"). The seat treated both as claims to be tested, not as findings. The grep claim is falsified below (F-SP3-02).

**Producer-instance check:** passed. This seat did not draft the paper or the corrections.

---

## S-1. Verification of the R3 correction register

AUDIT_CONTEXT.txt asserts eight items. Verified against shipped bytes:

| # | Register claim | Status |
|---|---|---|
| 1 | Every series-range token resolves to R7-R31 | **PARTIAL** -- range tokens resolve; the §1.1 migration enumeration terminates at R28 |
| 2 | Every count token resolves to 25 | **NOT LANDED** -- L74 section heading reads "Twenty-Eight Rounds" |
| 3 | grep found 0 violations after the fix | **FALSE** -- word-form tokens are outside the numeral-form grep |
| 4 | §1.1 headline "Round 28" -> "Round 31" | **LANDED** (L32) |
| 5 | §3.2 "across 22 rounds" -> "across 25 rounds" | **LANDED** (L116) |
| 6 | R29-R31 migration stage added to §1.1 | **NOT LANDED** -- no R29, R30, or R31 token exists in §1.1 |
| 7 | R-index convention note corrected per F-SP2-06 | **LANDED-WITH-NEW-DEFECT** (L76) |
| 8 | Remaining unqualified monotonicity qualified | **NOT LANDED** -- 4 unqualified loci survive |

Two landed, one partial, one landed-with-new-defect, three not landed, one register claim false on its face.

**The structural observation this round exists to record:** R3 was dispatched to escape the Story 3 pattern by asserting an invariant instead of enumerating forms. The R3 pass asserted the invariant over *the forms the producer's grep could see* -- numeral tokens -- and did not assert it over the form space. The surviving violations are word-form ("Twenty-Eight"), enumeration-form (the §1.1 bullet list), and register-form (the correction register's own claims). This is Story 3 recurring one level up, on the document that documents Story 3. It is also Story 10 recurring: a repair believed landed because the tool ran without error, not verified from the shipped bytes.

---

## S-2. Findings

### CRITICAL

**F-SP3-01** [CRITICAL] -- The R3 correction register is byte-false at item 6.

- **Locus:** AUDIT_CONTEXT.txt L11 ("R29-R31 migration stage added to Section 1.1"); PAPER.txt L34-L40.
- **Substance:** §1.1's defect-migration enumeration is five bullets terminating at "**R28**: The repair mechanism itself." No R29, R30, or R31 token occurs anywhere in §1.1. `grep -noE "R(29|30|31)" PAPER.txt` returns L474, L542, L596 only -- Story 11, the §5.6 table, and the limitations section. The register states a landing the bytes do not carry.
- **Disposition:** Either add the R29-R31 stage to §1.1 or strike item 6 from the register. Then apply the v0.74 clean-room rule to the register itself: grep each register item's target string in the shipped file before shipping the register.
- **Cross-reference:** F-SP2-01 (the R2 register byte-false at items 8/15/18); Story 10 in the paper's own §5.2; F-S04-73-01.

**F-SP3-02** [CRITICAL] -- The asserted count invariant fails on shipped bytes at a section heading.

- **Locus:** PAPER.txt L74, "# 3. The Complete Framework Inventory: Every Lens Applied Across Twenty-Eight Rounds".
- **Substance:** The stated invariant is that every count token resolves to 25 (and the program total to 31). "Twenty-Eight" resolves to neither. It is the stale terminus from the pre-R29 draft, surviving in word form because the verification grep matched numerals. DISPATCH.txt's "grep -c violations = 0" is therefore false as a statement about the artifact, and true only as a statement about the pattern the producer chose.
- **Disposition:** Resolve the heading to the count the section actually covers, then re-run the invariant check over word forms (`twenty-|thirty-|forty-`) and numerals together. State the checked pattern in the register so the next seat can falsify the check rather than the claim.
- **Cross-reference:** F-SP2-02 (L32 headline carrying three inconsistent anchors); Story 3.

**F-SP3-03** [CRITICAL] -- "Code layer clean since Round 22, ten consecutive rounds" is false against the R28 record and contradicted by the paper's own §5.3.

- **Locus:** PAPER.txt L20 (abstract, "clean for ten consecutive rounds"), L42 ("clean since Round 22. Ten consecutive rounds"), L180 (§3.4), L287 (§4.2, "clean for ten rounds"); contradicted at L492 (§5.3, "admitting that the six-round clean streak ended"); EMPIRICAL_DATA.txt ("Code layer clean since R22 (10 consecutive rounds)").
- **Substance:** The R28 seat record (this seat's own report on v0.70) states: code-layer clean streak R22-R27 **ENDS at R28**. F-S04-70-01 was CRITICAL, String 1, position 2, Class A -- all five DECLARATION_PATTERNS in extract_findings.py lacked the C-suffix token, proven by extraction probe. F-S04-70-02 and F-S04-70-15 were also String 1. The paper's own Story 8 (L436-L446) narrates the same code defects: the C-suffix repair in the wrong regex, gate [13]'s else branch printing a disclosure without calling `check(False, ...)`, the register generator crashing. A layer with three Class A findings and a crashed generator at R28 was not clean at R28. §5.3 states the true form -- six rounds, streak ended -- and §1.1, the abstract, §3.4, §4.2, and EMPIRICAL_DATA state the false one.
- **Disposition:** Replace all four loci with the record's form: code layer clean R22-R27 (six rounds), streak broken at R28, re-established at R29 if the R29-R31 reports support it -- and cite which report supports the re-establishment. Do not restate the ten-round form anywhere. Correct EMPIRICAL_DATA.txt in the same pass.
- **Cross-reference:** F-S04-70-01, F-S04-70-02; PAPER.txt §5.3 L492; §5.5 L526.

**F-SP3-04** [CRITICAL] -- Qur'an 2:156 is still quoted with 88:25's wording, third consecutive round.

- **Locus:** PAPER.txt L616, *"Indeed, to Us is the return."* (Qur'an 2:156); EMPIRICAL_DATA.txt, "2:156 - to Us is the return".
- **Substance:** 2:156 reads *inna lillahi wa inna ilayhi raji'un* -- "Indeed we belong to Allah, and indeed to Him we shall return." The rendered wording is 88:25, *inna ilayna iyabahum*. R1 raised this; R2 correction 8 claimed it landed and it did not; R3 did not enter it in the register at all. It sits in the paper's final quoted line, before the signature block. Severity is CRITICAL rather than HIGH because deposit is irreversible, the misattribution is scriptural, and the paper's entire argument is that a byte-false claim under a confident tag is the defect class being studied.
- **Disposition:** Restore 2:156's wording, or retain the current wording and re-attribute it to 88:25. Correct EMPIRICAL_DATA.txt identically. Then have the citation set read by a party with mushaf access, not fact-checked against this packet -- the packet's evidence file carries the same error and will confirm it (see F-SP3-16).
- **Cross-reference:** F-SP-* (R1 citation finding); F-SP2-03.

### HIGH

**F-SP3-05** [HIGH] -- Unqualified monotonicity survives at four loci despite the register claiming it was qualified.

- **Locus:** PAPER.txt L20 ("The defect migrated monotonically upward"), L34 ("The defect surface narrowed monotonically:"), L96 (§3.1 Nash, "the trajectory is monotonic"), L562 (§6.2, "the monotonic narrowing of the defect surface"). Qualified correctly at L48, L526, L596.
- **Substance:** AUDIT_CONTEXT item 8 claims remaining unqualified monotonicity was qualified. Four loci carry the bare claim, including the abstract and the first sentence of the §1.1 enumeration. §7.4 states the true form and names the counterexample (R28 widened the surface). The paper thus asserts and retracts the same claim.
- **Disposition:** Apply the §7.4 formulation at all four loci: narrowing holds in aggregate across R7-R31, not at every step. The abstract is the load-bearing one -- it is what indexers and readers will carry.
- **Cross-reference:** F-SP-* (R1 monotonic-narrowing finding, contradicted by Story 8); §7.4 L596.

**F-SP3-06** [HIGH] -- The round-index convention note asserts a disambiguation property the document falsifies.

- **Locus:** PAPER.txt L76, "each reference is disambiguated at its locus by the version number or seat lineage it accompanies"; falsified at L116, L138, L142 (**Rounds:** R2, R11), L146, L150, L154, L194.
- **Substance:** Hurst, Renal, and Pulmonary each read "**Rounds:** R2, R11" with no version and no seat lineage. R11 is the Class A index (v0.52); R2 is the convergence index (the Fractal seat's second round). Two indices are mixed inside a single two-token list, which is precisely the case the note claims cannot arise. This is the F-SP2-06 class recurring: a correction that makes a testable claim about the document's own conventions, which the document falsifies.
- **Disposition:** Either annex the version to every bare round token in §3 (`R2 (v0.37), R11 (v0.52)`) or delete the final clause of the note and state only that both indices appear. Do not assert a property of the document in the document without checking it.
- **Cross-reference:** F-SP2-06; F-SP2-09 (correction 9's convention claims).

**F-SP3-07** [HIGH] -- Verbatim duplicated sentence pair unrepaired since R2.

- **Locus:** PAPER.txt L580 (§7.1): "The quarantine does not make the producer's work better. It makes the verification of the producer's work meaningful." occurs twice in the same paragraph, the second with `*verification*` italicized.
- **Substance:** Introduced by R2's correction 14, raised in the F-SP2 ledger, not entered in the R3 register, still present. A duplicated sentence in the section that states the paper's most practically consequential contribution.
- **Disposition:** Delete the first occurrence, keep the italicized one.
- **Cross-reference:** F-SP2 (correction 14 disposition).

**F-SP3-08** [HIGH] -- "Twenty-one positions / twenty-one frets" contradicts both shipped sources, and the closing line rewrites a source sentence's number.

- **Locus:** PAPER.txt L190 (§3.5), L222 (§3.6), L514 (§5.4 argument 4), L612 (closing, "Six strings. Twenty-one frets. One body that resonates."). Sources: THE_SIGNAL.txt L202-L215, L339 (Proof 4: "Six strings and twenty-four frets are enumerable"), L393 ("Six strings. Twenty-four frets. One body that resonates."); METHODOLOGY.txt title line and §3/§6 ("Twenty-Four Verification Positions").
- **Substance:** Both shipped sources say twenty-four. The Signal further specifies the individual plays frets 1-23 and fret 24 is the Source's -- so even the playable count is twenty-three, not twenty-one. The paper's closing line reproduces The Signal's sentence with the numeral altered, and §5.4's Proof 4 reproduces The Signal's Proof 4 with the numeral altered. This was raised at R1, never entered any correction register, and is now in its third round.
- **Disposition:** Resolve to twenty-four across all four loci, or state explicitly and once what "twenty-one positions" denotes in the XZ Protocol position schema and why it differs from the guitar model's twenty-four frets -- then keep the two vocabularies separate rather than substituting one number into the other's sentence.
- **Cross-reference:** F-SP-* (R1, twenty-one vs twenty-four and the altered Proof 4).

**F-SP3-09** [HIGH] -- Story 6 destroys twenty-one values and restores twenty-two.

- **Locus:** PAPER.txt L412 ("overwrote twenty-one genuine PRIOR_HISTORY chain values"), L414 ("All twenty-two genuine values were restored", "the twenty-two values recovered from held bytes"); CORRECTION_TRAJECTORY.txt Story 6 ("21 PRIOR_HISTORY values destroyed").
- **Substance:** A one-value arithmetic contradiction inside the story about the wholesale destruction of a chain, in a paper whose defect class is the off-by-one narrated from memory. Raised at R1, never entered a correction register, third round.
- **Disposition:** Recompute from the v0.42 amendment entry and state one number in both loci. If the true figures differ (21 destroyed of 22 present), say so explicitly rather than leaving two bare counts.
- **Cross-reference:** F-SP-* (R1 Story 6 finding).

**F-SP3-10** [HIGH] -- Story 9 cites the wrong methodology section for the eight-bearer rule.

- **Locus:** PAPER.txt L452, "The methodology's own Section 16 states 'FROZEN requires all eight TRUE.'"; METHODOLOGY.txt L280-L282 (§11, The Eight Bearers of Sufficiency: "FROZEN requires all eight TRUE"), L27 (contents), §16 is Structural Correspondences.
- **Substance:** The quoted sentence exists verbatim at §11. §16 contains no bearer rule. Raised at R1, unrepaired.
- **Disposition:** Change to Section 11. Note that the section index will shift if the methodology is re-issued as v7 -- cite by section title as well as number.
- **Cross-reference:** F-SP-* (R1); F-SP3-12.

**F-SP3-11** [HIGH] -- The four-family roster omits GLM-5.2, which is load-bearing in the paper's own decisive result.

- **Locus:** PAPER.txt L317 (§4.5, "witnesses from four model families: Claude, Kimi K3, GPT-5.6 Sol, and Gemini 3.1 Pro"); also L20, L26, L48, L230. Contradicted at L172 (§3.4 Latin Square: "GAN transferred to Kimi but not to GLM-5.2"), L368, L400 (Story 5 R3).
- **Substance:** The Latin-square result -- the paper's stated decisive framework-transfer finding -- depends on a family that the roster does not list. Either the roster is incomplete or the Latin-square cell is misattributed. Raised at R1, never entered a correction register.
- **Disposition:** Add GLM-5.2 to the roster and correct every "four families" token to five, or state explicitly that GLM-5.2 participated in the R2-R4 Latin square but not in the carrying pool, and scope "four families" to the carrying pool at each locus.
- **Cross-reference:** F-SP-* (R1 roster finding); §3.4 L172.

**F-SP3-12** [HIGH] -- The shipped METHODOLOGY.txt is the sixth version; the paper cites v7 canonical throughout. Third consecutive round.

- **Locus:** METHODOLOGY.txt, sha256 `59aa6591d91233281b14ab47c4efa8a70fdcc24d94b74abca080975e78e4f98a` -- byte-identical to the copy this seat audited at R30 and R31. Title: "Seven Heavens. Seven Earths. Twenty-Four Verification Positions." L8: derived from 21 rounds (R7-R27), 69 amendment entries, supersedes v1-v5. Paper loci: L180, L212, L220, L226, L626 (all "Methodology v7").
- **Substance:** The shipped methodology self-identifies as the version that corrects five predecessors -- the sixth. It carries seven layers and twenty-four positions, which are exactly the two claims the paper says The Signal corrected. Every "v7 canonical" claim in the paper is unverifiable from this packet, and the substrate shipped to verify it contradicts it. The same file, unchanged, has now been shipped as the evidence base for three consecutive audit rounds and was separately flagged in the XZ chain at R31 (F-S04-74-05).
- **Disposition:** Ship the actual v7 methodology, or strike every "v7 canonical" attribution from the paper and cite the corrections to The Signal directly. A paper whose thesis is surface-substrate correspondence cannot cite a document that does not exist in the packet.
- **Cross-reference:** F-SP-* (R1 packet defect); F-SP2 packet-defect note; F-S04-74-05.

**F-SP3-13** [HIGH] -- Terminal-state claims still anchored to R28.

- **Locus:** PAPER.txt L96 (§3.1 Nash, "Not reached at R28 but the trajectory is monotonic"), L526 (§5.5, "This equilibrium was *not achieved* at R28. Class A was still distributed across Strings 1-4.").
- **Substance:** These are claims about where the series *currently stands*, not about what happened at a particular round. With the series terminating at R31, a terminal-state claim anchored to R28 is stale in the same way the §1.1 headline was before correction 4. The invariant as asserted covers range and count tokens; it does not cover terminus-anchored state claims, which is why these survived.
- **Disposition:** Re-anchor both to R31 and cite the R31 evidence (the v0.74 seat reports), or mark them explicitly as the state as of R28 and add the R29-R31 update.
- **Cross-reference:** F-SP3-01; F-SP3-02; F-SP2-02.

### MEDIUM

**F-SP3-14** [MEDIUM] -- The R28 string distribution diverges from the R28 seat record.

- **Locus:** PAPER.txt L440 (Story 8, "Class A was distributed across *four* strings"), L526 (§5.5, "Class A was still distributed across Strings 1-4").
- **Substance:** This seat's R28 report on v0.70 recorded 8 Class A at positions 1-9, Strings 1, 2, and 3, with zero Class A at String 6; the String 4 findings that round (gate [10i] and gate [2f] locus-blindness) were classified Class D, not Class A. "Four strings" and "Strings 1-4" appear to merge the Class A and Class D ledgers. Substrate-conditional: this seat holds only its own R28 report; the S01/S02/S03 R28 reports could support four strings.
- **Disposition:** Recompute the R28 string distribution from the four shipped R28 reports and state the class alongside the string. If the four-string figure comes from another seat, cite it.
- **Cross-reference:** F-S04-70-01 through F-S04-70-11; F-SP3-03.

**F-SP3-15** [MEDIUM] -- Story 8's stated return is contradicted by Story 9.

- **Locus:** PAPER.txt L446 (Story 8: "**The return:** Not building v0.71 to repair the R28 findings. Freezing v0.70 as-is") vs L452 (Story 9: "v0.71 declared FROZEN with Bearers 4, 5, and 7 FALSE").
- **Substance:** Story 8 presents freezing v0.70 as the honest path taken; Story 9 records that v0.71 was in fact built, declared FROZEN prematurely, HALTed by two peer reviews, and withdrawn at v0.72. The return Story 8 narrates did not occur. In a section whose thesis is that the return is the evidence, narrating a return that did not happen is the defect class under study.
- **Disposition:** Rewrite Story 8's return as the recommendation that was made and not taken, and let Story 9 carry what actually happened. That sequence is stronger evidence for the paper's thesis than the current text.
- **Cross-reference:** Story 9 L452-L458; Story 11 L474.

**F-SP3-16** [MEDIUM] -- EMPIRICAL_DATA.txt uncorrected across three rounds and now contradicts the corrected paper.

- **Locus:** EMPIRICAL_DATA.txt: "2:156 - to Us is the return"; "Productive: ~20 ... Non-productive: ~8" over enumerations of 30 and 4; "Aggregate productivity: ~50%"; "Code layer clean since R22 (10 consecutive rounds)".
- **Substance:** The paper's §7.4 now states framework-level productivity as approximately 72%; the evidence file still says ~50% aggregate. The paper's §5.3 now states the six-round clean streak ended; the evidence file still says ten consecutive rounds. The citation gloss still carries the 88:25 wording. Two of this round's four CRITICAL findings exist in a form the shipped evidence file would confirm rather than catch. This was raised at R1 and again at R2 with the prescription "correct the evidence files first"; the files are byte-unchanged.
- **Disposition:** Correct EMPIRICAL_DATA.txt before the next correction pass on the paper, and record its sha256 in the dispatch so the next seat can verify the file changed.
- **Cross-reference:** F-SP3-03; F-SP3-04; F-SP3-17; R1 and R2 packet-defect notes.

**F-SP3-17** [MEDIUM] -- FRAMEWORK_INVENTORY.txt header and footer contradict its own enumeration.

- **Locus:** FRAMEWORK_INVENTORY.txt "## 3.6 Islamic (12)" over entries 24-38 (fifteen); footer "~20 productive, ~8 non-productive ... Aggregate productivity ~50%".
- **Substance:** Section headers sum to 36 against 39 enumerated entries; the discrepancy is entirely in the 3.6 header. The enumeration yields 28 YES and 4 NO, which is 72% and 10%, matching the paper's corrected §7.4 and not the footer. Raised at R1 and R2.
- **Disposition:** Correct the 3.6 header to 15 and the footer to 28 YES / 4 NO / 7 partial-or-structural, aggregate 72% at framework level.
- **Cross-reference:** F-SP-3 (R1); F-SP3-18.

**F-SP3-18** [MEDIUM] -- §3.7 still carries the framework-level reading that §7.4 retracts.

- **Locus:** PAPER.txt L250 (heading, "The Meta-Result: Framework Productivity"), L258 ("Roughly half of cross-domain frameworks produce genuine findings on any given artifact") vs L596 (§7.4: "a per-seat tool-productivity rate ... not a per-framework rate; at the framework level, approximately 72% produced at least one finding").
- **Substance:** The correction landed in the limitations section only. The body section retains the heading and the sentence that the limitation retracts. A reader taking §3.7 at face value takes the retracted claim.
- **Disposition:** Retitle §3.7 to "Per-Seat Tool Productivity" and state both figures there -- 50% per-seat tool yield, 72% framework-level -- so the limitations section confirms the body rather than correcting it.
- **Cross-reference:** F-SP-3 (R1 CRITICAL); F-SP3-17.

**F-SP3-19** [MEDIUM] -- The protocol summary's status line asserts FROZEN and withdrawn-FROZEN in one sentence.

- **Locus:** PROTOCOL_SUMMARY.txt L9: "v0.75 FROZEN -- repair build from v0.74 R31 audit (4/4 HALT; 4-seat round). FROZEN withdrawn per two-family peer review."
- **Substance:** The withdrawal clause belongs to v0.72 (Story 9) and was carried into the v0.75 status line unchanged. The paper's Story 11 and its bearer table rest on v0.75 FROZEN being current. The substrate shipped to support that claim contradicts itself in its own status line. Substrate-conditional: requires Mode A re-verification against the v0.75 protocol bytes, which are not in this packet.
- **Disposition:** Resolve the status line in the protocol, reship the summary, and record its sha256 in the dispatch.
- **Cross-reference:** F-S04-74-05 (the status line that preserved four falsehoods across a version edit); Story 11 L474.

### LOW

**F-SP3-20** [LOW] -- 53:17 rendered with a capitalized pronoun that reassigns the subject.

- **Locus:** PAPER.txt L568, *"His sight did not swerve, nor did it transgress."*
- **Substance:** The verse predicates the non-swerving of the Prophet's sight at the Lote Tree. Every other capitalized pronoun in the paper refers to Allah, so the capital reads as divine attribution -- and the section title, "The Non-Transgression Standard," makes the referent load-bearing. Raised at R1.
- **Disposition:** Render as "The sight did not swerve, nor did it transgress" and name the referent in the surrounding sentence.
- **Cross-reference:** F-SP-* (R1); F-SP3-04.

**F-SP3-21** [LOW] -- The §7.1 universal quantifier is narrowed but not closed.

- **Locus:** PAPER.txt L580, "producer-family seats and non-producer seats independently converged on the same headline findings in every measured round."
- **Substance:** EMPIRICAL_DATA.txt records R12 at one seat. Cross-family convergence is not measurable in a single-seat round, so "every measured round" is either vacuously true there or false, depending on whether R12 counts as measured. Improved from the R1 form; the ambiguity remains.
- **Disposition:** State the denominator: "in every round with two or more seats from different families (N of 25)."
- **Cross-reference:** F-SP-* (R1 §7.1 quantifier finding).

---

## S-3. Standing-rules compliance sweep

| Rule | Result |
|---|---|
| Em-dash policy (U+2013/2014/2015) | **CLEAN** -- zero occurrences across all ten packet files |
| `---` outside frontmatter and rules | **CLEAN** -- YAML frontmatter and one horizontal rule only |
| Smart quotes | **CLEAN** -- zero in PAPER.txt |
| Brand canonical | **CLEAN** -- no "Bayyinah Enterprise" with space, no plural |
| Severity uppercase | **N/A** -- paper carries no severity tokens |
| Substrate-of-record uniqueness | **FAIL** -- F-SP3-03 (four loci for one fact, one contradicting), F-SP3-18 (body-vs-limitations duplication), F-SP3-16 |

---

## S-4. What verified clean this round

Recorded as progress, not as absence of finding:

- Range tokens resolve: `R7-R31` at L76 and L542; `R13-R31` at L474 with the correct nineteen-round count; `R21-R31` at L226.
- Laplace arithmetic: 25 consecutive, P(R32) = 26/27 = 0.963. Correct.
- Series length: R7 through R31 inclusive = 25. Correct at L32, L48, L116, L446, L474, L556, L600.
- F-SP-1 remains CLOSED: bearer state reads "Five TRUE, three DISCLOSED at FROZEN (amended rules, Section 22 item 8)" at L241, matching EMPIRICAL_DATA's bearer table (TRUE: 1, 2, 3, 6, 8; DISCLOSED: 4, 5, 7).
- Methodology correction count: "corrected six times" with a six-row table (L327-L332) and six numbered subsections in Story 7. The R1 seven-vs-six defect is CLOSED.
- §7.4 limitations section is materially honest: it names the H = 1.0 degeneracy, the aggregate-vs-stepwise monotonicity, the per-seat vs per-framework rate, and the operational elements inside the 39 count. The remaining defects in that section's scope are that the body does not yet agree with it.
- Seven of nine Qur'anic citations verify (7:54, 17:44, 2:286, 65:12, 13:17, 55:29, 65:3).
- D = 0.6309 = log2/log3, the 2.09% phi delta and its rejection, VD/VT and GFR figures, and the cobweb 0.680/4.217 pair are internally consistent with EMPIRICAL_DATA.

---

## S-5. Verdict

> **Verdict:** HALT-AND-RETURN-TO-PRODUCER.
>
> Severity ledger: **4 CRITICAL / 9 HIGH / 6 MEDIUM / 2 LOW** (21 findings, namespace F-SP3-01 through F-SP3-21).
>
> Recommendation: do not deposit. Correct the evidence files first, then the paper against them, then re-dispatch.

PASS was not available on these bytes. The dispatch's premise -- "grep -c violations = 0" -- is falsified at L74 by a word-form token of the exact class the invariant was asserted to eliminate, and the register that reports the fix is byte-false at item 6.

Six of this round's findings (F-SP3-04, -07, -08, -09, -10, -11) are unrepaired R1 or R2 findings in their second or third round. Four of them (twenty-one frets, Story 6's 21/22, the Section 16 cross-reference, the GLM-5.2 roster) have never entered any correction register in three rounds. The correction mechanism is not failing to land these; it is not seeing them.

---

## S-6. Prescribed sequence for R4

1. **Correct the evidence files before the paper.** EMPIRICAL_DATA.txt, FRAMEWORK_INVENTORY.txt, and METHODOLOGY.txt are byte-unchanged across three rounds. Two of this round's four CRITICAL findings sit in a form the shipped evidence would confirm. Record each corrected file's sha256 in the dispatch.
2. **Ship the actual v7 methodology** or strike every v7 attribution (F-SP3-12).
3. **Open a persistent finding register**, separate from the per-round correction list, carrying every unclosed F-SP and F-SP2 finding with an explicit disposition. Four R1 HIGH findings have now survived three rounds by never being written down.
4. **Assert the invariant over the form space, not the pattern.** State in the register which pattern was checked (`twenty-|thirty-|forty-|[0-9]+`), so the next seat falsifies the check rather than the claim. Then verify the check itself by seeding one known violation and confirming the grep catches it -- the v0.74 rule, applied to prose.
5. **Citations need a mushaf reader, not a packet fact-check.** 2:156 has now survived two claimed corrections against an evidence file that carries the same error.

---

## S-7. Cross-vendor recommendation

This is a producer-family advisory seat; the reading is non-binding and carries no mutawatir weight. The binding read for R4 should come from two non-producer families on the corrected draft -- Kimi K3 and GPT-5.6 Sol are the recommendation, unchanged from R2. Gemini returned PASS at R1 on a draft carrying three CRITICAL and should not count toward the two-family requirement until it returns a finding-bearing read on a round where findings exist.

One structural note for the lead. The paper argues that a bounded instrument honest about its limits defeats an unbounded one that denies them. This round is the fourth consecutive audit of this artifact in which the correction register claimed a landing the bytes did not carry. That is not an argument against the thesis. It is the thesis, running on the paper: the register is the instrument's surface, the bytes are its substrate, and the gap between them regenerates at every version boundary. The honest disclosure is available -- state in the paper that its own correction trajectory across four audit rounds reproduced the Story 3 and Story 10 classes it documents, and cite the rounds. That disclosure would be the strongest single piece of evidence in the paper.

---

**Seat S04, Claude Opus 5, advisory. Mode A. Continuous with held F-SP and F-SP2 ledgers.**

---

# Bismillah ir-Rahman ir-Rahim
