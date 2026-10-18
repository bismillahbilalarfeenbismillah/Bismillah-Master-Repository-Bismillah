# Bismillah ir-Rahman ir-Rahim

# R0517 -- furqan-lint Coding Strategy — Roadmap to v1.0

**Chronological Index:** 255 of 995  
**Date:** 2026-05-27  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** furqan_lint_v1_Roadmap.pdf  
**Source Format:** pdf  
**SHA-256:** `be99bb6154bab006c39e299b7f07b76fc6a4e121b6e1cdf76df5e6aee323b91f`  

---

## R0517 · furqan-lint Coding Strategy — Roadmap to v1.0

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: furqan_lint_v1_Roadmap.pdf
- source_format: pdf
- text_sha256: be99bb6154bab006c39e299b7f07b76fc6a4e121b6e1cdf76df5e6aee323b91f

furqan-lint Coding Strategy — Roadmap to v1.0

furqan-lint Coding Strategy
Roadmap to the Next Version (v0.8.5 → v1.0)
With the Context-Aware Suggestion Engine as the Centerpiece Feature

BayyinahEnterprise — Internal Engineering Strategy
Author: Bilal Syed Arfeen
Document Date: May 27, 2026

Page 1 of 11


furqan-lint Coding Strategy — Roadmap to v1.0

1. Where We Are — Baseline
Current public substrate (per dissertation Ch16 SI4 anchor):
•

Version: v0.8.5

•

Languages: Python (primary), Rust (functional), Go (growing), ONNX (growing)

•

Defect taxonomy: Four shapes — Optional collapse, silently-removed public name,
zero-return ring-close, return-None mismatch. Per dissertation §12.1, the checker
coverage is honest about what is not yet implemented.

•

Attestation: Sigstore-CASM Gate 11 — cryptographic attestation manifest of verified
codebase, with manifest schema, signing, surface extraction, and module
canonicalization implemented.

•

Distribution: GitHub source, pip-installable, no pre-commit hooks yet, no PyPI release
automation.

•

Self-application: Repo runs its own linter on commits via internal CI, but the selfapplication is not yet a release gate and no signed self-attestation ships with releases.

What the linter does well today: catches the four-shape defects in Python with low false-positive
rates, produces structured diagnostic output, integrates with the gate11 attestation chain. What
it does not do today: read a project-level context manifest, suggest fixes, cross-function R_may
analysis, code-vs-docstring consistency, source-SBOM consistency.

2. Where We Want To Be — Target for Next Version
The next version is a substantive release, not a patch. Working name: v1.0 (justified by the
scope below — manifest-awareness, suggestion engine, cross-function R_may, adoption
packaging together cross a v1.0 maturity line). Acceptance criteria:
•

Manifest-aware: reads `.ax-sh.yaml` declaring (O, K, R, R_may, Π_X, ~_X) for the
project.

•

Suggestion-engine capable: for every violation it flags, it generates ranked candidate
fixes scored against the declared context, with axiom-grounded explanations of why one
fix outranks another.

•

Cross-function R_may aware: catches caller-side exhaustiveness violations across
function boundaries, not just at the called site.

•

Code-vs-docstring projection consistency: detects when a docstring's described behavior
diverges from the function signature or body.

•

Self-application as release gate: the linter cannot release a version that fails its own lint,
and the release artifact carries a signed self-attestation.

•

Distribution-ready: PyPI publishing automation; pre-commit hook manifest; GitHub
Action; first three external codebases empirically characterized for FP/FN rates.

•

Documentation: 5-minute getting-started, full manifest schema reference, suggestionengine concept guide for users.

3. Priority 0 — Foundation (Sprint 1, ~2-3 weeks)
Everything downstream depends on these. Build these first or the rest fails.

Page 2 of 11


furqan-lint Coding Strategy — Roadmap to v1.0

3.1 Manifest schema and reader
New module: src/furqan_lint/manifest.py. Reads `.ax-sh.yaml` from project root. Schema (draft):
# .ax-sh.yaml
schema_version: 1
observer_model: external_caller
# or: internal_package, network_peer
context_set:
language: python
python_version: ">=3.10"
input_size_limit: "10MB"
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

