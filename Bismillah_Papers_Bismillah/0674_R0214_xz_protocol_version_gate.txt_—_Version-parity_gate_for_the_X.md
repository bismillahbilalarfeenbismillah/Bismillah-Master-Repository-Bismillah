# Bismillah ir-Rahman ir-Rahim

# R0214 -- xz_protocol_version_gate.txt — Version-parity gate for the XZ Protocol package.

**Chronological Index:** 674 of 995  
**Date:** Undated  
**Section:** IV. XZ Protocol  
**Source File:** xz_protocol_version_gate.txt  
**Source Format:** txt  
**SHA-256:** `3adbe8cb040423caba10d8bee472773b53b1939613eba0f42960ec808c9bd273`  

---

## R0214 · xz_protocol_version_gate.txt — Version-parity gate for the XZ Protocol package.

- section: IV. XZ Protocol
- source_file: xz_protocol_version_gate.txt
- source_format: txt
- text_sha256: 3adbe8cb040423caba10d8bee472773b53b1939613eba0f42960ec808c9bd273

"""Version-parity gate for the XZ Protocol package.

Absorbs F-XZ10-OP-04, F-XZ11-OP-02, F-XZ12-OP-02, F-XZ12-OP-03.

Design notes, stated because the v0.12 predecessor failed on each of them:

* Coverage is derived by globbing the package directory, never hardcoded.
  The gate asserts its own filename is inside its coverage set, so a gate
  that excludes itself cannot pass.
* Matches are examined by span (re.finditer), never by re-locating the
  first occurrence of the matched text. The v0.12 gate used text.index,
  so one whitelisted mention excused every later mismatch in the file.
* There is no proximity whitelist. Historical version references are
  admissible only inside a structured exclusion region: for the protocol
  text, the Section 27 amendment record, which is historical by
  definition and append-only by Axiom 1. Executable files carry exactly
  one stamp and get no exemption at all.
* --self-test mutates a copy of the package and asserts the gate returns
  a nonzero exit code for each covered file class.

Exit 0 = PASS. Exit 1 = FAIL.
"""
from __future__ import annotations

import glob
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

VERSION_TOKEN = re.compile(r"XZ Protocol v(\d+\.\d+)")
FRONT_MATTER_VERSION = re.compile(r"^\*\*Version:\*\*\s*(\d+\.\d+)")
AMENDMENT_HEADING = "## 27. Amendment record"


def package_dir() -> str:
    return os.path.dirname(os.path.abspath(__file__))


def protocol_path(root: str) -> str:
    candidates = sorted(glob.glob(os.path.join(root, "xz_protocol_v0_*.md")))
    if len(candidates) != 1:
        raise SystemExit(
            f"FAIL: expected exactly one protocol text, found {len(candidates)}: "
            + ", ".join(os.path.basename(c) for c in candidates)
        )
    return candidates[0]


def declared_version(path: str) -> str:
    for line in open(path, encoding="utf-8"):
        m = FRONT_MATTER_VERSION.match(line)
        if m:
            return m.group(1)
    raise SystemExit("FAIL: no '**Version:**' line in protocol front matter")


def coverage(root: str) -> list[str]:
    files = sorted(glob.glob(os.path.join(root, "*.py")))
    files += sorted(glob.glob(os.path.join(root, "*.json")))
    files += [protocol_path(root)]
    return files


def excluded_span(path: str, text: str) -> tuple[int, int]:
    """Byte range in which historical version references are admissible."""
    if path.endswith(".md") and AMENDMENT_HEADING in text:
        return (text.index(AMENDMENT_HEADING), len(text))
    return (-1, -1)


def check(root: str) -> list[str]:
    proto = protocol_path(root)
    expected = declared_version(proto)
    errors: list[str] = []
    files = coverage(root)

    me = os.path.basename(os.path.abspath(__file__))
    if me not in [os.path.basename(f) for f in files]:
        errors.append(f"  {me}: gate excludes itself from its own coverage set")

    for path in files:
        text = open(path, encoding="utf-8").read()
        lo, hi = excluded_span(path, text)
        for m in VERSION_TOKEN.finditer(text):
            if lo <= m.start() < hi:
                continue
            if m.group(1) != expected:
                line = text.count("\n", 0, m.start()) + 1
                errors.append(
                    f"  {os.path.basename(path)}:{line}: found v{m.group(1)}, "
                    f"expected v{expected}"
                )

    tr = os.path.join(root, "xz_protocol_trust_roots_PUBLIC.json")
    if os.path.exists(tr):
        declared = json.load(open(tr, encoding="utf-8")).get("protocol")
        if declared != f"XZ Protocol v{expected}":
            errors.append(
                f"  trust roots: protocol field is {declared!r}, "
                f"expected 'XZ Protocol v{expected}'"
            )
    else:
        errors.append("  trust roots file is absent")

    return errors


def self_test(root: str) -> int:
    """Mutate a copy and assert the gate fires for each covered file class."""
    stray = "XZ Protocol " + "v" + "0.1"  # assembled so this source carries no literal stamp
    cases = [
        ("module", "xz_protocol_kernel.py"),
        ("test suite", "test_xz_protocol_kernel.py"),
        ("gate", "xz_protocol_manifest_gate.py"),
        ("protocol text", None),
    ]
    failures = []
    for label, target in cases:
        with tempfile.TemporaryDirectory() as tmp:
            work = os.path.join(tmp, "pkg")
            shutil.copytree(root, work)
            if target is None:
                p = protocol_path(work)
                t = open(p, encoding="utf-8").read()
                head = t.index(AMENDMENT_HEADING)
                t = t[:head] + "\n" + stray + " stray reference\n" + t[head:]
                open(p, "w", encoding="utf-8").write(t)
            else:
                p = os.path.join(work, target)
                t = open(p, encoding="utf-8").read()
                open(p, "w", encoding="utf-8").write("# " + stray + "\n" + t)
            rc = subprocess.call(
                [sys.executable, os.path.join(work, os.path.basename(__file__))],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            if rc == 0:
                failures.append(f"  self-test: mutated {label} did not fire the gate")

    with tempfile.TemporaryDirectory() as tmp:
        work = os.path.join(tmp, "pkg")
        shutil.copytree(root, work)
        rc = subprocess.call(
            [sys.executable, os.path.join(work, os.path.basename(__file__))],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if rc != 0:
            failures.append("  self-test: unmutated package did not pass")

    if failures:
        print("FAIL: version gate self-test:")
        for f in failures:
            print(f)
        return 1
    print("PASS: version gate self-test (4 mutations fired, clean package passed)")
    return 0


def main() -> int:
    root = package_dir()
    if "--self-test" in sys.argv:
        return self_test(root)
    errors = check(root)
    if errors:
        print(f"FAIL: {len(errors)} version-parity errors:")
        for e in errors:
            print(e)
        return 1
    print(
        f"PASS: version parity v{declared_version(protocol_path(root))} "
        f"across {len(coverage(root))} shipped files"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

---

# Bismillah ir-Rahman ir-Rahim
