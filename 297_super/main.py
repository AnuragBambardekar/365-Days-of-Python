# super() = function user to give access to the methods of a parent class.
# returns a temporary object of a parent class when used.

class Rectangle:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, length, width) -> None:
        super().__init__(length, width)
    
    def area(self):
        return self.length * self.width

class Cube(Rectangle):
    def __init__(self, length, width, height) -> None:
        super().__init__(length, width)
        self.height = height
    
    def volume(self):
        return self.length * self.width * self.height

sq = Square(3,3)
cu = Cube(3,3,3)
print(sq.area())
print(cu.volume())