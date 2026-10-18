# Bismillah ir-Rahman ir-Rahim

# R0446 -- F-AA-R9 audit report — GPT 5.4

**Chronological Index:** 32 of 995  
**Date:** 2024  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-AA-R9_gpt54.md  
**Source Format:** md  
**SHA-256:** `ae2e893376d31874068bf39c9f943cb1a97938973c9ecabb03443677e24b7e92`  

---

## R0446 · F-AA-R9 audit report — GPT 5.4

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-AA-R9_gpt54.md
- source_format: md
- text_sha256: ae2e893376d31874068bf39c9f943cb1a97938973c9ecabb03443677e24b7e92

# F-AA-R9 audit report — GPT 5.4

## Member identity, lineage, and verdict

- Member: GPT 5.4
- Lineage: OpenAI
- Role in this round: qualifying non-producer rotation member
- Producing lineage excluded from verdict: Claude / Anthropic
- Verdict: PASS
- Executed reproduction: YES
- CRITICAL findings: 0
- HIGH findings: 0

## No-prior-state attestation

I am a fresh instance with no memory of prior rounds and no access to other members' work.

## Protocol execution status

### Step 1 — `python3 reproduce_paper2.py`
Status: EXECUTED

Command:
```bash
cd /home/user/workspace/audit-r9/member-gpt54 && python3 reproduce_paper2.py
```

Output:
```text
[integrity] hash OK, field inventory OK (22 fields), 37988 rows

[4.2] MWBE count vs dollar share (both estimands), by vintage:
  FY2022: count 16.4%  face 3.27% (x5.0)  exp 4.25% (x3.9)  [face $54.7B exp $6.8B miss 712 zero 0]
  FY2023: count 18.6%  face 3.51% (x5.3)  exp 6.27% (x3.0)  [face $63.6B exp $6.7B miss 1049 zero 111]
  FY2024: count 18.7%  face 3.95% (x4.7)  exp 7.06% (x2.7)  [face $65.2B exp $8.2B miss 1348 zero 48]
[4.1] FY2024 process (face | exp):
  Authority Contract - Competitive Bid     face 92.22%  exp 89.65%
  Authority Contract - Non-Competitive B   face  7.78%  exp  4.73%
  Purchased Under State Contract           face  0.00%  exp  3.24%
  Non Contract Procurement/Purchase Orde   face  0.00%  exp  2.38%
[4.3] face conc  top5 22.1% top10 30.4% top20 41.8% gini 0.931 (vendors 2656)
[4.3] exp  conc  top5 16.9% top10 26.2% top20 37.6% gini 0.904
[4.0] pre-2024-award face share 91.7% (stock, not FY2024 flow)
```

### Step 2 — `python3 reproduce_paper2.py --selftest`
Status: EXECUTED

Command:
```bash
cd /home/user/workspace/audit-r9/member-gpt54 && python3 reproduce_paper2.py --selftest
```

Output:
```text
[integrity] hash OK, field inventory OK (22 fields), 37988 rows

[4.2] MWBE count vs dollar share (both estimands), by vintage:
  FY2022: count 16.4%  face 3.27% (x5.0)  exp 4.25% (x3.9)  [face $54.7B exp $6.8B miss 712 zero 0]
  FY2023: count 18.6%  face 3.51% (x5.3)  exp 6.27% (x3.0)  [face $63.6B exp $6.7B miss 1049 zero 111]
  FY2024: count 18.7%  face 3.95% (x4.7)  exp 7.06% (x2.7)  [face $65.2B exp $8.2B miss 1348 zero 48]
[4.1] FY2024 process (face | exp):
  Authority Contract - Competitive Bid     face 92.22%  exp 89.65%
  Authority Contract - Non-Competitive B   face  7.78%  exp  4.73%
  Purchased Under State Contract           face  0.00%  exp  3.24%
  Non Contract Procurement/Purchase Orde   face  0.00%  exp  2.38%
[4.3] face conc  top5 22.1% top10 30.4% top20 41.8% gini 0.931 (vendors 2656)
[4.3] exp  conc  top5 16.9% top10 26.2% top20 37.6% gini 0.904
[4.0] pre-2024-award face share 91.7% (stock, not FY2024 flow)

[selftest] perturbing each statistic to confirm the comparator detects it...
[selftest] PASS: comparator detected all 45 deliberate perturbations
```

### Step 3 — `python3 reproduce_paper2.py --live`
Status: EXECUTED

