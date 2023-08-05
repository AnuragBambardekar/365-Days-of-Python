from pprint import pprint

# Sample dictionary with various types of values
person_info = {
    "name": "John Doe",
    "age": 28,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "zipcode": "12345"
    },
    "contacts": {
        "email": "john@example.com",
        "phone": {
            "home": "555-1234",
            "work": "555-5678"
        }
    },
    "is_student": False,
    "grades": [85, 92, 78, 95],
    "favorite_books": ("The Great Gatsby", "To Kill a Mockingbird"),
    "skills": ["Python", "JavaScript", "SQL"],
    "interests": {"hiking", "photography", "cooking"}
}

pprint(person_info)

# Sample list
fruits = ["apple", "banana", "orange", "grape"]

pprint(fruits)

# Sample tuple
coordinates = (10, 20)

pprint(coordinates)