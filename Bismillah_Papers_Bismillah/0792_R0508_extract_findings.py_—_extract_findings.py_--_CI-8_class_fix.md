# Bismillah ir-Rahman ir-Rahim

# R0508 -- extract_findings.py — extract_findings.py -- CI-8 class fix: automated findings extraction from seat reports.

**Chronological Index:** 792 of 995  
**Date:** Undated  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** extract_findings.py  
**Source Format:** py  
**SHA-256:** `212facc56eeea7e1bdcd87b93d7ef9e66c95bb5a360dce6a0e745cb68085fce8`  

---

## R0508 · extract_findings.py — extract_findings.py -- CI-8 class fix: automated findings extraction from seat reports.

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: extract_findings.py
- source_format: py
- text_sha256: 212facc56eeea7e1bdcd87b93d7ef9e66c95bb5a360dce6a0e745cb68085fce8

"""extract_findings.py -- CI-8 class fix: automated findings extraction from seat reports.

Reads markdown seat reports and produces a findings index JSON with correct
finding IDs and source severities extracted directly from the report bytes.
Eliminates manual transcription, which caused CI-8 recurrence at R22-R25.

Usage:
    python3 extract_findings.py report1.md report2.md ... > findings.json

The extractor looks for finding declarations in these formats:
    ### F-SNN-VV-NN -- SEVERITY -- ...
    ### F-SNN-VV-NN — SEVERITY — ...
    **F-SNN-VV-NN** ... SEVERITY ...
    | F-SNN-VV-NN | SEVERITY | ...
    F-SNN-VV-NN (SEVERITY) ...

The FIRST occurrence of a finding ID with a severity determines its
source_severity. Subsequent mentions are ignored (they may be references,
not declarations).
"""

import re
import json
import sys

FINDING_ID_RE = re.compile(r'F-S\d{2}C?-\d{2,3}-\d{2,3}[A-Z]?')
SEVERITY_RE = re.compile(r'\b(HIGH|MEDIUM|LOW|INFORMATIONAL|CRITICAL)\b')
SEAT_RE = re.compile(r'F-(S\d{2}C?)-')

# Declaration patterns (finding ID + severity in the same line, declaration context)
DECLARATION_PATTERNS = [
    # ### F-SNN-VV-NN -- SEVERITY -- ...
    re.compile(r'###?\s+(F-S\d{2}C?-\d{2,3}-\d{2,3}[A-Z]?)\s*[-—]+\s*(HIGH|MEDIUM|LOW|INFORMATIONAL|CRITICAL)\b'),
    # **F-SNN-VV-NN** ... SEVERITY
    re.compile(r'\*\*(F-S\d{2}C?-\d{2,3}-\d{2,3}[A-Z]?)\*\*[^|\n]*?\b(HIGH|MEDIUM|LOW|INFORMATIONAL|CRITICAL)\b'),
    # | F-SNN-VV-NN | SEVERITY | (table row)
    re.compile(r'\|\s*(F-S\d{2}C?-\d{2,3}-\d{2,3}[A-Z]?)\s*\|[^|]*\b(HIGH|MEDIUM|LOW|INFORMATIONAL|CRITICAL)\b'),
    # F-SNN-VV-NN (SEVERITY)
    re.compile(r'(F-S\d{2}C?-\d{2,3}-\d{2,3}[A-Z]?)\s*\(?(HIGH|MEDIUM|LOW|INFORMATIONAL|CRITICAL)\b'),
    # F-SNN-VV-NN [SEVERITY] (square bracket format, e.g. Gemini reports)
    re.compile(r'(F-S\d{2}C?-\d{2,3}-\d{2,3}[A-Z]?)\s*\[(HIGH|MEDIUM|LOW|INFORMATIONAL|CRITICAL)\]'),
]


def extract_from_report(text, filename="", version_filter=None):
    """Extract finding declarations from a single report's text.

    Returns dict: {finding_id: {"seat": str, "source_severity": str, "file": str}}

    Declaration-context extraction: only lines matching a DECLARATION_PATTERN
    are considered (heading declarations, bold declarations, table rows).
    This excludes finding IDs that appear in probe tables, inline references,
    or quoted examples.

    If version_filter is set (e.g. "68"), only finding IDs matching that
    version number are captured. This prevents prior-round references
    (e.g. F-S01-67-xx mentioned in an R27 report) from being counted.
    """
    findings = {}

    # Two-pass extraction: heading declarations first (authoritative),
    # then other patterns for findings not yet seen. This ensures
    # ### F-SNN-VV-NN -- SEVERITY -- wins over inline mentions.
    heading_pat = DECLARATION_PATTERNS[0]  # ### heading pattern
    other_pats = DECLARATION_PATTERNS[1:]

    for pass_patterns in ([heading_pat], other_pats):
        for line in text.split('\n'):
            for pattern in pass_patterns:
                for match in pattern.finditer(line):
                    fid = match.group(1)
                    sev = match.group(2)
                    # Version filter: skip findings from other rounds
                    if version_filter:
                        ver_match = re.search(r'F-S\d{2}C?-(\d{2,3})-', fid)
                        if ver_match and ver_match.group(1) != version_filter:
                            continue
                    # Seat range filter: skip seats outside S01-S06
                    seat_match = SEAT_RE.match(fid)
                    seat = seat_match.group(1) if seat_match else ""
                    seat_num = int(re.search(r'\d+', seat).group()) if seat else 0
                    if seat_num < 1 or seat_num > 6:
                        continue
                    if fid not in findings:
                        findings[fid] = {
                            "seat": seat,
                            "source_severity": sev,
                            "file": filename,
                        }

    return findings


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    version_filter = None
    for a in sys.argv[1:]:
        if a.startswith("--version="):
            version_filter = a.split("=", 1)[1]

    if not args:
        print("Usage: python3 extract_findings.py [--version=NN] report1.md [report2.md ...]", file=sys.stderr)
        sys.exit(1)

    all_findings = {}
    for path in args:
        text = open(path).read()
        extracted = extract_from_report(text, path, version_filter=version_filter)
        for fid, info in extracted.items():
            if fid not in all_findings:
                all_findings[fid] = info

    # Output as JSON
    output = {
        "extracted_findings": {
            fid: {"seat": info["seat"], "source_severity": info["source_severity"]}
            for fid, info in sorted(all_findings.items())
        },
        "total": len(all_findings),
        "by_seat": {},
    }

    for fid, info in all_findings.items():
        seat = info["seat"]
        if seat not in output["by_seat"]:
            output["by_seat"][seat] = 0
        output["by_seat"][seat] += 1

    json.dump(output, sys.stdout, indent=2)
    print(file=sys.stderr)
    print(f"Extracted {len(all_findings)} findings from {len(sys.argv)-1} reports", file=sys.stderr)


if __name__ == "__main__":
    main()

---

# Bismillah ir-Rahman ir-Rahim
