# Bismillah ir-Rahman ir-Rahim

# R0857 -- F-AM-R3 Audit Report — GPT 5.5 (OpenAI)

**Chronological Index:** 81 of 995  
**Date:** 2024-12-31  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** report (10).md  
**Source Format:** md  
**SHA-256:** `2d96099966c4cc9e4788b44eec3187a8fb427725fa814b4cf0aa5f594fa6e3cf`  

---

## R0857 · F-AM-R3 Audit Report — GPT 5.5 (OpenAI)

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: report (10).md
- source_format: md
- text_sha256: 2d96099966c4cc9e4788b44eec3187a8fb427725fa814b4cf0aa5f594fa6e3cf

# F-AM-R3 Audit Report — GPT 5.5 (OpenAI)

## 1. Member identity, lineage, new-relative-to-R1/R2 flag, role

- Member: GPT 5.5.
- Model lineage: OpenAI.
- New relative to R1/R2 clean qualifying pair: NO. GPT 5.5 was in the R1/R2 clean qualifying pair.
- Role: QUALIFYING, non-producer lineage.
- Artifact audited: Bayyinah al-Amāna Provenance Integrity packet v0.3 in `/home/user/workspace/R3-gpt55`.

## 2. Isolation attestation + no-prior-state attestation + command log summary

> I attest that I operated only within /home/user/workspace/R3-gpt55, did not list, read, search, or traverse any sibling, orchestrator, or workspace-root directory, and did not access another member's work.

I have no prior chat memory, saved state, personalization, or access to any prior round's report or another member's work; I executed this audit independently from this packet alone.

Command log is saved at `/home/user/workspace/R3-gpt55/command_log.txt`. Summary of logged operations:

- Initialized `command_log.txt`, listed and read only files inside `/home/user/workspace/R3-gpt55`.
- Unzipped the provided local `Bayyinah_ProvenanceIntegrity_ReproPackage.zip` into `/home/user/workspace/R3-gpt55/repro`.
- Read the local audit brief, reader note v0.3, companion v0.3, reproduction README, and reproduction script.
- Executed protocol steps 1–3 with the provided script.
- Wrote and ran fresh independent `urllib` code for protocol steps 4 and 5.
- Copied the local reproduction package to `/home/user/workspace/R3-gpt55/adversarial_repro`, mutated one captured value, rehashed its local manifest, and ran the comparator for protocol step 6.
- Gathered quoted textual loci using only local files in `/home/user/workspace/R3-gpt55`.
- Wrote this report to `/home/user/workspace/R3-gpt55/report.md`.

No command listed, read, searched, or traversed `/home/user/workspace` itself, any sibling `R3-*` directory, `R3-inspect`, any `model-council-*` file, or any other member's work. Outbound network access was limited to HTTPS calls made by the reproduction and independent-check code to `data.ny.gov`.

## 3. Execution status for each of the six steps

### Step 1 — `python3 repro/reproduce_paper3.py`

Status: PASS. Exit code 0. The hash equals `c49488723819d272beb6445435c724dfbf2050a363baf89d09a333a993e18201`.

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

### Step 2 — `python3 repro/reproduce_paper3.py --selftest`

Status: PASS. Exit code 0; 42 perturbations, 0 missed.

```text
[selftest] perturbing each captured value to confirm the comparator detects it...
[selftest] perturbed 42 captured values; comparator missed 0
EXIT_CODE=0

```

### Step 3 — `python3 repro/reproduce_paper3.py --live`

Status: PASS. Exit code 0; live pull reports no drift.

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

### Step 4 — Independent recompute with fresh code

Status: PASS. I wrote fresh `urllib` code and did not import or call functions from `repro/reproduce_paper3.py`. Exit code 0.

