# M05-T3 · Báo cáo kết quả phân lớp (Nhóm 3 · Parkinson)

- Nhiệm vụ: M05-T1, M05-T2, M05-T3 · Người làm: M05 · Ngày chạy: 2026-11-14
- Notebook: `notebooks/03_classification.ipynb` · Kết quả thô: `results/m05_f1_cv.csv`
- Reviewer: M01 (gate) + M06 · Trạng thái: chờ review

## 1. Dữ liệu và thiết lập

| Mục | Giá trị |
|-----|---------|
| Dữ liệu | canonical CSV `parkinsons_v1.csv` (195 dòng, 22 feature + `status`) |
| Nhãn | `status`: 1 = Parkinson (147 mẫu), 0 = khỏe (48 mẫu) → lệch lớp |
| Chuẩn hoá | `StandardScaler` nằm trong `Pipeline`, fit riêng trên fold train (tránh leakage) |
| CV ngoài | `StratifiedKFold(n_splits=10, shuffle=True, random_state=42)` |
| Chọn tham số | `GridSearchCV` 5-fold chạy bên trong fold train (nested CV), điểm chọn: `f1_macro` |
| Mô hình (3/5) | KNN, SVM, Random Forest |
| Chỉ số | F-score macro (chính) và weighted (đối chiếu), mean ± std trên 10 fold |

Lưới tham số: KNN `n_neighbors` ∈ {3, 5, 7}; SVM `C` ∈ {0.1, 1, 10}; Random Forest `n_estimators` ∈ {50, 100}.

Lý do chọn mô hình: KNN làm baseline dựa trên khoảng cách; SVM tìm ranh giới phân tách có lề lớn; Random Forest là tổ hợp nhiều cây quyết định, ít nhạy với thang đo của feature. Ba mô hình thuộc ba họ khác nhau nên dễ so sánh.

## 2. Kết quả (CV 10-fold, số thật từ lần chạy)

| Mô hình | F-score macro (test) | F-score weighted (test) | F-score macro (train) |
|---------|:-------------------:|:-----------------------:|:---------------------:|
| KNN | 0.8757 ± 0.0742 | 0.9073 ± 0.0578 | 0.9647 |
| SVM | 0.8904 ± 0.0804 | 0.9199 ± 0.0603 | 0.9787 |
| Random Forest | 0.8737 ± 0.1171 | 0.9103 ± 0.0824 | 1.0000 |

## 3. Quan sát (chỉ mô tả số liệu, chưa kết luận mô hình tốt nhất)

- Chênh lệch giữa các mô hình về F-score macro (test) khoảng 0.016, nhỏ hơn độ lệch chuẩn giữa các fold (0.07–0.12).
- F-score weighted cao hơn macro ở cả 3 mô hình. Điều này phù hợp với việc lớp 0 (khỏe) ít mẫu hơn nên điểm riêng của lớp này kéo macro xuống.
- Điểm train cao hơn điểm test ở cả 3 mô hình. Khoảng cách lớn nhất ở Random Forest (train 1.0000, test 0.8737), đồng thời std của Random Forest cũng lớn nhất (0.1171).

## 4. Assumptions / điểm đã quyết định

- Số fold: dùng k=10 theo đề bài notebook 03 và work-order M05 (docs/REPRODUCIBILITY.md đang ghi k=5, đề nghị M01 cập nhật cho khớp).
- Loại F-score: macro là chỉ số chính vì dữ liệu lệch lớp; weighted ghi kèm để đối chiếu. Cần M06 xác nhận.
- Dùng `X` gốc từ canonical CSV với `Pipeline`, không dùng ma trận chuẩn hoá riêng của M04.
- Tham số tối ưu của từng fold chưa được lưu; bảng chỉ báo điểm trung bình.

## 5. Hạn chế

- Dữ liệu nhỏ (195 mẫu): mỗi fold test chỉ có khoảng 20 mẫu, trong đó khoảng 5 mẫu lớp khỏe, nên điểm giữa các fold dao động lớn.
- Lệch lớp 147/48; dù đã dùng CV có phân tầng, kết quả vẫn nhạy với lớp ít mẫu.
- Dataset gồm nhiều bản ghi của cùng một người (khoảng 31 người), cột `name` đã bị loại khỏi canonical CSV nên `StratifiedKFold` có thể đặt bản ghi của cùng một người vào cả train và test. Điểm test vì vậy có thể cao hơn so với thực tế.
- Mới so sánh 3 mô hình với lưới tham số nhỏ.

## 6. Kết luận

*(Để trống: M01 và M06 cùng reviewer kết luận theo đúng work-order.)*

## 7. Tái lập

Seed 42 · k ngoài = 10 · k trong = 5 · canonical CSV v1 · phiên bản thư viện: xem cột `sklearn` trong `results/m05_f1_cv.csv`.
