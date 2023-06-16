# pip install colorthief

from colorthief import ColorThief
import matplotlib.pyplot as plt

ct = ColorThief("170_Extracting_Dominant_colors_from_images/test_img2.jpg")

dominant_color = ct.get_color(quality=1)
print(dominant_color) # get dominant color

plt.imshow([[dominant_color]])
plt.show()

#get 2 or 3 dominant colors
palette = ct.get_palette(color_count=5)
plt.imshow([[palette[i] for i in range(5)]])
plt.show()