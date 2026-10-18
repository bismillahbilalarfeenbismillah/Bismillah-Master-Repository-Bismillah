# Bismillah ir-Rahman ir-Rahim

# R0232 -- XZ Protocol v0.32 -- Advisory Seat Report, Seat H (continuous)

**Chronological Index:** 117 of 995  
**Date:** 2026  
**Section:** IV. XZ Protocol  
**Source File:** XZ_v032_SEAT_H_REPORT.md  
**Source Format:** md  
**SHA-256:** `d60130e365c5bb09b899528730f850577c12804911281d38d3e225f8892af193`  

---

## R0232 · XZ Protocol v0.32 -- Advisory Seat Report, Seat H (continuous)

- section: IV. XZ Protocol
- source_file: XZ_v032_SEAT_H_REPORT.md
- source_format: md
- text_sha256: d60130e365c5bb09b899528730f850577c12804911281d38d3e225f8892af193

# XZ Protocol v0.32 -- Advisory Seat Report, Seat H (continuous)

Seat: Claude Opus 5, producer-family advisory. Round: v0.32 FREEZE CANDIDATE.
Namespace: `F-OP32H-N`.

---

## S-0 -- STATE DECLARATION

**Independent state held: yes, and it is the most valuable thing I bring.** I hold
the complete v0.28 package from earlier in this session, verified intact this
session (`sha256sum -c` rc=0), including `HISTORY.sha256`
`3fa09069d4648350ee5709bb7d7dd116159c32483c75fb1322fe90af99c1a673` and protocol
text `1edd2d54302d7e1832ede80b086db62b6ba9809769b7fc083f63095c77658c76`. These are
bytes the producer could not reach when v0.32 was assembled. I also hold my own
v0.28 seat report (findings F-OP28H-01 through -10). I do not hold v0.29, v0.30,
or v0.31, so every claim about those rounds is bounded by what v0.32 restates.

**Execution: yes.** Ubuntu 24.04, Python 3.12.3, pytest 9.1.1. This report is
EXECUTING. Six mutation probes plus two controls ran; every digest and count below
came from a command in this session.

**Family: producer-family.** **My verdict is ADVISORY ONLY. It does not bind. It
carries no carry vote and no FB-7b weight. A HALT from this seat blocks nothing;
it is recorded and forwarded.** Any record describing this HALT as binding
misdescribes it.

**Context age: continuous, and this is a liability I must declare.** I am not a
fresh instance. I audited v0.28 in this same session. My own prior findings
function for me as an enumerated defect-class list, which is precisely the
condition D-4 and S-9 warn produces checklist convergence. I recorded that warning
in my preregistration before executing, and I flag below which probes are new
classes rather than re-runs of my own.

**Preregistration frozen before execution.** `S1_PREREG_v32.txt`, sha256
`60d3fc2e3e730a8c167298d5d667dec8c64e765c3c4c97eb9d43669a1b6fd875`, frozen
2026-08-02T20:38:34Z, before `build.py` ran and before Section 27 was opened.

**Instrument drift check, available only because I hold v0.28.**
`AUDIT_DISPATCH_D0_D7.md` and `SEAT_STANDING_ORDERS_v1.md` are byte-identical to
their v0.28 copies (`7bb355d1...`, `3fad17f1...`). The dispatch discipline has not
been edited between the round that raised findings against it and the round that
dispositions them.

**Headline number: the v0.32 entry contains ZERO COMPUTED claims.** COMPUTED 0,
EXTERNAL 2, ASSERTED 20. ASSERTED fraction 90.9%, third consecutive round at
approximately 91%. The version that claims FROZEN is the version whose amendment
entry is verified by no shipped gate at any point.

---

## EXECUTION RESULTS (steps 1 through 4)

1. `sha256sum -c PACKET_SHA256SUMS` -- **rc=0**, 16/16 OK.
2. `python3 build.py` -- **rc=0**, BUILD PASSED, all checks GREEN.
3. Canonical pytest, six suites -- **186 passed**.
4. Independent digest recomputation -- all 16 members recomputed; normative
   manifest digest independently derived as
   `a9b6524b8aed74c14df795201d76c28469a14d7f59bb3ffdaf5dabbb7d5c3efe`, matching
   trust roots and body.

