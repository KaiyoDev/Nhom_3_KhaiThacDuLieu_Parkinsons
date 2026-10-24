# tests/ — Kiểm thử (tạo ở giai đoạn sau)

> **Hiện tại: TRỐNG (chưa viết test ở giai đoạn setup).**
> Nơi đặt kiểm thử (pytest) cho module trong `src/`.

## Định hướng (không triển khai ở giai đoạn này)

- Kiểm tra **schema canonical CSV**: đủ 22 feature + `status`, không có `name`.
- Kiểm tra **tính reproducible** của pipeline (cùng seed → cùng kết quả).
- Kiểm tra **chỉ báo metric** (F-score, ARI) trả về giá trị hợp lệ (0–1).

## Quy định (khi viết test)

- Mỗi test **độc lập**, không phụ thuộc thứ tự chạy.
- Test chỉ dùng dữ liệu mẫu nhỏ / synthetic (không commit dataset thô).
- Chạy: `pytest` (cài theo `requirements.txt`).

## Ràng buộc setup

- **Không viết test cho code chưa tồn tại ở giai đoạn này.**
- Thư mục chỉ giữ README.
