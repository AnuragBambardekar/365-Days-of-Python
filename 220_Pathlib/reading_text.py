import pathlib

path = pathlib.Path("./manipulating_paths.py") # file

bytes_content = path.read_bytes()
text = path.read_text()
print(text)
print(bytes_content)