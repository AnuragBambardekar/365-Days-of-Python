from typing import Any, TypedDict, NotRequired

class ProfileT(TypedDict):
    name: str
    age: int
    jobs: NotRequired[list[str]] # Python 3.11 feature

profile: ProfileT = {
    "name":"Bamba",
    "age": 24,
    "jobs": ["Software Engineer"],
}

# profile["gender"] --> Error