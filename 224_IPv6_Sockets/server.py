import socket
from dotenv import load_dotenv
import os

# Go to CMD and type ipconfig

server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
# server.bind(("localhost", 9999))
# server.bind(("::1", 9999)) # IPv6 representation

# Load variables from .env file
load_dotenv()

# Get the IP address from the environment variable
my_ip_addr = os.getenv("MY_IP_ADDRESS")

if not my_ip_addr:
    raise ValueError("MY_IP_ADDRESS is not set in the .env file.")

server.bind((my_ip_addr, 9999))

server.listen()

while True:
    client, addr = server.accept()
    print(client.recv(1024).decode())
    client.send("Hello from server!".encode())