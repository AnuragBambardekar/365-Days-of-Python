import timeit

# Reversing a string using slicing
def reverse_string_slice():
    text = "Hello, World!"
    reversed_text = text[::-1]

# Reversing a list using reverse() method
def reverse_list_reverse():
    my_list = [1, 2, 3, 4, 5]
    reversed_list = my_list.reverse()

# Reversing a list using slicing
def reverse_list_slice():
    my_list = [1, 2, 3, 4, 5]
    reversed_list = my_list[::-1]

# Reversing a tuple using slicing
def reverse_tuple_slice():
    my_tuple = (1, 2, 3, 4, 5)
    reversed_tuple = my_tuple[::-1]

# Reversing a dictionary keys using list() and slicing
def reverse_dict_keys_slice():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    reversed_keys = list(my_dict.keys())[::-1]

# Reversing a dictionary values using list() and slicing
def reverse_dict_values_slice():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    reversed_values = list(my_dict.values())[::-1]

# Measure the timing of each reversing function
print("Timing for reversing a string using slicing:", timeit.timeit(reverse_string_slice, number=100000))

print("Timing for reversing a list using reverse():", timeit.timeit(reverse_list_reverse, number=100000))
print("Timing for reversing a list using slicing:", timeit.timeit(reverse_list_slice, number=100000))

print("Timing for reversing a tuple using slicing:", timeit.timeit(reverse_tuple_slice, number=100000))

print("Timing for reversing dictionary keys using slicing:", timeit.timeit(reverse_dict_keys_slice, number=100000))
print("Timing for reversing dictionary values using slicing:", timeit.timeit(reverse_dict_values_slice, number=100000))
