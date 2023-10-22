import sqlite3

# Define the database file name
database_file = 'invitee_database.db'

# Create a database connection
conn = sqlite3.connect(database_file)
cursor = conn.cursor()

# Create a table to store invitee information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS invitees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Salutation TEXT,
        first_name TEXT,
        last_name TEXT,
        job_title TEXT
    )
''')

# Commit changes and close the database connection
conn.commit()
conn.close()

print("Database and table created successfully.")
