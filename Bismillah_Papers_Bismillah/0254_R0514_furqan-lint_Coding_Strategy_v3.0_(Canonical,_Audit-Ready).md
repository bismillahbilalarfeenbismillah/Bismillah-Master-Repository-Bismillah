# Bismillah ir-Rahman ir-Rahim

# R0514 -- furqan-lint Coding Strategy v3.0 (Canonical, Audit-Ready)

**Chronological Index:** 254 of 995  
**Date:** 2026-05-27  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** furqan_lint_coding_strategy_v3_0_canonical.md  
**Source Format:** md  
**SHA-256:** `035127acff93b5c50b0f874b0eb6e627a4e8e3719e24b1116e7a4e3c25e638ae`  

---

## R0514 · furqan-lint Coding Strategy v3.0 (Canonical, Audit-Ready)

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: furqan_lint_coding_strategy_v3_0_canonical.md
- source_format: md
- merged_variants: 1 (furqan_lint_coding_strategy_v3_0_canonical.pdf)
- text_sha256: 035127acff93b5c50b0f874b0eb6e627a4e8e3719e24b1116e7a4e3c25e638ae

# furqan-lint Coding Strategy v3.0 (Canonical, Audit-Ready)

*Bismillah ar-Rahman ar-Rahim*

**Status:** Pre-execution canonical. Authored June 23, 2026 for the audit cycle that precedes implementation.

**Supersedes:** `furqan_lint_v5_Strategy.pdf` (2026-05-27) and `furqan_lint_coding_strategy_v2_0.md` (2026-06-23, intermediate revision).

**Successor relationship:** v3.0 (this document) keeps v2.0's substrate-anchored revisions and Bayyinah-arc operational disciplines verbatim. v3.0 adds four canonicalizing layers that v2.0 left implicit:

1. **Audit protocol** (§12) — what cross-vendor auditors check, what constitutes audit-pass.
2. **Pre-execution gate** (§13) — what must be true before any v0.13.1 code is cut.
3. **Binding-claims index** (§14) — every checkable assertion in one indexed list.
4. **Risk register** (§15) — what could fail during execution, with mitigations.

v3.0 also resolves the four open decisions v2.0 §8 routed to the user, recording each as a proposed default with explicit audit-time override slot.

**Author:** Bilal Syed Arfeen
**Document Date:** June 23, 2026
**Document ID:** SHV-FLINT-STRAT-v3.0-canonical

---

## Opening — The Seven Steps Applied to This Canonical Revision

**Step 1 — Bismillah (Initialization).** Building: the canonical, audit-ready coding strategy for furqan-lint v0.13.1 through v1.0.1, the commercialization tier. Authority source: (a) the v5 strategy's seven-principle taxonomy and Fatiha Construct protocol; (b) the v2.0 strategy's substrate-anchored revisions and Bayyinah-arc operational disciplines; (c) the v1.0 dissertation (`Structural_Honesty_Verification_Dissertation_Arfeen_2026.pdf`) as the underlying framework; (d) the furqan-lint and Bayyinah provisional patent documents as the IP perimeter. Optimization function: produce a strategy artifact that survives multi-vendor audit before execution begins, in keeping with the dissertation's §11.3 trust-gradient discipline. Scope: canonical strategy specification and audit-readiness instrumentation. Out of scope: actual code authorship (deferred to post-audit cowork sessions), patent-claim drafting (separate counsel workstream).

**Step 2 — Alhamdulillah (State Acknowledgment).** Current substrate state, audit-grade:

- `main` HEAD: `v0.12.0+5 c5c3c4c` (al-Mursalat / Phase G11.2 Go Sigstore-CASM extension). Confirmed by v2.0 strategy.
- Unmerged tagged branches: `v0.13.0-an-naziat-v16` (ONNX G11.3), `v0.14.0-tasdiq-al-bayan-v11` (cross-substrate verification corpus), `v1.0.0-al-basirah-v11` (self-attestation, canonical mushaf chain closing).
- Baseline pytest at main HEAD: 500 passed / 68 skipped on fresh install; 642 with all extras populated per v0.12.0 CHANGELOG.
- Public checker surface: D24, D11, R3, return_none_mismatch (Python), Rust gate11 (G11.1), Go gate11 (G11.2), ONNX gate11 (G11.3, unmerged).
- Bayyinah scanner state: v2.0.1 (recursive self-verification gate at v2.0.0; first calibration corrective at v2.0.1; seven releases v1.5.0→v2.0.1 shipped in one cowork session — the empirical anchor for v3.0's pacing).
- Dissertation state: v1.0 publication form, 397 pages, deposited.
- Patent state: provisional filings for Bayyinah and furqan-lint on file; counsel briefing on file.
- Prior strategy docs: v5 (`furqan_lint_v5_Strategy.pdf`, 2026-05-27, substrate floor v0.8.5 — six minor versions stale at authoring time); v2.0 (`furqan_lint_coding_strategy_v2_0.md`, 2026-06-23, substrate floor v0.12.0+5 c5c3c4c — current and binding for v3.0).

**Step 3 — Ar-Rahman ar-Rahim (Calibration).** MDL discipline: this canonical revision preserves everything from v5 and v2.0 that the substrate has not disproved, and adds only the four audit-readiness layers that v2.0 left implicit. The seven-principle taxonomy is preserved verbatim. The Bayyinah-arc operational disciplines (byte-identity, substrate probe, sync map, flake protocol, cumulative-bundle/push-clone) are preserved verbatim. What is new is exclusively the audit-protocol scaffold, the pre-execution gate, the binding-claims index, and the risk register — together forming the artifacts a cross-vendor audit needs to bind this strategy as ready-to-execute.

**Step 4 — Maliki Yawm ad-Din (Deadline Awareness).** Time horizon: the audit cycle itself is bounded by one cowork session of cross-vendor review. Execution begins only after audit binds. Once execution begins, the commercialization arc runs in approximately 7-10 cowork sessions per v2.0's calibrated estimate (deflated by the user's "agent estimates are 75% inflated" discipline). Calendar time is not the binding unit; cowork session cadence determines it. The pre-execution audit cycle is itself a deadline-bounded session: if audit findings cannot be resolved within one audit cycle, the strategy returns for revision rather than executing under unresolved concerns.

