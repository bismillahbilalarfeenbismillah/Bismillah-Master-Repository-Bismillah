# Bismillah ir-Rahman ir-Rahim

# R0676 -- Attestation Report: Flagship v0.13 Narrow Delta

**Chronological Index:** 864 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** model-council-gemini_3_1_pro (19).md  
**Source Format:** md  
**SHA-256:** `792bc2e28b777804a755cd38e325565dd8c79dd10deef6a89d9ac4886fa8cdc3`  

---

## R0676 · Attestation Report: Flagship v0.13 Narrow Delta

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: model-council-gemini_3_1_pro (19).md
- source_format: md
- text_sha256: 792bc2e28b777804a755cd38e325565dd8c79dd10deef6a89d9ac4886fa8cdc3

# Attestation Report: Flagship v0.13 Narrow Delta
## Seat: F-TM-N (Gemini 3.1 Pro)

### A. Seat and Routing Declaration
Verdict-carrying seat Gemini 3.1 Pro, namespace F-TM-N.

### B. Receipts Computed
Computed SHA256 hashes against all dispatched files.
- `Flagship_paper_v0_13_source.md`: 77c1819f5758b1987c4aedc92a7c9deff29e565434c3131a259c6b5474070d14 (Match)
- `Flagship_paper_v0_13.html`: 8f54921b8074bc5154e4fc792083e8d6cdbac65ebc8bab3426049260ffff8113 (Match)
- `Flagship_paper_v0_13.docx`: 27503a90c37bbae638a485797c7c81653c473588c73327a5c2538d9f2fc3ef09 (Match)
- `Flagship_paper_v0_13.pdf`: 7b7589587350209b0f96c0cdde27c4787f447255ca2c83324626c6b37c58c1d0 (Match)
- `Flagship_paper_audit_ledger.md`: 8e25aeb95e24c3873fd294d4cfb970c75717047f2fdd2acb13c6bca25569a520 (Match)
- `Flagship_paper_bibliography.bib`: a0848edcdb56effe19b5c21ffe85ed31412841888f1890cea68c4846cfc3816a (Match)
- `Flagship_paper_punch_list.md`: 8ef1f66d75f6d389252096e0f10dc159e4f42f90ad98d9d5d697b29030daa5f6 (Match)

**Ledger Invariants:**
- `Flagship_paper_audit_ledger.md` first 21,721 bytes hash to `5c5f7b4c2afd0bbd518d60d3a47cc4d059d3f6eef0661f84a1d890a9b19dfbd1` (Match)
- The baseline v0.12 ledger size is 40,831 bytes. Hashing the first 40,831 bytes of the v0.13 ledger matches the v0.12 baseline ledger hash `e8be4c20f4b6819a14e6c405b21f564316f0e05bd2361a8cc4f14ff03ce85827`. (Match)

### C. Leg-by-Leg Results

**L1 Receipts and Chain:**
All member hashes match the provided SHA256SUMS.txt. Both ledger byte-prefix invariants hold. The bibliography and punch list are byte-identical to their v0.12 receipts.

**L2 Source Delta:**
The diff between `baseline_v0_12/Flagship_paper_v0_12_source.md` and `Flagship_paper_v0_13_source.md` consists exactly of the two expected hunks:
1. Line 5 author note label removed: `*Author note (front matter; final wording at F-audit):* Prepared with` and installed: `*Author note:* Prepared with`.
2. Lines 1363-1369 references preface removed and replaced identically to the quoting in the ledger section 11. No other byte differences exist.

**L3 META-TEXT-ABSENCE Gate:**
Following extraction and normalization (whitespace collapse, hyphen-plus-linebreak removal, unescaping source brackets), the source, html, docx, and pdf were checked for the markers: "placeholder", "at build time", "raw markdown", "build profile", "F-audit", "not part of this packet", "Flagship_paper_references.bib". Count is ZERO for all markers across all surfaces.

**L4 Presence Parity:**
Surfaces were checked for the presence markers:
- "Author note: Prepared with": Present
- "body back-reference": **MISSING** (finding generated)
- "zero of forty-four": Present
- "recorded as incomplete rather than resolved": Present
- "Time Horizon 1.1": Present
- "sixteen-percent": **MISSING** (finding generated; the text contains "16-percent" and "16 percent", but not the explicitly spelled-out string "sixteen-percent")
- "accompanying bibliography file, Flagship_paper_bibliography.bib": Present
- References [1]..[35]: Present, no [36]

**L5 Record Integrity:**
The ledger section 11 accurately describes the delta, recording the considered and retained items correctly (Appendix A packet-boundary vocabulary and Section 5.2 provenance-ledger reference). In-packet adjudication records hash to their expected values.

### D. Findings Register
- [F-TM-N-1] L4 Presence Parity Failure -- The exact string "body back-reference" is completely absent across all text surfaces (source, pdf, docx, html). Disconfirming test: Regex searches accounting for whitespace, newlines, and case-insensitivity confirm zero occurrences of the phrase. A manual inspection of the word "back" confirms it does not precede "reference" anywhere in the document. Severity: HIGH.
- [F-TM-N-2] L4 Presence Parity Failure -- The exact string "sixteen-percent" is absent across all surfaces. Disconfirming test: Python regex searches across all surfaces confirm its absence. The phrase "16-percent" exists, and "16 percent" exists, but not the exact specified string "sixteen-percent". Severity: HIGH.

### E. UNKNOWN Register
None.

### F. Verdict
NON-PASS. Adverse gate count: 2.

---

# Bismillah ir-Rahman ir-Rahim
