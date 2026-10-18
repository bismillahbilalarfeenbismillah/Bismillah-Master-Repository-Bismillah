# Bismillah ir-Rahman ir-Rahim

# R0198 -- xz_protocol_closure_gate.txt — Closure-claim gate for the XZ Protocol package.

**Chronological Index:** 666 of 995  
**Date:** Undated  
**Section:** IV. XZ Protocol  
**Source File:** xz_protocol_closure_gate.txt  
**Source Format:** txt  
**SHA-256:** `6dd2aa0dfee59b7ef1e9ec3c680ad3794cf0455d0efb3a8d11d104b32861b64b`  

---

## R0198 · xz_protocol_closure_gate.txt — Closure-claim gate for the XZ Protocol package.

- section: IV. XZ Protocol
- source_file: xz_protocol_closure_gate.txt
- source_format: txt
- text_sha256: 6dd2aa0dfee59b7ef1e9ec3c680ad3794cf0455d0efb3a8d11d104b32861b64b

"""Closure-claim gate for the XZ Protocol package.

Absorbs F-XZ10-OP-03, F-XZ11-OP-03, F-XZ12-OP-01.

What this gate does, stated so the docstring and the implementation
cannot drift apart:

1. Parses the Section 27 amendment record and extracts every finding
   identifier whose recorded disposition is CLOSED. Dispositions of the
   form "DISCLOSED, NOT CLOSED" and "NOTED" are read and deliberately
   not treated as closures.
2. Requires every CLOSED identifier to appear in
   xz_protocol_locus_register.json. An unregistered closure claim is a
   failure: the point of the register is that a closure cannot be
   asserted without a machine-checkable locus.
3. Evaluates each registered assertion against the CURRENT package
   bytes. Assertions on the protocol text are evaluated against the body
   with the Section 27 amendment record removed, so a closure claim can
   never be satisfied by the log entry that asserts it. That inversion
   is what allowed the v0.12 predecessor to return PASS on an unfixed
   body.
4. Delegated entries name the gate that discharges them; that gate must
   exist in the package.

The v0.12 predecessor searched for two hardcoded strings, one of which
never occurred in the document and one of which was the corrected form
rather than the defective form, so it returned PASS precisely when the
fix was absent. Every check here is derived from the register and the
amendment record at run time; nothing is hardcoded.

Exit 0 = PASS. Exit 1 = FAIL.
"""
from __future__ import annotations

import ast
import glob
import json
import os
import re
import sys

AMENDMENT_HEADING = "## 27. Amendment record"
REGISTER = "xz_protocol_locus_register.json"

FINDING = r"F-[A-Z0-9]+(?:-[A-Z0-9]+)*-\d+"
CLOSED_CLAIM = re.compile(FINDING + r"\s+CLOSED\b")
NOT_CLOSED = re.compile(FINDING + r"\s+(?:DISCLOSED,\s*NOT\s+CLOSED|NOTED|OPEN)\b")
IDENT = re.compile(FINDING)


def package_dir() -> str:
    return os.path.dirname(os.path.abspath(__file__))


def protocol_path(root: str) -> str:
    candidates = sorted(glob.glob(os.path.join(root, "xz_protocol_v0_*.md")))
    if len(candidates) != 1:
        raise SystemExit(
            f"FAIL: expected exactly one protocol text, found {len(candidates)}"
        )
    return candidates[0]


def split_protocol(root: str) -> tuple[str, str]:
    text = open(protocol_path(root), encoding="utf-8").read()
    if AMENDMENT_HEADING not in text:
        raise SystemExit("FAIL: protocol text has no Section 27 amendment record")
    cut = text.index(AMENDMENT_HEADING)
    return text[:cut], text[cut:]


