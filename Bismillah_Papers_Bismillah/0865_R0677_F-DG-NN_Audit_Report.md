# Bismillah ir-Rahman ir-Rahim

# R0677 -- F-DG-NN Audit Report

**Chronological Index:** 865 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** model-council-gemini_3_1_pro (20).md  
**Source Format:** md  
**SHA-256:** `37c495207582b5cda243ac62182a40373f807cbda526b3de93bde766a474c94d`  

---

## R0677 · F-DG-NN Audit Report

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: model-council-gemini_3_1_pro (20).md
- source_format: md
- text_sha256: 37c495207582b5cda243ac62182a40373f807cbda526b3de93bde766a474c94d

# F-DG-NN Audit Report
Model: Gemini 3.1 Pro
Vendor: Google
Tier: frontier Pro
Seat Status: CARRYING
Namespace: F-DG-NN

## L1 Canon Delta
**[CONTROL] F-DG-01**
1. **Identifier:** F-DG-01
2. **Observation:** Reconstructed v1.3 canon differs from v1.2 baseline by exactly the expected hunks described in the D-1 through D-6 register items.
3. **Location:** Structural_Honesty_Dissertation_v1_3_source.md vs canon_v1_2_baseline.md
4. **Severity:** CONTROL
5. **Impact:** PASS. Zero findings outside the expected register.
6. **Disposition:** VERIFIED

## L2 Register Fidelity
**[CONTROL] F-DG-02**
1. **Identifier:** F-DG-02
2. **Observation:** Replacement spans in v1.3 source exactly match the replacement specifications in the audit ledger D-1 to D-6 (using wrap-immune normalization). P-1 to P-6 discharges observed and verified.
3. **Location:** Structural_Honesty_Dissertation_v1_3_source.md
4. **Severity:** CONTROL
5. **Impact:** PASS. The required text modifications are present.
6. **Disposition:** VERIFIED

## L3 Fact Legs
**[CONTROL] F-DG-03**
1. **Identifier:** F-DG-03
2. **Observation:** Farrin citation is "The Muslim World 100(1), 17-32, doi 10.1111/j.1478-1913.2009.01299.x". Independent primary search verifies Farrin published "Surat al-Baqara: A structural analysis" in The Muslim World, Volume 100, Issue 1, 2010, pp 17-32.
3. **Location:** Structural_Honesty_Dissertation_bibliography.bib
4. **Severity:** CONTROL
5. **Impact:** PASS. Accuracy established.
6. **Disposition:** VERIFIED

**[CONTROL] F-DG-04**
1. **Identifier:** F-DG-04
2. **Observation:** Sheshadri citation "Why do some language models fake alignment while others don't?" is verified at arXiv:2506.18032 with the correct authorship list.
3. **Location:** Structural_Honesty_Dissertation_bibliography.bib
4. **Severity:** CONTROL
5. **Impact:** PASS. Accuracy established.
6. **Disposition:** VERIFIED

**[CONTROL] F-DG-05**
1. **Identifier:** F-DG-05
2. **Observation:** Boxo citation "Caught in the Act: A Mechanistic Approach to Detecting Deception" is verified at arXiv:2508.19505. The primary source states "larger models (greater than 7B) reach 70-80%", confirming it reports accuracy for the open-source result, not AUROC. The bibliography explicitly clarifies this.
3. **Location:** Structural_Honesty_Dissertation_bibliography.bib
4. **Severity:** CONTROL
5. **Impact:** PASS. Accuracy established.
6. **Disposition:** VERIFIED

## L4 Render Gates
**[CONTROL] F-DG-06**
1. **Identifier:** F-DG-06
2. **Observation:** verify_dissertation_v1_3.py executed and returned "VERIFIER: ALL PASS", confirming chapter-identity, status-currency, and meta-text absence. The subtitle "An Independent Research Monograph" and the flagship DOI 10.5281/zenodo.21500700 are present in DEPOSIT_METADATA_v1_3.md. SHA256SUMS accurately match packet files.
3. **Location:** verify_dissertation_v1_3.py, DEPOSIT_METADATA_v1_3.md
4. **Severity:** CONTROL
5. **Impact:** PASS. Render and metadata constraints met.
6. **Disposition:** VERIFIED

## L5 Calibration Legs
**[CONTROL] F-DG-07**
1. **Identifier:** F-DG-07
2. **Observation:** D-5 correctly demotes the "completeness treatment" to "completeness-boundary treatment" as requested. D-6 accurately scopes T83 adequacy to the author-selected finite judgment set J. The calibration changes match the prescribed demotions.
3. **Location:** Structural_Honesty_Dissertation_v1_3_source.md
4. **Severity:** CONTROL
5. **Impact:** PASS. Required calibration adjustments are present.
6. **Disposition:** VERIFIED

