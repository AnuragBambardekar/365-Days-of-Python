from pytesseract import pytesseract
import PIL.Image
import cv2

windows_path = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
pytesseract.tesseract_cmd = windows_path
myconfig = r"--psm 6 --oem 3"

# img = cv2.imread("images/text.png")
img = cv2.imread("images/logos.jpg")
height, width, _ = img.shape

boxes = pytesseract.image_to_boxes(img, config=myconfig)
for box in boxes.splitlines():
    box = box.split(" ")
    x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    img = cv2.rectangle(img, (x, height - h), (w, height - y), (0, 255, 0), 2)


cv2.imshow("img", img)
cv2.waitKey(0)