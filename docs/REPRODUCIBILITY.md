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

- **Seed:** `42` (mặc định cho toàn bộ). Nếu đổi → ghi lý do + ai đổi.
- **k-fold CV:** `k = 5`, stratified (theo `status`).
- **Test set:** tách **1 lần cuối**, không "dùng lại" cho chọn mô hình (tránh overfit).
- **PCA:** giữ thành phần đến khi **total explained variance ≥ 90%** (hoặc theo M04-T2
  thống nhất, ghi rõ ngưỡng).
- **K (cluster):** chọn bằng silhouette + elbow; **ghi rõ K giữ lại** và lý do.
- **Scaler:** `StandardScaler` (mặc định, nếu M03-T2 không đề xuất khác).
- **F-score:** macro (nhiều lớp / cân bằng) hoặc weighted (gọi rõ khi báo cáo).
- **ARI:** tính trên nhiều giá trị K; ghi rõ K tham chiếu so với `status`.

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
