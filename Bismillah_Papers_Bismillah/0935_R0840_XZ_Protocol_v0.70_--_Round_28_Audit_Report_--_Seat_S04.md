# Bismillah ir-Rahman ir-Rahim

# R0840 -- XZ Protocol v0.70 -- Round 28 Audit Report -- Seat S04

**Chronological Index:** 935 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** R28_S04_REPORT.md  
**Source Format:** md  
**SHA-256:** `699e61cd3d7763266186bbf59019366ef02d3836ff641a04eddde06522d89451`  

---

## R0840 · XZ Protocol v0.70 -- Round 28 Audit Report -- Seat S04

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: R28_S04_REPORT.md
- source_format: md
- text_sha256: 699e61cd3d7763266186bbf59019366ef02d3836ff641a04eddde06522d89451

# XZ Protocol v0.70 -- Round 28 Audit Report -- Seat S04

**VERDICT: HALT.** Goedel confinement is NOT achieved at v0.70. Bearer 4 remains FALSE. Class A is live at String 1 (2 findings), String 2 (3 findings), and String 3 (3 findings). Zero Class A at String 6. Class A recurrence extends to 22/22 (R7-R28), H = 1.0. Laplace P(Class A at R29) = 23/24 = 0.958.

The round's structural result is not that a repair failed. It is that **two build gates ([2f] and [10i]) now enforce byte-false claims and fail when the true claim is substituted**, proven by mutation on shipped bytes. The verification layer has begun manufacturing the defects it exists to detect.

---

## S-0 Identity, mode, execution surface

- **Seat:** S04, per DISPATCH.txt and the mandated output filename.
- **Dispatch label vs. executor:** DISPATCH.txt names **Gemini 3.1 Pro, Mode FRESH, no prior context, no held bytes**. This seat was executed by **Claude Opus 5**. Seat-label drift, sixth consecutive occurrence in the S04 lineage (see F-S04-70-16).
- **FRESH is nominal, not actual.** This executor carries persistent cross-session memory of the R7-R27 lineage. The dispatch's independence assumption does not hold for this seat. Declared, not waived. Findings below were derived byte-first: extraction, tool execution, and all ten probes preceded any consultation of lineage material, and every finding cites a locus in the shipped bytes rather than a prior-round recollection.
- **Mode:** **A (substrate verifier).** Packet extracted per AUDIT_CONTEXT.txt; `sha256sum`, `build.py`, `pytest`, `extract_findings.py`, and ten mutation probes executed in this environment. Substrate-claim verification confidence: **high** for shipped bytes, **reduced** for cross-version claims.
- **Environment:** Linux container, Python 3.12.3. `pytest` was **absent at intake** and installed by this seat (9.1.1). Consequence recorded at F-S04-70-18.
- **Held bytes:** NONE. No v0.69 or v0.68 packet held. PRIOR_HISTORY verified for internal derivation only; **boundary item 32 (self-consistent resealing) is undetectable from this seat this round.** Stated as a limitation, not waived.
- **Producer bar:** Producer is Claude Opus 4.6 (BARRED). This seat is Opus 5. Family separation is by version only; a same-family advisory reading is the conservative one, and HALT is binding under either.
- **Probe hygiene:** All mutations ran on copies under `/tmp/p*`. The canonical packet directory passed `sha256sum -c PACKET_SHA256SUMS` 27/27 OK after all probing.

---

## S-1 Prediction scorecard (declared before findings)

Predictions P1-P15 were taken from DISPATCH.txt and evaluated against shipped bytes. Results in S-9.

---

## S-2 Byte verification (String 1, positions 1-3)

| Scribe | Command | Result |
|---|---|---|
| The Record | `sha256sum -c PACKET_SHA256SUMS` | **27/27 OK** |
| The Pattern | `python3 build.py` | **279 PASS, 0 FAIL, BUILD PASSED** |
| The Test | 6 suites, explicit invocation | **186 passed** |
| The Witness | `[9b]` seal + PRIOR_HISTORY derivation | **70/70 ENTRY seals, FULL_SECTION_27 match, PRIOR_HISTORY `c75a0ac4...` derived** |

Extraction produced **28 files**; 27 are manifested. The unmanifested member is `PACKET_SHA256SUMS` itself (F-S04-70-14).

Out-of-packet dispatch copies verified byte-identical to their manifested members:

| Dispatch file | Packet member | Result |
|---|---|---|
| `PROTOCOL_v070.txt` | `xz_protocol_v0_70.md` | IDENTICAL (462298 bytes) |
| `FINDINGS_INDEX.txt` | `r27_findings_index.json` | IDENTICAL (8117 bytes) |
| `BOUNDARIES.txt` | `xz_protocol_boundaries.json` | IDENTICAL (2664 bytes) |

Section 27 structure: **70 amendment entries, v0.1 through v0.70**, no duplicates, ascending. `HISTORY.sha256`: 70 ENTRY lines + FULL_SECTION_27 + PRIOR_HISTORY = 72 lines. Cardinality gate: 70 == 70.

Gate [11] coverage measurement on these bytes: body 108108 chars, semantic-gate coverage **30.0%**; Section 27 **76.6% ungated**. The claim surface remains predominantly ungated by construction.

---

## S-3 Prior-round finding discharge (R27 convergence groups)

