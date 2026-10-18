# Bismillah ir-Rahman ir-Rahim

# R0453 -- F-AM-R2 Audit Report — Claude Opus 4.8 (ADVISORY / NON-CONVERGENCE-BEARING)

**Chronological Index:** 74 of 995  
**Date:** 2024-12-31  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-AM-R2_claude_advisory.md  
**Source Format:** md  
**SHA-256:** `2278d01ab8745f3fcf5e03c97e2f589ba9d0c2e165eedb4078e041b1b0b35240`  

---

## R0453 · F-AM-R2 Audit Report — Claude Opus 4.8 (ADVISORY / NON-CONVERGENCE-BEARING)

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-AM-R2_claude_advisory.md
- source_format: md
- text_sha256: 2278d01ab8745f3fcf5e03c97e2f589ba9d0c2e165eedb4078e041b1b0b35240

# F-AM-R2 Audit Report — Claude Opus 4.8 (ADVISORY / NON-CONVERGENCE-BEARING)

**Namespace:** F-AM-R2
**Member identity:** Claude Opus 4.8 (Anthropic)
**Lineage:** Anthropic — the **PRODUCING** lineage. Per Operating Condition 5 (producer-lineage quarantine), this member is **advisory-only and EXCLUDED from the convergence-bearing synthesized verdict.**
**Execution environment:** Perplexity Computer (code-execution + network to public `data.ny.gov` Socrata API).
**Package used:** the extracted copy in my own working directory `/home/user/workspace/audit_r2/claude_opus_4_8/` (`reproduce_paper3.py`, `snapshot/provenance_capture.json`, `snapshot/MANIFEST.json`). Not recovered from any DOI or external link.

## Attestation

> Fresh, memoryless instance; producer-lineage quarantined advisory; did not access any other member's work.

I am a fresh, memoryless instance with no chat memory, stored state, personalization, prior reports, or access to any other council member's work. I executed every step and pasted the real, unedited outputs below. I did not merely compare stated numbers to the brief — I ran the scripts and independently recomputed against the live portal.

---

## Executed reproduction — six steps (real, unedited outputs)

### Step 1 — `python3 reproduce_paper3.py` (offline), exit code 0

```
[integrity] capture retrieved_utc: 2026-07-19T22:07:28Z

Check 1 -- Provenance classification and divergence
  gpsc-qqsz   provenance=community (MTA Procurement Report (All))
  twsw-2mqa   provenance=official  (MTA Procurements: Beginning 2018)
  2022-12-31 community-vs-official: rows d=+0 (0.0000%), face d=$-0.75 (0.0000000%)  [DIVERGENT]
  2023-12-31 community-vs-official: rows d=+0 (0.0000%), face d=$+0.00 (0.0000000%)  [identical]
  2024-12-31 community-vs-official: rows d=+70 (0.5103%), face d=$+58072427.23 (0.0890821%)  [DIVERGENT]
  [note] even at identical row count, FY2022 diverges by $0.75 in summed face value -- a value-level difference a coarse (billion-rounded) view misses.

Check 2 -- Snapshot integrity
  SHA-256 OK (c49488723819d272...)

Check 3 -- Declared-vs-actual freshness (row :created_at vs reporting-period close)
  gpsc-qqsz   2022-12-31 created 2025-12-01, 1066 days after close  [POST-CLOSE-BATCH]
  gpsc-qqsz   2023-12-31 created 2025-12-01, 701 days after close  [POST-CLOSE-BATCH]
  gpsc-qqsz   2024-12-31 created 2025-12-01, 335 days after close  [POST-CLOSE-BATCH]
  twsw-2mqa   2022-12-31 created 2026-04-01, 1187 days after close  [POST-CLOSE-BATCH]
  twsw-2mqa   2023-12-31 created 2026-04-01, 822 days after close  [POST-CLOSE-BATCH]
  twsw-2mqa   2024-12-31 created 2026-04-01, 456 days after close  [POST-CLOSE-BATCH]

Check 4 -- Schema divergence (served field inventory)
  field counts: {'gpsc-qqsz': 23, 'twsw-2mqa': 32}
  fields in official not in community view: 16
  fields in community view not in official: 7

[note] POST-CLOSE-BATCH = uniform :created_at postdating the period close (one batch load);
       a single pull does not distinguish a republish from a first-time bulk load.
[note] Divergences and batch loads are substrate facts. This tool does not judge whether any was legitimate, authorized, or improper (Tier 3, refused).
EXIT_CODE=0
```

