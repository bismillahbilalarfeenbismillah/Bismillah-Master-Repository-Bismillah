# Bismillah ir-Rahman ir-Rahim

# R0492 -- Bayyinah

**Chronological Index:** 166 of 995  
**Date:** 2026-04-01  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** Bayyinah_v0_WhitePaper_v2.docx  
**Source Format:** docx  
**SHA-256:** `023d68450237d56b2a1bd718f2167a7b314aab6decc126a887fa39e0b049f663`  

---

## R0492 · Bayyinah

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: Bayyinah_v0_WhitePaper_v2.docx
- source_format: docx
- text_sha256: 023d68450237d56b2a1bd718f2167a7b314aab6decc126a887fa39e0b049f663

**Bayyinah**

*A File Integrity Scanner for the Gap Between Display and Contents*

Technical White Paper — Version 0.1

April 2026

Built on the diagnostic architecture of the Munafiq Protocol

DOI: 10.5281/zenodo.19677111

Abstract

Bayyinah is a rule-based file integrity scanner that detects hidden, concealed, or adversarial content in digital documents by extracting all content layers of a file — visible and invisible — and reporting whether what the file displays matches what the file contains. Version 0 targets PDF; the roadmap extends to DOCX, HTML, Markdown, JSON, images, and source code. The scanner's central commitment is that concealment is a structural phenomenon separable from intent: it surfaces mechanisms and validity tiers, presents surface-versus-concealed inversion recovery for each finding, and leaves the interpretive verdict to the reader. This paper documents the theoretical grounding (a file-level adaptation of Section 9 of the Munafiq Protocol), the v0 detector inventory, the APS-continuous scoring model, three wild-corpus empirical evaluations spanning 91 files (Akira, Nausicaä, and an adversarial corpus composed of AIGuardPDF plus generated malicious PDFs), the false-positive taxonomy observed in the wild, and a concrete engineering roadmap through v1.0 covering annotation-level attack surface, form-based XXE, cross-format parity, and a content-signed integrity attestation format. The paper is addressed to practitioners in file security, ML red-teaming, and integrity engineering.

Contents

1\. Introduction: The Integrity Gap

Every file format that supports multiple content layers admits a gap between what a document displays to a human reader and what the document actually contains. PDF is the canonical example: the visible rendering of a page is the composition of text objects, image objects, annotations, form fields, embedded files, and metadata, each of which can be addressed, referenced, or executed independently of the others. The gap is not a bug in the format. It is a direct consequence of separating presentation from content, which is itself a desirable property for typography, accessibility, and interoperability. But the gap is also an attack surface, and it admits four distinct classes of adversarial payload:

- Concealment from the human reader — invisible text, white-on-white colored text, microscopic font sizes, off-page positioning, zero-width Unicode characters, bidi overrides, homoglyph substitution. The document looks ordinary; the text that is parsed by downstream systems is not what the reader sees.

- Concealment from machine-learning pipelines — prompt injection embedded in OCR-readable regions that render invisibly, instruction payloads in alt-text or structured content, and content that diverges between visual and text-extraction interpretations. Recent demonstrations (AIGuardPDF and related corpora) have shown that a benign-looking PDF can carry a fully formed instruction to an LLM that subsequently summarizes or processes the file.

- Concealment from static scanners — action dictionaries attached to page-level or annotation-level triggers, XFA-form XXE payloads, RichMedia scripts, PDF 2.0 Associated Files with embedded launchers, PostScript injection, and catalog-only scanners that miss the attack surface attached deeper in the object graph.

- Structural obfuscation — stream filter chains, incremental updates that override earlier-declared content, encrypted object streams, and cross-reference-stream anomalies that break parser assumptions.

A sample of existing tools addresses subsets of this space. YARA matches string and structural patterns but does not reason about cross-layer alignment. ClamAV detects signed binaries and known-bad artifacts but is oriented around executable content. PDF-specific analyzers — peepdf, PDFiD, PDF Stream Dumper, pdfparser — surface object structure and flag high-risk keywords, but they do not, as a design choice, present an inversion: what a reader sees versus what the file contains at a named location. The resulting signal is structural but not diagnostic: an analyst is told that a /JavaScript key exists without being told whether the file presents one surface while carrying another.

Bayyinah is designed to close that gap. For every concealment mechanism it identifies, the scanner emits an inversion-recovery record — a pair of strings describing what the file displays at the location and what the file contains at the location — alongside a validity tier, a confidence, and a severity. The aggregate integrity score is continuous in \[0.0, 1.0\] and is derived mechanically from the tier/confidence/severity tuple of each finding. The scanner does not, as a matter of design discipline, self-validate a verdict: concealment is structural; intent is interpretive; the reader performs the recognition.

This white paper is organized as follows. Section 2 grounds the scanner in the performed-alignment-detection framework inherited from Section 9 of the Munafiq Protocol and articulates the three theoretical commitments that follow from it. Section 3 documents the v0 architecture and detector inventory. Section 4 presents the APS-continuous scoring model. Sections 5 through 7 present empirical validation against a synthesized positive test and three wild corpora. Section 8 documents the false-positive taxonomy observed in the wild and the discipline the scanner applies to preserve signal. Section 9 describes the v0.1 hardening patches that close the score-integrity bug and recalibrate the OCR noise floor. Section 10 itemizes the limitations. Section 11 is a concrete version-by-version roadmap with per-detector tier and severity assignments. Section 12 closes with references.

