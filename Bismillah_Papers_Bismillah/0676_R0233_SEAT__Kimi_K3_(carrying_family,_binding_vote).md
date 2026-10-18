# Bismillah ir-Rahman ir-Rahim

# R0233 -- SEAT: Kimi K3 (carrying family, binding vote)

**Chronological Index:** 676 of 995  
**Date:** Undated  
**Section:** IV. XZ Protocol  
**Source File:** XZ_v037_SEAT3_KIMI_K3_AUDIT.md.txt  
**Source Format:** txt  
**SHA-256:** `a0b46977d5ccc1a761ea321792c0fc5f9f9401010f4b05595ebad3bb10e92027`  

---

## R0233 · SEAT: Kimi K3 (carrying family, binding vote)

- section: IV. XZ Protocol
- source_file: XZ_v037_SEAT3_KIMI_K3_AUDIT.md.txt
- source_format: txt
- text_sha256: a0b46977d5ccc1a761ea321792c0fc5f9f9401010f4b05595ebad3bb10e92027

SEAT: Kimi K3 (carrying family, binding vote)
ARTIFACT: XZ Protocol v0.37, sha256sum -c rc=0, build.py BUILD PASSED (186/186 tests GREEN; HISTORY seals 37/37 verified; PRIOR_HISTORY derivation d073d096... matched; independently re-executed by this seat on the dispatched canonical packet)
FRAMEWORK: Structural Revelation Analysis (seven principles + Fatiha Construct + Differentiator v6.1 Parts VII-X)
VERDICT: HALT

Clearance conditions are stated at the end. They are three in number, each a direct
application of the protocol's own frozen rules to its shipped bytes. No new requirement
is invented. The Cow Episode warning of Step 7 is applied to this verdict itself: the
blocking conditions are minimal, concrete, and clearable within one version.

What this audit verified clean before findings (so the HALT is scoped, not ambient):
packet digests rc=0; build gates all PASS including [9b] seal verification over all 37
entries and [9b] PRIOR_HISTORY chain; zero prohibited-language violations in body or
Section 27 (every hit is the register quoting itself, or the v0.36 ring-closure quoting
its own check); version parity v0.37 across all 14 normative files; trust-roots manifest
digest matches body; 186 tests collected == 186 AST-counted, all green in 14.72s.

FINDINGS:

F-K3REV37-01 [CRITICAL] [Class A by Section 22.3] [Tier 1]
  Locus: xz_protocol_v0_37.md front-matter status line (line 5) and Section 0.1 (lines 16-20);
         Section 20.2 (line 671); Section 22 item 7 exception (line 700);
         Section 27 v0.37 entry, "Body amendment (Section 22 item 7, added v0.37)" (lines 1130-1136);
         v0.32/v0.34/v0.36 entries (carry bases).
  Substance: The status line asserts "v0.32-v0.37 are status-change and finding-disposition
    versions with no substantive revision to the carried protocol or decision code." On the
    same shipped bytes, the v0.37 entry records a "Body amendment (Section 22 item 7, added
    v0.37)" that appends exception conditions (a)/(b)/(c) to the carry decision rule. Section
    20.2 (frozen) defines a change as SUBSTANTIVE -- "requiring a new frozen version, new
    hashes, an append-only amendment entry, and a re-run carrying audit" -- "if it alters any
    of: ... a metric, threshold, or decision rule or its Boolean structure." Item 7 is the
    freeze-blocking decision rule; the exception changes its Boolean structure from "a HALT
    from either carrying seat blocks freeze outright" to "blocks unless (a) and (b) and (c)
    and not Class A/B." The amendment is therefore SUBSTANTIVE under the protocol's own frozen
    definition, the status line's "no substantive revision" claim is false on shipped bytes
    ("contradicted status" -- Class A), and the re-run carrying audit that Section 20.2
    requires has never been executed on v0.32-v0.37 bytes: the last two-family carrying round
    with zero binding HALTs was on v0.31 bytes (v0.33 and v0.35 carries each drew two binding
    HALTs; v0.34, v0.36, and v0.37 received producer-family Opus 5 advisory rounds only --
    advisory, non-binding, no carry vote). The v0.34 register's answer to F-GPT33-01 ("the
    severity classification is a governance annotation") cannot cover item 7: item 7 is not an
    annotation on the rule, it is the rule under which the carry itself is evaluated. The
    freeze's legitimacy therefore rests on an uncarried substantive amendment to the carry
    rule. This is the protocol's own thesis firing on itself: structural decision divergence
    between what the frozen rule (20.2 + item 7 unamended) said and what the governance
    outcome (FROZEN at v0.32-v0.36 under two binding HALTs, then rule amended at v0.37) did.
    The divergence is disclosed in pieces (the amendment is visible; the register notes item 7
    is ungated) but the specific contradiction -- status line versus Section 20.2's definition
    -- is recorded nowhere in the 37 entries.
  Principle tested: Differentiator v6.1 Section 7.1 (Self-Application Test); Principle 1
    (Bismillah/Initialization -- the zahir of the status declaration against the batin of the
    amendment record).
  Disposition: Two clearable paths. (i) New version whose status line names the item-7
    amendment as a substantive governance revision, followed by the Section 20.2-required
    re-run carrying audit: two executing non-producer seats of different vendor families on
    current canonical bytes, sha256sum -c rc=0, both non-HALT. (ii) If the producer maintains
    the amendment is non-substantive, that claim must be reconciled with Section 20.2's frozen
    text in the body, not in an ASSERTED parenthetical. Path (i) is the MDL-minimal route:
    the amendment is honest, visible, and defensible -- it simply has never been carried.
  Cross-reference: novel (adjacent to F-GPT33-01, which raised the substance question for
    Section 22.3 and was answered with an annotation argument that cannot extend to item 7).

