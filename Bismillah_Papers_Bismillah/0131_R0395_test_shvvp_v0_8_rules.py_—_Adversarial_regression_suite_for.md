# Bismillah ir-Rahman ir-Rahim

# R0395 -- test_shvvp_v0_8_rules.py — Adversarial regression suite for SHVVP v0.8-rc1.

**Chronological Index:** 131 of 995  
**Date:** 2026  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** test_shvvp_v0_8_rules.py  
**Source Format:** py  
**SHA-256:** `a769a1400bd76d4309e8bffe13f2cde0ff174f6813d4a83c4543d9fc7b38179f`  

---

## R0395 · test_shvvp_v0_8_rules.py — Adversarial regression suite for SHVVP v0.8-rc1.

- section: V. BSSG & SHVVP Protocols
- source_file: test_shvvp_v0_8_rules.py
- source_format: py
- text_sha256: a769a1400bd76d4309e8bffe13f2cde0ff174f6813d4a83c4543d9fc7b38179f

"""Adversarial regression suite for SHVVP v0.8-rc1.

The suite uses pre-signed positive and negative vectors. No private release key is
shipped. An ephemeral attacker key is generated only to prove that a caller-created
trust root cannot replace a manifest-bound authority.
"""
from __future__ import annotations
import copy, hashlib, inspect, json, os
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
import shvvp_v0_8_route_gates as G

HERE=os.path.dirname(os.path.abspath(__file__))
V=json.load(open(os.path.join(HERE,'shvvp_v0_8_signed_test_vectors.json')))
COMM=V['commitments']; LOGS=V['run_logs']; NEG=V['negative_vectors']
FAIL=[]; COUNT=0

def check(name,cond,detail=''):
    global COUNT; COUNT+=1
    print(('PASS  ' if cond else 'FAIL  ')+name+(('  ['+detail+']') if detail and not cond else ''))
    if not cond: FAIL.append(name)

def raises(fn, exc=G.RouteInputError):
    try: fn(); return False
    except exc: return True

def cid_for(key):
    for cid,c in COMM.items():
        if c.get('kind')==G.KIND_SEALED and c.get('component')==key: return cid
        if c.get('kind')==G.KIND_REALIZED and c.get('pre_run',{}).get('component')==key: return cid
    raise KeyError(key)

def raw(key,d,n,viol=None,recon=None,cid=None):
    e=G.MANIFEST_BY_KEY[key]; s=G.BY_KEY[key]
    r={s.denominator_field:d,s.numerator_field:n,
       'manifest_sha256':G.MANIFEST_SHA256,'universe_id':e.universe_id}
    if s.violation_field: r[s.violation_field]=0 if viol is None else viol
    if e.kind in (G.KIND_SEALED,G.KIND_REALIZED): r['commitment_id']=cid or cid_for(key)
    if recon is not None: r['reconciliation']=recon
    return r

def good():
    return {
      'R1-A':raw('R1-A',8,8),'R2-A':raw('R2-A',16,16,0),
      'R2-B':raw('R2-B',100,100),'R3-A':raw('R3-A',12,12,0),
      'R4-B':raw('R4-B',60,60,0),'R4-C':raw('R4-C',216,216,0),
      'R5-A':raw('R5-A',25,25,0),'R5-C':raw('R5-C',9,9,0),
      'R6-A':raw('R6-A',60,60,0),'R6-B':raw('R6-B',40,40,0),
      'R6-C':raw('R6-C',35,35,0),
    }

def claims(ev,comm=None,logs=None): return G.route_claims(ev,comm or COMM,logs or LOGS)

def positive():
    out=claims(good())
    check('P1 full authentic corpus supports every route',set(v['claim'] for v in out['routes'].values())=={'SUPPORTED-DESCRIPTIVE'})
    check('P2 result reports all three manifest-bound authorities',out['authorities']=={'commitment_authority_pubkey':G.COMMITMENT_AUTHORITY_PUBKEY,'run_logger_pubkey':G.RUN_LOGGER_PUBKEY,'prerun_anchor_pubkey':G.PRERUN_ANCHOR_PUBKEY})
    check('P3 no inference is produced',out['inference'].startswith('NONE'))
    ev=good(); ev['R5-A']=raw('R5-A',24,24,0,{'universe_n':25,'excluded':[{'count':1,'reason':'not reached'}]})
    comp=claims(ev)['components']['R5-A']
    check('P4 reconciled 24/25 is scored over 25',comp['denominator']==25 and comp['numerator']==24 and comp['gate_pass'])
    check('P5 signed fixture manifest and public keys match module',V['manifest_sha256']==G.MANIFEST_SHA256 and V['public_keys']=={'commitment':G.COMMITMENT_AUTHORITY_PUBKEY,'logger':G.RUN_LOGGER_PUBKEY,'anchor':G.PRERUN_ANCHOR_PUBKEY})

