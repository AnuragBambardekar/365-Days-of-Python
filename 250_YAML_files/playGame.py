import random, yaml
import getpass

with open("250_YAML_files/gameConfig.yaml","r") as f:
    config = yaml.safe_load(f)

range_min = config['range']['min']
range_max = config['range']['max']
guesses_allowed = config['guesses']
mode = config['mode']

solved = False

if mode == "single":
    correct_number = random.randint(range_min, range_max)
elif mode == "multi":
    correct_number = int(getpass.getpass("Player 2 Please enter the number to guess: "))
else:
    print("Invalid Config!")
    exit()

for i in range(guesses_allowed):
    guess = int(input("Enter your guess: "))

    if guess == correct_number:
        print(f"Correct! You needed {i+1} tries!")
        solved = True
        break
    elif guess < correct_number:
        print("Too low!")
    else:
        print("Too High!")

if not solved:
    print("You Lost! The number was: ", correct_number)
