"""
Page Segmentation modes:
  0    Orientation and script detection (OSD) only.
  1    Automatic page segmentation with OSD.
  2    Automatic page segmentation, but no OSD, or OCR. (not implemented)
  3    Fully automatic page segmentation, but no OSD. (Default)
  4    Assume a single column of text of variable sizes.
  5    Assume a single uniform block of vertically aligned text.
  6    Assume a single uniform block of text.
  7    Treat the image as a single text line.
  8    Treat the image as a single word.
  9    Treat the image as a single word in a circle.
 10    Treat the image as a single character.
 11    Sparse text. Find as much text as possible in no particular order.
 12    Sparse text with OSD.
 13    Raw line. Treat the image as a single text line,
       bypassing hacks that are Tesseract-specific.

OCR Engine mode:
  0    Legacy Engine only
  1    Neural nets LSTM engine only
  2    Legacy + LSTM engines
  3    Default, based on what is available
"""

from pytesseract import pytesseract
import PIL.Image
import cv2

windows_path = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
pytesseract.tesseract_cmd = windows_path
myconfig = r"--psm 6 --oem 3"
text = pytesseract.image_to_string(PIL.Image.open("images/text.png"), config=myconfig)
print(text)
