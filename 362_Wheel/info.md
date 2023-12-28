# About Wheel (.whl) files

Wheels are a binary distribution format that aims to be a more efficient and faster alternative to the traditional Source Distribution (sdist) format. The wheel format is specified in PEP 427.

A Wheel package contains compiled code (usually in C or Cython) and metadata that describes the package, making it easier to install compared to source distributions. This format is particularly useful for distributing pre-built, platform-specific binary packages, which can save time during the installation process by avoiding the need to compile code on the target machine.

Naming convention:
```cmd
<distribution-name>-<version>-<python tag>-<abi tag>-<platform tag>.whl
```

- Wheels benefit both users and maintainers of Python packages alike in a handful of ways:
    - Wheels install faster than source distributions for both pure-Python packages and extension modules
    - Wheels are smaller than source distributions.
    - Wheels cut setup.py execution out of the equation.
    - There's no need for a compiler
    - pip automatically generates .pyc files
    - Wheels provide consistency by cutting many of the variables involved in installing a package out of the equation.

## Why make wheels?
- If you plan to distribute a Python packages to the community, then you should care immensely about distributing wheels for your project because they make the installation process cleaner and less complex for end users.

## Different Types of Wheels
- A Universal wheel contains py2.py3-none-any.whl. It supports both Python 2 and Python 3 on any OS and platform. The majority of wheels listed on the Python Wheels website are universal wheels.
- A pure-Python wheel contains either py3-none-any.whl or py2-none-any.whl. It supports either Python 3 or Python 2, but not both. It's otherwise the same as a universal wheel, but it'll be labeled with either py2 or py3 rather than the py2.py3 label.
- A platform wheel supports a specific Python version and platform. It contains segments indicating a specific Python version, ABI (Application Binary Interface), OS, or architecture.

## Creating a Wheel
You can build a pure-Python wheel or a universal wheel for any project using setuptools with just a single command:
```
python setup.py sdist bdist_wheel
```

This will create both a source distribution (sdist) and a wheel (bdist_wheel). By default, both will be placed in dist/ under the current directory.

