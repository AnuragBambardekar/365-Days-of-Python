# way to create a database that can store arbitrary objects

import shelve

# with shelve.open('194_Shelve/TestDB') as db: # by default it is read/write mode
#     db['a'] = 1
#     db['b'] = 2
#     db['c'] = 3

# with pickling, you'd have to load the entire object
# with shelve, you dont need to do that


with shelve.open('194_Shelve/TestDB') as db: # by default it is read/write mode
    print(type(db))
    print(dict(db))
    print(db['c'])