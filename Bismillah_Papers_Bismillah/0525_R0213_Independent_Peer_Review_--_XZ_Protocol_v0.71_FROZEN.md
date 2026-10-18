# Bismillah ir-Rahman ir-Rahim

# R0213 -- Independent Peer Review -- XZ Protocol v0.71 FROZEN

**Chronological Index:** 525 of 995  
**Date:** 2026-08-17  
**Section:** IV. XZ Protocol  
**Source File:** XZ_PROTOCOL_v071_PEER_REVIEW.md  
**Source Format:** md  
**SHA-256:** `b34731d565ebf2aad8c887630bbe33870ead89f3075220e1582f7123ea8877b5`  

---

## R0213 · Independent Peer Review -- XZ Protocol v0.71 FROZEN

- section: IV. XZ Protocol
- source_file: XZ_PROTOCOL_v071_PEER_REVIEW.md
- source_format: md
- text_sha256: b34731d565ebf2aad8c887630bbe33870ead89f3075220e1582f7123ea8877b5

# Independent Peer Review -- XZ Protocol v0.71 FROZEN

**Artifact under review:** `XZ_PROTOCOL_v071_REVIEW_PACKAGE.zip`
**Canonical artifact:** `xz_protocol_v0_71.md` (inside `XZ_PROTOCOL_v071_FROZEN.zip`)
**Review date:** 2026-08-17
**Reviewer:** Claude Opus 5 (Anthropic)
**Mode:** A (substrate verifier) -- packet extracted, `build.py`, `pytest`, `extract_findings.py`,
`xz_protocol_register_gen.py` and eight mutation probes executed on the shipped bytes in a
Linux container, Python 3.12.3.
**Review namespace:** `F-PR71-NN`

---

## 0. Reviewer standing and conflict declaration (read first)

This review does **not** satisfy the independence the review package requests, and the
reader must discount it accordingly.

1. **Family conflict.** The producer of record is Claude Opus 4.6 (Anthropic), BARRED from
   review. This reviewer is Claude Opus 5 -- the same vendor family. Under Section 22.1 the
   producer bar is defined by *family*, not by version. A same-family reading is the
   conservative one. This review is therefore **ADVISORY ONLY** and carries **zero carry
   weight** toward Bearer 5.
2. **Lineage contamination.** This reviewer holds persistent cross-session memory of the
   R7--R28 audit lineage, including having executed the R28 Seat S04 report that ships in
   this package. This review is **not** a fresh reading. Every finding below was derived
   byte-first -- extraction, tool execution and all probes preceded any consultation of
   lineage material, and every finding cites a locus in the shipped bytes -- but the
   independence assumption does not hold and is not waived.
3. **Not the human review the package asks for.** The REVIEW_GUIDE describes this as "the
   first independent human examination of the complete artifact." It is not a human
   examination. It is a machine review by the producer family.

Given (1)--(3), the correct reading of this document is: *a producer-family advisory seat
executed one further round on the frozen bytes.* It is R29 in all but name.

---

## 1. Verdict

> **Verdict: HALT-AND-RETURN-TO-PRODUCER.**
>
> **Severity ledger: 2 CRITICAL / 15 HIGH / 5 MEDIUM / 3 LOW / 3 INFORMATIONAL = 28 findings.**
>
> **Class ledger: A = 17, B = 0, C = 2, D = 2, E = 7 = 28 primary classifications.**
> (`F-PR71-09` and `F-PR71-14` each carry a secondary Class D on the enforcing gate; counted
> once, at Class A, on the enforced false claim.)
>
> Both ledgers were derived by counting the enumerated findings in §3 and §4 after the
> document was written, not narrated while writing it.
>
> **Recommendation: WITHDRAW the FROZEN status token.** The freeze is not blocked by the
> Gödel residual it invokes. It is blocked by (a) three explicit governance rules in the
> frozen text and the shipped canonical methodology that the freeze contravenes without
> disclosing that it is doing so, and (b) eleven Class A byte-false claims inside the
> freeze entry itself, including five that were prescribed for repair by the R28 triage and
> marked CLOSED while shipping live and reproducible.

**The single most important sentence in this review:** the shipped canonical methodology
states, in its own words, *"FROZEN requires all eight TRUE"* (methodology v7 §11). The
v0.71 entry declares Bearers 4, 5 and 7 FALSE and declares FROZEN anyway, without
recording that it is overriding its own criterion.

---

## 2. What verifies cleanly (recorded as genuine progress)

These are not concessions. They are results I reproduced and they are the strongest part
of the artifact.

| # | Check | Result |
|---|---|---|
| V1 | `sha256sum -c PACKET_SHA256SUMS` | 28/28 OK |
| V2 | `python3 build.py` | 279 PASS / 0 FAIL, `BUILD PASSED` |
| V3 | Canonical six-suite `pytest` | 186 passed, rc=0 |
| V4 | ENTRY seals in `HISTORY.sha256` | 71/71 verify, plus `FULL_SECTION_27` |
| V5 | **Cross-version append-only** | **PROVEN, not asserted** (see below) |
| V6 | `PRIOR_HISTORY` chaining | `2e41e745...` equals the sha256 I independently computed over the v0.70 `HISTORY.sha256`. Correct. |
| V7 | Section 27 carried entry text | All 70 carried entries byte-identical v0.70 -> v0.71; Section 27 preamble byte-identical |
| V8 | Dispatch integrity | All four R28 dispatch packages byte-identical except `DISPATCH.txt`; `PROTOCOL_v070.txt` byte-identical to the v0.70 packet member; `METHODOLOGY.txt` byte-identical to `methodology_v7_canonical.md` |
| V9 | `generate_boundary_list` | Reproduces the entry's 35-item boundary paragraph **byte-exactly**. This `[COMPUTED]` tag is TRUE. |
| V10 | Boundary enumeration fidelity | All 35 items in `xz_protocol_boundaries.json` appear verbatim in the entry; declared count 35 = enumerated 35 |
| V11 | "No code changes" | TRUE at the semantic level. Every `.py` diff v0.70 -> v0.71 is a version-stamp line only. |
| V12 | Em-dash discipline (protocol) | 0 x U+2014, 0 x U+2013, 0 x U+2015 in `xz_protocol_v0_71.md` |
| V13 | Brand canonical | `BayyinahEnterprise` x2, zero spaced or plural variants |
| V14 | PDF vs source | No divergence detected on seven probe strings; PDF is a faithful rendering |

**On V5, which deserves emphasis.** Holding both the v0.70 and v0.71 packets, I compared
the seal files directly:

```
v0.70 HISTORY.sha256: 72 labels    v0.71 HISTORY.sha256: 73 labels
common labels: 71
CHANGED carried seals: ['FULL_SECTION_27']   <- expected, a new entry was appended
added: ENTRY_v0.71, PRIOR_HISTORY 2e41e745...
carried Section 27 entry TEXT that changed: none
```