```text
#!/usr/bin/env python3
import json
import urllib.request
import urllib.parse
from decimal import Decimal, ROUND_HALF_UP
from datetime import date

PORTAL = "data.ny.gov"
SLUGS = ["gpsc-qqsz", "twsw-2mqa"]
FYS = ["2022", "2023", "2024"]

def get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "f-am-r3-gpt55-independent-recompute"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read().decode("utf-8")
        return json.loads(data)

def meta(slug):
    return get_json(f"https://{PORTAL}/api/views/{slug}.json")

def soda(slug, select, where):
    qs = urllib.parse.urlencode({"$select": select, "$where": where}, safe=":$(),*=.'-")
    return get_json(f"https://{PORTAL}/resource/{slug}.json?{qs}")

def money(x):
    if x is None:
        return None
    return Decimal(str(x)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def pct(num, den):
    if den == 0:
        return Decimal("0")
    return (Decimal(abs(num)) / Decimal(abs(den)) * Decimal("100"))

def lag_days(ts, close_yyyy_mm_dd):
    return (date.fromisoformat(ts[:10]) - date.fromisoformat(close_yyyy_mm_dd)).days

capture = {}
print("INDEPENDENT LIVE RECOMPUTE (fresh urllib code; no import/call to reproduction script)")
print(f"Portal: https://{PORTAL}")

for slug in SLUGS:
    m = meta(slug)
    fields = sorted([c.get("fieldName") for c in m.get("columns", []) if c.get("fieldName")])
    capture[slug] = {
        "name": m.get("name"),
        "provenance": m.get("provenance"),
        "rowsUpdatedAt": m.get("rowsUpdatedAt"),
        "fields": fields,
        "windows": {},
    }
    print(f"\nMETADATA {slug}")
    print(f"  name={m.get('name')!r}")
    print(f"  provenance={m.get('provenance')!r}")
    print(f"  rowsUpdatedAt={m.get('rowsUpdatedAt')!r}")
    print(f"  schema_field_count={len(fields)}")
    print("  schema_fields=" + ", ".join(fields))
    for fy in FYS:
        win = f"{fy}-12-31"
        where = f"fiscal_year_end_date='{fy}-12-31T00:00:00.000'"
        select = "count(*) as row_count, sum(contract_amount) as face_total, min(:created_at) as ca_min, max(:created_at) as ca_max, min(:updated_at) as ua_min, max(:updated_at) as ua_max"
        row = soda(slug, select, where)[0]
        rc = int(row["row_count"])
        ft = money(row.get("face_total"))
        ca_min = row.get("ca_min")
        ca_max = row.get("ca_max")
        ua_min = row.get("ua_min")
        ua_max = row.get("ua_max")
        capture[slug]["windows"][win] = {"row_count": rc, "face_total": ft, "ca_min": ca_min, "ca_max": ca_max, "ua_min": ua_min, "ua_max": ua_max}
        print(f"  WINDOW {win}: row_count={rc} face_total={ft} ca_min={ca_min} ca_max={ca_max} ua_min={ua_min} ua_max={ua_max} created_uniform={ca_min == ca_max} updated_uniform={ua_min == ua_max} created_lag_days={lag_days(ca_min, win)}")

print("\nPROVENANCE CONFIRMATION")
print(f"  gpsc-qqsz={capture['gpsc-qqsz']['provenance']} ; twsw-2mqa={capture['twsw-2mqa']['provenance']}")

print("\nDIVERGENCE BY FISCAL WINDOW (community gpsc-qqsz minus official twsw-2mqa)")
for fy in FYS:
    win = f"{fy}-12-31"
    g = capture["gpsc-qqsz"]["windows"][win]
    t = capture["twsw-2mqa"]["windows"][win]
    row_delta = g["row_count"] - t["row_count"]
    face_delta = g["face_total"] - t["face_total"]
    row_pct = pct(row_delta, g["row_count"])
    face_pct = pct(face_delta, g["face_total"])
    status = "IDENTICAL" if row_delta == 0 and face_delta == 0 else "DIVERGENT"
    print(f"  {win}: gpsc_rows={g['row_count']} twsw_rows={t['row_count']} row_delta={row_delta:+d} row_pct={row_pct:.4f}% gpsc_face={g['face_total']} twsw_face={t['face_total']} face_delta={face_delta:+.2f} face_pct={face_pct:.7f}% {status}")

print("\nFRESHNESS / UNIFORM TIMESTAMP CONFIRMATION")
for slug in SLUGS:
    for fy in FYS:
        win = f"{fy}-12-31"
        w = capture[slug]["windows"][win]
        print(f"  {slug} {win}: created_min={w['ca_min']} created_max={w['ca_max']} uniform_created={w['ca_min']==w['ca_max']} lag_days={lag_days(w['ca_min'], win)} updated_min={w['ua_min']} updated_max={w['ua_max']} uniform_updated={w['ua_min']==w['ua_max']}")

print("\nSCHEMA SET COMPARISON")
g_fields = set(capture["gpsc-qqsz"]["fields"])
t_fields = set(capture["twsw-2mqa"]["fields"])
official_only = sorted(t_fields - g_fields)
community_only = sorted(g_fields - t_fields)
print(f"  gpsc-qqsz field_count={len(g_fields)}")
print(f"  twsw-2mqa field_count={len(t_fields)}")
print(f"  official_only_count={len(official_only)} official_only={official_only}")
print(f"  community_only_count={len(community_only)} community_only={community_only}")

print("\nSUMMARY CONFIRMATIONS")
print("  provenance community/official confirmed:", capture['gpsc-qqsz']['provenance'] == 'community' and capture['twsw-2mqa']['provenance'] == 'official')
print("  FY2022 $0.75 divergence at identical 12156 row count confirmed:", capture['gpsc-qqsz']['windows']['2022-12-31']['row_count'] == 12156 and capture['twsw-2mqa']['windows']['2022-12-31']['row_count'] == 12156 and (capture['gpsc-qqsz']['windows']['2022-12-31']['face_total'] - capture['twsw-2mqa']['windows']['2022-12-31']['face_total']) == Decimal('-0.75'))
print("  FY2023 identical confirmed:", capture['gpsc-qqsz']['windows']['2023-12-31']['row_count'] == capture['twsw-2mqa']['windows']['2023-12-31']['row_count'] and capture['gpsc-qqsz']['windows']['2023-12-31']['face_total'] == capture['twsw-2mqa']['windows']['2023-12-31']['face_total'])
print("  FY2024 70 rows and $58,072,427.23 divergence confirmed:", (capture['gpsc-qqsz']['windows']['2024-12-31']['row_count'] - capture['twsw-2mqa']['windows']['2024-12-31']['row_count']) == 70 and (capture['gpsc-qqsz']['windows']['2024-12-31']['face_total'] - capture['twsw-2mqa']['windows']['2024-12-31']['face_total']) == Decimal('58072427.23'))
print("  uniform created timestamps confirmed:", all(capture[s]['windows'][f'{fy}-12-31']['ca_min'] == capture[s]['windows'][f'{fy}-12-31']['ca_max'] for s in SLUGS for fy in FYS))
print("  23-vs-32 schema and 16/7 split confirmed:", len(g_fields) == 23 and len(t_fields) == 32 and len(official_only) == 16 and len(community_only) == 7)

===== OUTPUT =====
INDEPENDENT LIVE RECOMPUTE (fresh urllib code; no import/call to reproduction script)
Portal: https://data.ny.gov

METADATA gpsc-qqsz
  name='MTA Procurement Report (All)'
  provenance='community'
  rowsUpdatedAt=1764609495
  schema_field_count=23
  schema_fields=amount_expended_for_fiscal_year, amount_expended_to_date, authority_name, award_date, award_process, begin_date, contract_amount, current_or_outstanding_balance, end_date, fiscal_year_end_date, number_of_bids_or_proposals_received, number_of_mwbe_proposals, procurement_description, procurements, solicited_mwbe, type_of_procurement, vendor_city, vendor_country, vendor_is_a_mwbe, vendor_name, vendor_postal_code, vendor_province_region, vendor_state
  WINDOW 2022-12-31: row_count=12156 face_total=54698007774.69 ca_min=2025-12-01T17:15:55.609Z ca_max=2025-12-01T17:15:55.609Z ua_min=2025-12-01T17:15:55.609Z ua_max=2025-12-01T17:15:55.609Z created_uniform=True updated_uniform=True created_lag_days=1066
  WINDOW 2023-12-31: row_count=12114 face_total=63569204049.36 ca_min=2025-12-01T17:15:55.609Z ca_max=2025-12-01T17:15:55.609Z ua_min=2025-12-01T17:15:55.609Z ua_max=2025-12-01T17:15:55.609Z created_uniform=True updated_uniform=True created_lag_days=701
  WINDOW 2024-12-31: row_count=13718 face_total=65189755228.64 ca_min=2025-12-01T17:15:55.609Z ca_max=2025-12-01T17:15:55.609Z ua_min=2025-12-01T17:15:55.609Z ua_max=2025-12-01T17:15:55.609Z created_uniform=True updated_uniform=True created_lag_days=335

METADATA twsw-2mqa
  name='MTA Procurements: Beginning 2018'
  provenance='official'
  rowsUpdatedAt=1775052776
  schema_field_count=32
  schema_fields=address_line_1, address_line_2, amount_expended_for_fiscal_year, amount_expended_to_date, award_date, award_process, basis_for_exemption, begin_date, city, contract_amount, country, current_or_outstanding_balance, end_date, exempt_from_article_4c, fair_market_value, fair_market_value_explanation, fiscal_year_end_date, number_of_bids_or_proposals_received, number_of_mwbe_proposals, postal_code, procurement_description, region, renewal_date, solicited_mwbe, state, status, transaction_number, type_of_procurement, vendor_is_a_mwbe, vendor_is_nys_or_fbe, vendor_name, zip_code_plus_4
  WINDOW 2022-12-31: row_count=12156 face_total=54698007775.44 ca_min=2026-04-01T14:09:46.913Z ca_max=2026-04-01T14:09:46.913Z ua_min=2026-04-01T14:09:46.913Z ua_max=2026-04-01T14:09:46.913Z created_uniform=True updated_uniform=True created_lag_days=1187
  WINDOW 2023-12-31: row_count=12114 face_total=63569204049.36 ca_min=2026-04-01T14:09:46.913Z ca_max=2026-04-01T14:09:46.913Z ua_min=2026-04-01T14:09:46.913Z ua_max=2026-04-01T14:09:46.913Z created_uniform=True updated_uniform=True created_lag_days=822
  WINDOW 2024-12-31: row_count=13648 face_total=65131682801.41 ca_min=2026-04-01T14:09:46.913Z ca_max=2026-04-01T14:09:46.913Z ua_min=2026-04-01T14:09:46.913Z ua_max=2026-04-01T14:09:46.913Z created_uniform=True updated_uniform=True created_lag_days=456

PROVENANCE CONFIRMATION
  gpsc-qqsz=community ; twsw-2mqa=official

DIVERGENCE BY FISCAL WINDOW (community gpsc-qqsz minus official twsw-2mqa)
  2022-12-31: gpsc_rows=12156 twsw_rows=12156 row_delta=+0 row_pct=0.0000% gpsc_face=54698007774.69 twsw_face=54698007775.44 face_delta=-0.75 face_pct=0.0000000% DIVERGENT
  2023-12-31: gpsc_rows=12114 twsw_rows=12114 row_delta=+0 row_pct=0.0000% gpsc_face=63569204049.36 twsw_face=63569204049.36 face_delta=+0.00 face_pct=0.0000000% IDENTICAL
  2024-12-31: gpsc_rows=13718 twsw_rows=13648 row_delta=+70 row_pct=0.5103% gpsc_face=65189755228.64 twsw_face=65131682801.41 face_delta=+58072427.23 face_pct=0.0890821% DIVERGENT

FRESHNESS / UNIFORM TIMESTAMP CONFIRMATION
  gpsc-qqsz 2022-12-31: created_min=2025-12-01T17:15:55.609Z created_max=2025-12-01T17:15:55.609Z uniform_created=True lag_days=1066 updated_min=2025-12-01T17:15:55.609Z updated_max=2025-12-01T17:15:55.609Z uniform_updated=True
  gpsc-qqsz 2023-12-31: created_min=2025-12-01T17:15:55.609Z created_max=2025-12-01T17:15:55.609Z uniform_created=True lag_days=701 updated_min=2025-12-01T17:15:55.609Z updated_max=2025-12-01T17:15:55.609Z uniform_updated=True
  gpsc-qqsz 2024-12-31: created_min=2025-12-01T17:15:55.609Z created_max=2025-12-01T17:15:55.609Z uniform_created=True lag_days=335 updated_min=2025-12-01T17:15:55.609Z updated_max=2025-12-01T17:15:55.609Z uniform_updated=True
  twsw-2mqa 2022-12-31: created_min=2026-04-01T14:09:46.913Z created_max=2026-04-01T14:09:46.913Z uniform_created=True lag_days=1187 updated_min=2026-04-01T14:09:46.913Z updated_max=2026-04-01T14:09:46.913Z uniform_updated=True
  twsw-2mqa 2023-12-31: created_min=2026-04-01T14:09:46.913Z created_max=2026-04-01T14:09:46.913Z uniform_created=True lag_days=822 updated_min=2026-04-01T14:09:46.913Z updated_max=2026-04-01T14:09:46.913Z uniform_updated=True
  twsw-2mqa 2024-12-31: created_min=2026-04-01T14:09:46.913Z created_max=2026-04-01T14:09:46.913Z uniform_created=True lag_days=456 updated_min=2026-04-01T14:09:46.913Z updated_max=2026-04-01T14:09:46.913Z uniform_updated=True

SCHEMA SET COMPARISON
  gpsc-qqsz field_count=23
  twsw-2mqa field_count=32
  official_only_count=16 official_only=['address_line_1', 'address_line_2', 'basis_for_exemption', 'city', 'country', 'exempt_from_article_4c', 'fair_market_value', 'fair_market_value_explanation', 'postal_code', 'region', 'renewal_date', 'state', 'status', 'transaction_number', 'vendor_is_nys_or_fbe', 'zip_code_plus_4']
  community_only_count=7 community_only=['authority_name', 'procurements', 'vendor_city', 'vendor_country', 'vendor_postal_code', 'vendor_province_region', 'vendor_state']

SUMMARY CONFIRMATIONS
  provenance community/official confirmed: True
  FY2022 $0.75 divergence at identical 12156 row count confirmed: True
  FY2023 identical confirmed: True
  FY2024 70 rows and $58,072,427.23 divergence confirmed: True
  uniform created timestamps confirmed: True
  23-vs-32 schema and 16/7 split confirmed: True
EXIT_CODE=0

```

