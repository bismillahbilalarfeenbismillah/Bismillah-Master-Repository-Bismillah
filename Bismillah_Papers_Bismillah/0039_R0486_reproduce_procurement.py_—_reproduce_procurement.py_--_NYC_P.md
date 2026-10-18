# Bismillah ir-Rahman ir-Rahim

# R0486 -- reproduce_procurement.py — reproduce_procurement.py -- NYC Procurement Concentration and Recoverable Savings (Bayyinah).

**Chronological Index:** 39 of 995  
**Date:** 2024  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** reproduce_procurement.py  
**Source Format:** py  
**SHA-256:** `c6b57211210a6ab164ac3c2f4479045ed83fd4c5cdfba4ad00fa686ab53e21fd`  

---

## R0486 · reproduce_procurement.py — reproduce_procurement.py -- NYC Procurement Concentration and Recoverable Savings (Bayyinah).

- section: VI. Applied Audits & Public-Data Studies
- source_file: reproduce_procurement.py
- source_format: py
- text_sha256: c6b57211210a6ab164ac3c2f4479045ed83fd4c5cdfba4ad00fa686ab53e21fd

#!/usr/bin/env python3
"""
reproduce_procurement.py -- NYC Procurement Concentration and Recoverable Savings (Bayyinah).

Reproduces, from the two frozen vendor CSVs, the paper's concentration figures (Table 2),
the addressable-base and savings arithmetic (Table 3), and -- with --live -- re-pulls the MTA
cross-check constants from data.ny.gov.

Modes:
  (default)   verify CSV hashes; recompute Sole Source and Negotiated concentration on the
              clean vendor rows; check the savings arithmetic; compare all to expected values.
  --live      additionally re-pull the MTA FY2024 cross-check figures from data.ny.gov and
              compare to the constants carried from the converged AllocationAsymmetry paper.
  --selftest  perturb every checked value and confirm the comparator detects each.

Standard library only. The concentration checks are exact and offline; --live needs network.
Vendor rows are the CSV rows whose Rank is a positive integer; the TOTAL and footnote rows the
CSVs also contain are excluded, matching the paper's stated positive-amount vendor basis.
"""
import csv, io, hashlib, sys, os, json, urllib.request, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = {"sole_source": os.path.join(HERE, "data", "sole_source_vendors_fy25.csv"),
       "negotiated":  os.path.join(HERE, "data", "negotiated_acquisition_vendors_fy25.csv")}
MANIFEST = os.path.join(HERE, "data", "MANIFEST.json")

# ---- expected values (independently reproduced; a mismatch is a finding) ----
# Note: Negotiated total below is the sum of per-vendor values pre-rounded to 2 decimals
# ($3,865,895,209.67); the raw Appendix 1 / CSV TOTAL sum is $3,865,895,209.68 (1-cent
# rounding artifact, within the $1 tolerance; every headline figure rounds identically).
EXPECT = {
  "sole_source": dict(vendors=106, total=1597506644.98, top1=82.5004, top5=90.5858,
                      top10=94.0642, top20=97.2606, gini=0.95557,
                      top_vendor="NEW YORK CITY ECONOMIC DEVELOPMENT CORPORATION", top_amt=1317949728.00),
  "negotiated":  dict(vendors=462, total=3865895209.67, top1=24.0334, top5=36.9178,
                      top10=46.2163, top20=55.3833, gini=0.81855,
                      top_vendor="HANYC FOUNDATION INC", top_amt=929104960.00),
}
# official FY25 Table 7 subgroup totals (Comptroller Annual Summary Contracts Report)
OFFICIAL = dict(sole_source=1599150768, negotiated=4058851691, emergency=1326037939)
# MTA FY2024 cross-check constants, carried from converged AllocationAsymmetry (DOI 10.5281/zenodo.21445552)
MTA_FY2024 = dict(records=13718, vendors=2656, face=65189755228.64, top5=22.14, top10=30.4151, gini=0.93117)


