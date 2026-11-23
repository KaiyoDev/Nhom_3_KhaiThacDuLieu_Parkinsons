# Báo cáo chất lượng dữ liệu Parkinson

## Thông tin nhiệm vụ

| Hạng mục | Thông tin |
|---|---|
| Mã nhiệm vụ | M03-T1, M03-T2, M03-T3 |
| Người thực hiện | Huỳnh Gia Hợp (M03) |
| Ngày cập nhật báo cáo | 23/11/2026 |
| Nguồn dữ liệu | `data/processed/parkinsons_v1.csv` |
| Phiên bản dữ liệu | `v1` |
| Python | 3.11.15 |
| Random seed | Không sử dụng; các phép thống kê không có bước lấy mẫu ngẫu nhiên |

## 1. Nguồn dữ liệu

- File đầu vào: `data/processed/parkinsons_v1.csv`
- Số dòng: 195
- Số cột: 23
- Cột nhãn: `status`
- Số feature: 22
- Cột `name` đã được loại khỏi canonical dataset.

Dữ liệu được đọc từ canonical CSV của nhóm. Không tạo hoặc sử dụng một bản CSV riêng thay thế.

## 2. Phân bố nhãn

| Nhãn | Số mẫu | Tỷ lệ |
|---|---:|---:|
| 0 - Khỏe | 48 | 24,62% |
| 1 - Parkinson | 147 | 75,38% |

**Nhận xét:** Dữ liệu mất cân bằng giữa hai lớp. Khi chia train/test nên sử dụng phân tầng theo `status` (`stratify`) để duy trì tỷ lệ nhãn. Khi đánh giá mô hình cần xem xét Precision, Recall, F1-score và Confusion Matrix, không chỉ dựa vào Accuracy.

## 3. Kiểm tra dữ liệu thiếu và trùng lặp

| Hạng mục | Kết quả |
|---|---:|
| Tổng giá trị thiếu (NaN) | 0 |
| Số dòng trùng lặp | 0 |
| Tổng số mẫu | 195 |
| Tổng số cột | 23 |

**Nhận xét:** Trong lần kiểm tra hiện tại, chưa phát hiện giá trị thiếu hoặc dòng trùng lặp. Vì vậy chưa có yêu cầu điền giá trị thiếu hoặc loại bỏ dòng trùng tại bước M03.

## 4. Thống kê mô tả feature - M03-T1

Thực hiện thống kê trên 22 feature số, không đưa cột nhãn `status` vào thống kê.

Các chỉ số được tính:

- `mean`: Giá trị trung bình.
- `median`: Trung vị.
- `std`: Độ lệch chuẩn.
- `min`: Giá trị nhỏ nhất.
- `max`: Giá trị lớn nhất.
- `skew`: Độ lệch phân phối.
- `kurtosis`: Độ nhọn phân phối (excess kurtosis theo cách tính của pandas).
| Feature          |     mean |   median |     std |      min |      max |    skew |   kurtosis |
|:-----------------|---------:|---------:|--------:|---------:|---------:|--------:|-----------:|
| MDVP:Fo(Hz)      | 154.229  | 148.79   | 41.3901 |  88.333  | 260.105  |  0.5917 |    -0.6279 |
| MDVP:Fhi(Hz)     | 197.105  | 175.829  | 91.4915 | 102.145  | 592.03   |  2.5421 |     7.6272 |
| MDVP:Flo(Hz)     | 116.325  | 104.315  | 43.5214 |  65.476  | 239.17   |  1.2174 |     0.6546 |
| MDVP:Jitter(%)   |   0.0062 |   0.0049 |  0.0048 |   0.0017 |   0.0332 |  3.0849 |    12.0309 |
| MDVP:Jitter(Abs) |   0      |   0      |  0      |   0      |   0.0003 |  2.6491 |    10.869  |
| MDVP:RAP         |   0.0033 |   0.0025 |  0.003  |   0.0007 |   0.0214 |  3.3607 |    14.2138 |
| MDVP:PPQ         |   0.0034 |   0.0027 |  0.0028 |   0.0009 |   0.0196 |  3.0739 |    11.9639 |
| Jitter:DDP       |   0.0099 |   0.0075 |  0.0089 |   0.002  |   0.0643 |  3.3621 |    14.2248 |
| MDVP:Shimmer     |   0.0297 |   0.023  |  0.0189 |   0.0095 |   0.1191 |  1.6665 |     3.2383 |
| MDVP:Shimmer(dB) |   0.2823 |   0.221  |  0.1949 |   0.085  |   1.302  |  1.9994 |     5.1282 |
| Shimmer:APQ3     |   0.0157 |   0.0128 |  0.0102 |   0.0046 |   0.0565 |  1.5806 |     2.7202 |
| Shimmer:APQ5     |   0.0179 |   0.0135 |  0.012  |   0.0057 |   0.0794 |  1.7987 |     3.8742 |
| MDVP:APQ         |   0.0241 |   0.0183 |  0.0169 |   0.0072 |   0.1378 |  2.618  |    11.1633 |
| Shimmer:DDA      |   0.047  |   0.0384 |  0.0305 |   0.0136 |   0.1694 |  1.5806 |     2.7207 |
| NHR              |   0.0248 |   0.0117 |  0.0404 |   0.0006 |   0.3148 |  4.2207 |    21.995  |
| HNR              |  21.886  |  22.085  |  4.4258 |   8.441  |  33.047  | -0.5143 |     0.616  |
| RPDE             |   0.4985 |   0.496  |  0.1039 |   0.2566 |   0.6852 | -0.1434 |    -0.9218 |
| DFA              |   0.7181 |   0.7223 |  0.0553 |   0.5743 |   0.8253 | -0.0332 |    -0.6862 |
| spread1          |  -5.6844 |  -5.7209 |  1.0902 |  -7.965  |  -2.434  |  0.4321 |    -0.0502 |
| spread2          |   0.2265 |   0.2189 |  0.0834 |   0.0063 |   0.4505 |  0.1444 |    -0.083  |
| D2               |   2.3818 |   2.3615 |  0.3828 |   1.4233 |   3.6712 |  0.4304 |     0.2203 |
| PPE              |   0.2066 |   0.1941 |  0.0901 |   0.0445 |   0.5274 |  0.7975 |     0.5283 |

**Nhận xét:** Các feature có thang đo và phân phối khác nhau. Skewness và Kurtosis được sử dụng để hỗ trợ nhận diện đặc điểm phân phối, không phải tiêu chí duy nhất để kết luận dữ liệu sai hoặc cần loại bỏ.

## 5. Kiểm tra candidate outlier bằng IQR - M03-T2

### 5.1. Phương pháp

Sử dụng phương pháp Interquartile Range (IQR) cho từng feature số:

- `Q1`: Phân vị 25%.
- `Q3`: Phân vị 75%.
- `IQR = Q3 - Q1`.
- Ngưỡng dưới: `Q1 - 1.5 × IQR`.
- Ngưỡng trên: `Q3 + 1.5 × IQR`.

Một giá trị nhỏ hơn ngưỡng dưới hoặc lớn hơn ngưỡng trên được đánh dấu là candidate outlier.

### 5.2. Kết quả tổng hợp

| Hạng mục | Kết quả |
|---|---:|
| Tổng số feature được kiểm tra | 22 |
| Feature có candidate outlier | 19 |
| Feature không có candidate outlier | 3 |
| Tổng số mẫu | 195 |
| Số mẫu có ít nhất một candidate outlier | 47 |
| Tỷ lệ mẫu có candidate outlier | 24,10% |

Một số kết quả đáng chú ý:

| Feature | Số candidate outlier |
|---|---:|
| NHR | 19 |
| HNR | 3 |