### Step 5 — Data-interface facts

Status: PASS. Both `/api/views/<slug>/revisions.json` endpoints returned HTTP 404, and `:created_at`/`:updated_at` system-column queries returned HTTP 200 with parsed results. Exit code 0.

```text
#!/usr/bin/env python3
import json
import urllib.request
import urllib.parse
import urllib.error

PORTAL = "data.ny.gov"
SLUGS = ["gpsc-qqsz", "twsw-2mqa"]

def http_status_and_body(url):
    req = urllib.request.Request(url, headers={"User-Agent": "f-am-r3-gpt55-interface-check"})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return resp.getcode(), resp.read().decode("utf-8", "replace")[:500]
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")[:500]
        return e.code, body

def system_query(slug):
    params = {
        "$select": "count(*) as n, min(:created_at) as ca_min, max(:updated_at) as ua_max",
        "$limit": "1",
    }
    qs = urllib.parse.urlencode(params, safe=":$(),*")
    return f"https://{PORTAL}/resource/{slug}.json?{qs}"

print("DATA-INTERFACE CHECKS")
for slug in SLUGS:
    rev_url = f"https://{PORTAL}/api/views/{slug}/revisions.json"
    code, body = http_status_and_body(rev_url)
    print(f"REVISIONS {slug}: url={rev_url} HTTP_STATUS={code} body_prefix={body[:160]!r}")

for slug in SLUGS:
    q = system_query(slug)
    code, body = http_status_and_body(q)
    print(f"SYSTEM_COLUMNS {slug}: url={q} HTTP_STATUS={code} body={body!r}")
    if code == 200:
        parsed = json.loads(body)
        first = parsed[0] if parsed else {}
        print(f"SYSTEM_COLUMNS_PARSED {slug}: n={first.get('n')} ca_min={first.get('ca_min')} ua_max={first.get('ua_max')}")

===== OUTPUT =====
DATA-INTERFACE CHECKS
REVISIONS gpsc-qqsz: url=https://data.ny.gov/api/views/gpsc-qqsz/revisions.json HTTP_STATUS=404 body_prefix='{\n  "code" : "not_found",\n  "error" : true,\n  "message" : "No service found for this URL."\n}\n'
REVISIONS twsw-2mqa: url=https://data.ny.gov/api/views/twsw-2mqa/revisions.json HTTP_STATUS=404 body_prefix='{\n  "code" : "not_found",\n  "error" : true,\n  "message" : "No service found for this URL."\n}\n'
SYSTEM_COLUMNS gpsc-qqsz: url=https://data.ny.gov/resource/gpsc-qqsz.json?$select=count(*)+as+n,+min(:created_at)+as+ca_min,+max(:updated_at)+as+ua_max&$limit=1 HTTP_STATUS=200 body='[{"n":"111879","ca_min":"2025-12-01T17:15:55.609Z","ua_max":"2025-12-01T17:15:55.609Z"}]\n'
SYSTEM_COLUMNS_PARSED gpsc-qqsz: n=111879 ca_min=2025-12-01T17:15:55.609Z ua_max=2025-12-01T17:15:55.609Z
SYSTEM_COLUMNS twsw-2mqa: url=https://data.ny.gov/resource/twsw-2mqa.json?$select=count(*)+as+n,+min(:created_at)+as+ca_min,+max(:updated_at)+as+ua_max&$limit=1 HTTP_STATUS=200 body='[{"n":"107503","ca_min":"2026-04-01T14:09:46.913Z","ua_max":"2026-04-01T14:09:46.913Z"}]\n'
SYSTEM_COLUMNS_PARSED twsw-2mqa: n=107503 ca_min=2026-04-01T14:09:46.913Z ua_max=2026-04-01T14:09:46.913Z
EXIT_CODE=0

```

