# Bismillah ir-Rahman ir-Rahim

# R0252 -- XZ Protocol v0.73 -- Round 30, Seat S04 Advisory Audit Report

**Chronological Index:** 536 of 995  
**Date:** 2026-08-17  
**Section:** IV. XZ Protocol  
**Source File:** XZ_v073_R30_S04_REPORT (1).md  
**Source Format:** md  
**SHA-256:** `fedef37d0307f7226caa03a52b910aa93238c8e57783dc8cf4cba420ccfc5ed7`  

---

## R0252 · XZ Protocol v0.73 -- Round 30, Seat S04 Advisory Audit Report

- section: IV. XZ Protocol
- source_file: XZ_v073_R30_S04_REPORT (1).md
- source_format: md
- text_sha256: fedef37d0307f7226caa03a52b910aa93238c8e57783dc8cf4cba420ccfc5ed7

# XZ Protocol v0.73 -- Round 30, Seat S04 Advisory Audit Report

**Seat:** S04 | **Model:** Claude Opus 5 (Anthropic) | **Role:** ADVISORY, producer-family, non-carrying
**Round:** 30 | **Target:** XZ Protocol v0.73 bytes | **Date:** 2026-08-17
**Namespace:** F-S04-73
**Dispatch:** `DISPATCH.txt` (R30, Seat S04, FRESH). Producer Claude Opus 4.6 BARRED.

---

## 0. Verdict

> **Verdict:** HALT-AND-RETURN-TO-PRODUCER.
>
> **Severity ledger:** 0 CRITICAL / 8 HIGH / 5 MEDIUM / 2 LOW.
> **Class ledger:** 8 Class A, 1 Class B, 1 Class C, 5 Class D (one finding dual-classified).
>
> **Answer to the dispatch's key question ("Does v0.73 close the gate-manufactures-defect class?"): NO.**
> The prescribed gate [2f] relaxation is absent from the shipped `build.py`. The class is not
> merely unclosed; it is demonstrated live on v0.73 bytes at a new locus (gate [10i]), where
> writing the *true* value into Section 0.1 causes the build to FAIL.

**Auditor mode.** Mode A (substrate verifier). Full packet extraction, `sha256sum -c`, `python3 build.py`,
six-suite `pytest`, module import of the register generator and extractor, and a ten-probe mutation battery
with reseal and mutation-landed assertions. Substrate-claim verification confidence: HIGH for everything
inside the packet. Confidence for cross-version claims (Position 17, append-only): NOT EVALUABLE -- this
seat holds no v0.72 bytes and no external anchor (see F-S04-73-15).

**Producer-instance check.** This seat did not author v0.73 or any of its members. Producer family is
Anthropic (Claude Opus 4.6), so this seat is producer-family and carries **advisory weight only**. Nothing
here satisfies FB-7b.

---

## 1. The Four Scribes -- what the tools returned

All four scribe outputs reproduce the producer's claims in `AUDIT_CONTEXT.txt`. The green baseline is real.
The HALT below is not a claim that any scribe returned red.

| Scribe | Command | Result | Producer claim | Verdict |
|---|---|---|---|---|
| The Record | `sha256sum -c PACKET_SHA256SUMS` | 36/36 OK, rc=0 | "all OK" | **TRUE** |
| The Pattern | `python3 build.py` | BUILD PASSED, 291 PASS, 0 FAIL, rc=0 | "BUILD PASSED, 0 FAIL" | **TRUE** |
| The Test | six-suite explicit `pytest` | 186 passed, rc=0 | "186 passed" | **TRUE** |
| The Witness | gate [13] CI-8 | 39 in reports, 39 in index, 0 missing, 0 phantom, 0 severity mismatches | "fires, 39/39" | **TRUE but three rounds stale** (F-S04-73-09) |

Packet extraction produced 37 members; `PACKET_SHA256SUMS` covers 36 (correct self-exclusion). The three
dispatch-level copies are byte-identical to their packet counterparts (`PROTOCOL.txt` = `xz_protocol_v0_73.md`
`08374c0d...`; `FINDINGS_INDEX.txt` = `r27_findings_index.json` `b345f98b...`; `BOUNDARIES.txt` =
`xz_protocol_boundaries.json` `530eaa69...`).

Section 27 enumerates **73 entries, v0.1 through v0.73**, no duplicates, no gaps (tool-derived).

---

## 2. Position ledger (Seven Layers, Twenty-Four Positions)