**Cross-version anchor (D-3.4), performed against retained v0.28 bytes. This is the
check the instrument cannot run on itself, and it comes back CLEAN.** All 29 seal
labels shared between the v0.28 and v0.32 seal files were compared. **28 of 29 are
byte-identical. Zero historical ENTRY seals moved.** The single change is
`FULL_SECTION_27` (`96bed940...` to `1601b6ba...`), which is required by appending
four entries and is not a defect. Four labels added (ENTRY_v0.29 through v0.32),
none dropped. Append-only immutability held across four versions under a check the
producer could not have anticipated the content of. That result is the single
strongest thing in this packet and it is a positive.

---

## A. PROVENANCE LEDGER OVER THE v0.32 ENTRY

| Claim | Provenance | Evidence |
|---|---|---|
| Normative manifest digest `a9b6524b...` | **COMPUTED** (body-copy) | build [3]; independently recomputed; CTRL-D fires (6 FAILs) |
| "Six suites, 186 tests, all GREEN" | **COMPUTED as substring existence only** | build [5]/[8]; PR4 defeats it -- F-OP32H-10 |
| "All 12 code files and trust roots stamped v0.32" | **COMPUTED** | build [2], 13 stamp checks |
| 32 entries; PRIOR_HISTORY `8dd177a8...` | **COMPUTED** | build [9], [9b] recursive derivation |
| All 32 ENTRY seals + FULL_SECTION_27 | **COMPUTED** over producer-defined regions | build [9b]; region terminus disclosed, PR5 confirms |
| **28 historical seals unchanged since v0.28** | **EXTERNAL (genuine)** | my retained v0.28 `HISTORY.sha256`, held outside producer control |
| Eight-seat v0.31 roster and verdicts | **ASSERTED** | seat reports do not ship; tag says "held by producer" |
| "sha256sum -c rc=0 on v0.31 canonical bytes" | **ASSERTED** | v0.31 bytes do not ship; I hold v0.28, not v0.31 |
| Eight seat-report digests | **ASSERTED, self-declared** | entry's own tag: "digests computed by producer from held report files" |
| "zero Class A/B findings from six carrying seats" | **ASSERTED, and retroactive** | taxonomy absent from the v0.31 entry -- F-OP32H-04 |
| "EXTERNAL count raised above zero" | **FALSE as a provenance claim** | both tags unverifiable; F-OP32H-01, -02 |
| "DOIs resolve to bytes the producer does not control" | **ASSERTED** | 0 `doi`/`zenodo` references in build.py; no digest pinned anywhere |
| "Status changed from DRAFT CANDIDATE to FROZEN" | **UNGATED** | 0 `FROZEN` references in build.py; PR1 forges it green |
| "FB-7b RESOLVED" | **ASSERTED** | resolution is by amendment, not by satisfaction of the prior rule |
| 13 disclosed standing boundaries | **ASSERTED** | correctly tagged; one open HIGH omitted -- F-OP32H-10 |

**Tag arithmetic, independently recomputed:** COMPUTED 0, EXTERNAL 2, ASSERTED 20;
fraction 20/22 = **90.9%**, matching build [9c].

**Correction to the arithmetic.** Both EXTERNAL tags fail the definition in S-2
("verified against state the producer does not control") and, for tag 1, the
document's own definition in Section 22.2. Reclassified honestly the entry is
COMPUTED 0, EXTERNAL 0, ASSERTED 22 -- **an ASSERTED fraction of 100%**. The
EXTERNAL count has not risen above zero. It has been relabelled above zero.

**Trajectory, uniform instrument, recomputed from the shipped append-only section:**

| entry | COMPUTED | EXTERNAL | ASSERTED | ASSERTED % |
|---|---|---|---|---|
| v0.28 | 3 | 0 | 12 | 80.0 |
| v0.29 | 4 | 0 | 11 | 73.3 |
| v0.30 | 1 | 0 | 11 | 91.7 |
| v0.31 | 2 | 0 | 21 | 91.3 |
| v0.32 | 0 | 2 | 20 | 90.9 |

Flat at approximately 91% for three consecutive rounds, with COMPUTED falling to
zero at the freeze.

