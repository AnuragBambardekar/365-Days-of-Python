from pytesseract import pytesseract
import PIL.Image
import cv2

windows_path = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
pytesseract.tesseract_cmd = windows_path
myconfig = r"--psm 6 --oem 3"
text = pytesseract.image_to_string(PIL.Image.open("planets_to_find.jpeg"), config=myconfig)
# print(text)

# Split the text into lines
lines = text.split('\n')

# Display the spaced text
for line in lines:
    planets = line.split()
    for planet in planets:
        print(planet)