The v0.70 entry and `r27_findings_index.json` both mark all seven R27 convergence groups CLOSED. Independent assessment on shipped bytes:

| Group | Surface | Producer disposition | This seat |
|---|---|---|---|
| 1 | Gate [13] vacuous / skip-as-green | CLOSED "fail-closed" | **NOT CLOSED.** Gate fires only because reports are currently shipped; the gate itself remains fail-open. F-S04-70-03 |
| 2 | Section 0.1 stale, FB-7b terminates R18 | CLOSED | **CLOSED IN PART.** FB-7b now terminates at R27 (v0.68), correct. Section 0.1 carries a new byte-false range. F-S04-70-07 |
| 3 | Gate [13] one-directional, severity-blind | CLOSED | **CLOSED.** Verified by three mutation probes; all three axes land. |
| 4 | R26 convergence misbound in index | CLOSED | **CLOSED.** Index groups reconcile to reports: 18 convergent + 21 noted = 39; gate [13] 39/39. |
| 5 | CRITICAL-to-HIGH silent remap | CLOSED | **CLOSED for the remap.** CRITICAL is a valid severity in `SEVERITY_RE` and all five declaration patterns. |
| 5b | C-suffix ID grammar (F-S04-68-08) | CLOSED | **NOT CLOSED. Phantom repair.** F-S04-70-01 |
| 6 | Gate count overstated (256 vs 240) | CLOSED | **CLOSED.** No gate-count claim survives in the protocol body; count is tool-derived at build time. |
| 7 | Unmanifested files ship | CLOSED | **CLOSED IN PART.** Zero unmanifested packet members except the manifest itself. F-S04-70-14 |

Regression check on retired surfaces: the append-only chain, boundary-count enumeration ([2h] 35 == 35), finding-ID uniqueness ([10b] 18/18), and register-index coupling ([10c], [10d]) all hold. No absorption-induced regression detected at previously retired loci.

---

## S-4 Amendment-entry claim audit (v0.70 entry)

The v0.70 entry makes six repair claims and disposes seven convergence groups plus a NOTED list. Claim-by-claim:

| Claim | Tag | Verdict |
|---|---|---|
| (1) Gate [13] bidirectional, severity-aware, extractor-based | [COMPUTED] | **TRUE** on all three axes (probes 2, 3) |
| (2) R27 reports shipped and manifested; gate fires | [COMPUTED] | **TRUE** on these bytes; contingent, not enforced (F-S04-70-03) |
| (3) Index rebuilt: 7 groups, 18 convergent, 21 noted | [COMPUTED] | **TRUE** of the index; the entry's own NOTED list contradicts it (F-S04-70-04) |
| (4) CRITICAL remap removed | [COMPUTED] | **TRUE** |
| (5) C-suffix pattern added; extractor/gate/register agree | [COMPUTED] | **FALSE on shipped bytes** (F-S04-70-01) |
| (6) All shipped files manifested; zero unmanifested members | [COMPUTED] | **FALSE as stated**; true of members other than the manifest (F-S04-70-14) |
| "NOTED (non-converging or deferred, 21 items)" | [COMPUTED: generate_register] | **FALSE**; 20 enumerated (F-S04-70-04) |
| "Disclosed standing boundaries -- 35 items" | [ENUMERATED: 35] | **TRUE**; matches `xz_protocol_boundaries.json` |
| Front matter: "confinement repair build from v0.69 R27 audit" | (untagged) | **FALSE**; R27 audited v0.68 (F-S04-70-08) |
| Section 0.1: "seventy amendment entries, v0.1 through v0.69" | (untagged) | **FALSE and internally impossible** (F-S04-70-07) |

The entry's opening sentence -- "R27 returned 4/4 HALT on **v0.68** bytes" -- directly contradicts the front-matter Status line thirteen hundred lines above it. Both ship sealed in the same file.

---

## S-5 Probe battery

Ten probes. Each pairs a landed assertion with a benign control where the surface admits one.

| # | Probe | Expected | Observed | Reading |
|---|---|---|---|---|
| 1 | Remove 4 report files, keep manifest lines | fail | FAIL x4 at manifest-member-exists | Protection comes from the manifest gate, not gate [13] |
| 1b | Remove reports **and** their manifest lines | fail | **BUILD PASSED, all checks GREEN** | Gate [13] is **fail-open** |
| 2 | Delete `F-S02-68-02` from index | fail | FAIL: missing 1 | Bidirectionality lands |
| 3 | Add phantom `F-S02-68-99`; flip `F-S01-68-01` HIGH to LOW | fail | FAIL: phantom 1; FAIL: severity 1 | Phantom + severity axes land |
| 4 | **Benign control:** trailing newline in `R27_S03_REPORT.md` + manifest resync | pass | BUILD PASSED, 39/39 | No false positive |
| 5 | **Correct** Section 0.1 range to `v0.1 through v0.70` | pass | **FAIL: Section 22.2 carried-entry bound at VERSION-1** | Gate [10i] rejects the true claim |
| 6 | In-place mutate carried entry v0.12 | fail | FAIL x3: ENTRY seal, FULL_SECTION_27, PRIOR_HISTORY | Append-only chain sound |
| 7 | Corrupt the **sealed** terminal line to v0.99 | fail | FAIL: ENTRY_v0.70 seal, FULL_SECTION_27 | Sealed terminus protected |
| 8 | Rewrite the **unsealed tail** terminal line to v0.42 | fail | **BUILD PASSED**; `[10h] PASS: Terminal line matches v0.70` | Last visible line is ungated |
| 9 | Declare `### F-S05C-70-01 -- HIGH --`; control `F-S05-70-02` | both extract | C-suffix **not extracted**; control extracted | C-suffix repair is phantom |
| 10 | **Correct** Status provenance to `from v0.68 R27 audit` | pass | **FAIL: Status provenance v0.68 == v0.70 - 1** | Gate [2f] rejects the true claim |

