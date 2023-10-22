import sqlite3

# Define the database file name
database_file = 'invitee_database.db'

# Function to insert invitee data into the database
def insert_invitee_data(conn, data):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO invitees (Salutation, first_name, last_name, job_title)
        VALUES (?, ?, ?, ?)
    ''', data)
    conn.commit()

# Sample invitee data for 10 invitees
invitee_data = [
    ("Mr", "John", "Doe", "Engineer"),
    ("Ms", "Jane", "Smith", "Manager"),
    ("Dr", "David", "Johnson", "Consultant"),
    ("Mrs", "Emily", "Wilson", "Designer"),
    ("Mr", "Michael", "Brown", "Developer"),
    ("Miss", "Sophia", "Davis", "Analyst"),
    ("Mr", "William", "Evans", "Director"),
    ("Ms", "Olivia", "Martinez", "Coordinator"),
    ("Mrs", "Isabella", "Harris", "Supervisor"),
    ("Mr", "James", "Garcia", "Architect"),
]

# Create a database connection
conn = sqlite3.connect(database_file)

# Insert invitee data for all 10 invitees
for data in invitee_data:
    insert_invitee_data(conn, data)

# Close the database connection
conn.close()

print("Invitee data inserted into the database.")
