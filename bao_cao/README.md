# BÁO CÁO BÀI TẬP LỚN — NHÓM 3 (Khai phá dữ liệu / Parkinson)

Thư mục chứa báo cáo hoàn chỉnh cho bài tập lớn, dựng trên template
[UTH LaTeX Template (Tiếng Việt)](https://github.com/vanphat111/uth_latex_template_vi)
(MIT license, tác giả `vanphat111`).

## Sản phẩm

| File | Mô tả |
|------|-------|
| `dist/BaoCao_BaiTapLon_Nhom3.pdf` | Báo cáo PDF đã biên dịch (32 trang, tiếng Việt) |
| `dist/BaoCao_BaiTapLon_Nhom3.docx` | Bản Word chỉnh sửa được (cùng nội dung, có mục lục Field) |
| `dist/BaoCao_Notebook05_Parkinson.pdf` | Phụ lục: notebook tổng hợp `05_integration_report.ipynb` xuất PDF |

Mọi số liệu trong báo cáo đều tái lập từ `data/processed/parkinsons_v1.csv`
(SHA-256 `55e2fed6…8153`) với seed `42`.

## Cách dựng lại

Yêu cầu: MiKTeX/TeX Live (pdflatex, bibtex) và Python với `python-docx`
(`pip install python-docx`).

```bash
make pdf     # dịch LaTeX -> dist/BaoCao_BaiTapLon_Nhom3.pdf
make docx    # dựng Word từ scripts/build_docx.py
make notebook  # (tùy chọn) xuất PDF notebook 05; cần pandoc
```

Hoặc gọi trực tiếp:

```bash
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
cp main.pdf dist/BaoCao_BaiTapLon_Nhom3.pdf
python scripts/build_docx.py
```

## Cấu trúc

- `preamble.tex` — **chỉnh thông tin đề tài tại đây** (trường/viện, GVHD, mã lớp,
  học kỳ, ngày địa điểm). Trang bìa đồng bộ theo các macro này.
- `frontmatter/` — bìa, cam đoan, cảm ơn, danh mục từ viết tắt.
- `chapters/` — 5 chương nội dung.
- `appendices/` — Phụ lục A (kho lưu trữ, cấu trúc, tái lập, nhóm) và B (bảng
  thống kê + IQR chi tiết).
- `figures/` — hình vẽ dùng trong báo cáo (sao chép từ `docs/images/` và
  `results/figures/`; `pipeline_diagram.png` do `scripts/make_pipeline_figure.py` vẽ).
- `refs.bib` — tài liệu tham khảo (chuẩn IEEE).
- `ieeetr-hyphen.bst` — biến thể `ieeetr` giữ dấu gạch trùng (`-`) cho khoảng trang.
- `scripts/build_docx.py` — dựng file `.docx`.
- `scripts/make_pipeline_figure.py` — vẽ sơ đồ quy trình.

## Thành viên

STT · Họ tên · MSSV · nhiệm vụ chính được liệt kê trên trang bìa và Bảng 1.1;
danh sách đầy đủ cùng tài khoản GitHub ở Phụ lục A.
