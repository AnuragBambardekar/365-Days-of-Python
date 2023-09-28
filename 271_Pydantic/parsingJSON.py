from typing import List, Optional
from pydantic import BaseModel, validator
import json

class Variant(BaseModel):
    name: str
    sku: str
    available: bool
    price: float

    @validator('sku')
    def sku_length(cls, value):
        if len(value) != 7:
            raise ValueError('SKU must be 7 characters.')
        return value

class Product(BaseModel):
    id: int
    title: str
    variants: Optional[List[Variant]]

# item = Product(
#     id = 123123,
#     title = "Cool Shirt",
#     variants = [
#         Variant(
#             name="Small",
#             sku="ABC1234",
#             available=True,
#             price=24.99
#         ),
#         Variant(
#             name="Medium",
#             sku="ABC1235",
#             available="False", # changes string to boolean
#             price=25 # changes int to float
#         ),
#         Variant(
#             name="Small",
#             sku="ABC1236",
#             available=True,
#             price=25
#         ),
#     ]
# )

# print(item.variants[0].name)
# print(item)



# using data.json
with open("271_Pydantic/data.json") as f:
    data = json.load(f)
    items = [Product(**item) for item in data['results']]

print(items)
print(items[0].variants[0].name)