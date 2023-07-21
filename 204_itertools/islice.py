import itertools as it

# with open("204_itertools/lyrics.txt") as f:
#     lines = f.readlines()

# for i in lines[6:11]:
#     print(i.strip())

# instead, we can do this:-
with open("204_itertools/lyrics.txt") as f:
    for line in it.islice(f, 6, 11):
        print(line.strip())