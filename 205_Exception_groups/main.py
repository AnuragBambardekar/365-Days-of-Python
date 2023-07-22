# Exception Groups are available only from Python 3.11

exc_group = ExceptionGroup("This is an exception Group",
                           [
                               ValueError("value must be greater than zero"),
                               NotADirectoryError("must be a directory"),
                               TypeError("Must be an int"),
                               NotADirectoryError("still must be a directory"),
                           ],
                           )
try:
    raise exc_group
except* ValueError as e:
    print("Handling ValueError")
except* NotADirectoryError as e:
    print("Handling NotADirectoryError") # takes all instances of NotADirectoryError
    print(e.exceptions)

# raise exc_group