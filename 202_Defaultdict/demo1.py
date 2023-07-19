from collections import defaultdict

# Create a defaultdict with a default value of 0
numbers = defaultdict(int)

numbers['one'] = 1
numbers['two'] = 2

print(numbers['one'])  # Output: 1
print(numbers['three'])  # Output: 0 (default value)

# Create a defaultdict with a default value of an empty list
fruits = defaultdict(list)

fruits['apple'].append('red')
fruits['apple'].append('green')
fruits['banana'].append('yellow')

print(fruits['apple'])  # Output: ['red', 'green']
print(fruits['banana'])  # Output: ['yellow']
print(fruits['orange'])  # Output: [] (default value, an empty list)
