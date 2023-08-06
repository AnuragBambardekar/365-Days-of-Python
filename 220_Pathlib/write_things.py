# file needs to exist before we write something
import pathlib

path = pathlib.Path("./create_this.txt") # file

text = "Hello World!"
sound=b"this is dummy sound data (not really)"

# path.write_text(text)
# path.write_bytes(sound)

"""
if using image or sound data, then use bytes
"""

# Also works with 'with'
with path.open("w") as f:
    f.write(text)