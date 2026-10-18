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
csv_oversized_freetext_cell -- v1.1.8 F2 calibration item 2.

Al-Baqarah 2:42 applied to per-cell length discipline. A spreadsheet
cell is, in practice, a short value: a number, an identifier, a date,
a brief note. Multi-paragraph payloads embedded in a single cell are
the canonical "long-cell hijack" shape: the grid still renders as a
tabular row, but one cell carries content that dwarfs every other
cell in the same column.

Detector contract:

  * For each non-header cell, compute the cell's character length.
  * For each column, compute the median cell length over all data
    rows (header excluded).
  * Fire a Tier 2 zahir finding when a cell is BOTH longer than 500
    characters AND longer than 10x the column's median cell length.

Tier 2 zahir (single deterministic walk over the rendered text
content): the cell length is observable from any single decoded view
of the file. The divergence is structural in shape (grid carries
sub-paragraph cells; this cell carries a paragraph), not encoding.

Severity 0.15. Same calibration as csv_column_type_drift -- both
surface a contract a tabular file establishes (one row per record,
short cells per column) versus a row that violates it.

False-positive guard: the 10x median requirement excludes columns
where every cell is long (legitimate description / note columns).
The 500-char absolute threshold excludes short tabular columns where
the median is small but no cell is actually a payload.

Reference: Munafiq Protocol Sec. 9. DOI: 10.5281/zenodo.19677111.
"""

from __future__ import annotations

import csv
import io
from pathlib import Path
from statistics import median
from typing import Iterable

from domain import Finding
from domain.config import TIER


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Absolute floor: a cell shorter than this never triggers, regardless
# of how much shorter the column median is.
_ABSOLUTE_LENGTH_THRESHOLD = 500

# Multiplier over the column median that the cell must exceed.
_MEDIAN_RATIO_THRESHOLD = 10.0

# Minimum number of data rows required for the median comparison to
# be meaningful. With fewer than 3 data rows, median is dominated by
# the long cell itself.
_MIN_DATA_ROWS_FOR_MEDIAN = 3


# ---------------------------------------------------------------------------
# Detector entry point
# ---------------------------------------------------------------------------


def detect_oversized_freetext_cell(
    text: str,
    delimiter: str,
    file_path: Path,
) -> Iterable[Finding]:
    """Yield csv_oversized_freetext_cell findings for the given CSV text.

    ``text`` is the already-decoded CSV body (NULs replaced, BOM
    stripped). ``delimiter`` is the inferred delimiter. ``file_path``
    is the source path used in finding ``location`` strings.
    """
    reader = csv.reader(io.StringIO(text), delimiter=delimiter)
    rows = list(reader)
    if len(rows) < 2:
        return
    header = rows[0]
    data_rows = rows[1:]
    if len(data_rows) < _MIN_DATA_ROWS_FOR_MEDIAN:
        return

    column_count = len(header)

    # Per-column length samples from every data row. Cells past the
    # header column count are ignored here -- those are surplus-
    # column territory.
    column_lengths: list[list[int]] = [[] for _ in range(column_count)]
    for row in data_rows:
        for col_index in range(min(len(row), column_count)):
            column_lengths[col_index].append(len(row[col_index]))

    column_medians: list[float] = [
        median(lengths) if lengths else 0.0
        for lengths in column_lengths
    ]

    for row_offset, row in enumerate(data_rows):
        # Row index reported is 1-indexed against the data rows
        # (header is row 0; first data row is row 1). Mirrors the
        # convention used by csv_column_type_drift.
        row_index = row_offset + 1
        for col_index in range(min(len(row), column_count)):
            cell_value = row[col_index]
            cell_len = len(cell_value)
            if cell_len <= _ABSOLUTE_LENGTH_THRESHOLD:
                continue
            col_median = column_medians[col_index]
            # Guard against zero / very small medians where the
            # ratio test would always pass.
            if col_median < 1.0:
                col_median = 1.0
            if cell_len < (col_median * _MEDIAN_RATIO_THRESHOLD):
                continue
            header_name = (
                header[col_index] if col_index < len(header) else ""
            )
            yield Finding(
                mechanism="csv_oversized_freetext_cell",
                tier=TIER["csv_oversized_freetext_cell"],
                confidence=0.85,
                description=(
                    f"Column {header_name!r} (column {col_index}) has "
                    f"a median cell length of {col_median:.0f} "
                    f"characters across {len(column_lengths[col_index])} "
                    f"data row(s); row {row_index} carries a cell of "
                    f"{cell_len} characters in that column "
                    f"({cell_len / col_median:.1f}x the median). "
                    "A spreadsheet cell carries one short value per "
                    "row by convention. A cell longer than 500 "
                    "characters AND more than 10x the column median "
                    "is a multi-paragraph payload smuggled into a "
                    "single tabular cell."
                ),
                location=(
                    f"{file_path}:row={row_index},col={col_index}"
                ),
                surface=(
                    f"(column {header_name!r} median {col_median:.0f}; "
                    f"row {row_index} cell length {cell_len})"
                ),
                concealed=cell_value[:240],
                source_layer="zahir",
            )


__all__ = ["detect_oversized_freetext_cell"]

# Bismillah ir-Rahman ir-Rahim