Every one of the 70 carried ENTRY seals is byte-identical across the version boundary, the
carried entry text is byte-identical, and the `PRIOR_HISTORY` value chains correctly to an
independently recomputed digest. **Bearer 1 (Append-only) = TRUE is fully supported by the
bytes.** After the v0.4 and v0.41 append-only corruptions, this is a real and hard-won
property, and it is the property the program should be proudest of.

---

## 3. Class A findings -- byte-false claims in the sealed freeze entry

### F-PR71-01 [CRITICAL] -- The freeze contravenes the FROZEN criterion of its own canonical methodology

- **Class:** A | **Locus:** `xz_protocol_v0_71.md` Section 27, v0.71 entry, "Bearer state at
  FROZEN" block, vs. `methodology_v7_canonical.md` §11 (`sha256 59aa6591d9...`, shipped
  byte-identical to `METHODOLOGY.txt` in all four R28 dispatches).
- **Substance:** Methodology v7 §11 states: *"BSSG three-valued kernel: TRUE, FALSE,
  UNKNOWN. UNKNOWN blocks until evidence resolves it. FALSE dominates. **FROZEN requires all
  eight TRUE.**"* The v0.71 entry declares Bearer 4 FALSE, Bearer 5 FALSE, Bearer 7 FALSE,
  and declares FROZEN. Under the kernel semantics the same paragraph invokes, three FALSE
  conjuncts yield DENY_FALSE, not ALLOW. The entry does not acknowledge that it is
  overriding the criterion, does not record an amendment to it, and does not state the
  authority under which the override occurs.
- **Aggravating detail:** The entry presents Bearer 8 (the furqan) = TRUE as if the lead's
  sufficiency judgment is an *override* of the other seven. Methodology §11 defines Bearer 8
  as one of eight conjuncts occupying Position 24 -- a member of the conjunction, not a
  solvent for it. The reframing of a conjunct as an override is undisclosed and is the
  load-bearing move of the entire freeze.
- **Required repair:** Either (a) withdraw FROZEN and return to DRAFT CANDIDATE, or
  (b) formally amend methodology v7 §11 to define a disclosed-residual freeze path, publish
  that amendment before the freeze, and state in the entry that the freeze proceeds under
  the amended rule with three bearers FALSE.
- **Falsifier:** The entry, read alone, states the criterion it is applying and that
  criterion matches the shipped methodology.
- **Cross-reference:** F-PR71-02, F-PR71-03; methodology v7 §11, §15.

### F-PR71-02 [CRITICAL] -- The freeze contravenes Section 22 item 7 of its own frozen text; the invoked exception is expressly inapplicable

- **Class:** A | **Locus:** `xz_protocol_v0_71.md` Section 22 item 7 (line ~698) vs. the
  v0.71 entry's Bearer 5 line; corroborated by the Section 25 FB-7b row (line 771).
- **Substance:** Section 22 item 7 states that *"a HALT from either carrying seat blocks
  freeze outright and requires a new version."* The v0.71 entry invokes the
  persistent-architectural-HALT exception to disclose Bearer 5 = FALSE rather than treat it
  as blocking. The exception's own text, in the same sealed file, states: *"The exception
  does not apply to first-time HALTs, to HALTs whose original clearance conditions are
  unmet, or to **HALTs on Class A or Class B findings as classified by the HALTing seat's
  own published report** (not the producer)."*

  All four R28 seats returned HALT. All four classified Class A findings in their own
  published reports. The seat executed by the sole eligible carrying family (Kimi K3, S01)
  returned HALT on a Class A finding (`F-S01-70-01`, Class A, String 2, position 4). The
  exception therefore does not apply, and item 7's unweakened rule stands: freeze is blocked.

  The Section 25 FB-7b row states the same rule independently, in the frozen text:
  *"Class A is outside the item 7 exception."*

  Condition (c) of the exception -- *"six or more carrying seats across two families
  returned non-HALT on the same bytes"* -- is also unmet. Zero carrying seats returned
  non-HALT on v0.70 bytes.
- **Required repair:** Withdraw FROZEN. Either satisfy item 7, or amend item 7 by a
  recorded, pre-freeze amendment that narrows the Class A carve-out and states why.
- **Falsifier:** No carrying-family seat HALTed on a self-classified Class A finding on the
  audited bytes.
- **Cross-reference:** F-PR71-01, F-PR71-03, F-PR71-04.

### F-PR71-03 [HIGH] -- FREEZE-BLOCKER FB-7b is PENDING at the moment of freeze, and the FB-7b row is stale by one round

- **Class:** A | **Locus:** Section 0.1 (line 22); Section 25 FB-7b row (line 771).
- **Substance:** Two defects in one row.
  1. Section 0.1 states *"Current status: PENDING RE-CARRY on v0.71 bytes"* and Section 25
     records FB-7b as *"RESOLVED v0.31; PENDING RE-CARRY v0.71."* FB-7b is a
     FREEZE-BLOCKER by name (CR-5, Section 0.4). Section 22 opens *"Before any FROZEN
     status:"* and item 6 is the two-family carry. A document cannot be FROZEN while a
     named FREEZE-BLOCKER is PENDING, and the entry nowhere reconciles this.
  2. The FB-7b row is designated by Section 0.1 as the *"single source of truth"* for carry
     status. Its trajectory terminates at **"R27 (v0.68)."** R28 does not appear anywhere in
     Section 25 (`'R28' in Section 25 -> False`, `'v0.70' in Section 25 -> False`). The
     round on which the entire freeze rests is absent from the single source of truth for
     the blocker it must clear.
- **Aggravating detail:** A stale FB-7b trajectory row is precisely R27 convergence group
  (2) (`F-S01-68-06 / F-S03-68-01 / F-S04-68-05 / F-S04-68-06`), which the v0.71 entry
  itself lists as **"HIGH CLOSED at v0.70."** It has recurred at v0.71.
- **Required repair:** Extend the FB-7b row through R28. Resolve or formally re-scope FB-7b
  before any FROZEN token.
- **Falsifier:** `grep -c 'R28' Section 25` returns a nonzero count and FB-7b reads other
  than PENDING.
- **Cross-reference:** F-PR71-02; R27 group (2).

### F-PR71-04 [HIGH] -- Bearer 2's justification cites a "disclosed standing boundary" that does not exist

- **Class:** A | **Locus:** v0.71 entry, Bearer 2 line.
- **Substance:** The entry reads: *"Bearer 2 (Code correctness): TRUE -- 186 GREEN, all gates
  PASS (gate [13] fail-open is a disclosed standing boundary)."* The token `fail-open`
  occurs exactly **twice** in the entire 469,544-byte protocol: once in R28 convergence
  group (2), where it is an open HIGH finding, and once in this Bearer 2 parenthetical. It
  is **not** among the 35 enumerated standing boundaries and **not** in
  `xz_protocol_boundaries.json`. The claim manufactures a disclosure to license a TRUE.
