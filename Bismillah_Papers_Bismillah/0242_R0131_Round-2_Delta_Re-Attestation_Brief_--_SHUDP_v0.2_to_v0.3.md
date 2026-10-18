# Bismillah ir-Rahman ir-Rahim

# R0131 -- Round-2 Delta Re-Attestation Brief -- SHUDP v0.2 to v0.3

**Chronological Index:** 242 of 995  
**Date:** 2026-05-19  
**Section:** III. Structural Honesty — Core Papers  
**Source File:** SHUDP_dispatch_brief_R2_SUPERSEDED.md  
**Source Format:** md  
**SHA-256:** `75dfacd796fb9f7c2dcbb4d4476dd2ae75d4641884949eb0a987fb955712ecea`  

---

## R0131 · Round-2 Delta Re-Attestation Brief -- SHUDP v0.2 to v0.3

- section: III. Structural Honesty — Core Papers
- source_file: SHUDP_dispatch_brief_R2_SUPERSEDED.md
- source_format: md
- text_sha256: 75dfacd796fb9f7c2dcbb4d4476dd2ae75d4641884949eb0a987fb955712ecea

# Round-2 Delta Re-Attestation Brief -- SHUDP v0.2 to v0.3
## Addressed to: Perplexity Computer, MODEL-COUNCIL MODE

Supersedes the Round-1 dispatch brief for all receipt declarations and scope. Round 1 is closed:
it converged READY-WITH-CONDITIONS on v0.2 with GPT 5.5 (OpenAI) and Gemini 3.1 Pro (Google)
carrying. This round is delta-scoped, not a fresh substantive audit.

## 0. Intake correction, stated first

The previous dispatch failed intake on **F-SP-001 CRITICAL**: the Round-1 brief was shipped inside
the v0.3 packet unchanged, so its Section 6 declared v0.2 receipts against v0.3 contents. The
finding is CONFIRMED, producer-owned, and adjudicated in the audit ledger's F-SP-001 section along
with its root cause. The intake gate performed correctly and the block was correct.

`SHUDP_dispatch_brief_R1_SUPERSEDED.md` remains in this packet **byte-identical** to the file the
Round-1 seats hashed (`33d42bf3ed19e5bcf5ec0960e57737fece9b1b0980110f427cc43e2173ee1eb7`), so its
receipts stay verifiable against the Round-1 reports. **Its Section 6 receipts refer to the v0.2
packet and are superseded by Section 6 of this brief.** No other packet file declares receipts.

## 1. Council structure and seat rules (carried unchanged from Round 1)

- Each seat DECLARES model, vendor, and tier at the head of its report. Undeclared seats carry no
  verdict.
- Per-seat namespaces, mandatory: F-D<V>-NN, where <V> is the vendor initial (G Google, O OpenAI,
  K Moonshot, X xAI, P other or native).
- Lineage exclusions: Anthropic-lineage seats are ADVISORY ONLY. The producer instance is Anthropic
  lineage.
- Family accounting: same-vendor seats count once.
- Producer self-repairs and producer-run gates earn NO absence-credit. Verify them; do not credit
  their presence.
- CONVERGENCE = PASS-DELTA from at least TWO carrying seats of DIFFERENT vendor families.
- Refuted findings do not flip a verdict; a seat whose findings are refuted re-attests on the
  corrected instrument.

## 2. Scope: the delta, and only the delta

v0.3 answers a converged Round-1 verdict plus an external peer review (Grok, filed as peer review,
not as a carrying seat). The repair register R-1 through R-20 is stated in full in the audit
ledger's v0.3 section. Verify the delta against that register.

**L1 Diff.** Diff `SHUDP_v2_baseline_source.md`
(`c8b64c2bf5f57fd56d084338e541395fd6c3ce855016a147b6c14c6cccb726ed`) against
`SHUDP_v3_source.md` (`d2d028dd051aab668f1406a6004960600895c75e280b2bfcdeae963736af51c7`). Every
hunk must map to a register item. Any hunk outside R-1 through R-20 is a finding.

