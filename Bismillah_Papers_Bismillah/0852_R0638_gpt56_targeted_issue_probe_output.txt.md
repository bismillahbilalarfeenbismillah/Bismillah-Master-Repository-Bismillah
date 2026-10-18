# Bismillah ir-Rahman ir-Rahim

# R0638 -- gpt56_targeted_issue_probe_output.txt

**Chronological Index:** 852 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** gpt56_targeted_issue_probe_output.txt  
**Source Format:** txt  
**SHA-256:** `0ac20daea55b0e8aa1d2344b172e70c356441ad5acdc693186446fce811bfb25`  

---

## R0638 · gpt56_targeted_issue_probe_output.txt

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: gpt56_targeted_issue_probe_output.txt
- source_format: txt
- merged_variants: 1 (A05_PROBE_OUTPUT.txt)
- text_sha256: 0ac20daea55b0e8aa1d2344b172e70c356441ad5acdc693186446fce811bfb25

{
  "commit": {
    "adapter_digest": "sha256:21bdc47378b816436b33def0f9dc27dacdacf2709c3d296e6d8582a2ac4b90b6",
    "authorization_receipt_digest": "sha256:6891ffee490d9755137ca2ada4855aa5937b713eacfe7c1089fafa521e23e93d",
    "commit_time_epoch_seconds": 1784980800,
    "commit_token_id": "token-00000002",
    "executed_params_digest": "sha256:b34e9edcb0fe92814cc862d7121d25a777887797443b6c09dbd444d213ef6793",
    "executed_target_canonical": "https://db.example.internal/records/row-1",
    "execution_id": "sha256:1d5baccec9a4fd10e5e7fea497bda424735386c63ef0e146a96443a3ad916c3c",
    "outcome": "COMMITTED_PENDING_OUTCOME",
    "reason_codes": [],
    "record_type": "bssg.execution-receipt",
    "request_digest": "sha256:ad8116a69a2aa147d9717701ece7a4f23038698590cb030c76a08623d8bb1164",
    "revalidation": {
      "authority_epoch": 4,
      "evidence_epoch": 10,
      "result": "PASS",
      "witness_epoch": 10
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
    "authority_epoch": 3,
    "reason_codes": []
  },
  "r1_mint_fault": {
    "decision": "ALLOW",
    "issuance_status": "FAILED_NO_EFFECT",
    "reasons": [
      "E-TOKEN-MINT-FAULT"
    ]
  },
  "r2_degraded_read": {
    "authority_snapshot": {
      "effects": [
        "READ"
      ],
      "target_scopes": [
        "https://db.example.internal/records/"
      ]
    },
    "decision": "ALLOW",
    "issuance_status": null
  },
  "r3_healthy_delete_before_lift": {
    "decision": "DENY_FALSE",
    "reasons": [
      "E-AUTHORITY-WIDENING",
      "E-FALSE-CONTRACTMATCH",
      "E-FALSE-EFFECTTYPEVALID",
      "E-FALSE-EVIDENCECURRENT",
      "E-FALSE-TARGETALLOWED",
      "E-FALSE-WITNESSHEALTHY"
    ]
  },
  "r4_healthy_delete_after_lift": {
    "authority_snapshot": {
      "effects": [
        "DELETE",
        "READ",
        "WRITE"
      ],
      "target_scopes": [
        "https://db.example.internal/records/"
      ]
    },
    "decision": "ALLOW",
    "issuance_status": null
  },
  "state_after_r1": {
    "ceiling": {
      "effects": [
        "DELETE",
        "READ",
        "WRITE"
      ],
      "target_scopes": [
        "https://db.example.internal/records/"
      ]
    },
    "contract_ceiling": {
      "effects": [
        "DELETE",
        "READ",
        "WRITE"
      ],
      "target_scopes": [
        "https://db.example.internal/records/"
      ]
    }
  }
}

---

# Bismillah ir-Rahman ir-Rahim
