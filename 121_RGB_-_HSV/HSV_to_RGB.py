"""
RGB values represent a color in terms of the amount of red, green, and blue light that are combined to create that color. 
In a digital image or on a computer screen, each pixel is composed of red, green, and blue color channels, each of which can have a value between 0 and 255.

So an RGB color is usually represented as a combination of three integers, each of which represents the intensity of the respective color channel. 
For example, the color white is represented as (255, 255, 255), which means that the red, green, and blue channels are at their maximum intensity, 
resulting in a pure white color.
"""

# Take user input for HSV color values
hue = float(input("Enter the value of hue between 0 and 360: "))
saturation = float(input("Enter the value of saturation between 0 and 1: "))
value = float(input("Enter the value of value between 0 and 1: "))

# Convert HSV to RGB
c = value * saturation
x = c * (1 - abs((hue / 60) % 2 - 1))
m = value - c

if hue < 60:
    red, green, blue = c, x, 0
elif hue < 120:
    red, green, blue = x, c, 0
elif hue < 180:
    red, green, blue = 0, c, x
elif hue < 240:
    red, green, blue = 0, x, c
elif hue < 300:
    red, green, blue = x, 0, c
else:
    red, green, blue = c, 0, x

red = round((red + m) * 255)
green = round((green + m) * 255)
blue = round((blue + m) * 255)

# Print RGB values
print("Red: ", red)
print("Green: ", green)
print("Blue: ", blue)
