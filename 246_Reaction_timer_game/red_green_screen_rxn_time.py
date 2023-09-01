import tkinter as tk
import time
import random

class ReactionTimeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Reaction Time Game")
        self.root.geometry("550x550")

        self.start_button = tk.Button(
            self.root, text="Start", command=self.start_game)
        self.start_button.pack(pady=20)

        self.instructions_label = tk.Label(
            self.root, text="Click when you see green", font=("Helvetica", 16))
        self.instructions_label.pack(pady=10)

        self.red_screen = tk.Canvas(self.root, width=400, height=400, bg="red")
        self.red_screen.pack(fill="both", expand=True)
        self.red_screen.pack_forget()  # Hide initially

        self.start_time = None
        self.reaction_time_label = tk.Label(
            self.root, text="", font=("Helvetica", 16))
        self.reaction_time_label.pack(pady=20)

        self.play_again_button = tk.Button(
            self.root, text="Play Again", command=self.play_again, state=tk.DISABLED)
        self.play_again_button.pack_forget()

        self.root.bind("<Button-1>", self.calculate_reaction_time)

    def start_game(self):
        self.start_button.pack_forget()  # Hide the start button
        self.instructions_label.pack_forget()  # Hide the instructions
        self.play_again_button.config(state=tk.DISABLED)  # Disable play again button
        self.red_screen.pack()  # Show the red screen
        self.red_screen.after(random.randint(1000, 5000), self.change_to_green)

    def change_to_green(self):
        self.red_screen.configure(bg="green")
        self.start_time = time.time()

    def calculate_reaction_time(self, event):
        if self.start_time is not None:
            end_time = time.time()
            reaction_time = end_time - self.start_time
            self.reaction_time_label.config(
                text=f"Your reaction time: {reaction_time*1000:.2f} milliseconds")
            self.play_again_button.pack(pady=10)
            self.play_again_button.config(state=tk.NORMAL)  # Enable play again button
            self.start_time = None

    def play_again(self):
        self.red_screen.configure(bg="red")  # Reset the screen color to red
        self.reaction_time_label.config(text="")  # Clear the reaction time label
        self.play_again_button.config(state=tk.DISABLED)  # Disable play again button
        self.red_screen.after(random.randint(1000, 5000), self.change_to_green)  # Start a new round

if __name__ == "__main__":
    root = tk.Tk()
    app = ReactionTimeGame(root)
    root.mainloop()
