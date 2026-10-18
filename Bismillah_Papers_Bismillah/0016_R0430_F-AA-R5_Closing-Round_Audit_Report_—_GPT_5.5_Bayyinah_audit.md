# Bismillah ir-Rahman ir-Rahim

# R0430 -- F-AA-R5 Closing-Round Audit Report — GPT 5.5 Bayyinah audit

**Chronological Index:** 16 of 995  
**Date:** 2024  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-AA-R5_gpt55.md  
**Source Format:** md  
**SHA-256:** `3e70d1fcd14d9e88e1dda16c6729bcaaa15804e5df0a268b0756f7c2c898a238`  

---

## R0430 · F-AA-R5 Closing-Round Audit Report — GPT 5.5 Bayyinah audit

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-AA-R5_gpt55.md
- source_format: md
- text_sha256: 3e70d1fcd14d9e88e1dda16c6729bcaaa15804e5df0a268b0756f7c2c898a238

# F-AA-R5 Closing-Round Audit Report — GPT 5.5 Bayyinah audit

## Identity, independence, and no-prior-state attestation

I identify this audit instance as **GPT 5.5, OpenAI lineage**, and I am a **qualifying non-Claude council member** for the requested closing-round F-AA-R5 audit. I ran this as a clean independent instance and did not use prior findings, memory, personalization, residual state, or any other model-council report files.

## Verdict

