number: int = 1_000_000_000
print(number)

_ = 10 # Assignment

for _ in range(3):
    print('hello')
    print(_)

try:
    result = 1/0
except ZeroDivisionError as _:
    print('Error Handled!')

# Unpacking tuples
ex1 = (1,2,3,4)
a, _, b, _ = ex1
print(a,b)

ex2 = (1,2,3,4,5)
a, *_, b = ex2
print(a,b)
print(_)

#UUID
from uuid import uuid4

class User:
    def __init__(self):
        self._id = uuid4()
    
    def _get_id(self):
        return self._id

user = User()    
# user. # cannot use the member functions

# if we want to use it
"""
class User:
    def __init__(self):
        self.__id = uuid4()
    
    def __get_id(self):
        return self.__id

user = User()    
print(user._get_id())
"""

#Use keywords as variables
if_ = 10
class_ = 'class'


class Fruit:
    def __init__(self):
        self.id = uuid4()

    def __str__(self):
        return f'Fruit: {self.id}'
    
    def __int__(self):
        return 4

fruit = Fruit()
print(fruit)
print(10 + int(fruit))
