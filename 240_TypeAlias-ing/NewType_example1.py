from typing import NewType

userId = int
# print(userId(10))

def findUser(user_id: userId):
    print('Found: ', user_id)

findUser(userId(10))
findUser(100) # also works, which makes our Type: 'userId' useless

# So, we can use a NewType which creates a subtype.
newUserId = NewType('newUserId',int)
# print(newUserId(10))

def findNewUser(newUser_id: newUserId):
    print('Found: ', newUser_id)

findNewUser(10) # should get some syntax highlighting in editor, but still executes

