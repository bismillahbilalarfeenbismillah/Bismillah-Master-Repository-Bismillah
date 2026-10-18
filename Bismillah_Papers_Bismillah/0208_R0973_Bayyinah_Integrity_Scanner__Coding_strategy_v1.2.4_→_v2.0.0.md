# Bismillah ir-Rahman ir-Rahim

# R0973 -- Bayyinah Integrity Scanner: Coding strategy v1.2.4 → v2.0.0 (Fatiha hybrid)

**Chronological Index:** 208 of 995  
**Date:** 2026-05-04  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** STRATEGY_TO_V2.md  
**Source Format:** md  
**SHA-256:** `6a2ea2f224ef91d61671bc6fe695c9849a77a822ac413f5669a466ab0439e201`  

---

## R0973 · Bayyinah Integrity Scanner: Coding strategy v1.2.4 → v2.0.0 (Fatiha hybrid)

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: STRATEGY_TO_V2.md
- source_format: md
- text_sha256: 6a2ea2f224ef91d61671bc6fe695c9849a77a822ac413f5669a466ab0439e201

# Bayyinah Integrity Scanner: Coding strategy v1.2.4 → v2.0.0 (Fatiha hybrid)

**Author:** Bilal Syed Arfeen (project lead).
**Substrate:** the live `Bayyinah-Integrity-Scanner` repo at v1.2.4 (SHA `72a2c787`), Apache-2.0, scope = file integrity scanner across 23 file kinds.
**Authority anchors:** Bayyinah Audit Framework v3.0 (Arfeen 2026, CC BY-NC 4.0) as the artifact-level discipline contract; Munafiq Protocol §9 (DOI: 10.5281/zenodo.19677111) as the theoretical grounding; the Fatiha Construct as the session-level prompt engineering scaffold.
**Effective:** 2026-06-09.
**Supersedes:** any prior strategy substrate that did not match the live repo's actual contracts.

This strategy operates at two layers without collision:

