import time
import threading
import tkinter as tk
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

class AutoClickerGUI:
    def __init__(self):
        self.clicking = False
        self.mouse = Controller()
        self.toggle_key = KeyCode(char="t")
        self.interval = 0.001
        self.click_count = 0
        
        self.window = tk.Tk()
        self.window.title("Auto Clicker")
        
        self.click_button = tk.Button(self.window, text="Click", command=self.increment_click_count)
        self.click_button.pack(padx=10, pady=10)
        
        self.toggle_button = tk.Button(self.window, text="Start Auto Clicker", command=self.toggle_clicking)
        self.toggle_button.pack(padx=10, pady=10)
        
        self.click_label = tk.Label(self.window, text="Clicks: 0")
        self.click_label.pack(padx=10, pady=10)
        
    def toggle_clicking(self):
        self.clicking = not self.clicking
        if self.clicking:
            self.toggle_button.config(text="Stop Auto Clicker")
            self.click_button.config(state=tk.DISABLED)
            click_thread = threading.Thread(target=self.clicker)
            click_thread.start()
        else:
            self.toggle_button.config(text="Start Auto Clicker") # Keep 't' pressed
            self.click_button.config(state=tk.NORMAL)
        
    def increment_click_count(self):
        self.click_count += 1
        self.click_label.config(text=f"Clicks: {self.click_count}")
        
    def clicker(self):
        while self.clicking:
            self.mouse.click(Button.left, 1)
            self.click_count += 1
            self.click_label.config(text=f"Clicks: {self.click_count}")
            time.sleep(self.interval)
            
    def start(self):
        with Listener(on_press=self.on_press) as listener:
            self.window.mainloop()
            
    def on_press(self, key):
        if key == self.toggle_key:
            self.toggle_clicking()

if __name__ == '__main__':
    autoclicker_gui = AutoClickerGUI()
    autoclicker_gui.start()