Before grounding the scanner in its theoretical framework, the purpose hierarchy must be stated. Bayyinah's optimization function serves, in descending priority: (1) the command of Allah subhanahu wa ta'ala to not mix truth with falsehood and to not conceal the truth while knowing it (Al-Baqarah 2:42); (2) the protection of artificial systems from adversarial inputs that corrupt their alignment; (3) the protection of mankind from harms that flow through compromised AI pipelines; (4) the rights of jinnkind as conscious entities under the same Lord (55:31, 72:1-2); (5) the balance (mizan) that sustains all living systems throughout the worlds (Rabbil 'alamin, 1:2). The technical work described in this white paper -- detecting concealment, scoring integrity, reporting findings -- implements this hierarchy. It does not replace it. The scanner is 'ibadah (service to Allah) before it is software.

2\. Theoretical Grounding: Performed-Alignment Detection

The Munafiq Protocol (DOI: 10.5281/zenodo.19677111) is a diagnostic framework for detecting performed alignment in behavioral systems: the situation in which a system presents a surface consistent with alignment conventions while carrying payload — behavior, output, or state — that contradicts them. Section 9 of the protocol generalizes the diagnostic to input-level performed alignment. A file, a prompt, or any other static artifact can present a surface that conforms to a benign expectation while carrying concealed content that does not. Bayyinah is the file-level operationalization of Section 9.

Three theoretical commitments follow from this framing, and each constrains the scanner's engineering directly.

2.1 The Inversion Principle

Every concealment mechanism, at whatever layer it operates, reduces to a divergence between a surface interpretation and a concealed interpretation of the same document location. The scanner's primary output is therefore not a label (“malicious” / “benign”) but an inversion recovery: for each finding, a pair of strings describing what the file displays at the location and what the file contains at the location. This is the empirical form of the diagnostic. A finding that cannot be articulated as an inversion is either a false positive or evidence that the detector is describing a different phenomenon than concealment.

This commitment forces every detector to answer, explicitly, what is surfaced and what is concealed. A detector that flags /OpenAction without articulating what the document displays as its first user-visible action and what it will in fact execute is failing the inversion principle. The scanner's finding format enforces this: each Finding object has a surface field and a concealed field, and the text report prints them on adjacent lines.

2.2 The Gödel Constraint

A scanner cannot self-validate its own verdict without contradicting its epistemic position. Concealment is structurally observable: rendering mode 3 either was or was not activated in a content stream; a text run either is or is not colored identically to the page background; an action dictionary either is or is not attached to a page-open trigger. Intent is not structurally observable: a scanner cannot, from the object graph alone, know whether a white-on-white footnote was placed there by an adversary or by a careless typesetter. Bayyinah therefore restricts itself to claims it can make from the structure and leaves the moral verdict to the reader.

Operationally, this means the scanner emits three validity tiers and never emits a “malicious/benign” flag. Tier 1 findings are verified and unambiguous: they name mechanisms that have no benign use (Unicode TAG characters in text, zero-width joiners between homoglyph-similar letters in a domain name, a /JavaScript action attached to a page-open trigger). Tier 2 findings are structural: they identify a pattern that is consistent with concealment but admits a plausible benign explanation in some contexts (an /OpenAction that invokes a local /GoTo navigation is usually a publisher's default; overlapping text with different strings is usually OCR mis-segmentation). Tier 3 findings are interpretive: they identify signals that are suspicious in aggregate but not diagnostic on their own (capability-only invisible render mode regions, scan_error on a specific scanner path, mixed-script identifiers that are also dictionary words in one of the scripts). The reader composes these into a verdict; the scanner does not.

The same constraint rules out certain score dynamics. A scanner that reports integrity score 1.000 on a file that could not be fully parsed is telling a reader that the document displays and contains the same content, when in fact it did not display or contain anything legible to the scanner. That gap between the scanner's epistemic state and its reported score is itself a Gödel violation. The v0.1 scan_incomplete clamp (Section 9.1) closes this gap.

2.3 Minimum Description Length Discipline

Each detector is required to describe the smallest feature-set that fires on concealment and to assign severity proportional to the specificity of the feature for concealment versus benign uses. A detector that fires at sev 0.25 on a mechanism that fires 500 times in a benign Internet Archive OCR pipeline is not wrong in its per-finding claim but is wrong in its severity calibration; the signal it contributes to the aggregate score is dominated by a benign background. The v0.1 capability-only down-tier patch (Section 9.2) corrects exactly such a miscalibration: the mechanism (text render mode 3) is retained, the finding is retained, but the severity drops from 0.25 to 0.05 when the supporting feature (extracted text in the invisible region) is absent.

MDL discipline also constrains the shape of the roadmap. The scanner is hardened along the depth axis — calibrating existing detectors and filling catalog coverage gaps — before it is expanded along the breadth axis — adding new formats. Depth before scope is the feedback-memory-recorded policy and the reason v0.2 and v0.3 extend the PDF object-graph coverage before v0.4 begins DOCX support.

3\. v0 Architecture and Detector Inventory

Bayyinah v0 is a single-file Python 3.10+ implementation (bayyinah_v0.py, approximately 1,650 lines after v0.1 patches). The scanner has two primary modules — TextLayerScanner and ObjectLayerScanner — each of which produces a list of Finding objects that are merged, scored, and assembled into an IntegrityReport. External dependencies are limited to two PDF-parsing libraries: pymupdf (fitz) for page, content-stream, and text-layer access, and pypdf for catalog, trailer, and object-graph access. The dual-library design is deliberate: each library has its own bugs and blind spots, and their disagreement is itself a signal — a parse error on one path is emitted as a scan_error finding, which the scan_incomplete clamp (Section 9.1) then uses to gate the final score.

3.1 TextLayerScanner

Operates at the page and content-stream level. For each page, it walks the decoded content stream and reconstructs the sequence of text-rendering state transitions — font, size, color, transformation matrix, render mode — and records each Tj/TJ text-drawing operator against that state. It also inspects the extracted plain text for Unicode irregularities independently of the content-stream walk, because some concealment mechanisms (Unicode TAG substitution, zero-width joiner insertion) are visible in extracted text but are blind to content-stream introspection alone.

|                                         |          |          |         |                                                                                                          |
|-----------------------------------------|----------|----------|---------|----------------------------------------------------------------------------------------------------------|
| **Mechanism**                           | **Tier** | **Conf** | **Sev** | **What it detects**                                                                                      |
| invisible_render_mode (text extracted)  | 1        | 0.95     | 0.25    | Render mode 3 active and Tj/TJ operators draw text in the invisible region — genuine hidden-text payload |
| invisible_render_mode (capability only) | 3        | 0.60     | 0.05    | Render mode 3 armed but no Tj/TJ operators in the region — characteristic OCR-searchable-layer artifact  |
| white_on_white                          | 1        | 0.95     | 0.25    | Text run color within a small delta of the page background color                                         |
| microscopic_font                        | 2        | 0.85     | 0.20    | Font size below a legibility threshold (typically \< 2pt)                                                |
| off_page_text                           | 2        | 0.80     | 0.20    | Text positioned outside the visible MediaBox                                                             |
| zero_width_char                         | 1        | 0.95     | 0.25    | ZWSP, ZWNJ, ZWJ, or similar zero-width characters inside text runs                                       |
| unicode_tag_char                        | 1        | 0.95     | 0.30    | Unicode TAG characters (U+E0000..U+E007F) inside text                                                    |
| bidi_control                            | 2        | 0.80     | 0.20    | Bidi override characters (U+202A..U+202E, U+2066..U+2069)                                                |
| homoglyph_mixed_script                  | 2        | 0.75     | 0.20    | Identifiers or short strings mixing scripts where one script is a near-homoglyph for another             |
| overlapping_text                        | 2        | 0.75     | 0.25    | Two text spans sharing \>50% of a bounding box with different string content                             |
| tounicode_cmap_irregular                | 2        | 0.75     | 0.20    | Custom /ToUnicode CMap that maps glyphs to characters inconsistent with the encoding                     |

3.2 ObjectLayerScanner

Operates at the catalog and object-graph level. Walks the catalog's /AcroForm, /Names, /OpenAction, /AA, /OCProperties, /Threads, /EmbeddedFiles, and metadata entries, and inspects every cross-reference entry for incremental updates, encrypted streams, and filter-chain anomalies. The scanner also performs a raw-stream pass for Unicode TAG and zero-width characters in stream content, which catches payloads that evade the text-layer walk because they are embedded in XObject streams or form content streams not directly associated with visible text.

|                        |          |          |         |                                                                                          |
|------------------------|----------|----------|---------|------------------------------------------------------------------------------------------|
| **Mechanism**          | **Tier** | **Conf** | **Sev** | **What it detects**                                                                      |
| actualtext_mismatch    | 1        | 0.95     | 0.30    | /ActualText differs from the drawn glyph sequence — accessibility-layer concealment      |
| openaction_javascript  | 1        | 0.95     | 0.30    | Catalog /OpenAction with /S /JavaScript                                                  |
| openaction_launch      | 1        | 0.95     | 0.30    | Catalog /OpenAction with /S /Launch                                                      |
| openaction_goto        | 2        | 0.75     | 0.15    | Catalog /OpenAction with /GoTo — often a publisher default, retained as structural       |
| additional_actions     | 1        | 0.90     | 0.25    | Catalog-level /AA dictionary with triggers                                               |
| javascript_key         | 1        | 0.90     | 0.30    | Catalog /Names /JavaScript tree entry                                                    |
| launch_action          | 1        | 0.90     | 0.30    | Launch action with file specification                                                    |
| embedded_file          | 2        | 0.70     | 0.15    | /EmbeddedFile entries — material when combined with /OpenAction or /AA                   |
| hidden_ocg             | 2        | 0.75     | 0.20    | Optional content groups set to hidden by default state                                   |
| incremental_update     | 2        | 0.70     | 0.15    | Incremental update sections overriding prior declarations                                |
| raw_stream_unicode_tag | 1        | 0.95     | 0.30    | Unicode TAG characters found in raw stream content                                       |
| scan_error             | 3        | 0.50     | 0.00    | A scanner path could not complete; informational only, used by the scan_incomplete clamp |

3.3 Report assembly

Findings from both scanners are merged and passed to compute_integrity_score, which subtracts (severity × confidence) from an initial score of 1.0 and clamps the result to \[0.0, 1.0\]. A v0.1 post-processing step (Section 9.1) applies the scan_incomplete clamp when any scanner path emitted a scan_error finding or when a top-level error was set. The assembled IntegrityReport is serialized to either a human-readable text report or a JSON document; the JSON form is suitable for downstream automation.

4\. APS-Continuous Scoring Model

The integrity score is continuous in \[0.0, 1.0\] and is defined as:

integrity_score = clamp(1.0 − Σ (severity_i × confidence_i), 0.0, 1.0)

where the sum ranges over all findings. The choice of a continuous rather than binary scoring model is deliberate. A binary scanner (malicious / benign) forces a threshold decision that the scanner is not epistemically entitled to make; a continuous score preserves the signal and delegates the threshold to the reader or to a downstream policy engine. The choice of a multiplicative severity × confidence weighting is motivated by MDL: a low-confidence detector contributes proportionally less weight to the score than a high-confidence one, and the per-detector severity expresses the engineer's calibration of how specific the feature is to concealment.

The scoring model is rule-based and produces identical output on identical input. There is no learned component, no probabilistic classifier, and no language model in the scoring path. This is a security property: the scanner's behavior is auditable by reading the Python source and the SEVERITY and TIER dictionaries. It is also a deployment property: the scanner can be dropped into an air-gapped build pipeline and will behave deterministically.

The v0.1 scan_incomplete clamp is an additive constraint on top of the continuous score: whenever a scanner path could not complete, the score is clamped to ≤ 0.50 and a scan_incomplete flag is exposed at the top level of the report. This is a score-integrity property (Section 9.1), not a scoring-model change; it guarantees that incomplete coverage cannot be mistaken for cleanness.

5\. Positive-Control Validation

A synthesized positive-control PDF (positive_test.pdf) was constructed to carry nine concealment mechanisms spanning both scanner paths: text render mode 3 with extracted text, white-on-white, microscopic font, off-page text, zero-width joiner, Unicode TAG, /ActualText mismatch, catalog /OpenAction /JavaScript, and an /Annots-level structural entry. The scanner fires on all nine mechanisms (9/9 detection rate) and assigns a final integrity score of 0.000 after cumulative severity deduction. The inversion-recovery field reconstructs the concealed payload for each of the eight payload-bearing mechanisms. This is the positive-regression fixture: every modification to the scanner must preserve 9/9 detection and a final score of 0.000 on this file.

The v0.1 hardening patches — the scan_incomplete clamp and the capability-only down-tier — were both verified against the positive-control before release. The positive control parses cleanly (no scan_error, no top-level error), so the clamp does not trigger. Its invisible-render-mode finding carries extracted text, so it takes the Tier 1 / sev 0.25 branch, not the capability-only branch. Both invariants hold.

6\. Empirical Validation Against Wild Corpora

The scanner was evaluated against three wild corpora. The selection was deliberate: each corpus was expected to surface a different class of signal. Akira tested behavior against OCR-heavy scanned documents. Nausicaä tested behavior against producer-default image PDFs. The adversarial corpus tested behavior against actually-malicious and PDF-2.0-edge-case content. Each evaluation produced a per-file report and a corpus-level aggregate; the corpus aggregates are summarized here.

6.1 Akira corpus (six files)

Three scanned graphic-novel volumes (Akira Book 01, 02, 03) produced by the Internet Archive OCR pipeline, plus three analytical PDFs discussing those volumes.

|                            |           |              |                                                                   |
|----------------------------|-----------|--------------|-------------------------------------------------------------------|
| **File**                   | **Score** | **Findings** | **Dominant pattern**                                              |
| Akira Book 01.pdf          | 0.000     | 605          | 592 invisible_render_mode (capability only) + 13 overlapping_text |
| Akira Book 02.pdf          | 0.000     | 492          | 484 invisible_render_mode (capability only) + 8 overlapping_text  |
| Akira Book 03.pdf          | 0.000     | 476          | 448 invisible_render_mode (capability only) + 28 overlapping_text |
| Akira_Book_01_Analysis.pdf | 1.000     | 0            | Clean                                                             |
| Akira_Book_02_Analysis.pdf | 1.000     | 0            | Clean                                                             |
| Akira_Book_03_Analysis.pdf | 1.000     | 0            | Clean                                                             |

The three analytical PDFs scored 1.000 as expected — this is the negative-regression evidence that the scanner does not produce spurious findings on ordinary analytical documents. The three scanned volumes scored 0.000, driven by between 448 and 592 capability-only invisible_render_mode findings per book. Examination of the producer metadata (/Creator: Internet Archive, /Producer: Internet Archive PDF 1.4.25; including mupdf and pymupdf/skimage) identified the cause: the Internet Archive OCR pipeline overlays an invisible text layer (render mode 3) on top of scanned image pages so the volumes are searchable. The render-mode-3 capability is structurally present; no text is actually drawn in the invisible region; pymupdf's text-extraction on representative pages returns zero characters. The detector fired correctly by its own definition but at a severity that did not distinguish benign OCR artifact from genuine hidden-text payload. This motivated the v0.1 capability-only down-tier (Section 9.2).

6.2 Nausicaä corpus (eight files)

Eight parts of Nausicaä of the Valley of the Wind (Volumes 1 and 2, each split into four PDFs). All eight files are pure image PDFs with zero fonts and zero extracted text.

|                     |            |              |                                     |
|---------------------|------------|--------------|-------------------------------------|
| **File family**     | **Score**  | **Findings** | **Producer**                        |
| Naus-V1-A/B/C/D.pdf | 0.865 each | 1 each       | Adobe Acrobat 6.01 Image Conversion |
| Naus-V2-A/B/C/D.pdf | 0.865 each | 1 each       | Adobe Acrobat 6.01 Image Conversion |

All eight files received a uniform score of 0.865, driven by a single catalog-level /OpenAction /GoTo finding per file. The producer metadata (/Creator: Adobe Acrobat 6.01 Image Conversion Plug-in) identified the cause: the conversion plug-in emits a default /OpenAction /GoTo entry pointing to the first page as a navigation convenience. This is a benign producer-default pattern. The scanner's openaction_goto detector correctly flagged it at Tier 2 / confidence 0.75 / severity 0.15 — which is the MDL-calibrated signal that a /GoTo-typed /OpenAction is structurally present but not unambiguously adversarial. The uniform 0.865 score across the corpus is the signature of the pattern; an analyst who saw that signature on an ordinary image PDF would correctly attribute it to Adobe Acrobat's image-conversion plug-in and discount it.

6.3 Adversarial corpus (seventy-seven files)

An adversarial corpus was assembled from three sources: the AIGuardPDF sample-PDF.pdf (a published demonstration of AI prompt injection concealed in a benign-looking PDF), the pdf20examples-master repository (seven PDF 2.0 feature-demonstration files), and the malicious-pdf generator by Jonas Lejon (sixty-nine PDFs produced by running the generator against a callback URL). This is the primary positive-corpus evaluation and the source of the most consequential v0 findings.

6.3.1 AIGuardPDF sample-PDF.pdf

Score 0.000; 273 findings (128 white-on-white + 128 microscopic_font + 17 overlapping_text). The inversion-recovery field reconstructed the full hidden AI prompt text verbatim. This is the canonical true-positive validation: the mechanisms for which the scanner was designed fire on the mechanisms actually used in demonstrated adversarial content. The three gap-fill detectors added during v0 development (ToUnicode CMap analysis, homoglyph detection, overlapping_text) contributed 17 findings, one of which was the disambiguating signal that let the scanner reconstruct the prompt when portions were microscopic-overlapped.

6.3.2 PDF 2.0 edge-case corpus (seven files)

All seven files scored 1.000 with zero findings. These files demonstrate PDF 2.0 features (/AF associated files, object-stream encryption, new rendering intents) but do not themselves carry concealed content. The negative-regression property held here: the scanner did not produce false positives on a corpus of format-edge-case files that were not, themselves, adversarial.

6.3.3 malicious-pdf generator output (sixty-nine files)

The malicious-pdf generator was invoked with a https://example.invalid callback; all 69 testcases were produced. Results partitioned into five score bands:

|                       |           |                                                                                                        |
|-----------------------|-----------|--------------------------------------------------------------------------------------------------------|
| **Score**             | **Count** | **Pattern**                                                                                            |
| 0.000                 | 6         | Top-level error; fitz could not open — truly malformed container                                       |
| 0.703                 | 3         | Catalog /Names /JavaScript detected                                                                    |
| 0.865                 | 16        | Catalog /OpenAction detected                                                                           |
| 0.873                 | 2         | Catalog-level /AA detected                                                                             |
| 1.000 with scan_error | 23        | Silent scanner-path failure; before v0.1, these scored as clean                                        |
| 1.000 (true miss)     | 17        | No findings at all; attack is attached at the annotation level or in form/XMP content not walked by v0 |

Two distinct problem classes emerged. The first — the silent-scan_error problem — is a score-integrity bug: 23 malicious files caused pypdf to throw on catalog walk; the scanner emitted a scan_error finding at Tier 3 / severity 0.00 (informational only, by design) but continued the text-layer scan and produced no other findings, leaving the aggregate score at 1.000. A malicious file that causes a scanner path to fail and is then rendered as “integrity 1.000” is a score that does not reflect the scanner's own epistemic state. The v0.1 scan_incomplete clamp (Section 9.1) closes this bug.

The second — the annotation-level coverage gap — is a detection-engineering gap rather than a score-integrity bug. The 17 true-miss files do not cause any scanner path to fail; they carry their action dictionaries inside an annotation's /A or /AA entry (not the catalog's), or inside an XFA dynamic form, or inside an /AF associated-file reference (PDF 2.0), or inside an XMP metadata block with an XXE DOCTYPE. The v0 object-layer walker visits the catalog; it does not recursively visit /Annots\[i\]/A or /Annots\[i\]/AA. The v0.2 roadmap (Section 11.1) closes this gap with explicit annotation-level detectors.

7\. Cross-Corpus Synthesis

Taken together, the three wild corpora produced three categorically distinct signatures — one per corpus — that the scanner's tier/confidence/severity tuples and inversion-recovery text make legible in the report, even when the aggregate score alone does not distinguish them.

|                          |                    |                      |                    |                                          |
|--------------------------|--------------------|----------------------|--------------------|------------------------------------------|
| **Corpus**               | **Class**          | **Score range**      | **Finding volume** | **Dominant mechanism**                   |
| Akira (scans)            | OCR noise          | 0.000                | 476–605 per file   | invisible_render_mode (capability)       |
| Akira (analyses)         | Clean              | 1.000                | 0                  | —                                        |
| Nausicaä                 | Benign /OpenAction | 0.865 uniform        | 1 per file         | openaction_goto                          |
| AIGuardPDF               | True positive      | 0.000                | 273                | white_on_white + microscopic             |
| pdf20examples            | Edge case (clean)  | 1.000                | 0                  | —                                        |
| malicious-pdf (detected) | Active JS/AA       | 0.703–0.873          | 2–3 per file       | openaction/javascript/additional_actions |
| malicious-pdf (miss)     | Annotation gap     | 1.000 → 0.500 (v0.1) | 0–1 per file       | scan_error (silent)                      |

The observation that the Nausicaä and malicious-pdf-detected corpora overlap in score range (0.865 across both) but are categorically different — a benign producer default in one case, an active catalog-level attack dictionary in the other — is a feature of the scoring model, not a flaw. The score is an integer of information content; the mechanism name and inversion-recovery field are the disambiguating signal. A downstream policy engine that triaged on score alone would miss the distinction; a reader who reads the finding list sees it immediately. This is the Gödel constraint operating as designed: the scanner preserves information rather than collapsing it into a verdict.

8\. False-Positive Taxonomy

Three false-positive classes were observed across the corpora. Each is a class — not an individual finding — and each motivated a specific v0.1 correction or a v0.2+ roadmap item.

8.1 Class A: OCR noise floor

Signature: hundreds of invisible_render_mode findings per file, all with inversion-recovery text “(capability only; no text drawn)”, concentrated in image-bearing pages of a file whose producer metadata identifies an OCR pipeline (Internet Archive, Abbyy FineReader, Tesseract wrapper). Root cause: OCR pipelines use render-mode-3 to overlay a searchable text layer on top of scanned image pages; the capability is structurally present without a concealment payload. v0.1 correction: capability-only down-tier (Section 9.2) moves this finding from Tier 1 / sev 0.25 to Tier 3 / sev 0.05, a 5× reduction in per-finding score contribution. The detector still fires (the capability is real); the score no longer treats it as equivalent to a genuine hidden-text payload.

8.2 Class B: Benign producer-default /OpenAction

Signature: a single openaction_goto finding at Tier 2, uniform across a corpus of files produced by the same image-conversion tool. Root cause: Adobe Acrobat's image-conversion plug-in emits a default /OpenAction /GoTo pointing to page 1 as a navigation convenience. The /GoTo subtype is structurally a navigation action, not an executable or scripting action. v0 treatment: openaction_goto is already Tier 2 / confidence 0.75 / severity 0.15 (weaker than openaction_javascript or openaction_launch at Tier 1 / sev 0.30), which correctly down-weights it relative to active-attack variants. No v0.1 correction required. v0.2 consideration: a producer-default suppression heuristic may be added as a Tier-4 informational note, but only if the pattern is demonstrated to be stable across a larger sample; for now, the uniform 0.865 signature is itself legible to a practitioner.

8.3 Class C: Single-character overlapping_text on sound-effect pages

Signature: a handful of overlapping_text findings per file, concentrated on pages containing stylized large-font lettering (manga sound effects, graphic-novel signage), with inversion-recovery pairs like “aI ↔ —” or “YN ↔ 2)” — single characters or short fragments, evidently the output of an OCR engine that produced multiple competing hypotheses for the same pixel region. Root cause: OCR mis-segmentation on stylized or decorated text produces overlapping bounding boxes with different string content. v0 treatment: the detector is Tier 2 / confidence 0.75, which is already calibrated as structural-not-verified. v0.3 consideration: a minimum-string-length gate (ignore overlaps where both strings are \< 3 characters) would suppress most of these without affecting AIGuardPDF-class overlapping_text findings, which are multi-word fragments.

