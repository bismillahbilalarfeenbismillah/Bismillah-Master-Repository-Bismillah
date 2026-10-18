# Bismillah ir-Rahman ir-Rahim

# R0456 -- F-AM-R2 Audit Report — GPT 5.5 qualifying auditor

**Chronological Index:** 77 of 995  
**Date:** 2024-12-31  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-AM-R2_gpt55.md  
**Source Format:** md  
**SHA-256:** `3d719d3fcad4f139d0c9a4090f55155b1098828ea173f8791307eeb2a04327f8`  

---

## R0456 · F-AM-R2 Audit Report — GPT 5.5 qualifying auditor

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-AM-R2_gpt55.md
- source_format: md
- text_sha256: 3d719d3fcad4f139d0c9a4090f55155b1098828ea173f8791307eeb2a04327f8

# F-AM-R2 Audit Report — GPT 5.5 qualifying auditor

## Scope and attestation

Fresh, memoryless instance; did not access any other member's work; worked only from my own directory copy: `/home/user/workspace/audit_r2/gpt_5_5/`.

Member identity: GPT 5.5 (OpenAI), qualifying non-producer auditor for namespace F-AM-R2.

## Verdict

**PASS (individual qualifying member verdict).** I executed and documented all six required reproduction steps. I found **0 CRITICAL** and **0 HIGH** findings. Non-blocking findings: **1 MEDIUM, 2 LOW**.

I do not synthesize the full Model Council result because I worked only from my own directory and did not read any other member's work.

## Step 1 — Offline reproduction

```text
$ cd /home/user/workspace/audit_r2/gpt_5_5 && python3 reproduce_paper3.py
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

## Step 2 — Self-test

```text
$ cd /home/user/workspace/audit_r2/gpt_5_5 && python3 reproduce_paper3.py --selftest
[selftest] perturbing each captured value to confirm the comparator detects it...
[selftest] perturbed 42 captured values; comparator missed 0
EXIT_CODE=0
```

## Step 3 — Live reproduction

```text
$ cd /home/user/workspace/audit_r2/gpt_5_5 && python3 reproduce_paper3.py --live
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

## Step 4 — Independent recompute, with my own code

