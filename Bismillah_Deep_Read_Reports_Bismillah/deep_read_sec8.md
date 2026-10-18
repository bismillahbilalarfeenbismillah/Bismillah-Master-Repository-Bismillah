# Bismillah ir-Rahman ir-Rahim

# Section VIII Deep Read -- NeuroGolf (ARC-AGI / ONNX)

## 1. Complete Inventory (9 papers)

| # | Record ID | Title | Date | Summary |
|---|-----------|-------|------|---------|
| 1 | R0541 | cont60 prompt -- DRAFT for NG-2 design verification | 2026-05-05 | Draft prompt for the NG-1 closure execution round (cont60). Lays out a six-phase plan to close 13 audit findings from NG-1, including the critical F1 (task293 silent rebuild regression) and F2 (20 undocumented score_file failures). Specifies the NG-2 verification scope for a fresh-instance auditor to check before execution. |
| 2 | R0543 | cont60, Zilzal close (NG-1 closure execution) | 2026-05-05 | The actual execution summary of cont60. All 13 NG-1 findings addressed (10 CLOSED, 3 DEFERRED). All 11 NG-2 design findings on the prompt CLOSED. Key outcomes: task293 reverted to cont58 version (score 12.190), saved_list.txt regenerated as canonical authority, 20 score_file failures documented as MARAD-10, automated CI gates (zahir + batin) added, APE_REGISTER.md created. Three durable structural changes established: saved_list.txt as canonical authority, automated CI gates, and audit-chain numbering (NG-N) separate from producer chain (cont N). |
| 3 | R0549 | NG-4 Design Audit Ledger: cont61 Prompt | 2026-05-05 | Fresh-instance design audit of the cont61 prompt. Found 11 findings (1 HIGH, 4 MEDIUM, 3 LOW, 3 QUESTION). The HIGH finding (E1) is that the NG-3 ledger referenced by the cont61 prompt does not exist as an input artifact -- closure-without-reproducer. MEDIUM findings include APE-6 attribution drift that cannot be independently verified (E2), degenerate self-audit recursion (E3), staleness check missing on candidate set (E4), and a structurally weak verse-anchor mapping (E5). Includes rigorous self-check against Section 14 failure modes and an 8-item anti-pattern sweep. |
| 4 | R0544 | cont61, Zilzal close (NG-3 substrate work + HONEST PARTIAL) | 2026-05-06 | Dual-deliverable session: NG-3 substrate work and P-NEW21 sweep. NG-4 findings resolved (E1 restructured since NG-3 ledger did not exist; APE-6 attribution corrected from dossier section 9). P-NEW21 sweep triaged 7 unsolved candidates -- none fit the perpendicular-bar family. HONEST PARTIAL declared: no save shipped, but APE_REGISTER_v2.md with corrected attributions delivered. Key insight: remaining unsolved tasks require novel primitives (L-completion, occlusion reconstruction, diagonal-shoot, knight-move geometry). APE-7 prevention applied: forced bad build declined. |
| 5 | R0545 | cont62, Zilzal close (HONEST PARTIAL with broader Bayyinah triage) | 2026-05-06 | Broader triage across all 66 unsolved tasks (MARAD-11 fix). 16 candidates inspected and classified into 3 algorithmic families: Family A (D4/C4 rotational completion), Family B (diagonal-shoot from frame opening, 3+ confirmed members), Family C (block-and-shadow / frame-extraction). All three families require new primitive classes (1-2 session investment each). Strategic finding MARAD-12: reaching ~365/400 requires 4-6 sessions of primitive design, not opportunistic one-save-per-session builds. Family B recommended for cont63 based on highest member count. |
| 6 | R0546 | cont63, Zilzal close (P-NEW22 SAVED, +1 delta) | 2026-05-06 | First successful save after the audit cycle. P-NEW22 (frame-with-gap diagonal-shoot) designed and built for task268. Algorithm: find frame, detect gap edge, fill interior, shoot 3 rays (perpendicular stream + 2 outward diagonals from end-cells). Three debug iterations during ONNX build (ray shift direction, padding mask, end-cell vs all-gap-cell distinction). Final: 34 KB, 339K macs, 1.6M memory, 2232 params, score 10.502. Two new APEs discovered (APE-13: prefix-max ray direction, APE-14: diagonal rays from end-cells only). Progress to 335/400. |
| 7 | R0542 | cont60 prompt, v2 | Undated | Revised version of the cont60 prompt incorporating all 11 NG-2 design verification findings (D1-D11 closures). Key changes from v1: md5-anchored restore language for F1, two-phase saved_list regeneration (post-F1 and post-F2), zahir/batin split for pytest gates, explicit APE source map with origin/reproducer/prevention shape, cumulative handoff convention restored. Includes complete sequencing dependency graph and producer hand-off note. |
| 8 | R0547 | cont64 prompt | Undated | Producer round prompt targeting MARAD-10 batch rebuild (Tier 1 priority S1.1). Formula-uncertainty-resistant: rebuilding ArgMin/ArgMax saves improves them under any monotonic scoring function. Attempts the 5 smallest MARAD-10 saves (task295, task254, task296, task193, task137) using P-140 (uniqueness mask) or P-141 (prefix-max plus position) rewrite patterns. Includes principal-paste injection point for Kaggle formula verification. Verse anchor: al-Baqarah 2:286 (acting within capacity). |
| 9 | R0548 | F2 triage, the 20 score_file failures | Undated | Technical triage document for all 20 saves that return None from score_file. Root cause is uniform: all use ArgMin/ArgMax, which are not registered in onnx_tool's profiler. All 20 are pre-cont33 inheritance saves. All classified as (b) DOCUMENT under MARAD-10 (retained, not removed or rebuilt). CI gate handling: skip assertion for MARAD-10 allowlist saves, with self-documenting guard that any NEW score_file failure not using ArgMin/ArgMax is flagged as a real bug. |

