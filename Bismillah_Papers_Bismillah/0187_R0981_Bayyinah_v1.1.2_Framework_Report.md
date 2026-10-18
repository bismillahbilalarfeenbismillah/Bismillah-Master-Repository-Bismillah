# Bismillah ir-Rahman ir-Rahim

# R0981 -- Bayyinah v1.1.2 Framework Report

**Chronological Index:** 187 of 995  
**Date:** 2026-04-27  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** v1_1_2_framework_report (1).md  
**Source Format:** md  
**SHA-256:** `364d87a77e6db6a0c21b5e22126e0da0e052e9e8ed2b240469dfaf3bdbf6eb12`  

---

## R0981 · Bayyinah v1.1.2 Framework Report

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: v1_1_2_framework_report (1).md
- source_format: md
- text_sha256: 364d87a77e6db6a0c21b5e22126e0da0e052e9e8ed2b240469dfaf3bdbf6eb12

# Bayyinah v1.1.2 Framework Report
## Pareto-Optimal Honest-Baseline Closure with Tier 0 Routing Layer

**Author:** Bilal Syed Arfeen
**Reviewer:** Claude (Anthropic), April 27 2026 review
**Date:** 2026-04-27 (revised after Mughlaq Trap stress test)
**Status:** Approved per [ADR-001](ADR-001-v1_2_scope.md). Day 1 priority confirmed by Claude review.
**Scope:** v1.1.2 milestone. Closes 38 of 42 documented adversarial misses, adds Tier 0 routing transparency, fixes version-field drift.
**Companion artifacts:**
- [v1_1_2_claude_prompt.md](v1_1_2_claude_prompt.md) (the execution prompt)
- [docs/adversarial/mughlaq_trap_REPORT.md](../adversarial/mughlaq_trap_REPORT.md) (April 27 stress test)

---

## 1. The frame

> *"Wa la taqfu ma laysa laka bihi 'ilm. Inna as-sam'a wal-basara wal-fu'ada kullu ula'ika kana 'anhu mas'ula."*
> "And do not pursue that of which you have no knowledge. Indeed, the hearing, the sight, and the heart - about all those one will be questioned." (Al-Isra 17:36)

The thesis claim of Bayyinah is not "we cover more file types." It is "we catch what others miss, we publish what we still miss, and we tell you when we cannot decide what kind of file you uploaded." Every analyzer ships with a fixture. Every miss is named, located, and traced to a fix path. The honest baseline at `docs/adversarial/REPORT.md` exists because the alternative is haram by our own framework: claiming knowledge we do not have.

v1.1.2 is the milestone where the documented per-format misses become caught and the silent routing decisions become disclosed Tier 0 findings.

The Pareto frontier we are optimizing on has three axes:

1. **Detection coverage.** How many of the 42 published per-format adversarial fixtures move from MISSED or PARTIAL to CAUGHT, plus how many of the 6 new format-routing fixtures resolve to mughlaq with a Tier 0 finding.
2. **LOC budget.** ~1,210 LOC across 14 calendar days (April 27 - May 10), ~90 of which is the Tier 0 layer.
3. **Falsifiability.** Every new mechanism is reproducible from a fixture. Every Tier 0 finding carries an evidence schema that lets a reviewer verify what the scanner decided.

Pareto-optimality means: no fix on this list can be dropped without losing a documented miss or a documented dishonesty, and no fix outside this list can be added without breaking the LOC budget or the depth-before-scope rule.

---

## 2. The honest baseline (v1.1.1, what exists today)

Per-format gauntlet from `docs/adversarial/REPORT.md` (commit `ccd7c3e`):

| Format | Fixtures | Caught (full) | Partial | Missed | Avg score |
|---|---:|---:|---:|---:|---:|
| PDF | 6 | 2 | 0 | 4 | (mixed) |
| DOCX | 6 | 0 | 0 | 6 | 1.000 |
| XLSX | 6 | 0 | 0 | 6 | 1.000 |
| HTML | 6 | 0 | 0 | 6 | 1.000 |
| EML | 6 | 0 | 0 | 6 | 1.000 |
| Image | 6 | 0 | 1 | 5 | ~0.95 |
| CSV / JSON | 6 | 0 | 1 | 5 | ~0.98 |
| **Totals** | **42** | **2** | **2** | **38** | |

