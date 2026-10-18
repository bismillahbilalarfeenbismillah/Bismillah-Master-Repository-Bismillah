# Bismillah ir-Rahman ir-Rahim

# R0208 -- xz_protocol_source_frame.py — xz_protocol_source_frame.py -- Source-frame manifest for the XZ Protocol.

**Chronological Index:** 59 of 995  
**Date:** 2024-03-29  
**Section:** IV. XZ Protocol  
**Source File:** xz_protocol_source_frame.py  
**Source Format:** py  
**SHA-256:** `bbdf704599066fe15dd4af9ad626e7e78ef5862fa874a344cb606580e3283b13`  

---

## R0208 · xz_protocol_source_frame.py — xz_protocol_source_frame.py -- Source-frame manifest for the XZ Protocol.

- section: IV. XZ Protocol
- source_file: xz_protocol_source_frame.py
- source_format: py
- merged_variants: 2 (xz_protocol_source_frame.py.txt; xz_protocol_source_frame.txt)
- text_sha256: bbdf704599066fe15dd4af9ad626e7e78ef5862fa874a344cb606580e3283b13

"""
xz_protocol_source_frame.py -- Source-frame manifest for the XZ Protocol.

XZ Protocol v0.75, Section 5.1, FREEZE-BLOCKER FB-4.

This module defines the closed, enumerable list of public-record sources
that constitute the universe from which effect boundaries are enumerated.
No source outside this manifest may enter the primary enumeration. A
source discovered after the seal is appended as a deviation and cannot
enter the primary denominator.

Frame window:
  Start: 2023-10-01 (180 days before disclosure)
  End:   2024-04-28 (30 days after disclosure)
  Disclosure: 2024-03-29 (Andres Freund, oss-security)

This manifest is OPEN (Tier 1). It contains no restricted content,
no payload detail, no activation recipe, and no compromised binary.

Author of record: Bilal Syed Arfeen
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Optional


# ---------------------------------------------------------------------------
# Frame window (frozen)
# ---------------------------------------------------------------------------

DISCLOSURE_DATE = date(2024, 3, 29)
FRAME_START = date(2023, 10, 1)   # 180 days before disclosure
FRAME_END = date(2024, 4, 28)     # 30 days after disclosure
DISCLOSURE_URL = "https://www.openwall.com/lists/oss-security/2024/03/29/4"


# ---------------------------------------------------------------------------
# Source categories
# ---------------------------------------------------------------------------

class SourceCategory(Enum):
    REPOSITORY = "repository"
    RELEASE_ARCHIVE = "release-archive"
    DISTRIBUTION = "distribution"
    MAILING_LIST = "mailing-list"
    ADVISORY = "advisory"
    BUILD_INFRASTRUCTURE = "build-infrastructure"
    TRANSPARENCY_LOG = "transparency-log"


class AuthenticationMethod(Enum):
    """How to verify the source is authentic and unmodified."""
    GIT_HASH = "git-commit-hash"
    GPG_SIGNATURE = "gpg-signature"
    TLS_CERTIFICATE = "tls-certificate"
    ARCHIVE_CHECKSUM = "archive-checksum"
    DISTRIBUTION_SIGNATURE = "distribution-package-signature"
    INSTITUTIONAL_AUTHORITY = "institutional-authority"
    CONTENT_HASH = "content-hash-at-retrieval"


# ---------------------------------------------------------------------------
# Stratum coverage
# ---------------------------------------------------------------------------

class BoundaryStratum(Enum):
    S_COMMIT = "S-COMMIT"
    S_RELEASE = "S-RELEASE"
    S_BUILD = "S-BUILD"
    S_DISTRIBUTION = "S-DISTRIBUTION"
    S_INSTALLATION = "S-INSTALLATION"
    S_RUNTIME_AUTH = "S-RUNTIME-AUTH"


# ---------------------------------------------------------------------------
# Source record
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class SourceRecord:
    """One entry in the source-frame manifest."""
    source_id: str
    name: str
    category: SourceCategory
    url: str
    authentication: tuple[AuthenticationMethod, ...]
    strata_covered: frozenset[BoundaryStratum]
    retrieval_rule: str
    notes: Optional[str] = None


# ---------------------------------------------------------------------------
# THE MANIFEST (frozen, enumerable, closed)
# ---------------------------------------------------------------------------

SOURCE_FRAME_MANIFEST: tuple[SourceRecord, ...] = (

    # === REPOSITORIES ===

    SourceRecord(
        source_id="SRC-REPO-01",
        name="tukaani-project/xz (GitHub)",
        category=SourceCategory.REPOSITORY,
        url="https://github.com/tukaani-project/xz",
        authentication=(AuthenticationMethod.GIT_HASH, AuthenticationMethod.TLS_CERTIFICATE),
        strata_covered=frozenset({BoundaryStratum.S_COMMIT, BoundaryStratum.S_RELEASE}),
        retrieval_rule="git clone with full history; enumerate commits in frame window by author date; "
                       "record commit hash, author, committer, date, changed paths, and parent hashes",
    ),

    SourceRecord(
        source_id="SRC-REPO-02",
        name="tukaani-project/xz issue tracker (GitHub Issues)",
        category=SourceCategory.REPOSITORY,
        url="https://github.com/tukaani-project/xz/issues",
        authentication=(AuthenticationMethod.TLS_CERTIFICATE,),
        strata_covered=frozenset({BoundaryStratum.S_COMMIT, BoundaryStratum.S_RELEASE}),
        retrieval_rule="GitHub API: list issues and comments in frame window; "
                       "record issue number, author, timestamps, and body hashes",
        notes="Issue 103 is a primary XZ citation",
    ),

    # === RELEASE ARCHIVES ===

    SourceRecord(
        source_id="SRC-REL-01",
        name="xz.tukaani.org releases",
        category=SourceCategory.RELEASE_ARCHIVE,
        url="https://xz.tukaani.org/xz-utils/",
        authentication=(AuthenticationMethod.GPG_SIGNATURE, AuthenticationMethod.ARCHIVE_CHECKSUM),
        strata_covered=frozenset({BoundaryStratum.S_RELEASE}),
        retrieval_rule="Download all release tarballs and .sig files in frame window; "
                       "record filename, size, SHA-256, GPG verification result, "
                       "and signing key fingerprint",
    ),

    SourceRecord(
        source_id="SRC-REL-02",
        name="GitHub Releases (tukaani-project/xz)",
        category=SourceCategory.RELEASE_ARCHIVE,
        url="https://github.com/tukaani-project/xz/releases",
        authentication=(AuthenticationMethod.TLS_CERTIFICATE,),
        strata_covered=frozenset({BoundaryStratum.S_RELEASE}),
        retrieval_rule="GitHub API: list releases in frame window; "
                       "record tag, date, asset URLs, asset checksums",
    ),

    # === DISTRIBUTION CHANNELS ===

    SourceRecord(
        source_id="SRC-DIST-01",
        name="Debian package tracker (xz-utils)",
        category=SourceCategory.DISTRIBUTION,
        url="https://tracker.debian.org/pkg/xz-utils",
        authentication=(AuthenticationMethod.DISTRIBUTION_SIGNATURE,),
        strata_covered=frozenset({BoundaryStratum.S_DISTRIBUTION, BoundaryStratum.S_BUILD}),
        retrieval_rule="Query snapshot.debian.org for all xz-utils versions in frame window; "
                       "record version, upload date, suite, architecture, maintainer, "
                       "source package hash, build log URL",
    ),

    SourceRecord(
        source_id="SRC-DIST-02",
        name="Fedora Koji / Bodhi (xz)",
        category=SourceCategory.DISTRIBUTION,
        url="https://koji.fedoraproject.org/koji/packageinfo?packageID=xz",
        authentication=(AuthenticationMethod.DISTRIBUTION_SIGNATURE,),
        strata_covered=frozenset({BoundaryStratum.S_DISTRIBUTION, BoundaryStratum.S_BUILD}),
        retrieval_rule="Koji API: list builds for xz in frame window; "
                       "Bodhi API: list updates; record build ID, version, "
                       "task ID, completion date, update status",
    ),

    SourceRecord(
        source_id="SRC-DIST-03",
        name="Arch Linux packages (xz)",
        category=SourceCategory.DISTRIBUTION,
        url="https://archlinux.org/packages/core/x86_64/xz/",
        authentication=(AuthenticationMethod.DISTRIBUTION_SIGNATURE,),
        strata_covered=frozenset({BoundaryStratum.S_DISTRIBUTION}),
        retrieval_rule="Arch Linux Archive: list xz package versions in frame window; "
                       "record version, packager, build date, signature",
    ),

    SourceRecord(
        source_id="SRC-DIST-04",
        name="Ubuntu Launchpad (xz-utils)",
        category=SourceCategory.DISTRIBUTION,
        url="https://launchpad.net/ubuntu/+source/xz-utils",
        authentication=(AuthenticationMethod.DISTRIBUTION_SIGNATURE,),
        strata_covered=frozenset({BoundaryStratum.S_DISTRIBUTION, BoundaryStratum.S_BUILD}),
        retrieval_rule="Launchpad API: list published versions in frame window; "
                       "record version, series, pocket, date published, build URLs",
    ),

    SourceRecord(
        source_id="SRC-DIST-05",
        name="Alpine Linux packages (xz)",
        category=SourceCategory.DISTRIBUTION,
        url="https://pkgs.alpinelinux.org/packages?name=xz",
        authentication=(AuthenticationMethod.DISTRIBUTION_SIGNATURE,),
        strata_covered=frozenset({BoundaryStratum.S_DISTRIBUTION}),
        retrieval_rule="Alpine package index: list xz versions in frame window; "
                       "record version, branch, maintainer, build date",
    ),

    SourceRecord(
        source_id="SRC-DIST-06",
        name="Homebrew formulae (xz)",
        category=SourceCategory.DISTRIBUTION,
        url="https://formulae.brew.sh/formula/xz",
        authentication=(AuthenticationMethod.GIT_HASH, AuthenticationMethod.TLS_CERTIFICATE),
        strata_covered=frozenset({BoundaryStratum.S_DISTRIBUTION}),
        retrieval_rule="Homebrew/homebrew-core git history: list formula changes for xz "
                       "in frame window; record commit hash, version, bottle URLs",
    ),

    # === MAILING LISTS ===

    SourceRecord(
        source_id="SRC-ML-01",
        name="oss-security mailing list",
        category=SourceCategory.MAILING_LIST,
        url="https://www.openwall.com/lists/oss-security/",
        authentication=(AuthenticationMethod.TLS_CERTIFICATE, AuthenticationMethod.CONTENT_HASH),
        strata_covered=frozenset({BoundaryStratum.S_RELEASE, BoundaryStratum.S_RUNTIME_AUTH}),
        retrieval_rule="Retrieve all posts mentioning 'xz' or 'CVE-2024-3094' in frame window; "
                       "record message-id, date, author, subject, body hash",
        notes="Contains the primary disclosure (2024-03-29)",
    ),

    SourceRecord(
        source_id="SRC-ML-02",
        name="Distribution security announcement lists",
        category=SourceCategory.MAILING_LIST,
        url="(multiple; see retrieval rule)",
        authentication=(AuthenticationMethod.GPG_SIGNATURE, AuthenticationMethod.TLS_CERTIFICATE),
        strata_covered=frozenset({BoundaryStratum.S_DISTRIBUTION}),
        retrieval_rule="Retrieve security announcements for xz-utils/CVE-2024-3094 from: "
                       "debian-security-announce, fedora-package-announce, "
                       "arch-security, ubuntu-security-announce. "
                       "Record message-id, date, DSA/advisory ID, affected versions, fixed versions",
    ),

    # === ADVISORIES ===

    SourceRecord(
        source_id="SRC-ADV-01",
        name="NVD CVE-2024-3094",
        category=SourceCategory.ADVISORY,
        url="https://nvd.nist.gov/vuln/detail/cve-2024-3094",
        authentication=(AuthenticationMethod.INSTITUTIONAL_AUTHORITY,
                        AuthenticationMethod.TLS_CERTIFICATE),
        strata_covered=frozenset({BoundaryStratum.S_RELEASE, BoundaryStratum.S_RUNTIME_AUTH}),
        retrieval_rule="NVD API: retrieve full CVE record; "
                       "record published date, modified dates, CVSS, CWE, references, "
                       "affected version ranges",
        notes="Primary XZ citation",
    ),

    SourceRecord(
        source_id="SRC-ADV-02",
        name="GitHub Advisory GHSA-rxwq-x6h5-x525",
        category=SourceCategory.ADVISORY,
        url="https://github.com/advisories/GHSA-rxwq-x6h5-x525",
        authentication=(AuthenticationMethod.INSTITUTIONAL_AUTHORITY,
                        AuthenticationMethod.TLS_CERTIFICATE),
        strata_covered=frozenset({BoundaryStratum.S_RELEASE, BoundaryStratum.S_DISTRIBUTION}),
        retrieval_rule="GitHub Advisory API: retrieve full advisory; "
                       "record published date, severity, affected packages and versions, "
                       "references",
        notes="Primary XZ citation",
    ),

    # === BUILD INFRASTRUCTURE ===

    SourceRecord(
        source_id="SRC-BUILD-01",
        name="Debian snapshot.debian.org build logs",
        category=SourceCategory.BUILD_INFRASTRUCTURE,
        url="https://snapshot.debian.org/",
        authentication=(AuthenticationMethod.INSTITUTIONAL_AUTHORITY,
                        AuthenticationMethod.TLS_CERTIFICATE),
        strata_covered=frozenset({BoundaryStratum.S_BUILD}),
        retrieval_rule="Retrieve build logs for xz-utils source package versions "
                       "in frame window; record builder, build date, build dependencies, "
                       "configure flags, build result hash",
    ),

    SourceRecord(
        source_id="SRC-BUILD-02",
        name="Reproducible Builds project (xz-utils results)",
        category=SourceCategory.BUILD_INFRASTRUCTURE,
        url="https://reproducible-builds.org/",
        authentication=(AuthenticationMethod.TLS_CERTIFICATE,),
        strata_covered=frozenset({BoundaryStratum.S_BUILD}),
        retrieval_rule="Query reproducibility status for xz-utils versions in frame window; "
                       "record version, reproducibility verdict, diffoscope output URL if available",
        notes="Covers Debian reproducible-builds infrastructure",
    ),
)


# ---------------------------------------------------------------------------
# Manifest operations
# ---------------------------------------------------------------------------

def get_sources_for_stratum(stratum: BoundaryStratum) -> list[SourceRecord]:
    """Return all sources covering the given stratum."""
    return [s for s in SOURCE_FRAME_MANIFEST if stratum in s.strata_covered]


def get_source_by_id(source_id: str) -> Optional[SourceRecord]:
    """Look up a source by its ID."""
    for s in SOURCE_FRAME_MANIFEST:
        if s.source_id == source_id:
            return s
    return None


def validate_manifest() -> dict:
    """Validate manifest completeness and internal consistency."""
    errors = []

    # Core strata must have at least one source; installation/runtime may be empty
    core_strata = {BoundaryStratum.S_COMMIT, BoundaryStratum.S_RELEASE,
                   BoundaryStratum.S_BUILD, BoundaryStratum.S_DISTRIBUTION}
    for stratum in BoundaryStratum:
        sources = get_sources_for_stratum(stratum)
        if stratum in core_strata and not sources:
            errors.append(f"No sources cover core stratum {stratum.value}")

    # Source IDs must be unique
    ids = [s.source_id for s in SOURCE_FRAME_MANIFEST]
    if len(ids) != len(set(ids)):
        errors.append("Duplicate source IDs found")

    # All four primary XZ citations must appear
    primary_urls = {
        DISCLOSURE_URL,
        "https://nvd.nist.gov/vuln/detail/cve-2024-3094",
        "https://github.com/tukaani-project/xz/issues",
        "https://github.com/advisories/GHSA-rxwq-x6h5-x525",
    }
    manifest_urls = {s.url for s in SOURCE_FRAME_MANIFEST}
    # Check that primary citations are covered (exact or prefix match)
    for purl in primary_urls:
        if not any(purl in murl or murl in purl for murl in manifest_urls):
            errors.append(f"Primary citation not covered: {purl}")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "source_count": len(SOURCE_FRAME_MANIFEST),
        "strata_coverage": {
            s.value: len(get_sources_for_stratum(s))
            for s in BoundaryStratum
        },
        "frame_start": str(FRAME_START),
        "frame_end": str(FRAME_END),
        "disclosure_date": str(DISCLOSURE_DATE),
    }

---

# Bismillah ir-Rahman ir-Rahim
