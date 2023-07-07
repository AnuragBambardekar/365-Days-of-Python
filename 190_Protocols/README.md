# Why you need Protocols ?

Python is a dynamically typed language.

Dynamic typing a.k.a. *Duck Typing* means types are checked at runtime and type declarations are not required. Also lots of flexibility.

```python
def my_func(a,b,c):
    return a+b-c

result = my_func(5,3,2)
```

Static typing means types are checked at compile time and type declarations are required.

```java
int my_func(int a, int b, int c)
{ return a+b-c }

int result = my_func(5,3,2)
```

## Duck (Dynamic) Typing
```python
class Duck:
    def walk(self):
        ...
    
    def quack(self):
        ...

duck = Duck()
duck.walk()
duck.quack()

class Donkey:
    def walk(self):
        ...

duck = Donkey()
duck.walk()
duck.quack() 

>> Attribute Error: 'Donkey' object has no attribute 'quack'

class ImpostorDuck:
    def walk(self):
        ...
    
    def quack(self):
        not_quite_quacking()
    
duck = ImpostorDuck()
duck.walk()
duck.quack()

# This is fine, ImpostorDuck is a Duck after all and Python doesn't worry about this since it has same behavior as a Duck.
```

**The downside of Duck Typing is that there is no type checking except at *runtime* which can be too late**

So, in order to fix this, we have **Type Hints**

```python
class Duck:
    def eat_bread(self):
        ...
    
    def swim(self):
        ...

def feed_the_duck(duck: Duck):
    duck.eat_bread()

duck = Duck()
feed_the_duck(duck)

class Monkey:
    def eat_bananas(self):
        ...

    def climb_trees(self):
        ...

monkey = Monkey()
feed_the_duck(monkey)

>> Attribute Error: 'Monkey' object has no attribute 'eat_bread'
```

```python
class Duck:
    def eat_bread(self):
        pass

def feed_bread(animal: Duck):
    animal.eat_bread()
```

```python
from typing import Union

class Duck:
    def eat_bread(self):
        pass

class Pig:
    def eat_bread(self):
        pass

def feed_bread(animal: Union[Duck, Pig]):
    animal.eat_bread()
```

So, in summary - Type Hints: <br>
- Type declarations are optional
- Optional static type checking
- Can not adapt type hints of imported code

## ABC - Abstract Based Classes

ABCs are base classes or classes that you can inherit from, but they cannot be instantiated. <br>
Used to define interface of what subclasses should look like.

```python
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass # Needs implementation by subclass

my_animal = Animal()

>> TypeError: Cannot instantiate Animal

# But, what we can do is:

class Duck(Animal):
    def walk(self):
        ...

duck = Duck()
assert isinstance(duck, Animal) # True
```

Going back to the eat bread example:

```python
from abc import ABCMeta, abstractmethod

class EatsBread(metaclass=ABCMeta):
    @abstractmethod
    def eat_bread(self):
        pass

class Duck(EatsBread):
    def eat_bread(self):
        ...

class Pig(EatsBread):
    def eat_bread(self):
        ...

def feed_bread(animal: EatsBread):
    animal.eat_bread()

class Bamba(EatsBread):
    def eat_bread(self):
        ...

feed_bread(Bamba()) # OK
```

So, ABCs:
- More structure to your types
- Type hints do not need updates for new subclasses
- Difficulties combining classes from other libraries
- Virtual subclasses need explicit registering

## Protocols [Introduced in Python 3.8]
a.k.a. *Structural Subtyping* or *static duck typing*

A protocol is a special case of ABC.

```python
from typing import Protocol

class EatsBread(Protocol):
    def eat_bread(self):
        pass

def feed_bread(animal: EatsBread):
    animal.eat_bread()

# Duck is implicitly a subtype of EatsBread
class Duck:
    def eat_bread(self):
        ...

feed_bread(Duck()) # OK

# Bamba is also implicitly a subtype of EatsBread
class Bamba:
    def eat_bread(self):
        ...

feed_bread(Bamba()) # Ok
```

### Predefined Protocols

#### Iterable [T]

```python
def __iter__(self) -> Iterator[T]:
```

#### Iterator [T]

```python
def __next__(self) -> T:
def __iter__(self) -> Iterator[T]:
```

#### Sized
```python
def __len__(self) -> int:
```

# Summary of Protocols
- No need to inherit or  register
- Best of both worlds: static checking of dynamic types

A protocol is a structural interface that defines a set of methods or attributes that a class can implement. It is a way to define a contract that a class can adhere to without explicitly inheriting from a specific base class.

Protocols allow you to specify the expected behavior of objects without dictating their inheritance hierarchy. They provide a mechanism for static type checking and can be used by type checkers and linters to verify that a class conforms to the defined interface.

ABC (Abstract Base Class) is a mechanism in Python that allows you to define abstract classes. An abstract class is a class that cannot be instantiated directly and is meant to be subclassed by concrete (non-abstract) classes. Abstract base classes provide a way to define a common interface that subclasses should implement.

While protocols and abstract base classes share some similarities, there are a few key differences:

Inheritance vs. Structural: ABC emphasizes the inheritance hierarchy, where a subclass is expected to inherit from an abstract base class. Protocols, on the other hand, focus on the structural interface, specifying the required methods and attributes without dictating the inheritance hierarchy.

Subclassing vs. Implementing: With ABC, a subclass must explicitly inherit from the abstract base class and provide implementations for all the abstract methods. Protocols, on the other hand, allow any class to implement the required methods and attributes without explicit subclassing.

Runtime vs. Static Checking: ABC is enforced at runtime. If a subclass fails to implement an abstract method, a TypeError is raised. Protocols, on the other hand, are primarily used for static type checking. They provide hints to type checkers and linters to verify that a class conforms to the protocol but are not strictly enforced at runtime.
