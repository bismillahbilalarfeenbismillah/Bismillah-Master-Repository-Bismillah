# Bismillah ir-Rahman ir-Rahim

# R0646 -- HUNT_35TH_OUTPUT.txt

**Chronological Index:** 854 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** HUNT_35TH_OUTPUT.txt  
**Source Format:** txt  
**SHA-256:** `43635c924488281aa2958209d496223547809e021d7ce54e429d84cebde9e244`  

---

## R0646 · HUNT_35TH_OUTPUT.txt

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: HUNT_35TH_OUTPUT.txt
- source_format: txt
- text_sha256: 43635c924488281aa2958209d496223547809e021d7ce54e429d84cebde9e244

{
  "hypothesis_1_reference_capture_race": {
    "r1_healthy_read": {
      "decision": "ALLOW",
      "contract_ceiling": {
        "effects": [
          "DELETE",
          "READ"
        ],
        "target_scopes": [
          "https://db.example.internal/records/"
        ]
      }
    },
    "r2_healthy_delete_same_session": {
      "decision": "DENY_FALSE",
      "reasons": [
        "E-EFFECT-ABOVE-CEILING",
        "E-EFFECT-NOT-REGISTERED",
        "E-FALSE-EFFECTTYPEVALID",
        "E-FALSE-TARGETALLOWED"
      ]
    },
    "VERDICT": "NOT REPRODUCED (class fix + kernel constrained by contract)"
  }
}

---

# Bismillah ir-Rahman ir-Rahim
