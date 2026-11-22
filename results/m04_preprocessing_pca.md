# M04 — Tiền xử lý, PCA và trực quan hóa

- **Mã nhiệm vụ:** M04-T1, M04-T2, M04-T3
- **Ngày:** 2026-11-05
- **Đầu vào duy nhất:** `data/processed/parkinsons_v1.csv` (canonical v1, 195 × 23)
- **Notebook:** `notebooks/02_preprocessing_pca.ipynb` · **Module dùng chung:** `src/preprocessing.py`

## Tham số và môi trường

| Hạng mục | Giá trị |
|---|---|
| Seed | 42 |
| Scaler | `StandardScaler`, fit trên 22 feature (không dùng `status`) |
| PCA | `n_components=2`, `random_state=42`; ngưỡng tham chiếu ≥ 90% phương sai |
| Outlier | Quy tắc IQR (1.5), chỉ quan sát, không loại dòng |
| Python / scikit-learn / pandas / numpy | 3.14.6 / 1.8.0 / 3.0.2 / 2.4.4 |

## M04-T1 — Tiền xử lý

| Kiểm tra | Kết quả |
|---|---:|
| `X` (feature) | 195 × 22 |
| Feature kiểu số | 22/22 (`float64`) |
| Tổng NaN / dòng trùng | 0 / 0 |
| Cột có outlier (IQR) | 19 / 22 |
| Dòng có ≥ 1 outlier | 47 / 195 |
| Outlier nhiều nhất | `NHR` (19), `MDVP:PPQ` (15), `MDVP:RAP`, `Jitter:DDP`, `MDVP:Jitter(%)` (14 mỗi cột) |

Quyết định: giữ nguyên 195 dòng, chuẩn hóa bằng `StandardScaler`. Sau chuẩn hóa `Xs` có shape (195, 22), mean ≈ 0, std ≈ 1, không có NaN.

## M04-T2 — PCA

| Hạng mục | Giá trị |
|---|---:|
| PC1 | 58.9% |
| PC2 | 11.3% |
| Tổng PC1 + PC2 | 70.2% |
| Số thành phần để đạt ≥ 90% | 6 (tích lũy 91.61%) |

Giữ 2 thành phần để vẽ; muốn đạt ngưỡng 90% của nhóm cần 6 thành phần.

## M04-T3 — Trực quan hóa

| Hình | File |
|---|---|
| Scatter PC1–PC2 tô theo `status` | `results/figures/02_pca_scatter.png` |
| Histogram 22 feature theo `status` | `results/figures/m04-t3_histograms.png` |
| Heatmap tương quan Pearson | `results/figures/m04-t3_corr_heatmap.png` |

Điểm chính: hai nhóm tách một phần, chồng lấp đáng kể trên PC1–PC2; 14/22 feature lệch phải; 26/231 cặp feature có |r| ≥ 0.9.

## Bàn giao

- **M05 / M06:** nạp dữ liệu bằng `load_xy()`, `make_scaler()`, `standardize()` trong `src/preprocessing.py`.
- **M05:** `Xs` được fit trên toàn bộ 195 dòng nên chỉ dùng cho PCA/phân cụm. Khi CV phân lớp, đặt `make_scaler()` trong Pipeline để tránh data leakage.

## Vấn đề chưa giải quyết

- M03-T2 (`quality_report.md`) chưa bàn giao; cần đối chiếu lại khi có đề xuất xử lý.
- Số outlier `NHR`: M02 ghi 20, M04 ra 19 (cùng quy tắc IQR, cùng canonical CSV); đã/sẽ báo M02.
- `Jitter:DDP` = 3 × `MDVP:RAP` và `Shimmer:DDA` = 3 × `Shimmer:APQ3` (r = 1.0): trùng thông tin hoàn toàn, canonical CSV giữ nguyên.