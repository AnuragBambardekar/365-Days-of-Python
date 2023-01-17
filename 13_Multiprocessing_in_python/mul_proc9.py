import concurrent.futures
import time
import sys  
sys.path.insert(0, 'Multiprocessing_in_python\do_something1.py')
from do_something1 import do_something1 as do_something1

if __name__ == "__main__":
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5,4,3,2,1]
        results = [executor.submit(do_something1, sec) for sec in secs]
    
    for f in concurrent.futures.as_completed(results):
        print(f.result())
    finish = time.perf_counter()
    print(start)
    print(finish)
    print(f'Finished in {round(finish-start, 2)} second(s)')


#=========Output==========#
# Sleeping 5 second(s)...
# Sleeping 4 second(s)...
# Sleeping 3 second(s)...
# Sleeping 2 second(s)...
# Sleeping 1 second(s)...
# Done Sleeping...2
# Done Sleeping...4
# Done Sleeping...1
# Done Sleeping...5
# Done Sleeping...3
# 157744.8722569
# 157750.0341956
# Finished in 5.16 second(s)