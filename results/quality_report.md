# Báo cáo chất lượng dữ liệu Parkinson

## 1. Nguồn dữ liệu
- File: `data/processed/parkinsons_v1.csv`
- Số dòng: 195
- Số cột: 23
- Cột nhãn: `status`
- Số feature: 22

## 2. Phân bố nhãn

| Nhãn | Số mẫu | Tỷ lệ |
|---|---:|---:|
| 0 - Khỏe | 48 | 24.62% |
| 1 - Parkinson | 147 | 75.38% |

Nhận xét: Dữ liệu mất cân bằng giữa hai lớp. Cần lưu ý khi chia tập train/test và đánh giá mô hình.

## 3. Kiểm tra chất lượng dữ liệu

| Hạng mục | Kết quả |
|---|---:|
| Tổng giá trị thiếu (NaN) | 0 |
| Số dòng trùng lặp | 0 |
| Tổng số mẫu | 195 |
| Tổng số cột | 23 |

Nhận xét: Chưa phát hiện dữ liệu thiếu hoặc dòng trùng lặp trong lần kiểm tra này.

## 4. Kiểm tra thang đo feature

Các feature có thang đo khác nhau đáng kể. Ví dụ, các thuộc tính MDVP:Fo(Hz), MDVP:Fhi(Hz), MDVP:Flo(Hz) có giá trị ở mức hàng trăm, trong khi MDVP:Jitter(Abs) có giá trị rất nhỏ.

Nhận xét: Cần xem xét chuẩn hóa các feature trước khi thực hiện PCA và huấn luyện mô hình.

## 5. Kết luận và đề xuất

- Dữ liệu có 195 mẫu và 22 feature.
- Nhãn `status` có sự mất cân bằng giữa hai lớp.
- Không phát hiện giá trị thiếu hoặc dòng trùng lặp.
- Cần xem xét chuẩn hóa feature và phương pháp xử lý mất cân bằng khi xây dựng mô hình.
- Bàn giao các lưu ý về chất lượng dữ liệu cho M04 để xử lý ở bước tiền xử lý.