# Bismillah ir-Rahman ir-Rahim

# R0786 -- R14 Seat S04 -- Advisory Audit Report

**Chronological Index:** 491 of 995  
**Date:** 2026-08-10  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** R14_S04_OPUS5_REVELATION_REPORT.md  
**Source Format:** md  
**SHA-256:** `7c877026e46a5bb28db345f1f952cee276dc177a4242ea52b9f5494ca8d57a27`  

---

## R0786 · R14 Seat S04 -- Advisory Audit Report

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: R14_S04_OPUS5_REVELATION_REPORT.md
- source_format: md
- text_sha256: 7c877026e46a5bb28db345f1f952cee276dc177a4242ea52b9f5494ca8d57a27

# R14 Seat S04 -- Advisory Audit Report

**Seat:** S04-OPUS5-REVELATION | Opus 5 | fresh | advisory, non-binding
**Lens:** Structural Revelation (n=2, l=1, ml=2, ms=-1/2)
**Artifact:** XZ Protocol v0.55 DRAFT CANDIDATE
**Date:** 2026-08-10
**Namespace:** F-S04-55-NN

---

## Verdict

**HALT (advisory).**

Severity ledger: **0 CRITICAL / 5 HIGH / 3 MEDIUM / 5 LOW** (13 findings).

Recommendation: absorb into v0.56 by append-only correction; do not edit the sealed v0.55 entry. Two of the HIGH findings (F-S04-55-01, F-S04-55-02) concern gate coverage claimed but not delivered, and should be dispositioned before any carrying seat is asked to treat the R13 defect classes as closed.

---

## Mode and scope

Auditor operated in **Mode A (partial)** with direct byte access to `PROTOCOL.txt` and `BUILD_GATES.txt`, and executed mutation probes on copies. The 12 code modules, trust roots, and `HISTORY.sha256` proper do not ship in this packet, so gates [1], [2] (code stamps), and [3] (digests) were not executable. Substrate-claim verification confidence: **high** for the protocol text and `build.py`; **reduced** for claims about code-file contents (`grep -c v0.55 across 13 files = 13`, `186 tests GREEN`).

**Manifest challenge (confirmed independently):**

| File | sha256 | Status |
|---|---|---|
| PROTOCOL.txt | `74dc8101bdb6071f8264db299df236b34cf4e52f43b2b8924375b51f7e844c39` | MATCH |
| BUILD_GATES.txt | `afc03768bdb060296035cdaef6da9d5ec4789a5072eeac3ab2725e7acf1d6aeb` | MATCH |

**Producer-instance check:** Opus 5 is producer-family (Section 22.1). Seat is advisory and non-binding, which is the correct posture; this report does not count toward FB-8.

---

## Part I findings

Ordered by severity, then locus.

### F-S04-55-01 HIGH -- standing boundary retired while the limitation it names is still true on shipped bytes

- **Locus:** `PROTOCOL.txt`:1280 register item (3) ("standing boundary item 29 retired"); :1282 correction (bp); :1286 boundary list (33 items; `[3a] fb_spec omits FB-7b locus assertion` absent). `BUILD_GATES.txt`:316-338 (`fb_spec`).
- **Substance:** The entry claims boundary item 29 is retired "via [2g]". On shipped `build.py` bytes, `[3a]`'s `fb_spec` dict carries keys FB-3, FB-4, FB-5, FB-6, FB-7a and still omits FB-7b; no FB-7b row-existence check exists (contrast the FB-8 existence gate at :331). `[2g]` compares a version token across the whole body, which is not a locus assertion. **Probe D:** deleting the entire `| FB-7b |` row from Section 25 and planting `PENDING RE-CARRY v0.55` in Section 0.1 leaves `[2g]` at PASS -- while Section 0.1 continues to name the deleted row as FB-7b's "single source of truth". The disclosure was withdrawn; the gap was not closed. Disclosed surface shrank by one item without a corresponding closure.
- **Disposition:** Choose one and record it. (i) Restore `[3a] fb_spec omits FB-7b locus assertion (F-S07-46-03)` to the boundary list at v0.56, raise the declared count and `[ENUMERATED:` tag to 34, and record an append-only correction retracting the v0.55 retirement claim. (ii) Add an `FB-7b` key to `fb_spec` asserting the Section 25 row's presence, re-scope `[2g]` to `s25_region`, and keep the retirement with a probe receipt attached. Do not leave both the retirement and the uncovered gap standing.
- **Cross-reference:** correction (bp); boundary item 20 ("no boundary-retirement mechanism"); Section 22.3 Class A; AX-SH Axiom 2; F-S04-55-06, F-S04-55-11.

