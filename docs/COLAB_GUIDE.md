# COLAB_GUIDE — Dùng Google Colab (Nhóm 3 · Parkinson)

> **Giai đoạn sau** — áp dụng khi notebook được tạo (không tạo `.ipynb` ở setup).
> Mục đích: hướng dẫn cách chạy phân tích trên Colab mà **không làm mất đồng nhất**
> với repo GitHub.

## 1. Hiểu đặc tính runtime của Colab (quan trọng)

- **Mỗi thành viên một runtime độc lập.** Máy Colab của M01 không thấy dữ liệu /
  thư viện / file của M02. Chạy riêng = kết quả có thể lệch nếu không thống nhất
  (seed, phiên bản, dữ liệu).
- **Thay đổi trên Colab KHÔNG tự động đồng bộ về GitHub.** Khi chạy Colab, notebook
  nằm trong `/content` (tạm thời, mất khi runtime tắt). Muốn lưu lại phải:
  1. *Tải xuống* notebook + kết quả (figure/CSV), **và**
  2. *Commit + push* vào repo (sau khi giai đoạn Git mở) để đồng bộ.
- **Dataset xlsx không được commit** (`.gitignore`) → trên Colab phải **tự upload**
  `data/processed/parkinsons_v1.csv` (hoặc xlsx) bằng `google.colab.files.upload()`
  hoặc `files/` panel, **không** kỳ vọng nó có sẵn trong repo.

## 2. Quy trình khuyến nghị

1. **Mở notebook trong Colab** (File → New notebook hoặc upload `.ipynb` từ repo).
2. **Kết nối dữ liệu** (chọn một, ghi rõ trong notebook):
   - Upload canonical CSV: `files.upload()` → lưu vào `data/processed/parkinsons_v1.csv`.
   - Hoặc (nếu canonical CSV đã được nhóm thống nhất chia sẻ qua `git add -f`) đọc từ repo.
3. **Cài/kiểm tra thư viện**: `!pip install -r requirements.txt` (Colab đã có sẵn phần lớn;
   chỉ cần thêm `openpyxl` nếu đọc xlsx).
4. **Cố định seed + phiên bản** theo `docs/REPRODUCIBILITY.md` (để kết quả của 6 người
   so sánh được).
5. **Chạy** → lưu kết quả (figure + CSV/JSON) → **TẢI XUỐNG**.
6. **Commit + push** notebook + kết quả (khi giai đoạn Git mở, xem `docs/GITHUB_GUIDE.md`).

## 3. Quy ước để không lệch giữa các thành viên

- **Một canonical CSV** (xem `data/README.md`) — mọi notebook nạp cùng file này.
- Ghi rõ ở đầu mỗi notebook: runtime, phiên bản thư viện, seed, phiên bản dữ liệu.
- Kết quả thật → `results/`; chỉ push file kết quả đã kiểm chứng (không push dữ liệu thô).
- Nếu runtime Colab bị "văng" giữa chừng → tải lại kết quả đã chạy, không chạy lại bừa
  (tránh sinh file trùng/khác nhau).

## 4. Cẩn thận

- Không upload/commit file xlsx hoặc dữ liệu chưa được phép chia sẻ.
- Không lưu bí mật (token/API key) trong notebook — xem `.gitignore` + nguyên tắc an toàn.
- Kết quả "trên màn hình Colab" **không coi là đã lưu** cho đến khi commit + push.
