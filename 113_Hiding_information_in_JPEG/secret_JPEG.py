# Read Hello World from the JPEG file
with open('113_Hiding_information_in_JPEG\eggs.jpg','rb') as f:
    content = f.read()

    # Look for FF D9
    offset = content.index(bytes.fromhex('FFD9'))
    # print(offset)

    f.seek(offset + 2) # 2 because 2 bytes further from index of FFD9
    print(f.read())