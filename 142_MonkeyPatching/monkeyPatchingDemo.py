"""
Monkey patching in Python refers to the ability to modify or extend the behavior of existing classes or modules at runtime. 
It allows you to add, modify, or replace methods, attributes, or functions in a class or module without changing its original source code.
"""

# Define a simple class
class MyClass:
    def my_method(self):
        return "Original method"

# Create an instance of MyClass
obj = MyClass()

# Define a new method to be patched into MyClass
def patched_method(self):
    return "Patched method"

# Monkey patching: Replace the original method with the patched method
MyClass.my_method = patched_method

# Now, when we call my_method on the instance, it will invoke the patched method
print(obj.my_method())  # Output: Patched method

"""
After creating an instance of MyClass, we define a new function patched_method that we want to patch into the class. 
Then, we replace the original my_method of MyClass with the patched method using monkey patching. 
Finally, when we call obj.my_method(), it invokes the patched method instead of the original one.
"""