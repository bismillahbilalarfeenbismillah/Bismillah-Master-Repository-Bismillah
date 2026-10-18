# Bismillah ir-Rahman ir-Rahim

# R0294 -- build_shvvp_v0_5_pdf.py — Render SHV_VALIDATION_PROTOCOL_v0_5_source.md to a monochrome academic PDF.

**Chronological Index:** 712 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** build_shvvp_v0_5_pdf.py  
**Source Format:** py  
**SHA-256:** `6b6bdaf359119b10f2d6ee7b39770b9afbb13d9b6dcb7288296390aae5f84109`  

---

## R0294 · build_shvvp_v0_5_pdf.py — Render SHV_VALIDATION_PROTOCOL_v0_5_source.md to a monochrome academic PDF.

- section: V. BSSG & SHVVP Protocols
- source_file: build_shvvp_v0_5_pdf.py
- source_format: py
- text_sha256: 6b6bdaf359119b10f2d6ee7b39770b9afbb13d9b6dcb7288296390aae5f84109

# -*- coding: utf-8 -*-
"""Render SHV_VALIDATION_PROTOCOL_v0_5_source.md to a monochrome academic PDF.

Design: strict greyscale ink only (no hue anywhere), embedded Source Serif 4
headings over Source Sans 3 body, clickable URLs, page footers, no decorative
elements. The canonical Markdown source is the single input; nothing is written
back to it.

Usage: python build_shvvp_v0_2_pdf.py
"""
import os
import re
import urllib.request

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, HRFlowable, Image,
                                KeepTogether, ListFlowable, ListItem, PageTemplate,
                                Paragraph, Spacer, Table, TableStyle)

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "SHV_VALIDATION_PROTOCOL_v0_5_source.md")
OUT = os.path.join(HERE, "SHV_VALIDATION_PROTOCOL_v0_5.pdf")

TITLE = "Structural Honesty Validation Protocol (SHVVP) v0.5"
AUTHOR = "Bilal Syed Arfeen"
SUBJECT = ("FROZEN preregistration, version 0.5. Evaluation contract for XZ construct "
           "validation, CVE-Bench effect control, and seeded novel-discovery stress testing. "
           "Versions 0.1, 0.2, 0.3 and 0.4 are HALTED and were never deposited. This version is "
           "NOT DEPOSITED and NOT BINDING pending a fresh two-family carrying audit.")
KEYWORDS = ("preregistration, structural honesty, SHVVP v0.5, noninferiority, CVE-Bench, "
            "XZ Utils, provenance, evidence independence")

# ---------------------------------------------------------------- fonts
FONT_DIR = "/tmp/shvvp_fonts"
os.makedirs(FONT_DIR, exist_ok=True)
FONTS = {
    "SerifBody": "https://github.com/google/fonts/raw/main/ofl/sourceserif4/SourceSerif4%5Bopsz%2Cwght%5D.ttf",
    "SerifItalic": "https://github.com/google/fonts/raw/main/ofl/sourceserif4/SourceSerif4-Italic%5Bopsz%2Cwght%5D.ttf",
    "SansBody": "https://github.com/google/fonts/raw/main/ofl/sourcesans3/SourceSans3%5Bwght%5D.ttf",
    "SansItalic": "https://github.com/google/fonts/raw/main/ofl/sourcesans3/SourceSans3-Italic%5Bwght%5D.ttf",
    "MonoBody": "https://github.com/google/fonts/raw/main/ofl/robotomono/RobotoMono%5Bwght%5D.ttf",
}


def static_instance(src_path, dst_path, weight, rename=None):
    """Materialise a static weight instance from a variable font."""
    if os.path.exists(dst_path):
        return True
    try:
        from fontTools import ttLib
        from fontTools.varLib import instancer
        font = ttLib.TTFont(src_path)
        if "fvar" not in font:
            return False
        axes = {a.axisTag: a for a in font["fvar"].axes}
        loc = {}
        if "wght" in axes:
            loc["wght"] = weight
        if "opsz" in axes:
            loc["opsz"] = 11
        inst = instancer.instantiateVariableFont(font, loc)
        if rename:
            # ReportLab caches font faces by the internal PostScript name, so a
            # bold instance carrying the regular name would silently reuse the
            # regular metrics. Rename the instance to keep the faces distinct.
            for rec in inst["name"].names:
                if rec.nameID in (1, 3, 4, 6, 16, 17):
                    inst["name"].setName(rename, rec.nameID, rec.platformID,
                                         rec.platEncID, rec.langID)
        inst.save(dst_path)
        return True
    except Exception as exc:  # pragma: no cover
        print("WARN instance", dst_path, exc)
        return False


