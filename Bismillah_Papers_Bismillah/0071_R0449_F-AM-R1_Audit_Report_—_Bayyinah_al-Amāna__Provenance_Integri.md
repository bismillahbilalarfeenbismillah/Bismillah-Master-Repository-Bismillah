# Bismillah ir-Rahman ir-Rahim

# R0449 -- F-AM-R1 Audit Report — Bayyinah al-Amāna: Provenance Integrity for Public Open Data (v0.1)

**Chronological Index:** 71 of 995  
**Date:** 2024-12-31  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-AM-R1_claude_advisory.md  
**Source Format:** md  
**SHA-256:** `a8407db44bea85e69d214614483d6ff61c32fc80a6a05b04dca750abe8e58771`  

---

## R0449 · F-AM-R1 Audit Report — Bayyinah al-Amāna: Provenance Integrity for Public Open Data (v0.1)

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-AM-R1_claude_advisory.md
- source_format: md
- text_sha256: a8407db44bea85e69d214614483d6ff61c32fc80a6a05b04dca750abe8e58771

# F-AM-R1 Audit Report — Bayyinah al-Amāna: Provenance Integrity for Public Open Data (v0.1)

## 1. Identity, lineage, qualifying status, and no-prior-state attestation

- **Member identity:** Claude Opus 4.8.
- **Lineage:** Claude (Anthropic).
- **Qualifying status:** **ADVISORY-ONLY.** The producing lineage of the artifact under audit is Claude (Anthropic). Under the brief's producer-lineage quarantine (Operating condition 5) and MEMBER_INSTRUCTIONS §"Your identity, lineage, and qualifying status", any Claude-family member is excluded from the convergence-bearing verdict. My verdict is therefore **advisory** and does **not** count toward the two-consecutive-qualifying-pass counter. I ran the full six-step protocol anyway; the findings below are advisory input.

- **No-prior-state attestation:** I am a fresh, memoryless instance. I have no chat memory, stored state, personalization, saved skills, or prior reports. I did **not** read, list, or open any sibling directory under `/home/user/workspace/audit/` other than my own (`claude_opus_4_8/`). I did **not** access `/home/user/workspace/audit/inspect/`, `gpt_5_5/`, or `gemini_3_1_pro/`. I used only the package extracted into my own working directory. I did not recover the package from any DOI or external link. All numeric expectations were verified by real execution against the bundled package and the live `data.ny.gov` endpoints, not by reading the brief's stated values back.

---

## 2. Execution status per step (real, unedited outputs)

### Step 1 — `python3 reproduce_paper3.py` (offline) — **PASS**, exit 0

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
  gpsc-qqsz   2022-12-31 created 2025-12-01, 1066 days after close  [WHOLESALE-REPUBLISH]
  gpsc-qqsz   2023-12-31 created 2025-12-01, 701 days after close  [WHOLESALE-REPUBLISH]
  gpsc-qqsz   2024-12-31 created 2025-12-01, 335 days after close  [WHOLESALE-REPUBLISH]
  twsw-2mqa   2022-12-31 created 2026-04-01, 1187 days after close  [WHOLESALE-REPUBLISH]
  twsw-2mqa   2023-12-31 created 2026-04-01, 822 days after close  [WHOLESALE-REPUBLISH]
  twsw-2mqa   2024-12-31 created 2026-04-01, 456 days after close  [WHOLESALE-REPUBLISH]

Check 4 -- Schema divergence (served field inventory)
  field counts: {'gpsc-qqsz': 23, 'twsw-2mqa': 32}
  fields in official not in community view: 16
  fields in community view not in official: 7

