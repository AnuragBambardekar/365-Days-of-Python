import concurrent.futures
import time
import sys  
sys.path.insert(0, 'Multiprocessing_in_python\do_something.py')
from do_something1 import do_something1 as do_something1

if __name__ == "__main__":
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something1, secs)

        for result in results:
            print(result)

    finish = time.perf_counter()
    print(start)
    print(finish)
    print(f'Finished in {round(finish-start, 2)} second(s)')

#=======Output=========#
# Sleeping 5 second(s)...
# Sleeping 4 second(s)...
# Sleeping 3 second(s)...
# Sleeping 2 second(s)...
# Sleeping 1 second(s)...
# Done Sleeping...5
# Done Sleeping...4
# Done Sleeping...3
# Done Sleeping...2
# Done Sleeping...1
# 157975.3829421
# 157980.6098159
# Finished in 5.23 second(s)