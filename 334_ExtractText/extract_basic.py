from PIL import Image
from pytesseract import pytesseract
import enum

class OS(enum.Enum):
    Mac = 0
    Windows = 1

class Language(enum.Enum):
    ENG = 'eng'
    RUS = 'rus'
    ITA = 'ita'
    HIN = 'hin'
    HIN_ENG = 'hin+eng'

class ImageReader:
    def __init__(self, os: OS) -> None:
        if os == OS.Mac:
            print("Running on MAC\n")
        if os == OS.Windows:
            windows_path = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
            pytesseract.tesseract_cmd = windows_path
            print("Running on Windows\n")

    def extract_text(self, image: str, lang: Language) -> str:
        img = Image.open(image)
        extracted_text = pytesseract.image_to_string(img, lang=lang.value)
        return extracted_text

if __name__ == "__main__":
    ir = ImageReader(OS.Windows)
    # text = ir.extract_text('images/test.jpg', lang='eng')
    # print(text)
    
    # https://github.com/indic-ocr/tessdata
    text = ir.extract_text('images/test_hindi.jpg', lang=Language.HIN)
    print(text)