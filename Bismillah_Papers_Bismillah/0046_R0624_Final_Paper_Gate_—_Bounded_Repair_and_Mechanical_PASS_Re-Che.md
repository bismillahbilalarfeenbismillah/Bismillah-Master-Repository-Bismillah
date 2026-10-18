# Bismillah ir-Rahman ir-Rahim

# R0624 -- Final Paper Gate — Bounded Repair and Mechanical PASS Re-Check

**Chronological Index:** 46 of 995  
**Date:** 2024  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** FINAL_PASS_RECHECK.md  
**Source Format:** md  
**SHA-256:** `705631903f97af38b98d5332d9ab4390c64a6fd0a606ff68d80f8c1c45a60854`  

---

## R0624 · Final Paper Gate — Bounded Repair and Mechanical PASS Re-Check

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: FINAL_PASS_RECHECK.md
- source_format: md
- text_sha256: 705631903f97af38b98d5332d9ab4390c64a6fd0a606ff68d80f8c1c45a60854

# Final Paper Gate — Bounded Repair and Mechanical PASS Re-Check
## *Inheritance, Transmission, and the Locus of Accountability*

**Seat declaration.** This is a single-agent **execution gate**, not a substantive review round.
It performs (a) the one bounded content repair authorized by the Round-3 model-council synthesis and
(b) the narrow mechanical PASS gate on the resulting deliverables. No argument, transfer condition,
omission, or theology was reopened; all such matters were dispositioned in Round 2 and are out of
scope here per the Re-Check Brief. The controlling correction instruction is
`ROUND3_model-council-synthesis.pplx.md` ("Required action"), carried by GPT 5.4 (OpenAI) and
Gemini 3.1 Pro (Google).

---

## 1. Controlled input packet — integrity

All six manifest files matched their recorded SHA-256 values in `SHA256SUMS-7.txt` before any edit:

| File | Manifest hash (prefix) | Verified |
|---|---|:---:|
| RECHECK_BRIEF.md | `88e24a5e…` | ✓ |
| ROUND2_model-council-synthesis.pplx.md | `a3037070…` | ✓ |
| paper.docx | `024d9f1c…` | ✓ |
| paper.pdf | `2ce8a0a1…` | ✓ |
| paper_source.md | `c71b95fd…` | ✓ |
| round2_controlled_source.md | `b956bc44…` | ✓ |

The baseline for the exact diff is `round2_controlled_source.md`. The corrected input carrying the
seven Round-2 corrections is `paper_source.md`.

---

## 2. The single bounded content repair