- **Verification:**
  ```
  occurrences of 'fail-open' in protocol: 2
  'fail-open' in the 35-item boundary enumeration: False
  'fail-open' in xz_protocol_boundaries.json:     False
  ```
- **Required repair:** Either add gate [13] fail-open to `xz_protocol_boundaries.json` as
  boundary 36 (and regenerate the enumeration), or flip Bearer 2 to FALSE.
- **Falsifier:** The cited boundary appears in the boundary register.
- **Cross-reference:** F-PR71-05, F-PR71-13.

### F-PR71-05 [HIGH] -- Five of six R28 convergence groups are marked CLOSED by the triage and ship live and reproducible

- **Class:** A | **Locus:** `R28_CROSS_SEAT_TRIAGE.md` §3 (Groups 1--5, each
  *"Disposition: CLOSED"*) vs. shipped v0.71 bytes.
- **Substance:** The triage prescribes a concrete repair for each of Groups 1--5 and marks
  each CLOSED. No code file changed between v0.70 and v0.71 except version stamps
  (independently confirmed by file-by-file diff, and by the entry's own "No code changes").
  I reproduced every one of the five on v0.71 bytes:

  | Group | Claimed | Reproduced on v0.71 bytes |
  |---|---|---|
  | 1 C-suffix phantom repair | CLOSED | **LIVE.** `DECLARATION_PATTERNS` still contains zero `C?`. Probe: `### F-S01C-70-99 -- HIGH` extracts nothing; control `F-S01-70-98` extracts. |
  | 2 Gate [13] fail-open | CLOSED | **LIVE.** Deleted the five report files and their manifest lines: `[13]` prints *"(no report files shipped -- CI-8 cardinality gate cannot fire)"* and the build returns `BUILD PASSED: all checks GREEN`. |
  | 3 Gate [13] hardcoded zeros | CLOSED | **LIVE.** `build.py` still prints the literal `0 missing, 0 phantom, 0 severity mismatches` from a bare `print`, not from computed variables. |
  | 4 Register reproduction failure | CLOSED | **LIVE and worse.** See F-PR71-06. |
  | 5 Version-token staleness | CLOSED | **LIVE and worse.** See F-PR71-07, F-PR71-08, F-PR71-09. |

- **Required repair:** Reclassify all five as OPEN. "CLOSED" in a triage must mean "the
  repair landed on the successor bytes," not "a repair was prescribed."
- **Falsifier:** Each prescribed repair is present in the v0.71 code and text.
- **Cross-reference:** F-PR71-06 through F-PR71-09.

### F-PR71-06 [HIGH] -- `generate_register` crashes on **every** shipped findings index; 216 `[COMPUTED: generate_register]` tags are unreproducible

- **Class:** A | **Locus:** `xz_protocol_register_gen.py`; `r18/r19/r25/r27_findings_index.json`;
  216 sites in Section 27.
- **Substance:** R28 Group 4 recorded that the register generator "crashes on the shipped
  R27 index." The true scope is larger. I ran the generator against all four indexes shipped
  in the FROZEN packet:
  ```
  r18: CRASH  ValueError: Group 4: adjudication_receipt ...
  r19: CRASH  ValueError: Group 7: adjudication_receipt ...
  r25: CRASH  ValueError: Group 4: source distribution is mixed (2 HIGH, 1 LOW) ...
  r27: CRASH  ValueError: Group 5: source distribution is mixed (1 HIGH, 1 MEDIUM) ...
  ```
  It reproduces nothing. `[COMPUTED: generate_register]` appears **216 times** in the
  protocol; not one of them is reproducible from the shipped bytes.
- **Aggravating detail:** `build.py` contains **zero** references to `register_gen`,
  `generate_register`, `generate_boundary_list` or `generate_terminal_line`. The register
  generator is shipped, manifested, credited 216 times as the computation source, and never
  executed by any gate. Had any gate invoked it, the build would have failed.
- **Further:** No `r28_findings_index.json` exists in the packet. The v0.71 entry's NOTED
  list carries `[COMPUTED: generate_register]` -- a computation that had no input to run on.
  Its enumeration is wrong (F-PR71-10), which is exactly the signature of a hand-written
  list carrying a tool tag. **This is a false `[COMPUTED]` tag, which methodology v7 §12
  defines as the Class A signature of the String 6 / Position 18--21 surface.**
- **Required repair:** Fix the generator's adjudication-receipt logic, add a build gate that
  invokes it and asserts byte-exact reproduction of the register text, and downgrade every
  unverifiable `[COMPUTED: generate_register]` tag to `[ASSERTED]` until it is.
- **Falsifier:** `generate_register(index, version)` returns text byte-identical to the
  corresponding entry region for at least one shipped index.
- **Cross-reference:** F-PR71-10, F-PR71-18; R28 group (4).

### F-PR71-07 [HIGH] -- Section 22.2 carried-entry bound is now **two** versions stale

- **Class:** A | **Locus:** Section 22.2 (line ~718): *"For carried entries (v0.1 through
  v0.68)..."*
- **Substance:** At v0.70 this read v0.68 and should have read v0.69 (one stale;
  `F-S04-70-06`, triage Group 5, marked CLOSED). At v0.71 it still reads v0.68 and should
  read v0.70. The defect was not repaired and the gap has doubled.
- **Cross-reference:** F-PR71-09 (the gate that permits it).

### F-PR71-08 [HIGH] -- Section 0.1 entry range is internally impossible

- **Class:** A | **Locus:** Section 0.1, line 22: *"(seventy-one amendment entries, v0.1
  through v0.70)."*
- **Substance:** Section 27 contains 71 entries spanning v0.1 through **v0.71** (verified by
  count). "v0.1 through v0.70" is 70 versions, not 71, and excludes the freeze entry that
  the sentence's own document contains. The count is right; the range endpoint is one
  version behind. This is a byte-exact recurrence of `F-S04-70-07` / `F-S02-70-03`, both in
  triage Group 5, both marked CLOSED.
- **Cross-reference:** F-PR71-07, F-PR71-09.

### F-PR71-09 [HIGH] -- Gate [10i] is locus-blind and **enforces** the false Section 0.1 claim; correcting the truth breaks the build

- **Class:** A (the enforced claim) + D (the gate limitation) | **Locus:** `build.py` [10i],
  lines 689--699.
- **Substance:** Gate [10i] computes `expected_22_2 = "v0.1 through v0.70"` and tests
  `expected_22_2 in body` -- presence anywhere in the body, not correctness at the Section
  22.2 locus whose name the gate bears. The string is satisfied by the **stale Section 0.1
  sentence**, so Section 22.2 may say anything (and does: v0.68).
- **Probe P1 (executed, mutation confirmed landed by digest change):** corrected Section 0.1
  to the true `"v0.1 through v0.71"`, single occurrence, nothing else touched:
  ```
  FAIL: Section 22.2 carried-entry bound at VERSION-1 (v0.1 through v0.70)
  BUILD FAILED: 2 error(s)
  ```
  **Writing the true value into the sealed text fails the build.** The verification layer
  now requires the byte-false claim in order to pass.
