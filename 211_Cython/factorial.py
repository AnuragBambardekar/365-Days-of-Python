def factorial(x):
    f=1
    for i in range(x):
        f *= (x-i)
    return f

print(factorial(5))