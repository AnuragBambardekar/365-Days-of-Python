def calculate_minimum_coins(amount, denominations):
    """Calculates the minimum number of coins needed to make the given amount using the given denominations."""
    # Create a list to store the minimum number of coins for each amount
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0  # Base case: 0 coins needed for 0 amount

    coin_used = [[0] * len(denominations) for _ in range(amount + 1)]  # Keep track of coins used

    for i in range(1, amount + 1):
        for j in range(len(denominations)):
            if denominations[j] <= i:
                if 1 + min_coins[i - denominations[j]] < min_coins[i]:
                    min_coins[i] = 1 + min_coins[i - denominations[j]]
                    coin_used[i] = coin_used[i - denominations[j]][:]
                    coin_used[i][j] += 1

    if min_coins[amount] == float('inf'):
        return []

    coins_required = []
    for i in range(len(denominations)):
        coins_required += [denominations[i]] * coin_used[amount][i]

    return coins_required


# Example usage
amount = 34
denominations = [1, 5, 10, 25]  # Penny, Nickel, Dime, Quarter
coins_required = calculate_minimum_coins(amount, denominations)

if coins_required:
    print(f"To make {amount} cents, you need the following coins: {coins_required}")
else:
    print(f"It is not possible to make {amount} cents with the given denominations.")
