# Bismillah ir-Rahman ir-Rahim

# R0848 -- Dissertation v1.1 Propagation — Substrate Package Manifest

**Chronological Index:** 297 of 995  
**Date:** 2026-07-21  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** README_MANIFEST.md  
**Source Format:** md  
**SHA-256:** `45ec14908008b682f9a4c3dc119f62ff68645fcbfe5c93604570c25cd0aee894`  

---

## R0848 · Dissertation v1.1 Propagation — Substrate Package Manifest

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: README_MANIFEST.md
- source_format: md
- text_sha256: 45ec14908008b682f9a4c3dc119f62ff68645fcbfe5c93604570c25cd0aee894

# Dissertation v1.1 Propagation — Substrate Package Manifest

**Prepared:** July 21, 2026
**Prepared by:** Bilal Syed Arfeen (primary author, BayyinahEnterprise)
**Purpose:** substrate package for council-verification of the dissertation v1.1 mechanical propagations and staged judgment-laden items

---

## Package contents

```
├── README_MANIFEST.md                                     (this file)
├── Dissertation_v1_1_Council_Dispatch_Packet.md           (full propagation record + per-item verification predicates)
│
├── governing_methodology/
│   ├── PMD_v1_8.md                                        (Predictive Modeling Discipline v1.8, markdown source)
│   ├── PMD_v1_8.pdf                                       (Predictive Modeling Discipline v1.8, deposited PDF)
│   └── SHV_Method_v1_1.pdf                                (Structural Honesty Verification Method v1.1)
│
├── flagship_v0_11/
│   ├── Flagship_paper_v0_11_publication.pdf               (CONVERGED AND FROZEN venue-facing paper)
│   ├── Flagship_paper_v0_11_publication.docx              (source-of-truth docx)
│   ├── Flagship_paper_references.bib                      (flagship's frozen bibliography, 35 entries)
│   ├── SHV_Flagship_Audit_Ledger_v0_11.md                 (per-version provenance record)
│   └── SHV_Flagship_Punch_List.md                         (post-convergence open items P-1 through P-10)
│
└── dissertation_v1_1/
    ├── Structural_Honesty_Dissertation_v1_1_canonical.md  (5306 lines, propagations applied)
    ├── Structural_Honesty_Dissertation_v1_1_canonical.txt (identical to .md, plain-text extension for seat ingest)
    ├── Structural_Honesty_Dissertation_v1_1_refs.bib      (73 entries, propagations applied)
    └── Structural_Honesty_Dissertation_v1_1_refs.txt      (identical to .bib, plain-text extension)
```

---

## Receipt discipline — SHA256 hashes

### Substrate under audit (dissertation v1.1)
```
d6c672a62329e0b05252cbea288016b393f77722a5009e97a7e4a2affaf63027  Structural_Honesty_Dissertation_v1_1_canonical.md
998c05cca4d428aff245a1555c96a4412e2aca8514879306a49818af8f623a41  Structural_Honesty_Dissertation_v1_1_refs.bib
```

### Flagship v0.11 (propagation source of truth — matches flagship audit ledger §1 frozen receipts)
```
56c8e245a8ae15f9051651f41a8c0efad4593a14486f042328c4bfeb48f9a021  Flagship_paper_references.bib
a17046c45b5502606ae8ac8042869f627a8f53b08a23f848de097556f7fb6161  Flagship_paper_v0_11_publication.pdf
6a280a1369ec0d28dcfd4c08303e59cec05a3bf7ee643d253663e2c1cd792db6  Flagship_paper_v0_11_publication.docx
5c5f7b4c2afd0bbd518d60d3a47cc4d059d3f6eef0661f84a1d890a9b19dfbd1  SHV_Flagship_Audit_Ledger_v0_11.md
8ef1f66d75f6d389252096e0f10dc159e4f42f90ad98d9d5d697b29030daa5f6  SHV_Flagship_Punch_List.md
```

### Governing methodology
```
cd2889405f8e8ebb671a1b70cb35581dae6284dd39db8be23febc31e1c39f2ed  PMD_v1_8.md
4a139ecce54cb32b071f601300524deff4d2304a342e3d6c01c6bba320b609aa  PMD_v1_8.pdf
8f8b43584219a52802f8ace4b4e49021448366b2a044b281ada00ba5762a8896  SHV_Method_v1_1.pdf
```

**Cross-reference:** the `Flagship_paper_references.bib`, `Flagship_paper_v0_11_publication.docx`, `Flagship_paper_v0_11_publication.pdf`, and `SHV_Method_v1_1.pdf` hashes above are bit-identical to the frozen-receipt hashes recorded in `SHV_Flagship_Audit_Ledger_v0_11.md` §1. This confirms these files are the flagship's own canonical substrate, not derivatives.

---

## How the package fits together

