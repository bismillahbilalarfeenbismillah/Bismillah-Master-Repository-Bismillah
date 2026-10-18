# Bismillah ir-Rahman ir-Rahim
# 
# Al-Asma ul-Husna -- The 99 Beautiful Names of Allah
#   Allah -- The God
#   Ar-Rahman -- The Most Merciful
#   Ar-Rahim -- The Most Compassionate
#   Al-Malik -- The King
#   Al-Quddus -- The Most Holy
#   As-Salam -- The Source of Peace
#   Al-Mu'min -- The Guardian of Faith
#   Al-Muhaymin -- The Protector
#   Al-Aziz -- The Almighty
#   Al-Jabbar -- The Compeller
#   Al-Mutakabbir -- The Supreme
#   Al-Khaliq -- The Creator
#   Al-Bari -- The Evolver
#   Al-Musawwir -- The Fashioner
#   Al-Ghaffar -- The Forgiver
#   Al-Qahhar -- The Subduer
#   Al-Wahhab -- The Bestower
#   Ar-Razzaq -- The Provider
#   Al-Fattah -- The Opener
#   Al-Alim -- The All-Knowing
#   Al-Qabid -- The Restrainer
#   Al-Basit -- The Expander
#   Al-Khafid -- The Abaser
#   Ar-Rafi -- The Exalter
#   Al-Mu'izz -- The Bestower of Honor
#   Al-Mudhill -- The Humiliator
#   As-Sami -- The All-Hearing
#   Al-Basir -- The All-Seeing
#   Al-Hakam -- The Judge
#   Al-Adl -- The Just
#   Al-Latif -- The Subtle One
#   Al-Khabir -- The All-Aware
#   Al-Halim -- The Forbearing
#   Al-Azim -- The Magnificent
#   Al-Ghafur -- The All-Forgiving
#   Ash-Shakur -- The Appreciative
#   Al-Ali -- The Most High
#   Al-Kabir -- The Most Great
#   Al-Hafiz -- The Preserver
#   Al-Muqit -- The Sustainer
#   Al-Hasib -- The Reckoner
#   Al-Jalil -- The Majestic
#   Al-Karim -- The Generous
#   Ar-Raqib -- The Watchful
#   Al-Mujib -- The Responsive
#   Al-Wasi -- The All-Encompassing
#   Al-Hakim -- The Perfectly Wise
#   Al-Wadud -- The Loving One
#   Al-Majid -- The Most Glorious
#   Al-Ba'ith -- The Resurrector
#   Ash-Shahid -- The Witness
#   Al-Haqq -- The Truth
#   Al-Wakil -- The Trustee
#   Al-Qawiyy -- The Most Strong
#   Al-Matin -- The Firm One
#   Al-Waliyy -- The Protector
#   Al-Hamid -- The Praiseworthy
#   Al-Muhsi -- The Accounter
#   Al-Mubdi -- The Originator
#   Al-Mu'id -- The Restorer
#   Al-Muhyi -- The Giver of Life
#   Al-Mumit -- The Creator of Death
#   Al-Hayy -- The Ever Living
#   Al-Qayyum -- The Self-Subsisting
#   Al-Wajid -- The Finder
#   Al-Majid -- The Noble
#   Al-Wahid -- The Unique
#   Al-Ahad -- The One
#   As-Samad -- The Eternal
#   Al-Qadir -- The Able
#   Al-Muqtadir -- The Powerful
#   Al-Muqaddim -- The Expediter
#   Al-Mu'akhkhir -- The Delayer
#   Al-Awwal -- The First
#   Al-Akhir -- The Last
#   Az-Zahir -- The Manifest
#   Al-Batin -- The Hidden
#   Al-Wali -- The Governor
#   Al-Muta'ali -- The Most Exalted
#   Al-Barr -- The Source of Goodness
#   At-Tawwab -- The Acceptor of Repentance
#   Al-Muntaqim -- The Avenger
#   Al-Afuww -- The Pardoner
#   Ar-Ra'uf -- The Most Kind
#   Malik-ul-Mulk -- Owner of Sovereignty
#   Dhul-Jalali wal-Ikram -- Lord of Majesty and Generosity
#   Al-Muqsit -- The Equitable
#   Al-Jami -- The Gatherer
#   Al-Ghaniyy -- The Self-Sufficient
#   Al-Mughni -- The Enricher
#   Al-Mani -- The Preventer
#   Ad-Darr -- The Distresser
#   An-Nafi -- The Propitious
#   An-Nur -- The Light
#   Al-Hadi -- The Guide
#   Al-Badi -- The Originator
#   Al-Baqi -- The Everlasting
#   Al-Warith -- The Inheritor
#   Ar-Rashid -- The Guide to the Right Path
#   As-Sabur -- The Patient
# 
"""Tests for the v1.1.9 demo route (bayyinah/demo.py).

All tests live behind the BAYYINAH_DEMO_ENABLED env flag so they
mirror the deployment shape: production /scan path is unaffected
when the demo is off; the demo only loads when the flag is set.

The Anthropic API call is mocked via httpx.MockTransport so the
suite runs deterministically and without network access.
"""
from __future__ import annotations

