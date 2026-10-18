# Bismillah ir-Rahman ir-Rahim

# R0509 -- file_router.py — FileRouter — each tribe knowing its drinking-place (Al-Baqarah 2:60).

**Chronological Index:** 793 of 995  
**Date:** Undated  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** file_router.py  
**Source Format:** py  
**SHA-256:** `ff7f5a591c10dc943abf906e5b5330c134688a6a6c68b32304ce839c04096214`  

---

## R0509 · file_router.py — FileRouter — each tribe knowing its drinking-place (Al-Baqarah 2:60).

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: file_router.py
- source_format: py
- text_sha256: ff7f5a591c10dc943abf906e5b5330c134688a6a6c68b32304ce839c04096214

"""
FileRouter — each tribe knowing its drinking-place (Al-Baqarah 2:60).

    قَدْ عَلِمَ كُلُّ أُنَاسٍ مَّشْرَبَهُمْ
    "Each tribe knew its drinking-place."

The architectural reading: Bayyinah will eventually accept PDF, DOCX,
HTML, Markdown, JSON, images, and code files. Each needs its own
parser — there is no single "document" extractor. The FileRouter
inspects a file (magic bytes first, extension as a hint, contents
disagreement flagged) and routes it to the right client. Phase 3
implements PDF dispatch; the other file types are classified
correctly but return ``UnsupportedFileType`` when a client is
requested — the signalling is honest about what the scanner can
currently drink from.

The router distinguishes:

    FileKind    — what the file IS, based on bytes + extension
    client_for  — the appropriate adapter, or raises UnsupportedFileType
    detect      — type detection without committing to a client

It also surfaces extension/content mismatches (a ``.pdf`` file whose
bytes are really ZIP is a strong signal in itself — polyglot files
are a known adversarial pattern).
"""

from __future__ import annotations

import enum
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from domain.exceptions import BayyinahError, PDFParseError
from infrastructure.pdf_client import PDFClient


# ---------------------------------------------------------------------------
# Router-specific exceptions
# ---------------------------------------------------------------------------

class UnsupportedFileType(BayyinahError):
    """The file was identified but Bayyinah has no client for it yet.

    Raised by ``FileRouter.client_for`` when asked to open a file whose
    type is recognised but whose parser path is not yet implemented.
    This is distinct from ``PDFParseError`` — the file is not *broken*,
    it is *out of scope*.
    """


class UnknownFileType(BayyinahError):
    """The file's type could not be identified from either magic bytes
    or extension. Distinct from UnsupportedFileType: we do not know
    *what* this file is, not merely that we cannot open it."""


# ---------------------------------------------------------------------------
# FileKind — closed enumeration of every file class Bayyinah recognises
# ---------------------------------------------------------------------------

