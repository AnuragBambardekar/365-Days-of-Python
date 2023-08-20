def hello(name):
    return f"Hello {name}"

def main(arg): # not the same as main() in other programming languages
    return f"I'm main: {arg}"
# print(__name__) # test

if __name__ == "__main__":
    # print(__name__) # __main__
    string = hello("Bamba")
    print(string)

    arg = main(10)
    print(arg)


"""
when you run this script as a standalone program, you'll get the message 
"Hello Bamba". 

However, if you import test into another script, the hello() won't execute 
unless explicitly called.
"""