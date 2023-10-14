# Document and Test your code at once

Python’s `doctest` module provides a testing framework that doesn’t have too steep a learning curve. It’ll allow you to use code examples for two purposes: documenting and testing your code.

- All exprienced programmers will tell you that documenting your code is a best practice.
- Some will say that code and its documentation are equally important and necessary.
- Others will tell you that documentation is even more important than the code itself.

In small projects using **explicit names**, **comments** and **docstrings** might be sufficient.

- Comments have a couple of drawbacks:
    - they're ignored by the interpreter or compiler, which makes them unreachable at runtime.
    - they often get outdated when the code evolves and the comments remain untouched.

- Documentation strings, or simply docstrings, are a neat Python feature that can help you document your code as you go. The advantage of docstrings compared to comments is that the interpreter doesn’t ignore them. They’re a living part of your code.

- Because docstrings are active parts of your code, you can access them at runtime. To do this, you can use the `.__doc__` special attributes on your packages, modules, classes, methods, and functions.

## About doctest

The doctest module is a lightweight testing framework that provides quick and straightforward test automation. It can read the test cases from your project’s documentation and your code’s docstrings. This framework is shipped with the Python interpreter and adheres to the batteries-included philosophy.

The doctest framework is well suited for the quick automation of acceptance tests at the integration and system testing levels. Acceptance tests are those tests that you run to determine if the specifications of a given project are met, while integration tests are intended to guarantee that different components of a project work correctly as a group.

- Writing quick and effective test cases to check your code as you write it
- Running acceptance, regression, and integration test cases on your projects, packages, and modules
- Checking if your docstrings are up-to-date and in sync with the target code
- Verifying if your projects’ documentation is up-to-date
- Writing hands-on tutorials for your projects, packages, and modules
- Illustrating how to use your projects’ APIs and what the expected input and output must be

## Running test cases with doctest
```cmd
python -m doctest calculations.py
```

This command won’t issue any output to your screen. Displaying no output means that doctest ran all your test cases and didn’t find any failing tests.

If you want doctest to be verbose about the process of running your test, then use the -v switch

```cmd
python -m doctest -v calculations.py
```

Output:
```cmd
Trying:
    add(4.0, 2.0)
Expecting:
    6.0
ok
Trying:
    add(4,2)
Expecting:
    6.0
ok
1 items had no tests:
    calculations
1 items passed all tests:
   2 tests in calculations.add
2 tests in 2 items.
2 passed and 0 failed.
Test passed.
```

Running doctest with the -v option produces detailed output that describes the test-running process. The first two highlighted lines show the actual tests and their corresponding expected output. The line immediately after the expected output of each test displays the word ok, meaning that the target test passed successfully. In this example, the two tests passed, as you can confirm in the last highlighted line.

