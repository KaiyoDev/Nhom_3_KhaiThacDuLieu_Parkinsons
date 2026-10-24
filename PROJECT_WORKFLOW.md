# PROJECT_WORKFLOW — Luồng tổng thể (Nhóm 3 · Parkinson)

> Mục đích: mô tả **con đường làm việc** từ chuẩn bị dữ liệu đến báo cáo, kèm các
> "cổng" (gate) đồng bộ. Ở giai đoạn setup, file này **chỉ là kế hoạch luồng**,
> **chưa triển khai** bất kỳ bước phân tích nào.

## 1. Luồng chính (end-to-end)

```text
G1  CHUẨN BỊ DỮ LIỆU        M01   raw → canonical processed CSV (1 đầu vào duy nhất)
        │
G2  ĐỒNG BỘ ĐẦU VÀO         ALL   S-T1: toàn nhóm xác nhận canonical CSV  ← CỬA CẢNH GATE #1
        │
G3  KHÁM PHÁ & CHẤT LƯỢNG   M02+M03  cấu trúc/dtype + thống kê mô tả + kiểm tra chất lượng
        │                    (bàn giao vấn đề cho M04)
G4  TIỀN XỬ LÝ & GIẢM CHIỀU M04   feature matrix (22 cột) → PCA → trực quan
        │
G5  MÔ HÌNH                 M05+M06  phân lớp + CV + F-score  |  phân cụm + ARI
        │
G6  TỔNG HỢP               M06+M01  M06 tổng hợp (chủ trì), M01 ký nhất quán  ← CỬA CẢNH GATE #2
        │
G7  BÁO CÁO                M06+M01  reports/ hoàn thiện + nghiệm thu cuối
```

> Hai "cổng" (gate) là điểm đồng bộ bắt buộc:
> **GATE #1 (S-T1)** — mọi thứ từ G3 trở đi phải dùng **cùng** canonical CSV.
> **GATE #2 (S-T2)** — trước khi hoàn thiện báo cáo, toàn bộ kết quả phải nhất quán.

## 2. Giai đoạn & người phụ trách

| Giai đoạn | Nội dung | Phụ trách chính | Gate | Đầu ra |
|-----------|----------|-----------------|------|--------|
| G1 | Chuẩn bị dữ liệu | M01 | — | `data/raw/`, `data/processed/` (canonical CSV + schema) |
| G2 | Đồng bộ đầu vào | Toàn nhóm | **GATE #1** | Xác nhận S-T1 |
| G3 | Khám phá + chất lượng | M02, M03 | — | Báo cáo cấu trúc, thống kê, chất lượng (`results/`) |
| G4 | Tiền xử lý + PCA + TVH | M04 | — | Feature matrix, PCA, figure (`results/`) |
| G5 | Phân lớp & phân cụm | M05, M06 | — | F-score, ARI (`results/`) |
| G6 | Tổng hợp | M06 (chủ) + M01 (gate) | **GATE #2** | `reports/summary.md` (bản thảo) |
| G7 | Báo cáo & nghiệm thu | M06 + M01 | — | `reports/` hoàn thiện |

> **Không để M01 làm tất cả việc tích hợp:** tổng hợp (G6) do **M06 chủ trì**;
> M01 chỉ đóng vai **gate nhất quán** (M01-T4 / S-T2).

## 3. Luồng trạng thái (Task Board)

```text
Todo → In Progress → Review → Done
   ↘ (thiếu đầu vào / phụ thuộc chưa xong)
       Blocked
```

- Mỗi nhiệm vụ (xem `TASK_ASSIGNMENTS.md`) bắt đầu `Todo`.
- Chỉ `Review → Done` khi **người review** xác nhận đạt tiêu chí nghiệm thu.
- M01 cập nhật `TASK_BOARD.md` khi có chuyển trạng thái; không tự đánh `Done`.

## 4. Ràng buộc đồng bộ dữ liệu

- **Một canonical processed CSV duy nhất** (M01-T2) là đầu vào cho mọi bước G3–G6.
- Không ai tạo bản CSV riêng; mọi biến đổi (scale, chọn PCA, chọn K) được **ghi lại**
  trong `results/`/notebook và tham chiếu cùng canonical CSV.
- Khi có nghi ngờ lệch chuẩn → M01 (gate) kiểm tra lại tính nhất quán trước khi qua gate.

## 5. Ràng buộc tái tạo (xem `docs/REPRODUCIBILITY.md`)

- Mỗi bước phải **chạy lại được** kết quả giống (seed, phiên bản thư viện, ngưỡng).
- Kết quả ghi trong `results/`, báo cáo trong `reports/`, code trong `src/`/`notebooks/`.

## 6. Phạm vi KHÔNG nằm ở giai đoạn setup

- Chưa tạo notebook, chưa viết code phân tích, chưa chạy mô hình, chưa có kết quả thật.
- Chưa commit / push / PR / merge (xem `docs/GITHUB_GUIDE.md`).
- File này chỉ **mô tả luồng**; các bước phân tích sẽ được triển khai khi mở giai đoạn làm việc.