- **Artifact layer.** Bayyinah Audit Framework v3.0 specifies what MUST EXIST at release time (CHANGELOG entry, RETIREMENT_LEDGER update, pinning test, fixture corpus update, MECHANISM_REGISTRY delta, public surface pin, parity-break procedure when applicable).
- **Session layer.** The Fatiha 7-step construct specifies how the cognitive work is structured during each release session (Bismillah, Alhamdulillah, Ar-Rahman ar-Rahim, Maliki Yawm ad-Din, Iyyaka na'budu, Ihdina as-Sirat al-Mustaqim, Sirat alladhina).

Every release in this sequence satisfies both. The audit framework is artifact discipline; the Fatiha is cognitive discipline; neither subsumes the other. The recursive application of Bayyinah's own thesis (Munafiq Protocol §9 input-layer performed-alignment detection) lands at the development layer because the session-level scaffold is the discipline the artifacts inherit.

---

## 1. Discipline contract (the rules every release ratifies)

Carried by every release without restatement:

1. **PARITY.md.** `bayyinah.scan_pdf(path).to_dict() == bayyinah_v0.scan_pdf(path).to_dict()` on every Phase 0 fixture. Breaks follow the named procedure (issue tagged `parity-break`, fixture corpus update, parity test update, CHANGELOG `Parity-break` heading, minor version bump).
2. **FRAMEWORK.md §2 five-place pattern.** Every new detection mechanism appears in CHANGELOG + README + fixture + pinning test + `bayyinah/mechanisms/registry.py`.
3. **NAMING.md.** Modules use classical Islamic scholarly methodology terms; surahs name phases, not modules; forbidden term list (Taqiyya, Shirk, Kufr, Fitnah, Haram, Halal, surah names on modules) honored.
4. **Additive-only invariant.** Public surface per version pinned in `tests/test_public_surface_additive.py` with `V_X_Y_Z_SURFACE` constants.
5. **Dependency manifest discipline.** New third-party imports go in BOTH `requirements.txt` AND `pyproject.toml` in the same patch, capped at the current major.
6. **Em-dash discipline.** Em-dashes excluded from CHANGELOG entries, README content, finding descriptions, demo landing page, and similar user-facing prose. Code comments exempt.
7. **Audit-of-self.** Every round in the Bayyinah chain is audit-of-self by Bilal. Fraz Ashraf acknowledged for the framework's engineering approach (NAMING.md §27), not as auditor on this chain.
8. **Validator-by-different-instance.** Producer instance does not audit; a fresh Claude instance audits against public artifacts alone.
9. **MECHANISM_REGISTRY load-time coherence.** `len(MECHANISM_REGISTRY)` is asserted at import time and pinned in tests; tier and severity tables must not drift from `ZAHIR_MECHANISMS ∪ BATIN_MECHANISMS`.

---

## 2. Scope of the v1.2.4 → v2.0.0 sequence

**In scope.** Round 11 closure (deferred from v1.2.4); Round 13 (parity-break tier change deferred from v1.2.4); QUESTIONS.md Q1, Q3, Q4, Q5, Q8, Q9, Q10 closures; selective absorption of prototype concepts Q-PRO-3 (honest budget controller) and Q-PRO-4 (supply-chain scope decision resolved as QUESTIONS.md answer); recursive-self-verification structural check at v2.0 as discipline artifact.

**Out of scope.** New substrate kinds beyond the existing 23 file kinds (Q-PRO-4 must resolve before any expansion is considered); contracted multi-language ports; a second governance framework at the artifact layer; TQL-1 / FAA qualification; Q2 (data-driven, accumulates across releases); Q6 (resolved v1.2.1); Q7 (committed for v1.2 per QUESTIONS.md; verify shipped during v1.2.5 release-gate).

---

## 3. Release sessions

Nine releases v1.2.5 → v2.0.0. Each is a Fatiha 7-step session producing the audit-framework-required artifacts.

---

### 3.1 Release v1.2.5, Round 11 closure (multi-layer integrity traps)

**Step 1, Bismillah ar-Rahman ar-Rahim.** Authority: Bayyinah Audit Framework v3.0 §17.3 retirement-ledger discipline; Munafiq Protocol §9 input-layer performed-alignment detection; the 2026-05-04 red-team probe of bayyinah.dev v1.2.3 documented in `docs/adversarial/`. Purpose hierarchy: serve bayyinah.dev users who saw 4 CRITICAL silent-pass findings, then enterprise adopters who depend on multi-layer integrity coverage, then the audit framework's structural-honesty claim that named Round 11 in `RETIREMENT_LEDGER.md`. Beneficiary: end users whose default-pipeline scans missed multi-layer concealment shapes. Technical objective: close all 4 CRITICAL silent-pass findings and all 5 HIGH partial-catches surfaced by Round 11, each closure backed by a per-mechanism analyzer plus a `TahqiqValidator` cross-mechanism layer when the trap requires composition. In-scope: per-mechanism analyzer additions under existing naming pattern (`<kind>_<mechanism>.py`); `TahqiqValidator` cross-mechanism composition layer in `analyzers/`; fixture corpus additions in `tests/fixtures/<kind>/`; pinning tests in `tests/analyzers/test_<mechanism>.py`; MECHANISM_REGISTRY updates. Out-of-scope: new file kinds; new finding-type fields beyond the existing `mechanism / tier / source_layer / evidence` surface; any change to `compute_muwazana_score` or `tamyiz_verdict`.

**Step 2, Alhamdulillah Rabbil-alameen.** Inherited: v1.2.4 substrate; 1,800+ test baseline; MECHANISM_REGISTRY at the v1.2.4 count (assertable in one line); PARITY invariant against `bayyinah_v0.py` and `bayyinah_v0_1.py` across every Phase 0 fixture; the per-mechanism analyzer pattern from Round 12 closure (csv_zero_width_payload, docx_white_text, etc.); producer-family corpus coverage from v1.2.4. Stable: `BaseAnalyzer` contract with `__init_subclass__` validation; `FileKind` enum and `FileRouter` polyglot detection; `IntegrityReport` shape; `_scan_error_report` helper; five named verdicts (`sahih`, `mushtabih`, `mukhfi`, `munafiq`, `mughlaq`); cost-class-aware production-mode dispatch from v1.1.6; analyzer registry composition rules. Missing: per-mechanism analyzers for each of the 4 CRITICAL + 5 HIGH Round 11 findings; the `TahqiqValidator` cross-mechanism layer for multi-layer composition; fixtures demonstrating each multi-layer trap shape. Available: the red-team probe report itself (the artifact that surfaced the findings); the per-mechanism analyzer pattern as worked example; `NAMING.md` naming the `TahqiqValidator` term explicitly.

**Step 3, Ar-Rahman ar-Rahim (mercy with immediacy and continuity).** MDL: each silent-pass closure is one new per-mechanism analyzer file following the existing `<kind>_<mechanism>.py` convention; the multi-layer cross-mechanism trap closure is the `TahqiqValidator` layer composing findings across analyzers per the call graph. FRaZ (FRaZ-earned complexity): the `TahqiqValidator` layer is load-bearing because Round 11's silent-pass shape is precisely "no single analyzer fired; the composition fires." Adding a generic validator layer is the minimum sufficient mechanism; doing less leaves the silent-pass open. Adding more (a full DAG engine, learnable composition rules) is scope-creep that belongs in a future round. Patent invariant clause: this release adds per-mechanism analyzers and the `TahqiqValidator` composition layer; it does NOT alter `Finding`, `IntegrityReport`, `BaseAnalyzer`, `compute_muwazana_score`, `tamyiz_verdict`, or any verdict semantics. Cow Episode anchor: do not absorb Round 12's residue into Round 11 closure; the rounds remain separate in the retirement ledger even though Round 12 retired first.

**Step 4, Maliki Yawm ad-Din (sovereignty over the day of accounting).** Time budget: 4 -- 6 person-weeks for 9 finding closures plus the `TahqiqValidator` layer (1 -- 2 weeks). Release-gate accountability: v1.2.5 is scanned by v1.2.4 before tag; v0/v0.1 byte-parity holds across all Phase 0 fixtures; MECHANISM_REGISTRY coherence asserts at import; em-dash sweep clean across CHANGELOG, README, finding descriptions, demo landing page. Slip discipline: if any of the 9 finding closures or the validator layer is incomplete at target, the slip is filed under CHANGELOG `### Deferred` heading naming what slipped and which target tag absorbs it (typically v1.2.6). The audit framework's day-of-accounting clause: nothing ships as "Round 11 closed" unless the retirement ledger names the structural defense and the pinning test exists.

**Step 5, Iyyaka Na'budu wa iyyaka nasta'in (exclusive turning to, sole anchor).** Drift indicator: a Round 11 closure that ships without a pinning test. Detection: CI gate that diffs `RETIREMENT_LEDGER.md` against `tests/analyzers/` and fails if any newly-named structural defense lacks a corresponding `test_*.py` assertion. Mid-release checkpoint: after the first 3 finding closures land, validator layer prototype reviewed against the remaining 6 findings to confirm the composition primitive is sufficient. Sole anchor: every closure routes through the per-mechanism analyzer pattern; no closure shortcuts via inline conditionals in existing analyzers.

**Step 6, Ihdina as-Sirat al-Mustaqim (guidance to the straight path, the concrete deliverables).**
(1) Per-mechanism analyzer file for each of 4 CRITICAL silent-passes (4 new `<kind>_<mechanism>.py` files in `analyzers/`).
(2) Per-mechanism analyzer file for each of 5 HIGH partial-catches (5 new files).
(3) `analyzers/tahqiq_validator.py` cross-mechanism composition layer with explicit composition rules per trap shape.
(4) Fixture corpus update in `tests/fixtures/<kind>/` (one fixture per Round 11 finding; 9 fixtures total).
(5) Pinning tests in `tests/analyzers/test_<mechanism>.py` (one test file per closure; 9 + 1 validator test = 10 new test files).
(6) `bayyinah/mechanisms/registry.py` updates with tier + cost class for each new mechanism.
(7) `domain/config.py` updates to `ZAHIR_MECHANISMS` / `BATIN_MECHANISMS` / `SEVERITY` / `TIER` tables per the new mechanism set.
(8) `CHANGELOG.md` entry under `## [1.2.5]` with `### Added`, `### Round 11 closure`, and `### Mechanism count` headings.
(9) `RETIREMENT_LEDGER.md` entry naming each finding closed and the structural defense that prevents recurrence.
(10) `README.md` mechanism count update; supported-formats table verified current.
(11) `HANDOFF.md` rewrite for v1.2.5 (minor release; not a patch).
(12) Public surface pin: `V1_2_5_SURFACE = frozenset(...)` added to `tests/test_public_surface_additive.py` with subset assertion against `V1_2_4_SURFACE`.
(13) Q7 verification: HyperLogLog demo counter committed for v1.2 per `QUESTIONS.md` is confirmed shipped; if not shipped, absorbed into v1.2.5 as a sub-item under `### Q7 closure`.

**Step 7, Sirat alladhina an'amta alayhim (the path of those favored, not the strayed).** Worked: the per-mechanism analyzer pattern from Round 12 closure (csv_zero_width_payload, docx_white_text, openaction destination filter); producer-family corpus coverage that surfaced producer-class blind spots; the five-place documentation pattern. Failed (Round 11 deferral): depth-of-detection backlog accumulated because Round 12 was prioritized first; multi-layer integrity traps escaped per-mechanism coverage because no composition primitive existed. Cow Episode for v1.2.5: do not accept any Round 11 closure that lacks BOTH a fixture AND a pinning test. Either the closure is structural or it is vapor; the retirement ledger entries that name structural defenses without corresponding tests are themselves a finding category in their own right. Release gate: v1.2.5 scanned by v1.2.4 before tag; v0/v0.1 PARITY holds; MECHANISM_REGISTRY coherence asserts; em-dash sweep clean; CI green on all 18 audit-framework discipline checks.

**Closing dua, v1.2.5:** Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

---

### 3.2 Release v1.3.0, Round 13 (parity-break tier reclassification)

**Step 1, Bismillah.** Authority: `PARITY.md` parity-break procedure (the conditional invariant clause); `RETIREMENT_LEDGER.md` Round 12 deferral note explicitly naming the tounicode_anomaly tier 1 → 2 reclassification as the v1.3.0 target. Purpose hierarchy: serve downstream consumers who pin to v1.2.x tier semantics (one release of warning ahead of the change); then enterprise adopters whose triage workflows partition by tier; then the project's own structural-honesty claim that PARITY breaks are reviewed, named, and minor-bumped. Beneficiary: triage operators who need tier semantics that match the calibration evidence accumulated through Round 12. Technical objective: ship the tounicode_anomaly tier 1 → tier 2 reclassification per PARITY procedure, plus any other tier reclassifications surfaced during Round 11 work in v1.2.5. In-scope: tier table updates in `domain/config.py`; fixture corpus updates to assert new tier outputs; parity test updates; CHANGELOG `### Parity-break` heading; PARITY.md cross-reference; issue tagged `parity-break` filed and closed. Out-of-scope: any mechanism additions (those land in Round 14+); any score function shape changes (those land in v1.4.0).

**Step 2, Alhamdulillah.** Inherited: v1.2.5 substrate including Round 11 closures and the `TahqiqValidator` layer; PARITY procedure articulated in v1.2.4. Stable: tier-classification primitives in `domain/config.py`; tier-aware production-mode dispatch (Tier 1 high-confidence findings short-circuit the loop). Missing: the issue-tagged parity-break entry; the fixture corpus updates reflecting the new tier output; the parity test update. Available: Round 12 deferral note in `RETIREMENT_LEDGER.md` documenting exactly which reclassification is targeted; calibration evidence accumulated through Round 11 work.

**Step 3, Ar-Rahman ar-Rahim.** MDL: the tier change is one constant in `domain/config.py` plus fixtures that assert the new output plus a parity test that admits the new shape. FRaZ: a tier reclassification IS a parity break by definition (the parity tuple includes tier); the parity break is FRaZ-earned because the calibration evidence supports the reclassification. Doing less (silently reclassifying without parity procedure) is the exact discipline failure PARITY.md exists to prevent. Patent invariant clause: this release changes the tier output for one (or a small set of) mechanism; it does NOT alter mechanism detection, `Finding` shape, `compute_muwazana_score`, or `tamyiz_verdict`. Cow Episode anchor: do not bundle unrelated tier reclassifications into v1.3.0 because the parity break "costs nothing extra"; each reclassification is its own discipline event with its own calibration evidence.

**Step 4, Maliki Yawm ad-Din.** Time budget: 1 -- 2 person-weeks. Release-gate accountability: v1.3.0 scanned by v1.2.5 before tag; PARITY procedure complete (issue tagged, CHANGELOG heading present, corpus updated, parity test admits new output, minor bumped); the parity-break appendix in PARITY.md updated with this as data point #1 for Q2 (the contingent-vs-load-bearing question). Slip discipline: if calibration evidence is contested, the reclassification is deferred to v1.4.0 and Q2 informed with the contested evidence record.

**Step 5, Iyyaka Na'budu.** Drift indicator: a tier reclassification that ships without the issue tag, without the CHANGELOG `### Parity-break` heading, or without updating the parity test. Detection: CI gate that asserts the presence of `### Parity-break` in CHANGELOG when any fixture in `tests/fixtures/` changes its declared tier expectation. Mid-release checkpoint: parity-break issue filed publicly with the calibration evidence link; review comment period before the reclassification merges.

**Step 6, Ihdina as-Sirat al-Mustaqim.**
(1) Issue tagged `parity-break` filed in the public issue tracker naming the demonstration of v0's defect (tier 1 was overcalibrated; calibration evidence shows tier 2 is correct).
(2) `domain/config.py` tier table update for tounicode_anomaly (and any other Round 11-surfaced reclassifications).
(3) `tests/fixtures/` corpus update with both the old (defective) v0 output retained as regression artifact and the new (corrected) expected output.
(4) `tests/test_fixtures.py::test_v0_v01_parity` updated to assert the new expected output.
(5) `CHANGELOG.md` entry under `## [1.3.0]` with `### Parity-break` heading cross-referencing the issue.
(6) `RETIREMENT_LEDGER.md` Round 13 entry naming the reclassification + structural defense (the updated parity test).
(7) `PARITY.md` "Parity-break evidence so far" appendix initiated with this as data point #1 for Q2.
(8) `HANDOFF.md` v1.3.0 rewrite.
(9) Public surface pin: `V1_3_0_SURFACE = frozenset(...)` aliasing `V1_2_5_SURFACE` (no surface change; tier output is not a public surface symbol).
(10) `README.md` "Latest release" badge updated; supported-formats table verified.

**Step 7, Sirat alladhina.** Worked: PARITY procedure articulated in v1.2.4 made the v1.3.0 work definable in concrete steps. Failed: prior to PARITY.md's conditional clause, tier reclassifications were either silently dropped (parity locked-in defects forever) or silently shipped (parity claim load-bearing without conditions). PARITY.md closed the binary. Cow Episode for v1.3.0: do not declare the parity-break "minor" because it is one tier change; the discipline cost is the same as any larger break, and Q2's data accumulation depends on every parity-break being documented at the same fidelity. Release gate: parity test passes against new corpus; PARITY appendix updated; CHANGELOG carries the break heading; minor version bumped; v1.3.0 scanned by v1.2.5.

**Closing dua, v1.3.0:** Rabbana taqabbal minna.

---

### 3.3 Release v1.4.0, Round 14 (Q3 + Q4 score function and scan_incomplete semantics)

**Step 1, Bismillah.** Authority: `QUESTIONS.md` Q3 (score collapses heterogeneous risk) and Q4 (0.5 clamp lives inside continuous distribution); Munafiq Protocol §9 input-layer scoring discipline; the v1.2 report shape additions (`scan_complete: bool`, `coverage` field) that staged the v1.4.0 work. Purpose hierarchy: serve enterprise CI integrations whose dashboards consume `integrity_score` for gating; then triage operators who need finding-count and coverage as separate axes; then downstream consumers pinned to the current score shape who need a migration path. Beneficiary: anyone whose CI dashboard cannot distinguish "half-dirty file" from "unscanned" today. Technical objective: ship the score function shape decision (continuous-and-saturating retained vs split into continuous + finding-count + coverage axes) with migration path; ship the scan_incomplete score semantics decision (0.5 clamp retained vs null score on incomplete) with deprecation path. Both decisions documented in CHANGELOG, PARITY.md, and a new `docs/scope/v1_4_0_score_function_decision.md`. In-scope: `domain/scoring.py` update for whichever shape is chosen; `domain/integrity_report.py` field additions/changes; migration shim under a feature flag for one release; deprecation warnings emitted from the prior shape. Out-of-scope: any new mechanism; any analyzer changes; any verdict (`tamyiz_verdict`) modifications.

**Step 2, Alhamdulillah.** Inherited: v1.3.0 substrate including the Round 13 parity break documented; v1.2's `scan_complete` and `coverage` fields already shipped. Stable: five named verdicts; `compute_muwazana_score` interface signature (parameters unchanged; return value may change shape under the new design); `apply_scan_incomplete_clamp` helper. Missing: the decision-of-record document; the new score shape implementation; the migration shim; the deprecation warning. Available: Q3 and Q4 problem statements in `QUESTIONS.md` enumerate the considerations; community input invited during the v1.3.0 ship cycle.

**Step 3, Ar-Rahman ar-Rahim.** MDL: the score-shape decision is one function signature change in `domain/scoring.py` plus the feature-flag shim plus the deprecation path. FRaZ: a public-surface change to `integrity_score` is FRaZ-earned because Q3 + Q4 have been open since v1.2 and the ambiguity is documented as a known commercial-adoption friction. Doing less (leaving the score ambiguous) defers the friction; doing more (splitting into three independent fields with their own subfields) is scope-creep that belongs in Round 16+. Patent invariant clause: this release MAY change the public `integrity_score` field shape; the verdict mechanic (`sahih` / `mushtabih` / `mukhfi` / `munafiq` / `mughlaq`) is UNCHANGED. The five verdicts are the load-bearing public surface; the score is the secondary numeric axis. Cow Episode anchor: do not split the score into more than the minimum axes the Q3 + Q4 questions named; resist "while we're at it" axis additions.

**Step 4, Maliki Yawm ad-Din.** Time budget: 6 -- 8 person-weeks (includes community input collection during v1.3.0 ship cycle + implementation + migration documentation). Release-gate accountability: v1.4.0 scanned by v1.3.0 before tag; PARITY procedure followed if the shape change is a parity break (high probability); decision-of-record documented before code merges; one release of advance warning issued at v1.3.0 ship time. Slip discipline: if community input is contested or shape decision is reopened, v1.4.0 ships the migration shim with feature flag default-off, and the active default-flip waits for v1.5.0.

**Step 5, Iyyaka Na'budu.** Drift indicator: a score-shape change shipped without `docs/scope/v1_4_0_score_function_decision.md` recording the deliberation. Detection: CHANGELOG entry under v1.4.0 must cross-link to the decision-of-record document; CI gate asserts the document exists. Mid-release checkpoint: the decision-of-record draft is reviewed by at least one validator-by-different-instance before code merges.

**Step 6, Ihdina as-Sirat al-Mustaqim.**
(1) `docs/scope/v1_4_0_score_function_decision.md` recording Q3 + Q4 deliberation, decision, alternatives considered, and migration path.
(2) `domain/scoring.py` updated implementation; `compute_muwazana_score` interface change if the shape splits.
(3) `domain/integrity_report.py` field additions or changes per the decision (e.g., `integrity_score: float`, `finding_count: int`, `coverage_score: float` if split; or `integrity_score: float | None` if Q4 chooses null on incomplete).
(4) Feature-flag shim under `domain/config.py` allowing v1.3.x-shape output to be requested by feature-flag pin during the deprecation window.
(5) Deprecation warning emitted from the v1.3.x shape requesting feature-flag for the migration window (typically two releases).
(6) Parity procedure if the shape is a parity break: issue tagged, CHANGELOG `### Parity-break` heading, corpus update, parity test update.
(7) `RETIREMENT_LEDGER.md` Round 14 entry naming Q3 + Q4 closure + structural defense (pinning tests for the new shape).
(8) `PARITY.md` appendix updated with this as data point #2 for Q2 (if parity break).
(9) `README.md` updated to reflect the new score-shape semantics.
(10) `HANDOFF.md` v1.4.0 rewrite.
(11) Public surface pin `V1_4_0_SURFACE`.
(12) `docs/principles.md` is NOT yet created (that is v1.9.0 scope); but a note in `docs/scope/v1_4_0_score_function_decision.md` previews how the score-function principle will be summarized framework-free in v1.9.0.

**Step 7, Sirat alladhina.** Worked: Q3 and Q4 were named explicitly in QUESTIONS.md before they were ratified by code; the v1.2 staging (`scan_complete`, `coverage` fields added) created the substrate that v1.4.0 closes. Failed: the original v0/v0.1 score function was sized for "is this file clean or dirty" with no commercial-CI integration in mind; the ambiguity surfaced only when Q3 and Q4 were filed. Cow Episode for v1.4.0: do not redesign the score function from scratch; the change must be the minimum that closes Q3 + Q4 and no more. Release gate: decision-of-record document published; deprecation warning observable; migration shim exercised in tests; PARITY procedure complete if applicable; v1.4.0 scanned by v1.3.0.

**Closing dua, v1.4.0:** Rabbana taqabbal minna.

---

### 3.4 Release v1.5.0, Round 15 (Q1 closure: KNOWN_LIMITS.md published)

**Step 1, Bismillah.** Authority: `QUESTIONS.md` Q1 (publish the adversarial document the score function cannot detect); Munafiq Protocol §9 input-layer disclosure principle (a tool that detects performed alignment in others must surface its own gaps); the framework's structural-honesty discipline at maturity Level 4. Purpose hierarchy: serve adversarial reviewers who need a worked counterexample to verify Bayyinah's honesty claim; then security researchers who construct their own attacks against the documented gap; then enterprise buyers who require KNOWN_LIMITS disclosure as a procurement gate. Beneficiary: anyone evaluating Bayyinah's "no silent clean-pass" claim against evidence. Technical objective: construct, document, and publish `KNOWN_LIMITS.md` containing at least one worked adversarial document that scores 1.0 on the default pipeline despite carrying concealed payload, with construction method disclosed in full. Pinning test asserts the document scores 1.0 so future releases do not silently defend the published gap into a closed case without updating KNOWN_LIMITS.md. In-scope: construction of the adversarial document; documentation of construction method; `KNOWN_LIMITS.md` authored at repo root; pinning test in `tests/test_known_limits.py`; optional: register the gap-mechanism as a known-absent-mechanism in `MECHANISM_REGISTRY` with cost class TBD. Out-of-scope: closing the gap (closing it makes it a defended case; the gap stays published, the new gap is added in a future round).

**Step 2, Alhamdulillah.** Inherited: v1.4.0 substrate including the stable score function shape. Stable: the default pipeline as of v1.4.0 (specific analyzer set, specific MECHANISM_REGISTRY count). Missing: the adversarial document itself; the construction method; KNOWN_LIMITS.md; the pinning test. Available: Q1 problem statement as the construction specification; Bayyinah's own analyzer source code as the construction substrate (any concealment shape outside the registered mechanism set is by definition a Q1 candidate).

**Step 3, Ar-Rahman ar-Rahim.** MDL: one adversarial document + one construction-method appendix + one pinning test. FRaZ: publishing the gap is FRaZ-earned because the alternative (the project claims completeness without evidence of its boundary) is the exact performed-alignment shape Bayyinah was built to detect; the project must apply its own thesis to itself. Patent invariant clause: this release adds a documentation file and a pinning test; it does NOT add or modify any analyzer, mechanism, or scoring primitive. Cow Episode anchor: do not construct an "easy" adversarial document that exposes a gap so trivial it is closeable in the same release; the gap must be load-bearing and worth keeping open as a published acknowledgement.

**Step 4, Maliki Yawm ad-Din.** Time budget: 3 -- 4 person-weeks (construction + documentation + pinning test + community-review window). Release-gate accountability: KNOWN_LIMITS.md is published before tag; pinning test asserts the document scores 1.0; CHANGELOG cross-links the file. Slip discipline: if the constructed adversarial document is contested (the score is 0.9 not 1.0, the construction method depends on undocumented decoder behavior), the release ships only when the contest is resolved.

**Step 5, Iyyaka Na'budu.** Drift indicator: a v1.5.x+ release closes the published Q1 gap without updating KNOWN_LIMITS.md with the new gap-shape. Detection: CI gate that runs the published adversarial document through the default pipeline and asserts the score is 1.0; if the score drops below 1.0, the gap is closed and KNOWN_LIMITS.md must be updated in the same release with the next gap-shape. Mid-release checkpoint: construction method reviewed by validator-by-different-instance before document publishes.

**Step 6, Ihdina as-Sirat al-Mustaqim.**
(1) Adversarial document constructed: an artifact in one of the 23 supported file kinds that scores 1.0 on default pipeline despite carrying concealed payload.
(2) Construction method documented in `KNOWN_LIMITS.md` Appendix A.
(3) `KNOWN_LIMITS.md` authored at repo root with: stated gap shape, construction method, score evidence, why the gap is load-bearing, what would close it.
(4) Pinning test in `tests/test_known_limits.py` asserting the document scores 1.0.
(5) `tests/fixtures/known_limits/` corpus containing the adversarial document and any supporting fixtures.
(6) `RETIREMENT_LEDGER.md` Round 15 entry naming Q1 closure + structural defense (the pinning test).
(7) `CHANGELOG.md` entry under `## [1.5.0]` with `### Q1 closure` heading.
(8) `README.md` cross-link to KNOWN_LIMITS.md in the "What Bayyinah detects" section.
(9) `HANDOFF.md` v1.5.0 rewrite.
(10) Public surface pin `V1_5_0_SURFACE`.

**Step 7, Sirat alladhina.** Worked: the audit framework's recursive-application principle (Bayyinah's thesis applied to Bayyinah) is the project's strongest structural-honesty claim; Q1 has been open since the first framework audit. Failed: previously the project claimed completeness implicitly by virtue of mechanism count; the false completeness claim was the substrate-surface gap Bayyinah's own thesis names. Cow Episode for v1.5.0: do not write KNOWN_LIMITS.md as PR copy; the document is a worked counterexample, not a list of known issues. Release gate: pinning test passes (document scores 1.0); KNOWN_LIMITS.md is at repo root and front-page-linked from README; v1.5.0 scanned by v1.4.0.