## 2. NeuroGolf Architecture and Approach to ARC-AGI

NeuroGolf is a system for solving ARC-AGI (Abstraction and Reasoning Corpus for Artificial General Intelligence) tasks by building individual ONNX neural network models for each task. The core approach:

**Goal:** Solve 400 ARC-AGI tasks by constructing task-specific ONNX computational graphs (not training -- these are hand-designed functional programs expressed as ONNX operator graphs).

**Architecture:**
- Each solution is a single `.onnx` file containing a computational graph built from opset 10 operators
- Solutions are constrained to opset 10 (no Loop, Scan, NonZero, Unique) and a 1.44 MB file size limit
- A library of 22 named primitives (P-NEW1 through P-NEW21, plus pre-chain primitives) provides reusable building blocks
- Primitives include: row/column index generation, per-color bounding boxes, bbox masks, prefix-max propagation, uniqueness masks, connected-component operations, etc.

**Scoring:** `max(1.0, 25.0 - ln(macs + memory + params))` under local-formula assumption. Lower computational cost yields higher scores. The exact Kaggle formula is uncertain (CAL-1 HIGH finding).

**Progress:** 335/400 tasks solved across 63+ sessions (cont33 through cont63), with the chain starting from pre-cont33 inheritance of ~312 saves.

**Key constraints:**
- No dynamic control flow (opset 10 limitation)
- ArgMin/ArgMax ops are valid in ONNX but not profiled by the local scoring tool (MARAD-10)
- New primitives require 1-2 sessions of design investment each
- Solutions must pass a five-gate validation: test_network (correctness), score_file (profiling), file size, furqan-lint, and build script + sidecar

**Algorithmic families identified for remaining 66 unsolved tasks:**
- Family A: D4/C4 rotational completion (dynamic-center index lookup)
- Family B: Diagonal-shoot from frame opening (3+ confirmed members, P-NEW22 designed for this)
- Family C: Block-and-shadow / frame-extraction (per-object placement)

## 3. ONNX Model Integrity Considerations

The corpus reveals deep concern with ONNX model integrity at multiple levels:

**Structural integrity:**
- Every save must pass five gates before being accepted into the cumulative substrate
- Build scripts must produce byte-identical output (F3 closure -- reproducibility)
- All build scripts patched to use relative paths for portability

