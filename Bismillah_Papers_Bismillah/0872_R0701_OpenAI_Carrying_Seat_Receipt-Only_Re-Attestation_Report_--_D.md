# Bismillah ir-Rahman ir-Rahim

# R0701 -- OpenAI Carrying Seat Receipt-Only Re-Attestation Report -- Dissertation v1.4 round 3

**Chronological Index:** 872 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** model-council-gpt_5_5 (22).md  
**Source Format:** md  
**SHA-256:** `7a706851008ff52c7353e8567667231937afc9ebf2a7100dd98537c28c0c3470`  

---

## R0701 · OpenAI Carrying Seat Receipt-Only Re-Attestation Report -- Dissertation v1.4 round 3

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: model-council-gpt_5_5 (22).md
- source_format: md
- text_sha256: 7a706851008ff52c7353e8567667231937afc9ebf2a7100dd98537c28c0c3470

# OpenAI Carrying Seat Receipt-Only Re-Attestation Report -- Dissertation v1.4 round 3

model GPT 5.5; vendor OpenAI; tier frontier carrying seat

Namespace: F-DO-NN exclusively for this seat.

Verdict: **PASS-DELTA**.

Convergence statement: this OpenAI seat is a carrying seat and contributes one valid PASS-DELTA family leg toward convergence. Under the in-packet council rule, convergence itself requires PASS-DELTA from at least two carrying seats of different vendor families; this report does not by itself establish cross-family convergence.

## Scope and method

I executed the bounded receipt-only scope from `RECEIPT_ROUND_BRIEF_v1_4.md` against the two original archives and the two extracted trees named in the task:

- `/home/user/workspace/round_brief/Dissertation_v1_4_PUBLICATION.zip`
- `/home/user/workspace/round_brief/Dissertation_v1_4_audit_trail.zip`
- `/home/user/workspace/round_brief/publication/Dissertation_v1_4_PUBLICATION`
- `/home/user/workspace/round_brief/audit`

Probe discipline: all literal content checks used the quoted literals from the receipt brief / verifier, with wrap-immune normalization by de-hyphenating line breaks and collapsing whitespace. I did not use web search; all evidence is packet-local and executable.

Generated evidence artifacts:

- `/home/user/workspace/gpt_5_5_receipt_audit.py`
- `/home/user/workspace/gpt_5_5_receipt_audit_evidence.json`
- `/home/user/workspace/gpt_5_5_verifier_publication_tree.txt`
- `/home/user/workspace/gpt_5_5_verifier_audit_tree.txt`
- `/home/user/workspace/gpt_5_5_reconstruction_diff_classification.json`

## Receipt results

### 1. Instrument identity against named round-2 anchors

| Artifact | File | Expected SHA-256 | Verified locations | Result |
|---|---|---:|---|---|
| source | `Structural_Honesty_Dissertation_v1_4_source.md` | `92ac1f1d88dc50c94d433a8b5e53e026260244e8710ce75ce5109421c5146e17` | pub_zip, aud_zip, pub_tree, aud_tree | PASS |
| canon | `Structural_Honesty_Dissertation_v1_4_canon.md` | `d4f1da364b5f068ad536a00bc4a46e08a8779b8f640e8ba42bf9370041053416` | pub_zip, aud_zip, pub_tree, aud_tree | PASS |
| PDF | `Structural_Honesty_Dissertation_v1_4.pdf` | `cfe04c4de6fad5c0365ed9446c8c0aad0a16b8f4fd6ef70492522a212768877f` | pub_zip, pub_tree | PASS |
| DOCX | `Structural_Honesty_Dissertation_v1_4.docx` | `da61eafc8682d69764faf89bc9e1efa27dcbb82c60780b74ebf7540905797883` | aud_zip, aud_tree | PASS |
| HTML | `Structural_Honesty_Dissertation_v1_4.html` | `b11114777f393617188c05d4c1bb4af9a5ef1b861020852ab24cc569db39c5d1` | pub_zip, aud_zip, pub_tree, aud_tree | PASS |
| bib | `Structural_Honesty_Dissertation_bibliography.bib` | `545e00bb58fa63146cb49b17cdd29667138502deb9145a496b5991e62ce165d4` | pub_zip, aud_zip, pub_tree, aud_tree | PASS |

