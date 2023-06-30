import struct

# This is useful when working with sockets

company = b"BambaCo"
day,month,year = 1,1,2023
awesome = True

byte_stream = struct.pack("10s 3i ?", company, day, month, year, awesome) # we dont have an identifier for string, so add a bunch of characters

print(byte_stream)

company, day, month, year, awesome = struct.unpack("10s 3i ?", byte_stream)
print(company, day, month, year, awesome)

# Can also write to a file
with open("data","wb") as f:
    f.write(byte_stream)

with open("data","rb") as f:
    data = f.read()

company, day, month, year, awesome = struct.unpack("10s 3i ?", data)
print(company, day, month, year, awesome)