•

Acceptance: Schema validates with jsonschema or pydantic; unit tests for malformed
manifests; path-pattern overrides resolve correctly; missing manifest falls back to safe
defaults with a single advisory finding noting the manifest is absent.

3.2 Self-application release gate
Modify the existing CI workflow so that:
•

furqan-lint runs over its own src/ tree on every PR.

•

Findings must be either fixed or dispositioned with a `# noqa: furqan-lint(reason)`
directive that itself appears in an append-only journal.

•

Release tag creation requires the self-lint to pass clean.

•

The release artifact carries a signed self-attestation: `release.tar.gz.sig +
release.attest.json` where the attestation declares which lint rules ran, which version,
which manifest was in effect, what the findings were, and how each was dispositioned.

This operationalizes Chapter 22's recursive self-application discipline at the release-gate layer.
It also produces the cleanest possible marketing artifact: the tool that catches the bugs you
don't want shipped catches its own bugs and refuses to ship them.

Page 3 of 11


furqan-lint Coding Strategy — Roadmap to v1.0

4. Priority 1 — The Suggestion Engine (Sprints 2-4, ~6-8
weeks)
This is the centerpiece feature. The thing that takes furqan-lint from "underlines the typo" to
"suggests the right word in your context." Architecture and implementation below.

4.1 Architecture
Four components, in src/furqan_lint/suggest/:
src/furqan_lint/suggest/
__init__.py
generator.py
# produces candidate fixes per violation class
context.py
# reads manifest + per-file overrides
ranker.py
# scores candidates against declared context
explain.py
# axiom-grounded explanation formatter
catalog/
# per-violation-class fix templates
optional_collapse.py
removed_public_name.py
zero_return_ring_close.py
return_none_mismatch.py

4.2 SuggestionGenerator
Input: a Finding object (existing diagnostic). Output: a list of Candidate(fix_text,
axiom_discharge, complexity_score, safety_margin).
Implementation strategy: start with template-based generation. For each defect class, the
catalog file enumerates 2-4 candidate fix patterns with documented axiom-discharge mapping.
Example for Optional collapse:
# catalog/optional_collapse.py
CANDIDATES = [
Candidate(
name="explicit_handle_none",
template="if {var} is None:\n
{handle}\nelse:\n
{body}",
discharge=A3_HANDLE,
complexity=2,
safety_margin=HIGH,
),
Candidate(
name="propagate_as_typed_incomplete",
template="return None # propagated as Optional[T]; caller handles",
discharge=A3_PROPAGATE,
complexity=1,
safety_margin=MEDIUM,
),
Candidate(
name="prove_unreachable",
template="assert {var} is not None, '{proof}'",
discharge=A3_UNREACHABLE,
complexity=1,

Page 4 of 11


furqan-lint Coding Strategy — Roadmap to v1.0

safety_margin=LOW,

# depends on proof

),
]

Later: layer in LLM-guided generation for cases the template catalog doesn't cover. When LLMguided, apply the multi-vendor cross-audit discipline (see §4.5).

4.3 SuggestionRanker
Scores each candidate against the manifest context. Rough scoring function:
def score(candidate, context):
s = 0
# Match the axiom discharge to context preferences
if context.safety_critical:
# prefer explicit handling > propagation > unreachable proof
s += {A3_HANDLE: 30, A3_PROPAGATE: 15, A3_UNREACHABLE: 0}
[candidate.discharge]
elif context.hot_path:
# prefer low-complexity, low-overhead solutions
s += 25 - candidate.complexity * 5
else:
# general purpose: match R_may declaration
if context.r_may_includes_explicit_incomplete:
s += {A3_PROPAGATE: 25, A3_HANDLE: 15, A3_UNREACHABLE: 5}
[candidate.discharge]
# safety margin always counts
s += candidate.safety_margin.numeric
return s

This is heuristic, not learned. Document the scoring transparently so users can see why one fix
ranked higher than another. A later version can learn weights from telemetry on which
suggestions users accept.

