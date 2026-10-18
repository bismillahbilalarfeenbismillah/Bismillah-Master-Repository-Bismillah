# Bismillah ir-Rahman ir-Rahim

# R0409 -- verify_shvvp_v0_8_rc1.py — Producer self-check for the SHVVP v0.8-rc1 revision candidate.

**Chronological Index:** 346 of 995  
**Date:** 2026-07-24  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** verify_shvvp_v0_8_rc1.py  
**Source Format:** py  
**SHA-256:** `0601593dada1add6bae306dbea2a5b50ff490b8b3bf0d54453cfc6df1208702e`  

---

## R0409 · verify_shvvp_v0_8_rc1.py — Producer self-check for the SHVVP v0.8-rc1 revision candidate.

- section: V. BSSG & SHVVP Protocols
- source_file: verify_shvvp_v0_8_rc1.py
- source_format: py
- text_sha256: 0601593dada1add6bae306dbea2a5b50ff490b8b3bf0d54453cfc6df1208702e

"""Producer self-check for the SHVVP v0.8-rc1 revision candidate.

Advisory only. Writes verify_shvvp_v0_8_rc1_receipt.json and exits non-zero on any
failed gate. No release private key is present or required.
"""
from __future__ import annotations
import hashlib, inspect, json, os, re, subprocess, sys
HERE=os.path.dirname(os.path.abspath(__file__))
SRC=os.path.join(HERE,'SHV_VALIDATION_PROTOCOL_v0_8_rc1_source.md')
PDF=os.path.join(HERE,'SHVVP_v0_8_rc1_flagship.pdf')
TESTS=os.path.join(HERE,'test_shvvp_v0_8_rules.py')
VECT=os.path.join(HERE,'shvvp_v0_8_signed_test_vectors.json')
RESULTS=[]
def gate(name,cond,detail=''):
    RESULTS.append((name,bool(cond),detail)); print(('%-6s '%('PASS' if cond else 'FAIL'))+name+(('  ['+detail+']') if detail and not cond else ''))
def sha(path): return hashlib.sha256(open(path,'rb').read()).hexdigest()
def main():
    sys.path.insert(0,HERE); import shvvp_v0_8_route_gates as G
    canon=G._manifest_canonical()
    gate('G1 manifest digest reproducible and binds all three authorities',
         G.MANIFEST_SHA256==hashlib.sha256(canon.encode()).hexdigest() and all(k in canon for k in (G.COMMITMENT_AUTHORITY_PUBKEY,G.RUN_LOGGER_PUBKEY,G.PRERUN_ANCHOR_PUBKEY)))
    sig=inspect.signature(G.route_claims)
    gate('G2 public route interface has no trust-root override',list(sig.parameters)==['raw_evidence','commitments','run_logs'],str(sig))
    vec=json.load(open(VECT)); gate('G3 signed vectors match manifest and fixed keys',vec['manifest_sha256']==G.MANIFEST_SHA256 and vec['public_keys']=={'commitment':G.COMMITMENT_AUTHORITY_PUBKEY,'logger':G.RUN_LOGGER_PUBKEY,'anchor':G.PRERUN_ANCHOR_PUBKEY})
    proc=subprocess.run([sys.executable,TESTS],cwd=HERE,capture_output=True,text=True)
    gate('G4 adversarial regression suite exits clean',proc.returncode==0,proc.stdout.strip().splitlines()[-1] if proc.stdout else proc.stderr[-300:])
    src=open(SRC,encoding='utf-8').read()
    current=['(SHVVP) v0.8-rc1','PRODUCER REVISION CANDIDATE, v0.8-rc1','End of producer revision candidate v0.8-rc1','Versions 0.1 through 0.7 are HALTED']
    gate('G5 candidate identity is internally explicit',all(x in src for x in current))
    gate('G6 F-P7 repairs are represented in source',all(x in src for x in ['No runtime trust-root selection.','Independent pre-run anchor.','Individually authenticated append history.','exact authenticated Channel-A sealed commitment resolved by `commitment_id`']))
    forbidden=['sealed value carried on the record','End of frozen contract v0.7','FROZEN preregistration, version 0.7']
    gate('G7 no stale current-contract denominator/version phrase remains',not any(x in src for x in forbidden),str([x for x in forbidden if x in src]))
    code=open(os.path.join(HERE,'shvvp_v0_8_route_gates.py')).read()
    gate('G8 code contains no trusted_pubkey interface', 'trusted_pubkey' not in code)
    gate('G9 no Unicode en/em dash in current artifacts','\u2013' not in src and '\u2014' not in src and '\u2013' not in code and '\u2014' not in code)
    pages=0; black=[]; pdf_ok=os.path.exists(PDF)
    try:
        import fitz
        doc=fitz.open(PDF); pages=doc.page_count
        for i,p in enumerate(doc):
            px=p.get_pixmap(dpi=60,colorspace=fitz.csGRAY)
            if sum(b<40 for b in px.samples)/len(px.samples)>0.5: black.append(i+1)
    except Exception as e:
        pdf_ok=False
    gate('G10 PDF is 61 pages and has no all-black page',pdf_ok and pages==61 and not black,'pages=%s black=%s'%(pages,black))
    # Fixtures must contain public material and signatures, never obvious private key fields.
    keys=[]
    def walk(x):
        if isinstance(x,dict):
            for k,v in x.items():
                if 'private' in k.lower() or 'seed' in k.lower(): keys.append(k)
                walk(v)
        elif isinstance(x,list):
            for v in x: walk(v)
    walk(vec)
    gate('G11 signed vectors contain no private-key or seed field',not keys,str(keys))
    carried=('shvvp_v0_5_decision_rules.py','shvvp_v0_5_power_sim.py','test_shvvp_v0_5_rules.py','power_sim_receipt.json')
    gate('G12 carried unchanged v0.5 modules are present',all(os.path.exists(os.path.join(HERE,n)) for n in carried))
    receipt={'artifact':'SHVVP v0.8-rc1 revision candidate','candidate_date':'2026-07-24','manifest_sha256':G.MANIFEST_SHA256,
             'authorities':{'commitment':G.COMMITMENT_AUTHORITY_PUBKEY,'logger':G.RUN_LOGGER_PUBKEY,'anchor':G.PRERUN_ANCHOR_PUBKEY},
             'source_sha256':sha(SRC),'pdf_sha256':sha(PDF) if os.path.exists(PDF) else None,'pdf_pages':pages,
             'tests_tail':proc.stdout.strip().splitlines()[-1] if proc.stdout else None,
             'gates':[{'name':n,'pass':ok,'detail':d} for n,ok,d in RESULTS],
             'all_pass':all(ok for _,ok,_ in RESULTS),
             'note':'Producer self-check only. Candidate is not frozen or carried.'}
    open(os.path.join(HERE,'verify_shvvp_v0_8_rc1_receipt.json'),'w').write(json.dumps(receipt,indent=2))
    failed=[n for n,ok,_ in RESULTS if not ok]; print('\n%d gates, %d failed'%(len(RESULTS),len(failed)))
    return 1 if failed else 0
if __name__=='__main__': raise SystemExit(main())

---

# Bismillah ir-Rahman ir-Rahim
