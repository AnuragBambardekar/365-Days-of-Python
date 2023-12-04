import socket

"""
The calculate_crc function is responsible for calculating the CRC-32 value for a given data input. 
This function uses the CRC-32 algorithm, which involves XOR and bit-wise operations.
crc = CRC_INITIAL: Initialize the CRC value with a predefined initial value (CRC_INITIAL).

for byte in data: Iterate through each byte in the input data.

crc ^= byte: XOR the current byte with the current CRC value.

for _ in range(8): Perform the following operations 8 times (once for each bit in the byte).

crc = (crc >> 1) ^ (CRC_POLYNOMIAL & ~0 if crc & 1 else 0): Right shift the CRC value by 1 bit. If the least significant bit (LSB) of the current CRC value is 1, XOR it with the CRC polynomial (CRC_POLYNOMIAL).
return crc ^ CRC_INITIAL: XOR the final CRC value with the initial value to obtain the CRC checksum.
"""
def calculate_crc(data):
    crc = 0xFFFFFFFF
    for byte in data:
        crc ^= byte
        for _ in range(8):
            crc = (crc >> 1) ^ (0xEDB88320 & ~0 if crc & 1 else 0)
    return crc ^ 0xFFFFFFFF

def add_crc(data):
    crc_value = calculate_crc(data.encode())
    return data.encode() + crc_value.to_bytes(4, byteorder='big')

def client(data):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    data_with_crc = add_crc(data)
    client_socket.sendall(data_with_crc)

    response = client_socket.recv(1024)
    print(f"Server response: {response.decode()}")

    client_socket.close()

if __name__ == "__main__":
    # Simulate a client sending data
    client_data = "Hello, Server!"
    client(client_data)