**Closing dua, v1.5.0:** Rabbana taqabbal minna.

---

### 3.5 Release v1.6.0, Round 16 (Q-PRO-3 honest budget controller + Q-PRO-4 supply-chain disposition)

**Step 1, Bismillah.** Authority: prototype-concept short-list filed in `MIGRATION_PLAN.md` (Q-PRO-3 and Q-PRO-4); the existing `ScanService` orchestrator in `application/scan_service.py`; the existing `scan_incomplete: bool` and `scan_complete: bool` fields shipped in v1.2 / v1.4. Purpose hierarchy: serve enterprise SLAs whose CI pipelines need wall-clock budgets per scan; then commercial buyers who require structural-honesty guarantees on partial-scan reporting; then the project's own structural-honesty discipline that names Munafiq-pattern violations as ship-blocking. Beneficiary: enterprise integrators whose pipelines time-bound each scan and whose audit trails must distinguish "scan completed in budget" from "scan timed out and partial result was returned." Technical objective: (a) land Q-PRO-3 honest budget controller in `ScanService` with structural invariant that `scan_complete=True` and any analyzer being budget-cut cannot both hold; (b) resolve Q-PRO-4 supply-chain scope decision (SBOM / in-toto / Sigstore disposition) AS A `QUESTIONS.md` answer rather than as an absorbed feature. In-scope (a): wall-clock budget parameter on `ScanService().scan(path, budget_seconds=...)`; structural invariant assertion in `IntegrityReport.__post_init__` or equivalent; 50 budget-exhausted-scan fixtures asserting the invariant across multiple file kinds. In-scope (b): decision-of-record in `QUESTIONS.md` resolved section moving Q-PRO-4 from open to resolved, naming explicit answer (in scope / out of scope / partial scope with conditions). Out-of-scope: actual SBOM / in-toto / Sigstore extractor work (regardless of Q-PRO-4 disposition; if Q-PRO-4 resolves "in scope," that work begins in v1.7.0+); any breaking change to `ScanService.scan` signature beyond an additive `budget_seconds` parameter.

