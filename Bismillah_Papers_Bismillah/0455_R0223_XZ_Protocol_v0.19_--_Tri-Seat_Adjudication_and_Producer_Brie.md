# Bismillah ir-Rahman ir-Rahim

# R0223 -- XZ Protocol v0.19 -- Tri-Seat Adjudication and Producer Brief

**Chronological Index:** 455 of 995  
**Date:** 2026-08-02  
**Section:** IV. XZ Protocol  
**Source File:** XZ_v19_ADJUDICATION.md  
**Source Format:** md  
**SHA-256:** `06a5183899a43539ca4f254f99f0f82cbf6f15d4b5b6405b2aa0ba7c4b28bcf1`  

---

## R0223 · XZ Protocol v0.19 -- Tri-Seat Adjudication and Producer Brief

- section: IV. XZ Protocol
- source_file: XZ_v19_ADJUDICATION.md
- source_format: md
- text_sha256: 06a5183899a43539ca4f254f99f0f82cbf6f15d4b5b6405b2aa0ba7c4b28bcf1

# XZ Protocol v0.19 -- Tri-Seat Adjudication and Producer Brief

**Prepared for:** Claude Opus 4.6, producer of record for v0.20.
**Adjudicator:** Claude Opus 5 (Anthropic), Seat A, producer-family.
**Date:** 2026-08-02.

## 0. Standing, method, and bias controls

**Adjudicator standing.** Producer-family. Under the producer-instance
exclusion my own findings enter this record as **advisory only: they cannot
HALT and cannot carry CRITICAL or HIGH in the adjudicated set.** Where my
severity differs from a non-producer seat's, theirs governs. I hold the v0.17,
v0.18 and v0.19 Seat A packets, which is what makes the execution triage below
possible.

**Bias controls, declared before clustering.**

1. I scored the seats' findings against mine before clustering. **Two of my own
   v0.19 claims are refuted by them and are recorded as refuted in Section 4.**
2. No contradiction is resolved toward my prior position.
3. A seat agreeing with me adds no weight beyond its own; a seat refuting me is
   recorded at full strength.

**Weighting.** GPT-5.6 Sol self-disqualified from carrying at v0.6, so its
findings enter as an adversarial record with full unique-finding weight and
**no carry vote**. Kimi K3 and GLM-5.2 are the designated carrying pool; the
methodology's tier table predates both, so I have treated each at consensus
weight 1.0. **That assignment is the project lead's to ratify, not mine.**
Consensus threshold is 2.0.

---

## 1. Execution triage

This is the check no seat can perform on itself. Every claimed value below was
re-derived against the Seat A packet bytes.

| Seat | Execution | Evidence verified by this adjudicator |
|---|---|---|
| **GPT-5.6 Sol** | **CONFIRMED EXECUTING** | Shipped a 15-file evidence tree. Its `baseline_sha256.txt` reproduces all 14 normative digests exactly. Return codes are real files (`0`,`1`), and the captured build output carries verbatim gate strings that match the shipped `build.py` (`FAIL: HISTORY seal ENTRY_v0.19 matches bytes`, `FAIL: S22 item 6: gate is convenience`). Probe outputs terminate in `BUILD PASSED: all checks GREEN` with rc=0. |
| **GLM-5.2** | **CONFIRMED EXECUTING, substrate-anchored** | Reported a challenge value of `166c2cae1491279ab83110236205800ba1d35d506dc58cd92974ebeb87959cf4` for the trust-roots JSON. **It reproduces exactly under `json.dumps(d, sort_keys=True)`** and appears nowhere in any dispatch. Seven verbatim gate strings (V1 to V7) all match `build.py`'s literal format, including `FAIL: Expected 1 line-starting '## 27.' heading, found 2`, which is a string only reachable by running `get_body()`. |
| **Kimi K3** | **CONFIRMED EXECUTING** | Probe P2's verbatim output, `FAIL: FB-4 row contains xz_protocol_source_frame.py digest (82d1066a76df4f60...)`, is byte-identical to this adjudicator's independent T2 probe on the same bytes. P1's three-failure signature on a one-character kernel edit matches. Reported one VOID sub-probe and one own-harness error rather than suppressing them. |