def parse_closure_claims(amendment_text: str) -> tuple[set[str], set[str]]:
    """Return (closed, explicitly_not_closed) finding identifiers."""
    not_closed = {IDENT.search(m.group(0)).group(0)
                  for m in NOT_CLOSED.finditer(amendment_text)}
    closed = {IDENT.search(m.group(0)).group(0)
              for m in CLOSED_CLAIM.finditer(amendment_text)}
    return closed - not_closed, not_closed


def test_function_count(path: str) -> int:
    tree = ast.parse(open(path, encoding="utf-8").read())
    return sum(
        1
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name.startswith("test_")
    )


def resolve_target(root: str, body: str, target: str) -> str | None:
    if target == "protocol_body":
        return body
    if target == "_package":
        return None
    path = os.path.join(root, target)
    if not os.path.exists(path):
        return None
    return open(path, encoding="utf-8").read()


def evaluate(root: str, body: str, fid: str, entry: dict) -> list[str]:
    errors: list[str] = []

    if "delegated_to" in entry:
        gate = entry["delegated_to"]
        if not os.path.exists(os.path.join(root, gate)):
            errors.append(f"  {fid}: delegated to {gate}, which is not in the package")
        return errors

    if "historical" in entry:
        return errors

    assertions = entry.get("assertions")
    if not assertions:
        errors.append(f"  {fid}: register entry has no assertions and is not delegated")
        return errors

    for a in assertions:
        target, kind, value = a["target"], a["type"], a.get("value")

        if kind == "file_exists":
            if not os.path.exists(os.path.join(root, value)):
                errors.append(f"  {fid}: required file {value} is absent")
            continue

        if kind == "test_function_count":
            path = os.path.join(root, target)
            if not os.path.exists(path):
                errors.append(f"  {fid}: {target} is absent")
                continue
            actual = test_function_count(path)
            if actual != value:
                errors.append(
                    f"  {fid}: {target} has {actual} test functions, register says {value}"
                )
            continue

        text = resolve_target(root, body, target)
        if text is None:
            errors.append(f"  {fid}: target {target} is absent")
            continue

        if kind == "present" and value not in text:
            errors.append(f"  {fid}: {target} is missing required text {value[:70]!r}")
        elif kind == "absent" and value in text:
            errors.append(f"  {fid}: {target} still contains {value[:70]!r}")
        elif kind == "section_contains":
            start, until = a["section"], a["until"]
            if start not in text or until not in text:
                errors.append(f"  {fid}: section bounds not found in {target}")
                continue
            lo = text.index(start)
            hi = text.index(until, lo)
            if value not in text[lo:hi]:
                errors.append(
                    f"  {fid}: section {start!r} does not contain {value[:60]!r}"
                )
        elif kind not in ("present", "absent", "section_contains"):
            errors.append(f"  {fid}: unknown assertion type {kind!r}")

    return errors


def main() -> int:
    root = package_dir()
    body, amendment = split_protocol(root)

    reg_path = os.path.join(root, REGISTER)
    if not os.path.exists(reg_path):
        print(f"FAIL: locus register {REGISTER} is absent")
        return 1
    register = {
        k: v for k, v in json.load(open(reg_path, encoding="utf-8")).items()
        if not k.startswith("_")
    }

    closed, not_closed = parse_closure_claims(amendment)

    errors: list[str] = []
    for fid in sorted(closed):
        if fid not in register:
            errors.append(
                f"  {fid}: marked CLOSED in the amendment record with no register entry"
            )
            continue
        errors.extend(evaluate(root, body, fid, register[fid]))

    for fid in sorted(register):
        if fid not in closed and fid not in not_closed:
            errors.extend(evaluate(root, body, fid, register[fid]))

    if errors:
        print(f"FAIL: {len(errors)} closure-claim errors:")
        for e in errors:
            print(e)
        return 1

    print(
        f"PASS: {len(closed)} closure claims verified against current bytes; "
        f"{len(not_closed)} disposition(s) recorded as not closed "
        f"({', '.join(sorted(not_closed)) or 'none'})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

---

# Bismillah ir-Rahman ir-Rahim