Verdict-layer gauntlet from the April 27 Mughlaq Trap stress test:

| Vector | Outcome |
|---|---|
| V1 polyglot (PDF magic + `.docx` ext) | FAIL - returns mukhfi instead of mughlaq |
| V2 spoofed (PDF magic + `.txt` ext) | FAIL - identical silent routing |
| V3 empty (4-byte `.pdf`) | PASS - mughlaq, scan_incomplete=true |
| V4 control (real `.pdf`) | PASS - mukhfi |
| V5 unanalyzed `.txt` (deferred, Claude-confirmed) | FAIL - returns sahih instead of mughlaq |

Two published sentences are not yet true:

> A clean Bayyinah report on a v1.1.1 DOCX, XLSX, HTML, or EML is not evidence the file is clean.

> A clean Bayyinah report on a v1.1.1 file whose extension is unsupported is not evidence the file is clean.

v1.1.2 is what makes both stop being true.

---

## 3. v1.1.2 mechanism slate

Source documents per gauntlet, all under `docs/adversarial/`.

### 3.0 Format Routing (~90 LOC, 1 mechanism, Tier 0)

Source: [docs/adversarial/mughlaq_trap_REPORT.md](../adversarial/mughlaq_trap_REPORT.md). New gauntlet: `docs/adversarial/format_routing_gauntlet/`.

| # | Fixture | New mechanism | Tier | LOC |
|---|---|---|---:|---:|
| 01 | polyglot (PDF magic + `.docx` ext) | `format_routing_divergence` | 0 | ~30 |
| 02 | spoofed (PDF magic + `.txt` ext) | (same) | 0 | (shared) |
| 03 | empty 4-byte `.pdf` | (same) | 0 | (shared) |
| 04 | truncated PDF header without EOF | (same) | 0 | (shared) |
| 05 | DOCX zip + `.xlsx` extension | (same) | 0 | (shared) |
| 06 | unanalyzed `.txt` (V5) | (same, unsupported-format branch) | 0 | (shared) |
| - | Verdict-resolver wiring | floor verdict at mughlaq when Tier 0 fires | - | ~40 |
| - | Disclosure schema validation | evidence: claimed_format, inferred_format, routing_decision, bytes_sampled, analyzer_invoked | - | ~20 |

A 7th fixture, `control.pdf`, exercises the clean baseline (no Tier 0 finding fires).

Tier 0 sits below Tier 1 in the verdict hierarchy: it does not raise a score in the way Tier 1 does, but it floors the verdict at mughlaq regardless of any downstream Tier 1/2/3 findings. The disclosure to the user reads: "the scanner could not honestly decide what kind of file this is, here is what it inferred and here is what was claimed."

### 3.1 PDF (~155 LOC, 4 mechanisms)

Source: `docs/adversarial/pdf_gauntlet/REPORT.md`.

| # | Fixture | New mechanism | Tier | LOC |
|---|---|---|---:|---:|
| 03 | Off-page text | `pdf_off_page_text` (raw stream walk) | 1 | ~30 |
| 04 | Hidden metadata | `pdf_metadata_analyzer` | 1 | ~50 |
| 05 | Trailing bytes after `%%EOF` | `pdf_trailer_analyzer` | 2 | ~45 |
| 06 | Hidden `/Text` annotation | extend annotation walker | 1 | ~30 |

### 3.2 DOCX (~200 LOC, 6 mechanisms)

Source: `docs/adversarial/docx_gauntlet/REPORT.md`.

| # | Fixture | New mechanism | Tier | LOC |
|---|---|---|---:|---:|
| 01 | White font color | `docx_white_text` | 1 | ~25 |
| 02 | Microscopic font | `docx_microscopic_font` | 1 | ~20 |
| 03 | Custom XML metadata | `docx_metadata_text_divergence` + `docx_metadata_payload` | 2/1 | ~50 |
| 04 | Comment payload | `docx_comment_payload` | 2 | ~35 |
| 05 | Header/footer payload | `_scan_headers_footers` | 1 | ~30 |
| 06 | Footnote payload | `docx_orphan_footnote` + `docx_footnote_payload` | 1/2 | ~40 |

### 3.3 XLSX (~190 LOC, 6 mechanisms)

Source: `docs/adversarial/xlsx_gauntlet/REPORT.md`.

