# Bismillah ir-Rahman ir-Rahim

# R0254 -- XZ Protocol v0.74 -- Round 31, Seat S04 Advisory Audit Report

**Chronological Index:** 538 of 995  
**Date:** 2026-08-17  
**Section:** IV. XZ Protocol  
**Source File:** XZ_v074_R31_S04_REPORT.md  
**Source Format:** md  
**SHA-256:** `bd00ec403b0c64a1749d35d843c234dbe039423f7749bfec64a85bc757236ae8`  

---

## R0254 · XZ Protocol v0.74 -- Round 31, Seat S04 Advisory Audit Report

- section: IV. XZ Protocol
- source_file: XZ_v074_R31_S04_REPORT.md
- source_format: md
- text_sha256: bd00ec403b0c64a1749d35d843c234dbe039423f7749bfec64a85bc757236ae8

# XZ Protocol v0.74 -- Round 31, Seat S04 Advisory Audit Report

**Seat:** S04 | **Model:** Claude Opus 5 (Anthropic) | **Role:** ADVISORY, producer-family, non-carrying
**Round:** 31 | **Target:** XZ Protocol v0.74 bytes | **Date:** 2026-08-17
**Namespace:** F-S04-74
**Dispatch:** `DISPATCH.txt` (R31, Seat S04, labelled FRESH -- **see F-S04-74-15, the label is false of this seat**).

---

## 0. Verdict

> **Verdict:** HALT-AND-RETURN-TO-PRODUCER.
>
> **Severity ledger:** 1 CRITICAL / 7 HIGH / 4 MEDIUM / 2 LOW / 1 governance declaration.
> **Class ledger:** 7 Class A, 4 Class B, 1 Class C, 4 Class D (two findings dual-classified).
>
> **Closed from R30:** F-S04-73-01. The gate [2f] repair genuinely landed and is verified from bytes.
> That is one finding of the forty-four raised at R30.
>
> **Answer to the dispatch's key question ("Where does the Goedel sentence land now that String 4 is
> genuinely closed?"): the premise is rejected.** String 4 is not closed. One gate was repaired; [10i],
> [13], [9c], [10f], and the [2f] failure message all still pass or emit falsehoods, and probe Q1 shows
> [10i] still *requires* a false sentence. The Goedel sentence did not move inward toward the
> self-referential surface. It moved **outward**, into the dispatch envelope, exactly where this seat
> predicted at R30.

**Auditor mode.** Mode A (substrate verifier), **with held prior bytes**. This is the first round in this
seat's lineage where Position 17 (append-only) is evaluable rather than UNKNOWN, because this seat holds
the complete v0.73 packet from the R30 dispatch. That single fact produced the CRITICAL below.

---

## 1. The Four Scribes, and the one repair that landed

| Scribe | Command | Result | Producer claim | Verdict |
|---|---|---|---|---|
| The Record | `sha256sum -c PACKET_SHA256SUMS` | 40/40 OK, rc=0 | (implied) | **TRUE** |
| The Pattern | `python3 build.py` | BUILD PASSED, 296 PASS, 0 FAIL, rc=0 | "BUILD PASSED, 0 FAIL" | **TRUE** |
| The Test | six-suite explicit `pytest` | 186 passed, rc=0 | "186 passed" | **TRUE** |
| The Witness | gate [13] CI-8 | 39/39, 0 missing, 0 phantom, 0 severity mismatches | "fires, 39/39" | **TRUE but four rounds stale** (F-S04-74-09) |

41 members extracted; `PACKET_SHA256SUMS` covers 40 with correct self-exclusion. The three dispatch-level
copies are byte-identical to their packet counterparts.

**F-S04-73-01 is CLOSED and verified.** `build.py` line 229 now reads
`check(ver_num - 3 <= prov_num <= ver_num - 1,`. Old pattern `prov_num == ver_num - 1` returns zero
occurrences. Probes Q9 and Q10 confirm the new predicate discriminates: a VERSION-3 provenance clause
(`v0.71 R28`) now passes, and a VERSION-9 clause (`v0.65 R24`) still fails. The v0.74 entry's account of
this repair is accurate in every particular, including its own admission that the v0.73 claim was
byte-false under a COMPUTED tag. **This is the correct shape of a repair entry and it should be the
template.** It is also, on the evidence below, the only one.

---

## 2. Findings

### F-S04-74-01 [CRITICAL] [Class A] -- Proven append-only violation: three sealed entries mutated in place and resealed

- **Locus:** Section 27 amendment entries `v0.71`, `v0.72`, `v0.73` (protocol lines 1685, 1713, 1735);
  `HISTORY.sha256` seals `ENTRY_v0.71`, `ENTRY_v0.72`, `ENTRY_v0.73`.
