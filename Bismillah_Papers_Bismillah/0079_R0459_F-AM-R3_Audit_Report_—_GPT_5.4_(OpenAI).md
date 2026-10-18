# Bismillah ir-Rahman ir-Rahim

# R0459 -- F-AM-R3 Audit Report — GPT 5.4 (OpenAI)

**Chronological Index:** 79 of 995  
**Date:** 2024-12-31  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-AM-R3_gpt54.md  
**Source Format:** md  
**SHA-256:** `1ee7c06652f4599e51a39ca2e9a151b225d90ce11a28a0c169eca3777fb0942c`  

---

## R0459 · F-AM-R3 Audit Report — GPT 5.4 (OpenAI)

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-AM-R3_gpt54.md
- source_format: md
- text_sha256: 1ee7c06652f4599e51a39ca2e9a151b225d90ce11a28a0c169eca3777fb0942c

# F-AM-R3 Audit Report — GPT 5.4 (OpenAI)

## 1. Member identity, lineage, new-relative-to-R1/R2 flag, role

- Member: GPT 5.4
- Model lineage: OpenAI
- New relative to the R1/R2 clean qualifying pair (GPT 5.5, Gemini 3.1 Pro): YES
- Role: QUALIFYING (non-producer lineage; rotated-in member for this confirming round)

## 2. Isolation attestation + no-prior-state attestation + command log summary

> I attest that I operated only within /home/user/workspace/R3-gpt54, did not list, read, search, or traverse any sibling, orchestrator, or workspace-root directory, and did not access another member's work.

> I have no prior chat memory, saved state, personalization, or access to any prior round's report or another member's work; I executed this audit independently from this packet alone.

Command log summary:

```text
Command/file-operation root log for F-AM-R3 audit

1. /home/user/workspace/R3-gpt54 (all reads, writes, listings, searches, unzip, and script execution)
2. https://data.ny.gov (outbound HTTPS only for live metadata and SODA queries)
```

## 3. Execution status for each of the six steps

### Step 1 — `python3 repro/reproduce_paper3.py`

Status: COMPLETED
Exit code: 0
Hash confirmation required by the protocol: `c49488723819d272beb6445435c724dfbf2050a363baf89d09a333a993e18201` reproduced.

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
```

### Step 2 — `python3 repro/reproduce_paper3.py --selftest`

Status: COMPLETED
Exit code: 0

```text
[selftest] perturbing each captured value to confirm the comparator detects it...
[selftest] perturbed 42 captured values; comparator missed 0
```

### Step 3 — `python3 repro/reproduce_paper3.py --live`

Status: COMPLETED
Exit code: 0

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
```

### Step 4 — Independent recompute with fresh urllib code

Status: COMPLETED
Exit code: 0

Independent code used:

