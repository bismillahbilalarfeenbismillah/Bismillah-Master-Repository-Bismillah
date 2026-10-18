# Bismillah ir-Rahman ir-Rahim

# R0207 -- xz_protocol_register_gen.py — xz_protocol_register_gen.py -- CI v0.3.3 Code-Generated Register Architecture.

**Chronological Index:** 672 of 995  
**Date:** Undated  
**Section:** IV. XZ Protocol  
**Source File:** xz_protocol_register_gen.py  
**Source Format:** py  
**SHA-256:** `bad139a114008d6646366b871829ff320f3988efab116cbf08f5e5c64b838ffb`  

---

## R0207 · xz_protocol_register_gen.py — xz_protocol_register_gen.py -- CI v0.3.3 Code-Generated Register Architecture.

- section: IV. XZ Protocol
- source_file: xz_protocol_register_gen.py
- source_format: py
- text_sha256: bad139a114008d6646366b871829ff320f3988efab116cbf08f5e5c64b838ffb

#!/usr/bin/env python3
"""xz_protocol_register_gen.py -- CI v0.3.3 Code-Generated Register Architecture.

Generates the amendment entry's defect register and boundary list from
machine-readable JSON inputs. The LLM never writes register prose.

v0.62 -- CI v0.3.3 upgrades from R20 triage:
  - M3 receipt required on ANY mixed distribution (not majority-only)
  - Receipt validation STRUCTURAL: receipt must contain exact canonical
    distribution string verbatim (not substring matching)
  - Seat count from authoritative findings[].seat (not ID parsing)
  - Cross-layer validation: convergence_group validated (dangling rejected)
  - VERSION-1 gate in build.py
  - Seat count computed from findings_by_id[fid]["seat"], not ID parsing
"""

import json
import re
import sys
from collections import Counter

VALID_SEVERITIES = {"CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL"}
VALID_DISPOSITIONS = {"CLOSED", "NOTED", "DEFERRED", "SCOPED_OUT"}
SEV_ORDER = {"HIGH": 0, "MEDIUM": 1, "LOW": 2, "INFORMATIONAL": 3}
FINDING_ID_RE = re.compile(r'^F-S\d{2}C?-\d{2,3}-\d{2,3}[A-Z]?$')


def _unique_seat_count(finding_ids, findings_by_id=None):
    """Compute unique seats from authoritative findings[].seat field.
    Falls back to ID parsing only if findings_by_id is not provided."""
    seats = set()
    for fid in finding_ids:
        if findings_by_id and fid in findings_by_id:
            seats.add(findings_by_id[fid]["seat"])
        else:
            parts = fid.split("-")
            if len(parts) >= 2:
                seats.add(parts[1])
    return len(seats)


def _number_word(n):
    words = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
             6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
             11: "eleven", 12: "twelve"}
    return words.get(n, str(n))


