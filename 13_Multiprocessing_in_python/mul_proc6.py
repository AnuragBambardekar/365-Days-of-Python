import concurrent.futures
import time
import sys  
sys.path.insert(0, 'Multiprocessing_in_python\do_something.py')
from do_something import do_something as do_something

if __name__ == "__main__":
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(do_something, 1)
        print(f1.result())
    finish = time.perf_counter()
    print(start)
    print(finish)
    print(f'Finished in {round(finish-start, 2)} second(s)')

#=======Output========#
# Sleeping 1 second(s)...
# Done Sleeping...
# 157148.2493362
# 157149.3884936
# Finished in 1.14 second(s)