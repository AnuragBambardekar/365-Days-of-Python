import random

# Define the cups
cups = ['A', 'B', 'C']

# Randomly select the cup with the ball
ball_cup = random.choice(cups)

# Ask the player to guess the cup with the ball
print("Welcome to the 3-cup monty game!")
print("One of the cups contains a ball. Can you guess which one it is?")
print("Choose a cup: A, B, or C")

# Get the player's guess
guess = input("> ")

# Show the cup with the ball and reveal the result
print(f"The ball was in cup {ball_cup}")
if guess == ball_cup:
    print("Congratulations, you won!")
else:
    print("Sorry, you lost.")
