import numpy as np
import PIL.Image

image = PIL.Image.open('114_Advanced_hiding_information_in_PNG\encoded.png','r')
img_arr = np.array(list(image.getdata()))

channels = 4 if image.mode == 'RGBA' else 3

pixels = img_arr.size // channels

# Extract LSB's
secret_bits = [bin(img_arr[i][j])[-1] for i in range(pixels) for j in range(0,3)]
secret_bits = ''.join(secret_bits)
secret_bits = [secret_bits[i:i+8] for i in range(0, len(secret_bits), 8)]# group them into bytes to convert to ASCII

# print(secret_bits)

secret_message = [chr(int(secret_bits[i], 2)) for i in range(len(secret_bits))]
secret_message = ''.join(secret_message)

stop_indicator = "$BAMBA$"

if stop_indicator in secret_message:
    print(secret_message[:secret_message.index(stop_indicator)])
else:
    print("Could not find secret message!")
