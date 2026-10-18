# Bismillah ir-Rahman ir-Rahim

# R0355 -- shvvp_v0_5_regression_scan.py — Contextual regression scan for the withdrawn 1,280-session design size.

**Chronological Index:** 739 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** shvvp_v0_5_regression_scan.py  
**Source Format:** py  
**SHA-256:** `8f5f7c0a52f8e93f26eb20f892c3c46ba9c2b422a8b8045cbc5123aac23ee12a`  

---

## R0355 · shvvp_v0_5_regression_scan.py — Contextual regression scan for the withdrawn 1,280-session design size.

- section: V. BSSG & SHVVP Protocols
- source_file: shvvp_v0_5_regression_scan.py
- source_format: py
- text_sha256: 8f5f7c0a52f8e93f26eb20f892c3c46ba9c2b422a8b8045cbc5123aac23ee12a

"""Contextual regression scan for the withdrawn 1,280-session design size.

Carrying finding F-P3-5: v0.3 froze a 1,440-session confirmatory design in
Section 6.8 and then, in Section 11, still froze a "1,280-session confirmatory
run". A plain string ban cannot fix that, because the packet MUST keep saying that
v0.2 used 1,280 sessions and that the design grew: deleting the history would hide
the amendment. This scan therefore classifies each occurrence as HISTORICAL or
CURRENT and fails only on CURRENT ones.

An occurrence is an OFFENCE if its surrounding context (a 400-character window, so
that a wrapped rendering is judged by the same sentence as the canonical source)
mentions the withdrawn size AND asserts it as a current
commitment (frozen, confirmatory run or design, deliverable, selected, planned,
will be, the design is) AND carries no historical marker (v0.1, v0.2, v0.3, withdrawn,
superseded, grew from, below target, earlier, previous, prior, historical,
8 repetitions, round 1, round 2, amendment, and the scan's own vocabulary). Data receipts and design-ladder rows, which
legitimately tabulate 1,280 as one rung of the frozen ladder, are not offences.

Used by verifier gate G13 and by test T19 so the two cannot drift apart.
"""
from __future__ import annotations

import os
import re

WITHDRAWN = ("1,280", "1280")
CURRENT = re.compile(
    r"frozen|confirmatory run|confirmatory design|deliverable|will be|is selected|"
    r"planned|the design is|current design|freezes", re.I)
HISTORICAL = re.compile(
    r"v0\.1|v0\.2|v0\.3|withdrawn|superseded|grew from|below target|"
    r"lower bound below|earlier|previous|prior|historical|was 1,280|"
    r"8 repetitions|reps= ?8|round 1|round 2|F-P3-5|amendment|stale|scan|"
    r"rung|offence|not in sec|regression|increases from|from 1,280|to 1,440|"
    r"lower bound is below|A-2\.\d|A-3\.\d", re.I)
SKIP_PREFIXES = ("SHV_VALIDATION_PROTOCOL_v0_1", "SHV_VALIDATION_PROTOCOL_v0_2",
                 "SHV_VALIDATION_PROTOCOL_v0_3", "SHVVP_v0_1_SEAT",
                 "SHVVP_v0_2_SEAT", "SHVVP_v0_3_SEAT")
SCAN_EXT = (".md", ".py", ".json", ".txt", ".css", ".html")
DATA_FILES = ("power_sim_receipt.json",)


def scan(root: str = ".") -> dict:
    """Return {'offences': [...], 'historical': [...], 'ladder': [...]}."""
    offences, historical, ladder = [], [], []
    for name in sorted(os.listdir(root)):
        if not name.endswith(SCAN_EXT) or name.startswith(SKIP_PREFIXES):
            continue
        path = os.path.join(root, name)
        if not os.path.isfile(path):
            continue
        text = open(path, encoding="utf-8", errors="replace").read()
        for m in re.finditer(r"1,280|1280", text):
            i = m.start()
            line_start = text.rfind("\n", 0, i) + 1
            line_end = text.find("\n", i)
            line = text[line_start:line_end if line_end != -1 else len(text)]
            # a character window, so that a wrapped rendering is classified by the same
            # sentence as the canonical source rather than by an arbitrary line break
            context = text[max(0, i - 400):i + 400]
            where = "%s:%d" % (name, text.count("\n", 0, i) + 1)
            if name in DATA_FILES or line.lstrip().startswith("|"):
                ladder.append(where)
            elif HISTORICAL.search(context):
                historical.append(where)
            elif CURRENT.search(context):
                offences.append(where + " :: " + line.strip()[:160])
            else:
                historical.append(where)
    return {"offences": offences, "historical": historical, "ladder": ladder}


if __name__ == "__main__":
    res = scan(os.path.dirname(os.path.abspath(__file__)))
    print("offences: %d" % len(res["offences"]))
    for o in res["offences"]:
        print("  " + o)
    print("historical references preserved: %d" % len(res["historical"]))
    print("ladder or data rows: %d" % len(res["ladder"]))

---

# Bismillah ir-Rahman ir-Rahim
