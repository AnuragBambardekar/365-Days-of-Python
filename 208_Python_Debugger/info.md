```python
python -m pdb .\inspect_this.py
```
```python
(Pdb) break 4
Breakpoint 1 at c:\users\anura\documents\vscode_workspace\365-days-of-python\208_python_debugger\inspect_this.py:4
(Pdb) p value
10
(Pdb) p values
[10, 5, 9, 3, 55, 63, 1, 0, 88, 99, 42]
(Pdb) c
1.0
Divisible by 5
Hello World
> c:\users\anura\documents\vscode_workspace\365-days-of-python\208_python_debugger\inspect_this.py(4)<module>()
-> print(10/value)
(Pdb) p value
5
```
```python
-> values = [10,5,9,3,55,63,1,0,88,99,42]
(Pdb) until 6
1.0
> c:\users\anura\documents\vscode_workspace\365-days-of-python\208_python_debugger\inspect_this.py(6)<module>()
-> if value%5 == 0:
(Pdb) 
```

**tbreak is a temporary break and only is valid once**

```python
-> values = [10,5,9,3,55,63,1,0,88,99,42]
(Pdb) l
  1  -> values = [10,5,9,3,55,63,1,0,88,99,42]
  2
  3     for value in values:
  4         # breakpoint() # can use with step
  5         print(10/value)
  6         if value%5 == 0:
  7             print('Divisible by 5')
  8         print("Hello World")
[EOF]
```

