def rgb_to_hex(red, green, blue):
    return "#{:02x}{:02x}{:02x}".format(red, green, blue)

print(rgb_to_hex(255, 0, 0))
print(rgb_to_hex(0, 255, 0))
print(rgb_to_hex(255, 0, 255))

import webcolors

def get_color_name(hex_code):
    try:
        rgb_code = webcolors.hex_to_rgb(hex_code)
        return webcolors.rgb_to_name(rgb_code)
    except ValueError:
        return None

print(get_color_name("#ff0000"))
print(get_color_name(rgb_to_hex(255, 0, 255)))