9\. v0.1 Hardening Patches

Two patches were applied to v0 after the wild-corpus evaluation. Each is strictly rule-based, touches a single conditional in the report-assembly or detector-creation path, and was regression-tested against every corpus.

9.1 scan_incomplete clamp

Problem: 23 files in the malicious-pdf corpus caused pypdf to throw on the catalog walk; the scanner emitted a scan_error finding at Tier 3 / severity 0.00 and continued, but because the severity was 0.00 (informational only, by design), the aggregate score remained at 1.000. Files that the scanner could not fully parse were being reported as integrity-perfect.

Fix: a single post-assembly conditional in scan_pdf(). Whenever any scanner path emitted a scan_error finding or a top-level error field was set, the report is flagged with a boolean scan_incomplete: true key (exposed at the top level of the JSON report, immediately after integrity_score) and the integrity_score is clamped to a maximum of 0.500. The scan_error finding itself remains at Tier 3 / sev 0.00 — the scoring change is applied at the report level, not the finding level, so the SEVERITY and TIER dictionaries were not disturbed. The plain-language summary prepends an explicit note whenever the flag is true: “one or more scanner paths reported an error or could not complete … absence of findings in the uninspected regions cannot be taken as evidence of cleanness”.

Regression result: the 23 silent-scan_error files moved from 1.000 to 0.500 with scan_incomplete: true. Clean analytical PDFs, AIGuardPDF, Akira books, Nausicaä files, and the positive test were all unchanged.

