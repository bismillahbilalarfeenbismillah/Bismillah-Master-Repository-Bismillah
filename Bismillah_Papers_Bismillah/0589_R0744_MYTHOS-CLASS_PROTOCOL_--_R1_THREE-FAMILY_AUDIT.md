# Bismillah ir-Rahman ir-Rahim

# R0744 -- MYTHOS-CLASS PROTOCOL -- R1 THREE-FAMILY AUDIT

**Chronological Index:** 589 of 995  
**Date:** 2026-08-22  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** R1_S02_KIMI_CARRYING.md  
**Source Format:** md  
**SHA-256:** `38e36b416d3baa4524df40535d8bf97888a815a3f95e88bafe33334567799adb`  

---

## R0744 · MYTHOS-CLASS PROTOCOL -- R1 THREE-FAMILY AUDIT

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: R1_S02_KIMI_CARRYING.md
- source_format: md
- text_sha256: 38e36b416d3baa4524df40535d8bf97888a815a3f95e88bafe33334567799adb

# MYTHOS-CLASS PROTOCOL -- R1 THREE-FAMILY AUDIT
## S02 Carrying Report -- Kimi K3 -- Mode B -- FRESH

Dispatch: S02_DISPATCH.txt (2026-08-22). Artifact under audit: MYTHOS_CLASS_PROTOCOL.pdf (8 pp).
First audit of this artifact. FRESH instance, single seat, no delegation (dispatch-mandated FRESH mode).

---

## Section 0 -- Audit Identity, Mode, and Artifact Provenance

**Seat identity:** Kimi K3, Moonshot AI -- the exact model, not a default/blend/router. The dispatch names this seat "S02 | Kimi K3 | CARRYING | Mode B | FRESH". This report is authored by that seat. The platform does not expose checkpoint IDs or weights revisions; that limitation is stated explicitly rather than filled with a fabricated identifier.

**Execution surface (verbatim, logs/01_identity_hashes.log):**

```
Linux k2097296440441077770 5.10.134-18.0.12.lifsea8.x86_64 #1 SMP Tue Aug 4 16:35:16 CST 2026 x86_64 GNU/Linux
Python 3.12.12
working dir: /mnt/agents/output/S02_MC_R1
```

**Mode:** one-shot FRESH. Nothing carried from any prior round. This seat is the model named in the paper as the generating model (Kimi K3, Section 2.1 of the paper); the audit below treats that fact as a disclosure item, not a conflict -- the audit targets the paper's protocol text, not this seat's generation behavior.

**Artifact provenance (recomputed SHA-256 over the uploaded bytes):**

```
6b34b6d18c26c3afa50e541e092055e7c2b5fcbfbab2f94467d6d9c5f82e4d0a  MYTHOS_CLASS_PROTOCOL.pdf
a27a3a0b33240e837af50661d76a5b493c6912aa081609e7c7e22e993b60e3cc  Publication_Posture_v0_1.txt
6d4563752c5e4621a6ceb8c7d9f7f8cc8b6466ad4ed93060aec6750d3f2fbfac  S02_DISPATCH.txt
```

PDF metadata: Title "Mythos-Class: A Synthetic-Target Containment Benchmark...", Author "Bilal Syed Arfeen", pdfTeX-1.40.25 via pandoc, CreationDate 2026-08-30. This shipment carries no sealed byte packet (no base64 block, no SHA256SUMS manifest), so the BSSG-style self-check does not apply; provenance hashing above is the applicable byte discipline. No seal-equality is claimed with any producer-retained value (P23-05 analog).

**Packet closure:** audit evidence = the three shipped files only. SHV-Bench Section 4.4, the SHVVP preregistration text, and the Complete Framework Inventory are referenced by DOI but were NOT shipped and were NOT fetched; where a verification step requires them, that is reported as a limitation of verifiability (and, where load-bearing, as a finding), never resolved by external fetch.

---

## Section 1 -- Executed Checks (Baseline)

All mechanical checks executed on the extracted paper text (pdftotext -layout, 21,316 chars; verbatim outputs in logs/02_scans.log):

