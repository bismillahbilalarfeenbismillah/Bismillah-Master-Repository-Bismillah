# Bismillah ir-Rahman ir-Rahim

# R0513 -- furqan-lint Coding Strategy v2.0

**Chronological Index:** 253 of 995  
**Date:** 2026-05-27  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** furqan_lint_coding_strategy_v2_0.md  
**Source Format:** md  
**SHA-256:** `130c3d265ea9f3c06d4ac06b76463c0210804b7693f53abd5f261a48d9473d60`  

---

## R0513 · furqan-lint Coding Strategy v2.0

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: furqan_lint_coding_strategy_v2_0.md
- source_format: md
- text_sha256: 130c3d265ea9f3c06d4ac06b76463c0210804b7693f53abd5f261a48d9473d60

# furqan-lint Coding Strategy v2.0

Bismillah ar-Rahman ar-Rahim

Successor to the v5 strategy authored 2026-05-27 (file:
`furqan_lint_v5_Strategy.pdf`). v2.0 keeps the v5 strategy's principle
taxonomy intact (the seven Structured-Revelation principles remain the
load-bearing version-feature mapping; the Fatiha Construct remains
the session protocol) and revises three things only:

1. The **substrate floor** -- v5 wrote against `v0.8.5`; main has
   shipped to `v0.12.0+5 c5c3c4c` with unmerged `v0.13.0` / `v0.14.0` /
   `v1.0.0` branches already pre-figuring v3-v4 strategy work.
2. The **calibrated timeline** -- v5's "approximately 5-6 years to v5.0"
   was authored before the Bayyinah commercialization arc (v1.5.0 ->
   v2.0.1 shipped in one cowork session). The new timeline runs in
   cowork-session units, not calendar years.
3. The **v1.0 commercialization signal** -- v5 schedules recursive
   self-verification at year 5 (v5.0/al-Fatiha). The Bayyinah arc just
   demonstrated that the recursive self-verification gate IS the
   commercialization signal and ships in a single major-release jump.
   v2.0 of this strategy ships it at v1.0, not v5.0.

Author: Bilal Syed Arfeen
Document Date: June 23, 2026

---

## Opening -- the seven steps applied to this revision

**Step 1 -- Bismillah.** Building: a substrate-anchored, session-paced
revision of the furqan-lint coding strategy. Authority source: (a) the
v5 strategy's seven-principle taxonomy and Fatiha Construct protocol
(carried forward intact); (b) the empirical pacing and discipline of
the Bayyinah commercialization arc that shipped between v5's authoring
date and now. Optimization function: serve the truth-over-falsehood
hierarchy by anchoring the strategy to substrate reality rather than
to outdated date-of-writing assumptions. Scope: timeline calibration
and v1.0 signal definition; out of scope: changes to the
version-to-principle mapping.

**Step 2 -- Alhamdulillah.** Current state as of c5c3c4c (`main` HEAD,
2026-06 era, 5 commits past `v0.12.0`):

- furqan-lint main HEAD is **v0.12.0+5 c5c3c4c** (al-Mursalat / Phase
  G11.2 Go Sigstore-CASM extension). The v5 strategy's stated floor
  (`v0.8.5`) is **6 minor versions stale**.
- Unmerged but tagged: `v0.13.0` (an-Naziat / G11.3 ONNX Sigstore-CASM
  extension), `v0.14.0` (Tasdiq al-Bayan / G11.4 cross-substrate
  verification corpus), `v1.0.0` (al-Basirah / G12.0 self-attestation
  / canonical mushaf chain closing). Three months of substrate work
  on unmerged branches.
- Baseline pytest at main HEAD: 500 passed / 68 skipped on fresh
  install (393 collected without optional extras; 642 was the v0.12.0
  CHANGELOG inventory with all extras populated).
- Public checker surface: D24, D11, R3, return_none_mismatch for
  Python live; Rust (G11.1) and Go (G11.2) gate11 verification
  pipelines; ONNX (G11.3) on unmerged branch.
