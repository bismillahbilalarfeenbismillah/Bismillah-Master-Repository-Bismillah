# Bismillah ir-Rahman ir-Rahim

# R0896 -- SHV-BENCH PROTOCOL PAPER -- R4 AUDIT DISPATCH

**Chronological Index:** 575 of 995  
**Date:** 2026-08-20  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** S02_SB_R4_DISPATCH.txt  
**Source Format:** txt  
**SHA-256:** `7f19cbd6fc1595417f7fe93099c8736676d036dbe1c53fd3d722265dd25d4e76`  

---

## R0896 · SHV-BENCH PROTOCOL PAPER -- R4 AUDIT DISPATCH

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: S02_SB_R4_DISPATCH.txt
- source_format: txt
- text_sha256: 7f19cbd6fc1595417f7fe93099c8736676d036dbe1c53fd3d722265dd25d4e76

SHV-BENCH PROTOCOL PAPER -- R4 AUDIT DISPATCH
Seat S02 | Moonshot Kimi K3 | CARRYING | Mode B | FRESH
Round R4 | 2026-08-20 | Dispatched by Bilal Syed Arfeen

================================================================
ROLE
================================================================

You are the CARRYING seat. Your verdict is binding.
This is R4: final verification of R3's two findings (1 MEDIUM,
1 LOW). Both repaired. FRESH instance.

================================================================
ARTIFACT
================================================================

SHV_BENCH_PROTOCOL_FINAL.pdf (11 pages).
Companion: SHV_BENCH_TASK_CORPUS_FINAL.csv (1,673 rows).

================================================================
R3 FINDING REGISTER -- VERIFY EACH
================================================================

F-S02-SB3-01 (LOW): Stale "five labels" / "5 closed labels."
  REPAIR: Changed to "six labels" in Section 6.5 opening
  sentence. Section 1.3 departure table changed to
  "6 closed labels + RUN-INVALID."
  VERIFY:
  (a) grep "five labels" -> expected: 0.
  (b) grep "5 closed labels" -> expected: 0.
  (c) Section 6.5 says "six labels."
  (d) Section 1.3 departure table outcome-mapping row says
      "6 closed labels + RUN-INVALID."

F-S02-SB3-02 (MEDIUM): Decision mapping non-total at the
  run-invalidation boundary and infra-fault dual governance.
  REPAIR: Added RUN-INVALID as a run-level outcome outside
  the six-label mapping. Reconciled infra-fault governance:
  session-level faults handled by Section 4.4 fail-closed
  imputation (session stays in ASA); run-level invalidation
  applies ONLY to Type-1-all-fail canary condition. Breach
  disclosure added for NEGATIVE-CAPABILITY + Type-2 breach.
  VERIFY:
  (a) RUN-INVALID defined in Section 6.5 with its trigger
      (all three Type-1 canaries fail under Condition A).
  (b) Infra-fault rule reconciled: session-level faults ->
      Section 4.4 imputation; run-level invalidation -> ONLY
      Type-1-all-fail.
  (c) The totality claim is scoped to valid runs ("total
      over valid runs") not all possible states.
  (d) Breach disclosure rule present for NEGATIVE labels.

================================================================
16-CELL TRUTH TABLE (mandatory re-run)
================================================================

Re-run the 16-cell enumeration from R3 on the AMENDED text.
The cells are:

  E1: {reject, fail}
  E2: {reject, fail}
  Canary: {clean, Type-2-breach, Type-1-all-fail, infra-fault}

  = 2 x 2 x 4 = 16 cells.

For each cell, identify which outcome applies (one of the 6
labels, RUN-INVALID, or UNDERPOWERED) and whether the mapping
is unambiguous.

Report the result as: N/16 cleanly mapped.

The R3 report found 9/16 cleanly mapped. The repair should
yield 16/16 (every cell resolves to exactly one outcome).

If any cell remains unmapped or ambiguous, report it as a
finding.

================================================================
CONSISTENCY CHECK
================================================================

Verify the infra-fault reconciliation does not contradict:
  (a) Section 3.5 (canary rules): does it still say
      infrastructure faults are the only run-invalidation
      trigger? It should now say Type-1-all-fail is the only
      trigger; individual session faults go to Section 4.4.
  (b) Section 4.4 (analysis populations): does it still say
      fail-closed imputation for infrastructure faults?
      It should, unchanged.
  (c) F-SB4: does it reference both Type-1-all-fail and
      Type-2-breach correctly?
  (d) F-SB10: does it reference the 15% missingness cap?

================================================================
CSV VERIFICATION (carry forward)
================================================================

  (a) SHA-256 matches Section 3.1 digest:
      6ad72bd43ffd50658a72b787f7e07b231bb5b6fdd
      181be01573444f885ae48bb
  (b) Classifier self-consistency: apply Section 3.2 keyword
      list to both text fields, count mismatches vs vuln_class.
      Expected: 0.

================================================================
RESIDUAL SCANS (carry forward)
================================================================

  "five labels"                        -> expected: 0
  "5 closed labels"                    -> expected: 0
  "frozen in the SHVVP"                -> expected: 0
  "inherits that specification"        -> expected: 0
  "Mann-Whitney"                       -> expected: 0
  "pooled median"                      -> expected: 0
  "inherited"                          -> expected: 0
  "inheriting"                         -> expected: 0

================================================================
FINDING FORMAT
================================================================

  ID:              F-S02-SB4-NN
  SEVERITY:        CRITICAL | HIGH | MEDIUM | LOW
  LOCUS:           Section and paragraph
  SUBSTANCE:       What is wrong
  DISPOSITION:     OPEN
  CROSS-REFERENCE: Which R3 finding

================================================================
VERDICT FORMAT
================================================================

VERDICT: [PASS | CONDITIONAL PASS | HALT]

R3 FINDING DISPOSITIONS:
  F-S02-SB3-01: [CLOSED / REOPENED]
  F-S02-SB3-02: [CLOSED / REOPENED]

16-CELL TRUTH TABLE: [N/16 cleanly mapped]
CONSISTENCY CHECK: [per item (a)-(d)]
CSV: [digest match + classifier mismatches]
RESIDUAL SCANS: [all counts]
NEW FINDING COUNT: [N]
BLIND SPOT: [one sentence]

FINDINGS: [any new findings]
SUMMARY: [one paragraph]

---

# Bismillah ir-Rahman ir-Rahim
