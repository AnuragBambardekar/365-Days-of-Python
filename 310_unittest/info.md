# unittest

unittest is a built-in Python library for writing and running unit tests. Unit testing is a software testing technique in which individual components or functions of a program are tested in isolation to ensure that they work correctly. unittest provides a framework for organizing and running these tests, making it a valuable tool for ensuring the quality of your code.

In unittest, test cases are defined as classes that inherit from unittest.TestCase. Each test case is a separate class containing test methods. Test methods are named with the prefix "test_" and are used to test specific parts of your code.

unittest contains both a testing framework and a test runner. unittest has some important requirements for writing and executing tests.

unittest requires that:

You put your tests into classes as methods
You use a series of special assertion methods in the unittest.TestCase class instead of the built-in assert statement

```cmd
>>> assert sum([1, 2, 3]) == 6, "Should be 6"
```

```cmd
>>> assert sum([1, 1, 1]) == 6, "Should be 6"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: Should be 6
```

In your test methods, you should use various assert methods provided by the unittest.TestCase class to check if your code behaves as expected. Common assertion methods include:

assertEqual(a, b): Checks if a is equal to b. <br>
assertNotEqual(a, b): Checks if a is not equal to b. <br>
assertTrue(expr): Checks if expr is True. <br>
assertFalse(expr): Checks if expr is False. <br>
assertRaises(exception, callable, *args, **kwargs): Checks if calling callable(*args, **kwargs) raises the specified exception. <br>

Instead of providing the name of a module containing tests, you can request an auto-discovery using the following:
```cmd
$ python -m unittest discover
```