```text
$ cat independent_recompute_gpt_5_5.py
#!/usr/bin/env python3
import json
from decimal import Decimal, getcontext
from urllib.parse import urlencode, quote
from urllib.request import Request, urlopen
from datetime import date

getcontext().prec = 40
BASE = "https://data.ny.gov"
DATASETS = ["gpsc-qqsz", "twsw-2mqa"]
YEARS = [2022, 2023, 2024]


def get_json(url):
    req = Request(url, headers={"User-Agent": "F-AM-R2 independent recompute gpt_5_5"})
    with urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode("utf-8"))

print("INDEPENDENT RECOMPUTE (no import of reproduce_paper3.py)")
metadata = {}
for ds in DATASETS:
    url = f"{BASE}/api/views/{ds}.json"
    m = get_json(url)
    cols = [c for c in m.get("columns", []) if not c.get("flags") or "hidden" not in c.get("flags", [])]
    metadata[ds] = {
        "name": m.get("name"),
        "provenance": m.get("provenance"),
        "fields": [c.get("fieldName") for c in cols],
        "columns": cols,
    }
    print(f"METADATA {ds}: name={m.get('name')!r} provenance={m.get('provenance')!r} field_count={len(cols)}")
    print("  fields=" + ", ".join(metadata[ds]["fields"]))

official_only = sorted(set(metadata["twsw-2mqa"]["fields"]) - set(metadata["gpsc-qqsz"]["fields"]))
community_only = sorted(set(metadata["gpsc-qqsz"]["fields"]) - set(metadata["twsw-2mqa"]["fields"]))
print(f"SCHEMA_DIFF official_only_count={len(official_only)} community_only_count={len(community_only)}")
print("  official_only=" + ", ".join(official_only))
print("  community_only=" + ", ".join(community_only))

rows = {ds: {} for ds in DATASETS}
for ds in DATASETS:
    for y in YEARS:
        fy = f"{y}-12-31T00:00:00.000"
        select = "count(*) as row_count, sum(contract_amount) as face_total, min(`:created_at`) as min_created, max(`:created_at`) as max_created, min(`:updated_at`) as min_updated, max(`:updated_at`) as max_updated"
        params = {
            "$select": select,
            "$where": f"fiscal_year_end_date='{fy}'",
        }
        url = f"{BASE}/resource/{ds}.json?{urlencode(params)}"
        data = get_json(url)
        if len(data) != 1:
            raise SystemExit(f"unexpected rows for {ds} {y}: {data}")
        rec = data[0]
        count = int(rec["row_count"])
        total = Decimal(str(rec["face_total"] or "0"))
        rows[ds][y] = {"count": count, "total": total, **{k: rec.get(k) for k in ("min_created", "max_created", "min_updated", "max_updated")}}
        print(f"AGG {ds} FY{y}: count={count} sum={total:.2f} min_created={rec.get('min_created')} max_created={rec.get('max_created')} min_updated={rec.get('min_updated')} max_updated={rec.get('max_updated')}")

print("DIVERGENCE community(gpsc-qqsz) minus official(twsw-2mqa)")
for y in YEARS:
    g = rows["gpsc-qqsz"][y]
    t = rows["twsw-2mqa"][y]
    row_delta = g["count"] - t["count"]
    amt_delta = g["total"] - t["total"]
    row_pct_vs_gpsc = (Decimal(row_delta) / Decimal(g["count"]) * Decimal(100)) if g["count"] else Decimal(0)
    amt_pct_vs_gpsc = (amt_delta / g["total"] * Decimal(100)) if g["total"] else Decimal(0)
    row_pct_vs_twsw = (Decimal(row_delta) / Decimal(t["count"]) * Decimal(100)) if t["count"] else Decimal(0)
    amt_pct_vs_twsw = (amt_delta / t["total"] * Decimal(100)) if t["total"] else Decimal(0)
    print(f"FY{y}: gpsc_count={g['count']} twsw_count={t['count']} row_delta={row_delta:+d} row_pct_vs_gpsc={row_pct_vs_gpsc:.4f}% row_pct_vs_twsw={row_pct_vs_twsw:.4f}% gpsc_sum={g['total']:.2f} twsw_sum={t['total']:.2f} amount_delta={amt_delta:+.2f} amount_pct_vs_gpsc={amt_pct_vs_gpsc:.7f}% amount_pct_vs_twsw={amt_pct_vs_twsw:.7f}%")

print("FRESHNESS LAGS (created_at date minus fiscal close date; uniform = min_created == max_created)")
for ds in DATASETS:
    for y in YEARS:
        rec = rows[ds][y]
        created_date = rec["min_created"][:10]
        lag = (date.fromisoformat(created_date) - date(y, 12, 31)).days
        print(f"{ds} FY{y}: uniform_created={rec['min_created'] == rec['max_created']} created_date={created_date} lag_days={lag}")

print("CONFIRMATIONS")
print("  provenance classifications: gpsc-qqsz=community, twsw-2mqa=official ->", metadata["gpsc-qqsz"]["provenance"] == "community" and metadata["twsw-2mqa"]["provenance"] == "official")
print("  schema counts: gpsc-qqsz=23, twsw-2mqa=32, official_only=16, community_only=7 ->", len(metadata["gpsc-qqsz"]["fields"]) == 23 and len(metadata["twsw-2mqa"]["fields"]) == 32 and len(official_only) == 16 and len(community_only) == 7)
print("  FY2022 $0.75 divergence ->", rows["gpsc-qqsz"][2022]["total"] - rows["twsw-2mqa"][2022]["total"] == Decimal("-0.75"))
print("  all created_at timestamps uniform ->", all(rows[ds][y]["min_created"] == rows[ds][y]["max_created"] for ds in DATASETS for y in YEARS))
$ cd /home/user/workspace/audit_r2/gpt_5_5 && python3 independent_recompute_gpt_5_5.py
INDEPENDENT RECOMPUTE (no import of reproduce_paper3.py)
METADATA gpsc-qqsz: name='MTA Procurement Report (All)' provenance='community' field_count=23
  fields=authority_name, fiscal_year_end_date, procurements, vendor_name, vendor_city, vendor_state, vendor_postal_code, vendor_province_region, vendor_country, procurement_description, type_of_procurement, award_process, number_of_bids_or_proposals_received, vendor_is_a_mwbe, solicited_mwbe, number_of_mwbe_proposals, award_date, begin_date, end_date, contract_amount, amount_expended_for_fiscal_year, amount_expended_to_date, current_or_outstanding_balance
METADATA twsw-2mqa: name='MTA Procurements: Beginning 2018' provenance='official' field_count=32
  fields=fiscal_year_end_date, vendor_name, transaction_number, procurement_description, status, type_of_procurement, award_process, award_date, begin_date, renewal_date, end_date, contract_amount, amount_expended_for_fiscal_year, amount_expended_to_date, current_or_outstanding_balance, number_of_bids_or_proposals_received, vendor_is_nys_or_fbe, vendor_is_a_mwbe, solicited_mwbe, number_of_mwbe_proposals, exempt_from_article_4c, basis_for_exemption, fair_market_value, fair_market_value_explanation, address_line_1, address_line_2, city, state, postal_code, zip_code_plus_4, region, country
SCHEMA_DIFF official_only_count=16 community_only_count=7
  official_only=address_line_1, address_line_2, basis_for_exemption, city, country, exempt_from_article_4c, fair_market_value, fair_market_value_explanation, postal_code, region, renewal_date, state, status, transaction_number, vendor_is_nys_or_fbe, zip_code_plus_4
  community_only=authority_name, procurements, vendor_city, vendor_country, vendor_postal_code, vendor_province_region, vendor_state
AGG gpsc-qqsz FY2022: count=12156 sum=54698007774.69 min_created=2025-12-01T17:15:55.609Z max_created=2025-12-01T17:15:55.609Z min_updated=2025-12-01T17:15:55.609Z max_updated=2025-12-01T17:15:55.609Z
AGG gpsc-qqsz FY2023: count=12114 sum=63569204049.36 min_created=2025-12-01T17:15:55.609Z max_created=2025-12-01T17:15:55.609Z min_updated=2025-12-01T17:15:55.609Z max_updated=2025-12-01T17:15:55.609Z
AGG gpsc-qqsz FY2024: count=13718 sum=65189755228.64 min_created=2025-12-01T17:15:55.609Z max_created=2025-12-01T17:15:55.609Z min_updated=2025-12-01T17:15:55.609Z max_updated=2025-12-01T17:15:55.609Z
AGG twsw-2mqa FY2022: count=12156 sum=54698007775.44 min_created=2026-04-01T14:09:46.913Z max_created=2026-04-01T14:09:46.913Z min_updated=2026-04-01T14:09:46.913Z max_updated=2026-04-01T14:09:46.913Z
AGG twsw-2mqa FY2023: count=12114 sum=63569204049.36 min_created=2026-04-01T14:09:46.913Z max_created=2026-04-01T14:09:46.913Z min_updated=2026-04-01T14:09:46.913Z max_updated=2026-04-01T14:09:46.913Z
AGG twsw-2mqa FY2024: count=13648 sum=65131682801.41 min_created=2026-04-01T14:09:46.913Z max_created=2026-04-01T14:09:46.913Z min_updated=2026-04-01T14:09:46.913Z max_updated=2026-04-01T14:09:46.913Z
DIVERGENCE community(gpsc-qqsz) minus official(twsw-2mqa)
FY2022: gpsc_count=12156 twsw_count=12156 row_delta=+0 row_pct_vs_gpsc=0.0000% row_pct_vs_twsw=0.0000% gpsc_sum=54698007774.69 twsw_sum=54698007775.44 amount_delta=-0.75 amount_pct_vs_gpsc=-0.0000000% amount_pct_vs_twsw=-0.0000000%
FY2023: gpsc_count=12114 twsw_count=12114 row_delta=+0 row_pct_vs_gpsc=0.0000% row_pct_vs_twsw=0.0000% gpsc_sum=63569204049.36 twsw_sum=63569204049.36 amount_delta=+0.00 amount_pct_vs_gpsc=0.0000000% amount_pct_vs_twsw=0.0000000%
FY2024: gpsc_count=13718 twsw_count=13648 row_delta=+70 row_pct_vs_gpsc=0.5103% row_pct_vs_twsw=0.5129% gpsc_sum=65189755228.64 twsw_sum=65131682801.41 amount_delta=+58072427.23 amount_pct_vs_gpsc=0.0890821% amount_pct_vs_twsw=0.0891616%
FRESHNESS LAGS (created_at date minus fiscal close date; uniform = min_created == max_created)
gpsc-qqsz FY2022: uniform_created=True created_date=2025-12-01 lag_days=1066
gpsc-qqsz FY2023: uniform_created=True created_date=2025-12-01 lag_days=701
gpsc-qqsz FY2024: uniform_created=True created_date=2025-12-01 lag_days=335
twsw-2mqa FY2022: uniform_created=True created_date=2026-04-01 lag_days=1187
twsw-2mqa FY2023: uniform_created=True created_date=2026-04-01 lag_days=822
twsw-2mqa FY2024: uniform_created=True created_date=2026-04-01 lag_days=456
CONFIRMATIONS
  provenance classifications: gpsc-qqsz=community, twsw-2mqa=official -> True
  schema counts: gpsc-qqsz=23, twsw-2mqa=32, official_only=16, community_only=7 -> True
  FY2022 $0.75 divergence -> True
  all created_at timestamps uniform -> True
EXIT_CODE=0
```

