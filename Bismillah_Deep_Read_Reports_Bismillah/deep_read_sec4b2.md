# Bismillah ir-Rahman ir-Rahim

# Deep Read Report -- Section IV-b2: XZ Protocol Audit Infrastructure & Empirical Reviews

**Papers read:** 17 (all read directly, not by agent)
**Section:** IV. XZ Protocol (second half of batch b)
**Scope:** Adversarial audit reports (R3-R4), findings indices, defect closure assessments, executable code modules, data artifacts, and the v0.75 frozen deposit

---

## Paper-by-Paper Analysis

### 0567_R0194 -- XZ Empirical R3 GPT-5.6 Sol Absorption Verification Report
- **Type:** Adversarial audit report (R3, S03 seat)
- **Verdict:** HALT
- **Key findings:** 3 HIGH -- (1) R15 recurrence assertion 25/25 unverified from shipped data, (2) migration population excludes 53 description-level Class A rows yielding 102 vs 155 universe, (3) migration classifier not reproducible from shipped code. 4 of 9 R2 findings closed, 4 partial, 1 open.
- **Significance:** Demonstrates that even with multiple rounds of repair, the empirical paper's core quantitative claims carry unresolved verification gaps. The 102 vs 155 population discrepancy is structurally significant -- it changes layer counts materially.

### 0568_R0195 -- XZ Empirical R4 GPT-5.6 Sol Final Audit Report
- **Type:** Adversarial audit report (R4, S03 seat)
- **Verdict:** HALT
- **Key findings:** 2 remaining HIGH -- R15 still unverified, migration population still incomplete. New finding: shipped classifier does not exactly reproduce shipped CSV (21 rationale cells differ). Sensitivity analysis shows the 155-row universe changes all layer counts materially.
- **Significance:** After four rounds of adversarial review, the XZ Empirical paper still cannot close its two central quantitative claims. The persistence of these findings across rounds is itself empirical evidence for the H=1.0 recurrence thesis.

### 0653_R0157 -- coverage.csv
- **Type:** Data artifact -- complete coverage matrix
- **Content:** 220 rows covering rounds 0-36, versions v0.13-v0.74, across model families from Anthropic, OpenAI, Google, Zhipu, Moonshot, Perplexity. Each row maps a report file to its round, version, seat, model family, role, mode, verdict, severity counts, finding count, and era label.
- **Significance:** The single most comprehensive map of the entire XZ audit program -- 220 distinct audit executions across 6+ vendor families, 31+ rounds, 60+ versions.

### 0654_R0164 -- Prepublication Peer Review of XZ Protocol v0.71
- **Type:** Independent technical peer review (GPT-based, not human)
- **Verdict:** HALT / Major Revision -- do not publish v0.71 as FROZEN
- **8 publication-blocking findings:**
  1. CRITICAL: v0.71 simultaneously claims FROZEN, PENDING RE-CARRY, FB-8 OPEN, and "draft candidate" -- self-contradictory status under its own rules
  2. CRITICAL: R28 cross-seat triage materially misbound -- 2 of 37 findings disappear, convergence groups bind wrong IDs to wrong propositions
  3. CRITICAL: v0.71 is not a substantive R28 repair -- C-suffix defect, register generator crash, Gate [13] fail-open, hardcoded summary all remain in current bytes
  4. HIGH: Section 25 test-count claims falsifiable (22 vs 29 source-frame, 30 vs 18 control-graph)
  5. MAJOR: Goedel confinement not formally established -- Bearers 4, 5, 7 not Goedel-coupled; finite syntactic/witness predicates
  6. MAJOR: H=1.0 Hurst exponent degenerate on constant series (0/0 R/S), Laplace 23/24 assumes implausible exchangeability
  7. HIGH: Methodology's sentence-level provenance-tag rule fails in freeze entry
  8. HIGH: Independent witness provenance not cryptographically authenticated
