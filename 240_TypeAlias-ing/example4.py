from typing import Tuple
from typing import TypeAlias

TokenPosition: TypeAlias = Tuple[int, int, int, int, str]
# Sometimes, the static type checker fails to recognize a type alias
# so Python 3.10 came up with updates to add explicit TypeAlias
# So, now the type checker doesn't have to guess whether the assignment 
# above is an alias or not.

# CAlias = 'C' # earlier the TypeChecker did not know that this is an 
# alias/forward annotation
# it considers this as a string assignment.

CAlias: TypeAlias = "C" # explicit TypeAlias
# now, the typechecker unambiguosuly knows that this is indeed a 
# forward annotation

def f(x: TokenPosition) -> str:
    pass

class C:
    pass