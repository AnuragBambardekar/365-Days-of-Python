from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

pos1 = Position('Oslo', 10.8, 59.9)
print(pos1)
print(pos1.lat)
print(f'{pos1.name} is at {pos1.lat}°N, {pos1.lon}°E')

pos2 = Position('Null Island')
print(pos2)

pos3 = Position('Greenwich', lat=51.8)
print(pos3)

pos4 = Position('Vancouver', -123.1, 49.3)
print(pos4)


"""
Alternative declaration of dataclasses
"""
from dataclasses import make_dataclass

Position = make_dataclass('Position', ['name', 'lat', 'lon'])



"""
Dataclass without explicit data types
"""
from typing import Any

@dataclass
class WithoutExplicitTypes:
    name: Any
    value: Any = 42

