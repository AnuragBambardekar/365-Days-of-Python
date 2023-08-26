from typing import TypeAlias

# Card = tuple[str, str]
# Deck = list[Card]

"""
This usually works okay. However, it’s often not possible for the type 
checker to know whether such a statement is a type alias or just the 
definition of a regular global variable. To help the type checker—or 
really, help the type checker help you—you can now explicitly annotate 
type aliases:
"""

from typing import TypeAlias

# Define type aliases
Card: TypeAlias = tuple[str, str]
Deck: TypeAlias = list[Card]

"""
Adding the TypeAlias annotation clarifies the intention, both to 
a type checker and to anyone reading your code.
"""

# Create a deck of cards
def create_deck() -> Deck:
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    return deck

# Shuffle the deck
def shuffle_deck(deck: Deck) -> Deck:
    import random
    random.shuffle(deck)
    return deck

# Deal a hand of cards
def deal_hand(deck: Deck, num_cards: int) -> Deck:
    if num_cards > len(deck):
        raise ValueError("Not enough cards in the deck to deal.")
    hand = deck[:num_cards]
    del deck[:num_cards]
    return hand

# Main game logic
if __name__ == "__main__":
    # Create and shuffle a deck
    deck = create_deck()
    shuffled_deck = shuffle_deck(deck.copy())  # Make a copy for shuffling
    
    # Deal hands to players
    num_players = 4
    num_cards_per_hand = 5
    hands = [deal_hand(shuffled_deck, num_cards_per_hand) for _ in range(num_players)]
    
    # Print the hands of each player
    for player, hand in enumerate(hands, start=1):
        print(f"Player {player}'s Hand:")
        for card in hand:
            print(f"{card[0]} of {card[1]}")
        print()


