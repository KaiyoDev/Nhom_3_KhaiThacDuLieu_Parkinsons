# M03 — Thống kê mô tả + Kiểm tra chất lượng dữ liệu

| Hạng mục | Giá trị |
|----------|---------|
| Mã thành viên | `M03` |
| Tên | `[CHƯA CẬP NHẬT]` |
| MSSV | `[CHƯA CẬP NHẬT]` |
| Vai trò dự kiến | Thống kê mô tả · kiểm tra chất lượng |
| Trạng thái ban đầu | `Todo` |

## Nhiệm vụ được giao (xem `TASK_ASSIGNMENTS.md`)

| Mã | Nhiệm vụ | Tóm tắt |
|----|----------|---------|
| M03-T1 | Thống kê mô tả | Mean/median/std/min/max, skew, kurtosis theo feature |
| M03-T2 | Kiểm tra chất lượng | Cân bằng label (0/1), trùng lặp, khoảng bất thường, thiếu → đề xuất xử lý |
| M03-T3 | Báo cáo chất lượng tổng hợp | `results/quality_report.md` |

## Đầu vào cần nhận

- Canonical CSV: `data/processed/parkinsons_v1.csv` (M01-T2, sau S-T1).
- Danh sách vấn đề từ M02 (M02-T3: scale / candidate outlier).

## Đầu ra cần bàn giao

- Bảng thống kê mô tả (feature + `status`) → `results/` (local).
- Kết luận chất lượng: cân bằng label, mức độ thiếu/trùng, khoảng bất thường.
- `results/quality_report.md` (báo cáo + **đề xuất phương pháp xử lý cho M04**).

## Tiêu chí hoàn thành

- Số thống kê **đúng thực tế** (không làm tròn sai, không bịa).
- Có kết luận rõ: dữ liệu sẵn sàng ở mức nào, cần xử lý gì trước khi chạy mô hình.
- Đề xuất xử lý (loại/gộp/thay NaN, chuẩn hoá) phải **giải trình được** (tại sao).

## Checklist tự kiểm tra

- [ ] Thống kê mô tả đủ cho **mỗi** feature (22) + `status`.
- [ ] Có kiểm tra cân bằng label (số `0` vs `1`).
- [ ] Có kiểm tra trùng lặp, khoảng bất thường, NaN (báo rõ nếu có).
- [ ] `results/quality_report.md` có **đề xuất xử lý** cho M04 (loại/thay/thuận chuẩn hoá).
- [ ] Đã bàn giao đề xuất cho M04 (mở M04-T1).
- [ ] Đã cập nhật `TASK_BOARD.md` (chuyển M03-T1..T3 sang `Review`).
- [ ] Không commit dữ liệu thô; chỉ ghi kết quả trong `results/` (local).

## Người review dự kiến

- M03-T1: **M02** (so khớp với khám phá cấu trúc).
- M03-T2: **M04** (đủ cho tiền xử lý).
- M03-T3: **M01 (gate)** (nhất quán trước khi qua cổng GATE #1).

## Trạng thái ban đầu

`Todo` — chờ canonical CSV (M01-T2) + S-T1, và M02-T3 trước khi hoàn tất M03-T2.
