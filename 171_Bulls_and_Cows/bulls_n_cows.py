import random

def generate_secret_number():
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:4]  # Generates a 4-digit secret number

def get_guess():
    while True:
        guess = input("Enter your guess (4 digits): ")
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid guess. Please enter a 4-digit number.")
        else:
            return list(map(int, guess))

def evaluate_guess(secret_number, guess):
    bulls = cows = 0
    for i in range(len(secret_number)):
        if secret_number[i] == guess[i]:
            bulls += 1
        elif secret_number[i] in guess:
            cows += 1
    return bulls, cows

def play_game():
    secret_number = generate_secret_number()
    attempts = 0
    while True:
        attempts += 1
        guess = get_guess()
        bulls, cows = evaluate_guess(secret_number, guess)
        print(f"Bulls: {bulls}, Cows: {cows}")
        if bulls == 4:
            print(f"Congratulations! You guessed the secret number in {attempts} attempts.")
            break

print("Welcome to Bulls and Cows!")
play_game()

"""
How to Play?

For each guess, the computer provides feedback in terms of "bulls" and "cows."
 A "bull" represents a correct digit in the correct position, while a "cow" represents a correct digit in the wrong position.
"""