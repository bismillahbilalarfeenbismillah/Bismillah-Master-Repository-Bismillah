# Bismillah ir-Rahman ir-Rahim

# R0852 -- REGISTER_GENERATOR.txt — xz_protocol_register_gen.py -- CI v0.2.1 Code-Generated Register Architecture.

**Chronological Index:** 939 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** REGISTER_GENERATOR.txt  
**Source Format:** txt  
**SHA-256:** `410c8b94aec3e64ea625f771258d9054789a0e3f4c4e6bbea6787c2ba9cc56cf`  

---

## R0852 · REGISTER_GENERATOR.txt — xz_protocol_register_gen.py -- CI v0.2.1 Code-Generated Register Architecture.

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: REGISTER_GENERATOR.txt
- source_format: txt
- text_sha256: 410c8b94aec3e64ea625f771258d9054789a0e3f4c4e6bbea6787c2ba9cc56cf

#!/usr/bin/env python3
"""xz_protocol_register_gen.py -- CI v0.2.1 Code-Generated Register Architecture.

Generates the amendment entry's defect register and boundary list from
machine-readable JSON inputs. The LLM never writes register prose.

v0.58 -- CI v0.2.1 upgrades from R16 triage:
  - Dual cardinality: emits both seat count and finding count
  - Seat count computed from unique seat prefixes in finding_ids
  - Finding count computed from len(finding_ids)
  - Severity validation: rejects unknown severity tokens at generation time
  - Reads from findings[] array for source_severity provenance when present
"""

import json
import sys

VALID_SEVERITIES = {"HIGH", "MEDIUM", "LOW", "INFORMATIONAL"}
SEV_ORDER = {"HIGH": 0, "MEDIUM": 1, "LOW": 2, "INFORMATIONAL": 3}


def _unique_seat_count(finding_ids):
    """Compute the number of unique seats from finding ID prefixes.

    Finding IDs follow the pattern F-S<NN>-<VV>-<FF>.
    The seat is extracted as the S<NN> component.
    """
    seats = set()
    for fid in finding_ids:
        parts = fid.split("-")
        if len(parts) >= 2:
            seats.add(parts[1])  # e.g., "S01"
    return len(seats)