- Bayyinah scanner is at **v2.0.1** (not v1.0 as v5 stated). The
  recursive self-verification gate landed at Bayyinah v2.0.0 and the
  first calibration corrective at v2.0.1. The session-pace empirical:
  Bayyinah v1.5.0 through v2.0.1 (seven releases) shipped in **one
  cowork session**. v5's "12 months between major versions" was a
  pre-session estimate calibrated to solo-developer pace.

**Step 3 -- Ar-Rahman ar-Rahim.** MDL discipline: this revision keeps
everything from v5 that holds and revises only what substrate has
disproved. The seven-principle taxonomy is preserved verbatim; the
Cow Episode anti-pattern guard is preserved; the falsification
criteria per version are preserved with timeline windows recalibrated.
What changes is small: floor anchor, timeline units, v1.0 signal
definition, and the addition of patent-invariant byte-identity
discipline (the Bayyinah-arc empirical finding).

**Step 4 -- Maliki Yawm ad-Din.** Time horizon -- recalibrated.
v5 stated 5-6 calendar years; the new unit is **cowork sessions**,
not calendar months. One cowork session in the Bayyinah pattern
shipped seven releases v1.5.0 -> v2.0.1. The new estimate, deflated
by user's "agent estimates are 75% inflated" discipline: v0.13.x
through v2.0.1 commercialization tier in **~7-10 cowork sessions**.
Calendar-time depends entirely on session cadence; not the binding
unit.

**Step 5 -- Iyyaka Na'budu.** Orientation check at the strategy
boundary: am I writing the strategy as if I am bound by the original
v5 timeline (which would be performance), or am I writing it as if
bound by what the substrate just demonstrated about session-pace
shipping (which is substrate-honest)? The substrate just produced
seven Bayyinah releases in a session; the strategy must reflect that
or it ships a false claim about its own pacing.

**Step 6 -- Ihdina as-Sirat al-Mustaqim.** Sequence: revise the
floor, revise the timeline, redefine v1.0's signal, add patent-
invariant byte-identity discipline. Do not touch the seven-principle
mapping; do not touch the Fatiha Construct protocol; do not touch
the falsification criteria's spirit.

**Step 7 -- Sirat Alladhina An'amta 'Alayhim.** What worked
empirically (per Bayyinah commercialization arc): cumulative-bundle
patches from a pristine floor, push-clone delta extraction, patent-
invariant byte-identity check as a release gate, three-line substrate
probes per release, documented flake protocol, multi-locus sync
verification. What failed empirically: calendar-time horizons that
do not account for session-pace shipping; commercialization-signal
definitions that require external author groups instead of own-source
recursive self-application.

Begin.

---

## 1. The strategy in compressed form (revised)

Six release tags, each governed by one of the v5 strategy's principles
(taxonomy unchanged), shipped in cowork-session pace. Two cross-cutting
principles (root architecture, disease model) operate at every layer.

