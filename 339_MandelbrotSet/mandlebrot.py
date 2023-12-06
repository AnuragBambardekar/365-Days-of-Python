# mandelbrot.py

from dataclasses import dataclass
from math import log

@dataclass
class MandelbrotSet:
    max_iterations: int
    escape_radius: float = 2.0

    def __contains__(self, c: complex) -> bool:
        return self.stability(c) == 1

    def stability(self, c: complex, smooth=False, clamp=True) -> float:
        value = self.escape_count(c, smooth) / self.max_iterations
        return max(0.0, min(value, 1.0)) if clamp else value

    def escape_count(self, c: complex, smooth=False) -> int | float:
        z = 0
        for iteration in range(self.max_iterations):
            z = z ** 2 + c
            if abs(z) > self.escape_radius:
                if smooth:
                    return iteration + 1 - log(log(abs(z))) / log(2)
                return iteration
        return self.max_iterations
    
# from mandelbrot import MandelbrotSet
# mandelbrot_set = MandelbrotSet(max_iterations=20, escape_radius=1000)

# width, height = 512, 512
# scale = 0.0075
# GRAYSCALE = "L"

# from PIL import Image
# image = Image.new(mode=GRAYSCALE, size=(width, height))
# for y in range(height):
#     for x in range(width):
#         c = scale * complex(x - width / 2, height / 2 - y)
#         instability = 1 - mandelbrot_set.stability(c, smooth=True)
#         image.putpixel((x, y), int(instability * 255))
# image.show()