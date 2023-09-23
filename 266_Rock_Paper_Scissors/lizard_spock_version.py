import random

print("Welcome to Rock Paper Scissors Lizard Spock!")
print("--------------------------------")

cpuScore = 0
playerScore = 0
tieScore = 0
possibleHands = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

# Create a dictionary to define the winning moves for each choice
winning_moves = {
    "Rock": ["Scissors", "Lizard"],
    "Paper": ["Rock", "Spock"],
    "Scissors": ["Paper", "Lizard"],
    "Lizard": ["Spock", "Paper"],
    "Spock": ["Scissors", "Rock"]
}

def checkForWinner(playerHand, computerHand):
    global cpuScore, playerScore, tieScore
    
    print(f"Player chose: {playerHand}")
    print(f"Computer chose: {computerHand}")

    if playerHand == computerHand:
        print("It's a tie!")
        tieScore += 1
    elif computerHand in winning_moves[playerHand]:
        print("Player wins!")
        playerScore += 1
    else:
        print("Computer wins!")
        cpuScore += 1

while True:
    playerChoice = input("Enter your choice (Rock/Paper/Scissors/Lizard/Spock or 'Quit' to exit): ").capitalize()
    
    if playerChoice == 'Quit':
        break
    
    if playerChoice not in possibleHands:
        print("Invalid choice. Please choose Rock, Paper, Scissors, Lizard, or Spock.")
        continue
    
    computerChoice = random.choice(possibleHands)
    checkForWinner(playerChoice, computerChoice)
    
    print(f"Player Score: {playerScore}")
    print(f"Computer Score: {cpuScore}")
    print(f"Tie Score: {tieScore}")
    print("--------------------------------")

print("Thanks for playing!")
