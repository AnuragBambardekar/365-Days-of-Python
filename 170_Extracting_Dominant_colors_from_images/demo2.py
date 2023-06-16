# pip install colorthief

from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys

ct = ColorThief("170_Extracting_Dominant_colors_from_images/test_img2.jpg")

dominant_color = ct.get_color(quality=1)
print(dominant_color) # get dominant color

plt.imshow([[dominant_color]])
plt.show()

#get 2 or 3 dominant colors
palette = ct.get_palette(color_count=5)
plt.imshow([[palette[i] for i in range(5)]])
plt.show()

for color in palette:
    print(color) # RGB
    print(f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}') # Hex
    print(colorsys.rgb_to_hsv(*color)) # HSV
    print(colorsys.rgb_to_hls(*color)) # HLS
    print()

"""
 the asterisk (*) is used to unpack a sequence or iterable object. 
 It allows you to pass the individual elements of the sequence as separate arguments to a function
"""

"""
HSV (Hue, Saturation, Value/Vibrance):

Hue: It represents the dominant wavelength of light and defines the color's base tone. It is typically represented as an angle on a color wheel, ranging from 0 to 360 degrees.
Saturation: It indicates the purity or intensity of the color. A saturation value of 0 results in grayscale, while a value of 1 represents the purest form of the color.
Value/Vibrance: It refers to the brightness or lightness of the color. A value of 0 represents black, and a value of 1 represents the maximum brightness of the color.
The HSV color model is often used in computer graphics, image processing, and color selection tools. It provides an intuitive way to manipulate colors by adjusting the hue, saturation, and value independently.

HLS (Hue, Lightness, Saturation):

Hue: Similar to HSV, it represents the base color tone.
Lightness/Luminance: It indicates the perceived brightness of the color. A lightness value of 0 represents black, while a value of 1 represents white.
Saturation: It represents the color intensity or purity. A saturation value of 0 results in grayscale, and a value of 1 represents the purest form of the color.
The HLS color model is often used in color spaces that aim to match human perception, such as the HSL (Hue, Saturation, Lightness) color model. It provides a way to manipulate colors by adjusting the hue, lightness, and saturation.
"""