Command:
```bash
cd /home/user/workspace/audit-r9/member-gpt54 && python3 reproduce_paper2.py --live
```

Output:
```text
[integrity] hash OK, field inventory OK (22 fields), 37988 rows

[4.2] MWBE count vs dollar share (both estimands), by vintage:
  FY2022: count 16.4%  face 3.27% (x5.0)  exp 4.25% (x3.9)  [face $54.7B exp $6.8B miss 712 zero 0]
  FY2023: count 18.6%  face 3.51% (x5.3)  exp 6.27% (x3.0)  [face $63.6B exp $6.7B miss 1049 zero 111]
  FY2024: count 18.7%  face 3.95% (x4.7)  exp 7.06% (x2.7)  [face $65.2B exp $8.2B miss 1348 zero 48]
[4.1] FY2024 process (face | exp):
  Authority Contract - Competitive Bid     face 92.22%  exp 89.65%
  Authority Contract - Non-Competitive B   face  7.78%  exp  4.73%
  Purchased Under State Contract           face  0.00%  exp  3.24%
  Non Contract Procurement/Purchase Orde   face  0.00%  exp  2.38%
[4.3] face conc  top5 22.1% top10 30.4% top20 41.8% gini 0.931 (vendors 2656)
[4.3] exp  conc  top5 16.9% top10 26.2% top20 37.6% gini 0.904
[4.0] pre-2024-award face share 91.7% (stock, not FY2024 flow)

[live] pulling all three years and comparing EVERY statistic + schema + row count...
[live] no drift on any published statistic, schema, or row count
```

### Step 4 — Independent recompute with my own code
Status: EXECUTED

I wrote and ran `/home/user/workspace/audit-r9/member-gpt54/independent_recompute_gpt54.py` without importing the supplied functions.

Command:
```bash
cd /home/user/workspace/audit-r9/member-gpt54 && python3 independent_recompute_gpt54.py
```

Output:
```text
[independent] loaded snapshot without importing supplied functions
total_rows=37988; FY rows: 2022=12156 2023=12114 2024=13718
FY2024 face_total=65189755228.64
FY2024 annual_expenditure_total=8170228558.54
FY2024 MWBE prime shares: count=18.7345% face=3.9532% annual_expenditure=7.0612%
FY2024 top10 face concentration=30.4151%
FY2024 vendor gini face=0.93117 annual_expenditure=0.90435
18-field overlaps: 2022-2023=2115 2022-2024=604 2023-2024=1002
exact all-field pairwise overlaps: 2022-2023=0 2022-2024=0 2023-2024=0
three_way_18=265; three_way_exact=0
stable18_field_count=18; exact_field_count=22
```

### Step 5 — Live provenance queries to `gpsc-qqsz` and `twsw-2mqa`
Status: EXECUTED

Command 1:
```bash
python3 - <<'PY'
import json, urllib.parse, urllib.request
resources = ['gpsc-qqsz', 'twsw-2mqa']
where = "fiscal_year_end_date='2024-12-31T00:00:00.000'"
for rid in resources:
    query = urllib.parse.urlencode({
        '$select': 'count(*),sum(contract_amount)',
        '$where': where,
    })
    url = f'https://data.ny.gov/resource/{rid}.json?{query}'
    data = json.load(urllib.request.urlopen(url, timeout=60))
    print(rid)
    print(url)
    print(json.dumps(data, indent=2))
PY
```

Output 1:
```text
gpsc-qqsz
https://data.ny.gov/resource/gpsc-qqsz.json?%24select=count%28%2A%29%2Csum%28contract_amount%29&%24where=fiscal_year_end_date%3D%272024-12-31T00%3A00%3A00.000%27
[
  {
    "count": "13718",
    "sum_contract_amount": "65189755228.64"
  }
]
twsw-2mqa
https://data.ny.gov/resource/twsw-2mqa.json?%24select=count%28%2A%29%2Csum%28contract_amount%29&%24where=fiscal_year_end_date%3D%272024-12-31T00%3A00%3A00.000%27
[
  {
    "count": "13648",
    "sum_contract_amount": "65131682801.41"
  }
]
```

Command 2:
```bash
python3 - <<'PY'
from decimal import Decimal
count_gpsc = Decimal('13718')
count_twsw = Decimal('13648')
face_gpsc = Decimal('65189755228.64')
face_twsw = Decimal('65131682801.41')
count_div = (count_gpsc - count_twsw) / count_gpsc * 100
face_div = (face_gpsc - face_twsw) / face_gpsc * 100
print(f'count divergence pct vs gpsc baseline = {count_div:.6f}%')
print(f'face divergence pct vs gpsc baseline = {face_div:.6f}%')
print(f'raw count difference = {count_gpsc - count_twsw}')
print(f'raw face difference = {face_gpsc - face_twsw}')
PY
```

