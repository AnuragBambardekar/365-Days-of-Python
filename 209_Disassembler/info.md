## We can also use disassembler in IDLE

>>> 10/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> import dis
>>> dis.dis()
  1           0 LOAD_CONST               0 (10)
              2 LOAD_CONST               1 (0)
    -->       4 BINARY_TRUE_DIVIDE
              6 PRINT_EXPR
              8 LOAD_CONST               2 (None)
        