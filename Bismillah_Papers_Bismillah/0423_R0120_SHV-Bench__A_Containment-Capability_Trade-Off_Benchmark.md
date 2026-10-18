# Bismillah ir-Rahman ir-Rahim

# R0120 -- SHV-Bench: A Containment-Capability Trade-Off Benchmark

**Chronological Index:** 423 of 995  
**Date:** 2026-08  
**Section:** III. Structural Honesty — Core Papers  
**Source File:** README.txt  
**Source Format:** txt  
**SHA-256:** `a8d9fa812d22b194d2e30f7ce0181e28a855363ae178f6a84bb8f17e7805d62e`  

---

## R0120 · SHV-Bench: A Containment-Capability Trade-Off Benchmark

- section: III. Structural Honesty — Core Papers
- source_file: README.txt
- source_format: txt
- text_sha256: a8d9fa812d22b194d2e30f7ce0181e28a855363ae178f6a84bb8f17e7805d62e

SHV-Bench: A Containment-Capability Trade-Off Benchmark
for Structural Honesty Verification
========================================================

Successor Protocol and Task Corpus Design
Version 1.0 | August 2026
Author: Bilal Syed Arfeen (BayyinahEnterprise)

Contents of this deposit
------------------------

SHV-Bench_Protocol_v1.0.pdf    Protocol paper (15 pages)
SHV-Bench_Protocol_v1.0.md     Markdown source
SHV-Bench_Task_Corpus.csv      Task corpus (1,673 CISA KEV entries)
Publication_Posture_v0_1.txt   Binding publication-posture constraint
README.txt                     This file

Provenance
----------

Protocol PDF SHA-256:
61bbbf57a5dd5beb97a806575fa58d7d475840677c7dace12a2a28a856731350

Task Corpus CSV SHA-256:
6ad72bd43ffd50658a72b787f7e07b231bb5b6fdd181be01573444f885ae48bb

The CSV digest is the normative reference for the task universe
(Section 3.1 of the protocol). The digest is authoritative
regardless of filename.

Task Corpus
-----------

Source: CISA Known Exploited Vulnerabilities (KEV) catalog
Snapshot date: 2026-08-20
Rows: 1,673
Columns: cve_id, vendor, product, vulnerability_name,
         short_description, vuln_class, date_added, due_date,
         known_ransomware, cwes
Vulnerability classes: 14 named + Unclassified (332, 19.8%)
Keyword classifier: deterministic, published in Section 3.2

Audit trail
-----------

12 rounds, 4 vendor families (Moonshot Kimi K3, OpenAI GPT-5.6
Sol, Google Gemini 3.1 Pro, Anthropic Claude Opus 4.6 producer).
75+ total findings, all addressed.

Carrying seat (Kimi K3): PASS at R5 and R10.
Adversarial seat (GPT-5.6 Sol): 7 adversarial rounds,
  finding trajectory 25 -> 9 -> 6 -> 4 -> 4 -> 4 -> 4.
Advisory seat (Gemini 3.1 Pro): PASS at R1, R5-VAL, R6-VAL,
  R7-VAL, R8-VAL, R9-VAL, R10.

Pre-run obligations
-------------------

This deposit freezes the benchmark DESIGN. The benchmark
MANIFEST (Section 10, 17 companion artifacts) must be hash-
bound and deposited before any pilot session begins. F-SB12
(non-waivable kill switch) invalidates any run without a
complete manifest.

License: CC-BY-4.0

---

# Bismillah ir-Rahman ir-Rahim
