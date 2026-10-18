# Bismillah ir-Rahman ir-Rahim

# R0168 -- r25_findings_index.json

**Chronological Index:** 655 of 995  
**Date:** Undated  
**Section:** IV. XZ Protocol  
**Source File:** r25_findings_index.json  
**Source Format:** json  
**SHA-256:** `ff2319811f646a485734a2457455f2bfe6c7e360e87e0e0742cd587d4e5779b3`  

---

## R0168 · r25_findings_index.json

- section: IV. XZ Protocol
- source_file: r25_findings_index.json
- source_format: json
- text_sha256: ff2319811f646a485734a2457455f2bfe6c7e360e87e0e0742cd587d4e5779b3

{
  "round": 25,
  "version": "0.66",
  "prior_version": "0.65",
  "total_seats": 4,
  "seats": [
    "S01",
    "S02",
    "S03",
    "S04"
  ],
  "seat_families": {
    "S01": "Kimi K3 (as Opus 5)",
    "S02": "GPT-5.6 Sol (as Kimi K3)",
    "S03": "GPT-5.6 Sol",
    "S04": "Gemini 3.1 Pro"
  },
  "all_halt": false,
  "carrying_halts": 1,
  "advisory_halts": 2,
  "advisory_non_halts": 1,
  "convergence_groups": [
    {
      "group_id": 1,
      "surface": "CI-8 severity fidelity: source severities wrong in R24 index",
      "finding_ids": [
        "F-S01-66-02",
        "F-S02-66-01"
      ],
      "triage_severity": "HIGH",
      "disposition": "CLOSED",
      "triage_adjudication": "R24 index has correct IDs but wrong severities for 12/35 entries. Class fix: extract_findings.py."
    },
    {
      "group_id": 2,
      "surface": "Format regex prefix-only (probe N3 variants pass)",
      "finding_ids": [
        "F-S01-66-01",
        "F-S02-66-02"
      ],
      "triage_severity": "HIGH",
      "disposition": "CLOSED",
      "triage_adjudication": "Prefix regex accepts malformed IDs. Fix: strict FINDING_ID_RE."
    },
    {
      "group_id": 3,
      "surface": "FB-7b trajectory gap (R19-R25 missing from Section 25)",
      "finding_ids": [
        "F-S04-66-05"
      ],
      "triage_severity": "HIGH",
      "disposition": "CLOSED",
      "triage_adjudication": "Section 25 FB-7b row ends at R18. Fix: update through R25."
    },
    {
      "group_id": 4,
      "surface": "Tagging discipline incomplete (self-referential Goedel surface)",
      "finding_ids": [
        "F-S01-66-05",
        "F-S02-66-05",
        "F-S04-66-03"
      ],
      "triage_severity": "HIGH",
      "disposition": "CLOSED",
      "triage_adjudication": "Untagged sentences persist. Self-referential surface."
    }
  ],
  "unique_findings_noted": [
    {
      "finding_id": "F-S01-66-03",
      "seat": "S01",
      "source_severity": "HIGH",
      "substance": "See R25 seat report. [COMPUTED: extract_findings.py]",
      "disposition": "NOTED",
      "convergence_group": null
    },
    {
      "finding_id": "F-S01-66-04",
      "seat": "S01",
      "source_severity": "HIGH",
      "substance": "See R25 seat report. [COMPUTED: extract_findings.py]",
      "disposition": "NOTED",
      "convergence_group": null
    },
    {
      "finding_id": "F-S01-66-06",
      "seat": "S01",
      "source_severity": "HIGH",
      "substance": "See R25 seat report. [COMPUTED: extract_findings.py]",
      "disposition": "NOTED",
      "convergence_group": null
    },
    {
      "finding_id": "F-S01-66-07",
      "seat": "S01",
      "source_severity": "MEDIUM",
      "substance": "See R25 seat report. [COMPUTED: extract_findings.py]",
      "disposition": "NOTED",
      "convergence_group": null
    },
    {
      "finding_id": "F-S01-66-08",
      "seat": "S01",
      "source_severity": "MEDIUM",
      "substance": "See R25 seat report. [COMPUTED: extract_findings.py]",
      "disposition": "NOTED",
      "convergence_group": null
    },
    {
      "finding_id": "F-S01-66-09",
      "seat": "S01",
      "source_severity": "MEDIUM",
      "substance": "See R25 seat report. [COMPUTED: extract_findings.py]",
      "disposition": "NOTED",
      "convergence_group": null
    },
    {
      "finding_id": "F-S01-66-10",
      "seat": "S01",
      "source_severity": "LOW",
      "substance": "See R25 seat report. [COMPUTED: extract_findings.py]",
      "disposition": "NOTED",
      "convergence_group": null
    },
    {
      "finding_id": "F-S01-66-11",
      "seat": "S01",
      "source_severity": "LOW",
      "substance": "See R25 seat report. [COMPUTED: extract_findings.py]",
      "disposition": "NOTED",
      "convergence_group": null
    },
    {
      "finding_id": "F-S01-66-12",
      "seat": "S01",
      "source_severity": "LOW",
      "substance": "See R25 seat report. [COMPUTED: extract_findings.py]",
      "disposition": "NOTED",
      "convergence_group": null
    },
    {
      "finding_id": "F-S01-66-13",
      "seat": "S01",
      "source_severity": "INFORMATIONAL",
      "substance": "See R25 seat report. [COMPUTED: extract_findings.py]",
      "disposition": "NOTED",
      "convergence_group": null
    },
    {
      "finding_id": "F-S01-66-14",
      "seat": "S01",
      "source_severity": "INFORMATIONAL",
      "substance": "See R25 seat report. [COMPUTED: extract_findings.py]",
      "disposition": "NOTED",
      "convergence_group": null
    },
    {
      "finding_id": "F-S01-66-15",
      "seat": "S01",
      "source_severity": "INFORMATIONAL",
      "substance": "See R25 seat report. [COMPUTED: extract_findings.py]",
      "disposition": "NOTED",
      "convergence_group": null
    },
    {
      "finding_id": "F-S02-66-03",
      "seat": "S02",
      "source_severity": "HIGH",
      "substance": "See R25 seat report. [COMPUTED: extract_findings.py]",
      "disposition": "NOTED",
      "convergence_group": null
    },
    {
      "finding_id": "F-S02-66-04",
      "seat": "S02",
      "source_severity": "HIGH",
      "substance": "See R25 seat report. [COMPUTED: extract_findings.py]",
      "disposition": "NOTED",
      "convergence_group": null
    },
    {
      "finding_id": "F-S02-66-06",
      "seat": "S02",
      "source_severity": "MEDIUM",
      "substance": "See R25 seat report. [COMPUTED: extract_findings.py]",
      "disposition": "NOTED",
      "convergence_group": null
    },
    {
      "finding_id": "F-S04-66-01",
      "seat": "S04",
      "source_severity": "HIGH",
      "substance": "See R25 seat report. [COMPUTED: extract_findings.py]",
      "disposition": "NOTED",
      "convergence_group": null
    },
    {
      "finding_id": "F-S04-66-02",
      "seat": "S04",
      "source_severity": "HIGH",
      "substance": "See R25 seat report. [COMPUTED: extract_findings.py]",
      "disposition": "NOTED",
      "convergence_group": null
    },
    {
      "finding_id": "F-S04-66-04",
      "seat": "S04",
      "source_severity": "HIGH",
      "substance": "See R25 seat report. [COMPUTED: extract_findings.py]",
      "disposition": "NOTED",
      "convergence_group": null
    },
    {
      "finding_id": "F-S04-66-06",
      "seat": "S04",
      "source_severity": "MEDIUM",
      "substance": "See R25 seat report. [COMPUTED: extract_findings.py]",
      "disposition": "NOTED",
      "convergence_group": null
    },
    {
      "finding_id": "F-S04-66-07",
      "seat": "S04",
      "source_severity": "MEDIUM",
      "substance": "See R25 seat report. [COMPUTED: extract_findings.py]",
      "disposition": "NOTED",
      "convergence_group": null
    },
    {
      "finding_id": "F-S04-66-08",
      "seat": "S04",
      "source_severity": "MEDIUM",
      "substance": "See R25 seat report. [COMPUTED: extract_findings.py]",
      "disposition": "NOTED",
      "convergence_group": null
    },
    {
      "finding_id": "F-S04-66-09",
      "seat": "S04",
      "source_severity": "MEDIUM",
      "substance": "See R25 seat report. [COMPUTED: extract_findings.py]",
      "disposition": "NOTED",
      "convergence_group": null
    },
    {
      "finding_id": "F-S04-66-10",
      "seat": "S04",
      "source_severity": "LOW",
      "substance": "See R25 seat report. [COMPUTED: extract_findings.py]",
      "disposition": "NOTED",
      "convergence_group": null
    },
    {
      "finding_id": "F-S04-66-11",
      "seat": "S04",
      "source_severity": "LOW",
      "substance": "See R25 seat report. [COMPUTED: extract_findings.py]",
      "disposition": "NOTED",
      "convergence_group": null
    }
  ],
  "findings": [
    {
      "finding_id": "F-S01-66-01",
      "seat": "S01",
      "source_severity": "HIGH",
      "convergence_group": 2
    },
    {
      "finding_id": "F-S01-66-02",
      "seat": "S01",
      "source_severity": "HIGH",
      "convergence_group": 1
    },
    {
      "finding_id": "F-S01-66-05",
      "seat": "S01",
      "source_severity": "HIGH",
      "convergence_group": 4
    },
    {
      "finding_id": "F-S02-66-01",
      "seat": "S02",
      "source_severity": "HIGH",
      "convergence_group": 1
    },
    {
      "finding_id": "F-S02-66-02",
      "seat": "S02",
      "source_severity": "HIGH",
      "convergence_group": 2
    },
    {
      "finding_id": "F-S02-66-05",
      "seat": "S02",
      "source_severity": "LOW",
      "convergence_group": 4
    },
    {
      "finding_id": "F-S04-66-03",
      "seat": "S04",
      "source_severity": "HIGH",
      "convergence_group": 4
    },
    {
      "finding_id": "F-S04-66-05",
      "seat": "S04",
      "source_severity": "HIGH",
      "convergence_group": 3
    }
  ]
}

---

# Bismillah ir-Rahman ir-Rahim
