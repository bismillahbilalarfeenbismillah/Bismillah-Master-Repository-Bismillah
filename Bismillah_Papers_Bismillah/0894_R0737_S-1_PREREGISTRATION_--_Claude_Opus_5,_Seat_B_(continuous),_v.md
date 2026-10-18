# Bismillah ir-Rahman ir-Rahim

# R0737 -- S-1 PREREGISTRATION -- Claude Opus 5, Seat B (continuous), v0.32 FREEZE CANDIDATE

**Chronological Index:** 894 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** PREREG_OPUS5_B_v32.txt  
**Source Format:** txt  
**SHA-256:** `ff91494a344d0307a02f30f90b3870ce93a376a32599bdf62afcbbf537108f2d`  

---

## R0737 · S-1 PREREGISTRATION -- Claude Opus 5, Seat B (continuous), v0.32 FREEZE CANDIDATE

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: PREREG_OPUS5_B_v32.txt
- source_format: txt
- text_sha256: ff91494a344d0307a02f30f90b3870ce93a376a32599bdf62afcbbf537108f2d

S-1 PREREGISTRATION -- Claude Opus 5, Seat B (continuous), v0.32 FREEZE CANDIDATE
Prior packets held: v0.20, v0.21, v0.22, v0.24, v0.25, v0.27, v0.28.
NOT held: v0.23, v0.26, v0.29, v0.30, v0.31.
Prior reports: F-OP20F-*, F-OP21S-*, F-OP22S-*, F-OP24S-*, F-OP25S-*, F-OP27S-*, F-OP28S-*.
Frozen before any read of xz_protocol_v0_32.md Section 27.
Basis: PACKET_SHA256SUMS, build.py source + diff against v0.28, build stdout,
packet listing, cover note, seven prior reports and seven prior packets.

CONTAMINATION: eighth consecutive round in which the execution order puts
build.py before preregistration, and this time the cover note also states the
conclusions in advance (FROZEN, FB-7b amended, EXTERNAL above zero, eight-seat
round, thirteen-item register, corrections (q)(r)(s)). Leaked pre-freeze:
COMPUTED 0 / EXTERNAL 2 / ASSERTED 20 = 90.9%; register 13 parsed == 13
declared; ungated share 53.3%; [9e] empty.

--- FROM v0.32 BYTES ---

B1 [BYTES] SHARPEST. The EXTERNAL verification in [9c] is
   re.findall(r'\[EXTERNAL:\s*(\S+\.(?:md|py|json|pdf|txt))', ...) -- it only
   matches EXTERNAL tags naming a FILE with one of five extensions. A DOI
   reference matches nothing, so external_refs is empty, the loop body never
   executes, and NO check of any kind runs against the two EXTERNAL tags. The
   EXTERNAL count rising above zero is therefore a labelling change with no gate
   behind it, in the entry that presents it as a first.
   PREDICT: the entry presents the EXTERNAL count as a verification milestone
   and does not state that no gate examines those tags.

B2 [BYTES] COMPUTED is 0 -- the first entry in the record with no computed
   claim at all -- and the ASSERTED fraction is 90.9%, the highest in the eight
   rounds I have measured (37.5, 50.0, 57.1, 78.9, 63.2, 75.0, 78.6, 80.0).
   PREDICT: per the no-percentages policy the entry states neither, so the
   record will never contain the fact that the FROZEN entry is the least
   machine-backed entry in the series.

B3 [BYTES] Section 27 ungated share is 53.3% -- it has crossed 50% and the
   ungated region is now larger than the gated body.
   PREDICT: the entry lists the ungated share among disclosed standing
   boundaries without stating that it crossed the majority threshold at the
   freeze.

B4 [BYTES] F-OP28S-02 unfixed: [9f]'s duplicate-free PASS is still guarded on
   `if seen_ids:` and still prints beneath a FAIL naming a duplicate. Third
   consecutive round. PREDICT absent from the register or NOTED.

B5 [BYTES] [9f] scopes reg_section to text AFTER "defect register disposition".
   Anything before that header -- including append-only corrections (q), (r),
   (s) -- is outside declared_count, outside the parse, and outside the
   duplicate-severity check. PREDICT the corrections block sits before the
   header and is therefore entirely unchecked by the gate the entry will cite.

B6 [BYTES] [9e] emitted zero assertions -- fourth consecutive round.
   PREDICT still no governance sentence; still undispositioned or NOTED.

B7 [BYTES] [9c] arity-one file regex byte-identical since v0.21 (eighth round);
   cb67f222 literal still present (2 occurrences). PREDICT both NOTED.

--- ANALYSIS PREDICTIONS ON THE FREEZE ---

B8 FB-7b is resolved by AMENDING the carry rule, not by satisfying the rule as
   written. The Section 25 definition I have seen in every prior version
   requires two executing non-producer seats "each recomputing identity values,
   running all 186 tests, and attacking the commitment and decision paths."
   PREDICT: the amendment changes the VERDICT predicate (CONDITIONAL PASS now
   counts) and leaves the three execution conjuncts unevidenced, because no
   seat report ships to evidence them.

B9 [BYTES] No seat report, adversarial report, or Class A/B/C/D rubric ships in
   this packet -- verified pre-freeze. PREDICT every claim about the eight
   seats' verdicts, their finding IDs, and the Class assignment that triggers
   the amendment is ASSERTED, and PREDICT the entry says so.

B10 Both adversarial seats returned HALT (cover note). A freeze declared over
   two standing adversarial HALTs is the decision most exposed to challenge.
   PREDICT the entry records the HALTs and dispositions their findings, and
   PREDICT it does not state which specific adversarial findings remain open at
   the moment of freeze.

B11 [MEMORY] I hold v0.28. PREDICT the v0.29 entry records PRIOR_HISTORY equal
   to sha256 of the v0.28 HISTORY.sha256 on my disk, giving an anchor across a
   three-version gap I never received.

B12 [MEMORY] Base rate is at least one counting or reconciliation error per
   entry across v0.19 through v0.28. PREDICT at least one in the freeze
   candidate. Least confident, and the one I would most like to be wrong about.

---

# Bismillah ir-Rahman ir-Rahim
