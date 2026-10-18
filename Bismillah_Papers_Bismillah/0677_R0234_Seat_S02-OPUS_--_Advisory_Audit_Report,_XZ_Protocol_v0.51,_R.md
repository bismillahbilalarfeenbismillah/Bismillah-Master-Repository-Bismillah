# Bismillah ir-Rahman ir-Rahim

# R0234 -- Seat S02-OPUS -- Advisory Audit Report, XZ Protocol v0.51, Round 10

**Chronological Index:** 677 of 995  
**Date:** Undated  
**Section:** IV. XZ Protocol  
**Source File:** XZ_v51_R10_SEAT_S02_OPUS_REPORT.md  
**Source Format:** md  
**SHA-256:** `51bce0cd848f93c78b35e345ed7449f293048c136c03a2e9b1ea1c9cb529513d`  

---

## R0234 · Seat S02-OPUS -- Advisory Audit Report, XZ Protocol v0.51, Round 10

- section: IV. XZ Protocol
- source_file: XZ_v51_R10_SEAT_S02_OPUS_REPORT.md
- source_format: md
- text_sha256: 51bce0cd848f93c78b35e345ed7449f293048c136c03a2e9b1ea1c9cb529513d

# Seat S02-OPUS -- Advisory Audit Report, XZ Protocol v0.51, Round 10

**Seat ID:** S02 | **Family:** Claude Opus 5 (Anthropic) | **Type:** Fresh (no prior seat context loaded)
**Role:** ADVISORY -- non-carrying, non-binding (producer family; Section 22.1)
**Finding namespace:** F-S02-51 | **Version audited:** v0.51 | **Round:** R10
**Verdict:** HALT-AND-RETURN-TO-PRODUCER (advisory)
**Severity ledger:** 3 CRITICAL / 3 HIGH / 4 MEDIUM / 2 LOW
**Class ledger (Section 22.3):** 4 Class A / 1 Class B / 4 Class D / 1 Class E / 2 unclassified LOW

Auditor operated in **Mode A** with full substrate access: packet reconstructed on disk, build.py and all six test suites executed, eight mutation builds constructed and run. Substrate-claim verification confidence **high**.

---

## 0. Reconstruction and baseline

| Step | Claimed | Executed | Result |
|---|---|---|---|
| `python3 setup.txt` | 16 OK | 16 OK / 0 FAIL / 0 MISSING | MATCH |
| `python3 build.py` | BUILD PASSED (200 checks) | BUILD PASSED, 200 PASS lines, 0 FAIL | MATCH |
| `pytest -q` | 117 tests | 117 passed | MATCH |
| `pytest xz_protocol_phase_a_tests.py -q` | 69 tests | 69 passed | MATCH |
| Total | 186 GREEN | 186 GREEN | MATCH |

Independently recomputed the trust-roots `manifest_digest` from its own stated construction (`sha256sum <12 normative code files, alphabetical> | sha256sum`): **a70cc7fd...460893 reproduces exactly.** Section 0.1's derived counts also hold on bytes: 27 adversarial tests, 14 kernel test functions, 16 source-frame records, 14 normative files (12 + 1 + 1).

**Task-register substitution (disclosed).** The dispatch mandates "Execute A-1 through A-7." No such register exists anywhere in the shipped packet. `A-4` appears exactly once, as an incidental back-reference inside the sealed v0.20 entry pointing to `PRODUCER_SELF_DISCIPLINE_v2_DELTA.md`, which does not ship. Rather than invent seven tasks and report against them, this seat executed **Section 22 items 1 through 7** -- the shipped, normative, in-packet audit obligations -- as the task register, plus the mutation battery the dispatch demands. See F-S02-51-07.

---

## 1. Mutation battery

MUTATION-LANDED is used strictly: a mutation *lands* when a semantic corruption survives to `BUILD PASSED: all checks GREEN` after the attacker resyncs `PACKET_SHA256SUMS`, which any packet-controlling party does by definition.