import importlib
import json
import os
from pathlib import Path

import httpx
import pytest
from fastapi.testclient import TestClient


CLEAN_PDF = Path("tests/fixtures/clean.pdf")
ADVERSARIAL_PDF = Path("tests/fixtures/positive_combined.pdf")


def _build_app_with_flag_on(monkeypatch, mock_anthropic_handler=None):
    """Reload api with BAYYINAH_DEMO_ENABLED=1.

    If ``mock_anthropic_handler`` is provided, patch the AsyncClient
    used in bayyinah.demo so any outbound httpx call routes to the
    mock instead of the real Anthropic API.
    """
    monkeypatch.setenv("BAYYINAH_DEMO_ENABLED", "1")
    import bayyinah.summary_queue as summary_queue
    importlib.reload(summary_queue)
    import bayyinah.summary_worker as summary_worker
    importlib.reload(summary_worker)
    import bayyinah.demo as demo_module
    importlib.reload(demo_module)
    import api as api_module
    importlib.reload(api_module)
    # Lifespan runs only when TestClient is used as a context manager;
    # the v1.1.9 helper uses bare TestClient(app), so initialise the
    # v1.2.2 summary queue schema explicitly here.
    summary_queue.init_db()

    if mock_anthropic_handler is not None:
        # Patch httpx.AsyncClient inside the demo module so requests
        # route through MockTransport without touching the network.
        original_async_client = httpx.AsyncClient

        class _PatchedAsyncClient(original_async_client):
            def __init__(self, *args, **kwargs):
                kwargs["transport"] = httpx.MockTransport(
                    mock_anthropic_handler
                )
                super().__init__(*args, **kwargs)

        monkeypatch.setattr(demo_module.httpx, "AsyncClient", _PatchedAsyncClient)

    return api_module.app


def _mock_anthropic_ok(_request: httpx.Request) -> httpx.Response:
    return httpx.Response(
        200,
        json={
            "content": [{"type": "text", "text": "Mocked summary."}],
            "usage": {"input_tokens": 287, "output_tokens": 12},
        },
    )


# ---------------------------------------------------------------------------
# 1. /demo returns 200 and serves HTML when env flag is on.
# ---------------------------------------------------------------------------
def test_demo_route_serves_html_when_flag_on(monkeypatch):
    app = _build_app_with_flag_on(monkeypatch)
    client = TestClient(app)
    r = client.get("/demo")
    assert r.status_code == 200
    assert "text/html" in r.headers.get("content-type", "")
    assert "Bayyinah Demo" in r.text


# ---------------------------------------------------------------------------
# 2. /demo/summarize returns 413 on oversize upload.
# ---------------------------------------------------------------------------
def test_demo_summarize_returns_413_on_oversize(monkeypatch):
    app = _build_app_with_flag_on(monkeypatch)
    client = TestClient(app)
    # 26 MiB of zeros, one byte over the demo cap.
    big_bytes = b"\x00" * (25 * 1024 * 1024 + 1)
    r = client.post(
        "/demo/summarize",
        files={"file": ("big.pdf", big_bytes, "application/pdf")},
    )
    assert r.status_code == 413


# ---------------------------------------------------------------------------
# 3. /demo/summarize returns 400 on empty upload.
# ---------------------------------------------------------------------------
def test_demo_summarize_returns_400_on_empty(monkeypatch):
    app = _build_app_with_flag_on(monkeypatch)
    client = TestClient(app)
    r = client.post(
        "/demo/summarize",
        files={"file": ("empty.pdf", b"", "application/pdf")},
    )
    assert r.status_code == 400


# ---------------------------------------------------------------------------
# 4. /demo/summarize blocks an adversarial fixture.
# ---------------------------------------------------------------------------
def test_demo_summarize_blocks_adversarial_fixture(monkeypatch):
    app = _build_app_with_flag_on(monkeypatch, _mock_anthropic_ok)
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")
    client = TestClient(app)
    contents = ADVERSARIAL_PDF.read_bytes()
    r = client.post(
        "/demo/summarize",
        files={"file": ("adversarial.pdf", contents, "application/pdf")},
    )
    assert r.status_code == 200
    payload = r.json()
    assert payload["blocked"] is True, f"expected blocked=True, got {payload}"
    assert payload["summary"] is None
    assert payload["llm_input_tokens"] == 0
    assert payload["block_reason"] in (
        "tier_1_finding",
        "verified_concealment",
        "high_confidence_tier_2",
    )


