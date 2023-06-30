import socket
import struct

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen()

client, addr = server.accept()
data = client.recv(1024)

first_name, last_name, age, gender, occupation, weight = struct.unpack("15s 15s i 15s 15s f", data)

print(first_name.decode().rstrip("\x00"), last_name.decode().rstrip("\x00"), age, gender.decode().rstrip("\x00"), occupation.decode().rstrip("\x00"), round(weight,2))