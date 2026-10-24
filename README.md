# Khai phá Dữ liệu — Dataset Parkinson (Nhóm 3)

> **Giai đoạn hiện tại: SETUP + NOTEBOOK SKELETONS** — đã có môi trường làm việc,
> dataset (đã commit) và **5 notebook khung** cho 6 thành viên triển khai phân tích.
> Đây là kho (repo) dùng để quản lý dự án nhóm môn *Khai phá dữ liệu* trên dataset
> **Oxford Parkinson's Disease Detection Dataset**.

---

## 1. Đề tài

Xây dựng quy trình khai phá dữ liệu trên tập dữ liệu giọng nói (voice) của bệnh nhân
Parkinson: từ chuẩn bị dữ liệu, khám phá, kiểm tra chất lượng, tiền xử lý (PCA),
đến phân lớp (classification + F-score) và phân cụm (clustering + ARI), cuối cùng
tổng hợp kết quả và báo cáo.

## 2. Mục tiêu

- Thiết lập không gian làm việc **an toàn, nhất quán, tái tạo được** cho 6 thành viên.
- Mỗi người nhận việc **độc lập** từ các workspace sẵn có (xem `workspaces/`).
- Thống nhất **một nguồn dữ liệu xử lý duy nhất** (canonical processed CSV) để tránh
  tình trạng mỗi người tạo ra các bản CSV khác nhau (xem `DATA_DICTIONARY.md`).
- Đã tạo **5 notebook khung** (skeleton, chưa có code phân tích / kết quả) để thành viên
  triển khai từng bước; mô hình và kết quả thật sẽ có ở giai đoạn làm việc (xem `notebooks/`).

## 3. Dữ liệu

- File dataset gốc: `data/raw/D07 - parkinsons.data.xlsx` (nằm ở `data/raw/`, **đã commit** —
  dataset UCI công khai; có exception riêng trong `.gitignore`, mọi xlsx khác vẫn bị ignore).
  - Sheet `"parkinsons.data"`: **195 dòng dữ liệu, 24 cột** (đã kiểm tra local).
  - Cột nhãn: `status` (`0` = khỏe mạnh, `1` = Parkinson).
  - Cột `name` (tên chủ thể + số bản ghi) được **loại bỏ trước khi phân tích**
    (theo ghi chú trong sheet `"Descriptipion"` của dataset).
  - Sheet `"Descriptipion"`: mô tả UCI + thông tin trích dẫn (citation).
- Chi tiết các thuộc tính: xem [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md).
- Dữ liệu thô trong `data/interim`, `data/processed` **không commit** (chỉ canonical CSV
  nếu nhóm thống nhất chia sẻ). Dataset gốc (xlsx UCI) **đã commit** cho tiện dùng.
  Quy ước xem [`data/README.md`](data/README.md).

## 4. Cấu trúc project

```text
Nhom_3_KhaiThacDuLieu_Parkinsons/
├── README.md              # file này
├── TEAM.md                # danh sách 6 thành viên (tên/MSSV để trống)
├── TASK_ASSIGNMENTS.md    # phân rã nhiệm vụ + phụ thuộc + người review
├── TASK_BOARD.md          # bảng trạng thái công việc (ban đầu: Todo)
├── PROJECT_WORKFLOW.md    # luồng tổng thể: chuẩn bị dữ liệu → báo cáo
├── HANDOFF.md             # quy trình bàn giao giữa các thành viên
├── CONTRIBUTING.md        # quy ước git/commit/review (hướng dẫn giai đoạn sau)
├── DATA_DICTIONARY.md     # bảng mô tả thuộc tính (từ thông tin đã xác minh)
├── requirements.txt       # phụ thuộc (không cài ở giai đoạn setup)
├── .gitignore             # loại dataset gốc, môi trường ảo, cache
├── data/                  # raw (dataset gốc, đã commit) / interim / processed (chỉ .gitkeep)
├── workspaces/            # 6 work-order thành viên (member-01..06) + mẫu giao task
├── notebooks/             # 5 notebook khung (skeleton): 01–05
├── src/                   # sẽ chứa module mã hóa ở giai đoạn sau (hiện trống)
├── tests/                 # sẽ chứa kiểm thử (hiện trống)
├── results/               # sẽ chứa kết quả thực nghiệm (hiện trống)
├── reports/               # sẽ chứa báo cáo tổng hợp (hiện trống)
└── docs/                  # hướng dẫn Colab / GitHub / Troubleshooting / Reproducibility
```

## 5. Cách bắt đầu

1. **Đọc** [`TEAM.md`](TEAM.md) để xem mã thành viên và vai trò dự kiến của bạn.
2. **Mở** `workspaces/member-XX/README.md` (XX = mã của bạn) để xem nhiệm vụ, đầu vào/ra và checklist.
3. **Đọc** [`TASK_ASSIGNMENTS.md`](TASK_ASSIGNMENTS.md) để hiểu phụ thuộc và người review.
4. **Xác nhận đầu vào** trước khi bắt đầu (nếu thiếu phụ thuộc → đánh dấu `Blocked` trong
   [`TASK_BOARD.md`](TASK_BOARD.md)).
5. Quy trình phối hợp chung xem [`PROJECT_WORKFLOW.md`](PROJECT_WORKFLOW.md) và
   [`HANDOFF.md`](HANDOFF.md).

> **Git:** repo đã có các commit trên GitHub (workspace + dataset + notebook skeleton +
> work-order). Khi triển khai phần phân tích, làm theo [`docs/GITHUB_GUIDE.md`](docs/GITHUB_GUIDE.md)
> (tạo nhánh → PR → review). Hướng dẫn Colab xem [`docs/COLAB_GUIDE.md`](docs/COLAB_GUIDE.md).

## 6. Trạng thái hiện tại

- **Setup: hoàn tất & đã commit/push.** Môi trường + dataset + tài liệu quản lý + work-order.
- **Notebook: đã tạo 5 khung** (skeleton, chưa có code phân tích / kết quả).
- **Progress: chưa bắt đầu.** Mọi nhiệm vụ phân tích ở `Todo` (xem `TASK_BOARD.md`),
  chờ M01 tạo canonical CSV (M01-T2) để mở khoá.
- Tên/MSSV thành viên: **chưa cập nhật** — chờ thông tin chính thức từ nhóm.

## 7. Nguyên tắc an toàn

- Dữ liệu **chưa được phép chia sẻ / bí mật** không đưa vào Git. (Dataset Parkinson là
  UCI công khai nên **đã được commit** cho tiện dùng; mọi xlsx khác vẫn bị ignore.)
- Không chứa token, mật khẩu, API key.
- Không ghi tên hoặc MSSV khi chưa được cung cấp (đánh dấu `[CHƯA CẬP NHẬT]`).
