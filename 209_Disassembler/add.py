import dis

def add1(x,y):
    return x+y

def add2(x,y,z):
    return x+y+z

print(dis.dis(add1)) # returns the python bytecode
print(dis.dis(add2)) # returns the python bytecode