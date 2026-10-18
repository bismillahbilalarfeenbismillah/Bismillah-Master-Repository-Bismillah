# Bismillah ir-Rahman ir-Rahim

# R0041 -- Substrate-of-Record Discipline

**Chronological Index:** 630 of 995  
**Date:** Undated  
**Section:** II. Analytical Frameworks & Methodology  
**Source File:** bayyinah_substrate-of-record.md  
**Source Format:** md  
**SHA-256:** `0609cc0e02a72c6fd4f9aa4840ef012578f269e203cef64f3e01047e8e6e24df`  

---

## R0041 · Substrate-of-Record Discipline

- section: II. Analytical Frameworks & Methodology
- source_file: bayyinah_substrate-of-record.md
- source_format: md
- text_sha256: 0609cc0e02a72c6fd4f9aa4840ef012578f269e203cef64f3e01047e8e6e24df

# Substrate-of-Record Discipline

## Definition

**Substrate-of-record** is the canonical authoritative state of the
artifact under audit at a specific point in time. It is the answer
to: "what does the code / document / prompt actually look like at
commit SHA X / version Y / tag Z?"

## Why it matters

Every audit cycle begins with a claim about the artifact. Without a
shared substrate-of-record, two auditors examining the same artifact
may arrive at contradictory conclusions because they examined
different versions. The substrate-of-record makes this impossible.

The methodology requires:

1. **Pinning.** Every audit cycle names the substrate-of-record by
   commit SHA, tag, version, or filename + hash. No audit operates
   against "the latest version" or "the current state."