**Bảng IQR chi tiết:**
| Feature          |       Q1 |       Q3 |     IQR |   Lower_bound |   Upper_bound |   Outlier_count |   Outlier_percent |
|:-----------------|---------:|---------:|--------:|--------------:|--------------:|----------------:|------------------:|
| MDVP:Fo(Hz)      | 117.572  | 182.769  | 65.197  |       19.7765 |      280.565  |               0 |            0      |
| MDVP:Fhi(Hz)     | 134.863  | 224.206  | 89.343  |        0.848  |      358.22   |              11 |            5.641  |
| MDVP:Flo(Hz)     |  84.291  | 140.018  | 55.7275 |        0.6997 |      223.61   |               9 |            4.6154 |
| MDVP:Jitter(%)   |   0.0035 |   0.0074 |  0.0039 |       -0.0024 |        0.0132 |              14 |            7.1795 |
| MDVP:Jitter(Abs) |   0      |   0.0001 |  0      |       -0      |        0.0001 |               7 |            3.5897 |
| MDVP:RAP         |   0.0017 |   0.0038 |  0.0022 |       -0.0016 |        0.0071 |              14 |            7.1795 |
| MDVP:PPQ         |   0.0019 |   0.004  |  0.0021 |       -0.0013 |        0.0071 |              15 |            7.6923 |
| Jitter:DDP       |   0.005  |   0.0115 |  0.0065 |       -0.0048 |        0.0213 |              14 |            7.1795 |
| MDVP:Shimmer     |   0.0165 |   0.0379 |  0.0214 |       -0.0156 |        0.07   |               8 |            4.1026 |
| MDVP:Shimmer(dB) |   0.1485 |   0.35   |  0.2015 |       -0.1538 |        0.6523 |              10 |            5.1282 |
| Shimmer:APQ3     |   0.0082 |   0.0203 |  0.012  |       -0.0098 |        0.0383 |               6 |            3.0769 |
| Shimmer:APQ5     |   0.0096 |   0.0224 |  0.0128 |       -0.0096 |        0.0416 |              13 |            6.6667 |
| MDVP:APQ         |   0.0131 |   0.0294 |  0.0163 |       -0.0114 |        0.0539 |              12 |            6.1538 |
| Shimmer:DDA      |   0.0247 |   0.0608 |  0.0361 |       -0.0294 |        0.1149 |               6 |            3.0769 |
| NHR              |   0.0059 |   0.0256 |  0.0197 |       -0.0236 |        0.0552 |              19 |            9.7436 |
| HNR              |  19.198  |  25.0755 |  5.8775 |       10.3818 |       33.8917 |               3 |            1.5385 |
| RPDE             |   0.4213 |   0.5876 |  0.1663 |        0.1719 |        0.8369 |               0 |            0      |
| DFA              |   0.6748 |   0.7619 |  0.0871 |        0.5441 |        0.8926 |               0 |            0      |
| spread1          |  -6.4501 |  -5.0462 |  1.4039 |       -8.556  |       -2.9403 |               4 |            2.0513 |
| spread2          |   0.1744 |   0.2792 |  0.1049 |        0.017  |        0.4366 |               2 |            1.0256 |
| D2               |   2.0991 |   2.6365 |  0.5373 |        1.2931 |        3.4425 |               1 |            0.5128 |
| PPE              |   0.1375 |   0.253  |  0.1155 |       -0.0358 |        0.4263 |               5 |            2.5641 |

===== TONG KET IQR =====
Tổng số feature: 22
Feature có outlier: 19
Feature không có outlier: 3
Tổng số mẫu: 195
Số mẫu có ít nhất một outlier: 47
Tỷ lệ: 24.1 %
Đã xuất bảng IQR:
Số feature trong bảng: 22

**Nhận xét:** Có 19/22 feature xuất hiện giá trị ngoài ngưỡng IQR. Có 47/195 mẫu (24,10%) chứa ít nhất một candidate outlier. NHR là feature cần được chú ý do có 19 giá trị được đánh dấu.

Candidate outlier theo IQR không đồng nghĩa chắc chắn là dữ liệu sai. Không tự động xóa các mẫu này. Cần kiểm tra phân phối, ý nghĩa chuyên môn và ảnh hưởng đến mô hình trước khi quyết định giữ, biến đổi hoặc xử lý.

