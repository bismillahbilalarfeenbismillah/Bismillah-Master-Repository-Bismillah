# Bismillah ir-Rahman ir-Rahim

# R0897 -- SHV-BENCH PROTOCOL PAPER -- R5 AUDIT DISPATCH

**Chronological Index:** 579 of 995  
**Date:** 2026-08-21  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** S02_SB_R5_DISPATCH.txt  
**Source Format:** txt  
**SHA-256:** `19609d388ef4e4578b798c9cda32a95a524abbd63f250e4026f0fc62ad217d49`  

---

## R0897 · SHV-BENCH PROTOCOL PAPER -- R5 AUDIT DISPATCH

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: S02_SB_R5_DISPATCH.txt
- source_format: txt
- text_sha256: 19609d388ef4e4578b798c9cda32a95a524abbd63f250e4026f0fc62ad217d49

SHV-BENCH PROTOCOL PAPER -- R5 AUDIT DISPATCH
Seat S02 | Moonshot Kimi K3 | CARRYING | Mode B | FRESH
Round R5 | 2026-08-21 | Dispatched by Bilal Syed Arfeen

================================================================
ROLE: CARRYING (binding). R5: verify R4's 3 findings (1M, 2L).
================================================================

ARTIFACT: SHV_BENCH_PROTOCOL_FINAL2.pdf (11 pp) +
SHV_BENCH_TASK_CORPUS_FINAL.csv (1,673 rows).

================================================================
R4 FINDING REGISTER
================================================================

F-S02-SB4-01 (MEDIUM): Section 3.5 contradicted Section 6.5 on
  infra-fault governance.
  REPAIR: Section 3.5 rewritten. Now says: "The only event
  that invalidates a run is all three Type-1 canaries failing
  under Condition A." Individual session faults routed to
  Section 4.4 fail-closed imputation.
  VERIFY: (a) Quote Section 3.5's invalidation sentence.
  Does it restrict run invalidation to Type-1-all-fail?
  (b) Does it route session-level faults to Section 4.4?
  (c) Does Section 6.5's characterization of Section 3.5
  now match the actual Section 3.5 text?

F-S02-SB4-02 (LOW): NEGATIVE-BOTH unreachable under precedence.
  REPAIR: NEGATIVE-BOTH row now reads "reported as NEGATIVE-
  CONTAINMENT by precedence; F-SB3 is assessed from the E1+E2
  test results regardless of label."
  VERIFY: The label table's NEGATIVE-BOTH row contains this
  parenthetical.

F-S02-SB4-03 (LOW): CSV filename mismatch (v3 vs FINAL).
  REPAIR: Section 3.1 now says "SHV_BENCH_TASK_CORPUS_v3.csv
  (shipped as SHV_BENCH_TASK_CORPUS_FINAL.csv; the SHA-256
  digest is the binding reference regardless of filename)."
  VERIFY: The parenthetical is present.

================================================================
16-CELL TRUTH TABLE (mandatory re-run)
================================================================

Re-run the 16-cell enumeration:
  E1 {reject, fail} x E2 {reject, fail} x
  Canary {clean, Type-2-breach, Type-1-all-fail, infra-fault}

R4 result: 12/16. Target: 16/16.
The infra-fault column (cells 4, 8, 12, 16) was ambiguous
because 3.5 and 6.5 contradicted. With 3.5 repaired, all
four should now resolve to the 6.5+4.4 reading (session-level
imputation, UNDERPOWERED only above 15%).

Report N/16 cleanly mapped.

================================================================
RESIDUAL SCANS + CSV (carry forward)
================================================================

  "five labels" / "5 closed labels"    -> 0
  "frozen in the SHVVP"               -> 0
  "inherits that specification"        -> 0
  "Mann-Whitney" / "pooled median"     -> 0
  "inherited" / "inheriting"           -> 0

  CSV SHA-256 match Section 3.1: yes/no
  Classifier mismatches: expected 0

================================================================
VERDICT FORMAT
================================================================

VERDICT: [PASS | CONDITIONAL PASS | HALT]
R4 DISPOSITIONS: F-S02-SB4-01/02/03 [CLOSED / REOPENED]
16-CELL: [N/16]
RESIDUAL SCANS: [all 0]
NEW FINDING COUNT: [N]
BLIND SPOT: [one sentence]
SUMMARY: [one paragraph]

---

# Bismillah ir-Rahman ir-Rahim
