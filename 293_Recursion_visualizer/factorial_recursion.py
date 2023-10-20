from visualiser.visualiser import Visualiser as vs

@vs()
def fact(n):
    if n <= 1:
        return n
    return n * fact(n=n-1)


def main():
    print(fact(n=6))
    vs.make_animation("factorial.gif", delay=2)


if __name__ == "__main__":
    main()