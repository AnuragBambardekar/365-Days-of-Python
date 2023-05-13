from collections import ChainMap

# create two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# create a ChainMap with the two dictionaries
chain_map = ChainMap(dict1, dict2)

# access keys in the ChainMap
print(chain_map['a']) # output: 1
print(chain_map['c']) # output: 3

# add a new dictionary to the ChainMap
dict3 = {'e': 5, 'f': 6}
chain_map = chain_map.new_child(dict3)

# access keys in the updated ChainMap
print(chain_map['e']) # output: 5
print(chain_map['b']) # output: 2 (from dict1)

# discard the last dictionary added to the ChainMap
chain_map = chain_map.parents

# access keys in the updated ChainMap
print(chain_map['d']) # output: 4 (from dict2)
print(chain_map['e']) # output: KeyError: 'e' (dict3 is discarded)
