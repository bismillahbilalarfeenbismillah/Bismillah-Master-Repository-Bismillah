# Bismillah ir-Rahman ir-Rahim

# R0174 -- XZ Protocol v0.42 — Seat B Fresh Carrying Audit (Binding)

**Chronological Index:** 459 of 995  
**Date:** 2026-08-06  
**Section:** IV. XZ Protocol  
**Source File:** SEAT_B_AUDIT_XZ_v0.42.md.txt  
**Source Format:** txt  
**SHA-256:** `9b828e5e718a3eb733eb16d211a1282193b4afbf63eb2955ef82c0f51b5745b9`  

---

## R0174 · XZ Protocol v0.42 — Seat B Fresh Carrying Audit (Binding)

- section: IV. XZ Protocol
- source_file: SEAT_B_AUDIT_XZ_v0.42.md.txt
- source_format: txt
- text_sha256: 9b828e5e718a3eb733eb16d211a1282193b4afbf63eb2955ef82c0f51b5745b9

# XZ Protocol v0.42 — Seat B Fresh Carrying Audit (Binding)

**Seat:** Seat B (carrying, binding) — fresh instance, non-producer
**Model:** Kimi K3 (Moonshot AI)
**Artifact:** XZ Protocol v0.42 (recovery build from v0.41 append-only corruption)
**Author of artifact:** Bilal Syed Arfeen (no organizational affiliation)
**Audit date:** 2026-08-07
**Round:** Convergence Round 1 on repaired bytes (post-v0.41 recovery)
**Dispatch:** AUDIT_PROMPT_v42_COMMON.md + SEAT_B_COVER.md
**Method:** Independent lead-seat verification of every dispatch item plus a five-lane parallel deep audit (Sections 0–8, 9–17 ×2 cross-validating, 18–26, code/build, Section 27 v0.1–v0.39). Every finding below was independently re-verified by this seat against shipped bytes (grep / python3 / sha256sum) before inclusion.

---

## 1. VERDICT: **HALT** (binding)

**Twelve Class A (byte-level error) findings and one Class B (concealed-defect) finding are confirmed on the shipped bytes.** Under the dispatch rule ("HALT: At least one Class A or Class B finding exists. The artifact cannot proceed") and the Seat B cover ("If you find any Class A or Class B finding, you MUST issue HALT"), this verdict is mandatory, not discretionary. Class A is outside the Section 22 item 7 persistent-architectural-HALT exception by that item's own text.

**The recovery itself verifies.** The v0.41 corruption is genuinely and completely repaired: packet integrity rc=0, build green with zero WARN pathways, the full PRIOR_HISTORY chain reconstructs from current bytes and matches every prose-quoted value (21/21) and the final shipped line (`632fda34…`). This HALT is **not** for the recovery mechanics. It is for prose-level truth defects elsewhere in the document — the Axiom-3 failure class (narrating values from memory rather than computing from bytes) — including one instance in the recovery build's own front matter (F-SB-08) and several in sealed historical entries that no append-only correction has ever addressed. This is precisely the failure mode FB-8 names: governance-layer prose claims are not independently verifiable from bytes alone; this seat verified them against bytes and twelve of them failed.

**Consequence:** FB-8 remains OPEN. A repair build (v0.43) is required. All Class A items are surgically repairable (Section 6).

---

## 2. Packet integrity (dispatch task 1) — VERIFIED

| Check | Expected | Observed | Result |
|---|---|---|---|
| `PACKET_SHA256SUMS` self-digest | `a0f00641…4dbab1` | identical | PASS |
| Protocol text digest | `740d918c…15bb7` | identical | PASS |
| Protocol text size | 263,439 bytes | 263,439 | PASS |
| Packet members | 16, no self-entry | 16, no self-entry | PASS |
| `sha256sum -c PACKET_SHA256SUMS` | rc=0 | rc=0, 16/16 OK | PASS |
| `python3 build.py` | "BUILD PASSED: all checks GREEN", zero WARN | rc=0, exact string, 0 WARN, 0 FAIL | PASS |
| Independent pytest re-run | green | `186 passed` (canonical six-suite invocation), rc=0 | PASS |

