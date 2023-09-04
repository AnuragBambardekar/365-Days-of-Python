"""
# Long Method
x = [1,2,1,3,4,1,2,4,1]

freq_dict = {}

for item in x:
    if item in freq_dict:
        freq_dict[item] += 1
    else:
        freq_dict[item] = 1

most_frequent = max(freq_dict, key=freq_dict.get)
print(most_frequent)
"""

x = [1,2,1,3,4,1,2,4,1]

# most = max(x, key=x.count)
# print(most)

# more optimized
most = max(set(x), key=x.count)
print(most)