import socket

def send_image(conn, filename):
    with open(filename, 'rb') as file:
        image_data = file.read()
        conn.sendall(image_data)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = 'localhost'  # Change this to your server IP address
    server_port = 9999  # Change this to an available port

    server_socket.bind((server_host, server_port))
    server_socket.listen(1)

    print("Server is listening on {}:{}".format(server_host, server_port))

    while True:
        conn, addr = server_socket.accept()
        print("Client connected:", addr)

        filename = 'image.jpg'  # Change this to the filename of your image
        send_image(conn, filename)

        conn.close()
        print("Image sent to client.")

if __name__ == '__main__':
    main()
