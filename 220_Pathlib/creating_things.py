import pathlib

# path = pathlib.Path("./create_this.txt") # file
# path.touch()

path = pathlib.Path("./create_this_dir") # file
path.mkdir(exist_ok=True)