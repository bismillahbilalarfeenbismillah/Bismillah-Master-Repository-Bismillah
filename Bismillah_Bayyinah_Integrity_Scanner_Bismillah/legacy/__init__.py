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
"""
bayyinah.legacy — pointers to the frozen reference implementations.

Bayyinah preserves two complete prior implementations of the PDF scanner
for reproducibility and byte-identical parity testing:

* ``bayyinah_v0``    — the original monolithic scanner (v0).
* ``bayyinah_v0_1``  — the fat-split intermediate (v0.1).

These modules ship unchanged at the top level of the distribution
(``bayyinah_v0.py`` and ``bayyinah_v0_1.py``). Their bytes are
md5-fingerprinted and the fingerprints are asserted in CI after every
push — the ``additive-only`` invariant of the project. The refactored
scanner at ``bayyinah.scan_pdf`` is byte-identical to
``bayyinah_v0.scan_pdf`` on every Phase 0 fixture; this guarantee is
what keeps the 1.0 release honest.

This package exists as an organisational pointer. The reference modules
*must* remain importable at their original top-level names for parity
CI and for any downstream caller that pinned to those paths — so they
are not physically moved. ``legacy.bayyinah_v0`` and
``legacy.bayyinah_v0_1`` are provided as additive aliases for readers
who prefer the conceptual grouping.

Usage::

    # Canonical — unchanged since v0:
    import bayyinah_v0
    bayyinah_v0.scan_pdf("file.pdf")

    # Conceptual alias (added in 1.0 for organisational clarity):
    from bayyinah.legacy import bayyinah_v0
    bayyinah_v0.scan_pdf("file.pdf")

Both resolve to the same module object.

Reference: Al-Baqarah 2:143 — the middle community as uniform witness.
The v0 / v0.1 modules are the preserved witnesses against which every
later refactor has been measured.
"""

from __future__ import annotations

# Re-export both reference modules at their conceptual location.
# These ``import`` statements bind ``legacy.bayyinah_v0`` and
# ``legacy.bayyinah_v0_1`` as attributes of this package without
# copying or shadowing the original top-level modules.
import bayyinah_v0  # noqa: F401 — public re-export
import bayyinah_v0_1  # noqa: F401 — public re-export


__all__ = [
    "bayyinah_v0",
    "bayyinah_v0_1",
]

# Bismillah ir-Rahman ir-Rahim