# Bismillah ir-Rahman ir-Rahim

# R0729 -- bayyinah_v0 vs bayyinah_v0_1 — PARITY REGRESSION REPORT

**Chronological Index:** 174 of 995  
**Date:** 2026-04-21  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** parity_summary.txt  
**Source Format:** txt  
**SHA-256:** `ca93bea80a1c0e88c34d8dd66f91d90b5ee2b239bbe6866b858da20e74d0ed4a`  

---

## R0729 · bayyinah_v0 vs bayyinah_v0_1 — PARITY REGRESSION REPORT

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: parity_summary.txt
- source_format: txt
- text_sha256: ca93bea80a1c0e88c34d8dd66f91d90b5ee2b239bbe6866b858da20e74d0ed4a

bayyinah_v0 vs bayyinah_v0_1 — PARITY REGRESSION REPORT
========================================================
Date: 2026-04-21
Harness: /sessions/peaceful-vibrant-babbage/mnt/outputs/run_parity.py
Normalization: pypdf IndirectObject(n, g, <id>) strings stripped
               (pypdf's __repr__ embeds id(doc) which varies every run —
                two back-to-back v0 runs diverge at this field too)

RESULT: 33 files PASS, 0 DIFF, 0 FAIL
All findings, scores, error strings, scan_incomplete flags, tier legends,
and verdict disclaimers match byte-for-byte.

                                                   v0       v0.1
FILE                                   findings    score    score   result
─────────────────────────────────────  ────────   ──────   ──────   ──────
positive_test.pdf                          9       0.0      0.0     PASS
The_Differentiator_Framework.pdf           .       .        .       PASS
Naus-V1-A / V1-B / V1-C / V1-D             .       .        .       PASS (×4)
Naus-V2-A / V2-B / V2-C / V2-D             .       .        .       PASS (×4)
AIGuardPDF sample-PDF.pdf                  .       0.0      0.0     PASS
Simple PDF 2.0 file.pdf                    .       .        .       PASS
PDF 2.0 with offset start.pdf              .       .        .       PASS
pdf20-utf8-test.pdf                        .       .        .       PASS
test1 / test1_1 / test3 / test10           .       .        .       PASS (×4)  (silent scan_error path)
test15 / test17 / test28 / test29          .       .        .       PASS (×4)
Akira Book 01.pdf                        605       0.0      0.0     PASS
Akira Book 02.pdf                        492       0.0      0.0     PASS
Akira Book 03.pdf                        476       0.0      0.0     PASS
Akira Book 04.pdf                        715       0.0      0.0     PASS
Akira Book 05.pdf                        664       0.0      0.0     PASS
Akira_Book_01..04 _Analysis.pdf            .       .        .       PASS (×4)
Akira_Book5_Analysis.pdf                   .       .        .       PASS
Akira_Book6_Final_Synthesis.pdf            .       .        .       PASS

Total: 33 PASS / 33 tested.

Verdict: bayyinah_v0_1.py is byte-identical to bayyinah_v0.py under the
representative corpus. The modular refactor (BaseAnalyzer / PDFContext /
ScanService) is safe to adopt as the new reference implementation.

Notes:
- Prior regression calibration (Akira OCR down-tier, scan_incomplete clamp,
  Nausicaä baseline, AIGuardPDF=0.000) is preserved in full.
- The silent-scan_error path (v0 behavior when pypdf cannot open but fitz can)
  is preserved in v0.1 via PDFContext.try_pypdf() returning (None, exc) and
  ObjectLayerAnalyzer emitting the same scan_error finding.
- Pre-existing non-determinism from pypdf's IndirectObject.__repr__ (id-based)
  is inherited unchanged. Not a v0.1 regression. A follow-up patch could
  stringify IndirectObject via (idnum, generation) to remove this noise from
  both v0 and v0.1 if reproducible JSON output is later required.

Next candidate tasks:
- Adopt v0.1 as the canonical scanner (rename v0 → v0_legacy, v0.1 → v0?).
- Split TextLayerAnalyzer and ObjectLayerAnalyzer into per-mechanism analyzers
  for ablation studies.

---

# Bismillah ir-Rahman ir-Rahim