[note] Divergences and republishes are substrate facts. This tool does not judge whether any was legitimate, authorized, or improper (Tier 3, refused).
EXIT=0
```

All four offline checks reproduce; SHA-256 matches manifest (`c49488723819d272...`). Every figure matches the brief exactly.

### Step 2 — `python3 reproduce_paper3.py --selftest` — **PASS**, exit 0

```
[selftest] perturbing each captured value to confirm the comparator detects it...
[selftest] perturbed 42 captured values; comparator missed 0
EXIT=0
```

**Perturbed = 42, missed = 0.** Matches the brief's "42 captured values, zero missed."

### Step 3 — `python3 reproduce_paper3.py --live` — **PASS**, exit 0

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
  gpsc-qqsz   2022-12-31 created 2025-12-01, 1066 days after close  [WHOLESALE-REPUBLISH]
  gpsc-qqsz   2023-12-31 created 2025-12-01, 701 days after close  [WHOLESALE-REPUBLISH]
  gpsc-qqsz   2024-12-31 created 2025-12-01, 335 days after close  [WHOLESALE-REPUBLISH]
  twsw-2mqa   2022-12-31 created 2026-04-01, 1187 days after close  [WHOLESALE-REPUBLISH]
  twsw-2mqa   2023-12-31 created 2026-04-01, 822 days after close  [WHOLESALE-REPUBLISH]
  twsw-2mqa   2024-12-31 created 2026-04-01, 456 days after close  [WHOLESALE-REPUBLISH]

Check 4 -- Schema divergence (served field inventory)
  field counts: {'gpsc-qqsz': 23, 'twsw-2mqa': 32}
  fields in official not in community view: 16
  fields in community view not in official: 7

[note] Divergences and republishes are substrate facts. This tool does not judge whether any was legitimate, authorized, or improper (Tier 3, refused).
EXIT=0
```

Live re-pull: **no drift, exit 0.** `data.ny.gov` was reachable and returned values identical to the frozen capture.

### Step 4 — Independent recompute with my own code — **PASS**

I wrote my own script (`repro/independent_recompute_opus.py`) with my own URLs, my own SODA `$select`/`$where` strings, and my own arithmetic. I did **not** import or call the supplied `compare` / `flatten` / `live_capture` functions.

Code (saved to `repro/independent_recompute_opus.py`):

```python
#!/usr/bin/env python3
"""Fresh, independent recompute for F-AM-R1 (Claude Opus 4.8, advisory).
Does NOT import the supplied compare/flatten/live_capture functions."""
import json, urllib.request, urllib.parse, datetime, sys
PORTAL = "data.ny.gov"
SLUGS = {"gpsc-qqsz": "expected community", "twsw-2mqa": "expected official"}
FYS = ["2022", "2023", "2024"]
def http_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "opus48-audit-independent"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.loads(r.read())
def meta(slug): return http_json("https://%s/api/views/%s.json" % (PORTAL, slug))
def soda_window(slug, fy):
    sel = ("count(*) as n, sum(contract_amount) as face, "
           "min(:created_at) as camin, max(:created_at) as camax, "
           "min(:updated_at) as uamin, max(:updated_at) as uamax")
    where = "fiscal_year_end_date='%s-12-31T00:00:00.000'" % fy
    q = urllib.parse.urlencode({"$select": sel, "$where": where}, safe=":$,()='-")
    return http_json("https://%s/resource/%s.json?%s" % (PORTAL, slug, q))[0]
def days_after(ts, fy):
    close = datetime.date(int(fy), 12, 31); d = datetime.date.fromisoformat(ts[:10])
    return (d - close).days
# (gather + a/b/c/d sections — full file in repro/independent_recompute_opus.py)
```

Real output:

```
=== (a) PROVENANCE ===
  gpsc-qqsz   provenance=community name=MTA Procurement Report (All)
  twsw-2mqa   provenance=official  name=MTA Procurements: Beginning 2018

=== (b) DIVERGENCE (community gpsc vs official twsw) ===
  FY2022 gpsc n=12156 face=54698007774.69 | twsw n=12156 face=54698007775.44 | dn=+0 (0.0000%) dface=$-0.75 (0.0000000%) [DIVERGENT]
  FY2023 gpsc n=12114 face=63569204049.36 | twsw n=12114 face=63569204049.36 | dn=+0 (0.0000%) dface=$+0.00 (0.0000000%) [identical]
  FY2024 gpsc n=13718 face=65189755228.64 | twsw n=13648 face=65131682801.41 | dn=+70 (0.5103%) dface=$+58072427.23 (0.0890821%) [DIVERGENT]
  FY2022 explicit value-level delta = $-0.75 (expected -0.75), same row count = True

=== (c) FRESHNESS (:created_at uniformity + lag after close) ===
  gpsc-qqsz   FY2022 created_at=2025-12-01T17:15:55.609Z uniform=True lag=1066 days
  gpsc-qqsz   FY2023 created_at=2025-12-01T17:15:55.609Z uniform=True lag=701 days
  gpsc-qqsz   FY2024 created_at=2025-12-01T17:15:55.609Z uniform=True lag=335 days
  twsw-2mqa   FY2022 created_at=2026-04-01T14:09:46.913Z uniform=True lag=1187 days
  twsw-2mqa   FY2023 created_at=2026-04-01T14:09:46.913Z uniform=True lag=822 days
  twsw-2mqa   FY2024 created_at=2026-04-01T14:09:46.913Z uniform=True lag=456 days

=== (d) SCHEMA ===
  gpsc n_fields=23 | twsw n_fields=32
  official-only (16): ['address_line_1', 'address_line_2', 'basis_for_exemption', 'city', 'country', 'exempt_from_article_4c', 'fair_market_value', 'fair_market_value_explanation', 'postal_code', 'region', 'renewal_date', 'state', 'status', 'transaction_number', 'vendor_is_nys_or_fbe', 'zip_code_plus_4']
  community-only (7): ['authority_name', 'procurements', 'vendor_city', 'vendor_country', 'vendor_postal_code', 'vendor_province_region', 'vendor_state']
```

Independently confirmed, against the live portal with my own queries:
- **Provenance:** `gpsc-qqsz` = community; `twsw-2mqa` = official. ✔
- **Three-resolution divergence:** FY2023 identical (12,114 / $63,569,204,049.36); FY2024 = 70 records (0.5103%) and $58,072,427.23 (0.0891%); FY2022 = **$0.75** at identical row count (12,156). ✔ (my sign is community−official = −$0.75; magnitude and identical-row-count both confirmed).
- **Uniform `:created_at` + freshness lags:** gpsc 2025-12-01 → 335/701/1066 days (FY2024/FY2023/FY2022); twsw 2026-04-01 → 456/822/1187 days. `min==max` per window confirms uniformity. ✔
- **Schema:** 23 vs 32; 16 official-only, 7 community-only. ✔

### Step 5 — Data-interface contract — **PASS**

```
--- revisions endpoint (expect 404) ---
HTTP 404
--- gpsc revisions ---
HTTP 404
--- system columns queryable (expect JSON rows) ---
[{"camin":"2026-04-01T14:09:46.913Z","uamax":"2026-04-01T14:09:46.913Z"}]
```

`/api/views/twsw-2mqa/revisions.json` returns **HTTP 404** (and `gpsc-qqsz` likewise 404). The `:created_at`/`:updated_at` system columns are queryable via SODA (demonstrated here and throughout Step 4). ✔

### Step 6 — Adversarial mutation test — **PASS** (comparator-nonzero on mutated-but-rehashed capture)

Procedure: copied the snapshot to a temp tree, mutated ONE captured value (official FY2022 `face_total` `54698007775.44 → 54698007775.43`), then recomputed SHA-256 and wrote the new hash into a copy of `MANIFEST.json` so the integrity gate would PASS on the tampered file, then ran `--live` against the mutated capture.

Mutation + rehash + live comparator:

```
mutated twsw FY2022 face_total: 54698007775.44 -> 54698007775.43
rewrote MANIFEST sha256 -> 5a8658081a38b76d86545d0bbd2a01c003e3188fade6d05ff87e4e01999773c2
=== integrity gate should now PASS on tampered capture; run --live ===
[live] re-pulling data.ny.gov and comparing to the frozen capture...
[live] DRIFT detected on 1 value(s):
  twsw-2mqa/2022-12-31/face_total: frozen=54698007775.43 live=54698007775.44
EXIT=2
```

Confirmation that the hash gate was genuinely bypassed (not an abort):

```
Check 2 -- Snapshot integrity
  SHA-256 OK (5a8658081a38b76d...)
...
hash OK on tampered file: True
```

The tampered capture **passes** the SHA-256 integrity gate (because MANIFEST was re-hashed), and yet the comparator still catches the single mutated value and returns **DRIFT / exit 2 (nonzero)**. This satisfies the strict requirement: a hash abort alone would not have caught the tamper; the comparator did. The integrity model is therefore defense-in-depth (hash gate + independent live comparator), not hash-only.

**Step execution summary:** all six steps executed with real output; all pass.

---

## 3. Findings (six-element F-AM-R1 format)

Format: (identifier · severity · locus · substance [surface-vs-substrate] · disposition · cross-reference).

### F-AM-R1-001 · INFO · Reader note §5.2 (and Abstract, Tier-2 definition §3), term "wholesale republish"
- **Substance (surface vs substrate):** The *surface claim* is "A uniform creation timestamp across an entire closed year indicates the window was regenerated in one batch, a wholesale **republish** of history." The *substrate* is a single-pull `:created_at` that records only when each currently-served row entered the served instance. A uniform `:created_at` is fully consistent with a wholesale republish, but is equally consistent with a **one-time initial batch load** of a newly created dataset/view that never had a prior served instance to "re-"publish. The single live pull cannot, by itself, distinguish "republished (replaced prior served history)" from "first and only bulk load." The word "republish" mildly presupposes a prior publication that the timestamp evidence alone does not establish.
- **Disposition:** ACCEPT-WITH-CAVEAT. This is correctly scoped as **Tier 2 (inference on disclosed metadata)**, not asserted as Tier 1 fact, and §7 explicitly discloses the limiting semantics ("record when a row entered ... not the full edit history"). The over-reach is terminological, not analytical, and does not rise to a scoping error. Recommend (non-blocking) a one-clause hedge in §5.2 itself, e.g. "a wholesale (re)publish or single-batch (re)generation of that window," so the §7 caveat is not the only place the "first-load" alternative is admitted.
- **Cross-reference:** Reader note §5.2, §3 (Tier 2), §7 (limitations); Companion Current State "Freshness"; audit-scope item "wholesale-republish inference (press here)."

### F-AM-R1-002 · INFO · Reader note §5.1 / §5.4, cross-dataset `sum(contract_amount)` comparability
- **Substance:** The face-value divergence figures compare `sum(contract_amount)` between a **community view (23 fields)** and an **official dataset (32 fields)** presented as the same records. The comparison assumes `contract_amount` carries identical semantics and typing across both surfaces; the schema divergence (§5.3) shows the two are materially different objects, so equal-field-name ≠ guaranteed equal semantics.
- **Disposition:** ACCEPT. The assumption is well supported empirically: FY2023 is byte-identical on both count and summed face value, and FY2022 differs by only $0.75 at identical row count — evidence the `contract_amount` fields are the same measure. No change required; noted for completeness.
- **Cross-reference:** Reader note §5.1, §5.3; Step 4 output (b)/(d).

