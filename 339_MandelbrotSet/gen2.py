from PIL import Image
from mandlebrot import MandelbrotSet
from viewport import Viewport

# Mandelbrot Set Centered At a Misiurewicz Point
mandelbrot_set = MandelbrotSet(max_iterations=256, escape_radius=1000)

image = Image.new(mode="L", size=(512, 512))
for pixel in Viewport(image, center=-0.7435 + 0.1314j, width=0.002):
    c = complex(pixel)
    instability = 1 - mandelbrot_set.stability(c, smooth=True)
    pixel.color = int(instability * 255)

# image.show()

from PIL import ImageEnhance
enhancer = ImageEnhance.Brightness(image)
enhancer.enhance(1.25).show()