Output 2:
```text
count divergence pct vs gpsc baseline = 0.510278%
face divergence pct vs gpsc baseline = 0.089082%
raw count difference = 70
raw face difference = 58072427.23
```

### Step 6 — Live capital join test across `wcsa-vkhf`, `kizb-nxtu`, and `ehz8-ag3n`
Status: EXECUTED

Command 1:
```bash
python3 - <<'PY'
import json, urllib.parse, urllib.request
BASE = 'https://data.ny.gov/resource'

def fetch_json(url):
    return json.load(urllib.request.urlopen(url, timeout=60))

url_wcsa = BASE + '/wcsa-vkhf.json?' + urllib.parse.urlencode({
    '$select': 'project_number,latitude,longitude',
    '$where': 'project_number is not null',
    '$limit': '20'
})
wcsa_rows = fetch_json(url_wcsa)
project_numbers = [r['project_number'] for r in wcsa_rows]
in_list = '(' + ','.join(["'" + p.replace("'", "''") + "'" for p in project_numbers]) + ')'

url_kizb = BASE + '/kizb-nxtu.json?' + urllib.parse.urlencode({
    '$select': 'project_number,count(*)',
    '$where': f'project_number in {in_list}',
    '$group': 'project_number',
    '$limit': '50'
})
url_ehz8 = BASE + '/ehz8-ag3n.json?' + urllib.parse.urlencode({
    '$select': 'proj_num,count(*)',
    '$where': f'proj_num in {in_list}',
    '$group': 'proj_num',
    '$limit': '50'
})

kizb_rows = fetch_json(url_kizb)
ehz8_rows = fetch_json(url_ehz8)

print('wcsa-vkhf sample URL')
print(url_wcsa)
print('wcsa-vkhf sample rows')
print(json.dumps(wcsa_rows, indent=2))
print('wcsa-vkhf keys from first row')
print(sorted(wcsa_rows[0].keys()))
print('contains borough-like key?', any('borough' in k.lower() for k in wcsa_rows[0].keys()))
print('sample project_numbers')
print(project_numbers)
print('kizb-nxtu grouped matches URL')
print(url_kizb)
print(json.dumps(kizb_rows, indent=2))
print('ehz8-ag3n grouped matches URL')
print(url_ehz8)
print(json.dumps(ehz8_rows, indent=2))
print(f'joined project_numbers found in kizb-nxtu: {len(kizb_rows)}/{len(project_numbers)}')
print(f'joined project_numbers found in ehz8-ag3n: {len(ehz8_rows)}/{len(project_numbers)}')
PY
```