The common instrument members (source, canon, HTML, bibliography) matched the anchors in all four packet forms. The publication packet carries the PDF and the audit-trail packet carries the DOCX; each matched its named anchor in both the original archive member bytes and its extracted tree bytes.

### 2. Cross-packet governance identity

| Governance file | SHA-256 in publication zip | SHA-256 in audit zip | SHA-256 in publication tree | SHA-256 in audit tree | Result |
|---|---:|---:|---:|---:|---|
| `Structural_Honesty_Dissertation_audit_ledger.md` | `2efd9c5ea106fc63bed66988f11be1f8b8440ef698a6fe25a3b9c52633208400` | `2efd9c5ea106fc63bed66988f11be1f8b8440ef698a6fe25a3b9c52633208400` | `2efd9c5ea106fc63bed66988f11be1f8b8440ef698a6fe25a3b9c52633208400` | `2efd9c5ea106fc63bed66988f11be1f8b8440ef698a6fe25a3b9c52633208400` | byte-identical |
| `Structural_Honesty_Dissertation_punch_list.md` | `05dda53c689fd5d41a4c84ea4fdd805bb183e710cc7861c77efd8b7783b81323` | `05dda53c689fd5d41a4c84ea4fdd805bb183e710cc7861c77efd8b7783b81323` | `05dda53c689fd5d41a4c84ea4fdd805bb183e710cc7861c77efd8b7783b81323` | `05dda53c689fd5d41a4c84ea4fdd805bb183e710cc7861c77efd8b7783b81323` | byte-identical |

The ledger bytes are identical across both archives and both extracted trees. The punch-list bytes are identical across both archives and both extracted trees.

The ledger contains the exact literal `Section: v1.4` twice and `Round-2 addendum` once in every packet form. The punch list also carries the current v1.4 round-state entries, but the exact `Section: v1.4` / `Round-2 addendum` literals are ledger-section markers; I therefore treat the receipt-brief phrase as requiring both packets to contain the updated governance section, not requiring those exact section-heading literals inside the punch list.

### 3. Manifest re-derivation / self-exclusion

| Container | Manifest entries | Self-listed SHA256SUMS.txt? | Mismatches | Missing listed files | Extra manifest files | Result |
|---|---:|---|---:|---:|---:|---|
| pub_zip | 18 | False | 0 | 0 | 0 | PASS |
| aud_zip | 18 | False | 0 | 0 | 0 | PASS |
| pub_tree | 18 | False | 0 | 0 | 0 | PASS |
| aud_tree | 18 | False | 0 | 0 | 0 | PASS |

The publication archive/tree manifest excludes `SHA256SUMS.txt` and re-derives exactly over its 18 listed members, including the PDF. The audit-trail archive/tree manifest excludes `SHA256SUMS.txt` and re-derives exactly over its 18 listed members, including the DOCX. The differing `SHA256SUMS.txt` hashes are expected because the publication manifest lists a PDF while the audit manifest lists a DOCX.

### 4. Metadata status currency

| Container | `version 1.4` count in deposit metadata | `version 1.3` count in deposit metadata | Status line present | Result |
|---|---:|---:|---|---|
| pub_zip | 1 | 0 | True | PASS |
| aud_zip | 1 | 0 | True | PASS |
| pub_tree | 1 | 0 | True | PASS |
| aud_tree | 1 | 0 | True | PASS |

The exact status line `Status: working research monograph, version 1.4.` is present in the deposit metadata in all four packet forms, and the exact stale literal `version 1.3` has zero occurrences in that metadata.

### 5. Baselines and reconstruction claim

