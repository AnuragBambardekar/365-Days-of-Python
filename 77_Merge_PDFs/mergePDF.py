# pip install pyPDF2
from PyPDF2 import PdfMerger

pdfs = ["77_Merge_PDFs/one.pdf", "77_Merge_PDFs/two.pdf", "77_Merge_PDFs/three.pdf"]
# Can also change the order

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("77_Merge_PDFs/merged.pdf")
merger.close()