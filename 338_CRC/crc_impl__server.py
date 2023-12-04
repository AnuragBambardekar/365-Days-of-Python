import socket
import zlib

def calculate_crc(data):
    crc = zlib.crc32(data)
    return crc.to_bytes(4, byteorder='big')

def server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        data = client_socket.recv(1024)
        if not data:
            break

        received_crc = data[-4:]
        data_without_crc = data[:-4]

        calculated_crc = calculate_crc(data_without_crc)
        if received_crc == calculated_crc:
            print("CRC check passed. Data received:", data_without_crc.decode())
            client_socket.sendall(b"ACK")
        else:
            print("CRC check failed. Data corrupted.")

        client_socket.close()

if __name__ == "__main__":
    server()