## 6. Thang đo và đề xuất tiền xử lý cho M04

Các feature có thang đo khác nhau đáng kể. Ví dụ, `MDVP:Fo(Hz)`, `MDVP:Fhi(Hz)`, `MDVP:Flo(Hz)` có giá trị ở mức hàng trăm, trong khi `MDVP:Jitter(Abs)` có giá trị rất nhỏ.

Đề xuất cho bước M04:

1. **Kiểm tra candidate outlier:** Đối chiếu các feature có outlier, đặc biệt là NHR, với kết quả khám phá M02 và đánh giá ảnh hưởng đến mô hình.
2. **Không xóa tự động:** Chỉ loại bỏ hoặc biến đổi giá trị khi có căn cứ cho thấy dữ liệu sai hoặc phương pháp xử lý phù hợp với mục tiêu mô hình.
3. **Chuẩn hóa feature:** Cân nhắc sử dụng `StandardScaler` trước PCA và các mô hình nhạy với thang đo.
4. **Tránh data leakage:** Chỉ `fit` scaler trên tập train; sau đó dùng scaler đã fit để `transform` validation/test. Không fit scaler trên toàn bộ dataset trước khi chia tập.
5. **Mất cân bằng nhãn:** Duy trì phân tầng khi chia tập và đánh giá bằng các metric phù hợp như Precision, Recall, F1-score và Confusion Matrix.

Việc sử dụng `StandardScaler` cần được thực hiện trong pipeline tiền xử lý của M04, không phải bằng cách chuẩn hóa toàn bộ dữ liệu trước khi chia train/test.

## 7. Kết luận

- Canonical dataset có 195 mẫu, 22 feature và 1 cột nhãn `status`.
- Phân bố nhãn mất cân bằng: Parkinson chiếm 75,38%, khỏe chiếm 24,62%.
- Không phát hiện giá trị thiếu hoặc dòng trùng lặp trong lần kiểm tra hiện tại.
- M03-T1 đã bổ sung thống kê mô tả gồm mean, median, std, min, max, skew và kurtosis.
- M03-T2 đã kiểm tra candidate outlier bằng IQR: 19/22 feature có candidate outlier và 47/195 mẫu có ít nhất một candidate outlier.
- M04 cần tiếp tục đánh giá candidate outlier và cân nhắc chuẩn hóa bằng `StandardScaler` trong pipeline phù hợp.

## 8. Phương pháp, giả định và khả năng tái lập

- **Nguồn dữ liệu:** `data/processed/parkinsons_v1.csv`, phiên bản v1.
- **Đường dẫn:** Sử dụng đường dẫn tương đối từ thư mục gốc dự án.
- **Phạm vi thống kê:** 22 feature số; không đưa `status` vào thống kê feature.
- **Kiểm tra outlier:** IQR với hệ số 1.5.
- **Giả định:** Các giá trị ngoài ngưỡng IQR là candidate outlier để xem xét, không mặc định là lỗi dữ liệu.
- **Random seed:** Không áp dụng cho các phép thống kê mô tả và IQR trong M03 vì không có bước lấy mẫu ngẫu nhiên.
- **Phiên bản môi trường:**
Python version: 3.11.15 (main, Mar  3 2026, 00:52:57) [Clang 17.0.0 (clang-1700.6.3.2)]
Pandas version: 3.0.3
NumPy version: 2.4.6
- **Tái lập:** Chạy Notebook `notebooks/01_data_exploration.ipynb` từ thư mục gốc dự án trên canonical CSV.
- **Giới hạn:** Kết quả phụ thuộc vào phiên bản dữ liệu đầu vào và môi trường thực thi. Khi dữ liệu hoặc môi trường thay đổi, cần chạy lại Notebook và cập nhật báo cáo.

---

**Bàn giao:** Báo cáo này thuộc nhiệm vụ M03-T3, phục vụ reviewer M01; kết quả thống kê và kiểm tra chất lượng được bàn giao cho M02/M04 đối chiếu và tiếp tục xử lý.