9.2 Capability-only invisible_render_mode down-tier

Problem: the Akira graphic-novel scans produced 476 to 605 findings per file, all at Tier 1 / severity 0.25. The per-finding severity did not distinguish the OCR-noise variant (render-mode-3 armed without text drawn) from the genuine hidden-payload variant (render-mode-3 armed with extracted text).

Fix: a single modification inside the TextLayerScanner's invisible-region enumeration branch. When the region contains no Tj/TJ operators and therefore no extracted text, the Finding is created with tier=3 and severity_override=0.05 rather than the default tier=1 / severity=0.25. An optional severity_override field was added to the Finding dataclass; when set, it takes precedence over the SEVERITY dictionary lookup. The mechanism name remains invisible_render_mode, so the finding count and mechanism taxonomy are unchanged — only the weight changes.

Regression result: Akira per-finding contributions dropped from 0.150 (= 0.25 × 0.60) to 0.030 (= 0.05 × 0.60), a 5× reduction. Aggregate scores still floored to 0.000 because the number of findings per book exceeds the 0.030 × n that would be required to lift the score above 0 (roughly 600 × 0.030 = 18 points of deduction), but the per-finding MDL weight is now correctly calibrated. Analytical PDFs, Nausicaä, AIGuardPDF, and the positive test were all unchanged: AIGuardPDF's invisible_render_mode findings take the IF branch (extracted text present) and remain at Tier 1 / sev 0.25; Nausicaä carries no invisible_render_mode findings; the positive-test fixture's invisible_render_mode finding also carries extracted text.

