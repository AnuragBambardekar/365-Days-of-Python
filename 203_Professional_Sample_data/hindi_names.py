from faker import Faker

#'hi_IN' changed the language
fake = Faker('hi_IN')	

for i in range(0, 10):
	print('Name->', fake.name(),
		'Country->', fake.country())
