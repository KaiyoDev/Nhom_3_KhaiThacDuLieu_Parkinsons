# notebooks/ — 5 notebook khung (skeleton)

> **Hiện tại: 5 notebook KHUNG đã được tạo** — có markdown hướng dẫn + cell `TODO`,
> **chưa có code phân tích / kết quả / biểu đồ / output chạy sẵn**. Thành viên triển khai
> từng cell theo **work-order** trong `workspaces/member-XX/README.md`.

## Danh sách notebook ↔ thành viên

| Notebook | Phụ trách | Nhiệm vụ |
|----------|-----------|----------|
| `01_data_exploration.ipynb` | M02 + M03 | khám phá + thống kê mô tả + chất lượng |
| `02_preprocessing_pca.ipynb` | M04 | tiền xử lý + PCA + scatter tô màu |
| `03_classification.ipynb` | M05 | 10-fold CV + 3 mô hình + F-score |
| `04_clustering.ipynb` | M06 | K-Means + DBSCAN + ARI |
| `05_integration_report.ipynb` | M06 (chủ) + M01 (gate) | tổng hợp + nhất quán + xuất PDF |

## Quy định khi triển khai

- Mỗi notebook **tham chiếu canonical CSV** `data/processed/parkinsons_v1.csv` (do **M01-T2**
  tạo, xác nhận S-T1) — **không** dùng CSV riêng (xem `data/README.md`).
- **Không bịa kết quả:** mọi số / biểu đồ phải từ **chạy thật**; kết quả lưu `results/`.
- **Không hardcode** đường dẫn máy cá nhân (chạy từ gốc project; Colab xem `docs/COLAB_GUIDE.md`).
- Seed + phiên bản thư viện: `docs/REPRODUCIBILITY.md`.
- **PCA / phân cụm: không dùng nhãn `status` làm feature** (chỉ tô màu / diễn giải / đánh giá ARI).
- Notebook phân lớp (03): tránh **data leakage** (scaler/PCA fit trên train fold).

## Hiện trạng

- 5 notebook ở trạng thái **khung / `Todo`**: chưa chạy mô hình, chưa có output.
- Khi triển khai + hoàn thành từng phần → commit notebook + kết quả (theo `docs/GITHUB_GUIDE.md`).