**All three seats executed.** That is the first round in this program's record
where every dispatched seat ran the code. It is worth stating plainly, because
six consecutive earlier rounds turned on one seat executing and another not.

**Method quality.** GLM and Kimi both froze S-1 preregistrations before opening
the amendment entry and scored them. GPT **did not**, and says so explicitly
rather than backfilling one. Kimi and GPT both voided non-landing probes.
Kimi's P3 records a first attempt that failed because the forgery was
incomplete, then the completed forgery. This is the strongest method discipline
the corpus has seen.

---

## 2. The headline: the three seats did not audit the same bytes

No seat raised this, because each could only see its own packet. It falls out
of comparing them.

| Packet | Members | `HISTORY.sha256` | Advisory reports | Discipline blocks |
|---|---|---|---|---|
| Seat A (adjudicator) | 33 | **present** | 4 | 3 |
| GLM (`DISPATCH_v19_CARRY_1`) | 28 | **present** | none | 2 + seat instructions |
| Kimi (`DISPATCH_v19_CARRY_2`) | 15 | **ABSENT** | none | 3 (held separately) |

Consequences, each verified by execution:

- **Kimi's F-K3-19-03 clause (c)** -- "`HISTORY.sha256` does not ship, so `[9b]`
  never executes at all" -- is **true of Kimi's packet and false of the other
  two**. Clauses (a) and (b) of that finding hold universally.
- **Kimi's probe P4** -- falsifying the v0.18 verdict inside Section 27 and
  getting rc=0 -- is **packet-conditional**. Reproduced on the Seat A packet
  with the seal file present: **rc=1, 4 fail-checks**, firing
  `FAIL: HISTORY seal ENTRY_v0.18 matches bytes` and
  `FAIL: FULL_SECTION_27 seal matches`. With the seal file removed from the
  same tree: **rc=0, zero fail-checks.**
- The three seats' packet-coverage counts (16 of 33, 14 of 28, 14 of 15) are
  **not a disagreement**. They are three correct measurements of three
  different substrates.

**This is a substrate-correction item and it precedes everything else.** A
two-family carry over non-identical bytes does not mean what the protocol says
it means. Section 22's FB-7b requires two executing non-producer seats *on
canonical bytes*; that condition was not met this round regardless of the
verdicts.

---

## 3. Adjudicated findings

### Consensus findings (weight >= 2.0)

**F-ADJ19-01 HIGH [consensus; weight 3.0]** -- `PRIOR_HISTORY` is decorative and
F-OP18-05 is CLOSED on a control that does not exist

- **Locus:** `xz_protocol_v0_19.md:869` register item (5);
  `build.py:254-257`.
- **Substance:** the entry closes F-OP18-05 and tags it
  `[COMPUTED: build.py [9b] PRIOR_HISTORY check, once implemented]`. The
  branch collects lines beginning `PRIOR_HISTORY` and executes `print(...)`;
  it contains no `check()` call and compares no value. A CLOSED whose own tag
  says "once implemented" is a closure claim on a future artifact.
- **Disposition:** downgrade to DISCLOSED, NOT CLOSED, **or** implement a
  `check()` that fails on a wrong or absent `PRIOR_HISTORY` value. Ship the
  prior `HISTORY.sha256` or embed its digest in a machine-checked field.
- **Cross-reference:** GPT F-GPT19-01 (HIGH), GLM F-GLM52-v19-01 (HIGH), Kimi
  F-K3-19-03 (HIGH, blocking), adjudicator F-OP19-04 (MEDIUM).
- **Severity note:** three non-producer seats independently graded HIGH; the
  adjudicator's MEDIUM is the outlier and is **conceded**. Their grading is
  better: the defect sits on a CLOSED disposition, not on a decorative line.
