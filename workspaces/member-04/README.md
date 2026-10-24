# M04 — Tiền xử lý + PCA + Trực quan hóa

| Hạng mục | Giá trị |
|----------|---------|
| Mã thành viên | `M04` |
| Tên | `[CHƯA CẬP NHẬT]` |
| MSSV | `[CHƯA CẬP NHẬT]` |
| Vai trò dự kiến | Tiền xử lý · PCA · trực quan hóa |
| Trạng thái ban đầu | `Todo` |

## Nhiệm vụ được giao (xem `TASK_ASSIGNMENTS.md`)

| Mã | Nhiệm vụ | Tóm tắt |
|----|----------|---------|
| M04-T1 | Tiền xử lý + feature matrix | Chuẩn hoá, xử lý NaN (theo M03), tạo feature matrix 22 cột |
| M04-T2 | PCA | Chọn số thành phần (ngưỡng variance), plot |
| M04-T3 | Trực quan hóa | Histogram, heatmap tương quan, scatter PC1–PC2 vs `status` |

## Đầu vào cần nhận

- Canonical CSV: `data/processed/parkinsons_v1.csv` (M01-T2).
- Đề xuất xử lý dữ liệu: từ M03-T2/M03-T3 (báo cáo chất lượng).

## Đầu ra cần bàn giao

- Feature matrix (22 cột) chuẩn hoá + pipeline reproducible → `src/`/notebook (code), dữ liệu local.
- Kết quả PCA (số thành phần giữ + variance explain) + figure → `results/`.
- Bộ figure (histogram / heatmap / scatter PC1–PC2 vs label) → `results/`.

## Tiêu chí hoàn thành

- **Pipeline chạy lại được** cùng kết quả (quy ước seed, chuẩn hoá được ghi trong
  `docs/REPRODUCIBILITY.md`).
- PCA: nêu rõ **ngưỡng variance** chọn & số thành phần giữ lại.
- Figure có chú thích đầy đủ, gắn với số liệu thật (không "làm đẹp" bịa).

## Checklist tự kiểm tra

- [ ] Đã dùng **canonical CSV** (không CSV riêng), đã áp dụng đề xuất xử lý của M03.
- [ ] Feature matrix: đủ 22 cột, không còn `name`, dtype số.
- [ ] Đã ghi rõ phương pháp chuẩn hoá (vd StandardScaler) + xử lý NaN (nếu còn).
- [ ] PCA: có ngưỡng chọn, có figure thành phần.
- [ ] Bộ trực quan đủ 3 loại: histogram, heatmap, scatter PC1–PC2 vs `status`.
- [ ] Code nằm ở `src/`/`notebooks/`, kết quả/figure ở `results/` (local, không commit thô).
- [ ] Đã chuyển M04-T1..T3 sang `Review` + thông báo người review (M05, M06, M01).

## Người review dự kiến

- M04-T1: **M05** (đủ dùng cho model).
- M04-T2: **M06** (đủ dùng cho phân cụm).
- M04-T3: **M01 (gate)** (nhất quán hình ảnh/kết quả).

## Trạng thái ban đầu

`Todo` — chờ M03-T2 (báo cáo chất lượng) + canonical CSV (S-T1) trước khi chạy M04-T1.