| ID | Mutation | Outcome |
|---|---|---|
| M1 | Duplicate `ENTRY_v0.49` seal line, canonical lowercase digest (exact R9 replay) | **CAUGHT** -- both new checks fired |
| M2b | Duplicate `ENTRY_v0.50` seal line, digest rendered uppercase, placed before the genuine line | **MUTATION-LANDED** |
| M3 | Restore the `*Provenance and review status.*` seal terminus | Build breaks (`ENTRY_v0.51`, `FULL_SECTION_27`) -- diagnostic, not an attack |
| M4 | In-place mutation of carried entry v0.30 with partial reseal | **CAUGHT** -- PRIOR_HISTORY derivation fired |
| M5b | In-place mutation of carried entry v0.30 with full internal reseal | **MUTATION-LANDED** |
| M6 | Second, false `FULL_SECTION_27` seal line (all-zero digest) | **MUTATION-LANDED** |
| M7 | Phantom uppercase seal for nonexistent `ENTRY_v0.52` | **MUTATION-LANDED** |
| M8 | Fabricated `[COMPUTED:]` evidence content sealed into the v0.51 entry | **MUTATION-LANDED** |

Five landed. Two controls confirm real coverage: the canonical R9 attack is genuinely closed (M1), and Section 22.2's partial-reseal detection claim genuinely holds (M4).

---

## 2. Findings

### CRITICAL

**F-S02-51-01** CRITICAL -- Sealed mutation-test evidence for the R9 repair is arithmetically impossible on v0.51 bytes

- **Locus:** `xz_protocol_v0_51.md` Section 27, v0.51 entry, third paragraph; register item (1).
- **Substance:** The entry states that on v0.51 bytes the duplicate-seal mutation produces `BUILD FAILED` with `"HISTORY seal line count (51) == entry count (50)"` and `"No duplicate ENTRY labels in HISTORY (51 lines, 50 unique)"`, tagged `[COMPUTED: mutation test executed on v0.51 build.py, both checks fired]`. Executed on shipped v0.51 bytes (M1), build.py emits `HISTORY seal line count (52) == entry count (51)` and `No duplicate ENTRY labels in HISTORY (52 lines, 51 unique)`. v0.51 carries 51 amendment entries and 51 seal lines; a duplicate yields 52 against 51. The quoted pair is the v0.50 arithmetic (50 entries, 51 lines after duplication). The evidence sealed to prove the repair was not produced on the bytes it claims.
- **Disposition:** HALT-and-escalate. Re-run the duplicate-seal mutation on v0.51 bytes, capture the actual two strings, and replace both quoted literals in the v0.51 entry and in register item (1). Because the v0.51 entry is current-version, this is a reseal, not an append-only violation. Do not carry the corrected strings forward without re-executing at the next version -- this defect is a straight copy-forward.
- **Cross-reference:** Section 22.3 Class A (sealed claim false on shipped bytes). F-S01-50-01, whose CLOSED disposition rests on this evidence. Enabling mechanism: F-S02-51-06.

**F-S02-51-02** CRITICAL -- The declared seal terminus does not exist in the document; both seal computations fall back silently

- **Locus:** `xz_protocol_v0_51.md`, end of Section 27 (`...e884e0f5ored by Bilal Syed Arfeen`); `build.py:67`; `build.py:366`.
- **Substance:** Standing boundary item six, declared in the v0.51 entry and in every entry from v0.44 onward, is `seal terminus at Provenance marker`. The string `*Provenance and review status.*` occurs **zero** times in the shipped document. The deletion took the surrounding sentence with it, splicing the 64-hex PRIOR_HISTORY value directly into a truncated word: `PRIOR_HISTORY c345bd90...e884e0f5ored by Bilal Syed Arfeen`. Both seal paths guard with `if prov > 0 else <whole section>`, so `find()` returning -1 is absorbed with no check. Consequence on bytes: 813 bytes of provenance, no-peer-review, and end-of-document prose are sealed inside `ENTRY_v0.51`, and `FULL_SECTION_27` now spans all 219,043 characters of Section 27. M3 confirms the omission is load-bearing -- restoring the marker breaks both seals, so the shipped chain values were derived from the corrupted text.
- **Disposition:** HALT-and-escalate. (1) Restore the marker and the elided sentence text at the splice point and reseal `ENTRY_v0.51`, `FULL_SECTION_27`, and `PRIOR_HISTORY`. (2) Replace the silent fallback at `build.py:67` and `build.py:366` with `check(prov > 0, "Provenance seal terminus present")` so absence is a build failure rather than a span change. (3) State in the v0.52 entry that the v0.51 chain values were computed over an unterminated span, so external holders of v0.51 bytes have a documented expectation.
- **Cross-reference:** Section 22.3 Class A. Standing boundary item six. Precedent for recording a chain fork rather than hiding it: v0.48 correction (bd).

