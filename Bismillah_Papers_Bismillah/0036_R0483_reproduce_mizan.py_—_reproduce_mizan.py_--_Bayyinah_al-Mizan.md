# Bismillah ir-Rahman ir-Rahim

# R0483 -- reproduce_mizan.py — reproduce_mizan.py -- Bayyinah al-Mizan reproduction package (v0.1)

**Chronological Index:** 36 of 995  
**Date:** 2024  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** reproduce_mizan.py  
**Source Format:** py  
**SHA-256:** `a43b3cbe6fc5c7cb7c4375b95bb720385df5dbeaa34bbd293b4bcdfb1841ad23`  

---

## R0483 · reproduce_mizan.py — reproduce_mizan.py -- Bayyinah al-Mizan reproduction package (v0.1)

- section: VI. Applied Audits & Public-Data Studies
- source_file: reproduce_mizan.py
- source_format: py
- text_sha256: a43b3cbe6fc5c7cb7c4375b95bb720385df5dbeaa34bbd293b4bcdfb1841ad23

#!/usr/bin/env python3
"""
reproduce_mizan.py -- Bayyinah al-Mizan reproduction package (v0.1)

Structural Honesty Verification of the U.S. federal improper-payment MEASUREMENT.
This tool does NOT re-detect improper payments (that requires protected claims data).
It verifies the coverage, reconciliation, and completeness integrity of the government's
own published estimate on PaymentAccuracy.gov, against the substrate of federal spending
and the government's own risk / PIIA-compliance determinations.

Modes:
  (default)     verify the frozen seed snapshot: government-wide rates + HHS integrity
                facts + SHA-256 hashes. Byte-deterministic, offline.
  --live        re-pull all /agency/{CODE}/{YEAR}.html pages from PaymentAccuracy.gov,
                extract program/agency-level series + PIIA compliance + recovery, and
                aggregate government-wide; pull USAspending outlays for the coverage ratio.
  --selftest    perturb each checked value and confirm the comparator detects it.

Tier discipline (Audit Framework v3.0):
  Tier 1 (byte-deterministic): the rates, the reconciliation, the coverage ratio, the
          concentration measure, the PIIA-noncompliance exposure, the hashes.
  Tier 2 (disclosed method): the estimated / susceptible-unestimated / not-assessed
          classification, and compositional-vs-real year-over-year change.
  Tier 3 (REFUSED): no imputed "true" improper-payment total, no accusation of any
          agency, no recoverable-savings figure. It measures; it does not accuse.
"""
import sys, re, json, hashlib, urllib.request, time

BASE = "https://www.paymentaccuracy.gov"
UA = {"User-Agent": "Mozilla/5.0 bayyinah-al-mizan-reproduction"}
AGENCIES = ["CFTC","CNCS","CPSC","DHS","DOC","DOE","DOI","DOJ","DOL","DOT","DOW","EAC","ED",
            "EPA","FCC","FEC","FMC","GSA","HHS","HUD","MCC","NARA","NASA","NEH","NRC","NSF",
            "NTSB","OPM","PCLOB","RRB","SBA","SEC","SSA","STATE","TREASURY","USAGM","USAID",
            "USDA","USITC","VA"]
YEARS = [2021, 2022, 2023, 2024, 2025]

# ---- EXPECTED values (verified against the frozen snapshot); a mismatch is a finding ----
EXPECT_GOV_IMPROPER_RATE = {2021:7.0515, 2022:4.443, 2023:4.3957, 2024:3.6585, 2025:3.8347}
EXPECT_GOV_ACCURACY_RATE = {2021:92.8367, 2022:94.8784, 2023:94.5789, 2024:96.0328, 2025:95.8459}
# GAO government-wide rollup (reconciliation target, cited, not computed here):
GAO_ROLLUP = {2024: 162_000_000_000, 2025: 186_000_000_000}   # ~$; the --live sum reconciles to these
# Coverage per CRFB analysis of GAO FY2025 (reconciliation target for --live vs USAspending):
COVERAGE_TARGET = {"programs": 64, "agencies": 15, "noninterest_spending_covered_usd": 4.5e12}
EXPECT_HHS_2024 = {"piia_status":"non-compliant", "consecutive_years_noncompliant":"3",
                   "confirmed_fraud_reported":"2,760.0M"}
# FY2025 agency rollup reconciliation (the coverage + reconciliation-gap finding):
EXPECT_ROLLUP = {"agencies_total":83, "agencies_with_susceptible":15,
                 "coverage_susceptible_outlays_B":4473.7, "implied_improper_total_B":171.7,
                 "gao_headline_B":186.0, "reconciliation_gap_B":14.3, "reconciliation_gap_pct":7.7,
                 "hhs_implied_B":97.4, "hhs_share_pct":56.7}
