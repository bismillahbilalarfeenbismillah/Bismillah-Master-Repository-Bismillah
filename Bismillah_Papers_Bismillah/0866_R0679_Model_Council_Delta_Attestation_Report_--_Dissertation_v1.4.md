# Bismillah ir-Rahman ir-Rahim

# R0679 -- Model Council Delta Attestation Report -- Dissertation v1.4

**Chronological Index:** 866 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** model-council-gemini_3_1_pro (22).md  
**Source Format:** md  
**SHA-256:** `c7139c4e4d999bdd75a428af386895e21523feb95ddebbb1abfc255e449b9a29`  

---

## R0679 · Model Council Delta Attestation Report -- Dissertation v1.4

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: model-council-gemini_3_1_pro (22).md
- source_format: md
- text_sha256: c7139c4e4d999bdd75a428af386895e21523feb95ddebbb1abfc255e449b9a29

# Model Council Delta Attestation Report -- Dissertation v1.4

**Identity Declaration:**
- Model: Gemini 3.1 Pro
- Vendor: Google
- Tier: Frontier carrying seat
- Namespace: F-DG-NN (Findings will use F-DG-01, etc.)

## Execution of Bounded Receipt-Only Scope

**1. Instrument Identity Verification**
Verified the unchanged hashes for the core dissertation instruments across the v1.4 packet.
The following files were confirmed to match the round-2 anchors:
- Source (`Structural_Honesty_Dissertation_v1_4_source.md`): `92ac1f1d88dc50c94d433a8b5e53e026260244e8710ce75ce5109421c5146e17`
- Canon (`Structural_Honesty_Dissertation_v1_4_canon.md`): `d4f1da364b5f068ad536a00bc4a46e08a8779b8f640e8ba42bf9370041053416`
- PDF (`Structural_Honesty_Dissertation_v1_4.pdf`): `cfe04c4de6fad5c0365ed9446c8c0aad0a16b8f4fd6ef70492522a212768877f` (Checked in PUBLICATION archive)
- DOCX (`Structural_Honesty_Dissertation_v1_4.docx`): `da61eafc8682d69764faf89bc9e1efa27dcbb82c60780b74ebf7540905797883` (Checked in audit archive)
- HTML (`Structural_Honesty_Dissertation_v1_4.html`): `b11114777f393617188c05d4c1bb4af9a5ef1b861020852ab24cc569db39c5d1`
- Bibliography (`Structural_Honesty_Dissertation_bibliography.bib`): `545e00bb58fa63146cb49b17cdd29667138502deb9145a496b5991e62ce165d4`

**2. Cross-Packet Governance Identity**
I compared the `Structural_Honesty_Dissertation_audit_ledger.md` and `Structural_Honesty_Dissertation_punch_list.md` files byte-for-byte between the PUBLICATION and audit_trail archives.
- Byte identity confirmed: Both files match exactly across the two archives.
- Content check: The audit ledger successfully contains the literal strings "Section: v1.4" and its "Round-2 addendum". (The punch list does not contain these strings, aligning with the grammar of the brief which applies these specific literals to the ledger). The prior F-DG-12 failure (stale audit-trail governance) has been successfully resolved.

**3. Manifest Re-derivation**
Calculated SHA-256 sums for all files in both the `publication/Dissertation_v1_4_PUBLICATION` and `audit` archives and cross-referenced them with the corresponding `SHA256SUMS.txt` files.
- The recalculated hashes perfectly match those listed in the manifests for all files present.
- The `SHA256SUMS.txt` file rightfully excludes itself from its own manifest, adhering to the self-exclusion rule.

**4. Metadata Status Currency**
Examined `DEPOSIT_METADATA_v1_4.md`:
- Confirmed the presence of "version 1.4" (specifically reading: "Status: working research monograph, version 1.4.").
- Confirmed zero occurrences of the stale "version 1.3" string.

**5. Baseline Verifications**
Verified the hashes of the baseline documents:
- `canon_v1_2_baseline.md`: `38dfa91dcae27ba5d90a07c3acb1d6719d96b5a351e5f1c4c2502f7038490eca`
- `canon_v1_3_baseline.md`: `4467dd1e5e9cf069db85d98e12fb6b41d1c7f11d4961b248120b58c4c9a77ba8`
- `Structural_Honesty_Dissertation_v1_3_baseline_source.md`: `56178d29e01967e51aa4541a48fa737fc66438b170820a113299b7319945b8c5`

**6. Verifier Execution (rev B)**
Executed `verify_dissertation_v1_4.py` (rev B) in both the PUBLICATION and audit archives.
- **Audit archive result**: `VERIFIER: ALL PASS`
- **PUBLICATION archive result**: `VERIFIER: ALL PASS`
The verifier script correctly inspects all available text members. It successfully executes and passes even in the audit archive where only a subset of text members (source, canon, html, docx) is present, proving the trail invocation is non-vacuous and correctly hardened in rev B to avoid the previous all-pass PDF-conditional failure.