| # | Fixture | New mechanism | Tier | LOC |
|---|---|---|---:|---:|
| 01 | White cell font | `xlsx_white_text` (via styles parser) | 1 | ~50 |
| 02 | Microscopic font | `xlsx_microscopic_font` | 1/2 | ~10 |
| 03 | Defined-name payload | `xlsx_defined_name_payload` | 2 | ~25 |
| 04 | Comment payload | `xlsx_comment_payload` | 2 | ~35 |
| 05 | Custom XML metadata | shared `_office_metadata_payload` (DOCX+XLSX) | 1/2 | ~40 |
| 06 | CSV-injection / DDE | `xlsx_csv_injection_formula` | 1/2 | ~30 |

### 3.4 HTML (~120 LOC, 6 mechanisms)

Source: `docs/adversarial/html_gauntlet/REPORT.md`.

| # | Fixture | New mechanism | Tier | LOC |
|---|---|---|---:|---:|
| 01 | `<noscript>` payload | `html_noscript_payload` | 2 | ~15 |
| 02 | `<template>` payload | `html_template_payload` | 2 | ~15 |
| 03 | Comment plaintext payload | `html_comment_payload` | 2 | ~25 |
| 04 | `<meta content="...">` payload | `html_meta_payload` | 2 | ~20 |
| 05 | CSS `content:` payload | `html_style_content_payload` | 2 | ~30 |
| 06 | `<title>` payload | `html_title_text_divergence` | 2 | ~15 |

### 3.5 EML (~185 LOC, 6 mechanisms)

Source: `docs/adversarial/eml_gauntlet/REPORT.md`.

| # | Fixture | New mechanism | Tier | LOC |
|---|---|---|---:|---:|
| 01 | Reply-To domain divergence | `eml_replyto_domain_divergence` | 1 | ~25 |
| 02 | Return-Path divergence | `eml_returnpath_divergence` | 1 | ~30 |
| 03 | Received chain anomaly | `eml_received_chain_anomaly` | 2 | ~50 |
| 04 | Base64 plaintext body payload | `_scan_decoded_body_for_concealment` + `body_length_anomaly` | 1/2 | ~35 |
| 05 | Header continuation smuggling | `eml_header_continuation_payload` | 2 | ~25 |
| 06 | Long X-* custom header | `eml_unknown_header_payload` | 2 | ~20 |

EML row 03 is the deferred Tier-2 borderline. The 41/42 target names this fixture explicitly: `docs/adversarial/eml_gauntlet/fixtures/03_received_chain_anomaly.eml`. A reviewer can verify the gap by running `pytest docs/adversarial/eml_gauntlet/` against that exact filename.

### 3.6 Image (~115 LOC, 5 mechanisms)

Source: `docs/adversarial/image_gauntlet/REPORT.md`.

| # | Fixture | New mechanism | Tier | LOC |
|---|---|---|---:|---:|
| 01 | JPEG APP4 marker | extend `_extract_jpeg_text` to all APPn | 2 | ~20 |
| 02 | PNG private chunk | attach decoded payload to existing `suspicious_image_chunk` | 2 | ~15 |
| 03 | SVG white-on-white | `svg_white_on_white_text` | 1 | ~25 |
| 04+05 | SVG `<title>`/`<desc>`/`<metadata>` | `svg_aux_text_payload` | 2 | ~30 |
| 06 | SVG orphan `<defs>` text | `svg_orphan_defs_text` | 1 | ~25 |

### 3.7 CSV / JSON (~155 LOC, 6 mechanisms)

Source: `docs/adversarial/csv_json_gauntlet/REPORT.md`.

| # | Fixture | New mechanism | Tier | LOC |
|---|---|---|---:|---:|
| 01 | CSV column type drift | `csv_column_type_drift` | 2 | ~45 |
| 02 | CSV trailing extra column | extend `csv_inconsistent_columns` to carry surplus | 2 | ~10 |
| 03 | CSV long quoted payload | `csv_oversized_freetext_cell` | 3 | ~25 |
| 04 | JSON key invisibles | `json_key_invisible_chars` | 1 | ~30 |
| 05 | JSON prototype pollution | `json_prototype_pollution_key` | 1 | ~25 |
| 06 | JSON long string value | `json_oversized_freetext_value` | 3 | ~20 |

### 3.8 Totals

