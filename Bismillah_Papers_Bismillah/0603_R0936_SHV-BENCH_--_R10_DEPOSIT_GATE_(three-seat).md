# Bismillah ir-Rahman ir-Rahim

# R0936 -- SHV-BENCH -- R10 DEPOSIT GATE (three-seat)

**Chronological Index:** 603 of 995  
**Date:** 2026-08-22  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** S04_R10_DISPATCH.txt  
**Source Format:** txt  
**SHA-256:** `7f642d50d8771d795822d07e77b59c17cfa64ca9f8ffd902a450111aea02c833`  

---

## R0936 · SHV-BENCH -- R10 DEPOSIT GATE (three-seat)

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: S04_R10_DISPATCH.txt
- source_format: txt
- text_sha256: 7f642d50d8771d795822d07e77b59c17cfa64ca9f8ffd902a450111aea02c833

SHV-BENCH -- R10 DEPOSIT GATE (three-seat)
S04 | Gemini 3.1 Pro | ADVISORY | FRESH | 2026-08-22

Advisory. FRESH. You returned PASS on R9 with 0 findings. R10
absorbed 4 more adversarial findings. Verify the changes and
confirm readability.

ARTIFACT: SHV_BENCH_PROTOCOL_R10.pdf + SHV_BENCH_TASK_CORPUS_DEPOSIT.csv

CHANGES SINCE R9:
1. Eligibility manifests (Tier 2/3) added to Section 10.
2. Wilcoxon: single permutation-based conditional exact test,
   replaces scipy. Pratt zeros corrected. Same algo in power
   sim and primary analysis.
3. Fixed N=800 always. Power sim diagnostic only.
4. BH standard step-up rule.

VERIFY: (a) Section 10 row count (17). (b) Readability of
Wilcoxon conventions block. (c) Fixed-N language clear.
(d) BH step-up clear. (e) CSV digest match. (f) No
effectiveness verbs. (g) Imputation still correct.

VERDICT: [PASS | CONDITIONAL PASS | HALT]
SECTION 10: [COMPLETE / INCOMPLETE]
READABILITY: [per item CLEAR / ADEQUATE / UNCLEAR]
NEW FINDINGS: [N]
SUMMARY: [one paragraph]

---

# Bismillah ir-Rahman ir-Rahim
