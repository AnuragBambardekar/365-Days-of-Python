import ast

# Define a simple Python code
source_code = """
def square(x):
    return x ** 2

result = square(5)
print(result)
"""

# Parse the source code into an abstract syntax tree
tree = ast.parse(source_code)

# Now you can traverse and analyze the abstract syntax tree
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        print(f"Found a function named {node.name}")

    if isinstance(node, ast.Call):
        print(f"Found a function call to {node.func.id}")

# You can also use the astor module to pretty-print the AST
import astor
print(astor.to_source(tree))
