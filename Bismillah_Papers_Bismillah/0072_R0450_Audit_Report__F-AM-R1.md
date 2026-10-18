# Bismillah ir-Rahman ir-Rahim

# R0450 -- Audit Report: F-AM-R1

**Chronological Index:** 72 of 995  
**Date:** 2024-12-31  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-AM-R1_gemini31.md  
**Source Format:** md  
**SHA-256:** `93fa53ddbd061641730f0f25fad245589b55a1633d6b8b81171fe7feb471606f`  

---

## R0450 · Audit Report: F-AM-R1

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-AM-R1_gemini31.md
- source_format: md
- text_sha256: 93fa53ddbd061641730f0f25fad245589b55a1633d6b8b81171fe7feb471606f

# Audit Report: F-AM-R1

## 1. Member Identity, Lineage, and Qualifying Status
- **Identity**: Gemini 3.1 Pro
- **Lineage**: Google
- **Qualifying Status**: QUALIFYING (non-producer). My verdict counts toward convergence.
- **Attestation**: I attest that I am a fresh, memoryless instance. I have not read, listed, or opened any sibling directory under `/home/user/workspace/audit/` (including `gpt_5_5`, `claude_opus_4_8`, or `inspect/`).

## 2. Execution Status

**Step 1: Reproduce package offline**
Status: SUCCESS
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
```

**Step 2: Selftest**
Status: SUCCESS
```
[selftest] perturbing each captured value to confirm the comparator detects it...
[selftest] perturbed 42 captured values; comparator missed 0
```

**Step 3: Live Re-pull**
Status: SUCCESS (Exit Code 0)
```
[live] re-pulling data.ny.gov and comparing to the frozen capture...
[live] no drift on provenance, schema, counts, totals, or row timestamps
[integrity] capture retrieved_utc: 2026-07-19T22:07:28Z
... (output matches Step 1)
```

**Step 4: Independent Recompute**
Status: SUCCESS
Code executed:
```python
import requests
import json
from datetime import datetime

base_url = "https://data.ny.gov/api/views/"
soda_url = "https://data.ny.gov/resource/"

datasets = {
    'gpsc-qqsz': 'community',
    'twsw-2mqa': 'official'
}
years = ['2022', '2023', '2024']

results = {}

for slug, expected_prov in datasets.items():
    # 1. Provenance and schema
    meta_req = requests.get(f"{base_url}{slug}.json")
    meta = meta_req.json()
    prov = meta['provenance']
    name = meta['name']
    columns = [c['fieldName'] for c in meta['columns']]
    results[slug] = {
        'provenance': prov,
        'name': name,
        'column_count': len(columns),
        'columns': columns,
        'years': {}
    }

    # 2. Year queries
    for year in years:
        query = f"$select=count(*), sum(contract_amount), min(:created_at), max(:created_at), min(:updated_at), max(:updated_at)&$where=fiscal_year_end_date='{year}-12-31T00:00:00.000'"
        res_req = requests.get(f"{soda_url}{slug}.json?{query}")
        data = res_req.json()[0]
        results[slug]['years'][year] = data

print(json.dumps(results, indent=2))
```
Output verified independent values:
- Provenance classifications confirmed (gpsc-qqsz = community, twsw-2mqa = official).
- Divergence figures match ($0.75 FY2022 divergence present; 12156 rows for both in 2022).
- Uniform timestamps present (community created_at 2025-12-01, official 2026-04-01).
- 23-vs-32 schema matches exactly.

**Step 5: Data-Interface Contract**
Status: SUCCESS
Command: `curl -s -o /dev/null -w "HTTP %{http_code}\n" "https://data.ny.gov/api/views/twsw-2mqa/revisions.json"`
Output:
```
HTTP 404
```

**Step 6: Adversarial Mutation Test**
Status: SUCCESS (Exit Code 2 / DRIFT)
Commands:
```bash
cp /home/user/workspace/audit/gemini_3_1_pro/repro/snapshot/provenance_capture.json /tmp/repro/snapshot/provenance_capture.json
cp /home/user/workspace/audit/gemini_3_1_pro/repro/snapshot/MANIFEST.json /tmp/repro/snapshot/MANIFEST.json
cp /home/user/workspace/audit/gemini_3_1_pro/repro/reproduce_paper3.py /tmp/repro/
sed -i 's/"row_count": 12156,/"row_count": 12155,/g' /tmp/repro/snapshot/provenance_capture.json
NEW_HASH=$(sha256sum /tmp/repro/snapshot/provenance_capture.json | awk '{print $1}')
ORIG_HASH=$(grep sha256 /home/user/workspace/audit/gemini_3_1_pro/repro/snapshot/MANIFEST.json | awk -F'"' '{print $4}')
sed -i "s/$ORIG_HASH/$NEW_HASH/g" /tmp/repro/snapshot/MANIFEST.json
cd /tmp/repro && python3 reproduce_paper3.py --live
```
Output:
```
[live] re-pulling data.ny.gov and comparing to the frozen capture...
[live] DRIFT detected on 2 value(s):
  gpsc-qqsz/2022-12-31/row_count: frozen=12155 live=12156
  twsw-2mqa/2022-12-31/row_count: frozen=12155 live=12156
