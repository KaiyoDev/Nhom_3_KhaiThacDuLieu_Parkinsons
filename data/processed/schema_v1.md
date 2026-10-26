# schema_v1 — canonical CSV `parkinsons_v1.csv` (M01-T2)

- **Nguồn:** `data/raw/D07 - parkinsons.data.xlsx`, sheet `"parkinsons.data"`.
- **Phương pháp:** parse xlsx bằng stdlib (regex), **loại cột `name`**, giữ **22 feature + `status`** (giữ nguyên thứ tự cột & giá trị từ xlsx). Không impute, không đổi dtype.
- **Số dòng dữ liệu:** 195
- **Số cột:** 23 (22 feature + `status`)
- **Trùng lặp hàng (23 cột):** 0
- **Version / Người / Ngày:** v1 · M01 (Đặng Hoàng Ân / @KaiyoDev) · 2026-10-26

## Các cột (23)

| # | Cột | Nhóm | Kiểu | Thiếu (NaN) |
|---|-----|------|------|:-----------:|
| 1 | `MDVP:Fo(Hz)` | FREQ | float | 0 |
| 2 | `MDVP:Fhi(Hz)` | FREQ | float | 0 |
| 3 | `MDVP:Flo(Hz)` | FREQ | float | 0 |
| 4 | `MDVP:Jitter(%)` | JITTER | float | 0 |
| 5 | `MDVP:Jitter(Abs)` | JITTER | float | 0 |
| 6 | `MDVP:RAP` | JITTER | float | 0 |
| 7 | `MDVP:PPQ` | JITTER | float | 0 |
| 8 | `Jitter:DDP` | JITTER | float | 0 |
| 9 | `MDVP:Shimmer` | SHIMMER | float | 0 |
| 10 | `MDVP:Shimmer(dB)` | SHIMMER | float | 0 |
| 11 | `Shimmer:APQ3` | SHIMMER | float | 0 |
| 12 | `Shimmer:APQ5` | SHIMMER | float | 0 |
| 13 | `MDVP:APQ` | SHIMMER | float | 0 |
| 14 | `Shimmer:DDA` | SHIMMER | float | 0 |
| 15 | `NHR` | NOISE | float | 0 |
| 16 | `HNR` | NOISE | float | 0 |
| 17 | `status` | NHÃN | int 0/1 | 0 |
| 18 | `RPDE` | NONLIN | float | 0 |
| 19 | `DFA` | NONLIN | float | 0 |
| 20 | `spread1` | NONLIN | float | 0 |
| 21 | `spread2` | NONLIN | float | 0 |
| 22 | `D2` | NONLIN | float | 0 |
| 23 | `PPE` | NONLIN | float | 0 |

## Nhãn `status`

| Giá trị | Số mẫu |
|---------|:------:|
| 0 | 48 |
| 1 | 147 |

## Ghi chú (để M04/M05 đối chiếu)

- Chưa impute/chuẩn hoá ở đây (canonical = nguồn sạch). Chuẩn hoá (StandardScaler) làm ở M04-T1 (notebook 02).
- Giá trị giữ nguyên từ xlsx (có thể dạng số khoa học, vd `7.84E-3` — pandas đọc được).
