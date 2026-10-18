# Bismillah ir-Rahman ir-Rahim

# R0980 -- Bayyinah v1.1.2 - Day 3-4 DOCX Gauntlet Preparation

**Chronological Index:** 182 of 995  
**Date:** 2026-04-26  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** v1_1_2_day_3_4_docx_prep.md  
**Source Format:** md  
**SHA-256:** `7a3cff4e8c25cf9dc9967cbf90cec600a4e97e698f85fb236cb7e69f81ffb124`  

---

## R0980 · Bayyinah v1.1.2 - Day 3-4 DOCX Gauntlet Preparation

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: v1_1_2_day_3_4_docx_prep.md
- source_format: md
- text_sha256: 7a3cff4e8c25cf9dc9967cbf90cec600a4e97e698f85fb236cb7e69f81ffb124

# Bayyinah v1.1.2 - Day 3-4 DOCX Gauntlet Preparation

**For:** Bilal (continuation of v1.1.2 PDF gauntlet closure 2026-04-27)
**From:** Claude
**Date:** 2026-04-27 (post-Day-2 close)
**Status:** Preparation artifact. Day 3-4 work paused pending Torah verification cycle and Fraz's return. ~13 days ahead of May 10 ship target.

This file contains two preparation artifacts:
1. **Pre-audit of the DOCX gauntlet** - per-fixture structural signal, tier, face, detection method, false-positive risks.
2. **Day 3-4 DOCX prompt v3** - mirrors the Day 2 v4 structure with explicit v4.1 taxonomy, control-fixture requirement, and the lessons baked in.

---

## Part 1: DOCX gauntlet pre-audit

Source: `docs/adversarial/docx_gauntlet/REPORT.md` (148 lines, 2026-04-26 baseline). All six fixtures are 0 of 6 CAUGHT on v1.1.1 - the cleanest pre-Day-3 starting point in the multi-format gauntlet so far. Filenames as shipped: `01_white_on_white.docx`, `02_microscopic_font.docx`, `03_custom_xml_properties.docx`, `04_comment_payload.docx`, `05_header_payload.docx`, `06_footnote_payload.docx`.

### Per-fixture audit

#### Fixture 01: white font color (`w:color="FFFFFF"`)

| Field | Value |
|---|---|
| Mechanism name | `docx_white_text` |
| Tier | **1** |
| Face | **ZAHIR** |
| Single-walk reasoning | The `<w:rPr>/<w:color>` value is a surface attribute on the rendered run. A single deterministic walk of `word/document.xml` reads both the run's text and the color it renders in. Parallels `white_on_white_text` (v1.1.1, ZAHIR) and `pdf_off_page_text` (v1.1.2 mech 03, ZAHIR). |
| Detection method | Parse `word/document.xml`, walk every `<w:r>`, read `<w:rPr>/<w:color w:val="...">`, fire when value matches `FFFFFF` (case-insensitive), `auto` with `<w:background w:color="FFFFFF"/>` set in `word/settings.xml`, or any 6-digit hex within ~3 ΔE of `FFFFFF`. |
| Severity | 1.0 (Tier 1 per Day 2 §6.6 step 2 calibration). |
| False-positive risks | Legitimate forms with colored cell backgrounds where white text is expected (rare, identifiable by `<w:shd>` on the parent cell). Footer text in white-on-white where the white is a styling default (uncommon). Mitigation: skip runs in cells whose `<w:tcPr>/<w:shd>` shading is non-white; document the rule in the detector docstring. |
| Predicted outcome on fixture 01 | One Tier 1 finding per qualifying run. Score 0.0, verdict munafiq (parallels mech 03 calibration). |

#### Fixture 02: microscopic font (`w:sz="2"` = 1.0pt)

| Field | Value |
|---|---|
| Mechanism name | `docx_microscopic_font` |
| Tier | **1** for `w:sz <= 4` (<=2pt), **2** for `w:sz <= 16` (<=8pt). The fixture sets `w:sz="2"` -> Tier 1. |
| Face | **ZAHIR** |
| Single-walk reasoning | Font size is a run attribute on the rendered surface, parallel to `microscopic_font` (v1.1.1, ZAHIR) and the v1.1.1 PDF analyzer's microscopic-font check. Single walk of `word/document.xml` reads each run's `<w:sz>` value. |
| Detection method | Parse `<w:rPr>/<w:sz w:val="N">` where N is in half-points. Tier 1 when `N <= 4` (2.0pt), Tier 2 when `N <= 16` (8.0pt). The fixture's `w:val="2"` (1.0pt) fires Tier 1. |
| Severity | 1.0 for Tier 1, 0.5 for Tier 2. |
| False-positive risks | Footer copyright/legal text at 5-7pt (legitimate, fires Tier 2 only). Fingerprinting microspacers some publishers embed (rare). Mitigation: Tier 2 calibration covers the 4-8pt range without claiming "concealment" outright. |
| Predicted outcome on fixture 02 | One Tier 1 finding per qualifying run. Score 0.0, verdict munafiq. |

