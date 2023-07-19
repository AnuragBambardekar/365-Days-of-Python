from collections import defaultdict

class MyDefaultDict(defaultdict):
    def __missing__(self, key):
        self[key] = value = len(key) # default value will now be length of the word
        return value
    
test = MyDefaultDict()
print(test["hello"])
print(test["hi"])
print(test)