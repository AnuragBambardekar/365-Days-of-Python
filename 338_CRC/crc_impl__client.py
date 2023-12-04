import socket
import zlib

def calculate_crc(data):
    crc = zlib.crc32(data)
    return crc.to_bytes(4, byteorder='big')

def client():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = "Hello, Server!"
    crc = calculate_crc(message.encode())

    # Introduce an error by changing a character in the message
    modified_message = message.replace('o', 'X')
    data_to_send = modified_message.encode() + crc

    # Append CRC to the message before sending
    # data_to_send = message.encode() + crc
    client_socket.sendall(data_to_send)

    response = client_socket.recv(1024)
    print(response.decode())

    client_socket.close()

if __name__ == "__main__":
    client()
