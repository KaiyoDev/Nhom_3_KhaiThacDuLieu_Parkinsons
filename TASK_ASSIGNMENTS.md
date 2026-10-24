# TASK_ASSIGNMENTS — Phân rã nhiệm vụ (Nhóm 3 · Parkinson)

> Trạng thái setup: chỉ **phân rã** để 6 thành viên nhận việc độc lập.
> Chưa có code, chưa có kết quả. Mọi mục ban đầu ở `Todo` (xem `TASK_BOARD.md`).
>
> **Nguyên tắc:** mỗi người **chỉ làm phần được giao**; đầu vào phải được xác nhận trước
> khi bắt đầu; **không để M01 làm tất cả việc tích hợp một mình** — tổng hợp kết quả
> (M06-T3) do **M06 chủ trì, M01 chỉ gate nhất quán**.

## 0. Bảng tổng hợp mã nhiệm vụ

| Mã | Nội dung ngắn | Phụ trách | Đầu vào (phụ thuộc) | Người review |
|----|---------------|-----------|----------------------|--------------|
| M01-T1 | Chuẩn bị dữ liệu thô → `data/raw/` | M01 | dataset gốc (root) | M06 |
| M01-T2 | Sản xuất canonical processed CSV | M01 | M01-T1 | S-T1 + M03 |
| M01-T3 | Gate đầu vào cho M02/M03/M04 | M01 | M01-T2 | M03 |
| M01-T4 | Kiểm tra nhất quán dữ liệu & kết quả (gate) | M01 | M05-T3, M06-T2 | M06 |
| M02-T1 | Khám phá cấu trúc & dtype | M02 | M01-T2 | M03 |
| M02-T2 | Bản đồ nhóm đặc trưng (bổ sung DATA_DICTIONARY) | M02 | M02-T1 | M03 |
| M02-T3 | Phát hiện vấn đề (scale / candidate outlier) | M02 | M02-T1 | M04 |
| M03-T1 | Thống kê mô tả | M03 | M01-T2 | M02 |
| M03-T2 | Kiểm tra chất lượng dữ liệu | M03 | M02-T3 | M04 |
| M03-T3 | Báo cáo chất lượng tổng hợp | M03 | M03-T1, M03-T2 | M01 (gate) |
| M04-T1 | Tiền xử lý + feature matrix (22 cột) | M04 | M03-T2 | M05 |
| M04-T2 | PCA (chọn số thành phần) | M04 | M04-T1 | M06 |
| M04-T3 | Trực quan hóa (histogram/heatmap/scatter PC) | M04 | M04-T2 | M01 |
| M05-T1 | Train/test + k-fold CV (quy ước seed, k) | M05 | M04-T1 | M01 |
| M05-T2 | Mô hình phân lớp baseline + F-score | M05 | M05-T1 | M01 (gate) + M06 |
| M05-T3 | Báo cáo kết quả phân lớp | M05 | M05-T2 | M06 |
| M06-T1 | Phân cụm (KMeans, chọn K) | M06 | M04-T1 | M05 |
| M06-T2 | ARI (so cluster với `status`) | M06 | M06-T1 | M01 (gate) |
| M06-T3 | **Tổng hợp kết quả** (chủ trì M06, gate M01) | M06 (+M01) | M05-T3, M06-T2 | M01 |
| S-T1 | Toàn nhóm xác nhận canonical CSV | All | M01-T2 | M03 + M05 |
| S-T2 | Nhất quán cuối trước báo cáo | M01 + M06 | M05-T3, M06-T3 | M01 |

> Mã `Mxx-Tn`: thuộc về member đó. Mã `S-Tn`: nhiệm vụ chung (shared).
> Cột "Người review" = người **xác nhận đầu ra** (reviewer), khác với phụ trách.

## 1. Chi tiết từng nhiệm vụ

> Mẫu chi tiết: **Đầu vào · Đầu ra · Tiêu chí nghiệm thu · Phụ thuộc · Review · Ghi chú phối hợp.**

### M01 — Điều phối + dữ liệu

**M01-T1 · Chuẩn bị dữ liệu thô**
- Đầu vào: file gốc `D07 - parkinsons.data.xlsx` (nằm ở root, **không đưa vào Git**).
- Đầu ra: copy vào `data/raw/` (local, gitignored) + `data/raw/manifest.md`
  (tên file, kích thước, hash SHA-256, nguồn, ngày sao chép).
- Tiêu chí: manifest đúng thực tế; không sửa dữ liệu gốc; không commit file xlsx.
- Phụ thuộc: — (dataset đã có sẵn).
- Review: M06 (kiểm tra hash/kích thước khớp).
- Phối hợp: chỉ M01 chạm `data/raw/`; các member khác **không** tạo bản CSV riêng.

