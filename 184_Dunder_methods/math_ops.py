class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return self.value == other.value
        return False
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        if isinstance(other, MyClass):
            return self.value < other.value
        raise TypeError("Unsupported operand type(s) for <: MyClass and {}".format(type(other)))
    
    def __gt__(self, other):
        if isinstance(other, MyClass):
            return self.value > other.value
        raise TypeError("Unsupported operand type(s) for >: MyClass and {}".format(type(other)))
    
    def __le__(self, other):
        if isinstance(other, MyClass):
            return self.value <= other.value
        raise TypeError("Unsupported operand type(s) for <=: MyClass and {}".format(type(other)))
    
    def __ge__(self, other):
        if isinstance(other, MyClass):
            return self.value >= other.value
        raise TypeError("Unsupported operand type(s) for >=: MyClass and {}".format(type(other)))
    
    def __add__(self, other):
        if isinstance(other, MyClass):
            return MyClass(self.value + other.value)
        raise TypeError("Unsupported operand type(s) for +: MyClass and {}".format(type(other)))
    
    def __sub__(self, other):
        if isinstance(other, MyClass):
            return MyClass(self.value - other.value)
        raise TypeError("Unsupported operand type(s) for -: MyClass and {}".format(type(other)))
    
    def __mul__(self, other):
        if isinstance(other, MyClass):
            return MyClass(self.value * other.value)
        raise TypeError("Unsupported operand type(s) for *: MyClass and {}".format(type(other)))
    
    def __truediv__(self, other):
        if isinstance(other, MyClass):
            if other.value == 0:
                raise ZeroDivisionError("Division by zero")
            return MyClass(self.value / other.value)
        raise TypeError("Unsupported operand type(s) for /: MyClass and {}".format(type(other)))
    
    def __mod__(self, other):
        if isinstance(other, MyClass):
            if other.value == 0:
                raise ZeroDivisionError("Modulo by zero")
            return MyClass(self.value % other.value)
        raise TypeError("Unsupported operand type(s) for %: MyClass and {}".format(type(other)))
    
    def __repr__(self):
        return f"MyClass({self.value})"


# Testing the dunder methods

obj1 = MyClass(10)
obj2 = MyClass(5)

# Equality
print(obj1 == obj2)  # Output: False
print(obj1 != obj2)  # Output: True

# Comparison
print(obj1 < obj2)   # Output: False
print(obj1 > obj2)   # Output: True
print(obj1 <= obj2)  # Output: False
print(obj1 >= obj2)  # Output: True

# Arithmetic operations
print(obj1 + obj2)   # Output: MyClass(15)
print(obj1 - obj2)   # Output: MyClass(5)
print(obj1 * obj2)   # Output: MyClass(50)
print(obj1 / obj2)   # Output: MyClass(2.0)
print(obj1 % obj2)   # Output: MyClass(0)
