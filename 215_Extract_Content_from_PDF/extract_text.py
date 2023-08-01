# pip install pdfminer.six

import re
from pdfminer.high_level import extract_pages, extract_text

# Extract individual elements
# for page_layout in extract_pages("215_Extract_Content_from_PDF/sample.pdf"):
#     for element in page_layout:
#         print(element)

text = extract_text("215_Extract_Content_from_PDF/sample.pdf")
print(text)

pattern = re.compile(r"[a-zA-Z]+,{1}\s{1}")
matches = pattern.findall(text)
print(matches)

names = [n[:-2] for n in matches]
print(names)