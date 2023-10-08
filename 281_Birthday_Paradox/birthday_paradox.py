import random

def birthday_paradox_simulation(num_simulations, num_people):
    shared_birthday_count = 0

    for _ in range(num_simulations):
        birthdays = [random.randint(1, 365) for _ in range(num_people)]
        if len(birthdays) != len(set(birthdays)):
            shared_birthday_count += 1

    probability = shared_birthday_count / num_simulations
    return probability

def main():
    num_simulations = 10000  # Number of simulations to run
    num_people = 23  # Number of people in each group

    """
    50% probability is reached with just 23 people and 99% with just 70 people.
    """

    probability = birthday_paradox_simulation(num_simulations, num_people)

    print(f"Probability of at least two people sharing a birthday with {num_people} people: {probability:.4f}")

if __name__ == "__main__":
    main()
