# Bismillah ir-Rahman ir-Rahim

# R0507 -- extract_corpus.py — XZ Protocol Audit Corpus Extractor v0.6

**Chronological Index:** 791 of 995  
**Date:** Undated  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** extract_corpus.py  
**Source Format:** py  
**SHA-256:** `c0622f824947eb036fc917e4318a8b41de85b6553257da9e05d28b37fee64df6`  

---

## R0507 · extract_corpus.py — XZ Protocol Audit Corpus Extractor v0.6

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: extract_corpus.py
- source_format: py
- text_sha256: c0622f824947eb036fc917e4318a8b41de85b6553257da9e05d28b37fee64df6

#!/usr/bin/env python3
"""
XZ Protocol Audit Corpus Extractor v0.6
========================================
Construction procedure for the XZ Structural Honesty Audit Corpus.
Versioned: v0.6 (post-R4 absorption -- locus boundary fix, description cleanup).

Walks all seat reports from the audit archive, extracts:
  1. Report-level metadata (round, version, seat, model family, role, verdict)
  2. Per-finding structured data (ID, severity, class, locus, description)
  3. Round-version-seat coverage matrix

Outputs:
  - reports.csv     (one row per report)
  - findings.csv    (one row per finding)
  - coverage.csv    (one row per report, keyed on filename)
  - summary.json    (aggregate statistics, includes extractor_version)
  - extraction.log  (operational log, not a data product)

Safety gate: no XZ Utils payload, activation, or reconstruction content
is extracted -- findings concern the protocol TEXT, not the backdoor.
"""

import os
import re
import csv
import json
import hashlib
import sys
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import Optional

# ── Configuration ──────────────────────────────────────────────

ARCHIVE_ROOTS = [
    Path(p) for p in os.environ.get(
        "XZ_CORPUS_ARCHIVE_ROOTS",
        "/home/claude/xz_corpus_raw/archive1/Archive 13:"
        "/home/claude/xz_corpus_raw/archive2/Archive 13 copy:"
        "/home/claude/xz_corpus_raw/archive3/Archive 13 copy"
    ).split(":")
]
OUTPUT_DIR = Path(os.environ.get(
    "XZ_CORPUS_OUTPUT_DIR",
    "/home/claude/xz_corpus_build/output"
))

# ── Manual overrides from prose inspection (v0.3 triage) ──────
MANUAL_VERDICTS = {
    "R12_OPUS5_ADVISORY_v0_53.md": "HALT",
    "xz_glm52_audit_report.md": "HALT",
    "XZ_v15_FABLE_ADVISORY_REPORT.md": "HALT",
    "XZ_v16_FABLE_ADVISORY_REPORT.md": "HALT",
    "report_v19_adversarial_audit.md": "HALT",
    "XZ_v032_SEAT_H_REPORT.md": "HALT",
    "R6_F_OPUS5_META_REPORT (1).md": "HALT",
    "XZ_v0.50_R9_Seat_S02_OPUS_Audit.md": "HALT",
    "XZ_v064_R23_S04_REPORT (1).md": "HALT",
    "GLM52_Seat4_R2_Continuous_XZ_v0.37_Audit_Report (1).md": "CONDITIONAL PASS",
    "XZ_v17_OPUS5_ADVISORY_REPORT (1).md": "CONDITIONAL PASS",
    "XZ_v20_SEAT_A_CONTINUOUS_REPORT.md": "HALT",
    "XZ_v21_SEAT_A_DEEP_REPORT.md": "HALT",
    "XZ_v24_SEAT_A_DEEP_REPORT (1).md": "HALT",
    "XZ_v25_INSTANCE_A_REPORT.md": "HALT",
    "XZ_v27_INSTANCE_A_REPORT.md": "HALT",
    "XZ_v28_SEAT_G_ADVISORY.md": "HALT",
    "XZ_v28_INSTANCE_A_REPORT.md": "HALT",
    "XZ_PROTOCOL_AUDIT_FINDINGS_SUMMARY_GPT56.md": "HALT",
    "XZ_Protocol_v0.30_GPT56Sol_Audit_Report_2026-08-02.md": "HALT",
    "XZ_v031_ADVERSARIAL_GPT2_AUDIT.md": "HALT",
    "XZ_v32_SEAT_G_ADVISORY (1).md": "HALT",
    "XZ_v32_SEAT_A_FREEZE_AUDIT (1).md": "HALT",
    "XZ_Protocol_v0.33_Adversarial_Audit_GPT_2.md": "HALT",
    "XZ_v033_ADVERSARIAL_GPT1B_AUDIT.md": "HALT",
    "AUDIT_REPORT_v033_GLM_1C.md": "HALT",
    "XZ_v34_SEAT_G_ADVISORY.md": "HALT",
    "XZ_v34_SEAT_A_FREEZE_AUDIT.md": "HALT",
    "XZ_Protocol_v0.35_Adversarial_Audit_GPT_2.md": "HALT",
    "XZ_v035_ADVERSARIAL_GPT1B_AUDIT.md": "HALT",
    "XZ_v36_SEAT_G_ADVISORY.md": "HALT",
    "XZ_v36_SEAT_A_RING_CLOSURE_AUDIT.md": "HALT",
    "REPORT_GLM_1B_v033.md": "HALT",
    "XZ_v22_SEAT_A_DEEP_REPORT.md": "HALT",
    "R6_OPUS5_META_REPORT.md": "HALT",
    "XZ_v062_R21_S04_GEMINI_REPORT.md": "PASS",
    "R20_v061_S02_GPT56_SOL_FRESH_AUDIT.md": "HALT",
    "gemini-code-1786937940280.md": "HALT",
    "gemini-code-1786946878856.md": "HALT",
    "XZ_v068_R27_S02_REPORT.md": "HALT",
    "XZ_v27_SEAT_G_ADVISORY.md": "HALT",
    "XZ_v062_R21_S03_GPT_REPORT.md": "HALT",
    "XZ_v065_R24_S02_REPORT (1).md": "HALT",
    "SEAT_C01_OPUS5_LEO_v48_R7_REPORT.md": "HALT",
    "SEAT_SC04_GPT_CONTINUOUS_LEO_VERDICT_v0_48.md": "HALT",
    "CONV_R1_OPUS5_FRESH_v0.40_report.md": "HALT",
    "CONV_R2_OPUS5_CONTINUOUS_v0.41_report.md": "HALT",
    "SEAT_01_OPUS5_FRESH_v45_REPORT.md": "HALT",
    "SEAT_01_OPUS5_LEO_v46_REPORT.md": "HALT",
    "SEAT_SC04_GPT_CONTINUOUS_LEO_VERDICT_v0_47.md": "HALT",
    "XZ-Protocol-v0.37-R2-C2-GPT-5.6-Sol-Fractal-Continuous-Audit (1).md": "HALT",
    "R5_FRESH_OPUS5_COBWEB_REPORT (1).md": "HALT",
}