**Step 5 — Iyyaka Na'budu (Orientation Check).** Am I producing the canonical strategy that an audit can actually bind, or am I producing the appearance of an auditable strategy? The drift indicator: if I find myself adding sections that look like audit instrumentation but do not produce check expressions an auditor can actually run, I have drifted. The binding-claims index (§14) and the risk register (§15) must be specific enough to be checked, not narrative. Every binding claim must be expressible as a runnable assertion or a verifiable artifact existence check.

**Step 6 — Ihdina as-Sirat al-Mustaqim (Task Execution).** Sequence: preserve v2.0's substantive content verbatim; resolve the four open decisions to proposed defaults; add the audit protocol; add the pre-execution gate; add the binding-claims index; add the risk register; close with the canonical seal that distinguishes this version from prior draft revisions. No other changes.

**Step 7 — Sirat Alladhina An'amta 'Alayhim (Anti-Pattern Avoidance).** What worked (Bayyinah arc empirical): cumulative-bundle patches from a pristine floor, push-clone delta extraction, patent-invariant byte-identity check as a release gate, three-line substrate probes per release, documented flake protocol, multi-locus sync verification. What worked (this strategy authoring): v2.0's substrate-anchoring discipline that caught the v5 strategy's six-minor-version-stale floor. What failed: v5's calendar-time horizons that did not account for session-pace shipping; v5's commercialization-signal definition that required external author groups instead of own-source recursive self-application. The Cow Episode warning specific to v3.0: do not specify the audit protocol so tightly that it becomes another over-specification layer the strategy must navigate. Auditors are competent; the protocol must be specific enough to bind but not so specific that it becomes the new constraint trap.

Begin.

---

## 1. The Strategy in Compressed Form (Canonical)

Six release tags, each governed by one of the v5 strategy's seven principles, shipped in cowork-session pace. The two cross-cutting principles (root architecture, disease model) operate at every layer. Mapping preserved verbatim from v2.0:

| Tag | Principle | Load-bearing feature | Bayyinah analogue |
| --- | --- | --- | --- |
| **v0.13.1** | P1 Bismillah (initialization) — declared scope | Contract-floor: `_CHECKER_REGISTRY` freeze + `tests/contracts/` directory + `KNOWN_LIMITS.md` + requirements-dev sync test + `.ax-sh.yaml` manifest schema v1 | v1.5.0 muwazana_score + scan_incomplete_clamp contract floor |
| **v0.14.1** | P2 Tanzil (phased delivery) — run-budget controller | Whole-repo lint budget with graceful stop; `lint_incomplete=True` honest reporting; deterministic-truncation ordering. Phase 1-4 disclosure UI deferred to v1.1.x per Cow Episode discipline. | v1.6.0 budget controller |
| **v0.15.0** | P3 Ring composition — cross-substrate correlation policy | When the same logical surface exists in Python live + Rust gate11 + Go gate11 + ONNX gate11 and substrates disagree, the published policy resolves which wins, when both fire, and when both are silenced. Substrate-layer ring composition; audit-ledger ring composition deferred to v1.2.x. | v1.7.0 cross-modal correlation policy |
| **v0.16.0** | P5 Zahir/Batin — differential testing matrix | Each Python checker cross-checked against an independent reference (D24 vs ruff RET503; D11 vs mypy strict; R3 vs pylint R1710; additive vs semgrep; gate11 Python vs sigstore CLI). Cross-substrate: tree-sitter vs cargo-check vs go-vet on the same fixture corpus. Disagreement is a test failure. | v1.8.0 differential testing matrix |
| **v0.17.0** | P4 Root architecture (surfaced) — framework-free principles doc | `docs/principles.md` — five engineering principles in vocabulary that holds without Furqan, BAF, Munafiq Protocol, or Quranic anchors. README stays framework-anchored; principles.md is the parallel entry-point for security review, regulated-industry compliance, academic citation. | v1.9.0 framework-free principles |
| **v1.0.0** | P6 al-Fatiha (recursive self-verification) — the commercialization signal | furqan-lint runs ALL its checkers against ITS OWN source tree on every CI run. Zero diagnostics required for any release in the commercialization tier. `_PENDING_CALIBRATION_FILES` pending-discipline forces promotion when a file starts scanning clean. **Composed with the existing unmerged `v1.0.0-al-basirah-v11` branch** (G12.0 self-attestation crypto-anchor + canonical mushaf chain closing). | v2.0.0 recursive self-verification gate |
| **v1.0.1** | (post-commercialization first corrective) | Whatever the v1.0.0 gate catches first. Round-12-style calibration corrective; substrate-conservative. | v2.0.1 file-router calibration corrective |

