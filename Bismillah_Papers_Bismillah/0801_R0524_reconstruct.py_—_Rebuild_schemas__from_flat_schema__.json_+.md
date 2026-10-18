# Bismillah ir-Rahman ir-Rahim

# R0524 -- reconstruct.py — Rebuild schemas/ from flat schema__*.json + restore SHA256SUMS from .txt, so the code

**Chronological Index:** 801 of 995  
**Date:** Undated  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** reconstruct.py  
**Source Format:** py  
**SHA-256:** `4151a22915f811557381f0cfb7e2c42647cb1ebd02a53f630dcccdd89d897eb9`  

---

## R0524 · reconstruct.py — Rebuild schemas/ from flat schema__*.json + restore SHA256SUMS from .txt, so the code

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: reconstruct.py
- source_format: py
- text_sha256: 4151a22915f811557381f0cfb7e2c42647cb1ebd02a53f630dcccdd89d897eb9

#!/usr/bin/env python3
"""Rebuild schemas/ from flat schema__*.json + restore SHA256SUMS from .txt, so the code
and verifier run. Run this FIRST, then the commands in AUDIT_BRIEF_KIMI.md."""
import os, shutil
PAIRS = {
  'schema__authorization-receipt.schema.json': 'schemas/authorization-receipt.schema.json',
  'schema__correction-event.schema.json': 'schemas/correction-event.schema.json',
  'schema__effect-request.schema.json': 'schemas/effect-request.schema.json',
  'schema__execution-receipt.schema.json': 'schemas/execution-receipt.schema.json',
  'schema__lineage-record.schema.json': 'schemas/lineage-record.schema.json',
  'schema__witness-receipt.schema.json': 'schemas/witness-receipt.schema.json',
}
os.makedirs('schemas', exist_ok=True)
for flat, rp in PAIRS.items():
    open(rp, 'wb').write(open(flat, 'rb').read())
if os.path.exists('SHA256SUMS.txt') and not os.path.exists('SHA256SUMS'):
    shutil.copyfile('SHA256SUMS.txt', 'SHA256SUMS')
print('rebuilt', len(PAIRS), 'schema files + restored SHA256SUMS')

---

# Bismillah ir-Rahman ir-Rahim
