# M06-T1/T2 · Báo cáo kết quả phân cụm + ARI (Nhóm 3 · Parkinson)

- Nhiệm vụ: M06-T1, M06-T2 · Người làm: M06 · Ngày chạy: 2026-11-22
- Notebook: `notebooks/04_clustering.ipynb` · Kết quả thô: `results/m06_cluster_ari.csv`
- Reviewer: M05 (M06-T1), M01 gate (M06-T2) · Trạng thái: chờ review

## 1. Thiết lập

| Mục | Giá trị |
|-----|---------|
| Dữ liệu | 195 dòng, 22 feature; `status`: 1 = 147 mẫu, 0 = 48 mẫu (lệch lớp) |
| Đầu vào | 22 feature chuẩn hoá `StandardScaler`; **không** có `status`/`name` (có `assert`); nhãn chỉ dùng để tính ARI |
| K-Means | K = 2..10, `n_init=10`, `random_state=42`; chọn K theo silhouette cao nhất |
| DBSCAN | `min_samples=5`, `eps=3.37` (knee của đồ thị k-distance, không dùng nhãn) |
| Chỉ số | silhouette, ARI so với `status` (điểm nhiễu -1 tính là một nhóm riêng) |

## 2. Kết quả (số thật từ lần chạy)

**K-Means** (K chọn = **2**):

| K | silhouette | Cỡ cụm | ARI |
|---|---|---|---|
| 2 | 0.4373 | [165, 30] | -0.0978 |
| 3 | 0.2763 | [106, 77, 12] | 0.0582 |
| 4 | 0.2358 | [91, 77, 23, 4] | 0.0583 |
| 5 | 0.2048 | [73, 64, 32, 22, 4] | 0.1000 |
| 6 | 0.2138 | [60, 51, 30, 28, 22, 4] | 0.1058 |
| 7 | 0.2094 | [54, 51, 31, 24, 23, 8, 4] | 0.0882 |
| 8 | 0.2201 | [53, 35, 32, 23, 23, 15, 10, 4] | 0.0313 |
| 9 | 0.2265 | [52, 39, 25, 24, 21, 13, 9, 8, 4] | 0.0574 |
| 10 | 0.1896 | [38, 35, 26, 23, 22, 18, 12, 9, 8, 4] | 0.0481 |

**DBSCAN:**

| eps | min_samples | Số cụm | Điểm nhiễu (-1) | ARI |
|---|---|---|---|---|
| 3.37 | 5 | 1 | 12 | -0.0639 |

Hình: `results/figures/m06_chon_tham_so.png`, `results/figures/m06_pca2d_cum_vs_status.png` (PCA 2D chỉ để minh hoạ).

## 3. Quan sát (chỉ mô tả số liệu)

- Silhouette cao nhất ở K=2 (0.4373); từ K=3 trở đi chỉ còn 0.1896–0.2763.
- ARI của K-Means nằm trong -0.0978 đến 0.1058 (cao nhất ở K=6); K=2: -0.0978. DBSCAN: -0.0639.
- K=2 tách cụm nhỏ 30 mẫu (30/30 có status=1; nổi bật Shimmer:APQ5, MDVP:Shimmer, MDVP:Shimmer(dB)). DBSCAN có 12 điểm nhiễu, trong đó 12/12 có status=1.

## 4. Lưu ý

- Chuẩn hoá lại trong notebook vì feature matrix M04-T1 chưa bàn giao.
- Dữ liệu lấy từ file xlsx gốc vì canonical CSV (M01-T2) chưa có; cần chạy lại khi M01-T2 xong.
- Dữ liệu nhỏ, lệch lớp; DBSCAN nhạy với `eps`, `min_samples` (ARI trên lưới thử từ -0.0744 đến 0.1625).

## 5. Kết luận

*(Để trống: M06 và reviewer cùng kết luận.)*

## 6. Tái lập

Seed 42 · K-Means `n_init=10` · phiên bản thư viện: cột `sklearn` trong `results/m06_cluster_ari.csv`.
