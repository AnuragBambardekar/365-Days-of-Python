# python -m doctest -v printed_output.py

def greet(name="World"):
    """Print a greeting to the screen.

    Usage examples:
    >>> greet("Pythonista")
    Hello, Pythonista!
    >>> greet()
    Hello, World!
    """
    print(f"Hello, {name}!")