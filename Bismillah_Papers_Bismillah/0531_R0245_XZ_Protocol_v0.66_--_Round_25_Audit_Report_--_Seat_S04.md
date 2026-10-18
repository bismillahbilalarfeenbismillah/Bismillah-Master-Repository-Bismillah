# Bismillah ir-Rahman ir-Rahim

# R0245 -- XZ Protocol v0.66 -- Round 25 Audit Report -- Seat S04

**Chronological Index:** 531 of 995  
**Date:** 2026-08-17  
**Section:** IV. XZ Protocol  
**Source File:** XZ_v066_R25_S04_REPORT (1).md  
**Source Format:** md  
**SHA-256:** `0799968287b9a092a92c10ac24a592e3dab2eb47864b3ba3284e0b70e4ff4454`  

---

## R0245 · XZ Protocol v0.66 -- Round 25 Audit Report -- Seat S04

- section: IV. XZ Protocol
- source_file: XZ_v066_R25_S04_REPORT (1).md
- source_format: md
- text_sha256: 0799968287b9a092a92c10ac24a592e3dab2eb47864b3ba3284e0b70e4ff4454

# XZ Protocol v0.66 -- Round 25 Audit Report -- Seat S04

**Round:** 25 ("The Furqan Window, continued")
**Artifact:** XZ Protocol v0.66 DRAFT CANDIDATE
**Seat:** S04
**Dispatched family:** Gemini 3.1 Pro (ADVISORY)
**Dispatched mode:** FRESH -- no prior context, no held bytes
**Executing family:** Claude Opus 5 -- see S0
**Actual mode:** CONTINUOUS with held prior bytes -- see S0
**Date:** 2026-08-17
**Verdict:** **HALT**

---

## S0. Seat identity, conformance, and disqualifying conditions

Auditor operated in **Mode A** (substrate verifier). Substrate-claim
verification confidence: **high**. Environment: Python 3.12.3,
pytest 9.1.1.

**Declared non-conformance -- three deviations. The third is
disqualifying for independence and must be carried into triage.**

1. **Family substitution.** DISPATCH.txt assigns this seat to
   Gemini 3.1 Pro, whose trial is textual audit without code execution.
   Executed by Claude Opus 5 with full sandbox. Third consecutive round
   of seat-label drift in this program (R23 S01, R24 S04, R25 S04).

2. **Producer adjacency.** Producer is Claude Opus 4.6, marked BARRED.
   The executing family is the producer's vendor family. Under
   METHODOLOGY Section 5 this seat carries the S01 trial wearing the
   S04 label.

3. **Mode falsification -- this seat is not fresh.** DISPATCH.txt
   declares `Mode: FRESH. No prior context. No held bytes.` Both
   conditions are false. This instance executed the R24 audit of v0.65
   in the same session; it holds the full v0.65 packet on disk,
   including `xz_protocol_v0_65.md`, and it authored
   `F-S04-65-01` through `F-S04-65-12`, which ship verbatim in
   `R24_REPORTS.txt` (L825 onward) and are the subject of several
   findings below.

**Consequences, stated in both directions.**

*Against the round.* This report's agreement with prior S04 findings is
**not** independent confirmation and must not be counted as convergence
at triage. Where a finding below records a defect this seat previously
recorded, the correct reading is persistence observed by the same
observer, not two chains. The Bayt al-Ma'mur principle (fresh seats
never return) is violated. Any R25 convergence arithmetic that treats
this seat as a fresh Gemini chain overstates the evidence.

*For the record.* The held bytes make one class of verification
available that no prior seat in this lineage has had. Bearer 1 is
normally assessed against producer-supplied anchors -- the HISTORY file
inside the same packet, or a truncated hash quoted in a prior report.
This seat compared all sixty-five carried entries in v0.66 against
independently held v0.65 bytes. The result is in S4 and it is the
strongest append-only evidence the program has produced. The deviation
that destroys this seat's independence is the same deviation that
produces that evidence. Both facts are recorded; neither cancels the
other.

Not producer-instance: this instance did not author v0.66, the R24
triage, the index, or any packet member.

---

## S1. Staging and the four scribes

| Scribe | Instrument | Result |
|---|---|---|
| The Record | `sha256sum -c PACKET_SHA256SUMS` | **19/19 OK** |
| The Record | `HISTORY.sha256` recompute | **66/66 ENTRY seals verify** |
| The Pattern | `python3 build.py` | **253 PASS / 0 FAIL**, BUILD PASSED |
| The Test | six-suite `pytest` | **186 passed** in 8.55s |
| The Witness | CI-1R | **PASS**, byte-identical |

