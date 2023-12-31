# About Manifest files

In Python, the MANIFEST.in file is used to specify additional files or directories to be included when creating a source distribution (sdist) package. This file is often used in conjunction with the setup.py script to define the content that should be included in the distribution package.

## File Content Specification:

- You can specify files and directories to include or exclude from the distribution.
- You can use wildcards and regular expressions to match files.

## Common Directives:

- include: Specifies files or file patterns to be included in the distribution.
- exclude: Specifies files or file patterns to be excluded from the distribution.
- recursive-include: Includes files matching a pattern recursively from a directory.

## Example:

```py
include *.txt
recursive-include docs *.html
exclude *.log
```

In this example:

- All text files in the root directory will be included.
- HTML files from the 'docs' directory and its subdirectories will be included.
- Log files will be excluded.

## Using setuptools.find_packages():

If you're using find_packages() in your setup.py, it automatically includes all packages found in your project directory. You might not need to specify them explicitly in MANIFEST.in.

**Remember that the MANIFEST.in file is primarily used for source distributions. If you're working with binary distributions (wheels), they may have a different mechanism for including files.**