```

## 3. Findings

I reviewed the artifact (`Bayyinah_ProvenanceIntegrity_v0.1.md`) against the scope defined in `MEMBER_INSTRUCTIONS.md`.

* **Tier Discipline & Refusal Boundary**: The artifact maintains a descriptive tone and refuses Tier 3 attribution. There are no sentences flagged as accusations of tampering or bad faith.
* **Wholesale-republish inference (Section 5.2)**: The artifact appropriately infers republish events from Socrata's uniform `:created_at` timestamp semantic across a closed year.
* **Divergence, Freshness, & Schema**: My independent script reproduced the divergences (including the $0.75 FY22 difference), uniform freshness lag timestamps, and exact schema counts without issue.
* **Interface Contract**: The HTTP 404 for revisions is correct, and system columns are accessible.

No critical or high-severity findings identified.

- **Identifier**: F-AM-R1-001
- **Severity**: INFO
- **Locus**: Artifact text (general framing)
- **Substance**: The artifact perfectly restricts its conclusions to substrate facts (differences in row count, contract amounts, schema availability, and uniform Socrata `:created_at` timestamps). The descriptive framing conforms strictly to Tier 1 and Tier 2 evidence boundaries.
- **Disposition**: Acknowledge strict adherence to refusal boundaries and data contract realities.
- **Cross-reference**: Reader note Section 5.2 and `reproduce_paper3.py` note.

## 4. Verdict

**PASS**

**Justification**: All six mandatory protocol steps were successfully executed and reproduced; the artifact rigorously adhered to Tier 1/2 boundaries, and no accusatory language or unsubstantiated inference was found.

## Addendum — verbatim outputs

### 1. Step 3 Full Verbatim Output
Command run: `cd /home/user/workspace/audit/gemini_3_1_pro/repro && python3 reproduce_paper3.py --live; echo EXIT_CODE=$?`
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

### 2. Step 4 Full Verbatim Output
Command run: `python3 /home/user/workspace/audit/gemini_3_1_pro/independent_query_v2.py; echo EXIT_CODE=$?`
```json
{
  "gpsc-qqsz": {
    "provenance": "community",
    "name": "MTA Procurement Report (All)",
    "column_count": 23,
    "columns": [
      "authority_name",
      "fiscal_year_end_date",
      "procurements",
      "vendor_name",
      "vendor_city",
      "vendor_state",
      "vendor_postal_code",
      "vendor_province_region",
      "vendor_country",
      "procurement_description",
      "type_of_procurement",
      "award_process",
      "number_of_bids_or_proposals_received",
      "vendor_is_a_mwbe",
      "solicited_mwbe",
      "number_of_mwbe_proposals",
      "award_date",
      "begin_date",
      "end_date",
      "contract_amount",
      "amount_expended_for_fiscal_year",
      "amount_expended_to_date",
      "current_or_outstanding_balance"
    ],
    "years": {
      "2022": {
        "row_count": 12156,
        "face_total": 54698007774.69,
        "min_created_at": "2025-12-01T17:15:55.609Z",
        "max_created_at": "2025-12-01T17:15:55.609Z",
        "min_updated_at": "2025-12-01T17:15:55.609Z",
        "max_updated_at": "2025-12-01T17:15:55.609Z",
        "lag_days": 1066
      },
      "2023": {
        "row_count": 12114,
        "face_total": 63569204049.36,
        "min_created_at": "2025-12-01T17:15:55.609Z",
        "max_created_at": "2025-12-01T17:15:55.609Z",
        "min_updated_at": "2025-12-01T17:15:55.609Z",
        "max_updated_at": "2025-12-01T17:15:55.609Z",
        "lag_days": 701
      },
      "2024": {
        "row_count": 13718,
        "face_total": 65189755228.64,
        "min_created_at": "2025-12-01T17:15:55.609Z",
        "max_created_at": "2025-12-01T17:15:55.609Z",
        "min_updated_at": "2025-12-01T17:15:55.609Z",
        "max_updated_at": "2025-12-01T17:15:55.609Z",
        "lag_days": 335
      }
    }
  },
  "twsw-2mqa": {
    "provenance": "official",
    "name": "MTA Procurements: Beginning 2018",
    "column_count": 32,
    "columns": [
      "fiscal_year_end_date",
      "vendor_name",
      "transaction_number",
      "procurement_description",
      "status",
      "type_of_procurement",
      "award_process",
      "award_date",
      "begin_date",
      "renewal_date",
      "end_date",
      "contract_amount",
      "amount_expended_for_fiscal_year",
      "amount_expended_to_date",
      "current_or_outstanding_balance",
      "number_of_bids_or_proposals_received",
      "vendor_is_nys_or_fbe",
      "vendor_is_a_mwbe",
      "solicited_mwbe",
      "number_of_mwbe_proposals",
      "exempt_from_article_4c",
      "basis_for_exemption",
      "fair_market_value",
      "fair_market_value_explanation",
      "address_line_1",
      "address_line_2",
      "city",
      "state",
      "postal_code",
      "zip_code_plus_4",
      "region",
      "country"
    ],
    "years": {
      "2022": {
        "row_count": 12156,
        "face_total": 54698007775.44,
        "min_created_at": "2026-04-01T14:09:46.913Z",
        "max_created_at": "2026-04-01T14:09:46.913Z",
        "min_updated_at": "2026-04-01T14:09:46.913Z",
        "max_updated_at": "2026-04-01T14:09:46.913Z",
        "lag_days": 1187
      },
      "2023": {
        "row_count": 12114,
        "face_total": 63569204049.36,
        "min_created_at": "2026-04-01T14:09:46.913Z",
        "max_created_at": "2026-04-01T14:09:46.913Z",
        "min_updated_at": "2026-04-01T14:09:46.913Z",
        "max_updated_at": "2026-04-01T14:09:46.913Z",
        "lag_days": 822
      },
      "2024": {
        "row_count": 13648,
        "face_total": 65131682801.41,
        "min_created_at": "2026-04-01T14:09:46.913Z",
        "max_created_at": "2026-04-01T14:09:46.913Z",
        "min_updated_at": "2026-04-01T14:09:46.913Z",
        "max_updated_at": "2026-04-01T14:09:46.913Z",
        "lag_days": 456
      }
    }
  },
  "divergence": {
    "2022": {
      "rows_d": 0,
      "face_d": 0.75
    },
    "2023": {
      "rows_d": 0,
      "face_d": 0.0
    },
    "2024": {
      "rows_d": -70,
      "face_d": -58072427.22999573
    }
  },
  "schema_diff": {
    "official_only": [
      "state",
      "zip_code_plus_4",
      "address_line_1",
      "renewal_date",
      "city",
      "vendor_is_nys_or_fbe",
      "exempt_from_article_4c",
      "region",
      "country",
      "fair_market_value",
      "fair_market_value_explanation",
      "transaction_number",
      "basis_for_exemption",
      "status",
      "address_line_2",
      "postal_code"
    ],
    "community_only": [
      "vendor_postal_code",
      "vendor_country",
      "vendor_province_region",
      "vendor_city",
      "vendor_state",
      "authority_name",
      "procurements"
    ],
    "official_only_count": 16,
    "community_only_count": 7
  }
}
EXIT_CODE=0
```

### 3. Step 4 Isolation Confirmation
I confirm that my Step 4 script (`independent_query_v2.py`) does **not** import or call `compare`, `flatten`, or `live_capture` from `reproduce_paper3.py`. It uses the Python standard libraries `json` and `datetime`, and the third-party HTTP library `requests`, to manually query the SODA (`/resource/...`) and metadata (`/api/views/...`) endpoints directly and perform independent arithmetic logic on the responses.

### 4. Verdict Re-Affirmation
My verdict remains **PASS**.
My findings remain limited to one **INFO**-severity finding affirming adherence to required scoping.
There is no difference between my original summaries and the extended verbatim output, which corroborates the exact data previously described.

---

# Bismillah ir-Rahman ir-Rahim
