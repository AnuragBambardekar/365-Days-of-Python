Python is a dynamically typed programming language. This means that the data type of a variable is determined at runtime, not at the time of declaration. Unlike statically typed languages, where the data type of a variable is explicitly defined when it is declared, Python allows you to assign any type of value to a variable, and its type can change during the execution of the program.

Cython is a programming language [First appeared 28 July 2007 {15 Years Today (wow what a coincidence)}] that is a superset of Python. It allows you to write C-like code with Python-like syntax, making it easier to integrate with existing Python codebases. Cython code is designed to be compiled into C or C++ extensions, which can then be imported and used in Python programs like regular Python modules.

**The reason why Cython is fast can be attributed to the following factors:**

Static typing: Cython allows you to add type annotations to your variables and function arguments. By specifying data types, the compiler can generate more efficient C code, avoiding the overhead of dynamic type checking during runtime.

Direct C-level interaction: Cython can interface directly with C and C++ code, allowing you to call C functions and use C data types. This enables direct memory access and manipulation, bypassing some of the abstractions of the Python interpreter and leading to better performance.

To run file:

```cmd
cythonize -a -b .\cfactorial.pyx
```
```
Usage: cythonize [options] [sources and packages]+

Options:
  -h, --help            show this help message and exit
  -X NAME=VALUE,..., --directive=NAME=VALUE,...
                        set a compiler directive
  -E NAME=VALUE,..., --compile-time-env=NAME=VALUE,...
                        set a compile time environment variable
  -s NAME=VALUE, --option=NAME=VALUE
                        set a cythonize option
  -2                    use Python 2 syntax mode by default
  -3                    use Python 3 syntax mode by default
  --3str                use Python 3 syntax mode by default
  -a, --annotate        generate annotated HTML page for source files
  -x PATTERN, --exclude=PATTERN
                        exclude certain file patterns from the compilation
  -b, --build           build extension modules using distutils
  -i, --inplace         build extension modules in place using distutils
                        (implies -b)
  -j N, --parallel=N    run builds in N parallel jobs (default: 24)
  -f, --force           force recompilation
  -q, --quiet           be less verbose during compilation
  --lenient             increase Python compatibility by ignoring some compile
                        time errors
  -k, --keep-going      compile as much as possible, ignore compilation
                        failures
  -M, --depfile         produce depfiles for the sources
 ``` 

Open the generate annotated HTML page for source files and observe the code. The more brighter the yellow line, the more python interaction there is in your code.

```cmd
cythonize -a -b .\sort.pyx
```