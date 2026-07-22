#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import csv
import math
import warnings
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import font_manager


Key = Tuple[str, str, str]  # (group, item, phase)


@dataclass(frozen=True)
class FitResult:
    key: Key
    k: np.ndarray
    t: np.ndarray
    theta: np.ndarray
    omega0: float
    beta: float
    intercept: float
    r2: float
    residual_std: float
    n: int


def configure_matplotlib() -> None:
    for font_path in (
        "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc",
        "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc",
    ):
        if Path(font_path).exists():
            font_manager.fontManager.addfont(font_path)

    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": [
            "Noto Serif CJK JP", "Noto Serif CJK SC", "Source Han Serif SC", "SimSun",
            "Times New Roman", "DejaVu Serif",
        ],
        "mathtext.fontset": "dejavuserif",
        "axes.unicode_minus": False,
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "axes.titlesize": 12,
        "axes.labelsize": 10.5,
        "legend.fontsize": 8.5,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
    })


def read_dynamic_data(csv_path: Path) -> Dict[Key, List[Tuple[float, float]]]:
    """读取 CSV 中 record_type == dynamic 的 k 与 time_s。"""
    data: Dict[Key, List[Tuple[float, float]]] = {}

    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        required = {"record_type", "group", "item", "phase_or_quantity", "k", "time_s"}
        missing = required.difference(reader.fieldnames or [])
        if missing:
            raise ValueError(f"CSV 缺少必要列：{', '.join(sorted(missing))}")

        for row_no, row in enumerate(reader, start=2):
            if row.get("record_type", "").strip() != "dynamic":
                continue

            group = row.get("group", "").strip()
            item = row.get("item", "").strip()
            phase = row.get("phase_or_quantity", "").strip()
            key = (group, item, phase)

            try:
                k = float(row.get("k", ""))
                t = float(row.get("time_s", ""))
            except ValueError as exc:
                raise ValueError(f"第 {row_no} 行 k 或 time_s 不是有效数字：{row}") from exc

            if not math.isfinite(k) or not math.isfinite(t):
                raise ValueError(f"第 {row_no} 行 k 或 time_s 不是有限值：{row}")
            if t <= 0:
                raise ValueError(f"第 {row_no} 行 time_s 必须大于 0：{row}")

            data.setdefault(key, []).append((k, t))

    for key, values in data.items():
        values.sort(key=lambda x: x[0])
        ks = [int(v[0]) for v in values]
        if len(values) != 8:
            warnings.warn(f"{key} 不是 8 个数据点，而是 {len(values)} 个。", RuntimeWarning)
        if ks != list(range(1, len(values) + 1)):
            warnings.warn(f"{key} 的 k 序列不是连续的 1~n：{ks}", RuntimeWarning)

    if not data:
        raise ValueError("CSV 中没有找到 record_type == 'dynamic' 的动态计时数据。")

    return data


def fit_beta(key: Key, values: List[Tuple[float, float]], *, free_intercept: bool = False) -> FitResult:

    k = np.array([v[0] for v in values], dtype=float)
    t = np.array([v[1] for v in values], dtype=float)
    theta = k * np.pi

    if free_intercept:
        design = np.column_stack([np.ones_like(t), t, 0.5 * t**2])
        coeff, *_ = np.linalg.lstsq(design, theta, rcond=None)
        intercept, omega0, beta = coeff
    else:
        design = np.column_stack([t, 0.5 * t**2])
        coeff, *_ = np.linalg.lstsq(design, theta, rcond=None)
        omega0, beta = coeff
        intercept = 0.0

    theta_hat = intercept + omega0 * t + 0.5 * beta * t**2
    residual = theta - theta_hat
    sse = float(np.sum(residual**2))
    sst = float(np.sum((theta - np.mean(theta)) ** 2))
    r2 = 1.0 - sse / sst if sst > 0 else float("nan")
    dof = max(len(t) - (3 if free_intercept else 2), 1)
    residual_std = float(np.sqrt(sse / dof))

    return FitResult(
        key=key,
        k=k,
        t=t,
        theta=theta,
        omega0=float(omega0),
        beta=float(beta),
        intercept=float(intercept),
        r2=float(r2),
        residual_std=residual_std,
        n=len(t),
    )


