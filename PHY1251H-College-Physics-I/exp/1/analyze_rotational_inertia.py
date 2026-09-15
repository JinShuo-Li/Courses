import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

CSV_FILE = "rotational_inertia_raw.csv"
OUT_PDF = "rotational_inertia_fit_report.pdf"
OUT_SUMMARY = "rotational_inertia_summary.csv"

mpl.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
    "mathtext.fontset": "dejavuserif",
    "axes.unicode_minus": False,
})


def mean_value(df, record_type, item, quantity):
    s = df[(df.record_type == record_type) & (df.item == item) & (df.phase_or_quantity == quantity)]["value"].astype(float)
    return float(s.mean())


def fit_motion(t, k):
    theta = np.asarray(k, dtype=float) * np.pi
    t = np.asarray(t, dtype=float)
    X = np.column_stack([t, 0.5 * t**2])
    omega0, beta = np.linalg.lstsq(X, theta, rcond=None)[0]
    pred = X @ np.array([omega0, beta])
    ss_res = float(np.sum((theta - pred) ** 2))
    ss_tot = float(np.sum((theta - theta.mean()) ** 2))
    r2 = 1 - ss_res / ss_tot
    rmse = float(np.sqrt(np.mean((theta - pred) ** 2)))
    return dict(omega0=float(omega0), beta=float(beta), r2=float(r2), rmse=rmse, theta=theta, pred=pred)


def total_inertia(m_hang, R, g, beta_acc, beta_dec):
    return m_hang * R * (g - R * beta_acc) / (beta_acc - beta_dec)


def rel_err(measured, calculated):
    return (measured - calculated) / calculated * 100


def build_analysis(csv_path):
    df = pd.read_csv(csv_path)
    dyn = df[df.record_type == "dynamic"].copy()
    fits = {}
    for (group, item, phase), sub in dyn.groupby(["group", "item", "phase_or_quantity"]):
        sub = sub.sort_values("k")
        fits[(item, phase)] = fit_motion(sub["time_s"].astype(float), sub["k"].astype(float))

    g = mean_value(df, "parameter", "g", "") if False else 9.80
    m_hang = mean_value(df, "mass", "hanging_mass", "mass") / 1000
    R_tower = mean_value(df, "length", "tower", "diameter") / 200

    loaded_items = ["empty", "disk", "ring", "two_cylinders", "plate_x", "plate_y", "plate_z"]
    total_J = {}
    for item in loaded_items:
        total_J[item] = total_inertia(
            m_hang, R_tower, g,
            fits[(item, "acceleration")]["beta"],
            fits[(item, "deceleration")]["beta"],
        )

    measured = {
        "Disk": total_J["disk"] - total_J["empty"],
        "Ring": total_J["ring"] - total_J["empty"],
        "Two cylinders": total_J["two_cylinders"] - total_J["empty"],
        "Plate x-axis": total_J["plate_x"] - total_J["empty"],
        "Plate y-axis": total_J["plate_y"] - total_J["empty"],
        "Plate z-axis": total_J["plate_z"] - total_J["empty"],
    }

    m_disk = mean_value(df, "mass", "disk", "mass") / 1000
    r_disk = mean_value(df, "length", "disk", "outer_diameter") / 200
    m_ring = mean_value(df, "mass", "ring", "mass") / 1000
    r_ring_in = mean_value(df, "length", "ring", "inner_diameter") / 200
    r_ring_out = mean_value(df, "length", "ring", "outer_diameter") / 200

    m_c1 = mean_value(df, "mass", "cylinder_1", "mass") / 1000
    m_c2 = mean_value(df, "mass", "cylinder_2", "mass") / 1000
    r_c1 = mean_value(df, "length", "cylinder_1", "outer_diameter") / 200
    r_c2 = mean_value(df, "length", "cylinder_2", "outer_diameter") / 200
    L_outer = mean_value(df, "length", "cylinders", "outer_side_distance") / 100
    L_inner = mean_value(df, "length", "cylinders", "inner_side_distance") / 100
    r_offset = (L_outer + L_inner) / 4

    m_plate = mean_value(df, "mass", "plate", "mass") / 1000
    a = mean_value(df, "length", "plate", "a") / 100
    b = mean_value(df, "length", "plate", "b") / 100
    h = mean_value(df, "length", "plate", "h") / 100

    calc = {
        "Disk": 0.5 * m_disk * r_disk**2,
        "Ring": 0.5 * m_ring * (r_ring_out**2 + r_ring_in**2),
        "Two cylinders": 0.5*m_c1*r_c1**2 + m_c1*r_offset**2 + 0.5*m_c2*r_c2**2 + m_c2*r_offset**2,
        "Plate x-axis": m_plate * (b**2 + h**2) / 12,
        "Plate y-axis": m_plate * (a**2 + h**2) / 12,
        "Plate z-axis": m_plate * (a**2 + b**2) / 12,
    }

    diagnostics = {
        "g (m/s^2)": g,
        "hanging mass (kg)": m_hang,
        "tower radius (m)": R_tower,
        "empty table J (kg m^2)": total_J["empty"],
        "cylinder offset from axis (m)": r_offset,
        "cylinder offset back-calculated from measured J (m)": np.sqrt(max((measured["Two cylinders"] - 0.5*m_c1*r_c1**2 - 0.5*m_c2*r_c2**2) / (m_c1 + m_c2), 0)),
        "plate theorem measured, (Jx+Jy-Jz)/Jz (%)": (measured["Plate x-axis"] + measured["Plate y-axis"] - measured["Plate z-axis"]) / measured["Plate z-axis"] * 100,
    }

    fit_rows = []
    for (item, phase), res in fits.items():
        fit_rows.append({
            "item": item,
            "phase": phase,
            "omega0_rad_s": res["omega0"],
            "beta_rad_s2": res["beta"],
            "r_squared": res["r2"],
            "rmse_rad": res["rmse"],
        })
    fit_table = pd.DataFrame(fit_rows).sort_values(["item", "phase"])

    moment_rows = []
    for name in calc:
        moment_rows.append({
            "object": name,
            "measured_kg_m2": measured[name],
            "calculated_kg_m2": calc[name],
            "difference_kg_m2": measured[name] - calc[name],
            "relative_difference_percent": rel_err(measured[name], calc[name]),
        })
    moment_table = pd.DataFrame(moment_rows)

    summary = pd.concat([
        pd.DataFrame({"section": "fit", **{c: fit_table[c] for c in fit_table.columns}}),
        pd.DataFrame({"section": "moment", **{c: moment_table[c] for c in moment_table.columns}}),
    ], ignore_index=True, sort=False)
    summary.to_csv(OUT_SUMMARY, index=False)
    return df, fits, fit_table, moment_table, diagnostics


