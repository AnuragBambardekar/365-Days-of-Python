def find_val(val, iterable):
    """
    return:
    True if val is in iterable
    False otherwise
    """
    for item in iterable:
        if val == item:
            return True
    return False

