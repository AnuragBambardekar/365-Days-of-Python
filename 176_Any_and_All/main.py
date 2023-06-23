# Pattern Matching Task

lst = ["hello","powepw","hello world","xxx world","sfaffa"]
patterns = ["hello","world"]

"""
matches = []
# This approach is non-pythonic and inefficient
for item in lst:
    for pattern in patterns:
        if pattern in item and item not in matches: # remove duplicates
            matches.append(item)

print(matches)

"""


# any function
matches = [item for item in lst if any(pattern in item for pattern in patterns)]
print(matches)

# all function
matches = [item for item in lst if all(pattern in item for pattern in patterns)]
print(matches)