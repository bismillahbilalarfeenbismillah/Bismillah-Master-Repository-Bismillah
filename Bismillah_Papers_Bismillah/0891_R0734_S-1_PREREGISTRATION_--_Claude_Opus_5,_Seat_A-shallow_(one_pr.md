# Bismillah ir-Rahman ir-Rahim

# R0734 -- S-1 PREREGISTRATION -- Claude Opus 5, Seat A-shallow (one prior round: v0.20)

**Chronological Index:** 891 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** PREREG_OPUS5_B_SHALLOW.txt  
**Source Format:** txt  
**SHA-256:** `448a88c281cd3dcc3fb11d4dae8d49624e8b5ca02cf5d0c30cc873f86e72974c`  

---

## R0734 · S-1 PREREGISTRATION -- Claude Opus 5, Seat A-shallow (one prior round: v0.20)

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: PREREG_OPUS5_B_SHALLOW.txt
- source_format: txt
- text_sha256: 448a88c281cd3dcc3fb11d4dae8d49624e8b5ca02cf5d0c30cc873f86e72974c

S-1 PREREGISTRATION -- Claude Opus 5, Seat A-shallow (one prior round: v0.20)
Frozen before any read of xz_protocol_v0_21.md Section 27.
Basis: PACKET_SHA256SUMS, build.py source + stdout, packet file listing, and my
own v0.20 report. No v0.17/v0.18/v0.19 packet bytes held.

CONTAMINATION DECLARATION:
(a) The dispatch again orders build.py (step 2) before preregistration
    (deliverable F). build.py stdout again prints Section 27-derived facts:
    entry count 21, "twenty-one", all 21 seal labels, PRIOR_HISTORY derivation
    PASS with value e181d642..., the [9e] cardinal PASS naming "four /
    v0.16..v0.19", the empty [9f] section, and COMPUTED 9 / EXTERNAL 0 /
    ASSERTED 12 = 57.1%. This is the same ordering defect I recorded at v0.20;
    it was not fixed. Predictions touching those values are marked
    [CONTAMINATED].
(b) I hold my own v0.20 report. Predictions sourced from it are marked [MEMORY].
    Predictions derivable only from v0.21 bytes are marked [BYTES].

--- FROM v0.20 MEMORY ---

M1 [MEMORY] F-OP20F-07 (PDF unsealed) is NOT fixed in bytes: xz_protocol_v0_21.pdf
   is absent from PACKET_SHA256SUMS and absent from build.py required_members
   (both confirmed pre-freeze). PREDICT: the v0.21 entry either omits it or
   claims a disposition the bytes do not support.

M2 [MEMORY] F-OP20F-01 was fixed by deleting the self-entry, which makes
   sha256sum -c return 0 but leaves PACKET_SHA256SUMS with no integrity anchor
   anywhere in the packet. PREDICT: the entry claims CLOSED and does not name
   the residual gap.

M3 [MEMORY] F-OP20F-04's new [9c] guard uses
   \[COMPUTED:\s*sha256sum\s+(?:of\s+)?(\S+\.(?:md|py|json)) which captures only
   the FIRST filename in a multi-file tag. PREDICT: claimed CLOSED; the
   second-file case remains uncovered.

M4 [MEMORY] F-OP20F-06 (narrow the Section 22.2 self-consistent-forgery
   statement) is cheap prose. PREDICT: dispositioned, and the narrowing lands.

M5 [MEMORY] F-OP20F-10 (D-8 ships to auditors) NOT fixed:
   AUDIT_DISPATCH_DISCIPLINE_v2.md ships again in this packet. PREDICT: entry
   marks it NOTED or CLOSED without the file actually being split.

M6 [CONTAMINATED] F-OP20F-11: EXTERNAL count still 0. Observed pre-freeze.

--- FROM v0.21 BYTES ---

B1 [BYTES] SHARPEST. build.py [9f] (the F-OP20F-03 fix) printed its heading and
   ZERO check lines. Its checks are guarded by `if ledger_match:` on the literal
   string "Adjudicated ledger:", and nothing appends an error when absent. So
   the gate written to close F-OP20F-03 is itself an instance of F-OP20F-08 --
   a conditional gate that silently no-ops -- and it no-ops on these very bytes.
   PREDICT: the v0.21 entry claims F-OP20F-03 CLOSED with a COMPUTED tag naming
   build.py [9f], while [9f] executed zero assertions.

B2 [BYTES] derive_prior_history() recovers the prior PRIOR_HISTORY value by
   regex-scraping "PRIOR_HISTORY" followed by a 64-hex on the same line out of
   the PRIOR ENTRY'S PROSE. The build's historical-integrity control is
   therefore coupled to narrative text in an append-only entry. PREDICT: the
   v0.21 entry does not state this coupling. Secondary: if the v0.21 entry does
   not itself contain a PRIOR_HISTORY + 64-hex on one line, the v0.22 build
   breaks. I will check both.

B3 [BYTES] [9e] fired exactly once, on "four ... (v0.16 through v0.19)".
   PREDICT: F-OP20F-02 is genuinely fixed in bytes, cardinal restored to "four".

B4 [BYTES] This packet ships XZ_v20_SEAT_A_FRESH_REPORT.md, PREREG_OPUS5_FRESH.txt,
   and xz_v20_fresh_seat_probes.py. The dispatch states an identical packet goes
   to a deep-continuous seat AND an entirely fresh seat. A fresh seat receiving a
   prior seat's complete findings register is not fresh on findings. PREDICT: not
   dispositioned anywhere in the entry; this is a D-0 leakage defect in the v0.21
   dispatch architecture, not the producer's text.

B5 [BYTES] ASSERTED fraction rose 50.0% -> 57.1% and COMPUTED fell 11 -> 9.
   PREDICT: the entry reports the fraction as disclosure without noting the
   direction of travel across two rounds.

B6 [BYTES] Base rate over v0.19 and v0.20 is one arithmetic or reconciliation
   error per entry, both caught only by side-by-side reading. PREDICT: at least
   one new counting or reconciliation error in the v0.21 entry. Least confident.

---

# Bismillah ir-Rahman ir-Rahim
