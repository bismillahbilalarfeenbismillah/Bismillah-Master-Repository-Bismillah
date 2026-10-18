# Bismillah ir-Rahman ir-Rahim

# R0963 -- SETUP_RENAME.txt

**Chronological Index:** 977 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** SETUP_RENAME.txt  
**Source Format:** txt  
**SHA-256:** `527682eee82a2691e11088691e1dad364081fce7040c7e1fd1cafe8688f1d036`  

---

## R0963 · SETUP_RENAME.txt

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: SETUP_RENAME.txt
- source_format: txt
- text_sha256: 527682eee82a2691e11088691e1dad364081fce7040c7e1fd1cafe8688f1d036

#!/bin/bash
mkdir -p xz_audit && cd xz_audit
for f in ../*.py.txt; do base=$(basename "$f" .txt); cp "$f" "./$base"; done
cp ../xz_protocol_trust_roots_PUBLIC.json.txt ./xz_protocol_trust_roots_PUBLIC.json
cp ../HISTORY.sha256.txt ./HISTORY.sha256
cp ../PACKET_SHA256SUMS.txt ./PACKET_SHA256SUMS
cp ../xz_protocol_v0_26.md ./ && cp ../xz_protocol_v0_26.pdf ./
echo "Ready. Run: sha256sum -c PACKET_SHA256SUMS && python3 build.py"

---

# Bismillah ir-Rahman ir-Rahim
