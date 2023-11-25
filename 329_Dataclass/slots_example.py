from dataclasses import dataclass

"""
Slots can be used to make classes faster and use less memory.
"""
@dataclass(slots=True)
class Person:
    name: str
    age: int
    job: str = None
    friends: list[str] = None

    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old and works as a {self.job}. His friends are: {self.friends}'

@dataclass()
class SimplePerson:
    name: str
    age: int
    job: str = None
    friends: list[str] = None

    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old and works as a {self.job}. His friends are: {self.friends}'
   

json: dict = {
    'name':'Bob',
    'age':20,
    'job':'Salesman',
    'friends':['Mario','Luigi']
}

bob1 = Person(json['name'], json['age'], json['job'], json['friends'])
bob2 = Person(json['name'], json['age'], json['job'], json['friends'])

print(bob1)
print(bob1==bob2)