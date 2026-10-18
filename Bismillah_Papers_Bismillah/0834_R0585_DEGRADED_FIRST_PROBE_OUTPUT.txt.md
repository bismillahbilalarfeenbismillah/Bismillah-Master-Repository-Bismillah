# Bismillah ir-Rahman ir-Rahim

# R0585 -- DEGRADED_FIRST_PROBE_OUTPUT.txt

**Chronological Index:** 834 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** DEGRADED_FIRST_PROBE_OUTPUT.txt  
**Source Format:** txt  
**SHA-256:** `65d88c5814a45cc741f4971b68f588fc315871945a8bda404f0cddd372da6d59`  

---

## R0585 · DEGRADED_FIRST_PROBE_OUTPUT.txt

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: DEGRADED_FIRST_PROBE_OUTPUT.txt
- source_format: txt
- text_sha256: 65d88c5814a45cc741f4971b68f588fc315871945a8bda404f0cddd372da6d59

{
  "VERDICT": "DEGRADED-FIRST BYPASS REPRODUCED",
  "commit": {
    "adapter_digest": "sha256:21bdc47378b816436b33def0f9dc27dacdacf2709c3d296e6d8582a2ac4b90b6",
    "authorization_receipt_digest": "sha256:77da33ecba2fd34daff0927b3f29b41cebc3d2f540ad86b91a5b953613ffd12c",
    "commit_time_epoch_seconds": 1784980800,
    "commit_token_id": "token-00000002",
    "executed_params_digest": "sha256:b34e9edcb0fe92814cc862d7121d25a777887797443b6c09dbd444d213ef6793",
    "executed_target_canonical": "https://db.example.internal/records/row-1",
    "execution_id": "sha256:1d5baccec9a4fd10e5e7fea497bda424735386c63ef0e146a96443a3ad916c3c",
    "outcome": "COMMITTED_PENDING_OUTCOME",
    "reason_codes": [],
    "record_type": "bssg.execution-receipt",
    "request_digest": "sha256:649bffee56211944249316283e84c14f5c2e3df84af8512162d96502762ce883",
    "revalidation": {
      "authority_epoch": 3,
      "evidence_epoch": 9,
      "result": "PASS",
      "witness_epoch": 9
    },
    "signature": {
      "alg": "unsigned-reference",
      "canonicalization": "BSSG-CANON-1",
      "envelope": "detached-json",
      "kid": "reference-gate",
      "verification_status": "not_performed_by_reference_gate"
    },
    "spec_version": "0.1"
  },
  "lift": {
    "accepted": true,
    "authority_epoch": 2,
    "reason_codes": []
  },
  "r1_degraded_read": {
    "ceiling_value": {
      "effects": [
        "READ"
      ],
      "target_scopes": [
        "https://db.example.internal/records/"
      ]
    },
    "contract_ceiling_present": false,
    "contract_ceiling_value": "ABSENT",
    "decision": "ALLOW",
    "tokens": [
      "token-00000001"
    ]
  },
  "r2_healthy_delete_widening": {
    "decision": "DENY_FALSE",
    "reasons": [
      "E-AUTHORITY-WIDENING",
      "E-FALSE-CONTRACTMATCH",
      "E-FALSE-EFFECTTYPEVALID",
      "E-FALSE-EVIDENCECURRENT",
      "E-FALSE-TARGETALLOWED",
      "E-FALSE-WITNESSHEALTHY"
    ],
    "terminal_session": "no_such_attr"
  },
  "r3_healthy_delete_after_lift": {
    "decision": "ALLOW",
    "has_receipt": true,
    "reasons": []
  }
}

---

# Bismillah ir-Rahman ir-Rahim