EXCLUDE_FILES = {
    "AUDIT_DISPATCH_DISCIPLINE.md",
    "AUDIT_DISPATCH_DISCIPLINE_v2.md",
    "XZ_PROTOCOL_AUDIT_COMMANDS_AND_EVIDENCE_GPT56.md",
    "ORBITAL_AUDIT_METHODOLOGY_v0_1.md",
    "QUANTUM_ORBITAL_AUDIT_METHODOLOGY_v0_1.md",
    "XZ_Protocol_v0.61_Audit_Results.md",
}

LOG = []
def log(msg):
    LOG.append(msg)
    print(msg, file=sys.stderr)


# ── Data structures ────────────────────────────────────────────

@dataclass
class ReportMeta:
    filepath: str = ""
    filename: str = ""
    sha256: str = ""
    # Extracted metadata
    round_number: Optional[int] = None
    round_label: str = ""           # e.g. "R31", "CONV R1"
    version: str = ""               # e.g. "v0.74", "v0.37"
    seat_id: str = ""               # e.g. "S04", "Seat 1", "C05"
    model_family: str = ""          # e.g. "Claude Opus 5", "GPT-5.6 Sol", "Kimi K3", "Gemini 3.1 Pro", "GLM-5.2"
    family_normalized: str = ""     # Anthropic, OpenAI, Moonshot, Google, Zhipu
    role: str = ""                  # carrying, advisory, adversarial
    mode: str = ""                  # fresh, continuous
    verdict: str = ""               # HALT, CONDITIONAL PASS, PASS
    severity_critical: int = 0
    severity_high: int = 0
    severity_medium: int = 0
    severity_low: int = 0
    class_a_count: int = 0
    finding_count: int = 0
    era: str = ""                   # pre-R7, seat-lineage, convergence, CI-era, mature


@dataclass
class Finding:
    report_file: str = ""
    finding_id: str = ""
    severity: str = ""              # CRITICAL, HIGH, MEDIUM, LOW, INFORMATIONAL
    finding_class: str = ""         # Class A, Class B, Class C, Class D, Class E
    tier: str = ""                  # Tier 1, Tier 2, Tier 3
    description: str = ""           # First-line description
    locus: str = ""                 # Where in the artifact
    round_number: Optional[int] = None
    version: str = ""
    seat_id: str = ""
    model_family: str = ""
    family_normalized: str = ""


# ── Family normalization ───────────────────────────────────────

FAMILY_MAP = {
    "claude": "Anthropic",
    "opus": "Anthropic",
    "anthropic": "Anthropic",
    "fable": "Anthropic",
    "gpt": "OpenAI",
    "sol": "OpenAI",
    "openai": "OpenAI",
    "kimi": "Moonshot",
    "moonshot": "Moonshot",
    "gemini": "Google",
    "google": "Google",
    "glm": "Zhipu",
    "zhipu": "Zhipu",
    "chatglm": "Zhipu",
    "deepseek": "DeepSeek",
    "qwen": "Alibaba",
    "perplexity": "Perplexity",
}

def normalize_family(raw: str) -> str:
    raw_lower = raw.lower()
    for key, val in FAMILY_MAP.items():
        if key in raw_lower:
            return val
    return raw


# ── Version / round extraction from filename ───────────────────

VERSION_PAT = re.compile(r'v0[._](\d+)', re.IGNORECASE)
ROUND_PAT = re.compile(r'R(\d+)', re.IGNORECASE)

def extract_version_from_name(name: str) -> str:
    m = VERSION_PAT.search(name)
    if m:
        return f"v0.{m.group(1)}"
    return ""

def extract_round_from_name(name: str) -> Optional[int]:
    m = ROUND_PAT.search(name)
    if m:
        return int(m.group(1))
    return None

def extract_seat_from_name(name: str) -> str:
    # S01-S12, Seat N, C01-C08, SC01-SC08
    patterns = [
        re.compile(r'(?:SEAT_?|_)(S\d+)', re.IGNORECASE),
        re.compile(r'(?:SEAT_?|_)(C\d+)', re.IGNORECASE),
        re.compile(r'(?:SEAT_?|_)(SC\d+)', re.IGNORECASE),
        re.compile(r'Seat[_ ](\d+)', re.IGNORECASE),
        re.compile(r'_([ABCDEF])_', re.IGNORECASE),  # early seat labels
    ]
    for pat in patterns:
        m = pat.search(name)
        if m:
            return m.group(1).upper()
    return ""