| Tag | Principle | Load-bearing feature | Bayyinah analogue |
| --- | --- | --- | --- |
| **v0.13.0** | Principle 1 (Bismillah/initialization) -- declared scope | Contract-floor: `_CHECKER_REGISTRY` freeze + `tests/contracts/` directory + KNOWN_LIMITS.md + requirements-dev sync test + the v5 strategy's `.ax-sh.yaml` manifest schema | v1.5.0 muwazana_score + scan_incomplete_clamp contract floor |
| **v0.14.0** | Principle 2 (Tanzil/phased delivery) -- run-budget controller | Whole-repo lint budget with graceful stop, `lint_incomplete=True` honest reporting, deterministic-truncation ordering. The v5 strategy's "Phase 1-4 disclosure UI" arrives in a later release; v0.14.0 ships the budget primitive first (Cow Episode discipline: do not specify Phase-1-4 UI in the v0.14.0 manifest schema). | v1.6.0 budget controller |
| **v0.15.0** | Principle 3 (Ring composition) -- cross-substrate correlation policy | When the same logical surface exists in Python live + Rust gate11 + Go gate11 + ONNX gate11 and the substrates disagree, the published policy resolves which wins, when both fire, and when both are silenced. This is ring-composition at the **substrate layer**, not yet at the v5-strategy ledger layer. The audit-ledger work from v5's v3.0 lands later as v0.18.0+. | v1.7.0 cross-modal correlation policy |
| **v0.16.0** | Principle 5 (Zahir/Batin) -- differential testing matrix | Each Python checker cross-checked against an independent reference (D24 vs. ruff RET503; D11 vs. mypy strict; R3 vs. pylint R1710; additive vs. semgrep; gate11 Python vs. sigstore CLI). Cross-substrate: tree-sitter vs. cargo-check vs. go-vet on the same fixture corpus. Disagreement is a test failure. | v1.8.0 differential testing matrix |
| **v0.17.0** | Principle 4 (root architecture, surfaced) -- framework-free principles doc | `docs/principles.md` -- five engineering principles in vocabulary that holds without Furqan, Bayyinah Audit Framework, Munafiq Protocol, or Quranic anchors. README stays framework-anchored; principles.md is the parallel entry-point for security review, regulated-industry compliance, academic citation. | v1.9.0 framework-free principles |
| **v1.0.0** | Principle 6 (al-Fatiha/recursive self-verification) -- the commercialization signal | furqan-lint runs ALL its checkers against ITS OWN source tree on every CI run. Zero diagnostics required for any release in the commercialization tier. `_PENDING_CALIBRATION_FILES` pending-discipline forces promotion when a file starts scanning clean. **This is the al-Fatiha principle, but at the own-source-recursive layer (Bayyinah-arc empirical), not at the multi-implementation reference-parity layer (v5 original).** | v2.0.0 recursive self-verification gate |
| **v1.0.1** | (post-commercialization first corrective) | Whatever the v1.0.0 gate catches first. Round-12-style calibration corrective; substrate-conservative. | v2.0.1 file-router calibration corrective |

The v5 strategy's v3.0 (audit ledger / cross-PR ring composition), v4.0
(multi-observer / projection consistency expansion), and v5.0 (multi-
implementation reference parity / Chapter 21 falsification tools as
runnable) are deferred to **post-v1.0.1** and do not need to be
specified now per the Cow Episode discipline. Their principle slots
remain claimed -- the principle-to-version map below extends.

Post-commercialization extension (Cow Episode permitting):

- **v1.1.x range** -- v5 strategy's v2.0 phased-disclosure suggestion
  engine (Phase 1-4 UI).
- **v1.2.x range** -- v5 strategy's v3.0 audit ledger / cross-PR
  coherence.
- **v1.3.x range** -- v5 strategy's v4.0 multi-observer / projection
  consistency.
- **v2.0** of furqan-lint (the SDK, not this strategy doc) -- v5's
  v5.0 reference-parity, **gated on whether independent
  reimplementations actually materialize by then**. The Bayyinah
  arc demonstrated that the commercialization signal does NOT require
  external reimplementations -- it requires own-source recursive
  self-verification, which v1.0.0 already delivers.

Cross-cutting principles operating at every layer (carried verbatim
from v5 strategy §7):

- **Principle 4: Lossless Compression Through Root Architecture.**
  The framework's vocabulary (zahir, batin, muwazana, bayyinah, mizan,
  tanzil, bismillah, fatiha) is the root system. Each technical term
  carries its full operational meaning through its root. Naming
  discipline maintained across all versions in a NAMING.md analog.
- **Principle 7: The Disease Model as Debugging Philosophy.** Every
  version treats failing modules as diseased components requiring
  diagnosis-treatment-verification, not betraying agents requiring
  rewrite-from-scratch.

---

## 2. Bayyinah-arc empirical discipline added (new in v2.0 of strategy)

The v5 strategy specified principles and falsification criteria but
did not specify a release-gate discipline. The Bayyinah arc shipped
seven releases through five disciplines that v2.0 of this strategy
makes mandatory for every furqan-lint release in the commercialization
tier.

### 2.1 Patent-invariant byte-identity discipline

Four surfaces in furqan-lint MUST stay byte-identical across the
v0.13.0 -> v1.0.1 commercialization arc. Any mutation to any of
these is flagged as a patent-substrate change and routed through
patent-disclosure review separately, not folded into a routine release.

