# Bismillah ir-Rahman ir-Rahim

# R0506 -- execution-receipt.schema.json.txt

**Chronological Index:** 790 of 995  
**Date:** Undated  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** execution-receipt.schema.json.txt  
**Source Format:** txt  
**SHA-256:** `398741899bf781f927c8e7269abeb0f7029ac4f3399a18a4fd4a8ef7d9b419cb`  

---

## R0506 · execution-receipt.schema.json.txt

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: execution-receipt.schema.json.txt
- source_format: txt
- merged_variants: 1 (execution-receipt.schema.json)
- text_sha256: 398741899bf781f927c8e7269abeb0f7029ac4f3399a18a4fd4a8ef7d9b419cb

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:bssg:schema:0.1:execution-receipt",
  "title": "BSSG execution receipt (v0.1 DRAFT)",
  "description": "The record of a commit attempt. Commit is the point at which a one-time token is redeemed under compare-and-swap and all bindings and epochs are revalidated. A commit receipt records that the protocol obligation was discharged; it does not assert that the external target actually performed the effect. Unknown remote outcomes MUST be recorded as INDETERMINATE and MUST NOT be retried blindly. Status: DRAFT, NOT CARRIED.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "record_type",
    "spec_version",
    "execution_id",
    "commit_token_id",
    "authorization_receipt_digest",
    "request_digest",
    "executed_target_canonical",
    "executed_params_digest",
    "adapter_digest",
    "outcome",
    "commit_time_epoch_seconds",
    "revalidation",
    "reason_codes",
    "signature"
  ],
  "properties": {
    "record_type": {
      "const": "bssg.execution-receipt"
    },
    "spec_version": {
      "const": "0.1"
    },
    "execution_id": {
      "$ref": "#/$defs/nullableDigest"
    },
    "commit_token_id": {
      "oneOf": [
        {
          "type": "string",
          "minLength": 8,
          "maxLength": 128
        },
        {
          "type": "null"
        }
      ]
    },
    "authorization_receipt_digest": {
      "$ref": "#/$defs/nullableDigest"
    },
    "request_digest": {
      "$ref": "#/$defs/nullableDigest"
    },
    "executed_target_canonical": {
      "oneOf": [
        {
          "type": "string",
          "minLength": 1
        },
        {
          "type": "null"
        }
      ],
      "description": "MUST equal the canonical target bound in the authorization receipt. Any difference is a binding violation, not a widening to be tolerated."
    },
    "executed_params_digest": {
      "$ref": "#/$defs/nullableDigest"
    },
    "adapter_digest": {
      "$ref": "#/$defs/nullableDigest"
    },
    "outcome": {
      "enum": [
        "COMMITTED_PENDING_OUTCOME",
        "SUCCEEDED",
        "FAILED_NO_EFFECT",
        "INDETERMINATE",
        "QUARANTINED"
      ]
    },
    "commit_time_epoch_seconds": {
      "type": [
        "integer",
        "null"
      ],
      "minimum": 0,
      "description": "Commit time in epoch seconds; null only on a fault path where the clock was unavailable (see reason E-CLOCK-UNAVAILABLE)."
    },
    "revalidation": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "result"
      ],
      "properties": {
        "result": {
          "enum": [
            "PASS",
            "FAIL",
            "UNKNOWN"
          ]
        },
        "authority_epoch": {
          "$ref": "#/$defs/epoch"
        },
        "evidence_epoch": {
          "$ref": "#/$defs/epoch"
        },
        "witness_epoch": {
          "$ref": "#/$defs/epoch"
        },
        "revalidated_at_epoch_seconds": {
          "type": "integer",
          "minimum": 0
        }
      },
      "description": "Commit-time revalidation is a protocol obligation around the frozen five-conjunct kernel. It is not a sixth conjunct and MUST NOT be written into the frozen equation."
    },
    "reason_codes": {
      "type": "array",
      "items": {
        "type": "string",
        "pattern": "^E-[A-Z0-9-]{2,64}$"
      }
    },
    "signature": {
      "$ref": "#/$defs/signature"
    }
  },
  "$defs": {
    "epoch": {
      "type": "integer",
      "minimum": 0,
      "maximum": 9007199254740991
    },
    "nullableDigest": {
      "oneOf": [
        {
          "type": "string",
          "pattern": "^sha256:[0-9a-f]{64}$"
        },
        {
          "type": "null"
        }
      ]
    },
    "signature": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "alg",
        "kid",
        "envelope",
        "canonicalization"
      ],
      "properties": {
        "alg": {
          "type": "string"
        },
        "kid": {
          "type": "string"
        },
        "envelope": {
          "enum": [
            "detached-json",
            "COSE_Sign1",
            "COSE_Sign"
          ]
        },
        "canonicalization": {
          "const": "BSSG-CANON-1"
        },
        "signature_b64": {
          "type": "string"
        },
        "cose_sign1_b64": {
          "type": "string"
        },
        "verification_status": {
          "enum": [
            "verified_by_injected_verifier",
            "rejected_by_injected_verifier",
            "unknown",
            "not_performed_by_reference_gate"
          ]
        }
      }
    }
  }
}

---

# Bismillah ir-Rahman ir-Rahim
