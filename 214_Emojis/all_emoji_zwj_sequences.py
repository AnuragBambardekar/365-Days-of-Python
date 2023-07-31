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
    emoji_data_file = "./emoji-zwj-sequences.txt"
    emoji_code_points = extract_emojis(emoji_data_file)

    # print(emoji_code_points)
    
    # for emoji in emoji_code_points:
    #     print(emoji)

    split_list = [item.split() for item in emoji_code_points]
    # print(split_list)

    # for sublist in split_list:
        # print(sublist)
        # break

    for i,sublist in enumerate( split_list):
        # print(sublist)
        if ".." in sublist[0]:
            start_str, end_str = sublist[0].split("..")
            start_code_point = int(start_str, 16)
            end_code_point = int(end_str, 16)
            code_points = [code_point for code_point in range(start_code_point, end_code_point + 1)]
            print(["{:X}".format(code) for code in code_points],convert_to_emoji(["{:X}".format(code) for code in code_points]))
        else:
            print(sublist,convert_to_emoji(sublist))
        # if i == 10:
        #     break
        