ok = {}
for name, url in FONTS.items():
    path = os.path.join(FONT_DIR, name + ".ttf")
    if not os.path.exists(path):
        try:
            urllib.request.urlretrieve(url, path)
        except Exception as exc:  # pragma: no cover
            print("WARN download", name, exc)
    use = path
    if name in ("SerifBody", "SansBody", "MonoBody"):
        reg = os.path.join(FONT_DIR, name + "-400.ttf")
        if static_instance(path, reg, 400):
            use = reg
        bold_name = name.replace("Body", "Bold")
        bold_path = os.path.join(FONT_DIR, name + "-700.ttf")
        if static_instance(path, bold_path, 700, rename=bold_name + "SHVVP"):
            try:
                pdfmetrics.registerFont(TTFont(bold_name, bold_path))
                ok[bold_name] = True
            except Exception as exc:  # pragma: no cover
                print("WARN register", bold_name, exc)
    try:
        pdfmetrics.registerFont(TTFont(name, use))
        ok[name] = True
    except Exception as exc:  # pragma: no cover
        print("WARN register", name, exc)
        ok[name] = False

SERIF = "SerifBody" if ok.get("SerifBody") else "Times-Roman"
SERIF_I = "SerifItalic" if ok.get("SerifItalic") else "Times-Italic"
SANS = "SansBody" if ok.get("SansBody") else "Helvetica"
SANS_I = "SansItalic" if ok.get("SansItalic") else "Helvetica-Oblique"
MONO = "MonoBody" if ok.get("MonoBody") else "Courier"
SERIF_B = "SerifBold" if ok.get("SerifBold") else SERIF
SANS_B = "SansBold" if ok.get("SansBold") else SANS
for base, bold, ital in ((SERIF, SERIF_B, SERIF_I), (SANS, SANS_B, SANS_I)):
    pdfmetrics.registerFontFamily(base, normal=base, bold=bold, italic=ital,
                                  boldItalic=bold)
# Alias the base-14 names to embedded faces so no non-embedded font can appear.
if ok.get("SansBody"):
    for alias in ("Helvetica", "Helvetica-Bold", "Helvetica-Oblique",
                  "Helvetica-BoldOblique"):
        try:
            pdfmetrics.registerFont(TTFont(alias, os.path.join(FONT_DIR, "SansBody.ttf")))
        except Exception:
            pass

# ---------------------------------------------------------------- greyscale ink
INK = HexColor("#111111")
SOFT = HexColor("#3C3C3C")
MUTED = HexColor("#5A5A5A")
RULE = HexColor("#8C8C8C")
HDR_FILL = HexColor("#E8E8E8")
ZEBRA = HexColor("#F5F5F5")

ss = getSampleStyleSheet()


def St(name, **kw):
    kw.setdefault("parent", ss["Normal"])
    return ParagraphStyle(name, **kw)


s_title = St("title", fontName=SERIF, fontSize=18.5, leading=22.5, alignment=TA_CENTER,
             textColor=INK, spaceAfter=5)
s_sub = St("sub", fontName=SERIF_I, fontSize=11.5, leading=15, alignment=TA_CENTER,
           textColor=SOFT, spaceAfter=11)
s_author = St("author", fontName=SANS, fontSize=11, leading=14, alignment=TA_CENTER,
              textColor=INK, spaceAfter=2)
s_date = St("date", fontName=SANS, fontSize=9.5, leading=12.5, alignment=TA_CENTER,
            textColor=MUTED, spaceAfter=10)
s_h1 = St("h1", fontName=SERIF_B, fontSize=13.2, leading=16.5, textColor=INK,
          spaceBefore=13, spaceAfter=5, keepWithNext=1)
s_h2 = St("h2", fontName=SERIF_B, fontSize=11.3, leading=14.5, textColor=INK,
          spaceBefore=9, spaceAfter=4, keepWithNext=1)
s_body = St("body", fontName=SANS, fontSize=9.4, leading=13.4, alignment=TA_JUSTIFY,
            textColor=INK, spaceAfter=6)
s_bullet = St("bul", parent=s_body, leftIndent=13, spaceAfter=3.2, alignment=TA_LEFT)
s_caption = St("cap", fontName=SANS_I, fontSize=8.2, leading=11, alignment=TA_CENTER,
               textColor=MUTED, spaceBefore=3, spaceAfter=9)
s_tc = St("tc", fontName=SANS, fontSize=7.3, leading=9.4, textColor=INK, alignment=TA_LEFT)
s_th = St("th", fontName=SANS_B, fontSize=7.3, leading=9.4, textColor=INK, alignment=TA_LEFT)
s_tc_small = St("tcs", parent=s_tc, fontSize=6.4, leading=8.2)
s_th_small = St("ths", parent=s_th, fontSize=6.4, leading=8.2)
s_source = St("src", fontName=SANS, fontSize=8.3, leading=11.2, textColor=INK,
              leftIndent=13, firstLineIndent=-13, spaceAfter=3.2, alignment=TA_LEFT)
