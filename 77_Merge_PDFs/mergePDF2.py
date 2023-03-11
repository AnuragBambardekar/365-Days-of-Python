# pip install pyPDF2
from PyPDF2 import PdfMerger

merger = PdfMerger()

merger.append("77_Merge_PDFs/one.pdf")
merger.append("77_Merge_PDFs/two.pdf")
merger.append("77_Merge_PDFs/three.pdf", pages=(0,4,2)) # page 0 to 4 with step size 2


merger.write("77_Merge_PDFs/merged2.pdf")
merger.close()