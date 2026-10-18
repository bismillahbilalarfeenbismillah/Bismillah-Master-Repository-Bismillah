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
"""Record verbatim /scan responses for the three landing-mock-v2 fixtures.

Output: docs/landing-mock-v2/fixtures.json
Usage:  python scripts/record_landing_fixtures.py
"""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import pikepdf  # noqa: E402
from bayyinah import __version__ as _BAYYINAH_VERSION  # noqa: E402
from bayyinah import scan_file  # noqa: E402


def make_encrypted(src: Path, dst: Path) -> None:
    """Encrypt a copy of src with a non-empty user password.

    A non-empty user password makes the content unreadable without the
    key, which is the condition Bayyinah's encrypted-PDF flow is meant
    to demonstrate.
    """
    with pikepdf.open(src) as pdf:
        pdf.save(
            dst,
            encryption=pikepdf.Encryption(
                owner="bayyinah-demo-owner",
                user="bayyinah-demo-user",
                R=4,
            ),
        )


def record(label: str, fixture_path: Path) -> dict:
    print(f"  scanning {label}: {fixture_path.name}")
    report = scan_file(str(fixture_path))
    payload = report.to_dict()
    payload["file_path"] = fixture_path.name
    # Add scanner_version so a curious reader can distinguish the
    # report-schema version (`version`, currently 0.1.0) from the
    # scanner package version that produced the report.
    payload["scanner_version"] = _BAYYINAH_VERSION
    return payload


def main() -> None:
    out_dir = ROOT / "docs" / "landing-mock-v2"
    out_dir.mkdir(parents=True, exist_ok=True)

    clean_pdf = ROOT / "tests" / "fixtures" / "clean.pdf"
    adversarial_pdf = ROOT / "tests" / "fixtures" / "positive_combined.pdf"

    with tempfile.TemporaryDirectory() as tmp:
        encrypted_path = Path(tmp) / "encrypted_demo.pdf"
        make_encrypted(clean_pdf, encrypted_path)

        recorded = {
            "clean": record("clean", clean_pdf),
            "adversarial": record("adversarial", adversarial_pdf),
            "encrypted": record("encrypted", encrypted_path),
        }

    out_path = out_dir / "fixtures.json"
    out_path.write_text(json.dumps(recorded, indent=2))
    print(f"\nwrote {out_path.relative_to(ROOT)}")
    for k, v in recorded.items():
        score = v.get("integrity_score", "?")
        n = len(v.get("findings", []))
        verdict = v.get("verdict", "?")
        print(f"  {k}: verdict={verdict} score={score} findings={n}")


if __name__ == "__main__":
    main()

# Bismillah ir-Rahman ir-Rahim