| Pos. | Name | Result | Finding |
|---|---|---|---|
| 1 | Packet integrity | **PASS** | -- |
| 2 | Test suite | **PASS** | -- |
| 3 | Build gates | **PASS** | -- |
| 4 | Register reproduction | **FAIL** | F-S04-73-12 |
| 5 | Index cardinality | PASS (scoped to R27) | F-S04-73-09 |
| 6 | Index severity fidelity | PASS (scoped to R27) | F-S04-73-09 |
| 7 | Title version | **PASS** | -- |
| 8 | Status line | **FAIL** (4 defects) | -01, -05, -06, -07, -11, -14 |
| 9 | Section 0.1 | **FAIL** | F-S04-73-03 |
| 10 | FB-7b trajectory | PASS | -- |
| 11 | Receipt probe | PASS | -- |
| 12 | Parity probe | PASS | -- |
| 13 | Validation probe | PASS | -- |
| 14 | Format probe | **FAIL** | F-S04-73-10 |
| 15 | Seal chain | **PASS** (73/73 + FULL_SECTION_27) | -- |
| 16 | PRIOR_HISTORY | **PASS** (derivation reproduces) | -- |
| 17 | Append-only | **NOT EVALUABLE** | F-S04-73-15 |
| 18 | Tagging completeness | **FAIL** (16/25 untagged) | F-S04-73-13 |
| 19 | Tag accuracy | **FAIL** (3 of 7 COMPUTED false) | -01, -03, -04 |
| 20 | Dispatch fidelity | **FAIL** | F-S04-73-07, -08 |
| 21 | Triage discipline | Not assessable from this seat | -- |
| 22 | Axiom set | **PASS** (A-X1..A-X5 present in 22.4) | -- |
| 23 | Sidrat clause | **PASS** (present, correctly `[DISCLOSED]`) | -- |
| 24 | The furqan | Reserved to the lead | -- |

**Layer distribution of Class A:** Layer 3 (Positions 8, 9) and Layer 4 (the gate-mechanism claim),
plus Layer 6 (Positions 19, 20). Class A is **not confined** to the self-referential surface.

---

## 3. Findings

### F-S04-73-01 [HIGH] [Class A] -- The gate [2f] relaxation was never implemented

- **Locus:** `build.py:229`; v0.73 amendment entry item (2); `AUDIT_CONTEXT.txt` item (1);
  `CI_METHODOLOGY.txt` line 2; `DISPATCH.txt` line 6.
- **Substance:** The v0.73 entry states, under the tag `[COMPUTED: build.py gate 2f]`: *"Gate [2f]
  VERSION-1 enforcement relaxed: accepts any v0.NN where NN is within 3 of VERSION, not rigidly
  VERSION-1. ... Closes F-S04-70-09, F-S04-70-10."* The shipped gate [2f] is:

  ```python
  check(prov_num == ver_num - 1,
        f"Status provenance v{prov_ver} == v{VERSION} - 1")
  ```

  That is the rigid VERSION-1 rule verbatim. No range logic, no tolerance, no `-3` term exists anywhere
  in `build.py` (grep: zero hits). The build log confirms the executed check is
  `PASS: Status provenance v0.72 == v0.73 - 1`. The claimed repair is **absent from the bytes it claims
  to describe**, and the `[COMPUTED]` tag asserts a tool produced a value no tool produced.
  `DISPATCH.txt`'s "Gate-manufactures-defect class closed" and `AUDIT_CONTEXT.txt` item (1) are byte-false
  on the same ground. F-S04-70-09 and F-S04-70-10 remain OPEN.
- **Disposition:** Either implement the relaxation in `build.py` [2f] and re-derive the entry claim from
  the shipped source, or withdraw item (2), restore F-S04-70-09/10 to OPEN in the register, and correct
  `DISPATCH.txt`, `AUDIT_CONTEXT.txt`, and `CI_METHODOLOGY.txt` in the same act. Do not close a finding
  in prose ahead of the code.
- **Cross-reference:** F-S04-70-09, F-S04-70-10; F-S04-73-02 (same class, live at a new locus);
  F-S04-73-10 (the tag-form defect that let this ship); phantom-repair precedent at R7 (v0.48).

### F-S04-73-02 [HIGH] [Class A] -- The gate-manufactures-defect class is live on v0.73 at gate [10i]

- **Locus:** `build.py` [10i] (`expected_22_2 in body`); protocol Section 0.1, byte offset 3828.
- **Substance:** Gate [10i] asserts `f"v0.1 through v0.{VERSION-1}" in body` -- a presence-anywhere test
  over the whole body, not an assertion at the Section 22.2 locus. On v0.73 bytes the string
  `"v0.1 through v0.72"` occurs **exactly once in the body**, and it is *not* in Section 22.2. It is in
  Section 0.1: *"seventy-three amendment entries, v0.1 through v0.72"* -- the false statement of
  F-S04-73-03. Probe **P1** (mutation landed, manifest resealed) replaced that phrase with the *correct*
  value `v0.1 through v0.73` and the build returned:

  ```
  BUILD FAILED
    FAIL: Section 22.2 carried-entry bound at VERSION-1 (v0.1 through v0.72)
  ```

  Writing the truth breaks the build. The gate structurally requires a false sentence in Section 0.1,
  and the two Class A defects mutually mask: each is the other's alibi.
- **Disposition:** Re-scope [10i] to assert at the locus. Slice Section 22.2 and Section 22.3 out of the
  body by heading and assert the bound *inside each slice*, exactly as [2e]/[2f] assert at the title and
  status loci. Then repair Section 0.1 and Section 22.2 independently.