**Principle slots reserved for post-commercialization extension** (do not specify now per Cow Episode discipline):

- **v1.1.x range** — v5 strategy's v2.0 phased-disclosure suggestion engine (Phase 1-4 UI).
- **v1.2.x range** — v5 strategy's v3.0 audit ledger / cross-PR coherence.
- **v1.3.x range** — v5 strategy's v4.0 multi-observer / projection consistency.
- **v2.0** of furqan-lint (the SDK, not this strategy doc) — v5's v5.0 multi-implementation reference-parity. **Gated on whether independent reimplementations actually materialize by then.** The Bayyinah arc demonstrated that the commercialization signal does NOT require external reimplementations — it requires own-source recursive self-verification, which v1.0.0 already delivers.

**Cross-cutting principles** (preserved verbatim from v5 §7, applied at every release):

- **P4 Root architecture.** The framework's vocabulary (zahir, batin, muwazana, bayyinah, mizan, tanzil, bismillah, fatiha) is the root system. Each technical term carries its full operational meaning through its root. Naming discipline maintained across all versions in a NAMING.md analog.
- **P7 Disease model.** Every release treats failing modules as diseased components requiring diagnosis-treatment-verification, not betraying agents requiring rewrite-from-scratch.

---

## 2. Patent-Invariant Byte-Identity Discipline

Four surfaces in furqan-lint MUST stay byte-identical across the v0.13.0 → v1.0.1 commercialization arc. Any mutation to any of these is flagged as a patent-substrate change and routed through patent-disclosure review separately, not folded into a routine release.

1. **`src/furqan_lint/runner.py`** — dispatch surface that calls the four Python checkers in defined order. Equivalent to Bayyinah's `application/scan_service.py`.
2. **`src/furqan_lint/additive.py`** — the additive-only public-surface checker. Python-substrate patent-claim core.
3. **`src/furqan_lint/return_none.py`** + **`src/furqan_lint/zero_return.py`** — the two Python-native checkers closing Phase 1 Gap 1 and the D24-R3 ring close.
4. **`src/furqan_lint/gate11/verification.py`** — Sigstore-CASM Gate 11 verification dispatch (Route a1-via-args canonical dispatch consolidated in v0.12.0 F22).

**Release gate:** `diff -q` against the previous release's byte-image of each surface returns empty. Empty or release is held.

---

## 3. Three-Line Substrate Probe (Mandatory Every Release)

Frozen at v0.13.1; checked at every subsequent release:

```python
furqan_lint.__version__ == pyproject_version
furqan_lint.__all__ == ("__version__",)               # additive-only floor
len(_CHECKER_REGISTRY) == N_BASELINE                   # N frozen at v0.13.1
GATE11_LANGUAGE_DISPATCH == ("python", "rust", "go", "onnx")
```

The `_CHECKER_REGISTRY` does not exist yet. Creating it is the first v0.13.1 task: freeze a `_CHECKER_REGISTRY: tuple[CheckerDescriptor, ...]` in `src/furqan_lint/_registry.py` whose ordering and shape become the patent-invariant claim surface.

**N_BASELINE proposed default: 6** (D24, D11, R3, return_none_mismatch, additive-surface, gate11-verification-dispatch). Resolved in §11.2 with audit-time override slot.

---

## 4. Multi-Locus Sync Map (Mandatory Enforcement)

| Surface | Mirror obligation | Enforcement |
| --- | --- | --- |
| `pyproject.toml [project] version` | `src/furqan_lint/__init__.py:__version__` | Already enforced by `tests/test_version_sync.py` |
| `pyproject.toml [project.optional-dependencies] *` | `requirements-dev.txt` | **NEW in v0.13.1:** add `tests/test_requirements_dev_sync.py` |
| CHANGELOG-claimed `### Added` paths | Actual file existence | **NEW in v0.13.1:** add a structural test that walks `### Added` lines and asserts each cited path exists |
| Gate11 language tuple | Three sites: `Manifest.from_dict` (manifest_schema.py:186), `Verifier.step2_3_check_version_and_language` (verification.py:157), F22 dispatch tuple | **NEW in v0.13.1:** add a fourth invariant check that all three are identical |
| `_CHECKER_REGISTRY` count | The substrate probe | **NEW in v0.13.1:** part of the substrate probe |

---

## 5. Documented Flake Protocol

Every furqan-lint release MUST document its known flakes in `KNOWN_LIMITS.md` with explicit retry protocol. Candidates pre-v0.13.1:

1. Sigstore TUF root fetching (network).
2. tree-sitter language pack version drift (Rust, Go).
3. ONNX runtime vs numpy reference (the `tests/test_onnx_numpy_reference.py` collection failure surfaced in the v0.12.0 probe is a numpy-presence issue, not strictly a flake; the divergence-test class under `src/furqan_lint/onnx_adapter/numpy_divergence.py` is the v0.13.1 ONNX-gate flake locus).
4. `go vet` exit code drift across Go toolchain minor versions.

Each gets a one-paragraph entry in KNOWN_LIMITS.md (a doc this repo does not yet have; create at v0.13.1).

---

## 6. Cumulative-Bundle Patch + Push-Clone Delta Discipline

Operational discipline that made the Bayyinah arc session-paceable. Every cowork-authored patch in the commercialization arc:

1. Applies cleanly against a **pristine floor** (`v0.12.0+5 c5c3c4c` for v0.13.1).
2. Authors the cumulative patch from the pristine floor, NOT from current HEAD.
3. Agent side: apply patch to pristine, diff against fresh clone of current main, push the delta (not the cumulative).
4. Patent-invariant byte-identity check runs on the four surfaces before push.
5. Substrate probe runs before push.
6. Full pytest runs before push; documented flakes retried per protocol.

Failure to follow this discipline (e.g. authoring the patch from current HEAD) breaks the pristine-floor reproducibility and is itself treated as a release-gate failure.

---

## 7. Tag-Claim Resolution for Unmerged Branches

**Resolved (canonical, audit-time override permitted):** Option A throughout. Merge each unmerged branch first; cut the commercialization-arc release as a patch release on top. This preserves the existing surah anchors and treats the unmerged branches as already-completed work that just needs landing rather than as work to be re-done.

Commercialization arc shape:

- v0.12.x + merge `v0.13.0-an-naziat-v16` + cut **v0.13.1** (contract floor)
- v0.13.1 + merge `v0.14.0-tasdiq-al-bayan-v11` + cut **v0.14.1** (budget controller)
- v0.14.1 + cut **v0.15.0** (cross-substrate correlation policy)
- v0.15.0 + cut **v0.16.0** (differential testing matrix)
- v0.16.0 + cut **v0.17.0** (framework-free principles)
- v0.17.0 + merge `v1.0.0-al-basirah-v11` + compose **v1.0.0** (al-Basirah self-attestation + recursive-self-lint gate)
- v1.0.0 + cut **v1.0.1** (first calibration corrective)

Seven releases total, mirroring the Bayyinah arc shape exactly.

---

## 8. Falsification Criteria (Per Version)

Each version's principle remains falsifiable. v2.0 criteria preserved verbatim:

- **v0.13.1 falsification (Bismillah/contract floor).** If `_CHECKER_REGISTRY` freeze does not catch at least one multi-locus sync drift across v0.14.0 → v1.0.1, the registry-as-invariant claim adds no engineering value. (Bayyinah caught three such drifts in five releases; furqan-lint should hit one.)
- **v0.14.1 falsification (Tanzil/budget controller).** If no whole-repo lint pass in v0.15.0 → v1.0.1 window ever clamps with `lint_incomplete=True`, the budget controller is theoretical scaffolding.
- **v0.15.0 falsification (Ring/cross-substrate policy).** If no substrate divergence is recorded between Python, Rust, Go, and ONNX gate11 verification on the same logical surface across the v0.16.0 → v1.0.1 window, the cross-substrate policy is empty documentation.
- **v0.16.0 falsification (Zahir-Batin/differential testing).** If no Python checker and its external reference (ruff/pylint/mypy/semgrep) ever disagree on the same fixture across v0.17.0 → v1.0.1 window, the differential matrix has no anti-drift signal.
- **v0.17.0 falsification (root architecture/framework-free principles).** If `docs/principles.md` produces no externally-consumable citation, audit reference, or compliance reading across the v1.0.0 release cycle, the parallel-entry-point claim has not landed.
- **v1.0.0 falsification (al-Fatiha/recursive self-verification).** If the recursive self-lint gate produces zero findings on furqan-lint's own source on its first run, EITHER the gate is too lenient (coverage must broaden before v1.0.0 ships) OR the source is uncommonly clean (shipping is correct). v1.0.1 resolves the ambiguity.
- **v1.0.1 falsification (first corrective).** If v1.0.0 gate catches nothing and v1.0.1 ships without absorbing a real false-positive, the entire commercialization arc has shipped features that passed their synthetic tests but caught nothing in the wild — the v5 strategy's Step 5 orientation check failure. v1.1.x scope must reduce to producing real defect catches in real codebases before any further principle-tagged work proceeds.

---

## 9. What This Strategy Does Not Specify (Cow Episode Discipline)

- **Does not specify the v5 strategy's v3.0 audit ledger schema in the v0.13.x contract floor.** Audit ledger lands at v1.2.x+.
- **Does not specify Phase 1-4 disclosure UI in the v0.14.x budget controller.** Suggestion-engine work is v1.1.x+.
- **Does not commit to a fifth substrate beyond ONNX.** Gate11 language tuple remains `(python, rust, go, onnx)` through the commercialization arc.
- **Does not extend the `__all__` public surface beyond `("__version__",)`.** Additive evolution stays additive; the public surface stays minimal.
- **Does not commit to independent reimplementations as a release-gate property.** Multi-implementation parity is long-horizon research, not commercialization deliverable. Own-source recursive self-verification (v1.0.0) IS the commercialization signal.