def extract_family_from_name(name: str) -> str:
    name_upper = name.upper()
    if "OPUS" in name_upper or "CLAUDE" in name_upper or "FABLE" in name_upper:
        return "Claude Opus 5"
    if "GPT" in name_upper or "SOL" in name_upper:
        return "GPT-5.6 Sol"
    if "KIMI" in name_upper or "K3" in name_upper:
        return "Kimi K3"
    if "GEMINI" in name_upper or "GEM" in name_upper:
        return "Gemini 3.1 Pro"
    if "GLM" in name_upper:
        return "GLM-5.2"
    return ""


# ── Report content parsing ─────────────────────────────────────

def parse_report_metadata(text: str, filename: str) -> ReportMeta:
    """Extract structured metadata from the report header."""
    meta = ReportMeta()
    meta.filename = filename

    # Version from text
    for pat in [
        re.compile(r'(?:Version under audit|Target|Artifact)[:\s]*(?:XZ Protocol\s+)?v0\.(\d+)', re.IGNORECASE),
        re.compile(r'XZ Protocol v0\.(\d+)', re.IGNORECASE),
        re.compile(r'v0\.(\d+)\s+(?:DRAFT|FROZEN|bytes)', re.IGNORECASE),
    ]:
        m = pat.search(text[:3000])
        if m:
            meta.version = f"v0.{m.group(1)}"
            break
    if not meta.version:
        meta.version = extract_version_from_name(filename)

    # Round from text
    for pat in [
        re.compile(r'\*\*Round:\*\*\s*(\d+)', re.IGNORECASE),
        re.compile(r'Round\s+(\d+)', re.IGNORECASE),
        re.compile(r'\bR(\d+)\b'),
    ]:
        m = pat.search(text[:3000])
        if m:
            meta.round_number = int(m.group(1))
            meta.round_label = f"R{meta.round_number}"
            break
    if meta.round_number is None:
        meta.round_number = extract_round_from_name(filename)
        if meta.round_number:
            meta.round_label = f"R{meta.round_number}"

    # Seat
    for pat in [
        re.compile(r'\*\*Seat(?:\s*ID)?:\*\*\s*(\S+)', re.IGNORECASE),
        re.compile(r'\*\*Seat:\*\*\s*(\S+)', re.IGNORECASE),
        re.compile(r'Seat[:\s]+([A-Z]\d+)', re.IGNORECASE),
    ]:
        m = pat.search(text[:3000])
        if m:
            meta.seat_id = m.group(1).strip(" |*,")
            break
    if not meta.seat_id:
        meta.seat_id = extract_seat_from_name(filename)

    # Model family from text
    for pat in [
        re.compile(r'\*\*(?:Model|Family):\*\*\s*(.+?)(?:\s*[-–—|]|\s*\*\*)', re.IGNORECASE),
        re.compile(r'Model:\s*(.+?)(?:\n|\||--)', re.IGNORECASE),
    ]:
        m = pat.search(text[:3000])
        if m:
            meta.model_family = m.group(1).strip()
            break
    if not meta.model_family:
        meta.model_family = extract_family_from_name(filename)
    # Normalize: try the extracted family first, then the filename
    meta.family_normalized = normalize_family(meta.model_family) if meta.model_family else ""
    if not meta.family_normalized or meta.family_normalized == meta.model_family:
        fn_family = normalize_family(filename)
        if fn_family != filename:
            meta.family_normalized = fn_family
        else:
            # Last resort: scan the text header for family keywords
            header = text[:3000].lower()
            for kw, fam in FAMILY_MAP.items():
                if kw in header:
                    meta.family_normalized = fam
                    break
            else:
                meta.family_normalized = "UNKNOWN"

    # Role
    text_upper = text[:3000].upper()
    if "CARRYING" in text_upper or "CARRY" in text_upper and "NON-CARRYING" not in text_upper:
        if "NON-CARRYING" in text_upper or "ADVISORY" in text_upper:
            meta.role = "advisory"
        else:
            meta.role = "carrying"
    elif "ADVERSARIAL" in text_upper:
        meta.role = "adversarial"
    else:
        meta.role = "advisory"

    # Mode (fresh vs continuous)
    if re.search(r'\bFRESH\b', text[:3000], re.IGNORECASE):
        meta.mode = "fresh"
    if re.search(r'\bCONTINUOUS\b', text[:3000], re.IGNORECASE):
        meta.mode = "continuous"
    if not meta.mode:
        meta.mode = "unknown"

    # Verdict — look for the verdict declaration, normalize to HALT/CONDITIONAL PASS/PASS
    verdict_pats = [
        re.compile(r'>\s*\*\*Verdict:\*\*\s*\*?\*?([^*\n<]+)', re.IGNORECASE),
        re.compile(r'\*\*Verdict[:\s]*\*\*\s*\*?\*?(HALT[^*\n]*|CONDITIONAL PASS[^*\n]*|PASS[^*\n]*)', re.IGNORECASE),
        re.compile(r'^#+\s*(HALT\b[^*\n]*)', re.MULTILINE | re.IGNORECASE),
        re.compile(r'## (?:Executive )?Verdict\s*\n+\*?\*?(HALT[^*\n]*|PASS[^*\n]*)', re.IGNORECASE),
        re.compile(r'VERDICT[:\s]+(HALT|CONDITIONAL PASS|PASS)', re.IGNORECASE),
        re.compile(r'Verdict[:\s]+(HALT|CONDITIONAL PASS|PASS)', re.IGNORECASE),
        re.compile(r'\*\*VERDICT:\s*(HALT[^*]*)\*\*', re.IGNORECASE),
        re.compile(r'(?:returns?|recommends?)\s+(?:`?)?(HALT|CONDITIONAL PASS|PASS)\b', re.IGNORECASE),
    ]
    for pat in verdict_pats:
        m = pat.search(text[:8000])
        if m:
            v = m.group(1).strip().strip("*").strip()
            if "HALT" in v.upper():
                meta.verdict = "HALT"
            elif "CONDITIONAL" in v.upper():
                meta.verdict = "CONDITIONAL PASS"
            elif "PASS" in v.upper():
                meta.verdict = "PASS"
            else:
                meta.verdict = v[:40]
            break
    # Fallback: scan for standalone HALT/PASS in first lines
    if not meta.verdict:
        for line in text[:3000].split("\n")[:30]:
            line_clean = line.strip().strip("*#> ").strip()
            if line_clean.upper() in ("HALT", "HALT.", "**HALT**"):
                meta.verdict = "HALT"
                break
            if "CONDITIONAL PASS" in line_clean.upper():
                meta.verdict = "CONDITIONAL PASS"
                break
            if line_clean.upper() in ("PASS", "PASS."):
                meta.verdict = "PASS"
                break

    # Severity ledger
    sev_pat = re.compile(
        r'(\d+)\s*(?:CRITICAL|Crit).*?(\d+)\s*(?:HIGH|Hi).*?(\d+)\s*(?:MEDIUM|Med).*?(\d+)\s*(?:LOW|Lo)',
        re.IGNORECASE
    )
    m = sev_pat.search(text[:5000])
    if m:
        meta.severity_critical = int(m.group(1))
        meta.severity_high = int(m.group(2))
        meta.severity_medium = int(m.group(3))
        meta.severity_low = int(m.group(4))

    # Class A count
    class_a_pat = re.compile(r'(\d+)\s*Class\s*A\b', re.IGNORECASE)
    m = class_a_pat.search(text[:5000])
    if m:
        meta.class_a_count = int(m.group(1))

    # Apply manual verdict overrides (from v0.3 prose triage)
    if not meta.verdict and filename in MANUAL_VERDICTS:
        meta.verdict = MANUAL_VERDICTS[filename]

    # Era classification
    if meta.round_number is not None:
        if meta.round_number < 7:
            # Check if it's a seat-lineage round (R1-R6)
            meta.era = "seat-lineage" if meta.round_number >= 1 else "pre-R7"
        elif meta.round_number <= 8:
            meta.era = "convergence"
        elif meta.round_number <= 14:
            meta.era = "mid-program"
        elif meta.round_number <= 20:
            meta.era = "CI-era"
        else:
            meta.era = "mature"
    else:
        # Try version-based classification
        ver = meta.version
        if ver:
            ver_num = int(ver.split(".")[-1]) if "." in ver else 0
            if ver_num <= 36:
                meta.era = "pre-R7"
            elif ver_num <= 39:
                meta.era = "seat-lineage"
            elif ver_num <= 48:
                meta.era = "convergence"
            elif ver_num <= 55:
                meta.era = "mid-program"
            elif ver_num <= 61:
                meta.era = "CI-era"
            else:
                meta.era = "mature"

    return meta