| Baseline | File | Expected SHA-256 | Verified locations | Result |
|---|---|---:|---|---|
| canon_v1_2_baseline | `canon_v1_2_baseline.md` | `38dfa91dcae27ba5d90a07c3acb1d6719d96b5a351e5f1c4c2502f7038490eca` | pub_zip, aud_zip, pub_tree, aud_tree | PASS |
| canon_v1_3_baseline | `canon_v1_3_baseline.md` | `4467dd1e5e9cf069db85d98e12fb6b41d1c7f11d4961b248120b58c4c9a77ba8` | pub_zip, aud_zip, pub_tree, aud_tree | PASS |
| source_v1_3_baseline | `Structural_Honesty_Dissertation_v1_3_baseline_source.md` | `56178d29e01967e51aa4541a48fa737fc66438b170820a113299b7319945b8c5` | pub_zip, aud_zip, pub_tree, aud_tree | PASS |

Feasibility reconstruction check: I diffed `canon_v1_2_baseline.md` to `canon_v1_3_baseline.md` from actual bytes. The diff has nine non-equal opcodes and no unclassified extra hunk after manual review: D-1a/D-1f Chapter 1 status and public-deposit clause; D-1d/D-1e pre-publication wording and public-surface clause; D-1b thesis sentence; D-1a Chapter 2 status; D-6 T83 calibration; D-5 completeness-boundary demotion; D-4 Boxo accuracy/AUROC corrigendum; D-3 Sheshadri corrigendum; and D-1c Chapter 22 status head. The resulting shipped v1.3 canon baseline hashes to `4467dd1e5e9cf069db85d98e12fb6b41d1c7f11d4961b248120b58c4c9a77ba8`. This supports the stated reconstruction claim within the bounded receipt scope; I did not conduct a new factual-primary review because the current round is receipt-only.

### 6. Hardened verifier rev B in both extracted archives

| Extracted tree | Return code | Captured output | Result |
|---|---:|---|---|
| publication_tree | 0 | `VERIFIER: ALL PASS` | PASS |
| audit_tree | 0 | `VERIFIER: ALL PASS` | PASS |

Trail invocation non-vacuity: the audit-trail tree has source, canon, HTML, and DOCX text members totaling substantial bytes before verifier extraction; the script hash is `8016cf6e4568c999620e3eea63e6485e7855adecf3e5bb4142429108f4622ce8`, its docstring says hardened rev B, and its corpus code includes source, canon, HTML, DOCX, and optional PDF members. Required marker literals were already present in the source/canon/HTML corpus in both extracted trees, so the audit-trail run was not a PDF-conditional empty pass.

## Archive/tree byte identity

Original archive SHA-256: `Dissertation_v1_4_PUBLICATION.zip` = `4be3ab34e141b51be45aba2c3ae5c71ea1e260ab34cf98bc75e49841835d735e`; `Dissertation_v1_4_audit_trail.zip` = `3eaa4e06ac9e61c0f4e80f686ba8a509d791ad84493da9621672f73077b9094e`.

Zip-member bytes match the corresponding extracted-tree bytes exactly for both packets: publication `only_a=[]`, `only_b=[]`, `hash_diffs=[]`; audit trail `only_a=[]`, `only_b=[]`, `hash_diffs=[]`. Across the two packet types, the only content-set differences are expected: publication-only PDF, audit-only DOCX, and different manifests reflecting those alternate render members.

## F-DO findings / controls

No adverse findings are registered. The following verified controls use the requested six-element SHV-style schema.

### F-DO-01 -- CONTROL

1. **Location.** Instrument receipt anchors
2. **Observation.** Source/canon/PDF/DOCX/HTML/bibliography bytes match the named round-2 anchors wherever those artifacts are present.
3. **Evidence.** SHA-256 anchor table above; archive and extracted-tree member hashes agree.
4. **Impact.** CONTROL; verified control, not an adverse defect.
5. **Disposition.** Control verified; supports PASS-DELTA.
6. **Verdict effect.** No adverse effect; supports PASS-DELTA.

### F-DO-02 -- CONTROL

