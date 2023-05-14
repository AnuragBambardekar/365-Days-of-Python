from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'gender', 'major', 'GPA'])

students = []
students.append(Student('Alice', 20, 'F', 'Computer Science', 3.8))
students.append(Student('Bob', 21, 'M', 'Electrical Engineering', 3.6))
students.append(Student('Charlie', 19, 'M', 'Psychology', 3.9))

for student in students:
    print(f"{student.name} is a {student.age}-year-old {student.gender} studying {student.major} with a GPA of {student.GPA}")