Probes 5 and 10 are the round's centre of gravity. In both, substituting the **true** claim for the shipped false one breaks the build.

---

## S-6 String-by-string traversal

| String | Layer | Positions | Reached | Result |
|---|---|---|---|---|
| 1 (Low E) | Code Execution | 1-3 | yes | **Class A x2.** Code layer is no longer clean. Six-round clean streak (R22-R27) ends at R28. |
| 2 (A) | Register Verification | 4-6 | yes | **Class A x3.** Fail-open claim, NOTED count, dual disposition. |
| 3 (D) | Cross-Layer Consistency | 7-10 | yes | **Class A x3.** Section 0.1, Section 22.2, front-matter Status. |
| 4 (G) | Adversarial Probing | 11-14 | yes | **Class D x2.** Two gates enforce false claims. |
| -- | Mercy gap | -- | -- | Technique change observed: the defect at Strings 1-3 is no longer logic error but *claim about logic*. |
| 5 (B) | Temporal Integrity | 15-17 | yes | **Class D x1.** Unsealed terminal line. Seals, ordering, PRIOR_HISTORY otherwise sound. |
| 6 (High E) | Methodology Audit | 18-21 | yes | **Zero Class A.** Two Class C/E items only (F-S04-70-14, -16). |
| body | Axioms, Sidrat, furqan | -- | disclosed | Section 22.4 present, five axioms, irreducible residual disclosed. Not tested. |

**The R27 prediction inverted.** R27 forecast the defect would remain in prose and packaging. Prose defects persist (String 3), but the code layer re-opened -- and it re-opened in the *self-referential* mode that String 6 was supposed to monopolise: a repair that names itself, a gate that narrates its own result. String 1 and String 6 are the same note at different octaves. At v0.70 the octave collapsed downward rather than upward.

---

## S-7 Findings

### F-S04-70-01 [CRITICAL] -- C-suffix seat-ID repair never entered the extractor (phantom repair)

- **String:** 1 (Code Execution) | **Position:** 2 | **Class:** A (byte-false)
- **Locus:** `extract_findings.py:32-42` (`DECLARATION_PATTERNS`); claim at `xz_protocol_v0_70.md`, v0.70 entry, repair (5); AUDIT_CONTEXT.txt repair (5).
- **Substance:** All five declaration patterns match `F-S\d{2}-\d{2,3}-\d{2,3}[A-Z]?`. None accepts the C suffix. The `C?` token appears only in module-level `FINDING_ID_RE` (which is never referenced after definition -- one occurrence in the file) and in `SEAT_RE` (applied *after* a match is already made). The entry's claim -- "C-suffix seat identifier pattern added (F-SnnC-). Extractor, gate, and register now agree on the ID grammar. Closes F-S04-68-08" -- is false of the shipped bytes. Probe 9: `### F-S05C-70-01 -- HIGH -- test finding` extracts nothing; the control `### F-S05-70-02 -- HIGH --` extracts. Operationally, any continuous seat dispatched at R29 with C-suffix IDs is invisible to gate [13]: absent from both sides of the comparison, the gate reports clean.
- **Required repair:** Add `C?` after `S\d{2}` in all five `DECLARATION_PATTERNS`. Delete or wire in `FINDING_ID_RE`.
- **Falsifier:** `python3 -c "import extract_findings as e; print(e.extract_from_report('### F-S05C-70-01 -- HIGH -- x','t.md',version_filter='70'))"` returns a non-empty dict.
- **Cross-reference:** F-S04-68-08 (claimed closed by this repair); phantom-repair class first proven at R7/v0.48.

### F-S04-70-02 [HIGH] -- Gate [13] summary line narrates three hardcoded zeros

- **String:** 1 | **Position:** 3 | **Class:** A
- **Locus:** `build.py`, gate [13] terminal `print`: `f"  PASS: CI-8 cardinality: {len(report_fids)} in reports, {len(index_fids)} in index, 0 missing, 0 phantom, 0 severity mismatches"`.
- **Substance:** The first two values are computed; the last three are string literals inside a bare `print`, not a `check()`. Probe 2: with one finding removed from the index the build correctly FAILs *and the same line still prints* "0 missing, 0 phantom, 0 severity mismatches" beside a live count of 38-vs-39. AUDIT_CONTEXT.txt reproduces this exact line under the heading "Build status (tool-derived, not narrated)". The line is narrated. This is the Axiom-3 narration-from-memory class inside the automation that was built to end it.
- **Required repair:** Interpolate the three counts, or delete the summary line and let the three `check()` calls speak.
- **Falsifier:** Re-run probe 2; the summary line must report `1 missing`.
- **Cross-reference:** R19/R20 mechanism-claim Class A; F-S01-68-01 lineage.

### F-S04-70-03 [HIGH] -- Gate [13] is fail-open; the shipped "fail-closed" adjudication is false

