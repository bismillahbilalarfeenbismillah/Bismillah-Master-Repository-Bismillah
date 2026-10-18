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
"""Sync gate: every fixture id used in playground.js must exist in
tests/fixtures.py and the v0.8.5 baseline. Drift fails CI.

We do not parse the JS file; we just grep for the `id:` keys with a
simple regex. The regex is intentionally narrow to avoid matching
unrelated `id:` text.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

from tests.fixtures import CHECK_FIXTURES, DIFF_FIXTURES

_HERE = Path(__file__).resolve().parent
_REPO = _HERE.parent
_PG_JS = _REPO / "static" / "playground.js"
_BASELINE = _HERE / "baselines" / "furqan_lint_v0_8_5.json"

_ID_PATTERN = re.compile(r"id:\s*'([a-z0-9-]+)'")


def _ids_in_js() -> set[str]:
    text = _PG_JS.read_text(encoding="utf-8")
    return set(_ID_PATTERN.findall(text))


def _ids_in_python_check() -> set[str]:
    return {fid for m in CHECK_FIXTURES.values() for fid in m}


def _ids_in_python_diff() -> set[str]:
    return {fid for m in DIFF_FIXTURES.values() for fid in m}


def _ids_in_baseline() -> set[str]:
    data = json.loads(_BASELINE.read_text(encoding="utf-8"))
    out: set[str] = set()
    for lang_map in data["fixtures"]["check"].values():
        out.update(lang_map.keys())
    for lang_map in data["fixtures"]["diff"].values():
        out.update(lang_map.keys())
    return out


def test_js_ids_match_python_fixtures() -> None:
    js_ids = _ids_in_js()
    py_ids = _ids_in_python_check() | _ids_in_python_diff()
    missing_in_py = js_ids - py_ids
    missing_in_js = py_ids - js_ids
    assert not missing_in_py, (
        f"playground.js declares fixture ids absent from "
        f"tests/fixtures.py: {sorted(missing_in_py)}"
    )
    assert not missing_in_js, (
        f"tests/fixtures.py declares fixture ids absent from "
        f"playground.js: {sorted(missing_in_js)}"
    )


def test_baseline_covers_every_python_fixture() -> None:
    py_ids = _ids_in_python_check() | _ids_in_python_diff()
    base_ids = _ids_in_baseline()
    missing = py_ids - base_ids
    assert not missing, (
        f"v0.8.5 baseline missing fixture ids: {sorted(missing)}"
    )

# Bismillah ir-Rahman ir-Rahim