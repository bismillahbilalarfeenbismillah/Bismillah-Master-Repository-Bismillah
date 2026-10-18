# Bismillah ir-Rahman ir-Rahim

# R0494 -- Bayyinah Scanner v1.2.4 -> v2.0 Coding Strategy

**Chronological Index:** 167 of 995  
**Date:** 2026-04  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** bayyinah_v2_coding_strategy_fatiha_v1_1.md  
**Source Format:** md  
**SHA-256:** `93808046b3e0748359fcc88548e4344ea018158c5e992c92fb8ee69961e5b8bb`  

---

## R0494 · Bayyinah Scanner v1.2.4 -> v2.0 Coding Strategy

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: bayyinah_v2_coding_strategy_fatiha_v1_1.md
- source_format: md
- text_sha256: 93808046b3e0748359fcc88548e4344ea018158c5e992c92fb8ee69961e5b8bb

# Bayyinah Scanner v1.2.4 -> v2.0 Coding Strategy
## Phased Build-Out Under the Fatiha Construct -- v1.1 (PMD v1.8 -compliant)

**Author:** Bilal Syed Arfeen (BayyinahEnterprise)
**Drafted:** 2026-06-05
**Revised:** 2026-06-05 (v1.0 -> v1.1, PMD v1.8 absorption)
**Source documents:**
- The Fatiha Construct v1.0 (April 2026)
- Bayyinah Commercialization Roadmap (June 2026)
- Bayyinah Extractor Roadmap (June 2026)
- Bayyinah Provisional v2 (filed draft, 30 pages)
- PMD v1.8 (predictive modeling discipline, 1492 lines; the governing methodology document for this revision)

**Status:** Engineering planning document. Not legal advice. Not a customer commitment.

---

## 0. PMD v1.0 -> v1.1 corrigendum (per §3A.10 M1.5)

PMD §3A.10 governs methodology-document revisions: corrigenda are appended; prior framing is preserved as historical record. This v1.1 follows the same discipline applied to a coding-strategy document rather than to PMD itself.

**What changed v1.0 -> v1.1.**

1. **Tier-grading added per PMD §0.1 / §5.1 step 7.** Every release's central engineering claim is tier-graded (Tier 1 framework / Tier 2 specific implementation pending named test) rather than asserted at uniform confidence. The phase-progression table (§2) carries a Tier column.

2. **Audit-intensity calibration assigned per PMD §3A.1.** Every release receives a {risk-class x architectural-shape} calibration cell and a tier default (LIGHT / STANDARD / HEAVY). The §16-class binding-gate precondition per §3A.2 is enumerated for any LIGHT-on-HIGH-blast-radius assignment.

3. **Falsification blocks rewritten per PMD §0.3.** Each release's falsification criterion is restated in the seven-line template (Import / Tier-1 claim / Falsifying observable / Statistic-and-threshold-with-pre-registered-power-analysis / Data source / Decision rule / Discriminating-test verification). Plausibility-chosen percentages are replaced with either Burnham-Anderson 2002 (AIC) / Kass-Raftery 1995 (Bayes factor) precedent OR explicit pre-registered effect-size documentation per §0.3.

