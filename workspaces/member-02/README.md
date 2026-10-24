# M02 — Khám phá cấu trúc & Kiểu dữ liệu (Work-order)

## 1. Thông tin
| | |
|---|---|
| Mã | `M02` |
| Tên / MSSV | `[CHƯA CẬP NHẬT]` |
| Vai trò | Khám phá cấu trúc & dtype, bản đồ nhóm đặc trưng, phát hiện vấn đề |
| Trạng thái | `Todo` |

## 2. Bạn làm ở đâu
- **Notebook:** `notebooks/01_data_exploration.ipynb`.
- **Các phần bạn phụ trách (theo "Bước" trong notebook):**
  - `Bước 1` Kiểm tra nguồn dữ liệu · `Bước 2` Kích thước · `Bước 3` Tên cột & dtype ·
    `Bước 4` Xác định thuộc tính & cột nhãn (chạy guard + assert tên cột).
  - `Bước 7` (phần **vấn đề**: scale / candidate outlier) — dùng chung với M03, nhưng **M02
    viết phần "cấu trúc/dtype/vấn đề"**, M03 viết phần "thống kê/chất lượng".

> M02 và M03 cùng notebook 01 → **chia bước rõ ở §4** để không ghi đè nhau.

## 3. Nhiệm vụ giao (theo `TASK_ASSIGNMENTS.md`)
| Mã | Việc | Nơi làm | Đầu vào | Đầu ra | Tiêu chí | Reviewer | Chặn bởi |
|----|------|---------|---------|--------|----------|----------|----------|
| M02-T1 | Khám phá cấu trúc & dtype | nb01 Bước 1–4 | canonical CSV (M01-T2) | bảng dòng/cột/dtype/thiếu/trùng/khoảng | đủ 22 feature + `status`, chỉ mô tả ĐÃ KIỂM TRA | M03 | M01-T2 (S-T1) |
| M02-T2 | Bản đồ nhóm đặc trưng | nb01 Bước 4 + `DATA_DICTIONARY.md` | M02-T1 | cập nhật nhóm (FREQ/JITTER/SHIMMER/NOISE/NONLIN) + nguồn | phân nhóm đúng, ghi nguồn | M03 | M02-T1 |
| M02-T3 | Phát hiện vấn đề | nb01 Bước 7 (vấn đề) | M02-T1 | danh sách scale/outlier → bàn M03, M04 | vấn đề rõ, đủ để xử lý | M04 | M02-T1 |

## 4. Thứ tự thực hiện (cụ thể, trong `notebooks/01_data_exploration.ipynb`)
0. **Chạy guard cell** (cell đầu tiên có `# if not os.path.exists(CSV)`): nếu **BLOCKED** (chưa
   có `data/processed/parkinsons_v1.csv`) → **DỪNG**, đánh dấu `Blocked` trong `TASK_BOARD.md`
   (chờ M01-T2 / S-T1), **KHÔNG** tự tạo CSV. Nếu đủ → tiếp tục.
1. **Bước 1–2:** đọc canonical CSV, `df.shape`, `list(df.columns)`, `df.dtypes()`. Ghi nhận
   số dòng/cột thực tế (đối chiếu ~195 dòng, 23 cột).
2. **Bước 3:** xác nhận các feature là số; cột `status` là 0/1. Ghi dtype vào
   `DATA_DICTIONARY.md` (cột "Kiểu / Thiếu" — mục M02-T1 được giao).
3. **Bước 4:** chạy 2 dòng `assert` (không còn `name`, có `status`, đủ 22 feature). Đối chiếu
   nhóm đặc trưng với `DATA_DICTIONARY.md` (M02-T2) — chỉ cập nhật nếu lệch, **ghi nguồn**.
4. **Bước 7 (phần của M02):** xem `df.describe()` / percentiles, liệt kê **vấn đề cấu trúc**:
   nhóm feature nào scale quá khác nhau (vd `MDVP:Jitter(Abs)` rất nhỏ), candidate outlier.
   → ghi thành danh sách, **bàn giao M03 + M04**.
5. Ghi kết quả vào **bảng "Kết quả & nhận xét"** trong notebook (phần của bạn) + `results/` (local).

> **Phân chia bước 5, 6 cho M03** (số mẫu theo nhãn, min/max/mean). Bạn **không** chạy các
> bước đó để tránh trùng (M03 chịu trách nhiệm). Bước 7 là **chia đôi**: M02 viết phần
> "vấn đề cấu trúc/scale/outlier", M03 viết phần "thiếu/trùng/bất thường + chất lượng".

## 5. Đầu vào cần nhận
- Canonical CSV (M01-T2, qua **S-T1**) + `DATA_DICTIONARY.md`. Không CSV riêng.

## 6. Đầu ra phải bàn giao
- Bảng khám phá cấu trúc (trong notebook + `results/`).
- Cập nhật `DATA_DICTIONARY.md` (cột Kiểu/Thiếu/Ghi chú cho M02-T1/T2) — **chỉ mô tả đã kiểm tra**.
- Danh sách vấn đề (scale/outlier) → bàn **M03 (chất lượng)** và **M04 (tiền xử lý)**.

## 7. Tiêu chí nghiệm thu (đo được)
- `DATA_DICTIONARY.md` đã điền cột "Kiểu / Thiếu" cho **mọi** feature (từ kết quả thật).
- Nhóm đặc trưng (FREQ/JITTER/SHIMMER/NOISE/NONLIN) đủ + có nguồn.
- Danh sách vấn đề nêu rõ ít nhất: **nhanh/tông scale** nào cần chuẩn hoá, candidate outlier nào.

## 8. Checklist tự kiểm
- [ ] Đã chạy guard (không Block) trước khi làm.
- [ ] Đã kiểm tra `df.shape`, `df.dtypes`, assert tên cột (khỏi bịa).
- [ ] `DATA_DICTIONARY.md` cột Kiểu/Thiếu + nhóm đặc trưng **cập nhật** (chỉ ghi đã kiểm tra).
- [ ] Danh sách vấn đề (scale/outlier) đã gửi M03 + M04.
- [ ] Kết quả ghi trong `results/`; không bịa số; không chạy Bước 5/6 của M03.
- [ ] Đã chuyển M02-T1..T3 sang `Review` trong `TASK_BOARD.md` + thông báo reviewer (M03, M04).

## 9. Người review
M02-T1 → **M03** · M02-T2 → **M03** · M02-T3 → **M04**.

## 10. Bàn giao & Blocked
- Theo `HANDOFF.md` (mô tả 5 dòng + test-report: `df.shape`, dtype, danh sách vấn đề).
- **Blocked nếu:** canonical CSV (S-T1) chưa có → ghi "chờ M01-T2 (S-T1)", thông báo M01.

## 11. Trạng thái
`Todo` — chờ **S-T1** (M01-T2 xong + nhóm xác nhận) trước khi chuyển `In Progress`.