All expected values match: hash OK (`c49488...e18201`), provenance community/official, three-resolution divergence incl. the **$0.75 FY2022** difference at identical row count, FY2023 identical, FY2024 +70 rows (0.5103%) / +$58,072,427.23 (0.0891%), freshness lags 1066/701/335 (community) and 1187/822/456 (official), all flags read **POST-CLOSE-BATCH**, schema 23 vs 32 (16 official-only / 7 community-only).

### Step 2 — `python3 reproduce_paper3.py --selftest` (42 perturbations), exit code 0

```
[selftest] perturbing each captured value to confirm the comparator detects it...
[selftest] perturbed 42 captured values; comparator missed 0
EXIT_CODE=0
```

All 42 captured values perturbed; comparator missed 0.

### Step 3 — `python3 reproduce_paper3.py --live` (re-pull data.ny.gov), exit code 0

```
[live] re-pulling data.ny.gov and comparing to the frozen capture...
[live] no drift on provenance, schema, counts, totals, or row timestamps
[integrity] capture retrieved_utc: 2026-07-19T22:07:28Z

Check 1 -- Provenance classification and divergence
  gpsc-qqsz   provenance=community (MTA Procurement Report (All))
  twsw-2mqa   provenance=official  (MTA Procurements: Beginning 2018)
  2022-12-31 community-vs-official: rows d=+0 (0.0000%), face d=$-0.75 (0.0000000%)  [DIVERGENT]
  2023-12-31 community-vs-official: rows d=+0 (0.0000%), face d=$+0.00 (0.0000000%)  [identical]
  2024-12-31 community-vs-official: rows d=+70 (0.5103%), face d=$+58072427.23 (0.0890821%)  [DIVERGENT]
  [note] even at identical row count, FY2022 diverges by $0.75 in summed face value -- a value-level difference a coarse (billion-rounded) view misses.

Check 2 -- Snapshot integrity
  SHA-256 OK (c49488723819d272...)

Check 3 -- Declared-vs-actual freshness (row :created_at vs reporting-period close)
  gpsc-qqsz   2022-12-31 created 2025-12-01, 1066 days after close  [POST-CLOSE-BATCH]
  gpsc-qqsz   2023-12-31 created 2025-12-01, 701 days after close  [POST-CLOSE-BATCH]
  gpsc-qqsz   2024-12-31 created 2025-12-01, 335 days after close  [POST-CLOSE-BATCH]
  twsw-2mqa   2022-12-31 created 2026-04-01, 1187 days after close  [POST-CLOSE-BATCH]
  twsw-2mqa   2023-12-31 created 2026-04-01, 822 days after close  [POST-CLOSE-BATCH]
  twsw-2mqa   2024-12-31 created 2026-04-01, 456 days after close  [POST-CLOSE-BATCH]

Check 4 -- Schema divergence (served field inventory)
  field counts: {'gpsc-qqsz': 23, 'twsw-2mqa': 32}
  fields in official not in community view: 16
  fields in community view not in official: 7
... (Tier-2 / refusal notes as above) ...
EXIT_CODE=0
```

Live re-pull: **no drift**, exit 0. The live portal reproduces every frozen figure exactly.

### Step 4 — Independent recompute with my OWN code (did NOT import `reproduce_paper3.py`), exit code 0

My independent script (`independent_recompute.py`, saved in this directory) queries `/api/views/<slug>.json` for `provenance`/field inventory and SODA for `count(*)`, `sum(contract_amount)`, and `min`/`max` of `:created_at`/`:updated_at` per fiscal window, using its own `urllib` code path.