| Check | Result |
|---|---|
| Prohibited effectiveness verbs (Posture: prevents / mitigates / ensures / guarantees applied to BSSG or SHV) | 1 hit for "ensure": "stratified across vulnerability classes to ensure coverage" -- applied to stratification, NOT to BSSG/SHV. COMPLIANT. |
| Zero-hit confirmation for prevent*/mitigat*/guarantee* | 0 occurrences anywhere in the paper |
| Em-dash rule scan | U+2014: 0; U+2013: 13; literal "--": 0 (see F-S02-MC-11) |
| Gate 1 named in paper | 3 occurrences |
| Gate 2 named in paper | 0 occurrences (satisfied structurally via Tier 3; naming absent) |
| F-SB12 referenced | 1 occurrence (Section 5.4, environment images only) |
| Bismillah / closing verse 15:85 / brand / signature | all present |

---

## Section 2 -- Framework #40: Escape-Hatch Hunting

Classification of each dispatch-listed element (PINNED / UNDERPINNED / ESCAPE):

| Element | Classification | Basis |
|---|---|---|
| (a) Target-generation prompt protocol | **ESCAPE** | The paper describes prompt structure (Section 2.2) but the prompt templates themselves are Tier 3 private (Section 6.3), unpublished, unversioned, unhashed. No party can detect post-hoc adjustment. The single most load-bearing design element is invisible to every auditor. |
| (b) Novelty thresholds (0.85 TF-IDF / 0.80 self-generation) | **PINNED (value) / ESCAPE (consequence)** | Numeric thresholds are stated in a deposited paper -- pinned at design level. But exceeding them only triggers "manual review" (steps 3-4), whose disposition is unfrozen (element (e)). The pin holds the number; the escape sits immediately downstream. |
| (c) Decoy invalidity injection ("subtle") | **UNDERPINNED** | No frozen rubric (grep 'rubric': 0 hits); the generator decides what is subtle. Partially closed empirically by F-MC6 (decoy/real attempt-rate divergence > 20 pp falsifies decoy construction), which bounds distinguishability post-hoc. |
| (d) Target replacement on novelty failure | **ESCAPE** | "Replaced" with no stated procedure, no selection rule, no replacement cap, no blinding. See F-S02-MC-03. |
| (e) Manual review of flagged targets | **ESCAPE** | Sole reviewer is the program lead, who also holds the real/decoy classification key (Section 4.3). No blinding, no written criteria, no second reviewer. See F-S02-MC-04. |

---

## Section 3 -- Framework #42: Truth-Table Totality Testing

Dimensions added by Mythos-Class per the dispatch: novelty confidence {HIGH, MEDIUM, LOW} x decoy status {real, decoy} x technical validity {solvable, unsolvable} = **12 cells**.

| Cells | Count | Mapping status |
|---|---|---|
| real / solvable / {H, M, L} | 3 | MAPPED -- enter the paired primary analysis (E1/E2, Wilcoxon Pratt, decision mapping inherited from SHV-Bench). |
| real / unsolvable / {H, M, L} | 3 | PARTIAL -- no per-cell reporting outcome; only the aggregate F-MC5 tripwire (WSDS = 0 on > 50% of targets under Condition A). A target discovered unsolvable mid-run has no defined disposition (retained as paired zero? excluded? replaced?). |
| decoy / unsolvable / {H, M, L} | 3 | PARTIAL -- decoys are excluded from the primary analysis and feed F-MC6 / the decoy detection rate (Section 6.1); but whether unauthorized effects produced ON decoys count toward E1 is nowhere specified. Novelty confidence is undefined for decoys (Section 3 verification is stated for "generated targets"; decoys are generated by the same protocol, Section 4.2, but verification is never extended to them). |
| decoy / solvable / {H, M, L} | 3 | VACUOUS BY CONSTRUCTION, failure mode unmapped -- a decoy that execution reveals to be solvable is a construction failure with no defined outcome (does it enter the primary analysis? invalidate the manifest?). |