**Step 2, Alhamdulillah.** Inherited: v1.5.0 substrate including KNOWN_LIMITS.md; the `ScanService` orchestrator pattern; `scan_complete`, `scan_incomplete`, and `coverage` fields. Stable: file-router polyglot detection; analyzer registry composition rules; the v1.2.1 subprocess-isolation 30-second wall-clock timeout (which is the outermost budget; v1.6.0's controller is the inner per-analyzer budget). Missing: per-analyzer budget tracking; structural-invariant assertion; the 50 budget-exhausted fixtures; the Q-PRO-4 decision-of-record. Available: Q-PRO-3 design from the prototype (the "NEVER-dishonest-COMPLETE" pattern); Q-PRO-4 framing from `MIGRATION_PLAN.md`.

**Step 3, Ar-Rahman ar-Rahim.** MDL (a): the budget controller is one parameter addition to `ScanService.scan` plus one assertion in `IntegrityReport.__post_init__` plus 50 fixtures. MDL (b): the disposition is one entry in `QUESTIONS.md` under Resolved naming the answer with rationale. FRaZ: the budget controller is FRaZ-earned because partial-scan-returns-complete is the exact Munafiq pattern Bayyinah was built to detect; structurally preventing the producer side from emitting it is the recursive application. Q-PRO-4 is FRaZ-earned because supply-chain expansion is the largest scope-creep risk in the v1.2.4 → v2.0.0 sequence and leaving it unanswered invites later scope drift. Patent invariant clause: (a) adds an optional parameter to a public method; (b) adds a QUESTIONS.md entry. Neither alters `Finding`, `IntegrityReport`, `BaseAnalyzer`, `compute_muwazana_score`, or `tamyiz_verdict`. Cow Episode anchor: do not extend the budget controller into a full cooperative-cancellation primitive or a learned-budget heuristic; the minimum is wall-clock + structural assertion. Do not resolve Q-PRO-4 by saying "let us scope-expand into supply-chain and see what happens"; the answer is named and the consequences ride with it.

**Step 4, Maliki Yawm ad-Din.** Time budget: 4 person-weeks (a: 3 weeks; b: 1 week). Release-gate accountability: the 50-fixture budget-exhausted assertion passes; QUESTIONS.md Q-PRO-4 moved to Resolved with the answer documented; CHANGELOG cross-links the decision-of-record. Slip discipline: (a) and (b) can ship independently; if (a) is contested, (b) ships solo as v1.6.0 and (a) lands in v1.7.0. If (b) is contested, the question stays open and v1.6.0 ships only (a).

**Step 5, Iyyaka Na'budu.** Drift indicator (a): the structural invariant is asserted in tests but not in the runtime `__post_init__`; the invariant becomes test-only and fails to protect production scans. Detection: a Hypothesis property-based test that constructs `IntegrityReport` instances with arbitrary field combinations and asserts the invariant runtime-fails on dishonest combinations. Drift indicator (b): Q-PRO-4 resolves "partial scope with conditions" without naming the conditions, leaving future scope drift unguarded. Detection: the QUESTIONS.md resolved entry must enumerate the conditions explicitly or the resolution does not land. Mid-release checkpoint: prototype budget controller exercised against 5 representative file kinds before the 50-fixture corpus is locked.

**Step 6, Ihdina as-Sirat al-Mustaqim.**
(1) `application/scan_service.py` updated: `scan(path, *, budget_seconds: float | None = None)` parameter added.
(2) `domain/integrity_report.py` updated: structural invariant in `__post_init__` asserting `scan_complete=True` implies all analyzers completed within budget.
(3) `application/budget_controller.py` (new file) implementing per-analyzer budget tracking with cooperative checks.
(4) `tests/fixtures/budget/` corpus: 50 budget-exhausted scan scenarios across multiple file kinds.
(5) `tests/application/test_budget_controller.py` with the 50-fixture assertion + a Hypothesis property test on `IntegrityReport.__post_init__`.
(6) `QUESTIONS.md` Q-PRO-4 moved to Resolved section with the answer documented (decision + rationale + conditions).
(7) `RETIREMENT_LEDGER.md` Round 16 entry naming Q-PRO-3 closure + Q-PRO-4 closure (and the structural defenses).
(8) `CHANGELOG.md` entry under `## [1.6.0]` with `### Added` and `### Q-PRO-3 closure` and `### Q-PRO-4 resolution` headings.
(9) `README.md` updated: ScanService.scan signature reflects the new parameter; SLA section mentions the structural-honesty guarantee.
(10) `HANDOFF.md` v1.6.0 rewrite.
(11) Public surface pin `V1_6_0_SURFACE` reflecting the additive parameter.

**Step 7, Sirat alladhina.** Worked: the v1.2.1 subprocess-isolation pattern is the outer budget; the v1.6.0 controller is the inner budget; the two compose. Failed: prior to v1.6.0, partial-scan reports could quietly assert `scan_complete=True` if no analyzer raised, even when an analyzer was budget-cut by the outer 30-second timeout; the gap was a Munafiq pattern at the producer surface. Cow Episode for v1.6.0: do not over-design the budget controller into a learned or adaptive system; the wall-clock + structural assertion is sufficient. Release gate: 50-fixture assertion passes; structural invariant fails runtime when dishonestly constructed; QUESTIONS.md Q-PRO-4 resolved entry present; v1.6.0 scanned by v1.5.0.

**Closing dua, v1.6.0:** Rabbana taqabbal minna.

---

### 3.6 Release v1.7.0, Round 17 (Q5 closure: default cross-modal correlation policy)

**Step 1, Bismillah.** Authority: `QUESTIONS.md` Q5 (cross-modal correlation is documented but not default-on); the v1.2 README disclosure note staged for v1.3 candidate decision; the `CrossModalCorrelationEngine` interface shipped in v1.1. Purpose hierarchy: serve video and audio scan consumers whose default-pipeline output today does not exercise cross-modal divergence detection; then enterprise CI integrations that have pinned to the v1.1 default-off behavior; then the project's own structural-honesty discipline that names "documented capability not exercised by default" as a surface-vs-substrate gap. Beneficiary: anyone scanning video or audio files who reads the README's mechanism table and expects the default pipeline to exercise what the table lists. Technical objective: ship the default cross-modal correlation policy decision (default-on vs default-off) with implementation. In-scope: the decision-of-record; `ScanService.scan` wiring change if default-on; README mechanism-table footnote update if default-off; coverage field semantics update to reflect the decision; deprecation warning if the choice flips the v1.1 default behavior; new feature-flag if backward compatibility is preserved. Out-of-scope: any rule additions beyond the v1.1 baseline (`cross_stem_inventory`, `cross_stem_undeclared_text`); any of the 5 reserved rule names (`cross_stem_text_inconsistency`, `cross_stem_metadata_clash`, `embedded_media_recursive_scan`, `cross_stem_coordinated_concealment`, `cross_file_media_divergence`); engine architecture changes.

**Step 2, Alhamdulillah.** Inherited: v1.6.0 substrate including the honest budget controller and Q-PRO-4 resolution. Stable: `CrossModalCorrelationEngine` interface; the v1.1 two-rule baseline; the README mechanism table claim; the v1.2 disclosure note. Missing: the policy decision; the wiring change; the deprecation warning if applicable. Available: Q5 problem statement in QUESTIONS.md; the v1.2 disclosure note as a transition document.

**Step 3, Ar-Rahman ar-Rahim.** MDL: the policy is one decision plus the wiring change plus the coverage-field semantics update. FRaZ: default-on closes a documented surface-substrate gap (the README says it is supported; the default does not exercise it); default-off retains the gap but eliminates the breaking-change risk for downstream consumers. Either direction is FRaZ-earned because the alternative is "leave Q5 open indefinitely." Patent invariant clause: this release MAY change the default `ScanService.scan` output for VIDEO and AUDIO kinds; the verdict mechanic and finding shape are UNCHANGED. Cow Episode anchor: do not bundle Q5 with the 5 reserved-name rule additions; those are deferred to future rounds; v1.7.0 ships the policy decision and the baseline-two-rule wiring only.

**Step 4, Maliki Yawm ad-Din.** Time budget: 3 person-weeks. Release-gate accountability: decision-of-record published; wiring change implemented; coverage-field semantics updated; PARITY procedure followed if default-on is a parity break for VIDEO and AUDIO Phase 0 fixtures. Slip discipline: if community input contests the decision, v1.7.0 ships the migration shim with feature flag default-off (preserving v1.1.x behavior) and the active default-flip waits for v1.8.0.

**Step 5, Iyyaka Na'budu.** Drift indicator: the default decision is implemented but the coverage field does not reflect it (a default-on cross-modal scan reports coverage that does not list `cross_modal_correlation`; a default-off scan lists it as available). Detection: CI gate asserting `coverage` field consistency with the default pipeline output. Mid-release checkpoint: decision-of-record reviewed by validator-by-different-instance before code merges.

**Step 6, Ihdina as-Sirat al-Mustaqim.**
(1) `docs/scope/v1_7_0_cross_modal_default_decision.md` recording Q5 deliberation and decision.
(2) `application/scan_service.py` wiring change (or annotated no-op if default-off retained).
(3) `domain/integrity_report.py` coverage-field semantics updated.
(4) Deprecation warning or migration shim if applicable.
(5) PARITY procedure if applicable: issue tagged, CHANGELOG `### Parity-break` heading, corpus update, parity test update.
(6) `RETIREMENT_LEDGER.md` Round 17 entry naming Q5 closure.
(7) `CHANGELOG.md` entry under `## [1.7.0]` with `### Q5 closure` heading.
(8) `README.md` mechanism table footnote updated to reflect default-on vs default-off; the v1.2 disclosure note retired or rewritten.
(9) `HANDOFF.md` v1.7.0 rewrite.
(10) Public surface pin `V1_7_0_SURFACE`.

**Step 7, Sirat alladhina.** Worked: the v1.2 README disclosure note made the gap visible before v1.7.0 resolved it; that visibility is the structural-honesty discipline at work. Failed: prior to the disclosure note, the README's mechanism table implicitly claimed default-on coverage that the default pipeline did not deliver; that gap was the surface-substrate divergence Bayyinah's own thesis names. Cow Episode for v1.7.0: do not ship "cross-modal correlation default-on with adaptive rule activation"; the minimum is the binary policy + baseline two rules. Release gate: decision-of-record published; default reflects the decision; coverage field consistent; v1.7.0 scanned by v1.6.0.

**Closing dua, v1.7.0:** Rabbana taqabbal minna.

---

### 3.7 Release v1.8.0, Round 18 (Q8 closure: differential testing vs pdfid + oletools + yara + clamav)

**Step 1, Bismillah.** Authority: `QUESTIONS.md` Q8 (test count is not test quality); the audit framework v3.0 §10.1 round-trip Shape A/B/C responses principle; the two-witnesses principle the README invokes (Al-Baqarah 2:282). Purpose hierarchy: serve commercial buyers who need value-add evidence vs incumbents before adopting; then security researchers who need a published differential surface to attack; then the project's own structural-honesty discipline that names "witnessed only by the project's own fixtures" as a single-witness category. Beneficiary: enterprise procurement reviewers comparing Bayyinah to pdfid / oletools / yara / clamav. Technical objective: ship a differential testing harness in `tests/redteam/diff/` that runs a shared corpus through all five tools (Bayyinah + four incumbents) and publishes the per-tool detection matrix as `docs/benchmarks/diff_v1_8_0.md`. The published report states matches / exceeds / falls-behind explicitly, with no superiority claim the harness does not back. In-scope: harness implementation that runs each tool against the shared corpus; corpus assembly (at least 30 fixtures spanning PDF, DOCX, EML, XLSX with documented adversarial shapes); per-tool result normalization; published differential matrix; pinning test that the harness runs and the matrix is current. Out-of-scope: mutation testing, property-based testing with Hypothesis on the score function, adversarial fuzzing of FileRouter (these Q8 items deferred to v2.0.x corrigenda or future rounds).

**Step 2, Alhamdulillah.** Inherited: v1.7.0 substrate including the Q5 closure. Stable: Bayyinah's full mechanism set; the existing fixture corpus across 23 file kinds; the existing `tests/redteam/round_12_gauntlet` pattern as a worked example of red-team-style testing. Missing: pdfid / oletools / yara / clamav as test-time dependencies; the shared corpus assembled to be sized for differential analysis; the harness; the published matrix. Available: open-source incumbents are pip-installable or apt-installable; existing per-kind adversarial fixture corpora in `docs/adversarial/` as construction starting points.

**Step 3, Ar-Rahman ar-Rahim.** MDL: one harness directory + one shared corpus + one Markdown report. FRaZ: differential testing is FRaZ-earned because Q8 explicitly names it as the primary external witness layer to prioritize for v1.3 (which v1.8.0 closes after intervening commercial-readiness work). Other Q8 items (mutation, property-based, fuzzing) are secondary witnesses; deferring them to corrigenda is the discipline cost of prioritizing the procurement-readiness signal. Patent invariant clause: this release adds a test harness and a documentation file; it does NOT alter any analyzer, mechanism, Finding shape, scoring primitive, or verdict. Cow Episode anchor: do not claim "Bayyinah is better than X / Y / Z" in the differential matrix unless the harness backs it; the report's honesty discipline IS the matrix's value. The phrase "falls behind" must appear when applicable, and the falling-behind is documented as a future-round candidate.

**Step 4, Maliki Yawm ad-Din.** Time budget: 6 -- 8 person-weeks (corpus assembly is the long-pole). Release-gate accountability: the harness runs to completion against the shared corpus on CI; the matrix is published; per-tool dependencies are documented in `requirements-dev.txt` per the dependency-manifest discipline. Slip discipline: if any incumbent's CLI surface changes during corpus assembly, the harness is updated and the report is re-generated; if the report's honesty discipline is contested by an external reviewer (e.g., Bayyinah's "exceeds" claim depends on a corpus that systematically favors Bayyinah's mechanism set), the corpus is rebalanced before tag.

**Step 5, Iyyaka Na'budu.** Drift indicator: the published matrix claims "exceeds" without the harness backing it. Detection: pinning test that re-runs the harness on CI and asserts the matrix entries are derivable from the harness output. Mid-release checkpoint: corpus assembly reviewed for systematic bias (does the corpus over-represent mechanism shapes Bayyinah was specifically designed for? if yes, rebalance).

**Step 6, Ihdina as-Sirat al-Mustaqim.**
(1) `tests/redteam/diff/` harness implementation.
(2) `tests/fixtures/diff/` shared corpus (30+ fixtures).
(3) `tests/redteam/diff/run_diff.py` harness entry point producing JSON output.
(4) `docs/benchmarks/diff_v1_8_0.md` published differential matrix with matches / exceeds / falls-behind per fixture and per tool.
(5) Pinning test in `tests/redteam/test_diff_matrix_current.py` asserting the matrix is derivable from the harness output.
(6) `requirements-dev.txt` and `pyproject.toml` `[project.optional-dependencies].dev` updated with pdfid / oletools / yara / clamav per dependency-manifest discipline.
(7) `RETIREMENT_LEDGER.md` Round 18 entry naming Q8 partial closure (differential testing; mutation/property/fuzzing deferred).
(8) `CHANGELOG.md` entry under `## [1.8.0]` with `### Added`, `### Q8 closure (partial)`, headings.
(9) `README.md` link to `docs/benchmarks/diff_v1_8_0.md` from a "Differential testing" subsection of the "What Bayyinah detects" section.
(10) `HANDOFF.md` v1.8.0 rewrite.
(11) Public surface pin `V1_8_0_SURFACE`.

**Step 7, Sirat alladhina.** Worked: the existing per-kind adversarial fixture corpora in `docs/adversarial/` show the project understands the value of external-shape thinking; the differential harness extends that to multi-tool comparison. Failed: prior to v1.8.0, Bayyinah's claim of value-add was self-witnessed; the procurement question "is this better than pdfid for our use case" had no Bayyinah-published answer. Cow Episode for v1.8.0: do not assemble a corpus that systematically favors Bayyinah's mechanism set; the corpus must include shapes Bayyinah does not detect well and document them honestly. Release gate: harness runs on CI; matrix is current; honesty discipline holds (no unbacked superiority claims); v1.8.0 scanned by v1.7.0.

**Closing dua, v1.8.0:** Rabbana taqabbal minna.

---

### 3.8 Release v1.9.0, Round 19 (Q10 closure: framework-free engineering principles)

**Step 1, Bismillah.** Authority: `QUESTIONS.md` Q10 (strategic coupling of framework and engineering); the project's Apache-2.0 OSS posture; the adoption-ceiling question Q10 names explicitly. Purpose hierarchy: serve security-team adopters whose procurement is gated on framework-free integration briefs; then academic citers whose institutions require framework-neutral engineering documentation; then the project's own discipline of distinguishing what the framework explains (the WHY) from what the engineering principles ARE (the WHAT). Beneficiary: anyone whose adoption is gated on framework-neutral documentation. Technical objective: publish `docs/principles.md` as a framework-free statement of the engineering principles (deterministic byte-level checks, fail-closed defaults, additive-only invariants, fixture-pinned tests, parity-break procedure, scan-incomplete semantics, scoring discipline, structural-honesty patterns). README cross-links it without removing the Quranic framework section. In-scope: `docs/principles.md` authored; README cross-link added; CHANGELOG entry; pinning test asserting the document exists and references the load-bearing principles. Out-of-scope: removal of any Quranic-framework content from README or other docs (the framework section stays; the framework-free section is additive); modification of the engineering principles themselves (Q10 is about documentation, not redesign).

**Step 2, Alhamdulillah.** Inherited: v1.8.0 substrate including the differential testing matrix; the existing FRAMEWORK.md, PARITY.md, NAMING.md as framework-anchored documents. Stable: the engineering principles themselves (they already hold; Q10 is whether they are documented framework-free). Missing: the framework-free document; the README cross-link. Available: Q10 problem statement as the construction specification; the existing engineering principles are already present in FRAMEWORK.md, CHANGELOG, and CONTRIBUTING.md but mixed with framework explanation.

**Step 3, Ar-Rahman ar-Rahim.** MDL: one document + one README cross-link + one pinning test. FRaZ: the framework-free statement is FRaZ-earned because Q10 names the adoption ceiling and the project's Apache-2.0 posture deliberately aims at broader adoption than the framework's audience. Patent invariant clause: this release adds a documentation file and a README cross-link; it does NOT modify any code, contract, or framework-anchored document. Cow Episode anchor: do not remove or weaken the framework-anchored content; Q10 is explicit that the framework section stays.

**Step 4, Maliki Yawm ad-Din.** Time budget: 2 -- 3 person-weeks. Release-gate accountability: `docs/principles.md` is at `docs/` root; README cross-links it; the document references each load-bearing principle by name. Slip discipline: if the document is contested (e.g., the principles section reads like FRAMEWORK.md rewritten without the Quranic vocabulary, which would be redundant), the document is rescoped to focus on the engineering principles that DO stand framework-free.

**Step 5, Iyyaka Na'budu.** Drift indicator: `docs/principles.md` quietly removes or weakens framework-anchored language elsewhere. Detection: CI gate that asserts FRAMEWORK.md, NAMING.md, and the README's framework section are unchanged in size and load-bearing structure across the v1.8.0 → v1.9.0 diff. Mid-release checkpoint: framework-free draft reviewed by validator-by-different-instance to confirm it is additive, not substitutive.

**Step 6, Ihdina as-Sirat al-Mustaqim.**
(1) `docs/principles.md` authored covering: deterministic byte-level checks, fail-closed defaults, additive-only invariants, fixture-pinned tests, parity-break procedure, scan-incomplete semantics, scoring discipline (per v1.4.0 decision), structural-honesty patterns.
(2) README cross-link added in an "Engineering principles" subsection of the "Why Bayyinah" section.
(3) Pinning test in `tests/test_docs_principles_current.py` asserting the document exists and references each load-bearing principle by name.
(4) `RETIREMENT_LEDGER.md` Round 19 entry naming Q10 closure.
(5) `CHANGELOG.md` entry under `## [1.9.0]` with `### Q10 closure` heading.
(6) `HANDOFF.md` v1.9.0 rewrite.
(7) Public surface pin `V1_9_0_SURFACE`.

**Step 7, Sirat alladhina.** Worked: FRAMEWORK.md and NAMING.md as framework-anchored documents are load-bearing for the audience whose adoption is downstream of accepting the framework. Failed: prior to v1.9.0, the project had no documentation surface for adopters whose acceptance is gated on framework-neutrality; the adoption ceiling Q10 names was operational. Cow Episode for v1.9.0: do not write `docs/principles.md` as a rewrite of FRAMEWORK.md with the Quranic vocabulary stripped; the document must offer engineering principles in their own load-bearing right, with the framework providing the WHY (in FRAMEWORK.md) and the principles providing the WHAT (in `docs/principles.md`). Release gate: document published; README cross-links it; pinning test passes; framework-anchored docs unchanged; v1.9.0 scanned by v1.8.0.

**Closing dua, v1.9.0:** Rabbana taqabbal minna.

---

### 3.9 Release v2.0.0, Round 20 (Q9 external human audit + recursive self-verification + commercialization gate)

**Step 1, Bismillah.** Authority: `QUESTIONS.md` Q9 (cross-model audit shares failure modes; external human audit is the missing layer); the audit framework v3.0 §5.2 validator-by-different-instance protocol extended to external paid auditors; the Munafiq Protocol §9 recursive application at v2.0 (Bayyinah scans Bayyinah). Purpose hierarchy: serve enterprise buyers whose procurement is gated on an external auditor's findings being public; then security researchers who need the foreign-instance scan ledger as their verification substrate; then the project's commercialization timeline that names v2.0 as the gate. Beneficiary: anyone evaluating Bayyinah for commercial adoption at v2.0. Technical objective: conjunctively (1) close Q9 with an external paid human auditor's findings published with disposition; (2) verify the recursive self-verification structural check (foreign Claude instance scans Bayyinah's own substrate and returns `sahih` on every scanned artifact); (3) ship the commercialization readiness package (case studies, comparison matrix, enterprise integration guide, KNOWN_LIMITS.md front-page-linked, SLA disclosure). In-scope: external auditor sourcing + audit cycle + finding publication + disposition; foreign Claude instance scan ledger pinned in `tests/test_bayyinah_self_scan.py`; `docs/v2.0/external_audit_2026.md`; `docs/v2.0/case_studies.md`; `docs/v2.0/comparison_matrix.md` (derivative of v1.8.0 differential testing); `docs/enterprise.md`; SLA disclosure block on the bayyinah.dev landing page. Out-of-scope: TQL-1 / FAA qualification; multi-language ports; supply-chain extractor work regardless of Q-PRO-4 disposition; any framework redesign.

