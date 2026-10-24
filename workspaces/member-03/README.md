# M03 — Thống kê mô tả + Kiểm tra chất lượng dữ liệu (Work-order)

## 1. Thông tin
| | |
|---|---|
| Mã | `M03` |
| Tên / MSSV | `[CHƯA CẬP NHẬT]` |
| Vai trò | Thống kê mô tả, kiểm tra chất lượng, báo cáo chất lượng |
| Trạng thái | `Todo` |

## 2. Bạn làm ở đâu
- **Notebook:** `notebooks/01_data_exploration.ipynb` (dùng chung với M02, nhưng **các bước khác nhau**).
- **Các phần bạn phụ trách:**
  - `Bước 5` Số mẫu theo từng nhãn · `Bước 6` min / max / mean (thống kê mô tả).
  - `Bước 7` (phần **chất lượng**: thiếu / trùng / bất thường) — M02 viết phần "cấu trúc/scale/
    outlier", **M03 viết phần "thiếu/trùng/bất thường"**.
  - **Báo cáo:** `results/quality_report.md` (M03-T3).

## 3. Nhiệm vụ giao (theo `TASK_ASSIGNMENTS.md`)
| Mã | Việc | Nơi làm | Đầu vào | Đầu ra | Tiêu chí | Reviewer | Chặn bởi |
|----|------|---------|---------|--------|----------|----------|----------|
| M03-T1 | Thống kê mô tả | nb01 Bước 5–6 | canonical CSV (M01-T2) | bảng mean/median/std/min/max (+skew/kurtosis nếu cần) | số ĐÚNG THỰC TẾ, có phân bố | M02 | M01-T2 (S-T1) |
| M03-T2 | Kiểm tra chất lượng | nb01 Bước 7 (chất lượng) | M02-T3 (danh sách vấn đề) | kết luận cân bằng label, trùng, bất thường + **đề xuất xử lý cho M04** | có kết luận "sẵn sàng / cần xử lý gì" | M04 | M02-T3 |
| M03-T3 | Báo cáo chất lượng tổng hợp | `results/quality_report.md` | M03-T1, M03-T2 | báo cáo + đề xuất | phản ánh thực tế, có đề xuất rõ | M01 (gate) | M03-T1, M03-T2 |

## 4. Thứ tự thực hiện (cụ thể, trong `notebooks/01_data_exploration.ipynb`)
0. **Chạy guard cell**: chưa có canonical CSV → **Blocked** (chờ M01-T2/S-T1). Có → tiếp tục.
   (M02 có thể chạy Bước 1–4 song song; bạn tập trung Bước 5–6 + phần chất lượng Bước 7.)
1. **Bước 5:** `df["status"].value_counts()` + `value_counts(normalize=True)` → ghi số mẫu
   lớp 0 và lớp 1, tỉ lệ (xác nhận cân bằng / lệch).
2. **Bước 6:** `df.describe().T` (mean/median/std/min/max per feature). Nhận xét feature có
   **scale cực đoan** (để M04 chuẩn hoá). Chỉ ghi **kết quả chạy thật**.
3. **Bước 7 (phần M03):** `df.isna().sum()` (thiếu), `df.duplicated().sum()` (trùng). Kết hợp
   danh sách vấn đề M02-T3 → **đề xuất phương án xử lý** (loại dòng / impute / giữ) cho M04.
4. **M03-T3:** viết `results/quality_report.md`: thống kê (Bước 5–6) + chất lượng (Bước 7) +
   **đề xuất xử lý** rõ ràng (đây là input cho `notebooks/02_preprocessing_pca.ipynb`).
5. Ghi kết quả vào **bảng "Kết quả & nhận xét"** (phần của bạn) trong notebook.

## 5. Đầu vào cần nhận
- Canonical CSV (M01-T2, qua **S-T1**).
- **M02-T3** (danh sách vấn đề cấu trúc/scale/outlier) — để hoàn thành M03-T2.
  (Nếu M02-T3 chưa xong → M03-T1 vẫn làm được; M03-T2 chờ M02-T3.)

## 6. Đầu ra phải bàn giao
- Bảng thống kê (Bước 5–6) trong notebook + `results/`.
- `results/quality_report.md` (M03-T3): thống kê + chất lượng + **đề xuất xử lý** (đủ để M04 làm tiếp).
- Bàn giao **M04** (đề xuất xử lý) và thông báo M01 (gate).

## 7. Tiêu chí nghiệm thu (đo được)
- Bảng thống kê có mean/median/std/min/max cho **mỗi** feature + `status` (số thật).
- `quality_report.md` có: cân bằng label (số 0/1), NaN/trùng, **đề xuất xử lý** có giải trình.
- M04 đọc được report và bắt đầu `notebooks/02_preprocessing_pca.ipynb` được.

## 8. Checklist tự kiểm
- [ ] Đã chạy guard (không Block).
- [ ] Bước 5: số mẫu + tỉ lệ label đúng (từ chạy thật).
- [ ] Bước 6: thống kê đủ feature, có nhận xét scale.
- [ ] Bước 7 (phần M03): NaN/trùng đã kiểm tra + kết hợp M02-T3.
- [ ] `results/quality_report.md` có **đề xuất xử lý** rõ (loại/impute/giữ + vì sao).
- [ ] Đã bàn giao M04 + thông báo M01 (gate); chuyển M03-T1..T3 sang `Review` trong `TASK_BOARD.md`.

## 9. Người review
M03-T1 → **M02** · M03-T2 → **M04** · M03-T3 → **M01 (gate)**.

## 10. Bàn giao & Blocked
- Theo `HANDOFF.md` (5 dòng + test-report: số mẫu 0/1, NaN count, đề xuất xử lý).
- **Blocked:** M03-T2 cần **M02-T3** (vấn đề). Nếu M02 chưa xong → M03-T1 vẫn chạy được;
  M03-T2 đánh `Blocked` (chờ M02-T3), ghi rõ trong `TASK_BOARD.md`.

## 11. Trạng thái
`Todo` — M03-T1 chờ **S-T1** (M01-T2); M03-T2 chờ **M02-T3**.
