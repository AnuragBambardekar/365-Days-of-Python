from collections import Counter

# create a list of elements
elements = [1, 2, 3, 4, 2, 3, 1, 2, 2, 2]

# create a Counter object from the list
counter = Counter(elements)

# print the Counter object
print(counter)

# get the most common element
most_common = counter.most_common(1)
print(f"The most common element is {most_common[0][0]} with a count of {most_common[0][1]}")