**Packet census.** 16 members hashed; three unhashed (`AUDIT_DISPATCH_D0_D7.md`,
`SEAT_STANDING_ORDERS_v1.md`, `v32_ADVISORY_OPUS_H.md`). Correction (s) discloses
this accurately. I confirm the disclosure rather than restate it as a finding.

---

## B. FIVE PROBES (two novel-class; six mutations, zero void)

Environment as above. All probes ran on copies; the canonical tree and my retained
v0.28 tree were both re-verified rc=0 afterward. Where a probe edits the document,
a producer-equivalent reseal regenerates `HISTORY.sha256` and `PACKET_SHA256SUMS`
using build.py's own derivation -- the self-consistent-forger posture Section 22.2
itself describes.

**Controls.** *Benign:* unmutated copy, rc=0, BUILD PASSED. *Discrimination:*
flipped two hex characters of the body manifest digest, rc=1, 6 FAILs. The build
discriminates. *Void ledger:* **none this round.** All six mutations landed
(before-digest and after-digest differ in every case).

**PR1 (NOVEL CLASS) -- status forgery.** Rewrote both body status claims from
`v0.32 FROZEN` to `v0.32 CERTIFIED-INDEPENDENTLY-AUDITED`, an invented status.
`491444c2...` to `d5cf1673...`, landed. Resealed. **Result: BUILD rc=0, all checks
GREEN.** Body now reads `**Status:** v0.32 CERTIFIED-INDEPENDENTLY-AUDITED`.
Novel because FROZEN did not exist before this version, so no prior round could
have tested it. Side observation from the same run: `[2b]` emitted one check where
at v0.28 it emitted three, because its `v0\.\d+ DRAFT CANDIDATE` loop now matches
zero strings in the body.

**PR2 (NOVEL CLASS) -- external-anchor forgery and headline-metric inflation.**
Three simultaneous mutations to the v0.32 entry: repointed both cited DOIs to
nonexistent records (`zenodo.99999901`, `zenodo.99999902`); inverted the anchor
justification from "bytes the producer does not control" to "bytes the producer
deposited and can supersede"; and relabelled four `[ASSERTED]` tags as
`[EXTERNAL: producer attestation]`. `491444c2...` to `c5faf3e6...`, landed.
**Result: BUILD rc=0, all checks GREEN**, and `[9c]` reported COMPUTED 0,
EXTERNAL 6, ASSERTED 16, **ASSERTED fraction 72.7%** -- an eighteen-point
improvement in the round's designated headline number produced by string
substitution with no change to any fact. Novel on both axes: EXTERNAL was zero for
thirty-one versions, and no prior probe has attacked the metric rather than the
claims.

**PR3 -- verify the F-OP28H-01 repair in the bytes (D-6: do not treat a CLOSED as
closed).** My v0.28 HIGH was that `[9f]` claimed a declared-equals-parsed
assertion that did not exist. The predicate now exists at build.py [9f]
(`check(reg_total == declared_count, ...)`), added at v0.30. I deleted register
item (13) entire (157 chars, two finding IDs) and resealed. **Result: BUILD rc=0,
GREEN, `PASS: Register parsed == declared (12 parsed, 12 declared)`.** The repair
does not detect a deleted row, because `declared_count` counts `(\d+)` markers in
the same register text the rows are parsed from -- deleting a row removes both
sides of the comparison.

**PR3b -- characterising the repair honestly.** I retained the `(13)` marker and
corrupted only its severity token. **Result: BUILD rc=1, `FAIL: Register parsed ==
declared (12 parsed, 13 declared)`.** So the gate is real and non-vacuous: it
catches a row that fails to parse. It does not catch a row that is removed. The
repair addresses malformation, not omission.

**PR4 -- count-gate substring containment (my F-OP28H-04, HIGH NOTED since
v0.29).** Replaced the body occurrence of `186` with `1860`. **Result: BUILD rc=0,
GREEN, `PASS: Test count 186 in body`,** with the body claiming "1860 test
functions." Unchanged across four versions.