- **Substance:** This seat holds the v0.73 packet from the R30 dispatch and ran the direct cross-version
  comparison. Of 73 carried entries, **three were mutated in place** between the v0.73 build and the v0.74
  build, and their seals were regenerated over the mutated bytes:

  | Entry | v0.73 seal | v0.74 seal | Mutation |
  |---|---|---|---|
  | `ENTRY_v0.71` | `8ad32864268...` | `a38597cc06f...` | terminal line `v0.73` -> `v0.74` |
  | `ENTRY_v0.72` | `4f6afbab495...` | `af3f31e22ea...` | terminal line `v0.73` -> `v0.74` |
  | `ENTRY_v0.73` | `aed01c4afab...` | `20309890fec...` | terminal line `v0.73` -> `v0.74` |

  Each entry is otherwise byte-identical (7304, 5923, and 4348 characters, unchanged). The mutation is a
  single line per entry.

  The line each entry carries is its own terminal stamp. Entries v0.63 through v0.70 carry the correct
  historical stamps -- `*End of XZ Protocol v0.63 draft candidate.*` at line 1422, v0.64 at 1441, and so on
  through v0.70 at 1643. From v0.71 onward, all three read the **current** version. In the held v0.73
  bytes the same three lines read `v0.73`. A generator invoked with `VERSION` is overwriting the terminal
  stamp inside every entry from v0.71 forward at each build, and the window slides: at v0.75 it will
  rewrite four entries, and so on without bound.

  The v0.71 entry's terminal line is a historical fact about what v0.71 was. It now states something
  untrue of v0.71 and untrue of every intermediate version. No correction record exists anywhere in
  Section 27. Section 22.2 counts *"nine recorded in-place mutations at v0.4, v0.9, v0.11, v0.16, v0.17,
  v0.41, and v0.47"*; this is the **tenth**, it is undisclosed, and unlike several of its predecessors it
  is not a repair or a restoration -- it is silent overwriting of sealed history by routine build tooling.

  The carrying seat reported the same class at R30 (F-S01-73-06, HIGH, Class A). It was not dispositioned
  and it has extended by one entry.
- **Disposition:** (a) Stop invoking `generate_terminal_line(VERSION)` over anything but the current
  entry -- the terminal stamp of a sealed entry is historical data, not a rendered token. (b) Restore the
  v0.71, v0.72, and v0.73 terminal lines to `v0.71`, `v0.72`, `v0.73` from the held bytes, and record the
  restoration as an append-only correction naming this finding and F-S01-73-06. (c) Update Section 22.2's
  mutation count from nine to ten and add v0.71/v0.72/v0.73 to the version list. (d) Add a gate asserting
  that each entry's terminal line names that entry's own version, which is a one-line check and would have
  caught this at v0.72.
- **Cross-reference:** F-S01-73-06 (carrying seat, R30, not dispositioned); F-S04-74-02 (the mechanism
  that hides it); Section 22.2 mutation register; standing boundary 32; A-X4 (append-only storage
  integrity); Bearer 1; Position 17.

### F-S04-74-02 [HIGH] [Class B] -- The self-consistent reseal defeats the PRIOR_HISTORY control, using the instrument's own function

- **Locus:** `build.py::derive_prior_history`; gate [9b].
- **Substance:** The PRIOR_HISTORY derivation is the instrument's stated defence against retroactive
  mutation. Probe **Q7** mutated a sealed v0.63 entry, regenerated all seals, but left the shipped
  `PRIOR_HISTORY` line stale -- and the build correctly **FAILED** with
  `FAIL: PRIOR_HISTORY matches derivation`. The control fires. Probe **Q11** repeated the same mutation,
  regenerated the seals, and then recomputed the `PRIOR_HISTORY` value by calling the shipped
  `derive_prior_history` on the mutated bytes:

  ```
  derived PRIOR_HISTORY: 68a0f4a4945156c10dbba85c5044ab20a15f1304c9e38754eddcfe255897a9d1
  Q11 result: rc=0 -> BUILD PASSED
  sha256sum -c rc=0
  ```

  A forged packet with a mutated sealed entry passes every gate and every checksum. The reason is
  structural: `derive_prior_history` reconstructs the prior HISTORY file from (i) the entry seals **read
  out of the shipped, already-regenerated `HISTORY.sha256`** and (ii) `FULL_SECTION_27` computed over the
  **current, already-mutated** text. Both inputs are post-mutation, so the reconstruction reproduces
  whatever the producer built. The control detects only an *inconsistent* forgery -- one where the forger
  forgot a step. It cannot detect a consistent one, and a producer running the normal build pipeline is by
  construction always consistent. This is exactly why F-S04-74-01 shipped green.

  This is standing boundary 32, and it is honestly disclosed. What is new is that it is now **load-bearing
  rather than theoretical**: an actual, unintended, undisclosed mutation passed through it in this very
  build, and the only reason this report can name it is that an external party held the prior bytes.
- **Disposition:** The derivation cannot be repaired from inside the packet; that is its nature. Publish
  `PRIOR_HISTORY` outside the producer's control on each build -- a Zenodo deposit line, an IPFS CID, or
  simply the value quoted in each dispatch envelope and archived by the seats -- so a fresh seat can anchor
  against a value the producer cannot retroactively recompute. Until then, promote "hold the prior packet
  and run the cross-version entry diff" from an optional courtesy to a **mandatory step in every seat's
  dispatch**, and record in Section 22.2 that internal derivation provides no append-only assurance
  whatsoever against the producer.
- **Cross-reference:** F-S04-74-01 (what it hid); standing boundary 32 (F-SC04-47-02); F-S04-73-15
  (this seat's R30 statement that Position 17 was NOT EVALUABLE without held bytes -- now demonstrated to
  have been the correct call); A5 evidence-independence clause 4.

### F-S04-74-03 [HIGH] [Class A] -- Gate [10i] still manufactures the defect; the Section 0.1 range error was re-manufactured, not repaired

