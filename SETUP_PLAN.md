# SETUP_PLAN — Setup workspace nhóm 6 người (Khai phá dữ liệu Parkinson)

> Kế hoạch thi công. Đọc kỹ trước khi approve. Sau khi approve, các bước
> **[POST-APPROVAL]** sẽ được thực thi (kể cả các file không phải markdown
> bị chặn ở chế độ plan hiện tại). Kế hoạch này *không* thay thế các tài liệu
> quản lý (những file đó sẽ được tạo ở các bước).

## 0. Đã xác minh (chỉ-đọc, không phân tích)

- **Repo local**: branch `main`, **chưa có commit nào**, remote =
  `https://github.com/KaiyoDev/Nhom_3_KhaiThacDuLieu_Parkinsons`.
- **File có sẵn (bảo toàn, KHÔNG sửa/xoá/ghi đè)**:
  `D07 - parkinsons.data.xlsx` (untracked, ~53 KB).
- **Dataset (đọc từ chính file, metadata-only)**:
  - 2 sheet: `"Descriptipion"` (mô tả UCI + ghi chú tiếng Việt) và `"parkinsons.data"`.
  - Sheet data: **195 dòng dữ liệu, 24 cột**. Cột nhãn `status` (`0`=khỏe, `1`=Parkinson);
    cột `name` **loại bỏ trước khi phân tích** (theo ghi chú trong sheet mô tả).
  - 24 cột đã xác minh: `name, MDVP:Fo(Hz), MDVP:Fhi(Hz), MDVP:Flo(Hz), MDVP:Jitter(%),
    MDVP:Jitter(Abs), MDVP:RAP, MDVP:PPQ, Jitter:DDP, MDVP:Shimmer, MDVP:Shimmer(dB),
    Shimmer:APQ3, Shimmer:APQ5, MDVP:APQ, Shimmer:DDA, NHR, HNR, status, RPDE, DFA,
    spread1, spread2, D2, PPE`.
- **Chưa có** `.gitignore`, không có ghi chú bài tập nào khác.

## 1. Phân công dự kiến (không đổi khi setup)

| Mã | Vai trò dự kiến |
|----|-----------------|
| M01 | Điều phối + chuẩn bị dữ liệu + thống nhất đầu vào |
| M02 | Khám phá cấu trúc & kiểu dữ liệu |
| M03 | Thống kê mô tả + kiểm tra chất lượng dữ liệu |
| M04 | Tiền xử lý + PCA + trực quan hóa |
| M05 | Phân lớp + cross-validation + F-score |
| M06 | Phân cụm + ARI + hỗ trợ tổng hợp kết quả |

## 2. Đã tạo (phạm vi markdown, được phép ở chế độ plan)

- `README.md` — giới thiệu đề tài, mục tiêu, cấu trúc, cách bắt đầu, trạng thái.
- `TEAM.md` — bảng 6 thành viên (tên/MSSV `[CHƯA CẬP NHẬT]`), vai trò, liên hệ trống.

## 3. [POST-APPROVAL] Các bước thi công

Mỗi bước = 1 nhóm file, tạo **mới** (không ghi đè). Bước B1 gồm các file
không-markdown bị chặn ở chế độ plan; B2–B7 là markdown.

- **B1 — File gốc không-markdown** (bị chặn ở plan mode, chạy sau approval):
  - `.gitignore` — loại dataset gốc (`D07 - parkinsons.data.xlsx`, `*.xlsx`), nội dung
    `data/*` (giữ `.gitkeep`), env ảo, `__pycache__`, `.ipynb_checkpoints`, bí mật, file OS.
    **Không** ignore `*.ipynb` (notebook là artifact cần commit sau này).
  - `requirements.txt` — numpy, pandas, scipy, scikit-learn, matplotlib, seaborn,
    openpyxl (đọc xlsx), jupyter (Colab có env riêng). Chỉ khai báo, **không cài**.
  - `.gitkeep`: `data/raw/.gitkeep`, `data/interim/.gitkeep`, `data/processed/.gitkeep`.

- **B2 — Quản lý task**: `TASK_ASSIGNMENTS.md` (nhiệm vụ có mã `Mxx-Tn`/`S-Tn`,
  đầu vào/ra, tiêu chí, phụ thuộc, người review; tích hợp kết quả **đồng M01+M06**),
  `TASK_BOARD.md` (5 trạng thái, **mọi mục = Todo**), `PROJECT_WORKFLOW.md`
  (luồng tổng thể, chưa triển khai phân tích).

- **B3 — Dữ liệu**: `DATA_DICTIONARY.md` (bảng 24 cột + ý nghĩa **từ sheet mô tả đã
  xác minh**, ghi rõ nguồn; đánh dấu các cột cần loại = `name`, cột nhãn = `status`),
  `data/README.md` (quy ước canonical CSV, cách nạp dữ liệu, an toàn dữ liệu).

- **B4 — 6 workspace**: `workspaces/README.md` + `workspaces/member-01..06/README.md`
  (mã, tên/MSSV `[CHƯA CẬP NHẬT]`, vai trò, nhiệm vụ, đầu vào/ra, tiêu chí, checklist,
  reviewer, trạng thái `Todo`).

- **B5 — Thư mục trống**: `notebooks/`, `src/`, `tests/`, `results/`, `reports/`
  → mỗi thư mục 1 `README.md` mô tả đích + quy định (không `.ipynb`, không code phân tích).

- **B6 — Hướng dẫn docs**: `docs/COLAB_GUIDE.md`, `docs/GITHUB_GUIDE.md`
  (ghi rõ = hướng dẫn giai đoạn sau; **không** thực hiện commit/push/PR/merge;
  xác minh quyền ghi trước khi push), `docs/TROUBLESHOOTING.md`,
  `docs/REPRODUCIBILITY.md`.

- **B7 — Nghiệm thu** (xem mục 4).

## 4. [POST-APPROVAL] Tiêu chí nghiệm thu (checklist)

- [x] Đúng cấu trúc thư mục theo spec (mục 3 của task).
- [x] Tất cả tài liệu có **nội dung thật**, không placeholder trống.
- [x] Đủ **6** workspace thành viên.
- [x] Bảng phân công (`TASK_ASSIGNMENTS.md`) + bảng trạng thái (`TASK_BOARD.md`) có đủ.
- [x] **Không** có file `.ipynb`.
- [x] **Không** có code phân tích / kết quả thực nghiệm giả.
- [x] `git status`: file mới **untracked**, **chưa commit**, **chưa push**, không PR/merge.
- [x] Dataset gốc không nằm trong Git (`.gitignore` phủ).
- [x] File có sẵn `D07 - parkinsons.data.xlsx` **không bị sửa/xoá/ghi đè**.
- [x] Báo cáo cuối bằng tiếng Việt (đường dẫn, file tạo, kiểm tra đã làm, thiếu sót,
      xác nhận chưa tạo notebook / chưa commit / chưa push).

## 5. Ranh giới an toàn (không đổi)

- Không notebook, không code phân tích, không chạy mô hình, không kết quả thực nghiệm.
- Không commit, không push, không PR/merge, không đổi visibility, không ghi đè file có sẵn.
- Không token/mật khẩu/API key; không ghi tên/MSSV giả (dùng `[CHƯA CẬP NHẬT]`).