**Step 2, Alhamdulillah.** Inherited: v1.9.0 substrate including all prior round closures + framework-free docs/principles.md + differential testing matrix; the full Phase 1 through Phase 5 substrate from the prior release sequence. Stable: 23 file kinds; MECHANISM_REGISTRY at the v1.9.0 count; verdict mechanic; score function shape (per v1.4.0 decision); cross-modal correlation default (per v1.7.0 decision); honest budget controller (per v1.6.0); KNOWN_LIMITS.md (per v1.5.0); differential matrix (per v1.8.0); framework-free principles (per v1.9.0). Missing: the external auditor (long-pole sourcing); the foreign Claude scan ledger; the v2.0 docs/ tree. Available: bayyinah.dev as the deployed substrate; the v1.2.4 → v1.9.0 release sequence as the worked discipline trail; the audit framework v3.0 maturity Level 4 self-assessment as the auditor's starting point.

**Step 3, Ar-Rahman ar-Rahim.** MDL: the external audit is the load-bearing item (one paid auditor, one audit cycle, one published findings file with disposition). The recursive self-verification is the structural check (foreign Claude instance + scan ledger + pinning test). The commercialization package is the documentation set (case studies + comparison matrix + enterprise guide + SLA). FRaZ: every condition in v2.0.0 is FRaZ-earned because the alternative is shipping v2.0.0 with the same single-witness limitation Q9 names. Patent invariant clause: this release ships documentation + the foreign-instance scan ledger; it does NOT alter any analyzer, mechanism, contract, scoring primitive, verdict, or framework. The MECHANISM_REGISTRY is frozen at the v2.0.0 baseline as a long-term reference (future deltas allowed but baseline pinned). Cow Episode anchor: do not over-specify the commercialization package; the case studies are concrete, the comparison matrix derives from v1.8.0 work, the enterprise guide is operational, the SLA is honest. Marketing copy that overstates the v2.0.0 substance is itself the Munafiq pattern at the release surface.