**L2 Per-finding discharge.** For each Round-1 finding, verify the repair discharges it:
F-SO-01 all-black to R-20 and G6; F-SO-04 title and numbering to R-18 and R-19; F-SO-02 and
F-SG-NN-05 and the Fable telemetry item to R-17's three dependency classes; F-SO-03 to R-12;
Fable H1 to R-14; F-SG-NN-04 to R-9. For Grok's annotations: p1 to R-1 and R-19, p2 to R-2 and R-3,
p3 and p8 to R-4, p7 to R-6, p10 to R-7, p11 to R-8, p13 to R-10, p14 to R-11, p17 to R-13,
p20 to R-16, p24 to R-15.

**L3 Refutation audit.** Two Round-1 claims were REFUTED rather than repaired. Test both against the
primary yourselves; a refutation that does not hold is a finding.
1. The claim that the paper misrepresents METR on monitoring. The producer's position is that METR's
   Figure 8 caption states verbatim that none of the incidents involved agents taking effective steps
   to disable monitors or erase evidence *in their transcripts or other logs*, so routine monitoring
   measures could have caught all incidents if applied, and that the paper's rendering is therefore
   the primary's own claim with its conditional intact. The producer nonetheless CONFIRMED a
   narrower defect in the same sentence, that its scoping clause had been dropped, and repaired it
   at R-5. Verify both halves.
2. The claim that the METR citation date is wrong. The producer's position is that May 19, 2026 is
   the report's masthead publication date; the assessment window was added anyway at R-15.

**L4 New gates.** Execute both new gates yourselves.
- **G7 SHEC-PARSE.** Extract the YAML block from Appendix A and parse it with a real parser. It must
  parse, and every member of `conservative_outcome_set` must carry a `discharge` key. In v0.2 it did
  not parse; this is the round's most consequential repair.
- **G8 NO-TRUNCATION.** Confirm no code-block content is lost off the right margin in the PDF. The
  v0.2 render truncated a comment mid-word.
- **G6 ALL-BLACK, now exhaustive.** Inspect PDF color operators directly and scan every page, not a
  sample. The v0.2 producer gate sampled five pages and missed colored content on pages 20 and 21.

**L5 Carried checks.** Section identity across all three renders; meta-text absence;
status currency; standing-rule lint (no em-dash characters, brand canonical, severity tokens
uppercase).

## 3. Probe discipline (defects here are findings against the seat)

- Wrap-immune normalization on all text probes: de-hyphenate line breaks, collapse whitespace, then
  match.
- Gate token lists are QUOTED LITERALS ONLY.
- Scope probes to this artifact. It contains code blocks and a table with a numeric column header.
  Probes over table cells must test constituent tokens rather than contiguous phrases, because the
  renderer interleaves column text. The producer made all three of these probe errors and recorded
  them in the ledger.

## 4. Findings and verdict

Six-element findings: ID, severity, locus pinned exactly, substance, disposition, cross-reference.
Severities UPPERCASE. Verified controls take LOW or CONTROL, never CRITICAL or HIGH.

Per-seat verdict: PASS-DELTA or NON-PASS. Synthesis reports per-seat verdicts and the convergence
determination under Section 1, and must not launder refuted findings into the synthesis.

## 5. Instrument receipts, v0.3

```
d2d028dd051aab668f1406a6004960600895c75e280b2bfcdeae963736af51c7  SHUDP_v3_source.md
c072b3b66c2c98b096c35d0663cbfe629cf149b633df7dc1eb17e29c0a7861e5  SHUDP_v3.pdf
269e4a484a474e46b308a1b22b416419b53e01c0e95ea1bf782d2be9d05dabe4  SHUDP_v3.docx
51c3559a445d67ec3c05ca33a3831037ba913874c5431663da61700ce4fb1ee9  SHUDP_v3.html
c8b64c2bf5f57fd56d084338e541395fd6c3ce855016a147b6c14c6cccb726ed  SHUDP_v2_baseline_source.md
33d42bf3ed19e5bcf5ec0960e57737fece9b1b0980110f427cc43e2173ee1eb7  SHUDP_dispatch_brief_R1_SUPERSEDED.md
```

**`SHA256SUMS.txt` is authoritative for every other packet file**, including the audit ledger and
punch list, whose contents change as this round is recorded. This brief deliberately does not
declare their hashes, because a brief that declared the hash of a ledger it is itself about to be
recorded in could never be self-consistent. Verify the manifest against the packet on arrival; a
mismatch is a CRITICAL intake finding and the round does not proceed.

---

# Bismillah ir-Rahman ir-Rahim
