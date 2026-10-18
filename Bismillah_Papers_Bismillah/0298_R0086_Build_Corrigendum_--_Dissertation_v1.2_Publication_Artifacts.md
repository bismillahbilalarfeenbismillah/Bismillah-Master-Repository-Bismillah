# Bismillah ir-Rahman ir-Rahim

# R0086 -- Build Corrigendum -- Dissertation v1.2 Publication Artifacts (July 22, 2026)

**Chronological Index:** 298 of 995  
**Date:** 2026-07-22  
**Section:** III. Structural Honesty — Core Papers  
**Source File:** BUILD_CORRIGENDUM_2026-07-22.md  
**Source Format:** md  
**SHA-256:** `c8dc038d76343096da533f3b32257e35a1b1ae46aab5731bf251d969915fb274`  

---

## R0086 · Build Corrigendum -- Dissertation v1.2 Publication Artifacts (July 22, 2026)

- section: III. Structural Honesty — Core Papers
- source_file: BUILD_CORRIGENDUM_2026-07-22.md
- source_format: md
- text_sha256: c8dc038d76343096da533f3b32257e35a1b1ae46aab5731bf251d969915fb274

# Build Corrigendum -- Dissertation v1.2 Publication Artifacts (July 22, 2026)

## Finding SOL-R1 (external review, GPT-5.6 Sol via ChatGPT)

The initially shipped v1.2 publication PDF (superseded; zip SHA-256 prefix 93fe814c5645..., full value in session ledger; PDF 360 pp)

exhibited a chapter-projection failure: the page rendered under the number 8 carried Chapter 9's
status block and self-references; Chapter-8 (Integrative Evaluation) material ran under the
Chapter-7 running header; raw '#' heading markers and mangled table-like text appeared in the
Chapter-8 region. For a dissertation whose Axiom 4 is projection consistency, the rendered
navigation diverging from underlying chapter identity is an Axiom-4-class failure in the
publication projection. Severity for the derived artifact: HIGH (navigation-breaking).
The frozen canon substrate was never affected.

## Root causes (two, both parser interactions -- canon substrate untouched and re-verified)

1. **Mid-document YAML metadata block capture.** The canon separates chapter status blocks with
   `---` horizontal-rule lines. pandoc's default `yaml_metadata_block` extension interprets a
   blank-line-preceded `---` span as a YAML metadata block; Chapter 9's opener (`---` /
   `# heading` -- a YAML comment / `**Status: ...` / ... / `---`) triggered capture attempts,
   corrupting sectioning, running headers, and emitting partially-consumed markdown as literal
   text (the raw '#' markers and pseudo-table wreckage).
2. **Missing blank line before one chapter heading.** The Chapter-8 marker is the single site in
   the 5,600-line body where `---` is immediately followed by the `#` heading with no blank line;
   pandoc's default `blank_before_header` therefore did not recognize that one heading, which is
   why exactly one chapter was swallowed and all subsequent numbering shifted.

## Build-layer fixes (derived-artifact transformations; deterministic; canon frozen)

1. Body parsed with `--from markdown-yaml_metadata_block` (extension disabled); document metadata
   supplied solely via `--metadata-file`.
2. Whitespace normalization: a blank line inserted before any ATX heading lacking one
   (exactly 1 site: the Chapter-8 marker). Content-neutral.
3. Appendix lettering forced to match internal identity: `\appendix` + `\setcounter{chapter}{3}`
   so the two appendix chapters render as Appendix D (Standing Rulings Register) and Appendix E
   (Publication History) as the council designation and internal text state -- book-class default
   would have lettered them A/B, a second latent projection mismatch.
4. `pagestyle: headings` set explicitly (running chapter headers restored) and longtable relief
   added to the preamble (etoolbox + \small in longtable).

## Canon corrigendum candidate (queued, NOT applied -- version discipline)

The canon-side irregularity behind root-cause 2 (inconsistent blank-line convention at the
Chapter-8 join, canon.md L1499 region) is queued as a LOW formatting corrigendum for the next
authorized canon version. It is build-blocking only; no content defect.

## Verification (scripted harness, corrected artifacts)

23/23 chapters verified: displayed "Chapter N" adjacent to the expected title; order monotone;
Appendix D and E verified; zero literal '#' heading lines in the text layer; Chapter 9's status
block ("Full Chapter 9 assembled") located inside displayed Chapter 9; Chapter 15's
("full-chapter-canon version of Chapter 15") inside displayed Chapter 15; running headers present
and tracking (26 header lines across Chapter 8's span, 13 across Chapter 9's). Page count
360 -> 371 (recovered chapter-opening structure). Canon SHA-256 re-verified unchanged:
38dfa91dcae27ba5d90a07c3acb1d6719d96b5a351e5f1c4c2502f7038490eca (full value in SHA256SUMS-equivalent below).

## Superseded and current hashes

Superseded: prior Structural_Honesty_Dissertation_v1_2.zip (SHA-256 prefix 93fe814c5645..., session-ledger record) and its PDF/DOCX/HTML members.
PDF/DOCX/HTML members. Current member hashes accompany this corrigendum in the refreshed zip.
Pre-existing non-blocking warnings unchanged: 3x duplicate footnote reference '[^1]' (body lines
408 / 1824 / 3142) -- queued with the I-30-class hygiene items.

## Addendum (publication kit, July 23): front-matter author note

Retroactive application of the AUTHOR-NOTE-RENDER-PARITY standing gate (adopted during the
flagship v0.12 cycle, where the note's absence from renders was rated HIGH): the dissertation
renders carried no reader-facing AI-collaboration disclosure. A one-sentence author note is
added at the build layer immediately before the Abstract, pointing to the audit ledger and
Appendix E for the full lineage enumeration. The canon is untouched (SHA-256 re-verified
38dfa91d...); this is a documented derived-artifact transformation in the same class as the
SOL-R1 build fixes above. Renders rebuilt; chapter-identity harness, META-TEXT-ABSENCE gate,
attribution-parity check, and chromatic scan re-run against the rebuilt artifacts.

## Correction to the July-23 addendum (page count)

The July-23 addendum failed to update the stated page count: after the author-note insertion
the v1.2 PDF was 372 pages, not 371. Producer-owned count miss, caught by external
(Perplexity) review.

## v1.3 build note (July 23)

Typography matched to the flagship publication profile: Latin Modern at the flagship's
10pt/12pt metrics (classoption 10pt), letter geometry, all-black. Engine: xelatex is
REQUIRED for this volume -- the canon carries transliteration and notation codepoints
(dot-below consonants, combining macrons, arrows, Greek capitals) outside pdflatex's
default coverage; the font family is identical to the flagship's, with the engine
difference disclosed here. Book class retained for the 23-chapter structure (the flagship
is a single-article layout; "same structure" is implemented as same type family, size,
margins, page stock, and link suppression). Page count at v1.3: 324.

---

# Bismillah ir-Rahman ir-Rahim