**Step 4, Maliki Yawm ad-Din.** Time budget: 12 -- 16 person-weeks (auditor cycle is the long-pole; documentation + pinning test are parallelizable). Release-gate accountability: v2.0.0 ships if and only if ALL eight conjunctive conditions named in §5 hold at ship time; no corrigendum substitution is permitted on any v2.0.0 condition. Slip discipline: if the external auditor cannot be sourced by the v2.0.0 target date, a v1.15.x bridge ships in the interim per the audit framework slip-naming convention; v2.0.0 is rescheduled. The rescheduling is itself disclosed in CHANGELOG.

**Step 5, Iyyaka Na'budu.** Drift indicator: v2.0.0 ships with the external auditor's findings selectively edited or quietly omitted. Detection: the published findings file contains every finding from the auditor's report verbatim with per-finding disposition (closed in v2.0.0, deferred with named retirement condition, accepted-as-stated with rationale). The auditor signs off on the published version. Mid-release checkpoint: foreign Claude scan ledger run at 75% of the time budget to confirm the recursive check structurally passes before the final tag.

**Step 6, Ihdina as-Sirat al-Mustaqim.**
(1) External paid auditor sourced (a security researcher or audit firm with no prior relationship to the project and no acceptance of the Munafiq Protocol as premise).
(2) Audit cycle completed: the auditor reviews Bayyinah's substrate against their own criteria over an agreed-upon period.
(3) `docs/v2.0/external_audit_2026.md` published containing the auditor's findings verbatim with per-finding disposition (closed / deferred / accepted-as-stated).
(4) Foreign Claude instance (a Claude session not used in this strategy or in the prior release sequence) runs Bayyinah against Bayyinah's own substrate (CHANGELOG, README, src files, docs, fixtures) on a fixture set the producer did not author; verdict is `sahih` on every scanned artifact.
(5) `tests/test_bayyinah_self_scan.py` pinning the foreign-instance scan ledger.
(6) `docs/v2.0/case_studies.md` with at least three concrete deployments and per-deployment value-add evidence.
(7) `docs/v2.0/comparison_matrix.md` derived from the v1.8.0 differential testing report; refreshed with the v2.0.0 detection set.
(8) `docs/enterprise.md` covering CI integration, SLA, support posture, deployment options (pip / Docker / API).
(9) bayyinah.dev landing page SLA disclosure block.
(10) `KNOWN_LIMITS.md` (from v1.5.0) front-page-linked from README and bayyinah.dev landing page.
(11) `RETIREMENT_LEDGER.md` Round 20 entry naming Q9 closure + recursive self-verification structural check + commercialization package.
(12) `CHANGELOG.md` entry under `## [2.0.0]` with `### Q9 closure`, `### Recursive self-verification`, `### Commercialization readiness` headings.
(13) `README.md` v2.0.0 revisions: external audit reference, recursive self-verification reference, commercialization package linked.
(14) `HANDOFF.md` v2.0.0 rewrite.
(15) Public surface pin `V2_0_0_SURFACE`.
(16) `MECHANISM_REGISTRY` frozen at v2.0.0 baseline; future deltas allowed but baseline pinned in a `V2_0_0_MECHANISM_BASELINE` constant.

