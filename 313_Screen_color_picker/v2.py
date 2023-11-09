from pynput import keyboard
from pynput import mouse
from PIL import Image, ImageGrab
import webcolors
import os

# Save color as an image feature added

def getHex(rgb):
    return '%02X%02X%02X' % rgb

def getRGBFromHex(hex_color):
    return webcolors.hex_to_rgb('#'+hex_color)

def displayColorInfo(rgb):
    hex_color = getHex(rgb)
    actual_color = getRGBFromHex(hex_color)
    print(f'COLOR: rgb{rgb} | HEX #{hex_color}')

    # Create an image filled with the actual color
    image = Image.new('RGB', (100, 100), actual_color)
    save_path = os.path.join('color_images', f'{hex_color}.png')
    image.save(save_path)
    print(f'Saved color image to {save_path}')

def checkColor(x, y):
    bbox = (x, y, x + 1, y + 1)
    im = ImageGrab.grab(bbox=bbox)
    rgbim = im.convert('RGB')
    r, g, b = rgbim.getpixel((0, 0))
    displayColorInfo((r, g, b))

def onClick(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
        checkColor(x, y)

def onRel(key):
    if key == keyboard.Key.esc:
        mlstnr.stop()
        return False

if __name__ == '__main__':
    # Create a folder to store color images if it doesn't exist
    os.makedirs('color_images', exist_ok=True)

    with keyboard.Listener(on_release=onRel) as klstnr:
        with mouse.Listener(on_click=onClick) as mlstnr:
            klstnr.join()
            mlstnr.join()
