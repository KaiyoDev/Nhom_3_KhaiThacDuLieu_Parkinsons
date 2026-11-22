"""Tiền xử lý dùng chung (M04-T1): nạp canonical CSV, tách X/y, chuẩn hóa.

Quy ước (docs/REPRODUCIBILITY.md): scaler = StandardScaler, seed = 42.
"""
from pathlib import Path

import pandas as pd
from sklearn.preprocessing import StandardScaler

CANONICAL = "data/processed/parkinsons_v1.csv"
LABEL = "status"


def find_root(start=None):
    """Tìm gốc project (thư mục chứa canonical CSV), chạy từ đâu cũng được."""
    start = Path(start) if start else Path.cwd()
    for p in [start, *start.parents]:
        if (p / CANONICAL).exists():
            return p
    raise FileNotFoundError("Không thấy canonical CSV (S-T1) -> Blocked, báo M01")


def load_xy(root=None):
    """Trả về (X, y): X = 22 feature (chưa chuẩn hóa), y = status."""
    root = Path(root) if root else find_root()
    df = pd.read_csv(root / CANONICAL)
    y = df[LABEL]
    X = df.drop(columns=[LABEL])
    assert X.shape[1] == 22 and LABEL not in X.columns and "name" not in X.columns
    return X, y


def make_scaler():
    """Scaler chuẩn của nhóm. Dùng trong Pipeline để tránh data leakage khi CV."""
    return StandardScaler()


def standardize(X):
    """Fit scaler trên toàn bộ X (không dùng nhãn). Trả về (Xs là DataFrame, scaler)."""
    scaler = make_scaler()
    Xs = pd.DataFrame(scaler.fit_transform(X), columns=X.columns, index=X.index)
    return Xs, scaler