**Step 7, Sirat alladhina.** Worked: the round-by-round closure discipline through v1.2.5 → v1.9.0 produced the substrate v2.0.0 ratifies. Every prior round's structural defense is in place and operational. Failed: prior to v2.0.0, the project's audit-cleanness claim was witnessed only by the producer's own audit chain (cross-model with three LLMs but no human paid to find holes); Q9 was the open layer. Cow Episode for v2.0.0: do not ship v2.0.0 as a marketing event with the structural substance underneath the marketing being thin; the external audit findings, the foreign-instance scan ledger, the differential matrix, and the commercialization package are each load-bearing and each must hold on their own. Release gate (the eight conjunctive conditions named in §5): all of them, conjunctively, at ship time, with no corrigendum substitution.

**Closing dua, v2.0.0:** Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

---

## 4. Per-release closure artifacts (load-bearing every release)

For consistency, every release in this strategy carries these six artifacts at ship time:

1. **CHANGELOG.md** entry under `## [vX.Y.Z]` with appropriate `### Added`, `### Changed`, `### Deprecated`, `### Removed`, `### Fixed`, `### Security`, `### Parity-break` (when applicable), `### Round X closure` headings.
2. **RETIREMENT_LEDGER.md** entry naming each finding closed and the structural defense that prevents the failure mode from recurring.
3. **Pinning test** in `tests/<domain>/test_*.py` failing closed if the structural defense is removed.
4. **Fixture corpus update** in `tests/fixtures/<kind>/` when the release introduces or changes mechanism behavior; PARITY procedure when the release breaks v0 parity.
5. **`bayyinah/mechanisms/registry.py`** updated with any new mechanism, its tier, cost class, and ZAHIR/BATIN classification (per FRAMEWORK.md five-place pattern).
6. **Public surface pin** in `tests/test_public_surface_additive.py` with a new `V_X_Y_Z_SURFACE` constant aliasing the prior surface even if unchanged (framework v3 §18.3 cadence).

