"""Vẽ sơ đồ quy trình (pipeline) cho báo cáo Bài tập lớn - Nhom 3 Parkinson.

Ra file: ../figures/pipeline_diagram.png
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures" / "pipeline_diagram.png"

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["axes.unicode_minus"] = False

fig, ax = plt.subplots(figsize=(13.2, 7.4), dpi=180)
ax.set_xlim(0, 132)
ax.set_ylim(0, 74)
ax.axis("off")

C_RAW = "#E8EEF7"
C_DATA = "#D6E4F0"
C_STEP = "#EAF3EA"
C_RESULT = "#FFF1D6"
C_GATE = "#FBE3E3"
EDGE = "#33506E"


def box(x, y, w, h, text, fc="#EAF3EA", ec=EDGE, fs=10.5, bold=False, r=1.6):
    patch = FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad=0.0,rounding_size={r}",
        linewidth=1.4, edgecolor=ec, facecolor=fc,
    )
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fs, color="#17233A",
            fontweight="bold" if bold else "normal", linespacing=1.35)


def arrow(x1, y1, x2, y2, label=None, lx=0, ly=0, style="-"):
    a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                        mutation_scale=13, linewidth=1.4,
                        color=EDGE, linestyle=style)
    ax.add_patch(a)
    if label:
        ax.text((x1 + x2) / 2 + lx, (y1 + y2) / 2 + ly, label,
                ha="center", va="center", fontsize=9, color="#7A2E2E",
                fontstyle="italic")


# Row 1: data flow
box(2, 58, 26, 11, "Dữ liệu thô\nD07 - parkinsons.data.xlsx\n195 × 24 (gồm name)", C_RAW, fs=9.5)
box(34, 58, 26, 11, "Canonical CSV v1\nparkinsons_v1.csv\n195 × 23 (bỏ name)", C_DATA, fs=9.5, bold=True)
box(66, 58, 26, 11, "GATE #1\nThống nhất đầu vào chung\n(S-T1)", C_GATE, fs=9.5, bold=True)
box(98, 58, 32, 11, "Tiền xử lý: StandardScaler\nX = 22 feature · y = status", C_STEP, fs=9.5)

arrow(28, 63.5, 34, 63.5)
arrow(60, 63.5, 66, 63.5)
arrow(92, 63.5, 98, 63.5)

# Row 2: analysis branches
box(2, 40, 30, 12, "Khám phá & chất lượng dữ liệu\nM02 (khám phá, dtype) +\nM03 (thống kê, IQR, outlier)", "#EAF3EA", fs=9.5)
box(38, 40, 28, 12, "PCA\nM04 · PC1 58.9% + PC2 11.3%\n= 70.2%; 6 comps 91.61%", C_RESULT, fs=9.5)
box(72, 40, 28, 12, "Phân loại có giám sát\nM05 · KNN / SVM / RF\nStratified 10-fold CV", C_RESULT, fs=9.5)
box(106, 40, 24, 12, "Phân cụm không giám sát\nM06 · KMeans / DBSCAN\nARI so với status", C_RESULT, fs=9.5)

arrow(50, 58, 17, 52, "dùng chung canonical v1", lx=-16, ly=2)
arrow(50, 58, 52, 52)
arrow(80, 58, 86, 52)
arrow(98, 58, 118, 52)

# Row 3: outputs
box(2, 22, 30, 11, "Báo cáo chất lượng & EDA\nresults/quality_report.md · iqr_table.md", "#EAF3EA", fs=9.5)
box(38, 22, 28, 11, "Trực quan PCA\nfigures/ (scatter, histogram, heatmap)", "#EAF3EA", fs=9.5)
box(72, 22, 28, 11, "F-score macro (test)\nKNN 0.8757 · SVM 0.8904 · RF 0.8737", C_RESULT, fs=9.5, bold=True)
box(106, 22, 24, 11, "ARI KMeans K=2: -0.0978\nDBSCAN: -0.0639", C_RESULT, fs=9.5, bold=True)

arrow(17, 40, 17, 33)
arrow(52, 40, 52, 33)
arrow(86, 40, 86, 33)
arrow(118, 40, 118, 33)

# Integration / gate 2
box(30, 4, 72, 11, "Tổng hợp & GATE #2 (S-T2): cùng canonical v1 · cùng seed 42 · cùng metric/quy ước\nM06 chủ trì · M01 ký nhất quán → reports/summary.md · notebooks/05_integration_report.ipynb",
     C_GATE, fs=10, bold=True)

arrow(17, 22, 45, 15)
arrow(52, 22, 60, 15)
arrow(86, 22, 75, 15)
arrow(118, 22, 90, 15)

fig.tight_layout()
fig.savefig(OUT, bbox_inches="tight", facecolor="white")
print("Saved:", OUT)
