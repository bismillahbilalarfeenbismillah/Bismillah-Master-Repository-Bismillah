# Bismillah ir-Rahman ir-Rahim

# R0515 -- furqan-lint ONNX expansion plan, derived from cont59-cont63 substrate

**Chronological Index:** 215 of 995  
**Date:** 2026-05-06  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** FURQAN_LINT_ONNX_EXPANSION_PLAN.md  
**Source Format:** md  
**SHA-256:** `d92115bc903ac672d301ba1615d4384f4c95647c448030f6043e7f247198c861`  

---

## R0515 · furqan-lint ONNX expansion plan, derived from cont59-cont63 substrate

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: FURQAN_LINT_ONNX_EXPANSION_PLAN.md
- source_format: md
- text_sha256: d92115bc903ac672d301ba1615d4384f4c95647c448030f6043e7f247198c861

# furqan-lint ONNX expansion plan, derived from cont59-cont63 substrate

**Author:** producer (Bilal + cont63-instance Claude reflective handoff)
**Date:** 2026-05-06
**Status:** DRAFT for principal review and furqan-lint maintainer adoption
**Substrate basis:** cont59 (NG-1 F1 origin), cont60 (NG-1 closure execution),
cont61 (NG-3 substrate work), cont62 (broader Bayyinah triage), cont63
(P-NEW22 build with three debug iterations)

---

## 1. Audit posture

This plan audits the work shipped across cont59 through cont63 and translates
the findings into concrete check proposals for furqan-lint's ONNX adapter.
Each proposed check has: an empirical origin (a specific failure that occurred
in the chain), a check definition (what the linter would inspect), severity
classification (per BAF v4.0), and implementation notes (what data structure
or code would be needed).

The current furqan-lint v0.9.4 ONNX adapter ships five checks: D24-onnx
(all-paths-emit), opset-compliance, D11-onnx (shape-coverage), numpy_divergence,
and score_validity. These ran clean on every cont53-cont63 save and caught
zero of the actual bugs encountered. The proposed expansion is targeted: each
new check addresses a failure that the existing five did not catch but
demonstrably could have.

The work pattern across cont59-cont63 was roughly 60% audit/closure work and
40% producer chain output. cont60's NG-1 closure spent 24 audit findings (13
NG-1 + 11 NG-2) repairing structural drift. cont63 produced one save (task268)
with three debug iterations exposing two new APE classes (APE-13 ray direction,
APE-14 end-cell masking). The expansion plan is shaped by both halves: the
audit findings give us methodology checks, and the producer debug iterations
give us algorithm-level checks.

## 2. Self-audit of cont59-cont63 work

### What shipped clean

Eight automated checks now run on every cont60+ build:
- pytest tests/test_all_saves_correct.py (zahir gate, 650 cases pass)
- pytest tests/test_all_saves_score.py (batin gate, 650 pass + 20 MARAD-10 skip)
- furqan-lint v0.9.4 ONNX adapter (5 structural checks, runs in seconds)
- Five-gate manual checklist before SAVED claim
- saved_list.txt regeneration after every solutions/ mutation
- removed_list.txt audit trail
- byte-identity CI sample (3/3 PASS at cont60 close)
- Methodology files at handoff root from cont60 onward

These eight catch the bug shapes that NG-1 F1, F2, F3, F5 surfaced.

### What still ships in human discipline

Not yet automated:
- §11.4 pre-flight Q0 through Q5 (run by hand at session open)
- APE register backfill (run at session close per cont60 standing rule)
- Cross-document consistency between dossier §9, APE_REGISTER, and SKILL.md
- Verse anchor + round-numbering disclosure at session open
- Q3 REBUILD_THRESHOLD calibration (still v0 placeholder at 0.5)

These are the layer where furqan-lint expansion has the most leverage.

### Bug-shapes that furqan-lint v0.9.4 could not have caught

Cont63 build had three debug iterations producing three bugs:
1. **Prefix-max ray direction inverted (APE-13).** r=0 w=4 on initial build.
   numpy_divergence COULD catch this if the ONNX adapter had a sidecar that
   listed expected outputs. v0.9.4 silent-passes when sidecar is absent.
2. **Paint mask extending into padding (APE-4 reaffirmation).** Single-cell
   diff at (0, 7) on train[0]. numpy_divergence would also catch this with
   sidecar.
3. **Diagonal rays from all gap cells instead of end-cells (APE-14).** r=1 w=3.
   numpy_divergence would catch with sidecar.

