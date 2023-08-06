import pathlib

path = pathlib.Path(".") # file

for p in path.glob("*.py"):
    print(p)