```
======================================================================
DATASET gpsc-qqsz : name='MTA Procurement Report (All)' provenance='community' fieldCount=23
  FY2022  n=12156  face=54698007774.69  created[2025-12-01T17:15:55.609Z..2025-12-01T17:15:55.609Z] uniform=True lag=1066 days  updated[2025-12-01T17:15:55.609Z..2025-12-01T17:15:55.609Z]
  FY2023  n=12114  face=63569204049.36  created[2025-12-01T17:15:55.609Z..2025-12-01T17:15:55.609Z] uniform=True lag=701 days  updated[2025-12-01T17:15:55.609Z..2025-12-01T17:15:55.609Z]
  FY2024  n=13718  face=65189755228.64  created[2025-12-01T17:15:55.609Z..2025-12-01T17:15:55.609Z] uniform=True lag=335 days  updated[2025-12-01T17:15:55.609Z..2025-12-01T17:15:55.609Z]
======================================================================
DATASET twsw-2mqa : name='MTA Procurements: Beginning 2018' provenance='official' fieldCount=32
  FY2022  n=12156  face=54698007775.44  created[2026-04-01T14:09:46.913Z..2026-04-01T14:09:46.913Z] uniform=True lag=1187 days  updated[2026-04-01T14:09:46.913Z..2026-04-01T14:09:46.913Z]
  FY2023  n=12114  face=63569204049.36  created[2026-04-01T14:09:46.913Z..2026-04-01T14:09:46.913Z] uniform=True lag=822 days  updated[2026-04-01T14:09:46.913Z..2026-04-01T14:09:46.913Z]
  FY2024  n=13648  face=65131682801.41  created[2026-04-01T14:09:46.913Z..2026-04-01T14:09:46.913Z] uniform=True lag=456 days  updated[2026-04-01T14:09:46.913Z..2026-04-01T14:09:46.913Z]
======================================================================
PROVENANCE: gpsc-qqsz='community'  twsw-2mqa='official'
SCHEMA: gpsc-qqsz=23 fields  twsw-2mqa=32 fields
  official-only (16): ['address_line_1', 'address_line_2', 'basis_for_exemption', 'city', 'country', 'exempt_from_article_4c', 'fair_market_value', 'fair_market_value_explanation', 'postal_code', 'region', 'renewal_date', 'state', 'status', 'transaction_number', 'vendor_is_nys_or_fbe', 'zip_code_plus_4']
  community-only (7): ['authority_name', 'procurements', 'vendor_city', 'vendor_country', 'vendor_postal_code', 'vendor_province_region', 'vendor_state']
======================================================================
THREE-RESOLUTION DIVERGENCE (community gpsc vs official twsw):
  FY2022: gpsc(n=12156,$54698007774.69) twsw(n=12156,$54698007775.44) -> rowd=+0 (0.0000%) faced=$-0.75 (0.0000%) [DIVERGENT]
  FY2023: gpsc(n=12114,$63569204049.36) twsw(n=12114,$63569204049.36) -> rowd=+0 (0.0000%) faced=$+0.00 (0.0000%) [identical]
  FY2024: gpsc(n=13718,$65189755228.64) twsw(n=13648,$65131682801.41) -> rowd=+70 (0.5103%) faced=$+58072427.23 (0.0891%) [DIVERGENT]
======================================================================
FY2022 exact face check: gpsc=54698007774.69 twsw=54698007775.44 diff=0.75
Uniform timestamps: gpsc all-uniform=True  twsw all-uniform=True
EXIT_CODE=0
```

Independent recompute confirms, from first principles: provenance community/official; 23-vs-32 schema (16 official-only, 7 community-only, exact field lists shown); the three-resolution divergence including the **$0.75 FY2022** value-level difference at identical row count (12,156 both); FY2023 identical; FY2024 +70 rows / +$58,072,427.23; and uniform `:created_at`/`:updated_at` per window with all lags matching (335/701/1066 and 456/822/1187).

### Step 5 — Data-interface facts (real output)

