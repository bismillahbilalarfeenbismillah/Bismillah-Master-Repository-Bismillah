# Bismillah ir-Rahman ir-Rahim

# R0081 -- AXSH5 Round-3 Absorption Receipt (Authoritative Return Receipt)

**Chronological Index:** 318 of 995  
**Date:** 2026-07-23  
**Section:** III. Structural Honesty — Core Papers  
**Source File:** AXSH5_R3_ABSORPTION_RECEIPT.md  
**Source Format:** md  
**SHA-256:** `eea4328b30cc998ad65c550c17cc67a0afad6693444f3203ed05df182b071927`  

---

## R0081 · AXSH5 Round-3 Absorption Receipt (Authoritative Return Receipt)

- section: III. Structural Honesty — Core Papers
- source_file: AXSH5_R3_ABSORPTION_RECEIPT.md
- source_format: md
- text_sha256: eea4328b30cc998ad65c550c17cc67a0afad6693444f3203ed05df182b071927

# AXSH5 Round-3 Absorption Receipt (Authoritative Return Receipt)

**Role:** Perplexity, producer of the AX-SH 5 release packet; executed as the Anthropic / Claude Opus 4.8 council seat for the Round-3 governance-only absorption.
**Round:** GOVERNANCE-ONLY surgical-amendment absorption of Fable Round-2 findings F-EI-10 (MEDIUM), F-EI-11 (LOW), F-EI-12 (LOW), plus the parent-council Round-3 corrections F-EI-13..F-EI-16.
**Decision:** Branch A (frozen instrument byte-identical; no full audit round reopened). Branch B remains UNELECTED and was not executed.
**Date:** July 24, 2026.

## 1. Mandatory intake gate results

| Gate step | Result |
| --- | --- |
| Dispatch `sha256sum -c SHA256SUMS` (6 members, excludes itself) | 6/6 OK |
| Baseline `axsh5-release-packet.zip` = Section-2 hash `6b7544...1077` | Match |
| Baseline internal `sha256sum -c SHA256SUMS` | 15/15 OK |
| Frozen `is-evidence-independence-an-axiom-canonical.pplx.md` `fcd1e70d...` | Match |
| Frozen `is-evidence-independence-an-axiom-canonical.pdf` `3e757231...` | Match |
| Frozen `axsh5_content.py` `d58830c1...` | Match |

No mismatch at intake; absorption proceeded.

## 2. Frozen instrument -- UNCHANGED (Branch A)

The three Section-3 instrument members are byte-identical to the baseline. No instrument byte was touched in Round-3.

| Frozen member | SHA-256 (unchanged) |
| --- | --- |
| `is-evidence-independence-an-axiom-canonical.pplx.md` | `fcd1e70d9f24066f9403e41612dc3b7a48c902e683cc16913273dd79f39d9255` |
| `is-evidence-independence-an-axiom-canonical.pdf` | `3e7572312c7bf48409897be4923ceb15128d313c441c1609924511038fe55549` |
| `axsh5_content.py` | `d58830c1def16bd0717b895315311fb09c33dd4d70ff55cad10b77044712a224` |

## 3. Finding -> change -> member mapping (Fable Round-2 findings)

**F-EI-10 [MEDIUM] -- transformed audit-trail members lacked integrity binding.** Routes a-d:
- (a) Integrity binding: raw originals shipped in-packet under `historical_inputs/` (gate-exempt, G9 rev B) AND new member `historical-originals-manifest.md` records per member the raw filename, raw SHA-256, packet-copy SHA-256, and transformation classes. Members: ADDED `historical_inputs/*` (8 files), ADDED `historical-originals-manifest.md`.
- (b) Fable editions: ADDED auditor-issued `claude-fable-5-audit-round1-2026-07-23.md` and `claude-fable-5-audit-round2-2026-07-24.md`; the transformed copy was RENAMED to `claude-fable-5-audit-2026-07-23-DERIVED-SUPERSEDED.md` and declared a superseded derived copy.
- (c) Editorial notes: retained bracketed in place; admissible because (a) ships hash-bound originals. Exact cardinality corrected under F-EI-14 (below).
- (d) README provenance claim corrected: CHANGED `README.md` (enumerates actual transformation classes; points to manifest).

**F-EI-11 [LOW] -- phantom finding ID.** CHANGED `remediation-receipt.md`: Section 5 heading relabeled from "(F-EI-12)" to "Mechanical QA results," with a note that the former label predates and is unrelated to the real F-EI-12.

**F-EI-12 [LOW] -- generation path + block-count.** ADDED `emit_markdown.py`, `emit_pdf.py` (auditable executable build tools, hashes in packet SHA256SUMS). CHANGED `remediation-receipt.md` Section 1 (softened to "generated from one source; the concordance receipt is the operative parity guarantee"). CHANGED `concordance_receipt.txt` (block-universe definition; corrected to 116 of 166 per F-EI-13).

## 4. Member-level DISPATCH BASELINE -> FINAL SHA-256 (changed / added live members)

Hashes are stated as **DISPATCH BASELINE** (the Fable Round-2 baseline packet `axsh5-release-packet.zip`, internal SHA256SUMS) **-> FINAL** (this returned archive). `historical-originals-manifest.md` did not exist in the baseline and is marked ABSENT/ADDED.

