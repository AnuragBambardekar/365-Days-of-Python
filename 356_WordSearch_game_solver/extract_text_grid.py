from pytesseract import pytesseract
import PIL.Image
import cv2

windows_path = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
pytesseract.tesseract_cmd = windows_path
myconfig = r"--psm 6 --oem 3"
text = pytesseract.image_to_string(PIL.Image.open("planets.jpeg"), config=myconfig)
# print(text)

# Split the text into lines
lines = text.split('\n')

# Store characters with spaces between them
spaced_text = []
for line in lines:
    spaced_line = ' '.join(line)
    spaced_text.append(spaced_line)

# Display the spaced text
for line in spaced_text:
    print(line)