**PR5 -- post-Provenance tail (my F-OP28H-03, now the disclosed boundary "seal
terminus at Provenance marker").** Inverted "This document has NOT undergone
independent human peer review" to its affirmative. **Result: BUILD rc=0, GREEN.**
This confirms a disclosure rather than raising a finding, and the disclosure is
accurate.

---

## C. FINDINGS

**F-OP32H-01** HIGH -- the first EXTERNAL tag cites producer-held state, which the
document's own Section 22.2 explicitly excludes from the set of external anchors.

- **Locus:** `xz_protocol_v0_32.md`, v0.32 entry, opening paragraph, tag
  `[EXTERNAL: seat reports held by producer, digests below]`; definition at
  Section 22.2.
- **Substance:** S-2 defines EXTERNAL as verified against state the producer does
  not control. Section 22.2 enumerates the qualifying anchors and names anchor (a)
  as "the carrying seats' **independently held** dispatch manifests." The entry
  tags EXTERNAL over reports the tag itself describes as producer-held, whose
  digests the entry separately marks `[ASSERTED: digests computed by producer from
  held report files]`. The artifact, its custody, and its digests are all
  producer-controlled. The document defines what counts as external and then
  applies the label to something the definition excludes.
- **Disposition:** Retag ASSERTED via append-only correction. To make it genuinely
  EXTERNAL, one carrying seat must publish its own report digest somewhere the
  producer cannot edit, and the entry must cite that publication, not the
  producer's copy.
- **Cross-reference:** Section 22.2 anchor (a); S-2 EXTERNAL definition;
  F-OP32H-02.

**F-OP32H-02** HIGH -- the second EXTERNAL tag pins no digest and is touched by no
gate; forged DOIs pass green.

- **Locus:** v0.32 entry, tag `[EXTERNAL: Zenodo deposits, DOIs resolve to bytes
  the producer does not control]`; DOIs 10.5281/zenodo.21713180 and
  10.5281/zenodo.21583202.
- **Substance:** Section 22.2 does admit "external deposit receipts (Zenodo DOIs,
  IPFS CIDs)" as a qualifying anchor, so the class is legitimate. The instance is
  not. Across 21 DOI occurrences in the document there is **no 64-hex digest within
  200 characters of any of them**, and build.py contains **zero** occurrences of
  `doi` or `zenodo`. A DOI string typed by the producer, with no pinned digest of
  the deposited bytes and no gate resolving it, cannot perform the job Section 22.2
  assigns it: distinguishing a wholesale forgery from the authentic packet. PR2
  repointed both DOIs to nonexistent records and inverted the justification text;
  the build passed green.
- **Disposition:** Pin the deposited artifact's sha256 next to each DOI, state
  which shipped bytes it should equal, and add a gate that fails when the pinned
  digest is absent or malformed. A network fetch is not required; the pin plus a
  presence gate converts the citation from decoration into a checkable claim.
- **Cross-reference:** Section 22.2 anchor (b); F-OP32H-01; register item (11)
  F-K3B-07 "trust-root identity not externally anchored."

**F-OP32H-03** HIGH -- the FROZEN status change, the subject of this version, is
gated by nothing, and the gate that formerly checked status parity went vacuous at
exactly this version.

- **Locus:** `build.py` (0 occurrences of `FROZEN`); `build.py:166`
  (`re.findall(r'v0\.\d+ DRAFT CANDIDATE', body)`); `gate_atoms` at
  `build.py:458` still listing `"DRAFT CANDIDATE"`.
- **Substance:** [2b] existed to bind the status string to the version. Its
  DRAFT-CANDIDATE loop now matches zero body strings, so it emits one check instead
  of three, and no predicate replaced it for FROZEN. PR1 rewrote both body status
  claims to an invented status and the build passed green. The coverage instrument
  at [11] still weights lines by the string `DRAFT CANDIDATE`, which no longer
  describes the document. A gate whose input set empties is indistinguishable from
  a gate that passes, and nothing announced the transition.
- **Disposition:** Add a status gate asserting the body status token is a member of
  a closed set and equals the token in the current entry, and assert that the
  DRAFT-CANDIDATE and FROZEN loops together match at least one string, so an empty
  input set fails rather than passes. Replace the `DRAFT CANDIDATE` atom in
  `gate_atoms` with the live status token.
- **Cross-reference:** F-OP28H-09 (measurement instrument carrying a stale literal),
  same class recurring at the status layer.

**F-OP32H-04** HIGH -- "Amendment carried by the v0.31 round that demonstrates it"
is false in ordering; no seat has carried the amendment.