**Governing methodology (`governing_methodology/`)** establishes the discipline the propagation obeys. Specifically:
- `PMD_v1_8.md` §3A.12.4(c) defines the mechanical-propagation admissibility rule (reproducible-verifiable propagations bind regardless of vendor).
- `PMD_v1_8.md` §3A.12.4(b) defines the judgment-laden producer-discount rule (same-vendor-family verdicts on interpretive items are discounted).
- `PMD_v1_8.md` §3A.10 defines M1.5 append-only provenance discipline (why the v1.0 amendment note is preserved unchanged and the v1.1 note supersedes-not-rewrites).
- `PMD_v1_8.md` §3B.3 defines the multi-vendor rotation discipline (why parallel Perplexity + Kimi dispatch).
- `SHV_Method_v1_1.pdf` establishes the eight-discipline audit methodology the flagship's convergence-verification instantiated.

**Flagship v0.11 (`flagship_v0_11/`)** is the propagation source of truth:
- `Flagship_paper_v0_11_publication.pdf` is the CONVERGED AND FROZEN venue-facing paper whose corrections were mechanically propagated to the dissertation.
- `SHV_Flagship_Audit_Ledger_v0_11.md` §3 contains the Standing Rulings Register (six rulings) that governs this dispatch's verdict authority — particularly Ruling 3 (lineage exclusions) and Ruling 5 (fresh-seat admissibility with UNKNOWN-BY-CAPABILITY discipline).
- `SHV_Flagship_Audit_Ledger_v0_11.md` §4 contains the flagship's own per-version provenance record with preserved-verbatim REPLACED wordings for every correction — this is the specific ground truth each mechanical propagation is verified against.

**Dissertation v1.1 (`dissertation_v1_1/`)** is the substrate under audit. The v1.1 amendment note at the top of `canonical.md` (lines 3-23) records every propagation applied; the canon body (lines 25+) contains the propagated content.

**Dispatch packet (`Dissertation_v1_1_Council_Dispatch_Packet.md`)** provides the full per-item verification predicates for both mechanical items (M1a-M4) and staged judgment-laden items (J1-J3). The two dispatch briefs (delivered separately to Perplexity and Kimi) are compressed views of this packet targeted at their respective interfaces.

---

## The two dispatch briefs (delivered separately)

**Perplexity Council Dispatch Brief** — structured for parallel multi-seat rotation. Recommended pool: GPT-5.6 Sol, Grok 4.5, GLM 5.2-based Preview, plus Sonnet 5 as advisory (Ruling 3 Anthropic exclusion). Grok is Ruling-3-excluded from verdicts on M1b, J2, J3 (Munafiq contributor lineage).

**Kimi K2.6 High Dispatch Brief** — structured for Kimi as fresh-seat under Ruling 5. Kimi is bind-eligible on all items; empowered to declare UNKNOWN-BY-CAPABILITY on any item its capability envelope cannot verify. Kimi's participation in this dispatch is one of the first empirical instances of Ruling 5 being applied outside the flagship's own convergence round.

Both briefs reference this package as substrate; the seats read this package and produce structured seat reports per their brief's Section C format.

---

## Timeline

**Dispatch (day 0):** send this package plus the two briefs to Perplexity and Kimi. Both dispatches run in parallel.

**Return (days 5-10):** seat reports return. Perplexity synthesis (or manual aggregation) collates verdicts across the council. Kimi's single-seat report is aggregated alongside.

**Disposition (days 10-14):** producer-instance (Claude Opus 4.7) drafts a disposition document. APPLY-AS-DRAFTED J-items land as canon via v1.2 promotion-pass amendment note. APPLY-WITH-EDITS J-items are revised and re-dispatched (round two). DECLINE items are withdrawn or re-routed.

**Convergence declaration (days 14-18):** if aggregate verdict is convergence-ready (3-of-4 non-lineage-excluded seats OK on all mechanical items, 3-of-4 APPLY on all J-items), the dissertation is promoted to v1.2 with new SHA256 receipts and the package is re-frozen. Otherwise, second round.

---

## Governing methodology basis

**PMD v1.8** — full-file governance for the propagation. Key sections seats should reference:
- §3A.10 (M1.5 append-only provenance)
- §3A.12.4 (verdict-type differentiation: mechanical vs judgment-laden)
- §3B.3 (multi-vendor rotation)
- §5.1 (producer-instance discipline)

**Flagship v0.11 Standing Rulings Register** (in `SHV_Flagship_Audit_Ledger_v0_11.md` §3) — supplements PMD v1.8 with six rulings emerging from the flagship's convergence process. All six apply to this dispatch.

**SHV Method v1.1** — background on the eight-discipline audit methodology the whole research program operates under.

---

*End of manifest. Seats should read this file first, then the dispatch packet, then their specific brief, before beginning verification.*

---

# Bismillah ir-Rahman ir-Rahim
