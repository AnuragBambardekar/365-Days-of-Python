from timeit import timeit

# Lots of if statements vs elif construct

def test_if(text: str):
    if text == 'a':
        ...
    if text == 'b': # Checks this as well
        ...
    if text == 'c': # Checks this as well
        ...
    
    ...

def test_if_else(text: str):
    if text == 'a': # Stops here and doesn't execute anything else
        ...
    elif text == 'b':
        ...
    elif text == 'c':
        ...
    else:
        ...

if __name__ == '__main__':
    letter: str = 'a'

    if_chain_time: float = timeit('test_if(letter)', globals=globals(), number=10**7)
    if_else_chain_time: float = timeit('test_if_else(letter)', globals=globals(), number=10**7)

    print('if if:', round(if_chain_time,3))
    print('if else:', round(if_else_chain_time,3))