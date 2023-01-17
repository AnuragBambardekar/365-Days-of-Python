""" import time
start = time.perf_counter()
def do_something():
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done Sleeping!")

do_something()
do_something()

finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s)") """


#------Threading------#
""" import threading
import time
start = time.perf_counter()
def do_something():
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done Sleeping!")

#Create Threads
t1 = threading.Thread(target=do_something) #pass the function by itself unexecuted
t2 = threading.Thread(target=do_something) #pass the function by itself unexecuted

#Run threads
t1.start()
t2.start()

#Join method
t1.join()
t2.join()

finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s)")  """


""" import threading
import time
start = time.perf_counter()
def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    print("Done Sleeping!")

#append all threads
threads = []

#start all threads
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5]) #sleep for 1.5 seconds
    t.start()
    threads.append(t) #append each thread we started

#Run join
for thread in threads:
    thread.join()

finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s)")  """

#using threadpoolexecutor
import concurrent.futures
import time
start = time.perf_counter()
def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return "Done Sleeping!"

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something, 1) #1 second
    print(f1.result())

finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s)") 