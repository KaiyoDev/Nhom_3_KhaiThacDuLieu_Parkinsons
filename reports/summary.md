# Báo cáo tổng hợp — Khai phá dữ liệu Parkinson (Nhóm 3)

> **Ngày tổng hợp:** 2026-11-23 · **Deadline bài tập:** 20/11/2026 (đã qua)
> **Đầu vào chung:** `data/processed/parkinsons_v1.csv` (canonical v1, 195 × 23, bỏ `name`)
> **Người tổng hợp:** M06 (chủ trì) · **Gate nhất quán:** M01 (S-T2)
> **Trạng thái:** đã nghiệm thu **21 / 21** nhiệm vụ; **GATE #1 (S-T1)** và **GATE #2 (S-T2)** đã ký.

---

## 1. Tổng quan

Dự án xây dựng quy trình khai phá dữ liệu hoàn chỉnh trên tập dữ liệu giọng nói Parkinson
(Oxford, UCI): khám phá & chất lượng → tiền xử lý & PCA → phân lớp có giám sát (F-score) →
phân cụm không giám sát (ARI). Mọi bước dùng **một canonical CSV duy nhất** và seed `42`.

| Sản phẩm | Nhiệm vụ | Đường dẫn |
|----------|----------|-----------|
| Khám phá + chất lượng | M02, M03 | `results/m02_exploration.md`, `results/quality_report.md`, `results/iqr_table.md` |
| Tiền xử lý + PCA + TVH | M04 | `results/m04_preprocessing_pca.md`, `results/figures/02_pca_scatter.png`, `results/figures/m04-t3_histograms.png`, `results/figures/m04-t3_corr_heatmap.png` |
| Phân lớp + F-score | M05 | `results/classification_report.md`, `results/m05_f1_cv.csv` |
| Phân cụm + ARI | M06 | `results/m06_clustering_report.md`, `results/m06_cluster_ari.csv`, `results/m06_dbscan_grid.csv`, `results/figures/m06_*.png` |
| Pipeline tổng hợp | M01 (lead) | `src/pipeline.py` → `results/pipeline_summary.json` |

---

## 2. Dữ liệu & chất lượng (M01–M03)

- **Kích thước:** 195 dòng × 23 cột (22 feature + `status`), `name` đã loại; **0 NaN, 0 trùng lặp**.
- **Nhãn:** `status=0` 48 mẫu (24.62%) · `status=1` 147 mẫu (75.38%) → **mất cân bằng**.
- **Thang đo:** chênh lệch lớn (`MDVP:Fhi(Hz)` ~102–592 so với `MDVP:Jitter(Abs)` ~7e-6–2.6e-4) → cần chuẩn hoá.
- **Candidate outlier (IQR 1.5):** 19/22 feature; 47/195 dòng (24.10%); nhiều nhất `NHR=19`,
  `MDVP:PPQ=15`, `MDVP:RAP`/`Jitter:DDP`/`MDVP:Jitter(%)=14`. Ba feature không có outlier:
  `MDVP:Fo(Hz)`, `RPDE`, `DFA`.
- **Độ lệch:** 14/22 feature có `|skew| > 1` (vd `NHR` skew 4.2207 / kurt 21.9950).
- **Đề xuất đã áp dụng:** `StandardScaler` trước PCA/mô hình; giữ outlier có kiểm soát;
  cân nhắc xử lý lệch nhãn khi đánh giá.

## 3. Tiền xử lý & PCA (M04)

- Tách `X` (22 feature) / `y` (`status`) với assert chặn nhãn và `name`.
- Chuẩn hoá `StandardScaler` (fit trên toàn bộ X cho PCA/phân cụm).

| Chỉ số PCA | Giá trị |
|------------|---------|
| PC1 | 58.9% |
| PC2 | 11.3% |
| PC1 + PC2 | **70.2%** |
| Thành phần đạt ≥ 90% | **6** (tích lũy 91.61%) |

Tương quan: 26/231 cặp feature có `|r| ≥ 0.9`; `Jitter:DDP ≈ 3 × MDVP:RAP`,
`Shimmer:DDA ≈ 3 × Shimmer:APQ3` (gần trùng thông tin).

## 4. Phân lớp (M05)

Thiết lập: **StratifiedKFold ngoài 10**, **GridSearchCV trong 5**, seed 42, scaler nằm trong
`Pipeline` (chống leakage); 3 mô hình KNN / SVM / Random Forest.

| Mô hình | F-score macro (test) | F-score weighted (test) | F-score macro (train) |
|---------|:--------------------:|:-----------------------:|:---------------------:|
| KNN | 0.8757 ± 0.0742 | 0.9073 ± 0.0578 | 0.9647 |
| SVM | **0.8904 ± 0.0804** | **0.9199 ± 0.0603** | 0.9787 |
| Random Forest | 0.8737 ± 0.1171 | 0.9103 ± 0.0824 | 1.0000 |

