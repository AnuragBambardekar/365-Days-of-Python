import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
img = cv2.imread(r"311_Smart_SnippingTool\\capture.png")
cv2.imshow("window",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

text = pytesseract.image_to_string(img)
print(text)