# Bismillah ir-Rahman ir-Rahim

# R0169 -- r27_findings_index.json

**Chronological Index:** 656 of 995  
**Date:** Undated  
**Section:** IV. XZ Protocol  
**Source File:** r27_findings_index.json  
**Source Format:** json  
**SHA-256:** `b345f98ba63e8a189324cc81212cd546414ce76033243abb0eec8828fc2ab439`  

---

## R0169 · r27_findings_index.json

- section: IV. XZ Protocol
- source_file: r27_findings_index.json
- source_format: json
- text_sha256: b345f98ba63e8a189324cc81212cd546414ce76033243abb0eec8828fc2ab439

{
  "round": 27,
  "version": "0.68",
  "total_seats": 4,
  "seats": [
    "S01",
    "S02",
    "S03",
    "S04"
  ],
  "all_halt": true,
  "convergence_groups": [
    {
      "group_id": 1,
      "surface": "Gate [13] vacuous on shipped bytes / skip-as-green",
      "finding_ids": [
        "F-S01-68-01",
        "F-S02-68-01",
        "F-S04-68-01"
      ],
      "triage_severity": "HIGH",
      "disposition": "CLOSED",
      "triage_adjudication": "Gate [13] rebuilt: bidirectional, severity-aware, extractor-based, fail-closed. Reports shipped in-packet."
    },
    {
      "group_id": 2,
      "surface": "Section 0.1 stale (v0.62) and FB-7b trajectory terminates at R18",
      "finding_ids": [
        "F-S01-68-06",
        "F-S03-68-01",
        "F-S04-68-05",
        "F-S04-68-06"
      ],
      "triage_severity": "HIGH",
      "disposition": "CLOSED",
      "triage_adjudication": "Section 0.1 updated to v0.70. FB-7b trajectory extended through R27. Repaired at v0.69, carried to v0.70."
    },
    {
      "group_id": 3,
      "surface": "Gate [13] logic defects: one-directional, severity-blind, false-positives",
      "finding_ids": [
        "F-S01-68-02",
        "F-S01-68-03",
        "F-S02-68-02"
      ],
      "triage_severity": "HIGH",
      "disposition": "CLOSED",
      "triage_adjudication": "Gate [13] rebuilt with bidirectional set equality, per-ID severity comparison, and declaration-context extraction (not raw regex)."
    },
    {
      "group_id": 4,
      "surface": "R26 convergence semantically misbound in index",
      "finding_ids": [
        "F-S02-68-03",
        "F-S04-68-02"
      ],
      "triage_severity": "HIGH",
      "disposition": "CLOSED",
      "triage_adjudication": "R27 index rebuilt with correct convergence grouping from extractor output."
    },
    {
      "group_id": 5,
      "surface": "Extractor CRITICAL->HIGH silent remap",
      "finding_ids": [
        "F-S01-68-05",
        "F-S04-68-07"
      ],
      "triage_severity": "MEDIUM",
      "disposition": "CLOSED",
      "triage_adjudication": "CRITICAL remap removed from extract_findings.py. CRITICAL is a valid severity."
    },
    {
      "group_id": 6,
      "surface": "Gate count overstates (256 claimed, 240 actual)",
      "finding_ids": [
        "F-S01-68-07",
        "F-S04-68-04"
      ],
      "triage_severity": "HIGH",
      "disposition": "CLOSED",
      "triage_adjudication": "Gate count tool-derived at build time, not narrated. AUDIT_CONTEXT claims removed from protocol body."
    },
    {
      "group_id": 7,
      "surface": "Unmanifested files ship in packet",
      "finding_ids": [
        "F-S01-68-11",
        "F-S04-68-09"
      ],
      "triage_severity": "LOW",
      "disposition": "CLOSED",
      "triage_adjudication": "All shipped files manifested in PACKET_SHA256SUMS."
    }
  ],
  "findings": [
    {
      "finding_id": "F-S01-68-01",
      "seat": "S01",
      "source_severity": "HIGH",
      "convergence_group": 1
    },
    {
      "finding_id": "F-S01-68-02",
      "seat": "S01",
      "source_severity": "HIGH",
      "convergence_group": 3
    },
    {
      "finding_id": "F-S01-68-03",
      "seat": "S01",
      "source_severity": "HIGH",
      "convergence_group": 3
    },
    {
      "finding_id": "F-S01-68-05",
      "seat": "S01",
      "source_severity": "MEDIUM",
      "convergence_group": 5
    },
    {
      "finding_id": "F-S01-68-06",
      "seat": "S01",
      "source_severity": "HIGH",
      "convergence_group": 2
    },
    {
      "finding_id": "F-S01-68-07",
      "seat": "S01",
      "source_severity": "HIGH",
      "convergence_group": 6
    },
    {
      "finding_id": "F-S01-68-11",
      "seat": "S01",
      "source_severity": "LOW",
      "convergence_group": 7
    },
    {
      "finding_id": "F-S02-68-01",
      "seat": "S02",
      "source_severity": "HIGH",
      "convergence_group": 1
    },
    {
      "finding_id": "F-S02-68-02",
      "seat": "S02",
      "source_severity": "HIGH",
      "convergence_group": 3
    },
    {
      "finding_id": "F-S02-68-03",
      "seat": "S02",
      "source_severity": "HIGH",
      "convergence_group": 4
    },
    {
      "finding_id": "F-S03-68-01",
      "seat": "S03",
      "source_severity": "HIGH",
      "convergence_group": 2
    },
    {
      "finding_id": "F-S04-68-01",
      "seat": "S04",
      "source_severity": "HIGH",
      "convergence_group": 1
    },
    {
      "finding_id": "F-S04-68-02",
      "seat": "S04",
      "source_severity": "HIGH",
      "convergence_group": 4
    },
    {
      "finding_id": "F-S04-68-04",
      "seat": "S04",
      "source_severity": "HIGH",
      "convergence_group": 6
    },
    {
      "finding_id": "F-S04-68-05",
      "seat": "S04",
      "source_severity": "HIGH",
      "convergence_group": 2
    },
    {
      "finding_id": "F-S04-68-06",
      "seat": "S04",
      "source_severity": "HIGH",
      "convergence_group": 2
    },
    {
      "finding_id": "F-S04-68-07",
      "seat": "S04",
      "source_severity": "HIGH",
      "convergence_group": 5
    },
    {
      "finding_id": "F-S04-68-09",
      "seat": "S04",
      "source_severity": "HIGH",
      "convergence_group": 7
    }
  ],
  "unique_findings_noted": [
    {
      "finding_id": "F-S01-68-04",
      "seat": "S01",
      "source_severity": "MEDIUM",
      "convergence_group": null
    },
    {
      "finding_id": "F-S01-68-08",
      "seat": "S01",
      "source_severity": "LOW",
      "convergence_group": null
    },
    {
      "finding_id": "F-S01-68-09",
      "seat": "S01",
      "source_severity": "LOW",
      "convergence_group": null
    },
    {
      "finding_id": "F-S01-68-10",
      "seat": "S01",
      "source_severity": "MEDIUM",
      "convergence_group": null
    },
    {
      "finding_id": "F-S01-68-12",
      "seat": "S01",
      "source_severity": "INFORMATIONAL",
      "convergence_group": null
    },
    {
      "finding_id": "F-S02-68-04",
      "seat": "S02",
      "source_severity": "HIGH",
      "convergence_group": null
    },
    {
      "finding_id": "F-S02-68-05",
      "seat": "S02",
      "source_severity": "MEDIUM",
      "convergence_group": null
    },
    {
      "finding_id": "F-S02-68-06",
      "seat": "S02",
      "source_severity": "LOW",
      "convergence_group": null
    },
    {
      "finding_id": "F-S02-68-07",
      "seat": "S02",
      "source_severity": "INFORMATIONAL",
      "convergence_group": null
    },
    {
      "finding_id": "F-S03-68-02",
      "seat": "S03",
      "source_severity": "MEDIUM",
      "convergence_group": null
    },
    {
      "finding_id": "F-S03-68-03",
      "seat": "S03",
      "source_severity": "MEDIUM",
      "convergence_group": null
    },
    {
      "finding_id": "F-S04-68-03",
      "seat": "S04",
      "source_severity": "HIGH",
      "convergence_group": null
    },
    {
      "finding_id": "F-S04-68-08",
      "seat": "S04",
      "source_severity": "HIGH",
      "convergence_group": null
    },
    {
      "finding_id": "F-S04-68-10",
      "seat": "S04",
      "source_severity": "MEDIUM",
      "convergence_group": null
    },
    {
      "finding_id": "F-S04-68-11",
      "seat": "S04",
      "source_severity": "MEDIUM",
      "convergence_group": null
    },
    {
      "finding_id": "F-S04-68-12",
      "seat": "S04",
      "source_severity": "MEDIUM",
      "convergence_group": null
    },
    {
      "finding_id": "F-S04-68-13",
      "seat": "S04",
      "source_severity": "MEDIUM",
      "convergence_group": null
    },
    {
      "finding_id": "F-S04-68-14",
      "seat": "S04",
      "source_severity": "LOW",
      "convergence_group": null
    },
    {
      "finding_id": "F-S04-68-15",
      "seat": "S04",
      "source_severity": "LOW",
      "convergence_group": null
    },
    {
      "finding_id": "F-S04-68-16",
      "seat": "S04",
      "source_severity": "LOW",
      "convergence_group": null
    },
    {
      "finding_id": "F-S04-68-17",
      "seat": "S04",
      "source_severity": "INFORMATIONAL",
      "convergence_group": null
    }
  ]
}

---

# Bismillah ir-Rahman ir-Rahim
