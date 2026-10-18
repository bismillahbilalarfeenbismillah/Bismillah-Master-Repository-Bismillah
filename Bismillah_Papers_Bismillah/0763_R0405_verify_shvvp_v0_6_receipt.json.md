# Bismillah ir-Rahman ir-Rahim

# R0405 -- verify_shvvp_v0_6_receipt.json

**Chronological Index:** 763 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** verify_shvvp_v0_6_receipt.json  
**Source Format:** json  
**SHA-256:** `5a77b22e3406db3ccd577a05bda98203a2ea32b9a6d3a0b69fa800812ddb9127`  

---

## R0405 · verify_shvvp_v0_6_receipt.json

- section: V. BSSG & SHVVP Protocols
- source_file: verify_shvvp_v0_6_receipt.json
- source_format: json
- text_sha256: 5a77b22e3406db3ccd577a05bda98203a2ea32b9a6d3a0b69fa800812ddb9127

{
  "artifact": "SHVVP v0.6 release",
  "manifest_sha256": "505bfc026b2896b5fbe65e5726874c95430838b86d431074c4946ace07d91831",
  "flagship_pdf_sha256": "37d0e5172a838b746798c23e79c1604e9c6afb96cea49f0b4c6da6c7a3793a1a",
  "flagship_pages": 56,
  "gates": [
    {
      "name": "G1 manifest digest reproducible",
      "pass": true,
      "detail": "505bfc026b2896b5fbe65e5726874c95430838b86d431074c4946ace07d91831"
    },
    {
      "name": "G2 manifest covers 11 components, R4-C universe = 216",
      "pass": true,
      "detail": ""
    },
    {
      "name": "G3 F-P5-1 attacks a/b/c closed and R3 OOS preserved",
      "pass": true,
      "detail": "a=True b=True c=True r3=True"
    },
    {
      "name": "G4 test_shvvp_v0_6_rules.py exits clean",
      "pass": true,
      "detail": "62 checks, 0 failures"
    },
    {
      "name": "G5 no em-dash and no live stale version reference",
      "pass": true,
      "detail": "stale: []"
    },
    {
      "name": "G6 source declares v0.6 and the six-label list",
      "pass": true,
      "detail": ""
    },
    {
      "name": "G7 flagship PDF present and free of all-black pages",
      "pass": true,
      "detail": "black pages: []"
    },
    {
      "name": "G8 carried-unchanged modules byte-identical to v0.5",
      "pass": true,
      "detail": "mismatched: []"
    }
  ],
  "all_pass": true,
  "note": "producer self-check only; a fresh two-family carrying audit is required before deposit"
}

---

# Bismillah ir-Rahman ir-Rahim
