import MathUtils

# Define the corrected version of divide function
def patched_divide(a, b):
    return a / b

# Monkey patching: Replace the original divide function with the patched_divide function
MathUtils.divide = patched_divide

# Test the patched function
result = MathUtils.divide(10, 5)
print(result)  # Output: 2.0
