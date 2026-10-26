# TASK_BOARD — Bảng trạng thái công việc (Nhóm 3 · Parkinson)

> **5 trạng thái:** `Todo` · `In Progress` · `Review` · `Blocked` · `Done`.
> Ban đầu **mọi nhiệm vụ ở `Todo`**. Không giả lập tiến độ: chỉ chuyển trạng thái
> khi có bằng chứng (đã làm xong / đã review / đang bị chặn).
>
> Quy tắc chuyển trạng thái (xem `PROJECT_WORKFLOW.md`):
> - `Todo → In Progress`: phụ trách bắt đầu (đầu vào đã sẵn sàng).
> - `In Progress → Review`: phụ trách hoàn thành + qua checklist tự kiểm tra.
> - `Review → Done`: **người review** xác nhận đạt tiêu chí nghiệm thu.
> - Bất kỳ lúc nào thiếu đầu vào / phụ thuộc chưa xong → `Blocked` (ghi rõ vì sao).
> - M01 là người điều phối cập nhật bảng này khi có chuyển trạng thái.

## Hạng mục

| Mã | Nhiệm vụ | Phụ trách | Trạng thái | Ghi chú / Chặn bởi |
|----|----------|-----------|:----------:|--------------------|
| M01-T1 | Chuẩn bị dữ liệu thô → `data/raw/` | M01 | **Done** | data ở `data/raw/` + `manifest.md`; đã commit |
| M01-T2 | Sản xuất canonical processed CSV | M01 | **Done** | v1 đã tạo + commit (`data/processed/`); chờ review S-T1 |
| M01-T3 | Gate đầu vào cho M02/M03/M04 | M01 | **In Progress** | gate mở, chờ S-T1 (toàn nhóm xác nhận) |
| M01-T4 | Kiểm tra nhất quán dữ liệu & kết quả (gate) | M01 | Todo | Chặn bởi M05-T3, M06-T2 |
| M02-T1 | Khám phá cấu trúc & dtype | M02 | Todo | Chặn bởi M01-T2 |
| M02-T2 | Bản đồ nhóm đặc trưng | M02 | Todo | Chặn bởi M02-T1 |
| M02-T3 | Phát hiện vấn đề (scale / outlier) | M02 | Todo | Chặn bởi M02-T1 |
| M03-T1 | Thống kê mô tả | M03 | Todo | Chặn bởi M01-T2 |
| M03-T2 | Kiểm tra chất lượng dữ liệu | M03 | Todo | Chặn bởi M02-T3 |
| M03-T3 | Báo cáo chất lượng tổng hợp | M03 | Todo | Chặn bởi M03-T1, M03-T2 |
| M04-T1 | Tiền xử lý + feature matrix (22 cột) | M04 | Todo | Chặn bởi M03-T2 |
| M04-T2 | PCA (chọn số thành phần) | M04 | Todo | Chặn bởi M04-T1 |
| M04-T3 | Trực quan hóa (hist/heatmap/scatter PC) | M04 | Todo | Chặn bởi M04-T2 |
| M05-T1 | Train/test + k-fold CV | M05 | Todo | Chặn bởi M04-T1 |
| M05-T2 | Phân lớp baseline + F-score | M05 | Todo | Chặn bởi M05-T1 |
| M05-T3 | Báo cáo kết quả phân lớp | M05 | Todo | Chặn bởi M05-T2 |
| M06-T1 | Phân cụm (KMeans, chọn K) | M06 | Todo | Chặn bởi M04-T1 |
| M06-T2 | ARI (so cluster với `status`) | M06 | Todo | Chặn bởi M06-T1 |
| M06-T3 | Tổng hợp kết quả (chủ M06, gate M01) | M06 | Todo | Chặn bởi M05-T3, M06-T2 |
| S-T1 | Toàn nhóm xác nhận canonical CSV | All | Todo | Chặn bởi M01-T2 |
| S-T2 | Nhất quán trước báo cáo | M01 + M06 | Todo | Chặn bởi M05-T3, M06-T3 |

## Trạng thái tổng hợp (snapshot)

> Cập nhật mỗi lần có chuyển trạng thái. Hiện tại: **2 / 21** hoàn thành (+1 In Progress).

- **Todo:** 18
- **In Progress:** 1 (M01-T3)
- **Review:** 0
- **Blocked:** 0
- **Done:** 2 (M01-T1, M01-T2)

## Định danh "chặn bởi"

- Mã trong cột *Chặn bởi* là **nhiệm vụ phải ở `Done`** trước khi hạng mục này chạy được
  (hoặc ít nhất đầu ra của nó đã sẵn sàng). Nếu một nhiệm vụ chặn là `Blocked`/`Todo`,
  hạng mục hiện tại cũng phải đứng ở `Todo` hoặc `Blocked`.
- Khi có hạng mục `Blocked`: ghi rõ **thiếu gì** và **ai** cần cung cấp (vd:
  "M04-T1 Blocked — chờ M03-T2 (báo cáo chất lượng)").

## Ghi chú an toàn

- Bảng này **chỉ mô tả trạng thái làm việc**, không phản ánh tiến độ thật nếu chưa có
  bằng chứng. Không tự đánh `Done`. Không ghi tên/MSSV (chỉ dùng mã M01–M06).
