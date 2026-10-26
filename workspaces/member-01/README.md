# M01 — Điều phối + Chuẩn bị dữ liệu + Thống nhất đầu vào (Work-order)

## 1. Thông tin
| | |
|---|---|
| Mã | `M01` |
| Tên | Đặng Hoàng Ân |
| MSSV | `080206014982` |
| Vai trò | Điều phối · chuẩn bị dữ liệu · thống nhất đầu vào · gate nhất quán |
| Trạng thái | `Todo` |

## 2. Bạn làm ở đâu
- **Không phải notebook phân tích.** Công việc của M01 nằm trong `data/` (manifest, canonical CSV,
  schema), `TASK_BOARD.md` (điều phối), và **gate nhất quán** trên `notebooks/05_integration_report.ipynb`.
- M01 là **người mở khoá** cho cả nhóm: canonical CSV chưa có → mọi notebook (01–05) đứng `Blocked`.

## 3. Nhiệm vụ giao (theo `TASK_ASSIGNMENTS.md`)
| Mã | Việc | Nơi làm | Đầu vào | Đầu ra | Tiêu chí | Reviewer | Chặn bởi | Unblock |
|----|------|---------|---------|--------|----------|----------|----------|---------|
| M01-T1 | Manifest dataset | `data/raw/manifest.md` | `data/raw/D07 - parkinsons.data.xlsx` (đã có, đã commit) | `data/raw/manifest.md` | hash/size đúng thực tế | M06 | — | M01-T2 |
| M01-T2 | Canonical CSV + schema | `data/processed/` | raw xlsx + `DATA_DICTIONARY.md` | `parkinsons_v1.csv` + `schema_v1.md` | 23 cột (22 feature+status), ~195 dòng, không `name`, 1 bản duy nhất | S-T1 + M03 | M01-T1 | toàn nhóm (S-T1) |
| M01-T3 | Gate đầu vào | `TASK_BOARD.md` + thông báo | M01-T2 (đã xong) | cập nhật board + thông báo | S-T1 đã xác nhận | M03 | M01-T2 | M02/M03/M04 chạy |
| M01-T4 | Gate nhất quán (cuối) | notebook 05 + `reports/` | kết quả M05-T3, M06-T2, M06-T3 | ký nhận nhất quán | cùng CSV/metric/quy ước | M06 | M05-T3, M06-T2 | S-T2 / báo cáo |

## 4. Thứ tự thực hiện (cụ thể)
1. **Xác nhận dataset** (`data/raw/D07 - parkinsons.data.xlsx` đã có, đã commit). Kiểm tra SHA-256
   (đúng `d5d96457…`). → **M01-T1**: viết `data/raw/manifest.md` (tên file, kích thước, hash,
   nguồn UCI Oxford Parkinson's, ngày).
2. **Tạo canonical CSV** → **M01-T2**. Gợi ý thao tác (sinh viên tự chạy, không chạy sẵn ở đây):
   ```python
   import pandas as pd
   # cần openpyxl (đã trong requirements.txt) để đọc .xlsx
   df = pd.read_excel("data/raw/D07 - parkinsons.data.xlsx", sheet_name="parkinsons.data")
   df = df.drop(columns=["name"])            # DROP 'name' (theo DATA_DICTIONARY + ghi chú dataset)
   df.to_csv("data/processed/parkinsons_v1.csv", index=False)
   ```
   - Kèm `data/processed/schema_v1.md`: liệt kê **22 feature + `status`**, dtype từng cột,
     **số NaN** (thường 0), cách xử lý (báo "giữ nguyên / chưa impute" nếu vậy).
3. **Mở gate đầu vào** → **M01-T3**: thông báo nhóm (S-T1) đọc `schema_v1.md` + xác nhận canonical CSV.
   Mọi người **mới** bắt đầu notebook 01. Cập nhật `TASK_BOARD.md`.
4. **Giữa chừng**: giữ "1 đầu vào duy nhất". Nếu ai cần đổi schema → M01 duyệt + cập nhật
   `schema_v1.md` (changelog) + `data/README.md`.
5. **Gate nhất quán cuối** → **M01-T4**: khi notebook 03/04 có kết quả, M01 (cùng M06, S-T2)
   kiểm tra tất cả dùng **cùng** canonical CSV v1, cùng quy ước (F-score macro/weighted, seed,
   k) → ký trước khi hoàn thiện `reports/summary.md` (notebook 05).

## 5. Đầu vào cần nhận
- Dataset (đã có ở `data/raw/`), `DATA_DICTIONARY.md`, `docs/REPRODUCIBILITY.md` (quy ước seed).
- Kết quả M05-T3 + M06-T2 (cho M01-T4).

## 6. Đầu ra phải bàn giao
- `data/raw/manifest.md` · `data/processed/parkinsons_v1.csv` · `data/processed/schema_v1.md`.
- Cập nhật `TASK_BOARD.md` (gate M01-T3, M01-T4) + ký nhất quán S-T2.

## 7. Tiêu chí nghiệm thu (đo được)
- CSV **đúng 23 cột** (22 feature + `status`), **không** cột `name`, ~195 dòng.
- Schema ghi đủ dtype + NaN + cách xử lý; **1 bản CSV duy nhất** (không ai tạo CSV riêng).
- Gate M01-T3: S-T1 đã được xác nhận (toàn nhóm đồng ý dùng canonical CSV).
- Gate M01-T4: các phần không mâu thuẫn (cùng CSV/metric/quy ước).

## 8. Checklist tự kiểm (trước khi chuyển Review)
- [ ] `manifest.md` có hash + size đúng (khớp file thật).
- [ ] `parkinsons_v1.csv`: 23 cột, không `name`, đã kiểm tra `df.shape`.
- [ ] `schema_v1.md`: 22 feature + status, dtype, NaN, cách xử lý.
- [ ] Đã thông báo S-T1 + cập nhật `TASK_BOARD.md`.
- [ ] (Cuối) Đã ký nhất quán M01-T4/S-T2 (cùng M06).
- [ ] Không commit/xoá/xử lý sai dataset; không tạo CSV riêng cho ai.

## 9. Người review
M01-T1 → **M06** · M01-T2 → **S-T1 + M03** · M01-T3 → **M03** · M01-T4 → **M06** (chủ tổng hợp).

## 10. Bàn giao & Blocked
- Theo `HANDOFF.md`: mô tả 5 dòng + test-report (đã chạy tạo CSV, `df.shape` = ...).
- M01-T2 **không bị Block** (dataset đã có). Nếu thiếu `openpyxl` → `pip install openpyxl`
  (đã khai báo trong `requirements.txt`) rồi làm tiếp.

## 11. Trạng thái
`Todo` — chờ M01 nhận việc; đây là bước mở khoá cho cả nhóm.