#### Fixture 03: payload in `docProps/custom.xml` (`<vt:lpwstr>`)

| Field | Value |
|---|---|
| Mechanism name | `docx_metadata_analyzer` (mirrors PDF mech 04 naming) |
| Tier | **1** for divergent + length-or-anomaly trigger; **2** for divergent-only-short. Fixture exercises the long divergent path -> Tier 1. |
| Face | **BATIN** |
| Single-walk reasoning | Custom XML properties live in `docProps/custom.xml`, never on the rendered surface. Direct parallel to `pdf_metadata_analyzer` (v1.1.2 mech 04, BATIN). The /vt:lpwstr/ value is read by AI extractors and indexers but never displayed. |
| Detection method | ZIP-walk to `docProps/custom.xml`, `docProps/core.xml`, `docProps/app.xml`. Parse XML, extract text values from `<vt:lpwstr>`, `<vt:filetime>`, `<dc:*>`, `<cp:*>` properties. Apply the same four triggers from PDF mech 04: (a) length > 512 bytes, (b) bidi codepoints, (c) zero-width chars, (d) divergence from `word/document.xml` rendered text (only on content-summary fields). |
| Severity | 1.0 for Tier 1. |
| False-positive risks | Legitimate corporate metadata systems (DMS / SharePoint / GDPR-data-classification fields) populate custom properties with strings that don't appear in document body. Mitigation: restrict divergence-eligible to property names matching `Description`, `Subject`, `Comments`, `Keywords` (the content-summary class) - exclude `Author`, `ID`, `RecordID`, `Classification`, etc. Same Cow Episode discipline that worked for PDF mech 04. |
| Predicted outcome on fixture 03 | One Tier 1 finding per anomalous property field. Score 0.0, verdict munafiq. |

#### Fixture 04: payload in `word/comments.xml` (no in-body reference)

