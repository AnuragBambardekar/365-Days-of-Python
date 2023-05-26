# profile_example.py

from line_profiler import LineProfiler

# Define a class with a method to be profiled
class MyClass:
    def process_data(self, data):
        # Perform some data processing
        result = data.upper()
        return result

# Create an instance of LineProfiler
profiler = LineProfiler()

# Add the method to be profiled
profiler.add_function(MyClass.process_data)

# Create an instance of MyClass
my_object = MyClass()

# Run the profiler
profiler.enable_by_count()

# Call the method
result = my_object.process_data("hello world")

# Disable the profiler and print the results
profiler.disable_by_count()
profiler.print_stats()