- **Independent confirmation:** the value `cb67f222...` is *correct* -- it is
  the sha256 of the v0.18 `HISTORY.sha256`, verified against the packet this
  adjudicator holds. The datum is right; the control is absent.

**F-ADJ19-02 HIGH [consensus; weight 3.0]** -- the provenance ledger is
unimplemented, incomplete, and its one EXTERNAL tag is invalid on three
independent grounds

- **Locus:** `xz_protocol_v0_19.md:865` (the EXTERNAL tag), `:871` register
  item (11); `build.py` section `[11]`.
- **Substance:** `[11]` prints character counts; it does not parse, count or
  validate tags, so the claim that the ledger "is implemented in this entry
  [COMPUTED: build.py [11]]" is false. Multiple claims carry no tag. The single
  EXTERNAL tag fails for three separate reasons found by three separate seats:
  the cited report carries no digest in any shipped text (GPT); it is
  producer-family and therefore not "state the producer does not control"
  (GLM); and the cited locus, Rev B Section 10, states `0/3/6/4` while the
  claim attributes `0/3/4/3` (adjudicator, verified at line 446 of the shipped
  report). The three grounds compound rather than compete.
- **Disposition:** retag ASSERTED. Have the build parse every `[COMPUTED: ...]`
  tag, extract the section it names, assert that section exists in `build.py`,
  and fail otherwise; assert every EXTERNAL tag names a shipping file with a
  matching digest; print the ASSERTED fraction as a build output.
- **Cross-reference:** GPT F-GPT19-02 (HIGH), Kimi F-K3-19-04 (MEDIUM), GLM
  F-GLM52-v19-02 (MEDIUM), adjudicator F-OP19-02 (HIGH) and F-OP19-06
  (MEDIUM). Severity-debated; lower bound MEDIUM per GLM and Kimi.

**F-ADJ19-03 HIGH [consensus; weight 3.0]** -- the entry asserts the recurrence
ordinal it twice disclaims

- **Locus:** `xz_protocol_v0_19.md:865` ("The twelfth Axiom-3 recurrence...")
  against `:869` item (3) ("this entry does not assert one") and item (6)
  ("This entry does not assert an ordinal").
- **Substance:** all three strings verified verbatim. The v2 discipline blocks
  shipping in the same packet instruct that no ordinal be narrated until a
  recurrence table exists; no such table ships. The entry therefore contradicts
  itself, its own disposition of F-OPUS5-17-06, and the methodology it claims
  to have integrated.
- **Disposition:** strike the ordinal, or ship a tool-maintained recurrence
  table and derive it. Reconcile the opening sentence with items (3) and (6).
- **Cross-reference:** Kimi F-K3-19-02 (HIGH, blocking), GLM F-GLM52-v19-04
  (MEDIUM), GPT F-GPT19-03 (MEDIUM). Severity-debated; lower bound MEDIUM.
  **Adjudicator missed this and asserted the opposite -- see Section 4.**

**F-ADJ19-04 HIGH [consensus; weight 2.0]** -- F-OP18-09 is raised in the
entry's own range statement and dispositioned nowhere

- **Locus:** `xz_protocol_v0_19.md:865` ("Rev A: F-OP18-01 through F-OP18-10")
  against the disposition block at `:869`.
- **Substance:** `grep` across the protocol returns `F-OP18-01` through `-08`
  and `-10` through `-13`. `F-OP18-09` occurs zero times anywhere in the
  packet. D-3.7 requires that a raised finding may be closed, disclosed or
  noted, but not absent. For the record, F-OP18-09 is the em-dash convention
  finding in the Rev B report, and it is the same item that was dropped from
  the v0.18 register as F-OP17-09 -- **the same finding has now been dropped
  in two consecutive rounds.**
