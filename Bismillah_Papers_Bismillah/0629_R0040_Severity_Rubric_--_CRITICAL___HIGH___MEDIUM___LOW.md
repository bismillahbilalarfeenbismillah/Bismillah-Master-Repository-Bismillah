# Bismillah ir-Rahman ir-Rahim

# R0040 -- Severity Rubric -- CRITICAL / HIGH / MEDIUM / LOW

**Chronological Index:** 629 of 995  
**Date:** Undated  
**Section:** II. Analytical Frameworks & Methodology  
**Source File:** bayyinah_severity-rubric.md  
**Source Format:** md  
**SHA-256:** `d756564a3aed9e7601f005cccd9832a0e9a4533059a4eaeb75df53e8206492ff`  

---

## R0040 · Severity Rubric -- CRITICAL / HIGH / MEDIUM / LOW

- section: II. Analytical Frameworks & Methodology
- source_file: bayyinah_severity-rubric.md
- source_format: md
- text_sha256: d756564a3aed9e7601f005cccd9832a0e9a4533059a4eaeb75df53e8206492ff

# Severity Rubric -- CRITICAL / HIGH / MEDIUM / LOW

Severity is uppercase, always. Calibration is empirical, drawn from
Rounds 31 through 38.5.

## CRITICAL

The finding renders the artifact unfit to ship. Examples from the
empirical record:

- Substrate verification reveals the artifact's load-bearing claim is
  factually wrong (e.g., Round 36 caught three CRITICAL substrate-
  divergence findings where the prompt's enumerated test count did not
  match pytest-collected count under canonical full-extras profile).
- Public API removal without ADR (al-Hujurat T05 CHANGELOG-math gate
  violation; ship would break downstream consumers).
- Hidden PDF layer carrying a different financial figure than the
  visible surface (canonical Bayyinah Scanner case).
- Producer-instance auditor cycle (producer audits its own output) --
  audit invalid; methodology violation.

Disposition for CRITICAL findings: **HALT-and-escalate to project lead**.
Do not propose absorption routes; the project lead decides whether to
re-author from scratch, escalate to substrate-correction first, or
amend methodology.

## HIGH

The finding blocks ship but is locally resolvable. Examples from the
empirical record:

- Round 38 (al-Mursalat v1.5) surfaced one HIGH on cross-text claim
  scope (prompt claimed "across all mushaf chains" when substrate
  evidence was only al-Mursalat).
- Round 38.5 (al-Mursalat v1.7) surfaced F-PA-3 HIGH on T05 four-
  surface contradiction (alphabetical-vs-end-append; absorption-induced
  regression).

Disposition for HIGH findings: **specific prescribed route with all
surfaces aligned**. Auditor must enumerate every surface (code block,
comment, fixture #1, fixture #3, etc.) that requires correction.
Absorption cycle executes the route; next audit cycle verifies all
surfaces aligned.

## MEDIUM

The finding does not block ship but degrades methodology fidelity.
Examples from the empirical record:

- F-PA-1 MEDIUM (Round 38.5): retroactive editing of v1.6 historical
  preservation cells; immutability discipline violation; absorption
  route is "restore v1.6 archived values verbatim plus inline v1.7
  cross-reference."
- F-PA-2 MEDIUM (Round 38.5): §0 framing arithmetic absent; absorption
  route is "insert framing test-count summary sentence with full
  derivation."
- F-PF-1 MEDIUM (Co-work T00): substrate-actual file count is 16, not
  14 as the prompt claimed.

Disposition for MEDIUM findings: **absorption-route prescribed but
ship-permissive**. Findings can ship into the next version provided
they are documented in the v1.x -> v1.x+1 appendix. The cycle should
not ship to production with open MEDIUM findings, but can ship to
internal next-version absorption.

## LOW

The finding is a polish or hygiene matter. Examples from the empirical
record:

- F-PA-4 LOW (Round 38.5): T02.0 sub-verification subtask presents
  helper-symbol resolution as pending when Co-work T00 §7b already
  confirmed both absent; staleness, not error.
- F-PA-5 LOW (Round 38.5): missing `import sys` in T02 Edit 3a/3b
  imports block.
- Severity in sentence case ("High" instead of "HIGH").
- Findings-format compliance gaps (missing cross-reference, generic
  locus).

Disposition for LOW findings: **prescribed route stated; absorption
optional in next cycle, mandatory before ship**. LOW findings accumulate
across rounds; project lead may batch-absorb at version-boundary.

## Severity boundary calibration

When unsure between two bands, consult these decision rules:

- **CRITICAL vs HIGH:** would shipping cause user-visible harm
  (security incident, data loss, regulatory violation, public API
  break)? CRITICAL. Otherwise HIGH.
- **HIGH vs MEDIUM:** does the finding require all surfaces to be
  corrected before the artifact is internally consistent? HIGH.
  Otherwise MEDIUM.
- **MEDIUM vs LOW:** is the finding a methodology-fidelity matter
  (substrate / immutability / framing)? MEDIUM. Is it surface polish
  (formatting / missing imports / stale notes)? LOW.

## Severity reconciliation under cross-vendor disagreement

When multiple LLM auditors disagree on severity for the same finding:

- **One-band disagreement** (HIGH vs MEDIUM): adopt the higher severity
  and annotate "severity-debated; lower bound MEDIUM per vendor X."
- **Two-band-or-more disagreement** (CRITICAL vs LOW): treat as
  contradiction; HALT and escalate to project lead. Two-band
  disagreement usually indicates one vendor misread the locus.

## Monotonic narrowing expectation

Across iterative rounds, severity counts should narrow monotonically:

- CRITICAL count must be non-increasing across consecutive rounds; an
  increase is itself a methodology finding.
- HIGH count may oscillate (absorption can resurface previously-retired
  surfaces; see PMD v1.2 absorption-induced regression).
- MEDIUM and LOW counts may grow during expansion phases (new prompt
  surface area introduces new polish opportunities) and narrow during
  absorption phases.

Convergence is reached when two consecutive cross-vendor rounds produce
0 CRITICAL and 0 HIGH (with optional project-lead-signed exception
ledger for residual HIGH).

---

# Bismillah ir-Rahman ir-Rahim
