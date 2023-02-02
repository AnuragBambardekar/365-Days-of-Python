import socket
import googletrans

translator = googletrans.Translator()
server_lang = "en"

#server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 8000))
    server.listen()
    print ("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))

client, addr = server.accept()
while True:
    message = client.recv(1024).decode()
    # print(message)
    # lang = message[1:3]
    # print(lang)
    # msg = message[3:-1]
    msg = message[1:-1]
    
    # Detect language of user input, rather than asking them to explicitly enter language
    dec_lan = googletrans.Translator().detect(msg)
    print(dec_lan)
    # print(msg)
    translation = translator.translate(msg,src=dec_lan.lang, dest=server_lang)

    print(translation.text)