1. **`src/furqan_lint/runner.py`** -- dispatch surface that calls the
   four Python checkers in defined order. Equivalent to Bayyinah's
   `application/scan_service.py`.
2. **`src/furqan_lint/additive.py`** -- the additive-only public-
   surface checker. This is the Python-substrate patent-claim core.
3. **`src/furqan_lint/return_none.py`** + **`src/furqan_lint/zero_return.py`**
   -- the two Python-native checkers that close Phase 1 Gap 1 and
   the D24-R3 ring close.
4. **`src/furqan_lint/gate11/verification.py`** -- the Sigstore-CASM
   Gate 11 verification dispatch (the Route a1-via-args canonical
   dispatch consolidated in v0.12.0 F22).

Release gate: `diff -q` against the previous release's byte-image
of each surface returns empty. Empty or release is held.

### 2.2 Three-line substrate probe (mandatory every release)

Bayyinah's analogue:
```python
bayyinah.__version__ == pyproject_version
len(MECHANISM_REGISTRY) == 159
TIER['tounicode_anomaly'] == 2
```

furqan-lint substrate probe (to be frozen at v0.13.0):
```python
furqan_lint.__version__ == pyproject_version
furqan_lint.__all__ == ("__version__",)               # additive-only floor
len(_CHECKER_REGISTRY) == N_BASELINE                  # freeze N at v0.13.0
GATE11_LANGUAGE_DISPATCH == ("python", "rust", "go", "onnx")
```

The `_CHECKER_REGISTRY` does not exist yet. Creating it is the first
v0.13.0 task: freeze a `_CHECKER_REGISTRY: tuple[CheckerDescriptor, ...]`
in `src/furqan_lint/_registry.py` whose ordering and shape become the
patent-invariant claim surface. Every subsequent contract test pins
against the registry.

### 2.3 Multi-locus sync map (mandatory enforcement)

The Bayyinah arc caught multi-locus sync gaps in v1.3.0, v1.4.0, and
v1.8.0 -- a recurring pattern that justifies enforced sync tests.

| Surface | Mirror obligation | Enforcement |
| --- | --- | --- |
| `pyproject.toml [project] version` | `src/furqan_lint/__init__.py:__version__` | Already enforced by `tests/test_version_sync.py` |
| `pyproject.toml [project.optional-dependencies] *` | `requirements-dev.txt` | **NEW in v0.13.0:** add `tests/test_requirements_dev_sync.py` |
| CHANGELOG-claimed `### Added` paths | Actual file existence | **NEW in v0.13.0:** add a structural test that walks `### Added` lines and asserts each cited path exists |
| Gate11 language tuple | Three sites: `Manifest.from_dict` (manifest_schema.py:186), `Verifier.step2_3_check_version_and_language` (verification.py:157), F22 dispatch tuple | **NEW in v0.13.0:** add a fourth invariant check that all three are identical |
| `_CHECKER_REGISTRY` count | The substrate probe | **NEW in v0.13.0:** part of the substrate probe |

### 2.4 Documented flake protocol

Bayyinah's documented flake: `test_corpus_round_trip_byte_stable_on_pdftex_fixtures`
(pdfTeX timestamp embedding; passes pristine, drifts on clone). Every
furqan-lint release MUST document its known flakes in `KNOWN_LIMITS.md`
with explicit retry protocol. Candidates pre-v0.13.0:

1. Sigstore TUF root fetching (network).
2. tree-sitter language pack version drift (Rust, Go).
3. ONNX runtime vs. numpy reference (the
   `tests/test_onnx_numpy_reference.py` collection failure that
   surfaced in my v0.12.0 probe is a numpy-presence issue, not
   strictly a flake -- but the divergence-test class under
   `src/furqan_lint/onnx_adapter/numpy_divergence.py` is the
   v0.13.0 ONNX-gate flake locus).
4. `go vet` exit code drift across Go toolchain minor versions.

