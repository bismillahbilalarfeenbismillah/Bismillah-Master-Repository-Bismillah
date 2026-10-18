# Bismillah ir-Rahman ir-Rahim

# R0166 -- r18_findings_index.json

**Chronological Index:** 495 of 995  
**Date:** 2026-08-11  
**Section:** IV. XZ Protocol  
**Source File:** r18_findings_index.json  
**Source Format:** json  
**SHA-256:** `1164fe7acb597dc9845b7f945c1bf1472efb763b0fe2c58c1489ad4e4682a290`  

---

## R0166 · r18_findings_index.json

- section: IV. XZ Protocol
- source_file: r18_findings_index.json
- source_format: json
- text_sha256: 1164fe7acb597dc9845b7f945c1bf1472efb763b0fe2c58c1489ad4e4682a290

{
  "round": 18,
  "version_under_audit": "0.59",
  "target_version": "0.60",
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
  "seat_families": {
    "S01F": "Kimi K3 (Moonshot AI)",
    "S01C": "Kimi K3 (Moonshot AI)",
    "S02F": "GPT-5.6 Sol (OpenAI)",
    "S02C": "GPT-5.6 Sol (OpenAI)",
    "S03F": "Gemini 3.1 Pro (Google)",
    "S03C": "Gemini 3.1 Pro (Google)",
    "S04F": "Kimi K3 (Moonshot AI)",
    "S04C": "Kimi K3 (Moonshot AI)",
    "S05F": "GPT-5.6 Sol (OpenAI)",
    "S05C": "GPT-5.6 Sol (OpenAI)"
  },
  "seat_roles": {
    "S01F": "carrying binding fresh",
    "S01C": "carrying binding continuous",
    "S02F": "carrying binding fresh",
    "S02C": "carrying binding continuous",
    "S03F": "advisory fresh",
    "S03C": "advisory continuous",
    "S04F": "advisory fresh",
    "S04C": "advisory continuous",
    "S05F": "advisory fresh",
    "S05C": "advisory continuous"
  },
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
      "finding_id": "F-S01-59-01",
      "seat": "S01F",
      "source_severity": "HIGH",
      "defect_class": "Section 22.2/22.3 version-token staleness recurrence (6th round)",
      "convergence_group": 3
    },
    {
      "finding_id": "F-S01-59-02",
      "seat": "S01F",
      "source_severity": "HIGH",
      "defect_class": "R16 group 6 receipt still wrong: 2M+1L claimed, actual 3M+1L",
      "convergence_group": 5
    },
    {
      "finding_id": "F-S01-59-03",
      "seat": "S01F",
      "source_severity": "HIGH",
      "defect_class": "findings[] semantically inert: severity derivation and receipt enforcement false",
      "convergence_group": 1
    },
    {
      "finding_id": "F-S01-59-04",
      "seat": "S01F",
      "source_severity": "HIGH",
      "defect_class": "Correction-letter namespace collision: register vs body cross-references false",
      "convergence_group": 2
    },
    {
      "finding_id": "F-S01-59-05",
      "seat": "S01F",
      "source_severity": "MEDIUM",
      "defect_class": "Gate count 262 vs 261 vs 222 documentation inconsistency",
      "convergence_group": 6
    },
    {
      "finding_id": "F-S01-59-06",
      "seat": "S01F",
      "source_severity": "MEDIUM",
      "defect_class": "COMPUTED tag overclaim: adjudication prose copied verbatim under COMPUTED tag",
      "convergence_group": 7
    },
    {
      "finding_id": "F-S01-59-07",
      "seat": "S01F",
      "source_severity": "LOW",
      "defect_class": "Noted-item missing field crashes instead of validation error",
      "convergence_group": 8
    },
    {
      "finding_id": "F-S01-59-08",
      "seat": "S01F",
      "source_severity": "LOW",
      "defect_class": "Secondary membership CLOSED label overstates repair (was scoped out)",
      "convergence_group": 4
    },
    {
      "finding_id": "F-S01-59-09",
      "seat": "S01F",
      "source_severity": "INFORMATIONAL",
      "defect_class": "PRIOR_HISTORY untagged; correction (cf) target outside packet closure",
      "convergence_group": null
    },
    {
      "finding_id": "F-S02-59-01F",
      "seat": "S02F",
      "source_severity": "HIGH",
      "defect_class": "findings[] semantically inert: front-matter/docstring claims false",
      "convergence_group": 1
    },
    {
      "finding_id": "F-S02-59-02F",
      "seat": "S02F",
      "source_severity": "HIGH",
      "defect_class": "Secondary membership CLOSED but not implemented",
      "convergence_group": 4
    },
    {
      "finding_id": "F-S02-59-03F",
      "seat": "S02F",
      "source_severity": "HIGH",
      "defect_class": "Correction-letter namespace collision",
      "convergence_group": 2
    },
    {
      "finding_id": "F-S02-59-04F",
      "seat": "S02F",
      "source_severity": "MEDIUM",
      "defect_class": "CI-4 metric ambiguity",
      "convergence_group": null
    },
    {
      "finding_id": "F-S02-59-05F",
      "seat": "S02F",
      "source_severity": "MEDIUM",
      "defect_class": "Gate count documentation inconsistency",
      "convergence_group": 6
    },
    {
      "finding_id": "F-S02-59-01C",
      "seat": "S02C",
      "source_severity": "HIGH",
      "defect_class": "findings[] semantically inert",
      "convergence_group": 1
    },
    {
      "finding_id": "F-S02-59-02C",
      "seat": "S02C",
      "source_severity": "HIGH",
      "defect_class": "Correction-letter namespace collision with F-CI-3R",
      "convergence_group": 2
    },
    {
      "finding_id": "F-S02-59-03C",
      "seat": "S02C",
      "source_severity": "MEDIUM",
      "defect_class": "Gate count documentation",
      "convergence_group": 6
    },
    {
      "finding_id": "F-S02-59-04C",
      "seat": "S02C",
      "source_severity": "MEDIUM",
      "defect_class": "CI-4 metric ambiguity",
      "convergence_group": null
    },
    {
      "finding_id": "F-S02-59-05C",
      "seat": "S02C",
      "source_severity": "MEDIUM",
      "defect_class": "R17 triage severity arithmetic error",
      "convergence_group": null
    },
    {
      "finding_id": "F-S03-59-01F",
      "seat": "S03F",
      "source_severity": "HIGH",
      "defect_class": "Severity provenance failure: generator validates tokens only",
      "convergence_group": 1
    },
    {
      "finding_id": "F-S03-59-01C",
      "seat": "S03C",
      "source_severity": "HIGH",
      "defect_class": "Byte-false adjudication receipt enforcement claim",
      "convergence_group": 1
    },
    {
      "finding_id": "F-S04-59-01",
      "seat": "S04F",
      "source_severity": "HIGH",
      "defect_class": "Correction-letter namespace collision (metastasis)",
      "convergence_group": 2
    },
    {
      "finding_id": "F-S04-59-02",
      "seat": "S04F",
      "source_severity": "HIGH",
      "defect_class": "findings[] semantically inert: M2/M3 prove inertness",
      "convergence_group": 1
    },
    {
      "finding_id": "F-S04-59-03",
      "seat": "S04F",
      "source_severity": "MEDIUM",
      "defect_class": "Gate count 262 vs 261 vs 222",
      "convergence_group": 6
    },
    {
      "finding_id": "F-S04-59-04",
      "seat": "S04F",
      "source_severity": "MEDIUM",
      "defect_class": "Validation boundary gap: noted dispositions, findings[] IDs, cross-references",
      "convergence_group": 8
    },
    {
      "finding_id": "F-S04-59-05",
      "seat": "S04F",
      "source_severity": "LOW",
      "defect_class": "Correction (cf) DIFF-VERIFIED target outside packet closure",
      "convergence_group": null
    },
    {
      "finding_id": "F-S04-59-06",
      "seat": "S04F",
      "source_severity": "LOW",
      "defect_class": "CI_METHODOLOGY lacks normative v0.2.2 schema",
      "convergence_group": null
    },
    {
      "finding_id": "F-S04-59-07",
      "seat": "S04F",
      "source_severity": "INFORMATIONAL",
      "defect_class": "Carried observations: no byte-identity register gate, PRIOR_HISTORY untagged, version arg uncoupled",
      "convergence_group": null
    },
    {
      "finding_id": "F-S05-59-01F",
      "seat": "S05F",
      "source_severity": "HIGH",
      "defect_class": "findings[] semantically inert: 6 inert mutations",
      "convergence_group": 1
    },
    {
      "finding_id": "F-S05-59-02F",
      "seat": "S05F",
      "source_severity": "HIGH",
      "defect_class": "Correction-letter namespace collision",
      "convergence_group": 2
    },
    {
      "finding_id": "F-S05-59-03F",
      "seat": "S05F",
      "source_severity": "HIGH",
      "defect_class": "Secondary membership CLOSED without closure mechanism",
      "convergence_group": 4
    },
    {
      "finding_id": "F-S05-59-04F",
      "seat": "S05F",
      "source_severity": "MEDIUM",
      "defect_class": "Gate count documentation",
      "convergence_group": 6
    },
    {
      "finding_id": "F-S05-59-01C",
      "seat": "S05C",
      "source_severity": "HIGH",
      "defect_class": "findings[] semantically inert (continuous verification)",
      "convergence_group": 1
    },
    {
      "finding_id": "F-S05-59-02C",
      "seat": "S05C",
      "source_severity": "HIGH",
      "defect_class": "Secondary membership not represented",
      "convergence_group": 4
    },
    {
      "finding_id": "F-S05-59-03C",
      "seat": "S05C",
      "source_severity": "HIGH",
      "defect_class": "Correction-letter collision (continuous verification)",
      "convergence_group": 2
    }
  ],
  "convergence_groups": [
    {
      "group_id": 1,
      "label": "findings[] semantically inert (spec-impl gap R16-R18)",
      "finding_ids": [
        "F-S01-59-03",
        "F-S02-59-01F",
        "F-S02-59-01C",
        "F-S03-59-01F",
        "F-S03-59-01C",
        "F-S04-59-02",
        "F-S05-59-01F",
        "F-S05-59-01C"
      ],
      "triage_severity": "HIGH",
      "disposition": "CLOSED",
      "repair_type": "architecture",
      "architecture_version": "CI v0.3",
      "triage_adjudication": "Spec-impl gap recurring for the R16-R18 span (3 occurrences). CI v0.3 implements actual severity derivation from findings[] source records with mandatory adjudication receipt on divergence. M2/M3-class mutations now either change output or fail generation.",
      "adjudication_receipt": "All 8 source findings are HIGH. Triage severity HIGH. No deviation."
    },
    {
      "group_id": 2,
      "label": "Correction-letter namespace collision (novel R18)",
      "finding_ids": [
        "F-S01-59-04",
        "F-S02-59-03F",
        "F-S02-59-02C",
        "F-S04-59-01",
        "F-S05-59-02F",
        "F-S05-59-03C"
      ],
      "triage_severity": "HIGH",
      "disposition": "CLOSED",
      "repair_type": "architecture",
      "architecture_version": "CI v0.3",
      "triage_adjudication": "Generator assumed one correction per group. CI v0.3 uses explicit correction_refs[] per group -- multi-correction groups supported. Body-repair ledger generated from same refs.",
      "adjudication_receipt": "All 6 source findings are HIGH. Triage severity HIGH. No deviation."
    },
    {
      "group_id": 3,
      "label": "Section 22.2/22.3 version-token staleness (recurrence R13-R18 (6 occurrences))",
      "finding_ids": [
        "F-S01-59-01"
      ],
      "triage_severity": "HIGH",
      "disposition": "CLOSED",
      "correction_refs": [
        "cg"
      ],
      "triage_adjudication": "Version-token staleness class recurring for the R13-R18 span (6 occurrences). Repair applied R17 literal target (v0.57) instead of VERSION-1 semantic rule. CI v0.3 gates both bounds to VERSION-1 (entry count minus one). Correction (cg) advances to v0.59.",
      "adjudication_receipt": "Source severity: F-S01-59-01 HIGH. Triage severity HIGH. No deviation."
    },
    {
      "group_id": 4,
      "label": "Secondary membership disposition label",
      "finding_ids": [
        "F-S01-59-08",
        "F-S02-59-02F",
        "F-S05-59-03F",
        "F-S05-59-02C"
      ],
      "triage_severity": "HIGH",
      "disposition": "SCOPED_OUT",
      "correction_refs": [
        "ch"
      ],
      "triage_adjudication": "Register said CLOSED via architecture repair but nothing was implemented -- it was scoped out. S01F/S04F accepted the scope-out as adequate; S02F/S05F called it Class A because the label was false. Correction (ch): change disposition to SCOPED_OUT with truthful scope note.",
      "adjudication_receipt": "Source severities: F-S01-59-08 LOW, F-S02-59-02F HIGH, F-S05-59-03F HIGH, F-S05-59-02C HIGH. Triage severity HIGH. F-S01-59-08 elevated from LOW: the substance (false label) is the same across all 4 findings.",
      "scope_note": "canonical-group rule retained, multi-membership not implemented"
    },
    {
      "group_id": 5,
      "label": "R16 group 6 receipt distribution still wrong",
      "finding_ids": [
        "F-S01-59-02"
      ],
      "triage_severity": "HIGH",
      "disposition": "CLOSED",
      "correction_refs": [
        "ci"
      ],
      "triage_adjudication": "The v0.59 correction (cf) claimed 2M+1L but findings[] shows 3M+1L (S02 is MEDIUM). The R17 triage propagated its own miscount. Correction (ci): fix receipt in R17 index to 3 MEDIUM (F-S01-58-03, F-S02-58-04, F-S05-58-05) + 1 LOW (F-S04-58-06).",
      "adjudication_receipt": "Source severity: F-S01-59-02 HIGH. Triage severity HIGH. No deviation."
    },
    {
      "group_id": 6,
      "label": "Gate count documentation inconsistency (recurring since R14)",
      "finding_ids": [
        "F-S01-59-05",
        "F-S02-59-05F",
        "F-S02-59-03C",
        "F-S04-59-03",
        "F-S05-59-04F"
      ],
      "triage_severity": "MEDIUM",
      "disposition": "NOTED",
      "triage_adjudication": "AUDIT_CONTEXT said 262; executed build emits 261 PASS lines; CI_METHODOLOGY says 222. Derive from build.py output in R19 dispatch.",
      "adjudication_receipt": "All 5 source findings are MEDIUM. Triage severity MEDIUM. No deviation."
    },
    {
      "group_id": 7,
      "label": "COMPUTED tag overclaim on adjudication prose",
      "finding_ids": [
        "F-S01-59-06"
      ],
      "triage_severity": "MEDIUM",
      "disposition": "NOTED",
      "triage_adjudication": "Adjudication prose is copied verbatim from index under COMPUTED tag. Tag scope disclosure needed.",
      "adjudication_receipt": "Source severity: F-S01-59-06 MEDIUM. Triage severity MEDIUM. No deviation."
    },
    {
      "group_id": 8,
      "label": "Validation boundary gap (noted dispositions, findings[] IDs, cross-references)",
      "finding_ids": [
        "F-S01-59-07",
        "F-S04-59-04"
      ],
      "triage_severity": "MEDIUM",
      "disposition": "CLOSED",
      "repair_type": "architecture",
      "architecture_version": "CI v0.3",
      "triage_adjudication": "CI v0.3 extends fail-closed validation to noted dispositions, findings[] IDs (format + uniqueness), required fields, and cross-layer references.",
      "adjudication_receipt": "Source severities: F-S01-59-07 LOW, F-S04-59-04 MEDIUM. Triage severity MEDIUM. F-S01-59-07 elevated from LOW: same validation-boundary substance."
    }
  ],
  "unique_findings_noted": [
    {
      "finding_id": "F-S01-59-09",
      "seat": "S01F",
      "source_severity": "INFORMATIONAL",
      "disposition": "NOTED",
      "substance": "PRIOR_HISTORY line untagged; correction (cf) target outside packet closure"
    },
    {
      "finding_id": "F-S02-59-04F",
      "seat": "S02F",
      "source_severity": "MEDIUM",
      "disposition": "NOTED",
      "substance": "CI-4 metric ambiguity: tag-count vs character-share basis undefined"
    },
    {
      "finding_id": "F-S02-59-04C",
      "seat": "S02C",
      "source_severity": "MEDIUM",
      "disposition": "NOTED",
      "substance": "CI-4 dead-space metric underspecified"
    },
    {
      "finding_id": "F-S02-59-05C",
      "seat": "S02C",
      "source_severity": "MEDIUM",
      "disposition": "NOTED",
      "substance": "R17 triage severity arithmetic: 13H/12M/4L/2I should be 13H/11M/5L/2I"
    },
    {
      "finding_id": "F-S04-59-05",
      "seat": "S04F",
      "source_severity": "LOW",
      "disposition": "NOTED",
      "substance": "Correction (cf) DIFF-VERIFIED target outside packet closure"
    },
    {
      "finding_id": "F-S04-59-06",
      "seat": "S04F",
      "source_severity": "LOW",
      "disposition": "NOTED",
      "substance": "CI_METHODOLOGY lacks normative v0.2.2/v0.3 schema"
    },
    {
      "finding_id": "F-S04-59-07",
      "seat": "S04F",
      "source_severity": "INFORMATIONAL",
      "disposition": "NOTED",
      "substance": "No byte-identity register gate; PRIOR_HISTORY untagged; version arg uncoupled; ASSERTED basis-dependent"
    }
  ]
}

---

# Bismillah ir-Rahman ir-Rahim