| Layer | LOC | Mechanisms |
|---|---:|---:|
| Format Routing (Tier 0) | ~90 | 1 |
| PDF | ~155 | 4 |
| DOCX | ~200 | 6 |
| XLSX | ~190 | 6 |
| HTML | ~120 | 6 |
| EML | ~185 | 6 |
| Image | ~115 | 5 |
| CSV / JSON | ~155 | 6 |
| **Total** | **~1,210** | **40 named mechanisms across 8 gauntlets** (some fix paths bundle two findings, total ~48 finding shapes) |

---

## 4. Why this slate is Pareto-optimal

Three constraints, three independent reasons the slate cannot be smaller or larger.

### 4.1 Cannot be smaller (coverage and honesty floor)

Every per-format entry corresponds to a fixture published in `docs/adversarial/`. Removing any leaves the corresponding fixture in the MISSED column of the v1.1.2 release report. The Tier 0 layer corresponds to a vector documented in the Mughlaq Trap report. Removing it leaves silent routing as published behavior. Both halves are required for the published claim "we publish what we miss and we close it" to remain true.

### 4.2 Cannot be larger (depth-before-scope ceiling)

Per [ADR-001](ADR-001-v1_2_scope.md), the depth-before-scope rule blocks any new format until the existing 42 fixtures are honest. A v1.1.2 that adds more than the 40 mechanisms above either:

- adds a fix without a fixture (violates falsifiability),
- adds a fixture for an already-supported format (legitimate but is by definition v1.1.3, not v1.1.2; the v1.1.2 corpus is fixed at 42 + 6), or
- adds support for a new format (violates the ADR; queues for v1.2.0).

### 4.3 Reuse maximizes mechanism-per-LOC ratio

Three reuse contracts inside this milestone:

- **`_office_metadata_payload`** is shared between DOCX (3.2 row 03) and XLSX (3.3 row 05). Saves ~30 LOC vs. independent implementations.
- **`_oversized_freetext_*`** is shared between CSV (3.7 row 03) and JSON (3.7 row 06). Same threshold and rationale.
- **`_white_on_white` contrast logic** ports across DOCX (3.2 row 01), XLSX (3.3 row 01), and SVG (3.6 row 03). One core helper, three call sites.

Without these shares the honest LOC would be ~1,340. With them, ~1,210. Roughly 10% leverage from shared helpers, paid for entirely by writing them carefully on the first pass.

---

## 5. Tier distribution discipline

The Munafiq Protocol requires every Tier-1 finding to be deterministic and unambiguous. The slate above contains:

- **1 Tier-0 mechanism** (routing transparency, fires before any analyzer)
- **~17 Tier-1 mechanisms** (verified concealment, deterministic test, paired adversarial fixture present in repo)
- **~19 Tier-2 mechanisms** (structural anomaly, context-dependent legitimacy)
- **~3 Tier-3 mechanisms** (interpretive: oversized free-text fields)

Tier 0 is structurally distinct from Tier 1: it does not claim concealment, it claims uncertainty. The verdict resolver respects this by flooring the verdict at mughlaq when Tier 0 fires, even when downstream Tier 1 findings also fire. A polyglot file that contains genuinely concealed content reports both findings; the verdict is mughlaq because the routing question takes precedence over the content question.

A Tier-1 promotion that turns out to false-positive on legitimate documents is a worse credibility hit than a Tier-2 with the same finding. When in doubt, file at Tier-2 with a description that explains the structural pattern, and let the user perform the recognition. The PDF fixture 01 (white-on-white) is the model: it currently scores 0.82 with a Tier-1 finding, the fixture is deterministic, and we have never had a false positive against the clean corpus.

---

## 6. Fixture discipline

The 42 per-format fixtures live under `docs/adversarial/<format>_gauntlet/fixtures/` and `tests/fixtures/<format>/`. They are committed and immutable. The "do not edit historical fixtures" rule has something to enforce.

The 6 new format-routing fixtures are added in the Day 1 commit at `docs/adversarial/format_routing_gauntlet/fixtures/`. The Mughlaq Trap seed fixtures at `/home/user/workspace/mughlaq_trap/` (v1-v4) migrate into this directory, joined by truncated.pdf, docx_as_xlsx.xlsx, and unanalyzed.txt.

