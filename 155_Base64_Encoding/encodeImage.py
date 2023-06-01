import base64

with open("155_Base64_Encoding\image.png","rb") as f:
    data = f.read()

# with open("155_Base64_Encoding\image2.png","wb") as f:
#     f.write(data)

# print(data)
# print(base64.b64encode(data))

encoded_data = base64.b64encode(data)

with open("encoded_data.txt", "w") as f:
    f.write(encoded_data.decode("utf-8"))

print("Encoded data written to encoded_data.txt")


