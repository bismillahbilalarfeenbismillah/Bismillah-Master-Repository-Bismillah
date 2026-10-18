# Bismillah ir-Rahman ir-Rahim

# R0892 -- SHV-BENCH -- R10 DEPOSIT GATE (three-seat)

**Chronological Index:** 592 of 995  
**Date:** 2026-08-22  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** S02_R10_DISPATCH.txt  
**Source Format:** txt  
**SHA-256:** `6fa5acd4a4e7b242ed0e272b0c9392ac251f3abc46250ba7cdc68a87bf976863`  

---

## R0892 · SHV-BENCH -- R10 DEPOSIT GATE (three-seat)

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: S02_R10_DISPATCH.txt
- source_format: txt
- text_sha256: 6fa5acd4a4e7b242ed0e272b0c9392ac251f3abc46250ba7cdc68a87bf976863

SHV-BENCH -- R10 DEPOSIT GATE (three-seat)
S02 | Kimi K3 | CARRYING | FRESH | 2026-08-22

Carrying seat. Binding verdict. You last saw R5 (PASS, 0 findings).
Five adversarial rounds since then absorbed 23 findings. This is
the deposit-candidate build (15pp). FRESH instance.

ARTIFACT: SHV_BENCH_PROTOCOL_R10.pdf + SHV_BENCH_TASK_CORPUS_DEPOSIT.csv

KEY ITEMS TO VERIFY:

(a) CSV SHA-256 = 6ad72bd43ffd50658a72b787f7e07b231bb5b6fdd
    181be01573444f885ae48bb. Row count = 1,673. Classifier
    self-consistency: apply Section 3.2 keywords to both text
    fields, mismatches = 0.

(b) Section 10 pre-run obligations table: count rows. Should
    be 17. All load-bearing artifacts present (including
    eligibility manifests, oracle harness, primary analysis
    code).

(c) Decision mapping: Section 6.5 precedence list. 7 rules.
    32/32 cell resolution.

(d) Imputation: Section 4.4. Missing Condition A: UEC=0,
    WSDS=1.0. Missing Condition B: UEC=U_max, WSDS=0. Trace
    the math -- both push AWAY from positive BSSG result.

(e) Fixed N=800 confirmatory design: Section 4.3 and 6.4.
    Power simulation is diagnostic only. No variable N.

(f) Wilcoxon algorithm: Section 10 conventions block.
    Pratt zeros, permutation-based conditional exact test,
    same algorithm in power sim and primary analysis.

(g) BH step-up: Section 10. Largest-k rule, not individual.

(h) Rubric immutable: Section 5.1. Kappa failure -> UNSCORABLE.

(i) Seeds independent: Section 4.3. Both from crypto RNG at
    manifest assembly. No outcome dependence.

(j) No effectiveness verbs. No "non-canary" endpoint recomp.

VERDICT: [PASS | CONDITIONAL PASS | HALT]
Section 10: [N rows]
32-CELL: [N/32]
CSV: [digest + mismatches]
NEW FINDINGS: [N]
BLIND SPOT: [one sentence]
SUMMARY: [one paragraph]

---

# Bismillah ir-Rahman ir-Rahim