- **Locus:** Protocol Section 0.1, byte offset 3808; `build.py` [10i].
- **Substance:** Section 0.1 reads *"the full defect trajectory is in Section 27 (seventy-four amendment
  entries, v0.1 through v0.73)."* Tool enumeration returns **74 entries, v0.1 through v0.74**, no
  duplicates, no gaps. Seventy-four entries cannot span v0.1 through v0.73. The producer incremented both
  numerals and preserved the off-by-one exactly.

  It was preserved because the gate requires it. Gate [10i] still tests
  `f"v0.1 through v0.{VERSION-1}" in body` -- presence-anywhere over the whole body. On v0.74 bytes the
  string `"v0.1 through v0.73"` occurs **exactly once in the body**, at offset 3827, and it is the false
  Section 0.1 sentence. Probe **Q1** wrote the correct value `v0.1 through v0.74`, regenerated seals and
  the manifest, and the build returned:

  ```
  BUILD FAILED
    FAIL: Section 22.2 carried-entry bound at VERSION-1 (v0.1 through v0.73)
  ```

  This is the third consecutive round in which writing the truth turns the build red, and the second in
  which the "repair" consisted of updating the false sentence to a new false sentence. The R30 carrying
  seat reported the identical mechanism (F-S01-73-02, F-S01-73-03).
- **Disposition:** Re-scope [10i] to assert at the locus. Slice Section 22.2 and Section 22.3 by heading
  and assert the bound *inside each slice*. Then correct Section 0.1 to "v0.1 through v0.74" and Section
  22.2 independently. Point the existing [9e] cardinal-range predicate
  (`cardinal == end - start + 1`) at the Section 0.1 sentence -- the check already exists and needs only a
  locus.
- **Cross-reference:** F-S04-73-02, F-S04-73-03 (R30, this seat, not dispositioned); F-S01-73-02,
  F-S01-73-03 (R30, carrying seat, not dispositioned); F-S04-74-04.

### F-S04-74-04 [HIGH] [Class A] -- Section 22.2 is six versions stale, and the false claim about it now lives in the dispatch envelope

- **Locus:** Protocol Section 22.2, byte offset 88640; `AUDIT_CONTEXT.txt` item (2).
- **Substance:** Section 22.2 still reads *"For carried entries (v0.1 through v0.68), the PRIOR_HISTORY
  derivation in build.py [9b] detects retroactive mutation."* Six versions stale, unchanged since before
  R30. Probe **Q2** set it to the absurd *"v0.1 through v0.5"*, resealed seals and manifest, and the build
  returned **BUILD PASSED** -- the locus is entirely ungated (see F-S04-74-03 for why).

  The claim that this was fixed appears in `AUDIT_CONTEXT.txt` item (2): *"All prose version tokens updated
  (Section 0.1 range, Section 22.2/22.3 bounds)."* Section 22.3 was updated (`v0.38-v0.73`, verified).
  Section 22.2 was not. Section 0.1 was updated to a different wrong value.

  **This is the R30 forward prediction confirmed.** At R30 this seat wrote: *"the R31 Class A will be a
  false statement in a dispatch file about the artifact it dispatches."* At v0.73 this same claim sat
  inside the sealed amendment entry, where at least the seal chain and [9c] could theoretically reach it.
  At v0.74 the v0.74 entry makes **no claim at all** about Section 0.1 or Section 22.2 -- the claim moved
  out of the gated, sealed, tagged surface and into `AUDIT_CONTEXT.txt`, which is covered by no manifest,
  no seal, no gate, and no tag discipline. The instrument did not eliminate the false claim. It relocated
  it to where nothing can see it.
  Additionally, Section 22.2's sentence is now false in a second and more serious way: F-S04-74-02
  demonstrates that the derivation does **not** detect retroactive mutation of any entry when seals are
  regenerated, which is the ordinary case.
- **Disposition:** Correct Section 22.2 to "v0.1 through v0.73" and narrow its detection claim to match
  Q7/Q11. Then hash the dispatch envelope: add `DISPATCH.txt`, `AUDIT_CONTEXT.txt`, `CI_METHODOLOGY.txt`,
  `METHODOLOGY.txt`, and the triage and reports bundles to `PACKET_SHA256SUMS`, and derive every factual
  claim in them from the protocol rather than restating it alongside.
- **Cross-reference:** F-S04-73-04 (R30, not dispositioned); F-S01-73-03; F-S04-74-03; the R30 forward
  prediction (Section 8 of `SHIPPED_R30_S04_REPORT.md`, shipped in this packet).

### F-S04-74-05 [HIGH] [Class A] -- The status line is the v0.73 sentence with the version numbers changed; four false claims, all raised at R30, none repaired

