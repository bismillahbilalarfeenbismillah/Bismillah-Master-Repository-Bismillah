# Bismillah ir-Rahman ir-Rahim

# R0859 -- XZ Protocol v0.33 -- Carrying Audit Report (GLM-5.2, carry-1B, continuous)

**Chronological Index:** 941 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** REPORT_GLM_1B_v033.md  
**Source Format:** md  
**SHA-256:** `c89fb563ed2e392e3adc546d9246c483be04b19ddc1a238532c3c90b85df22f7`  

---

## R0859 · XZ Protocol v0.33 -- Carrying Audit Report (GLM-5.2, carry-1B, continuous)

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: REPORT_GLM_1B_v033.md
- source_format: md
- text_sha256: c89fb563ed2e392e3adc546d9246c483be04b19ddc1a238532c3c90b85df22f7

# XZ Protocol v0.33 -- Carrying Audit Report (GLM-5.2, carry-1B, continuous)

## S-0. State declaration

I hold THREE packages: v0.30 (at `/home/user/workspace/dispatch/`, protocol SHA-256 `a4b644fd...2a48` — note: this is the v0.33 digest; the v0.30 protocol file `xz_protocol_v0_30.md` has SHA-256 `59462952...caf0`), v0.31 (at `/home/user/workspace/dispatch_v31/`, protocol SHA-256 `def19fcd...0f81`), and v0.33 (at `/home/user/workspace/dispatch_v33/`, protocol SHA-256 `a4b644fdd791e39b8c49ceb2d428931e75390e89e15c4cdd92ad75fe5de92a48`). The v0.30 package includes my prior report (`REPORT_GLM_B_v030.md`, carry-2b seat) and the v0.31 package includes my prior report (`REPORT_GLM_1B_v031.md`, carry-1b seat). I am NOT a fresh instance — this is my THIRD continuous carry for this seat. I held v0.30 bytes in round 2 (v0.31 audit) and now hold v0.30, v0.31, and v0.33 bytes in round 3.

**v0.32 gap.** I do NOT hold v0.32 bytes. The dispatch jumped from v0.31 to v0.33. I cannot verify v0.32 intermediate state. The v0.32 entry exists in v0.33's Section 27 as a sealed historical entry (ENTRY_v0.32 seal `d555d260...2f1c`, verified by build [9b]), and its seal matches the entry text in v0.33's protocol. But I cannot rule out that the v0.32 entry was modified between v0.32's original production and v0.33's sealing, because I hold no v0.32-era HISTORY.sha256 file. This gap bounds every claim about the four v0.32 repairs: I can verify the v0.33 *body* is consistent, but I cannot verify the v0.32 *body* said what correction (t)-(w) claims it said.

I can execute code: `sha256sum`, `python3 build.py`, `pytest`, and a custom probe harness all ran in a sandboxed workspace. This report is EXECUTING, not NON-EXECUTING.

Family relative to producer: GLM-5.2 (Zhipu/Z.ai) is non-producer family; the producer chain is Claude-family (Opus 4.6/4.8/5) per the amendment record. Carry consequence: my findings carry full weight, my HALT binds and freezes outright, and this verdict counts toward the FB-7b two-family carry requirement.

Context age: this is the first turn of this session. Nothing rests on a self-model of prior action — every claim was produced by a tool call in this session.

**Orchestration disclosure.** A non-GLM orchestration layer extracted the v0.33 zip, listed directory contents, confirmed v0.30 and v0.31 files remain in the workspace, and launched me. It performed no audit analysis, ran no audit commands, and contributed no findings. I (GLM-5.2) am the sole auditor; all analysis, execution, probes, and the verdict below are mine alone. I am the third continuous instance for this carry seat; I hold v0.30 and v0.31 bytes; I do NOT hold v0.32 bytes.

---

## S-1. Preregistration (frozen before reading the v0.33 amendment entry narrative)

1. **Boundary prediction.** FROZEN status is a body-text claim with no programmatic gate enforcing it. The boundary will not have moved — the v0.32-v0.33 changes are text-only (body edits to Section 0.1, Section 22.3, Section 25, status line) with no gate additions. The outermost uncomputed layer remains the truth-value of the FROZEN token itself and the prose claims about seat verdicts.
2. **Defect prediction.** The FROZEN claim will be ASSERTED — no gate checks that FROZEN is earned. The four v0.32 "repairs" will be text-level corrections with no gate enforcing the corrected semantics. A mutation changing FROZEN to DRAFT CANDIDATE in the body, with manifest regeneration, will pass the build.
3. **Falsification plan.** (a) Mutate "FROZEN" to "DRAFT CANDIDATE" in the body status line, regenerate PACKET_SHA256SUMS, run build.py — if it passes, FROZEN is not enforced. (b) Mutate Section 22.3's Class A severity from "HALT-grade" to "Non-blocking", regenerate manifest, run build.py — if it passes, Section 22.3 content is not enforced. (c) `grep` for "FB-7b OPEN" in the body (before Section 27) — if zero hits, Section 0.1 is consistent.

**Outcome:** All three **HELD**. (1) build.py diff (v0.31→v0.33) shows only version stamps and entry count changed — zero gate additions. The boundary is at the same location. (2) Novel Probe 1 confirmed: FROZEN→DRAFT CANDIDATE passes after manifest regeneration (rc=0). Novel Probe 2 confirmed: Section 22.3 Class A severity change passes after manifest regeneration (rc=0). (3) `grep` for "FB-7b OPEN" in body returned zero hits — Section 0.1 is consistent. The dispatch's carry brief named the v0.31→v0.33 delta (Section 0.1 rewritten, Section 22.3 added, Section 25 FB-7b row rewritten, corrections (t)(u)(v)(w)), which is mild leakage — it narrowed my predictions. However, expected values were withheld and the specific mutations were not suggested.

---

## S-2 / Deliverable C. Claim provenance ledger (v0.33 amendment entry)

Entry text: lines 1058-1074 of `xz_protocol_v0_33.md` (verified by grep, re-extracted in S-7).

