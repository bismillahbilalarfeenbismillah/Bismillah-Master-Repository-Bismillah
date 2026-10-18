# Bismillah ir-Rahman ir-Rahim

# R0295 -- build_shvvp_v0_7_pdf.sh

**Chronological Index:** 363 of 995  
**Date:** 2026-07-26  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** build_shvvp_v0_7_pdf.sh  
**Source Format:** sh  
**SHA-256:** `12758daff48657afaed437b8357f9327de4613c03b7ef2c993a6468ed38e692c`  

---

## R0295 · build_shvvp_v0_7_pdf.sh

- section: V. BSSG & SHVVP Protocols
- source_file: build_shvvp_v0_7_pdf.sh
- source_format: sh
- merged_variants: 1 (build_shvvp_v0_6_pdf.sh)
- text_sha256: 12758daff48657afaed437b8357f9327de4613c03b7ef2c993a6468ed38e692c

#!/usr/bin/env bash
# Render SHV_VALIDATION_PROTOCOL_v0_7_source.md to the monochrome release flagship
# SHVVP_v0_7_flagship.pdf via pandoc -> pdflatex.
#
# Font note: the frozen flagship profile is Latin Modern (LMRoman/LMMono). Where
# lmodern.sty is unavailable in the build host, this script falls back to Computer
# Modern via T1 fontenc, the same Latin Modern family; the substitution is stated
# rather than implied and does not affect the finding F-P5-3 remedy, which concerns
# table legibility, not font identity. Table text is set at \footnotesize with long
# identifier hyphenation so every Section 8.2 cell renders within the text block.
set -euo pipefail
SRC="${1:-SHV_VALIDATION_PROTOCOL_v0_7_source.md}"
OUT="${2:-SHVVP_v0_7_flagship.pdf}"
WORK="$(mktemp -d)"
cp "$SRC" "$WORK/src.md"
# carry the one referenced raster if present alongside the source
[ -f shvvp-v0-5-phase-b-power.png ] && cp shvvp-v0-5-phase-b-power.png "$WORK/" || true
cd "$WORK"

pandoc src.md -s -o v06.tex \
  --pdf-engine=pdflatex --toc --number-sections \
  -V documentclass=article -V geometry:margin=1in -V fontsize=11pt \
  -V colorlinks=true -V linkcolor=black -V urlcolor=black -V toccolor=black \
  -V title="Structural Honesty Validation Protocol (SHVVP) v0.7" \
  -V author="Bilal Syed Arfeen (BayyinahEnterprise)" -V date="2026-07-26"

# lmodern fallback: drop the package if the host lacks it.
if ! kpsewhich lmodern.sty >/dev/null 2>&1; then
  sed -i '/^\\usepackage{lmodern}$/d' v06.tex
fi
# Computer Modern is non-scalable here, so disable microtype font expansion.
sed -i 's|^  \\usepackage\[\]{microtype}$|  \\usepackage[]{microtype}\n  \\microtypesetup{expansion=false}|' v06.tex
# Bare DOI identifiers in body text are single non-breakable tokens under the
# Computer Modern fallback; insert zero-width break opportunities. This matches the
# displayed "doi:10.5281/zenodo.N" text only, never the href URL argument
# (which is "doi.org/10.5281/zenodo.N", a different prefix).
sed -i 's#\(doi:10\.5281/\)#\1\\allowbreak{}#g' v06.tex
sed -i 's#\(doi:10\.5281/\\allowbreak{}zenodo\.\)#\1\\allowbreak{}#g' v06.tex
# Legible tables: small font, break long identifiers, tolerate tight lines.
python3 - <<'PY'
t=open("v06.tex").read()
inj=(r"\usepackage{etoolbox}"+"\n"
     r"\AtBeginEnvironment{longtable}{\footnotesize}"+"\n"
     r"\setlength{\emergencystretch}{3em}"+"\n"
     r"\IfFileExists{hyphenat.sty}{\usepackage[htt]{hyphenat}}{}"+"\n")
t=t.replace(r"\begin{document}", inj+r"\begin{document}",1)
open("v06.tex","w").write(t)
PY

pdflatex -interaction=nonstopmode -halt-on-error v06.tex >/dev/null
pdflatex -interaction=nonstopmode -halt-on-error v06.tex >/dev/null
qpdf --check v06.pdf >/dev/null && echo "qpdf: structurally OK"
cp v06.pdf "$OLDPWD/$OUT"
cd "$OLDPWD"
echo "wrote $OUT"
pdfinfo "$OUT" | grep -i pages

---

# Bismillah ir-Rahman ir-Rahim
