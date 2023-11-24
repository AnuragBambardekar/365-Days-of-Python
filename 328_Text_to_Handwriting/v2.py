from PIL import Image
import os
import sys

def open_text_file(file_path):
    try:
        txt = open(file_path, "r")
    except FileNotFoundError:
        print("Could not find file, using default file...")
        txt = open("dummy.txt", "r")
    return txt

def create_output_directory(directory):
    os.makedirs(directory, exist_ok=True)

def create_initial_background():
    return Image.open("op/bg.png").copy()

def paste_word_on_page(word, bg, gap, ht, space_image):
    for i in word:
        cases = Image.open("op/{}.png".format(str(ord(i))))
        bg.paste(cases, (gap, ht))
        size = cases.width
        gap += size

    bg.paste(space_image, (gap, ht))
    gap += space_image.width
    return gap

def save_page(bg, output_dir, page_number):
    bg.save(os.path.join(output_dir, f"page_{page_number}.png"))

def main():
    # path of text file
    try:
        file_path = sys.argv[1]
    except IndexError:
        print("No file entered, using default file...")
        file_path = "dummy.txt"

    txt = open_text_file(file_path)

    # Output directory for pages
    output_dir = "output_pages"
    create_output_directory(output_dir)

    space_image = Image.open("op/space.png")

    gap, ht = 0, 0
    page_number = 0
    bg = create_initial_background()
    sheet_width, sheet_height = bg.width, bg.height

    for word in txt.read().replace("\n", "").split():
        word_width = sum(Image.open("op/{}.png".format(ord(c))).width for c in word)

        if sheet_width < gap + word_width or len(word) > (sheet_width - gap):
            gap, ht = 0, ht + 110  # Start a new line

        if ht + 110 > sheet_height:
            gap, ht = 0, 0
            page_number += 1
            save_page(bg, output_dir, page_number)
            bg = create_initial_background()

        gap = paste_word_on_page(word, bg, gap, ht, space_image)
    page_number+=1
    save_page(bg, output_dir, page_number)

if __name__ == "__main__":
    main()
