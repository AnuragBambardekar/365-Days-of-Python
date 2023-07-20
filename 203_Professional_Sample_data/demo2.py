from faker import Faker

f = Faker(["fr_FR", "de_DE"])

# unique values
for _ in range(10):
    print(f.unique.random_int(min=1, max=10))

# fill the digits
for _ in range(5):
    print(f.bothify(text="????-########", letters="ABCDEFG"))

# hexify to generate MAC addresses
for _ in range(5):
    print(f.hexify(text="MAC: ^^:^^:^^:^^:^^:^^", upper=True))