**F-S02-51-03** CRITICAL -- "The R8 duplicate-seal defect class is structurally extinct" is false; three neighbouring shapes pass

- **Locus:** `build.py:360` and `build.py:363-365`; claim at `xz_protocol_v0_51.md` Section 27, v0.51 entry, third paragraph.
- **Substance:** Both repaired checks select seal lines with `l.startswith(c) for c in '0123456789abcdef'` and `'ENTRY_' in l`. The filter is case-sensitive and ENTRY-only, so the repair covers exactly one shape of the class: a lowercase-hex-leading duplicate of an existing ENTRY label. Three shapes survive. M2b: a duplicate `ENTRY_v0.50` line whose digest is rendered uppercase (its true digest begins `e`, so `E` escapes the filter) and placed *before* the genuine line so the PRIOR_HISTORY derivation dictionary still resolves to the genuine value -- `HISTORY.sha256` contains two `ENTRY_v0.50` lines and the gate reports `51 lines, 51 unique`, BUILD PASSED. M6: a second `FULL_SECTION_27` line carrying an all-zero digest is uncounted because non-ENTRY seal lines have no cardinality check, and line 368 tests existence (`any(l == expected)`) rather than uniqueness -- BUILD PASSED. M7: a phantom seal for a nonexistent `ENTRY_v0.52`, uppercase-rendered, evades both the cardinality filter and the surjectivity check at line 356, which uses the same lowercase filter -- BUILD PASSED. The extinction claim overstates a one-shape fix as a class closure.
- **Disposition:** HALT-and-escalate. (1) Case-fold the filter: `l[:1].lower() in '0123456789abcdef'`, at lines 356 and 360. (2) Extend cardinality to all seal lines, not only ENTRY lines: assert exactly one `FULL_SECTION_27` line and exactly one line per declared label. (3) Assert the label set of `HISTORY.sha256` equals the expected label set exactly, so unknown labels such as `ENTRY_v0.52` fail rather than being ignored. (4) Restate the claim as "the lowercase-duplicate shape is closed; the class is not," or re-verify extinction with the mutations above after the fix.
- **Cross-reference:** Section 22.3 Class A. F-S01-49-04 and F-S01-50-01 (the R8/R9 duplicate-seal lineage). M1 shows the canonical shape is genuinely closed.

### HIGH

**F-S02-51-04** HIGH -- Correction (bh)'s locus claim is byte-false at the line it names

- **Locus:** `xz_protocol_v0_51.md` Section 27, v0.51 entry, correction (bh); `build.py:356`.
- **Substance:** Correction (bh) is tagged `[COMPUTED: v0.50 build.py line 356 is a set comprehension; v0.51 build.py lines 356-365 are list operations]`. On shipped v0.51 bytes, line 356 is `seal_labels = {l.split()[1] for l in history_lines if ...}` -- still a set comprehension. Line 358 is a string `find`. Lines 357, 361 and 364 are `check` calls. Only 360 and 363 are list operations. A verifier following the correction to line 356 to confirm the repair finds the exact construct the correction says was replaced, and would reasonably conclude the repair did not land.
- **Disposition:** Amend correction (bh) to cite the actual repair locus, `build.py:360-365`, and drop the "356" claim or restate it as "the v0.50 cardinality set comprehension at line 356 is replaced by the list operations now at lines 360-365; the set comprehension surviving at line 356 in v0.51 is `seal_labels`, a different check."
- **Cross-reference:** Section 22.3 Class A. F-S02-51-01 (same paragraph, same class). F-S02-51-06 (why no gate caught it).

