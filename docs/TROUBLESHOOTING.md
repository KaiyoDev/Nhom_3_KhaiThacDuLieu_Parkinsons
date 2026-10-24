# TROUBLESHOOTING — Lỗi thường gặp & cách xử lý

> Mỗi mục: **triệu chứng → nguyên nhân khả dĩ → cách xử lý.** Khi không chắc,
> đọc lại `docs/` liên quan trước khi thử bừa.

## Dữ liệu / dataset

### `pandas.read_excel` báo thiếu `openpyxl`
- **Nguyên nhân:** Python local không có `openpyxl` (ở local hiện tại đã thiếu).
- **Xử lý:** `pip install openpyxl` (đã khai báo trong `requirements.txt`).
- **Thuế thay thế:** chuyển canonical CSV (`data/processed/parkinsons_v1.csv`) và dùng
  `pandas.read_csv(...)` (không cần `openpyxl`).

### "Không thấy dataset trong repo" (clone về mà thiếu `D07 - parkinsons.data.xlsx`)
- **Nguyên nhân:** file xlsx bị `.gitignore` (đúng ý — không đưa dataset gốc vào Git).
- **Xử lý:** lấy dataset từ nguồn gốc (M01 / người quản lý) vào `data/raw/`, không
  kỳ vọng nó nằm trong Git. Canonical CSV (nếu nhóm thống nhất chia sẻ) nằm trong
  `data/processed/`.

### File xlsx có 2 sheet, đọc sai sheet
- **Nguyên nhân:** sheet data là `"parkinsons.data"`, sheet mô tả là `"Descriptipion"`.
- **Xử lý:** `pd.read_excel(file, sheet_name="parkinsons.data")`.

### Cột `name` lẫn vào feature
- **Nguyên nhân:** quên drop cột định danh (ghi chú Việt trong dataset nói rõ).
- **Xử lý:** canonical CSV đã drop `name`; nếu tự sinh → `df.drop(columns=["name"])`.

## Git

### `git push` lỗi 403 / "permission denied"
- **Nguyên nhân:** thành viên chưa có quyền **Write** (xem `docs/GITHUB_GUIDE.md` §0).
- **Xử lý:** báo M01 / người quản lý mời với vai trò `Write`; trước đó chỉ làm local.

### `git pull` / merge bị conflict
- **Xử lý:** theo `docs/GITHUB_GUIDE.md` §8 — pull/merge `main` vào nhánh, giải conflict
  từng file, **chạy lại kiểm tra**, mới commit.

### Lẫn file bí mật / dataset vào commit
- **Xử lý:** kiểm tra `git status` + `git diff --staged`; chắc chắn `.gitignore` phủ
  (`*.xlsx`, `.env`, `data/*`). Nếu lỡ commit → không "xóa" bằng rewrite bừa, báo nhóm.

## Môi trường / Colab

### Colab "văng" giữa chừng, mất kết quả
- **Nguyên nhân:** runtime Colab tạm thời; kết quả trong `/content` mất khi tắt.
- **Xử lý:** chạy **TẢI XUỐNG** kết quả ngay khi có; sau đó commit (xem `docs/COLAB_GUIDE.md`).

### 6 người chạy Colab cho kết quả khác nhau
- **Nguyên nhân:** runtime độc lập + seed/phiên bản/dữ liệu không thống nhất.
- **Xử lý:** cố định seed + pin phiên bản + dùng **cùng** canonical CSV (xem
  `docs/REPRODUCIBILITY.md` + `data/README.md`).

## Kết quả / chỉ báo

### Không rõ dùng F-score hay accuracy
- **Xử lý:** nhiệm vụ dùng **F-score** (macro/weighted) — ghi rõ loại trong báo cáo
  (xem `workspaces/member-05/README.md`).

### ARI âm / bất thường
- **Nguyên nhân:** so cluster với label sai, hoặc K chọn bừa.
- **Xử lý:** ARI tính trên **label thật `status`** + nhiều giá trị K (xem
  `workspaces/member-06/README.md`), kiểm tra lại code tính ARI.

## Khi không xử lý được

- Ghi lại: **triệu chứng + bước đã thử + màn hình lỗi** vào `TASK_BOARD.md` (hạng mục
  `Blocked`, cột "Ghi chú") → nhờ M01 (điều phối) phân công / hỗ trợ.