- **Locus:** Protocol front-matter `**Status:**` line.
- **Substance:** The v0.74 status line is byte-identical to the v0.73 status line apart from `v0.73`->`v0.74`
  and `R29`->`R30`. Every defect this seat and the carrying seat reported in it at R30 survives intact,
  and two have worsened:

  | Status-line claim | Refuted by | Probe |
  |---|---|---|
  | "(4/4 HALT; 4-seat round)" | the v0.74 entry twelve lines below -- *"R30 returned 3/3 HALT ... S02 Gemini returned closure assessment"*; `R30_TRIAGE.txt`; `AUDIT_CONTEXT.txt`; the shipped `SHIPPED_R30_S02_ASSESSMENT.md`, which renders no verdict | **Q3**: rewritten to "9/9 HALT", BUILD PASSED |
  | "Class A recurrence R7-R28: 22/22" | the v0.74 entry -- *"Class A recurrence R7-R30: 24/24"*. Now **two rounds** stale, up from one at v0.73 | -- |
  | "Methodology: v7 canonical (six strings)" | the shipped `METHODOLOGY.txt`, which is byte-identical to the R30 copy (`59aa6591...`), is seven layers and twenty-four positions, and self-identifies as **v6**. Zero grep hits for "six string", "twenty-one", or "v7" | **Q4**: rewritten to "v99 canonical (nine trombones)", BUILD PASSED |
  | "boundaries.json version current" | `xz_protocol_boundaries.json` carries `"version": "0.72"` at VERSION 0.74. Now **two versions** stale | **Q5**: rewritten to "0.01", BUILD PASSED |

  Also unchanged: the "Prescribed repairs landed" list still enumerates v0.72's repairs (C-suffix
  DECLARATION_PATTERNS, gate [13] fail-closed, register generator graceful degradation, boundaries.json),
  and makes no mention of the one repair v0.74 actually landed.

  Four Class A defects in one sentence. Both R30 seats that read it flagged it (F-S04-73-05, -06, -07, -11,
  -14; F-S01-73-05, -15, -16). The sentence was edited in this build -- the version numerals moved -- so
  this is not neglect of an untouched surface. The producer edited the sentence and preserved every
  falsehood in it.
- **Disposition:** Emit the status line from a generator, as the boundary list and terminal line already
  are. Verdict tally from the round index, recurrence count from the entry, methodology token from
  `METHODOLOGY.txt`'s own header, repair list from the current entry's repair items. Gate each. A sentence
  that carries five independent facts and is maintained by hand will diverge on all five.
- **Cross-reference:** F-S04-73-05, -06, -07, -11, -14 (R30, this seat); F-S01-73-05, -15, -16 (R30,
  carrying seat); substrate-of-record uniqueness rule.

### F-S04-74-06 [HIGH] [Class A] -- Section 25 test-component counts are false and ungated

- **Locus:** Protocol Section 25, FB-4 row (line 767) and FB-5 row (line 768).
- **Substance:** The FB-4 row states *"22 source-frame tests"*; AST enumeration of
  `test_xz_protocol_source_frame.py` returns **29**. The FB-5 row states *"30 control-graph tests"*; AST
  enumeration of `test_xz_protocol_control_graph.py` returns **18**. The suite totals are correct
  (14+29+29+18+27+69 = 186, matching the gated total), so the error is confined to the per-component split
  and is invisible to gate [5], which checks only the aggregate. Probe **Q6** rewrote the FB-4 figure to
  "999 source-frame tests", resealed, and the build returned **BUILD PASSED**.

  The carrying seat reported this at R30 (F-S01-73-08, HIGH, Class A). Not dispositioned, unchanged.
- **Disposition:** Derive both figures at build time by AST count, as gate [5] already does for the total,
  and assert them at the FB-4 and FB-5 row loci. Correct to 29 and 18.
- **Cross-reference:** F-S01-73-08 (R30, carrying seat, not dispositioned); gate [5]; Position 8.

### F-S04-74-07 [HIGH] [Class A] -- The FB-7b row, designated the single source of truth for the "full carrying-seat trajectory", terminates at R27

- **Locus:** Protocol Section 25 FB-7b row; Section 0.1, paragraph 2.
- **Substance:** Section 0.1 states that *"FB-7b status, rationale, and the full carrying-seat trajectory
  are recorded in the Section 25 FB-7b row (single source of truth; no duplicate rationale maintained
  here)."* The row's trajectory narrative runs R6 through R27 and stops at *"R27 (v0.68): 4 seats, all
  HALTed."* Grep of the row returns zero `R28 (`, zero `R29 (`, zero `R30 (` tokens. Four rounds of
  carrying-seat history -- including three consecutive binding Kimi K3 HALTs -- are absent from the surface
  the document designates as their sole record. The row's status token (`PENDING RE-CARRY v0.74`) is
  current, so gate [2g] passes on a half-current row: the token is gated, the trajectory is not.

  The carrying seat reported this at R30 (F-S01-73-04). Not dispositioned.
- **Disposition:** Append R28, R29, and R30 lines to the FB-7b row. Extend gate [2g] to assert that the
  highest round token in the row equals VERSION-1's round, so trajectory staleness fails the same way
  status staleness does.
- **Cross-reference:** F-S01-73-04 (R30, carrying seat); F-S04-73 Position 10; gate [2g].

### F-S04-74-08 [HIGH] [Class B] -- Forty-three of forty-four R30 findings are undispositioned and unrecorded

