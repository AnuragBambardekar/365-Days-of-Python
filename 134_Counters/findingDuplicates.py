from collections import Counter

# find duplicate elements in a list
numbers = [1, 2, 3, 4, 2, 3, 1, 2, 2, 2]
duplicates = [element for element, count in Counter(numbers).items() if count > 1]
print(duplicates)

# find duplicate characters in a string
text = "This is a sample text with some duplicate characters."
duplicates = [char for char, count in Counter(text).items() if count > 1]
print(duplicates)
