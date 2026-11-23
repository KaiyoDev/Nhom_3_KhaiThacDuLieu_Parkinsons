# Khai phá Dữ liệu — Oxford Parkinson's Disease Detection

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3%2B-F7931E?logo=scikit-learn&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-2.0%2B-150458?logo=pandas&logoColor=white)
![matplotlib](https://img.shields.io/badge/matplotlib-3.7%2B-0076C8)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![PRs](https://img.shields.io/badge/PRs-review%20required-success)

> **Môn:** Khai phá dữ liệu · **Nhóm 3** · **Dataset:** Oxford Parkinson's Disease Detection (UCI, Max Little)
> **Repo:** [`KaiyoDev/Nhom_3_KhaiThacDuLieu_Parkinsons`](https://github.com/KaiyoDev/Nhom_3_KhaiThacDuLieu_Parkinsons)

Mục lục: [About](#-about) · [Pipeline](#-kiến-trúc--pipeline) · [Dữ liệu](#-dữ-liệu) · [Kết quả](#-kết-quả-thực-nghiệm) · [Cấu trúc](#-cấu-trúc-thư-mục) · [Cài đặt](#-cài-đặt--chạy) · [Tái lập](#-tái-lập-reproducibility) · [Trạng thái](#-trạng-thái--deadline) · [Team](#-đội-ngũ) · [Tham khảo](#-tài-liệu--tham-khảo)

---

## 📌 About

Dự án xây dựng quy trình **khai phá dữ liệu (data mining)** hoàn chỉnh trên tập dữ liệu giọng nói
của bệnh nhân Parkinson: chuẩn bị dữ liệu → khám phá & chất lượng → tiền xử lý & PCA →
**phân lớp có giám sát** (F-score) → **phân cụm không giám sát** (ARI) → tổng hợp.

- **Bài toán:** phân loại `status` (`0` = khỏe, `1` = Parkinson) từ **22 đặc trưng giọng nói**
  (tần số, jitter, shimmer, noise, chỉ số phi tuyến).
- **Dữ liệu:** 195 bản ghi × 23 cột (22 feature + `status`), đã loại cột định danh `name`.
- **Mục tiêu kỹ thuật:** một đầu vào canonical duy nhất, pipeline tái lập được (cùng seed/phiên bản),
  đánh giá đúng chuẩn (CV stratified, chống data leakage), mọi kết quả có bảng/hình minh hoạ.
- **Kết quả nổi bật:**
  - PCA: 2 thành phần giải thích **70.2%** phương sai; 6 thành phần đạt **91.61%**.
  - Phân lớp: **F-score macro 0.87–0.89** (10-fold CV) với KNN / SVM / Random Forest.
  - Phân cụm: K-Means chọn **K=2** (silhouette 0.4373) nhưng **ARI ≈ −0.10**; DBSCAN **ARI −0.064**
    → cấu trúc không gian đặc trưng **không tự tách theo `status`** (bệnh lý cần mô hình có giám sát).

Dự án do 6 thành viên phối hợp qua quy trình Git/PR rõ ràng (branch theo nhiệm vụ → PR → review → merge),
với 2 "cổng" đồng bộ: **GATE #1** (thống nhất canonical CSV) và **GATE #2** (nhất quán trước báo cáo).

---

## 🏗️ Kiến trúc & Pipeline

```mermaid
flowchart TD
    A["data/raw/D07 - parkinsons.data.xlsx<br/>195 x 24 (gồm name)"] --> B["M01-T2 · Canonical CSV v1<br/>data/processed/parkinsons_v1.csv<br/>195 x 23 (bỏ name)"]
    B --> C["Khám phá + chất lượng<br/>M02 + M03"]
    C --> D["Tiền xử lý + PCA<br/>M04 · StandardScaler"]
    D --> E["Phân lớp + F-score<br/>M05 · 10-fold CV"]
    D --> F["Phân cụm + ARI<br/>M06 · KMeans/DBSCAN"]
    E --> G["Tổng hợp + Gate #2<br/>M06 chủ trì · M01 ký nhất quán"]
    F --> G
    G --> H["Báo cáo / figures"]
    B -. "GATE #1: mọi bước dùng cùng canonical v1" .-> C
```

Luồng trạng thái của mỗi nhiệm vụ:

```mermaid
stateDiagram-v2
    [*] --> Todo
    Todo --> InProgress: phụ trách bắt đầu
    InProgress --> Review: hoàn thành + checklist
    Review --> Done: reviewer xác nhận
    Todo --> Blocked: thiếu đầu vào
    InProgress --> Blocked: thiếu đầu vào
    Blocked --> Todo: đầu vào đã sẵn sàng
    Done --> [*]
```

Luồng dữ liệu trong pipeline tổng hợp (`src/pipeline.py`):

```mermaid
flowchart LR
    R["raw xlsx"] --> D["canonical CSV v1"]
    D --> X["X: 22 feature"]
    D --> Y["y: status"]
    X --> SC["StandardScaler"]
    SC --> P["PCA"]
    SC --> CL["Pipeline phân lớp<br/>(scaler + model)"]
    SC --> KM["KMeans / DBSCAN"]
    Y --> CL
    P --> F1["figures PCA"]
    CL --> R1["F-score (10-fold CV)"]
    KM --> R2["ARI (so status)"]
```

---

## 📊 Dữ liệu

### Tổng quan (đã xác minh trên `data/processed/parkinsons_v1.csv`)

| Hạng mục | Giá trị |
|----------|---------|
| Số mẫu | **195** |
| Số cột canonical | **23** = 22 feature + `status` |
| Nhãn | `0` (khỏe): **48** (24.62%) · `1` (Parkinson): **147** (75.38%) |
| Missing / trùng lặp | **0** / **0** |
| Feature | FREQ (3) · JITTER (5) · SHIMMER (6) · NOISE (2) · NONLIN (6) |
| Cột đã loại | `name` (định danh chủ thể) |
| Chênh lệch scale | Có (FREQ hàng trăm, JITTER ~1e-4) → cần chuẩn hoá |

```mermaid
pie
    "Parkinson (status=1)" : 147
    "Khỏe (status=0)" : 48
```

**Bằng chứng:** phân bố nhãn, phân bố feature và candidate outlier theo IQR 1.5,
sinh từ chạy thật trên canonical v1.

![Tổng quan dữ liệu](docs/images/eda_summary.png)

> Ghi chú: header UCI ghi "197 instances" nhưng file thực tế có **195 dòng dữ liệu** — đã đối chiếu
> và ghi nhận trong `DATA_DICTIONARY.md`.

---

## 🧪 Kết quả thực nghiệm

### 1. Kiểm tra chất lượng & thống kê mô tả (M03)

| Hạng mục | Kết quả |
|----------|---------|
| Label | `0`: 48 (24.62%) · `1`: 147 (75.38%) — **mất cân bằng** |
| NaN / trùng lặp | **0** / **0** |
| Candidate outlier (IQR 1.5) | **19/22** feature; **47/195** dòng (24.10%); `NHR=19`, `HNR=3` |
| Feature không có outlier | `MDVP:Fo(Hz)`, `RPDE`, `DFA` |
| Độ lệch | 14/22 feature có `\|skew\| > 1` (vd `NHR` skew 4.2207 / kurt 21.9950) |
| Đề xuất cho M04/M05 | `StandardScaler`; cân nhắc xử lý lệch nhãn; giữ outlier có kiểm soát |

Chi tiết: [`results/quality_report.md`](results/quality_report.md) ·
[`results/iqr_table.md`](results/iqr_table.md).

### 2. Phân tích thành phần chính (PCA, M04)

| Chỉ số | Giá trị |
|--------|---------|
| PC1 | **58.9%** |
| PC2 | **11.3%** |
| PC1 + PC2 | **70.2%** |
| Số thành phần đạt ≥ 90% | **6** (tích lũy **91.61%**) |

![PCA scatter](results/figures/02_pca_scatter.png)

Hai nhóm tách một phần, chồng lấp đáng kể trên PC1–PC2 — phù hợp với bài toán nhị phân có
nhiều đặc trưng âm thanh tương quan cao.

### 3. Phân bố & tương quan (M04)

![Phân bố 22 feature theo status](results/figures/m04-t3_histograms.png)

![Ma trận tương quan](results/figures/m04-t3_corr_heatmap.png)

- **14/22** feature lệch (`|skew| > 1`); **26/231** cặp feature có `|r| ≥ 0.9`.
- `Jitter:DDP ≈ 3 × MDVP:RAP` và `Shimmer:DDA ≈ 3 × Shimmer:APQ3` (r ≈ 1.0) — gần như trùng
  thông tin, được giữ nguyên trong canonical v1 và cần cân nhắc khi phân cụm.

### 4. Phân lớp (M05, 10-fold CV, seed 42)

| Mô hình | F-score macro (test) | F-score weighted (test) | F-score macro (train) |
|---------|:--------------------:|:-----------------------:|:---------------------:|
| KNN | 0.8757 ± 0.0742 | 0.9073 ± 0.0578 | 0.9647 |
| **SVM** | **0.8904 ± 0.0804** | **0.9199 ± 0.0603** | 0.9787 |
| Random Forest | 0.8737 ± 0.1171 | 0.9103 ± 0.0824 | 1.0000 |

![F-score 3 mô hình](docs/images/f1_scores.png)

- Chênh lệch giữa các mô hình (~0.016) **nhỏ hơn** độ lệch chuẩn giữa các fold (0.07–0.12) →
  không kết luận mô hình tốt nhất một cách quá chắc chắn.
- Random Forest có train F-score 1.0000 và std lớn nhất → dấu hiệu overfit.
- Điểm weighted cao hơn macro do lớp khỏe (48 mẫu) nhỏ hơn.

### 5. Phân cụm + ARI (M06, KMeans & DBSCAN)

**K-Means** (seed 42, `n_init=10`), K được chọn theo **Silhouette cực đại**:

| K | Inertia | Silhouette | Kích thước cụm | ARI (so `status`) |
|---:|--------:|-----------:|----------------|------------------:|
| **2** | 2817.2 | **0.4373** | `[165, 30]` | **−0.0978** |
| 3 | 2076.2 | 0.2763 | `[106, 77, 12]` | 0.0582 |
| 4 | 1822.4 | 0.2358 | `[91, 77, 23, 4]` | 0.0583 |
| 5 | 1595.5 | 0.2048 | `[73, 64, 32, 22, 4]` | 0.1000 |
| 6 | 1442.0 | 0.2138 | `[60, 51, 30, 28, 22, 4]` | 0.1058 |
| 7 | 1319.8 | 0.2094 | `[54, 51, 31, 24, 23, 8, 4]` | 0.0882 |
| 8 | 1230.5 | 0.2201 | `[53, 35, 32, 23, 23, 15, 10, 4]` | 0.0313 |
| 9 | 1157.0 | 0.2265 | `[52, 39, 25, 24, 21, 13, 9, 8, 4]` | 0.0574 |
| 10 | 1110.7 | 0.1896 | `[38, 35, 26, 23, 22, 18, 12, 9, 8, 4]` | 0.0481 |

**DBSCAN** (`min_samples=5`, `eps=3.37` — knee của k-distance):

| eps | min_samples | Số cụm | Điểm nhiễu (−1) | ARI |
|----:|------------:|:------:|:---------------:|----:|
| 3.37 | 5 | **1** (183 điểm) | **12** | **−0.0639** |

- Toàn lưới (`min_samples ∈ {3,5,10}` × `eps ∈ {1.5…5.0}`): ARI ∈ **[−0.0744, 0.1625]**;
  giá trị cao nhất ở `eps=1.5, min_samples=5` nhưng 149/195 điểm bị coi là nhiễu → không có ý nghĩa.
- **Nhận xét:** cụm K=2 tách một nhóm nhỏ 30 mẫu (toàn `status=1`) khác biệt mạnh ở
  `Shimmer:APQ5`, `MDVP:Shimmer`, `HNR`; nhưng **ARI ≈ 0/âm** ⇒ cấu trúc tự nhiên **không khớp**
  ranh giới bệnh lý — cần mô hình có giám sát (M05).

![K-Means selection](results/figures/m06_kmeans_selection.png)

![DBSCAN analysis](results/figures/m06_dbscan_analysis.png)

---

## 🗂️ Cấu trúc thư mục

```text
Nhom_3_KhaiThacDuLieu_Parkinsons/
├── README.md                     # file này
├── TEAM.md                       # đội ngũ 6 thành viên
├── TASK_BOARD.md                 # trạng thái từng nhiệm vụ + deadline
├── TASK_ASSIGNMENTS.md           # phân rã 21 mã nhiệm vụ + phụ thuộc + reviewer
├── PROJECT_WORKFLOW.md           # luồng 6 giai đoạn + 2 gate
├── HANDOFF.md · CONTRIBUTING.md  # quy trình bàn giao & đóng góp
├── DATA_DICTIONARY.md            # mô tả 24 cột (đã xác minh)
├── docs/
│   ├── COLAB_GUIDE.md · GITHUB_GUIDE.md · TROUBLESHOOTING.md
│   ├── REPRODUCIBILITY.md        # quy ước seed/k/scaler/phiên bản
│   └── images/                   # hình minh hoạ trong README
├── data/
│   ├── raw/                      # dataset gốc (xlsx, đã commit)
│   ├── interim/                  # trung gian (không commit)
│   └── processed/                # canonical CSV v1 + schema
├── notebooks/                    # 01 khám phá · 02 PCA · 03 phân lớp · 04 cụm · 05 tổng hợp
├── src/
│   ├── preprocessing.py          # nạp canonical, tách X/y, StandardScaler
│   └── pipeline.py               # pipeline tổng hợp (chạy được độc lập)
├── results/                      # thống kê/chất lượng/F-score/ARI/báo cáo + figures/
├── reports/                      # báo cáo tổng hợp (M06-T3)
└── workspaces/                   # work-order từng thành viên
```

---

## ⚙️ Cài đặt & chạy

### Môi trường

- **Python ≥ 3.10** (đã kiểm tra trên 3.14)
- `numpy`, `pandas`, `scipy`, `scikit-learn`, `matplotlib`, `seaborn`, `openpyxl`, `jupyter`
  (phiên bản tối thiểu trong `requirements.txt`)

```bash
git clone https://github.com/KaiyoDev/Nhom_3_KhaiThacDuLieu_Parkinsons.git
cd Nhom_3_KhaiThacDuLieu_Parkinsons
python -m venv .venv
source .venv/Scripts/activate      # Windows; trên Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
```

### Chạy pipeline tổng hợp

```bash
python -m src.pipeline
```

Đầu ra: `results/pipeline_summary.json` — chỉ báo dữ liệu, PCA, F-score, tham số mỗi fold,
seed và phiên bản thư viện.

### Chạy notebook từng bước

```bash
jupyter lab notebooks/01_data_exploration.ipynb
jupyter lab notebooks/02_preprocessing_pca.ipynb
jupyter lab notebooks/03_classification.ipynb
jupyter lab notebooks/04_clustering.ipynb
```

### Google Colab

Mỗi thành viên dùng runtime riêng: upload `data/processed/parkinsons_v1.csv`, cài thêm
`openpyxl` nếu đọc xlsx, chạy từ notebook. Xem `docs/COLAB_GUIDE.md`.

---

## 🔁 Tái lập (reproducibility)

Quy ước chốt trong `docs/REPRODUCIBILITY.md`:

| Tham số | Giá trị |
|---------|---------|
| Seed | `42` |
| CV phân lớp | **k ngoài = 10**, **k trong = 5**, stratified theo `status` |
| Scaler | `StandardScaler` (fit trên train trong Pipeline; PCA/cụm fit trên toàn bộ X) |
| Chỉ số phân lớp | F-score **macro** (chính) + weighted (đối chiếu) |
| PCA | 2 thành phần để vẽ (70.2%); 6 thành phần nếu cần ≥ 90% |
| Phân cụm | KMeans `n_init=10`, K = 2…10; DBSCAN `min_samples=5`, `eps=3.37` (knee); ARI so `status` |
| Anti-leakage | scaler fit trong fold train (Pipeline); chọn tham số bằng nested `GridSearchCV`; PCA/phân cụm fit trên toàn bộ X (không giám sát) |
| Dữ liệu | `data/processed/parkinsons_v1.csv` (version v1) — một đầu vào duy nhất |
| Phiên bản đã dùng | `scikit-learn 1.9.x`, `pandas 3.x`, `numpy 2.4+` (chi tiết từng lần chạy trong `results/*`) |

Chạy `python -m src.pipeline` phải cho ra đúng các số PCA/F-score ở mục [Kết quả](#-kết-quả-thực-nghiệm);
số phân cụm/ARI đã được tái lập độc lập trên canonical v1 (`results/m06_cluster_ari.csv`).

---

## ⚠️ Hạn chế

- Dữ liệu nhỏ (**195 mẫu**) và **mất cân bằng** (147/48); nhiều bản ghi thuộc cùng một người
  (~31 chủ thể) nên CV có thể đặt bản ghi cùng người vào cả train/test.
- PCA 2 thành phần chỉ giữ **70.2%** phương sai (nếu cần ≥90% phải dùng 6 thành phần).
- Phân cụm không giám sát cho **ARI ≈ 0/âm** — không tìm được cấu trúc cụm tự nhiên khớp `status`.
- DBSCAN chỉ thành **1 cụm + 12 điểm nhiễu** ở tham số đã chọn.
- Một số kết quả thư viện khác phiên bản giữa các lần chạy (vd M06 dùng `sklearn 1.9.1`) nhưng
  số liệu vẫn tái lập khớp khi kiểm tra chéo.

---

## 📋 Trạng thái & deadline

> **Deadline bài tập: 20/11/2026 (đã qua).** Bảng chi tiết: [`TASK_BOARD.md`](TASK_BOARD.md).

| Mã | Thành viên | Trạng thái | Bằng chứng |
|----|-----------|:----------:|------------|
| M01 | Đặng Hoàng Ân | 🟡 Đang điều phối | T1/T2 xong; gate S-T1 đang chốt |
| M02 | Lê Thiên Lộc | ✅ Hoàn thành | PR #5 đạt review & merge |
| M03 | Huỳnh Gia Hợp | 🔵 Đang review | PR #13: đủ thống kê/skew/kurtosis/IQR; notebook JSON hợp lệ |
| M04 | Trần Hoàng Thông | ✅ Hoàn thành | PR #7 đã merge (17/11) |
| M05 | Ngô Thị Anh Thư | ✅ Hoàn thành | PR #8 đã merge (22/11) |
| M06 | Nguyễn Hoàng Bách | 🔵 Đang review | PR #14: KMeans/DBSCAN + ARI tái lập khớp |

**Tiến độ:** 11 `Done` · 5 `Review` · 2 `In Progress` · 2 `Blocked` · 1 `Todo`.
Các PR đã merge: #5 (M02), #7 (M04), #8 (M05), #9 (board), #10 (README+pipeline),
#13 (M03), #14 (M06). Còn treo: **M06-T3** tổng hợp (`reports/summary.md` + notebook 05) và các gate S-T1/S-T2.

---

## 👥 Đội ngũ

| Mã | Tên | MSSV | Vai trò | Notebook |
|----|-----|------|---------|:--------:|
| M01 | Đặng Hoàng Ân | `080206014982` | Điều phối · dữ liệu · gate | (data prep, gate) |
| M02 | Lê Thiên Lộc | `079306040024` | Khám phá cấu trúc & dtype | 01 |
| M03 | Huỳnh Gia Hợp | `054205008367` | Thống kê mô tả · chất lượng | 01 |
| M04 | Trần Hoàng Thông | `075206008044` | Tiền xử lý · PCA · trực quan | 02 |
| M05 | Ngô Thị Anh Thư | `087306008195` | Phân lớp · CV · F-score | 03 |
| M06 | Nguyễn Hoàng Bách | `056205005522` | Phân cụm · ARI · tổng hợp | 04, 05 |

Nguồn: [`TEAM.md`](TEAM.md).

---

## 🤝 Quy ước đóng góp

- **Branch:** `task/<mã-member>-<mã-task>-<tên-ngắn>`; commit theo **Conventional Commits**.
- **PR:** bắt buộc trên `main` (branch protection `PR required`), gồm `Summary` · `Test Plan` · `Risk`.
- **Review:** mỗi nhiệm vụ có người review; chỉ `Done` khi đạt tiêu chí nghiệm thu.
- **Dữ liệu:** một canonical CSV duy nhất; không tạo bản CSV riêng; không commit bí mật/raw.
- Chi tiết: [`CONTRIBUTING.md`](CONTRIBUTING.md) · [`HANDOFF.md`](HANDOFF.md).

---

## 📚 Tài liệu & tham khảo

- **Dataset:** Max Little, University of Oxford — *Oxford Parkinson's Disease Detection Dataset*,
  UCI Machine Learning Repository. Ghi chú: mô tả UCI ghi 197 instances, file thực tế 195 dòng.
- **Bài báo liên quan:** Little, M. A., McSharry, P. E., Hunter, E. J., & Ramig, L. O. (2009).
  *Suitability of dysphonia measurements for telemonitoring of Parkinson's disease.*
  IEEE Transactions on Biomedical Engineering, 56(4), 1015–1023.
- **Tài liệu nội bộ:** [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md) ·
  [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md) ·
  [`PROJECT_WORKFLOW.md`](PROJECT_WORKFLOW.md) ·
  [`docs/COLAB_GUIDE.md`](docs/COLAB_GUIDE.md).

---

## 🛡️ Ghi chú an toàn

- Không commit token/mật khẩu/API key; `.env`, `*.key`, `secrets*` đã được `.gitignore` chặn.
- Cột `name` (định danh chủ thể) **loại bỏ** khỏi canonical CSV; chỉ giữ trong `data/raw/` nếu
  cần đối chiếu nội bộ.
- Mọi số liệu/figure trong README đều sinh từ chạy thật trên canonical v1; không điền sẵn số giả.
