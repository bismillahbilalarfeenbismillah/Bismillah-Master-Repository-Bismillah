# Bismillah ir-Rahman ir-Rahim

# R0455 -- F-AM-R2 audit report (GPT 5.4)

**Chronological Index:** 76 of 995  
**Date:** 2024-12-31  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-AM-R2_gpt54.md  
**Source Format:** md  
**SHA-256:** `ba0f239be1b53a4abd48add115c2ac90c85ce1c820b5fb74ce3c128b99a8434e`  

---

## R0455 · F-AM-R2 audit report (GPT 5.4)

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-AM-R2_gpt54.md
- source_format: md
- text_sha256: ba0f239be1b53a4abd48add115c2ac90c85ce1c820b5fb74ce3c128b99a8434e

# F-AM-R2 audit report (GPT 5.4)

## Scope and execution-status note

Model: GPT 5.4 (OpenAI), qualifying non-producer auditor.

Working directory used for the audit: `/home/user/workspace/audit_r2/gpt_5_4/`.

I executed all six requested reproduction steps and captured real outputs below.

Important protocol note: I cannot honestly make the exact requested isolation attestation. After the required reproductions were already underway, I accidentally ran one workspace-wide grep that touched other round directories. I therefore do **not** claim full compliance with the "worked only from my own directory copy / did not access any other member's work" condition. Because that binding operating condition was breached by this audit instance, my overall verdict is **INCOMPLETE**, even though the artifact itself reproduced and my artifact-level findings stayed below HIGH.

## Step 1

Command:

```bash
cd /home/user/workspace/audit_r2/gpt_5_4 && python3 reproduce_paper3.py; code=$?; printf '\nEXIT_CODE=%s\n' "$code"
```

Real output:

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

## Step 2

Command:

```bash
cd /home/user/workspace/audit_r2/gpt_5_4 && python3 reproduce_paper3.py --selftest; code=$?; printf '\nEXIT_CODE=%s\n' "$code"
```

Real output:

```text
[selftest] perturbing each captured value to confirm the comparator detects it...
[selftest] perturbed 42 captured values; comparator missed 0

EXIT_CODE=0
```

## Step 3

Command:

```bash
cd /home/user/workspace/audit_r2/gpt_5_4 && python3 reproduce_paper3.py --live; code=$?; printf '\nEXIT_CODE=%s\n' "$code"
```

Real output:

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

## Step 4 -- independent recompute with separate code

Code used (`independent_recompute_step4.py`):

