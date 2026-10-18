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
BaseAnalyzer — the uniform "middle community" contract (Al-Baqarah 2:143).

    وَكَذَٰلِكَ جَعَلْنَاكُمْ أُمَّةً وَسَطًا لِّتَكُونُوا شُهَدَاءَ عَلَى النَّاسِ
    "And thus We have made you a middle community, that you might be
    witnesses over the people."

The architectural reading: an analyzer is a witness. Every analyzer
inherits the same contract, applies the same standard, and reports in
the same shape — so the reader who inspects the final IntegrityReport
can trust that every concealment mechanism was evaluated against the
same bar, regardless of which subsystem produced it. No analyzer gets
to invent its own output format. No analyzer gets to suppress its own
errors. The contract is the *wasatiyyah* — the balance that makes the
witness just.

Concretely, ``BaseAnalyzer`` is an abstract class declaring:

    .name          — short identifier (stable across versions)
    .error_prefix  — how this analyzer's errors appear in report.error
    .source_layer  — "zahir" or "batin"; which concealment locus this
                     analyzer inspects
    .scan(file_path: Path) -> IntegrityReport
                   — the analyzer's pass over the document, returning
                     its own self-contained report

Analyzers returning a full ``IntegrityReport`` (not just a finding list)
is the Phase 2 generalisation. The registry then composes those reports
into the document-level report. A report-returning contract lets each
analyzer own its own scan-incomplete state, its own error, and its own
score calculation — the registry merges, but does not second-guess.

This is additive-only: v0.1's own ``BaseAnalyzer`` (which takes a
``PDFContext`` and returns ``list[Finding]``) is unchanged. The two
contracts coexist in different namespaces until later phases migrate
v0.1's scanners onto this one.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import ClassVar

from domain import (
    Finding,
    IntegrityReport,
    SourceLayer,
    compute_muwazana_score,
)
from infrastructure.file_router import FileKind


# ---------------------------------------------------------------------------
# BaseAnalyzer
# ---------------------------------------------------------------------------

