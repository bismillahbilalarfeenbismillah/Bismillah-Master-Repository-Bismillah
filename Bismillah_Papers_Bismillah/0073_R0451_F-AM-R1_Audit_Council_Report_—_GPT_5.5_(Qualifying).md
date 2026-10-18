# Bismillah ir-Rahman ir-Rahim

# R0451 -- F-AM-R1 Audit Council Report — GPT 5.5 (Qualifying)

**Chronological Index:** 73 of 995  
**Date:** 2024-12-31  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-AM-R1_gpt55.md  
**Source Format:** md  
**SHA-256:** `1f90f52cb13ebcbbe47e7dcec42bf76fe9f6d61b9f3aee172c52c1fb9992f2e6`  

---

## R0451 · F-AM-R1 Audit Council Report — GPT 5.5 (Qualifying)

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-AM-R1_gpt55.md
- source_format: md
- text_sha256: 1f90f52cb13ebcbbe47e7dcec42bf76fe9f6d61b9f3aee172c52c1fb9992f2e6

# F-AM-R1 Audit Council Report — GPT 5.5 (Qualifying)

## 1. Identity, lineage, qualifying status, and no-prior-state attestation

- Identity: GPT 5.5.
- Lineage: OpenAI.
- Producer lineage: Claude / Anthropic.
- Qualifying status: QUALIFYING, non-producer-lineage member; this verdict counts toward qualifying convergence if accepted by the synthesis process.
- Fresh-state attestation: I acted as a fresh, memoryless audit member for this task. I did not read, list, or open any sibling directory under `/home/user/workspace/audit/` other than `/home/user/workspace/audit/gpt_5_5/`; I did not read `/home/user/workspace/audit/inspect/`; and I did not use any prior report or other member work.

## 2. Execution status per mandatory step, with pasted real outputs

### Step 1 — Offline reproduction: `python3 reproduce_paper3.py`

Status: EXECUTED. Exit code 0.

```text
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
EXIT_CODE=0
```

### Step 2 — Self-test: `python3 reproduce_paper3.py --selftest`

Status: EXECUTED. Exit code 0. Perturbed count 42; missed count 0.

```text
[selftest] perturbing each captured value to confirm the comparator detects it...
[selftest] perturbed 42 captured values; comparator missed 0
EXIT_CODE=0
```

### Step 3 — Live reproduction: `python3 reproduce_paper3.py --live`

Status: EXECUTED. Exit code 0.

```text
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
EXIT_CODE=0
```

### Step 4 — Independent recompute with my own code and live queries

Status: EXECUTED. Exit code 0. I did not import or call the supplied `compare`, `flatten`, or `live_capture` functions.

Code used:

```python
#!/usr/bin/env python3
import json
import urllib.request
import urllib.parse
from decimal import Decimal, ROUND_HALF_UP
from datetime import date

PORTAL = "https://data.ny.gov"
SLUGS = ["gpsc-qqsz", "twsw-2mqa"]
FYS = ["2022", "2023", "2024"]

def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "gpt-5.5-audit-independent-recompute"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.loads(r.read().decode("utf-8"))

def metadata(slug):
    url = f"{PORTAL}/api/views/{slug}.json"
    return url, fetch_json(url)

def soda_agg(slug, fy):
    select = "count(*) as row_count, sum(contract_amount) as face_total, min(:created_at) as ca_min, max(:created_at) as ca_max, min(:updated_at) as ua_min, max(:updated_at) as ua_max"
    where = f"fiscal_year_end_date='{fy}-12-31T00:00:00.000'"
    qs = urllib.parse.urlencode({"$select": select, "$where": where}, safe=":,$()*='-.")
    url = f"{PORTAL}/resource/{slug}.json?{qs}"
    rows = fetch_json(url)
    if len(rows) != 1:
        raise RuntimeError(f"unexpected rows for {slug} {fy}: {rows!r}")
    r = rows[0]
    return url, {
        "row_count": int(r["row_count"]),
        "face_total": Decimal(str(r["face_total"])).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        "created_at_min": r["ca_min"],
        "created_at_max": r["ca_max"],
        "updated_at_min": r["ua_min"],
        "updated_at_max": r["ua_max"],
    }

def lag_days(ts, fy):
    return (date.fromisoformat(ts[:10]) - date(int(fy), 12, 31)).days

# Pull metadata and per-window aggregates independently.
meta = {}
windows = {}
print("INDEPENDENT RECOMPUTE CODE PATH: urllib direct API calls; no imports from reproduce_paper3.py")
for slug in SLUGS:
    url, m = metadata(slug)
    fields = sorted([c["fieldName"] for c in m.get("columns", []) if c.get("fieldName")])
    meta[slug] = {"name": m.get("name"), "provenance": m.get("provenance"), "field_count": len(fields), "fields": fields, "url": url}
    windows[slug] = {}
    print(f"METADATA {slug}: url={url} name={meta[slug]['name']!r} provenance={meta[slug]['provenance']!r} field_count={meta[slug]['field_count']}")
    for fy in FYS:
        qurl, agg = soda_agg(slug, fy)
        windows[slug][fy] = agg
        uniform_created = agg["created_at_min"] == agg["created_at_max"]
        uniform_updated = agg["updated_at_min"] == agg["updated_at_max"]
        print(
            f"WINDOW {slug} FY{fy}: query={qurl} rows={agg['row_count']} face_total={agg['face_total']} "
            f"created_at_min={agg['created_at_min']} created_at_max={agg['created_at_max']} "
            f"updated_at_min={agg['updated_at_min']} updated_at_max={agg['updated_at_max']} "
            f"uniform_created={uniform_created} uniform_updated={uniform_updated} lag_days={lag_days(agg['created_at_min'], fy)}"
        )

print("\nPROVENANCE CONFIRMATION")
print(f"gpsc-qqsz provenance == community: {meta['gpsc-qqsz']['provenance'] == 'community'}")
print(f"twsw-2mqa provenance == official: {meta['twsw-2mqa']['provenance'] == 'official'}")

print("\nDIVERGENCE CONFIRMATION")
for fy in FYS:
    g = windows["gpsc-qqsz"][fy]
    t = windows["twsw-2mqa"][fy]
    row_delta = g["row_count"] - t["row_count"]
    face_delta = (g["face_total"] - t["face_total"]).quantize(Decimal("0.01"))
    count_pct = (Decimal(abs(row_delta)) / Decimal(g["row_count"]) * Decimal(100)).quantize(Decimal("0.0001")) if g["row_count"] else Decimal(0)
    face_pct = (abs(face_delta) / g["face_total"] * Decimal(100)).quantize(Decimal("0.0001")) if g["face_total"] else Decimal(0)
    print(f"FY{fy}: gpsc_rows={g['row_count']} twsw_rows={t['row_count']} row_delta={row_delta} count_pct={count_pct}% gpsc_face={g['face_total']} twsw_face={t['face_total']} face_delta={face_delta} face_pct={face_pct}%")

print("\nFRESHNESS CONFIRMATION")
for slug in SLUGS:
    parts = []
    for fy in ["2024", "2023", "2022"]:
        w = windows[slug][fy]
        parts.append(f"FY{fy}: created_date={w['created_at_min'][:10]} lag={lag_days(w['created_at_min'], fy)} min=max? {w['created_at_min'] == w['created_at_max']}")
    print(f"{slug}: " + "; ".join(parts))

print("\nSCHEMA CONFIRMATION")
g_fields = set(meta["gpsc-qqsz"]["fields"])
t_fields = set(meta["twsw-2mqa"]["fields"])
print(f"gpsc-qqsz fields={len(g_fields)} twsw-2mqa fields={len(t_fields)}")
print(f"official_only_count={len(t_fields - g_fields)} official_only={sorted(t_fields - g_fields)}")
print(f"community_only_count={len(g_fields - t_fields)} community_only={sorted(g_fields - t_fields)}")

```

Real output:

```text
INDEPENDENT RECOMPUTE CODE PATH: urllib direct API calls; no imports from reproduce_paper3.py
METADATA gpsc-qqsz: url=https://data.ny.gov/api/views/gpsc-qqsz.json name='MTA Procurement Report (All)' provenance='community' field_count=23
WINDOW gpsc-qqsz FY2022: query=https://data.ny.gov/resource/gpsc-qqsz.json?$select=count(*)+as+row_count,+sum(contract_amount)+as+face_total,+min(:created_at)+as+ca_min,+max(:created_at)+as+ca_max,+min(:updated_at)+as+ua_min,+max(:updated_at)+as+ua_max&$where=fiscal_year_end_date='2022-12-31T00:00:00.000' rows=12156 face_total=54698007774.69 created_at_min=2025-12-01T17:15:55.609Z created_at_max=2025-12-01T17:15:55.609Z updated_at_min=2025-12-01T17:15:55.609Z updated_at_max=2025-12-01T17:15:55.609Z uniform_created=True uniform_updated=True lag_days=1066
WINDOW gpsc-qqsz FY2023: query=https://data.ny.gov/resource/gpsc-qqsz.json?$select=count(*)+as+row_count,+sum(contract_amount)+as+face_total,+min(:created_at)+as+ca_min,+max(:created_at)+as+ca_max,+min(:updated_at)+as+ua_min,+max(:updated_at)+as+ua_max&$where=fiscal_year_end_date='2023-12-31T00:00:00.000' rows=12114 face_total=63569204049.36 created_at_min=2025-12-01T17:15:55.609Z created_at_max=2025-12-01T17:15:55.609Z updated_at_min=2025-12-01T17:15:55.609Z updated_at_max=2025-12-01T17:15:55.609Z uniform_created=True uniform_updated=True lag_days=701
WINDOW gpsc-qqsz FY2024: query=https://data.ny.gov/resource/gpsc-qqsz.json?$select=count(*)+as+row_count,+sum(contract_amount)+as+face_total,+min(:created_at)+as+ca_min,+max(:created_at)+as+ca_max,+min(:updated_at)+as+ua_min,+max(:updated_at)+as+ua_max&$where=fiscal_year_end_date='2024-12-31T00:00:00.000' rows=13718 face_total=65189755228.64 created_at_min=2025-12-01T17:15:55.609Z created_at_max=2025-12-01T17:15:55.609Z updated_at_min=2025-12-01T17:15:55.609Z updated_at_max=2025-12-01T17:15:55.609Z uniform_created=True uniform_updated=True lag_days=335
METADATA twsw-2mqa: url=https://data.ny.gov/api/views/twsw-2mqa.json name='MTA Procurements: Beginning 2018' provenance='official' field_count=32
WINDOW twsw-2mqa FY2022: query=https://data.ny.gov/resource/twsw-2mqa.json?$select=count(*)+as+row_count,+sum(contract_amount)+as+face_total,+min(:created_at)+as+ca_min,+max(:created_at)+as+ca_max,+min(:updated_at)+as+ua_min,+max(:updated_at)+as+ua_max&$where=fiscal_year_end_date='2022-12-31T00:00:00.000' rows=12156 face_total=54698007775.44 created_at_min=2026-04-01T14:09:46.913Z created_at_max=2026-04-01T14:09:46.913Z updated_at_min=2026-04-01T14:09:46.913Z updated_at_max=2026-04-01T14:09:46.913Z uniform_created=True uniform_updated=True lag_days=1187
WINDOW twsw-2mqa FY2023: query=https://data.ny.gov/resource/twsw-2mqa.json?$select=count(*)+as+row_count,+sum(contract_amount)+as+face_total,+min(:created_at)+as+ca_min,+max(:created_at)+as+ca_max,+min(:updated_at)+as+ua_min,+max(:updated_at)+as+ua_max&$where=fiscal_year_end_date='2023-12-31T00:00:00.000' rows=12114 face_total=63569204049.36 created_at_min=2026-04-01T14:09:46.913Z created_at_max=2026-04-01T14:09:46.913Z updated_at_min=2026-04-01T14:09:46.913Z updated_at_max=2026-04-01T14:09:46.913Z uniform_created=True uniform_updated=True lag_days=822
WINDOW twsw-2mqa FY2024: query=https://data.ny.gov/resource/twsw-2mqa.json?$select=count(*)+as+row_count,+sum(contract_amount)+as+face_total,+min(:created_at)+as+ca_min,+max(:created_at)+as+ca_max,+min(:updated_at)+as+ua_min,+max(:updated_at)+as+ua_max&$where=fiscal_year_end_date='2024-12-31T00:00:00.000' rows=13648 face_total=65131682801.41 created_at_min=2026-04-01T14:09:46.913Z created_at_max=2026-04-01T14:09:46.913Z updated_at_min=2026-04-01T14:09:46.913Z updated_at_max=2026-04-01T14:09:46.913Z uniform_created=True uniform_updated=True lag_days=456

PROVENANCE CONFIRMATION
gpsc-qqsz provenance == community: True
twsw-2mqa provenance == official: True

DIVERGENCE CONFIRMATION
FY2022: gpsc_rows=12156 twsw_rows=12156 row_delta=0 count_pct=0.0000% gpsc_face=54698007774.69 twsw_face=54698007775.44 face_delta=-0.75 face_pct=0.0000%
FY2023: gpsc_rows=12114 twsw_rows=12114 row_delta=0 count_pct=0.0000% gpsc_face=63569204049.36 twsw_face=63569204049.36 face_delta=0.00 face_pct=0.0000%
FY2024: gpsc_rows=13718 twsw_rows=13648 row_delta=70 count_pct=0.5103% gpsc_face=65189755228.64 twsw_face=65131682801.41 face_delta=58072427.23 face_pct=0.0891%

FRESHNESS CONFIRMATION
gpsc-qqsz: FY2024: created_date=2025-12-01 lag=335 min=max? True; FY2023: created_date=2025-12-01 lag=701 min=max? True; FY2022: created_date=2025-12-01 lag=1066 min=max? True
twsw-2mqa: FY2024: created_date=2026-04-01 lag=456 min=max? True; FY2023: created_date=2026-04-01 lag=822 min=max? True; FY2022: created_date=2026-04-01 lag=1187 min=max? True

SCHEMA CONFIRMATION
gpsc-qqsz fields=23 twsw-2mqa fields=32
official_only_count=16 official_only=['address_line_1', 'address_line_2', 'basis_for_exemption', 'city', 'country', 'exempt_from_article_4c', 'fair_market_value', 'fair_market_value_explanation', 'postal_code', 'region', 'renewal_date', 'state', 'status', 'transaction_number', 'vendor_is_nys_or_fbe', 'zip_code_plus_4']
community_only_count=7 community_only=['authority_name', 'procurements', 'vendor_city', 'vendor_country', 'vendor_postal_code', 'vendor_province_region', 'vendor_state']
EXIT_CODE=0
```