class FileKind(enum.Enum):
    """File classes Bayyinah is designed to scan.

    This enumeration matches the project scope declared in the Bayyinah
    charter. Values are stable strings suitable for logging and for
    future serialisation — do not renumber.
    """

    PDF = "pdf"
    DOCX = "docx"
    # Phase 17 — XLSX is the spreadsheet analogue of DOCX: an Office Open
    # XML ZIP with its own set of parts (xl/workbook.xml, xl/worksheets/*,
    # xl/sharedStrings.xml, xl/vbaProject.bin, xl/embeddings/*, etc.). Like
    # DOCX the router disambiguates ZIP-magic files by extension; the
    # XlsxAnalyzer is the client the router's dispatch now routes to.
    XLSX = "xlsx"
    # Phase 18 — PPTX is the presentation analogue of DOCX / XLSX: an
    # Office Open XML ZIP with its own set of parts (ppt/presentation.xml,
    # ppt/slides/slide*.xml, ppt/notesSlides/notesSlide*.xml,
    # ppt/slideMasters/*, ppt/slideLayouts/*, ppt/vbaProject.bin,
    # ppt/embeddings/*, ppt/revisions/*, ppt/externalLinks/*, customXml/*,
    # etc.). The router disambiguates ZIP-magic files by extension or by
    # an ``ppt/presentation.xml`` marker visible in the head of the
    # archive; the PptxAnalyzer is the client this dispatch routes to.
    # Al-Baqarah 2:79: the verse describes the presentation-file attack
    # surface exactly — structured slides that look trustworthy while
    # carrying hidden speaker notes, macros, embedded objects, and
    # revision data.
    PPTX = "pptx"
    HTML = "html"
    MARKDOWN = "markdown"
    JSON = "json"
    IMAGE_PNG = "image_png"
    IMAGE_JPEG = "image_jpeg"
    # Phase 10 — SVG is a vector image by purpose but XML by substrate.
    # Routed separately from PNG/JPEG (binary raster) so SvgAnalyzer can
    # apply the XML/text mechanism set while ImageAnalyzer applies the
    # raster-chunk mechanism set. The two share the image FileKind prefix
    # to signal intent to downstream code without conflating the parsers.
    IMAGE_SVG = "image_svg"
    CODE = "code"
    # Phase 19 — RFC 5322 email message (.eml). Emails are the format
    # that most literally ships different content to different audiences
    # (Al-Baqarah 2:42: "do not mix truth with falsehood"): the reader
    # sees the rendered HTML body, the filter sees the text/plain body,
    # the headers carry routing/spoofing metadata, and attachments
    # carry their own nested document graphs. The router distinguishes
    # .eml from the text-family kinds so EmlAnalyzer can apply the
    # MIME-aware mechanism set (multipart/alternative divergence,
    # display-name spoofing, smuggled headers, nested .eml, attachment
    # recursion) while the text analyzers stay focused on raw decoded
    # text. Detection is header-shape + extension — the canonical
    # RFC 5322 header names ("From:", "To:", "Subject:", "Received:",
    # "Message-ID:", "MIME-Version:", "Return-Path:", "Delivered-To:",
    # or the mbox "From " line) at the top of the file are sufficient
    # to route an email reliably.
    EML = "eml"
    # Phase 20 — CSV / TSV / delimited data file. Al-Baqarah 2:42: "do
    # not mix truth with falsehood, nor conceal the truth while you
    # know it." CSV is the format where the parser and the human
    # disagree most literally — parsers silently skip comment rows,
    # silently misalign mismatched columns, silently reinterpret the
    # BOM in the first field, silently truncate at null bytes — while
    # the human sees only the rendered grid and trusts it. The
    # delimited-data FileKind covers ``.csv`` (comma), ``.tsv`` (tab),
    # and ``.psv`` (pipe) under a single kind because the underlying
    # attack surface (formula injection in cells, comment rows,
    # encoding anomalies, delimiter manipulation) is identical across
    # separators — CsvAnalyzer detects the delimiter at scan time.
    CSV = "csv"
    UNKNOWN = "unknown"


# ---------------------------------------------------------------------------
# Detection result
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class FileTypeDetection:
    """Result of ``FileRouter.detect``.

    Fields
    ------
    kind
        Best-guess classification of the file.
    reason
        Human-readable explanation of how ``kind`` was determined
        ("PDF magic header at byte 0"; "extension .md with no
        magic-byte signature"; etc.).
    extension_mismatch
        True when the file's bytes indicate a different type than its
        extension would suggest. Polyglot files (.pdf with a ZIP
        header, .png with HTML inside) are a known adversarial pattern
        — callers can surface this as a structural finding without
        loading a parser.
    """

    kind: FileKind
    reason: str
    extension_mismatch: bool = False


# ---------------------------------------------------------------------------
# Detection primitives
# ---------------------------------------------------------------------------

# Magic-byte prefixes, ordered by specificity.
_MAGIC_PREFIXES: list[tuple[bytes, FileKind, str]] = [
    (b"%PDF-",                     FileKind.PDF,        "PDF %PDF- header"),
    (b"\x89PNG\r\n\x1a\n",         FileKind.IMAGE_PNG,  "PNG 8-byte signature"),
    (b"\xff\xd8\xff",              FileKind.IMAGE_JPEG, "JPEG SOI marker"),
]

