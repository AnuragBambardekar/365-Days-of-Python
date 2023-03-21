import socket
"""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen()

# Work

server.close()
# All this can be put into a context manager
"""

# Using Context Managers
"""
class ServerSocket:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def __enter__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("localhost", 9999))
        self.server.listen()
        return self.server
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.server.close()

with ServerSocket("localhost", 9999) as server:
    server.accept()
"""

# Using Context Managers Library
from contextlib import contextmanager

@contextmanager
def server_socket(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.server.bind(("localhost", 9999))
    s.server.listen()
    yield s
    s.close()

with server_socket("localhost", 9999) as server:
    client, addr = server.accept()