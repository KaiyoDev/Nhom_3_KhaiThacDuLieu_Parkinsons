# M05 — Phân lớp + Cross-validation + F-score

| Hạng mục | Giá trị |
|----------|---------|
| Mã thành viên | `M05` |
| Tên | `[CHƯA CẬP NHẬT]` |
| MSSV | `[CHƯA CẬP NHẬT]` |
| Vai trò dự kiến | Phân lớp · cross-validation · F-score |
| Trạng thái ban đầu | `Todo` |

## Nhiệm vụ được giao (xem `TASK_ASSIGNMENTS.md`)

| Mã | Nhiệm vụ | Tóm tắt |
|----|----------|---------|
| M05-T1 | Train/test + k-fold CV | Quy ước split, k, seed (ghi trong `docs/REPRODUCIBILITY.md`) |
| M05-T2 | Mô hình phân lớp baseline + F-score | ≥2 mô hình (vd kNN/LogReg/SVM), F-score macro/weighted theo CV |
| M05-T3 | Báo cáo kết quả phân lớp | `results/classification_report.md` (so sánh giữa các mô hình) |

## Đầu vào cần nhận

- Feature matrix (22 cột) chuẩn hoá: từ M04-T1.
- Canonical CSV (nguồn gốc): `data/processed/parkinsons_v1.csv`.

## Đầu ra cần bàn giao

- Quy ước CV (k, seed, split) ghi trong `docs/REPRODUCIBILITY.md` (M05-T1).
- Kết quả F-score (macro/weighted) theo ≥2 mô hình + bảng so sánh → `results/` (M05-T2).
- `results/classification_report.md` (M05-T3).

## Tiêu chí hoàn thành

- Kết quả được đánh giá bằng **k-fold CV** (không chỉ train/test đơn lẻ).
- Chỉ số chính là **F-score** (nêu rõ macro/weighted, kèm precision/recall nếu cần).
- Kết quả **reproducible**: seed, k, data split, phiên bản thư viện được ghi lại.
- Không "overfit" vào test set (test set chỉ dùng **một lần** cuối).

## Checklist tự kiểm tra

- [ ] Đã dùng **feature matrix từ M04** (không chạy lại tiền xử lý riêng).
- [ ] Quy ước k-fold CV + seed đã ghi rõ trong `docs/REPRODUCIBILITY.md`.
- [ ] Chạy ≥2 mô hình (vd kNN, LogisticRegression, SVM) + báo cáo F-score (macro/weighted).
- [ ] Kết quả so sánh được giữa các mô hình (có bảng).
- [ ] Chưa "quá khớp" (F-score test < F-score CV là cảnh báo; ghi chú nếu gặp).
- [ ] Code nằm ở `src/`/`notebooks/`, kết quả ở `results/` (local, không commit dữ liệu thô).
- [ ] Đã chuyển M05-T1..T3 sang `Review` + thông báo M01 (gate) & M06.

## Người review dự kiến

- M05-T1: **M01 (gate)** (quy ước CV nhất quán).
- M05-T2: **M01 (gate) + M06** (chủ trì tổng hợp).
- M05-T3: **M06** (tham chiếu trước khi viết `reports/summary.md`).

## Trạng thái ban đầu

`Todo` — chờ M04-T1 (feature matrix) trước khi chạy M05-T1.
