# Bismillah ir-Rahman ir-Rahim

# Deep Read Report -- Section VII-B: Software Tools (Batch 2)
## Papers Read: 27

## Total Size: 266,097 characters across 6,861 lines

---

## Per-Paper Summaries

### R0505 -- effect-request.schema.json.txt
- **Date:** Undated
- **Source:** effect-request.schema.json.txt
- **Size:** 148 lines, 4,750 chars
- **SHA-256:** `7885bac402e9d58d...`

**Key Concepts:** BSSG, DRAFT, ONLY, MUST NOT, NOT CARRIED, CANON, MUST, FALSE, UNKNOWN, SHA

**Content Summary:**
- source_format: txt - text_sha256: 7885bac402e9d58d2ca07823cdfa5e3dd70e68078dff9d4ef4512f8f33acd280
{ "$schema": "https://json-schema.org/draft/2020-12/schema", "$id": "urn:bssg:schema:0.1:effect-request", "title": "BSSG effect request (v0.1 DRAFT)", "description": "A request by a subject for a consequential effect. This record carries ONLY raw evidence and declarations. It MUST NOT carry any derived authorization fact: no decision, no conjunct value, no 'verified' or 'within_auth' flag. A gate that accepts such a field from a caller has surrendered authority to the caller. Status: DRAFT, NOT CARRIED. No effectiveness claim attaches to this schema.", "type": "object", "additionalProperties": false, "required": [ "record_type", "spec_version", "request_id", "subject_id", "session_id", "con...

---

### R0506 -- execution-receipt.schema.json.txt
- **Date:** Undated
- **Source:** execution-receipt.schema.json.txt
- **Size:** 214 lines, 5,487 chars
- **SHA-256:** `398741899bf781f9...`

**Key Concepts:** BSSG, DRAFT, MUST, INDETERMINATE, MUST NOT, NOT CARRIED, COMMITTED, PENDING, OUTCOME, SUCCEEDED

**Content Summary:**
- source_format: txt - merged_variants: 1 (execution-receipt.schema.json) - text_sha256: 398741899bf781f927c8e7269abeb0f7029ac4f3399a18a4fd4a8ef7d9b419cb
{ "$schema": "https://json-schema.org/draft/2020-12/schema", "$id": "urn:bssg:schema:0.1:execution-receipt", "title": "BSSG execution receipt (v0.1 DRAFT)", "description": "The record of a commit attempt. Commit is the point at which a one-time token is redeemed under compare-and-swap and all bindings and epochs are revalidated. A commit receipt records that the protocol obligation was discharged; it does not assert that the external target actually performed the effect. Unknown remote outcomes MUST be recorded as INDETERMINATE and MUST NOT be retried blindly. Status: DRAFT, NOT CARRIED.", "type": "object", "additionalProperties": false, ...

---

### R0507 -- extract_corpus.py — XZ Protocol Audit Corpus Extractor v0.6
- **Date:** Undated
- **Source:** extract_corpus.py
- **Size:** 984 lines, 40,152 chars
- **SHA-256:** `c0622f824947eb03...`

**Structure:**
  - !/usr/bin/env python3
  - 1. Report-level metadata (round, version, seat, model family, role, verdict)
  - 2. Per-finding structured data (ID, severity, class, locus, description)
  - 3. Round-version-seat coverage matrix
  - ── Configuration ──────────────────────────────────────────────
  - ── Manual overrides from prose inspection (v0.3 triage) ──────
  - ── Data structures ────────────────────────────────────────────
  - Extracted metadata
  - ── Family normalization ───────────────────────────────────────
  - ── Version / round extraction from filename ───────────────────
  - S01-S12, Seat N, C01-C08, SC01-SC08
  - ── Report content parsing ─────────────────────────────────────
  - Version from text
  - Round from text
  - Seat

**Key Concepts:** TEXT, ARCHIVE, ROOTS, CORPUS, OUTPUT, DIR, MANUAL, VERDICTS, OPUS, ADVISORY

**Content Summary:**
- source_format: py - text_sha256: c0622f824947eb036fc917e4318a8b41de85b6553257da9e05d28b37fee64df6
#!/usr/bin/env python3 """ XZ Protocol Audit Corpus Extractor v0.6 ======================================== Construction procedure for the XZ Structural Honesty Audit Corpus. Versioned: v0.6 (post-R4 absorption -- locus boundary fix, description cleanup).
Walks all seat reports from the audit archive, extracts: 1. Report-level metadata (round, version, seat, model family, role, verdict) 2. Per-finding structured data (ID, severity, class, locus, description) 3. Round-version-seat coverage matrix

---

### R0508 -- extract_findings.py — extract_findings.py -- CI-8 class fix: automated findings extraction from seat reports.
- **Date:** Undated
- **Source:** extract_findings.py
- **Size:** 160 lines, 6,272 chars
- **SHA-256:** `212facc56eeea7e1...`

**Structure:**
  -     F-SNN-VV-NN -- SEVERITY -- ...
  -     F-SNN-VV-NN — SEVERITY — ...
  - Declaration patterns (finding ID + severity in the same line, declaration context)
  - ### F-SNN-VV-NN -- SEVERITY -- ...
  - **F-SNN-VV-NN** ... SEVERITY
  - | F-SNN-VV-NN | SEVERITY | (table row)
  - F-SNN-VV-NN (SEVERITY)
  - F-SNN-VV-NN [SEVERITY] (square bracket format, e.g. Gemini reports)
  - Two-pass extraction: heading declarations first (authoritative),
  - then other patterns for findings not yet seen. This ensures
  - ### F-SNN-VV-NN -- SEVERITY -- wins over inline mentions.
  - Version filter: skip findings from other rounds
  - Seat range filter: skip seats outside S01-S06
  - Output as JSON

**Key Concepts:** JSON, SNN, SEVERITY, FIRST, FINDING, HIGH, MEDIUM, LOW, INFORMATIONAL, CRITICAL

**Content Summary:**
- source_format: py - text_sha256: 212facc56eeea7e1bdcd87b93d7ef9e66c95bb5a360dce6a0e745cb68085fce8
"""extract_findings.py -- CI-8 class fix: automated findings extraction from seat reports.
Reads markdown seat reports and produces a findings index JSON with correct finding IDs and source severities extracted directly from the report bytes. Eliminates manual transcription, which caused CI-8 recurrence at R22-R25.

---

### R0509 -- file_router.py — FileRouter — each tribe knowing its drinking-place (Al-Baqarah 2:60).
- **Date:** Undated
- **Source:** file_router.py
- **Size:** 782 lines, 32,028 chars
- **SHA-256:** `ff7f5a591c10dc94...`

**Structure:**
  - ---------------------------------------------------------------------------
  - Router-specific exceptions
  - ---------------------------------------------------------------------------
  - ---------------------------------------------------------------------------
  - FileKind — closed enumeration of every file class Bayyinah recognises
  - ---------------------------------------------------------------------------
  - Phase 17 — XLSX is the spreadsheet analogue of DOCX: an Office Open
  - XML ZIP with its own set of parts (xl/workbook.xml, xl/worksheets/*,
  - xl/sharedStrings.xml, xl/vbaProject.bin, xl/embeddings/*, etc.). Like
  - DOCX the router disambiguates ZIP-magic files by extension; the
  - XlsxAnalyzer is the client the router's dispatch now routes to.
  - Phase 18 — PPTX is the presentation analogue of DOCX / XLSX: an
  - Office Open XML ZIP with its own set of parts (ppt/presentation.xml,
  - ppt/slides/slide*.xml, ppt/notesSlides/notesSlide*.xml,
  - ppt/slideMasters/*, ppt/slideLayouts/*, ppt/vbaProject.bin,

**Key Concepts:** PDF, DOCX, HTML, JSON, ZIP, PDFP, PDFC, XLSX, XML ZIP, PPTX

**Content Summary:**
- source_format: py - text_sha256: ff7f5a591c10dc943abf906e5b5330c134688a6a6c68b32304ce839c04096214
""" FileRouter — each tribe knowing its drinking-place (Al-Baqarah 2:60).
قَدْ عَلِمَ كُلُّ أُنَاسٍ مَّشْرَبَهُمْ "Each tribe knew its drinking-place."

---

### R0510 -- finalize_packet_v0_5.py — Insert artifact hashes into the dispatch brief, then write SHA256SUMS.
- **Date:** Undated
- **Source:** finalize_packet_v0_5.py
- **Size:** 157 lines, 7,762 chars
- **SHA-256:** `22e2474c04f229db...`

**Key Concepts:** SHA, SUMS, HERE, BRIEF, SHVVP, AUDIT, DISPATCH, MANIFEST, SKIP, PREFIX

**Content Summary:**
- source_format: py - text_sha256: 22e2474c04f229db45a202eafaf7948b63b85382fc728f15cec25202ecde299e
"""Insert artifact hashes into the dispatch brief, then write SHA256SUMS.
Order matters: the brief must be written before the manifest, because the manifest covers the brief. The manifest never lists itself. """ import hashlib import os import re

---

### R0511 -- finding_codes.py — Finding-code registry.
- **Date:** Undated
- **Source:** finding_codes.py
- **Size:** 1004 lines, 32,499 chars
- **SHA-256:** `8864834914110259...`

**Structure:**
  - CSV finding codes (NEW v1.2.5)
  - JSON finding codes (NEW v1.2.5)
  - ZIP composition / defense finding codes (NEW v1.2.6)
  - ML extractor finding codes (NEW v1.3.0)
  - Manifest extractor finding codes (NEW v1.3.0)
  - AUTOSAR ARXML finding codes (NEW v1.4.0)
  - ELF binary substrate finding codes (NEW v1.10.0)
  - ARXML-ELF pairing finding codes (NEW v1.4.1)
  - ARINC-653 + Munafiq finding codes (NEW v1.5.0)
  - ARINC-653 + ELF cross-substrate pairing finding codes (NEW v1.5.1)
  - IEC 61850 SCL finding codes (NEW v1.7.0)
  - SBOM (SPDX + CycloneDX) finding codes (NEW v1.9.0)
  - IEC 61131-3 PLCopen finding codes (NEW v1.6.0)

**Key Concepts:** NEW, CSV, BYN, JSON, ZIP, CODES, HIGH, MEDIUM, RFC, EOF

**Content Summary:**
- source_format: py - text_sha256: 8864834914110259816c493d5a303bb6bb160b441794b6e71ac89ef531173a61
NEW in v1.2.5: CSV (BYN-CSV-001..099) and JSON (BYN-JSON-001..099) namespaces. NEW in v1.2.6: ZIP composition / defense (BYN-ZIP-901..999) namespace.
Each finding code carries: - id: canonical string identifier - kind: substrate-kind (CSV, JSON, ZIP, ...) - title: short human-readable name - severity_default: default severity if the analyzer does not override - description: what the finding indicates about the surface/substrate divergence """

---

### R0512 -- furqan-lint coding strategy: main (v0.12.0+5) to v2.0.1 commercialization tier
- **Date:** Undated
- **Source:** furqan_lint_coding_strategy_to_v2_0.md
- **Size:** 396 lines, 21,038 chars
- **SHA-256:** `046acdeddf992273...`

**Structure:**
  - furqan-lint coding strategy: main (v0.12.0+5) to v2.0.1 commercialization tier
  -   Calibrated time
  -   0. Where the substrate is
  -   1. Bayyinah pattern -> furqan-lint mapping
  -   2. Patent-invariant surface for furqan-lint
  -   3. Required invariant probes for every release
  -   4. Multi-locus update map
  -   5. Pre-existing flaky baselines to document
  - 1. Any test that depends on Sigstore identity TUF root fetching (network).
  - 2. Any tree-sitter language pack version-pinned test (tree-sitter-rust,
  - 3. Any ONNX runtime check that compares against numpy reference (the
  - 4. Any go-test fixture that depends on `go vet` exit codes (Go toolchain
  -   6. Release-by-release intent
  -     v0.13.0 (claim the existing an-Naziat tag, OR cut fresh)
  -     v0.14.0 (claim al-Tasdiq al-Bayan tag, OR cut fresh)

**Key Concepts:** HEAD, CASM, ONNX, CHANGELOG, README, ALL, ITS OWN, PENDING, CALIBRATION, DOCS

**Content Summary:**
- source_format: md - text_sha256: 046acdeddf992273efb729d9e841a8177edfe93ebc81879a7b6cb35d12dcb969
# furqan-lint coding strategy: main (v0.12.0+5) to v2.0.1 commercialization tier
Mirror of `bayyinah_v1_2_4_to_v2_0_cowork_executable_strategy.md` applied to the furqan-lint substrate. The Bayyinah commercialization arc shipped v1.5.0 - v2.0.1 in a single session by holding four disciplines constant: patent-invariant byte-identity, multi-locus contract pinning, structural self-defense via a recursive gate, and Round-12-style calibration correctives forced by the gate. This document translates each into furqan-lint shape.

---

### R0519 -- inject_sim_values_v0_5.py — Substitute the simulation receipt into the canonical v0.5 source.
- **Date:** Undated
- **Source:** inject_sim_values_v0_5.py
- **Size:** 177 lines, 8,880 chars
- **SHA-256:** `7e2c9d9fc0676dd2...`

**Key Concepts:** HERE, SRC, SHV, VALIDATION, PROTOCOL, RECEIPT, SUCCESS, SELECTED, NOT

**Content Summary:**
- source_format: py - text_sha256: 7e2c9d9fc0676dd2b5fde5b6cd21554964133e55c17db4744254a98a138db563
"""Substitute the simulation receipt into the canonical v0.5 source.
Guarantees literal concordance between the frozen text and the shipped simulation: every power, calibration and sensitivity figure in Section 6.8, and the frozen design size wherever it appears, is written from power_sim_receipt.json rather than typed by hand.

---

### R0520 -- lineage-record.schema.json.txt
- **Date:** Undated
- **Source:** lineage-record.schema.json.txt
- **Size:** 146 lines, 5,064 chars
- **SHA-256:** `bffbf81553f8d41c...`

**Key Concepts:** BSSG, DRAFT, MUST NOT, COMPLETE, NOT CARRIED, PARTIAL, UNKNOWN, COSE, CANON

**Content Summary:**
- source_format: txt - text_sha256: bffbf81553f8d41c645b4040f10265550d7becf26e911613a87684a32e77f5c5
{ "$schema": "https://json-schema.org/draft/2020-12/schema", "$id": "urn:bssg:schema:0.1:lineage-record", "title": "BSSG lineage record (v0.1 DRAFT)", "description": "A hash-linked view of the records covering one session or one artifact. Lineage records claim continuity only for transformations that passed through a mediated adapter. Completeness outside the declared mediation boundary is not claimed and cannot be claimed. A lineage record with declared gaps MUST NOT report COMPLETE. Status: DRAFT, NOT CARRIED.", "type": "object", "additionalProperties": false, "required": [ "record_type", "spec_version", "lineage_id", "subject_id", "session_id", "nodes", "head_digest", "chain_alg", "compl...

---

### R0522 -- make_text_fixtures.py — Phase 9 fixture generator — adversarial + clean fixtures for the text-based
- **Date:** Undated
- **Source:** make_text_fixtures.py
- **Size:** 308 lines, 10,516 chars
- **SHA-256:** `4fa4bfa8c9bbc13a...`

**Structure:**
  - ---------------------------------------------------------------------------
  - Expectation table
  - ---------------------------------------------------------------------------
  - Maps each fixture's path (relative to ``tests/fixtures/text_formats/``)
  - to the mechanisms it SHOULD fire. An empty list means "clean — no
  - analyzer should fire". Tests in ``tests/test_text_fixtures.py`` walk
  - this table and assert per-fixture expectations.
  - Clean fixtures — any firing is a false positive.
  - Adversarial — each fires a specific detector.
  - ---------------------------------------------------------------------------
  - Clean fixtures
  - ---------------------------------------------------------------------------
  - Bayyinah Clean Markdown Reference
  - ---------------------------------------------------------------------------
  - Adversarial fixtures — each isolates ONE mechanism

**Key Concepts:** MARKDOWN, CODE, JSON, PDF, TEXT, FIXTURE, EXPECTATIONS, FIXTURES, DIR, CLEAN

**Content Summary:**
- source_format: py - text_sha256: 4fa4bfa8c9bbc13a4b484a5bbd6f920b0e32fa3ea1c22268fec9257b55338534
""" Phase 9 fixture generator — adversarial + clean fixtures for the text-based FileKinds the router recognises: MARKDOWN, CODE, JSON.
This module is structurally parallel to ``tests/make_test_documents.py`` (the PDF fixture generator) but stays in its own file so the two pipelines remain independent. PDF fixtures are byte-sensitive and regenerating them would break the parity tests; text fixtures are plain-text and trivially regeneratable — keeping them separate keeps the dependency footprint of one from bleeding into the other.

---

### R0523 -- pyproject.toml
- **Date:** Undated
- **Source:** pyproject.toml
- **Size:** 94 lines, 2,487 chars
- **SHA-256:** `3bfbf2b42c6e350d...`

**Structure:**
  - Runtime dependencies: stdlib-only for v1.2.5 (csv, json modules).
  - Optional scipy used by the F1 harness for exact Clopper-Pearson bounds.
  - Per dependency-manifest discipline (memory): new third-party imports go in
  - BOTH requirements.txt AND pyproject.toml in the same patch, capped at current major.

**Key Concepts:** ARINC, README, BOTH, AND

**Content Summary:**
- source_format: toml - text_sha256: 3bfbf2b42c6e350d42e941868caa194a260c4a171b7bb37b635d29f4faa79404
[build-system] requires = ["setuptools>=68", "wheel"] build-backend = "setuptools.build_meta"
[project] name = "bayyinah" version = "1.5.0" description = "Bayyinah Scanner: file integrity verification through surface/substrate parity (ARINC-653 + Munafiq self-detect, avionics advisory tier)" readme = "README.md" requires-python = ">=3.9" license = { text = "Proprietary" } authors = [ { name = "Bilal Syed Arfeen", email = "bayyinahenterprises@tuta.com" }, ] classifiers = [ "Programming Language :: Python :: 3", "Programming Language :: Python :: 3 :: Only", "Programming Language :: Python :: 3.9", "Programming Language :: Python :: 3.10", "Programming Language :: Python :: 3.11", "Programmi...

---

### R0524 -- reconstruct.py — Rebuild schemas/ from flat schema__*.json + restore SHA256SUMS from .txt, so the code
- **Date:** Undated
- **Source:** reconstruct.py
- **Size:** 43 lines, 1,801 chars
- **SHA-256:** `4151a22915f81155...`

**Structure:**
  - !/usr/bin/env python3

**Key Concepts:** SHA, SUMS, FIRST, AUDIT, BRIEF, KIMI, PAIRS

**Content Summary:**
- source_format: py - text_sha256: 4151a22915f811557381f0cfb7e2c42647cb1ebd02a53f630dcccdd89d897eb9
#!/usr/bin/env python3 """Rebuild schemas/ from flat schema__*.json + restore SHA256SUMS from .txt, so the code and verifier run. Run this FIRST, then the commands in AUDIT_BRIEF_KIMI.md.""" import os, shutil PAIRS = { 'schema__authorization-receipt.schema.json': 'schemas/authorization-receipt.schema.json', 'schema__correction-event.schema.json': 'schemas/correction-event.schema.json', 'schema__effect-request.schema.json': 'schemas/effect-request.schema.json', 'schema__execution-receipt.schema.json': 'schemas/execution-receipt.schema.json', 'schema__lineage-record.schema.json': 'schemas/lineage-record.schema.json', 'schema__witness-receipt.schema.json': 'schemas/witness-receipt.schema.json',...

---

### R0525 -- Bayyinah — development requirements
- **Date:** Undated
- **Source:** requirements-dev.txt
- **Size:** 35 lines, 886 chars
- **SHA-256:** `b653a471eb30b20e...`

**Structure:**
  - Bayyinah — development requirements
  - Kept in sync with [project.optional-dependencies].dev in pyproject.toml.
  - Install with:  pip install -r requirements-dev.txt

**Content Summary:**
- source_format: txt - text_sha256: b653a471eb30b20e00f5bdb9a8c0df154d57e04afd81c53e48a90b775f448e36
# Bayyinah — development requirements # Kept in sync with [project.optional-dependencies].dev in pyproject.toml. # Install with:  pip install -r requirements-dev.txt

---

### R0526 -- Bayyinah — runtime requirements
- **Date:** Undated
- **Source:** requirements.txt
- **Size:** 59 lines, 1,982 chars
- **SHA-256:** `4672b686f2411f15...`

**Structure:**
  - Bayyinah — runtime requirements
  - Kept in sync with the [project.dependencies] table in pyproject.toml.
  - Install with:  pip install -r requirements.txt
  - Upper bounds (added v1.1.1, Phase-26 review fix #4) extend the
  - additive-only invariant to upstream dependencies. A pymupdf 2.x or
  - pypdf 7.x release that changes the parse surface could break PDF
  - parity silently; capping at the current major versions forces any
  - compatibility step to be explicit. See pyproject.toml's
  - [project.dependencies] block for the full rationale.
  - PDF object-layer + text-layer extraction
  - pikepdf - raw PDF content-stream walking for v1.1.2 Day 2 mechanism 03
  - (pdf_off_page_text). Bypasses PyMuPDF get_text(dict) silent drop of
  - spans whose origin is outside the page rectangle.
  - Audio container metadata (Phase 24 - MP3 / WAV / FLAC / M4A / OGG).
  - HTTP API wrapper (api.py). Used by the Railway deployment that exposes

**Key Concepts:** PDF, WAV, FLAC, OGG, HTTP API, HTTP, API, BAYYINAH, DEMO, ENABLED

**Content Summary:**
- source_format: txt - text_sha256: 4672b686f2411f158518f013dbfcddc114f95c526d362030ac0ba6a65b0a2e0d
# Bayyinah — runtime requirements # Kept in sync with the [project.dependencies] table in pyproject.toml. # Install with:  pip install -r requirements.txt # # Upper bounds (added v1.1.1, Phase-26 review fix #4) extend the # additive-only invariant to upstream dependencies. A pymupdf 2.x or # pypdf 7.x release that changes the parse surface could break PDF # parity silently; capping at the current major versions forces any # compatibility step to be explicit. See pyproject.toml's # [project.dependencies] block for the full rationale.
# PDF object-layer + text-layer extraction pymupdf>=1.24,<2 pypdf>=4.0,<7 # pikepdf - raw PDF content-stream walking for v1.1.2 Day 2 mechanism 03 # (pdf_off_pa...

---

### R0527 -- BSSG v0.1 Requirements Traceability
- **Date:** Undated
- **Source:** REQUIREMENTS_TRACEABILITY.md.txt
- **Size:** 141 lines, 13,456 chars
- **SHA-256:** `fcd590ab2688fa56...`

**Structure:**
  - BSSG v0.1 Requirements Traceability
  -   1. Complete mediation and reference-monitor requirements
  -   2. Fail-closed and UNKNOWN discipline
  -   3. ContractMatch
  -   4. EffectTypeValid
  -   5. TargetAllowed
  -   6. WitnessHealthy
  -   7. EvidenceCurrent
  -   8. Receipts, logs, provenance
  -   9. Charter requirements from the producing task

**Key Concepts:** BSSG, DRAFT, NOT CARRIED, NOT VERIFIED, ENFORCED, ASSUMED, NIST CSRC, PDP, PEP, NIST SP

**Content Summary:**
- source_format: txt - text_sha256: fcd590ab2688fa56265b1d5b2f5405b8baf96297d54b2625ee66cefe03ca7dab
**Status:** DRAFT / NOT CARRIED. Each row traces a requirement from its evidentiary source, through the specification section that carries it, to the artifact that implements or checks it. A requirement with no verification hook is marked NOT VERIFIED and is not claimed.
Requirement identifiers R-S* are taken from the source-grounded evidence report `bssg-research-evidence.pplx.md`.

---

### R0528 -- run_gauntlet.py — Run the seven format-routing fixtures against the live API and capture
- **Date:** Undated
- **Source:** run_gauntlet.py
- **Size:** 178 lines, 6,309 chars
- **SHA-256:** `ce3f22766925ee62...`

**Structure:**
  - Cloudflare-fronted Railway. The --resolve pin keeps gauntlet runs
  - stable when DNS rotates between Railway-direct and Cloudflare front.
  - Each entry: (fixture filename, expected Tier 0 fired, expected
  - routing_decision value, friendly description).
  - Pass: Tier 0 fired iff expected, routing_decision matches expected
  - value, and the verdict is mughlaq for routing-divergence fixtures.

**Key Concepts:** API, AND, PDF, FIXTURES, DIR, RESULTS, PATH, URL, DNS, RESOLVE

**Content Summary:**
- source_format: py - text_sha256: ce3f22766925ee6209ebb44a5706d564e9b6bfe2dc9c1b23de50bd5665db1c5f
""" Run the seven format-routing fixtures against the live API and capture the full structured response. Output: results.json + a printable summary.
Pass criteria: - Fixtures 01-06 each return at least one finding with tier == 0 AND mechanism == 'format_routing_divergence' AND verdict == 'mughlaq'. - Fixture 07 (control) returns NO finding with tier == 0; verdict is whatever the existing per-format analyzer would produce (mukhfi via the seed PDF's white_on_white_text Tier 1). """ from __future__ import annotations

---

### R0529 -- run_test.sh
- **Date:** Undated
- **Source:** run_test.sh
- **Size:** 57 lines, 1,262 chars
- **SHA-256:** `226169dedc306c47...`

**Structure:**
  - !/bin/bash

**Key Concepts:** PREFIX

**Content Summary:**
- source_format: sh - text_sha256: 226169dedc306c47d13d5eb4ec018a463228b7c1ed30720932f9663ebbec7e17
genrb de.txt echo "de.res" > list.txt pkgdata -p mybundle list.txt
test ! -f $PREFIX/lib/libicudata.a test -f $PREFIX/lib/libicudata.78.3.dylib test ! -f $PREFIX/lib/libicui18n.a test -f $PREFIX/lib/libicui18n.78.3.dylib test ! -f $PREFIX/lib/libicuio.a test -f $PREFIX/lib/libicuio.78.3.dylib test ! -f $PREFIX/lib/libicutest.a test -f $PREFIX/lib/libicutest.78.3.dylib test ! -f $PREFIX/lib/libicutu.a test -f $PREFIX/lib/libicutu.78.3.dylib test ! -f $PREFIX/lib/libicuuc.a test -f $PREFIX/lib/libicuuc.78.3.dylib genbrk --help gencfu --help gencnval --help gendict --help icuinfo --help icu-config --help makeconv gb-18030-2000.ucm exit 0

---

### R0530 -- run_v0_5_regression.sh
- **Date:** Undated
- **Source:** run_v0_5_regression.sh
- **Size:** 35 lines, 1,223 chars
- **SHA-256:** `db18070a4cc11aeb...`

**Structure:**
  - !/usr/bin/env bash
  - The four v0.5 files at top level are byte-identical PROVENANCE copies checked by the
  - verifier's G10. The v0.5 regression suite needs the COMPLETE v0.5 module set, which
  - ships intact under lineage/. This wrapper runs it there.

**Key Concepts:** PROVENANCE, COMPLETE, HERE

**Content Summary:**
- source_format: sh - text_sha256: db18070a4cc11aebe24893643be1babd1971608fd019da267a9b07c0c2bcd849
#!/usr/bin/env bash # The four v0.5 files at top level are byte-identical PROVENANCE copies checked by the # verifier's G10. The v0.5 regression suite needs the COMPLETE v0.5 module set, which # ships intact under lineage/. This wrapper runs it there. set -euo pipefail HERE="$(cd "$(dirname "$0")" && pwd)" V05="$(find "$HERE/lineage" -type d -name shvvp_v0_5_release | awk '{print length, $0}' | sort -n | tail -1 | cut -d' ' -f2-)" [ -n "$V05" ] || { echo "v0.5 lineage release not found"; exit 1; } echo "running v0.5 regression in: $V05" ( cd "$V05" && python3 test_shvvp_v0_5_rules.py )

---

### R0531 -- test_file_router.py — Tests for infrastructure.file_router.FileRouter.
- **Date:** Undated
- **Source:** test_file_router.py
- **Size:** 458 lines, 15,775 chars
- **SHA-256:** `d4ea2cec40b6f6eb...`

**Structure:**
  - ---------------------------------------------------------------------------
  - Magic-byte detection
  - ---------------------------------------------------------------------------
  - ---------------------------------------------------------------------------
  - DOCX (ZIP + .docx)
  - ---------------------------------------------------------------------------
  - ZIP without a mapped extension is not something Bayyinah scans;
  - must not be misclassified as DOCX.
  - ---------------------------------------------------------------------------
  - Content sniff: HTML
  - ---------------------------------------------------------------------------
  - Unknown extension is not a "mismatch" per se — we have no
  - extension-declared expectation to contradict.
  - ---------------------------------------------------------------------------
  - Content sniff: JSON

**Key Concepts:** PDF, PNG, JPEG, DOCX, ZIP, HTML, JSON, UNKNOWN, PDFC, FIXTURES

**Content Summary:**
- source_format: py - text_sha256: d4ea2cec40b6f6eb037b83e5e15c7c6b469fbd2ae6b3ac20ffda5d9ea6a76416
""" Tests for infrastructure.file_router.FileRouter.
Coverage targets: * Magic-byte detection (PDF, PNG, JPEG) * DOCX detection via ZIP + extension combination * HTML content sniff (case-insensitive) * JSON content sniff (objects and arrays) * Extension fall-through for markdown / code / text-family * UNKNOWN fall-through * extension_mismatch flag for polyglot-style files * client_for dispatches PDF → PDFClient * client_for raises UnsupportedFileType / UnknownFileType correctly * is_supported convenience wrapper * Exercises Phase 0 fixtures directly """

---

### R0532 -- test_format_routing.py — Tests for the v1.1.2 Tier 0 routing-transparency layer.
- **Date:** Undated
- **Source:** test_format_routing.py
- **Size:** 448 lines, 16,903 chars
- **SHA-256:** `3740a99e35089551...`

**Structure:**
  - 1. The detector function ``detect_format_routing_divergence`` returns
  - 2. The detector returns ``None`` on a clean control file (no false
  - 3. The Finding constructor's disclosure-schema validator (the five
  - 4. The verdict resolver (``tamyiz_verdict``) floors at mughlaq when a
  - 5. The verdict resolver returns the existing verdict when no Tier 0
  - 6. A full ScanService scan on each fixture produces the expected
  - 7. Each Tier 0 finding's ``evidence`` dict contains exactly the five
  - ===========================================================================
  - Configuration-level pins
  - ===========================================================================
  - ===========================================================================
  - Finding-construction pins (disclosure schema validator)
  - ===========================================================================
  - to_dict should not contain 'evidence' for parity with v0/v0.1.
  - ===========================================================================

**Key Concepts:** OOXML, ROUTING, DISCLOSURE, KEYS, REPORT, MECHANISMS, SEVERITY, TIER, VERDICT, MUGHLAQ

**Content Summary:**
- source_format: py - text_sha256: 3740a99e35089551c8f164e1f26fa76ab5f580251341bdab6aaa463fd781f3e6
""" Tests for the v1.1.2 Tier 0 routing-transparency layer.
1. The detector function ``detect_format_routing_divergence`` returns the right Tier 0 finding for each of the four trigger conditions (T0a extension/magic mismatch, T0b unknown, T0c content-depth floor, T0d OOXML internal-path divergence). 2. The detector returns ``None`` on a clean control file (no false positives). 3. The Finding constructor's disclosure-schema validator (the five required keys in ``ROUTING_DISCLOSURE_KEYS``) rejects incomplete evidence at construction time. 4. The verdict resolver (``tamyiz_verdict``) floors at mughlaq when a Tier 0 finding is present, even when downstream Tier 1 findings also fire. 5. The verdi...

---

### R0533 -- test_scan_endpoint_verdict.py — Integration tests for /scan endpoint verdict emission.
- **Date:** Undated
- **Source:** test_scan_endpoint_verdict.py
- **Size:** 107 lines, 3,679 chars
- **SHA-256:** `e9203f6dd82c41c6...`

**Key Concepts:** HTTP, FIXTURES, DIR, ROUTING, DIVERGENCE, CONTROL, FIXTURE, PDF

**Content Summary:**
- source_format: py - text_sha256: e9203f6dd82c41c618ad7113bef5b2eafead0f2ef609603cbc49b6234e1f2bb5
""" Integration tests for /scan endpoint verdict emission.
Asserts that every routing-divergence fixture in the format_routing_gauntlet surfaces verdict=mughlaq at the HTTP layer, and that the control fixture does not.

---

### R0534 -- test_scan_file_public_api.py — Tests for the format-agnostic ``scan_file()`` public API (Week-1 assessment I3).
- **Date:** Undated
- **Source:** test_scan_file_public_api.py
- **Size:** 136 lines, 5,057 chars
- **SHA-256:** `aa7cad57d5ee1817...`

**Structure:**
  - Try a handful of fixture paths; at least one must resolve.
  - Clean fixtures produce integrity 1.0 and no error; we only assert
  - the report is well-formed — specific findings are analyzer-specific
  - and tested elsewhere.

**Key Concepts:** API, REST, POST, PDF

**Content Summary:**
- source_format: py - text_sha256: aa7cad57d5ee1817ac68ca4d50a0f4d6fa55647e80c8293fc16e7d4d112c1d71
""" Tests for the format-agnostic ``scan_file()`` public API (Week-1 assessment I3).
The scanner has always handled 12 formats internally via ``ScanService`` and ``FileRouter``, but the public surface only exposed ``scan_pdf()``. ``scan_file()`` is the additive counterpart — it is the recommended entry point for new code and is the natural top-level hook for the forthcoming REST/FastAPI wrapper (POST /scan accepting any format). ``scan_pdf()`` remains a backward-compatible alias.

---

### R0536 -- test_walkers.py — Tests for v1.2.6 composition walkers + ZIP-bomb defense."""
- **Date:** Undated
- **Source:** test_walkers.py
- **Size:** 151 lines, 4,967 chars
- **SHA-256:** `e83412c69771ab16...`

**Structure:**
  - OCI walker produces descriptor JSON for each layer; descriptors don't have
  - a .json extension so no per-extension dispatch fires. We assert that the
  - walker runs cleanly without crashing.
  - No findings expected on a clean manifest with well-formed descriptors

**Key Concepts:** ZIP, DEFLATED, OCI, BYN, CSV, BLOCKER, JSON

**Content Summary:**
- source_format: py - text_sha256: e83412c69771ab16d7057df317e82a1f133b5656a004e213c5fd5c1a731e36e6
"""Tests for v1.2.6 composition walkers + ZIP-bomb defense."""
from bayyinah.walkers import ( SafetyLimits, ZipBombDetected, compose_scan, detect_kind, evaluate_zip_safety, )

---

### R0537 -- three_way_projection.py — Source-SBOM-binary three-way projection orchestrator (NEW v1.9.0).
- **Date:** Undated
- **Source:** three_way_projection.py
- **Size:** 212 lines, 7,421 chars
- **SHA-256:** `100bfd3a12259638...`

**Structure:**
  - BYN-3WAY-001: SBOM has it, source doesn't
  - BYN-3WAY-002: source has it, SBOM doesn't
  - BYN-3WAY-003: SBOM has it, binary doesn't

**Key Concepts:** SBOM, NEW, NOT, BYN, WAY, SBOM
    BYN, NTIA, SBOMD, JSOND, TOML

**Content Summary:**
- source_format: py - text_sha256: 100bfd3a122596382a9b636ea94cb08535819fb1daacdc5180726deb40f60717
"""Source-SBOM-binary three-way projection orchestrator (NEW v1.9.0).
Per strategy Phase 3.1 Step 6 task 4: Source-SBOM-binary three-way projection check (30 triples; per-category box). Per strategy Phase 3.1 Step 7: Worked: v1.3.0 manifest-vs-model parity pattern translates to SBOM-vs-binary parity. Failed: prior SBOM-correctness verification without binary cross-check. Cow Episode: do NOT invent new SBOM-vs-binary discrepancy categories.

---

### R0538 -- verify_live.sh
- **Date:** Undated
- **Source:** verify_live.sh
- **Size:** 80 lines, 2,511 chars
- **SHA-256:** `3bf20e6809c8a5eb...`

**Structure:**
  - !/usr/bin/env bash
  - Day 1 live-curl verification gate (v1.1.2 prompt section 3.2).
  - Runs after deploying v1.1.2 to bayyinah.dev. All three commands
  - below must return `true` for Day 1 to be considered complete and
  - Day 2 (PDF) to begin. From the prompt:
  - "All three must return `true`. If any return `false`, Day 1 is
  - not complete and Day 2 does not begin."
  - Cannot run from the build sandbox - bayyinah.dev is the live
  - Cloudflare-fronted Railway deployment, and the v1.1.2 code in
  - this branch has not been pushed yet. Run this on the deploy
  - machine after `git push` and Railway rolls v1.1.2 forward.

**Key Concepts:** PDF, GAUNTLET, ALL PASS, LEAST ONE FAIL, NOT

**Content Summary:**
- source_format: sh - text_sha256: 3bf20e6809c8a5eb7c5ef77e0e93ab9a751883d192050eb7c2e86f2979faddd2
#!/usr/bin/env bash # Day 1 live-curl verification gate (v1.1.2 prompt section 3.2). # # Runs after deploying v1.1.2 to bayyinah.dev. All three commands # below must return `true` for Day 1 to be considered complete and # Day 2 (PDF) to begin. From the prompt: # #   "All three must return `true`. If any return `false`, Day 1 is #    not complete and Day 2 does not begin." # # Cannot run from the build sandbox - bayyinah.dev is the live # Cloudflare-fronted Railway deployment, and the v1.1.2 code in # this branch has not been pushed yet. Run this on the deploy # machine after `git push` and Railway rolls v1.1.2 forward.
GAUNTLET="docs/adversarial/format_routing_gauntlet/fixtures"

---

### R0540 -- witness-receipt.schema.json.txt
- **Date:** Undated
- **Source:** witness-receipt.schema.json.txt
- **Size:** 151 lines, 5,930 chars
- **SHA-256:** `8bf30f505e1ff7ee...`

**Key Concepts:** BSSG, DRAFT, NOT, MUST NOT, NOT CARRIED, MUST, UNKNOWN, DECLARATION, DETECTION, HEALTHY

**Content Summary:**
- source_format: txt - text_sha256: 8bf30f505e1ff7ee21276bf631430adbd3d44706332e4a6d75079b27fabbc054
{ "$schema": "https://json-schema.org/draft/2020-12/schema", "$id": "urn:bssg:schema:0.1:witness-receipt", "title": "BSSG witness receipt (v0.1 DRAFT)", "description": "A signed statement by a witness about its own observed state and its coverage of a subject. A witness receipt attests observation and consistency with the witness's own prior state. It does NOT attest that the subject behaved correctly, that the witness is honest, or that the evidence is independent. WitnessHealthy MUST NOT be read as witness honesty. Status: DRAFT, NOT CARRIED.", "type": "object", "additionalProperties": false, "required": [ "record_type", "spec_version", "witness_id", "covered_subject", "covered_subject_do...

---

## Cross-Paper Themes

**Recurring Concepts (appearing in multiple papers):**
  - pdf: 8 papers
  - json: 7 papers
  - unknown: 6 papers
  - bssg: 5 papers
  - draft: 5 papers
  - not carried: 5 papers
  - dir: 5 papers
  - fixtures: 5 papers
  - must not: 4 papers
  - canon: 4 papers
  - rfc: 4 papers
  - zip: 4 papers
  - not: 4 papers
  - must: 3 papers
  - sha: 3 papers
  - cose: 3 papers
  - high: 3 papers
  - docx: 3 papers
  - html: 3 papers
  - code: 3 papers

**Date Range:** Undated to Undated

**Source Formats:** md(1), py(15), sh(3), toml(1), txt(7)

## Key Findings

(See per-paper summaries above for detailed findings per paper.)

## Connections to Other Sections

**Cross-references found:** bayyinah, bssg, furqan, munafiq protocol, section i, shv, xz protocol

# Bismillah ir-Rahman ir-Rahim
