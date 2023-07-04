import random

def get_product_code():
    products = [
        "COM_1234",
        "COM_1724",
        "PHN_1004",
        "PHN_1304",
    ]

    return random.choice(products)

# print(get_product_code())

product_code = get_product_code()
print(product_code)

type_product = product_code[:3]
print(type_product)

type_product = product_code[:3]
print(type_product)


type_product = product_code[0:3:1] # step size = 1
print(type_product)
type_product = product_code[0:3:2] # step size = 2
print(type_product)
type_product = product_code[0:3:-1] # step size = -1
print(type_product)
type_product = product_code[3:0:-1] # step size = -1
print(type_product)


print()
product_code = get_product_code()
print(product_code)

type_product = product_code[:3]
# print(type_product)

type_product_slice = slice(3)
print(product_code[type_product_slice])

type_product_slice = slice(1,3,1)
print(product_code[type_product_slice])

type_product_slice = slice(-1,-3,-1)
print(product_code[type_product_slice])