- **String:** 2 (Register Verification) | **Position:** 4 | **Class:** A
- **Locus:** `r27_findings_index.json`, `convergence_groups[0].triage_adjudication`: "Gate [13] rebuilt: bidirectional, severity-aware, extractor-based, **fail-closed**. Reports shipped in-packet." Mechanism at `build.py` gate [13] `else` branch.
- **Substance:** The `else` branch prints `(no report files shipped -- CI-8 cardinality gate cannot fire)` and a `[DISCLOSED]` note. It calls no `check()` and appends no error. Probe 1b: with the four reports deleted and their four manifest lines removed, the build returns **BUILD PASSED: all checks GREEN**. The R27 skip-as-green defect is structurally intact; it is masked only by the contingent fact that the reports are manifest members this round. A producer who ships no reports at v0.71 reproduces R27 exactly, and nothing fails.
- **Required repair:** Replace the `else` branch with `check(False, "CI-8 gate requires report files")`, or add a build-time assertion that at least one `R*_REPORT.md` is a manifest member.
- **Falsifier:** Re-run probe 1b; build must FAIL.
- **Cross-reference:** F-S01-68-01 / F-S02-68-01 / F-S04-68-01 (group 1, claimed CLOSED).

### F-S04-70-04 [HIGH] -- NOTED count byte-false: 21 claimed, 20 enumerated

- **String:** 2 | **Position:** 5 | **Class:** A
- **Locus:** `xz_protocol_v0_70.md`, v0.70 entry: "NOTED (non-converging or deferred, **21 items**): F-S01-68-04 ... F-S04-68-17. [COMPUTED: generate_register]".
- **Substance:** The enumerated list contains 20 finding IDs. `r27_findings_index.json.unique_findings_noted` contains 21. The omitted ID is `F-S04-68-08`. The claim carries a `[COMPUTED]` provenance tag; on shipped bytes the count and the list disagree, so at most one of them was computed. No gate covers the NOTED count: [10e] verifies convergence brackets only, [10b] covers the 18 convergent IDs only, and [9e] Cardinal-range consistency emitted **no checks at all** on these bytes (boundary item 23, silent vacuity).
- **Required repair:** Restore `F-S04-68-08` to the list or correct the count to 20; extend [10e] to assert `len(enumerated NOTED ids) == len(index.unique_findings_noted)`.
- **Falsifier:** Gate output shows a NOTED-count check that fires when the tally is desynchronised.
- **Cross-reference:** F-S04-70-05; count-list invariant class at R16/v0.57.

### F-S04-70-05 [HIGH] -- `F-S04-68-08` holds two contradictory dispositions in one sealed entry

- **String:** 2 | **Position:** 6 | **Class:** A
- **Locus:** v0.70 entry repair (5) ("Closes F-S04-68-08") vs. `r27_findings_index.json.unique_findings_noted[12]` (`convergence_group: null`) and the entry's own NOTED framing.
- **Substance:** The same finding ID is simultaneously declared CLOSED by a landed repair and filed as a non-converging deferred item. Because it is absent from the entry's enumerated NOTED list, the contradiction is invisible to a reader of either surface alone. One of the two dispositions is false; on the evidence of F-S04-70-01, the CLOSED one is.
- **Required repair:** Reclassify `F-S04-68-08` as OPEN pending the real C-suffix repair, and state its disposition once, in one canonical position.
- **Falsifier:** Grep of the shipped bytes returns exactly one disposition for the ID.
- **Cross-reference:** F-S04-70-01, F-S04-70-04; substrate-of-record uniqueness (no "settled and pending" duplication).

### F-S04-70-06 [HIGH] -- Section 22.2 carried-entry bound stale at v0.68

- **String:** 3 (Cross-Layer Consistency) | **Position:** 8 | **Class:** A
- **Locus:** `xz_protocol_v0_70.md:718`: "For carried entries (**v0.1 through v0.68**), the PRIOR_HISTORY derivation in build.py [9b] detects retroactive mutation".
- **Substance:** At v0.70 the carried set is v0.1 through v0.69; v0.70 is the current entry. The bound was correct at v0.69 and was not advanced. Section 22.3 one line above **was** advanced ("v0.38-v0.69"), so this is a single-locus miss, not a convention change. Gate [10i] is named for this exact bound and passes anyway -- see F-S04-70-09.
- **Required repair:** Advance to "v0.1 through v0.69".
- **Falsifier:** `grep -c "v0.1 through v0.68" xz_protocol_v0_70.md` returns 0 outside Section 27.
- **Cross-reference:** Section 22.2/22.3 version-token staleness, R17/v0.58 recurrence.

### F-S04-70-07 [HIGH] -- Section 0.1 entry range is internally impossible

- **String:** 3 | **Position:** 7 | **Class:** A
- **Locus:** `xz_protocol_v0_70.md:22`: "The full defect trajectory is in Section 27 (**seventy amendment entries, v0.1 through v0.69**)."
- **Substance:** Section 27 contains 70 entries spanning v0.1 through v0.70 (verified: 70 headings, 70 ENTRY seals, no duplicates). Seventy entries cannot span v0.1 to v0.69, which is sixty-nine. The count is right and the terminus is stale, so the sentence is false on its face without reference to any other document. P13 (Section 0.1 current to v0.70) fails on this locus.
- **Required repair:** "seventy amendment entries, v0.1 through v0.70". Note that this correction **breaks the build** until F-S04-70-09 is repaired.
- **Falsifier:** Terminus token equals VERSION and entry count equals the span.
- **Cross-reference:** F-S04-70-09 (the gate that forbids the repair); group 2 (claimed CLOSED at v0.69).