All three are caught only by running test_network with ARC data, which is
expensive (loads onnxruntime, runs inference). A static-analysis check that
detects these patterns at the ONNX graph level would catch them before
runtime.

### Methodology-level bugs that bypassed all checks

NG-1 F1 (cont59 task293 silent rebuild claimed as +1 delta) bypassed every
check because it was a count-arithmetic bug, not a graph bug. The fix was
saved_list.txt as canonical authority + Q0 in pre-flight + APE-12 documentation.
A linter check on the build script that reads saved_list.txt would have
caught this.

NG-3 N1 (APE-6 attribution drift in cont60 APE_REGISTER.md) bypassed every
check because APE_REGISTER.md was treated as producer-authored prose. A linter
check that verifies APE entries against dossier §9 canonical would have caught
this.

## 3. Proposed checks, organized by adoption priority

### Round 1: Bug-shape mechanical checks (high leverage, low complexity)

These detect specific ONNX graph patterns that mapped to real failures in
cont59-cont63. Each is mechanically checkable from the .onnx file alone.

#### Check ARGMIN-WARN (severity LOW)

**Origin:** MARAD-10, NG-1 F2.

**What it does:** scan graph for ArgMin or ArgMax nodes. If present, emit
ADVISORY: "this save uses ArgMin/ArgMax; onnx_tool cannot profile it locally
and score_file will return None. The save is still valid for Kaggle submission
but should be documented under MARAD-10."

**Implementation:** one pass over `model.graph.node`, check `op_type` field.
About 10 lines of Python. Wire into the existing structural-checks list.

**Why it matters:** prevents the cont60 F2 surprise pattern. A save that
ships and silently fails score_file is a phantom-test risk; surfacing it via
ADVISORY makes the failure expected.

#### Check EQUAL-FLOAT (severity MEDIUM)

**Origin:** APE-1, APE-5, APE-11.

**What it does:** scan for Equal nodes whose input tensors are float type.
Opset 10 Equal supports only integer types. Float-Equal silently fails or
mis-compares.

**Implementation:** for each Equal node, trace input dtype via shape inference
or initializer types. If float, emit FAIL (or ADVISORY for opset 11+). About
30 lines.

**Why it matters:** APE-5 was rediscovered at cont55 (P-NEW17.5 size_count
comparison). A linter check would have caught it pre-merge.

#### Check IN-GRID-MASK-COVERAGE (severity MEDIUM)

**Origin:** APE-4, cont63 second debug iteration.

**What it does:** detect output-painting patterns (Mul or Add nodes in the
final 1-3 layers before the output node). Verify that at least one of their
upstream inputs traces to a `ReduceSum(input, axes=[1])` operation (the
canonical in_grid_mask). If not, emit ADVISORY: "output painting may extend
into 30x30 padding region; consider masking by in_grid_mask."

**Implementation:** dataflow analysis over the last few layers; a heuristic
match for "ReduceSum with axes=[1] over the input tensor". About 60 lines.
Not perfectly precise (false positives possible if the build genuinely doesn't
paint outside its bbox) but useful as a warning.

**Why it matters:** cont63 task268 first build painted (0, 7) outside the
actual 7x7 grid because in_grid_mask wasn't applied. APE-4 is one of the
most-frequent latent bugs.

#### Check ORPHAN-INITIALIZERS (severity LOW)

**Origin:** NG-1 F9.

**What it does:** for each tensor in `model.graph.initializer`, verify it
appears in the input list of at least one node. Initializers not referenced
by any node are dead weight.

**Implementation:** set difference between initializer names and union of
all node input names. About 10 lines.

**Why it matters:** NG-1 found 93 of 334 saves (28%) have orphan initializers.
Not safety-critical but bloats file size. furqan-lint catching this lets the
chain clean up incrementally.

### Round 2: Sidecar-driven checks (medium leverage, requires NeuroGolf-convention sidecar)

These checks require the build to ship a sidecar JSON describing expected
behavior. The cont53+ NeuroGolf saves already ship `task{NNN}.json` sidecars
with the canonical fields.

#### Check SAVED-LIST-Q0 (severity HIGH)

**Origin:** NG-1 F1 (the load-bearing finding of the entire NG-1 audit).

