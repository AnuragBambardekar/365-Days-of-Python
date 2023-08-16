"""
The glob module in Python is a built-in module that provides functions for working with file and directory patterns. 
It allows you to find all the pathnames matching a specified pattern according to the rules used by the Unix shell, although 
it's available on various platforms, not just Unix-like systems.

The main function provided by the glob module is the glob() function, which is used to search for files using wildcard patterns.
"""

import glob

print(glob.glob('apple.js'))
print(glob.glob('aple.js'))

# ? matches any single character
print(glob.glob('??ple.js'))
print(glob.glob('??????.js'))

# Asterisk
print(glob.glob('*.js'))
print(glob.glob('*.py'))
print(glob.glob('*.*'))

# [] matches any character in the sequence
print(glob.glob('[avd]*.js')) # first character should match a,v,d
print(glob.glob('[ab]*.js')) # first character should match a,b
print(glob.glob('[zf]*.js')) # first character should match z,f

# [!] matches any character not in the sequence
print(glob.glob('[!zf]*.js')) # first character should not match z,f