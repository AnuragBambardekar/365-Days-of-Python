class MyClass:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"MyClass object (name: {self.name})"
    
    def __repr__(self):
        return f"MyClass('{self.name}')"
    
    def __len__(self):
        return len(self.name)
    
    def __getitem__(self, index):
        return self.name[index]
    
    def __setitem__(self, index, value):
        self.name = self.name[:index] + value + self.name[index+1:]
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index >= len(self.name):
            raise StopIteration
        else:
            result = self.name[self.index].upper()
            self.index += 1
            return result


# Testing the dunder methods

obj = MyClass("Hello")

# __str__ and __repr__
print(str(obj))  # Output: MyClass object (name: Hello)
print(repr(obj))  # Output: MyClass('Hello')

# __len__
print(len(obj))  # Output: 5

# __getitem__
print(obj[1])  # Output: e

# __setitem__
obj[0] = "J"
print(obj.name)  # Output: Jello

# __iter__ and __next__
for letter in obj:
    print(letter, end=" ")  # Output: J e l l o


"""
Explanation:

__init__ is the constructor method that initializes the name attribute of an object.
__str__ and __repr__ define string representations of the object. The former is used for informal string representation, while the latter is used for the official representation.
__len__ returns the length of the name attribute.
__getitem__ enables indexing on the object.
__setitem__ allows assignment of values to specific indices.
__iter__ and __next__ enable iteration over the object.
"""

"""
Even without the __str__ method, we can still obtain a string representation of the object using the repr() function. 
Additionally, the object remains iterable due to the fallback behavior provided by the __getitem__ method.

It's important to note that while Python allows you to omit certain dunder methods, 
it's generally a good practice to define them for clarity and to ensure the expected behavior of your custom objects.

So, I added .upper() to the __next__ dunder function to see difference.
"""


"""
Applications:

Comparison and Equality:

__eq__, __ne__, __lt__, __gt__, __le__, __ge__: These methods allow you to define the behavior of comparison operators (==, !=, <, >, <=, >=) for objects of your class.
Arithmetic Operations:

__add__, __sub__, __mul__, __div__, __mod__: These methods enable you to define the behavior of arithmetic operators (+, -, *, /, %) for objects of your class.
__radd__, __rsub__, __rmul__, __rdiv__, __rmod__: These methods define the right-hand side versions of the arithmetic operations, allowing operations with objects of your class on the right side of the operator.
Container and Membership:

__contains__: Allows you to define the behavior of the in operator for checking membership in objects of your class.
__len__: Enables you to define the length of objects, making them compatible with the len() function.
__getitem__, __setitem__: These methods allow objects to behave as containers, supporting item access and assignment using square brackets.
Callable Objects:

__call__: Defines the behavior of calling an object as if it were a function. It allows you to make instances of your class callable.
Context Managers:

__enter__, __exit__: These methods enable you to create context managers using the with statement, defining the setup and teardown procedures for the context.
Attribute Access and Management:

__getattr__, __setattr__, __delattr__: These methods control the behavior when getting, setting, and deleting attributes of an object.
__getattribute__: Provides a general attribute access mechanism and is called for every attribute access.
Hashing:

__hash__: Allows you to define a custom hash value for objects, enabling them to be used in hash-based collections like dictionaries and sets.
"""