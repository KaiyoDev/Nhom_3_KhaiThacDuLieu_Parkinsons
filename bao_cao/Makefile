# ==============================================================
#  BÁO CÁO BÀI TẬP LỚN - NHÓM 3 (Parkinson)
# ==============================================================

PDF_OUT   = dist/BaoCao_BaiTapLon_Nhom3.pdf
DOCX_OUT  = dist/BaoCao_BaiTapLon_Nhom3.docx

.PHONY: all pdf docx notebook clean

all: pdf docx

pdf:
	pdflatex -interaction=nonstopmode main.tex
	bibtex main
	pdflatex -interaction=nonstopmode main.tex
	pdflatex -interaction=nonstopmode main.tex
	cp main.pdf $(PDF_OUT)

docx:
	python scripts/build_docx.py

notebook:
	jupyter nbconvert --to pdf ../notebooks/05_integration_report.ipynb \
		--output-dir dist --output BaoCao_Notebook05_Parkinson

clean:
	rm -f main.aux main.bbl main.blg main.lof main.lot main.log main.out main.toc
	rm -rf qa
