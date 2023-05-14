from collections import namedtuple

"""
namedtuple is a Python class from the collections module that allows you to create a subclass of tuple with named fields. 
It's a convenient way to define a simple class that only contains some data fields and no methods.
"""

# create a namedtuple class
Person = namedtuple('Person', ['name', 'age', 'gender'])

# create an instance of the Person class
person1 = Person('John', 30, 'Male')

# access the fields using the dot notation
print(person1.name)    # output: 'John'
print(person1.age)     # output: 30
print(person1.gender)  # output: 'Male'