## Verified Hashes
- DELTA_ATTESTATION_BRIEF_v1_3.md: a2f6f9371cf4b5e2183b2cd0d2478bd96c74d4e5c7bb2347b92c717c8f5caeb0
- SHV_Method_v1_1.pdf: 8f8b43584219a52802f8ace4b4e49021448366b2a044b281ada00ba5762a8896
- Structural_Honesty_Dissertation_audit_ledger.md: f7e539bb3733c128fd2abb768861c8ab72c93287d7946695344fcbe25663bb8c
- Structural_Honesty_Dissertation_v1_3_source.md: 56178d29e01967e51aa4541a48fa737fc66438b170820a113299b7319945b8c5
- canon_v1_2_baseline.md: 38dfa91dcae27ba5d90a07c3acb1d6719d96b5a351e5f1c4c2502f7038490eca
- Structural_Honesty_Dissertation_bibliography.bib: 545e00bb58fa63146cb49b17cdd29667138502deb9145a496b5991e62ce165d4
- DEPOSIT_METADATA_v1_3.md: 46f855b166c851a4d9051b7063ddecdad14972f03eca2b7ee35e11202950c191
- verify_dissertation_v1_3.py: 78c8a3b35d66295f24ce0c48157a5ba9416c53fd88ec3e47c9e4c1a1936571ed
- Structural_Honesty_Dissertation_v1_3.pdf: 57560b35ccd75ac4f9e0ace868d25f8c1f76ca05c62cfa5c562b0b9071158fc4
- SHA256SUMS.txt: 776ab8eab660da423eb160b73c78b0ad2502b6d8f57e2206ba7da6ee851fc5cf

## Carrying-Seat Adjudication Addendum
The carrying seat performed a targeted follow-up probe on specific findings:

### 1. Version 1.2 Canonical Reference
**[HIGH/L4-STATUS-CURRENCY] F-DG-08**
1. **Identifier:** F-DG-08
2. **Observation:** The exact phrase `Version 1.2 canonical` survives unpatched in the Abstract of the v1.3 source, HTML, and PDF text, which misrepresents the current version status to readers as "Version 1.2 canonical" despite the update to v1.3. This escaped the `verify_dissertation_v1_3.py` script because it is not in the script's exact literal gate list.
3. **Location:** Structural_Honesty_Dissertation_v1_3_source.md (and rendered HTML/PDF), Abstract section.
4. **Severity:** HIGH
5. **Impact:** NON-PASS on L2 P-1 / L4 status-currency. The reader-facing abstract asserts an outdated version, a material defect in structural honesty (surface misrepresents current status).
6. **Disposition:** FINDING

### 2. Appendix E Reference
**[CONTROL/L2-APP-E-VERIFY] F-DG-09**
1. **Identifier:** F-DG-09
2. **Observation:** The D-1 revision introduced the phrase `the versioned public-deposit line recorded in Appendix E`. A probe across the v1.3 source confirms Appendix E exists and includes 9 references to `v1.3`. The record points to a valid destination.
3. **Location:** Structural_Honesty_Dissertation_v1_3_source.md (Appendix E)
4. **Severity:** CONTROL
5. **Impact:** PASS.
6. **Disposition:** VERIFIED

### 3. T83 Framing Sentence Propagation
**[MEDIUM/L5-CALIBRATION-DROP] F-DG-10**
1. **Identifier:** F-DG-10
2. **Observation:** The text `corresponds to what operational practitioners call structural honesty across the four substrate instances.` appears twice in the baseline and v1.3 source (lines ~1326 and ~1412). The D-6 calibration clause (about finite judgment-set adequacy) was appended to the first instance (Chapter 7 introduction) but NOT propagated to the identical framing sentence in the Chapter 8 framing section.
3. **Location:** Structural_Honesty_Dissertation_v1_3_source.md (around line 1412)
4. **Severity:** MEDIUM
5. **Impact:** FINDING. The calibration clause failed to propagate to the second occurrence of the target sentence, leaving an uncalibrated claim.
6. **Disposition:** FINDING

### 4. D-6 Quotation Fidelity
**[LOW/L2-QUOTATION-DRIFT] F-DG-11**
1. **Identifier:** F-DG-11
2. **Observation:** The actual replaced text for D-6 in the source includes the phrase `with several constructed scenarios` ("principally author-selected and author-labeled, with several constructed scenarios"), which is NOT present in the D-6 ledger quotation.
3. **Location:** Structural_Honesty_Dissertation_v1_3_source.md (D-6 replacement site)
4. **Severity:** LOW
5. **Impact:** FINDING. Minor quotation drift between the ledger specification and the actual applied text.
6. **Disposition:** FINDING

## Updated Verdict
**NON-PASS**

## Updated Register
- F-DG-08: `Version 1.2 canonical` string remains in Abstract.
- F-DG-10: D-6 calibration clause not propagated to second T83 framing sentence.
- F-DG-11: D-6 applied text contains `with several constructed scenarios` not recorded in the ledger.

---

# Bismillah ir-Rahman ir-Rahim
