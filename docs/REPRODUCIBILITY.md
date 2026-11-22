# REPRODUCIBILITY — Tái tạo kết quả (Nhóm 3 · Parkinson)

> Mục đích: bất kỳ kết quả nào cũng phải **chạy lại được** cùng số (hoặc chênh lệch
> có giải thích được). Ghi rõ mọi "thông số" để 6 thành viên không sinh ra các bản
> kết quả khác nhau.

## 1. Ba trụ cột của tái tạo

1. **Dữ liệu:** canonical CSV `data/processed/parkinsons_v1.csv` (version v1). Mọi bước
   phải nạp **cùng** file này — không bản CSV riêng (xem `data/README.md`).
2. **Tham số:** seed, k (CV), ngưỡng PCA, K (cluster), chuẩn hoá, xử lý NaN.
3. **Môi trường:** phiên bản Python + thư viện (pin trong `requirements.txt`).

## 2. Ghi lại ở đâu, khi nào

| Loại | Ghi vào | Ghi khi |
|------|---------|---------|
| Seed, k-fold, ngưỡng PCA, K, loại scaler | `docs/REPRODUCIBILITY.md` (phần §3) | M04-T1 / M05-T1 (lần đầu dùng) |
| Phiên bản thư viện | `requirements.txt` (pin khi thống nhất) | M01 (điều phối) trước khi chạy rộng |
| Kết quả + tham số dùng | `results/<mã-nhiệm-vụ>.md` hoặc CSV/JSON | Người phụ trách nhiệm vụ đó |
| Figure (nếu có) | `results/figures/` | Cùng lúc sinh figure |

## 3. Quy ước tham số (thống nhất 1 lần, dùng chung)

> **Chốt ngày 2026-11-22** (sau khi hợp nhánh PR #5 / #8 / #9).

- **Seed:** `42` (mặc định cho toàn bộ). Nếu đổi → ghi lý do + ai đổi.
- **k-fold CV (phân lớp):** **k ngoài = 10**, **k trong (chọn tham số) = 5**, stratified
  theo `status`. Đây là quy ước chung; trước đây tài liệu ghi k=5 đã được cập nhật.
- **Test set:** trong thiết lập CV lồng nhau, fold test chỉ dùng để đánh giá; chọn tham số
  chỉ chạy trên fold train (tránh overfit / leakage).
- **PCA:** để trực quan hóa dùng **2 thành phần** (PC1 + PC2 = 70.2%); nếu cần đạt
  ngưỡng **≥ 90%** phương sai thì giữ **6 thành phần** (91.61%) — theo M04-T2.
- **K (cluster):** chọn bằng silhouette + elbow; **ghi rõ K giữ lại** và lý do.
- **Scaler:** `StandardScaler`, fit **chỉ trên train** trong Pipeline khi phân lớp;
  đối với PCA/phân cụm (không giám sát) có thể fit trên toàn bộ `X` (ghi rõ).
- **F-score:** **macro** là chỉ số chính (dữ liệu lệch lớp 147/48); **weighted** ghi kèm
  để đối chiếu. Ghi rõ loại khi báo cáo.
- **ARI:** tính trên nhiều giá trị K; ghi rõ K tham chiếu so với `status`.
- **Phiên bản đã dùng:** `scikit-learn 1.9.0`, `pandas 3.0.x`, `numpy 2.4.x`
  (chi tiết trong `results/m05_f1_cv.csv` và `results/pipeline_summary.json`).

## 4. Khi "không tái tạo được"

- Ghi lại: seed dùng, phiên bản thư viện, đường dẫn dữ liệu, code chạy → mở issue trong
  `TASK_BOARD.md` (hạng mục liên quan) + nhờ M01 (điều phối) phân công soát.
- **Không** bịa số để "kèm" cho khớp.

## 5. Pin phiên bản (khi mở giai đoạn phân tích)

Sau khi thống nhất:

```bash
pip freeze > requirements.lock   # tạo bản "đã pin"
```

- Mỗi thành viên dùng `requirements.lock` (không dùng `requirements.txt` loose khi chạy
  kết quả chính thức).
- Colab: chạy `!pip install -r requirements.lock` (xem `docs/COLAB_GUIDE.md`).

## 6. Checklist tái tạo (trước khi báo cáo)

- [ ] Dữ liệu: canonical CSV đúng version (v1).
- [ ] Tham số: seed, k, ngưỡng, K, scaler, loại F-score → đã ghi trong §3.
- [ ] Môi trường: `requirements.lock` (hoặc bản pin tương đương).
- [ ] Kết quả: có file trong `results/` với đầy đủ tham số + ngày + mã nhiệm vụ.
- [ ] Chạy lại pipeline → số khớp (hoặc chênh lệch có giải thích được).
