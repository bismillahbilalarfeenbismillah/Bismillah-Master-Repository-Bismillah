# Bismillah ir-Rahman ir-Rahim

# R0484 -- reproduce_paper2.py — Reproduce every figure in Bayyinah Allocation & Asymmetric-Measure Audits (Paper 2, v0.3).

**Chronological Index:** 37 of 995  
**Date:** 2024  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** reproduce_paper2.py  
**Source Format:** py  
**SHA-256:** `74fa6ef7b9dd32e57fe0707e44b5c4487e4a19a41873e583f55e02e8ddef9f84`  

---

## R0484 · reproduce_paper2.py — Reproduce every figure in Bayyinah Allocation & Asymmetric-Measure Audits (Paper 2, v0.3).

- section: VI. Applied Audits & Public-Data Studies
- source_file: reproduce_paper2.py
- source_format: py
- text_sha256: 74fa6ef7b9dd32e57fe0707e44b5c4487e4a19a41873e583f55e02e8ddef9f84

#!/usr/bin/env python3
"""
Reproduce every figure in Bayyinah Allocation & Asymmetric-Measure Audits (Paper 2, v0.3).

A single stats() object holds EVERY published statistic. It drives three modes:
  python3 reproduce_paper2.py           # offline report from the frozen snapshot (hash + field-inventory validated)
  python3 reproduce_paper2.py --live    # re-pull all 3 years live; compare EVERY statistic + schema + row count
  python3 reproduce_paper2.py --selftest# perturb each statistic and confirm the comparator detects it
Exit status is nonzero on any integrity failure, any live drift beyond tolerance, or any missed perturbation.
Source: NY State Open Data, community view gpsc-qqsz (first-party: twsw-2mqa).
"""
import json, hashlib, sys, os, copy
from collections import defaultdict
HERE=os.path.dirname(os.path.abspath(__file__))
SNAP=os.path.join(HERE,"snapshot","gpsc-qqsz_FY2022-2024.json")
MAN =os.path.join(HERE,"snapshot","MANIFEST.json")
FYS=('2022','2023','2024')
PCT_TOL=0.05      # percentage-point tolerance
REL_TOL=1e-4      # relative tolerance for dollar totals

def _num(r,f):
    try: return float(r.get(f))
    except (TypeError,ValueError): return None
def _fy(rows,y): return [r for r in rows if r.get('fiscal_year_end_date','').startswith(f"{y}-12-31")]

def stats(rows):
    """Complete structured statistics object: every number the note publishes."""
    S={"total_rows":len(rows),
       "field_inventory":sorted({k for r in rows for k in r.keys() if not k.startswith(':')})}
    for y in FYS:
        ry=_fy(rows,y); n=len(ry)
        face=sum(_num(r,'contract_amount') or 0 for r in ry)
        ae  =sum(_num(r,'amount_expended_for_fiscal_year') or 0 for r in ry)
        S[y]={"n":n,"face_total":face,"ae_total":ae,
              "missing":sum(1 for r in ry if r.get('contract_amount') in (None,'')),
              "zero":sum(1 for r in ry if _num(r,'contract_amount')==0.0),
              "mwbe_count_pct":sum(1 for r in ry if r.get('vendor_is_a_mwbe')=='Y')/n*100,
              "mwbe_face_pct":sum(_num(r,'contract_amount') or 0 for r in ry if r.get('vendor_is_a_mwbe')=='Y')/face*100,
              "mwbe_ae_pct":sum(_num(r,'amount_expended_for_fiscal_year') or 0 for r in ry if r.get('vendor_is_a_mwbe')=='Y')/ae*100}
    # FY2024 detail
    r24=_fy(rows,'2024')
    pf=defaultdict(float); pae=defaultdict(float); tf=0.0; tae=0.0
    for r in r24:
        a=_num(r,'contract_amount') or 0; e=_num(r,'amount_expended_for_fiscal_year') or 0
        pf[r.get('award_process')]+=a; pae[r.get('award_process')]+=e; tf+=a; tae+=e
    S["proc_face_pct"]={k:pf[k]/tf*100 for k in pf}
    S["proc_ae_pct"]={k:pae[k]/tae*100 for k in pae}
    def conc(field):
        byv=defaultdict(float)
        for r in r24:
            v=_num(r,field)
            if v: byv[r.get('vendor_name')]+=v
        vals=sorted(byv.values(),reverse=True); tot=sum(vals)
        x=sorted(vals);N=len(x);cum=sum(i*v for i,v in enumerate(x,1))
        gini=(2*cum)/(N*sum(x))-(N+1)/N
        return {"vendors":len(byv),"top5":sum(vals[:5])/tot*100,"top10":sum(vals[:10])/tot*100,
                "top20":sum(vals[:20])/tot*100,"gini":gini}
    S["conc_face"]=conc('contract_amount'); S["conc_ae"]=conc('amount_expended_for_fiscal_year')
    def yr(r):
        d=r.get('award_date'); return int(d[:4]) if d else None
    S["pre2024_face_share"]=sum(_num(r,'contract_amount') or 0 for r in r24 if (yr(r) or 9999)<2024)/tf*100
    return S

def _flatten(S,prefix=""):
    out={}
    for k,v in S.items():
        key=f"{prefix}{k}"
        if isinstance(v,dict): out.update(_flatten(v,key+"."))
        elif isinstance(v,(int,float)): out[key]=float(v)
        elif isinstance(v,list): out[key]=("|".join(map(str,v)))
    return out

