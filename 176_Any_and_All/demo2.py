numbers = [0, 1, 2, 3, 4]
result = any(numbers)
print(result)

empty_list = []
result = any(empty_list)
print(result) 

words = ["apple", "", "banana", ""]
result = any(words)
print(result)

# all()

numbers = [1, 2, 3, 4, 5]
result = all(numbers)
print(result) 

empty_list = []
result = all(empty_list)
print(result) 

words = ["apple", "banana", "cherry"]
result = all(words)
print(result) 

mixed_values = [True, 10, "hello", None]
result = all(mixed_values)
print(result) 

zeros = [0, 0, 0, 0]
result = all(zeros)
print(result)

# Application - Boolean Aggregation

def has_positive_numbers(numbers):
    return any(num > 0 for num in numbers)

def all_even(numbers):
    return all(num % 2 == 0 for num in numbers)

list1 = [-1, 0, 2, -3, 4]
list2 = [2, 4, 6, 8, 10]

# Check if any positive number exists in the list
if has_positive_numbers(list1):
    print("List 1 contains at least one positive number.")
else:
    print("List 1 does not contain any positive number.")

# Check if all numbers in the list are even
if all_even(list2):
    print("All numbers in List 2 are even.")
else:
    print("List 2 contains at least one odd number.")