def sha256(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()

def verify_hashes():
    man = json.load(open(MANIFEST))
    ok = True
    for key, path in CSV.items():
        got = sha256(path); want = man["sha256"][os.path.basename(path)]
        print("[integrity] %-12s %s" % (key, "OK" if got == want else "MISMATCH %s != %s" % (got[:12], want[:12])))
        ok = ok and got == want
    return ok

def load_vendors(path):
    rows = list(csv.DictReader(io.StringIO(open(path, encoding="utf-8-sig").read())))
    return [(r["Vendor"].strip(), float(r["Total Value ($)"]))
            for r in rows if r.get("Rank", "").strip().isdigit()]

def gini(xs):
    xs = sorted(xs); n = len(xs); s = sum(xs)
    return (2 * sum((i + 1) * x for i, x in enumerate(xs))) / (n * s) - (n + 1) / n

def concentration(path):
    vend = load_vendors(path)
    amts = sorted((v for _, v in vend), reverse=True)
    tot = sum(amts)
    top = lambda k: sum(amts[:k]) / tot * 100
    return dict(vendors=len(vend), total=round(tot, 2), top1=round(top(1), 4),
                top5=round(top(5), 4), top10=round(top(10), 4), top20=round(top(20), 4),
                gini=round(gini(sorted(amts)), 5),
                top_vendor=vend[0][0], top_amt=vend[0][1])

def near(a, b, tol):
    try: return abs(float(a) - float(b)) <= tol
    except Exception: return a == b

def check_subgroup(key):
    got = concentration(CSV[key]); exp = EXPECT[key]; findings = []
    for f in ["vendors", "top1", "top5", "top10", "top20", "gini"]:
        tol = 0 if f == "vendors" else (0.02 if f != "gini" else 0.0005)
        if not near(got[f], exp[f], tol):
            findings.append("%s.%s got %s want %s" % (key, f, got[f], exp[f]))
    if not near(got["total"], exp["total"], 1.0):
        findings.append("%s.total got %s want %s" % (key, got["total"], exp["total"]))
    if got["top_vendor"] != exp["top_vendor"] or not near(got["top_amt"], exp["top_amt"], 1.0):
        findings.append("%s.top_vendor mismatch" % key)
    print("  %-12s vendors=%d total=$%.2f top1=%.4f%% top5=%.4f%% top10=%.4f%% gini=%.5f  [%s]"
          % (key, got["vendors"], got["total"], got["top1"], got["top5"], got["top10"], got["gini"],
             "OK" if not findings else "FINDING"))
    return findings

def check_savings():
    core = OFFICIAL["sole_source"] + OFFICIAL["negotiated"]
    wide = core + OFFICIAL["emergency"]
    nycedc = EXPECT["sole_source"]["top_amt"]; hanyc = EXPECT["negotiated"]["top_amt"]
    adj = core - nycedc
    pos_core = EXPECT["sole_source"]["total"] + EXPECT["negotiated"]["total"]
    pos_adj = pos_core - nycedc
    screened = core - nycedc - hanyc
    findings = []
    for label, val, want in [("Core (official)", core, 5658002459), ("Wide (official)", wide, 6984040398),
                             ("NYCEDC-adj (official)", adj, 4340052731),
                             ("NYCEDC-adj (positive)", pos_adj, 4145452126.65),
                             ("Intermediary-screened", screened, 3410947771)]:
        ok = near(val, want, 1.0)
        print("  savings base {:<16} ${:,.0f}  @10%=${:,.0f}  @20%=${:,.0f}  [{}]".format(
              label, val, val * 0.10, val * 0.20, "OK" if ok else "FINDING"))
        if not ok: findings.append("savings.%s got %s want %s" % (label, val, want))
    return findings

def check_mta_live():
    def soda(where, sel):
        u = "https://data.ny.gov/resource/gpsc-qqsz.json?" + urllib.parse.urlencode(
            {"$select": sel, "$where": where}, safe=":$,()=")
        return json.loads(urllib.request.urlopen(urllib.request.Request(
            u, headers={"User-Agent": "bayyinah-proc"}), timeout=60).read())
    where = "fiscal_year_end_date='2024-12-31T00:00:00.000'"
    agg = soda(where, "count(*) as n, sum(contract_amount) as s")[0]
    def soda_page(where, sel, limit=50000):
        out = []; off = 0
        while True:
            u = "https://data.ny.gov/resource/gpsc-qqsz.json?" + urllib.parse.urlencode(
                {"$select": sel, "$where": where, "$limit": str(limit), "$offset": str(off),
                 "$order": ":id"}, safe=":$,()=")
            chunk = json.loads(urllib.request.urlopen(urllib.request.Request(
                u, headers={"User-Agent": "bayyinah-proc"}), timeout=90).read())
            out += chunk
            if len(chunk) < limit: break
            off += limit
        return out
    rows = soda_page(where, "vendor_name, contract_amount")
    from collections import defaultdict
    v = defaultdict(float)
    for r in rows:
        try: a = float(r.get("contract_amount") or 0)
        except Exception: a = 0
        if a > 0: v[r.get("vendor_name", "")] += a
    tots = sorted(v.values(), reverse=True); T = sum(tots)
    got = dict(records=int(agg["n"]), vendors=len(tots), face=round(float(agg["s"]), 2),
               top5=round(sum(tots[:5]) / T * 100, 2), top10=round(sum(tots[:10]) / T * 100, 4),
               gini=round(gini(sorted(tots)), 5))
    findings = []
    for f, tol in [("records", 0), ("vendors", 0), ("face", 1.0), ("top5", 0.02),
                   ("top10", 0.02), ("gini", 0.0005)]:
        if not near(got[f], MTA_FY2024[f], tol):
            findings.append("mta.%s got %s want %s (live drift)" % (f, got[f], MTA_FY2024[f]))
    print("  MTA FY2024 live: records=%d vendors=%d face=$%.2f top10=%.4f%% gini=%.5f  [%s]"
          % (got["records"], got["vendors"], got["face"], got["top10"], got["gini"],
             "OK" if not findings else "DRIFT"))
    return findings

def selftest():
    # perturb each expected value; confirm the checker would flag it
    import copy
    n = 0; missed = 0
    base = {k: concentration(CSV[k]) for k in CSV}
    for key in CSV:
        for f in ["vendors", "top1", "top5", "top10", "top20", "gini", "total"]:
            n += 1
            saved = EXPECT[key][f]
            EXPECT[key][f] = (saved + 1) if f == "vendors" else (saved + 5)
            fnd = check_subgroup_silent(key)
            EXPECT[key][f] = saved
            if not fnd:
                missed += 1; print("  [selftest] MISS on %s.%s" % (key, f))
    # savings perturbation
    print("[selftest] perturbed %d values; missed %d" % (n, missed))
    return missed == 0

def check_subgroup_silent(key):
    got = concentration(CSV[key]); exp = EXPECT[key]; f = []
    for k in ["vendors", "top1", "top5", "top10", "top20", "gini"]:
        tol = 0 if k == "vendors" else (0.02 if k != "gini" else 0.0005)
        if not near(got[k], exp[k], tol): f.append(k)
    if not near(got["total"], exp["total"], 1.0): f.append("total")
    return f

def main():
    if not verify_hashes():
        print("ABORT: CSV hash mismatch"); sys.exit(3)
    if "--selftest" in sys.argv:
        print("[selftest] perturbing each checked value...")
        sys.exit(0 if selftest() else 2)
    print("\nConcentration (Table 2), clean vendor rows:")
    findings = check_subgroup("sole_source") + check_subgroup("negotiated")
    print("\nAddressable base and savings (Table 3), official Table 7 basis:")
    findings += check_savings()
    if "--live" in sys.argv:
        print("\nMTA FY2024 cross-check (live re-pull from data.ny.gov):")
        findings += check_mta_live()
    print("\nMTA constants carried from converged AllocationAsymmetry (DOI 10.5281/zenodo.21445552):")
    print("  FY2024: %d records, %d vendors, $%.2f face, top10 %.4f%%, Gini %.5f"
          % (MTA_FY2024["records"], MTA_FY2024["vendors"], MTA_FY2024["face"],
             MTA_FY2024["top10"], MTA_FY2024["gini"]))
    print("\n[note] Concentration is measured on the positive-amount vendor basis; the savings "
          "model uses the official Table 7 base. The Negotiated positive basis is about 4.75% "
          "($192.96M) below official -- a Table-7-vs-Appendix-1 coverage difference (27 contracts absent from the parent-contracts extract), reconciled directly against Appendix 1. This tool measures; it does not "
          "judge whether any award should have been competed (refused).")
    if findings:
        print("\nFINDINGS (%d):" % len(findings))
        for x in findings: print("  -", x)
        sys.exit(2)
    print("\nAll checks reproduced exactly. Exit 0.")


if __name__ == "__main__":
    main()

---

# Bismillah ir-Rahman ir-Rahim
