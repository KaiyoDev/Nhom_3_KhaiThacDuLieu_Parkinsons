# notebooks/ — Notebook phân tích (tạo ở giai đoạn sau)

> **Hiện tại: TRỐNG (chưa tạo `.ipynb` ở giai đoạn setup).**
> Đây là nơi 6 thành viên sẽ đặt notebook phân tích khi mở giai đoạn làm việc.

## Quy định (áp dụng khi tạo notebook)

- Mỗi notebook **tham chiếu canonical CSV** (`data/processed/parkinsons_v1.csv`),
  không dùng bản CSV riêng (xem `data/README.md`).
- Notebook của ai nằm cùng thư mục (vd `notebooks/m02_exploration.ipynb`),
  đặt tên theo `member-XX_đích.ipynb`.
- Kết quả (figure, bảng số) **bắt buộc** lưu kèm trong `results/` (định dạng máy đọc
  được: CSV/JSON + PNG), không chỉ "in ra màn hình".
- Quy ước chạy: seed + phiên bản thư viện ghi trong `docs/REPRODUCIBILITY.md`.
- Chạy trên Colab xem `docs/COLAB_GUIDE.md` (mỗi người một runtime, không tự đồng bộ
  với GitHub — cần commit notebook + upload dữ liệu riêng).

## Ràng buộc setup

- **Không tạo file `.ipynb` ở giai đoạn này.** Thư mục này chỉ giữ README.
- Không commit notebook chứa dữ liệu thô / kết quả bịa / bí mật.
