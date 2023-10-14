# python -m doctest -v catching_exceptions.py

def divide(a, b):
    """Compute and return the quotient of two numbers.

    Usage examples:
    >>> divide(84, 2)
    42.0
    >>> divide(15, 3)
    5.0
    >>> divide(42, -2)
    -21.0

    >>> divide(42, 0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero
    """
    return float(a / b)