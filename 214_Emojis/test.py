def split_and_reference(input_list):
    split_list = [item.split() for item in input_list]
    return split_list

if __name__ == "__main__":
    input_list = [
        '1F1FD 1F1F0',
        '1F1FE 1F1EA',
        '1F1FE 1F1F9',
        '1F1FF 1F1E6',
        '1F1FF 1F1F2',
        '1F1FF 1F1FC',
        '1F3F4 E0067 E0062 E0065 E006E E0067 E007F',
        '1F3F4 E0067 E0062 E0073 E0063 E0074 E007F',
        '1F3F4 E0067 E0062 E0077 E006C E0073 E007F'
    ]

    split_list = split_and_reference(input_list)
    print(split_list)