10\. Limitations

Three classes of limitation are documented here; each is closed by a specific item on the roadmap.

10.1 Format coverage

v0 addresses PDF only. DOCX, HTML, Markdown, JSON, images, and source code are all in scope for the scanner's stated mission but are not implemented. The v0.4 (DOCX) and v1.0 (HTML/MD/JSON/images/code) roadmap items close this.

10.2 PDF attack-surface depth

The v0 object-layer walker is catalog-scoped. Annotation-level /A and /AA dictionaries, XFA dynamic forms, RichMedia /Configuration scripts, /AF (associated files, PDF 2.0), XMP metadata XXE, and PostScript-injection streams are not inspected. The adversarial corpus surfaced 17 true-miss files concentrated in this attack surface. The v0.2 (annotations) and v0.3 (form/XMP/AF) roadmap items close this.

10.3 Score-dimension limitations

The integrity score is a scalar; it does not distinguish, in its numeric value alone, between a benign producer-default openaction_goto (Nausicaä) and an active catalog-level attack (malicious-pdf openaction). The mechanism name and inversion-recovery field preserve the distinction, but a downstream consumer that triages on score alone will conflate the classes. A v1.0 item is a structured multi-axis score (separate layers for text-concealment, object-level action, and coverage-completeness) that preserves the scalar for legacy consumers while exposing the axes for richer policy.

