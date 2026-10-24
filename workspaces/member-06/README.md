# M06 — Phân cụm + ARI + Hỗ trợ tổng hợp kết quả

| Hạng mục | Giá trị |
|----------|---------|
| Mã thành viên | `M06` |
| Tên | `[CHƯA CẬP NHẬT]` |
| MSSV | `[CHƯA CẬP NHẬT]` |
| Vai trò dự kiến | Phân cụm · ARI · hỗ trợ tổng hợp kết quả |
| Trạng thái ban đầu | `Todo` |

## Nhiệm vụ được giao (xem `TASK_ASSIGNMENTS.md`)

| Mã | Nhiệm vụ | Tóm tắt |
|----|----------|---------|
| M06-T1 | Phân cụm | KMeans + chọn K (silhouette/elbow), figure |
| M06-T2 | ARI | Adjusted Rand Index so cluster với nhãn `status` |
| M06-T3 | **Tổng hợp kết quả** (chủ trì M06) | `reports/summary.md`; M01 ký nhận nhất quán |

## Đầu vào cần nhận

- Feature matrix (22 cột) chuẩn hoá: từ M04-T1.
- Kết quả phân lớp: từ M05-T3.
- Kết quả ARI của chính mình (M06-T2).
- `results/` từ M02–M05 (để tổng hợp).

## Đầu ra cần bàn giao

- Kết quả phân cụm (K chọn + silhouette/elbow) + figure → `results/` (M06-T1).
- ARI (so cluster với `status`, nhiều K) → `results/` (M06-T2).
- `reports/summary.md` (bản thảo tổng hợp) → `reports/` (M06-T3).

## Tiêu chí hoàn thành

- ARI được tính **đúng** theo định nghĩa (so cluster với label thật, không bịa).
- Có so sánh K khác nhau (không chỉ 1 giá trị).
- `reports/summary.md` **nhất quán**: cùng canonical CSV, cùng quy ước metric,
  không mâu thuẫn với kết quả M02–M05. **M01 gate** (M01-T4/S-T2) trước khi hoàn thiện.

## Checklist tự kiểm tra

- [ ] Đã dùng **feature matrix từ M04** (không chạy lại tiền xử lý riêng).
- [ ] Chọn K có giải trình (silhouette/elbow), đã ghi ngưỡng + K giữ lại.
- [ ] ARI: so cluster với `status`, báo nhiều K (không chỉ K=2 nếu không có lý do).
- [ ] `reports/summary.md` tham chiếu các `results/` thật, không làm kết quả bịa.
- [ ] Đã thông báo M01 (gate) để ký nhận nhất quán trước khi hoàn thiện báo cáo.
- [ ] Code ở `src/`/`notebooks/`, kết quả + figure ở `results/`, tổng hợp ở `reports/` (local).
- [ ] Đã chuyển M06-T1..T3 sang `Review` + thông báo người review (M05, M01).

## Người review dự kiến

- M06-T1: **M05** (so với kết quả phân lớp, nhất quán cluster/label).
- M06-T2: **M01 (gate)** (ARI đúng, nhất quán).
- M06-T3: **M01 (gate)** (nhất quán toàn bộ trước khi hoàn thiện `reports/`).

## Trạng thái ban đầu

`Todo` — chờ M04-T1 (feature matrix) + M05-T3 trước khi hoàn tất M06-T3.

## Lưu ý đặc biệt (M06 ≠ M01)

M06 **chủ trì** tổng hợp kết quả (viết `reports/summary.md`); M01 chỉ đóng vai
**gate nhất quán** (M01-T4/S-T2). Đây là cách đảm bảo M01 không làm tất cả việc
tích hợp một mình (xem `PROJECT_WORKFLOW.md` mục 2).