```python
#!/usr/bin/env python3
import json
import urllib.parse
import urllib.request
from decimal import Decimal
from datetime import date

PORTAL = 'https://data.ny.gov'
SLUGS = ['gpsc-qqsz', 'twsw-2mqa']
FYS = ['2022', '2023', '2024']


def get_json(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'gpt-5-4-independent-recompute'})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode('utf-8'))


def days_after_close(ts, fy):
    return (date.fromisoformat(ts[:10]) - date.fromisoformat(f'{fy}-12-31')).days


def metadata(slug):
    url = f'{PORTAL}/api/views/{slug}.json'
    data = get_json(url)
    fields = sorted(col['fieldName'] for col in data.get('columns', []) if col.get('fieldName'))
    return {
        'url': url,
        'name': data.get('name'),
        'provenance': data.get('provenance'),
        'field_count': len(fields),
        'fields': fields,
    }


def fiscal_aggregate(slug, fy):
    select = (
        'count(*) as row_count, '
        'sum(contract_amount) as face_total, '
        'min(:created_at) as created_min, '
        'max(:created_at) as created_max, '
        'min(:updated_at) as updated_min, '
        'max(:updated_at) as updated_max'
    )
    where = f"fiscal_year_end_date='{fy}-12-31T00:00:00.000'"
    url = f"{PORTAL}/resource/{slug}.json?" + urllib.parse.urlencode({'$select': select, '$where': where})
    row = get_json(url)[0]
    return {
        'url': url,
        'row_count': int(row['row_count']),
        'face_total': Decimal(row['face_total']).quantize(Decimal('0.01')),
        'created_min': row['created_min'],
        'created_max': row['created_max'],
        'updated_min': row['updated_min'],
        'updated_max': row['updated_max'],
    }


def main():
    meta = {slug: metadata(slug) for slug in SLUGS}
    print('STEP 4 INDEPENDENT RECOMPUTE')
    print('Metadata:')
    for slug in SLUGS:
        m = meta[slug]
        print(f"- {slug}: name={m['name']!r}, provenance={m['provenance']!r}, field_count={m['field_count']}")
        print(f"  metadata_url={m['url']}")
    official_only = sorted(set(meta['twsw-2mqa']['fields']) - set(meta['gpsc-qqsz']['fields']))
    community_only = sorted(set(meta['gpsc-qqsz']['fields']) - set(meta['twsw-2mqa']['fields']))
    print(f"Schema comparison: gpsc-qqsz={meta['gpsc-qqsz']['field_count']} fields, twsw-2mqa={meta['twsw-2mqa']['field_count']} fields")
    print(f'official_only_count={len(official_only)}')
    print('official_only_fields=' + ', '.join(official_only))
    print(f'community_only_count={len(community_only)}')
    print('community_only_fields=' + ', '.join(community_only))
    print('\nFiscal aggregates:')
    aggs = {slug: {} for slug in SLUGS}
    for fy in FYS:
        for slug in SLUGS:
            aggs[slug][fy] = fiscal_aggregate(slug, fy)
            a = aggs[slug][fy]
            print(
                f"- {slug} FY{fy}: row_count={a['row_count']}, face_total={a['face_total']}, "
                f"created_min={a['created_min']}, created_max={a['created_max']}, "
                f"updated_min={a['updated_min']}, updated_max={a['updated_max']}, "
                f"created_days_after_close={days_after_close(a['created_min'], fy)}"
            )
            print(f"  aggregate_url={a['url']}")
    print('\nDivergence summary (gpsc-qqsz minus twsw-2mqa):')
    for fy in FYS:
        g = aggs['gpsc-qqsz'][fy]
        t = aggs['twsw-2mqa'][fy]
        row_diff = g['row_count'] - t['row_count']
        face_diff = (g['face_total'] - t['face_total']).quantize(Decimal('0.01'))
        row_pct = (Decimal(abs(row_diff)) / Decimal(g['row_count']) * Decimal('100')).quantize(Decimal('0.0001'))
        face_pct = (Decimal(abs(face_diff)) / g['face_total'] * Decimal('100')).quantize(Decimal('0.0001'))
        print(
            f"- FY{fy}: row_diff={row_diff}, face_diff={face_diff}, row_pct={row_pct}%, face_pct={face_pct}%"
        )
        print(
            f"  creation_uniformity: gpsc={g['created_min'] == g['created_max']}, twsw={t['created_min'] == t['created_max']}"
        )
        print(
            f"  update_uniformity: gpsc={g['updated_min'] == g['updated_max']}, twsw={t['updated_min'] == t['updated_max']}"
        )


if __name__ == '__main__':
    main()
```

Command:

```bash
cd /home/user/workspace/audit_r2/gpt_5_4 && python3 independent_recompute_step4.py; code=$?; printf '\nEXIT_CODE=%s\n' "$code"
```

Real output:

```text
STEP 4 INDEPENDENT RECOMPUTE
Metadata:
- gpsc-qqsz: name='MTA Procurement Report (All)', provenance='community', field_count=23
  metadata_url=https://data.ny.gov/api/views/gpsc-qqsz.json
- twsw-2mqa: name='MTA Procurements: Beginning 2018', provenance='official', field_count=32
  metadata_url=https://data.ny.gov/api/views/twsw-2mqa.json
Schema comparison: gpsc-qqsz=23 fields, twsw-2mqa=32 fields
official_only_count=16
official_only_fields=address_line_1, address_line_2, basis_for_exemption, city, country, exempt_from_article_4c, fair_market_value, fair_market_value_explanation, postal_code, region, renewal_date, state, status, transaction_number, vendor_is_nys_or_fbe, zip_code_plus_4
community_only_count=7
community_only_fields=authority_name, procurements, vendor_city, vendor_country, vendor_postal_code, vendor_province_region, vendor_state

Fiscal aggregates:
- gpsc-qqsz FY2022: row_count=12156, face_total=54698007774.69, created_min=2025-12-01T17:15:55.609Z, created_max=2025-12-01T17:15:55.609Z, updated_min=2025-12-01T17:15:55.609Z, updated_max=2025-12-01T17:15:55.609Z, created_days_after_close=1066
  aggregate_url=https://data.ny.gov/resource/gpsc-qqsz.json?%24select=count%28%2A%29+as+row_count%2C+sum%28contract_amount%29+as+face_total%2C+min%28%3Acreated_at%29+as+created_min%2C+max%28%3Acreated_at%29+as+created_max%2C+min%28%3Aupdated_at%29+as+updated_min%2C+max%28%3Aupdated_at%29+as+updated_max&%24where=fiscal_year_end_date%3D%272022-12-31T00%3A00%3A00.000%27
- twsw-2mqa FY2022: row_count=12156, face_total=54698007775.44, created_min=2026-04-01T14:09:46.913Z, created_max=2026-04-01T14:09:46.913Z, updated_min=2026-04-01T14:09:46.913Z, updated_max=2026-04-01T14:09:46.913Z, created_days_after_close=1187
  aggregate_url=https://data.ny.gov/resource/twsw-2mqa.json?%24select=count%28%2A%29+as+row_count%2C+sum%28contract_amount%29+as+face_total%2C+min%28%3Acreated_at%29+as+created_min%2C+max%28%3Acreated_at%29+as+created_max%2C+min%28%3Aupdated_at%29+as+updated_min%2C+max%28%3Aupdated_at%29+as+updated_max&%24where=fiscal_year_end_date%3D%272022-12-31T00%3A00%3A00.000%27
- gpsc-qqsz FY2023: row_count=12114, face_total=63569204049.36, created_min=2025-12-01T17:15:55.609Z, created_max=2025-12-01T17:15:55.609Z, updated_min=2025-12-01T17:15:55.609Z, updated_max=2025-12-01T17:15:55.609Z, created_days_after_close=701
  aggregate_url=https://data.ny.gov/resource/gpsc-qqsz.json?%24select=count%28%2A%29+as+row_count%2C+sum%28contract_amount%29+as+face_total%2C+min%28%3Acreated_at%29+as+created_min%2C+max%28%3Acreated_at%29+as+created_max%2C+min%28%3Aupdated_at%29+as+updated_min%2C+max%28%3Aupdated_at%29+as+updated_max&%24where=fiscal_year_end_date%3D%272023-12-31T00%3A00%3A00.000%27
- twsw-2mqa FY2023: row_count=12114, face_total=63569204049.36, created_min=2026-04-01T14:09:46.913Z, created_max=2026-04-01T14:09:46.913Z, updated_min=2026-04-01T14:09:46.913Z, updated_max=2026-04-01T14:09:46.913Z, created_days_after_close=822
  aggregate_url=https://data.ny.gov/resource/twsw-2mqa.json?%24select=count%28%2A%29+as+row_count%2C+sum%28contract_amount%29+as+face_total%2C+min%28%3Acreated_at%29+as+created_min%2C+max%28%3Acreated_at%29+as+created_max%2C+min%28%3Aupdated_at%29+as+updated_min%2C+max%28%3Aupdated_at%29+as+updated_max&%24where=fiscal_year_end_date%3D%272023-12-31T00%3A00%3A00.000%27
- gpsc-qqsz FY2024: row_count=13718, face_total=65189755228.64, created_min=2025-12-01T17:15:55.609Z, created_max=2025-12-01T17:15:55.609Z, updated_min=2025-12-01T17:15:55.609Z, updated_max=2025-12-01T17:15:55.609Z, created_days_after_close=335
  aggregate_url=https://data.ny.gov/resource/gpsc-qqsz.json?%24select=count%28%2A%29+as+row_count%2C+sum%28contract_amount%29+as+face_total%2C+min%28%3Acreated_at%29+as+created_min%2C+max%28%3Acreated_at%29+as+created_max%2C+min%28%3Aupdated_at%29+as+updated_min%2C+max%28%3Aupdated_at%29+as+updated_max&%24where=fiscal_year_end_date%3D%272024-12-31T00%3A00%3A00.000%27
- twsw-2mqa FY2024: row_count=13648, face_total=65131682801.41, created_min=2026-04-01T14:09:46.913Z, created_max=2026-04-01T14:09:46.913Z, updated_min=2026-04-01T14:09:46.913Z, updated_max=2026-04-01T14:09:46.913Z, created_days_after_close=456
  aggregate_url=https://data.ny.gov/resource/twsw-2mqa.json?%24select=count%28%2A%29+as+row_count%2C+sum%28contract_amount%29+as+face_total%2C+min%28%3Acreated_at%29+as+created_min%2C+max%28%3Acreated_at%29+as+created_max%2C+min%28%3Aupdated_at%29+as+updated_min%2C+max%28%3Aupdated_at%29+as+updated_max&%24where=fiscal_year_end_date%3D%272024-12-31T00%3A00%3A00.000%27

Divergence summary (gpsc-qqsz minus twsw-2mqa):
- FY2022: row_diff=0, face_diff=-0.75, row_pct=0.0000%, face_pct=0.0000%
  creation_uniformity: gpsc=True, twsw=True
  update_uniformity: gpsc=True, twsw=True
- FY2023: row_diff=0, face_diff=0.00, row_pct=0.0000%, face_pct=0.0000%
  creation_uniformity: gpsc=True, twsw=True
  update_uniformity: gpsc=True, twsw=True
- FY2024: row_diff=70, face_diff=58072427.23, row_pct=0.5103%, face_pct=0.0891%
  creation_uniformity: gpsc=True, twsw=True
  update_uniformity: gpsc=True, twsw=True

EXIT_CODE=0
```