# Extensions, lower-cased without the leading dot.
_EXT_MAP: dict[str, FileKind] = {
    "pdf":      FileKind.PDF,
    "docx":     FileKind.DOCX,
    "xlsx":     FileKind.XLSX,
    "pptx":     FileKind.PPTX,
    "html":     FileKind.HTML,
    "htm":      FileKind.HTML,
    "md":       FileKind.MARKDOWN,
    "markdown": FileKind.MARKDOWN,
    "json":     FileKind.JSON,
    "png":      FileKind.IMAGE_PNG,
    "jpg":      FileKind.IMAGE_JPEG,
    "jpeg":     FileKind.IMAGE_JPEG,
    "svg":      FileKind.IMAGE_SVG,
    "svgz":     FileKind.IMAGE_SVG,  # gzipped SVG; decoding deferred to analyzer
    # Phase 19 — .eml is the canonical RFC 5322 email extension.
    # Microsoft Outlook's .msg is a compound OLE binary and deliberately
    # NOT routed here — .msg is a different format (a DOCX-era CFB
    # container), and giving it its own FileKind would smuggle CFB-parsing
    # responsibility into the email analyzer. The router stays honest
    # about what it classifies.
    "eml":      FileKind.EML,
    # Phase 20 — delimited-data extensions. ``.csv`` is the canonical
    # comma-separated form; ``.tsv`` is tab-separated; ``.psv`` is the
    # pipe-separated variant occasionally seen in data-engineering
    # exports. All three map to FileKind.CSV because the analyzer's
    # delimiter is inferred from content, not from the extension — the
    # same CsvAnalyzer handles all three, and the router does not need
    # to distinguish them at classification time. ``.txt`` deliberately
    # stays mapped to CODE; a file explicitly called ``.txt`` is the
    # general-purpose text family (flat prose, logs, notes), not a
    # tabular export, and misrouting it to the CSV analyzer would
    # fire delimiter / column-count findings on prose.
    "csv":      FileKind.CSV,
    "tsv":      FileKind.CSV,
    "psv":      FileKind.CSV,
    # Plain-text family — no dedicated FileKind today, so txt joins
    # the CODE bucket. TextFileAnalyzer's supported_kinds already
    # includes CODE, so the dispatch is correct; semantically "code"
    # means "raw decoded text the Unicode concealment detectors apply
    # to verbatim", which is exactly what a .txt file is.
    "txt":      FileKind.CODE,
    # Code file extensions that the future code-scanner will consume.
    "py":       FileKind.CODE,
    "js":       FileKind.CODE,
    "ts":       FileKind.CODE,
    "tsx":      FileKind.CODE,
    "jsx":      FileKind.CODE,
    "go":       FileKind.CODE,
    "rs":       FileKind.CODE,
    "java":     FileKind.CODE,
    "c":        FileKind.CODE,
    "cpp":      FileKind.CODE,
    "h":        FileKind.CODE,
    "hpp":      FileKind.CODE,
    "rb":       FileKind.CODE,
    "sh":       FileKind.CODE,
}


def _detect_docx(head: bytes, path: Path) -> bool:
    """DOCX is a ZIP with a specific entry. Heuristic: ZIP magic +
    .docx extension. Full structural validation is the job of the
    future DOCX client; the router only needs to classify."""
    return head.startswith(b"PK\x03\x04") and path.suffix.lower() == ".docx"


def _detect_xlsx(head: bytes, path: Path) -> bool:
    """XLSX is a ZIP with a specific entry set. Heuristic: ZIP magic +
    .xlsx extension, OR ZIP magic + a recognisable ``xl/`` part visible
    in the first ``HEAD_BYTES`` of the archive.

    The byte-sniff complements the extension check so an XLSX renamed
    to ``.zip`` (or a polyglot that lies about its extension) still
    surfaces as XLSX when the archive's early table of local file
    headers mentions ``xl/workbook.xml``. In practice most XLSX files
    put the workbook part near the head of the archive, so the bounded
    head read is enough for classification; deeper structural validation
    is the XlsxAnalyzer's job.
    """
    if not head.startswith(b"PK\x03\x04"):
        return False
    if path.suffix.lower() == ".xlsx":
        return True
    # Byte-sniff fallback: the XLSX workbook part is commonly named
    # ``xl/workbook.xml`` and is referenced from the local file headers
    # within the first few KB of the archive.
    return b"xl/workbook.xml" in head


def _detect_pptx(head: bytes, path: Path) -> bool:
    """PPTX is a ZIP with a specific entry set. Heuristic: ZIP magic +
    .pptx extension, OR ZIP magic + a recognisable ``ppt/`` part visible
    in the first ``HEAD_BYTES`` of the archive.

    Mirrors the ``_detect_xlsx`` / ``_detect_docx`` idiom exactly — each
    Office Open XML family has one canonical part that appears in the
    local file header table near the head of the archive
    (``ppt/presentation.xml`` for PPTX). The bounded head read is
    sufficient for classification; deeper structural validation is the
    PptxAnalyzer's job.
    """
    if not head.startswith(b"PK\x03\x04"):
        return False
    if path.suffix.lower() == ".pptx":
        return True
    return b"ppt/presentation.xml" in head


