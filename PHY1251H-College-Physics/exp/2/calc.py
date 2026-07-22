#!/usr/bin/env python3
"""Compute all numerical results for the DC bridge and four-terminal experiment.

Run this script in the same directory as data.csv:

    python calc.py

The script writes calc_results.json and LaTeX tables under ./tables/.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import pandas as pd

T_FACTOR_OVER_SQRT_N = 2.48
STANDARD_RESISTOR_REL_UNCERTAINTY = 0.0005
RESIDUAL_RESISTANCE_OHM = 0.020

DECADE_RELATIVE_UNCERTAINTY = {
    10000.0: 0.001,
    1000.0: 0.001,
    100.0: 0.001,
    10.0: 0.001,
    1.0: 0.005,
    0.1: 0.020,
}

WHEATSTONE_DATA = [
    {
        "label": "A",
        "rough_Rx_ohm": 1.1022e5,
        "R1_ohm": 1.0e4,
        "R2_ohm": 1.0e3,
        "R0_readings_ohm": [11027.3, 11027.2, 11027.1],
        "I_mA": 0.875,
        "delta_R0_ohm": 1.0,
        "delta_U0_mV": 0.06,
    },
    {
        "label": "B",
        "rough_Rx_ohm": 913.4,
        "R1_ohm": 1.0e3,
        "R2_ohm": 1.0e3,
        "R0_readings_ohm": [912.7, 912.5, 912.8],
        "I_mA": 10.982,
        "delta_R0_ohm": 1.0,
        "delta_U0_mV": 0.01,
    },
    {
        "label": "C",
        "rough_Rx_ohm": 50.82,
        "R1_ohm": 1.0e2,
        "R2_ohm": 1.0e4,
        "R0_readings_ohm": [5077.0, 5076.7, 5077.4],
        "I_mA": 7.262,
        "delta_R0_ohm": 1.0,
        "delta_U0_mV": 0.04,
    },
]

EXCHANGE_DATA = {
    "label": "B'",
    "rough_Rx_ohm": 913.3,
    "R1_ohm": 1.0e3,
    "R2_ohm": 1.0e3,
    "R0_readings_ohm": [912.8, 912.6, 912.3],
    "I_mA": 11.020,
    "delta_R0_ohm": 1.0,
    "delta_U0_mV": 0.01,
}

FOUR_TERMINAL_DIMENSIONS = [
    {"index": 1, "diameter_mm": 0.506, "length_mm": 14.20},
    {"index": 2, "diameter_mm": 0.510, "length_mm": 14.20},
    {"index": 3, "diameter_mm": 0.452, "length_mm": 14.20},
]


def fmt(x: float, digits: int = 4) -> str:
    """Format a floating-point number for LaTeX tables."""
    return f"{x:.{digits}f}"


def decade_b_uncertainty(resistance_ohm: float) -> tuple[float, list[dict[str, float]]]:
    """Return B-type uncertainty of the resistance box by decade summation."""
    remainder = float(resistance_ohm)
    total = 0.0
    components: list[dict[str, float]] = []

    for decade in [10000.0, 1000.0, 100.0, 10.0, 1.0, 0.1]:
        if decade >= 1.0:
            digit = math.floor(remainder / decade + 1e-12)
            component_value = digit * decade
            remainder -= component_value
        else:
            component_value = max(remainder, 0.0)
            remainder = 0.0

        contribution = component_value * DECADE_RELATIVE_UNCERTAINTY[decade]
        components.append(
            {
                "decade_ohm": decade,
                "component_ohm": component_value,
                "relative_uncertainty": DECADE_RELATIVE_UNCERTAINTY[decade],
                "contribution_ohm": contribution,
            }
        )
        total += contribution

    total += RESIDUAL_RESISTANCE_OHM
    return total, components


def process_bridge_record(record: dict[str, object], include_standard_resistors: bool = True) -> dict[str, object]:
    """Compute bridge value, sensitivity, and uncertainty for one record."""
    readings = np.array(record["R0_readings_ohm"], dtype=float)
    R0_mean = float(np.mean(readings))
    sample_sigma = float(np.std(readings, ddof=1))
    delta_A = T_FACTOR_OVER_SQRT_N * sample_sigma
    delta_B, b_components = decade_b_uncertainty(R0_mean)
    u_R0 = math.sqrt(delta_A**2 + delta_B**2)
    u_rel_R0 = u_R0 / R0_mean

    ratio = float(record["R1_ohm"]) / float(record["R2_ohm"])
    Rx = ratio * R0_mean

    if include_standard_resistors:
        u_rel_Rx = math.sqrt(
            STANDARD_RESISTOR_REL_UNCERTAINTY**2
            + STANDARD_RESISTOR_REL_UNCERTAINTY**2
            + u_rel_R0**2
        )
    else:
        u_rel_Rx = u_rel_R0

    u_Rx = Rx * u_rel_Rx
    sensitivity_mV = float(record["delta_U0_mV"]) / (float(record["delta_R0_ohm"]) / R0_mean)

    return {
        **record,
        "R0_mean_ohm": R0_mean,
        "sample_sigma_ohm": sample_sigma,
        "delta_A_ohm": delta_A,
        "delta_B_ohm": delta_B,
        "u_R0_ohm": u_R0,
        "u_rel_R0": u_rel_R0,
        "ratio_R1_over_R2": ratio,
        "Rx_ohm": Rx,
        "u_rel_Rx": u_rel_Rx,
        "u_Rx_ohm": u_Rx,
        "sensitivity_mV": sensitivity_mV,
        "B_components": b_components,
    }


def linear_fit_with_errors(current_mA: np.ndarray, voltage_mV: np.ndarray) -> dict[str, float]:
    """Fit U = kI + b and return k, b, R^2, and standard errors."""
    slope, intercept = np.polyfit(current_mA, voltage_mV, deg=1)
    fitted = slope * current_mA + intercept
    residual = voltage_mV - fitted
    ss_res = float(np.sum(residual**2))
    ss_tot = float(np.sum((voltage_mV - np.mean(voltage_mV)) ** 2))
    r_squared = 1.0 - ss_res / ss_tot if ss_tot != 0 else float("nan")

    n = len(current_mA)
    dof = n - 2
    residual_variance = ss_res / dof
    sxx = float(np.sum((current_mA - np.mean(current_mA)) ** 2))
    slope_stderr = math.sqrt(residual_variance / sxx)
    intercept_stderr = math.sqrt(
        residual_variance * (1.0 / n + float(np.mean(current_mA)) ** 2 / sxx)
    )

    return {
        "n": int(n),
        "sum_I_mA": float(np.sum(current_mA)),
        "sum_U_mV": float(np.sum(voltage_mV)),
        "sum_IU_mA_mV": float(np.sum(current_mA * voltage_mV)),
        "sum_I2_mA2": float(np.sum(current_mA * current_mA)),
        "sum_U2_mV2": float(np.sum(voltage_mV * voltage_mV)),
        "slope_ohm": float(slope),
        "intercept_mV": float(intercept),
        "r_squared": float(r_squared),
        "slope_stderr_ohm": float(slope_stderr),
        "intercept_stderr_mV": float(intercept_stderr),
    }


def add_resistivity_results(fit_results: list[dict[str, float]]) -> None:
    """Add wire cross-sectional area and resistivity to each four-terminal fit."""
    dimensions = {item["index"]: item for item in FOUR_TERMINAL_DIMENSIONS}
    for fit in fit_results:
        dim = dimensions[fit["index"]]
        diameter_mm = float(dim["diameter_mm"])
        length_mm = float(dim["length_mm"])
        area_mm2 = math.pi * diameter_mm**2 / 4.0
        resistivity_ohm_m = fit["slope_ohm"] * area_mm2 / length_mm * 1.0e-3
        resistivity_stderr_ohm_m = fit["slope_stderr_ohm"] * area_mm2 / length_mm * 1.0e-3
        fit.update(
            {
                "diameter_mm": diameter_mm,
                "length_mm": length_mm,
                "area_mm2": area_mm2,
                "resistivity_ohm_m": resistivity_ohm_m,
                "resistivity_micro_ohm_m": resistivity_ohm_m * 1.0e6,
                "resistivity_stderr_ohm_m": resistivity_stderr_ohm_m,
                "resistivity_stderr_micro_ohm_m": resistivity_stderr_ohm_m * 1.0e6,
            }
        )


def write_latex_tables(results: dict[str, object], out_dir: Path) -> None:
    """Write LaTeX table fragments used by report.tex."""
    out_dir.mkdir(parents=True, exist_ok=True)

    bridge_rows = []
    for item in results["wheatstone"]:
        r = item["R0_readings_ohm"]
        bridge_rows.append(
            f"{item['label']} & {item['rough_Rx_ohm']:.4g} & {item['R1_ohm']:.0f} & {item['R2_ohm']:.0f} & "
            f"{r[0]:.1f} & {r[1]:.1f} & {r[2]:.1f} & {item['I_mA']:.3f} & "
            f"{item['delta_R0_ohm']:.0f} & {item['delta_U0_mV']:.2f} \\\\"
        )
    (out_dir / "wheatstone_raw_rows.tex").write_text("\n".join(bridge_rows), encoding="utf-8")

    ex = results["exchange"]
    r = ex["R0_readings_ohm"]
    exchange_row = (
        f"{ex['label']} & {ex['rough_Rx_ohm']:.4g} & {ex['R1_ohm']:.0f} & {ex['R2_ohm']:.0f} & "
        f"{r[0]:.1f} & {r[1]:.1f} & {r[2]:.1f} & {ex['I_mA']:.3f} & "
        f"{ex['delta_R0_ohm']:.0f} & {ex['delta_U0_mV']:.2f} \\\\"
    )
    (out_dir / "exchange_raw_row.tex").write_text(exchange_row, encoding="utf-8")

    processed_rows = []
    for item in results["wheatstone"]:
        processed_rows.append(
            f"{item['label']} & {item['R0_mean_ohm']:.4f} & {item['Rx_ohm']:.4f} & "
            f"{item['delta_A_ohm']:.4f} & {item['delta_B_ohm']:.4f} & {item['u_R0_ohm']:.4f} & "
            f"{100*item['u_rel_Rx']:.4f} & {item['u_Rx_ohm']:.4f} & {item['sensitivity_mV']:.4f} \\\\"
        )
    (out_dir / "wheatstone_processed_rows.tex").write_text("\n".join(processed_rows), encoding="utf-8")

    exchange_result = results["exchange_result"]
    exchange_processed_row = (
        f"{ex['label']} & {ex['R0_mean_ohm']:.4f} & {ex['delta_A_ohm']:.4f} & "
        f"{ex['delta_B_ohm']:.4f} & {ex['u_R0_ohm']:.4f} & {100*ex['u_rel_R0']:.4f} & "
        f"{exchange_result['Rx_exchange_ohm']:.4f} & {exchange_result['u_Rx_exchange_ohm']:.4f} \\\\"
    )
    (out_dir / "exchange_processed_row.tex").write_text(exchange_processed_row, encoding="utf-8")

    fit_rows = []
    for fit in results["four_terminal_fits"]:
        fit_rows.append(
            f"{fit['index']} & {fit['slope_ohm']:.6f} & {fit['intercept_mV']:.6f} & "
            f"{fit['r_squared']:.6f} & {fit['slope_stderr_ohm']:.6f} \\\\"
        )
    (out_dir / "four_terminal_fit_rows.tex").write_text("\n".join(fit_rows), encoding="utf-8")

    resistivity_rows = []
    for fit in results["four_terminal_fits"]:
        resistivity_rows.append(
            f"{fit['index']} & {fit['diameter_mm']:.3f} & {fit['length_mm']:.2f} & "
            f"{fit['area_mm2']:.6f} & {fit['slope_ohm']:.6f} & "
            f"{fit['resistivity_ohm_m']:.6e} & {fit['resistivity_micro_ohm_m']:.6f} \\"
        )
    (out_dir / "four_terminal_resistivity_rows.tex").write_text("\n".join(resistivity_rows), encoding="utf-8")

    data = pd.read_csv(Path(__file__).resolve().parent / "data.csv")
    data.columns = [c.strip() for c in data.columns]
    data_rows = []
    for _, row in data.iterrows():
        data_rows.append(
            f"{row['U1(mV)']:.2f} & {row['I1(mA)']:.2f} & "
            f"{row['U2(mV)']:.2f} & {row['I2(mA)']:.2f} & "
            f"{row['U3(mV)']:.2f} & {row['I3(mA)']:.2f} \\\\"
        )
    (out_dir / "four_terminal_raw_rows.tex").write_text("\n".join(data_rows), encoding="utf-8")


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    data_path = base_dir / "data.csv"
    if not data_path.exists():
        raise FileNotFoundError(f"Cannot find {data_path}")

    bridge_results = [process_bridge_record(record) for record in WHEATSTONE_DATA]
    exchange_result = process_bridge_record(EXCHANGE_DATA, include_standard_resistors=False)

    R0 = bridge_results[1]["R0_mean_ohm"]
    R0_exchange = exchange_result["R0_mean_ohm"]
    Rx_exchange = math.sqrt(R0 * R0_exchange)
    u_rel_exchange = 0.5 * math.sqrt(
        bridge_results[1]["u_rel_R0"] ** 2 + exchange_result["u_rel_R0"] ** 2
    )
    u_Rx_exchange = Rx_exchange * u_rel_exchange

    data = pd.read_csv(data_path)
    data.columns = [column.strip() for column in data.columns]
    fit_results = []
    for index in range(1, 4):
        current = data[f"I{index}(mA)"].to_numpy(dtype=float)
        voltage = data[f"U{index}(mV)"].to_numpy(dtype=float)
        fit_results.append({"index": index, **linear_fit_with_errors(current, voltage)})
    add_resistivity_results(fit_results)

    results = {
        "constants": {
            "T_FACTOR_OVER_SQRT_N": T_FACTOR_OVER_SQRT_N,
            "STANDARD_RESISTOR_REL_UNCERTAINTY": STANDARD_RESISTOR_REL_UNCERTAINTY,
            "RESIDUAL_RESISTANCE_OHM": RESIDUAL_RESISTANCE_OHM,
            "DECADE_RELATIVE_UNCERTAINTY": DECADE_RELATIVE_UNCERTAINTY,
            "FOUR_TERMINAL_DIMENSIONS": FOUR_TERMINAL_DIMENSIONS,
        },
        "wheatstone": bridge_results,
        "exchange": exchange_result,
        "exchange_result": {
            "Rx_exchange_ohm": Rx_exchange,
            "u_rel_Rx_exchange": u_rel_exchange,
            "u_Rx_exchange_ohm": u_Rx_exchange,
        },
        "four_terminal_fits": fit_results,
    }

    with (base_dir / "calc_results.json").open("w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    write_latex_tables(results, base_dir / "tables")

    print("Wheatstone bridge results:")
    for item in bridge_results:
        print(
            f"  {item['label']}: Rx = {item['Rx_ohm']:.6g} ohm, "
            f"u(Rx) = {item['u_Rx_ohm']:.4g} ohm, "
            f"S = {item['sensitivity_mV']:.4g} mV"
        )
    print(
        "Exchange method: "
        f"Rx = {Rx_exchange:.6g} ohm, u(Rx) = {u_Rx_exchange:.4g} ohm"
    )
    print("Four-terminal fits:")
    for fit in fit_results:
        print(
            f"  {fit['index']}: U = {fit['slope_ohm']:.6f} I "
            f"{fit['intercept_mV']:+.6f}, R^2 = {fit['r_squared']:.6f}, "
            f"rho = {fit['resistivity_ohm_m']:.6e} ohm*m"
        )


if __name__ == "__main__":
    main()
