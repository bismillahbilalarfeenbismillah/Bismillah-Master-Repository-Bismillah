# Bismillah ir-Rahman ir-Rahim

# R0485 -- reproduce_paper3.py — reproduce_paper3.py -- Provenance Integrity for Public Open Data (Bayyinah Paper 3).

**Chronological Index:** 38 of 995  
**Date:** 2024  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** reproduce_paper3.py  
**Source Format:** py  
**SHA-256:** `188e21a072c1ccb9663a6375c1e4d03f07ab327e6d08d45fe7f2cb0a6e3b6689`  

---

## R0485 · reproduce_paper3.py — reproduce_paper3.py -- Provenance Integrity for Public Open Data (Bayyinah Paper 3).

- section: VI. Applied Audits & Public-Data Studies
- source_file: reproduce_paper3.py
- source_format: py
- text_sha256: 188e21a072c1ccb9663a6375c1e4d03f07ab327e6d08d45fe7f2cb0a6e3b6689

#!/usr/bin/env python3
"""
reproduce_paper3.py -- Provenance Integrity for Public Open Data (Bayyinah Paper 3).

Reproduces four provenance-integrity checks against the frozen capture:
  1. Provenance classification and community-vs-official divergence.
  2. Snapshot integrity (SHA-256 of the frozen capture vs MANIFEST).
  3. Declared-vs-actual freshness (row-level :created_at postdating the reporting period).
  4. Schema divergence (served field inventory per dataset).

Modes:
  (default)     verify hash and reproduce all four checks from the frozen capture, offline.
  --live        re-pull the live data.ny.gov endpoints and compare to the frozen capture;
                nonzero exit on any drift.
  --selftest    perturb every captured value and confirm the comparator detects each;
                nonzero exit if any perturbation is missed.

Standard library only. The checks detect and quantify divergence; they do NOT judge whether
any republish, edit, or divergence was legitimate, authorized, or improper (Tier 3, refused).
"""
import json, hashlib, sys, os, datetime, urllib.request, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
SNAP = os.path.join(HERE, "snapshot", "provenance_capture.json")
MANIFEST = os.path.join(HERE, "snapshot", "MANIFEST.json")
PORTAL = "data.ny.gov"
FYS = ["2022", "2023", "2024"]


# ---------- io ----------
def load_capture():
    return json.load(open(SNAP))

def verify_hash():
    raw = open(SNAP, "rb").read()
    got = hashlib.sha256(raw).hexdigest()
    want = json.load(open(MANIFEST))["sha256"]
    return got == want, got, want

def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "bayyinah-p3"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())

def _soda(slug, params):
    return _get("https://%s/resource/%s.json?%s" % (PORTAL, slug,
                urllib.parse.urlencode(params, safe=":$,()=")))


# ---------- live pull (mirrors how the capture was built) ----------
def live_capture(frozen):
    out = {"datasets": {}}
    for slug, ds in frozen["datasets"].items():
        m = _get("https://%s/api/views/%s.json" % (PORTAL, slug))
        fields = sorted(c["fieldName"] for c in m.get("columns", []) if c.get("fieldName"))
        d = {"name": m.get("name"), "provenance": m.get("provenance"),
             "rows_updated_at_unix": m.get("rowsUpdatedAt"),
             "schema_field_count": len(fields), "schema_fields": fields,
             "fiscal_windows": {}}
        for fy in FYS:
            r = _soda(slug, {"$select": "count(*) as row_count, sum(contract_amount) as face_total, "
                             "min(:created_at) as ca_min, max(:created_at) as ca_max, "
                             "min(:updated_at) as ua_min, max(:updated_at) as ua_max",
                             "$where": "fiscal_year_end_date='%s-12-31T00:00:00.000'" % fy})[0]
            d["fiscal_windows"]["%s-12-31" % fy] = {
                "row_count": int(r["row_count"]), "face_total": round(float(r["face_total"]), 2),
                "created_at_min": r["ca_min"], "created_at_max": r["ca_max"],
                "updated_at_min": r["ua_min"], "updated_at_max": r["ua_max"]}
        out["datasets"][slug] = d
    return out


# ---------- flatten for comparison / perturbation ----------
CHECKED = ["provenance", "rows_updated_at_unix", "schema_field_count"]
WINDOW_KEYS = ["row_count", "face_total", "created_at_min", "created_at_max",
               "updated_at_min", "updated_at_max"]

def flatten(cap):
    flat = {}
    for slug, ds in cap["datasets"].items():
        for k in CHECKED:
            flat["%s/%s" % (slug, k)] = ds.get(k)
        for win, w in ds["fiscal_windows"].items():
            for k in WINDOW_KEYS:
                flat["%s/%s/%s" % (slug, win, k)] = w.get(k)
    return flat

def compare(frozen, other):
    fa, ob = flatten(frozen), flatten(other)
    drift = []
    for key in sorted(set(fa) | set(ob)):
        if fa.get(key) != ob.get(key):
            drift.append((key, fa.get(key), ob.get(key)))
    return drift


