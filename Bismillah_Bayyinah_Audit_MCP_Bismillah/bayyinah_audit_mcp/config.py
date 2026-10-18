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
"""Environment configuration for the Bayyinah Audit MCP server.

Security note:
    BAYYINAH_PATH_STRICT defaults to off for local stdio backward compatibility.
    SSE/HTTP transports must set BAYYINAH_PATH_STRICT=1 so client-supplied paths
    are constrained to BAYYINAH_AUDIT_ROOT and symlink escapes are rejected.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Literal, Mapping

Severity = Literal["HIGH", "MED", "LOW"]

VALID_SEVERITIES: tuple[str, ...] = ("HIGH", "MED", "LOW")
SEVERITY_RANK: dict[str, int] = {"LOW": 1, "MED": 2, "HIGH": 3}


@dataclass(frozen=True)
class BayyinahConfig:
    """Frozen runtime configuration.

    API keys are intentionally excluded. Cross-vendor audit reads keys only when
    that tool is invoked.
    """

    audit_root: Path
    framework_prompt: Path | None
    framework_pdf: Path | None
    section_index: Path | None
    furqan_lint_cmd: str
    severity_threshold: Severity
    path_strict: bool


def _optional_path(value: str | None) -> Path | None:
    if not value:
        return None
    return Path(value).expanduser()


def _severity(value: str | None) -> Severity:
    normalized = (value or "MED").strip().upper()
    if normalized not in VALID_SEVERITIES:
        return "MED"
    return normalized  # type: ignore[return-value]


def _bool_env(value: str | None) -> bool:
    if value is None:
        return False
    return value.strip().lower() in {"1", "true", "yes", "on", "strict"}


def load_config(env: Mapping[str, str] | None = None) -> BayyinahConfig:
    """Load configuration from environment variables."""

    source = env if env is not None else os.environ

    audit_root_raw = source.get("BAYYINAH_AUDIT_ROOT") or os.getcwd()
    audit_root = Path(audit_root_raw).expanduser().resolve()

    return BayyinahConfig(
        audit_root=audit_root,
        framework_prompt=_optional_path(source.get("BAYYINAH_FRAMEWORK_PROMPT")),
        framework_pdf=_optional_path(source.get("BAYYINAH_FRAMEWORK_PDF")),
        section_index=_optional_path(source.get("BAYYINAH_SECTION_INDEX")),
        furqan_lint_cmd=source.get("BAYYINAH_FURQAN_LINT_CMD", "furqan-lint"),
        severity_threshold=_severity(source.get("BAYYINAH_SEVERITY_THRESHOLD")),
        path_strict=_bool_env(source.get("BAYYINAH_PATH_STRICT")),
    )


def resolve_path(path: str | Path, config: BayyinahConfig | None = None) -> Path:
    """Resolve an absolute or root-relative path.

    BAYYINAH_AUDIT_ROOT is the base for relative paths. Absolute paths are
    allowed by default for backward compatibility.

    When BAYYINAH_PATH_STRICT=1, the resolved path must remain inside
    BAYYINAH_AUDIT_ROOT after symlink resolution. This prevents arbitrary local
    file reads when the server is exposed through SSE/HTTP.
    """

    cfg = config or load_config()
    raw = Path(path).expanduser()

    if raw.is_absolute():
        resolved = raw.resolve()
    else:
        resolved = (cfg.audit_root / raw).resolve()

    if cfg.path_strict and not resolved.is_relative_to(cfg.audit_root):
        raise ValueError(
            f"Path '{resolved}' is outside BAYYINAH_AUDIT_ROOT '{cfg.audit_root}'. "
            "Set BAYYINAH_PATH_STRICT=0 only for trusted local stdio use."
        )

    return resolved


def severity_blocks(severity: str, threshold: str) -> bool:
    """Return whether severity meets or exceeds the configured block threshold."""

    return SEVERITY_RANK.get(severity.upper(), 0) >= SEVERITY_RANK.get(
        threshold.upper(), SEVERITY_RANK["MED"]
    )

# Bismillah ir-Rahman ir-Rahim