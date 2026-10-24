# data/ — Quy ước dữ liệu (Nhóm 3 · Parkinson)

> Mối quan tâm cốt lõi: **một đầu vào dữ liệu duy nhất** cho toàn nhóm → tránh
> "mỗi người một bản CSV". Mọi phân tích (G3–G6 trong `PROJECT_WORKFLOW.md`)
> phải tham chiếu canonical CSV, không phải bản do từng người tự sinh.

## 1. Thư mục

| Thư mục | Chứa gì | Commit Git? |
|---------|---------|:-----------:|
| `data/raw/` | Dataset gốc (xlsx) + manifest | **Không** (gitignored, chỉ giữ `.gitkeep`) |
| `data/interim/` | Dữ liệu trung gian (chưa xử lý xong) | Không |
| `data/processed/` | Canonical CSV + schema (artifact chung) | Mặc định **Không**; có thể `git add -f` nếu nhóm thống nhất chia sẻ |

> `data/README.md` + `.gitkeep` trong `raw/` `interim/` `processed/` là những file
> duy nhất được commit (khung thư mục). Nội dung thật không commit.

## 2. Canonical processed CSV (quy ước bắt buộc)

- **Tên file duy nhất:** `data/processed/parkinsons_v1.csv` (bản kế tiếp là `_v2`, ...
  không bao giờ thay tên bản đã dùng — tạo bản mới và ghi rõ trong schema).
- **Cột (theo `DATA_DICTIONARY.md`):** giữ **22 feature + `status`**; **loại `name`**.
- **Kiểu / trị thiếu:** ghi trong `data/processed/schema_v1.md` (manifest: tên cột, dtype,
  phương pháp xử lý NaN, số dòng/cột sau khi lọc).
- **Nguồn tạo:** chỉ M01 (M01-T2) được sinh canonical CSV; M01 chỉ **không sửa nội dung
  `data/raw/`** (raw giữ nguyên). Các member **không** tự tạo bản CSV riêng.

## 3. Cách nạp dữ liệu (dùng ở giai đoạn phân tích)

1. Đọc dataset gốc (chỉ `data/raw/`, không commit):
   - `pandas.read_excel("D07 - parkinsons.data.xlsx", sheet_name="parkinsons.data")`
     (cần `openpyxl`, xem `requirements.txt`).
2. Sau khi có canonical CSV (khuyến nghị dùng):
   - `pandas.read_csv("data/processed/parkinsons_v1.csv")`.
3. Mỗi bước (M02–M06) chỉ được nạp từ **canonical CSV** (hoặc nguồn gốc qua `data/raw/`
   nhưng phải đi theo cùng quy ước ở §2).

## 4. An toàn dữ liệu

- **Không đưa dataset gốc / xlsx / dữ liệu chưa được phép chia sẻ vào Git** (`.gitignore`
  đã phủ). Không `git add -f` file xlsx.
- **Không chứa bí mật** (token, mật khẩu, API key). File `.env`, `secrets*`, `*.key`,
  `*.pem` đã được ignore.
- **Không ghi tên / MSSV / dữ liệu cá nhân** (thành viên chưa cung cấp); dùng mã M01–M06.
- Cột `name` (tên chủ thể + số bản ghi) **loại bỏ** ở canonical CSV → không để lộ
  danh tính; nếu cần đối chiếu cá nhân về sau, giữ chỉ ở `data/raw/` (local).
- Không tự ý thay đổi quyền riêng tư repository.

## 5. Quy ước báo cáo "thay đổi dữ liệu"

Khi có thay đổi (thêm cột, đổi kiểu, xử lý NaN khác), người chịu trách nhiệm **phải**:
- Ghi vào `data/processed/schema_v1.md` (changelog: ngày, ai, thay gì, vì sao, ảnh hưởng).
- Cập nhật `TASK_BOARD.md` (nhiệm vụ có thể bị chặn / cần review lại).
- Thông báo nhóm qua M01 (điều phối) trước khi các bước khác dùng lại.