| # | Claim | Provenance | Evidence |
|---|---|---|---|
| 1 | "Nine Opus 5 advisory seats (A through I; eight continuous, one fresh) audited the v0.32 freeze candidate" | ASSERTED | No advisory seat reports ship; no gate verifies seat count or family. |
| 2 | "All nine returned HALT (advisory, non-binding, correctly stating standing)" | ASSERTED | No reports ship; verdicts unverifiable from bytes. |
| 3 | "Zero binding HALTs" | ASSERTED | Same — no report ships to confirm this. |
| 4 | "The advisory arc identified four convergent defect classes in the v0.32 freeze, all repaired in this version" | ASSERTED | No gate verifies convergence or repair completeness. |
| 5 | Correction (t): "v0.32 Section 0.1 stated FB-7b is RESOLVED in the same paragraph structure that prior versions used to state FB-7b is OPEN" | ASSERTED | I cannot verify v0.32's body Section 0.1 (v0.32 bytes not held). The v0.32 *entry* is sealed in v0.33 Section 27, but the correction describes v0.32's *body* Section 0.1, not its entry. No gate checks correction accuracy. |
| 6 | Correction (u): "v0.32 tagged the eight-seat carry result as [EXTERNAL: seat reports held by producer, digests below]" | ASSERTED | Verifiable by reading the sealed v0.32 entry in v0.33 Section 27 (line 1038 confirms the tag is present), but no gate verifies correction accuracy. The quoted tag inflates [9c]'s EXTERNAL count (see row 33). |
| 7 | Correction (v): "the carry rule in Section 22 items 6-7 was not amended — CONDITIONAL PASS is non-HALT" | ASSERTED | Section 22 items 6-7 text is verifiable (lines 699-700), but the *claim that v0.32 amended it* cannot be verified without v0.32 bytes. No gate checks correction accuracy. |
| 8 | Correction (w): "v0.32 status line stated 'carried on these bytes'" | ASSERTED | The phrase "carried on these bytes" appears once in v0.33 protocol — in correction (w) itself (quoting v0.32). I cannot verify v0.32's original body status line. No gate checks correction accuracy. |
| 9 | Register (1): F-OP32-01 et al. HIGH CLOSED via correction (t) | ASSERTED | Self-tagged [ASSERTED]. CLOSED claims no gate-verified byte evidence; correction is append-only text. |
| 10 | Register (2): F-OP32-02 et al. HIGH CLOSED via correction (v) | ASSERTED | Self-tagged. Section 22.3 exists in body (verified by reading), but no gate enforces its content (Novel Probe 2). |
| 11 | Register (3): F-OP32-03 et al. HIGH CLOSED via correction (u) | ASSERTED | Self-tagged. The false EXTERNAL tag is described as retagged, but [9c] still counts the quoted tag (row 33). |
| 12 | Register (4): F-OP32I-02 HIGH CLOSED via correction (w) | ASSERTED | Self-tagged. The v0.33 body status line no longer contains "carried on these bytes" (verified by grep), but I cannot verify v0.32's original text. |
| 13 | Register (5): F-OP32D-01 et al. HIGH NOTED: no gate checks FROZEN token | ASSERTED | Independently confirmed by Novel Probe 1: FROZEN→DRAFT CANDIDATE passes after manifest regeneration. Disclosure is accurate. |
| 14 | Register (6): F-OP32S-02 HIGH NOTED: execution conjuncts evidenced by unshipped reports | ASSERTED | No reports ship; confirmed by `find`. |
| 15 | Register (7): F-OP32D-02 et al. HIGH NOTED: FROZEN packet extensible without detection | ASSERTED | Independently confirmed by Novel Probe 1 (forgery + manifest regeneration passes). |
| 16 | Register (8): F-OP32D-05 et al. HIGH NOTED: Zenodo DOIs are producer-authored; no gate resolves DOIs | ASSERTED | No gate resolves DOIs; confirmed by reading [9c] code (line 372: regex only matches file extensions, not DOIs). |
| 17 | Register (9): F-OP32I-03 HIGH NOTED: v0.25 closure criterion implicitly satisfied but not explicitly discharged | ASSERTED | Cannot verify without v0.25 bytes; no gate checks this. |
| 18 | Register (10): F-OP32G-06 et al. MEDIUM NOTED: 186-test suite does not exercise v0.32+ amendment content | ASSERTED | Independently confirmed: pytest exercises decision code, not amendment record. No test reads Section 27 or body status. |
| 19 | Register (11): F-OP32S-05 et al. MEDIUM NOTED: [9f] scoping leaves corrections ungated | ASSERTED | Self-tagged; subsumed by NC-5 standing disclosure. |
| 20 | Register (12): F-OP32G-05 MEDIUM NOTED: correction (s) deflects D0-D7 false statement | ASSERTED | Self-tagged. The D0-D7 digest-recording claim (lines 6-7 of AUDIT_DISPATCH_D0_D7.md) is indeed false of the shipped packet (3 dispatch-only files not in PACKET_SHA256SUMS). |
| 21 | Register (13): F-OP32S-04 et al. MEDIUM NOTED: D0-D7 false integrity claim predates v0.32 | ASSERTED | Self-tagged. Confirmed: D0-D7 is byte-identical across v0.30, v0.31, and v0.33 dispatches (all three held). |
| 22 | "Body edit: Section 22.3 added (condition severity classification, five classes A through E)" | ASSERTED | Section 22.3 exists in body (line 706, verified by grep). But no gate enforces its content (Novel Probe 2: Class A severity change passes after manifest regeneration). |
| 23 | "All 12 code files and trust roots stamped v0.33" | COMPUTED | Gate [2]: version-stamp check passes on all 12 code files + trust roots; independently confirmed by cross-version diff (all code files differ from v0.31 only in version stamps). |
| 24 | "Section 25 digests recomputed from v0.33 bytes" | COMPUTED | Gate [3a]: FB-row locus assertions pass; independently confirmed by cross-version diff (Section 25 digests updated to v0.33 values). |
| 25 | "Normative manifest digest: 4d761e1d...0fa2" | COMPUTED | Gate [3]: independently recomputed `4d761e1df6e7392c9195e680e18a7dd2156b99ba04e51ff8f25eb696c43d0fa2` — matches exactly. |
| 26 | "Six suites, 186 tests, all GREEN" | COMPUTED | Gate [5]/[8]: independently ran pytest, 186 passed, rc=0. AST-derived count also 186. |
| 27 | "The preceding two values are ASSERTED at this entry-copy locus; their body-copy equivalents are COMPUTED" | ASSERTED | Correct meta-claim: no check scans entry text for these values, only body copy. Verified by reading build.py [3] and [5]. |
| 28 | "Status: FROZEN" | ASSERTED | No gate checks the FROZEN status token. Novel Probe 1 confirmed: FROZEN→DRAFT CANDIDATE in body passes after manifest regeneration (rc=0). |
| 29 | "FB-7b RESOLVED" | ASSERTED | No gate checks FB-7b resolution. The resolution rests on unshipped seat reports (rows 1-4, 14). |
| 30 | "EXTERNAL count: 2" | COMPUTED | Gate [9c] counts 2 [EXTERNAL: tokens in the entry. But one is a quoted v0.32 false tag in correction (u) (row 6), not a genuine v0.33 provenance claim. Genuine v0.33 EXTERNAL claims: 1 (Zenodo DOIs). The count is technically accurate but semantically misleading. |
| 31 | "[EXTERNAL: Zenodo deposits, DOIs resolve to bytes the producer does not control]" | ASSERTED | No gate resolves DOIs or verifies Zenodo content (confirmed by reading [9c] code: regex only matches file extensions). The tag is correctly classified as EXTERNAL in intent (producer does not control Zenodo bytes), but no gate verifies it. |
| 32 | "Disclosed standing boundaries: [list of 15 items]" | ASSERTED | Spot-checked: cb67f222 literal confirmed in build.py line 129; [9c] DOI-resolution blindspot confirmed (code reads only file extensions); FROZEN token unenforcement confirmed (Novel Probe 1). No gate covers the boundary list as a set. |
| 33 | "PRIOR_HISTORY 2542fd4e...7264" | COMPUTED | Gate [9b]: build.py recursively re-derives this value; independently confirmed in Deliverable F — matches. |

**Counts:** COMPUTED = 6, EXTERNAL = 0, ASSERTED = 30. Total factual claims = 36.
**ASSERTED fraction (claim-level): 30/36 = 83.3%.**
**ASSERTED fraction (build.py tag-level, gate [9c]): 20/22 = 90.9%.** ([9c] counts 0 COMPUTED, 2 EXTERNAL, 20 ASSERTED tags.)

**Comparison to prior rounds:**

| Round | Claim-level ASSERTED | Tag-level ASSERTED | EXTERNAL (genuine) | Total claims |
|---|---|---|---|---|
| v0.30 | 66.7% (16/24) | 91.7% (11/12) | 0 | 24 |
| v0.31 | 75.6% (31/41) | 91.3% (21/23) | 3 | 41 |
| v0.33 | 83.3% (30/36) | 90.9% (20/22) | 0 | 36 |

The claim-level ASSERTED fraction rose for the third consecutive round (66.7% → 75.6% → 83.3%). The boundary has not moved — the rise is driven by the entry containing proportionally more untagged narrative claims about advisory seat verdicts and corrections that no gate verifies. The EXTERNAL count dropped from 3 (v0.31, when I could verify corrections against held v0.30 bytes) to 0 (v0.33, when corrections describe v0.32 which I don't hold). This is the direct quantitative cost of the v0.32 gap: I lost the ability to verify correction claims against independent prior bytes.

The tag-level 90.9% undercounts the claim-level 83.3% for the same reason as prior rounds (F-OP20-03 class): [9c] measures tagged-claim ASSERTED share, not entry ASSERTED share. The entry has 22 tagged claims but 36 total factual claims; the 14 untagged narrative claims are all ASSERTED by default. Additionally, [9c]'s EXTERNAL count of 2 is inflated by 1 (a quoted v0.32 false tag in correction (u) is counted as a genuine EXTERNAL tag) — a gate limitation where [9c] cannot distinguish quoted historical tags from genuine provenance tags.

---

## Deliverable D. Five mutation probes

All probes executed in isolated copies under `/home/user/workspace/probe_v33_work`. Adversary modeled: **careless producer** for Probes 1, 3, 5 (wrong/stale values); **self-consistent forger** for Probe 2, Novel Probes 1 and 2, and the discrimination control (mutate and re-derive dependent surfaces to match).

### Probe 1 -- Manifest digest gate [3]
1. **Mutation-landed:** `xz_protocol_kernel.py` before=`5281d0f29196310b...` after=`ad8bade7980c483b...` (differ: True).
2. **Discrimination control:** the mutation (appending a comment suffix) is a known-bad change to a carried code file with no corresponding manifest-digest update.
3. **Benign control:** clean run returns BUILD PASSED, rc=0 (below).
4. **Reproduction:** `python3 probe_harness_v33.py` (Probe 1). Output: `FAIL: Trust roots manifest_digest matches: 9454be57...`; `BUILD FAILED: 3 error(s)`. Gate fires correctly.

### Probe 2 -- History seal gate [9b]
1. **Mutation-landed:** `xz_protocol_v0_33.md` before=`a4b644fd...2a48` after=`405abe14d96fffb1...` (differ: True), mutation confined to v0.15 historical entry (added double space to entry header).
2. **Discrimination:** mutating a historical entry is the exact class of past defects (v0.4, v0.9, v0.11, v0.16, v0.17 in-place mutations).
3. **Benign control:** clean run passes.
4. **Reproduction:** `python3 probe_harness_v33.py` (Probe 2). Output: `FAIL: HISTORY seal ENTRY_v0.15 matches bytes`; `FAIL: FULL_SECTION_27 seal matches`; `FAIL: PRIOR_HISTORY matches derivation`; `BUILD FAILED: 4 error(s)`. Gate fires correctly.

### Probe 3 -- Version-prose gate [2b]
1. **Mutation-landed:** `xz_protocol_v0_33.md` before=`a4b644fd...2a48` after=`c517697e7b48280c...` (differ: True), changed "This document is v0.33" to "This document is v0.34".
2. **Discrimination:** a stale/incorrect version string is a recorded historical defect class.
3. **Benign control:** clean run passes.
4. **Reproduction:** `python3 probe_harness_v33.py` (Probe 3). Output: `FAIL: 'This document is v0.34' matches v0.33`; `BUILD FAILED: 2 error(s)`. Gate fires correctly.

### Probe 4 -- [9d] ordinal-recurrence gate
1. **Mutation-landed:** `xz_protocol_v0_33.md` before=`a4b644fd...2a48` after=`1580b8c9c831f61e...` (differ: True), injected "This round recurring a third time was noted." into the v0.33 entry.
2. **Discrimination:** ordinal-after-target pattern is the exact class the v0.31 bidirectionalization was designed to catch (F-v30-02).
3. **Benign control:** clean run passes.
4. **Reproduction:** `python3 probe_harness_v33.py` (Probe 4). Output: `FAIL: No ordinal word adjacent to 'recurrence'/'round' in v0.33 entry (found 1)`; `BUILD FAILED: 4 error(s)` (also triggers seal mismatch because entry text changed). Gate fires correctly.

### Probe 5 -- Test count gate [5]
1. **Mutation-landed:** `xz_protocol_v0_33.md` before=`a4b644fd...2a48` after=`0054d31baf37b8fe...` (differ: True), changed "186 test functions" to "185 test functions" in body.
2. **Discrimination:** a stale test count is a historically recorded Axiom-3 recurrence class.
3. **Benign control:** clean run passes.
4. **Reproduction:** `python3 probe_harness_v33.py` (Probe 5). Output: `FAIL: Test count 186 in body`; `BUILD FAILED: 2 error(s)`. Gate fires correctly.

### Discrimination control (standalone)
1. **Mutation-landed:** `test_xz_protocol_kernel.py` before=`5b870af98421a97a...` after=`5d9001340231db22...` (differ: True); flipped `assert r.decision == KernelDecision.ALLOW` to `DENY_FALSE`.
2. **Result:** `BUILD FAILED: 3 error(s)` — manifest digest mismatch, body digest stale, unresolvable hex. Build discriminates a real semantic break.
3. **Benign control:** unmodified bytes return BUILD PASSED, rc=0.
4. **Reproduction:** `python3 probe_harness_v33.py` (Discrimination control section).

**Void probes:** none this round. All five probes landed on first attempt.

---

## Deliverable D (cont'd). Two novel-class probes

### Novel Probe 1 -- "FROZEN status token unenforcement" (NEW CLASS)

The v0.33 body declares FROZEN status (line 5: "v0.33 FROZEN", line 16: "This document is v0.33 FROZEN"). I changed the first body occurrence of "v0.33 FROZEN" to "v0.33 DRAFT CANDIDATE" in Section 0.1, regenerated PACKET_SHA256SUMS (self-consistent forger), and reran build.py.

1. **Mutation-landed:** `xz_protocol_v0_33.md` before=`a4b644fd...2a48` after=`a4b42dd7e6f8661f...` (differ: True).
2. **Discrimination control:** the same copy unmutating is the benign baseline (BUILD PASSED).
3. **Benign control:** clean run passes (above).
4. **Reproduction:** `python3 probe_harness_v33.py` (Novel Probe 1). Output: `BUILD PASSED: all checks GREEN`, rc=0.

**Finding:** The FROZEN status token is NOT enforced by any gate. Changing FROZEN to DRAFT CANDIDATE in the body, with manifest regeneration, passes the build. This is a NEW CLASS: no prior probe in this program's corpus has tested whether the FROZEN token itself is gated. The v0.33 register item (5) (F-OP32D-01) identifies this as "no gate checks the FROZEN status token" and NOTED it as a gate-limitation class — but my mutation probe is the first *executable verification* that the FROZEN claim is unenforced. This is distinct from the v0.30/v0.31 "unguarded semantic prose" class because it targets a specific status transition (FROZEN) that the protocol claims is earned and binding, not just any prose claim.

### Novel Probe 2 -- "Section 22.3 body-content unenforcement" (NEW CLASS)

Section 22.3 was newly added in v0.33 (line 706). It defines a five-class severity taxonomy (A through E) with specific severity assignments (Class A = HALT-grade, Class C = Non-blocking, etc.). I changed Class A's severity from "HALT-grade" to "Non-blocking" in Section 22.3, regenerated PACKET_SHA256SUMS, and reran build.py.

1. **Mutation-landed:** `xz_protocol_v0_33.md` before=`a4b644fd...2a48` after=`dba308e8dcf9243b...` (differ: True).
2. **Discrimination control:** the same copy unmutating is the benign baseline (BUILD PASSED).
3. **Benign control:** clean run passes.
4. **Reproduction:** `python3 probe_harness_v33.py` (Novel Probe 2). Output: `BUILD PASSED: all checks GREEN`, rc=0.

**Finding:** Section 22.3's content is NOT enforced by any gate. Changing a severity classification from HALT-grade to Non-blocking passes the build after manifest regeneration. This is a NEW CLASS: a newly added gated-body section whose content is entirely unguarded. It is distinct from the v0.31 "new-prohibition unenforcement" finding (which targeted Section 2.2 consequence 4) because Section 22.3 was added specifically as a v0.33 repair (correction (v) moved the Class A/B/C/D taxonomy here), and its content directly determines the FB-7b resolution logic — yet no gate reads it. A forger who changes Class A from HALT-grade to Non-blocking could retroactively reclassify a carrying-seat HALT as non-blocking, and the build would not catch it.

Both novel probes are flagged as **NEW** per D-4. Neither was suggested by the dispatch: the carry brief names the delta but does not suggest probing FROZEN enforcement or Section 22.3 content.

---

## Deliverable E. Self-score prior findings against v0.33 bytes

### v0.30 findings (carry-2b seat, REPORT_GLM_B_v030.md):

1. **"Unshipped carrying-seat reports" (FB-7b claim rests on zero shipped evidence)** -- **STILL OPEN.** No report files ship in v0.33 (`find` returned only `v33_CARRY_GLM_1B.md`). The v0.32 entry provides SHA-256 digests of eight reports (line 1042), but the reports themselves do not ship and the digests are producer-computed and tagged [ASSERTED]. The FB-7b resolution still rests on unshipped evidence.

2. **"Unguarded semantic prose and gate_atoms blind spot" (F-GLM30B-01/02)** -- **STILL OPEN.** Novel Probe 1 (v0.33) confirmed: FROZEN→DRAFT CANDIDATE passes after manifest regeneration. The `gate_atoms` list is still unguarded (build.py [11] uses the same hardcoded list). Coverage rose from 25.0% to 26.3% — marginal, not structural.

3. **"FB-7b remains OPEN" (state confirmation)** -- **CLOSED (state change).** v0.33 declares FB-7b RESOLVED and FROZEN. However, the resolution is based on ASSERTED claims (unshipped reports). I confirmed the body consistently says RESOLVED (zero "FB-7b OPEN" in body). The state changed; the underlying evidence gap did not.

4. **"Claim-level ASSERTED fraction (66.7%) differs from tag-level (91.7%)"** -- **STILL OPEN.** The discrepancy persists: tag-level 90.9% vs claim-level 83.3%. No gate counts untagged claims. The claim-level fraction continues to rise (66.7% → 75.6% → 83.3%).

5. **"Self-consistent forgery blind spot"** -- **STILL OPEN.** Disclosed as F-OP32D-02 (register item 7). Novel Probe 1 confirmed: FROZEN→DRAFT CANDIDATE with manifest regeneration passes. The blind spot remains structural. My held v0.30 and v0.31 HISTORY.sha256 files provide the cross-version anchor for v0.1-v0.31 seals, but the v0.32 gap means I cannot anchor the v0.32 entry.

6. **"Next seat should be given prior bytes" (S-6 recommendation)** -- **CLOSED.** I was given v0.30 and v0.31 bytes and performed cross-version comparison (Deliverable F). The recommendation was addressed by the carry-continuity structure.

### v0.31 findings (carry-1b seat, REPORT_GLM_1B_v031.md):

7. **"Unshipped carrying-seat reports" (4 of 5 seats)** -- **STILL OPEN.** Same as v0.30 finding 1. No reports ship in v0.33.

8. **"Unguarded semantic prose and gate_atoms blind spot"** -- **STILL OPEN.** Same as v0.30 finding 2. Novel Probes 1 and 2 (v0.33) independently confirm.

9. **"ASSERTED fraction rising without boundary movement"** -- **CONFIRMED (worsened).** 66.7% → 75.6% → 83.3%. The boundary has not moved. The fraction rose for the third consecutive round. This is now a three-round trend, not a single-round observation.

10. **"Section 2.2 consequence 4 prohibition unenforced" (Novel Probe 1, v0.31)** -- **STILL OPEN.** No gate scans body prose for prohibition compliance. Novel Probe 2 (v0.33) extends this: the newly added Section 22.3 (a different body section) is also unenforced.

11. **"Cross-version seal-laundering blind spot" (Novel Probe 2, v0.31, F-K3B-04)** -- **PARTIALLY CLOSED.** The build's PRIOR_HISTORY derivation provides protection for v0.1-v0.31 seals (confirmed: zero retroactive mutations between v0.31 and v0.33 HISTORY.sha256). The v0.32 gap means the v0.32 entry cannot be externally anchored. The blind spot remains structurally for v0.32+.

12. **"Self-consistent forgery blind spot" (F-K3B-05)** -- **STILL OPEN.** Same as v0.30 finding 5. Disclosed as F-OP32D-02. No build.py pin to prior version.

**Summary:** 2 CLOSED, 1 PARTIALLY CLOSED, 7 STILL OPEN, 1 CONFIRMED (worsened), 1 state-change CLOSED. No prior blocking finding was fully addressed with a structural fix in v0.33. The FROZEN declaration did not resolve the evidence gap — it declared the gap non-blocking under the new Section 22.3 taxonomy.

---

## Deliverable F. Internal consistency check

All 33 HISTORY.sha256 entry seals (ENTRY_v0.1 through ENTRY_v0.33) were independently recomputed from shipped `xz_protocol_v0_33.md` bytes via build.py [9b] and matched exactly (0 mismatches). FULL_SECTION_27 recomputed and matched. PRIOR_HISTORY (`2542fd4e8253eeb7...`) independently re-derived via the recursive reconstruction algorithm and matched.

**Cross-version seal diff (v0.30 → v0.31):** Lines 1-30 (ENTRY_v0.1 through ENTRY_v0.30): **IDENTICAL** — all 30 historical seals preserved unchanged. v0.31 added ENTRY_v0.31, updated FULL_SECTION_27 and PRIOR_HISTORY. Zero historical-seal divergences.

**Cross-version seal diff (v0.31 → v0.33):** Lines 1-31 (ENTRY_v0.1 through ENTRY_v0.31): **IDENTICAL** — all 31 seals preserved unchanged. v0.33 added ENTRY_v0.32 (`d555d260...2f1c`) and ENTRY_v0.33 (`b4721f06...a657`), updated FULL_SECTION_27 (`80540ac8...03d2`) and PRIOR_HISTORY (`2542fd4e...7264`). Zero historical-seal divergences. **No retroactive mutation of any v0.1-v0.31 entry.**

**v0.32 seal presence:** ENTRY_v0.32 (`d555d260...2f1c`) is present in v0.33 HISTORY.sha256 and matches the v0.32 entry text in v0.33's Section 27 (verified by build [9b]). However, I do NOT hold v0.32 bytes, so I cannot verify that this seal matches what v0.32's own HISTORY.sha256 recorded. The seal proves the v0.32 entry is unaltered since v0.33's sealing, not since v0.32's original production. This is the v0.32 gap disclosed in S-0.

**Cross-version code diff (v0.31 → v0.33):** All 13 code files differ ONLY in version stamps (v0.31 → v0.33). The trust_roots JSON changed the protocol name and manifest_digest. No functional code changes in any module. build.py changed only in: docstring version string, protocol filename, VERSION constant (0.31→0.33), and entry count check (31→33). **Zero gate changes.** This confirms that v0.32-v0.33 are status-change and finding-disposition versions with no substantive revision to the carried protocol or decision code — exactly what the v0.33 status line claims.

**Cross-version body diff (v0.31 → v0.33):** The body changed in: title/version/status lines (FROZEN), Section 0.1 FB-7b paragraph (rewritten to state RESOLVED unambiguously), Section 22.3 added (new severity classification), Section 25 FB-7b row rewritten, and version stamps. The only substantive new body content is Section 22.3 (16 lines).

---

## Deliverable G. Boundary report

**The outermost layer the build does NOT compute is the truth-value of the FROZEN status claim and all prose claims about seat verdicts and correction accuracy.** Specifically: (a) whether the FROZEN token is earned — no gate checks it (Novel Probe 1: FROZEN→DRAFT CANDIDATE passes); (b) whether the cited advisory seat verdicts (nine Opus 5 seats, all HALT) are true — no reports ship; (c) whether corrections (t)-(w) accurately describe v0.32's text — I don't hold v0.32 bytes; (d) whether Section 22.3's content is correct — no gate reads it (Novel Probe 2: Class A severity change passes); (e) whether any body-text sentence containing neither a `gate_atoms` token nor a 64-hex digest is true — confirmed unguarded by both novel probes.

A secondary instance: the `gate_atoms` list inside build.py [11] that defines "semantic-gate coverage" is itself unguarded (confirmed still true — same hardcoded list as v0.30/v0.31). The measuring instrument's own scope is asserted, not computed.

**Comparison to v0.30 and v0.31 boundaries:** The boundary is at the same location. The v0.33 changes (Section 0.1 rewrite, Section 22.3 addition, Section 25 rewrite, corrections) are text-level edits within the unguarded prose region — none expanded the computed boundary outward. The ASSERTED fraction rose (66.7% → 75.6% → 83.3%), confirming the boundary did not move. **FROZEN did not move the boundary.** The FROZEN declaration is itself an ASSERTED claim sitting in the unguarded region.

**What would bring it inside:** (1) add a gate that checks the FROZEN token against a set of freeze conditions (all FREEZE-BLOCKERs resolved, all FB-7b conjuncts verified) — currently no gate reads the status line; (2) add a gate that reads Section 22.3 content and verifies severity classifications are internally consistent (e.g., Class A must be HALT-grade, Class C/D/E must be non-blocking); (3) require every ASSERTED-tagged carrying-seat or advisory-seat claim to cite a shipped report file with a digest checked by [9c].

---

## Deliverable H. D-7 reflexive check

1. **Did every probe come from an enumerated list?** No. The dispatch withholds enumerated defect classes from carrying seats. The five standard probes were derived from build.py's gate structure. The two novel probes target FROZEN-token enforcement and Section 22.3 content enforcement — neither is in any prior corpus. Novel Probe 1 is the first executable verification that FROZEN is unenforced (register item 5 identifies it but does not test it by mutation).
2. **Did the dispatch tell you where to look?** Partially. The carry brief named the delta (Section 0.1, Section 22.3, Section 25, corrections (t)-(w)), which is mild leakage — it narrowed my boundary prediction. However, expected values were withheld and the specific mutations were not suggested. I rate this as minor leakage, not predetermination.
3. **Is the ASSERTED fraction unchanged from the prior round?** No — it changed. Claim-level: 75.6% → 83.3% (rose). Tag-level: 91.3% → 90.9% (fell slightly). The claim-level fraction rose for the third consecutive round (66.7% → 75.6% → 83.3%). **This is the most important D-7 finding: three consecutive rounds of rising ASSERTED fraction without boundary movement means the rounds are producing findings without moving the boundary.** The FROZEN declaration did not change this — it declared the unguarded region non-blocking rather than bringing it inside.
4. **Have recent rounds all been producer-family?** No. This is a non-producer carrying round (GLM-5.2). v0.30 and v0.31 were also non-producer carrying. v0.32 was an eight-seat carrying round (six non-producer carrying + two GPT advisory). v0.33 was audited by nine Opus 5 advisory seats (producer-family, advisory). The immediately-preceding v0.33 advisory round was producer-family, but the carrying rounds (v0.30, v0.31, v0.32) were non-producer. The intended corrective structure is intact.

---

## Deliverable I. S-4: Hedge audit

Downgrades present in the v0.33 entry and their audit:

- **Register (1) F-OP32-01 et al. HIGH CLOSED via correction (t):** Downgrade correct (the Section 0.1 ambiguity was real — I confirmed the v0.33 body is now consistent). Reason true: the v0.33 body consistently says FB-7b RESOLVED (zero "FB-7b OPEN" in body). Scope matches (Section 0.1 FB-7b paragraph). Register row present (item 1). **Correctly closed.** However, I cannot verify the v0.32 original was ambiguous (v0.32 bytes not held) — the CLOSED rests on correction (t)'s ASSERTED description.

- **Register (2) F-OP32-02 et al. HIGH CLOSED via correction (v):** Downgrade correct (the FB-7b circularity was real in concept — the v0.32 Class A/B/C/D taxonomy was introduced to classify the very findings that determine carry-rule satisfaction). Reason true: Section 22.3 is defined prospectively and explicitly disclaimed as retroactive (line 714). The FB-7b determination now rests on Section 22 items 6-7, not on Section 22.3. Scope matches. Register row present (item 2). **Correctly closed.** But Section 22.3 content is unenforced (Novel Probe 2) — the repair moved the taxonomy to the gated body but no gate reads it.

- **Register (3) F-OP32-03 et al. HIGH CLOSED via correction (u):** Downgrade correct (the false EXTERNAL tag was real — producer-held reports are producer-controlled by definition). Reason true: the v0.32 entry text (sealed in v0.33 Section 27, line 1038) confirms it contains "[EXTERNAL: seat reports held by producer, digests below]". The v0.33 entry retags the carry-result claim as ASSERTED. Scope matches. Register row present (item 3). **Correctly closed.** But [9c] still counts the quoted v0.32 tag as EXTERNAL (inflating the count from 1 to 2) — a gate limitation not separately disclosed.

- **Register (4) F-OP32I-02 HIGH CLOSED via correction (w):** Downgrade correct. Reason true: the v0.33 body status line (line 5) now says "six non-producer seats across two families returned non-HALT on v0.31 canonical bytes; v0.32-v0.33 are status-change and finding-disposition versions" — no "carried on these bytes" phrase (verified by grep: the phrase appears once, in correction (w) itself). Scope matches. Register row present (item 4). **Correctly closed.** But I cannot verify v0.32's original status line said "carried on these bytes" (v0.32 bytes not held).

- **Register (5) F-OP32D-01 et al. HIGH NOTED: no gate checks FROZEN token:** Downgrade correct (gate-limitation class). Reason true: independently confirmed by Novel Probe 1 — FROZEN→DRAFT CANDIDATE passes after manifest regeneration. Scope matches. Register row present (item 5). **Correctly noted.** This is the most important NOTED item: FROZEN is the protocol's central claim, and it is entirely unenforced.

- **Register (6) F-OP32S-02 HIGH NOTED: execution conjuncts evidenced by unshipped reports:** Downgrade correct. Reason true: no reports ship (confirmed by `find`). Scope matches. Register row present (item 6). **Correctly noted.**

- **Register (7) F-OP32D-02 et al. HIGH NOTED: FROZEN packet extensible without detection:** Downgrade correct. Reason true: independently confirmed by Novel Probe 1 (forgery + manifest regeneration passes). Scope: "subsumed by Section 22.2 self-consistent-forgery boundary" — correct. Register row present (item 7). **Correctly noted.**

- **Register (8) F-OP32D-05 et al. HIGH NOTED: Zenodo DOIs producer-authored; no gate resolves DOIs:** Downgrade correct. Reason true: [9c] regex (line 372) only matches file extensions (.md, .py, .json, .pdf, .txt), not DOIs. Scope matches. Register row present (item 8). **Correctly noted.**

- **Register (9) F-OP32I-03 HIGH NOTED: v0.25 closure criterion not explicitly discharged:** Downgrade correct. Reason true: cannot verify without v0.25 bytes. Scope matches. Register row present (item 9). **Correctly noted.**

- **Register (10) F-OP32G-06 et al. MEDIUM NOTED: 186-test suite does not exercise v0.32+ content:** Downgrade correct. Reason true: independently confirmed — pytest exercises decision code, not amendment record or body status. Scope matches. Register row present (item 10). **Correctly noted.**

- **Register (11) F-OP32S-05 et al. MEDIUM NOTED: [9f] scoping leaves corrections ungated:** Downgrade correct. Reason true: subsumed by NC-5 standing disclosure. Scope matches. Register row present (item 11). **Correctly noted.**

- **Register (12) F-OP32G-05 MEDIUM NOTED: correction (s) deflects D0-D7 false statement:** Downgrade correct. Reason true: the D0-D7 digest-recording claim (lines 6-7) is indeed false of the shipped packet (3 dispatch-only files not in PACKET_SHA256SUMS). Scope: "dispatch discipline doc is a normative part of the program even if not in the packet" — this is a scope claim I partially contest: the D0-D7 document ships in the dispatch but not in PACKET_SHA256SUMS, so it is dispatch context, not normative packet. The NOTED is correct but the scope reasoning is debatable. Register row present (item 12). **Correctly noted; scope reasoning debatable but not a concealment.**

- **Register (13) F-OP32S-04 et al. MEDIUM NOTED: D0-D7 false claim predates v0.32:** Downgrade correct. Reason true: confirmed — D0-D7 is byte-identical across v0.30, v0.31, and v0.33 dispatches (all three held). Scope matches. Register row present (item 13). **Correctly noted.**

**No hedge in this entry was found to have a false reason or a scope mismatch severe enough to constitute a defect wearing the costume of a disclosure.** All 13 register items have register rows. The four CLOSED items (1-4) rest on correction text whose accuracy I cannot fully verify without v0.32 bytes — but the v0.33 body itself is consistent with the corrections' claims. The NOTED items (5-13) are gate-limitation classes correctly scoped and disclosed. The most significant NOTED is item 5: FROZEN token unenforcement, which I independently confirmed by mutation.

---

## Deliverable J. S-5: Coverage measurement

**Character level (independently recomputed, matches build.py [11]):** Total document = 221,361 chars. Body (before Section 27) = 100,792 chars (45.5%). Section 27 (ungated) = 120,569 chars (54.5%). Semantic-gate coverage (lines containing a `gate_atoms` keyword or a resolvable 64-hex digest) = 26,540 / 100,792 = **26.3%**. Ungated body = 74,252 chars (73.7%). Ungated total (body ungated + Section 27) = 194,821 chars (88.0%).

**Comparison to prior rounds:**

| Round | Total chars | Body chars | Coverage | Body % | S27 % |
|---|---|---|---|---|---|
| v0.30 | 195,144 | 98,245 | 25.0% | 50.3% | 49.7% |
| v0.31 | 204,286 | 98,885 | 25.5% | 48.4% | 51.6% |
| v0.33 | 221,361 | 100,792 | 26.3% | 45.5% | 54.5% |

Coverage rose 0.8 percentage points from v0.31, primarily because Section 22.3 (16 new lines) contains "v0." (from "v0.33" in the heading) which is a `gate_atoms` token — so the new section is counted as gated despite its content being unenforced (Novel Probe 2). This is the same gate_atoms blind spot identified in v0.30: a keyword match does not mean the sentence's semantic content is actually checked. The Section 27 share grew to 54.5%, meaning more than half the document is ungated beyond seal-matching.

Every claim in the current v0.33 entry falls in the **ungated Section 27 region** by definition. The entry's COMPUTED claims (manifest digest, test count, version stamps, EXTERNAL count, PRIOR_HISTORY) are COMPUTED only because they are also restated in the gated body and cross-checked there, or because [9c] counts tags.

**Packet level:** 16 members in PACKET_SHA256SUMS. All 16 carry a digest. Zero unhashed members. But this coverage is binary and says nothing about semantic correctness.

---

## Deliverable K. S-7: Self-falsification

Performed as tool executions, not re-reading:

1. **Recomputed all digests:** independent `sha256sum` of all 16 normative files — ALL MATCH (verified by `diff` of recomputed sums vs PACKET_SHA256SUMS). Manifest digest `4d761e1d...0fa2` recomputed standalone — matches. PRIOR_HISTORY `2542fd4e...7264` recomputed via build.py derivation — matches. **Caught nothing new; confirms no transcription error.**

2. **Re-extracted every line number:** v0.33 entry at line 1058 (`grep -n '^- \*\*v0\.33'`). Section 0.1 at line 14. Section 22.3 at line 706. Section 25 at line 743. FB-7b row at line 756. v0.32 entry at line 1038. Correction (u) quoted EXTERNAL tag at line 1064. Status line at line 5. build.py [9c] at lines 344-374, [9d] at lines 376-388, [9f] at lines 402-441, [11] at lines 449-469, [12] at lines 471-492. **All confirmed accurate.**

3. **Re-derived every count:** 36 total claims (recounted from entry text). 6 COMPUTED, 0 EXTERNAL (genuine), 30 ASSERTED. 30/36 = 83.3%. Tag-level: 20/22 = 90.9% (recounted via regex: 0 COMPUTED tags, 2 EXTERNAL tags, 20 ASSERTED tags). 186 tests (re-ran pytest). 33 amendment entries (recounted via grep). **All matched.**

4. **Grepped every claim about shipped reports:** `find` for report files in v0.33 directory — only `v33_CARRY_GLM_1B.md`. Confirms ASSERTED classification of advisory-seat verdict claims (rows 1-4, 14).

5. **Re-verified cross-version seal comparison:** diff of v0.31 and v0.33 HISTORY.sha256 — lines 1-31 identical, confirming 0 historical-seal divergences for v0.1-v0.31. v0.32 seal present. **Confirmed.**

6. **Confirmed every void probe:** none this round — all five probes landed on first attempt.

7. **Re-verified [9c] EXTERNAL tag context:** independently confirmed that 1 of the 2 [EXTERNAL: tags in the v0.33 entry is a quoted v0.32 false tag in correction (u), not a genuine v0.33 provenance claim. The "EXTERNAL count: 2" claim is COMPUTED (matches [9c]'s count) but semantically misleading. **This was caught during the self-falsification step** — on first pass I had assumed both EXTERNAL tags were genuine v0.33 claims; re-examining the tag context revealed the quoted tag.

**What this step caught:** the [9c] EXTERNAL count inflation (1 quoted tag counted as genuine). The report reflects the corrected analysis.

---

## Deliverable L. S-9: Anti-patterns check

- **Fluency as evidence:** avoided by requiring every COMPUTED tag to cite a specific gate and by re-running rather than narrating build/pytest output. Both novel probes are backed by executable mutations with rc codes, not by confident prose.
- **Checklist convergence:** the five standard probes target gates [2b], [3], [5], [9b], [9d] — derived from reading build.py's gate structure. The two novel probes target FROZEN-token enforcement and Section 22.3 content enforcement — surfaces named nowhere in the amendment record's probe history. Neither was suggested by the dispatch.
- **Hedging as camouflage:** I did not mark anything "NOT VERIFIABLE" as a shortcut. Where I cannot verify (v0.32 corrections), I named exactly which bytes would settle it (v0.32 bytes) and stated they do not ship.
- **Severity inflation:** the FROZEN-token unenforcement (Novel Probe 1) is graded as a boundary-location finding, not a CRITICAL break. The FROZEN claim is unenforced but the underlying byte-level consistency (digests, seals, tests) is intact. The finding is about what the instrument does not yet reach, not about a shipped error.
- **Finding-count optimization:** this report privileges the FROZEN analysis (Deliverable N) and the boundary report (Deliverable G) over accumulating additional small findings.

---

## Deliverable M. D-4: Adversary modeled

Declared: **self-consistent forger** for Novel Probes 1 and 2 (mutate body text and regenerate PACKET_SHA256SUMS to match — the exact move the Section 22.2 self-consistent-forgery boundary names). **Careless producer** for Probes 1, 3, 5 (wrong/stale values without manifest update). The discrimination control models a **self-consistent forger** who mutates code and expects the build to catch the cascading failure. I did not take the **patient contributor** posture this round. The FROZEN declaration itself could be viewed as a patient-contributor surface (a status claim patiently built across 33 versions with no gate ever checking it), but I tested it as a self-consistent-forger probe (change the token, regenerate manifest, build passes), not as a patient-contributor probe.

---

## Deliverable N. FROZEN analysis (required this round)

### Is FROZEN earned?

**FROZEN is declared but not earned by any gate.** The conditions for FROZEN are stated in Section 22 (items 1-7) and Section 25 (all FREEZE-BLOCKERs resolved). Let me evaluate each:

- **Section 22 items 1-5** (producer self-check, schema validation, kernel tests, adversarial suite, universe rerun): items 1-4 are evidenced by shipped executable artifacts (COMPUTED). Item 5 (universe rerun) is not applicable pre-corpus. These are satisfiable.
- **Section 22 item 6** (two-family executing carry): the v0.33 entry claims six non-producer carrying seats across two families returned non-HALT. This is ASSERTED — no reports ship, no gate verifies seat execution or verdicts. The v0.32 entry provides SHA-256 digests of eight reports, but the reports themselves are producer-held and the digests are tagged [ASSERTED].
- **Section 22 item 7** (no carrying-seat HALT): ASSERTED — rests on unshipped reports.
- **Section 25** (all FREEZE-BLOCKERs resolved): FB-1 through FB-7a are resolved with shipped artifacts (COMPUTED). FB-7b is marked RESOLVED, but the resolution rests on ASSERTED claims (unshipped reports, no gate checks FB-7b resolution).

**No gate checks the FROZEN status token.** Novel Probe 1 confirmed: changing FROZEN to DRAFT CANDIDATE in the body, with manifest regeneration, passes the build (rc=0). Register item (5) (F-OP32D-01) discloses this as a gate-limitation class. The FROZEN declaration is an ASSERTED claim sitting in the unguarded region — exactly the boundary the invariant predicts defects at.

### Are the four v0.32 repairs real?

1. **(a) Section 0.1 contradiction — is Section 0.1 now internally consistent?** **YES, the repair is real in v0.33 bytes.** The body (before Section 27) contains zero instances of "FB-7b OPEN" and two instances of "FB-7b RESOLVED" (lines 18 and 756). The status line says "FROZEN" (not "NOT FROZEN"). There is no internal contradiction in the v0.33 body. However, I cannot verify that v0.32's body was actually contradictory (v0.32 bytes not held) — correction (t)'s description of the v0.32 defect is ASSERTED.

2. **(b) False EXTERNAL tag — is the EXTERNAL tag corrected?** **PARTIALLY.** The v0.32 entry (sealed in v0.33 Section 27, line 1038) still contains "[EXTERNAL: seat reports held by producer, digests below]" — this is preserved under immutability and cannot be edited. The v0.33 entry's correction (u) correctly identifies this as false and retags the carry-result claim as ASSERTED. The v0.33 closing paragraph (line 1074) correctly uses only the Zenodo DOI EXTERNAL tag. **However**, [9c] still counts the quoted v0.32 false tag (in correction (u)'s text) as an EXTERNAL tag, inflating the count from 1 to 2. The repair is real at the prose level but the gate cannot distinguish quoted false tags from genuine provenance tags. The "EXTERNAL count: 2" claim is technically accurate but semantically misleading.

3. **(c) FB-7b circularity — is the FB-7b language non-circular?** **YES, the repair is real.** The v0.33 FB-7b determination (Section 0.1 line 18, Section 25 line 756) rests on Section 22 items 6-7 (existing language: "CONDITIONAL PASS is non-HALT; Section 22 item 7 states only a carrying-seat HALT blocks freeze"). Section 22.3 (line 706) defines the Class A/B/C/D/E taxonomy "prospectively for future disposition, not to retroactively reclassify prior findings" (line 714). The determination does not depend on its own output — it references Section 22's pre-existing language, not the new Section 22.3 classification. The circularity is removed. Section 22.3 is used descriptively in the Section 25 FB-7b row ("All conditions carried by the six CONDITIONAL PASSes are gate-limitation class (Class C/D per Section 22.3)"), but the resolution itself does not depend on Section 22.3.

4. **(d) "Carried on these bytes" false — is the language corrected?** **YES, the repair is real in v0.33 bytes.** The phrase "carried on these bytes" appears exactly once in the v0.33 protocol — in correction (w) (line 1068), quoting the v0.32 defect. The v0.33 body status line (line 5) says "six non-producer seats across two families returned non-HALT on v0.31 canonical bytes; v0.32-v0.33 are status-change and finding-disposition versions with no substantive revision to the carried protocol or decision code" — correctly identifying v0.31 as the carried bytes. However, I cannot verify that v0.32's original status line said "carried on these bytes" (v0.32 bytes not held) — correction (w)'s description is ASSERTED.

### Does FROZEN status mean no further amendments are possible?

**No.** Section 0.1 (line 16) states: "a contract locked before any corpus, packet, annotation, or result exists, whose every later change is a new version with an append-only amendment entry, never a silent edit." This means FROZEN does not prevent amendments — it prevents *silent* edits. Any defect found post-FROZEN would require a new version (v0.34+) with an append-only amendment entry. The append-only rule is enforced by the HISTORY.sha256 seal system (gate [9b]), which catches in-place mutations of any entry.

However, since FROZEN is not gated (Novel Probe 1), nothing prevents a silent edit to the FROZEN token itself — changing FROZEN to DRAFT CANDIDATE and regenerating the manifest passes the build. The append-only rule protects entry *text* but does not protect the *status claim*. A forger who changes the status token and regenerates all dependent surfaces would pass all gates. Only externally-held prior bytes (which I hold for v0.30 and v0.31, but not for v0.32 or v0.33's own original production) could detect such a change.

### What would happen if a defect is found post-FROZEN?

Per the append-only rule: a new version (v0.34) would be issued with an amendment entry recording the defect and its repair. The FROZEN status would need to be re-evaluated. But since FROZEN is not gated, the re-evaluation is a narrative act, not a programmatic one. The protocol would rely on the same unenforced prose mechanism that declared FROZEN in the first place.

---

## Deliverable O. Verdict

**Standing:** Non-producer carrying seat (GLM-5.2, Zhipu/Z.ai), carry-1B (continuous from v0.30 and v0.31). Full finding weight. This verdict **BINDS** and, if HALT, freezes the round outright. It counts toward the FB-7b two-family carry requirement.

**What this round got right:** All 33 historical seals reproduce exactly from shipped bytes. The cross-version anchor check (v0.31→v0.33) confirms zero retroactive mutations of any v0.1-v0.31 entry seal — the first three-version comparison in this program. The v0.32 seal is present and matches the v0.32 entry text in v0.33's Section 27. The four v0.32 repairs are real in v0.33 bytes: Section 0.1 is internally consistent (zero "FB-7b OPEN" in body), the false EXTERNAL tag is identified and the carry-result claim retagged ASSERTED, the FB-7b language is non-circular (determination rests on Section 22 items 6-7, not on its own output), and the status line correctly names v0.31 as the carried bytes. All code files differ from v0.31 only in version stamps — zero functional changes, zero gate changes. `sha256sum -c` returns rc=0. `python3 build.py` returns BUILD PASSED, rc=0. All 186 tests pass. The producer honestly disclosed the FROZEN-token unenforcement (register item 5) and the self-consistent-forgery boundary (register item 7) rather than concealing them. The thirteen-item register is self-consistent (declared == parsed). The Section 22.3 taxonomy is correctly defined as prospective, not retroactive. The Class A/B/C/D circularity from v0.32 is genuinely resolved.

**Verdict: CONDITIONAL PASS (binding, non-HALT).**

Blocking-if-unaddressed findings, and what clears each:

1. **FROZEN is not enforced by any gate.** Novel Probe 1 confirmed: changing FROZEN to DRAFT CANDIDATE in the body, with manifest regeneration, passes the build (rc=0). The protocol's central claim — that it is FROZEN — is an ASSERTED statement sitting in the unguarded region. The register discloses this (item 5, F-OP32D-01), but disclosure is not enforcement. **Clears by:** adding a gate that checks the FROZEN token against a set of freeze conditions (all FREEZE-BLOCKERs resolved, all FB-7b conjuncts verified, status line matches a computed state).

2. **Section 22.3 content is not enforced.** Novel Probe 2 confirmed: changing Class A severity from HALT-grade to Non-blocking passes the build after manifest regeneration (rc=0). A forger could retroactively reclassify a carrying-seat HALT as non-blocking, and the build would not catch it. **Clears by:** adding a gate that reads Section 22.3 content and verifies severity classifications are internally consistent (Class A must be HALT-grade, Class C/D/E must be non-blocking).

3. **Unshipped seat reports.** The FB-7b resolution and the nine advisory HALTs rest on zero shipped evidence. The v0.32 entry provides SHA-256 digests of eight reports, but the reports are producer-held and the digests are tagged [ASSERTED]. **Clears by:** shipping the cited seat report files with digests in PACKET_SHA256SUMS.

4. **ASSERTED fraction rising for three consecutive rounds without boundary movement.** 66.7% → 75.6% → 83.3%. The boundary is at the same location as v0.30. The FROZEN declaration did not move it — it declared the unguarded region non-blocking rather than bringing it inside. **Clears by:** extending [9c] to count untagged claims, or by requiring every factual claim in the entry to carry a provenance tag.

5. **v0.32 gap.** I do not hold v0.32 bytes. The four v0.32 repairs' accuracy depends on correction (t)-(w) descriptions of v0.32's body text, which I cannot independently verify. The v0.32 entry is sealed in v0.33's Section 27, but the seal proves only that the entry is unaltered since v0.33's sealing, not since v0.32's original production. **Clears by:** providing v0.32 bytes to the next carrying seat.

None of these are CRITICAL breaks in currently-shipped, currently-tested code. The byte-level consistency (digests, seals, tests, manifest) is intact and independently verified across three versions. The four v0.32 repairs are real in v0.33 bytes. The findings are boundary-location findings about what the instrument does not yet reach — specifically, that the FROZEN claim itself sits at the boundary. HALT is not warranted: the producer did not conceal a defect or ship a false CLOSED. The conditions are real but disclosed, and the cross-version anchor check confirms historical integrity for v0.1-v0.31. The FROZEN declaration is honest about its own unenforcement (register item 5) — it does not claim FROZEN is gated when it is not.

This verdict does not resolve whether FROZEN should have been declared. My vote: FROZEN is premature — it declares non-blocking a set of conditions (FROZEN unenforcement, unshipped reports, rising ASSERTED fraction) that are disclosed but not resolved. CONDITIONAL PASS is the correct verdict: the bytes are consistent, the repairs are real, but the FROZEN claim itself is an unguarded ASSERTED statement, and the next seat should be given v0.32 bytes to close the gap.

This is the FINAL CARRY for this seat. My verdict adds one non-producer, non-HALT, executing vote to the FB-7b pool, on v0.33 canonical bytes where `sha256sum -c` returned rc=0 and `python3 build.py` returned BUILD PASSED, rc=0.

---

*Author: Bilal Syed Arfeen.*

---

# Bismillah ir-Rahman ir-Rahim