def evaluate_fit(result: FitResult, t_grid: np.ndarray) -> np.ndarray:
    return result.intercept + result.omega0 * t_grid + 0.5 * result.beta * t_grid**2


NAME_MAP = {
    ("mandatory", "empty"): "空台",
    ("mandatory", "disk"): "圆盘+空台",
    ("mandatory", "ring"): "圆环+空台",
    ("mandatory", "two_cylinders"): "两个圆柱+空台",
    ("optional", "plate_x"): "垂直轴 x 方向",
    ("optional", "plate_y"): "垂直轴 y 方向",
    ("optional", "plate_z"): "垂直轴 z 方向",
}


PHASE_NAME = {
    "acceleration": "加速",
    "deceleration": "减速",
}


def display_name(key: Key) -> str:
    group, item, phase = key
    return NAME_MAP.get((group, item), f"{group}/{item}")


def plot_group(ax: plt.Axes, results: Dict[Key, FitResult], keys: Iterable[Key], title: str) -> None:
    plotted = 0
    for key in keys:
        result = results.get(key)
        if result is None:
            warnings.warn(f"未找到数据组：{key}", RuntimeWarning)
            continue

        t_min, t_max = float(np.min(result.t)), float(np.max(result.t))
        t_grid = np.linspace(t_min, t_max, 240)
        theta_grid = evaluate_fit(result, t_grid)
        name = display_name(key)
        label = f"{name}: β={result.beta:+.5f} rad/s², R²={result.r2:.5f}"

        ax.scatter(result.t, result.theta, s=26, marker="o", zorder=3)
        ax.plot(t_grid, theta_grid, linewidth=1.8, label=label)
        plotted += 1

    ax.set_title(title)
    ax.set_xlabel("t / s")
    ax.set_ylabel(r"$\theta = k\pi$ / rad")
    ax.grid(True, linestyle="--", alpha=0.35)
    if plotted:
        ax.legend(loc="best", frameon=True)
    else:
        ax.text(0.5, 0.5, "没有可绘制的数据", transform=ax.transAxes,
                ha="center", va="center")

def save_summary_csv(results: Dict[Key, FitResult], summary_path: Path) -> None:
    rows = []
    for key in sorted(results):
        group, item, phase = key
        r = results[key]
        rows.append({
            "group": group,
            "item": item,
            "phase": phase,
            "name": display_name(key),
            "n_points": r.n,
            "omega0_rad_s": f"{r.omega0:.12g}",
            "beta_rad_s2": f"{r.beta:.12g}",
            "intercept_rad": f"{r.intercept:.12g}",
            "r2": f"{r.r2:.12g}",
            "residual_std_rad": f"{r.residual_std:.12g}",
        })

    with summary_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def make_pdf(results: Dict[Key, FitResult], pdf_path: Path) -> None:
    first_page_acc = [
        ("mandatory", "empty", "acceleration"),
        ("mandatory", "disk", "acceleration"),
        ("mandatory", "ring", "acceleration"),
    ]
    first_page_dec = [
        ("mandatory", "empty", "deceleration"),
        ("mandatory", "disk", "deceleration"),
        ("mandatory", "ring", "deceleration"),
    ]

    cylinder_acc = [("mandatory", "two_cylinders", "acceleration")]
    cylinder_dec = [("mandatory", "two_cylinders", "deceleration")]

    plate_acc = [
        ("optional", "plate_x", "acceleration"),
        ("optional", "plate_y", "acceleration"),
        ("optional", "plate_z", "acceleration"),
    ]
    plate_dec = [
        ("optional", "plate_x", "deceleration"),
        ("optional", "plate_y", "deceleration"),
        ("optional", "plate_z", "deceleration"),
    ]

    pages = [
        ("空台、圆盘+空台、圆环+空台", first_page_acc, "加速拟合", first_page_dec, "减速拟合"),
        ("两个圆柱+空台", cylinder_acc, "加速拟合", cylinder_dec, "减速拟合"),
        ("垂直轴 x、y、z 三个方向", plate_acc, "加速拟合", plate_dec, "减速拟合"),
    ]

    with PdfPages(pdf_path) as pdf:
        for page_title, left_keys, left_title, right_keys, right_title in pages:
            fig, axes = plt.subplots(1, 2, figsize=(11.69, 8.27), constrained_layout=False)
            fig.suptitle(f"{page_title}：角位移-时间二次拟合", fontsize=14, y=0.965)
            fig.subplots_adjust(left=0.065, right=0.985, top=0.88, bottom=0.13, wspace=0.11)
            plot_group(axes[0], results, left_keys, left_title)
            plot_group(axes[1], results, right_keys, right_title)
            # 页脚写明拟合模型，方便检查 beta 的来源。
            fig.text(
                0.5, 0.018,
                r"拟合模型：$\theta_k = k\pi = \omega_0 t_k + \frac{1}{2}\beta t_k^2$；"
                r"图中圆点为原始数据，曲线为最小二乘拟合。",
                ha="center", va="bottom", fontsize=9,
            )
            pdf.savefig(fig)
            plt.close(fig)


