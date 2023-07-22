# Sub Exceptions - Nested Exceptions

exc_group = ExceptionGroup("This is an exception Group",
                           [
                               ValueError("value must be greater than zero"),
                               ExceptionGroup(
                                   "directory errors: ", [
                                        NotADirectoryError("must be a directory"),
                                        NotADirectoryError("still must be a directory"),
                                   ]
                               )
                           ],
                           )
# try:
#     raise exc_group
# except* ValueError as e:
#     print("Handling ValueError")
# except* NotADirectoryError as e:
#     print("Handling NotADirectoryError") # takes all instances of NotADirectoryError
#     print(e.exceptions)

## Also, we cannot have except and except* part of the same try block

raise exc_group