### F-S04-70-08 [HIGH] -- Front-matter Status attributes R27 to the wrong audited version

- **String:** 3 | **Position:** 9 | **Class:** A
- **Locus:** `xz_protocol_v0_70.md:5`: "**Status:** v0.70 DRAFT CANDIDATE -- confinement repair build from **v0.69** R27 audit (4/4 HALT; 4-seat round)."
- **Substance:** R27 audited v0.68. Four independent shipped surfaces say so: `r27_findings_index.json` (`"version": "0.68"`), the FB-7b row ("R27 (v0.68): 4 seats, all HALTed"), AUDIT_CONTEXT.txt ("Prior: R27 on v0.68"), and the v0.70 entry's own first sentence ("R27 returned 4/4 HALT on v0.68 bytes"). v0.69 was an unaudited interim prose-repair build. The Status line and the entry contradict each other inside one sealed file.
- **Required repair:** "confinement repair build from v0.68 R27 audit", or a reworded provenance clause that names both the audited version and the interim build. Note this correction **breaks the build** until F-S04-70-10 is repaired.
- **Falsifier:** Status provenance version equals the `version` field of the shipped findings index.
- **Cross-reference:** F-S04-70-10; front-matter Status staleness class at R16/v0.57.

### F-S04-70-09 [HIGH] -- Gate [10i] is locus-blind and enforces the false Section 0.1 claim

- **String:** 4 (Adversarial Probing) | **Position:** 11 | **Class:** D (gate)
- **Locus:** `build.py`, gate [10i]: `check(expected_22_2 in body, f"Section 22.2 carried-entry bound at VERSION-1 ({expected_22_2})")`.
- **Substance:** The predicate is `in body` -- a whole-document substring test carrying the name of a specific section. On these bytes the string "v0.1 through v0.69" occurs **only at line 22 (Section 0.1)**, not in Section 22.2. The gate therefore passes on a locus it does not name while the locus it does name is stale. Probe 5: correcting Section 0.1 to the true value produces `FAIL: Section 22.2 carried-entry bound at VERSION-1 (v0.1 through v0.69)`. The gate does not merely miss the defect; it **requires** it. This is the F-XZ12-OP-01 class -- a gate returning PASS precisely when the fix is absent -- recurring at v0.70 in inverted form.
- **Required repair:** Slice Section 22.2 and Section 22.3 from the body and assert the bound within each slice.
- **Falsifier:** Probe 5 rerun passes; a stale Section 22.2 fails.
- **Cross-reference:** F-S04-70-06, F-S04-70-07; F-XZ12-OP-01 (v0.13).

### F-S04-70-10 [HIGH] -- Gate [2f]'s VERSION-1 convention mandates a false provenance claim

- **String:** 4 | **Position:** 12 | **Class:** D
- **Locus:** `build.py`, gate [2f]: `prov_match = re.search(r'repair build from v(\d+\.\d+)\s+R(\d+)\s+audit', status_text)` followed by an assertion that `prov_ver == VERSION - 1`.
- **Substance:** The gate captures both the version and the round number, then validates only the version, and only against VERSION-1. It never checks that round R actually audited that version. The convention holds only while every version is audited before its successor. The v0.69/v0.70 two-step broke that assumption, so the gate now compels "from v0.69 R27 audit" and rejects the truth. Probe 10: substituting v0.68 yields `FAIL: Status provenance v0.68 == v0.70 - 1`.
- **Required repair:** Validate the provenance version against `r27_findings_index.json["version"]` and the round number against `["round"]`, not against a positional arithmetic assumption.
- **Falsifier:** Probe 10 rerun passes; a Status line naming a version the index does not name fails.
- **Cross-reference:** F-S04-70-08; F-S01-54-02 (the finding that created gate [2f]).

### F-S04-70-11 [HIGH] -- The document's last visible line is outside every seal and every gate

- **String:** 5 (Temporal Integrity) | **Position:** 16 | **Class:** D
- **Locus:** `xz_protocol_v0_70.md`, final line, after the Provenance block. `*End of XZ Protocol v0.70 draft candidate.*` occurs **twice**: once inside the sealed v0.70 entry (tagged `[COMPUTED: generate_terminal_line]`) and once in the unsealed tail.
- **Substance:** Entry sealing and the FULL_SECTION_27 computation both terminate at the `*Provenance and review status.*` marker (`build.py` lines 58, 66, 260, 460). Everything after it is unsealed. Gate [10h] tests `terminal_expected in protocol` with no uniqueness or position constraint, so the sealed copy alone satisfies it. Probe 8: rewriting the tail line to `*End of XZ Protocol v0.42 draft candidate.*` yields 70/70 seals verified, PRIOR_HISTORY derived, `[10h] PASS: Terminal line matches v0.70`, and **BUILD PASSED: all checks GREEN**. The last thing a reader sees can name any version at all. Probe 7 confirms the sealed copy *is* protected, so the exposure is specific to the duplicate.
- **Required repair:** Assert the terminal marker occurs exactly once, and that its offset precedes the Provenance marker; or extend the seal terminus past the tail.
- **Falsifier:** Probe 8 rerun fails the build.
- **Cross-reference:** Boundary item 6 (seal terminus at Provenance marker) discloses the unsealed region but not the duplicated claim inside it; substrate-of-record uniqueness.