- **Disposition:** disposition F-OP18-09 explicitly, or record it withdrawn
  with reason. Add a build check extracting finding IDs from each named report
  and asserting each occurs in the entry.
- **Cross-reference:** Kimi F-K3-19-01 (HIGH, blocking), GLM F-GLM52-v19-03
  (MEDIUM). Severity-debated; lower bound MEDIUM. **Adjudicator missed this and
  asserted the opposite -- see Section 4.**

### Vendor-unique findings (below consensus threshold; lead disposes)

**F-ADJ19-05 HIGH-tentative [vendor-unique to Kimi K3; independently confirmed
by adjudicator execution]** -- the seal gate silently no-ops when its subject is
absent

- **Locus:** `build.py:224`, `if os.path.exists("HISTORY.sha256"):` with no
  else-branch failure.
- **Substance:** a packet shipped without `HISTORY.sha256` skips `[9b]`
  entirely and the build returns green. Confirmed by execution on the Seat A
  tree: with the seal file present a Section 27 mutation fails at rc=1 with
  four fail-checks; **with the same tree and the seal file deleted, rc=0 and
  zero fail-checks.** A gate that passes when its subject is missing converts
  a missing control into a green checkmark, and it is the mechanism by which
  Kimi's packet produced a false-clean history layer.
- **Disposition:** fail the build when `HISTORY.sha256` is absent. One
  `check()`. **I recommend the lead promote this to consensus HIGH** despite
  its single-seat origin: it is the only finding this round whose exploitation
  requires no forgery at all, merely an omission during packet assembly, and
  that omission has already occurred once.
- **Cross-reference:** Kimi F-K3-19-06 (MEDIUM, structural); Section 2 above.

**F-ADJ19-06 INFORMATIONAL, highest structural significance [vendor-unique to
Kimi K3]** -- the full gate suite is blind to self-consistent forgery

- **Locus:** the verification surface as a whole.
- **Substance:** Kimi mutated kernel bytes, recomputed the manifest digest,
  re-sealed the trust roots and updated the body citations, and the build
  returned `BUILD PASSED, rc=0`. The packet's verification surface proves
  internal agreement, not correspondence with anything outside it. The only
  anchors outside the producer's control are the seat-held dispatch manifest
  and external receipts -- and the producer authors the dispatch.
- **Disposition:** none available inside the packet; this is a boundary
  statement and belongs in the protocol's disclosed limitations, not in a fix
  queue. It should be written into Section 22 as a stated limit of the
  verification model before any FROZEN claim.
- **Cross-reference:** Kimi F-K3-19-10; the adversary-rotation clause D-4,
  under which Kimi declared *self-consistent forger* and delivered the first
  executed instance in the corpus.

**F-ADJ19-07 LOW [vendor-unique to Kimi K3; substance confirmed, figure
unresolved]** -- `build.py [11]` labels the entire body "gated"

- **Locus:** `build.py` section `[11]` output line `Body (gated): 96482 chars
  (70.4%)`.
- **Substance:** the body-versus-Section-27 partition is real, but almost none
  of the body is read by any gate. Kimi measured 3.3% of the document on lines
  carrying a gated atom. This adjudicator's independent remeasure, using a
  broader atom set, returned **10.5%**. The two figures differ by method and
  Kimi's atom list does not ship, so the specific number is **not
  reproduced**; the direction is confirmed decisively either way, since both
  are far below 70.4%. The mislabelled figure is the one the F-OP18-12
  disposition cites as evidence.
- **Disposition:** rename the output to `Body (in-scope for gates)` and add a
  separate measured `semantic-gate coverage` line with the atom list printed,
  so the figure is reproducible.
- **Cross-reference:** Kimi F-K3-19-07; adjudicator F-OP19 coverage section.

**F-ADJ19-08 MEDIUM [vendor-unique to Kimi K3; corroborated by adjudicator]** --
items (1) and (4) make irreconcilable report-attribution claims