The Round-3 synthesis (NON-PASS) found that, beyond the seven authorized corrections, the corrected
`paper_source.md` contained one **unauthorized Shumailov-transition rewrite** — a reframing
("**Both halves matter.** … The second **strengthens rather than weakens** the case for intervening
at propagation, because the practices the severity depends on are themselves difficult to measure…")
that changed argumentative emphasis rather than merely removing a repeated transition.

Per the synthesis "Required action", the repair replaces that hunk with the scope-compliant wording:

> **Both halves matter here.** The first establishes that recursive formative signal is not merely a
> bookkeeping concern. The second establishes that the harm is conditional on practices which are
> themselves unmeasurable without the marking this paper asks for. This is the argument for
> intervening at propagation rather than at formation, and it is also why marking is cheap now and
> unrecoverable later.

This restores the Round-2 controlled wording and performs only the minimal lint-safe repair
(deleting the duplicated "the argument for the ask rather than against it" clause that produced the
"…for the ask rather than against it. This is the argument for…" repetition). No other wording,
formatting, theology, citation, section structure, metadata, or argument was altered.

**Method (DOCX).** The supplied `paper.docx` was edited directly at the XML level: the DOCX was
unpacked, and the exact run sequence for the Shumailov paragraph in `word/document.xml` was replaced
in place, preserving the bold run for the lead phrase and all paragraph/section/style structure. The
document was repacked. No re-layout, no style change, no conversion from Markdown.

**Method (PDF).** The original `paper.pdf` was produced by pandoc → XeLaTeX (`Producer: xdvipdfmx`,
Latin Modern fonts, numbered sections, letter, 1-inch margins). To preserve that presentation, the
final PDF was regenerated from the corrected source through the **same pandoc → XeLaTeX pipeline**
(`--number-sections --shift-heading-level-by=-1 -V papersize=letter -V geometry:margin=1in
-V parskip=true`, with title/subtitle/author/date metadata matching the original title block). A
LibreOffice DOCX→PDF conversion was rejected because it produced divergent typography and pagination;
the pandoc regeneration reproduces the original title block, numbered headings, Latin Modern
typography, paragraph spacing, and margins. The corrected paragraph and its page were rendered and
visually verified.

---

## 3. Mechanical PASS gate — results

Verification script: `pass_gate.py`; machine evidence: `pass_gate_results.json`.
Normalization is **wrap-immune**: all whitespace is collapsed, Markdown emphasis (`*`/`**`) is
stripped, and PDF soft-hyphenation at line breaks is healed before matching.

### 3.1 Exact source diff against `round2_controlled_source.md`
Ten unified-diff hunks, mapping exactly to the seven authorized corrections plus the one minimal
lint-safe Shumailov restoration — no other substantive hunk:

| Hunk | Disposition |
|---|---|
| `@@ -15` | #7 Standing lint — front-matter `structure.2` / `remedy.3` remnants removed |
| `@@ -343` | #3 Bridge condition four — present-tense correction locus; locus need not sit with the originating model |
| `@@ -353` | #4 Public decidability — categorical → graded observability |
| `@@ -463` | #5 NIST body — three primitives without upgrading to "distinct controls" |
| `@@ -514` | #1 Article 12 body — record-keeping scoped away from the marking obligation |
| `@@ -540` | **Minimal lint-safe Shumailov restoration** (duplicate "the argument for" clause removed only) |
| `@@ -635` | #6 Concealment variable — penalty-if-detected defined once, expected cost derived |
| `@@ -694` | #2 F-5 sentence — malformed ending replaced |
| `@@ -719` | #7 Standing lint — `remedy.4` numeric section reference removed in F-7 |
| `@@ -887` | #1 / #5 Reference annotations — Article 50 vs Article 12; NIST provenance-tracking wording |

### 3.2 Unauthorized rewrite absent
`strengthens rather than weakens` — **absent** in source, DOCX, and PDF.
`which is the argument for the ask rather than against it` (baseline-only clause) — **absent**
(correctly removed by the minimal restoration).

### 3.3 Seven authorized corrections present (wrap-immune, all confirmed)
Article 50/Article 12 annotation and body scope; F-5 repaired sentence; bridge correction locus and
"need not sit with the originating model"; graded public decidability; NIST body + annotation
separate provenance-tracking techniques and provenance-vs-detection distinction; concealment variable
defined once with derived expected cost; standing lint remnants (`structure.2`, `remedy.3`,
`remedy.4`, `falsification conditions's`) all absent; no flagged doubled words.

### 3.4 Cross-format semantic synchronization (source / DOCX / PDF)
Every correction marker and the scope-compliant Shumailov wording is present in **all three**
formats; the unauthorized "strengthens rather than weakens" wording is absent in **all three**.

### 3.5 Primary-source validation of the scoped Article 50 / NIST text
- **AI Act Article 50** requires that synthetic outputs be "marked in a machine-readable format and
  detectable as artificially generated or manipulated" ([EUR-Lex, Regulation (EU) 2024/1689](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)); it does **not** contain a
  lifecycle-logging obligation.
- **AI Act Article 12 "Record-keeping"** requires high-risk systems to "technically allow for the
  automatic recording of events (logs) over the lifetime of the system" ([EUR-Lex, Regulation (EU) 2024/1689](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)) — this is where the
  logging requirement actually sits, as the corrected annotation states.
- **NIST AI 600-1** lists "digital watermarking" and provenance metadata among
  "provenance data tracking techniques," distinct from synthetic-content detection ([NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)), matching the corrected body and
  annotation without upgrading them to formally distinct controls.

### 3.6 SHA-256 checksums (final deliverables)
Recorded in `FINAL_SHA256SUMS.txt`:

| File | SHA-256 |
|---|---|
| FINAL_paper_source.md | `9ce60e1468b1b04bbcf478b9385b6d0db98ac317c9a193615b3ae64b309f92a9` |
| FINAL_paper.docx | `3fe768c70a948dd6bab73c0202fec3ce3c20cc0e79e2fa296afa754f5877c72d` |
| FINAL_paper.pdf | `7cad4ed88e89b7769a15373ab7a7a480c8eaa0c78351c5d1cc8196215cdfad60` |

---

## 4. Verdict

| Gate check | Result |
|---|:---:|
| Diff = seven corrections + minimal lint-safe restoration only | ✓ |
| Unauthorized Shumailov rewrite absent (all formats) | ✓ |
| All seven authorized corrections present | ✓ |
| Scope-compliant Shumailov wording present | ✓ |
| Standing lint clean; no doubled words | ✓ |
| Markdown / DOCX / PDF semantically synchronized | ✓ |
| Scoped Article 50 / Article 12 / NIST text validated against primary sources | ✓ |

## **VERDICT: PASS**

The single authorized bounded repair has been applied, the seven Round-2 corrections are preserved
unchanged, no unauthorized hunk remains, the three publication formats are synchronized, and the
scoped regulatory/standards text is validated against its primary sources. The controlled file set
is now delta-disciplined and passes the narrow mechanical gate.

---

# Bismillah ir-Rahman ir-Rahim
