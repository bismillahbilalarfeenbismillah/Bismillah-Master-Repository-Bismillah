# Bismillah ir-Rahman ir-Rahim

# R0225 -- XZ Protocol v0.20 -- Build Specification and Producer Handoff

**Chronological Index:** 456 of 995  
**Date:** 2026-08-02  
**Section:** IV. XZ Protocol  
**Source File:** XZ_v20_BUILD_SPECIFICATION.md  
**Source Format:** md  
**SHA-256:** `308b37867e0f6448c63560206f0c6d9b9df6c27c0cb19ed8ac188eab51760416`  

---

## R0225 · XZ Protocol v0.20 -- Build Specification and Producer Handoff

- section: IV. XZ Protocol
- source_file: XZ_v20_BUILD_SPECIFICATION.md
- source_format: md
- text_sha256: 308b37867e0f6448c63560206f0c6d9b9df6c27c0cb19ed8ac188eab51760416

# XZ Protocol v0.20 -- Build Specification and Producer Handoff

**For:** A fresh Claude Opus 4.6 instance.
**From:** The outgoing Opus 4.6 producer (context exhausted after v0.15-v0.19).
**Adjudicator:** Claude Opus 5, Seat A, producer-family advisory.
**Date:** 2026-08-02.

## What this document is

This is a clean-room build specification for v0.20 of the XZ Protocol, a
preregistration instrument for a retrospective structural decision replay of
CVE-2024-3094 (the XZ Utils backdoor). You are taking over production from a
prior Opus 4.6 instance whose context window is exhausted.

The prior instance produced v0.15 through v0.19 across one session. That
session's Axiom-3 defect trajectory: stale digests coexisting with correct
ones (v0.15), global replacement leaking into historical entries (v0.16),
narrative overclaims about verifiability (v0.17), claims about other
documents that were false of the shipped reports (v0.18), and self-
contradictory ordinal claims plus decorative controls (v0.19). The pattern
moved from wrong values to wrong narratives to wrong claims about the
verification apparatus itself.

Read every file in this package before writing any code or text.

## Reading order

1. **This file** -- what exists, what's broken, what v0.20 needs.
2. **HANDOFF_ADDENDUM_v20.md** -- Opus 5's review of this handoff. Adds three
   absent reports, a handoff manifest, two reconciliations, and an open
   prediction for v0.20 scoring. Read alongside this document.
3. **XZ_v19_ADJUDICATION.md** -- Opus 5's tri-seat adjudication with the
   producer brief (Blocks A-E). Section 8 is a PROPOSAL from a producer-
   family seat, not an instruction. The one substrate contradiction is
   escalated to the project lead unresolved and must not be treated as settled.
4. **PRODUCER_SELF_DISCIPLINE_v2_DELTA.md** -- O-1 through O-13. Load this
   as standing orders for your session.
5. **AUDIT_DISPATCH_DISCIPLINE_v2.md** -- the auditor-side discipline. You
   need to understand it to produce dispatches, but per D-0 you must NOT
   merge it with the producer document.
6. **SEAT_STANDING_ORDERS_v1.md** -- the seat self-command block. Ships in
   every dispatch.
7. The four v0.19 audit reports (GPT, GLM, Kimi, Opus 5) -- raw findings.
8. The v0.17 reports (Seat A and Seat B, by digest) and v0.18 Rev A --
   needed for D1 disposition and F-ADJ19-02 second path.
9. The v0.19 normative files -- the bytes you're fixing.

## Verification

Before reading anything else, verify the handoff:
```
sha256sum -c HANDOFF_SHA256SUMS.txt
```
A mismatch is a stop condition, not a curiosity.

## What exists (the v0.19 normative instrument)

14 normative files: 7 code modules, 5 test suites, 1 trust-roots JSON,
1 protocol text (.md). Plus tooling: build.py, HISTORY.sha256.

The code plane is CLEAN: 186 tests pass, all 14 digests verify, the manifest
chain pins every code file under mutation. Three consecutive rounds have
confirmed this. The code is not the problem.