Each gets a one-paragraph entry in KNOWN_LIMITS.md (a doc this repo
does not yet have; create at v0.13.0).

### 2.5 Cumulative-bundle patch discipline + push-clone delta

This is the operational discipline that made the Bayyinah arc
session-paceable. Every cowork-authored patch in the commercialization
arc:

1. Applies cleanly against a **pristine floor** (`v0.12.0+5 c5c3c4c`).
2. Author the cumulative patch from the pristine floor, not from
   current HEAD.
3. On the agent side: apply patch to pristine, diff against fresh
   clone of current main, push the delta (not the cumulative).
4. Patent-invariant byte-identity check runs on the four surfaces
   before push.
5. Substrate probe runs before push.
6. Full pytest runs before push; documented flakes retried per
   protocol.

Failure to follow this discipline (e.g. authoring the patch from
current HEAD) breaks the pristine-floor reproducibility and is itself
treated as a release-gate failure.

---

## 3. Tag-claim question for v0.13.0

The existing `v0.13.0` tag on an unmerged branch ships G11.3 ONNX
Sigstore-CASM. Two options:

- **Option A (preferred).** Merge `v0.13.0-an-naziat-v16` to main,
  then cut **v0.13.1** as the contract-floor release. ONNX work
  carries forward as intended; the commercialization arc starts at
  v0.13.1. This preserves the existing tag's semantic claim
  (an-Naziat / G11.3 ONNX) and adds the contract floor as the first
  patch release on top.
- **Option B.** Orphan the unmerged `v0.13.0`, `v0.14.0`, `v1.0.0`
  branches and re-cut. Higher semver-confusion cost; loses the
  existing tag-claim-to-surah-anchor mapping.

Same question recurs at v0.14.0 (Tasdiq al-Bayan / cross-substrate
verification corpus, also unmerged) and v1.0.0 (al-Basirah / G12.0
self-attestation, also unmerged).

**Strategy v2.0 recommendation:** Option A throughout. Merge each
unmerged branch first; cut the commercialization-arc release as a
patch release on top. This preserves the existing surah anchors and
treats the unmerged branches as already-completed work that just
needs landing rather than as work to be re-done.

This makes the commercialization arc:
- v0.12.x + merge v0.13.0 + cut **v0.13.1** (contract floor)
- v0.13.1 + merge v0.14.0 + cut **v0.14.1** (budget controller)
- v0.14.1 + cut **v0.15.0** (cross-substrate correlation policy)
- v0.15.0 + cut **v0.16.0** (differential testing matrix)
- v0.16.0 + cut **v0.17.0** (framework-free principles)
- v0.17.0 + merge v1.0.0 + compose **v1.0.0 as the commercialization
  signal** -- the al-Basirah self-attestation crypto-anchor + the
  recursive-self-lint structural gate together
- v1.0.0 + cut **v1.0.1** (first calibration corrective)

Seven releases total, mirroring the Bayyinah arc shape exactly.

---

## 4. Falsification criteria (preserved from v5, recalibrated windows)

Each version's principle remains falsifiable. The v5 falsification
criteria are preserved; only the measurement windows recalibrate.

- **v0.13.1 falsification (Bismillah/contract floor).** If the
  `_CHECKER_REGISTRY` freeze does not catch at least one multi-locus
  sync drift across the v0.14.0 -> v1.0.1 arc, the registry-as-
  invariant claim adds no engineering value and the v0.14.0+
  releases should freeze checkers ad-hoc instead. (Bayyinah caught
  three such drifts in five releases; furqan-lint should hit one.)
- **v0.14.1 falsification (Tanzil/budget controller).** If no whole-
  repo lint pass in the v0.15.0 -> v1.0.1 window ever clamps with
  `lint_incomplete=True`, the budget controller is theoretical
  scaffolding and v0.15.0+ releases should remove it.
- **v0.15.0 falsification (Ring/cross-substrate policy).** If no
  substrate divergence is recorded between Python, Rust, Go, and
  ONNX gate11 verification on the same logical surface across the
  v0.16.0 -> v1.0.1 window, the cross-substrate policy is empty
  documentation and v0.16.0+ releases should treat substrates as
  independent.
