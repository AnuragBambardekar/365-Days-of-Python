import barcode
from barcode import generate
from barcode.writer import ImageWriter

# Data for each barcode
barcode_data = {
    "Code39": "CODE39BARCODE",
    "Code128": "CODE128BARCODE",
    "EAN-13": "123456789012",
    "EAN-8": "12345670",
    "JAN": "4901234567890",  # Valid Japanese country code (490)
    "ISBN-13": "9780123456789",
    "UPC-A": "01234567890",
    "EAN14": "12345678901234",
    "GS1-128": "12345678901234",
}

# Generate barcodes and save them as PNG images
for symbology, data in barcode_data.items():
    try:
        if symbology == "EAN-13":
            barcode_class = barcode.ean.EuropeanArticleNumber13
        elif symbology == "EAN-8":
            barcode_class = barcode.ean.EuropeanArticleNumber8
        elif symbology == "JAN":
            barcode_class = barcode.ean.JapanArticleNumber
        elif symbology == "ISBN-13":
            barcode_class = barcode.isxn.InternationalStandardBookNumber13
        elif symbology == "UPC-A":
            barcode_class = barcode.upc.UniversalProductCodeA
        elif symbology == "GS1-128":
            barcode_class = barcode.codex.Gs1_128
        else:
            barcode_class = barcode.get_barcode_class(symbology)

        generated_barcode = barcode_class(data, writer=ImageWriter())
        generated_barcode.save(f"{symbology}.png")
        print(f"Generated {symbology} barcode.")
    except Exception as e:
        print(f"Error generating {symbology} barcode: {e}")

# For unsupported symbologies like PZN7, ISBN-10, and ISSN, consider using other libraries or online tools.