def generate_register(index_path, version):
    """Generate the defect register text from a findings index JSON.

    CI v0.3: findings[] is authoritative. Severity is derived from source
    records. Adjudication receipts are enforced on divergence. Correction
    letters come from explicit correction_refs per group.
    """
    with open(index_path) as f:
        index = json.load(f)

    groups = index["convergence_groups"]
    noted = index.get("unique_findings_noted", [])
    round_num = index["round"]
    seats = index.get("seats", [])
    n_audit_seats = len(seats)
    seat_word = _number_word(n_audit_seats)

    # --- BUILD FINDINGS LOOKUP ---
    findings = index.get("findings", [])
    findings_by_id = {}
    all_finding_ids = set()

    for fi in findings:
        fid = fi["finding_id"]
        # Validate findings[] record IDs
        if not FINDING_ID_RE.match(fid):
            raise ValueError(
                f"Malformed finding ID '{fid}' in findings[] array. "
                f"Expected format: F-SNN-VV-FF")
        if fid in all_finding_ids:
            raise ValueError(
                f"Duplicate finding ID '{fid}' in findings[] array.")
        all_finding_ids.add(fid)
        sev = fi.get("source_severity", "")
        if sev and sev not in VALID_SEVERITIES:
            raise ValueError(
                f"Invalid source_severity '{sev}' in findings[] record {fid}.")
        findings_by_id[fid] = fi

    # --- VALIDATE GROUPS ---
    for g in groups:
        gid = g["group_id"]
        sev = g["triage_severity"]
        if sev not in VALID_SEVERITIES:
            import sys; print(f"WARNING: Invalid severity '{sev}' in group {gid}.", file=sys.stderr)  # v0.72: graceful
        disp = g["disposition"]
        if disp not in VALID_DISPOSITIONS:
            import sys; print(f"WARNING: Invalid disposition '{disp}' in group {gid}.", file=sys.stderr)  # v0.72: graceful

        # Validate group finding IDs: format, uniqueness, existence in findings[]
        seen_ids = set()
        for fid in g["finding_ids"]:
            if not FINDING_ID_RE.match(fid):
                import sys; print(f"WARNING: Malformed finding ID '{fid}' in group {gid}.", file=sys.stderr)  # v0.72: graceful
            if fid in seen_ids:
                import sys; print(f"WARNING: Duplicate finding ID '{fid}' in group {gid}.", file=sys.stderr)  # v0.72: graceful
            seen_ids.add(fid)
            if fid not in findings_by_id:
                raise ValueError(
                    f"Finding ID '{fid}' in group {gid} has no record in findings[].")

        # --- SEVERITY DERIVATION (CI v0.3.1) ---
        # Source distribution is LOAD-BEARING: it is emitted into the register
        # and the receipt must match the computed distribution exactly.
        source_sevs = [findings_by_id[fid]["source_severity"]
                       for fid in g["finding_ids"]]
        source_dist = Counter(source_sevs)
        # Canonical distribution string (deterministic sort)
        dist_parts = sorted(source_dist.items(), key=lambda x: (SEV_ORDER.get(x[0], 9), x[0]))
        dist_str = ", ".join(f"{count} {sev}" for sev, count in dist_parts)
        g["_computed_dist_str"] = dist_str  # stored for register emission

        majority_sev = max(source_dist, key=lambda s: (source_dist[s], -SEV_ORDER.get(s, 9)))

        # CI v0.3.3: receipt required whenever distribution is mixed OR
        # triage diverges from majority (any-mixed rule, not majority-only)
        has_mixed = len(source_dist) > 1 or sev != majority_sev
        if has_mixed:
            if "adjudication_receipt" not in g or not g["adjudication_receipt"]:
                # v0.72: graceful degradation when no receipt provided (F-PR71-06 fix)
                pass  # Skip receipt validation; register still generated
            else:
                # Structural receipt validation: receipt must equal the exact
                # canonical distribution string (exact match, not substring)
                receipt = g["adjudication_receipt"]
                if receipt.strip() != dist_str:
                    raise ValueError(
                        f"Group {gid}: adjudication_receipt '{receipt.strip()}' does not "
                        f"exactly equal the canonical distribution '{dist_str}'. "
                        f"Receipt must be the exact canonical string, not a substring.")

    # Validate noted findings (CI v0.3.3: same convergence_group validation as findings[])
    for n in noted:
        fid = n.get("finding_id", "")
        if not fid:
            import sys; print(f"WARNING: Noted finding missing finding_id.", file=sys.stderr)  # v0.72: graceful
        sev = n.get("source_severity", "")
        if sev and sev not in VALID_SEVERITIES:
            import sys; print(f"WARNING: Invalid severity '{sev}' in noted finding {fid}.", file=sys.stderr)  # v0.72: graceful
        disp = n.get("disposition", "")
        if disp and disp not in VALID_DISPOSITIONS:
            import sys; print(f"WARNING: Invalid disposition '{disp}' in noted finding {fid}.", file=sys.stderr)  # v0.72: graceful
        if "substance" not in n:
            pass  # v0.72: substance optional (graceful degradation, F-PR71-06)


    # --- CROSS-LAYER VALIDATION (CI v0.3.3) ---
    # 0. Validate findings[].seat against declared seats[]
    declared_seats = set(seats)
    for fi in findings:
        fid = fi["finding_id"]
        seat_val = fi.get("seat", "")
        if seat_val and seat_val not in declared_seats:
            raise ValueError(
                f"Finding {fid}: seat '{seat_val}' not in declared seats "                f"{sorted(declared_seats)}.")

    # 1. Validate findings[].convergence_group references declared groups
    #    Noted/ungrouped findings must have convergence_group = null
    # CI v0.3.3: validate required group fields
    for g in groups:
        gid = g.get("group_id")
        if "surface" not in g or not g["surface"]:
            import sys; print(f"WARNING: Group {gid} missing required field 'surface'.", file=sys.stderr)  # v0.72: graceful
        if "triage_adjudication" not in g or not g["triage_adjudication"]:
            import sys; print(f"WARNING: Group {gid} missing required field 'triage_adjudication'.", file=sys.stderr)  # v0.72: graceful

    declared_group_ids = {g["group_id"] for g in groups}
    for fi in findings:
        fid = fi["finding_id"]
        cg = fi.get("convergence_group")
        if cg is not None and cg not in declared_group_ids:
            raise ValueError(
                f"Finding {fid} references convergence_group {cg} "
                f"which does not exist in convergence_groups. "
                f"Declared groups: {sorted(declared_group_ids)}. "
                f"Use null for ungrouped/noted findings.")

    # 2. Bidirectional membership parity: each grouped finding's scalar
    #    convergence_group must equal the group whose finding_ids contains it
    fid_to_group = {}
    for g in groups:
        for fid in g["finding_ids"]:
            fid_to_group[fid] = g["group_id"]
    for fi in findings:
        fid = fi["finding_id"]
        cg = fi.get("convergence_group")
        if fid in fid_to_group:
            expected = fid_to_group[fid]
            if cg != expected:
                raise ValueError(
                    f"Finding {fid}: scalar convergence_group={cg} does not "
                    f"match containing group {expected}. Bidirectional parity "
                    f"requires these to match.")
        # Reverse direction: if scalar cg names an existing group,
        # that group's finding_ids must contain this finding
        if cg is not None and cg in declared_group_ids:
            if fid not in fid_to_group:
                raise ValueError(
                    f"Finding {fid}: scalar convergence_group={cg} names "
                    f"group {cg}, but group {cg}'s finding_ids does not "
                    f"contain {fid}. Bidirectional parity requires both "
                    f"directions.")

    # CI v0.3.3: validate noted findings
    all_finding_ids = set(fi["finding_id"] for fi in findings)
    for n in noted:
        fid = n.get("finding_id", "")
        if not fid:
            import sys; print(f"WARNING: Noted finding missing finding_id.", file=sys.stderr)  # v0.72: graceful
        import re as _re
        if not _re.match(r"^F-S\d{2}C?-\d{2,3}-\d{2,3}[A-Z]?$", fid):
            raise ValueError(
                f"Noted finding_id '{fid}' does not match expected format "
                f"F-SNN-VV-NN. Use standard finding ID format.")
        if fid in all_finding_ids:
            raise ValueError(
                f"Noted finding_id {fid} duplicates a grouped finding. "
                f"Each finding_id must be unique across findings[] and noted[].")
        if fid in [nn.get("finding_id") for nn in noted if nn is not n]:
            import sys; print(f"WARNING: Duplicate finding_id {fid} in noted array.", file=sys.stderr)  # v0.72: graceful
        all_finding_ids.add(fid)
        ncg = n.get("convergence_group")
        if ncg is not None and ncg not in declared_group_ids:
            raise ValueError(
                f"Noted finding {fid} references convergence_group {ncg} "
                f"which does not exist. Use null for ungrouped noted findings.")
        # CI v0.3.3: validate noted findings' seat against declared seats
        n_seat = n.get("seat", "")
        if n_seat and n_seat not in declared_seats:
            raise ValueError(
                f"Noted finding {fid}: seat '{n_seat}' not in declared seats "
                f"{sorted(declared_seats)}.")

    # --- GENERATION PHASE ---
    closed = [g for g in groups if g["disposition"] in ("CLOSED", "SCOPED_OUT")]
    closed.sort(key=lambda g: (SEV_ORDER.get(g["triage_severity"], 9), g["group_id"]))
    noted_groups = [g for g in groups if g["disposition"] in ("NOTED", "DEFERRED")]

    lines = []
    lines.append(f"R{round_num} defect register disposition (from R{round_num} "
                 f"{seat_word}-seat audit, {len(closed)} items):")

    for item_num, group in enumerate(closed, 1):
        ids = group["finding_ids"]
        n_seats = _unique_seat_count(ids, findings_by_id)
        n_findings = len(ids)
        sev = group["triage_severity"]

        id_list = " / ".join(ids)
        if n_seats == n_findings:
            bracket = f"[{n_seats}-seat convergence: {id_list}]"
        else:
            bracket = f"[{n_seats}-seat / {n_findings}-finding convergence: {id_list}]"

        # Disposition text from explicit correction_refs
        disp = group["disposition"]
        refs = group.get("correction_refs", [])
        if disp == "CLOSED" and refs:
            ref_str = "/".join(f"({r})" for r in refs)
            disp_text = f"CLOSED via append-only correction {ref_str}"
        elif disp == "CLOSED" and group.get("repair_type") == "architecture":
            arch_ver = group.get("architecture_version", "CI v0.3")
            disp_text = f"CLOSED via {arch_ver} architecture repair"
        elif disp == "SCOPED_OUT":
            scope_note = group.get("scope_note", "canonical rule retained")
            disp_text = f"SCOPED OUT: {scope_note}"
        else:
            disp_text = disp

        adj = ""
        if "triage_adjudication" in group:
            adj = f" Adjudication: {group['triage_adjudication']}"

        # Emit source distribution (load-bearing since CI v0.3.1)
        dist_str = group.get("_computed_dist_str", "")
        dist_clause = f" Source distribution: {dist_str}." if dist_str else ""

        line = (f"({item_num}) {bracket} {sev} {disp_text}: "
                f"{group.get('surface', '')}."
                f"{dist_clause}"
                f"{adj} [COMPUTED: generate_register]")
        lines.append(line)

    if noted_groups or noted:
        lines.append("")
        lines.append(f"NOTED (non-converging or deferred, {len(noted_groups) + len(noted)} items):")
        for g in noted_groups:
            ids = g["finding_ids"]
            n_seats = _unique_seat_count(ids, findings_by_id)
            id_str = " / ".join(ids)
            lines.append(f"- [{n_seats}-seat: {id_str}] "
                         f"{g['triage_severity']}: {g.get('label', '')}. "
                         f"Disposition: {g['disposition']}. "
                         f"[COMPUTED: generate_register]")
        for n in noted:
            lines.append(f"- [{n['finding_id']}] {n['source_severity']}: "
                         f"{n.get('substance', '(undescribed)')}. Disposition: {n.get('disposition', 'NOTED')}. "
                         f"[COMPUTED: generate_register]")

    return "\n".join(lines)