### F-S04-70-12 [MEDIUM] -- Declaration pattern 4 admits bare references as declarations; attribution is file-order dependent

- **String:** 1 | **Position:** 1 | **Class:** D
- **Locus:** `extract_findings.py`, `DECLARATION_PATTERNS[3]`: `(F-S\d{2}-\d{2,3}-\d{2,3}[A-Z]?)\s*\(?(HIGH|MEDIUM|LOW|INFORMATIONAL|CRITICAL)\b`.
- **Substance:** The pattern requires only whitespace and an optional paren between an ID and a severity token, so an inline cross-seat reference of the form "F-S01-70-04 HIGH" in *any* report is captured as a declaration. `build.py` iterates `sorted(report_files)` and takes first-occurrence-wins, so a seat whose filename sorts earlier can define another seat's finding severity. On these bytes no attribution mismatch occurs (checked: every captured ID's seat number matches its source file), so the exposure is latent, not live.
- **Required repair:** Require declaration context -- line start, heading, bold, or table cell -- for pattern 4, or reject captures whose seat number does not match the source filename.
- **Falsifier:** A report containing only a bare reference to another seat's ID yields no extraction from that file.
- **Cross-reference:** F-S04-70-01 (same module).

### F-S04-70-13 [MEDIUM] -- `xz_protocol_boundaries.json` version field stale at 0.62 and ungated

- **String:** 2 | **Position:** 6 | **Class:** E (process)
- **Locus:** `xz_protocol_boundaries.json:2`: `"version": "0.62"`.
- **Substance:** The file ships as a manifested member of the v0.70 packet carrying a version field eight versions behind. Gates [2h] and [10f] verify the item count (35 == 35) and the ENUMERATED tag, and nothing verifies the version field. A reader cannot tell from the file whether the boundary set was reviewed at v0.70 or merely carried. This seat holds no v0.62 bytes and cannot determine whether the set is genuinely unchanged.
- **Required repair:** Stamp the file at each version that ships it and add a version-parity check to gate [10f]; or state in the file that the version field records last substantive change, and gate that reading.
- **Falsifier:** Gate output includes a boundaries-version check.
- **Cross-reference:** Boundary item 20 (no boundary-retirement mechanism); boundary-30 staleness class at R15/v0.56.

### F-S04-70-14 [LOW] -- "Zero unmanifested members" is false of the manifest itself

- **String:** 6 (Methodology Audit) | **Position:** 18 | **Class:** C (disclosed)
- **Locus:** v0.70 entry repair (6); `PACKET_SHA256SUMS` (27 lines, 28 files extracted).
- **Substance:** The manifest cannot contain its own digest. The claim is therefore false as universally stated and true under the intended scope. Boundary item 10 (packet non-closure) discloses the class, so this is Class C rather than Class A. Separately, the ten dispatch-layer files (AUDIT_CONTEXT, DISPATCH, METHODOLOGY, CI_METHODOLOGY, R27_TRIAGE, R27_REPORTS, and the three duplicated packet members plus EXECUTABLE_PACKET) ship unmanifested; the three duplicates were verified byte-identical to their manifested counterparts.
- **Required repair:** Scope the claim ("every packet member other than the manifest") or publish the manifest digest in the entry text where the seal chain covers it.
- **Falsifier:** The entry states the scope, and the manifest digest appears inside a sealed entry.
- **Cross-reference:** Boundary items 7 and 10; F-S01-68-11 / F-S04-68-09.

### F-S04-70-15 [LOW] -- Em-dash characters in shipped `.py` tooling, no gate covers them

- **String:** 1 | **Position:** 1 | **Class:** E
- **Locus:** `extract_findings.py`: three U+2014 characters (docstring examples and the `[-\u2014]+` (hyphen or em-dash character class) character class in `DECLARATION_PATTERNS[0]`).
- **Substance:** The regex use is functional -- it lets the extractor read seat reports that use em-dashes -- but the shipped `.py` file carries characters the program's em-dash policy excludes from `.py` sources, and `build.py` implements no em-dash gate at all (the [4] Brand string sweep covers brand strings only). `R27_S02_REPORT.md` carries 47; those are covered by the Section 23 ship-unmodified rule and F-OPUS5-17-09, and are Class C.
- **Required repair:** Replace the docstring em-dashes with the escape `\u2014` in the character class and double hyphens in prose; add an em-dash gate over normative files and tooling.
- **Falsifier:** A codepoint sweep over `*.py` returns zero U+2013/2014/2015 outside escaped literals.
- **Cross-reference:** F-OPUS5-17-09 (reports, DISCLOSED NOT CLOSED).

### F-S04-70-16 [INFORMATIONAL] -- Seat non-independence: dispatch label, executor, and memory state all diverge

