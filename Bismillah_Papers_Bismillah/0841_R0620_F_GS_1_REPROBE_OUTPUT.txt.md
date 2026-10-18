# Bismillah ir-Rahman ir-Rahim

# R0620 -- F_GS_1_REPROBE_OUTPUT.txt

**Chronological Index:** 841 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** F_GS_1_REPROBE_OUTPUT.txt  
**Source Format:** txt  
**SHA-256:** `11d7eb5fff6d54d74f2272b1944e763f710d63505ef5ba2cd984ad0f9e32fec6`  

---

## R0620 · F_GS_1_REPROBE_OUTPUT.txt

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: F_GS_1_REPROBE_OUTPUT.txt
- source_format: txt
- text_sha256: 11d7eb5fff6d54d74f2272b1944e763f710d63505ef5ba2cd984ad0f9e32fec6

{
  "commit": null,
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
    "authority_snapshot": null,
    "decision": "DENY_FALSE",
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
      "effects": [],
      "target_scopes": []
    }
  }
}

---

# Bismillah ir-Rahman ir-Rahim
