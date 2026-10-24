# M04 — Tiền xử lý + PCA + Trực quan hóa (Work-order)

## 1. Thông tin
| | |
|---|---|
| Mã | `M04` |
| Tên / MSSV | `[CHƯA CẬP NHẬT]` |
| Vai trò | Tiền xử lý (feature matrix), PCA, trực quan hoá (scatter) |
| Trạng thái | `Todo` |

## 2. Bạn làm ở đâu
- **Notebook:** `notebooks/02_preprocessing_pca.ipynb`.
- **Các phần bạn phụ trách:** `Bước 1` thuộc tính liên tục · `Bước 2` tách `X`/`y` ·
  `Bước 3` thiếu/bất thường · `Bước 4` đề xuất & ghi phương án · `Bước 5` chuẩn hoá ·
  `Bước 6` PCA 2D · `Bước 7` scatter tô màu theo `status`.

> **Điểm mấu chốt:** kết quả của M04-T1 (feature matrix 22 cột đã chuẩn hoá) là **đầu vào
> cho cả M05 (notebook 03) lẫn M06 (notebook 04)**. Làm sai chuẩn hoá → 2 người bị ảnh hưởng.

## 3. Nhiệm vụ giao (theo `TASK_ASSIGNMENTS.md`)
| Mã | Việc | Nơi làm | Đầu vào | Đầu ra | Tiêu chí | Reviewer | Chặn bởi |
|----|------|---------|---------|--------|----------|----------|----------|
| M04-T1 | Tiền xử lý + feature matrix (22 cột) | nb02 Bước 1–5 | canonical CSV + `results/quality_report.md` (M03-T2) | pipeline reproducible + feature matrix chuẩn hoá (Xs) | code chạy lại được, scaler + xử lý NaN được ghi | M05 | M03-T2 |
| M04-T2 | PCA (giảm về 2D, chọn theo variance) | nb02 Bước 6 | M04-T1 (Xs) | kết quả PCA + tỷ lệ phương sai + figure | nêu rõ ngưỡng variance & số thành phần | M06 | M04-T1 |
| M04-T3 | Trực quan (scatter PC1–PC2 vs `status`) | nb02 Bước 7 | M04-T2 | figure (tô màu theo nhãn) | figure gắn số thật, chú thích đủ | M01 (gate) | M04-T2 |

## 4. Thứ tự thực hiện (cụ thể, trong `notebooks/02_preprocessing_pca.ipynb`)
0. **Chạy guard / điều kiện:** cần **`results/quality_report.md` (M03-T2)** + canonical CSV
   (M01-T2, S-T1). Nếu M03 chưa xong → **Blocked** (chờ M03-T2).
1. **Bước 1–2:** nạp canonical CSV, tách `X` (22 feature) + `y` (`status`). Chạy
   `assert "status" not in X.columns` (nhãn **không** làm feature).
2. **Bước 3–4:** xem lại NaN/outlier; **đề xuất + GHI LẠI phương án xử lý** (theo
   `quality_report.md` + `docs/REPRODUCIBILITY.md` — scaler mặc định `StandardScaler`).
   Quyết định này phải **ghi vào `results/` + `REPRODUCIBILITY.md`**.
3. **Bước 5:** chuẩn hoá (StandardScaler). Lưu `Xs` (feature matrix chuẩn hoá).
4. **Bước 6:** PCA về **2 thành phần** (để vẽ) + ghi `explained_variance_ratio_` (tỷ lệ
   phương sai PC1/PC2, tổng). Nếu cần nhiều hơn 2 thành phần (ngưỡng variance) → nêu rõ.
5. **Bước 7:** scatter **PC1 vs PC2, tô màu theo `status`** (label chỉ để tô màu/diễn giải).
   Lưu figure vào `results/figures/`.
6. Ghi **kết quả thật** vào bảng "Kết quả & nhận xét" (variance, phân tách).

## 5. Đầu vào cần nhận
- Canonical CSV (M01-T2, S-T1) + `results/quality_report.md` (M03-T2, đề xuất xử lý).

## 6. Đầu ra phải bàn giao
- **Feature matrix chuẩn hoá** (Xs) + pipeline reproducible (code trong notebook / `src/`).
- Kết quả PCA (tỷ lệ phương sai) + figure scatter PC1–PC2 (tô màu theo `status`) → `results/`.
- Quyết định chuẩn hoá **ghi trong** `docs/REPRODUCIBILITY.md`.

## 7. Tiêu chí nghiệm thu (đo được)
- `Xs` đúng 22 cột, không `name`/`status`; scaler + cách xử lý NaN **được ghi rõ**.
- PCA: có ngưỡng variance + số thành phần giữ (để vẽ = 2); figure có chú thích.
- Label `status` **không** nằm trong input PCA (đã assert).
- Pipeline **chạy lại** cho cùng kết quả (seed + phiên bản thư viện ghi lại).

## 8. Checklist tự kiểm
- [ ] Đã chờ M03-T2 (quality_report.md) + S-T1 trước khi chạy (nếu thiếu → Blocked).
- [ ] `assert "status" not in X.columns` (label không làm feature).
- [ ] Đã chuẩn hoá + **ghi quyết định** scaler/xử lý NaN (results + REPRODUCIBILITY).
- [ ] PCA 2D + tỷ lệ phương sai + figure PC1–PC2 tô màu theo `status`.
- [ ] Kết quả ghi trong `results/` (không bịa số); figure trong `results/figures/`.
- [ ] Đã chuyển M04-T1..T3 sang `Review` + thông báo reviewer (M05, M06, M01-gate).

## 9. Người review
M04-T1 → **M05** (đủ dùng cho mô hình) · M04-T2 → **M06** (đủ dùng cho phân cụm) · M04-T3 → **M01 (gate)**.

## 10. Bàn giao & Blocked
- Theo `HANDOFF.md` (5 dòng + test-report: `Xs.shape`, tỷ lệ phương sai PC1/PC2).
- **Blocked:** thiếu M03-T2 (chất lượng/xử lý) → ghi "chờ M03-T2", thông báo M01.

## 11. Trạng thái
`Todo` — chờ **M03-T2** (đề xuất xử lý) + **S-T1** (canonical CSV).