**F-S02-51-05** HIGH -- Section 25 FB-7b row, the designated single source of truth, omits R9

- **Locus:** `xz_protocol_v0_51.md` Section 25, FB-7b row, final sentence; Section 0.1, paragraph two.
- **Substance:** Section 0.1 states that "FB-7b status, rationale, and the full carrying-seat trajectory are recorded in the Section 25 FB-7b row (single source of truth; no duplicate rationale maintained here)." The row's trajectory ends at `R8 (v0.49): Kimi K3 S01 carrying seat HALTed binding`. R9 on v0.50 -- a binding carrying-seat HALT on a Class A finding, recorded in the v0.51 entry -- is absent. The freeze-blocker register therefore understates the carrying-seat HALT record by one round, and the surface Section 0.1 designates as complete is not.
- **Disposition:** Append to the FB-7b row: `R9 (v0.50): Kimi K3 S01 carrying seat HALTed binding (cardinality gate set semantics, Class A); Opus S02 advisory CONDITIONAL PASS.` Add a standing producer step that the FB-7b row is updated in the same edit as any entry recording a carrying-seat verdict.
- **Cross-reference:** Section 22.3 Class B (concealed defect the entry does not disclose). Absorption-induced regression of F-S02-49-02 and F-S04-49-03, whose v0.50 disposition was "Section 25 FB-7b row updated with R6-R8 carrying-seat trajectory, completing the single source of truth."

**F-S02-51-06** HIGH -- [9c] provenance-tag validation reaches none of the v0.51 entry's evidence tags

- **Locus:** `build.py:394` (`\[COMPUTED:\s*build\.py\s*\[([^\]]+)\]\s*([^\]]*)\]`); `xz_protocol_v0_51.md` Section 27, v0.51 entry.
- **Substance:** The [9c] gate validates `[COMPUTED:]` tags only in bracket form, `build.py [9b]`. All six `[COMPUTED:]` tags in the v0.51 entry use prose form -- `build.py lines 356-365`, `grep -c v0.51 across 13 files = 13`, `pytest`, `mutation test executed on v0.51 build.py` -- so the validator matches zero of six and passes vacuously. Nothing in the build inspects the *content* of any evidence claim. M8 confirms the consequence: replacing the sealed evidence string with `"HISTORY seal line count (999) == entry count (-7)"` and resealing yields BUILD PASSED across all 200 checks. This is the mechanism by which F-S02-51-01 and F-S02-51-04 shipped green.
- **Disposition:** Extend the [9c] regex to accept prose-form loci and assert, at minimum, that any `build.py line N` or `lines N-M` reference resolves to a line range that exists and that a stated construct token (`set comprehension`, `list`) matches the cited line. Where content cannot be gated, require the prose form to be tagged `[ASSERTED]` rather than `[COMPUTED]`, and add a build check that `[COMPUTED:]` tags not matched by [9c] are counted and reported rather than silently ignored.
- **Cross-reference:** Section 22.3 Class D. Standing boundaries `[9c] arity-one regex` and `[9e] silent vacuity`. F-ADJ19-02 (the original tag-validity finding).

### MEDIUM

**F-S02-51-07** MEDIUM -- Dispatch mandates a task register that does not ship

- **Locus:** `prompt.txt:12`; `xz_protocol_v0_51.md` Section 27, v0.20 entry (sole `A-4` reference).
- **Substance:** The dispatch instructs "Execute A-1 through A-7." No definition of A-1 through A-7 exists in any of the nine dispatched files. The only occurrence of any member is `A-4`, inside the sealed v0.20 entry, referring to `PRODUCER_SELF_DISCIPLINE_v2_DELTA.md`, which is not a packet member. A fresh seat cannot execute the register as named, and any seat that reports "A-1 through A-7 executed" is reporting against invented content.
- **Disposition:** Either ship the discipline document as a packet member and list it in `PACKET_SHA256SUMS`, or inline the seven task definitions in the dispatch prompt. Until then, dispatches should name Section 22 items 1-7 explicitly.
- **Cross-reference:** Section 22.3 Class E. F-DB19-01 and F-DB19-03, the prior findings against the discipline blocks themselves.

