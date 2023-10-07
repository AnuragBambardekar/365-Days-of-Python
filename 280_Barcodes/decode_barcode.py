from pyzbar.pyzbar import decode
from PIL import Image

image = Image.open('280_Barcodes/generated_barcode.png')

# Decode the barcode
decoded_objects = decode(image)

for obj in decoded_objects:
    barcode_data = obj.data.decode('utf-8')
    barcode_type = obj.type
    print(f"Type: {barcode_type}, Data: {barcode_data}")
