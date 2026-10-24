# src/ — Mã nguồn tái sử dụng (tạo ở giai đoạn sau)

> **Hiện tại: TRỐNG (chưa viết code phân tích ở giai đoạn setup).**
> Đây là nơi đặt module Python **tái sử dụng được** cho pipeline (không phải
> notebook), để các thành viên dùng chung.

## Định hướng (không triển khai ở giai đoạn này)

- `src/data.py` — nạp canonical CSV, kiểm tra schema, drop `name`.
- `src/preprocessing.py` — chuẩn hoá, xử lý NaN (quy ước một chiều, dùng chung).
- `src/pca.py`, `src/classification.py`, `src/clustering.py` — đóng gói từng bước,
  trả về kết quả định dạng nhất quán (dict/DataFrame) để ghi vào `results/`.
- Mỗi module **test được** (xem `tests/`).

## Quy định (khi viết code)

- **Một canonical CSV duy nhất** — mọi module nạp từ `data/processed/parkinsons_v1.csv`,
  không có nhiều bản.
- Không hardcode secret; cấu hình (seed, k, ngưỡng) ghi trong `docs/REPRODUCIBILITY.md`.
- Không `console.log`/`print` debug bỏ lại; code sạch trước khi bàn giao.
- Kết quả thực nghiệm chỉ lưu trong `results/` (không commit dữ liệu thô).

## Ràng buộc setup

- **Không viết code phân tích / không tạo kết quả ở giai đoạn này.**
- Thư mục chỉ giữ README.