### F-S04-55-02 HIGH -- gate [2f] does not close the defect class register item (2) states it closes

- **Locus:** `PROTOCOL.txt`:1280 register item (2). `BUILD_GATES.txt`:208-234.
- **Substance:** R13 finding 2 was a provenance clause carried verbatim from a prior version (`repair build from v0.52 R11 audit` still standing at v0.54). `[2f]` asserts the status self-reference equals VERSION and that `prov_ver < VERSION`; it never checks that `prov_ver == VERSION - 1`, and it never inspects the round number at all. **Probe A:** reinstating the exact R13 defect string on v0.55 bytes yields PASS on both `[2f]` checks (`prov v0.52 (R11) < v0.55`). The entry disposes the finding "HIGH CLOSED via body repair and new gate"; the body repair landed, but the gate does not prevent recurrence of the class it was built for. No standing boundary discloses this limitation on shipped bytes -- the dispatch's own `AUDIT_CONTEXT.txt` §3 notes it, but that document does not ship.
- **Disposition:** Either tighten `[2f]` to require `prov_ver == VERSION - 1` and cross-check the round number against a declared round register, or amend item (2)'s disposition at v0.56 to "CLOSED via body repair; gate coverage partial" and add a standing boundary reading `[2f] provenance clause not pinned to VERSION-1; round number unchecked` (declared count and `[ENUMERATED:` tag incremented accordingly).
- **Cross-reference:** R13 finding 2 (F-S01-54-02 class); Predictive Audit Paper R1 (failure-mode shift); F-S04-55-08.

### F-S04-55-03 HIGH -- register item (3) convergence count unsupported by its own citation list and understated against the R13 record

- **Locus:** `PROTOCOL.txt`:1278 ("Third finding (3/5 seats)"); :1280 register item (3).
- **Substance:** Item (3) cites exactly two finding IDs (F-S01-54-03, F-S03-54-03) and claims "3-seat convergence". On shipped bytes alone the claim is unsupported: 3 asserted against 2 enumerated. Against the R13 record supplied with this dispatch, the FB-7b row finding was returned by four seats (F-S01-54-03, F-S02-54-02, F-S03-54-03, F-S05-54-02), so both the narrative "3/5 seats" and the register's "3-seat convergence" understate it. `[9f]` parses item count and severity only; it passed cleanly (6 declared, 6 parsed), so this is fully ungated. This is a wrong count inside a sealed claim -- Class A by Section 22.3.
- **Disposition:** At v0.56, correct item (3) to cite all four IDs and read "4-seat convergence", correct the narrative to "Third finding (4/5 seats)", and record both by append-only correction rather than editing the sealed v0.55 entry. Extend `[9f]` with an assertion that each item's `<N>-seat convergence` equals the count of distinct seat prefixes among its cited finding IDs.
- **Cross-reference:** F-S04-55-04; correction (as) at v0.44 (finding-ID transposition precedent); PMD v1.8 M1.6 (codification-cycle self-error).

### F-S04-55-04 HIGH -- register item (2) transposes S05's finding ID

