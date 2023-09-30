matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

# find 11 and break
for r in matrix:
    for elem in r:
        if elem == 11:
            print("Found 11. Breaking!")
            break
    else:
        continue
    break