**F-S02-51-08** MEDIUM -- Section 22.2 declares nine in-place mutations and enumerates seven loci

- **Locus:** `xz_protocol_v0_51.md` Section 22.2, sentence beginning "This control covers the historically dominant failure mode".
- **Substance:** The sentence reads "nine recorded in-place mutations at v0.4, v0.9, v0.11, v0.16, v0.17, v0.41, and v0.47" -- seven versions for a count of nine. The count may be defensible if some versions carry multiple mutations, but nothing shipped establishes that, and the sentence is written as an enumeration. No build check parses this count. This is the same declared-versus-enumerated shape that produced a ten-seat convergent HALT at R6 (29 declared, 30 enumerated).
- **Disposition:** Either enumerate all nine loci explicitly, or restate as "nine recorded in-place mutations across seven versions (v0.4, v0.9, v0.11, v0.16, v0.17, v0.41, v0.47)" with the per-version multiplicity named.
- **Cross-reference:** Section 22.3 Class D. F-S02-51-10 (same ungated-cardinality shape).

**F-S02-51-09** MEDIUM -- The external anchor set narrows without disclosure while the count is held at one

- **Locus:** `xz_protocol_v0_51.md` Section 27, v0.51 entry, final paragraph.
- **Substance:** Entries v0.44 through v0.50 each record `EXTERNAL count: 1 [EXTERNAL: v0.40 dispatch manifests held by carrying seats and Zenodo deposits doi:10.5281/zenodo.21713180 and doi:10.5281/zenodo.21583202]`. The v0.51 entry records `EXTERNAL count: 1 [EXTERNAL: v0.40 dispatch manifests]`, dropping both deposit receipts, while the count is unchanged. Section 22.2 names external anchors as the only defense against self-consistent forgery, and M5b confirms that class is live at v0.51: an in-place rewrite of carried entry v0.30 with full internal reseal returns BUILD PASSED. A silent contraction of the only defense is material.
- **Disposition:** Restore the two DOI anchors to the v0.51 EXTERNAL tag, or record an append-only correction stating why they were withdrawn and what the EXTERNAL count of one now denotes.
- **Cross-reference:** Section 22.3 Class E. Section 22.2 anchor list (a), (b), (c). Standing boundary `self-consistent resealing blind spot`.

**F-S02-51-10** MEDIUM -- The disclosed-boundary count is tagged as enumerated but no shipped code enumerates it

- **Locus:** `xz_protocol_v0_51.md` Section 27, v0.51 entry, `[ENUMERATED: 31 items]`; `build.py` (absence).
- **Substance:** `grep -n "ENUMERATED\|standing boundar" build.py` returns nothing. No check parses the boundary list or compares its length to the declared count. The v0.49 and v0.50 entries strengthen the tag to `[ENUMERATED: 31 items parsed from this list]`, asserting a parse that no shipped code performs. Hand-count on v0.51 bytes returns 31, so the count is correct this round; the finding is the absent gate on a defect class that produced a ten-seat convergent HALT at R6.
- **Disposition:** Add a build check that splits the boundary list on top-level commas, counts the items, and compares against the declared cardinality, failing on mismatch. Until it exists, downgrade the tag from `[ENUMERATED: ... parsed from this list]` to `[ASSERTED]`.
- **Cross-reference:** Section 22.3 Class D. R6 v0.47 boundary-count finding (29 declared, 30 enumerated). F-S02-51-08.

### LOW

**F-S02-51-11** LOW -- setup.txt carries three stale or wrong counts

