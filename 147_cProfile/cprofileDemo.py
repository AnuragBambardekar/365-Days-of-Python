import cProfile
import time

# SIMULATING A WEBSITE BACKEND

def api_call():
    time.sleep(2)
    return None

# Simulate Processing Data
def process_data():
    for i in range(10**7):
        pass

def sort_data():
    for i in range(10**8):
        pass

    process_data()

def reload_page():
    process_data()
    sort_data()
    time.sleep(2)

def main():
    api_call()
    sort_data()
    reload_page()

if __name__ == '__main__':
    print("Timing Program...")

    cProfile.run('main()', sort='cumtime')


"""
OUTPUT

Timing Program...
         13 function calls in 6.692 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    6.692    6.692 {built-in method builtins.exec}
        1    0.000    0.000    6.692    6.692 <string>:1(<module>)
        1    0.000    0.000    6.692    6.692 cprofileDemo.py:26(main)
        2    4.014    2.007    4.014    2.007 {built-in method time.sleep}
        1    0.000    0.000    3.433    3.433 cprofileDemo.py:21(reload_page)
        2    2.305    1.153    2.558    1.279 cprofileDemo.py:15(sort_data)
        1    0.000    0.000    2.010    2.010 cprofileDemo.py:6(api_call)
        3    0.373    0.124    0.373    0.124 cprofileDemo.py:11(process_data)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""