- **Locus:** `PROTOCOL.txt`:1280 register item (2).
- **Substance:** Item (2), disposing the status-provenance defect, cites `F-S05-54-02`. The R13 record supplied with this dispatch assigns `F-S05-54-02` to the FB-7b row finding and `F-S05-54-03` to the status finding. The cited ID therefore belongs to the class dispositioned in item (3): item (2)'s five-ID list is arithmetically correct and semantically wrong, and item (3) is short by exactly that ID. Not verifiable from the shipped protocol alone, since the R13 seat reports do not ship -- verified against the dispatch's own R13 finding-ID table.
- **Disposition:** At v0.56, correct item (2) to `F-S05-54-03` and move `F-S05-54-02` into item (3) alongside `F-S02-54-02`, by append-only correction. If the dispatch table rather than the entry is wrong, correct the dispatch and record which surface was in error -- do not reconcile silently.
- **Cross-reference:** F-S04-55-03; correction (as) at v0.44; `AUDIT_CONTEXT.txt` R13 findings 2 and 3.

### F-S04-55-05 HIGH -- register header item count unsupported by the register it introduces

- **Locus:** `PROTOCOL.txt`:1280 ("v0.55 defect register disposition (from R13 five-seat audit, 5 Class A items + additional findings)").
- **Substance:** The register carries six numbered items at 3 HIGH / 1 MEDIUM / 2 LOW. Under the convention used at v0.43, v0.45, v0.46 and v0.54, the numeral preceding "items" is the register item count, which is 6. Under a severity reading, Class A is HALT-grade (Section 22.3) and maps to the three HIGH items. Neither reading yields 5. The claim is additionally unverifiable on its own terms, because register item (5) discloses that no class-to-severity mapping exists on shipped bytes -- so "Class A items" has no byte-resolvable referent.
- **Disposition:** At v0.56, restate as "6 items" or "6 items (3 Class A)", by append-only correction. Extend `[9f]` to assert that any numeral appearing in the register header matches the parsed item count.
- **Cross-reference:** F-S04-55-07; v0.54 register header ("5 items", accurate on its own register); Section 22.3.

### F-S04-55-06 MEDIUM -- gate [2g] structurally forbids FB-7b resolution

- **Locus:** `BUILD_GATES.txt`:236-254.
- **Substance:** The outer guard searches the entire protocol for `PENDING RE-CARRY v<X>`. Section 27 permanently contains that token -- correction (bp) at `PROTOCOL.txt`:1282 quotes `"PENDING RE-CARRY v0.53"` -- so the guard always matches and the `else` branch printing "may be RESOLVED" is unreachable dead code. **Probe 1:** rewriting the Section 25 row to `RESOLVED v0.55` yields `FAIL: PENDING RE-CARRY found in body`. The build therefore fails on the legitimate terminal state the register is working toward, and the failure will present as a gate error rather than as the milestone it is.
- **Disposition:** Scope the outer guard to `body` (or to `s25_region`) instead of `protocol`, so that absence of a body token reaches the RESOLVED branch. Alternatively, require the FB-7b row to match `(PENDING RE-CARRY v{VERSION}|RESOLVED v{VERSION})` and check that disjunction directly.
- **Cross-reference:** F-S04-55-01, F-S04-55-09; `AUDIT_CONTEXT.txt` §3 `[2g]` edge note.

### F-S04-55-07 MEDIUM -- register item (5) and boundary item 29 assert the absence of a mapping they themselves ship

- **Locus:** `PROTOCOL.txt`:1280 register item (5); :1286 boundary item 29.
- **Substance:** Item (5) states that the class-to-severity mapping `(A=CRITICAL/HIGH, B=MEDIUM, C=LOW, D=LOW, E=INFORMATIONAL)` is "not defined on shipped bytes", and boundary item 29 repeats "class-to-severity mapping undefined on shipped bytes". The parenthetical is a complete mapping, and it ships inside a sealed entry. Read strictly, the claim is falsified by the sentence making it. Read charitably, it means "not defined normatively in Section 22.3" -- which the text does not say. This is the R5 self-similarity signature: the correction carries the class of error it describes. It is also a REV-4 uniqueness break, since the same fact now sits at two loci with no canonical position.
- **Disposition:** Either promote the mapping into Section 22.3 as normative rows and reword boundary item 29 to "class-to-severity mapping not asserted by any gate", or delete the parenthetical from item (5) so the mapping is genuinely undefined. Record by append-only correction at v0.56.
- **Cross-reference:** F-S04-55-05; Section 22.3; substrate-of-record uniqueness.

