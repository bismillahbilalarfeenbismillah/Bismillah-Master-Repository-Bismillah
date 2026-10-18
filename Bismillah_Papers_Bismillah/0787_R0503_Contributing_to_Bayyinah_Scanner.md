# Bismillah ir-Rahman ir-Rahim

# R0503 -- Contributing to Bayyinah Scanner

**Chronological Index:** 787 of 995  
**Date:** Undated  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** CONTRIBUTING.md  
**Source Format:** md  
**SHA-256:** `8e737ec0c7ed0425ab94b87faa55c6c57c9b68feb56eb050347325eaa60ffff0`  

---

## R0503 · Contributing to Bayyinah Scanner

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: CONTRIBUTING.md
- source_format: md
- text_sha256: 8e737ec0c7ed0425ab94b87faa55c6c57c9b68feb56eb050347325eaa60ffff0

# Contributing to Bayyinah Scanner

Bayyinah is authored against the canonical v1.6 FINAL coding strategy under the Fatiha Construct. The strategy is the contract; this file is the operational guide.

## Before you contribute

Read these three documents in order:

1. `README.md` for release identity and tag status
2. `BOUNTY.md` for the falsification bounty scope and 14-day SLA
3. `ANNOUNCEMENT.md` for what v2.0 IS NOT

If your contribution is a counterexample (false negative, false positive, cross-port disagreement, canonical-schema instability), file it via the `Falsification bounty submission` issue template, not as a pull request.

## Setup

```bash
git clone <repo url>
cd bayyinah
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev,f1]"
```

## Run the tests

```bash
# Regenerate fixture corpora
for s in scripts/generate_fixtures_v*.py scripts/generate_fp_fixtures.py; do
  PYTHONPATH=src python3 "$s"
done

# Unit tests
PYTHONPATH=src python3 -m pytest tests/ -q

# F1-F16 regression harnesses
for h in f1 f2 f3 f4 f5 f6 f7 f8 f9 f10 f11 f12_1 f12_2 f12_3 f13 f14 f15 f16; do
  PYTHONPATH=src python3 scripts/run_${h}_evaluation.py
done

# F-MASTER aggregate decision
PYTHONPATH=src python3 scripts/run_fmaster_evaluation.py
```

All harnesses must PASS (or PREP, for F-MASTER) before any PR is merged.

## Disciplines (load-bearing)

These are not stylistic preferences. They are the canonical disciplines that the framework's structural-honesty claim rests on.

### Em-dash policy (§9.5)

Em-dashes (U+2014) and en-dashes (U+2013) are forbidden in user-facing prose: READMEs, error messages, finding `witness` text, BOUNTY.md, ANNOUNCEMENT.md, CHANGELOG.md, CONTRIBUTING.md.

Code comments and CSS comments are exempt. Use `--` (double hyphen with spaces around it) where you would otherwise use an em-dash.

### Patent invariant

Five components are explicitly immutable across all releases:

1. The analyzer registry mechanism
2. The layer-classification discipline (ZAHIR / BATIN)
3. The producer-signature calibration component
4. The verdict aggregator's five-verdict structure
5. The witness emitter

A PR that modifies any of these is rejected at review. Extensions are ADDITIVE only (new finding codes, new extractor pairs, new metadata fields with default `None`).

### Dependency manifest discipline

New third-party imports go in BOTH `requirements.txt` AND `pyproject.toml` in the same patch, capped at the current major version.

### MDL discipline (fill gaps before expanding scope)

Before proposing a new extractor or format support, verify that existing extractors have full coverage of their declared finding codes against both clean and divergent corpora.

### Audit attribution

The Bayyinah audit chain is audit-of-self by Bilal Syed Arfeen. Cross-vendor adjudications are recorded by vendor instance; never as substitute author. PRs that misattribute authorship are rejected.

### ZAHIR/BATIN single-walk classification

`Finding.layer_classification` is set by a single-walk surface-readability test for source-layer classification, independent of which analyzer module hosts the call. A PR that introduces a multi-pass classifier is rejected.

## Pull request template

Use the PR template at `.github/PULL_REQUEST_TEMPLATE.md`. Every checkbox must be checked or explicitly justified.

## Commit hygiene

- One logical change per commit
- Subject line ≤ 72 characters
- Body explains the WHY, not the WHAT
- Reference the strategy phase + F-block if applicable: `Phase 3.2 F11`

## When you are stuck

The framework's structural-honesty discipline applies to contributor work as much as producer work. If your PR introduces complexity, ask explicitly: is this complexity FRaZ-earned (Roadmap Risk-justified) or scope-creep? Cow Episode warnings exist in every release for a reason; if you find yourself enumerating every variant, you are violating the Cow Episode for that release.

## Closing dua

> Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.
> (Our Lord, accept this from us. Indeed, You are the All-Hearing, the All-Knowing.)

---

# Bismillah ir-Rahman ir-Rahim