class BaseAnalyzer(ABC):
    """Abstract base class for every Bayyinah analyzer.

    Subclasses MUST declare non-empty ``name`` and ``error_prefix`` class
    attributes, and MUST declare ``source_layer`` as either ``"zahir"``
    or ``"batin"``. The ``__init_subclass__`` hook enforces these for
    every concrete subclass (i.e. anything without remaining abstract
    methods).

    Subclasses MUST implement ``scan(file_path: Path) -> IntegrityReport``.
    Conventions the registry relies on:

      * **Expected failures** (the file is not a PDF, a specific parser
        cannot open the font stream) SHOULD be converted into a
        ``scan_error`` finding inside the analyzer. The helper
        ``_scan_error_report`` produces the canonical shape.
      * **Unexpected failures** MAY raise. The registry catches them and
        records the error at the merged-report level using this
        analyzer's ``error_prefix``.

    The analyzer's ``source_layer`` attribute is used by
    ``_scan_error_report`` to correctly attribute the scan_error
    finding's locus — a text-layer analyzer's failure is a zahir
    scan_error, even though the ``scan_error`` mechanism itself
    defaults to batin classification.
    """

    # ------------------------------------------------------------------
    # Declared contract (subclasses override these)
    # ------------------------------------------------------------------

    name: ClassVar[str] = ""
    """Short, stable identifier used by the registry and appearing in
    scan_error finding locations (``analyzer:<name>``)."""

    error_prefix: ClassVar[str] = "Analyzer error"
    """Prefix the registry applies when this analyzer raises an
    unexpected exception. Mirrors v0.1's format, e.g.
    ``"Text layer scan error: <message>"``."""

    source_layer: ClassVar[SourceLayer] = "batin"
    """Which concealment locus this analyzer inspects. Drives the
    source_layer of any ``scan_error`` finding the analyzer emits."""

    supported_kinds: ClassVar[frozenset[FileKind]] = frozenset({FileKind.PDF})
    """File kinds this analyzer is willing to scan.

    Phase 9 extension of the middle-community contract (Al-Baqarah 2:60:
    *qad 'alima kullu unaasin mashrabahum* — each tribe knew its
    drinking-place). An analyzer declares which FileKinds it can speak
    about; the registry only dispatches it for a matching file.

    The default is ``{FileKind.PDF}`` so every pre-Phase-9 analyzer
    retains byte-identical behaviour without any change to its source:
    the PDF registry, run on a PDF, reduces to exactly the same set of
    analyzers firing in the same order as before. Non-PDF analyzers
    (text, JSON, markdown, code) override this to declare their own
    supported kinds.
    """

    # ------------------------------------------------------------------
    # Subclass registration-time validation
    # ------------------------------------------------------------------

    def __init_subclass__(cls, **kwargs: object) -> None:
        """Enforce the middle-community contract at class-definition time.

        Intermediate abstract subclasses (e.g. a mix-in that still has
        unimplemented abstract methods) are not required to declare
        name/source_layer — only the concrete leaves are. We detect
        "concrete" by checking whether the resolved ``scan`` method is
        still marked abstract. ``__abstractmethods__`` cannot be used
        here because ``ABCMeta`` populates it *after* ``__init_subclass__``
        returns.
        """
        super().__init_subclass__(**kwargs)
        scan_impl = getattr(cls, "scan", None)
        if scan_impl is None or getattr(scan_impl, "__isabstractmethod__", False):
            # Still abstract; skip validation.
            return
        if not isinstance(cls.name, str) or not cls.name:
            raise TypeError(
                f"Concrete BaseAnalyzer subclass {cls.__name__!r} must "
                "declare a non-empty string class attribute 'name'."
            )
        if cls.source_layer not in ("zahir", "batin"):
            raise TypeError(
                f"Concrete BaseAnalyzer subclass {cls.__name__!r} must "
                "declare source_layer as either 'zahir' or 'batin' — "
                f"got {cls.source_layer!r}."
            )
        if not isinstance(cls.error_prefix, str) or not cls.error_prefix:
            raise TypeError(
                f"Concrete BaseAnalyzer subclass {cls.__name__!r} must "
                "declare a non-empty string class attribute 'error_prefix'."
            )
        # supported_kinds must be a non-empty frozenset of FileKind.
        sk = cls.supported_kinds
        if not isinstance(sk, frozenset) or not sk:
            raise TypeError(
                f"Concrete BaseAnalyzer subclass {cls.__name__!r} must "
                "declare 'supported_kinds' as a non-empty frozenset of "
                f"FileKind members — got {sk!r}."
            )
        if not all(isinstance(k, FileKind) for k in sk):
            raise TypeError(
                f"Concrete BaseAnalyzer subclass {cls.__name__!r} has "
                "non-FileKind entries in supported_kinds."
            )

    # ------------------------------------------------------------------
    # Abstract scan
    # ------------------------------------------------------------------

    @abstractmethod
    def scan(self, file_path: Path) -> IntegrityReport:
        """Inspect the document at ``file_path`` and return this analyzer's
        slice of the final integrity report.

        Implementations are free to populate any subset of
        IntegrityReport fields, but the conventions the registry assumes
        are:

          * ``findings`` — list of this analyzer's findings, in emission
            order.
          * ``error`` — a free-form message if the analyzer's own pass
            was incomplete, ``None`` otherwise.
          * ``scan_incomplete`` — ``True`` if the analyzer could not
            fully cover its scope; the registry propagates the flag.
          * ``integrity_score`` — the analyzer's own continuous score
            over its findings. The registry RECOMPUTES the merged score
            from the concatenated findings, so this value is advisory
            at the per-analyzer level.
        """
        raise NotImplementedError

    # ------------------------------------------------------------------
    # Helpers — canonical shapes for common report states
    # ------------------------------------------------------------------

    def _empty_report(self, file_path: Path) -> IntegrityReport:
        """Canonical clean report — no findings, perfect score.

        Use at the top of ``scan`` to seed a per-analyzer report the
        implementation then populates.
        """
        return IntegrityReport(file_path=str(file_path), integrity_score=1.0)

    def _scan_error_report(
        self,
        file_path: Path,
        message: str,
        *,
        location: str | None = None,
    ) -> IntegrityReport:
        """Canonical scan-incomplete report carrying a ``scan_error`` finding.

        Produces the v0.1-compatible shape: one ``scan_error`` finding
        (tier 3, severity 0.0 — reported but non-deducting) attributed
        to this analyzer's source layer, plus ``error`` populated with
        the analyzer's ``error_prefix`` and ``scan_incomplete=True``.
        The integrity_score remains at 1.0 here because the analyzer
        emitted no evidence of concealment; the registry will apply the
        scan-incomplete clamp after merging.
        """
        finding = Finding(
            mechanism="scan_error",
            tier=3,
            confidence=1.0,
            description=message,
            location=location or f"analyzer:{self.name}",
            surface="(scan did not complete)",
            concealed="(absence of findings is not evidence of cleanness)",
            source_layer=self.source_layer,
        )
        return IntegrityReport(
            file_path=str(file_path),
            integrity_score=compute_muwazana_score([finding]),
            findings=[finding],
            error=f"{self.error_prefix}: {message}",
            scan_incomplete=True,
        )

    # ------------------------------------------------------------------
    # Dunders
    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}("
            f"name={self.name!r}, source_layer={self.source_layer!r})"
        )


__all__ = ["BaseAnalyzer"]

# Bismillah ir-Rahman ir-Rahim