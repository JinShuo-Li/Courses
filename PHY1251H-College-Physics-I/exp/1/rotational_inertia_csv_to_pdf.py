from __future__ import annotations

import argparse
import csv
from collections import OrderedDict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from statistics import mean, pstdev
from typing import Iterable

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


@dataclass(frozen=True)
class CsvRow:
    record_type: str
    group: str
    item: str
    phase_or_quantity: str
    index: str
    k: str
    time_s: str
    value: str
    unit: str

    @property
    def measurement(self) -> str:
        if self.value not in ("", None):
            return self.value
        return self.time_s

    @property
    def measurement_label(self) -> str:
        if self.value not in ("", None):
            return "value"
        return "time_s"


def register_times_font() -> str:
    candidates = [
        r"C:\Windows\Fonts\times.ttf",
        r"C:\Windows\Fonts\timesbd.ttf",
        r"C:\Windows\Fonts\timesi.ttf",
        r"C:\Windows\Fonts\timesbi.ttf",
        r"/usr/share/fonts/truetype/msttcorefonts/times.ttf",
        r"/Library/Fonts/Times New Roman.ttf",
    ]
    regular = next((path for path in candidates if Path(path).exists()), None)
    bold = next((path for path in [r"C:\Windows\Fonts\timesbd.ttf", r"/Library/Fonts/Times New Roman Bold.ttf"] if Path(path).exists()), None)
    italic = next((path for path in [r"C:\Windows\Fonts\timesi.ttf", r"/Library/Fonts/Times New Roman Italic.ttf"] if Path(path).exists()), None)
    bold_italic = next((path for path in [r"C:\Windows\Fonts\timesbi.ttf", r"/Library/Fonts/Times New Roman Bold Italic.ttf"] if Path(path).exists()), None)

    if regular:
        pdfmetrics.registerFont(TTFont("TimesNewRomanCustom", regular))
        if bold:
            pdfmetrics.registerFont(TTFont("TimesNewRomanCustom-Bold", bold))
        if italic:
            pdfmetrics.registerFont(TTFont("TimesNewRomanCustom-Italic", italic))
        if bold_italic:
            pdfmetrics.registerFont(TTFont("TimesNewRomanCustom-BoldItalic", bold_italic))
        return "TimesNewRomanCustom"

    return "Times-Roman"


def format_number(value: str) -> str:
    if value in (None, ""):
        return ""
    try:
        numeric = float(value)
    except ValueError:
        return value
    if numeric.is_integer():
        return f"{numeric:.0f}"
    return f"{numeric:.3f}".rstrip("0").rstrip(".")


def safe_float(value: str) -> float | None:
    if value in (None, ""):
        return None
    try:
        return float(value)
    except ValueError:
        return None


def read_rows(csv_path: Path) -> list[CsvRow]:
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        rows: list[CsvRow] = []
        for row in reader:
            if not any((row.get(key) or "").strip() for key in reader.fieldnames or []):
                continue
            rows.append(
                CsvRow(
                    record_type=(row.get("record_type") or "").strip(),
                    group=(row.get("group") or "").strip(),
                    item=(row.get("item") or "").strip(),
                    phase_or_quantity=(row.get("phase_or_quantity") or "").strip(),
                    index=(row.get("index") or "").strip(),
                    k=(row.get("k") or "").strip(),
                    time_s=(row.get("time_s") or "").strip(),
                    value=(row.get("value") or "").strip(),
                    unit=(row.get("unit") or "").strip(),
                )
            )
        return rows


def grouped_rows(rows: Iterable[CsvRow]) -> OrderedDict[str, OrderedDict[str, OrderedDict[str, list[CsvRow]]]]:
    nested: OrderedDict[str, OrderedDict[str, OrderedDict[str, list[CsvRow]]]] = OrderedDict()
    for row in rows:
        nested.setdefault(row.record_type, OrderedDict())
        nested[row.record_type].setdefault(row.group, OrderedDict())
        nested[row.record_type][row.group].setdefault(row.item, [])
        nested[row.record_type][row.group][row.item].append(row)
    return nested


def summarize(values: list[float]) -> tuple[int, float, float, float, float]:
    count = len(values)
    if not values:
        return 0, 0.0, 0.0, 0.0, 0.0
    if count == 1:
        return 1, values[0], 0.0, values[0], values[0]
    return count, mean(values), pstdev(values), min(values), max(values)


