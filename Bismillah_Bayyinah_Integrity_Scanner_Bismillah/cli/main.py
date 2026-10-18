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
bayyinah CLI — the surface the world sees (Al-Baqarah 2:204).

    وَمِنَ النَّاسِ مَن يُعْجِبُكَ قَوْلُهُ فِي الْحَيَاةِ الدُّنْيَا
    "And of the people is he whose speech pleases you in worldly life..."

The architectural reading: a tool's CLI is the first thing a user sees
— its speech in the worldly life. Bayyinah's CLI must therefore be
unambiguous, predictable, and non-presumptuous: it reports what the
scan found, it does not assert a moral verdict, and it exits with
codes a CI pipeline can reliably branch on.

Public shape::

    bayyinah scan <file>                    # human-readable report
    bayyinah scan <file> --json             # machine-readable JSON
    bayyinah scan <file> --quiet            # suppress report, keep
                                            # the exit code
    bayyinah scan <file> --summary          # one-paragraph summary
    bayyinah --version                      # "bayyinah X.Y.Z"

Exit codes — stable contract, byte-identical to v0/v0.1::

    0   scan completed cleanly with zero findings
    1   scan completed with one or more findings
    2   scan could not complete (file not found, unparseable, ...)

Subcommand-based argparse layout is deliberate. The ``scan``
subcommand is the first of several this CLI will grow into later
(DOCX/HTML/code scanning, batch mode, registry inspection), and the
subcommand style keeps the surface extensible without rebinding
existing arguments.

Additive-only: this module does not import from ``bayyinah_v0`` or
``bayyinah_v0_1``. Both of those continue to ship their own
``main(argv)`` entry points at the ``bayyinah_v0`` /
``bayyinah_v0_1`` module level for callers that pinned to them.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

from bayyinah import (
    __version__,
    format_text_report,
    plain_language_summary,
    scan_pdf,
)


# ---------------------------------------------------------------------------
# Exit-code constants — named so callers / tests do not lean on magic numbers.
# ---------------------------------------------------------------------------

EXIT_CLEAN = 0
"""Scan completed with zero findings."""

EXIT_FINDINGS = 1
"""Scan completed; at least one concealment mechanism was detected."""

EXIT_ERROR = 2
"""Scan did not complete (missing file, unparseable PDF, …)."""


# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------

def _build_parser() -> argparse.ArgumentParser:
    """Construct the top-level argparse parser.

    Factored out so tests can introspect the CLI surface without
    invoking ``main``.
    """
    parser = argparse.ArgumentParser(
        prog="bayyinah",
        description=(
            "Bayyinah — file integrity scanner that detects hidden, "
            "concealed, or adversarial content in digital documents. "
            "Reports the gap between what the file displays and what "
            "the file contains. Does not assert malicious intent — "
            "the reader performs the recognition."
        ),
        epilog=(
            "Reference: Munafiq Protocol — DOI 10.5281/zenodo.19677111. "
            "Licensed Apache-2.0."
        ),
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"bayyinah {__version__}",
        help="show program version and exit",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        metavar="COMMAND",
        title="commands",
        description="Pick the operation to run.",
    )

    # ----- scan --------------------------------------------------------
    scan_p = subparsers.add_parser(
        "scan",
        help="scan a single document for integrity violations",
        description=(
            "Scan a single file. Emits findings, an integrity score, "
            "and a scan-incomplete flag if any analyzer could not "
            "fully cover its scope."
        ),
    )
    scan_p.add_argument(
        "file",
        metavar="FILE",
        type=Path,
        help=(
            "path to the document to scan — PDF, DOCX, HTML, XLSX, PPTX, "
            "EML, CSV, JSON, images (PNG / JPEG / GIF / BMP / TIFF / WebP), "
            "SVG, and Markdown / code / plain text are all supported; any "
            "other format surfaces an unknown_format finding via FallbackAnalyzer"
        ),
    )

    output_modes = scan_p.add_mutually_exclusive_group()
    output_modes.add_argument(
        "--json",
        action="store_true",
        help="emit the report as JSON on stdout (machine-readable)",
    )
    output_modes.add_argument(
        "--summary",
        action="store_true",
        help="emit only the one-paragraph plain-language summary",
    )
    output_modes.add_argument(
        "--quiet",
        action="store_true",
        help=(
            "suppress report output entirely; the exit code still "
            "reflects findings (0 clean, 1 findings, 2 error)"
        ),
    )

    return parser


# ---------------------------------------------------------------------------
# Exit-code resolution — one place, one rule.
# ---------------------------------------------------------------------------

def _exit_code_for(report) -> int:
    """Map an IntegrityReport to its CLI exit code.

    Preserved byte-identically from v0/v0.1:

        error present   → EXIT_ERROR    (2)
        findings > 0    → EXIT_FINDINGS (1)
        otherwise       → EXIT_CLEAN    (0)

    ``scan_incomplete`` without ``error`` (e.g. an analyzer that
    emitted a ``scan_error`` finding but cleared the top-level error)
    falls through to the findings-or-clean branch — that is v0's
    historical behaviour, and changing it would break CI pipelines.
    """
    if report.error:
        return EXIT_ERROR
    if report.findings:
        return EXIT_FINDINGS
    return EXIT_CLEAN


# ---------------------------------------------------------------------------
# Command dispatch
# ---------------------------------------------------------------------------

def _cmd_scan(args: argparse.Namespace) -> int:
    """Run the ``scan`` subcommand."""
    report = scan_pdf(args.file)

    if args.quiet:
        pass  # exit code only
    elif args.json:
        print(json.dumps(report.to_dict(), indent=2, default=str))
    elif args.summary:
        print(plain_language_summary(report))
    else:
        print(format_text_report(report))

    return _exit_code_for(report)


# ---------------------------------------------------------------------------
# main — the script entry point
# ---------------------------------------------------------------------------

def main(argv: Sequence[str] | None = None) -> int:
    """CLI entry point.

    Parameters
    ----------
    argv
        Argument vector (without the leading program name). If
        ``None``, ``sys.argv[1:]`` is used — the normal console-script
        behaviour.

    Returns
    -------
    int
        The exit code (0 / 1 / 2 as documented at the top of this
        module).

    The function is deliberately ``return`` instead of ``sys.exit`` so
    tests can call it in-process without intercepting ``SystemExit``.
    The ``if __name__ == '__main__'`` guard below calls ``sys.exit``
    with the return value for real console invocation.
    """
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help(sys.stderr)
        return EXIT_ERROR

    if args.command == "scan":
        return _cmd_scan(args)

    # argparse enforces the subparser choices, so the fall-through is
    # defensive: any new subcommand added without a handler will hit
    # this and surface a clear error instead of silently exiting 0.
    parser.error(f"unrecognised command: {args.command!r}")
    return EXIT_ERROR  # pragma: no cover — parser.error raises SystemExit


if __name__ == "__main__":  # pragma: no cover — exercised via console_scripts
    sys.exit(main())

# Bismillah ir-Rahman ir-Rahim