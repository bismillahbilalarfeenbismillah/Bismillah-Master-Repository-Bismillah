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
"""bayyinah_audit_artifact tool."""

from __future__ import annotations

from pathlib import Path
from typing import TypedDict

from pydantic import BaseModel, ConfigDict, Field

from bayyinah_audit_mcp.config import load_config, resolve_path
from bayyinah_audit_mcp.sections import lookup_section, normalize_section_ref


class AuditArtifactInput(BaseModel):
    """Input model for bayyinah_audit_artifact."""

    model_config = ConfigDict(extra="forbid")

    artifact_text: str | None = Field(
        default=None,
        description="Inline artifact text to audit.",
    )
    artifact_path: str | None = Field(
        default=None,
        description="Root-relative or absolute artifact path.",
    )
    artifact_name: str | None = Field(
        default=None,
        description="Human-readable artifact name.",
    )
    artifact_kind: str = Field(
        default="document",
        description="Artifact type, such as document, code, invoice, report, or prompt.",
    )
    audit_goal: str = Field(
        default="Run a Bayyinah structural honesty audit.",
        description="Specific audit objective for the calling agent.",
    )
    section_refs: list[str] = Field(
        default_factory=list,
        description="Optional section references to emphasize, such as ['9.1', '14.5'].",
    )
    include_framework_prompt: bool = Field(
        default=True,
        description="Include BAYYINAH_FRAMEWORK_PROMPT text when configured.",
    )
    max_artifact_chars: int = Field(
        default=12000,
        ge=1000,
        le=100000,
        description="Maximum inline artifact characters to include in the prompt scaffold.",
    )


class AuditArtifactOutput(TypedDict):
    status: str
    tool: str
    audit_prompt: str
    framework_prompt_loaded: bool
    artifact_descriptor: str
    section_refs: list[str]
    warnings: list[str]


def _read_text(path: Path, max_chars: int) -> tuple[str, str | None]:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        return "", f"Could not read artifact_path '{path}': {exc}"

    if len(text) > max_chars:
        return (
            text[:max_chars],
            f"Artifact text was truncated to {max_chars} characters for prompt size control.",
        )

    return text, None


def _read_framework_prompt(path: Path | None) -> tuple[str, bool, str | None]:
    if path is None:
        return "", False, None

    try:
        text = path.expanduser().read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        return "", False, f"Could not read BAYYINAH_FRAMEWORK_PROMPT '{path}': {exc}"

    return text, True, None


def _section_context(section_refs: list[str]) -> tuple[list[str], str]:
    normalized_refs: list[str] = []
    lines: list[str] = []

    for ref in section_refs:
        normalized = normalize_section_ref(ref)
        normalized_refs.append(normalized)
        found = lookup_section(normalized)
        if found["status"] == "ok":
            lines.append(
                f"- §{found['section_ref']} - {found['title']}: {found['summary']}"
            )
        else:
            lines.append(f"- §{normalized} - not in loaded section index")

    if not lines:
        lines.append("- No section emphasis provided. Use the full Bayyinah audit lens.")

    return normalized_refs, "\n".join(lines)


def bayyinah_audit_artifact(request: AuditArtifactInput) -> AuditArtifactOutput:
    """Return a provider-neutral Bayyinah audit prompt scaffold."""

    config = load_config()
    warnings: list[str] = []
    artifact_body = request.artifact_text or ""
    artifact_source = "inline artifact_text"
    artifact_path_given = bool(request.artifact_path)
    artifact_path_read = False

    if request.artifact_path:
        try:
            path = resolve_path(request.artifact_path, config)
        except ValueError as exc:
            warnings.append(str(exc))
        else:
            artifact_source = str(path)
            artifact_path_read = True
            artifact_body_from_file, warning = _read_text(
                path, request.max_artifact_chars
            )
            if warning:
                warnings.append(warning)
            if artifact_body_from_file:
                artifact_body = artifact_body_from_file
            elif not warning:
                warnings.append(f"artifact_path '{path}' was read but the file was empty.")

    if not artifact_body:
        if not artifact_path_given:
            warnings.append(
                "No artifact_text or artifact_path was provided. "
                "The scaffold still instructs the calling agent how to run the audit."
            )
        elif not artifact_path_read:
            warnings.append(
                "artifact_path was provided but could not be read. "
                "The scaffold still instructs the calling agent how to run the audit."
            )

    framework_text = ""
    framework_loaded = False
    if request.include_framework_prompt:
        framework_text, framework_loaded, framework_warning = _read_framework_prompt(
            config.framework_prompt
        )
        if framework_warning:
            warnings.append(framework_warning)

    normalized_refs, section_context = _section_context(request.section_refs)

    artifact_name = request.artifact_name or artifact_source
    artifact_descriptor = (
        f"name={artifact_name}; kind={request.artifact_kind}; source={artifact_source}"
    )

    framework_block = (
        framework_text
        if framework_loaded
        else "No external framework prompt configured. Use the section context and Bayyinah output contract below."
    )

    artifact_block = (
        artifact_body
        if artifact_body
        else "[Artifact content not embedded. Request it from the MCP client context or inspect artifact_path if available.]"
    )

    audit_prompt = f"""You are acting as a Bayyinah Audit Framework evaluator.

Goal:
{request.audit_goal}

Artifact descriptor:
{artifact_descriptor}

Relevant Bayyinah sections:
{section_context}

Framework prompt / governing instructions:
{framework_block}

Artifact to evaluate:
~~~text
{artifact_block}
~~~

Required audit behavior:
1. Compare visible claims, hidden assumptions, source attributions, section references, and structural consistency.
2. Do not invent evidence. If a needed source or substrate is unavailable, state that explicitly.
3. Use Bayyinah finding format exactly:
   - severity: HIGH | MED | LOW
   - section_ref: string
   - message: concise finding
   - location: artifact location, section, line, page, field, or "global"
4. Separate confirmed findings from cautions and unavailable checks.
5. If no findings are present, return an empty findings list and explain what was checked.
"""

    return {
        "status": "ok",
        "tool": "bayyinah_audit_artifact",
        "audit_prompt": audit_prompt,
        "framework_prompt_loaded": framework_loaded,
        "artifact_descriptor": artifact_descriptor,
        "section_refs": normalized_refs,
        "warnings": warnings,
    }

# Bismillah ir-Rahman ir-Rahim