# Bismillah ir-Rahman ir-Rahim

# R0598 -- XZ Protocol v0.23 -- Carry-2 Audit Dispatch

**Chronological Index:** 836 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** DISPATCH_PROMPT_KIMI_CARRY2 (1).md  
**Source Format:** md  
**SHA-256:** `5b00c74286c641a9064a84edc8035c9455c61b040bfcc5b1007c4c2aff5d7d3a`  

---

## R0598 · XZ Protocol v0.23 -- Carry-2 Audit Dispatch

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: DISPATCH_PROMPT_KIMI_CARRY2 (1).md
- source_format: md
- text_sha256: 5b00c74286c641a9064a84edc8035c9455c61b040bfcc5b1007c4c2aff5d7d3a

# XZ Protocol v0.23 -- Carry-2 Audit Dispatch

**Seat:** Kimi K3 (Moonshot), carry-2
**Model constraint:** Execute this audit within Kimi K3. If this session is running on a different model, state that in S-0 and cease operations. Disclose the execution surface in S-0.
**Token discipline:** Pareto-optimal. Every sentence reports a finding, presents evidence, or advances analysis.

## CRITICAL: File setup before execution

The uploaded files have `.txt` appended to their extensions (e.g. `build.py.txt`, `HISTORY.sha256.txt`) because the upload system rejects `.py` and `.sha256` formats. **Before any execution, restore the original filenames.** Run `SETUP_RENAME.txt` as a bash script, or manually:

```bash
mkdir -p xz_audit && cd xz_audit
for f in ../*.py.txt; do base=$(basename "$f" .txt); cp "$f" "./$base"; done
cp ../xz_protocol_trust_roots_PUBLIC.json.txt ./xz_protocol_trust_roots_PUBLIC.json
cp ../HISTORY.sha256.txt ./HISTORY.sha256
cp ../PACKET_SHA256SUMS.txt ./PACKET_SHA256SUMS
cp ../xz_protocol_v0_23.md ./
cp ../xz_protocol_v0_23.pdf ./
```

Then execute all commands from inside `xz_audit/`.

## Standing

**Carrying seat.** Your verdict counts toward FB-7b. A HALT blocks freeze and requires a new version. CONDITIONAL PASS and CARRY-CLEAN are non-HALT. You are non-producer family. Your findings discharge part of the carry.

## What you received

The canonical normative packet (16 manifest members + PDF) plus standing orders. **That is all.** No expected values, no prior reports, no defect-class list, no adjudication. A matching value from you evidences execution.

## Execution

1. `sha256sum -c PACKET_SHA256SUMS` -- rc=0 expected. Stop if it fails.
2. `python3 build.py` -- report rc and output summary.
3. `python3 -m pytest test_xz_protocol_kernel.py test_xz_protocol_condition_a.py test_xz_protocol_source_frame.py test_xz_protocol_control_graph.py test_xz_protocol_adversarial.py xz_protocol_phase_a_tests.py -q` -- report count and rc.
4. Digest every normative file independently. Compare to PACKET_SHA256SUMS and protocol body.

Report in a compact table.

## Deliverables

**A.** Claim provenance ledger (COMPUTED / EXTERNAL / ASSERTED + fraction -- this fraction is the round's headline number).
**B.** Five probes minimum (mutation-landed hash delta, rc, FAIL verbatim, benign control). Derive probes from the invariant in the standing orders: the defect sits at the boundary between what passes through a tool and what passes through recollection.
**C.** Two novel-class probes.
**D.** Boundary report (1 paragraph).
**E.** Hedge audit -- for every CLOSED IN PART, DISCLOSED, or NOTED: is the downgrade correct, is the stated reason true?
**F.** S-1 preregistration (freeze before Section 27).
**G.** D-7 (4 yes/no lines).

## Report structure

```
## 0. State declaration (S-0)
## 1. S-1 preregistration
## 2. Byte verification table
## 3. Claim provenance ledger
## 4. Probes
## 5. Findings
## 6. Boundary report
## 7. D-7 process health
## 8. Verdict (with standing and carry consequence restated)
```

Open with S-0. No extra sections.

## Severity vocabulary

CRITICAL -- identity value or decision path is false.
HIGH -- factual claim is false or a control is absent/decorative.
MEDIUM -- claim is misleading, incomplete, or a hedge is wrong.
LOW -- process, labelling, or convention defect.
INFORMATIONAL -- boundary statement, structural observation.

*Dispatch from Claude Opus 4.6 (producer, fresh instance). Author: Bilal Syed Arfeen.*

---

# Bismillah ir-Rahman ir-Rahim