**M01-T2 · Sản xuất canonical processed CSV**
- Đầu vào: `data/raw/*` (M01-T1) + quy ước trong `DATA_DICTIONARY.md`.
- Đầu ra: `data/processed/parkinsons_v1.csv` (drop cột `name`, giữ 22 feature + `status`,
  chuẩn hoá dtype) + `data/processed/schema_v1.md` (manifest: cột, kiểu, missing, cách xử lý).
- Tiêu chí: **1 file CSV duy nhất** làm đầu vào chung; schema ghi rõ cách xử lý NaN/loại cột;
  file nằm ở `data/processed/` (mặc định local, không commit — xem `data/README.md`).
- Phụ thuộc: M01-T1.
- Review: **S-T1** (toàn nhóm xác nhận) + M03 (chất lượng).
- Phối hợp: đây là "nguồn dữ liệu xử lý duy nhất" → tránh nhiều bản CSV khác nhau.

**M01-T3 · Gate đầu vào**
- Xác nhận canonical CSV + schema sẵn sàng, thông báo M02/M03/M04 được nhận việc.
- Đầu ra: cập nhật `TASK_BOARD.md` (đánh dấu sẵn sàng) + thông báo nhóm.
- Tiêu chí: reviewer M03 xác nhận đủ điều kiện làm.

**M01-T4 · Kiểm tra nhất quán (gate)**
- Đầu vào: kết quả M05-T3, M06-T2, M06-T3.
- Đầu ra: ký nhận nhất quán (cùng canonical CSV, cùng metric, cùng quy ước báo cáo).
- Tiêu chí: các phần dùng **cùng** đầu vào & quy ước; không mâu thuẫn.
- Phụ thuộc: M05-T3, M06-T2. **Không** thay cho tổng hợp (tổng hợp do M06-T3).

### M02 — Khám phá cấu trúc & dtype

**M02-T1** · Đầu vào: canonical CSV (M01-T2). · Đầu ra: bảng khám phá cấu trúc
(dòng/cột/dtype/thiếu/trùng/khoảng) + bổ sung cột "Kiểu" & "Thiếu" vào `DATA_DICTIONARY.md`.
· Tiêu chí: đủ 22 feature + `status`, có chỉ báo NaN/trùng; chỉ mô tả **đã kiểm tra**.
· Phụ thuộc: M01-T2. · Review: M03.

**M02-T2 · Bản đồ nhóm đặc trưng**
- Nhóm: *frequency (Fo/Fhi/Flo)*, *jitter (5)*, *shimmer (6)*, *noise (NHR, HNR)*,
  *nonlinear (RPDE, DFA, spread1, spread2, D2, PPE)*.
- Đầu ra: cập nhật `DATA_DICTIONARY.md` (phân nhóm + nguồn trích từ sheet mô tả).
- Phụ thuộc: M02-T1. · Review: M03.

**M02-T3 · Phát hiện vấn đề**
- Đầu ra: danh sách vấn đề (chênh lệch scale giữa các nhóm feature, candidate outlier).
- Bàn giao: M03 (chất lượng) + M04 (tiền xử lý). · Phụ thuộc: M02-T1. · Review: M04.

### M03 — Thống kê mô tả + chất lượng

**M03-T1 · Thống kê mô tả**
- Đầu vào: canonical CSV. · Đầu ra: bảng thống kê (mean/median/std/min/max, skew, kurtosis)
  theo từng feature → ghi trong `results/` (local). · Tiêu chí: chỉ số đúng thực tế, có phân bố.
- Phụ thuộc: M01-T2. · Review: M02.

**M03-T2 · Kiểm tra chất lượng**
- Đầu vào: danh sách vấn đề (M02-T3). · Đầu ra: kết quả kiểm tra cân bằng label (0 vs 1),
  trùng lặp, khoảng bất thường, thiếu → đề xuất phương pháp xử lý cho M04.
- Tiêu chí: có kết luận rõ "sẵn sàng / cần xử lý gì". · Phụ thuộc: M02-T3. · Review: M04.

**M03-T3 · Báo cáo chất lượng tổng hợp**
- Đầu ra: `results/quality_report.md`. · Tiêu chí: phản ánh thực tế dữ liệu, có đề xuất.
- Phụ thuộc: M03-T1, M03-T2. · Review: M01 (gate).

### M04 — Tiền xử lý + PCA + trực quan

**M04-T1 · Tiền xử lý + feature matrix**
- Đầu vào: canonical CSV + đề xuất xử lý (M03-T2). · Đầu ra: pipeline reproducible +
  feature matrix 22 cột (code để trong `src/`/notebook, dữ liệu local).
- Tiêu chí: code chạy lại được kết quả giống; quy ước chuẩn hoá (vd StandardScaler) được ghi.
- Phụ thuộc: M03-T2. · Review: M05 (đủ dùng cho model).

**M04-T2 · PCA**
- Đầu ra: kết quả PCA (số thành phần theo ngưỡng variance) + figure → `results/`.
- Tiêu chí: nêu rõ ngưỡng chọn & số thành phần giữ lại. · Phụ thuộc: M04-T1. · Review: M06.

