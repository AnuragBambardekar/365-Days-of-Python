# Before running this script, we must run the following commands:
# gcc -c -Wall -Werror -fpic sum.c 
# gcc -shared -o libsum.so sum.o

from ctypes import CDLL

# Load the shared library (.so file on Linux, .dll file on Windows)
lib = CDLL('./libsum.so')

# Call the 'add' function from the shared library
sum = lib.add(2, 3)

# Print the result
print("The sum is", sum)