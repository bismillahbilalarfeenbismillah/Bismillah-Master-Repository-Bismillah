# Bismillah ir-Rahman ir-Rahim

# R0510 -- finalize_packet_v0_5.py — Insert artifact hashes into the dispatch brief, then write SHA256SUMS.

**Chronological Index:** 794 of 995  
**Date:** Undated  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** finalize_packet_v0_5.py  
**Source Format:** py  
**SHA-256:** `22e2474c04f229db45a202eafaf7948b63b85382fc728f15cec25202ecde299e`  

---

## R0510 · finalize_packet_v0_5.py — Insert artifact hashes into the dispatch brief, then write SHA256SUMS.

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: finalize_packet_v0_5.py
- source_format: py
- text_sha256: 22e2474c04f229db45a202eafaf7948b63b85382fc728f15cec25202ecde299e

"""Insert artifact hashes into the dispatch brief, then write SHA256SUMS.

Order matters: the brief must be written before the manifest, because the
manifest covers the brief. The manifest never lists itself.
"""
import hashlib
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
BRIEF = "SHVVP_v0_5_AUDIT_DISPATCH_BRIEF.md"
MANIFEST = "SHA256SUMS"
SKIP_PREFIX = ("__pycache__",)

ROLES = {
    "SHV_VALIDATION_PROTOCOL_v0_5_source.md":
        "**PRIMARY ARTIFACT UNDER AUDIT, canonical source.** Authoritative",
    "SHV_VALIDATION_PROTOCOL_v0_5.pdf":
        "**ARTIFACT UNDER AUDIT, flagship render.** 30 pages, monochrome",
    "SHV_VALIDATION_PROTOCOL_v0_5.html": "Rendering, self-contained HTML",
    "SHV_VALIDATION_PROTOCOL_v0_5.docx": "Rendering, Word",
    "pandoc_shvvp.css": "Monochrome stylesheet for the HTML rendering",
    "shvvp_v0_5_decision_rules.py":
        "**NORMATIVE AND UNDER AUDIT.** Phase B total ordered label mapping; Phase C total priority order",
    "shvvp_v0_5_route_gates.py":
        "**NORMATIVE AND UNDER AUDIT.** Raw-evidence-only descriptive route gates. No p-value, no null, no bound, no multiplicity procedure",
    "shvvp_v0_5_regression_scan.py":
        "**UNDER AUDIT.** Contextual scan separating historical from current references to the withdrawn design size",
    "SHVVP_v0_5_FOCUSED_DELTA_ADDENDUM.md":
        "**PART OF THE BRIEF.** Focused-delta audit permission, immutable v0.3 receipts, mandatory audit surface",
    "SHV_VALIDATION_PROTOCOL_v0_3_source.md":
        "**LINEAGE, UNMODIFIED.** HALTED v0.3 canonical source",
    "SHV_VALIDATION_PROTOCOL_v0_4_source.md":
        "**LINEAGE, UNMODIFIED.** HALTED v0.4 canonical source, the exact artifact audited in round 4",
    "SHV_VALIDATION_PROTOCOL_v0_4.pdf":
        "**LINEAGE, UNMODIFIED.** HALTED v0.4 flagship render, the exact artifact audited in round 4",
    "SHVVP_v0_4_SEAT_A_GPT_DELTA_VERDICT.md":
        "**LINEAGE, UNMODIFIED.** Round 4 GPT-class verdict, HALT, findings F-P4-1 to F-P4-3, preserved unmodified",
    "SHVVP_v0_4_PRODUCER_COMPLETION_REPORT.md":
        "**LINEAGE, UNMODIFIED.** v0.4 producer completion report. ADVISORY, not a verdict",
    "SHV_VALIDATION_PROTOCOL_v0_3.pdf":
        "**LINEAGE, UNMODIFIED.** HALTED v0.3 flagship render, the exact artifact audited in round 3",
    "SHVVP_v0_3_SEAT_A_GPT_VERDICT.md":
        "**LINEAGE, UNMODIFIED.** Round 3 GPT-class verdict, HALT, findings F-P3-1 to F-P3-6",
    "SHVVP_v0_3_SEAT_B_GEMINI_VERDICT.md":
        "**LINEAGE, UNMODIFIED.** Round 3 Gemini-class verdict, PASS, zero findings, preserved in full",
    "sim_v0_5_stdout.log": "Raw simulation stdout for this freeze",
    "sim_v0_5_stderr.log": "Stage progress log for this freeze",
    "shvvp_v0_5_power_sim.py":
        "**NORMATIVE AND UNDER AUDIT.** Exact frozen BCa interval rule and staged design simulation",
    "test_shvvp_v0_5_rules.py": "Deterministic and statistical tests over the normative modules, including the round 3 boundary counterexamples and invalid-input fuzzing",
    "power_sim_receipt.json": "Machine-readable receipt of the staged simulation",
    "power_sim_run.log": "Raw simulation stdout for this freeze",
    "power_sim_progress.log": "Stage progress log for this freeze",
    "shvvp_v0_5_power_chart.py": "Monochrome figure generator, reads the receipt",
    "shvvp-v0-5-phase-b-power.png": "Figure embedded in the contract",
    "inject_sim_values_v0_5.py": "Writes receipt figures into the canonical source",
    "build_shvvp_v0_5_pdf.py": "Markdown to monochrome PDF renderer",
    "finalize_packet_v0_5.py": "Writes the brief hash table and the manifest",
    "SHVVP_v0_5_AMENDMENT_AND_ADJUDICATION_RECORD.md":
        "**UNDER AUDIT.** Append-only register and adjudication for all three rounds",
    "SHVVP_v0_5_AUDIT_LEDGER.md":
        "Producer-side build-gate ledger. ADVISORY, test it rather than trust it",
    "SHVVP_v0_5_AUDIT_DISPATCH_BRIEF.md": "This brief. Hashed in the manifest, not in the table above",
    "DEPOSIT_METADATA_v0_5.md": "Deposit metadata, held pending convergence",
    "README.md": "Packet overview and verification instructions",
    "verify_shvvp_v0_5.py": "Producer-built verifier, 22 gates. Default mode is verify-only. ADVISORY",
    "verifier_receipt.json": "Machine-readable output of the producer verifier run",
    "SHV_VALIDATION_PROTOCOL_v0_1.md":
        "**LINEAGE, UNMODIFIED.** HALTED v0.1 canonical source, never deposited as binding",
    "SHV_VALIDATION_PROTOCOL_v0_1.pdf": "**LINEAGE, UNMODIFIED.** HALTED v0.1 render",
    "SHV_VALIDATION_PROTOCOL_v0_2_source.md":
        "**LINEAGE, UNMODIFIED.** HALTED v0.2 canonical source, the exact artifact audited in round 2",
    "SHV_VALIDATION_PROTOCOL_v0_2.pdf":
        "**LINEAGE, UNMODIFIED.** HALTED v0.2 flagship render, the exact artifact audited in round 2",
    "SHVVP_v0_1_SEAT_A_GPT_VERDICT.md": "**LINEAGE, UNMODIFIED.** Round 1 GPT-class verdict, HALT",
    "SHVVP_v0_1_SEAT_B_GEMINI_VERDICT.md":
        "**LINEAGE, UNMODIFIED.** Round 1 Gemini-class verdict, PASS-WITH-AMENDMENTS",
    "SHVVP_v0_2_SEAT_A_GPT_VERDICT.md":
        "**LINEAGE, UNMODIFIED.** Round 2 GPT-class verdict, HALT, findings F-P2-1 to F-P2-4",
    "SHVVP_v0_2_SEAT_B_GEMINI_VERDICT.md":
        "**LINEAGE, UNMODIFIED.** Round 2 Gemini-class verdict, PASS, zero findings, preserved in full",
    "SHVVP_v0_2_SHA256SUMS.txt": "The v0.2 packet manifest, for custody continuity",
}


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def members():
    out = []
    for name in sorted(os.listdir(HERE)):
        path = os.path.join(HERE, name)
        if not os.path.isfile(path) or name == MANIFEST or name.startswith(SKIP_PREFIX):
            continue
        out.append(name)
    return out


def main():
    names = members()
    rows = ["| File | SHA-256 | Role |", "|---|---|---|"]
    for name in names:
        if name == BRIEF:
            continue
        rows.append("| `%s` | `%s` | %s |"
                    % (name, sha256(os.path.join(HERE, name)),
                       ROLES.get(name, "Packet member")))
    table = "\n".join(rows)

    brief_path = os.path.join(HERE, BRIEF)
    text = open(brief_path, encoding="utf-8").read()
    if "<!--HASH_TABLE-->" in text:
        text = text.replace("<!--HASH_TABLE-->", table)
    else:
        text = re.sub(r"\| File \| SHA-256 \| Role \|.*?(?=\n\n)", table, text,
                      flags=re.S)
    open(brief_path, "w", encoding="utf-8").write(text)
    print("brief hash table written: %d rows" % (len(rows) - 2))

    lines = ["%s  %s" % (sha256(os.path.join(HERE, n)), n) for n in members()]
    open(os.path.join(HERE, MANIFEST), "w").write("\n".join(lines) + "\n")
    print("manifest written: %d members, excludes itself" % len(lines))


if __name__ == "__main__":
    main()

---

# Bismillah ir-Rahman ir-Rahim
