# name-main idiom
Python’s name-main idiom isn’t special. It’s just a conditional check. It may look cryptic at first, especially when you’re starting to work with Python and you’re used to Python’s slim and elegant syntax. After all, the name-main idiom includes a dunder variable from the global namespace, and a string that’s a dunder value as well.

So it’s not the type of entry point that main represents in other languages.

```test.py```
```py
def hello(name):
    return f"Hello {name}"

string = hello("Bamba")
print(string)
```

```program.py```
```py
import test
```

When I run either of these programs, I get the output:
```cmd
Hello Bamba
```

Let's modify ```program.py```:
```py
import test

print(test.hello("Bob"))
```

And, I just want:
```cmd
Hello Bob
```
to be printed.

So, let's modify ```test.py```:
```py
def hello(name):
    return f"Hello {name}"

if __name__ == "__main__":
    string = hello("Bamba")
    print(string)
```
Now, I get the desired output:
```cmd
Hello Bob
```

# Why you should use it?
`__name__` is a dunder method - predefined by Python.

- It helps maintain a clear separation between your script's code that should be executed when it's run as a standalone program and code that might be used as a module in other programs.

Nesting code under if `__name__` == "`__main__`" allows you to cater to different use cases:

**Script**: When run as a script, your code prompts the user for input or executes the code in the block, calls hello(), and prints the result. <br>
**Module**: When you import test as a module, then hello() gets defined, but no code executes. You provide hello() to the main code session without any side effects. <br>

At its core, the idiom is a conditional statement that checks whether the value of the variable `__name__` is equal to the string "`__main__`":

If the `__name__` == "`__main__`" expression is True, then the indented code following the conditional statement executes. <br>
If the `__name__` == "`__main__`" expression is False, then Python skips the indented code.