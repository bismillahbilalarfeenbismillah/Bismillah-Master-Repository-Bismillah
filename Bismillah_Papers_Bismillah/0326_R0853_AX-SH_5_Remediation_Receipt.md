# Bismillah ir-Rahman ir-Rahim

# R0853 -- AX-SH 5 Remediation Receipt

**Chronological Index:** 326 of 995  
**Date:** 2026-07-23  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** remediation-receipt.md  
**Source Format:** md  
**SHA-256:** `6ffbb81b9f2eb3cc918860a21e67d28a92149d083198c7efeb9b63ad2c4e0b34`  

---

## R0853 · AX-SH 5 Remediation Receipt

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: remediation-receipt.md
- source_format: md
- text_sha256: 6ffbb81b9f2eb3cc918860a21e67d28a92149d083198c7efeb9b63ad2c4e0b34

# AX-SH 5 Remediation Receipt

**Artifact:** *Is Evidence Independence an Axiom? Decomposing a Proposed Extension to AX-SH* (Bilal Syed Arfeen, July 23, 2026)

**Remediation trigger:** Claude Fable 5 HALT-AND-ESCALATE audit, July 23, 2026 (1 CRITICAL / 5 MEDIUM / 3 LOW), preserved in this packet as `claude-fable-5-audit-2026-07-23.md`.

**Remediation pass completed:** July 24, 2026.

## 1. Root-cause fix: single authoritative source

Edition divergence (F-EI-1, CRITICAL) is eliminated at the root. Both text members are now mechanically generated from ONE authoritative source:

- Authoritative source: `axsh5_content.py` (a typed block list; policy-compliant punctuation only).
- Markdown emitter: `emit_markdown.py` -> `is-evidence-independence-an-axiom-canonical.pplx.md`.
- PDF emitter: `emit_pdf.py` -> `is-evidence-independence-an-axiom-canonical.pdf`.

Because both members derive from the same source, divergence cannot recur by construction. Independent confirmation is provided by the G9 concordance receipt.

## 2. G9 concordance receipt (F-EI-1)

`concordance_receipt.txt` records the bidirectional, wrap-immune, quote/dash-normalized concordance between the Markdown and PDF:

- BLOCK-LEVEL bidirectional parity: 116 / 116 content blocks present in BOTH members (0 missing).
- GLOBAL token-multiset parity: similarity 1.0000 (0 differing prose tokens).
- Load-bearing riders present in BOTH: 16 / 16, including E-star in the boxed axiom; F-2 and F-7 discharged-but-live riders; the exact-security-notion hedge; the temporal rule forbidding reconstruction from subject-emitted logs; the axiom-level UNSATISFIED vs event-level UNKNOWN distinction; the WithinAuth-primitive sentence; ETSI TS 119 511; ML-DSA-primary / SLH-DSA-not-categorically-preferable; the no-machine-checked-verification claim; and the proposal-on-file citation.
- Forbidden strings absent in BOTH: 3 / 3 (the ambiguous compound-label shorthand that joined the two status words with a slash; the old ETSI EN 319 102-1 preservation misuse; the removed Wikipedia LSP entry).
- **Result: BIDIRECTIONAL PARITY: PASS.**

## 3. Finding-by-finding disposition (F-EI-1 ... F-EI-9)

| Finding | Severity | Status |
| --- | --- | --- |
| F-EI-1 edition divergence | CRITICAL | CLOSED (single source; receipt PASS) |
| F-EI-2 ETSI EN 319 102-1 preservation misuse | MEDIUM | CLOSED (replaced by ETSI TS 119 511 V1.2.1, source [14]) |
| F-EI-3 proposal uncited; dangling companion pointer | MEDIUM | CLOSED (source [16]; proposal artifact + adjudication + reviews + stress test + Fable audit shipped in this packet) |
| F-EI-4 PDF metadata attributes authorship to tool | MEDIUM | CLOSED with recorded metadata-layer limitation (see Section 4) |
| F-EI-5 WithinAuth detectability regress | MEDIUM | CLOSED (Section 6.1 primitive-relation sentence added) |
| F-EI-6 ambiguous compound-label shorthand | MEDIUM | CLOSED (two-level distinction in abstract and Section 7; axiom-level UNSATISFIED (nonconforming) vs event-level UNKNOWN under Proposition 1; compound label removed from canonical pair and adjudication) |
| F-EI-7 source-layer dash violations | LOW | CLOSED (zero U+2014 and U+2013 verified across all text members) |
| F-EI-8 duplicate SP 800-57; Wikipedia over-reliance | LOW | CLOSED (SP 800-57 deduped to source [8]; Wikipedia LSP removed; Liskov-Wing 1994 with DOI is source [4]) |
| F-EI-9 quantum collision-level imprecision | LOW | CLOSED (preimage ~2^128 vs collision ~2^85 BHT distinguished; NIST-sourced) |