P6, P7, P8 CONFIRMED. P14 falsified: see F-S04-66-10.

---

## S2. CI-1R and the register emission repair

`generate_register('r24_findings_index.json', '0.66')` produces 4011
characters, present verbatim in the v0.66 entry.
`generate_boundary_list` output (1797 characters) likewise.
**CI-1R: PASS.** P1 CONFIRMED.

The `label` to `surface` repair **landed**. Diff against the v0.65
generator is exactly two changes: the noted-ID prefix check at L219--223
and `group.get('label', '')` becoming `group.get('surface', '')` at
L288. Every register item now carries a defect description where v0.65
emitted an empty string. **P2 CONFIRMED.** This was a genuine one-word
defect, correctly diagnosed at R24 and correctly fixed.

Probe P-N3 (`finding_id = "XX-BOGUS"`) now **raises ValueError**.
**P3 CONFIRMED.** The R24 blocking probe is closed at the instance
level. See F-S04-66-06 for the class.

Three real repairs landed this round. That is the most in any round this
seat has observed, and it should be read against the findings below
rather than replaced by them.

---

## S3. Prior-round discharge -- this seat's twelve R24 findings

`R24_REPORTS.txt` ships this seat's R24 report verbatim, so discharge is
checkable line by line rather than by recollection.

| R24 ID | Substance | Status at v0.66 |
|---|---|---|
| F-S04-65-01 | noted format validation absent | **CLOSED (instance)** -- class open, F-S04-66-06 |
| F-S04-65-02 | CI-8 source fidelity | **COUNT closed, FIDELITY open** -- F-S04-66-01 |
| F-S04-65-03 | Section 0.1 `on v0.62` | **OPEN** -- F-S04-66-03, and recorded CLOSED under a different substance |
| F-S04-65-04 | FB-7b row ends at R18 | **OPEN** -- F-S04-66-04, and recorded CLOSED under a different substance |
| F-S04-65-05 | gate `[10f]` count not text | **OPEN** -- F-S04-66-07 |
| F-S04-65-06 | register generator untested | **OPEN** -- F-S04-66-08 |
| F-S04-65-07 | ASSERTED metric counts tags | **OPEN** -- F-S04-66-09 |
| F-S04-65-08 | repair tag cites unshipped file | **SUPERSEDED** -- v0.66 cites `r24_findings_index.json`, which ships |
| F-S04-65-09 | gate count off by one | **OPEN** -- F-S04-66-10 |
| F-S04-65-10 | tagging discipline | **OPEN** -- F-S04-66-05 |
| F-S04-65-11 | dispatch filename divergence | **CLOSED** -- both files now resolve to `XZ_v066_R25_S04_REPORT.md` |
| F-S04-65-12 | boundaries file version token | **OPEN** -- F-S04-66-11 |

Two closed, one superseded, one half-closed, eight open. The R24 triage
recorded dispositions of CLOSED for surfaces 5 and 6, both of which are
demonstrably open below.

---

## S4. Append-only integrity against held bytes

All sixty-six ENTRY seals recompute from v0.66 bytes. Beyond that:

```
v0.65 entry, held bytes  : 9cc80aa914e73826...
v0.65 entry, v0.66 ship  : 9cc80aa914e73826...
byte-identical           : True
carried entries v0.1 through v0.65 differing from held bytes : NONE
```

Every one of the sixty-five carried entries in v0.66 is byte-identical
to the same entry as it shipped in the v0.65 packet this instance
independently extracted, verified, and retained. This is not an anchor
supplied by the producer and not a prefix quoted from a prior report.
It is a full-text comparison against bytes held outside the artifact
under audit.

**Bearer 1 is TRUE on the strongest evidence available in this
lineage.** P9 CONFIRMED. The append-only discipline holds.

Section 22.4 present at L722 with the axiom set and the Sidrat clause.
**P5 CONFIRMED.** Terminal line reads `v0.66`. **P13 CONFIRMED.**

---

## S5. Probe battery

| Probe | Mutation | Result |
|---|---|---|
| P-N3 | noted `finding_id` = "XX-BOGUS" | **REJECTED** (was accepted at v0.65) |
| P-N3b | noted `finding_id` = "F-S04-65-N9" | **ACCEPTED -- FALSE PASS** |
| P-N5 | noted `substance` = empty string | **ACCEPTED -- FALSE PASS** |
| P-N6 | noted `substance` = "TODO" | **ACCEPTED -- FALSE PASS** |
| P-G1 | group `surface` key deleted | REJECTED |
| P-G2 | group `surface` replaced with unrelated text | **ACCEPTED -- FALSE PASS** |
| M3 | boundary item reworded in the boundaries file | **BUILD PASSED -- FALSE PASS** |

