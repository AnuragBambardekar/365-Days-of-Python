import cv2
import numpy as np
import pyautogui

while True:
    """
    left is 200 pixels from the left side of the screen.
    top is 550 pixels from the top of the screen.
    width is 255 pixels.
    height is 250 pixels.
    """
    image = pyautogui.screenshot(region = (200,550,255,250))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # count the pixels
    black_pixel_count = np.sum(image<100) # if any pixel val < 100 --> black pixel
    white_pixel_count = np.sum(image>100) # if any pixel val > 100 --> white pixel

    print("# Black pixels: ", black_pixel_count)
    print("# White pixels: ", white_pixel_count)

    # check pixel value:
    # for light mode --> black pixel count should be 4000 to 30000
    if black_pixel_count > 4000 and black_pixel_count < 30000:
        pyautogui.press('up')

    if white_pixel_count > 4000 and white_pixel_count < 30000:
        pyautogui.press('up')

    cv2.imshow('image',image)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break