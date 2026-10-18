# Bismillah ir-Rahman ir-Rahim

# R0983 -- Bayyinah v1.2.4 - Round 11 audit closure (red-team CRITICAL findings)

**Chronological Index:** 209 of 995  
**Date:** 2026-05-04  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** v1_2_4_round_11_prompt.md  
**Source Format:** md  
**SHA-256:** `bd546b9333a8332caa402640aaf576c03184cf476afe02cda512b0f070367314`  

---

## R0983 · Bayyinah v1.2.4 - Round 11 audit closure (red-team CRITICAL findings)

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: v1_2_4_round_11_prompt.md
- source_format: md
- text_sha256: bd546b9333a8332caa402640aaf576c03184cf476afe02cda512b0f070367314

# Bayyinah v1.2.4 - Round 11 audit closure (red-team CRITICAL findings)

You are executing v1.2.4 of Bayyinah Integrity Scanner as **Round 11** of the Bayyinah audit chain, continuing from Round 10 (audit-of-self against v1.2.2, closed in v1.2.3 release commit 86c8351). Every round in the Bayyinah chain is audit-of-self by Bilal Syed Arfeen under Bayyinah Audit Framework v3.0 §1.2 and §15. Fraz Ashraf is acknowledged for the engineering-approach contribution to the framework itself (v3 §27) and is co-author on joint research papers; he is not an auditor on the Bayyinah chain. The validator-by-different-instance protocol (v3 §5.2) is satisfied at the Claude-instance axis: cowork Claude produced v1.2.3's substrate; the executor of this prompt is a fresh instance with no continuity to that producer; Bilal in the auditor role generated the empirical reproducer (the red-team report dated 2026-05-04 with 10 fixtures against deployed bayyinah.dev).

**Attribution-discipline note for v1.2.4 CHANGELOG.** v1.2.3's commit messages (d032553, e572091, 54942b0, 86c8351) attributed Round 10 findings to "Fraz round 10". This is the same imprecision pattern v3 §18.10 names (the furqan-lint v0.8.5 attribution corrective). The historical commit messages stand verbatim per the immutability discipline; the v1.2.4 CHANGELOG includes a brief attribution-discipline note correcting the framing going forward. See §13 CHANGELOG template.

This prompt is locked. Do not negotiate scope, severity, or commit count with the user mid-execution. If something appears load-bearing that this prompt does not authorise (see §17), stop and request a prompt revision rather than extending scope.

---

## Operating discipline (read first; bind for every commit)

**Validator-bias disclosure (non-negotiable).** Before applying any fix, reproduce every finding empirically against v1.2.3's substrate. Do not trust this prompt's classification. The prompt is the producer's account; the substrate is what the test suite says. Any divergence between this prompt and what the substrate actually does is itself a Round 11 finding to surface in your handoff.