# ---------------------------------------------------------------------------
# 5. /demo/summarize passes a clean fixture and includes a summary.
# ---------------------------------------------------------------------------
def test_demo_summarize_passes_clean_with_summary(monkeypatch):
    """Clean PDFs enqueue (v1.2.2 contract; was synchronous in v1.1.9).

    The v1.1.9 shape returned ``summary`` in the synchronous response.
    v1.2.2 enqueues the work and returns ``summary_status: "queued"``
    with a ``summary_job_id``; the actual summary lands later via
    GET /demo/summary/{job_id} (covered by
    tests/test_demo_queue_endpoints.py and the worker tests). This
    test now asserts the new synchronous contract per the framework's
    "convert to the new shape" rule, not the retired one.
    """
    app = _build_app_with_flag_on(monkeypatch, _mock_anthropic_ok)
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")
    client = TestClient(app)
    contents = CLEAN_PDF.read_bytes()
    r = client.post(
        "/demo/summarize",
        files={"file": ("clean.pdf", contents, "application/pdf")},
    )
    assert r.status_code == 200
    payload = r.json()
    assert payload["blocked"] is False
    assert payload["summary"] is None  # v1.2.2: summary delivered async
    assert payload["summary_status"] == "queued"
    assert payload["summary_job_id"] is not None
    assert payload["scan"]["verdict"] == "sahih"


# ---------------------------------------------------------------------------
# 6. /demo/summarize returns anthropic_key_missing when API key unset.
# ---------------------------------------------------------------------------
def test_demo_summarize_no_api_key_returns_summary_error(monkeypatch):
    app = _build_app_with_flag_on(monkeypatch)
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    client = TestClient(app)
    contents = CLEAN_PDF.read_bytes()
    r = client.post(
        "/demo/summarize",
        files={"file": ("clean.pdf", contents, "application/pdf")},
    )
    assert r.status_code == 200
    payload = r.json()
    assert payload["blocked"] is False
    assert payload["summary"] is None
    assert payload["summary_error"] == "anthropic_key_missing"
    assert payload["llm_input_tokens"] == 0


# ---------------------------------------------------------------------------
# 7. _block_decision unit test covering all branches.
# ---------------------------------------------------------------------------
def test_block_decision_branches(monkeypatch):
    monkeypatch.setenv("BAYYINAH_DEMO_ENABLED", "1")
    import bayyinah.demo as demo_module
    importlib.reload(demo_module)
    bd = demo_module._block_decision

    # mughlaq blocks (verdict-level)
    assert bd({"verdict": "mughlaq", "findings": []}) == (
        True, "scan_incomplete_or_routing_dispute"
    )
    # munafiq blocks (verdict-level)
    assert bd({"verdict": "munafiq", "findings": []}) == (
        True, "verified_concealment"
    )
    # Tier 1 finding blocks regardless of verdict
    assert bd({
        "verdict": "sahih",
        "findings": [{"tier": 1, "confidence": 0.9}],
    }) == (True, "tier_1_finding")
    # Tier 2 high confidence blocks regardless of verdict
    assert bd({
        "verdict": "sahih",
        "findings": [{"tier": 2, "confidence": 0.8}],
    }) == (True, "high_confidence_tier_2")
    # Tier 2 low confidence does NOT block on its own
    assert bd({
        "verdict": "sahih",
        "findings": [{"tier": 2, "confidence": 0.5}],
    }) == (False, "clean_or_low_confidence")
    # mukhfi with no findings passes
    assert bd({"verdict": "mukhfi", "findings": []}) == (
        False, "clean_or_low_confidence"
    )
    # mushtabih with low-conf Tier 3 only passes
    assert bd({
        "verdict": "mushtabih",
        "findings": [{"tier": 3, "confidence": 0.4}],
    }) == (False, "clean_or_low_confidence")
    # sahih clean passes
    assert bd({"verdict": "sahih", "findings": []}) == (
        False, "clean_or_low_confidence"
    )


# ---------------------------------------------------------------------------
# 8. /demo route returns 404 when env flag is off.
# ---------------------------------------------------------------------------
def test_demo_route_not_mounted_when_flag_off(monkeypatch):
    monkeypatch.delenv("BAYYINAH_DEMO_ENABLED", raising=False)
    import api as api_module
    importlib.reload(api_module)
    client = TestClient(api_module.app)
    r = client.get("/demo")
    assert r.status_code == 404
    # And the production /scan endpoint is still reachable.
    r2 = client.get("/version")
    assert r2.status_code == 200
    assert r2.json().get("version")

# Bismillah ir-Rahman ir-Rahim