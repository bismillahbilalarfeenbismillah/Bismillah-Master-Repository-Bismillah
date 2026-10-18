# Bismillah ir-Rahman ir-Rahim

# R0530 -- run_v0_5_regression.sh

**Chronological Index:** 807 of 995  
**Date:** Undated  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** run_v0_5_regression.sh  
**Source Format:** sh  
**SHA-256:** `db18070a4cc11aebe24893643be1babd1971608fd019da267a9b07c0c2bcd849`  

---

## R0530 · run_v0_5_regression.sh

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: run_v0_5_regression.sh
- source_format: sh
- text_sha256: db18070a4cc11aebe24893643be1babd1971608fd019da267a9b07c0c2bcd849

#!/usr/bin/env bash
# The four v0.5 files at top level are byte-identical PROVENANCE copies checked by the
# verifier's G10. The v0.5 regression suite needs the COMPLETE v0.5 module set, which
# ships intact under lineage/. This wrapper runs it there.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
V05="$(find "$HERE/lineage" -type d -name shvvp_v0_5_release | awk '{print length, $0}' | sort -n | tail -1 | cut -d' ' -f2-)"
[ -n "$V05" ] || { echo "v0.5 lineage release not found"; exit 1; }
echo "running v0.5 regression in: $V05"
( cd "$V05" && python3 test_shvvp_v0_5_rules.py )

---

# Bismillah ir-Rahman ir-Rahim
