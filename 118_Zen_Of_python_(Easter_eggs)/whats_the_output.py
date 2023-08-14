name = "Bamba"

if name=='Bob' or 'John' or 'Mike':
    print("Access Granted!")
else:
    print("Access Denied!")

"""
F | T = T
"""

# Fix:
if name in ['Bob','John','Mike']:
    print("Access Granted!")
else:
    print("Access Denied!")