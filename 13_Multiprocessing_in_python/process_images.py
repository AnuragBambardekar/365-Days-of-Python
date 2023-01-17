from PIL import Image, ImageFilter
import time
import concurrent.futures

img_names = [
    'photo-1517935706615-2717063c2225.jpg',
    'photo-1583211237509-9d5d3bfcd07b.jpg',
    'photo-1582585861644-d275d5c108e0.jpg',
    'photo-1557978557-2068ea6a817e.jpg',
    'photo-1557978557-57231f2dbc36.jpg',
    'photo-1518378892156-2c6bb23677df.jpg',
    'photo-1508693926297-1d61ee3df82a.jpg',
    'photo-1588733103629-b77afe0425ce.jpg',
    'photo-1551009175-15bdf9dcb580.jpg',
    'photo-1490623970972-ae8bb3da443e.jpg',
]

size = (1200,1200) #set image resize size

def process_image(img_name):
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size) #Resizing image
    img.save(f'processed/{img_name}')
    print(f'{img_name} was processed...')