- **Cross-reference:** F-S04-73-03, F-S04-73-04; the standing presence-anywhere-not-correctness-at-locus
  root class (F-OP17 series); `AUDIT_CONTEXT.txt` "Gate-manufactures-defect class closed" -- refuted.

### F-S04-73-03 [HIGH] [Class A] -- Section 0.1 entry range is arithmetically impossible

- **Locus:** Protocol Section 0.1, final sentence of the Carry-status paragraph; v0.73 entry item (1).
- **Substance:** Section 0.1 reads *"the full defect trajectory is in Section 27 (seventy-three amendment
  entries, v0.1 through v0.72)."* Seventy-three entries cannot span v0.1 through v0.72; that interval
  holds seventy-two. Tool enumeration of Section 27 returns 73 entries, first `v0.1`, last `v0.73`, zero
  duplicates, zero gaps. The correct range is **v0.1 through v0.73**. Entry item (1), tagged
  `[COMPUTED: grep]`, asserts *"'v0.1 through v0.72' matches 73 entries"* -- a false equality that no grep
  computes. This is a recurrence: R29 Seat S03 reported *"an impossible Section 0.1 version range"* on
  v0.72 bytes, and the v0.73 "correction" moved the terminus from v0.69 to v0.72 without fixing the
  arithmetic.
- **Disposition:** Correct to "v0.1 through v0.73" **together with** the [10i] re-scoping of F-S04-73-02
  (correcting this alone turns the build red). Add a gate asserting
  `entry_count == end_version - start_version + 1` at the Section 0.1 locus -- [9e] already implements
  exactly this predicate for cardinal ranges inside the current entry and can be pointed at Section 0.1.
- **Cross-reference:** R29 S03 (impossible Section 0.1 range); F-S01-72-01, F-S01-72-02 (claimed closed by
  entry item (1)); F-S04-73-02.

### F-S04-73-04 [HIGH] [Class A] -- Section 22.2 bound is five versions stale while the entry claims it current

- **Locus:** Protocol Section 22.2, byte offset 88641; v0.73 entry item (4); `AUDIT_CONTEXT.txt` item (4).
- **Substance:** Section 22.2 reads *"For carried entries (v0.1 through v0.68), the PRIOR_HISTORY
  derivation in build.py [9b] detects retroactive mutation."* The bound is five versions stale. Entry item
  (4), tagged `[COMPUTED: grep]`, states *"Section 22.2 coverage bound updated to v0.72"* and *"All version
  tokens in the protocol body tool-verified current."* Both are refuted by grep. Only Section 22.3 was
  updated (`v0.38-v0.72`, verified present). Because gate [10i] is satisfied elsewhere (F-S04-73-02), the
  22.2 locus is entirely unverified: probe **P2b** set it to the absurd *"v0.1 through v0.5"*, resealed,
  and the build returned **BUILD PASSED, 0 fail-checks**.
- **Disposition:** Correct Section 22.2 to "v0.1 through v0.72". Re-scope [10i] per F-S04-73-02 so the
  locus is actually gated. Withdraw the "all version tokens tool-verified current" sentence or produce the
  tool output that supports it.
- **Cross-reference:** F-S04-73-02 (masking mechanism); R17 (v0.58) and R18 (v0.59) Section 22.2/22.3
  version-token staleness -- third recorded recurrence of this exact surface.

### F-S04-73-05 [HIGH] [Class A] -- Status line "4/4 HALT" contradicted by four independent sources including the same document

- **Locus:** Protocol front-matter `**Status:**` line.
- **Substance:** The status line reads *"repair build from v0.72 R29 audit (4/4 HALT; 4-seat round)."*
  Refuted by: (a) the v0.73 amendment entry, twelve lines later in the same file -- *"R29 returned 3/3 HALT
  on v0.72 bytes ... S02 Gemini returned defect closure assessment"*; (b) `R29_TRIAGE.txt` -- *"3/3 HALT + 1
  closure assessment"*; (c) `AUDIT_CONTEXT.txt` -- same; (d) the shipped bytes themselves --
  `SHIPPED_R29_S01/S03/S04_REPORT.md` carry HALT verdicts, and the fourth file is
  `SHIPPED_R29_S02_ASSESSMENT.md`, titled *"v0.72 Defect Closure Assessment"*, which renders no verdict.
  A verdict tally is a value; it is refutable by one grep inside the same packet. Probe **P4** changed
  "4/4" to "9/9", resealed, and the build returned **BUILD PASSED** -- no gate binds verdict counts.
- **Disposition:** Correct to "3/3 HALT + 1 closure assessment; 4-seat round". Extend gate [10g]
  (narrative-index cross-check) to assert the status-line verdict tally against a seat-verdict field in
  the round index, so the value is derived rather than narrated.
- **Cross-reference:** D1 verdict-provenance standing lesson; F-OP18-01 (v0.18, entry asserted a verdict
  refutable by one grep inside the same zip) -- same class, sixth recorded occurrence.