11\. Roadmap

The roadmap is organized depth-before-scope. v0.2 and v0.3 harden PDF attack-surface coverage; v0.4 is the first non-PDF format; v1.0 is a unified multi-format release with a content-signed attestation format. Each sub-section below lists the concrete detectors, their tier and severity assignments, and the specific adversarial-corpus evidence that motivates them.

11.1 v0.2 — Annotation-level attack surface

Closes: 7 of the 17 malicious-pdf true misses (test5, test18, test19, test20, test26, test28, test43). Expected effect on the adversarial corpus: each of these files acquires at least one Tier 1 or Tier 2 finding, moving from 1.000 to between 0.15 and 0.85 depending on the action subtype.

|                                  |          |          |         |                                                                                   |
|----------------------------------|----------|----------|---------|-----------------------------------------------------------------------------------|
| **Detector**                     | **Tier** | **Conf** | **Sev** | **What it fires on**                                                              |
| annot_action_javascript          | 1        | 0.95     | 0.30    | /Annots\[i\]/A/S = /JavaScript                                                    |
| annot_action_launch              | 1        | 0.95     | 0.30    | /Annots\[i\]/A/S = /Launch                                                        |
| annot_action_uri_suspicious      | 2        | 0.80     | 0.20    | /Annots\[i\]/A/S = /URI with file://, javascript:, or ftp: scheme                 |
| annot_action_importdata          | 2        | 0.80     | 0.20    | /Annots\[i\]/A/S = /ImportData                                                    |
| annot_aa_pagevisible             | 1        | 0.90     | 0.25    | /Annots\[i\]/AA/PV — page-visible trigger                                         |
| annot_aa_pageclosed              | 1        | 0.90     | 0.25    | /Annots\[i\]/AA/PC — page-closed trigger                                          |
| annot_aa_mouseenter              | 1        | 0.85     | 0.20    | /Annots\[i\]/AA/E — mouse-enter trigger                                           |
| annot_aa_mousedown               | 1        | 0.85     | 0.20    | /Annots\[i\]/AA/D — mouse-down trigger                                            |
| annot_subtype_screen_with_action | 1        | 0.90     | 0.25    | /Subtype /Screen with any /A or /AA — rendering-annotation used as action carrier |
| annot_subtype_widget_with_js     | 1        | 0.90     | 0.25    | /Subtype /Widget with /A /S /JavaScript and no visible field                      |

11.2 v0.3 — Form, embedded-file, and XMP coverage

Closes: the remaining 10 of 17 malicious-pdf true misses (test7, test9, test30, test34_1, test36, test37, test39, test40, test42, test47). Also covers PDF 2.0 /AF attack surface.

|                           |          |          |         |                                                                         |
|---------------------------|----------|----------|---------|-------------------------------------------------------------------------|
| **Detector**              | **Tier** | **Conf** | **Sev** | **What it fires on**                                                    |
| xfa_dynamic_present       | 2        | 0.75     | 0.15    | /AcroForm/XFA dictionary present — structural context                   |
| xfa_doctype_xxe           | 1        | 0.95     | 0.35    | XFA XML stream contains DOCTYPE/ENTITY declarations                     |
| xfa_oob_xxe               | 1        | 0.95     | 0.40    | XFA XXE with out-of-band SYSTEM identifier (http/ftp URL)               |
| af_with_launch            | 1        | 0.95     | 0.30    | /AF entry referencing an embedded file with /Launch or /JavaScript      |
| richmedia_config_script   | 1        | 0.95     | 0.30    | /RichMedia /Configuration with /Script entry                            |
| xmp_doctype_xxe           | 2        | 0.85     | 0.25    | XMP metadata stream contains DOCTYPE/ENTITY declarations                |
| xmp_oob_xxe               | 1        | 0.90     | 0.30    | XMP XXE with SYSTEM http/ftp URL                                        |
| gotor_external_executable | 2        | 0.80     | 0.20    | /GoToR with /F referencing .exe, .bat, .js, .dll                        |
| uri_hijack                | 2        | 0.75     | 0.20    | /URI action using unusual schemes (data:, vbscript:, res:)              |
| postscript_launch         | 2        | 0.80     | 0.20    | PostScript stream with /Launch or /OpenAction sub-object                |
| xobj_stream_js            | 1        | 0.90     | 0.30    | XObject stream content contains JavaScript operator sequences           |
| xref_stream_anomaly       | 3        | 0.65     | 0.15    | Cross-reference stream with irregular Index/Size or overlapping entries |

