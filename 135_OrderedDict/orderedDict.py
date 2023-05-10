from collections import OrderedDict

# Create an empty ordered dictionary
od = OrderedDict()

# Add some key-value pairs
od['a'] = 1
od['b'] = 2
od['c'] = 3

# Print the ordered dictionary
print(od)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Access the values using keys
print(od['a'])  # 1

# Iterate over the key-value pairs in order
for key, value in od.items():
    print(key, value)  # a 1   b 2   c 3

# Move a key to the end of the ordered dictionary
od.move_to_end('a')
print(od)  # OrderedDict([('b', 2), ('c', 3), ('a', 1)])