**What it does:** read sidecar's `task_num` field. Read companion
`saved_list.txt` (located at handoff tarball root or alongside the .onnx).
If `task{N}` already in saved_list AND sidecar's `score` is not significantly
higher than the existing save's score (default REBUILD_THRESHOLD=0.5), emit
FAIL: "task already saved at score X; this rebuild scores Y, which is below
the rebuild threshold."

**Implementation:** sidecar parser + saved_list reader + score comparison.
About 80 lines. Requires the sidecar to include `score` (which cont53+ already
does) and a way to fetch the existing save's score (either from a parallel
`saved_scores.txt` or by running score_file on the existing .onnx).

**Why it matters:** this is APE-12 prevention. NG-1 F1 spent 13+ audit
findings to clean up the structural drift. A linter check would have stopped
the regression-rebuild before it ever shipped.

#### Check NUMPY-DIVERGENCE-WITH-SIDECAR (severity HIGH)

**Origin:** cont63 three debug iterations.

**What it does:** v0.9.4 numpy_divergence silent-passes when no sidecar is
present. EXTEND: when sidecar is present, require it to include `task_uid`
and look up the ARC task data, run `test_network` against the .onnx, fail if
wrong > 0. Already-essentially-implemented; just needs the sidecar contract
formalized and the silent-pass converted to a hard fail when `[onnx-runtime]`
extra is installed.

**Implementation:** about 40 lines. The plumbing already exists in the
adapter; the gap is the contract.

**Why it matters:** cont63 build had three iterations; each iteration's bug
would have been caught by numpy_divergence with sidecar. Currently this check
silent-passes by default.

#### Check BUILD-SCRIPT-RELATIVE-PATH (severity MEDIUM)

**Origin:** NG-1 F3 (hardcoded build paths breaking handoff reproducibility).

**What it does:** when a `build*.py` is present alongside `task*.onnx`,
inspect the build script for hardcoded absolute paths matching
`/tmp/.../solutions/` or similar. If found, emit FAIL: "build script uses
absolute path; output will not write in handoff context."

**Implementation:** simple regex over the build script text. About 20 lines.

**Why it matters:** NG-1 F3 found that 10 of 26 build scripts had this drift.
A linter check at ship time prevents it from accumulating.

#### Check BYTE-IDENTITY-REPRODUCER (severity MEDIUM)

**Origin:** NG-1 F3 follow-up (NG-2 D8).

**What it does:** when a `build*.py` is present alongside `task*.onnx`, run
the build script in a fresh tempdir, compare md5 of the produced .onnx with
the committed .onnx. If not byte-identical, emit FAIL.

**Implementation:** about 50 lines (subprocess + md5sum). Requires build
script to use relative paths (depends on BUILD-SCRIPT-RELATIVE-PATH check).

**Why it matters:** NG-1 F3 ship-time CI sample passed 3/3, but the chain
discipline only checks samples. A linter that runs this on every save makes
nondeterminism mechanically detectable.

### Round 3: Algorithm-pattern checks (high complexity, semantic detection)

These are speculative. They detect specific algorithmic patterns that mapped
to bugs in cont63. Implementation requires shape inference plus pattern
matching over the graph topology.

#### Check PREFIX-MAX-RAY-DIRECTION (severity MEDIUM)

**Origin:** APE-13 (cont63 first debug iteration).

**What it does:** detect prefix-max ray accumulator patterns (a sequence of
Pad+Slice+Max with doubling step sizes). For each detected ray, verify the
shift direction is consistent with the apparent ray direction. The "apparent
direction" is harder; could heuristically infer from variable names or comments.

**Implementation:** about 200 lines, includes graph pattern matching plus
heuristics. Hard to make precise; useful as a warning rather than a hard fail.

**Why it matters:** APE-13 cost cont63 one debug iteration. Catching it
statically would save iteration time.

**Caveat:** this check is specific enough to NeuroGolf substrate that it may
not generalize. Could be implemented as a NeuroGolf-specific plugin rather
than core furqan-lint.

#### Check END-CELL-MASKING (severity MEDIUM)

**Origin:** APE-14 (cont63 second debug iteration).

**What it does:** detect when a multi-cell mask feeds a diagonal ray
accumulator without first being decomposed into end-cells via the
`mask * (1 - shift(mask, ...))` idiom.

**Implementation:** specific pattern match over graph topology. About 150
lines. Same generality caveat as above.

#### Check OPSET10-BANNED-OPS (severity HIGH, possibly already covered)

**Origin:** APE-8.

