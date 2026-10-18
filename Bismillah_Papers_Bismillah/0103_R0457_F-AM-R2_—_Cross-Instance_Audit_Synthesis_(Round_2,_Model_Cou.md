# Bismillah ir-Rahman ir-Rahim

# R0457 -- F-AM-R2 — Cross-Instance Audit Synthesis (Round 2, Model Council)

**Chronological Index:** 103 of 995  
**Date:** 2025-12-01  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-AM-R2_synthesis.md  
**Source Format:** md  
**SHA-256:** `b86e7cbc9a66fe4c2602f8fb4135e654bd0cb8e1fb41ea45788682a629633220`  

---

## R0457 · F-AM-R2 — Cross-Instance Audit Synthesis (Round 2, Model Council)

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-AM-R2_synthesis.md
- source_format: md
- text_sha256: b86e7cbc9a66fe4c2602f8fb4135e654bd0cb8e1fb41ea45788682a629633220

# F-AM-R2 — Cross-Instance Audit Synthesis (Round 2, Model Council)

**Artifact audited:** Bayyinah al-Amāna, Provenance Integrity for Public Open Data, v0.2 (reader note + Audit & Provenance Companion + reproduction package `Bayyinah_ProvenanceIntegrity_ReproPackage.zip`).
**Namespace:** F-AM-R2. **Round:** Second of the two consecutive qualifying passes convergence requires.
**Produced by:** BayyinahEnterprise (Claude/Anthropic = producing lineage).
**Synthesizer:** Perplexity Computer (orchestrator), operating from the attached package only.

---

## A. No-prior-state attestation (orchestrator)

Each council member was launched as a fresh, memoryless subagent instance in a clean session, given its own extracted copy of the package under `/home/user/workspace/audit_r2/<member>/`, instructed not to read any other member's work or directory before synthesis, and required to paste real, unedited outputs for all six protocol steps. The orchestrator (Computer) ran an independent shadow reproduction of all six steps before dispatch and again verified every member's pasted outputs against the live `data.ny.gov` endpoints and the actual v0.2 document text. I do not claim an absolute guarantee of isolation beyond these operational controls; I report each member's own attestation below, including one member that could not truthfully attest it.

---

## B. Per-member results

| Member | Lineage | Role | Isolation attestation | Execution (all 6 steps, real outputs) | Verdict | CRIT/HIGH | Other findings |
|---|---|---|---|---|---|---|---|
| GPT 5.5 | OpenAI | Qualifying | Clean | Documented, verified genuine | **PASS** | 0 / 0 | 1 MEDIUM, 2 LOW |
| Gemini 3.1 Pro | Google | Qualifying | Clean | Documented, verified genuine | **PASS** | 0 / 0 | 0 |
| GPT 5.4 | OpenAI | Qualifying (rotated in vs R1) | **Could not attest** — workspace-wide grep touched other round directories | Documented, verified genuine | **INCOMPLETE** | 0 / 0 | 1 MEDIUM, 1 LOW |
| Claude Opus 4.8 | Anthropic | Advisory (quarantined, producing lineage) | Clean | Documented, verified genuine | **ADVISORY PASS** (non-convergence-bearing) | 0 / 0 | 1 LOW, 5 INFO |

**Members new relative to F-AM-R1:** GPT 5.4 (R1 used GPT 5.5 + Gemini 3.1 Pro). GPT 5.4 was the rotated-in member; it executed the full protocol with genuine outputs but is non-pass-bearing because it could not attest isolation.

**Verification of genuine execution.** The brief warns that comparing stated numbers to the brief is not a reproduction. I confirmed each report contains real, unedited outputs — e.g., GPT 5.5's independent recompute printed the actual served field inventories from `/api/views/<slug>.json` (23 vs 32, with the 16 official-only / 7 community-only field names enumerated), computed the FY2022 divergence as `Decimal('-0.75')`, and fetched the live `revisions.json` HTTP 404 body (`{"code":"not_found",...,"message":"No service found for this URL."}`); GPT 5.4's output included full response headers (`X-Socrata-RequestId: 3e52e064...`); all four independently demonstrated the adversarial mutate-and-rehash returning `DRIFT` / exit 2 after the hash gate was defeated. None merely compared to the brief.

---

## C. Reproduced substance (consensus across all executing members + orchestrator)

- **Hash:** SHA-256 of `snapshot/provenance_capture.json` = `c49488723819d272beb6445435c724dfbf2050a363baf89d09a333a993e18201` (matches MANIFEST).
- **Provenance (Socrata-declared field):** `gpsc-qqsz` = community ("MTA Procurement Report (All)"); `twsw-2mqa` = official ("MTA Procurements: Beginning 2018").
- **Three-resolution divergence:** FY2023 identical (12,114 rows, $63,569,204,049.36); FY2024 divergent 70 rows (0.5103%) / $58,072,427.23 (0.0891%) — gpsc 13,718 / $65,189,755,228.64 vs twsw 13,648 / $65,131,682,801.41; FY2022 identical row count (12,156) but **$0.75** summed-face divergence ($54,698,007,774.69 vs $54,698,007,775.44).
- **Freshness:** uniform `:created_at` per closed year — gpsc 2025-12-01 (335/701/1066 days after FY24/23/22 close); twsw 2026-04-01 (456/822/1187). Tool flag reads `POST-CLOSE-BATCH` (relabeled from R1's `WHOLESALE-REPUBLISH`).
- **Schema:** 23 vs 32 fields; 16 official-only, 7 community-only.
- **Data-interface:** `/api/views/twsw-2mqa/revisions.json` → HTTP 404; `:created_at`/`:updated_at` system columns queryable on both datasets.
- **Tool behavior:** offline exit 0; `--selftest` detects 42/42 perturbations (exit 0); `--live` no-drift (exit 0); adversarial mutate-and-rehash → comparator `DRIFT` (exit 2) even after the hash gate is defeated.

---

## D. Regression checks (R1 findings absorbed in v0.2)

- **F-AM-R1-S-001 (MEDIUM, "wholesale republish" over-claim):** Primary loci resolved — Abstract, §3 Tier-2, §5.2, and the tool flag now claim only the batch-after-close fact and admit the first-time-bulk-load alternative in-line. **Residual defect remains** (see finding F-AM-R2-001 below).
- **F-AM-R1-S-002 (LOW, provenance wording):** Resolved — provenance labelled as the Socrata-declared metadata field, not an independent chain-of-custody determination (§2, §3).
- **F-AM-R1-S-003 (LOW, "stronger signal"):** Resolved — row-timestamp signal described as "an available freshness signal (row-instantiation timing)... not a full change log" (§4, §7).

---

## E. Findings (namespace F-AM-R2; six-element format)

All findings are below HIGH and therefore **non-blocking** per the brief ("a finding below HIGH does not block the pass but should be recorded for absorption"). Each was independently verified by the orchestrator against the actual v0.2 document text.

### F-AM-R2-001 — MEDIUM
- **Identifier / Severity:** F-AM-R2-001 / MEDIUM.
- **Locus:** Reader note v0.2 §5.4 ("At Tier 2 it emits... the republish inference"), §7 ("which the method reports as a republish rather than reconstructing what changed"), and §6 ("the... republish checks need no period field").
- **Substance (surface vs substrate):** Surface presents F-AM-R1-S-001 as absorbed and the artifact as claiming only the batch-after-close fact. Substrate still emits "republish" as a Tier-2 output / what the method "reports," which exceeds what a single-pull uniform `:created_at` establishes (the tool flag was relabelled to `POST-CLOSE-BATCH` precisely because a single pull cannot distinguish a republish from a first-time bulk load). This reasserts the republish over-claim outside the corrected primary loci.
- **Disposition:** Record for absorption. Replace "republish inference / reports as a republish / republish checks" with "post-close-batch inference (republish or first-time bulk load, indistinguishable from a single pull)" so §5.4, §6, §7 match the Abstract, §3, §5.2, and the tool. Disturbs no reproduced count, total, timestamp, or lag.
- **Cross-reference:** F-AM-R1-S-001. Raised by GPT 5.5 and GPT 5.4 (corroborated); Gemini 3.1 Pro and the Claude advisory member treated S-001 as fully resolved and did not flag it.

### F-AM-R2-002 — LOW
- **Identifier / Severity:** F-AM-R2-002 / LOW.
- **Locus:** Companion v0.2 header line 3: "Companion to: ... (the reader-facing note, v0.1)."
- **Substance (surface vs substrate):** Current-status loci should uniformly read v0.2; the companion's own line 5 and Current State block read v0.2, but line 3 stale-labels the reader note v0.1.
- **Disposition:** Record for absorption — change line 3 to v0.2.
- **Cross-reference:** Status-propagation check. Raised by GPT 5.5, GPT 5.4, and the Claude advisory member (3-way corroboration); Gemini 3.1 Pro's status check examined only the four primary loci and did not catch it.

### F-AM-R2-003 — LOW
- **Identifier / Severity:** F-AM-R2-003 / LOW.
- **Locus:** Companion v0.2 "Audit rounds" line 40: "None yet. The first round appendix... will be appended here when the first rotated Model Council round executes against the v0.1 reader note..."
- **Substance (surface vs substrate):** Current-status text says one qualifying round exists (F-AM-R1), and the F-AM-R1 appendix is appended immediately below; line 40 still says "None yet / will be appended" and also re-states "v0.1 reader note."
- **Disposition:** Record for absorption — mark line 40 as superseded historical text or replace with "F-AM-R1 appended below."
- **Cross-reference:** Status-propagation check; companion Current State lines 12–13. Raised by GPT 5.5 only.

---

## F. Synthesized qualifying verdict (non-Claude members only)

Qualifying set (non-Claude, clean isolation attestation, documented executed reproduction of all six steps):

- **GPT 5.5 — PASS** (0 CRITICAL / 0 HIGH).
- **Gemini 3.1 Pro — PASS** (0 CRITICAL / 0 HIGH).

GPT 5.4 is non-Claude and rotated in relative to R1, but its individual verdict is **INCOMPLETE** (could not attest isolation) and is therefore **excluded from the convergence-bearing pass count**; its corroborating findings (F-AM-R2-001, F-AM-R2-002) are recorded for absorption. Claude Opus 4.8 is the producing lineage and is **advisory-only / quarantined**, excluded from the verdict.

**Synthesized qualifying verdict: QUALIFYING PASS.** At least two qualifying non-producer members independently executed all six protocol steps with pasted real outputs and each returned 0 CRITICAL and 0 HIGH.

---

## G. Convergence determination

F-AM-R1 was the first consecutive qualifying pass (GPT 5.5 + Gemini 3.1 Pro). F-AM-R2 is the second. Both rounds were on materially-identical substance; only wording and one tool-flag label changed between them, and no figure moved. Under the brief's written pass criterion — at least two qualifying members, documented executed reproduction, 0 CRITICAL and 0 HIGH — **convergence under Audit Framework v3.0, Standing Rule 7 is MET on the v0.2 artifact.**

**Membership of both consecutive passes (independence on record):**
- F-AM-R1 qualifying: GPT 5.5 (OpenAI), Gemini 3.1 Pro (Google).
- F-AM-R2 qualifying (clean PASS subset): GPT 5.5 (OpenAI), Gemini 3.1 Pro (Google); GPT 5.4 (OpenAI) rotated in as a third qualifying member but returned INCOMPLETE on isolation attestation.

**Rotation caveat (prominent):** R2 did include a rotated-in non-Claude member (GPT 5.4, a different version new relative to R1), so the round's membership was rotated. However, because GPT 5.4 self-disqualified as INCOMPLETE, the **convergence-bearing clean PASS subset for R2 is GPT 5.5 and Gemini 3.1 Pro — the same pair as F-AM-R1.** Under the written pass criterion this still satisfies the second consecutive qualifying PASS; the rotation record is, however, weaker than intended. If the framework owner interprets "rotated membership rather than a fixed pair" to require a *different clean pass-bearing pair* across the two consecutive passes, a follow-up rotated round (R3) with a successfully-isolated third qualifying member would be needed to close that gap. This caveat is recorded here rather than concealed.

**Recorded-for-absorption (non-blocking) findings:** F-AM-R2-001 (MEDIUM, residual republish wording in §5.4/§6/§7), F-AM-R2-002 (LOW, companion header line 3 stale v0.1), F-AM-R2-003 (LOW, companion line 40 stale "None yet"/v0.1). None disturbs any reproduced count, total, timestamp, lag, hash, schema, or data-interface fact.

---

## H. Scope note on the framework

The "Audit Framework v3.0, Standing Rule 7," the consecutive-qualifying-PASS counter, the producer-lineage quarantine, and the F-AM namespace are the user's own governance construct for this artifact. The convergence statement above is made strictly **within that user-supplied framework**. The substantive, externally-verifiable result — that every numerical and data-interface claim in the v0.2 artifact reproduces exactly from the public `data.ny.gov` endpoints and the frozen capture, and that the comparator is tamper-evident under hash-gate defeat — holds independently of the framework ceremony.

---

# Bismillah ir-Rahman ir-Rahim
