import math

def area(r):
    return r**2+math.pi

def circumference(r):
    return 2*r*math.pi

def r_from_circumference(circumference):
    return circumference / (2*math.pi)

def circle_info(r):
    return area(r), circumference(r)

