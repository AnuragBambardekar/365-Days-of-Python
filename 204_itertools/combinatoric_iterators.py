import itertools

# Permutations
perms = itertools.permutations([1, 2, 3], 2)
print(list(perms))

# Combinations
combs = itertools.combinations([1, 2, 3, 4], 2)
print(list(combs))

# Combinations with replacement
combs_with_replacement = itertools.combinations_with_replacement([1, 2, 3], 2)
print(list(combs_with_replacement))

# Cartesian Product
cartesian_product = itertools.product([1, 2], ['A', 'B'])
print(list(cartesian_product))