## 4. Metadata-layer limitation (transparent disclosure, F-EI-4)

The PDF `/Author` field is set to "Perplexity Computer" as required by the loaded PDF skill's mandatory Author-field rule. To reduce attribution ambiguity, `/Subject` and `/Creator` explicitly state: "Authored by Bilal Syed Arfeen; prepared with Perplexity Computer as an analytical and drafting instrument." The visible byline on page 1 and in the author note names Bilal Syed Arfeen as the author.

**Limitation, stated rather than papered over:** a reader who inspects only the raw `/Author` PDF field will still see the drafting tool, not the human author. This is a known constraint of following the skill's Author-field rule; it is recorded here rather than claimed as full closure. Full closure would require either overriding the skill rule (not done) or a metadata standard that separates "author" from "producer/preparer" in a field every reader inspects.

Verified metadata (via `pdfinfo`):

- Title: Is Evidence Independence an Axiom? Decomposing a Proposed Extension to AX-SH
- Author: Perplexity Computer
- Subject: Authored by Bilal Syed Arfeen; prepared with Perplexity Computer as an analytical and drafting instrument. ...
- Creator: Authored by Bilal Syed Arfeen; prepared with Perplexity Computer as an analytical and drafting instrument.
- Keywords: Bilal Syed Arfeen; structural honesty; AX-SH; evidence independence; ...
- CreationDate / ModDate: set (July 23-24, 2026).

## 5. Mechanical QA results (F-EI-12)

- `qpdf --check`: no syntax or stream encoding errors.
- `pdffonts`: all fonts embedded and subsetted; no non-embedded Helvetica remains.
- `pdfinfo`: 12 pages; all metadata fields populated.
- Forbidden dashes across all packet text members: zero U+2014, zero U+2013.
- Empty-superscript defect occurrences in canonical Markdown and PDF: zero.
- TODO / PLACEHOLDER / FIXME: zero.
- Citation numbering: 16 sources, unique and sequential (1..16), no duplicate reference entries or duplicate URLs.
- Visual QA: pages inspected; equations, boxed axiom, tables, and superscripts render without overflow or squashing; page numbers present.
- Bidirectional parity: PASS.

## 6. Fable seat status

Under the program's same-vendor-counts-once rule, the Claude Fable 5 audit is advisory and non-carrying for this artifact (prior Claude lineage; Claude Opus 4.8 council seat; Claude named as drafting instrument). It is preserved as an independent adversarial audit record, and its CRITICAL finding drove this pass. Carrying re-attestation seats for the receipt-level delta are GPT-5.4 and Gemini 3.1 Pro.

## 7. Final delta re-attestation (carrying seats)

Two cross-vendor seats independently re-attested the remediated packet at the receipt level; both reached PASS and both carry. Their reports are in this packet.

| Seat | Vendor | Verdict | Carry status | Report file |
| --- | --- | --- | --- | --- |
| GPT-5.4 delta re-attestation | OpenAI | PASS | Carries | `council-review-openai-gpt-5.4-delta-reattestation.pplx.md` |
| Gemini 3.1 Pro delta re-attestation | Google | PASS | Carries | `council-review-google-gemini-3.1-pro-delta-reattestation.pplx.md` |
| Claude Fable 5 audit | Anthropic | HALT-AND-ESCALATE (remediation driver) | Advisory, non-carrying | `claude-fable-5-audit-2026-07-23.md` |

GPT-5.4 independently re-ran integrity and PDF checks, block/token comparison against the authoritative source, and hyperlink enumeration, and closed F-EI-1 through F-EI-9 for deposit with the single disclosed `/Author` caveat. It raised one non-blocking observation, that this adjudication and receipt still carried the ambiguous compound-label shorthand in explanatory prose; that observation is resolved in this final revision (the shorthand is replaced by the explicit two-level distinction throughout the adjudication and this receipt). Gemini 3.1 Pro executed the concordance check locally (116/116 blocks, token similarity 1.0000, 16/16 riders) and confirmed every substantive disposition with no mathematical regression.

## 8. Substantive verdict

The mathematics was not changed by this pass; the Fable audit itself confirmed M-minus, M-plus, and Propositions 1 and 2 are sound as paper proofs. This remediation corrected the instrument pair (edition integrity, citations, metadata, punctuation) and sharpened four claims (F-EI-5, F-EI-6, F-EI-9, and the ETSI swap). With the concordance receipt passing, F-EI-1 through F-EI-9 closed, and two carrying cross-vendor PASS seats (GPT-5.4 and Gemini 3.1 Pro), the regenerated pair is **DEPOSIT-CLEARED** as a decomposition paper.

**Completion status: COMPLETE.** This is the final revision pass; the release packet is closed for deposit.

---

# Bismillah ir-Rahman ir-Rahim
