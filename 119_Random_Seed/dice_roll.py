import random

# Set the random seed to ensure the same result each time the program runs
random.seed(1234)

# Define the possible values for the dice roll
dice = [1, 2, 3, 4, 5, 6]

# Roll two dice by randomly selecting a value from the list of possible values
roll1 = random.choice(dice)
roll2 = random.choice(dice)

# Determine the total value of the dice roll
total = roll1 + roll2

# Print the results of the dice roll
print("You rolled a", roll1, "and a", roll2, "for a total of", total)

# Determine if the roll is a win or a loss
if total in [7, 11]:
    print("You win!")
elif total in [2, 3, 12]:
    print("You lose!")
else:
    print("Roll again...")
