# Bismillah ir-Rahman ir-Rahim

# R0460 -- F-AM-R3 Synthesis — Bayyinah al-Amāna Provenance Integrity (v0.3), Confirming Round

**Chronological Index:** 767 of 995  
**Date:** Undated  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-AM-R3_synthesis.md  
**Source Format:** md  
**SHA-256:** `823c0abef1c3839aa0ce6be896b9f80b8081e2e80aa15f626ca050d819c3a2c9`  

---

## R0460 · F-AM-R3 Synthesis — Bayyinah al-Amāna Provenance Integrity (v0.3), Confirming Round

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-AM-R3_synthesis.md
- source_format: md
- text_sha256: 823c0abef1c3839aa0ce6be896b9f80b8081e2e80aa15f626ca050d819c3a2c9

# F-AM-R3 Synthesis — Bayyinah al-Amāna Provenance Integrity (v0.3), Confirming Round

**Round:** F-AM-R3 (confirming convergence round on the corrected v0.3 artifact).
**Council:** GPT 5.5 (OpenAI), Gemini 3.1 Pro (Google), GPT 5.4 (OpenAI, rotated-in), Claude Opus 4.8 (Anthropic, advisory-only — producing lineage quarantined).
**Orchestrator shadow-run:** independent recompute + adversarial test executed by the orchestrator (Claude, producing lineage) as a ground-truth baseline; it is NOT a qualifying member and is not counted.

---

## A. Per-member result

| Member | Lineage | Role | New vs R1/R2? | Isolation attestation | 6-step execution | Findings | Verdict |
|---|---|---|---|---|---|---|---|
| GPT 5.5 | OpenAI | Qualifying | NO (R1/R2 clean pair) | Clean, verbatim | All 6 executed; outputs match ground truth exactly | 1× LOW (F-AM-R3-001) | **PASS** |
| Gemini 3.1 Pro | Google | Qualifying | NO (R1/R2 clean pair) | Clean, verbatim | Steps 1–3, 5, 6 match; **Step 4 independent recompute nonconforming** (broader filter, misattributed) | None raised | **PASS**, but Step 4 nonconforming — **not counted in the clean pass-bearing pair** |
| GPT 5.4 | OpenAI | Qualifying — rotated-in | **YES** | **Clean, verbatim** (the R2 failure is fixed) | All 6 executed; outputs match ground truth exactly | None | **PASS** |
| Claude Opus 4.8 | Anthropic | Advisory-only (producing lineage) | N/A | Clean, verbatim + disclosed incidental grep-tool scope expansion (not read/used) | All 6 executed; outputs match ground truth exactly | None | Advisory PASS (non-qualifying) |

All four members gave the verbatim isolation and no-prior-state attestations. Command-log audit by the orchestrator confirmed every member's file operations were confined to its own directory (the only outside touch was outbound HTTPS to data.ny.gov). GPT 5.4 — which returned INCOMPLETE on isolation in R2 — this time confined every operation to its own directory and attested cleanly, closing the rotation gap.

## B. Where the qualifying members agree

| Finding | GPT 5.5 | Gemini 3.1 Pro | GPT 5.4 | Evidence |
|---|---|---|---|---|
| Hash c4948872…e18201 verifies; default run exit 0 | ✓ | ✓ | ✓ | All four pasted identical Step-1 output |
| Self-test 42/42, 0 missed, exit 0 | ✓ | ✓ | ✓ | Identical Step-2 output |
| `--live` no drift, exit 0 (live data == frozen capture) | ✓ | ✓ | ✓ | Identical Step-3 output |
| FY2023 identical (12,114 / $63,569,204,049.36) | ✓ | ⚠¹ | ✓ | Step 4 exact-match recompute |
| FY2024 +70 rows / +$58,072,427.23 (0.5103% / 0.0891%) | ✓ | ⚠¹ | ✓ | Step 4 recompute |
| FY2022 identical 12,156 rows, $0.75 face divergence | ✓ | ⚠¹ | ✓ | Step 4 recompute |
| Provenance community/official; schema 23 vs 32 (16/7) | ✓ | ✓ | ✓ | Step 4 recompute |
| Uniform `:created_at`/`:updated_at`; lags 335/701/1066 & 456/822/1187 | ✓ | ✓ | ✓ | Step 4 recompute |
| revisions.json HTTP 404 both; system columns queryable (200) | ✓ | ✓ | ✓ | Step 5 |
| Adversarial: rehash passes integrity, comparator still DRIFT (exit 2) | ✓ | ✓ | ✓ | Step 6 |
| F-AM-R2-001/002/003 all resolved in the specified loci | ✓ | ✓ | ✓ | Quoted loci |
| Status-propagation: all current-status loci uniform on v0.3 / TWO / two rounds | ✓ | ✓ | ✓ | Quoted loci |
| Refusal boundary holds (no accusation of impropriety) | ✓ | ✓ | ✓ | Whole-note search |