---

## 10. Pace Acknowledgement and Honest Scoping

- **The seven-principle taxonomy is the load-bearing claim.** Preserved verbatim from v5. Strategy-level corrigenda event if it ever needs to change.
- **Per-version feature lists are best-current-judgment.** They will evolve. The arc shape (contract floor → budget → policy → differential → framework-free → recursive-gate → first corrective) is the empirical Bayyinah-arc shape; deviations are permitted but must be justified against substrate.
- **Calibrated timeline is in cowork sessions, not calendar years.** Bayyinah's commercialization arc shipped in one session. furqan-lint's commercialization arc is estimated at 7-10 sessions per the "agent estimates are 75% inflated" discipline. Calendar time is determined by session cadence.
- **The al-Fatiha principle lands at v1.0.0, not v5.0.** Per Bayyinah empirical: own-source recursive self-verification IS the commercialization signal. Multi-implementation reference parity is a long-horizon research extension.
- **AI-assistance disclosure preserved.** Claude (Anthropic Opus 4.6/4.7) is the analytical synthesizer; ChatGPT (OpenAI), Perplexity (Kimi), and Grok (xAI) are cross-vendor audit surfaces; the human author retains full responsibility for all claims and dispositions.
- **Patent-claim scope unchanged.** Patent counsel reviews any version's feature set against filed and forthcoming provisional and non-provisional claims before that version is publicly described in patent-claim-relevant terms.

---

## 11. Resolved Open Decisions (Audit-Time Override Permitted)

v2.0 §8 routed four decisions to the user. v3.0 resolves each as a proposed default with explicit audit-time override slot:

### 11.1 Tag-claim option

**Proposed default:** Option A (merge each unmerged branch first; cut commercialization release as patch on top).

**Rationale:** Preserves existing surah anchors; lower semver-confusion cost; treats unmerged branches as already-completed work that needs landing.

**Audit-time override:** If auditors prefer Option B (orphan unmerged branches and re-cut), explicit override here. Override requires re-mapping v0.13.x → v1.0.x sequence to fresh tags.

### 11.2 `_CHECKER_REGISTRY` baseline count `N_BASELINE`

**Proposed default:** **N_BASELINE = 6.** Components:

1. D24 (Python — return-path discipline)
2. D11 (Python — additive-only diff check)
3. R3 (Python — zero-return ring-close / MARAD zero_return_path)
4. return_none_mismatch (Python)
5. additive-surface (Python — the `__all__` public-surface invariant)
6. gate11-verification-dispatch (cross-substrate Python/Rust/Go/ONNX)

**Audit concern to surface:** Items 1-4 are AST-walking checkers operating on Python source. Item 5 is a module-level public-surface invariant (different shape — operates on module state, not AST). Item 6 is a cross-substrate dispatch (different shape again — orchestrates per-language verifiers). All three shapes are valid `CheckerDescriptor` entries, but the audit must confirm the descriptor schema can carry all three uniformly. If not, N_BASELINE may need to be 4 (Python AST checkers only) with the additive-surface invariant and gate11 dispatch tracked separately.

**Audit-time override slot:** N_BASELINE = ___ (auditor fills in).

### 11.3 `.ax-sh.yaml` schema v1

**Proposed default:** Ship the v5 strategy §2.1 draft schema as-is at v0.13.1:

```yaml
schema_version: 1
framework: ax-sh
framework_version: "1.0"
optimization:
  - serve_truth_over_falsehood
  - catch_surface_substrate_divergence_in_production_code
  - reduce_caller_side_undischarged_R_may
observer_model: external_caller
context_set:
  language: python
  python_version: ">=3.10"
  hot_path: false
  safety_critical: false
correspondence: behavioral_refinement
r_may:
  - ok
  - error_with_diagnostic
  - incomplete_with_provenance
  - timeout
projection_family:
  - source_code
  - api_documentation
  - sbom
  - test_suite
consistency_relation: signature_agreement
overrides:
  "src/critical_path/*":
    hot_path: true
    safety_critical: true
```

**Audit concern to surface:** v5 schema was authored before the Bayyinah-arc empirical disciplines existed. The schema should probably also carry `byte_identity_surfaces` (list of file paths that must stay byte-identical) and `substrate_probe` (the three-line check). This pushes schema v1 to be a v2.0-aware schema, not a pure v5 schema.

**Audit-time override slot:** Schema v1 final spec = (auditor reviews and signs off on draft above, or proposes revisions).

### 11.4 v1.0.0 composition

**Proposed default:** Compose the existing unmerged `v1.0.0-al-basirah-v11` branch (G12.0 self-attestation crypto-anchor + canonical mushaf chain closing) with the recursive-self-lint structural gate, treating al-Basirah as the commercialization signal.

**Rationale:** Both deliverables are al-Fatiha-principle instances at different layers — the crypto-anchor is the supply-chain layer, the recursive-self-lint is the source-tree layer. Together they form a single signal.

**Audit concern to surface:** The al-Basirah branch was authored before the recursive-self-lint gate concept crystallized. Auditors must verify the compose does not break either deliverable's existing semantics.

