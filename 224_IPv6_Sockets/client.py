import socket
from dotenv import load_dotenv
import os

client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
# client.connect(("localhost", 9999))
# client.connect(("::1", 9999)) # IPv6 representation

# Load variables from .env file
load_dotenv()

# Get the IP address from the environment variable
my_ip_addr = os.getenv("MY_IP_ADDRESS")

if not my_ip_addr:
    raise ValueError("MY_IP_ADDRESS is not set in the .env file.")

client.connect((my_ip_addr, 9999))

client.send("Hello from client!".encode())
print(client.recv(1024).decode())
