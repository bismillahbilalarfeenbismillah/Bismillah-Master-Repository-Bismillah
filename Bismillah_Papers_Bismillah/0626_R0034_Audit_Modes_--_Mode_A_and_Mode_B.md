# Bismillah ir-Rahman ir-Rahim

# R0034 -- Audit Modes -- Mode A and Mode B

**Chronological Index:** 626 of 995  
**Date:** Undated  
**Section:** II. Analytical Frameworks & Methodology  
**Source File:** bayyinah_audit-modes.md  
**Source Format:** md  
**SHA-256:** `e35179a35628ac21462b4ce4eb3407470588d794f10b6d7fc323d4c83db635e4`  

---

## R0034 · Audit Modes -- Mode A and Mode B

- section: II. Analytical Frameworks & Methodology
- source_file: bayyinah_audit-modes.md
- source_format: md
- text_sha256: e35179a35628ac21462b4ce4eb3407470588d794f10b6d7fc323d4c83db635e4

# Audit Modes -- Mode A and Mode B

The methodology distinguishes two auditor operating modes based on the
auditor's access to the substrate-of-record.

## Mode A -- substrate verifier

**Definition:** Auditor has direct access to the substrate (git
repository checkout at pinned tag, file system access, ability to run
tools like `pytest --collect-only`, `grep`, `cat`, `git diff`).

**Canonical use cases:**

- T00 pre-flight (substrate-of-record reconciliation)
- First-cycle audits where substrate claims have not yet been verified
- Any audit where substrate-claim verification is load-bearing (e.g.,
  test-count gates, file-inventory verification, helper-symbol
  presence checks)
- Post-ship audits against actual shipped artifacts

**Strengths:**

- High-confidence substrate-claim verification
- Can directly cite line numbers from substrate
- Can verify "the prompt claims X; the substrate actually says Y" with
  reproducible evidence
- Can run pytest under the canonical full-extras profile and verify
  test counts

**Weaknesses:**

- Slower than Mode B (requires tool invocation per claim)
- Susceptible to overconfidence on surface checks if auditor neglects
  semantic / methodology-fidelity dimensions
- Requires git / tool access; not always available in fresh-instance
  contexts

**Empirical Mode A instances:**

- Round 36 (Perplexity) -- caught 3 CRITICAL substrate divergences in
  al-Mursalat v1.3
- Round 37 (Perplexity) -- caught 1 CRITICAL in v1.4
- Co-work T00 (Claude with git access) -- caught 3 MEDIUM substrate
  divergences (F-PF-1/2/3) in v1.6

## Mode B -- continuity reviewer

**Definition:** Auditor reviews the artifact (prompt, document,
deliverable) without direct substrate access; substrate inheritance is
single-sourced through the artifact's own restatement of substrate
facts.

**Canonical use cases:**

- Cross-instance re-audits (fresh Claude, fresh GPT-5, fresh Gemini
  loading the artifact from cold)
- Methodology-fidelity checks (em-dash policy, brand canonical,
  severity uppercase, six-element findings format)
- Narrative-vs-body propagation gap detection
- Cross-cutting compliance checks across an artifact
- Mechanical-traceability verification (did the absorption cycle
  follow the prior audit's prescribed routes?)

**Strengths:**

- Strong on internal-consistency checks
- Strong on format-compliance and methodology-fidelity
- No tool dependency; works in any LLM context
- Best-suited to detecting absorption-induced regression at retired
  surfaces (the PMD v1.2 candidate finding mechanism)

**Weaknesses:**

- Reduced confidence on substrate-claim verification
- Susceptible to absorbing substrate errors from the artifact's
  restatement (single-sourced substrate inheritance)
- Cannot independently verify "the prompt claims X; what does
  substrate actually say?"

**Empirical Mode B instances:**

- Round 38 (Claude) -- caught 1 HIGH + 4 MEDIUM + 2 LOW in v1.5
- Round 38.5 (Fraz + fresh Claude) -- caught 1 HIGH + 2 MEDIUM + 2 LOW
  in v1.7; reduced-confidence Mode B due to absent T00 substrate record
- Round 38.5 v1.8 (Perplexity) -- caught 0 findings in v1.8;
  Mode B continuity review with Mode A spot-verification at tag
  eb24408

## Mixed-mode and Mode B with spot-verification

The Round 38.5 v1.8 audit illustrates a productive variant:

- Primary mode: Mode B continuity review (verify F-PA findings
  absorbed; verify cross-cutting compliance)
- Spot-verification: Mode A for specific load-bearing claims (verify
  F-PA-3 four-surface alignment by reading paste.txt lines 2984-3134
  directly)

This recovers Mode A confidence on the few claims that need it without
the time cost of full Mode A re-walk.

## Mode selection rule

| Context | Recommended mode |
|---|---|
| T00 pre-flight | Mode A (mandatory) |
| First-cycle audit, substrate not yet verified | Mode A |
| Cross-instance re-audit, prior cycle established substrate | Mode B |
| Mechanical-traceability verification | Mode B |
| Format-compliance / methodology-fidelity check | Mode B |
| Test-count gate verification | Mode A |
| Post-ship audit against shipped artifact | Mode A |
| Full-chain meta-audit | Mode B (Gemini-suited) |

## Confidence annotation

Every audit deliverable must annotate the mode explicitly:

> Auditor operated in Mode A with direct git access at tag
> `cac6917`. Substrate-claim verification confidence high.

OR

> Auditor operated in Mode B with single-sourced substrate inheritance
> through the artifact's restatement of T00 record. Substrate-claim
> verification confidence reduced. Recommend downstream Mode A
> re-audit before ship.

Confidence annotation is itself a finding when absent.

## Absorption-induced regression -- a Mode B failure mode

PMD v1.2 §X documents a specific Mode B failure mode caught by Round
38.5: **absorption of new substrate truth can resurface a previously-
retired contradiction sharing a surface**.

Example: v1.6 retired F-TR-6 (alphabetical ordering claim) as a
methodology finding. v1.7 absorbed F-PF-1 (substrate-actual file count
is 16 with alphabetical ordering). The two surfaces collided in T05's
code block, producing F-PA-3 HIGH (alphabetical-vs-end-append four-
surface contradiction).

The lesson: Mode B auditors must check whether new substrate absorptions
resurface previously-retired contradictions. Add to audit checklist:

> For each retired finding in the chain history, verify the current
> artifact does not resurface its surface. Cross-reference retired-
> finding ID in audit notes.

---

# Bismillah ir-Rahman ir-Rahim
