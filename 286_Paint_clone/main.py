# import tkinter as tk

# # Global variables to track the current color and brush size
# current_color = "black"
# current_brush_size = 2

# def change_color(new_color):
#     global current_color
#     current_color = new_color

# def change_brush_size(new_size):
#     global current_brush_size
#     current_brush_size = new_size

# def paint(event):
#     x1, y1 = (event.x - current_brush_size), (event.y - current_brush_size)
#     x2, y2 = (event.x + current_brush_size), (event.y + current_brush_size)
#     canvas.create_oval(x1, y1, x2, y2, fill=current_color, width=0)

# root = tk.Tk()
# root.title("Simple Paint App")

# canvas = tk.Canvas(root, bg="white", width=400, height=400)
# canvas.pack()

# color_frame = tk.Frame(root)
# color_frame.pack()

# colors = ["black", "red", "green", "blue", "orange", "yellow"]
# for color in colors:
#     color_button = tk.Button(color_frame, bg=color, width=2, height=1, command=lambda c=color: change_color(c))
#     color_button.pack(side=tk.LEFT)

# size_frame = tk.Frame(root)
# size_frame.pack()

# sizes = [1, 2, 4, 6, 8]
# for size in sizes:
#     size_button = tk.Button(size_frame, text=str(size), width=2, height=1, command=lambda s=size: change_brush_size(s))
#     size_button.pack(side=tk.LEFT)

# canvas.bind("<B1-Motion>", paint)

# root.mainloop()


import tkinter as tk

# Global variables to track the current color, brush size, and history of actions
current_color = "black"
current_brush_size = 2

def change_color(new_color):
    global current_color
    current_color = new_color

def change_brush_size(new_size):
    global current_brush_size
    current_brush_size = new_size

def paint(event):
    x1, y1 = (event.x - current_brush_size), (event.y - current_brush_size)
    x2, y2 = (event.x + current_brush_size), (event.y + current_brush_size)
    canvas.create_oval(x1, y1, x2, y2, fill=current_color, width=0)

def erase():
    global current_color
    current_color = "white"

root = tk.Tk()
root.title("Simple Paint App")

canvas = tk.Canvas(root, bg="white", width=400, height=400)
canvas.pack()

color_frame = tk.Frame(root)
color_frame.pack()

colors = ["black", "red", "green", "blue", "orange", "yellow"]
for color in colors:
    color_button = tk.Button(color_frame, bg=color, width=2, height=1, command=lambda c=color: change_color(c))
    color_button.pack(side=tk.LEFT)

size_frame = tk.Frame(root)
size_frame.pack()

sizes = [1, 2, 4, 6, 8]
for size in sizes:
    size_button = tk.Button(size_frame, text=str(size), width=2, height=1, command=lambda s=size: change_brush_size(s))
    size_button.pack(side=tk.LEFT)

erase_button = tk.Button(root, text="Erase", command=erase)
erase_button.pack()

canvas.bind("<B1-Motion>", paint)

root.mainloop()