- Chênh lệch giữa mô hình (~0.016) nhỏ hơn độ lệch chuẩn fold (0.07–0.12) → không kết luận
  quá chắc chắn mô hình tốt nhất.
- Random Forest train = 1.0000, std lớn nhất → dấu hiệu overfit.
- Weighted cao hơn macro do lớp khỏe ít mẫu.

## 5. Phân cụm + ARI (M06)

- Đầu vào chỉ gồm 22 feature chuẩn hoá (có `assert`); nhãn `status` chỉ dùng khi tính ARI.
- **K-Means** K=2..10, `n_init=10`, seed 42; chọn K theo silhouette cực đại:

| K | Inertia | Silhouette | Cỡ cụm | ARI |
|---:|--------:|-----------:|---------|----:|
| **2** | 2817.2 | **0.4373** | `[165, 30]` | **−0.0978** |
| 3 | 2076.2 | 0.2763 | `[106, 77, 12]` | 0.0582 |
| 4 | 1822.4 | 0.2358 | `[91, 77, 23, 4]` | 0.0583 |
| 5 | 1595.5 | 0.2048 | `[73, 64, 32, 22, 4]` | 0.1000 |
| 6 | 1442.0 | 0.2138 | `[60, 51, 30, 28, 22, 4]` | 0.1058 |
| 7 | 1319.8 | 0.2094 | `[54, 51, 31, 24, 23, 8, 4]` | 0.0882 |
| 8 | 1230.5 | 0.2201 | `[53, 35, 32, 23, 23, 15, 10, 4]` | 0.0313 |
| 9 | 1157.0 | 0.2265 | `[52, 39, 25, 24, 21, 13, 9, 8, 4]` | 0.0574 |
| 10 | 1110.7 | 0.1896 | `[38, 35, 26, 23, 22, 18, 12, 9, 8, 4]` | 0.0481 |

- **DBSCAN:** `min_samples=5`, `eps=3.37` (knee) → **1 cụm (183 điểm)** + **12 nhiễu**, ARI **−0.0639**;
  lưới tham số cho ARI ∈ [−0.0744, 0.1625].
- **Nhận xét:** cụm K=2 tách nhóm nhỏ 30 mẫu (toàn `status=1`) khác biệt ở
  `Shimmer:APQ5`, `MDVP:Shimmer`, `MDVP:Shimmer(dB)` (đơn vị z-score); nhưng ARI ≈ 0/âm ⇒
  **cấu trúc cụm không khớp** ranh giới bệnh lý. Phân cụm đóng vai trò đối chiếu, không thay
  thế mô hình có giám sát.

## 6. Kết luận

1. Dữ liệu sạch (0 NaN/trùng) nhưng **lệch nhãn** (147/48) và **lệch thang đo** — đã xử lý
   bằng chuẩn hoá và CV stratified.
2. **Phân lớp đạt kết quả tốt:** F-score macro 0.87–0.89 trên 10-fold CV; SVM cao nhất
   (0.8904) nhưng chênh lệch giữa các mô hình nhỏ so với biến động giữa các fold.
3. **PCA** giữ 70.2% phương sai với 2 thành phần; 6 thành phần đạt 91.61%.
4. **Phân cụm không tách được cấu trúc khớp `status`** (ARI ≈ 0/âm) — bệnh lý cần tín hiệu có giám sát.
5. Toàn bộ số liệu tái lập được trên cùng canonical v1 + seed 42.

## 7. Hạn chế

- Mẫu nhỏ (195) và lệch nhãn; ~32 chủ thể (bản mô tả UCI ghi 31) nên cùng người có thể rơi vào cả train/test.
- PCA 2D chỉ giữ 70.2% phương sai.
- Phân cụm ARI thấp; DBSCAN chỉ 1 cụm + 12 nhiễu.
- Một số lần chạy dùng phiên bản thư viện khác nhau (vd M06: sklearn 1.9.1) nhưng số liệu
  vẫn khớp khi kiểm tra chéo.

## 8. Tái lập

- Seed `42`; CV phân lớp k ngoài 10 / trong 5; `StandardScaler`; F-score macro chính;
  PCA 2 thành phần (hoặc 6 để ≥90%); KMeans `n_init=10`, DBSCAN `eps=3.37/min_samples=5`.
- Lệnh tổng hợp: `python -m src.pipeline` → `results/pipeline_summary.json`
  (khớp PCA/F-score; phân cụm/ARI được kiểm tra chéo).
- Chi tiết: `docs/REPRODUCIBILITY.md`.

## 9. Đội ngũ

| Mã | Vai trò |
|----|---------|
| M01 | Điều phối · dữ liệu · gate |
| M02 | Khám phá cấu trúc & dtype |
| M03 | Thống kê mô tả · chất lượng |
| M04 | Tiền xử lý · PCA · trực quan |
| M05 | Phân lớp · CV · F-score |
| M06 | Phân cụm · ARI · tổng hợp (báo cáo này) |

Nguồn dataset: Oxford Parkinson's Disease Detection (Max Little), UCI ML Repository.
