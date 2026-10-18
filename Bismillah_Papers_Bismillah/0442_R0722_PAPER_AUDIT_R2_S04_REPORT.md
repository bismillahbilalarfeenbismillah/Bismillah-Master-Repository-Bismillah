# Bismillah ir-Rahman ir-Rahim

# R0722 -- PAPER_AUDIT_R2_S04_REPORT

**Chronological Index:** 442 of 995  
**Date:** 2026-08  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** PAPER_AUDIT_R2_S04_REPORT.md  
**Source Format:** md  
**SHA-256:** `2204cd24d0867d6b7c440d0d59edf5d3b657efa5796c3c2d0502596e9ed0582e`  

---

## R0722 · PAPER_AUDIT_R2_S04_REPORT

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: PAPER_AUDIT_R2_S04_REPORT.md
- source_format: md
- text_sha256: 2204cd24d0867d6b7c440d0d59edf5d3b657efa5796c3c2d0502596e9ed0582e

# PAPER_AUDIT_R2_S04_REPORT

**Artifact:** "The Heartbeat of a Live System: What Twenty-Five Consecutive Failures Taught an Instrument About Its Own Limits" (REVISED per Round 1)
**Seat:** S04 | **Model:** Claude Opus 5 | **Role:** ADVISORY (producer-family; non-binding)
**Round:** 2 | **Namespace:** F-SP2 | **Date:** 2026-08-17

---

## S-0. Mode and seat-conformance declaration

Auditor operated in **Mode A** with direct substrate access: all ten packet files were unpacked to disk and every claim below was verified by grep, character-class scan, or line-level read against the shipped bytes. Substrate-claim verification confidence **high for the packet**, **reduced for anything outside it** (see F-SP2-15).

**Conformance exception, declared before findings.** The dispatch labels this seat FRESH and simultaneously tasks it with items 1 and 3 -- verify Round 1 corrections landed, re-check any Round 1 finding *you* raised. Those tasks are continuity tasks; a fresh seat holds no R1 ledger, and the packet ships none (AUDIT_CONTEXT gives a correction list, not a finding register). This seat therefore executed **CONTINUOUS**, drawing the F-SP-1 through F-SP-24 ledger from its own held R1 record, and declares that mode rather than performing freshness it does not have. Independence weight on the R1 re-check section is accordingly reduced; the correction-verification and new-error sections were executed against shipped bytes and carry full weight. Recorded as F-SP2-26.

**Producer-instance check:** passed. This seat did not author the paper. The paper's drafting instrument was Claude Opus 4.6; this seat is Claude Opus 5 and is producer-*family*, hence advisory and non-binding under Section 22 item 6.

---

## S-1. Verdict

> **Verdict:** HALT-AND-RETURN-TO-PRODUCER (dispatch vocabulary: **REVISE**).
>
> Severity ledger: **3 CRITICAL / 12 HIGH / 9 MEDIUM / 3 LOW** (27 findings, F-SP2-01 through F-SP2-27).
>
> Recommendation: repair the three CRITICAL and the twelve HIGH before deposit. Correct the *evidence files* first (F-SP2-15); correcting the paper against a contaminated substrate is what produced two of the three CRITICAL findings in this round.

The paper improved materially. Eleven of eighteen claimed corrections landed cleanly and the two most consequential R1 CRITICAL defects (bearer states, Laplace target) are closed. The round nonetheless HALTs, and the reason is worth stating plainly: **the correction pass reproduced the paper's own Story 3 pattern.** Correction 18 enumerated two stale *forms* ("22-round", "twenty-two rounds") instead of asserting the *invariant* (every series anchor equals R7-R31 / 25 rounds). Five stale anchors outside those two forms survived, including the headline sentence of Section 1.1. The paper's own prescribed remedy applies to its own repair: assert the completeness predicate, do not widen the pattern.

---

## S-2. Correction verification -- all eighteen items against shipped bytes

