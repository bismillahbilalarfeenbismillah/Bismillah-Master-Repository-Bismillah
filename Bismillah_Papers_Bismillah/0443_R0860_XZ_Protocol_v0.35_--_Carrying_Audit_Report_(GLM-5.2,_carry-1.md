# Bismillah ir-Rahman ir-Rahim

# R0860 -- XZ Protocol v0.35 -- Carrying Audit Report (GLM-5.2, carry-1B, continuous, fourth carry)

**Chronological Index:** 443 of 995  
**Date:** 2026-08-01  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** REPORT_GLM_1B_v035.md  
**Source Format:** md  
**SHA-256:** `4ed6b1f83968c7e9d6cf937b1a7014fa3264a0abe5645cc26121db23182a3ad3`  

---

## R0860 · XZ Protocol v0.35 -- Carrying Audit Report (GLM-5.2, carry-1B, continuous, fourth carry)

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: REPORT_GLM_1B_v035.md
- source_format: md
- text_sha256: 4ed6b1f83968c7e9d6cf937b1a7014fa3264a0abe5645cc26121db23182a3ad3

# XZ Protocol v0.35 -- Carrying Audit Report (GLM-5.2, carry-1B, continuous, fourth carry)

## S-0. State declaration

I hold FOUR packages: v0.30 (at `/home/user/workspace/dispatch/`, protocol SHA-256 `10e9c7f4...` is the v0.35 digest; the v0.30 protocol file `xz_protocol_v0_30.md` has a different digest), v0.31 (at `/home/user/workspace/dispatch_v31/`), v0.33 (at `/home/user/workspace/dispatch_v33/`), and v0.35 (at `/home/user/workspace/dispatch_v35/`, current). The v0.30 package includes my prior report (`REPORT_GLM_B_v030.md`, carry-2b seat), the v0.31 package includes my prior report (`REPORT_GLM_1B_v031.md`, carry-1b seat), and the v0.33 package includes my prior report (`REPORT_GLM_1B_v033.md`, carry-1b seat, third carry). I am NOT a fresh instance — this is my FOURTH continuous carry for this seat. I held v0.30 bytes in round 2 (v0.31 audit), v0.30+v0.31 bytes in round 3 (v0.33 audit), and now hold v0.30, v0.31, v0.33, and v0.35 bytes in round 4.

**v0.32 gap.** I do NOT hold v0.32 bytes. The dispatch jumped from v0.31 to v0.33. I cannot verify v0.32 intermediate state. The v0.32 entry exists in v0.35's Section 27 as a sealed historical entry (ENTRY_v0.32 seal `d555d260...2f1c`), verified by build [9b], but I cannot verify this seal matches what v0.32's own HISTORY.sha256 recorded.

**v0.34 gap.** I do NOT hold v0.34 bytes. The dispatch jumped from v0.33 to v0.35. I cannot verify v0.34 intermediate state. The v0.34 entry exists in v0.35's Section 27 as a sealed historical entry (ENTRY_v0.34 seal `42d1e5bf...e7d7`), verified by build [9b], but I cannot verify this seal matches what v0.34's own HISTORY.sha256 recorded. This is the second gap in my carry chain.

I can execute code: `sha256sum`, `python3 build.py`, `pytest`, and a custom probe harness all ran in a sandboxed workspace. This report is EXECUTING, not NON-EXECUTING.

Family relative to producer: GLM-5.2 (Zhipu/Z.ai) is non-producer family; the producer chain is Claude-family (Opus 4.6/4.8/5) per the amendment record. Carry consequence: my findings carry full weight, my HALT binds and freezes outright, and this verdict counts toward the FB-7b two-family carry requirement.

Context age: this is the first turn of this session. Nothing rests on a self-model of prior action — every claim was produced by a tool call in this session.

**Orchestration disclosure.** A non-GLM orchestration layer extracted the v0.35 zip, listed directory contents, confirmed prior version files remain in the workspace, and launched me. It performed no audit analysis, ran no audit commands, and contributed no findings. I (GLM-5.2) am the sole auditor; all analysis, execution, probes, and the verdict below are mine alone. I am the fourth continuous instance for this carry seat; I hold v0.30, v0.31, and v0.33 bytes; I do NOT hold v0.32 or v0.34 bytes.

---

## Execution steps (rc and output)

**Step 1.** `cd /home/user/workspace/dispatch_v35 && sha256sum -c PACKET_SHA256SUMS`
- **rc=0.** All 16 files OK.

**Step 2.** `cd /home/user/workspace/dispatch_v35 && python3 build.py`
- **rc=0.** BUILD PASSED: all checks GREEN. Key outputs: 186 tests, 35 entries, manifest digest `8f7b9679...c69a`, [9c] reports COMPUTED: 0, EXTERNAL: 1, ASSERTED: 13, ASSERTED fraction 13/14 (92.9%). Coverage 26.3%.

**Step 3.** `cd /home/user/workspace/dispatch_v35 && python3 -m pytest test_xz_protocol_kernel.py test_xz_protocol_condition_a.py test_xz_protocol_source_frame.py test_xz_protocol_control_graph.py test_xz_protocol_adversarial.py xz_protocol_phase_a_tests.py`
- **rc=0.** 186 passed in 6.06s.

**Step 4.** Independent digest recomputation of all 16 normative files via standalone `sha256sum` — all match PACKET_SHA256SUMS. Manifest digest independently recomputed: `8f7b9679c59611863fbea45e9d0e3522db69472c5cba5666482ec5900c00c69a` — matches trust roots. PRIOR_HISTORY independently re-derived via build.py's recursive algorithm: `c1924dcca1d1f678ba3054fdc58b44a51f67e631e3071c2ccf2b753848df1ae7` — matches shipped value.

---

## S-1. Preregistration (frozen before reading the v0.35 amendment entry narrative)

1. **Boundary prediction.** The v0.35 changes are status-change and finding-disposition text only (v0.32-v0.35 per the status line). Zero gate additions expected. The outermost uncomputed layer remains the FROZEN token and all prose claims about seat verdicts, correction accuracy, and HALT clearance. The boundary will not have moved from v0.33.
2. **Defect prediction.** The v0.35 entry will reframe HALT clearance (producer cannot clear HALTs; HALTing seats clear themselves). This reframing will be ASSERTED — no gate checks whether clearance is "pending" or "achieved." The EXTERNAL count correction will be real on v0.35 bytes (count drops to 1 because [9c] scans only the current entry) but the body's count claim will not be gated.
3. **Falsification plan.** (a) Mutate "Status: FROZEN" to "Status: WITHDRAWN" in the v0.35 entry, regenerate HISTORY.sha256 and PACKET_SHA256SUMS, run build — if it passes, FROZEN is not enforced. (b) Mutate "EXTERNAL count: 1" to "EXTERNAL count: 3", regenerate all surfaces, run build — if it passes, the count claim is not gated. (c) Mutate "clearance pending" to "clearance achieved", regenerate all surfaces, run build — if it passes, HALT clearance status is not gated.

**Outcome:**
1. **HELD.** Cross-version code diff (v0.33→v0.35) shows only version stamps changed — zero gate additions. Boundary at same location.
2. **HELD.** Novel Probe 1 confirmed: "EXTERNAL count: 1" → "EXTERNAL count: 3" passes after full forger regeneration (rc=0). Novel Probe 2 confirmed: "clearance pending" → "clearance achieved" passes (rc=0). Novel Probe 3 confirmed: "Status: FROZEN" → "Status: WITHDRAWN" passes (rc=0).
3. **HELD.** All three falsification commands executed and produced the predicted results.

The carry brief named the delta (EXTERNAL count inflation correction, HALT clearance reframing, ten advisory findings), which is mild leakage — it narrowed the defect prediction. However, expected values were withheld and specific mutations were not suggested.

---

## Deliverable C / S-2. Claim provenance ledger (v0.35 amendment entry)

Entry text: lines 1094-1106 of `xz_protocol_v0_35.md` (verified by grep, re-extracted in S-7).

| # | Claim | Provenance | Evidence |
|---|---|---|---|
| 1 | "Ten Opus 5 advisory seats (A through J; nine continuous, one fresh) audited v0.34" | ASSERTED | No advisory seat reports ship; no gate verifies seat count or family. |
| 2 | "All ten returned HALT (advisory, non-binding, correctly stating standing)" | ASSERTED | No reports ship; verdicts unverifiable from bytes. |
| 3 | "Zero binding HALTs" | ASSERTED | Same — no report ships to confirm this. |
| 4 | "The advisory arc identified one Class A finding (EXTERNAL count inflation)" | ASSERTED | No gate verifies convergence or finding identification. |
| 5 | "confirmed the trajectory analysis (defect-class convergence at Class C/D since v0.26)" | ASSERTED | No gate checks trajectory analysis. |
| 6 | "All ten findings are dispositioned below" | ASSERTED | No gate checks disposition completeness. |
| 7 | Correction (z): "v0.34 entry's register item (3) states 'The build output shows EXTERNAL: 2'" | ASSERTED | I can verify the v0.34 entry text (sealed in v0.35 Section 27, line 1090) contains this quote. But I cannot verify v0.34's actual build output without v0.34 bytes. |
| 8 | "The build output does show EXTERNAL: 2" | ASSERTED | I cannot run build.py on v0.34 bytes (not held). I can reason: the v0.34 entry has 2 [EXTERNAL: tags (1 backtick-quoted in register item 3, 1 genuine in closing paragraph), so [9c] would count 2. But the claim about v0.34's build output is not independently verified. |
| 9 | "one of those two counts comes from the quoted false-EXTERNAL tag in correction (u) (the v0.33 entry)" | ASSERTED | I can verify the v0.34 entry's register item (3) contains a backtick-quoted `[EXTERNAL: ...]`. But the claim that it "comes from correction (u)" is a semantic attribution — [9c] counts the tag in the v0.34 entry's text, not in the v0.33 entry. |
| 10 | "[9c] counts as an active tag when the v0.33 entry is the current entry" | ASSERTED | Verified from my v0.33 report: [9c] on v0.33 reported EXTERNAL: 2 (1 genuine + 1 quoted). But the claim about [9c]'s behavior is an observation, not a gate-checked fact. |
| 11 | "the closing paragraph's 'EXTERNAL count: 2' attributes both counts to Zenodo deposits when one is the quoted tag" | ASSERTED | I can verify the v0.34 closing paragraph (line 1092) says "EXTERNAL count: 2 (BSSG v0.1..., SHVVP v0.8...) [EXTERNAL: Zenodo deposits...]". The attribution claim is semantically correct but not gate-checked. |
| 12 | "This is Class A by Section 22.3: a sealed claim is false on the shipped bytes" | ASSERTED | The classification depends on the v0.34 count being wrong, which requires v0.34 bytes. No gate checks Section 22.3 classifications. |
| 13 | "Correction (u) is in the v0.33 entry and is immutable; the quoted tag cannot be removed" | ASSERTED | I can verify the v0.33 entry contains the tag and the seal system prevents modification. But immutability is a design property, not a gate-checked fact about this specific tag. |
| 14 | "The genuine EXTERNAL count on v0.35 bytes (which does not include the v0.33 entry in its current-entry scan) is 1" | COMPUTED | Gate [9c] scans the v0.35 entry and reports EXTERNAL: 1. Independently verified by grep: the v0.35 entry has 1 [EXTERNAL: tag. The count is derived by the gate's regex. |
| 15 | "v0.34 text is preserved under immutability" | ASSERTED | The v0.34 entry is sealed in v0.35's Section 27 (ENTRY_v0.34 seal matches bytes per [9b]). But I cannot verify the seal matches v0.34's own HISTORY.sha256 (v0.34 bytes not held). |
| 16 | Correction (aa): "v0.34 corrections (x) and (y) state that the clearance conditions for the two v0.33 binding HALTs are 'met'" | ASSERTED | I can verify the v0.34 entry (line 1084, 1086) contains these claims. But the HALTs themselves are ASSERTED (no reports ship). |
| 17 | "the producer cannot clear a binding HALT on behalf of the seat that issued it" | ASSERTED | Governance principle. No gate checks who can clear HALTs. Novel Probe 2 confirmed: changing "clearance pending" to "clearance achieved" passes the build. |
| 18 | "Clearance is pending the HALTing seats' own verification on dispatched bytes" | ASSERTED | Novel Probe 2 confirmed: this language is not gated. A forger can change "pending" to "achieved" and pass the build. |
| 19 | Register (1): "F-OP34F-01 et al. HIGH CLOSED via correction (z): EXTERNAL count inflation fixed" | ASSERTED | Self-tagged [ASSERTED]. The EXTERNAL count is 1 on v0.35 bytes (COMPUTED, row 14), but the CLOSED disposition depends on the v0.34 count being wrong (requires v0.34 bytes). |
| 20 | "Correction (u) rewritten to avoid reproducing the tag token" | ASSERTED | Misleadingly worded: correction (u) is in the immutable v0.33 entry and was NOT rewritten (verified: v0.33 entry text is identical in v0.33 and v0.35 protocols). The v0.35 entry's correction (z) avoids reproducing the tag token. The register item should say "the v0.35 entry avoids reproducing the tag token" not "Correction (u) rewritten." |
| 21 | "Genuine EXTERNAL count on v0.35 bytes: 1" | COMPUTED | Same as row 14, restated in register. [9c] reports EXTERNAL: 1; independently verified by grep. |
| 22 | Register (2): "F-OP34-02 et al. HIGH NOTED: two carrying seats HALTed on v0.33" | ASSERTED | No reports ship; the v0.34 entry describes the HALTs but I cannot verify they occurred. |
| 23 | "the entry states 'six non-HALT' while citing 'two HALT'" | ASSERTED | I can verify the v0.34 entry says this. But the factual accuracy of the HALTs is unverified. |
| 24 | "Both statements are true of different subsets (six CONDITIONAL PASS, two HALT, eight total)" | ASSERTED | Depends on unshipped reports. |
| 25 | "The freeze argument runs on non-HALT from carrying seats; Section 22 item 7 blocks on HALT" | ASSERTED | I can verify Section 22 item 7 text (line 700). The interpretation is a governance claim. |
| 26 | "The two HALTs are dispositioned in v0.34 corrections (x)/(y); clearance is pending per correction (aa)" | ASSERTED | Governance narrative. Novel Probe 2 confirmed "clearance pending" is not gated. |
| 27 | Register (3): "F-OP34C899-01 et al. HIGH NOTED: correction (x) clears a HALT on bytes the HALTing seat has not seen" | ASSERTED | No gate checks this; the finding describes a process issue. |
| 28 | "Addressed by correction (aa): clearance is pending, not claimed" | ASSERTED | Governance narrative. |
| 29 | Register (4): "F-OP34E-05 et al. MEDIUM NOTED: Section 22.3 supplies the taxonomy; its addition post-carry is a substantive body change" | ASSERTED | I can verify Section 22.3 exists (line 706). The "substantive body change" classification is a governance judgment. |
| 30 | "The carry's scope is the protocol and decision code; 22.3 is a governance annotation that does not alter any executable artifact" | ASSERTED | Governance claim. Cross-version code diff confirms zero functional code changes, but the scope claim itself is not gated. |
| 31 | Register (5): "F-OP34F-02 HIGH NOTED: the v0.19 entry contains a historical EXTERNAL tag that [9c] does not count" | ASSERTED | I can verify [9c] scans only the current entry (by reading build.py [9c] code, lines 346-351). The v0.19 tag claim requires checking the v0.19 entry. |
| 32 | "No action needed" | ASSERTED | Governance narrative. |
| 33 | Register (6): "F-OP34-04 MEDIUM NOTED: FROZEN token can be rewritten to WITHDRAWN under a green build" | ASSERTED | Independently confirmed by Novel Probe 3: "Status: FROZEN" → "Status: WITHDRAWN" passes after full forger regeneration (rc=0). |
| 34 | "Subsumed by 'no gate checks FROZEN status token' standing disclosure" | ASSERTED | I can verify this disclosure exists in the v0.35 entry's standing boundaries list. |
| 35 | Register (7): "F-OP34J-01 MEDIUM NOTED: Seat J reported packet-attachment failure. Platform issue" | ASSERTED | No report ships. |
| 36 | "Body edit: none (historical entries immutable; EXTERNAL inflation disclosed as standing boundary)" | ASSERTED | Governance narrative. I can verify no body edits by cross-version diff (v0.33→v0.35 body text changes are limited to version stamps and the new v0.34/v0.35 entries in Section 27). |
| 37 | "All 12 code files and trust roots stamped v0.35" | COMPUTED | Gate [2]: version-stamp check passes on all 12 code files + trust roots. Independently confirmed by cross-version diff (all code files differ from v0.33 only in version stamps). |
| 38 | "Section 25 digests recomputed from v0.35 bytes" | COMPUTED | Gate [3a]: FB-row locus assertions pass. Independently confirmed by cross-version diff (Section 25 digests updated to v0.35 values). |
| 39 | "Normative manifest digest (body-copy, gated by [3]): 8f7b9679...c69a" | COMPUTED | Gate [3]: independently recomputed `8f7b9679c59611863fbea45e9d0e3522db69472c5cba5666482ec5900c00c69a` — matches exactly. |
| 40 | "Six suites, 186 tests, all GREEN (gated by [5] and [8])" | COMPUTED | Gate [5]/[8]: independently ran pytest, 186 passed, rc=0. AST-derived count also 186. |
| 41 | "The preceding two values are ASSERTED at this entry-copy locus; their body-copy equivalents are COMPUTED" | ASSERTED | Correct meta-claim: no check scans entry text for these values, only body copy. Verified by reading build.py [3] and [5]. |
| 42 | "Status: FROZEN" | ASSERTED | Novel Probe 3 confirmed: no gate checks the FROZEN status token. Changing FROZEN to WITHDRAWN with full forger regeneration passes the build (rc=0). |
| 43 | "FB-7b RESOLVED" | ASSERTED | No gate checks FB-7b resolution. The resolution rests on unshipped seat reports (rows 1-6, 22-24) and two pending binding HALTs (rows 16-18, 26). |
| 44 | "EXTERNAL count: 1 (Zenodo deposits, DOIs resolve to bytes the producer does not control)" | ASSERTED | Novel Probe 1 confirmed: changing "EXTERNAL count: 1" to "EXTERNAL count: 3" passes the build after full forger regeneration (rc=0). No gate checks the body's count against [9c]'s actual count. [9c] does report EXTERNAL: 1 (the count itself is computed by the regex), but the body's restatement of that count is not gated. |
| 45 | "[EXTERNAL: Zenodo deposits doi:10.5281/zenodo.21713180 and doi:10.5281/zenodo.21583202]" | ASSERTED | No gate resolves DOIs or verifies Zenodo content. [9c]'s external_refs regex (line 372) only matches file extensions (.md, .py, .json, .pdf, .txt), not DOIs. The tag is correctly classified as EXTERNAL in intent (producer does not control Zenodo bytes), but no gate verifies it. |
| 46 | "Disclosed standing boundaries: [list of 17 items]" | ASSERTED | Spot-checked: FROZEN token unenforcement confirmed (Novel Probe 3); [9c] quoted-tag inflation confirmed (by reading); [9c] DOI-resolution blindspot confirmed (by reading code). No gate covers the boundary list as a set. |
| 47 | "Two v0.33 binding HALTs: disposition evidence recorded in v0.34 corrections (x)/(y); clearance pending HALTing seats' own verification on dispatched bytes" | ASSERTED | Novel Probe 2 confirmed: "clearance pending" language is not gated. The HALTing seats (GLM-5.2 carry-1C and Kimi K3 carry-1A) have not verified v0.35 bytes. |
| 48 | "PRIOR_HISTORY c1924dcca1d1f678...1ae7" | COMPUTED | Gate [9b]: build.py recursively re-derives this value; independently confirmed — matches. |
| 49 | "All ten findings are dispositioned below [ASSERTED]" | ASSERTED | Self-tagged [ASSERTED]. No gate checks disposition completeness. |

**Counts:** COMPUTED = 7, EXTERNAL = 0, ASSERTED = 42. Total factual claims = 49.
**ASSERTED fraction (claim-level): 42/49 = 85.7%.**
**ASSERTED fraction (build.py tag-level, gate [9c]): 13/14 = 92.9%.**

**Comparison to prior rounds:**

| Round | Claim-level ASSERTED | Tag-level ASSERTED | EXTERNAL (genuine) | Total claims |
|---|---|---|---|---|
| v0.30 | 66.7% (16/24) | 91.7% (11/12) | 0 | 24 |
| v0.31 | 75.6% (31/41) | 91.3% (21/23) | 3 | 41 |
| v0.33 | 83.3% (30/36) | 90.9% (20/22) | 0 | 36 |
| v0.35 | 85.7% (42/49) | 92.9% (13/14) | 0 | 49 |

The claim-level ASSERTED fraction rose for the fourth consecutive round (66.7% → 75.6% → 83.3% → 85.7%). The boundary has not moved — the rise is driven by the entry containing proportionally more untagged narrative claims about advisory seat verdicts, HALT clearance, and correction accuracy that no gate verifies. The tag-level fraction also rose (90.9% → 92.9%), and the total tagged claims dropped from 22 to 14 — the v0.35 entry has fewer tagged claims than the v0.33 entry, concentrating the ASSERTED share.

The tag-level 92.9% undercounts the claim-level 85.7% for the same structural reason as prior rounds (F-OP20-03 class): [9c] measures tagged-claim ASSERTED share, not entry ASSERTED share. The entry has 14 tagged claims but 49 total factual claims; the 35 untagged narrative claims are all ASSERTED by default.

---

## Deliverable D. Five mutation probes

All probes executed in isolated copies under `/home/user/workspace/probe_v35_work`. Adversary modeled: **careless producer** for Probes 1, 3, 4, 5 (wrong/stale values without manifest update); **self-consistent forger** for Novel Probes 1, 2, 3 and the discrimination control (mutate and re-derive every dependent surface including HISTORY.sha256 and PACKET_SHA256SUMS).

### Probe 1 -- Manifest digest gate [3]
1. **Mutation-landed:** `xz_protocol_kernel.py` before=`0d057e36...` after differs (appended comment suffix). Protocol file hash unchanged (mutation was to code file, not protocol). Assert they differ: True (for code file).
2. **Discrimination control:** the mutation (appending a comment to a code file) is a known-bad change with no corresponding manifest-digest update.
3. **Benign control:** clean run returns BUILD PASSED, rc=0.
4. **Reproduction:** `python3 probe_harness_v35.py` (Probe 1). Output: `FAIL: Trust roots manifest_digest matches: 4dbc9c8e...`; `BUILD FAILED: 4 error(s)`. Gate fires correctly.

### Probe 2 -- History seal gate [9b]
1. **Mutation-landed:** `xz_protocol_v0_35.md` before=`10e9c7f4...` after=`43671d68...` (differ: True). Mutation: added double space to v0.15 entry header ("- **v0.15 (2026-08-01):" → "- **v0.15  (2026-08-01):").
2. **Discrimination control:** mutating a historical entry is the exact class of past defects (v0.4, v0.9, v0.11, v0.16, v0.17 in-place mutations).
3. **Benign control:** clean run passes.
4. **Reproduction:** `python3 -c "..."` (Probe 2 fixed). Output: `FAIL: HISTORY seal ENTRY_v0.15 matches bytes`; `FAIL: FULL_SECTION_27 seal matches`; `FAIL: PRIOR_HISTORY matches derivation`; `BUILD FAILED: 4 error(s)`. Gate fires correctly.

### Probe 3 -- Version-prose gate [2b]
1. **Mutation-landed:** `xz_protocol_v0_35.md` before=`10e9c7f4...` after=`e4b23769...` (differ: True). Changed "This document is v0.35" to "This document is v0.36".
2. **Discrimination control:** a stale/incorrect version string is a recorded historical defect class.
3. **Benign control:** clean run passes.
4. **Reproduction:** `python3 probe_harness_v35.py` (Probe 3). Output: `FAIL: 'This document is v0.36' matches v0.35`; `BUILD FAILED: 2 error(s)`. Gate fires correctly.

### Probe 4 -- [9d] ordinal-recurrence gate
1. **Mutation-landed:** `xz_protocol_v0_35.md` before=`10e9c7f4...` after=`4db58732...` (differ: True). Injected "This fourth round recurring a fourth time" into the v0.35 entry.
2. **Discrimination control:** ordinal-after-target pattern is the exact class the v0.31 bidirectionalization was designed to catch (F-v30-02).
3. **Benign control:** clean run passes.
4. **Reproduction:** `python3 probe_harness_v35.py` (Probe 4). Output: `FAIL: No ordinal word adjacent to 'recurrence'/'round' in v0.35 entry (found 2)`; `BUILD FAILED: 4 error(s)`. Gate fires correctly.

### Probe 5 -- Test count gate [5]
1. **Mutation-landed:** `xz_protocol_v0_35.md` before=`10e9c7f4...` after=`fd97f5a4...` (differ: True). Replaced all 2 occurrences of "186" in body with "185".
2. **Discrimination control:** a stale test count is a historically recorded Axiom-3 recurrence class.
3. **Benign control:** clean run passes.
4. **Reproduction:** `python3 probe_harness_v35_v2.py` (Probe 5). Output: `FAIL: Test count 186 in body`; `BUILD FAILED: 4 error(s)`. Gate fires correctly.

### Discrimination control (standalone)
1. **Mutation-landed:** `test_xz_protocol_kernel.py` before=`affcae92...` after=`2b7ac840...` (differ: True). Flipped `assert r.decision == KernelDecision.ALLOW` to `DENY_FALSE`.
2. **Result:** `BUILD FAILED: 5 error(s)` — manifest digest mismatch, body digest stale, unresolvable hex, test failure, collected count mismatch. Build discriminates a real semantic break.
3. **Benign control:** unmodified bytes return BUILD PASSED, rc=0.
4. **Reproduction:** `python3 probe_harness_v35.py` (Discrimination control section).

**Void probes:** none this round. All five probes landed on first attempt (Probe 2 required a format fix after the initial attempt's replacement string didn't match the v0.15 entry header).

---

## Deliverable D (cont'd). Two novel-class probes

### Novel Probe 1 -- "EXTERNAL count claim unenforcement" (NEW CLASS)

The v0.35 entry's closing paragraph states "EXTERNAL count: 1" (line 1106). Gate [9c] independently computes the EXTERNAL count (1) by regex, but no gate checks that the body's stated count matches [9c]'s actual count. I changed "EXTERNAL count: 1" to "EXTERNAL count: 3" in the v0.35 entry, regenerated HISTORY.sha256 (including ENTRY_v0.35 seal, FULL_SECTION_27, and PRIOR_HISTORY via build.py's recursive derivation) and PACKET_SHA256SUMS (full self-consistent forger), and reran build.py.

1. **Mutation-landed:** `xz_protocol_v0_35.md` before=`10e9c7f4...` after=`1161ddc6...` (differ: True).
2. **Discrimination control:** the same copy unmutating is the benign baseline (BUILD PASSED).
3. **Benign control:** clean run passes (above).
4. **Reproduction:** `python3 probe_harness_v35_v2.py` (Novel Probe 1). Output: `BUILD PASSED: all checks GREEN`, rc=0. [9c] output: `COMPUTED: 0, EXTERNAL: 1, ASSERTED: 13` — [9c] still reports 1, but the body says 3, and no gate catches the mismatch.

**Finding:** The EXTERNAL count claim is NOT enforced by any gate. Changing "EXTERNAL count: 1" to "EXTERNAL count: 3" passes the build after full forger regeneration. This is a NEW CLASS: no prior probe in this program's corpus has tested whether a specific count claim in the entry prose is verified against the gate's actual computation. It is distinct from the v0.33 FROZEN-token probe (which tested a status token) and the v0.33 Section 22.3 probe (which tested body content) — this probe tests the specific gap between what a gate computes and what the entry claims the gate computed.

### Novel Probe 2 -- "HALT clearance status unenforcement" (NEW CLASS)

The v0.35 correction (aa) reframes HALT clearance: "clearance is pending the HALTing seats' own verification on dispatched bytes" (line 1100). This is the central governance claim of the v0.35 entry. I changed "clearance is pending" to "clearance is achieved" in correction (aa) and in the closing paragraph, regenerated HISTORY.sha256 and PACKET_SHA256SUMS (full self-consistent forger), and reran build.py.

1. **Mutation-landed:** `xz_protocol_v0_35.md` before=`10e9c7f4...` after=`01557c75...` (differ: True).
2. **Discrimination control:** the same copy unmutating is the benign baseline (BUILD PASSED).
3. **Benign control:** clean run passes.
4. **Reproduction:** `python3 probe_harness_v35_v2.py` (Novel Probe 2). Output: `BUILD PASSED: all checks GREEN`, rc=0.

**Finding:** The HALT clearance status language is NOT enforced by any gate. A forger can change "clearance pending" to "clearance achieved" and pass the build. This is a NEW CLASS: no prior probe has tested whether the HALT clearance reframing's specific language is gated. It is distinct from the FROZEN-token probe because it targets a process-status claim (clearance state) rather than a protocol-status claim (freeze state). The reframing shifts the burden of clearance from the producer to the HALTing seats, but nothing enforces that the shift is correctly stated — a forger could reverse the shift and claim the producer cleared the HALTs, and the build would not catch it.

### Novel Probe 3 -- "FROZEN token enforcement" (re-tested from v0.33)

This is the same probe class as v0.33 Novel Probe 1, re-tested on v0.35 bytes with full forger regeneration (including HISTORY.sha256). Changed "Status: FROZEN" to "Status: WITHDRAWN" in the v0.35 entry closing paragraph.

1. **Mutation-landed:** `xz_protocol_v0_35.md` before=`10e9c7f4...` after=`e00cb22b...` (differ: True).
2. **Discrimination control:** benign baseline passes.
3. **Benign control:** clean run passes.
4. **Reproduction:** `python3 probe_harness_v35_v2.py` (Novel Probe 3). Output: `BUILD PASSED: all checks GREEN`, rc=0.

**Finding:** FROZEN is still NOT enforced. This is the same class as v0.33 Novel Probe 1, confirmed on v0.35 bytes with HISTORY.sha256 regeneration. The register item (6) (F-OP34-04) discloses this as "FROZEN token can be rewritten to WITHDRAWN under a green build" — the disclosure is accurate and the finding persists.

Both novel-class probes (1 and 2) are flagged as **NEW** per D-4. Neither was suggested by the dispatch. Novel Probe 3 re-tests a prior class with the added rigor of HISTORY.sha256 regeneration (the v0.33 probe only regenerated PACKET_SHA256SUMS).

---

## Deliverable E. Self-score prior findings against v0.35 bytes

### v0.30 findings (carry-2b seat, REPORT_GLM_B_v030.md):

1. **"Unshipped carrying-seat reports" (FB-7b claim rests on zero shipped evidence)** -- **STILL OPEN.** No report files ship in v0.35 (`find` returned only `v35_GLM_CONTINUOUS.md`). The ten Opus 5 advisory reports don't ship. The v0.34 entry provides SHA-256 digests of eleven reports (line 1080), but the reports themselves are producer-held and the digests are tagged [ASSERTED].

2. **"Unguarded semantic prose and gate_atoms blind spot" (F-GLM30B-01/02)** -- **STILL OPEN.** Novel Probe 3 confirmed: FROZEN→WITHDRAWN passes after full forger regeneration. The `gate_atoms` list is still unguarded (build.py [11] uses the same hardcoded list). Coverage unchanged at 26.3%.

3. **"FB-7b remains OPEN" (state confirmation)** -- **STILL OPEN (reopened).** v0.33 declared FB-7b RESOLVED. v0.34 had two binding HALTs from carrying seats (GLM-5.2 carry-1C, Kimi K3 carry-1A). v0.35 reframes these as "clearance pending" — meaning the HALTs are not cleared. FB-7b is marked RESOLVED in the body, but two binding HALTs are pending clearance, and the HALTing seats have not verified v0.35 bytes. The state is internally consistent (the body says RESOLVED) but the underlying evidence gap widened.

4. **"Claim-level ASSERTED fraction differs from tag-level"** -- **STILL OPEN.** The discrepancy persists: tag-level 92.9% vs claim-level 85.7%. No gate counts untagged claims. The claim-level fraction continues to rise (66.7% → 75.6% → 83.3% → 85.7%).

5. **"Self-consistent forgery blind spot"** -- **STILL OPEN.** Disclosed as F-OP34-04 (register item 6). Novel Probes 1, 2, 3 all confirmed: mutations with full forger regeneration (including HISTORY.sha256) pass the build. The blind spot remains structural. My held v0.30, v0.31, and v0.33 HISTORY.sha256 files provide the cross-version anchor for v0.1-v0.33 seals, but the v0.32 and v0.34 gaps mean I cannot anchor those entries.

6. **"Next seat should be given prior bytes" (S-6 recommendation)** -- **CLOSED.** I was given v0.30, v0.31, and v0.33 bytes and performed four-version cross-version comparison (Deliverable F). The recommendation was addressed by the carry-continuity structure.

### v0.31 findings (carry-1b seat, REPORT_GLM_1B_v031.md):

7. **"Unshipped carrying-seat reports" (4 of 5 seats)** -- **STILL OPEN.** Same as v0.30 finding 1. No reports ship in v0.35.

8. **"Unguarded semantic prose and gate_atoms blind spot"** -- **STILL OPEN.** Same as v0.30 finding 2. Novel Probes 1, 2, 3 independently confirm.

9. **"ASSERTED fraction rising without boundary movement"** -- **CONFIRMED (worsened).** 66.7% → 75.6% → 83.3% → 85.7%. Four consecutive rounds of rising ASSERTED fraction without boundary movement. This is now a four-round trend.

10. **"Section 2.2 consequence 4 prohibition unenforced" (Novel Probe 1, v0.31)** -- **STILL OPEN.** No gate scans body prose for prohibition compliance.

11. **"Cross-version seal-laundering blind spot" (F-K3B-04)** -- **PARTIALLY CLOSED.** The build's PRIOR_HISTORY derivation provides protection for v0.1-v0.33 seals (confirmed: zero retroactive mutations between v0.33 and v0.35 HISTORY.sha256). The v0.32 and v0.34 gaps mean those entries cannot be externally anchored. The blind spot remains structural for v0.32+ and v0.34+.

12. **"Self-consistent forgery blind spot" (F-K3B-05)** -- **STILL OPEN.** Same as v0.30 finding 5. Disclosed as F-OP34-04. Novel Probes 1, 2, 3 all confirmed with HISTORY.sha256 regeneration.

### v0.33 findings (carry-1b seat, REPORT_GLM_1B_v033.md) -- five blocking findings:

13. **FROZEN token not enforced (v0.33 blocking finding 1)** -- **STILL OPEN.** Novel Probe 3 confirmed: FROZEN→WITHDRAWN passes after full forger regeneration (rc=0). Register item (6) (F-OP34-04) discloses this. Disclosure is accurate but disclosure is not enforcement. No gate was added to check the FROZEN token.

14. **Section 22.3 content not enforced (v0.33 blocking finding 2)** -- **STILL OPEN.** No gate reads Section 22.3 content. build.py [10] checks only one string ("gate execution is a build-time convenience") in Section 22, not Section 22.3's severity classifications. The v0.34 register item (7) (F-GPT33-02/F-GPT33-06) discloses this. No structural fix was added.

15. **Unshipped seat reports (v0.33 blocking finding 3)** -- **STILL OPEN.** No reports ship in v0.35. The ten Opus 5 advisory reports and the v0.34 eleven carrying seat reports are all producer-held. The v0.34 entry provides digests (line 1080) but the reports don't ship and the digests are [ASSERTED].

16. **ASSERTED fraction rising without boundary movement (v0.33 blocking finding 4)** -- **CONFIRMED WORSENED.** 83.3% → 85.7%. The boundary is at the same location as v0.30. Four consecutive rounds of rising ASSERTED fraction. The v0.35 changes (EXTERNAL count correction, HALT clearance reframing) are text-level edits within the unguarded prose region — none expanded the computed boundary outward.

17. **v0.32 gap (v0.33 blocking finding 5)** -- **NOT ADDRESSED.** v0.32 bytes were not provided. Now compounded by a v0.34 gap — I hold neither v0.32 nor v0.34 bytes. The v0.32 entry is sealed in v0.35's Section 27 (ENTRY_v0.32 seal `d555d260...2f1c`, verified by [9b]), and the v0.34 entry is sealed (ENTRY_v0.34 seal `42d1e5bf...e7d7`, verified by [9b]), but I cannot verify either seal matches what those versions' own HISTORY.sha256 files recorded.

**Summary:** 1 CLOSED, 1 PARTIALLY CLOSED, 8 STILL OPEN, 2 CONFIRMED (worsened), 5 STILL OPEN (v0.33 blocking). No prior blocking finding was fully addressed with a structural fix in v0.35. The FROZEN declaration persists without enforcement. The EXTERNAL count correction is real (count drops to 1) but the count claim itself is not gated (Novel Probe 1). The HALT clearance reframing is more conservative but leaves two binding HALTs pending while FROZEN is maintained (Novel Probe 2).

---

## Deliverable F. Internal consistency check

All 35 HISTORY.sha256 entry seals (ENTRY_v0.1 through ENTRY_v0.35) were independently recomputed from shipped `xz_protocol_v0_35.md` bytes via build.py [9b] and matched exactly (0 mismatches). FULL_SECTION_27 recomputed and matched. PRIOR_HISTORY (`c1924dcca1d1f678...1ae7`) independently re-derived via build.py's recursive reconstruction algorithm and matched.

**Cross-version seal diff (v0.30 → v0.31):** Lines 1-30 (ENTRY_v0.1 through ENTRY_v0.30): **IDENTICAL** — all 30 historical seals preserved unchanged. v0.31 added ENTRY_v0.31, updated FULL_SECTION_27 and PRIOR_HISTORY. Zero historical-seal divergences.

**Cross-version seal diff (v0.31 → v0.33):** Lines 1-31 (ENTRY_v0.1 through ENTRY_v0.31): **IDENTICAL** — all 31 seals preserved unchanged. v0.33 added ENTRY_v0.32 and ENTRY_v0.33, updated FULL_SECTION_27 and PRIOR_HISTORY. Zero historical-seal divergences.

**Cross-version seal diff (v0.33 → v0.35):** Lines 1-33 (ENTRY_v0.1 through ENTRY_v0.33): **IDENTICAL** — all 33 seals preserved unchanged. v0.35 added ENTRY_v0.34 (`42d1e5bf...e7d7`) and ENTRY_v0.35 (`958c1617...87c3`), updated FULL_SECTION_27 (`6883d4e9...bb12`) and PRIOR_HISTORY (`c1924dcc...1ae7`). Zero historical-seal divergences. **No retroactive mutation of any v0.1-v0.33 entry.**

This is the first four-version cross-version seal comparison in this program. The HISTORY.sha256 chain is internally consistent across v0.30, v0.31, v0.33, and v0.35 — every historical seal from v0.1 through v0.33 is byte-identical across all four versions.

**v0.34 seal presence:** ENTRY_v0.34 (`42d1e5bf...e7d7`) is present in v0.35's HISTORY.sha256 and matches the v0.34 entry text in v0.35's Section 27 (verified by build [9b]). However, I do NOT hold v0.34 bytes, so I cannot verify that this seal matches what v0.34's own HISTORY.sha256 recorded. The seal proves the v0.34 entry is unaltered since v0.35's sealing, not since v0.34's original production.

**v0.32 seal presence:** ENTRY_v0.32 (`d555d260...2f1c`) is present in both v0.33 and v0.35's HISTORY.sha256 (identical across both). It matches the v0.32 entry text in v0.35's Section 27 (verified by [9b]). But I do NOT hold v0.32 bytes, so I cannot verify it matches v0.32's own HISTORY.sha256.

**Entry text comparison across versions:** The v0.30, v0.31, and v0.33 entries are byte-identical across all versions that contain them (verified by Python text extraction and comparison). This confirms the append-only discipline is enforced by the seal system — no historical entry text was retroactively mutated.

**Cross-version code diff (v0.33 → v0.35):** All 13 code files differ ONLY in version stamps (v0.33 → v0.35). The trust_roots JSON changed the protocol name and manifest_digest. No functional code changes in any module. build.py changed only in: docstring version string, protocol filename, VERSION constant (0.33→0.35), and entry count check (33→35). **Zero gate changes.** This confirms that v0.32-v0.35 are status-change and finding-disposition versions with no substantive revision to the carried protocol or decision code — exactly what the v0.35 status line claims.

**Cross-version body diff (v0.33 → v0.35):** The body changed in: title/version/status lines, Section 0.1 (carry status paragraph extended to reference v0.32-v0.34 entries), Section 25 FB-7b row (unchanged from v0.33), and version stamps. The only substantive new body content is the extension of the carry status paragraph (line 20) to mention v0.32-v0.34 entries.

---

## Deliverable G. Boundary report

**The outermost layer the build does NOT compute is the truth-value of the FROZEN status claim, the HALT clearance status, the EXTERNAL count claim, and all prose claims about seat verdicts and correction accuracy.** Specifically: (a) whether the FROZEN token is earned — no gate checks it (Novel Probe 3: FROZEN→WITHDRAWN passes); (b) whether HALT clearance is "pending" or "achieved" — no gate checks it (Novel Probe 2: "pending"→"achieved" passes); (c) whether the EXTERNAL count claim matches [9c]'s actual count — no gate checks it (Novel Probe 1: "1"→"3" passes); (d) whether the cited advisory seat verdicts (ten Opus 5 seats, all HALT) are true — no reports ship; (e) whether corrections (z) and (aa) accurately describe v0.34's text — I don't hold v0.34 bytes; (f) whether Section 22.3's content is correct — no gate reads it (v0.33 Novel Probe 2 confirmed, still unenforced); (g) whether any body-text sentence containing neither a `gate_atoms` token nor a 64-hex digest is true — confirmed unguarded by all three novel probes.

A secondary instance: the `gate_atoms` list inside build.py [11] that defines "semantic-gate coverage" is itself unguarded (confirmed still true — same hardcoded list as v0.30/v0.31/v0.33). The measuring instrument's own scope is asserted, not computed.

**Comparison across all four rounds:**

| Round | Boundary location | Coverage | ASSERTED fraction | FROZEN enforced? |
|---|---|---|---|---|
| v0.30 | Prose claims about seat reports + gate_atoms unguarded | 25.0% | 66.7% | N/A (DRAFT CANDIDATE) |
| v0.31 | Same | 25.5% | 75.6% | N/A |
| v0.33 | FROZEN token + Section 22.3 + seat verdicts | 26.3% | 83.3% | No (Novel Probe 1) |
| v0.35 | FROZEN token + HALT clearance + EXTERNAL count claim + seat verdicts | 26.3% | 85.7% | No (Novel Probe 3) |

**The boundary did not move.** The v0.35 changes (EXTERNAL count correction, HALT clearance reframing, register disposition) are text-level edits within the unguarded prose region — none expanded the computed boundary outward. The ASSERTED fraction rose for the fourth consecutive round (66.7% → 75.6% → 83.3% → 85.7%), confirming the boundary did not move. The FROZEN declaration persists without enforcement. The HALT clearance reframing added a new unguarded surface (clearance status language) without bringing any prior surface inside the computed region.

**What would bring it inside:** (1) add a gate that checks the FROZEN token against a set of freeze conditions; (2) add a gate that checks HALT clearance status against a registry of HALTing seats and their return verdicts; (3) add a gate that checks the body's "EXTERNAL count: N" claim against [9c]'s actual count; (4) add a gate that reads Section 22.3 content and verifies severity classifications; (5) require every ASSERTED-tagged carrying-seat or advisory-seat claim to cite a shipped report file with a digest checked by [9c].

---

## Deliverable H. D-7 reflexive check

1. **Did every probe come from an enumerated list?** No. Novel Probes 1 (EXTERNAL count claim unenforcement) and 2 (HALT clearance status unenforcement) target surfaces not probed in any prior round. Novel Probe 3 re-tests the v0.33 FROZEN-token class with added HISTORY.sha256 regeneration rigor.
2. **Did the dispatch tell me where to look?** Partially. The carry brief named the EXTERNAL count correction and HALT clearance reframing, narrowing my defect prediction. However, expected values were withheld and the specific mutations were not suggested.
3. **Is the ASSERTED fraction unchanged from the prior round?** No — it changed. Claim-level: 83.3% → 85.7% (rose). Tag-level: 90.9% → 92.9% (rose). **The claim-level fraction rose for the fourth consecutive round (66.7% → 75.6% → 83.3% → 85.7%). This is the most important D-7 finding: four consecutive rounds of rising ASSERTED fraction without boundary movement means the rounds are producing findings and corrections without moving the boundary.** The EXTERNAL count correction and HALT clearance reframing are real text-level improvements, but they sit in the unguarded region — they did not bring any layer inside the computed boundary.
4. **Have recent rounds all been producer-family?** No. This is a non-producer carrying round (GLM-5.2). v0.30, v0.31, and v0.33 were also non-producer carrying. v0.34 was an eleven-seat carry (eight non-producer carrying + three GPT advisory). The v0.35 advisory round (ten Opus 5) was producer-family advisory. The carrying rounds remain non-producer. The intended corrective structure is intact.

---

## Deliverable I. S-4: Hedge audit

Downgrades present in the v0.35 entry and their audit:

- **Register (1) F-OP34F-01 et al. HIGH CLOSED via correction (z):** Downgrade correct (the EXTERNAL count was inflated on v0.34 — I can verify the v0.34 entry has 2 [EXTERNAL: tags, one of which is a backtick-quoted reference). Reason true: the v0.35 entry has 1 genuine [EXTERNAL: tag, confirmed by [9c] and grep. Scope matches. Register row present (item 1). **Correctly closed.** However, register item (1)'s claim "Correction (u) rewritten to avoid reproducing the tag token" is misleadingly worded — correction (u) is in the immutable v0.33 entry and was NOT rewritten (verified: v0.33 entry text is identical in v0.33 and v0.35 protocols). The v0.35 entry's correction (z) avoids reproducing the tag. This is a semantic imprecision, not a factual error, but it could mislead a reader into thinking an immutable entry was modified.

- **Register (2) F-OP34-02 et al. HIGH NOTED:** Downgrade correct (gate-limitation class). Reason true: two carrying seats HALTed on v0.33 (ASSERTED — no reports ship); the freeze argument runs on non-HALT from carrying seats per Section 22 item 7. Scope matches. Register row present (item 2). **Correctly noted.**

- **Register (3) F-OP34C899-01 et al. HIGH NOTED:** Downgrade correct. Reason true: correction (x) does state clearance conditions are "met" on bytes the HALTing seat has not seen (verified by reading v0.34 entry line 1084). Addressed by correction (aa): clearance is pending, not claimed. Scope matches. Register row present (item 3). **Correctly noted.** But "addressed" means the language was changed, not that the HALTs were cleared — Novel Probe 2 confirmed the clearance status language is not gated.

- **Register (4) F-OP34E-05 et al. MEDIUM NOTED:** Downgrade correct. Reason true: Section 22.3 is a substantive body addition post-carry. The carry's scope is the protocol and decision code; 22.3 is a governance annotation. Scope matches. Register row present (item 4). **Correctly noted.**

- **Register (5) F-OP34F-02 HIGH NOTED:** Downgrade correct. Reason true: [9c] scans only the current entry (verified by reading build.py [9c] code, lines 346-351). The v0.19 historical tag claim requires checking the v0.19 entry — ASSERTED. Scope matches. Register row present (item 5). **Correctly noted.**

- **Register (6) F-OP34-04 MEDIUM NOTED:** Downgrade correct. Reason true: independently confirmed by Novel Probe 3 — FROZEN→WITHDRAWN passes after full forger regeneration. Subsumed by "no gate checks FROZEN status token" standing disclosure. Scope matches. Register row present (item 6). **Correctly noted.** This is the most important NOTED item: FROZEN is the protocol's central claim, and it is entirely unenforced — now confirmed with HISTORY.sha256 regeneration (stronger than the v0.33 probe which only regenerated PACKET_SHA256SUMS).

- **Register (7) F-OP34J-01 MEDIUM NOTED:** Downgrade correct. Reason true: no report ships to verify Seat J's packet-attachment failure. Platform issue, not protocol defect. Scope matches. Register row present (item 7). **Correctly noted.**

**No hedge in this entry was found to have a false reason or a scope mismatch severe enough to constitute a defect wearing the costume of a disclosure.** All 7 register items have register rows. The one CLOSED item (1) rests on correction (z)'s description of v0.34's EXTERNAL count, which I can partially verify (the v0.34 entry has 2 tags, one quoted) but cannot fully verify (v0.34's build output requires v0.34 bytes). The NOTED items (2-7) are gate-limitation classes correctly scoped and disclosed. The most significant finding is that the HALT clearance reframing (correction (aa)) is correctly stated as "pending" — but nothing enforces that the pending state is maintained or that the HALTing seats ever return to clear it.

---

## Deliverable J. S-5: Coverage measurement

**Character level (independently recomputed, matches build.py [11]):** Total document = 234,397 chars. Body (before Section 27) = 100,790 chars (43.0%). Section 27 (ungated) = 133,607 chars (57.0%). Semantic-gate coverage (lines containing a `gate_atoms` keyword or a resolvable 64-hex digest) = 26,538 / 100,790 = **26.3%**. Ungated body = 74,252 chars (73.7%). Ungated total (body ungated + Section 27) = 207,859 chars (88.6%).

**Comparison to prior rounds:**

| Round | Total chars | Body chars | Coverage | Body % | S27 % |
|---|---|---|---|---|---|
| v0.30 | 195,144 | 98,245 | 25.0% | 50.3% | 49.7% |
| v0.31 | 204,286 | 98,885 | 25.5% | 48.4% | 51.6% |
| v0.33 | 221,361 | 100,792 | 26.3% | 45.5% | 54.5% |
| v0.35 | 234,397 | 100,790 | 26.3% | 43.0% | 57.0% |

Coverage is unchanged from v0.33 (26.3%). The body char count is nearly identical (100,792 → 100,790, a 2-char decrease). Section 27 grew by 13,036 chars (the v0.34 and v0.35 entries). The Section 27 share grew to 57.0%, meaning more than half the document is ungated beyond seal-matching. No new gate coverage was added — the boundary did not move.

Every claim in the v0.35 entry falls in the **ungated Section 27 region** by definition. The entry's COMPUTED claims (manifest digest, test count, version stamps, PRIOR_HISTORY) are COMPUTED only because they are also restated in the gated body and cross-checked there, or because [9c] counts tags.

**Packet level:** 16 members in PACKET_SHA256SUMS. All 16 carry a digest. Zero unhashed members. But this coverage is binary and says nothing about semantic correctness.

---

## Deliverable K. S-7: Self-falsification

Performed as tool executions, not re-reading:

1. **Recomputed all digests:** independent `sha256sum` of all 16 normative files — ALL MATCH (verified by `sha256sum -c PACKET_SHA256SUMS`, rc=0). Manifest digest `8f7b9679...c69a` recomputed standalone — matches. PRIOR_HISTORY `c1924dcca1d1f678...1ae7` recomputed via build.py derivation — matches. **Caught nothing new; confirms no transcription error.**

2. **Re-extracted every line number:** v0.35 entry at line 1094 (`grep -n '^- \*\*v0\.35'`). Section 0.1 at line 14. Section 22 at line 690. Section 22.3 at line 706. Section 25 at line 743. Section 27 at line 806. FB-7b row at line 756. v0.34 entry at line 1076. v0.33 entry at line 1058. Correction (z) at line 1098. Correction (aa) at line 1100. Status line at line 5. build.py [9c] at lines 344-374, [9d] at lines 376-388, [10] at lines 443-447, [11] at lines 449-469, [12] at lines 471-492. **All confirmed accurate.**

3. **Re-derived every count:** 49 total claims (recounted from entry text). 7 COMPUTED, 0 EXTERNAL (genuine), 42 ASSERTED. 42/49 = 85.7%. Tag-level: 13/14 = 92.9% (recounted via [9c] build output: 0 COMPUTED, 1 EXTERNAL, 13 ASSERTED). 186 tests (re-ran pytest). 35 amendment entries (recounted via grep). 26.3% coverage (recomputed). **All matched.**

4. **Grepped every claim about shipped reports:** `find` for report files in v0.35 directory — only `v35_GLM_CONTINUOUS.md`. Confirms ASSERTED classification of advisory-seat verdict claims (rows 1-6, 22, 35).

5. **Re-verified cross-version seal comparison:** diff of v0.33 and v0.35 HISTORY.sha256 — lines 1-33 identical, confirming 0 historical-seal divergences for v0.1-v0.33. v0.34 seal present. Entry text comparison: v0.30, v0.31, v0.33 entries byte-identical across versions. **Confirmed.**

6. **Confirmed every void probe:** none this round — all five probes landed (Probe 2 required a format fix, but the fixed version landed).

7. **Re-verified [9c] EXTERNAL count:** independently confirmed that the v0.35 entry has 1 [EXTERNAL: tag (grep on lines 1094-1106). [9c] reports EXTERNAL: 1. The v0.34 entry has 2 [EXTERNAL: tags (1 backtick-quoted in register item 3, 1 genuine in closing paragraph). The v0.33 entry has 2 [EXTERNAL: tags (1 quoted in correction (u), 1 genuine). **Confirmed the EXTERNAL count inflation correction is real on v0.35 bytes.**

**What this step caught:** the misleading wording in register item (1) — "Correction (u) rewritten to avoid reproducing the tag token" — which implies the immutable v0.33 entry was modified. On first pass I had not flagged this; re-examining the entry text during self-falsification revealed that correction (u) is in the immutable v0.33 entry and was NOT rewritten (verified by entry text comparison). The report reflects this finding (row 20 of the ledger, Deliverable I hedge audit).

---

## Deliverable L. S-9: Anti-patterns check

- **Fluency as evidence:** avoided by requiring every COMPUTED tag to cite a specific gate and by re-running rather than narrating build/pytest output. All three novel probes are backed by executable mutations with rc codes and full forger regeneration (including HISTORY.sha256), not by confident prose.
- **Checklist convergence:** the five standard probes target gates [3], [9b], [2b], [9d], [5] — derived from reading build.py's gate structure. The two novel probes target EXTERNAL count claim enforcement and HALT clearance status enforcement — surfaces named nowhere in the amendment record's probe history. Novel Probe 3 re-tests the v0.33 FROZEN-token class with added rigor.
- **Hedging as camouflage:** I did not mark anything "NOT VERIFIABLE" as a shortcut. Where I cannot verify (v0.32/v0.34 corrections), I named exactly which bytes would settle it (v0.32 and v0.34 bytes) and stated they do not ship.
- **Severity inflation:** the FROZEN-token unenforcement (Novel Probe 3) is graded as a boundary-location finding, not a CRITICAL break. The HALT clearance reframing gap (Novel Probe 2) is graded as a governance-process finding, not a byte-level error. The EXTERNAL count claim unenforcement (Novel Probe 1) is graded as a gate-scope finding. None of these are concealed defects — they are disclosed limitations.
- **Finding-count optimization:** this report privileges the boundary report (Deliverable G), the FROZEN analysis (Deliverable N), and the four-round ASSERTED fraction trend over accumulating additional small findings.

---

## Deliverable M. D-4: Adversary declaration

Declared: **self-consistent forger** for Novel Probes 1, 2, 3 (mutate body text and regenerate HISTORY.sha256 + PACKET_SHA256SUMS to match — the exact move the Section 22.2 self-consistent-forgery boundary names). This is stronger than the v0.33 novel probes, which only regenerated PACKET_SHA256SUMS. The v0.35 probes regenerate HISTORY.sha256 using build.py's own recursive derivation, making them full self-consistent forgeries. **Careless producer** for Probes 1, 3, 4, 5 (wrong/stale values without manifest update). The discrimination control models a **self-consistent forger** who mutates code and expects the build to catch the cascading failure. I did not take the **patient contributor** posture this round.

---

## Deliverable N. FROZEN analysis (required)

### Is FROZEN earned?

**FROZEN is declared but not earned by any gate.** The conditions for FROZEN are stated in Section 22 (items 1-7) and Section 25 (all FREEZE-BLOCKERs resolved). Evaluation:

- **Section 22 items 1-5** (producer self-check, schema validation, kernel tests, adversarial suite, universe rerun): items 1-4 are evidenced by shipped executable artifacts (COMPUTED). Item 5 (universe rerun) is not applicable pre-corpus. These are satisfiable.
- **Section 22 item 6** (two-family executing carry): the v0.35 entry claims six non-producer carrying seats across two families returned non-HALT on v0.31 canonical bytes. This is ASSERTED — no reports ship, no gate verifies seat execution or verdicts. The FB-7b resolution rests on the v0.31 carry round, not the v0.34 or v0.35 carry rounds.
- **Section 22 item 7** (no carrying-seat HALT): the v0.34 entry records two binding HALTs from carrying seats (GLM-5.2 carry-1C and Kimi K3 carry-1A). The v0.35 entry reframes these as "clearance pending." **Two binding HALTs are pending clearance.** The HALTing seats have not verified v0.35 bytes. FROZEN is maintained while two binding HALTs are unresolved.
- **Section 25** (all FREEZE-BLOCKERs resolved): FB-1 through FB-7a are resolved with shipped artifacts (COMPUTED). FB-7b is marked RESOLVED, but the resolution rests on ASSERTED claims (unshipped reports) and two pending binding HALTs.

**No gate checks the FROZEN status token.** Novel Probe 3 confirmed: changing "Status: FROZEN" to "Status: WITHDRAWN" in the body, with full forger regeneration (including HISTORY.sha256), passes the build (rc=0). Register item (6) (F-OP34-04) discloses this. The FROZEN declaration is an ASSERTED claim sitting in the unguarded region — exactly the boundary the invariant predicts defects at. This is now confirmed with HISTORY.sha256 regeneration, making it a stronger result than the v0.33 probe.

### Was the EXTERNAL count inflation actually corrected?

**Yes, on v0.35 bytes.** I independently verified:

- The v0.35 entry has 1 [EXTERNAL: tag (the Zenodo deposits tag in the closing paragraph, line 1106).
- [9c] reports EXTERNAL: 1 on v0.35 bytes.
- The v0.35 entry's closing paragraph says "EXTERNAL count: 1" — matches [9c].
- The v0.34 entry (sealed in v0.35 Section 27, lines 1076-1092) has 2 [EXTERNAL: tags: one backtick-quoted `` `[EXTERNAL: ...]` `` in register item (3) (a reference to the v0.33 entry's correction (u) tag) and one genuine "[EXTERNAL: Zenodo deposits...]" in the closing paragraph. [9c] would count 2 on v0.34.
- The v0.33 entry (sealed in v0.35 Section 27, lines 1058-1074) has 2 [EXTERNAL: tags: one quoted "[EXTERNAL: seat reports held by producer...]" in correction (u) and one genuine "[EXTERNAL: Zenodo deposits...]" in the closing paragraph. [9c] reported EXTERNAL: 2 on v0.33 (confirmed by my v0.33 report).

The correction is real: the v0.35 entry avoids reproducing the quoted tag, so [9c] counts only the genuine tag (1). The v0.34 count of 2 was inflated by 1 (the backtick-quoted reference in register item (3)). However, I cannot verify v0.34's actual build output (requires v0.34 bytes). The claim that the v0.34 count was inflated is ASSERTED but supported by my independent analysis of the v0.34 entry text.

**However**, the body's "EXTERNAL count: 1" claim is NOT enforced by any gate. Novel Probe 1 confirmed: changing "EXTERNAL count: 1" to "EXTERNAL count: 3" passes the build after full forger regeneration. [9c] computes the count (1) but no gate checks that the body's stated count matches [9c]'s computed count. The correction is real at the text level but the count claim remains unguarded.

### Is the HALT clearance reframing sound?

**Partially sound, with a structural gap.**

The reframing (correction (aa)) states: "the producer cannot clear a binding HALT on behalf of the seat that issued it. Clearance is pending the HALTing seats' own verification on dispatched bytes."

**Sound aspects:**
- The principle is correct: the producer should not unilaterally clear a HALT issued by another seat. Section 22 item 7 says a HALT "blocks freeze outright and requires a new version." The v0.34 corrections (x)/(y) claiming clearance conditions are "met" was the producer clearing HALTs on behalf of HALTing seats — the reframing correctly identifies this as improper.
- The reframing is more conservative than v0.34's "clearance conditions met" language. It acknowledges that clearance requires the HALTing seat's own verification.

**Structural gap:**
- FROZEN is maintained while two binding HALTs are pending clearance. Section 22 item 7 says a HALT "blocks freeze outright." The v0.34 HALTs blocked v0.34's freeze. v0.35 is the new version required by the HALTs, but v0.35 still says FROZEN while the HALTs are pending.
- The FB-7b resolution is based on the v0.31 carry round (six non-HALT), not the v0.34 carry round (six non-HALT, two HALT). The question is whether v0.34 HALTs on v0.33 bytes retroactively affect the v0.31-based FB-7b resolution. The protocol's answer is that FB-7b was resolved at v0.32 based on v0.31 bytes, and subsequent HALTs require new versions but don't retroactively un-resolve FB-7b. This is a reasonable reading but depends on interpreting Section 22 item 7 as applying per-version rather than globally.
- Novel Probe 2 confirmed: the "clearance pending" language is not gated. A forger can change "pending" to "achieved" and pass the build. The reframing adds an unguarded surface (clearance status language) without bringing any prior surface inside the computed boundary.
- The HALTing seats (GLM-5.2 carry-1C and Kimi K3 carry-1A) have not returned to verify v0.35 bytes. The reframing says clearance is "pending" — but nothing in the protocol requires the HALTing seats to ever return, and nothing prevents FROZEN from persisting indefinitely while the HALTs remain pending.

**Is it circular?** No, not exactly circular. The reframing separates concerns: the producer records disposition evidence; the HALTing seats make the clearance determination. This is not self-referential. But it creates an open-ended deferral: FROZEN is maintained while HALTs are "pending" clearance that may never come, and nothing enforces the "pending" status.

**Is the producer trying to clear HALTs that only HALTing seats can clear?** The v0.35 entry explicitly says the producer does NOT clear the HALTs — it records disposition evidence and defers clearance to the HALTing seats. This is the correct posture. But the v0.34 entry (corrections (x)/(y)) DID claim clearance conditions were "met" — that was the producer clearing HALTs, which the v0.35 reframing corrects. The correction is real but the HALTs remain pending.

---

## Deliverable O. Verdict

**Standing:** Non-producer carrying seat (GLM-5.2, Zhipu/Z.ai), carry-1B (continuous from v0.30, v0.31, v0.33). Full finding weight. This verdict **BINDS** and, if HALT, freezes the round outright. It counts toward the FB-7b two-family carry requirement.

**What this round got right:** All 35 historical seals reproduce exactly from shipped bytes. The four-version cross-version anchor check (v0.30 → v0.31 → v0.33 → v0.35) confirms zero retroactive mutations of any v0.1-v0.33 entry seal — the first four-version comparison in this program. The v0.34 seal is present and matches the v0.34 entry text. Entry text comparison confirms v0.30, v0.31, and v0.33 entries are byte-identical across all versions that contain them. All code files differ from v0.33 only in version stamps — zero functional changes, zero gate changes. `sha256sum -c` returns rc=0. `python3 build.py` returns BUILD PASSED, rc=0. All 186 tests pass. The EXTERNAL count inflation correction is real on v0.35 bytes: the entry has 1 genuine [EXTERNAL: tag (down from 2 on v0.34, where one was a backtick-quoted reference), and [9c] reports EXTERNAL: 1. The HALT clearance reframing (correction (aa)) is more conservative and more correct than v0.34's "clearance conditions met" — it correctly identifies that the producer cannot clear binding HALTs on behalf of HALTing seats. The register is self-consistent (7 items, 7 declared). The "Correction (u) rewritten" wording in register item (1) is imprecise but not a factual error (the v0.33 entry was not modified; the v0.35 entry avoids reproducing the tag).

**Verdict: CONDITIONAL PASS (binding, non-HALT).**

Blocking-if-unaddressed findings, and what clears each:

1. **FROZEN is not enforced by any gate.** Novel Probe 3 confirmed: changing "Status: FROZEN" to "Status: WITHDRAWN" passes the build after full forger regeneration including HISTORY.sha256 (rc=0). This is the fourth consecutive round where FROZEN is unenforced (v0.33 Novel Probe 1 first identified it; v0.35 Novel Probe 3 confirms with stronger forger regeneration). Register item (6) discloses this, but disclosure is not enforcement. **Clears by:** adding a gate that checks the FROZEN token against a set of freeze conditions (all FREEZE-BLOCKERs resolved, all FB-7b conjuncts verified, no pending binding HALTs, status line matches a computed state).

2. **HALT clearance status is not enforced.** Novel Probe 2 confirmed: changing "clearance pending" to "clearance achieved" passes the build after full forger regeneration (rc=0). The v0.35 reframing correctly shifts clearance burden to HALTing seats, but nothing enforces that the "pending" status is maintained, and nothing requires the HALTing seats to ever return. Two binding HALTs (GLM-5.2 carry-1C, Kimi K3 carry-1A) remain pending while FROZEN is maintained. **Clears by:** adding a gate that tracks HALTing seats and their return verdicts, or by the HALTing seats returning non-HALT on v0.35 bytes.

3. **EXTERNAL count claim is not enforced.** Novel Probe 1 confirmed: changing "EXTERNAL count: 1" to "EXTERNAL count: 3" passes the build after full forger regeneration (rc=0). [9c] computes the count (1) but no gate checks the body's stated count against [9c]'s computed count. The EXTERNAL count correction is real at the text level but the count claim remains unguarded. **Clears by:** adding a gate that checks the body's "EXTERNAL count: N" claim against [9c]'s actual count.

4. **Unshipped seat reports.** The FB-7b resolution and the ten advisory HALTs rest on zero shipped evidence. The v0.34 entry provides SHA-256 digests of eleven reports, but the reports are producer-held and the digests are tagged [ASSERTED]. **Clears by:** shipping the cited seat report files with digests in PACKET_SHA256SUMS.

5. **ASSERTED fraction rising for four consecutive rounds without boundary movement.** 66.7% → 75.6% → 83.3% → 85.7%. The boundary is at the same location as v0.30. The EXTERNAL count correction and HALT clearance reframing are text-level improvements within the unguarded region — they did not bring any layer inside the computed boundary. **Clears by:** extending [9c] to count untagged claims, or by requiring every factual claim in the entry to carry a provenance tag, or by adding gates that check the claims currently marked ASSERTED.

6. **v0.32 and v0.34 gaps.** I hold neither v0.32 nor v0.34 bytes. The v0.32 and v0.34 entries are sealed in v0.35's Section 27, but the seals prove only that the entries are unaltered since v0.35's sealing, not since their original production. Correction (z)'s description of v0.34's EXTERNAL count and correction (aa)'s description of v0.34's HALT clearance claims depend on v0.34's body text, which I cannot independently verify. **Clears by:** providing v0.32 and v0.34 bytes to the next carrying seat.

None of these are CRITICAL breaks in currently-shipped, currently-tested code. The byte-level consistency (digests, seals, tests, manifest) is intact and independently verified across four versions. The EXTERNAL count correction is real on v0.35 bytes. The HALT clearance reframing is more conservative and more correct than v0.34. The findings are boundary-location findings about what the instrument does not yet reach — specifically, that the FROZEN claim, the HALT clearance status, and the EXTERNAL count claim all sit at the boundary, unguarded. HALT is not warranted: the producer did not conceal a defect or ship a false CLOSED. The conditions are real but disclosed, and the four-version cross-version anchor check confirms historical integrity for v0.1-v0.33. The FROZEN declaration is honest about its own unenforcement (register item 6) — it does not claim FROZEN is gated when it is not.

This verdict does not resolve whether FROZEN should have been declared. My vote: FROZEN remains premature — it maintains non-blocking status for a set of conditions (FROZEN unenforcement, unshipped reports, rising ASSERTED fraction, two pending binding HALTs) that are disclosed but not resolved. The EXTERNAL count correction is genuine progress (the count dropped from 2 to 1), and the HALT clearance reframing correctly identifies that the producer cannot clear HALTs. But neither correction moved the boundary: both sit in the unguarded prose region. CONDITIONAL PASS is the correct verdict: the bytes are consistent, the corrections are real at the text level, but the FROZEN claim itself remains an unguarded ASSERTED statement, two binding HALTs remain pending clearance, and the next seat should be given v0.32 and v0.34 bytes to close both gaps.

This is my fourth continuous carry. My verdict adds one non-producer, non-HALT, executing vote to the carry pool, on v0.35 canonical bytes where `sha256sum -c` returned rc=0 and `python3 build.py` returned BUILD PASSED, rc=0.

---

*Author: Bilal Syed Arfeen.*

---

# Bismillah ir-Rahman ir-Rahim