## Step 5 — Data-interface facts

```text
$ curl revisions endpoint and query system columns
REVISION_ENDPOINT_CHECK
HTTP_STATUS=404
CONTENT_TYPE=application/json; charset=utf-8
URL=https://data.ny.gov/api/views/twsw-2mqa/revisions.json
BODY_FIRST_500
{
  "code" : "not_found",
  "error" : true,
  "message" : "No service found for this URL."
}

SYSTEM_COLUMNS_QUERYABLE_CHECK
gpsc-qqsz HTTP_STATUS=200 [{"max_updated": "2025-12-01T17:15:55.609Z", "min_created": "2025-12-01T17:15:55.609Z", "row_count": "111879"}]
twsw-2mqa HTTP_STATUS=200 [{"max_updated": "2026-04-01T14:09:46.913Z", "min_created": "2026-04-01T14:09:46.913Z", "row_count": "107503"}]
EXIT_CODE=0
```

## Step 6 — Adversarial mutate-and-rehash

```text
$ copy snapshot to scratch, mutate one value, rehash manifest, run offline and live comparator
MUTATION old_gpsc_FY2024_row_count=13718 new=99999
REHASHED_MANIFEST_SHA256=635edbcaa550c3fd76688b0c3d12483506a487b212a08ecf056ec56e9bac6d52
VERIFY_HASH_AFTER_REHASH_OFFLINE
[integrity] capture retrieved_utc: 2026-07-19T22:07:28Z

Check 1 -- Provenance classification and divergence
  gpsc-qqsz   provenance=community (MTA Procurement Report (All))
  twsw-2mqa   provenance=official  (MTA Procurements: Beginning 2018)
  2022-12-31 community-vs-official: rows d=+0 (0.0000%), face d=$-0.75 (0.0000000%)  [DIVERGENT]
  2023-12-31 community-vs-official: rows d=+0 (0.0000%), face d=$+0.00 (0.0000000%)  [identical]
  2024-12-31 community-vs-official: rows d=+86351 (86.3519%), face d=$+58072427.23 (0.0890821%)  [DIVERGENT]
  [note] even at identical row count, FY2022 diverges by $0.75 in summed face value -- a value-level difference a coarse (billion-rounded) view misses.

Check 2 -- Snapshot integrity
  SHA-256 OK (635edbcaa550c3fd...)

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
OFFLINE_EXIT_CODE=0
LIVE_COMPARATOR_AFTER_MUTATION
[live] re-pulling data.ny.gov and comparing to the frozen capture...
[live] DRIFT detected on 1 value(s):
  gpsc-qqsz/2024-12-31/row_count: frozen=99999 live=13718
LIVE_EXIT_CODE=2
```

