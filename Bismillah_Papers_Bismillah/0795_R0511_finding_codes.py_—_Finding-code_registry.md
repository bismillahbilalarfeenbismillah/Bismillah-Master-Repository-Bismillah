# Bismillah ir-Rahman ir-Rahim

# R0511 -- finding_codes.py — Finding-code registry.

**Chronological Index:** 795 of 995  
**Date:** Undated  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** finding_codes.py  
**Source Format:** py  
**SHA-256:** `8864834914110259816c493d5a303bb6bb160b441794b6e71ac89ef531173a61`  

---

## R0511 · finding_codes.py — Finding-code registry.

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: finding_codes.py
- source_format: py
- text_sha256: 8864834914110259816c493d5a303bb6bb160b441794b6e71ac89ef531173a61

"""Finding-code registry.

NEW in v1.2.5: CSV (BYN-CSV-001..099) and JSON (BYN-JSON-001..099) namespaces.
NEW in v1.2.6: ZIP composition / defense (BYN-ZIP-901..999) namespace.

Each finding code carries:
- id: canonical string identifier
- kind: substrate-kind (CSV, JSON, ZIP, ...)
- title: short human-readable name
- severity_default: default severity if the analyzer does not override
- description: what the finding indicates about the surface/substrate divergence
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional


@dataclass(frozen=True)
class FindingCode:
    """Immutable record of a finding code."""

    id: str
    kind: str
    title: str
    severity_default: str
    description: str


# CSV finding codes (NEW v1.2.5)
CSV_CODES: List[FindingCode] = [
    FindingCode(
        id="BYN-CSV-001",
        kind="CSV",
        title="declared-header-vs-actual-column-count-mismatch",
        severity_default="HIGH",
        description=(
            "The declared header row enumerates N columns; the substrate row tokenization "
            "produced rows with a different column count. Surface advertises one row shape; "
            "substrate carries another."
        ),
    ),
    FindingCode(
        id="BYN-CSV-002",
        kind="CSV",
        title="declared-column-name-vs-actual-token-mismatch",
        severity_default="MEDIUM",
        description=(
            "A column name declared in the header is not present in the substrate tokenization, "
            "or vice versa, even though counts match."
        ),
    ),
    FindingCode(
        id="BYN-CSV-003",
        kind="CSV",
        title="ragged-rows-inconsistent-column-count",
        severity_default="HIGH",
        description=(
            "Substrate rows have inconsistent column counts. RFC 4180 §2 requires that "
            "each record contain the same number of fields throughout the file."
        ),
    ),
    FindingCode(
        id="BYN-CSV-004",
        kind="CSV",
        title="unquoted-embedded-comma-tokenization-divergence",
        severity_default="HIGH",
        description=(
            "Substrate tokenization produces more columns than the header declares because "
            "an embedded comma was not quoted per RFC 4180 §2."
        ),
    ),
    FindingCode(
        id="BYN-CSV-005",
        kind="CSV",
        title="unterminated-quoted-field",
        severity_default="HIGH",
        description=(
            "A quoted field opens but does not close before EOF or end-of-row, leaving "
            "substrate tokenization ambiguous."
        ),
    ),
    FindingCode(
        id="BYN-CSV-006",
        kind="CSV",
        title="line-ending-mismatch-CRLF-vs-LF",
        severity_default="LOW",
        description=(
            "RFC 4180 §2 specifies CRLF as the canonical line ending; substrate uses bare LF "
            "or mixed line endings. Tolerated by most parsers; surfaced for audit completeness."
        ),
    ),
    FindingCode(
        id="BYN-CSV-007",
        kind="CSV",
        title="trailing-empty-row",
        severity_default="LOW",
        description="Trailing empty row(s) at EOF; informational signal of editor artifact.",
    ),
]


# JSON finding codes (NEW v1.2.5)
JSON_CODES: List[FindingCode] = [
    FindingCode(
        id="BYN-JSON-001",
        kind="JSON",
        title="declared-key-set-vs-actual-key-set-divergence",
        severity_default="HIGH",
        description=(
            "The declared schema or top-level key set does not match the actual top-level "
            "keys present in the substrate. Surface advertises one shape; substrate carries another."
        ),
    ),
    FindingCode(
        id="BYN-JSON-002",
        kind="JSON",
        title="declared-value-type-vs-actual-value-type-mismatch",
        severity_default="HIGH",
        description=(
            "A declared value type (e.g., string, integer, array) does not match the actual "
            "type at that JSON pointer in the substrate."
        ),
    ),
    FindingCode(
        id="BYN-JSON-003",
        kind="JSON",
        title="malformed-json-not-parseable",
        severity_default="HIGH",
        description=(
            "The substrate is not parseable as RFC 8259 JSON. Trailing commas, comments, "
            "or unquoted identifiers all trigger this code."
        ),
    ),
    FindingCode(
        id="BYN-JSON-004",
        kind="JSON",
        title="duplicate-object-key",
        severity_default="MEDIUM",
        description=(
            "RFC 8259 §4 SHOULD requirement: object names should be unique. Substrate carries "
            "duplicate keys, producing parser-dependent behavior."
        ),
    ),
    FindingCode(
        id="BYN-JSON-005",
        kind="JSON",
        title="non-utf8-encoding",
        severity_default="MEDIUM",
        description=(
            "RFC 8259 §8.1 requires UTF-8 encoding for interchange. Substrate uses a different "
            "encoding (e.g., UTF-16, Latin-1) without BOM declaration."
        ),
    ),
    FindingCode(
        id="BYN-JSON-006",
        kind="JSON",
        title="declared-array-length-vs-actual-mismatch",
        severity_default="MEDIUM",
        description=(
            "A declared array length contract does not match the actual array length in substrate."
        ),
    ),
    FindingCode(
        id="BYN-JSON-007",
        kind="JSON",
        title="number-out-of-spec-range",
        severity_default="LOW",
        description=(
            "RFC 8259 §6 advisory: implementations limit number range. Substrate carries a number "
            "outside IEEE 754 double-precision representable range."
        ),
    ),
]


# ZIP composition / defense finding codes (NEW v1.2.6)
ZIP_CODES: List[FindingCode] = [
    FindingCode(
        id="BYN-ZIP-901",
        kind="ZIP",
        title="zip-bomb-defense-engaged",
        severity_default="BLOCKER",
        description=(
            "The ZIP-bomb defense engaged against this composed artifact. One or more "
            "of the safety bounds (file count, per-file decompressed size, total "
            "decompressed size, compression ratio, or recursion depth) would be exceeded. "
            "The walker GRACEFULLY refused to recurse further; no decompression bomb "
            "is detonated. Composition_path identifies the offending archive."
        ),
    ),
]


# ML extractor finding codes (NEW v1.3.0)
ML_CODES: List[FindingCode] = [
    FindingCode(
        id="BYN-ML-001",
        kind="ML",
        title="declared-opset-version-vs-actual-mismatch",
        severity_default="HIGH",
        description=(
            "The model's declared opset version (via metadata_props or sidecar manifest) "
            "does not match the actual opset_import value in the substrate."
        ),
    ),
    FindingCode(
        id="BYN-ML-002",
        kind="ML",
        title="declared-producer-name-vs-actual-mismatch",
        severity_default="HIGH",
        description=(
            "The model's declared producer_name does not match the producer_name string "
            "carried in the substrate."
        ),
    ),
    FindingCode(
        id="BYN-ML-003",
        kind="ML",
        title="model-format-wire-parse-failure",
        severity_default="HIGH",
        description=(
            "The model substrate is not parseable as its declared format (ONNX protobuf, "
            "TF SavedModel protobuf, or TorchScript ZIP-of-pickle)."
        ),
    ),
    FindingCode(
        id="BYN-ML-004",
        kind="ML",
        title="declared-input-names-vs-actual-mismatch",
        severity_default="HIGH",
        description=(
            "The declared input tensor names do not match the actual graph.input names "
            "in the substrate."
        ),
    ),
    FindingCode(
        id="BYN-ML-005",
        kind="ML",
        title="declared-output-names-vs-actual-mismatch",
        severity_default="HIGH",
        description=(
            "The declared output tensor names do not match the actual graph.output names "
            "in the substrate."
        ),
    ),
    FindingCode(
        id="BYN-ML-006",
        kind="ML",
        title="tensorflow-version-provenance-missing",
        severity_default="MEDIUM",
        description=(
            "TF SavedModel substrate carries no tensorflow_version string in meta_info_def; "
            "FDA premarket review expects model provenance metadata to be present."
        ),
    ),
    FindingCode(
        id="BYN-ML-007",
        kind="ML",
        title="tf-savedmodel-empty-meta-graphs",
        severity_default="HIGH",
        description=(
            "TF SavedModel substrate contains zero MetaGraphDef entries; the model has "
            "no executable signature."
        ),
    ),
    FindingCode(
        id="BYN-ML-008",
        kind="ML",
        title="torchscript-version-file-missing",
        severity_default="MEDIUM",
        description=(
            "TorchScript archive does not declare a `version` file at any depth in the "
            "ZIP. PyTorch's serialization format expects this metadata."
        ),
    ),
    FindingCode(
        id="BYN-ML-009",
        kind="ML",
        title="torchscript-pickle-rce-vector",
        severity_default="BLOCKER",
        description=(
            "TorchScript pickle byte-stream references a known RCE vector "
            "(os.system, subprocess, builtins.exec, builtins.eval, posix.system, nt.system). "
            "Do NOT unpickle this archive."
        ),
    ),
    FindingCode(
        id="BYN-ML-010",
        kind="ML",
        title="torchscript-archive-empty",
        severity_default="HIGH",
        description=(
            "TorchScript ZIP archive contains neither code/ nor data.pkl; cannot represent "
            "a valid serialized model."
        ),
    ),
]


# Manifest extractor finding codes (NEW v1.3.0)
MFST_CODES: List[FindingCode] = [
    FindingCode(
        id="BYN-MFST-001",
        kind="MANIFEST",
        title="manifest-parse-failure",
        severity_default="HIGH",
        description=(
            "The .bayyinah.yaml manifest cannot be parsed under its declared format "
            "(YAML, TOML, or JSON)."
        ),
    ),
    FindingCode(
        id="BYN-MFST-002",
        kind="MANIFEST",
        title="declared-kind-vs-detected-mismatch",
        severity_default="MEDIUM",
        description=(
            "The manifest's declared artifact.kind does not match the kind detected from "
            "the companion artifact's substrate."
        ),
    ),
    FindingCode(
        id="BYN-MFST-003",
        kind="MANIFEST",
        title="required-field-missing-for-declared-kind",
        severity_default="MEDIUM",
        description=(
            "The manifest declares an artifact.kind that imposes schema obligations, but "
            "one or more required fields are absent from the manifest."
        ),
    ),
    FindingCode(
        id="BYN-MFST-004",
        kind="MANIFEST",
        title="cross-format-round-trip-parity-mismatch",
        severity_default="MEDIUM",
        description=(
            "When the manifest is supplied in multiple formats (e.g., YAML and JSON), "
            "the parsed documents must canonicalize to byte-identical structure. They do not."
        ),
    ),
]


# AUTOSAR ARXML finding codes (NEW v1.4.0)
ARXML_CODES: List[FindingCode] = [
    FindingCode(
        id="BYN-ARXML-001",
        kind="ARXML",
        title="arxml-xml-parse-failure",
        severity_default="HIGH",
        description=(
            "The ARXML substrate is not parseable as XML. AUTOSAR R22-11 schema "
            "interpretation cannot proceed."
        ),
    ),
    FindingCode(
        id="BYN-ARXML-CHK1",
        kind="ARXML",
        title="signal-datatype-reference-unresolved",
        severity_default="HIGH",
        description=(
            "I-SIGNAL declares DATA-TYPE-REF referencing a data type that is not "
            "present in IMPLEMENTATION-DATA-TYPE or APPLICATION-DATA-TYPE packages. "
            "Cross-layer reconciliation fails."
        ),
    ),
    FindingCode(
        id="BYN-ARXML-CHK2",
        kind="ARXML",
        title="signal-length-vs-datatype-width-mismatch",
        severity_default="HIGH",
        description=(
            "I-SIGNAL LENGTH does not match the canonical bit-width of its declared "
            "data type (e.g., LENGTH=16 with DATA-TYPE-REF=uint8 where uint8 is 8 bits)."
        ),
    ),
    FindingCode(
        id="BYN-ARXML-CHK3",
        kind="ARXML",
        title="port-direction-vs-element-type-mismatch",
        severity_default="HIGH",
        description=(
            "Port declared DIRECTION does not match the structural type "
            "(PROVIDED-PORT-PROTOTYPE / REQUIRED-PORT-PROTOTYPE)."
        ),
    ),
    FindingCode(
        id="BYN-ARXML-CHK4",
        kind="ARXML",
        title="runnable-timing-budget-exceeded",
        severity_default="HIGH",
        description=(
            "RUNNABLE-ENTITY declared BUDGET-MS is exceeded by the cumulative sum of "
            "ACTIVATION-MS triggers. ISO 26262 timing analysis fails."
        ),
    ),
]


# ELF binary substrate finding codes (NEW v1.10.0)
ELF_CODES: List[FindingCode] = [
    FindingCode(
        id="BYN-ELF-001",
        kind="ELF",
        title="elf-header-parse-failure",
        severity_default="HIGH",
        description=(
            "The substrate does not present a valid ELF identification + header. "
            "Magic bytes, class, or endianness fields are not parseable."
        ),
    ),
    FindingCode(
        id="BYN-ELF-002",
        kind="ELF",
        title="unsupported-machine-class-for-phase-1",
        severity_default="MEDIUM",
        description=(
            "ELF substrate declares a machine class outside v1.10.0 phase-1 support "
            "(x86_64, aarch64, i386, arm). Deferred to v1.10.0.x or v1.10.1."
        ),
    ),
    FindingCode(
        id="BYN-ELF-003",
        kind="ELF",
        title="no-dwarf-debug-info",
        severity_default="LOW",
        description=(
            "ELF substrate carries no .debug_* sections. FRaZ-calibrated default: "
            "regulated-submission ELFs SHOULD ship with DWARF debug info for AUTOSAR "
            "pairing (v1.4.1) cross-check."
        ),
    ),
    FindingCode(
        id="BYN-ELF-004",
        kind="ELF",
        title="empty-text-section",
        severity_default="HIGH",
        description=(
            "ELF binary has no .text section or .text section is zero-length. "
            "Binary carries no executable code; structural anomaly."
        ),
    ),
]


# ARXML-ELF pairing finding codes (NEW v1.4.1)
PAIR_CODES: List[FindingCode] = [
    FindingCode(
        id="BYN-PAIR-001",
        kind="PAIR",
        title="paired-elf-parse-failure",
        severity_default="HIGH",
        description=(
            "The paired ELF substrate did not parse; cross-substrate ARXML-ELF "
            "reconciliation cannot proceed."
        ),
    ),
    FindingCode(
        id="BYN-PAIR-002",
        kind="PAIR",
        title="arxml-symbol-missing-in-elf",
        severity_default="HIGH",
        description=(
            "ARXML declares RUNNABLE-ENTITY or port short-names that are not present "
            "as symbols in the ELF substrate. SWC-impl-to-ELF-symbol bridge broken."
        ),
    ),
    FindingCode(
        id="BYN-PAIR-003",
        kind="PAIR",
        title="elf-symbol-unmapped-in-arxml",
        severity_default="MEDIUM",
        description=(
            "ELF substrate carries symbols not declared in any ARXML SHORT-NAME; "
            "possible undocumented implementation surface."
        ),
    ),
    FindingCode(
        id="BYN-PAIR-901",
        kind="PAIR",
        title="budget-controller-dishonest-complete",
        severity_default="BLOCKER",
        description=(
            "The budget controller reported scan COMPLETE while incomplete_axes was "
            "non-empty. This is the Munafiq pattern (surface claims complete; "
            "substrate carries incomplete sub-scans). F7 hard sub-gate violation."
        ),
    ),
]


# ARINC-653 + Munafiq finding codes (NEW v1.5.0)
ARINC_CODES: List[FindingCode] = [
    FindingCode(
        id="BYN-ARINC-001",
        kind="ARINC",
        title="arinc653-config-parse-failure",
        severity_default="HIGH",
        description=(
            "The ARINC-653 module XML config could not be parsed as a valid "
            "ARINC-653 module / partition schedule document."
        ),
    ),
    FindingCode(
        id="BYN-ARINC-002",
        kind="ARINC",
        title="partition-memory-bound-exceeds-linker-region",
        severity_default="HIGH",
        description=(
            "ARINC-653 partition memory bound exceeds the linker-script segment "
            "size allocated for the partition. Surface declares one bound; substrate "
            "binary carries another."
        ),
    ),
    FindingCode(
        id="BYN-ARINC-003",
        kind="ARINC",
        title="partition-memory-bound-undersized-vs-linker-region",
        severity_default="MEDIUM",
        description=(
            "ARINC-653 partition memory bound is substantially smaller than the "
            "linker-script segment allocated to the partition. Likely overprovisioned "
            "linker region or undersized config."
        ),
    ),
    FindingCode(
        id="BYN-ARINC-004",
        kind="ARINC",
        title="scheduling-slot-shorter-than-declared-wcet",
        severity_default="HIGH",
        description=(
            "ARINC-653 partition schedule slot duration is shorter than the declared "
            "WCET of the partition. Surface advertises a schedulable system; substrate "
            "carries a deadline-miss configuration."
        ),
    ),
    FindingCode(
        id="BYN-ARINC-005",
        kind="ARINC",
        title="channel-source-partition-undeclared",
        severity_default="HIGH",
        description=(
            "ARINC-653 inter-partition channel references a SOURCE partition that "
            "is not declared in the module's PARTITION list."
        ),
    ),
    FindingCode(
        id="BYN-ARINC-006",
        kind="ARINC",
        title="channel-destination-partition-undeclared",
        severity_default="HIGH",
        description=(
            "ARINC-653 inter-partition channel references a DESTINATION partition "
            "that is not declared in the module's PARTITION list."
        ),
    ),
    FindingCode(
        id="BYN-ARINC-007",
        kind="ARINC",
        title="channel-port-not-found-on-source-partition",
        severity_default="HIGH",
        description=(
            "ARINC-653 channel SOURCE port name not present in the source partition's "
            "declared SOURCE ports."
        ),
    ),
    FindingCode(
        id="BYN-ARINC-008",
        kind="ARINC",
        title="channel-port-not-found-on-destination-partition",
        severity_default="HIGH",
        description=(
            "ARINC-653 channel DESTINATION port name not present in the destination "
            "partition's declared DESTINATION ports."
        ),
    ),
]


MUNAFIQ_CODES: List[FindingCode] = [
    FindingCode(
        id="BYN-MUNAFIQ-001",
        kind="MUNAFIQ",
        title="surface-clean-substrate-divergent",
        severity_default="HIGH",
        description=(
            "Munafiq probe: a scan target's surface declares conformance while the "
            "substrate-only walk reveals declared-but-missing references. The "
            "Finding.munafiq_meta tag records the Munafiq Protocol process number "
            "matched by the AX-SH heuristic set (DOI 10.5281/zenodo.19700420)."
        ),
    ),
    FindingCode(
        id="BYN-MUNAFIQ-002",
        kind="MUNAFIQ",
        title="performed-alignment-detected",
        severity_default="MEDIUM",
        description=(
            "Munafiq probe: structural-honesty heuristic over AX-SH discipline matched "
            "an adversarial-crafted target whose surface and substrate both claim "
            "alignment but exhibit divergence under closer reading. NOT a learned "
            "classifier; heuristic-only."
        ),
    ),
]


# ARINC-653 + ELF cross-substrate pairing finding codes (NEW v1.5.1)
AEPAIR_CODES: List[FindingCode] = [
    FindingCode(
        id="BYN-AEPAIR-001",
        kind="AEPAIR",
        title="partition-section-missing-in-elf",
        severity_default="HIGH",
        description=(
            "ARINC-653 partition declares a memory bound but the corresponding "
            "linker-script section (.part_<name> by convention) is not present in "
            "the paired ELF binary's section table."
        ),
    ),
    FindingCode(
        id="BYN-AEPAIR-002",
        kind="AEPAIR",
        title="partition-memory-bound-exceeds-elf-segment",
        severity_default="HIGH",
        description=(
            "ARINC-653 partition declares a memory bound LARGER than the actual "
            "ELF section size allocated to the partition. Surface advertises one "
            "bound; substrate binary carries another."
        ),
    ),
    FindingCode(
        id="BYN-AEPAIR-003",
        kind="AEPAIR",
        title="partition-memory-bound-undersized-vs-elf-segment",
        severity_default="MEDIUM",
        description=(
            "ARINC-653 partition memory bound is substantially smaller than the "
            "ELF section sized for the partition. Likely under-provisioned config "
            "or over-allocated linker region."
        ),
    ),
    FindingCode(
        id="BYN-AEPAIR-004",
        kind="AEPAIR",
        title="elf-parse-failure-during-pairing",
        severity_default="HIGH",
        description=(
            "The paired ELF binary could not be parsed during ARINC-653 + ELF "
            "cross-substrate pairing. Pairing aborts; standalone ARINC-653 "
            "findings remain valid."
        ),
    ),
]


# IEC 61850 SCL finding codes (NEW v1.7.0)
SCL_CODES: List[FindingCode] = [
    FindingCode(
        id="BYN-SCL-001",
        kind="SCL",
        title="scl-config-parse-failure",
        severity_default="HIGH",
        description=(
            "The SCL XML config could not be parsed as a valid IEC 61850-6 SCL "
            "document (SSD / SCD / CID / IID)."
        ),
    ),
    FindingCode(
        id="BYN-SCL-002",
        kind="SCL",
        title="ssd-logical-node-missing-in-scd",
        severity_default="HIGH",
        description=(
            "A logical node declared in the SSD (system specification) is not "
            "instantiated in the SCD (substation configuration). Surface declares "
            "one substation; substrate carries another."
        ),
    ),
    FindingCode(
        id="BYN-SCL-003",
        kind="SCL",
        title="scd-ied-missing-in-cid",
        severity_default="HIGH",
        description=(
            "An IED declared in the SCD is not identified by the corresponding CID "
            "(configured IED description). Per IEC 61850-6 the CID must describe "
            "exactly the IED referenced in the SCD."
        ),
    ),
    FindingCode(
        id="BYN-SCL-004",
        kind="SCL",
        title="cid-dataset-missing-in-iid",
        severity_default="MEDIUM",
        description=(
            "A DataSet declared in the CID is not instantiated in the IID "
            "(instantiated IED description). DataSet identity must round-trip "
            "between configuration and instantiation."
        ),
    ),
    FindingCode(
        id="BYN-SCL-005",
        kind="SCL",
        title="scd-goose-control-block-missing-subscriber",
        severity_default="HIGH",
        description=(
            "A GOOSE control block declared in the SCD has no matching "
            "subscriber in any CID. GOOSE topology surface advertises a "
            "publisher-subscriber pair that the substrate does not realize."
        ),
    ),
    FindingCode(
        id="BYN-SCL-006",
        kind="SCL",
        title="scd-goose-subscriber-references-unknown-publisher",
        severity_default="HIGH",
        description=(
            "A CID subscribes to a GOOSE control block that is not declared in "
            "the SCD. Subscriber-side surface references a publisher that the "
            "substrate does not configure."
        ),
    ),
]


# SBOM (SPDX + CycloneDX) finding codes (NEW v1.9.0)
SBOM_CODES: List[FindingCode] = [
    FindingCode(
        id="BYN-SBOM-001",
        kind="SBOM",
        title="sbom-parse-failure",
        severity_default="HIGH",
        description=(
            "SBOM document could not be parsed as SPDX 2.3 or CycloneDX 1.5."
        ),
    ),
    FindingCode(
        id="BYN-SBOM-002",
        kind="SBOM",
        title="ntia-minimum-element-missing",
        severity_default="HIGH",
        description=(
            "An SBOM component lacks one or more NTIA SBOM minimum elements "
            "(supplier name, component name, version, unique identifier, "
            "dependency relationship, author, timestamp)."
        ),
    ),
    FindingCode(
        id="BYN-SBOM-003",
        kind="SBOM",
        title="component-hash-malformed",
        severity_default="MEDIUM",
        description=(
            "An SBOM component declares a hash but the hash value does not "
            "match the declared algorithm's expected output length."
        ),
    ),
    FindingCode(
        id="BYN-SBOM-004",
        kind="SBOM",
        title="dependency-references-undeclared-component",
        severity_default="HIGH",
        description=(
            "An SBOM dependency relationship references a component identifier "
            "that is not declared in the components/packages list."
        ),
    ),
]

INTOTO_CODES: List[FindingCode] = [
    FindingCode(
        id="BYN-INTOTO-001",
        kind="INTOTO",
        title="dsse-envelope-parse-failure",
        severity_default="HIGH",
        description=(
            "The DSSE envelope could not be parsed as a valid in-toto v1 "
            "attestation envelope."
        ),
    ),
    FindingCode(
        id="BYN-INTOTO-002",
        kind="INTOTO",
        title="predicate-type-not-recognised",
        severity_default="MEDIUM",
        description=(
            "The attestation predicate type is not a recognised in-toto / SLSA "
            "predicate (slsa.dev/provenance, in-toto.io/Statement)."
        ),
    ),
    FindingCode(
        id="BYN-INTOTO-003",
        kind="INTOTO",
        title="subject-digest-malformed",
        severity_default="HIGH",
        description=(
            "An attestation subject declares a digest with an algorithm not in "
            "the allowed set (sha256, sha512, sha3-256, sha3-512)."
        ),
    ),
    FindingCode(
        id="BYN-INTOTO-004",
        kind="INTOTO",
        title="slsa-provenance-missing-builder-id",
        severity_default="HIGH",
        description=(
            "SLSA provenance v1 requires a builder.id field; substrate omits it."
        ),
    ),
]

SIG_CODES: List[FindingCode] = [
    FindingCode(
        id="BYN-SIG-001",
        kind="SIG",
        title="signature-verification-failed",
        severity_default="BLOCKER",
        description=(
            "Signature verification against the supplied public key FAILED. "
            "The attestation payload does not match its claimed signature."
        ),
    ),
    FindingCode(
        id="BYN-SIG-002",
        kind="SIG",
        title="signature-missing",
        severity_default="HIGH",
        description=(
            "DSSE envelope declares signatures field but the signatures list "
            "is empty."
        ),
    ),
    FindingCode(
        id="BYN-SIG-003",
        kind="SIG",
        title="signature-algorithm-not-allowed",
        severity_default="HIGH",
        description=(
            "Signature algorithm is not in the allowed set."
        ),
    ),
]

THREEWAY_CODES: List[FindingCode] = [
    FindingCode(
        id="BYN-3WAY-001",
        kind="3WAY",
        title="sbom-component-missing-in-source",
        severity_default="HIGH",
        description=(
            "An SBOM component is not present in the source manifest "
            "(package.json, requirements.txt, Cargo.toml, etc)."
        ),
    ),
    FindingCode(
        id="BYN-3WAY-002",
        kind="3WAY",
        title="source-package-missing-in-sbom",
        severity_default="HIGH",
        description=(
            "A source manifest package is not declared in the SBOM components "
            "list."
        ),
    ),
    FindingCode(
        id="BYN-3WAY-003",
        kind="3WAY",
        title="sbom-component-not-in-binary",
        severity_default="HIGH",
        description=(
            "An SBOM component is not present in the binary artifact's "
            "embedded package list."
        ),
    ),
]


# IEC 61131-3 PLCopen finding codes (NEW v1.6.0)
PLC_CODES: List[FindingCode] = [
    FindingCode(
        id="BYN-PLC-001",
        kind="PLC",
        title="plcopen-config-parse-failure",
        severity_default="HIGH",
        description=(
            "The PLCopen XML configuration could not be parsed as a valid "
            "IEC 61131-3 PLCopen TC6 XML schema document."
        ),
    ),
    FindingCode(
        id="BYN-PLC-002",
        kind="PLC",
        title="pou-declared-but-not-instantiated",
        severity_default="HIGH",
        description=(
            "A Program Organization Unit (POU) is declared in the project but "
            "never instantiated in the resource configuration."
        ),
    ),
    FindingCode(
        id="BYN-PLC-003",
        kind="PLC",
        title="resource-task-references-unknown-pou",
        severity_default="HIGH",
        description=(
            "A resource task binds to a POU name that is not declared in the "
            "project's POU list."
        ),
    ),
    FindingCode(
        id="BYN-PLC-004",
        kind="PLC",
        title="global-var-type-mismatch-vs-pou-input",
        severity_default="HIGH",
        description=(
            "A POU input variable declares a data type that does not match the "
            "corresponding global-variable declaration."
        ),
    ),
    FindingCode(
        id="BYN-PLC-005",
        kind="PLC",
        title="safety-class-attribute-missing",
        severity_default="HIGH",
        description=(
            "Per NRC RG 1.152 a safety-related POU must declare a safety class "
            "attribute; substrate omits it."
        ),
    ),
    FindingCode(
        id="BYN-PLC-006",
        kind="PLC",
        title="task-interval-not-positive",
        severity_default="MEDIUM",
        description=(
            "A periodic task declares interval=0 or a non-numeric interval. "
            "Periodic tasks require a positive interval."
        ),
    ),
]


def all_codes() -> List[FindingCode]:
    """Return the full v1.6.0 finding-code registry."""
    return [
        *CSV_CODES,
        *JSON_CODES,
        *ZIP_CODES,
        *ML_CODES,
        *MFST_CODES,
        *ARXML_CODES,
        *ELF_CODES,
        *PAIR_CODES,
        *ARINC_CODES,
        *MUNAFIQ_CODES,
        *AEPAIR_CODES,
        *SCL_CODES,
        *SBOM_CODES,
        *INTOTO_CODES,
        *SIG_CODES,
        *THREEWAY_CODES,
        *PLC_CODES,
    ]


def code_by_id(code_id: str) -> Optional[FindingCode]:
    """Look up a FindingCode by canonical id string."""
    for c in all_codes():
        if c.id == code_id:
            return c
    return None


def _id_index() -> Dict[str, FindingCode]:
    return {c.id: c for c in all_codes()}

---

# Bismillah ir-Rahman ir-Rahim
