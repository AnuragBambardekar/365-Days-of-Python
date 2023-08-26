from typing import TypeAlias

Strings: TypeAlias = list[str]
# people: Strings = ['James','Johns']
people: Strings = [10,10]

print(people)

#--------------------------------------------#

# Forward referencing
Basket: TypeAlias = 'list[Fruit]'
print(Basket) # prints a string

class Fruit:
    def __init__(self, fruit: str):
        self.fruit = fruit

    def create_baskets(self) -> Basket:
        return 3* [Fruit(self.fruit)]
    
banana: Fruit = Fruit('Banana')
basket: Basket = banana.create_baskets()
print(basket[0].fruit)