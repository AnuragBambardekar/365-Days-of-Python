"""String Manipulation Functions

This module provides functions for performing various string manipulation tasks.

Examples:
    >>> from string_manipulation import manipulator
    >>> manipulator.capitalize_first('hello, world')
    'Hello, world'
    >>> manipulator.reverse_string('python')
    'nohtyp'
    >>> from string_manipulation.manipulator import extract_numbers
    >>> extract_numbers('abc123xyz456')
    [123, 456]

The module contains the following functions:

- `capitalize_first(text: str) -> str`: Capitalizes the first letter of a string.
- `reverse_string(text: str) -> str`: Reverses the characters in a string.
- `extract_numbers(text: str) -> List[int]`: Extracts all the numbers from a string.

"""

from typing import List

def capitalize_first(text: str) -> str:
    """Capitalize the first letter of a string.

    Examples:
        >>> capitalize_first('hello, world')
        'Hello, world'
        >>> capitalize_first('apple')
        'Apple'

    Args:
        text (str): The input string to be processed.

    Returns:
        str: A new string with the first letter capitalized.
    """
    return text[0].upper() + text[1:]

def reverse_string(text: str) -> str:
    """Reverse the characters in a string.

    Examples:
        >>> reverse_string('python')
        'nohtyp'
        >>> reverse_string('12345')
        '54321'

    Args:
        text (str): The input string to be reversed.

    Returns:
        str: A new string with the characters reversed.
    """
    return text[::-1]

def extract_numbers(text: str) -> List[int]:
    """Extract all the numbers from a string.

    Examples:
        >>> extract_numbers('abc123xyz456')
        [123, 456]
        >>> extract_numbers('no numbers here')
        []

    Args:
        text (str): The input string containing numbers.

    Returns:
        List[int]: A list of integers extracted from the input string.
    """
    numbers = [int(word) for word in text.split() if word.isdigit()]
    return numbers