- **Locus:** `xz_protocol_v0_19.md:869`, items (1) and (4).
- **Substance:** item (1) states that only the Perplexity-labelled report
  returned HALT; item (4) states the Perplexity-labelled file was
  byte-identical to the Claude Opus 5 output and that the entry does not
  re-assert routing it cannot verify. Kimi's formulation is sharper than the
  adjudicator's and is adopted: **byte-identical files cannot carry divergent
  verdicts.** The two v0.17 reports are `eab568a7...` (HALT) and `f7841692...`
  (CONDITIONAL PASS); those digests are not in dispute and the labels are.
- **Disposition:** restate item (1) by digest and drop route names entirely.
  Adopt digests as the primary identifier for seat reports.
- **Cross-reference:** Kimi F-K3-19-05 (MEDIUM), adjudicator F-OP19-03
  (MEDIUM).

**F-ADJ19-09 LOW [vendor-unique to Kimi K3; confirmed]** -- Section 22 item 1
cites "the shipped prohibited-content verifier", which does not ship

- **Locus:** `xz_protocol_v0_19.md:693`.
- **Substance:** verified. The named file
  `xz_protocol_prohibited_content_verifier.py` is absent from the packet, a
  consequence of the v0.14 tooling partition. The word "shipped" is the defect.
- **Disposition:** change to the future or conditional form used elsewhere for
  partitioned tooling, or ship the verifier.
- **Cross-reference:** Kimi F-K3-19-08; F-XZ12-OP-07.

**F-ADJ19-10 LOW [vendor-unique to GLM-5.2; confirmed]** -- "five defects found
in the discipline blocks themselves" carry no IDs and no dispositions

- **Locus:** `xz_protocol_v0_19.md:865`.
- **Substance:** verified verbatim. Five defects are asserted as absorbed with
  no identifiers, so nothing tracks whether any of them landed.
- **Disposition:** assign IDs in a namespace and disposition each, or drop the
  claim.
- **Cross-reference:** GLM F-GLM52-v19-05.

**F-ADJ19-11 MEDIUM [adjudicator-originated; no seat could see it]** -- the
three seats were dispatched materially different packets

- **Locus:** packet composition across `DISPATCH_v19_SEAT_A`,
  `DISPATCH_v19_CARRY_1`, `DISPATCH_v19_CARRY_2`.
- **Substance:** 33, 28 and 15 members respectively; `HISTORY.sha256` present
  in two and absent in the third; advisory reports present in one and absent
  in two. Kimi's F-K3-19-03(c) and probe P4 are artifacts of that divergence
  rather than properties of the instrument, and no seat could have known.
- **Disposition:** emit one canonical packet, hash it, and ship the same member
  set to every seat with `PACKET_SHA256SUMS`; state role-appropriate
  *instructions* in a per-seat cover note rather than by varying the payload.
  Re-run the two carrying seats on identical bytes before any FB-7b claim.
- **Cross-reference:** F-ADJ19-05; D-0 leakage matrix; Section 22 FB-7b.

**F-ADJ19-12 LOW [vendor-unique to Kimi K3; process]** -- the dispatch violated
its own D-0 and D-5

- **Locus:** the carrying dispatches, which print `Expected: 186 passed, rc=0`;
  the absence of any sealed nonce.
- **Substance:** D-0 withholds expected values from carrying seats precisely so
  that a matching value evidences execution; printing them makes the count
  non-probative, and no nonce ships, so D-5's challenge is unsatisfiable as
  written. Kimi worked around it by reporting values printed nowhere. **This is
  a defect in the dispatch design, which this adjudicator authored**, not in
  the producer's work.
- **Disposition:** issue a per-seat sealed nonce from the lead, withhold
  expected counts and digests from carrying dispatches, and keep the true nonce
  value out of the producer's hands.
- **Cross-reference:** Kimi S-0 dispatch-deviation note; D-0; D-5; F-OP19-08.

### Contradictions