### F-S04-73-06 [HIGH] [Class A] -- Status line and current entry state contradictory Class A recurrence counts

- **Locus:** Protocol front-matter `**Status:**` line; v0.73 entry, sentence 3.
- **Substance:** The status line says *"Class A recurrence R7-R28: 22/22."* The v0.73 entry says
  *"Class A recurrence R7-R29: 23/23."* `R29_TRIAGE.txt` says *"H = 1.0 at 23/23."* The entry and triage
  are correct for a build produced after R29; the status line is one round stale and the two statements
  cannot both be true of the same document. Probe **P7** rewrote the status figure to "R7-R99: 2/2",
  resealed, and the build returned **BUILD PASSED**.
- **Disposition:** Correct the status line to "R7-R29: 23/23". Derive both loci from a single source and
  gate their equality, rather than maintaining the recurrence count at two independent loci.
- **Cross-reference:** F-S04-73-05 (same locus, same class); substrate-of-record uniqueness rule
  (BAF v3.0) -- a fact stated twice is a fact that will diverge.

### F-S04-73-07 [HIGH] [Class A] -- Three-way methodology-identity contradiction, unrepaired from R29

- **Locus:** Protocol front-matter `**Status:**` line; `AUDIT_CONTEXT.txt` header; `METHODOLOGY.txt`.
- **Substance:** Three shipped surfaces name three different methodologies:
  - Protocol status line: *"Methodology: v7 canonical (six strings)."*
  - `AUDIT_CONTEXT.txt`: *"Methodology: Six Strings, Twenty-One Positions (v7)."*
  - `METHODOLOGY.txt` (the actual shipped document): *"Seven Heavens. Seven Earths. Twenty-Four
    Verification Positions"*, seven layers, twenty-four positions, and self-identified as **v6** --
    *"v6 retains the insight ... but removes the assignment"*, superseding v1 through v5.

  Grep of `METHODOLOGY.txt` for "six string", "twenty-one", "21 position", and "v7" returns **zero hits**.
  There is no six-string, twenty-one-position methodology in this packet. R29 Seat S03 reported this exact
  defect on v0.72 -- *"the unreconciled six-string/21-position versus seven-layer/24-position methodology
  contradiction"* -- and v0.73 did not repair it. Probe **P5** rewrote the token to "v99 canonical (nine
  trombones)", resealed, and the build returned **BUILD PASSED**.

  `METHODOLOGY.txt` is additionally stale on its own terms: it declares itself *"the canonical methodology
  for all rounds from R28 onward"*, its Section 15 (Path to FROZEN) is keyed to v0.69 and *"the key
  question at R28"*, its Section 17.1 series terminates at R27, and its Section 1 gives
  *"P = 22/23 = 0.957"* -- all four rounds and five versions behind the artifact under audit.
- **Disposition:** Decide which methodology is canonical and make the three surfaces say it. If
  `METHODOLOGY.txt` is canonical, correct the status line and `AUDIT_CONTEXT.txt` to
  "v6, seven layers, twenty-four positions" and refresh Sections 1, 15, and 17.1 to R29/v0.72. If a v7
  exists, ship it. Add the methodology token to the [2b]-family version-prose gate.
- **Cross-reference:** R29 S03 (same finding, v0.72, not discharged); F-S04-73-08 (same document, seat
  table); Position 20 (dispatch fidelity).

### F-S04-73-08 [HIGH] [Class A] -- Shipped witness table contradicts the shipped seat assignments

- **Locus:** `METHODOLOGY.txt` Section 5, "Current Witness Pool"; v0.73 amendment entry sentence 2;
  `DISPATCH.txt`.
- **Substance:** `METHODOLOGY.txt` Section 5 tables the pool as S01 = Claude Opus 5 (ADVISORY,
  producer-family), S02 = Kimi K3 (CARRYING, binding), S03 = GPT-5.6 Sol (ADVERSARIAL), S04 = Gemini 3.1
  Pro (ADVISORY, *"Textual analysis; no code execution"*). The v0.73 entry records the R29 round as
  S01 = Kimi K3 CARRYING, S02 = Gemini, S03 = GPT-5.6 Sol, S04 = Claude Opus 5 ADVISORY. `DISPATCH.txt`
  routes seat S04 in this round to Claude Opus 5. Three of four slots are inverted between the two shipped
  documents. This is not cosmetic: seat-to-family mapping is the predicate of the producer-family exclusion
  rule and of the two-family carry requirement (FB-7b, Section 22.1), and `METHODOLOGY.txt`'s S04 row
  further asserts a capability ("no code execution") that is false of the seat actually occupying the slot
  -- this seat executed the full packet.
- **Disposition:** Make the witness table derived rather than narrated. Emit Section 5 from the same round
  index that gate [10g] already reads, and gate the seat/family/role triple against `DISPATCH.txt` at
  build time. Until then, correct Section 5 to match the R29/R30 assignments and strike the
  capability claim.
