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
"""HTTP-API helper functions shared between /scan and /demo/summarize.

The single helper here, ``scan_file_bytes``, encapsulates the temp-file
write, ``scan_file`` call, dict shaping, and cleanup that both the
production /scan endpoint and the v1.1.9 demo firewall endpoint need.

v1.2.1 (Q6 closure) wraps the scan in a subprocess with a wall-clock
timeout. If the scan does not complete within ``timeout`` seconds, the
worker process is terminated and a scan-incomplete report is returned
with verdict mughlaq. The subprocess provides process isolation: a
pymupdf segfault no longer crashes the API process.

The timeout payload shape matches IntegrityReport.to_dict() exactly so
downstream consumers see a schema-stable payload regardless of whether
the scan completed or timed out.

The deeper isolation fix (seccomp-bpf, dedicated scanning microservice,
OS-level CPU rlimit per request) remains on the v1.3 roadmap. v1.2.1
closes the most concrete instance of the threat model documented in
QUESTIONS.md Q6; v1.3 hardens the rest.
"""
from __future__ import annotations

import multiprocessing
import os
import queue as queue_module
import tempfile
from pathlib import Path

from bayyinah import scan_file
from domain.config import (
    SCAN_INCOMPLETE_CLAMP,
    TIER_LEGEND,
    TOOL_NAME,
    TOOL_VERSION,
    VERDICT_DISCLAIMER,
    VERDICT_MUGHLAQ,
)
from domain.value_objects import tamyiz_verdict


SCAN_TIMEOUT_SECONDS = 30


def _scan_worker(
    path: str,
    mode: str,
    result_queue: "multiprocessing.Queue",
) -> None:
    """Run scan_file in a child process; put a (status, payload) tuple
    on the result queue.

    Verdict is computed inside the worker (where the IntegrityReport
    object lives) and added to the dict before queueing. The parent
    process receives a fully-shaped dict with no need to reconstruct
    the report.
    """
    try:
        report = scan_file(path, mode=mode)
        payload = report.to_dict()
        payload["verdict"] = tamyiz_verdict(report)
        result_queue.put(("ok", payload))
    except Exception as exc:  # pragma: no cover - defensive
        # Send the exception class name + message back to the parent.
        # Full traceback would not pickle reliably for all exception
        # types; class name plus message is the contract Fraz's
        # round-3 framing prescribes for cross-process error reporting.
        result_queue.put(("error", f"{type(exc).__name__}: {exc}"))


def _timeout_payload(filename: str, timeout: int) -> dict:
    """The dict returned when a scan exceeds the wall-clock budget.

    Shape matches IntegrityReport.to_dict() exactly so downstream
    consumers (CI gates, dashboards, the demo UI) see a schema-stable
    payload regardless of whether the scan completed or timed out.
    """
    return {
        "tool": TOOL_NAME,
        "version": TOOL_VERSION,
        "file_path": filename,
        "integrity_score": SCAN_INCOMPLETE_CLAMP,
        "scan_incomplete": True,
        "scan_complete": False,
        "coverage": {"zahir": None, "batin": None},
        "verdict": VERDICT_MUGHLAQ,
        "verdict_disclaimer": VERDICT_DISCLAIMER,
        "tier_legend": TIER_LEGEND,
        "findings": [],
        "error": (
            f"Scan timed out after {timeout} seconds. The document "
            f"may contain pathological structure that exceeds the "
            f"parser's time budget."
        ),
    }


def scan_file_bytes(
    contents: bytes,
    filename: str,
    mode: str = "forensic",
    timeout: int = SCAN_TIMEOUT_SECONDS,
) -> dict:
    """Scan ``contents`` and return the IntegrityReport as a dict.

    v1.2.1: the scan runs in a subprocess with a ``timeout``-second
    wall-clock budget. If the worker does not complete in time, it is
    terminated and a scan-incomplete payload is returned with verdict
    mughlaq. Process isolation also means a pymupdf segfault no longer
    takes down the API process.
    """
    suffix = Path(filename).suffix
    tmp = tempfile.NamedTemporaryFile(suffix=suffix, delete=False)
    try:
        tmp.write(contents)
        tmp.close()
        # Use an explicit fork context. Linux default is fork; setting
        # it explicitly prevents an upstream change to the global
        # default from breaking this code path. macOS default switched
        # to spawn in Python 3.8; pinning fork keeps test runs on
        # macOS aligned with production on Railway (Linux). Windows
        # has no fork and is unsupported.
        ctx = multiprocessing.get_context("fork")
        result_queue: "multiprocessing.Queue" = ctx.Queue()
        proc = ctx.Process(
            target=_scan_worker,
            args=(tmp.name, mode, result_queue),
        )
        proc.start()
        proc.join(timeout=timeout)
        if proc.is_alive():
            # Scan exceeded the wall-clock budget. Terminate the
            # worker, then kill if SIGTERM does not land in 5s.
            proc.terminate()
            proc.join(timeout=5)
            if proc.is_alive():
                proc.kill()
                proc.join()
            return _timeout_payload(filename, timeout)
        # Process completed within timeout. Drain the queue.
        try:
            status, data = result_queue.get_nowait()
        except queue_module.Empty:
            # Worker exited without putting anything on the queue.
            # This is unusual (would mean the worker was killed by
            # the OS, or _scan_worker raised before its try block).
            # Treat as a timeout-style failure for the consumer.
            return _timeout_payload(filename, timeout)
        if status == "error":
            # Re-raise as RuntimeError so existing callers that catch
            # Exception (api.py /scan, demo.py /demo/summarize) keep
            # working unchanged. The original exception type is in
            # the message string for diagnostic purposes.
            raise RuntimeError(data)
        payload = data
        payload["file_path"] = filename
        return payload
    finally:
        try:
            os.unlink(tmp.name)
        except OSError:
            pass


__all__ = ["scan_file_bytes", "SCAN_TIMEOUT_SECONDS"]

# Bismillah ir-Rahman ir-Rahim