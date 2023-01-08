import multiprocessing
import time

t1 = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

processes = []

for _ in range(10):
    p = multiprocessing.Process(target=do_something)
    p.start()
    processes.append(p)

for process in processes:
    process.join()

t2 = time.perf_counter()

print(t1)
print(t2)
print(f"Finished in {round(t2-t1, 2)} second(s)")


#=========Output===========#
# RuntimeError:
#         An attempt has been made to start a new process before the
#         current process has finished its bootstrapping phase.

#         This probably means that you are not using fork to start your
#         child processes and you have forgotten to use the proper idiom
#         in the main module:

#             if __name__ == '__main__':
#                 freeze_support()
#                 ...

#         The "freeze_support()" line can be omitted if the program
#         is not going to be frozen to produce an executable.
# 156960.0477813
# 156960.2098818
# Finished in 0.16 second(s)