Four live false-passes. P-N5, P-N6, and P-G2 are the mechanism behind
F-S04-66-01 and F-S04-66-02: the index schema validates that a substance
field and a surface field *exist*, never that either says anything true
about the finding it labels.

---

## S6. Findings

### F-S04-66-01 [HIGH] -- CI-8 completeness was achieved by count and voided by content

- **Locus:** `FINDINGS_INDEX.txt` / `r24_findings_index.json`,
  `unique_findings_noted[]` (23 records) and `findings[]` (12 records);
  `xz_protocol_v0_66.md` Section 27, v0.66 entry, repair clause (3);
  `AUDIT_CONTEXT.txt`, "What is new in v0.66".
- **Substance:** ID-level completeness is genuinely achieved and should
  be credited: the set of finding IDs in the index and the set in
  `R24_REPORTS.txt` are **exactly equal at 35 each**, with no ID in
  either set absent from the other. Content fidelity is not achieved.
  All **23 of 23** noted records carry the identical substance string
  `See R24 seat report for details.` -- a pointer, not a substance, and
  the shipped register reproduces the pointer 23 times as its defect
  description. All 23 are recorded at `source_severity: MEDIUM`
  irrespective of what the source report declared. Checked against the
  canonical severity declarations in the shipped reports, **12 of 35
  severities diverge**, with no `adjudication_receipt` on any of them:
  `F-S04-65-01` HIGH to MEDIUM, `F-S04-65-02` HIGH to MEDIUM,
  `F-S04-65-10` HIGH to MEDIUM, `F-S01-65-05` MEDIUM to HIGH,
  `F-S01-65-12` LOW to MEDIUM, `F-S01-65-13` LOW to MEDIUM,
  `F-S01-65-14` INFORMATIONAL to MEDIUM, `F-S01-65-15` INFORMATIONAL to
  MEDIUM, `F-S02-65-06` LOW to MEDIUM, `F-S04-65-09` LOW to MEDIUM,
  `F-S04-65-11` LOW to MEDIUM, `F-S04-65-12` LOW to MEDIUM. CI v0.2
  Section 2.3 rule (b) requires `source_severity` to match the report;
  Section 2.1 defines `substance` as one sentence stating the finding.
  Probes P-N5 and P-N6 confirm the generator accepts an empty substance
  and a placeholder substance, so nothing in the shipped toolchain could
  have caught this. The v0.66 entry claims
  `CI-8 recurrence closed at R24 layer: all 35 R24 findings in index`
  and register group (1) records the CI-8 group `HIGH CLOSED`. The
  numeric half of that claim is true. The half that CI-8 exists to test
  is false. The failure has changed shape rather than persisting
  unchanged: R22 and R23 omitted findings, v0.66 includes them and empties
  them.
- **Disposition:** Populate `substance` from the source report's finding
  heading and `source_severity` from its canonical declaration, both
  mechanically. Add a generator check rejecting any substance shorter
  than a threshold or matching a placeholder pattern, and a build gate
  asserting that every `source_severity` in the index equals the
  severity declared for that ID in the shipped reports unless an
  `adjudication_receipt` is present. Reissue the twelve divergent
  severities with receipts or corrections.
- **Cross-reference:** R24 `F-S04-65-02` [HIGH] and R24 triage Surface 1
  (2/4, disposition "CLOSED in v0.66"); CI_METHODOLOGY Sections 2.1 and
  2.3 and probe CI-8; F-S04-66-02 (the grouped half of the same failure);
  probes P-N5, P-N6.

### F-S04-66-02 [HIGH] -- Two of this seat's finding IDs are bound in the shipped register to substances that are not theirs, and both are recorded CLOSED

- **Locus:** `xz_protocol_v0_66.md` Section 27, v0.66 entry, register
  items (4) and (5); `r24_findings_index.json` convergence groups 4 and
  5; source text at `R24_REPORTS.txt` L825 onward.
