from collections import namedtuple

Point2D = namedtuple('Point2D', ['x', 'y'])

def distance(p1, p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
    
# Usage example
p1 = Point2D(1, 2)
p2 = Point2D(4, 6)
print(distance(p1, p2))  # output: 5.0