s_close = St("close", fontName=SANS_I, fontSize=9, leading=12.6, alignment=TA_JUSTIFY,
             textColor=SOFT, spaceBefore=6)

PAGE_W, PAGE_H = letter
LM = RM = 0.78 * inch
TM = 0.78 * inch
BM = 0.86 * inch
FRAME_W = PAGE_W - LM - RM


# ---------------------------------------------------------------- inline markup
def esc(text):
    return (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


LINK_RE = re.compile(r"\[([^\]\[]+)\]\(([^()\s]+)\)")
SHOW_URLS = {"on": False}   # set while rendering the Sources section


def inline(text, link_color=INK):
    """Convert inline Markdown to ReportLab mini-HTML. Monochrome links, underlined."""
    out = esc(text)
    holders = []

    def hold(html):
        holders.append(html)
        return "\x00%d\x00" % (len(holders) - 1)

    def link_sub(m):
        label, url = m.group(1), m.group(2)
        label = _emphasis(label)
        href = url.replace("&amp;", "&")
        if SHOW_URLS["on"]:
            return hold('<a href="%s"><u>%s</u></a> <font face="%s" size="7.2">'
                        '<a href="%s"><u>%s</u></a></font>'
                        % (href, label, MONO, href, esc(href)))
        return hold('<a href="%s"><u>%s</u></a>' % (href, label))

    out = LINK_RE.sub(link_sub, out)
    out = re.sub(r"`([^`]+)`", lambda m: hold('<font face="%s" size="8.4">%s</font>'
                                             % (MONO, m.group(1))), out)
    out = _emphasis(out)
    for i, html in enumerate(holders):
        out = out.replace("\x00%d\x00" % i, html)
    return out


def _emphasis(text):
    text = re.sub(r"\*\*([^*]+)\*\*", lambda m: "<b>%s</b>" % m.group(1), text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", lambda m: "<i>%s</i>" % m.group(1), text)
    return text


# ---------------------------------------------------------------- table build
def col_widths(rows, total, font, size):
    """Proportional widths with a per-column floor equal to the longest word,
    which prevents mid-word wrapping in narrow columns."""
    ncol = len(rows[0])
    weights, minima = [], []
    for c in range(ncol):
        cells = [re.sub(r"[*`\[\]()]|https?://\S+", " ", r[c]) for r in rows]
        lens = [len(r[c]) for r in rows]
        weights.append(max(6.0, sum(lens) / len(lens) * 0.65 + max(lens) * 0.35))
        words = [w for cell in cells for w in cell.split()] or [""]
        longest = max(words, key=len)
        minima.append(pdfmetrics.stringWidth(longest, font, size) + 7.5)
    if sum(minima) > total:
        scale = total / sum(minima)
        minima = [m * scale for m in minima]
    slack = total - sum(minima)
    wsum = sum(weights)
    widths = [minima[c] + slack * weights[c] / wsum for c in range(ncol)]
    scale = total / sum(widths)
    return [w * scale for w in widths]


def make_table(rows):
    ncol = len(rows[0])
    small = ncol >= 6
    cs, hs = (s_tc_small, s_th_small) if small else (s_tc, s_th)
    data = [[Paragraph(inline(cell), hs if r == 0 else cs) for cell in row]
            for r, row in enumerate(rows)]
    widths = col_widths(rows, FRAME_W, cs.fontName, cs.fontSize)
    tbl = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    style = [
        ("GRID", (0, 0), (-1, -1), 0.35, RULE),
        ("BACKGROUND", (0, 0), (-1, 0), HDR_FILL),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3.2),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3.2),
        ("TOPPADDING", (0, 0), (-1, -1), 2.6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.6),
        ("LINEBELOW", (0, 0), (-1, 0), 0.7, INK),
    ]
    for r in range(2, len(rows), 2):
        style.append(("BACKGROUND", (0, r), (-1, r), ZEBRA))
    tbl.setStyle(TableStyle(style))
    return tbl


