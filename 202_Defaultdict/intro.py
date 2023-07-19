"""
Dictionaries
"""

# mydict = {}
# print(type(mydict))

# mydict = dict()
# print(type(mydict))

# print(mydict['name']) # KeyError: 'name'
# mydict['age'] += 10 # KeyError: 'age'

"""
This error can be solved using defaultdict
"""

from collections import defaultdict

mydict = defaultdict(int)
print(mydict)

print(mydict['age']) # 0 --> default value assigned
print(mydict)

mydict['some_other_value'] += 20
print(mydict)


# values = {
#     "person1": 0,
#     "person2": 0,
#     "person3": 0,
# }

values = defaultdict(int)

values['person4'] += 10 # this will not work if you don't have a defaultdict
print(values)