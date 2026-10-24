# results/ — Kết quả thực nghiệm (tạo ở giai đoạn sau)

> **Hiện tại: TRỐNG (chưa có kết quả ở giai đoạn setup).**
> Nơi lưu kết quả của từng bước: thống kê, PCA, phân lớp (F-score), phân cụm (ARI), figure.

## Quy ước đặt tên (dùng chung, tránh trùng/conflict)

- Mỗi thành viên viết kết quả vào file **mang mã nhiệm vụ** (vd `results/m03_quality_report.md`),
  không ghi đè file của người khác.
- Kết quả số: ưu tiên **CSV/JSON** (máy đọc được) để dễ tổng hợp.
- Figure: `results/figures/<mã-nhiệm-vụ>_<ten>.png`.

## Quy định khi tạo kết quả

- **Không bịa kết quả** — mọi số phải có thể tái tạo từ code + canonical CSV + seed
  (ghi rõ trong `docs/REPRODUCIBILITY.md`).
- Mỗi file kết quả ghi rõ: mã nhiệm vụ, ngày, tham số (k, seed, ngưỡng), nguồn dữ liệu
  (canonical CSV version).
- Kết quả **thô / dữ liệu** không commit; chỉ commit file kết quả đã kiểm chứng
  (JSON/CSV nhỏ, figure). Xem `.gitignore`.

## Ràng buộc setup

- **Chưa tạo bất kỳ kết quả nào ở giai đoạn này.** Thư mục chỉ giữ README.
