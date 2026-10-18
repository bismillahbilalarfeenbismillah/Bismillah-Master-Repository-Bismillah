# Bismillah ir-Rahman ir-Rahim

# R0154 -- verify_dissertation_v1_4.py — Dissertation v1.4 publication verifier -- hardened rev B (gates run on all available text members, not PDF-only)."""

**Chronological Index:** 325 of 995  
**Date:** 2026-07-23  
**Section:** III. Structural Honesty — Core Papers  
**Source File:** verify_dissertation_v1_4.py  
**Source Format:** py  
**SHA-256:** `767be6439e0880663da1448ad036c00a7cc0cd8f887b00ae1501c2b10d0e4b86`  

---

## R0154 · verify_dissertation_v1_4.py — Dissertation v1.4 publication verifier -- hardened rev B (gates run on all available text members, not PDF-only)."""

- section: III. Structural Honesty — Core Papers
- source_file: verify_dissertation_v1_4.py
- source_format: py
- text_sha256: 767be6439e0880663da1448ad036c00a7cc0cd8f887b00ae1501c2b10d0e4b86

#!/usr/bin/env python3
"""Dissertation v1.4 publication verifier -- hardened rev B (gates run on all available text members, not PDF-only)."""
import re, subprocess, sys, hashlib, os
fails = []
if os.path.exists('SHA256SUMS.txt'):
    for line in open('SHA256SUMS.txt'):
        hsh, f = line.split(None,1); f = f.strip()
        if f == 'SHA256SUMS.txt': continue
        if os.path.exists(f):
            if hashlib.sha256(open(f,'rb').read()).hexdigest() != hsh: fails.append(f"hash mismatch: {f}")
corpus = ""
for f in ['Structural_Honesty_Dissertation_v1_4_source.md','Structural_Honesty_Dissertation_v1_4_canon.md','Structural_Honesty_Dissertation_v1_4.html']:
    if os.path.exists(f): corpus += open(f,encoding='utf-8',errors='replace').read()
if os.path.exists('Structural_Honesty_Dissertation_v1_4.docx'):
    corpus += subprocess.run(['unzip','-p','Structural_Honesty_Dissertation_v1_4.docx','word/document.xml'],capture_output=True,text=True).stdout
pdf = 'Structural_Honesty_Dissertation_v1_4.pdf'
lines = []
if os.path.exists(pdf):
    txt = subprocess.run(['pdftotext',pdf,'-'],capture_output=True,text=True).stdout
    lines = txt.split('\n'); corpus += txt
corpus = re.sub(r'\s+',' ',re.sub(r'-\s*\n\s*','',re.sub(r'<[^>]+>',' ',corpus)))
if not corpus: fails.append("no text members found to gate")
else:
    for t in ["Version 1.2 canonical","(Arfeen 2026, forthcoming)","Pre-publication working draft of Chapter","toward v1.0 publication targeted","During the present pre-publication phase","section is a placeholder","remove at submission","build profile"]:
        if t in corpus: fails.append(f"stale/meta literal present: {t[:44]}")
    for t in ["Prepared with Claude","not independent human peer review","An Independent Research Monograph","completeness-boundary treatment","reports accuracy, not AUROC","see the corrected bibliography entry sheshadri2025","The Muslim World","the public-deposit version","v1.4 (July 23, 2026)"]:
        if t not in corpus: fails.append(f"required marker missing: {t[:44]}")
    if corpus.count("finite judgment-set adequacy relative to the named set") < 2: fails.append("T83 propagation count < 2")
if os.path.exists('DEPOSIT_METADATA_v1_4.md'):
    md = open('DEPOSIT_METADATA_v1_4.md').read()
    if "version 1.3" in md: fails.append("metadata carries stale spelled version")
    if "version 1.4" not in md: fails.append("metadata missing current spelled version")
if os.path.exists('Structural_Honesty_Dissertation_audit_ledger.md'):
    lg = open('Structural_Honesty_Dissertation_audit_ledger.md').read()
    if "Section: v1.4" not in lg: fails.append("ledger missing governing v1.4 section")
if lines:
    def fh(label, frag):
        return any(l.strip()==label and all(w in ' '.join(lines[i+1:i+6]) for w in (frag.split()[0],frag.split()[-1])) for i,l in enumerate(lines))
    for n,f in {1:"Structural-Honesty Hypothesis",8:"Integrative Evaluation",15:"SI3 Munafiq",22:"Recursive Self-Application",23:"Preservation Strategy"}.items():
        if not fh(f"Chapter {n}",f): fails.append(f"chapter {n} identity")
    if not (fh("Appendix D","Standing Rulings") and fh("Appendix E","Publication History")): fails.append("appendix identity")
    if sum(1 for l in lines if re.match(r'^\s*#{1,6} ',l)): fails.append("literal # in render")
print("VERIFIER:", "ALL PASS" if not fails else "FAIL: " + "; ".join(fails[:8]))
sys.exit(0 if not fails else 1)

---

# Bismillah ir-Rahman ir-Rahim
