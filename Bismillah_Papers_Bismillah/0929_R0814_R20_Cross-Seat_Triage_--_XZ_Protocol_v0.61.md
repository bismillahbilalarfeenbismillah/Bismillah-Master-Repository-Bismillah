# Bismillah ir-Rahman ir-Rahim

# R0814 -- R20 Cross-Seat Triage -- XZ Protocol v0.61

**Chronological Index:** 929 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** R20_TRIAGE.txt  
**Source Format:** txt  
**SHA-256:** `03815458ca76ffcb729d1b97c11f822cd6ab6ad71582d439804ddb930619c5e5`  

---

## R0814 · R20 Cross-Seat Triage -- XZ Protocol v0.61

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: R20_TRIAGE.txt
- source_format: txt
- text_sha256: 03815458ca76ffcb729d1b97c11f822cd6ab6ad71582d439804ddb930619c5e5

# R20 Cross-Seat Triage -- XZ Protocol v0.61
# Round: 20 (10 seats: 5 fresh + 5 continuous)
# All 10 seats: HALT (4 carrying binding HALT, 6 advisory HALT)
# Class A recurrence: R7-R20 (14/14), H = 1.0
# Laplace P(Class A at R21) = 15/16 = 0.9375

## What CI v0.3.1 got right (verified across 10 seats)

- CI-1R: byte-exact register reproduction at all executing seats
- Baseline green: build.py PASS, 186/186 pytest, 19/19 PACKET_SHA256SUMS
- S02C exhaustive 75/75 M2 single-severity mutation battery: all fail generation (M2 DONE)
- VERSION-1 gate sabotage-proven at all executing seats
- Dangling convergence_group rejection confirmed
- Source distribution load-bearing and emitted into register
- PRIOR_HISTORY cross-anchored to held v0.60 HISTORY
- R19 Defects 2 (correction (ch) landing), 3 (VERSION-1 gate), 4 (dangling refs) DISCHARGED

## Convergent defect groups

### Surface 1: M3 receipt enforcement majority-only + substring validation
Convergence: 8/10 seats (S02F, S02C, S03F, S03C, S05F, S05C + 2 others).
- F-S02-61-01F, F-S02-61-02F, F-S02-61-02C (HIGH): receipt required only on majority
  divergence; mixed-majority groups accept receipt removal. Receipt validation is
  substring-based, not structural (exact canonical distribution string not required).
- F-S03-61-02F, F-S03-61-01C (HIGH): same substance
- F-S05-61-01F, F-S05-61-01C (HIGH): same, with stale receipt accepted after flip

Triage severity: HIGH. The generator's receipt gate fires only when triage_severity !=
source majority AND no receipt exists. If a receipt of any content exists, or if triage
equals majority, the receipt is not validated against the actual distribution. A
valid-token source-severity mutation can flip the majority while the old receipt passes
because it is checked by substring, not by exact canonical string.
Disposition: CLOSED via CI v0.3.2 -- receipt required on ANY mixed distribution (not
majority-only); receipt validation structural (exact canonical distribution string
verbatim, not substring matching).

### Surface 2: _unique_seat_count parser (seat count from ID parsing)
Convergence: 3/10 seats (S02C, S03C + 1 other).
- F-S02-61-01C (HIGH): seat count computed by parsing finding_id prefix, not from
  authoritative findings[].seat field
- F-S03-61-02C (HIGH): same substance

Triage severity: HIGH. The generator extracts seat identity from the finding_id string
(F-SNN-VV-FF -> SNN) instead of from findings_by_id[fid]["seat"]. A finding with a
non-standard ID format produces a wrong seat count silently.
Disposition: CLOSED via CI v0.3.2 -- seat count from findings[].seat (authoritative
field, not ID parsing).

### Surface 3: Noted-finding dangling bypass
Convergence: 1/10 seats (S03F).
- F-S03-61-01F (HIGH): ungrouped findings with non-null convergence_group bypass
  validation because noted findings skip the group-existence check

Triage severity: HIGH. A noted finding with convergence_group pointing to a non-existent
group passes validation. The bypass was intended for ungrouped findings (null group) but
applied to all noted findings regardless of group value.
Disposition: CLOSED via CI v0.3.2 -- bypass removed; ungrouped findings must have
convergence_group=null; any non-null reference to non-existent group rejected.

### Surface 4: Bidirectional membership parity
Convergence: 2/10 seats (S05F, S05C).
- F-S05-61-03F (HIGH): finding's scalar convergence_group can disagree with the group
  whose finding_ids list contains it
- F-S05-61-03C (MEDIUM): same substance

Triage severity: HIGH (elevated from 1H+1M per convergence). Each finding's
convergence_group must equal the group whose finding_ids contains it. Without
bidirectional enforcement, a finding can claim membership in group X while group Y's
finding_ids includes it.
Disposition: CLOSED via CI v0.3.2 -- bidirectional parity enforced.

### NOTED (carried forward)

- [5-seat: F-S02-61-03F, F-S02-61-03C, F-S03-61-03F, F-S05-61-02F, F-S05-61-02C] HIGH:
  CI-8 source-ID fidelity (16/25 index finding IDs carry F/C suffixes absent from
  source reports). Disposition: NOTED. The source_finding_id field added in CI v0.3.2
  for literal resolution.

---

# Bismillah ir-Rahman ir-Rahim