Conclusion from step 4: independently reproduced. Provenance classifications matched (`community` / `official`), schema matched (23 vs 32, with 16 official-only and 7 community-only), FY2022 reproduced the $0.75 value-level divergence at equal row count, FY2023 matched exactly, FY2024 reproduced the 70-row and $58,072,427.23 divergence, and both datasets showed uniform `:created_at` / `:updated_at` within each fiscal window.

## Step 5 -- data-interface facts

Command:

```bash
cd /home/user/workspace/audit_r2/gpt_5_4 && {
  echo '--- revisions endpoint ---'
  curl -i -sS https://data.ny.gov/api/views/twsw-2mqa/revisions.json
  echo
  echo '--- gpsc system columns ---'
  curl -sS 'https://data.ny.gov/resource/gpsc-qqsz.json?%24select=%3Acreated_at%2C%3Aupdated_at&%24limit=1'
  echo
  echo '--- twsw system columns ---'
  curl -sS 'https://data.ny.gov/resource/twsw-2mqa.json?%24select=%3Acreated_at%2C%3Aupdated_at&%24limit=1'
}; code=$?; printf '\nEXIT_CODE=%s\n' "$code"
```

Real output:

```text
--- revisions endpoint ---
HTTP/1.1 404 Not Found
Server: nginx
Date: Sun, 19 Jul 2026 22:52:00 GMT
Content-Type: application/json; charset=utf-8
Transfer-Encoding: chunked
Connection: keep-alive
Access-Control-Allow-Origin: *
X-Error-Code: not_found
X-Error-Message: No service found for this URL.
X-Socrata-RequestId: 3e52e064a105fd90cd6833b9831312b7
Strict-Transport-Security: max-age=31536000; includeSubDomains

{
  "code" : "not_found",
  "error" : true,
  "message" : "No service found for this URL."
}

--- gpsc system columns ---
[{":created_at":"2025-12-01T17:15:55.609Z",":updated_at":"2025-12-01T17:15:55.609Z"}]

--- twsw system columns ---
[{":created_at":"2026-04-01T14:09:46.913Z",":updated_at":"2026-04-01T14:09:46.913Z"}]

EXIT_CODE=0
```

