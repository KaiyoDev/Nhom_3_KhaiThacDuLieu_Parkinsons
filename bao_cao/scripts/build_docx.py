"""Build BaoCao_BaiTapLon_Nhom3.docx from the report content (mirrors the LaTeX PDF).

Run: python scripts/build_docx.py
"""
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
DIST.mkdir(exist_ok=True)
FIG = ROOT / "figures"

NAVY = RGBColor(0x1F, 0x38, 0x64)
DARK = RGBColor(0x20, 0x20, 0x20)

doc = Document()

# ----- base styles -----
normal = doc.styles["Normal"]
normal.font.name = "Times New Roman"
normal.font.size = Pt(13)
normal.font.color.rgb = DARK
normal.element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
pf = normal.paragraph_format
pf.line_spacing = 1.3
pf.space_after = Pt(6)

for name, size, bold, italic, color in (
    ("Heading 1", 15, True, False, NAVY),
    ("Heading 2", 13.5, True, False, NAVY),
    ("Heading 3", 13, True, True, NAVY),
    ("Heading 4", 13, True, False, DARK),
):
    st = doc.styles[name]
    st.font.name = "Times New Roman"
    st.font.size = Pt(size)
    st.font.bold = bold
    st.font.italic = italic
    st.font.color.rgb = color
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")

sec = doc.sections[0]
sec.top_margin = Cm(2.5)
sec.bottom_margin = Cm(2.5)
sec.left_margin = Cm(3.0)
sec.right_margin = Cm(2.0)


def rich(p, text, bold=False, italic=False, size=None, color=None):
    """Add runs, hien thi **in dam**."""
    parts = text.split("**")
    for i, part in enumerate(parts):
        if not part:
            continue
        r = p.add_run(part)
        r.font.name = "Times New Roman"
        r.element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
        r.bold = bold or i % 2 == 1
        r.italic = italic
        if size:
            r.font.size = Pt(size)
        if color is not None:
            r.font.color.rgb = color
    return p


def para(text="", align=None, bold=False, italic=False, size=None, space_after=None, color=None):
    p = doc.add_paragraph()
    if align is not None:
        p.alignment = align
    if space_after is not None:
        p.paragraph_format.space_after = Pt(space_after)
    rich(p, text, bold=bold, italic=italic, size=size, color=color)
    return p


def bullet(text):
    p = doc.add_paragraph(style="List Bullet")
    rich(p, text)
    p.paragraph_format.space_after = Pt(3)
    return p


def numbered(text):
    p = doc.add_paragraph(style="List Number")
    rich(p, text)
    p.paragraph_format.space_after = Pt(3)
    return p


def shade(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color)
    tcPr.append(shd)


def set_cell(cell, text, bold=False, size=11, align=None, color=None):
    cell.text = ""
    p = cell.paragraphs[0]
    if align is not None:
        p.alignment = align
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.space_before = Pt(2)
    rich(p, str(text), bold=bold, size=size, color=color)


