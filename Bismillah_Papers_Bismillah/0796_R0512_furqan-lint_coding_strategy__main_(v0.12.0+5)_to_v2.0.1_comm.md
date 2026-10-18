# Bismillah ir-Rahman ir-Rahim

# R0512 -- furqan-lint coding strategy: main (v0.12.0+5) to v2.0.1 commercialization tier

**Chronological Index:** 796 of 995  
**Date:** Undated  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** furqan_lint_coding_strategy_to_v2_0.md  
**Source Format:** md  
**SHA-256:** `046acdeddf992273efb729d9e841a8177edfe93ebc81879a7b6cb35d12dcb969`  

---

## R0512 · furqan-lint coding strategy: main (v0.12.0+5) to v2.0.1 commercialization tier

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: furqan_lint_coding_strategy_to_v2_0.md
- source_format: md
- text_sha256: 046acdeddf992273efb729d9e841a8177edfe93ebc81879a7b6cb35d12dcb969

# furqan-lint coding strategy: main (v0.12.0+5) to v2.0.1 commercialization tier

Mirror of `bayyinah_v1_2_4_to_v2_0_cowork_executable_strategy.md` applied
to the furqan-lint substrate. The Bayyinah commercialization arc shipped
v1.5.0 - v2.0.1 in a single session by holding four disciplines constant:
patent-invariant byte-identity, multi-locus contract pinning, structural
self-defense via a recursive gate, and Round-12-style calibration
correctives forced by the gate. This document translates each into
furqan-lint shape.

## Calibrated time

Per user discipline: agent-stated time estimates are inflated 75%. All
phase windows below are stated as "calibrated workdays" (already
deflated). Each phase below is one release tag.

## 0. Where the substrate is

- `main` HEAD: `c5c3c4c`, 5 commits past tag `v0.12.0` (al-Mursalat,
  Phase G11.2 Go Sigstore-CASM extension).
- Tag-only branches (not merged to main): `v0.13.0-an-naziat-v16`
  (G11.3 ONNX), `v0.14.0-tasdiq-al-bayan-v11` (G11.4 cross-substrate
  verification corpus), `v1.0.0-al-basirah-v11` (G12.0 self-attestation
  / canonical mushaf chain closing).
- Baseline pytest at `main` HEAD: 500 passed / 68 skipped on a fresh
  install with optional gate11 extras present. Two collection failures
  (numpy, sigstore in my probe env) are environmental, not substrate.
- Test count delta v0.11.8 -> v0.12.0 per CHANGELOG: +24 (618 -> 642
  by the v0.12.0 §3 inventory; my fresh env collects 393 because the
  optional-extras-gated sigstore / numpy / ONNX tests are skipped).
- Public checker surface (as of v0.12.0): four structural checks across
  three substrates (Python live; Rust under G11.1; Go under G11.2). The
  Python checks are D24 (all-paths-return), D11 (status-coverage with
  Optional and Result-aware producers), R3 (zero-return-path), and
  return_none_mismatch. Rust and Go pipelines run the analogous
  surface-extraction + signature-canonicalization + verification through
  Sigstore-CASM Gate 11.
- ONNX adapter exists but its gate11 extension is on the unmerged
  v0.13.0 branch.

## 1. Bayyinah pattern -> furqan-lint mapping

Five Bayyinah commercialization tier moves and their furqan-lint
analogues. Each is one release tag.