2. **Uniqueness.** Each fact about the substrate is stated once in its
   canonical position. The prompt does not state "the test count is
   618" in one section and "the test count is 644" in another. If
   both are needed (e.g., baseline vs projection), each is stated
   once, with explicit naming ("v0.11.8 baseline: 618; v0.12.0
   projection: 644").
3. **Reconciliation.** Before any intervention, the auditor verifies
   the prompt's substrate claims against the actual substrate. This
   is the **T00 pre-flight** pattern, described below.

## T00 pre-flight pattern

T00 (test zero) is the substrate-of-record reconciliation step that
precedes any intervention. The canonical structure:

### T00 step 1: substrate identification

State the substrate-of-record explicitly:

- Repository: `BayyinahEnterprise/furqan-lint`
- Tag or commit: `v0.11.8` at SHA `cac6917`
- Profile (if applicable): canonical full-extras
  `[dev,gate11,rust,onnx,onnx-runtime,onnx-profile]`

### T00 step 2: substrate facts enumeration

List the substrate facts the prompt depends on, with citations:

- File count: `_CHECKER_SOURCE_FILES` has 16 entries
- verification.py line count: 618
- `verify` function at line 556
- `_LANGUAGE_DISPATCH` at lines 594-597 (construction) and 599-606
  (consumption)
- Test count: 618 collected under canonical full-extras profile per
  CHANGELOG `### Tests` block

### T00 step 3: divergence detection

Cross-check each prompt claim against the actual substrate. Surface
divergences as F-PF-N findings (pre-flight namespace).

Example divergences from al-Mursalat T00 (Co-work execution):

- F-PF-1 MEDIUM: prompt claimed 14-entry inventory; substrate-actual
  is 16 entries.
- F-PF-2 MEDIUM: prompt claimed cmd_check_gate11 signature
  `(args: list[str])`; substrate-actual is `(directory: Path, opts:
  dict[str, object])`.
- F-PF-3 MEDIUM: prompt missing goast source path pin
  (`src/furqan_lint/go_adapter/cmd/goast/main.go`).

### T00 step 4: substrate-conditional handling

For findings where substrate may evolve, document conditional handling:

- If helper X is PRESENT at substrate: do A
- If helper X is ABSENT at substrate: do B (current state per T00 §7b)
- If both PRESENT: do C (future-reference branching)

### T00 step 5: project-lead disposition

Three routes when T00 surfaces findings:

- **Route A:** amend prompt before dispatch (project lead authors
  v1.x+1 absorbing the F-PF findings)
- **Route B:** dispatch with carry-forward (F-PF findings noted; next
  cycle absorbs)
- **Route C:** halt and re-substrate (substrate may be wrong; pre-flight
  reveals the issue)

## Substrate-of-record uniqueness violations

Common patterns that violate uniqueness:

### Pattern 1: Settled and pending duplication

The prompt states a fact as both "resolved" and "still pending."
Example (F-PA-4 from Round 38.5):

> T02.0 sub-verification subtask presents helper-symbol resolution as
> pending PRESENT/ABSENT branching when Co-work T00 §7b already
> confirmed both helpers ABSENT.

**Absorption route:** state the resolved state directly; move
PRESENT/ABSENT branching to a "for future reference" subsection
explicitly marked NOT operative at current substrate.

### Pattern 2: Narrative-vs-body propagation gap

Framing summary states one number, section body states another.
Example (F-PA-2 from Round 38.5):

> §0 framing test-count arithmetic line absent; section bodies state
> the test counts but the framing summary does not propagate them.

**Absorption route:** insert framing test-count summary sentence with
full derivation (`X baseline + delta = Y projection`) and CHANGELOG
cross-reference.

### Pattern 3: Bulk-substitution immutability violation

Automated find-and-replace edits historical preservation cells that
were already shipped under a DOI / commit SHA. Example (F-PA-1 from
Round 38.5):

> v1.6's historical preservation block (F-TR-1 entry) was edited from
> its v1.6-shipped values to v1.7-corrected values, violating §14.5
> attribution-corrective immutability.

**Absorption route:** restore v1.6's archived values verbatim; add
inline v1.7 cross-reference annotation per §14.5 (annotation, not
edit).

## Mode A vs Mode B operating modes

Two auditor operating modes under this discipline:

### Mode A -- substrate verifier

The auditor has direct access to the substrate (git access, file
system access, repository checkout at the pinned tag). Mode A
findings are typically high-confidence because the auditor can
verify substrate claims directly.

Mode A is the canonical mode for T00 pre-flight, for first-cycle
audits, and for any cycle where substrate-claim verification is
load-bearing.

### Mode B -- continuity reviewer

The auditor reviews the artifact (prompt, document, deliverable)
without direct substrate access; substrate inheritance is single-
sourced through the artifact's restatement. Mode B findings are
typically lower-confidence on substrate-claim verification but
higher-confidence on internal-consistency, format-compliance, and
narrative-vs-body propagation.

Mode B is the canonical mode for cross-instance re-audits, for
methodology-fidelity checks, and for any cycle where the goal is
verifying the artifact, not verifying the substrate.

## Cross-instance rotation discipline

To prevent producer-instance self-audit (a methodology violation),
auditors rotate across LLM vendors. Round-by-round:

- Round N producer: Claude
- Round N+1 auditor: must NOT be Claude (Perplexity, GPT-5, or Gemini)
- Round N+2 auditor (if needed): must NOT be the Round N+1 auditor

Tier weighting (per PMD v1.2 §X cross-vendor adjudication rules):

- Tier 1 (Claude, GPT-5, Perplexity): full vote weight in consensus
  calculations
- Tier 2 (Gemini, Grok): half vote weight in consensus; full weight
  for unique-finding surfacing

## Materials gap

When an auditor lacks direct substrate access AND the prompt's
substrate restatement is single-sourced, the auditor is operating in
**reduced-confidence Mode B**. The audit deliverable must state this
explicitly:

> Auditor operated in Mode B with single-sourced substrate inheritance.
> Substrate-claim verification confidence reduced. Recommend
> downstream Mode A re-audit before ship.

Round 38.5 (Fraz + fresh Claude) operated in reduced-confidence Mode B
and was followed by Round 38.5 v1.8 (Perplexity with Mode A spot-
verification via direct git access) to recover confidence.

---

# Bismillah ir-Rahman ir-Rahim
