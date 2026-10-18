# Bismillah ir-Rahman ir-Rahim

# R0410 -- verify_shvvp_v0_8_rc1_receipt.json

**Chronological Index:** 347 of 995  
**Date:** 2026-07-24  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** verify_shvvp_v0_8_rc1_receipt.json  
**Source Format:** json  
**SHA-256:** `75da2cee01351d3a1f7930c0ac49c09d171540042c94d1a4f4ad46e131a16b45`  

---

## R0410 · verify_shvvp_v0_8_rc1_receipt.json

- section: V. BSSG & SHVVP Protocols
- source_file: verify_shvvp_v0_8_rc1_receipt.json
- source_format: json
- text_sha256: 75da2cee01351d3a1f7930c0ac49c09d171540042c94d1a4f4ad46e131a16b45

{
  "artifact": "SHVVP v0.8-rc1 revision candidate",
  "candidate_date": "2026-07-24",
  "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
  "authorities": {
    "commitment": "b603204916623ec030e6ba851a321dc67f6a00c7a28bee1d878d0a71a611c251",
    "logger": "8d8dab152398183082c0461ece15d06a58528c1e6df942c153d2cc024bba28a0",
    "anchor": "0ebc3b1e23207fd41eef3f519983c5eae76efdd9555d8ec142b7eba3b64e2a73"
  },
  "source_sha256": "822149b725492bedf52f35f4b43166c7ab9c2f01c76e01bf06fb7af51dc57ba1",
  "pdf_sha256": "4857ab26c4d91168ac8e53b3fa6080543ee0b397883310c820b70a1ae8885d70",
  "pdf_pages": 61,
  "tests_tail": "44 checks, 0 failures",
  "gates": [
    {
      "name": "G1 manifest digest reproducible and binds all three authorities",
      "pass": true,
      "detail": ""
    },
    {
      "name": "G2 public route interface has no trust-root override",
      "pass": true,
      "detail": "(raw_evidence: 'Mapping[str, Any]', commitments: 'Mapping[str, Any] | None' = None, run_logs: 'Mapping[str, Any] | None' = None) -> 'dict'"
    },
    {
      "name": "G3 signed vectors match manifest and fixed keys",
      "pass": true,
      "detail": ""
    },
    {
      "name": "G4 adversarial regression suite exits clean",
      "pass": true,
      "detail": "44 checks, 0 failures"
    },
    {
      "name": "G5 candidate identity is internally explicit",
      "pass": true,
      "detail": ""
    },
    {
      "name": "G6 F-P7 repairs are represented in source",
      "pass": true,
      "detail": ""
    },
    {
      "name": "G7 no stale current-contract denominator/version phrase remains",
      "pass": true,
      "detail": "[]"
    },
    {
      "name": "G8 code contains no trusted_pubkey interface",
      "pass": true,
      "detail": ""
    },
    {
      "name": "G9 no Unicode en/em dash in current artifacts",
      "pass": true,
      "detail": ""
    },
    {
      "name": "G10 PDF is 61 pages and has no all-black page",
      "pass": true,
      "detail": "pages=61 black=[]"
    },
    {
      "name": "G11 signed vectors contain no private-key or seed field",
      "pass": true,
      "detail": "[]"
    },
    {
      "name": "G12 carried unchanged v0.5 modules are present",
      "pass": true,
      "detail": ""
    }
  ],
  "all_pass": true,
  "note": "Producer self-check only. Candidate is not frozen or carried."
}

---

# Bismillah ir-Rahman ir-Rahim