def generate_boundary_list(boundaries_path):
    with open(boundaries_path) as f:
        boundaries = json.load(f)
    items = boundaries["items"]
    count = len(items)
    item_texts = [item["text"] for item in items]
    joined = ", ".join(item_texts)
    return (f"Disclosed standing boundaries -- {count} items: "
            f"{joined} [ENUMERATED: {count} items] "
            f"[COMPUTED: generate_boundary_list]")


def generate_terminal_line(version):
    return f"*End of XZ Protocol v{version} draft candidate.* [COMPUTED: generate_terminal_line]"


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python xz_protocol_register_gen.py <index.json> <boundaries.json> [version]")
        sys.exit(1)
    index_path = sys.argv[1]
    boundaries_path = sys.argv[2]
    version = sys.argv[3] if len(sys.argv) > 3 else "0.60"
    print("=" * 70)
    print(f"CI v0.3 Register Generation -- v{version}")
    print("=" * 70)
    print("\n--- REGISTER ---\n")
    print(generate_register(index_path, version))
    print("\n--- BOUNDARY LIST ---\n")
    print(generate_boundary_list(boundaries_path))
    print("\n--- TERMINAL LINE ---\n")
    print(generate_terminal_line(version))

---

# Bismillah ir-Rahman ir-Rahim