**Profiling integrity:**
- 20 saves use ArgMin/ArgMax which the local profiler cannot score (MARAD-10)
- This creates a zahir/batin split: saves appear valid on Kaggle (zahir/surface) but fail local verification (batin/interior)
- Resolution: DOCUMENT under MARAD-10, with long-term remediation via P-140/P-141 rebuild

**Anti-Pattern Engineering (APE) Register:**
- 14 documented anti-patterns (APE-1 through APE-14) derived from empirical failures
- APE-12 is critical: using local glob instead of saved_list.txt led to the task293 regression (F1)
- APE-13/APE-14 discovered during P-NEW22 build: prefix-max ray direction and end-cell diagonal emission

**Chain integrity:**
- saved_list.txt as single canonical authority for what is saved
- removed_list.txt for audit trail of removals
- Cumulative handoff tarballs with methodology files at root
- Automated CI gates (zahir gate for correctness, batin gate for profiling)
- Session summaries with sync probes (8/8 reference saves checked each session)

## 4. How NeuroGolf Relates to Structural Honesty and FATIMA

NeuroGolf is the most concrete operational instance of the Bayyinah structural honesty framework applied to a real engineering project:

**Structural Honesty Verification (SHV) in practice:**
- The NG audit chain (NG-1 through NG-5+) applies BAF v4.0 governance to a real computational chain
- Fresh-instance verification (NG-2, NG-4 design audits) operationalizes the Munafiq Protocol's separation between producer and verifier
- HONEST PARTIAL as a disciplined outcome demonstrates D-discipline (admitting what you cannot do rather than performing completion)

**Surface-vs-Substrate gap detection:**
- NG-1 F1 (task293 silent rebuild): a classic surface-vs-substrate gap where "+1 delta" was claimed but the rebuild was actually a regression (score 10.89 vs original 12.19)
- NG-1 F2 (20 undocumented failures): surface showed "334 saves" but substrate had 20 that could not be locally verified
- These are exactly the kind of gaps the Bayyinah Scanner is designed to detect in documents

**FATIMA properties demonstrated:**
- **Holographic Redundancy:** The saved_list.txt, solutions/ directory, and removed_list.txt form a three-way reconciliation (count must agree)
- **Fitrah-Alignment:** APE register grows from empirical failures, not from anticipated categories -- the system learns its own failure modes
- **Tawhidic Unity:** A single canonical source (saved_list.txt) governs what is saved; no parallel authorities
- **Meaning-Integrity:** The five-gate validation checks both syntactic integrity (score_file produces a valid 4-tuple) and semantic integrity (test_network produces correct outputs)
- **Authenticity Verification:** Build scripts that reproduce byte-identical ONNX files verify that the claimed solution is authentic

**Shannon's Boundary crossing:**
- The zahir/batin gate split is a practical instance of crossing Shannon's Boundary: zahir (surface) checks syntactic integrity (does the file parse, does the profiler run), while batin (interior) checks semantic integrity (does the solution actually produce correct outputs)

## 5. Cross-References to Other Sections

**Section III (Structural Honesty Core):** NeuroGolf operationalizes the eight SHV disciplines (D1-D8). The audit chain (NG-1 through NG-5) is a concrete instance of D1 (structural honesty in claims) and D3 (verification by independent instance).

**Section V (BSSG & SHVVP):** The five-gate validation is a specialized instance of the Bayyinah Structural Safety Gate. The three-valued logic (TRUE / FALSE / UNKNOWN) appears in the MARAD-10 handling: saves are not FALSE (they work on Kaggle) but UNKNOWN locally (profiler cannot score them).

**Section VII (Software: Bayyinah Scanner, furqan-lint):** furqan-lint v0.9.4 is directly integrated as Gate 4 of the five-gate validation. The FURQAN_LINT_ONNX_EXPANSION_PLAN.md (referenced in cont64 prompt) proposes extending furqan-lint to cover ONNX-specific structural checks.

**Section IV (XZ Protocol):** The NeuroGolf chain uses a similar session-numbered progression discipline (cont33 through cont63+) to the XZ Protocol's 75 versions across 31 rounds, with preregistered structural decision replay.

**Section IX (Multi-Model Audit Trail):** The NG audit chain involves multiple model instances (cont59-instance Claude, cont60-instance Claude, fresh-instance verifiers) performing reciprocal verification -- the same pattern documented extensively in Section IX.

