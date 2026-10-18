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
Bayyinah domain exceptions.

These types are the contract the domain layer uses to signal failure.
Infrastructure adapters (pypdf, pymupdf) raise library-specific
exceptions; analyzers catch those and re-raise a Bayyinah exception
that callers can handle without importing the underlying parser.

Design invariant: every exception here inherits from ``BayyinahError``,
so a single ``except BayyinahError`` at the edge catches anything the
domain layer can raise. Python's built-in exceptions (``TypeError``,
``ValueError``) still surface for real programming bugs — those should
not be silently swallowed.

Phase 1 introduces the hierarchy only. Nothing in ``bayyinah_v0.py`` or
``bayyinah_v0_1.py`` raises these yet; later phases will migrate the
scanner-side error paths onto this contract. Additive-only.
"""

from __future__ import annotations


class BayyinahError(Exception):
    """Root exception for every error raised from the Bayyinah domain.

    Callers that want to handle any Bayyinah-originated failure without
    caring which stage of the scan produced it should catch this type.
    Library errors from pypdf/pymupdf that we have not wrapped intentionally
    will NOT inherit from this — they are programming bugs we want to see.
    """


class PDFParseError(BayyinahError):
    """The file could not be opened, decoded, or parsed as a PDF.

    Raised when pypdf/pymupdf fail on the container (bad xref, truncated
    file, unsupported encryption). This is a structural failure — the
    scan cannot even begin.
    """


class ScanError(BayyinahError):
    """An analyzer could not complete its pass over the document.

    A ``ScanError`` is recoverable at the report level: the scanner
    records the failure as a ``scan_error`` finding, sets
    ``scan_incomplete = True``, and clamps the integrity score. The
    absence of findings from the incomplete region cannot be taken as
    evidence of cleanness — that is the whole point of the clamp.
    """

    def __init__(self, message: str, *, layer: str | None = None) -> None:
        super().__init__(message)
        self.layer = layer
        """Which source layer's analyzer failed — 'zahir' or 'batin' if
        known, else None. Lets report assembly attribute the scan_error
        correctly without re-inspecting the traceback."""


class InvalidFindingError(BayyinahError, ValueError):
    """A Finding was constructed with semantically invalid fields.

    Raised by ``Finding.__post_init__`` when confidence is out of range,
    tier is not 1/2/3, or source_layer is neither 'zahir' nor 'batin'.
    This is a programming error — inherits from ``ValueError`` so code
    that catches either type still catches it.
    """


__all__ = [
    "BayyinahError",
    "PDFParseError",
    "ScanError",
    "InvalidFindingError",
]

# Bismillah ir-Rahman ir-Rahim