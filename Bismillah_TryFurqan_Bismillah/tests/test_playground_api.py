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
"""Unit tests for the playground backend.

Covers:
  - verdict classification across exit codes
  - share id generation and validation
  - request schema enforcement (size cap, missing fields)
  - share storage round-trip (in a tmp DB)
  - share TTL expiration

These are pure-Python tests that do NOT exec furqan-lint; the
end-to-end fixture-baseline tests (test_fixture_baselines.py) cover
that path. Splitting keeps the unit tests fast and CI-portable
even on machines without furqan-lint installed.
"""
from __future__ import annotations

import json
import os
import time

import pytest


@pytest.fixture(autouse=True)
def isolated_share_db(tmp_path, monkeypatch):
    """Point the share DB at a per-test sqlite file.

    The module reads TRYFURQAN_SHARE_DB at import time, so we set the
    env var before importing playground and force a re-import.
    """
    db_path = tmp_path / "shares.db"
    monkeypatch.setenv("TRYFURQAN_SHARE_DB", str(db_path))
    import importlib
    import playground as pg
    importlib.reload(pg)
    yield pg


def test_classify_pass(isolated_share_db):
    pg = isolated_share_db
    assert pg._classify(0, "PASS  module.py\n") == ("pass", "PASS")


def test_classify_advisory(isolated_share_db):
    pg = isolated_share_db
    assert pg._classify(0, "ADVISORY  module.py\n  ...") == ("advisory", "ADVISORY")


def test_classify_marad(isolated_share_db):
    pg = isolated_share_db
    assert pg._classify(1, "MARAD  module.py\n") == ("marad", "MARAD")


def test_classify_parse_error(isolated_share_db):
    pg = isolated_share_db
    assert pg._classify(2, "PARSE ERROR ...") == ("parse_error", "PARSE ERROR")


def test_classify_unknown(isolated_share_db):
    pg = isolated_share_db
    assert pg._classify(99, "weird") == ("internal_error", "INTERNAL ERROR")


def test_share_id_format(isolated_share_db):
    pg = isolated_share_db
    sid = pg._gen_share_id()
    assert pg._is_valid_share_id(sid)
    assert len(sid) == 12
    assert pg._is_valid_share_id("a" * 12)
    assert not pg._is_valid_share_id("short")
    assert not pg._is_valid_share_id("a" * 13)
    assert not pg._is_valid_share_id("contains space")
    assert not pg._is_valid_share_id("has/slash1234")
    assert not pg._is_valid_share_id(None)  # type: ignore[arg-type]


def test_share_round_trip_check(isolated_share_db):
    pg = isolated_share_db
    payload = {
        "mode": "check",
        "language": "python",
        "source": "def f() -> int: return 1\n",
    }
    sid = pg._put_share(payload)
    assert pg._is_valid_share_id(sid)
    got = pg._get_share(sid)
    assert got == payload


def test_share_round_trip_diff(isolated_share_db):
    pg = isolated_share_db
    payload = {
        "mode": "diff",
        "language": "rust",
        "old_source": "pub fn a() {}\n",
        "new_source": "pub fn a() {}\npub fn b() {}\n",
    }
    sid = pg._put_share(payload)
    got = pg._get_share(sid)
    assert got == payload


def test_share_missing_returns_none(isolated_share_db):
    pg = isolated_share_db
    assert pg._get_share("nosuchxxxxxx") is None


def test_share_invalid_id_returns_none(isolated_share_db):
    pg = isolated_share_db
    assert pg._get_share("/etc/passwd") is None
    assert pg._get_share("") is None


def test_share_ttl_sweep(isolated_share_db, monkeypatch):
    """Inserts a row with a stale created_at, then writes another row;
    the lazy sweep on write should remove the stale row."""
    pg = isolated_share_db
    payload = {"mode": "check", "language": "python", "source": "x = 1\n"}
    sid = pg._put_share(payload)
    assert pg._get_share(sid) is not None

    # Manually backdate it past TTL.
    import sqlite3
    conn = sqlite3.connect(str(pg._SHARE_DB_PATH))
    stale = int(time.time()) - pg._SHARE_TTL_S - 60
    conn.execute("UPDATE share SET created_at = ? WHERE id = ?", (stale, sid))
    conn.commit()
    conn.close()

    # Trigger the sweep by writing another share.
    other = pg._put_share({"mode": "check", "language": "go", "source": "package main\n"})
    assert pg._get_share(other) is not None
    assert pg._get_share(sid) is None  # swept


def test_share_payload_size_cap(isolated_share_db):
    pg = isolated_share_db
    huge = "x" * (pg._MAX_SOURCE_BYTES + 1)
    from pydantic import ValidationError
    with pytest.raises(ValidationError):
        pg.SharePayload(mode="check", language="python", source=huge)


def test_check_request_rejects_bad_language(isolated_share_db):
    pg = isolated_share_db
    from pydantic import ValidationError
    with pytest.raises(ValidationError):
        pg.CheckRequest(language="java", source="x")  # type: ignore[arg-type]


def test_check_request_rejects_empty_source(isolated_share_db):
    pg = isolated_share_db
    from pydantic import ValidationError
    with pytest.raises(ValidationError):
        pg.CheckRequest(language="python", source="")


def test_diff_request_rejects_empty(isolated_share_db):
    pg = isolated_share_db
    from pydantic import ValidationError
    with pytest.raises(ValidationError):
        pg.DiffRequest(language="python", old_source="", new_source="x")


def test_run_check_too_large_envelope(isolated_share_db):
    pg = isolated_share_db
    huge = "x = 1\n" * 30000  # ~180 KiB
    result = pg._run_check(huge, "python")
    assert result["verdict"] == "internal_error"
    assert result["verdict_label"] == "INPUT TOO LARGE"


def test_run_check_unsupported_language(isolated_share_db):
    pg = isolated_share_db
    result = pg._run_check("x = 1", "ruby")  # type: ignore[arg-type]
    assert result["verdict"] == "internal_error"
    assert "unsupported language" in result["error"]


def test_run_check_rejects_non_string_source(isolated_share_db):
    pg = isolated_share_db
    result = pg._run_check(None, "python")  # type: ignore[arg-type]
    assert result["verdict"] == "internal_error"

# Bismillah ir-Rahman ir-Rahim