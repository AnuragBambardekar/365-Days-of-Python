def calculate_minimum_coins(amount, denominations, memo={}):
    """Calculates the minimum number of coins needed to make the given amount using the given denominations."""
    if amount == 0:
        return []

    if amount in memo:
        return memo[amount]

    min_coins = float('inf')
    coins_required = []

    for coin in denominations:
        if coin <= amount:
            remaining_coins = calculate_minimum_coins(amount - coin, denominations, memo)
            if remaining_coins is not None and len(remaining_coins) + 1 < min_coins:
                min_coins = len(remaining_coins) + 1
                coins_required = remaining_coins + [coin]

    memo[amount] = coins_required if coins_required else None
    return memo[amount]


# Example usage
amount = 34
denominations = [1, 5, 10, 25]  # Penny, Nickel, Dime, Quarter
coins_required = calculate_minimum_coins(amount, denominations)

if coins_required:
    print(f"To make {amount} cents, you need the following coins: {coins_required}")
else:
    print(f"It is not possible to make {amount} cents with the given denominations.")
