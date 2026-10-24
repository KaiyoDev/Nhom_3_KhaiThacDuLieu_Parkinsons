# DATA_DICTIONARY — Bảng mô tả thuộc tính (dataset Parkinson)

> **Nguồn đã xác minh:** file dataset `D07 - parkinsons.data.xlsx`,
> sheet `"Descriptipion"` (mô tả UCI Oxford Parkinson's + ghi chú nhóm) và
> sheet `"parkinsons.data"` (đã đọc header + kích thước tại local).
>
> **Nguyên tắc:** chỉ mô tả những gì **đã kiểm tra được**. Các cột *kiểu dữ liệu (dtype)*
> và *trị thiếu (missing)* chưa kiểm tra thực tế ở đây → để mục `M02-T1` (khám phá)
> điền sau, không bịa.

## 1. Tổng quan (đã xác minh)

| Mục | Giá trị | Nguồn |
|-----|---------|-------|
| File | `D07 - parkinsons.data.xlsx` | kiểm tra local |
| Sheet dữ liệu | `"parkinsons.data"` | kiểm tra local |
| Sheet mô tả | `"Descriptipion"` (gõ tắt "Description" trong file gốc) | kiểm tra local |
| Số dòng dữ liệu | **195** (sheet data, đã đếm tại local) | kiểm tra local |
| Số cột | **24** (1 `name` + 22 feature + 1 `status`) | kiểm tra local |
 | Ghi chú UCI | UCI header ghi "Number of Instances: 197" — **lệch với 195 thực tế**, cần đối chiếu lại khi phân tích | sheet mô tả |
| Nguồn gốc | Oxford Parkinson's Disease Detection Dataset (Max Little, Oxford) | sheet mô tả |
| Ghi chú Việt | "Data nằm ở sheet còn lại, cột nhãn là cột status (0- khỏe mạnh, 1- có bị Parkinson)"; "loại bỏ cột name trước khi thực hiện" | sheet mô tả |
| Nhiệm vụ | Phân lớp (classification) | sheet mô tả |

> Đối tượng: 31 người, 23 người bị Parkinson (theo UCI, sheet mô tả).

## 2. Bảng thuộc tính (24 cột)

> Nhóm: **FREQ** = frequency, **JITTER** = biến thiên tần số, **SHIMMER** = biến thiên biên độ,
> **NOISE** = nhiễu/tonal, **NONLIN** = phi tuyến. Cột *Xử lý* ghi rõ `LOẠI`/`NHÃN`/`FEATURE`.

| # | Cột | Nhóm | Ý nghĩa (đã xác minh từ sheet mô tả) | Xử lý | Kiểu / Thiếu |
|---|-----|------|----------------------------------------|:------:|--------------|
| 1 | `name` | ID | Tên chủ thể + số bản ghi (ASCII) | **LOẠI** (theo ghi chú) | chưa xác nhận (M02-T1) |
| 2 | `MDVP:Fo(Hz)` | FREQ | Tần số giọng cơ bản trung bình | FEATURE | chưa xác nhận |
| 3 | `MDVP:Fhi(Hz)` | FREQ | Tần số giọng cơ bản lớn nhất | FEATURE | chưa xác nhận |
| 4 | `MDVP:Flo(Hz)` | FREQ | Tần số giọng cơ bản nhỏ nhất | FEATURE | chưa xác nhận |
| 5 | `MDVP:Jitter(%)` | JITTER | Biến thiên tần số (jitter %) | FEATURE | chưa xác nhận |
| 6 | `MDVP:Jitter(Abs)` | JITTER | Biến thiên tần số (jitter tuyệt đối) | FEATURE | chưa xác nhận |
| 7 | `MDVP:RAP` | JITTER | Biên độ dao động ngắn hạn (jitter) | FEATURE | chưa xác nhận |
| 8 | `MDVP:PPQ` | JITTER | Chênh lệch pitch period (jitter) | FEATURE | chưa xác nhận |
| 9 | `Jitter:DDP` | JITTER | Chênh lệch pitch period 3 điểm (jitter) | FEATURE | chưa xác nhận |
| 10 | `MDVP:Shimmer` | SHIMMER | Biến thiên biên độ (shimmer) | FEATURE | chưa xác nhận |
| 11 | `MDVP:Shimmer(dB)` | SHIMMER | Biến thiên biên độ (dB) | FEATURE | chưa xác nhận |
| 12 | `Shimmer:APQ3` | SHIMMER | Amplitude pulse (shimmer) | FEATURE | chưa xác nhận |
| 13 | `Shimmer:APQ5` | SHIMMER | Amplitude pulse (shimmer) | FEATURE | chưa xác nhận |
| 14 | `MDVP:APQ` | SHIMMER | Amplitude pulse (shimmer) | FEATURE | chưa xác nhận |
| 15 | `Shimmer:DDA` | SHIMMER | Dạng sóng (shimmer) | FEATURE | chưa xác nhận |
| 16 | `NHR` | NOISE | Tỉ lệ noise (nhiễu) / tonal trong giọng | FEATURE | chưa xác nhận |
| 17 | `HNR` | NOISE | Harmonics-to-Noise Ratio (tonal / noise) | FEATURE | chưa xác nhận |
| 18 | `status` | NHÃN | Trạng thái sức khỏe: `1` = Parkinson, `0` = khỏe | **NHÃN (target)** | chưa xác nhận |
| 19 | `RPDE` | NONLIN | Độ phức tạp động học phi tuyến (nonlinear) | FEATURE | chưa xác nhận |
| 20 | `DFA` | NONLIN | Số mũ fractal scaling (fractal scaling exponent) | FEATURE | chưa xác nhận |
| 21 | `spread1` | NONLIN | Chỉ số phi tuyến (độ lan tỏa tần số, 1) | FEATURE | chưa xác nhận |
| 22 | `spread2` | NONLIN | Chỉ số phi tuyến (độ lan tỏa tần số, 2) | FEATURE | chưa xác nhận |
| 23 | `D2` | NONLIN | Chỉ số phi tuyến (fractal dimension) | FEATURE | chưa xác nhận |
| 24 | `PPE` | NONLIN | Pitch period entropy | FEATURE | chưa xác nhận |

> Nhóm phi tuyến (NONLIN) gồm `RPDE, DFA, spread1, spread2, D2, PPE` — UCI gom
> "ba chỉ số phi tuyến về biến thiên tần số cơ bản" (`spread1, spread2, PPE`)
> và "hai chỉ số phức tạp động học phi tuyến" (`RPDE, D2`); `DFA` là "signal fractal scaling exponent".
> Nhóm này có thể được **mở rộng/kết hợp** theo ý nghĩa cụ thể của từng bài (M02-T2).

## 3. Feature vector dùng cho mô hình (thống nhất trước)

- **Feature (22):** các dòng #2–#17 và #19–#24 ở trên (loại `name` #1, loại `status` #18).
- **Nhãn (target):** `status` (#18), nhị phân `0/1`.
- Các bước phân tích sẽ dùng **feature matrix 22 cột** (xem `M04-T1`), không bao giờ
  giữ `name`.

## 4. Trách nhiệm cập nhật

- **M02-T1** điền cột *Kiểu / Thiếu* sau khi kiểm tra thực tế trên canonical CSV.
- **M02-T2** có thể bổ sung *Ghi chú* (đơn vị, khoảng) nếu có nguồn rõ.
- Không sửa lại các ý nghĩa đã xác minh ở trên; nếu phát hiện lệch → ghi rõ nguồn + chờ review (M03).
