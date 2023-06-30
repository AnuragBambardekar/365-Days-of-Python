"Allows to package binary data in a structured way"

import struct

byte_stream = struct.pack("iii", 10, 20, 30) # iii means 3 integers, can also write it as 3i
# byte_stream = struct.pack("hhh", 10, 20, 30) # iii means 3 short integers
print(byte_stream)
print(struct.calcsize("i")) # using 4 bytes to represent an integer
print(struct.calcsize("h")) # using 2 bytes to represent an integer

a, b, c = struct.unpack("iii", byte_stream)
print(a,b,c)



# We can also unpack 2 unsigned short ints as 1 int
byte_stream = struct.pack("HH", 10, 20)
a = struct.unpack("i", byte_stream)
print(a)