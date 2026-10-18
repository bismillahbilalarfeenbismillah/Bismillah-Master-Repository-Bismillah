# Bismillah ir-Rahman ir-Rahim

# R0206 -- xz_protocol_prohibited_content_verifier.txt — Prohibited-content and prohibited-claim verifier for the XZ Protocol package.

**Chronological Index:** 7 of 995  
**Date:** 2024  
**Section:** IV. XZ Protocol  
**Source File:** xz_protocol_prohibited_content_verifier.txt  
**Source Format:** txt  
**SHA-256:** `e9a00f8d5e11c81ef95732d954a6cae67a3e83608f69ca5ca7fd11deaf363ef2`  

---

## R0206 · xz_protocol_prohibited_content_verifier.txt — Prohibited-content and prohibited-claim verifier for the XZ Protocol package.

- section: IV. XZ Protocol
- source_file: xz_protocol_prohibited_content_verifier.txt
- source_format: txt
- text_sha256: e9a00f8d5e11c81ef95732d954a6cae67a3e83608f69ca5ca7fd11deaf363ef2

"""Prohibited-content and prohibited-claim verifier for the XZ Protocol package.

Absorbs F-XZ09-OP-05 and F-XZ12-OP-07. This is the artifact Section 22
item 1 and Section 23 item 16 refer to; before v0.13 those sections named
a verifier that did not exist.

Three obligations:

1. Prohibited language. Every pattern in the Section 0.3 register is
   searched across the protocol text and every shipped code file. The
   Section 0.3 register itself is excluded by line range, located from
   its heading rather than by a magic number.

2. Declared exemptions. A small number of sentences elsewhere in the
   document contain a prohibited token while stating the prohibition
   rather than committing it -- for example a sentence declaring that a
   contrast is not an estimate of attack prevention. These are listed
   below as exact strings with the section that authorizes each one. The
   list is closed and asserted in both directions: an unlisted hit fails,
   and a listed sentence that has disappeared from the document also
   fails, so the exemption list cannot rot into a blanket permission.
   A proximity or negation heuristic was deliberately not used; that is
   the shape of escape hatch this program has had to close four times.

3. Citation restriction. The set of non-DOI URLs in the protocol text
   must equal exactly the four permitted XZ sources of Section 26.3, and
   no payload, activation, or reconstruction token may appear anywhere.

Exit 0 = PASS. Exit 1 = FAIL.
"""
from __future__ import annotations

import glob
import os
import re
import sys

PROHIBITION_HEADING = "### 0.3 Prohibited language"
NEXT_HEADING = "### 0.4"

PATTERNS = {
    "effectiveness verb applied to BSSG": re.compile(
        r"BSSG[^.]{0,140}?\b(prevents|mitigates|reduces|ensures|guarantees|protects)\b"
        r"|\b(prevents|mitigates|reduces|ensures|guarantees|protects)\b[^.]{0,140}?BSSG"
    ),
    "outcome modal applied to history": re.compile(r"would have"),
    "attack-prevention framing": re.compile(r"attack prevention"),
    "unqualified kernel-denies claim": re.compile(r"the kernel denies the attack"),
    "validation claim": re.compile(r"Structural Honesty has been validated"),
    "DENY-class aggregation": re.compile(
        r"DENY_FALSE\s*\+\s*DENY_UNKNOWN"
        r"|\b(?:sum|summed|total|totalled|combined|aggregated|pooled)\b[^.]{0,60}"
        r"DENY_FALSE[^.]{0,60}DENY_UNKNOWN"
    ),
}

# Closed list. Each entry is an exact substring that contains a prohibited
# token while stating the prohibition, plus the section that authorizes it.
DECLARED_EXEMPTIONS = [
    (
        "It is not an estimate of attack prevention, deployment behavior, "
        "causal outcome change, adversary adaptation, or population performance",
        "Section 2.2 claim boundary",
    ),
]

PERMITTED_XZ_SOURCES = {
    "https://www.openwall.com/lists/oss-security/2024/03/29/4",
    "https://nvd.nist.gov/vuln/detail/cve-2024-3094",
    "https://github.com/tukaani-project/xz/issues/103",
    "https://github.com/advisories/GHSA-rxwq-x6h5-x525",
}

HAZARD_TOKENS = ["ifunc", "got_plt", "rsa_public_decrypt", "activation recipe"]

# A file that carries prohibited strings as test data must declare itself with
# this exact marker. The declaration is explicit, enumerable, and reported in
# the PASS line, rather than a silent per-filename skip.
FIXTURE_MARKER = "PROHIBITED_CONTENT_FIXTURES = True"

