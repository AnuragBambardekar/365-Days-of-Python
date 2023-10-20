from visualiser.visualiser import Visualiser as vs

@vs()
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    n = 5 
    print(f"Fibonacci({n}) = {fibonacci(n)}")
    vs.make_animation("fibonacci.gif", delay=2)

if __name__ == "__main__":
    main()