- **Cross-reference:** F-S04-73-07 (same document, stale); seat-provenance defect class (F-OP18-04, v0.16
  through v0.18, three consecutive cycles); `METHODOLOGY.txt` Section 13 requires 9 of 10 dispatch files
  byte-identical across witnesses -- unverifiable from a single seat.

### F-S04-73-09 [MEDIUM] [Class D] -- Gate [13] is pinned to R27 and cannot see the R28 or R29 reports

- **Locus:** `build.py` [13], `report_files` glob and `version_filter`; `AUDIT_CONTEXT.txt` build-status
  block; v0.73 entry item (5).
- **Substance:** Gate [13] selects reports with
  `[f for f in os.listdir(".") if f.startswith("R") and f.endswith("_REPORT.md")]`. On v0.73 bytes that
  glob resolves to exactly four files -- `R27_S01..S04_REPORT.md`. The eight R28/R29 reports ship under a
  `SHIPPED_` prefix and are excluded by the first character; `XZ_v070_R28_S01_REPORT.md` is excluded by
  the same test. The index is `r27_findings_index.json` (`version: 0.68`, `round: 27`). The "39/39" is
  therefore R27 fidelity, three rounds and five versions stale, and confers zero verification on the
  reports this round actually turns on. The pinning is doubled: probe **P3** renamed
  `SHIPPED_R29_S04_REPORT.md` to `R29_S04_REPORT.md`, resealed, and the build still returned
  **BUILD PASSED** -- because `version_filter` is derived from the index version ("68") and filters out
  every `F-S04-72-*` ID even once the file is in scope. Entry item (5)'s *"R29 seat reports (3 files + 1
  assessment) shipped in-packet and manifested"* is true and, as a verification claim, empty.
- **Disposition:** Advance `index_file` to an R29 index and normalise report filenames to the glob, or
  replace the glob with an explicit manifest of the round's reports. State the gate's round scope in its
  own PASS line (`CI-8 cardinality (round 27)`) so a stale index is visible in the build output rather
  than inferable from the filename.
- **Cross-reference:** F-S01-68-01 (gate [13] vacuous, closed at v0.70) -- the vacuity was closed and the
  *scope* staleness replaced it; R23 (v0.64) "CI-8 gap 17 findings".

### F-S04-73-10 [MEDIUM] [Class D] -- COMPUTED-tag validation is evaded by tag form, and that is how F-S04-73-01 shipped

- **Locus:** `build.py` [9c], regex `\[COMPUTED:\s*build\.py\s*\[([^\]]+)\]\s*([^\]]*)\]`;
  v0.73 entry item (2).
- **Substance:** [9c] validates that a `[COMPUTED: build.py [X] ...]` tag names a section that exists in
  `build.py`. The regex requires the section id in **square brackets**. The v0.73 entry writes
  `[COMPUTED: build.py gate 2f]` -- unbracketed -- so the regex does not match and the tag is never
  validated at all. Paired probes isolate the mechanism (both resealed; seal-level noise identical across
  the pair, so the contrast is the [9c] check alone):

  | Probe | Tag written | [9c] outcome |
  |---|---|---|
  | **P8** | `[COMPUTED: build.py [zz9] fake]` | `FAIL: COMPUTED tag references existing build.py section [zz9]` |
  | **P9** | `[COMPUTED: build.py gate zz9]` | no [9c] failure -- tag invisible |

  This is Position 14 (format probe: strict regex match, not prefix-only) failing, and it is the enabling
  mechanism for F-S04-73-01: the false relaxation claim carries a `[COMPUTED]` grade that no gate ever
  examined.
- **Disposition:** Widen [9c] to match `build.py` followed by an optional `gate`/`section` keyword and an
  optionally-bracketed identifier, and fail-closed on any `[COMPUTED: build.py ...]` tag the regex cannot
  parse -- an unparseable provenance tag must be an error, not a silent skip.
- **Cross-reference:** F-S04-73-01 (the claim this defect protected); the silent-skip class
  (F-ADJ19-05, F-OP20F-08); standing boundary 1 ("[9c] arity-one regex").

### F-S04-73-11 [MEDIUM] [Class A / Class D] -- `boundaries.json` version field is stale and ungated while the status line asserts it current

- **Locus:** `xz_protocol_boundaries.json` field `version`; protocol status line; `build.py` [10f].
- **Substance:** The file carries `"version": "0.72"` at VERSION 0.73. The status line asserts, in its
  "Prescribed repairs landed" list, *"boundaries.json version current."* Gate [10f] couples only the item
  **count** (35) to the register; the version field is read by nothing. Probe **P6** set the field to
  `"0.01"`, resealed, and the build returned **BUILD PASSED**.
- **Disposition:** Either stamp the file to VERSION at build time and add a `check()` in [10f], or declare
  the field non-normative and strike the status-line claim. A field that is asserted current in prose and
  gated by nothing is the exact shape this program keeps re-finding.
- **Cross-reference:** F-S04-73-14 (the status-line repair list it sits in); R15 (v0.56) boundary-30
  staleness; version-stamp loop precedent at v0.18.

