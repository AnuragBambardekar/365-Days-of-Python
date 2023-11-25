from dataclasses import dataclass, field
from typing import List

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

@dataclass(order=True) # so that we can compare cards
class PlayingCard:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS)
                           + SUITS.index(self.suit))

    def __str__(self) -> str:
        return f'{self.suit}{self.rank}'

"""
@dataclass
class Deck:
    cards: List[PlayingCard]

    
    # The problem with the following is that all instances of Deck will use the
    # same list object as the default value of the .cards property
    
    # cards: List[PlayingCard] = make_french_deck() # use default_factory()

queen_of_hearts = PlayingCard('Q', 'Hearts')
ace_of_spades = PlayingCard('A', 'Spades')
two_cards = Deck([queen_of_hearts, ace_of_spades])

print(two_cards)

"""


"""
Setting Default values - Create a regular (French) deck
"""

# RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
# SUITS = '♣ ♢ ♡ ♠'.split()

def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]

# print(make_french_deck())

"""
Setting a Default Deck using 'field'
"""
# from dataclasses import field

@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_french_deck)

    def __repr__(self):
        cards = ', '.join(f'{c!s}' for c in self.cards)
        return f'{self.__class__.__name__}({cards})'

print(Deck())

ace_of_spades = PlayingCard('A', '♠')
print(ace_of_spades)


queen_of_hearts = PlayingCard('Q', '♡')
ace_of_spades = PlayingCard('A', '♠')
"""
data classes compare objects as if they were tuples of their fields. 
In other words, a Queen is higher than an Ace because 'Q' comes after 'A' in the alphabet:
"""
print(ace_of_spades > queen_of_hearts)

print(Deck(sorted(make_french_deck())))

from random import sample
print(Deck(sample(make_french_deck(), k=10)))