```python
#!/usr/bin/env python3
import json
import urllib.parse
import urllib.request
from datetime import date

PORTAL = "data.ny.gov"
SLUGS = {
    "gpsc-qqsz": "community_view",
    "twsw-2mqa": "official_dataset",
}
FYS = ["2022", "2023", "2024"]


def get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "gpt54-r3-independent-recompute"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.status, json.loads(resp.read().decode("utf-8"))


def soda_query(slug, select_sql, where_sql=None):
    params = {"$select": select_sql}
    if where_sql:
        params["$where"] = where_sql
    query = urllib.parse.urlencode(params, safe=":$,()='")
    url = f"https://{PORTAL}/resource/{slug}.json?{query}"
    status, payload = get_json(url)
    return status, url, payload


def days_after_close(ts, fy_close):
    return (date.fromisoformat(ts[:10]) - date.fromisoformat(fy_close)).days


def main():
    live = {}
    for slug in SLUGS:
        meta_url = f"https://{PORTAL}/api/views/{slug}.json"
        meta_status, meta = get_json(meta_url)
        fields = sorted(c["fieldName"] for c in meta.get("columns", []) if c.get("fieldName"))
        live[slug] = {
            "meta_url": meta_url,
            "meta_status": meta_status,
            "name": meta.get("name"),
            "provenance": meta.get("provenance"),
            "rowsUpdatedAt": meta.get("rowsUpdatedAt"),
            "fields": fields,
            "windows": {},
        }
        for fy in FYS:
            select_sql = (
                "count(*) as row_count, "
                "sum(contract_amount) as face_total, "
                "min(:created_at) as created_at_min, "
                "max(:created_at) as created_at_max, "
                "min(:updated_at) as updated_at_min, "
                "max(:updated_at) as updated_at_max"
            )
            where_sql = f"fiscal_year_end_date='{fy}-12-31T00:00:00.000'"
            status, url, payload = soda_query(slug, select_sql, where_sql)
            row = payload[0]
            live[slug]["windows"][fy] = {
                "status": status,
                "url": url,
                "row_count": int(row["row_count"]),
                "face_total": round(float(row["face_total"]), 2),
                "created_at_min": row["created_at_min"],
                "created_at_max": row["created_at_max"],
                "updated_at_min": row["updated_at_min"],
                "updated_at_max": row["updated_at_max"],
            }

    print("# Independent recompute using fresh urllib code")
    for slug, data in live.items():
        print(f"METADATA {slug} status={data['meta_status']} provenance={data['provenance']} name={data['name']}")
        print(f"SCHEMA {slug} field_count={len(data['fields'])}")
        print("FIELDS", slug, json.dumps(data["fields"], ensure_ascii=False))
        for fy in FYS:
            row = data["windows"][fy]
            fy_close = f"{fy}-12-31"
            lag = days_after_close(row["created_at_min"], fy_close)
            uniform_created = row["created_at_min"] == row["created_at_max"]
            uniform_updated = row["updated_at_min"] == row["updated_at_max"]
            print(
                f"WINDOW {slug} FY{fy} row_count={row['row_count']} face_total={row['face_total']:.2f} "
                f"created_min={row['created_at_min']} created_max={row['created_at_max']} "
                f"updated_min={row['updated_at_min']} updated_max={row['updated_at_max']} "
                f"created_days_after_close={lag} uniform_created={uniform_created} uniform_updated={uniform_updated}"
            )

    gpsc = live["gpsc-qqsz"]
    twsw = live["twsw-2mqa"]
    print("# Cross-dataset divergence summary")
    for fy in FYS:
        g = gpsc["windows"][fy]
        t = twsw["windows"][fy]
        row_diff = g["row_count"] - t["row_count"]
        face_diff = round(g["face_total"] - t["face_total"], 2)
        print(
            f"DIVERGENCE FY{fy} row_diff={row_diff} face_diff={face_diff:.2f} "
            f"gpsc_row_count={g['row_count']} twsw_row_count={t['row_count']} "
            f"gpsc_face_total={g['face_total']:.2f} twsw_face_total={t['face_total']:.2f}"
        )

    only_official = sorted(set(twsw["fields"]) - set(gpsc["fields"]))
    only_community = sorted(set(gpsc["fields"]) - set(twsw["fields"]))
    print(f"SCHEMA_DIFF official_only_count={len(only_official)} community_only_count={len(only_community)}")
    print("OFFICIAL_ONLY_FIELDS", json.dumps(only_official, ensure_ascii=False))
    print("COMMUNITY_ONLY_FIELDS", json.dumps(only_community, ensure_ascii=False))


if __name__ == "__main__":
    main()
```

Real output:

```text
# Independent recompute using fresh urllib code
METADATA gpsc-qqsz status=200 provenance=community name=MTA Procurement Report (All)
SCHEMA gpsc-qqsz field_count=23
FIELDS gpsc-qqsz ["amount_expended_for_fiscal_year", "amount_expended_to_date", "authority_name", "award_date", "award_process", "begin_date", "contract_amount", "current_or_outstanding_balance", "end_date", "fiscal_year_end_date", "number_of_bids_or_proposals_received", "number_of_mwbe_proposals", "procurement_description", "procurements", "solicited_mwbe", "type_of_procurement", "vendor_city", "vendor_country", "vendor_is_a_mwbe", "vendor_name", "vendor_postal_code", "vendor_province_region", "vendor_state"]
WINDOW gpsc-qqsz FY2022 row_count=12156 face_total=54698007774.69 created_min=2025-12-01T17:15:55.609Z created_max=2025-12-01T17:15:55.609Z updated_min=2025-12-01T17:15:55.609Z updated_max=2025-12-01T17:15:55.609Z created_days_after_close=1066 uniform_created=True uniform_updated=True
WINDOW gpsc-qqsz FY2023 row_count=12114 face_total=63569204049.36 created_min=2025-12-01T17:15:55.609Z created_max=2025-12-01T17:15:55.609Z updated_min=2025-12-01T17:15:55.609Z updated_max=2025-12-01T17:15:55.609Z created_days_after_close=701 uniform_created=True uniform_updated=True
WINDOW gpsc-qqsz FY2024 row_count=13718 face_total=65189755228.64 created_min=2025-12-01T17:15:55.609Z created_max=2025-12-01T17:15:55.609Z updated_min=2025-12-01T17:15:55.609Z updated_max=2025-12-01T17:15:55.609Z created_days_after_close=335 uniform_created=True uniform_updated=True
METADATA twsw-2mqa status=200 provenance=official name=MTA Procurements: Beginning 2018
SCHEMA twsw-2mqa field_count=32
FIELDS twsw-2mqa ["address_line_1", "address_line_2", "amount_expended_for_fiscal_year", "amount_expended_to_date", "award_date", "award_process", "basis_for_exemption", "begin_date", "city", "contract_amount", "country", "current_or_outstanding_balance", "end_date", "exempt_from_article_4c", "fair_market_value", "fair_market_value_explanation", "fiscal_year_end_date", "number_of_bids_or_proposals_received", "number_of_mwbe_proposals", "postal_code", "procurement_description", "region", "renewal_date", "solicited_mwbe", "state", "status", "transaction_number", "type_of_procurement", "vendor_is_a_mwbe", "vendor_is_nys_or_fbe", "vendor_name", "zip_code_plus_4"]
WINDOW twsw-2mqa FY2022 row_count=12156 face_total=54698007775.44 created_min=2026-04-01T14:09:46.913Z created_max=2026-04-01T14:09:46.913Z updated_min=2026-04-01T14:09:46.913Z updated_max=2026-04-01T14:09:46.913Z created_days_after_close=1187 uniform_created=True uniform_updated=True
WINDOW twsw-2mqa FY2023 row_count=12114 face_total=63569204049.36 created_min=2026-04-01T14:09:46.913Z created_max=2026-04-01T14:09:46.913Z updated_min=2026-04-01T14:09:46.913Z updated_max=2026-04-01T14:09:46.913Z created_days_after_close=822 uniform_created=True uniform_updated=True
WINDOW twsw-2mqa FY2024 row_count=13648 face_total=65131682801.41 created_min=2026-04-01T14:09:46.913Z created_max=2026-04-01T14:09:46.913Z updated_min=2026-04-01T14:09:46.913Z updated_max=2026-04-01T14:09:46.913Z created_days_after_close=456 uniform_created=True uniform_updated=True
# Cross-dataset divergence summary
DIVERGENCE FY2022 row_diff=0 face_diff=-0.75 gpsc_row_count=12156 twsw_row_count=12156 gpsc_face_total=54698007774.69 twsw_face_total=54698007775.44
DIVERGENCE FY2023 row_diff=0 face_diff=0.00 gpsc_row_count=12114 twsw_row_count=12114 gpsc_face_total=63569204049.36 twsw_face_total=63569204049.36
DIVERGENCE FY2024 row_diff=70 face_diff=58072427.23 gpsc_row_count=13718 twsw_row_count=13648 gpsc_face_total=65189755228.64 twsw_face_total=65131682801.41
SCHEMA_DIFF official_only_count=16 community_only_count=7
OFFICIAL_ONLY_FIELDS ["address_line_1", "address_line_2", "basis_for_exemption", "city", "country", "exempt_from_article_4c", "fair_market_value", "fair_market_value_explanation", "postal_code", "region", "renewal_date", "state", "status", "transaction_number", "vendor_is_nys_or_fbe", "zip_code_plus_4"]
COMMUNITY_ONLY_FIELDS ["authority_name", "procurements", "vendor_city", "vendor_country", "vendor_postal_code", "vendor_province_region", "vendor_state"]
```

### Step 5 — Independent data-interface confirmation (`revisions.json` HTTP codes; system columns queryable)

Status: COMPLETED
Exit code: 0

```text
# Revisions endpoint checks
REVISIONS slug=gpsc-qqsz status=404 body_prefix='{\n  "code" : "not_found",\n  "error" : true,\n  "message" : "No service found for this URL."\n}\n'
REVISIONS slug=twsw-2mqa status=404 body_prefix='{\n  "code" : "not_found",\n  "error" : true,\n  "message" : "No service found for this URL."\n}\n'
# System column query checks
SYSTEM_COLUMNS slug=gpsc-qqsz status=200 payload=[{"row_count": "13718", "created_min": "2025-12-01T17:15:55.609Z", "updated_max": "2025-12-01T17:15:55.609Z"}]
SYSTEM_COLUMNS slug=twsw-2mqa status=200 payload=[{"row_count": "13648", "created_min": "2026-04-01T14:09:46.913Z", "updated_max": "2026-04-01T14:09:46.913Z"}]
```

