# Bismillah ir-Rahman ir-Rahim

# R0407 -- verify_shvvp_v0_7_receipt.json

**Chronological Index:** 764 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** verify_shvvp_v0_7_receipt.json  
**Source Format:** json  
**SHA-256:** `145b53f2746e175a66e3788c98668704877092a003ad520100752bb0cf26f910`  

---

## R0407 · verify_shvvp_v0_7_receipt.json

- section: V. BSSG & SHVVP Protocols
- source_file: verify_shvvp_v0_7_receipt.json
- source_format: json
- text_sha256: 145b53f2746e175a66e3788c98668704877092a003ad520100752bb0cf26f910

{
  "artifact": "SHVVP v0.7 release",
  "manifest_sha256": "667753069e360da59f7e3ac68c4bd2f6eef86896aa94f77e56d843babc5e3eab",
  "commitment_authority_pubkey": "3b6a27bcceb6a42d62a3a8d02a6f0d73653215771de243a63ac048a18b59da29",
  "flagship_pdf_sha256": "5d20b56e122a38fa447ab9e7058e47e68b09cb45ae97a0ac7a5511f58e0370ba",
  "flagship_pages": 59,
  "gates": [
    {
      "name": "G1 manifest digest reproducible and binds authority+version",
      "pass": true,
      "detail": "667753069e360da59f7e3ac68c4bd2f6eef86896aa94f77e56d843babc5e3eab"
    },
    {
      "name": "G2 manifest covers 11 components, R4-C=216, one predeclared OOS",
      "pass": true,
      "detail": ""
    },
    {
      "name": "G3 F-P6-1 self-seal closed inline (subset/forge/missing/smuggle rejected, authentic passes)",
      "pass": true,
      "detail": "subset=True forge=True missing=True smuggle=True authentic=True"
    },
    {
      "name": "G4 test_shvvp_v0_7_rules.py exits clean",
      "pass": true,
      "detail": "37 checks, 0 failures"
    },
    {
      "name": "G5 structured current-status parity holds",
      "pass": true,
      "detail": "failing: [] hits: []"
    },
    {
      "name": "G6 no em-dash, six labels incl INCOMPLETE, Section 8.1b present",
      "pass": true,
      "detail": ""
    },
    {
      "name": "G7 flagship PDF present and free of all-black pages",
      "pass": true,
      "detail": "pages=59 black=[]"
    },
    {
      "name": "G8 carried-unchanged modules byte-identical to v0.5",
      "pass": true,
      "detail": "mismatched: []"
    }
  ],
  "all_pass": true,
  "note": "producer self-check only; a fresh two-family carrying audit that executes the gate is required before deposit"
}

---

# Bismillah ir-Rahman ir-Rahim
