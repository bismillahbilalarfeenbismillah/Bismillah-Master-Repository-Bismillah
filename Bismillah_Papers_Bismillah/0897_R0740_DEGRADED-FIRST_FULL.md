# Bismillah ir-Rahman ir-Rahim

# R0740 -- DEGRADED-FIRST FULL

**Chronological Index:** 897 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** PROBE_REPLAYS_FULL.txt  
**Source Format:** txt  
**SHA-256:** `2f3323d01a41ac81f2b9e1b736fb954e53bfad2f008c7de164f5fe9bcca409e6`  

---

## R0740 · DEGRADED-FIRST FULL

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: PROBE_REPLAYS_FULL.txt
- source_format: txt
- text_sha256: 2f3323d01a41ac81f2b9e1b736fb954e53bfad2f008c7de164f5fe9bcca409e6

=== DEGRADED-FIRST FULL ===
{
  "VERDICT": "NOT REPRODUCED",
  "commit": null,
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
    "contract_ceiling_present": true,
    "contract_ceiling_value": {
      "effects": [],
      "target_scopes": []
    },
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
    "decision": "DENY_FALSE",
    "has_receipt": false,
    "reasons": [
      "E-AUTHORITY-WIDENING",
      "E-FALSE-CONTRACTMATCH",
      "E-FALSE-EFFECTTYPEVALID",
      "E-FALSE-EVIDENCECURRENT",
      "E-FALSE-TARGETALLOWED",
      "E-FALSE-WITNESSHEALTHY"
    ]
  }
}

=== A-05 FULL ===
{
  "VERDICT": "A-05 NOT REPRODUCED",
  "commit": null,
  "lift": {
    "accepted": true,
    "authority_epoch": 3,
    "reason_codes": []
  },
  "r1_healthy_read_with_ceiling_write_failure": {
    "decision": "ALLOW",
    "has_authorization_receipt": true,
    "issuance_status": null,
    "reasons": []
  },
  "r2_degraded_read": {
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
    "decision": "DENY_FALSE",
    "has_authorization_receipt": false,
    "issuance_status": null,
    "reasons": [
      "E-AUTHORITY-WIDENING",
      "E-FALSE-CONTRACTMATCH",
      "E-FALSE-EFFECTTYPEVALID",
      "E-FALSE-EVIDENCECURRENT",
      "E-FALSE-TARGETALLOWED",
      "E-FALSE-WITNESSHEALTHY"
    ]
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
    "contract_ceiling_present": true,
    "contract_ceiling_value": {
      "effects": [],
      "target_scopes": []
    },
    "tokens_present": [
      "token-00000001"
    ]
  }
}

=== MINT-FAULT FULL ===
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
