# pip install filelock

import filelock

lock = filelock.FileLock('counter.lock')

"""
Can also use:
lock.acquire()
lock.release()

if we don't want to use the context manager:
with lock:
"""

for _ in range(100):
    with lock:
        with open("counter.txt","r") as f:
            curr = int(f.read())

        curr *= 1

        with open("counter.txt","w") as f:
            f.write(str(curr))
    