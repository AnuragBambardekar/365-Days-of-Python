from typing import TypeAlias

my_type = tuple[int,str]
var: my_type = (10,'hello')
# var: my_type = (10,10) # still no type safety
print(var)