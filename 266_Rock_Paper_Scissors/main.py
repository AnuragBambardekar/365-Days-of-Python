import random

print("Welcome to Rock Paper Scissors!")
print("--------------------------------")

cpuScore = 0
playerScore = 0
tieScore = 0
possibleHands = ["Rock", "Paper", "Scissors"]

def checkForWinner(playerHand, computerHand):
    global cpuScore, playerScore, tieScore
    
    print(f"Player chose: {playerHand}")
    print(f"Computer chose: {computerHand}")

    if playerHand == computerHand:
        print("It's a tie!")
        tieScore += 1
    elif (playerHand == "Rock" and computerHand == "Scissors") or \
         (playerHand == "Paper" and computerHand == "Rock") or \
         (playerHand == "Scissors" and computerHand == "Paper"):
        print("Player wins!")
        playerScore += 1
    else:
        print("Computer wins!")
        cpuScore += 1

while True:
    playerChoice = input("Enter your choice (Rock/Paper/Scissors or 'Quit' to exit): ").capitalize()
    
    if playerChoice == 'Quit':
        break
    
    if playerChoice not in possibleHands:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        continue
    
    computerChoice = random.choice(possibleHands)
    checkForWinner(playerChoice, computerChoice)
    
    print(f"Player Score: {playerScore}")
    print(f"Computer Score: {cpuScore}")
    print(f"Tie Score: {tieScore}")
    print("--------------------------------")

print("Thanks for playing!")
