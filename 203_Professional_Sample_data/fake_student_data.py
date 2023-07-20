# References: https://www.geeksforgeeks.org/python-faker-library/

from faker import Faker

# To create a json file
import json		

# For student id
from random import randint	

fake = Faker()

def input_data(x):

	# dictionary
	student_data ={}
	for i in range(0, x):
		student_data[i]={}
		student_data[i]['id']= randint(1, 100)
		student_data[i]['name']= fake.name()
		student_data[i]['address']= fake.address()
		student_data[i]['latitude']= str(fake.latitude())
		student_data[i]['longitude']= str(fake.longitude())
	print(student_data)

	# dictionary dumped as json in a json file
	with open('students.json', 'w') as fp:
		json.dump(student_data, fp)
	

def main():

	# Enter number of students
	# For the above task make this 100
	number_of_students = 10
	input_data(number_of_students)
main()
# The folder or location where this python code
# is save there a students.json will be created
# having 10 students data.