### F-S04-73-12 [MEDIUM] [Class D] -- Position 4 fails: the shipped register is not the generator's output

- **Locus:** v0.73 entry, "R27 defect register disposition" paragraph;
  `xz_protocol_register_gen.py::generate_register`.
- **Substance:** Position 4's criterion is byte-exact reproduction of the shipped register from the
  generator. Importing the shipped generator and running it against `r27_findings_index.json` yields
  **4060 characters**; the shipped register is **877 characters** -- an abridgement that drops every
  `Source distribution:` and `Adjudication:` clause. Items (5) and (6) are additionally **transposed**
  relative to generator order: shipped (5) carries `F-S01-68-05 / F-S04-68-07` (CRITICAL remap, MEDIUM)
  where the generator emits that pair at (6). Content travels with its IDs, so no attribution is falsified
  -- this is ordering and abridgement, not a false claim -- and the paragraph is honestly tagged
  `[ASSERTED]` rather than `[COMPUTED: generate_register]`. The two other generator outputs *are*
  byte-exact: `generate_boundary_list` reproduces the shipped 35-item paragraph exactly, and
  `generate_terminal_line` reproduces the terminal line exactly. The register is the sole CI-1R surface
  that is hand-maintained, and no gate binds it.
- **Disposition:** Either emit the register verbatim from `generate_register` (as is already done for the
  boundary list and terminal line) and re-tag it `[COMPUTED]`, or add a gate asserting that each shipped
  register item's finding-ID set and severity match the generator's item at the same ordinal.
- **Cross-reference:** R14 (v0.55) "register finding-ID transposition, Class A" -- same surface, this time
  without a false attribution; Position 4.

### F-S04-73-13 [MEDIUM] [Class B] -- The ASSERTED fraction improved by shrinking its denominator

- **Locus:** v0.73 amendment entry; `build.py` [9c] tag census.
- **Substance:** The build reports `COMPUTED: 7, EXTERNAL: 0, ASSERTED: 2` and an ASSERTED fraction of
  **2/9 (22.2%)** -- the lowest in the recorded series, against a band the program itself described as
  87-93% at v0.36. The improvement is an artifact of the denominator. Independent sentence census of the
  v0.73 entry: **25 sentences, 16 untagged**, against Position 18's criterion of *zero* untagged sentences
  in the current entry. The untagged set includes the entry's most load-bearing claims -- *"Class A
  recurrence R7-R29: 23/23"*, *"The gate no longer manufactures false provenance claims when the build
  skips a version"*, *"All version tokens in the protocol body tool-verified current"*, *"Tool-derived,
  not narrated"*. Of the 7 `[COMPUTED]` tags, **3 are false or unverifiable** on the shipped bytes
  (F-S04-73-01, -03, -04). Counting only tagged claims, the metric reads 22.2%; counting claims, the
  ASSERTED-or-untagged fraction exceeds 70%, and the COMPUTED-and-true fraction is 4/25.
- **Disposition:** Report both denominators explicitly in the entry, as v0.26 was required to do for the
  same defect (F-GLM26-02). Add a [9c] sub-check counting untagged sentences in the current entry and
  print it beside the fraction, so Position 18 is measured rather than assumed.
- **Cross-reference:** F-GLM26-02 (ASSERTED-fraction denominator understated, v0.26 -- recurrence);
  F-OP20-03 (untagged narrative claims detected by no gate, DISCLOSED NOT CLOSED since v0.20);
  Position 18.

### F-S04-73-14 [LOW] [Class C] -- The status line's "prescribed repairs landed" list enumerates the *previous* build's repairs

- **Locus:** Protocol front-matter `**Status:**` line.
- **Substance:** The status line reads *"Prescribed repairs landed: C-suffix in all five
  DECLARATION_PATTERNS, gate [13] fail-closed, register generator graceful degradation, boundaries.json
  version current."* `CI_METHODOLOGY.txt` attributes gate [13] fail-closed and the terminal dual-token to
  **v0.72**, and the v0.73 entry's own repair list is a disjoint set of five different items. The
  front-matter narrates v0.72's repairs on a v0.73 artifact, and its last element is now false
  (F-S04-73-11).
- **Disposition:** Replace with the v0.73 repair list, or point to the entry rather than duplicating it.
  Duplication at two loci is what let this drift.
- **Cross-reference:** F-S04-73-11; substrate-of-record uniqueness rule.

### F-S04-73-15 [LOW] [evidence limit, not a defect claim] -- Position 17 is NOT EVALUABLE from this seat

- **Locus:** Position 17 (append-only); Section 22.2 self-consistent-forgery boundary.
- **Substance:** Gate [9b] verifies 73 of 73 `ENTRY_v0.k` seals against the shipped Section 27 bytes,
  verifies `FULL_SECTION_27`, and derives `PRIOR_HISTORY` successfully -- all four checks reproduce
  independently in this seat's environment. That establishes **internal** consistency only. This seat
  holds no v0.72 packet and no external anchor, and Section 22.2 states plainly that internal derivation
  cannot distinguish an authentic packet from a self-consistent forgery where `HISTORY.sha256` is
  regenerated over mutated text. Position 17's criterion ("prior entry seals unchanged from prior build")
  is therefore **UNKNOWN**, not TRUE, on this seat's evidence. Reporting it as TRUE would be the exact
  class of claim this instrument exists to catch.
