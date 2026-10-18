# Bismillah ir-Rahman ir-Rahim

# R0167 -- r19_findings_index.json

**Chronological Index:** 496 of 995  
**Date:** 2026-08-11  
**Section:** IV. XZ Protocol  
**Source File:** r19_findings_index.json  
**Source Format:** json  
**SHA-256:** `319e42f637d232e9aa5b074a9ed508459abc55df7ea7d0f98b68ba5b4fb81448`  

---

## R0167 · r19_findings_index.json

- section: IV. XZ Protocol
- source_file: r19_findings_index.json
- source_format: json
- merged_variants: 1 (FINDINGS_INDEX.txt)
- text_sha256: 319e42f637d232e9aa5b074a9ed508459abc55df7ea7d0f98b68ba5b4fb81448

{
  "round": 19,
  "version_under_audit": "0.60",
  "target_version": "0.61",
  "seats": [
    "S01F",
    "S01C",
    "S02F",
    "S02C",
    "S03F",
    "S03C",
    "S04F",
    "S04C",
    "S05F",
    "S05C"
  ],
  "triage_date": "2026-08-11",
  "verdicts": {
    "S01F": "HALT",
    "S01C": "HALT",
    "S02F": "HALT",
    "S02C": "HALT",
    "S03F": "HALT",
    "S03C": "HALT",
    "S04F": "HALT",
    "S04C": "HALT",
    "S05F": "HALT",
    "S05C": "HALT"
  },
  "carrying_halts": 4,
  "advisory_halts": 6,
  "findings": [
    {
      "finding_id": "F-S01-60-01",
      "seat": "S01F",
      "source_severity": "HIGH",
      "defect_class": "Source severity not load-bearing: M2 inert",
      "convergence_group": 1,
      "source_finding_id": "F-S01-60-01"
    },
    {
      "finding_id": "F-S01-60-02",
      "seat": "S01F",
      "source_severity": "HIGH",
      "defect_class": "Correction (ch) never landed: group 4 still CLOSED",
      "convergence_group": 2,
      "source_finding_id": "F-S01-60-02"
    },
    {
      "finding_id": "F-S01-60-03",
      "seat": "S01F",
      "source_severity": "HIGH",
      "defect_class": "VERSION-1 gate claimed but absent from build.py",
      "convergence_group": 3,
      "source_finding_id": "F-S01-60-03"
    },
    {
      "finding_id": "F-S01C-60-01",
      "seat": "S01C",
      "source_severity": "HIGH",
      "defect_class": "Source severity not load-bearing: M2/M3 inert",
      "convergence_group": 1,
      "source_finding_id": "F-S01-60-01"
    },
    {
      "finding_id": "F-S01C-60-02",
      "seat": "S01C",
      "source_severity": "HIGH",
      "defect_class": "Correction (ch) never landed",
      "convergence_group": 2,
      "source_finding_id": "F-S01-60-02"
    },
    {
      "finding_id": "F-S01C-60-03",
      "seat": "S01C",
      "source_severity": "HIGH",
      "defect_class": "VERSION-1 gate absent; sabotage passes build",
      "convergence_group": 3,
      "source_finding_id": "F-S01-60-03"
    },
    {
      "finding_id": "F-S02-60-01F",
      "seat": "S02F",
      "source_severity": "HIGH",
      "defect_class": "M2/M3 inert: receipt not authenticated",
      "convergence_group": 1,
      "source_finding_id": "F-S02-60-01"
    },
    {
      "finding_id": "F-S02-60-02F",
      "seat": "S02F",
      "source_severity": "HIGH",
      "defect_class": "Correction (ch) DIFF-VERIFIED false",
      "convergence_group": 2,
      "source_finding_id": "F-S02-60-02"
    },
    {
      "finding_id": "F-S02-60-03F",
      "seat": "S02F",
      "source_severity": "HIGH",
      "defect_class": "CI-8 finding ID F/C suffixes not in reports",
      "convergence_group": 5,
      "source_finding_id": "F-S02-60-03"
    },
    {
      "finding_id": "F-S02-60-04F",
      "seat": "S02F",
      "source_severity": "MEDIUM",
      "defect_class": "Gate count 258 vs 257 vs 222",
      "convergence_group": 6,
      "source_finding_id": "F-S02-60-04"
    },
    {
      "finding_id": "F-S02-60-01C",
      "seat": "S02C",
      "source_severity": "HIGH",
      "defect_class": "M2/M3 inert: source severity not load-bearing",
      "convergence_group": 1,
      "source_finding_id": "F-S02-60-01"
    },
    {
      "finding_id": "F-S02-60-02C",
      "seat": "S02C",
      "source_severity": "HIGH",
      "defect_class": "Correction (ch) false",
      "convergence_group": 2,
      "source_finding_id": "F-S02-60-02"
    },
    {
      "finding_id": "F-S02-60-03C",
      "seat": "S02C",
      "source_severity": "HIGH",
      "defect_class": "VERSION-1 gate absent",
      "convergence_group": 3,
      "source_finding_id": "F-S02-60-03"
    },
    {
      "finding_id": "F-S03-60-01F",
      "seat": "S03F",
      "source_severity": "HIGH",
      "defect_class": "VERSION-1 gate absent from build.py",
      "convergence_group": 3,
      "source_finding_id": "F-S03-60-01"
    },
    {
      "finding_id": "F-S03-60-01C",
      "seat": "S03C",
      "source_severity": "HIGH",
      "defect_class": "Group 4 disposition remains CLOSED",
      "convergence_group": 2,
      "source_finding_id": "F-S03-60-01"
    },
    {
      "finding_id": "F-S03-60-02C",
      "seat": "S03C",
      "source_severity": "HIGH",
      "defect_class": "Seat undercounting in convergence bracket",
      "convergence_group": 7,
      "source_finding_id": "F-S03-60-02"
    },
    {
      "finding_id": "F-S04-60-01",
      "seat": "S04C",
      "source_severity": "HIGH",
      "defect_class": "Correction (ch) never landed; Status false",
      "convergence_group": 2,
      "source_finding_id": "F-S04-60-01"
    },
    {
      "finding_id": "F-S04-60-02",
      "seat": "S04C",
      "source_severity": "HIGH",
      "defect_class": "VERSION-1 gate absent; sabotage proof executed",
      "convergence_group": 3,
      "source_finding_id": "F-S04-60-02"
    },
    {
      "finding_id": "F-S05-60-01F",
      "seat": "S05F",
      "source_severity": "HIGH",
      "defect_class": "M2/M3 inert: 6 mutations byte-identical",
      "convergence_group": 1,
      "source_finding_id": "F-S05-60-01"
    },
    {
      "finding_id": "F-S05-60-02F",
      "seat": "S05F",
      "source_severity": "HIGH",
      "defect_class": "Dangling convergence_group values 9-12",
      "convergence_group": 4,
      "source_finding_id": "F-S05-60-02"
    },
    {
      "finding_id": "F-S05-60-03F",
      "seat": "S05F",
      "source_severity": "HIGH",
      "defect_class": "Correction (ch) DIFF-VERIFIED false",
      "convergence_group": 2,
      "source_finding_id": "F-S05-60-03"
    },
    {
      "finding_id": "F-S05-60-04F",
      "seat": "S05F",
      "source_severity": "HIGH",
      "defect_class": "VERSION-1 gate absent",
      "convergence_group": 3,
      "source_finding_id": "F-S05-60-04"
    },
    {
      "finding_id": "F-S05-60-05F",
      "seat": "S05F",
      "source_severity": "HIGH",
      "defect_class": "Body-repair ledger not generated from refs",
      "convergence_group": 7,
      "source_finding_id": "F-S05-60-05"
    },
    {
      "finding_id": "F-S05-60-06F",
      "seat": "S05F",
      "source_severity": "MEDIUM",
      "defect_class": "Gate count documentation",
      "convergence_group": 6,
      "source_finding_id": "F-S05-60-06"
    },
    {
      "finding_id": "F-S05-60-01C",
      "seat": "S05C",
      "source_severity": "HIGH",
      "defect_class": "M2/M3 inert: 14 continuity mutations",
      "convergence_group": 1,
      "source_finding_id": "F-S05-60-01"
    }
  ],
  "convergence_groups": [
    {
      "group_id": 1,
      "label": "Source severity not load-bearing (M2/M3 inert, R16-R19)",
      "finding_ids": [
        "F-S01-60-01",
        "F-S01C-60-01",
        "F-S02-60-01F",
        "F-S02-60-01C",
        "F-S05-60-01F",
        "F-S05-60-01C"
      ],
      "triage_severity": "HIGH",
      "disposition": "CLOSED",
      "repair_type": "architecture",
      "architecture_version": "CI v0.3.1",
      "triage_adjudication": "CI v0.3.1 emits the source distribution into the register (load-bearing) and validates receipt content against the computed distribution. M2 mutations now change output; receipt removal on mixed groups fails.",
      "adjudication_receipt": "Source distribution: 6 HIGH. All 6 source findings are HIGH. Triage severity HIGH. No deviation."
    },
    {
      "group_id": 2,
      "label": "Correction (ch) never landed (group 4 still CLOSED)",
      "finding_ids": [
        "F-S01-60-02",
        "F-S01C-60-02",
        "F-S02-60-02F",
        "F-S02-60-02C",
        "F-S03-60-01C",
        "F-S04-60-01",
        "F-S05-60-03F"
      ],
      "triage_severity": "HIGH",
      "disposition": "CLOSED",
      "correction_refs": [
        "cj"
      ],
      "triage_adjudication": "One-line fix: r18_findings_index.json group 4 disposition set to SCOPED_OUT with scope_note. Correction (cj) verifies the landing.",
      "adjudication_receipt": "Source distribution: 7 HIGH. All 7 source findings are HIGH. Triage severity HIGH. No deviation."
    },
    {
      "group_id": 3,
      "label": "VERSION-1 gate absent from build.py",
      "finding_ids": [
        "F-S01-60-03",
        "F-S01C-60-03",
        "F-S02-60-03C",
        "F-S03-60-01F",
        "F-S04-60-02",
        "F-S05-60-04F"
      ],
      "triage_severity": "HIGH",
      "disposition": "CLOSED",
      "repair_type": "architecture",
      "architecture_version": "CI v0.3.1",
      "triage_adjudication": "Gate [10i] added to build.py: derives VERSION-1 from VERSION constant and asserts both Section 22 tokens match.",
      "adjudication_receipt": "Source distribution: 6 HIGH. All 6 source findings are HIGH. Triage severity HIGH. No deviation."
    },
    {
      "group_id": 4,
      "label": "Dangling convergence_group values in findings[]",
      "finding_ids": [
        "F-S05-60-02F"
      ],
      "triage_severity": "HIGH",
      "disposition": "CLOSED",
      "repair_type": "architecture",
      "architecture_version": "CI v0.3.1",
      "triage_adjudication": "Generator validates findings[].convergence_group against declared groups. Noted findings use null. 7 dangling values fixed in r18 index.",
      "adjudication_receipt": "Source distribution: 1 HIGH. Source severity: F-S05-60-02F HIGH. Triage severity HIGH. No deviation."
    },
    {
      "group_id": 5,
      "label": "Finding ID F/C suffixes not in source reports",
      "finding_ids": [
        "F-S02-60-03F"
      ],
      "triage_severity": "HIGH",
      "disposition": "NOTED",
      "triage_adjudication": "The F/C suffixes disambiguate fresh vs continuous seats. Source reports use base IDs. A normalization receipt or source_finding_id field is needed. NOTED for R20 architectural resolution.",
      "adjudication_receipt": "Source distribution: 1 HIGH. Source severity: F-S02-60-03F HIGH. Triage severity HIGH. No deviation."
    },
    {
      "group_id": 6,
      "label": "Gate count documentation (recurring)",
      "finding_ids": [
        "F-S02-60-04F",
        "F-S05-60-06F"
      ],
      "triage_severity": "MEDIUM",
      "disposition": "NOTED",
      "triage_adjudication": "Derive from build.py runtime in R20 dispatch.",
      "adjudication_receipt": "Source distribution: 2 MEDIUM. Both source findings MEDIUM. Triage severity MEDIUM. No deviation."
    },
    {
      "group_id": 7,
      "label": "Body-repair ledger / COMPUTED tag scope",
      "finding_ids": [
        "F-S03-60-02C",
        "F-S05-60-05F"
      ],
      "triage_severity": "MEDIUM",
      "disposition": "NOTED",
      "triage_adjudication": "Adjudication prose is index-verbatim under COMPUTED tag. Body-repair ledger not generated from correction_refs. NOTED for future COMPUTED tag scope reform.",
      "adjudication_receipt": "Source distribution: 2 HIGH. Source severities: F-S03-60-02C HIGH, F-S05-60-05F HIGH. Triage severity MEDIUM. Elevated findings: both source findings are HIGH but the substance (tag scope) is structural, not byte-false."
    }
  ],
  "unique_findings_noted": []
}

---

# Bismillah ir-Rahman ir-Rahim
