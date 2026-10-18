# Bismillah ir-Rahman ir-Rahim

# R0296 -- build_shvvp_v0_8_pdf.sh

**Chronological Index:** 352 of 995  
**Date:** 2026-07-25  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** build_shvvp_v0_8_pdf.sh  
**Source Format:** sh  
**SHA-256:** `b7122de5c6d92b1904a3ca03f9884ebe25f3ae59e3870d4c1e7c04ec27fae66d`  

---

## R0296 · build_shvvp_v0_8_pdf.sh

- section: V. BSSG & SHVVP Protocols
- source_file: build_shvvp_v0_8_pdf.sh
- source_format: sh
- text_sha256: b7122de5c6d92b1904a3ca03f9884ebe25f3ae59e3870d4c1e7c04ec27fae66d

#!/usr/bin/env bash
# Flagship render: pdflatex + Type-1 Latin Modern (lmodern), embedded fonts, Unicode
# maps, searchable text, and full PDF metadata (title/author/subject/keywords). F-R8-PUB-5/6.
set -euo pipefail
SRC="${1:-SHV_VALIDATION_PROTOCOL_v0_8_source.md}"; OUT="${2:-SHVVP_v0_8_flagship.pdf}"
TITLE="Structural Honesty Validation Protocol (SHVVP) v0.8"
AUTHOR="Bilal Syed Arfeen (BayyinahEnterprise)"
pandoc "$SRC" -f markdown-smart -o "$OUT" --pdf-engine=pdflatex \
  -V title="$TITLE" -V "title-meta=$TITLE" \
  -V author="$AUTHOR" -V "author-meta=$AUTHOR" -V date="2026-07-25" \
  -V fontfamily=lmodern -V fontenc=T1 -V fontsize=10pt -V geometry=margin=1in -V colorlinks=false \
  --highlight-style=monochrome \
  -V header-includes='\usepackage{fvextra}\DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,breakanywhere,commandchars=\\\{\}}' \
  -M subject="Frozen preregistration for cyber-agent structural-honesty validation" \
  -M keywords="structural honesty; preregistration; AI safety; cyber-agent evaluation; two-family carrying audit"
qpdf --check "$OUT" >/dev/null 2>&1 && echo "qpdf: structurally OK" || echo "qpdf: warnings"
echo "wrote $OUT"

---

# Bismillah ir-Rahman ir-Rahim
