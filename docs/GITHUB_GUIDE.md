# GITHUB_GUIDE — Quy trình GitHub (Nhóm 3 · Parkinson)

> ⚠️ **Đây là hướng dẫn cho GIAI ĐOẠN SAU.** Ở giai đoạn setup hiện tại:
> **không commit, không push, không tạo Pull Request, không merge.**
> Chỉ dùng hướng dẫn này khi nhóm chính thức mở giai đoạn Git.

## 0. Trước khi bắt đầu: xác minh quyền truy cập (bắt buộc)

**Không giả định mọi thành viên đều có quyền ghi (write) vào repo.**
Repository: `https://github.com/KaiyoDev/Nhom_3_KhaiThacDuLieu_Parkinsons`

- Mỗi thành viên kiểm tra quyền: mở repo trên web, nếu thấy nút **`< Add file` / `Code`
  cho phép tạo branch** → có quyền ghi. Nếu chỉ **`Watch`** (read-only) → chưa đủ quyền.
- Người có quyền (M01 hoặc người quản lý repo) cần **mời các thành viên với vai trò
  `Write`** (Settings → Collaborators). Thành viên chưa đủ quyền → báo M01, **không** tự
  push (sẽ lỗi 403).
- **Không tự ý thay đổi visibility / quyền riêng tư của repo.**

## 1. Clone (làm 1 lần)

```bash
git clone https://github.com/KaiyoDev/Nhom_3_KhaiThacDuLieu_Parkinsons.git
cd Nhom_3_KhaiThacDuLieu_Parkinsons
```

## 2. Kiểm tra trạng thái

```bash
git status          # xem file thay đổi / chưa theo dõi
git log --oneline   # lịch sử commit (sau khi có commit)
```

## 3. Tạo nhánh theo nhiệm vụ

Đặt tên nhánh theo **mã nhiệm vụ** (xem `TASK_ASSIGNMENTS.md`):

```bash
git checkout -b task/m01-t2-canonical-csv
# hoặc task/m02-t1-exploration, task/m04-t2-pca, ...
```

Quy ước: `task/<mã-member>-<mã-task>-<ten-ngan>` (chữ thường, dấu gạch nối).

## 4. Chỉnh sửa file (chỉ phần được giao)

- Xem `CONTRIBUTING.md` về phạm vi chỉnh sửa (mỗi người chỉ đụng phần của mình).
- Không ghi đè / sửa file của thành viên khác.

## 5. Xem diff trước khi commit

```bash
git status
git diff                      # so với HEAD (chưa stage)
git diff --staged            # so với index (đã stage)
```

- **Tự review diff**: loại `console.log`/`print` debug, file tạm, bí mật, dữ liệu thô.
- Kiểm tra `.gitignore` có phủ đúng (dataset xlsx, env, cache).

## 6. Commit (CHỈ khi giai đoạn Git đã mở)

Theo **Conventional Commits** (xem `CONTRIBUTING.md`):

```bash
git add <file>                # add từng file, KHÔNG dùng `git add -A` bừa
git commit -m "feat(m01-t2): tạo canonical processed CSV"
# type: feat | fix | docs | chore | test | refactor
# Không ghi tên tác giả, không Co-authored-by (trừ khi yêu cầu).
```

## 7. Push nhánh + mở Pull Request

```bash
git push -u origin task/m01-t2-canonical-csv
```

- Trên web: **Create Pull Request** → nhánh task → `main`.
- Ghi PR theo 3 phần (xem `CONTRIBUTING.md`): `## Summary` · `## Test Plan` · `## Risk`.
- Chỉ mở PR khi nhiệm vụ đạt tiêu chí nghiệm thu (checklist trong workspace).

## 8. Review + xử lý conflict

- **Người review** (cột "Người review" trong `TASK_ASSIGNMENTS.md`) đọc diff, chạy test
  (nếu có), xác nhận đạt tiêu chí → **merge** (chỉ merge khi review xong).
- Conflict:

```bash
git fetch origin
git checkout main && git pull origin main    # cập nhật main
git checkout task/m01-t2-canonical-csv
git merge main                                # hoặc merge main vào nhánh
# giải conflict từng file, chạy lại kiểm tra
git add <file>
git commit
```

## 9. Cập nhật `main`

- `main` chỉ nhận thay đổi qua **PR đã được review + merge** (không push thẳng).
- Sau merge, nhánh task có thể bỏ (web UI hoặc `git branch -d ...`).

## 10. Mẹo an toàn

- Luôn `git pull --rebase` (hoặc merge) main trước khi mở PR để giảm conflict.
- Không `git push --force` lên `main`; force push nhánh cá nhân chỉ khi chắc chắn.
- Dữ liệu (xlsx, CSV thô, figure nặng) **không commit** — xem `.gitignore`.

## Trạng thái hiện tại (setup)

> **Chưa commit, chưa push, chưa PR, chưa merge.** Mọi file đang ở trạng thái untracked
> trên máy local (xem `git status`). Bỏ qua các bước §6–§10 cho đến khi nhóm mở
> giai đoạn Git.