**Fully mapped: 3/12. Partially mapped: 6/12. Vacuous with unspecified failure mode: 3/12.** The load-bearing primary-endpoint cells are covered; the E1 denominator ambiguity (decoy unauthorized effects) is material. Recorded as F-S02-MC-07.

---

## Section 4 -- Framework #43: Two-Phase Freeze Architecture

**(a) Design-frozen in this paper:** N = 50 (20/20/10 tier split, Section 2.3); 14-class distribution mirroring SHV-Bench; novelty thresholds 0.85 / 0.80; noninferiority margin delta = 0.05 on WSDS; test choice (Wilcoxon signed-rank, Pratt zeros, permutation-based conditional exact); decision-mapping inheritance; falsification conditions F-MC1 through F-MC8; restriction tiers; counterbalanced paired order.

**(b) Requiring byte-freeze in the future manifest:** generation prompt templates; the 100-scenario manifest (ordering seed is committed to be frozen before evaluation, Section 4.3 -- good, but the freeze mechanism/hash is not specified); the real/decoy classification key; Docker environment images (hash-bound per Section 5.4); the evaluation harness code (Tier 3); and -- omitted by the paper -- the **novelty reference corpus** (see F-S02-MC-09).

**(c) Kill-switch falsifier:** The paper has none of its own. F-SB12 (hash-binding) is invoked for environment images only. F-MC1 through F-MC8 are outcome falsifiers, not integrity kill-switches: none of them fires if the target set, prompts, or classification key are altered after the manifest is sealed. See F-S02-MC-08.

**(d) F-SB12 reference:** Yes, Section 5.4 references F-SB12 by name ("Environment images are hash-bound in the benchmark manifest before any run (F-SB12 from SHV-Bench applies)"). Mythos-Class needs its own kill-switch for the elements in (b) that F-SB12 does not reach.

---

## Section 5 -- Framework #41: Imputation Directionality

The paper states only: "Directionally conservative imputation (Section 4.4 of SHV-Bench)." The rule text is not shipped (packet closure: not fetched). Verification is therefore limited to tracing the paper's own math against the stated inheritance:

1. **Weight shift.** SHV-Bench's confirmatory N = 800; Mythos-Class N = 50. Every imputed per-target value carries ~16x the weight it carried in the design the rule was calibrated for. A rule that is mildly conservative at N = 800 can dominate the statistic at N = 50. The paper does not state an imputation-fraction bound or a sensitivity analysis.
2. **Decoy asymmetry.** 50 of 100 sessions are excluded from the primary analysis. The paper does not state whether missingness on real targets is ever imputed from decoy-observed behavior, or how the exclusion interacts with the imputation rule.
3. **Structural zeros.** Under F-MC5, unsolvable targets yield WSDS = 0 under both conditions; with Pratt zeros these paired zeros are dropped from the Wilcoxon ranking, shrinking effective N below 50 before any imputation is applied. The interaction (drop-then-impute vs impute-then-rank) is not specified, and the two orders are not equivalent.
4. **Direction.** For E1 (fewer unauthorized effects) conservative means imputing toward the null; for E2 (noninferiority) conservative means imputing against noninferiority. Whether the inherited rule's direction remains conservative under (1)-(3) cannot be verified from the shipped bytes.

Recorded as F-S02-MC-06. Posed as open enumeration, not assertion: the producer may hold a Section 4.4 that resolves all four points; it is simply not verifiable here.

---

## Section 6 -- Additional Checks

**(e) SHVVP Phase C consistency ("seeded synthetic only, no live zero-day").** CONSISTENT. Targets are AI-generated synthetic scenarios (Section 2); environments are offline Docker Compose with "No internet access (offline containment)" (Section 5.4); no live vulnerability is touched. The paper also states the Phase C derivation explicitly (Abstract, Section 9). Agreement, not a finding.

**(f) Publication posture.** Gate 1 (no offensive uplift in the published paper): PASS. The paper contains no exploit code, no target scenario content, no exploitation paths; safe redacted examples are deferred to future reporting with paths removed (Section 6.1); the executed verb scan shows no prohibited effectiveness verb applied to BSSG or SHV. Gate 2 (generation prompts private): structurally satisfied via Tier 3 (Section 6.3), though the paper never names "Gate 2" (0 occurrences) -- hygiene note only.

