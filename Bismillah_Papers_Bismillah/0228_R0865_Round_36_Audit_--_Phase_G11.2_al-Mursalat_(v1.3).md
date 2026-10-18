# Bismillah ir-Rahman ir-Rahim

# R0865 -- Round 36 Audit -- Phase G11.2 al-Mursalat (v1.3)

**Chronological Index:** 228 of 995  
**Date:** 2026-05-10  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** round_36_v1_3_audit_for_claude.md  
**Source Format:** md  
**SHA-256:** `209f8b85d3c9ce242b08ef6244124728fc9aa5480d245d085ef1486315955162`  

---

## R0865 · Round 36 Audit -- Phase G11.2 al-Mursalat (v1.3)

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: round_36_v1_3_audit_for_claude.md
- source_format: md
- text_sha256: 209f8b85d3c9ce242b08ef6244124728fc9aa5480d245d085ef1486315955162

# Round 36 Audit -- Phase G11.2 al-Mursalat (v1.3)

**Reviewer:** Perplexity (cross-instance)
**Subject:** al-Mursalat v1.3 prompt at `/home/user/workspace/paste.txt` (1873 lines)
**Substrate baseline:** v0.11.8 shipped 2026-05-10; main `cace1c0`; tag `v0.11.8` -> commit `cac6917`
**Producer (Claude) prior absorption passes:** v1.0 -> v1.1 (Round 31 cross-instance) -> v1.2 (Round 32 cross-instance) -> v1.3 (self-review same-instance per methodology v1.1 §0.1)
**Methodology:** v1.1 §0 (cross-instance discipline), six-element findings, severity uppercase
**Verdict:** **HALT-AND-RETURN-TO-v1.4** (3 CRITICAL, 3 HIGH, 4 MEDIUM, 2 LOW)

---

## Recognition

v1.3 correctly identifies the as-Saff cycle as the architectural prerequisite, cites the actual ship SHAs (`cac6917` / `cace1c0`), preserves the v1.1 / v1.2 absorption ledgers cleanly, and acknowledges the same-instance limitation explicitly in the v1.3 amendments closing note (lines 1852-1865). The narrative reconstruction in the closing audit-chain section is accurate through the v0.11.8 ship. F-AL-3 (test-count baseline shift), F-AL-7 (F22 closure attribution), F-AL-8 (Round 35 finding-seed inheritance), F-AL-9 (pre-registration sources), F-AL-10 (audit-chain narrative) are substrate-true.

The same-instance limitation note in the appendix (lines 1852-1865) explicitly anticipates the failure mode this audit caught: "the as-Saff Round 35 cycle demonstrated that same-instance review can miss substrate-true findings... v1.3's amendments are substrate-evidence-traceable rather than architectural reframings, which reduces but does not eliminate the same-instance miss risk." The prediction proved correct. The findings below are precisely that class: substrate-untrue symbol claims that v1.3 self-review could not catch because it did not consult the actual v0.11.8 substrate.

---

## CRITICAL findings -- substrate-untrue symbol claims at load-bearing T02 / T04 / T05 sites

### F-RM-1 CRITICAL -- `python_verification.verify` and `rust_verification.verify` are NOT public substrate symbols at v0.11.8

- **Severity:** CRITICAL
- **Locus:** F-AL-1 (line 28-32), F-AL-2 (line 36-39), F-AL-4 (line 49-57), T02 `_VERIFIER_DISPATCH` code block (lines 935-964), T02 test fixtures #1, #2 (lines 967-981), T02 prose (lines 905-916), Closing audit-chain narrative (lines 1719-1722), F-AL-1 / F-AL-4 / F-AL-7 appendix entries (lines 1830-1836)
- **Observation:** v1.3 asserts as a substrate fact that as-Saff v0.11.8 provides public `python_verification.verify` and `rust_verification.verify` symbols that al-Mursalat T02 will wire into `_VERIFIER_DISPATCH`. The prompt's T02 code block reads `_VERIFIER_DISPATCH = {"python": python_verification.verify, "rust": rust_verification.verify, "go": go_verification.verify}`.
- **Substrate truth (verified at tag `v0.11.8` / commit `cac6917`):**
  - `src/furqan_lint/gate11/python_verification.py` line 53 defines `def _verify_python(manifest, args)` -- underscore-prefixed, private.
  - `src/furqan_lint/gate11/python_verification.py` line 86 declares `__all__ = ("_verify_python",)` -- only the underscore-prefixed symbol is exported.
  - `src/furqan_lint/gate11/rust_verification.py` line 54 defines `def _verify_rust(manifest, args)` -- underscore-prefixed, private.
  - `src/furqan_lint/gate11/rust_verification.py` line 87 declares `__all__ = ("_verify_rust",)`.
  - There is no public `python_verification.verify` or `rust_verification.verify` symbol anywhere in the v0.11.8 substrate.