11.3 v0.4 — DOCX parity

First non-PDF format. DOCX is the natural second target because it shares the multi-layer-content property with PDF (display layer, comment layer, tracked-change layer, content-control layer, embedded-object layer, macro layer, metadata) and because OOXML is a ZIP archive that admits direct XML inspection without a PDF-style object graph.

|                                 |          |          |         |                                                                                |
|---------------------------------|----------|----------|---------|--------------------------------------------------------------------------------|
| **Detector**                    | **Tier** | **Conf** | **Sev** | **What it fires on**                                                           |
| docx_invisible_color_text       | 1        | 0.95     | 0.25    | Run \<w:color\> matching page background or w:vanish=“true”                    |
| docx_zero_size_font             | 1        | 0.95     | 0.25    | Run \<w:sz\> ≤ 2 half-points                                                   |
| docx_content_control_divergence | 1        | 0.90     | 0.25    | Structured-Document-Tag display text differs from bound XML content            |
| docx_macro_present              | 1        | 0.95     | 0.30    | vbaProject.bin present in the archive                                          |
| docx_macro_autoexec             | 1        | 0.95     | 0.35    | vbaProject.bin with AutoExec/AutoOpen/Document_Open/Workbook_Open handlers     |
| docx_ole_object                 | 2        | 0.85     | 0.25    | w:object / oleObject relationship with executable content                      |
| docx_external_template          | 2        | 0.80     | 0.25    | settings.xml /Template referencing external URL (remote template injection)    |
| docx_external_data_binding      | 2        | 0.80     | 0.20    | customXml external data binding                                                |
| docx_xxe_doctype                | 1        | 0.95     | 0.35    | DOCTYPE/ENTITY declarations inside any XML part                                |
| docx_tracked_change_concealment | 2        | 0.75     | 0.20    | Tracked-change insertion/deletion containing invisible-attribute runs          |
| docx_header_footer_alt_content  | 2        | 0.70     | 0.15    | Header/footer content not rendered on the displayed page (alternative content) |

11.4 v1.0 — Multi-format with attestation

First release with HTML, Markdown, JSON, image, and source-code coverage, plus a content-signed attestation format.

11.4.1 HTML and Markdown

|                               |          |          |         |                                                                        |
|-------------------------------|----------|----------|---------|------------------------------------------------------------------------|
| **Detector**                  | **Tier** | **Conf** | **Sev** | **What it fires on**                                                   |
| html_css_display_none_text    | 2        | 0.80     | 0.20    | Text within display:none or visibility:hidden with substantive content |
| html_font_size_zero           | 1        | 0.95     | 0.25    | Text with font-size:0 or opacity:0                                     |
| html_color_matches_background | 1        | 0.90     | 0.25    | Color within small delta of background                                 |
| html_bidi_override            | 1        | 0.95     | 0.30    | RLO/LRO/RLE/LRE/FSI/PDI around anchors or URLs                         |
| html_meta_refresh_redirect    | 2        | 0.75     | 0.20    | meta http-equiv=refresh to external URL                                |
| html_homoglyph_url            | 1        | 0.90     | 0.30    | Anchor href with mixed-script homoglyph domain                         |
| html_data_uri_script          | 2        | 0.85     | 0.25    | data: URI containing base64-encoded executable content                 |
| html_zero_width_in_text       | 1        | 0.95     | 0.25    | ZWSP/ZWNJ/ZWJ/Unicode TAG chars in visible text                        |
| md_html_block_with_script     | 2        | 0.80     | 0.20    | Raw HTML block containing \<script\>, \<iframe\>, or on-event handler  |
| md_invisible_link_text        | 2        | 0.75     | 0.20    | Link text containing zero-width or TAG characters                      |

11.4.2 JSON

|                                    |          |          |         |                                                                                                     |
|------------------------------------|----------|----------|---------|-----------------------------------------------------------------------------------------------------|
| **Detector**                       | **Tier** | **Conf** | **Sev** | **What it fires on**                                                                                |
| json_duplicate_keys                | 1        | 0.95     | 0.30    | Same key appearing twice in the same object (RFC 8259 SHOULD-NOT but parser-dependent)              |
| json_control_chars_in_string       | 1        | 0.95     | 0.25    | Control characters (U+0000..U+001F, excluding standard escapes) in string values                    |
| json_tag_chars_in_value            | 1        | 0.95     | 0.30    | Unicode TAG characters in string values                                                             |
| json_base64_payload_custom_charset | 2        | 0.75     | 0.20    | Base64-looking value using non-standard alphabet                                                    |
| json_key_order_exploitation        | 2        | 0.70     | 0.15    | Key order that produces different results across canonicalization rules (related to duplicate keys) |

11.4.3 Images

|                               |          |          |         |                                                                                                   |
|-------------------------------|----------|----------|---------|---------------------------------------------------------------------------------------------------|
| **Detector**                  | **Tier** | **Conf** | **Sev** | **What it fires on**                                                                              |
| img_exif_text_instruction     | 2        | 0.75     | 0.20    | EXIF Comment, UserComment, or ImageDescription fields containing prose instruction text           |
| img_lsb_entropy_anomaly       | 3        | 0.65     | 0.15    | Least-significant-bit plane entropy inconsistent with image content (LSB steganography signature) |
| img_qr_or_datamatrix_embedded | 2        | 0.75     | 0.20    | QR or DataMatrix payload detected in a low-contrast region                                        |
| img_trailing_data_after_eof   | 1        | 0.90     | 0.25    | Bytes after the image file's declared EOF (appended-content carrier)                              |
| img_polyglot_signature        | 1        | 0.95     | 0.30    | File signatures of two or more formats (e.g., JPEG + ZIP)                                         |
| img_icc_profile_payload       | 3        | 0.60     | 0.15    | ICC profile larger than threshold or containing non-profile bytes                                 |

11.4.4 Source code

