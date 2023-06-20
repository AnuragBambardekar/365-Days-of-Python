import socket

def receive_image(sock, filename):
    with open(filename, 'wb') as file:
        while True:
            data = sock.recv(1024)
            if not data:
                break
            file.write(data)

def main():
    server_host = 'localhost'  # Change this to your server IP address
    server_port = 9999  # Change this to the server port

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    filename = 'received_image.jpg'  # Change this to the desired filename for the received image
    receive_image(client_socket, filename)

    client_socket.close()
    print("Image received from server.")

if __name__ == '__main__':
    main()