def make_table(headers, rows, widths=None, font_size=10.5):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = t.rows[0].cells
    for i, h in enumerate(headers):
        set_cell(hdr[i], h, bold=True, size=font_size, align=WD_ALIGN_PARAGRAPH.CENTER)
        shade(hdr[i], "D9E2F3")
    for row in rows:
        cells = t.add_row().cells
        for i, val in enumerate(row):
            align = WD_ALIGN_PARAGRAPH.CENTER if i == 0 else None
            set_cell(cells[i], val, size=font_size, align=align)
    if widths:
        for r in t.rows:
            for i, w in enumerate(widths):
                r.cells[i].width = Cm(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return t


def caption(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    rich(p, text, italic=True, size=11)
    p.paragraph_format.space_after = Pt(10)
    return p


def figure(name, cap, width_cm=15.5):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(str(FIG / name), width=Cm(width_cm))
    caption(cap)


def page_break():
    p = doc.add_paragraph()
    p.add_run().add_break(WD_BREAK.PAGE)


def add_hyperlink(paragraph, url, text):
    part = paragraph.part
    r_id = part.relate_to(url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink", is_external=True)
    link = OxmlElement("w:hyperlink")
    link.set(qn("r:id"), r_id)
    r = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    rFonts = OxmlElement("w:rFonts")
    rFonts.set(qn("w:ascii"), "Times New Roman")
    rFonts.set(qn("w:hAnsi"), "Times New Roman")
    rPr.append(rFonts)
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "0563C1")
    rPr.append(color)
    u = OxmlElement("w:u")
    u.set(qn("w:val"), "single")
    rPr.append(u)
    r.append(rPr)
    t = OxmlElement("w:t")
    t.text = text
    r.append(t)
    link.append(r)
    paragraph._p.append(link)


def toc():
    p = doc.add_paragraph()
    run = p.add_run()
    b = OxmlElement("w:fldChar"); b.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText"); instr.set(qn("xml:space"), "preserve")
    instr.text = 'TOC \\o "1-3" \\h \\z \\u'
    s = OxmlElement("w:fldChar"); s.set(qn("w:fldCharType"), "separate")
    txt = OxmlElement("w:t"); txt.text = "Mục lục sẽ hiện ra khi bạn nhấn F9 (hoặc Cập nhật trường)."
    e = OxmlElement("w:fldChar"); e.set(qn("w:fldCharType"), "end")
    for el in (b, instr, s, txt, e):
        run._r.append(el)


# ============================ COVER ============================
para("TRƯỜNG ĐẠI HỌC GIAO THÔNG VẬN TẢI TP.HCM", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=13)
para("VIỆN CÔNG NGHỆ THÔNG TIN VÀ ĐIỆN - ĐIỆN TỬ", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=13)
para("", space_after=6)
pic = doc.add_paragraph(); pic.alignment = WD_ALIGN_PARAGRAPH.CENTER
pic.add_run().add_picture(str(FIG / "uth_logo.png"), width=Cm(9))
para("", space_after=6)
para("BÁO CÁO BÀI TẬP LỚN", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=15)
para("KHAI PHÁ DỮ LIỆU GIỌNG NÓI", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=17, color=NAVY)
para("PHÁT HIỆN BỆNH PARKINSON", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=17, color=NAVY)
para("", space_after=6)
para("Học phần: Khai phá dữ liệu", align=WD_ALIGN_PARAGRAPH.CENTER, size=13)
para("Mã lớp học phần: 012012204102", align=WD_ALIGN_PARAGRAPH.CENTER, size=13)
para("Học kỳ I · Năm học 2026-2027", align=WD_ALIGN_PARAGRAPH.CENTER, size=13)
para("", space_after=6)
para("Giảng viên hướng dẫn: Bùi Trọng Hiếu", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=13)
para("Sinh viên thực hiện: NHÓM 3", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=13)
para("", space_after=6)
make_table(
    ["STT", "Họ và tên", "MSSV", "Nhiệm vụ chính"],
    [
        ["1", "Đặng Hoàng Ân", "080206014982", "Điều phối, dữ liệu, gate"],
        ["2", "Lê Thiên Lộc", "079306040024", "Khám phá cấu trúc, dtype"],
        ["3", "Huỳnh Gia Hợp", "054205008367", "Thống kê mô tả, chất lượng dữ liệu"],
        ["4", "Trần Hoàng Thông", "075206008044", "Tiền xử lý, PCA, trực quan hóa"],
        ["5", "Ngô Thị Anh Thư", "087306008195", "Phân loại, cross-validation, F-score"],
        ["6", "Nguyễn Hoàng Bách", "056205005522", "Phân cụm, ARI, tổng hợp báo cáo"],
    ],
    widths=[1.3, 4.5, 3.2, 6.5],
)
para("", space_after=6)
para("TP. Hồ Chí Minh, tháng 11 năm 2026", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=13)
page_break()

# ============================ DECLARATION ============================
doc.add_heading("LỜI CAM ĐOAN", level=1)
para("Chúng em - NHÓM 3 lớp 012012204102 - xin cam đoan báo cáo đề tài “KHAI PHÁ DỮ LIỆU GIỌNG NÓI PHÁT HIỆN BỆNH PARKINSON” là công trình nghiên cứu và thực nghiệm thực hiện phối hợp bởi Nhóm 3 dưới sự hướng dẫn khoa học của giảng viên Bùi Trọng Hiếu. Toàn bộ số liệu, phân tích, công thức tính toán, mã nguồn và kết quả thực nghiệm trình bày trong báo cáo là trung thực, được tái lập được trên cùng một bộ dữ liệu chuẩn (parkinsons_v1.csv) và cùng hạt giống ngẫu nhiên (seed = 42).")
para("Mọi tài liệu tham khảo, tiêu chuẩn và công trình học thuật trích dẫn trong báo cáo đều được ghi rõ nguồn gốc theo đúng quy định về liêm chính học thuật. Chúng em xin chịu trách nhiệm hoàn toàn về nội dung và mã nguồn được trình bày trong báo cáo này.")
para("")
make_table(
    ["STT", "Họ và tên", "MSSV", "Chữ ký"],
    [[str(i + 1), n, m, ""] for i, (n, m) in enumerate([
        ("Đặng Hoàng Ân", "080206014982"),
        ("Lê Thiên Lộc", "079306040024"),
        ("Huỳnh Gia Hợp", "054205008367"),
        ("Trần Hoàng Thông", "075206008044"),
        ("Ngô Thị Anh Thư", "087306008195"),
        ("Nguyễn Hoàng Bách", "056205005522"),
    ])],
    widths=[1.3, 4.6, 3.4, 4.0],
)
para("TP. Hồ Chí Minh, tháng 11 năm 2026", align=WD_ALIGN_PARAGRAPH.RIGHT, italic=True)
para("Sinh viên thực hiện", align=WD_ALIGN_PARAGRAPH.RIGHT, bold=True)
page_break()

# ============================ ACKNOWLEDGEMENTS ============================
doc.add_heading("LỜI CẢM ƠN", level=1)
para("Lời đầu tiên, chúng em - NHÓM 3 - xin bày tỏ lòng biết ơn sâu sắc nhất tới giảng viên hướng dẫn, Bùi Trọng Hiếu, người đã tận tình hướng dẫn, chỉnh chu học thuật và động viên nhóm trong suốt quá trình thực hiện bài tập lớn môn Khai phá dữ liệu.")
para("Chúng em cũng xin gửi lời cảm ơn chân thành đến quý Thầy, Cô thuộc Viện Công nghệ Thông tin và Điện - Điện tử - Trường Đại học Giao thông Vận tải TP.HCM đã truyền đạt những kiến thức nền tảng quý báu và tạo điều kiện về môi trường học tập, nghiên cứu để nhóm hoàn thành đề tài.")
para("Cuối cùng, chúng em xin cảm ơn gia đình, bạn bè và mọi người đã luôn động viên, chia sẻ trong thời gian thực hiện. Dù đã nỗ lực hết mình, báo cáo khó tránh khỏi những thiếu sót; nhóm rất mong nhận được ý kiến đóng góp của giảng viên và bạn đọc.")
para("TP. Hồ Chí Minh, tháng 11 năm 2026", align=WD_ALIGN_PARAGRAPH.RIGHT, italic=True)
para("Sinh viên thực hiện", align=WD_ALIGN_PARAGRAPH.RIGHT, bold=True)
page_break()

# ============================ TOC & ABBREVIATIONS ============================
doc.add_heading("MỤC LỤC", level=1)
toc()
page_break()
doc.add_heading("DANH MỤC TỪ VIẾT TẮT", level=1)
make_table(
    ["STT", "Từ viết tắt", "Giải thích"],
    [
        ["1", "ARI", "Adjusted Rand Index (Chỉ số Rand hiệu chỉnh)"],
        ["2", "CV", "Cross-Validation (Kiểm định chéo)"],
        ["3", "DBSCAN", "Density-Based Spatial Clustering of Applications with Noise"],
        ["4", "EDA", "Exploratory Data Analysis (Phân tích dữ liệu khám phá)"],
        ["5", "F-score", "F-measure (Độ đo F, đánh giá phân loại)"],
        ["6", "IQR", "Interquartile Range (Khoảng tứ phân vị)"],
        ["7", "KNN", "K-Nearest Neighbors (K láng giềng gần nhất)"],
        ["8", "PCA", "Principal Component Analysis (Phân tích thành phần chính)"],
        ["9", "RF", "Random Forest (Rừng ngẫu nhiên)"],
        ["10", "SVM", "Support Vector Machine (Máy vector hỗ trợ)"],
        ["11", "UCI", "University of California, Irvine - Kho lưu trữ học máy"],
        ["12", "XLSX / CSV", "Định dạng tệp Excel / Giá trị phân tách bởi dấu phẩy"],
    ],
    widths=[1.3, 3.4, 10.8],
)
page_break()

# ============================ CHAPTER 1 ============================
doc.add_heading("CHƯƠNG 1. MỞ ĐẦU", level=1)
doc.add_heading("1.1. Bối cảnh và động lực", level=2)
para("Bệnh Parkinson là một trong những bệnh thoái hoá thần kinh phổ biến ở người cao tuổi. Giai đoạn đầu bệnh diễn biến âm thầm, khiến việc phát hiện sớm trở nên khó khăn nếu chỉ dựa vào các triệu chứng vận động điển hình. Một trong những dấu hiệu sớm và dễ quan sát là thay đổi giọng nói: người bệnh thường xuất hiện run giọng, giọng nhỏ, khàn hoặc mất điều khiển tần số, biên độ. Các đại lượng âm học thu được từ giọng nói do đó trở thành nguồn tín hiệu phi xâm lấn có tiềm năng hỗ trợ sàng lọc và theo dõi bệnh.")
para("Trong công trình nghiên cứu nổi bật, Little và cộng sự đã thu thập và công bố bộ dữ liệu giọng nói Parkinson trên kho lưu trữ học máy UCI. Bộ dữ liệu gồm 195 bản ghi, mỗi bản ghi mô tả bởi 22 đặc trưng giọng nói thuộc các nhóm tần số, độ run (jitter), độ ồn (shimmer), tỷ lệ nhiễu-giọng và chỉ số phi tuyến, kèm nhãn status (0 = khỏe, 1 = Parkinson). Kích thước nhỏ và mất cân bằng nhãn làm bộ dữ liệu trở thành tình huống thực tế để rèn nghề khai phá dữ liệu.")
doc.add_heading("1.2. Mục tiêu đề tài", level=2)
para("**Mục tiêu tổng quát.** Xây dựng một quy trình khai phá dữ liệu hoàn chỉnh, tái lập được trên bộ dữ liệu giọng nói Parkinson; sử dụng một bộ dữ liệu chuẩn duy nhất, cùng hạt giống ngẫu nhiên và cùng bộ chỉ số đánh giá ở mọi bước.")
para("**Các câu hỏi nghiên cứu.**")
bullet("RQ1 - Chất lượng dữ liệu: kích thước, kiểu dữ liệu, nhãn, thang đo, giá trị thiếu/trùng, ngoại lai và độ lệch như thế nào? Cần xử lý ra sao?")
bullet("RQ2 - Phân loại có giám sát: các mô hình KNN, SVM và Random Forest đạt kết quả nào khi đánh giá bằng kiểm định chéo phân tầng 10-fold và độ đo F-score?")
bullet("RQ3 - Phân cụm không giám sát: cấu trúc cụm tự phát sinh có phù hợp với ranh giới bệnh lý status hay không (đo bằng ARI)?")
doc.add_heading("1.3. Phạm vi và giới hạn", level=2)
para("Đề tài tập trung vào quy trình khai phá dữ liệu và học máy với bộ dữ liệu công khai có sẵn, không nhằm mục tiêu chẩn đoán y khoa. Kết quả thực nghiệm được giới hạn ở 195 bản ghi, khoảng 32 chủ thể trong dữ liệu thô, nên chưa khẳng định được hiệu năng trên dân số rộng. Nhóm không thay đổi, bổ sung hay gán lại nhãn ngoài dữ liệu công bố.")
doc.add_heading("1.3. Tổ chức báo cáo", level=2)
para("Báo cáo gồm năm chương: Chương 1 mở đầu; Chương 2 cơ sở lý thuyết; Chương 3 phương pháp và kiến trúc thực hiện; Chương 4 kết quả thực nghiệm; Chương 5 kết luận và hướng phát triển.")
doc.add_heading("1.4. Thành viên và vai trò", level=2)
make_table(
    ["Mã", "Họ và tên", "MSSV", "Vai trò / nhiệm vụ chính"],
    [
        ["M01", "Đặng Hoàng Ân", "080206014982", "Điều phối, chuẩn bị dữ liệu, kiểm soát gate"],
        ["M02", "Lê Thiên Lộc", "079306040024", "Khám phá cấu trúc, kiểu dữ liệu, bản đồ đặc trưng"],
        ["M03", "Huỳnh Gia Hợp", "054205008367", "Thống kê mô tả, kiểm tra chất lượng, ngoại lai IQR"],
        ["M04", "Trần Hoàng Thông", "075206008044", "Tiền xử lý, PCA, trực quan hóa"],
        ["M05", "Ngô Thị Anh Thư", "087306008195", "Phân loại, cross-validation, F-score"],
        ["M06", "Nguyễn Hoàng Bách", "056205005522", "Phân cụm, ARI, tổng hợp kết quả và báo cáo"],
    ],
    widths=[1.4, 4.0, 3.2, 6.9],
)
caption("Bảng 1.1. Thành viên và vai trò trong đề tài")
page_break()

# ============================ CHAPTER 2 ============================
doc.add_heading("CHƯƠNG 2. CƠ SỞ LÝ THUYẾT", level=1)
doc.add_heading("2.1. Tín hiệu giọng nói và các nhóm đặc trưng", level=2)
para("Bộ dữ liệu sử dụng các đại lượng âm học thu được từ bản ghi âm đọc nguyên âm “aa” dài khoảng một giây của từng chủ thể. Mỗi bản ghi được mô tả bởi 22 đặc trưng thuộc năm nhóm chức năng.")
make_table(
    ["Nhóm", "Đặc trưng đại diện", "Số lượng"],
    [
        ["Tần số cơ bản", "MDVP:Fo(Hz), MDVP:Fhi(Hz), MDVP:Flo(Hz)", "3"],
        ["Độ run tần số (Jitter)", "MDVP:Jitter(%), MDVP:Jitter(Abs), MDVP:RAP, MDVP:PPQ, Jitter:DDP", "5"],
        ["Độ run biên độ (Shimmer)", "MDVP:Shimmer, MDVP:Shimmer(dB), Shimmer:APQ3, Shimmer:APQ5, MDVP:APQ, Shimmer:DDA", "6"],
        ["Tỷ lệ nhiễu - giọng", "NHR, HNR", "2"],
        ["Chỉ số phi tuyến", "RPDE, DFA, spread1, spread2, D2, PPE", "6"],
    ],
    widths=[4.2, 8.6, 2.2],
)
caption("Bảng 2.1. Các nhóm đặc trưng trong bộ dữ liệu")
doc.add_heading("2.2. Tiền xử lý dữ liệu", level=2)
para("Kiểm tra chất lượng bao gồm kích thước, kiểu dữ liệu, giá trị thiếu, trùng lặp, ngoại lai và độ lệch. Giá trị ngoại lai xác định theo quy tắc IQR: IQR = Q3 − Q1; ngưỡng = [Q1 − 1,5·IQR; Q3 + 1,5·IQR]. Độ lệch đo bằng skewness; với |skew| > 1 cần lưu ý khi dùng mô hình nhạy cảm với phân phối.")
para("Vì các đặc trưng có thang đo khác nhau, nhóm áp dụng chuẩn hoá z-score: z_ij = (x_ij − μ_j)/σ_j. Trong phân loại, bộ chuẩn hoá chỉ học trên tập huấn luyện từng fold; với PCA và phân cụm, chuẩn hoá trên toàn bộ tập đặc trưng do không dùng nhãn khi học.")
doc.add_heading("2.3. Phân tích thành phần chính (PCA)", level=2)
para("PCA tìm hệ trục tuyến tính mới để thành phần đầu giữ phương sai lớn nhất, các thành phần tiếp theo kề nhau trực giao. Với ma trận hiệp phương sai S = XᵀX/(n−1), phân tích trị riêng S·v_i = λ_i·v_i; tỷ lệ phương sai giải thích của thành phần i là λ_i/Σλ_j. PCA vừa trực quan hoá dữ liệu, vừa xác định số thành phần cần giữ đạt ngưỡng phương sai mong muốn.")
doc.add_heading("2.4. Các phương pháp phân loại có giám sát", level=2)
bullet("KNN phân loại theo đa số nhãn của k láng giềng gần nhất; nhạy với thang đo nên cần chuẩn hoá.")
bullet("SVM tìm siêu phẳng phân chia tối đu định hướng với lề lớn; kernel RBF cho ranh giới phi tuyến.")
bullet("Random Forest là tập hợp nhiều cây quyết định huấn luyện trên mẫu và đặc trưng ngẫu nhiên, tổng hợp bằng đa số phiếu; dễ quá khớp nếu không giới hạn.")
para("Đánh giá dùng kiểm định chéo phân tầng 10-fold (StratifiedKFold, seed 42), chọn tham số bằng GridSearchCV 5-fold trong tập huấn luyện. Độ đo chính là F-score macro: F1 = 2PR/(P+R); macro-F = trung bình F1 các lớp; weighted-F = trung bình có trọng số tỷ trọng mẫu.")
doc.add_heading("2.5. Các phương pháp phân cụm không giám sát", level=2)
para("K-Means chia dữ liệu thành K cụm bằng cách tối thiểu inertia J = Σ_c Σ_{x∈C_c} ||x − μ_c||². Số cụm chọn theo silhouette: s(i) = (b(i) − a(i))/max{a(i), b(i)}.")
para("DBSCAN nhóm theo mật độ: điểm lõi có ít nhất min_samples điểm trong bán kính ε; điểm không thuộc cụm nào là nhiễu. ARI đo tương đồng phân hoạch với nhãn thật, hiệu chỉnh theo ngẫu nhiên: ARI = 1 là phù hợp hoàn hảo, 0 tương đương phân ngẫu nhiên, âm là kém hơn ngẫu nhiên.")
doc.add_heading("2.6. Đảm bảo tái lập và chống rò rỉ dữ liệu", level=2)
numbered("Một đầu vào chuẩn duy nhất: parkinsons_v1.csv (GATE #1).")
numbered("Bộ chuẩn hoá nằm trong Pipeline: fit trên từng fold huấn luyện, tránh rò rỉ.")
numbered("Hạt giống cố định: seed 42 ở mọi thủ tục ngẫu nhiên.")
page_break()

# ============================ CHAPTER 3 ============================
doc.add_heading("CHƯƠNG 3. PHƯƠNG PHÁP VÀ KIẾN TRÚC THỰC HIỆN", level=1)
doc.add_heading("3.1. Quy trình tổng thể", level=2)
para("Quy trình gồm sáu giai đoạn theo hướng một đầu vào chuẩn - nhiều nhánh phân tích - tổng hợp có kiểm soát. Hai cổng chất lượng bắt buộc: GATE #1 (S-T1) thống nhất đầu vào chuẩn và GATE #2 (S-T2) kiểm tra nhất quán toàn bộ số liệu trước khi tổng hợp.")
figure("pipeline_diagram.png", "Hình 3.1. Sơ đồ quy trình khai phá dữ liệu và các cổng kiểm soát", 15.8)
doc.add_heading("3.2. Dữ liệu và chuẩn hoá đầu vào", level=2)
para("Dữ liệu thô là tệp D07 - parkinsons.data.xlsx (Oxford Parkinson's Disease Detection, UCI), 195 bản ghi × 24 cột gồm 22 đặc trưng, nhãn status và cột định danh name. Nhóm loại bỏ cột name (thông tin cá nhân), giữ nguyên 22 đặc trưng định lượng.")
para("Canonical CSV v1: data/processed/parkinsons_v1.csv - 195 dòng × 23 cột; SHA-256: 55e2fed63eb74ad19a119b43ef33d92c60d60f7d6751688f1cae45d38d358153. SHA-256 tệp thô: d5d96457a760cd06e93b1a1d1cd6380b38909c2cc82121968bb51ef29f80029a.")
doc.add_heading("3.3. Kiến trúc thực hiện", level=2)
make_table(
    ["Đường dẫn", "Vai trò"],
    [
        ["data/raw/", "Dữ liệu thô và manifest nguồn"],
        ["data/processed/", "Canonical CSV v1 và schema"],
        ["notebooks/", "5 notebook phân tích có lần lượt M01-M06"],
        ["src/", "Hàm dùng chung và pipeline tổng hợp (pipeline.py)"],
        ["results/", "Báo cáo, bảng số liệu, hình ảnh, pipeline_summary.json"],
        ["reports/", "Báo cáo tổng hợp cuối cùng"],
        ["workspaces/member-XX/", "Không gian làm việc của từng thành viên"],
    ],
    widths=[5.0, 10.5],
)
caption("Bảng 3.1. Cấu trúc chính của kho lưu trữ")
para("Pipeline tổng hợp chạy bằng lệnh python -m src.pipeline, ghi results/pipeline_summary.json để đối chiếu chéo.")
doc.add_heading("3.4. Quản lý công việc và đảm bảo chất lượng", level=2)
para("Nhóm áp dụng luồng Git theo nhánh: mỗi nhiệm vụ tạo nhánh riêng, mở pull request về main, review và tag thành viên liên quan, chỉ nhập nhánh sau khi đạt. PR đã merge: #5 (khám phá), #7 (tiền xử lý-PCA), #8 (phân loại), #13 (thống kê/chất lượng), #14 (phân cụm), #16 (tổng hợp), #17 (chốt gate). TASK_BOARD.md báo 21/21 nhiệm vụ Done; GATE #1 và #2 đã ký.")
make_table(
    ["Mã", "Họ và tên", "Mô-đun / minh chứng nghiệm thu"],
    [
        ["M01", "Đặng Hoàng Ân", "Dữ liệu, pipeline tổng hợp; ký GATE #1, GATE #2"],
        ["M02", "Lê Thiên Lộc", "M02-T1..T3; PR #5 đạt review"],
        ["M03", "Huỳnh Gia Hợp", "M03-T1..T3; PR #13 đạt review"],
        ["M04", "Trần Hoàng Thông", "M04-T1..T3; PR #7 đã merge"],
        ["M05", "Ngô Thị Anh Thư", "M05-T1..T3; PR #8 đạt review"],
        ["M06", "Nguyễn Hoàng Bách", "M06-T1..T3; PR #14, PR #16 đạt review"],
    ],
    widths=[1.4, 4.4, 9.7],
)
caption("Bảng 3.2. Phân công theo mô-đun và nghiệm thu")
doc.add_heading("3.5. Môi trường thực nghiệm", level=2)
make_table(
    ["Thành phần", "Phiên bản / giá trị"],
    [
        ["Python", "3.14.0"],
        ["numpy / pandas / scipy", "2.4.2 / 3.0.3 / 1.17.1"],
        ["scikit-learn", "1.9.0"],
        ["matplotlib / seaborn", "3.10.8 / 0.13.2"],
        ["Jupyter (nbformat, nbclient, nbconvert)", "5.11.1 / 0.11.0 / 7.17.2"],
        ["Hạt giống ngẫu nhiên", "42"],
        ["Kiểm định chéo", "StratifiedKFold 10 (ngoài), GridSearchCV 5 (trong)"],
        ["Độ đo chính", "F-score macro (phân loại), ARI (phân cụm)"],
    ],
    widths=[7.0, 8.5],
)
caption("Bảng 3.3. Môi trường thực nghiệm")
doc.add_heading("3.6. Phương pháp đánh giá", level=2)
para("Phân loại báo cáo trung bình ± độ lệch chuẩn F-score macro trên 10 fold, kèm F-score weighted và điểm huấn luyện. Phân cụm chọn K theo silhouette, so cụm với nhãn bằng ARI; DBSCAN chọn eps theo điểm uốn k-distance và kiểm tra chéo trên lưới tham số. Mọi kết quả ghi đầy đủ trong results/ kèm tham số, seed và phiên bản thư viện.")
page_break()

# ============================ CHAPTER 4 ============================
doc.add_heading("CHƯƠNG 4. KẾT QUẢ THỰC NGHIỆM", level=1)
doc.add_heading("4.1. Khám phá và chất lượng dữ liệu", level=2)
make_table(
    ["Hạng mục", "Giá trị"],
    [
        ["Số mẫu × số cột", "195 × 23 (22 feature + status)"],
        ["Giá trị thiếu / dòng trùng lặp", "0 / 0"],
        ["Nhãn status=0 (khỏe)", "48 mẫu (24,62%)"],
        ["Nhãn status=1 (Parkinson)", "147 mẫu (75,38%)"],
        ["Feature có candidate outlier (IQR)", "19 / 22"],
        ["Mẫu có ít nhất một candidate outlier", "47 / 195 (24,10%)"],
    ],
    widths=[8.0, 7.5],
)
caption("Bảng 4.1. Tổng quan dữ liệu canonical v1")
para("Dữ liệu sạch về thiếu/trùng nhưng nhãn mất cân bằng và thang đo chênh lệch lớn (từ 7×10⁻⁶ đến hàng trăm Hz), nên chuẩn hoá là bắt buộc.")
figure("eda_summary.png", "Hình 4.1. Phân bố nhãn status và các đặc trưng có nhiều candidate outlier theo IQR", 15.5)
para("Theo IQR hệ số 1,5: NHR 19 điểm (9,74%), MDVP:PPQ 15, MDVP:RAP/Jitter:DDP/MDVP:Jitter(%) 14 mỗi cột, Shimmer:APQ5 13; ba feature không có candidate outlier là MDVP:Fo(Hz), RPDE, DFA. Nhóm giữ nguyên và kiểm soát, không loại bỏ mù quáng. 14/22 feature có |skew| > 1; NHR có skew 4,2207 và kurtosis 21,9950. 26/231 cặp feature có |r| ≥ 0,9; Jitter:DDP ≈ 3×MDVP:RAP và Shimmer:DDA ≈ 3×Shimmer:APQ3 với r = 1,0.")
doc.add_heading("4.2. Tiền xử lý và phân tích thành phần chính", level=2)
para("Ma trận chuẩn hoá X_s có kích thước 195 × 22, mean gần 0, std gần 1, không NaN. Chuẩn hoá trên toàn bộ X chỉ dùng cho PCA/phân cụm; trong phân loại scaler nằm trong Pipeline.")
make_table(
    ["Thành phần", "Tỷ lệ phương sai giải thích"],
    [
        ["PC1", "58,9%"],
        ["PC2", "11,3%"],
        ["PC1 + PC2", "70,2%"],
        ["Thành phần đạt ngưỡng ≥ 90%", "6 (tích luỹ 91,61%)"],
    ],
    widths=[7.0, 8.5],
)
caption("Bảng 4.2. Phương sai giải thích của PCA")
figure("pca_scatter.png", "Hình 4.2. Scatter PC1-PC2 tô theo status", 11.5)
figure("histograms.png", "Hình 4.3. Histogram 22 feature theo status", 13.5)
figure("corr_heatmap.png", "Hình 4.4. Ma trận tương quan Pearson giữa các feature", 13.5)
para("Hai thành phần đầu giữ 70,2% phương sai; đạt ngưỡng 90% cần 6 thành phần (91,61%). Hai nhóm tách một phần nhưng chồng lấn đáng kể trên PC1-PC2; một số feature phi tuyến (RPDE, DFA, PPE) tách biệt hơn.")
doc.add_heading("4.3. Phân loại có giám sát", level=2)
para("Thiết lập: StratifiedKFold ngoài 10 (seed 42), GridSearchCV 5 trong tập huấn luyện; lưới KNN n_neighbors ∈ {3,5,7}, SVM C ∈ {0,1; 1; 10}, RF n_estimators ∈ {50; 100}; scaler trong Pipeline.")
make_table(
    ["Mô hình", "F-score macro (test)", "F-score weighted (test)", "F-score macro (train)"],
    [
        ["KNN", "0,8757 ± 0,0742", "0,9073 ± 0,0578", "0,9647"],
        ["SVM", "0,8904 ± 0,0804", "0,9199 ± 0,0603", "0,9787"],
        ["Random Forest", "0,8737 ± 0,1171", "0,9103 ± 0,0824", "1,0000"],
    ],
    widths=[3.6, 3.9, 4.1, 3.9],
)
caption("Bảng 4.3. F-score trên 10-fold CV (mean ± std)")
figure("f1_scores.png", "Hình 4.5. F-score macro và weighted trên 10-fold CV cho ba mô hình", 13.0)
para("Ba mô hình đạt F-score macro trên 0,87. SVM cao nhất (0,8904) nhưng chênh lệch giữa các mô hình (~0,016) nhỏ hơn độ lệch chuẩn giữa fold (0,07-0,12), nên không kết luận một mô hình tốt nhất chắc chắn. F-score weighted cao hơn macro do lớp khỏe ít mẫu. Random Forest có train 1,0000 và std lớn nhất, dấu hiệu quá khớp.")
doc.add_heading("4.4. Phân cụm không giám sát và đánh giá ARI", level=2)
make_table(
    ["K", "Inertia", "Silhouette", "Kích thước cụm", "ARI"],
    [
        ["2", "2817,2", "0,4373", "[165, 30]", "-0,0978"],
        ["3", "2076,2", "0,2763", "[106, 77, 12]", "0,0582"],
        ["4", "1822,4", "0,2358", "[91, 77, 23, 4]", "0,0583"],
        ["5", "1595,5", "0,2048", "[73, 64, 32, 22, 4]", "0,1000"],
        ["6", "1442,0", "0,2138", "[60, 51, 30, 28, 22, 4]", "0,1058"],
        ["7", "1319,8", "0,2094", "[54, 51, 31, 24, 23, 8, 4]", "0,0882"],
        ["8", "1230,5", "0,2201", "[53, 35, 32, 23, 23, 15, 10, 4]", "0,0313"],
        ["9", "1157,0", "0,2265", "[52, 39, 25, 24, 21, 13, 9, 8, 4]", "0,0574"],
        ["10", "1110,7", "0,1896", "[38, 35, 26, 23, 22, 18, 12, 9, 8, 4]", "0,0481"],
    ],
    widths=[1.2, 2.2, 2.6, 6.5, 2.6],
    font_size=9.5,
)
caption("Bảng 4.4. Kết quả K-Means và ARI so với status")
para("Silhouette đạt cực đại tại K = 2 (0,4373) nhưng ARI chỉ -0,0978; trên toàn dải K, ARI nằm trong [-0,0978; 0,1058]. Cụm nhỏ 30 mẫu nằm lệch về phía PC1 dương, nhiều khả năng là nhóm biên độ cao thay vì nhóm khỏe mạnh.")
figure("kmeans_selection.png", "Hình 4.6. Đánh giá K-Means: inertia, silhouette và kích thước cụm theo K", 15.0)
para("Với min_samples = 5, điểm uốn k-distance tại ε = 3,37. DBSCAN tạo một cụm gồm 183 điểm và 12 điểm nhiễu, ARI -0,0639. Lưới tham số (ε ∈ {1,5; 2,0; 2,5; 3,0; 3,5; 4,0; 5,0}, min_samples ∈ {3; 5; 10}) cho ARI ∈ [-0,0744; 0,1625]; giá trị 0,1625 đạt khi ε = 1,5, min_samples = 5 nhưng 149/195 điểm là nhiễu, không có ý nghĩa phân cụm. Mật độ điểm phân bố liên tục, không hình thành vùng mật độ tách biệt ứng với hai lớp.")
figure("dbscan_analysis.png", "Hình 4.7. Phân tích DBSCAN: k-distance, cụm/nhiễu và ARI theo tham số", 15.0)
doc.add_heading("4.5. Đối chiếu tổng hợp", level=2)
make_table(
    ["Câu hỏi", "Kết quả chính", "Nhận xét"],
    [
        ["RQ1", "0 NaN/trùng; 19/22 feature có outlier IQR; 47/195 mẫu; nhãn 147/48; 14/22 feature lệch mạnh", "Dữ liệu sạch nhưng lệch nhãn/thang đo; cần chuẩn hoá và CV phân tầng"],
        ["RQ2", "F-score macro 0,8757 (KNN), 0,8904 (SVM), 0,8737 (RF); RF dấu hiệu quá khớp", "Phân loại đạt tốt; chênh lệch mô hình nhỏ so với biến động fold"],
        ["RQ3", "K-Means K=2 silhouette 0,4373 nhưng ARI -0,0978; DBSCAN 1 cụm, 12 nhiễu, ARI -0,0639", "Cấu trúc cụm không khớp status; bệnh lý cần mô hình có giám sát"],
    ],
    widths=[1.6, 7.2, 6.7],
    font_size=10,
)
caption("Bảng 4.5. Đối chiếu câu hỏi nghiên cứu với kết quả")
page_break()

# ============================ CHAPTER 5 ============================
doc.add_heading("CHƯƠNG 5. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN", level=1)
doc.add_heading("5.1. Kết luận", level=2)
para("RQ1: bộ dữ liệu canonical 195 × 23, không thiếu/trùng; nhãn mất cân bằng (147/48), thang đo chênh lệch, 19/22 feature có candidate outlier, 47/195 mẫu chứa outlier, 14/22 feature lệch mạnh. Nhóm áp dụng chuẩn hoá z-score và kiểm định chéo phân tầng.")
para("RQ2: F-score macro 0,8757 (KNN), 0,8904 (SVM), 0,8737 (Random Forest) trên 10-fold CV; SVM cao nhất nhưng chênh lệch giữa các mô hình nhỏ so với biến động giữa fold; Random Forest dấu hiệu quá khớp (train 1,0000). Tín hiệu giọng nói mang thông tin phân biệt bệnh lý ở mức tốt.")
para("RQ3: K-Means chọn K=2 theo silhouette (0,4373) nhưng ARI -0,0978; DBSCAN ε = 3,37, min_samples = 5 cho một cụm lớn, 12 điểm nhiễu, ARI -0,0639. Cấu trúc cụm không khớp ranh giới bệnh lý; phân cụm đóng vai trò đối chiếu.")
para("Ngoài kết quả kỹ thuật, đề tài rèn được quy trình làm việc nhóm: quản lý mã nguồn theo nhánh, review từng PR, đóng băng đầu vào chuẩn và chốt hai cổng GATE.")
doc.add_heading("5.2. Hạn chế", level=2)
bullet("Mẫu nhỏ (195 bản ghi, khoảng 32 chủ thể) và mất cân bằng nhãn; mỗi fold test khoảng 20 mẫu, khoảng 5 mẫu lớp khỏe.")
bullet("Cột name đã loại khỏi canonical CSV nên chưa kiểm định chéo theo nhóm chủ thể; bản ghi cùng người có thể rơi vào cả train/test.")
bullet("PCA 2D chỉ giữ 70,2% phương sai; phân cụm không tách được cấu trúc khớp nhãn; DBSCAN chỉ một cụm lớn.")
bullet("Mới so sánh ba mô hình với lưới nhỏ; chưa tinh chỉnh ngưỡng, chưa có tập kiểm định độc lập.")
bullet("Một số thành viên chạy trên phiên bản thư viện khác nhau; số liệu khớp khi kiểm tra chéo nhưng cần ghi rõ môi trường.")
doc.add_heading("5.3. Hướng phát triển", level=2)
bullet("Bổ sung đặc trưng/lựa chọn đặc trưng, thử nghiệm mô hình mới; dùng GroupKFold theo chủ thể để khắc phục rò rỉ.")
bullet("Điều chỉnh ngưỡng, class-weight phù hợp mục tiêu sàng lọc; đánh giá calibration, độ nhạy, độ đặc hiệu.")
bullet("Học bán giám sát hoặc học sâu trên âm thanh thô; xây dựng giao diện minh hoạ pipeline.")
bullet("Hoàn thiện tái lập: khóa phiên bản, kiểm tra tự động đầu vào/đầu ra, chạy một lệnh.")
doc.add_heading("5.4. Đóng góp của nhóm và nghiệm thu", level=2)
para("Toàn bộ 21 nhiệm vụ đã hoàn thành và nghiệm thu Done; hai cổng GATE #1 và GATE #2 đã ký. PR đã merge: #5, #7, #8, #13, #14, #16, #17.")
make_table(
    ["Mã", "Thành viên", "Trạng thái / bằng chứng"],
    [
        ["M01", "Đặng Hoàng Ân", "Hoàn thành; ký GATE #1, GATE #2"],
        ["M02", "Lê Thiên Lộc", "Hoàn thành; PR #5 đạt review"],
        ["M03", "Huỳnh Gia Hợp", "Hoàn thành; PR #13 đạt review"],
        ["M04", "Trần Hoàng Thông", "Hoàn thành; PR #7 đã merge"],
        ["M05", "Ngô Thị Anh Thư", "Hoàn thành; PR #8 đạt review"],
        ["M06", "Nguyễn Hoàng Bách", "Hoàn thành; PR #14, #16 đạt review"],
    ],
    widths=[1.4, 4.4, 9.7],
)
caption("Bảng 5.1. Trạng thái nghiệm thu của từng thành viên")
page_break()

# ============================ REFERENCES ============================
doc.add_heading("TÀI LIỆU THAM KHẢO", level=1)
refs = [
    "[1] M. A. Little, P. E. McSharry, E. J. Hunter, J. Spielman, and L. O. Ramig, “Suitability of dysphonia measurements for telemonitoring of Parkinson's disease,” IEEE Transactions on Biomedical Engineering, vol. 56, no. 4, pp. 1015-1022, 2009.",
    "[2] UCI Machine Learning Repository, “Parkinson's Disease Detection / Oxford Parkinson's Dataset.\" Truy cập: https://archive.ics.uci.edu/ml/datasets/parkinsons (tháng 11 năm 2026).",
    "[3] I. T. Jolliffe, Principal Component Analysis, 2nd ed. New York: Springer, 2002.",
    "[4] G. James, D. Witten, T. Hastie, and R. Tibshirani, An Introduction to Statistical Learning: With Applications in R. New York: Springer, 2013.",
    "[5] J. Han, M. Kamber, and J. Pei, Data Mining: Concepts and Techniques, 3rd ed. Waltham, MA: Morgan Kaufmann, 2011.",
    "[6] M. Ester, H.-P. Kriegel, J. Sander, and X. Xu, “A density-based algorithm for discovering clusters in large spatial databases with noise,” Proc. KDD-96, pp. 226-231, 1996.",
]
for r in refs:
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(6)
    rich(p, r, size=12)
page_break()

# ============================ APPENDIX A ============================
doc.add_heading("PHỤ LỤC A. KHO LƯU TRỮ, CẤU TRÚC VÀ CÁCH TÁI LẬP", level=1)
para("Kho lưu trữ: ", )
p = doc.paragraphs[-1]
add_hyperlink(p, "https://github.com/KaiyoDev/Nhom_3_KhaiThacDuLieu_Parkinsons", "https://github.com/KaiyoDev/Nhom_3_KhaiThacDuLieu_Parkinsons")
para("Nhánh main chứa sản phẩm đã nghiệm thu; PR #5, #7, #8, #13, #14, #16, #17 ghi nhận lịch sử thay đổi.")
make_table(
    ["Đường dẫn", "Nội dung"],
    [
        ["data/raw/", "Tệp thô D07 - parkinsons.data.xlsx, manifest"],
        ["data/processed/", "parkinsons_v1.csv (canonical), schema_v1.md"],
        ["notebooks/", "01 exploration, 02 preprocessing+PCA, 03 classification, 04 clustering, 05 integration report"],
        ["src/", "preprocessing.py, pipeline.py"],
        ["results/", "Báo cáo, bảng số liệu CSV, hình ảnh, pipeline_summary.json"],
        ["reports/summary.md", "Báo cáo tổng hợp đa nhiệm vụ"],
    ],
    widths=[4.5, 11.0],
)
caption("Bảng A.1. Cấu trúc thư mục chính")
para("Cách tái lập (trong thư mục gốc):")
for cmd in ["pip install -r requirements.txt",
            "python -m src.pipeline          # ghi results/pipeline_summary.json",
            "jupyter nbconvert -to notebook -execute notebooks/05_integration_report.ipynb"]:
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.8)
    rich(p, cmd, size=11.5)
para("Quy ước: seed 42; CV ngoài 10, trong 5; StandardScaler; F-score macro và ARI; PCA 2 thành phần để trực quan hoá, 6 thành phần để đạt ≥ 90% phương sai.")
make_table(
    ["Mã", "Họ và tên", "MSSV", "Tài khoản GitHub"],
    [
        ["M01", "Đặng Hoàng Ân", "080206014982", "@KaiyoDev"],
        ["M02", "Lê Thiên Lộc", "079306040024", "@Phiadz"],
        ["M03", "Huỳnh Gia Hợp", "054205008367", "@HGiaHop"],
        ["M04", "Trần Hoàng Thông", "075206008044", "@HoangThongTom"],
        ["M05", "Ngô Thị Anh Thư", "087306008195", "@THUNGO-dot"],
        ["M06", "Nguyễn Hoàng Bách", "056205005522", "@nguyenhoangbach1"],
    ],
    widths=[1.4, 4.4, 3.4, 5.4],
)
caption("Bảng A.2. Thông tin nhóm")
page_break()

# ============================ APPENDIX B ============================
doc.add_heading("PHỤ LỤC B. BẢNG THỐNG KÊ CHI TIẾT", level=1)
doc.add_heading("B.1. Thống kê mô tả 22 đặc trưng", level=2)
stats_rows = [
    ["MDVP:Fo(Hz)", "154,229", "148,79", "41,3901", "88,333", "260,105", "0,5917", "-0,6279"],
    ["MDVP:Fhi(Hz)", "197,105", "175,829", "91,4915", "102,145", "592,03", "2,5421", "7,6272"],
    ["MDVP:Flo(Hz)", "116,325", "104,315", "43,5214", "65,476", "239,17", "1,2174", "0,6546"],
    ["MDVP:Jitter(%)", "0,0062", "0,0049", "0,0048", "0,0017", "0,0332", "3,0849", "12,0309"],
    ["MDVP:Jitter(Abs)", "0,0000", "0,0000", "0,0000", "0,0000", "0,0003", "2,6491", "10,8690"],
    ["MDVP:RAP", "0,0033", "0,0025", "0,0030", "0,0007", "0,0214", "3,3607", "14,2138"],
    ["MDVP:PPQ", "0,0034", "0,0027", "0,0028", "0,0009", "0,0196", "3,0739", "11,9639"],
    ["Jitter:DDP", "0,0099", "0,0075", "0,0089", "0,0020", "0,0643", "3,3621", "14,2248"],
    ["MDVP:Shimmer", "0,0297", "0,0230", "0,0189", "0,0095", "0,1191", "1,6665", "3,2383"],
    ["MDVP:Shimmer(dB)", "0,2823", "0,2210", "0,1949", "0,0850", "1,3020", "1,9994", "5,1282"],
    ["Shimmer:APQ3", "0,0157", "0,0128", "0,0102", "0,0046", "0,0565", "1,5806", "2,7202"],
    ["Shimmer:APQ5", "0,0179", "0,0135", "0,0120", "0,0057", "0,0794", "1,7987", "3,8742"],
    ["MDVP:APQ", "0,0241", "0,0183", "0,0169", "0,0072", "0,1378", "2,6180", "11,1633"],
    ["Shimmer:DDA", "0,0470", "0,0384", "0,0305", "0,0136", "0,1694", "1,5806", "2,7207"],
    ["NHR", "0,0248", "0,0117", "0,0404", "0,0006", "0,3148", "4,2207", "21,9950"],
    ["HNR", "21,8860", "22,0850", "4,4258", "8,4410", "33,0470", "-0,5143", "0,6160"],
    ["RPDE", "0,4985", "0,4960", "0,1039", "0,2566", "0,6852", "-0,1434", "-0,9218"],
    ["DFA", "0,7181", "0,7223", "0,0553", "0,5743", "0,8253", "-0,0332", "-0,6862"],
    ["spread1", "-5,6844", "-5,7209", "1,0902", "-7,9650", "-2,4340", "0,4321", "-0,0502"],
    ["spread2", "0,2265", "0,2189", "0,0834", "0,0063", "0,4505", "0,1444", "-0,0830"],
    ["D2", "2,3818", "2,3615", "0,3828", "1,4233", "3,6712", "0,4304", "0,2203"],
    ["PPE", "0,2066", "0,1941", "0,0901", "0,0445", "0,5274", "0,7975", "0,5283"],
]
make_table(
    ["Feature", "mean", "median", "std", "min", "max", "skew", "kurtosis"],
    stats_rows,
    widths=[3.0, 1.8, 1.8, 1.7, 1.7, 1.8, 1.6, 1.8],
    font_size=9.5,
)
caption("Bảng B.1. Thống kê mô tả 22 đặc trưng")
doc.add_heading("B.2. Kiểm tra candidate outlier theo IQR", level=2)
iqr_rows = [
    ["MDVP:Fo(Hz)", "117,572", "182,769", "65,197", "0", "0,00"],
    ["MDVP:Fhi(Hz)", "134,863", "224,206", "89,343", "11", "5,64"],
    ["MDVP:Flo(Hz)", "84,291", "140,018", "55,7275", "9", "4,62"],
    ["MDVP:Jitter(%)", "0,0035", "0,0074", "0,0039", "14", "7,18"],
    ["MDVP:Jitter(Abs)", "0,0000", "0,0001", "0,0000", "7", "3,59"],
    ["MDVP:RAP", "0,0017", "0,0038", "0,0022", "14", "7,18"],
    ["MDVP:PPQ", "0,0019", "0,0040", "0,0021", "15", "7,69"],
    ["Jitter:DDP", "0,0050", "0,0115", "0,0065", "14", "7,18"],
    ["MDVP:Shimmer", "0,0165", "0,0379", "0,0214", "8", "4,10"],
    ["MDVP:Shimmer(dB)", "0,1485", "0,3500", "0,2015", "10", "5,13"],
    ["Shimmer:APQ3", "0,0082", "0,0203", "0,0120", "6", "3,08"],
    ["Shimmer:APQ5", "0,0096", "0,0224", "0,0128", "13", "6,67"],
    ["MDVP:APQ", "0,0131", "0,0294", "0,0163", "12", "6,15"],
    ["Shimmer:DDA", "0,0247", "0,0608", "0,0361", "6", "3,08"],
    ["NHR", "0,0059", "0,0256", "0,0197", "19", "9,74"],
    ["HNR", "19,1980", "25,0755", "5,8775", "3", "1,54"],
    ["RPDE", "0,4213", "0,5876", "0,1663", "0", "0,00"],
    ["DFA", "0,6748", "0,7619", "0,0871", "0", "0,00"],
    ["spread1", "-6,4501", "-5,0462", "1,4039", "4", "2,05"],
    ["spread2", "0,1744", "0,2792", "0,1049", "2", "1,03"],
    ["D2", "2,0991", "2,6365", "0,5373", "1", "0,51"],
    ["PPE", "0,1375", "0,2530", "0,1155", "5", "2,56"],
]
make_table(
    ["Feature", "Q1", "Q3", "IQR", "Số outlier", "Tỷ lệ (%)"],
    iqr_rows,
    widths=[3.6, 2.2, 2.2, 2.2, 2.6, 2.6],
    font_size=9.5,
)
caption("Bảng B.2. Candidate outlier theo quy tắc IQR (hệ số 1,5)")

out = DIST / "BaoCao_BaiTapLon_Nhom3.docx"
doc.save(out)
print("Saved:", out)
