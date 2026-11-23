# TASK_BOARD — Bảng trạng thái công việc (Nhóm 3 · Parkinson)

> **5 trạng thái:** `Todo` · `In Progress` · `Review` · `Blocked` · `Done`.
> Ban đầu **mọi nhiệm vụ ở `Todo`**. Không giả lập tiến độ: chỉ chuyển trạng thái
> khi có bằng chứng (đã làm xong / đã review / đang bị chặn).
>
> **Cập nhật:** 2026-11-23 · **Deadline bài tập: 20/11/2026 (đã qua)** · **Đã hoàn thành 21 / 21 nhiệm vụ**.
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
| M01-T2 | Sản xuất canonical processed CSV | M01 | **Done** | v1 đã tạo + commit (`data/processed/`); đã dùng chung thực tế |
| M01-T3 | Gate đầu vào cho M02/M03/M04 | M01 | **Done** | GATE #1 (S-T1) đã chốt; canonical v1 làm đầu vào chung |
| M01-T4 | Kiểm tra nhất quán dữ liệu & kết quả (gate) | M01 | **Done** | GATE #2 (S-T2) đã ký: cùng canonical v1, cùng metric/quy ước |
| M02-T1 | Khám phá cấu trúc & dtype | M02 | **Done** | PR #5 đạt review 19/11; notebook có output |
| M02-T2 | Bản đồ nhóm đặc trưng | M02 | **Done** | Đã cập nhật `DATA_DICTIONARY.md` 5 nhóm; PR #5 |
| M02-T3 | Phát hiện vấn đề (scale / outlier) | M02 | **Done** | Đã ghi scale/outlier IQR (`NHR=19`); PR #5 |
| M03-T1 | Thống kê mô tả | M03 | **Done** | PR #13 đạt review: mean/median/std/min/max + skew/kurtosis cho 22 feature |
| M03-T2 | Kiểm tra chất lượng dữ liệu | M03 | **Done** | PR #13 đạt review: NaN/trùng = 0; IQR 19/22 feature, 47/195 mẫu; đề xuất xử lý |
| M03-T3 | Báo cáo chất lượng tổng hợp | M03 | **Done** | `results/quality_report.md` + `results/iqr_table.md` đạt review |
| M04-T1 | Tiền xử lý + feature matrix (22 cột) | M04 | **Done** | PR #7 merge 17/11; `Xs` 195×22, `StandardScaler` |
| M04-T2 | PCA (chọn số thành phần) | M04 | **Done** | PC1 58.9% / PC2 11.3%; 6 thành phần = 91.61% |
| M04-T3 | Trực quan hóa (hist/heatmap/scatter PC) | M04 | **Done** | 3 figure trong `results/figures/` |
| M05-T1 | Train/test + k-fold CV | M05 | **Done** | PR #8 đạt review 18/11; 10-fold stratified, seed 42 |
| M05-T2 | Phân lớp baseline + F-score | M05 | **Done** | KNN/SVM/RF; F-score tái lập khớp |
| M05-T3 | Báo cáo kết quả phân lớp | M05 | **Done** | `results/classification_report.md` + `results/m05_f1_cv.csv` |
| M06-T1 | Phân cụm (KMeans, chọn K) | M06 | **Done** | PR #14 đạt review: K=2..10, silhouette cực đại K=2; số tái lập khớp |
| M06-T2 | ARI (so cluster với `status`) | M06 | **Done** | PR #14 đạt review: ARI KMeans/DBSCAN khớp; grid DBSCAN kiểm tra chéo |
| M06-T3 | Tổng hợp kết quả (chủ M06, gate M01) | M06 | **Done** | `reports/summary.md` + notebook 05 đạt review; ký gate S-T2 |
| S-T1 | Toàn nhóm xác nhận canonical CSV | All | **Done** | canonical v1 (`parkinsons_v1.csv`) duy nhất, đã dùng xuyên suốt |
| S-T2 | Nhất quán trước báo cáo | M01 + M06 | **Done** | Cùng canonical v1/metric/quy ước; summary khớp toàn bộ `results/` |

## Trạng thái tổng hợp (snapshot)

> Cập nhật 2026-11-23. **Đã hoàn thành 21 / 21** nhiệm vụ; GATE #1 (S-T1) và GATE #2 (S-T2) đã ký.
> **Deadline 20/11/2026 đã qua**; mọi sản phẩm đã merge trên `main`.

- **Todo:** 0
- **In Progress:** 0
- **Review:** 0
- **Blocked:** 0
- **Done:** 21 (M01-T1..T4, M02-T1..T3, M03-T1..T3, M04-T1..T3, M05-T1..T3, M06-T1..T3, S-T1, S-T2)

## Trạng thái từng thành viên (deadline 20/11/2026)

| Mã | Thành viên | Trạng thái | Bằng chứng / ghi chú |
|----|-----------|:----------:|----------------------|
| M01 | Đặng Hoàng Ân | ✅ Hoàn thành | T1–T4 xong; đã ký GATE #1 (S-T1) và GATE #2 (S-T2) |
| M02 | Lê Thiên Lộc | ✅ Hoàn thành | PR #5 đạt review & merge |
| M03 | Huỳnh Gia Hợp | ✅ Hoàn thành | PR #13 đạt review (thống kê/chất lượng/IQR) |
| M04 | Trần Hoàng Thông | ✅ Hoàn thành | PR #7 đã merge (17/11) |
| M05 | Ngô Thị Anh Thư | ✅ Hoàn thành | PR #8 đạt review & merge |
| M06 | Nguyễn Hoàng Bách | ✅ Hoàn thành | PR #14 + `reports/summary.md` + notebook 05 đạt review |

> Mọi task được đánh `Done` sau khi đạt review độc lập tại PR (lead/owner), số liệu tái lập khớp
> trên canonical v1 + seed 42.

## Định danh "chặn bởi"

- Mã trong cột *Chặn bởi* là **nhiệm vụ phải ở `Done`** trước khi hạng mục này chạy được
  (hoặc ít nhất đầu ra của nó đã sẵn sàng). Nếu một nhiệm vụ chặn là `Blocked`/`Todo`,
  hạng mục hiện tại cũng phải đứng ở `Todo` hoặc `Blocked`.
- Khi có hạng mục `Blocked`: ghi rõ **thiếu gì** và **ai** cần cung cấp (vd:
  "M04-T1 Blocked — chờ M03-T2 (báo cáo chất lượng)").

## Ghi chú an toàn

- Bảng này **chỉ mô tả trạng thái làm việc**, không phản ánh tiến độ thật nếu chưa có
  bằng chứng. Không tự đánh `Done`. Không ghi tên/MSSV (chỉ dùng mã M01–M06).
