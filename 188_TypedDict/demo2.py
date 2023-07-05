from typing import TypedDict, Optional # (NotRequired in Python 3.11)
from typing_extensions import Required

Vote = TypedDict('Vote', {'for':int, 'against':int}, total=True)
Vote2 = TypedDict('Vote2', {'for':int, 'against':Required[int]}, total=False)

vote: Vote = {'for':100, 'against':90}
vote: Vote2 = {'adadad':100} # doesnt work in versions < Python 3.11, it should not allow me to add whatever field and 'against' is a required field


print(vote)