- **Why CRITICAL:** This is the F-AS-2-class regression the as-Saff Round 35 cycle was instituted to prevent. The v1.3 self-review codified substrate-nonexistent symbols as load-bearing public API for al-Mursalat to consume; if Co-work implements T02 verbatim, the dispatch table construction will raise `AttributeError` at import time when Python attempts to resolve `python_verification.verify`. The CI lint guard will not catch this (it's a runtime / import-time failure, not a syntactic em-dash). The T02 test fixtures encode the same wrong target and will fail collection.
- **Closure:** v1.4 must reframe T02 to dispatch through the substrate-actual public surface. The architecturally clean choice is to call `verification.verify(manifest, args)` -- the module-level facade that v0.11.8 actually exports (line 556 of `verification.py`, listed in `verification.__all__`). The CLI's `manifest verify` subcommand inspects `manifest.module_identity["language"]`, then routes through `verification.verify(manifest, args)` which internally dispatches to `_verify_python` or `_verify_rust` via its function-local dispatch dict. al-Mursalat's substrate task becomes (a) extending `python_verification`, `rust_verification` to optionally expose public `verify` aliases if the per-language-module symmetrization is desired (separate ADR; not necessary for F22 closure), AND (b) adding `_verify_go` (private) plus `go_verification.py` mirroring the v0.11.8 facade pattern, AND (c) extending `verification.verify`'s function-local dispatch dict to include `"go": _verify_go`. The F-AL-4 framing ("CLI saves one indirection by dispatching to per-language modules directly") is architecturally permissible but requires first introducing the public `python_verification.verify` / `rust_verification.verify` aliases as a separate prerequisite phase or as an explicit task within al-Mursalat (a new T01.5: "extend per-language modules with public verify aliases"). The v1.3 prompt treats those aliases as preexisting; v1.4 must either drop the F-AL-4 symmetrization (route through `verification.verify`) or explicitly introduce the aliases as a new task with its own substrate edits, tests, and acceptance criteria.
- **Reference:** as-Saff v1.2 F-XR-1 reversed an analogous F-AS-2 codification (verification.verify portrayed as preexisting); the v1.3 self-review replicated the same anti-pattern one layer down (per-language-module verify aliases portrayed as preexisting).

### F-RM-2 CRITICAL -- `_LANGUAGE_DISPATCH` is NOT a module-level symbol in v0.11.8 substrate

- **Severity:** CRITICAL
- **Locus:** F-AL-2 (line 39), §0 framing (line 339-341), Calibration rung v0.11.8 (lines 470-471), T00 step 4 expectations (lines 714-716), F-AL-5 appendix entry (line 1834), Closing audit-chain narrative (line 1721-1722)
- **Observation:** v1.3 asserts repeatedly that v0.11.8 substrate provides "module-level `verification.verify(manifest, args)` plus `_LANGUAGE_DISPATCH`" as a paired top-level symbol. T00 step 4's gate11 module inventory expects `_LANGUAGE_DISPATCH` to be inspectable at module-level in `verification.py`.
- **Substrate truth (verified at v0.11.8 / `verification.py` lines 556-612):** `_LANGUAGE_DISPATCH` is a **function-local dict** constructed inside `def verify(manifest, args)` after a lazy import of `_verify_python` and `_verify_rust`. It is NOT a module-level symbol; it cannot be imported, inspected externally, monkeypatched for tests, or extended from outside the function body. The lazy-import-inside-function pattern was chosen specifically to avoid circular imports between `verification.py` and the per-language modules (which import `Verifier` from `verification`).
- **Why CRITICAL:** Multiple v1.3 specifications depend on `_LANGUAGE_DISPATCH` being externally accessible. T00 step 4 will record `_LANGUAGE_DISPATCH PRESENT` as a substrate fact -- which is false. If al-Mursalat T01 attempts to extend `_LANGUAGE_DISPATCH` to include `"go"` by appending at module-load time, it will not find the symbol. If al-Mursalat T02 test fixture #6 (`test_dispatch_does_not_call_unmatched_verifiers`) attempts to mock entries in a module-level `_LANGUAGE_DISPATCH`, the mock target does not exist.
- **Closure:** v1.4 must reframe: extending dispatch to Go means editing the function-local dispatch dict inside `verification.verify()` (adding a third lazy-import line `from furqan_lint.gate11.go_verification import _verify_go` and a third dict entry `"go": _verify_go`). T00 step 4 inventory expectation revised to record the substrate-actual shape (module-level `verify` function; function-local dispatch dict). T02 test fixtures that need to inspect or mock dispatch routing must either patch at the per-language-module level (`_verify_python` etc.) or refactor `verification.verify` to lift the dispatch dict to module level as a separate ADR -- which is a real architectural change with its own acceptance criteria, NOT a substrate-already-true fact al-Mursalat can rely on.
- **Reference:** Substrate read of `src/furqan_lint/gate11/verification.py` lines 556-612 at tag `v0.11.8` / commit `cac6917`.

### F-RM-3 CRITICAL -- T02 / T04 import paths reference non-existent modules

- **Severity:** CRITICAL
- **Locus:** T02 code block (line 940): `from furqan_lint.gate11.errors import CasmVerificationError`. T04 code block (lines 1118-1121): `from furqan_lint.gate11.manifest import Manifest`, `from furqan_lint.gate11.errors import CasmVerificationError`, `from furqan_lint.gate11._policy import _build_identity_policy`. T06 (line 1240): `_build_identity_policy(args)` cross-reference.
- **Observation:** T02 and T04 code blocks declare imports from `furqan_lint.gate11.errors`, `furqan_lint.gate11.manifest`, and `furqan_lint.gate11._policy`.
- **Substrate truth (verified at v0.11.8):**
  - `furqan_lint/gate11/errors.py` does not exist. `CasmVerificationError` is defined at line 52 of `verification.py` and exported via `verification.__all__`.
  - `furqan_lint/gate11/manifest.py` does not exist. The Manifest schema lives at `furqan_lint/gate11/manifest_schema.py`.
  - `furqan_lint/gate11/_policy.py` does not exist. `_build_identity_policy` does not appear anywhere under `src/furqan_lint/gate11/` -- it is referenced in v1.3 prose as a shared helper but is not in the substrate at v0.11.8.
- **Why CRITICAL:** Each of the three imports fails with `ModuleNotFoundError` at module load time if Co-work copies the v1.3 code blocks verbatim. T02's CLI module will fail to import; T04's `go_verification.py` will fail to import; T06's identity-policy parity claim ("shared helper") is structurally unfounded because the helper does not exist.
- **Closure:** v1.4 imports must reference substrate-actual paths:
  - `from furqan_lint.gate11.verification import CasmVerificationError` (or `from furqan_lint.gate11 import verification` with `verification.CasmVerificationError` use)
  - `from furqan_lint.gate11.manifest_schema import Manifest`
  - For `_build_identity_policy`: T00 step 6 (already mandated to extract live API patterns) must include a grep `grep -rn "_build_identity_policy\|build_identity_policy" src/furqan_lint/gate11/` and report the actual location, OR if the helper does not exist substrate-wide, T04 cannot claim "shared helper" parity. al-Mursalat must either introduce the helper as a substrate ADR (separate task, separate acceptance) or duplicate the identity-policy-construction inline in `go_verification.py` matching the in-line construction in `verification.py` / `rust_verification.py`. The "shared helper" architectural premise in T06 is fictional at v0.11.8.
- **Reference:** Substrate read of `src/furqan_lint/gate11/` directory listing and grep for `_build_identity_policy` across `src/`.

---

## HIGH findings -- substrate-mismatch in load-bearing surfaces

### F-RM-4 HIGH -- `manifest.module_identity.language` is attribute access on a dict; substrate uses `.get()` / `["language"]`

- **Severity:** HIGH
- **Locus:** T02 code block (line 951): `language = manifest.module_identity.language`. T04 code block (line 1134, 1137): `manifest.module_identity.language != "go"`, `manifest.module_identity.language!r`.
- **Observation:** T02 and T04 use attribute syntax `manifest.module_identity.language` to read the language field.
- **Substrate truth:** `manifest_schema.py` line 134 declares `module_identity: dict[str, Any]`. The v0.11.8 `verification.verify` body (line 605) reads `language = manifest.module_identity.get("language")` -- dict access. Attribute syntax `manifest.module_identity.language` raises `AttributeError` because `dict` has no `language` attribute.
- **Why HIGH:** Every dispatch test, every Go verifier invocation, every CLI routing call would hit `AttributeError` before reaching its first verification step. F22 closure tests (T02 fixtures #1-#6) all fail. T04 Go verifier raises `AttributeError` on its first line.
- **Closure:** v1.4 reads use `manifest.module_identity["language"]` or `manifest.module_identity.get("language")` mirroring the v0.11.8 substrate convention. F-AL-6's preserved CASM-V-001 semantic test in T02 fixture #4 should also assert the substrate-actual dict-access raising surface.
- **Reference:** `src/furqan_lint/gate11/manifest_schema.py` line 134; `src/furqan_lint/gate11/verification.py` line 605 (`manifest.module_identity.get("language")`).

### F-RM-5 HIGH -- T02 targets `src/furqan_lint/cli.py`; the `manifest verify` subcommand lives in `src/furqan_lint/gate11/cli.py`

- **Severity:** HIGH
- **Locus:** T02 substrate declaration (line 888): "**Substrate**: `src/furqan_lint/cli.py` `manifest verify` subcommand." T02 code block header comment (line 925).
- **Observation:** T02 declares `src/furqan_lint/cli.py` as the substrate for the `manifest verify` subcommand and the home for `_VERIFIER_DISPATCH`.
- **Substrate truth:**
  - `src/furqan_lint/cli.py` is the top-level CLI module handling `check`, `diff`, `version` subcommands (docstring lines 3-11). No `manifest verify` subcommand. No `Verifier` import.
  - `src/furqan_lint/gate11/cli.py` line 286 defines `def cmd_manifest_verify(args)` which IS the `furqan-lint manifest verify` subcommand. Lines 333 and 456 construct `Verifier(trust_config=trust_config)` and call `verifier.verify_bundle(...)` directly. No dispatch dict.
- **Why HIGH:** If Co-work edits `src/furqan_lint/cli.py` per T02's declaration, the `manifest verify` subcommand is unchanged; F22 is not closed. The CI matrix could plausibly turn green if the new tests are scoped to the wrong CLI module (testing dispatch behavior in `cli.py` that has no manifest-verify code path). The bug surface is exactly the kind that surfaces at first real-bundle invocation, not at unit-test time.
- **Closure:** v1.4 T02 substrate declaration: "`src/furqan_lint/gate11/cli.py` `cmd_manifest_verify` function (lines 286-... at v0.11.8; see T00 step 4 record for current line numbers)." T02 code block header comment updated; T02 prose's "the `manifest verify` subcommand" references updated to the actual function name `cmd_manifest_verify`.
- **Reference:** `src/furqan_lint/cli.py` head + `src/furqan_lint/gate11/cli.py` line 286 + grep `verify_bundle\|Verifier\|_DISPATCH` against `src/furqan_lint/gate11/cli.py` (returns 4 matches, none involving a dispatch dict).

### F-RM-6 HIGH -- T05 filename `_pinned_checker_sources_go.py` + symbol `PINNED_CHECKER_SOURCES_GO` repeats the as-Saff F-XR-3 anti-pattern

- **Severity:** HIGH
- **Locus:** T05 substrate (line 1171): `src/furqan_lint/gate11/_pinned_checker_sources_go.py` (new file). T05 implementation pattern (lines 1203-1215): `PINNED_CHECKER_SOURCES_GO: Final[frozenset[str]] = frozenset({...})`. T05 closure (line 1235): "H-6 Go-side parity."
- **Observation:** T05 introduces a new file `_pinned_checker_sources_go.py` containing a separate `PINNED_CHECKER_SOURCES_GO` frozenset, paralleling a presumed `_pinned_checker_sources.py` / `PINNED_CHECKER_SOURCES` Python file.
- **Substrate truth (verified):** v0.11.8 has a SINGLE pinned-sources module: `src/furqan_lint/gate11/checker_set_hash.py` containing `_CHECKER_SOURCE_FILES: tuple[Path, ...]` (a tuple, not a frozenset; a single canonical list, not language-partitioned). The as-Saff F-XR-3 absorption specifically corrected the prior prompt iteration's invented `_pinned_checker_sources.py` / `PINNED_CHECKER_SOURCES` symbol -- those names were Co-work hallucinations that the as-Saff Round 35 cycle reversed. v1.3's T05 reintroduces the exact same hallucinated naming convention for the Go side.
- **Why HIGH:** Co-work implementing T05 verbatim will (a) create a new file `_pinned_checker_sources_go.py` that does not integrate with the substrate's `checker_set_hash.py`, (b) declare a frozenset where the substrate uses a tuple, (c) miss the architecturally correct site (extending `_CHECKER_SOURCE_FILES` tuple in `checker_set_hash.py` to include `go_verification.py` and `go_signature_canonicalization.py`, mirroring how as-Saff T04(b) extended it to include `python_verification.py` and `rust_verification.py`). The Form A checker_set_hash discipline (line 1218) presumes a single canonical hash computation; bifurcating into two pinned lists breaks the single-hash semantic unless explicitly designed (which v1.3 does not do).
- **Closure:** v1.4 T05 substrate: `src/furqan_lint/gate11/checker_set_hash.py` (existing; per as-Saff T04(b)). T05 required change: extend `_CHECKER_SOURCE_FILES: tuple[Path, ...]` to include `_PKG_ROOT / "gate11" / "go_verification.py"` and `_PKG_ROOT / "gate11" / "go_signature_canonicalization.py"` entries (path-join idiom from as-Saff F-XR-3 absorption). Acceptance §13-style "byte-stable diff scope" bullet: `git diff v0.11.8..v0.12.0 -- src/furqan_lint/gate11/checker_set_hash.py` shows exactly the `_CHECKER_SOURCE_FILES` tuple extended with the two new entries.
- **Reference:** as-Saff v1.2 F-XR-3 absorption; substrate read of `src/furqan_lint/gate11/checker_set_hash.py` at v0.11.8.

---

## MEDIUM findings -- prose and acceptance criteria misaligned with substrate truth

### F-RM-7 MEDIUM -- T00 step 4 expected gate11 module inventory does not match substrate

- **Severity:** MEDIUM
- **Locus:** T00 step 4 (lines 708-736).
- **Observation:** T00 step 4 lists expected files at v0.11.8 substrate. The list includes `_LANGUAGE_DISPATCH` as a module-level expectation (line 715-716); the file inventory itself is partially correct but the `_CHECKER_SOURCE_FILES` claim (line 727-730) is structurally correct while the per-language inventory's expected exports are wrong (related to F-RM-1).
- **Substrate truth:** As verified for F-RM-1 / F-RM-2: `verification.py` extended with module-level `verify` (correct); `_LANGUAGE_DISPATCH` is function-local not module-level; `python_verification.py` exports only `_verify_python`; `rust_verification.py` exports only `_verify_rust`; `checker_set_hash.py` has `_CHECKER_SOURCE_FILES` extended with `python_verification.py` and `rust_verification.py` (correct per as-Saff T04(b)).
- **Why MEDIUM:** T00 step 4 is the gate where Co-work would discover the divergence between v1.3's substrate claims and reality. The current wording instructs the implementer to halt-and-escalate if the expected state is not met; a substrate-aligned T00 step 4 would record the actual shape rather than halting on a false expectation.
- **Closure:** v1.4 T00 step 4 inventory expectations:
  - `verification.py` PRESENT, extended with module-level `verify(manifest, args)` function (NOT module-level `_LANGUAGE_DISPATCH` symbol; dispatch dict is function-local inside `verify()`).
  - `python_verification.py` PRESENT, exporting private `_verify_python(manifest, args)` only (no public `verify` symbol).
  - `rust_verification.py` PRESENT, exporting private `_verify_rust(manifest, args)` only (no public `verify` symbol).
  - `go_verification.py` ABSENT (al-Mursalat T04 adds it; will export private `_verify_go(manifest, args)` per substrate convention).
  - `checker_set_hash.py` PRESENT with `_CHECKER_SOURCE_FILES: tuple[Path, ...]` extended at v0.11.8 to include `python_verification.py` and `rust_verification.py` entries; al-Mursalat T05 extends this tuple to include `go_verification.py` and `go_signature_canonicalization.py`.

### F-RM-8 MEDIUM -- T00 step 7 al-Hujurat amendments check refers to seven verification steps, but step 7 itself is the seventh, creating circular completeness

- **Severity:** MEDIUM
- **Locus:** T00 required record format (line 776-836): the template lists steps 1-7 plus a "Pre-flight verdict" §8. Step 7 (lines 763-774) is "al-Hujurat amendments confirmation". The record template's step 7 (lines 827-832) and "Cow Episode warning" (line 1497) reference seven verification steps.
- **Observation:** Internal counting consistency: T00 has steps 1-7 (seven gate steps) plus §8 verdict. The prompt narrative refers to "seven verification steps" but the actual record template (line 776-836) numbers them 1-7 with §8 as the verdict. This is internally consistent but the Cow Episode warning ("Do not expand T00 pre-flight beyond the seven verification steps") and the v1.4 closure may want to consider whether the v0.11.8 substrate-state-alignment work surfaces any new pre-flight gates worth a step 8.
- **Why MEDIUM:** Not a substrate truth issue; raised for visibility because v1.4 will need to add at least one new substrate-truth verification step covering the as-Saff symbol-export shape, and the Cow Episode warning currently forbids step expansion.
- **Closure:** v1.4 either (a) lifts the seven-step ceiling explicitly in the Cow Episode warning to accommodate a new "step 4b: per-language module export verification" subtask covering the F-RM-1 closure, OR (b) folds the new verification into step 4 as additional bulletpoints without bumping the step count.

### F-RM-9 MEDIUM -- §0 framing's "as-Saff Acceptance §15 two-layer dispatch pattern" citation is precise but the pattern itself doesn't license v1.3's claim

- **Severity:** MEDIUM
- **Locus:** F-AL-4 absorption note (lines 53-57); §0 framing (lines 358-360); T02 code block header comment (lines 925-933).
- **Observation:** v1.3 cites "as-Saff Acceptance §15 two-layer dispatch pattern" as the architectural license for symmetrizing the CLI's `_VERIFIER_DISPATCH` on per-language modules (`"python": python_verification.verify`, etc.). The framing implies as-Saff documented a two-layer dispatch (CLI-level + module-level) with per-language-module public verify entry points.
- **Substrate truth:** as-Saff Acceptance §15 (per the v1.3 audit we conducted at session start) establishes `verification.verify` as the public API entry point. as-Saff explicitly preserved the existing `Verifier` class as the byte-stable substrate; the per-language modules host the private dispatch handlers (`_verify_python`, `_verify_rust`). as-Saff did NOT establish public `python_verification.verify` / `rust_verification.verify` as canonical per-language entry points -- those are v1.3 self-review inventions.
- **Why MEDIUM:** This is the citation-misattribution shape from as-Saff F-AS-7 / F-XR-2. v1.3 cites as-Saff to legitimize a pattern as-Saff did not establish. The honest framing: "F-AL-4 introduces public per-language verify aliases as a new architectural extension; as-Saff Acceptance §15 establishes `verification.verify` as the canonical programmatic-RP entry point but does not pre-establish per-language public aliases."
- **Closure:** v1.4 F-AL-4 reframing: drop the "as-Saff Acceptance §15 two-layer dispatch pattern" license and either (a) accept that the CLI routes through `verification.verify(manifest, args)` (one-layer dispatch; matches substrate; saves no indirection but is correct), OR (b) introduce a new al-Mursalat task (T01.5) that adds public `verify` aliases to `python_verification.py`, `rust_verification.py`, AND `go_verification.py`, with its own substrate edits, tests, and acceptance criteria, explicitly framed as "al-Mursalat introduces the per-language-module public verify alias pattern".

### F-RM-10 MEDIUM -- Test-count baseline working hypothesis ~418 / ~440 is speculative; v0.11.8 CHANGELOG claim must ground it

- **Severity:** MEDIUM
- **Locus:** F-AL-3 (lines 42-47); §Calibration rungs v0.11.8 (lines 475-478); T00 step 2 (lines 684-696); Acceptance §11 (lines 1553-1560); T09 CHANGELOG entry test count delta (lines 1409-1417).
- **Observation:** v1.3 cites a working hypothesis of ~418 (408 + ~10 as-Saff delta) for the v0.11.8 baseline, with v0.12.0 projection ~440. The number is presented as a hypothesis to be confirmed by T00 step 2, which is methodologically correct.
- **Substrate truth:** The v0.11.8 ship merged today (2026-05-10). The actual v0.11.8 CHANGELOG entry's `### Tests` block contains the real count claim. F-RM-10 is not that the working hypothesis is wrong; it is that v1.3 missed an opportunity to ground the rung in the actual CHANGELOG number. The v0.11.8 substrate is now read-back-able; v1.4 can replace "working hypothesis ~418" with the literal v0.11.8 CHANGELOG count (with T00 step 2 still serving as the pytest-collect-only empirical cross-check per al-Hujurat T05 discipline).
- **Why MEDIUM:** Soft hardening. The current wording is methodologically correct (hypothesis to be confirmed); the upgrade is to substitute the substrate-claim ground truth so T00 step 2's role becomes "confirm CHANGELOG claim matches pytest count" rather than "discover the CHANGELOG claim".
- **Closure:** v1.4 reads the v0.11.8 CHANGELOG `### Tests` block's stated count at tag `cac6917` and substitutes the literal value for "~418" throughout the prompt. T00 step 2 record template line 792 ("CHANGELOG claim: <fill in>") becomes a confirmation step rather than a discovery step.

---

## LOW findings -- prose alignment

### F-RM-11 LOW -- v1.3 amendments header line 82 contains an em-dash

- **Severity:** LOW
- **Locus:** Line 82 (F-AL-7 absorption text): "F22 was closed at v0.11.3 per the release commit (\"F22 corrective — dispatch whitelist alignment\")"
- **Observation:** The line contains a U+2014 em-dash inside the cited release-commit subject line. Per the locked em-dash policy, project-authored prose must use `--`; the citation reproduces external text verbatim, but the v1.3 amendments block is project-authored prose, and the cited commit subject itself was authored as `dispatch whitelist alignment` (no em-dash; the em-dash is v1.3 self-review's prose addition).
- **Why LOW:** Single character; CI lint guard (now extended to docs/) will catch it if al-Mursalat v1.4 lands in `docs/g11.2-preflight.md` or any other CI-scanned path. The prompt itself is not under the CI guard, but the policy is locked.
- **Closure:** v1.4 line 82: `("F22 corrective -- dispatch whitelist alignment")`.

### F-RM-12 LOW -- v1.3 amendments header line 481 contains an em-dash

- **Severity:** LOW
- **Locus:** Line 481 (F-AL-2 calibration rung explanation): "pre-flight `docs/g11.2-preflight.md` inherits this guarantee — em-dash policy violations..."
- **Observation:** Standalone em-dash in F-AL-2 prose.
- **Closure:** v1.4 line 481: replace with `--`.

---

## Cross-walk: v1.3 self-review claims -> substrate verification

| v1.3 claim | Substrate at v0.11.8 (verified at `cac6917`) | Status |
|---|---|---|
| `python_verification.verify` (public) provided | Only `_verify_python` (private; `__all__ = ("_verify_python",)`) | FALSE -- F-RM-1 |
| `rust_verification.verify` (public) provided | Only `_verify_rust` (private; `__all__ = ("_verify_rust",)`) | FALSE -- F-RM-1 |
| `verification.verify` module-level | `def verify(manifest, args)` at line 556, in `__all__` | TRUE |
| `_LANGUAGE_DISPATCH` module-level symbol | Function-local dict inside `verification.verify` (line 599-603) | FALSE -- F-RM-2 |
| `_CHECKER_SOURCE_FILES` extended in `checker_set_hash.py` | TRUE (per as-Saff T04(b)) | TRUE |
| `gate11.errors` module | Does not exist | FALSE -- F-RM-3 |
| `gate11.manifest` module | Substrate has `manifest_schema` | FALSE -- F-RM-3 |
| `gate11._policy` module | Does not exist; `_build_identity_policy` not in gate11/ | FALSE -- F-RM-3 |
| `manifest.module_identity.language` attribute | `module_identity: dict[str, Any]`; use `.get("language")` | FALSE -- F-RM-4 |
| CLI substrate `src/furqan_lint/cli.py` for `manifest verify` | `manifest verify` is in `src/furqan_lint/gate11/cli.py` `cmd_manifest_verify` | FALSE -- F-RM-5 |
| Tag `v0.11.8` -> `cac6917`; main `cace1c0` | TRUE | TRUE |
| F22 closed at v0.11.3 (not al-Mursalat closing) | TRUE | TRUE |
| as-Saff Round 35 cycle ran on v1.0/v1.1/v1.2 | TRUE | TRUE |

Eleven substrate claims; four are substrate-true; seven are substrate-false (six load-bearing, one filesystem-level).

---

## Verdict

**HALT-AND-RETURN-TO-v1.4.**

Rationale:
- Three CRITICAL substrate-untrue load-bearing symbol/import claims (F-RM-1, F-RM-2, F-RM-3) plus three HIGH substrate-mismatches in load-bearing surfaces (F-RM-4, F-RM-5, F-RM-6). If Co-work implements T02 / T04 / T05 verbatim, the v0.12.0 implementation fails at module-import time before any test runs; CI will not catch this cleanly because the failure mode is `AttributeError` / `ModuleNotFoundError`, not syntactic.
- The same-instance limitation the v1.3 amendments block explicitly anticipated (lines 1852-1865) materialized: substrate-evidence-traceable amendments DID reduce architectural-reframing-class miss risk, but the F-AL-1 / F-AL-2 / F-AL-4 self-review codified substrate-nonexistent public symbol shapes as load-bearing facts. This is structurally identical to as-Saff v1.1's F-AS-2 / F-AS-7 same-instance miss that the Round 35 cycle reversed.
- v1.4 must be authored against direct substrate read at tag `v0.11.8` / commit `cac6917`. Specifically: read `src/furqan_lint/gate11/python_verification.py`, `rust_verification.py`, `verification.py` in full; read `src/furqan_lint/gate11/cli.py` to confirm `cmd_manifest_verify` location and current dispatch shape; grep `_build_identity_policy` across `src/`; read `manifest_schema.py` to confirm `module_identity` type.
- v1.4 is NOT a polish pass; it is a substrate-truth realignment of the dispatch architecture. The prompt's structural intent (closing F22 by routing CLI dispatch through language-aware paths plus adding Go substrate) is correct and unchanged; the wiring details need to be re-grounded.

---

## Recommended v1.4 authoring order

1. F-RM-3 closure FIRST (import path corrections) -- affects T02, T04, T06 code blocks; mechanically locatable, smallest surface.
2. F-RM-4 closure (dict access vs attribute access) -- one-token substitutions across T02 / T04 code blocks.
3. F-RM-5 closure (CLI module relocation) -- T02 substrate declaration + code block header comment.
4. F-RM-6 closure (T05 substrate path + symbol + integration) -- mirrors as-Saff F-XR-3 absorption pattern; reuses as-Saff T04(b) idiom.
5. F-RM-1 + F-RM-2 closure TOGETHER (dispatch architecture decision) -- this is the load-bearing decision: either (a) route CLI through `verification.verify(manifest, args)` and extend the function-local dispatch dict with `"go"` (minimal-substrate-change path; F22 closes; per-language-module-symmetric dispatch dropped), OR (b) introduce a new T01.5 task adding public `verify` aliases to `python_verification`, `rust_verification`, `go_verification` as a substrate ADR with its own acceptance criteria. Project-lead disposition between (a) and (b) is the meaningful decision; both are substrate-honest. The audit recommends (a) as the principle-of-least-substrate-change path; (b) is defensible if the per-language-module-symmetric public API surface is judged worth the additional substrate edits and ADR-level documentation.
6. F-RM-7 closure (T00 step 4 expected inventory) -- mechanical update reflecting (5)'s decision.
7. F-RM-8 closure (T00 step count handling) -- one-paragraph Cow Episode warning amendment.
8. F-RM-9 closure (as-Saff §15 citation precision) -- prose tightening; depends on (5).
9. F-RM-10 closure (test-count baseline grounding) -- read v0.11.8 CHANGELOG `### Tests` block at `cac6917`; substitute literal count.
10. F-RM-11 + F-RM-12 closure (em-dash sweep) -- two character substitutions.

---

## Substrate verification log (this audit)

- Tag `v0.11.8` -> commit `cac6917d8136ed9fa10ce65ff023469ce6eeef3f` (verified via `git rev-list -n1 v0.11.8`).
- Main HEAD `cace1c0df49f322b2a9d8aee7533f98ad1304a86` (merge of PR #26; verified via `git log origin/main`).
- `verification.py`: 618 lines; module-level `def verify(manifest, args)` at line 556; function-local `_LANGUAGE_DISPATCH` dict inside `verify()` at lines 599-603; `CasmVerificationError` class at line 52; `__all__` includes `"verify"` and `"CasmVerificationError"`.
- `python_verification.py`: 86 lines; `def _verify_python(manifest, args)` at line 53; `__all__ = ("_verify_python",)` at line 86. No public `verify`.
- `rust_verification.py`: 87 lines; `def _verify_rust(manifest, args)` at line 54; `__all__ = ("_verify_rust",)` at line 87. No public `verify`.
- `gate11/cli.py`: `def cmd_manifest_verify(args: list[str]) -> int` at line 286; `Verifier(trust_config=trust_config)` at lines 333 and 456; no dispatch dict.
- `gate11/`: no `errors.py`; no `manifest.py` (substrate is `manifest_schema.py`); no `_policy.py`.
- `gate11/manifest_schema.py`: `module_identity: dict[str, Any]` at line 134.
- `grep -rn _build_identity_policy src/furqan_lint/gate11/`: zero matches.

---

## Methodology notes

- Six-element findings format observed: severity, locus, observation, substrate truth, why-severity, closure, reference.
- Severity uppercase throughout.
- Em-dash policy: this audit uses `--` in prose; no `---` LaTeX ligatures.
- F-RM-N namespace: distinct from F-AL-N (v1.3 self-review), F-XR-N (as-Saff Round 35), F-AS-N (as-Saff producer same-instance), F-RV-N (as-Saff Round 35 v1.2 review). Round 36 namespace is open for this and any subsequent v1.4 + audits.

End of Round 36 audit.

---

# Bismillah ir-Rahman ir-Rahim