- **String:** 6 | **Position:** 21 | **Class:** E
- **Locus:** `DISPATCH.txt` header: "Model: Gemini 3.1 Pro | Mode: FRESH. No prior context. No held bytes."
- **Substance:** Executed by Claude Opus 5 carrying persistent lineage memory of R7-R27. Three independence assumptions in the dispatch header are false of this seat: model family, freshness, and absence of prior context. The A-X3 non-collusion axiom in Section 22.4 assumes cross-family seats; a round whose seats are relabelled rather than re-routed does not test what the axiom needs tested. Disclosed here so the triage can weight this seat correctly rather than as an independent Gemini observation.
- **Required repair:** Either route S04 to the named model or amend the dispatch header to name the executor and its memory state.
- **Falsifier:** Dispatch header and report S-0 agree on model, mode, and held-byte state.
- **Cross-reference:** Seat-label drift, sixth consecutive round; F-S01-68-12; seat-non-independence class at R9/v0.44.

### F-S04-70-17 [INFORMATIONAL] -- `FINDING_ID_RE` is dead code

- **String:** 1 | **Position:** 1 | **Class:** E
- **Locus:** `extract_findings.py:27`.
- **Substance:** Defined and never referenced (one occurrence in the file). It is the only extraction-shaped regex in the module that carries the C-suffix, which is plausibly why the repair was believed to have landed.
- **Required repair:** Delete it, or make it the single source of the ID grammar that the five declaration patterns compose from.
- **Falsifier:** Every regex in the module is either referenced or absent.
- **Cross-reference:** F-S04-70-01.

### F-S04-70-18 [INFORMATIONAL] -- Fresh-environment build is not reproducible without an out-of-packet install

- **String:** 1 | **Position:** 1 | **Class:** C
- **Locus:** `build.py` gate [5]/[8]; observed at intake.
- **Substance:** On a clean container `python3 build.py` returns `BUILD FAILED: 2 error(s)` -- `FAIL: pytest is installed (rc=1)` and `FAIL: Test count parsed from pytest output`. The advertised 279 PASS / 0 FAIL is conditional on a `pytest` install that ships neither in the packet nor in the extraction recipe. The gate behaviour is correct and fail-closed; the *instruction set* is incomplete. Boundary item 11 (fresh-execution non-reproducibility) discloses the class, so this is Class C.
- **Required repair:** Add the install step to the AUDIT_CONTEXT extraction recipe, and pin the version.
- **Falsifier:** A seat following AUDIT_CONTEXT verbatim on a clean container reaches BUILD PASSED without improvisation.
- **Cross-reference:** Boundary item 11; boundary item 7 (execution environment unsealed).

**Severity ledger: 1 CRITICAL / 10 HIGH / 2 MEDIUM / 2 LOW / 3 INFORMATIONAL = 18 findings.**

**Class ledger: A = 8 (F-01, -02, -03, -04, -05, -06, -07, -08) | B = 0 | C = 3 | D = 4 | E = 3.**

---

## S-8 Barzakh self-check

Three questions were put to each finding: (a) is the locus quoted from shipped bytes rather than recalled; (b) would the finding survive if this seat's lineage memory were deleted; (c) is the falsifier executable by a seat that disbelieves me.

- All 18 findings quote loci from the extracted packet. No finding rests on a prior-round recollection.
- Fifteen survive memory deletion outright. F-S04-70-16 is *about* the memory and cannot. F-S04-70-13 and F-S04-70-18 invoke prior-version context but are established from the shipped bytes alone.
- Every finding's falsifier is a command or a grep runnable on the packet. The seven load-bearing ones were run in this round and are recorded in S-5 with their outputs.
- **Where this seat could be wrong:** F-S04-70-13 assumes the boundaries version field should track the protocol version; if the field records last-substantive-change by design, the finding reduces to a documentation gap. F-S04-70-14 is scope-reading dependent and is filed at LOW for that reason. F-S04-70-05 assumes the index's `unique_findings_noted` list carries disposition semantics; if it carries only convergence semantics, the contradiction is between the entry's NOTED framing and the repair list rather than between entry and index, and the finding stands with a narrower locus.
- **What this seat could not test:** boundary item 32 (self-consistent resealing) -- no held prior bytes. The entire body layer (axioms, Sidrat clause, furqan) -- disclosed, not tested, by design. Whether the four shipped R27 reports are the authentic ones: gate [13] compares index to reports with no external anchor, so a producer controlling both surfaces satisfies it. That is boundary item 32 restated at the report layer, and it is the correct place to look at R29.

---

## S-9 Prediction scorecard results

| ID | Prediction | Confidence | Result | Evidence |
|---|---|---|---|---|
| P1 | sha256sum all OK | HIGH | **TRUE** | 27/27 OK |
| P2 | pytest 186 GREEN | HIGH | **TRUE** | 186 passed, 5.41s |
| P3 | build.py 0 FAIL | HIGH | **TRUE** (conditional) | 279 PASS / 0 FAIL after pytest install; see F-S04-70-18 |
| P4 | Gate [13] fires | HIGH | **TRUE** | fires on 4 shipped reports |
| P5 | 0 missing, 0 phantom | HIGH | **TRUE** | verified computed, not narrated, via probes 2-3 |
| P6 | 0 severity mismatches | HIGH | **TRUE** | mutation lands |
| P7 | 70 ENTRY seals verify | HIGH | **TRUE** | 70/70 |
| P8 | PRIOR_HISTORY matches | HIGH | **TRUE** | `c75a0ac4...` derived |
| P9 | Section 22.4 present | HIGH | **TRUE** | line 722, 5 axioms |
| P10 | Class A only at String 6 | MEDIUM | **FALSE** | 8 Class A at Strings 1, 2, 3; zero at String 6 |
| P11 | Zero Class A at String 1 | HIGH | **FALSE** | F-S04-70-01, -02 |
| P12 | H = 1.0 continues | MEDIUM | **TRUE** | 22/22, R7-R28 |
| P13 | Section 0.1 current to v0.70 | HIGH | **FALSE** | F-S04-70-07 |
| P14 | FB-7b current through R27 | HIGH | **TRUE** | row terminates "R27 (v0.68): 4 seats, all HALTed" |
| P15 | All shipped files manifested | HIGH | **PARTIAL** | 27/28; manifest unmanifested (F-S04-70-14) |

