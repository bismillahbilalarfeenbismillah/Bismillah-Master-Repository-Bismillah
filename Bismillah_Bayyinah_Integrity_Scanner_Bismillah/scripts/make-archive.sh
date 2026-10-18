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
#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# make-archive.sh — produce a clean zip of the Bayyinah working tree.
#
# macOS's Finder zip and `ditto -c` both inject __MACOSX/ resource-fork
# sidecar directories and .DS_Store files into archives. Those pollute
# the zip for every collaborator who extracts it, and they are exactly
# the kind of silent-surface artifact this scanner is designed to flag.
#
# This script wraps `zip` with the two exclusions that keep a shared
# archive clean. Run from the repository root:
#
#     ./scripts/make-archive.sh                         # default name
#     ./scripts/make-archive.sh bayyinah-v1.0-share     # custom name
#
# Output: <name>.zip, one level up from the repo root so the extracted
# folder reconstructs cleanly.
# ---------------------------------------------------------------------------

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ARCHIVE_NAME="${1:-$(basename "$REPO_ROOT")}"
ARCHIVE_PATH="${REPO_ROOT}/../${ARCHIVE_NAME}.zip"

cd "$(dirname "$REPO_ROOT")"
FOLDER="$(basename "$REPO_ROOT")"

echo "Creating clean archive: ${ARCHIVE_PATH}"
echo "Excluding: .DS_Store, __MACOSX/, __pycache__/, *.egg-info, .pytest_cache"

# -r     : recurse into directories
# -x ... : exclusion patterns — each must cover both top-level and nested
#          occurrences. The patterns match against the archive path, not
#          the filesystem path.
zip -r "${ARCHIVE_PATH}" "${FOLDER}" \
    -x "*.DS_Store" \
    -x "*__MACOSX/*" \
    -x "*__pycache__/*" \
    -x "*.egg-info/*" \
    -x "*.pytest_cache/*" \
    -x "*.mypy_cache/*" \
    -x "*.ruff_cache/*" \
    -x "*build/*" \
    -x "*/bayyinah-1.0.0/*"

echo ""
echo "Done. Archive contents summary:"
unzip -l "${ARCHIVE_PATH}" | tail -1
echo ""
echo "Verify no junk entries:"
if unzip -l "${ARCHIVE_PATH}" | grep -E "(__MACOSX|\.DS_Store|__pycache__|\.egg-info)" > /dev/null; then
    echo "  WARNING — junk entries found in archive:"
    unzip -l "${ARCHIVE_PATH}" | grep -E "(__MACOSX|\.DS_Store|__pycache__|\.egg-info)"
    exit 1
else
    echo "  OK — no .DS_Store / __MACOSX / __pycache__ / .egg-info in archive."
fi

# Bismillah ir-Rahman ir-Rahim