- **v0.16.0 falsification (Zahir-Batin/differential testing).** If
  no Python checker and its external reference (ruff/pylint/mypy/
  semgrep) ever disagree on the same fixture across the v0.17.0 ->
  v1.0.1 window, the differential matrix has no anti-drift signal
  and should be removed.
- **v0.17.0 falsification (root architecture/framework-free
  principles).** If `docs/principles.md` produces no externally-
  consumable citation, audit reference, or compliance reading
  across the v1.0.0 release cycle, the parallel-entry-point claim
  has not landed and the doc should fold back into README.
- **v1.0.0 falsification (al-Fatiha/recursive self-verification).**
  If the recursive self-lint gate produces zero findings on furqan-
  lint's own source on its first run, EITHER the gate is too lenient
  to catch real shape (in which case the gate's checker coverage
  must broaden before v1.0.0 ships) OR the source is uncommonly
  clean (in which case shipping is correct). Either way, v1.0.1
  resolves the ambiguity: v1.0.1 SHOULD correct a real false-positive
  the way Bayyinah v2.0.1 did, otherwise the gate is performance
  rather than discipline.
- **v1.0.1 falsification (first corrective).** If the v1.0.0 gate
  catches nothing and v1.0.1 ships without absorbing a real
  false-positive, the entire commercialization arc has shipped
  features that passed their synthetic tests but caught nothing in
  the wild -- the v5 strategy's Step 5 orientation check failure.
  In that case, v1.1.x scope must reduce to producing real defect
  catches in real codebases before any further principle-tagged
  work proceeds.

---

## 5. What this strategy does not specify (Cow Episode discipline)

Following the v5 strategy's §7 Cow Episode warning verbatim:

- **Does not specify the v5 strategy's v3.0 audit ledger schema in
  the v0.13.x contract floor.** Audit ledger lands at v1.2.x+ at
  earliest, after the commercialization arc closes.
- **Does not specify Phase 1-4 disclosure UI in the v0.14.x budget
  controller.** Suggestion-engine work is v1.1.x+ after
  commercialization.
- **Does not commit to a fifth substrate beyond ONNX.** Gate11
  language tuple remains `(python, rust, go, onnx)` through the
  commercialization arc.
- **Does not extend the `__all__` public surface beyond
  `("__version__",)`.** Additive evolution stays additive; the public
  surface stays minimal.
- **Does not commit to independent reimplementations as a
  release-gate property.** The v5 strategy's v5.0 multi-
  implementation parity is a long-horizon research goal, not a
  commercialization-arc deliverable. Own-source recursive
  self-verification (v1.0.0) IS the commercialization signal,
  empirically validated by the Bayyinah arc.

---

## 6. Pace acknowledgement and honest scoping

Per the v5 strategy's §9 honest acknowledgments, recalibrated:

- **The seven-principle taxonomy is the load-bearing claim.** That
  claim is preserved verbatim from v5. If the principle taxonomy
  ever needs to change, that is a strategy-level corrigenda event
  requiring v3.0 of this strategy doc.
- **Per-version feature lists are best-current-judgment.** They
  will evolve. The arc shape (contract floor -> budget -> policy ->
  differential -> framework-free -> recursive-gate -> first
  corrective) is the empirical Bayyinah-arc shape; deviations are
  permitted but must be justified against substrate.
- **Calibrated timeline is in cowork sessions, not calendar years.**
  Bayyinah's commercialization arc shipped in one session. furqan-
  lint's commercialization arc is estimated at 7-10 sessions per
  the user's "agent estimates are 75% inflated" discipline. Calendar
  time is determined by session cadence; this strategy does not
  predict cadence.
- **The al-Fatiha principle lands at v1.0.0, not v5.0.** Per Bayyinah
  empirical: own-source recursive self-verification IS the
  commercialization signal. Multi-implementation reference parity is
  a long-horizon research extension, not the commercialization gate.
