from random import randint
class SetConfuser:
    def __hash__(self):
        return randint(0,1)
    
    def __eq__(self, other):
        return True
    
c = SetConfuser()
S = {c}

# print(S)
# print(c)

print(c in S)
print(c in S)
print(c in S)

print(len({c, c, c}))
print( {c: 1, c: 2} )

#====CONFUSION===#

"""
True
True
False
2
{<__main__.SetConfuser object at 0x00000234E844EE90>: 1, <__main__.SetConfuser object at 0x00000234E844EE90>: 2}

"""

"""
False
False
False
2
{<__main__.SetConfuser object at 0x00000176C952EED0>: 2}
"""

"""
True
False
True
1
{<__main__.SetConfuser object at 0x000002012533EE90>: 1, <__main__.SetConfuser object at 0x000002012533EE90>: 2}
"""

"""
These lines check whether the instance c is in the set S. 
Due to the overridden __eq__ method that always returns True, 
the instance c will always be considered to be in the set. 
However, because of the random hash function, the in operator 
might still produce unpredictable results, causing some True and 
some False outputs.
"""

