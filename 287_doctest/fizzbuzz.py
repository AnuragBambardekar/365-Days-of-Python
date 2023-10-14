# python -m doctest -v fizzbuzz.py

def fizzbuzz(numbers):
    """
    Implement the FizzBuzz Game

    >>> fizzbuzz([3,6,9,12])
    ['fizz', 'fizz', 'fizz', 'fizz']

    >>> fizzbuzz([5, 10, 20, 25])
    ['buzz', 'buzz', 'buzz', 'buzz']

    >>> fizzbuzz([15, 30, 45])
    ['fizz buzz', 'fizz buzz', 'fizz buzz']

    >>> fizzbuzz([3, 6, 5, 2, 15, 30])
    ['fizz', 'fizz', 'buzz', 2, 'fizz buzz', 'fizz buzz']
    """
    res = []
    for n in numbers:
        if n % 15 == 0:
            res.append("fizz buzz")
        elif n%3 == 0:
            res.append("fizz")
        elif n%5 == 0:
            res.append("buzz")
        else:
            res.append(n)
    return res