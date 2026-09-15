#!/usr/bin/env python3
"""Plot and fit the U-I data for the four-terminal resistance experiment.

Run this script in the same directory as data.csv:

    python plot.py

The script reads three U-I column pairs, fits each pair with

    U = slope * I + intercept

and saves a single PDF figure named ui_fit.pdf.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np
import pandas as pd


CSV_NAME = "data.csv"
PDF_NAME = "ui_fit.pdf"


def configure_font() -> str:
    """Configure a Times New Roman style font for Matplotlib."""
    available_fonts = {font.name for font in font_manager.fontManager.ttflist}

    for font_name in ["Times New Roman", "Tinos", "Liberation Serif", "DejaVu Serif"]:
        if font_name in available_fonts:
            plt.rcParams["font.family"] = font_name
            break
    else:
        font_name = "serif"
        plt.rcParams["font.family"] = "serif"

    plt.rcParams["pdf.fonttype"] = 42
    plt.rcParams["ps.fonttype"] = 42
    plt.rcParams["mathtext.fontset"] = "stix"
    return font_name


def linear_fit(x: np.ndarray, y: np.ndarray) -> tuple[float, float, float]:
    """Return slope, intercept, and R^2 for the fit y = slope*x + intercept."""
    slope, intercept = np.polyfit(x, y, deg=1)
    y_pred = slope * x + intercept
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r_squared = 1.0 - ss_res / ss_tot if ss_tot != 0 else np.nan
    return slope, intercept, r_squared


def axis_start_point(slope: float, intercept: float) -> tuple[float, float]:
    """Return the visible positive-axis intersection of y = slope*x + intercept."""
    if intercept >= 0:
        return 0.0, intercept
    if slope > 0:
        return -intercept / slope, 0.0
    return 0.0, max(intercept, 0.0)


def main() -> None:
    """Read data.csv, fit three U-I pairs, and save the PDF plot."""
    configure_font()

    script_dir = Path(__file__).resolve().parent
    csv_path = script_dir / CSV_NAME
    pdf_path = script_dir / PDF_NAME

    if not csv_path.exists():
        raise FileNotFoundError(f"Cannot find {CSV_NAME} in {script_dir}")

    data = pd.read_csv(csv_path)
    data.columns = [column.strip() for column in data.columns]

    fig, ax = plt.subplots(figsize=(7.2, 5.0))
    fit_results = []
    all_x_values = []
    all_y_values = []

    for index in range(1, 4):
        u_col = f"U{index}(mV)"
        i_col = f"I{index}(mA)"
        if u_col not in data.columns or i_col not in data.columns:
            raise KeyError(f"Missing required columns: {u_col} and/or {i_col}")

        pair_data = data[[i_col, u_col]].dropna()
        x = pair_data[i_col].to_numpy(dtype=float)
        y = pair_data[u_col].to_numpy(dtype=float)
        slope, intercept, r_squared = linear_fit(x, y)
        x_start, y_start = axis_start_point(slope, intercept)

        fit_results.append({
            "index": index,
            "x": x,
            "y": y,
            "slope": slope,
            "intercept": intercept,
            "r_squared": r_squared,
            "x_start": x_start,
            "y_start": y_start,
        })
        all_x_values.extend(x.tolist())
        all_y_values.extend(y.tolist())

    x_max = max(all_x_values) * 1.08
    for result in fit_results:
        y_end = result["slope"] * x_max + result["intercept"]
        all_y_values.extend([result["y_start"], y_end])
    y_max = max(all_y_values) * 1.10

    for result in fit_results:
        index = result["index"]
        slope = result["slope"]
        intercept = result["intercept"]
        r_squared = result["r_squared"]

        ax.scatter(result["x"], result["y"], s=32, marker="o", label=f"Data {index}")
        x_line = np.linspace(result["x_start"], x_max, 300)
        y_line = slope * x_line + intercept
        ax.plot(
            x_line,
            y_line,
            linewidth=1.8,
            label=f"Fit {index}: U = {slope:.6f} I {intercept:+.6f}, R^2 = {r_squared:.6f}",
        )

        print(
            f"Fit {index}: U = {slope:.6f} I {intercept:+.6f}; "
            f"R^2 = {r_squared:.6f}"
        )

    ax.set_xlim(left=0, right=x_max)
    ax.set_ylim(bottom=0, top=y_max)
    ax.set_xlabel("Current I (mA)")
    ax.set_ylabel("Voltage U (mV)")
    ax.set_title("Linear Least-Squares Fitting of U-I Data")
    ax.grid(True, linestyle="--", linewidth=0.6, alpha=0.6)
    ax.legend(fontsize=8.2, frameon=True)
    fig.tight_layout()
    fig.savefig(pdf_path, bbox_inches="tight")
    plt.close(fig)

    print(f"Saved PDF: {pdf_path}")


if __name__ == "__main__":
    main()