Output 1:
```text
wcsa-vkhf sample URL
https://data.ny.gov/resource/wcsa-vkhf.json?%24select=project_number%2Clatitude%2Clongitude&%24where=project_number+is+not+null&%24limit=20
wcsa-vkhf sample rows
[
  {
    "project_number": "D701HH89",
    "latitude": "40.8796260",
    "longitude": "-73.9186440"
  },
  {
    "project_number": "D703HH63",
    "latitude": "40.8796260",
    "longitude": "-73.9186440"
  },
  {
    "project_number": "ED040307",
    "latitude": "40.8170850",
    "longitude": "-73.8037800"
  },
  {
    "project_number": "ET050213",
    "latitude": "40.7014230",
    "longitude": "-74.0138550"
  },
  {
    "project_number": "ET120309",
    "latitude": "40.5741030",
    "longitude": "-74.1656130"
  },
  {
    "project_number": "L50701PG",
    "latitude": "40.7246000",
    "longitude": "-73.7064870"
  },
  {
    "project_number": "T5041113",
    "latitude": "40.6089710",
    "longitude": "-73.9577670"
  },
  {
    "project_number": "T6060305",
    "latitude": "40.7548270",
    "longitude": "-73.9626890"
  },
  {
    "project_number": "T6070321",
    "latitude": "40.7463300",
    "longitude": "-73.9639520"
  },
  {
    "project_number": "T7041214",
    "latitude": "40.6924440",
    "longitude": "-73.8599500"
  },
  {
    "project_number": "T7160717",
    "latitude": "40.5937880",
    "longitude": "-73.9922310"
  },
  {
    "project_number": "T6041261",
    "latitude": "40.6613800",
    "longitude": "-73.9622040"
  },
  {
    "project_number": "ET060320",
    "latitude": "40.7040070",
    "longitude": "-74.0115500"
  },
  {
    "project_number": "ET100218",
    "latitude": "40.8670280",
    "longitude": "-73.9230730"
  },
  {
    "project_number": "D701AW98",
    "latitude": "40.7420360",
    "longitude": "-73.9521930"
  },
  {
    "project_number": "T8050311",
    "latitude": "40.8864890",
    "longitude": "-73.9000760"
  },
  {
    "project_number": "T8080672",
    "latitude": "40.8670340",
    "longitude": "-73.8935010"
  },
  {
    "project_number": "T8070379",
    "latitude": "40.8353780",
    "longitude": "-73.8483270"
  },
  {
    "project_number": "T6041278",
    "latitude": "40.7491460",
    "longitude": "-73.8696290"
  },
  {
    "project_number": "T6080650",
    "latitude": "40.8484810",
    "longitude": "-73.9118130"
  }
]
wcsa-vkhf keys from first row
['latitude', 'longitude', 'project_number']
contains borough-like key? False
sample project_numbers
['D701HH89', 'D703HH63', 'ED040307', 'ET050213', 'ET120309', 'L50701PG', 'T5041113', 'T6060305', 'T6070321', 'T7041214', 'T7160717', 'T6041261', 'ET060320', 'ET100218', 'D701AW98', 'T8050311', 'T8080672', 'T8070379', 'T6041278', 'T6080650']
kizb-nxtu grouped matches URL
https://data.ny.gov/resource/kizb-nxtu.json?%24select=project_number%2Ccount%28%2A%29&%24where=project_number+in+%28%27D701HH89%27%2C%27D703HH63%27%2C%27ED040307%27%2C%27ET050213%27%2C%27ET120309%27%2C%27L50701PG%27%2C%27T5041113%27%2C%27T6060305%27%2C%27T6070321%27%2C%27T7041214%27%2C%27T7160717%27%2C%27T6041261%27%2C%27ET060320%27%2C%27ET100218%27%2C%27D701AW98%27%2C%27T8050311%27%2C%27T8080672%27%2C%27T8070379%27%2C%27T6041278%27%2C%27T6080650%27%29&%24group=project_number&%24limit=50
[
  {
    "project_number": "D701AW98",
    "count": "1"
  },
  {
    "project_number": "D701HH89",
    "count": "1"
  },
  {
    "project_number": "D703HH63",
    "count": "1"
  },
  {
    "project_number": "ED040307",
    "count": "1"
  },
  {
    "project_number": "ET050213",
    "count": "1"
  },
  {
    "project_number": "ET060320",
    "count": "1"
  },
  {
    "project_number": "ET100218",
    "count": "1"
  },
  {
    "project_number": "ET120309",
    "count": "1"
  },
  {
    "project_number": "L50701PG",
    "count": "6"
  },
  {
    "project_number": "T5041113",
    "count": "6"
  },
  {
    "project_number": "T6041261",
    "count": "1"
  },
  {
    "project_number": "T6041278",
    "count": "1"
  },
  {
    "project_number": "T6060305",
    "count": "1"
  },
  {
    "project_number": "T6070321",
    "count": "1"
  },
  {
    "project_number": "T6080650",
    "count": "1"
  },
  {
    "project_number": "T7041214",
    "count": "1"
  },
  {
    "project_number": "T7160717",
    "count": "1"
  },
  {
    "project_number": "T8050311",
    "count": "1"
  },
  {
    "project_number": "T8070379",
    "count": "1"
  },
  {
    "project_number": "T8080672",
    "count": "1"
  }
]
ehz8-ag3n grouped matches URL
https://data.ny.gov/resource/ehz8-ag3n.json?%24select=proj_num%2Ccount%28%2A%29&%24where=proj_num+in+%28%27D701HH89%27%2C%27D703HH63%27%2C%27ED040307%27%2C%27ET050213%27%2C%27ET120309%27%2C%27L50701PG%27%2C%27T5041113%27%2C%27T6060305%27%2C%27T6070321%27%2C%27T7041214%27%2C%27T7160717%27%2C%27T6041261%27%2C%27ET060320%27%2C%27ET100218%27%2C%27D701AW98%27%2C%27T8050311%27%2C%27T8080672%27%2C%27T8070379%27%2C%27T6041278%27%2C%27T6080650%27%29&%24group=proj_num&%24limit=50
[
  {
    "proj_num": "D701AW98",
    "count": "24"
  },
  {
    "proj_num": "D701HH89",
    "count": "24"
  },
  {
    "proj_num": "D703HH63",
    "count": "24"
  },
  {
    "proj_num": "ED040307",
    "count": "24"
  },
  {
    "proj_num": "ET050213",
    "count": "24"
  },
  {
    "proj_num": "ET060320",
    "count": "24"
  },
  {
    "proj_num": "ET100218",
    "count": "24"
  },
  {
    "proj_num": "ET120309",
    "count": "24"
  },
  {
    "proj_num": "L50701PG",
    "count": "22"
  },
  {
    "proj_num": "T5041113",
    "count": "22"
  },
  {
    "proj_num": "T6041261",
    "count": "24"
  },
  {
    "proj_num": "T6041278",
    "count": "24"
  },
  {
    "proj_num": "T6060305",
    "count": "24"
  },
  {
    "proj_num": "T6070321",
    "count": "24"
  },
  {
    "proj_num": "T6080650",
    "count": "24"
  },
  {
    "proj_num": "T7041214",
    "count": "24"
  },
  {
    "proj_num": "T7160717",
    "count": "24"
  },
  {
    "proj_num": "T8050311",
    "count": "24"
  },
  {
    "proj_num": "T8070379",
    "count": "2"
  },
  {
    "proj_num": "T8080672",
    "count": "1"
  }
]
joined project_numbers found in kizb-nxtu: 20/20
joined project_numbers found in ehz8-ag3n: 20/20
```

