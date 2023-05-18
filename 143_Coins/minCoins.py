def calculate_minimum_coins(amount, denominations):
    """Calculates the minimum number of coins needed to make the given amount using the given denominations."""
    # Create a list to store the minimum number of coins for each amount
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0  # Base case: 0 coins needed for 0 amount

    for coin in denominations:
        for i in range(coin, amount + 1):
            min_coins[i] = min(min_coins[i], 1 + min_coins[i - coin])

    return min_coins[amount]

# Example usage
amount = 34
denominations = [1, 5, 10, 25]  # Penny, Nickel, Dime, Quarter
minimum_coins = calculate_minimum_coins(amount, denominations)
print(f"The minimum number of coins needed to make {amount} cents is {minimum_coins}.")
