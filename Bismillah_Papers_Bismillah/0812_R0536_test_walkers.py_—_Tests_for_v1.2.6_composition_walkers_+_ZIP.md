# Bismillah ir-Rahman ir-Rahim

# R0536 -- test_walkers.py — Tests for v1.2.6 composition walkers + ZIP-bomb defense."""

**Chronological Index:** 812 of 995  
**Date:** Undated  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** test_walkers.py  
**Source Format:** py  
**SHA-256:** `e83412c69771ab16d7057df317e82a1f133b5656a004e213c5fd5c1a731e36e6`  

---

## R0536 · test_walkers.py — Tests for v1.2.6 composition walkers + ZIP-bomb defense."""

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: test_walkers.py
- source_format: py
- text_sha256: e83412c69771ab16d7057df317e82a1f133b5656a004e213c5fd5c1a731e36e6

"""Tests for v1.2.6 composition walkers + ZIP-bomb defense."""

from __future__ import annotations

import io
import json
import zipfile

from bayyinah.walkers import (
    SafetyLimits,
    ZipBombDetected,
    compose_scan,
    detect_kind,
    evaluate_zip_safety,
)


def _build_zip(members: dict) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in members.items():
            z.writestr(name, data)
    return buf.getvalue()


def test_detect_kind_zip():
    data = _build_zip({"a.txt": b"hi"})
    assert detect_kind(data).value == "ZIP"


def test_detect_kind_oci_manifest():
    manifest = json.dumps(
        {"schemaVersion": 2, "layers": []}, indent=2
    ).encode("utf-8")
    assert detect_kind(manifest).value == "OCI"


def test_detect_kind_none_for_leaf():
    assert detect_kind(b"alpha,beta\n1,2\n") is None


def test_compose_scan_single_zip_emits_composition_path():
    csv_bytes = b"alpha,beta,gamma,delta\r\n1,2,3\r\n"  # mismatch → BYN-CSV-001
    zip_bytes = _build_zip({"inner.csv": csv_bytes})
    findings = compose_scan(zip_bytes, outer_path="outer.zip")
    csv_findings = [f for f in findings if f.code.startswith("BYN-CSV")]
    assert csv_findings, "expected CSV finding to bubble up through composition"
    assert csv_findings[0].composition_path == "outer.zip!inner.csv"


def test_compose_scan_nested_zip_preserves_full_composition_path():
    csv_bytes = b'name,description\r\nfoo,"open\r\n'  # BYN-CSV-005
    inner_zip = _build_zip({"buried.csv": csv_bytes})
    outer_zip = _build_zip({"middle.zip": inner_zip})

    findings = compose_scan(outer_zip, outer_path="outer.zip")
    csv5 = [f for f in findings if f.code == "BYN-CSV-005"]
    assert csv5, [f.code for f in findings]
    assert csv5[0].composition_path == "outer.zip!middle.zip!buried.csv"


def test_zip_bomb_defense_rejects_high_ratio():
    payload = b"\x00" * (8 * 1024 * 1024)
    zip_bytes = _build_zip({"bomb.bin": payload})
    findings = compose_scan(zip_bytes, outer_path="bomb.zip")
    assert any(
        f.code == "BYN-ZIP-901" and f.severity.value == "BLOCKER"
        for f in findings
    ), [f.code for f in findings]


def test_zip_bomb_defense_rejects_file_count_explosion():
    members = {f"f_{i:05d}.txt": b"" for i in range(10_500)}
    zip_bytes = _build_zip(members)
    findings = compose_scan(zip_bytes, outer_path="fcount.zip")
    assert any(f.code == "BYN-ZIP-901" for f in findings)


def test_evaluate_zip_safety_rejects_corrupt_header():
    import pytest

    with pytest.raises(ZipBombDetected):
        evaluate_zip_safety(b"PK\x03\x04bad", SafetyLimits())


def test_compose_scan_max_depth_enforced():
    inner = _build_zip({"leaf.csv": b"a,b\n1,2\n"})
    nested = _build_zip({"d1.zip": inner})
    nested = _build_zip({"d2.zip": nested})
    nested = _build_zip({"d3.zip": nested})
    findings = compose_scan(
        nested,
        outer_path="d4.zip",
        limits=SafetyLimits(max_depth=2),  # too shallow on purpose
    )
    assert any(
        f.code == "BYN-ZIP-901" and "depth" in f.substrate_actual
        for f in findings
    ), [f.code for f in findings]


def test_oci_manifest_walked_as_descriptors():
    manifest = json.dumps(
        {
            "schemaVersion": 2,
            "mediaType": "application/vnd.oci.image.manifest.v1+json",
            "layers": [
                {
                    "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",
                    "digest": "sha256:abc",
                    "size": 100,
                },
                {
                    "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",
                    "digest": "sha256:def",
                    "size": 200,
                },
            ],
        }
    ).encode("utf-8")
    # OCI walker produces descriptor JSON for each layer; descriptors don't have
    # a .json extension so no per-extension dispatch fires. We assert that the
    # walker runs cleanly without crashing.
    findings = compose_scan(manifest, outer_path="manifest.json")
    # No findings expected on a clean manifest with well-formed descriptors
    assert all(f.code != "BYN-ZIP-901" for f in findings)

---

# Bismillah ir-Rahman ir-Rahim
