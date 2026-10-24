# M05 — Phân lớp + Cross-validation + F-score (Work-order)

## 1. Thông tin
| | |
|---|---|
| Mã | `M05` |
| Tên / MSSV | `[CHƯA CẬP NHẬT]` |
| Vai trò | Phân lớp nhị phân, 10-fold CV, so sánh 3 mô hình bằng F-score |
| Trạng thái | `Todo` |

## 2. Bạn làm ở đâu
- **Notebook:** `notebooks/03_classification.ipynb`.
- **Các phần bạn phụ trách:** `Bước 1` biến mục tiêu · `Bước 2` chuẩn bị `X`/`y` ·
  `Bước 3` quy trình tiền xử lý (chống leakage) · `Bước 4` 10-fold CV ·
  `Bước 5` chọn 3/5 mô hình · `Bước 6` phạm vi tinh chỉnh · `Bước 7` F-score.

## 3. Nhiệm vụ giao (theo `TASK_ASSIGNMENTS.md`)
| Mã | Việc | Nơi làm | Đầu vào | Đầu ra | Tiêu chí | Reviewer | Chặn bởi |
|----|------|---------|---------|--------|----------|----------|----------|
| M05-T1 | Train/test + k-fold CV | nb03 Bước 1–4 | feature matrix (M04-T1) | quy ước CV (k, seed, stratified) + anti-leakage | CV lặp lại được, ghi seed/k | M01 | M04-T1 |
| M05-T2 | 3 mô hình + F-score | nb03 Bước 5–7 | M05-T1 | F-score (CV) theo 3 mô hình (mean ± std) | đủ 3 mô hình trong 5, có CV, ghi F-score thật | M01 (gate) + M06 | M05-T1 |
| M05-T3 | Báo cáo kết quả phân lớp | `results/classification_report.md` | M05-T2 | bảng so sánh + nhận xét | so sánh được 3 mô hình | M06 | M05-T2 |

## 4. Thứ tự thực hiện (cụ thể, trong `notebooks/03_classification.ipynb`)
0. **Điều kiện:** cần **feature matrix chuẩn hoá (M04-T1)**. Nếu chưa có → **Blocked** (chờ M04-T1).
   Kiểm tra lại 2 điểm **CẦN XÁC MINH** (xem §7) trước khi chạy chính thức.
1. **Bước 1–2:** `y = status` (nhị phân), `X` = 22 feature. Xây pipeline `scaler + model`
   để **chống data-leakage** (scaler fit trên train fold, transform trên val fold).
2. **Bước 3:** ghi quy trình anti-leakage: tune tham số **chỉ trên fold train** (inner CV),
   test set dùng **một lần** ở cuối.
3. **Bước 4:** `StratifiedKFold(n_splits=10, shuffle=True, random_state=42)`.
4. **Bước 5:** chọn **đúng 3** trong {KNN, Random Forest, Naive Bayes, AdaBoost, SVM}.
5. **Bước 6:** đặt **vài giá trị thử** cho 1–2 tham số/mô hình (không chạy lưới lớn).
6. **Bước 7:** chạy CV, thu **F-score** (mean ± std) theo từng mô hình → **bảng so sánh**
   (KHÔNG tự điền "mô hình nào tốt nhất" — để reviewer + M06 kết luận).
7. **M05-T3:** viết `results/classification_report.md` (so sánh 3 mô hình + ghi 2 điểm CẦN XÁC MINH).

## 5. Đầu vào cần nhận
- **Feature matrix (M04-T1)** + canonical CSV. Không tự chạy lại tiền xử lý riêng
  (dùng pipeline chuẩn hoá của M04 hoặc Pipeline trong notebook).

## 6. Đầu ra phải bàn giao
- Quy ước CV (k=10, seed) + **F-score 3 mô hình** (mean ± std) → `results/`.
- `results/classification_report.md` (M05-T3) + cập nhật `docs/REPRODUCIBILITY.md` (seed, k, F-score).

## 7. Tiêu chí nghiệm thu + 2 điểm CẦN XÁC MINH (đánh dấu, không tự đoán)
- CV stratified 10-fold, anti-leakage đúng (pipeline), đủ **3/5** mô hình, F-score thật.
- ⚠️ **Xác minh 1 — số fold:** đề bài notebook 03 dùng **k=10**, nhưng
  `docs/REPRODUCIBILITY.md` ghi **k=5** → thống nhất (M05-T1) + ghi quyết định.
- ⚠️ **Xác minh 2 — loại F-score:** tài liệu chưa chốt **macro** hay **weighted** (nên cân
  nhắc macro vì bài cân bằng) → thống nhất (M05-T2/M06) + ghi lại.

## 8. Checklist tự kiểm
- [ ] Chờ M04-T1 (feature matrix); thiếu → Blocked.
- [ ] Pipeline anti-leakage (scaler/PCA fit trên train fold); tune không chạm test.
- [ ] 10-fold stratified CV (ghi seed, k).
- [ ] Đúng 3/5 mô hình; F-score (mean ± std) **từ kết quả thật** vào bảng.
- [ ] Đã đánh dấu 2 điểm CẦN XÁC MINH (k, F-score) trong notebook + `TASK_BOARD.md`.
- [ ] Đã chuyển M05-T1..T3 sang `Review` + thông báo M01 (gate) & M06.

## 9. Người review
M05-T1 → **M01** · M05-T2 → **M01 (gate) + M06** · M05-T3 → **M06**.

## 10. Bàn giao & Blocked
- Theo `HANDOFF.md` (5 dòng + test-report: k, seed, F-score 3 mô hình mean ± std).
- **Blocked:** thiếu feature matrix (M04-T1) → "chờ M04-T1", thông báo M01.

## 11. Trạng thái
`Todo` — chờ **M04-T1**.
