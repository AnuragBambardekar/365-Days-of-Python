data = "abcefgxyz"

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b

if __name__ == '__main__':
    fib(10)

"""
pyarmor cfg enable_trace=1
pyarmor gen --mix-str --assert-call fib.py
cat .pyarmor/pyarmor.trace.log

Then check the .pyarmor/pyarmor.trace.log
String constant abcefgxyz and function fib will be protected.
"""