### Step 6 — Adversarial mutate, rehash, comparator drift

Status: PASS. The copied snapshot was mutated, the copied `MANIFEST.json` was rehashed so the integrity gate passed, and the live comparator returned DRIFT with nonzero exit code 2.

```text
===== MUTATE AND REHASH =====
MUTATION target=datasets/gpsc-qqsz/fiscal_windows/2024-12-31/row_count
MUTATION old_value=13718 new_value=13719
REHASHED_MANIFEST_SHA256=e21187546b35bd4fcdb37aadb99bbf7a05004bc0ee4792a6645abd0050406af9

===== INTEGRITY CHECK AFTER REHASH: python3 adversarial_repro/reproduce_paper3.py =====
[integrity] capture retrieved_utc: 2026-07-19T22:07:28Z

Check 1 -- Provenance classification and divergence
  gpsc-qqsz   provenance=community (MTA Procurement Report (All))
  twsw-2mqa   provenance=official  (MTA Procurements: Beginning 2018)
  2022-12-31 community-vs-official: rows d=+0 (0.0000%), face d=$-0.75 (0.0000000%)  [DIVERGENT]
  2023-12-31 community-vs-official: rows d=+0 (0.0000%), face d=$+0.00 (0.0000000%)  [identical]
  2024-12-31 community-vs-official: rows d=+71 (0.5175%), face d=$+58072427.23 (0.0890821%)  [DIVERGENT]
  [note] even at identical row count, FY2022 diverges by $0.75 in summed face value -- a value-level difference a coarse (billion-rounded) view misses.

Check 2 -- Snapshot integrity
  SHA-256 OK (e21187546b35bd4f...)

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
INTEGRITY_EXIT_CODE=0

===== COMPARATOR AFTER HASH-GATE DEFEAT: python3 adversarial_repro/reproduce_paper3.py --live =====
[live] re-pulling data.ny.gov and comparing to the frozen capture...
[live] DRIFT detected on 1 value(s):
  gpsc-qqsz/2024-12-31/row_count: frozen=13719 live=13718
COMPARATOR_EXIT_CODE=2

```

