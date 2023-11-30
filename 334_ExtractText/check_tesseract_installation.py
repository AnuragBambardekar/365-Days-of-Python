import pytesseract
import cv2
from matplotlib import pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
img = cv2.imread(r"images\\capture.png")
cv2.imshow("window",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Display the image using matplotlib
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.show()

text = pytesseract.image_to_string(img)
print(text)