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
"""FastMCP server wiring for the Bayyinah Audit MCP server."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from mcp.server.fastmcp import FastMCP

from bayyinah_audit_mcp.tools.audit_artifact import bayyinah_audit_artifact
from bayyinah_audit_mcp.tools.check_attributions import bayyinah_check_attributions
from bayyinah_audit_mcp.tools.cross_vendor_audit import bayyinah_cross_vendor_audit
from bayyinah_audit_mcp.tools.furqan_lint import bayyinah_run_furqan_lint
from bayyinah_audit_mcp.tools.generate_round_report import (
    bayyinah_generate_round_report,
)
from bayyinah_audit_mcp.tools.list_sections import bayyinah_list_sections
from bayyinah_audit_mcp.tools.lookup_section import bayyinah_lookup_section

SERVER_NAME = "bayyinah-audit-mcp"

TOOL_REGISTRY: tuple[tuple[str, Callable[..., Any]], ...] = (
    ("bayyinah_audit_artifact", bayyinah_audit_artifact),
    ("bayyinah_run_furqan_lint", bayyinah_run_furqan_lint),
    ("bayyinah_check_attributions", bayyinah_check_attributions),
    ("bayyinah_cross_vendor_audit", bayyinah_cross_vendor_audit),
    ("bayyinah_lookup_section", bayyinah_lookup_section),
    ("bayyinah_list_sections", bayyinah_list_sections),
    ("bayyinah_generate_round_report", bayyinah_generate_round_report),
)

TOOL_NAMES: tuple[str, ...] = tuple(name for name, _ in TOOL_REGISTRY)


def _new_fastmcp(host: str, port: int) -> FastMCP:
    """Create a FastMCP instance while tolerating minor SDK constructor drift."""

    try:
        return FastMCP(SERVER_NAME, host=host, port=port)
    except TypeError:
        try:
            return FastMCP(SERVER_NAME, port=port)
        except TypeError:
            return FastMCP(SERVER_NAME)


def create_mcp(host: str = "127.0.0.1", port: int = 8000) -> FastMCP:
    """Create and register a fresh Bayyinah Audit MCP server."""

    mcp = _new_fastmcp(host=host, port=port)

    for name, func in TOOL_REGISTRY:
        mcp.tool(name=name)(func)

    return mcp

# Bismillah ir-Rahman ir-Rahim