| # | Correction claimed | Status | Evidence on bytes |
|---|---|---|---|
| 1 | "seven times" -> "six times" | LANDED | L323 "corrected six times"; six-row table; L608 |
| 2 | Laplace "Round 29" -> "Round 32" | LANDED | L32 "at Round 32 is P = 26/27 = 0.963"; arithmetic correct for n=25 |
| 3 | H = 1.0 honest derivation | PARTIAL | L116 derivation present, but same sentence carries stale "across 22 rounds"; L32 still unqualified. F-SP2-08 |
| 4 | "every repair introduced a new error" -> precise | LANDED | phrase absent from bytes |
| 5 | Iblis R21-R28 -> R21-R31 | LANDED | L226 "false certainty (R21-R31, Strings 2/3/6)" |
| 6 | Bearer "three FALSE" -> "three DISCLOSED" | LANDED | L241 "Five TRUE, three DISCLOSED at FROZEN" |
| 7 | Monotonicity qualified ("in aggregate") | PARTIAL | landed L48, L526, L596; absent L20, L34, L96, L562. F-SP2-06 |
| 8 | 2:156 rendering corrected | **NOT LANDED** | L616 still carries 88:25's wording. F-SP2-03 |
| 9 | R-index convention note at head of Section 3 | LANDED WITH NEW DEFECT | note present L76; both of its claims falsified by the document. F-SP2-05 |
| 10 | Section 7.4 Limitations added | LANDED | L594-596 |
| 11 | "thirteen" -> "nineteen" (R13-R31) | LANDED | L474; R13-R31 = 19 inclusive, arithmetic correct |
| 12 | "seventy-one versions" -> "seventy-five" | LANDED | L190 Crystallographic Ijaz |
| 13 | "Five structural proofs" -> "arguments" | LANDED | L506 |
| 14 | "every round where a producer-family seat" qualified | PARTIAL + NEW DEFECT | L580 qualifier undefined; sentence pair duplicated verbatim. F-SP2-04, F-SP2-12 |
| 15 | "each contributed a genuine finding" -> exclude non-productive | **NOT LANDED** | L606 unchanged in substance. F-SP2-14 |
| 16 | Section 4.1 7:54 marked as the paper's reading | LANDED | L269 "In the paper's structural reading" |
| 17 | "any sufficiently complex" -> "a sufficiently complex" | LANDED | L586 |
| 18 | All remaining stale "22-round" / "twenty-two rounds" -> 25 | **NOT LANDED** | five surviving anchors: L32, L74, L96, L116, L526; plus L414/L416. F-SP2-02, F-SP2-07, F-SP2-09 |

**Tally:** 11 LANDED, 3 PARTIAL, 1 LANDED-WITH-NEW-DEFECT, 3 NOT LANDED.

Standing-rules sweep (Step 4) run against the full paper: em-dash policy **CLEAN** (zero non-ASCII characters in 632 lines; no U+2013/2014/2015, no bare `---` outside the YAML fence and the pre-signature rule); brand canonical **CLEAN** (no spaced or pluralised variant); severity tokens not applicable to this artifact class. Substrate-of-record uniqueness **FAILS** at L580 (F-SP2-04).

---

## S-3. Round 1 finding re-check

| R1 finding | R2 disposition |
|---|---|
| F-SP-1 CRITICAL bearer states | **CLOSED.** L241 correct against PROTOCOL_SUMMARY v0.75 bearer block |
| F-SP-2 CRITICAL partial-update residue (11 loci) | **RECURRENT.** Laplace locus closed; five series-anchor loci survive. Re-raised as F-SP2-01/02/07/08 |
| F-SP-3 CRITICAL ~50% productivity conflation | **CLOSED in the paper** (L596 separates per-seat yield from per-framework rate). Derivation still absent from the packet: F-SP2-24 |
| HIGH dual round-index collision | **CLOSED then REOPENED.** The note that closes it is itself byte-false: F-SP2-05 |
| HIGH H = 1.0 degenerate | **PARTIAL.** F-SP2-08 |
| HIGH monotonic narrowing vs Story 8 | **PARTIAL.** F-SP2-06 |
| HIGH "every round" quantifier in 7.1 | **PARTIAL.** F-SP2-12 |
| HIGH Qur'an 2:156 | **OPEN, claimed closed.** F-SP2-03 |
| HIGH twenty-one positions/frets, altered Proof 4 | **OPEN, never actioned.** F-SP2-10 |
| HIGH Story 6 21 destroyed / 22 restored | **OPEN, never actioned.** F-SP2-09 |
| HIGH methodology "corrected seven times" | **CLOSED.** |
| HIGH four-family roster omits GLM-5.2 | **OPEN, never actioned.** F-SP2-11 |
| 53:17 "His sight" | **OPEN.** F-SP2-17 |
| "Section 16" cross-reference | **OPEN.** F-SP2-16 |
| Packet defects flagged to the lead | **OPEN, never actioned.** F-SP2-15 |