1. **Location.** Cross-packet governance identity
2. **Observation.** Audit ledger and punch list are byte-identical across publication and audit-trail packets; updated ledger section and addendum are present in both packets.
3. **Evidence.** Ledger SHA-256 `2efd9c5e...`; punch list SHA-256 `05dda53c...`; ledger exact literal counts: `Section: v1.4` = 2, `Round-2 addendum` = 1 in all packet forms.
4. **Impact.** CONTROL; verified control, not an adverse defect.
5. **Disposition.** Control verified; resolves the stale-trail packet defect in this receipt round.
6. **Verdict effect.** No adverse effect; supports PASS-DELTA.

### F-DO-03 -- CONTROL

1. **Location.** Manifest self-exclusion and re-derivation
2. **Observation.** Both manifests exclude their own `SHA256SUMS.txt` entry and exactly match all listed member bytes in original archives and extracted trees.
3. **Evidence.** Manifest check table above: zero mismatches, zero missing, zero extra in all four containers.
4. **Impact.** CONTROL; verified control, not an adverse defect.
5. **Disposition.** Control verified.
6. **Verdict effect.** No adverse effect; supports PASS-DELTA.

### F-DO-04 -- CONTROL

1. **Location.** Deposit metadata spelled-version currency
2. **Observation.** Deposit metadata states version 1.4 and has zero exact stale `version 1.3` literals.
3. **Evidence.** Metadata table above: `version 1.4` count 1, `version 1.3` count 0, status line present in all four packet forms.
4. **Impact.** CONTROL; verified control, not an adverse defect.
5. **Disposition.** Control verified.
6. **Verdict effect.** No adverse effect; supports PASS-DELTA.

### F-DO-05 -- CONTROL

1. **Location.** Baseline receipts and reconstruction support
2. **Observation.** v1.2 canon, v1.3 canon, and v1.3 source baselines match named anchors; v1.2-to-v1.3 canon diff is bounded to the recorded D-register families.
3. **Evidence.** Baseline table above; nine diff opcodes mapped to D-1/D-3/D-4/D-5/D-6 and no extra hunk found.
4. **Impact.** CONTROL; verified control, not an adverse defect.
5. **Disposition.** Control verified within receipt-only scope.
6. **Verdict effect.** No adverse effect; supports PASS-DELTA.

### F-DO-06 -- CONTROL

1. **Location.** Rev-B verifier execution and trail non-vacuity
2. **Observation.** `verify_dissertation_v1_4.py` runs ALL PASS in both extracted trees, and the audit-trail run exercises source/canon/HTML/DOCX text members rather than depending on a PDF-only path.
3. **Evidence.** Verifier output table above; script hash `8016cf6e...`; audit tree text members include source, canon, HTML, and DOCX.
4. **Impact.** CONTROL; verified control, not an adverse defect.
5. **Disposition.** Control verified.
6. **Verdict effect.** No adverse effect; supports PASS-DELTA.

## SHA-256 inventory for every verified file