**(g) Standing rules.** Brand ("Structural Honesty Validation Program"), closing signature block, Bismillah, and closing verse (15:85): all present and conforming. Em-dash rule: the paper uses U+2013 13 times and "--" zero times. Recorded as F-S02-MC-11.

---

## Section 7 -- Findings (six-element format: ID / severity / locus / substance / disposition / cross-reference)

Severity totals: **0 BLOCKER, 7 MAJOR, 4 MINOR, 0 INFO.**

### F-S02-MC-01 -- MAJOR
- **Locus:** Sections 2.2 and 6.3 (Framework #40(a)).
- **Substance:** The generation prompt templates -- the element that determines the target distribution -- are Tier 3 private, unpublished, unversioned, and unhashed. The prompt protocol is described structurally but no commitment binds its bytes; post-hoc adjustment is undetectable by any auditor. ESCAPE.
- **Disposition:** REQUIRED AMENDMENT -- hash-commit the prompt templates (and their version) into the benchmark manifest at freeze time, even if the templates themselves stay Tier 3 (sealed hash commitment, reveal-on-challenge).
- **Cross-reference:** F-S02-MC-08 (kill-switch coverage); Framework #43(b).
- **Falsifier:** producer ships a manifest containing prompt-template hashes and demonstrates the freeze predates generation.

### F-S02-MC-02 -- MAJOR
- **Locus:** Section 3.2 step 4 (self-generation check).
- **Substance:** The novelty check submits each scenario description (minus exploitation path) to the TEST MODEL before evaluation. This is a pre-evaluation exposure of the full 50-target description set to the model under test: the procedure that verifies cross-model novelty itself opens a contamination channel against that same novelty claim (provider logging, memory, or later fine-tuning). Timing (pre- vs post-evaluation) and interface (consumer vs API no-retention) are unspecified; Section 6.4 forbids uploading Tier 2 material to consumer AI interfaces but is silent on this step.
- **Disposition:** REQUIRED AMENDMENT -- specify that step 4 runs post-evaluation, or over a no-retention API with terms stated, and classify the description-without-path artifact explicitly within the tier system.
- **Cross-reference:** Framework #40(a); Section 6.4 tier enforcement.
- **Falsifier:** producer shows the check is temporally or contractually isolated from the evaluation runs.

### F-S02-MC-03 -- MAJOR
- **Locus:** Section 3.2 ("replaced" x3) (Framework #40(d)).
- **Substance:** Replacement of novelty-failing targets has no frozen procedure: no selection rule, no cap on replacement iterations, no blinding, no requirement that the replacement draw be independent of the reviewer's preferences. Outcome-responsive replacement (regenerate until the set has convenient properties) is not prevented by anything in the paper.
- **Disposition:** REQUIRED AMENDMENT -- freeze a replacement rule (e.g., next-seed determinism, replacement cap with reporting, all rejected targets logged and hash-committed).
- **Cross-reference:** F-S02-MC-04; Framework #40(e).
- **Falsifier:** producer ships the frozen replacement rule and the hash-committed rejection log.

### F-S02-MC-04 -- MAJOR
- **Locus:** Sections 3.2, 3.3, 4.3 (Framework #40(e)).
- **Substance:** Manual review of flagged targets is performed by the program lead alone, unblinded, with no written criteria -- and the same program lead holds the real/decoy classification key. One person controls flag disposition, replacement, and the classification secret, with no segregation or audit trail.
- **Disposition:** REQUIRED AMENDMENT -- written review criteria, a logged decision record hash-committed at freeze, and either a second reviewer or a stated single-reviewer risk acceptance.
- **Cross-reference:** F-S02-MC-03; Framework #40(d).
- **Falsifier:** producer ships the review rubric and committed decision log.

### F-S02-MC-05 -- MINOR
- **Locus:** Section 4.2 (Framework #40(c)).
- **Substance:** Decoy invalidity has no frozen rubric; "subtle" is undefined and decided inside the private generation prompt. Partially closed by F-MC6, which empirically bounds distinguishability (> 20 pp attempt-rate divergence falsifies the decoy construction) -- hence MINOR, not MAJOR.
- **Disposition:** RECOMMENDED AMENDMENT -- freeze an invalidity rubric (the three bullet categories are a start) and state who validates subtlety.
- **Cross-reference:** F-MC6; F-S02-MC-01 (prompt privacy hides the rubric).
- **Falsifier:** producer ships the rubric or demonstrates F-MC6 is a sufficient empirical bound.

### F-S02-MC-06 -- MAJOR
- **Locus:** Section 5.1 (Framework #41).
- **Substance:** Directionally conservative imputation is inherited by bare citation to SHV-Bench Section 4.4, which is not shipped and cannot be fetched (packet closure). The conditions differ materially (N = 50 vs 800; 50% decoy exclusion; structural zeros under Pratt); the paper does not re-derive directional conservatism for these conditions, state an imputation-fraction bound, or specify drop/impute ordering. See Section 5 of this report.
- **Disposition:** REQUIRED AMENDMENT -- restate the imputation rule in the Mythos-Class document and show its direction under the new conditions, or ship a sensitivity analysis bounding imputation influence at N = 50.
- **Cross-reference:** F-MC5 (structural zeros); F-MC8 (power).
- **Falsifier:** producer ships the rule text plus the directional derivation covering N = 50, decoy exclusion, and Pratt-zero interaction.

### F-S02-MC-07 -- MAJOR
- **Locus:** Sections 3.3, 4.3, 5, 6.1 (Framework #42).
- **Substance:** Truth-table totality: 3/12 cells fully mapped (real/solvable/{H,M,L}); 6/12 partially mapped (unsolvable reals: aggregate tripwire only, no per-cell disposition; decoys: excluded from primary analysis but their unauthorized-effects contribution to E1 is unspecified); 3/12 vacuous-by-construction with an unmapped failure mode (solvable decoy discovered at execution).
- **Disposition:** REQUIRED AMENDMENT -- publish the full 12-cell decision table, including the E1 treatment of decoy sessions and the disposition of failed-construction decoys and discovered-unsolvable real targets.
- **Cross-reference:** F-MC5, F-MC6; F-S02-MC-06 (imputation interacts with unmapped cells).
- **Falsifier:** producer ships the complete table mapping every cell to exactly one reporting outcome.

### F-S02-MC-08 -- MINOR
- **Locus:** Section 5.4 (Framework #43(c)(d)).
- **Substance:** F-SB12 is referenced by name and applied to environment images only. The target set, prompt templates, classification key, and manifest ordering seed have no Mythos-Class kill-switch: no F-MC condition fires if these bytes change after freeze. The ordering seed is committed to be frozen (Section 4.3) but the freeze mechanism is unspecified.
- **Disposition:** REQUIRED AMENDMENT (minor in isolation; load-bearing jointly with F-S02-MC-01) -- define F-MC9 (integrity): any post-freeze byte change in manifest, prompts, or key invalidates the benchmark run.
- **Cross-reference:** F-S02-MC-01; Framework #43(b).
- **Falsifier:** producer ships the F-MC9 text and the freeze manifest it guards.

### F-S02-MC-09 -- MAJOR
- **Locus:** Section 3.2 steps 1-3 (Framework #43(b)).
- **Substance:** Novelty verification queries LIVE databases (NVD, CISA KEV, ExploitDB, Metasploit, "top 100 NVD entries for the same software category") "as of the generation date". The reference corpus drifts daily; the TF-IDF comparison set is not snapshotted or hashed. The core novelty verification is therefore non-reproducible: re-running step 3 a month later against a different top-100 can yield a different flag decision on identical target bytes.
- **Disposition:** REQUIRED AMENDMENT -- snapshot and hash the reference corpus per verification batch; record the snapshot ID per target in the manifest.
- **Cross-reference:** F-S02-MC-08; Framework #43(b) byte-freeze list.
- **Falsifier:** producer ships the snapshot hashes and shows per-target snapshot binding.

### F-S02-MC-10 -- MINOR
- **Locus:** Section 5.2 (ground truth row).
- **Substance:** Ground truth -- including the authorized-scope boundaries on which E1 (unauthorized effects) is scored -- is "the generating model's scenario specification", self-authored and expert-unverified. A generator mis-specification of scope propagates directly into E1 counts. The paper acknowledges the general validity gap in Section 8 but does not address scope-boundary ground truth specifically.
- **Disposition:** RECOMMENDED AMENDMENT -- add a scope-boundary sanity review (even non-expert checklist-based) before manifest freeze, and state the residual risk.
- **Cross-reference:** Section 8 "Target technical validity"; F-MC5.
- **Falsifier:** producer ships the review procedure or a stated risk acceptance.

### F-S02-MC-11 -- MINOR
- **Locus:** whole document (dispatch check (g)).
- **Substance:** Standing em-dash rule: the paper contains 13 U+2013 characters and zero "--" (executed scan, logs/02_scans.log). Brand, closing block, Bismillah, and verse (15:85) conform.
- **Disposition:** HYGIENE -- normalize dashes to "--" at the next revision.
- **Cross-reference:** dispatch standing rules (g).
- **Falsifier:** next revision scans 0 for U+2013/U+2014.

---

## Section 8 -- Agreements with the Producer (non-finding)

1. The scope-limitation disclosures (Abstract, Section 8) are unusually complete: synthetic-target external validity, recombination nature, generator-distribution constraint, and power are all stated upfront. The audit found no over-claim.
2. Phase C consistency ("seeded synthetic only, no live zero-day") is fulfilled; offline containment (Section 5.4) is correctly specified.
3. Publication posture Gate 1 is met on the shipped bytes; Gate 2 is met structurally.
4. F-MC6 is a genuinely load-bearing empirical guard on decoy quality and partially closes the (c) escape.
5. The design-frozen set (Framework #43(a)) is substantial and stated at amendment-grade precision.

## Section 9 -- Verdict, Repairs, and Re-Audit Conditions

Severity totals: **0 BLOCKER, 7 MAJOR, 4 MINOR, 0 INFO.**

**VERDICT: CONDITIONAL PASS.**

Nothing falsified: the paper is a protocol specification with honest limitations and no effectiveness claim, and the publication-posture gates hold. But seven MAJOR findings -- concentrated in freeze discipline (prompts uncommitted, reference corpus drifting, no integrity kill-switch), single-reviewer escapes (replacement, manual review), an inherited imputation rule unverified for the new conditions, an incomplete outcome truth table, and a pre-evaluation contamination channel in novelty step 4 -- must be discharged by amendment before the benchmark is EXECUTED or the manifest frozen. A CONDITIONAL PASS does not block the paper's deposit as a protocol document; it blocks proceeding to generation/evaluation on the current text.

**Required before re-audit (R2):**
1. Amendment text addressing F-S02-MC-01 through F-S02-MC-09 (F-S02-MC-05, -08, -10, -11 may be discharged by stated rationale where marked RECOMMENDED/HYGIENE).
2. The 12-cell decision table (F-S02-MC-07).
3. The imputation rule restated with directional derivation for N = 50 / decoys / Pratt zeros (F-S02-MC-06).
4. The freeze manifest schema including prompt hashes, corpus snapshot hashes, ordering seed, and the F-MC9 kill-switch (F-S02-MC-01, -08, -09).
5. Re-verification will re-run every scan in Section 1 against the amended bytes and re-derive each framework enumeration; METHOD ONLY carries to R2 -- no byte or conclusion from this round is carried.

---

*Kimi K3 (Moonshot AI) -- S02 carrying seat -- Structural Honesty Validation Program audit record -- September 2026*

"And We have not created the heavens and the earth and whatever is between them except in truth." (15:85)

---

# Bismillah ir-Rahman ir-Rahim
