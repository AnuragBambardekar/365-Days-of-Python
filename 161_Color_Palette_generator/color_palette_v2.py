import tkinter as tk
import random
import tkinter.filedialog
import tkinter.messagebox

"""
Saving Palette colors - feature added!
"""

# Function to generate random colors
def generate_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    color = f'#{r:02x}{g:02x}{b:02x}'
    return color

# Function to generate color palette
def generate_palette():
    num_colors = int(select_field.get())
    for widget in color_frame.winfo_children():
        widget.destroy()
    for i in range(num_colors):
        color = generate_color()
        color_label = tk.Label(color_frame, bg=color, width=10, height=5)
        color_label.grid(row=i, column=0, padx=5, pady=5)
        color_label.bind("<Button-1>", lambda event, c=color: copy_color(c))  # Bind copy_color to left mouse button click

        hex_label = tk.Label(color_frame, text=color, width=10)
        hex_label.grid(row=i, column=1, padx=5, pady=5)

# Function to save the palette to a file
def save_palette():
    file_path = tk.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                for widget in color_frame.winfo_children():
                    if isinstance(widget, tk.Label):
                        hex_color = widget.cget("text")
                        file.write(hex_color + "\n")
            tkinter.messagebox.showinfo("Success", "Palette saved successfully!")
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error saving palette: {str(e)}")

# Function to copy the color to the clipboard
def copy_color(color):
    root.clipboard_clear()
    root.clipboard_append(color)
    root.update()  # Required on macOS to update clipboard content

root = tk.Tk()
root.title("Color Palette Generator")
root.geometry("300x600")

select_field = tk.StringVar(value="1")
select = tk.OptionMenu(root, select_field, "1", "2", "3", "4", "5")
select.pack(side="top", pady=10)

generate_button = tk.Button(root, text="Generate", command=generate_palette)
generate_button.pack(side="top")

save_button = tk.Button(root, text="Save Palette", command=save_palette)
save_button.pack(side="top", pady=10)

color_frame = tk.Frame(root)
color_frame.pack(pady=10)

root.mainloop()