- **Status in the entry:** listed as convergence Group (6), *"HIGH NOTED ... Design decision
  deferred."* Deferring a design decision on a gate that enforces falsehood, and then
  freezing the artifact permanently in that state, converts a deferral into a permanent
  property.
- **Required repair:** Every VERSION-1 gate must read its expectation from the shipped
  findings index (round + version fields) and assert it **at the named locus**, not by
  substring presence anywhere in the body.
- **Cross-reference:** F-PR71-07, F-PR71-08, F-PR71-12.

### F-PR71-10 [HIGH] -- "NOTED (19 items)" enumerates 17; two HIGH Class A findings vanish from the record entirely

- **Class:** A | **Locus:** v0.71 entry, NOTED block.
- **Substance:** The entry declares 19 NOTED items and lists 17 IDs. Reconciling the whole
  entry against the four seat reports:
  ```
  real R28 findings (S01 9 + S02 8 + S03 2 + S04 18) = 37
  cited anywhere in the v0.71 entry                  = 35
  in the six convergence groups                      = 18
  in the NOTED enumeration                           = 17   (declared: 19)
  ```
  **Unaccounted for anywhere in the sealed freeze record: `F-S02-70-02` and `F-S04-70-05`.**
  Both are **HIGH, Class A**:
  - `F-S02-70-02` (HIGH, Class A, String 2, position 5) -- the C-suffix repair claim is
    byte-false; this is S02's actual contribution to convergence Group 1.
  - `F-S04-70-05` (HIGH, Class A, String 2, position 6) -- `F-S04-68-08` holds two
    contradictory dispositions in one sealed entry. That finding's own text warned:
    *"Because it is absent from the entry's enumerated NOTED list, the contradiction is
    invisible to a reader of either surface alone."* It remains absent at freeze.