# ── Finding extraction ─────────────────────────────────────────

# Pattern variants for finding headers:
FINDING_PATTERNS = [
    # 1. Mature: ### F-S04-74-01 [CRITICAL] [Class A] -- description
    re.compile(
        r'^###\s+(F-[\w-]+)\s+\[(\w+)\]\s+\[Class\s+(\w)\]'
        r'\s*[-\u2013\u2014]+\s*(.*)',
        re.MULTILINE
    ),
    # 2. Mid-era variant: ### F-S03-54-01 [Class A] HIGH -- description
    re.compile(
        r'^###\s+(F-[\w-]+)\s+\[Class\s+(\w)\]\s+(\w+)'
        r'\s*[-\u2013\u2014]+\s*(.*)',
        re.MULTILINE
    ),
    # 3. Cross-domain: ### F-GPT37FH-R2-01 [CRITICAL] [Tier 1] -- description
    re.compile(
        r'^###\s+(F-[\w-]+)\s+\[(\w+)\]\s+\[Tier\s+(\d)\]'
        r'(?:\s*[-\u2013\u2014]+\s*(.*))?',
        re.MULTILINE
    ),
    # 4. Kimi bracket-severity bare-class: ### F-S03-68-01 [HIGH] -- Class A -- description
    re.compile(
        r'^###\s+(F-[\w-]+)\s+\[(\w+)\]\s*[-\u2013\u2014]+\s*Class\s+(\w)\s*[-\u2013\u2014]+\s*(.*)',
        re.MULTILINE
    ),
    # 5. Severity-first without class: ### F-OP17-01 [HIGH] -- description
    re.compile(
        r'^###\s+(F-[\w-]+)\s+\[(\w+)\]'
        r'\s*[-\u2013\u2014]+\s*(.*)',
        re.MULTILINE
    ),
    # 6. GPT em-dash slash-class: ### F-S02-59-01 — HIGH / Class A
    re.compile(
        r'^###\s+(F-[\w-]+)\s*[\u2013\u2014]+\s*(\w+)\s*/\s*Class\s+(\w)(?:\s*$)?',
        re.MULTILINE
    ),
    # 7. GPT em-dash paren-class: ### F-S03-62-01 — HIGH (Class A): description
    re.compile(
        r'^###\s+(F-[\w-]+)\s*[\u2013\u2014]+\s*(\w+)\s*\(Class\s+(\w)\)[:\s]*(.*)',
        re.MULTILINE
    ),
    # 8. Em-dash severity only: ### F-CONV1-01 — CRITICAL
    re.compile(
        r'^###\s+(F-[\w-]+)\s*[\u2013\u2014]+\s*(CRITICAL|HIGH|MEDIUM|LOW|INFO(?:RMATIONAL)?)\b\s*(.*)',
        re.MULTILINE | re.IGNORECASE
    ),
    # 9. Em-dash severity-em-dash-description: ### F-FABLE5-05 — CRITICAL — description
    # (subsumed by pattern 8 since .* captures the rest)

    # 10. GLM inline: ### N.N F-GLM52-01 — description — **SEVERITY**
    re.compile(
        r'^###\s+\d+\.?\d*\s+(F-[\w-]+)\s*[\u2013\u2014]+\s*(.*?)\s*[\u2013\u2014]+\s*\*\*(\w+)\*\*',
        re.MULTILINE
    ),
    # 11. Convergence: ### F-V43-01 -- SEVERITY (double-hyphen)
    re.compile(
        r'^###\s+(F-[\w-]+)\s*--\s*(CRITICAL|HIGH|MEDIUM|LOW|INFO(?:RMATIONAL)?)\b\s*(.*)',
        re.MULTILINE | re.IGNORECASE
    ),
    # 12. Numbered early (no F-ID): ### N. Severity - description
    re.compile(
        r'^###\s+(\d+)\.\s+(Critical|High|Medium|Low)\s*[-:\u2013\u2014]+\s*(.*)',
        re.MULTILINE | re.IGNORECASE
    ),
    # 13. Bold finding (no ###): **F-OP20F-01** [HIGH] -- description  OR  **F-OP20F-01** HIGH -- description
    re.compile(
        r'^\*\*(F-[\w-]+)\*\*\s+\[?(\w+)\]?\s*[-\u2013\u2014]+\s*(.*)',
        re.MULTILINE
    ),
    # 13. R8 numbered-bold: N. **F-S02-49-01 — Class A:** description
    re.compile(
        r'^\d+\.\s+\*\*(F-[\w-]+)\s*[\u2013\u2014]+\s*Class\s+(\w):\*\*\s*(.*)',
        re.MULTILINE
    ),
    # 14. R16 pipe-bold: **F-S03-57-01 | SEVERITY (Class X) | description**
    re.compile(
        r'^\*\*(F-[\w-]+)\s*\|\s*(\w+)\s*\(Class\s+(\w)\)\s*\|\s*(.*?)\*\*',
        re.MULTILINE
    ),
    # 15. R17 pipe-hash: ### F-S03-58-01 | SEVERITY (Class X) | description
    re.compile(
        r'^###\s+(F-[\w-]+)\s*\|\s*(\w+)\s*\(Class\s+(\w)\)\s*\|\s*(.*)',
        re.MULTILINE
    ),
    # 15. R12 class-after-dash: ### F-S01-53-01 -- CLASS A (description)
    re.compile(
        r'^###\s+(F-[\w-]+)\s*--\s*CLASS\s+([A-E])\s*\(?(.*?)\)?\s*$',
        re.MULTILINE | re.IGNORECASE
    ),
    # 16. Bare F-ID header: ### F-S05-59-01 (severity/class on next lines)
    re.compile(
        r'^###\s+(F-[\w-]+)\s*$',
        re.MULTILINE
    ),
    # 16. GPT no-severity bare-description: ### F-GPT33-01 — description
    re.compile(
        r'^###\s+(F-[\w-]+)\s*[\u2013\u2014]+\s*(?!CRITICAL|HIGH|MEDIUM|LOW|INFO|Class)(.*)',
        re.MULTILINE | re.IGNORECASE
    ),
]


