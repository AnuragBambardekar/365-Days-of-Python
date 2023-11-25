# Dataclass

- Introduced in Python 3.7+
- A data class is a class typically containing mainly data, although there aren't really any restrictions.
- It is created using the new @dataclass decorator.

- A data class is a regular Python class. The only thing that sets it apart is that it has basic data model methods like `.__init__()`, `.__repr__()`, and `.__eq__()` implemented for you.

```py
from dataclasses import dataclass

@dataclass
class DataClassCard:
    rank: str
    suit: str
```

## Alternatives to Data Classes

Tuple or a dict can be used.
```py
queen_of_hearts_tuple = ('Q', 'Hearts')
queen_of_hearts_dict = {'rank': 'Q', 'suit': 'Hearts'}
```

It works. However, it puts a lot of responsibility on you as a programmer:

- You need to remember that the queen_of_hearts_... variable represents a card.

- For the tuple version, you need to remember the order of the attributes. Writing ('Spades', 'A') will mess up your program but probably not give you an easily understandable error message.

- If you use the dict version, you must make sure the names of the attributes are consistent. For instance {'value': 'A', 'suit': 'Spades'} will not work as expected.

We can also use namedtuple
```py
from collections import namedtuple

NamedTupleCard = namedtuple('NamedTupleCard', ['rank', 'suit'])
```

**Why even use dataclasses instead of namedtuple ?**

- Data classes come with many more features than you have seen so far. At the same time, the namedtuple has some other features that are not necessarily desirable.

- For instance, it will also happily compare two different namedtuple classes.
```py
Person = namedtuple('Person', ['first_initial', 'last_name'])
ace_of_spades = NamedTupleCard('A', 'Spades')
ace_of_spades == Person('A', 'Spades')
True
```

-  A namedtuple is also by nature immutable.