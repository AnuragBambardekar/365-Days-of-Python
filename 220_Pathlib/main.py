import pathlib

path = pathlib.Path()
print(path) # Prints --> .

path = pathlib.Path.cwd()
print(path) # Prints full path of current working directory

path = pathlib.Path("etc/passwd")
print(path.is_absolute())
print()

path = pathlib.Path("./main.py")
# print(path)
print(path.name)
print(path.stem)
print(path.suffix)

print()

print(path.parts)
print(path.resolve()) # full path
print(path.resolve().parts)
print(path.absolute().as_uri()) # as_uri needs to be done on a full path

