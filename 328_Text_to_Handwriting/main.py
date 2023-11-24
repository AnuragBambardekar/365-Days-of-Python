from PIL import Image
from sys import argv

# path of text file
fileName = "dummy.txt"

try:
    txt = open(argv[1],"r")
except IndexError:
    print("No File Entered, using default file...")
    txt = open(fileName,"r")
except FileNotFoundError:
    print("Could not find file, Using default file...")
    txt = open(fileName,"r")

# Blank page
bg = Image.open("op/bg.png")
sheet_width = bg.width
gap, ht = 0,0

# Read unicode value of each text and replace with corresponding handwritten letter from folder
# for i in txt.read().replace("\n",""):
#     cases = Image.open("op/{}.png".format(str(ord(i))))
#     bg.paste(cases,(gap,ht))
#     size = cases.width
#     height = cases.height
#     # print("Runnning....")
#     gap+=size

#     if sheet_width < gap or len(i) > (sheet_width-gap):
#         gap,ht = 0, ht+110

# Use space.png as the space between words
space_image = Image.open("op/space.png")

for word in txt.read().replace("\n", "").split():
    word_width = sum(Image.open("op/{}.png".format(ord(c))).width for c in word)

    # Check if the word exceeds the remaining space on the line
    if sheet_width < gap + word_width or len(word) > (sheet_width - gap):
        gap, ht = 0, ht + 110  # Start a new line

    # Paste each character of the word
    for i in word:
        cases = Image.open("op/{}.png".format(str(ord(i))))
        bg.paste(cases, (gap, ht))
        size = cases.width
        gap += size
    
    bg.paste(space_image, (gap, ht))
    gap += space_image.width


    # gap += space_image.width

# print(gap)
# print(sheet_width)
bg.show()