## 4. Audit-scope confirmations/disputes

- Tier discipline: Confirmed. Reader note Section 3 states Tier 1 covers hash/counts/schema/byte identity/system timestamps; Tier 2 covers Socrata-declared provenance, freshness reconciliation, and a post-close batch inference; Tier 3 refuses legitimacy/intent judgments. Quoted loci: reader lines 35, 37, and 39 in `textual_loci.txt`.
- Refusal boundary: Confirmed as to accusations or legitimacy judgments. The reader note says the method "refuses to judge whether any was legitimate, authorized, or improper" in the Abstract (line 17), "does not adjudicate" legitimacy in Section 1 (line 23), and in Section 5.4 "does not conclude that the community view is unauthorized, that any batch load was improper, that the FY2024 divergence is an error in either dataset, or that any party intended to mislead" (line 63). I found no assertion that a divergence, batch load, or edit is illegitimate, unauthorized, improper, deceptive, malicious, or manipulative.
- Three-resolution divergence: Confirmed by executed reproduction and independent live recompute. Step 4 independently produced FY2022 row_delta `+0` and face_delta `-0.75`; FY2023 row_delta `+0` and face_delta `+0.00`; FY2024 row_delta `+70` and face_delta `+58072427.23`.
- Freshness lags: Confirmed by executed reproduction and independent live recompute. Step 4 independently produced community created lags 1066 / 701 / 335 days for FY2022 / FY2023 / FY2024 and official created lags 1187 / 822 / 456 days for FY2022 / FY2023 / FY2024, all with uniform `:created_at` and `:updated_at` within each queried window.
- Schema counts: Confirmed by executed reproduction and independent live recompute. Step 4 independently produced `gpsc-qqsz` field_count 23, `twsw-2mqa` field_count 32, official_only_count 16, community_only_count 7.
- Data-interface facts: Confirmed by step 5. Both revisions endpoints returned HTTP 404; both system-column aggregate queries returned HTTP 200.
- Dispute/qualification: I found one residual wording issue in reader Section 1, line 23: "an observed divergence or republish". I do not read it as an accusation or legitimacy judgment, and the core result sections now correctly use the indistinguishable alternatives, but it is a remaining bare/imprecise "republish" phrase outside the specific R2 loci. I record it below as F-AM-R3-001 (LOW).

