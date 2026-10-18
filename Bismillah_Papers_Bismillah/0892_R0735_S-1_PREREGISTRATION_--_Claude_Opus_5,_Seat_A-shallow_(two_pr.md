# Bismillah ir-Rahman ir-Rahim

# R0735 -- S-1 PREREGISTRATION -- Claude Opus 5, Seat A-shallow (two prior rounds: v0.20 fresh, v0.21 shallow)

**Chronological Index:** 892 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** PREREG_OPUS5_B_SHALLOW_v22.txt  
**Source Format:** txt  
**SHA-256:** `e55d6313987c1341b5ba8577196489d6d390405e31d717b72f5152e09963e45c`  

---

## R0735 · S-1 PREREGISTRATION -- Claude Opus 5, Seat A-shallow (two prior rounds: v0.20 fresh, v0.21 shallow)

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: PREREG_OPUS5_B_SHALLOW_v22.txt
- source_format: txt
- text_sha256: e55d6313987c1341b5ba8577196489d6d390405e31d717b72f5152e09963e45c

S-1 PREREGISTRATION -- Claude Opus 5, Seat A-shallow (two prior rounds: v0.20 fresh, v0.21 shallow)
Frozen before any read of xz_protocol_v0_22.md Section 27.
Basis: PACKET_SHA256SUMS, build.py source + diff against v0.21, build stdout,
packet listing, and my own v0.20 and v0.21 reports plus both prior packets.

CONTAMINATION DECLARATION:
Third consecutive round in which the dispatch orders build.py before
preregistration. Build stdout has again printed Section 27-derived facts before
I could freeze: entry count 22, "twenty-two", the PRIOR_HISTORY derivation PASS
with value 4a2842d2..., the [9e] cardinal PASS, the [9f] "Register: 14 items,
{HIGH 4, MEDIUM 4, LOW 5, INFORMATIONAL 1}" line, and COMPUTED 4 / EXTERNAL 0 /
ASSERTED 15 = 78.9%. Predictions touching those are [CONTAMINATED].
Predictions sourced from my v0.20/v0.21 reports are [MEMORY]; predictions
derivable only from v0.22 build.py source are [BYTES].

--- FROM v0.22 BYTES ---

B1 [BYTES] SHARPEST. [9f] printed "Register: 14 items, {...}" and then nothing:
   no ledger line, no self-consistency line, no check() at all. Reading the
   source, the only path producing that output shape is ledger_match truthy but
   tally_matches empty -- the regex
   r'Adjudicated ledger:\s*(.*?)(?:\[|$)' is non-greedy and stops at the first
   '[', so if a provenance tag immediately follows the phrase, group(1) is
   empty, no tally is parsed, no check runs, AND the else-branch is skipped.
   PREDICT: the v0.22 entry claims F-OP21S-02 CLOSED with a COMPUTED tag naming
   build.py [9f], while [9f] executed zero assertions on these bytes -- the
   identical failure I raised at v0.21, at the identical locus, by a new
   mechanism.

B2 [BYTES] The duplicate-finding-ID check added for F-OP21S-03 lives in the
   ELSE branch of `if ledger_match:`. Since ledger_match is truthy, that check
   is unreachable on these bytes.
   PREDICT: the entry claims F-OP21S-03 CLOSED via [9f]; the check never runs.

B3 [BYTES] F-OP21S-01 is genuinely fixed. derive_prior_history now recurses:
   when the prose scrape misses at a level, it reconstructs the prior-prior
   file instead of silently omitting the line. Build reports PASS.
   PREDICT: CLOSED and correct in bytes. I will verify against the v0.21
   HISTORY.sha256 I hold (deliverable E), which is the check no other seat can
   perform.

B4 [BYTES] The recursion terminates at v0.19 by searching that entry for
   r'cb67f222[0-9a-f]{56}' -- an eight-character hand-populated literal. D-8
   (as shipped at v0.20/v0.21) prohibits hand-populated comparands, and that
   prohibition is the stated basis of F-OP20F-05.
   PREDICT: the entry does not name this residual literal.

B5 [BYTES/CONTAMINATED] ASSERTED 15/19 = 78.9%, COMPUTED down to 4 from 9.
   PREDICT: the entry reports the fraction and does NOT note that COMPUTED fell
   by more than half while the register grew.

--- FROM v0.20/v0.21 MEMORY ---

M1 [MEMORY] F-OP20F-07 (PDF unbound) still not fixed: xz_protocol_v0_22.pdf is
   absent from PACKET_SHA256SUMS and from build.py required_members, verified
   pre-freeze. PREDICT: NOTED for a third consecutive round.

M2 [MEMORY] F-OP21S-05: the [9c] file_computed regex is byte-identical to
   v0.21's and still captures only the first filename per tag. PREDICT: claimed
   CLOSED or partially closed without the arity limitation being named.

M3 [MEMORY] F-OP21S-06 (silent-skip census): the [9f] rewrite adds new bare
   guards (`if reg_items`, `if ledger_match`, `if tally_matches`). PREDICT: the
   census did not fall.

M4 [MEMORY] F-OP21S-07: the D-8 split landed -- the shipped file is
   AUDIT_DISPATCH_D0_D7.md with zero D-8 occurrences. But
   XZ_v20_SEAT_A_FRESH_REPORT.md and XZ_v21_SEAT_A_SHALLOW_REPORT.md still ship.
   PREDICT: dispositioned as closed in part.

M5 [MEMORY] F-OP21S-04 (stale coverage figures): PREDICT corrected for the v0.21
   values AND at least one new stale or short figure appears in the v0.22 entry.
   Base rate is one counting error per entry across v0.19, v0.20, and v0.21.
   Least confident.

---

# Bismillah ir-Rahman ir-Rahim