```
=== revisions.json (expect HTTP 404) ===
HTTP_STATUS=404                      # curl, twsw-2mqa
HTTPError code = 404                 # urllib, twsw-2mqa
gpsc revisions HTTP=404             # gpsc-qqsz also 404

=== system columns :created_at / :updated_at queryable on both ===
--- gpsc-qqsz ---
[{"ca":"2025-12-01T17:15:55.609Z","ua":"2025-12-01T17:15:55.609Z"}]
--- twsw-2mqa ---
[{"ca":"2026-04-01T14:09:46.913Z","ua":"2026-04-01T14:09:46.913Z"}]
```

`/api/views/twsw-2mqa/revisions.json` returns **HTTP 404** (confirmed via both curl and urllib; gpsc-qqsz likewise 404). The SODA `:created_at`/`:updated_at` system columns are **queryable** on both datasets.

### Step 6 — Adversarial: mutate one captured value, re-hash MANIFEST so hash passes, confirm DRIFT (real output)

I copied the full package to a scratch dir, mutated **one** captured value (`gpsc-qqsz` FY2024 `face_total` 65189755228.64 -> 65189755228.65), regenerated the frozen JSON, and rewrote `MANIFEST.json` with the new SHA-256 so the integrity check would PASS. The original package files in my working directory were left untouched.

```
mutated gpsc FY2024 face_total: 65189755228.64 -> 65189755228.65
re-hashed MANIFEST sha256 = 89037b3225e586ec4033943ad74cc6c51457cc7b23309baaaaff2384e663f1e4
--- offline run does NOT abort (hash now matches) ---
offline exit=0
  SHA-256 OK (89037b3225e586ec...)
--- --live: comparator detects DRIFT (nonzero exit), NOT hash abort ---
[live] re-pulling data.ny.gov and comparing to the frozen capture...
[live] DRIFT detected on 1 value(s):
  gpsc-qqsz/2024-12-31/face_total: frozen=65189755228.65 live=65189755228.64
LIVE_EXIT_CODE=2
```

The mutation defeated the SHA-256 integrity gate (offline exit 0, "SHA-256 OK" on the re-hashed manifest), yet the **live comparator still caught the tampered value** (exit 2, DRIFT on `gpsc-qqsz/2024-12-31/face_total`). This is the required demonstration — the comparator, not merely the hash abort, detects the mutation.

---

## Regression checks on absorbed R1 findings (loci cited)