Conclusion from step 5: `/api/views/twsw-2mqa/revisions.json` returned HTTP 404, and `:created_at` / `:updated_at` were publicly queryable on both datasets.

## Step 6 -- adversarial mutate-and-rehash test

Command used:

```bash
python3 - <<'PY'
import os, json, hashlib, shutil
src = '/home/user/workspace/audit_r2/gpt_5_4'
dst = '/home/user/workspace/audit_r2/gpt_5_4/scratch_mutation'
if os.path.exists(dst):
    pass
shutil.copytree(src, dst, dirs_exist_ok=True)
cap_path = os.path.join(dst, 'snapshot', 'provenance_capture.json')
man_path = os.path.join(dst, 'snapshot', 'MANIFEST.json')
with open(cap_path) as f:
    cap = json.load(f)
old = cap['datasets']['gpsc-qqsz']['fiscal_windows']['2024-12-31']['row_count']
cap['datasets']['gpsc-qqsz']['fiscal_windows']['2024-12-31']['row_count'] = 99999
with open(cap_path, 'w') as f:
    json.dump(cap, f, indent=2, sort_keys=True)
raw = open(cap_path, 'rb').read()
sha = hashlib.sha256(raw).hexdigest()
with open(man_path, 'w') as f:
    json.dump({'sha256': sha}, f, indent=2)
print('MUTATED_FROM', old)
print('MUTATED_TO', 99999)
print('NEW_SHA256', sha)
PY
cd /home/user/workspace/audit_r2/gpt_5_4/scratch_mutation && python3 reproduce_paper3.py --live; code=$?; printf '\nEXIT_CODE=%s\n' "$code"
```

Real output:

```text
MUTATED_FROM 13718
MUTATED_TO 99999
NEW_SHA256 b5608c6575fde8c741ed9b32b72cfa9a8c24c490cac2b4113fa5466dd313be67
[live] re-pulling data.ny.gov and comparing to the frozen capture...
[live] DRIFT detected on 1 value(s):
  gpsc-qqsz/2024-12-31/row_count: frozen=99999 live=13718

EXIT_CODE=2
```

Conclusion from step 6: the manifest re-hash defeated the integrity abort, but the live comparator still returned DRIFT / exit 2, as required.

## Regression checks

### F-AM-R1-S-001 (republish over-claim)

- Reader note **Abstract** is appropriately hedged: it says the single post-close batch is "consistent with a wholesale republish and equally with a first-time bulk load, which a single-pull timestamp cannot distinguish."
- Reader note **Section 3 Tier-2** is appropriately hedged: it says the single pull cannot resolve a batch into republish versus first-time bulk load.
- Reader note **Section 5.2** is appropriately hedged and correctly claims only the batch-after-close fact.
- The **tool flag** is correctly `POST-CLOSE-BATCH`, and the tool note says a single pull does not distinguish republish from first-time bulk load.
- **Dispute / unresolved regression:** reader note **Section 5.4** still says Tier 2 emits "the republish inference" and refers to "the republishes"; reader note **Section 7** says the method "reports as a republish rather than reconstructing what changed." Those loci still present republish as the method's output rather than preserving the batch-versus-first-load ambiguity.

### F-AM-R1-S-002 (provenance wording)