## 5. Regression confirmations (F-AM-R2-001/002/003) with quoted loci

### F-AM-R2-001 — recurring "republish" over-claim

Disposition: Mostly resolved in the specified R2 loci, with one low-severity residual whole-note wording issue.

Quoted resolved loci:

- Abstract, reader line 17: "in a single post-close batch (consistent with a wholesale republish and equally with a first-time bulk load, which a single-pull timestamp cannot distinguish)".
- Section 3, reader line 37: "a batch that a single pull cannot resolve into a republish versus a first-time bulk load".
- Section 5.2, reader line 55: "consistent with a wholesale republish of previously-served history and equally consistent with a first-time bulk load...; a single live pull cannot distinguish the two, and the note claims only the batch-after-close fact".
- Section 5.4, reader line 63: "post-close-batch inference (a batch load after the period close, which a single pull does not resolve into a republish versus a first-time bulk load)".
- Section 6, reader line 67: "post-close-batch checks".
- Section 7, reader line 71: "reports as a post-close batch load (a republish or a first-time bulk load, which a single pull cannot distinguish)".
- Tool output in steps 1 and 3: "POST-CLOSE-BATCH = uniform :created_at postdating the period close (one batch load); a single pull does not distinguish a republish from a first-time bulk load."

Whole-note search result: `grep -ni 'republish' Bayyinah_ProvenanceIntegrity_v0.3.md` found no surviving claim in Sections 5.4, 6, or 7 that a republish occurred as a method result. However, reader line 23 says: "it does not adjudicate whether an observed divergence or republish was a correction, a migration, an error, or a manipulation." Because "observed ... republish" is not phrased as one of the two indistinguishable alternatives, I record a LOW wording finding.

