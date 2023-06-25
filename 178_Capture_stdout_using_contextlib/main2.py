import contextlib
import sys

with contextlib.redirect_stdout(sys.stderr):
    help(pow)

# Terminal might print out stdout and stderr the same way