def print_result_table(results: Dict[Key, FitResult]) -> None:
    print("\n拟合结果：")
    print("{:<12s} {:<16s} {:<13s} {:>14s} {:>14s} {:>10s}".format(
        "group", "item", "phase", "omega0(rad/s)", "beta(rad/s^2)", "R^2"
    ))
    print("-" * 86)
    for key in sorted(results):
        r = results[key]
        group, item, phase = key
        print("{:<12s} {:<16s} {:<13s} {:>14.7f} {:>14.7f} {:>10.6f}".format(
            group, item, phase, r.omega0, r.beta, r.r2
        ))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="由原始 CSV 拟合转动惯量实验各组角加速度 beta。")
    parser.add_argument(
        "csv_path", nargs="?", default="rotational_inertia_raw.csv",
        help="原始数据 CSV 文件路径，默认 rotational_inertia_raw.csv",
    )
    parser.add_argument(
        "--pdf", default="beta_fit_pages.pdf",
        help="输出拟合图 PDF 文件名，默认 beta_fit_pages.pdf",
    )
    parser.add_argument(
        "--summary", default="beta_fit_results.csv",
        help="输出 beta 拟合结果 CSV 文件名，默认 beta_fit_results.csv",
    )
    parser.add_argument(
        "--free-intercept", action="store_true",
        help="使用自由截距模型 theta=c+omega0*t+0.5*beta*t^2；默认使用过原点模型。",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    csv_path = Path(args.csv_path).expanduser().resolve()
    if not csv_path.exists():
        raise FileNotFoundError(f"找不到 CSV 文件：{csv_path}")

    # 输出文件默认放在 CSV 同目录；若用户给的是绝对路径，则尊重绝对路径。
    pdf_path = Path(args.pdf).expanduser()
    if not pdf_path.is_absolute():
        pdf_path = csv_path.parent / pdf_path
    summary_path = Path(args.summary).expanduser()
    if not summary_path.is_absolute():
        summary_path = csv_path.parent / summary_path

    configure_matplotlib()
    dynamic_data = read_dynamic_data(csv_path)
    results = {
        key: fit_beta(key, values, free_intercept=args.free_intercept)
        for key, values in dynamic_data.items()
    }

    make_pdf(results, pdf_path)
    save_summary_csv(results, summary_path)
    print_result_table(results)
    print(f"\n已保存拟合图：{pdf_path}")
    print(f"已保存 beta 汇总：{summary_path}")


if __name__ == "__main__":
    main()
