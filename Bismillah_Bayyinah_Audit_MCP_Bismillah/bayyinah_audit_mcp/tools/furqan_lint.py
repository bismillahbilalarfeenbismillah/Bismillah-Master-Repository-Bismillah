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
"""bayyinah_run_furqan_lint tool."""

from __future__ import annotations

import json
import shlex
import subprocess
from pathlib import Path
from typing import Any, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import TypedDict

from bayyinah_audit_mcp.config import load_config, resolve_path, severity_blocks

Severity = Literal["HIGH", "MED", "LOW"]


class FurqanLintInput(BaseModel):
    """Input model for bayyinah_run_furqan_lint."""

    model_config = ConfigDict(extra="forbid")

    path: str = Field(description="Root-relative or absolute path to lint.")
    extra_args: list[str] = Field(
        default_factory=list,
        description="Additional command-line arguments passed after the path.",
    )
    timeout_seconds: int = Field(
        default=60,
        ge=1,
        le=600,
        description="Subprocess timeout in seconds.",
    )
    severity_threshold: Severity | None = Field(
        default=None,
        description="Override BAYYINAH_SEVERITY_THRESHOLD for blocked=true calculation.",
    )
    max_output_chars: int = Field(
        default=65536,
        ge=0,
        le=1048576,
        description="Maximum stdout/stderr characters returned through the MCP response.",
    )


class Finding(TypedDict):
    severity: Severity
    section_ref: str
    message: str
    location: str


class FurqanLintOutput(BaseModel):
    status: str
    command: list[str]
    returncode: Optional[int] = None
    findings: list[Finding]
    blocked: bool
    stdout: str
    stderr: str
    error: Optional[str] = None


def _coerce_severity(value: Any) -> Severity:
    normalized = str(value or "LOW").strip().upper()
    if normalized in {"HIGH", "MED", "LOW"}:
        return normalized  # type: ignore[return-value]
    if normalized in {"MEDIUM", "WARN", "WARNING"}:
        return "MED"
    if normalized in {"ERROR", "CRITICAL", "BLOCKER"}:
        return "HIGH"
    return "LOW"


def _coerce_finding(obj: Any) -> Finding | None:
    if not isinstance(obj, dict):
        return None

    message = obj.get("message") or obj.get("detail") or obj.get("description")
    if not message:
        return None

    return {
        "severity": _coerce_severity(obj.get("severity")),
        "section_ref": str(obj.get("section_ref") or obj.get("section") or "23.3"),
        "message": str(message),
        "location": str(
            obj.get("location") or obj.get("path") or obj.get("span") or "global"
        ),
    }


def _parse_json_findings(stdout: str) -> list[Finding]:
    try:
        payload = json.loads(stdout)
    except json.JSONDecodeError:
        return []

    raw_findings: Any
    if isinstance(payload, list):
        raw_findings = payload
    elif isinstance(payload, dict):
        raw_findings = payload.get("findings") or payload.get("issues") or []
    else:
        return []

    findings: list[Finding] = []
    if isinstance(raw_findings, list):
        for item in raw_findings:
            finding = _coerce_finding(item)
            if finding is not None:
                findings.append(finding)

    return findings


def _parse_text_findings(stdout: str, stderr: str) -> list[Finding]:
    findings: list[Finding] = []
    combined = "\n".join(part for part in (stdout, stderr) if part)

    for line_number, raw_line in enumerate(combined.splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue

        upper = line.upper()
        severity: Severity
        if upper.startswith("HIGH"):
            severity = "HIGH"
        elif upper.startswith(("MED", "MEDIUM", "WARN", "WARNING")):
            severity = "MED"
        elif upper.startswith("LOW"):
            severity = "LOW"
        else:
            continue

        findings.append(
            {
                "severity": severity,
                "section_ref": "23.3",
                "message": line,
                "location": f"furqan-lint output line {line_number}",
            }
        )

    return findings


def _build_command(cmd_value: str, target: Path, extra_args: list[str]) -> list[str]:
    base = shlex.split(cmd_value) if cmd_value.strip() else ["furqan-lint"]
    return [*base, str(target), *extra_args]


def _coerce_output(value: str | bytes | None) -> str:
    if value is None:
        return ""
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    return value


def _truncate_output(text: str, max_chars: int) -> str:
    if max_chars <= 0:
        return ""

    if len(text) <= max_chars:
        return text

    suffix = "\n[truncated by bayyinah_run_furqan_lint]"
    if max_chars <= len(suffix):
        return suffix[:max_chars]

    return text[: max_chars - len(suffix)] + suffix


def bayyinah_run_furqan_lint(request: FurqanLintInput) -> FurqanLintOutput:
    """Invoke furqan-lint as a subprocess and return Bayyinah-format findings."""

    config = load_config()
    threshold = request.severity_threshold or config.severity_threshold

    try:
        target = resolve_path(request.path, config)
    except ValueError as exc:
        return FurqanLintOutput(
            status="error",
            command=[],
            returncode=None,
            findings=[],
            blocked=False,
            stdout="",
            stderr="",
            error=str(exc),
        )

    command = _build_command(config.furqan_lint_cmd, target, request.extra_args)

    try:
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=request.timeout_seconds,
            check=False,
        )
    except FileNotFoundError as exc:
        return FurqanLintOutput(
            status="unavailable",
            command=command,
            returncode=None,
            findings=[],
            blocked=False,
            stdout="",
            stderr="",
            error=f"furqan-lint command not found: {exc}",
        )
    except subprocess.TimeoutExpired as exc:
        return FurqanLintOutput(
            status="timeout",
            command=command,
            returncode=None,
            findings=[],
            blocked=False,
            stdout=_truncate_output(
                _coerce_output(exc.stdout),
                request.max_output_chars,
            ),
            stderr=_truncate_output(
                _coerce_output(exc.stderr),
                request.max_output_chars,
            ),
            error=f"furqan-lint timed out after {request.timeout_seconds} seconds.",
        )

    stdout = completed.stdout or ""
    stderr = completed.stderr or ""
    findings = _parse_json_findings(stdout)

    if not findings:
        findings = _parse_text_findings(stdout, stderr)

    blocked = any(severity_blocks(item["severity"], threshold) for item in findings)

    error: str | None = None
    if completed.returncode == 0 and not findings:
        status = "ok"
    elif completed.returncode != 0 and not findings:
        status = "error"
        error = "furqan-lint exited non-zero without Bayyinah-format findings."
    elif blocked:
        status = "blocked"
    else:
        status = "completed_with_findings"

    return FurqanLintOutput(
        status=status,
        command=command,
        returncode=completed.returncode,
        findings=findings,
        blocked=blocked,
        stdout=_truncate_output(stdout, request.max_output_chars),
        stderr=_truncate_output(stderr, request.max_output_chars),
        error=error,
    )

# Bismillah ir-Rahman ir-Rahim