**Audit-time override slot:** If auditors prefer to keep al-Basirah's existing meaning unchanged and ship the recursive-self-lint gate as a separate v1.1.0, that is the alternative. (If chosen, the commercialization arc becomes 8 releases instead of 7.)

---

## 12. Audit Protocol

This section specifies what cross-vendor auditors check, what constitutes audit-pass, and how findings are dispositioned.

### 12.1 Audit panel composition

Per the dissertation §11.3 trust-gradient discipline and the Bayyinah-arc three-model architecture:

- **Producer:** Claude (Anthropic Opus 4.6/4.7), as the analytical synthesizer of this strategy document.
- **Cross-vendor audit surface:** at minimum two of {ChatGPT (OpenAI), Perplexity (Kimi K2.6), Grok (xAI), Gemini (Google)}. Independent fresh-instance sessions; no continuity-mode context; no prior exposure to this strategy.
- **Final arbiter:** Bilal Syed Arfeen, project lead. Final disposition authority.

Producer-correlated review (Claude reviewing Claude) does NOT bind; it is recorded but flagged as same-vendor and discounted under §11.3.

### 12.2 What auditors check

Each cross-vendor auditor receives:

1. This document (canonical strategy v3.0).
2. The substrate floor (`main` HEAD SHA `c5c3c4c` of furqan-lint).
3. The v0.12.0 CHANGELOG and the four unmerged branch tag-messages.
4. The v2.0 predecessor strategy document (for delta context).
5. The Fatiha Construct (`The_Fatiha_Construct.docx`).
6. The Structured Revelation paper.

Auditors are instructed to verify:

- **A1. Substrate accuracy.** Does the `main` HEAD SHA match? Does the baseline pytest count match? Do the four unmerged branch tags exist?
- **A2. Principle-to-version mapping.** Does each tag's principle anchor (Bismillah, Tanzil, Ring, Zahir-Batin, root architecture, al-Fatiha) correspond to a substantive feature, not decorative labeling? Is the principle's load-bearing feature the dominant deliverable of that release, not a side-effect?
- **A3. Byte-identity surface coverage.** Are the four named patent-invariant surfaces sufficient to cover the patent-claim core, or are there additional surfaces that should be added?
- **A4. Substrate probe completeness.** Is the four-line probe sufficient to catch the failure modes the Bayyinah arc caught? Are there additional probe lines needed for furqan-lint specifically?
- **A5. Sync map enforcement.** Are the five mirror obligations (version, requirements-dev, CHANGELOG paths, gate11 language tuple, registry count) sufficient? Are there additional sync points the Bayyinah arc did not test for that furqan-lint should?
- **A6. Falsification criterion specificity.** Per version, is the falsification criterion sufficiently specific that it can be checked at the named window? Is the window itself well-defined?
- **A7. Cow Episode discipline.** Does §9 omit anything that should be there, or include anything that violates the discipline?
- **A8. Open decisions resolution.** For each of §11.1-11.4, are the proposed defaults defensible? Are the audit concerns surfaced sufficient?
- **A9. Risk register completeness (§15).** Are there risks the producer missed?
- **A10. Audit protocol self-application.** Does this section (§12) describe an audit protocol the producer could actually pass? Producer must not specify an unfalsifiable audit.

### 12.3 Audit findings format

Each cross-vendor auditor produces a structured response in the six-element findings format from the Bayyinah Audit Framework:

```
Finding ID: AUDIT-{vendor}-{check}-{n}
Severity: CRITICAL | HIGH | MEDIUM | LOW
Location: §{n}, ¶ or table cell
Claim: (what the strategy claims)
Evidence: (auditor's substrate check or reasoning)
Impact: (what fails if claim is wrong)
Recommendation: (accept | reject | revise)
```

### 12.4 Audit-pass criteria

The strategy passes audit when ALL of the following hold:

- **AP1.** At least two non-Claude vendors return audit findings.
- **AP2.** No CRITICAL findings remain unresolved.
- **AP3.** All HIGH findings are either resolved or explicitly accepted by the final arbiter with rationale.
- **AP4.** Per §11.1-11.4, every open decision either has its proposed default confirmed or has its override populated.
- **AP5.** The producer (Claude) has reviewed all cross-vendor findings and posted dispositions (accept-and-fix / defer / decline-with-justification) for each.
- **AP6.** The final arbiter has signed off in §16.

### 12.5 Audit failure dispositions

If audit cannot bind in one cycle:

- **Light revisions** (MEDIUM/LOW findings only): producer applies fixes, re-circulates for one verification pass, audit closes.
- **Substantive revisions** (HIGH findings requiring re-architecture): strategy returns to draft as v3.1, full audit cycle re-runs.
- **CRITICAL findings**: strategy returns to v2.0 baseline; v3.0 retracted; the audit cycle failure is itself recorded as a structural-honesty empirical instance.

---

## 13. Pre-Execution Gate

No v0.13.1 code is cut until ALL of the following are true:

- **G1.** Audit-pass per §12.4 achieved.
- **G2.** Final arbiter sign-off recorded in §16.
- **G3.** First cowork prompt drafted per §17 and itself audited (one cross-vendor sweep, lighter than strategy audit).
- **G4.** Pristine floor confirmed: `git fetch origin && git log --oneline main | head -1` reports `c5c3c4c` (or whatever floor the audit confirms).
- **G5.** Substrate-state delta acknowledged: if the substrate has moved since strategy authoring (June 23, 2026), the delta is reviewed and either incorporated or explicitly held as out-of-scope.
- **G6.** Patent counsel briefing acknowledged: counsel has reviewed the byte-identity surface list (§2) and confirmed it does not under-cover or over-cover the patent claim perimeter.

Once all six gates are satisfied, execution begins at the first cowork prompt per §17.

---

## 14. Binding-Claims Index

Every checkable assertion this strategy makes, indexed for audit verification. Each claim is either CONFIRMED at strategy authoring time, ASSERTED for future verification, or ROUTED to audit.

| ID | Claim | Status | Verification |
| --- | --- | --- | --- |
| C1 | `main` HEAD SHA is `c5c3c4c` | CONFIRMED (v2.0) | `git log -1 main \| head -1` |
| C2 | Baseline pytest is 500 passed / 68 skipped at fresh install | CONFIRMED (v2.0) | `pip install -e . && pytest` |
| C3 | Unmerged tags exist: `v0.13.0-an-naziat-v16`, `v0.14.0-tasdiq-al-bayan-v11`, `v1.0.0-al-basirah-v11` | CONFIRMED (v2.0) | `git tag -l 'v0.13.0*' 'v0.14.0*' 'v1.0.0*'` |
| C4 | Four patent-invariant surfaces named in §2 are the complete set | ASSERTED | Counsel review (G6); cross-vendor audit (A3) |
| C5 | N_BASELINE = 6 is the correct registry baseline | ROUTED to audit (§11.2) | Auditor verification of descriptor schema |
| C6 | `.ax-sh.yaml` schema v1 (§11.3) is sufficient | ROUTED to audit (§11.3) | Auditor sign-off or revision |
| C7 | Option A (merge-then-patch) is the right tag-claim resolution | ROUTED to audit (§11.1) | Auditor sign-off or override |
| C8 | v1.0.0 composes al-Basirah + recursive-self-lint | ROUTED to audit (§11.4) | Auditor verification of compose semantics |
| C9 | Bayyinah arc shipped 7 releases (v1.5.0 → v2.0.1) in one cowork session | CONFIRMED (v2.0) | Bayyinah git log inspection |
| C10 | Each principle's load-bearing feature dominates its release | ASSERTED | Cross-vendor audit (A2) |
| C11 | Cow Episode discipline is honored (§9 list is comprehensive) | ASSERTED | Cross-vendor audit (A7) |
| C12 | Falsification criteria per version are checkable at named windows | ASSERTED | Cross-vendor audit (A6) |
| C13 | Audit protocol (§12) is itself falsifiable (can produce a failing outcome) | ASSERTED | Self-application check (A10) |
| C14 | All checker shapes (AST-walker, module-state, cross-substrate dispatch) fit one `CheckerDescriptor` schema | ROUTED to audit (§11.2 concern) | Auditor schema review |
| C15 | The five operational disciplines (byte-identity, substrate probe, sync map, flake protocol, cumulative-bundle/push-clone) are sufficient | ASSERTED | Cross-vendor audit (A4, A5) |

Auditors are encouraged to add C16+ entries for any binding claim they identify that the producer did not index.

---

## 15. Risk Register

What could fail during execution, with mitigations. Risks are scored on severity (impact if realized) and likelihood.

| ID | Risk | Severity | Likelihood | Mitigation |
| --- | --- | --- | --- | --- |
| R1 | The four unmerged branches do not cleanly merge into `main` due to substrate drift since their authoring | HIGH | MEDIUM | Per-branch merge dry-run before §13 G4; if conflicts, address before audit closes |
| R2 | `N_BASELINE = 6` proves wrong post-execution; descriptor schema cannot uniformly carry all six shapes | HIGH | MEDIUM-HIGH | Audit-time review (§11.2); revise N during v0.13.1 authoring if schema constraint emerges |
| R3 | Byte-identity surface list (§2) under-covers the patent-claim core; a routine release accidentally mutates an undeclared patent surface | CRITICAL | LOW | Counsel review (G6); auditors check (A3); periodic counsel re-review at v0.16.0 mid-arc |
| R4 | Cowork session pacing assumption (7-10 sessions for full arc) proves too aggressive; the arc takes 15-20 sessions | MEDIUM | MEDIUM | Maliki Yawm ad-Din discipline: if any version's session count exceeds 2x estimate, reduce scope rather than extend horizon |
| R5 | The recursive self-lint gate at v1.0.0 returns zero findings on first run; falsification criterion §8 leaves ambiguity | MEDIUM | MEDIUM | v1.0.1 absorbs a real false positive; if v1.0.1 ships clean too, return to v1.1.x with explicit "find real defects" mission |
| R6 | A cross-vendor auditor produces a CRITICAL finding the producer did not anticipate | MEDIUM | MEDIUM | §12.5 dispositions; strategy retracts to v2.0 baseline; failure itself is recorded as empirical |
| R7 | The Bayyinah arc empirical (seven releases in one cowork session) does not generalize to furqan-lint due to substrate differences (gate11 cryptographic complexity, four-language coverage) | MEDIUM | MEDIUM-HIGH | First two releases (v0.13.1, v0.14.1) function as empirical calibration; if their session-count exceeds 2 each, recalibrate the §1 timeline and rescope downstream |
| R8 | Patent counsel review (G6) introduces material constraints that require strategy revision | MEDIUM | MEDIUM | Audit cycle accommodates one round-trip with counsel; if more required, strategy returns to v3.1 |
| R9 | Substrate drift during the audit cycle itself (someone pushes to main while audit is open) | LOW-MEDIUM | LOW | Producer locks reference to `c5c3c4c`; if main moves, substrate-state delta acknowledgment (G5) handles |
| R10 | The Fatiha Construct's falsification criteria (F2, F3) prove against this strategy after v1.0.1 — replacing Quranic verse anchors with generic labels produces equivalent outcomes | LOW (for this strategy) | UNKNOWN | Recorded as a future research question, not a blocker. The methodology paper's F2/F3 falsification is the methodology paper's burden, not this strategy's. |