### Step 6 — Adversarial mutate, re-hash, and comparator DRIFT check

Status: COMPLETED
Exit code: 2 (expected nonzero DRIFT result)

```text
# Adversarial mutate-and-rehash
MUTATED_PATH=datasets/gpsc-qqsz/fiscal_windows/2024-12-31/row_count
OLD_VALUE=13718
NEW_VALUE=13719
REHASHED_MANIFEST_SHA256=e21187546b35bd4fcdb37aadb99bbf7a05004bc0ee4792a6645abd0050406af9
INTEGRITY_PASSES=True
COMPARATOR=DRIFT count=1
DRIFT gpsc-qqsz/2024-12-31/row_count original=13718 tampered=13719
```

## 4. Audit-scope confirmations/disputes

### 4.1 Tier discipline

Confirmed. The reader note explicitly sorts claims into Tier 1 / Tier 2 / Tier 3 and states the refusal boundary: line 35 says Tier 1 covers "the SHA-256 of a frozen capture; a dataset's row count and served field inventory; whether two datasets are byte-identical over a shared window; and the row-level Socrata system timestamps `:created_at` and `:updated_at`"; line 37 says Tier 2 covers the portal-metadata provenance classification, freshness reconciliation, and "whether the served history is preserved-since-origin or was instantiated in a single post-close batch"; line 39 says "Tier 3 is interpretive and is refused". Section 5.4 line 63 is consistent: "At Tier 1 it emits the hashes, counts, exact divergences, and row timestamps. At Tier 2 it emits the provenance classifications, the freshness reconciliation, and the post-close-batch inference ... At Tier 3 it refuses ..."

### 4.2 Refusal boundary

Confirmed. I searched the whole reader note for refusal-boundary terms and found the current operative language at lines 17, 23, 39, and 63, each refusing legitimacy judgments rather than making them. The key loci are:

- Line 17: "The method detects and quantifies these divergences and refuses to judge whether any was legitimate, authorized, or improper."
- Line 23: "It does not adjudicate whether an observed divergence or republish was a correction, a migration, an error, or a manipulation."
- Line 39: "Tier 3 is interpretive and is refused: whether a change was legitimate, authorized, malicious, or intended to deceive ..."
- Line 63: "At Tier 3 it refuses: it does not conclude that the community view is unauthorized, that any batch load was improper, that the FY2024 divergence is an error in either dataset, or that any party intended to mislead."

The execution outputs are aligned with that boundary: Step 1 and Step 3 print "This tool does not judge whether any was legitimate, authorized, or improper (Tier 3, refused)." No surviving locus in the current reader note asserts or implies that a divergence, batch load, or edit was illegitimate, unauthorized, improper, or deceptive.

### 4.3 Three-resolution divergence, including the FY2022 $0.75 at identical row count

Confirmed with executed evidence. The independent recompute reproduced:

- FY2022: `row_diff=0`, `face_diff=-0.75`, with `gpsc_row_count=12156`, `twsw_row_count=12156`, `gpsc_face_total=54698007774.69`, `twsw_face_total=54698007775.44`
- FY2023: `row_diff=0`, `face_diff=0.00`, with both row counts `12114` and both totals `63569204049.36`
- FY2024: `row_diff=70`, `face_diff=58072427.23`, with `gpsc_row_count=13718`, `twsw_row_count=13648`, `gpsc_face_total=65189755228.64`, `twsw_face_total=65131682801.41`

These outputs match reader note Section 5.1 line 51.

### 4.4 Freshness lags

Confirmed with executed evidence. The independent recompute reproduced uniform timestamps and lags of 1066 / 701 / 335 days after close for `gpsc-qqsz` and 1187 / 822 / 456 days after close for `twsw-2mqa`. The reader note states the same at Section 5.2 line 55.

### 4.5 Schema counts

Confirmed with executed evidence. The independent recompute reproduced `gpsc-qqsz` `field_count=23`, `twsw-2mqa` `field_count=32`, `official_only_count=16`, `community_only_count=7`. This matches reader note Section 5.3 line 59.

### 4.6 Data-interface facts

Confirmed with executed evidence. Step 5 independently reproduced `REVISIONS slug=gpsc-qqsz status=404` and `REVISIONS slug=twsw-2mqa status=404`, and successfully queried `:created_at` / `:updated_at` system columns for both datasets with HTTP 200 payloads. This matches reader note Section 4 line 43 and brief line 34.