- **Critical insight:** "The most consequential observation is almost the inverse of the current conclusion: the R28 process did what a rigorous audit process is supposed to do. It caught substantive errors that a 186/186 green build did not catch. Those errors should now be corrected, not converted into a theorem of irreducibility."
- **Significance:** One of the most technically sophisticated reviews in the entire corpus. Establishes that the protocol's own review infrastructure caught the very thing it was designed to catch.

### 0655_R0168 -- r25_findings_index.json
- **Type:** Structured findings index for Round 25
- **Content:** 4 seats (Kimi K3, GPT-5.6 Sol x2, Gemini 3.1 Pro), version 0.66. 4 convergence groups (all CLOSED), 24 unique findings NOTED. Not all-HALT (1 carrying HALT, 2 advisory HALT, 1 advisory non-HALT).
- **Convergence surfaces:** CI-8 severity fidelity, format regex prefix-only, FB-7b trajectory gap, tagging discipline incomplete (Goedel surface)

### 0656_R0169 -- r27_findings_index.json
- **Type:** Structured findings index for Round 27
- **Content:** 4 seats, version 0.68, all_halt=true. 7 convergence groups (all CLOSED), 21 unique findings NOTED, 35 total findings.
- **Convergence surfaces:** Gate [13] vacuous/skip-as-green, Section 0.1 stale + FB-7b trajectory, Gate [13] logic defects, R26 convergence misbound, CRITICAL->HIGH silent remap, gate count overstates (256 vs 240), unmanifested files
- **Significance:** All 7 convergence groups CLOSED. Gate [13] required complete rebuild (bidirectional, severity-aware, fail-closed). CRITICAL is now a valid severity, not silently downgraded.

### 0657_R0170 -- v0.72 Defect Closure Assessment
- **Type:** R29 defect closure audit (Gemini-based)
- **Verdict:** v0.72 does NOT close all R28 defects
- **Closed (7):** C-suffix, Gate [13] fail-closed, Gate [13] derived summary, register generator graceful degradation, R28 reports in-packet, boundaries.json version, terminal-line gate
- **Remaining:** String 3 (stale Section 0.1), String 4 (Gates [10i]/[2f] manufacturing false claims), String 6 (pattern over-capture, dispatch fidelity)
- **Key insight:** Gates [10i]/[2f] *actively create* the defects they detect -- the verification layer manufactures the defects it is meant to prevent. This is Shannon's Boundary made concrete.

### 0658_R0171 -- XZ Protocol v0.73 Audit Results
- **Type:** R30 gate-manufactures-defect closure
- **Repair:** Gate [2f] enforcement relaxed to accept version within 3 of current VERSION. Section 0.1 entry range corrected. Closes F-S04-70-09 and F-S04-70-10.

### 0659_R0172 -- XZ Protocol v0.75 FROZEN -- Zenodo Deposit
- **Type:** README for the frozen Zenodo deposit
- **Content:** Complete evidence chain for 25 rounds. H=1.0 across R7-R31. "The artifact contains known defects. The defects are the finding."

### 0660_R0173 -- reports.csv
- **Type:** Structured CSV of all 220 audit reports with SHA-256 hashes, verdicts, severity counts, era labels.

### 0661_R0181 -- summary.json
- **Type:** Aggregate statistics
- **Key numbers:** 199 reports, 832 findings, 812 unique IDs. Family: Anthropic 86, OpenAI 62, Zhipu 23, Google 21, Moonshot 5, Perplexity 1. Severity: HIGH 365, MEDIUM 232, LOW 127, CRITICAL 62, INFO 41. Verdicts: HALT 147 (73.9%), CONDITIONAL PASS 22, PASS 4. 32 rounds, 63 versions (v0.13-v0.74).

### 0662_R0183 -- test_xz_protocol_condition_a.py
- **Type:** Adversarial test suite for Condition A
- **Content:** 7 test classes covering disposition vocabulary, baseline profile completeness, accept/reject/indeterminate logic, dual-evaluability, input validation, supply-chain decoy scenarios. Key: A-REJECT dominates A-INDETERMINATE (parallels FALSE > UNKNOWN). NOT_APPLICABLE on mandatory yields INDETERMINATE (F-SOL-XZ-3). String decisions rejected.

