from statistics import mean
from functools import cached_property

class Calculator:
    def __init__(self, values: list[float]):
        self.values = values

    @cached_property
    def sum(self) -> float:
        print(f'Getting the sum of: {self.values}')
        return sum(self.values)
    
    @cached_property
    def mean(self) -> float:
        print(f'Getting the mean of: {self.values}')
        return mean(self.values)
    
if __name__ == '__main__':
    numbers: list[float] = [4.2,6.8,3.0,13.5,9.5]

    calc: Calculator = Calculator(numbers)
    # print(calc.sum())
    # print(calc.sum())
    # print(calc.sum())
    # Why compute it 3 times when the result is same always, so use @cached_property

    """
    This means that the property's value is computed once and then stored for future access, preventing unnecessary recomputation. 
    This can be especially useful for properties that involve complex or expensive calculations.
    """

    print(calc.sum)
    print(calc.sum)
    print(calc.sum)

    print(calc.mean)
    print(calc.mean)
    print(calc.mean)