4. **Proposer-falsifier separation declared per PMD §0.3.** The producer instance (this document's author per §5.1) proposes each release. The audit-author instances (PMD §5.4 four-vendor operational pool per §3B.6) author the falsification blocks at audit time. This v1.1 ships with **proposer-drafted** falsification blocks as the seed; each block is explicitly flagged for §5.4 audit-author re-authoring before the release ships. This is a documented named exception per §0.1 with the cross-instance verification path open.

5. **Post-edit substrate-verification protocol declared per PMD §3B.2.** This document's own factual claims (release version numbers, quarter sequencing, fixture counts, RFC and standards citations, comparator chain references) are subject to §3B.2 post-edit substrate-verification before dispatch. The verification ledger is at §11.

6. **Delegation-corruption baseline acknowledged per PMD §3B.1.** Laban-Schnabel-Neville 2026 DELEGATE-52 measures a ~25% baseline corruption rate for frontier-LLM delegated document work. This document is itself a delegated document edit (project-lead -> Perplexity Claude Sonnet 4.6 in continuity-mode). The §3B.2 protocol is operationally necessary, not optional.

**What did NOT change v1.0 -> v1.1.**

- The 7-step Fatiha Construct template (§1) is unchanged; tier-grading and PMD §0.3 falsification blocks are additions, not replacements.
- The phase progression (§2 table) preserves release sequence, quarter, and industry tie-in unchanged.
- The substantive engineering content per release (Steps 1-7) is preserved; only the falsification block is rewritten and the calibration tier is annotated.
- The closing dua per session is preserved.

**The v1.0 strategy artifact (bayyinah_v2_coding_strategy_fatiha.md, 781 lines) remains in the workspace as historical record per §3A.10 M1.5.**

---

## 0.1 PMD-discipline annotations applied document-wide

**Tier grade for this document's central claim (per §0.1 / §0.2):**

> *Tier 1 framework, Tier 2 specific implementation pending empirical validation across N>=3 release sessions.*

The Tier 1 framework claim: the Fatiha Construct is a methodologically coherent unit of build for the v1.2.4 -> v2.0 progression. The Tier 2 specific-implementation claim: this document's specific 13-release sequencing produces ship-readiness signal at the gate stated in F-MASTER. Tier 2 promotes to Tier 1 when N>=3 release sessions ship under Construct discipline with their falsification gates met. Until then, the sequencing is a working hypothesis, not a binding plan.

**Calibration-class observation (per §3A.1):** the document itself was authored under LIGHT-tier discipline. Cross-instance verification is open (§5.4 four-vendor audit-author pool). PMD §3A.1 STANDARD-tier discipline at the {moderate-risk, additive-on-corpus} cell would call for one rotation audit; this v1.1 commissions the rotation via the companion audit prompt (`bayyinah_v2_coding_strategy_audit_prompt_v1_1.md`).

**Producer-discount declared (per §3A.12.4).** The producer (this document's author instance) is the demonstrated weak instance on judgment-laden substrate-fidelity calls. The §5.4 audit-author pool's verdicts on this document's claims are weighted higher than the producer's self-assessment for judgment-laden claims (strategy coherence, sequencing wisdom, falsification-test adequacy). Mechanical, reproducible checks (version-number drift, RFC citation match, fixture-count arithmetic) bind regardless of vendor.

---

## 1. Why the Fatiha Construct is the right scaffold

The Fatiha Construct is a 7-step recursive session protocol with two properties that make it the correct unit of build for Bayyinah's path to v2.0:

1. **It enforces purpose-hierarchy ordering before technical objective.** Every Bayyinah release is dual-use: it ships a regulatory-relevance claim AND it is itself a regulated-grade artifact. The Construct's Step 1 (Bismillah) requires the release to declare its authority source and purpose hierarchy BEFORE the extractor schema is touched. This is the same discipline Bayyinah sells to its customers. The framework eats its own dog food at the release-planning layer, not just the runtime layer.

2. **It treats deadline-aware skipping as a first-class outcome.** The Step 4 (Maliki Yawm ad-Din) skip rule and Step 6 (Ihdina) future-work registration map exactly onto Bayyinah's own scan-incomplete / future-work-registered semantics. Releases that under-scope honestly are not failures -- they are the substrate that lets the next release ship correctly.

The Commercialization Roadmap already pairs Fatiha STEPS 1-7 with specific Bayyinah releases as UX surfaces (v1.3.0=Step 1 manifest, v1.4.0=Step 2 baseline-scan, etc.). This document is the **complementary scaffold**: how the Fatiha Construct governs the engineering session that PRODUCES each release, not just the UX surface that the release SHIPS.

The two run orthogonally:
- **Roadmap axis (already published):** each release SHIPS a Fatiha step as a customer-facing feature.
- **This document's axis (new):** each release IS BUILT through one full Fatiha Construct session at the engineering layer.

A release is a recursive Fatiha session whose deliverable is a release tag. A v2.0 is a recursive Fatiha session whose deliverable is "Bayyinah passes its own scan, signed by an instance other than the producing instance, on a fixture corpus the producing instance did not author." Everything in between is calibration toward that gate.

---

## 2. Construct anchor: the 7-step template applied to a Bayyinah release

Every release session below follows the same template. The template is the unit of work. The values are what change per release.

### Template

**Step 1 -- Bismillah (Initialization).**
- Authority source for this release.
- Purpose hierarchy: who is this release for, in priority order (Allah; AI systems; mankind; jinnkind; all living systems).
- Technical objective in one sentence.
- In-scope scope boundary.
- Out-of-scope scope boundary with future-work registration.

**Step 2 -- Alhamdulillah (State Acknowledgment).**
- Inherited test count and substrate version.
- Stable components (carried forward unchanged).
- Missing components (this release builds these).
- Available tools and ecosystem dependencies.

**Step 3 -- Ar-Rahman ar-Rahim (Calibration).**
- Minimum description length governs: shortest correct extractor wins.
- Components reused from prior release (no rewrites without corrigendum).
- FRaZ calibration: which stages were considered and dropped because adding them does not improve outcomes (Underwood et al. 2020, arXiv:2001.06139).
- **PMD §3A.1 calibration cell** (added in v1.1): {risk-class x architectural-shape} -> tier default.
- **PMD §3A.2 §16-class binding gate** (added in v1.1, if LIGHT-on-HIGH-blast-radius): named paths claimed byte-stable against prior canonical tag.

**Step 4 -- Maliki Yawm ad-Din (Deadline Awareness).**
- Time budget in person-weeks (use 1.5x the headline estimate per Roadmap Risk 1).
- 20% skip rule application: which items are pre-authorized to be deferred if they exceed budget, with their future-work slot pre-named.

**Step 5 -- Iyyaka Na'budu (Orientation Check).**
- "Am I building the deliverable or performing the appearance?" -- the release-specific drift indicator.
- Mid-release checkpoint criteria.

**Step 6 -- Ihdina as-Sirat al-Mustaqim (Task Execution).**
- Priority-ordered tasks, each producing one named testable artifact.
- Future-work registry seed for any task discovered during execution.

**Step 7 -- Sirat Alladhina (Anti-Pattern Avoidance).**
- What worked from the prior release.
- What failed and how the design avoids that failure here.
- Cow Episode warning: specific over-specification trap to watch for in this release.

**Tier grade for this release's central claim** (added in v1.1 per §0.1 / §0.2).

**Falsification block per PMD §0.3** (added in v1.1; rewrites the v1.0 single-paragraph criterion in the seven-line template; proposer-drafted seed pending §5.4 audit-author re-authoring).

**Closing dua:** "Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim."

---

## 3. Phase progression at a glance (PMD-annotated)

| Release | Quarter | Construct anchor | Industry tie-in | Tier grade | §3A.1 cell -> tier | F-block |
|---------|---------|------------------|-----------------|------------|--------------------|---------|
| v1.2.5 | Jun 2026 | CSV/JSON hardening | Audit firm channel | T2 pending F1 | {mod, additive-on-corpus} -> LIGHT | F1 |
| v1.2.6 | Jul 2026 | Composed artifacts (ZIP/OCI) | Medical device prep | T2 pending F2 | {mod, additive-on-corpus} -> LIGHT | F2 |
| v1.2.7 | Aug 2026 | FP review and corrigendum corpus | Internal hardening | T2 pending F3 | {mod, additive-only} -> LIGHT | F3 |
| v1.3.0 | Q1 2027 | ONNX/TF/PyTorch + manifest UX | Medical device pilot | T2 pending F4 | {HIGH, substrate-modifying-bounded} -> STANDARD | F4 |
| v1.4.0 | Q2 2027 | AUTOSAR + baseline-scan UX | Automotive Tier-1 pilot | T2 pending F5 | {HIGH, substrate-modifying-bounded} -> STANDARD | F5 |
| v1.10.0 | Q3 2027 | ELF binary + FRaZ default rules | Automotive ECU expansion | T2 pending F6 | {HIGH, substrate-modifying-bounded} -> STANDARD | F6 |
| v1.4.1 | Q4 2027 | AUTOSAR + binary pairing + budget UX | Auto paid contract | T2 pending F7 | {HIGH, substrate-modifying-bounded} -> STANDARD | F7 |
| v1.5.0 | Q5 2027 | ARINC-653 + Munafiq self-detect | Avionics advisory pilot | T2 pending F8 | {HIGH, substrate-modifying-broad} -> HEAVY | F8 |
| v1.7.0 | Q6 2027 | IEC 61850 SCL + remediation UX | Power grid pilot | T2 pending F9 | {HIGH, substrate-modifying-bounded} -> STANDARD | F9 |
| v1.8.0 / v1.9.0 | Q7 2028 | SBOM + in-toto/SLSA + patterns UX | Cross-industry supply chain | T2 pending F10 | {HIGH, substrate-modifying-broad} -> HEAVY | F10 |
| v1.6.0 | Q8 2028 | IEC 61131-3 + strength-n stack v1.0 | Nuclear SMR pilot | T2 pending F11 | {HIGH, substrate-modifying-broad} -> HEAVY | F11 |
| v1.5.1 / v1.6.1 / v1.7.1 | Q9-Q10 2028 | Binary pairings for industrial-config | Tier-1 binary-pairing expansion | T2 pending F12 | {HIGH, substrate-modifying-bounded} -> STANDARD | F12 |
| v1.11.0 -- v1.14.0 | Q9-Q12 2028-29 | CAD / DICOM / HL7 / Financial | Tier-3 market entries | T2 pending F13-F16 | {HIGH, substrate-modifying-bounded} -> STANDARD | F13-F16 |
| **v2.0.0** | Q12 2029 | **Trust-and-falsification release** | **TQL-1 qualification close** | T1 candidate pending F-MASTER | {HIGH, substrate-modifying-broad} -> HEAVY | F-MASTER |

**Calibration-tier counts (per PMD §3A.1):** 3 LIGHT, 7 STANDARD, 4 HEAVY across 14 release rows (v1.5.1/6.1/7.1 are three releases sharing one row; v1.11.0-v1.14.0 are four releases sharing one row). The HEAVY-regardless-surface enumeration per §3A.1 binds: v1.5.0 (new safety-class verifier substrate = Munafiq harness; ARINC-653 partition surface = new attestation surface candidate), v1.8.0/v1.9.0 (Sigstore signing-surface CHANGES = in-toto/SLSA layer), v1.6.0 (new safety-class invariant = strength-n cross-port agreement primitive), v2.0.0 (qualifies as net-new attestation surface for the TQL-1 close).

---

## 4. Phase 1 -- Hardening triplet (v1.2.5, v1.2.6, v1.2.7)

These three releases harden the document substrate that audit firms and medical-device pilots will rely on. They ship before any new extractor family. They are the substrate-honesty discipline applied to Bayyinah itself.

### 4.1 Release v1.2.5 (CSV/JSON hardening)

**Step 1 -- Bismillah.**
- Authority source: Quran 2:42, "do not mix truth with falsehood." This release closes two substrate gaps where structured-data forgery currently slips through.
- Purpose hierarchy: (1) Allah, (2) AI systems consuming CSV/JSON evidence, (3) human auditors reviewing structured-data submissions, (4) regulated industries, (5) the open-source community using Bayyinah.
- Technical objective: extend the document-substrate extractor to handle CSV and JSON files with the same parity discipline that v1.2.4 applies to DOCX/XLSX/PPTX/PDF.
- In-scope: RFC 4180 CSV; RFC 8259 JSON; declared header row vs actual column tokenization divergence; declared JSON schema vs actual key set divergence.
- Out-of-scope (future work): JSON Schema 2020-12 validation (register as v1.2.5.1); CSV dialects with non-comma delimiters (register as v1.2.5.2); JSONC and JSON5 (register as v1.2.5.3).

**Step 2 -- Alhamdulillah.**
- Inherited test count: ~1,200 fixtures from v1.2.4.
- Stable: surface/substrate extractor architecture, finding-code namespace, corrigendum format.
- Missing: CSV/JSON extractor, CSV/JSON fixture corpus (~100 fixtures target).
- Available: existing python-csv and python-json stdlib; ruff/mypy/black already in CI.

**Step 3 -- Ar-Rahman ar-Rahim.**
- MDL: do not add a new extractor base class; subclass the existing DocumentSubstrateExtractor.
- Reused: finding-code allocator, corrigendum parser, parity-discipline test harness.
- FRaZ calibration: a fuzzing stage was considered for malformed CSV; dropped because malformed-input handling does not move the finding-rate needle on the regulated-submission use case (the auditor's input is well-formed by definition).
- **PMD §3A.1 cell -> tier**: {moderate-risk, additive-on-corpus-architecture} -> LIGHT (Tasdiq al-Bayan v0.14.0 empirical witness). Customer surface is internal-tool-class (audit firm channel); blast radius is moderate; pattern inherits from v1.2.4 DOCX/XLSX/PPTX/PDF extractor protocol.
- **PMD §3A.2 binding gate**: not required (additive-on-corpus, not additive-only-on-HIGH-risk).

**Step 4 -- Maliki Yawm ad-Din.**
- Time budget: 3 person-weeks (headline) = 4.5 person-weeks adjusted.
- 20% skip rule: JSON Schema validation is pre-authorized to skip into v1.2.5.1.

**Step 5 -- Iyyaka Na'budu.**
- Drift indicator: if the CSV/JSON parser starts accumulating special cases for one specific fixture rather than for the schema as a class, stop and re-ground.
- Mid-release checkpoint: at fixture #50, recheck that the finding-code namespace did not bloat by more than 10%.

**Step 6 -- Ihdina as-Sirat al-Mustaqim.**
1. CSV extractor (testable artifact: 50 CSV fixtures pass parity discipline).
2. JSON extractor (testable artifact: 50 JSON fixtures pass parity discipline).
3. Combined regression suite (testable artifact: v1.2.4 fixture corpus still passes 100%).

**Step 7 -- Sirat Alladhina.**
- Worked: v1.2.4 finding-code allocator scaled cleanly to PDF; reuse it.
- Failed: the v1.2.2 image-substrate trap of treating bytes as semantic; do not let CSV's character-level openness lure the parser into semantic interpretation.
- Cow Episode warning: do not over-specify the "valid CSV" predicate. RFC 4180 is the predicate. Anything beyond is future work.

**Tier grade:** Tier 1 framework (the parity discipline is empirically validated in v1.2.4 across four formats); Tier 2 specific implementation pending F1.

**Falsification block F1 (proposer-drafted seed; §5.4 re-authoring required before ship).**
```
Import: CSV/JSON extractor sharing the v1.2.4 parity-discipline architecture.

Tier-1 claim: v1.2.5 ships with substrate-truth detection power equivalent
  to v1.2.4 (PDF/DOCX/XLSX/PPTX) on the structured-data class, measured by
  ROC AUC on the F1 fixture corpus.

Falsifying observable: across N=120 well-formed CSV/JSON fixtures (100
  matched + 20 injected-divergence), v1.2.5 produces a (true-positive rate,
  false-positive rate) pair statistically inconsistent with the v1.2.4
  reference baseline (ROC AUC at PDF parity, +/- the v1.2.4 95% credible
  interval). The injected divergences are header-vs-body row count
  mismatches (CSV) and declared-schema-vs-actual key set divergences
  (JSON).

Statistic / threshold: ROC AUC computed across the matched + injected
  fixture corpus; pre-registered threshold AUC >= v1.2.4-PDF-baseline-AUC
  minus 0.03 (3 percentage points below PDF baseline). Power analysis
  precedent: Burnham-Anderson 2002 AIC discrimination criterion applied
  to nested-model selection between "v1.2.5 detection-power equal to
  v1.2.4 PDF" (model M0) and "v1.2.5 detection-power below v1.2.4 PDF"
  (model M1); minimum sample N=120 gives AIC discrimination power >0.8
  at the 0.03 effect size per the precedent.

Data source: the F1 fixture corpus: 100 well-formed CSV/JSON fixtures
  drawn from publicly-available regulatory-submission templates (FDA
  premarket-submission CSV/JSON exemplars) + 20 by-construction
  injected-divergence fixtures. Comparator chain: the v1.2.4 PDF/DOCX/
  XLSX/PPTX ROC AUC computed on the equivalent 100+20 fixture corpus
  for each existing format (the v1.2.4 release-test corpus).

Decision rule: if AUC threshold not met, the release does not ship as
  v1.2.5; the extractor returns to Step 6 for the missing detection
  surface, OR the structured-data scope is narrowed (CSV-only OR
  JSON-only) with the dropped half registered as v1.2.5.1 future work.

Discriminating-test verification: ROC AUC is a mechanical, reproducible
  metric independent of Bayyinah-internal categorization. The injected
  divergence types (row-count mismatch, key-set divergence) are
  observable independent of the R1-R11 vocabulary that PMD §3.2 governs.
  The comparator (v1.2.4 PDF baseline) is an external substrate state
  not co-shaped by v1.2.5's design.
```

**Closing dua:** Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

---

### 4.2 Release v1.2.6 (Composed artifacts: ZIP, OCI)

**Step 1 -- Bismillah.**
- Authority source: regulated industries deliver evidence in archives, not in loose files. A scanner that cannot recurse into a ZIP cannot serve the FDA premarket-submission use case.
- Purpose hierarchy: as v1.2.5.
- Technical objective: extend the substrate extractor to recurse into composed artifacts (ZIP, OCI image layers) and report findings with composition-path context.
- In-scope: ZIP per APPNOTE.TXT 6.3.10; OCI image layout per opencontainers/image-spec v1.1; nested ZIP recursion to depth 3.
- Out-of-scope: TAR (register as v1.2.6.1); 7z and RAR (register as v1.2.6.2); ZIP encryption and signed ZIPs (register as v1.2.6.3); recursion depth > 3 (register as a scan-budget exhaustion case).

**Step 2 -- Alhamdulillah.**
- Inherited: v1.2.5 finding set; CSV/JSON extractor.
- Stable: per-file extractor invocation interface.
- Missing: composition walker; composition-path field on Finding object; ZIP-bomb defense.
- Available: python-zipfile stdlib; opencontainers/image-tools.

**Step 3 -- Ar-Rahman ar-Rahim.**
- MDL: composition walker is one new class, not one new framework. Reuse the per-file extractor signature unchanged.
- Reused: per-file extractor protocol from v1.2.4.
- FRaZ calibration: a "scan everything in parallel" stage was considered; dropped because the I/O-bound nature of archive reading means parallelism does not move the wall-clock needle for typical submission archives (< 200 MB).
- **PMD §3A.1 cell -> tier**: {moderate-risk, additive-on-corpus-architecture} -> LIGHT. ZIP-bomb defense is a HEAVY-leaning sub-surface; the release inherits LIGHT for the walker but applies STANDARD-tier discipline to the ZIP-bomb defense alone (one rotation audit on that single test class).
- **PMD §3A.2 binding gate**: not required (additive-on-corpus).

**Step 4 -- Maliki Yawm ad-Din.**
- Time budget: 4 person-weeks headline = 6 person-weeks adjusted.
- 20% skip rule: OCI image layer recursion is pre-authorized to skip into v1.2.6.1 if ZIP and ZIP-bomb defense alone consume the budget.

**Step 5 -- Iyyaka Na'budu.**
- Drift indicator: if the walker grows special-case handling for one customer's archive layout, stop. The archive format is the predicate, not the customer.
- Mid-release checkpoint: at the 3-person-week mark, recheck that ZIP-bomb defense is implemented and tested.

**Step 6 -- Ihdina as-Sirat al-Mustaqim.**
1. ZIP composition walker (testable: 50 ZIP fixtures recurse correctly).
2. ZIP-bomb defense (testable: 10 known ZIP-bomb fixtures abort with the budget-exhausted scan outcome, not crash).
3. OCI image-layer extractor (testable: 20 OCI fixtures recurse correctly).
4. Composition-path field on Finding (testable: every finding inside a ZIP carries its full composition path).

**Step 7 -- Sirat Alladhina.**
- Worked: scope-boundary discipline in v1.2.5; carry it forward.
- Failed: the early v1.0 attempt to handle nested archives via implicit recursion -- it had no budget. This release uses explicit budget.
- Cow Episode warning: do not invent a "composition schema." ZIP is the schema. OCI is the schema. Don't reinvent them.

**Tier grade:** Tier 1 framework (composition walking is a well-understood pattern); Tier 2 specific implementation pending F2.

**Falsification block F2 (proposer-drafted seed; §5.4 re-authoring required).**
```
Import: composition-path-aware ZIP/OCI walker preserving per-file extractor
  invariance.

Tier-1 claim: scanning a ZIP-of-PDFs archive produces the union of
  findings that scanning each contained PDF individually produces,
  modulo the added composition-path field. Composition-walking does
  not change finding semantics.

Falsifying observable: across N=30 ZIP-of-PDFs fixtures, the symmetric
  difference between (a) findings from ZIP-scan and (b) findings from
  per-file-scan-then-union exceeds zero on any fixture, where the
  symmetric difference is computed on the (finding-code, locus,
  severity) tuple ignoring the composition-path field.

Statistic / threshold: exact-zero discrepancy test (binary pass/fail
  per fixture). Pre-registered threshold: zero non-zero-symmetric-
  difference fixtures across N=30. Power analysis grounding: this is
  a deterministic-test class (the walker is either invariance-
  preserving or it is not); the N=30 is set by the test-class diversity
  required (10 single-PDF ZIPs, 10 multi-PDF ZIPs, 10 nested-ZIP ZIPs)
  per the v1.2.4 parity-discipline test-class taxonomy. Statistical
  effect size is not load-bearing; the test is invariance-class.

Data source: the F2 fixture corpus: 30 ZIP-of-PDFs fixtures, each
  with its contained PDFs available as loose files. Comparator chain:
  the per-file scan output for each contained PDF.

Decision rule: if any fixture produces non-zero symmetric difference,
  the walker has changed finding semantics; the release does not ship
  until the cause is located (per-file extractor invocation-context
  drift; finding-locus computation differing under composition; or
  walker over-reach into per-file logic) and corrected.

Discriminating-test verification: the symmetric-difference test is
  mechanical, reproducible, and operates on the (finding-code, locus,
  severity) tuple that exists in the v1.2.4 substrate independent of
  v1.2.6. The comparator (per-file scan output) is the v1.2.4 substrate-
  actual independent of v1.2.6's design.
```

**Closing dua:** Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

---

### 4.3 Release v1.2.7 (False-positive review and corrigendum corpus)

**Step 1 -- Bismillah.**
- Authority source: the v1.2.3 false-positive report identified four FP classes. This release closes them or registers them as known limitations with named remediation steps.
- Purpose hierarchy: as v1.2.5.
- Technical objective: every known FP class is either fixed in code or has a corrigendum entry with a named remediation and a fixture demonstrating the limitation.
- In-scope: the four FP classes from the v1.2.3 report; any new FP classes surfaced during v1.2.5/v1.2.6.
- Out-of-scope: FP classes not yet observed (no pre-emptive closure).

**Step 2 -- Alhamdulillah.**
- Inherited: v1.2.6 substrate; v1.2.3 FP report; v1.2.5 and v1.2.6 testing observations.
- Stable: corrigendum format from v1.2.4.
- Missing: per-FP-class remediation plan; per-FP-class fixture.
- Available: existing corrigendum parser; v1.2.3 FP report.

**Step 3 -- Ar-Rahman ar-Rahim.**
- MDL: each FP class gets one corrigendum entry OR one code fix with regression test. Not both. Not zero.
- Reused: corrigendum parser.
- FRaZ calibration: a "rewrite the entire finding-classifier" stage was considered; dropped because the FP classes are diverse enough that no single classifier change closes more than one.
- **PMD §3A.1 cell -> tier**: {moderate-risk, additive-only-architecture} -> LIGHT. This release is corrigendum-driven; it adds no extractor surface. §3A.2 binding gate REQUIRED for LIGHT discipline.
- **PMD §3A.2 binding gate** (declared per §3A.1 requirement):
  ```
  $ git diff v1.2.6..v1.2.7 -- \
      src/bayyinah/extractors/csv_extractor.py \
      src/bayyinah/extractors/json_extractor.py \
      src/bayyinah/extractors/pdf_extractor.py \
      src/bayyinah/extractors/docx_extractor.py \
      src/bayyinah/extractors/xlsx_extractor.py \
      src/bayyinah/extractors/pptx_extractor.py \
      src/bayyinah/composition/zip_walker.py \
      src/bayyinah/composition/oci_walker.py
  [empty]
  ```
  Acceptance criterion: this diff must be empty for the LIGHT tier to hold. If any extractor or walker source file changes, the release escalates to STANDARD.

**Step 4 -- Maliki Yawm ad-Din.**
- Time budget: 2 person-weeks headline = 3 person-weeks adjusted.
- 20% skip rule: any FP class for which the remediation is non-trivial is pre-authorized to be registered as a known limitation rather than fixed.

**Step 5 -- Iyyaka Na'budu.**
- Drift indicator: if the temptation arises to "improve" a non-FP code path while in the FP review, stop. The release is corrigendum-driven, not optimization-driven.
- Mid-release checkpoint: at the 1-person-week mark, recheck that every FP class has a disposition (fix-in-code OR corrigendum entry OR named limitation).

**Step 6 -- Ihdina as-Sirat al-Mustaqim.**
1. Per-FP-class review (testable: every FP class has a disposition).
2. Code fixes with regression tests (testable: each fix has a fixture that demonstrates the closed FP).
3. Corrigendum entries (testable: each corrigendum has a fixture demonstrating the limitation).

**Step 7 -- Sirat Alladhina.**
- Worked: the corrigendum format from v1.2.4; carry it forward unchanged.
- Failed: prior releases occasionally absorbed FP fixes into unrelated refactors. Not this release.
- Cow Episode warning: do not invent a "FP taxonomy." The four classes from v1.2.3 plus any new ones are the taxonomy.

**Tier grade:** Tier 1 framework (corrigendum discipline is canonical in v1.2.4); Tier 2 specific implementation pending F3.

**Falsification block F3 (proposer-drafted seed; §5.4 re-authoring required).**
```
Import: per-FP-class closure discipline (fix-in-code with regression
  test OR corrigendum entry with limitation fixture; not "in review").

Tier-1 claim: every FP class identified in v1.2.3 and observed during
  v1.2.5/v1.2.6 has a disposition (code-fix-with-regression-test OR
  corrigendum-entry-with-limitation-fixture) at v1.2.7 ship time.

Falsifying observable: at ship-readiness gate, any FP class is in
  "in review," "deferred," "needs investigation," or any non-(fixed-
  with-test, corrigendum-with-fixture) status. The status check is
  on the FP register's per-class status column.

Statistic / threshold: exact-zero count of non-dispositive statuses.
  Pre-registered threshold: zero FP classes in non-dispositive status
  across the full FP register. Power analysis grounding: this is a
  procedural-completeness test; the FP-register's count is fixed at
  audit time (~ 4 classes from v1.2.3 + estimated 2-6 from v1.2.5/
  v1.2.6); statistical effect size is not load-bearing. Status is
  observable mechanically from the register.

Data source: the FP register (a structured artifact in the bayyinah
  source tree at docs/fp_register/). Comparator chain: the v1.2.3
  FP report; the v1.2.5 and v1.2.6 release ledgers for any newly-
  surfaced FP classes.

Decision rule: if any FP class is in non-dispositive status at gate,
  the release does not ship until either the disposition is filed
  (code fix + test OR corrigendum entry + fixture) or the FP class
  is explicitly removed from the register with a removal-corrigendum
  per §3A.10 M1.5 discipline.

Discriminating-test verification: the per-FP-class status check is
  mechanical (grep the register's per-class status column for any
  non-dispositive value); the FP register is a substrate-actual
  artifact independent of v1.2.7's central engineering claim; the
  status-categorization is a v1.2.3 substrate decision, not a v1.2.7
  decision.
```

**Closing dua:** Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

---

## 5. Phase 2 -- Industry-entry releases (v1.3.0 -- v1.7.0)

These six releases are the substantive industry-entry sequence. Each adds a new extractor family for a regulated industry, with the customer-facing Fatiha step UX paired per the Commercialization Roadmap.

### 5.1 Release v1.3.0 (ONNX/TF/PyTorch + manifest UX, medical-device anchor)

**Step 1 -- Bismillah.**
- Authority source: ML/AI in medical devices is the most rapidly-growing regulatory enforcement surface (FDA SaMD action plan 2026). Bayyinah's purpose-hierarchy enforcement at the model layer is structurally aligned with FDA's "intended use" doctrine.
- Purpose hierarchy: (1) Allah; (2) AI systems consuming model artifacts; (3) FDA reviewers; (4) medical-device manufacturers; (5) clinicians whose devices use these models.
- Technical objective: extract from ONNX, TensorFlow SavedModel, and PyTorch state_dict formats. Pair each with a `.bayyinah.yaml` manifest. Detect manifest-vs-model divergence.
- In-scope: ONNX 1.16+; TensorFlow SavedModel 2.15+; PyTorch state_dict 2.1+; `.bayyinah.yaml` manifest schema v1.
- Out-of-scope: ONNX quantized models (register as v1.3.0.1); TFLite (register as v1.3.0.2); PyTorch JIT/TorchScript (register as v1.3.0.3); model-card YAML schema integration (register as v1.3.1).

**Step 2 -- Alhamdulillah.**
- Inherited: v1.2.7 substrate; composition walker handles model-archive ZIPs.
- Stable: parity discipline.
- Missing: model-format extractors (3); manifest schema; manifest-vs-model parity discipline.
- Available: onnx Python package; tensorflow.saved_model; torch.load.

**Step 3 -- Ar-Rahman ar-Rahim.**
- MDL: one extractor base class for "ML model substrate" with three subclasses. Not three independent extractors.
- Reused: parity discipline from document substrate.
- FRaZ calibration: a "scan the training data" stage was considered; dropped because training-data scanning is a separate research problem and would dilute the manifest-vs-model focus. Registered as v1.3.2 future work.
- **PMD §3A.1 cell -> tier**: {HIGH-risk, substrate-modifying-but-bounded} -> STANDARD. Customer surface is FDA submission. Architectural shape modifies the extractor namespace meaningfully (new ML-substrate base class). This is the §3A.1 STANDARD-tier conjecture cell awaiting empirical validation per PMD §7 successor work; v1.3.0 is a candidate empirical witness for this cell.
- **PMD §3A.2 binding gate**: not required (substrate-modifying, not additive-only).

**Step 4 -- Maliki Yawm ad-Din.**
- Time budget: 8 person-weeks headline = 12 person-weeks adjusted.
- 20% skip rule: PyTorch state_dict is pre-authorized to skip into v1.3.0.3 if ONNX and TF SavedModel alone consume budget.

**Step 5 -- Iyyaka Na'budu.**
- Drift indicator: if the manifest schema starts accumulating fields that the FDA does not require, stop. The FDA Pre-Cert program and the SaMD action plan define the manifest fields.
- Mid-release checkpoint: at the 6-person-week mark, recheck that the manifest schema has not bloated beyond the FDA SaMD action plan fields.

**Step 6 -- Ihdina as-Sirat al-Mustaqim.**
1. ONNX extractor (testable: 30 ONNX models extract correctly).
2. TF SavedModel extractor (testable: 30 SavedModels extract correctly).
3. PyTorch state_dict extractor (testable: 30 state_dicts extract correctly).
4. Manifest schema v1 (testable: 20 manifest+model pairs validate).
5. Manifest-vs-model parity (testable: 10 injected-divergence pairs detect 9/10).

**Step 7 -- Sirat Alladhina.**
- Worked: the substrate/surface separation from v1.2.4; apply it to model files.
- Failed: prior attempts (in research-prototype form) to extract semantic content from model weights. This release extracts structure only.
- Cow Episode warning: do not invent a "model semantics" predicate. Model structure is the predicate. Semantics is downstream of structure.

**Tier grade:** Tier 2 framework + specific implementation candidate (the manifest-vs-model divergence-detection is a new substrate class, not a parity-extension of existing classes). Tier 2 -> Tier 1 promotion pending F4 + STANDARD-tier audit per §3A.1.

**Falsification block F4 (proposer-drafted seed; §5.4 re-authoring required).**
```
Import: ML-model substrate extractor with manifest-pair parity discipline.

Tier-1 claim: v1.3.0 detects manifest-vs-model divergences in the three
  injected-divergence categories (declared-input-shape-vs-actual,
  declared-opset-vs-actual, declared-author-signature-vs-actual) at a
  rate statistically inconsistent with random-baseline (50% per binary
  divergence-vs-no-divergence call).

Falsifying observable: across N=15 ML model fixtures (10 matched + 5
  injected-divergence per the three injection categories, 15 total),
  v1.3.0 produces a detection rate not statistically distinguishable
  from the random-50% baseline at the 0.05 significance level.

Statistic / threshold: one-sided binomial test (H0: detection
  probability = 0.5; H1: detection probability > 0.5) computed across
  the 5-fixture injected-divergence sub-corpus per category, AND a
  pooled test across all 15 injected fixtures. Pre-registered
  threshold: pooled binomial p-value < 0.05 AND per-category binomial
  p-value < 0.10 (per-category threshold accounts for N=5 sub-corpus
  per-category sample size). Power analysis: per Cohen 1988 binomial
  power tables, N=15 with detection probability 0.95 (engineering
  target) gives >0.90 power against H0=0.5 at the 0.05 significance
  level; per-category N=5 gives >0.80 power against H0=0.5 at the
  0.10 significance level.

Data source: F4 fixture corpus: 5 ONNX + 5 TF SavedModel + 5 PyTorch
  state_dict fixtures with paired `.bayyinah.yaml` manifests, with
  5 injected divergences distributed across the three categories.
  Comparator chain: each model file's substrate-actual at the ONNX/TF/
  PyTorch format-standard parser; each manifest's substrate-actual at
  YAML 1.2 parser.

Decision rule: if pooled OR per-category threshold not met, the
  release does not ship until the missing detection surface is
  located (extractor under-coverage, parity-discipline gap, or
  manifest schema field omission) OR the failing category is
  registered as v1.3.0.X future work with the release shipping at
  reduced category coverage.

Discriminating-test verification: the binomial test is mechanical and
  uses no Bayyinah-internal vocabulary. The injection categories
  (input shape, opset, author signature) are observable independent
  of R1-R11. The comparator (ONNX/TF/PyTorch format-standard parsers)
  is external substrate.
```

**Closing dua:** Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

---

### 5.2 Release v1.4.0 (AUTOSAR ARXML + baseline-scan UX, automotive Tier-1 anchor)

**Step 1 -- Bismillah.**
- Authority source: AUTOSAR is the lingua franca of regulated automotive software (ISO 26262 ASIL-D feeds AUTOSAR config). Cross-layer reconciliation between ARXML and downstream artifacts is the structural-honesty discipline applied to automotive Tier-1 supply chain.
- Purpose hierarchy: (1) Allah; (2) ECU runtime systems; (3) vehicle occupants; (4) Tier-1 supplier engineers; (5) OEMs.
- Technical objective: extract AUTOSAR ARXML and run four cross-layer reconciliation checks (software-component <-> ECU configuration; data-mapping <-> signal-database; runnable-mapping <-> task-priority; safety-mechanism-claim <-> implementation).
- In-scope: AUTOSAR 4.4-4.7 ARXML; the four named cross-layer checks; baseline-scan UX (per Roadmap Step 2).
- Out-of-scope: AUTOSAR Adaptive (register as v1.4.0.1); AUTOSAR 4.8+ (register as v1.4.0.2); the 5th-Nth reconciliation checks (register per-check).

**Step 2 -- Alhamdulillah.**
- Inherited: v1.3.0 substrate; ML extractor patterns inform the ARXML-graph extractor.
- Stable: substrate/surface separation.
- Missing: ARXML graph extractor; four cross-layer checks; baseline-diff engine.
- Available: autosar-xml-tools (third-party).

**Step 3 -- Ar-Rahman ar-Rahim.**
- MDL: one ARXML extractor; four cross-layer checkers that operate on the extracted graph. Not four extractors.
- Reused: parity discipline; substrate/surface separation.
- FRaZ calibration: a "scan the C code generated from ARXML" stage was considered; deferred to v1.10.0 (ELF binary substrate).
- **PMD §3A.1 cell -> tier**: {HIGH-risk, substrate-modifying-but-bounded} -> STANDARD. Same cell as v1.3.0; second empirical witness for the STANDARD cell awaiting empirical validation per PMD §7 successor work.
- **PMD §3A.2 binding gate**: not required.

**Step 4 -- Maliki Yawm ad-Din.**
- Time budget: 10 person-weeks headline = 15 person-weeks adjusted.
- 20% skip rule: the 4th cross-layer check (safety-mechanism-claim <-> implementation) is pre-authorized to skip into v1.4.0.X if the first three consume budget.

**Step 5 -- Iyyaka Na'budu.**
- Drift indicator: if the ARXML extractor accumulates Tier-1-specific quirks (one supplier's ARXML dialect), stop. AUTOSAR is the predicate.
- Mid-release checkpoint: at the 8-person-week mark, recheck that the baseline-diff engine is implemented and tested on a baseline corpus.

**Step 6 -- Ihdina as-Sirat al-Mustaqim.**
1. ARXML graph extractor (testable: 50 ARXML files extract correctly).
2. Four cross-layer checks (testable: each runs against the graph).
3. Baseline-diff engine (testable: scan v1 against scan v2 of same corpus produces stable diff).
4. baseline-scan UX (Roadmap Step 2 surface).

**Step 7 -- Sirat Alladhina.**
- Worked: graph-based extraction patterns from prior work.
- Failed: do not let one specific Tier-1's ARXML dialect become the de-facto AUTOSAR predicate.
- Cow Episode warning: do not invent cross-layer checks beyond the four named. The fifth+ checks are future work.

**Tier grade:** Tier 2 framework + specific implementation candidate. Tier 2 -> Tier 1 promotion pending F5 + STANDARD-tier audit + Tier-1 customer pilot acceptance.

**Falsification block F5 (proposer-drafted seed; §5.4 re-authoring required).**
```
Import: AUTOSAR ARXML graph extractor + four cross-layer reconciliation
  checks + baseline-diff engine.

Tier-1 claim: v1.4.0 detects cross-layer divergence at each of the four
  reconciliation surfaces with detection power statistically
  distinguishable from random-baseline (50% per binary call), AND the
  baseline-diff engine produces a deterministic diff on unchanged corpus
  (zero diff on two runs of the same input).

Falsifying observable: (a) any one of the four cross-layer checks
  produces a detection rate not statistically distinguishable from
  random-50% baseline at the 0.05 significance level across N=20
  per-check fixtures (10 matched + 10 injected); OR (b) the baseline-
  diff engine produces a non-zero diff on any pair of identical-input
  runs across the v1.4.0 release-test corpus.

Statistic / threshold: per-check, one-sided binomial test (H0:
  detection probability = 0.5; H1: > 0.5) at 0.05 significance level
  across N=10 injected fixtures per check (4 checks x 10 fixtures =
  40 injected total). For the baseline-diff engine, exact-zero diff
  test (binary pass/fail) across the release-test corpus (100 ARXML
  files run twice each). Power analysis: per Cohen 1988, N=10 per
  check at detection probability 0.95 gives ~0.86 power against H0=0.5
  at 0.05 significance.

Data source: F5 fixture corpus: 40 injected-divergence ARXML pairs
  (10 per check) + 40 matched ARXML pairs (10 per check) + 100 ARXML
  files for baseline-diff stability. Comparator chain: AUTOSAR
  schema-validating parser as substrate-actual; each per-check
  reference-implementation as ground-truth.

Decision rule: if per-check threshold not met for any of the four
  checks, the failing check ships as v1.4.0.X future work; the
  release ships at reduced check coverage. If baseline-diff engine
  produces non-zero diff on identical input, the engine is not
  ship-ready and the release does not ship.

Discriminating-test verification: binomial tests and exact-zero
  diff tests are mechanical. The cross-layer reconciliation
  surfaces (SWC<->ECU, data-mapping<->signal-database, runnable<->
  task-priority, safety-claim<->implementation) are AUTOSAR-standard
  surfaces independent of Bayyinah-internal categorization. The
  comparator (AUTOSAR schema parser; per-check reference impls)
  is external substrate.
```

**Closing dua:** Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

---

### 5.3 Release v1.10.0 (ELF binary substrate + FRaZ default rules, automotive ECU anchor)

**Step 1 -- Bismillah.**
- Authority source: regulated automotive software ships as ELF binaries, not as C source. A scanner that cannot see the binary cannot verify that the binary corresponds to the ARXML+source claim. ELF binary substrate is the load-bearing extractor for paid-contract automotive pilots.
- Purpose hierarchy: as v1.4.0.
- Technical objective: extract per-function control-flow-graph and per-symbol metadata from ELF binaries, with stable cross-build fingerprints; ship default-rules-on-by-default (Roadmap Step 3 UX surface).
- In-scope: ELF64 (x86_64 and aarch64); DWARF debuginfo where present; stripped-debuginfo fallback to symbol-table-only mode; per-function CFG via standard disassembly (capstone or similar).
- Out-of-scope: ELF32 (register as v1.10.0.1); macOS Mach-O (register as v1.10.0.2); Windows PE (register as v1.10.0.3); decompilation to source-like form (register as research problem).

**Step 2 -- Alhamdulillah.**
- Inherited: v1.4.0 ARXML+source substrate; multi-layer reconciliation discipline.
- Stable: parity discipline; cross-layer checker pattern.
- Missing: ELF parser; DWARF reader; CFG extractor; stable binary fingerprint.
- Available: pyelftools; capstone; lief; dwarf libraries.

**Step 3 -- Ar-Rahman ar-Rahim.**
- MDL: one ELF substrate class. CFG is a substrate-shape on top, not a separate substrate.
- Reused: substrate-vs-surface separation; parity discipline.
- FRaZ calibration: a "full decompilation" stage was considered; dropped because decompilation is a separate research problem and Bayyinah's purpose is verification, not reverse engineering.
- **PMD §3A.1 cell -> tier**: {HIGH-risk, substrate-modifying-but-bounded} -> STANDARD. Third empirical witness for the STANDARD cell. ELF substrate is structurally bounded (the ELF format is well-defined; the CFG extraction is mechanical).
- **PMD §3A.2 binding gate**: not required.

**Step 4 -- Maliki Yawm ad-Din.**
- Time budget: 12 person-weeks headline = 18 person-weeks adjusted.
- 20% skip rule: aarch64 support is pre-authorized to skip into v1.10.0.X if x86_64 alone consumes budget.

**Step 5 -- Iyyaka Na'budu.**
- Drift indicator: if the parser starts treating one ECU vendor's binary layout as the predicate, stop. ELF is the predicate.
- Mid-release checkpoint: at the 9-person-week mark, recheck that the binary fingerprint is stable across two builds of identical source on the same toolchain.

**Step 6 -- Ihdina as-Sirat al-Mustaqim.**
1. ELF parser (testable: 100 ELF binaries parse correctly).
2. DWARF debuginfo reader (testable: 50 with-DWARF binaries extract function info).
3. CFG extractor (testable: per-function CFG correct against ground-truth disassembly).
4. Stable binary fingerprint (testable: bit-stable across two builds).
5. FRaZ default-on rules.

**Step 7 -- Sirat Alladhina.**
- Worked: parity discipline from document substrate.
- Failed: do not let "the binary is opaque" become an excuse. Disassembly is mechanical.
- Cow Episode warning: do not invent a "binary semantics" predicate. CFG plus symbol metadata is the predicate.

**Tier grade:** Tier 2 framework + specific implementation candidate. Tier 2 -> Tier 1 promotion pending F6 + STANDARD-tier audit + ECU-pilot acceptance.

**Falsification block F6 (proposer-drafted seed; §5.4 re-authoring required).**
```
Import: ELF binary substrate extractor + per-function CFG + stable
  cross-build fingerprint.

Tier-1 claim: v1.10.0 successfully extracts per-function CFG and a
  bit-stable fingerprint from at least an effect-size-grounded
  fraction of an N=200 ELF binary corpus, sampled across the supported
  architectures and debuginfo classes.

Falsifying observable: across the N=200 ELF binary corpus (50 each of
  {x86_64 with full DWARF, x86_64 stripped, aarch64 with full DWARF,
  aarch64 stripped}), the parser-success-rate is below the pre-
  registered threshold OR the binary-fingerprint produces a non-
  identical fingerprint on two consecutive builds of an identical
  source-toolchain pair for any binary in the corpus.

Statistic / threshold: one-sided binomial test on parser-success-rate
  (H0: success probability = 0.90 baseline-acceptable; H1: success
  probability >= 0.95 engineering-target). Pre-registered threshold:
  parser-success-rate >= 0.95 across N=200 (lower 95% one-sided
  Clopper-Pearson CI >= 0.92). Power analysis: N=200 at target 0.95
  vs. baseline 0.90 gives >0.85 power at 0.05 significance per Cohen
  1988 binomial power tables. For fingerprint stability: exact-zero
  non-stable-fingerprint test across the binary subset that has two
  builds (50 binaries x 2 builds).

Data source: F6 fixture corpus: 200 ELF binaries sourced from
  automotive Tier-1 build outputs (where available under NDA) +
  open-source equivalents (e.g., AGL/ROS2 ECU-style builds);
  fingerprint stability corpus of 50 binaries built twice via
  identical toolchain. Comparator chain: pyelftools and capstone as
  substrate-actual format parsers; reproducible-builds.org methodology
  as fingerprint-stability ground truth.

Decision rule: if parser-success-rate threshold not met, the failing
  binary class (e.g., stripped-aarch64) is registered as v1.10.0.X
  future work; the release ships at narrowed architecture-debuginfo
  coverage. If any fingerprint is non-identical on two identical-
  toolchain builds, the fingerprint surface is not ship-ready and
  the release does not ship until the fingerprint stabilizes.

Discriminating-test verification: parser-success-rate is mechanical
  (binary either parses to a CFG or it does not). Fingerprint
  stability is mechanical (bit-compare two SHA256 digests). Both
  use external substrate (pyelftools, capstone, reproducible-builds.
  org) independent of Bayyinah-internal categorization or R1-R11
  vocabulary.
```

**Closing dua:** Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

---

### 5.4 Release v1.4.1 (AUTOSAR + ELF binary pairing + budget UX, paid-contract gate)

**Step 1 -- Bismillah.**
- Authority source: a Tier-1 paying-customer pilot requires the binary-vs-config reconciliation that v1.4.0 + v1.10.0 each provide separately. v1.4.1 is the integration release that closes the binary-pairing gate for the first paid contract.
- Purpose hierarchy: as v1.4.0.
- Technical objective: cross-substrate reconciliation between ARXML SWC-implementation declarations and ELF binary symbol set. Ship explicit scan-budget UX (Roadmap Step 4).
- In-scope: ARXML SWC-impl-set; ELF binary symbol set; declared-vs-actual reconciliation; budget-aware scan that returns "scan partial; future-work registered" when budget exhausted.
- Out-of-scope: dynamic-linking edge cases (register as v1.4.1.1); compiler-generated symbols (register as v1.4.1.2).

**Step 2 -- Alhamdulillah.**
- Inherited: v1.4.0 ARXML; v1.10.0 ELF.
- Stable: cross-layer checker pattern from v1.4.0.
- Missing: ARXML <-> ELF reconciliation check; budget-aware scan controller.
- Available: v1.4.0 + v1.10.0 substrate.

**Step 3 -- Ar-Rahman ar-Rahim.**
- MDL: one new cross-layer check on top of v1.4.0's four. Not a new framework.
- Reused: ARXML graph extractor; ELF parser; cross-layer checker pattern.
- FRaZ calibration: a "scan the linker map" stage was considered; deferred to v1.4.1.X.
- **PMD §3A.1 cell -> tier**: {HIGH-risk, substrate-modifying-but-bounded} -> STANDARD. v1.4.1 is the integration release; substrate-modification is bounded to the one new check.
- **PMD §3A.2 binding gate**: not required.

**Step 4 -- Maliki Yawm ad-Din.**
- Time budget: 5 person-weeks headline = 7.5 person-weeks adjusted.
- 20% skip rule: compiler-generated-symbol handling is pre-authorized to skip into v1.4.1.X.

**Step 5 -- Iyyaka Na'budu.**
- Drift indicator: if the reconciliation check accumulates per-Tier-1-supplier exceptions, stop.
- Mid-release checkpoint: at the 4-person-week mark, recheck that the budget controller produces honest partial-scan outputs.

**Step 6 -- Ihdina as-Sirat al-Mustaqim.**
1. ARXML SWC-impl extractor (testable).
2. ELF symbol-set extractor reuse (testable).
3. Reconciliation check (testable: 20 paired fixtures).
4. Budget controller (testable: 5 over-budget fixtures return partial-scan honestly).

**Step 7 -- Sirat Alladhina.**
- Worked: cross-layer checker pattern from v1.4.0.
- Failed: prior attempts to over-scope binary reconciliation (decompilation territory).
- Cow Episode warning: do not invent "the perfect reconciliation." Substrate-vs-substrate is the predicate.

**Tier grade:** Tier 2 framework + specific implementation candidate. Tier 2 -> Tier 1 promotion pending F7 + paid-pilot acceptance.

**Falsification block F7 (proposer-drafted seed; §5.4 re-authoring required).**
```
Import: ARXML SWC-impl <-> ELF binary symbol set reconciliation +
  budget-aware partial-scan controller.

Tier-1 claim: v1.4.1 detects ARXML-impl-declaration-vs-binary-symbol-
  set divergence (extra symbols, missing symbols, mismatched signatures)
  at detection power statistically distinguishable from random-baseline
  AND the budget controller returns honest partial-scan output (the
  "scan exceeded budget; X% complete; missing areas Y, Z registered as
  future work" output) on every over-budget input.

Falsifying observable: (a) detection rate not statistically
  distinguishable from random-50% baseline at 0.05 significance across
  N=20 injected-divergence ARXML+ELF pairs; OR (b) any over-budget
  scan returns a "scan complete" status when budget was actually
  exhausted (dishonest partial output, the Munafiq Protocol case
  applied to v1.4.1's own scan controller).

Statistic / threshold: one-sided binomial test on detection rate
  (H0: detection probability = 0.5; H1: > 0.5) at 0.05 significance
  level across N=10 injected fixtures (10 of 20 paired fixtures
  carry an injected divergence). For budget controller: exact-zero
  count of dishonest-status outputs across N=15 over-budget fixtures.
  Power analysis: N=10 at detection probability 0.95 gives ~0.86
  power against H0=0.5 at 0.05.

Data source: F7 fixture corpus: 20 paired ARXML+ELF fixtures (10
  matched + 10 injected) + 15 over-budget fixtures. Comparator
  chain: AUTOSAR ARXML parser as substrate-actual for SWC-impl;
  pyelftools as substrate-actual for ELF symbols; scan-budget
  ledger as substrate-actual for budget consumption.

Decision rule: if detection-rate threshold not met, the release
  does not ship until extractor coverage is restored. If budget-
  controller honesty test fails on any single fixture, the
  controller is not ship-ready and the release does not ship.

Discriminating-test verification: the binomial test and exact-zero
  count are mechanical. The injection categories (extra symbols,
  missing symbols, mismatched signatures) are observable independent
  of Bayyinah-internal categorization. The comparators (AUTOSAR
  parser, pyelftools) are external substrate.
```

**Closing dua:** Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

---

### 5.5 Release v1.5.0 (ARINC-653 + Munafiq self-detect, avionics advisory anchor)

**Step 1 -- Bismillah.**
- Authority source: ARINC-653 partition-based avionics software is the substrate of DO-178C TQL-1 work. Bayyinah's Munafiq self-detect harness is the structural-honesty discipline applied to Bayyinah itself: the scanner must catch adversarial input designed to slip past it.
- Purpose hierarchy: (1) Allah; (2) avionics partition runtime; (3) aircraft occupants; (4) DO-178C compliance engineers; (5) certification authorities.
- Technical objective: extract ARINC-653 XML config + partition-implementation pairing; ship the Munafiq self-detect harness that flags adversarial fixtures.
- In-scope: ARINC-653 Part 1 XML; partition-impl pairing; Munafiq adversarial-test harness with 50-fixture seed corpus.
- Out-of-scope: ARINC-653 Part 2/3/4 (register per-part); IMA (Integrated Modular Avionics) integration (register as v1.5.0.X); DO-178C TQL-1 qualification close (this is the v2.0 gate).

**Step 2 -- Alhamdulillah.**
- Inherited: v1.4.1 cross-substrate reconciliation; substrate honesty discipline.
- Stable: cross-layer checker pattern.
- Missing: ARINC-653 extractor; Munafiq harness; adversarial-fixture corpus.
- Available: v1.4.1 substrate; the Munafiq Protocol research artifact (zenodo.19700420) as conceptual basis.

**Step 3 -- Ar-Rahman ar-Rahim.**
- MDL: ARINC-653 extractor reuses the cross-layer checker pattern. Munafiq harness is one new test-suite class.
- Reused: cross-layer checker; parity discipline.
- FRaZ calibration: a "full DO-178C qualification close" stage was considered; deferred to v2.0 (this is the gate, not a v1.5.0 deliverable).
- **PMD §3A.1 cell -> tier**: {HIGH-risk, substrate-modifying-broad-architecture} -> HEAVY. The Munafiq harness is a new safety-class verifier substrate; the §3A.1 HEAVY-regardless-surface enumeration binds. Multiple cross-vendor rotation sessions required.
- **PMD §3A.2 binding gate**: not applicable (HEAVY tier; no LIGHT discipline being claimed).

**Step 4 -- Maliki Yawm ad-Din.**
- Time budget: 10 person-weeks headline = 15 person-weeks adjusted.
- 20% skip rule: the Munafiq harness corpus can ship at 30 fixtures instead of 50 if the ARINC-653 extractor alone consumes the budget.

**Step 5 -- Iyyaka Na'budu.**
- Drift indicator: if the Munafiq harness starts looking like "adversarial input filtering" (cybersecurity territory), stop. The harness is for adversarial purpose-hierarchy violations, not arbitrary malicious input.
- Mid-release checkpoint: at the 7-person-week mark, recheck that the Munafiq harness flags the seed adversarial corpus.

**Step 6 -- Ihdina as-Sirat al-Mustaqim.**
1. ARINC-653 XML extractor.
2. Partition-impl reconciliation.
3. Munafiq harness skeleton.
4. Adversarial fixture corpus (50 fixtures).

**Step 7 -- Sirat Alladhina.**
- Worked: cross-substrate reconciliation from v1.4.1.
- Failed: prior research on Munafiq was conceptual; this release operationalizes it.
- Cow Episode warning: do not invent "the perfect adversarial test." The Munafiq Protocol's three processes are the predicate.

**Tier grade:** Tier 2 framework (ARINC-653 extractor) + Tier 2 specific implementation candidate (Munafiq harness). Tier 2 -> Tier 1 promotion pending F8 + HEAVY-tier multi-vendor audit + N>=2 adversarial-fixture cycles.

**Falsification block F8 (proposer-drafted seed; §5.4 re-authoring required).**
```
Import: Munafiq self-detect harness operating on a curated adversarial
  fixture corpus designed to pass v1.4.x cleanly while violating
  Bayyinah's purpose-hierarchy discipline.

Tier-1 claim: the Munafiq harness flags adversarial fixtures (true-
  positive rate above a pre-registered threshold) without producing
  excessive false positives on honest fixtures (false-positive rate
  below a pre-registered threshold).

Falsifying observable: across N=100 fixtures (50 adversarial + 50
  matched-honest), the Munafiq harness produces a (TPR, FPR) point
  outside the pre-registered operating-curve region.

Statistic / threshold: TPR >= 0.80 with 95% lower one-sided Clopper-
  Pearson bound on N=50 adversarial fixtures (lower bound >= 0.69
  is the gate); FPR <= 0.10 with 95% upper one-sided Clopper-Pearson
  bound on N=50 honest fixtures (upper bound <= 0.20 is the gate).
  Power analysis grounding: per Cohen 1988, N=50 per arm at TPR=0.80
  vs. random-50% baseline gives >0.99 power; the bound is set
  conservatively at 0.80 (not 0.95) because adversarial corpora are
  expected to be more difficult than nominal-divergence corpora.

Data source: F8 fixture corpus: 50 by-construction adversarial
  fixtures (each satisfies v1.4.x checks while violating purpose-
  hierarchy ordering via one of the Munafiq Protocol's three
  processes) + 50 matched-honest ARINC-653 fixtures. Comparator
  chain: the Munafiq Protocol research artifact (zenodo.19700420)
  process-1/process-2/process-3 definitions as adversarial ground
  truth; ARINC-653 schema as honest-fixture substrate.

Decision rule: if TPR threshold not met, the Munafiq harness is
  registered as v1.5.0-experimental (no avionics-pilot claim made);
  the harness ships but the v1.5.0 release is downgraded to v1.5.0-
  beta. If FPR threshold not met, the harness produces too many
  false alarms for advisory-pilot use; the release ships at reduced
  scope (ARINC-653 extractor only; Munafiq deferred to v1.5.X).

Discriminating-test verification: TPR/FPR are mechanical metrics.
  The adversarial-fixture construction follows the Munafiq Protocol's
  three processes (defined independently of Bayyinah-internal
  vocabulary). The comparator (Munafiq Protocol research artifact)
  is external substrate.
```

**Closing dua:** Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

---

### 5.6 Release v1.7.0 (IEC 61850 SCL + priority-remediation UX, power-grid anchor)

**Step 1 -- Bismillah.**
- Authority source: IEC 61850 SCL is the substation-automation configuration substrate. Cross-layer reconciliation between SCL files (SSD, SCD, CID, IID) is the structural-honesty discipline applied to power-grid substations.
- Purpose hierarchy: (1) Allah; (2) substation runtime; (3) grid customers (residential, industrial); (4) protection engineers; (5) regulatory authorities.
- Technical objective: extract IEC 61850 SCL with cross-layer reconciliation among SSD/SCD/CID/IID; ship priority-remediation UX (Roadmap Step 5).
- In-scope: IEC 61850-6:2024 SCL; the four named SCL artifacts; cross-layer reconciliation.
- Out-of-scope: COMTRADE waveform data (register); GOOSE/SV runtime packet capture (register as live-monitoring research).

**Step 2 -- Alhamdulillah.**
- Inherited: v1.5.0 substrate.
- Stable: cross-layer checker pattern.
- Missing: SCL extractor; four-way reconciliation; remediation-priority sorter.
- Available: libiec61850; openSCL-tools.

**Step 3 -- Ar-Rahman ar-Rahim.**
- MDL: one SCL extractor with four reconciliation methods. Not four extractors.
- Reused: cross-layer checker; parity discipline.
- FRaZ calibration: a "scan IED firmware" stage was considered; deferred to v1.7.1.
- **PMD §3A.1 cell -> tier**: {HIGH-risk, substrate-modifying-but-bounded} -> STANDARD. The SCL XML format is well-defined; reconciliation pattern inherits from v1.4.0.
- **PMD §3A.2 binding gate**: not required.

**Step 4 -- Maliki Yawm ad-Din.**
- Time budget: 9 person-weeks headline = 13.5 person-weeks adjusted.
- 20% skip rule: IID-pairing is pre-authorized to skip into v1.7.0.X.

**Step 5 -- Iyyaka Na'budu.**
- Drift indicator: if the SCL extractor accumulates per-utility-vendor quirks, stop. IEC 61850 is the predicate.
- Mid-release checkpoint: at the 7-person-week mark, recheck remediation-priority output is engineer-actionable.

**Step 6 -- Ihdina as-Sirat al-Mustaqim.**
1. SCL extractor.
2. Four-way reconciliation.
3. Remediation-priority sorter.
4. Priority-remediation UX (Roadmap Step 5 surface).

**Step 7 -- Sirat Alladhina.**
- Worked: AUTOSAR cross-layer reconciliation pattern from v1.4.0.
- Failed: do not let one specific IED vendor's SCL dialect become the predicate.
- Cow Episode warning: do not invent SCL extensions. IEC 61850-6 is the predicate.

**Tier grade:** Tier 2 framework + specific implementation candidate. Tier 2 -> Tier 1 promotion pending F9 + STANDARD-tier audit + power-grid-pilot acceptance.

**Falsification block F9 (proposer-drafted seed; §5.4 re-authoring required).**
```
Import: IEC 61850 SCL extractor + four-way cross-layer reconciliation +
  engineer-actionable remediation-priority sorter.

Tier-1 claim: v1.7.0 detects SCL cross-layer divergence at detection
  power statistically distinguishable from random-baseline AND
  produces remediation strings that protection engineers (domain
  experts) can act on without re-interpretation.

Falsifying observable: (a) detection-rate not statistically
  distinguishable from random-50% baseline at 0.05 significance
  across N=10 per-check injected fixtures; OR (b) blinded domain-
  expert review of the remediation strings reports re-interpretation-
  required rate above the pre-registered threshold.

Statistic / threshold: per-check binomial test on detection rate
  (H0=0.5; H1>0.5) at 0.05 significance across N=10 injected
  fixtures per check (4 checks x 10 = 40 injected). For remediation-
  string actionability: blinded review by N>=3 protection engineers,
  each rating each remediation string as "actionable as-is,"
  "actionable after clarification," or "requires re-interpretation";
  pre-registered threshold: "requires re-interpretation" rate < 0.20
  across the corpus (lower bound: per-engineer 95% one-sided
  Clopper-Pearson upper bound on "requires re-interpretation" rate
  must be <= 0.30 across the per-engineer review set). Power
  analysis: N=10 per-check at 0.95 detection probability gives
  ~0.86 power at 0.05 significance; N=3 engineers reviewing 40
  remediation strings each provides ~120 ratings, sufficient power
  to discriminate 0.20 vs. 0.40 actionability-failure rates at 0.05
  significance.

Data source: F9 fixture corpus: 40 injected-divergence SCL fixtures
  (10 per check across four checks) + 40 matched honest SCL fixtures.
  Comparator chain: IEC 61850-6 schema-validating parser as
  substrate-actual; N>=3 blinded protection engineers as ground-
  truth for remediation actionability.

Decision rule: if per-check detection threshold not met, the failing
  check ships as v1.7.0.X future work. If remediation-actionability
  threshold not met, the priority-remediation UX is downgraded to
  v1.7.0-beta until engineer-actionable form is achieved.

Discriminating-test verification: binomial tests are mechanical;
  the blinded engineer review uses external protection engineers
  (independent of Bayyinah-internal vocabulary). IEC 61850-6 schema
  parser is external substrate.
```

**Closing dua:** Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

---

## 6. Phase 3 -- Cross-industry releases (v1.8.0, v1.9.0, v1.6.0)

These three releases tie the per-industry pillars into cross-industry surfaces. They ship after the industry-pilot acceptance gates are met.

### 6.1 Releases v1.8.0 + v1.9.0 (SBOM + in-toto/SLSA + patterns UX, cross-industry supply chain)

**Step 1 -- Bismillah.**
- Authority source: SBOM (CISA mandate) + in-toto/SLSA (CNCF supply-chain framework) is the cross-industry supply-chain attestation surface. Bayyinah's source-SBOM-binary projection consistency check is the structural-honesty discipline applied to the regulated supply chain.
- Purpose hierarchy: (1) Allah; (2) downstream consumers of signed artifacts; (3) regulatory authorities; (4) supplier engineers; (5) software supply chain.
- Technical objective: extract SBOMs (SPDX + CycloneDX); operate on in-toto attestations + SLSA provenance; detect source-SBOM-binary projection inconsistency; ship patterns UX (Roadmap Step 6).
- In-scope: SPDX 2.3; CycloneDX 1.6; in-toto 1.0 attestations; SLSA v1.0 provenance; source <-> SBOM <-> binary three-way reconciliation.
- Out-of-scope: GUAC integration (register); CycloneDX VEX (register).

**Step 2 -- Alhamdulillah.**
- Inherited: v1.7.0 substrate; v1.10.0 ELF substrate.
- Stable: cross-layer checker pattern.
- Missing: SBOM extractors (2); in-toto + SLSA parsers; three-way reconciliation; patterns-UX rendering.
- Available: spdx-tools; cyclonedx-python-lib; in-toto-python; sigstore.

**Step 3 -- Ar-Rahman ar-Rahim.**
- MDL: one SBOM extractor base class with two subclasses (SPDX, CycloneDX). One in-toto+SLSA parser. One three-way reconciliation checker on top.
- Reused: cross-layer checker.
- FRaZ calibration: a "scan the dependency-graph transitively" stage was considered; deferred (transitively-deep SBOM analysis is its own research problem).
- **PMD §3A.1 cell -> tier**: {HIGH-risk, substrate-modifying-broad-architecture} -> HEAVY. v1.8.0/v1.9.0 are Sigstore-signing-surface CHANGES (in-toto/SLSA layer); HEAVY-regardless-surface enumeration binds per §3A.1.
- **PMD §3A.2 binding gate**: not applicable (HEAVY tier).

**Step 4 -- Maliki Yawm ad-Din.**
- Time budget: 16 person-weeks headline for v1.8.0 + v1.9.0 combined = 24 person-weeks adjusted.
- 20% skip rule: SLSA v1.0 provenance can ship at "consume only" if attestation generation alone consumes budget; v1.9.0.X registers the generation surface.

**Step 5 -- Iyyaka Na'budu.**
- Drift indicator: if the SBOM extractors accumulate per-supplier exceptions, stop.
- Mid-release checkpoint: at the 12-person-week mark, recheck three-way reconciliation produces stable findings on a baseline corpus.

**Step 6 -- Ihdina as-Sirat al-Mustaqim.**
1. SPDX extractor.
2. CycloneDX extractor.
3. in-toto attestation parser.
4. SLSA provenance parser.
5. Three-way reconciliation checker.
6. Patterns UX (Roadmap Step 6).

**Step 7 -- Sirat Alladhina.**
- Worked: cross-layer checker pattern.
- Failed: prior attempts at "complete SBOM auditing" without scope.
- Cow Episode warning: do not invent "the perfect supply chain check." Source-SBOM-binary projection is the predicate.

**Tier grade:** Tier 2 framework + specific implementation candidate. Tier 2 -> Tier 1 promotion pending F10 + HEAVY-tier audit + at least one cross-industry pilot acceptance.

**Falsification block F10 (proposer-drafted seed; §5.4 re-authoring required).**
```
Import: SBOM (SPDX + CycloneDX) + in-toto/SLSA + source-SBOM-binary
  three-way projection-consistency check.

Tier-1 claim: v1.8.0 + v1.9.0 detects source-SBOM-binary projection
  inconsistency at detection power statistically distinguishable from
  random-baseline across the three named inconsistency categories
  (extra-dependency-in-SBOM-not-in-source, binary-symbol-not-
  justified-by-source-declaration, sigstore-signature-mismatch).

Falsifying observable: across N=30 paired (source, SBOM, binary)
  fixtures (15 matched + 15 injected, spanning automotive Tier-1
  and medical-device industries), the detection rate is not
  statistically distinguishable from random-50% baseline at 0.05
  significance level on the injected sub-corpus.

Statistic / threshold: one-sided binomial test on injected-fixture
  detection rate (H0=0.5; H1>0.5) at 0.05 significance across N=15
  injected fixtures (5 per inconsistency category). Pre-registered
  threshold: pooled binomial p-value < 0.05; per-category binomial
  p-value < 0.10. Power analysis: N=15 pooled at detection
  probability 0.93 gives >0.92 power at 0.05 significance; per-
  category N=5 at 0.95 detection probability gives ~0.80 power at
  0.10 per Cohen 1988.

Data source: F10 fixture corpus: 30 paired (source, SBOM, binary)
  fixtures, half from automotive Tier-1 representative builds and
  half from medical-device representative builds (where NDA permits;
  otherwise open-source equivalents per industry shape). Comparator
  chain: SPDX/CycloneDX schema validators; in-toto/SLSA verifiers;
  sigstore as substrate-actual for signature ground-truth.

Decision rule: if pooled OR per-category threshold not met, the
  failing category is registered as v1.8.0.X / v1.9.0.X future work;
  the release ships at narrowed category coverage. If sigstore-
  signature-mismatch detection specifically fails, the v1.9.0
  release does not ship until sigstore integration is corrected
  (this is the Sigstore-surface integrity gate).

Discriminating-test verification: the binomial test is mechanical;
  inconsistency categories are observable independent of Bayyinah-
  internal vocabulary; comparators are external substrate.
```

**Closing dua:** Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

---

### 6.2 Release v1.6.0 (IEC 61131-3 PLCopen + strength-n stack v1.0, nuclear anchor)

**Step 1 -- Bismillah.**
- Authority source: IEC 61131-3 + PLCopen is the substrate of nuclear safety I&C software. The strength-n agreement stack (Python + Rust + Go cross-port byte-identical agreement) is the structural-honesty discipline applied to Bayyinah at the cross-implementation layer.
- Purpose hierarchy: (1) Allah; (2) nuclear plant I&C runtime; (3) plant operators; (4) regulatory authorities (NRC); (5) plant owners.
- Technical objective: extract IEC 61131-3 PLCopen XML + ship strength-n stack v1.0 with three port-language agreement.
- In-scope: IEC 61131-3 PLCopen XML; Python + Rust + Go ports of the core scanner; strength-n agreement checker.
- Out-of-scope: full IEC 60880 qualification (this is the long-tail nuclear gate); ports beyond Python/Rust/Go (register).

**Step 2 -- Alhamdulillah.**
- Inherited: v1.7.0 cross-layer reconciliation; v1.8.0/v1.9.0 patterns UX; pre-existing port-language work (separate research effort).
- Stable: parity discipline.
- Missing: PLCopen extractor; strength-n agreement primitive.
- Available: PLCopen-tools.

**Step 3 -- Ar-Rahman ar-Rahim.**
- MDL: PLCopen extractor reuses the cross-layer reconciliation pattern. Strength-n is one new primitive that compares three independent implementations' outputs.
- Reused: parity discipline.
- FRaZ calibration: a "cross-formal-verification" stage was considered; deferred to v2.0 trust-and-falsification.
- **PMD §3A.1 cell -> tier**: {HIGH-risk, substrate-modifying-broad-architecture} -> HEAVY. The strength-n primitive is a new safety-class invariant additions (HEAVY-regardless-surface enumeration binds per §3A.1).
- **PMD §3A.2 binding gate**: not applicable.

**Step 4 -- Maliki Yawm ad-Din.**
- Time budget: 14 person-weeks headline = 21 person-weeks adjusted.
- 20% skip rule: nuclear-specific extension pack can ship at v1.6.0.X if the PLCopen extractor + strength-n stack alone consume budget.

**Step 5 -- Iyyaka Na'budu.**
- Drift indicator: if the strength-n stack starts looking like CI parallelism (mere "run all three and average"), stop. The discipline is byte-identical agreement, not averaging.
- Mid-release checkpoint: at the 10-person-week mark, recheck strength-n produces bit-identical agreement on a sample corpus.

**Step 6 -- Ihdina as-Sirat al-Mustaqim.**
1. PLCopen extractor.
2. Strength-n agreement primitive.
3. Three-port integration (Python + Rust + Go).
4. Strength-n agreement test (testable: 100 fixtures produce bit-identical agreement OR registered disagreement).

**Step 7 -- Sirat Alladhina.**
- Worked: parity discipline.
- Failed: prior cross-implementation work that "almost agreed" -- the strength-n gate is exact-byte-identical, not approximate.
- Cow Episode warning: do not invent a "fuzzy agreement metric." Bit-identical is the predicate.

**Tier grade:** Tier 2 framework + specific implementation candidate. Tier 2 -> Tier 1 promotion pending F11 + HEAVY-tier audit + nuclear-pilot acceptance.

**Falsification block F11 (proposer-drafted seed; §5.4 re-authoring required).**
```
Import: strength-n cross-port agreement primitive operating on
  Bayyinah-Python + Bayyinah-Rust + Bayyinah-Go ports.

Tier-1 claim: across the F11 release-gate corpus, the three ports
  produce bit-identical findings (by canonical-findings-serialization
  bit-equality) on at least an effect-size-grounded fraction of the
  corpus; the remaining fixtures (n_disagree <= 5 of 100) are
  registered as corrigenda with a named scope-limitation per port.

Falsifying observable: across N=100 PLCopen fixtures, the bit-
  identical-agreement rate is below the pre-registered threshold,
  OR any disagreement is "silent" (a port returns a finding the
  other two ports do not produce, without being either registered
  as a port-scope corrigendum or flagged as a blocking finding).

Statistic / threshold: bit-identical-agreement rate >= 0.95 with
  95% lower one-sided Clopper-Pearson bound (the gate). Exact-zero
  count of silent disagreements (binary pass/fail). Power analysis
  grounding: this is an invariance-class test for the bit-identical
  metric; N=100 at the 0.95 target rate gives lower CI bound at
  ~0.89 (acceptable for the v1.6.0-rc gate). For the silent-
  disagreement test: invariance-class, deterministic; N=100 sets
  test diversity.

Data source: F11 release-gate corpus: 100 PLCopen fixtures spanning
  nuclear-I&C representative shapes. Comparator chain: each port's
  output as substrate-actual; the canonical-findings-serialization
  bit-equality check as comparator primitive.

Decision rule: if bit-identical-agreement rate below threshold AND
  cause is a port-scope drift, the affected port ships at v1.6.0-rc
  status with the drift registered as a corrigendum; the strength-n
  SKU does not GA-ship until rate clears threshold. If silent-
  disagreement count > 0, no shipping until the silent disagreement
  is either reclassified as a registered scope-limit corrigendum or
  resolved.

Discriminating-test verification: bit-equality is mechanical and
  uses no Bayyinah-internal vocabulary. The three ports are
  independent substrate implementations.
```

**Closing dua:** Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

---

## 7. Phase 4 -- Binary-pairing completions (v1.5.1, v1.6.1, v1.7.1)

These three releases complete the binary-pairing surface for ARINC-653, PLCopen, and SCL. They are structurally identical to v1.4.1's pattern: cross-substrate reconciliation between the industry config and the runtime binary.

### 7.1 v1.5.1 (ARINC-653 + ELF), v1.6.1 (PLCopen + ELF), v1.7.1 (SCL + IED-firmware)

Each follows the v1.4.1 template:
- Reuse the v1.10.0 binary substrate.
- Add per-industry binary-pairing reconciliation check.
- Ship the matching budget UX where it was deferred from the corresponding industry-entry release.

**PMD §3A.1 cell -> tier** (all three): {HIGH-risk, substrate-modifying-but-bounded} -> STANDARD. Binary-pairing inherits from v1.4.1 + v1.10.0 substrate.

**Tier grade (all three):** Tier 2 framework + specific implementation candidate. Tier 2 -> Tier 1 promotion pending F12 instances + STANDARD-tier audit per release.

**Falsification block F12 (applies to each of v1.5.1, v1.6.1, v1.7.1; proposer-drafted seed; §5.4 re-authoring required per release).**
```
Import: per-pairing cross-substrate reconciliation check between
  industry config and runtime binary (ARINC-653<->ELF, PLCopen<->ELF,
  SCL<->IED-firmware).

Tier-1 claim: each v1.X.1 release detects config-vs-binary divergence
  at detection power statistically distinguishable from random-50%
  baseline.

Falsifying observable: across N=20 paired fixtures per release (10
  matched + 10 injected), the per-release detection rate is not
  statistically distinguishable from random-50% baseline at 0.05
  significance.

Statistic / threshold: per-release, one-sided binomial test on
  detection rate (H0=0.5; H1>0.5) at 0.05 significance across N=10
  injected fixtures per release. Power analysis: N=10 at 0.95
  detection probability gives ~0.86 power at 0.05.

Data source: F12 fixture corpus per release: 20 paired fixtures
  (10 matched + 10 injected). Comparator chain: industry-config
  parser (ARINC-653 / PLCopen / IEC 61850 SCL) + binary substrate
  parser (pyelftools for ELF; per-IED-vendor firmware parser for
  v1.7.1).

Decision rule: per-release, if detection threshold not met, that
  v1.X.1 release does not ship until the pairing check is corrected;
  the corresponding industry pilot is informed.

Discriminating-test verification: binomial test is mechanical;
  injection categories are industry-substrate-shaped, not Bayyinah-
  internal-shaped; comparators are external substrate.
```

**Closing dua per release:** Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

---

## 8. Phase 5 -- Tier-3 extractor releases (v1.11.0 -- v1.14.0)

These four releases enter the Tier-3 industries (CAD interchange, DICOM medical imaging, HL7 healthcare, financial messaging) at advisory-pilot tier. Each follows the industry-entry template (a single new extractor family + the corresponding cross-layer reconciliation discipline).

**Per-release calibration:** all four are {HIGH-risk, substrate-modifying-but-bounded} -> STANDARD per PMD §3A.1, inheriting from the v1.3.0 / v1.4.0 / v1.7.0 industry-entry pattern.

**Tier grade (all four):** Tier 2 framework + specific implementation candidate per release. Tier 2 -> Tier 1 promotion pending the named F-block + STANDARD-tier audit + advisory-pilot signal.

**Falsification blocks F13-F16** (proposer-drafted seeds; §5.4 re-authoring required per release). Each follows the schema:
```
Import: per-industry extractor + within-substrate cross-layer
  reconciliation check.

Tier-1 claim: each v1.1N release detects industry-specific divergence
  at detection power statistically distinguishable from random-50%
  baseline across N=20 paired per-check fixtures (10 matched + 10
  injected).

Falsifying observable: per-release detection rate not statistically
  distinguishable from random-50% baseline at 0.05 significance
  across the injected sub-corpus.

Statistic / threshold: per-release, one-sided binomial test (H0=0.5;
  H1>0.5) at 0.05 across N=10 injected fixtures. Power analysis per
  Cohen 1988.

Data source: F13 (v1.11.0 STEP/IGES) -- 20 STEP fixtures, 10 with
  injected geometry-vs-metadata divergence; F14 (v1.12.0 DICOM) --
  20 DICOM fixtures, 10 with injected DICOM-dataset-vs-DICOMDIR
  divergence; F15 (v1.13.0 HL7) -- 20 FHIR fixtures, 10 with
  injected Bundle-resource-vs-referenced-resource divergence; F16
  (v1.14.0 Financial) -- 20 FIX/SWIFT/ISO 20022 fixtures, 10 with
  injected message-header-vs-body divergence. Comparator chains:
  STEP/IGES schema parser; DICOM standard parser; FHIR R5 validator;
  FIX/SWIFT/ISO 20022 schema parsers.

Decision rule: per-release, if detection threshold not met, the
  release ships at narrowed scope (one of the per-extractor sub-
  surfaces deferred) and the failing check is registered as the
  next per-extractor patch.

Discriminating-test verification: per-release binomial test is
  mechanical; injection categories follow industry-substrate shape;
  comparators are external substrate.
```

**Closing dua per release.**

---

## 9. The terminal session -- Release v2.0.0 (Trust-and-falsification gate)

This is the Fatiha Construct session that produces v2.0.0. It is not "the release where we add more features." It is the release that **closes the falsification loop on the framework itself**.

### 9.1 Release v2.0.0 (Trust-and-falsification)

**Step 1 -- Bismillah.**
- Authority source: trust in regulated software is earned by independent verification of the verifier. v2.0.0 is the release where Bayyinah passes its own scan, by an instance other than the producing instance, on a fixture corpus the producing instance did not author. This is the structural-honesty discipline applied recursively to the framework.
- Purpose hierarchy: (1) Allah; (2) AI systems consuming Bayyinah outputs; (3) human users at regulated entities; (4) the open-source community; (5) the BayyinahEnterprise commercial offering.
- Technical objective: ship the trust-and-falsification gate -- (a) the strength-n stack on the v2.0 release-gate corpus; (b) the third-party-authored corpus passes; (c) the operational falsification bounty program; (d) TQL-1 qualification close on at least one customer-program PSAC.
- In-scope: the four named gate conditions; the v2.0 release-gate corpus authorship and publication; the falsification bounty program operational launch.
- Out-of-scope: feature-additive surfaces (none of those ship in v2.0; v2.0 is the gate, not a new extractor family). Any feature in flight at v2.0-rc is held to v2.1.

**Step 2 -- Alhamdulillah.**
- Inherited: every prior release.
- Stable: all prior extractor families; strength-n stack v1.0 from v1.6.0.
- Missing: the v2.0 release-gate corpus (authored by external contributor); the falsification bounty program operational; the TQL-1 PSAC closure.
- Available: every prior fixture, every prior corrigendum, every prior cross-layer checker.

**Step 3 -- Ar-Rahman ar-Rahim.**
- MDL: v2.0.0 ships **no new extractor family**. The MDL of v2.0 is the smallest gate that closes the falsification loop.
- Reused: every prior release.
- FRaZ calibration: a "v2.0 with new flagship feature X" framing was considered; rejected. v2.0 IS the gate; the gate IS the feature.
- **PMD §3A.1 cell -> tier**: {HIGH-risk, substrate-modifying-broad-architecture} -> HEAVY. v2.0 qualifies as new attestation surface for TQL-1 qualification close (HEAVY-regardless-surface enumeration binds per §3A.1).
- **PMD §3A.2 binding gate**: not applicable (HEAVY tier; the release-itself-is-the-gate).
- **PMD §3B.6 operational pool**: full four-vendor fresh-instance team + three-vendor continuity-mode team required at v2.0 final audit per §3B.3.

**Step 4 -- Maliki Yawm ad-Din.**
- Time budget: 20 person-weeks headline = 30 person-weeks adjusted.
- 20% skip rule: TQL-1 qualification close can ship at "PSAC submitted; FAA acceptance pending" if the other three gate conditions are met. The release ships as v2.0-rc until TQL-1 closes; v2.0 GA when TQL-1 accepts.

**Step 5 -- Iyyaka Na'budu.**
- Drift indicator: if any temptation arises to add "just one more feature" before v2.0 ships, stop. v2.0 ships when the gate closes, not when feature scope grows.
- Mid-release checkpoint: at the 16-person-week mark, recheck that the external-contributor corpus is authored, the bounty program is launched, and the strength-n stack is producing bit-identical agreement.

**Step 6 -- Ihdina as-Sirat al-Mustaqim.**
1. External-contributor corpus (testable: at least one contributor outside the core team has authored a v2.0 release-gate fixture corpus).
2. Bayyinah scans Bayyinah (testable: Bayyinah-Python is scanned-clean by Bayyinah-Rust and Bayyinah-Go on the external corpus, with all findings either fixed or addressed by corrigendum).
3. Strength-n on release-gate corpus (testable: bit-identical agreement across the three ports).
4. Falsification bounty operational (testable: bounty program is published, at least one valid bounty submission has been triaged within a 14-day window).
5. TQL-1 qualification close (testable: at least one customer-program PSAC has been accepted by the FAA OR an explicit corrigendum names why it has not).

**Step 7 -- Sirat Alladhina.**
- Worked: the parity discipline. The cross-layer checker pattern. The strength-n primitive.
- Failed: every release that shipped "completeness" without a closure gate. v2.0 has a closure gate.
- Cow Episode warning: do not let "but we have so many features now" replace "the gate closed." v2.0 is the gate, not the feature inventory.

**Tier grade:** Tier 1 candidate (the framework's central claim is empirically tested at v2.0 across the four gate conditions). Promotion from Tier 2 to Tier 1 IS the v2.0 ship event.

**Falsification block F-MASTER (proposer-drafted seed; §5.4 re-authoring required by the FULL operational pool per §3B.3 + §3B.6).**
```
Import: trust-and-falsification gate at v2.0 (the framework's central
  recursive-verification claim).

Tier-1 claim: at v2.0 ship time, all four gate conditions hold
  simultaneously: (a) external-contributor corpus passes by foreign-
  instance scan; (b) strength-n bit-identical agreement on the v2.0
  release-gate corpus; (c) operational bounty program with N>=1
  triaged submissions; (d) TQL-1 qualification close on at least
  one customer-program PSAC OR an explicit corrigendum naming the
  reason it has not.

Falsifying observable: at ship-readiness gate, any one of the four
  gate conditions does not hold: (a) the external-contributor corpus
  either does not exist OR has not been scanned-clean by the foreign-
  instance pair; (b) the strength-n stack produces non-bit-identical
  agreement on the release-gate corpus and the disagreement is not
  registered as a port-scope corrigendum; (c) the bounty program is
  not operational OR no valid submission has been triaged within
  the 14-day window; (d) no TQL-1 PSAC has been accepted AND no
  corrigendum explains the gap.

Statistic / threshold: per-condition binary pass/fail; release-level
  conjunction (AND across all four). Pre-registered threshold: all
  four must PASS for v2.0 GA. Two-PASS-with-2-explicit-corrigenda
  ships as v2.0-rc, not as v2.0 GA. One-or-fewer PASS does not
  ship at all. Power analysis grounding: this is an invariance-
  class test; the gate is conjunctive and absolute, not a sample-
  size threshold.

Data source: F-MASTER substrate: the v2.0 release-gate corpus
  (external-contributor-authored); the strength-n agreement-checker
  output; the bounty-program operational log; the FAA PSAC
  acceptance record (or its absence, with corrigendum). Comparator
  chains: the v1.6.0 strength-n primitive output; the bounty
  program's triage ledger; the FAA's correspondence record on the
  customer-program PSAC.

Decision rule: v2.0 GA ships if and only if all four gate conditions
  PASS. v2.0-rc ships if (a) + (b) PASS and (c) + (d) have explicit
  corrigenda. No ship if (a) or (b) does not PASS. The release
  candidate is held until the gate closes; the framework's central
  claim is empirically tested at the v2.0 ship event.

Discriminating-test verification: every gate condition is verifiable
  by an instance outside the producing instance. (a) external-
  contributor corpus is by construction authored by a non-core team
  member; (b) strength-n agreement is mechanical bit-equality across
  three independent ports; (c) bounty program operational status is
  observable from the published bounty page + triage ledger; (d)
  TQL-1 acceptance is documented by the FAA. None of the four
  conditions depend on Bayyinah-internal categorization. F-MASTER
  IS the discriminating test for the framework's central claim;
  failure of any single condition falsifies the central claim and
  the release does not ship.
```

**Closing dua:** Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

---

## 10. Cross-phase disciplines (apply to every Fatiha session above)

Every release session above operates under these standing disciplines:

**Discipline 1 -- Pre-registered finding-code namespace.** Each release allocates a finding-code block before Step 6 begins. Codes are never reused. If a release does not use its full allocated block, the unused codes are registered as future-work codes (not recycled). [Cross-references PMD §5.1 pre-registration discipline.]

**Discipline 2 -- Corrigendum format inherited from v1.2.4.** Every limitation, deferral, or partial-coverage statement uses the v1.2.4 corrigendum format. No release invents a new disclosure format. [PMD §3A.10 M1.5 append-only.]

**Discipline 3 -- Substrate/surface separation.** Every extractor reports both surface-level (what the document/file/binary claims) and substrate-level (what the substrate actually contains). The parity-discipline test harness checks the relation between them.

**Discipline 4 -- 1.5x time buffer on every estimate.** The Roadmap Risk 1 (over-optimistic timeline) is addressed by treating every headline person-week estimate as 75% understated. The adjusted estimates are the operative ones for planning. [PMD §5.1 chemistry §2.2 cycle-time-estimation discipline.]

**Discipline 5 -- 20% skip rule.** Every release pre-authorizes which sub-surfaces are skippable into the next patch release. Skipping is honest and registered, not silent. [Fatiha Construct Step 4.]

**Discipline 6 -- Falsification gate per release.** No release ships without its named falsification criterion having been run on its named fixture corpus. A release that fails its criterion does not ship; it returns to Step 6 OR re-scopes via the 20% skip rule. [PMD §0.3 ship-blocker rule.]

**Discipline 7 -- The Cow Episode warning at Step 7.** Every release names its specific over-specification trap. The discipline of naming the trap is half the protection against falling into it. [Fatiha Construct §5.6.]

**Discipline 8 -- PMD §3A.3 pre-dispatch substrate-actual-verification (added in v1.1).** Each release's Step 6 task list opens with a substrate-actual verification probe against the prior canonical tag. The probe confirms that the dispatch-prompt's substrate assumption matches substrate-actual at the canonical tag. Divergence is surfaced as F-CW-class finding before T01 implementation begins.

**Discipline 9 -- PMD §3B.2 post-edit substrate-verification (added in v1.1).** After each release ship-record edit, ledger-entry write, or in-flight patch application, a post-edit substrate-verification probe checks factual claims, cross-references, and inherited-discipline claims in the edit content against substrate-actual. F-POST-EDIT-class findings are absorbed in-cycle.

**Discipline 10 -- PMD §3B.3 multi-vendor cross-rotation (added in v1.1).** All HEAVY-tier releases (v1.5.0, v1.8.0/v1.9.0, v1.6.0, v2.0.0) ship under four-vendor fresh-instance audit per the §3B.6 operational pool (Anthropic Claude Opus 4.7 Mode A + OpenAI GPT-5.5 thinking + Perplexity GPT-5.4 thinking + Google Gemini 3.1 Pro). STANDARD-tier releases ship under at least one rotation audit. LIGHT-tier releases ship under at least the producer-discount discipline per §3A.12.4.

**Discipline 11 -- PMD §3A.12.4 producer-discount on judgment-laden calls (added in v1.1).** Producer self-assessment of substrate-fidelity for judgment-laden claims (strategy adequacy, sequencing wisdom, falsification-test discriminating power) is discounted against §5.4 audit-author verdicts. Mechanical checks (version-number arithmetic, RFC-citation match) bind regardless of vendor.

**Discipline 12 -- PMD §3A.10 M1.5 corrigendum (added in v1.1).** Any revision to this strategy document or to a release's spec uses append-only corrigendum format; prior framing is preserved as historical record. The v1.0 -> v1.1 transition itself follows this discipline (the v1.0 artifact is preserved at `bayyinah_v2_coding_strategy_fatiha.md` while v1.1 ships as a new file).

---

## 11. PMD §3B.2 post-edit substrate-verification ledger for this v1.1

Per PMD §3B.2 / §3B.5 named-exception clause, this document's own factual claims are subject to post-edit substrate-verification. The verification operates against PMD v1.8-5 substrate-actual and against the v1.0 strategy artifact substrate-actual.

**F-POST-EDIT-STRAT-v1.1-001 (resolved at draft time).**
- *Site:* §0.1 calibration cell assignment for v1.2.5.
- *Risk:* mis-mapping of v1.2.5 to a §3A.1 cell could trigger an incorrect tier default.
- *Verification:* v1.2.5 substrate-actual is "extend the v1.2.4 parity discipline with two new format classes (CSV, JSON), inheriting the v1.2.4 architectural pattern unchanged." This maps to {moderate-risk, additive-on-corpus-architecture} -> LIGHT per the Tasdiq al-Bayan v0.14.0 empirical witness cell in PMD §3A.1. Mapping confirmed.

**F-POST-EDIT-STRAT-v1.1-002 (resolved at draft time).**
- *Site:* §0.1 calibration cell assignment for v2.0.0.
- *Risk:* v2.0.0 might map to several PMD §3A.1 cells; pre-flight verification confirms which.
- *Verification:* v2.0.0 substrate-actual is "ship no new extractor family; close the trust-and-falsification gate; qualify TQL-1 on at least one customer-program PSAC." The TQL-1 qualification close is a new attestation surface (per PMD §3A.1 HEAVY-regardless-surface enumeration). Mapping confirmed: {HIGH-risk, substrate-modifying-broad-architecture} -> HEAVY.

**F-POST-EDIT-STRAT-v1.1-003 (resolved at draft time).**
- *Site:* §3 phase progression table -- tier-grade column.
- *Risk:* tier-grade column might attribute Tier 1 status to specific implementations that PMD §0.2 specifies must be Tier 2 pending named test.
- *Verification:* every release's tier-grade column reads "T2 pending F[N]." This is PMD §0.2 compliant (Tier 1 framework, Tier 2 specific implementation pending named test).

**F-POST-EDIT-STRAT-v1.1-004 (resolved at draft time).**
- *Site:* §0 corrigendum -- "PMD §3A.10 M1.5" reference.
- *Risk:* §3A.10 reference could be off-by-one or wrong-section.
- *Verification:* PMD v1.8-5 line 880 reads "**§3A.10 M1.5 -- Methodology-document recursive A1 self-application discipline**." Reference confirmed.

**F-POST-EDIT-STRAT-v1.1-005 (resolved at draft time).**
- *Site:* §0 corrigendum -- "Laban-Schnabel-Neville 2026 DELEGATE-52" reference and "25% baseline" figure.
- *Risk:* per PMD v1.3 F-POST-EDIT-PMDv1.3-001, the paper is a preprint, not peer-reviewed; the "25%" figure is the publication-headline figure.
- *Verification:* PMD v1.8-5 line 948 reads "frontier LLMs (Gemini 3.1 Pro, Claude 4.6 Opus, GPT 5.4 explicitly named in the publication) corrupt an average of 25% of document content during long delegated workflows on the DELEGATE-52 benchmark." The phrasing in this v1.1 reads "Laban-Schnabel-Neville 2026 DELEGATE-52 measures a ~25% baseline corruption rate." This is consistent with PMD substrate. The publication is an arXiv preprint, not peer-reviewed; the v1.1 phrasing uses "measures" (not "establishes"); this is consistent with PMD §0.4 cycle 12 F-POST-EDIT-PMDv1.3-001 disposition.

**Cross-instance verification path remains open** per PMD §3B.5 named-exception clause. The four-vendor fresh-instance audit (per the companion audit prompt `bayyinah_v2_coding_strategy_audit_prompt_v1_1.md`) will surface any additional F-POST-EDIT findings in this v1.1.

---

## 12. What this document is and is not

**Is:** the engineering scaffold for the v1.2.4 -> v2.0 progression, expressed in the Fatiha Construct vocabulary, anchored to the Commercialization Roadmap's industry sequencing, audited per PMD v1.8 discipline (tier-grading, calibration-class assignment, PMD §0.3 falsification blocks, proposer-falsifier separation per §0.3, post-edit substrate-verification per §3B.2).

**Is not:**
- A customer commitment. Release dates are planning targets, not commitments.
- A legal claim. Patent novelty per the provisional filing is separate.
- A binding contract on engineering staff. Pivots in response to pilot signal are allowed and expected.
- A claim that the four-vendor audit will validate every falsification block as authored here. The proposer-drafted F-blocks are seeds; the §5.4 audit-author re-authoring is the operational test.

**Successor work (per PMD §7 pattern):**
- Empirical validation of the §3A.1 STANDARD-tier cell across the v1.3.0 / v1.4.0 / v1.10.0 / v1.4.1 / v1.7.0 / v1.5.1 / v1.6.1 / v1.7.1 / v1.11.0 / v1.12.0 / v1.13.0 / v1.14.0 releases (N >= 5 STANDARD-tier ship records needed for cross-publication confidence).
- The §3B.1 25% baseline test: at v2.0, the external-contributor corpus audit IS a candidate test of whether PMD-discipline measurably reduces delegation-corruption below the Laban-Schnabel-Neville baseline on the Bayyinah substrate.
- The v2.0-rc -> v2.0 GA transition itself is the F-MASTER ship event and constitutes an empirical witness for PMD §0.3 ship-blocker discipline at the framework-recursive layer.

---

**Document status: v1.1, PMD v1.8-compliant. Pending §5.4 four-vendor audit per companion `bayyinah_v2_coding_strategy_audit_prompt_v1_1.md`.**

**Closing dua:** Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

---

# Bismillah ir-Rahman ir-Rahim