## Regression checks

### F-AM-R1-S-001

Primary requested loci are resolved:

- Reader note Abstract, line 17: claims a "single post-close batch" and explicitly says it is "consistent with a wholesale republish and equally with a first-time bulk load, which a single-pull timestamp cannot distinguish."
- Reader note Section 3 Tier 2, line 37: says a single pull cannot resolve a batch into "a republish versus a first-time bulk load."
- Reader note Section 5.2, line 55: says the note claims only the batch-after-close fact, not which cause produced it.
- Tool output and `reproduce_paper3.py` lines 135 and 147-148: use `POST-CLOSE-BATCH` and print a note that a single pull does not distinguish republish from first-time bulk load.

However, residual non-primary loci still use republish as what the method emits/reports, especially reader note Section 7 line 71: "which the method reports as a republish." I record this as F-AM-R2-S-001.

### F-AM-R1-S-002

Resolved in the reader note. Section 2 line 27 states the substrate uses "the Socrata-declared `provenance` field, not an independent inquiry into agency authorship," and Section 3 line 37 states the classification is read from portal metadata, not an independent chain-of-custody inquiry.

### F-AM-R1-S-003

Resolved in the reader note. Section 4 line 43 describes the row-level system timestamps as "an available freshness signal (row-instantiation timing)" and "not a full change log with prior values or edit authorship." Section 7 line 71 also says the columns record row entry/last-change timing, not full edit history.

