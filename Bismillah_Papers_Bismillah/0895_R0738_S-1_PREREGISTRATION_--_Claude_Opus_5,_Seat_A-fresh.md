# Bismillah ir-Rahman ir-Rahim

# R0738 -- S-1 PREREGISTRATION -- Claude Opus 5, Seat A-fresh

**Chronological Index:** 895 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** PREREG_OPUS5_FRESH.txt  
**Source Format:** txt  
**SHA-256:** `b99995c380a536233b210d36001777e7289a483207464cb792d44a5484324804`  

---

## R0738 · S-1 PREREGISTRATION -- Claude Opus 5, Seat A-fresh

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: PREREG_OPUS5_FRESH.txt
- source_format: txt
- text_sha256: b99995c380a536233b210d36001777e7289a483207464cb792d44a5484324804

S-1 PREREGISTRATION -- Claude Opus 5, Seat A-fresh
Frozen before any read of xz_protocol_v0_20.md Section 27.
Basis: PACKET_SHA256SUMS, build.py source + stdout, protocol lines 1-25 only.

CONTAMINATION DECLARATION (mandatory before scoring):
build.py stdout, which the dispatch orders me to run at step 2, prints
Section 27-derived facts: entry count 20, the string "twenty", all 20 seal
labels, FULL_SECTION_27 seal PASS, PRIOR_HISTORY 41428758..., and the
provenance tally COMPUTED 11 / EXTERNAL 0 / ASSERTED 11 = 50.0%.
Any prediction touching those values is NOT a blind prediction. Predictions
below are marked [BLIND] or [CONTAMINATED] accordingly. Only [BLIND] items
carry evidential weight.

P1 [BLIND] The v0.20 entry claims the PRIOR_HISTORY control is closed
   (F-ADJ19-01) without stating that build.py [9b] compares the shipped
   HISTORY.sha256 value against a literal hardcoded in build.py, so the
   check cannot detect a coordinated edit of both shipped files.
   PREDICT: TRUE (claim present, limitation not stated in the entry).

P2 [BLIND] The v0.20 entry describes the prose-citation verifier [3c] as a
   control over cited digests without stating its guard
   `if os.path.exists(cited_file)`, which silently skips every citation to a
   file not shipped in the packet.
   PREDICT: TRUE (limitation not stated in the entry).

P3 [BLIND] xz_protocol_v0_20.pdf is absent from NORMATIVE_FILES and from
   PACKET_SHA256SUMS, so no gate binds the PDF to the .md.
   PREDICT: the entry does not name the PDF as an unsealed surface.

P4 [BLIND] EXTERNAL count is 0 while the entry narrates findings attributed
   to other seats/audits.
   PREDICT: at least one claim about what another seat found appears in the
   v0.20 entry carrying ASSERTED or no tag, never EXTERNAL.

P5 [BLIND] `sha256sum -c PACKET_SHA256SUMS` -- the dispatch step-1 gate --
   returns rc=1 by construction, because the self-entry holds the digest of
   the 16-line body, not of the file.
   PREDICT: the v0.20 entry claims PACKET_SHA256SUMS verification is closed
   and does not record that the canonical verify command fails.

P6 [BLIND] build.py [9d] matches only `<ordinal> [^.]* recurrence`.
   PREDICT: the gate is one-directional and the entry does not say so;
   a numeral form or a post-positioned ordinal would pass unflagged.

P7 [BLIND] build.py [8] prints `pytest: {last line of stdout}` and, when
   pytest is absent, prints an empty string while reporting
   "FAIL: All tests GREEN (rc=1)".
   PREDICT: environment-absence and test-failure are indistinguishable in
   build output; the entry does not distinguish them.

P8 [BLIND] Semantic-gate coverage of the body is well under 50% (measured
   24.4%). PREDICT: the entry reports a coverage number and frames it as a
   disclosed limitation rather than a resolved one.

P9 [CONTAMINATED] ASSERTED fraction stated in the entry equals 50.0%
   (11/22). PREDICT: TRUE.

P10 [BLIND] At least one CLOSED/resolved claim in the v0.20 entry references
   a prior audit report (v0.17/v0.18/v0.19 seat reports) that is NOT a file
   in this packet, making it unverifiable from shipped bytes.
   PREDICT: TRUE, at least one such claim.

P11 [BLIND] The 20 amendment entries are internally coherent: no entry
   contradicts an earlier entry's recorded outcome.
   PREDICT: FALSE is the risk case; I predict TRUE (no contradiction) but
   flag this as the prediction I am least confident in.

P12 [BLIND] HISTORY.sha256 seals every entry INCLUDING v0.20 itself, so the
   seal file cannot be produced until after the entry text is final.
   PREDICT: no self-reference paradox, but the v0.20 seal provides zero
   tamper-evidence for v0.20 because both files ship together and neither is
   externally anchored. PREDICT: the entry does not state this.

---

# Bismillah ir-Rahman ir-Rahim
