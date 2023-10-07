"""
pip install python-barcode
"""

import barcode
from barcode import generate

code = '123456789'
barcode_class = barcode.get_barcode_class('code128')
generated_barcode = barcode_class(code, writer=barcode.writer.ImageWriter())

generated_barcode.save('generated_barcode')
