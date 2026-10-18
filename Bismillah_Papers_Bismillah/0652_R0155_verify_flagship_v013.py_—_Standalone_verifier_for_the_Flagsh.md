# Bismillah ir-Rahman ir-Rahim

# R0155 -- verify_flagship_v013.py — Standalone verifier for the Flagship v0.13 publication set (BayyinahEnterprise).

**Chronological Index:** 652 of 995  
**Date:** Undated  
**Section:** III. Structural Honesty — Core Papers  
**Source File:** verify_flagship_v013.py  
**Source Format:** py  
**SHA-256:** `c422b13ccf6dcb60d5a96c3461f43af6a50a32d71b446e05885ccb2c9f616853`  

---

## R0155 · verify_flagship_v013.py — Standalone verifier for the Flagship v0.13 publication set (BayyinahEnterprise).

- section: III. Structural Honesty — Core Papers
- source_file: verify_flagship_v013.py
- source_format: py
- merged_variants: 1 (verify_flagship_v012.py)
- text_sha256: c422b13ccf6dcb60d5a96c3461f43af6a50a32d71b446e05885ccb2c9f616853

#!/usr/bin/env python3
"""Standalone verifier for the Flagship v0.13 publication set (BayyinahEnterprise).
Checks: (1) every SHA256SUMS.txt entry; (2) the append-only ledger chain
(frozen v0.11 prefix at 21,721 bytes must hash 5c5f7b4c...); (3) the bib
delta (removing line 1 byte-preservingly must reproduce the frozen v0.11
bib hash 56c8e245...); (4) wrap-immune presence parity on available
surfaces; (5) the META-TEXT-ABSENCE gate (zero drafting-process markers).
Run in the directory containing the set. Exit 0 = ALL PASS."""
import hashlib, pathlib, re, sys, subprocess

def sha(b): return hashlib.sha256(b).hexdigest()
ok = True
def check(name, cond):
    global ok
    print(("PASS " if cond else "FAIL "), name); ok = ok and cond

for line in pathlib.Path("SHA256SUMS.txt").read_text().splitlines():
    if not line.strip(): continue
    h, f = line.split(None, 1)
    p = pathlib.Path(f.strip())
    check(f"receipt {p.name}", p.exists() and sha(p.read_bytes()) == h)

led = pathlib.Path("Flagship_paper_audit_ledger.md").read_bytes()
check("ledger frozen v0.11 prefix (21,721 bytes -> 5c5f7b4c...)",
      sha(led[:21721]).startswith("5c5f7b4c2afd0bbd"))

bib = pathlib.Path("Flagship_paper_bibliography.bib").read_bytes()
check("bib minus line 1 (byte-preserving) -> frozen v0.11 bib 56c8e245...",
      sha(bib.split(b"\n",1)[1]).startswith("56c8e245a8ae15f9"))

def norm(t):
    t = t.replace("-\n","").replace("\u00ad","")
    return re.sub(r"\s+"," ", t)
present = ["Author note:", "drafting instrument disclosed in the author note",
           "zero of forty-four", "recorded as incomplete rather than resolved",
           "tasks longer than eight hours, at least 16 percent",
           "accompanying bibliography file, Flagship_paper_bibliography.bib", "[35]"]
absent  = ["placeholder", "at build time", "raw markdown", "build profile",
           "F-audit", "not part of this packet", "Flagship_paper_references.bib", "[36]"]
src = norm(pathlib.Path("Flagship_paper_v0_13_source.md").read_text(encoding="utf-8").replace("\\[","[").replace("\\]","]"))
surfaces = {"source": src, "html": norm(pathlib.Path("Flagship_paper_v0_13.html").read_text(encoding="utf-8"))}
try:
    subprocess.run(["pdftotext","Flagship_paper_v0_13.pdf","/tmp/_v13.txt"], check=True, capture_output=True)
    surfaces["pdf"] = norm(pathlib.Path("/tmp/_v13.txt").read_text(encoding="utf-8"))
except Exception:
    print("NOTE  pdf text extraction unavailable; pdf parity skipped")
for name, t in surfaces.items():
    for tok in present: check(f"{name}: present: {tok!r}", tok in t)
    for tok in absent:  check(f"{name}: absent: {tok!r}", tok not in t)

print("RESULT:", "ALL PASS" if ok else "FAILURES ABOVE"); sys.exit(0 if ok else 1)

---

# Bismillah ir-Rahman ir-Rahim
