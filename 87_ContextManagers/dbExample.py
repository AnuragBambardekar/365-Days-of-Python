import sqlite3
from contextlib import contextmanager

@contextmanager
def db_connection(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    yield cursor
    conn.commit()
    print("Table values:")
    cursor.execute('SELECT * FROM person')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

with db_connection("87_ContextManagers/mydb.db") as c:
    c.execute("CREATE TABLE IF NOT EXISTS person ("
              "name VARCHAR(255),"
              "age INT);")
    # Define a SQL query to insert data into a table
    query = "INSERT INTO person (name, age) VALUES (?, ?)"

    # Define the data to be inserted as a tuple
    data = ('robert', '20')
    c.execute(query, data)