"""
HSV stands for Hue, Saturation, and Value. It is a color model used in color applications such as image and graphics editing software. 
The HSV color model is based on the concept of a color wheel, where hues are arranged in a circular pattern. 
The hue represents the color itself, and it is expressed as an angle in degrees (ranging from 0 to 360) around the color wheel. Saturation represents the purity or intensity of the hue, and it is expressed as a percentage (ranging from 0 to 100). Value represents the brightness or lightness of the color, and it is also expressed as a percentage (ranging from 0 to 100).

The HSV color model is often used as an alternative to the RGB color model because it separates the color information (hue) from the 
brightness and saturation information, making it easier to manipulate and adjust colors.
"""

# Take user input for RGB color values
red = int(input("Enter the value of red between 0 and 255: "))
green = int(input("Enter the value of green between 0 and 255: "))
blue = int(input("Enter the value of blue between 0 and 255: "))

# Convert RGB to HSV
red_norm = red/255
green_norm = green/255
blue_norm = blue/255

cmax = max(red_norm, green_norm, blue_norm)
cmin = min(red_norm, green_norm, blue_norm)
delta = cmax - cmin

if delta == 0:
    hue = 0
elif cmax == red_norm:
    hue = ((green_norm - blue_norm) / delta) % 6
elif cmax == green_norm:
    hue = (blue_norm - red_norm) / delta + 2
else:
    hue = (red_norm - green_norm) / delta + 4

hue = round(hue * 60)
if hue < 0:
    hue += 360

if cmax == 0:
    saturation = 0
else:
    saturation = delta / cmax

value = cmax

# Print HSV values
print("Hue: ", hue)
print("Saturation: ", saturation)
print("Value: ", value)