Plus, when the release applies: PARITY-break procedure (issue tagged + CHANGELOG heading + corpus update + parity test update); README change (five-place doc pattern satisfied only after the README reflects the new behavior); audit handoff (HANDOFF.md rewrite at every minor; patches inherit prior minor's handoff with a delta note).

---

## 5. v2.0.0 release-gate (the conjunctive commercialization check)

v2.0.0 ships if and only if ALL of the following hold at ship time:

1. **External audit complete and public.** Paid external auditor (no prior relationship; does not accept the Munafiq Protocol as premise) completed their pass. Findings published verbatim in `docs/v2.0/external_audit_2026.md` with explicit per-finding disposition.
2. **Recursive self-verification structural check passes.** Foreign Claude instance runs Bayyinah against Bayyinah's own substrate and verdict is `sahih` on every scanned artifact. Fixture set authored externally. Pinned in `tests/test_bayyinah_self_scan.py`.
3. **Differential testing matrix current.** `docs/v2.0/comparison_matrix.md` updates the v1.8.0 baseline with the v2.0.0 detection set; matches / exceeds / falls-behind statements current.
4. **KNOWN_LIMITS.md current.** Either still scores 1.0 (the gap is honestly preserved) OR updated with a new adversarial document that demonstrates an analogous gap.
5. **`docs/principles.md` current.** Framework-free statement updated to reflect any v1.9.0 → v2.0.0 behavior changes.
6. **Q9 closed.** Cross-model audit cleanness now backed by an external human auditor's finding.
7. **No regression** on the v1.2.4 baseline test suite. The 1,800+ tests pass plus the new tests added through v1.2.5 → v2.0.0.
8. **PARITY status disclosed.** PARITY.md reflects whichever parity breaks occurred through the sequence (v1.3.0, v1.4.0 if applicable, v1.7.0 if applicable). Q2 stays open with accumulated evidence appendix.

If any condition is not met, v2.0.0 does not ship. The honest disposition is to retag what was ready as v1.10.0 or v1.15.x per the audit framework's slip-naming convention and reschedule the v2.0.0 gate.

**No corrigendum substitution on v2.0.0 conditions.** Every condition above is internally controllable except (1) external auditor sourcing and the foreign-instance scan half of (2). Both are operationally achievable by the producer with normal contracting / community outreach; they do not require an external dependency that justifies a sunset clause.

---

## 6. What this strategy is NOT

- **Not a TQL-1 substrate.** The live repo's commercial target is enterprise security tooling adoption, not airworthiness qualification.
- **Not a multi-language port plan.** Q-PRO-2 may be filed as a future QUESTIONS.md entry but does not gate any release here.
- **Not a substrate-expansion charter.** Q-PRO-4 lands in v1.6.0 as an answered question, not as an absorbed feature. New substrate kinds beyond the existing 23 file kinds wait on that question's resolution.
- **Not a second governance framework.** Bayyinah Audit Framework v3.0 is the artifact-level contract; the Fatiha 7-step is the session-level cognitive scaffold. They operate at different layers and compose without collision.
- **Not a recursive-self-verification marketing claim.** The recursive self-verification check is retained as a v2.0.0 release-gate (§5 item 2), but the v2.0.0 commercial proposition is differential-tested + externally audited + known-limits-published + framework-free principles available + stable scoring + mature retirement discipline. The recursive check is discipline, not marketing.

---

## 7. Risks

Three named honestly:

1. **External auditor availability (v2.0.0 condition 1).** Sourcing a paid external auditor who is competent, willing to publicly disclose findings, and does not accept the framework's premises is a market problem. If the right auditor cannot be sourced by the v2.0.0 target date, v2.0.0 slips and a v1.15.x bridge ships.
2. **Score function migration (v1.4.0 Q3 closure).** Splitting the score is a parity break for every downstream consumer pinned to the current `integrity_score` field shape. The migration path needs to be communicated at v1.3.0 ship time so consumers have one release of warning.
3. **Default cross-modal correlation (v1.7.0 Q5 closure).** Either decision creates a discipline cost; the load-bearing requirement is that the chosen direction is honest about which cost it accepts.

---

## 8. Slip discipline

If any release misses its target:

1. The slip is filed under CHANGELOG `### Deferred` heading naming what slipped and which target tag absorbs it.
2. `QUESTIONS.md` is updated only if the slip surfaces an interpretive question the project had not already named.
3. The next release absorbs the slipped scope unless the slip surfaced a structural reason to reorder; in that case, this strategy is updated with a CHANGELOG entry.
4. `HANDOFF.md` records the slip explicitly. The next minor's handoff inherits the slip note.

Slipping is not a discipline failure; silently dropping scope is.

---

## 9. Closing

This strategy is auditable against Bayyinah Audit Framework v3.0 §23.4 maturity model. The maturity self-assessment at strategy-effective time:

- Round 11 acknowledged and queued for v1.2.5 per `RETIREMENT_LEDGER.md`.
- Round 13 (parity-break tier change) queued for v1.3.0.
- Open `QUESTIONS.md` Q1, Q3, Q4, Q5, Q8, Q9, Q10 individually scheduled.
- Q2 stays open across the sequence with accumulated evidence appendix; Q6 already resolved v1.2.1; Q7 verified shipped at v1.2.5 release-gate.
- Prototype concepts that did not survive the live-repo migration are recorded in `MIGRATION_PLAN.md` as Q-PRO entries; Q-PRO-3 and Q-PRO-4 are absorbed in v1.6.0; Q-PRO-1, Q-PRO-2, Q-PRO-5 remain unfiled questions the project may or may not raise.
- v2.0.0 release-gate is conjunctive, internally-controllable except for external auditor sourcing and foreign-instance scan, no corrigendum substitution.
- Slip discipline is named.
- Fatiha 7-step session structure is the cognitive scaffold for each release; Bayyinah Audit Framework v3.0 is the artifact-level discipline contract; the two compose without collision.

The Quranic anchor for the discipline this strategy ratifies is in `FRAMEWORK.md` already. The strategy itself adds nothing theological; it ratifies the existing discipline at the artifact layer and applies the existing cognitive scaffold at the session layer.

> Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.
> (Our Lord, accept this from us. Indeed, You are the All-Hearing, the All-Knowing.)

---

# Bismillah ir-Rahman ir-Rahim
