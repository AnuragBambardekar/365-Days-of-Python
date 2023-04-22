import random

# Set the random seed to ensure the same result each time the program runs
random.seed(1234)

# Define the possible moves for rock-paper-scissors
moves = ["rock", "paper", "scissors"]

# Randomly select a move for the player and the computer
player_move = random.choice(moves)
computer_move = random.choice(moves)

# Print the moves of the player and the computer
print("You chose", player_move)
print("The computer chose", computer_move)

# Determine the winner of the game
if player_move == computer_move:
    print("It's a tie!")
elif player_move == "rock" and computer_move == "scissors" or \
     player_move == "paper" and computer_move == "rock" or \
     player_move == "scissors" and computer_move == "paper":
    print("You win!")
else:
    print("The computer wins!")