def compare(a,b,label_a="frozen",label_b="live"):
    """Compare every numeric and schema field. Returns list of mismatches."""
    fa,fb=_flatten(a),_flatten(b); miss=[]
    keys=set(fa)|set(fb)
    for k in sorted(keys):
        if k not in fa or k not in fb: miss.append(f"{k}: present in only one ({label_a if k in fa else label_b})"); continue
        va,vb=fa[k],fb[k]
        if isinstance(va,str) or isinstance(vb,str):
            if va!=vb: miss.append(f"{k}: {label_a}={va} vs {label_b}={vb}")
        else:
            tol = PCT_TOL if ("pct" in k or "top" in k or "gini" in k or "share" in k) else max(abs(va)*REL_TOL,0.5)
            if abs(va-vb)>tol: miss.append(f"{k}: {label_a}={va:.4f} vs {label_b}={vb:.4f} (tol {tol:g})")
    return miss

def load_verify():
    raw=open(SNAP).read(); man=json.load(open(MAN))
    if hashlib.sha256(raw.encode()).hexdigest()!=man["sha256_of_canonical_json"]:
        sys.exit("ABORT: snapshot hash mismatch.")
    rows=json.loads(raw)
    if sorted({k for r in rows for k in r.keys() if not k.startswith(':')})!=sorted(man["fields"]):
        sys.exit("ABORT: manifest field inventory != actual fields.")
    print(f"[integrity] hash OK, field inventory OK ({len(man['fields'])} fields), {man['row_count']} rows")
    return rows

def report(S):
    print("\n[4.2] MWBE count vs dollar share (both estimands), by vintage:")
    for y in FYS:
        d=S[y]
        print(f"  FY{y}: count {d['mwbe_count_pct']:4.1f}%  face {d['mwbe_face_pct']:4.2f}% (x{d['mwbe_count_pct']/d['mwbe_face_pct']:.1f})"
              f"  exp {d['mwbe_ae_pct']:4.2f}% (x{d['mwbe_count_pct']/d['mwbe_ae_pct']:.1f})  "
              f"[face ${d['face_total']/1e9:.1f}B exp ${d['ae_total']/1e9:.1f}B miss {d['missing']} zero {d['zero']}]")
    print("[4.1] FY2024 process (face | exp):")
    for k in sorted(S['proc_face_pct'],key=lambda k:-S['proc_face_pct'][k]-S['proc_ae_pct'][k]):
        print(f"  {k[:38]:40} face {S['proc_face_pct'][k]:5.2f}%  exp {S['proc_ae_pct'][k]:5.2f}%")
    cf,ce=S['conc_face'],S['conc_ae']
    print(f"[4.3] face conc  top5 {cf['top5']:.1f}% top10 {cf['top10']:.1f}% top20 {cf['top20']:.1f}% gini {cf['gini']:.3f} (vendors {cf['vendors']})")
    print(f"[4.3] exp  conc  top5 {ce['top5']:.1f}% top10 {ce['top10']:.1f}% top20 {ce['top20']:.1f}% gini {ce['gini']:.3f}")
    print(f"[4.0] pre-2024-award face share {S['pre2024_face_share']:.1f}% (stock, not FY2024 flow)")

def live_compare(frozen_stats):
    import urllib.request
    print("\n[live] pulling all three years and comparing EVERY statistic + schema + row count...")
    base="https://data.ny.gov/resource/gpsc-qqsz.json"; live=[]
    for y in FYS:
        off=0
        while True:
            u=f"{base}?$where=fiscal_year_end_date='{y}-12-31T00:00:00.000'&$limit=20000&$offset={off}"
            b=json.load(urllib.request.urlopen(u,timeout=60))
            if not b: break
            live+=b; off+=len(b)
            if len(b)<20000: break
    miss=compare(frozen_stats,stats(live))
    if miss:
        print(f"[live] DRIFT on {len(miss)} field(s):"); [print("   "+m) for m in miss]
        return 2
    print("[live] no drift on any published statistic, schema, or row count"); return 0

def selftest(S):
    print("\n[selftest] perturbing each statistic to confirm the comparator detects it...")
    fails=[]
    flat=_flatten(S)
    numeric=[k for k,v in flat.items() if isinstance(v,float)]
    for k in numeric:
        pert=copy.deepcopy(S)
        # navigate to the leaf and bump it by 10x tolerance
        parts=k.split("."); ref=pert
        for p in parts[:-1]: ref=ref[p]
        ref[parts[-1]]=ref[parts[-1]]+ (1.0 if ("pct" in k or "top" in k or "gini" in k or "share" in k) else max(abs(flat[k])*1e-3,1000))
        if not compare(S,pert,"orig","perturbed"):
            fails.append(k)
    # schema perturbation
    pert=copy.deepcopy(S); pert["field_inventory"]=pert["field_inventory"][:-1]
    if not compare(S,pert): fails.append("field_inventory")
    if fails:
        print(f"[selftest] FAIL: comparator missed {len(fails)} perturbation(s): {fails}"); return 1
    print(f"[selftest] PASS: comparator detected all {len(numeric)+1} deliberate perturbations"); return 0

if __name__=="__main__":
    rows=load_verify(); S=stats(rows); report(S)
    code=0
    if "--selftest" in sys.argv: code=max(code,selftest(S))
    if "--live" in sys.argv: code=max(code,live_compare(S))
    sys.exit(code)

---

# Bismillah ir-Rahman ir-Rahim