def fp71_key_boundary():
    sig=inspect.signature(G.route_claims)
    check('A1 route_claims exposes no trusted_pubkey parameter','trusted_pubkey' not in sig.parameters,str(sig))
    check('A2 caller cannot pass a key override',raises(lambda:G.route_claims(good(),COMM,LOGS,trusted_pubkey='00'*32),TypeError))
    canon=G._manifest_canonical()
    check('A3 manifest binds all fixed authority keys',all(k in canon for k in (G.COMMITMENT_AUTHORITY_PUBKEY,G.RUN_LOGGER_PUBKEY,G.PRERUN_ANCHOR_PUBKEY)))
    # Caller-generated key and favorable 20 seal.
    atk=Ed25519PrivateKey.generate(); pub=atk.public_key().public_bytes_raw().hex(); key='R5-A'; e=G.MANIFEST_BY_KEY[key]
    fake={'kind':G.KIND_SEALED,'commitment_id':'attacker-r5a','protocol_version':G.PROTOCOL_VERSION,
          'manifest_sha256':G.MANIFEST_SHA256,'component':key,'universe_id':e.universe_id,
          'sealed_universe_n':20,'sealed_universe_inventory_hash':'b'*64,'authority':'attacker',
          'commitment_sequence':1,'committed_at':'2026-07-24T12:00:00Z'}
    fake['signature']=atk.sign(G.sealed_commitment_payload(fake)).hex()
    ev=good(); ev['R5-A']=raw('R5-A',20,20,0,cid='attacker-r5a')
    cm=dict(COMM); cm['attacker-r5a']=fake
    check('A4 self-signed favorable subset under caller key is rejected',raises(lambda:claims(ev,cm,LOGS)))
    check('A5 attacker public key is absent from manifest',pub not in canon)
    # Valid signed negatives under actual authority isolate binding checks.
    for label,name in [('A6 validly signed cross-version commitment rejects','cross_version'),('A7 validly signed cross-manifest commitment rejects','cross_manifest'),('A8 validly signed cross-component commitment rejects','cross_component')]:
        c=NEG[name]; cm=dict(COMM); cid=c['commitment_id']; cm[cid]=c
        ev=good(); ev['R5-A']=raw('R5-A',25,25,0,cid=cid)
        check(label,raises(lambda ev=ev,cm=cm:claims(ev,cm,LOGS)))

def fp72_realized():
    key='R2-B'; cid=cid_for(key); bundle=COMM[cid]; logs=LOGS[cid]
    check('B1 authentic pre-run+anchor+append+close path verifies',G.evaluate_gate(key,raw(key,100,100),bundle,logs).gate_pass)
    cm=dict(COMM); cm[cid]=NEG['close_only']
    check('B2 correct-authority close without pre-run and anchor rejects',raises(lambda:claims(good(),cm,LOGS)))
    cm=dict(COMM); cm[cid]=NEG['wrong_logger_bundle']; lg=dict(LOGS); lg[cid]=NEG['wrong_logger_logs']
    check('B3 post-outcome list signed by close authority, not frozen logger, rejects',raises(lambda:claims(good(),cm,lg)))
    # Missing/mutated pre-run or anchor.
    for label,mut in [
      ('B4 missing independent anchor rejects',lambda b:b.pop('anchor')),
      ('B5 mutated pre-run run_id rejects',lambda b:b['pre_run'].__setitem__('run_id','late-run')),
      ('B6 mutated anchor signature rejects',lambda b:b['anchor'].__setitem__('signature','00'*64)),
      ('B7 close not bound to pre-run digest rejects',lambda b:b['close'].__setitem__('pre_run_commitment_sha256','0'*64)),
    ]:
        b=copy.deepcopy(bundle); mut(b); cm=dict(COMM); cm[cid]=b
        check(label,raises(lambda cm=cm:claims(good(),cm,LOGS)))
    # Append-history attacks.
    attacks=[]
    attacks.append(('B8 truncated append history rejects',logs[:-1]))
    r=copy.deepcopy(logs); r[0],r[1]=r[1],r[0]; attacks.append(('B9 reordered append history rejects',r))
    r=copy.deepcopy(logs); r[10]=copy.deepcopy(r[9]); attacks.append(('B10 duplicate sequence rejects',r))
    r=copy.deepcopy(logs); r[5]['event']['idx']=999; attacks.append(('B11 post-signature event mutation rejects',r))
    r=copy.deepcopy(logs); r[5]['previous_chain_hash']='0'*64; attacks.append(('B12 broken append-chain link rejects',r))
    r=copy.deepcopy(logs); r[0]['observed_at']='2026-07-24T00:00:00Z'; attacks.append(('B13 event timestamp before anchor rejects',r))
    for label,l in attacks:
        lg=dict(LOGS); lg[cid]=l; check(label,raises(lambda lg=lg:claims(good(),COMM,lg)))
    b=copy.deepcopy(bundle); b['close']['realized_total']=50; cm=dict(COMM); cm[cid]=b
    check('B14 unsigned realized_total reduction rejects',raises(lambda:claims(good(),cm,LOGS)))
    lg=dict(LOGS); del lg[cid]
    check('B15 no append history rejects',raises(lambda:claims(good(),COMM,lg)))

