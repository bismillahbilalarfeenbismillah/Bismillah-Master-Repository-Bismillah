# Bismillah ir-Rahman ir-Rahim

# R0861 -- RESTORE_AND_RUN.txt

**Chronological Index:** 942 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** RESTORE_AND_RUN.txt  
**Source Format:** txt  
**SHA-256:** `a80aee8b5025d880bd74d2c7fbfef065cccd02ee8231464be6a749f97c130c9c`  

---

## R0861 · RESTORE_AND_RUN.txt

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: RESTORE_AND_RUN.txt
- source_format: txt
- text_sha256: a80aee8b5025d880bd74d2c7fbfef065cccd02ee8231464be6a749f97c130c9c

#!/bin/bash
# Run this script to restore original filenames and execute the audit.
# All .py.txt files become .py, .json.txt become .json, .md.txt become .md.
mkdir -p packet/schemas

for f in *.py.txt; do cp "$f" "packet/${f%.txt}"; done
for f in schemas_txt/*.json.txt; do
    base=$(basename "$f" .txt)
    cp "$f" "packet/schemas/$base"
done
for f in *.md.txt; do cp "$f" "packet/${f%.txt}"; done
cp SHA256SUMS.txt packet/SHA256SUMS

cd packet
echo "=== Verifying file integrity ==="
sha256sum -c SHA256SUMS
echo ""
echo "=== Running test suite ==="
python3 test_bssg_gate.py
echo ""
echo "=== Running counterexamples ==="
python3 bssg_counterexamples.py
echo ""
echo "=== Running model check ==="
python3 bssg_model_check.py
echo ""
echo "=== Running verifier ==="
python3 verify_bssg_v0_1.py
echo ""
echo "=== Gate smoke test ==="
python3 bssg_gate.py
echo ""
echo "=== Computing identity values ==="
python3 -c "
import hashlib, os
files = sorted([
    'bssg_attest.py', 'bssg_counterexamples.py', 'bssg_gate.py',
    'bssg_model_check.py', 'schemas/authorization-receipt.schema.json',
    'schemas/correction-event.schema.json', 'schemas/effect-request.schema.json',
    'schemas/execution-receipt.schema.json', 'schemas/lineage-record.schema.json',
    'schemas/witness-receipt.schema.json', 'test_bssg_gate.py', 'verify_bssg_v0_1.py',
])
MANIFEST = hashlib.sha256(''.join(
    hashlib.sha256(open(f,'rb').read()).hexdigest() for f in files
).encode()).hexdigest()
NONCE = 'BSSG-CARRY-KIMI-fc8133ea55a2bfb2'
challenge = hashlib.sha256((MANIFEST + NONCE).encode()).hexdigest()
print('MANIFEST:', MANIFEST)
print('CHALLENGE:', challenge)
"
echo ""
echo "=== Attestation ==="
python3 bssg_attest.py BSSG-CARRY-KIMI-fc8133ea55a2bfb2

---

# Bismillah ir-Rahman ir-Rahim
