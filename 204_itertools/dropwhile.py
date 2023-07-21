import itertools as it
import json

with open("204_itertools/data.json","r") as f:
    data = json.load(f)

for k,v in it.dropwhile(lambda x: x[0] != "address", data.items()): # drop everything before "address"
    print(k,v)

print()

for k,v in it.takewhile(lambda x: x[0] != "address", data.items()): # drop everything before "address"
    print(k,v)