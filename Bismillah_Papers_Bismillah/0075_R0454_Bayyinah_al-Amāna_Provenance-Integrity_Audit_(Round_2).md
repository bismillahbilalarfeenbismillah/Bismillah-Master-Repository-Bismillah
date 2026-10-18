# Bismillah ir-Rahman ir-Rahim

# R0454 -- Bayyinah al-Amāna Provenance-Integrity Audit (Round 2)

**Chronological Index:** 75 of 995  
**Date:** 2024-12-31  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-AM-R2_gemini31.md  
**Source Format:** md  
**SHA-256:** `01d8a5769f5fbee29f00df8a47d614949b4869247ea6cabc769ca53b0b2c2dad`  

---

## R0454 · Bayyinah al-Amāna Provenance-Integrity Audit (Round 2)

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-AM-R2_gemini31.md
- source_format: md
- text_sha256: 01d8a5769f5fbee29f00df8a47d614949b4869247ea6cabc769ca53b0b2c2dad

# Bayyinah al-Amāna Provenance-Integrity Audit (Round 2)
**Auditor**: Gemini 3.1 Pro (Google) - QUALIFYING
**Namespace**: F-AM-R2

## Attestation
"Fresh, memoryless instance; did not access any other member's work; worked only from my own directory copy."

## Executed Steps

### Step 1: Baseline Offline Reproduction
**Command:** `python3 reproduce_paper3.py`
**Output:**
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
```
**Exit Code:** 0

### Step 2: Comparator Selftest
**Command:** `python3 reproduce_paper3.py --selftest`
**Output:**
```
[selftest] perturbing each captured value to confirm the comparator detects it...
[selftest] perturbed 42 captured values; comparator missed 0
```
**Exit Code:** 0

### Step 3: Live Verification
**Command:** `python3 reproduce_paper3.py --live`
**Output:**
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

[note] POST-CLOSE-BATCH = uniform :created_at postdating the period close (one batch load);
       a single pull does not distinguish a republish from a first-time bulk load.
[note] Divergences and batch loads are substrate facts. This tool does not judge whether any was legitimate, authorized, or improper (Tier 3, refused).
```
**Exit Code:** 0

### Step 4: Independent Recompute
**Code Executed:**
```python
import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def fetch_json(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, context=ctx) as response:
         return json.loads(response.read())

print("--- METADATA ---")
meta_gpsc = fetch_json("https://data.ny.gov/api/views/gpsc-qqsz.json")
meta_twsw = fetch_json("https://data.ny.gov/api/views/twsw-2mqa.json")

print(f"gpsc-qqsz provenance={meta_gpsc.get('provenance')}, name={meta_gpsc.get('name')}, fields={len(meta_gpsc.get('columns', []))}")
print(f"twsw-2mqa provenance={meta_twsw.get('provenance')}, name={meta_twsw.get('name')}, fields={len(meta_twsw.get('columns', []))}")

print("\n--- SODA QUERY ---")
years = [2022, 2023, 2024]
for y in years:
    q = f"$select=count(*),sum(contract_amount),min(:created_at),max(:created_at),min(:updated_at),max(:updated_at)&$where=fiscal_year_end_date='{y}-12-31T00:00:00.000'"
    q = q.replace(" ", "%20")
    data_gpsc = fetch_json(f"https://data.ny.gov/resource/gpsc-qqsz.json?{q}")[0]
    data_twsw = fetch_json(f"https://data.ny.gov/resource/twsw-2mqa.json?{q}")[0]

    print(f"\nFY{y}:")
    print(f"  gpsc-qqsz: rows={data_gpsc.get('count')}, sum={float(data_gpsc.get('sum_contract_amount', 0)):.2f}, min_created={data_gpsc.get('min_created_at')}")
    print(f"  twsw-2mqa: rows={data_twsw.get('count')}, sum={float(data_twsw.get('sum_contract_amount', 0)):.2f}, min_created={data_twsw.get('min_created_at')}")

    diff_rows = int(data_gpsc.get('count')) - int(data_twsw.get('count'))
    diff_sum = float(data_gpsc.get('sum_contract_amount', 0)) - float(data_twsw.get('sum_contract_amount', 0))
    print(f"  Difference: rows {diff_rows}, sum {diff_sum:.2f}")
```
**Output:**
```
--- METADATA ---
gpsc-qqsz provenance=community, name=MTA Procurement Report (All), fields=23
twsw-2mqa provenance=official, name=MTA Procurements: Beginning 2018, fields=32

--- SODA QUERY ---

FY2022:
  gpsc-qqsz: rows=12156, sum=54698007774.69, min_created=2025-12-01T17:15:55.609Z
  twsw-2mqa: rows=12156, sum=54698007775.44, min_created=2026-04-01T14:09:46.913Z
  Difference: rows 0, sum -0.75

FY2023:
  gpsc-qqsz: rows=12114, sum=63569204049.36, min_created=2025-12-01T17:15:55.609Z
  twsw-2mqa: rows=12114, sum=63569204049.36, min_created=2026-04-01T14:09:46.913Z
  Difference: rows 0, sum 0.00

FY2024:
  gpsc-qqsz: rows=13718, sum=65189755228.64, min_created=2025-12-01T17:15:55.609Z
  twsw-2mqa: rows=13648, sum=65131682801.41, min_created=2026-04-01T14:09:46.913Z
  Difference: rows 70, sum 58072427.23
```

