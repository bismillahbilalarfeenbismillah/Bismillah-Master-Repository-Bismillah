# Bismillah ir-Rahman ir-Rahim

# R0209 -- xz_protocol_trust_roots_PUBLIC.json

**Chronological Index:** 111 of 995  
**Date:** 2026  
**Section:** IV. XZ Protocol  
**Source File:** xz_protocol_trust_roots_PUBLIC.json  
**Source Format:** json  
**SHA-256:** `7b6c59789025883c8ee4e24a6d6ba5e9a33693fdb5743c27ed0e2fb7c5e88722`  

---

## R0209 · xz_protocol_trust_roots_PUBLIC.json

- section: IV. XZ Protocol
- source_file: xz_protocol_trust_roots_PUBLIC.json
- source_format: json
- merged_variants: 3 (trust_roots.txt; xz_protocol_trust_roots_PUBLIC.json.txt; xz_protocol_trust_roots_PUBLIC.txt)
- text_sha256: 7b6c59789025883c8ee4e24a6d6ba5e9a33693fdb5743c27ed0e2fb7c5e88722

{
  "protocol": "XZ Protocol v0.75",
  "trust_roots": {
    "commitment-authority": {
      "role": "commitment-authority",
      "description": "Signs the universe inventory, cardinality, and sealed commitments",
      "algorithm": "Ed25519",
      "public_key_hex": "aa6ea152ee9d7d781dfbdb2f26461f092a71ef0837baee302c749c50e4889e15",
      "generated": "2026-08-07T20:00:00.000000Z"
    },
    "independent-anchor": {
      "role": "independent-anchor",
      "description": "Signs the manifest digest independently; verifies commitment integrity",
      "algorithm": "Ed25519",
      "public_key_hex": "ce5943dc59224c0fc6148ce3f960c169e59a73deb77b28c88b63a4e6120a65bc",
      "generated": "2026-08-07T20:00:00.000000Z"
    },
    "run-logger": {
      "role": "run-logger",
      "description": "Records seal events, arm outputs, and adjudication timestamps",
      "algorithm": "Ed25519",
      "public_key_hex": "f6688b09d27cd664641427b0f44450de713e88d49439213c79f50c1de9bfbb66",
      "generated": "2026-08-07T20:00:00.000000Z"
    }
  },
  "generated": "2026-08-07T20:00:00.000000Z",
  "note": "Private keys are NOT in this file. They are in the separate PRIVATE file.",
  "manifest_digest": "f2c84764afe16be02a06084d5aad83d773c31a5681806a470ec56126d0416e60",
  "manifest_digest_algorithm": "SHA-256",
  "manifest_digest_note": "SHA-256 over the concatenated sha256sum output lines of the 12 normative code files (6 modules + 6 test suites) in alphabetical filename order (excluding this trust-roots file and the protocol text). Construction: sha256sum <files alphabetically> | sha256sum.",
  "version": "0.75"
}

---

# Bismillah ir-Rahman ir-Rahim
