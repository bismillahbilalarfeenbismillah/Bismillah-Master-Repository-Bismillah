# Bismillah ir-Rahman ir-Rahim

# R0477 -- Bayyinah al-Amāna -- Provenance Integrity for Public Open Data: Reproduction and Audit Dataset (v1.0)

**Chronological Index:** 104 of 995  
**Date:** 2025-12-01  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** README.md  
**Source Format:** md  
**SHA-256:** `3e8c095bf4c980b1e9e291ea9f9fe71a0da1a137a33f53cffca72e7cc3c9e36e`  

---

## R0477 · Bayyinah al-Amāna -- Provenance Integrity for Public Open Data: Reproduction and Audit Dataset (v1.0)

- section: VI. Applied Audits & Public-Data Studies
- source_file: README.md
- source_format: md
- text_sha256: 3e8c095bf4c980b1e9e291ea9f9fe71a0da1a137a33f53cffca72e7cc3c9e36e

# Bayyinah al-Amāna -- Provenance Integrity for Public Open Data: Reproduction and Audit Dataset (v1.0)

This dataset reproduces four provenance-integrity checks against a frozen capture of two New York State open-data (Socrata) datasets, re-pulls the live endpoints to detect drift, and includes the full three-round cross-instance audit trail.

## Related deposits

- Reader note (paper): DOI 10.5281/zenodo.21446613
- Audit and provenance ledger: DOI 10.5281/zenodo.21446618
- This dataset is deposited alongside the ledger (DOI 10.5281/zenodo.21446618). The artifact converged after three consecutive qualifying cross-instance passes (gate met at F-AM-R2, confirmed clean at F-AM-R3 with the rotation gap closed).

## Datasets

- `gpsc-qqsz` -- "MTA Procurement Report (All)", provenance **community** (a community-created view).
- `twsw-2mqa` -- "MTA Procurements: Beginning 2018", provenance **official** (first-party).

Both are served from `data.ny.gov`.

## Contents

- `reproduce_paper3.py` -- standard-library Python; verifies the frozen capture's hash and reproduces all four checks (`default`), re-pulls and compares to the live endpoints (`--live`), and perturbs every captured value to confirm the comparator detects it (`--selftest`).
- `snapshot/provenance_capture.json` -- the frozen capture: per-dataset provenance, declared update time, schema field inventory, and per-fiscal-year row counts, face totals, and row-level `:created_at`/`:updated_at` system timestamps.
- `snapshot/MANIFEST.json` -- the SHA-256 of the capture; the script aborts on mismatch.
- `audit-reports/` -- the primary auditor outputs for all three rounds (F-AM-R1/R2/R3), organized by round: each Model Council member report and each synthesis, the source records behind the ledger's summaries.
- `audit-reports/` -- the primary auditor outputs for all three cross-instance rounds (F-AM-R1, R2, R3), organized by round, including each Model Council member report and each synthesis. These are the source records behind the ledger's summaries. The artifact converged after three consecutive qualifying passes (the gate met at R2, confirmed clean at R3 with the rotation gap closed).

## How to run

Requires Python 3 (standard library only).

```
python3 reproduce_paper3.py            # verify hash + reproduce the four checks, offline
python3 reproduce_paper3.py --selftest # perturb every captured value; confirm all are detected
python3 reproduce_paper3.py --live     # re-pull data.ny.gov and compare to the frozen capture
```

## The four checks and what the capture shows

1. **Provenance classification and divergence.** `gpsc-qqsz` declares itself a community view; `twsw-2mqa` is official. Their FY2023 windows are byte-identical; FY2024 diverges by 70 records and about $58.1M (0.5103% count, 0.0891% face); and FY2022, despite identical row counts, diverges by $0.75 in summed face value -- a value-level difference a billion-rounded view misses.
2. **Snapshot integrity.** SHA-256 of the capture matches the manifest.
3. **Declared-vs-actual freshness (primary method).** Each dataset's currently-served history carries row `:created_at` timestamps long after the reporting period closed: the community view's rows were created 2025-12-01 (335 to 1066 days after each fiscal year), the official dataset's on 2026-04-01 (456 to 1187 days after), uniformly across rows -- a single post-close batch load (consistent with a wholesale republish or a first-time bulk load; a single pull does not distinguish them), detectable without a two-pull time gap.
4. **Schema divergence.** The community view serves 23 fields, the official dataset 32; 16 fields are official-only and 7 community-only.

## Refusal boundary

Divergences and republishes are substrate facts. Republishes, migrations, and corrections routinely regenerate historical rows and their timestamps. This package detects and quantifies divergence; it does **not** judge whether any batch load, edit, or divergence was legitimate, authorized, or improper. That legitimacy question is Tier 3 and is refused.

---

# Bismillah ir-Rahman ir-Rahim
