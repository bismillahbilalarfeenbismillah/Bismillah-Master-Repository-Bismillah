# Bismillah ir-Rahman ir-Rahim

# R0057 -- Methodology Foundations -- PMD v1.2

**Chronological Index:** 227 of 995  
**Date:** 2026-05-10  
**Section:** II. Analytical Frameworks & Methodology  
**Source File:** PMD_v1_2_BAF_v3_0.md  
**Source Format:** md  
**SHA-256:** `e337cc7d9d41c0cbe199b688f08f437b2fb9927a67f73a340ff6800004586973`  

---

## R0057 · Methodology Foundations -- PMD v1.2

- section: II. Analytical Frameworks & Methodology
- source_file: PMD_v1_2_BAF_v3_0.md
- source_format: md
- text_sha256: e337cc7d9d41c0cbe199b688f08f437b2fb9927a67f73a340ff6800004586973

# Methodology Foundations -- PMD v1.2

**Source:** Predictive Modeling Discipline (PMD) v1.2; Bayyinah Audit
Framework v3.0 (Zenodo DOI 10.5281/zenodo.20017335).

**Authors:** Bilal Syed Arfeen, Fraz Ashraf (BayyinahEnterprise).

## §0. Framing

The BayyinahEnterprise audit methodology checks whether software,
documents, and AI-generated artifacts are **honest about what they do**.
Not whether they are correct -- existing tools (linters, type checkers,
security scanners, fuzzers) cover correctness. Whether they keep the
promises they make.

The defects we detect are **structural, not syntactic**. A function
claims to return patient data but sometimes silently returns nothing. A
public API had ten functions last week and nine this week with no
notice. A document shows a $2,450 invoice but contains a hidden layer
with $245,000. These are honesty failures: the system's surface claims
diverge from its substrate behavior.

## §0.1 Surface vs substrate

Every artifact has two layers:

- **Surface:** what the artifact claims, advertises, documents, or
  promises (function signatures, docstrings, public APIs, displayed
  invoice amounts, README claims).
- **Substrate:** what the artifact actually does (function bodies,
  control flow, hidden PDF layers, actual test counts).

An artifact is **structurally honest** when surface and substrate match.
A finding is a documented surface-substrate divergence.

## §0.2 Standing rules (cross-cutting)

These rules apply across every audit cycle, every role, every artifact:

1. **Em-dash policy** -- no `--`-em characters; use `--` double hyphen.
   In LaTeX, the `---` ligature must also become `--` outside legitimate
   Markdown horizontal rules.
2. **Brand canonical** -- "BayyinahEnterprise" no space.
3. **Severity uppercase** -- CRITICAL, HIGH, MEDIUM, LOW.
4. **Six-element findings format** -- ID + severity + locus + substance
   + disposition + cross-reference.
5. **Substrate-of-record uniqueness** -- each fact stated once.
6. **Audit-chain immutability** -- append-only ledger; historical
   preservation cells never edited retroactively (only annotated with
   cross-references per Bayyinah Audit Framework v3.0 §14.5).
7. **Cross-vendor rotation** -- producer-instance excluded from auditor
   pool; tier-weighted consensus.
8. **Time discipline** -- estimates inflated 75% to match reality.

## §0.3 The six-stage lifecycle (engineering-discipline import)

From Fraz Ashraf's power-systems engineering background (renewable
energy, BESS, EV charging, micro-grid; standards IEC 61508, IEEE 1547):

1. **Pre-flight** -- substrate-of-record reconciliation before any
   intervention (T00 pattern).
2. **Author** -- producer-instance creates the artifact (Claude
   typically; other vendors acceptable).
3. **Audit** -- auditor-instance executes Mode A or Mode B verification
   under cross-vendor rotation.
4. **Adjudicate** -- if multiple auditors disagree, adjudicator applies
   PMD v1.2 cross-vendor rules.