Environment note: gate [8] hard-fails closed when pytest is absent (`FAIL: pytest is installed`); after installing pytest the build is fully green. Fails-closed is the correct direction (F-ADJ19-05: absence is not green); see F-SB-17 family for gate-limitation notes.

## 3. Recovery verification (dispatch task 2) — VERIFIED

This seat re-implemented the full seal-chain derivation from shipped bytes, independent of build.py:

1. **42/42 ENTRY seals** recomputed from current bytes match `HISTORY.sha256`; `FULL_SECTION_27` recomputed matches (`b4aacc01…`).
2. **Prose PRIOR_HISTORY values, entries v0.19–v0.40:** 21 genuine chain values (the v0.21 entry quotes none — corroborated by the v0.22 entry item (3); build.py's derivation correctly recurses through that level). A blind same-line regex of the v0.41 corruption type matches exactly **22 occurrences** (the 22nd is a same-line false hit on a v0.17 report digest inside the v0.20 entry). All 22 occurrences are **pairwise distinct** — no single-constant overwrite exists on these bytes.
3. **Full chain verification (stronger than the shipped gate — see F-SB-18):** for every v0.19 ≤ n ≤ v0.40, the prose-quoted value equals sha256 of the HISTORY.sha256 reconstructed for v0.(n−1) from current bytes. **21/21 MATCH.**
4. **Final link:** shipped `PRIOR_HISTORY 632fda343fcdb24a8c38b486b71ed8434bffb366d24e055d3efe9f88575f290a` == this seat's independent reconstruction of the v0.41 HISTORY.sha256 == the v0.42 entry's closing quote.
5. **Gate [9b] hard assertion:** every [9b] check routes through `check()` → `errors` → `sys.exit(1)`. Token sweep of build.py: **zero `WARN` occurrences**; no WARN pathway exists. The v0.41 concealment mode (assertion → print(WARN)) is absent.
6. **Residue sweep:** the v0.41 overwrite constant `a58c684c…` occurs exactly once packet-wide — inside the v0.41 RETRACTED entry's own narrative naming it. No residue in any seal position.

## 4. New-substance verification (dispatch task 3) — VERIFIED

| # | Required fact | Evidence | Result |
|---|---|---|---|
| 1 | Section 0.1: "This document is v0.42 DRAFT CANDIDATE" | line 16, exact; not FROZEN, not v0.40 | PASS |
| 2 | Front-matter status token == Section 0.1 status token (gate [2c]) | both `DRAFT`; [2c] PASS; independently grep-confirmed | PASS |
| 3 | FB-8 row in Section 25 with governance-convergence exit condition | present, OPEN; exit: "two non-producer carrying seats from different families return non-HALT on bytes where every prose claim in the current entry is verified against shipped bytes by grep before sealing" | PASS |
| 4 | v0.41 entry exists, marked RETRACTED | "**v0.41 (2026-08-06): RETRACTED -- append-only corruption.**" | PASS |
| 5 | v0.42 entry with real 64-hex PRIOR_HISTORY (not PLACEHOLDER) | `632fda34…` chain-verified; the sole "PLACEHOLDER" token is the narrative "(not PLACEHOLDER)" in F-CONV2-06's closure note | PASS |
| 6 | Append-only correction (aa) for v0.40's false F-R6META-01 CLOSED claim | present in v0.42 entry; v0.40 entry preserved verbatim (still carries the false CLOSED line; its seal verifies) | PASS |

## 5. Findings register

Severities: CRITICAL / HIGH / MEDIUM / LOW / INFORMATIONAL. Every finding re-verified by this seat on shipped bytes. Subagent-origin IDs in cross-ref where applicable.

### 5.1 Class A — byte-level errors (12)

**F-SB-01 -- MEDIUM**
- Locus: `xz_protocol_v0_42.md` Section 26.1 header (line 765) and table (lines 769–781); Section 27 v0.13 entry item (9).
- Substance: Header claims "The supplied program corpus (twelve distinct records)"; the table carries **13 data rows with 13 distinct records** (counted by this seat). The v0.13 entry item (9) records "the header count is corrected to twelve distinct records" as CLOSED — false on current bytes; no amendment entry records the addition of the thirteenth row (the BAF Application Brief v1 row appears in no amendment narrative). The exact Axiom-3 count-narration class this protocol polices.
- Class: A
- Disposition: **blocking**
- Cross-ref: F-S26-1 / F-S00-2 (dual independent discovery); FB-8 exit condition is the control designed to catch this.

**F-SB-02 -- MEDIUM**
- Locus: Section 27 v0.36 entry, ring-closure paragraph.
- Substance: The ring closure repeatedly cites "Section 0.2 consequence 1/2/3/4". Section 0.2 contains no enumerated consequences (`grep`: zero occurrences of "consequence" in §0.2); the four consequences are numbered in **Section 2.2** ("Four consequences are drawn now"). The v0.31 entry itself says "Section 2.2 consequence 4 added". The locus citation is false on shipped bytes inside a sealed verification paragraph; never explicitly corrected (v0.38 item (9) notes "ring-closure mislabeling" generically without this locus).
- Class: A
- Disposition: **blocking** (sealed entry — requires an append-only correction in the repair build)
- Cross-ref: F-A27-1.

**F-SB-03 -- MEDIUM**
- Locus: Section 27 v0.25 entry, register item (4).
- Substance: Item (4) states "the v0.22 fresh instance's namespace F-OP22C collided with the v0.21 one-round instance's namespace, causing three findings to be dropped." Every component is false of the record: (i) the v0.22 fresh namespace was **F-OP21S/F-OP21** (v0.22 preamble), not F-OP22C; (ii) F-OP22C is the **v0.23** namespace; (iii) no "one-round" instance existed at v0.21 (its instances were F-OP20 continuous and F-OP20F fresh); (iv) the three dropped findings were **F-OP21S-03/04/05**, whose omission the v0.23 correction (e) attributes to a D-3.7 violation, not a namespace collision. Carries a HIGH-severity label and an [ASSERTED] tag, but the record's own bytes contradict it; never corrected.
- Class: A
- Disposition: **blocking** (sealed entry — append-only correction required)
- Cross-ref: F-A27-2; F-SB-13 (same discipline family).

**F-SB-04 -- LOW**
- Locus: Section 12 (line 424) vs Section 13.3.4 (line 470) vs `xz_protocol_phase_a_intervals.py` lines 9–12 and `xz_protocol_phase_a_tests.py` line 5.
- Substance: §12 states undefined alpha "is handled as INDETERMINATE-ADJUDICATION under the **protocol-level scoring module's PA-Z4 rule**." §13.3.4 states PA-Z4 "is an adjudication-layer rule **outside the scoring module**"; the module docstring states PA-Z4 "is scoped out of the code and tested at the adjudication layer"; no code implements PA-Z4 (packet-wide grep: only scoping-out notes). The §12 locus attribution is false on shipped bytes; the rule's semantics are consistent everywhere (only ownership conflicts). Triple independently discovered (three audit lanes).
- Class: A
- Disposition: **blocking**
- Cross-ref: F-S08-1 / F-S17-1 / F-S26-2; protocol's own falsifier XZ-I3 (text/code divergence is a defect to be raised).

**F-SB-05 -- LOW**
- Locus: Section 22.2 (line 716).
- Substance: "This control covers the historically dominant failure mode (**seven recorded in-place mutations** at v0.4, v0.9, v0.11, v0.16, and v0.17)." The record now contains **eight**: the v0.41 entry records the eighth in-place mutation, self-described as "larger than all seven combined" — the same failure mode 22.2 characterizes, and the very event this recovery build answers. The recovery build did not update 22.2's count. (The five-version enumeration itself is accurate; the aggregate "seven recorded" is stale on current bytes.)
- Class: A
- Disposition: **blocking**
- Cross-ref: F-S26-3; F-SB-09.

**F-SB-06 -- LOW**
- Locus: `xz_protocol_phase_a_intervals.py` line 330 ("Interval conjunct formally retired (PA-A5)"); `xz_protocol_phase_a_m3.py` line 22 ("recorded as amendment entry PA-A12").
- Substance: Packet-wide grep for `PA-A[0-9]+` finds exactly these two loci. No PA-A* amendment entries exist in Section 27 or anywhere else in the packet. The docstring claim "recorded as amendment entry PA-A12" is false on shipped bytes — dangling provenance pointers (the substances themselves are properly recorded under §13.3.3/§13.3.5 and the v0.2 entry).
- Class: A
- Disposition: **blocking**
- Cross-ref: F-S17-2.

**F-SB-07 -- LOW**
- Locus: Section 17 item 11 vs Section 15.3, Section 11.2, Section 18.4, `xz_protocol_phase_a_m3.py` line 40; Section 25.
- Substance: §17.11 claims "Section 25 lists every value this draft does not fix." Counterexamples on bytes: (a) §15.3 invokes "a pre-registered floor" for the dual-evaluable frame — no floor value appears anywhere and "floor" is absent from Section 25; (b) §11.2's "closed list" of UNKNOWN reason codes enumerates five with non-exhaustive "includes" and the full list is fixed nowhere, unlisted in Section 25; (c) the code freezes a numeric wall-clock budget (`FROZEN_BUDGET_MINUTES = 480.0`, pinned by a test) while the text references only "the fixed budget" with no value ("480" occurs zero times in the protocol text) and Section 25 is silent. The universal claim is overbroad on shipped bytes.
- Class: A
- Disposition: **blocking**
- Cross-ref: F-S17-3; CR-7 (no invented thresholds) — the values are honestly unfixed; the *claim about their listing* is what fails.

**F-SB-08 -- LOW**
- Locus: Front matter (line 4).
- Substance: "**Version:** 0.42, draft candidate, **2026-08-06**" — the date token equals the **retracted v0.41** entry's date (2026-08-06), not the v0.42 entry's date (2026-08-07). The dispatch itself dates the artifact 2026-08-07. Gate [2c] binds the status token but no gate covers the date. This is the F-CONV1-02 defect class — a stale token surviving a version bump in front matter — recurring inside the recovery build whose correction (aa) describes that very class.
- Class: A
- Disposition: **blocking**
- Cross-ref: F-S00-3; correction (aa); F-SB-05 (same recovery-completeness family).

**F-SB-09 -- LOW**
- Locus: Section 27 v0.41 entry (RETRACTED).
- Substance: The entry calls v0.41 "the eighth recorded in-place mutation … (after v0.4, **v0.9 x2**, v0.11 x2, v0.16, **v0.17**)". The multiplicities are inverted against the corroborated record: v0.9 is recorded as **one** mutation (v0.10 "second append-only violation"; v0.13 F-XZ12-OP-06 "v0.9's mutation was the second"), v0.17 as **two** (v0.18 (a) "the sixth and seventh"). The compensating errors preserve the total (seven), so "eighth" survives only the naive tally; under the per-locus convention the v0.19 entry (F-OP18-06) records "the tally should be eight" and expressly declines an ordinal. Mitigated: the entry is banner-retracted, so the defect is disclosed in situ — but this specific inconsistency is not among the stated retraction grounds.
- Class: A (disclosed by retraction banner)
- Disposition: disclosed / **blocking for the record** (an append-only correction should name it, per the protocol's correction discipline)
- Cross-ref: F-S26-5 / F-S00-1 / O-1 (triple discovery); F-SB-05.

**F-SB-10 -- LOW**
- Locus: Section 27 v0.27 entry preamble.
- Substance: "GPT-5.6 Sol adversarial seat VOID -- Perplexity routed through Claude instead of GPT (routing failure, **see v0.26 entry**)". The v0.26 entry contains no routing-failure account; its only "routing" token (F-OP25-ALL-07) refers to the v0.25 round. Temporally the GPT void is an artifact of the v0.26 carrying round, which postdates the v0.26 entry — the pointer cannot have a referent. Undisclosed.
- Class: A
- Disposition: **blocking** (sealed entry — append-only correction required)
- Cross-ref: F-A27-3.

**F-SB-11 -- LOW**
- Locus: Section 27 v0.36 entry, closing paragraph.
- Substance: "The 186-test suite is GREEN across all thirty-six versions" is false of the record: the v0.3 entry records "Six suites, **185** tests" and the v0.15 entry records the increase "from 185 to 186". The 186-test suite has existed since v0.15 (22 versions, not 36). [ASSERTED]-tagged; never corrected.
- Class: A
- Disposition: **blocking** (sealed entry — append-only correction required)
- Cross-ref: F-A27-5.

**F-SB-12 -- LOW**
- Locus: Section 27 v0.25 items (10)/(12) vs v0.26 items (8)/(9) and the anchored series v0.21–v0.23.
- Substance: Ungated-share series is anchored: v0.21 "third", v0.22 "fourth", v0.23 "fifth" consecutive round — implying v0.24 sixth, v0.25 seventh, v0.26 eighth. v0.25 claims "sixth" (one low); v0.26 claims "eighth" (anchor-consistent). PDF-unbound series: v0.23 "fourth", v0.25 "fifth", v0.26 "seventh" — irreconcilable under any single counting convention (at least one member of the v0.25/v0.26 pair is false). Same pattern for "[9c] arity-one third round" (v0.25) vs "fifth" (v0.26). [ASSERTED]-tagged process metrics; no correction exists.
- Class: A
- Disposition: **blocking** (sealed entry — append-only correction required)
- Cross-ref: F-A27-4; F-OPUS5-17-06 (ordinal-underivability disclosure).

### 5.2 Class B — concealed defects (1)

**F-SB-13 -- LOW**
- Locus: Section 27 v0.26 entry preamble.
- Substance: The preamble carries six instance verdicts (A CONDITIONAL PASS; B HALT advisory; C APPROVE-WITH-SURGICAL; D/E HALT advisory; F CONDITIONAL PASS) with **zero provenance tags** — verified as the only verdict-bearing preamble in v0.19–v0.38 without one. The record's own F-OP18-12 discipline (v0.19 item 11) requires tags precisely so unverifiable seat claims are marked as such; the omission presents unverifiable verdicts without the marker that discloses their status. The concealment is the defect. Never disclosed.
- Class: B
- Disposition: **blocking** (sealed entry — append-only correction required)
- Cross-ref: F-A27-6; F-SB-03.

### 5.3 Class D — gate/test limitations (6)

**F-SB-14 -- MEDIUM**
- Locus: `xz_protocol_control_graph.py` lines 123–128 (H-2 enforcement); `test_xz_protocol_control_graph.py`.
- Substance: The v0.3 entry claims "WithinAuthAssessment enforces verdict == compute_verdict(edges) at construction (H-2)." Enforcement is present (direct probe: mismatched verdict raises ValueError), but **no test pins it**: deleting the H-2 block in a scratch copy leaves all 18 control-graph tests GREEN. A regression removing H-2 would ship green.
- Class: D
- Disposition: noted
- Cross-ref: F-CODE-1.

**F-SB-15 -- LOW**
- Locus: `xz_protocol_condition_a.py` lines 254–264, 354–355; CAT-2 test.
- Substance: All six strata have non-empty BASELINE_PROFILEs, so `A_NOT_APPLICABLE` is unreachable via `evaluate_boundary`; the `is_dual_evaluable` exclusion branch is reachable only by hand-construction; no test exercises either path. The CAT-2 test itself concedes "NOT-APPLICABLE is unreachable from normal strata" — its named risk ("A-NOT-APPLICABLE must not enter the S1 denominator") is unpinned. Correct-by-construction, dead-under-current-profile.
- Class: D
- Disposition: noted
- Cross-ref: F-CODE-2.

**F-SB-16 -- LOW**
- Locus: `test_xz_protocol_source_frame.py` lines 46–53 (`test_installation_runtime_may_be_empty`).
- Substance: Sole assertion is `isinstance(sources, list)` — the function returns a list by construction, so this test **cannot fail** under any manifest content; it is counted in the "29 tests" claim and hence in the 186. Intent is documented in its docstring (non-concealing → reclassified from the code lane's initial Class B), and exact pins at lines 165–173 (0 and 2 sources) preserve protection. (Lead reclassification: the dispatch's Class B requires concealment-as-defect; this is an openly-documented vacuous test — a test-gate limitation.)
- Class: D
- Disposition: noted
- Cross-ref: F-CODE-3.

**F-SB-17 -- LOW**
- Locus: `build.py` gates [5] (lines 266–267), [6] (273–275), [7] (281–282).
- Substance: Prose gates are substring-presence, not locus-pinned: `"186" in body`, `"16-source" in body`, and the PA-Z14 string checks pass if the token appears anywhere. On current bytes "186" occurs exactly once, so corruption is caught today (mutation probe confirmed FAIL); the residual is authoring-time fragility, not forgery (any byte mutation trips [12]). Same disclosed family as "[9c] arity-one regex" and "[3c] single-line citation evasion".
- Class: D
- Disposition: noted
- Cross-ref: F-CODE-5; v0.42 standing boundaries.

**F-SB-18 -- LOW**
- Locus: `build.py` `derive_prior_history` (lines 98–134).
- Substance: The derivation anchors each level on the **first scrapeable prose quote** in the target entry (v0.40's quote anchors the shipped v0.42 derivation) and never chain-verifies an intermediate quote against reconstruction at that level; only the final shipped line is compared. Consequently a *complete, self-consistent* mutation of the prose quotes plus regenerated seals passes [9b] **without** control of build.py — a sharper residual than Section 22.2's framing ("a forger who also controls build.py …"). For these bytes this seat closed the gap by full chain verification (21/21 quotes == reconstruction), so no byte-level error exists — the limitation is the gate's. External anchors (22.2 (a)(b)(c)) remain the actual terminus, as disclosed.
- Class: D
- Disposition: noted
- Cross-ref: Section 22.2; standing boundaries ("cb67f222 termination literal", "packet non-closure").

**F-SB-19 -- LOW**
- Locus: Section 9.3 vs Section 16.2 (XZ-S5).
- Substance: §9.3 voids any Track 2 decision computed on a non-PRE_BOUNDARY packet; XZ-S5 as registered fires only when a counted S1 case uses post-cutoff evidence. Regime mixing without post-cutoff use in a counted case falls outside XZ-S5 as written (nearest cover XZ-I2/CR-11); the result labels also diverge ("void" vs "FALSIFIED"). A coverage gap between the stricter body rule and its falsifier — stated openly, not concealed.
- Class: D
- Disposition: noted
- Cross-ref: F-S26-6.

### 5.4 Class C — disclosed boundaries (confirmed accurate; no new ones found)

This seat confirmed the accuracy of the artifact's disclosures rather than adding to them: gate [9e] silent vacuity (disclosed as persisting F-CONV1-10; source-confirmed zero `check()` calls when no pattern matches); the 22-item standing-boundaries list in the v0.42 entry (count verified; spot-verified members all true on bytes — cb67f222 termination literal, [9d] word-list cap at fifteenth, [9c] DOI-resolution blindspot, packet non-closure, execution environment unsealed, seal terminus at Provenance marker, etc.); the 13-item persisting-findings list (F-CONV1-02, -04, -06, -07, -08, -09, -10, -12, -13, -14, -15, -16, F-CONV2-07) with 10 closed + 13 persisting = 23 = 24 reported findings − 1 merged pair (arithmetic verified); unseeded-but-outcome-neutral `secrets.token_hex` provenance guards (disclosed in both module docstrings as "NOT a security boundary"); golden-vector environment pinning to numpy 2.4.4/scipy 1.17.1 (disclosed; cross-version reproduction at 1e-6 verified by the code lane).

### 5.5 Class E — measurements / observations (6)

- **E-1 (INFORMATIONAL):** Section 22 subsection order is 22.1 → 22.3 → 22.2 (insertion order never renumbered). Editorial; degrades citability of the item-7 exception. (F-S26-4)
- **E-2 (INFORMATIONAL):** "7 code modules and 5 test suites" vs the ubiquitous "six suites": the partition counts `xz_protocol_phase_a_tests.py` as a module (no `test_` prefix) while every test narrative counts it as the sixth suite; consistently applied across artifacts (trust roots repeats it), so a naming artifact, not a byte error — but it invites the miscount class of F-SB-01. (F-S26-7)
- **E-3 (INFORMATIONAL):** Gate [8] runs the six suites alphabetically; the protocol's stated canonical command lists kernel-first. Same file set; the prose command executes verbatim (186 passed); no order dependence observed. (F-CODE-8)
- **E-4 (INFORMATIONAL):** Cosmetic code items: `is_dual_evaluable` docstring/behavior nuance (intentional, pinned by CAT-2); duplicate docstring string-literal at control_graph.py:107; dead loop in `ConjunctVector.__post_init__`. (F-CODE-9)
- **E-5 (INFORMATIONAL):** "22 PRIOR_HISTORY values" counts blind-regex occurrences (21 genuine chain values + 1 same-line false hit on a v0.17 report digest in the v0.20 entry), all distinct and intact; the v0.41-side count is [ASSERTED] about bytes that do not ship, inside a retracted entry. Restoration completeness is cryptographically verified (Section 3). (Lead + O-2)
- **E-6 (INFORMATIONAL):** Historical note — the v0.19 entry (F-OP18-06) expressly declined to assert a mutation ordinal ("the tally should be eight" under the per-locus convention); the v0.41 entry asserted "eighth" anyway. Folded into F-SB-09; recorded here for the repair build's correction drafting.

## 6. Repair path (all surgical; no normative behavior change required)

1. **F-SB-01:** correct the §26.1 header to thirteen records (or remove a row) **and** record the thirteenth row's provenance in the new amendment entry; reopen the v0.13 item (9) CLOSED via an append-only correction.
2. **F-SB-04:** repoint §12's PA-Z4 attribution to the adjudication layer (matching §13.3.4 and the module docstrings).
3. **F-SB-05:** update §22.2 to eight recorded in-place mutations (adding v0.41).
4. **F-SB-06:** repoint the two docstrings to the real amendment loci (v0.2 entry / §13.3.3 / §13.3.5) or add PA-A* entries.
5. **F-SB-07:** narrow §17.11's universal (or list the floor, the reason-code list residue, and the code-frozen 480-minute budget in Section 25).
6. **F-SB-08:** set the front-matter date to 2026-08-07 (and consider extending gate [2c] to the date token).
7. **F-SB-02, F-SB-03, F-SB-09, F-SB-10, F-SB-11, F-SB-12, F-SB-13:** sealed-entry errors — correct exclusively by new append-only correction entries in the v0.43 entry (the (aa) pattern), never by editing the sealed entries.
8. **F-SB-14/15/16 (recommended, non-blocking):** pin H-2 with a mismatch-construction test; exercise the NOT_APPLICABLE path via hand-constructed disposition or delete the dead branch with a note; strengthen or remove the vacuous list-type test (keep the count honest).
9. **F-SB-17/18/19 (optional hardening):** locus-pin the prose gates; chain-verify intermediate quotes in `derive_prior_history`; align XZ-S5 with §9.3 or narrow the body rule.

## 7. What verified TRUE (load-bearing sample; full lane reports held by this seat)

- Packet identity, 16-member integrity, BUILD PASSED with zero WARN; 186/186 tests green across the canonical six suites (independently re-run twice).
- **Full PRIOR_HISTORY chain:** 42/42 entry seals, FULL_SECTION_27, 21/21 prose quotes == reconstruction, final link `632fda34…` == independent reconstruction of the v0.41 HISTORY.sha256.
- Kernel: 243 = 3⁵ exhaustive vectors, decisions match the three rules by independent oracle (ALLOW=1, DENY_FALSE=211, DENY_UNKNOWN=31); mutation probes fail as designed (kernel dominance inversion → 4 failures; Condition A dominance inversion → 4; PA-Z14 guard removal → 1; PA-Z5 guard removal → 1).
- 16-source frame (six categories; TRANSPARENCY_LOG unused, disclosed), five-channel WithinAuth graph, Condition A mandatory-attestation profile, adversarial CAT-1…CAT-9 mapping 1:1 onto Section 22 item 4's nine categories, 13 implemented PA-Z rules, T2 gates (30 min / 0.20 / excludes-zero / BCa), T5 ratio-only retirement, M5=200 / M6=240 enforced exactly.
- All eight Section 25 quoted digests byte-exact; all 9 body 64-hex tokens resolve (zero stale); manifest digest `f4cef44f…` byte-exact under the documented construction; default-discovery caveat true (117 vs 69).
- Section 22 item 7 exception text internally consistent with the carry narrative; "Class A is outside the exception" confirmed by the item's own exclusion clause.
- External (live-verified by the 18–26 lane via Zenodo API): §26.1 divergence note (record 21539816 = A5 title over SHUDP v0.5 files) and §26.2 dual-DOI record confirmed; openwall/NVD/GHSA URLs resolve with expected content.

## 8. Unverifiable-from-bytes claims (flagged; tagging assessed)

- All carrying/advisory seat verdicts, severities, and finding IDs (v0.19–v0.42) — reports do not ship; tagged [ASSERTED] throughout **except** the v0.26 preamble (F-SB-13) and v0.39's terse preamble metrics (partially untagged; noted for the repair build's correction sweep).
- Historical byte states (v0.40's §0.1 sentence, v0.41's corrupted bytes, per-version manifest digests v0.6–v0.41) — [ASSERTED]; current bytes are consistent with those narratives wherever checkable.
- SHVVP v0.8 / BSSG / SHUDP inheritance fidelity at content level — deposited instruments are not packet members; DOIs resolve; usage is internally consistent; [EXTERNAL] discipline observed.
- Golden-vector provenance (generated-by-this-revision vs edited-after) — not decidable from bytes; reproduces on execution and corroborated by an independent scipy BCa stream.

## 9. Convergence note for the chair

This HALT does not contradict the recovery narrative — it confirms its premise. The recovery build repaired the bytes and the gates (verified end-to-end), but FB-8's named failure mode is prose-truth under audit, and this fresh carrying round found twelve byte-false prose claims, eleven of them the Axiom-3 class the program exists to police, one of them in the recovery build's own front matter. Under the protocol's own rules this is a HALT, and the repair is cheap: every defect is a count, a pointer, a date, a locus, or a missing tag. This seat's verdict is binding and is recorded for the amendment record.

**Verdict: HALT.** Issued 2026-08-07 by Seat B (Kimi K3, fresh, non-producer, carrying, binding).

---

*Audit executed with independent tooling on the shipped packet (sha256sum -c rc=0; build.py BUILD PASSED, zero WARN; 186/186 pytest green). No packet file was modified at any point; all mutation probes ran in scratch copies outside the packet directory. Parallel verification lanes: Sections 0–8, Sections 9–17 (two independent lanes, convergent), Sections 18–26, executable artifacts (with mutation/sabotage probing), Section 27 entries v0.1–v0.39. Every candidate finding was re-verified by the lead seat against shipped bytes before admission to the register.*

---

# Bismillah ir-Rahman ir-Rahim