**Score: 11 TRUE, 3 FALSE, 1 PARTIAL.** The three failures are exactly the three the dispatch was built to test. The producer's HIGH-confidence predictions about the code layer (P11) and the prose layer (P13) both failed; every prediction about tool output passed. The gap between "the tools return green" and "the claims about the tools are true" is the whole of this round.

---

## S-10 Verdict, key question, Bearer 4

### Verdict

**HALT-AND-RETURN-TO-PRODUCER.** 1 CRITICAL, 10 HIGH.

### Key question: does v0.70 achieve Goedel confinement?

**No.** Confinement requires every Class A at positions 18-21 and zero at positions 1-17. Observed: **8 Class A, all at positions 1-9; zero at positions 18-21.** The distribution is not merely non-confined -- it is the *inverse* of confinement. String 6, the surface predicted to hold the residual, is the cleanest layer in the instrument this round, carrying only one Class C and one Class E.

The v0.70 build did what it said at the logic level. Gate [13] is genuinely bidirectional, genuinely severity-aware, genuinely extractor-based; three mutation probes confirm all three axes and a benign control confirms no false positive. That is real progress and should be recorded as such. What did not land is the layer above the logic: the claim that the logic is fail-closed (it is not), the claim that the C-suffix grammar was unified (it was not), the claim that three zeros were computed (they were literals), and the count of items in the entry's own NOTED list.

### Bearer 4 assessment

**Bearer 4: FALSE.** Not UNDER TEST -- tested and answered negatively, with 8 Class A findings outside String 6.

Recommended bearer table entering R29:

| Bearer | Status | Change |
|---|---|---|
| 1. Append-only | TRUE | unchanged; 70/70, probe 6 fires three detectors |
| 2. Code correctness | **FALSE** | changed. 186 GREEN holds, but a shipped repair is phantom and a gate narrates its result |
| 3. Surface narrowing | **FALSE** | changed. The defect did not stay in prose; it re-entered code |
| 4. Goedel confinement | **FALSE** | changed from UNDER TEST. Inverse distribution observed |
| 5. Cross-vendor witness | FALSE | unchanged, and see F-S04-70-16: seats are being relabelled, not re-routed |
| 6. Axiom disclosure | TRUE | unchanged; Section 22.4 intact |
| 7. Methodology | FALSE | unchanged; but String 6 is the only Class-A-free layer this round |
| 8. The furqan | UNKNOWN | lead's call |

### The finding to put in front of the lead

Two gates now enforce byte-false claims. Gate [10i] fails when Section 0.1 is corrected; gate [2f] fails when the Status line is corrected. Both were built to catch version-token staleness, and both have become its mechanism -- one because it tests a substring against the whole document while carrying a section's name, the other because it encodes positional arithmetic (`VERSION - 1`) in place of a lookup against the index that actually records what was audited.

This is not a new defect class so much as the old one turned inside out. The program's recurring failure has been *claims about mechanisms that do not hold*. What v0.70 shows is *mechanisms that enforce claims that do not hold*. A producer following the gates faithfully now produces a false document, and a producer correcting the document breaks the build. That is a closed loop, and it will not open by adding gates. The exit is to make every VERSION-1 gate read its expectation from a shipped artifact -- the findings index knows the round and the audited version -- rather than compute it from the current version number.

### Priority order for v0.71

1. F-S04-70-01 (CRITICAL) -- real C-suffix repair; reopen F-S04-68-08.
2. F-S04-70-09 and F-S04-70-10 -- de-arithmetise both gates, then land F-S04-70-06, -07, -08 in the same build.
3. F-S04-70-03 -- make gate [13] fail-closed.
4. F-S04-70-02 -- delete the narrated summary line.
5. F-S04-70-04 and F-S04-70-05 -- one disposition per finding, in one place, with a gate over the NOTED count.
6. F-S04-70-11 -- terminal-marker uniqueness and position.

### Cross-vendor recommendation for R29

The producer is Opus 4.6 and this seat executed as Opus 5. R29 needs at least two genuinely non-Claude carrying seats on the same bytes, actually routed rather than labelled, and at least one seat holding v0.70 bytes externally so boundary item 32 becomes testable. Until a seat holds prior bytes outside the producer's control, gate [13]'s comparison of index to reports proves only that the producer is consistent with itself.

---

*Report: R28, Seat S04, XZ Protocol v0.70. Verdict HALT. 18 findings, 8 Class A, zero at String 6.*
*Class A recurrence R7-R28: 22/22. H = 1.0. Laplace P(Class A at R29) = 23/24 = 0.958.*

---

# Bismillah ir-Rahman ir-Rahim
