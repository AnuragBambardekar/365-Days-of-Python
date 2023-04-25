import random

def random_hex_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

print(random_hex_color())

import webcolors
from PIL import Image

def get_color_name(hex_code):
    """Returns the name and a visual representation of the color represented by the hex code [returns closest match because webcolors library does not have all colors
    for any random hex code, so it returns the closest available hex code-color]."""
    rgb_code = webcolors.hex_to_rgb(hex_code)
    try:
        color_name = webcolors.rgb_to_name(rgb_code, spec='css3')
    except ValueError:
        color_name = None
    color_swatch = Image.new('RGB', (100, 100), rgb_code)
    return color_name, color_swatch

name, swatch = get_color_name("#11d097")
print(name)  # Output: violet
swatch.show()  # Displays a color swatch of the color violet


