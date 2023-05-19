# importing the module
from types import FunctionType
  
# function at run-time
f_code = compile('def add(a, b): return(a + b) ', "<int>", "exec")
f_func = FunctionType(f_code.co_consts[0], globals(), "add")
  
val1 = 3999
val2 =4999
  
# calliong the function
print(f_func(val1, val2))