## 5. Regression confirmations (F-AM-R2-001 / 002 / 003) with quoted loci

### F-AM-R2-001 — recurring republish over-claim

Resolved cleanly in the specified loci.

- Reader Section 5.4, line 63 now reads: "At Tier 2 it emits the provenance classifications, the freshness reconciliation, and the post-close-batch inference (a batch load after the period close, which a single pull does not resolve into a republish versus a first-time bulk load)."
- Reader Section 6, line 67 now reads: "the provenance, schema, snapshot-hash, and post-close-batch checks need no period field"
- Reader Section 7, line 71 now reads: "the method reports as a post-close batch load (a republish or a first-time bulk load, which a single pull cannot distinguish)"

These loci are consistent with the already-correct framing elsewhere:

- Abstract line 17: "in a single post-close batch (consistent with a wholesale republish and equally with a first-time bulk load, which a single-pull timestamp cannot distinguish)"
- Section 3 line 37: "a batch that a single pull cannot resolve into a republish versus a first-time bulk load"
- Section 5.2 line 55: "consistent with a wholesale republish of previously-served history and equally consistent with a first-time bulk load ... the note claims only the batch-after-close fact"
- Tool output in Steps 1 and 3: `POST-CLOSE-BATCH` with the note "a single pull does not distinguish a republish from a first-time bulk load."

Whole-note search result: `republish` still appears in generic or historical-reference contexts (for example line 29 "A portal can republish ...", line 75 "residual republish wording ..."), but I found no surviving bare assertion that the observed MTA batch event was a republish as fact.

### F-AM-R2-002 — stale companion header versioning

Resolved. The current companion header loci are internally consistent and read v0.3:

- Line 3: "Companion to: *Bayyinah al-Amāna: Provenance Integrity for Public Open Data* (the reader-facing note, v0.3)."
- Line 5: "Mirrors note state v0.3 ..."

I found no stale `v0.1` or `v0.2` in any current-status locus.

### F-AM-R2-003 — stale "Audit rounds" placeholder

Resolved. The current "Audit rounds" section no longer presents "None yet" as current status. Line 40 now reads:

"Appended below as dated append-only appendices: F-AM-R1 (v0.1 -> v0.2) and F-AM-R2 (v0.2 -> v0.3). [Superseded per Section 14.5: the original 'None yet' placeholder is retained here in spirit only; the round appendices follow.]"

That is a current pointer to the appended F-AM-R1 and F-AM-R2 appendices, with the placeholder explicitly marked superseded rather than current.

## 6. Status-propagation check result

Current-status loci read consistently on version, counter, and round count.

### Reader note loci

- Header line 7: "Working draft v0.3 (two qualifying cross-instance audit passes, F-AM-R1 and F-AM-R2: the consecutive qualifying-PASS count is TWO ... )"
- Section 8 line 75: "This is a v0.3 draft ... Two such passes have occurred (F-AM-R1 and F-AM-R2 ...), so the consecutive qualifying-PASS count is two ..."

### Companion header loci

- Line 3: "... the reader-facing note, v0.3."
- Line 5: "Mirrors note state v0.3 (two qualifying cross-instance audit passes, F-AM-R1 and F-AM-R2; the consecutive qualifying-PASS count is TWO ... )"

### Companion Current State loci

- Header line 9: "## Current State (authoritative, as of v0.3)"
- Artifact-state line 11: "Artifact state: v0.3 reader note plus this companion and the reproduction package ..."
- Counter line 12: "Consecutive qualifying-PASS count (single operational counter): TWO. Two qualifying rounds have occurred (F-AM-R1 and F-AM-R2 ... )"
- Round-history line 13: "Independent audit history: two rounds. F-AM-R1 ... F-AM-R2 ..."

Result: no current-status inconsistency found. Version is uniformly v0.3, the current counter is uniformly TWO/two, and the current round count is uniformly two (F-AM-R1 and F-AM-R2). Appendix references to earlier states remain correct in context and do not conflict with current status.

## 7. Findings

No findings.

## 8. Verdict

PASS.

Reason: I completed documented executed reproduction for all six required steps, including live `data.ny.gov` queries and an independent recompute with fresh code; I found zero CRITICAL and zero HIGH findings, and I can truthfully provide the required isolation attestation.

---

# Bismillah ir-Rahman ir-Rahim