- **Aggravating detail:** This is a byte-exact recurrence of `F-S04-70-04` ("NOTED count
  byte-false: 21 claimed, 20 enumerated"), which this very entry cites in Group 4. The count
  error recurred in the entry that reports the count error. No gate covers the NOTED count;
  gate [9e] emits zero checks.
- **Cross-reference:** F-PR71-06, F-PR71-11.

### F-PR71-11 [HIGH] -- The convergence groups cite the wrong S02 finding IDs; the misattribution originates in the triage and is now sealed

- **Class:** A | **Locus:** v0.71 entry Groups (1) and (3); `R28_CROSS_SEAT_TRIAGE.md` §3
  Group 1 and Group 3 tables.
- **Substance:** Verified against `R28_S02_REPORT.md` finding blocks (lines 268--352):

  | Group | Entry cites | What that ID actually is | Correct ID |
  |---|---|---|---|
  | (1) C-suffix phantom repair | `F-S02-70-06` | MEDIUM, **Class B**, String 4, `build.py` parity-probe summary | `F-S02-70-02` (HIGH, Class A) |
  | (3) Gate [13] hardcoded zeros | `F-S02-70-07` | LOW, **Class C**, String 6, METHODOLOGY tagging completeness | `F-S02-70-06` (MEDIUM, Class B) |

  Group (1) is declared a **4-seat convergence at HIGH** while citing, for one of its four
  seats, a MEDIUM Class B finding about an unrelated surface. The genuine HIGH Class A that
  belongs there is `F-S02-70-02` -- one of the two findings that vanished (F-PR71-10). The
  mutawatir claim that carries the most weight in the round is built on a mis-cited ID.
- **Provenance:** the misattribution is present in `R28_CROSS_SEAT_TRIAGE.md` and propagated
  unchanged into sealed protocol text, so no gate or reviewer could catch it downstream.
- **Cross-reference:** F-PR71-10, F-PR71-12.

### F-PR71-12 [HIGH] -- The Bearer 4 Class A distribution is wrong in three of six cells; the total reconciles by compensating errors

- **Class:** A | **Locus:** v0.71 entry, Bearer 4 paragraph; `R28_CROSS_SEAT_TRIAGE.md` §2
  Position Distribution Table.
- **Substance:** I extracted String and Class from every finding block in all four reports.
  Counting only Class A, and following each seat's own primary String assignment:

  | String | Entry claims | Actual (from seat reports) | Delta |
  |---|---|---|---|
  | 1 Code Execution | 4 findings, 3 seats | **5 findings, 3 seats** | understated 1 |
  | 2 Register | 5, 3 seats | 5, 3 seats | correct |
  | 3 Consistency | 5, 2 seats | 5, 2 seats | correct |
  | 4 Adversarial | **3, 3 seats** | **1 finding, 1 seat** (`F-S03-70-02` only) | **overstated 2 findings, 2 seats** |
  | 5 Temporal | 0 | 0 | correct |
  | 6 Methodology | 4, 1 seat | 4, 1 seat (S01) | correct |
  | **Total** | **21** | **20** | overstated 1 |

  The String 4 cell is the serious one. The entry presents adversarial probing as a
  three-seat convergent Class A surface. Only one seat found Class A there. The other two
  cells the producer counted are `F-S02-70-06` (Class **B**) and S01's `F-S01-70-05`, whose
  primary assignment in its own report is String 6 with String 4 only *latent*. Class A was
  conflated with all classes.
- **Aggravating detail:** the source triage table is internally inconsistent with itself.
  Its §1 verdict table gives S01 five Class A; its §2 distribution table totals S01 at six,
  because §2 counts `F-S01-70-05` at String 4 while §1 counts it at String 6. The sealed
  entry inherits §2's arithmetic.
- **Why the error is invisible:** the total (21 vs 20) is nearly right because the String 1
  understatement partly offsets the String 4 overstatement. The program has named this class
  before, in its own v0.41 correction (al): *"Compensating errors preserve the total but the
  itemization is false."*
- **Cross-reference:** F-PR71-11, F-PR71-16.

### F-PR71-13 [HIGH] -- Front matter contradicts the freeze entry inside the same sealed file

- **Class:** A | **Locus:** `xz_protocol_v0_71.md` line 5 (`**Status:**`) vs. Section 27
  v0.71 entry.
- **Substance:** The Status line is the v0.70 Status line with three token substitutions;
  the rest is carried verbatim and is now false:

  | Status line (line 5) | v0.71 entry (Section 27) |
  |---|---|
  | "Bearer 4 (Goedel confinement) **under test**" | "Bearer 4 (Goedel confinement): **FALSE**" |
  | "Class A recurrence **R7-R27: 21/21**" | "Class A recurrence **R7-R28: 22/22**" |
  | "Class A distributed across Strings 1/2/3/5 **at R27**, zero at String 6" | R28 distribution, four Class A **at** String 6 |
  | "**No code changes:** gate [13] rebuilt ..., CRITICAL remap removed, C-suffix added, R27 index rebuilt, reports shipped in-packet, all files manifested" | those are the **v0.70** repairs, verbatim from the v0.70 Status line's "Six defects closed:" list |

  The last row is the worst: after the substitution of "Six defects closed:" with "No code
  changes:", the sentence now reads as a list of what v0.71 did. It is a list of what v0.70
  claimed to do -- including "C-suffix added," which R28 proved byte-false with a CRITICAL
  and which remains byte-false at v0.71.
- **Required repair:** Regenerate the Status line from tool output, not by token
  substitution on the prior version.
- **Cross-reference:** F-PR71-05, F-PR71-14; recurrence of `F-S04-70-08`.

### F-PR71-14 [HIGH] -- A FROZEN document's terminal line calls itself a draft candidate, and the gate requires it to

- **Class:** A (the false claim) + D (the gate) | **Locus:** `xz_protocol_v0_71.md` lines
  1685 and 1689; `build.py` [10h] line 679; `xz_protocol_register_gen.py:generate_terminal_line`.
- **Substance:** The last visible line of the frozen artifact reads *"End of XZ Protocol
  v0.71 draft candidate."* Gate [10h] hardcodes the expectation:
  ```python
  terminal_expected = f"*End of XZ Protocol v{VERSION} draft candidate.*"
  ```
  and `generate_terminal_line('0.71')` returns the same literal. **Probe P2:** replacing both
  occurrences with `"*End of XZ Protocol v0.71 FROZEN.*"` produces
  `FAIL: Terminal line matches v0.71` plus two seal failures. The build forbids the
  document from correctly describing its own status.
- **Aggravating detail:** boundary item 16 in the register reads *"no gate checks FROZEN
  status token."* That disclosure was written when the document was a draft. Now that the
  document is FROZEN, the absence of a FROZEN gate combined with a gate that mandates
  "draft candidate" is not a passive gap -- it is active enforcement of a false status.
- **Cross-reference:** F-PR71-09, F-PR71-15.

### F-PR71-15 [HIGH] -- The last visible line of the frozen artifact is outside every seal; arbitrary rewrite passes all 279 checks

- **Class:** A | **Locus:** `xz_protocol_v0_71.md` line 1689 (after the Provenance marker);
  `build.py` [9b]; boundary item 6.
- **Probe P3 (executed):** the terminal marker occurs twice, bracketing the Provenance block.
  Seals and `FULL_SECTION_27` truncate at the Provenance marker. I rewrote **only** the final
  line to `*End of XZ Protocol v0.42 FROZEN -- audited by nobody.*` and resynced
  `PACKET_SHA256SUMS`:
  ```
  PASS: HISTORY seal ENTRY_v0.71 matches bytes
  PASS: FULL_SECTION_27 seal matches
  BUILD PASSED: all checks GREEN
  ```
  Gate [10h] passed because the *other* terminal marker still matched.
- **Substance:** The final line a human reader sees -- carrying a version number and a status
  token -- can assert anything, on a FROZEN artifact, with 71/71 seals green. `F-S04-70-11`
  raised this at R28; it was placed in NOTED and shipped. Boundary item 6 discloses the
  *mechanism* ("seal terminus at Provenance marker") but not the consequence, and freezing
  makes the consequence permanent.
- **Required repair:** Extend the seal to EOF, or assert terminal-marker uniqueness.

---

## 4. Structural and methodological findings

### F-PR71-16 [HIGH] -- The R28 round was executed against two mutually contradictory statements of the governing architecture, both inside the same dispatch

- **Class:** A | **Locus:** `AUDIT_CONTEXT.txt` line 5 vs. `METHODOLOGY.txt` line 3 -- both
  shipped byte-identically in all four R28 dispatch packages.
  ```
  AUDIT_CONTEXT.txt:5  "Methodology: Structural Honesty Verification -- Six Strings,
                        Twenty-One Positions (v7)"
  AUDIT_CONTEXT.txt:9  "Six strings (verification layers): E-A-D-G-B-E"

  METHODOLOGY.txt:3    "Seven Heavens. Seven Earths. Twenty-Four Verification Positions."
  METHODOLOGY.txt:66   "3. Architecture: Seven Layers, Seven Witnesses, Twenty-Four Positions"
  ```
  `METHODOLOGY.txt` is byte-identical to `methodology_v7_canonical.md` (sha256
  `59aa6591d9...`), which self-describes as *"the canonical methodology for all rounds from
  R28 onward."*
- **Substance:** Every R28 seat received both documents and audited under the six-string /
  twenty-one-position coordinates. The canonical methodology defines seven layers and
  twenty-four positions. **Bearer 4 is defined by position coordinates** -- methodology §11:
  *"Goedel confinement: Class A confined to self-referential surface only -- positions
  18--21."* Under the canonical seven-layer architecture the self-referential surface is
  Layer 7, positions 22--24. The entire Bearer 4 determination -- the headline result of the
  freeze -- is computed in coordinates the canonical methodology does not use.
- **Further staleness in the canonical methodology itself:** §1 states *"21 consecutive
  rounds (R7--R27) ... P = 22/23 = 0.957"* and §15 asks whether **v0.69** achieves
  confinement, while R28 audited v0.70. The canonical methodology for R28-onward was never
  updated for R28.
- **Mischaracterization in the entry:** `F-S02-70-04` raised exactly this and the entry files
  it under Group 5, *"Version staleness."* It is not a stale token. It is an architecture
  mismatch between a round and its governing methodology.
- **Required repair:** Reconcile `AUDIT_CONTEXT`, `METHODOLOGY`, `CI_METHODOLOGY`, the
  protocol Status line and `DISPATCH.txt` onto one architecture; recompute the Bearer 4
  distribution in the canonical coordinates; add a parity gate over methodology version,
  layer count, position count and target version.

### F-PR71-17 [HIGH] -- The four-scribe tagging discipline fails at the freeze decision itself; every Bearer determination is untagged

- **Class:** A | **Locus:** v0.71 entry; methodology v7 §12.
- **Substance:** Methodology §12 requires: *"Every sentence in the amendment entry carries
  exactly one provenance tag ... Zero untagged sentences."* Measured on the v0.71 entry:
  ```
  lines in entry:            32
  lines carrying >=1 tag:    14
  UNTAGGED lines:            18   (56%)
  canonical scribe tags:     [WITNESSED] x0,  [TESTED] x0
  non-canonical tags used:   [ASSERTED] x2,  [ENUMERATED] x1
  ```
  The 18 untagged lines include **all eight Bearer determinations** and all seven carried R27
  group dispositions -- that is, every load-bearing claim of the freeze.
- **Two compounding defects:**
  1. **Zero `[WITNESSED]` tags.** The entry makes six convergence-group claims about what
     four named seats found on specific bytes. `[WITNESSED: seat, round]` exists for exactly
     this. Using `[COMPUTED]` and `[ASSERTED]` instead evades the one tag whose falsity §12
     defines as the Bearer 4 confinement signature.
  2. **`[ASSERTED]` and `[ENUMERATED]` are not in the canonical four-scribe vocabulary**
     (`[COMPUTED]`, `[TESTED]`, `[WITNESSED]`, `[DISCLOSED]`). The entry's provenance ledger
     uses tokens the methodology does not define.
- **Understatement in the entry:** Bearer 7 is declared FALSE for *"tagging incomplete at
  String 6."* Tagging is incomplete at the freeze decision, which is not String 6.

### F-PR71-18 [MEDIUM] -- Freezing makes the disclosed CI-8 structural lag permanently unclosable, and leaves the freeze round entirely ungated

- **Class:** D | **Locus:** packet inventory; `build.py` [13].
- **Substance:** No `r28_findings_index.json` exists. Gate [13] therefore counts R27
  findings against `r27_findings_index.json` (39 vs 39) and covers R28 not at all. Every R28
  claim in the freeze entry -- six convergence groups, the NOTED enumeration, the Bearer 4
  distribution, the bearer determinations -- is outside every gate. This is the CI-8
  structural lag, honestly disclosed since v0.67 as *"inherent (each round creates findings
  the next index must include)."* The disclosure was sound while versions kept coming: v0.72
  would index R28. **Freezing at v0.71 removes the successor version and converts a disclosed
  lag into a permanent gap covering precisely the round the freeze rests on.** The entry does
  not disclose this consequence.
