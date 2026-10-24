# M06 — Phân cụm + ARI + Hỗ trợ tổng hợp kết quả (Work-order)

## 1. Thông tin
| | |
|---|---|
| Mã | `M06` |
| Tên / MSSV | `[CHƯA CẬP NHẬT]` |
| Vai trò | Phân cụm (K-Means, DBSCAN) + ARI; **chủ trì tổng hợp** (nhận M01 gate) |
| Trạng thái | `Todo` |

## 2. Bạn làm ở đâu
- **Notebook 04:** `notebooks/04_clustering.ipynb` (phân cụm + ARI).
- **Notebook 05:** `notebooks/05_integration_report.ipynb` (**chủ trì tổng hợp** báo cáo).

> ⚠️ **Lưu ý quan trọng (M06 ≠ M01):** tổng hợp (M06-T3) do **M06 chủ trì** (viết
> `reports/summary.md`); **M01 chỉ gate nhất quán** (M01-T4 / S-T2). M01 **không** tự làm
> toàn bộ việc tích hợp (xem `PROJECT_WORKFLOW.md` mục 2).

## 3. Nhiệm vụ giao (theo `TASK_ASSIGNMENTS.md`)
| Mã | Việc | Nơi làm | Đầu vào | Đầu ra | Tiêu chí | Reviewer | Chặn bởi |
|----|------|---------|---------|--------|----------|----------|----------|
| M06-T1 | Phân cụm (K-Means + DBSCAN, chọn K) | nb04 Bước 1–4 | feature matrix (M04-T1) | kết quả cụm + figure | chọn K có giải trình (silhouette/elbow), DBSCAN ghi eps/min_samples | M05 | M04-T1 |
| M06-T2 | ARI (so cluster với `status`) | nb04 Bước 5 | M06-T1 | ARI (nhiều K) | ARI đúng định nghĩa, so nhiều K | M01 (gate) | M06-T1 |
| M06-T3 | **Tổng hợp kết quả** (chủ trì) | nb05 Bước 1–7 | M05-T3, M06-T2, kết quả 02/03/04 | `reports/summary.md` (bản thảo) | nhất quán, chỉ dùng kết quả ĐÃ review | M01 | M05-T3, M06-T2 |

## 4. Thứ tự thực hiện (cụ thể)
### A) `notebooks/04_clustering.ipynb`
0. **Điều kiện:** cần **feature matrix (M04-T1)**. Nếu chưa có → **Blocked** (chờ M04-T1).
1. **Bước 1:** chuẩn bị `X` (22 feature). Chạy `assert "status" not in X.columns` (nhãn **không**
   vào input cụm).
2. **Bước 2:** chuẩn hoá (dùng `Xs` từ M04 hoặc chuẩn hoá lại; ghi quyết định).
3. **Bước 3:** K-Means nhiều K (vd 2,3,4) + chọn K bằng silhouette/elbow.
4. **Bước 4:** DBSCAN (chọn `eps`, `min_samples`; ghi số điểm nhiễu `-1`).
5. **Bước 5 (M06-T2):** tính **ARI** so với `status` thật (label chỉ dùng ở bước này).

### B) `notebooks/05_integration_report.ipynb` (chủ trì M06-T3)
6. Cập nhật **bảng trạng thái** 4 notebook (chỉ đổi khi nguồn `Done`).
7. **Bước 1–4:** tổng hợp dataset (đã xác minh) + PCA (nb02) + phân lớp (nb03) + phân cụm (nb04).
   **Kết quả nào chưa bàn giao → giữ `Pending`, KHÔNG bịa.**
8. **Bước 5:** nhận xét **chỉ trên kết quả đã review** (trỏ về `results/`).
9. **Bước 6:** ghi **hạn chế** (dữ liệu ~195, cân bằng label, cách chọn K, F-score macro/weighted,
   2 điểm CẦN XÁC MINH từ notebook 03, "197 vs 195" UCI).
10. **Bước 7:** khu kết luận **cất trống** → cùng M01 (gate M01-T4/S-T2) điền sau khi nhất quán.
11. Xuất PDF từng notebook (checklist ở nb05) khi đủ điều kiện.

## 5. Đầu vào cần nhận
- **Feature matrix (M04-T1)** (cho phân cụm) + **M05-T3** (kết quả phân lớp) + kết quả 02/03/04
  (cho tổng hợp). Không nguồn nào đủ → mục tương ứng **`Pending`**.

## 6. Đầu ra phải bàn giao
- Kết quả K-Means/DBSCAN + ARI → `results/` (không kết quả giả).
- `reports/summary.md` (bản thảo tổng hợp) → `reports/`.
- Bản thảo báo cáo cho gate M01 (M01-T4/S-T2).

## 7. Tiêu chí nghiệm thu (đo được)
- K-Means: có K chọn + silhouette; DBSCAN: có eps/min_samples + số nhiễu (-1).
- ARI (nhiều K) so với `status` — tính đúng (ARI=1 khớp, 0 ngẫu nhiên, <0 kém hơn).
- `summary.md`: nhất quán (cùng canonical CSV v1, cùng quy ước), chỉ dùng kết quả đã review;
  mục thiếu ghi `Pending`.

## 8. Checklist tự kiểm
- [ ] Chờ M04-T1 (feature matrix); thiếu → Blocked.
- [ ] `assert "status" not in X.columns` (label không vào input cụm).
- [ ] K-Means (nhiều K + chọn K) + DBSCAN (eps/min_samples, đếm -1) + ARI.
- [ ] `reports/summary.md` chỉ tổng hợp kết quả ĐÃ review; mục chưa có → `Pending`.
- [ ] Đã ghi hạn chế + 2 điểm CẦN XÁC MINH (từ nb03).
- [ ] Bàn giao M01 (gate M01-T4/S-T2); chuyển M06-T1..T3 sang `Review` trong `TASK_BOARD.md`.

## 9. Người review
M06-T1 → **M05** · M06-T2 → **M01 (gate)** · M06-T3 → **M01 (gate)** (M06 chủ trì, M01 ký nhất quán).

## 10. Bàn giao & Blocked
- Theo `HANDOFF.md` (5 dòng + test-report: K/eps, ARI, silhouette).
- **Blocked (phân cụm):** thiếu M04-T1. **Blocked (tổng hợp):** notebook 02/03/04 chưa `Done`
  → các mục tổng hợp giữ `Pending`, ghi "chờ Mxx" trong `TASK_BOARD.md`, thông báo M01.

## 11. Trạng thái
`Todo` — M06-T1 chờ **M04-T1**; M06-T3 chờ **M05-T3 + M06-T2**.