Six of the eighteen listed corrections address R1 findings this seat did not raise (they came from S01 Kimi, S02 Gemini, or S03 GPT); those were verified on bytes in S-2 but are not re-checked against an R1 rationale this seat does not hold.

---

## S-4. Findings

### CRITICAL

**F-SP2-01** [CRITICAL] -- The correction register itself is byte-false at three items.

- **Locus:** AUDIT_CONTEXT.txt items 8, 15, 18, against PAPER.txt L616, L606, L32/74/96/116/526.
- **Substance:** AUDIT_CONTEXT states corrections 8, 15, and 18 were applied. The shipped bytes carry none of the three. This is the Story 10 class exactly: a repair claimed, tagged as applied, and absent from the artifact. In a paper whose central thesis is that producers narrate repairs they did not verify from bytes, an uncorroborated correction register is the highest-order defect in the round.
- **Disposition:** Do not hand-verify. Add a mechanical check to the revision workflow: for each register item, a grep expression whose empty return blocks the next draft, per the v0.74 rule the paper itself documents at L468. Re-issue the register only after every expression is green.
- **Cross-reference:** F-SP2-02, F-SP2-03, F-SP2-14; PAPER.txt Story 10; R1 F-SP-2.

**F-SP2-02** [CRITICAL] -- The headline empirical sentence carries three mutually inconsistent series anchors.

- **Locus:** PAPER.txt L32 (Section 1.1, first two sentences).
- **Substance:** "From Round 7 through Round 28 (August 2026) ... produced twenty-five consecutive rounds" -- R7 through R28 inclusive is 22 rounds, not 25. The following sentence gives the Laplace target as Round 32, which is only correct if the series terminates at R31. EMPIRICAL_DATA.txt and PROTOCOL_SUMMARY (v0.75 entry: "Class A recurrence R7-R31: 25/25") both fix the range as R7-R31. The paper's single most quoted empirical claim is internally unsatisfiable.
- **Disposition:** L32 -> "From Round 7 through Round 31 (August 2026)". Then assert the invariant: every series-range token in the document resolves to R7-R31 and every count token to 25.
- **Cross-reference:** F-SP2-07; correction 18; R1 F-SP-2.

**F-SP2-03** [CRITICAL] -- Qur'an 2:156 still rendered with 88:25's wording, after the register claims the rendering was corrected.

