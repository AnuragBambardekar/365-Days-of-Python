import cv2
import qrcode

def decode_qr_code(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create a QRCodeDetector object
    qr_code_detector = cv2.QRCodeDetector()

    # Detect and decode the QR code
    retval, decoded_info, points, straight_qrcode = qr_code_detector.detectAndDecodeMulti(gray_image)

    if retval:
        return decoded_info
    else:
        return None

if __name__ == "__main__":
    image_path = "102_Two_Factor_Authentication/new_QR.png"

    decoded_data = decode_qr_code(image_path)

    if decoded_data is not None:
        print("Decoded QR Code data:", decoded_data)
    else:
        print("No QR Code found or could not be decoded.")