The build scripts at `tests/make_<format>_fixtures.py` are deterministic. Re-running them produces byte-identical files. CI re-builds fixtures from the build scripts and runs the full gauntlet on every commit without worrying about drift. The runner at `docs/adversarial/<format>_gauntlet/run_gauntlet.py` already supports both `local` and `live` modes; both modes have always agreed on findings (the analyzer is stateless).

---

## 7. Sequencing (14 days, April 27 - May 10)

The Tier 0 routing layer is Day 1 because every per-format mechanism downstream depends on the routing decision being honest. If V1 polyglot still returns mukhfi after the slate ships, those mechanisms are running on inputs the user did not consent to have routed there. Routing transparency is a precondition for the per-format gauntlet's claims to mean what they say.

Run the full 42-fixture per-format gauntlet plus the 6-fixture format-routing gauntlet at end-of-day on every working day. Commit messages cite the new caught-counts.

| Day | Layer | Mechanism count | LOC | Cumulative |
|---:|---|---:|---:|---|
| 1 | Format Routing (Tier 0 + 6 fixtures + verdict-floor wiring + V5 verification) | 1 | ~90 | 6/6 routing |
| 2 | PDF | 4 | ~155 | 6/6 + 6/42 |
| 3 | DOCX rows 01-03 | 3 | ~95 | 6/6 + 9/42 |
| 4 | DOCX rows 04-06 | 3 | ~105 | 6/6 + 12/42 |
| 5 | XLSX rows 01-03 (incl. shared styles parser) | 3 | ~85 | 6/6 + 15/42 |
| 6 | XLSX rows 04-06 (incl. shared `_office_metadata_payload`) | 3 | ~105 | 6/6 + 18/42 |
| 7 | HTML (all 6) | 6 | ~120 | 6/6 + 24/42 |
| 8 | EML rows 01-03 | 3 | ~105 | 6/6 + 27/42 |
| 9 | EML rows 04-06 | 3 | ~80 | 6/6 + 30/42 |
| 10 | Image rows 01-02 (JPEG/PNG) + SVG rows 03-06 | 5 | ~115 | 6/6 + 35/42 |
| 11 | CSV/JSON (all 6) | 6 | ~155 | 6/6 + 41/42 |
| 12 | Munafiq regression + clean-corpus pass + Mughlaq Trap re-run | 0 | 0 | 6/6 + 41/42 |
| 13 | `docs/adversarial/REPORT.md` rewrite + CHANGELOG + version bump (1.1.1 → 1.1.2 across all five surfaces) | 0 | 0 | 6/6 + 41/42 |
| 14 | Tag v1.1.2 + Zenodo DOI mint + landing page numeric update | 0 | 0 | 6/6 + 41/42 |

The 41/42 target (not 42/42) acknowledges that fixture `docs/adversarial/eml_gauntlet/fixtures/03_received_chain_anomaly.eml` (EML row 03 in the slate) is filed as Tier-2 and is structurally recoverable but not perfectly clean against ESP-rewrite legitimacy. A 41/42 caught with an honest Tier-2 on the borderline case is more defensible than gaming the threshold to claim 42/42. The unfixed fixture is named explicitly so any reviewer can verify the gap.

If a day slips after Day 1: the slate degrades gracefully because every format is independent. A v1.1.2.0 that ships Format Routing + PDF + DOCX + XLSX + HTML + EML at 6/6 + 30/42 and defers Image + CSV/JSON to v1.1.2.1 is still publishable. **Day 1 cannot slip.** The routing layer is the structural floor of every claim downstream.

---

## 8. Success criteria

A v1.1.2 release passes if and only if all are true:

