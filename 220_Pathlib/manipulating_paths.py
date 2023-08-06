import pathlib

path = pathlib.Path("./manipulating_paths.py") # file
# path = pathlib.Path(".") # directory
# path = pathlib.Path("./nonExistingFile.py") # non-existing file
print(path.exists())
print(path.is_file())
print(path.is_dir())
# Run it as: 
# python .\manipulating_paths.py
# True
