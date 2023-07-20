#pip install faker

from faker import Faker

f = Faker(['it_IT', 'en_US', 'ja_JP'])
print(f.name())
print(f.address())
print(f.country())
print(f.latitude(), f.longitude())
print(f.ipv4_private())
print(f.ipv4_public())
print(f.sentence())
print(f.zipcode())
print(f.locale())
print(f.license_plate())
print(f.phone_number())