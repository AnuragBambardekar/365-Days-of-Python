class MyClass:
    def __init__(self):
        self.public_var = "This is a public variable"
        self._protected_var = "This is a protected variable"
        self.__private_var = "This is a private variable"

    def public_method(self):
        return "This is a public method"

    def _protected_method(self):
        return "This is a protected method"

    def __private_method(self):
        return "This is a private method"


obj = MyClass()

# Accessing public members
print(obj.public_var) 
print(obj.public_method())

# Accessing protected members
print(obj._protected_var)
print(obj._protected_method())

# Accessing private members
# print(obj.__private_var) # AttributeError: 'MyClass' object has no attribute '__private_var'
# print(obj.__private_method()) # AttributeError: 'MyClass' object has no attribute '__private_method'. Did you mean: '_protected_method'?

# However, we can still access them using the mangled names:
print(obj._MyClass__private_var)
print(obj._MyClass__private_method())
