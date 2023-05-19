# importing the module
from types import FunctionType

# functttion during run-time
f_code = compile('def bamba(): return "BAMBA"', "<string>", "exec")
f_func = FunctionType(f_code.co_consts[0], globals(), "bamba")

# calling the function
print(f_func())
