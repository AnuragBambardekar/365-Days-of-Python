import tkinter as tk
import random
import webcolors
import colorsys

"""
Color Information - HSV - feature added!
"""

# Function to generate random colors
def generate_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = f'#{r:02x}{g:02x}{b:02x}'
    return color


# Function to generate color palette
# Function to generate color palette
def generate_palette():
    num_colors = int(select_field.get())
    for widget in color_frame.winfo_children():
        widget.destroy()
    for i in range(num_colors):
        color = generate_color()
        color_label = tk.Label(color_frame, bg=color, width=10, height=5)
        color_label.grid(row=i, column=0, padx=5, pady=5)
        color_label.bind("<Button-1>", lambda event, c=color: copy_color(c))

        hex_label = tk.Label(color_frame, text=color, width=10)
        hex_label.grid(row=i, column=1, padx=5, pady=5)

        hsv = colorsys.rgb_to_hsv(int(color[1:3], 16) / 255, int(color[3:5], 16) / 255, int(color[5:], 16) / 255)
        hsv_label = tk.Label(color_frame, text=f"H: {int(hsv[0] * 360)}, S: {int(hsv[1] * 100)}, V: {int(hsv[2] * 100)}")
        hsv_label.grid(row=i, column=2, padx=5, pady=5)


# Function to convert RGB to hexadecimal color
def rgb_to_hex(color):
    r, g, b = color
    hex_color = f'#{r:02x}{g:02x}{b:02x}'
    return hex_color

# Function to convert RGB to HSV color
def rgb_to_hsv(color):
    r, g, b = color
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    max_value = max(r, g, b)
    min_value = min(r, g, b)
    diff = max_value - min_value

    if diff == 0:
        h = 0
    elif max_value == r:
        h = (60 * ((g - b) / diff) + 360) % 360
    elif max_value == g:
        h = (60 * ((b - r) / diff) + 120) % 360
    else:
        h = (60 * ((r - g) / diff) + 240) % 360

    if max_value == 0:
        s = 0
    else:
        s = (diff / max_value) * 100

    v = max_value * 100
    hsv_color = f"{int(h)}, {int(s)}%, {int(v)}%"
    return hsv_color

# Function to get color name from hexadecimal code
def get_color_name(hex_color):
    closest_name = ""
    closest_distance = float("inf")
    r, g, b = webcolors.hex_to_rgb(hex_color)
    for name, rgb in webcolors.CSS3_NAMES_TO_HEX.items():
        distance = abs(rgb[0] - r) + abs(rgb[1] - g) + abs(rgb[2] - b)
        if distance < closest_distance:
            closest_distance = distance
            closest_name = name
    return closest_name

# Function to copy the color to the clipboard
def copy_color(color):
    root.clipboard_clear()
    root.clipboard_append(color)
    root.update()  # Required on macOS to update clipboard content

root = tk.Tk()
root.title("Color Palette Generator")
root.geometry("500x600")

select_field = tk.StringVar(value="1")
select = tk.OptionMenu(root, select_field, "1", "2", "3", "4", "5")
select.pack(side="top", pady=10)

generate_button = tk.Button(root, text="Generate", command=generate_palette)
generate_button.pack(side="top")

color_frame = tk.Frame(root)
color_frame.pack(pady=10)

root.mainloop()