5. **Absorb** -- producer-instance generates next version absorbing
   audit findings under disposition-prescribed routes; mechanical-
   traceability discipline preserved.
6. **Ledger** -- append-only record of the cycle; immutability discipline
   enforced.

The cycle iterates until convergence (zero CRITICAL findings; HIGH
narrows monotonically; MEDIUM and LOW tracked but not blocking).

## §0.4 Convergence definition

A chain has **converged** when:

- Two consecutive cross-vendor rounds produce 0 CRITICAL findings
- HIGH residual is 0 or accompanied by a project-lead-signed exception
  ledger entry
- MEDIUM and LOW findings are either absorbed or moved to "future
  reference" with explicit non-operative annotation
- All standing-rule compliance checks pass (em-dash, brand, severity,
  six-element format, substrate uniqueness)

Convergence is not the same as completion. Convergence permits ship;
new rounds may surface new findings at any time.

## §0.5 Six absorption candidates -- v1.1 -> v1.2 (this version)

PMD v1.2 absorbed six methodology surfaces previously surfaced as
findings during the al-Mursalat audit chain (Rounds 36-38.5):

1. **Absorption-induced regression at retired surfaces** -- when new
   substrate truth resurfaces a previously-retired contradiction
   sharing a surface, both must be re-examined as a pair. See
   `references/audit-modes.md` and the Round 38.5 worked example.
2. **Bulk-substitution automation immutability risk** -- automated
   find-and-replace operations may inadvertently edit historical
   preservation cells; §14.5 immutability discipline prohibits this
   without explicit ADR.
3. **Narrative-vs-body propagation gap detection** -- framing
   summaries and section bodies must propagate the same arithmetic;
   gap detection is an explicit auditor sub-task.
4. **Stale sub-verification subtask retirement** -- once a verification
   task is resolved (e.g., Co-work T00 §7b confirms helper absent),
   the resolved state is the canonical statement; PRESENT/ABSENT
   branching moves to "for future reference."
5. **Mechanical-traceability exception** -- when an absorption cycle
   exclusively executes prior audit's disposition-prescribed routes
   with zero architectural latitude, cross-instance re-audit is
   recommended-but-not-blocking; project-lead signoff suffices.
6. **Lane-execution discipline** -- methodology specifies producer /
   auditor / adjudicator roles AND execution lanes (skill bundle, CI,
   cross-vendor validator, MCP server). Lanes are the canonical
   execution substrate; producer / auditor / adjudicator are the
   canonical role substrate.

## §0.6 Empirical record

The methodology was empirically validated across 38.5 audit rounds on
three repositories between April 20 and May 10, 2026. Severity
narrowing curve:

| Round | Repo focus | CRITICAL | HIGH | MEDIUM | LOW |
|---|---|---|---|---|---|
| Round 31 | as-Saff v0.11.7 | 3 | -- | -- | -- |
| Round 32 | as-Saff F10-F13 | 1 | -- | -- | -- |
| Round 36 | al-Mursalat v1.3 | 3 | 0 | 0 | 0 |
| Round 37 | al-Mursalat v1.4 | 1 | 0 | 0 | 0 |
| Round 38 | al-Mursalat v1.5 | 0 | 1 | 4 | 2 |
| T00 (Mode A) | al-Mursalat v1.6 | 0 | 0 | 3 | 0 |
| Round 38.5 | al-Mursalat v1.7 | 0 | 1 | 2 | 2 |
| Round 38.5 v1.8 | al-Mursalat v1.8 | 0 | 0 | 0 | 0 |

CRITICAL convergence at Round 38 holds through v1.8 ship. HIGH residual
was the load-bearing surface in Rounds 38 and 38.5; v1.8 closes it.

## §0.7 What this skill does

Loads the above into Claude's working context so that any operation
under this skill -- producing, auditing, or adjudicating -- inherits
the methodology automatically rather than requiring re-statement in
every prompt.

---

# Bismillah ir-Rahman ir-Rahim
