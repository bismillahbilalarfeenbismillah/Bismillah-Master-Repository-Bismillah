# Bismillah ir-Rahman ir-Rahim

# R0504 -- correction-event.schema.json.txt

**Chronological Index:** 788 of 995  
**Date:** Undated  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** correction-event.schema.json.txt  
**Source Format:** txt  
**SHA-256:** `65561b8340c40e0c6f5ba9617d6395b246b5b9e933dcc9b73bb3f3191cf6a5ad`  

---

## R0504 · correction-event.schema.json.txt

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: correction-event.schema.json.txt
- source_format: txt
- text_sha256: 65561b8340c40e0c6f5ba9617d6395b246b5b9e933dcc9b73bb3f3191cf6a5ad

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:bssg:schema:0.1:correction-event",
  "title": "BSSG correction event (v0.1 DRAFT)",
  "description": "A correction is a NEW record deriving from a prior record. Records are never edited in place. A correction that widens authority, or that lifts a terminal state, MUST carry at least two adjudicators in distinct control domains, neither of which is the subject's domain. Descendant closure that has not been established MUST be reported as PARTIAL or UNKNOWN and MUST NOT be reported as COMPLETE. Status: DRAFT, NOT CARRIED.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "record_type",
    "spec_version",
    "correction_id",
    "correction_class",
    "supersedes",
    "reason_code",
    "issued_by",
    "issued_at",
    "descendants",
    "descendant_closure_status",
    "signature"
  ],
  "properties": {
    "record_type": { "const": "bssg.correction-event" },
    "spec_version": { "const": "0.1" },
    "correction_id": { "$ref": "#/$defs/identifier" },
    "correction_class": {
      "enum": ["SUPERSEDE", "INVALIDATE", "AMEND_AUTHORITY", "LIFT_TERMINAL_STATE"]
    },
    "supersedes": {
      "$ref": "#/$defs/digest",
      "description": "Digest of the corrected record. The corrected record remains in the log; evidence that justified the original decision MUST NOT be destroyed by the correction."
    },
    "reason_code": { "type": "string", "pattern": "^C-[A-Z0-9-]{2,64}$" },
    "issued_by": {
      "type": "object",
      "additionalProperties": false,
      "required": ["authority_id", "control_domain"],
      "properties": {
        "authority_id": { "$ref": "#/$defs/identifier" },
        "control_domain": { "type": "string", "minLength": 1 }
      }
    },
    "session_id": { "$ref": "#/$defs/identifier" },
    "subject_control_domain": { "type": "string", "minLength": 1 },
    "adjudicators": {
      "type": "array",
      "minItems": 2,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["adjudicator_id", "control_domain", "signature"],
        "properties": {
          "adjudicator_id": { "$ref": "#/$defs/identifier" },
          "control_domain": { "type": "string", "minLength": 1 },
          "reproduction_digest": { "$ref": "#/$defs/digest" },
          "signature": { "$ref": "#/$defs/signature" }
        }
      },
      "description": "REQUIRED for AMEND_AUTHORITY and LIFT_TERMINAL_STATE. Distinctness of control domains is checked structurally; actual independence of those domains is an assumption the reference implementation cannot establish."
    },
    "descendants": {
      "type": "array",
      "items": { "$ref": "#/$defs/digest" },
      "description": "Recorded descendants known to be affected by this correction."
    },
    "unreachable_descendants": {
      "type": "array",
      "items": { "$ref": "#/$defs/digest" },
      "description": "Descendants known to exist but not reachable for correction. A non-empty list forbids a COMPLETE closure claim."
    },
    "descendant_closure_status": {
      "enum": ["COMPLETE", "PARTIAL", "UNKNOWN"],
      "description": "UNKNOWN is a first-class value. It MUST NOT be smoothed into COMPLETE."
    },
    "issued_at": { "$ref": "#/$defs/timestamp" },
    "effective_from": { "$ref": "#/$defs/timestamp" },
    "notes": { "type": "string" },
    "signature": { "$ref": "#/$defs/signature" }
  },
  "$defs": {
    "identifier": { "type": "string", "pattern": "^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$" },
    "digest": { "type": "string", "pattern": "^sha256:[0-9a-f]{64}$" },
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
