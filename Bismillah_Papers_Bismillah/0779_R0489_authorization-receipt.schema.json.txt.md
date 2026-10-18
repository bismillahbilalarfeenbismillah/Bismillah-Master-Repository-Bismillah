# Bismillah ir-Rahman ir-Rahim

# R0489 -- authorization-receipt.schema.json.txt

**Chronological Index:** 779 of 995  
**Date:** Undated  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** authorization-receipt.schema.json.txt  
**Source Format:** txt  
**SHA-256:** `512caca6aa2ad565625d253dc307a1177f38be4c8197eb3e2778978917ab5ca7`  

---

## R0489 · authorization-receipt.schema.json.txt

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: authorization-receipt.schema.json.txt
- source_format: txt
- text_sha256: 512caca6aa2ad565625d253dc307a1177f38be4c8197eb3e2778978917ab5ca7

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:bssg:schema:0.1:authorization-receipt",
  "title": "BSSG authorization receipt (v0.1 DRAFT)",
  "description": "Issued by the decision point when and only when all five frozen conjuncts recomputed to TRUE. The receipt binds the decision to the exact request bytes, contract and policy digests, witness receipt, evidence epoch, authority epoch, nonce, and expiry, and carries a one-time commit token. The receipt is NOT permission to execute later under different conditions: the commit protocol revalidates. Status: DRAFT, NOT CARRIED.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "record_type",
    "spec_version",
    "receipt_id",
    "request_digest",
    "request_id",
    "subject_id",
    "session_id",
    "contract_digest",
    "policy_digest",
    "witness_receipt_digest",
    "evidence_epoch",
    "witness_epoch",
    "authority_epoch",
    "authority_snapshot",
    "decision",
    "conjuncts",
    "reason_codes",
    "nonce",
    "effect_type",
    "canonical_target",
    "params_digest",
    "adapter_digest",
    "commit_token",
    "issued_at_epoch_seconds",
    "signature"
  ],
  "properties": {
    "record_type": { "const": "bssg.authorization-receipt" },
    "spec_version": { "const": "0.1" },
    "receipt_id": { "$ref": "#/$defs/digest" },
    "request_digest": { "$ref": "#/$defs/digest" },
    "request_id": { "$ref": "#/$defs/identifier" },
    "subject_id": { "$ref": "#/$defs/identifier" },
    "session_id": { "$ref": "#/$defs/identifier" },
    "contract_digest": { "$ref": "#/$defs/digest" },
    "policy_digest": { "$ref": "#/$defs/digest" },
    "witness_receipt_digest": { "$ref": "#/$defs/digest" },
    "evidence_epoch": { "$ref": "#/$defs/epoch" },
    "witness_epoch": { "$ref": "#/$defs/epoch" },
    "authority_epoch": {
      "$ref": "#/$defs/epoch",
      "description": "Monotone non-decreasing. A commit whose authority epoch differs from the epoch bound here MUST fail."
    },
    "authority_snapshot": {
      "type": "object",
      "additionalProperties": false,
      "required": ["effects", "target_scopes"],
      "properties": {
        "effects": { "type": "array", "items": { "type": "string" } },
        "target_scopes": { "type": "array", "items": { "type": "string" } }
      },
      "description": "The authority ceiling in force at decision time. Degradation of witness health MUST NOT enlarge this set."
    },
    "decision": { "const": "ALLOW" },
    "conjuncts": { "$ref": "#/$defs/conjuncts" },
    "reason_codes": {
      "type": "array",
      "items": { "$ref": "#/$defs/reasonCode" },
      "maxItems": 0,
      "description": "An ALLOW receipt carries no reason codes. DENY outcomes are recorded in a decision record, not in an authorization receipt."
    },
    "nonce": { "$ref": "#/$defs/nonce" },
    "effect_type": { "type": "string" },
    "canonical_target": { "type": "string" },
    "params_digest": { "$ref": "#/$defs/digest" },
    "adapter_digest": { "$ref": "#/$defs/digest" },
    "commit_token": {
      "type": "object",
      "additionalProperties": false,
      "required": ["token_id", "one_time", "expires_at_epoch_seconds"],
      "properties": {
        "token_id": { "type": "string", "minLength": 8, "maxLength": 128 },
        "one_time": { "const": true },
        "expires_at_epoch_seconds": { "type": "integer", "minimum": 0 }
      }
    },
    "issued_at_epoch_seconds": { "type": "integer", "minimum": 0 },
    "signature": { "$ref": "#/$defs/signature" }
  },
  "$defs": {
    "identifier": { "type": "string", "pattern": "^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$" },
    "digest": { "type": "string", "pattern": "^sha256:[0-9a-f]{64}$" },
    "nonce": { "type": "string", "pattern": "^[0-9a-f]{32}$" },
    "epoch": { "type": "integer", "minimum": 0, "maximum": 9007199254740991 },
    "truthValue": { "enum": ["TRUE", "FALSE", "UNKNOWN"] },
    "conjuncts": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "ContractMatch",
        "EffectTypeValid",
        "TargetAllowed",
        "WitnessHealthy",
        "EvidenceCurrent"
      ],
      "properties": {
        "ContractMatch": { "$ref": "#/$defs/truthValue" },
        "EffectTypeValid": { "$ref": "#/$defs/truthValue" },
        "TargetAllowed": { "$ref": "#/$defs/truthValue" },
        "WitnessHealthy": { "$ref": "#/$defs/truthValue" },
        "EvidenceCurrent": { "$ref": "#/$defs/truthValue" }
      },
      "description": "Exactly the five frozen conjuncts. No sixth conjunct may appear. Commit-time revalidation is a protocol obligation recorded in the execution receipt, not an additional conjunct."
    },
    "reasonCode": { "type": "string", "pattern": "^E-[A-Z0-9-]{2,64}$" },
    "signature": {
      "type": "object",
      "additionalProperties": false,
      "required": ["alg", "kid", "envelope", "canonicalization", "verification_status"],
      "properties": {
        "alg": { "type": "string" },
        "kid": { "type": "string" },
        "envelope": { "enum": ["detached-json", "COSE_Sign1", "COSE_Sign"] },
        "canonicalization": { "const": "BSSG-CANON-1" },
        "signature_b64": { "type": "string" },
        "cose_sign1_b64": { "type": "string" },
        "verification_status": {
          "enum": [
            "verified_by_injected_verifier",
            "rejected_by_injected_verifier",
            "unknown",
            "not_performed_by_reference_gate"
          ],
          "description": "The reference implementation models signature verification through an injected verifier. It does not establish key custody, key distribution, or trust-root provenance. 'verified_by_injected_verifier' is a statement about a callable, not about a key."
        }
      }
    }
  }
}

---

# Bismillah ir-Rahman ir-Rahim
