# Bismillah ir-Rahman ir-Rahim

# R0614 -- Bayyinah — End-of-Day Summary

**Chronological Index:** 173 of 995  
**Date:** 2026-04-21  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** EOD_2026-04-21.md  
**Source Format:** md  
**SHA-256:** `4a6f7370b40111be8b1c0ee275255581b95c219e1d327614dcd0d82a5ebadc8c`  

---

## R0614 · Bayyinah — End-of-Day Summary

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: EOD_2026-04-21.md
- source_format: md
- text_sha256: 4a6f7370b40111be8b1c0ee275255581b95c219e1d327614dcd0d82a5ebadc8c

# Bayyinah — End-of-Day Summary

**Date:** 2026-04-21
**Session focus:** Modular refactor, parity regression, packaging

---

## What was achieved

**Architecture.** Refactored the monolithic two-scanner design in `bayyinah_v0.py` into a plugin architecture. `bayyinah_v0_1.py` introduces three primitives:

- `PDFContext` — lazy, cached `fitz` + `pypdf` state with a `try_pypdf() → (reader, exc)` seam that preserves v0's silent-scan_error behavior
- `BaseAnalyzer` (ABC) — a uniform `scan(ctx) → list[Finding]` contract with per-analyzer `name` and `error_prefix` class attributes
- `ScanService` — dispatch with per-analyzer failure isolation, same aggregate error-string format and `scan_incomplete` clamp as v0

The two existing scanners were ported as "fat" analyzers (`TextLayerAnalyzer`, `ObjectLayerAnalyzer`), one mechanism per method. Per-mechanism splitting is deferred.

**Parity validation.** Built `run_parity.py` and ran it against 33 files across the representative corpus: positive_test (9 findings / 0.0), Differentiator, 8 Nausicaä, AIGuardPDF (0.0), 3 PDF 2.0 examples, 8 `malicious_generated` adversarials including the silent-scan_error path, 5 Akira scan books (605/492/476/715/664 findings), and 6 Akira analysis PDFs. **All 33 byte-identical** after normalizing pypdf's non-deterministic `IndirectObject.__repr__` — a pre-existing quirk that affects v0 too (two back-to-back v0 runs diverge on the same field).

**Packaging.** Wrote `pyproject.toml` (Apache-2.0, Python ≥3.10, `bayyinah` console script), `requirements.txt`, `requirements-dev.txt`. Confirmed the only third-party imports are `pymupdf` and `pypdf` — everything else is stdlib.

Prior calibration preserved in full: Akira OCR down-tier, scan_incomplete clamp, Nausicaä baseline, AIGuardPDF at 0.000, bidi false-positive fix.

---

## Challenges ahead

**Per-mechanism analyzer split.** The real ablation payoff of the plugin architecture isn't here yet. `ObjectLayerAnalyzer` still bundles incremental-update detection, catalog anomaly, ToUnicode CMap analysis, embedded-file enumeration, etc. in a single class. Splitting these into individual analyzers (one per mechanism) is the next load-bearing refactor — it's what lets us measure the marginal contribution of each detector.

**Format expansion vs. depth.** The scope document names PDF, DOCX, HTML, Markdown, JSON, images, and code files. Current memory note reminds us: **harden depth before scope**. We should fill PDF detection gaps and validate both corpora before we touch DOCX, even though DOCX is the obvious next format given oletools is well-known.

**Detection gaps worth auditing on PDF alone.** Encrypted PDFs (we currently bail), digitally signed PDFs with tampered signatures, XFA forms, JavaScript action analysis beyond presence, polyglot files (PDF-in-ZIP, PDF-in-JPG), PDF/A compliance signals, structured annotations hiding payloads, and embedded Type 3 font glyph substitution.

**No ground-truth labels.** We detect surface/concealed mismatch, but without a labeled benign/adversarial corpus we cannot compute precision/recall. All current evaluation is "does it fire on known-bad, stay quiet on known-benign" — qualitative, not quantitative.

**Reproducible JSON output.** The `IndirectObject` id() repr blocks any downstream workflow that wants hash-based report integrity (e.g., "this file's scan report has hash X"). Fixable by stringifying IndirectObject via `(idnum, generation)` in finding emission.

**Regression formalization.** Parity is a manual harness right now. The next step is pytest + golden-output fixtures so regressions fail CI instead of being caught by running `run_parity.py` by hand.

**Performance.** Akira Book 04 takes ~34s per scanner run. For interactive use, the raw-stream Unicode scan is the likely hot path. Profile before optimizing.

---

## Resources to strengthen the project

**Reference codebases worth reading more carefully:**
- **peepdf / pdfid / pdf-parser** (Didier Stevens) — the canonical PDF forensics trilogy. We skipped it in the initial pass; it encodes decades of PDF-specific adversarial pattern knowledge.
- **pypdfium2** — alternative backend when pypdf and pymupdf disagree; useful for cross-validation at the parse layer rather than the detection layer.
- **strelka, oletools** — already referenced for structure; still the best lens for the per-mechanism split.

**Canonical references for the detection logic itself:**
- **Unicode Technical Report #36** (Security Considerations) — authoritative source for bidi, ZWSP, homoglyph attack classification. We've implemented heuristics aligned with it but haven't cited it as grounding.
- **ICANN confusables list** — broader than the CONFUSABLE_TO_LATIN table currently in v0.1.
- **ISO 32000-1 / 32000-2** — PDF spec; helpful for distinguishing legitimate structural oddities from adversarial ones.
- **"Trojan Source" (Boucher & Anderson, 2021)** — the paper that put bidi override attacks on source code on the map; adjacent threat model.

**Corpora to pursue:**
- A labeled benign/adversarial PDF set, target ~1000 files with ground-truth class labels. Candidates: Contagio PDF dump, MalDocs, VirusShare PDFs with AV labels, academic corpora from PDF malware detection papers.
- PDF 2.0 conformance tests beyond the 7 we have.
- A small curated "tricky benign" set — Arabic/Hebrew academic PDFs, math-heavy PDFs with exotic Unicode, CJK-heavy scans — specifically to stress the false-positive surface.

**Infrastructure upgrades worth one session each:**
- pytest + golden-output snapshot fixtures
- pre-commit hooks (ruff, mypy)
- GitHub Actions matrix (3.10, 3.11, 3.12, 3.13) running the parity harness + pytest
- A small CHANGELOG.md so version bumps track calibration changes

**Positioning / community:**
- The Munafiq Protocol paper (DOI: 10.5281/zenodo.19677111) is already the theoretical grounding. A short companion preprint tying Bayyinah's input-layer detection to Section 9 of that paper would make the connection citable.
- Bayyinah's natural collaborators are the prompt-injection detection community and file-format forensics community — two audiences that rarely overlap. Either is a viable venue; both together is the differentiator.

---

## Posture heading into tomorrow

The v0.1 modular substrate is in place and proven byte-identical to v0. That makes every subsequent change a comparatively safe delta rather than a rewrite. The discipline from here forward is: split one analyzer at a time, re-run the parity harness after each split to prove the split was behavior-neutral, and only then move to gap-filling or new formats.

_Modest work, but durable._

---

# Bismillah ir-Rahman ir-Rahim