- **Disposition:** Route Position 17 to a seat holding prior-version bytes, or publish `PRIOR_HISTORY`
  outside the producer's control so a fresh seat can anchor against it. Standing boundary 32
  ("self-consistent resealing blind spot") covers the residual; this finding records that the residual
  was **load-bearing for this round's verdict scope**, not merely disclosed.
- **Cross-reference:** Section 22.2; standing boundaries 32 and 34; A-X4 (append-only storage integrity);
  F-OP18-05 (PRIOR_HISTORY cross-anchoring).

---

## 4. Probe battery

Ten probes, each with a mutation-landed digest assertion and a `PACKET_SHA256SUMS` reseal, so that the
manifest gate is not the discriminator and semantic gates are tested in isolation. A probe whose mutation
did not land is VOID and is not reported; none were void.

| Probe | Mutation | Landed | Build | Reading |
|---|---|---|---|---|
| **P0** | none (clean packet) | -- | PASSED, 0 fail-checks | baseline green is real |
| **P-neg** | title `v0.73` -> `v0.72` | yes | **FAILED** (`Title version v0.72 == VERSION v0.73`) | control: gates discriminate |
| **P1** | Section 0.1 range -> **v0.73** (the true value) | yes | **FAILED** (`Section 22.2 carried-entry bound`) | **truth breaks the build** (F-S04-73-02) |
| **P2** | Section 22.2 -> v0.72 (the true value) | yes | PASSED | correct value is accepted |
| **P2b** | Section 22.2 -> "v0.1 through v0.5" | yes | **PASSED** | **false-PASS**: 22.2 locus ungated |
| **P3** | rename `SHIPPED_R29_S04` into the [13] glob | yes | **PASSED** | **false-PASS**: `version_filter` pins to R27 |
| **P4** | status "4/4 HALT" -> "9/9 HALT" | yes | **PASSED** | **false-PASS**: verdict tally ungated |
| **P5** | status methodology -> "v99 (nine trombones)" | yes | **PASSED** | **false-PASS**: methodology token ungated |
| **P6** | `boundaries.json` version -> "0.01" | yes | **PASSED** | **false-PASS**: version field ungated |
| **P7** | status "R7-R28: 22/22" -> "R7-R99: 2/2" | yes | **PASSED** | **false-PASS**: recurrence count ungated |
| **P8** | `[COMPUTED: build.py [zz9] fake]` | yes | **FAILED** ([9c] fires) | bracketed form is validated |
| **P9** | `[COMPUTED: build.py gate zz9]` | yes | no [9c] failure | **false-PASS**: unbracketed form evades [9c] |

Six demonstrated false-PASS paths, all in the **protocol prose and the JSON side-files** -- none in the
code layer, which remains clean. P1 is the round's most significant result: it is the first probe in this
seat's experience where inserting the **correct** value is what turns the build red.

---

## 5. Coverage measurement

| Surface | Chars | Share |
|---|---|---|
| Total document | 479,770 | 100% |
| Body (in scope for gates) | 108,007 | 22.5% |
| Section 27 (outside every semantic gate) | 371,763 | **77.5%** |
| Semantic-gate coverage of the body | 32,303 | 29.9% of body |
| Semantic-gate coverage of the document | 32,303 | **6.7% of total** |

Every Class A finding in this report lives in the 93.3% the semantic gates do not read, or in a JSON
side-file no gate reads at all. That is the measurement, not a target -- but it is the structural
explanation of the H = 1.0 series, and it has worsened monotonically (Section 27 was 26.2% of the document
at v0.18).

---

## 6. Bearer assessment (BSSG three-valued)

| Bearer | Value | Basis |
|---|---|---|
| 1. Append-only | **UNKNOWN** | 73/73 seals + `FULL_SECTION_27` + `PRIOR_HISTORY` derivation all verify internally; no held prior bytes, no external anchor (F-S04-73-15) |
| 2. Code correctness | **TRUE** | 186 passed rc=0; build 291 PASS / 0 FAIL rc=0; `sha256sum -c` 36/36 rc=0 |
| 3. Surface narrowing | **FALSE** | Defect surface did not migrate upward. It returned to Layer 3 (Positions 8, 9) and Layer 4 (the gate-mechanism claim of F-S04-73-01) |
| 4. Goedel confinement | **FALSE** | 8 Class A findings; only F-S04-73-13 is confined to Positions 18-21. Positions 8, 9, 14, 20 all carry Class A |
| 5. Cross-vendor witness | **FALSE** | R29 returned 3 HALT from three families; this seat is producer-family advisory and carries no weight |
| 6. Axiom disclosure | **TRUE** | A-X1..A-X5 present and complete in Section 22.4; Sidrat clause present and correctly `[DISCLOSED]` |
| 7. Methodology verification | **FALSE** | Position 18 fails (16/25 untagged), Position 19 fails (3 of 7 COMPUTED false), Position 20 fails (F-S04-73-07, -08), index three rounds stale |
| 8. The furqan | **RESERVED** | Position 24 is the lead's act, given and not derived. This seat does not exercise it |