4.4 ExplanationFormatter
Every ranked suggestion ships with an explanation grounded in the framework's axiomdischarge vocabulary. Example output:
Finding: Optional collapse at src/parser.py:142
Top suggestion (rank 1, score 47):
explicit_handle_none — Axiom 3 discharge path 1 (handle)
if result is None:
return ParseError("unexpected EOF")
else:
return result
Why: your manifest declares this file under src/critical_path/*,
which sets safety_critical=true. Under safety-critical context,
the framework prefers explicit handling over silent propagation.

Page 5 of 11


furqan-lint Coding Strategy — Roadmap to v1.0

Alternative (rank 2, score 32):
propagate_as_typed_incomplete — A3 discharge path 2 (propagate)
return result

# callers must handle Optional[T]

Why: lower complexity, but pushes the obligation to callers.
In safety-critical contexts this is acceptable only if all callers
are themselves verified to discharge the incompleteness.

4.5 LLM-guided generation and the multi-vendor cross-audit safety
For violations the template catalog doesn't cover, optionally invoke an LLM to propose
candidate fixes. The recursive concern is real: an LLM-generated fix in a structural-honesty tool
is exactly the kind of producer-correlated artifact the framework worries about. Mitigation:
•

LLM-generated candidates are flagged as such in the explanation.

•

Optional multi-vendor mode: invoke 2-3 LLM vendors independently, present only
candidates that two or more vendors converge on. Divergent candidates surface as
advisory rather than ranked.

•

LLM mode is off by default; user opts in via manifest setting
`suggestion_engine.llm_assist: true`.

•

All LLM-generated candidates pass through the static-analysis discipline before being
shown to the user. Candidates that themselves fail furqan-lint are filtered out.

5. Priority 2 — Deeper Axiom Checks (Sprints 5-7, ~6-8
weeks)
Each item below is a new checker module. Start with Python; Rust/Go follow in subsequent
point releases.

5.1 Cross-function R_may analysis
New module: src/furqan_lint/checkers/r_may_caller_side.py. For every function in the
codebase, compute the function's R_may (declared returns plus inferable error paths plus
partial-state outcomes) and verify every caller discharges its full R_may via one of the three
paths.
Implementation strategy: build a call graph using existing AST infrastructure (ast.walk-based
extraction is already in place for other checkers). For each function, derive R_may from:
•

Return type annotation (if present) — base R_may from declared returns.

•

Raise statements in the function body — adds exception variants to R_may.

•

Calls to known partial-state-returning library functions (e.g., dict.get) — propagates their
R_may up.

Then for each caller of the function, statically check that the caller handles, propagates, or
proves-unreachable each R_may variant. Flag callers that don't.
Acceptance: catches the canonical cases (caller of a Result<T, E> Rust function that handles
only Ok; caller of a Python function that raises but doesn't declare the exception in its own raise;

Page 6 of 11


furqan-lint Coding Strategy — Roadmap to v1.0

caller of dict.get that doesn't handle None). False-positive characterization against three opensource codebases before release.

5.2 Code-vs-docstring projection consistency (A4 at the documentation
layer)
New module: src/furqan_lint/checkers/docstring_consistency.py. Parses docstrings as
projections of function behavior; verifies they don't contradict the function signature or body.
Checks initially supported (Python, NumPy/Google docstring formats):
•

Docstring claims `@returns: int` but signature says `-> str` → flag.

•

Docstring lists parameters that aren't in the signature, or omits parameters that are →
flag.

•

Docstring claims `@raises: ValueError` but no raise ValueError in body → flag with low
confidence (might be inherited).

•

Docstring's `@behavior: pure` annotation but body has side effects (print, file I/O,
network) → flag.

5.3 Source-vs-SBOM consistency
New module: src/furqan_lint/checkers/sbom_consistency.py. Reads SBOM file (SPDX or
CycloneDX) and verifies it matches the source dependency tree.
•

Every entry in pyproject.toml / requirements.txt / Cargo.toml / go.mod must appear in the
SBOM, and vice versa.

•

Pinned versions must match between source and SBOM.

•

Transitive dependencies in the SBOM must be reachable from declared roots.

•

Output is the canonical Mini Shai-Hulud defense at the SBOM-projection layer.

6. Priority 3 — Adoption Packaging (Sprints 8-9, ~4-6 weeks)
All the verification work above is moot if developers can't easily install and run the tool. This
sprint is operational.

6.1 PyPI distribution
•

Reserve the name `furqan-lint` on PyPI (do this in Sprint 1 if not already).

•

Set up automated PyPI publishing on tagged releases via GitHub Actions, using OIDC
trusted publishing (no API token in repo).

•

Polish pyproject.toml: entry points, classifiers, long description from README, license.

•

First release to TestPyPI; verify install works; promote to production PyPI.

6.2 Pre-commit hook
Add `.pre-commit-hooks.yaml` to repo root:
- id: furqan-lint
name: Furqan Lint — structural honesty checks
entry: furqan-lint check
language: python

Page 7 of 11


furqan-lint Coding Strategy — Roadmap to v1.0

types_or: [python, rust, go]
args: [--respect-manifest]
- id: furqan-lint-gate11
name: Sigstore-CASM Gate 11 attestation
entry: furqan-lint gate11 verify
language: python
always_run: true
pass_filenames: false

Ensure `furqan-lint check` respects the `--files` argument pre-commit passes (only run on
changed files); this is critical for adoption — slow hooks get disabled.

6.3 GitHub Action
Publish `BayyinahEnterprise/furqan-lint-action@v1` to GitHub Marketplace. Action wraps the
CLI:
- uses: BayyinahEnterprise/furqan-lint-action@v1
with:
languages: python,rust,go
manifest: .ax-sh.yaml
suggestion-engine: true

6.4 Documentation
•

README: "Furqan-lint catches the kind of bugs where your code's description doesn't
match what it does." Then concrete examples.

•

Getting started in 5 minutes: install, init a manifest, run on your repo, fix the first finding
using a suggestion.

•

Manifest schema reference: every key, what it means, what happens when it's omitted.

•

Suggestion engine concept guide: how candidates are ranked, what the axiomdischarge labels mean, how to override or disable specific suggestions.

6.5 Empirical FP/FN characterization
Run furqan-lint at v1.0 against three open-source codebases (suggested: a mid-sized Python
library like requests; a mid-sized Rust crate; a mid-sized Go service). For each:
•

Document raw finding counts and categorize as true positive, false positive, debatable.

•

Publish the analysis as a case-study document (also serves as Chapter 21 falsificationprotocol grounding).

•

Refine the catalog and ranker based on findings before final release.

7. Priority 4 — Research Scaffolding (Sprint 10+, ongoing)
These don't block v1.0 release but should be visible as ongoing work — they're what makes
furqan-lint a research instrument as well as a product.

Page 8 of 11


furqan-lint Coding Strategy — Roadmap to v1.0

7.1 Reference-parity test corpus
Publish a fixed corpus of test inputs (Python files, Rust crates, Go packages) where the
expected findings are stable and bit-identically comparable. Independent reimplementations of
furqan-lint can be checked against this corpus for parity. This is the year-10 strength-n
milestone made operationally tractable: even before independent reimplementations exist, the
corpus is the ground truth they would have to match.

7.2 Falsification-protocol scripts
Chapter 21's four protocols implemented as runnable tools shipped with furqan-lint:
•

`furqan-lint falsify adequacy` — adequacy counter-example construction harness.

•

`furqan-lint falsify independence` — fault-source inventory tool.

•

`furqan-lint falsify quantum` — public-key dependency analyzer.

•

`furqan-lint falsify durability` — preservation-discipline simulator.

7.3 Ecosystem-condition probe
`furqan-lint diagnose ecosystem` — examines a codebase and reports whether the four
ecosystem conditions hold. Where they don't, axiom satisfaction is operationally empty and the
report surfaces this honestly.

8. Sequencing and Dependencies
Critical path (what blocks what):
Sprint 1 (P0):
Sprint 2-4 (P1):
Sprint 5-7 (P2):
Sprint 8-9 (P3):

Sprint 10+ (P4):

Manifest + self-application gate
↓
Suggestion engine [needs P0 manifest]
↓
Cross-function R_may + docstring + SBOM
↓
↘
PyPI + pre-commit + Action + docs
↓
v1.0 RELEASE
Reference-parity corpus + falsification scripts
(parallel, post-release)

Total horizon to v1.0: approximately 20-24 weeks of focused engineering. The single-developer
estimate; faster with help. Multiplication factor of ~1.5x for one external code-review discipline
(per the dissertation's R5 validator-diversity discipline, the framework asks for it).

9. Definition of "v1.0 Complete"
v1.0 ships when all of the following are true:
•

Manifest schema implemented, documented, validated. Five sample manifests covering
common project shapes shipped as templates.

•

Self-application release gate active. The v1.0 release artifact itself carries a signed selfattestation.
Page 9 of 11


furqan-lint Coding Strategy — Roadmap to v1.0

•

Suggestion engine: all four current defect classes have ≥2 candidate fixes each in the
catalog. Ranker produces sensible rankings against the five sample manifests.

•

Cross-function R_may checker: catches the canonical Python and Rust cases; FP rate
<5% on the three reference codebases.

•

Docstring consistency checker: catches the canonical Python cases; FP rate <10%
(docstrings are noisier).

•

SBOM consistency checker: passes on the three reference codebases; flags injected
discrepancies in dedicated test fixtures.

•

PyPI release: installable via `pip install furqan-lint`.

•

Pre-commit hook: install instructions in README work end-to-end on a fresh repo.

•

GitHub Action: listed on Marketplace, succeeds on a sample project.

•

Documentation: 5-minute getting-started works, manifest reference complete,
suggestion-engine guide explains the axiom-discharge ranking.

•

Empirical case studies: three published, with FP/FN data and refinements applied to the
catalog and ranker.

10. What v1.0 Does Not Build (and Why)
Honest scoping. The following are deferred to v1.x or v2.0 even though they appear in the
broader strategy documents:
•

Independent reimplementations (year-10 reference-parity engineering target).
Requires institutional partnership or grant funding; not a single-developer deliverable.
Deferred to v2.x.

•

Quantum-survivable signing primitives in Gate 11. Sigstore itself has not migrated;
we follow upstream. Tracked but not implemented.

•

DER firmware attestation generalization (the Ashraf-proposal large scope).
Requires substrate-domain expert collaboration. Deferred to whichever institutional
partnership emerges first.

•

Furqan-language native checker integration. Furqan is still a type-checker prototype
without a backend. Compose later when Furqan reaches v1.0.

•

Cross-product (Bayyinah ↔ furqan-lint) routing. Defer until both products have
independent v1.0 releases; integrating before each is mature would produce coupled
releases that are hard to maintain.

The principle: ship a tight, complete v1.0 that does what it says with manifest awareness and a
suggestion engine, rather than a sprawling release that does many things partly. The
framework's own A1 discipline applies: v1.0 commits to a public surface that v1.x must remain
Liskov-Wing-compatible with. Better to commit to less than to break the discipline with a tooambitious surface.

11. Closing
The suggestion engine is the single feature that takes furqan-lint from "linter" to "structuralhonesty advisor" in a way no other linter currently shipping is positioned to match. Because the
ranking is grounded in the declared (O, K, R, R_may) sextuple, the suggestions are contextual
in a way that LLM-only suggestion tools cannot be — the framework knows what context the

Page 10 of 11


furqan-lint Coding Strategy — Roadmap to v1.0

developer is operating in because the manifest says so, and the ranking is explicit about why
one fix outranks another in that context.
That is the product story for v1.0. The research story is the same: the suggestion engine
operationalizes Axiom 3's three discharge paths (handle / propagate / prove-unreachable) as
user-facing choices, which is the cleanest possible empirical demonstration that the axioms are
not just theoretical machinery but engineering primitives developers can use.
Twenty to twenty-four weeks. Real engineering work. The next conversation worth having is
which sprint to start in week one, whether to begin with the manifest or with prepping the PyPI
release while the manifest design is being refined. I would start with the manifest — everything
else depends on it — but the PyPI name reservation is a same-day side task that should not
wait.
La hawla wa la quwwata illa billah.

Page 11 of 11

---

# Bismillah ir-Rahman ir-Rahim