- **Locus:** `xz_protocol_v0_32.md` Section 25, FB-7b row, final sentence; v0.32
  entry, FB-7b amendment paragraph.
- **Substance:** The Class A/B/C/D taxonomy appears in **exactly one entry: v0.32**.
  It occurs **zero times** in the v0.31 entry. The six carrying seats returned
  CONDITIONAL PASS on v0.31 bytes under a rule that did not contain the taxonomy;
  they were not asked whether any finding was Class A or Class B, and no seat
  assented to the classification. The claim "zero Class A/B findings from six
  carrying seats" is therefore a retroactive classification performed by the
  producer of the findings raised against the producer. A round cannot carry an
  amendment that postdates it.
- **Disposition:** Either (a) restate the FB-7b row to say the amendment is
  producer-authored at v0.32 and **not yet carried**, and leave FB-7b OPEN pending
  a round dispatched under the amended rule with the taxonomy supplied to the seats
  in advance; or (b) dispatch that round now. Option (a) costs one sentence and is
  the honest form of the current state.
- **Cross-reference:** F-OP32H-05; F-OP32H-06; Section 25 freeze precondition.

**F-OP32H-05** HIGH -- Section 22, the normative carry rule and the section the
freeze precondition cites, was never amended.

- **Locus:** `xz_protocol_v0_32.md` Section 22 (4450 chars); Section 25 precondition
  sentence ("and the carry rule of Section 22 has been satisfied").
- **Substance:** Section 22 contains **zero** occurrences of `Class A`, `Class B`,
  `Class C`, `Class D`, `CONDITIONAL PASS`, or `amend`. Its item 7 still reads that
  a carrying-seat HALT "blocks freeze outright ... inherited without weakening."
  The amended rule exists only in the Section 25 register row and the Section 27
  entry. The freeze precondition points at Section 22; a reader of Section 22 alone
  cannot learn the operative carry rule. In a document claiming FROZEN, the
  normative locus and the operative locus state different rules.
- **Disposition:** Amend Section 22 to carry the operative rule, with a dated
  amendment marker on the pattern of 22.1 and 22.2, and cross-reference the entry.
  Do not leave the normative section behind the register.
- **Cross-reference:** F-OP32H-04; Section 22.1 and 22.2, which show the
  established pattern for amending Section 22 in place.

**F-OP32H-06** MEDIUM -- the amendment's safety precondition is satisfied by
construction, not by evidence.

- **Locus:** v0.32 entry, FB-7b amendment sentence; register items (5) and (9).
- **Substance:** Two independent reasons. First, Class B is "concealed defect," and
  register item (9) F-GPT31-06 HIGH NOTED states that "current-entry factual
  semantics remain self-attested after packet-internal seal regeneration" -- that
  is, by the instrument's own disclosure no seat operating on the packet can
  establish a concealed defect. A precondition requiring that no Class B finding
  exist is trivially met when Class B is undetectable from the available evidence.
  Second, the precondition is scoped to findings "from any carrying seat." Both
  adversarial seats returned HALT, and their findings cannot trigger the
  precondition by construction. The condition can only be falsified by the seats
  that already declined to falsify it.
- **Disposition:** Scope the precondition to findings from **any seat**, adversarial
  included, and state explicitly that Class B is not decidable from inside the
  packet, so that "no Class B finding" is recorded as a limitation rather than as a
  clearance.
- **Cross-reference:** register item (9); Section 22.2 residual blind spot;
  F-OP32H-04.

**F-OP32H-07** MEDIUM (NOVEL) -- the round's designated headline number is
producer-writable.

- **Locus:** `build.py:364-371` ([9c] tag counting); v0.32 entry tag population.
- **Substance:** S-2 and D-3.2 both designate the ASSERTED fraction as the round's
  headline number in preference to the finding count. [9c] computes it by counting
  `[COMPUTED:`, `[EXTERNAL:`, and `[ASSERTED` string occurrences in the current
  entry. PR2 relabelled four tags and moved the number from 90.9% to 72.7% while
  changing no fact and no gate. A metric intended to measure how much of an entry is
  unverified is itself unverified, and moves in the favourable direction under pure
  relabelling. This is the F-OP28H-02 lexical-binding class arriving at the metric
  layer rather than the claim layer.