def make_pdf(df, fits, fit_table, moment_table, diagnostics, out_pdf):
    plot_order = [
        "empty", "disk", "ring", "two_cylinders",
        "plate_x", "plate_y", "plate_z",
    ]
    titles = {
        "empty": "Empty table", "disk": "Disk", "ring": "Ring", "two_cylinders": "Two cylinders",
        "plate_x": "Plate x-axis", "plate_y": "Plate y-axis", "plate_z": "Plate z-axis",
    }

    fig = plt.figure(figsize=(23.4, 16.5))
    gs = fig.add_gridspec(4, 5, width_ratios=[1, 1, 1, 1, 1.55], height_ratios=[1, 1, 1, 1], wspace=0.35, hspace=0.42)
    dyn = df[df.record_type == "dynamic"].copy()

    for i, item in enumerate(plot_order):
        ax = fig.add_subplot(gs[i // 2, (i % 2) * 2: (i % 2) * 2 + 2])
        for phase, marker in [("acceleration", "o"), ("deceleration", "s")]:
            sub = dyn[(dyn.item == item) & (dyn.phase_or_quantity == phase)].sort_values("k")
            t = sub["time_s"].astype(float).to_numpy()
            k = sub["k"].astype(float).to_numpy()
            theta = k * np.pi
            res = fits[(item, phase)]
            tt = np.linspace(0, t.max() * 1.03, 160)
            fit_curve = res["omega0"] * tt + 0.5 * res["beta"] * tt**2
            ax.plot(t, theta, marker, ms=4, label=phase)
            ax.plot(tt, fit_curve, lw=1.3)
        ax.set_title(titles[item], fontsize=11)
        ax.set_xlabel("Time t (s)", fontsize=9)
        ax.set_ylabel(r"Angular displacement $\theta$ (rad)", fontsize=9)
        ax.grid(True, alpha=0.25)
        ax.tick_params(labelsize=8)
        ax.legend(fontsize=7, loc="upper left")

    ax_text = fig.add_subplot(gs[:, 4])
    ax_text.axis("off")
    ax_text.set_title("Fitted and calculated parameters", fontsize=13, pad=8)

    fit_small = fit_table.copy()
    fit_small["label"] = fit_small["item"].str.replace("_", " ") + " " + fit_small["phase"].str[0].str.upper()
    lines = ["Motion fits: theta = omega0 t + 0.5 beta t^2", ""]
    lines.append(f"{'Case':<19} {'beta':>10} {'R2':>8} {'RMSE':>8}")
    for _, r in fit_small.iterrows():
        lines.append(f"{r['label']:<19.19s} {r['beta_rad_s2']:>10.4f} {r['r_squared']:>8.6f} {r['rmse_rad']:>8.4f}")
    lines += ["", "Moment of inertia:", f"{'Object':<17} {'Meas.':>10} {'Calc.':>10} {'Diff.':>10} {'Rel.%':>8}"]
    for _, r in moment_table.iterrows():
        lines.append(f"{r['object']:<17.17s} {r['measured_kg_m2']:>10.6f} {r['calculated_kg_m2']:>10.6f} {r['difference_kg_m2']:>10.6f} {r['relative_difference_percent']:>8.2f}")
    lines += ["", "Other parameters:"]
    for k, v in diagnostics.items():
        lines.append(f"{k}: {v:.6g}")
    lines += ["", "Notes:", "Friction is included through the deceleration run.", "The two-cylinder result is anomalously high.", "The plate data support the perpendicular-axis theorem."]

    ax_text.text(0.0, 0.98, "\n".join(lines), va="top", ha="left", fontsize=8.4, family="monospace",
                 transform=ax_text.transAxes)
    fig.suptitle("Rotational Inertia Experiment: Data, Fits, and Calculated Results", fontsize=18, y=0.985)
    fig.text(0.02, 0.012, "All lengths and masses are averaged from the raw CSV. Units for J are kg m^2.", fontsize=9)
    fig.savefig(out_pdf, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    base = os.path.dirname(os.path.abspath(__file__)) or "."
    os.chdir(base)
    df, fits, fit_table, moment_table, diagnostics = build_analysis(CSV_FILE)
    make_pdf(df, fits, fit_table, moment_table, diagnostics, OUT_PDF)
    print("Saved:", OUT_PDF)
    print("Saved:", OUT_SUMMARY)
    print("\nMoment results:")
    print(moment_table.to_string(index=False, float_format=lambda x: f"{x:.6g}"))
    print("\nDiagnostics:")
    for k, v in diagnostics.items():
        print(f"{k}: {v:.6g}")
