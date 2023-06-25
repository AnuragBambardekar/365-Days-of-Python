import contextlib

# help(pow)

# capture what is printed in the stdout
# res = help(pow) # Return type is NoneType

with open("power_help_page.txt","w") as f:
    with contextlib.redirect_stdout(f):
        help(pow)