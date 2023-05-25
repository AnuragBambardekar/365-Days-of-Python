from timeit import timeit

# Lots of if statements vs elif construct

def test_if(text: str):
    if text == 'a':
        return True
    if text == 'b': # Checks this as well
        return True
    if text == 'c': # Checks this as well
        return True
    
    return False

def test_if_else(text: str):
    if text == 'a': # Stops here and doesn't execute anything else
        return True
    elif text == 'b':
        return True
    elif text == 'c':
        return True
    else:
        return False

if __name__ == '__main__':
    # letter: str = 'a'
    letter: str = 'd'

    if_chain_time: float = timeit('test_if(letter)', globals=globals(), number=10**7)
    if_else_chain_time: float = timeit('test_if_else(letter)', globals=globals(), number=10**7)

    print('if if:', round(if_chain_time,3))
    print('if else:', round(if_else_chain_time,3))