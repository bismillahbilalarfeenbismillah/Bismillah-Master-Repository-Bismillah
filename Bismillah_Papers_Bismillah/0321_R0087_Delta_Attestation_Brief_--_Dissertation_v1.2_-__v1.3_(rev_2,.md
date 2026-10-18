# Bismillah ir-Rahman ir-Rahim

# R0087 -- Delta Attestation Brief -- Dissertation v1.2 -> v1.3 (rev 2, July 23, 2026)

**Chronological Index:** 321 of 995  
**Date:** 2026-07-23  
**Section:** III. Structural Honesty — Core Papers  
**Source File:** DELTA_ATTESTATION_BRIEF_v1_3.md  
**Source Format:** md  
**SHA-256:** `b41cd9ad11bb2ebfb2566400e3856db019514c27d87d04e8698c5b8c66cd0740`  

---

## R0087 · Delta Attestation Brief -- Dissertation v1.2 -> v1.3 (rev 2, July 23, 2026)

- section: III. Structural Honesty — Core Papers
- source_file: DELTA_ATTESTATION_BRIEF_v1_3.md
- source_format: md
- text_sha256: b41cd9ad11bb2ebfb2566400e3856db019514c27d87d04e8698c5b8c66cd0740

# Delta Attestation Brief -- Dissertation v1.2 -> v1.3 (rev 2, July 23, 2026)
## Addressed to: Perplexity Computer, MODEL-COUNCIL MODE

Rev 2 supersedes rev 1: restructured for a Perplexity-orchestrated council; governing
methodology SHV_Method_v1_1.pdf now ships in the packet (SHA-256
8f8b43584219a52802f8ace4b4e49021448366b2a044b281ada00ba5762a8896 -- verify on receipt).

## 0. What this round is
A delta-scoped attestation of dissertation v1.2 -> v1.3 against the correction register
(D-1..D-9) recorded in the packet's audit ledger, v1.3 section. The register dispositions
Perplexity's own v1.2 review; this round therefore verifies the producer's repairs, and
each seat works from the PACKET AND PRIMARIES, not from the prior review's prose
(record-over-person). Producer (Anthropic lineage, drafting instrument) carries no
verdict; producer self-repairs earn no absence-credit (Ruling 4): verify them, do not
credit their mere presence.

## 1. Council structure and seat rules
- Each seat DECLARES its underlying model, vendor, and tier at the head of its report
  (standing disclosure rule). Undeclared seats carry no verdict.
- Namespaces are per-seat (mandatory): F-D<V>-NN, where <V> is the vendor initial
  (G=Google, O=OpenAI, K=Moonshot, X=xAI, P=other/native) and NN is sequential.
- Lineage exclusions (Ruling 3): Anthropic-lineage seats are ADVISORY ONLY (producer
  lineage); xAI/Grok seats are advisory on Munafiq-adjacent legs (record contributor).
- Family accounting: same-vendor seats count once toward convergence.
- CONVERGENCE = PASS-DELTA from at least TWO carrying seats of DIFFERENT vendor
  families. Refuted findings do not flip a verdict; a seat whose findings are refuted
  re-attests on the corrected instrument (R2b/R3b precedent).

## 2. Verification legs (every seat runs all legs within its capability; gaps are
declared UNKNOWN-BY-CAPABILITY and must be covered by another seat)
- L1 Canon delta. Diff canon_v1_2_baseline.md (SHA 38dfa91dcae27ba5d90a07c3acb1d6719d96b5a351e5f1c4c2502f7038490eca)
  against the v1.3 canon reconstructed from the packet source. The diff must consist of
  exactly the D-1..D-6 register hunks quoted in the ledger; any hunk outside the register
  is a finding.
- L2 Register fidelity. Each D-item's replaced span matches the ledger's quoted old/new
  text, and each disposition discharges the corresponding finding of the v1.2 external
  review (P-1 status currency; P-2a/2b/2c citations; P-3 taxonomy calibration; P-4 T83;
  P-5 metadata; P-6 peer-review labeling).
- L3 Fact legs against primaries (fetch them yourselves): Farrin = The Muslim World
  100(1), 17-32, doi 10.1111/j.1478-1913.2009.01299.x; Sheshadri = arXiv:2506.18032
  (actual title and authorship); Boxo = arXiv:2508.19505 (reports accuracy, not AUROC,
  for the 70-80% open-source result).
- L4 Render gates. Execute verify_dissertation_v1_3.py inside the unpacked kit
  (chapter-identity harness 23+D/E; STATUS-CURRENCY; META-TEXT-ABSENCE;
  author-note/disclaimer render parity; SHA256SUMS re-derivation). Confirm the subtitle
  and the flagship DOI 10.5281/zenodo.21500700 in DEPOSIT_METADATA_v1_3.md.
- L5 Calibration legs. D-5 text claims a completeness-boundary treatment (non-exhaustiveness
  analysis with boundary handling), not a proved partition -- REVERSIBLE-DEFAULT status
  disclosed: the lead may reverse this demotion, and a seat's view on the demotion is
  registered as a finding, not grounds for NON-PASS by itself. D-6 T83 clause claims
  finite judgment-set adequacy relative to the named set J only.

## 3. Probe discipline (defects here are seat findings against the seat)
- ALL text probes use wrap-immune normalization: de-hyphenate line breaks, collapse
  whitespace, then match. A naive grep miss on wrapped text is a probe-specification
  error, not a packet finding.
- Gate token lists are QUOTED LITERALS ONLY; do not probe for item names or prose
  descriptors from this brief.
- Replacement-span checks anchor on actual packet bytes, minimal unique span.

## 4. Findings and verdicts
- Six-element findings format per SHV v1.1; severities UPPERCASE; severity denotes
  adverse defect impact (verified controls take LOW or CONTROL, never CRITICAL/HIGH).
- Per-seat verdict: PASS-DELTA or NON-PASS with register. Council synthesis reports
  per-seat verdicts, the convergence determination under Section 1, and must not launder
  refuted findings into the synthesis.
- Return: per-seat reports (with model declarations) plus synthesis, in one reply;
  include the SHA-256 of every packet file each seat actually verified.

---

# Bismillah ir-Rahman ir-Rahim