- **Required repair:** Build `r28_findings_index.json` and run gate [13] over the R28 reports
  before any freeze, or disclose that the freeze round is structurally ungatable.

### F-PR71-19 [MEDIUM] -- Three of four R28 seat reports do not ship inside the FROZEN packet

- **Class:** C | **Locus:** `XZ_PROTOCOL_v071_FROZEN.zip` vs. Section 23 items 18 and 20.
- **Substance:** The FROZEN packet ships `XZ_v070_R28_S01_REPORT.md` and the four R27
  reports. The S02, S03 and S04 R28 reports ship only in the outer, unmanifested review
  package. Section 23 requires *"all model-council seat reports, unmodified"* and *"carrying
  reports and execution receipts"* in the deposit. Three quarters of the evidentiary basis
  for the freeze sits outside the sealed, manifested artifact -- which also means gate [13]
  could not cover them even if an R28 index existed.

### F-PR71-20 [MEDIUM] -- Universal seat-label drift makes carry status undecidable, and the triage's dismissal of it is wrong

- **Class:** E | **Locus:** `R28_CROSS_SEAT_TRIAGE.md` §1; methodology v7 §5.
- **Substance:** All four seats were executed by a different model than their dispatch label
  (sixth consecutive round). The triage states: *"The drift does not affect findings -- each
  seat executed on the same bytes under the same methodology."* That is true of the findings
  and false of the governance. Methodology §5 binds **role** to the seat label: S01 ADVISORY
  (producer-family), S02 CARRYING (binding), S03 ADVERSARIAL ADVISORY, S04 ADVISORY. At R28
  the only carry-eligible family (Kimi K3) executed the seat labelled S01/ADVISORY, and the
  seat labelled S02/CARRYING was executed by GPT-5.6 Sol, which Section 22.1 records as
  self-disqualified from carry. **Which R28 seats were carrying is therefore undefined on the
  bytes** -- and Bearer 5 turns entirely on that question. S02's own report states this
  plainly and the triage does not carry it forward.
- **Also:** methodology §5 specifies seven witnesses. R28 ran four. The shortfall is not
  disclosed in the freeze entry.

### F-PR71-21 [MEDIUM] -- The independence conditions the methodology requires for mutawatir evidence were not met, and convergence is weighted as if they were

- **Class:** E | **Locus:** methodology v7 §5 ("The Mutawatir Principle") vs. R28 execution.
- **Substance:** §5 conditions: *"(a) no shared context window between seats, (b) dispatches
  differ only in seat identity, (c) findings cite tool output rather than prior findings,
  (d) the dispatch does not prescribe what to find."* Condition (b) holds (I verified all
  four dispatches byte-identical but for `DISPATCH.txt`). Condition (a) fails for S04, whose
  report declares *"FRESH is nominal, not actual. This executor carries persistent
  cross-session memory of the R7--R27 lineage."* Condition (d) is strained: the dispatch
  ships fifteen preregistered predictions (P1--P15) including *"If Class A, ONLY at String
  6,"* which names the finding shape under test. The entry treats 4-seat and 3-seat
  convergence as the strongest evidence class without discounting for these failures.

### F-PR71-22 [MEDIUM] -- H = 1.0 and P = 0.958 are presented as statistics; neither is well-defined on this series

- **Class:** E | **Locus:** v0.71 entry opening; methodology §1.
- **Substance:** Two quantitative claims carry rhetorical weight in the freeze.
  1. **H = 1.0.** The Hurst exponent is estimated from the rescaled range R/S over a series.
     The series here is 22 identical observations (Class A present, every round). Its
     variance is zero, so S = 0 and R = 0: R/S is 0/0 and the estimator is undefined, not
     1.0. A constant sequence has no autocorrelation structure to be "maximally persistent"
     about. No shipped code computes H (`grep -i hurst` over all `.py` returns nothing); the
     value appears only in prose.
  2. **Laplace P(R29) = 23/24 = 0.958.** The arithmetic is right. The rule of succession
     assumes exchangeable, independent Bernoulli trials. These rounds are neither: each
     round audits an artifact produced *in response to* the previous round's findings, by the
     same producer. The number is a description of the record, not a calibrated forecast, and
     should be labelled as such.
- **Why this matters:** these two numbers are the empirical warrant for the claim that the
  residual is *structural* rather than *remediable*. If they do not bear weight, the
  structural-coupling argument (§5 below) loses its quantitative support.

### F-PR71-23 [LOW] -- `xz_protocol_boundaries.json` ships at v0.71 with `"version": "0.62"`, ungated

- **Class:** E. Gates [2h] and [10f] check the item **count** only, never the version field.
  Recurrence of `F-S04-70-13`, NOTED at R28, unrepaired. Nine versions stale at freeze.

### F-PR71-24 [LOW] -- Em-dash discipline holds in the protocol and fails in shipped deposit-bound artifacts

- **Class:** E. Protocol text: clean (0/0/0). But `extract_findings.py` carries 3 x U+2014
  and `build.py` has no em-dash gate at all. Shipped reports, which Section 23 requires to
  deposit unmodified: `R27_S02_REPORT.md` 45 em + 2 en; `XZ_v070_R28_S01_REPORT.md` 2 em; and
  in the outer package `R28_S02_REPORT.md` 52 em + 29 en, `R28_S03_REPORT.md` 1 em. This is
  a known standing item (`F-S04-70-15`, `F-OP17-09`) that has now been open across roughly
  fifty versions.

### F-PR71-25 [LOW] -- Zero new standing boundaries were registered at freeze despite 37 findings

