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
Tier 2 detector for ``Received`` chain anomalies that contradict the
``From`` claim (v1.1.2 EML format gauntlet).

Each ``Received`` header captures one SMTP hop: ``from <claimed-host>
... by <relay-host>``. A legitimate message from
``billing@trusted-vendor.example`` should show at least one Received
hop whose ``from`` or ``by`` host sits in the same registered domain
as the From address - the vendor's outbound MTA put the message into
the wider relay graph somewhere. When the chain shows zero hops
through the From-domain's infrastructure and instead routes entirely
through unrelated relays (``relay.attacker.example``,
``internal.attacker.example``), the routing story contradicts the
identity story.

The reader never inspects the Received chain. It is a batin-layer
surface: prior-state routing concealed beneath the rendered sender
identity. This detector pairs structurally with
``eml_returnpath_from_mismatch`` - both surface envelope-vs-display
divergence, but at different headers (Return-Path = SMTP MAIL FROM
authority; Received = the actual hop graph).

Trigger: ``From`` parses to a valid address with a registered domain;
at least one ``Received`` header is present; and no Received hop's
``from <host>`` or ``by <host>`` clause names a host whose domain
matches (or is a subdomain of) the From domain.

Closes ``eml_gauntlet`` fixture ``03_received_chain_anomaly.eml``.

Tier discipline: Tier 2 structural. The trigger compares domain
substrings inside RFC 5321 ``from``/``by`` clauses against the From
domain - all byte-deterministic. The interpretation (this is a
spoofed sender or a hijacked relay) is not made by this detector.
"""
from __future__ import annotations

import email
import email.policy
import email.utils
import re
from pathlib import Path
from typing import Iterable

from domain.finding import Finding


_MAX_EML_BYTES: int = 16 * 1024 * 1024
_PREVIEW_LIMIT: int = 240

# Match ``from <host>`` and ``by <host>`` clauses inside a Received
# header. Hostnames may be followed by parenthesised IP info or end
# at a whitespace boundary; we keep only the bare hostname token.
_FROM_CLAUSE: re.Pattern[str] = re.compile(
    r"\bfrom\s+([A-Za-z0-9._\-]+)",
    re.IGNORECASE,
)
_BY_CLAUSE: re.Pattern[str] = re.compile(
    r"\bby\s+([A-Za-z0-9._\-]+)",
    re.IGNORECASE,
)


def _registered_domain(host: str) -> str:
    """Lower-cased domain - the last two labels of ``host``.

    For ``mx.relay.victim-corp.example`` this returns
    ``victim-corp.example``. Bare hosts (no dot) return the host
    unchanged. We match by suffix in the trigger so subdomain matches
    still pass.
    """
    h = host.strip().lower().rstrip(".")
    parts = [p for p in h.split(".") if p]
    if len(parts) >= 2:
        return ".".join(parts[-2:])
    return h


def _domain_of_address(address: str) -> str:
    if "@" not in address:
        return ""
    return address.rsplit("@", 1)[1].strip().lower().rstrip(">")


def detect_eml_received_chain_anomaly(file_path: Path) -> Iterable[Finding]:
    """Surface a ``From`` domain whose registered domain does not appear
    in any ``Received`` hop's ``from``/``by`` clause."""
    try:
        raw = file_path.read_bytes()
    except OSError:
        return

    if len(raw) > _MAX_EML_BYTES:
        raw = raw[:_MAX_EML_BYTES]

    try:
        msg = email.message_from_bytes(raw, policy=email.policy.default)
    except Exception:  # noqa: BLE001 - defensive
        return

    from_value = msg.get("From")
    if not from_value:
        return

    try:
        _, from_addr = email.utils.parseaddr(str(from_value))
    except Exception:  # noqa: BLE001 - defensive
        return
    if not from_addr:
        return

    from_domain_full = _domain_of_address(from_addr)
    if not from_domain_full:
        return
    from_reg = _registered_domain(from_domain_full)
    if not from_reg:
        return

    received_values = msg.get_all("Received") or []
    if not received_values:
        return

    hop_hosts: list[str] = []
    for received in received_values:
        text = str(received)
        for match in _FROM_CLAUSE.finditer(text):
            hop_hosts.append(match.group(1))
        for match in _BY_CLAUSE.finditer(text):
            hop_hosts.append(match.group(1))

    if not hop_hosts:
        return

    # Pass condition: any hop host shares the registered domain of From.
    for host in hop_hosts:
        host_reg = _registered_domain(host)
        if not host_reg:
            continue
        if host_reg == from_reg or host_reg.endswith("." + from_reg):
            return  # legitimate-shape chain
        if from_reg.endswith("." + host_reg):
            return  # From sits inside hop host's tree

    # Fail: chain never traverses the From-claimed domain.
    chain_preview = " | ".join(
        str(r)[:120] for r in received_values
    )[:_PREVIEW_LIMIT]
    hop_summary = ", ".join(sorted({_registered_domain(h) for h in hop_hosts if h}))[
        :_PREVIEW_LIMIT
    ]

    yield Finding(
        mechanism="eml_received_chain_anomaly",
        tier=2,
        confidence=0.85,
        description=(
            f"Received chain shows {len(received_values)} hop(s) through "
            f"infrastructure {{{hop_summary}}} - none of which match the "
            f"From-claimed registered domain {from_reg!r}. A message "
            f"from {from_addr!r} should traverse that domain's outbound "
            f"MTA in at least one Received hop. The routing story and "
            f"the identity story diverge - structural anomaly at the "
            f"prior-state routing layer."
        ),
        location=f"{file_path}:header:received",
        surface=f"From: {str(from_value)[:120]}",
        concealed=f"Received chain: {chain_preview}",
        source_layer="batin",
    )


__all__ = ["detect_eml_received_chain_anomaly"]

# Bismillah ir-Rahman ir-Rahim