**None on severity.** No cluster shows a two-band disagreement, so no
severity-driven escalation applies. Every divergence is one band, and each is
resolved upward with the lower bound recorded.

**One on substrate,** which is more serious than a severity split and is
escalated in Section 7: Kimi reports `HISTORY.sha256` absent while GLM and this
adjudicator verify it present and all 20 seals reproducing. Resolved as packet
divergence, not seat error. **No seat is at fault.**

---

## 4. Refutations of the adjudicator's own report

Record-over-person applies to me. Two claims in
`XZ_v19_SEAT_A_REPORT.md` are false and are withdrawn.

1. **"The entry asserts no recurrence ordinal"** (Section S-8, line 437).
   **REFUTED** by GPT F-GPT19-03, GLM F-GLM52-v19-04 and Kimi F-K3-19-02, and
   confirmed by my own re-extraction: line 865 reads "The twelfth Axiom-3
   recurrence...". I credited the producer with a discipline it did not
   exercise, in the same paragraph where I was listing what the round got
   right. That is the failure mode of a favourable summary written from a
   self-model rather than from a grep.
2. **"All thirteen findings from both revisions are dispositioned --
   finding-accounting is complete for the first time"** (same paragraph).
   **REFUTED** by Kimi F-K3-19-01 and GLM F-GLM52-v19-03. F-OP18-09 is absent.
   Twelve of thirteen were dispositioned.

Both errors are in the *positive* half of my report. Three seats checked what I
praised; none of them found an error in what I criticised. That asymmetry is
worth recording as a corpus datum: **an auditor's commendations are less
checked than its findings, by the auditor and by everyone downstream.**

A third correction: my packet-coverage figure of 14 hashed and 19 unhashed was
wrong. GPT's 16 and 17 is correct on the Seat A packet, reproduced here. My
count scanned only the dispatch and the protocol text and missed digests
recorded inside the advisory reports.

---

## 5. Novel defect classes contributed (D-4 harvest)

Appended to the program class register. All are new to the corpus.

| Class | Source | Executed |
|---|---|---|
| Presence-only field spoof: a control value that is read but never compared | GPT P1, GLM Probe A, Kimi F-K3-19-03 | yes, three independent instances |
| Provenance-tag spoof: rewriting a claim's own COMPUTED/ASSERTED tag | GPT P2, adjudicator T6b | yes, two independent instances |
| Wholesale self-consistent forgery across every internal surface | Kimi P3 (N1) | yes |
| Seal-absent narrative mutation, and gate-silence-on-absence | Kimi P4 (N2), adjudicator confirmation | yes |
| Packet-member deletion | adjudicator T7 | yes |
| Cited-artifact tamper where the digest is in prose only | adjudicator T4 | yes |

The quota worked. Every seat contributed at least one class not on any
enumerated list, and the two most significant results of the round -- Kimi's
self-consistent forgery and the seal-silence chain -- came from outside every
checklist in circulation.

---

## 6. Boundary and headline number

All four seats independently located the same boundary: **the factual content
of Section 27 amendment entries.** GLM's and Kimi's preregistered boundary
predictions both HELD; Kimi's defect prediction HELD; mine HELD on the class
and was REFUTED on the sub-prediction that the packet manifest would land.

GLM computed the round's headline number: **ASSERTED fraction 14 of 25 claims,
56.0%**, with two producer self-tags wrong. That figure should be carried
forward as the tracked series. Note it is not comparable to a v0.18 baseline
because no such measurement was taken then; v0.19 is the first data point.

Document coverage is agreed by all three executing seats at 137,056 characters
total, 96,482 body, 40,574 Section 27, 29.6% ungated -- **up from 26.2% at
v0.18.** Four gates were added inside the boundary; the boundary did not move.

---

## 7. Adjudicated verdict