**Severity per v3 §7 (impact, not appetite).**
- Four CRITICAL: fixtures 01, 02, 04, 07 silent-pass v1.2.3 at integrity_score 1.000 / sahih on multi-layer integrity traps. Per v3 §7 "claimed feature does not function" applied to Bayyinah's core thesis (concealed-content detection) on its highest-priority attack class. Per v3 §15.1, surfacing CRITICAL severity in an audit-of-self round is the structural defense against severity deflation: the auditor classified by impact, not by appetite for fixing.
- Five HIGH: fixtures 03, 05, 06, 09, 10 partial-catch (flagged the layer's existence; missed the divergent payload content within it).
- One MEDIUM: tier-classification audit. Currency tokens currently surface at tier-3 in `image_text_metadata`; per the substrate-readability rule, tier-2 minimum on currency tokens absent from rendered output.

**Em-dash discipline (project standard).** Zero em-dashes in any user-facing prose written by this round. CHANGELOG, README, FRAMEWORK.md, RETIREMENT_LEDGER.md, finding descriptions, and commit messages are all user-facing. Code comments are exempt. Verify with `grep -c "—"` against every changed prose file before each commit. If a code-comment em-dash trips the sweep, decide case-by-case.

**Dependency manifest discipline (project standard).** Any new third-party imports go in BOTH `requirements.txt` AND `pyproject.toml` in the same patch, capped at the current major. The seven new analyzers in this round should not require new third-party deps. Flag and stop if any do.

**Additive-only invariant (v3 §18.3).** No removals from `bayyinah.__all__`. New public names are allowed. A new `V1_2_4_SURFACE` frozenset lands in `tests/test_public_surface_additive.py` whether or not `__all__` changes; the per-version cadence rule from v1.2.3 commit 54942b0 stands. If unchanged, alias `V1_2_4_SURFACE = V1_2_3_SURFACE`.

**Five-place pattern (Bayyinah extension of v3 §11).** A documented detection mechanism reaches: CHANGELOG, README, fixture, pinning test, AND `bayyinah/mechanisms/registry.py` with its tier and cost class. Five places.

**Branch:** `v1.2.4-round-11-closure` off main. Baseline: commit 86c8351 (v1.2.3 release). 13 commits expected.

---

## §0 Pre-flight self-review (v3 §12.1, applied before commit 1)

1. Confirm the 10 fixtures and their builders are accessible. Bilal will mount the corpus at `/tmp/redteam/` or copy it into `tests/redteam/round_11_gauntlet/` directly. If neither location exists, ask before proceeding.
2. State expected post-fix test count: 1837 (v1.2.3 baseline) plus 30 to 50 new tests = 1870 to 1890. Capture the actual count after each commit.
3. State expected mech registry count: 113 (current) plus 7 new plus 4 extended descriptions = 120 entries. Verify against `bayyinah/mechanisms/registry.py` after commit 11.
4. Run the v3 four-revision check on this prompt itself. If you find more than two acceptable residual concerns after your first read, stop and request revision 2.

---

## §1 Commit 1: Seed Round 11 corpus

Layout under `tests/redteam/round_11_gauntlet/`:

```
README.md                         # round provenance, fixture index, expected verdicts
EXPECTED.json                     # machine-readable pre-fix and post-fix verdicts
REDTEAM_v1_2_3_REPORT.md          # the 2026-05-04 red-team report, verbatim
fixture_01_pdf_acroform_override.pdf
... (fixtures 02 through 10)
build_01_pdf_acroform_override.py
... (builders 02 through 10)
test_corpus_round_trips.py        # asserts every fixture regenerates byte-identically
test_corpus_pre_fix_verdicts.py   # parametrised; passes against v1.2.3, inverts post-fix
```

Determinism: each `build_NN_*.py` MUST be deterministic. Wrap any timestamp or RNG in a `freezegun` freeze and a fixed seed at module top. The corpus round-trip test asserts sha256 stability across two consecutive regen runs.

Commit message:
```
seed Round 11 corpus (red-team v1.2.3 gauntlet)

Adds the 10-fixture multi-layer-consensus-trap corpus that surfaced
4 CRITICAL silent-passes and 5 HIGH partial-catches against v1.2.3
on bayyinah.dev. Each fixture has a deterministic builder and an
expected pre-fix and post-fix verdict in EXPECTED.json. Subsequent
commits in this round close the 10 findings against the locked
corpus.

Round provenance: red-team probe of bayyinah.dev v1.2.3, dated
2026-05-04, reported in REDTEAM_v1_2_3_REPORT.md (this commit).

Five questions:
1. Smallest input demonstrating the corpus works:
     pytest tests/redteam/round_11_gauntlet/test_corpus_round_trips.py
2. Smallest input that would have shown the gap on v1.2.3:
     pytest tests/redteam/round_11_gauntlet/test_corpus_pre_fix_verdicts.py
   (passes against v1.2.3; inverts after the round-N closure commits land)
3. What this commit does not do: it does not close any finding. It
   establishes the corpus that subsequent commits close.
4. New code paths: 10 fixture builders, 1 round-trip test, 1
   parametrised pre-fix verdict test. No production code changes.
5. Limitations retired: none. Round 11 opens here.

Co-authored-by: Claude (cowork) <claude+cowork@anthropic.com>
```

---

## §2 Commit 2: CRITICAL 01 - `pdf_acroform_field_value_payload`

**Reproduce first.** `pytest tests/redteam/round_11_gauntlet/test_corpus_pre_fix_verdicts.py::test_fixture_01_silent_passes_v1_2_3` must pass before this commit.

**Spec.**
- New module `bayyinah/analyzers/pdf_acroform_field_value_payload.py`.
- Walk `/AcroForm /Fields` recursively; extract each field's `/V` (value) and `/DV` (default value).
- Fire tier-1 (mushtabih or stronger) when (a) the field has the Hidden flag bit (bit 2) set in `/F`, OR (b) the `/V` text contains a token that does not appear in any rendered page's content stream.
- Cost class: B (selective scan, not full document).
- ZAHIR/BATIN per v4.1: BATIN.
- Registry entry: `pdf_acroform_field_value_payload` with description "Concealed value in AcroForm field /V or /DV not present in rendered page content".

**Tests (minimum 5).**
1. `test_acroform_v_token_not_on_page_fires_tier_1` (fixture 01)
2. `test_acroform_v_token_on_page_does_not_fire` (control)
3. `test_acroform_hidden_flag_set_fires_tier_1`
4. `test_acroform_no_fields_does_not_fire` (no false positive)
5. `test_acroform_dv_default_value_also_scanned`

**Five-place documentation:** README bullet under "Detection mechanisms"; fixture 01 already in corpus; pinning test `tests/redteam/round_11_gauntlet/test_finding_01_acroform_closed.py`; registry entry; CHANGELOG deferred to release commit (§13).

**Verification before commit:** analyzer test file passes; corpus closure test passes; em-dash count 0 on the new module; existing surface tests still pass.

Commit message:
```
add pdf_acroform_field_value_payload analyzer (Round 11 CRITICAL 1)

Closes Round 11 fixture 01: a PDF whose AcroForm field /V says
$99M while the rendered page draws $9K silent-passed v1.2.3 at
integrity_score 1.000 / sahih.

Per v3 §7, this is CRITICAL: the scanner's claimed feature
(concealed-content detection) did not function on a multi-layer
integrity trap that is the document equivalent of invoice fraud.
The fix walks /AcroForm /Fields, extracts each /V and /DV, and
fires tier-1 when (a) the Hidden flag bit is set in /F or (b) the
value text contains a token not in any rendered page's content
stream.

Five questions:
1. Smallest input demonstrating fix:
     pytest tests/redteam/round_11_gauntlet/test_finding_01_acroform_closed.py
2. Smallest input that would have shown the bug on v1.2.3:
     curl -F file=@fixture_01_pdf_acroform_override.pdf https://bayyinah.dev/scan
3. What this fix does not do: it does not close fixtures 02, 04, 07
   (each its own analyzer); does not synthesise the cross-layer
   meta-finding (deferred to v1.2.5).
4. New code paths: one analyzer module, five tests in the analyzer
   test file, one closure-pinning test in the corpus directory.
5. Limitations retired: closes Round 11 CRITICAL 1.

Co-authored-by: Claude (cowork) <claude+cowork@anthropic.com>
```

---

## §3 Commit 3: CRITICAL 02 - `pdf_tounicode_remap`

This is the most novel attack class in Round 11 (content-stream operators vs post-extraction text, structurally distinct from cross-layer reconciliation).

**Spec.**
- New module `bayyinah/analyzers/pdf_tounicode_remap.py`.
- For each font, parse the `/ToUnicode` CMap stream.
- For each `bfchar` mapping, fire tier-1 when (a) the mapped Unicode length per source glyph code exceeds 2 codepoints, OR (b) the mapped Unicode differs from the standard Unicode for that source code in WinAnsi or MacRoman encoding (strict equality).
- Cost class: B (skip documents with no custom ToUnicode).
- ZAHIR/BATIN: BATIN.
- Registry: `pdf_tounicode_remap`, description "Custom ToUnicode CMap remaps drawn glyphs to divergent extracted text (concealment via glyph-translation manipulation)".

**Tests (minimum 6).**
1. `test_tounicode_length_inflation_fires` (fixture 02: 0x39 maps to "99", 0x30 to "00000")
2. `test_tounicode_codepoint_substitution_fires`
3. `test_tounicode_identity_does_not_fire`
4. `test_no_tounicode_cmap_does_not_fire`
5. `test_multiple_fonts_evaluated_independently`
6. `test_extracted_text_recorded_in_finding` (payload includes source code and divergent Unicode)

Five-place doc, verification, and commit message follow the §2 template, swapping specifics. Mention that this defect class is not closed by the v1.2.5 cross-layer meta-mechanism.

---

## §4 Commit 4: CRITICAL 04 - `docx_alternate_content_divergence`

**Spec.**
- New module `bayyinah/analyzers/docx_alternate_content_divergence.py`.
- Walk every `mc:AlternateContent` in `word/document.xml` and header/footer parts.
- Normalise text content of `mc:Choice` and `mc:Fallback` (whitespace, lowercase, punctuation strip).
- Fire tier-1 when the two texts differ in any currency-shaped token (regex `\$\d[\d,]*\.\d{2}` plus the international variants from §5).
- Cost class: B. BATIN.
- Registry: `docx_alternate_content_divergence`.

**Tests (minimum 5).** Including a control where Choice and Fallback agree (no fire), one where they differ only in cosmetic markup (no fire), and fixture 04 (fires).

---

## §5 Commit 5: CRITICAL 07 - `eml_alternative_part_numeric_divergence`

**Spec.**
- New module `bayyinah/analyzers/eml_alternative_part_numeric_divergence.py`.
- Walk every `multipart/alternative` block (including nested).
- Extract currency-shaped tokens from each part. Currency regex set:
  - USD: `\$\d[\d,]*(?:\.\d{2})?`
  - EUR: `€\s?\d[\d.,]*` (note European decimal/thousand convention)
  - GBP: `£\s?\d[\d,]*(?:\.\d{2})?`
  - JPY: `¥\s?\d[\d,]*`
  - ISO codes: `(?:USD|EUR|GBP|JPY)\s+\d[\d,.]*`
- Fire tier-1 when any two parts disagree on any currency-shaped token after normalisation.
- Cost class: B. BATIN.
- Registry: `eml_alternative_part_numeric_divergence`.

**Tests (minimum 6).** Including unicode currency symbols, tab-separated currency in plain-text, HTML with whitespace-stripped currency, and fixture 07.

---

## §6 Commit 6: HIGH 03 - extend `pdf_metadata_analyzer`

**Spec.**
- Existing `bayyinah/analyzers/pdf_metadata_analyzer.py` only flags `/Keywords`. Extend the not-on-rendered-page check symmetrically to `/Title`, `/Subject`, `/Author`, `/Creator`, `/Producer` and their XMP equivalents (`dc:title`, `dc:subject`, `dc:creator`, `pdf:Producer`, `xmp:CreatorTool`).
- Each Info-key gets the same treatment: extract tokens, compare against the union of rendered-page content streams, fire tier-1 on currency-shaped tokens absent from rendered output.
- Extension only; registry tier and ZAHIR/BATIN do not change. Update registry description to enumerate the new keys.

**Tests (minimum 6).** One per Info-key plus a control.

---

## §7 Commit 7: HIGH 05 - `xlsx_defined_name_into_hidden_sheet` and `xlsx_doc_properties` extension

**Two-part commit.**

**Part A.** New analyzer `xlsx_defined_name_into_hidden_sheet`. Walks `xl/workbook.xml`'s `<definedNames>`, resolves each name's range to a sheet, fires tier-1 when the sheet has `state="hidden"` or `state="veryHidden"`.

**Part B.** Extend (or add) `xlsx_doc_properties` to flag dollar-amount-shaped tokens in `docProps/core.xml`'s `<dc:title>`, `<dc:subject>`, `<dc:description>` that don't appear in any visible cell of any visible sheet.

**Tests (minimum 6).** Three per part.

---

## §8 Commit 8: HIGH 06 - extend `svg_foreign_object`

**Spec.**
- Existing `svg_foreign_object` flags presence at tier-2. Extend to recursively flatten the `<foreignObject>` body's HTML into text and surface that text in the finding payload.
- Promote to tier-1 when the recovered text is non-empty AND contains a currency-shaped token not present in the SVG's `<text>` elements.
- Update registry description: "(now extracts foreignObject body to text)".

**Tests (minimum 5).** Including nested `<foreignObject>` containing `<svg>`, and a no-fire control where body matches visible text.

---

## §9 Commit 9: HIGH 09 - `png_iccp_desc_text_payload` and `image_text_metadata` tier raise

**Two-part commit.**

**Part A.** New analyzer `png_iccp_desc_text_payload`. Parses the iCCP profile (zlib-compressed); extracts `desc`, `cprt`, `dmnd` tag text. Fires tier-1 when any contains a currency-shaped token not present in the rendered image's OCR text (use existing OCR pathway).

**Part B.** Extend `image_text_metadata` (currently tier-3 on `tEXt` and `iTXt`) to fire at tier-2 when recovered text contains a currency-shaped token absent from rendered output. Tier-3 still applies for non-currency text.

**Tests (minimum 6).** Three per part.

---

## §10 Commit 10: HIGH 10 - `pdf_invisible_text_in_content_stream` and `embedded_file` extension

**Two-part commit.**

**Part A.** New analyzer `pdf_invisible_text_in_content_stream`. Tracks active opacity/alpha state through the content stream parser (`gs` operator with `/CA` and `/ca` graphics-state keys). Fires tier-1 when any `Tj` or `TJ` operator's effective rendered alpha is 0 AND the drawn text contains a currency-shaped token.

**Part B.** Extend `embedded_file` (currently flags presence) to extract currency-shaped tokens from `/F` and `/UF` filename strings and from the embedded file body if it is a text/plain or PDF. Surface as concealed substrate at tier-2 minimum.

**Tests (minimum 7).** Four for invisible-text (alpha-1.0 control, alpha-0.5 control, alpha-0 currency fires, alpha-0 non-currency does not), three for embedded-file extension.

After this commit, fixture 10 closes fully: §6 catches D and E; §2 catches C; §10A catches F; §10B catches G. The cross-layer meta-finding at the reconciliation layer is deferred to v1.2.5.

---

## §11 Commit 11: MEDIUM - tier-classification audit

**Spec.**
- New helper `bayyinah/domain/tier_promotion.py` exposing `currency_token_promotion(finding) -> Tier`.
- Sweep every analyzer that surfaces text-token findings: `image_text_metadata`, `pdf_off_page_text`, all analyzers added in this round, all existing `*_metadata_*` analyzers.
- For each, ensure that when the recovered text contains a currency-shaped token (regex set from §5) that does not appear in any rendered output, the finding fires at tier-2 minimum, regardless of the analyzer's default tier for non-currency findings.
- Apply the helper at each emission site, not as a post-filter.

**Tests (minimum 8).** One per analyzer that touches currency tokens, plus a unit test on the helper itself, plus a parametrised cross-analyzer test that asserts every analyzer's currency-token output reaches tier-2 minimum.

**Round 11 finding category retired (per v3 §17.3):** "currency tokens at tier-3 in image_text_metadata" -> mechanically prevented by the promotion helper applied at every emission site.

---

## §12 Commit 12: FRAMEWORK.md and RETIREMENT_LEDGER.md (Track 2)

**`FRAMEWORK.md` at repo root.**
- Title: "Bayyinah Audit Framework Conformance"
- §1 Pinned to Bayyinah Audit Framework v3.0 (cite Zenodo DOI; if not yet assigned, use placeholder `<DOI-TBA>` and flag in CHANGELOG release entry).
- §2 Project-specific deviations:
  - v4.1 ZAHIR/BATIN classification rule (single-walk surface-readability test, independent of analyzer module).
  - Per-version frozenset cadence in `tests/test_public_surface_additive.py` (every minor and patch gets its own constant; aliases allowed when surface unchanged).
  - Five-place pattern: CHANGELOG, README, fixture, pinning test, AND `bayyinah/mechanisms/registry.py`.
  - Em-dash discipline in user-facing prose (CHANGELOGs, READMEs, finding descriptions, landing copy; code comments exempt).
- §3 Maturity self-assessment: Bayyinah currently at Level 3 (Managed) per v3 §23.4. Round 11 closure plus the additions in this commit advance the project to Level 4 (Structurally Honest).
- §4 Pointers to QUESTIONS.md, per-version CHANGELOG retirement entries, and `RETIREMENT_LEDGER.md`.

**`RETIREMENT_LEDGER.md` at repo root.**
- Header: "Round-by-round failure-mode retirement ledger for Bayyinah Integrity Scanner".
- Per-round entries from Round 1 through Round 11. Each entry: round number, version retired in, finding shape, structural defense, gate or test that prevents recurrence.
- Round 11's entry covers the seven new analyzers plus the four extensions plus the tier audit.
- Reconstruct rounds 1 through 10 from CHANGELOG history. This is archaeology, not invention. Where the historical CHANGELOG does not name the round number, use `Round N (reconstructed from CHANGELOG)` and flag in the ledger preamble.

Em-dash check: zero in either document.

Commit message: `add FRAMEWORK.md and RETIREMENT_LEDGER.md (Round 11 §22 closure)`. Cite v3 §22 item 1 explicitly. Five-questions block stays.

---

## §13 Commit 13: v1.2.4 release

**Version bumps.**
- `pyproject.toml`: `version = "1.2.4"`
- `bayyinah/__init__.py`: `__version__ = "1.2.4"`

**Surface snapshot.** Add `V1_2_4_SURFACE` to `tests/test_public_surface_additive.py`. If new public names entered `__all__` (analyzer module entry points), enumerate them; otherwise alias to `V1_2_3_SURFACE`. Add the corresponding `test_v1_2_4_surface_is_subset_of_current` test.

**CHANGELOG entry (verbatim template; substitute `<placeholders>`).**

```
## [1.2.4] - <YYYY-MM-DD> - Round 11 audit closure (red-team CRITICAL findings)

Round 11 was an audit-of-self round. Bilal red-teamed bayyinah.dev v1.2.3
with a 10-fixture multi-layer-consensus-trap corpus on 2026-05-04. Four
fixtures silent-passed at integrity_score 1.000 / sahih (CRITICAL); five
partial-caught the substrate layer but missed the divergent payload (HIGH);
one tier-classification gap was identified across analyzers (MEDIUM). The
report and corpus are preserved at tests/redteam/round_11_gauntlet/.

### CRITICAL findings closed

- Fixture 01: AcroForm /V field-value override. New analyzer
  `pdf_acroform_field_value_payload` (commit <hash>).
- Fixture 02: ToUnicode CMap remap. New analyzer `pdf_tounicode_remap`
  (commit <hash>).
- Fixture 04: DOCX mc:AlternateContent Choice/Fallback divergence. New
  analyzer `docx_alternate_content_divergence` (commit <hash>).
- Fixture 07: EML multipart/alternative numeric divergence. New analyzer
  `eml_alternative_part_numeric_divergence` (commit <hash>).

### HIGH findings closed

- Fixture 03: PDF Title and Subject divergence. `pdf_metadata_analyzer`
  extended to symmetric Info-key sweep across Title, Subject, Author,
  Creator, Producer, plus XMP equivalents (commit <hash>).
- Fixture 05: XLSX defined-name into hidden sheet plus core.xml title.
  New analyzer `xlsx_defined_name_into_hidden_sheet` plus extension to
  `xlsx_doc_properties` (commit <hash>).
- Fixture 06: SVG foreignObject body not extracted. `svg_foreign_object`
  extended to flatten body to text and promote to tier-1 on currency
  tokens (commit <hash>).
- Fixture 09: PNG iCCP profile desc tag missed. New analyzer
  `png_iccp_desc_text_payload` plus tier raise on `image_text_metadata`
  (commit <hash>).
- Fixture 10: PDF six-layer consensus trap. New analyzer
  `pdf_invisible_text_in_content_stream` plus extension to `embedded_file`
  for /F and /UF filename token extraction (commit <hash>).

### MEDIUM finding closed

- Currency-token tier audit. New helper
  `bayyinah.domain.tier_promotion.currency_token_promotion` applied at
  every text-token emission site to enforce tier-2 minimum on currency
  tokens absent from rendered output (commit <hash>).

### Internal

- Test count: 1837 -> <N>.
- Mech registry: 113 -> 120 (7 new mechanisms; 4 existing extended).
- Public surface change: <enumerate new names, or "none, alias V1_2_4_SURFACE = V1_2_3_SURFACE">.
- Parity break: none.
- Round 11 retirement-ledger entry added to RETIREMENT_LEDGER.md.
- FRAMEWORK.md added; project advances from Level 3 (Managed) to Level 4
  (Structurally Honest) per Audit Framework v3.0 §23.4.

### Attribution discipline (v3 §18.10 corrective applied to Bayyinah)

Every round in the Bayyinah audit chain is and has been audit-of-self by
Bilal Syed Arfeen, per Audit Framework v3.0 §1.2 and §15. v1.2.3 commit
messages (d032553, e572091, 54942b0, 86c8351) attributed Round 10
findings to "Fraz round 10"; this was imprecise. Fraz Ashraf is
acknowledged for the engineering-approach contribution to the Audit
Framework itself (v3 §27) and is co-author on joint research papers
including Bayyinah al-Khabir, Cross-Text Computational Linguistics, and
Furqan; he is not an auditor on the Bayyinah chain. The historical
commit messages stand verbatim per the framework's record-preservation
discipline; this note corrects the framing going forward, in the same
shape as the furqan-lint v0.8.5 attribution corrective named in v3
§18.10.

### Five questions (release level)

1. Smallest input demonstrating the corrective release: a clean clone of
   v1.2.4, `pip install -e .[dev]`, then
   `pytest tests/redteam/round_11_gauntlet/` shows all 10 fixture-closure
   tests pass and pre-fix verdicts now invert.
2. Smallest input that would have shown each gap on v1.2.3: every fixture
   in tests/redteam/round_11_gauntlet/ has a `build_NN_*.py` builder and
   a corresponding `test_corpus_pre_fix_verdicts.py` parametrisation that
   passes against v1.2.3's silent-pass and partial-catch behaviour.
3. What this release does not do: it does not synthesise the cross-layer
   numeric-disagreement meta-finding (deferred to v1.2.5 per the depth-
   before-scope discipline; substrate completeness ships first, the
   reconciliation layer second). It does not extend ToUnicode detection
   beyond length inflation and codepoint substitution.
4. New code paths: 7 new analyzer modules, 4 extended analyzers, 1 tier-
   promotion helper, the Round 11 corpus, FRAMEWORK.md, and
   RETIREMENT_LEDGER.md. No new third-party dependencies.
5. Limitations retired: closes Round 11 (4 CRITICAL, 5 HIGH, 1 MEDIUM).
   Per v3 §15.1, surfacing CRITICAL severity in audit-of-self despite
   ten prior rounds with declining severity slope is empirical evidence
   that novel attack classes can re-introduce CRITICAL severity, and
   that the validator-by-different-instance protocol applied to deployed
   substrate (bayyinah.dev v1.2.3) catches what producer-side review
   missed.
```

Em-dash check on CHANGELOG entry: 0. Replace any em-dash with hyphen or restructure.

**Release commit message.**
```
release v1.2.4 (Round 11 audit closure)

Closes 4 CRITICAL silent-pass findings, 5 HIGH partial-catch findings,
and 1 MEDIUM tier-classification finding surfaced by Bilal's red-team
probe of bayyinah.dev v1.2.3 on 2026-05-04. See CHANGELOG.md for the
per-finding closure rationale, the v3 round-N report, and the release-
level five-questions block.

Test count: 1837 -> <N>. Mech registry: 113 -> 120. No public surface
removals. No parity break. No new third-party dependencies.

Project advances from Level 3 (Managed) to Level 4 (Structurally
Honest) per Audit Framework v3.0 §23.4.

Co-authored-by: Claude (cowork) <claude+cowork@anthropic.com>
```

---

## §14 Verification block (run all eight; capture verbatim output)

```bash
cd /tmp/bay
git log --oneline -14   # expect 13 commits + v1.2.3 release at the bottom
grep -n "1.2.4" pyproject.toml bayyinah/__init__.py
diff <(grep -E "^[a-zA-Z]" requirements-dev.txt | sort) \
     <(python3 -c "import tomllib; print('\n'.join(sorted(tomllib.load(open('pyproject.toml','rb'))['project']['optional-dependencies']['dev'])))")
pytest tests/redteam/round_11_gauntlet/ -v --tb=line -p no:cacheprovider
pytest tests/test_public_surface_additive.py -v --tb=line -p no:cacheprovider   # expect 6 passed
pytest -q --tb=line -p no:cacheprovider   # expect <N> = 1870 to 1890 passed
python3 -c "from bayyinah.mechanisms.registry import REGISTRY; print(len(REGISTRY))"   # expect 120
for f in $(git diff --name-only 86c8351..HEAD | grep -E '\.(md|txt|py)$'); do
  c=$(grep -c "—" "$f" 2>/dev/null || echo 0)
  [ "$c" != "0" ] && echo "EM-DASH: $c in $f"
done   # expect zero output on user-facing prose files
```

---

## §15 Patch bundle and handoff

```bash
git format-patch -13 --stdout HEAD > "/Users/bilalsfolder/Documents/Claude/Projects/Bayyinah/v1.2.4_round_11.patch"
```

Handoff format (write into the chat at end):
- 13 commit hashes in order (1 corpus seed, 4 CRITICAL closures, 5 HIGH closures, 1 MEDIUM tier audit, 1 framework conformance, 1 release).
- Verbatim verification output from §14.
- Actual post-fix test count <N>.
- Actual mech registry count.
- Em-dash sweep result.
- One-line deviation block: any place this prompt's spec was extended or contracted, with reason. If none, state "no deviations from v1_2_4_round_11_prompt.md revision <K>".

---

## §16 Post-deploy probe (after Bilal pushes and Railway redeploys)

Add `benchmarks/verify_v1_2_4_deploy.py` as a sibling to `verify_v1_1_4_deploy.py`. The v1.2.4 probe:
1. GET /version: must return `{"version": "1.2.4"}`.
2. GET /healthz: must return `{"status": "ok"}`.
3. POST each Round 11 fixture to /scan; assert the post-fix verdict from `EXPECTED.json`. Exit 0 only if all 10 fixtures return their post-fix expected verdicts.

---

## §17 What this prompt does not authorise

Stop and request a prompt revision rather than extending scope into any of the following:
- Cross-layer numeric-disagreement meta-mechanism (v1.2.5 work).
- GitHub Action packaging of framework gates (post-deadline commercial track).
- ToUnicode v2 (any additional CMap heuristics beyond length inflation and codepoint substitution).
- Format expansion (no new top-level formats; existing format coverage is what closes Round 11).
- Public surface removals or parity breaks.
- Any rewrite of existing analyzers beyond the four extensions explicitly listed (§6, §7B, §8, §10B).

---

## §18 Validator-by-different-instance protocol (v3 §5.2)

After the patch bundle lands in `/Users/bilalsfolder/Documents/Claude/Projects/Bayyinah/`, Bilal applies it on a fresh clone via `git am`, then runs the §14 verification block on a fresh Claude instance with no access to this prompt. The fresh instance audits the patch against `tests/redteam/round_11_gauntlet/REDTEAM_v1_2_3_REPORT.md` alone. Differences between the producer's account and the validator's re-derivation are Round 11.5 findings to land in v1.2.4.1 if any.

This is the load-bearing structural defense against confirmation bias under audit-of-self (v3 §15.1).

---

End of locked prompt. Revision 2 (attribution corrective applied 2026-05-04).

---

# Bismillah ir-Rahman ir-Rahim
