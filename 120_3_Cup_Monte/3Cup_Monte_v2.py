import random

# Define the cups
cups = ['A', 'B', 'C']

# Shuffle the cups
random.shuffle(cups)

# Randomly select the cup with the ball
ball_cup = random.choice(cups)

# Ask the player to guess the cup with the ball
print("Welcome to the 3-cup monty game!")
print("One of the cups contains a ball. Can you guess which one it is?")
print("Choose a cup: A, B, or C")

# Play the game
num_guesses = 0
while True:
    # Get the player's guess
    guess = input("> ")

    # Check if the guess is valid
    if guess not in cups:
        print("Invalid input. Please choose A, B, or C.")
        continue

    # Increment the number of guesses
    num_guesses += 1

    # Show the cup with the ball and reveal the result
    print(f"The ball was in cup {ball_cup}")
    if guess == ball_cup:
        print("Congratulations, you won!")
        break
    else:
        print("Sorry, try again.")

    # Shuffle the cups again
    random.shuffle(cups)

    # Randomly select the cup with the ball
    ball_cup = random.choice(cups)

    # Ask if the player wants to continue playing
    print("Do you want to play again? (y/n)")
    choice = input("> ")
    if choice.lower() == 'n':
        break

# Display the number of guesses
print(f"You made {num_guesses} guesses.")
