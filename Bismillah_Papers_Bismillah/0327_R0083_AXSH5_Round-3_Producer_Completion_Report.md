# Bismillah ir-Rahman ir-Rahim

# R0083 -- AXSH5 Round-3 Producer Completion Report

**Chronological Index:** 327 of 995  
**Date:** 2026-07-24  
**Section:** III. Structural Honesty — Core Papers  
**Source File:** AXSH5_R3_PRODUCER_COMPLETION_REPORT.md  
**Source Format:** md  
**SHA-256:** `dd063a6f09013d32f74f292ab7c9ac1520c825d7d466d9c9e20e04473acedf2c`  

---

## R0083 · AXSH5 Round-3 Producer Completion Report

- section: III. Structural Honesty — Core Papers
- source_file: AXSH5_R3_PRODUCER_COMPLETION_REPORT.md
- source_format: md
- text_sha256: dd063a6f09013d32f74f292ab7c9ac1520c825d7d466d9c9e20e04473acedf2c

# AXSH5 Round-3 Producer Completion Report

**Role:** Perplexity, producer of the AX-SH 5 release packet, executed as the Anthropic / Claude Opus 4.8 council seat.
**Scope:** Revision of the accepted R3 candidate per the parent council adjudication's exact corrections (F-EI-13 through F-EI-16), rebuild of the returned archive, and full QA.
**Decision:** Branch A (frozen instrument byte-identical). Branch B remains UNELECTED and was not executed.
**Date:** July 24, 2026.

## 1. Corrected finding namespace (final)

| ID | Severity | Disposition | Summary |
| --- | --- | --- | --- |
| F-EI-10 | MEDIUM | CLOSED | Audit-trail integrity binding: raws shipped under `historical_inputs/` + `historical-originals-manifest.md`; Fable editions shipped; transformed copy renamed/superseded; README provenance corrected. |
| F-EI-11 | LOW | CLOSED | Phantom finding ID: remediation receipt Section 5 relabeled "Mechanical QA results" with the phantom-ID note. |
| F-EI-12 | LOW | CLOSED | Emitters shipped as auditable build tools; README softened; concordance block-universe defined. |
| F-EI-13 | MEDIUM | ACCEPTED (GPT) | Executable `axsh5_content.BLOCKS` = **166**, not 174. Concordance universe = **116 of 166** (prose subset: p=81, bul=30, authornote=1, box=4). The 50 non-prose blocks: h1=18, source=16, h2=5, prop=3, and eight singletons. Every live governance file now states 116-of-166; "174" preserved only in the historical GPT delta seat report, with live correction notes that 174 is a reviewer-local segmentation count and not the executable BLOCKS count. No instrument byte changed. |
| F-EI-14 | LOW | ACCEPTED (GPT) | Exact editorial-note cardinality: **three** insertions across the two named seat reports (1 Opus, 2 GPT delta) **plus one** in the derived Fable copy. Live manifest/receipt statements corrected. Retention allowed (raws shipped and hash-bound). |
| F-EI-15 | n/a | REJECTED / NOT APPLICABLE | Concerned a local extracted working directory, not a returned-archive member. The archive ships no working directory, `__pycache__`, `.pyc`, or undeclared extraction (QA verified). |
| F-EI-16 | LOW | ACCEPTED (producer self-identified; renumbered from the earlier stale-pointer finding to avoid namespace collision) | Stale live pointers from the F-EI-10b rename SELF-REPAIRED; all live governance pointers resolve. No absence-credit claimed (Ruling 4). |

## 2. Emitter / README wording correction (parent item 6)

The emitters `emit_markdown.py` and `emit_pdf.py` are shipped in-packet and were verified to reproduce the frozen canonical members byte-for-byte in the producer environment. They are now described as **auditable executable build tools**, not turnkey portable scripts: each carries a configurable/absolute output path in its header and `emit_pdf.py` downloads specific fonts at build time, so reproduction requires local path and font configuration. The README and remediation receipt no longer claim unconditional reader reproducibility. The **concordance receipt remains the operative parity guarantee** between the two rendered members, independent of build environment.

## 3. Final QA output (all PASS)

| Check | Result |
| --- | --- |
| Dispatch `sha256sum -c SHA256SUMS` | 6/6 OK |
| Baseline internal `sha256sum -c SHA256SUMS` | 15/15 OK |
| Final internal `sha256sum -c SHA256SUMS` (fresh extract) | 29/29 OK, 0 fail |
| Frozen `is-evidence-independence-an-axiom-canonical.pplx.md` | `fcd1e70d...` (exact) |
| Frozen `is-evidence-independence-an-axiom-canonical.pdf` | `3e757231...` (exact) |
| Frozen `axsh5_content.py` | `d58830c1...` (exact) |
| Emitters reproduce frozen artifacts (isolated configured run) | Markdown YES, PDF YES (byte-for-byte) |
| `qpdf --check` on frozen PDF | No syntax or stream encoding errors |
| Live-new/edited text U+2013/U+2014/U+2015 count | 0 |
| Absolute workspace paths / local-file-URIs in live governance text | 0 |
| Live governance pointers resolve | Yes (to members, `historical_inputs/`, or declared external siblings) |
| Raw historical subtree exemption honored | Yes (`historical_inputs/*` unedited; declared gate-exempt) |
| `__pycache__` / `.pyc` / working directory in archive | 0 (none) |

## 4. Packet composition

- **Members (excluding internal `SHA256SUMS`):** 29
- **Total files in archive (including `SHA256SUMS`):** 30
- **Directories:** packet root + `historical_inputs/` only (no working directory)
- **Block-count fact (F-EI-13):** `axsh5_content.BLOCKS` = 166; concordance content universe = 116.

## 5. Returned artifacts and hashes

- **Final archive:** `axsh5-release-packet-r3.zip`, sha256 **`8d9b8c6f68a5652498d1e5140f8c97f6ef2ce32a7417addc2b470f617cf8ae6e`**
- **External sibling hash receipt:** `AXSH5_R3_RETURN_SHA256SUMS.txt` (final zip sha + three frozen hashes)
- **In-packet authoritative return receipt:** `AXSH5_R3_ABSORPTION_RECEIPT.md`
- **Updated packet-internal `SHA256SUMS`:** inside the archive, covering all 29 members.

Branch B (PDF `/Author` rewrite) remains unelected and was not executed; the disclosed metadata-layer limitation stands as both carrying seats accepted.

---

# Bismillah ir-Rahman ir-Rahim
