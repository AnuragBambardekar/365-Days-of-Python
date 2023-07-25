import pdb

def my_function():
    x = 10
    y = 5
    # pdb.set_trace()  # Set a breakpoint
    result = x + y
    print(result)

my_function()

"""
(Pdb) p x
10
(Pdb) p y
5
(Pdb) c
15
(Pdb) next
-> print(result)
(Pdb) step

(Pdb) until 8

(Pdb) q
To Quit

OR

python -m pdb .\pdb_inspect.py

(Pdb) jump 6

(Pdb) l
"""