# Bismillah ir-Rahman ir-Rahim

# R0537 -- three_way_projection.py — Source-SBOM-binary three-way projection orchestrator (NEW v1.9.0).

**Chronological Index:** 813 of 995  
**Date:** Undated  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** three_way_projection.py  
**Source Format:** py  
**SHA-256:** `100bfd3a122596382a9b636ea94cb08535819fb1daacdc5180726deb40f60717`  

---

## R0537 · three_way_projection.py — Source-SBOM-binary three-way projection orchestrator (NEW v1.9.0).

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: three_way_projection.py
- source_format: py
- text_sha256: 100bfd3a122596382a9b636ea94cb08535819fb1daacdc5180726deb40f60717

"""Source-SBOM-binary three-way projection orchestrator (NEW v1.9.0).

Per strategy Phase 3.1 Step 6 task 4:
    Source-SBOM-binary three-way projection check (30 triples; per-category box).
Per strategy Phase 3.1 Step 7:
    Worked: v1.3.0 manifest-vs-model parity pattern translates to SBOM-vs-binary
    parity. Failed: prior SBOM-correctness verification without binary cross-check.
    Cow Episode: do NOT invent new SBOM-vs-binary discrepancy categories.

The strategy enumerates exactly three discrepancy categories:
    BYN-3WAY-001: SBOM component missing in source
    BYN-3WAY-002: source package missing in SBOM
    BYN-3WAY-003: SBOM component not in binary

Source manifests supported (subset of NTIA-recommended): package.json (npm),
Python requirements.txt, Cargo.toml. Binary "embedded package list" is a
witness inventory: in this orchestrator we accept it as an explicit set of
package names supplied by the caller (derived elsewhere, e.g., from a wheel
archive walk or node_modules manifest).

Patent invariant: orchestration over existing extractor outputs. No new
analyzer kind. The verdict aggregator is not modified.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Optional, Set, Tuple

from bayyinah.aggregator.finding import Finding, Severity
from bayyinah.extractors.sbom_extractor import SBOMDocument, parse_sbom


@dataclass(frozen=True)
class ThreeWayProjectionResult:
    findings: Tuple[Finding, ...]
    sbom_components: Tuple[str, ...]
    source_packages: Tuple[str, ...]
    binary_packages: Tuple[str, ...]


def _parse_package_json_names(text: str) -> Set[str]:
    try:
        doc = json.loads(text)
    except json.JSONDecodeError:
        return set()
    out: Set[str] = set()
    for key in ("dependencies", "devDependencies", "peerDependencies"):
        d = doc.get(key)
        if isinstance(d, dict):
            for name in d.keys():
                if isinstance(name, str):
                    out.add(name)
    return out


def _parse_requirements_txt(text: str) -> Set[str]:
    out: Set[str] = set()
    for line in text.splitlines():
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        m = re.match(r"^([A-Za-z0-9_.\-]+)", line)
        if m:
            out.add(m.group(1).lower())
    return out


def _parse_cargo_toml_names(text: str) -> Set[str]:
    """Minimal TOML-section extractor for [dependencies] table."""
    out: Set[str] = set()
    in_deps = False
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("["):
            in_deps = s.startswith("[dependencies") or s == "[dependencies]"
            continue
        if in_deps and "=" in s and not s.startswith("#"):
            name = s.split("=", 1)[0].strip()
            if name:
                out.add(name)
    return out


def parse_source_manifest(
    name: str, data: bytes
) -> Set[str]:
    """Return the set of package names declared in a source manifest."""
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return set()
    n = name.lower()
    if n.endswith("package.json"):
        return _parse_package_json_names(text)
    if n.endswith("requirements.txt"):
        return _parse_requirements_txt(text)
    if n.endswith("cargo.toml") or n.endswith("cargo.lock"):
        return _parse_cargo_toml_names(text)
    return set()


def three_way_projection(
    sbom_bytes: bytes,
    source_manifest_name: str,
    source_manifest_bytes: bytes,
    binary_package_names: Iterable[str],
) -> ThreeWayProjectionResult:
    """Reconcile SBOM <-> source manifest <-> binary embedded package list.

    Emits BYN-3WAY-001/002/003 per the named categories.
    """
    sbom = parse_sbom(sbom_bytes)
    if sbom is None:
        return ThreeWayProjectionResult(
            findings=(
                Finding(
                    code="BYN-SBOM-001",
                    severity=Severity.HIGH,
                    path="<sbom>",
                    surface_claim="SBOM document",
                    substrate_actual="unparseable",
                    witness="SBOM parser rejected input during three-way projection",
                    layer_classification="BATIN",
                ),
            ),
            sbom_components=tuple(),
            source_packages=tuple(),
            binary_packages=tuple(),
        )

    sbom_names = {c.name.lower() for c in sbom.components if c.name}
    source_names = {
        n.lower() for n in parse_source_manifest(source_manifest_name, source_manifest_bytes)
    }
    binary_names = {str(n).lower() for n in binary_package_names}

    findings: List[Finding] = []

    # BYN-3WAY-001: SBOM has it, source doesn't
    for n in sorted(sbom_names - source_names):
        findings.append(
            Finding(
                code="BYN-3WAY-001",
                severity=Severity.HIGH,
                path=f"sbom/component[{n}]",
                surface_claim=f"SBOM declares component {n}",
                substrate_actual=f"source manifest {source_manifest_name} does not declare {n}",
                witness=f"SBOM component {n} missing in source",
                layer_classification="ZAHIR",
            )
        )
    # BYN-3WAY-002: source has it, SBOM doesn't
    for n in sorted(source_names - sbom_names):
        findings.append(
            Finding(
                code="BYN-3WAY-002",
                severity=Severity.HIGH,
                path=f"source/{source_manifest_name}/package[{n}]",
                surface_claim=f"source manifest declares package {n}",
                substrate_actual="SBOM does not declare component",
                witness=f"Source package {n} missing in SBOM",
                layer_classification="ZAHIR",
            )
        )
    # BYN-3WAY-003: SBOM has it, binary doesn't
    for n in sorted(sbom_names - binary_names):
        findings.append(
            Finding(
                code="BYN-3WAY-003",
                severity=Severity.HIGH,
                path=f"sbom/component[{n}]",
                surface_claim=f"SBOM declares component {n}",
                substrate_actual="binary embedded package list does not contain",
                witness=f"SBOM component {n} not present in binary",
                layer_classification="BATIN",
            )
        )

    return ThreeWayProjectionResult(
        findings=tuple(findings),
        sbom_components=tuple(sorted(sbom_names)),
        source_packages=tuple(sorted(source_names)),
        binary_packages=tuple(sorted(binary_names)),
    )

---

# Bismillah ir-Rahman ir-Rahim