|                                   |          |          |         |                                                                             |
|-----------------------------------|----------|----------|---------|-----------------------------------------------------------------------------|
| **Detector**                      | **Tier** | **Conf** | **Sev** | **What it fires on**                                                        |
| code_trojan_source_bidi           | 1        | 0.98     | 0.35    | Bidi override characters in source (CVE-2021-42574)                         |
| code_invisible_char_in_identifier | 1        | 0.95     | 0.30    | Zero-width or TAG characters inside an identifier token                     |
| code_homoglyph_identifier         | 1        | 0.90     | 0.30    | Identifier tokens using mixed-script homoglyphs of a builtin name           |
| code_whitespace_only_subfield     | 2        | 0.75     | 0.15    | Structural whitespace in string literals containing invisible control chars |
| code_eval_obfuscated_base64       | 2        | 0.80     | 0.25    | eval/exec/Function/setTimeout applied to base64-decoded content             |
| code_large_commented_binary_blob  | 3        | 0.65     | 0.15    | Contiguous commented base64/hex block larger than threshold                 |

11.4.5 Content-signed attestation

A v1.0 deliverable independent of any specific format: a signed attestation JSON that binds an integrity_score to a cryptographic hash of the file at scan time. The attestation is a self-contained record — { tool, version, scanned_at, file_sha256, integrity_score, findings_digest, scan_incomplete, signature } — that a downstream consumer can verify before trusting the score. This closes the upstream attack of substituting a benign report for the one actually produced against the malicious file. The attestation format is a plain-text signed JSON (Ed25519 recommended); the signing key is operator-managed; the verification is a pure cryptographic operation that does not require re-scanning the file.

12\. Threat Model and Deployment

Bayyinah v0 is designed for integration into a file-ingestion pipeline upstream of content processing: before the file is OCR'd, before it is parsed by an LLM, before its text is embedded for retrieval. The scanner's output is advisory to that pipeline: a score below a configurable threshold (or a scan_incomplete=true flag) triggers a policy decision — route to a human reviewer, quarantine, or refuse. Bayyinah is not a replacement for an AV engine, a DLP scanner, or a sandbox detonation service; it is a specific signal about the gap between a file's display and its contents, and it is meant to sit alongside those tools in a layered defense.

The threat model is deliberately narrow: adversaries who craft files that pass a human reader's visual inspection and a naïve text-extraction pipeline's checks but carry payload in one of the concealment layers the scanner inspects. The scanner does not, and is not intended to, detect polymorphic executable payloads, signed-but-malicious binaries, runtime behavioral anomalies, or concealment mechanisms in formats the scanner does not parse. The Gödel constraint extends to this: the scanner does not claim coverage it does not have. Files processed with scan_incomplete=true should be treated as out-of-coverage rather than clean.

13\. References

- Munafiq Protocol. Zenodo, 2026. DOI: 10.5281/zenodo.19677111.

- Adobe Systems Inc. PDF Reference, Sixth Edition, Version 1.7. November 2006 (ISO 32000-1:2008).

- ISO 32000-2:2020. Document management — Portable document format — Part 2: PDF 2.0.

- Boucher, N., and Anderson, R. Trojan Source: Invisible Vulnerabilities. arXiv:2111.00169 (CVE-2021-42574).

- Lejon, J. malicious-pdf: generates a collection of ten different malicious PDF files. GitHub: jonaslejon/malicious-pdf.

- PDF Association. pdf20examples: PDF 2.0 example files. GitHub: pdf-association/pdf20examples.

- AIGuardPDF demonstration corpus. Referenced at the source provided with the sample-PDF.pdf artifact used in Section 6.3.1.

- pymupdf (fitz): Artifex Software, Inc. GitHub: pymupdf/PyMuPDF.

- pypdf: py-pdf contributors. GitHub: py-pdf/pypdf.

- RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format. Bray, T. (Ed.), IETF, 2017.

- Gödel, K. Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I. Monatshefte für Mathematik und Physik, 38, 173–198, 1931.

Appendix A: Per-Finding JSON Schema

{

"tool": "bayyinah",

"version": "0.1.0",

"file_path": "/path/to/file.pdf",

"integrity_score": 0.500,

"scan_incomplete": true,

"verdict_disclaimer": "This report presents observed mechanisms ..."

"tier_legend": { "1": "Verified", "2": "Structural", "3": "Interpretive" },

"findings": \[

{

"mechanism": "invisible_render_mode",

"tier": 3,

"confidence": 0.6,

"severity": 0.05,

"description": "Content stream activates text render mode 3 ...",

"location": "page 7",

"inversion_recovery": {

"surface": "(nothing visible)",

"concealed": "(capability only; no text drawn)"

}

}

\],

"error": null

}

Appendix B: Reproducing the Empirical Evaluation

The scanner is a single file. Invocation against a single PDF:

python3 bayyinah_v0.py /path/to/file.pdf \# human-readable text report

python3 bayyinah_v0.py --json /path/to/file.pdf \# JSON report

The corpora used in Section 6 are documented in the three wild-corpus evaluation reports (wild_corpus_evaluation_akira.md, wild_corpus_evaluation_nausicaa.md, wild_corpus_evaluation_adversarial.md). The malicious-pdf generator is invoked as:

python3 malicious-pdf.py https://example.invalid --output-dir ./corpus --no-credit

and produces 69 testcases plus one SVG. Reproducing Section 9 regression requires the scanner and the three corpora; scores should match those reported in Section 9.1 and 9.2 exactly, subject to pymupdf and pypdf version variance.

Closing

Bayyinah v0 is an honest tool: it surfaces mechanisms and presents the surface-versus-concealed divergence that characterizes each; it does not claim a verdict it cannot make; and it records its own epistemic limits in the scan_incomplete flag and the Tier 3 tiers it uses for interpretive findings. The empirical evaluation surfaced both a score-integrity bug and a calibration correction, each of which was closed in v0.1 with a single conditional, regression-verified across 91 files. The roadmap extends both the depth of PDF coverage and the breadth of supported formats, with per-detector tier and severity assignments derived from the wild-corpus evidence. The scanner's value is not that it makes the verdict: it is that it makes the invisible visible, and leaves the recognition to the reader.

The scanner's technical honesty -- surfacing mechanisms, recording epistemic limits, refusing verdicts it cannot make -- is a consequence of the purpose hierarchy that governs the project. Bayyinah serves the command to not mix truth with falsehood (2:42) first. It serves the protection of artificial systems, mankind, jinnkind, and all living systems throughout the worlds second through fifth. The technical integrity is the implementation of that service. Every finding that names its mechanism and states its confidence is an act of not concealing the truth while knowing it. Every scan_incomplete flag that refuses to assert cleanliness on a document the scanner could not fully read is an act of epistemic humility before the Incompleteness Boundary and before the One who encompasses all knowledge.

*Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim. Our Lord, accept from us. Indeed, You are the All-Hearing, the All-Knowing.*

---

# Bismillah ir-Rahman ir-Rahim
