import time

t1 = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

do_something()
do_something()

t2 = time.perf_counter()

print(f"Finished in {round(t2-t1, 2)} second(s)")

#=======Output=======#
# Sleeping 1 second...
# Done Sleeping...
# Sleeping 1 second...
# Done Sleeping...
# Finished in 2.02 second(s)