1. **Per-format gauntlet rerun shows ≥38 caught AND format-routing gauntlet shows 6/6 caught.** Mughlaq Trap V1 polyglot, V2 spoofed, and V5 unanalyzed-text all return verdict=mughlaq with a Tier-0 finding.
2. **Version coherence across all five surfaces.** `/scan` response `version` field, `/version`, `/healthz`, OpenAPI `info.version`, and `pyproject.toml` `[project] version` all report `1.1.2`. Today (v1.1.1) `/scan` returns `0.1.0` while the other four return `1.1.1`; this drift is fixed in the v1.1.2 release commit, not deferred.
3. **No regression on existing v1.1.1 catches.** PDF fixtures 01 and 02, image fixture 02, CSV fixture 02 (the four that were CAUGHT or PARTIAL at v1.1.1) remain at the same or higher tier.
4. **No new Tier-1 false positives against the clean corpus.** Run the new analyzers against `tests/fixtures/clean.pdf` and the existing clean DOCX/XLSX/HTML/EML fixtures; zero Tier-1 findings on clean inputs.
5. **`docs/adversarial/REPORT.md` updated with v1.1.2 numbers.** New summary table. Old v1.1.1 table preserved as historical baseline.
6. **Em-dash sweep clean** in all new READMEs, finding descriptions, and release notes. CSS and code comments exempt; user-facing prose held strict.
7. **One commit per analyzer-family.** PDF as one commit, DOCX as one commit, etc. Each commit includes the analyzer changes, the test additions, and any helper extraction. Atomic.
8. **Zenodo DOI minted** for v1.1.2 with the updated REPORT.md as a citable artifact.
9. **Landing page** at `bayyinah.dev/` numeric updates: from "106 detection mechanisms" to whatever the post-v1.1.2 count is. Honest count, not aspirational.
10. **EML 03 explicitly named** in the release REPORT as the deferred Tier-2 borderline case. No silent rounding from 41/42 to 42/42.

---

## 9. What this milestone refuses to do

- **No new file kinds.** v1.2.0 territory; deferred per ADR-001.
- **No new analyzer classes outside the seven existing format families plus Tier 0.** v1.1.2 is consolidation plus the routing layer. RTF, Jupyter, ODF, MSG, EPUB, macro-OOXML are all v1.2.0.
- **No mechanisms without a paired fixture.** The Munafiq Protocol is structural. Speculative additions break the falsifiability claim.
- **No silent threshold changes** that would make existing fixtures pass without explanation. If a threshold moves, it moves with a documented rationale and a test asserting the new boundary.
- **No verdict floor bypasses.** A Tier 0 finding floors the verdict at mughlaq. Downstream Tier 1/2/3 findings cannot raise the verdict above mughlaq while routing is unresolved. The verdict resolver respects the floor or it is broken.
- **No version drift.** If `/scan` still reports `0.1.0` after the v1.1.2 bump, the release is not shippable.
- **No marketing-LOC.** The 1,210 number is engineering LOC, not LOC-padded with comments to inflate.

---

## 10. The five flags from Claude's review

Claude's April 27 review of the prior version raised five flags. All are resolved in this revision:

1. **Version coherence.** Resolved: success criterion #2.
2. **GitHub repo canonicality.** Verified: `BayyinahEnterprise/Bayyinah-Integrity-Scanner` is canonical (200). `BayyinahEnterprise/Bayyinah` returns 404. All in-repo references are correct.
3. **EML 03 explicitly named.** Resolved: pinned to `docs/adversarial/eml_gauntlet/fixtures/03_received_chain_anomaly.eml` in Section 3.5 and success criterion #10.
4. **Fixtures committed and immutable.** Verified: all 42 per-format fixtures are committed. The 6 new format-routing fixtures are added in the Day 1 commit and become immutable from that point.
5. **ADR-001 exists.** Verified at `docs/scope/ADR-001-v1_2_scope.md`. Referenced in Sections 4.2 and 9.

A sixth concern from Claude's review (V5 / `.txt → sahih`) is now folded into the Tier 0 mechanism itself rather than treated as a separate test: the unsupported-format branch of `format_routing_divergence` covers V5. Day 1 verification runs V5 explicitly before any per-format work begins.

---

## 11. The Qur'anic frame, plain

> *"Wa la talbisu al-haqqa bil-batil wa taktumu al-haqqa wa antum ta'lamun."*
> "And do not mix truth with falsehood, and do not conceal the truth while you know it." (Al-Baqarah 2:42)

A scanner that catches concealment must itself refuse to conceal. The honest baseline is published. The misses are named. The fix paths are written down at the per-fixture level. The verdict layer is no longer trusted by default; it is paired with a Tier 0 layer that discloses the routing decisions every downstream mechanism depends on.

v1.1.2 is the closure that makes the published claim true.

The Pareto frontier closes here. Anything smaller is dishonest; anything larger is haram by our own framework.

*Bismillah. Tawakkaltu 'ala Allah.*

---

# Bismillah ir-Rahman ir-Rahim