**Verdict: FINDINGS-BEARING NON-PASS, with mandatory reproduction-package execution incomplete.** A qualifying PASS is unavailable because the supplied audit packet did not contain `reproduce_paper2.py`, `snapshot/gpsc-qqsz_FY2022-2024.json`, or `MANIFEST.json`, so mandatory protocol steps 1-3 could not be executed against the supplied reproduction package. Independent live recomputation from New York Open Data did reproduce the principal numerical claims from `gpsc-qqsz`, and first-party reconciliation against `twsw-2mqa` also matched the disclosed dollar totals closely ([data.ny.gov gpsc aggregate query](https://data.ny.gov/resource/gpsc-qqsz.json?%24select=count(*)+as+row_count,+sum(contract_amount)+as+face_total,+sum(amount_expended_for_fiscal_year)+as+exp_total&fiscal_year_end_date=2024-12-31T00%3A00%3A00.000), [data.ny.gov twsw aggregate query](https://data.ny.gov/resource/twsw-2mqa.json?%24select=count(*)+as+row_count,+sum(contract_amount)+as+face_total,+sum(amount_expended_for_fiscal_year)+as+exp_total&fiscal_year_end_date=2024-12-31T00%3A00%3A00.000)).

## Materials reviewed and package-recovery work

I reviewed only the two supplied artifacts: `Bayyinah_AllocationAsymmetry_v0.4.md` and `Bayyinah_AllocationAsymmetry_AuditCompanion.md`. The two artifacts contain the public data URL `https://data.ny.gov/resource/gpsc-qqsz`, Zenodo references for other Bayyinah papers, and Socrata resource identifiers `gpsc-qqsz`, `twsw-2mqa`, `wcsa-vkhf`, `kizb-nxtu`, and `ehz8-ag3n`, but they do not contain a direct URL for the frozen snapshot, manifest, or reproduction script.

The referenced Zenodo records I checked contained other Bayyinah or companion-paper files, not the allocation-asymmetry reproduction package ([Zenodo API record 21436484](https://zenodo.org/api/records/21436484), [Zenodo API record 19894724](https://zenodo.org/api/records/19894724), [Zenodo API record 20069654](https://zenodo.org/api/records/20069654)). The Bayyinah homepage and public research index pointed to the Bayyinah Integrity Scanner repository and several Zenodo deposits but did not expose `reproduce_paper2.py`, `gpsc-qqsz_FY2022-2024.json`, or `MANIFEST.json` ([Bayyinah homepage](https://bayyinah.dev/), [Bayyinah research index](https://raw.githubusercontent.com/BayyinahEnterprise/Bayyinah-Integrity-Scanner/main/docs/research.md)).

### Artifact link extraction output

```text
FILE Bayyinah_AllocationAsymmetry_v0.4.md
URLS
https://zenodo.org/records/21436484
https://zenodo.org/records/19894724
https://zenodo.org/records/20069654
https://data.ny.gov/resource/gpsc-qqsz
RESOURCE_IDS ['ehz8-ag3n', 'gpsc-qqsz', 'kizb-nxtu', 'twsw-2mqa', 'wcsa-vkhf']
FILE Bayyinah_AllocationAsymmetry_AuditCompanion.md
URLS
RESOURCE_IDS ['ehz8-ag3n', 'gpsc-qqsz', 'kizb-nxtu', 'mn7w-32rv', 'twsw-2mqa', 'wcsa-vkhf']

```

### Zenodo and homepage recovery outputs

```text
ZENODO_API_URL https://zenodo.org/api/records/21436484
TITLE Bayyinah at-Taʿlīm: Structural Honesty Verification for Educational Fairness Systems, from Primary Schooling to Graduate Research
DOI 10.5281/zenodo.21436484
FILE_COUNT 1
FILE Bayyinah_at-Taleem_Paper_rc10.pdf 128287 https://zenodo.org/api/records/21436484/files/Bayyinah_at-Taleem_Paper_rc10.pdf/content
ZENODO_API_URL https://zenodo.org/api/records/19894724
TITLE Al-Mutaffifin: Structural Integrity Verification for Financial Governance Systems
DOI 10.5281/zenodo.19894724
FILE_COUNT 1
FILE Al_Mutaffifin_Thesis_v1_2.pdf 122174 https://zenodo.org/api/records/19894724/files/Al_Mutaffifin_Thesis_v1_2.pdf/content
ZENODO_API_URL https://zenodo.org/api/records/20069654
TITLE Bayyinah al-Munāsabāt: A Multi-Corpus, Multi-Pipeline Falsification Study of Canonical-versus-Chronological Long-Range Autocorrelation in the Uthmanic Quran
DOI 10.5281/zenodo.20069654
FILE_COUNT 4
FILE Bayyinah al Munasabat v1.0.pdf 252305 https://zenodo.org/api/records/20069654/files/Bayyinah%20al%20Munasabat%20v1.0.pdf/content
FILE 08_reconciliation.py 9319 https://zenodo.org/api/records/20069654/files/08_reconciliation.py/content
FILE 09_orthogonal_tanakh.py 10898 https://zenodo.org/api/records/20069654/files/09_orthogonal_tanakh.py/content
FILE 10_bonferroni_pvalues.py 3630 https://zenodo.org/api/records/20069654/files/10_bonferroni_pvalues.py/content

```

```text
URL https://bayyinah.dev/
HREF https://doi.org/10.5281/zenodo.19894724
HREF https://github.com/BayyinahEnterprise/Bayyinah-Integrity-Scanner/blob/main/docs/adversarial/csv_json_gauntlet/REPORT.md
HREF https://pypi.org/project/bayyinah/
HREF https://github.com/BayyinahEnterprise/Bayyinah-Integrity-Scanner
HREF https://doi.org/10.5281/zenodo.19700420
HREF https://doi.org/10.5281/zenodo.19776584
HREF https://doi.org/10.5281/zenodo.19776577
HREF https://doi.org/10.5281/zenodo.19776576
HREF https://doi.org/10.5281/zenodo.19744163
HREF https://doi.org/10.5281/zenodo.19746539
HREF https://doi.org/10.5281/zenodo.19745154
HREF https://doi.org/10.5281/zenodo.19802455
HREF https://doi.org/10.5281/zenodo.19875931
HREF https://doi.org/10.5281/zenodo.19894724
HREF https://doi.org/10.5281/zenodo.19746298
HREF https://github.com/BayyinahEnterprise/Bayyinah-Integrity-Scanner/blob/main/docs/research.md
HREF https://zenodo.org/search?q=Arfeen%20Bilal&l=list&p=1&s=10&sort=newest
HREF https://github.com/BayyinahEnterprise/Bayyinah-Integrity-Scanner
HREF https://github.com/BayyinahEnterprise/Bayyinah-Integrity-Scanner/blob/main/docs/adversarial/REPORT.md
HREF https://github.com/BayyinahEnterprise/Bayyinah-Integrity-Scanner/blob/main/docs/research.md
TOTAL_HREFS 51

```

## Execution matrix

| Step | Status | Evidence |
|---|---:|---|
| 1. `python3 reproduce_paper2.py` offline integrity/hash/field/stats | **INCOMPLETE** | Required script and frozen package were absent from the supplied packet; raw command output below. |
| 2. `python3 reproduce_paper2.py --selftest` | **INCOMPLETE** | Required script was absent; raw command output below. |
| 3. `python3 reproduce_paper2.py --live` | **INCOMPLETE** | Required script was absent; raw command output below. |
| 4. Wholly independent recompute | **COMPLETE** | Independent Python code fetched three live `gpsc-qqsz` vintages and recomputed totals, shares, process composition, concentration/Gini, pre-2024 share, missing/zero counts, and stable-field fingerprints ([gpsc 2022 query](https://data.ny.gov/resource/gpsc-qqsz.json?%24limit=50000&%24order=:id&fiscal_year_end_date=2022-12-31T00:00:00.000), [gpsc 2023 query](https://data.ny.gov/resource/gpsc-qqsz.json?%24limit=50000&%24order=:id&fiscal_year_end_date=2023-12-31T00:00:00.000), [gpsc 2024 query](https://data.ny.gov/resource/gpsc-qqsz.json?%24limit=50000&%24order=:id&fiscal_year_end_date=2024-12-31T00:00:00.000)). |
| 5. Live query gpsc-qqsz and first-party twsw-2mqa | **COMPLETE** | Direct SoQL aggregates returned 13,718 / $65.1898B for `gpsc-qqsz` and 13,648 / $65.1317B for `twsw-2mqa` ([gpsc aggregate query](https://data.ny.gov/resource/gpsc-qqsz.json?%24select=count(*)+as+row_count,+sum(contract_amount)+as+face_total,+sum(amount_expended_for_fiscal_year)+as+exp_total&fiscal_year_end_date=2024-12-31T00%3A00%3A00.000), [twsw aggregate query](https://data.ny.gov/resource/twsw-2mqa.json?%24select=count(*)+as+row_count,+sum(contract_amount)+as+face_total,+sum(amount_expended_for_fiscal_year)+as+exp_total&fiscal_year_end_date=2024-12-31T00%3A00%3A00.000)). |
| 6. Capital join | **COMPLETE** | Batch joined 120 sampled `wcsa-vkhf.project_number` values to `kizb-nxtu.project_number` and `ehz8-ag3n.proj_num`, and metadata showed no borough field in `wcsa-vkhf` ([wcsa metadata](https://data.ny.gov/api/views/wcsa-vkhf), [kizb resource](https://data.ny.gov/resource/kizb-nxtu.json), [ehz8 resource](https://data.ny.gov/resource/ehz8-ag3n.json)). |
| 7. Adversarial drift | **PARTIAL / independent only** | The supplied comparator was absent, but my independent comparator flagged a $1.00 non-MWBE face-value mutation with exit code 2; this does not satisfy the supplied-script comparator requirement. |

## Mandatory supplied-package execution attempt

```text
[required-package-name search returned no matching files]
```

```text
PWD
/home/user/workspace
REPO_LIST
Bayyinah_AllocationAsymmetry_AuditCompanion.md
Bayyinah_AllocationAsymmetry_v0.4.md
snapshot/gpsc-qqsz_FY2022-2024_live.json
test_fetch.py
RUN_OFFLINE
python3: can't open file '/home/user/workspace/fresh-instance-audit-packet/reproduce_paper2.py': [Errno 2] No such file or directory
RUN_SELFTEST
python3: can't open file '/home/user/workspace/fresh-instance-audit-packet/reproduce_paper2.py': [Errno 2] No such file or directory
RUN_LIVE
python3: can't open file '/home/user/workspace/fresh-instance-audit-packet/reproduce_paper2.py': [Errno 2] No such file or directory

```

## Independent recomputation — code

```python
#!/usr/bin/env python3
import json, urllib.parse, urllib.request, decimal, hashlib, statistics, itertools, os, sys
from collections import defaultdict, Counter
D=decimal.Decimal
BASE='https://data.ny.gov/resource'
YEARS=['2022-12-31T00:00:00.000','2023-12-31T00:00:00.000','2024-12-31T00:00:00.000']

def qurl(res, params):
    return f"{BASE}/{res}.json?" + urllib.parse.urlencode(params, safe="(),:' *")

def get_json(url):
    with urllib.request.urlopen(url, timeout=120) as r:
        return json.loads(r.read().decode('utf-8'))

def fetch_year(res, fy):
    url=qurl(res, {'$limit':50000,'$order':':id','fiscal_year_end_date':fy})
    rows=get_json(url)
    return url, rows

def dec(x):
    if x is None or x=='': return None
    try: return D(str(x))
    except Exception: return None

def sum_field(rows, field):
    s=D('0')
    for r in rows:
        v=dec(r.get(field))
        if v is not None: s += v
    return s

def fmt_money(d):
    return f"${d:,.2f}"

def pct(num, den):
    return (D(num) / D(den) * D(100)) if den else D(0)

def gini(vals):
    vals=[D(v) for v in vals]
    n=len(vals)
    if n==0: return D(0)
    vals=sorted(vals)
    total=sum(vals, D(0))
    if total==0: return D(0)
    weighted=sum((D(i+1)*v) for i,v in enumerate(vals))
    return (D(2)*weighted/(D(n)*total)) - (D(n+1)/D(n))

def stats_for(rows):
    n=len(rows)
    face=sum_field(rows,'contract_amount')
    exp=sum_field(rows,'amount_expended_for_fiscal_year')
    mw=[r for r in rows if str(r.get('vendor_is_a_mwbe','')).strip().upper()=='Y']
    mwn=len(mw); mwface=sum_field(mw,'contract_amount'); mwexp=sum_field(mw,'amount_expended_for_fiscal_year')
    missing=sum(1 for r in rows if 'contract_amount' not in r or r.get('contract_amount') in (None,''))
    zero=sum(1 for r in rows if dec(r.get('contract_amount')) == D(0))
    pre24=sum((dec(r.get('contract_amount')) or D(0)) for r in rows if (r.get('award_date') or '')[:4] < '2024')
    award_years=[(r.get('award_date') or '')[:4] for r in rows if r.get('award_date')]
    face_by_proc=defaultdict(D); exp_by_proc=defaultdict(D); count_by_proc=Counter()
    for r in rows:
        ap=r.get('award_process') or '(missing)'
        count_by_proc[ap]+=1
        face_by_proc[ap]+=dec(r.get('contract_amount')) or D(0)
        exp_by_proc[ap]+=dec(r.get('amount_expended_for_fiscal_year')) or D(0)
    vendor_face=defaultdict(D); vendor_exp=defaultdict(D)
    for r in rows:
        vendor=(r.get('vendor_name') or '(missing)').strip()
        vendor_face[vendor]+=dec(r.get('contract_amount')) or D(0)
        vendor_exp[vendor]+=dec(r.get('amount_expended_for_fiscal_year')) or D(0)
    vf_sorted=sorted(vendor_face.items(), key=lambda kv: kv[1], reverse=True)
    ve_sorted=sorted(vendor_exp.items(), key=lambda kv: kv[1], reverse=True)
    return {
        'rows':n, 'face_total':face, 'exp_total':exp,
        'mwbe_count':mwn, 'mwbe_count_share':pct(mwn,n), 'mwbe_face':mwface, 'mwbe_face_share':pct(mwface,face), 'mwbe_exp':mwexp, 'mwbe_exp_share':pct(mwexp,exp),
        'missing_contract_amount':missing, 'zero_contract_amount':zero,
        'award_date_min':min(award_years) if award_years else None, 'award_date_max':max(award_years) if award_years else None,
        'pre2024_face_share':pct(pre24,face),
        'face_by_proc':face_by_proc, 'exp_by_proc':exp_by_proc, 'count_by_proc':count_by_proc,
        'vendor_count':sum(1 for v in vendor_face.values() if v>0),
        'vendor_count_all':len(vendor_face),
        'face_top5_share':pct(sum(v for _,v in vf_sorted[:5]), face), 'face_top10_share':pct(sum(v for _,v in vf_sorted[:10]), face), 'face_top20_share':pct(sum(v for _,v in vf_sorted[:20]), face),
        'face_gini':gini([v for v in vendor_face.values() if v>0]),
        'exp_vendor_count':sum(1 for v in vendor_exp.values() if v>0),
        'exp_top5_share':pct(sum(v for _,v in ve_sorted[:5]), exp), 'exp_top10_share':pct(sum(v for _,v in ve_sorted[:10]), exp), 'exp_top20_share':pct(sum(v for _,v in ve_sorted[:20]), exp),
        'exp_gini':gini([v for v in vendor_exp.values() if v>0]),
        'top_face_vendors':vf_sorted[:10], 'top_exp_vendors':ve_sorted[:10]
    }

def fp_set(rows, fields):
    return {tuple((r.get(f) if f in r else None) for f in fields) for r in rows}

def exact_set(rows, fields):
    return fp_set(rows, fields)

def main():
    all_rows=[]; by={}; urls=[]
    for fy in YEARS:
        url, rows=fetch_year('gpsc-qqsz', fy)
        print('FETCH', url)
        print('FETCHED', fy[:4], len(rows))
        by[fy]=rows; all_rows.extend(rows); urls.append(url)
    os.makedirs('/home/user/workspace/faa_r5_outputs', exist_ok=True)
    with open('/home/user/workspace/faa_r5_outputs/gpsc_live_FY2022_2024.json','w') as f:
        json.dump(all_rows, f, sort_keys=True, separators=(',',':'))
    print('TOTAL_ROWS', len(all_rows))
    print('LIVE_JSON_SHA256_SORTED', hashlib.sha256(json.dumps(all_rows, sort_keys=True, separators=(",",":")).encode()).hexdigest())
    fields=sorted(set().union(*(r.keys() for r in all_rows)))
    print('FIELD_COUNT_UNION', len(fields))
    print('FIELDS_UNION', ','.join(fields))
    print('\nTHREE-YEAR MWBE VINTAGE SHARES')
    for fy in YEARS:
        st=stats_for(by[fy]); yr=fy[:4]
        print(yr, 'rows', st['rows'], 'face', fmt_money(st['face_total']), 'exp', fmt_money(st['exp_total']),
              'MWBE count/share', st['mwbe_count'], f"{st['mwbe_count_share']:.6f}%", 'face/share', fmt_money(st['mwbe_face']), f"{st['mwbe_face_share']:.6f}%", 'exp/share', fmt_money(st['mwbe_exp']), f"{st['mwbe_exp_share']:.6f}%")
    st=stats_for(by[YEARS[-1]])
    print('\nFY2024 DETAIL')
    for k in ['rows','face_total','exp_total','mwbe_count','mwbe_count_share','mwbe_face','mwbe_face_share','mwbe_exp','mwbe_exp_share','missing_contract_amount','zero_contract_amount','award_date_min','award_date_max','pre2024_face_share','vendor_count','vendor_count_all','exp_vendor_count','face_top5_share','face_top10_share','face_top20_share','face_gini','exp_top5_share','exp_top10_share','exp_top20_share','exp_gini']:
        v=st[k]
        if isinstance(v,D) and ('total' in k or k in ['mwbe_face','mwbe_exp']): print(k, fmt_money(v))
        elif isinstance(v,D): print(k, f"{v:.9f}")
        else: print(k, v)
    print('\nFY2024 PROCESS FACE')
    for ap,val in sorted(st['face_by_proc'].items(), key=lambda kv: kv[1], reverse=True):
        print(ap, 'count', st['count_by_proc'][ap], 'face', fmt_money(val), 'share', f"{pct(val, st['face_total']):.6f}%")
    print('\nFY2024 PROCESS EXPENDITURE')
    for ap,val in sorted(st['exp_by_proc'].items(), key=lambda kv: kv[1], reverse=True):
        print(ap, 'count', st['count_by_proc'][ap], 'exp', fmt_money(val), 'share', f"{pct(val, st['exp_total']):.6f}%")
    print('\nFY2024 TOP FACE VENDORS')
    for name,val in st['top_face_vendors']:
        print(name, fmt_money(val), f"share={pct(val,st['face_total']):.6f}%")
    # fingerprints
    excl={'fiscal_year_end_date','amount_expended_for_fiscal_year','amount_expended_to_date','current_or_outstanding_balance'}
    stable=[f for f in fields if f not in excl]
    print('\nFINGERPRINT_FIELDS_COUNT', len(stable), 'EXCLUDED', ','.join(sorted(excl)))
    pairs=[(YEARS[0],YEARS[1]),(YEARS[0],YEARS[2]),(YEARS[1],YEARS[2])]
    stable_counts=[]; exact_counts=[]
    for a,b in pairs:
        sc=len(fp_set(by[a], stable) & fp_set(by[b], stable))
        ec=len(exact_set(by[a], fields) & exact_set(by[b], fields))
        stable_counts.append(sc); exact_counts.append(ec)
        print('PAIR', a[:4]+'-'+b[:4], 'stable_overlap', sc, 'exact_all_field_overlap', ec)
    print('FINGERPRINT_SUMMARY stable', stable_counts, 'exact', exact_counts)
if __name__=='__main__': main()

```

## Independent recomputation — raw output

```text
FETCH https://data.ny.gov/resource/gpsc-qqsz.json?%24limit=50000&%24order=:id&fiscal_year_end_date=2022-12-31T00:00:00.000
FETCHED 2022 12156
FETCH https://data.ny.gov/resource/gpsc-qqsz.json?%24limit=50000&%24order=:id&fiscal_year_end_date=2023-12-31T00:00:00.000
FETCHED 2023 12114
FETCH https://data.ny.gov/resource/gpsc-qqsz.json?%24limit=50000&%24order=:id&fiscal_year_end_date=2024-12-31T00:00:00.000
FETCHED 2024 13718
TOTAL_ROWS 37988
LIVE_JSON_SHA256_SORTED 5f34136a62cfcdd5758c36c82f2bfb51c078f8563b90741314a6247ef758434b
FIELD_COUNT_UNION 22
FIELDS_UNION amount_expended_for_fiscal_year,amount_expended_to_date,authority_name,award_date,award_process,begin_date,contract_amount,current_or_outstanding_balance,end_date,fiscal_year_end_date,number_of_bids_or_proposals_received,number_of_mwbe_proposals,procurement_description,solicited_mwbe,type_of_procurement,vendor_city,vendor_country,vendor_is_a_mwbe,vendor_name,vendor_postal_code,vendor_province_region,vendor_state

THREE-YEAR MWBE VINTAGE SHARES
2022 rows 12156 face $54,698,007,774.69 exp $6,837,685,984.96 MWBE count/share 1996 16.419875% face/share $1,790,411,209.54 3.273266% exp/share $290,382,493.81 4.246795%
2023 rows 12114 face $63,569,204,049.36 exp $6,681,146,956.30 MWBE count/share 2251 18.581806% face/share $2,234,350,334.90 3.514831% exp/share $419,000,626.21 6.271388%
2024 rows 13718 face $65,189,755,228.64 exp $8,170,228,558.54 MWBE count/share 2570 18.734509% face/share $2,577,060,377.07 3.953168% exp/share $576,915,678.94 7.061194%

FY2024 DETAIL
rows 13718
face_total $65,189,755,228.64
exp_total $8,170,228,558.54
mwbe_count 2570
mwbe_count_share 18.734509404
mwbe_face $2,577,060,377.07
mwbe_face_share 3.953167746
mwbe_exp $576,915,678.94
mwbe_exp_share 7.061193880
missing_contract_amount 1348
zero_contract_amount 48
award_date_min 1984
award_date_max 2025
pre2024_face_share 91.687575808
vendor_count 2656
vendor_count_all 2907
exp_vendor_count 2518
face_top5_share 22.143422964
face_top10_share 30.415090280
face_top20_share 41.776851994
face_gini 0.931167744
exp_top5_share 16.868471520
exp_top10_share 26.241901200
exp_top20_share 37.566878907
exp_gini 0.904345045

FY2024 PROCESS FACE
Authority Contract - Competitive Bid count 10876 face $60,117,800,204.79 share 92.219705%
Authority Contract - Non-Competitive Bid count 1494 face $5,071,955,023.85 share 7.780295%
Non Contract Procurement/Purchase Order count 840 face $0.00 share 0.000000%
Purchased Under State Contract count 508 face $0.00 share 0.000000%

FY2024 PROCESS EXPENDITURE
Authority Contract - Competitive Bid count 10876 exp $7,324,883,484.56 share 89.653349%
Authority Contract - Non-Competitive Bid count 1494 exp $386,380,169.61 share 4.729123%
Purchased Under State Contract count 508 exp $264,491,190.67 share 3.237256%
Non Contract Procurement/Purchase Order count 840 exp $194,473,713.70 share 2.380273%

FY2024 TOP FACE VENDORS
KAWASAKI RAIL CAR INC $6,460,041,129.73 share=9.909596%
NEW FLYER OF AMERICA INC $2,561,472,333.08 share=3.929256%
HALMAR-RAILWORKS A JV $1,878,276,491.47 share=2.881245%
3RD TRACK CONSTRUCTORS $1,809,977,479.86 share=2.776475%
TUTOR PERINI CORP $1,725,475,795.41 share=2.646851%
JUDLAU CONTRACTING, INC. $1,631,565,796.92 share=2.502795%
SPRAGUE OPERATING RESOURCES, LLC $1,101,337,725.52 share=1.689434%
MITSUBISHI ELECTRIC POWER PRODUCTS INC $917,693,020.43 share=1.407726%
SKANSKA USA CIVIL NORTHEAST INC. $880,683,695.26 share=1.350954%
L.K. COMSTOCK AND COMPANY LLC $860,999,438.44 share=1.320759%

FINGERPRINT_FIELDS_COUNT 18 EXCLUDED amount_expended_for_fiscal_year,amount_expended_to_date,current_or_outstanding_balance,fiscal_year_end_date
PAIR 2022-2023 stable_overlap 2115 exact_all_field_overlap 0
PAIR 2022-2024 stable_overlap 604 exact_all_field_overlap 0
PAIR 2023-2024 stable_overlap 1002 exact_all_field_overlap 0
FINGERPRINT_SUMMARY stable [2115, 604, 1002] exact [0, 0, 0]

```

## Live first-party/community aggregate queries — code

```python
#!/usr/bin/env python3
import urllib.parse, urllib.request, json, decimal
BASE='https://data.ny.gov/resource'
queries=[]
for res in ['gpsc-qqsz','twsw-2mqa']:
    params={'$select':'count(*) as row_count, sum(contract_amount) as face_total, sum(amount_expended_for_fiscal_year) as exp_total', 'fiscal_year_end_date':'2024-12-31T00:00:00.000'}
    url=f'{BASE}/{res}.json?'+urllib.parse.urlencode(params, safe='(),* ')
    data=json.load(urllib.request.urlopen(url, timeout=120))
    print('QUERY_URL', url)
    print('RESULT', res, json.dumps(data, sort_keys=True))

```

## Live first-party/community aggregate queries — raw output

```text
QUERY_URL https://data.ny.gov/resource/gpsc-qqsz.json?%24select=count(*)+as+row_count,+sum(contract_amount)+as+face_total,+sum(amount_expended_for_fiscal_year)+as+exp_total&fiscal_year_end_date=2024-12-31T00%3A00%3A00.000
RESULT gpsc-qqsz [{"exp_total": "8170228558.54", "face_total": "65189755228.64", "row_count": "13718"}]
QUERY_URL https://data.ny.gov/resource/twsw-2mqa.json?%24select=count(*)+as+row_count,+sum(contract_amount)+as+face_total,+sum(amount_expended_for_fiscal_year)+as+exp_total&fiscal_year_end_date=2024-12-31T00%3A00%3A00.000
RESULT twsw-2mqa [{"exp_total": "8148961067.82", "face_total": "65131682801.41", "row_count": "13648"}]

```

## Capital join — code

```python
#!/usr/bin/env python3
import urllib.parse, urllib.request, json
BASE='https://data.ny.gov/resource'
def get(res, params):
    url=f'{BASE}/{res}.json?'+urllib.parse.urlencode(params, safe='(),*')
    with urllib.request.urlopen(url, timeout=120) as r:
        return url, json.loads(r.read().decode())
def meta(res):
    url=f'https://data.ny.gov/api/views/{res}'
    return url, json.load(urllib.request.urlopen(url, timeout=120))
# metadata borough check
url, md=meta('wcsa-vkhf')
fields=[c['fieldName'] for c in md['columns']]
print('METADATA_URL', url)
print('WCSA_FIELDS', ','.join(fields))
print('WCSA_HAS_BOROUGH_FIELD', any('borough' in f.lower() for f in fields))
# sample 120 distinct project numbers from locations
url, locs=get('wcsa-vkhf', {'$select':'project_number', '$where':'project_number is not null', '$group':'project_number', '$order':'project_number', '$limit':120})
projects=[r['project_number'] for r in locs]
print('LOCATION_SAMPLE_QUERY', url)
print('LOCATION_SAMPLE_COUNT', len(projects), 'FIRST10', projects[:10])
# batch using SoQL IN string literals
quoted=','.join("'"+p.replace("'","''")+"'" for p in projects)
url_k, kres=get('kizb-nxtu', {'$select':'project_number, count(*) as rows, sum(total_allocation) as total_allocation_sum', '$where':f'project_number in({quoted})', '$group':'project_number', '$limit':50000})
url_e, eres=get('ehz8-ag3n', {'$select':'proj_num, count(*) as rows, sum(current_budget) as current_budget_sum', '$where':f'proj_num in({quoted})', '$group':'proj_num', '$limit':50000})
kset={r['project_number'] for r in kres}; eset={r['proj_num'] for r in eres}
print('KIZB_JOIN_QUERY', url_k)
print('KIZB_MATCHED_PROJECTS', len(kset), 'OF', len(projects), 'UNMATCHED', [p for p in projects if p not in kset][:20])
print('KIZB_FIRST5_RESULTS', json.dumps(kres[:5], sort_keys=True))
print('EHZ8_JOIN_QUERY', url_e)
print('EHZ8_MATCHED_PROJECTS', len(eset), 'OF', len(projects), 'UNMATCHED', [p for p in projects if p not in eset][:20])
print('EHZ8_FIRST5_RESULTS', json.dumps(eres[:5], sort_keys=True))
# worked example: first project matched in both
for p in projects:
    if p in kset and p in eset:
        print('WORKED_PROJECT', p)
        print('KIZB_WORKED', [r for r in kres if r['project_number']==p][:1])
        print('EHZ8_WORKED', [r for r in eres if r['proj_num']==p][:1])
        break

```

## Capital join — raw output

```text
METADATA_URL https://data.ny.gov/api/views/wcsa-vkhf
WCSA_FIELDS project_number,project_number_sequence,plan_series,capital_plan,agency_name,category_description,element_description,project_description,latitude,longitude,location_indicator,location,georeference,:@computed_region_yamh_8v7k,:@computed_region_wbg7_3whc,:@computed_region_kjdx_g34t
WCSA_HAS_BOROUGH_FIELD False
LOCATION_SAMPLE_QUERY https://data.ny.gov/resource/wcsa-vkhf.json?%24select=project_number&%24where=project_number+is+not+null&%24group=project_number&%24order=project_number&%24limit=120
LOCATION_SAMPLE_COUNT 120 FIRST10 ['D501CB08', 'D501TN85', 'D502BW89', 'D502HH80', 'D502TB64', 'D502TN50', 'D502VN80', 'D601BB28', 'D601BW07', 'D601BW14']
KIZB_JOIN_QUERY https://data.ny.gov/resource/kizb-nxtu.json?%24select=project_number,+count(*)+as+rows,+sum(total_allocation)+as+total_allocation_sum&%24where=project_number+in(%27D501CB08%27,%27D501TN85%27,%27D502BW89%27,%27D502HH80%27,%27D502TB64%27,%27D502TN50%27,%27D502VN80%27,%27D601BB28%27,%27D601BW07%27,%27D601BW14%27,%27D601BW84%27,%27D601BW97%27,%27D601CB09%27,%27D601HH07%27,%27D601HH81%27,%27D601HH89%27,%27D601MP06%27,%27D601MP16%27,%27D601MPXB%27,%27D601QM18%27,%27D601QM40%27,%27D601RK19%27,%27D601RK23%27,%27D601RK76%27,%27D601TN52%27,%27D601TN60%27,%27D601VN34%27,%27D601VN35%27,%27D602BB54%27,%27D602BW63%27,%27D602BW89%27,%27D602HH10%27,%27D602HH88%27,%27D602MP21%27,%27D602RK65%27,%27D602RK70%27,%27D602RK73%27,%27D602RK74%27,%27D602RK75%27,%27D602RKXD%27,%27D602TN49%27,%27D602TN82%27,%27D602VN03%27,%27D602VN80%27,%27D602VN84%27,%27D603HH85%27,%27D604BB28%27,%27D604BB45%27,%27D604BW15%27,%27D604MP03%27,%27D604MPXA%27,%27D604QM30%27,%27D604QM81%27,%27D604VN87%27,%27D605BB21%27,%27D605BB43%27,%27D607HH10%27,%27D607HH85%27,%27D607MP21%27,%27D607MPXC%27,%27D607RK65%27,%27D607TN82%27,%27D607TN85%27,%27D607TN87%27,%27D607VN35%27,%27D607VN80%27,%27D607VN84%27,%27D607VN88%27,%27D701AW98%27,%27D701BW07%27,%27D701BW14%27,%27D701BW84%27,%27D701CB18%27,%27D701CB24%27,%27D701HC28%27,%27D701HC48%27,%27D701HH07%27,%27D701HH89%27,%27D701QM18%27,%27D701QM40%27,%27D701RK04%27,%27D701RK19%27,%27D701RK20%27,%27D701RK22%27,%27D701RK70%27,%27D701TN53%27,%27D701TN87%27,%27D701VN10%27,%27D701VN32%27,%27D701VN34%27,%27D701VN89%27,%27D701VN8Q%27,%27D702RK23%27,%27D702RK65%27,%27D702TN49%27,%27D702TN55%27,%27D702VN11%27,%27D702VN80%27,%27D702VN84%27,%27D702VN86%27,%27D703AW32%27,%27D703BW63%27,%27D703CB63%27,%27D703HC63%27,%27D703HH63%27,%27D703HH88%27,%27D703MP63%27,%27D703QM63%27,%27D703RK63%27,%27D703TN63%27,%27D703VN63%27,%27D704AW67%27,%27D704BW32%27,%27D704BW39%27,%27D704HC07%27,%27D704HC30%27,%27D704HC64%27,%27D704HH13%27,%27D704HH19%27,%27D704QM81%27)&%24group=project_number&%24limit=50000
KIZB_MATCHED_PROJECTS 120 OF 120 UNMATCHED []
KIZB_FIRST5_RESULTS [{"project_number": "D501CB08", "rows": "6", "total_allocation_sum": "368254"}, {"project_number": "D501TN85", "rows": "6", "total_allocation_sum": "106330"}, {"project_number": "D502BW89", "rows": "6", "total_allocation_sum": "1020785"}, {"project_number": "D502HH80", "rows": "6", "total_allocation_sum": "453523"}, {"project_number": "D502TB64", "rows": "6", "total_allocation_sum": "1564961"}]
EHZ8_JOIN_QUERY https://data.ny.gov/resource/ehz8-ag3n.json?%24select=proj_num,+count(*)+as+rows,+sum(current_budget)+as+current_budget_sum&%24where=proj_num+in(%27D501CB08%27,%27D501TN85%27,%27D502BW89%27,%27D502HH80%27,%27D502TB64%27,%27D502TN50%27,%27D502VN80%27,%27D601BB28%27,%27D601BW07%27,%27D601BW14%27,%27D601BW84%27,%27D601BW97%27,%27D601CB09%27,%27D601HH07%27,%27D601HH81%27,%27D601HH89%27,%27D601MP06%27,%27D601MP16%27,%27D601MPXB%27,%27D601QM18%27,%27D601QM40%27,%27D601RK19%27,%27D601RK23%27,%27D601RK76%27,%27D601TN52%27,%27D601TN60%27,%27D601VN34%27,%27D601VN35%27,%27D602BB54%27,%27D602BW63%27,%27D602BW89%27,%27D602HH10%27,%27D602HH88%27,%27D602MP21%27,%27D602RK65%27,%27D602RK70%27,%27D602RK73%27,%27D602RK74%27,%27D602RK75%27,%27D602RKXD%27,%27D602TN49%27,%27D602TN82%27,%27D602VN03%27,%27D602VN80%27,%27D602VN84%27,%27D603HH85%27,%27D604BB28%27,%27D604BB45%27,%27D604BW15%27,%27D604MP03%27,%27D604MPXA%27,%27D604QM30%27,%27D604QM81%27,%27D604VN87%27,%27D605BB21%27,%27D605BB43%27,%27D607HH10%27,%27D607HH85%27,%27D607MP21%27,%27D607MPXC%27,%27D607RK65%27,%27D607TN82%27,%27D607TN85%27,%27D607TN87%27,%27D607VN35%27,%27D607VN80%27,%27D607VN84%27,%27D607VN88%27,%27D701AW98%27,%27D701BW07%27,%27D701BW14%27,%27D701BW84%27,%27D701CB18%27,%27D701CB24%27,%27D701HC28%27,%27D701HC48%27,%27D701HH07%27,%27D701HH89%27,%27D701QM18%27,%27D701QM40%27,%27D701RK04%27,%27D701RK19%27,%27D701RK20%27,%27D701RK22%27,%27D701RK70%27,%27D701TN53%27,%27D701TN87%27,%27D701VN10%27,%27D701VN32%27,%27D701VN34%27,%27D701VN89%27,%27D701VN8Q%27,%27D702RK23%27,%27D702RK65%27,%27D702TN49%27,%27D702TN55%27,%27D702VN11%27,%27D702VN80%27,%27D702VN84%27,%27D702VN86%27,%27D703AW32%27,%27D703BW63%27,%27D703CB63%27,%27D703HC63%27,%27D703HH63%27,%27D703HH88%27,%27D703MP63%27,%27D703QM63%27,%27D703RK63%27,%27D703TN63%27,%27D703VN63%27,%27D704AW67%27,%27D704BW32%27,%27D704BW39%27,%27D704HC07%27,%27D704HC30%27,%27D704HC64%27,%27D704HH13%27,%27D704HH19%27,%27D704QM81%27)&%24group=proj_num&%24limit=50000
EHZ8_MATCHED_PROJECTS 120 OF 120 UNMATCHED []
EHZ8_FIRST5_RESULTS [{"current_budget_sum": "1322227873.68", "proj_num": "D501CB08", "rows": "22"}, {"current_budget_sum": "726462879.66", "proj_num": "D501TN85", "rows": "22"}, {"current_budget_sum": "4143835105.73", "proj_num": "D502BW89", "rows": "22"}, {"current_budget_sum": "1752337639.29", "proj_num": "D502HH80", "rows": "22"}, {"current_budget_sum": "5161585683.66", "proj_num": "D502TB64", "rows": "22"}]
WORKED_PROJECT D501CB08
KIZB_WORKED [{'project_number': 'D501CB08', 'rows': '6', 'total_allocation_sum': '368254'}]
EHZ8_WORKED [{'proj_num': 'D501CB08', 'rows': '22', 'current_budget_sum': '1322227873.68'}]

```

## Adversarial independent drift check — code

```python
#!/usr/bin/env python3
import json, decimal, copy, os
from collections import defaultdict
D=decimal.Decimal
P='/home/user/workspace/faa_r5_outputs/gpsc_live_FY2022_2024.json'
rows=json.load(open(P))

def dec(x):
    if x in (None,''): return None
    return D(str(x))
def stats(rows):
    fy24=[r for r in rows if r.get('fiscal_year_end_date')=='2024-12-31T00:00:00.000']
    face=sum((dec(r.get('contract_amount')) or D(0)) for r in fy24)
    mw=[r for r in fy24 if str(r.get('vendor_is_a_mwbe','')).strip().upper()=='Y']
    mwface=sum((dec(r.get('contract_amount')) or D(0)) for r in mw)
    return {'fy2024_rows':len(fy24),'fy2024_face_total':str(face),'fy2024_mwbe_face_total':str(mwface),'fy2024_mwbe_face_share':str((mwface/face*D(100)) if face else D(0))}
base=stats(rows)
mut=copy.deepcopy(rows)
changed=None
for r in mut:
    if r.get('fiscal_year_end_date')=='2024-12-31T00:00:00.000' and str(r.get('vendor_is_a_mwbe','')).strip().upper()!='Y':
        v=dec(r.get('contract_amount'))
        if v and v>0:
            before=v; after=v+D('1.00'); r['contract_amount']=str(after); changed=(r.get('vendor_name'), before, after); break
assert changed
mut_path='/home/user/workspace/faa_r5_outputs/gpsc_live_FY2022_2024_mutated_nonmwbe.json'
json.dump(mut, open(mut_path,'w'), sort_keys=True, separators=(',',':'))
new=stats(mut)
print('BASELINE_FILE', P)
print('MUTATED_FILE', mut_path)
print('MUTATION_NON_MWBE_VENDOR_AMOUNT', changed[0], 'before', changed[1], 'after', changed[2])
print('BASELINE_STATS', json.dumps(base, sort_keys=True))
print('MUTATED_STATS', json.dumps(new, sort_keys=True))
diffs={k:(base[k],new[k]) for k in base if base[k]!=new[k]}
print('DRIFT_FLAGGED', bool(diffs))
print('DIFFS', json.dumps(diffs, sort_keys=True))
if diffs: raise SystemExit(2)

```

## Adversarial independent drift check — raw output

```text
BASELINE_FILE /home/user/workspace/faa_r5_outputs/gpsc_live_FY2022_2024.json
MUTATED_FILE /home/user/workspace/faa_r5_outputs/gpsc_live_FY2022_2024_mutated_nonmwbe.json
MUTATION_NON_MWBE_VENDOR_AMOUNT 22ND CENTURY TECHNOLOGIES, INC before 4500000.00 after 4500001.00
BASELINE_STATS {"fy2024_face_total": "65189755228.64", "fy2024_mwbe_face_share": "3.953167745501539723052003459", "fy2024_mwbe_face_total": "2577060377.07", "fy2024_rows": 13718}
MUTATED_STATS {"fy2024_face_total": "65189755229.64", "fy2024_mwbe_face_share": "3.953167745440898787500459274", "fy2024_mwbe_face_total": "2577060377.07", "fy2024_rows": 13718}
DRIFT_FLAGGED True
DIFFS {"fy2024_face_total": ["65189755228.64", "65189755229.64"], "fy2024_mwbe_face_share": ["3.953167745501539723052003459", "3.953167745440898787500459274"]}

```

## Scope assessment

The estimand discipline is substantively sound: `contract_amount` is treated as contract face-value stock, `amount_expended_for_fiscal_year` is treated as annual flow, the independent live recompute found FY2024 face value $65,189,755,228.64 and FY2024 annual expenditure $8,170,228,558.54, and 91.687575808% of FY2024 face value was from pre-2024 awards ([gpsc 2024 query](https://data.ny.gov/resource/gpsc-qqsz.json?%24limit=50000&%24order=:id&fiscal_year_end_date=2024-12-31T00:00:00.000)). The MWBE framing is substantively descriptive rather than goal-attainment-based in the current reader note: the independently recomputed FY2024 MWBE prime-vendor shares were 18.734509404% by count, 3.953167746% by face value, and 7.061193880% by annual expenditure ([gpsc 2024 query](https://data.ny.gov/resource/gpsc-qqsz.json?%24limit=50000&%24order=:id&fiscal_year_end_date=2024-12-31T00:00:00.000)). The concentration explanation is appropriately non-culpable and structural: my recompute found FY2024 top-10 face-value concentration of 30.415090280% and positive-face-vendor Gini of 0.931167744, with the annual-expenditure Gini also high at 0.904345045 ([gpsc 2024 query](https://data.ny.gov/resource/gpsc-qqsz.json?%24limit=50000&%24order=:id&fiscal_year_end_date=2024-12-31T00:00:00.000)). The 18-field vintage-overlap fingerprint prose matches the reproducing method: excluding fiscal year and the three annual-state fields yielded overlaps of 2,115, 604, and 1,002, while exact all-field overlap was zero in all three pairings ([gpsc 2022 query](https://data.ny.gov/resource/gpsc-qqsz.json?%24limit=50000&%24order=:id&fiscal_year_end_date=2022-12-31T00:00:00.000), [gpsc 2023 query](https://data.ny.gov/resource/gpsc-qqsz.json?%24limit=50000&%24order=:id&fiscal_year_end_date=2023-12-31T00:00:00.000), [gpsc 2024 query](https://data.ny.gov/resource/gpsc-qqsz.json?%24limit=50000&%24order=:id&fiscal_year_end_date=2024-12-31T00:00:00.000)). Provenance is mostly accurate because the reader note identifies `gpsc-qqsz` as a community-created view and separately names first-party `twsw-2mqa`; however, the “under 0.1 percent” divergence wording needs narrowing to dollar totals because row counts differ by about 0.51% ([gpsc aggregate query](https://data.ny.gov/resource/gpsc-qqsz.json?%24select=count(*)+as+row_count,+sum(contract_amount)+as+face_total,+sum(amount_expended_for_fiscal_year)+as+exp_total&fiscal_year_end_date=2024-12-31T00%3A00%3A00.000), [twsw aggregate query](https://data.ny.gov/resource/twsw-2mqa.json?%24select=count(*)+as+row_count,+sum(contract_amount)+as+face_total,+sum(amount_expended_for_fiscal_year)+as+exp_total&fiscal_year_end_date=2024-12-31T00%3A00%3A00.000)).

## Regression assessment

The previously reported stock/flow, MWBE goal-attainment, competitive-process “pass,” first-party provenance, three-year row-count, common-schema, missing/zero split, live-comparator breadth, fingerprint-method, and annual-expenditure-concentration issues appear substantively absorbed in the reader-facing v0.4 text. The recurring version/status propagation defect is not fully cured because the companion’s authoritative Current State block simultaneously states “one of two” and “ZERO” for consecutive-passing status. The reproduction-package availability problem remains blocking for this closing round because the paper and companion describe an accompanying frozen package that was not supplied and was not recoverable from the artifact links I checked.

## Findings

### F-AA-R5-01

1. **Identifier:** F-AA-R5-01
2. **Severity:** HIGH
3. **Locus:** Reader Section 8; Companion Current State and Verification Status; supplied audit-packet inventory.
4. **Substance:** The surface says the frozen three-year snapshot, manifest, and `reproduce_paper2.py` accompany the published/current package, but the substrate supplied for this audit lacked the required files under their mandated names, and the artifact links I checked did not recover them.
5. **Disposition:** OPEN; this blocks mandatory supplied-script steps 1-3 and prevents a qualifying PASS even though independent live recomputation succeeded.
6. **Cross-reference:** Execution matrix steps 1-3; “Mandatory supplied-package execution attempt”; recovery checks against [Bayyinah homepage](https://bayyinah.dev/), [Bayyinah research index](https://raw.githubusercontent.com/BayyinahEnterprise/Bayyinah-Integrity-Scanner/main/docs/research.md), and the three referenced Zenodo API records ([21436484](https://zenodo.org/api/records/21436484), [19894724](https://zenodo.org/api/records/19894724), [20069654](https://zenodo.org/api/records/20069654)).

### F-AA-R5-02

1. **Identifier:** F-AA-R5-02
2. **Severity:** HIGH
3. **Locus:** Audit Companion, Current State bullets for consecutive-passing status.
4. **Substance:** The surface of the authoritative Current State block presents two incompatible status substrates: it says F-AA-R4 makes the letter count “one of two,” but the immediately following bullet says the count “toward convergence” is “ZERO” and “has never left zero,” which no longer matches the recorded F-AA-R4 PASS state.
5. **Disposition:** OPEN; revise the authoritative Current State block to one unambiguous status convention, such as “letter count one of two; evidentiary reproduction gap remains; convergence not declared.”
6. **Cross-reference:** Reader header, Reader Sections 6-7, Companion Current State, and prior propagation defects F-AA-R2-05 and F-AA-R3-01/02.

### F-AA-R5-03

1. **Identifier:** F-AA-R5-03
2. **Severity:** LOW
3. **Locus:** Reader Section 3 provenance comparison of `gpsc-qqsz` and `twsw-2mqa`.
4. **Substance:** The surface states the community and first-party resources differ by “under 0.1 percent,” but the live substrate shows the face-value total differs by about 0.089% while the row-count difference is 70 records, about 0.51% of the `gpsc-qqsz` FY2024 count.
5. **Disposition:** OPEN; clarify that the under-0.1% statement applies to face-value dollars, not row counts.
6. **Cross-reference:** Execution matrix step 5 and the live aggregate outputs from [data.ny.gov `gpsc-qqsz`](https://data.ny.gov/resource/gpsc-qqsz.json?%24select=count(*)+as+row_count,+sum(contract_amount)+as+face_total,+sum(amount_expended_for_fiscal_year)+as+exp_total&fiscal_year_end_date=2024-12-31T00%3A00%3A00.000) and [data.ny.gov `twsw-2mqa`](https://data.ny.gov/resource/twsw-2mqa.json?%24select=count(*)+as+row_count,+sum(contract_amount)+as+face_total,+sum(amount_expended_for_fiscal_year)+as+exp_total&fiscal_year_end_date=2024-12-31T00%3A00%3A00.000).

## Files saved

- `/home/user/workspace/model-council-gpt_5_5.md` — this standalone report.
- `/home/user/workspace/faa_r5_independent_recompute.py` — independent recomputation code.
- `/home/user/workspace/faa_r5_live_query_step5.py` — live aggregate query code.
- `/home/user/workspace/faa_r5_capital_join_step6.py` — capital join check code.
- `/home/user/workspace/faa_r5_adversarial_step7.py` — independent adversarial drift code.
- `/home/user/workspace/faa_r5_outputs/` — raw outputs and live JSON artifacts generated during this audit.

---

# Bismillah ir-Rahman ir-Rahim
