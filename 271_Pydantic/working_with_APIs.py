# from pydantic import BaseModel, validator

# def to_camel_case(text):
#     camel_string = "".join(x.capitalize() for x in text.lower().split("_"))
#     return text[0].lower() + camel_string[1:]

# class Profile(BaseModel):
#     name: str
#     age: int
#     my_jobs: list[str] = []

#     class Config:
#         validate_assignment = True
#         alias_generator = to_camel_case

#     @validator("age")
#     def age_gt_0(cls, value: int) -> int:
#         if value < 0:
#             raise ValueError("age must be greater than zero")
#         return value

# resp = {"name":"Bob",
#         "age":"24",
#         "my_jobs":("gamer",)}

# p = Profile(**resp) # to pass all key:value pairs of dict
# print(p)

# p.age = -1 # doesnt run validation on assignment, but you can change this by configuring the Config class
# print(p.age)


import requests
from pydantic import BaseModel

# Define a Pydantic model for the user data
class User(BaseModel):
    gender: str
    name: dict
    location: dict
    email: str
    login: dict
    dob: dict
    registered: dict
    phone: str
    cell: str
    id: dict
    picture: dict
    nat: str

# Make an API request
api_url = "https://randomuser.me/api/"
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the API response into a dictionary
    user_data = response.json()

    # Extract the user information from the "results" list
    user_info = user_data["results"][0]

    # Create a User object using the Pydantic model
    user = User(**user_info)
    
    # Now you can work with the user data
    print(f"Gender: {user.gender}")
    print(f"Name: {user.name['title']} {user.name['first']} {user.name['last']}")
    print(f"Email: {user.email}")
    print(f"Username: {user.login['username']}")
    print(f"Date of Birth: {user.dob['date']}")
    print(f"Phone: {user.phone}")
    print(f"Cell: {user.cell}")
    print(f"Nationality: {user.nat}")
else:
    print(f"API request failed with status code {response.status_code}")