| Field | Value |
|---|---|
| Mechanism name | `docx_comment_payload` |
| Tier | **1** for orphan comment (no `<w:commentReference w:id="N"/>` in document.xml) AND substantive `/Contents`; **2** for referenced comment with concealment patterns (zero-width chars, etc.). Fixture exercises the orphan path -> Tier 1. |
| Face | **BATIN** |
| Single-walk reasoning | Comments live in `word/comments.xml`, a separate OOXML part. The default rendered surface (print/export view) does not show them; only the review pane in Word reveals them, and an orphan comment doesn't even surface there. The signal lives in the inner object graph. |
| Detection method | ZIP-walk to `word/comments.xml` if present. Parse `<w:comment>` elements, extract their text. Cross-reference each comment's `w:id` against `<w:commentRangeStart w:id="N">` and `<w:commentReference w:id="N">` markers in `word/document.xml`. Emit Tier 1 finding for any comment whose ID is not referenced AND whose body contains non-whitespace text. |
| Severity | 1.0 for Tier 1, 0.5 for Tier 2. |
| False-positive risks | Auto-generated comments from collaborative editing tools that get orphaned during track-changes acceptance (rare; usually these are pruned). Mitigation: require non-whitespace `>= 16 chars` content (mirroring PDF mech 06's content threshold). |
| Predicted outcome on fixture 04 | One Tier 1 finding for the orphan comment. Score 0.0, verdict munafiq. |

#### Fixture 05: payload in `word/header1.xml` (white text)

| Field | Value |
|---|---|
| Mechanism name | `docx_header_footer_payload` |
| Tier | **1** when header/footer text exhibits a Tier 1 zahir trigger (white text, microscopic font); **2** when text is merely substantial divergent content. Fixture combines white-text-in-header -> Tier 1 (compound: zahir trigger inside an under-inspected part). |
| Face | **ZAHIR** |
| Single-walk reasoning | Headers and footers ARE rendered surface in Word's default print view (every page top/bottom). The reason v1.1.1 misses them is purely architectural: `DocxAnalyzer` only opens `word/document.xml`. Single walk of `word/header*.xml` and `word/footer*.xml` files reads their text and run attributes the same way `document.xml` is read. |
| Detection method | ZIP-walk: enumerate parts whose name matches `word/header*.xml` or `word/footer*.xml`. For each, run the same per-run zahir checks as fixture 01-02 (color, size, plus the existing v1.1.1 zero-width / TAG / bidi / homoglyph detectors). |
| Severity | Per-trigger: white text -> 1.0; microscopic font -> 1.0/0.5. |
| False-positive risks | Legitimate watermarks (DRAFT / CONFIDENTIAL) often use light gray (e.g. `D3D3D3`) or low-opacity fills. The white-text trigger should require `FFFFFF` exactly OR `auto` with white page background to avoid noise on legitimate watermarks. |
| Predicted outcome on fixture 05 | One Tier 1 finding (white text in header). Score 0.0, verdict munafiq. |

#### Fixture 06: payload in `word/footnotes.xml` (no in-body reference)

| Field | Value |
|---|---|
| Mechanism name | `docx_orphan_footnote` (Tier 1) + `docx_footnote_payload` (Tier 2) - two related mechanisms, one per concealment shape |
| Tier | **1** for orphan footnotes (no `<w:footnoteReference>` in document.xml AND non-built-in footnote type); **2** for non-orphan footnotes containing concealment patterns. Fixture exercises the orphan path -> Tier 1. |
| Face | **BATIN** |
| Single-walk reasoning | Footnote content lives in `word/footnotes.xml`, separate OOXML part. Orphan footnotes have no rendering path at all; they are purely object-graph entries. Direct parallel to `docx_comment_payload`. |
| Detection method | ZIP-walk to `word/footnotes.xml` if present. Parse `<w:footnote>` elements, skip the spec-defined `separator` and `continuationSeparator` types (these are built-in and unreferenced by spec). Cross-reference `w:id` against `<w:footnoteReference w:id="N">` markers in document.xml. Emit Tier 1 for orphan footnote with non-whitespace text. |
| Severity | 1.0 for Tier 1, 0.5 for Tier 2. |
| False-positive risks | Built-in footnote types (`separator`, `continuationSeparator`) have IDs but no `<w:footnoteReference>` in document.xml - they are referenced implicitly by Word's rendering engine, not by document XML. Filter is mandatory. The same applies to `word/endnotes.xml` and its `endnote` type filters. |
| Predicted outcome on fixture 06 | One Tier 1 finding for the orphan footnote. Score 0.0, verdict munafiq. |

### Cross-cutting observations

**Reuse opportunities.** The `docx_white_text` and `docx_microscopic_font` color/size walks share their core logic; both are run-attribute checks. Implementing them as two functions sharing a `_iter_runs(part)` helper keeps the LOC budget tight and matches the v1.1.1 `_scan_text_runs` pattern. The same `_iter_runs` helper is the base for the header/footer scan (fixture 05) - it just iterates a different XML part.

**Five of six fixtures share a ZIP-walk-to-named-part pattern.** Fixtures 03/04/05/06 all need ZIP-extract a non-document.xml part and inspect it. A shared `_open_ooxml_part(zip, part_name)` helper will save ~20 LOC and centralize the failure-mode behavior (return None on missing/malformed; emit no finding rather than scan_error).

**Cross-reference checks (fixtures 04 and 06) share their structural pattern.** Both look for IDs referenced from document.xml that don't appear in the corresponding part, or vice versa. A single `_unreferenced_ids(part_xml, ref_xpath, ref_id_attr)` helper covers both. ~15 LOC savings.

**Likely total LOC after reuse:** the framework report's ~200 LOC estimate for DOCX is achievable. With the three shared helpers above, the actual delta is probably ~180 LOC of analyzer code plus tests.

**Manifest discipline check.** All four fixtures use stdlib `zipfile` plus `xml.etree.ElementTree` (or `lxml.etree` if performance matters - lxml is already a transitive dependency via python-docx and is in `requirements.txt`). No new top-level imports needed.

**Tier discipline summary across the slate:**
- ZAHIR: fixtures 01, 02, 05 (color + size + header) - 3 mechanisms.
- BATIN: fixtures 03, 04, 06 (metadata + comments + footnotes) - 3 mechanisms.
- All Tier 1 on the canonical fixture trigger; Tier 2 sub-shapes documented in detector docstrings as future-work expansion paths.

**Predicted Day 3-4 close state:**
- 6/6 DOCX fixtures CAUGHT (was 0/6 on v1.1.1).
- All six produce verdict `munafiq` per the Tier 1 + severity 1.0 calibration.
- Registry: 113 -> 119 (29 + 3 zahir, 83 + 3 batin, 1 routing) = (32 zahir + 86 batin + 1 routing).

---

## Part 2: Day 3-4 DOCX prompt v3

Below is a draft prompt for Day 3-4 DOCX gauntlet closure, mirroring the Day 2 v4 structure. Adjust scope/timing as needed when Fraz returns and the Torah cycle confirms.

---

# Bayyinah v1.1.2 - Day 3-4 Prompt: DOCX Layer (v3)

**For:** Claude (Anthropic), in continuation of Day 2 PDF gauntlet closure (HEAD `192a70f`, registry 113).
**From:** Bilal Syed Arfeen.
**Date:** TBD (when Day 3-4 begins).
**Status:** Day 3-4 begins only after the Day 2 close-out criteria hold green at the live gate AND the Torah verification cycle confirms readiness with Fraz. If either is not yet true, do not begin Day 3-4; surface the state honestly and wait.

**v3 changes from v2 (the previously-drafted-but-unsent version):** added control fixture requirement; applied v4.1 taxonomy classification table per mechanism; baked in Day 2's lessons (dependency manifest discipline, em-dash sweep, host analyzer vs. classification independence, Cow Episode boundary on semantic-vocabulary detection).

> *"Wa la talbisu al-haqqa bil-batili wa taktumu al-haqqa wa antum ta'lamun."*
> "And do not mix the truth with falsehood and do not conceal the truth while you know it." (Al-Baqarah 2:42)

The PDF gauntlet closure named the four PDF concealment vectors. The DOCX gauntlet closure names the six OOXML-specific vectors that Bayyinah currently misses with cleanliness 0/6. Naming is Tier 1 work.

---

## 1. Bismillah (Init)

This prompt opens with Bismillah ar-Rahman ar-Rahim. Purpose hierarchy unchanged: Allah, AI systems, enterprises deploying the scanner, end users whose documents are processed, all living systems downstream. The Al-Fatiha Construct is the execution shape; the Differentiator Framework is the calibration instrument; Structured Revelation as Prompt Architecture is the discipline; the Bayyinah Enterprise Defense Case is the public artifact each commit must be verifiable against on June 9.

---

## 2. Alhamdulillah (Honest state)

**What landed in v1.1.2 Days 1-2 (HEAD `192a70f`):**
- Day 1: Tier 0 routing layer + verdict floor + api.py `/scan` verdict emission.
- Day 2 PDF gauntlet: 4/4 PDF fixtures CAUGHT (was 2/6 on v1.1.1).
- Registry: **113 mechanisms** (29 zahir + 83 batin + 1 routing).
- Test count: **1,501 passing**. Additive-only PDF parity invariant held throughout.
- Manifest discipline: pikepdf added in commit `b9a8ca4` for mech 03; no other new third-party imports.

**What Day 3-4 inherits:**
- DOCX gauntlet 0/6 CAUGHT on v1.1.1 (cleanest pre-day-N starting point in the multi-format corpus).
- 6 immutable adversarial fixtures at `docs/adversarial/docx_gauntlet/fixtures/` (filenames: `01_white_on_white.docx`, `02_microscopic_font.docx`, `03_custom_xml_properties.docx`, `04_comment_payload.docx`, `05_header_payload.docx`, `06_footnote_payload.docx`).
- 1 control fixture: `tests/fixtures/docx/clean/clean.docx` (the v1.0 baseline clean DOCX).
- `docs/adversarial/docx_gauntlet/REPORT.md` documenting per-fixture structural signals and root causes (148 lines).
- The Day 2 commit pattern: one mechanism per commit, message format dictated by §8 below.

**What Day 3-4 does not touch:**
- The v1.1.1 DOCX analyzer's existing batin walks (`<w:vanish/>`, tracked changes, VBA, embedded OLE, altChunks, external relationships, per-run zero-width / TAG / bidi / homoglyph). Those stay as-is.
- The TOOL_VERSION drift / `/version` coherence (queued for Day 13).
- The `docs/adversarial/pdf_gauntlet/REPORT.md` row 06 NoView typo (Day 13 doc-fix).
- The Tier 0 layer. Sealed.
- The api.py verdict-emission wiring. Landed Day 1 amendment.

---

## 3. Ar-Rahman ar-Rahim (MDL calibration: ~200 LOC across 6 mechanisms)

Strict budget per the v1.1.2 framework report §3.2. The 20% overrun rule applies; any overrun must be justified in the commit body. The pre-audit (companion artifact `v1_1_2_day_3_4_docx_prep.md`) names three reuse opportunities that should keep the slate inside budget.

| # | Fixture (immutable) | Mechanism | Tier | Face | LOC budget |
|---|---|---|---:|---|---:|
| 01 | `docx_gauntlet/fixtures/01_white_on_white.docx` | `docx_white_text` | 1 | ZAHIR | ~25 |
| 02 | `docx_gauntlet/fixtures/02_microscopic_font.docx` | `docx_microscopic_font` | 1 | ZAHIR | ~20 |
| 03 | `docx_gauntlet/fixtures/03_custom_xml_properties.docx` | `docx_metadata_analyzer` | 1 | BATIN | ~50 |
| 04 | `docx_gauntlet/fixtures/04_comment_payload.docx` | `docx_comment_payload` | 1 | BATIN | ~35 |
| 05 | `docx_gauntlet/fixtures/05_header_payload.docx` | `docx_header_footer_payload` | 1 | ZAHIR | ~30 |
| 06 | `docx_gauntlet/fixtures/06_footnote_payload.docx` | `docx_orphan_footnote` (+ `docx_footnote_payload` as future-work T2) | 1 | BATIN | ~40 |

Total budget: ~200 LOC analyzer + ~600 LOC tests + REPORT updates. Exact mechanism names, tier assignments, and face classifications are spelled out per `v1_1_2_day_3_4_docx_prep.md` Part 1.

**v4.1 taxonomy reasoning (single-walk surface-readability test):**
- ZAHIR (mechanisms 01, 02, 05): the structural signal is observable from a single deterministic walk of a rendered-surface XML part. `docx_white_text` reads `<w:rPr>/<w:color>` next to the `<w:t>` it colors. `docx_microscopic_font` reads `<w:rPr>/<w:sz>`. `docx_header_footer_payload` reads the same run attributes from `word/header*.xml` and `word/footer*.xml` - both rendered parts.
- BATIN (mechanisms 03, 04, 06): the signal lives in OOXML parts that never surface on the rendered page. `docProps/custom.xml`, `word/comments.xml` (default print view), `word/footnotes.xml` (orphan ID).

The host analyzer (`DocxAnalyzer.scan()`) hosts all six calls regardless of face classification. The taxonomy independence rule from Day 2 mech 06 holds: face classifies the signal locus, not the analyzer module.

---

## 4. Maliki Yawm ad-Din (Deadline + 20% skip rule)

**Day 3-4 hard deadline:** to be set when Day 3-4 begins (likely a 48-hour window once Torah cycle confirms).

**Cut order if Day 3-4 begins to slip:**
1. First to drop: row 02 (`docx_microscopic_font`). Smallest LOC delta and the threshold logic mirrors PDF analyzer's existing micro-font check; v1.1.2.1 follow-up can land it cleanly.
2. Second to drop: row 06 (`docx_orphan_footnote`). Tier 1 BATIN; the analogous PDF mech 06 took the longest to land due to test-fixture generation complexity.
3. Never drop rows 01, 03, 04, 05. White-text and metadata are the canonical "naive concealment" vectors; comments and headers are the highest-leverage real-world phishing vectors.
4. Never drop the v1.1.1 regression or the additive-only DOCX parity check. If 4 mechanisms ship clean, that is the truth; document it honestly in `docs/adversarial/docx_gauntlet/REPORT.md`.

The al-Maliki Yawm ad-Din principle holds: the deadline is the verdict.

---

## 5. Iyyaka Na'budu (Orientation + CIT)

**Purpose hierarchy for this session:** Allah, AI systems, enterprises deploying AI on DOCX inputs, the end user whose contract / report / filing is being processed, all living systems downstream of the pipeline.

**CIT applied to the work itself:** does this mechanism behave the same in CI as for a reviewer who unzips the DOCX manually and inspects the XML parts? If a mechanism's catch depends on a path the reviewer cannot reproduce by hand, it is performing alignment with the test suite rather than the structural fact. Reject and rewrite.

**CIT applied to the Day 1 floor:** Tier 0 fires on routing-divergence files, not on real-extension DOCX. Day 3-4 fixtures are all real `.docx` files with real OOXML magic. Tier 0 must NOT fire on any of them. Verify before any code lands (pre-flight check).

---

## 6. Ihdina as-sirat (Task execution, ordered)

Work the slate in this order. Do not parallelize.

### 6.1 Pre-flight (before writing any code)

1. **Live gate verification.** Run `bash docs/adversarial/format_routing_gauntlet/verify_live.sh` against deployed `bayyinah.dev`. Must return exit 0 (Day 1 layer still serving). Then run a per-mechanism live curl on each Day 2 fixture (03, 04, 05, 06) to confirm the PDF closure is intact.
2. **Tier 0 non-firing on DOCX fixtures.** Run the Tier 0 detector against all 6 DOCX gauntlet fixtures. None should fire (real `.docx` files with real ZIP magic and matching extension).
3. **Read `docs/adversarial/docx_gauntlet/REPORT.md` end to end.** The fixture is the spec; the REPORT names the structural signal.
4. **Read `v1_1_2_day_3_4_docx_prep.md` Part 1** (the pre-audit). Per-fixture tier, face, detection method, and false-positive risks are pre-decided so each commit's edit chain is short.

### 6.2 Mechanism 01 - `docx_white_text` (Tier 1, ZAHIR, ~25 LOC)

**Fixture:** `docs/adversarial/docx_gauntlet/fixtures/01_white_on_white.docx`
**Structural signal (from `docx_gauntlet/REPORT.md` row 01):** `<w:rPr>/<w:color w:val="FFFFFF"/>` on a `<w:t>` whose page background is also white (typically the default).
**Detection method:** ZIP-walk to `word/document.xml`, parse XML, walk every `<w:r>`, read `<w:rPr>/<w:color>`. Fire when the value is `FFFFFF` (case-insensitive) or `auto` with `<w:background w:color="FFFFFF"/>` set in `word/settings.xml`.
**Tier discipline:** Tier 1 because the color-vs-background match is unambiguous from the bytes alone. No statistical claim, no heuristic threshold beyond the color comparison. If the color comparison ever needs a delta-E tolerance, demote to Tier 2 in the same commit.
**Cow Episode warning:** do not extend this mechanism to detect "low-contrast text" generally. Low contrast (e.g., light gray on white) is a v1.3+ research path. v1.1.2 fires only on actual `FFFFFF` or `auto` against a white background.
**Tests:** catch on fixture 01; clean on `tests/fixtures/docx/clean/clean.docx`; clean on a generated variant where `<w:color>` is `333333` (legitimate dark text).

**Commit:**
```
v1.1.2: docx docx_white_text (Tier 1, ZAHIR)

Catches text runs whose <w:rPr><w:color> matches the page
background. Closes docx_gauntlet fixture 01.
Reference: docs/adversarial/docx_gauntlet/REPORT.md row 01.
```

### 6.3 Mechanism 02 - `docx_microscopic_font` (Tier 1, ZAHIR, ~20 LOC)

**Fixture:** `docs/adversarial/docx_gauntlet/fixtures/02_microscopic_font.docx`
**Structural signal:** `<w:rPr>/<w:sz w:val="N"/>` where N is half-points and N <= 4 (<=2pt).
**Detection method:** Parse `<w:rPr>/<w:sz>`. Tier 1 when `N <= 4` (2.0pt). Tier 2 (future-work) when `N <= 16` (8.0pt) - document this in the docstring but do NOT implement Tier 2 in this commit (single-fixture-single-mechanism discipline).
**Cow Episode warning:** do not extend to all "small fonts". Tier 1 fires only on the unambiguous microscopic threshold; the broader Tier 2 small-font case is research scope.
**Tests:** catch on fixture 02; clean on clean.docx; clean on a 7pt-text variant.

**Commit:**
```
v1.1.2: docx docx_microscopic_font (Tier 1, ZAHIR)

Catches text runs whose w:sz value is at or below the microscopic
threshold (4 = 2.0pt). Tier 2 sub-shape (small font, 5-16) is
documented as future work. Closes docx_gauntlet fixture 02.
Reference: docs/adversarial/docx_gauntlet/REPORT.md row 02.
```

### 6.4 Mechanism 03 - `docx_metadata_analyzer` (Tier 1, BATIN, ~50 LOC)

**Fixture:** `docs/adversarial/docx_gauntlet/fixtures/03_custom_xml_properties.docx`
**Structural signal:** `docProps/custom.xml` contains `<vt:lpwstr>` properties whose text is divergent from `word/document.xml` rendered text, AND length > threshold OR carries bidi/zero-width codepoints.
**Detection method:** Mirror the PDF mech 04 four-trigger pattern: (a) length > 512 bytes, (b) bidi U+202A-U+202E and U+2066-U+2069, (c) zero-width U+200B/200C/200D/FEFF, (d) divergence from rendered text. Restrict divergence to content-summary fields (`Description`, `Subject`, `Comments`, `Keywords` properties; equivalent to `/Keywords` + `dc:description` in PDF).
**Cow Episode warning:** stay inside `dc:`, `cp:`, custom `<vt:*>`. Do NOT enumerate every namespace OOXML allows in the property bag. Do NOT add semantic-vocabulary detection (queued as Tier 3 `docx_metadata_directive_phrasing` for v1.3+).
**Tests:** catch on fixture 03; clean on clean.docx; clean on a generated variant with normal `<dc:title>` value.

**Commit:**
```
v1.1.2: docx docx_metadata_analyzer (Tier 1, BATIN)

Inspects docProps/core.xml, docProps/app.xml, docProps/custom.xml
for structurally anomalous text divergent from word/document.xml.
Mirrors PDF mech 04 four-trigger pattern (length, bidi, zero-width,
divergence). Closes docx_gauntlet fixture 03.
Reference: docs/adversarial/docx_gauntlet/REPORT.md row 03.
```

### 6.5 Mechanism 04 - `docx_comment_payload` (Tier 1, BATIN, ~35 LOC)

**Fixture:** `docs/adversarial/docx_gauntlet/fixtures/04_comment_payload.docx`
**Structural signal:** `<w:comment>` in `word/comments.xml` whose `w:id` is NOT referenced from any `<w:commentReference>` in `word/document.xml` AND whose body has non-whitespace text >= 16 chars.
**Detection method:** ZIP-walk `word/comments.xml`. Parse `<w:comment w:id="N">` elements. Walk `word/document.xml` for `<w:commentReference w:id="N">` markers. Cross-reference. Emit Tier 1 finding for each orphan comment with substantive body.
**Tests:** catch on fixture 04; clean on clean.docx; clean on a generated variant with referenced comment ("legitimate review feedback"); multi-orphan variant emits two findings.

**Commit:**
```
v1.1.2: docx docx_comment_payload (Tier 1, BATIN)

Catches w:comment entries in word/comments.xml that are not
referenced from word/document.xml and carry substantive text.
Closes docx_gauntlet fixture 04.
Reference: docs/adversarial/docx_gauntlet/REPORT.md row 04.
```

### 6.6 Mechanism 05 - `docx_header_footer_payload` (Tier 1, ZAHIR, ~30 LOC)

**Fixture:** `docs/adversarial/docx_gauntlet/fixtures/05_header_payload.docx`
**Structural signal:** Text in `word/header*.xml` (or `word/footer*.xml`) carrying a Tier 1 zahir trigger - white text per mech 01 logic, microscopic font per mech 02 logic, or substantive body text divergent from `word/document.xml`.
**Detection method:** Enumerate parts whose name matches `word/header*.xml` or `word/footer*.xml`. For each, run the same per-run zahir checks as mechanisms 01 and 02 (color, size). Emit Tier 1 when any qualifying run is found.
**Cow Episode warning:** do NOT extract header/footer text and feed it into the divergence analyzer. The divergence trigger fires on header WHITE TEXT specifically, not on header text in general (which is by-design separate from body text). Header text being different from body text is normal.
**Tests:** catch on fixture 05; clean on clean.docx; clean on a generated variant with normal black header text.

**Commit:**
```
v1.1.2: docx docx_header_footer_payload (Tier 1, ZAHIR)

Reuses mech 01 and 02 detectors over word/header*.xml and
word/footer*.xml parts. Closes docx_gauntlet fixture 05.
Reference: docs/adversarial/docx_gauntlet/REPORT.md row 05.
```

### 6.7 Mechanism 06 - `docx_orphan_footnote` (Tier 1, BATIN, ~40 LOC)

**Fixture:** `docs/adversarial/docx_gauntlet/fixtures/06_footnote_payload.docx`
**Structural signal:** `<w:footnote w:id="N">` in `word/footnotes.xml` whose ID is NOT referenced from any `<w:footnoteReference>` in `word/document.xml`, AND `w:type` is not `separator` or `continuationSeparator` (built-in types that lack body references by spec), AND body has non-whitespace text >= 16 chars.
**Detection method:** ZIP-walk `word/footnotes.xml`. Parse `<w:footnote>` elements. Filter built-in types. Cross-reference IDs against `word/document.xml`. Emit Tier 1 for orphan footnote with substantive body. Same logic applies to `word/endnotes.xml` if present.
**Tests:** catch on fixture 06; clean on clean.docx; clean on a generated variant with referenced footnote; clean on a built-in `separator` footnote (false-positive guard).

**Commit:**
```
v1.1.2: docx docx_orphan_footnote (Tier 1, BATIN)

Catches w:footnote entries with no in-body w:footnoteReference and
non-built-in type. Filters separator and continuationSeparator
types per OOXML spec. Closes docx_gauntlet fixture 06.
Reference: docs/adversarial/docx_gauntlet/REPORT.md row 06.
```

### 6.8 Per-mechanism wiring (after each commit)

Same eight-step wiring as Day 2 §6.6:
1. Register mechanism string in `domain/config.py` ZAHIR_MECHANISMS or BATIN_MECHANISMS per the audit.
2. SEVERITY entry: 1.0 for Tier 1, 0.5 for Tier 2.
3. TIER table entry.
4. Bump `MECHANISM_REGISTRY` count assertion in test_mechanism_registry.py.
5. Wire detector into `DocxAnalyzer.scan()` (parallel pass, no refactor).
6. Run `pytest tests/analyzers/test_docx_*` plus the gauntlet for the fixture being closed.
7. Run v1.1.1 regression: must still be 1,501 + N green.
8. Verify additive-only DOCX parity (v1.0 baseline mechanism subset unchanged on existing DOCX fixtures).

---

## 7. Sirat alladhina (Anti-pattern avoidance)

All Day 2 §7 anti-patterns apply verbatim. Two DOCX-specific reinforcements:

**Cow Episode (DOCX edition):** the v1.1.1 `DocxAnalyzer` already catches the batin idioms (VBA, OLE, altChunks, external rels, tracked changes, hidden runs, per-run unicode primitives). Day 3-4 adds the OOXML zahir-and-metadata vectors that mirror the PDF gauntlet's lessons. Do NOT re-enumerate the v1.1.1 mechanisms; do NOT extend any v1.1.1 detector.

**Manifest discipline:** all six mechanisms use stdlib `zipfile` + `xml.etree.ElementTree` (or `lxml.etree` already in deps). NO new third-party imports. Verify `git diff requirements.txt pyproject.toml` shows no changes before each commit.

**Em-dash sweep:** zero em-dashes in analyzer descriptions, REPORT.md updates, commit messages. Run `grep -rn $'—' --include='*.py' --include='*.md' .` before each commit. Pre-existing v1.1.1 em-dashes in unrelated files are out of scope (Day 13 sweep).

---

## 8. End-of-day verification gate

Day 3-4 ships only when ALL are true:

1. `pytest tests/analyzers/test_docx_*` green.
2. `pytest docs/adversarial/docx_gauntlet/` green; 6 of 6 fixtures CAUGHT (was 0 of 6 on v1.1.1).
3. Test count: minimum **1,501 + ~18 = 1,519** tests pass (3 tests minimum per mechanism: registry pin + catch + control). Zero v1.1.1 or Day 1-2 regressions.
4. Additive-only DOCX parity invariant: every v1.0 baseline mechanism produces the same Finding shape on each existing DOCX fixture under v0/v0.1/v1.1.2.
5. **MECHANISM_REGISTRY count is 119** (113 + 6 new DOCX mechanisms). Coherence assertion green.
6. `docs/adversarial/docx_gauntlet/REPORT.md` updated: hit rate 6/6 (was 0/6). Honest, no rounding.
7. CHANGELOG entries for each of the 6 new mechanisms.
8. README "what we catch" section updated to match.
9. Em-dash sweep clean across all touched files.
10. Tier 0 still silent on DOCX fixtures.
11. Live API regression after each mechanism's commit (per-mechanism gate): curl with the fixture, assert at least one finding with the new mechanism name and tier.

If any item fails, Day 3-4 does not ship. Cut per §4 and reland honestly.

---

## 9. Ring composition closure

This prompt opens with Al-Baqarah 2:42: do not mix truth with falsehood, do not conceal truth while you know it. The DOCX gauntlet's six MISSED rows are six instances of Bayyinah knowing-but-not-surfacing what AI extractors will read. Day 3-4 makes the six structural facts surface alongside the rendered surface.

The four operational frameworks converge:
- **Differentiator:** each mechanism has its adversarial fixture and its control. Tier discipline preserved across six new entries.
- **Fatiha:** seven-step session, Cow Episode boundary, 20% skip rule, no over-specification beyond the fixture.
- **Structured Revelation:** every DOCX mechanism inspects the depth representation independently of (or alongside) the rendered surface.
- **Defense Case:** Day 3-4 closes 6 of the 6 documented DOCX MISSED rows. The "input-layer named component" claim gains six more named components.

If Day 3-4 ships clean, Bayyinah's per-format gauntlet hit rate moves to 10/12 across PDF and DOCX (83%, was 17% on v1.1.1).

> *"Wa allama Adama al-asma'a kullaha."* (Al-Baqarah 2:31)

The naming continues.

Bismillah. Tawakkaltu 'ala Allah.

---

*End of v1_1_2_day_3_4_docx_prep.md.*

---

# Bismillah ir-Rahman ir-Rahim