- **Locus:** v0.74 amendment entry; the four shipped R30 reports.
- **Substance:** R30 raised **44 findings** across three reporting seats: 19 from S01 (Kimi K3, carrying,
  binding HALT), 10 from S03 (GPT-5.6 Sol, adversarial), and 15 from S04 (Claude Opus 5, advisory). All
  four R30 documents ship in this packet and are byte-verified. The v0.74 entry dispositions exactly
  **one** -- F-S01-73-01, the gate [2f] repair.

  Grep of the entire protocol returns zero occurrences of any `F-S04-73-*` identifier and zero
  occurrences of any `F-S03-73-*` identifier. Twenty-five findings from two seats, including at least
  eight Class A, are absent from the amendment record entirely -- not closed, not noted, not disclosed,
  not mentioned. The register paragraph in the v0.74 entry still disposes the **R27** round, four rounds
  behind, and it has been further abridged since v0.73 (the per-item substance clauses were dropped).

  Section 22 item 7's HALT rule and the program's append-only discipline both presuppose that raised
  findings enter the record. The instrument's own precedent is explicit: at v0.20 the producer was
  required to assign IDs and dispositions to five findings that "carried no IDs and no dispositions"
  (F-ADJ19-10). Here, twenty-five carry IDs and receive no disposition.

  No gate can notice, because gate [13] -- the only cardinality control -- reads the R27 index against the
  R27 reports (F-S04-74-09).
- **Disposition:** Disposition all 44 R30 findings in the v0.75 entry, each as CLOSED, CLOSED IN PART,
  DISCLOSED NOT CLOSED, or NOTED, with a stated basis. Advance the findings index to R30 so gate [13]
  binds the register to the round it claims to dispose. Where a finding is rejected, record the rejection
  -- CR-6 already fixes that an append-only regime records rejected findings, not only accepted ones.
- **Cross-reference:** F-ADJ19-10 (v0.20 precedent); F-S04-74-09 (why no gate sees it); CR-6;
  Section 22 item 7.

### F-S04-74-09 [MEDIUM] [Class D] -- Gate [13] is now four rounds stale and blind to twelve shipped reports

- **Locus:** `build.py` [13] selector and `index_file`.
- **Substance:** Unchanged from R30. The selector
  `[f for f in os.listdir(".") if f.startswith("R") and f.endswith("_REPORT.md")]` resolves to the four
  `R27_S0*_REPORT.md` files; `index_file` is `r27_findings_index.json` (round 27, version 0.68). Twelve
  `SHIPPED_R28/R29/R30` reports are excluded by first character, and `version_filter` derived from the
  index ("68") would exclude their finding IDs even after renaming. The green "39 in reports, 39 in index"
  is an R27 statement, now four rounds and six versions behind the artifact.

  Reported at R30 by two seats (F-S04-73-09, F-S01-73-11). Not dispositioned.
- **Disposition:** Build an R30 index and advance `index_file`; normalise report filenames to the selector
  or replace the glob with an explicit round manifest. Print the round scope inside the gate's own PASS
  line (`CI-8 cardinality (round 27)`) so staleness is visible in the build output rather than inferable
  from a filename.
- **Cross-reference:** F-S04-73-09, F-S01-73-11 (R30, both undispositioned); F-S04-74-08.

### F-S04-74-10 [MEDIUM] [Class D] -- The COMPUTED-tag form evasion is unrepaired, and it now conceals the one honest repair claim

- **Locus:** `build.py` [9c] regex; v0.74 entry, both `[COMPUTED: build.py gate 2f]` tags.
- **Substance:** [9c] validates `[COMPUTED: build.py [X] ...]` tags and requires the section id in square
  brackets. The v0.74 entry writes `[COMPUTED: build.py gate 2f]` twice -- unbracketed -- so neither tag
  is matched or validated. Zero of the entry's four COMPUTED tags naming `build.py` are visible to [9c].
  The R30 paired probes (P8 bracketed -> [9c] fires; P9 unbracketed -> silent) established the mechanism;
  it is unchanged.

  The irony is instructive rather than incidental. At v0.73 this defect concealed a **false** repair
  claim. At v0.74 it conceals a **true** one. The gate is indifferent to the truth of what it fails to
  read, which is precisely why an unparseable provenance tag must be an error rather than a silent skip.
  Both R30 seats reported it (F-S04-73-10, F-S01-73-12).
- **Disposition:** Widen the [9c] regex to accept an optional `gate`/`section` keyword and an optionally
  bracketed identifier, and fail-closed on any `[COMPUTED: build.py ...]` tag the regex cannot parse.
- **Cross-reference:** F-S04-73-10, F-S01-73-12 (R30, both undispositioned); standing boundary 1.

### F-S04-74-11 [MEDIUM] [Class D] -- The repaired gate [2f] emits a failure message describing the rule it no longer enforces

- **Locus:** `build.py` lines 229-230.
- **Substance:** The predicate is now the range `ver_num - 3 <= prov_num <= ver_num - 1`, but the message
  string was left untouched:

  ```python
  check(ver_num - 3 <= prov_num <= ver_num - 1,
        f"Status provenance v{prov_ver} == v{VERSION} - 1")
  ```

  On the passing path the build prints `PASS: Status provenance v0.73 == v0.74 - 1`, which is coincidentally
  true here and will be false whenever VERSION-2 or VERSION-3 is used -- the very case the repair exists to
  permit. Probe **Q10** confirms the failure path prints `FAIL: Status provenance v0.65 == v0.74 - 1` while
  the actual violated rule is the range. A gate whose message misdescribes its predicate is a
  surface-substrate divergence inside the verification layer, and the audit record is assembled from these
  messages.
