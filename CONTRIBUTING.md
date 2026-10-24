# CONTRIBUTING — Quy định đóng góp (Nhóm 3 · Parkinson)

> ⚠️ **Đây là hướng dẫn, không phải thao tác thực thi.** Ở giai đoạn setup hiện tại:
> **không commit, không push, không PR, không merge, không chạy lệnh git ghi.**
> Chỉ dùng file này khi nhóm mở giai đoạn Git (xem `docs/GITHUB_GUIDE.md`).

## 1. Tên nhánh (branch)

- Quy ước: `task/<mã-member>-<mã-task>-<ten-ngan>` — chữ thường, dấu gạch nối.
  - Ví dụ: `task/m01-t2-canonical-csv`, `task/m04-t2-pca`, `task/m06-t3-summary`.
- Mỗi nhánh **một nhiệm vụ** (một mã trong `TASK_ASSIGNMENTS.md`), không trộn nhiều việc.
- Nhánh `main` là nhánh "chính thức" — chỉ nhận thay đổi qua PR đã review.

## 2. Commit message (Conventional Commits)

```text
<type>(<scope>): <mô tả>
```

- `type` (đầy đủ): `feat` · `fix` · `docs` · `style` · `refactor` · `test` ·
  `chore` · `perf` · `build` · `ci`.
- `scope` (đề xuất): mã nhiệm vụ (vd `m01-t2`) hoặc tên module (vd `pca`, `data`).
- **Mô tả**: câu mệnh lệnh, chữ thường, **không** chấm cuối.
- Breaking change: thêm `!` ngay sau `type`/`scope`.
- **Không** ghi tên tác giả, **không** `Co-authored-by` (trừ khi được yêu cầu).

Ví dụ:

```text
docs(m02-t1): bổ sung dtype + missing vào DATA_DICTIONARY
feat(m04-t2): thêm module PCA + lưu figure
chore(m01-t2): thêm canonical CSV v1 + schema
```

## 3. Phạm vi chỉnh sửa (rất quan trọng)

- Mỗi thành viên **chỉ đụng phần được giao** (xem `workspaces/member-XX/README.md`).
- **Không ghi đè / sửa file của người khác.** Cần thay đổi file chung
  (`DATA_DICTIONARY.md`, `docs/REPRODUCIBILITY.md`, canonical CSV...) → ghi rõ +
  nhờ M01 (điều phối) duyệt trước.
- **Dữ liệu:** không commit xlsx / CSV thô / figure nặng / bí mật — `.gitignore` đã phủ.
- **Canonical CSV** do M01 duy nhất sinh (M01-T2); các thành viên khác **không** tạo bản
  CSV riêng (nguyên tắc "một đầu vào duy nhất", xem `data/README.md`).

## 4. Quy trình review

- Mỗi nhiệm vụ có **người review** (cột "Người review" trong `TASK_ASSIGNMENTS.md`).
- Flow: `In Progress → Review → (reviewer xác nhận) → Done`. **Không tự đánh `Done`.**
- Trước khi mở PR: hoàn thành **checklist tự kiểm tra** trong workspace của mình +
  tự review `git diff` (loại debug, file tạm, bí mật).
- PR đủ 3 phần: `## Summary` · `## Test Plan` · `## Risk` (xem `docs/GITHUB_GUIDE.md` §7).
- Reviewer **đọc diff + chạy kiểm tra** (nếu có); đạt tiêu chí nghiệm thu mới merge.
- **Coder không tự merge phần quan trọng của chính mình** — cần reviewer ký.

## 5. Xử lý conflict

```bash
git fetch origin
git checkout main && git pull origin main     # cập nhật main
git checkout task/m04-t2-pca
git merge main                                # hợp main vào nhánh task
# Giải conflict: mở file có "<<<<<<<", giữ đúng thứ cần, loại "đầu thừa"
git add <file>
git commit -m "chore(m04-t2): giải conflict sau khi merge main"
```

- Nguyên tắc conflict: **ưu tiên nội dung đúng + mới nhất theo quy ước nhóm**;
  nếu không chắc ai đúng → giữ lại **hết** và để comment cho reviewer quyết định.
- Sau khi giải conflict → **chạy lại kiểm tra** trước khi commit (không "gỡ mù").
- Không `git push --force` lên `main`.

## 6. Nguyên tắc chung

- Nhỏ và rõ: **một commit một mục đích** (không trộn docs + code + config vào 1 commit).
- Không code chết, không `print`/`console.log` debug, không `TODO`/`FIXME` bỏ lại.
- Ghi chú giải thích khi phải "làm khác quy ước" (vd đổi seed, đổi ngưỡng PCA).
- Mọi thay đổi file chung → cập nhật `TASK_BOARD.md` (trạng thái) và thông báo M01.

## 7. Khi chưa mở Git (giai đoạn hiện tại)

- Chỉ làm việc **local** trên file (tạo/sửa tài liệu, workspace, hướng dẫn).
- **Không** chạy `git add / commit / push / merge / PR`.
- Khi nào mở Git: làm theo `docs/GITHUB_GUIDE.md` (xác minh quyền ghi trước, xem §0).