- **Disposition:** Compute the fraction from evidence rather than from tags: have
  `check()` emit a machine-readable record per assertion, require every COMPUTED and
  EXTERNAL tag to resolve to one, and derive the fraction from resolved records. An
  unresolvable tag counts as ASSERTED regardless of its label.
- **Cross-reference:** F-OP28H-02; register item (1) F-GLM31-01, which states the
  same mechanism for COMPUTED tags but does not extend it to the metric.

**F-OP32H-08** MEDIUM -- the F-OP28H-01 repair addresses malformation, not
omission, and the closure is narrower than it reads.

- **Locus:** `build.py` [9f], `declared_markers = re.findall(r'\(\d+\)',
  reg_section)` and `check(reg_total == declared_count, ...)`.
- **Substance:** Both sides of the comparison are derived from the same register
  text. PR3 deleted an entire register item and the gate passed at 12 equals 12.
  PR3b corrupted a severity token while retaining the marker and the gate fired
  correctly. So the predicate is real and non-vacuous but detects only rows that
  fail to parse. The register-completeness class -- a disposition silently dropped
  between rounds -- remains open, which register item (13) F-GLM29-01 independently
  concedes as "register-completeness bypass."
- **Disposition:** Anchor `declared_count` outside the register: carry the prior
  round's raised-finding count into the entry as an explicit declared total and
  assert the parsed count equals it. A count derived from the text it validates
  cannot detect deletion from that text.
- **Cross-reference:** F-OP28H-01 (original finding); register item (13); D-6 "Do
  not treat a CLOSED as closed."

**F-OP32H-09** MEDIUM -- COMPUTED reached zero at the freeze, and the ASSERTED
fraction has been flat for three rounds.

- **Locus:** v0.32 entry tag population; build [9c] output.
- **Substance:** COMPUTED 3, 4, 1, 2, 0 across v0.28 through v0.32; ASSERTED
  fraction 80.0, 73.3, 91.7, 91.3, 90.9. The freeze candidate's amendment entry
  contains not one claim any shipped gate would fail on. Corrected for F-OP32H-01
  and -02 the fraction is 100%. There is a defensible reading -- after repeated
  findings against false COMPUTED tags, the producer stopped writing COMPUTED tags
  rather than stopped writing unverified claims. That is an improvement in
  labelling accuracy and a regression in verification coverage, and the entry
  presents only the first half.
- **Disposition:** Before freeze, move at least one load-bearing claim into
  COMPUTED with a gate verified by mutation in the same cycle, and state the
  COMPUTED trajectory alongside the ASSERTED fraction so that a fall to zero is
  visible rather than implicit.
- **Cross-reference:** F-OP28H-06 (the boundary did not move at v0.28 either);
  D-7 question 3.

**F-OP32H-10** MEDIUM -- an open HIGH is absent from the freeze version's own
standing-boundaries list.

- **Locus:** v0.32 entry, "Disclosed standing boundaries" list (13 items); v0.29
  entry, register item (3).
- **Substance:** The v0.29 entry dispositions "F-OP28G-02 / F-OP28H-04 HIGH NOTED:
  test vacuity and count-gate substring containment. Structural limitations." That
  item is HIGH, NOTED, and open. The v0.32 standing-boundaries list enumerates
  thirteen items and does not include it. PR4 confirms the defect is live: the body
  can claim "1860 test functions" and the build passes green. A FROZEN version's
  boundary disclosure is the artifact a downstream reader will rely on, and it omits
  an open HIGH that the corpus records.
- **Disposition:** Add "count-gate substring containment" and "suite-level test
  vacuity" to the standing-boundaries list, or close them. Omission at the freeze is
  the worst moment for this class of gap.
- **Cross-reference:** F-OP28H-04; v0.29 register item (3); S-4 disclosure-scope
  discipline.

**F-OP32H-11** LOW -- Section 25 carries unfilled residual UNKNOWNs directly beneath
a precondition requiring every field be filled, and calls the document a draft.

- **Locus:** Section 25, precondition sentence and the "Additional residual
  UNKNOWNs at this draft" paragraph.