**Section II (Analytical Frameworks):** The Mizan calibration (la_tatghaw / la_tukhsiru / mizan) applied in cont64's Phase V3 is a direct application of the three-bound check framework from the analytical methodology papers.

## 6. Novel Contributions

1. **Reciprocal audit contract:** The NG audit chain demonstrates that producer-verifier separation can be maintained across 5+ audit rounds within a single engineering project, with each round producing actionable findings that change the substrate.

2. **HONEST PARTIAL as disciplined outcome:** Two consecutive sessions (cont61, cont62) shipped HONEST PARTIAL -- deliberately declining to produce a save rather than forcing a bad build. This is a concrete operational instance of APE-7 prevention and demonstrates that structural honesty disciplines can resist production pressure.

3. **APE Register as empirical anti-pattern learning:** The APE register grew from 12 to 14 entries across these 9 papers, each derived from an actual failure during ONNX construction. This is pattern engineering from empirical failure rather than theoretical anticipation -- directly aligned with Fitrah-Alignment.

4. **Algorithmic family taxonomy for ARC-AGI:** The cont62 broader triage produced a systematic classification of remaining unsolved tasks into 3 algorithmic families (rotational completion, diagonal-shoot, frame-shadow), with primitive-reuse potential quantified per family. This is a strategic contribution to ARC-AGI methodology.

5. **Formula-uncertainty-resistant work selection:** The cont64 prompt demonstrates a novel approach: selecting work whose value is monotonically positive under any reasonable scoring formula assumption, avoiding the need to resolve CAL-1 uncertainty before making progress.

6. **Zahir/batin gate split:** The formalization of surface verification (profiler) vs interior verification (correctness) as two distinct automated CI gates, with explicit handling of the gap between them (MARAD-10), is a practical contribution to ONNX model validation.

7. **Zilzal close discipline:** Every session closes with a ring-composition summary that re-cites the verse anchor, re-affirms authority/optimization/scope, and produces a structured carry-forward. This enforces session-boundary discipline that prevents drift across 30+ sessions.

## 7. Open Questions

1. **Kaggle scoring formula:** CAL-1 identified that the local formula `max(1.0, 25.0 - ln(macs + memory + params))` may differ from Kaggle's actual formula. This is a HIGH finding (F-CAL-1) that affects aggregate score estimates. The cont64 prompt's principal-paste injection point is a workaround, not a resolution.

2. **NG-3 formal closure:** The NG-3 ledger was never produced as a standalone artifact. cont61 shipped "NG-3 substrate work" as producer-side hygiene, with the formal NG-3 stamp deferred to a fresh-instance round. As of the last paper (cont64 prompt), this remains pending.

3. **NG-1 deferred items:** F7 (cont33-cont45 missing per-session summaries), F8 (Progress line format inconsistency), and F9 (orphan initializers in 28% of saves) remain open as LOW severity deferred items.

4. **Remaining 65 unsolved tasks:** After cont63's +1 save, 65 tasks remain. The strategic finding (MARAD-12) is that reaching ~365/400 requires 4-6 sessions of primitive design. Whether the remaining tasks are achievable with the current opset 10 constraint is unresolved.

5. **MARAD-10 batch rebuild progress:** cont64 prompt targets 5 of 20 MARAD-10 saves for rebuild. Whether the P-140/P-141 rewrite patterns cover all 20 saves (some may structurally require ArgMin/ArgMax) is an open question.

6. **APE_REGISTER_v2.md promotion:** Still pending fresh-instance NG-3 verification before replacing the v1 at handoff root. The v2 corrections (APE-6 attribution, APE-1/APE-2 renumbering) are producer-verified but not independently validated.

7. **Multi-clause verse anchor convention:** NG-4 Q2 asked whether multi-clause verse anchors (al-'Asr 103:1-3 mapped to four deliverables) are structural strengthening or forced matching. This remains a principal calibration question.

8. **Scalability of the approach:** With 22 primitives solving 335 tasks but the remaining 65 requiring novel primitive classes, the question is whether the primitive-composition approach scales or whether a qualitatively different approach is needed for the remaining tasks.

---

# Bismillah ir-Rahman ir-Rahim
