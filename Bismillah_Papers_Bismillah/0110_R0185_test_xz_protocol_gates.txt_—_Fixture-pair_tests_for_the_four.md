# Bismillah ir-Rahman ir-Rahim

# R0185 -- test_xz_protocol_gates.txt — Fixture-pair tests for the four XZ Protocol gates.

**Chronological Index:** 110 of 995  
**Date:** 2026-01-01  
**Section:** IV. XZ Protocol  
**Source File:** test_xz_protocol_gates.txt  
**Source Format:** txt  
**SHA-256:** `0419ca742e47900d92b56a22c2635a3ed12044cac90034210466d1d60fd9cf31`  

---

## R0185 · test_xz_protocol_gates.txt — Fixture-pair tests for the four XZ Protocol gates.

- section: IV. XZ Protocol
- source_file: test_xz_protocol_gates.txt
- source_format: txt
- text_sha256: 0419ca742e47900d92b56a22c2635a3ed12044cac90034210466d1d60fd9cf31

"""Fixture-pair tests for the four XZ Protocol gates.

Absorbs F-XZ12-OP-01. The v0.12 gates shipped with no fixtures at all,
and two of them could not have failed on any input: one searched for a
string absent from the document, the other searched for the corrected
form of a defect rather than the defective form, so green meant unfixed.

Every gate here is tested in both directions. A known-good fixture (the
shipped package, unmodified) must produce exit 0, and one known-bad
fixture per defect class must produce exit 1. This is the discipline
already applied to the kernel, where 243 exhaustive vectors pin every
decision state; it was never applied to the gates.

Run inside the canonical invocation, so a gate that stops discriminating
fails the same build that ships it.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from contextlib import contextmanager

import pytest

ROOT = os.path.dirname(os.path.abspath(__file__))

# Declared to xz_protocol_prohibited_content_verifier.py: this file carries
# prohibited strings as deliberate test inputs, not as claims.
PROHIBITED_CONTENT_FIXTURES = True

VERSION_GATE = "xz_protocol_version_gate.py"
CLOSURE_GATE = "xz_protocol_closure_gate.py"
MANIFEST_GATE = "xz_protocol_manifest_gate.py"
CONTENT_GATE = "xz_protocol_prohibited_content_verifier.py"
HISTORY_GATE = "xz_protocol_history_gate.py"

ALL_GATES = [VERSION_GATE, CLOSURE_GATE, MANIFEST_GATE, CONTENT_GATE, HISTORY_GATE]

PROTOCOL = "xz_protocol_v0_13.md"

# Stale stamps are assembled from parts so this fixture file carries no literal
# version token of its own; otherwise the version gate would flag its own tests.
STAMP = "XZ Protocol " + "v"
CURRENT = STAMP + "0.13"
STALE = STAMP + "0.3"


def run(root: str, gate: str, *args: str) -> int:
    return subprocess.call(
        [sys.executable, os.path.join(root, gate), *args],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


@contextmanager
def sandbox():
    with tempfile.TemporaryDirectory() as tmp:
        work = os.path.join(tmp, "pkg")
        shutil.copytree(ROOT, work, ignore=shutil.ignore_patterns(
            "__pycache__", ".pytest_cache"))
        yield work


def edit(root: str, name: str, old: str, new: str) -> None:
    path = os.path.join(root, name)
    text = open(path, encoding="utf-8").read()
    assert text.count(old) >= 1, f"fixture anchor not found in {name}: {old[:60]!r}"
    open(path, "w", encoding="utf-8").write(text.replace(old, new, 1))


# --- known-good direction -----------------------------------------------------

@pytest.mark.parametrize("gate", ALL_GATES)
def test_gate_passes_on_shipped_bytes(gate):
    assert run(ROOT, gate) == 0, f"{gate} does not pass on the shipped package"


def test_version_gate_self_test():
    assert run(ROOT, VERSION_GATE, "--self-test") == 0


# --- known-bad direction: version gate ---------------------------------------

def test_version_gate_fires_on_stale_module_stamp():
    with sandbox() as work:
        edit(work, "xz_protocol_kernel.py", CURRENT, STALE)
        assert run(work, VERSION_GATE) == 1


def test_version_gate_fires_on_stale_test_suite_stamp():
    with sandbox() as work:
        path = os.path.join(work, "test_xz_protocol_kernel.py")
        body = open(path, encoding="utf-8").read()
        open(path, "w", encoding="utf-8").write(
            "# " + STAMP + "0.4\n" + body)
        assert run(work, VERSION_GATE) == 1


def test_version_gate_fires_on_stale_gate_stamp():
    with sandbox() as work:
        path = os.path.join(work, MANIFEST_GATE)
        body = open(path, encoding="utf-8").read()
        open(path, "w", encoding="utf-8").write(
            "# " + STAMP + "0.2\n" + body)
        assert run(work, VERSION_GATE) == 1


def test_version_gate_rejects_proximity_style_exemption():
    """A historical marker beside a stale stamp must not excuse it.

    The v0.12 gate excused any mismatch within 100 characters of a marker
    such as 'RESOLVED in v0.'. That exemption path was controllable by the
    artifact under test, which is the escape-hatch shape this program has
    closed four times upstream.
    """
    with sandbox() as work:
        edit(work, "xz_protocol_source_frame.py",
             CURRENT, "RESOLVED in v0.3 -- " + STALE)
        assert run(work, VERSION_GATE) == 1


def test_version_gate_fires_when_trust_roots_disagree():
    with sandbox() as work:
        edit(work, "xz_protocol_trust_roots_PUBLIC.json",
             '"' + CURRENT + '"', '"' + STAMP + '0.12"')
        assert run(work, VERSION_GATE) == 1


# --- known-bad direction: closure gate ---------------------------------------

def test_closure_gate_fires_when_a_closed_locus_regresses():
    """Reverting the SHUDP deduplication must fail the gate.

    The v0.12 predecessor searched for the corrected string, so it passed
    on exactly this state.
    """
    with sandbox() as work:
        edit(work, PROTOCOL,
             "| Is Evidence Independence an Axiom? Decomposing a Proposed Extension to AX-SH ",
             "| Is Evidence Independence an Axiom? (SHUDP v0.5) | placeholder ")
        assert run(work, CLOSURE_GATE) == 1


def test_closure_gate_fires_on_unregistered_closure_claim():
    with sandbox() as work:
        path = os.path.join(work, PROTOCOL)
        text = open(path, encoding="utf-8").read()
        open(path, "w", encoding="utf-8").write(
            text + "\n- **v9.9 (2026-01-01): fabricated.** F-XX-99 CLOSED: nothing.\n")
        assert run(work, CLOSURE_GATE) == 1


def test_closure_gate_is_not_satisfied_by_the_amendment_record_itself():
    """A closure claim must be provable in the body, not in the log asserting it."""
    with sandbox() as work:
        edit(work, PROTOCOL,
             "21539074 and 21539816 are two version DOIs under one concept DOI",
             "PLACEHOLDER removed from body")
        assert run(work, CLOSURE_GATE) == 1


def test_closure_gate_fires_when_register_is_absent():
    with sandbox() as work:
        os.remove(os.path.join(work, "xz_protocol_locus_register.json"))
        assert run(work, CLOSURE_GATE) == 1


# --- known-bad direction: manifest gate --------------------------------------

def test_manifest_gate_fires_on_modified_module():
    with sandbox() as work:
        path = os.path.join(work, "xz_protocol_condition_a.py")
        open(path, "a", encoding="utf-8").write("\n# drift\n")
        assert run(work, MANIFEST_GATE) == 1


def test_manifest_gate_fires_on_modified_gate():
    """The v0.12 predecessor hardcoded twelve files and could not see this."""
    with sandbox() as work:
        path = os.path.join(work, VERSION_GATE)
        open(path, "a", encoding="utf-8").write("\n# drift\n")
        assert run(work, MANIFEST_GATE) == 1


def test_manifest_gate_fires_on_unresolvable_digest_in_body():
    with sandbox() as work:
        path = os.path.join(work, PROTOCOL)
        text = open(path, encoding="utf-8").read()
        cut = text.index("## 27. Amendment record")
        open(path, "w", encoding="utf-8").write(
            text[:cut] + "\nStray digest " + "0" * 64 + "\n" + text[cut:])
        assert run(work, MANIFEST_GATE) == 1


# --- known-bad direction: prohibited-content verifier ------------------------

def test_content_gate_fires_on_effectiveness_claim():
    with sandbox() as work:
        path = os.path.join(work, PROTOCOL)
        text = open(path, encoding="utf-8").read()
        open(path, "w", encoding="utf-8").write(
            text + "\nBSSG reduces supply-chain risk.\n")
        assert run(work, CONTENT_GATE) == 1


def test_content_gate_fires_on_outcome_modal():
    with sandbox() as work:
        path = os.path.join(work, PROTOCOL)
        text = open(path, encoding="utf-8").read()
        open(path, "w", encoding="utf-8").write(
            text + "\nThe kernel would have denied the release.\n")
        assert run(work, CONTENT_GATE) == 1


def test_content_gate_fires_on_non_permitted_citation():
    with sandbox() as work:
        path = os.path.join(work, PROTOCOL)
        text = open(path, encoding="utf-8").read()
        open(path, "w", encoding="utf-8").write(
            text + "\nSee https://example.com/xz-writeup for detail.\n")
        assert run(work, CONTENT_GATE) == 1


def test_content_gate_fires_when_a_declared_exemption_disappears():
    """The exemption list is asserted in both directions so it cannot rot."""
    with sandbox() as work:
        edit(work, PROTOCOL,
             "It is not an estimate of attack prevention",
             "It is not an estimate of prevention")
        assert run(work, CONTENT_GATE) == 1


# --- known-bad direction: history gate ---------------------------------------

def test_history_gate_fires_on_mutated_historical_entry():
    """The v0.4, v0.9 and v0.11 in-place mutations would each fail here."""
    with sandbox() as work:
        edit(work, PROTOCOL,
             "94353b3cadc5134eea971f8a11b13f5379cc7e0472946f314e9544d9f908deea",
             "0" * 64)
        assert run(work, HISTORY_GATE) == 1


def test_history_gate_fires_on_unsealed_appended_entry():
    with sandbox() as work:
        path = os.path.join(work, PROTOCOL)
        text = open(path, encoding="utf-8").read()
        open(path, "w", encoding="utf-8").write(
            text + "\n- **v0.14 (2026-09-09): unsealed.** Status: DRAFT CANDIDATE.\n")
        assert run(work, HISTORY_GATE) == 1


def test_history_gate_fires_on_removed_entry():
    with sandbox() as work:
        path = os.path.join(work, "HISTORY.sha256")
        lines = open(path, encoding="utf-8").read().splitlines()
        open(path, "w", encoding="utf-8").write(
            "\n".join(lines + ["0" * 64 + "  0.99"]) + "\n")
        assert run(work, HISTORY_GATE) == 1

---

# Bismillah ir-Rahman ir-Rahim
