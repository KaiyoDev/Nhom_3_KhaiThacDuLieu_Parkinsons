# M01 — Điều phối + Chuẩn bị dữ liệu + Thống nhất đầu vào

| Hạng mục | Giá trị |
|----------|---------|
| Mã thành viên | `M01` |
| Tên | `[CHƯA CẬP NHẬT]` |
| MSSV | `[CHƯA CẬP NHẬT]` |
| Vai trò dự kiến | Điều phối · chuẩn bị dữ liệu · thống nhất đầu vào |
| Trạng thái ban đầu | `Todo` |

## Nhiệm vụ được giao (xem `TASK_ASSIGNMENTS.md`)

| Mã | Nhiệm vụ | Tóm tắt |
|----|----------|---------|
| M01-T1 | Chuẩn bị dữ liệu thô | Copy dataset gốc → `data/raw/` + `manifest.md` (hash, kích thước) |
| M01-T2 | Canonical processed CSV | Sinh `data/processed/parkinsons_v1.csv` (drop `name`, giữ 22 feature + `status`) + `schema_v1.md` |
| M01-T3 | Gate đầu vào | Xác nhận đầu vào sẵn sàng cho M02/M03/M04 |
| M01-T4 | Kiểm tra nhất quán (gate) | Gate tính nhất quán dữ liệu & kết quả giữa các phần (kèm M06-T3/S-T2) |

## Đầu vào cần nhận

- Dataset gốc: `D07 - parkinsons.data.xlsx` (ở root repo, **không đưa vào Git**).
- Quy ước cột: `DATA_DICTIONARY.md` (22 feature + nhãn `status`, loại `name`).

## Đầu ra cần bàn giao

- `data/raw/manifest.md` (M01-T1).
- `data/processed/parkinsons_v1.csv` + `data/processed/schema_v1.md` (M01-T2) — **đầu vào chung** toàn nhóm.
- Cập nhật `TASK_BOARD.md` tại M01-T3 (gate mở) và M01-T4 (gate đóng).
- Ký nhận nhất quán tại `S-T2` (cùng M06).

## Tiêu chí hoàn thành

- Canonical CSV **duy nhất** — mọi bước khác tham chiếu file này, không bản riêng.
- `schema_v1.md` ghi rõ: danh sách cột, dtype, số dòng/cột, cách xử lý NaN/loại cột.
- Không commit/xoá/sửa file xlsx gốc; hash trong manifest khớp với file thực.
- Gate nhất quán (M01-T4) được ký trước khi hoàn thiện `reports/`.

## Checklist tự kiểm tra

- [ ] Đã copy dataset gốc vào `data/raw/`, ghi manifest (hash + kích thước + ngày + nguồn).
- [ ] `data/processed/parkinsons_v1.csv`: đúng 22 feature + `status`, đã drop `name`.
- [ ] `schema_v1.md` đầy đủ (cột, dtype, số dòng/cột, xử lý NaN/loại).
- [ ] Đã thông báo S-T1 (toàn nhóm xác nhận canonical CSV) trước khi M02/M03/M04 chạy.
- [ ] Đã cập nhật `TASK_BOARD.md` tại gate M01-T3 và M01-T4.
- [ ] Không có file xlsx / dữ liệu cá nhân / bí mật được commit.
- [ ] Kết quả giữa các phần đã được kiểm tra nhất quán (cùng CSV, cùng metric, cùng quy ước).

## Người review dự kiến

- M01-T1: **M06** (kiểm tra hash/kích thước).
- M01-T2: **S-T1 (toàn nhóm) + M03** (chất lượng dữ liệu).
- M01-T3: **M03**.
- M01-T4: **M06** (chủ trì tổng hợp).

## Trạng thái ban đầu

`Todo` — mọi nhiệm vụ của M01 chưa bắt đầu.