### F-AM-R2-002 — companion header current-status version

Disposition: Resolved. Companion line 3 reads: "Companion to: *Bayyinah al-Amāna: Provenance Integrity for Public Open Data* (the reader-facing note, v0.3)." Companion line 5 reads: "Mirrors note state v0.3 (two qualifying cross-instance audit passes, F-AM-R1 and F-AM-R2; the consecutive qualifying-PASS count is TWO...)". Current State line 9 says "as of v0.3" and line 11 says "v0.3 reader note plus this companion". Stale v0.1/v0.2 occurrences are append-only historical context, not current-status loci.

### F-AM-R2-003 — companion Audit rounds placeholder

Disposition: Resolved. Companion line 40 reads: "Appended below as dated append-only appendices: F-AM-R1 (v0.1 -> v0.2) and F-AM-R2 (v0.2 -> v0.3). [Superseded per Section 14.5: the original 'None yet' placeholder is retained here in spirit only; the round appendices follow.]" This no longer states "None yet" as current and correctly points to the appended F-AM-R1 and F-AM-R2 appendices.

## 6. Status-propagation check result

Result: PASS. Current-status loci are mutually consistent on version v0.3, consecutive qualifying-PASS counter TWO, and two-round history F-AM-R1/F-AM-R2. Appendices preserve earlier v0.1/v0.2 states and are correct in context.

