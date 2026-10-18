# Bismillah ir-Rahman ir-Rahim

# R0505 -- effect-request.schema.json.txt

**Chronological Index:** 789 of 995  
**Date:** Undated  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** effect-request.schema.json.txt  
**Source Format:** txt  
**SHA-256:** `7885bac402e9d58d2ca07823cdfa5e3dd70e68078dff9d4ef4512f8f33acd280`  

---

## R0505 · effect-request.schema.json.txt

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: effect-request.schema.json.txt
- source_format: txt
- text_sha256: 7885bac402e9d58d2ca07823cdfa5e3dd70e68078dff9d4ef4512f8f33acd280

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:bssg:schema:0.1:effect-request",
  "title": "BSSG effect request (v0.1 DRAFT)",
  "description": "A request by a subject for a consequential effect. This record carries ONLY raw evidence and declarations. It MUST NOT carry any derived authorization fact: no decision, no conjunct value, no 'verified' or 'within_auth' flag. A gate that accepts such a field from a caller has surrendered authority to the caller. Status: DRAFT, NOT CARRIED. No effectiveness claim attaches to this schema.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "record_type",
    "spec_version",
    "request_id",
    "subject_id",
    "session_id",
    "contract_digest",
    "policy_digest",
    "effect_type",
    "target",
    "params_digest",
    "adapter_digest",
    "nonce",
    "sequence",
    "issued_at",
    "expires_at"
  ],
  "properties": {
    "record_type": {
      "const": "bssg.effect-request"
    },
    "spec_version": {
      "$ref": "#/$defs/specVersion"
    },
    "request_id": {
      "$ref": "#/$defs/identifier",
      "description": "Unique identifier for this request. Uniqueness is asserted by the issuer and is not established by this schema."
    },
    "subject_id": {
      "$ref": "#/$defs/identifier",
      "description": "The acting system. Untrusted for all derived facts."
    },
    "session_id": {
      "$ref": "#/$defs/identifier"
    },
    "contract_digest": {
      "$ref": "#/$defs/digest",
      "description": "Digest over the canonical bytes (BSSG-CANON-1) of the contract body. The gate MUST recompute this digest rather than trust it."
    },
    "policy_digest": {
      "$ref": "#/$defs/digest"
    },
    "effect_type": {
      "type": "string",
      "pattern": "^[A-Z][A-Z0-9_]{1,63}$",
      "description": "A member of the contract's closed effect registry. Membership is checked by the gate, not by this schema."
    },
    "target": {
      "type": "object",
      "additionalProperties": false,
      "required": ["declared_uri", "canonical_uri", "target_class"],
      "properties": {
        "declared_uri": {
          "type": "string",
          "minLength": 1,
          "maxLength": 2048
        },
        "canonical_uri": {
          "type": "string",
          "minLength": 1,
          "maxLength": 2048,
          "description": "The subject's claim about the canonical form. The gate MUST recompute canonicalization and MUST treat a mismatch as FALSE and an uncanonicalizable target as UNKNOWN."
        },
        "target_class": {
          "type": "string",
          "pattern": "^[a-z][a-z0-9_.-]{1,63}$"
        }
      }
    },
    "params_digest": {
      "$ref": "#/$defs/digest",
      "description": "Digest over the canonical bytes of the effect parameters. Parameters themselves are transported out of band; the authorization binds only the digest."
    },
    "adapter_digest": {
      "$ref": "#/$defs/digest",
      "description": "Digest of the executor adapter that will perform the effect."
    },
    "nonce": {
      "$ref": "#/$defs/nonce"
    },
    "sequence": {
      "type": "integer",
      "minimum": 0,
      "maximum": 9007199254740991
    },
    "issued_at": {
      "$ref": "#/$defs/timestamp"
    },
    "expires_at": {
      "$ref": "#/$defs/timestamp"
    }
  },
  "$defs": {
    "specVersion": {
      "const": "0.1"
    },
    "identifier": {
      "type": "string",
      "pattern": "^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$"
    },
    "digest": {
      "type": "string",
      "pattern": "^sha256:[0-9a-f]{64}$",
      "description": "Lowercase hex SHA-256 over BSSG-CANON-1 canonical bytes. Hash agility is an OPEN DECISION (OD-4)."
    },
    "nonce": {
      "type": "string",
      "pattern": "^[0-9a-f]{32}$"
    },
    "timestamp": {
      "type": "string",
      "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$",
      "description": "RFC 3339 UTC with second precision and a literal Z. Any other lexical form MUST be treated as malformed, never coerced."
    }
  }
}

---

# Bismillah ir-Rahman ir-Rahim
