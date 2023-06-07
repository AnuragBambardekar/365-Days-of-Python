import tkinter as tk
import random

root = tk.Tk()
root.title("Color Palette Generator")
root.geometry("300x600")

select_field = tk.StringVar(value="1")
select = tk.OptionMenu(root, select_field, "1","2","3","4","5")