- **F-AM-R1-S-001 (republish over-claim) — CONFIRMED RESOLVED.** The reader note claims only the batch-after-close fact and admits the first-time-bulk-load alternative in-line at the Abstract (line 17: "in a single post-close batch (consistent with a wholesale republish and equally with a first-time bulk load, which a single-pull timestamp cannot distinguish)"), the Section 3 Tier-2 definition (line 37: "a batch that a single pull cannot resolve into a republish versus a first-time bulk load"), and Section 5.2 (line 55: "the note claims only the batch-after-close fact, not which of the two produced it"). No current-status locus asserts a republish as established fact; line 39 references the *language* only to disclaim over-reading. The tool freshness flag reads **`POST-CLOSE-BATCH`** (`reproduce_paper3.py` line 135) with the clarifying note that "a single pull does not distinguish a republish from a first-time bulk load" (line 148), and prints POST-CLOSE-BATCH on every window in Steps 1 and 3. **No dispute.**
- **F-AM-R1-S-002 (Socrata-declared provenance field) — CONFIRMED RESOLVED.** Provenance is labelled as the Socrata-declared metadata field, not a chain-of-custody determination: Section 2 line 27 ("the Socrata-declared `provenance` field, not an independent inquiry into agency authorship") and Section 3 line 37 ("the Socrata-declared `provenance` field ... not an independent chain-of-custody inquiry"). **No dispute.**
- **F-AM-R1-S-003 (available freshness signal, not full change log) — CONFIRMED RESOLVED.** Section 4 line 43 describes the row-timestamp signal as "an available freshness signal (row-instantiation timing) ... not a full change log with prior values or edit authorship." The reader note no longer uses "stronger signal." (The phrase "stronger freshness signal" survives only in the companion's append-only Pre-audit producer record P3-B1, line 34, which is a historical baseline record correct-in-context, not the reader-note wording R1-S-003 governs.) **No dispute.**

## Status-propagation check (version / counter / round count)

| Locus | Version | Counter | Round count | Consistent? |
|---|---|---|---|---|
| Reader note header (line 7) | v0.2 | ONE | one (F-AM-R1) | yes |
| Reader note Section 8 (line 75) | v0.2 | one | one (F-AM-R1) | yes |
| Companion header subtitle (line 5) | v0.2 | ONE | one (F-AM-R1) | yes |
| Companion Current State (lines 9–13) | v0.2 | ONE | one (F-AM-R1) | yes |
| **Companion header line 3** | **calls reader note "v0.1"** | — | — | **NO — stale** |
| Companion append-only appendix (line 42+) | v0.1→v0.2 amendments, R1 | ONE | one | correct-in-context (append-only) |
| Companion Pre-audit producer record (lines 30–36) | v0.1 baseline, counter ZERO | — | — | correct-in-context (append-only baseline) |

**Finding:** Companion header **line 3** — "Companion to: *Bayyinah al-Amāna ...* (the reader-facing note, **v0.1**)" — is a current-status locus (it identifies the artifact this companion presently accompanies) that is stale: the reader note is v0.2, as the companion's own subtitle (line 5, "Mirrors note state v0.2") and Current State block confirm. This is exactly the "stale v0.1" case the brief flags. Recorded as **F-AM-R2-S-001 (LOW)** below.

The append-only appendix and Pre-audit producer record correctly reference v0.1 / ZERO as *past* states and are correct-in-context per Section 14.5. Companion line 40 ("Audit rounds — None yet ...") is an append-only ledger scaffold immediately superseded by the appended appendix and by the authoritative Current State block; it is a housekeeping artifact and is recorded as INFO (F-AM-R2-S-002).

---

## Findings (six-element format; namespace F-AM-R2)

**F-AM-R2-S-001 — LOW**
- **Identifier:** F-AM-R2-S-001
- **Severity:** LOW
- **Locus:** Audit and Provenance Companion, header line 3 ("Companion to: ... the reader-facing note, v0.1").
- **Substance (surface vs substrate):** Surface — a current-status header states the accompanied reader note is at version v0.1. Substrate — the reader note is v0.2 (its header line 7 and Section 8 line 75), and the companion's own subtitle (line 5) and Current State block (lines 9–13) all read v0.2. The header version pointer diverges from the actual current artifact version.
- **Disposition:** Recorded for absorption. Non-blocking (below HIGH). Recommend correcting line 3 to "v0.2" (or "current version") to match all other current-status loci. Moves no reproduced figure; does not affect any reproduction step.
- **Cross-reference:** Status-propagation check; brief's "stale v0.1" example (Round-2 brief, Status-propagation check).

**F-AM-R2-S-002 — INFO**
- **Identifier:** F-AM-R2-S-002
- **Severity:** INFO
- **Locus:** Companion "Audit rounds" section, line 40 ("None yet. The first round appendix ... will be appended here ...").
- **Substance (surface vs substrate):** Surface — a scaffold line states no audit rounds have occurred yet. Substrate — one round (F-AM-R1) has occurred and is appended in the very next block (line 42+) and recorded in the authoritative Current State (line 13). The scaffold sentence is a stale template header within the append-only ledger.
- **Disposition:** Informational only; the append-only appendix directly below and the Current State block are authoritative and correct. Optional tidy-up (annotate the scaffold as superseded). Not a blocking inconsistency; the operative current-status loci agree.
- **Cross-reference:** Section 14.5 append-only immutability; F-AM-R2-S-001.

**F-AM-R2-S-003 — INFO (affirmative)**
- **Identifier:** F-AM-R2-S-003
- **Severity:** INFO
- **Locus:** Reader note Abstract/§3/§5.2 and `reproduce_paper3.py` freshness flag.
- **Substance:** F-AM-R1-S-001 confirmed resolved — every republish locus now claims only the batch-after-close fact and admits the first-bulk-load alternative in-line; tool flag reads POST-CLOSE-BATCH. No locus asserts a republish as established fact.
- **Disposition:** Affirmative; no action. Regression clean.
- **Cross-reference:** F-AM-R1-S-001.

**F-AM-R2-S-004 — INFO (affirmative)**
- **Identifier:** F-AM-R2-S-004
- **Severity:** INFO
- **Locus:** Reader note §2 (line 27) and §3 (line 37).
- **Substance:** F-AM-R1-S-002 confirmed resolved — provenance is labelled the Socrata-declared metadata field, explicitly not a chain-of-custody / agency-authorship determination.
- **Disposition:** Affirmative; no action. Regression clean.
- **Cross-reference:** F-AM-R1-S-002.

**F-AM-R2-S-005 — INFO (affirmative)**
- **Identifier:** F-AM-R2-S-005
- **Severity:** INFO
- **Locus:** Reader note §4 (line 43).
- **Substance:** F-AM-R1-S-003 confirmed resolved — the row-timestamp signal is described as an available freshness signal (row-instantiation timing), not a full change log; "stronger signal" removed from the reader note.
- **Disposition:** Affirmative; no action. Regression clean.
- **Cross-reference:** F-AM-R1-S-003.

**F-AM-R2-S-006 — INFO (affirmative)**
- **Identifier:** F-AM-R2-S-006
- **Severity:** INFO
- **Locus:** Whole reproduction package (all six executed steps) and the live `data.ny.gov` endpoints.
- **Substance:** Every expected value reproduced exactly under executed reproduction: hash `c49488...e18201`; provenance community/official; three-resolution divergence incl. **$0.75** FY2022 at identical row count, FY2023 identical, FY2024 +70 rows (0.5103%) / +$58,072,427.23 (0.0891%); uniform freshness lags 1066/701/335 and 1187/822/456; schema 23 vs 32 (16 official-only / 7 community-only); revisions.json HTTP 404 with system columns queryable; self-test 42/42; live no-drift (exit 0); adversarial mutate+rehash caught by comparator (exit 2). Tier-1/Tier-2/Tier-3 discipline and the refusal boundary hold; no divergence, batch load, or edit is asserted or implied to be illegitimate, unauthorized, improper, or deceptive.
- **Disposition:** Affirmative; substrate fully corresponds to surface at the audited resolution. No action.
- **Cross-reference:** Reproduction protocol Steps 1–6; F-AM-R1 substance.

**Severity tally:** CRITICAL 0 · HIGH 0 · MEDIUM 0 · LOW 1 (F-AM-R2-S-001) · INFO 5.

---

## ADVISORY VERDICT (NON-CONVERGENCE-BEARING)

**ADVISORY VERDICT: PASS.**

Criterion: 0 CRITICAL AND 0 HIGH AND documented executed reproduction = PASS. I recorded **0 CRITICAL and 0 HIGH**, executed all six protocol steps with real pasted outputs, independently recomputed with my own code, confirmed the data-interface facts, and demonstrated the adversarial mutate-and-rehash returning comparator DRIFT (exit 2). The single LOW (F-AM-R2-S-001, stale "v0.1" in a companion header) and one INFO housekeeping item (F-AM-R2-S-002) are non-blocking and recommended for absorption; they move no reproduced figure.

**This verdict is ADVISORY ONLY and NON-CONVERGENCE-BEARING.** As a member of the Claude (Anthropic) **producing lineage**, I am quarantined under Operating Condition 5 and **EXCLUDED from the synthesized qualifying verdict**, which must be computed over the non-Claude qualifying members only. My PASS does not count toward the two-consecutive-qualifying-pass convergence gate under Audit Framework v3.0, Standing Rule 7.

## Attestation (repeated)

> Fresh, memoryless instance; producer-lineage quarantined advisory; did not access any other member's work.

---

# Bismillah ir-Rahman ir-Rahim
