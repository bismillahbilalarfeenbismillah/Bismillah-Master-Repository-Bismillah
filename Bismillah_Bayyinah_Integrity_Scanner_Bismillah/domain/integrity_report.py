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
IntegrityReport — the report object Bayyinah returns for a single scan.

Phase 1 domain port of the dataclass in ``bayyinah_v0.py`` /
``bayyinah_v0_1.py``. Additive-only: ``to_dict`` produces output
byte-identical to v0.1, preserving the parity invariant asserted by
``tests/test_fixtures.py::test_v0_v01_parity``.

Semantic grounding:
    The IntegrityReport is Bayyinah's equivalent of a court record. It
    does not render a moral verdict; it records (a) the observed
    mechanisms of concealment, (b) the continuous integrity score those
    mechanisms produce under the APS weighting, (c) whether the scan
    itself completed cleanly, and (d) a standing disclaimer that the
    reader — not Bayyinah — performs the recognition.

    Al-Baqarah 2:8-10's munafiqun are identified structurally — by the
    gap between what they say and what they carry in their hearts —
    not by assertion. Likewise a Bayyinah report surfaces the gap
    between what a document displays and what it contains, and leaves
    the judgement to the consumer.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from domain.config import (
    TIER_LEGEND,
    TOOL_NAME,
    TOOL_VERSION,
    VERDICT_DISCLAIMER,
)
from domain.finding import Finding


@dataclass
class IntegrityReport:
    """The product of a single ``scan_pdf`` call.

    Shape parity with ``bayyinah_v0.IntegrityReport`` /
    ``bayyinah_v0_1.IntegrityReport``: every field those dataclasses
    carry is present here with the same name, default, and serialisation
    behaviour.

    Fields
    ------
    file_path
        Absolute or relative path of the scanned document, stringified.
    integrity_score
        APS-style continuous score in [0.0, 1.0]. 1.0 = no concealment
        observed. Lower = more concealment signal. Scan-incomplete reports
        are clamped at ``SCAN_INCOMPLETE_CLAMP`` (see ``domain.config``).
    findings
        List of ``Finding`` objects emitted by the analyzer pipeline,
        in emission order. Empty list = clean report.
    error
        Free-form error message if the scan failed to complete. ``None``
        on a clean scan.
    scan_incomplete
        ``True`` when the scan did not fully cover the document (error
        raised, or a ``scan_error`` finding was emitted). Consumers MUST
        treat an incomplete scan as inconclusive — absence of findings
        in the uninspected region is not evidence of cleanness.
    """

    file_path: str
    integrity_score: float = 1.0
    findings: list[Finding] = field(default_factory=list)
    error: str | None = None
    scan_incomplete: bool = False
    # v1.2.0 parity-break: per-layer coverage fraction. None means the
    # layer did not run or did not report coverage. Layer names are
    # source_layer values (zahir / batin). Initial implementation emits
    # {"zahir": None, "batin": None} via to_dict; instrumentation lands
    # in v1.3. See PARITY.md for the procedure under which this break
    # was made.
    coverage: dict[str, float | None] | None = None

    # ------------------------------------------------------------------
    # Serialisation
    # ------------------------------------------------------------------

    def to_dict(self) -> dict[str, Any]:
        """Serialise to the Phase 0 report shape extended for v1.2.0.

        v0.1 keys are emitted in the same order with the same values, so
        the v0.1 output remains a prefix subset of this method's output.
        v1.2.0 appends two additional keys after the v0.1 set:

          * ``scan_complete`` (bool): logical complement of
            ``scan_incomplete``, exposed under a positively-named key
            for downstream readability.
          * ``coverage`` (dict[str, float | None] | None): per-layer
            coverage fraction. ``{"zahir": None, "batin": None}`` until
            layer instrumentation lands in v1.3.

        This is a deliberate parity break documented in PARITY.md and
        CHANGELOG.md. Nothing from the domain-layer-only ``source_layer``
        field of individual findings leaks into this output.
        """
        return {
            "tool": TOOL_NAME,
            "version": TOOL_VERSION,
            "file_path": self.file_path,
            "integrity_score": round(self.integrity_score, 3),
            "scan_incomplete": self.scan_incomplete,
            "verdict_disclaimer": VERDICT_DISCLAIMER,
            "tier_legend": TIER_LEGEND,
            "findings": [f.to_dict() for f in self.findings],
            "error": self.error,
            # v1.2.0 additions (parity break, see PARITY.md and CHANGELOG.md).
            # scan_complete is a derived view of scan_incomplete so the two
            # cannot drift; coverage defaults to a per-layer mapping with
            # None values until layer instrumentation lands in v1.3.
            "scan_complete": not self.scan_incomplete,
            "coverage": (
                self.coverage if self.coverage is not None
                else {"zahir": None, "batin": None}
            ),
        }

    # ------------------------------------------------------------------
    # Convenience accessors (domain-only; not reflected in to_dict)
    # ------------------------------------------------------------------

    @property
    def zahir_findings(self) -> list[Finding]:
        """Findings whose concealment lives in the rendered/text surface."""
        return [f for f in self.findings if f.source_layer == "zahir"]

    @property
    def batin_findings(self) -> list[Finding]:
        """Findings whose concealment lives in the inner object graph."""
        return [f for f in self.findings if f.source_layer == "batin"]


__all__ = ["IntegrityReport"]

# Bismillah ir-Rahman ir-Rahim