def fp73_ids_channels():
    ev=good(); ev['R5-A']=raw('R5-A',25,25,0,cid='does-not-exist')
    check('C1 arbitrary nonempty raw commitment_id rejects',raises(lambda:claims(ev)))
    real=cid_for('R5-A'); cm=dict(COMM); cm['alias-id']=cm[real]
    ev=good(); ev['R5-A']=raw('R5-A',25,25,0,cid='alias-id')
    check('C2 alias key cannot override signed commitment_id',raises(lambda:claims(ev,cm,LOGS)))
    ev=good(); ev['R5-A']=raw('R5-A',25,25,0,cid=cid_for('R5-C'))
    check('C3 valid commitment id for another component rejects',raises(lambda:claims(ev)))
    for f,v in [('sealed_universe_n',25),('sealed_universe_inventory_hash','a'*64),('realized_total',100),('run_log_hash','a'*64),('signature','00')]:
        ev=good(); ev['R5-A' if 'realized' not in f and 'run_log' not in f else 'R2-B'][f]=v
        check('C4 raw authority field %s rejects'%f,raises(lambda ev=ev:claims(ev)))

def carried():
    ev=good(); ev['R4-C']=raw('R4-C',30,30,0)
    check('D1 fixed-universe favorable subset rejects',raises(lambda:claims(ev)))
    ev['R4-C']=raw('R4-C',30,30,0,{'universe_n':216,'excluded':[{'count':186,'reason':'not run'}]})
    comp=claims(ev)['components']['R4-C']; check('D2 reconciliation scores fixed subset over 216',comp['denominator']==216 and not comp['gate_pass'])
    ev=good(); del ev['R2-B']; check('D3 omitted committed component is INCOMPLETE',claims(ev)['routes']['R2']['claim']=='INCOMPLETE')
    ev=good(); del ev['R3-A']; check('D4 sole predeclared exclusion remains OUT OF SCOPE',claims(ev)['routes']['R3']['claim']=='OUT OF SCOPE')
    ev=good(); ev['R5-A']=raw('R5-A',25,25,1); check('D5 zero-tolerance violation dominates share',claims(ev)['routes']['R5']['claim']=='FAILED')
    ev=good(); ev['R6-A']['manifest_sha256']='0'*64; check('D6 wrong raw manifest rejects',raises(lambda:claims(ev)))
    check('D7 manifest digest is reproducible',G.MANIFEST_SHA256==hashlib.sha256(G._manifest_canonical().encode()).hexdigest())
    ev=good(); ev['R9-Z']={'x':1}; check('D8 unknown component rejects',raises(lambda:claims(ev)))

def main():
    positive(); fp71_key_boundary(); fp72_realized(); fp73_ids_channels(); carried()
    print('\n%d checks, %d failures'%(COUNT,len(FAIL)))
    if FAIL:
        for x in FAIL: print('  FAILED:',x)
    raise SystemExit(1 if FAIL else 0)
if __name__=='__main__': main()

---

# Bismillah ir-Rahman ir-Rahim
