import dis

"""
The is operator is used to compare the identity of two objects, meaning it checks if two variables or expressions refer to the 
same memory location. 
It returns True if the objects have the same identity and False otherwise.
"""

"""
The == operator is used to compare the values of two variables or expressions to check if they are equal. 
It returns True if the values are equal, and False otherwise.
"""

# In summary, == checks for value equality, and is checks for object identity.

def test():
    a = 1000
    b = 1000

    # b+=2

    print(a==b) # True
    print(a is b) # True

    print(id(a))
    print(id(b))

print(dis.dis(test))
test()