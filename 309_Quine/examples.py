# # Example A. chr(39) == "'".
# a = 'a = {}{}{}; print(a.format(chr(39), a, chr(39)))'; print(a.format(chr(39), a, chr(39)))
"""
In this quine, the variable a contains a string that represents the source code of the program.
The source code is within single quotes, which are represented by chr(39). chr(39) returns the character '.
The a.format(chr(39), a, chr(39)) part replaces the three sets of {} placeholders with the single quote ', the content of a, and another single quote '. 
So it effectively prints the source code enclosed in single quotes.
"""

# # Example B. chr(39) == "'".
# b = 'b = %s%s%s; print(b %% (chr(39), b, chr(39)))'; print(b % (chr(39), b, chr(39)))

# # Example C. %r will quote automatically.
# c = 'c = %r; print(c %% c)'; print(c % c)

# exec(s:='print("exec(s:=%r)"%s)')