Confirmed resolved. Reader note Section 2 and Section 3 both label provenance as the Socrata-declared `provenance` metadata field, not an independent chain-of-custody determination.

### F-AM-R1-S-003 (row-timestamp signal scope)

Confirmed resolved in current-status text. Reader note Section 4 says the row-level system timestamps supply "an available freshness signal (row-instantiation timing)" and explicitly says they are "not a full change log with prior values or edit authorship."

## Status-propagation check

Reader note header and reader note Section 8 are mutually consistent on current version (`v0.2`), consecutive qualifying-PASS count (`ONE` / one), and round count (one prior qualifying round, F-AM-R1).

Companion **Current State** is also consistent on those same current-status fields.

However, the companion **header** is not fully consistent: line 3 says the companion is to the reader-facing note, `v0.1`, while the surrounding current-status header text at line 5 says it mirrors note state `v0.2`, and the authoritative Current State block is explicitly `v0.2`. I treat that stale `v0.1` header label as a current-status propagation defect.

## Findings (artifact-level)

1. **Identifier:** F-AM-R2-001
   **Severity:** MEDIUM
   **Locus:** `Bayyinah_ProvenanceIntegrity_v0.2.md` §5.4 line 63; §7 line 71; cross-check against §Abstract line 17, §3 line 37, §5.2 line 55, and `reproduce_paper3.py` lines 135-149.
   **Substance (surface vs substrate):** Surface says the R1-S-001 regression was absorbed and that the note now claims only the batch-after-close fact, but substrate text still states that Tier 2 emits a "republish inference" and that the method "reports as a republish," which exceeds what a single-pull uniform `:created_at` establishes.
   **Disposition:** Unresolved regression. Replace the republish-specific wording in §§5.4 and 7 with the same batch-after-close / first-time-bulk-load ambiguity used in the Abstract, §3, §5.2, and the reproduction tool.
   **Cross-reference:** Regression check F-AM-R1-S-001; steps 1, 3, 4, 5.

2. **Identifier:** F-AM-R2-002
   **Severity:** LOW
   **Locus:** `Bayyinah_ProvenanceIntegrity_Companion_v0.2.md` header line 3 versus header line 5 and Current State lines 9-13; cross-check against `Bayyinah_ProvenanceIntegrity_v0.2.md` header line 7 and §8 line 75.
   **Substance (surface vs substrate):** Surface current-status propagation is supposed to be uniform at `v0.2` with one prior qualifying round, but the companion header still labels the reader-facing note as `v0.1`, contradicting the surrounding current-status text and authoritative Current State block.
   **Disposition:** Stale header metadata. Update the companion header to reference the `v0.2` reader note so all current-status loci are consistent.
   **Cross-reference:** Status-propagation check.

## Severity count

- CRITICAL: 0
- HIGH: 0
- MEDIUM: 1
- LOW: 1
- INFO: 0

## Artifact reproduction result on the merits

On the merits of the package and public endpoints, I reproduced the expected hash, provenance classifications, schema counts, FY2022/FY2023/FY2024 divergence figures, freshness lags, 404 revisions endpoint, system-column queryability, self-test behavior, live no-drift result, and adversarial mutate-and-rehash DRIFT behavior.

## Verdict

**INCOMPLETE** for this audit instance.

Reason: although all six reproduction steps were executed successfully and artifact-level findings remained below HIGH, I cannot truthfully provide the required isolation attestation because I accidentally touched other round directories during the session. Under the brief's binding operating conditions, I therefore do not return PASS.

## Attestation

Requested attestation text: "Fresh, memoryless instance; did not access any other member's work; worked only from my own directory copy."

I can attest only this narrower statement truthfully: I was a fresh, memoryless instance at launch, and I performed the substantive reproduction work in `/home/user/workspace/audit_r2/gpt_5_4/`; however, I cannot attest the full requested sentence because I accidentally touched other round directories during one later workspace-wide grep.

---

# Bismillah ir-Rahman ir-Rahim
