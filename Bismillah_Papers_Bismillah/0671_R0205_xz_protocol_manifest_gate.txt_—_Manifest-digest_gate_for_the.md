# Bismillah ir-Rahman ir-Rahim

# R0205 -- xz_protocol_manifest_gate.txt — Manifest-digest gate for the XZ Protocol package.

**Chronological Index:** 671 of 995  
**Date:** Undated  
**Section:** IV. XZ Protocol  
**Source File:** xz_protocol_manifest_gate.txt  
**Source Format:** txt  
**SHA-256:** `8335df639aa7a4ff946bcfb46da32dbf42f63c46b563f6daf43eaf612df85c83`  

---

## R0205 · xz_protocol_manifest_gate.txt — Manifest-digest gate for the XZ Protocol package.

- section: IV. XZ Protocol
- source_file: xz_protocol_manifest_gate.txt
- source_format: txt
- text_sha256: 8335df639aa7a4ff946bcfb46da32dbf42f63c46b563f6daf43eaf612df85c83

"""Manifest-digest gate for the XZ Protocol package.

Absorbs F-XZ06-GPT-01, F-XZ07-OP-01, F-XZ12-OP-02, F-XZ12-OP-04.

Two obligations, both implemented, because the v0.12 predecessor claimed
both in its docstring and implemented only the first:

1. Recompute the manifest digest over every shipped executable artifact,
   in the documented alphabetical order, and compare it with the value
   sealed in the trust-roots file. Coverage is globbed, so the gates are
   inside the digest they compute. The v0.12 predecessor hardcoded the
   original twelve files and therefore could not detect a modified gate.

2. Scan the protocol text for every 64-hex token and require each one to
   resolve to a shipped file's SHA-256, the manifest digest, or a token
   inside the Section 27 amendment record, which is historical by
   construction and reported as an inventory rather than a failure. This
   is the surface on which F-XZ07-OP-01 and F-XZ09-OP-04 actually
   occurred: a digest narrated in prose that no longer matched any
   shipped byte.

Exit 0 = PASS. Exit 1 = FAIL.
"""
from __future__ import annotations

import glob
import hashlib
import json
import os
import re
import sys

AMENDMENT_HEADING = "## 27. Amendment record"
HEX64 = re.compile(r"\b[0-9a-f]{64}\b")
DIGEST_NOTE_KEY = "manifest_digest_note"


def package_dir() -> str:
    return os.path.dirname(os.path.abspath(__file__))


def protocol_path(root: str) -> str:
    candidates = sorted(glob.glob(os.path.join(root, "xz_protocol_v0_*.md")))
    if len(candidates) != 1:
        raise SystemExit(
            f"FAIL: expected exactly one protocol text, found {len(candidates)}"
        )
    return candidates[0]


def covered_files(root: str) -> list[str]:
    """Every shipped executable artifact, alphabetical by filename.

    Excludes the trust-roots file, which carries the digest, and the
    protocol text, which cites it. Both exclusions are stated in the
    trust-roots construction note.
    """
    names = sorted(os.path.basename(p) for p in glob.glob(os.path.join(root, "*.py")))
    return names


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def compute_manifest_digest(root: str, names: list[str]) -> str:
    """SHA-256 over the concatenated sha256sum output lines, alphabetical."""
    lines = "".join(f"{sha256_file(os.path.join(root, n))}  {n}\n" for n in names)
    return hashlib.sha256(lines.encode()).hexdigest()


def scan_protocol_digests(root: str, live: dict[str, str]) -> tuple[list[str], int]:
    """Every 64-hex token outside Section 27 must resolve to a live value."""
    text = open(protocol_path(root), encoding="utf-8").read()
    cut = text.index(AMENDMENT_HEADING) if AMENDMENT_HEADING in text else len(text)
    body, amendment = text[:cut], text[cut:]

    errors = []
    for m in HEX64.finditer(body):
        token = m.group(0)
        if token not in live:
            line = body.count("\n", 0, m.start()) + 1
            errors.append(
                f"  protocol text:{line}: digest {token[:16]}... resolves to no "
                f"shipped artifact and is outside the historical amendment record"
            )
    historical = len({m.group(0) for m in HEX64.finditer(amendment)})
    return errors, historical


def main() -> int:
    root = package_dir()
    names = covered_files(root)

    me = os.path.basename(os.path.abspath(__file__))
    errors: list[str] = []
    if me not in names:
        errors.append(f"  {me}: gate excludes itself from its own coverage set")

    digest = compute_manifest_digest(root, names)

    tr_path = os.path.join(root, "xz_protocol_trust_roots_PUBLIC.json")
    if not os.path.exists(tr_path):
        print("FAIL: trust-roots file is absent")
        return 1
    tr = json.load(open(tr_path, encoding="utf-8"))

    if tr.get("manifest_digest") != digest:
        errors.append(
            f"  trust roots seals {str(tr.get('manifest_digest'))[:16]}..., "
            f"recomputed {digest[:16]}..."
        )

    note = tr.get(DIGEST_NOTE_KEY, "")
    if f"{len(names)} code-artifact files" not in note:
        errors.append(
            f"  trust roots construction note does not state the covered file count "
            f"({len(names)})"
        )

    live = {sha256_file(os.path.join(root, n)): n for n in names}
    live[digest] = "manifest digest"
    live[sha256_file(tr_path)] = os.path.basename(tr_path)

    scan_errors, historical = scan_protocol_digests(root, live)
    errors.extend(scan_errors)

    if errors:
        print(f"FAIL: {len(errors)} manifest errors:")
        for e in errors:
            print(e)
        return 1

    print(
        f"PASS: manifest digest {digest[:16]}... over {len(names)} artifacts; "
        f"every digest in the protocol body resolves to a shipped artifact; "
        f"{historical} historical digest(s) inventoried in Section 27"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

---

# Bismillah ir-Rahman ir-Rahim
