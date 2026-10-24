# workspaces/ — Workspace của 6 thành viên

> Mỗi thư mục `member-XX/` là **khu làm việc cá nhân** cho một thành viên.
> File `README.md` trong mỗi thư mục mô tả: mã, tên/MSSV, vai trò, nhiệm vụ,
> đầu vào/ra, tiêu chí hoàn thành, checklist, người review, trạng thái ban đầu.

## Chỉ mục

| Thư mục | Mã | Vai trò dự kiến |
|---------|----|-----------------|
| `member-01/` | M01 | Điều phối + chuẩn bị dữ liệu + thống nhất đầu vào |
| `member-02/` | M02 | Khám phá cấu trúc & kiểu dữ liệu |
| `member-03/` | M03 | Thống kê mô tả + kiểm tra chất lượng |
| `member-04/` | M04 | Tiền xử lý + PCA + trực quan hóa |
| `member-05/` | M05 | Phân lớp + cross-validation + F-score |
| `member-06/` | M06 | Phân cụm + ARI + hỗ trợ tổng hợp kết quả |

## Quy ước chung (tất cả thành viên)

- **Mã M01–M06** là định danh an toàn; không ghi tên/MSSV khi chưa được cung cấp
  (để `[CHƯA CẬP NHẬT]`).
- **Một canonical CSV duy nhất** làm đầu vào (xem `data/README.md`, `M01-T2` trong
  `TASK_ASSIGNMENTS.md`). Không ai tự tạo bản CSV riêng.
- Làm theo **checklist tự kiểm tra** trong README của mình trước khi chuyển trạng thái
  sang `Review` (xem `TASK_BOARD.md`).
- Trạng thái ban đầu của mọi nhiệm vụ: **`Todo`**.
- Chỉ chuyển `Review → Done` khi **người review** (ghi trong README) xác nhận đạt tiêu chí.
- Thiếu đầu vào / phụ thuộc chưa xong → đánh dấu **`Blocked`** + ghi rõ thiếu gì, ai cung cấp.

## Cấu trúc mỗi `member-XX/README.md` (nhất quán)

1. Mã thành viên · Tên & MSSV · Vai trò dự kiến.
2. Nhiệm vụ được giao (mã + tóm tắt).
3. Đầu vào cần nhận (từ nhiệm vụ nào, ai).
4. Đầu ra cần bàn giao (file/kết quả, để ở đâu).
5. Tiêu chí hoàn thành.
6. Checklist tự kiểm tra.
7. Người review dự kiến.
8. Trạng thái ban đầu (`Todo`).

> File README trong workspace chỉ là **trần nhà quy ước làm việc cá nhân**, không thay
> `TASK_ASSIGNMENTS.md` (nơi ghi phụ thuộc & người review chính thức).