### Step 5: Data-Interface Facts
**Command 1:** `curl -sI https://data.ny.gov/api/views/twsw-2mqa/revisions.json | head -n 1`
**Output 1:** `HTTP/1.1 404 Not Found`

**Command 2:** `curl -s "https://data.ny.gov/resource/twsw-2mqa.json?\$select=:created_at,:updated_at&\$limit=1"`
**Output 2:** `[{":created_at":"2026-04-01T14:09:46.913Z",":updated_at":"2026-04-01T14:09:46.913Z"}]`

### Step 6: Adversarial Testing
**Methodology:**
Copied `snapshot` and `reproduce_paper3.py` to `scratch`. Used `sed` to replace `"row_count": 13718,` with `"row_count": 99999,` inside `snapshot/provenance_capture.json`. Ran python script to recalculate and overwrite `sha256` value in `snapshot/MANIFEST.json`. Ran `python3 reproduce_paper3.py --live`.
**Output:**
```
[live] re-pulling data.ny.gov and comparing to the frozen capture...
[live] DRIFT detected on 1 value(s):
  gpsc-qqsz/2024-12-31/row_count: frozen=99999 live=13718
```
**Exit Code:** 2
*The test confirms that even if MANIFEST hash checking is bypassed, the live drift checking detects the data mutation and returns a non-zero exit code.*

## Regression Checks
- **F-AM-R1-S-001:** Reader note Abstract, Section 3 (Tier 2), and Section 5.2 explicitly hedge the batch creation time as "equally consistent with a first-time bulk load" vs a republish, admitting the single-pull timestamp cannot distinguish them. The tool prints `POST-CLOSE-BATCH` instead of `WHOLESALE-REPUBLISH` and notes "a single pull does not distinguish a republish from a first-time bulk load." (PASS)
- **F-AM-R1-S-002:** Reader note Section 3 (Tier 2) explicitly states "provenance classification read from portal metadata (the Socrata-declared `provenance` field, official versus community view, not an independent chain-of-custody inquiry)". (PASS)
- **F-AM-R1-S-003:** Reader note Section 4 explicitly states "row-level system timestamps supply an available freshness signal (row-instantiation timing) in its place, though not a full change log with prior values or edit authorship." (PASS)

## Status-Propagation Check
- **Reader Note Header:** "Working draft v0.2 (one qualifying cross-instance audit pass so far, F-AM-R1: the consecutive qualifying-PASS count is ONE" (PASS)
- **Reader Note Section 8:** "This is a v0.2 draft. [...] The consecutive qualifying-PASS count is one, the first of the two required" (PASS)
- **Companion Header:** "Mirrors note state v0.2 (one qualifying cross-instance audit pass, F-AM-R1; the consecutive qualifying-PASS count is ONE, the first of the two required)." (PASS)
- **Companion Current State:** "Artifact state: v0.2", "Consecutive qualifying-PASS count (single operational counter): ONE." (PASS)
*All current-status loci are uniformly v0.2, count ONE, round one.*

## Verdict and Findings

No findings.

Verdict: **PASS** (0 CRITICAL, 0 HIGH, all reproduction and checks executed successfully).

---

# Bismillah ir-Rahman ir-Rahim
