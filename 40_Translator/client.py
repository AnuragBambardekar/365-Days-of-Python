import socket
import googletrans

x = googletrans.LANGUAGES

""" # Print the names of the columns.
print("{:<10} {:<10}".format('langCode', 'Language'))
 
# print each data item.
for key, value in x.items():
    print("{:<10} {:<10}".format(key, value))

lang = input("Enter your language: ") """



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
client.connect(("localhost", 8000))

while True:
    message = input("Enter message to translate to English: ")
    # print(message)
    if message == '!q':
        client.close()
        break
    else:
        # client.send(f"[{lang}{message}]".encode())
        client.send(f"[{message}]".encode())