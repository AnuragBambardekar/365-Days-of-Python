import time

def timing(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()-t1
        print(f"{func.__name__} ran in {t2} seconds")

    return wrapper

@timing
def do_this():
    time.sleep(1.5)

@timing
def do_that():
    time.sleep(0.5)

do_this()
do_that()
print("Done")