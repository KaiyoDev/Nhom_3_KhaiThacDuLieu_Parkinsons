"""Pipeline tổng hợp (integration) trên canonical CSV v1.

Chạy từ gốc project:

    python -m src.pipeline

Thứ tự thực hiện: kiểm tra dữ liệu → tiền xử lý/PCA → phân lớp (CV 10-fold)
→ ghi ``results/pipeline_summary.json``. Module tái dùng ``src/preprocessing.py``
và dùng chung quy ước trong ``docs/REPRODUCIBILITY.md`` (seed 42, k ngoài 10 / trong 5).
"""
from __future__ import annotations

import datetime as dt
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import sklearn
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, StratifiedKFold, cross_validate
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

from src.preprocessing import find_root, load_xy, standardize

SEED = 42
K_OUTER = 10
K_INNER = 5


def dataset_checks(df: pd.DataFrame) -> dict:
    """Các chỉ báo kiểm tra dữ liệu (không bịa số)."""
    X = df.drop(columns=["status"])
    q1, q3 = X.quantile(0.25), X.quantile(0.75)
    iqr = q3 - q1
    mask = (X < q1 - 1.5 * iqr) | (X > q3 + 1.5 * iqr)
    return {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "features": int(X.shape[1]),
        "missing_cells": int(df.isna().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "label_counts": {
            str(int(k)): int(v) for k, v in df["status"].value_counts().sort_index().items()
        },
        "iqr_outlier_columns": int((mask.sum() > 0).sum()),
        "iqr_outlier_rows": int(mask.any(axis=1).sum()),
        "nhr_outliers": int(mask["NHR"].sum()),
    }


def run_pca(Xs: pd.DataFrame) -> dict:
    """PCA 2 thành phần để vẽ + số thành phần để đạt ngưỡng 90%."""
    pca2 = PCA(n_components=2, random_state=SEED).fit(Xs)
    evr = pca2.explained_variance_ratio_
    full = PCA(random_state=SEED).fit(Xs)
    cum = np.cumsum(full.explained_variance_ratio_)
    n90 = int(np.argmax(cum >= 0.90) + 1)
    return {
        "pc1": round(float(evr[0]), 4),
        "pc2": round(float(evr[1]), 4),
        "pc1_pc2_total": round(float(evr.sum()), 4),
        "n_components_for_90pct": n90,
        "cum_variance_at_90pct": round(float(cum[n90 - 1]), 4),
    }


def run_classification(X: pd.DataFrame, y: pd.Series) -> list[dict]:
    """3 mô hình (KNN, SVM, RandomForest) với CV lồng nhau, chống leakage."""
    outer_cv = StratifiedKFold(n_splits=K_OUTER, shuffle=True, random_state=SEED)
    inner_cv = StratifiedKFold(n_splits=K_INNER, shuffle=True, random_state=SEED)
    models = {
        "KNN": (
            Pipeline([("scaler", StandardScaler()), ("clf", KNeighborsClassifier())]),
            {"clf__n_neighbors": [3, 5, 7]},
        ),
        "SVM": (
            Pipeline([("scaler", StandardScaler()), ("clf", SVC(random_state=SEED))]),
            {"clf__C": [0.1, 1, 10]},
        ),
        "RandomForest": (
            Pipeline([("scaler", StandardScaler()),
                      ("clf", RandomForestClassifier(random_state=SEED))]),
            {"clf__n_estimators": [50, 100]},
        ),
    }
    rows = []
    for name, (pipe, grid) in models.items():
        search = GridSearchCV(pipe, grid, cv=inner_cv, scoring="f1_macro", n_jobs=-1)
        res = cross_validate(
            search, X, y, cv=outer_cv,
            scoring={"f1_macro": "f1_macro", "f1_weighted": "f1_weighted"},
            return_train_score=True, return_estimator=True,
        )
        rows.append({
            "model": name,
            "f1_macro_test_mean": round(float(res["test_f1_macro"].mean()), 4),
            "f1_macro_test_std": round(float(res["test_f1_macro"].std()), 4),
            "f1_weighted_test_mean": round(float(res["test_f1_weighted"].mean()), 4),
            "f1_weighted_test_std": round(float(res["test_f1_weighted"].std()), 4),
            "f1_macro_train_mean": round(float(res["train_f1_macro"].mean()), 4),
            "best_params_per_fold": [est.best_params_ for est in res["estimator"]],
            "grid": {k: [int(v) if isinstance(v, (int, np.integer)) else v for v in vals]
                     for k, vals in grid.items()},
        })
    return rows


def main() -> None:
    root = find_root()
    df = pd.read_csv(root / "data" / "processed" / "parkinsons_v1.csv")
    checks = dataset_checks(df)
    X, y = load_xy(root)
    Xs, _ = standardize(X)

    summary = {
        "generated_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
        "canonical_csv": "data/processed/parkinsons_v1.csv",
        "seed": SEED,
        "cv": {"k_outer": K_OUTER, "k_inner": K_INNER},
        "versions": {
            "python": sys.version.split()[0],
            "numpy": np.__version__,
            "pandas": pd.__version__,
            "scikit_learn": sklearn.__version__,
        },
        "dataset": checks,
        "pca": run_pca(Xs),
        "classification": run_classification(X, y),
    }

    out = root / "results" / "pipeline_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print("Đã ghi:", out)


if __name__ == "__main__":
    main()
