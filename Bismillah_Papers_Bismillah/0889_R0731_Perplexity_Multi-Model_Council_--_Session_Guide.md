# Bismillah ir-Rahman ir-Rahim

# R0731 -- Perplexity Multi-Model Council -- Session Guide

**Chronological Index:** 889 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** PERPLEXITY_SESSION_GUIDE.md  
**Source Format:** md  
**SHA-256:** `bd0ece60fa0b61d318b0d5b37b842555e7d9e5d8f15bcfdf4735fa0f39cf1f6a`  

---

## R0731 · Perplexity Multi-Model Council -- Session Guide

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: PERPLEXITY_SESSION_GUIDE.md
- source_format: md
- text_sha256: bd0ece60fa0b61d318b0d5b37b842555e7d9e5d8f15bcfdf4735fa0f39cf1f6a

# Perplexity Multi-Model Council -- Session Guide

## Pre-requisites

1. Deposit the paper + bundle on Zenodo (see ZENODO_DEPOSIT_INSTRUCTIONS.md)
2. Record the new version DOI
3. Fill in the DOI in COUNCIL_DISPATCH_FULL.md (two placeholders near the top)

## Council composition

Run the dispatch through every available model family in Perplexity.
Each session = one seat. The goal is maximum vendor diversity.

| Seat | Model | Vendor family | Vote weight | Notes |
|------|-------|--------------|-------------|-------|
| 1 | GPT-4.1 / GPT-5 | OpenAI | 1.0 (Tier 1, non-producer) | Full weight |
| 2 | Gemini 2.5 Pro | Google | 0.5 consensus / 1.0 unique | Tier 2; long-context strength |
| 3 | Claude Sonnet 4.6 / Opus 4.8 | Anthropic | 0.0 (advisory only) | PRODUCER FAMILY -- advisory, no vote weight |
| 4 | Grok | xAI | 0.5 consensus / 1.0 unique | Tier 2; adversarial framing |
| 5 | Sonar / Perplexity default | Perplexity | 1.0 (Tier 1) | If Perplexity's own model is available |
| 6 | DeepSeek R1 | DeepSeek | 1.0 (non-producer, fresh family) | Novel family not in prior council |
| 7 | Qwen | Alibaba | 1.0 (non-producer, fresh family) | Novel family not in prior council |

**Which models are available in Perplexity** depends on your account
tier and current model offerings. Run as many as available. Minimum
for a creditable council: at least 3 non-producer families.

## How to run each seat

1. Open a NEW Perplexity session (clear context; each seat must be independent)
2. Select the target model
3. Paste the entire content of COUNCIL_DISPATCH_FULL.md
4. Wait for the full review
5. Save the output as `seat_[model_name].md` (e.g., `seat_gpt4.md`)

## After all seats complete

### Adjudication

1. Open a final Perplexity session (any model -- Perplexity default or Claude for methodology fidelity)
2. Paste all seat outputs together with this adjudication prompt:

```
You are the adjudicator for a multi-model peer review council under the
BayyinahEnterprise audit methodology (BAF v3.0). Below are the individual
seat reviews. Your tasks:

1. Identify CONVERGENT findings (same finding from 2+ seats, possibly
   different severity). Apply vote weighting per the table in the seat
   outputs. A finding clears consensus at >= 2.0 total weight.

2. Identify UNIQUE findings (found by exactly one seat). These are
   equally surfaceable regardless of weight. List each with the
   originating seat.

3. Identify CONTRADICTIONS (seats disagree on whether something is a
   finding at all, or disagree by 2+ severity bands). Flag for
   project-lead disposition.

4. Produce a SYNTHESIS with:
   - All convergent findings (with severity = highest assigned)
   - All unique findings (with originating seat noted)
   - All contradictions (with both sides quoted)
   - A unified severity ledger
   - A unified verdict (CLEAN / CONDITIONAL / HALT)

Producer-family seats (Claude/Anthropic) are advisory-only: their
findings are listed but do not contribute to vote weight or consensus
threshold.

[PASTE ALL SEAT OUTPUTS HERE]
```

### Recording

Save the adjudication output as `council_synthesis.md`. This is the
paper's peer-review record.

## Relationship to prior program audits

This council reviews the PAPER, not the ARTIFACT. The artifact has
already survived 37 passes, a V32--V34 convergence, and a two-family
carry. The paper is a new document that reports those results. A
CRITICAL finding on the paper does not invalidate the artifact's carry;
it means the paper mis-states something about it.

## Timeline

- Zenodo deposit: ~10 minutes
- Per-seat review: ~5-10 minutes each (depends on model)
- All seats: ~30-60 minutes for 5-7 seats
- Adjudication: ~15 minutes
- Total: ~1-2 hours

## Output files

After completion, the deposit should contain:

```
zenodo_deposit/
  BSSG_PAPER.md                    -- the paper
  BSSG_PAPER_BUNDLE.zip            -- the artifact bundle
  SHA256SUMS_DEPOSIT.txt           -- digest manifest
  ZENODO_DEPOSIT_INSTRUCTIONS.md   -- deposit metadata
  COUNCIL_AUDIT_BRIEF.md           -- the audit brief (template)
  COUNCIL_DISPATCH_FULL.md         -- brief + paper (paste-ready)
  PERPLEXITY_SESSION_GUIDE.md      -- this file
  seats/
    seat_gpt.md                    -- GPT seat output
    seat_gemini.md                 -- Gemini seat output
    seat_claude.md                 -- Claude seat output (advisory)
    seat_grok.md                   -- Grok seat output
    seat_deepseek.md               -- DeepSeek seat output
    seat_qwen.md                   -- Qwen seat output
  council_synthesis.md             -- adjudication output
```

---

# Bismillah ir-Rahman ir-Rahim
