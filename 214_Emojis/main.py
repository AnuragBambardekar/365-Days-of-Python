emoji1 = "\U0001F604"  # Unicode for 😄
print(emoji1)

emoji2 = "\U0001F40D"  # Unicode for 🐍
print(emoji2)

emoji3 = "\U0001F680"  # Unicode for 🚀
print(emoji3)

start_code_point = 0x23E9
end_code_point = 0x23EC

for code_point in range(start_code_point, end_code_point + 1):
    emoji = chr(code_point)
    print(emoji, end=" ") # ⏩ ⏪ ⏫ ⏬

emoji = chr(0x26A1)
print(emoji) #⚡

print("\U0001F441") # 👁

emoji_code_points = ["1F441", "FE0F", "200D", "1F5E8", "FE0F"]# 👁️‍🗨️
emoji_str = "".join([chr(int(code_point, 16)) for code_point in emoji_code_points])
print(emoji_str)

emoji_code_points = ["1F90C", "1F3FB"] # 🤌🏻
emoji_str = "".join([chr(int(code_point, 16)) for code_point in emoji_code_points])
print(emoji_str)

emoji_code_points = ["23E9", "23EA", "23EB", "23EC"] # ⏩ ⏪ ⏫ ⏬
emoji_str = "".join([chr(int(code_point, 16)) for code_point in emoji_code_points])
print(emoji_str)

emoji_code_points = ["1F468","200D","2764","FE0F","200D","1F468"] # 👨‍❤️‍👨
emoji_str = "".join([chr(int(code_point, 16)) for code_point in emoji_code_points])
print(emoji_str)