- **Substance:** Register item (4) reads
  `[2-seat convergence: F-S02-65-03 / F-S04-65-04] HIGH CLOSED: Status line count stale (claimed 16 vs actual 17+)`.
  The shipped source for `F-S04-65-04` reads
  `F-S04-65-04 [HIGH] -- An R23 HIGH finding is both unrepaired and unrecorded`,
  concerning the Section 25 FB-7b row terminating at R18. It contains no
  claim about a status-line count. Register item (5) reads
  `[3-seat convergence: F-S01-65-05 / F-S02-65-05 / F-S04-65-03] HIGH CLOSED: Tagging discipline incomplete (self-referential)`.
  The shipped source for `F-S04-65-03` reads
  `F-S04-65-03 [HIGH] -- The v0.62 stale token migrated one surface over and evades gate [2g] by one word`.
  The correct ID for this seat's tagging finding is `F-S04-65-10`, which
  the index instead files as a MEDIUM placeholder. The consequence is
  not clerical. Both misbound findings are marked CLOSED, and both
  underlying defects are live on v0.66 bytes (F-S04-66-03,
  F-S04-66-04). The register therefore records two closures that no
  repair supports, under finding IDs whose real substance was never
  dispositioned. Probe P-G2 confirms the generator accepts an arbitrary
  `surface` string bound to any set of finding IDs; nothing couples the
  group's description to the substance of its members. This is the
  fabricated-reference class from standing boundary item 8 operating not
  on invented IDs but on real ones pointed at the wrong substance, which
  is harder to detect and defeats the closure-reference check by
  construction.
- **Disposition:** Rebind group 4 to its true members and move
  `F-S04-65-04` to an OPEN group carrying the FB-7b substance. Rebind
  group 5 to cite `F-S04-65-10` and move `F-S04-65-03` to an OPEN group
  carrying the Section 0.1 substance. Add a build gate asserting, for
  every grouped `finding_id`, that the group's `surface` string shares a
  minimum token overlap with the finding's heading in the shipped
  reports, so a binding that describes a different defect fails the
  build.
