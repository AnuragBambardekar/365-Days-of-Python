from dataclasses import dataclass

@dataclass
class DataClassCard:
    rank: str
    suit: str

queen_of_hearts = DataClassCard('Q','Hearts')
print(queen_of_hearts.rank)
print(queen_of_hearts)
print(queen_of_hearts == DataClassCard('Q','Hearts'))


"""
rank and suit are both repeated three times simply to initialize an object.
"""
class RegularCard:
    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.suit = suit

    """
    To fix this Falsy situation:
    print( queen_of_hearts == RegularCard('Q', 'Hearts')) # Returns False

    We, need to implement __repr__ and __eq__
    """
    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(rank={self.rank!r}, suit={self.suit!r})')

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.rank, self.suit) == (other.rank, other.suit)

"""
for some reason a queen of hearts is not the same as a queen of hearts
"""
queen_of_hearts = RegularCard('Q', 'Hearts')
print( queen_of_hearts.rank)
print( queen_of_hearts)
print( queen_of_hearts == RegularCard('Q', 'Hearts'))