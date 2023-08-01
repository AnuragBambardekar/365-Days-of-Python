# pip install tabula-py

import tabula

tables = tabula.read_pdf("215_Extract_Content_from_PDF/sample2.pdf", pages="all")
print(type(tables[1]))
print(tables[1])

df = tables[1]
print(df)

print(df[df.Age > 29])