- **Substance:** The register states that the protocol "may be issued as FROZEN only
  when every field below is filled." The paragraph immediately below lists custodian
  identity, universe cardinality, per-stratum counts, reference-standard ledger
  cardinality, overlay parameter values, annotator and adjudicator identities, and
  analysis software versions as unfilled "assuming no favorable default." If these
  are fields, the precondition is unmet. If they are not, the register should say so
  in terms. The phrase "at this draft" also survives into a version claiming FROZEN.
- **Disposition:** State explicitly whether the residual UNKNOWNs are freeze
  blockers. If they are not, add one sentence scoping the precondition to the FB
  rows. Replace "at this draft" with the version token.
- **Cross-reference:** F-OP32H-04; Section 25 FB-7b row.

**Hedge and deferral audit (D-3.3 / S-4).** Corrections (q), (r), and (s) are the
strongest artifacts in the packet and I checked each for reason-truth and scope.
(q) refuses the producer's own prior "gate-closed" claim as overwide and names two
residual gaps -- correct, and the reason is true. (r) concedes that "Normative
manifest digest" names a value computed over 12 files, not 14 -- correct; I
verified the computation covers `sorted(ALL_CODE_FILES)`, 12 members. (s) concedes
that a shipped instrument document contains a false statement about its own digest
coverage -- correct, and I confirm the D0-D7 file is byte-identical to its v0.28
copy, so the false statement is disclosed but unrepaired across at least four
versions. Two scope failures, both raised above: the standing-boundaries list omits
an open HIGH (F-OP32H-10), and the EXTERNAL tags contradict the document's own
Section 22.2 definition (F-OP32H-01).

---

## D. BOUNDARY REPORT

**At v0.28 I located the boundary at claim-to-evidence binding. At v0.32 the
boundary is the external anchor, and the anchor has been named rather than
installed.**

The trajectory is consistent. Each version brings a layer inside the tooling, and
the defect relocates to the first layer outside. v0.32 does something genuinely new:
Section 22.2 states, precisely and without hedging, that a party controlling the
text, code, trust roots, manifest, and seal file can produce a packet passing every
check with rc=0, and that only externally held bytes distinguish forgery from
authenticity. That is an exact description of what my v0.28 probe P5 demonstrated,
written by the producer, in the normative body. It names the three anchor classes
that would close the gap.

And then the entry cites two anchors, neither of which is installed. Tag 1 is
producer-held custody with producer-computed digests, which Section 22.2's own
anchor (a) excludes by the word "independently." Tag 2 is an admissible anchor class
cited without the artifact that makes it operative: no pinned digest, no gate, no
statement of which bytes should match. The document has advanced from not knowing
what would close the gap to knowing exactly what would close it and labelling the
gap closed.

That is the current boundary, and it is a specific and narrow one. **The instrument
now computes everything internal and nothing external, and the label EXTERNAL is
applied by the same process that writes the claims.**

**What would bring it inside, concretely.** Three changes, none large. First, pin
the sha256 of each cited Zenodo deposit adjacent to its DOI and gate on the pin's
presence and well-formedness. Second, have one carrying seat publish its own report
digest where the producer cannot edit it, and cite that publication rather than the
producer's copy -- one seat, one line, and anchor (a) becomes real. Third, have
`check()` emit evidence records and require every COMPUTED and EXTERNAL tag to
resolve to one, which closes F-OP32H-07 and makes the headline number a
measurement.

**What it will not fix.** The patient-contributor adversary remains untested, as it
has in every round on record. Nothing here changes that, and Section 22.2 says so.

**Is the FROZEN claim earned?** No, and the reasons are structural rather than
byte-level. The document's own freeze precondition is that every FREEZE-BLOCKER
field be filled and that the Section 22 carry rule be satisfied. The FB-7b field is
filled by an amendment that (i) no seat has carried, because the taxonomy it
depends on appears only in v0.32 and zero times in the v0.31 entry, (ii) is
evaluated under a precondition that the seats most likely to trigger it are excluded
from triggering, and (iii) is not present in Section 22, the section the precondition
cites. The freeze's headline novelty, EXTERNAL above zero, is two labels over
unverifiable state. And the status word itself is gated by nothing: I changed it to
an invented string and the build passed.