The problem is the protocol text's amendment record (Section 27), which is
29.6% of the document, outside every semantic gate, and where every Axiom-3
recurrence has lived. The v0.19 entry makes four false claims about its own
verification apparatus (the four consensus HIGHs).

## The four consensus HIGHs (your primary task)

From the adjudication (Section 3), each with the falsification test from
the producer brief (Section 8) written BEFORE the fix:

### F-ADJ19-01 HIGH: PRIOR_HISTORY is decorative; F-OP18-05 falsely CLOSED

build.py line 254-257 collects PRIOR_HISTORY lines and prints them. It
contains no check() call and compares no value. The entry tags this
[COMPUTED: build.py [9b] PRIOR_HISTORY check, once implemented] -- a CLOSED
whose own tag says "once implemented."

**Fix:** Retag as DISCLOSED, NOT CLOSED. Then implement the real check():
require exactly one PRIOR_HISTORY line, compare its value against the
shipped prior HISTORY.sha256 (or a known digest), fail on mismatch or
absence. Ship the prior HISTORY.sha256 or embed its digest.

**Falsification test (write first):** Replace the PRIOR_HISTORY digest with
64 zeros, reseal, assert build fails. Currently passes.

### F-ADJ19-02 HIGH: Provenance ledger unimplemented; EXTERNAL tag invalid

build.py [11] prints character counts. It does not parse, count, or validate
COMPUTED/EXTERNAL/ASSERTED tags. The single EXTERNAL tag in the entry fails
for three independent reasons found by three seats:
- The cited report carries no digest in any shipped text (GPT)
- It is producer-family, not "state the producer does not control" (GLM)
- The cited severity figures are wrong (Opus 5)

**Fix:** Retag the EXTERNAL claim as ASSERTED. Then make tags machine-checked:
parse every [COMPUTED: ...], extract the build section, assert it exists in
build.py, fail otherwise. Assert every EXTERNAL tag names a shipping file
with a matching digest. Print the ASSERTED fraction.

**Falsification test (write first):** Rewrite one tag to name build.py [99],
a section that does not exist, reseal, assert build fails. Currently passes.

### F-ADJ19-03 HIGH: Entry asserts the ordinal it twice disclaims

Line 865: "The twelfth Axiom-3 recurrence..." Items (3) and (6): "this
entry does not assert one" / "This entry does not assert an ordinal."
Self-contradiction.

**Fix:** Strike the ordinal from the opening sentence. Do not replace it.

**Falsification test (write first):** grep the entry for ordinal words
adjacent to "recurrence"; assert zero hits while no recurrence table ships.

### F-ADJ19-04 HIGH: F-OP18-09 dropped for the second consecutive round

"F-OP18-01 through F-OP18-10" is stated in the entry, but F-OP18-09 (the
em-dash convention finding) appears zero times anywhere in the packet. Same
finding was dropped as F-OP17-09 at v0.18.

**Fix:** Disposition F-OP18-09 explicitly. State it was dropped twice. Resolve.

**Falsification test (write first):** Extract every finding ID from each
report named in the entry; assert each occurs in the entry; fail on absence.

## Additional required items (from the producer brief)

### Block A -- Substrate correction (DO FIRST, blocks everything else)

**A1.** Emit ONE canonical packet. Hash every member into PACKET_SHA256SUMS.
Verify it in build.py. Ship the IDENTICAL member set to every seat. Vary
the cover note, never the payload.

**A2.** The v0.19 carry is NOT ATTEMPTED (three seats got three different
packets). Record it as such, not as divergent.

### Block C -- the one-line control with the highest ratio

**C1 (F-ADJ19-05).** Fail the build when HISTORY.sha256 is absent. Replace
the bare `if os.path.exists(...)` with a `check()` on presence. Currently
returns rc=0 with zero fail-checks when the file is missing, which is how
Kimi's packet produced a false-clean history layer.

### Block D -- absorb without blocking

**D1 (F-ADJ19-08).** Restate item (1) by digest; drop route names.
**D2 (F-ADJ19-07).** Rename coverage output; add semantic-gate line.
**D3 (F-ADJ19-09).** Fix "the shipped prohibited-content verifier".
**D4 (F-ADJ19-10).** Assign IDs to the five discipline-block defects.
**D5 (F-ADJ19-06).** Write the self-consistent-forgery limit into Section 22.

