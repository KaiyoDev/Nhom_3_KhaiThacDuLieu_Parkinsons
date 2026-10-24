# M02 — Khám phá cấu trúc & kiểu dữ liệu

| Hạng mục | Giá trị |
|----------|---------|
| Mã thành viên | `M02` |
| Tên | `[CHƯA CẬP NHẬT]` |
| MSSV | `[CHƯA CẬP NHẬT]` |
| Vai trò dự kiến | Khám phá cấu trúc & kiểu dữ liệu |
| Trạng thái ban đầu | `Todo` |

## Nhiệm vụ được giao (xem `TASK_ASSIGNMENTS.md`)

| Mã | Nhiệm vụ | Tóm tắt |
|----|----------|---------|
| M02-T1 | Khám phá cấu trúc & dtype | Số dòng/cột, dtype từng cột, NaN, trùng lặp, khoảng (min/max) |
| M02-T2 | Bản đồ nhóm đặc trưng | Nhóm jitter/shimmer/noise/nonlinear/frequency, bổ sung `DATA_DICTIONARY.md` |
| M02-T3 | Phát hiện vấn đề | Chênh lệch scale giữa nhóm feature, candidate outlier → bàn M03 & M04 |

## Đầu vào cần nhận

- Canonical CSV: `data/processed/parkinsons_v1.csv` + `schema_v1.md` (từ M01-T2).
- `DATA_DICTIONARY.md` (ý nghĩa cột đã xác minh).
- **Cần S-T1 đã xác nhận** (toàn nhóm đã đồng ý canonical CSV) trước khi bắt đầu.

## Đầu ra cần bàn giao

- Bảng khám phá cấu trúc (dòng/cột/dtype/thiếu/trùng/khoảng) → `results/` (local).
- Bổ sung cột *Kiểu / Thiếu* + *Ghi chú* trong `DATA_DICTIONARY.md` (M02-T1/T2).
- Danh sách vấn đề (scale, candidate outlier) → bàn giao M03 (chất lượng) & M04 (tiền xử lý) (M02-T3).

## Tiêu chí hoàn thành

- Chỉ mô tả những gì **đã kiểm tra** trên canonical CSV (không bịa).
- Có đánh giá: cân bằng label (`status`), mức độ thiếu/trùng (nếu có).
- Danh sách vấn đề rõ ràng, đủ cho M04 chọn phương pháp tiền xử lý.

## Checklist tự kiểm tra

- [ ] Đã đọc canonical CSV (không đọc bản CSV riêng).
- [ ] Ghi dtype, số NaN, trùng, min/max cho **mỗi** feature (22 cột) + `status`.
- [ ] Đã cập nhật `DATA_DICTIONARY.md` (cột Kiểu / Thiếu).
- [ ] Đã phân nhóm đặc trưng rõ (frequency/jitter/shimmer/noise/nonlinear).
- [ ] Danh sách vấn đề (scale/outlier) đã gửi M03 & M04, có ghi rõ ảnh hưởng.
- [ ] Kết quả ghi trong `results/` (local), không commit dữ liệu thô.
- [ ] Đã chuyển trạng thái M02-T1..T3 sang `Review` + thông báo người review (M03, M04).

## Người review dự kiến

- M02-T1: **M03** (so với thống kê).
- M02-T2: **M03** (ý nghĩa nhóm).
- M02-T3: **M04** (đủ cho tiền xử lý).

## Trạng thái ban đầu

`Todo` — chờ S-T1 (xác nhận canonical CSV) trước khi chuyển `In Progress`.