| Live member | DISPATCH BASELINE | FINAL |
| --- | --- | --- |
| `README.md` | `1ffd02d8b14f9014b96185ec1db2832265d14f4862eec8a50e0e66b251bee950` | `9b264483664fdd550fa541d42a201453518df7c18343a0950d1ba7de62515aa5` |
| `remediation-receipt.md` | `feb5846378662dd6645d7c84548534dec3eb9ac5f4cd4dd68fa46f3c00333da4` | `36d4dd294d134a9fb2d26827aa5d5e9f152ceadba251a0dfaa273a453a91cf50` |
| `concordance_receipt.txt` | `2c98f7511711fcae200e7815920a2da80737a35f02645cf5edb307188199d224` | `fe948d39c74a3249ddcb1f8fe4411e37b08c6f9aa65cd321c8cb789a4682016e` |
| `ax-sh-5-model-council-adjudication.pplx.md` | `029e7b92ab0d95f24c7e348283738e36fe89825a94bfd8bd91ff7238714a9ced` | `3584422b25fff589378204d811535448ab21afd934e7ca3d7260b4e782e11815` |
| `historical-originals-manifest.md` | `ABSENT/ADDED` | `9464a1d9932a558c97e9d1fa18312655cc0571e2ba2199d1ecf37adbc7ef0340` |

No other live member changed relative to the dispatch baseline except the ADDED members enumerated in Section 5. The three frozen instrument members are byte-identical to the baseline; all historical members (`historical_inputs/*`, the two auditor editions, the derived-superseded copy) are unchanged in this revision.

## 5. ADDED / REMOVED / RENAMED members (relative to the Fable Round-2 baseline)

**ADDED (new members):**
- `historical-originals-manifest.md`
- `AXSH5_R3_ABSORPTION_RECEIPT.md`
- `emit_markdown.py`
- `emit_pdf.py`
- `claude-fable-5-audit-round1-2026-07-23.md`
- `claude-fable-5-audit-round2-2026-07-24.md`
- `claude-fable-5-audit-2026-07-23-DERIVED-SUPERSEDED.md`
- `historical_inputs/ax-sh-5-google-council-review.pplx.md`
- `historical_inputs/ax-sh-5-independent-review-20260723.pplx.md`
- `historical_inputs/ax-sh-5-independent-review.pplx.md`
- `historical_inputs/ax-sh-5-stress-test-adjudication-memo.pplx.md`
- `historical_inputs/ax-sh-a5-observer-independence.pplx.md`
- `historical_inputs/axsh5-gemini31pro-delta-reattestation.pplx.md`
- `historical_inputs/axsh5-gpt54-delta-reattestation.pplx.md`
- `historical_inputs/claude-fable-5-audit-2026-07-23.md`

**RENAMED (superseded, not deleted):**
- `claude-fable-5-audit-2026-07-23.md` -> `claude-fable-5-audit-2026-07-23-DERIVED-SUPERSEDED.md` (retained as a derived copy superseded by the auditor-issued editions; hash-bound in the manifest)

**REMOVED:** none. Append-only governance: nothing was deleted; the transformed Fable copy was superseded by rename, not removed.

## 6. Parent-council correction adjudication table (F-EI-13 .. F-EI-16)

| ID | Severity | Origin | Disposition | Live members touched |
| --- | --- | --- | --- | --- |
| F-EI-13 | MEDIUM | GPT | ACCEPTED. Executable `axsh5_content.BLOCKS` = 166, not 174; concordance universe = 116 prose blocks of 166. 174 preserved only in the historical GPT delta report with a live correction note. No instrument byte changed. | `concordance_receipt.txt`, `README.md`, `remediation-receipt.md`, `ax-sh-5-model-council-adjudication.pplx.md`, this receipt |
| F-EI-14 | LOW | GPT | ACCEPTED. Exact cardinality: 3 editorial-note insertions across the two named seat reports (1 Opus, 2 GPT delta) + 1 in the derived Fable copy. Retention allowed (raws shipped and hash-bound). | `historical-originals-manifest.md`, `remediation-receipt.md`, this receipt |
| F-EI-15 | (n/a) | GPT | REJECTED / NOT APPLICABLE. Concerned a local extracted working directory, not a member of the returned archive. Archive ships no working dir, `__pycache__`, `.pyc`, or undeclared extraction. | none (verified by QA) |
| F-EI-16 | LOW | Producer (self-identified; renumbered from the producer's earlier stale-pointer finding to avoid namespace collision) | ACCEPTED. Stale live pointers from the F-EI-10b rename SELF-REPAIRED; all live governance pointers resolve. No absence-credit claimed (Ruling 4). | `remediation-receipt.md`, `ax-sh-5-model-council-adjudication.pplx.md` |

## 7. Final packet member count

Exact composition of the returned archive: **29 members are listed in the packet-internal `SHA256SUMS`, plus `SHA256SUMS` itself = 30 total files.** There is exactly **one subdirectory, `historical_inputs/`** (holding the 8 raw historical originals); no other directories exist in the archive (no working directory, no `__pycache__`).

## 8. Final zip SHA-256 (post-build; external)

The final archive SHA-256 cannot be embedded inside itself. It is published in the external sibling receipt `AXSH5_R3_RETURN_SHA256SUMS.txt` (alongside the three frozen hashes) and in `AXSH5_R3_PRODUCER_COMPLETION_REPORT.md`.

POST-BUILD FIELD (filled after zip build, external to the archived member): see `AXSH5_R3_RETURN_SHA256SUMS.txt`.

---

# Bismillah ir-Rahman ir-Rahim