def generate_register(index_path, version):
    """Generate the defect register text from a findings index JSON.

    Returns the register block (from header through NOTED clause),
    ready for insertion into the amendment entry. Deterministic:
    same input always produces same output.

    CI v0.2.1: seat_count is derived from unique seat prefixes.
    finding_count is len(finding_ids). Both are emitted.
    Severity tokens are validated against VALID_SEVERITIES.
    """
    with open(index_path) as f:
        index = json.load(f)

    groups = index["convergence_groups"]
    noted = index.get("unique_findings_noted", [])
    round_num = index["round"]

    # Validate all severity tokens before generation
    for g in groups:
        sev = g["triage_severity"]
        if sev not in VALID_SEVERITIES:
            raise ValueError(
                f"Invalid severity '{sev}' in convergence group {g['group_id']}. "
                f"Valid: {sorted(VALID_SEVERITIES)}"
            )
    for n in noted:
        sev = n.get("source_severity", "")
        if sev and sev not in VALID_SEVERITIES:
            raise ValueError(
                f"Invalid severity '{sev}' in noted finding {n['finding_id']}. "
                f"Valid: {sorted(VALID_SEVERITIES)}"
            )

    # Sort: CLOSED items by severity (HIGH first), then group_id
    closed = [g for g in groups if g["disposition"] == "CLOSED"]
    closed.sort(key=lambda g: (SEV_ORDER.get(g["triage_severity"], 9), g["group_id"]))
    noted_groups = [g for g in groups if g["disposition"] in ("NOTED", "DEFERRED")]

    # Correction letter assignment.
    # The protocol uses (a)-(z), then (ba)-(bz), then (ca)-(cz), etc.
    # v0.57 used (bv)-(by). Next available: (bz), then (ca), (cb), ...
    # start_letter_offset is the position within the full sequence.
    # (a)=0..(z)=25, (ba)=26..(bz)=51, (ca)=52..(cz)=77, ...
    # v0.57 ended at (by) = position 50. Next = 51 = (bz).
    _correction_start = 51  # (bz)
    correction_idx = 0

    lines = []
    # Register header
    lines.append(f"R{round_num} defect register disposition (from R{round_num} "
                 f"five-seat audit, {len(closed)} items):")

    # Numbered items
    for item_num, group in enumerate(closed, 1):
        ids = group["finding_ids"]
        # CI v0.2.1: compute both cardinalities from the data
        n_seats = _unique_seat_count(ids)
        n_findings = len(ids)
        sev = group["triage_severity"]
        defect = group["defect_class"]
        disp = group["disposition"]
        repair = group.get("repair_type", "correction")

        # Build the convergence bracket with dual cardinality
        id_list = " / ".join(ids)
        if n_seats == n_findings:
            bracket = f"[{n_seats}-seat convergence: {id_list}]"
        else:
            bracket = f"[{n_seats}-seat / {n_findings}-finding convergence: {id_list}]"

        # Build disposition text
        if repair == "correction":
            pos = _correction_start + correction_idx
            correction_idx += 1
            # (a)-(z) = positions 0-25, (ba)-(bz) = 26-51, (ca)-(cz) = 52-77
            series = pos // 26   # 0 -> single letter, 1 -> b_, 2 -> c_, ...
            offset = pos % 26
            if series == 0:
                label = chr(ord('a') + offset)
            else:
                prefix = chr(ord('a') + series)   # b, c, d, ...
                suffix = chr(ord('a') + offset)
                label = f"{prefix}{suffix}"
            disp_text = f"{disp} via append-only correction ({label})"
        elif repair == "gate":
            gate_id = group.get("gate_id", "[10x]")
            disp_text = f"{disp} via gate {gate_id}"
        elif repair == "architecture":
            disp_text = f"{disp} via CI v0.2.1 architecture repair"
        else:
            disp_text = disp

        # Adjudication receipt if present
        adj = ""
        if "triage_adjudication" in group:
            adj = f" Adjudication: {group['triage_adjudication']}"

        line = (f"({item_num}) {bracket} {sev} {disp_text}: "
                f"{defect}.{adj} [COMPUTED: generate_register]")
        lines.append(line)

    # NOTED clause for non-converging findings
    if noted_groups or noted:
        lines.append("")
        lines.append(f"NOTED (non-converging or deferred, {len(noted_groups) + len(noted)} items):")
        for g in noted_groups:
            ids = g["finding_ids"]
            n_seats = _unique_seat_count(ids)
            id_str = " / ".join(ids)
            lines.append(f"- [{n_seats}-seat: {id_str}] "
                         f"{g['triage_severity']}: {g['defect_class']}. "
                         f"Disposition: {g['disposition']}."
                         f"{' ' + g.get('note', '') if g.get('note') else ''} "
                         f"[COMPUTED: generate_register]")
        for n in noted:
            lines.append(f"- [{n['finding_id']}] {n['source_severity']}: "
                         f"{n['substance']}. Disposition: {n['disposition']}."
                         f"{' ' + n.get('note', '') if n.get('note') else ''} "
                         f"[COMPUTED: generate_register]")

    return "\n".join(lines)


def generate_boundary_list(boundaries_path):
    """Generate the standing-boundary paragraph from a boundaries JSON file.

    Returns the boundary block ready for insertion into the amendment entry.
    Deterministic: same input always produces same output.
    """
    with open(boundaries_path) as f:
        boundaries = json.load(f)

    items = boundaries["items"]
    count = len(items)

    # Build the comma-separated list
    item_texts = [item["text"] for item in items]
    joined = ", ".join(item_texts)

    return (f"Disclosed standing boundaries -- {count} items: "
            f"{joined} [ENUMERATED: {count} items] "
            f"[COMPUTED: generate_boundary_list]")


def generate_terminal_line(version):
    """Generate the terminal version line. Code-stamped, never LLM-typed."""
    return f"*End of XZ Protocol v{version} draft candidate.*"


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python xz_protocol_register_gen.py <index.json> <boundaries.json> [version]")
        sys.exit(1)

    index_path = sys.argv[1]
    boundaries_path = sys.argv[2]
    version = sys.argv[3] if len(sys.argv) > 3 else "0.58"

    print("=" * 70)
    print(f"CI v0.2.1 Register Generation -- v{version}")
    print("=" * 70)

    print("\n--- REGISTER ---\n")
    register = generate_register(index_path, version)
    print(register)

    print("\n--- BOUNDARY LIST ---\n")
    boundary = generate_boundary_list(boundaries_path)
    print(boundary)

    print("\n--- TERMINAL LINE ---\n")
    terminal = generate_terminal_line(version)
    print(terminal)

---

# Bismillah ir-Rahman ir-Rahim
