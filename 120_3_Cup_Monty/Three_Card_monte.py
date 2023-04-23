import random

# Define the three cards
cards = ["Ace", "King", "Queen"]

# Shuffle the cards
random.shuffle(cards)

# Show the player the cards
print("Welcome to Three-card Monte!")
print("I'm going to shuffle three cards: Ace, King, and Queen.")
print("Watch closely and try to remember which card is the Ace.\n")
print(cards)

# Get the player's guess
guess = input("Which card do you think is the Ace? (Enter 1, 2, or 3): ")

# Convert the guess to an index
guess_index = int(guess) - 1

# Check if the guess is correct
if cards[guess_index] == "Ace":
    print("Congratulations! You guessed correctly.")
else:
    print("Sorry, the Ace was actually under card number " + str(cards.index("Ace") + 1) + ".")
