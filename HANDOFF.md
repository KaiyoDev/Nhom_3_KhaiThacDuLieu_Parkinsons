# HANDOFF — Quy trình bàn giao giữa các thành viên (Nhóm 3 · Parkinson)

> Bàn giao = chuyển **đầu ra** của một nhiệm vụ cho người dùng tiếp theo / reviewer.
> Áp dụng khi một hạng mục trong `TASK_BOARD.md` chuyển từ `In Progress → Review`.

## 1. File nào cần giao (theo hạng mục)

| Khi bàn giao | File / đầu ra bắt buộc kèm |
|--------------|------------------------------|
| M01-T2 (canonical CSV) | `data/processed/parkinsons_v1.csv` + `data/processed/schema_v1.md` |
| M02-T1/T2 (khám phá) | Bảng khám phá + cập nhật `DATA_DICTIONARY.md` (cột Kiểu/Thiếu/Ghi chú) |
| M03-T3 (chất lượng) | `results/quality_report.md` + đề xuất xử lý cho M04 |
| M04-T1 (feature matrix) | Code tiền xử lý (`src/`/notebook) + quy ước scaler/xử lý NaN (ghi trong `docs/REPRODUCIBILITY.md`) |
| M05-T3 (phân lớp) | `results/classification_report.md` (F-score theo CV) |
| M06-T2 (ARI) | Kết quả ARI (nhiều K) trong `results/` |
| M06-T3 (tổng hợp) | `reports/summary.md` (bản thảo, tham chiếu các `results/`) |

> Nguyên tắc: **kèm đủ đầu ra + nơi lưu + tham số dùng** — không "chỉ gửi thông báo".

## 2. Cách mô tả thay đổi (bắt buộc trong mỗi lần bàn giao)

Định dạng ngắn, 5 dòng:

```text
[Hạng mục]  M04-T2 · PCA (M04)
[Đã làm]    Chạy PCA, giữ 8 thành phần (variance ≥ 90%)
[Đầu ra]    results/pca_m04.csv, results/figures/pca_var.png
[Tham số]    seed=42, canonical CSV v1, scaler=Standard
[Lưu ý]      Ngưỡng 90% do M03-T2 đề xuất; nếu đổi → ghi lại tại sao
```

- Không ghi tên/MSSV thật (dùng mã M01–M06). Không đưa dữ liệu thô/bí mật.

## 3. Cách báo cáo kiểm thử (test report)

- Chạy lại bước (re-run) với **cùng seed + cùng canonical CSV** → số phải khớp.
- Ghi trong `results/<mã-nhiệm-vụ>.md`: tham số, seed, phiên bản thư viện, đường dẫn
  kết quả, ngày chạy.
- Nếu có test (`tests/`) → chạy `pytest` và **báo kết quả pass/fail cụ thể** (bảo không
  "đã test rồi" chung chung).
- Chỉ báo "đạt" khi mọi chỉ tiêu trong tiêu chí nghiệm thu (README workspace) đúng.

## 4. Những giả định cần ghi lại

- Mọi "thông số tự chọn" (ngưỡng, K, loại F-score, cách xử lý NaN) phải **ghi rõ + lý do**.
- Giả định về dữ liệu (vd "cân bằng label", "không thiếu") → xác nhận thực tế trước khi
  viết trong báo cáo (M02-T1/M03-T2).
- "Đang chạy Colab / runtime tạm thời" → không coi kết quả là đã lưu cho đến khi commit.
- Ghi giả định vào `results/<mã-nhiệm-vụ>.md` (mục *Assumptions*), để reviewer đối chiếu.

## 5. Cách yêu cầu review

1. Chuyển hạng mục sang `Review` trong `TASK_BOARD.md` (M01 cập nhật).
2. Xác định **người review** (cột "Người review" trong `TASK_ASSIGNMENTS.md`).
3. Gửi (qua thông báo nhóm / comment): **mã hạng mục + link/head đường dẫn file đầu ra
   + 5 dòng mô tả (mục §2) + test report (mục §3)**.
4. Chờ reviewer **xác nhận đạt tiêu chí** → mới `Done`. Nếu bị trả lại → ghi rõ điểm sửa,
   sửa rồi lại `Review`.

## 6. Cách xử lý khi đầu vào chưa sẵn sàng

- **Không tự bịa / không tự tạo đầu vào thay người khác.**
- Trong `TASK_BOARD.md`, đặt hạng mục ở **`Blocked`** + ghi rõ trong cột "Ghi chú":
  "Blocked — chờ <mã-nhiệm-vụ-của-ai> (lý do: ...)".
- Thông báo **M01 (điều phối)** để M01 rà soát phụ thuộc & gỡ block đúng lúc.
- Nếu block kéo dài (>1 mốc) → nêu trong điểm nhóm để điều phối lại phân công.

## 7. Chấm bàn giao (đúng = Done)

- [ ] Đầu ra đủ (file + nơi lưu + tham số).
- [ ] Mô tả thay đổi (5 dòng) rõ, đúng mã, không tên/MSSV thật.
- [ ] Test report: re-run khớp, có kết quả cụ thể (không "đã chạy").
- [ ] Giả định đã ghi.
- [ ] Người review đã ký (reviewer theo bảng phân công).
- [ ] `TASK_BOARD.md` cập nhật đúng trạng thái.