### F-S04-55-08 MEDIUM -- gate [2h] is silently vacuous and comma-only

- **Locus:** `BUILD_GATES.txt`:255-292.
- **Substance:** When the declaration regex does not match, `[2h]` prints INFO and passes. **Probe 2:** deleting the whole `Disclosed standing boundaries -- 33 items: ... [ENUMERATED: 33 items]` span silences the gate entirely -- the count gate is evaded by removing the count. **Probe 4:** an additional item joined with a semicolon rather than a comma yields `declared 33 == tag 33 == actual 33` PASS while the list carries 34. **Probe 3** confirms the comma path works correctly (34th comma-separated item caught). The entry's description of `[2h]` matches the code, so this is coverage rather than a seam break -- but the vacuity path is undisclosed, whereas the structurally identical `[9e]` vacuity is boundary item 23.
- **Disposition:** Replace the INFO branch with `check(False, ...)`, and tokenize on `[,;]` at depth zero. If the code change is deferred, add a standing boundary reading `[2h] silently vacuous on missing declaration; comma-only tokenization` at v0.56 and increment the declared count and `[ENUMERATED:` tag.
- **Cross-reference:** boundary item 23 (`[9e]` silent vacuity); F-S01-54-05 / F-S04-54-03; F-S04-55-02.

### F-S04-55-09 LOW -- [2g] comment claims a scope the code does not implement

- **Locus:** `BUILD_GATES.txt`:242 ("The FB-7b row is in Section 25 (body), so check the body occurrence").
- **Substance:** The comment names Section 25; the code searches the whole body, Sections 0 through 26. Probe D shows the operational consequence: the row can be deleted and the token relocated. A REV-3 seam gap at the comment level, even though the entry's prose description of `[2g]` is accurate.
- **Disposition:** Search `s25_region` (already computed at `[3a]`) and update the comment, or reword the comment to "body-scoped" so code and description agree.
- **Cross-reference:** F-S04-55-01, F-S04-55-06.

### F-S04-55-10 LOW -- defect-class label conflation in the v0.55 narrative

- **Locus:** `PROTOCOL.txt`:1278.
- **Substance:** The narrative states that all three R13 defects "are the version-token staleness class previously seen at F-S01-47-02 (R6 boundary count) and F-S01-53-01 (R12 boundary count)". Both cited precedents are count-staleness findings -- a declared count diverging from an enumerated list -- not version-token staleness. The same paragraph then states that the R13 class "is distinct". Correction (bn) at :1282 gives the coherent framing ("a version-advancing manual-update step omitted during the build ... at a novel locus"); the narrative does not inherit it.
- **Disposition:** Reword the narrative to name the shared genus (version-advancing manual-update omission) and keep the two species distinct (count staleness; version-token staleness). Editorial, no seal impact on prior entries.
- **Cross-reference:** correction (bn); correction (bm); F-S04-55-05.

### F-S04-55-11 LOW -- boundary item 20 inconsistent with v0.55 practice

- **Locus:** `PROTOCOL.txt`:1286 boundary item 20 ("no boundary-retirement mechanism").
- **Substance:** v0.55 retires a boundary item (register item (3), correction (bp)) while the boundary list continues to disclose that no retirement mechanism exists. Either the retirement was performed without a mechanism -- in which case F-S04-55-01 applies and the retirement is unaudited -- or a mechanism now exists and item 20 is stale. The list cannot consistently hold both.
- **Disposition:** State the retirement rule explicitly (retirement requires a gate asserting the negation of the retired limitation, plus a mutation-probe receipt in the entry), then either retire item 20 under that rule or keep it and record future retirements as suspensions.
- **Cross-reference:** F-S04-55-01; Predictive Audit Paper R8 (boundary accumulation).

