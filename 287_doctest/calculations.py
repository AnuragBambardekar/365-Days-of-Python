# python -m doctest calculations.py
# python -m doctest -v calculations.py

def add(a,b):
    """
    Compute and return the sum of two numbers.

    Usage examples:
    >>> add(4.0, 2.0)
    6.0
    >>> add(4,2)
    6.0
    """
    return float(a+b)