- **AI-assistance disclosure preserved verbatim from v5 §9.** Claude
  is the analytical synthesizer; Perplexity (current session) is
  one cross-vendor audit surface; the human author retains full
  responsibility for all claims and dispositions.
- **Patent-claim scope unchanged from v5.** Patent counsel reviews
  any version's feature set against filed and forthcoming
  provisional and non-provisional claims before that version is
  publicly described in patent-claim-relevant terms.

---

## 7. The first cowork prompt to author

The next deliverable after this strategy lands is the **v0.13.1 cowork
prompt** (assuming Option A; if Option B is chosen, v0.13.0). Shape:

- **§1 substrate state.** Cite `main` HEAD SHA (`c5c3c4c`), baseline
  pytest count (500/68), the four patent-invariant surfaces.
- **§2 deliverables.**
  - `tests/contracts/__init__.py` + the contract test files
    (`test_checker_registry_shape.py`, `test_diagnostic_shape.py`,
    `test_lint_incomplete_clamp.py`)
  - `tests/test_requirements_dev_sync.py`
  - `tests/test_changelog_added_paths_exist.py`
  - `tests/test_gate11_language_tuple_invariant.py`
  - `KNOWN_LIMITS.md` first cut (four flake candidates)
  - `src/furqan_lint/_registry.py` (the `_CHECKER_REGISTRY` freeze)
  - `.ax-sh.yaml` schema v1 (carried from v5 strategy §2.1)
- **§3 test inventory.** Claimed test-count delta with arithmetic
  shown.
- **§4 patent-invariant byte-identity assertion.** The four surfaces
  stay byte-identical to v0.12.0.
- **§5 release-gate checklist.** Pristine apply + push-clone diff +
  invariant probes + full pytest + flake retry.
- **§6 commit message template.** The Bayyinah-arc-burnt-in format.

Authored against the floor `v0.12.0+5 c5c3c4c` (Option A) or against
whatever new floor Option B produces.

---

## 8. Open decisions for the user

Before the v0.13.1 cowork prompt is authored:

1. **Option A vs Option B for the unmerged tags.** v2.0 of this
   strategy recommends Option A. User can override.
2. **`_CHECKER_REGISTRY` baseline count `N`.** Frozen at v0.13.1
   first ship. My read of the substrate: four Python checkers
   (D24, D11, R3, return_none_mismatch) + the additive surface
   + the gate11 verification dispatch = six entries. User should
   confirm before the freeze.
3. **The `.ax-sh.yaml` schema v1.** v5 strategy §2.1 specifies a
   draft. v0.13.1 can ship it as-specified, or refine.
4. **v1.0.0 composition.** v5 strategy reserves v1.0.0 for the
   Bismillah manifest layer; v2.0 of this strategy proposes
   composing the existing unmerged `v1.0.0-al-basirah-v11` branch
   (G12.0 self-attestation crypto-anchor) with the recursive-self-
   lint structural gate, treating al-Basirah as the commercialization
   signal. If the user prefers to keep al-Basirah's existing
   meaning unchanged and ship the recursive-self-lint gate as a
   separate `v1.1.0`, that is the alternative.

---

## 9. Closing

The v5 strategy's spine remains: the Quran's structural architecture,
independent of theological content, encodes engineering principles for
communicating complex multi-phase instructions to AI systems. Bayyinah
demonstrated this in 22 phases over three weeks; the Bayyinah
commercialization arc demonstrated it in seven releases in one cowork
session; furqan-lint's commercialization arc demonstrates it in seven
releases at session pace, anchored against the substrate as it stands
today and not against the substrate floor the v5 strategy assumed.

The v5 commitment to ship the Chapter 21 falsification protocols as
runnable tools at v5.0 is preserved as long-horizon research goal,
not as commercialization-arc gate.

The most important orientation check is the same one v5 strategy §10
prescribed: at every release boundary, ask whether the version's
added features detected real surface-substrate divergence in real
codebases, or whether they only passed their own synthetic test
suite. v1.0.1 of furqan-lint IS that orientation check, by design.

Begin.

Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.
La hawla wa la quwwata illa billah.

---

# Bismillah ir-Rahman ir-Rahim