# ---------- the four checks (offline, from the frozen capture) ----------
def days_after_close(ts, fy_close):
    d = datetime.date.fromisoformat(ts[:10])
    c = datetime.date.fromisoformat(fy_close)
    return (d - c).days

def report_checks(cap):
    ds = cap["datasets"]
    print("[integrity] capture retrieved_utc:", cap.get("retrieved_utc"))

    print("\nCheck 1 -- Provenance classification and divergence")
    for slug, d in ds.items():
        print("  %-11s provenance=%-9s (%s)" % (slug, d["provenance"], d["name"]))
    g, t = ds.get("gpsc-qqsz"), ds.get("twsw-2mqa")
    if g and t:
        for win in sorted(g["fiscal_windows"]):
            gw, tw = g["fiscal_windows"][win], t["fiscal_windows"].get(win)
            if not tw:
                continue
            rdiff = gw["row_count"] - tw["row_count"]
            fdiff = round(gw["face_total"] - tw["face_total"], 2)
            cd = abs(rdiff) / max(gw["row_count"], 1) * 100
            fd = abs(fdiff) / max(gw["face_total"], 1e-9) * 100
            tag = "identical" if rdiff == 0 and fdiff == 0 else "DIVERGENT"
            print("  %s community-vs-official: rows d=%+d (%.4f%%), face d=$%+.2f (%.7f%%)  [%s]"
                  % (win, rdiff, cd, fdiff, fd, tag))
        print("  [note] even at identical row count, FY2022 diverges by $0.75 in summed face value -- "
              "a value-level difference a coarse (billion-rounded) view misses.")

    print("\nCheck 2 -- Snapshot integrity")
    ok, got, want = verify_hash()
    print("  SHA-256 %s (%s)" % ("OK" if ok else "MISMATCH", got[:16] + "..."))

    print("\nCheck 3 -- Declared-vs-actual freshness (row :created_at vs reporting-period close)")
    for slug, d in ds.items():
        for win, w in sorted(d["fiscal_windows"].items()):
            lag = days_after_close(w["created_at_min"], win)
            uniform = w["created_at_min"] == w["created_at_max"]
            flag = "POST-CLOSE-BATCH" if (uniform and lag > 0) else ("post-close" if lag > 0 else "in-period")
            print("  %-11s %s created %s, %d days after close  [%s]"
                  % (slug, win, w["created_at_min"][:10], lag, flag))

    print("\nCheck 4 -- Schema divergence (served field inventory)")
    counts = {slug: d["schema_field_count"] for slug, d in ds.items()}
    print("  field counts:", counts)
    if g and t:
        only_t = sorted(set(t["schema_fields"]) - set(g["schema_fields"]))
        only_g = sorted(set(g["schema_fields"]) - set(t["schema_fields"]))
        print("  fields in official not in community view: %d" % len(only_t))
        print("  fields in community view not in official: %d" % len(only_g))
    print("\n[note] POST-CLOSE-BATCH = uniform :created_at postdating the period close (one batch load);\n"
          "       a single pull does not distinguish a republish from a first-time bulk load.")
    print("[note] Divergences and batch loads are substrate facts. This tool does not judge "
          "whether any was legitimate, authorized, or improper (Tier 3, refused).")


# ---------- selftest ----------
def selftest(cap):
    flat = flatten(cap)
    import copy
    misses = 0; n = 0
    for key in flat:
        n += 1
        pert = copy.deepcopy(cap)
        slug = key.split("/")[0]
        parts = key.split("/")
        val = flat[key]
        newval = (val + "_X") if isinstance(val, str) else ((val or 0) + 1)
        if len(parts) == 2:
            pert["datasets"][slug][parts[1]] = newval
        else:
            pert["datasets"][slug]["fiscal_windows"][parts[1]][parts[2]] = newval
        if not compare(cap, pert):
            misses += 1
            print("  [selftest] MISS on", key)
    print("[selftest] perturbed %d captured values; comparator missed %d" % (n, misses))
    return misses == 0


def main():
    cap = load_capture()
    ok, got, want = verify_hash()
    if not ok:
        print("ABORT: snapshot hash mismatch\n  got  %s\n  want %s" % (got, want))
        sys.exit(3)

    if "--selftest" in sys.argv:
        print("[selftest] perturbing each captured value to confirm the comparator detects it...")
        sys.exit(0 if selftest(cap) else 2)

    if "--live" in sys.argv:
        print("[live] re-pulling %s and comparing to the frozen capture..." % PORTAL)
        live = live_capture(cap)
        drift = compare(cap, live)
        if not drift:
            print("[live] no drift on provenance, schema, counts, totals, or row timestamps")
            report_checks(cap)
            sys.exit(0)
        print("[live] DRIFT detected on %d value(s):" % len(drift))
        for key, frozen_v, live_v in drift:
            print("  %s: frozen=%r live=%r" % (key, frozen_v, live_v))
        sys.exit(2)

    report_checks(cap)


if __name__ == "__main__":
    main()

---

# Bismillah ir-Rahman ir-Rahim
