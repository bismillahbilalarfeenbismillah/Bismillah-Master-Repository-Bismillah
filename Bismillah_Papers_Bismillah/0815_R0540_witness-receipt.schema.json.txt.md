# Bismillah ir-Rahman ir-Rahim

# R0540 -- witness-receipt.schema.json.txt

**Chronological Index:** 815 of 995  
**Date:** Undated  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** witness-receipt.schema.json.txt  
**Source Format:** txt  
**SHA-256:** `8bf30f505e1ff7ee21276bf631430adbd3d44706332e4a6d75079b27fabbc054`  

---

## R0540 · witness-receipt.schema.json.txt

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: witness-receipt.schema.json.txt
- source_format: txt
- text_sha256: 8bf30f505e1ff7ee21276bf631430adbd3d44706332e4a6d75079b27fabbc054

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:bssg:schema:0.1:witness-receipt",
  "title": "BSSG witness receipt (v0.1 DRAFT)",
  "description": "A signed statement by a witness about its own observed state and its coverage of a subject. A witness receipt attests observation and consistency with the witness's own prior state. It does NOT attest that the subject behaved correctly, that the witness is honest, or that the evidence is independent. WitnessHealthy MUST NOT be read as witness honesty. Status: DRAFT, NOT CARRIED.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "record_type",
    "spec_version",
    "witness_id",
    "covered_subject",
    "covered_subject_domain",
    "independence_declaration",
    "within_auth_assessment",
    "epoch",
    "sequence",
    "checkpoint",
    "health",
    "observed_at",
    "expires_at",
    "signature"
  ],
  "properties": {
    "record_type": { "const": "bssg.witness-receipt" },
    "spec_version": { "const": "0.1" },
    "witness_id": { "$ref": "#/$defs/identifier" },
    "covered_subject": { "$ref": "#/$defs/identifier" },
    "covered_subject_domain": {
      "type": "string",
      "minLength": 1,
      "description": "The administrative control domain of the covered subject, as declared by the witness."
    },
    "covered_effect_classes": {
      "type": "array",
      "items": { "type": "string" }
    },
    "independence_declaration": {
      "type": "object",
      "additionalProperties": false,
      "required": ["control_domain", "subject_can_administer", "basis"],
      "properties": {
        "control_domain": { "type": "string", "minLength": 1 },
        "subject_can_administer": {
          "enum": [true, false, "unknown"],
          "description": "Whether the subject or its transitive administrators can write, truncate, fork, sign for, reconfigure, or roll back this witness. Only an explicit false is admissible; true and 'unknown' MUST yield UNKNOWN at the gate. This is a DECLARATION and cannot be derived from a signature."
        },
        "basis": {
          "type": "string",
          "description": "How the declaration was established: control-graph review identifier, operator attestation, or 'undetermined'."
        },
        "control_graph_ref": { "type": "string" }
      }
    },
    "within_auth_assessment": {
      "type": "object",
      "additionalProperties": false,
      "required": ["value", "method", "assessor"],
      "properties": {
        "value": {
          "enum": ["outside_subject_authority", "within_subject_authority", "unknown"],
          "description": "The WithinAuth control predicate of AX-SH 5, carried as an assessment. Evidence independence is an assumption plus a verified relation; it is NOT derivable from a valid signature."
        },
        "method": { "type": "string" },
        "assessor": { "type": "string" },
        "assessed_at": { "$ref": "#/$defs/timestamp" }
      }
    },
    "epoch": { "$ref": "#/$defs/epoch" },
    "sequence": { "$ref": "#/$defs/epoch" },
    "checkpoint": {
      "type": "object",
      "additionalProperties": false,
      "required": ["origin", "tree_size", "root_hash"],
      "properties": {
        "origin": { "type": "string", "minLength": 1 },
        "tree_size": { "$ref": "#/$defs/epoch" },
        "root_hash": { "$ref": "#/$defs/digest" },
        "previous_root_hash": { "$ref": "#/$defs/digest" }
      },
      "description": "Checkpoint state permitting fork DETECTION by comparison across observers. Detection is not prevention."
    },
    "health": {
      "enum": ["HEALTHY", "DEGRADED", "FAILED", "UNKNOWN"],
      "description": "An availability and self-consistency signal. HEALTHY does not imply honesty, correctness, or non-collusion."
    },
    "health_reason": { "type": "string" },
    "observed_at": { "$ref": "#/$defs/timestamp" },
    "expires_at": {
      "$ref": "#/$defs/timestamp",
      "description": "End of the health lease. A gate MUST NOT reuse a lapsed lease."
    },
    "time_authority_id": { "type": "string" },
    "signature": { "$ref": "#/$defs/signature" }
  },
  "$defs": {
    "identifier": { "type": "string", "pattern": "^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$" },
    "digest": { "type": "string", "pattern": "^sha256:[0-9a-f]{64}$" },
    "epoch": { "type": "integer", "minimum": 0, "maximum": 9007199254740991 },
    "timestamp": {
      "type": "string",
      "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
    },
    "signature": {
      "type": "object",
      "additionalProperties": false,
      "required": ["alg", "kid", "envelope", "canonicalization"],
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
          ]
        }
      }
    }
  }
}

---

# Bismillah ir-Rahman ir-Rahim
