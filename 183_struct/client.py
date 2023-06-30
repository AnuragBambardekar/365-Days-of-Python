import socket
import struct

first_name = "Anurag"
last_name = "Bambardekar"
age = 35
gender = "male"
occupation = "Programmer"
weight = 70.45

# We can either use .encode() to convert to byte or add a 'b' in front of the string above so like: b"Anurag"

data = struct.pack("15s 15s i 15s 15s f", first_name.encode(), last_name.encode(), age, gender.encode(), occupation.encode(), weight)
print(data)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

client.send(data)
client.close()
