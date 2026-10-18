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
"""Post-fix verdict tests for the Round 12 corpus.

Each fixture's post_fix_v1_2_4 expectation is asserted. Passes
on v1.2.4 with the closure commits applied; fails on v1.2.3
(by design, that is the calibration gap Round 12 closes).
"""
from __future__ import annotations
import json
from pathlib import Path
import pytest
from bayyinah import scan_pdf

CORPUS_DIR = Path(__file__).parent
EXPECTED = json.loads((CORPUS_DIR / "EXPECTED.json").read_text())


@pytest.mark.parametrize("fixture_name", sorted(EXPECTED.keys()))
def test_post_fix_verdict(fixture_name: str) -> None:
    fixture = CORPUS_DIR / fixture_name
    if not fixture.exists():
        pytest.skip(f"{fixture_name} not regenerated; run builders")
    expected = EXPECTED[fixture_name]["post_fix_v1_2_4"]

    rd = scan_pdf(fixture).to_dict()
    fires = sorted({f.get('mechanism') for f in rd.get('findings', [])})

    assert rd.get('integrity_score') == expected["integrity_score"], (
        f"{fixture_name}: expected score {expected['integrity_score']}, "
        f"got {rd.get('integrity_score')}; fires={fires}"
    )
    assert fires == expected["fires"], (
        f"{fixture_name}: expected fires {expected['fires']}, got {fires}"
    )


def test_corpus_round_trip_byte_stable_on_pdftex_fixtures() -> None:
    """The pdfTeX builders are byte-stable across consecutive runs.

    Determinism is the v3 §12.1 pre-flight item: a non-deterministic
    fixture means future regen produces a different sha256, breaking
    EXPECTED.json's promise. SOURCE_DATE_EPOCH=0 strips the build
    timestamp.
    """
    import hashlib
    import subprocess
    targets = [
        ("build_clean_pdftex_article.py", "fixture_clean_pdftex_article.pdf"),
        ("build_clean_pdftex_with_hyperref.py", "fixture_clean_pdftex_with_hyperref.pdf"),
    ]
    for builder, output in targets:
        out_path = CORPUS_DIR / output
        if not out_path.exists():
            pytest.skip(f"{output} not present; run builder")
        sha_first = hashlib.sha256(out_path.read_bytes()).hexdigest()
        # Re-run builder
        result = subprocess.run(
            ["python3", str(CORPUS_DIR / builder)],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            pytest.skip(f"builder failed (likely missing pdflatex): {result.stderr}")
        sha_second = hashlib.sha256(out_path.read_bytes()).hexdigest()
        assert sha_first == sha_second, (
            f"{output} not byte-stable across runs: {sha_first} != {sha_second}"
        )

# Bismillah ir-Rahman ir-Rahim