- **Locus:** `setup.txt:177` ("199 checks"); `setup.txt:4` ("17-member packet", "10-file .txt dispatch format"); docstring lines 11-12.
- **Substance:** The next-steps block advertises `build.py # run build verification (199 checks)`; the shipped build emits 200 PASS lines and the dispatch prompt says 200. The docstring says "17-member packet" where the manifest carries 16 members and the script itself prints "all 16 files match," and "10-file .txt dispatch format" where nine .txt files ship. Note the docstring's "6 individual .py files" per bundle is correct and verified.
- **Disposition:** Change 199 to 200; change "17-member" to "16-member"; change "10-file" to "9-file". Add these three strings to the version-stamp sweep so they move with the build.
- **Cross-reference:** F-S01-50-03 and F-S01-50-04, the prior setup.txt count corrections, closed at v0.51 for the "15" to "16" strings but not for these.

**F-S02-51-12** LOW -- Hand-patch residue at the repair site

- **Locus:** `build.py:359`.
- **Substance:** The comment `# HISTORY cardinality check (v0.51): count seal LINES, not set members` is indented at four spaces inside an eight-space block. It is syntactically inert, but it sits at the exact line range the round's central repair is verified from and is direct evidence the repair was patched in by hand rather than edited in context -- consistent with F-S02-51-01 and F-S02-51-04.
- **Disposition:** Re-indent to eight spaces.
- **Cross-reference:** F-S02-51-04 (adjacent locus claim, byte-false).

---

## 3. Section 22 item-by-item disposition

| Item | Obligation | Disposition |
|---|---|---|
| 1 | Producer self-check via prohibited-content verifier | NOT EXECUTABLE -- verifier does not ship (conditional form "when shipped" is honest) |
| 2 | Schema validation and manifest verification | PASS -- 16/16 manifest, trust-roots digest independently reproduced |
| 3 | Exhaustive 3^5 = 243 kernel decision-state tests | PASS -- 14 test functions, 243 vectors, GREEN |
| 4 | XZ-specific adversarial suite, nine categories | PASS on execution -- 27 tests GREEN; coverage limit at four of six modules remains disclosed (F-V44-01) |
| 5 | Independent rerun of universe enumeration | NOT APPLICABLE -- no corpus exists at this draft |
| 6 | Two-family executing carry | NOT SATISFIED -- this seat is producer-family and advisory by construction |
| 7 | HALT from either carrying seat blocks freeze | ADVISORY HALT recorded. The v0.37 persistent-architectural-HALT exception does not reach this report: by its own terms it excludes Class A and Class B findings as classified by the HALTing seat, and this report classifies four Class A and one Class B |

---

## 4. What held

Recorded so the HALT is not read as a global negative:

- Reconstruction, build, and all 186 tests reproduce exactly as the dispatch claims.
- The trust-roots `manifest_digest` verifies independently from its own published construction -- a genuine externally checkable surface.
- M1: the canonical R9 duplicate-seal attack is genuinely closed. The repair works for the shape it was written against.
- M4: Section 22.2's claim that the [9b] PRIOR_HISTORY derivation detects a partially resealed in-place mutation of a carried entry is true on bytes. Partial forgery is caught.
- Section 0.1's derived counts (27 adversarial tests, 14 kernel functions, 16 sources, 14 normative files) all hold.
- The disclosed-boundary count of 31 is correct on bytes this round.

---

## 5. Cross-vendor recommendation

This seat is Claude Opus 5 and the producer family is Claude (Section 22.1); this report is advisory and carries no vote toward FB-7b. The three CRITICAL findings are byte-checkable in under a minute each and should be dispositioned before any further carrying dispatch, so that non-producer seats spend their round on the protocol rather than on re-deriving F-S02-51-01.

For R11, dispatch to a non-producer family (Kimi K3 or GLM-5.2) with three concrete asks: re-execute the duplicate-seal mutation on the repaired bytes and compare the emitted strings against the entry; grep for `*Provenance and review status.*` before trusting any seal value; and run the case-fold and non-ENTRY-label mutations above against the corrected filter.

---

*Seat S02-OPUS, advisory, non-carrying. Executed on the canonical v0.51 packet, sixteen members, `PACKET_SHA256SUMS` digest f3151b985d8fee20562460d248fb87b320b21539fba25d724626afac20015c6b. Mutation builds constructed from the reconstructed tree; no shipped byte was modified in place. This report is a consistency check by an AI system, not peer review.*

---

# Bismillah ir-Rahman ir-Rahim
