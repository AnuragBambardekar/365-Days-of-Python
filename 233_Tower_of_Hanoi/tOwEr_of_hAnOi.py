def move(f,t):
    """
    f: from
    t: to
    """
    print(f"Move disc from {f} to {t}")

def moveVia(f,v,t):
    """
    f: from
    v: via
    t: to
    """
    move(f,v)
    move(v,t)

# move("A","C")
# moveVia("A","B","C")

# Recursion (Super Power)
def hanoi(n,f,h,t):
    """
    n: number of disks
    f: from
    h: helper
    t: to
    """
    if n==0:
        pass
    else:
        hanoi(n-1,f,t,h)
        move(f,t)
        hanoi(n-1,h,f,t)

hanoi(3,"A","B","C")