def extract_findings(text: str, meta: ReportMeta) -> list:
    """Extract all findings from a report."""
    findings = []
    seen_ids = set()

    for pat_idx, pat in enumerate(FINDING_PATTERNS):
        for m in pat.finditer(text):
            f = Finding()
            f.report_file = meta.filename
            f.round_number = meta.round_number
            f.version = meta.version
            f.seat_id = meta.seat_id
            f.model_family = meta.model_family
            f.family_normalized = meta.family_normalized

            if pat_idx == 0:
                # Mature: ID, severity, class, description
                f.finding_id = m.group(1)
                f.severity = m.group(2).upper()
                f.finding_class = f"Class {m.group(3).upper()}"
                f.description = m.group(4).strip()
            elif pat_idx == 1:
                # Mid-era: ID, class, severity, description
                f.finding_id = m.group(1)
                f.finding_class = f"Class {m.group(2).upper()}"
                f.severity = m.group(3).upper()
                f.description = m.group(4).strip()
            elif pat_idx == 2:
                # Cross-domain: ID, severity, tier
                f.finding_id = m.group(1)
                f.severity = m.group(2).upper()
                f.tier = f"Tier {m.group(3)}"
                f.description = (m.group(4) or "").strip()
            elif pat_idx == 3:
                # Kimi bracket-severity bare-class: ID, severity, class, description
                f.finding_id = m.group(1)
                f.severity = m.group(2).upper()
                f.finding_class = f"Class {m.group(3).upper()}"
                f.description = m.group(4).strip()
            elif pat_idx == 4:
                # Severity-first: ID, severity, description
                f.finding_id = m.group(1)
                f.severity = m.group(2).upper()
                f.description = m.group(3).strip()
            elif pat_idx == 5:
                # GPT slash-class: ID, severity, class
                f.finding_id = m.group(1)
                f.severity = m.group(2).upper()
                f.finding_class = f"Class {m.group(3).upper()}"
            elif pat_idx == 6:
                # GPT paren-class: ID, severity, class, description
                f.finding_id = m.group(1)
                f.severity = m.group(2).upper()
                f.finding_class = f"Class {m.group(3).upper()}"
                f.description = m.group(4).strip()
            elif pat_idx == 7:
                # Em-dash severity: ID, severity, description
                f.finding_id = m.group(1)
                sev = m.group(2).upper()
                f.severity = "INFORMATIONAL" if sev.startswith("INFO") else sev
                f.description = m.group(3).strip().lstrip('\u2013\u2014- ').strip()
            elif pat_idx == 8:
                # GLM inline: ID, description, severity
                f.finding_id = m.group(1)
                f.description = m.group(2).strip()
                f.severity = m.group(3).upper()
            elif pat_idx == 9:
                # Convergence double-hyphen: ID, severity, description
                f.finding_id = m.group(1)
                sev = m.group(2).upper()
                f.severity = "INFORMATIONAL" if sev.startswith("INFO") else sev
                f.description = m.group(3).strip()
            elif pat_idx == 10:
                # Numbered early: generate synthetic ID
                num = m.group(1)
                # Namespace per source report to prevent cross-report collisions
                report_slug = meta.filename.replace('.md','').replace(' ','_')[:20]
                f.finding_id = f"F-EARLY-{report_slug}-{num.zfill(2)}"
                f.severity = m.group(2).upper()
                f.description = m.group(3).strip()
            elif pat_idx == 11:
                # Bold finding: **F-OP20F-01** [HIGH -- qualifier] -- description
                f.finding_id = m.group(1)
                sev = m.group(2).upper()
                if sev in ("CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "INFO"):
                    f.severity = "INFORMATIONAL" if sev == "INFO" else sev
                else:
                    f.severity = ""
                f.description = m.group(3).strip()
            elif pat_idx == 12:
                # R8 numbered-bold: N. **F-ID — Class X:** description
                f.finding_id = m.group(1)
                f.finding_class = f"Class {m.group(2).upper()}"
                f.description = m.group(3).strip()
                # Infer severity from class
                if f.finding_class == "Class A":
                    f.severity = "HIGH"
                elif f.finding_class == "Class B":
                    f.severity = "MEDIUM"
            elif pat_idx == 13:
                # R16 pipe-bold: **F-ID | SEVERITY (Class X) | description**
                f.finding_id = m.group(1)
                f.severity = m.group(2).upper()
                f.finding_class = f"Class {m.group(3).upper()}"
                f.description = m.group(4).strip()
            elif pat_idx == 14:
                # R17 pipe-hash: ### F-ID | SEVERITY (Class X) | Locus: ... | description
                f.finding_id = m.group(1)
                f.severity = m.group(2).upper()
                f.finding_class = f"Class {m.group(3).upper()}"
                desc = m.group(4).strip()
                # Extract inline locus if present: "Locus: X | description"
                if "|" in desc:
                    parts = desc.split("|", 1)
                    if parts[0].strip().startswith("Locus:"):
                        f.locus = parts[0].strip()[6:].strip()
                        f.description = parts[1].strip() if len(parts) > 1 else ""
                    else:
                        f.description = desc
                else:
                    f.description = desc
            elif pat_idx == 15:
                # R12 class-after-dash: ### F-ID -- CLASS X (description)
                f.finding_id = m.group(1)
                f.finding_class = f"Class {m.group(2).upper()}"
                f.description = m.group(3).strip()
                # Infer severity from class
                if f.finding_class == "Class A":
                    f.severity = "HIGH"
                elif f.finding_class == "Class B":
                    f.severity = "MEDIUM"
                else:
                    f.severity = "LOW"
                # Try to get exact severity from **Severity:** line
                pos = m.end()
                body_chunk = text[pos:pos+500]
                sev_line = re.search(r'\*\*Severity:\*\*\s*(\w+)', body_chunk, re.IGNORECASE)
                if sev_line:
                    f.severity = sev_line.group(1).upper()
            elif pat_idx == 16:
                # Bare F-ID header: ### F-ID (severity/class on next lines)
                f.finding_id = m.group(1)
                pos = m.end()
                body_chunk = text[pos:pos+500]
                # Extract severity from **Severity:** line
                sev_line = re.search(r'\*\*Severity:\*\*\s*(\w+)', body_chunk, re.IGNORECASE)
                if sev_line:
                    f.severity = sev_line.group(1).upper()
                else:
                    for sev_word in ["CRITICAL", "HIGH", "MEDIUM", "LOW"]:
                        if sev_word in body_chunk.upper()[:200]:
                            f.severity = sev_word
                            break
                # Extract class from body
                cls_match = re.search(r'\bClass\s+([A-E])\b', body_chunk[:300])
                if cls_match:
                    f.finding_class = f"Class {cls_match.group(1).upper()}"
                # Extract description from **Substance:** or first non-empty line
                sub_match = re.search(r'\*\*Substance:\*\*\s*(.+?)(?:\n|$)', body_chunk)
                if sub_match:
                    f.description = sub_match.group(1).strip()[:200]
                else:
                    for line in body_chunk.split('\n')[1:5]:
                        stripped = line.strip().strip('*').strip()
                        if stripped and not stripped.startswith('**') and len(stripped) > 10:
                            f.description = stripped[:200]
                            break
            elif pat_idx == 17:
                # Bare description catch-all (no severity) -- 2 groups only
                f.finding_id = m.group(1)
                f.description = m.group(2).strip()
                pos = m.end()
                body_chunk = text[pos:pos+500]
                for sev_word in ["CRITICAL", "HIGH", "MEDIUM", "LOW"]:
                    if sev_word in body_chunk.upper()[:200]:
                        f.severity = sev_word
                        break

            # Compute per-finding body boundary (stop at next finding header)
            pos = m.end()
            next_header = re.search(r'^###\s+F-|\n\*\*F-', text[pos:], re.MULTILINE)
            body_end = pos + next_header.start() if next_header else pos + 1500
            body_end = min(body_end, pos + 1500)  # hard cap
            body_chunk = text[pos:body_end]

            # Extract locus from finding body (bounded)
            for locus_pat in [
                re.compile(r'\*\*Locus:\*\*\s*(.+?)(?:\n|$)', re.IGNORECASE),
                re.compile(r'[-\*]\s*\*\*Locus:\*\*\s*(.+?)(?:\n|$)', re.IGNORECASE),
                re.compile(r'Locus:\s*`([^`]+)`', re.IGNORECASE),
            ]:
                lm = locus_pat.search(body_chunk)
                if lm:
                    f.locus = lm.group(1).strip().strip("`*")[:200]
                    break

            # Extract class from body if not in header (only single letters A-E)
            if not f.finding_class:
                class_pat = re.compile(r'\bClass\s+([A-E])\b')
                cm = class_pat.search(body_chunk[:300])
                if cm:
                    f.finding_class = f"Class {cm.group(1).upper()}"

            # Description-field validation: strip leaked locus markers and backfill
            desc_stripped = f.description.lstrip('- *')
            if desc_stripped.startswith("Locus:") or f.description.startswith("**Locus:"):
                # Locus marker leaked into description -- extract locus, backfill desc
                locus_content = re.sub(r'^\**\s*-?\s*\**Locus:\**\s*', '', f.description).strip()
                if locus_content:
                    # Current finding's locus takes priority over any body-scanned locus
                    f.locus = locus_content[:200]
                # Backfill description from bounded body
                body_lines = body_chunk.split('\n')
                f.description = ""
                for bl in body_lines[1:8]:
                    bl_clean = bl.strip().lstrip('- *')
                    if (bl_clean and not bl_clean.startswith("Locus:")
                        and not bl_clean.startswith("**Locus:")
                        and not bl_clean.startswith("Severity:")
                        and not bl_clean.startswith("**Severity:")
                        and len(bl_clean) > 10):
                        if bl_clean.startswith("Substance:") or bl_clean.startswith("**Substance:"):
                            f.description = re.sub(r'^\**Substance:\**\s*', '', bl_clean)[:200]
                        elif not f.description:
                            f.description = bl_clean[:200]
                        break
            # Clean severity-metadata leaked into description
            if re.match(r'^Severity:\*?\*?\s*(CRITICAL|HIGH|MEDIUM|LOW)', f.description, re.IGNORECASE):
                f.description = ""
            if f.description.startswith("[") and "HALT" in f.description[:30]:
                f.description = ""

            # Deduplicate
            if f.finding_id and f.finding_id not in seen_ids:
                seen_ids.add(f.finding_id)
                findings.append(f)

    return findings


# ── File discovery ─────────────────────────────────────────────

def is_seat_report(filepath: Path) -> bool:
    """Heuristic: is this .md file a seat report vs a dispatch/methodology doc?"""
    name = filepath.name.upper()
    # Positive signals
    if any(kw in name for kw in ["REPORT", "AUDIT", "VERDICT", "RESULT", "ADVISORY"]):
        return True
    # Negative signals (dispatches, methodology, prompts, non-report docs)
    if any(kw in name for kw in ["DISPATCH_PROMPT", "METHODOLOGY", "DISCIPLINE",
                                  "HANDOFF", "CONCEPT", "ADJUDICATION_V", "TRIAGE",
                                  "CRYSTALLOGRAPHIC", "ORBITAL_AUDIT_METH",
                                  "QUANTUM_ORBITAL", "PEER_REVIEW_PROMPT",
                                  "PUBLICATION_REVIEW"]):
        return False
    # Check content for verdict
    try:
        with open(filepath, 'r', errors='replace') as f:
            head = f.read(3000)
        if re.search(r'Verdict.*(?:HALT|PASS|CONDITIONAL)', head, re.IGNORECASE):
            return True
    except:
        pass
    return False


def discover_reports() -> list:
    """Walk all archive roots and find seat report .md files."""
    reports = []
    seen_hashes = set()

    for root in ARCHIVE_ROOTS:
        if not root.exists():
            log(f"WARN: archive root not found: {root}")
            continue
        for md_file in sorted(root.rglob("*.md")):
            if "__MACOSX" in str(md_file) or ".DS_Store" in str(md_file):
                continue
            if not is_seat_report(md_file):
                continue
            if md_file.name in EXCLUDE_FILES:
                log(f"EXCLUDE: {md_file.name} (manual triage)")
                continue

            # Deduplicate by content hash (handles (1) copies)
            try:
                content = md_file.read_bytes()
                h = hashlib.sha256(content).hexdigest()
                if h in seen_hashes:
                    log(f"DEDUP: {md_file.name} (duplicate content)")
                    continue
                seen_hashes.add(h)
                reports.append(md_file)
            except Exception as e:
                log(f"ERROR reading {md_file}: {e}")

    return reports


# ── Main pipeline ──────────────────────────────────────────────

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    log("=" * 60)
    log("XZ Protocol Audit Corpus Extractor v0.6")
    log("=" * 60)

    # Phase 1: Discover reports
    log("\n--- Phase 1: Report discovery ---")
    report_files = discover_reports()
    log(f"Found {len(report_files)} unique seat reports")

    all_reports = []
    all_findings = []

    # Phase 2: Extract metadata and findings
    log("\n--- Phase 2: Extraction ---")
    for rf in report_files:
        try:
            text = rf.read_text(errors='replace')
            meta = parse_report_metadata(text, rf.name)
            meta.filepath = str(rf)
            meta.sha256 = hashlib.sha256(rf.read_bytes()).hexdigest()

            findings = extract_findings(text, meta)
            meta.finding_count = len(findings)

            all_reports.append(meta)
            all_findings.extend(findings)

            if findings:
                log(f"  {rf.name}: {meta.round_label or '?'} {meta.version} "
                    f"{meta.seat_id} ({meta.family_normalized}) "
                    f"-> {meta.verdict}, {len(findings)} findings")
            else:
                log(f"  {rf.name}: {meta.round_label or '?'} {meta.version} "
                    f"{meta.seat_id} ({meta.family_normalized}) "
                    f"-> {meta.verdict}, 0 findings (may need format adaptation)")
        except Exception as e:
            log(f"ERROR processing {rf.name}: {e}")

    # Phase 3: Write outputs
    log(f"\n--- Phase 3: Output ---")
    log(f"Total reports: {len(all_reports)}")
    log(f"Total findings extracted: {len(all_findings)}")

    # Reports CSV
    report_fields = [
        "filename", "sha256", "round_number", "round_label", "version",
        "seat_id", "model_family", "family_normalized", "role", "mode",
        "verdict", "severity_critical", "severity_high", "severity_medium",
        "severity_low", "class_a_count", "finding_count", "era"
    ]
    with open(OUTPUT_DIR / "reports.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=report_fields)
        w.writeheader()
        for r in sorted(all_reports, key=lambda x: (x.round_number or 0, x.version, x.seat_id)):
            w.writerow({k: getattr(r, k) for k in report_fields})

    # Findings CSV
    finding_fields = [
        "finding_id", "severity", "finding_class", "tier", "description",
        "locus", "round_number", "version", "seat_id", "model_family",
        "family_normalized", "report_file"
    ]
    with open(OUTPUT_DIR / "findings.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=finding_fields)
        w.writeheader()
        for fd in sorted(all_findings, key=lambda x: (x.round_number or 0, x.finding_id)):
            w.writerow({k: getattr(fd, k) for k in finding_fields})

    # Coverage matrix -- keyed on filename to prevent silent collision
    with open(OUTPUT_DIR / "coverage.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["round", "version", "seat", "family", "verdict", "report_file"])
        for r in sorted(all_reports, key=lambda x: (x.round_number or 0, x.version, x.seat_id)):
            w.writerow([r.round_number or 0, r.version, r.seat_id,
                        r.family_normalized, r.verdict, r.filename])

    # Summary statistics
    summary = {
        "extractor_version": "v0.6",
        "total_reports": len(all_reports),
        "total_findings": len(all_findings),
        "unique_finding_ids": len(set(f.finding_id for f in all_findings)),
        "reports_by_era": {},
        "reports_by_family": {},
        "findings_by_severity": {},
        "findings_by_class": {},
        "verdicts": {},
        "rounds_covered": sorted(set(r.round_number for r in all_reports if r.round_number)),
        "versions_covered": sorted(set(r.version for r in all_reports if r.version)),
    }
    for r in all_reports:
        summary["reports_by_era"][r.era] = summary["reports_by_era"].get(r.era, 0) + 1
        summary["reports_by_family"][r.family_normalized] = summary["reports_by_family"].get(r.family_normalized, 0) + 1
        summary["verdicts"][r.verdict] = summary["verdicts"].get(r.verdict, 0) + 1
    for fd in all_findings:
        summary["findings_by_severity"][fd.severity] = summary["findings_by_severity"].get(fd.severity, 0) + 1
        if fd.finding_class:
            summary["findings_by_class"][fd.finding_class] = summary["findings_by_class"].get(fd.finding_class, 0) + 1

    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump(summary, f, indent=2, default=str)

    # Write log
    with open(OUTPUT_DIR / "extraction.log", "w") as f:
        f.write("\n".join(LOG))

    # Print summary
    log(f"\n{'='*60}")
    log(f"EXTRACTION COMPLETE")
    log(f"{'='*60}")
    log(f"Reports:  {len(all_reports)}")
    log(f"Findings: {len(all_findings)}")
    log(f"Unique finding IDs: {summary['unique_finding_ids']}")
    log(f"\nBy era: {json.dumps(summary['reports_by_era'], indent=2)}")
    log(f"\nBy family: {json.dumps(summary['reports_by_family'], indent=2)}")
    log(f"\nBy severity: {json.dumps(summary['findings_by_severity'], indent=2)}")
    log(f"\nBy class: {json.dumps(summary['findings_by_class'], indent=2)}")
    log(f"\nVerdicts: {json.dumps(summary['verdicts'], indent=2)}")
    log(f"\nRounds covered: {summary['rounds_covered']}")
    log(f"\nOutputs in: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()

---

# Bismillah ir-Rahman ir-Rahim
