from icecream import ic

def myfunc(val):
    if val%2 == 0:
        ic() # to see where we are at in the code
        return True
    else:
        ic()
        return False
    
print(myfunc(10))
print(myfunc(11))
print(myfunc(12))

ic.disable()

print(myfunc(10))
print(myfunc(11))
print(myfunc(12))

ic.enable()

print(myfunc(10))
print(myfunc(11))
print(myfunc(12))