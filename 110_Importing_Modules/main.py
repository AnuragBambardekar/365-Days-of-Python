from functionality import *

print(add(10,20))
print(sub(10,20))
print(mul(10,20))

# from otherModules import second
# from otherModules.second import *
# second.myfunction()

from otherModules import * # create __init__ in folder
second.myfunction()
third.another_function()

from otherModules.subModule import fourth
fourth.last_func()

from otherModules.subModule.fourth import last_func
last_func()