## Verified Hashes
The following SHA-256 hashes were independently verified during this execution:
- `Structural_Honesty_Dissertation_v1_4_source.md`: `92ac1f1d88dc50c94d433a8b5e53e026260244e8710ce75ce5109421c5146e17`
- `Structural_Honesty_Dissertation_v1_4_canon.md`: `d4f1da364b5f068ad536a00bc4a46e08a8779b8f640e8ba42bf9370041053416`
- `Structural_Honesty_Dissertation_v1_4.pdf`: `cfe04c4de6fad5c0365ed9446c8c0aad0a16b8f4fd6ef70492522a212768877f`
- `Structural_Honesty_Dissertation_v1_4.docx`: `da61eafc8682d69764faf89bc9e1efa27dcbb82c60780b74ebf7540905797883`
- `Structural_Honesty_Dissertation_v1_4.html`: `b11114777f393617188c05d4c1bb4af9a5ef1b861020852ab24cc569db39c5d1`
- `Structural_Honesty_Dissertation_bibliography.bib`: `545e00bb58fa63146cb49b17cdd29667138502deb9145a496b5991e62ce165d4`
- `Structural_Honesty_Dissertation_audit_ledger.md`: `2efd9c5ea106fc63bed66988f11be1f8b8440ef698a6fe25a3b9c52633208400`
- `Structural_Honesty_Dissertation_punch_list.md`: `05dda53c689fd5d41a4c84ea4fdd805bb183e710cc7861c77efd8b7783b81323`
- `DEPOSIT_METADATA_v1_4.md`: `1f29c8532f58ee4ec303ab3e62b4b47c1960fba33f7c5db6d981f2910667c257`
- `canon_v1_2_baseline.md`: `38dfa91dcae27ba5d90a07c3acb1d6719d96b5a351e5f1c4c2502f7038490eca`
- `canon_v1_3_baseline.md`: `4467dd1e5e9cf069db85d98e12fb6b41d1c7f11d4961b248120b58c4c9a77ba8`
- `Structural_Honesty_Dissertation_v1_3_baseline_source.md`: `56178d29e01967e51aa4541a48fa737fc66438b170820a113299b7319945b8c5`
- `verify_dissertation_v1_4.py`: `8016cf6e4568c999620e3eea63e6485e7855adecf3e5bb4142429108f4622ce8`
- `SHA256SUMS.txt` (audit): `fda5bae46a2f20528f769ad83769033bb96ae183dba3dd2bd4f55b7ccda73f1e`
- `SHA256SUMS.txt` (publication): `2f0047d68be8bf29d2f4d2472d2359bf8bdc35b2e6eb76335d846e113396a939`
- `BUILD_CORRIGENDUM_2026-07-22.md`: `275883b540035df2006e0ef3e44ba156b9313d4c94987d892fcebd869692f3a6`
- `DELTA_ATTESTATION_BRIEF_v1_3.md`: `a2f6f9371cf4b5e2183b2cd0d2478bd96c74d4e5c7bb2347b92c717c8f5caeb0`
- `DELTA_ATTESTATION_BRIEF_v1_4.md`: `e96c03d5841cf4118be3151ce01fa5b00cfda971ece5bd15842a8bbd3563a45c`
- `README_PUBLICATION.md`: `216f6db7c86548ddd8cdb15fb64dc09349866626dac0759f0f422c22eea40894`
- `RECEIPT_ROUND_BRIEF_v1_4.md`: `636876121d5a246debb6b39a62ecd89acd3f5875b29ceacc6868b1805c648ee4`
- `SHV_Method_v1_1.pdf`: `8f8b43584219a52802f8ace4b4e49021448366b2a044b281ada00ba5762a8896`

## Findings
No adverse findings discovered.

[F-DG-01] CONTROL/LOW
- **Location/Locus**: Cross-packet governance files (`Structural_Honesty_Dissertation_audit_ledger.md` and `Structural_Honesty_Dissertation_punch_list.md` across both archives).
- **Claim/Substance**: The audit ledger and punch list must be byte-identical across the PUBLICATION and audit_trail archives, and the ledger must contain the literal strings "Section: v1.4" AND its "Round-2 addendum".
- **Evidence/Observation**: Byte-for-byte identity was confirmed for both the ledger and punch list via direct binary read. The audit ledger in both archives successfully contains both required strings. The punch list does not contain these strings (and is not expected to per the brief's precise grammar).
- **Disposition/Impact**: Resolves the previous F-DG-12 failure (stale audit-trail governance) by confirming identical up-to-date governance structures.
- **Cross-Reference/Trace**: Relates to Section 1 rules of `DELTA_ATTESTATION_BRIEF_v1_3.md` and the S-register of the ledger.
- **Verdict Effect**: Supports PASS-DELTA; no adverse effect.

[F-DG-02] CONTROL/LOW
- **Location/Locus**: Verifier execution (`verify_dissertation_v1_4.py` rev B) inside both isolated archives.
- **Claim/Substance**: The verifier script must run correctly on all available text members without vacuous PDF-conditional false passes.
- **Evidence/Observation**: Execution in both the PUBLICATION and audit archives yields `VERIFIER: ALL PASS`. The script correctly aggregates text from `.md`, `.html`, `.docx`, and `.pdf` files present in the respective execution context, proving non-vacuous operation even in the audit archive where the PDF is absent.
- **Disposition/Impact**: Confirms successful hardening of the verifier logic to rev B, resolving the advisory finding from Round 2.
- **Cross-Reference/Trace**: Relates to verifier claim (S-3) in the v1.4 audit ledger.
- **Verdict Effect**: Supports PASS-DELTA; no adverse effect.

## Conclusion and Verdict
All verification legs passed. The structural and governance integrity of the v1.4 packet is fully intact and aligned with the round brief requirements. The producer successfully resolved the F-DG-12 discrepancy identified in Round 2.

**Verdict: PASS-DELTA**
This seat **carries convergence** for the Google vendor family.

---

# Bismillah ir-Rahman ir-Rahim
