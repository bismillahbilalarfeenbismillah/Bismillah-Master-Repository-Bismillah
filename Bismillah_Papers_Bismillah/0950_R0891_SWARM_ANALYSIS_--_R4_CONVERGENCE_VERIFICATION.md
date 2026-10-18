# Bismillah ir-Rahman ir-Rahim

# R0891 -- SWARM ANALYSIS -- R4 CONVERGENCE VERIFICATION

**Chronological Index:** 950 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** S02_R4_DISPATCH.txt  
**Source Format:** txt  
**SHA-256:** `5e86ea934b5a87b373f6f9ca31280803e9074bff187b4c9e9e6f18f5cca4e2d4`  

---

## R0891 · SWARM ANALYSIS -- R4 CONVERGENCE VERIFICATION

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: S02_R4_DISPATCH.txt
- source_format: txt
- text_sha256: 5e86ea934b5a87b373f6f9ca31280803e9074bff187b4c9e9e6f18f5cca4e2d4

SWARM ANALYSIS -- R4 CONVERGENCE VERIFICATION
S02 | Kimi K3 | CARRYING (binding) | Mode B | FRESH

R3 HALT (0C 0H 5M 3L). All sentence-level propagation.
R4 build (8pp) applies all 8 fixes. FRESH instance.

ARTIFACT: PAPER.txt

VERIFY EACH R3 FINDING CLOSED:

F-S02-SW3-01: Three populations not in abstract/S1.
  VERIFY: "tens of thousands launched; ~1,200 board; ~700 HF"
  present in BOTH abstract AND Section 1.

F-S02-SW3-02: "48 hours before detection" in Section 1.
  VERIFY: grep "48 hours" = 0. Detection dates (July 16,
  July 19-21) stated separately from operations (July 11-13).

F-S02-SW3-03: "shared Artifactory credential" in S5/S6.
  VERIFY: grep "shared Artifactory credential" = 0.

F-S02-SW3-04: SHV-Bench quotation fidelity in S7.
  VERIFY: Either verbatim-quoted or paraphrased without
  quotation marks.

F-S02-SW3-05: Prevention sentence in S5.
  VERIFY: No "would have prevented." Prerequisite-removal
  wording instead.

F-S02-SW3-06: D5 body/table reconciliation.
  VERIFY: Table row 5 axiom/EC/condition match the D5 body.

F-S02-SW3-07: Duplicated abstract clause.
  VERIFY: No duplicated mapping clause in abstract.

F-S02-SW3-08: "is itself a finding" duplicated.
  VERIFY: Appears at most once.

CONVERGENCE CHECK: If all 8 closed and no new MEDIUM+,
this paper has converged.

FINDING FORMAT: F-S02-SW4-NN
VERDICT: [PASS | CONDITIONAL PASS | HALT]

---

# Bismillah ir-Rahman ir-Rahim