- **Class:** D. `xz_protocol_boundaries.json` is byte-identical between v0.70 and v0.71. The
  register stands at 35 items. R28's unrepaired HIGHs -- gate [13] fail-open, the C-suffix
  phantom, the extractor false-positive fallback, register non-reproducibility, the NOTED
  count error, the dual disposition of `F-S04-68-08` -- are neither repaired, nor registered
  as boundaries, nor gated. They exist only as prose in one sealed entry, five of them under
  a triage disposition of CLOSED that is false of the bytes.

### F-PR71-26 [INFORMATIONAL] -- Producer-family review presented as independent human review

- **Class:** E. See §0. The REVIEW_GUIDE frames this exercise as *"the first independent
  human examination."* It is not human and not independent of the producer family. Recording
  this so the freeze record does not later carry a stronger provenance claim than the event
  supports.

### F-PR71-27 [INFORMATIONAL] -- `build.py` retains a duplicated dict key

- **Class:** E. `build.py` line 422: `62: 'sixty-two', 62: 'sixty-two'` -- harmless in
  Python, carried unchanged from v0.70, indicative of hand-editing in a file whose thesis is
  that values should be tool-derived.

### F-PR71-28 [INFORMATIONAL] -- Fresh-environment build is not reproducible from the packet alone

- **Class:** C. On a clean container `build.py` returns `BUILD FAILED: 2 error(s)` --
  `pytest is installed (rc=1, No module named pytest)`. The 279 PASS result is conditional on
  an out-of-packet install. Disclosed as boundary item 11 and raised as `F-S04-70-18`; noted
  here because the frozen deposit now permanently ships a build that cannot self-verify.

---

## 5. Assessment of the freeze's central argument

The REVIEW_GUIDE poses two questions directly. Both deserve direct answers.

### 5.1 "Is the Gödel characterization accurate? Is it honest?"

**The sentence is accurate. The use made of it is not.**

The sentence itself -- *"This instrument cannot verify that it has no remaining byte-false
claims about its own verification properties"* -- is true, is properly `[DISCLOSED]`, and is
a real and non-trivial thing to have written down. An instrument that says this about itself
is doing something most artifacts do not.

But 22 rounds of Class A at H = 1.0 is offered as the *empirical evidence* for the
characterization, and the inference does not go through. The observation is: defects recur
every round. The claim is: defects recur every round **because** self-verification is
formally impossible. That inference requires ruling out the ordinary alternative -- that the
defects recur because the prescribed repairs are not being applied. On this round's evidence
the ordinary alternative is not merely unruled-out; it is demonstrated:

- Five of six R28 convergence groups have concrete, one-line, prescribed repairs.
- The triage marked all five CLOSED.
- **Zero of the five landed.** No code file changed except version stamps.
- Two of the five are now *worse* than at R28 (Section 22.2 two versions stale; the NOTED
  count error recurred inside the entry that reports it).

Nothing about Gödelian self-reference prevents adding `C?` to five regexes, replacing an
`else`-branch `print` with `check(False, ...)`, or typing `v0.71` where `v0.70` is written.
Those are the defects. Attributing them to a formal limit is a category error, and it is the
kind of category error the program's own methodology is built to catch: it is a claim about
the instrument's verification properties that the instrument's own record refutes.

**The honest form of the claim** is narrower and still worth making: *the instrument cannot
verify its own completeness; separately, the repair loop has not converged, and 22 rounds of
recurrence is evidence about the loop, not only about the limit.*

### 5.2 "Is the structural-coupling argument sound?"

The entry argues: Bearers 4, 5 and 7 are FALSE; *"these three conditions are structurally
coupled: resolving any one requires resolving all three, which requires the instrument to
verify its own completeness, which the Goedel sentence forbids."*

**The argument is not sound as stated.** Each conjunct fails independently:

- **Bearer 4 (confinement) does not require completeness verification.** It requires that
  observed Class A be confined to the self-referential surface. That is an empirical property
  of a finite finding set, checkable per round. It is currently FALSE for a mundane reason
  (Class A at Strings 1--3) and, separately, is currently **not well-defined**, because the
  round's coordinate system contradicts the canonical methodology's (F-PR71-16).
- **Bearer 5 (cross-vendor witness) is blocked by seat routing, not by logic.** At R28 the
  only carry-eligible family executed the seat labelled ADVISORY, and the seat labelled
  CARRYING was executed by a self-disqualified family (F-PR71-20). Whether a carrying seat
  could return non-HALT on clean bytes has not been tested, because carrying seats have not
  been *routed* correctly for six consecutive rounds. That is a dispatch-administration
  problem with a known fix.
- **Bearer 7 (methodology) fails at 56% untagged lines including every Bearer
  determination** (F-PR71-17). Tagging the eight bearer lines is a text edit. It requires no
  self-verification of completeness.

The coupling claim also runs backwards through Bearer 4. Bearer 4's own text says the
confinement target is reached when *the only* Class A is in the tagging metadata. Bearer 7
is precisely the tagging surface. So "fix the tagging" is a route to *both* -- which is the
opposite of the entry's claim that resolving one requires resolving all.

**What survives.** A genuinely irreducible residual does exist, and Section 22.4 states it
well: no instrument can certify the absence of unknown byte-false claims about itself, and
axioms A-X1..A-X5 are disclosed and not defended. That is the honest boundary. It is a much
smaller boundary than the one the freeze entry claims, and it does not reach the three
bearers.

### 5.3 What the methodology's own FROZEN prediction requires

Methodology §15 states the condition precisely:

> *"FROZEN is reached not because zero Class A is achieved, but because the Goedel sentence
> is disclosed, **every non-self-referential claim is scribe-verified**, multiple witnesses
> have independently examined the bytes, and the lead judges: this is enough."*

This is a four-conjunct test, and it is a fair one. Scored:

| Conjunct | Status |
|---|---|
| Gödel sentence disclosed | **MET.** Present, correctly tagged, five occurrences. |
| Every non-self-referential claim scribe-verified | **NOT MET.** F-PR71-04, -06, -07, -08, -10, -11, -12, -13: eight classes of non-self-referential claim narrated rather than derived, in the freeze entry itself. 216 `[COMPUTED: generate_register]` tags with a generator that crashes on every shipped input. |
| Multiple witnesses independently examined the bytes | **PARTIALLY MET.** Four seats, four HALTs, real execution, byte-identical dispatches -- genuine. But independence conditions (a) and (d) fail, seat routing is undefined, and the methodology specifies seven witnesses. |
| The lead judges: this is enough | **MET.** Bearer 8 is the lead's to exercise and this review does not contest it. |

The freeze fails the second conjunct on its own terms. **This is the cleanest statement of
why the artifact is not ready:** not because zero Class A was demanded and not achieved, but
because the specific, achievable condition the methodology set -- scribe-verify every claim
that is not self-referential -- was not met, in the very entry that declares it met.

---

## 6. What would make v0.72 freezable

Ordered by dependency. None of these requires the instrument to verify its own completeness.