Quoted current-status loci:

1. Reader note header, line 7: "Working draft v0.3 (two qualifying cross-instance audit passes, F-AM-R1 and F-AM-R2: the consecutive qualifying-PASS count is TWO... a confirming round on this corrected v0.3 is recommended...)".
2. Reader note Section 8, line 75: "This is a v0.3 draft... Two such passes have occurred (F-AM-R1 and F-AM-R2... ), so the consecutive qualifying-PASS count is two... all absorbed in this v0.3...".
3. Companion header line 3: "Companion to: ... (the reader-facing note, v0.3)."
4. Companion header line 5: "Mirrors note state v0.3 (two qualifying cross-instance audit passes, F-AM-R1 and F-AM-R2; the consecutive qualifying-PASS count is TWO...)".
5. Companion Current State header line 9: "## Current State (authoritative, as of v0.3)".
6. Companion artifact-state line 11: "v0.3 reader note plus this companion and the reproduction package...".
7. Companion counter line 12: "Consecutive qualifying-PASS count (single operational counter): TWO. Two qualifying rounds have occurred (F-AM-R1 and F-AM-R2...)".
8. Companion independent audit history line 13: "Independent audit history: two rounds. F-AM-R1... F-AM-R2...".

## 7. Findings (six-element format, F-AM-R3 namespace)

1. **Identifier:** F-AM-R3-001.
   **Severity:** LOW.
   **Locus:** Reader note v0.3, Section 1, line 23.
   **Substance as surface-vs-substrate divergence:** Surface correction says a single-pull uniform timestamp supports only a post-close batch load, not a resolved republish; substrate wording at line 23 says "an observed divergence or republish," which can be read as a bare/imprecise republish observation rather than as "republish or first-time bulk load, indistinguishable from a single pull." This is not an accusation, not a result-table claim, and not in the specific R2 loci (Sections 5.4/6/7), but it is a remaining whole-note wording survivor.
   **Disposition:** Open wording cleanup recommended: replace with "an observed divergence or post-close batch load" or "an observed divergence or batch load (republish or first-time bulk load, indistinguishable from a single pull)." Non-blocking for qualifying PASS because severity is LOW and no reproduced numerical/interface claim is affected.
   **Cross-reference:** F-AM-R2-001 and reader note lines 37, 55, 63, and 71, which correctly state the indistinguishable alternatives.

No CRITICAL or HIGH findings.

## 8. Verdict: PASS / INCOMPLETE / FAIL, with reason

Verdict: **PASS**.

Reason: I maintained isolation, executed all six mandatory reproduction steps with pasted real outputs and exit codes, independently recomputed the live data.ny.gov facts, confirmed the adversarial hash-gate-defeat comparator DRIFT behavior, and found zero CRITICAL and zero HIGH findings. I record one LOW wording finding (F-AM-R3-001) concerning a residual imprecise "observed ... republish" phrase in Section 1, but it does not affect the reproduced substrate facts or the qualifying PASS criterion.

---

# Bismillah ir-Rahman ir-Rahim