> **HALT-AND-ESCALATE**, then **HALT-AND-RETURN-TO-PRODUCER**.
>
> **Escalation first (project lead):** the three seats audited three different
> packets. FB-7b requires two executing non-producer seats on canonical bytes.
> That condition was not met, so the divergence between Kimi's HALT and GLM's
> CONDITIONAL PASS **cannot be read as a two-family divergence** and must not
> be recorded as one. Substrate correction precedes any carry accounting.
>
> **Then producer return:** four consensus HIGH findings.
>
> Adjudicated ledger: **0 CRITICAL / 4 HIGH consensus / 1 HIGH-tentative
> vendor-unique / 2 MEDIUM vendor-unique / 3 LOW vendor-unique / 1
> INFORMATIONAL boundary.**
>
> Seat verdicts as returned: Kimi K3 **HALT** (binding, blocks freeze);
> GLM-5.2 **CONDITIONAL PASS** (non-HALT, not carry-clean); GPT-5.6 Sol
> **HALT** (adversarial record, no carry vote); Seat A **HALT** (advisory, no
> carry vote).

**What the round got right, before the queue.** All three dispatched seats
executed -- a first. The code plane is byte-clean for a second consecutive
round: 14 of 14 digests, 186 tests, every COMPUTED-tagged gate that exists
fires under mutation across three independent seats' probes. The FB-row locus
assertion, seal surjectivity, entry ordering and `get_body()` fixes all landed
and all discriminate. The producer honestly tagged its weakest claim ASSERTED,
disclosed the packet-manifest gap, and corrected the v0.18 verdict
mischaracterization by append-only narration while leaving the v0.18 entry text
intact. Three of four consensus HIGHs are single-sentence corrections.

**Why it is still a HALT.** All four consensus findings sit in the amendment
entry, and three of them are the entry making false statements about its own
verification apparatus: a CLOSED on an unimplemented control, a COMPUTED tag on
a gate that does not read tags, and an ordinal asserted in the same entry that
twice disclaims it. The round's own thesis is that this region is where the
defect lives, and the round proved it.

---

## 8. Producer brief for Opus 4.6

Ordered by cost. Each item ships with the falsification test **written before
the fix**, per O-5, so the check is inherited rather than composed afterward by
the context that would make the error.

**Governance flag, stated inside the artifact per the standing rule.** This
brief is written by a producer-family seat that also audited v0.17, v0.18 and
v0.19 and authored the discipline blocks. That is audits-plus-writes-fix. It
should reach you as a **proposal, not an instruction**, and no item in it
resolves a contradiction -- the one substrate contradiction is escalated to the
lead unresolved.

### Block A -- substrate correction (do first; blocks everything else)

**A1.** Emit one canonical v0.20 packet. Hash every member into
`PACKET_SHA256SUMS`, verify it in `build.py`, and ship the identical member set
to every seat. Vary the cover note, never the payload.
*Falsification test, write first:* delete one non-normative member and confirm
the build fails; add one and confirm it fails.

**A2.** Re-dispatch v0.20 to Kimi K3 and GLM-5.2 on identical bytes. Until that
happens, record the v0.19 carry as **NOT ATTEMPTED**, not as divergent.

### Block B -- the four consensus HIGHs (three are sentences)

**B1 (F-ADJ19-03).** Strike "The twelfth Axiom-3 recurrence" from the opening
sentence. Do not replace it with another ordinal.
*Falsification test:* grep the entry for ordinal words adjacent to
"recurrence"; assert zero hits while no recurrence table ships.

**B2 (F-ADJ19-04).** Disposition F-OP18-09 explicitly. It is the em-dash
convention finding, and it was also dropped as F-OP17-09 at v0.18, so state
that it has been dropped twice and resolve it.
*Falsification test:* extract every finding ID from each report named in the
entry; assert each occurs in the entry; fail on any absence.