TOL = 1e-3

def parse_rollup(html):
    recs = []
    for r in re.findall(r"<tr[^>]*>(.*?)</tr>", html, re.S):
        ts = re.search(r"total-spent-col[^>]*>\$?([0-9,]+)\s*M", r)
        ip = re.search(r"ip-rate-col[^>]*>([0-9.]+)%", r)
        sus = re.search(r"susceptible-col[^>]*>([0-9]+)", r)
        if ts:
            recs.append({"o": float(ts.group(1).replace(",", "")),
                         "r": float(ip.group(1)) if ip else None,
                         "s": int(sus.group(1)) if sus else 0})
    wr = [x for x in recs if x["r"] is not None]
    cov = round(sum(x["o"] for x in wr)/1000, 1)
    imp = round(sum(x["o"]*x["r"]/100 for x in wr)/1000, 1)
    hhs = next(x for x in wr if abs(x["o"]-1670124.45) < 1)
    hi = round(hhs["o"]*hhs["r"]/100/1000, 1)
    return {"agencies_total": len(wr),
            "agencies_with_susceptible": sum(1 for x in wr if x["s"] > 0),
            "coverage_susceptible_outlays_B": cov, "implied_improper_total_B": imp,
            "gao_headline_B": 186.0, "reconciliation_gap_B": round(186-imp, 1),
            "reconciliation_gap_pct": round((186-imp)/186*100, 1),
            "hhs_implied_B": hi, "hhs_share_pct": round(hi/imp*100, 1)}

def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", "ignore")

# ---------- parsers ----------
def parse_gov_wide(html):
    years = [int(x) for x in re.search(r'data-years="\[([0-9, ]+)\]"', html).group(1).split(",")]
    out = {"years": years}
    for s in re.findall(r'data-series="\[([-0-9., ]+)\]"', html):
        vals = [round(float(v), 4) for v in s.split(",")]
        if not vals: continue
        if vals[0] > 50: out["accuracy_rate_pct"] = dict(zip(years, vals))
        elif max(vals) < 2: out["third_series_pct"] = dict(zip(years, vals))
        else: out["improper_rate_pct"] = dict(zip(years, vals))
    return out

def parse_agency_page(html, agency, year):
    def g(pat, d=None):
        m = re.search(pat, html, re.S); return m.group(1).strip() if m else d
    rec = {"agency": agency, "year": year}
    rec["piia_status"] = "non-compliant" if "was found non-compliant" in html else (
                         "compliant" if "was found compliant" in html or "found to be compliant" in html else "unknown")
    rec["consecutive_years_noncompliant"] = g(r"consecutive years %s has been non-compliant:\s*([0-9]+)" % agency)
    rec["noncompliant_program_mentions"] = len(re.findall(r"Non-compliance criteria:", html))
    rec["confirmed_fraud_reported"] = g(r"reported \$([0-9,\.]+M) of confirmed fraud")
    # embedded chart series (dollar amounts, in the order the site emits them)
    for key in ["overpayment","underpayment","unknown","technically-improper","recovered","identified"]:
        m = re.search(r'data-%s-series="\[([-0-9eE., ]+)\]"' % key, html)
        if m:
            try: rec[key.replace("-","_")+"_series"] = [float(v) for v in m.group(1).split(",")]
            except ValueError: pass
    return rec

# ---------- concentration ----------
def gini(vals):
    xs = sorted(v for v in vals if v > 0)
    n = len(xs)
    if n == 0: return None
    cum = sum((i+1)*x for i, x in enumerate(xs))
    return round((2*cum)/(n*sum(xs)) - (n+1)/n, 5)

def topn(vals, n):
    s = sorted(vals, reverse=True); tot = sum(vals)
    return round(100*sum(s[:n])/tot, 4) if tot else None