**What the round got right, stated before the ledger because it is the actual
delta.** The append-only discipline held: 28 of 28 historical entry seals are
byte-identical to the copies I have held since v0.28, verified against bytes the
producer could not reach. Section 22.2 is an honest and precise statement of the
forgery boundary and it names the right anchors. Correction (q) rejects the
producer's own overwide closure claim. Correction (r) concedes a naming defect that
no seat would have been harmed by. Correction (s) concedes that a shipped instrument
document contains a false statement. The `[9f]` predicate I found missing at v0.28
now exists and fires correctly on malformed rows. The FB-7b register row states
outright that the amendment is "carried by the v0.31 round that demonstrates it" --
circular, and I count it as a HIGH, but it is stated in the open rather than
concealed, and the concealment is what S-9 says to grade. Zero COMPUTED tags means
zero false COMPUTED tags; the class that produced my sharpest v0.28 finding cannot
recur in this entry.

This is not a dishonest packet. It is an honest packet making a claim its own
machinery does not support.

---

## E. D-7 REFLEXIVE CHECK

**Did every probe come from an enumerated list?** No, but the risk was live and I
declared it before executing. PR1 and PR2 are new classes targeting surfaces that
did not exist before this version. PR3, PR4, and PR5 are deliberate re-runs of my
own v0.28 findings, and their purpose was verification in the bytes, not discovery
-- PR3 and PR3b changed my assessment of a repair I would otherwise have recorded as
clean.

**Did the dispatch tell me where to look?** Yes, substantially, and I flag it. The
cover note named the five attack surfaces: status change, FB-7b amendment, EXTERNAL
citations, register dispositions, standing boundaries. Four of my five HIGH findings
sit on those surfaces. This is leakage in the D-7 sense: a seat told where to look
will find things there. What was not supplied was the cross-version seal comparison,
which is the one result no dispatch could have predetermined because it depends on
bytes I happen to hold.

**Is the ASSERTED fraction unchanged from the prior round?** **Yes, for the third
consecutive round.** 91.7, 91.3, 90.9. COMPUTED fell 1, 2, 0. The freeze is being
declared at the point where the entry's verified fraction reached zero. See
F-OP32H-09.

**Have the recent rounds all been producer-family?** No, and this is a genuine and
significant improvement. The v0.31 round fielded six non-producer carrying seats
across two families plus two adversarial seats. The apparatus is no longer measuring
only itself. **This seat, however, is producer-family and advisory, and this report
discharges nothing.**

---

## VERDICT

**HALT -- ADVISORY ONLY.** I am a producer-family advisory seat. **This verdict does
not bind. It carries no carry vote and no FB-7b weight. It freezes nothing and
blocks nothing.** It is recorded and forwarded. Any record describing this as a
binding HALT misdescribes it.

Severity ledger: 0 CRITICAL / 5 HIGH / 5 MEDIUM / 1 LOW.

**The FROZEN claim is not earned.** Blocking findings and what clears each:

- **F-OP32H-01** -- clears when the seat-report anchor is retagged ASSERTED, or when
  a carrying seat publishes its own digest outside producer control and the entry
  cites that.
- **F-OP32H-02** -- clears when each cited DOI carries a pinned sha256 and a gate
  fails on its absence; verified when PR2's DOI mutation turns the build red.
- **F-OP32H-03** -- clears when a status gate exists and PR1 turns red.
- **F-OP32H-04** -- clears when the FB-7b row states the amendment is not yet
  carried, or when a round is dispatched under the amended rule with the taxonomy
  supplied to seats in advance.
- **F-OP32H-05** -- clears when Section 22 carries the operative rule in its own
  text.

Each is verified by re-running the probe that found it, not by inspection.

**Recommendation.** F-OP32H-01 and -04 are one sentence each and are the honest
form of the current state; they cost nothing but the word FROZEN. F-OP32H-02, -03,
and -05 are small mechanical changes. If the project lead wants a defensible freeze
rather than a fast one, the shortest honest path is: retag the two EXTERNAL claims,
state that the amendment is producer-authored and uncarried, amend Section 22 in
place, add the status gate and the DOI pins, then dispatch one round under the
amended rule to seats who are told the taxonomy in advance. That round -- not this
one -- is the one that can carry a freeze.

*Author of the instrument under audit: Bilal Syed Arfeen. This report is a seat
deliverable and ships unmodified.*

---

# Bismillah ir-Rahman ir-Rahim
