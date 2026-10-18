# Bismillah ir-Rahman ir-Rahim

# R0520 -- lineage-record.schema.json.txt

**Chronological Index:** 798 of 995  
**Date:** Undated  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** lineage-record.schema.json.txt  
**Source Format:** txt  
**SHA-256:** `bffbf81553f8d41c645b4040f10265550d7becf26e911613a87684a32e77f5c5`  

---

## R0520 · lineage-record.schema.json.txt

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: lineage-record.schema.json.txt
- source_format: txt
- text_sha256: bffbf81553f8d41c645b4040f10265550d7becf26e911613a87684a32e77f5c5

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:bssg:schema:0.1:lineage-record",
  "title": "BSSG lineage record (v0.1 DRAFT)",
  "description": "A hash-linked view of the records covering one session or one artifact. Lineage records claim continuity only for transformations that passed through a mediated adapter. Completeness outside the declared mediation boundary is not claimed and cannot be claimed. A lineage record with declared gaps MUST NOT report COMPLETE. Status: DRAFT, NOT CARRIED.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "record_type",
    "spec_version",
    "lineage_id",
    "subject_id",
    "session_id",
    "nodes",
    "head_digest",
    "chain_alg",
    "completeness",
    "declared_gaps",
    "mediation_boundary_ref",
    "issued_at",
    "signature"
  ],
  "properties": {
    "record_type": { "const": "bssg.lineage-record" },
    "spec_version": { "const": "0.1" },
    "lineage_id": { "$ref": "#/$defs/identifier" },
    "subject_id": { "$ref": "#/$defs/identifier" },
    "session_id": { "$ref": "#/$defs/identifier" },
    "nodes": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["node_id", "node_type", "digest", "parents"],
        "properties": {
          "node_id": { "$ref": "#/$defs/identifier" },
          "node_type": {
            "enum": [
              "effect-request",
              "authorization-receipt",
              "witness-receipt",
              "execution-receipt",
              "correction-event",
              "decision-record"
            ]
          },
          "digest": { "$ref": "#/$defs/digest" },
          "parents": { "type": "array", "items": { "$ref": "#/$defs/identifier" } },
          "superseded_by": { "$ref": "#/$defs/digest" },
          "recorded_at": { "$ref": "#/$defs/timestamp" }
        }
      }
    },
    "head_digest": { "$ref": "#/$defs/digest" },
    "chain_alg": { "const": "sha256-parent-chain" },
    "completeness": {
      "enum": ["COMPLETE", "PARTIAL", "UNKNOWN"],
      "description": "COMPLETE means only: every mediated transformation inside the declared boundary has a recorded node. It never means that all causation has been reconstructed."
    },
    "declared_gaps": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["gap_kind", "description"],
        "properties": {
          "gap_kind": {
            "enum": [
              "unmediated-channel",
              "missing-witness-receipt",
              "uncorrected-descendant",
              "pre-boundary-artifact",
              "unknown"
            ]
          },
          "description": { "type": "string" },
          "related_digest": { "$ref": "#/$defs/digest" }
        }
      }
    },
    "mediation_boundary_ref": {
      "type": "string",
      "minLength": 1,
      "description": "Identifier of the deployment's declared effect-path inventory. Non-bypassability claims are scoped to exactly this inventory."
    },
    "correction_epoch": { "$ref": "#/$defs/epoch" },
    "issued_at": { "$ref": "#/$defs/timestamp" },
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