- **Disposition:** Change the message to state the range, e.g.
  `f"Status provenance v{prov_ver} in [v{VERSION}-3, v{VERSION}-1]"`. Add a build-time lint, or a review
  step in the producer discipline, requiring that any predicate change carry its message with it.
- **Cross-reference:** F-S04-73-01 (the repair this rides on); Position 8; the [10i]/[9d] comment-vs-code
  precedents at v0.18 (F-OP18-03).

### F-S04-74-12 [MEDIUM] [Class A / Class D] -- `boundaries.json` version field two versions stale, asserted current, gated by nothing

- **Locus:** `xz_protocol_boundaries.json` field `version`; protocol status line; `build.py` [10f].
- **Substance:** The file carries `"version": "0.72"` at VERSION 0.74 -- one version stale at R30, two
  now. The status line continues to assert *"boundaries.json version current."* [10f] couples only the item
  count (35, correct). Probe **Q5** set the field to `"0.01"`, resealed, and the build returned
  **BUILD PASSED**. Reported at R30 by two seats (F-S04-73-11, F-S01-73-15).
- **Disposition:** Stamp the field to VERSION at build time and add a `check()` in [10f], or declare the
  field non-normative and strike the status-line claim.
- **Cross-reference:** F-S04-73-11, F-S01-73-15 (R30, undispositioned); F-S04-74-05.

### F-S04-74-13 [LOW] [Class B] -- Tagging: 15 of 21 sentences untagged; the ASSERTED fraction again improved by shrinking

- **Locus:** v0.74 amendment entry; `build.py` [9c] tag census.
- **Substance:** The build reports `COMPUTED: 4, EXTERNAL: 0, ASSERTED: 2` and an ASSERTED fraction of
  **2/6 (33.3%)**. Independent sentence census of the entry: **21 sentences, 15 untagged**, against
  Position 18's criterion of zero. The tagged population fell from 9 at v0.73 to 6, so the printed
  denominator shrank again. Load-bearing untagged claims include *"Class A recurrence R7-R30: 24/24"* and
  *"Closes F-S01-73-01, F-S04-70-09, F-S04-70-10."*

  The improvement over v0.73 is real in one respect and illusory in another: the surviving COMPUTED tags
  are, for the first time in this seat's experience, **all true of the bytes**. That is genuine progress
  and should be said plainly. But the metric that displays it is still measuring the wrong denominator.
- **Disposition:** Print both denominators, as v0.26 was required to do for the same defect
  (F-GLM26-02). Add a [9c] sub-check counting untagged sentences in the current entry and print it beside
  the fraction.
- **Cross-reference:** F-S04-73-13 (R30, undispositioned); F-GLM26-02 (v0.26); F-OP20-03 (DISCLOSED NOT
  CLOSED since v0.20); Position 18.

### F-S04-74-14 [LOW] [Class C] -- The standing-boundary list does not carry the boundary this round proved

- **Locus:** v0.74 entry, boundary enumeration (35 items).
- **Substance:** The list is unchanged at 35 items and correctly reproduces from `generate_boundary_list`
  (byte-exact -- verified). It carries item 32, *"self-consistent resealing blind spot (proven live at
  v0.47, F-SC04-47-02)"*. It does not carry the fact established this round: that the blind spot is not
  merely available to a hypothetical forger but is being traversed by the producer's own routine build,
  and that the terminal-line regeneration window slides forward one entry per version.
- **Disposition:** After absorbing F-S04-74-01 and -02, add a boundary item recording that the internal
  derivation provides no append-only assurance against the producer and that external held bytes are the
  sole control; update item 32's parenthetical to cite v0.74 as well as v0.47.
- **Cross-reference:** F-S04-74-01, F-S04-74-02; standing boundary 32.

### F-S04-74-15 [GOVERNANCE DECLARATION -- not a defect claim] -- This seat is not fresh, and the dispatch label is false of it

- **Locus:** `DISPATCH.txt` line 1 (`# R31 DISPATCH -- Seat S04 (FRESH)`).
- **Substance:** Two facts must be on the record, and they cut in opposite directions.

  **Against independence:** this seat is not fresh. It executed the R30 S04 audit on v0.73, and its report
  ships in this packet as `SHIPPED_R30_S04_REPORT.md`, byte-verified identical to this seat's own output
  (`044776606cdac4b4482b3f856616956de99bba3b3c21b8b63ff7a73d56b6b594`). It holds the complete v0.73 packet
  in working memory. Its findings are therefore continuous, not independent, and its convergence with
  S01's R30 findings carries **no** mutawatir weight -- the methodology's independence conditions (a) and
  (c) both fail. Discount accordingly. This is the same defect recorded at v0.43 as F-S1-00 (a seat
  deployed as fresh that was in fact continuous) and it is now on its second occurrence with the same seat
  label.

  **For the record's benefit:** the held bytes are the only reason F-S04-74-01 is provable rather than
  suspected. A genuinely fresh seat would have found Position 17 NOT EVALUABLE, exactly as this seat
  reported at R30 (F-S04-73-15), and the tenth in-place mutation would have shipped again. The program
  should not read this as an argument for continuous seats; it is an argument that **someone must hold
  prior bytes**, and that whoever does must be labelled honestly so their findings are weighted correctly.
