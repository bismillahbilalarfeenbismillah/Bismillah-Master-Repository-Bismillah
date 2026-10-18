# Bismillah ir-Rahman ir-Rahim

# R0739 -- PRIOR ROUND TRIAGE SUMMARY (R17-R20)

**Chronological Index:** 896 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** PRIOR_TRIAGE.txt  
**Source Format:** txt  
**SHA-256:** `93556b177daf8f12c0ad994294f2e9e276f219d80504573046e560c878620cd7`  

---

## R0739 · PRIOR ROUND TRIAGE SUMMARY (R17-R20)

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: PRIOR_TRIAGE.txt
- source_format: txt
- text_sha256: 93556b177daf8f12c0ad994294f2e9e276f219d80504573046e560c878620cd7

PRIOR ROUND TRIAGE SUMMARY (R17-R20)
XZ Protocol Audit Program
For context only -- you are auditing v0.62, not these prior versions.

R17 (v0.58, 5 seats): 5/5 HALT. Class A on Section 22.2/22.3 version-token
staleness, findings[] inert, secondary membership unimplemented. CI v0.2.1.

R18 (v0.59, 10 seats): 10/10 HALT. Class A on findings[] semantically inert
for severity derivation, correction-letter namespace collision, Section
22.2/22.3 staleness (6th occurrence). CI v0.2.2.

R19 (v0.60, 10 seats): 10/10 HALT. Class A on source-severity distribution
not load-bearing, correction (ch) never landed (CLOSED claim false on bytes),
VERSION-1 gate claimed but absent, dangling convergence_group values.
S04C definitive: "The Class A defects are not in the mechanism; they are
in the hand-written claims about the mechanism and about corrections that
did not land." CI v0.3.

R20 (v0.61, 10 seats): 10/10 HALT. Class A on M3 receipt enforcement
(majority-only, substring validation), seat-count parser (ID parsing not
authoritative field), noted-finding dangling bypass, bidirectional membership
parity. S02C exhaustive 75/75 M2 battery proved discriminator convergence.
CI v0.3.1.

PATTERN: Each CI version closes the prior version's gap and introduces a
new one. The gap is always between the docstring (what the code claims to
do) and the code (what it actually does). H = 1.0 across R7-R20 (14 rounds).
Laplace P(Class A at R21) = 15/16 = 0.9375.

DEFECT MIGRATION: R7-R12 register formatting -> R13-R15 body prose ->
R16 narrative+spec-impl -> R17 body+spec-impl -> R18 spec-impl in CI +
cursor collision -> R19 unlanded corrections + missing gate -> R20 receipt
semantics + parser fidelity. Surface narrowing is monotonic.

CURRENT STATE: v0.62 DRAFT CANDIDATE, CI v0.3.2. R21 dispatches shipped
(10 seats), awaiting returns. This dispatch is a FRESH audit of v0.62.

---

# Bismillah ir-Rahman ir-Rahim