# ---------------------------------------------------------------- parse markdown
def parse(md):
    """Yield flowables from the canonical Markdown."""
    story = []
    lines = md.split("\n")
    i = 0
    n = len(lines)
    front = True
    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped == "---":
            story.append(Spacer(1, 3))
            story.append(HRFlowable(width="100%", thickness=0.5, color=RULE,
                                    spaceBefore=2, spaceAfter=7))
            i += 1
            continue

        if stripped.startswith("# "):
            story.append(Paragraph(inline(stripped[2:]), s_title))
            i += 1
            continue

        if stripped.startswith("### "):
            story.append(Paragraph(inline(stripped[4:]), s_h2))
            i += 1
            continue

        if stripped.startswith("## "):
            SHOW_URLS["on"] = stripped[3:].strip().startswith("14. Sources")
            story.append(Paragraph(inline(stripped[3:]), s_h1))
            i += 1
            continue

        if stripped.startswith("!["):
            m = re.match(r"!\[([^\]]*)\]\(([^)]+)\)", stripped)
            if m:
                alt, path = m.group(1), m.group(2)
                path = os.path.join(HERE, path.lstrip("./"))
                if os.path.exists(path):
                    from reportlab.lib.utils import ImageReader
                    iw, ih = ImageReader(path).getSize()
                    w = FRAME_W
                    h = w * ih / iw
                    story.append(KeepTogether([Image(path, width=w, height=h),
                                               Paragraph(esc(alt), s_caption)]))
            i += 1
            continue

        if stripped.startswith("|"):
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                raw = lines[i].strip()
                cells = [c.strip() for c in raw.strip("|").split("|")]
                if not re.fullmatch(r"[:\-\s|]+", raw.strip("|")):
                    rows.append(cells)
                i += 1
            width = max(len(r) for r in rows)
            rows = [r + [""] * (width - len(r)) for r in rows]
            story.append(Spacer(1, 2))
            story.append(make_table(rows))
            story.append(Spacer(1, 8))
            continue

        if re.match(r"^[-*]\s+", stripped) or re.match(r"^\d+\.\s+", stripped):
            items = []
            ordered = bool(re.match(r"^\d+\.\s+", stripped))
            while i < n:
                cur = lines[i].strip()
                if re.match(r"^[-*]\s+", cur):
                    text = re.sub(r"^[-*]\s+", "", cur)
                elif re.match(r"^\d+\.\s+", cur):
                    text = re.sub(r"^\d+\.\s+", "", cur)
                else:
                    break
                i += 1
                while i < n and lines[i].strip() and not re.match(
                        r"^([-*]\s+|\d+\.\s+|\||#|!\[|---)", lines[i].strip()):
                    text += " " + lines[i].strip()
                    i += 1
                kw = {"leftIndent": 15}
                if ordered:
                    kw["value"] = len(items) + 1
                items.append(ListItem(Paragraph(inline(text), s_bullet), **kw))
            story.append(ListFlowable(
                items, bulletType="1" if ordered else "bullet",
                bulletFontName=SANS, bulletFontSize=8.6,
                start="1" if ordered else "circle",
                leftIndent=15, bulletDedent=10, spaceBefore=1, spaceAfter=5))
            continue

        # paragraph
        buf = [stripped]
        i += 1
        while i < n and lines[i].strip() and not re.match(
                r"^(#|\||!\[|---|[-*]\s+|\d+\.\s+)", lines[i].strip()):
            buf.append(lines[i].strip())
            i += 1
        text = " ".join(buf)
        style = s_body
        if front:
            if text.startswith("**A preregistered"):
                style = s_sub
            elif text.startswith("Bilal Syed Arfeen."):
                style = s_author
                front = False
        if text.startswith("**End of frozen contract"):
            style = s_close
        story.append(Paragraph(inline(text), style))
    return story


# ---------------------------------------------------------------- page furniture
def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.4)
    canvas.line(LM, BM - 16, PAGE_W - RM, BM - 16)
    canvas.setFont(SANS, 7.4)
    canvas.setFillColor(MUTED)
    canvas.drawString(LM, BM - 27,
                      "SHVVP v0.5  |  FROZEN preregistration  |  NOT DEPOSITED, "
                      "NOT BINDING pending a fresh two-family carrying audit")
    canvas.drawRightString(PAGE_W - RM, BM - 27, "Page %d" % canvas.getPageNumber())
    canvas.restoreState()


def build():
    md = open(SRC, encoding="utf-8").read()
    doc = BaseDocTemplate(
        OUT, pagesize=letter, leftMargin=LM, rightMargin=RM,
        topMargin=TM, bottomMargin=BM,
        title=TITLE, author=AUTHOR, subject=SUBJECT, keywords=KEYWORDS,
        creator="Perplexity Computer", producer="ReportLab")
    frame = Frame(LM, BM, FRAME_W, PAGE_H - TM - BM, id="body",
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="all", frames=[frame], onPage=footer)])
    story = parse(md)
    doc.build(story)
    print("built", OUT)


if __name__ == "__main__":
    build()

---

# Bismillah ir-Rahman ir-Rahim