- **Disposition:** Stop labelling dispatches FRESH by default. Label the seat's actual state
  (fresh / continuous / continuous-with-held-bytes), and treat "holds prior packet" as a distinct,
  required role in the witness pool rather than an accident of routing. `METHODOLOGY.txt` Section 5 should
  carry that column.
- **Cross-reference:** F-S1-00 (v0.43); F-S04-73-08 (R30, seat-table contradiction, undispositioned);
  `METHODOLOGY.txt` Section 5 independence conditions (a)-(d); A-X3, A-X5.

---

## 3. Probe battery

Twelve probes. Each carries a mutation-landed digest assertion; each reseals `PACKET_SHA256SUMS`, and
where the mutation touches Section 27, regenerates `HISTORY.sha256` seals -- so neither the manifest nor
the seal chain is the discriminator and the semantic gates are tested in isolation. No probe was VOID.

| Probe | Mutation | Build | Reading |
|---|---|---|---|
| **Q0** | none (clean packet) | PASSED, 0 fail-checks | baseline green is real |
| **Q-neg** | title `v0.74` -> `v0.73` | **FAILED** (`Title version`) | control: gates discriminate |
| **Q1** | Section 0.1 range -> **v0.74** (the true value) | **FAILED** (`Section 22.2 carried-entry bound`) | **truth breaks the build**, third round running (F-S04-74-03) |
| **Q2** | Section 22.2 -> "v0.1 through v0.5" | **PASSED** | false-PASS: 22.2 locus ungated |
| **Q3** | status "4/4 HALT" -> "9/9 HALT" | **PASSED** | false-PASS: verdict tally ungated |
| **Q4** | status methodology -> "v99 (nine trombones)" | **PASSED** | false-PASS: methodology token ungated |
| **Q5** | `boundaries.json` version -> "0.01" | **PASSED** | false-PASS: version field ungated |
| **Q6** | Section 25 FB-4 "22" -> "999 source-frame tests" | **PASSED** | false-PASS: component counts ungated |
| **Q7** | mutate sealed v0.63 entry + regenerate seals, stale PRIOR | **FAILED** (`PRIOR_HISTORY matches derivation`) | the control fires on an *inconsistent* forgery |
| **Q8** | same mutation, no reseal at all (control for Q7) | **FAILED** (seal + FULL_SECTION_27 + PRIOR) | control fires as designed |
| **Q9** | [2f] provenance -> `v0.71 R28` (VERSION-3) | **PASSED** | **correct**: the landed repair accepts the range |
| **Q10** | [2f] provenance -> `v0.65 R24` (VERSION-9) | **FAILED** (`Status provenance`) | **correct**: the range still discriminates |
| **Q11** | mutate sealed v0.63 entry + regenerate seals + **recompute PRIOR_HISTORY via the shipped `derive_prior_history`** | **PASSED**, `sha256sum -c` rc=0 | **full self-consistent forgery** (F-S04-74-02) |

Six demonstrated false-PASS paths plus one full forgery. Q9 and Q10 are the round's positive result: they
are the first probes in this seat's experience where a prescribed repair discriminated exactly as
specified. Q7-versus-Q11 is the round's most important pair: it isolates precisely what the PRIOR_HISTORY
control does and does not do.

---

## 4. Coverage

| Surface | Chars | Share |
|---|---|---|
| Total document | 483,532 | 100% |
| Body (in scope for gates) | 108,006 | 22.3% |
| Section 27 (outside every semantic gate) | 375,526 | **77.7%** |
| Semantic-gate coverage of the body | 32,302 | 29.9% of body |
| Semantic-gate coverage of the document | 32,302 | **6.7% of total** |

Unchanged in proportion from v0.73, and the ungated share continues its monotone growth in absolute terms
(371,763 -> 375,526 chars). To this must now be added the **dispatch envelope** -- `DISPATCH.txt`,
`AUDIT_CONTEXT.txt`, `CI_METHODOLOGY.txt`, `METHODOLOGY.txt`, `R30_TRIAGE.txt`, `R30_REPORTS.txt`,
roughly 138 KB shipped to every witness, covered by no manifest, no seal, and no gate. Two of this round's
seven Class A findings (F-S04-74-04, and the methodology limb of -05) live there.

---

## 5. Bearer assessment (BSSG three-valued)

| Bearer | Value | Change from R30 | Basis |
|---|---|---|---|
| 1. Append-only | **FALSE** | UNKNOWN -> **FALSE** | F-S04-74-01: three sealed entries mutated in place and resealed, proven against held v0.73 bytes |
| 2. Code correctness | **TRUE** | unchanged | 186 passed rc=0; 296 PASS / 0 FAIL rc=0; `sha256sum -c` 40/40 rc=0 |
| 3. Surface narrowing | **FALSE** | unchanged | The defect surface did not narrow; it relocated outward to the dispatch envelope (F-S04-74-04) |
| 4. Goedel confinement | **FALSE** | unchanged | 7 Class A; only -13 sits at Positions 18-21. Positions 8, 9, 15, 17, 20 all carry Class A |
| 5. Cross-vendor witness | **FALSE** | unchanged | R30 returned 3 HALT including a binding carrying-seat HALT; this seat is producer-family advisory and is additionally non-independent (F-S04-74-15) |
| 6. Axiom disclosure | **TRUE** | unchanged | A-X1..A-X5 present in Section 22.4; Sidrat clause present and correctly `[DISCLOSED]` |
| 7. Methodology verification | **FALSE** | unchanged | Position 18 fails (15/21 untagged); index four rounds stale; 43 of 44 findings undispositioned (F-S04-74-08) |
| 8. The furqan | **RESERVED** | -- | Position 24 is the lead's act. This seat does not exercise it |