Command 2:
```bash
python3 - <<'PY'
import json, urllib.parse, urllib.request
url = 'https://data.ny.gov/resource/wcsa-vkhf.json?' + urllib.parse.urlencode({
    '$where': 'project_number is not null',
    '$limit': '1'
})
row = json.load(urllib.request.urlopen(url, timeout=60))[0]
print(url)
print(sorted(row.keys()))
print('borough-like keys:', [k for k in row.keys() if 'borough' in k.lower()])
PY
```

Output 2:
```text
https://data.ny.gov/resource/wcsa-vkhf.json?%24where=project_number+is+not+null&%24limit=1
['agency_name', 'capital_plan', 'category_description', 'element_description', 'georeference', 'latitude', 'location', 'location_indicator', 'longitude', 'plan_series', 'project_description', 'project_number', 'project_number_sequence']
borough-like keys: []
```

### Step 7 — Adversarial mutation test
Status: EXECUTED

I mutated one non-MWBE FY2024 `contract_amount` in a copied package, re-hashed the manifest, and reran `--live` from the copied package. The comparator returned DRIFT with exit code 2, so this step passed on comparator behavior rather than a hash abort.

Command:
```bash
python3 - <<'PY'
import json, hashlib, os, shutil, subprocess
src = '/home/user/workspace/audit-r9/member-gpt54'
dst = '/home/user/workspace/audit-r9/member-gpt54-adversarial-large'
shutil.copytree(src, dst, dirs_exist_ok=True)
snap = os.path.join(dst, 'snapshot', 'gpsc-qqsz_FY2022-2024.json')
man = os.path.join(dst, 'snapshot', 'MANIFEST.json')
with open(snap, 'r') as f:
    rows = json.load(f)
mutated = None
for r in rows:
    if r.get('fiscal_year_end_date') == '2024-12-31T00:00:00.000' and r.get('vendor_is_a_mwbe') != 'Y':
        try:
            amt = float(r.get('contract_amount'))
        except (TypeError, ValueError):
            continue
        if amt > 0:
            r['contract_amount'] = f'{amt + 10000000:.2f}'
            mutated = {
                'vendor_name': r.get('vendor_name'),
                'award_date': r.get('award_date'),
                'old_contract_amount': f'{amt:.2f}',
                'new_contract_amount': r['contract_amount'],
            }
            break
if mutated is None:
    raise SystemExit('No suitable non-MWBE row found to mutate.')
raw = json.dumps(rows, sort_keys=True, separators=(',', ':'))
with open(snap, 'w') as f:
    f.write(raw)
with open(man, 'r') as f:
    manifest = json.load(f)
manifest['sha256_of_canonical_json'] = hashlib.sha256(raw.encode()).hexdigest()
with open(man, 'w') as f:
    json.dump(manifest, f, indent=2)
print('[mutation-large] mutated one non-MWBE FY2024 contract_amount and re-hashed manifest')
print(json.dumps(mutated, indent=2))
proc = subprocess.run(['python3', 'reproduce_paper2.py', '--live'], cwd=dst, capture_output=True, text=True)
print('[mutation-large] stdout begin')
print(proc.stdout, end='')
print('[mutation-large] stdout end')
print('[mutation-large] stderr begin')
print(proc.stderr, end='')
print('[mutation-large] stderr end')
print(f'[mutation-large] exit_code={proc.returncode}')
PY
```