Four bearers FALSE, one UNKNOWN. Under FALSE-dominance the computational bearers do not clear, and
FROZEN is not reachable on v0.73 bytes.

---

## 7. Standing-rules compliance sweep

| Rule | Result |
|---|---|
| Em-dash policy (U+2013/2014/2015) | **CLEAN** -- zero occurrences in protocol, `build.py`, `METHODOLOGY.txt`, `AUDIT_CONTEXT.txt`, `DISPATCH.txt` |
| Brand canonical ("BayyinahEnterprise") | **CLEAN** -- zero occurrences of the spaced or plural form |
| Severity uppercase | **CLEAN** -- zero lowercase severity tokens in finding contexts |
| Six-element findings format | Applied to all 15 findings in this report |
| Substrate-of-record uniqueness | **VIOLATED** by the artifact -- F-S04-73-05, -06, -11, -14 are all two-locus duplications that diverged |
| Audit-chain immutability | Not violated on these bytes; Section 27 is append-only-consistent internally |

---

## 8. Root class and forward prediction

**Root class.** Every Class A in this round reduces to one mechanism: **a claim about a mechanism, stated
in prose, at a locus no gate reads.** F-S04-73-01 claims build.py behaves a way it does not.
F-S04-73-04 claims a grep result the grep refutes. F-S04-73-05 claims a verdict tally the shipped reports
refute. F-S04-73-07 and -08 claim a methodology and a seat pool the shipped documents refute. The code
layer has been clean since R22 and remains clean; the defect has finished migrating out of the mechanism
and into the description of the mechanism, and the description is 93.3% ungated.

**The v0.73-specific inversion.** F-S04-73-02 is a genuinely new shape and worth naming. Prior rounds
found gates that failed to catch false statements. This round found a gate that **requires** one: [10i]
passes only because Section 0.1 is wrong, and correcting Section 0.1 turns the build red. The
"gate-manufactures-defect" class that `DISPATCH.txt` declares closed is not only open, it has produced its
cleanest instance to date -- and it did so through a repair (moving the Section 0.1 terminus v0.69 -> v0.72)
that was itself prescribed by R29.

**Forward prediction for R31, offered so the next seat can test it rather than rediscover it.** The
program's outermost unhashed layer is no longer the protocol prose -- `PACKET_SHA256SUMS` now covers 36 of
37 members. It is the **dispatch envelope**: `DISPATCH.txt`, `AUDIT_CONTEXT.txt`, `CI_METHODOLOGY.txt`,
`METHODOLOGY.txt`, `R29_TRIAGE.txt`, and `R29_REPORTS.txt` are shipped to every witness, are load-bearing
for what each witness believes about the artifact, and are covered by no manifest and no gate. Three of
this round's eight Class A findings (-01, -07, -08) are already there. Unless the dispatch envelope is
hashed into the packet and its claims derived from the protocol rather than narrated alongside it, the
R31 Class A will be a false statement in a dispatch file about the artifact it dispatches.

---

## 9. Recommendation

1. **Absorb F-S04-73-01 first and in the correct order** -- implement gate [2f] in code, or withdraw the
   claim and reopen F-S04-70-09/10. Do not carry a `[COMPUTED]` tag on an unimplemented repair into
   another round.
2. **Repair F-S04-73-02, -03, and -04 as one atomic change.** Re-scope [10i] to assert at the Section 22.2
   and 22.3 loci, then correct Section 0.1 to v0.73 and Section 22.2 to v0.72. Repairing any one alone
   either turns the build red (P1) or leaves the locus unverified (P2b).
3. **Derive the status line rather than narrating it.** Verdict tally, recurrence count, methodology token,
   and repair list should each be emitted by a generator and gated, exactly as the boundary list and
   terminal line already are. Four of this round's eight Class A findings are in one sentence.
4. **Advance gate [13] to R29** and normalise the report filenames, so shipping the reports means
   verifying them.
5. **Fail-closed on unparseable provenance tags** in [9c] (F-S04-73-10).
6. **Cross-vendor rotation.** This seat is Anthropic, the producer is Anthropic; this round carries
   **advisory weight only** and does not touch FB-7b. Route R31 to Kimi K3 and to a second non-producer
   family. Ask the carrying seats specifically to (a) hold v0.73 bytes across the round so Position 17 can
   move from UNKNOWN to a verdict, and (b) attack the **dispatch envelope**, which is where this seat
   predicts the next Class A will land.
7. **Position 24 is not exercised here.** The bayyinah is the record above; the furqan is the lead's.

---

*Seat S04, Round 30. Advisory, non-carrying. The record is the evidence.*

---

# Bismillah ir-Rahman ir-Rahim
