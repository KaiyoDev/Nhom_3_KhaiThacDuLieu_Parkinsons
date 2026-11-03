# M02 — Báo cáo khám phá cấu trúc dữ liệu

## Đầu vào và cách chạy

- Đầu vào duy nhất: `data/processed/parkinsons_v1.csv` (canonical v1).
- Notebook: `notebooks/01_data_exploration.ipynb`.
- Kiểm tra candidate outlier: quy tắc IQR, ngưỡng `Q1 - 1.5*IQR` và `Q3 + 1.5*IQR`.
- Không tự động xoá hoặc thay thế candidate outlier.

## M02-T1 — Cấu trúc và kiểu dữ liệu

| Kiểm tra | Kết quả |
|---|---:|
| Số dòng | 195 |
| Số cột | 23 |
| Số feature | 22 |
| Cột nhãn | `status` |
| Cột `name` | Không tồn tại trong canonical |
| Feature kiểu số | 22/22 |
| `status` | Số nguyên, chỉ có `0` và `1` |
| Tổng missing | 0 |
| Hàng trùng toàn bộ | 0 |
| Phân bố nhãn | `0`: 48, `1`: 147 |

## M02-T2 — Bản đồ nhóm đặc trưng

| Nhóm | Số cột | Cột |
|---|---:|---|
| FREQ | 3 | `MDVP:Fo(Hz)`, `MDVP:Fhi(Hz)`, `MDVP:Flo(Hz)` |
| JITTER | 5 | `MDVP:Jitter(%)`, `MDVP:Jitter(Abs)`, `MDVP:RAP`, `MDVP:PPQ`, `Jitter:DDP` |
| SHIMMER | 6 | `MDVP:Shimmer`, `MDVP:Shimmer(dB)`, `Shimmer:APQ3`, `Shimmer:APQ5`, `MDVP:APQ`, `Shimmer:DDA` |
| NOISE | 2 | `NHR`, `HNR` |
| NONLIN | 6 | `RPDE`, `DFA`, `spread1`, `spread2`, `D2`, `PPE` |

## M02-T3 — Vấn đề cần bàn giao

### Chênh lệch scale

Các khoảng quan sát cho thấy FREQ có range hàng trăm, trong khi JITTER có giá trị
rất nhỏ (ví dụ `MDVP:Jitter(Abs)` từ `0.000007` đến `0.00026`). SHIMMER, NOISE và
NONLIN cũng có range khác nhau. M04 cần dùng chuẩn hoá trước PCA và các mô hình nhạy
với scale.

### Candidate outlier theo IQR

| Feature | Số điểm bị đánh dấu |
|---|---:|
| `NHR` | 20 |
| `MDVP:PPQ` | 15 |
| `MDVP:Jitter(%)` | 14 |
| `MDVP:RAP` | 14 |
| `Jitter:DDP` | 14 |
| `Shimmer:APQ5` | 13 |
| `MDVP:APQ` | 12 |
| `MDVP:Fhi(Hz)` | 11 |
| `MDVP:Shimmer(dB)` | 10 |
| `MDVP:Flo(Hz)` | 9 |
| `MDVP:Shimmer` | 8 |
| `MDVP:Jitter(Abs)` | 7 |
| `Shimmer:APQ3` | 6 |
| `Shimmer:DDA` | 6 |
| `PPE` | 5 |
| `spread1` | 4 |
| `HNR` | 3 |
| `spread2` | 2 |
| `D2` | 1 |

Đây là các ứng viên để M03/M04 xem xét, không phải kết luận dữ liệu sai. Không có
missing hoặc trùng toàn hàng cần xử lý ở bước này.

## Bàn giao

- **M03:** cấu trúc đã xác nhận; lưu ý nhãn lệch `48/147` và danh sách candidate outlier.
- **M04:** chuẩn hoá là cần thiết do khác biệt scale; không xoá outlier tự động khi
  chưa có quy ước xử lý được thống nhất.