**What it does:** scan for Loop, Scan, Function, NonZero, Unique nodes. If
present and target opset is 10, emit FAIL.

**Implementation:** maybe already covered by opset-compliance check; verify
and extend if not. About 20 lines.

### Round 4: Cross-document methodology checks (out of scope for ONNX adapter, candidate for separate plugin)

These are not ONNX-graph checks; they verify NeuroGolf chain discipline at
the methodology level. Listed for completeness; recommend a separate
`furqan-lint-neurogolf` plugin rather than core ONNX adapter.

#### Check APE-PROVENANCE

**Origin:** NG-3 N1.

**What it does:** parse APE_REGISTER.md, extract each APE's claimed origin,
verify against dossier §9 canonical record (or the equivalent canonical
source).

**Why it matters:** NG-3 N1 caught APE-6 origin drift in cont60. Mechanical
provenance verification prevents future drift.

#### Check METHODOLOGY-FILES-PRESENT

**Origin:** NG-1 F5.

**What it does:** verify saved_list.txt, STATE.md, METHODOLOGY.md,
PRIMITIVES.md, APE_REGISTER.md exist at handoff tarball root.

**Why it matters:** F5 caught that cont46-cont59 dropped these. Prevention
via mechanical presence check.

#### Check CUMULATIVE-HANDOFF

**Origin:** NG-2 D6.

**What it does:** verify handoff tarball includes cumulative `solutions/`
directory unless explicit incremental-handoff is named.

**Why it matters:** D6 caught that cont59 broke the cumulative convention.

#### Check STANDING-RULE-1-EM-DASH

**Origin:** NG-2 Q2 (resolved strict).

**What it does:** grep for em-dash characters in NG documentation.

**Why it matters:** Standing Rule 1 inheritance for the NG chain. Currently
hand-enforced.

#### Check MARAD-CONSISTENCY

**Origin:** general BAF discipline.

**What it does:** verify each MARAD register entry has all five fields
(severity, diagnosis, location, minimal_fix, regression_check).

#### Check ROUND-NUMBERING-MONOTONIC

**Origin:** NG-2 D10.

**What it does:** verify NG-N round numbers are monotonic and that closure
ledgers reference each previous round explicitly.

## 4. Adoption sequence

### Phase 1 (recommend for furqan-lint v0.9.5 or v0.10.0)

Implement Round 1 checks: ARGMIN-WARN, EQUAL-FLOAT, IN-GRID-MASK-COVERAGE,
ORPHAN-INITIALIZERS. About 110 lines total. Low risk, high frequency of
firing on real bugs. Severity tier mostly LOW/MEDIUM.

### Phase 2 (v0.10.0 or v0.11.0)

Implement Round 2 checks: SAVED-LIST-Q0, NUMPY-DIVERGENCE-WITH-SIDECAR,
BUILD-SCRIPT-RELATIVE-PATH, BYTE-IDENTITY-REPRODUCER. About 190 lines total.
Requires sidecar contract formalization. Severity tier MEDIUM/HIGH; biggest
wins.

### Phase 3 (separate plugin, furqan-lint-neurogolf or equivalent)

Implement Round 3 + Round 4 as a NeuroGolf-specific plugin. About 500+ lines
total. Higher complexity, lower generality. Reserve until Phase 1 + 2 land
and the chain has accumulated more producer-side iterations to inform pattern
matching.

## 5. Sidecar contract proposal

For Round 2 checks to land, the NeuroGolf sidecar JSON contract should be
formalized. Cont53+ already ships sidecars with the following fields; this
plan codifies them as the canonical structure.

```json
{
  "task_uid": "string, ARC-AGI task hash like ba97ae07",
  "task_num": 268,
  "session": "cont63",
  "algorithm": "string, brief algorithm description",
  "description": "string, one-paragraph algorithm description",
  "score": 10.502,
  "macs": 339394,
  "memory": 1638084,
  "params": 2232,
  "all_correct": true,
  "opset": 10,
  "ir": 10
}
```

Optional Round 2 extensions:
- `expected_test_outputs`: list of expected one-hot output tensors for
  numpy_divergence verification (or pointer to ARC-AGI task file by `task_uid`)
- `replaces_save`: if this is a rebuild, the previous save's score (for
  REBUILD-DELTA check)
- `apes_invoked`: list of APE numbers this build's algorithm guards against
- `primitives_used`: list of P-NEW numbers this build invokes

## 6. Severity calibration philosophy

