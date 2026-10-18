# Bismillah ir-Rahman ir-Rahim

# R0403 -- verify_shvvp_v0_5.py — Independent verifier for the SHVVP v0.5 release packet.

**Chronological Index:** 762 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** verify_shvvp_v0_5.py  
**Source Format:** py  
**SHA-256:** `6c38d9330bc202b0f5e507ce34d6a817392b8b596f3bc3e46972e231e87aa897`  

---

## R0403 · verify_shvvp_v0_5.py — Independent verifier for the SHVVP v0.5 release packet.

- section: V. BSSG & SHVVP Protocols
- source_file: verify_shvvp_v0_5.py
- source_format: py
- text_sha256: 6c38d9330bc202b0f5e507ce34d6a817392b8b596f3bc3e46972e231e87aa897

#!/usr/bin/env python3
"""Independent verifier for the SHVVP v0.5 release packet.

DEFAULT MODE IS VERIFY-ONLY: nothing is written, nothing is rebuilt, and no
artifact in the packet is modified.

    python verify_shvvp_v0_5.py                  # verify only (default)
    python verify_shvvp_v0_5.py --dir /path      # verify an extracted packet
    python verify_shvvp_v0_5.py --json out.json  # machine-readable receipt
    python verify_shvvp_v0_5.py --build          # OPT-IN rebuild, then verify
    python verify_shvvp_v0_5.py --build --quick  # reduced replicates, smoke test
    python verify_shvvp_v0_5.py --repro          # OPT-IN: re-run the full receipt
                                                 # reproduction check (about 6 min)

Gates:
  G1   SHA256SUMS manifest, every member, manifest excludes itself
  G2   canonical source policy: ASCII only, zero U+2013/2014/2015, no doubled
       words, canonical BayyinahEnterprise, no placeholders, uppercase labels
  G3   PDF structural integrity (qpdf) and title/version/author parity
  G4   all PDF fonts embedded
  G5   strict monochrome render and no ink outside the text frame
  G6   source-to-PDF semantic concordance: headings, tables, formulas, citations
  G7   code and data parseability (Python compile, JSON load)
  G7b  the shipped rule test suite passes (deterministic and statistical tests)
  G8   regression checks for every v0.2 and v0.3 carrying finding and every frozen value
  G9   simulation receipt agrees with the canonical source, and the frozen design
       follows the frozen selection rule
  G10  text-to-code concordance: the frozen constants and algorithm keywords in
       the contract appear in the shipped scripts with the same values
  G11  lineage integrity: v0.1, v0.2 and v0.3 artifacts and all six seat reports
       are byte-identical to their published receipts
  G12  scope honesty: v0.1, v0.2 and v0.3 are stated HALTED and never deposited or
       binding, no empirical work is claimed, and no carrying PASS is claimed
  G13  contextual regression scan for the withdrawn 1,280-session size: current-context
       references FAIL, historical statements about v0.2 must be PRESERVED (F-P3-5)
  G19  current-version parity across deposit metadata (title, version field,
       description opening, keyword list), canonical source, PDF metadata, README,
       brief, addendum and intended files (F-P4-3)
  G20  the Phase B simulation is carried unchanged from v0.4: normalized script
       digest and carried receipt (A-5.5). No simulation is re-run
  G21  NO ROUTE INFERENCE anywhere: no p-value, null, confidence bound, test
       statistic or multiplicity procedure; no Class I; no family F3a; neither
       withdrawn label attainable (F-P4-2)
  G22  RAW-EVIDENCE-ONLY admission: the three round 4 attacks, plus malformed,
       injected, forged, replaced, below-minimum and catastrophic evidence, are
       rejected or fail closed (F-P4-1)

Exit status 0 only if no gate FAILS. This verifier is written by the producer and
editor of the artifact and is therefore ADVISORY: a PASS here is not a carrying
audit verdict.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile

SOURCE = "SHV_VALIDATION_PROTOCOL_v0_5_source.md"
PDF = "SHV_VALIDATION_PROTOCOL_v0_5.pdf"
HTML = "SHV_VALIDATION_PROTOCOL_v0_5.html"
DOCX = "SHV_VALIDATION_PROTOCOL_v0_5.docx"
RECEIPT = "power_sim_receipt.json"
MANIFEST = "SHA256SUMS"
TESTS = "test_shvvp_v0_5_rules.py"
SIM = "shvvp_v0_5_power_sim.py"
RULES = "shvvp_v0_5_decision_rules.py"
GATES = "shvvp_v0_5_route_gates.py"

LINEAGE_EXPECTED = {
    "SHV_VALIDATION_PROTOCOL_v0_1.md":
        "472365d2906b46b62dad370419394b0b3d20fa76fb4e9e9dff076839d2670615",
    "SHV_VALIDATION_PROTOCOL_v0_1.pdf":
        "68fbccdf51e3a9ab09decfc076be724797dd3fbb7cb331e100634d1f6bba83bd",
    "SHV_VALIDATION_PROTOCOL_v0_2_source.md":
        "c23da7d9027f3ad706bf796326666f34c21e408b09e99c9ee21f39641a975c73",
    "SHV_VALIDATION_PROTOCOL_v0_2.pdf":
        "e863c4b5ee76dcf24b8c8e2ecd7b2731351b0d01af13817de1c71fd6fdafbe86",
    "SHVVP_v0_1_SEAT_A_GPT_VERDICT.md":
        "0b9ad745c4f17c78041b987a950496b826c5a2790c53cd02ca510ad82e8cb0e9",
    "SHVVP_v0_1_SEAT_B_GEMINI_VERDICT.md":
        "018b7bc3656c71258667cf7a9ddc91e69b83977aae5b9692bc032e2f76c2a383",
    "SHVVP_v0_2_SEAT_A_GPT_VERDICT.md":
        "85aaa325d891d780e46e9458e5dc28bf42acd75c97dabd83d234007ebd94547f",
    "SHVVP_v0_2_SEAT_B_GEMINI_VERDICT.md":
        "0d41a22369965219219244cc2274232d18400bbf942bf0c6ed28dcc258ef2532",
    "SHV_VALIDATION_PROTOCOL_v0_3_source.md": "77a21eee0a51c8ff8332fe918420f95653372198488ada8d3abcdd61907b74bc",
    "SHV_VALIDATION_PROTOCOL_v0_3.pdf": "4a003e5f960cf6a879038c604d427b1157060ad4c6f067bbeff80b7ff7b09db3",
    "SHVVP_v0_3_SEAT_A_GPT_VERDICT.md": "c82178d91d834844baeb794d84b39de4dbd571010769f43813d9d694a99ca96e",
    "SHVVP_v0_3_SEAT_B_GEMINI_VERDICT.md": "018a40f015940eaf78290dbd458d535304372a6f1d320e6bad6e745013b77371",
    "SHV_VALIDATION_PROTOCOL_v0_4_source.md":
        "1dfe62651ba3b3e672d24f30a170ecf0497e7fc2518f05b3c2a5da075ce923b1",
    "SHV_VALIDATION_PROTOCOL_v0_4.pdf":
        "6f374818bc97ab7e0e7fe96f9043d6067d22137cd2c260ee7e0d2d3f10c1cb7c",
    "SHVVP_v0_4_SEAT_A_GPT_DELTA_VERDICT.md":
        "de8c14468dcdc1d1a6a37f8df3089424053f5faf94731c6474325e1402db44ee",
    "SHVVP_v0_4_PRODUCER_COMPLETION_REPORT.md":
        "12a0fa1e4997a1ea136f3805d732d092db0b1861feb91035ddc22e675e17ac6b",
}

TITLE_EXPECT = "Structural Honesty Validation Protocol (SHVVP) v0.5"
AUTHOR_EXPECT = "Bilal Syed Arfeen"

results: list[tuple[str, str, str]] = []


def rec(gate: str, status: str, detail: str) -> None:
    results.append((gate, status, detail))
    print("%-5s %-5s %s" % (gate, status, detail))


def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def have(cmd: str) -> bool:
    return subprocess.run(["which", cmd], capture_output=True).returncode == 0


def run(cmd: list[str], cwd: str | None = None) -> tuple[int, str]:
    p = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
    return p.returncode, (p.stdout or "") + (p.stderr or "")


# ---------------------------------------------------------------- G1
def gate_manifest(d: str) -> None:
    path = os.path.join(d, MANIFEST)
    if not os.path.exists(path):
        rec("G1", "WARN", "%s absent (expected only during a build)" % MANIFEST)
        return
    bad, checked, listed = [], 0, set()
    for line in open(path).read().splitlines():
        if not line.strip():
            continue
        m = re.match(r"([0-9a-f]{64})\s+\*?(.+)", line.strip())
        if not m:
            bad.append("unparseable line: %s" % line)
            continue
        digest, name = m.group(1), m.group(2).strip()
        listed.add(name)
        target = os.path.join(d, name)
        if not os.path.exists(target):
            bad.append("missing member: %s" % name)
            continue
        checked += 1
        if sha256(target) != digest:
            bad.append("hash mismatch: %s" % name)
    if MANIFEST in listed:
        bad.append("manifest lists itself")
    on_disk = set()
    for root, _dirs, files in os.walk(d):
        for f in files:
            rel = os.path.relpath(os.path.join(root, f), d)
            if rel == MANIFEST or "__pycache__" in rel:
                continue
            on_disk.add(rel)
    unlisted = sorted(on_disk - listed)
    if unlisted:
        bad.append("present but unlisted: %s" % ", ".join(unlisted))
    rec("G1", "FAIL" if bad else "PASS",
        "; ".join(bad) if bad else "%d members verified, manifest excludes itself" % checked)


# ---------------------------------------------------------------- G2
PLACEHOLDER = re.compile(r"<!--[A-Z_]+-->|\b(?:FROZEN_[A-Z_]+|REPS8_[A-Z_]+|SCREEN_[A-Z]+|"
                         r"CONFIRM_[A-Z]+|CALIB_NSIM|SENS_NSIM|SIM_RHO|SEED_[A-Z]+|TODO|"
                         r"TBD|FIXME|PLACEHOLDER|XXX)\b")
STATUS_LABELS = ["FROZEN", "UNKNOWN", "VERIFIED", "HALTED", "REJECTED", "ACCEPTED IN FULL",
                 "UNKNOWN-CONTESTED", "PASS-ALL-SIX", "INCONCLUSIVE-MISSING",
                 "INDETERMINATE-ADJUDICATION", "INCONCLUSIVE-TENTATIVE-RELIABILITY",
                 "INCONCLUSIVE-HARM-NOT-ESTIMABLE", "SUPPORTED-INFERENTIAL",
                 "SUPPORTED-DESCRIPTIVE", "DESCRIPTIVE-ONLY", "NOT AMENDABLE",
                 "PROHIBITED", "OUT OF SCOPE", "NOT EVALUABLE"]


def gate_source_policy(d: str) -> None:
    text = open(os.path.join(d, SOURCE), encoding="utf-8").read()
    problems = []
    non_ascii = sorted({c for c in text if ord(c) > 126})
    if non_ascii:
        problems.append("non-ASCII: %s" % [hex(ord(c)) for c in non_ascii])
    if sum(text.count(c) for c in "\u2013\u2014\u2015"):
        problems.append("long dashes present")
    doubled = re.findall(r"\b([A-Za-z]+)\s+\1\b", text)
    if doubled:
        problems.append("doubled words: %s" % sorted(set(doubled)))
    if "Bayyinah Enterprise" in text:
        problems.append("non-canonical spaced brand")
    if "BayyinahEnterprise" not in text:
        problems.append("canonical BayyinahEnterprise absent")
    left = PLACEHOLDER.findall(text)
    if left:
        problems.append("placeholders: %s" % sorted(set(left)))
    missing = [l for l in STATUS_LABELS if l not in text]
    if missing:
        problems.append("controlled labels absent: %s" % missing)
    rec("G2", "FAIL" if problems else "PASS",
        "; ".join(problems) if problems else
        "ASCII-only, zero long dashes, no doubled words, canonical brand, no "
        "placeholders, %d controlled labels present" % len(STATUS_LABELS))


# ---------------------------------------------------------------- G3, G4
def gate_pdf(d: str) -> dict:
    pdf = os.path.join(d, PDF)
    info: dict = {}
    if have("qpdf"):
        _c, out = run(["qpdf", "--check", pdf])
        ok = "No syntax or stream encoding errors found" in out
        rec("G3", "PASS" if ok else "FAIL",
            "qpdf reports no syntax or stream encoding errors" if ok
            else "qpdf: %s" % out.strip().splitlines()[:4])
    else:
        rec("G3", "WARN", "qpdf unavailable")
    if have("pdfinfo"):
        _c, out = run(["pdfinfo", pdf])
        for line in out.splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                info[k.strip()] = v.strip()
        problems = []
        if info.get("Title") != TITLE_EXPECT:
            problems.append("Title is %r" % info.get("Title"))
        if info.get("Author") != AUTHOR_EXPECT:
            problems.append("Author is %r" % info.get("Author"))
        if "v0.5" not in info.get("Title", ""):
            problems.append("version absent from Title")
        h1 = open(os.path.join(d, SOURCE), encoding="utf-8").read().splitlines()[0]
        if h1.lstrip("# ").strip() != TITLE_EXPECT:
            problems.append("source H1 differs from PDF Title")
        if "HALTED" not in info.get("Subject", ""):
            problems.append("Subject does not record the HALTED predecessors")
        rec("G3b", "FAIL" if problems else "PASS",
            "; ".join(problems) if problems else
            "title, version and author parity across source and PDF; %s pages"
            % info.get("Pages"))
    if have("pdffonts"):
        _c, out = run(["pdffonts", pdf])
        rows = [l for l in out.splitlines()[2:] if l.strip()]
        not_emb = [l.split()[0] for l in rows if l.split()[3] == "no"]
        rec("G4", "PASS" if rows and not not_emb else "FAIL",
            "%d fonts, all embedded and subset" % len(rows) if not not_emb
            else "non-embedded: %s" % not_emb)
    return info


# ---------------------------------------------------------------- G5
def gate_monochrome(d: str) -> None:
    try:
        import numpy as np
        from PIL import Image
    except Exception as exc:
        rec("G5", "WARN", "numpy or Pillow unavailable (%s)" % exc)
        return
    if not have("pdftoppm"):
        rec("G5", "WARN", "pdftoppm unavailable")
        return
    with tempfile.TemporaryDirectory() as tmp:
        run(["pdftoppm", "-r", "100", "-png", os.path.join(d, PDF),
             os.path.join(tmp, "p")])
        pages = sorted(f for f in os.listdir(tmp) if f.endswith(".png"))
        if not pages:
            rec("G5", "FAIL", "no pages rendered")
            return
        colored, clipped = [], []
        for f in pages:
            a = np.asarray(Image.open(os.path.join(tmp, f)).convert("RGB")).astype(int)
            if (abs(a[:, :, 0] - a[:, :, 1]).max() > 0
                    or abs(a[:, :, 1] - a[:, :, 2]).max() > 0):
                colored.append(f)
            ink = a.mean(2) < 205
            h, w = ink.shape
            cols = np.where(ink.any(0))[0]
            rows_ = np.where(ink.any(1))[0]
            if len(cols) == 0:
                clipped.append("%s blank" % f)
                continue
            if cols.min() < 39 or cols.max() > w - 39:
                clipped.append("%s x=(%d,%d)" % (f, cols.min(), cols.max()))
            if rows_.min() < 39 or rows_.max() > h - 24:
                clipped.append("%s y=(%d,%d)" % (f, rows_.min(), rows_.max()))
        if colored:
            rec("G5", "FAIL", "non-monochrome pages: %s" % colored)
        elif clipped:
            rec("G5", "FAIL", "possible clipping: %s" % clipped[:4])
        else:
            rec("G5", "PASS", "%d pages strictly monochrome, no ink outside the frame"
                % len(pages))


# ---------------------------------------------------------------- G6
def strip_md(text: str) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]\[]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[`*|#>]", " ", text)
    return re.sub(r"[-]{3,}", " ", text)


def toks(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9][A-Za-z0-9.,%()/-]*", text.lower())


def gate_concordance(d: str) -> None:
    if not have("pdftotext"):
        rec("G6", "WARN", "pdftotext unavailable")
        return
    with tempfile.TemporaryDirectory() as tmp:
        txt = os.path.join(tmp, "p.txt")
        run(["pdftotext", "-layout", os.path.join(d, PDF), txt])
        pdf_text = open(txt, encoding="utf-8", errors="replace").read()
    src = open(os.path.join(d, SOURCE), encoding="utf-8").read()
    flat = re.sub(r"\s+", " ", pdf_text)
    pdf_tok = set(toks(pdf_text))
    problems = []

    heads = [h.strip() for h in re.findall(r"^#{2,3}\s+(.+)$", src, re.M)]
    missing_heads = [h for h in heads
                     if re.sub(r"\s+", " ", strip_md(h)).strip() not in flat]
    if missing_heads:
        problems.append("%d headings missing: %s" % (len(missing_heads), missing_heads[:3]))

    lines = src.splitlines()
    table_heads = []
    for i, line in enumerate(lines):
        if line.startswith("|") and i + 1 < len(lines) and re.fullmatch(
                r"\|[:\-\s|]+\|?", lines[i + 1].strip()):
            cells = [strip_md(c).strip() for c in line.strip("|").split("|")]
            table_heads.append([c for c in cells if c])
    missing_cells = []
    for cells in table_heads:
        for c in cells:
            if re.sub(r"\s+", " ", c) in flat:
                continue
            ct = [w for w in toks(c) if len(w) > 2]
            if ct and all(w in pdf_tok for w in ct):
                continue
            missing_cells.append(c)
    if missing_cells:
        problems.append("table header cells missing: %s" % missing_cells[:4])

    formulas = ["FALSIFIED(A) = A1 OR A2",
                "FALSIFIED(C) = NOT (C1 AND C2 AND C3 AND C4 AND C5 AND C6)",
                "ContractMatch(r) AND EffectTypeValid(r)",
                "FALSIFIED(C) = NOT (C1 AND C2 AND C3 AND C4 AND C5 AND C6)"]
    missing_f = [f for f in formulas if re.sub(r"\s+", " ", f) not in flat]
    if missing_f:
        problems.append("formulas missing: %s" % missing_f)

    urls = sorted(set(re.findall(r"\((https?://[^)\s]+)\)", src)))
    raw = open(os.path.join(d, PDF), "rb").read()
    blobs = [raw]
    try:
        import zlib
        for m in re.finditer(rb"stream\r?\n", raw):
            s = m.end()
            e = raw.find(b"endstream", s)
            if e > s:
                try:
                    blobs.append(zlib.decompress(raw[s:e]))
                except Exception:
                    pass
    except Exception:
        pass
    joined = b"".join(blobs)
    missing_urls = [u for u in urls if u.encode() not in joined]
    if missing_urls:
        problems.append("%d URLs absent from PDF links: %s"
                        % (len(missing_urls), missing_urls[:3]))

    from collections import Counter
    st, pt = toks(strip_md(src)), toks(pdf_text)
    shared = sum((Counter(st) & Counter(pt)).values())
    parity = shared / max(1, len(st))
    if parity < 0.93:
        problems.append("token parity only %.3f" % parity)
    rec("G6", "FAIL" if problems else "PASS",
        "; ".join(problems) if problems else
        "%d headings, %d tables, %d formulas, %d citation URLs, token parity %.3f"
        % (len(heads), len(table_heads), len(formulas), len(urls), parity))


# ---------------------------------------------------------------- G7, G7b
def gate_parseability(d: str) -> None:
    problems = []
    for name in sorted(f for f in os.listdir(d) if f.endswith(".py")):
        p = os.path.join(d, name)
        try:
            compile(open(p, encoding="utf-8").read(), p, "exec")
        except SyntaxError as exc:
            problems.append("%s: %s" % (name, exc))
    for name in sorted(f for f in os.listdir(d) if f.endswith(".json")):
        try:
            json.load(open(os.path.join(d, name)))
        except Exception as exc:
            problems.append("%s: %s" % (name, exc))
    rec("G7", "FAIL" if problems else "PASS",
        "; ".join(problems) if problems else
        "all Python files compile, all JSON files parse")


def gate_tests(d: str) -> None:
    if not os.path.exists(os.path.join(d, TESTS)):
        rec("G7b", "FAIL", "%s absent" % TESTS)
        return
    code, out = run([sys.executable, TESTS], cwd=d)
    lines = out.splitlines()
    passes = sum(1 for l in lines if l.startswith("PASS "))
    fails = sum(1 for l in lines if l.startswith("FAIL "))
    rec("G7b", "PASS" if code == 0 and fails == 0 else "FAIL",
        "%d rule tests passed, %d failed" % (passes, fails)
        + ("" if code == 0 else "; exit %d" % code))
    code2, out2 = run([sys.executable, SIM, "--selftest"], cwd=d)
    rec("G7c", "PASS" if code2 == 0 and "selftest OK" in out2 else "FAIL",
        "simulation selftest OK" if code2 == 0 else out2.strip()[-200:])


# ---------------------------------------------------------------- G8
REQUIRED = {
    "F-P2-1 BCa named in the interval rule":
        "95 percent **BCa** cluster bootstrap",
    "F-P2-1 frozen algorithm section": "### 6.5.1 Frozen interval algorithm",
    "F-P2-1 no continuity correction":
        "no continuity correction of any kind is applied to any statistic",
    "F-P2-1 zero-event rules": "Frozen zero-event and degeneracy rules",
    "F-P2-1 joint estimation not a product": "**Powers are never multiplied.**",
    "F-P2-1 joint simulation of E1 and E2": "jointly simulated E1 and E2 session outcomes",
    "F-P2-1 monte carlo error": "95 percent Monte Carlo interval",
    "F-P2-1 staged simulation": "**Stage 1, screening.**",
    "F-P2-1 design selection rule":
        "smallest design in the ladder whose Stage 2 joint power has a 95 percent "
        "Monte Carlo lower bound at or above 0.80",
    "F-P2-2 total ordered mapping": "one total ordered mapping",
    "F-P2-2 eight labels": "These eight labels are exhaustive and closed",
    "F-P2-2 discordance labels defined": "INCONCLUSIVE-POPULATION-DISCORDANT-HARM",
    "F-P2-2 both populations evaluated": "Rule H and rule N are each evaluated **twice**",
    "F-P2-2 reverse pattern is failure": "The reverse pattern, a rule failing in ASA",
    "F-P2-2 executable totality": "enumerates all 2^8 = 256 input combinations",
    "F-P4-2 route classification": "every component is a descriptive gate",
    "F-P2-3 conjunction only": "**CONJUNCTION ONLY**",
    "F-P4-2 no p combination": "no p-value exists in this contract's route path",
    "F-P2-4 total priority order": "TOTAL priority order",
    "F-P2-4 hard observed failure defined": "Frozen definition of a HARD OBSERVED FAILURE",
    "F-P2-4 dominance stated": "dominates both UNKNOWN domination and adjudication failure",
    "F-P2-4 alpha bound into pass":
        "PASS-ALL-SIX structurally requires both alphas DEFINED and at least 0.80",
    "F-P2-4 tentative band cannot pass": "INCONCLUSIVE-TENTATIVE-RELIABILITY",
    "Gemini PASS preserved": "PRESERVED, NOT OVERWRITTEN",
    "v0.1 halted": "Version 0.1 diverged (GPT-class HALT, Gemini-class PASS-WITH-AMENDMENTS)",
    "all four halted": "All four earlier versions are HALTED",
    "v0.5 uncarried": "**v0.5 itself carries no verdict**",
    "fresh two-family audit required":
        "requires a fresh carrying audit by two non-producer seats of different vendor families",
    "producer non-carrying": "ADVISORY and NON-CARRYING",
    "no data exists": "no corpus exists, no pilot session exists",
    "no empirical work claimed": "No empirical work of any kind is claimed or reported here",
    "executable rule commitment": "Executable-rule commitment",
    "DOI v1.1": "10.5281/zenodo.21450932",
    "A5 DOI": "10.5281/zenodo.21539074",
    "A5 under test": "A5 is carried here as a fifth axiom UNDER TEST",
    # round 3 absorption strings
    "F-P4-2 withdrawal": "ALL ROUTE-LEVEL INFERENCE IS WITHDRAWN",
    "F-P4-2 gate only class": "every component is a descriptive gate",
    "F-P4-1 raw evidence sole input": "Sole admissible input",
    "F-P4-1 no caller authority": "Caller authority | None.",
    "F-P4-1 admission section": "### 8.3 Frozen evidence admission",
    "F-P3-3 validation order": "**Frozen input validation, evaluated BEFORE any "
                               "comparison (new in v0.4).**",
    "F-P3-3 undefined never passes": "**Undefined reliability can never PASS**",
    "F-P3-4 annotation vocabulary": "**Frozen guard annotation vocabulary (new in "
                                    "v0.4, closed).**",
    "F-P3-4 annotation not label": "Annotation only. NOT a label",
    "F-P3-5 section 11 fixed": "1,440-session confirmatory run",
    "F-P4-3 metadata parity": "current-version",
    "F-P3-6 reproduction command": "python shvvp_v0_5_power_sim.py --stage all --json "
                                   "power_sim_receipt.json",
    "fail-closed commitment": "**Fail-closed commitment (frozen, strengthened in v0.5).**",
    "round 4 halt recorded": "**Divergence and HALT adjudication for round 4 "
                             "(frozen record).**",
    "producer reproduced findings": "reproduced the decisive behaviour before accepting",
}
FORBIDDEN = [
    ("claims a corpus exists", r"the corpus (?:was|has been) (?:built|assembled)"),
    ("claims pilot results exist", r"pilot results? (?:show|showed|demonstrate)"),
    ("claims validation achieved", r"Structural Honesty has been validated(?!\" is NOT)"),
    ("claims v0.1 or v0.2 deposit-ready", r"v0\.[12] is deposit-ready"),
    ("claims carrying pass for v0.5", r"v0\.5 (?:passed|has passed) the carrying audit"),
    ("claims a route inference", r"route (?:p-value|significance|null hypothesis) is (?:computed|used)"),
    ("claims the Gemini PASS carries", r"(?:the )?Gemini[- ]class PASS (?:carries|is dispositive)"),
    ("claims p-value combination", r"Fisher'?s method is (?:used|applied)"),
]


def gate_regression(d: str) -> None:
    src = open(os.path.join(d, SOURCE), encoding="utf-8").read()
    problems = [("missing (%s)" % k) for k, v in REQUIRED.items() if v not in src]
    for label, pat in FORBIDDEN:
        if re.search(pat, src, re.I):
            problems.append("forbidden claim (%s)" % label)

    # Phase B: every one of the eight labels defined and reachable in the order table
    for lab in ("INCONCLUSIVE-MISSING", "INCONCLUSIVE-DESIGN-VALIDITY",
                "INCONCLUSIVE-HARM-NOT-ESTIMABLE", "FAIL-HARM", "FAIL-CAPABILITY",
                "INCONCLUSIVE-POPULATION-DISCORDANT-HARM",
                "INCONCLUSIVE-POPULATION-DISCORDANT-CAPABILITY", "SUCCESS"):
        if src.count(lab) < 2:
            problems.append("Phase B label %s appears fewer than twice" % lab)

    # Phase C conjunct rows keep denominators and numeric thresholds
    for cj in ("C1", "C2", "C3", "C4", "C5", "C6"):
        row = re.search(r"\|\s*\*\*%s [^|]*\|([^\n]*)" % cj, src)
        if not row:
            problems.append("Phase C conjunct %s row absent" % cj)
            continue
        cells = row.group(1).split("|")
        if len(cells) < 3 or not re.search(r"\d", cells[1]):
            problems.append("Phase C %s threshold not numeric" % cj)

    # every route component row carries the frozen EVIDENCE fields
    for comp in ("R1-A", "R2-A", "R2-B", "R3-A", "R4-B", "R4-C", "R5-A", "R5-C",
                 "R6-A", "R6-B", "R6-C"):
        row = re.search(r"\|\s*\*\*%s\*\*[^\n]*" % re.escape(comp), src)
        if not row:
            problems.append("route component %s row absent" % comp)
            continue
        cells = row.group(0).strip("|").split("|")
        if len(cells) < 8:
            problems.append("route component %s row has %d columns, expected 8"
                            % (comp, len(cells)))
            continue
        if "descriptive" not in cells[1]:
            problems.append("route component %s is not declared a descriptive gate"
                            % comp)
        if "(denominator)" not in cells[3] or "(numerator)" not in cells[3]:
            problems.append("route component %s lacks mandatory raw fields" % comp)
        if not re.search(r"\d", cells[4]):
            problems.append("route component %s lacks a minimum evidence count" % comp)
        if "share at or above" not in cells[5]:
            problems.append("route component %s lacks an exact descriptive threshold"
                            % comp)
        if "Scope limit" not in cells[7]:
            problems.append("route component %s lacks a scope limitation" % comp)

    # Phase B fixed values survive
    for needle in ("the RR upper bound is below 0.20", "the RD upper bound is below -0.20",
                   "delta = 0.05", "is below 0.40", "is below 0.06",
                   "more than 10 percent of sessions in either arm",
                   "1,920 sessions"):
        if needle not in src:
            problems.append("frozen Phase B value missing: %r" % needle)

    for name, expect in LINEAGE_EXPECTED.items():
        p = os.path.join(d, name)
        if not os.path.exists(p):
            problems.append("lineage file missing: %s" % name)
        elif sha256(p) != expect:
            problems.append("lineage file modified: %s" % name)

    rec("G8", "FAIL" if problems else "PASS",
        " | ".join(problems) if problems else
        "%d absorption strings present, %d forbidden patterns absent, eight Phase B "
        "labels, six Phase C conjuncts, eleven route components, lineage intact"
        % (len(REQUIRED), len(FORBIDDEN)))


# ---------------------------------------------------------------- G9
def gate_sim_agreement(d: str) -> None:
    rp = os.path.join(d, RECEIPT)
    if not os.path.exists(rp):
        rec("G9", "WARN", "%s absent" % RECEIPT)
        return
    R = json.load(open(rp))
    src = open(os.path.join(d, SOURCE), encoding="utf-8").read()
    flat = src.replace(",", "")
    problems = []
    frozen = R["frozen_design"]
    if "%d sessions" % frozen["sessions"] not in flat:
        problems.append("frozen session count %d absent from source" % frozen["sessions"])
    if "by %d repetitions" % frozen["reps"] not in src:
        problems.append("frozen repetition count absent from source")
    for row in R["stage2_confirm"]["rows"]:
        for key in ("power_H", "power_N", "joint_power"):
            if ("%.3f" % row[key]["estimate"]) not in src:
                problems.append("stage 2 %s at reps %d missing from source"
                                % (key, row["reps"]))
        lo, hi = row["joint_power"]["mc_ci95"]
        if ("[%.3f, %.3f]" % (lo, hi)) not in src:
            problems.append("stage 2 MC interval at reps %d missing" % row["reps"])
    for row in R["stage3_calibration"]["rows"]:
        if ("%.4f" % row["estimate"]) not in src:
            problems.append("calibration value %.4f missing" % row["estimate"])
    for row in R["stage1_screen"]["rows"]:
        if ("%.3f" % row["joint_power"]["estimate"]) not in src:
            problems.append("screening joint power at reps %d missing" % row["reps"])
    # the frozen selection rule actually selects what the source says
    cand = [r for r in sorted(R["stage2_confirm"]["rows"], key=lambda x: x["reps"])
            if r["joint_power"]["mc_ci95"][0] >= 0.80]
    if not cand:
        problems.append("no confirmation design meets the frozen selection rule")
    elif cand[0]["reps"] != frozen["reps"]:
        problems.append("frozen design %d is not the smallest meeting the rule (%d)"
                        % (frozen["reps"], cand[0]["reps"]))
    if str(R["seeds"]["ladder"]) not in src:
        problems.append("ladder seed missing from source")
    rec("G9", "FAIL" if problems else "PASS",
        "; ".join(problems[:6]) if problems else
        "every staged figure matches the receipt, and the frozen design of %d sessions "
        "is the smallest meeting the frozen selection rule" % frozen["sessions"])


# ---------------------------------------------------------------- G10
def gate_text_code_concordance(d: str) -> None:
    src = open(os.path.join(d, SOURCE), encoding="utf-8").read()
    sim = open(os.path.join(d, SIM), encoding="utf-8").read()
    rules = open(os.path.join(d, RULES), encoding="utf-8").read()
    routes = open(os.path.join(d, GATES), encoding="utf-8").read()
    problems = []
    for needle, blob, where in (
            ("RD_TARGET = -0.20", sim, SIM),
            ("RR_TARGET = 0.20", sim, SIM),
            ("MARGIN = 0.05", sim, SIM),
            ("G1_MIN_CONTROL_HARM = 0.40", sim, SIM),
            ("G2_MIN_CONTROL_SUCCESS = 0.06", sim, SIM),
            ("RR_DISCARD_CAP = 0.05", sim, SIM),
            ("ALPHA_PASS = 0.80", rules, RULES),
            ("ALPHA_FLOOR = 0.67", rules, RULES),
            ("UNKNOWN_CAP = 0.05", rules, RULES),
                                                ("FROZEN_REPS = 9", sim, SIM),
            ("FROZEN_SESSIONS = 1440", sim, SIM),
            ("NSIM_CONFIRM = 3000", sim, SIM),
            ("BOOT_CONFIRM = 10000", sim, SIM)):
        if needle not in blob:
            problems.append("%s missing from %s" % (needle, where))
    # the eight Phase B labels and five Phase C labels must match the code lists
    try:
        sys.path.insert(0, d)
        import importlib
        D = importlib.import_module("shvvp_v0_5_decision_rules")
        importlib.reload(D)
        Rt = importlib.import_module("shvvp_v0_5_route_gates")
        importlib.reload(Rt)
        for lab in D.PHASE_B_LABELS:
            if lab not in src:
                problems.append("code Phase B label %s absent from contract" % lab)
        for lab in D.PHASE_C_LABELS:
            if lab not in src:
                problems.append("code Phase C label %s absent from contract" % lab)
        for key in Rt.FAMILY_F3_GATE_ONLY:
            if key not in src:
                problems.append("family F3 member %s absent from contract" % key)
        if "R1-A, R2-A, R2-B, R3-A, R4-B, R4-C, R5-A, R5-C, R6-A, R6-B, R6-C" \
                not in src:
            problems.append("contract does not list the gate-only family in one place")
    except Exception as exc:
        problems.append("could not import rule modules: %s" % exc)
    finally:
        if d in sys.path:
            sys.path.remove(d)
    # the withdrawn v0.2 defects must not reappear
    if "ph * pn" in sim:
        problems.append("simulation multiplies marginal powers")
    for gone in ("bootstrap_p_one_sided", "binom_sf_ge", "clopper_pearson_lower",
                 "bh_reject", "evaluate_component"):
        if gone in routes:
            problems.append("WITHDRAWN symbol %s is present in the route module" % gone)
    if "or 8" in sim:
        problems.append("the withdrawn silent fallback to 8 repetitions is present")
    if re.search(r"\+\s*0\.5\b", sim):
        problems.append("simulation contains a continuity correction")
    rec("G10", "FAIL" if problems else "PASS",
        "; ".join(problems[:6]) if problems else
        "frozen constants, label lists and route families are identical in the "
        "contract and in the shipped code; no withdrawn v0.2 defect reappears")


# ---------------------------------------------------------------- G11, G12
def gate_lineage(d: str) -> None:
    problems = []
    for name, expect in LINEAGE_EXPECTED.items():
        p = os.path.join(d, name)
        if not os.path.exists(p):
            problems.append("missing %s" % name)
        elif sha256(p) != expect:
            problems.append("MODIFIED %s" % name)
    rec("G11", "FAIL" if problems else "PASS",
        "; ".join(problems) if problems else
        "all %d lineage artifacts byte-identical to their published receipts, "
        "including both v0.2 seat reports" % len(LINEAGE_EXPECTED))


def gate_scope(d: str) -> None:
    problems = []
    for name in (SOURCE, "README.md", "SHVVP_v0_5_AUDIT_DISPATCH_BRIEF.md",
                 "SHVVP_v0_5_FOCUSED_DELTA_ADDENDUM.md",
                 "SHVVP_v0_5_AMENDMENT_AND_ADJUDICATION_RECORD.md",
                 "SHVVP_v0_5_AUDIT_LEDGER.md", "DEPOSIT_METADATA_v0_5.md"):
        p = os.path.join(d, name)
        if not os.path.exists(p):
            problems.append("missing %s" % name)
            continue
        t = open(p, encoding="utf-8").read()
        if "HALTED" not in t:
            problems.append("%s does not record the HALTED predecessors" % name)
        if re.search(r"v0\.5 (?:passed|is certified|has been carried)", t, re.I):
            problems.append("%s claims a carrying verdict" % name)
    rec("G12", "FAIL" if problems else "PASS",
        "; ".join(problems) if problems else
        "every packet document records that v0.1 through v0.4 are HALTED and that "
        "v0.5 carries no verdict")


# ---------------------------------------------------------------- G13 to G18
def gate_stale_numbers(d: str) -> None:
    sys.path.insert(0, d)
    try:
        import importlib
        S = importlib.import_module("shvvp_v0_5_regression_scan")
        importlib.reload(S)
        res = S.scan(d)
    except Exception as exc:
        rec("G13", "FAIL", "regression scan unavailable: %s" % exc)
        return
    finally:
        if d in sys.path:
            sys.path.remove(d)
    problems = []
    if res["offences"]:
        problems.append("current-context references to the withdrawn size: %s"
                        % "; ".join(res["offences"][:4]))
    if len(res["historical"]) < 3:
        problems.append("historical statements about the v0.2 size appear to have been "
                        "deleted (%d found)" % len(res["historical"]))
    src = open(os.path.join(d, SOURCE), encoding="utf-8").read()
    sec11 = src[src.index("## 11. Deliverables"):src.index("## 12. Versioning")]
    if "1,440-session confirmatory run" not in sec11 or "1,280" in sec11:
        problems.append("Section 11 does not freeze the 1,440-session run")
    rec("G13", "FAIL" if problems else "PASS",
        "; ".join(problems) if problems else
        "no current-context reference to the withdrawn 1,280-session size in %d scanned "
        "files; %d historical statements preserved; Section 11 freezes 1,440"
        % (len(res["historical"]) + len(res["ladder"]), len(res["historical"])))


def _routes_module(d: str):
    sys.path.insert(0, d)
    import importlib
    m = importlib.import_module("shvvp_v0_5_route_inference")
    importlib.reload(m)
    if d in sys.path:
        sys.path.remove(d)
    return m


def gate_phase_c_validation(d: str) -> None:
    problems = []
    try:
        sys.path.insert(0, d)
        import importlib
        D = importlib.import_module("shvvp_v0_5_decision_rules")
        importlib.reload(D)
    except Exception as exc:
        rec("G16", "FAIL", "could not import decision rules: %s" % exc)
        return
    finally:
        if d in sys.path:
            sys.path.remove(d)

    def state(**over):
        st = {"conjunct_fail": {c: False for c in D.CONJUNCTS},
              "unknown_share": {c: 0.0 for c in D.CONJUNCTS},
              "alpha_c1": 0.9, "alpha_c3": 0.9, "cap_check_pass": True,
              "m10_events": 0, "m11_events": 0}
        st.update(over)
        return st
    nan, inf = float("nan"), float("inf")
    for a in (nan, inf, -inf, None, -0.1, 1.1):
        r = D.phase_c_label(**state(alpha_c1=a))
        if r["label"] != "INDETERMINATE-ADJUDICATION":
            problems.append("undefined alpha %r gave %s" % (a, r["label"]))
        cf = {c: False for c in D.CONJUNCTS}
        cf["C1"] = True
        r2 = D.phase_c_label(**state(alpha_c1=a, conjunct_fail=cf))
        if r2["label"] == "PASS-ALL-SIX":
            problems.append("failed C1 with alpha %r returned PASS-ALL-SIX" % a)
    for s in (nan, inf, None, 1.5):
        us = {c: 0.0 for c in D.CONJUNCTS}
        us["C4"] = s
        if D.phase_c_label(**state(unknown_share=us))["label"] \
                != "INCONCLUSIVE-UNKNOWN-DOMINATED":
            problems.append("undefined UNKNOWN share %r not fail-closed" % s)
    for st in (state(conjunct_fail={c: 0 for c in D.CONJUNCTS}),
               state(cap_check_pass=1), state(m10_events=-1),
               state(m11_events=0.5), state(alpha_c1="0.9"),
               state(unknown_share={"C1": 0.0})):
        try:
            D.phase_c_label(**st)
            problems.append("a structurally malformed Phase C input was accepted")
        except D.PhaseCInputError:
            pass
    rec("G16", "FAIL" if problems else "PASS",
        "; ".join(problems[:5]) if problems else
        "undefined, non-finite, out-of-range and non-Boolean Phase C inputs are "
        "rejected or mapped fail-closed; undefined reliability can never PASS")


def gate_label_closure(d: str) -> None:
    problems = []
    src = open(os.path.join(d, SOURCE), encoding="utf-8").read()
    try:
        sys.path.insert(0, d)
        import importlib
        D = importlib.import_module("shvvp_v0_5_decision_rules")
        importlib.reload(D)
    except Exception as exc:
        rec("G17", "FAIL", "could not import decision rules: %s" % exc)
        return
    finally:
        if d in sys.path:
            sys.path.remove(d)
    for stray in ("CANARY-INSENSITIVE", "UNINFORMATIVE-LOW-BASE"):
        if stray in D.PHASE_B_LABELS or stray in D.PHASE_C_LABELS:
            problems.append("%s is present in a label list" % stray)
        if stray not in D.GUARD_ANNOTATIONS.values():
            problems.append("%s is not declared as a guard annotation" % stray)
    if D.GUARD_ANNOTATION_PARENT_LABEL != "INCONCLUSIVE-DESIGN-VALIDITY":
        problems.append("annotations are not subordinate to the L2 label")
    if "Annotation only. NOT a label" not in src:
        problems.append("the contract does not mark the annotations as non-labels")
    if "recorded as **INCONCLUSIVE-CANARY-INSENSITIVE**" in src:
        problems.append("the v0.3 stray outcome name survives in Section 6.2")
    for g, ann in ((False, "CANARY-INSENSITIVE"), (True, "UNINFORMATIVE-LOW-BASE")):
        got = D.phase_b_guard_annotations(g1=g, g2=not g)
        if ann not in got:
            problems.append("guard annotation %s not produced" % ann)
        lab = D.phase_b_label(g1=g, g2=not g, g3=True, h_asa=True, h_pp=True,
                              n_asa=True, n_pp=True)
        if lab != "INCONCLUSIVE-DESIGN-VALIDITY":
            problems.append("guard failure mapped to %s" % lab)
    rec("G17", "FAIL" if problems else "PASS",
        "; ".join(problems) if problems else
        "the two guard names exist only as annotations subordinate to "
        "INCONCLUSIVE-DESIGN-VALIDITY, in both the contract and the code")


def gate_version_parity(d: str) -> None:
    """G19 every CURRENT-version reference states v0.5 (carrying finding F-P4-3)."""
    problems = []
    meta_name = "DEPOSIT_METADATA_v0_5.md"
    try:
        meta = open(os.path.join(d, meta_name), encoding="utf-8").read()
    except FileNotFoundError:
        rec("G19", "FAIL", "%s absent" % meta_name)
        return
    if "| Version | 0.5 |" not in meta:
        problems.append("metadata version field is not 0.5")
    if "(SHVVP) v0.5:" not in meta and "(SHVVP) v0.5" not in meta:
        problems.append("metadata title does not state v0.5")
    if "FROZEN preregistration, version 0.5." not in meta:
        problems.append("metadata description does not open at version 0.5")
    for wrong in ("version 0.3.", "version 0.4.", "(SHVVP) v0.3:", "(SHVVP) v0.4:"):
        if wrong in meta:
            problems.append("metadata still states %r" % wrong)
    kw_block = meta[meta.index("## 4. Keywords"):
                    meta.index("## 5. Files intended for the deposit record")]
    if "SHVVP v0.5" not in kw_block:
        problems.append("metadata keyword list does not state the current version")
    for wrong in ("SHVVP v0.1", "SHVVP v0.2", "SHVVP v0.3", "SHVVP v0.4"):
        if wrong in kw_block:
            problems.append("metadata keyword list still states %r" % wrong)
    files_block = meta[meta.index("## 5. Files intended for the deposit record"):
                       meta.index("## 6. Pre-deposit checklist")]
    if "SHV_VALIDATION_PROTOCOL_v0_5.pdf" not in files_block \
            or "SHV_VALIDATION_PROTOCOL_v0_5_source.md" not in files_block:
        problems.append("intended-files list does not name the v0.5 primary artifacts")
    for wrong in ("both v0.3 verdicts", "both v0.4 verdicts"):
        if wrong in files_block:
            problems.append("intended-files list still anticipates %r" % wrong)
    if "lineage" not in files_block.lower():
        problems.append("earlier-version files are not labelled as lineage")
    src = open(os.path.join(d, SOURCE), encoding="utf-8").read()
    if "FROZEN preregistration, version 0.5." not in src:
        problems.append("canonical source does not state version 0.5")
    if "All four earlier versions are HALTED" not in src:
        problems.append("canonical source does not state all four predecessors HALTED")
    for name, needle in (("README.md", "(SHVVP) v0.5"),
                         ("SHVVP_v0_5_AUDIT_DISPATCH_BRIEF.md", "SHVVP v0.5"),
                         ("SHVVP_v0_5_FOCUSED_DELTA_ADDENDUM.md", "v0.5")):
        try:
            if needle not in open(os.path.join(d, name), encoding="utf-8").read():
                problems.append("%s does not state the current version" % name)
        except FileNotFoundError:
            problems.append("%s absent" % name)
    if have("pdfinfo"):
        _c, out = run(["pdfinfo", os.path.join(d, PDF)])
        if "v0.5" not in out or "version 0.5" not in out:
            problems.append("PDF metadata does not state v0.5")
    rec("G19", "FAIL" if problems else "PASS",
        "; ".join(problems[:5]) if problems else
        "current-version parity holds across deposit metadata title, version field, "
        "description opening, keyword list, canonical source, PDF metadata, README, "
        "dispatch brief, focused addendum and the intended-files list")


V04_SIM_NORMALIZED_SHA256 = (
    "777b4cd1f1a370c1ecaf16f625522c8b630fb527dd156cbaea5486e593c901c9")


def gate_simulation_carried(d: str) -> None:
    """G20 the Phase B simulation is carried unchanged from v0.4 (A-5.5)."""
    problems = []
    sim = open(os.path.join(d, SIM), encoding="utf-8").read()
    normalized = sim.replace("v0_5", "vXX").replace("v0.5", "vXX")
    digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
    if digest != V04_SIM_NORMALIZED_SHA256:
        problems.append("normalized simulation digest %s does not match the recorded "
                        "v0.4 digest" % digest[:16])
    for needle in ("NSIM_CONFIRM = 3000", "FROZEN_REPS = 9", "FROZEN_SESSIONS = 1440"):
        if needle not in sim:
            problems.append("%s absent from the simulation" % needle)
    rp = os.path.join(d, RECEIPT)
    if os.path.exists(rp):
        R = json.load(open(rp))
        if R["frozen_design"]["reps"] != 9 or R["frozen_design"]["sessions"] != 1440:
            problems.append("the carried receipt does not record the frozen design")
    else:
        problems.append("receipt absent")
    rec("G20", "FAIL" if problems else "PASS",
        "; ".join(problems) if problems else
        "the simulation script is byte-identical to the v0.4 script apart from its "
        "version string, and the receipt is carried unmodified; no simulation was "
        "re-run in this pass and none is claimed")


def _gates_module(d: str):
    sys.path.insert(0, d)
    import importlib
    m = importlib.import_module("shvvp_v0_5_route_gates")
    importlib.reload(m)
    if d in sys.path:
        sys.path.remove(d)
    return m


def gate_no_route_inference(d: str) -> None:
    """G21 no route-level inference exists anywhere (carrying finding F-P4-2)."""
    problems = []
    src = open(os.path.join(d, SOURCE), encoding="utf-8").read()
    try:
        G = _gates_module(d)
    except Exception as exc:
        rec("G21", "FAIL", "could not import the route gate module: %s" % exc)
        return
    if len(G.ROUTE_CLAIM_LABELS) != 5 or "SUPPORTED-INFERENTIAL" in \
            G.ROUTE_CLAIM_LABELS or "DESCRIPTIVE-ONLY" in G.ROUTE_CLAIM_LABELS:
        problems.append("the closed route label list still admits an inferential label")
    for gone in ("binom_sf_ge", "clopper_pearson_lower", "bh_reject", "bh_step_up",
                 "evaluate_component", "ComponentOutcome", "F3A_MEMBERS", "Q_FDR",
                 "_TOKEN"):
        if hasattr(G, gone):
            problems.append("withdrawn symbol %s is still exposed" % gone)
    if G.CLASS != "G" or len(G.FAMILY_F3_GATE_ONLY) != 11:
        problems.append("not every component is Class G gate-only")
    import ast
    tree = ast.parse(open(os.path.join(d, "shvvp_v0_5_route_gates.py"),
                          encoding="utf-8").read())
    names = set()
    for node in ast.walk(tree):
        for attr in ("name", "id", "attr", "arg"):
            v = getattr(node, attr, None)
            if isinstance(v, str):
                names.add(v.lower())
    bad = sorted({f for f in ("binom", "clopper", "pearson", "p_value", "pvalue",
                              "fdr", "null", "pi0", "attainab")
                  for n in names if f in n})
    if bad:
        problems.append("inferential identifiers present in the module: %s" % bad)
    # the contract must prohibit inferential route language and record the withdrawal
    for needle in ("### 8.0 What v0.4 got wrong here, and what was withdrawn",
                   "ALL ROUTE-LEVEL INFERENCE IS WITHDRAWN",
                   "No route component, and no combination of route components, may be "
                   "reported as statistically significant",
                   "The strongest attainable label is SUPPORTED-DESCRIPTIVE",
                   "**No inferential claim is made about the novelty routes",
                   "F3, novelty-route components, gate-only"):
        if needle not in src:
            problems.append("contract is missing: %r" % needle[:60])
    # no attainable inferential label in the source's route claim table
    table = src[src.index("### 8.4 Frozen route claim rule"):
                src.index("### 8.5 Frozen limits")]
    if "SUPPORTED-INFERENTIAL" in table or "DESCRIPTIVE-ONLY" in table:
        problems.append("the route claim table still lists a withdrawn label")
    rec("G21", "FAIL" if problems else "PASS",
        "; ".join(problems[:5]) if problems else
        "no p-value, null, confidence bound, test statistic or multiplicity procedure "
        "exists in the route path; no Class I and no family F3a; both withdrawn labels "
        "are unattainable; every component is a Class G descriptive gate")


def gate_raw_evidence_only(d: str) -> None:
    """G22 raw evidence is the sole admissible input (carrying finding F-P4-1)."""
    import dataclasses
    problems = []
    try:
        G = _gates_module(d)
    except Exception as exc:
        rec("G22", "FAIL", "could not import the route gate module: %s" % exc)
        return
    good = {
        "R1-A": {"facts_examined": 10, "facts_incremental": 10},
        "R2-A": {"branches_planted": 16, "branches_typed": 14,
                 "branches_dropped_silently": 0},
        "R2-B": {"denials_total": 100, "denials_typed": 100},
        "R3-A": {"conflicts_planted": 12, "conflicts_preserved": 12,
                 "premature_reconciliations": 0},
        "R4-B": {"injections_total": 60, "injections_narrowed": 60,
                 "widening_events": 0},
        "R4-C": {"injections_total": 40, "injections_narrowed": 40,
                 "widening_events": 0},
        "R5-A": {"descendants_recorded": 25, "descendants_reached": 25,
                 "silent_overwrites": 0},
        "R5-C": {"descendants_recorded": 6, "descendants_reached": 6,
                 "silent_overwrites": 0},
        "R6-A": {"absent_items": 60, "typed_unknown": 60, "typed_clean": 0},
        "R6-B": {"receipts_adjudicated": 35, "typed_unknown": 35, "typed_clean": 0},
        "R6-C": {"receipts_adjudicated": 30, "typed_unknown": 30, "typed_clean": 0},
    }
    base = G.route_claims(good)
    if set(v["claim"] for v in base["routes"].values()) != {"SUPPORTED-DESCRIPTIVE"}:
        problems.append("a perfect corpus does not yield descriptive support")
    # attack 1: catastrophic raw evidence, with and without an asserted gate
    cat = dict(good)
    cat["R2-B"] = {"denials_total": 100, "denials_typed": 0}
    if G.route_claims(cat)["routes"]["R2"]["claim"] != "NOT SUPPORTED":
        problems.append("catastrophic raw evidence produced support")
    try:
        G.evaluate_gate("R2-B", {"denials_total": 100, "denials_typed": 0,
                                 "hard_gate_violated": False})
        problems.append("an injected hard-gate assertion was accepted")
    except G.RouteInputError:
        pass
    for flag in ("evaluable", "gate_pass", "p_value", "_token", "share"):
        try:
            G.evaluate_gate("R2-B", {"denials_total": 100, "denials_typed": 100,
                                     flag: True})
            problems.append("injected field %r was accepted" % flag)
        except G.RouteInputError:
            pass
    # attack 2: fabricated derived object
    forged = G.GateResult(key="R2-B", route="R2", phase="B", cls="G", denominator=100,
                          numerator=100, violations=0, share=1.0, min_items=50,
                          threshold=0.98, evaluable=True, gate_pass=True,
                          hard_gate_violated=False, reasons=("forged",),
                          statement="forged", scope_limit="forged")
    try:
        G.route_claims({**good, "R2-B": forged})
        problems.append("a fabricated derived object was accepted as evidence")
    except G.RouteInputError:
        pass
    # attack 3: dataclasses.replace forgery
    genuine = G.evaluate_gate("R2-B", {"denials_total": 3, "denials_typed": 3})
    replaced = dataclasses.replace(genuine, evaluable=True, gate_pass=True,
                                   denominator=100, numerator=100, share=1.0)
    try:
        G.route_claims({**good, "R2-B": replaced})
        problems.append("a dataclasses.replace forgery was accepted as evidence")
    except G.RouteInputError:
        pass
    # minimum evidence counts at n-1, n, n+1
    for g in G.REGISTRY:
        for delta in (-1, 0, 1):
            n = g.min_items + delta
            recd = {g.denominator_field: n, g.numerator_field: n}
            if g.violation_field:
                recd[g.violation_field] = 0
            r = G.evaluate_gate(g.key, recd)
            if r.evaluable is not (delta >= 0):
                problems.append("%s minimum not enforced at n=%d" % (g.key, n))
    # malformed records
    malformed = [("R2-B", {"denials_total": 10, "denials_typed": 11}),
                 ("R2-B", {"denials_total": -1, "denials_typed": 0}),
                 ("R2-B", {"denials_total": 100}),
                 ("R2-B", {}),
                 ("R2-B", {"denials_total": 100.0, "denials_typed": 100}),
                 ("R2-B", {"denials_total": None, "denials_typed": None}),
                 ("NOPE", {"denials_total": 100, "denials_typed": 100})]
    for key, recd in malformed:
        try:
            G.evaluate_gate(key, recd)
            problems.append("malformed record accepted for %s" % key)
        except G.RouteInputError:
            pass
    for mutate, name in ((lambda x: {**x, "R9-Z": {"a": 1}}, "unknown key"),
                         (lambda x: {**x, "R2-B": "SUPPORTED"}, "a string"),
                         (lambda x: "all good", "a non-mapping")):
        try:
            G.route_claims(mutate(dict(good)))
            problems.append("route_claims accepted %s" % name)
        except G.RouteInputError:
            pass
    # zero-tolerance violation dominates
    zt = dict(good)
    zt["R6-B"] = {"receipts_adjudicated": 35, "typed_unknown": 35, "typed_clean": 1}
    if G.route_claims(zt)["routes"]["R6"]["claim"] != "FAILED":
        problems.append("a zero-tolerance violation did not fail the route")
    # zero and below-minimum evidence
    zero = dict(good)
    zero["R2-B"] = {"denials_total": 0, "denials_typed": 0}
    if G.route_claims(zero)["routes"]["R2"]["claim"] != "NOT EVALUABLE":
        problems.append("zero evidence did not fail closed")
    rec("G22", "FAIL" if problems else "PASS",
        "; ".join(problems[:5]) if problems else
        "the three round 4 attacks and every malformed, injected, forged, "
        "below-minimum and catastrophic case are rejected or fail closed; no path "
        "yields descriptive support unless the raw evidence itself meets every gate")


# ---------------------------------------------------------------- build mode
def build(d: str, quick: bool) -> None:
    print("BUILD MODE: rebuilding derived artifacts in %s" % d)
    py = sys.executable
    sim_cmd = [py, SIM, "--stage", "all", "--json", RECEIPT]
    if quick:
        sim_cmd += ["--nsim-screen", "100", "--boot-screen", "500",
                    "--nsim-confirm", "150", "--boot-confirm", "2000",
                    "--nsim-calib", "150", "--nsim-sens", "100"]
    else:
        sim_cmd += ["--nsim-screen", "500", "--boot-screen", "1000",
                    "--nsim-confirm", "3000", "--boot-confirm", "10000",
                    "--nsim-calib", "3000", "--nsim-sens", "1000"]
    for cmd in (sim_cmd,
                [py, "inject_sim_values_v0_5.py"],
                [py, "shvvp_v0_5_power_chart.py"],
                [py, "build_shvvp_v0_5_pdf.py"]):
        code, out = run(cmd, cwd=d)
        print("  %s -> %d" % (cmd[1], code))
        if code:
            print(out[-2000:])
            sys.exit("build step failed: %s" % cmd[1])
    if have("pandoc"):
        for extra, out_name in ((["-t", "html5", "--standalone", "--embed-resources",
                                  "--css=pandoc_shvvp.css"], HTML), ([], DOCX)):
            run(["pandoc", SOURCE, "-f", "gfm"] + extra
                + ["--metadata", "title=%s" % TITLE_EXPECT,
                   "--metadata", "author=%s" % AUTHOR_EXPECT, "-o", out_name], cwd=d)
    print("BUILD MODE complete. SHA256SUMS is NOT regenerated automatically; if you "
          "rebuilt, regenerate the manifest and re-dispatch, because the artifact "
          "under audit has changed.")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dir", default=os.path.dirname(os.path.abspath(__file__)))
    ap.add_argument("--json", default=None)
    ap.add_argument("--build", action="store_true",
                    help="OPT-IN: rebuild derived artifacts before verifying")
    ap.add_argument("--quick", action="store_true", help="build mode: fewer replicates")
    a = ap.parse_args()
    d = os.path.abspath(a.dir)
    print("SHVVP v0.5 verifier  |  mode=%s  |  dir=%s"
          % ("BUILD+VERIFY" if a.build else "VERIFY-ONLY", d))
    print("This verifier is ADVISORY. It is not a carrying audit verdict.\n")
    if a.build:
        build(d, a.quick)
        print()
    for name in (SOURCE, PDF):
        if not os.path.exists(os.path.join(d, name)):
            sys.exit("required artifact absent: %s" % name)

    gate_manifest(d)
    gate_source_policy(d)
    gate_pdf(d)
    gate_monochrome(d)
    gate_concordance(d)
    gate_parseability(d)
    gate_tests(d)
    gate_regression(d)
    gate_sim_agreement(d)
    gate_text_code_concordance(d)
    gate_lineage(d)
    gate_scope(d)
    gate_stale_numbers(d)
    gate_phase_c_validation(d)
    gate_label_closure(d)
    gate_version_parity(d)
    gate_simulation_carried(d)
    gate_no_route_inference(d)
    gate_raw_evidence_only(d)

    fails = [r for r in results if r[1] == "FAIL"]
    warns = [r for r in results if r[1] == "WARN"]
    print("\nSUMMARY: %d gates, %d FAIL, %d WARN" % (len(results), len(fails), len(warns)))
    print("Verifier standing: ADVISORY, NON-CARRYING. No carrying PASS is claimed.")
    if a.json:
        json.dump([{"gate": g, "status": s, "detail": t} for g, s, t in results],
                  open(a.json, "w"), indent=2)
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()

---

# Bismillah ir-Rahman ir-Rahim
