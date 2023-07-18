from functools import wraps # to avoid a bug
from time import perf_counter, sleep

def get_time(func):
    """Times any function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()

        print(args, kwargs)

        func(*args, **kwargs)
        end_time = perf_counter()

        total_time = round(end_time - start_time, 2)
        print("Time", total_time, "seconds")

    return wrapper
        
@get_time
def do_something(param: str, list: list):
    """Does something important"""
    sleep(1)
    print(param)

if __name__ == "__main__":
    do_something("Hello", ['hello',3])

    print(do_something.__name__) # bug --> resolved by adding @wraps to wrapper function