### F-S04-55-12 LOW -- Sections 22.2 and 22.3 in inverted document order

- **Locus:** `PROTOCOL.txt`:714 (22.3) preceding :718 (22.2).
- **Substance:** Section 22.3 ("Condition severity classification", added v0.33) appears before Section 22.2 ("Self-consistent-forgery boundary", added v0.20). Both are cited by number elsewhere, including in body repair [e] of the v0.55 entry. No gate asserts sub-section ordering, so a reader resolving "Section 22.2" by document position lands on 22.3.
- **Disposition:** Reorder to 22.1, 22.2, 22.3 at v0.56 as an editorial body repair with a `[DIFF-VERIFIED]` tag; no seal impact, since the body carries no HISTORY seal (see F-S04-55-13).
- **Cross-reference:** F-S04-55-13; body repair [e].

### F-S04-55-13 LOW -- the protocol body carries no append-only seal, and every R13 Class A lived there

- **Locus:** `SEAL_HISTORY.txt` (55 ENTRY seals, FULL_SECTION_27, PRIOR_HISTORY); `PROTOCOL.txt`:1-808 and :1288-1290.
- **Substance:** The three seals cover Section 27 up to the Provenance marker only. Sections 0 through 26 and the two lines after the Provenance marker fall outside all three. All three R13 Class A defects -- title, front-matter Status, FB-7b row -- sat in that unsealed band, and the v0.55 remedy is four prose gates rather than a seal. The boundary list names "Section 27 ungated share" (item 3) and "seal terminus at Provenance marker" (item 6), but no item names body unsealedness, so the largest unsealed surface in the artifact is the one the list does not describe.
- **Disposition:** Add a `BODY_SECTIONS_0_26` line to `HISTORY.sha256` with a corresponding `[9b]` check at v0.56, or add a standing boundary reading `protocol body outside all HISTORY seals` and increment the declared count and `[ENUMERATED:` tag.
- **Cross-reference:** Section 22.2 self-consistent-forgery boundary; boundary items 3 and 6; REV-5.

---

## Part II -- Structural Revelation lens results

### REV-1 Ring composition -- CLOSES, with one break

Verified against shipped bytes:

| Ring pair | Section 0 claim | Section 25 / 27 confirmation | Result |
|---|---|---|---|
| Entry count | "fifty-five amendment entries, v0.1 through v0.55" | 55 entries parsed, contiguous v0.1-v0.55, ascending, no duplicates | CLOSES |
| FB-7b status | "PENDING RE-CARRY on v0.55 bytes" | Section 25 row: "RESOLVED v0.31; PENDING RE-CARRY v0.55" | CLOSES |
| FB-8 status | "OPEN" | Section 25 row: "OPEN"; front matter: "FB-8 OPEN" | CLOSES |
| Status provenance | "repair build from v0.54 R13 audit" | v0.55 entry: R13 on v0.54, 2 carrying / 3 advisory HALT | CLOSES |
| Title / Version / self-ref | `# XZ Protocol v0.55`, `Version: 0.55`, "This document is v0.55" | consistent | CLOSES |

All three R13 ring breaks are repaired. The FB-7b triplication is genuinely resolved rather than papered over: Section 0.1 now delegates rationale to the Section 25 row and names it the single source of truth, and no duplicate rationale remains in Section 0.1.

The surviving break is not one of the three R13 breaks but a new one: the ring runs Section 0 -> body -> Section 25 -> Section 27, and the register at the far end of Section 27 (F-S04-55-03, F-S04-55-04, F-S04-55-05) no longer confirms the R13 record it claims to be closing. The chiasm's outer arms agree; its inner arm does not.

### REV-2 Entry structural integrity -- narrative and register diverge

Read as a self-contained document, the v0.55 entry is internally coherent on every byte-level surface and incoherent on every cross-reference surface.

Body repairs [a] through [h], all verified landed at their claimed loci:

| Repair | Claim | Shipped bytes | Result |
|---|---|---|---|
| [a] | Title to v0.55 | line 1 reads `# XZ Protocol v0.55` | LANDED |
| [b] | Version to 0.55 | `**Version:** 0.55, draft candidate, 2026-08-10` | LANDED |
| [c] | Status with v0.55/R13 provenance | present | LANDED |
| [d] | "fifty-five amendment entries, v0.1 through v0.55" | present; count verified 55 | LANDED |
| [e] | Section 22.2 to "v0.1 through v0.54" | present | LANDED |
| [f] | Section 22.3 lineage to v0.38-v0.55 | present | LANDED |
| [g] | FB-7b row to "PENDING RE-CARRY v0.55" plus R12/R13 trajectory | present | LANDED |
| [h] | Section 0.1 to "PENDING RE-CARRY on v0.55 bytes" | present | LANDED |

Register cross-reference audit:

| Item | IDs cited | Convergence claimed | Result |
|---|---|---|---|
| (1) title | 5 | 5-seat | consistent |
| (2) status | 5 | 5-seat | count consistent, one ID transposed (F-S04-55-04) |
| (3) FB-7b | 2 | 3-seat | inconsistent (F-S04-55-03) |
| (4) boundary count | 2 | 2-seat | consistent |
| (5) class-to-severity | 2 | none claimed | self-falsifying claim (F-S04-55-07) |
| (6) no-op diff | 1 | none claimed | consistent |

Tag census for the entry: 2 `[EXTERNAL:` (matches the declared EXTERNAL count of 2), 10 `[COMPUTED:`, 5 `[ASSERTED]`, 9 `[DIFF-VERIFIED]` (8 claims plus one quoted instance in item (6), the known `[9c]` quoted-tag inflation class), 1 `[ENUMERATED:`. Correction letters run `(ba)` through `(bp)` with no gap.

Boundary arithmetic verified: 32 at v0.54, minus 1 retired, plus 2 added, equals 33 declared, 33 in the `[ENUMERATED:` tag, and 33 under independent paren-aware tokenization.

### REV-3 Gate seams -- descriptions accurate, coverage overclaimed

Each of the four new gates' prose description matches its code logic exactly. The seam between prose and code is clean. The seam between the gate and the *defect class the entry says it closes* is not:

| Gate | Entry's description | Code | Seam | Coverage |
|---|---|---|---|---|
| [2e] | title version == VERSION | reads line 1, compares to VERSION | matches | adequate; Probe B fires correctly |
| [2f] | self-ref == VERSION, provenance < VERSION | exactly that | matches | **inadequate** -- Probe A reinstates the R13 defect and passes (F-S04-55-02) |
| [2g] | PENDING RE-CARRY version == VERSION in body | exactly that | matches | **misdirected** -- body-wide, not row-anchored; blocks resolution (F-S04-55-06, F-S04-55-09) |
| [2h] | declared == tag == actual, paren-aware | exactly that | matches | **partial** -- vacuous on absence, comma-only (F-S04-55-08) |

The pattern worth naming: the entry describes what each gate *does* with precision, and describes what each gate *achieves* with optimism. `[2f]` is the sharpest instance -- the description is exact, and the exact description is the proof that the gate cannot catch the defect that motivated it.

### REV-4 Substrate-of-record uniqueness -- one break

The R13 triplication (FB-7b at three loci with two values) is resolved. Every v0.55 version token agrees across the title, front matter, Section 0.1, Section 22.3, the Section 25 row, and the entry. The boundary count appears at exactly one locus.

The break is the class-to-severity mapping (F-S04-55-07): the same fact -- that no such mapping exists -- is stated at two loci, and one of those loci contains the mapping.

### REV-5 Seal-chain integrity -- triad intact

Independently recomputed from shipped bytes:

- **ENTRY seals:** 55 of 55 match. No in-place mutation of any carried entry v0.1 through v0.54.
- **FULL_SECTION_27:** computed `41a314e75d7b696bae0da0ae3d208a055e0e58d920777627f7b9c58a1550b723`, matches the shipped line.
- **PRIOR_HISTORY:** the recursive derivation reproduces `123550f514f0ee05c9eded3b430f008c411578c4c79c60d60e60a7f27afe98bc` exactly, matching the shipped value.