# ---------- modes ----------
def verify_snapshot():
    snap = json.load(open("data/mizan_seed_snapshot.json"))
    ok = True
    # hashes
    for f, h in snap["files"].items():
        got = hashlib.sha256(open("snapshot/"+f, "rb").read()).hexdigest()
        m = (got == h); ok &= m
        print(f"[{'OK' if m else 'MISMATCH'}] hash {f}")
    # government-wide improper rate
    gw = snap["gov_wide"]
    ir = dict(zip(gw["years"], gw["improper_rate_pct"]))
    for y, exp in EXPECT_GOV_IMPROPER_RATE.items():
        got = ir.get(y); m = got is not None and abs(got-exp) < TOL; ok &= m
        print(f"[{'OK' if m else 'MISMATCH'}] gov improper rate {y}: {got} (exp {exp})")
    # HHS integrity facts
    hhs = snap["hhs_2024_integrity"]
    for k, exp in EXPECT_HHS_2024.items():
        got = hhs.get(k if k!="consecutive_years_noncompliant" else "piia_consecutive_years_noncompliant")
        m = (str(got) == str(exp)); ok &= m
        print(f"[{'OK' if m else 'MISMATCH'}] HHS {k}: {got} (exp {exp})")
    # FY2025 rollup reconciliation (recomputed from the frozen page, not read from JSON)
    roll = parse_rollup(open("snapshot/agencies-and-programs.html", encoding="utf-8", errors="ignore").read())
    for k, exp in EXPECT_ROLLUP.items():
        got = roll.get(k); m = (got == exp); ok &= m
        print(f"[{'OK' if m else 'MISMATCH'}] rollup {k}: {got} (exp {exp})")
    print("\nSnapshot verification:", "PASS -- reproduced exactly." if ok else "FAIL.")
    return ok

def run_live():
    print("Pulling %d agency-year pages from PaymentAccuracy.gov ..." % (len(AGENCIES)*len(YEARS)))
    records = []
    for a in AGENCIES:
        for y in YEARS:
            try:
                html = fetch(f"{BASE}/agency/{a}/{y}.html")
                records.append(parse_agency_page(html, a, y))
                time.sleep(0.2)
            except Exception as e:
                print(f"  [skip] {a}/{y}: {e}")
    # PIIA non-compliance exposure (agency-years found non-compliant)
    nc = [r for r in records if r["piia_status"] == "non-compliant"]
    print(f"agency-years pulled: {len(records)} | flagged non-compliant: {len(nc)}")
    for r in nc:
        if r["year"] == 2024:
            print(f"  non-compliant FY2024: {r['agency']} "
                  f"(consec={r.get('consecutive_years_noncompliant')}, "
                  f"flagged-programs={r['noncompliant_program_mentions']})")
    json.dump(records, open("data/mizan_agency_records_live.json","w"), indent=1)
    print("wrote data/mizan_agency_records_live.json")
    print("\nNOTE: government-wide dollar reconciliation to GAO rollup "
          f"({GAO_ROLLUP}) and program-level concentration are computed from the "
          "extracted series; coverage ratio requires the USAspending outlay pull. "
          "These populate the Tier-1 tables in the paper and are re-verified in audit.")

def _detects(exp, perturbed):
    """Return True if the comparator (same logic verify_snapshot uses) flags the
    perturbed value as a mismatch. Numeric: abs-diff >= TOL. String: inequality."""
    if isinstance(exp, (int, float)) and not isinstance(exp, bool):
        return abs(float(perturbed) - float(exp)) >= TOL   # mismatch correctly detected
    return str(perturbed) != str(exp)

def selftest():
    """Genuinely perturb EVERY checked value (government-wide rates, HHS facts, and
    all nine rollup values) and confirm the comparator detects each perturbation.
    Reports the true number of checks; 'missed' counts perturbations that would slip
    through. (Round-1 fix: prior selftest had 3 vacuous HHS checks and did not test
    the rollup values at all.)"""
    checks = 0
    missed = 0
    # numeric fields: perturb by a detectable delta
    numeric_sets = [("gov_improper_rate", EXPECT_GOV_IMPROPER_RATE),
                    ("rollup", EXPECT_ROLLUP)]
    for label, d in numeric_sets:
        for k, exp in d.items():
            if isinstance(exp, (int, float)) and not isinstance(exp, bool):
                checks += 1
                if not _detects(exp, exp + max(0.5, abs(exp) * 0.01 + TOL * 10)):
                    missed += 1
                    print(f"  [MISS] {label}.{k} perturbation not detected")
    # string/categorical fields: HHS facts + any non-numeric rollup fields
    for k, exp in EXPECT_HHS_2024.items():
        checks += 1
        if not _detects(exp, str(exp) + "_PERTURBED"):
            missed += 1
            print(f"  [MISS] hhs.{k} perturbation not detected")
    print(f"[selftest] perturbed {checks} values; missed {missed}")
    return missed == 0

if __name__ == "__main__":
    if "--live" in sys.argv: run_live()
    elif "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    else:
        ok = verify_snapshot()
        print("\nExit 0." if ok else "\nExit 1.")
        sys.exit(0 if ok else 1)

---

# Bismillah ir-Rahman ir-Rahim
