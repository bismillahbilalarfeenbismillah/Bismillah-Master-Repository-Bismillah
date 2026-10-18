# Bismillah ir-Rahman ir-Rahim

# R0736 -- S-1 PREREGISTRATION -- Claude Opus 5, Seat B_SHALLOW

**Chronological Index:** 893 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** PREREG_OPUS5_B_SHALLOW_v24.txt  
**Source Format:** txt  
**SHA-256:** `b7fb762d97bae730f9f909b66373feeb04ce7e187f90fae4868c59146fd9674e`  

---

## R0736 · S-1 PREREGISTRATION -- Claude Opus 5, Seat B_SHALLOW

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: PREREG_OPUS5_B_SHALLOW_v24.txt
- source_format: txt
- text_sha256: b7fb762d97bae730f9f909b66373feeb04ce7e187f90fae4868c59146fd9674e

S-1 PREREGISTRATION -- Claude Opus 5, Seat B_SHALLOW
Prior rounds held: v0.20 (fresh), v0.21 (shallow), v0.22 (shallow). NOT held: v0.23.
Frozen before any read of xz_protocol_v0_24.md Section 27.
Basis: PACKET_SHA256SUMS, build.py source + diff against v0.22, build stdout,
packet listing, my three prior reports and three prior packets.

CONTAMINATION: fourth consecutive round in which the dispatch orders build.py
before preregistration. Build stdout leaked pre-freeze: entry count 24,
PRIOR_HISTORY cbacd073..., the [9e] cardinal PASS naming "three / v0.20..v0.22",
the [9f] "Register: 13 items, {HIGH 3, MEDIUM 6, LOW 2, INFORMATIONAL 2}" line
with "21 unique" IDs, and COMPUTED 7 / EXTERNAL 0 / ASSERTED 12 = 63.2%.
Predictions touching those are [CONTAMINATED]. I raised this ordering defect at
v0.20, v0.21 and v0.22; it has never been dispositioned.

--- FROM v0.24 BYTES ---

B1 [BYTES] SHARPEST. build.py [9] carries stale message strings: the conditions
   were bumped to 24 and "twenty-four" but the messages still read
   "(expected 22)" and "Protocol says 'twenty-two'". The build therefore prints
   two self-contradicting green lines:
     PASS: Entries: 24 (expected 22)
     PASS: Protocol says 'twenty-two'
   PREDICT: the v0.24 entry does not name this. It is a new instance of the
   stale-carried-string class the record has committed at v0.20 (governance
   cardinal), v0.21 (24.4% coverage), and v0.22 (coverage series), now landing
   inside the build's own output rather than in prose.

B2 [BYTES] [9f] was restructured -- the "Adjudicated ledger:" anchor is gone and
   the duplicate-ID loop is unconditional within the register block. PREDICT:
   F-OP22S-01 CLOSED and the fix genuinely lands. But two residuals: the block
   still terminates with `check(True, ...)`, an assertion that cannot fail, and
   the outer `if id_sev_pairs:` still has a print-only else. PREDICT the entry
   names neither.

B3 [CONTAMINATED] ASSERTED fell 78.9% -> 63.2% and COMPUTED rose 4 -> 7: the
   first reversal in four rounds. PREDICT the entry reports the fraction, and
   (base rate across v0.21, v0.22) reports the PRIOR round's transition rather
   than its own.

B4 [BYTES] No v0.23 packet ships and no v0.23 seat report ships, though entry
   count 24 means a v0.23 entry exists. PREDICT the v0.24 entry describes a
   v0.23 round whose reports are unverifiable from any shipped file, and my
   chain verification bottoms out one link earlier than at v0.22 -- I can anchor
   v0.23's PRIOR_HISTORY against my held v0.22 file only if the v0.23 entry
   records that value in prose.

--- FROM MEMORY (v0.20/v0.21/v0.22 reports and packets) ---

M1 [MEMORY] F-OP21S-05 / F-OP22S-05: the [9c] file_computed regex is
   byte-identical to v0.21 and v0.22. Verified pre-freeze. PREDICT: absent from
   the register for a second consecutive round, or claimed closed without a byte
   change.

M2 [MEMORY] F-OP22S-06: the cb67f222 hand-populated literal is still present
   (2 occurrences). PREDICT: not dispositioned, or NOTED without removal.

M3 [MEMORY] F-OP22S-07: PDF unbound for a fourth consecutive round; absent from
   PACKET_SHA256SUMS and build.py required_members, verified pre-freeze.
   PREDICT: NOTED again.

M4 [MEMORY] F-OP22S-03 (three F-OP21S IDs absent from the v0.22 register).
   PREDICT: dispositioned this round, and PREDICT no range-versus-register gate
   was added -- none appears in [9f].

M5 [MEMORY] Base rate is one counting or reconciliation error per entry across
   v0.19, v0.20, v0.21, v0.22. PREDICT at least one new one in the v0.24 entry.
   Least confident.

M6 [MEMORY] Silent-skip census fell 19 -> 17. PREDICT the entry claims progress
   on the class without noting that [9f]'s own else-branch remains print-only.

---

# Bismillah ir-Rahman ir-Rahim