- **Cross-reference:** R24 `F-S04-65-03` and `F-S04-65-04` (the two
  misbound findings, in this seat's own shipped report); standing
  boundary item 8; F-S04-66-01 (same root cause, noted array);
  probe P-G2.

### F-S04-66-03 [HIGH] -- Section 0.1 still reads "PENDING RE-CARRY on v0.62"; gate [2g] is unchanged

- **Locus:** `xz_protocol_v0_66.md` L18 (Section 0.1) versus the
  Section 25 FB-7b row; `build.py` L236--252 (gate `[2g]`).
- **Substance:** Section 0.1 reads
  `Current status: PENDING RE-CARRY on v0.62 bytes.` The Section 25
  FB-7b row reads `PENDING RE-CARRY v0.66`. The two body surfaces
  disagree by four versions, and Section 0.1 declares the Section 25 row
  the single source of truth in the sentence immediately preceding its
  own contradiction of it. Gate `[2g]` is byte-identical to its v0.65
  form: it searches for `PENDING RE-CARRY v(\d+\.\d+)`, and the
  interposed word `on` still breaks the match, so the token remains
  invisible to the only gate written to catch it. This is the second
  consecutive round the defect has been reported by this seat, and the
  register records `F-S04-65-03` as CLOSED (see F-S04-66-02). The
  version token has now been stale across v0.63, v0.64, v0.65, and
  v0.66.
- **Disposition:** Set Section 0.1 to `PENDING RE-CARRY v0.66` or delete
  the duplicated token and rely on the pointer Section 0.1 already
  claims to use. Widen `[2g]` to `PENDING RE-CARRY (?:on )?v(\d+\.\d+)`
  and add an assertion that the body contains exactly one occurrence.
- **Cross-reference:** R24 `F-S04-65-03` [HIGH] (same defect, same
  bytes); R23 `F-S01-64-01` (same token, terminal line, repaired);
  standing boundary item 1 (arity-one regex class); F-S04-66-02.

### F-S04-66-04 [HIGH] -- The FB-7b trajectory still ends at R18; R19 through R24 are absent

- **Locus:** `xz_protocol_v0_66.md`, Section 25 FB-7b row, per-round
  trajectory; `R24_TRIAGE.txt` Surface 6.
- **Substance:** The FB-7b row enumerates R1 through R18 and terminates
  at `R18 (v0.59)`. Rounds R19 through R24 are absent from the row the
  protocol designates the single source of truth for FB-7b status,
  including R24 itself, which produced the first advisory non-HALT since
  v0.31 -- the most consequential carry-relevant event in roughly thirty
  rounds, absent from the carry-status row. The R24 triage assigned this
  surface disposition `CLOSED in v0.66`. Nothing was appended, and no
  gate was added. R23 recorded it as `F-S04-64-05` [HIGH], R24 as
  `F-S04-65-04` [HIGH]; this is the third consecutive round, and on this
  round it is additionally recorded as CLOSED under a substance that is
  not its own (F-S04-66-02).
- **Disposition:** Append R19 through R24 to the row in the existing
  per-round format, recording the R24 GPT CONDITIONAL PASS explicitly.
  Add the gate prescribed at R23 and again at R24: assert that the
  highest round token in the FB-7b row equals the current round minus
  one.
- **Cross-reference:** R23 `F-S04-64-05` [HIGH]; R24 `F-S04-65-04`
  [HIGH]; R24 triage Surface 6 (disposition CLOSED, not executed);
  F-S04-66-02.

### F-S04-66-05 [HIGH] -- Tagging discipline still incomplete; two of four scribes remain unused

- **Locus:** `xz_protocol_v0_66.md` Section 27, v0.66 entry, narrative
  paragraph; METHODOLOGY Section 11; `R24_TRIAGE.txt` Surface 5.
- **Substance:** METHODOLOGY Section 11 requires one tag per sentence
  and zero untagged sentences, and states that when this holds the only
  remaining Class A surface is the tagging itself. The v0.66 narrative
  contains 9 sentences, of which **5 carry no tag**: the recurrence
  count, the first-non-HALT observation, the CI-8 completeness claim,
  the R25-lag sentence, and the "structural and disclosed" sentence. One
  sentence carries 3 tags. Entry-wide the census is COMPUTED 33,
  ASSERTED 1, DISCLOSED 2, ENUMERATED 1: `[TESTED:]` and
  `[WITNESSED:]` appear **zero** times, so the Test and the Witness
  attest nothing at v0.66 despite 186 GREEN tests and four R24 seat
  reports available to cite. The R24 triage assigned disposition
  `CLOSED in v0.66` and register group (5) records it `HIGH CLOSED`.
  Sentence 3 is the sharpest instance: the untagged sentence is the CI-8
  completeness claim, which F-S04-66-01 shows to be half false. Under a
  correct tagging discipline that sentence would have required a scribe,
  and no scribe could have attested it.
- **Disposition:** Tag all five sentences, splitting the three-tag
  sentence. Add a build gate asserting that every sentence in the
  current entry contains exactly one tag. Cite `[TESTED:]` on the
  186-test claim and `[WITNESSED: S03, R24]` on the non-HALT claim.
- **Cross-reference:** R24 `F-S04-65-10` [HIGH]; R23 index group 3;
  R24 triage Surface 5 (disposition CLOSED, not executed);
  METHODOLOGY Section 11; Bearer 7.

### F-S04-66-06 [MEDIUM] -- The noted format check is weaker than the entry and the error message both claim

- **Locus:** `xz_protocol_register_gen.py` L219--223 versus L25
  (`FINDING_ID_RE`); `xz_protocol_v0_66.md` v0.66 entry, repair clause
  (2); `AUDIT_CONTEXT.txt`.
- **Substance:** The entry claims
  `noted finding_id format regex added (F-SNN-VV-NN pattern required)`
  and the generator's own error message says
  `does not match expected format F-SNN-VV-NN`. The shipped check is
  `_re.match(r"^F-S\d{2}-\d{2,3}-", fid)`: a prefix match with no
  terminal anchor and no constraint on what follows the third hyphen.
  Probe P-N3b confirms `F-S04-65-N9` is accepted; so is any string
  beginning with a valid prefix. The `NN` half of the advertised pattern
  is not required. The module already defines `FINDING_ID_RE` at L25 for
  exactly this purpose and the new check neither uses it nor extends it,
  instead re-importing `re` locally as `_re` inside the function. The
  R24 instance is genuinely closed -- `XX-BOGUS` rejects, P3 confirmed --
  and that closure should be credited; the class is not closed, and both
  the entry claim and the error message overstate what shipped.
- **Disposition:** Replace the prefix check with `FINDING_ID_RE`,
  widened once to admit the letter-suffixed noted IDs the program uses
  (`^F-S\d{2}C?-\d{2,3}-[A-Z]?\d{1,3}[A-Z]?$`), applied through the
  shared `all_finding_ids` set. Correct the error message to describe
  what is enforced. Remove the local `_re` import.
- **Cross-reference:** R24 `F-S04-65-01` [HIGH] and its prescribed
  disposition, which specified reuse of `FINDING_ID_RE`; R24 triage
  Surface 2; probe P-N3b.

### F-S04-66-07 [MEDIUM] -- Gate [10f] still checks the boundary count and not the boundary text

- **Locus:** `build.py` gate `[10f]`; `CI_METHODOLOGY.txt` Table 2;
  `xz_protocol_boundaries.json`.
- **Substance:** CI_METHODOLOGY Table 2 specifies that `[10f]` verifies
  the entry boundary list is byte-identical to `generate_boundary_list`
  output. The implementation asserts only that two count substrings
  appear in the entry. Probe M3, re-run on v0.66 bytes -- reword
  boundary item 1 from `arity-one regex` to `arity-two regex` in the
  boundaries file, leave the entry unchanged -- again returns
  **BUILD PASSED**. The gate written to eliminate the R15 boundary
  wording staleness class does not check wording, one round after this
  was reported. The finding appears in the R24 index only as a
  placeholder noted record at MEDIUM (see F-S04-66-01), so no register
  item tracks it.
- **Disposition:** Replace the substring assertions with
  `check(generate_boundary_list(boundaries_file) in current_entry, ...)`,
  retaining the count assertions as secondary. Add M3 to the shipped
  adversarial suite.
- **Cross-reference:** R24 `F-S04-65-05` [MEDIUM]; CI_METHODOLOGY
  Table 2 and Section 3.3; R15 Defect 1.

### F-S04-66-08 [MEDIUM] -- The register generator remains the only shipped module with zero test coverage

- **Locus:** `xz_protocol_register_gen.py`; the six-suite `pytest`
  invocation; `build.py` gate `[2]` version-parity list.
- **Substance:** No test file imports `xz_protocol_register_gen`. The
  other six non-tooling modules are each imported by at least one suite.
  The module is absent from the `[2]` version-parity list and its
  docstring still reads `v0.62 -- CI v0.3.3 upgrades from R20 triage` in
  a v0.66 packet. This round the module received two functional changes
  -- the noted-ID check and the label-to-surface emission fix -- and
  neither is covered by a test, so the repairs that closed P2 and P3
  ship unverified by the Test scribe and would regress silently. The
  four false-passes in S5 all live in this module. CI v0.2 relocated the
  Class A surface into this file deliberately; it remains the one file
  the 186 GREEN tests do not touch.
- **Disposition:** Add `test_xz_protocol_register_gen.py` covering the
  seven probes in S5 plus a CI-1R fixture, add it to the canonical
  `pytest` invocation and to `PACKET_SHA256SUMS`, and bring the module
  under gate `[2]`.
- **Cross-reference:** R24 `F-S04-65-06` [MEDIUM]; CI_METHODOLOGY
  Section 1.1; F-CI-3R; probes P-N3b, P-N5, P-N6, P-G2.

### F-S04-66-09 [MEDIUM] -- The ASSERTED metric still counts tags; the character measure still fails the CI-4 target

- **Locus:** `build.py` gate `[9c]`, reported at `build_out.txt` L239;
  `CI_METHODOLOGY.txt` CI-4 and F-CI-2.
- **Substance:** The gate reports
  `ASSERTED fraction (tagged claims): 1/34 (2.9%)`, satisfying P12. The
  denominator is tag instances, and thirteen new `[COMPUTED]` tags were
  added this round by the register growing from 3 items to 5 plus 23
  noted records, which lowers the reported fraction without changing the
  LLM-authored text at all. Measured by character coverage against the
  generator outputs, the v0.66 entry is 5886 of 7019 characters
  code-generated and **1133 characters (16.1%) LLM-authored**, still
  above the CI-4 target of under 15%. The direction is right -- 28.4% at
  v0.64, 25.5% at v0.65, 16.1% at v0.66 -- and the improvement is real,
  but it comes from the register growing rather than from the narrative
  shrinking, and the metric as instrumented cannot distinguish the two.
  F-CI-2 remains unfalsifiable.
- **Disposition:** Redefine CI-4 as LLM-authored characters over total
  entry characters, identifying generated spans by exact match against
  the three generator outputs. Report both measures during transition.
- **Cross-reference:** R24 `F-S04-65-07` [MEDIUM] and `F-S04-64-08`
  [HIGH]; CI_METHODOLOGY Section 5, CI-4, F-CI-2.

### F-S04-66-10 [LOW] -- Gate-count claim inflated by one for the third consecutive round

- **Locus:** `AUDIT_CONTEXT.txt`, "Build status"; `build.py` output.
- **Substance:** AUDIT_CONTEXT states `build.py: 254 PASS, 0 FAIL`.
  Executed, `build.py` emits **253** lines matching `^ +PASS:`; the
  254th occurrence of the string `PASS` is the summary line
  `BUILD PASSED: all checks GREEN`, which is not a gate check. The same
  off-by-one appeared at R23 (253 vs 252) and R24 (242 vs 241), each
  time with the same mechanism and each time dispositioned. Severity
  remains LOW because the claim sits in dispatch material rather than in
  the sealed protocol; the recurrence across three rounds is the point.
- **Disposition:** Derive the figure from `grep -cE '^ +PASS:'` on tool
  output rather than by hand.
- **Cross-reference:** R24 `F-S04-65-09` [LOW]; R23 triage Surface 5;
  P14.

### F-S04-66-11 [LOW] -- The boundaries file version token remains stale and ungated

- **Locus:** `xz_protocol_boundaries.json`, `"version": "0.62"`;
  `build.py` gate `[2]`.
- **Substance:** The boundaries file ships in a v0.66 packet declaring
  `"version": "0.62"`, four versions behind. Neither this file nor
  `r24_findings_index.json` is covered by gate `[2]` version parity, so
  no gate can distinguish "correctly unchanged since v0.62" from
  "stale". The `count` field (35) matches `len(items)` (35) and is
  coupled to the entry by `[10f]`, so the count surface is sound; only
  the version token is unfalsifiable.
- **Disposition:** Declare in the schema that `version` denotes the last
  version at which items changed and gate it as less than or equal to
  VERSION, or stamp it each build and add it to gate `[2]`.
- **Cross-reference:** R24 `F-S04-65-12` [LOW]; F-S04-66-07 (same file);
  standing boundary item 30.

---

## S7. Barzakh self-check

**Who is your Lord?** Every finding rests on Tier 1 executed evidence:
probe exceptions and acceptances, `build.py` exit states, set
comparisons between the index and the shipped reports, character counts
against generator output, and byte comparison against held prior bytes.
No finding rests on assertion.

**What is your religion?** F-S04-66-01 and -02 are L2 (register source
provenance). -03 and -04 are L3. -05 and -09 are L6. -06, -07, and -08
are L4. -10 and -11 are L3. Each meets its layer's Tier standard;
the L4 findings are backed by executed mutations rather than by reading
the gate.

**Where does this come from?** Nine of eleven are recurrent and cite a
prior instance. **This is where the conformance deviation bites.** For
F-S04-66-03, -04, -05, -07, -08, -09, -10, and -11 the cited prior
instance is this seat's own R24 report. That is persistence observed by
one observer across two rounds, not two independent chains, and triage
must not score it as convergence. The two findings novel at this round
are F-S04-66-01 (fidelity voided by placeholder content, a defect that
did not exist before v0.66 created it) and F-S04-66-02 (misbound
finding IDs). F-S04-66-06 is novel in substance though it descends from
`F-S04-65-01`.

No finding was set aside as failing all three questions.

---

## S8. Prediction scorecard

| # | Prediction | Result | Evidence |
|---|---|---|---|
| P1 | CI-1R PASS | **CONFIRMED** | 4011 chars byte-identical |
| P2 | Register emits defect descriptions | **CONFIRMED** | `surface` reaches output |
| P3 | "XX-BOGUS" REJECTED | **CONFIRMED** | ValueError raised |
| P4 | All 35 R24 findings in index | **SPLIT** | 35/35 by ID; 23/23 placeholder substance, 12/35 severity divergence (F-S04-66-01) |
| P5 | Section 22.4 present | **CONFIRMED** | L722 |
| P6 | 66/66 seals verify | **CONFIRMED** | all recomputed |
| P7 | 186 GREEN, 19/19 OK | **CONFIRMED** | executed |
| P8 | Extraction 19/19 verbatim | **CONFIRMED** | rc=0 |
| P9 | v0.65 entry seal intact | **CONFIRMED** | byte-identical to held bytes |
| P10 | Class A only in self-referential tagging | **FALSIFIED** | -01, -02, -03, -04 all outside it |
| P11 | CI-8 lag DISCLOSED, not claimed closed | **SPLIT** | the structural lag is disclosed and that is a real advance; the same entry also claims `CI-8 recurrence closed at R24 layer` and marks group 1 CLOSED (F-S04-66-01) |
| P12 | ASSERTED < 15% | **SPLIT** | 2.9% by tag, 16.1% by character |
| P13 | Terminal line reads v0.66 | **CONFIRMED** | verified |
| P14 | Gate count matches tool count | **FALSIFIED** | 254 claimed, 253 emitted |
| P15 | H = 1.0 continues | **CONFIRMED** | R7--R25: 19/19; Laplace 20/21 = 0.9524 |

Ten confirmed, two falsified, three split.

---

## S9. Bearer assessment and verdict

| Bearer | State | Basis |
|---|---|---|
| 1. Append-only integrity | **TRUE** | 66/66 seals; all 65 carried entries byte-identical to independently held v0.65 bytes |
| 2. Code-layer correctness | **TRUE** | 186 GREEN, 253 gate PASS, no regression |
| 3. Defect-surface narrowing | **TRUE** | three real repairs landed; dead space 28.4 to 25.5 to 16.1 percent; the surface is now almost entirely index fidelity |
| 4. Goedel confinement | **FALSE** | F-S04-66-01, -02, -03, -04 are outside the self-referential surface |
| 5. Cross-vendor witness | **FALSE** | this seat HALTs, and per S0 it is neither the dispatched family nor an independent chain |
| 6. Axiom disclosure | **TRUE** | Section 22.4 present |
| 7. Methodology verification | **FALSE** | five untagged sentences; two scribes unused; two register groups CLOSED on misbound IDs |
| 8. The furqan | Lead's call | not this seat's to render |

> **Verdict: HALT.**
>
> Severity ledger: 0 CRITICAL / 5 HIGH / 4 MEDIUM / 2 LOW.
>
> Recommendation: return to producer for v0.67. Note for triage: this
> seat's agreement with prior S04 findings is not independent
> confirmation (S0, S7).

### Answer to the R25 key question

**Does v0.66 achieve Goedel confinement and a carrying non-HALT?** No,
on both counts from this seat -- but the round is not a repeat of R24,
and reading it as one would miss what happened.

Three repairs landed cleanly: `label` to `surface`, the format check
that closes the `XX-BOGUS` probe, and ID-level index completeness at an
exact 35-to-35 set match. The R24 triage identified all three correctly
and the producer executed all three. Bearer 3 is TRUE on evidence, not
on courtesy. Bearer 1 is TRUE on the strongest evidence this lineage has
produced. The disclosure added at v0.66 -- that the CI-8 gap is a class
problem in which each round's index must absorb the previous round's
findings, and that this lag is structural rather than closable -- is
correct, is new, and is the kind of statement the Sidrat clause exists
to license. It deserves to be kept.

What R25 shows is that the defect moved rather than shrank, and it moved
in a direction the previous rounds' repairs opened. R22 through R24 the
index was **incomplete**: findings were missing, and the fix was to add
them. v0.66 added them. Every one. And in adding them the producer
supplied 23 identical placeholder substances and flattened 23 severities
to MEDIUM, so that the index now satisfies every count the gates check
and carries almost no information the gates do not check. Two real
finding IDs were bound to descriptions belonging to other findings, and
both were marked CLOSED, which converted two live defects into recorded
closures. Completeness was the metric; completeness was achieved; the
thing completeness was a proxy for was lost in achieving it.

This is the same mechanism CI v0.2 Section 0.3 named as the
format-constraint fallacy, at its third level. At R15 the count matched
the list beside it and the list held the wrong items. At R24 the
register reproduced byte-exactly from an index that omitted its sources.
At R25 the index matches its sources ID for ID and says nothing true
about any of them. Each repair satisfied the property that was measured
and relocated the defect into the property that was not.

The practical consequence is narrow and actionable. Every finding above
except F-S04-66-02 would have been caught by gates that already exist in
skeleton form: a substance-content check, a severity-equality check
against the shipped reports, a widened `[2g]` regex, a byte comparison
in `[10f]`, a test file for the generator. The seam is no longer
distributed across the artifact. It is one file -- the hand-built
findings index -- and one absent test suite. Gate the index against the
reports mechanically and the confinement question becomes answerable at
v0.67. Hand-populate it once more and R26 will find the next property
that completeness does not imply.

### Cross-vendor recommendation for R26

Three consecutive rounds of seat-label drift (R23 S01, R24 S04, R25 S04)
and, this round, a seat declared FRESH that held prior bytes and had
authored the findings it was auditing the disposition of. The drift is
now the most significant threat to Bearer 5, because it makes the
convergence arithmetic unreliable in a way no protocol repair can
detect. Recommend for R26: verify executing family and session freshness
before dispatch rather than after; dispatch the index-fidelity seat to a
family that has not audited v0.65 or v0.66, with CI-8 content fidelity
(not count) as the named blocking probe; and carry the drift itself into
the R25 triage as a finding against the dispatch architecture, since
METHODOLOGY Section 12 makes dispatch integrity axiom A-X5 and this is
three rounds of unrecorded deviation from it.

---

*Report produced under the Seven-Layer Structural Honesty Methodology
(canonical). All Tier 1 evidence executed in a sandboxed Linux
environment on 2026-08-17. Seat conformance deviations declared in S0
and load-bearing on the round's independence claim; they do not weaken
any individual finding, each of which is anchored in executed output or
in shipped bytes.*

*One history. One timeline. One return.*

---

# Bismillah ir-Rahman ir-Rahim