Auditors are encouraged to add R11+ entries for any risk they identify that the producer did not surface.

---

## 16. Final Arbiter Sign-Off Slot

The strategy passes the §13 G2 gate when the final arbiter (Bilal Syed Arfeen) signs the following:

```
I have reviewed the canonical strategy v3.0 (this document), the cross-
vendor audit findings, the producer's dispositions, the resolved open
decisions in §11, and the binding-claims index in §14. I confirm that:

[ ] The substrate floor is correctly anchored at c5c3c4c.
[ ] Option A (tag-claim resolution) is binding, OR override in §11.1 is set.
[ ] N_BASELINE is set to ___ (number).
[ ] The .ax-sh.yaml schema v1 is binding as drafted, OR revisions in §11.3 are
    incorporated.
[ ] The v1.0.0 composition decision (al-Basirah + recursive-self-lint, or
    separate) is set per §11.4.
[ ] All CRITICAL and HIGH audit findings are resolved or explicitly accepted.
[ ] Patent counsel has reviewed the byte-identity surface list (§2).
[ ] Execution may begin at the first cowork prompt per §17.

Signed: ________________________
Date: __________________________
Strategy version executed against: v3.0 (or v3.x with audit-cycle revisions)
```

---

## 17. The First Cowork Prompt to Author (Template)

The next deliverable after this strategy passes audit is the **v0.13.1 cowork prompt**. Shape:

- **§1 substrate state.** Cite `main` HEAD SHA (`c5c3c4c`), baseline pytest count (500/68), the four patent-invariant surfaces.
- **§2 deliverables.**
  - `tests/contracts/__init__.py` + the contract test files (`test_checker_registry_shape.py`, `test_diagnostic_shape.py`, `test_lint_incomplete_clamp.py`)
  - `tests/test_requirements_dev_sync.py`
  - `tests/test_changelog_added_paths_exist.py`
  - `tests/test_gate11_language_tuple_invariant.py`
  - `KNOWN_LIMITS.md` first cut (four flake candidates per §5)
  - `src/furqan_lint/_registry.py` (the `_CHECKER_REGISTRY` freeze at N=___ per §11.2)
  - `.ax-sh.yaml` schema v1 (per §11.3)
- **§3 test inventory.** Claimed test-count delta with arithmetic shown.
- **§4 patent-invariant byte-identity assertion.** The four surfaces stay byte-identical to v0.12.0.
- **§5 release-gate checklist.** Pristine apply + push-clone diff + invariant probes + full pytest + flake retry.
- **§6 commit message template.** The Bayyinah-arc-burnt-in format.

Authored against the floor `v0.12.0+5 c5c3c4c` (Option A confirmed).

The cowork prompt itself goes through a lighter audit cycle (one cross-vendor sweep) before §13 G3 is satisfied and execution begins.

---

## 18. Closing

The v5 strategy's spine remains: the Quran's structural architecture, independent of theological content, encodes engineering principles for communicating complex multi-phase instructions to AI systems. The v2.0 strategy correctly substrate-anchored the v5 spine to the actual current floor and added the five Bayyinah-arc operational disciplines that v5 lacked. The v3.0 canonical strategy (this document) preserves both v5's principle taxonomy and v2.0's operational disciplines verbatim, and adds the four audit-readiness layers (audit protocol §12, pre-execution gate §13, binding-claims index §14, risk register §15) that v2.0 left implicit.

The strategy is now ready for cross-vendor audit. Once audit binds per §12.4 and the final arbiter signs §16, the first cowork prompt is authored per §17 and execution begins.

The most important orientation check remains the one v5 and v2.0 both name: at every release boundary, ask whether the version's added features detected real surface-substrate divergence in real codebases, or whether they only passed their own synthetic test suite. v1.0.1 of furqan-lint IS that orientation check, by design.

The strategy is the instrument. The discriminator is the audit panel and the final arbiter together. Neither replaces the other.

Begin the audit.

*Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.*
*La hawla wa la quwwata illa billah.*

---

# Bismillah ir-Rahman ir-Rahim