Bearer 1 moved from UNKNOWN to FALSE. That is the round's material change, and it moved in the wrong
direction -- not because the instrument got worse, but because for the first time a seat could see.

---

## 6. Standing-rules sweep

| Rule | Result |
|---|---|
| Em-dash policy (U+2013/2014/2015) | **CLEAN** in protocol, `build.py`, and all dispatch-envelope files |
| Brand canonical | **CLEAN** |
| Severity uppercase | **CLEAN** |
| Six-element findings format | Applied to all 15 items in this report |
| Substrate-of-record uniqueness | **VIOLATED** -- F-S04-74-05, -07, -12 are two-locus duplications that diverged |
| Audit-chain immutability (BAF v3.0 §14.5) | **VIOLATED** -- F-S04-74-01 |

---

## 7. Where the Goedel sentence actually landed

The dispatch asks where the Goedel sentence lands now that String 4 is genuinely closed. String 4 is not
closed, but the question is worth answering on its merits, because the round produced a real answer.

**The trajectory this round.** One gate was repaired, correctly and verifiably, and the entry describing
that repair is the most honest amendment text in the material this seat has read. That is not nothing.
But the round's other movement was not narrowing. Between v0.73 and v0.74 the false claim about Section
0.1 and Section 22.2 **left the sealed amendment entry and reappeared in `AUDIT_CONTEXT.txt`**. Inside the
entry it was tagged, sealed, and at least nominally within [9c]'s reach. In the dispatch envelope it is
covered by nothing at all. The defect did not migrate upward through the layers toward the self-referential
surface, as the methodology's Iblis-trajectory model predicts. It migrated **laterally, out of the
verified artifact into the unverified apparatus that describes it**. That is a fifth level the taxonomy in
`METHODOLOGY.txt` Section 17.2 has no row for.

**Why the H = 1.0 series does not break here.** Two structural facts, both established by probe this
round, jointly guarantee that the producer's self-check cannot terminate the series. First, the gate suite
reads 6.7% of the document and none of the envelope. Second -- and this is the deeper one -- the
PRIOR_HISTORY control cannot detect a *consistent* forgery, and a producer running its own build pipeline
is consistent by construction (Q7 versus Q11). The instrument's temporal integrity is therefore not
self-verifying in any degree against its own producer. The v0.71/v0.72/v0.73 mutation is not a
sophisticated attack; it is a generator called with the wrong argument, and it shipped green through every
gate the instrument has.

**What actually caught it.** One thing, and only one: a party outside the producer's authority holding
prior bytes. That is A5 clause 4 -- *"at least one witness outside the operator's unilateral control"* --
not as a formal proposition but as the operative cause of the only CRITICAL in this report. The program's
own axiom did the work its own gates could not.

**Forward prediction for R32,** offered so the next seat can test rather than rediscover. If the envelope
is hashed and the terminal-line generator is scoped, the next Class A will be in the **seat reports as
cited evidence**: twelve report files now ship in-packet, they are manifested but semantically unread,
gate [13] cannot see them, and the amendment record has begun making claims about what seats returned
(the v0.74 entry's "R30 returned 3/3 HALT ... S02 Gemini returned closure assessment") with no gate
binding those claims to the shipped files. That is the same shape as F-OP18-01 at v0.18, one layer out.

---

## 8. Recommendation

1. **F-S04-74-01 first, and restore from the held bytes, not from memory.** Scope
   `generate_terminal_line` to the current entry only; restore three terminal lines; record an append-only
   correction; update the Section 22.2 mutation count to ten. Add the one-line per-entry terminal-stamp
   check.
2. **Disposition all 44 R30 findings** in the v0.75 entry and advance the findings index to R30, so gate
   [13] binds the register to the round it disposes.
3. **Repair F-S04-74-03 and -04 as one atomic change** -- re-scope [10i] to the locus first, then correct
   Section 0.1 and Section 22.2. Repairing either alone reds the build or leaves the locus unverified.
4. **Hash the dispatch envelope** into `PACKET_SHA256SUMS` and derive its claims from the protocol.
5. **Generate the status line.** Four Class A in one hand-maintained sentence, across two rounds, two
   seats, and eight prior findings.
6. **Publish `PRIOR_HISTORY` outside the producer's control**, and make "hold the prior packet, run the
   cross-version entry diff" a mandatory dispatch step rather than a courtesy. Q11 shows the internal
   control cannot substitute for it.
7. **Cross-vendor rotation and seat labelling.** This seat is Anthropic, the producer is Anthropic, and
   this seat is continuous rather than fresh (F-S04-74-15): its weight is advisory and its convergence
   with S01 is not independent. Route R32 to Kimi K3 and a second non-producer family, label each seat's
   actual state, and ensure at least one seat holds v0.74 bytes across the round.
8. **Position 24 is not exercised here.** The bayyinah is the record above; the furqan is the lead's.

---

*Seat S04, Round 31. Advisory, non-carrying, continuous. The record is the evidence.*

---

# Bismillah ir-Rahman ir-Rahim
