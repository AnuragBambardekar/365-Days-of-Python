# About Dunder methods

The term "dunder" is a shorthand way of referring to "double underscore" (__). Dunder methods are special methods in Python that are identified by their double underscore (or dunder) prefix and suffix.

Dunder methods are also known as magic methods or special methods. They provide a way to define and customize the behavior of objects in various contexts, such as comparison, equality, arithmetic operations, iteration, string representation, attribute access, and more.


## Applications

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