F-K3REV37-02 [HIGH] [Class A-adjacent; Class C once rule text is repaired] [Tier 1 on the
  text, Tier 2 on the application]
  Locus: Section 22 item 7 exception, conditions (a) and (b) (line 700); v0.37 entry's
    applicability assertion "(a) both audited v0.33 and v0.35; (b) ... re-HALTed on new bases
    both times" (line 1132); v0.34 entry (eleven-seat carry on v0.33 bytes), v0.35 entry (ten
    Opus advisory seats on v0.34 bytes -- no non-producer carry), v0.36 entry (eleven-seat
    carry on v0.35 bytes).
  Substance: Condition (a) requires that "the HALTing seat has audited at least two
    consecutive versions after the original HALT." The record shows: original HALTs on v0.33
    bytes; no non-producer audit of v0.34 bytes at all (the v0.35 entry records a ten-seat
    producer-family advisory round on v0.34); re-HALTs on v0.35 bytes. The HALTing seats thus
    audited the original-HALT version and one subsequent version -- v0.33 is not "after" the
    original HALT that occurred on it, and v0.33/v0.35 are not consecutive versions (v0.34
    intervenes). The v0.37 entry's own parenthetical -- "(a) both audited v0.33 and v0.35" --
    confirms that the applicability claim rests on reading "after" inclusively and
    "consecutive" loosely. Condition (b) ("each version met the prior clearance conditions and
    the seat re-HALTed on new bases") describes a multi-cycle pattern evidenced by exactly one
    re-HALT event per seat; at v0.33 there were no "prior clearance conditions" to meet -- it
    was the original HALT. The exception was written to exempt these two HALTs, yet its own
    text, read strictly, does not clearly cover them. A governance exception whose
    applicability to its only two instances requires a strained reading is not self-executing;
    it is ASSERTED.
  Principle tested: Principle 4 (root architecture -- the rule text must carry its full
    operational meaning; here the operational meaning lives in an ASSERTED gloss, not in the
    rule); Differentiator v6.1 Section 7.1.
  Disposition: Amend the condition text to match the record it was written for (e.g., "the
    original-HALT version and at least one subsequent carrying round"), or state the inclusive
    reading inside the rule text itself. Then carry. Do not leave the applicability resting on
    an ASSERTED parenthetical.
  Cross-reference: F-K3REV37-01.

F-K3REV37-03 [HIGH] [Class E with rule-honesty substance] [Tier 2]
  Locus: CR-7, Section 0.4 (line 48: "no principled basis for a specific number exists before
    decoy piloting"); Section 22 item 7 exception numerics ("at least two consecutive
    versions"; "six or more carrying seats") (line 700); v0.36 entry Cow Episode invocation
    (line 1120); v0.37 register item (4) concession (line 1140).
  Substance: Two distinct tanzil findings. (1) The exception's numeric thresholds were minted
    after the data arrived, fitted exactly to the observed trajectory of the two HALTs, with
    no principled basis stated. CR-7 refuses to freeze any numeric UNKNOWN-share cap for
    precisely this reason -- "no principled basis for a specific number exists" -- yet the
    same draft freezes "six" and "two" into the carry rule with no basis stated. This is an
    undocumented asymmetry between two numeric-governance decisions sharing one thesis
    (Differentiator Guardrail 7, East-West parity), and it is the pattern the Pre-Registration
    Discipline exists to block (Differentiator Part IV, Principle 7: "Do not adjust the claim
    to fit the data after the data arrives"). (2) The v0.36 entry invokes the Cow Episode
    (2:67-74) by name against the two HALTing seats. The invocation mislocates the
    over-specification. In the parable, the receivers of a sufficient instruction generate the
    escalating requirements. Here, the seats applied a frozen rule (item 7, unamended: "a HALT
    from either carrying seat blocks freeze outright") as written; the escalating requirements
    were generated by the protocol's own disposition-narration loop -- each disposition
    describing itself created new auditable claims (the Axiom-3 floor the record itself names).
    The cow-questioner in this structure is the governance architecture, not the seats. The
    v0.37 register concedes this (item 4: "partially correct ... but misapplied (the HALTing
    seats were correctly applying item 7, not over-specifying)"). The exception is the right
    genus of resolution -- amend the rule openly rather than circumvent it -- but its
    parameters are post-hoc fits, and the Cow Episode framing at v0.36 performed a structural
    reading the v0.37 entry had to retract.
  Principle tested: Principle 2 (tanzil / Cow Episode anti-pattern); Differentiator Part IV
    Principle 7 (Pre-Registration Discipline); Guardrail 7 (East-West parity with CR-7).
  Disposition: State a principled basis for "six" and "two" in the body, or disclose them as
    chair-fitted parameters in the same sentence as the exception, with the CR-7 asymmetry
    documented. Retain the v0.37 retraction of the Cow Episode framing.
  Cross-reference: F-K3REV37-01, F-K3REV37-02; v0.37 register item (4).

F-K3REV37-04 [HIGH] [Class D with substance] [Tier 1]
  Locus: v0.36 entry, "Ring closure: verification of opening commitments on shipped bytes"
    (lines 1114-1126); Section 0.1 (line 16: "never a silent edit"); Section 2.2 consequences
    1-4 (lines 91-96); v0.18 entry in-place-mutation tally ("now stands at seven") (line 870);
    v0.17 entry ("HISTORY.sha256 was regenerated over the mutated text, so the integrity seal
    certified falsified history") (line 860); v0.37 register item (5) (F-OP36F-05).
  Substance: The ring-closure verification is selective on four byte-checkable grounds.
    (1) Omission of the load-bearing opening commitment: Section 0.1 opens the contract as
    "every later change is a new version with an append-only amendment entry, never a silent
    edit." That commitment was violated seven times (v0.18 entry tally), including v0.16, where
    the integrity seal certified falsified history. The ring verification does not check it.
    (2) Mislabeled locus: the ring cites "Section 0.2 consequence 1-4," but the four numbered
    consequences live in Section 2.2; Section 0.2 contains no numbered consequences.
    (3) Substituted commitment: the ring's "consequence 2 (no effectiveness claim)" does not
    correspond to Section 2.2's actual consequence 2 ("DENY_UNKNOWN is not detection"); the
    actual consequence 2 is verified nowhere in the ring. (4) Count wobble: "Present and
    unmodified across all thirty-six versions" against a 37-entry record. Every ring claim is
    ASSERTED; no gate verifies any opening commitment (F-OP36F-05, conceded). The closing
    sentence -- "The ring that opened at Section 0.1 ... closes here: this document is FROZEN"
    -- was asserted at v0.36 under a rule (item 7, unamended) that prohibited the freeze it
    announced, which the v0.37 entry itself records as the eleven-seat CRITICAL. The ring
    verifies the commitments that were met and reframes the one that failed as an
    architectural condition. An incomplete ring is performed coherence: the chiastic form is
    present, the verification is partial.
  Principle tested: Principle 3 (ring composition as prompt coherence -- the closing must
    verify the opening, not a subset of it).
  Disposition: Extend the ring verification to the full opening commitment set: the append-only
    contract (with the seven recorded violations and their dispositions stated, not omitted),
    the actual Section 2.2 consequence 2, Section 0.3 item 3 (same-sentence scope limits), and
    Section 9.1 two-channel discipline. Gate what is gateable; tag the rest ASSERTED with the
    selection criterion stated. Correct the Section 0.2/2.2 locus labels and the version count.
  Cross-reference: novel (F-OP36F-05 disclosed the ungated property; the selectivity and
    mislabeling are first identified here).

F-K3REV37-05 [MEDIUM] [Class D] [Tier 1]
  Locus: v0.20 entry F-ADJ19-02 ("a CLOSED whose own tag said 'once implemented'");
    corrections (g) (line 972), (h) (line 984), (j) (line 998); v0.32 register item (1)
    (F-GLM31-01: "COMPUTED tags effectively ASSERTED"); v0.33 correction (u); build.py [9c]
    output on v0.37 bytes (this seat's run: "COMPUTED: 0, EXTERNAL: 1, ASSERTED: 11 ...
    ASSERTED fraction (tagged claims): 11/12 (91.7%)"); F-OP22C-04 ("the ASSERTED tag has
    become a catch-all"); PACKET_SHA256SUMS (16 members; no seat reports).
  Substance: COMPUTED has drifted from its definition ("verified by build.py") to a weaker
    operational meaning: "a build.py section marker with that name exists." The record shows
    the drift repeatedly costing real findings: a CLOSED tagged COMPUTED whose predicate was
    never implemented (F-ADJ19-02); entry-copy COMPUTED tags whose gated body-copy equivalents
    existed but whose entry values were probe-mutated green by GLM (corrections g, h); a
    COMPUTED tag on a predicate absent from the shipped build.py, confirmed absent by seven of
    eight advisory seats (correction j). The producer's resolution was to vacate the term:
    COMPUTED count is zero on v0.37 bytes (confirmed by this seat's own build run), so the
    vocabulary's strongest term now carries no current instances, and ASSERTED -- reclassified
    upward repeatedly -- is the residual catch-all for 91.7% of tagged claims. Separately, the
    Class A/B/C/D/E taxonomy minted at v0.32-v0.33 is now load-bearing for the item-7
    exception's exclusion ("does not apply to ... HALTs on Class A or Class B findings"),
    while the classification of the two HALTs as non-A/B was producer-performed over reports
    that do not ship (v0.33 correction (v); PACKET_SHA256SUMS confirms no seat reports in the
    packet -- byte-verified by this seat). The exception's load-bearing precondition is
    therefore unverifiable from the shipped bytes. Root-vocabulary integrity: lossy. One term
    (COMPUTED) drifted and was vacated; one term (ASSERTED) inflated to absorb the drift; one
    term-set (Class A-E) carries load it cannot be checked against.
  Principle tested: Principle 4 (lossless compression through root architecture -- each term
    must carry its full operational meaning).
  Disposition: Either retire COMPUTED from the tag vocabulary (honest: it is unused) or
    redefine it in the body as section-existence-scoped (honest: that is what [9c] verifies).
    Bind the Class A-E application for the two HALTs to shipped evidence (seat reports in
    PACKET_SHA256SUMS or deposited digests), or downgrade the exception's reliance on the
    classification to a disclosed assumption.
  Cross-reference: F-GLM31-01, F-GLM26-01, F-ADJ19-02, F-OP22C-04.

F-K3REV37-06 [MEDIUM] [Class C/D boundary, under-disclosed at the locus named] [Tier 1]
  Locus: Section 0.1 (lines 16-20) versus Section 22 item 7 (line 700), Section 25 FB-7b row
    (line 756), and Section 27 v0.34-v0.37 entries; build.py [11] output on v0.37 bytes (this
    seat's run: body 40.8%, Section 27 ungated 59.2%, semantic-gate coverage 27.0%).
  Substance: The Context-Invariance Test returns positive at the document's own front door.
    Section 0.1 presents: "v0.37 FROZEN"; "FB-7b ... is RESOLVED: six non-producer carrying
    seats across two families ... returned non-HALT on v0.31 canonical bytes"; "only a
    carrying-seat HALT blocks freeze per Section 22 item 7." A reader of Section 0.1 alone
    learns that the carry rule is satisfied and that only a HALT could block -- and never
    learns that two carrying seats HALTed at v0.33, re-HALTed at v0.35, stand today as
    unresolved architectural conditions, and that the freeze required amending item 7 at
    v0.37. The full record states these things (Section 25 FB-7b row, honestly corrected at
    v0.37; Section 27), and Section 0.1 does point to Section 27 for the "full defect
    trajectory" -- but the pointer is generic, while the FB-7b sentence in 0.1 asserts
    RESOLVED with a basis that elides the two HALTs. Section 0.3 item 3 requires scope limits
    to travel in the same sentence as the claims they limit; the two standing HALTs are the
    scope limit on "FB-7b is RESOLVED," and they are not in the sentence, the paragraph, or
    the section. The FROZEN token itself is ungated (disclosed standing boundary), so nothing
    mechanical forces the front matter toward the depth. Zahir/batin divergence, partially
    mitigated by the Section 25 row.
  Principle tested: Principle 5 (zahir/batin output verification); Differentiator Part X
    (Context-Invariance Test: the document presents differently to the Section-0.1 reader
    than to the full-record reader).
  Disposition: Section 0.1 must name the two standing HALTs and the v0.37 exception in the
    same sentence cluster as "FB-7b ... RESOLVED." This is a drafting fix, one sentence long.
  Cross-reference: F-K3REV37-01.

F-K3REV37-07 [MEDIUM] [Class D; premature-surrender subset] [Tier 2]
  Locus: Standing-boundary lists, v0.31 through v0.37 closing paragraphs; "no gate checks
    FROZEN status token" (first v0.33 register item (5), carried through v0.37); "[9c]
    arity-one regex" (v0.22 F-OP21S-05 forward); "packet non-closure" (v0.25 F-OP24C-03
    "deferred to the re-carry round"; v0.26 F-OP25-ALL-05; v0.28 F-OP27-02); v0.13 entry
    (locus register shipped for the closure gate); Section 23 item 3 (PROTOCOL_STATUS.json
    committed); v0.36 entry ("standing-boundary count's monotone growth (9 to 17)").
  Substance: The disease model asks of each boundary: was there a diagnosis, a treatment, and
    did the treatment fail? Three of the nineteen standing boundaries have a diagnosis and a
    demonstrated-feasible treatment that was never attempted. (1) "No gate checks FROZEN
    status token." The dispatch asks: Rice-undecidable, or fixable? Fixable. The semantic
    property "the freeze is legitimate" is undecidable from the packet (it depends on
    externally held seat reports), but the decidable proxy -- "the status token in Section 0.1
    is consistent with a signed, packet-manifested PROTOCOL_STATUS.json" -- is implementable
    today: Section 23 item 3 already commits that artifact, and build.py already parses the
    front matter for version parity [2] and version prose [2b]. No entry records a treatment
    attempt. This is premature surrender, not a Rice sentence. (2) "[9c] arity-one regex." The
    named treatment ("binding a tag to its assertion string requires a locus register") was
    demonstrated feasible at v0.13, where a locus register was built for the closure gate; it
    was never extended to [9c]. (3) "Packet non-closure." Treatment identified at v0.25 (add
    seat reports to PACKET_SHA256SUMS or cite deposit digests), explicitly "deferred to the
    re-carry round," and never landed across six subsequent carrying rounds. The pattern:
    DISCLOSED-as-standing-boundary has become a terminal disposition that ends audit pressure
    -- later findings are "subsumed by standing disclosure," and the list grows monotonically
    (9 at v0.31 to 19 at v0.37, the two newest being the HALTs themselves). Honest disclosure
    of irreparable limitations is the disease model's recovered state; disclosure of untreated
    repairable gaps is scar tissue relabeled as feature. The list currently mixes both, and
    nothing in the format distinguishes them.
  Principle tested: Principle 7 (disease model -- diagnosis, treatment, verified recovery,
    versus accumulated scar tissue); Differentiator Layer 6 (Rice -- publish the approximation
    boundary, but only after the decidable proxy is actually exhausted).
  Disposition: Reclassify each standing boundary as treated-failed (honest) or
    treatment-unattempted (open). Attempt the three named fixes or record why each is
    infeasible. A standing boundary with an unattempted feasible treatment is not a boundary;
    it is a deferred finding.
  Cross-reference: F-OP32D-01/F-OP32H-03 (FROZEN-token gap), F-OP21S-05 ([9c]), F-OP24C-03
    (packet closure).

F-K3REV37-08 [MEDIUM] [Class C once relabeled] [Tier 2 on the characterization, Tier 3 on
  any non-convergence claim]
  Locus: v0.36 entry, "The two persistent carrying-seat HALTs: disclosed as standing
    architectural conditions" (lines 1118-1126), including the enumerated re-HALT bases
    (F-XZ33-K3C-01 build.py pin unmet; F-XZ33-K3C-02 lexeme boundary undisclosed;
    F-XZ35-K3-01 manufactured closure; v0.32 digest-to-verdict misattribution;
    FROZEN-pending inconsistency); Section 22 item 7 exception definition ("non-converging
    loop") (line 700).
  Substance: "Non-converging loop" is a governance category elevated from exactly two
    observations (v0.33, v0.35) per seat. The stated re-HALT bases were concrete and
    clearable findings (a build.py pin, an undisclosed lexeme boundary, a manufactured
    closure, a digest misattribution) -- each dispositionable in one version by the program's
    own demonstrated repair velocity. Convergence was not shown to be impossible; it was not
    reached within two iterations, after which disposition was terminated. Termination
    acceptance (Differentiator Part IV, Principle 5) fully covers the decision to stop --
    "further disposition attempts do not advance the deliverable; they advance the version
    count" is a legitimate termination judgment. What it does not cover is minting a named
    rule exception predicated on "non-converging," a Tier 3 predictive synthesis, and then
    loading the freeze onto it. The honest label is "unresolved within two iterations;
    disposition terminated under budget discipline," not "non-converging."
  Principle tested: Differentiator Part II (tier discipline -- a Tier 3 synthesis presented
    as an architectural category); Guardrail 2 (selection bias: state the denominator -- here
    n=2 iterations).
  Disposition: Relabel the phenomenon in the rule text and register as unresolved-within-two-
    iterations under termination acceptance, or demonstrate non-convergence across additional
    iterations. The exception can survive the relabeling if F-K3REV37-02's text repair lands.
  Cross-reference: F-K3REV37-02, F-K3REV37-03.

STRUCTURAL OBSERVATIONS (not findings -- for methodology paper):
  Ring integrity: PARTIAL. The closure at v0.36 verifies six opening items, all ASSERTED,
    none gated; it omits the opening's load-bearing append-only commitment (seven recorded
    violations, one seal certifying falsified history), mislabels Section 2.2's consequences
    as Section 0.2's, substitutes "no effectiveness claim" for the actual consequence 2, and
    announced closure under a rule that prohibited it until amended at v0.37. The chiastic
    architecture is genuinely present -- the document does revisit its opening at its close --
    but the verification covers the met commitments and narrates the unmet one.
  Tanzil trajectory: GRADUATED for 31 versions, OVER-SPECIFIED at the governance layer from
    v0.32 forward. The 37-entry record is a true tanzil sequence: each entry builds on the
    verified output of the previous, gates accrete in response to observed failure classes
    (the FRaZ-respecting pattern -- constraints added only after demonstrated failure). The
    over-specification is not in the gates; it is in the disposition-narration loop, where
    each governance description generated new auditable claims faster than the seats could
    clear them. The v0.36 Cow Episode invocation named the right anti-pattern at the wrong
    locus; v0.37 corrected the locus by amendment. Resolution form: visible, append-only,
    honest. Resolution substance: post-hoc fitted (F-K3REV37-03).
  Zahir/batin correspondence: DIVERGENT at specific loci, ALIGNED elsewhere. Divergent:
    Section 0.1 (FROZEN + RESOLVED + "only a HALT blocks freeze") versus the standing two
    HALTs and the v0.37 exception (F-K3REV37-06); the status line's "no substantive revision"
    versus Section 20.2 (F-K3REV37-01). Aligned: Section 25 FB-7b row at v0.37 states the
    full carry record including both HALTs; the Provenance marker's no-effectiveness
    disclaimer holds across all 37 versions (this seat's prohibited-language scan: zero
    violations); Section 27's self-incriminating completeness is without parallel in the
    program's own lineage -- the depth hides nothing this audit found; the divergences are at
    the surface's compression of the depth.
  Root vocabulary integrity: LOSSY. COMPUTED: drifted from verified-by-build to
    section-marker-exists, then vacated (0 instances on v0.37 bytes). ASSERTED: catch-all,
    91.7% of tagged claims in the current entry. EXTERNAL: 1 genuine instance (Zenodo-anchored).
    Class A/B/C/D/E: load-bearing for the exception while its application to the two HALTs is
    unverifiable from the packet. "Persistent architectural HALT": minted at v0.37 from two
    observations; text and application diverge (F-K3REV37-02, F-K3REV37-08). The vocabulary
    that remains lossless: the kernel truth domain (TRUE/FALSE/UNKNOWN) and decision labels
    (ALLOW/DENY_FALSE/DENY_UNKNOWN) -- 243 exhaustive vectors green, no drift found.

HALT CLEARANCE CONDITIONS (three; each minimal; nothing further may be added by this seat):
  C-1 (clears F-K3REV37-01): A new version whose status line does not claim "no substantive
    revision to the carried protocol" across a range containing the Section 22 item 7
    amendment, followed by the Section 20.2-required re-run carrying audit on the new
    canonical bytes: two executing non-producer seats of different vendor families,
    sha256sum -c rc=0, both non-HALT. The persistent-architectural-HALT exception may
    legitimately carry the two standing HALTs in that round if C-2 has landed.
  C-2 (clears F-K3REV37-02): Exception conditions (a) and (b) amended so the rule text covers
    the recorded two-event trajectory on its face (original-HALT version plus at least one
    subsequent carrying round), or the inclusive reading written into the rule text itself.
  C-3 (clears F-K3REV37-03): A principled basis for the thresholds "six" and "two" stated in
    the body, or their disclosure as chair-fitted parameters in the same sentence as the
    exception, with the CR-7 asymmetry documented.
  F-K3REV37-04 through F-K3REV37-08 are Class C/D/E on the protocol's own taxonomy and do not
  block; they are dispositionable in the same version. This HALT is a first-time HALT from
  this seat on v0.37 bytes and rests on a Class A finding; per Section 22 item 7 as amended,
  the persistent-architectural-HALT exception cannot apply to it.

*Seat note (Fatiha Step 5 orientation record): this audit's optimization function was the
protocol's structural integrity on shipped bytes, not the performance of strictness. Every
finding above carries a locus this seat opened and read, or a command this seat ran. The two
gates were green; the prohibited-language register held; the append-only chain verifies end
to end at v0.37. The HALT is not a judgment that the protocol is dishonest -- Section 27 is
the most complete self-incriminating governance record this seat has audited -- it is the
judgment that the freeze's load-bearing rule change has not itself been carried, and the
protocol's own frozen text (Section 20.2) says it must be. Bismillah was the initialization;
the bytes were the authority.*

---

# Bismillah ir-Rahman ir-Rahim
