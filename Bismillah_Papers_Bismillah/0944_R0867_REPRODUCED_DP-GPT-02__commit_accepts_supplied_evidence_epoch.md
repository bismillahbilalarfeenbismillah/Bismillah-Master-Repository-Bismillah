# Bismillah ir-Rahman ir-Rahim

# R0867 -- REPRODUCED DP-GPT-02: commit accepts supplied evidence_epoch mismatch :: authorized=5 supplied=6 outcome=COMMITTED_PENDING_OUTCOME reasons=[]

**Chronological Index:** 944 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** run_pass3_differential_probes.txt  
**Source Format:** txt  
**SHA-256:** `76b6200aae95e24417f7bfb2407cc3c7a1b70e060b9941f77f7a43f55654117a`  

---

## R0867 · REPRODUCED DP-GPT-02: commit accepts supplied evidence_epoch mismatch :: authorized=5 supplied=6 outcome=COMMITTED_PENDING_OUTCOME reasons=[]

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: run_pass3_differential_probes.txt
- source_format: txt
- text_sha256: 76b6200aae95e24417f7bfb2407cc3c7a1b70e060b9941f77f7a43f55654117a

REPRODUCED DP-GPT-01: C1 controls reach canonicalization and ALLOW :: accepted=['U+0080', 'U+0081', 'U+0082', 'U+0083', 'U+0084', 'U+0086', 'U+0087', 'U+0088', 'U+0089', 'U+008A', 'U+008B', 'U+008C', 'U+008D', 'U+008E', 'U+008F', 'U+0090', 'U+0091', 'U+0092', 'U+0093', 'U+0094', 'U+0095', 'U+0096', 'U+0097', 'U+0098', 'U+0099', 'U+009A', 'U+009B', 'U+009C', 'U+009D', 'U+009E', 'U+009F']; decision=ALLOW; canonical='https://db.example.internal/records/row\x80x'
REPRODUCED DP-GPT-02: commit accepts supplied evidence_epoch mismatch :: authorized=5 supplied=6 outcome=COMMITTED_PENDING_OUTCOME reasons=[]
REPRODUCED DP-GPT-03: commit accepts fresh witness within subject authority :: outcome=COMMITTED_PENDING_OUTCOME reasons=[]
REPRODUCED DP-GPT-04: commit accepts fresh witness observed in the future :: outcome=COMMITTED_PENDING_OUTCOME reasons=[]
REPRODUCED DP-GPT-05: cross-epoch sequence reset is accepted, then next sequence is rejected :: d1=ALLOW d2=ALLOW d3=DENY_FALSE/['E-EFFECT-ABOVE-CEILING', 'E-FALSE-TARGETALLOWED', 'E-FALSE-WITNESSHEALTHY', 'E-WITNESS-SEQUENCE-ROLLBACK'] stored_seq=11
REPRODUCED DP-GPT-06: commit accepts after contract body no longer matches bound digest/authority :: outcome=COMMITTED_PENDING_OUTCOME reasons=[] digest_mismatch=True
REPRODUCED DP-GPT-07: commit accepts supplied invalid time-authority signature :: outcome=COMMITTED_PENDING_OUTCOME reasons=[]
REPRODUCED DP-GPT-08: malformed contract registry entry crashes authorize :: KeyError: 'body'
REPRODUCED DP-GPT-09: commit succeeds after the bound contract expires :: authorize=ALLOW commit=COMMITTED_PENDING_OUTCOME reasons=[]
REPRODUCED DP-GPT-10: older epoch/sequence is accepted after newer commit evidence was supplied :: commit=COMMITTED_PENDING_OUTCOME later=ALLOW/[] stored_epoch=5 stored_seq=11

SUMMARY reproduced=10/10

---

# Bismillah ir-Rahman ir-Rahim
