import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class SpellCheck:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x500")

        self.text = ScrolledText(self.root, font=("Arial", 14))
        self.text.bind("<KeyRelease>", self.check)
        self.text.pack()

        self.root.mainloop()

    def check(self, event):
        print("hello World")

SpellCheck()