⚠¹ Gemini: these exact divergence values are corroborated by Gemini's **script** Step 3 (`--live`, no drift, exit 0), but Gemini's **independent Step 4 recompute did not reproduce them** — it used a broader date-range filter and returned different gpsc row counts (and an FY2023 sum $49,000 high). See disagreement table. The orchestrator treats Gemini's Step 4 as nonconforming.

## C. Where the qualifying members disagree

| Topic | GPT 5.5 | Gemini 3.1 Pro | GPT 5.4 | Why they differ |
|---|---|---|---|---|
| Reader note §1 line 23: "an observed divergence or republish" — surviving bare republish assertion? | **YES — disputed single-member LOW (F-AM-R3-001)** (imprecise; presupposes a republish was observed when only a post-close batch load is established) | Not raised (read as a refused Tier-3 hypothetical, not an assertion of fact) | Not raised (read line 23 as "does not adjudicate whether…", i.e. refusal, not a bare claim; saw "republish" only in generic/historical contexts) | GPT 5.5 applied the brief's "search the WHOLE note" instruction most strictly and flagged it; the other two judged the refusal-sentence context dispositive. The R2-specified loci (5.4/6/7) are resolved; this is a newly-surfaced §1 survivor of the same wording class, at LOW. |
| Step 4 independent recompute reproduced the exact snapshot values | Yes (exact-match filter) | **No** — used a broader date-range SoQL filter; got gpsc FY2022 12158, FY2023 12115/$49,000-high, FY2024 13719; attributed to "moving data" | Yes (exact-match filter) | Gemini's `fiscal_year_end_date >= 'YYYY-01-01' AND <= 'YYYY-12-31T23:59:59.999'` captures rows with non-Dec-31 fiscal ends that the snapshot's exact-match `= 'YYYY-12-31T00:00:00.000'` excludes. Gemini's own Step 3 (`--live`, no drift) proves the data is not moving, so the Step-4 discrepancy is a filter mismatch in Gemini's own recompute, not data drift. Gemini did not re-run with the correct filter to reconcile. |

## D. Unique discoveries

| Model | Finding | Why it matters |
|---|---|---|
| GPT 5.5 | F-AM-R3-001 (LOW, disputed/single-member): residual "observed divergence or republish" phrasing in reader §1 line 23 — a newly-surfaced locus of the same republish-wording class as F-AM-R1/R2-001 (the R2-specified loci are resolved) | The producer's recurring "fix some loci, not all" failure mode surfaced again, now at LOW (down from the R2 MEDIUM) and in a new locus (§1, outside the R2-specified 5.4/6/7). Arguable, non-blocking, but a carry-forward to absorb before v1.0. |
| Gemini 3.1 Pro (orchestrator-identified) | Step-4 filter mismatch + misattribution to "moving data" | Audit-execution defect (not an artifact defect). Shows the value of the multi-member council: one member's independent recompute erred, but two qualifying members + the advisory member + the orchestrator all confirmed the exact values, so convergence is robust. |

## E. Synthesized verdict (qualifying, successfully-isolated members only)

**Qualifying PASS under the written criterion.** Two qualifying, successfully-isolated, non-producer-lineage members — GPT 5.5 and GPT 5.4 — each executed all six protocol steps with pasted real outputs, independently recomputed the live data.ny.gov facts with their own code using the specified exact-match fiscal-window filter, demonstrated the adversarial hash-gate-defeat DRIFT, and returned **zero CRITICAL and zero HIGH**. Both corroborate every substrate fact: provenance community/official; FY2023 identical; FY2024 +70 rows / +$58,072,427.23; FY2022 identical 12,156 rows with the $0.75 face divergence; uniform post-close-batch timestamps with lags 335/701/1066 and 456/822/1187; schema 23 vs 32 (16/7); revisions.json 404; system columns queryable. The orchestrator's independent ground-truth recompute agrees exactly. Convergence rests on GPT 5.5 + GPT 5.4.