def make_styles(font_name: str):
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="ReportTitleCustom",
            parent=styles["Title"],
            fontName=font_name,
            fontSize=22,
            leading=26,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#152238"),
            spaceAfter=10,
        )
    )
    styles.add(
        ParagraphStyle(
            name="ReportHeadingCustom",
            parent=styles["Heading1"],
            fontName=font_name,
            fontSize=15,
            leading=18,
            textColor=colors.HexColor("#1F3A5F"),
            spaceBefore=12,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="ReportSubheadingCustom",
            parent=styles["Heading2"],
            fontName=font_name,
            fontSize=11,
            leading=13,
            textColor=colors.HexColor("#304A6E"),
            spaceBefore=8,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="ReportBodyCustom",
            parent=styles["BodyText"],
            fontName=font_name,
            fontSize=9.5,
            leading=12,
            alignment=TA_LEFT,
        )
    )
    styles.add(
        ParagraphStyle(
            name="ReportSmallCustom",
            parent=styles["BodyText"],
            fontName=font_name,
            fontSize=8,
            leading=10,
            alignment=TA_LEFT,
        )
    )
    return styles


def build_table(data: list[list[str]], font_name: str) -> Table:
    table = Table(data, repeatRows=1, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#DDE7F7")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#152238")),
                ("FONTNAME", (0, 0), (-1, -1), font_name),
                ("FONTSIZE", (0, 0), (-1, -1), 8.5),
                ("LEADING", (0, 0), (-1, -1), 10),
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#8FA8C8")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F7FAFF")]),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return table


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont(doc.font_name, 8)
    canvas.setFillColor(colors.HexColor("#52627A"))
    canvas.drawString(doc.leftMargin, 0.4 * inch, doc.doc_label)
    canvas.drawRightString(doc.pagesize[0] - doc.rightMargin, 0.4 * inch, f"Page {doc.page}")
    canvas.restoreState()


def render_document(csv_path: Path, pdf_path: Path) -> None:
    font_name = register_times_font()
    styles = make_styles(font_name)
    rows = read_rows(csv_path)
    grouped = grouped_rows(rows)

    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=landscape(letter),
        leftMargin=0.45 * inch,
        rightMargin=0.45 * inch,
        topMargin=0.6 * inch,
        bottomMargin=0.6 * inch,
        title=csv_path.stem,
        author="Copilot",
    )
    doc.font_name = font_name
    doc.doc_label = csv_path.name

    story = []
    story.append(Paragraph("Rotational Inertia Data Report", styles["ReportTitleCustom"]))
    story.append(Paragraph(f"Source file: {csv_path.name}", styles["ReportBodyCustom"]))
    story.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles["ReportBodyCustom"]))
    story.append(Spacer(1, 0.18 * inch))

    overview_data = [["Record type", "Group", "Items", "Rows"]]
    for record_type, group_map in grouped.items():
        for group_name, item_map in group_map.items():
            item_names = ", ".join(item_map.keys())
            row_count = sum(len(item_rows) for item_rows in item_map.values())
            overview_data.append([record_type, group_name, item_names, str(row_count)])
    story.append(Paragraph("Overview", styles["ReportHeadingCustom"]))
    story.append(build_table(overview_data, font_name))
    story.append(Spacer(1, 0.14 * inch))

    first_section = True
    for record_type, group_map in grouped.items():
        if not first_section:
            story.append(PageBreak())
        first_section = False
        story.append(Paragraph(record_type.title(), styles["ReportHeadingCustom"]))

        for group_name, item_map in group_map.items():
            story.append(Paragraph(group_name.title(), styles["ReportSubheadingCustom"]))
            for item_name, item_rows in item_map.items():
                label_parts = [part for part in [item_name, item_rows[0].phase_or_quantity] if part]
                section_label = " / ".join(label_parts) if label_parts else item_name
                story.append(Paragraph(section_label, styles["ReportBodyCustom"]))

                table_rows = [["#", "k", "Measurement", "Unit"]]
                numeric_values = []
                measurement_label = item_rows[0].measurement_label
                for row in item_rows:
                    measurement = format_number(row.measurement)
                    table_rows.append([
                        row.index,
                        row.k,
                        measurement,
                        row.unit,
                    ])
                    numeric_value = safe_float(row.measurement)
                    if numeric_value is not None:
                        numeric_values.append(numeric_value)

                story.append(build_table(table_rows, font_name))

                count, avg, std_dev, minimum, maximum = summarize(numeric_values)
                summary_text = (
                    f"Measurement source: {measurement_label}. "
                    f"Count={count}, mean={avg:.4f}, std={std_dev:.4f}, min={minimum:.4f}, max={maximum:.4f}."
                    if count
                    else f"Measurement source: {measurement_label}."
                )
                story.append(Paragraph(summary_text, styles["ReportSmallCustom"]))
                story.append(Spacer(1, 0.08 * inch))

    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a readable PDF report from the rotational inertia CSV file.")
    parser.add_argument("csv_file", nargs="?", default=r"C:\Users\Jinshuo Li\Downloads\rotational_inertia_raw.csv")
    parser.add_argument("pdf_file", nargs="?", default=None)
    args = parser.parse_args()

    csv_path = Path(args.csv_file)
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    pdf_path = Path(args.pdf_file) if args.pdf_file else csv_path.with_suffix(".pdf")
    render_document(csv_path, pdf_path)
    print(f"PDF generated: {pdf_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())