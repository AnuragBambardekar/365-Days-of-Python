import socket

# CRC-32 parameters
CRC_POLYNOMIAL = 0xEDB88320
CRC_INITIAL = 0xFFFFFFFF

def calculate_crc(data):
    crc = CRC_INITIAL
    for byte in data:
        crc ^= byte
        for _ in range(8):
            crc = (crc >> 1) ^ (CRC_POLYNOMIAL & ~0 if crc & 1 else 0)
    return crc ^ CRC_INITIAL

"""
The verify_crc function checks if the received data has a valid CRC by comparing the calculated CRC with the received CRC.
data = data_with_crc[:-4]: Extract the data part by excluding the last 4 bytes, which represent the CRC value.

received_crc = int.from_bytes(data_with_crc[-4:], byteorder='big'): Extract the received CRC value from the last 4 bytes.

calculated_crc = calculate_crc(data): Calculate the CRC for the extracted data using the same calculate_crc function.

return received_crc == calculated_crc: Compare the received CRC with the calculated CRC. If they match, the data is considered intact.
"""
def verify_crc(data_with_crc):
    data = data_with_crc[:-4]
    received_crc = int.from_bytes(data_with_crc[-4:], byteorder='big')
    calculated_crc = calculate_crc(data)
    return received_crc == calculated_crc

def handle_client(client_socket):
    data_with_crc = client_socket.recv(1024)
    if not data_with_crc:
        return

    if verify_crc(data_with_crc):
        print("Data received intact.")
        client_socket.send(b"ACK")
    else:
        print("Data corrupted. Sending NAK.")
        client_socket.send(b"NAK")

    client_socket.close()

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)

    print("Server listening on port 12345")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connection from {addr}")

        # Handle each client in a separate thread or process
        client_handler = threading.Thread(target=handle_client, args=(conn,))
        client_handler.start()

if __name__ == "__main__":
    import threading

    # Start the server in a separate thread
    server_thread = threading.Thread(target=server)
    server_thread.start()
