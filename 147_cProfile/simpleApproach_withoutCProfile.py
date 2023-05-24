import time
import sys

def add(x,y):
    res_sum = 0
    res_sum += x
    res_sum += y
    return res_sum

def fact(n):
    res=1
    for i in range(1, n+1):
        res *= i
    return res

def do_stuff():
    res=[]
    for x in range(100000):
        res.append(x ** 2)
    return res

def waste_time():
    time.sleep(5)
    print("Hello")

if __name__ == "__main__":
    sys.set_int_max_str_digits(100000000)  # Set the limit for integer string conversion
    print(add(100,5000))
    print(fact(7000))
    print(do_stuff())
    waste_time()