### Step 5 — Data-interface contract

Status: EXECUTED. The revisions endpoint returned HTTP 404. The Step 4 SODA queries also demonstrate that `:created_at` and `:updated_at` are queryable because each query selected `min(:created_at)`, `max(:created_at)`, `min(:updated_at)`, and `max(:updated_at)` successfully.

```text
HTTP 404
EXIT_CODE=0
```

### Step 6 — Adversarial mutation test

Status: EXECUTED. I copied the reproduction package into a mutation-test package, changed one captured value (`gpsc-qqsz` provenance), recomputed SHA-256, wrote the new SHA into the manifest, confirmed the integrity check would pass, and then ran the live comparator. The comparator returned nonzero / DRIFT with exit code 2.

Stdout:

```text
mutated gpsc-qqsz provenance to community_MUTATED
new_sha256 6aeb98d68a1194ad37e6bbe156d26b222b0f75ed110fc16529e11af0b68603e9
Check 2 -- Snapshot integrity
  SHA-256 OK (6aeb98d68a1194ad...)

[live] re-pulling data.ny.gov and comparing to the frozen capture...
[live] DRIFT detected on 1 value(s):
  gpsc-qqsz/provenance: frozen='community_MUTATED' live='community'
EXIT_CODE=2
```

Stderr:

```text
+ WORK=/home/user/workspace/audit/gpt_5_5/mutation_test_repro
+ rm -rf /home/user/workspace/audit/gpt_5_5/mutation_test_repro
+ cp -a /home/user/workspace/audit/gpt_5_5/repro /home/user/workspace/audit/gpt_5_5/mutation_test_repro
+ python3 -
+ cd /home/user/workspace/audit/gpt_5_5/mutation_test_repro
+ python3 reproduce_paper3.py
+ sed -n '/Check 2 -- Snapshot integrity/,+2p'
+ python3 reproduce_paper3.py --live
+ STATUS=2
+ printf 'EXIT_CODE=%s
' 2
+ exit 0
++ '[' 1 = 1 ']'
++ '[' -x /usr/bin/clear_console ']'
++ /usr/bin/clear_console -q
```

## 3. Audit findings — F-AM-R1 namespace

### F-AM-R1-001

