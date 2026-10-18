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
"""Structural enforcement of the requirements-dev.txt / [dev] sync.

The leading comment in requirements-dev.txt has long claimed equivalence
with the [project.optional-dependencies].dev table in pyproject.toml, but
no test enforced it. The two surfaces drifted by four entries between
v1.1.x and v1.2.2. This test parses both files and asserts the
dependency specs are identical, so any future drift fails CI rather
than slipping into a release.

Closes Fraz round 10 MEDIUM 1.
"""

from __future__ import annotations

from pathlib import Path

# tomllib is stdlib in 3.11+; project supports 3.10+ so use the tomli
# back-compat alias when running on 3.10. tomli is a transitive dev
# dep available in this environment.
try:
    import tomllib  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover - 3.10 path
    import tomli as tomllib  # type: ignore[import-not-found, no-redef]


_REPO_ROOT = Path(__file__).resolve().parent.parent


def _parse_pyproject_dev_extras() -> set[str]:
    """Return the [project.optional-dependencies].dev set from pyproject."""
    with (_REPO_ROOT / "pyproject.toml").open("rb") as f:
        data = tomllib.load(f)
    extras = data["project"]["optional-dependencies"]["dev"]
    return {entry.strip() for entry in extras}


def _parse_requirements_dev_txt() -> set[str]:
    """Return the dependency-line set from requirements-dev.txt.

    Skips blank lines, comment lines (``#``-prefixed), and ``-r``
    references to other requirements files.
    """
    deps: set[str] = set()
    path = _REPO_ROOT / "requirements-dev.txt"
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#"):
            continue
        if line.startswith("-r"):
            continue
        deps.add(line)
    return deps


def test_requirements_dev_matches_pyproject_dev_extras() -> None:
    """requirements-dev.txt must list the same dependency specs as
    [project.optional-dependencies].dev in pyproject.toml.

    Failure prints which file is missing which entries so the fix shape
    is obvious from the test output alone.
    """
    pyproj = _parse_pyproject_dev_extras()
    reqs = _parse_requirements_dev_txt()

    missing_from_reqs = pyproj - reqs
    missing_from_pyproj = reqs - pyproj

    msg_lines: list[str] = []
    if missing_from_reqs:
        msg_lines.append(
            "Entries in pyproject [dev] but missing from "
            f"requirements-dev.txt: {sorted(missing_from_reqs)}"
        )
    if missing_from_pyproj:
        msg_lines.append(
            "Entries in requirements-dev.txt but missing from "
            f"pyproject [dev]: {sorted(missing_from_pyproj)}"
        )

    assert pyproj == reqs, "\n".join(msg_lines) or "drift detected"

# Bismillah ir-Rahman ir-Rahim