Append-only integrity is the strongest surface in this build. The text that falls outside all three seals is the entire protocol body (Sections 0-26), the Provenance paragraph, and the closing line -- see F-S04-55-13.

---

## Standing-rules sweep

| Rule | Result |
|---|---|
| Em-dash policy | CLEAN -- no U+2013/2014/2015 in either file |
| Brand canonical | CLEAN -- no spaced variant; the two `BayyinahEnterprise` occurrences sit in Section 27, outside the gate's body scope |
| Severity uppercase | CLEAN |
| Six-element findings format (register items) | items carry ID, severity, locus, substance, disposition; cross-references are the failing element (F-S04-55-03, F-S04-55-04) |
| Substrate-of-record uniqueness | one break (F-S04-55-07) |
| Audit-chain immutability | CLEAN -- seals verified, corrections append-only, no historical entry edited |

---

## Program-level reading

**Prediction 1 (register cross-references) -- CONFIRMED.** Three of the five HIGH findings live exactly where the predictive analysis said they would: the register's finding-ID lists and convergence counts, ungated by `[9f]`, written from memory of reports that do not ship. The M1.6 signature is intact -- byte-level repairs all landed, and the narration of those repairs is where the errors are.

**Prediction 2 (new gate edge cases) -- CONFIRMED.** All four predicted edge cases were probed; three fired. `[2f]`'s missing `VERSION - 1` pin, `[2g]`'s behavior on FB-7b resolution, and `[2h]`'s non-comma tokenization are all live.

**R1 (failure-mode shift) -- CONFIRMED, with a novel class.** With the three historical classes mechanically gated, the defect migrated to two cells not previously occupied: gate-coverage overclaim (F-S04-55-02) and boundary retirement without closure (F-S04-55-01). The second is worth naming as its own class -- it is the first defect in this lineage that *reduces* disclosed surface rather than misstating it, and the boundary list's own item 20 predicted it.

**R2 (ungated band concentration) -- CONFIRMED.** All five HIGH findings are in the ungated prose interior: four in the Section 27 register, one in the boundary list. Nothing surfaced in the gated layer.

**R5 (self-similarity) -- CONFIRMED at Level 0.** Register item (5) asserts the absence of a mapping while shipping the mapping. The generator sits above the correction level.

**R11 (producer attention gradient) -- CONFIRMED.** Reading bottom-up was the right instruction. The register's later items and the boundary list carry the defects; the earlier narrative and the body repairs are clean.

**Hurst.** A Class A is present at R14, so the R7-R14 binary series remains persistent and H does not drop. The four v0.55 gates were a Level 3 intervention and behaved as the Fractal Cube model predicted: they closed their target cells and the generator found adjacent ones. The next intervention that could move H is at Level 0 -- specifically, requiring that every register cross-reference be transcribed from the shipped seat report rather than narrated, and that no boundary be retired without a probe receipt in the entry.

**FB-8.** Unaffected by this seat, which is producer-family and advisory. FB-8 remains OPEN.

---

## Cross-vendor recommendation

This seat is producer-family (Opus 5, Claude). Per Section 22.1 and PMD v1.8 cross-vendor rotation, R14's binding disposition must come from the carrying seats. F-S04-55-04 in particular cannot be settled from shipped bytes -- it requires a seat holding the R13 S05 report, or the report itself entering the packet. Recommend that v0.56's dispatch ship the R13 finding-ID table inside the sealed packet so that register cross-references become byte-verifiable rather than externally anchored; that single change would move the entire Prediction 1 attack surface from ungated to gated.

---

*Seat S04, R14, advisory and non-binding. Findings are stated plainly, including where they contradict the entry's own closure claims. Where I could not verify from shipped bytes, I have said so rather than smoothing the boundary.*

---

# Bismillah ir-Rahman ir-Rahim