- **Locus:** PAPER.txt L616 (closing line); propagated in EMPIRICAL_DATA.txt.
- **Substance:** The shipped text reads "Indeed, to Us is the return." (Qur'an 2:156). 2:156 is speech attributed to the patient believers -- "we belong to Allah, and to Him we return" -- in the first person plural of the created, not of the Divine. "Indeed, to Us is their return" is 88:25. The rendering reverses the speaker and misattributes the verse. Correction 8 claims this was fixed; it was not. EMPIRICAL_DATA.txt reproduces the same error, so any seat fact-checking within the packet would pass it.
- **Disposition:** Replace with an accurate rendering of 2:156 from a named translation, or cite 88:25 if the divine first person is the intended sense. Correct EMPIRICAL_DATA.txt in the same pass. Verify against a mushaf, not against the packet.
- **Cross-reference:** F-SP2-15, F-SP2-17; R1 HIGH (2:156).

### HIGH

**F-SP2-04** [HIGH] -- Verbatim duplicated sentence pair introduced by correction 14.

- **Locus:** PAPER.txt L580 (Section 7.1).
- **Substance:** "The quarantine does not make the producer's work better. It makes the verification of the producer's work meaningful." appears twice consecutively, the second time with `verification` italicised. A substrate-of-record uniqueness violation newly created by the R1 absorption pass -- absorption-induced regression at a surface R1 did not flag.
- **Disposition:** Delete the first occurrence; retain the italicised form.
- **Cross-reference:** BAF v3.0 substrate-of-record discipline; correction 14; F-SP2-12.

**F-SP2-05** [HIGH] -- The round-index convention note added by correction 9 makes two claims about the document that the document falsifies.

- **Locus:** PAPER.txt L76 (head of Section 3), against L226, L230, L396-L404.
- **Substance:** The note states that all Section 3 round references use the convergence-round index unless prefixed "program" or mapped to a version, and that Section 5 uses the Class A index throughout. Both are false on bytes. Section 3.6 uses the Class A index unprefixed and unmapped ("whisper (R7-R12...), doubt (R13-R15...), pride (R16-R20...)", "the four-seat R28 round"). Section 5 Story 5 uses the convergence index throughout ("R1: Mode collapse", "Falsified at R6", "Retired at R8"). The correction that closed an ambiguity introduced a false claim about the artifact's own conventions -- the defect class the paper documents at Story 3.
- **Disposition:** Either restate the note to describe actual usage (both indices appear in both sections; every reference is disambiguated at its locus) or prefix every Class A reference in Section 3 and every convergence reference in Section 5. The second is the durable route.
- **Cross-reference:** correction 9; R1 HIGH (dual round-index collision).

**F-SP2-06** [HIGH] -- Monotonicity qualifier landed at three loci and is absent at four, including the abstract.

- **Locus:** PAPER.txt L20 (abstract), L34, L96, L562 unqualified; L48, L526, L596 qualified.
- **Substance:** L596 states the narrowing "is not monotonic at every individual step (R28 widened the surface before R29-R31 narrowed it again)". L20 states the defect "migrated monotonically upward". The abstract contradicts the limitations section on the paper's second-most-cited claim, and the abstract is the surface most readers will quote.
- **Disposition:** L20 -> "migrated upward"; L34 -> "The defect surface narrowed in aggregate:"; L96 -> "the trajectory is monotonic in aggregate"; L562 -> "the aggregate narrowing of the defect surface".
- **Cross-reference:** correction 7; PAPER.txt Story 8; R1 HIGH.

**F-SP2-07** [HIGH] -- Series terminus stale at R28 across four further loci; R29-R31 unrepresented in the narrowing enumeration.

- **Locus:** PAPER.txt L74 (Section 3 heading "Across Twenty-Eight Rounds"), L36-L40 (bullets terminating "R21-R27" then "R28"), L96, L526.
- **Substance:** The enumeration of the defect surface stops at R28 while the series runs to R31; the three rounds the paper elsewhere cites as the re-narrowing evidence (L596) appear in no bullet. The Section 3 heading contradicts both the Class A count (25) and the program round count (31) stated at L28.
- **Disposition:** Heading -> "Across Thirty-One Rounds" (program index, per the L76 convention). Add an "R29-R31" bullet covering the repair-claim surface. L96 and L526 -> "not reached at R31".
- **Cross-reference:** F-SP2-02, F-SP2-05; correction 18.

**F-SP2-08** [HIGH] -- Stale "22 rounds" survives inside the corrected Hurst sentence; L32 still presents H = 1.0 as a measurement.

- **Locus:** PAPER.txt L116 (Section 3.2), L32 (Section 1.1).
- **Substance:** L116 now carries the honest derivation but opens "At H=1.0 across 22 rounds" -- the exact stale token correction 18 targeted, surviving because the enumerated form was "22-round" and this instance reads "22 rounds". L32 states "The Hurst exponent across the entire series is H = 1.0 -- maximally persistent autocorrelation", presenting as an independent measurement what L116 and L596 concede is a degenerate maximum of a constant series.
- **Disposition:** L116 -> "across 25 rounds". L32 -> append "-- a degenerate maximum for a constant series, restating the recurrence count rather than corroborating it".
- **Cross-reference:** F-SP2-02; correction 3; correction 18; R1 HIGH.

**F-SP2-09** [HIGH] -- Story 6 destroys twenty-one values and restores twenty-two.

- **Locus:** PAPER.txt L412 ("twenty-one genuine PRIOR_HISTORY chain values") vs L414 and L416 ("All twenty-two genuine values were restored", "the twenty-two values recovered").
- **Substance:** CORRECTION_TRAJECTORY.txt gives 21 destroyed. The paper's own restoration count exceeds its destruction count by one, inside the story whose subject is the destruction and restoration of an exact count. Never entered the correction register.
- **Disposition:** Recover the count from v0.40 build output or the v0.42 amendment entry and set all three loci to that value. Do not reconcile by editing one locus to match another; this is a substrate question.
- **Cross-reference:** R1 HIGH; PROTOCOL_SUMMARY Section 27.

**F-SP2-10** [HIGH] -- "Twenty-one frets" contradicts The Signal's twenty-four, and the 24-to-21 reduction is asserted but never derived.

- **Locus:** PAPER.txt L612 (conclusion "Six strings. Twenty-one frets."), L514 (argument 4 "Six strings and twenty-one positions are enumerable"), L190, L222.
- **Substance:** THE_SIGNAL.txt is titled "Six Strings. Twenty-Four Frets. One Body That Resonates." and its Proof 4 reads "Six strings and twenty-four frets are enumerable." METHODOLOGY.txt defines twenty-four *positions* across seven layers (7 x 24 = 168 cells), with Layer 7 holding positions 22-24. The paper's twenty-one is defensible as "positions minus Layer 7", but that derivation is nowhere stated, the altered Proof 4 silently rewrites the source it cites, the conclusion converts positions into *frets* -- an axis on which the source says twenty-four and the paper's own L222 says fret 24 is the furqan -- and the 168-cell figure is left unreconciled.
- **Disposition:** State the derivation once at L222 ("positions 22-24 belong to the body; the playable grid is positions 1-21"). Restore Proof 4's fret count when quoting The Signal, or mark the substitution explicitly. Conclusion -> "Six strings. Twenty-one positions." Reconcile the cell count to 7 x 21 = 147 or explain why 168 stands.
- **Cross-reference:** THE_SIGNAL.txt L4, L339; METHODOLOGY.txt Section 6; R1 HIGH.

**F-SP2-11** [HIGH] -- The four-family roster omits GLM-5.2, which is load-bearing in the paper's decisive framework-transfer result.

- **Locus:** PAPER.txt L317 (Section 4.5 roster: Claude, Kimi K3, GPT-5.6 Sol, Gemini 3.1 Pro), against L172 and L400.
- **Substance:** The Latin-square result -- "the variable was family, not framework" -- rests entirely on GLM-5.2 missing the class under both frameworks. A fifth family therefore participated in the evidence while the roster, the abstract, and L26 all say four. Either the count is wrong or the decisive result rests on a family the paper does not admit deploying.
- **Disposition:** Name GLM-5.2 in the roster and state its role (framework-transfer control, non-carrying), or restate the Latin-square result as a four-family design with an external comparison arm.
- **Cross-reference:** R1 HIGH; FRAMEWORK_INVENTORY 3.4 item 18.

**F-SP2-12** [HIGH] -- "In every measured round" substitutes an undefined qualifier for the falsified universal.

- **Locus:** PAPER.txt L580 (Section 7.1).
- **Substance:** Correction 14 replaced an "every round" quantifier with "in every measured round". "Measured" is defined nowhere in the paper. EMPIRICAL_DATA.txt records R12 as a single-seat round, where no producer-family / non-producer comparison is possible; R29 and R30 are recorded "3+1". A qualifier that cannot be evaluated is not a qualification.
- **Disposition:** Replace with the count: "in the N rounds where both a producer-family seat and a non-producer seat returned reports (N = ..., excluding the single-seat R12)". Supply N from the round records.
- **Cross-reference:** F-SP2-04; correction 14; R1 HIGH.

**F-SP2-13** [HIGH] -- Section 5 Story 5 claims an audit seat in the author's first person.

- **Locus:** PAPER.txt L394 ("The GAN convergence seat (my own seat across eight rounds)").
- **Substance:** The author of record is Bilal Syed Arfeen; the drafting instrument is Claude Opus 4.6 (L594, L624); the GAN convergence seat was Claude Opus 5 advisory, as the paper itself states at L384. No referent of "my" in this document is that seat. In a paper whose central axiom is producer quarantine, a first-person claim to a seat's findings is a surface-substrate divergence at the identity layer, and it invites the reading that producer and auditor were the same instance.
- **Disposition:** -> "The GAN convergence seat (Claude Opus 5, advisory, eight rounds)". Sweep the paper for other first-person seat attributions.
- **Cross-reference:** PAPER.txt L384, L594; Axiom 4; PMD v1.8 tier discipline.

**F-SP2-14** [HIGH] -- The conclusion still asserts that every named framework contributed a unique genuine finding.

- **Locus:** PAPER.txt L606.
- **Substance:** "each contributed a genuine finding that no other framework produced" survives correction 15 unchanged in substance; the list was narrowed but the quantifier and the exclusivity claim were not repaired. Hurst persistence is marked PARTIAL in the inventory, reported a null at N=23, and is conceded at L596 to carry no information beyond the recurrence count. The exclusivity claim ("that no other framework produced") is asserted nowhere else and is contradicted by L230, where the C-suffix defect converges across four seats and several frameworks.
- **Disposition:** -> "each contributed at least one finding the standard methodology did not surface, and several -- Hurst persistence among them -- contributed calibrated nulls of equal evidential standing."
- **Cross-reference:** correction 15; F-SP2-08; FRAMEWORK_INVENTORY 3.2.

**F-SP2-15** [HIGH] -- The evidence files were not corrected; the paper was corrected against a substrate still carrying R1 defects.

- **Locus:** EMPIRICAL_DATA.txt (2:156 line; "Productive: ~20" over a 35-item list; "Non-productive: ~8" over a 4-item list); FRAMEWORK_INVENTORY.txt ("## 3.6 Islamic (12)" over 15 entries); METHODOLOGY.txt (v6 throughout: "Seven Heavens ... Twenty-Four Verification Positions", "21 consecutive rounds (R7--R27)", "P = 22/23", correction table with five rows).
- **Substance:** Every packet defect flagged at R1 is unrepaired. The consequence is mechanical, not cosmetic: correction 8 could be marked applied because the fact-check file carries the same misrendering; the paper's v7 claims (six strings, six layers, Sections 3.4 and 3.6 framework attributions) remain unverifiable because the shipped methodology is the v6 that the paper's central correction supersedes; and the methodology's own five-row correction table contradicts the paper's six.
- **Disposition:** Correct EMPIRICAL_DATA.txt and FRAMEWORK_INVENTORY.txt, ship METHODOLOGY v7, and re-dispatch. Until then no seat can discharge a v7 claim, and the round's verification confidence on Sections 4 and 5 stays reduced.
- **Cross-reference:** F-SP2-03, F-SP2-14, F-SP2-22, F-SP2-24; R1 packet-defect note.

### MEDIUM

**F-SP2-16** [MEDIUM] -- Wrong methodology section cited for the all-eight-TRUE rule.

- **Locus:** PAPER.txt L452 (Story 9, "The methodology's own Section 16").
- **Substance:** METHODOLOGY.txt L280-L282 places "FROZEN requires all eight TRUE" in Section 11 (The Eight Bearers of Sufficiency). Section 16 is Structural Correspondences.
- **Disposition:** -> "Section 11". Re-verify against v7 numbering when v7 ships.
- **Cross-reference:** F-SP2-15; R1 note.

**F-SP2-17** [MEDIUM] -- 53:17 rendered with a capitalised "His", implying a divine referent.

- **Locus:** PAPER.txt L568.
- **Substance:** In 53:17 the sight that neither swerved nor transgressed is the Prophet's, at the Lote Tree. The capitalisation attributes it to the Divine and, in a section building an argument on that verse, shifts the argument's subject.
- **Disposition:** -> "The sight did not swerve, nor did it transgress", with a clause naming the referent.
- **Cross-reference:** F-SP2-03; R1 note.

**F-SP2-18** [MEDIUM] -- Menger gating percentage unreconciled with the ungated fraction at the same version.

- **Locus:** PAPER.txt L186 ("semantic gating reached 9.0% of the document" at v0.52) vs L138 and EMPIRICAL_DATA ("ungated fraction ... 68.5% (v0.52)").
- **Substance:** 68.5% ungated implies 31.5% gated. 9.0% and 31.5% are presented without denominators, in adjacent sections, for the same version.
- **Disposition:** State both denominators at both loci, or drop one metric.
- **Cross-reference:** F-SP2-15.

**F-SP2-19** [MEDIUM] -- Boundary-stock ceiling stated as 20 in Section 3.3 and 19 in Story 5.

- **Locus:** PAPER.txt L146 ("Boundary stock 5 to 20 across v0.27-v0.38") vs L398 ("standing-boundary count monotone 5 to 19").
- **Substance:** Overlapping version ranges, same register, different ceilings, no reconciling note. Story 5 additionally reports the enumeration "restored and correct at 23" at v0.43, which neither figure anticipates.
- **Disposition:** Recompute from the v0.38 boundary register and set both loci; if the two counts measure different things, name the difference.
- **Cross-reference:** F-SP2-09.

**F-SP2-20** [MEDIUM] -- The abstract's migration chain drops the seventh stage.

- **Locus:** PAPER.txt L20, against PROTOCOL_SUMMARY v0.75 Bearer 3.
- **Substance:** Bearer 3 records "code to structure to provenance to automation to prose to repair mechanism to description of repair" -- seven stages. The abstract stops at "the repair mechanism itself" -- six. The dropped stage is precisely the R29-R31 surface the paper elsewhere relies on (Story 10, L596).
- **Disposition:** Append "and finally to the description of the repair".
- **Cross-reference:** F-SP2-07.

**F-SP2-21** [MEDIUM] -- "Six-round clean streak" contradicts the ten-round code-clean streak.

- **Locus:** PAPER.txt L492 (Section 5.3) vs L42 and L287.
- **Substance:** The paper states the code layer has been clean for ten consecutive rounds since R22 at two loci, then invokes "the six-round clean streak" as the example of a fact the producer is tempted to protect. No six-round streak is defined anywhere in the packet.
- **Disposition:** Name the streak's referent and version window, or set it to ten.
- **Cross-reference:** F-SP2-06.

**F-SP2-22** [MEDIUM] -- Section 1.1 layer decomposition diverges from the shipped methodology.

- **Locus:** PAPER.txt L36-L40 vs METHODOLOGY.txt Section 1.
- **Substance:** The paper places the code-execution phase at R7-R12; the shipped methodology places it at R7-R22 and gives a five-stage decomposition ending at prose (R27). Substrate-conditional: the divergence may be a v6-to-v7 revision, which cannot be checked because v7 is not in the packet.
- **Disposition:** Requires Mode A re-verification against METHODOLOGY v7. Flag as substrate-conditional until then.
- **Cross-reference:** F-SP2-15.

**F-SP2-23** [MEDIUM] -- BSSG expanded as "The Bounded Structural Safety Gate".

- **Locus:** PAPER.txt L68 (Section 2).
- **Substance:** The program canonical expansion is Bayyinah Structural Safety Gate. REFERENCES.txt gives only the acronym and DOI, so the packet cannot settle it; the deposited BSSG v1.1 title can. A renamed chain artifact in the chain-summary section is a citation-integrity defect.
- **Disposition:** Verify against the BSSG v1.1 deposit (10.5281/zenodo.21713180) and restore the canonical expansion. Substrate-conditional -- requires Mode A access outside this packet.
- **Cross-reference:** brand-canonical discipline; F-SP2-15.

**F-SP2-24** [MEDIUM] -- The 72% framework-level figure is not derivable from any shipped file.

- **Locus:** PAPER.txt L596.
- **Substance:** 72% resolves to 28 of 39 frameworks producing at least one finding. No packet file states 28. EMPIRICAL_DATA.txt says "~20 productive / ~8 non-productive" over lists of 35 and 4 items. A limitations section that introduces a new unsourced statistic weakens the section it strengthens.
- **Disposition:** State the derivation inline ("28 of 39 frameworks produced at least one finding") and correct EMPIRICAL_DATA.txt to enumerate 28 and 11.
- **Cross-reference:** F-SP2-15; R1 F-SP-3.

### LOW

**F-SP2-25** [LOW] -- Two DOI placeholders in a deposit-ready draft.

- **Locus:** PAPER.txt L626, L628 ("10.5281/zenodo.TBD" for Methodology v7 and XZ Protocol v0.75); REFERENCES.txt same.
- **Substance:** The paper's two most load-bearing internal citations are unresolvable. Acceptable pre-deposit; blocking at deposit.
- **Disposition:** Reserve both DOIs before submission; re-run the citation sweep after reservation.
- **Cross-reference:** F-SP2-15.

**F-SP2-26** [LOW] -- Dispatch labels the seat FRESH while assigning continuity tasks and shipping no R1 register.

- **Locus:** DISPATCH.txt L1 and L6-L8; AUDIT_CONTEXT.txt "Your task" items 1 and 3.
- **Substance:** A fresh seat cannot re-check findings it never made. This seat resolved the conflict by declaring continuous execution (S-0), which is honest but reduces the independence weight of S-3. The recurring alternative -- a seat that accepts the FRESH label and reports on continuity anyway -- is the seat-non-independence defect already on the program's record.
- **Disposition:** Either ship the R1 finding register in the packet and label the seat CONTINUOUS, or drop tasks 1 and 3 and label it FRESH. Do not label a seat fresh and task it with memory.
- **Cross-reference:** Quantum-orbital seat discipline (Pauli exclusion on continuity state); S-0 above.

**F-SP2-27** [LOW] -- Correction count stated inconsistently across the packet.

- **Locus:** DISPATCH.txt ("18 corrections applied") vs AUDIT_CONTEXT.txt ("Ten corrections were applied", followed by eight more under a second header).
- **Substance:** The reconciliation (10 + 8 = 18) is inferable but unstated. In a register whose function is completeness verification, an unstated total invites an incomplete sweep.
- **Disposition:** Single header, single numbered list, explicit total.
- **Cross-reference:** F-SP2-01.

---

## S-5. What the round says about the repair mechanism

Three observations the finding ledger does not carry on its own.

**The correction pass instantiated Story 3.** Correction 18 named two stale forms and repaired those two forms. Five stale anchors outside the enumerated forms survived -- including one inside the very sentence corrected by item 3. The paper's own prescription (L376: "The durable remedy is always the completeness assertion ... never the wider pattern") was available and not applied to the paper. The mechanical route is an assertion over the document: every round-range token resolves to R7-R31, every series count to 25, every terminus to R31, with the build failing on any residue.

**Two corrections created defects at the surfaces they repaired.** Correction 9 introduced a false claim about the document's own indexing conventions; correction 14 introduced a verbatim duplication. Both are absorption-induced regression, and both landed in the same pass that closed three CRITICAL findings. This is the R28 pattern at the prose layer: the repair mechanism producing the class of defect it exists to remove.

**The evidence files remained frozen while the paper moved.** The single highest-leverage action before Round 3 is not a paper edit. It is correcting EMPIRICAL_DATA.txt, FRAMEWORK_INVENTORY.txt, and shipping METHODOLOGY v7. Two of this round's three CRITICAL findings exist because the paper was checked against a substrate that agreed with its errors.

---

## S-6. Cross-vendor recommendation

This seat is producer-family and advisory; nothing here carries binding weight. The paper's own Axiom 4 forecloses a producer-family close on a producer-drafted artifact.

- **Round 3 binding read:** two non-producer families on the corrected bytes -- Kimi K3 and GPT-5.6 Sol are the strongest pair given their R1 REVISE verdicts (both hold priors on the specific loci). Gemini 3.1 Pro returned PASS at R1 on a draft carrying three CRITICAL defects; a Gemini seat should not be counted toward the two-family requirement this round.
- **Citation audit:** the three Qur'anic findings (F-SP2-03, F-SP2-17, and the 7:54 reading at L269) need a reader with mushaf access and tafsir competence, not a packet fact-check. This is the second consecutive round in which the packet's own citation file propagated the error under audit.
- **Mechanical sweep before dispatch:** run the completeness assertions from S-5 and F-SP2-01 and ship the grep transcript in the R3 packet. If the transcript is in the packet, the next round's correction verification takes minutes rather than a full seat.

---

## S-7. Ledger

| Severity | IDs | Count |
|---|---|---|
| CRITICAL | F-SP2-01, 02, 03 | 3 |
| HIGH | F-SP2-04 through 15 | 12 |
| MEDIUM | F-SP2-16 through 24 | 9 |
| LOW | F-SP2-25, 26, 27 | 3 |
| **Total** | | **27** |

Corrections verified landed: 11 of 18. Partial: 3. Landed with new defect: 1. Not landed: 3.
R1 findings closed: 4. Partial: 4. Open: 7 (of which 4 never entered the correction register).

**Verdict: HALT-AND-RETURN-TO-PRODUCER (REVISE).**

Seat S04, Claude Opus 5, advisory. Non-binding.

---

# Bismillah ir-Rahman ir-Rahim