| Bayyinah move | Bayyinah file shape | furqan-lint analogue | Target tag |
| --- | --- | --- | --- |
| v1.5.0 muwazana_score contract + scan_incomplete_clamp contract | `tests/contracts/test_muwazana_score_shape.py`, `tests/contracts/test_scan_incomplete_clamp.py` | Diagnostic-shape contract: every checker returns a `(rule_code, location, severity, message, status_complete)` tuple with documented properties + status_complete invariant | v0.13.0 (claim the existing an-Naziat tag for it; rename if needed) |
| v1.6.0 budget controller | `application/budget_controller.py` + 18 contract tests | Run-budget controller for whole-repo lint: total node-walk budget per substrate, graceful stop with `lint_incomplete=True`, per-checker time and memory ceilings, deterministic-truncation ordering | v0.14.0 |
| v1.7.0 cross-modal correlation policy | `docs/cross_modal.md` + 17 contract tests | Cross-substrate correlation policy: when Python, Rust, and Go pipelines disagree on the same logical surface (e.g. a Python module + its Rust extension + its Go fallback exposing the same public name), document which substrate wins, when both fire, and when both are silenced | v0.15.0 |
| v1.8.0 differential testing matrix | `tests/differential/` + `pdfid` external reference | Differential testing matrix: each Python checker cross-checked against an independent linter that overlaps on the same shape (ruff or pylint for R3-shaped checks, mypy for return_none_mismatch, semgrep for additive-only patterns). Cross-substrate: tree-sitter parse vs. cargo-check vs. go-vet on the same fixture corpus. Disagreement is a test failure. | v0.16.0 |
| v1.9.0 framework-free principles | `docs/principles.md` (52 -> 330 lines) | Framework-free engineering principles doc: state the five furqan-lint engineering claims in vocabulary that holds without Furqan, Bayyinah Audit Framework, Munafiq Protocol, or Quranic anchors. README stays framework-anchored; principles.md is the parallel entry-point for security review, regulated-industry compliance, academic citation. | v0.17.0 |
| v2.0.0 recursive self-verification gate | `tests/recursive_self_verification/test_self_scan.py` (66 tests; scans Bayyinah's own release docs clean) | Recursive self-lint gate: furqan-lint runs ALL its checkers (D24 + D11 + R3 + return_none_mismatch + additive + gate11 Python-substrate verification) against ITS OWN source tree (`src/furqan_lint/`) on every CI run. Zero diagnostics required for any release tag in the commercialization tier. Pending-calibration discipline tracks known false-positives the same way Bayyinah's `_PENDING_CALIBRATION_DOCS` does. | v1.0.0 (claim the existing al-Basirah tag for it; this is the commercialization signal) |
| v2.0.1 first calibration corrective | `infrastructure/file_router.py` extension-guard for `.md` vs CSV mis-routing | First Round-12-style corrective triggered by the v1.0.0 self-lint gate. Whatever false-positive the gate finds first (and it WILL find one -- the v1.0.0 al-Basirah branch's test corpus will surface it; my prior is something in the `_exceptions.py` modules or one of the gate11 facade modules) gets a minimal scoped corrective | v1.0.1 |

The Bayyinah arc was seven tags (v1.5.0 through v2.0.1). The furqan-lint
arc is seven tags (v0.13.0 through v1.0.1). The number is not magic;
the discipline is.

## 2. Patent-invariant surface for furqan-lint

Bayyinah's patent-invariant set is four surfaces that MUST stay
byte-identical across the commercialization arc:
`application/scan_service.py`, `domain/value_objects.py`,
`domain/config.py`, `analyzers/`.

The furqan-lint patent-invariant set, by analogy:

1. **`src/furqan_lint/runner.py`** -- the dispatch surface that calls
   the four Python checkers in defined order. Equivalent to
   `scan_service.py`. No mutation through the commercialization arc;
   only the data structure it returns may extend additively.
2. **`src/furqan_lint/additive.py`** -- the additive-only surface
   checker. This IS the patent claim's core for the Python substrate
   (additive discipline is the contract). Byte-identical.
3. **`src/furqan_lint/return_none.py`** + **`src/furqan_lint/zero_return.py`**
   -- the two Python-native checkers that close Phase 1 Gap 1 and the
   D24-R3 ring close. Byte-identical.
4. **`src/furqan_lint/gate11/verification.py`** -- the
   Sigstore-CASM Gate 11 verification dispatch (Route a1-via-args).
   Per the v0.12.0 F22 dispatch consolidation, this is the canonical
   single-entry verification surface across Python, Rust, Go (and ONNX
   under the unmerged v0.13.0 branch). Byte-identical.

Mutations to these four through v0.13.0 -> v1.0.1 must be flagged in
the cowork prompt as patent-substrate changes and routed through
patent-disclosure review separately. The commercialization arc is
substrate-conservative by design.

## 3. Required invariant probes for every release

The Bayyinah three-line probe is:

```python
bayyinah.__version__ == pyproject_version
len(MECHANISM_REGISTRY) == 159
TIER['tounicode_anomaly'] == 2
```

The furqan-lint analogue:

```python
furqan_lint.__version__ == pyproject_version
furqan_lint.__all__ == ("__version__",)  # additive-only floor
len(_CHECKER_REGISTRY) == N_BASELINE      # define N at v0.13.0 freeze
GATE11_LANGUAGE_DISPATCH == ("python", "rust", "go")  # extend at G11.3
```

`_CHECKER_REGISTRY` does not yet exist as a single registry the way
Bayyinah's `MECHANISM_REGISTRY` does. Creating it is a v0.13.0 task:
freeze a `_CHECKER_REGISTRY: tuple[CheckerDescriptor, ...]` in
`src/furqan_lint/_registry.py` whose ordering and shape become the
patent-invariant claim surface. This unblocks every subsequent contract
test (every contract pins against the registry).

## 4. Multi-locus update map

The "version-bump goes here, mirror goes there" map the Bayyinah arc
caught repeatedly. furqan-lint version:

| Surface | Mirror obligation |
| --- | --- |
| `pyproject.toml [project] version` | `src/furqan_lint/__init__.py:__version__` (currently the only version-sync test, `tests/test_version_sync.py`, already enforces this) |
| `pyproject.toml [project.optional-dependencies] *` | `requirements-dev.txt` (NOT YET ENFORCED; v0.13.0 task: add `tests/test_requirements_dev_sync.py` mirroring Bayyinah's) |
| CHANGELOG-claimed test count delta | actual `pytest --collect-only` delta (Bayyinah caught two prose-vs-substrate gaps this way; v0.12.0 CHANGELOG already cites "drift -2 within al-Hujurat T05 CHANGELOG-math" so the discipline is partially in place) |
| Gate11 language tuple | three sites per v0.12.0 CHANGELOG: `Manifest.from_dict` (manifest_schema.py:186), `Verifier.step2_3_check_version_and_language` (verification.py:157), and the F22 dispatch tuple. Add a fourth invariant check that all three are identical. |
| New release doc claimed in CHANGELOG | doc actually exists (Bayyinah missed `tests/contracts/__init__.py` repeatedly; add a structural test that walks CHANGELOG `### Added` sections and asserts each claimed path exists) |

## 5. Pre-existing flaky baselines to document

Bayyinah's documented flake: `test_corpus_round_trip_byte_stable_on_pdftex_fixtures`
(pdfTeX timestamp embedding; passes pristine, drifts on clone).

furqan-lint analogues to identify before v0.13.0 ships:

1. Any test that depends on Sigstore identity TUF root fetching (network).
2. Any tree-sitter language pack version-pinned test (tree-sitter-rust,
   tree-sitter-go may drift between system installs).
3. Any ONNX runtime check that compares against numpy reference (the
   `test_onnx_numpy_reference.py` collection failure in my probe is
   a numpy-presence issue, not a flake; but the divergence test class
   under `src/furqan_lint/onnx_adapter/numpy_divergence.py` is the
   v0.13.0 ONNX gate's likely flake locus).
4. Any go-test fixture that depends on `go vet` exit codes (Go toolchain
   minor versions can shift advisory behavior).

Each gets a one-paragraph entry in `KNOWN_LIMITS.md` (a doc this repo
does not yet have but Bayyinah does; create at v0.13.0 alongside the
contract tests).

## 6. Release-by-release intent

### v0.13.0 (claim the existing an-Naziat tag, OR cut fresh)

The existing v0.13.0 tag ships G11.3 ONNX. Two options:

- **Option A (preferred): merge v0.13.0-an-naziat-v16 to main, then
  cut v0.13.1 as the contract-floor release.** Carry ONNX forward as
  intended; the commercialization arc starts at v0.13.1.
- **Option B: orphan the unmerged branches and re-cut.** Higher
  semver-confusion cost.

Either way, the contract-floor release adds:

- `tests/contracts/__init__.py`
- `tests/contracts/test_checker_registry_shape.py` (registry tuple
  shape, ordering, completeness)
- `tests/contracts/test_diagnostic_shape.py` (every checker returns
  the documented diagnostic tuple)
- `tests/contracts/test_lint_incomplete_clamp.py` (when a checker is
  budget-clamped, the diagnostic carries `status_complete=False` and
  the overall lint result clamps accordingly)
- `tests/test_requirements_dev_sync.py`
- `KNOWN_LIMITS.md` first cut (the four flake candidates above)
- `src/furqan_lint/_registry.py` (the `_CHECKER_REGISTRY` freeze)

Patent-invariant byte-identity required: `runner.py`, `additive.py`,
`return_none.py`, `zero_return.py`, `gate11/verification.py`.

### v0.14.0 (claim al-Tasdiq al-Bayan tag, OR cut fresh)

Run-budget controller. The cross-substrate verification corpus on the
existing v0.14.0 branch is orthogonal and can be merged in alongside;
the commercialization arc requires the budget controller specifically.

Adds `src/furqan_lint/budget_controller.py` modeled on Bayyinah's
`application/budget_controller.py`. Whole-repo lint gets a node-walk
budget (default ~50M AST nodes per substrate), graceful stop with
`lint_incomplete=True` on the result, deterministic truncation ordering
(alphabetical file path, then checker order from `_CHECKER_REGISTRY`).

Contract tests: ~18 new in `tests/contracts/test_budget_controller.py`
covering ceiling enforcement, clamp propagation, truncation determinism,
and the "graceful stop is honest" property (a clamped run reports its
own clampedness).

### v0.15.0 cross-substrate correlation policy

`docs/cross_substrate_policy.md` (analogue of `docs/cross_modal.md`)
+ ~17 contract tests. The policy answers: when the same logical surface
exists in Python (live) and the Rust extension (G11.1) and the Go
fallback (G11.2), and the three pipelines disagree, what wins. The
Bayyinah analogue answers the same question for analyzers; here it's
substrates.

Likely policy shape (write the doc first; do not pre-decide here):

- If Python lint passes and Rust gate11 verification fails: substrate-
  divergence error, surface both.
- If two substrates agree clean and one fires: pending-calibration
  status the same way recursive self-lint will (v1.0.0) handle
  `_PENDING_CALIBRATION_DOCS`.
- If all three substrates fire on the same shape: composite finding
  with `correlation=true` flag.

### v0.16.0 differential testing matrix

`tests/differential/` directory. Each Python checker gets a witness
contract against an independent reference:

- D24 + R3 vs. `ruff` rule `RET503` and `pylint` `R1710`.
- return_none_mismatch vs. `mypy --strict` "Incompatible return value
  type" findings.
- additive vs. `pyupgrade` + `semgrep` rules.
- gate11 Python-substrate verification vs. `sigstore-python verify`
  CLI direct.

Cross-substrate: every fixture in `tests/fixtures/` that exists for
both Python and Rust gets a parametrize-cross test that asserts the
two substrates' diagnostic emissions are isomorphic up to the
documented language-binding differences.

Disagreement is a test failure. False-positive correction is a
calibration corrective (Round-12 discipline imported from Bayyinah).

### v0.17.0 framework-free principles

`docs/principles.md`. Five engineering principles in language that
holds without Furqan vocabulary or Quranic anchors. README stays
framework-anchored as the canonical entry-point; principles.md is
the parallel entry-point.

Candidate principles (refine in drafting):

1. Additive-only public-surface discipline. Removing a public name
   fires; adding one is silent. Renames must be declared.
2. Honest incompleteness reporting. Every checker that stops short
   reports `status_complete=False`; the overall lint result clamps.
3. Cross-substrate witness symmetry. The same logical shape lints
   identically across Python, Rust, Go (and ONNX) up to documented
   binding differences.
4. Sigstore-CASM Gate 11 fail-closed. Unknown languages, unsigned
   substrates, and identity-policy violations halt the pipeline.
5. Recursive self-verification. The linter lints its own source under
   its own rules on every CI run. (This principle is forward-pointing
   to v1.0.0.)

Each principle paired with its enforcing test or document.

### v1.0.0 (claim the al-Basirah tag) recursive self-lint gate

`tests/recursive_self_lint/test_self_lint.py`. Mirror of Bayyinah's
`tests/recursive_self_verification/test_self_scan.py`.

Corpus: every `.py` file under `src/furqan_lint/` enumerated explicitly
(no glob; Bayyinah's enumeration-not-glob discipline applies). Every
file must lint clean under D24 + D11 + R3 + return_none_mismatch +
additive checks, with `lint_incomplete=False` and zero diagnostics.

Pending-calibration: `_PENDING_CALIBRATION_FILES` tuple for files with
known false-positives, paired with `TestPendingCalibrationDiagnostic`
that asserts each pending file CURRENTLY fires; when one stops firing,
the diagnostic fails and forces promotion.

This is the commercialization signal. For a buyer, regulator, or
auditor, "furqan-lint passes its own rules on its own source on every
CI run" is the difference between "trust us" and "the tool's own CI
proves it on every commit."

The existing v1.0.0-al-basirah-v11 branch already pre-figures this
under the "G12.0 self-attestation" framing. Compose the two: the
existing branch's self-attestation crypto-anchor + the new recursive-
self-lint structural gate.

### v1.0.1 first calibration corrective

Whatever the v1.0.0 gate catches first. My prior, given the substrate:

- ONNX adapter modules (`numpy_divergence.py`, `score_validity.py`,
  `probe_grid.py`) carry significant numpy-typed surfaces where a
  D11 status-coverage walk may hit a documented incompleteness pattern
  that the upstream furqan checker classifies as a gap.
- Tree-sitter parser modules (`rust_adapter/parser.py`,
  `go_adapter/parser.py`) walk CSTs with `errors="replace"` decoding
  fallbacks. R3 may fire on a defensive branch that returns None
  through an exception handler that does not declare it.

Minimal scoped corrective at the routing or checker-calibration layer;
no patent-invariant mutations.

## 7. Discipline carry-overs from the Bayyinah arc

These are not new; they are the patterns the Bayyinah arc burned in
that furqan-lint must adopt verbatim.

- **Patches are cumulative bundles from a known floor.** Define the
  floor as `v0.12.0+5 main HEAD c5c3c4c`. Every Claude-authored patch
  in the arc applies cleanly against THAT floor; the live-vs-floor
  delta is what gets pushed.
- **Pristine apply, push-clone diff.** Apply the cumulative patch to a
  pristine copy of the floor; diff against a fresh clone of current
  main; that diff is the actual push payload.
- **Patent-invariant byte-identity check is a release gate, not a
  hope.** A `diff -q` of the four patent-invariant surfaces against
  the previous release must return empty for every release in the
  arc.
- **Substrate probes are three lines, not a paragraph.** Version
  parity, registry count, dispatch tuple. If any of the three drifts
  unintentionally, the release is held.
- **Flaky tests are documented, retried, and known by name.** A
  release with an undocumented new flake does not ship.
- **CHANGELOG test-count arithmetic must hold.** Bayyinah's
  CHANGELOG-claimed deltas were verified against `pytest --collect-only`
  output on every release. furqan-lint v0.12.0 CHANGELOG already
  documents a -2 drift against the al-Mursalat prompt projection; the
  discipline is partially in place. Make it mandatory at v0.13.0.

## 8. What this strategy explicitly does not do

- Does not add new Python checkers beyond the four shipped. The
  commercialization arc is substrate-conservative. New checkers are
  the post-v1.0.1 roadmap.
- Does not extend gate11 to a fifth substrate beyond ONNX. ONNX (G11.3)
  arrives via the existing unmerged v0.13.0 branch; the commercialization
  arc rides that substrate but does not extend it.
- Does not change the additive-only public surface of `furqan_lint`
  itself. `__all__` stays `("__version__",)` through the entire arc.
  Any internal symbol surfaces remain underscore-prefixed.
- Does not introduce a new license, attribution discipline, or
  audit-attribution convention. The v0.8.5 attribution-corrective
  convention holds.
- Does not move any of the Bayyinah-only artifacts (Munafiq Protocol
  references, Quranic verse anchors per release) into furqan-lint.
  furqan-lint already has its own Sigstore-CASM-anchored discipline;
  do not double-anchor.

## 9. First cowork prompt to author

The next deliverable after this strategy lands is the v0.13.0 cowork
prompt. Shape:

- §1 substrate state (cite main HEAD SHA, baseline test count, the
  four patent-invariant surfaces).
- §2 deliverables (the `tests/contracts/` directory contents, the
  `_CHECKER_REGISTRY` freeze, `KNOWN_LIMITS.md`, the requirements-dev
  mirror test).
- §3 test inventory (claimed test-count delta with arithmetic).
- §4 patent-invariant byte-identity assertion (the four surfaces stay
  byte-identical).
- §5 release-gate checklist (pristine apply + push-clone diff +
  invariant probes + full pytest).
- §6 commit message template (the same format the Bayyinah arc has
  burned in).

Author the prompt against the floor `v0.12.0+5 c5c3c4c`. Decide
the v0.13.0 / v0.13.1 tag question (Option A vs Option B in §6 above)
before authoring.

---

Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

---

# Bismillah ir-Rahman ir-Rahim