def _detect_html(head: bytes) -> bool:
    """HTML by content sniff (case-insensitive)."""
    stripped = head.lstrip().lower()
    return stripped.startswith((b"<!doctype html", b"<html", b"<body", b"<head"))


def _detect_svg(head: bytes) -> bool:
    """SVG by content sniff (case-insensitive).

    Two accepted prefixes:
      * ``<svg``  — raw SVG without XML prolog
      * ``<?xml`` followed by ``<svg`` within the first 1 KB — the common
        form produced by Inkscape / editors.

    An ``<?xml`` prolog without any ``<svg`` element falls through to
    the extension-based classification — a plain XML file is not an SVG
    and the current scanner routes it through the text-file path via
    the CODE kind.
    """
    stripped = head.lstrip().lower()
    if stripped.startswith(b"<svg"):
        return True
    if stripped.startswith(b"<?xml"):
        # Bounded search — a legitimate SVG declares <svg within a few
        # hundred bytes of the prolog. 1 KB is generous.
        if b"<svg" in stripped[:1024]:
            return True
    return False


# Phase 20 — delimited-data content sniff. A CSV/TSV doesn't have a
# magic header; the closest-to-reliable heuristic is "the first line
# contains the same delimiter at least twice AND the next several lines
# repeat that same delimiter with a consistent count". We restrict the
# delimiter set to the three most common (``,``, ``\t``, ``|``) so
# delimited-data files don't steal classification from prose that
# happens to contain commas. The sniff is deliberately conservative:
# the extension map above handles ``.csv`` / ``.tsv`` / ``.psv`` the
# vast majority of the time, and this sniff only exists to catch
# delimited data that has been misnamed or stripped of its extension.
def _detect_csv(head: bytes) -> bool:
    """Heuristic CSV / TSV / PSV detection.

    Rules:
      * The first non-empty, non-comment line contains at least one of
        ``,``, ``\\t``, or ``|``.
      * The same delimiter appears at least twice in that line (so we
        do not match prose that merely contains one comma).
      * At least two further non-empty lines in the head repeat the
        same delimiter count within ±1 (so we do not match prose that
        contains varying comma counts per sentence).

    The sniff rejects:
      * Binary files (any null byte inside the first 4 KB).
      * Lines that look like markup / HTML (start with ``<``).

    The detected delimiter itself is not returned — the analyzer
    re-infers it from the bytes it reads. The router only needs a
    boolean classification.
    """
    # Quick reject: null bytes inside a reasonable prefix indicate
    # binary data. CSV/TSV are always text.
    if b"\x00" in head[:4096]:
        return False
    try:
        text = head.decode("utf-8", errors="strict")
    except UnicodeDecodeError:
        # Try a permissive decode — a CSV with a couple of Latin-1
        # stragglers is still a CSV. If the whole prefix is unreadable,
        # it's not CSV.
        try:
            text = head.decode("latin-1", errors="strict")
        except UnicodeDecodeError:
            return False

    # Strip a UTF-8 BOM if present; it should not count as content.
    if text.startswith("\ufeff"):
        text = text[1:]

    lines = text.splitlines()
    # Take the first few non-empty, non-comment lines.
    content_lines: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            continue
        if stripped.startswith("<"):
            # HTML / XML shape — not CSV.
            return False
        content_lines.append(line)
        if len(content_lines) >= 6:
            break

    if len(content_lines) < 2:
        return False

    first = content_lines[0]
    # Try each candidate delimiter in descending order of specificity.
    # Tab first because tabs inside prose are very rare; then pipe
    # (same reasoning); then comma (commas do appear in prose, so the
    # count check below is the real guard).
    for delim in ("\t", "|", ","):
        first_count = first.count(delim)
        if first_count < 2:
            continue
        matching = 0
        for line in content_lines[1:]:
            count = line.count(delim)
            # Allow ±1 slack to tolerate a trailing delimiter or a
            # legitimately-quoted delimiter inside a field.
            if abs(count - first_count) <= 1:
                matching += 1
        # Require the majority of the sampled lines to agree on the
        # delimiter count.
        if matching >= max(2, (len(content_lines) - 1) // 2):
            return True
    return False


def _detect_json(head: bytes) -> bool:
    """Try parsing the first ~64 KB as JSON."""
    stripped = head.lstrip()
    if not stripped.startswith((b"{", b"[")):
        return False
    try:
        json.loads(head.decode("utf-8", errors="strict"))
        return True
    except Exception:  # noqa: BLE001 — json/unicode can raise either
        return False


# Canonical RFC 5322 header names that are highly specific to email.
# Detection requires at least one of these at the very start of the file
# (optionally preceded by the mbox ``From `` envelope line), followed by
# a colon. The list is deliberately conservative — generic header names
# like ``Content-Type:`` appear in HTTP captures and raw MIME fragments
# too, so we key detection off headers that only appear in real mail.
_EML_HEADER_NAMES: frozenset[bytes] = frozenset({
    b"from:",
    b"to:",
    b"cc:",
    b"bcc:",
    b"subject:",
    b"date:",
    b"message-id:",
    b"mime-version:",
    b"received:",
    b"return-path:",
    b"delivered-to:",
    b"reply-to:",
    b"sender:",
    b"x-mailer:",
    b"x-originating-ip:",
    b"dkim-signature:",
    b"authentication-results:",
    b"list-unsubscribe:",
    b"in-reply-to:",
    b"references:",
})


def _detect_eml(head: bytes) -> bool:
    """RFC 5322 email detection by header-shape sniff.

    Rules (first rule to match wins):

      1. An mbox envelope line (``From `` — note the trailing space, not
         a colon) at the very start. Rare in modern single-message
         ``.eml`` dumps but accepted so archived mailboxes classify.
      2. The first non-empty line is a known email header name followed
         by ``:``. Case-insensitive. We only look at the first line so
         a file that happens to contain header-shaped text in its middle
         (a forwarded-email quote in an HTML document, say) does not
         misclassify.

    The header name set in ``_EML_HEADER_NAMES`` is deliberately
    conservative: generic MIME headers like ``Content-Type:`` are
    excluded because they also appear at the start of raw MIME fragments
    and HTTP response captures — not emails. The names retained are
    specific enough that their presence at byte 0 is reliable evidence
    of a mail message.
    """
    # Strip leading whitespace to tolerate the occasional empty line at
    # the head of a saved message.
    stripped = head.lstrip(b"\r\n\t ")
    if not stripped:
        return False

    # Mbox envelope line.
    if stripped.startswith(b"From "):
        return True

    # First line of the stripped head.
    newline_idx = stripped.find(b"\n")
    first_line = stripped if newline_idx == -1 else stripped[:newline_idx]
    # Trim trailing CR.
    first_line = first_line.rstrip(b"\r")
    # Isolate the header-name portion up to the first colon.
    colon_idx = first_line.find(b":")
    if colon_idx <= 0:
        return False
    header_name = first_line[: colon_idx + 1].lower().strip()
    return header_name in _EML_HEADER_NAMES


# Extensions that we consider "plain-text family"; a content sniff
# treats these as their declared kind rather than UNKNOWN when no
# magic bytes fire.
_TEXT_FAMILY_KINDS: frozenset[FileKind] = frozenset({
    FileKind.HTML,
    FileKind.MARKDOWN,
    FileKind.JSON,
    FileKind.CODE,
    # SVG is XML text — an .svg file that starts with whitespace or a
    # comment won't match the content sniff, but the extension is
    # authoritative enough to route it to the SVG analyzer.
    FileKind.IMAGE_SVG,
    # Phase 19 — EML. An .eml that somehow fails the header sniff (e.g.
    # a saved message that starts with a blank line before any header)
    # still routes to EmlAnalyzer via the extension. The analyzer's own
    # error path will surface a parse failure as scan_error — the honest
    # signal that the extension and content disagree at a structural
    # level.
    FileKind.EML,
    # Phase 20 — delimited-data family. An extension-classified ``.csv``
    # / ``.tsv`` / ``.psv`` always routes to the CSV analyzer, which
    # handles its own content-level checks (delimiter inference, BOM,
    # encoding, formula injection, etc.). A file whose extension
    # disagrees with its contents (e.g. a ZIP that pretends to be a
    # CSV) will surface the mismatch when the analyzer itself detects
    # the binary shape — the router stays honest.
    FileKind.CSV,
})


# ---------------------------------------------------------------------------
# FileRouter
# ---------------------------------------------------------------------------

class FileRouter:
    """Identify a file's type and return a client for scanning it.

    Detection order (first to fire wins):
        1. Magic bytes at file start (PDF, PNG, JPEG, DOCX-as-ZIP).
        2. Content sniff for HTML / JSON.
        3. File extension.
        4. ``FileKind.UNKNOWN``.

    Extension mismatch is flagged when magic-byte detection disagrees
    with the extension's implied kind. Callers can surface this as an
    integrity signal independent of any parser (a ``.pdf`` that is
    really ZIP is adversarial before a single byte is interpreted).
    """

    # Amount of file head to read for content sniffing. 64 KB is enough
    # for every format we detect; larger reads waste I/O on huge files.
    HEAD_BYTES = 64 * 1024

    # ------------------------------------------------------------------
    # Detection
    # ------------------------------------------------------------------

    def detect(self, path: Path) -> FileTypeDetection:
        """Classify ``path`` without opening any parser.

        Does a single bounded read of the file head. Raises ``OSError``
        subclasses (``FileNotFoundError``, ``PermissionError``, etc.)
        if the path is unreadable — those are programmer errors, not
        Bayyinah errors, and should not be swallowed.
        """
        path = Path(path)
        try:
            with path.open("rb") as fh:
                head = fh.read(self.HEAD_BYTES)
        except FileNotFoundError:
            raise
        except OSError:
            raise

        ext = path.suffix.lower().lstrip(".")
        ext_kind = _EXT_MAP.get(ext, FileKind.UNKNOWN)

        # 1. Magic-byte detection.
        for prefix, kind, reason in _MAGIC_PREFIXES:
            if head.startswith(prefix):
                mismatch = ext_kind is not FileKind.UNKNOWN and ext_kind is not kind
                return FileTypeDetection(
                    kind=kind,
                    reason=reason,
                    extension_mismatch=mismatch,
                )

        # DOCX needs the extension hint to separate it from other ZIPs.
        if _detect_docx(head, path):
            return FileTypeDetection(
                kind=FileKind.DOCX,
                reason="ZIP container with .docx extension",
                extension_mismatch=False,
            )

        # XLSX — same shape as DOCX, different parts. The sniff accepts
        # either the ``.xlsx`` extension or an ``xl/workbook.xml`` marker
        # in the head of the archive. Ordered after DOCX so a ``.docx``
        # never falls through to the XLSX branch.
        if _detect_xlsx(head, path):
            mismatch = ext_kind not in (FileKind.XLSX, FileKind.UNKNOWN)
            return FileTypeDetection(
                kind=FileKind.XLSX,
                reason=(
                    "ZIP container with .xlsx extension"
                    if path.suffix.lower() == ".xlsx"
                    else "ZIP container with xl/workbook.xml part"
                ),
                extension_mismatch=mismatch,
            )

        # PPTX — same shape as DOCX / XLSX, different parts. The sniff
        # accepts either the ``.pptx`` extension or a
        # ``ppt/presentation.xml`` marker in the head of the archive.
        # Ordered after XLSX so a ``.xlsx`` never falls through to the
        # PPTX branch. Al-Baqarah 2:79 — a presentation is trusted on
        # its surface (visible slides) while the archive may carry
        # hidden slides, macros, revision history, embedded objects,
        # external links, speaker-notes prompt injections, and slide-
        # master template payloads. The router classifies; PptxAnalyzer
        # enumerates the mechanisms.
        if _detect_pptx(head, path):
            mismatch = ext_kind not in (FileKind.PPTX, FileKind.UNKNOWN)
            return FileTypeDetection(
                kind=FileKind.PPTX,
                reason=(
                    "ZIP container with .pptx extension"
                    if path.suffix.lower() == ".pptx"
                    else "ZIP container with ppt/presentation.xml part"
                ),
                extension_mismatch=mismatch,
            )

        # 2. Content sniff for SVG / HTML / JSON.
        #
        # SVG runs first because an SVG with an XML prolog (<?xml ...> <svg>)
        # is legal XML that the HTML sniff happens not to match today,
        # but the precedence is kept explicit for defensibility: an SVG's
        # own element should always win over "unrecognised XML".
        if _detect_svg(head):
            mismatch = ext_kind not in (FileKind.IMAGE_SVG, FileKind.UNKNOWN)
            return FileTypeDetection(
                kind=FileKind.IMAGE_SVG,
                reason="SVG content sniff",
                extension_mismatch=mismatch,
            )

        if _detect_html(head):
            mismatch = ext_kind not in (FileKind.HTML, FileKind.UNKNOWN)
            return FileTypeDetection(
                kind=FileKind.HTML,
                reason="HTML content sniff",
                extension_mismatch=mismatch,
            )

        # EML — RFC 5322 message. Detected by a canonical header name at
        # byte 0 (or an mbox "From " envelope line). Ordered after HTML
        # so an HTML document that quotes an email header as its first
        # line does not misclassify; ordered before JSON so a well-formed
        # email whose body happens to contain leading JSON bytes cannot
        # pass the JSON parse test before the header sniff fires. Phase
        # 19 — the format that most literally mixes visible and hidden
        # content across audiences (Al-Baqarah 2:42).
        if _detect_eml(head):
            mismatch = ext_kind not in (FileKind.EML, FileKind.UNKNOWN)
            return FileTypeDetection(
                kind=FileKind.EML,
                reason="RFC 5322 header sniff",
                extension_mismatch=mismatch,
            )

        if _detect_json(head):
            mismatch = ext_kind not in (FileKind.JSON, FileKind.UNKNOWN)
            return FileTypeDetection(
                kind=FileKind.JSON,
                reason="JSON content sniff",
                extension_mismatch=mismatch,
            )

        # CSV / TSV / PSV — delimited-data content sniff. Ordered after
        # JSON so a JSON array of strings containing commas doesn't
        # race ahead of its own JSON parse; ordered before the generic
        # text-family fall-through so a delimited-data file without a
        # recognised extension still routes to CsvAnalyzer instead of
        # UNKNOWN. Phase 20 — Al-Baqarah 2:42: the parser and the
        # human reading must not see different things.
        if _detect_csv(head):
            mismatch = ext_kind not in (FileKind.CSV, FileKind.UNKNOWN)
            return FileTypeDetection(
                kind=FileKind.CSV,
                reason="delimited-data content sniff",
                extension_mismatch=mismatch,
            )

        # 3. Extension-based fall-through for text-family kinds.
        if ext_kind in _TEXT_FAMILY_KINDS:
            return FileTypeDetection(
                kind=ext_kind,
                reason=f"extension .{ext} (no magic signature)",
                extension_mismatch=False,
            )

        # 4. Nothing matched.
        return FileTypeDetection(
            kind=FileKind.UNKNOWN,
            reason=(
                f"no magic signature and unrecognised extension "
                f"{ext or '(none)'!r}"
            ),
            extension_mismatch=False,
        )

    # ------------------------------------------------------------------
    # Client dispatch
    # ------------------------------------------------------------------

    def client_for(self, path: Path) -> PDFClient:
        """Return a ready-to-use client for ``path``.

        Phase 3 only implements the PDF path; every other recognised
        type raises ``UnsupportedFileType`` (honestly saying "we know
        what this is, we just don't scan it yet") and ``UNKNOWN`` raises
        ``UnknownFileType``. Callers should generally ``detect()`` first
        and branch on the result.

        The return type annotation is ``PDFClient`` because that's the
        only concrete client today. When DOCX / HTML clients land, the
        signature will widen to a Union — that is a *widening*, not a
        breaking change, and will be additive for existing callers.
        """
        detection = self.detect(path)

        if detection.kind is FileKind.PDF:
            return PDFClient(path)

        if detection.kind is FileKind.UNKNOWN:
            raise UnknownFileType(
                f"Could not identify {path}: {detection.reason}"
            )

        raise UnsupportedFileType(
            f"{path} identified as {detection.kind.value!r} "
            f"({detection.reason}); no client implemented yet. "
            "Supported kinds in Phase 3: PDF."
        )

    def is_supported(self, path: Path) -> bool:
        """Convenience — True if ``client_for`` would succeed."""
        try:
            self.client_for(path).close()
            return True
        except (UnsupportedFileType, UnknownFileType, PDFParseError):
            return False
        except OSError:
            return False


__all__ = [
    "FileRouter",
    "FileKind",
    "FileTypeDetection",
    "UnsupportedFileType",
    "UnknownFileType",
]

---

# Bismillah ir-Rahman ir-Rahim
