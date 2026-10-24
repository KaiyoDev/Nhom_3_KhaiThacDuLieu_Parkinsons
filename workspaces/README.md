# workspaces/ — Work-order cho 6 thành viên

> Mỗi thư mục `member-XX/` là **lệnh làm việc (work-order)** cụ thể cho một thành viên:
> đúng notebook, đúng bước/cell, đúng đầu vào/ra, phụ thuộc, tiêu chí, checklist, reviewer,
> và cách báo cáo khi bị chặn (Blocked). Đây là hướng dẫn **cụ thể nhất** — đọc kỹ trước khi nhận việc.

## Bản đồ notebook ↔ thành viên (trùng với `TASK_ASSIGNMENTS.md`)

| Notebook | Thành viên làm | Nhiệm vụ |
|----------|----------------|----------|
| `notebooks/01_data_exploration.ipynb` | **M02 + M03** | M02: cấu trúc/dtype/vấn đề · M03: thống kê + chất lượng |
| `notebooks/02_preprocessing_pca.ipynb` | **M04** | tiền xử lý + PCA + scatter |
| `notebooks/03_classification.ipynb` | **M05** | 10-fold CV + 3 mô hình + F-score |
| `notebooks/04_clustering.ipynb` | **M06** | K-Means + DBSCAN + ARI |
| `notebooks/05_integration_report.ipynb` | **M06 (chủ) + M01 (gate)** | tổng hợp + nhất quán + PDF |
| (không notebook) | **M01** | chuẩn bị dữ liệu (canonical CSV) + điều phối + gate |

## MẪU "GIAO TASK" (work-order) — áp dụng cho mọi `member-XX/`

Mỗi work-order bắt buộc có đủ 11 mục sau (để không thiếu bước, không mơ hồ):

```text
1. Thông tin          : mã, tên/MSSV [CHƯA CẬP NHẬT], vai trò, trạng thái (Todo)
2. Làm ở đâu         : notebook + phần/cell cụ thể (hoặc file trong data/ nếu không phải notebook)
3. Nhiệm vụ giao     : bảng [mã | việc | nơi làm | đầu vào | đầu ra | tiêu chí | reviewer | chặn bởi | unblock ai]
4. Thứ tự thực hiện  : từng bước "việc cụ thể → cell/đoạn cần làm → dừng/Blocked nếu thiếu gì"
5. Đầu vào nhận      : file + ai cung cấp + điều kiện (phụ thuộc phải = Done/Review)
6. Đầu ra bàn giao   : file + đường dẫn + nội dung phải có (không bịa)
7. Tiêu chí nghiệm thu: đo được (số dòng/cột đúng, có seed, CV đúng k, F-score/ARI từ kết quả thật ...)
8. Checklist tự kiểm : trước khi chuyển trạng thái Review
9. Người review      : ai + review cái gì
10. Bàn giao & Blocked: theo HANDOFF.md (mô tả 5 dòng + test-report + Blocked nếu thiếu đầu vào)
11. Trạng thái       : Todo (ban đầu)
```

## Quy tắc chung (tất cả thành viên)

- **Chỉ làm phần được giao**; đầu vào phải **xác nhận** trước khi bắt đầu.
- **Một canonical CSV duy nhất** (`data/processed/parkinsons_v1.csv`) làm đầu vào — không ai
  tạo bản CSV riêng (xem `data/README.md`).
- **Không bịa** kết quả/số liệu/biểu đồ. Mọi số chỉ lấy từ **chạy thật**.
- **Không hardcode** đường dẫn máy cá nhân (chạy từ gốc project / Colab).
- Thiếu đầu vào / phụ thuộc chưa xong → **`Blocked`** trong `TASK_BOARD.md` + ghi rõ thiếu gì, ai
  cung cấp, thông báo M01 (xem `HANDOFF.md` mục 6).
- Ghi kết quả vào `results/`, tổng hợp vào `reports/`, code vào `src/` (nếu tách module).
- `git`/commit/PR ở giai đoạn sau (xem `docs/GITHUB_GUIDE.md`) — hiện chưa commit.
