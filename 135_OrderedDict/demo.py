from collections import OrderedDict
numbers = OrderedDict()

numbers["one"] = 1
numbers["two"] = 2
numbers["three"] = 3

print(numbers)

keys = ["one","two","three"]

print(OrderedDict.fromkeys(keys, 0))

# OrderedDict is a mutable data structure
numbers2 = OrderedDict(one=1, two=2, three=3)
print(numbers2)

numbers2["four"] = 4
print(numbers2)

del numbers2["one"]
print(numbers2)

numbers2["one"] = 1
print(numbers2)

# update
numbers2["one"] = 1.0
print(numbers2)

#======Unique features=====#
# Reordering items with move_to_end()

numbers3 = OrderedDict(one=1, two=2, three=3)
numbers3.move_to_end("two", True)
print(numbers3)

numbers3.move_to_end("two", False)
print(numbers3)