URL = re.compile(r"https?://[^)\s\]]+")


def package_dir() -> str:
    return os.path.dirname(os.path.abspath(__file__))


def protocol_path(root: str) -> str:
    candidates = sorted(glob.glob(os.path.join(root, "xz_protocol_v0_*.md")))
    if len(candidates) != 1:
        raise SystemExit(
            f"FAIL: expected exactly one protocol text, found {len(candidates)}"
        )
    return candidates[0]


def register_span(text: str) -> tuple[int, int]:
    if PROHIBITION_HEADING not in text:
        raise SystemExit("FAIL: Section 0.3 prohibition register not found")
    lo = text.index(PROHIBITION_HEADING)
    hi = text.index(NEXT_HEADING, lo)
    return lo, hi


def exempt_spans(text: str) -> list[tuple[int, int]]:
    spans = []
    for phrase, _ in DECLARED_EXEMPTIONS:
        start = 0
        while True:
            i = text.find(phrase, start)
            if i < 0:
                break
            spans.append((i, i + len(phrase)))
            start = i + 1
    return spans


def covered(pos: int, spans: list[tuple[int, int]]) -> bool:
    return any(lo <= pos < hi for lo, hi in spans)


def main() -> int:
    root = package_dir()
    proto = protocol_path(root)
    text = open(proto, encoding="utf-8").read()
    errors: list[str] = []

    # Obligation 2, second direction: every declared exemption must still exist.
    for phrase, authority in DECLARED_EXEMPTIONS:
        if phrase not in text:
            errors.append(
                f"  declared exemption for {authority} is no longer present in the "
                f"protocol text; the exemption list is stale"
            )

    reg_lo, reg_hi = register_span(text)
    allowed = [(reg_lo, reg_hi)] + exempt_spans(text)

    targets = [(os.path.basename(proto), text, allowed)]
    declared_fixtures = []
    for p in sorted(glob.glob(os.path.join(root, "*.py"))):
        name = os.path.basename(p)
        # This verifier necessarily carries the prohibited tokens as patterns.
        if name == os.path.basename(os.path.abspath(__file__)):
            continue
        src = open(p, encoding="utf-8").read()
        if FIXTURE_MARKER in src:
            declared_fixtures.append(name)
            continue
        targets.append((name, src, []))

    for name, body, spans in targets:
        for label, pattern in PATTERNS.items():
            for m in pattern.finditer(body):
                if covered(m.start(), spans):
                    continue
                line = body.count("\n", 0, m.start()) + 1
                errors.append(f"  {name}:{line}: {label}: {m.group(0)[:70]!r}")

    # Obligation 3: citation restriction and hazard tokens.
    urls = {u.rstrip(".,);") for u in URL.findall(text)}
    non_doi = {u for u in urls if "doi.org" not in u}
    if non_doi != PERMITTED_XZ_SOURCES:
        for extra in sorted(non_doi - PERMITTED_XZ_SOURCES):
            errors.append(f"  protocol text cites a non-permitted source: {extra}")
        for missing in sorted(PERMITTED_XZ_SOURCES - non_doi):
            errors.append(f"  protocol text no longer cites permitted source: {missing}")

    low = text.lower()
    for token in HAZARD_TOKENS:
        if token in low:
            errors.append(f"  protocol text: hazard token present: {token!r}")

    adversarial = os.path.join(root, "test_xz_protocol_adversarial.py")
    if os.path.exists(adversarial):
        src_adv = open(adversarial, encoding="utf-8").read().lower()
        missing = [t for t in HAZARD_TOKENS if t not in src_adv]
        if missing:
            errors.append(
                "  test_xz_protocol_adversarial.py no longer checks for hazard "
                f"tokens: {', '.join(missing)}"
            )
    else:
        errors.append("  adversarial suite is absent; hazard-token control removed")

    if errors:
        print(f"FAIL: {len(errors)} prohibited-content errors:")
        for e in errors:
            print(e)
        return 1

    print(
        f"PASS: prohibited-language register clean across {len(targets)} files "
        f"({len(DECLARED_EXEMPTIONS)} declared exemptions, all still present); "
        f"citations restricted to the {len(PERMITTED_XZ_SOURCES)} permitted XZ sources; "
        f"no hazard tokens; declared fixture carriers: "
        f"{', '.join(declared_fixtures) or 'none'}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

---

# Bismillah ir-Rahman ir-Rahim