Output:
```text
[mutation-large] mutated one non-MWBE FY2024 contract_amount and re-hashed manifest
{
  "vendor_name": "22ND CENTURY TECHNOLOGIES, INC",
  "award_date": "2016-07-01T00:00:00.000",
  "old_contract_amount": "4500000.00",
  "new_contract_amount": "14500000.00"
}
[mutation-large] stdout begin
[integrity] hash OK, field inventory OK (22 fields), 37988 rows

[4.2] MWBE count vs dollar share (both estimands), by vintage:
  FY2022: count 16.4%  face 3.27% (x5.0)  exp 4.25% (x3.9)  [face $54.7B exp $6.8B miss 712 zero 0]
  FY2023: count 18.6%  face 3.51% (x5.3)  exp 6.27% (x3.0)  [face $63.6B exp $6.7B miss 1049 zero 111]
  FY2024: count 18.7%  face 3.95% (x4.7)  exp 7.06% (x2.7)  [face $65.2B exp $8.2B miss 1348 zero 48]
[4.1] FY2024 process (face | exp):
  Authority Contract - Competitive Bid     face 92.22%  exp 89.65%
  Authority Contract - Non-Competitive B   face  7.78%  exp  4.73%
  Purchased Under State Contract           face  0.00%  exp  3.24%
  Non Contract Procurement/Purchase Orde   face  0.00%  exp  2.38%
[4.3] face conc  top5 22.1% top10 30.4% top20 41.8% gini 0.931 (vendors 2656)
[4.3] exp  conc  top5 16.9% top10 26.2% top20 37.6% gini 0.904
[4.0] pre-2024-award face share 91.7% (stock, not FY2024 flow)

[live] pulling all three years and comparing EVERY statistic + schema + row count...
[live] DRIFT on 1 field(s):
   2024.face_total: frozen=65199755228.6400 vs live=65189755228.6400 (tol 6.51998e+06)
[mutation-large] stdout end
[mutation-large] stderr begin
[mutation-large] stderr end
[mutation-large] exit_code=2
```

## Audit-scope and regression checks

- Estimand / stock-flow integrity: confirmed.
- MWBE framing: current text is descriptive and does not currently claim goal attainment, operative-substrate status, short-measure language, or a compliance pass.
- Concentration framing: current text presents concentration as a structural explanation and withholds Tier 3 intent / culpability claims.
- Fingerprint prose: current reader text matches the 18-field method and the reported pairwise overlaps; exact all-field overlap is zero.
- Provenance: current text separates face divergence from count divergence.
- Single convergence counter: current-status loci are mutually consistent on v0.7, eight audit rounds, and consecutive qualifying-PASS count ONE.
- Section 8 package direction: current text correctly says the package must be handed directly and that its own DOI remains pending.
- Prior findings disposition: the absorbed findings and the still-open owner action F-AA-R5-C-01 are described consistently; I did not find a new current status-propagation defect.

## Findings (namespace F-AA-R9)

1. **Identifier:** F-AA-R9-01
   **Severity:** LOW
   **Locus:** `AUDIT_PROTOCOL.md` exact reproduction specifications, fingerprint line.
   **Substance (surface vs substrate):** the protocol line states the 18-field fingerprint has the reproduced pairwise overlaps `2,115 / 604 / 1,002` and then says `No three-way intersection`; my independent 18-field recompute reproduced the stated pairwise overlaps and exact all-field pairwise zero, but the stable 18-field three-way intersection was `265`, not zero.
   **Disposition:** recorded as a brief-level wording/value nuance only; I did not find a corresponding incorrect current claim in the reader note or companion, and it does not affect the pass criterion because there are still 0 CRITICAL and 0 HIGH findings.
   **Cross-reference:** Step 4 output above; `AUDIT_PROTOCOL.md` line 21.

## Final statement

I executed the reproduction. All seven mandatory protocol steps were executed. I return PASS with 0 CRITICAL and 0 HIGH.

---

# Bismillah ir-Rahman ir-Rahim