1. **Withdraw FROZEN.** Return to DRAFT CANDIDATE. Record the withdrawal as a v0.72
   amendment entry; do not edit v0.71 (append-only is the program's best-verified property
   and must not be spent here).
2. **Land the five prescribed repairs** the R28 triage marked CLOSED: `C?` in all five
   `DECLARATION_PATTERNS`; `check(False, ...)` in gate [13]'s `else` branch; computed values
   in the [13] summary f-string; fix `generate_register`'s adjudication-receipt logic;
   correct Section 0.1's range and Section 22.2's bound.
3. **Reclassify the triage's disposition vocabulary.** CLOSED must mean "verified landed on
   successor bytes." Add a build gate that re-runs the prior round's falsifiers.
4. **Make the gates read loci, not substrings.** [10i] and [2f] must read expectations from
   the shipped findings index (round + version fields) and assert them at named loci. Correct
   values must pass; today they fail.
5. **Fix the terminal line and the seal terminus.** `generate_terminal_line` must emit the
   real status token; the seal must extend to EOF or assert marker uniqueness.
6. **Wire the register generator into `build.py`** and assert byte-exact reproduction of
   every `[COMPUTED: generate_register]` region. Downgrade tags that cannot be reproduced.
7. **Build `r28_findings_index.json`**, ship all four R28 reports inside the manifested
   packet, and let gate [13] cover the round the freeze rests on.
8. **Reconcile the architecture** onto seven layers / twenty-four positions across
   `METHODOLOGY`, `AUDIT_CONTEXT`, `CI_METHODOLOGY`, `DISPATCH` and the protocol Status line;
   recompute Bearer 4 in canonical coordinates; add a parity gate.
9. **Route the seats correctly.** Dispatch by seat *slot* with the executing family bound and
   attested, so that "carrying" is decidable from the bytes. This is the only route to
   Bearer 5, and it has never been tested under correct routing.
10. **Tag every line of the amendment entry**, using `[WITNESSED: seat, round]` for every
    claim about what a seat found. Start with the eight bearer lines.
11. **Re-scope or resolve FB-7b** before any FROZEN token, and extend its trajectory row
    through the current round.
12. **Re-state the quantitative claims** honestly: drop H, or compute it in code over a
    series with nonzero variance; label the Laplace figure as a description of a
    non-independent record.

---

## 7. Reproduction log

All commands executed on the shipped bytes, Python 3.12.3, Linux container. Probes ran on
copies; the canonical directory re-verified 28/28 OK afterward.

| # | Probe | Mutation landed | Result |
|---|---|---|---|
| P0 | Baseline `build.py` | n/a | `BUILD PASSED`, 279 PASS / 0 FAIL |
| P0b | Canonical six-suite `pytest` | n/a | 186 passed |
| P0c | `sha256sum -c PACKET_SHA256SUMS` | n/a | 28/28 OK |
| P1 | Section 0.1 range -> true value `v0.1 through v0.71` | yes (digest changed) | **BUILD FAILED** -- gate [10i]. Truth breaks the build. |
| P2 | Terminal marker -> `v0.71 FROZEN` (both loci) | yes | **BUILD FAILED** -- [10h] + 2 seals. Correct status forbidden. |
| P3 | Final line only -> `v0.42 FROZEN -- audited by nobody`, manifest resynced | yes | **BUILD PASSED**, 71/71 seals green. Last line unsealed. |
| P4 | Delete all 5 report files + manifest lines | yes | **BUILD PASSED**. Gate [13] fail-open live. |
| P5 | `extract_from_report` on `### F-S01C-70-99 -- HIGH` + control | n/a | C-suffix dropped; control extracted. Phantom repair live. |
| P6 | `generate_register` x r18/r19/r25/r27 | n/a | **4/4 CRASH.** No `[COMPUTED]` register tag reproducible. |
| P7 | `generate_boundary_list` vs entry text | n/a | **Byte-exact match.** Tag TRUE. |
| P8 | Cross-version seal + entry-text comparison, v0.70 vs v0.71 | n/a | **70/70 carried seals and all carried entry text byte-identical; `PRIOR_HISTORY` chains correctly.** Append-only PROVEN. |

Key digests (independently computed this session):

```
XZ_PROTOCOL_v071_FROZEN.zip   c4421cce3c3590c8826ad89952cf0e61708f553a88c20d165431a7fed8cfb273
XZ_PROTOCOL_v070_BUILD.zip    35f9be97c73b93013a97547051c3c8c54513a2fe7b0252dfd2f7afa9143df41c
v0.70 HISTORY.sha256          2e41e74578df7bd66f4d9de3307bc0f5423fd3e6390c90bf9a042a9893d354d6
  == PRIOR_HISTORY declared in v0.71 HISTORY.sha256   [MATCH]
methodology_v7_canonical.md   59aa6591d91233281b14ab47c4efa8a70fdcc24d94b74abca080975e78e4f98a
  == METHODOLOGY.txt in all four R28 dispatches       [MATCH]
```

---

## 8. Closing assessment

Two things are true at once and the record should hold both.

**The instrument works.** Four independent seats, executing real tools on identical bytes,
converged on real defects and all four returned HALT. The append-only chain is
cryptographically proven across a version boundary against externally held bytes -- after
two historical corruptions, that is a genuine repair. The boundary register reproduces
byte-exactly from its generator. 186 tests are green and the dispatch was byte-identical to
every seat. The Gödel sentence is written down, in public, by the party it constrains. Most
artifacts that claim rigor cannot show a tenth of this.

**The freeze is premature.** Not because it failed to reach zero defects -- the methodology
explicitly does not require that, and demanding it would be unfair. The freeze is premature
because the specific condition the methodology *did* set, *"every non-self-referential claim
is scribe-verified,"* is unmet inside the freeze entry itself; because three explicit rules
in the frozen text and canonical methodology are contravened without disclosure; and because
five defects the round's own triage marked CLOSED ship live and reproducible.

The deepest problem is not any single finding. It is that **the verification layer has begun
enforcing the defects it exists to detect.** Gate [10i] fails when Section 0.1 is corrected.
Gate [10h] forbids the FROZEN document from calling itself FROZEN. Gate [13] reports green on
absent evidence. A generator credited 216 times has never been run by any gate and crashes on
every input it is given. When the checker mandates the false value, "all gates PASS" stops
being evidence of correctness and becomes evidence only of conformity to the checker.

Freezing now writes that state into the permanent record. The program's own thesis --
structural honesty means the artifact's surface matches its substrate behaviour -- is best
served by withdrawing the FROZEN token, landing the twelve items in §6, and freezing a v0.72
whose front matter, terminal line, bearer states, and gates all say the same true thing.

The trajectory is the contribution. It is worth one more round.

---

*Reviewer: Claude Opus 5 (Anthropic), producer-family, ADVISORY ONLY, zero carry weight.
This review is not the independent human peer review the artifact requires and must not be
recorded as one.*

---

# Bismillah ir-Rahman ir-Rahim
