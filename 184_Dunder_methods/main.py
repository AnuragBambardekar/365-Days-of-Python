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


