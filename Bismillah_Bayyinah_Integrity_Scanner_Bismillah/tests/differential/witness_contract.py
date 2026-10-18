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
DifferentialWitness contract (v1.8.0).

Defines the abstract base class every external-witness implementation
must satisfy, plus the WitnessFinding and WitnessDivergence
dataclasses used by differential pair tests.

Per docs/differential_testing.md §2: the contract is intentionally
minimal so that witnesses with very different internal designs
(structural inspectors like pdfid, rule-based matchers like yara,
signature-based scanners like clamav) can all conform.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass(frozen=True)
class WitnessFinding:
    """One observation by an external witness.

    Fields:
        witness_name: stable identifier of the witness tool
                      (e.g. "pdfid").
        finding_key: the witness's mechanism / rule / signature name.
                     Witnesses use their own vocabulary; mapping to
                     Bayyinah's mechanism names is the pair test's
                     responsibility, not the witness's.
        location: optional structural reference (page / object id /
                  byte offset). Empty string when not applicable.
    """

    witness_name: str
    finding_key: str
    location: str


@dataclass(frozen=True)
class WitnessDivergence:
    """A divergence between Bayyinah and an external witness on one
    fixture.

    Fields:
        fixture: file path of the fixture under inspection.
        kind: one of "solo_bayyinah", "solo_witness", "distinct_locus"
              per docs/differential_testing.md §2.2.
        bayyinah_finding_key: Bayyinah mechanism name when applicable;
                              empty string for solo_witness.
        witness_finding_key: external witness mechanism when
                             applicable; empty string for solo_bayyinah.
        location: structural reference when known; empty string
                  otherwise.
    """

    fixture: str
    kind: str
    bayyinah_finding_key: str
    witness_finding_key: str
    location: str

    _VALID_KINDS = ("solo_bayyinah", "solo_witness", "distinct_locus")

    def __post_init__(self) -> None:
        if self.kind not in self._VALID_KINDS:
            raise ValueError(
                f"WitnessDivergence kind must be one of "
                f"{self._VALID_KINDS}; got {self.kind!r}"
            )


class DifferentialWitness(ABC):
    """Abstract base for an external-witness implementation.

    A subclass MUST implement ``witness_name`` and ``observe``. A
    subclass MAY override ``is_available`` if availability depends on
    more than just module-import success (e.g. system-daemon
    reachability for clamd).
    """

    @property
    @abstractmethod
    def witness_name(self) -> str:
        """The stable identifier of this witness tool."""
        raise NotImplementedError

    @abstractmethod
    def observe(self, path: Path) -> List[WitnessFinding]:
        """Run the witness against ``path`` and return its findings.

        Implementations MUST return a list (possibly empty). Raising
        an exception is an error in the witness, not a divergence.
        """
        raise NotImplementedError

    def is_available(self) -> bool:
        """Return True iff the witness can run in the current env.

        Default: True. Override to add module-import or daemon-
        reachability checks.
        """
        return True

    @property
    def install_hint(self) -> str:
        """Human-readable install instruction for when is_available
        returns False. Override in subclasses with the tool-specific
        hint."""
        return "(no install hint provided by witness subclass)"


__all__ = [
    "DifferentialWitness",
    "WitnessFinding",
    "WitnessDivergence",
]

# Bismillah ir-Rahman ir-Rahim