**M04-T3 · Trực quan hóa**
- Đầu ra: histogram (phân bố), heatmap tương quan, scatter PC1–PC2 vs `status` → `results/`.
- Tiêu chí: figure gắn với số liệu thật, chú thích đủ. · Phụ thuộc: M04-T2. · Review: M01.

### M05 — Phân lớp + CV + F-score

**M05-T1 · Train/test + k-fold CV**
- Đầu vào: feature matrix (M04-T1). · Đầu ra: quy ước split + k-fold (seed, k) viết trong
  `docs/REPRODUCIBILITY.md`. · Tiêu chí: quy ước lặp lại được, ghi rõ seed/k.
- Phụ thuộc: M04-T1. · Review: M01.

**M05-T2 · Phân lớp baseline + F-score**
- Đầu ra: kết quả F-score (macro/weighted) theo ≥2 mô hình (vd kNN/LogReg/SVM) → bảng trong
  `results/`. · Tiêu chí: có CV, chỉ báo F-score (không phải "chạy thử" đơn lẻ).
- Phụ thuộc: M05-T1. · Review: M01 (gate) + M06.

**M05-T3 · Báo cáo kết quả phân lớp**
- Đầu ra: `results/classification_report.md`. · Tiêu chí: so sánh được giữa các mô hình.
- Phụ thuộc: M05-T2. · Review: M06.

### M06 — Phân cụm + ARI + tổng hợp

**M06-T1 · Phân cụm**
- Đầu vào: feature matrix (M04-T1). · Đầu ra: kết quả KMeans (chọn K bằng silhouette/elbow)
  + figure → `results/`. · Tiêu chí: nêu rõ phương pháp chọn K. · Phụ thuộc: M04-T1.
- Review: M05.

**M06-T2 · ARI**
- Đầu ra: Adjusted Rand Index so cluster với nhãn `status` → `results/`.
- Tiêu chí: có so sánh K khác nhau. · Phụ thuộc: M06-T1. · Review: M01 (gate).

**M06-T3 · Tổng hợp kết quả (chủ trì M06, M01 gate)**
- Đầu vào: báo cáo M05-T3 + M06-T2 (và các kết quả M02/M03/M04). · Đầu ra: `reports/summary.md`
  (bản thảo tổng hợp). · Tiêu chí: nhất quán chung (cùng đầu vào/metric/quy ước); **không phải
  M01 viết một mình** — M06 chủ trì, M01 ký nhận nhất quán (M01-T4).
- Phụ thuộc: M05-T3, M06-T2. · Review: M01.

## 2. Nhiệm vụ chung (shared)

**S-T1 · Xác nhận canonical CSV (toàn nhóm)**
- Sau M01-T2, **tất cả** member đọc `schema_v1.md` và xác nhận đủ dùng → mới bắt đầu phần mình.
- Review: M03 + M05. Đây là "rào cổng" để tránh đầu vào không thống nhất.

**S-T2 · Nhất quán trước báo cáo (M01 + M06)**
- Kiểm tra toàn bộ kết quả dùng cùng canonical CSV & quy ước → ký trước khi hoàn thiện `reports/`.

## 3. Lưu đồ phụ thuộc (text)

```text
[M01-T1 raw] → [M01-T2 canonical CSV] → (S-T1 xác nhận) ─┬→ [M02-T1..T3 khám phá]
                                                          ├→ [M03-T1..T3 thống kê/chất lượng]
                                                          └→ (M03-T2 đề xuất xử lý)
[M02-T3] → [M03-T2] → [M04-T1 tiền xử lý] ─┬→ [M04-T2 PCA] → [M04-T3 trực quan]
                                            ├→ [M05-T1 CV] → [M05-T2 F-score] → [M05-T3]
                                            └→ [M06-T1 cluster] → [M06-T2 ARI]
[M05-T3] + [M06-T2] → [M06-T3 tổng hợp (chủ M06)] + [M01-T4 gate] + [S-T2] → reports/
```

## 4. Quy ước phối hợp (tóm tắt)

1. Đọc nhiệm vụ & **xác nhận đầu vào** trước khi làm. 2. Chỉ làm phần được giao.
3. Thiếu dữ liệu / phụ thuộc chưa xong → đánh dấu `Blocked` trong `TASK_BOARD.md`.
4. Trước khi bàn giao: kiểm tra file + hoàn thành checklist trong workspace của mình.
5. Thành viên khác **review** đầu ra (theo cột "Người review"). 6. Chỉ đánh `Done` khi đạt
   tiêu chí nghiệm thu. 7. M01 kiểm tra **nhất quán** dữ liệu & kết quả giữa các phần.
8. **Một canonical CSV duy nhất** — không ai tự tạo bản CSV riêng (xem `data/README.md`).