### 0663_R0186 -- test_xz_protocol_kernel.py
- **Type:** Exhaustive 3^5=243 kernel test suite
- **Content:** Complete enumeration of all 243 truth-value combinations across five conjuncts. Verifies DENY_FALSE and DENY_UNKNOWN never collapse (CR-3, XZ-S9). No caller-supplied decisions. Reason codes track which conjuncts are FALSE.
- **Significance:** The mathematical core of the Bayyinah framework -- executable proof that the five-conjunct kernel is complete and correct.

### 0664_R0191 -- XZ Corpus R4 S03 GPT Absorption Verification Report
- **Type:** R4 audit of the XZ Structural Honesty Audit Corpus v1.2
- **Verdict:** HALT (0 CRITICAL / 1 HIGH / 1 MEDIUM / 4 LOW)
- **New HIGH:** v0.5 extractor can assign neighboring finding's locus -- 1500-char scan crosses finding boundaries. Minimal reproduction deterministic. CSV contains sequences consistent with cross-finding shift.
- **All aggregates pass:** 832 findings, 812 unique IDs, 199 reports. Class A partition correct (102 R7-R31, 136 corpus-wide).
- **Significance:** The audit process extends to the corpus itself. The locus cross-assignment is a data-integrity regression where visible parsing defects were replaced by silent wrong assignments.

### 0665_R0197 -- xz_protocol_boundaries.json
- **Type:** Machine-readable disclosed boundaries/limitations register
- **Content:** 35 items at v0.72. Includes regex limitations, seal gaps, persistent HALTs with exceptions, FB-8 governance OPEN, BSSG fabrication class, and critically: [2g] structurally forbids FB-7b resolution.
- **Significance:** Item 35 is the empirical Goedel sentence -- the protocol's own governance rule makes it impossible to close one of its own freeze-blockers.

### 0666_R0198 -- xz_protocol_closure_gate.txt
- **Type:** Executable closure-claim verification gate
- **Key design:** Evaluates closure claims against protocol body *with Section 27 amendment record removed* -- a closure cannot be satisfied by the log entry that asserts it. v0.12 predecessor searched for corrected form rather than defective form, returning PASS when fix was absent.
- **Significance:** Anti-circularity made executable. The Section 27 exclusion rule is the most elegant structural integrity mechanism in the codebase.

### 0667_R0199 -- xz_protocol_condition_a.py
- **Type:** Executable Condition A disposition function (production code)
- **Content:** Four-label vocabulary, six boundary strata, 17 baseline checks, dominance rule, six frozen fairness rules. Dual-evaluability and primary seam divergence detection.
- **Key properties:** String inputs rejected everywhere. NOT_APPLICABLE on mandatory yields INDETERMINATE. Generator consumption prevented (M-6). Provenance token as disclosed accident guard.

---

## Synthesis

### The XZ Protocol as Self-Referential Empirical Program

1. **Scale:** 199 reports, 832 findings, 220 coverage entries, 31+ rounds, 6+ families, 63 versions. This is a sustained empirical observation program.

2. **H=1.0 in context:** The prepublication review correctly identifies the Hurst exponent as degenerate on a constant series. But the underlying observation -- Class A findings in 25/25 consecutive rounds -- remains the most striking empirical result. Every round that attempts to close all defects generates new ones.

3. **Goedel confinement:** The boundaries register provides an empirical instance: Gate [2g] structurally forbids FB-7b resolution. Whether this constitutes a genuine empirical Goedel sentence or a governance design defect is the open question.

4. **Gate-manufactures-defect:** Verification gates can *create* the defects they detect (R0170, String 4). This is Shannon's Boundary made concrete.

5. **Three-valued logic made executable:** The kernel (243-state exhaustive test) and Condition A (6-strata disposition) together implement the complete BSSG three-valued logic.

6. **Closure-gate anti-circularity:** Closure claims evaluated against bytes *with the amendment record removed*. Prevents self-referential closure.

---

# Bismillah ir-Rahman ir-Rahim