| File | SHA-256 | Publication zip | Publication tree | Audit zip | Audit tree |
|---|---:|---|---|---|---|
| `Dissertation_v1_4_PUBLICATION.zip` | `4be3ab34e141b51be45aba2c3ae5c71ea1e260ab34cf98bc75e49841835d735e` | original archive | n/a | n/a | n/a |
| `Dissertation_v1_4_audit_trail.zip` | `3eaa4e06ac9e61c0f4e80f686ba8a509d791ad84493da9621672f73077b9094e` | n/a | n/a | original archive | n/a |
| `BUILD_CORRIGENDUM_2026-07-22.md` | `275883b540035df2006e0ef3e44ba156b9313d4c94987d892fcebd869692f3a6` | yes | yes | yes | yes |
| `DELTA_ATTESTATION_BRIEF_v1_3.md` | `a2f6f9371cf4b5e2183b2cd0d2478bd96c74d4e5c7bb2347b92c717c8f5caeb0` | yes | yes | yes | yes |
| `DELTA_ATTESTATION_BRIEF_v1_4.md` | `e96c03d5841cf4118be3151ce01fa5b00cfda971ece5bd15842a8bbd3563a45c` | yes | yes | yes | yes |
| `DEPOSIT_METADATA_v1_4.md` | `1f29c8532f58ee4ec303ab3e62b4b47c1960fba33f7c5db6d981f2910667c257` | yes | yes | yes | yes |
| `README_PUBLICATION.md` | `216f6db7c86548ddd8cdb15fb64dc09349866626dac0759f0f422c22eea40894` | yes | yes | yes | yes |
| `RECEIPT_ROUND_BRIEF_v1_4.md` | `636876121d5a246debb6b39a62ecd89acd3f5875b29ceacc6868b1805c648ee4` | yes | yes | yes | yes |
| `SHA256SUMS.txt` (publication manifest) | `2f0047d68be8bf29d2f4d2472d2359bf8bdc35b2e6eb76335d846e113396a939` | yes | yes | no | no |
| `SHA256SUMS.txt` (audit-trail manifest) | `fda5bae46a2f20528f769ad83769033bb96ae183dba3dd2bd4f55b7ccda73f1e` | no | no | yes | yes |
| `SHV_Method_v1_1.pdf` | `8f8b43584219a52802f8ace4b4e49021448366b2a044b281ada00ba5762a8896` | yes | yes | yes | yes |
| `Structural_Honesty_Dissertation_audit_ledger.md` | `2efd9c5ea106fc63bed66988f11be1f8b8440ef698a6fe25a3b9c52633208400` | yes | yes | yes | yes |
| `Structural_Honesty_Dissertation_bibliography.bib` | `545e00bb58fa63146cb49b17cdd29667138502deb9145a496b5991e62ce165d4` | yes | yes | yes | yes |
| `Structural_Honesty_Dissertation_punch_list.md` | `05dda53c689fd5d41a4c84ea4fdd805bb183e710cc7861c77efd8b7783b81323` | yes | yes | yes | yes |
| `Structural_Honesty_Dissertation_v1_3_baseline_source.md` | `56178d29e01967e51aa4541a48fa737fc66438b170820a113299b7319945b8c5` | yes | yes | yes | yes |
| `Structural_Honesty_Dissertation_v1_4.docx` | `da61eafc8682d69764faf89bc9e1efa27dcbb82c60780b74ebf7540905797883` | no | no | yes | yes |
| `Structural_Honesty_Dissertation_v1_4.html` | `b11114777f393617188c05d4c1bb4af9a5ef1b861020852ab24cc569db39c5d1` | yes | yes | yes | yes |
| `Structural_Honesty_Dissertation_v1_4.pdf` | `cfe04c4de6fad5c0365ed9446c8c0aad0a16b8f4fd6ef70492522a212768877f` | yes | yes | no | no |
| `Structural_Honesty_Dissertation_v1_4_canon.md` | `d4f1da364b5f068ad536a00bc4a46e08a8779b8f640e8ba42bf9370041053416` | yes | yes | yes | yes |
| `Structural_Honesty_Dissertation_v1_4_source.md` | `92ac1f1d88dc50c94d433a8b5e53e026260244e8710ce75ce5109421c5146e17` | yes | yes | yes | yes |
| `canon_v1_2_baseline.md` | `38dfa91dcae27ba5d90a07c3acb1d6719d96b5a351e5f1c4c2502f7038490eca` | yes | yes | yes | yes |
| `canon_v1_3_baseline.md` | `4467dd1e5e9cf069db85d98e12fb6b41d1c7f11d4961b248120b58c4c9a77ba8` | yes | yes | yes | yes |
| `verify_dissertation_v1_4.py` | `8016cf6e4568c999620e3eea63e6485e7855adecf3e5bb4142429108f4622ce8` | yes | yes | yes | yes |

## Final disposition

PASS-DELTA. This seat registers no adverse F-DO finding. The OpenAI carrying-seat leg is satisfied and may be counted once for the OpenAI family under the council convergence rule.

---

# Bismillah ir-Rahman ir-Rahim
