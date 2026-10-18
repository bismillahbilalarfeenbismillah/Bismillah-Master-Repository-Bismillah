# Bismillah ir-Rahman ir-Rahim

# R0037 -- Cross-Vendor Rotation Discipline

**Chronological Index:** 226 of 995  
**Date:** 2026-05-10  
**Section:** II. Analytical Frameworks & Methodology  
**Source File:** bayyinah_cross-vendor-rotation.md  
**Source Format:** md  
**SHA-256:** `ad37708029ec6bdc4a36012de060e7c04688a7a0c2fce92a37ed9fdcc8d9b785`  

---

## R0037 · Cross-Vendor Rotation Discipline

- section: II. Analytical Frameworks & Methodology
- source_file: bayyinah_cross-vendor-rotation.md
- source_format: md
- text_sha256: ad37708029ec6bdc4a36012de060e7c04688a7a0c2fce92a37ed9fdcc8d9b785

# Cross-Vendor Rotation Discipline

## Rationale

A producer-instance auditing its own output is a methodology violation
of the highest order. The methodology requires producer / auditor
separation, and the strongest separation available is **cross-vendor
rotation**: the auditor runs on a different LLM (different model
family, different training data, different RLHF lineage) than the
producer.

## Tier classification

Per the May 10, 2026 third-auditor-LLM decision, four-vendor coverage
splits into two tiers:

### Tier 1 -- per-round cross-instance auditors

Strong methodology adherence under structured prompts; strong
adversarial residual hunting; high instruction-fidelity on the
methodology's rule density.

- **Claude** (Anthropic) -- canonical producer in BayyinahEnterprise
  workflow; also serves as auditor when producer is non-Claude
- **GPT-5** (OpenAI) -- recommended third Tier 1 auditor; orthogonal
  failure modes from Claude; strong instruction-adherence on rule sets
- **Perplexity** (Perplexity AI; computer-tool-augmented) -- load-
  bearing Mode A substrate verifier; direct git/web/tool access

### Tier 2 -- specialized roles

Strong on different axes; reserve for specific cells rather than
per-round rotation.

- **Gemini** (Google) -- long-context recall at 100K+ tokens; cross-
  document gestalt synthesis; full-chain meta-audits at mushaf-chain
  ship boundaries and PMD revision boundaries
- **Grok** (xAI) -- supplementary surface for Lane 3 fan-out; useful
  for adversarial / contrarian framings

## Vote weighting

In Lane 3 cross-vendor adjudication:

| Vendor | Consensus weight | Unique-finding weight |
|---|---|---|
| Claude | 1.0 | 1.0 |
| GPT-5 | 1.0 | 1.0 |
| Perplexity | 1.0 | 1.0 |
| Gemini | 0.5 | 1.0 |
| Grok | 0.5 | 1.0 |

**Consensus weight** affects whether a finding clears the consensus
threshold (>= 2.0 total weight = finding stands).

**Unique-finding weight** treats every vendor's unique findings as
equally surfaceable; project lead disposes individually.

## Rotation rule

Formal rule for per-round auditor selection:

> The per-round cross-instance auditor must differ from the prior
> round's auditor AND from the producer instance. Selection from
> {Perplexity, GPT-5} when Claude was producer; selection from
> {Perplexity, GPT-5, Claude} when producer was non-Claude.

Gemini gets a separate clause:

> Full-chain meta-audit invoked at mushaf-chain ship boundary AND PMD
> revision boundary. Not in the per-round rotation.

## Producer-instance exclusion

If the artifact under audit was produced by Claude:

- Claude is excluded from the auditor pool for that audit, OR
- Claude is relegated to advisory-only role (cannot HALT or assign
  CRITICAL / HIGH severities; can flag for human review)

Same rule applies symmetrically: any producer is excluded as auditor
of its own output.

## Same-instance §0.1 named exception

When an absorption cycle is **mechanically traceable** from the prior
audit's remediation checklist:

- No architectural latitude exercised
- No new content beyond what the prior audit's recommended-remediation
  paragraphs specify
- Every absorbed finding maps to an explicit prescribed route

...then cross-instance re-audit is recommended-but-not-blocking;
project-lead signoff suffices.

**Test for mechanical traceability:** did the absorption cycle add ANY
content beyond the remediation checklist? Binary check:

- If yes: cross-instance audit is blocking
- If no: §0.1 exception applies; project-lead signoff suffices;
  optional cross-instance audit recommended for hygiene

The al-Mursalat v1.8 cycle was the first to qualify under §0.1
(Round 38.5 -> v1.8 absorption was pure mechanical execution).

## Audit-modes by tier

| Tier | Mode A capability | Mode B capability | Typical role |
|---|---|---|---|
| Claude | Limited (no direct git in standard env) | Strong | Producer; continuity reviewer |
| GPT-5 | Limited | Strong | Per-round cross-instance auditor |
| Perplexity | Strong (tool-augmented) | Strong | Mode A substrate verifier; per-round cross-instance auditor |
| Gemini | Limited | Strong (long-context) | Full-chain meta-audit |
| Grok | Limited | Moderate | Supplementary surface |

Lane 3 cross-vendor validator (under construction) productizes the
parallel-fan-out pattern: all Tier 1 + Tier 2 vendors invoked
simultaneously, adjudication engine applies the rules above.

## Empirical record

Rotation actually executed across the al-Mursalat chain (Rounds 36-38.5):

- Round 36: Perplexity (Mode A substrate verifier)
- Round 37: Perplexity (Mode A; same-vendor consecutive permitted only
  when no other vendor available; flagged in audit deliverable)
- Round 38: Claude (Mode B continuity review; cross-instance)
- Co-work T00: Claude (Mode A substrate verifier via Co-work git
  access; sub-instance, distinct from Round 38 Claude)
- Round 38.5: Fraz + fresh Claude (Mode B with reduced confidence; the
  human-LLM hybrid arm)
- Round 38.5 v1.8: Perplexity (Mode B continuity review with Mode A
  spot-verification via direct git access at tag eb24408)
- Round 39 (post-v0.12.0 ship): pre-registered as Perplexity Mode A,
  recommended for Lane 3 productization once Phase 3 ships

## Why Gemini Tier 2, not Tier 1

Two reasons:

1. Gemini tends to drift into verbose narrative when prompts get long;
   the methodology is rule-dense and short-leash instruction adherence
   matters more than gestalt synthesis at per-round granularity.
2. Gemini's gestalt-synthesis strength is best deployed at the
   full-chain meta-audit boundary, where the question is "do all eight
   mushaf chains tell a coherent story" rather than "did this prompt
   absorb the prior audit's findings."

Gemini in Tier 1 would waste its strengths on per-round work where
GPT-5 outperforms it on instruction adherence. Gemini in Tier 2 puts
it where it's actually best.

## Why Grok Tier 2, not excluded

Grok is included rather than excluded because:

1. xAI's training lineage is genuinely orthogonal to Anthropic /
   OpenAI / Google; vendor diversity is a feature.
2. Adversarial / contrarian framings sometimes surface findings other
   vendors smooth over.

Grok is half-weighted because its instruction-fidelity on rule-dense
prompts is more variable than Tier 1 vendors. Half-weight prevents a
single Grok finding from clearing consensus alone.

---

# Bismillah ir-Rahman ir-Rahim
