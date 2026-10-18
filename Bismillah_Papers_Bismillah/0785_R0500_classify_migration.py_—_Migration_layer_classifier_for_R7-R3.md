# Bismillah ir-Rahman ir-Rahim

# R0500 -- classify_migration.py — Migration layer classifier for R7-R31 Class A findings.

**Chronological Index:** 785 of 995  
**Date:** Undated  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** classify_migration.py  
**Source Format:** py  
**SHA-256:** `1c8fadd31d9fc077bba748d4e0cd074a69b3979d924969c001db18f8fe17af9e`  

---

## R0500 · classify_migration.py — Migration layer classifier for R7-R31 Class A findings.

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: classify_migration.py
- source_format: py
- text_sha256: 1c8fadd31d9fc077bba748d4e0cd074a69b3979d924969c001db18f8fe17af9e

#!/usr/bin/env python3
"""Migration layer classifier for R7-R31 Class A findings.
Reads findings.csv, outputs migration_classification.csv.
Layer assignment: keyword matching against locus+description; highest-scoring layer wins."""
import csv, re
from collections import Counter

CODE_TERMS = ['BUILD.PY', 'PYTEST', 'TEST_', '.PY`', '.PY]', 'GATE [', 'GATE[',
              'CI V0', 'CI-', 'REGISTER_GEN', 'EXTRACT_FINDINGS', 'FINDINGS_INDEX',
              'UNIQUE_FINDINGS']
XLAYER_TERMS = ['SECTION 0.1', 'STATUS LINE', 'FRONT-MATTER', 'FRONT MATTER',
                'SECTION 25', 'FB-7B', 'FB-4', 'FB-5', 'TITLE', 'STATUS:',
                'CARRY STATUS', 'ENTRY RANGE']
PROV_TERMS = ['SECTION 27', 'SECTION 22', 'AMENDMENT', 'HISTORY.SHA256',
              'PRIOR_HISTORY', 'APPEND-ONLY', 'SEALED ENTRIES', 'RESEALED']
METH_TERMS = ['METHODOLOGY', 'TAGGING', 'DISPATCH', 'TRIAGE', 'AUDIT_CONTEXT',
              'WITNESS', 'SCRIBE']

def classify(locus, desc):
    combined = (locus + " " + desc).upper()
    scores = {
        'Code/CI': sum(1 for t in CODE_TERMS if t in combined),
        'Cross-layer consistency': sum(1 for t in XLAYER_TERMS if t in combined),
        'Provenance/amendment': sum(1 for t in PROV_TERMS if t in combined),
        'Methodology/dispatch': sum(1 for t in METH_TERMS if t in combined),
    }
    max_score = max(scores.values())
    if max_score == 0:
        return 'Other/unclassified', 'No layer-specific terms matched'
    matched = [k for k, v in scores.items() if v > 0]
    primary = max(scores, key=scores.get)
    if len(matched) > 1:
        return primary, f"Mixed-layer ({', '.join(matched)}); primary={primary}"
    return primary, f"Matched {scores[primary]} {primary} term(s)"

with open('findings.csv') as fin, open('migration_classification.csv', 'w', newline='') as fout:
    w = csv.writer(fout)
    w.writerow(['finding_id','round_number','version','migration_layer',
                'coding_rationale','locus_excerpt','description_excerpt'])
    for row in csv.DictReader(fin):
        rn = row['round_number'].strip()
        if rn and rn != '0' and 7 <= int(float(rn)) <= 31 and row['finding_class'] == 'Class A':
            layer, rationale = classify(row['locus'], row['description'])
            w.writerow([row['finding_id'], int(float(rn)), row['version'],
                        layer, rationale, row['locus'][:100], row['description'][:100]])

---

# Bismillah ir-Rahman ir-Rahim