- Identifier: F-AM-R1-001
- Severity: MEDIUM
- Locus: Reader note Section 5.2, especially: “They could not” and “A uniform creation timestamp across an entire closed year indicates the window was regenerated in one batch, a wholesale republish of history rather than selective edits.”
- Substance: The surface wording moves from the observed substrate fact — the currently served row objects have uniform `:created_at` and `:updated_at` timestamps long after fiscal close — to a stronger historical reconstruction: “regenerated,” “wholesale republish of history,” and “rather than selective edits.” The substrate supports a batch entry/update of the currently served rows in the Socrata instance; it does not by itself reconstruct whether equivalent records existed earlier elsewhere, why the batch occurred, or whether “republish” rather than migration/reload is the best noun.
- Disposition: Revise Section 5.2 to say the rows “entered and were last updated in the served instance in a uniform batch, consistent with a wholesale reload/republish or migration,” and keep the causal/legitimacy question refused. This does not disturb the reproduced counts, totals, schema, timestamps, or lags.
- Cross-reference: Mandatory Steps 3 and 4 confirmed the exact uniform timestamps and lags; the concern is inference scope, not arithmetic.

### F-AM-R1-002

- Identifier: F-AM-R1-002
- Severity: LOW
- Locus: Reader note Sections 2, 3, and 5.1, especially phrases such as “actual provenance classification,” “first-party official dataset,” and “declared provenance versus actual provenance.”
- Substance: The surface wording can read as if the audit independently establishes real-world first-party status. The substrate actually observed in this package is the Socrata metadata field `provenance` from `https://data.ny.gov/api/views/gpsc-qqsz.json` and `https://data.ny.gov/api/views/twsw-2mqa.json`, not an independent inquiry into agency authorship or chain-of-custody outside the portal metadata.
- Disposition: Clarify throughout that the Tier 2 provenance result is “portal metadata provenance classification” or “Socrata-declared provenance,” unless additional non-portal evidence is added.
- Cross-reference: Mandatory Step 4 metadata output confirmed `gpsc-qqsz` = `community` and `twsw-2mqa` = `official` from the metadata endpoints.

### F-AM-R1-003

- Identifier: F-AM-R1-003
- Severity: LOW
- Locus: Reader note Section 4: “the row-level system timestamps supply a stronger signal in its place.”
- Substance: The surface wording “stronger” is too broad. The substrate confirms that `/api/views/twsw-2mqa/revisions.json` returns HTTP 404 and that `:created_at`/`:updated_at` are queryable, but row-level timestamps are a different freshness signal rather than a full substitute for a portal-native revision history with change authorship, prior values, or edit reasons.
- Disposition: Replace “a stronger signal” with “an available row-level freshness signal” or “a stronger signal for row-instantiation timing, but not a full change log.”
- Cross-reference: Mandatory Step 5 confirmed HTTP 404; Mandatory Step 4 confirmed successful system-column aggregate queries.

### F-AM-R1-004

- Identifier: F-AM-R1-004
- Severity: INFO
- Locus: Refusal boundary across the abstract, Sections 1, 3, 5.4, and 7.
- Substance: I did not find an explicit accusation that the divergences, republishes, or edits were illegitimate, unauthorized, improper, or intended to deceive. Some charged terms — “silently rewritten,” “wrong one,” and “wholesale-republished history” — are close to the refusal boundary, but the note repeatedly states that legitimacy, authorization, intent, accuracy, and fitness are refused questions.
- Disposition: No blocker; retain the refusal language and consider softening the charged terms per F-AM-R1-001/F-AM-R1-003.
- Cross-reference: Reader note Sections 1, 3, 5.4, and 7.

### F-AM-R1-005

- Identifier: F-AM-R1-005
- Severity: INFO
- Locus: Divergence figures, freshness/schema counts, and data-interface claims in Reader note Sections 4, 5.1, 5.2, 5.3, and 9.
- Substance: The surface numerical claims matched the substrate in the supplied reproduction, live reproduction, and independent recomputation: FY2023 identical; FY2024 divergent by 70 records and $58,072,427.23; FY2022 divergent by $0.75 at identical row count; community and official freshness lags 335/701/1066 and 456/822/1187 days; schema 23 versus 32 with 16 official-only and 7 community-only fields; revisions endpoint HTTP 404; system columns queryable.
- Disposition: Confirmed; no correction needed for the reproduced numerical and interface claims.
- Cross-reference: Mandatory Steps 1 through 5.

## 4. Verdict

Verdict: PASS.

Justification: All six mandatory steps were executed with pasted real outputs; the independent recomputation matched the expected values; the adversarial mutated-but-rehashed capture produced comparator DRIFT with exit code 2; and this report has zero CRITICAL and zero HIGH findings. The MEDIUM and LOW findings require wording/scope tightening but do not invalidate the reproduced substrate facts.

---

# Bismillah ir-Rahman ir-Rahim