**B3 (F-ADJ19-01).** Retag F-OP18-05 as DISCLOSED, NOT CLOSED. Separately, add
the real `check()`: require exactly one `PRIOR_HISTORY` line and compare its
value against a shipped prior `HISTORY.sha256`, failing on mismatch or absence.
*Falsification test:* replace the `PRIOR_HISTORY` digest with sixty-four zeros,
reseal, and assert the build fails. This is GPT's P1 and GLM's Probe A; both
currently pass, and both must fail after the fix.

**B4 (F-ADJ19-02).** Retag the EXTERNAL claim as ASSERTED, or ship Rev A with
its digest. Then make tags machine-checked: parse every `[COMPUTED: ...]`,
extract the build section it names, assert that section exists, and fail
otherwise; assert every EXTERNAL tag names a shipping file whose digest
matches; print the ASSERTED fraction.
*Falsification test:* rewrite one tag to name `build.py [12]`, a section that
does not exist, reseal, and assert the build fails. This is GPT's P2 and my
T6b; both currently pass.

### Block C -- the one-line control with the highest ratio

**C1 (F-ADJ19-05).** Fail the build when `HISTORY.sha256` is absent. Replace the
bare `if os.path.exists(...)` with a `check()` on presence.
*Falsification test:* delete `HISTORY.sha256` and assert rc=1. It currently
returns rc=0 with zero fail-checks, which is how one seat received a
false-clean history layer this round.

### Block D -- absorb without blocking

**D1 (F-ADJ19-08).** Restate item (1) by digest; drop route names.
**D2 (F-ADJ19-07).** Rename the coverage output and add a reproducible
semantic-gate line with the atom list printed.
**D3 (F-ADJ19-09).** Fix "the shipped prohibited-content verifier".
**D4 (F-ADJ19-10).** Assign IDs to the five discipline-block defects.
**D5 (F-ADJ19-06).** Write the self-consistent-forgery limit into Section 22 as
a disclosed boundary of the verification model. Do not attempt to gate it.

### Block E -- do not do

Do not add a gate to close the ungated fraction by shrinking the entry. The
entry should get longer as the record grows; the fix is to bring claims inside
the computed region, not to write fewer of them. The 29.6% figure is a
measurement, not a target.

---

## 9. What the project lead must decide

1. **Ratify or revise the weighting.** I treated Kimi and GLM at consensus
   weight 1.0 each. The methodology's tier table does not name them.
2. **Rule on the substrate divergence.** Whether the v0.19 carry is recorded as
   NOT ATTEMPTED, as this adjudication recommends, or otherwise.
3. **Dispose F-ADJ19-05.** Single-seat origin, independently confirmed by
   execution; I recommend promotion to consensus HIGH.
4. **Dispose the vendor-unique set** F-ADJ19-06 through F-ADJ19-12 individually.
   None were auto-rejected.
5. **Decide who writes the v0.20 spec.** If this seat writes it and also audits
   v0.20, that is the same role collapse one storey up. Either I write it and
   another seat audits, or another party writes it and I audit. Not both.
6. **Note the governance state:** four consecutive producer-family advisory
   cycles preceded this round, and this round is the first non-producer contact
   since v0.14. That contact was worth it -- the two findings that refute my own
   report came from the seats, not from me.

---

*Adjudication prepared by Claude Opus 5 (Anthropic), Seat A, producer-family,
under the BayyinahEnterprise cross-vendor adjudication rules. Producer-instance
exclusion applied to this seat's own findings throughout. Every value re-derived
from the shipped bytes by local tool execution; no value typed from memory. The
Seat A tree was re-verified 14 of 14 against the dispatch manifest after all
reproduction work. Raw seat reports ship unmodified:
`report_v19_adversarial_audit.md` (526130a7...),
`GLM5_2_AUDIT_REPORT_v0_19.md` (c111dcda...),
`XZ_v019_CARRY2_AUDIT.md` (Kimi, in `Kimi_Agent_Shared_attachments__11_.zip`,
47e3fa1a...), and the GPT evidence tree (`058c2c9d...`).*

---

# Bismillah ir-Rahman ir-Rahim