### Block E -- do not do

Do not add a gate to close the ungated fraction by shrinking the entry.

## Critical rules (carried from the prior handoff)

* Do NOT edit historical amendment entries. Corrections go in v0.20 only.
* Do NOT claim FROZEN. v0.20 is a DRAFT CANDIDATE.
* Do NOT trust any digest, count, or version string from this document.
  Recompute everything from bytes.
* Every number in the protocol text must come from a tool computation.
* The normative/tooling partition: gates are tooling (not carried); the
  protocol text and decision code are normative (carried).
* Carrying seats: Kimi K3 (Moonshot) + GLM-5.2 (Zhipu/Z.ai).
* GPT-5.6 Sol: adversarial record only, no carry vote.
* Producer family: Claude (Anthropic). Your review is advisory, not carrying.
* Author: Bilal Syed Arfeen. No organizational affiliation. No
  "BayyinahEnterprise" anywhere.
* Em-dashes as `--` (double hyphen) in all non-LaTeX output.
* Severities in UPPERCASE.

## The program chain

```
AX-SH5 -> SHUDP -> SHVVP -> BSSG -> XZ Protocol (v0.20 pending) -> XZ Corpus -> XZ Empirical
```

## Key DOIs

* SHV Flagship: 10.5281/zenodo.21500700
* Dissertation v1.4: 10.5281/zenodo.21501912
* SHVVP v0.8: 10.5281/zenodo.21583202
* SHUDP v0.5: 10.5281/zenodo.21539816
* BSSG (concept): 10.5281/zenodo.21712481
* BSSG (version-of-record): 10.5281/zenodo.21713180
* BAF v3.0: 10.5281/zenodo.20046910
* PMD v1.8: 10.5281/zenodo.21462879
* SHV Method v1.1: 10.5281/zenodo.21450932

## Dispatch architecture for v0.20

Per A1 and D-0, reconciled per HANDOFF_ADDENDUM_v20.md Section 3.1:

Split the dispatch into two parts:
1. **Canonical normative packet** -- the 14 normative files plus build.py,
   HISTORY.sha256, and PACKET_SHA256SUMS. Byte-identical to every seat.
   The carry is over this and only this, so FB-7b keeps its meaning.
2. **Per-seat context bundle** -- standing orders, discipline blocks, prior
   reports, adjudication, cover note. Varies by role per D-0.

Carrying seats (GLM, Kimi): no expected values, no defect-class list, no
  prior advisory reports in their context bundle.
Adversarial seat (GPT): gets the class list and prior reports.
Advisory seat (Opus 5): gets everything.

## What you should produce

1. Fix every item in Blocks A through D of the producer brief.
2. Write the v0.20 amendment entry LAST (O-1), deriving every claim from
   tool output, tagging every claim COMPUTED/EXTERNAL/ASSERTED.
3. Run build.py. It must pass with the new checks (PRIOR_HISTORY, tag
   validation, PACKET_SHA256SUMS, HISTORY.sha256 presence).
4. Generate the PDF (pandoc + pdflatex, Computer Modern, black text).
5. Package ONE canonical dispatch zip. Ship to all four seats with
   per-seat cover notes.

## The refutation register (from Opus 5's self-correction)

The outgoing adjudicator's own claims that were refuted by non-producer
seats and must not be re-asserted:

1. "The entry asserts no recurrence ordinal" -- REFUTED; it does.
2. "Finding-accounting is complete for the first time" -- REFUTED; F-OP18-09
   is absent.
3. Packet-coverage figure of 14 hashed / 19 unhashed -- wrong; GPT's 16/17
   is correct.

An auditor's commendations are less checked than its findings.

## Session hygiene (O-13)

You are a fresh instance. You have no memory of what the prior instance did.
That is an advantage: you will check the bytes rather than trusting a
self-model. Do not let this session run long enough to accumulate a
self-model that substitutes for checking. If you feel yourself writing
claims from memory rather than from tool output, stop and re-derive.

---

# Bismillah ir-Rahman ir-Rahim
