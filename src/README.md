# src/ — Mã nguồn tái sử dụng (Nhóm 3 · Parkinson)

> Module Python dùng chung cho pipeline. Không hardcode đường dẫn máy cá nhân;
> mọi module tìm gốc project qua `data/processed/parkinsons_v1.csv`.

## Hiện có

| Module | Vai trò | Dùng ở |
|--------|---------|--------|
| `preprocessing.py` | `find_root()`, `load_xy()`, `make_scaler()`, `standardize()` — nạp canonical CSV, tách `X`/`y`, chuẩn hoá `StandardScaler` | notebook 02, `pipeline.py` |
| `pipeline.py` | **Pipeline tổng hợp**: kiểm tra dữ liệu → PCA (2D + ngưỡng 90%) → phân lớp 3 mô hình (CV 10-fold) → ghi `results/pipeline_summary.json` | chạy độc lập, tái lập kết quả |
| `__init__.py` | Đánh dấu `src` là package | — |

## Chạy pipeline tổng hợp

```bash
python -m src.pipeline
```

Đầu ra: `results/pipeline_summary.json` (số liệu + seed + phiên bản thư viện + ngày chạy).

## Quy định

- **Một canonical CSV duy nhất** — mọi module nạp từ `data/processed/parkinsons_v1.csv`.
- Cấu hình (seed, k, ngưỡng) lấy từ `docs/REPRODUCIBILITY.md`; không hardcode bí mật.
- Code sạch, không để `print` debug; kết quả thực nghiệm chỉ lưu trong `results/`.