Per BAF v4.0 §3, severity is by impact on substrate, not by author intent.
Calibration for furqan-lint check severities:

- **HIGH:** check FAIL means the .onnx should not ship in current state.
  Examples: SAVED-LIST-Q0, OPSET10-BANNED-OPS, NUMPY-DIVERGENCE with sidecar.
- **MEDIUM:** check FAIL means the .onnx ships but should be documented;
  cleanup is desired. Examples: EQUAL-FLOAT, IN-GRID-MASK-COVERAGE,
  BUILD-SCRIPT-RELATIVE-PATH, BYTE-IDENTITY.
- **LOW:** check WARN/ADVISORY means hygiene/style issue; ship is acceptable.
  Examples: ARGMIN-WARN (Kaggle-valid even if local profile fails),
  ORPHAN-INITIALIZERS, STANDING-RULE-1-EM-DASH.

## 7. Empirical validation plan

Each proposed check should be validated against the cont33-cont63 substrate
to ensure it does not produce excessive false positives. Specifically:

1. **ARGMIN-WARN:** should fire on exactly 20 saves (the MARAD-10 cohort).
   If it fires on more, the check is over-broad. If less, the check missed
   a save.
2. **EQUAL-FLOAT:** should fire on zero saves currently shipping (since
   APE-5 was caught manually). Validates the check doesn't produce
   false positives on clean substrate.
3. **IN-GRID-MASK-COVERAGE:** should fire on ~5 saves where painting is the
   final step but in_grid_mask might be missing (heuristic, expect some
   false positives).
4. **ORPHAN-INITIALIZERS:** should fire on 93 of 334 saves per NG-1 F9.
   Validates the count.
5. **SAVED-LIST-Q0:** should fire on cont59 task293 retroactively (the
   regression-rebuild). Validates the check would have prevented F1.

## 8. Connection to BAF v4.0 reciprocal contract

The NG-1 audit caught F1 via fresh-instance reading of the substrate. The
proposed furqan-lint expansions move some of the fresh-instance discipline
into automated checks that run before fresh-instance audit is invoked. This
is structurally analogous to the cont60 NG-1 F2 closure: human-only gate
enforcement converted to automated CI gate. The audit chain remains
load-bearing for the structural-layer findings that automation cannot catch
(reciprocal contract drift, severity calibration, decorative-vs-structural
calibration), but the bug-shape-level findings move into the linter where
they fire on every save rather than waiting for the next NG round.

This is exactly the inversion the cont60 closure work demonstrated:
session-boundary discipline is not enough at chain length 25+. Tooling that
fires on every save catches the regression patterns; audit chain catches
the structural patterns that tooling cannot reach.

## 9. Open questions for principal review

**Q1 (sidecar contract):** is the JSON structure proposed in section 5
acceptable for canonical adoption? The cont53+ shipping sidecars already
follow it; the plan codifies but does not change.

**Q2 (Round 3 plugin separation):** should the NeuroGolf-specific algorithm
checks (PREFIX-MAX-RAY-DIRECTION, END-CELL-MASKING) live in core
furqan-lint or in a separate NeuroGolf plugin? Plugin separation preserves
furqan-lint's general-Python discipline; core inclusion preserves single-tool
ergonomics.

**Q3 (REBUILD-THRESHOLD calibration):** the SAVED-LIST-Q0 check defaults
REBUILD_THRESHOLD = 0.5. NG-2 Q3 marked this as v0 placeholder pending
empirical calibration. cont63 produced one save without rebuild data; the
calibration data set is still small. Defer until 2-3 rebuilds have happened.

**Q4 (verification cost ceiling):** Round 3 checks take significant
implementation effort (200-500 lines). Is the producer chain budget for
furqan-lint expansion sufficient, or should Round 3 wait until Phase 1 + 2
have been validated in production?

## 10. Closing note

The cont59-cont63 work demonstrated that the NeuroGolf chain at length 25+
sessions cannot rely on session-boundary discipline alone for structural
authorities. The cont60 closure execution shipped automated CI gates as the
substrate-level fix; this plan extends the same discipline to the ONNX
graph layer.

The reciprocal contract is preserved: the audit chain catches structural
findings that tooling cannot, and tooling catches the bug-shapes that audit
chains spend cycles re-discovering. Each plays its load-bearing role; neither
replaces the other.

Standing Rule 1 (no em-dashes) holds throughout this document.

End of plan.

---

# Bismillah ir-Rahman ir-Rahim
