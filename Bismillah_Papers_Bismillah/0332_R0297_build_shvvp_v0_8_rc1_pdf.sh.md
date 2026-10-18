# Bismillah ir-Rahman ir-Rahim

# R0297 -- build_shvvp_v0_8_rc1_pdf.sh

**Chronological Index:** 332 of 995  
**Date:** 2026-07-24  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** build_shvvp_v0_8_rc1_pdf.sh  
**Source Format:** sh  
**SHA-256:** `84c9b278c676e5ffcd7119b5ab5abfe2b0a7f21388ae07ab887857efaa998b09`  

---

## R0297 · build_shvvp_v0_8_rc1_pdf.sh

- section: V. BSSG & SHVVP Protocols
- source_file: build_shvvp_v0_8_rc1_pdf.sh
- source_format: sh
- text_sha256: 84c9b278c676e5ffcd7119b5ab5abfe2b0a7f21388ae07ab887857efaa998b09

#!/usr/bin/env bash
set -euo pipefail
SRC="${1:-SHV_VALIDATION_PROTOCOL_v0_8_rc1_source.md}"
OUT="${2:-SHVVP_v0_8_rc1_flagship.pdf}"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT
cp "$SRC" "$WORK/src.md"
[ -f shvvp-v0-5-phase-b-power.png ] && cp shvvp-v0-5-phase-b-power.png "$WORK/" || true
cd "$WORK"
pandoc src.md -s -o v08.tex --pdf-engine=pdflatex --toc --number-sections \
  -V documentclass=article -V geometry:margin=1in -V fontsize=11pt \
  -V colorlinks=true -V linkcolor=black -V urlcolor=black -V toccolor=black \
  -V title="Structural Honesty Validation Protocol (SHVVP) v0.8-rc1" \
  -V author="Bilal Syed Arfeen (BayyinahEnterprise)" -V date="Revision candidate 2026-07-24"
if ! kpsewhich lmodern.sty >/dev/null 2>&1; then sed -i '/^\\usepackage{lmodern}$/d' v08.tex; fi
sed -i 's|^  \\usepackage\[\]{microtype}$|  \\usepackage[]{microtype}\n  \\microtypesetup{expansion=false}|' v08.tex
sed -i 's#\(doi:10\.5281/\)#\1\\allowbreak{}#g' v08.tex
sed -i 's#\(doi:10\.5281/\\allowbreak{}zenodo\.\)#\1\\allowbreak{}#g' v08.tex
python3 - <<'PY'
t=open('v08.tex').read()
inj=(r"\usepackage{etoolbox}"+"\n"+r"\AtBeginEnvironment{longtable}{\footnotesize}"+"\n"+r"\setlength{\emergencystretch}{3em}"+"\n"+r"\IfFileExists{hyphenat.sty}{\usepackage[htt]{hyphenat}}{}"+"\n")
t=t.replace(r"\begin{document}",inj+r"\begin{document}",1)
open('v08.tex','w').write(t)
PY
pdflatex -interaction=nonstopmode -halt-on-error v08.tex >/dev/null
pdflatex -interaction=nonstopmode -halt-on-error v08.tex >/dev/null
pdfinfo v08.pdf >/dev/null
cp v08.pdf "$OLDPWD/$OUT"
echo "wrote $OUT"
pdfinfo "$OLDPWD/$OUT" | grep -i '^Pages'

---

# Bismillah ir-Rahman ir-Rahim