**Rotation gap: CLOSED.** GPT 5.4 — new relative to the R1/R2 clean pair (GPT 5.5, Gemini 3.1 Pro), the member that returned INCOMPLETE on isolation in R2 — this round achieved a clean, isolated PASS with documented executed reproduction. The pass-bearing set therefore includes a successfully-isolated member new relative to R1/R2, satisfying the rotation the prior rounds could not complete.

**One open LOW finding (F-AM-R3-001).** GPT 5.5 flagged reader §1 line 23's "an observed divergence or republish" as a residual bare republish phrasing — a LOW recurrence of the F-AM-R1/R2-001 wording class in a previously-unflagged locus. Gemini 3.1 Pro, GPT 5.4, and the Claude advisory member did not raise it, reading the phrase as a refused Tier-3 hypothetical rather than a bare assertion. It is non-blocking (LOW; 0C/0H) and disturbs no reproduced count, total, timestamp, or interface fact; it is a wording-cleanup carry-forward for the producer to absorb at canonical v1.0 promotion. The orchestrator's read agrees it is at least imprecise (the method establishes a post-close batch load, not a republish), so LOW is appropriate.

**Gemini 3.1 Pro — Step 4 nonconforming; not in the clean pass-bearing pair.** Gemini returned PASS and its Steps 1–3, 5, and 6 are correct and corroborate (including the script's `--live` no-drift confirmation), but its mandatory Step 4 independent recompute did not conform to the specified exact fiscal-window filter (`fiscal_year_end_date = 'YYYY-12-31T00:00:00.000'`): it used a broader date-range filter and produced gpsc row counts (FY2022 12158, FY2023 12115, FY2024 13719) and an FY2023 sum ($49,000 high) inconsistent with both the frozen capture and its own Step-3 `--live` no-drift result. Gemini misattributed the discrepancy to "moving data" rather than recognizing the filter mismatch, and did not re-run with the correct filter to reconcile. Because its Step 4 did not independently confirm the exact three-resolution divergence as specified, the orchestrator treats Gemini's Step 4 as nonconforming and does not count Gemini in the clean pass-bearing pair. This is an audit-execution defect, not an artifact defect, and does not reduce the qualifying-pass count below two (GPT 5.5 + GPT 5.4 both cleanly confirm the exact values).

**Advisory corroboration.** Claude Opus 4.8 (producing lineage, quarantined, excluded from the verdict) independently reproduced all six steps with matching outputs and raised no findings, with an honest disclosure of one incidental grep-tool scope expansion it did not read or use. Corroboration only — not convergence-bearing.

## F. Counter and recommendation

Under the brief's pass criterion (zero CRITICAL, zero HIGH, documented executed reproduction from ≥2 clean-isolated qualifying members), **F-AM-R3 is a qualifying PASS**. The operational consecutive qualifying-PASS count advances from **TWO to THREE** (F-AM-R1, F-AM-R2, F-AM-R3); F-AM-R3 confirms the corrected v0.3 artifact. This round is materially cleaner than R2 (finding load: MEDIUM + 2 LOW → 1 LOW) and the rotation record is now clean (a successfully-isolated new member, GPT 5.4, is in the pass-bearing set).

It is **not zero-findings clean**: one open LOW (F-AM-R3-001) remains. It is clean on the blocking criteria (zero CRITICAL, zero HIGH) and clean on rotation (GPT 5.4 successfully isolated and new). Recommendation: absorb F-AM-R3-001 (rephrase §1 line 23's "an observed divergence or republish" to the "post-close batch load (republish or first-time bulk load, indistinguishable from a single pull)" discipline already applied in the Abstract, §3, §5.2, §5.4, §6, §7, and the tool flag), then promote to canonical v1.0. The way to v1.0 is substantially cleared; the rotation caveat that held back R2 is resolved.

**Bottom line:** Convergence is confirmed under the written 0C/0H criterion, the rotation gap is closed, and one non-blocking LOW wording finding remains to absorb before v1.0.

---

# Bismillah ir-Rahman ir-Rahim
