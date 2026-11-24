"""Vẽ lại 2 hình minh chứng dùng trong báo cáo (không dùng dấu gạch ngang).

- docs/images/eda_summary.png: phân bố nhãn + top outlier theo IQR.
- docs/images/f1_scores.png: F-score macro/weighted 10-fold CV của 3 mô hình.

Chạy: python bao_cao/scripts/make_proof_figures.py
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]  # gốc repo
DOCS = ROOT / "docs" / "images"
BAO = ROOT / "bao_cao" / "figures"

plt.rcParams["font.family"] = "DejaVu Sans"

df = pd.read_csv(ROOT / "data" / "processed" / "parkinsons_v1.csv")
feat = [c for c in df.columns if c not in ("status", "name")]
label_counts = df["status"].value_counts().sort_index()

# IQR 1.5
q1 = df[feat].quantile(0.25, interpolation="linear")
q3 = df[feat].quantile(0.75, interpolation="linear")
iqr = q3 - q1
out = ((df[feat] < (q1 - 1.5 * iqr)) | (df[feat] > (q3 + 1.5 * iqr))).sum()
top = out.sort_values(ascending=False).head(10)

# ---- Hình 1: EDA summary ----
fig, axes = plt.subplots(1, 2, figsize=(13.5, 4.8), dpi=150)
ax = axes[0]
bars = ax.bar(["0 - Khỏe", "1 - Parkinson"], label_counts.values,
              color=["#4C72B0", "#C44E52"], edgecolor="black", linewidth=0.6)
for b, v in zip(bars, label_counts.values):
    ax.text(b.get_x() + b.get_width() / 2, v + 3, str(v),
            ha="center", va="bottom", fontweight="bold")
ax.set_title("Phân bố nhãn status (n=195)")
ax.set_ylabel("Số mẫu")
ax.set_ylim(0, 165)

ax = axes[1]
names = top.index.tolist()[::-1]
vals = top.values.tolist()[::-1]
bars = ax.barh(names, vals, color="#55A868", edgecolor="black", linewidth=0.6)
for b, v in zip(bars, vals):
    ax.text(v + 0.25, b.get_y() + b.get_height() / 2, str(v),
            va="center", fontweight="bold")
ax.set_title("Top 10 feature có nhiều candidate outlier (IQR 1.5)")
ax.set_xlabel("Số điểm ngoài ngưỡng")
ax.set_xlim(0, 21)

fig.suptitle("Tổng quan dữ liệu - canonical CSV v1 (195 × 23)",
             fontsize=14, fontweight="bold")
fig.tight_layout(rect=[0, 0, 1, 0.94])
fig.savefig(DOCS / "eda_summary.png", facecolor="white")
plt.close(fig)

# ---- Hình 2: F-score ----
models = ["KNN", "SVM", "RandomForest"]
macro = np.array([0.8757, 0.8904, 0.8737])
macro_std = np.array([0.0742, 0.0804, 0.1171])
weighted = np.array([0.9073, 0.9199, 0.9103])
weighted_std = np.array([0.0578, 0.0603, 0.0824])

base = 0.75
x = np.arange(len(models))
w = 0.34

fig, ax = plt.subplots(figsize=(9.2, 5.6), dpi=160)
b1 = ax.bar(x - w / 2, macro - base, w, bottom=base, color="#4C72B0",
            edgecolor="black", linewidth=0.6, label="F-score macro (test)")
b2 = ax.bar(x + w / 2, weighted - base, w, bottom=base, color="#DD8452",
            edgecolor="black", linewidth=0.6, label="F-score weighted (test)")
ax.errorbar(x - w / 2, macro, yerr=macro_std, fmt="none", ecolor="black",
            elinewidth=1.3, capsize=4)
ax.errorbar(x + w / 2, weighted, yerr=weighted_std, fmt="none", ecolor="black",
            elinewidth=1.3, capsize=4)

for xi, v, s in zip(x - w / 2, macro, macro_std):
    ax.text(xi, v + s + 0.004, f"{v:.4f}", ha="center", va="bottom", fontsize=9.5)
for xi, v, s in zip(x + w / 2, weighted, weighted_std):
    ax.text(xi, v + s + 0.004, f"{v:.4f}", ha="center", va="bottom", fontsize=9.5)

ax.set_xticks(x)
ax.set_xticklabels(models)
ax.set_ylim(base - 0.015, 1.0)
ax.set_yticks(np.arange(0.75, 1.01, 0.05))
ax.set_ylabel("F-score")
ax.set_title("Kết quả phân loại - 10-fold CV (seed 42, canonical v1)")
ax.legend(loc="lower right", framealpha=0.95)
ax.grid(axis="y", linestyle=":", alpha=0.4)
fig.tight_layout()
fig.savefig(DOCS / "f1_scores.png", facecolor="white")
plt.close(fig)

for name in ("eda_summary.png", "f1_scores.png"):
    src = DOCS / name
    dst = BAO / name
    dst.write_bytes(src.read_bytes())
    print("Saved:", src)
    print("Copied:", dst)
