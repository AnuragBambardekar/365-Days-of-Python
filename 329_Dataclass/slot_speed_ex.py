from dataclasses import dataclass

@dataclass
class SimplePosition:
    name: str
    lon: float
    lat: float

@dataclass
class SlotPosition:
    __slots__ = ['name', 'lon', 'lat']
    name: str
    lon: float
    lat: float

from timeit import timeit
print(timeit('slot.name', setup="slot=SlotPosition('Oslo', 10.8, 59.9)", globals=globals()))

print(timeit('simple.name', setup="simple=SimplePosition('Oslo', 10.8, 59.9)", globals=globals()))

# about 35% faster