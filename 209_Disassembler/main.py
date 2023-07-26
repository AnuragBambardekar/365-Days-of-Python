import dis

def example_function(x, y):
    result = (x + y) * 2
    return result

# Get the code object of the function
code_obj = example_function.__code__

# Disassemble the bytecode
dis.dis(code_obj)

"""
Disassembler is a tool that allows you to inspect the bytecode generated by the Python interpreter for a given Python code. 
Bytecode is the low-level representation of Python code that the interpreter uses to execute the program. 
The disassembler module in Python provides functions to disassemble Python bytecode into a more human-readable form, helping 
you understand how Python code is translated into bytecode instructions.
"""

"""
  3           0 RESUME                   0

  4           2 LOAD_FAST                0 (x)
              4 LOAD_FAST                1 (y)
              6 BINARY_OP                0 (+)
             10 LOAD_CONST               1 (2)
             12 BINARY_OP                5 (*)
             16 STORE_FAST               2 (result)

  5          18 LOAD_FAST                2 (result)
             20 RETURN_VALUE
             
LOAD_FAST, BINARY_ADD, LOAD_CONST, BINARY_MULTIPLY, and STORE_FAST are different opcodes that perform various operations like 
loading values, performing arithmetic operations, and storing values in the local namespace.
"""