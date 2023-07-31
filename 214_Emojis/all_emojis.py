def extract_emojis(file_path):
    emojis = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if not line.startswith("#"):
                parts = line.strip().split(";", 1)
                if len(parts) >= 2:
                    emoji_code = parts[0].strip()
                    emojis.append(emoji_code)
    return emojis

def convert_to_emoji(emoji_code_points):
    emoji_str = "".join([chr(int(code_point, 16)) for code_point in emoji_code_points])
    return emoji_str

if __name__ == "__main__":
    emoji_data_file = "./emoji-test.txt"
    emoji_code_points = extract_emojis(emoji_data_file)

    # print(emoji_code_points)
    
    # for emoji in emoji_code_points:
    #     print(emoji)

    split_list = [item.split() for item in emoji_code_points]
    # print(split_list)

    # for sublist in split_list:
    #     print(sublist)

    for sublist in split_list:
        print(convert_to_emoji(sublist))
