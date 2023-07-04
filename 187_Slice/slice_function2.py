string = "Hello, World!"
s = slice(5)
print(string[s])

my_list = [1, 2, 3, 4, 5]
s = slice(2, 4)
print(my_list[s])

# Slicing with step size
my_tuple = (1, 2, 3, 4, 5)
s = slice(1, 5, 2)
print(my_tuple[s]) 

numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
even = [x for x in numbers if x % 2 == 0]

#========Reversing a sequence==============#

my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]  # [5, 4, 3, 2, 1]
print(reversed_list)