# Getting better at OOP's

class Human:
    def __init__(self, name, age, jobs=None):
        self.name = name
        self.age = age
        self.jobs = jobs

    def __init_subclass__(cls, meme=None):
        print(meme)

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f"Human({self.name!r}, age={self.age})"
    
    def __int__(self):
        return self.age
    
    def __add__(self, other):
        # should not work for instances of other classes
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.age + other.age
    
    def __sub__(self, other):
        # should not work for instances of other classes
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.age - other.age
    
    def __truediv__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.age / other.age
    
    def __floordiv__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.age // other.age
    
    def __mod__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.age % other.age
    
    def __mul__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.age * other.age
    
    def __iadd__(self, other): # similarly there are isub, imod, imul and so on.
        if not isinstance(other, self.__class__):
            return NotImplemented
        self.age += other.age
        return self
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.name == other.name
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        # print(self.age, other.age)
        return self.age < other.age
    # similarly le,lt,ge,gt

    def __contains__(self, value):
        return value in self.jobs
    
    def __getitem__(self, key):
        return self.jobs[key]

class Test(Human, meme="rickroll"): # inheriting Human Class and its subclass
    ...

print(Human("Bamba", 24)) # str is called
print(repr(Human("Bamba", 24))) # repr is called
print(int(Human("Bamba", 24))) # int is called
# print(hash(Human("Bamba", 24))) # default hash is called (This line doesn't execute when I added the __eq__ method in the class)

# Operator Overloads
print(Human("Bob",24)+Human("Alice",12))
print(Human("Bob",24)-Human("Alice",12))
print(Human("Bob",24)/Human("Alice",12))
print(Human("Bob",24)//Human("Alice",12))
print(Human("Bob",24)%Human("Alice",12))
print(Human("Bob",24)*Human("Alice",12))

alice = Human("Alice",12)
bob = Human("Bob",24)
ethan = Human("Ethan",6)
alice2 = Human("Alice",8)
# print(alice+bob+ethan)  # doesn't work!

alice += bob
print(alice.age)

# Comparison Operators
print(alice == bob) # checking age
print(alice != bob) # checking age
print(alice == alice2) # checking if names are equal
print(ethan < bob) # checking age

# Contains
Jack = Human("Jack", 23, "Programmer")
John = Human("John", 32, "Farmer")
print("Programmer" in Jack)

# getItem
Jonny = Human("Jack", 23, ["Programmer","Illustrator","Architect"])
print(Jonny[0])
print(Jonny[1])