## Status-propagation check

- Reader note header line 7: v0.2, one qualifying pass, counter ONE, first of two required.
- Reader note Section 8 line 75: v0.2, one qualifying pass occurred (F-AM-R1), counter one, one further pass required.
- Companion header line 5: mirrors note state v0.2, one qualifying pass, F-AM-R1, counter ONE.
- Companion Current State lines 9-13: authoritative v0.2 state, counter ONE, independent audit history one round, F-AM-R1.

Two stale companion loci remain: line 3 says the companion is to the reader-facing note "v0.1," and line 40 says "Audit rounds: None yet" although line 13 says one round and the F-AM-R1 appendix follows. I record these as F-AM-R2-S-002 and F-AM-R2-S-003.

## Findings

### F-AM-R2-S-001

- **Identifier:** F-AM-R2-S-001
- **Severity:** MEDIUM
- **Locus:** Reader note v0.2 Section 7 line 71; related shorthand in Section 5.4 line 63 and Section 6 line 67.
- **Substance as surface-vs-substrate divergence:** Surface: F-AM-R1-S-001 is presented as absorbed, with the artifact claiming only `POST-CLOSE-BATCH` and not republish as established. Substrate: residual wording still says the method "reports as a republish" and refers to a "republish inference/checks," which can reassert the same overclaim outside the primary corrected loci.
- **Disposition:** Non-blocking because the Abstract, Tier-2 definition, Section 5.2, and tool output are corrected and all reproduced data are unaffected; revise residual wording to "post-close batch" or "batch-load inference" and preserve the first-time-bulk-load alternative wherever republish is mentioned.
- **Cross-reference:** F-AM-R1-S-001.

### F-AM-R2-S-002

- **Identifier:** F-AM-R2-S-002
- **Severity:** LOW
- **Locus:** Companion v0.2 header line 3.
- **Substance as surface-vs-substrate divergence:** Surface: the current-status loci should uniformly identify the current artifact as v0.2. Substrate: the companion header says it is companion to the reader-facing note "v0.1," while the immediately following header line 5 and Current State block state v0.2.
- **Disposition:** Non-blocking status-propagation wording fix; change line 3 to v0.2.
- **Cross-reference:** Status-propagation check, companion header vs companion Current State.

### F-AM-R2-S-003

- **Identifier:** F-AM-R2-S-003
- **Severity:** LOW
- **Locus:** Companion v0.2 line 40 under "Audit rounds."
- **Substance as surface-vs-substrate divergence:** Surface: current-status text says one qualifying round exists, F-AM-R1. Substrate: line 40 says "None yet" and says the first appendix "will be appended," despite the F-AM-R1 appendix appearing immediately below and Current State line 13 saying one round occurred.
- **Disposition:** Non-blocking ledger/status hygiene fix; mark line 40 as superseded historical text or replace it with "F-AM-R1 appended below."
- **Cross-reference:** Status-propagation check; companion Current State lines 12-13.

## Finding count by severity

- CRITICAL: 0
- HIGH: 0
- MEDIUM: 1
- LOW: 2
- INFO: 0

## Final statement

The reproduction package passes the required executable checks: offline hash and four checks pass, self-test detects all 42 perturbations, live re-pull reports no drift, independent recompute confirms metadata/schema/counts/sums/timestamps, interface checks confirm revisions endpoint HTTP 404 and queryable system columns, and adversarial mutate-and-rehash produces comparator DRIFT with nonzero exit after hash success.

Because there are zero CRITICAL and zero HIGH findings and all six reproduction steps were executed and pasted above, my individual qualifying verdict is **PASS**.

---

# Bismillah ir-Rahman ir-Rahim