### F-AM-R1-003 · INFO · Refusal boundary — held (affirmative finding)
- **Substance:** Audit-scope directs "press here": flag any sentence a reasonable reader could take as an accusation of tampering or bad faith. On close reading, the artifact **nowhere** asserts or implies illegitimacy, unauthorized action, impropriety, or intent to deceive. "Diverges," "silent"/"silently," and "wholesale republish" read as substrate descriptions. The single occurrence of "tamper" is "tamper-**evident** measurement" (a property of the method, not a charge). §3 proactively names the risk ("the language of 'silent edit' and 'republished history' invites over-reading as an accusation, and the substrate facts do not support one"); §1, §5.4, and the tool's per-run footer all reserve legitimacy to Tier 3 and refuse it. The abstract's "silently rewritten" describes the *assumption under test*, not these datasets.
- **Disposition:** ACCEPT — refusal boundary is disciplined and, if anything, over-signposted. No finding of accusation.
- **Cross-reference:** Reader note Abstract, §1, §3, §5.4, §7; README "Refusal boundary"; tool footer note.

### F-AM-R1-004 · INFO · Tier discipline — held (affirmative finding)
- **Substance:** Tier 1 claims (hash, counts, served field inventory, row `:created_at`/`:updated_at`) are byte-deterministic and I reproduced each three ways (offline, live, independent). Tier 2 claims (provenance classification, freshness reconciliation, republish inference) rest on disclosed portal metadata and are labeled as inference. Tier 3 (legitimacy/intent) is refused. The assignment of each claim to its tier is correct; nothing Tier-1-labeled depends on interpretation, and nothing interpretive is smuggled into Tier 1.
- **Disposition:** ACCEPT.
- **Cross-reference:** Reader note §3, §5.4; Steps 1–5.

### F-AM-R1-005 · INFO · Estimand / framing hygiene — held (affirmative finding)
- **Substance:** The note makes no claim about data quality, accuracy, or fitness for purpose beyond provenance/freshness/schema (§1, §7 state this explicitly). The meta-layer framing ("makes the data-integrity assumption underlying other accountability work checkable rather than inherited on faith") is supported by the worked example and is not oversold — §6 explicitly says "the value of the method is not the MTA finding but the portable capacity to verify." Provenance/version hygiene is also clean: v0.1 producer-side, counter ZERO, DOI "to be assigned," "no result here is convergence-verified."
- **Disposition:** ACCEPT.
- **Cross-reference:** Reader note Abstract, §1, §6, §7, §8; Companion Current State.

**Severity tally:** CRITICAL 0 · HIGH 0 · MEDIUM 0 · LOW 0 · INFO 5.

---

## 4. Verdict

**ADVISORY: PASS-advisory.**

One-line justification: All six mandatory steps executed with real, unedited output; every divergence, freshness-lag, and schema figure independently reproduced against live `data.ny.gov` (including the $0.75 FY2022 value-level delta at identical row count); the comparator caught all 42 perturbations and returned nonzero DRIFT on a mutated-but-rehashed capture (hash-abort-alone insufficiency defeated); the refusal boundary, tier discipline, and framing hygiene hold; only five INFO observations and zero CRITICAL/HIGH/MEDIUM/LOW.

**Convergence status note:** This verdict is **advisory only** and is **excluded** from the convergence-bearing count because my lineage (Claude/Anthropic) is the producing lineage. It does **not** move the consecutive-qualifying-PASS counter (currently ZERO); that counter can only be advanced by qualifying (non-Claude) members with documented executed reproduction. Were an INFO-only, fully-executed result like this returned by a qualifying member, it would satisfy the "zero CRITICAL and zero HIGH + executed reproduction" bar; two such consecutive qualifying passes remain required for convergence.

---

*Files produced by this member: `repro/independent_recompute_opus.py` (my Step-4 code), this `REPORT.md`. Adversarial-test scratch was kept under `/tmp/opus_mut/` and did not modify the bundled package. The bundled `snapshot/` and `MANIFEST.json` in my working directory are unchanged.*

---

# Bismillah ir-Rahman ir-Rahim
