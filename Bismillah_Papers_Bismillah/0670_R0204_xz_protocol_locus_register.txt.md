# Bismillah ir-Rahman ir-Rahim

# R0204 -- xz_protocol_locus_register.txt

**Chronological Index:** 670 of 995  
**Date:** Undated  
**Section:** IV. XZ Protocol  
**Source File:** xz_protocol_locus_register.txt  
**Source Format:** txt  
**SHA-256:** `cb28bf3d07e046635f21c35e37004796c0911036f47e7f45a629d5d78aafa0b9`  

---

## R0204 · xz_protocol_locus_register.txt

- section: IV. XZ Protocol
- source_file: xz_protocol_locus_register.txt
- source_format: txt
- text_sha256: cb28bf3d07e046635f21c35e37004796c0911036f47e7f45a629d5d78aafa0b9

{
  "_note": "Every finding marked CLOSED in the Section 27 amendment record must appear here. Each entry either carries assertions evaluated against the CURRENT package bytes, or declares itself delegated to another gate, or declares itself historical with a stated reason. Assertions on target 'protocol_body' are evaluated against the protocol text with the Section 27 amendment record excluded, so a closure claim can never be satisfied by the log that asserts it.",

  "F-XZ06-GPT-01": {
    "claim": "Manifest digest recomputed in documented alphabetical order",
    "delegated_to": "xz_protocol_manifest_gate.py"
  },
  "F-XZ07-OP-01": {
    "claim": "No digest narrated from memory anywhere in the protocol text",
    "delegated_to": "xz_protocol_manifest_gate.py"
  },
  "F-XZ07-OP-02": {
    "claim": "Trust-roots file stamped to the current protocol version",
    "delegated_to": "xz_protocol_version_gate.py"
  },
  "F-XZ07-OP-03": {
    "claim": "Canonical six-suite invocation is required for the stated test count",
    "assertions": [
      {"target": "protocol_body", "type": "present", "value": "default pytest discovery does not collect xz_protocol_phase_a_tests.py"}
    ]
  },
  "F-K3-01": {
    "claim": "Source-frame test count stated as 29 and AST-derived",
    "assertions": [
      {"target": "protocol_body", "type": "present", "value": "29 tests"},
      {"target": "test_xz_protocol_source_frame.py", "type": "test_function_count", "value": 29}
    ]
  },
  "F-K3-02": {
    "claim": "Canonical verification command pinned in Section 0.1",
    "assertions": [
      {"target": "protocol_body", "type": "present", "value": "The canonical verification command is `pytest test_xz_protocol_kernel.py"},
      {"target": "protocol_body", "type": "section_contains", "section": "### 0.1 Status", "until": "### 0.2", "value": "The canonical verification command is"}
    ]
  },
  "F-K3-03": {
    "claim": "Kernel evaluation gate uses an exact type check, not isinstance",
    "assertions": [
      {"target": "xz_protocol_kernel.py", "type": "present", "value": "type(vector) is not ConjunctVector"},
      {"target": "xz_protocol_kernel.py", "type": "absent", "value": "isinstance(vector"}
    ]
  },
  "F-K3-08": {
    "claim": "PA-Z rule count stated as thirteen in code docstrings",
    "assertions": [
      {"target": "xz_protocol_phase_a_intervals.py", "type": "present", "value": "thirteen rules"},
      {"target": "xz_protocol_phase_a_intervals.py", "type": "absent", "value": "eleven rules"},
      {"target": "xz_protocol_phase_a_tests.py", "type": "present", "value": "thirteen rules"},
      {"target": "xz_protocol_phase_a_tests.py", "type": "absent", "value": "eleven rules"}
    ]
  },
  "F-XZ09-OP-01": {
    "claim": "BSSG concept DOI stated as 21712481, verified against the Zenodo API",
    "assertions": [
      {"target": "protocol_body", "type": "present", "value": "10.5281/zenodo.21712481 is the Zenodo concept DOI"},
      {"target": "protocol_body", "type": "absent", "value": "10.5281/zenodo.21611192 is the Zenodo concept DOI"}
    ]
  },
  "F-XZ09-OP-02": {
    "claim": "SHUDP and A5 citations deduplicated; the two version DOIs are stated as one record",
    "assertions": [
      {"target": "protocol_body", "type": "absent", "value": "| Is Evidence Independence an Axiom? (SHUDP v0.5) |"},
      {"target": "protocol_body", "type": "absent", "value": "(all thirteen records)"},
      {"target": "protocol_body", "type": "present", "value": "21539074 and 21539816 are two version DOIs under one concept DOI"},
      {"target": "protocol_body", "type": "present", "value": "Deposit-record divergence (verified against the Zenodo API, routed upstream)"}
    ]
  },
  "F-XZ09-OP-03": {
    "claim": "FB-7 split into FB-7a RESOLVED and FB-7b OPEN",
    "assertions": [
      {"target": "protocol_body", "type": "present", "value": "| ~~FB-7a~~ |"},
      {"target": "protocol_body", "type": "present", "value": "| FB-7b |"},
      {"target": "protocol_body", "type": "absent", "value": "| ~~FB-7~~ |"}
    ]
  },
  "F-XZ09-OP-05": {
    "claim": "Prohibited-content verifier exists and is named where it is relied upon",
    "assertions": [
      {"target": "protocol_body", "type": "absent", "value": "the shipped verifier fails the package if any prohibited sentence"},
      {"target": "protocol_body", "type": "present", "value": "xz_protocol_prohibited_content_verifier.py"},
      {"target": "_package", "type": "file_exists", "value": "xz_protocol_prohibited_content_verifier.py"}
    ]
  },
  "F-XZ12-OP-01": {
    "claim": "Closure gate parses the amendment record and evaluates registered loci against current bytes",
    "assertions": [
      {"target": "xz_protocol_closure_gate.py", "type": "present", "value": "def parse_closure_claims"},
      {"target": "_package", "type": "file_exists", "value": "test_xz_protocol_gates.py"}
    ]
  },
  "F-XZ12-OP-02": {
    "claim": "Gate coverage is globbed and includes the gates themselves",
    "assertions": [
      {"target": "xz_protocol_manifest_gate.py", "type": "absent", "value": "ALPHA_FILES = sorted(["},
      {"target": "xz_protocol_version_gate.py", "type": "present", "value": "gate excludes itself from its own coverage set"}
    ]
  },
  "F-XZ12-OP-03": {
    "claim": "Version gate uses match spans and a structured exclusion region, with no proximity whitelist",
    "assertions": [
      {"target": "xz_protocol_version_gate.py", "type": "present", "value": "VERSION_TOKEN.finditer"},
      {"target": "xz_protocol_version_gate.py", "type": "absent", "value": "text.index(f\"v{v}\")"},
      {"target": "xz_protocol_version_gate.py", "type": "present", "value": "def self_test"}
    ]
  },
  "F-XZ12-OP-04": {
    "claim": "Manifest gate scans the protocol text for unresolved digests",
    "assertions": [
      {"target": "xz_protocol_manifest_gate.py", "type": "present", "value": "def scan_protocol_digests"}
    ]
  },
  "F-XZ12-OP-06": {
    "claim": "The v0.11 entry's self-referential mutation count is corrected in a current entry, not by editing v0.11",
    "assertions": [
      {"target": "protocol_body", "type": "absent", "value": "CORRECTION-PLACEHOLDER"}
    ],
    "note": "The correction text lives in the v0.13 amendment entry, which is outside protocol_body by construction. The history gate protects the v0.11 entry from edit; this assertion only guards against a placeholder shipping."
  },
  "F-XZ12-OP-07": {
    "claim": "Prohibited-content verifier and amendment-integrity file both ship",
    "assertions": [
      {"target": "_package", "type": "file_exists", "value": "xz_protocol_prohibited_content_verifier.py"},
      {"target": "_package", "type": "file_exists", "value": "HISTORY.sha256"},
      {"target": "_package", "type": "file_exists", "value": "xz_protocol_history_gate.py"}
    ]
  }
}

---

# Bismillah ir-Rahman ir-Rahim
