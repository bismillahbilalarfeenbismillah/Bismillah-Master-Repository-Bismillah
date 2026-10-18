# Bismillah ir-Rahman ir-Rahim

# R0202 -- xz_protocol_history_gate.txt — Amendment-record integrity gate for the XZ Protocol package.

**Chronological Index:** 668 of 995  
**Date:** Undated  
**Section:** IV. XZ Protocol  
**Source File:** xz_protocol_history_gate.txt  
**Source Format:** txt  
**SHA-256:** `21425870915457adcdc97f8c403679c56c734b7d2108c9343c270c772de544d0`  

---

## R0202 · xz_protocol_history_gate.txt — Amendment-record integrity gate for the XZ Protocol package.

- section: IV. XZ Protocol
- source_file: xz_protocol_history_gate.txt
- source_format: txt
- text_sha256: 21425870915457adcdc97f8c403679c56c734b7d2108c9343c270c772de544d0

"""Amendment-record integrity gate for the XZ Protocol package.

Absorbs F-XZ10-OP-01, F-XZ11-OP-01, F-XZ12-OP-07.

Axiom 1 requires that no prior declaration is silently rewritten. This
lineage has mutated a historical amendment entry in place four times
(v0.4, v0.9, and twice in v0.11), and each mutation was found by an
auditor rather than by the build. This gate moves that detection into
the build.

HISTORY.sha256 records one SHA-256 per amendment entry, keyed by version.
On every run the gate re-derives the entries from the protocol text and
compares. A changed historical entry fails. A newly appended entry that
is not yet in HISTORY.sha256 is reported and fails, so the record has to
be sealed deliberately with --seal rather than drifting.

Scope limit, stated because it bounds what this gate can prove: the file
is generated from the bytes present when it is first sealed, so it can
only detect mutation from that point forward. It is not evidence about
any entry as it stood in an earlier packet. Establishing that requires
recomputation from the archived packet by a non-producer seat, which is
tracked separately under F-XZ09-OP-04, recorded as DISCLOSED, NOT CLOSED.

Exit 0 = PASS. Exit 1 = FAIL.
"""
from __future__ import annotations

import glob
import hashlib
import os
import re
import sys

AMENDMENT_HEADING = "## 27. Amendment record"
ENTRY = re.compile(r"^- \*\*v(\d+\.\d+) \(", re.M)
HISTORY = "HISTORY.sha256"


def package_dir() -> str:
    return os.path.dirname(os.path.abspath(__file__))


def protocol_path(root: str) -> str:
    candidates = sorted(glob.glob(os.path.join(root, "xz_protocol_v0_*.md")))
    if len(candidates) != 1:
        raise SystemExit(
            f"FAIL: expected exactly one protocol text, found {len(candidates)}"
        )
    return candidates[0]


def entries(root: str) -> dict[str, str]:
    """Map version label to SHA-256 of that amendment entry's exact bytes."""
    text = open(protocol_path(root), encoding="utf-8").read()
    if AMENDMENT_HEADING not in text:
        raise SystemExit("FAIL: no Section 27 amendment record")
    amend = text[text.index(AMENDMENT_HEADING):]

    marks = [(m.group(1), m.start()) for m in ENTRY.finditer(amend)]
    out: dict[str, str] = {}
    for i, (version, start) in enumerate(marks):
        end = marks[i + 1][1] if i + 1 < len(marks) else len(amend)
        blob = amend[start:end].rstrip()
        out[version] = hashlib.sha256(blob.encode()).hexdigest()
    return out


def read_history(root: str) -> dict[str, str]:
    path = os.path.join(root, HISTORY)
    if not os.path.exists(path):
        return {}
    out = {}
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        digest, version = line.split(None, 1)
        out[version.strip()] = digest
    return out


def seal(root: str) -> int:
    current = entries(root)
    lines = [
        "# XZ Protocol amendment-record integrity file.",
        "# One SHA-256 per Section 27 entry. Verified by xz_protocol_history_gate.py.",
        "# A changed historical entry fails the build. Re-seal only when appending.",
    ]
    for version in sorted(current, key=lambda v: [int(x) for x in v.split(".")]):
        lines.append(f"{current[version]}  {version}")
    open(os.path.join(root, HISTORY), "w", encoding="utf-8").write(
        "\n".join(lines) + "\n"
    )
    print(f"SEALED: {len(current)} amendment entries written to {HISTORY}")
    return 0


def main() -> int:
    root = package_dir()
    if "--seal" in sys.argv:
        return seal(root)

    current = entries(root)
    recorded = read_history(root)

    if not recorded:
        print(f"FAIL: {HISTORY} is absent; run --seal to establish the baseline")
        return 1

    errors = []
    for version, digest in sorted(current.items()):
        if version not in recorded:
            errors.append(
                f"  v{version}: entry present in the protocol text but not sealed in "
                f"{HISTORY}; re-seal deliberately after appending"
            )
        elif recorded[version] != digest:
            errors.append(
                f"  v{version}: amendment entry has changed since it was sealed "
                f"({recorded[version][:16]}... -> {digest[:16]}...); Axiom 1 forbids "
                f"in-place edits of historical entries"
            )
    for version in sorted(recorded):
        if version not in current:
            errors.append(f"  v{version}: sealed entry has been removed from the record")

    if errors:
        print(f"FAIL: {len(errors)} amendment-record integrity errors:")
        for e in errors:
            print(e)
        return 1

    print(f"PASS: {len(current)} amendment entries match their sealed digests")
    return 0


if __name__ == "__main__":
    sys.exit(main())

---

# Bismillah ir-Rahman ir-Rahim
