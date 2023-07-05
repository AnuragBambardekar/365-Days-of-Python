from typing import TypedDict, Optional

"""
TypedDict is a type hint introduced in Python 3.8 as part of the typing module. 
It allows you to define dictionary-like objects with specific key-value types, providing static type checking and improving code clarity.

"""


class Coordinate(TypedDict):
    x: float
    y: float
    label: str
    category: Optional[str]

coordinate = {'x':10, 'y':10} # Doesnt conform to the parameters of class Coordinate

coordinate1: Coordinate = {'x':10, 'y':10, 'label':'Profit','category':'Finance'} # Code editor now prompts you
coordinate2: Coordinate = {'x':15, 'y':14, 'label':'Loss'} # Code editor now prompts you

print(coordinate)
print(coordinate1)
print(coordinate2)
